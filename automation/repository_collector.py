"""Collect every repository owned by the profile plus everything needed to
document it: metadata, statistics, languages, README, tree/architecture,
CI workflows, releases and contributor counts.
"""
from __future__ import annotations

import base64
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Dict, List, Optional

from github_client import GitHubClient, GitHubError

REPO_BATCH_QUERY = """
query($login: String!, $cursor: String, $first: Int!) {
  user(login: $login) {
    repositories(first: $first, after: $cursor, privacy: PUBLIC,
                 ownerAffiliations: [OWNER], orderBy: {field: PUSHED_AT, direction: DESC}) {
      pageInfo { hasNextPage endCursor }
      nodes {
        id
        name
        nameWithOwner
        url
        description
        homepageUrl
        createdAt
        updatedAt
        pushedAt
        isArchived
        isFork
        isDisabled
        isTemplate
        isPrivate
        isInOrganization
        diskUsage
        forkCount
        stargazerCount
        watchers { totalCount }
        primaryLanguage { name }
        languages(first: 25, orderBy: {field: SIZE, direction: DESC}) {
          totalSize
          edges { size node { name color } }
        }
        licenseInfo { key name spdxId url }
        repositoryTopics(first: 30) { nodes { topic { name } } }
        defaultBranchRef { name target { ... on Commit { committedDate } } }
        openIssues: issues(states: OPEN) { totalCount }
        closedIssues: issues(states: CLOSED) { totalCount }
        openPullRequests: pullRequests(states: OPEN) { totalCount }
        mergedPullRequests: pullRequests(states: MERGED) { totalCount }
        closedPullRequests: pullRequests(states: CLOSED) { totalCount }
        releases(first: 5, orderBy: {field: CREATED_AT, direction: DESC}) {
          totalCount
          nodes { name tagName url publishedAt isPrerelease description }
        }
        hasIssuesEnabled
        hasWikiEnabled
        hasProjectsEnabled
        hasDiscussionsEnabled
        discussions { totalCount }
        branchRefs: refs(refPrefix: "refs/heads/", first: 1) { totalCount }
        tags: refs(refPrefix: "refs/tags/", first: 1) { totalCount }
        deployments { totalCount }
        environments { totalCount }
        primaryPackage: packages(first: 5) { totalCount }
        vulnerabilityAlerts { totalCount }
      }
    }
  }
}
"""

CONTRIBUTED_QUERY = """
query($login: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $login) {
    contributionsCollection(from: $from, to: $to) {
      commitContributionsByRepository(maxRepositories: 100) {
        repository {
          nameWithOwner
          url
          description
          stargazerCount
          primaryLanguage { name }
          isFork
          owner { login }
        }
        contributions(first: 1) { totalCount }
      }
      pullRequestContributionsByRepository(maxRepositories: 100) {
        repository { nameWithOwner url description isFork owner { login } }
        contributions(first: 1) { totalCount }
      }
      issueContributionsByRepository(maxRepositories: 100) {
        repository { nameWithOwner url description isFork owner { login } }
        contributions(first: 1) { totalCount }
      }
      pullRequestReviewContributionsByRepository(maxRepositories: 100) {
        repository { nameWithOwner url description owner { login } }
        contributions(first: 1) { totalCount }
      }
    }
  }
}
"""

IMPORTANT_FILE_PATTERNS = (
    "main.py", "app.py", "index.js", "server.js", "manage.py", "package.json",
    "requirements.txt", "pyproject.toml", "Dockerfile", "docker-compose.yml",
    "firebase.json", ".firebaserc", "vercel.json", "netlify.toml", "Makefile",
    "tsconfig.json", "vite.config", "next.config", "README.md", "LICENSE",
    "schema.sql", "Procfile", "go.mod", "Cargo.toml", "pom.xml", "build.gradle",
)

FRAMEWORK_HINTS = {
    "react": "React", "next": "Next.js", "vue": "Vue", "svelte": "Svelte",
    "angular": "Angular", "express": "Express", "fastapi": "FastAPI",
    "flask": "Flask", "django": "Django", "streamlit": "Streamlit",
    "tailwind": "Tailwind CSS", "firebase": "Firebase", "supabase": "Supabase",
    "pandas": "pandas", "numpy": "NumPy", "openai": "OpenAI API",
    "anthropic": "Anthropic API", "langchain": "LangChain", "playwright": "Playwright",
    "selenium": "Selenium", "pytest": "pytest", "jest": "Jest", "mcp": "MCP",
    "gspread": "Google Sheets API", "google-api-python-client": "Google APIs",
    "sqlalchemy": "SQLAlchemy", "requests": "requests", "beautifulsoup4": "BeautifulSoup",
}


def _split_repo(repo: Dict[str, Any]) -> Dict[str, Any]:
    languages = {}
    for edge in ((repo.get("languages") or {}).get("edges") or []):
        node = edge.get("node") or {}
        languages[node.get("name")] = edge.get("size")
    releases = []
    for rel in ((repo.get("releases") or {}).get("nodes") or []):
        if not rel:
            continue
        releases.append({
            "name": rel.get("name"),
            "tag_name": rel.get("tagName"),
            "url": rel.get("url"),
            "published_at": rel.get("publishedAt"),
            "is_prerelease": rel.get("isPrerelease"),
        })
    topics = [((n or {}).get("topic") or {}).get("name")
              for n in ((repo.get("repositoryTopics") or {}).get("nodes") or [])]
    return {
        "id": repo.get("id"),
        "name": repo.get("name"),
        "full_name": repo.get("nameWithOwner"),
        "url": repo.get("url"),
        "description": repo.get("description"),
        "homepage": repo.get("homepageUrl"),
        "created_at": repo.get("createdAt"),
        "updated_at": repo.get("updatedAt"),
        "pushed_at": repo.get("pushedAt"),
        "default_branch": ((repo.get("defaultBranchRef") or {}).get("name")),
        "last_commit_at": (((repo.get("defaultBranchRef") or {}).get("target") or {})
                           .get("committedDate")),
        "visibility": "private" if repo.get("isPrivate") else "public",
        "is_private": bool(repo.get("isPrivate")),
        "archived": bool(repo.get("isArchived")),
        "fork": bool(repo.get("isFork")),
        "disabled": bool(repo.get("isDisabled")),
        "is_template": bool(repo.get("isTemplate")),
        "in_organization": bool(repo.get("isInOrganization")),
        "license": (repo.get("licenseInfo") or {}).get("spdxId"),
        "license_name": (repo.get("licenseInfo") or {}).get("name"),
        "language": (repo.get("primaryLanguage") or {}).get("name"),
        "languages": languages,
        "language_total_size": (repo.get("languages") or {}).get("totalSize"),
        "stars": repo.get("stargazerCount"),
        "forks": repo.get("forkCount"),
        "watchers": ((repo.get("watchers") or {}).get("totalCount")),
        "open_issues": ((repo.get("openIssues") or {}).get("totalCount")),
        "closed_issues": ((repo.get("closedIssues") or {}).get("totalCount")),
        "open_pull_requests": ((repo.get("openPullRequests") or {}).get("totalCount")),
        "merged_pull_requests": ((repo.get("mergedPullRequests") or {}).get("totalCount")),
        "closed_pull_requests": ((repo.get("closedPullRequests") or {}).get("totalCount")),
        "releases_count": ((repo.get("releases") or {}).get("totalCount")),
        "releases": releases,
        "tags_count": ((repo.get("tags") or {}).get("totalCount")),
        "branches_count": ((repo.get("branchRefs") or {}).get("totalCount")),
        "discussions_count": ((repo.get("discussions") or {}).get("totalCount")),
        "deployments_count": ((repo.get("deployments") or {}).get("totalCount")),
        "environments_count": ((repo.get("environments") or {}).get("totalCount")),
        "packages_count": ((repo.get("primaryPackage") or {}).get("totalCount")),
        "has_issues": repo.get("hasIssuesEnabled"),
        "has_wiki": repo.get("hasWikiEnabled"),
        "has_projects": repo.get("hasProjectsEnabled"),
        "has_discussions": repo.get("hasDiscussionsEnabled"),
        "topics": [t for t in topics if t],
        "size_kb": repo.get("diskUsage"),
    }


def collect_repository_metadata(client: GitHubClient, login: str,
                                page_size: int = 50) -> List[Dict[str, Any]]:
    repos: List[Dict[str, Any]] = []
    cursor = None
    while True:
        data = client.graphql(REPO_BATCH_QUERY,
                              {"login": login, "cursor": cursor, "first": page_size})
        block = ((data or {}).get("user") or {}).get("repositories") or {}
        for node in (block.get("nodes") or []):
            if node:
                repos.append(_split_repo(node))
        page_info = block.get("pageInfo") or {}
        if not page_info.get("hasNextPage"):
            break
        cursor = page_info.get("endCursor")
    return repos


def _fetch_readme(client: GitHubClient, full_name: str) -> Optional[Dict[str, Any]]:
    data = client.get(f"/repos/{full_name}/readme", allow_404=True)
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
        "size": data.get("size"),
        "content": content,
    }


def _fetch_tree(client: GitHubClient, full_name: str, branch: str) -> Optional[Dict[str, Any]]:
    data = client.get(f"/repos/{full_name}/git/trees/{branch}",
                      params={"recursive": "1"}, allow_404=True)
    if not data:
        return None
    tree = data.get("tree") or []
    dirs = sorted({item["path"].split("/")[0] for item in tree if "/" in item.get("path", "")})
    files = [item["path"] for item in tree if item.get("type") == "blob"]
    important = []
    for path in files:
        base = path.split("/")[-1].lower()
        if base in IMPORTANT_FILE_PATTERNS or path.lower() in IMPORTANT_FILE_PATTERNS:
            important.append(path)
    important = sorted(set(important))[:40]
    workflows = [p for p in files if p.startswith(".github/workflows/")]
    tests = [p for p in files if any(seg in p.lower() for seg in
                                     ("test", "spec", "__tests__", "conftest"))]
    return {
        "truncated": bool(data.get("truncated")),
        "total_files": len(files),
        "total_entries": len(tree),
        "top_level_directories": dirs[:50],
        "important_files": important,
        "workflow_files": workflows[:20],
        "test_files_count": len(tests),
        "ci_enabled": bool(workflows),
    }


def _fetch_contributors(client: GitHubClient, full_name: str) -> Optional[Dict[str, Any]]:
    """Contributor count using a single page and the Link header."""
    try:
        _, headers = client._request(  # noqa: SLF001 - intentional low-level use
            "GET", f"{client.api_url}/repos/{full_name}/contributors",
            params={"per_page": 1, "anon": "false"})
    except GitHubError:
        return None
    link = headers.get("Link") or headers.get("link") or ""
    if 'rel="last"' in link:
        import re
        match = re.search(r'[?&]page=(\d+)>; rel="last"', link)
        if match:
            return {"count": int(match.group(1)), "anonymous_included": False}
    return {"count": 1, "anonymous_included": False}


def _detect_stack(client: GitHubClient, repo: Dict[str, Any]) -> Dict[str, Any]:
    """Detect frameworks/libraries from common dependency files (best effort)."""
    frameworks, dependencies, configs = set(), set(), []
    checks = {
        "requirements.txt": "_parse_requirements",
        "package.json": "_parse_package_json",
        "pyproject.toml": "_parse_pyproject",
        "docker-compose.yml": "_parse_compose",
        "Dockerfile": "_parse_dockerfile",
        "firebase.json": "_mark_firebase",
    }
    for filename, handler in checks.items():
        data = client.get(f"/repos/{repo['full_name']}/contents/{filename}", allow_404=True)
        if not data or not isinstance(data, dict) or not data.get("content"):
            continue
        try:
            text = base64.b64decode(data["content"]).decode("utf-8", "replace")
        except Exception:  # noqa: BLE001
            continue
        configs.append(filename)
        lower = text.lower()
        for key, label in FRAMEWORK_HINTS.items():
            if key in lower:
                frameworks.add(label)
        if filename == "requirements.txt":
            for line in text.splitlines():
                line = line.strip()
                if line and not line.startswith("#"):
                    dependencies.add(line.split("==")[0].split(">=")[0].split("[")[0].strip())
        elif filename == "package.json":
            import json as _json
            try:
                pkg = _json.loads(text)
            except Exception:  # noqa: BLE001
                pkg = {}
            for section in ("dependencies", "devDependencies"):
                for dep in (pkg.get(section) or {}):
                    dependencies.add(dep)
        if handler == "_mark_firebase":
            frameworks.add("Firebase")
    return {
        "frameworks": sorted(frameworks),
        "dependencies": sorted(dependencies)[:60],
        "config_files": configs,
    }


def collect_repositories(client: GitHubClient, login: str,
                         previous_repositories: Optional[List[Dict[str, Any]]] = None,
                         light: bool = False) -> Dict[str, Any]:
    """Collect repository detail.

    ``light`` mode reuses every detail block (readme/tree/stack/contributors) for
    repositories whose ``pushed_at`` has not moved, so an hourly run costs two
    metadata requests plus a handful of detail requests for churn only.
    """
    base = collect_repository_metadata(client, login)
    previous = {r.get("full_name"): r for r in (previous_repositories or []) if r.get("full_name")}
    if not base:
        return {"owned": [], "forked": []}

    def build(repo: Dict[str, Any]) -> Dict[str, Any]:
        full_name = repo["full_name"]
        cached = previous.get(full_name)
        if light and cached and cached.get("pushed_at") == repo.get("pushed_at"):
            record = dict(cached)
            record.update({k: v for k, v in repo.items() if v is not None})
            if not record.get("readme_full_content"):
                # The canonical JSON keeps only an excerpt; the body is needed to
                # re-render the project page, so refetch this one cheap request.
                readme = _fetch_readme(client, full_name)
                body = (readme or {}).get("content") or ""
                record.update({
                    "readme": {
                        "path": (readme or {}).get("path"),
                        "html_url": (readme or {}).get("html_url"),
                        "has_readme": bool(readme),
                        "length": len(body),
                        "excerpt": body[:4000] if body else None,
                        "full_content_path": None,
                    },
                    "readme_full_content": body,
                    "external_links": _extract_links(body) if body else [],
                })
            record["detail_source"] = "cached"
            return record

        readme = _fetch_readme(client, full_name)
        tree = _fetch_tree(client, full_name, repo.get("default_branch") or "main")
        contributors = _fetch_contributors(client, full_name)
        stack = _detect_stack(client, repo)

        readme_content = (readme or {}).get("content") or ""
        external_links = _extract_links(readme_content) if readme_content else []

        record = dict(repo)
        record.update({
            "readme": {
                "path": (readme or {}).get("path"),
                "html_url": (readme or {}).get("html_url"),
                "has_readme": bool(readme),
                "length": len(readme_content),
                "excerpt": readme_content[:4000] if readme_content else None,
                "full_content_path": None,
            },
            "readme_full_content": readme_content,
            "tree": tree,
            "contributors": contributors,
            "technology": stack,
            "external_links": external_links,
            "documentation_status": "documented" if readme_content else "no_readme",
            "detail_refreshed_at": _utc_now(),
            "detail_source": "api",
        })
        return record

    # Detail fetching is network bound; bounded concurrency keeps a full run to
    # minutes instead of the better part of an hour while staying inside limits.
    workers = min(8, max(1, len(base)))
    with ThreadPoolExecutor(max_workers=workers) as pool:
        records = list(pool.map(build, base))

    owned, forked = [], []
    for record in records:
        if record.get("fork"):
            forked.append(record)
        else:
            owned.append(record)
    return {"owned": owned, "forked": forked}


def _utc_now() -> str:
    from datetime import datetime, timezone
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _extract_links(markdown: str) -> List[str]:
    import re
    urls = re.findall(r"https?://[^\s)\]\"'<>]+", markdown or "")
    seen, ordered = set(), []
    for url in urls:
        if any(url.startswith(p) for p in ("https://github.com/", "https://img.shields.io",
                                           "https://user-images.githubusercontent",
                                           "https://camo.githubusercontent")):
            continue
        url = url.rstrip(".,;:")
        if url not in seen:
            seen.add(url)
            ordered.append(url)
    return ordered[:30]


def collect_contributed_repositories(client: GitHubClient, login: str,
                                     days: int = 365) -> Dict[str, Any]:
    from datetime import datetime, timedelta, timezone
    to = datetime.now(timezone.utc)
    frm = to - timedelta(days=days)
    try:
        data = client.graphql(CONTRIBUTED_QUERY, {
            "login": login,
            "from": frm.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "to": to.strftime("%Y-%m-%dT%H:%M:%SZ"),
        })
    except GitHubError as exc:
        print(f"[contributions] contributed repositories unavailable: {exc}")
        return {"repositories": [], "window": {"from": frm.isoformat(), "to": to.isoformat()}}
    block = ((data or {}).get("user") or {}).get("contributionsCollection") or {}
    merged: Dict[str, Dict[str, Any]] = {}
    mapping = {
        "commitContributionsByRepository": "commits",
        "pullRequestContributionsByRepository": "pull_requests",
        "issueContributionsByRepository": "issues",
        "pullRequestReviewContributionsByRepository": "reviews",
    }
    for key, kind in mapping.items():
        for item in (block.get(key) or []):
            repo = item.get("repository") or {}
            name = repo.get("nameWithOwner")
            if not name:
                continue
            entry = merged.setdefault(name, {
                "full_name": name,
                "url": repo.get("url"),
                "description": repo.get("description"),
                "owner": (repo.get("owner") or {}).get("login"),
                "is_fork": repo.get("isFork"),
                "stars": repo.get("stargazerCount"),
                "language": (repo.get("primaryLanguage") or {}).get("name"),
                "commits": 0, "pull_requests": 0, "issues": 0, "reviews": 0,
                "owned_by_profile": (repo.get("owner") or {}).get("login") == login,
            })
            entry[kind] = (item.get("contributions") or {}).get("totalCount") or 0
    repos = sorted(merged.values(),
                   key=lambda r: -sum(r[k] for k in ("commits", "pull_requests", "issues", "reviews")))
    return {"repositories": repos,
            "window": {"from": frm.strftime("%Y-%m-%dT%H:%M:%SZ"),
                       "to": to.strftime("%Y-%m-%dT%H:%M:%SZ")}}
