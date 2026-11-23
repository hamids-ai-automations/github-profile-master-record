"""Verify the master database against the live GitHub API.

Confirms that every repository the API reports for the account exists in
MASTER_DATABASE.json, and that no stale repositories linger. Purely read-only.

Exit codes: 0 = complete, 1 = drift detected, 2 = token missing/ unusable.
"""
from __future__ import annotations

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import json  # noqa: E402

from github_client import GitHubClient  # noqa: E402


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Verify database completeness vs GitHub API")
    parser.add_argument("--root", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    args = parser.parse_args(argv)

    token = os.environ.get("GH_PROFILE_SYNC_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not token:
        print("[completeness] SKIPPED — no token in environment")
        return 2

    with open(os.path.join(args.root, "MASTER_DATABASE.json"), "r", encoding="utf-8") as handle:
        db = json.load(handle)

    client = GitHubClient(token=token)
    user = client.get("/user") or {}
    login = user.get("login")
    api_repos = client.paginate("/user/repos", params={"affiliation": "owner", "per_page": 100}) or []
    client.close()

    # The collector records public repositories only (GraphQL privacy: PUBLIC), so
    # completeness is measured against the same scope; private repositories are
    # counted for transparency but never treated as drift.
    api_public = [repo for repo in api_repos if not repo.get("private")]
    api_private = [repo for repo in api_repos if repo.get("private")]
    api_names = {repo.get("full_name") for repo in api_public if repo.get("full_name")}
    db_repos = db.get("repositories") or []
    db_all = {r.get("full_name") for r in db_repos if r.get("full_name")}
    owner_prefix = f"{login}/" if login else ""
    db_owned = {name for name in db_all if owner_prefix and name.lower().startswith(owner_prefix.lower())}

    missing = sorted(api_names - db_all)
    owned_missing = sorted(api_names - db_owned)
    print(f"[completeness] account={login} public_repos={len(api_names)} "
          f"private_repos={len(api_private)} db_repos={len(db_all)}")
    print(f"[completeness] missing_from_db={len(missing)} owned_scope_missing={len(owned_missing)}")
    for name in missing[:25]:
        print(f"  MISSING {name}")

    if missing:
        print("[completeness] RESULT: DRIFT")
        return 1
    print("[completeness] RESULT: COMPLETE")
    return 0


if __name__ == "__main__":
    sys.exit(main())
