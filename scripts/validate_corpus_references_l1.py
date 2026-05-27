#!/usr/bin/env python3
"""L1 internal reference discipline validator — read-only, stdlib only (Sprint 5K)."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROUTES_PATH = ROOT / "main/data/routes.json"
INTERNAL_LINKS = ROOT / "main/data/internal_links.json"

URL_RE = re.compile(r"https?://[^\s\])>]+", re.I)
MD_LINK_RE = re.compile(r"\[[^\]]+\]\([^)]+\)")


def run_validation() -> tuple[list[str], list[str], dict]:
    errors: list[str] = []
    warnings: list[str] = []
    stats: dict = {"drafts_scanned": 0, "md_links_found": 0, "raw_urls_found": 0}

    routes = json.loads(ROUTES_PATH.read_text(encoding="utf-8"))["routes"]
    published_ids = {r["route_id"] for r in routes if r.get("status") == "published"}

    if INTERNAL_LINKS.exists():
        il = json.loads(INTERNAL_LINKS.read_text(encoding="utf-8"))
        if il.get("status") not in ("inactive", "planned"):
            warnings.append(f"internal_links.json status is {il.get('status')!r}")
        stats["internal_links_status"] = il.get("status", "unknown")
    else:
        warnings.append("internal_links.json not found")

    for route in routes:
        cf = ROOT / route["content_file"]
        if not cf.exists():
            continue
        stats["drafts_scanned"] += 1
        rid = route["route_id"]
        text = cf.read_text(encoding="utf-8")
        _, body = (text.split("---", 2) + ["", ""])[1:3]
        if text.startswith("---") and len(text.split("---", 2)) >= 3:
            body = text.split("---", 2)[2]

        if URL_RE.search(body):
            stats["raw_urls_found"] += 1
            errors.append(f"{rid}: raw external URL in draft")
        for m in MD_LINK_RE.finditer(body):
            stats["md_links_found"] += 1
            errors.append(f"{rid}: markdown link {m.group(0)[:60]}")

        lower = body.lower()
        if "published page" in lower and "not published" not in lower:
            warnings.append(f"{rid}: language may assume published pages")
        if "click here" in lower and "http" in lower:
            errors.append(f"{rid}: hyperlink-style public reference")

    stats["missing_internal_link_wiring"] = stats["drafts_scanned"]
    warnings.append(
        "Internal link graph wiring remains a pre-publication blocker; "
        "draft-only pages do not require internal_links.json changes in Sprint 5K"
    )

    return errors, warnings, stats


def main() -> int:
    errors, warnings, stats = run_validation()
    print("=== Corpus References L1 Validation ===")
    for k, v in stats.items():
        print(f"{k}: {v}")
    print()
    if errors:
        print("FAIL — errors:")
        for e in errors:
            print(f"  - {e}")
    else:
        print("PASS — no blocking errors")
    if warnings:
        print("\nWarnings:")
        for w in warnings:
            print(f"  - {w}")
    print(f"\nSummary: {'FAIL' if errors else 'PASS'} ({len(errors)} errors, {len(warnings)} warnings)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
