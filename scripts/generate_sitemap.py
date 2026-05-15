#!/usr/bin/env python3
"""generate_sitemap.py — Prelaunch sitemap generator for bisulfid.com.

Reads routes.json and sitemap_policy.json.
Generates site/sitemap.xml with an empty urlset.
No planned routes are included. No published routes exist yet.
Python standard library only. No external dependencies.
"""

import json
import os


ROUTES_PATH = "main/data/routes.json"
SITEMAP_POLICY_PATH = "main/data/sitemap_policy.json"
SITE_DIR = "site"
SITEMAP_PATH = os.path.join(SITE_DIR, "sitemap.xml")


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    if not os.path.isfile(ROUTES_PATH):
        print(f"ERROR: Routes file not found: {ROUTES_PATH}")
        return 1

    routes_data = load_json(ROUTES_PATH)
    routes = routes_data.get("routes", [])

    # Only published, indexable, in_sitemap routes enter the sitemap.
    # All routes are currently planned. Zero URLs are included.
    sitemap_urls = [
        r for r in routes
        if r.get("status") == "published"
        and r.get("indexable") is True
        and r.get("in_sitemap") is True
    ]

    os.makedirs(SITE_DIR, exist_ok=True)

    sitemap_content = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<!-- No published indexable routes. -->\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        '  <!-- Sitemap URLs will appear here when routes are published and pass Quality Gate. -->\n'
        '</urlset>\n'
    )

    with open(SITEMAP_PATH, "w", encoding="utf-8") as f:
        f.write(sitemap_content)

    print(f"Sitemap generated with {len(sitemap_urls)} URLs.")
    print(f"  Output: {SITEMAP_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
