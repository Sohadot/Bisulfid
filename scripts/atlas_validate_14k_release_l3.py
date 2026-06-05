#!/usr/bin/env python3
"""Sprint 99 — Validate full 14K public dossier release."""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from atlas_dossier_common_l3 import FORBIDDEN_PUBLIC_PATTERNS, load_release_model  # noqa: E402

LEDGER_PATH = ROOT / "main/data/release_ledger.json"
PUBLIC_DIR = ROOT / "site/public"
REPORT_PATH = ROOT / "main/data/14K_VALIDATION_REPORT.md"
HREF_RE = re.compile(r'<a\s+href="([^"]+)"', re.I)
MIN_BODY_CHARS = 400


def main() -> int:
    print("=" * 60)
    print("Sprint 99 — 14K Release Validator")
    print("=" * 60)
    model = load_release_model()
    min_links = model.get("min_internal_links", 8)
    ledger = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    released = [r for r in ledger["records"] if r["release_status"] == "released"]
    public_paths: set[str] = set()
    ledger_paths: set[str] = set()
    sitemap_urls: set[str] = set()
    errors: list[str] = []
    warnings: list[str] = []

    for rec in released:
        path = rec.get("route_path", "/").rstrip("/")
        ledger_paths.add("/" if not path else path + "/")
        public_paths.add("/" if not path else "/" + path + "/")

    shard_contents: dict[str, str] = {}
    for rec in released:
        path = rec.get("route_path", "/").strip("/")
        html_path = PUBLIC_DIR / ("index.html" if not path else f"{path}/index.html")
        if not html_path.is_file():
            errors.append(f"{rec['route_id']}: missing HTML")
            continue
        text = html_path.read_text(encoding="utf-8")
        lower = text.lower()
        rid = rec["route_id"]
        if "<title>" not in lower:
            errors.append(f"{rid}: missing title")
        if 'name="description"' not in lower:
            errors.append(f"{rid}: missing meta description")
        if 'rel="canonical"' not in lower:
            errors.append(f"{rid}: missing canonical")
        if "noindex" in lower:
            errors.append(f"{rid}: contains noindex")
        visible = re.sub(r'<a\s+href="[^"]*"', '<a href=""', text, flags=re.I)
        visible = re.sub(r'<link[^>]+>', "", visible, flags=re.I)
        visible = re.sub(r'https?://[^\s<"]+', "", visible, flags=re.I)
        visible = re.sub(r'data-[a-z-]+="[^"]*"', "", visible, flags=re.I)
        visible = re.sub(r'cohort\d+_en_[a-z0-9_]+', "", visible, flags=re.I)
        for pat in FORBIDDEN_PUBLIC_PATTERNS:
            if pat.search(visible):
                errors.append(f"{rid}: forbidden {pat.pattern}")
                break
        link_count = lower.count("<a href=")
        if link_count < min_links:
            errors.append(f"{rid}: fewer than {min_links} links ({link_count})")
        body_match = re.search(r'class="atlas-page__body">(.*?)</section>', text, re.S | re.I)
        if body_match and len(re.sub(r"<[^>]+>", "", body_match.group(1)).strip()) < MIN_BODY_CHARS:
            errors.append(f"{rid}: body below minimum threshold")
        for href in HREF_RE.findall(text):
            if href.startswith("http") or href.startswith("#") or href.startswith("mailto:"):
                continue
            norm = href if href.endswith("/") else href + "/"
            if not norm.startswith("/"):
                norm = "/" + norm
            if norm not in public_paths and norm not in {"/", "/sources/", "/reference/corpus-methodology/"}:
                if norm.count("/") > 2:
                    target = PUBLIC_DIR / norm.strip("/") / "index.html"
                    if not target.is_file():
                        warnings.append(f"{rid}: link target may 404: {href}")

    for rec in released:
        shard = rec.get("sitemap_file")
        path = rec.get("route_path", "/").rstrip("/")
        if shard and path:
            if shard not in shard_contents:
                sf = PUBLIC_DIR / shard
                shard_contents[shard] = sf.read_text(encoding="utf-8") if sf.is_file() else ""
            if path + "/" not in shard_contents[shard]:
                errors.append(f"{rec['route_id']}: not in sitemap shard {shard}")

    sitemap_index = PUBLIC_DIR / "sitemap.xml"
    if not sitemap_index.is_file():
        errors.append("sitemap.xml missing")
    robots = PUBLIC_DIR / "robots.txt"
    if not robots.is_file() or "sitemap" not in robots.read_text(encoding="utf-8").lower():
        errors.append("robots.txt missing or no sitemap reference")

    shard_files = list(PUBLIC_DIR.glob("sitemap*.xml"))
    total_sitemap_urls = 0
    for sf in shard_files:
        if sf.name == "sitemap.xml":
            continue
        total_sitemap_urls += sf.read_text(encoding="utf-8").count("<loc>")

    if total_sitemap_urls != len(released):
        errors.append(
            f"sitemap URL count {total_sitemap_urls} != released count {len(released)}"
        )

    lines = [
        "# 14K Validation Report",
        "",
        f"**Date:** {date.today().isoformat()}",
        f"**Released routes checked:** {len(released)}",
        f"**Sitemap URLs:** {total_sitemap_urls}",
        f"**Errors:** {len(errors)}",
        f"**Warnings:** {len(warnings)}",
        "",
    ]
    if errors:
        lines.append("## Errors (first 50)")
        lines.append("")
        for e in errors[:50]:
            lines.append(f"- {e}")
        if len(errors) > 50:
            lines.append(f"- ... and {len(errors) - 50} more")
    if warnings:
        lines.extend(["", "## Warnings (first 20)", ""])
        for w in warnings[:20]:
            lines.append(f"- {w}")
    lines.extend([
        "",
        f"**Summary:** {'FAIL' if errors else 'PASS'}",
    ])
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Released: {len(released)}")
    print(f"Sitemap URLs: {total_sitemap_urls}")
    print(f"Errors: {len(errors)}")
    if errors:
        for e in errors[:15]:
            print(f"  ERROR: {e}")
        print("VALIDATION SUMMARY: FAIL")
        return 1
    print("VALIDATION SUMMARY: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
