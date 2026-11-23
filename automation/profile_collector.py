"""Collect the GitHub profile layer: identity, bio, websites, social links,
pinned repositories, statistics, achievements (where exposed) and README.
"""
from __future__ import annotations

import base64
from typing import Any, Dict, List, Optional

from github_client import GitHubClient, GitHubError

PROFILE_QUERY = """
query($login: String!) {
  user(login: $login) {
    login
    name
    bio
    company
    location
    email
    websiteUrl
    twitterUsername
    avatarUrl
    createdAt
    updatedAt
    isHireable
    isDeveloperProgramMember
    isGitHubStar
    followers { totalCount }
    following { totalCount }
    repositories(privacy: PUBLIC, ownerAffiliations: [OWNER]) { totalCount }
    starredRepositories { totalCount }
    organizations(first: 50) { nodes { login name url } }
    socialAccounts(first: 25) { nodes { provider displayName url } }
    status { message emoji }
    profileReadme: repository(name: $login) {
      name
      url
      description
      object(expression: "HEAD:README.md") { ... on Blob { text } }
    }
    pinnedItems(first: 6, types: [REPOSITORY]) {
      nodes { ... on Repository { name nameWithOwner url description stargazerCount primaryLanguage { name } } }
    }
    contributionsCollection {
      totalCommitContributions
      totalIssueContributions
      totalPullRequestContributions
      totalPullRequestReviewContributions
      totalRepositoriesWithContributedCommits
      restrictedContributionsCount
      contributionCalendar { totalContributions }
    }
  }
}
"""

ACHIEVEMENTS_QUERY = """
query($login: String!) {
  user(login: $login) {
    login
    repositories(first: 100, privacy: PUBLIC, ownerAffiliations: [OWNER]) {
      nodes {
        name
        owner { login }
        object(expression: "HEAD:README.md") { ... on Blob { text } }
      }
    }
  }
}
"""


def _readme_from_rest(client: GitHubClient, login: str) -> Optional[Dict[str, Any]]:
    data = client.get(f"/repos/{login}/{login}/readme", allow_404=True)
    if not data:
        return None
    content = None
    if data.get("content"):
        try:
            content = base64.b64decode(data["content"]).decode("utf-8", "replace")
        except Exception:  # noqa: BLE001
            content = None
    return {
        "path": data.get("path"),
        "html_url": data.get("html_url"),
        "download_url": data.get("download_url"),
        "content": content,
    }


def _parse_profile_readme_links(text: Optional[str]) -> List[str]:
    import re
    if not text:
        return []
    urls = re.findall(r"https?://[^\s)\]\"'<>]+", text)
    seen, ordered = set(), []
    for url in urls:
        url = url.rstrip(".,;:")
        if url not in seen:
            seen.add(url)
            ordered.append(url)
    return ordered


def collect_profile(client: GitHubClient, login: str) -> Dict[str, Any]:
    rest_user = client.get(f"/users/{login}") or {}
    graph: Dict[str, Any] = {}
    try:
        graph = (client.graphql(PROFILE_QUERY, {"login": login}) or {}).get("user") or {}
    except GitHubError as exc:  # keep REST-derived data usable
        print(f"[profile] GraphQL profile unavailable: {exc}")

    readme = _readme_from_rest(client, login)
    graph_readme = ((graph.get("profileReadme") or {}).get("object") or {}).get("text")
    if readme and graph_readme and not readme.get("content"):
        readme["content"] = graph_readme
    if readme is None and graph_readme:
        readme = {"path": "README.md", "html_url": f"https://github.com/{login}",
                  "download_url": None, "content": graph_readme}

    social = []
    for node in ((graph.get("socialAccounts") or {}).get("nodes") or []):
        social.append({"provider": node.get("provider"), "display_name": node.get("displayName"),
                       "url": node.get("url")})
    if rest_user.get("blog") and all(s.get("url") != rest_user["blog"] for s in social):
        social.append({"provider": "website", "display_name": "Profile website",
                       "url": rest_user["blog"]})

    pinned = []
    for node in ((graph.get("pinnedItems") or {}).get("nodes") or []):
        if not node:
            continue
        pinned.append({
            "name": node.get("name"),
            "name_with_owner": node.get("nameWithOwner"),
            "url": node.get("url"),
            "description": node.get("description"),
            "stars": node.get("stargazerCount"),
            "language": (node.get("primaryLanguage") or {}).get("name"),
        })

    contrib = graph.get("contributionsCollection") or {}
    calendar = contrib.get("contributionCalendar") or {}

    details = {
        "username": login,
        "display_name": rest_user.get("name") or graph.get("name"),
        "profile_url": rest_user.get("html_url") or f"https://github.com/{login}",
        "avatar_url": rest_user.get("avatar_url") or graph.get("avatarUrl"),
        "bio": rest_user.get("bio") if rest_user.get("bio") is not None else graph.get("bio"),
        "company": rest_user.get("company") if rest_user.get("company") is not None else graph.get("company"),
        "location": rest_user.get("location") if rest_user.get("location") is not None else graph.get("location"),
        "public_email": rest_user.get("email") or graph.get("email"),
        "website_url": rest_user.get("blog") or graph.get("websiteUrl"),
        "twitter_username": rest_user.get("twitter_username") or graph.get("twitterUsername"),
        "account_type": rest_user.get("type"),
        "created_at": rest_user.get("created_at") or graph.get("createdAt"),
        "updated_at": rest_user.get("updated_at") or graph.get("updatedAt"),
        "is_hireable": graph.get("isHireable"),
        "is_developer_program_member": graph.get("isDeveloperProgramMember"),
        "is_github_star": graph.get("isGitHubStar"),
        "status": (graph.get("status") or {}).get("message"),
        "social_accounts": social,
        "organizations": [
            {"login": o.get("login"), "name": o.get("name"), "url": o.get("url")}
            for o in ((graph.get("organizations") or {}).get("nodes") or []) if o
        ],
        "profile_readme": readme,
    }

    statistics = {
        "public_repos": rest_user.get("public_repos"),
        "public_gists": rest_user.get("public_gists"),
        "followers": rest_user.get("followers"),
        "following": rest_user.get("following"),
        "owned_repositories_graphql": ((graph.get("repositories") or {}).get("totalCount")),
        "starred_repositories": ((graph.get("starredRepositories") or {}).get("totalCount")),
        "total_contributions_last_year": calendar.get("totalContributions"),
        "total_commit_contributions": contrib.get("totalCommitContributions"),
        "total_issue_contributions": contrib.get("totalIssueContributions"),
        "total_pull_request_contributions": contrib.get("totalPullRequestContributions"),
        "total_pull_request_review_contributions": contrib.get("totalPullRequestReviewContributions"),
        "repositories_with_contributed_commits": contrib.get("totalRepositoriesWithContributedCommits"),
        "restricted_contributions": contrib.get("restrictedContributionsCount"),
    }

    return {
        "profile_details": details,
        "statistics": statistics,
        "pinned_repositories": pinned,
        "profile_readme_links": _parse_profile_readme_links((readme or {}).get("content")),
        "raw": {"rest": rest_user, "graphql": graph},
    }


ACHIEVEMENT_LABELS = {
    "Pull Shark": "pull_shark",
    "Quickdraw": "quickdraw",
    "Starstruck": "starstruck",
    "Pair Extraordinaire": "pair_extraordinaire",
    "Galaxy Brain": "galaxy_brain",
    "YOLO": "yolo",
    "Arctic Code Vault Contributor": "arctic_code_vault",
}


def collect_achievements(client: GitHubClient, login: str,
                         repositories: List[Dict[str, Any]]) -> Dict[str, Any]:
    """GitHub exposes achievements only in the web UI, not the REST/GraphQL API.

    We therefore (a) try the public achievements page, and (b) infer nothing.
    Anything not machine-verifiable is stored as unverified with a null value.
    """
    import json as _json
    import re
    import urllib.request

    entries: List[Dict[str, Any]] = []
    source_url = f"https://github.com/{login}?tab=achievements"
    html = None
    try:
        req = urllib.request.Request(source_url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=45) as resp:
            html = resp.read().decode("utf-8", "replace")
    except Exception as exc:  # noqa: BLE001
        print(f"[achievements] public page fetch failed: {exc}")

    if html:
        for label, slug in ACHIEVEMENT_LABELS.items():
            if label.lower() in html.lower():
                entries.append({
                    "name": label,
                    "slug": slug,
                    "tier": None,
                    "source_url": source_url,
                    "value": None,
                    "status": "unverified",
                    "note": "Achievement label present on public profile page; tier/points are not exposed by the GitHub API.",
                })

    entries.append({
        "name": "Achievements API availability",
        "slug": "api_availability",
        "tier": None,
        "source_url": "https://docs.github.com/rest",
        "value": None,
        "status": "unavailable",
        "note": "GitHub REST/GraphQL APIs do not expose achievement badges or their tiers. Badges can only be observed on the profile web page; values are intentionally left null rather than invented.",
    })

    # Profile highlights: pinned items + achievements tab are the only surfaced highlights.
    highlights = [{"type": "pinned_repository", "name": r.get("name"), "url": r.get("url")}
                  for r in []]

    return {"badges": entries, "highlights": highlights,
            "source_url": source_url, "fetched_html": bool(html)}
