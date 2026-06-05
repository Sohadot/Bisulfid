#!/usr/bin/env python3
"""Sprint 98 — Generate sharded atlas sitemaps from release ledger."""
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
LEDGER_PATH = ROOT / "main/data/release_ledger.json"
PUBLIC_DIR = ROOT / "site/public"
REPORT_PATH = ROOT / "main/data/SITEMAP_VALIDATION_REPORT.md"
SITE_BASE = "https://bisulfid.com"


def urlset(urls: list[str]) -> str:
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for url in sorted(urls):
        lines.append("  <url>")
        lines.append(f"    <loc>{escape(url)}</loc>")
        lines.append("  </url>")
    lines.append("</urlset>")
    return "\n".join(lines) + "\n"


def sitemap_index(maps: list[str]) -> str:
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for m in maps:
        lines.append("  <sitemap>")
        lines.append(f"    <loc>{escape(SITE_BASE + '/' + m)}</loc>")
        lines.append("  </sitemap>")
    lines.append("</sitemapindex>")
    return "\n".join(lines) + "\n"


def main() -> int:
    print("=" * 60)
    print("Sprint 98 — Atlas Sitemap Generator")
    print("=" * 60)
    ledger = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    shards: dict[str, list[str]] = {
        "sitemap-core.xml": [],
        "sitemap-languages.xml": [],
        "sitemap-context.xml": [],
    }
    for rec in ledger["records"]:
        if rec.get("release_status") != "released":
            continue
        shard = rec.get("sitemap_file") or "sitemap-core.xml"
        path = rec.get("route_path", "/").rstrip("/")
        url = SITE_BASE + (path if path else "")
        if not url.endswith("/") and path:
            url += "/"
        elif not path:
            url = SITE_BASE + "/"
        shards.setdefault(shard, []).append(url)
    written_maps = []
    total_urls = 0
    for name, urls in shards.items():
        if not urls:
            continue
        (PUBLIC_DIR / name).write_text(urlset(urls), encoding="utf-8")
        written_maps.append(name)
        total_urls += len(urls)
    if written_maps:
        (PUBLIC_DIR / "sitemap.xml").write_text(sitemap_index(written_maps), encoding="utf-8")
    robots = (
        "User-agent: *\n"
        "Allow: /\n"
        f"Sitemap: {SITE_BASE}/sitemap.xml\n"
    )
    (PUBLIC_DIR / "robots.txt").write_text(robots, encoding="utf-8")
    report = [
        "# Sitemap Validation Report",
        "",
        f"**Date:** {date.today().isoformat()}",
        f"**Sitemap index:** sitemap.xml",
        f"**Shard maps:** {', '.join(written_maps)}",
        f"**Total indexable URLs:** {total_urls}",
        "",
        "## Shard counts",
        "",
    ]
    for name in written_maps:
        report.append(f"- `{name}`: {len(shards[name])} URLs")
    REPORT_PATH.write_text("\n".join(report) + "\n", encoding="utf-8")
    print(f"URLs: {total_urls}")
    print(f"Shards: {written_maps}")
    print(f"Report: {REPORT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
