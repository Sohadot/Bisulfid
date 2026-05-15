#!/usr/bin/env python3
"""generate_robots.py — Prelaunch robots.txt generator for bisulfid.com.

Generates site/robots.txt with a full Disallow policy for prelaunch.
Public indexing is disabled until all 11 Quality Gates pass and site status
changes from prelaunch to launched.
Python standard library only. No external dependencies.
"""

import os


SITE_DIR = "site"
ROBOTS_PATH = os.path.join(SITE_DIR, "robots.txt")

ROBOTS_CONTENT = """\
# Prelaunch robots policy. Public indexing disabled until Quality Gate passes.
# Do not modify this file to allow indexing before launch conditions are met.
# See doctrine/QUALITY_GATE.md for the 11 launch conditions.

User-agent: *
Disallow: /
"""


def main():
    os.makedirs(SITE_DIR, exist_ok=True)

    with open(ROBOTS_PATH, "w", encoding="utf-8") as f:
        f.write(ROBOTS_CONTENT)

    print("robots.txt generated.")
    print(f"  Output: {ROBOTS_PATH}")
    print("  Policy: Prelaunch — all indexing blocked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
