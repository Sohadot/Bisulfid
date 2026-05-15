#!/usr/bin/env python3
"""build.py — Static build orchestrator for bisulfid.com.

Reads route governance from main/data/routes.json and build config from
main/config/build.json. Generates site/build-status.json only.

No public route pages are generated. All routes are currently planned.
Only published routes may produce HTML output, and none are published yet.
Python standard library only. No external dependencies.
"""

import json
import os
import sys
from datetime import datetime, timezone


CONFIG_PATH = "main/config/build.json"
ROUTES_PATH = "main/data/routes.json"
SITE_DIR = "site"


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    print("bisulfid.com — Static Build Skeleton")
    print("=" * 50)

    if not os.path.isfile(CONFIG_PATH):
        print(f"ERROR: Build config not found: {CONFIG_PATH}")
        return 1

    if not os.path.isfile(ROUTES_PATH):
        print(f"ERROR: Routes file not found: {ROUTES_PATH}")
        return 1

    build_config = load_json(CONFIG_PATH)
    routes_data = load_json(ROUTES_PATH)

    output_dir = build_config.get("output_dir", SITE_DIR)
    os.makedirs(output_dir, exist_ok=True)

    routes = routes_data.get("routes", [])
    total = len(routes)
    published = [r for r in routes if r.get("status") == "published"]
    planned = [r for r in routes if r.get("status") == "planned"]

    # generate_only_published_routes is true in build.json.
    # All routes are planned. No HTML pages are generated.
    public_pages = 0

    build_status = {
        "build_status": build_config.get("build_status", "skeleton"),
        "public_pages_generated": public_pages,
        "reason": "No routes are published.",
        "route_count": total,
        "published_route_count": len(published),
        "planned_route_count": len(planned),
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    }

    status_path = os.path.join(output_dir, "build-status.json")
    with open(status_path, "w", encoding="utf-8") as f:
        json.dump(build_status, f, indent=2)

    print(f"  Routes loaded:          {total}")
    print(f"  Published routes:       {len(published)}")
    print(f"  Planned routes:         {len(planned)}")
    print(f"  Public pages generated: {public_pages}")
    print(f"  Build status file:      {status_path}")
    print("=" * 50)
    print("Build skeleton complete. No public pages generated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
