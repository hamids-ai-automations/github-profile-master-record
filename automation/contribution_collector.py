"""Collect contributions and GitHub activity: authored pull requests, issues,
reviews, discussions, commits by repository plus gists, releases and packages.
"""
from __future__ import annotations

from typing import Any, Dict, List

from github_client import GitHubClient, GitHubError

REVIEW_QUERY = """
query($login: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $login) {
    contributionsCollection(from: $from, to: $to) {
      totalPullRequestReviewContributions
      pullRequestReviewContributions(first: 100) {
        totalCount
        nodes {
          occurredAt
          pullRequest { number title url state repository { nameWithOwner } }
        }
      }
    }
  }
}
"""

DISCUSSION_QUERY = """
query($login: String!) {
  user(login: $login) {
    repositoryDiscussions(first: 50, orderBy: {field: CREATED_AT, direction: DESC}) {
      totalCount
      nodes { number title url createdAt repository { nameWithOwner } }
    }
    repositoryDiscussionComments(first: 50) {
      totalCount
      nodes { url createdAt discussion { title number repository { nameWithOwner } } }
    }
  }
}
"""


def _pr_record(item: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "id": item.get("id"),
        "number": item.get("number"),
        "title": item.get("title"),
        "state": item.get("state"),
        "url": item.get("html_url"),
        "created_at": item.get("created_at"),
        "updated_at": item.get("updated_at"),
        "closed_at": item.get("closed_at"),
        "merged_at": item.get("pull_request", {}).get("merged_at")
        if isinstance(item.get("pull_request"), dict) else None,
        "repository": (item.get("repository_url") or "").replace(
            "https://api.github.com/repos/", ""),
        "author": (item.get("user") or {}).get("login"),
        "merged": bool((item.get("pull_request") or {}).get("merged_at"))
        if isinstance(item.get("pull_request"), dict) else None,
    }


def _issue_record(item: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "id": item.get("id"),
        "number": item.get("number"),
        "title": item.get("title"),
        "state": item.get("state"),
        "url": item.get("html_url"),
        "created_at": item.get("created_at"),
        "updated_at": item.get("updated_at"),
        "closed_at": item.get("closed_at"),
        "repository": (item.get("repository_url") or "").replace(
            "https://api.github.com/repos/", ""),
        "author": (item.get("user") or {}).get("login"),
        "labels": [l.get("name") for l in (item.get("labels") or []) if isinstance(l, dict)],
    }


def collect_pull_requests(client: GitHubClient, login: str) -> List[Dict[str, Any]]:
    items = client.paginate_search(
        "/search/issues", {"q": f"author:{login} type:pr", "sort": "updated", "order": "desc"})
    return [_pr_record(i) for i in items]


def collect_issues(client: GitHubClient, login: str) -> List[Dict[str, Any]]:
    items = client.paginate_search(
        "/search/issues", {"q": f"author:{login} type:issue", "sort": "updated", "order": "desc"})
    return [_issue_record(i) for i in items]


def collect_reviews(client: GitHubClient, login: str) -> Dict[str, Any]:
    from datetime import datetime, timedelta, timezone
    to = datetime.now(timezone.utc)
    frm = to - timedelta(days=365)
    try:
        data = client.graphql(REVIEW_QUERY, {
            "login": login,
            "from": frm.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "to": to.strftime("%Y-%m-%dT%H:%M:%SZ"),
        })
    except GitHubError as exc:
        print(f"[contributions] reviews unavailable: {exc}")
        return {"total": None, "items": [], "error": str(exc)}
    block = (((data or {}).get("user") or {}).get("contributionsCollection") or {})
    reviews = block.get("pullRequestReviewContributions") or {}
    items = []
    for node in (reviews.get("nodes") or []):
        pr = node.get("pullRequest") or {}
        items.append({
            "occurred_at": node.get("occurredAt"),
            "pull_request_number": pr.get("number"),
            "title": pr.get("title"),
            "url": pr.get("url"),
            "state": pr.get("state"),
            "repository": (pr.get("repository") or {}).get("nameWithOwner"),
        })
    return {"total": block.get("totalPullRequestReviewContributions"),
            "collected": reviews.get("totalCount"), "items": items}


def collect_discussions(client: GitHubClient, login: str) -> Dict[str, Any]:
    try:
        data = client.graphql(DISCUSSION_QUERY, {"login": login})
    except GitHubError as exc:
        print(f"[contributions] discussions unavailable: {exc}")
        return {"available": False, "error": str(exc), "authored": [], "comments": []}
    user = (data or {}).get("user") or {}
    authored_block = user.get("repositoryDiscussions") or {}
    comments_block = user.get("repositoryDiscussionComments") or {}
    authored = []
    for node in (authored_block.get("nodes") or []):
        authored.append({
            "number": node.get("number"), "title": node.get("title"), "url": node.get("url"),
            "created_at": node.get("createdAt"),
            "repository": (node.get("repository") or {}).get("nameWithOwner"),
        })
    comments = []
    for node in (comments_block.get("nodes") or []):
        disc = node.get("discussion") or {}
        comments.append({
            "url": node.get("url"), "created_at": node.get("createdAt"),
            "discussion_title": disc.get("title"), "discussion_number": disc.get("number"),
            "repository": (disc.get("repository") or {}).get("nameWithOwner"),
        })
    return {"available": True,
            "authored_total": authored_block.get("totalCount"),
            "comments_total": comments_block.get("totalCount"),
            "authored": authored, "comments": comments}


def collect_commits_by_repository(client: GitHubClient, login: str) -> Dict[str, Any]:
    from datetime import datetime, timedelta, timezone
    to = datetime.now(timezone.utc)
    frm = to - timedelta(days=365)
    query = """
    query($login: String!, $from: DateTime!, $to: DateTime!) {
      user(login: $login) {
        contributionsCollection(from: $from, to: $to) {
          totalCommitContributions
          commitContributionsByRepository(maxRepositories: 100) {
            repository { nameWithOwner url }
            contributions(first: 1) { totalCount }
          }
          contributionCalendar {
            totalContributions
            weeks { contributionDays { date contributionCount } }
          }
        }
      }
    }
    """
    try:
        data = client.graphql(query, {"login": login,
                                      "from": frm.strftime("%Y-%m-%dT%H:%M:%SZ"),
                                      "to": to.strftime("%Y-%m-%dT%H:%M:%SZ")})
    except GitHubError as exc:
        print(f"[contributions] commit summary unavailable: {exc}")
        return {"error": str(exc), "by_repository": [], "calendar": None}
    block = (((data or {}).get("user") or {}).get("contributionsCollection") or {})
    by_repo = []
    for item in (block.get("commitContributionsByRepository") or []):
        repo = item.get("repository") or {}
        by_repo.append({"repository": repo.get("nameWithOwner"), "url": repo.get("url"),
                        "commits": (item.get("contributions") or {}).get("totalCount")})
    calendar = block.get("contributionCalendar") or {}
    days = []
    for week in (calendar.get("weeks") or []):
        for day in (week.get("contributionDays") or []):
            if (day.get("contributionCount") or 0) > 0:
                days.append({"date": day.get("date"), "count": day.get("contributionCount")})
    return {"window": {"from": frm.strftime("%Y-%m-%dT%H:%M:%SZ"),
                       "to": to.strftime("%Y-%m-%dT%H:%M:%SZ")},
            "total_commits": block.get("totalCommitContributions"),
            "total_contributions": calendar.get("totalContributions"),
            "by_repository": by_repo, "active_days": days}


def collect_gists(client: GitHubClient, login: str) -> List[Dict[str, Any]]:
    gists = client.get(f"/users/{login}/gists", params={"per_page": 100}, allow_404=True) or []
    records = []
    for g in gists:
        files = g.get("files") or {}
        records.append({
            "id": g.get("id"),
            "description": g.get("description"),
            "url": g.get("html_url"),
            "api_url": g.get("url"),
            "public": g.get("public"),
            "created_at": g.get("created_at"),
            "updated_at": g.get("updated_at"),
            "comments": g.get("comments"),
            "files": [{"filename": name, "language": (meta or {}).get("language"),
                       "size": (meta or {}).get("size")}
                      for name, meta in files.items()],
        })
    return records


def collect_packages(client: GitHubClient, login: str) -> Dict[str, Any]:
    containers = client.get(f"/users/{login}/packages",
                            params={"package_type": "container"}, allow_404=True)
    npm = client.get(f"/users/{login}/packages",
                     params={"package_type": "npm"}, allow_404=True)
    pypi = client.get(f"/users/{login}/packages",
                      params={"package_type": "pypi"}, allow_404=True)
    def _norm(items, kind):
        return [{"name": (i or {}).get("name"), "type": kind,
                 "url": (i or {}).get("html_url"),
                 "visibility": (i or {}).get("visibility")}
                for i in (items or []) if isinstance(i, dict)]
    packages = _norm(containers, "container") + _norm(npm, "npm") + _norm(pypi, "pypi")
    return {"packages": packages, "count": len(packages)}


def collect_contributions(client: GitHubClient, login: str) -> Dict[str, Any]:
    prs = collect_pull_requests(client, login)
    issues = collect_issues(client, login)
    reviews = collect_reviews(client, login)
    discussions = collect_discussions(client, login)
    commits = collect_commits_by_repository(client, login)
    return {
        "pull_requests": prs,
        "issues": issues,
        "reviews": reviews,
        "discussions": discussions,
        "commits": commits,
        "summary": {
            "pull_requests_total": len(prs),
            "pull_requests_merged": sum(1 for p in prs if p.get("merged")),
            "issues_total": len(issues),
            "issues_open": sum(1 for i in issues if i.get("state") == "open"),
            "reviews_last_year": reviews.get("total"),
            "discussions_authored": discussions.get("authored_total"),
            "discussion_comments": discussions.get("comments_total"),
            "commits_last_year": commits.get("total_commits"),
            "contributions_last_year": commits.get("total_contributions"),
        },
    }
