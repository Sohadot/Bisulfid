#!/usr/bin/env python3
"""Sprint 99B-H — Align legacy public hub pages to sovereign semantic shell."""
from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from atlas_hub_semantic_99bh import HUB_REQUIRED_PATHS, align_hub  # noqa: E402

PUBLIC_DIR = ROOT / "site/public"


def main() -> int:
    print("=" * 60)
    print("Sprint 99B-H — Legacy Hub Semantic Shell Alignment")
    print(f"Date: {date.today().isoformat()}")
    print("=" * 60)
    aligned = 0
    skipped = 0
    errors: list[str] = []
    for route_path in HUB_REQUIRED_PATHS:
        if route_path == "/methodology/":
            target = PUBLIC_DIR / "methodology" / "index.html"
            if not target.is_file():
                print(f"  SKIP (not present): {route_path}")
                skipped += 1
                continue
        ok, msg = align_hub(route_path, PUBLIC_DIR)
        if ok:
            print(f"  ALIGNED: {route_path}")
            aligned += 1
        else:
            print(f"  FAIL: {route_path} — {msg}")
            errors.append(f"{route_path}: {msg}")
    print(f"\nAligned: {aligned}  Skipped: {skipped}  Errors: {len(errors)}")
    if errors:
        return 1
    print("99B-H HUB ALIGNMENT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
