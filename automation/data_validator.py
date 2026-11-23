"""Data quality validation: schema conformance, duplicate detection,
completeness accounting and markdown link checking.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import re
from typing import Any, Dict, List

REQUIRED_TOP_LEVEL = (
    "profile", "repositories", "projects", "contributions", "external_links",
    "gists", "github_pages", "releases", "achievements", "technology_stack",
    "change_history", "data_quality",
)

REQUIRED_REPOSITORY_FIELDS = (
    "id", "name", "full_name", "url", "description", "created_at", "updated_at",
    "pushed_at", "default_branch", "visibility", "archived", "fork", "license",
    "language", "languages", "stars", "forks", "watchers", "open_issues",
)


def validate_database(db: Dict[str, Any]) -> Dict[str, Any]:
    errors: List[str] = []
    warnings: List[str] = []

    for key in REQUIRED_TOP_LEVEL:
        if key not in db:
            errors.append(f"missing top-level key: {key}")

    repos = db.get("repositories") or []
    ids, names = set(), set()
    for repo in repos:
        for field in REQUIRED_REPOSITORY_FIELDS:
            if field not in repo:
                errors.append(f"repository {repo.get('full_name')} missing field: {field}")
        rid = repo.get("id")
        if rid in ids:
            errors.append(f"duplicate repository id: {rid}")
        ids.add(rid)
        if repo.get("full_name") in names:
            errors.append(f"duplicate repository full_name: {repo.get('full_name')}")
        names.add(repo.get("full_name"))
        if not repo.get("url"):
            errors.append(f"repository {repo.get('name')} missing source URL")
        if not repo.get("readme", {}).get("has_readme"):
            warnings.append(f"repository {repo.get('full_name')} has no README")

    links = db.get("external_links") or []
    for link in links:
        if not link.get("url"):
            errors.append("external link without URL")
        if not link.get("relationships"):
            errors.append(f"external link {link.get('url')} has no relationship")

    for pr in (db.get("contributions") or []):
        if not pr.get("repository"):
            warnings.append(f"contribution record without repository: {pr.get('url')}")

    # JSON round-trip guarantee
    try:
        json.dumps(db)
    except (TypeError, ValueError) as exc:
        errors.append(f"database is not JSON serialisable: {exc}")

    quality = db.get("data_quality") or {}
    total_discovered = quality.get("total_repositories_discovered") or len(repos)
    total_documented = sum(1 for r in repos if r.get("documentation_status") == "documented")
    if total_documented > total_discovered:
        errors.append("documented repositories exceed discovered repositories")

    return {
        "valid": not errors,
        "errors": errors,
        "warnings": warnings,
        "counts": {
            "repositories": len(repos),
            "repositories_documented": total_documented,
            "projects": len(db.get("projects") or []),
            "contributions": len(db.get("contributions") or []),
            "external_links": len(links),
            "gists": len(db.get("gists") or []),
            "github_pages": len(db.get("github_pages") or []),
            "releases": len(db.get("releases") or []),
            "achievements": len(db.get("achievements") or []),
        },
    }


def check_markdown_links(root: str) -> Dict[str, Any]:
    """Verify that relative markdown links inside generated docs resolve."""
    broken: List[str] = []
    checked = 0
    pattern = re.compile(r"\[[^\]]*\]\((?!https?://|#)([^)]+)\)")
    for dirpath, _dirnames, filenames in os.walk(root):
        if f"{os.sep}.git" in dirpath:
            continue
        for filename in filenames:
            if not filename.endswith(".md"):
                continue
            full = os.path.join(dirpath, filename)
            with open(full, "r", encoding="utf-8") as handle:
                text = handle.read()
            for target in pattern.findall(text):
                target = target.split("#")[0].strip()
                if not target:
                    continue
                checked += 1
                resolved = os.path.normpath(os.path.join(dirpath, target))
                if not os.path.exists(resolved):
                    broken.append(f"{os.path.relpath(full, root)} -> {target}")
    return {"checked": checked, "broken": broken, "valid": not broken}


def csv_safety(value: Any) -> str:
    if value is None:
        return ""
    text = str(value)
    if any(ch in text for ch in (",", '"', "\n")):
        text = '"' + text.replace('"', '""') + '"'
    return text


def _load_db(root: str) -> Dict[str, Any]:
    with open(os.path.join(root, "MASTER_DATABASE.json"), "r", encoding="utf-8") as handle:
        return json.load(handle)


def _check_csv(root: str) -> Dict[str, Any]:
    """Every CSV must parse with a stable header and non-ragged rows."""
    problems: List[str] = []
    checked = 0
    for dirpath, _dirnames, filenames in os.walk(root):
        if f"{os.sep}.git" in dirpath:
            continue
        for filename in filenames:
            if not filename.endswith(".csv"):
                continue
            path = os.path.join(dirpath, filename)
            rel = os.path.relpath(path, root)
            with open(path, "r", encoding="utf-8", newline="") as handle:
                rows = list(csv.reader(handle))
            checked += 1
            if not rows:
                problems.append(f"{rel}: empty CSV")
                continue
            width = len(rows[0])
            for index, row in enumerate(rows[1:], start=2):
                if len(row) != width:
                    problems.append(f"{rel}: ragged row {index} ({len(row)} vs {width})")
    return {"csv_files_checked": checked, "problems": problems}


def _check_json(root: str) -> Dict[str, Any]:
    problems: List[str] = []
    checked = 0
    for dirpath, _dirnames, filenames in os.walk(root):
        if f"{os.sep}.git" in dirpath:
            continue
        for filename in filenames:
            if not filename.endswith(".json"):
                continue
            path = os.path.join(dirpath, filename)
            rel = os.path.relpath(path, root)
            checked += 1
            try:
                with open(path, "r", encoding="utf-8") as handle:
                    json.load(handle)
            except Exception as exc:  # noqa: BLE001
                problems.append(f"{rel}: invalid JSON ({exc})")
    return {"json_files_checked": checked, "problems": problems}


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Validate master database, JSON and CSV integrity")
    parser.add_argument("--root", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    parser.add_argument("--strict", action="store_true", help="warnings also fail the build")
    args = parser.parse_args(argv)

    db = _load_db(args.root)
    result = validate_database(db)
    json_check = _check_json(args.root)
    csv_check = _check_csv(args.root)
    links = check_markdown_links(args.root)

    print(f"[validate] JSON files: {json_check['json_files_checked']} "
          f"(problems: {len(json_check['problems'])})")
    print(f"[validate] CSV files: {csv_check['csv_files_checked']} "
          f"(problems: {len(csv_check['problems'])})")
    print(f"[validate] markdown links checked: {links.get('checked')} "
          f"broken: {len(links.get('broken') or [])}")
    print(f"[validate] database errors: {len(result.get('errors') or [])} "
          f"warnings: {len(result.get('warnings') or [])}")

    problems = (json_check["problems"] + csv_check["problems"]
                + (links.get("broken") or []) + (result.get("errors") or []))
    for problem in problems[:40]:
        print(f"  ERROR {problem}")
    for warning in (result.get("warnings") or [])[:40]:
        print(f"  WARN  {warning}")

    failed = bool(problems) or (args.strict and bool(result.get("warnings")))
    print("[validate] RESULT:", "FAILED" if failed else "PASSED")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
