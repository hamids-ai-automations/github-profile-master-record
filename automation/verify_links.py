"""Standalone markdown link integrity gate.

Fails when any relative link inside generated Markdown does not resolve to a
real file in the repository. External (http/https) links are not fetched.
"""
from __future__ import annotations

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_validator import check_markdown_links  # noqa: E402


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Verify markdown link integrity")
    parser.add_argument("--root", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    args = parser.parse_args(argv)
    result = check_markdown_links(args.root)
    broken = result.get("broken") or []
    print(f"[links] checked={result.get('checked')} broken={len(broken)}")
    for item in broken[:40]:
        print(f"  BROKEN {item}")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
