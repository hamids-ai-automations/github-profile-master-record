"""Main entry point: build, validate and regenerate the master record.

Usage:
    python automation/sync.py --mode full          # complete rebuild
    python automation/sync.py --mode incremental   # hourly lightweight update
    python automation/sync.py --mode audit         # full sync + validation report
    python automation/sync.py --dry-run            # collect and validate, write nothing
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

from change_detector import detect_changes, merge_history
from contribution_collector import collect_contributions
from data_validator import check_markdown_links, validate_database
from generator import render_all
from github_client import AuthError, GitHubClient
from link_collector import (build_technology_stack, collect_links, collect_releases)
from profile_collector import collect_achievements, collect_profile
from repository_collector import collect_contributed_repositories, collect_repositories

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASE_PATH = os.path.join(ROOT, "MASTER_DATABASE.json")
SCHEMA_VERSION = "1.0.0"


def now_utc() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def load_previous() -> Optional[Dict[str, Any]]:
    if not os.path.exists(DATABASE_PATH):
        return None
    try:
        with open(DATABASE_PATH, "r", encoding="utf-8") as handle:
            return json.load(handle)
    except (json.JSONDecodeError, OSError) as exc:
        print(f"[sync] previous database unreadable ({exc}); treating as first run")
        return None


def build_contributions(contrib) -> tuple[List[Dict[str, Any]], Dict[str, Any]]:
    records: List[Dict[str, Any]] = []
    for pr in contrib.get("pull_requests") or []:
        record = dict(pr)
        record["pull_request_or_issue"] = "pull_request"
        record["relationship"] = "authored"
        records.append(record)
    for issue in contrib.get("issues") or []:
        record = dict(issue)
        record["pull_request_or_issue"] = "issue"
        record["relationship"] = "authored"
        records.append(record)
    summary = contrib.get("summary") or {}
    return records, summary


def write_json_atomic(path: str, data: Any) -> None:
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as handle:
        json.dump(data, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
    os.replace(tmp, path)


def save_snapshot(db: Dict[str, Any], mode: str, timestamp: str) -> None:
    stamp = timestamp.replace(":", "").replace("-", "")[:15]
    is_full = mode in ("full", "audit")
    if is_full:
        target = os.path.join(ROOT, "history", "snapshots", f"{stamp}_full.json")
        payload: Any = {k: v for k, v in db.items() if k != "readme_full_content"}
    else:
        target = os.path.join(ROOT, "history", "snapshots", f"{stamp}_light.json")
        payload = {
            "timestamp": timestamp,
            "mode": mode,
            "repositories": [{
                "full_name": r.get("full_name"), "stars": r.get("stars"),
                "forks": r.get("forks"), "pushed_at": r.get("pushed_at"),
                "description": r.get("description"), "language": r.get("language"),
            } for r in db.get("repositories") or []],
        }
    os.makedirs(os.path.dirname(target), exist_ok=True)
    write_json_atomic(target, payload)


def prune_snapshots(keep_light: int = 72, keep_full: int = 60) -> None:
    folder = os.path.join(ROOT, "history", "snapshots")
    if not os.path.isdir(folder):
        return
    for kind, keep in (("light", keep_light), ("full", keep_full)):
        files = sorted(f for f in os.listdir(folder) if f.endswith(f"_{kind}.json"))
        for stale in files[:-keep] if len(files) > keep else []:
            os.remove(os.path.join(folder, stale))


def _strip_readme_bodies(db: Dict[str, Any]) -> Dict[str, Any]:
    """Return a copy of the database with README bodies removed.

    Full README text lives in ``projects/individual_projects/*.md``; keeping a
    second copy in the canonical JSON triples the file size and slows every
    hourly diff, so only the excerpt stays in the database.
    """
    import copy
    trimmed = copy.deepcopy(db)
    for key in ("repositories",):
        for repo in trimmed.get(key) or []:
            repo["readme_full_content"] = None
    return trimmed


def run(mode: str = "incremental", dry_run: bool = False, trigger: str = "manual",
        token: Optional[str] = None) -> int:
    started = time.time()
    print(f"[sync] mode={mode} dry_run={dry_run} trigger={trigger}")

    client = GitHubClient(token=token)
    try:
        identity = client.identity()
    except AuthError as exc:
        print(f"[sync] FATAL authentication failed: {exc}")
        return 2

    login = identity.get("login")
    token_scopes = ", ".join(identity.get("scopes") or []) or "unknown"
    print(f"[sync] authenticated as {login} (token scopes: {token_scopes})")

    previous = load_previous()
    failures: List[str] = []

    print("[sync] collecting profile ...")
    profile = collect_profile(client, login)

    print("[sync] collecting repositories ...")
    repo_block = collect_repositories(
        client, login,
        previous_repositories=(previous or {}).get("repositories") or [],
        light=mode == "incremental",
    )
    owned = repo_block["owned"]
    forked = repo_block["forked"]
    repositories = owned + forked

    achievements_block = collect_achievements(client, login, repositories)
    profile["achievements"] = achievements_block.get("badges") or []
    profile["achievements_highlights"] = achievements_block.get("highlights") or {}
    profile["achievements_source"] = achievements_block.get("source_url")

    print("[sync] collecting contributions ...")
    contrib = collect_contributions(client, login)
    contributions, contribution_summary = build_contributions(contrib)
    contributed_repos = collect_contributed_repositories(client, login)

    print("[sync] collecting links, pages, releases, gists ...")
    link_block = collect_links(client, profile, repositories)
    releases = collect_releases(repositories)
    from contribution_collector import collect_gists, collect_packages
    gists = collect_gists(client, login)
    try:
        packages = collect_packages(client, login)
    except Exception as exc:  # noqa: BLE001
        packages = {"packages": [], "count": 0}
        failures.append(f"packages unavailable: {exc}")

    if profile.get("errors"):
        failures.extend(profile["errors"])

    technology_stack = build_technology_stack(repositories)
    timestamp = now_utc()

    projects = [{
        "name": r.get("name"),
        "full_name": r.get("full_name"),
        "url": r.get("url"),
        "documentation": None,
        "status": "archived" if r.get("archived") else ("fork" if r.get("fork") else "active"),
    } for r in repositories]

    documented = sum(1 for r in repositories if r.get("readme", {}).get("has_readme"))
    missing_fields = []
    for repo in repositories:
        if not repo.get("description"):
            missing_fields.append(f"{repo.get('full_name')}: description")
    coverage = round(documented * 100 / len(repositories), 2) if repositories else 0.0

    db: Dict[str, Any] = {
        "metadata": {
            "schema_version": SCHEMA_VERSION,
            "username": login,
            "generated_at": timestamp,
            "source": "GitHub REST API v3 + GraphQL API v4",
            "generator": "github-profile-master-record/automation/sync.py",
            "canonical": True,
            "mode": mode,
            "trigger": trigger,
        },
        "profile": profile,
        "repositories": repositories,
        "projects": projects,
        "contributions": contributions,
        "contribution_summary": contribution_summary,
        "reviews": contrib.get("reviews"),
        "discussions": contrib.get("discussions"),
        "commits": contrib.get("commits"),
        "contributed_repositories": contributed_repos,
        "external_links": link_block["external_links"],
        "github_pages": link_block["github_pages"],
        "releases": releases["releases"],
        "gists": gists,
        "packages": packages,
        "achievements": profile.get("achievements") or [],
        "technology_stack": technology_stack,
        "change_history": [],
        "data_quality": {
            "total_repositories_discovered": len(repositories),
            "total_repositories_documented": documented,
            "documentation_coverage_percent": coverage,
            "repositories_without_description": len(missing_fields),
            "total_projects": len(projects),
            "total_contributions": len(contributions),
            "total_external_links": len(link_block["external_links"]),
            "total_gists": len(gists),
            "total_releases": len(releases["releases"]),
            "total_packages": (packages or {}).get("count", 0),
            "missing_optional_fields": missing_fields[:50],
            "unavailable_sources": failures,
            "validation_errors": 0,
            "validation_warnings": 0,
            "last_validated": timestamp,
        },
    }

    change_report = detect_changes(previous, db)
    db = merge_history(previous, db, change_report, timestamp)
    validation = validate_database(db)
    db["data_quality"]["validation_errors"] = len(validation["errors"])
    db["data_quality"]["validation_warnings"] = len(validation["warnings"])

    stats = client.stats()
    run_info = {
        "mode": mode,
        "trigger": trigger,
        "api_requests": stats["requests"],
        "failed_requests": stats["failures"],
        "duration_seconds": round(time.time() - started, 1),
        "failures": failures + validation["errors"][:20],
    }
    db["profile"]["last_synced"] = timestamp
    db["metadata"]["run"] = run_info

    print(f"[sync] repositories={len(repositories)} documented={documented} "
          f"changes={len(change_report['changes'])} "
          f"validation_errors={len(validation['errors'])} warnings={len(validation['warnings'])}")

    if dry_run:
        print("[sync] dry-run: nothing written")
        print(json.dumps(validation, indent=2)[:4000])
        return 0

    db_for_disk = _strip_readme_bodies(db)
    write_json_atomic(DATABASE_PATH, db_for_disk)
    render_all(db, ROOT, change_report, run_info, timestamp)

    os.makedirs(os.path.join(ROOT, "history", "changes"), exist_ok=True)
    change_file = os.path.join(
        ROOT, "history", "changes",
        timestamp.replace(":", "").replace("-", "")[:15] + "_changes.json")
    write_json_atomic(change_file, {
        "timestamp": timestamp, "mode": mode, "trigger": trigger,
        "changes": change_report["changes"],
    })

    save_snapshot(db_for_disk, mode, timestamp)
    prune_snapshots()

    links = check_markdown_links(ROOT)
    if links["broken"]:
        print(f"[sync] WARNING: {len(links['broken'])} broken internal documentation link(s)")
        for item in links["broken"][:10]:
            print(f"        {item}")

    print(f"[sync] done in {run_info['duration_seconds']}s — "
          f"{stats['requests']} API requests, {stats['failures']} failures")

    if validation["errors"]:
        print("[sync] validation errors:")
        for error in validation["errors"][:20]:
            print(f"        - {error}")
        return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="GitHub profile master record sync")
    parser.add_argument("--mode", default="incremental",
                        choices=["incremental", "full", "audit", "initial"])
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--trigger", default="manual")
    parser.add_argument("--token", default=None,
                        help="GitHub token; defaults to GITHUB_TOKEN / GH_TOKEN env var")
    parser.add_argument("--require-changes", action="store_true",
                        help="exit code 3 when nothing changed (used by CI)")
    args = parser.parse_args()
    code = run(mode=args.mode, dry_run=args.dry_run, trigger=args.trigger, token=args.token)
    return code


if __name__ == "__main__":
    sys.exit(main())
