"""GitHub API client: authenticated REST + GraphQL with pagination, rate-limit
and transient-failure recovery.

No token is ever hardcoded or logged. The token is read from the environment
(``GH_PROFILE_SYNC_TOKEN`` first, then ``GITHUB_TOKEN``/``GH_TOKEN``).
"""
from __future__ import annotations

import json
import http.client
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Dict, Iterable, List, Optional

REST_ROOT = "https://api.github.com"
GRAPHQL_URL = "https://api.github.com/graphql"
USER_AGENT = "github-profile-master-record-sync/1.0"

MAX_RATE_LIMIT_WAIT = 3600


class GitHubError(RuntimeError):
    """Raised when an API request fails permanently."""


class AuthError(GitHubError):
    """Raised when the token is missing, expired, revoked or lacks permission."""


def _log(message: str) -> None:
    print(f"[github] {message}", file=sys.stderr, flush=True)


class GitHubClient:
    def __init__(self, token: Optional[str] = None, api_url: str = REST_ROOT,
                 max_retries: int = 4):
        self.token = token or os.environ.get("GH_PROFILE_SYNC_TOKEN") \
            or os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
        if not self.token:
            raise GitHubError(
                "No GitHub token found. Set GH_PROFILE_SYNC_TOKEN (or GITHUB_TOKEN)."
            )
        self.api_url = api_url.rstrip("/")
        self.graphql_url = api_url.rstrip("/") + "/graphql" if api_url != REST_ROOT else GRAPHQL_URL
        self.max_retries = max_retries
        self.request_count = 0
        self.failed_requests: List[Dict[str, Any]] = []

    # ------------------------------------------------------------------ transport
    def _headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": USER_AGENT,
        }

    def _wait_for_rate_limit(self, headers: Dict[str, str]) -> None:
        reset = headers.get("X-RateLimit-Reset") or headers.get("x-ratelimit-reset")
        remaining = headers.get("X-RateLimit-Remaining") or headers.get("x-ratelimit-remaining")
        if remaining is not None and str(remaining).strip() == "0" and reset:
            wait = max(0, int(reset) - int(time.time())) + 5
            wait = min(wait, MAX_RATE_LIMIT_WAIT)
            _log(f"rate limit exhausted; sleeping {wait}s")
            time.sleep(wait)
        else:
            retry_after = headers.get("Retry-After")
            wait = int(retry_after) if retry_after else 10
            _log(f"rate limited; sleeping {wait}s")
            time.sleep(min(wait, MAX_RATE_LIMIT_WAIT))

    def _request(self, method: str, url: str, payload: Optional[Dict[str, Any]] = None,
                 params: Optional[Dict[str, Any]] = None) -> tuple[Any, Dict[str, str]]:
        if params:
            clean = {k: v for k, v in params.items() if v is not None}
            if clean:
                url = f"{url}?{urllib.parse.urlencode(clean)}"
        body = json.dumps(payload).encode("utf-8") if payload is not None else None
        last_error = None
        for attempt in range(1, self.max_retries + 1):
            req = urllib.request.Request(url, data=body, method=method,
                                         headers=self._headers())
            try:
                self.request_count += 1
                with urllib.request.urlopen(req, timeout=60) as resp:
                    raw = resp.read().decode("utf-8")
                    headers = dict(resp.headers.items())
                    return (json.loads(raw) if raw.strip() else {}, headers)
            except urllib.error.HTTPError as exc:  # type: ignore[attr-defined]
                headers = dict(exc.headers.items()) if exc.headers else {}
                code = exc.code
                detail = ""
                try:
                    detail = exc.read().decode("utf-8", "replace")[:300]
                except Exception:  # noqa: BLE001
                    pass
                if code in (403, 429):
                    last_error = f"HTTP {code}: {detail}"
                    self._wait_for_rate_limit(headers)
                    continue
                if code >= 500:
                    last_error = f"HTTP {code}: {detail}"
                    time.sleep(min(2 ** attempt, 30))
                    continue
                if code == 404:
                    raise GitHubError(f"404 not found: {url}") from exc
                if code == 401:
                    raise AuthError(f"401 unauthorized: token missing, expired or revoked ({url})") from exc
                raise GitHubError(f"HTTP {code} for {url}: {detail}") from exc
            except (urllib.error.URLError, TimeoutError, json.JSONDecodeError,
                    ConnectionError, OSError, http.client.HTTPException) as exc:
                last_error = f"{type(exc).__name__}: {exc}"
                time.sleep(min(2 ** attempt, 30))
                continue
        self.failed_requests.append({"url": url, "error": last_error})
        raise GitHubError(f"request failed after {self.max_retries} attempts: {url} ({last_error})")

    # ------------------------------------------------------------------ REST
    def get(self, path: str, params: Optional[Dict[str, Any]] = None,
            allow_404: bool = False) -> Any:
        url = path if path.startswith("http") else f"{self.api_url}{path}"
        try:
            data, _ = self._request("GET", url, params=params)
            return data
        except GitHubError as exc:
            if allow_404 and "404" in str(exc):
                return None
            raise

    def paginate(self, path: str, params: Optional[Dict[str, Any]] = None,
                 per_page: int = 100, max_pages: int = 100) -> List[Any]:
        """Collect every page of a list endpoint (pagination-safe)."""
        url = path if path.startswith("http") else f"{self.api_url}{path}"
        results: List[Any] = []
        page = 1
        base_params = dict(params or {})
        base_params["per_page"] = per_page
        while page <= max_pages:
            page_params = dict(base_params)
            page_params["page"] = page
            data, _ = self._request("GET", url, params=page_params)
            if not isinstance(data, list):
                raise GitHubError(f"expected list from {url}, got {type(data).__name__}")
            if not data:
                break
            results.extend(data)
            if len(data) < per_page:
                break
            page += 1
        else:
            _log(f"WARNING: pagination stopped at max_pages={max_pages} for {url}")
        return results

    def paginate_search(self, path: str, params: Dict[str, Any],
                        max_items: int = 1000) -> List[Any]:
        """Search endpoints cap at 1000 results and need page-based stepping."""
        items: List[Any] = []
        page = 1
        while page <= 10 and len(items) < max_items:
            page_params = dict(params)
            page_params.update({"per_page": 100, "page": page})
            data = self.get(path, params=page_params, allow_404=True)
            if not data or not data.get("items"):
                break
            items.extend(data["items"])
            if len(data["items"]) < 100:
                break
            page += 1
        return items[:max_items]

    # ------------------------------------------------------------------ GraphQL
    def graphql(self, query: str, variables: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        payload = {"query": query, "variables": variables or {}}
        last_error = None
        for attempt in range(1, self.max_retries + 1):
            try:
                data, _ = self._request("POST", self.graphql_url, payload=payload)
            except GitHubError as exc:
                last_error = str(exc)
                if "404" in last_error:
                    raise
                time.sleep(min(2 ** attempt, 30))
                continue
            if isinstance(data, dict) and data.get("errors"):
                messages = "; ".join(str(e.get("message")) for e in data["errors"])
                # Partial data can still be usable for field-level permission gaps.
                if data.get("data"):
                    _log(f"GraphQL partial errors: {messages}")
                    return data["data"]
                raise GitHubError(f"GraphQL error: {messages}")
            return (data or {}).get("data") or {}
        raise GitHubError(f"GraphQL failed after retries: {last_error}")

    # ------------------------------------------------------------------ helpers
    def identity(self) -> Dict[str, Any]:
        """Authenticated user plus the OAuth scopes reported by the API."""
        data, headers = self._request("GET", f"{self.api_url}/user")
        headers = headers or {}
        scopes = headers.get("X-OAuth-Scopes") or headers.get("x-oauth-scopes") or ""
        return {
            "login": (data or {}).get("login"),
            "name": (data or {}).get("name"),
            "id": (data or {}).get("id"),
            "type": (data or {}).get("type"),
            "scopes": [s.strip() for s in scopes.split(",") if s.strip()],
        }

    def stats(self) -> Dict[str, int]:
        return {
            "requests": self.request_count,
            "failures": len(self.failed_requests),
        }

    def rate_limit(self) -> Dict[str, Any]:
        try:
            return self.get("/rate_limit") or {}
        except GitHubError:
            return {}
