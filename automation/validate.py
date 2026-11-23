"""Validate the committed master record without touching the network.

Exit code 0 when valid, 1 when the data or documentation has problems.
"""
from __future__ import annotations

import json
import os
import sys

from data_validator import check_markdown_links, validate_database

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main() -> int:
    path = os.path.join(ROOT, "MASTER_DATABASE.json")
    if not os.path.exists(path):
        print(f"FAIL: {path} not found")
        return 1
    with open(path, "r", encoding="utf-8") as handle:
        db = json.load(handle)

    result = validate_database(db)
    links = check_markdown_links(ROOT)

    print("MASTER_DATABASE.json validation")
    print(f"  valid: {result['valid']}")
    for key, value in result["counts"].items():
        print(f"  {key}: {value}")
    if result["errors"]:
        print("\nERRORS:")
        for error in result["errors"][:50]:
            print(f"  - {error}")
    if result["warnings"]:
        print(f"\nWARNINGS ({len(result['warnings'])}):")
        for warn in result["warnings"][:20]:
            print(f"  - {warn}")

    print("\nInternal markdown links")
    print(f"  checked: {links['checked']}, broken: {len(links['broken'])}")
    for broken in links["broken"][:30]:
        print(f"  - {broken}")

    profile = db.get("profile") or {}
    print("\nFreshness")
    print(f"  last_synced: {profile.get('last_synced')}")
    print(f"  schema_version: {(db.get('metadata') or {}).get('schema_version')}")

    return 0 if result["valid"] and not links["broken"] else 1


if __name__ == "__main__":
    sys.exit(main())
