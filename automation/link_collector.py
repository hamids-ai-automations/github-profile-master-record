"""External link discovery plus GitHub Pages / live-site detection.

Every link is stored with its relationship to the resource it came from, and
nothing is invented: unknown values stay ``None``.
"""
from __future__ import annotations

import re
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Dict, List, Optional

from github_client import GitHubClient, GitHubError

IGNORED_HOST_PATTERNS = (
    "img.shields.io", "shields.io", "user-images.githubusercontent.com",
    "camo.githubusercontent.com", "badgen.net", "travis-ci.org",
    "travis-ci.com", "circleci.com/gh", "codecov.io", "coveralls.io",
    "github.com/login", "docs.github.com/en/actions",
)


def _clean_url(url: str) -> str:
    return url.strip().rstrip(".,;:)\"'").rstrip("/")


def _is_noise(url: str) -> bool:
    lowered = url.lower()
    return any(pattern in lowered for pattern in IGNORED_HOST_PATTERNS)


def _classify(url: str) -> str:
    lowered = url.lower()
    if "github.com" in lowered:
        return "github"
    if "docs." in lowered or "/docs" in lowered:
        return "documentation"
    if "api." in lowered:
        return "api"
    if any(host in lowered for host in ("vercel.app", "netlify.app", "web.app",
                                        "firebaseapp.com", "github.io", "herokuapp.com",
                                        "streamlit.app", "pages.dev", "workers.dev")):
        return "live_site"
    if "youtube.com" in lowered or "youtu.be" in lowered:
        return "video"
    if "linkedin.com" in lowered or "twitter.com" in lowered or "x.com" in lowered:
        return "social"
    return "website"


def _fetch_pages_info(client: GitHubClient, full_name: str) -> Optional[Dict[str, Any]]:
    data = client.get(f"/repos/{full_name}/pages", allow_404=True)
    if not data:
        return None
    return {
        "url": data.get("html_url"),
        "status": data.get("status"),
        "cname": data.get("cname"),
        "custom_404": data.get("custom_404"),
        "source": (data.get("source") or {}).get("branch"),
        "source_path": (data.get("source") or {}).get("path"),
        "build_type": data.get("build_type"),
        "public": data.get("public"),
    }


def _repo_page_facts(client: GitHubClient, repo: Dict[str, Any]):
    """Return (pages_info, custom_domain) for one repository in two calls."""
    full_name = repo.get("full_name")
    pages_info = _fetch_pages_info(client, full_name)
    domain = ""
    cname = client.get(f"/repos/{full_name}/contents/CNAME", allow_404=True)
    if isinstance(cname, dict) and cname.get("content"):
        try:
            import base64
            domain = base64.b64decode(cname["content"]).decode("utf-8", "replace").strip()
        except Exception:  # noqa: BLE001
            domain = ""
    return pages_info, domain


def collect_links(client: GitHubClient, profile: Dict[str, Any],
                  repositories: List[Dict[str, Any]]) -> Dict[str, Any]:
    links: List[Dict[str, Any]] = []
    seen: Dict[str, Dict[str, Any]] = {}

    def add(url: Optional[str], relationship: str, source: str,
            related: Optional[str] = None, kind: Optional[str] = None) -> None:
        if not url:
            return
        url = _clean_url(url)
        if not url.startswith("http") or _is_noise(url):
            return
        key = url.lower()
        if key in seen:
            existing = seen[key]
            if relationship not in existing["relationships"]:
                existing["relationships"].append(relationship)
            if related and related not in existing["related_resources"]:
                existing["related_resources"].append(related)
            return
        entry = {
            "url": url,
            "type": kind or _classify(url),
            "relationships": [relationship],
            "related_resources": [related] if related else [],
            "source": source,
            "verified": None,
        }
        seen[key] = entry
        links.append(entry)

    details = profile.get("profile_details") or {}
    add(details.get("website_url"), "profile_website", "profile bio website field")
    for account in details.get("social_accounts") or []:
        add(account.get("url"), "social_account", f"profile social account ({account.get('provider')})")
    for url in profile.get("profile_readme_links") or []:
        add(url, "profile_readme_link", "profile README")

    pages: List[Dict[str, Any]] = []
    # Two calls per repository are the bulk of this collector; fetch them
    # concurrently so a full run stays in the low minutes.
    with ThreadPoolExecutor(max_workers=8) as pool:
        facts = list(pool.map(lambda r: _repo_page_facts(client, r), repositories))
    for repo, (pages_info, domain) in zip(repositories, facts):
        full_name = repo.get("full_name")
        add(repo.get("homepage"), "repository_homepage", f"repository {full_name}",
            related=full_name, kind="live_site" if repo.get("homepage") else None)
        for url in repo.get("external_links") or []:
            add(url, "repository_readme_link", f"README of {full_name}", related=full_name)

        if pages_info and pages_info.get("url"):
            pages.append({
                "repository": full_name,
                "url": pages_info.get("url"),
                "status": pages_info.get("status"),
                "cname": pages_info.get("cname"),
                "source_branch": pages_info.get("source"),
                "source_path": pages_info.get("source_path"),
                "build_type": pages_info.get("build_type"),
            })
            add(pages_info.get("url"), "github_pages", f"GitHub Pages of {full_name}",
                related=full_name, kind="live_site")
        # Detect CNAME / index.html hosted sites even when Pages API is empty
        if domain:
            add(f"https://{domain}", "custom_domain", f"CNAME file in {full_name}",
                related=full_name, kind="live_site")

    return {
        "external_links": links,
        "github_pages": pages,
        "summary": {
            "total_links": len(links),
            "live_sites": sum(1 for l in links if l["type"] == "live_site"),
            "documentation_links": sum(1 for l in links if l["type"] == "documentation"),
            "github_pages_sites": len(pages),
        },
    }


def collect_releases(repositories: List[Dict[str, Any]]) -> Dict[str, Any]:
    releases = []
    for repo in repositories:
        for rel in repo.get("releases") or []:
            releases.append({
                "repository": repo.get("full_name"),
                "name": rel.get("name"),
                "tag_name": rel.get("tag_name"),
                "url": rel.get("url"),
                "published_at": rel.get("published_at"),
                "is_prerelease": rel.get("is_prerelease"),
            })
    releases.sort(key=lambda r: r.get("published_at") or "", reverse=True)
    return {"releases": releases, "count": len(releases)}


def build_technology_stack(repositories: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    language_bytes: Dict[str, int] = {}
    frameworks: Dict[str, List[str]] = {}
    for repo in repositories:
        for name, size in (repo.get("languages") or {}).items():
            language_bytes[name] = language_bytes.get(name, 0) + int(size or 0)
        for fw in (repo.get("technology") or {}).get("frameworks", []):
            frameworks.setdefault(fw, []).append(repo.get("name"))
    total = sum(language_bytes.values()) or 1
    stack = [{
        "name": name,
        "category": "language",
        "total_bytes": size,
        "percentage": round(size * 100 / total, 2),
        "repository_count": sum(1 for r in repositories if name in (r.get("languages") or {})),
    } for name, size in sorted(language_bytes.items(), key=lambda kv: -kv[1])]
    stack += [{
        "name": fw,
        "category": "framework",
        "total_bytes": None,
        "percentage": None,
        "repository_count": len(set(repos)),
        "repositories": sorted(set(repos))[:20],
    } for fw, repos in sorted(frameworks.items(), key=lambda kv: -len(set(kv[1])))]
    return stack
