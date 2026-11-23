"""Idempotent change detection between the previous and the freshly collected
snapshot. Enables incremental, non-duplicating updates and changelog entries.
"""
from __future__ import annotations

import hashlib
from typing import Any, Dict, List, Optional

REPO_TRACKED_FIELDS = (
    "description", "homepage", "stars", "forks", "watchers", "open_issues",
    "closed_issues", "open_pull_requests", "merged_pull_requests", "releases_count",
    "pushed_at", "updated_at", "default_branch", "language", "languages", "topics",
    "archived", "visibility", "license", "fork", "has_discussions",
)

PROFILE_TRACKED_FIELDS = (
    "display_name", "bio", "company", "location", "public_email", "website_url",
    "twitter_username", "social_accounts", "status",
)


def _hash(value: Any) -> str:
    return hashlib.sha256(repr(value).encode("utf-8")).hexdigest()[:16]


def detect_changes(old_db: Optional[Dict[str, Any]],
                   new_db: Dict[str, Any]) -> Dict[str, Any]:
    changes: List[Dict[str, Any]] = []
    if not old_db:
        changes.append({
            "type": "initial_snapshot",
            "resource": "database",
            "summary": "First full snapshot of the profile created.",
            "fields": {},
        })
        return {"changes": changes, "has_changes": True, "is_initial": True}

    # ---------------------------------------------------------------- profile
    old_profile = (old_db.get("profile") or {}).get("profile_details") or {}
    new_profile = (new_db.get("profile") or {}).get("profile_details") or {}
    profile_diff: Dict[str, Any] = {}
    for field in PROFILE_TRACKED_FIELDS:
        if _hash(old_profile.get(field)) != _hash(new_profile.get(field)):
            profile_diff[field] = {"old": old_profile.get(field), "new": new_profile.get(field)}
    old_readme = (old_profile.get("profile_readme") or {}).get("content")
    new_readme = (new_profile.get("profile_readme") or {}).get("content")
    if _hash(old_readme) != _hash(new_readme):
        profile_diff["profile_readme"] = {
            "old": (old_readme or "")[:200] or None,
            "new": (new_readme or "")[:200] or None,
        }
    if profile_diff:
        changes.append({
            "type": "profile_updated",
            "resource": "profile",
            "summary": "Profile information changed: " + ", ".join(sorted(profile_diff)),
            "fields": {k: v for k, v in profile_diff.items()},
        })

    # ---------------------------------------------------------------- repositories
    old_repos = {r.get("full_name"): r for r in (old_db.get("repositories") or [])}
    new_repos = {r.get("full_name"): r for r in (new_db.get("repositories") or [])}

    for name, repo in new_repos.items():
        if name not in old_repos:
            changes.append({
                "type": "repository_added",
                "resource": name,
                "url": repo.get("url"),
                "summary": f"New repository discovered: {name}",
                "fields": {},
            })
            continue
        old = old_repos[name]
        diff: Dict[str, Any] = {}
        for field in REPO_TRACKED_FIELDS:
            if _hash(old.get(field)) != _hash(repo.get(field)):
                old_value, new_value = old.get(field), repo.get(field)
                if field == "languages" and isinstance(old_value, dict) and isinstance(new_value, dict):
                    old_value = list(old_value.keys())
                    new_value = list(new_value.keys())
                diff[field] = {"old": old_value, "new": new_value}
        old_readme_len = (old.get("readme") or {}).get("length")
        new_readme_len = (repo.get("readme") or {}).get("length")
        if old_readme_len != new_readme_len:
            diff["readme"] = {"old": old_readme_len, "new": new_readme_len}
        if diff:
            changes.append({
                "type": "repository_updated",
                "resource": name,
                "url": repo.get("url"),
                "summary": f"{name} updated: " + ", ".join(sorted(diff)),
                "fields": diff,
            })

    for name in old_repos:
        if name not in new_repos:
            changes.append({
                "type": "repository_missing",
                "resource": name,
                "url": old_repos[name].get("url"),
                "summary": f"{name} was not returned by the API (deleted, renamed or made private). "
                           f"The historical record is preserved, not deleted.",
                "fields": {},
            })

    # ---------------------------------------------------------------- gists / links / releases / pages
    for key, label in (("gists", "gist"), ("github_pages", "GitHub Pages site"),
                       ("releases", "release")):
        old_items = {(i.get("id") or i.get("url") or i.get("repository", "") + str(i.get("tag_name")))
                     for i in (old_db.get(key) or [])}
        new_items = {(i.get("id") or i.get("url") or i.get("repository", "") + str(i.get("tag_name")))
                     for i in (new_db.get(key) or [])}
        added = new_items - old_items
        if added:
            changes.append({
                "type": f"{key}_added",
                "resource": key,
                "summary": f"{len(added)} new {label}(s) discovered.",
                "fields": {"added": sorted(str(a) for a in added)[:20]},
            })

    old_links = {l.get("url") for l in (old_db.get("external_links") or [])}
    new_links = {l.get("url") for l in (new_db.get("external_links") or [])}
    added_links = new_links - old_links
    if added_links:
        changes.append({
            "type": "external_links_added",
            "resource": "external_links",
            "summary": f"{len(added_links)} new external link(s) discovered.",
            "fields": {"added": sorted(added_links)[:20]},
        })

    # ---------------------------------------------------------------- contributions
    old_contrib = {c.get("id") or c.get("url") for c in (old_db.get("contributions") or [])}
    new_contrib = {c.get("id") or c.get("url") for c in (new_db.get("contributions") or [])}
    new_prs = new_contrib - old_contrib
    if new_prs:
        changes.append({
            "type": "contributions_updated",
            "resource": "contributions",
            "summary": f"{len(new_prs)} new pull request / issue record(s) detected.",
            "fields": {"added": sorted(str(x) for x in new_prs)[:20]},
        })

    return {"changes": changes, "has_changes": bool(changes), "is_initial": False}


def merge_history(old_db: Optional[Dict[str, Any]], new_db: Dict[str, Any],
                  change_report: Dict[str, Any], timestamp: str) -> Dict[str, Any]:
    """Preserve historical information and append the change entry."""
    history: List[Dict[str, Any]] = []
    if old_db:
        history.extend(old_db.get("change_history") or [])
    for change in change_report.get("changes") or []:
        entry = dict(change)
        entry["detected_at"] = timestamp
        history.append(entry)
    new_db["change_history"] = history[-1000:]
    return new_db
