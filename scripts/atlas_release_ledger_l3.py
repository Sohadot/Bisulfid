#!/usr/bin/env python3
"""Sprint 99 — Build full 14K release ledger from dossier audit."""
from __future__ import annotations

import json
import sys
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / "main/data/14K_DOSSIER_RELEASE_AUDIT.json"
OUT_LEDGER = ROOT / "main/data/release_ledger.json"
OUT_REPORT = ROOT / "main/data/14K_RELEASE_LEDGER_REPORT.md"


def main() -> int:
    print("=" * 60)
    print("Sprint 99 — 14K Release Ledger")
    print("=" * 60)
    if not AUDIT_PATH.is_file():
        print("ERROR: run atlas_dossier_audit_l3.py first")
        return 1
    audit = json.loads(AUDIT_PATH.read_text(encoding="utf-8"))
    records = []
    released = blocked = 0
    for row in audit["routes"]:
        elig = row["release_eligibility"]
        if elig == "released":
            released += 1
            status = "released"
            blockers = []
            public_status = "public_dossier"
            validation_status = "pending"
            source_pack = "SPK-SPEKTRUM-MOS2-DE" if row["release_mode"] == "source_verified_page" else None
            claim_basis = "CLM-TERM-MOS2-DE-001" if row["release_mode"] == "source_verified_page" else "CLM-CAUTIOUS-ATLAS-001"
        else:
            blocked += 1
            status = "blocked"
            blockers = ["blocked_high_risk"]
            public_status = "not_indexed"
            validation_status = "not_applicable"
            source_pack = None
            claim_basis = None
        records.append({
            "route_id": row["route_id"],
            "route_path": row["route_path"],
            "production_lane": row["lane"],
            "page_type": row["page_type"],
            "release_mode": row["release_mode"],
            "source_pack_id": source_pack,
            "cautious_framing_basis": claim_basis if status == "released" else None,
            "claim_set_id": "cautious_framing" if status == "released" else None,
            "release_status": status,
            "public_status": public_status,
            "indexable": row["indexable"],
            "sitemap_file": row.get("sitemap_shard"),
            "validation_status": validation_status,
            "blockers": blockers,
            "internal_link_targets": row.get("internal_link_targets", []),
        })
    ledger = {
        "sprint": "99",
        "date": date.today().isoformat(),
        "total_routes": len(records),
        "released_count": released,
        "blocked_count": blocked,
        "records": records,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, indent=2), encoding="utf-8")
    shard_counts = Counter(r["sitemap_file"] for r in records if r["release_status"] == "released")
    lines = [
        "# 14K Release Ledger Report",
        "",
        f"**Date:** {date.today().isoformat()}",
        f"**Total routes:** {len(records)}",
        f"**Released:** {released}",
        f"**Blocked:** {blocked}",
        "",
        "## Sitemap shard counts",
        "",
    ]
    for shard, count in sorted(shard_counts.items()):
        lines.append(f"- `{shard}`: {count}")
    OUT_REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Released: {released}")
    print(f"Blocked: {blocked}")
    print(f"Ledger: {OUT_LEDGER}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
