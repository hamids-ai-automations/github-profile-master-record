"""Render every human-readable artifact from MASTER_DATABASE.json.

MASTER_DATABASE.json is the single canonical source; Markdown, CSV, dashboards
and reports are generated from it so they can never drift apart.
"""
from __future__ import annotations

import csv
import json
import os
import re
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


def slugify(name: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", (name or "").lower()).strip("-")
    return slug or "unnamed"


def _write(root: str, relative: str, content: str) -> None:
    path = os.path.join(root, relative)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(content if content.endswith("\n") else content + "\n")


def _write_json(root: str, relative: str, data: Any) -> None:
    _write(root, relative, json.dumps(data, indent=2, ensure_ascii=False, sort_keys=False))


def _md_escape(text: Any) -> str:
    if text is None:
        return "-"
    return str(text).replace("|", "\\|").replace("\n", " ")


def _fmt_date(value: Optional[str]) -> str:
    if not value:
        return "-"
    return str(value)[:10]


def _repo_table(repos: List[Dict[str, Any]]) -> str:
    lines = [
        "| Repository | Description | Language | Stars | Forks | Status | Last push |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for repo in repos:
        status = "archived" if repo.get("archived") else ("fork" if repo.get("fork") else "active")
        lines.append(
            f"| [{_md_escape(repo.get('name'))}]({repo.get('url')}) "
            f"| {_md_escape(repo.get('description'))} "
            f"| {_md_escape(repo.get('language'))} "
            f"| {repo.get('stars') if repo.get('stars') is not None else 0} "
            f"| {repo.get('forks') if repo.get('forks') is not None else 0} "
            f"| {status} "
            f"| {_fmt_date(repo.get('pushed_at'))} |"
        )
    return "\n".join(lines)


# --------------------------------------------------------------------------- profile
def render_profile(db: Dict[str, Any], root: str) -> None:
    profile = db["profile"]
    details = profile["profile_details"]
    stats = profile["statistics"]
    readme = details.get("profile_readme") or {}

    _write_json(root, "profile/profile_details.json", details)
    detail_lines = ["# Profile Details", "", f"Source: {details.get('profile_url')}", "",
                    "| Field | Value |", "| --- | --- |"]
    for key, label in (("username", "Username"), ("display_name", "Display name"),
                       ("bio", "Bio"), ("company", "Company"), ("location", "Location"),
                       ("email", "Public email"), ("blog", "Website"), ("twitter", "Twitter"),
                       ("followers", "Followers"), ("following", "Following"),
                       ("public_repos", "Public repositories"), ("public_gists", "Public gists"),
                       ("account_created", "Account created"), ("account_updated", "Last updated"),
                       ("avatar_url", "Avatar"), ("profile_url", "Profile URL")):
        detail_lines.append(f"| {label} | {_md_escape(details.get(key))} |")
    social = details.get("social_accounts") or []
    if social:
        detail_lines += ["", "## Social accounts", "", "| Provider | URL |", "| --- | --- |"]
        detail_lines += [f"| {_md_escape(item.get('provider'))} | {item.get('url')} |" for item in social]
    _write(root, "profile/profile_details.md", "\n".join(detail_lines))
    _write_json(root, "profile/profile_statistics.json", stats)
    _write_json(root, "profile/pinned_repositories.json", profile.get("pinned_repositories") or [])
    _write(root, "profile/profile_readme.md",
           "# Profile README (source of truth)\n\n"
           f"Source: {readme.get('html_url') or details.get('profile_url')}\n\n"
           "```markdown\n" + (readme.get("content") or "(no profile README)") + "\n```\n")

    lines = [
        f"# {details.get('display_name') or details.get('username')} — GitHub Profile",
        "",
        f"- **Username:** `{details.get('username')}`",
        f"- **Profile URL:** {details.get('profile_url')}",
        f"- **Bio:** {details.get('bio') or '- '}",
        f"- **Company:** {details.get('company') or '-'}",
        f"- **Location:** {details.get('location') or '-'}",
        f"- **Website:** {details.get('website_url') or '-'}",
        f"- **Public email:** {details.get('public_email') or '-'}",
        f"- **Twitter/X:** {details.get('twitter_username') or '-'}",
        f"- **Account created:** {_fmt_date(details.get('created_at'))}",
        f"- **Last profile update:** {_fmt_date(details.get('updated_at'))}",
        f"- **Last synchronized:** {profile.get('last_synced')}",
        "",
        "## Statistics",
        "",
        "| Metric | Value |",
        "| --- | --- |",
    ]
    for key, value in stats.items():
        lines.append(f"| {key.replace('_', ' ')} | {value if value is not None else '-'} |")
    lines += ["", "## Social accounts", ""]
    if details.get("social_accounts"):
        lines += [f"- {a.get('provider')}: {a.get('url') or a.get('display_name')}"
                  for a in details["social_accounts"]]
    else:
        lines.append("- none publicly listed")
    lines += ["", "## Organizations", ""]
    if details.get("organizations"):
        lines += [f"- [{o.get('login')}]({o.get('url')})" for o in details["organizations"]]
    else:
        lines.append("- none public")
    lines += ["", "## Pinned repositories", ""]
    if profile.get("pinned_repositories"):
        for pin in profile["pinned_repositories"]:
            lines.append(f"- [{pin.get('name')}]({pin.get('url')}) — "
                         f"{pin.get('description') or 'no description'} "
                         f"({pin.get('stars') or 0} stars, {pin.get('language') or 'n/a'})")
    else:
        lines.append("- none pinned")
    lines += ["", "## Profile README", "", "Full source: [`profile/profile_readme.md`](profile/profile_readme.md)", ""]
    if readme.get("content"):
        lines.append("```markdown")
        lines.append(readme["content"][:6000])
        lines.append("```")
    lines.append("")
    _write(root, "MASTER_PROFILE.md", "\n".join(lines))


# --------------------------------------------------------------------------- repositories
def render_repositories(db: Dict[str, Any], root: str) -> None:
    repos = db["repositories"]
    owned = [r for r in repos if not r.get("fork")]
    forked = [r for r in repos if r.get("fork")]

    _write_json(root, "repositories/repositories_index.json", {
        "generated_from": "MASTER_DATABASE.json",
        "count": len(repos),
        "owned_count": len(owned),
        "forked_count": len(forked),
        "repositories": [{
            "id": r.get("id"), "name": r.get("name"), "full_name": r.get("full_name"),
            "url": r.get("url"), "description": r.get("description"),
            "language": r.get("language"), "stars": r.get("stars"), "forks": r.get("forks"),
            "archived": r.get("archived"), "fork": r.get("fork"),
            "pushed_at": r.get("pushed_at"), "homepage": r.get("homepage"),
            "documentation": f"projects/individual_projects/{slugify(r.get('name'))}.md",
        } for r in repos],
    })

    csv_path = os.path.join(root, "repositories", "repositories_index.csv")
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    fields = ["name", "full_name", "url", "description", "language", "languages",
              "stars", "forks", "watchers", "open_issues", "closed_issues", "fork",
              "archived", "visibility", "license", "created_at", "updated_at",
              "pushed_at", "default_branch", "homepage", "topics", "releases_count"]
    with open(csv_path, "w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for repo in repos:
            row = {k: repo.get(k) for k in fields}
            for key in ("languages", "topics"):
                row[key] = ";".join(row.get(key) or []) if isinstance(row.get(key), (list, dict)) else row.get(key)
            writer.writerow(row)

    for group, items in (("owned_repositories", owned), ("forked_repositories", forked)):
        for repo in items:
            payload = {k: v for k, v in repo.items() if k != "readme_full_content"}
            _write_json(root, f"repositories/{group}/{slugify(repo.get('name'))}.json", payload)

    for entry in (db.get("contributed_repositories") or {}).get("repositories", []):
        _write_json(root, f"repositories/contributed_repositories/{slugify(entry.get('full_name'))}.json", entry)

    # Markdown index
    lines = [
        "# Repository Index",
        "",
        f"Generated from `MASTER_DATABASE.json` — {len(repos)} repositories "
        f"({len(owned)} owned, {len(forked)} forked).",
        "",
        "## Owned repositories",
        "",
        _repo_table(owned) if owned else "_none_",
        "",
        "## Forked repositories",
        "",
        _repo_table(forked) if forked else "_none_",
        "",
    ]
    _write(root, "PROJECT_INDEX.md", "\n".join(lines))


# --------------------------------------------------------------------------- projects
def render_projects(db: Dict[str, Any], root: str) -> None:
    repos = [r for r in db["repositories"]]
    pages_by_repo = {p.get("repository"): p for p in db.get("github_pages") or []}
    links_by_repo: Dict[str, List[str]] = {}
    for link in db.get("external_links") or []:
        for rel in link.get("related_resources") or []:
            links_by_repo.setdefault(rel, []).append(link.get("url"))

    index = []
    for repo in repos:
        slug = slugify(repo.get("name"))
        page = pages_by_repo.get(repo.get("full_name"))
        index.append({
            "name": repo.get("name"),
            "full_name": repo.get("full_name"),
            "url": repo.get("url"),
            "documentation": f"projects/individual_projects/{slug}.md",
            "live_url": (page or {}).get("url") or repo.get("homepage"),
            "language": repo.get("language"),
            "stars": repo.get("stars"),
            "status": "archived" if repo.get("archived") else ("fork" if repo.get("fork") else "active"),
            "is_fork": repo.get("fork"),
        })
    _write_json(root, "projects/projects_index.json", {
        "generated_from": "MASTER_DATABASE.json",
        "count": len(index),
        "projects": index,
    })

    for repo in repos:
        _render_project_doc(db, repo, root, page=pages_by_repo.get(repo.get("full_name")),
                            links=links_by_repo.get(repo.get("full_name"), []))


_LINK_RE = re.compile(r"(!?)\[([^\]]*)\]\(([^)\s]+)((?:\s+\"[^\"]*\")?)\)")


def _absolutize_readme_links(markdown: str, repo: Dict[str, Any]) -> str:
    """Rewrite repository-relative README links to absolute GitHub URLs.

    README bodies are authored against the repository root, so a copied body in
    ``projects/`` would otherwise point at files that do not exist in this tree.
    """
    if not markdown:
        return ""
    full_name = repo.get("full_name") or ""
    branch = repo.get("default_branch") or "main"
    if not full_name:
        return markdown

    def repl(match: "re.Match[str]") -> str:
        bang, label, target, title = match.groups()
        if target.startswith(("http://", "https://", "#", "mailto:", "tel:")):
            return match.group(0)
        path = target.lstrip("/")
        while path.startswith("./"):
            path = path[2:]
        path = path.split("#")[0]
        if not path:
            return match.group(0)
        anchor = target.split("#", 1)[1] if "#" in target else ""
        suffix = f"#{anchor}" if anchor else ""
        if bang:
            url = f"https://raw.githubusercontent.com/{full_name}/{branch}/{path}"
        else:
            url = f"https://github.com/{full_name}/blob/{branch}/{path}"
        return f"{bang}[{label}]({url}{suffix}{title})"

    return _LINK_RE.sub(repl, markdown)


def _render_project_doc(db: Dict[str, Any], repo: Dict[str, Any], root: str,
                        page: Optional[Dict[str, Any]], links: List[str]) -> None:
    tree = repo.get("tree") or {}
    tech = repo.get("technology") or {}
    readme = repo.get("readme") or {}
    readme_body = _absolutize_readme_links(repo.get("readme_full_content") or "", repo)
    page_url = (page or {}).get("url") or repo.get("homepage")
    related = [r.get("full_name") for r in db["repositories"]
               if r.get("full_name") != repo.get("full_name")
               and r.get("language") and r.get("language") == repo.get("language")][:5]

    lines = [
        f"# {repo.get('name')}",
        "",
        f"**Overview:** {repo.get('description') or '_No repository description provided._'}",
        "",
        "| Attribute | Value |",
        "| --- | --- |",
        f"| Repository | [{repo.get('full_name')}]({repo.get('url')}) |",
        f"| Live website | {page_url or 'not deployed / not declared'} |",
        f"| Visibility | {repo.get('visibility')} |",
        f"| Status | {'archived' if repo.get('archived') else ('fork' if repo.get('fork') else 'active')} |",
        f"| Creation date | {_fmt_date(repo.get('created_at'))} |",
        f"| Last update | {_fmt_date(repo.get('updated_at'))} |",
        f"| Last push | {_fmt_date(repo.get('pushed_at'))} |",
        f"| Default branch | {repo.get('default_branch') or '-'} |",
        f"| License | {repo.get('license') or 'none declared'} |",
        f"| Primary language | {repo.get('language') or '-'} |",
        f"| Stars / Forks / Watchers | {repo.get('stars') or 0} / {repo.get('forks') or 0} / {repo.get('watchers') or 0} |",
        f"| Issues (open / closed) | {repo.get('open_issues') or 0} / {repo.get('closed_issues') or 0} |",
        f"| Pull requests (open / merged) | {repo.get('open_pull_requests') or 0} / {repo.get('merged_pull_requests') or 0} |",
        f"| Releases | {repo.get('releases_count') or 0} |",
        f"| Contributors | {(repo.get('contributors') or {}).get('count') if repo.get('contributors') else 'not accessible'} |",
        f"| Size | {repo.get('size_kb') or 0} KB |",
        f"| Topics | {', '.join(repo.get('topics') or []) or '-'} |",
        "",
        "## Objectives",
        "",
        (readme_body.split("\n\n")[0][:600] if readme_body else
         f"Objectives are not documented in a README. Repository description: {repo.get('description') or 'none'}."),
        "",
        "## Features",
        "",
        _extract_section(readme_body, ("features", "what it does", "capabilities", "highlights")) or
        "No explicit feature list found in the README.",
        "",
        "## Technical architecture",
        "",
        f"- **Top-level directories:** {', '.join(tree.get('top_level_directories') or []) or '-'}",
        f"- **Total files (tracked in default branch):** {tree.get('total_files') or 0}",
        f"- **CI workflows:** {', '.join(tree.get('workflow_files') or []) or 'none detected'}",
        f"- **Test files detected:** {tree.get('test_files_count') or 0}",
        "",
        "## Languages and technologies",
        "",
        "| Language | Bytes |",
        "| --- | --- |",
        *([f"| {name} | {size} |" for name, size in
           sorted((repo.get('languages') or {}).items(), key=lambda kv: -(kv[1] or 0))] or ["| - | - |"]),
        "",
        f"**Frameworks / libraries detected:** {', '.join(tech.get('frameworks') or []) or 'none detected from dependency files'}",
        "",
        f"**Dependencies:** {', '.join(tech.get('dependencies') or []) or 'none detected'}",
        "",
        "## Important source files",
        "",
        *([f"- `{f}`" for f in tree.get("important_files") or []] or ["- none of the well-known entry/config files detected"]),
        "",
        "## Installation and setup",
        "",
        _extract_section(readme_body, ("installation", "install", "setup", "getting started", "quick start")) or
        "No installation instructions found in the README.",
        "",
        "## Deployment",
        "",
        (f"GitHub Pages deploy from `{page.get('source_branch')}/{page.get('source_path')}` "
         f"(status: {page.get('status')}); custom domain: {page.get('cname') or 'none'}."
         if page else
         ("Firebase/other hosting declared via homepage field: " + (repo.get("homepage") or "")
          if repo.get("homepage") else "No deployment configuration detected.")),
        "",
        "## Documentation links",
        "",
        *([f"- {url}" for url in links] or [f"- Repository README: {readme.get('html_url') or repo.get('url')}"]),
        "",
        "## Development status",
        "",
        ("Archived — no further development expected." if repo.get("archived") else
         ("Fork of another project; see upstream for original authorship." if repo.get("fork") else
          ("Active — last push " + _fmt_date(repo.get("pushed_at")) if repo.get("pushed_at") else "Active"))),
        "",
        "## Associated contributions",
        "",
        f"- Open issues: {repo.get('open_issues') or 0}",
        f"- Merged pull requests: {repo.get('merged_pull_requests') or 0}",
        f"- Releases: {repo.get('releases_count') or 0}",
        "",
        "## Related projects",
        "",
        *([f"- {name}" for name in related] or ["- none identified"]),
        "",
        "## Known issues and limitations",
        "",
        _extract_section(readme_body, ("known issues", "limitations", "caveats", "disclaimer")) or
        "No limitations documented in the README.",
        "",
        "## Future development opportunities",
        "",
        _extract_section(readme_body, ("roadmap", "future", "todo", "planned")) or
        "No roadmap documented in the README.",
        "",
        "## README source",
        "",
        f"Full README: {readme.get('html_url') or repo.get('url')}",
        "",
    ]
    if readme_body:
        lines += ["```markdown", readme_body[:8000], "```", ""]
    _write(root, f"projects/individual_projects/{slugify(repo.get('name'))}.md", "\n".join(lines))


def _extract_section(markdown: str, keywords: tuple, max_lines: int = 18) -> Optional[str]:
    if not markdown:
        return None
    lines = markdown.splitlines()
    for index, line in enumerate(lines):
        stripped = line.strip().lstrip("#").strip().lower()
        if any(stripped.startswith(k) for k in keywords) and line.strip().startswith("#"):
            block = []
            for follow in lines[index + 1:index + 1 + max_lines]:
                if follow.strip().startswith("#"):
                    break
                block.append(follow)
            text = "\n".join(block).strip()
            if text:
                return text
    return None


# --------------------------------------------------------------------------- contributions
def render_contributions(db: Dict[str, Any], root: str) -> None:
    contributions = db.get("contributions") or []
    prs = [c for c in contributions if c.get("pull_request_or_issue") == "pull_request"]
    issues = [c for c in contributions if c.get("pull_request_or_issue") == "issue"]
    reviews = db.get("reviews") or {}
    discussions = db.get("discussions") or {}
    commits = db.get("commits") or {}

    _write_json(root, "contributions/pull_requests.json", prs)
    _write_json(root, "contributions/issues.json", issues)
    _write_json(root, "contributions/discussions.json", discussions)
    _write_json(root, "contributions/commits.json", commits)
    _write_json(root, "contributions/contribution_summary.json", db.get("contribution_summary") or {})

    summary = db.get("contribution_summary") or {}
    lines = [
        "# Contribution History",
        "",
        f"Generated from `MASTER_DATABASE.json` on {db['profile'].get('last_synced')}.",
        "",
        "## Summary",
        "",
        "| Metric | Value |",
        "| --- | --- |",
    ]
    for key, value in summary.items():
        lines.append(f"| {key.replace('_', ' ')} | {value if value is not None else 'unavailable'} |")
    lines += ["", "## Commits by repository (last 12 months)", "",
              "| Repository | Commits |", "| --- | --- |"]
    for entry in (commits.get("by_repository") or []):
        lines.append(f"| [{entry.get('repository')}]({entry.get('url')}) | {entry.get('commits')} |")
    if not commits.get("by_repository"):
        lines.append("| - | - |")

    lines += ["", "## Authored pull requests", ""]
    if prs:
        lines += ["| PR | Repository | State | Created | Merged |", "| --- | --- | --- | --- | --- |"]
        for pr in prs[:200]:
            lines.append(f"| [#{pr.get('number')} {_md_escape(pr.get('title'))}]({pr.get('url')}) "
                         f"| {pr.get('repository')} | {pr.get('state')} "
                         f"| {_fmt_date(pr.get('created_at'))} | {_fmt_date(pr.get('merged_at'))} |")
    else:
        lines.append("_No authored pull requests discovered._")

    lines += ["", "## Authored issues", ""]
    if issues:
        lines += ["| Issue | Repository | State | Created |", "| --- | --- | --- | --- |"]
        for issue in issues[:200]:
            lines.append(f"| [#{issue.get('number')} {_md_escape(issue.get('title'))}]({issue.get('url')}) "
                         f"| {issue.get('repository')} | {issue.get('state')} | {_fmt_date(issue.get('created_at'))} |")
    else:
        lines.append("_No authored issues discovered._")

    lines += ["", "## Reviews given (last 12 months)", ""]
    if reviews.get("items"):
        lines += ["| Pull request | Repository | Date |", "| --- | --- | --- |"]
        for item in reviews["items"][:100]:
            lines.append(f"| [#{item.get('pull_request_number')} {_md_escape(item.get('title'))}]({item.get('url')}) "
                         f"| {item.get('repository')} | {_fmt_date(item.get('occurred_at'))} |")
    else:
        lines.append(f"_None recorded in the last 12 months "
                     f"(total: {reviews.get('total') if reviews.get('total') is not None else 'unavailable'})._")

    lines += ["", "## Discussions", ""]
    if discussions.get("authored"):
        lines += [f"- [{d.get('title')}]({d.get('url')}) in {d.get('repository')}"
                  for d in discussions["authored"][:50]]
    elif discussions.get("available") is False:
        lines.append("_Discussions could not be collected: " + str(discussions.get("error")) + "_")
    else:
        lines.append("_No authored discussions discovered._")

    lines += ["", "## Contributions to external repositories (last 12 months)", ""]
    external = [r for r in (db.get("contributed_repositories") or {}).get("repositories", [])
                if not r.get("owned_by_profile")]
    if external:
        lines += ["| Repository | Commits | PRs | Issues | Reviews |", "| --- | --- | --- | --- | --- |"]
        for repo in external:
            lines.append(f"| [{repo.get('full_name')}]({repo.get('url')}) | {repo.get('commits')} "
                         f"| {repo.get('pull_requests')} | {repo.get('issues')} | {repo.get('reviews')} |")
    else:
        lines.append("_No external repository contributions detected in the last 12 months._")
    lines.append("")
    _write(root, "CONTRIBUTION_HISTORY.md", "\n".join(lines))


# --------------------------------------------------------------------------- resources
def render_resources(db: Dict[str, Any], root: str) -> None:
    _write_json(root, "resources/gists.json", db.get("gists") or [])
    _write_json(root, "resources/github_pages.json", db.get("github_pages") or [])
    _write_json(root, "resources/releases.json", db.get("releases") or [])
    _write_json(root, "resources/packages.json", db.get("packages") or {})
    _write_json(root, "resources/external_links.json", db.get("external_links") or [])
    _write_json(root, "achievements/badges.json", db.get("achievements") or [])
    _write_json(root, "achievements/achievements_history.json", {
        "note": "Achievement badges are web-UI only; this history records observed states per sync.",
        "observations": [{
            "timestamp": db["profile"].get("last_synced"),
            "badges": [{"name": b.get("name"), "status": b.get("status")}
                       for b in db.get("achievements") or []],
        }],
    })

    links = db.get("external_links") or []
    lines = ["# External Links & Live Sites", "",
             f"{len(links)} links discovered, each mapped to the resource it belongs to.", "",
             "| URL | Type | Relationships | Related resource |", "| --- | --- | --- | --- |"]
    for link in sorted(links, key=lambda l: (l.get("type") or "", l.get("url") or "")):
        lines.append(f"| {link.get('url')} | {link.get('type')} | {', '.join(link.get('relationships') or [])} "
                     f"| {', '.join(link.get('related_resources') or []) or '-'} |")
    if not links:
        lines.append("| - | - | - | - |")
    lines += ["", "## GitHub Pages sites", ""]
    if db.get("github_pages"):
        lines += ["| Repository | URL | Status | Source |", "| --- | --- | --- | --- |"]
        for page in db["github_pages"]:
            lines.append(f"| {page.get('repository')} | {page.get('url')} | {page.get('status')} "
                         f"| {page.get('source_branch')}/{page.get('source_path')} |")
    else:
        lines.append("_No GitHub Pages sites detected._")
    lines.append("")
    _write(root, "EXTERNAL_LINKS.md", "\n".join(lines))

    stack = db.get("technology_stack") or []
    lines = ["# Technology Stack", "",
             "Derived from repository language byte counts and dependency files.", "",
             "## Languages", "", "| Language | Bytes | Share | Repositories |", "| --- | --- | --- | --- |"]
    for item in [s for s in stack if s.get("category") == "language"]:
        lines.append(f"| {item.get('name')} | {item.get('total_bytes')} | {item.get('percentage')}% "
                     f"| {item.get('repository_count')} |")
    lines += ["", "## Frameworks and tools", "", "| Name | Repositories |", "| --- | --- |"]
    for item in [s for s in stack if s.get("category") == "framework"]:
        lines.append(f"| {item.get('name')} | {item.get('repository_count')} |")
    lines.append("")
    _write(root, "TECHNOLOGY_STACK.md", "\n".join(lines))

    badges = db.get("achievements") or []
    lines = ["# Achievements and Badges", ""]
    if badges:
        lines += ["| Achievement | Status | Source | Note |", "| --- | --- | --- | --- |"]
        for badge in badges:
            lines.append(f"| {badge.get('name')} | {badge.get('status')} | {badge.get('source_url')} "
                         f"| {_md_escape(badge.get('note'))} |")
    else:
        lines.append("_No achievement data could be collected._")
    lines += ["", "GitHub does not expose achievement badges through its REST or GraphQL APIs; "
                  "anything that cannot be machine-verified is recorded as `unverified`/`unavailable` "
                  "instead of being invented.", ""]
    _write(root, "ACHIEVEMENTS.md", "\n".join(lines))

    releases = db.get("releases") or []
    gists = db.get("gists") or []
    pages = db.get("github_pages") or []
    packages = (db.get("packages") or {}).get("packages") or []

    rows = [[r.get("name"), r.get("full_name"), r.get("url"), r.get("description"),
             r.get("language"), r.get("stars"), r.get("forks"), r.get("open_issues"),
             r.get("releases_count"), r.get("archived"), r.get("fork"), r.get("homepage"),
             r.get("created_at"), r.get("updated_at"), r.get("pushed_at")]
            for r in db["repositories"]]
    header = ["name", "full_name", "url", "description", "language", "stars", "forks",
              "open_issues", "releases", "archived", "fork", "homepage", "created_at",
              "updated_at", "pushed_at"]
    csv_path = os.path.join(root, "MASTER_DATABASE.csv")
    with open(csv_path, "w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(header)
        writer.writerows(rows)
    return {"releases": len(releases), "gists": len(gists), "pages": len(pages), "packages": len(packages)}


# --------------------------------------------------------------------------- dashboard
def render_dashboard(db: Dict[str, Any], root: str, change_report: Dict[str, Any]) -> None:
    profile = db["profile"]
    details = profile["profile_details"]
    repos = db["repositories"]
    owned = [r for r in repos if not r.get("fork")]
    top_repos = sorted([r for r in owned if r.get("stars")], key=lambda r: -(r.get("stars") or 0))[:8]
    live = [l for l in db.get("external_links") or [] if l.get("type") == "live_site"]
    recent = sorted(owned, key=lambda r: r.get("pushed_at") or "", reverse=True)[:8]
    summary = db.get("contribution_summary") or {}
    quality = db.get("data_quality") or {}
    changes = (change_report.get("changes") or [])[:10]

    lines = [
        f"# {details.get('display_name') or details.get('username')} — GitHub Master Record",
        "",
        f"> Single source of truth for the complete GitHub history of "
        f"[@{details.get('username')}]({details.get('profile_url')}). "
        f"**Last synchronized:** {profile.get('last_synced')}",
        "",
        f"{details.get('bio') or ''}",
        "",
        "## Profile overview",
        "",
        "| Metric | Value |",
        "| --- | --- |",
        f"| Repositories (owned / forked) | {len(owned)} / {len(repos) - len(owned)} |",
        f"| Projects documented | {len(db.get('projects') or [])} |",
        f"| Public gists | {len(db.get('gists') or [])} |",
        f"| Live websites | {len(live)} |",
        f"| Releases tracked | {len(db.get('releases') or [])} |",
        f"| External links | {len(db.get('external_links') or [])} |",
        f"| Pull requests authored | {summary.get('pull_requests_total')} |",
        f"| Issues authored | {summary.get('issues_total')} |",
        f"| Commits (last 12 months) | {summary.get('commits_last_year')} |",
        f"| Total contributions (last 12 months) | {summary.get('contributions_last_year')} |",
        f"| Followers | {(db['profile'].get('statistics') or {}).get('followers')} |",
        "",
        "## Main technologies",
        "",
        ", ".join(f"{s['name']} ({s['percentage']}%)"
                  for s in [x for x in (db.get("technology_stack") or [])
                            if x.get("category") == "language"][:8]) or "not available",
        "",
        "## Important projects",
        "",
        _repo_table(top_repos) if top_repos else "_No starred repositories yet._",
        "",
        "## Live websites",
        "",
        *([f"- {l.get('url')}" for l in live[:15]] or ["- none detected"]),
        "",
        "## Latest changes in this sync",
        "",
        *([f"- **{c.get('type')}** — {c.get('summary')}" for c in changes] or
          ["- no changes detected in this run"]),
        "",
        "## Recently pushed repositories",
        "",
        "| Repository | Last push | Language |",
        "| --- | --- | --- |",
        *[f"| [{r.get('name')}]({r.get('url')}) | {_fmt_date(r.get('pushed_at'))} | {r.get('language') or '-'} |"
          for r in recent],
        "",
        "## Data quality",
        "",
        "| Check | Value |",
        "| --- | --- |",
        *[f"| {k.replace('_', ' ')} | {v} |" for k, v in quality.items()],
        "",
        "## Documentation map",
        "",
        "| Document | Purpose |",
        "| --- | --- |",
        "| [MASTER_PROFILE.md](MASTER_PROFILE.md) | Full profile record |",
        "| [MASTER_DATABASE.json](MASTER_DATABASE.json) | Canonical machine-readable database |",
        "| [MASTER_DATABASE.csv](MASTER_DATABASE.csv) | Flat repository table |",
        "| [PROJECT_INDEX.md](PROJECT_INDEX.md) | Every repository, owned and forked |",
        "| [projects/individual_projects/](projects/individual_projects/) | One document per repository |",
        "| [CONTRIBUTION_HISTORY.md](CONTRIBUTION_HISTORY.md) | Commits, PRs, issues, reviews, discussions |",
        "| [EXTERNAL_LINKS.md](EXTERNAL_LINKS.md) | Links, live sites and GitHub Pages |",
        "| [TECHNOLOGY_STACK.md](TECHNOLOGY_STACK.md) | Language and framework inventory |",
        "| [ACHIEVEMENTS.md](ACHIEVEMENTS.md) | Achievements and badge availability |",
        "| [SYNC_STATUS.md](SYNC_STATUS.md) | Automation state and sync history |",
        "| [CHANGELOG.md](CHANGELOG.md) | Every detected change |",
        "| [AI_AGENT_CONTEXT.md](AI_AGENT_CONTEXT.md) | Entry point for AI agents |",
        "",
        f"## GitHub profile",
        "",
        f"[{details.get('profile_url')}]({details.get('profile_url')})",
        "",
    ]
    _write(root, "README.md", "\n".join(lines))


def render_ai_context(db: Dict[str, Any], root: str) -> None:
    details = db["profile"]["profile_details"]
    repos = db["repositories"]
    owned = [r for r in repos if not r.get("fork")]
    active = [r for r in owned if not r.get("archived")]
    archived = [r for r in owned if r.get("archived")]
    live = [l for l in db.get("external_links") or [] if l.get("type") == "live_site"]
    lines = [
        "# AI Agent Context",
        "",
        f"**Owner:** {details.get('display_name')} (@{details.get('username')}) — "
        f"{details.get('bio') or 'no bio'}",
        "",
        f"**Last synchronized:** {db['profile'].get('last_synced')}",
        "",
        "## How to use this repository",
        "",
        "1. Read `MASTER_DATABASE.json` for structured, canonical data. Everything else is generated from it — never edit generated files by hand.",
        "2. Use `repositories/repositories_index.json` to map repository names to documentation files.",
        "3. Read `projects/individual_projects/<slug>.md` for the human narrative of a single project.",
        "4. Read `CONTRIBUTION_HISTORY.md` for work done outside owned repositories.",
        "5. Read `EXTERNAL_LINKS.md` to map live URLs to their owning repository.",
        "6. Read `SYNC_STATUS.md` to see whether the data is fresh.",
        "",
        "## Ground rules",
        "",
        "- `null` means the value was genuinely unavailable, not zero.",
        "- `unverified` / `unavailable` markers identify data GitHub does not expose via API.",
        "- Historical records are append-only; removed repositories are marked, not deleted.",
        "",
        "## Profile facts",
        "",
        f"- Total repositories documented: {len(repos)} ({len(owned)} owned, {len(repos) - len(owned)} forked)",
        f"- Active owned repositories: {len(active)}; archived: {len(archived)}",
        f"- Live websites: {len(live)}",
        f"- Languages in use: {', '.join(s['name'] for s in (db.get('technology_stack') or []) if s.get('category') == 'language')[:400] or 'unknown'}",
        "",
        "## Key repositories",
        "",
        _repo_table(sorted(owned, key=lambda r: (-(r.get('stars') or 0), r.get('name') or ''))[:25]),
        "",
        "## Live sites and their repositories",
        "",
        *([f"- {l.get('url')} → {', '.join(l.get('related_resources') or []) or 'profile-level'}"
           for l in live[:40]] or ["- none detected"]),
        "",
        "## Frequently asked questions",
        "",
        "- *Does this project exist?* Look it up in `repositories/repositories_index.json`.",
        "- *What does it do?* Read its project document.",
        "- *Is it deployed?* Check the `live_url` field in `projects/projects_index.json`.",
        "- *Is it finished?* Check `status` and `archived` in the database plus the project document's development status.",
        "",
    ]
    _write(root, "AI_AGENT_CONTEXT.md", "\n".join(lines))


def render_sync_status(db: Dict[str, Any], root: str, run_info: Dict[str, Any]) -> None:
    quality = db.get("data_quality") or {}
    lines = [
        "# Sync Status",
        "",
        f"- **Last successful sync:** {db['profile'].get('last_synced')}",
        f"- **Sync mode:** {run_info.get('mode')}",
        f"- **Triggered by:** {run_info.get('trigger')}",
        f"- **API requests this run:** {run_info.get('api_requests')}",
        f"- **Failed API requests:** {run_info.get('failed_requests')}",
        f"- **Runtime:** {run_info.get('duration_seconds')}s",
        "",
        "## Data quality",
        "",
        "| Check | Value |",
        "| --- | --- |",
        *[f"| {k.replace('_', ' ')} | {v} |" for k, v in quality.items()],
        "",
        "## Automation schedule",
        "",
        "| Workflow | Schedule (UTC) | Purpose |",
        "| --- | --- | --- |",
        "| `automatic-profile-sync.yml` | hourly at :17 | Detect new/updated repositories, profile changes, releases |",
        "| `scheduled-full-sync.yml` | daily 02:41 | Full profile and repository audit |",
        "| `scheduled-full-sync.yml` | weekly Sun 03:23 | Deep integrity and completeness audit |",
        "| `validate-master-data.yml` | on push / PR / manual | Validate JSON, CSV, duplicates and internal links |",
        "| `initial-data-collection.yml` | manual dispatch | Bootstrap or re-bootstrap the database |",
        "",
        "## Failed or unavailable resources",
        "",
        *([f"- {item}" for item in run_info.get("failures") or []] or ["- none"]),
        "",
    ]
    _write(root, "SYNC_STATUS.md", "\n".join(lines))


def append_changelog(root: str, change_report: Dict[str, Any], timestamp: str,
                     run_info: Dict[str, Any]) -> None:
    path = os.path.join(root, "CHANGELOG.md")
    existing = ""
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as handle:
            existing = handle.read()
    if not existing:
        existing = ("# Changelog\n\n"
                    "Every detected change to the GitHub profile record is appended here.\n"
                    "Entries are generated automatically from `MASTER_DATABASE.json` change history.\n")

    changes = change_report.get("changes") or []
    if not changes:
        return
    block = [f"\n## {timestamp} — {run_info.get('mode')} sync\n", ""]
    for change in changes:
        block.append(f"- **{change.get('type')}** ({change.get('resource')}): {change.get('summary')}")
        fields = change.get("fields") or {}
        for field, delta in list(fields.items())[:6]:
            if isinstance(delta, dict) and "old" in delta:
                block.append(f"  - `{field}`: {str(delta.get('old'))[:120]} → {str(delta.get('new'))[:120]}")
    block.append("")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(existing.rstrip() + "\n" + "\n".join(block))


def render_daily_report(db: Dict[str, Any], root: str, change_report: Dict[str, Any],
                        timestamp: str) -> None:
    date = timestamp[:10]
    changes = change_report.get("changes") or []
    added = [c for c in changes if c.get("type") == "repository_added"]
    updated = [c for c in changes if c.get("type") == "repository_updated"]
    missing = [c for c in changes if c.get("type") == "repository_missing"]
    links = [c for c in changes if c.get("type") == "external_links_added"]
    contributions = [c for c in changes if c.get("type") == "contributions_updated"]
    profile_changes = [c for c in changes if c.get("type") == "profile_updated"]
    quality = db.get("data_quality") or {}

    lines = [
        f"# Daily Report — {date}",
        "",
        f"Generated at {timestamp} from `MASTER_DATABASE.json`.",
        "",
        "## 1. What changed today?",
        "",
        f"{len(changes)} change(s) detected."
        if changes else "No changes detected.",
        "",
        "## 2. Repositories added",
        "",
        *([f"- [{c.get('resource')}]({c.get('url')})" for c in added] or ["- none"]),
        "",
        "## 3. Repositories updated",
        "",
        *([f"- {c.get('resource')}: {', '.join((c.get('fields') or {}).keys())}" for c in updated] or ["- none"]),
        "",
        "## 4. Projects modified",
        "",
        f"- Project documents regenerated: {len(db.get('projects') or [])}",
        "",
        "## 5. New links discovered",
        "",
        *([f"- {', '.join((c.get('fields') or {}).get('added') or [])}" for c in links] or ["- none"]),
        "",
        "## 6. Contributions detected",
        "",
        *([f"- {c.get('summary')}" for c in contributions] or ["- none"]),
        "",
        "## 7. Records corrected",
        "",
        *([f"- Profile: {', '.join((c.get('fields') or {}).keys())}" for c in profile_changes] or ["- none"]),
        "",
        "## 8. Could not be collected",
        "",
        *([f"- {c.get('resource')} ({c.get('type')})" for c in missing] or ["- nothing"]),
        "",
        "## 9. Still incomplete",
        "",
        "| Metric | Value |",
        "| --- | --- |",
        *[f"| {k.replace('_', ' ')} | {v} |" for k, v in quality.items()],
        "",
    ]
    _write(root, f"history/daily_reports/{date}.md", "\n".join(lines))


def render_sync_log(root: str, run_info: Dict[str, Any], timestamp: str,
                    change_report: Dict[str, Any]) -> str:
    """Persist one machine-readable sync log per run (history/sync_logs/)."""
    safe_ts = timestamp.replace(":", "").replace("-", "")
    record = {
        "run_at": timestamp,
        "mode": run_info.get("mode"),
        "trigger": run_info.get("trigger"),
        "duration_seconds": run_info.get("duration_seconds"),
        "api_requests": run_info.get("api_requests"),
        "failed_requests": run_info.get("failed_requests"),
        "changes_detected": change_report.get("total_changes", 0),
        "changed_fields": change_report.get("changed_fields") or [],
        "result": run_info.get("result") or "success",
        "error": run_info.get("error"),
    }
    relative = f"history/sync_logs/{safe_ts}_{run_info.get('mode') or 'full'}.json"
    _write_json(root, relative, record)
    return relative


def render_all(db: Dict[str, Any], root: str, change_report: Dict[str, Any],
               run_info: Dict[str, Any], timestamp: str) -> Dict[str, Any]:
    render_profile(db, root)
    render_repositories(db, root)
    render_projects(db, root)
    render_contributions(db, root)
    counters = render_resources(db, root)
    render_dashboard(db, root, change_report)
    render_ai_context(db, root)
    render_sync_status(db, root, run_info)
    render_daily_report(db, root, change_report, timestamp)
    render_sync_log(root, run_info, timestamp, change_report)
    append_changelog(root, change_report, timestamp, run_info)
    return counters
