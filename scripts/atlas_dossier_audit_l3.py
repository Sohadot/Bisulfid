#!/usr/bin/env python3
"""Sprint 99 — Full 14K dossier release audit."""
from __future__ import annotations

import json
import sys
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from atlas_dossier_common_l3 import (  # noqa: E402
    SITE_BASE,
    assign_release_mode,
    build_lane_index,
    build_path_index,
    internal_link_targets,
    load_classification,
    load_release_model,
    load_routes,
    sitemap_shard_for,
)

OUT_JSON = ROOT / "main/data/14K_DOSSIER_RELEASE_AUDIT.json"
OUT_REPORT = ROOT / "main/data/14K_PUBLIC_REFERENCE_DOSSIER_RELEASE_REPORT.md"


def main() -> int:
    print("=" * 60)
    print("Sprint 99 — 14K Dossier Release Audit")
    print(f"Date: {date.today().isoformat()}")
    print("=" * 60)
    routes = load_routes()
    routes_by_id = {r["route_id"]: r for r in routes}
    classification = load_classification()
    model = load_release_model()
    path_index = build_path_index(routes)
    lane_index = build_lane_index(routes, classification)
    urls_per_shard = model.get("sitemap_urls_per_shard", 2500)
    lane_counters = {"A": 0, "CTX": 0}
    records = []
    mode_counts: Counter = Counter()
    shard_counts: Counter = Counter()
    for route in routes:
        rid = route["route_id"]
        cls = classification.get(rid, {})
        lane = cls.get("proposed_production_lane", "A")
        page_type = cls.get("template_type", "terminology_node")
        release_mode = assign_release_mode(route, cls)
        mode_counts[release_mode] += 1
        indexable = release_mode != "blocked_high_risk"
        shard = None
        if indexable:
            shard = sitemap_shard_for(lane, lane_counters, urls_per_shard)
            shard_counts[shard] += 1
        links = (
            internal_link_targets(rid, route, routes_by_id, path_index, lane_index, classification)
            if indexable else []
        )
        path = route.get("path", "/")
        records.append({
            "route_id": rid,
            "route_path": path,
            "lane": lane,
            "page_type": page_type,
            "release_mode": release_mode,
            "source_risk": route.get("risk_level", "unknown"),
            "claim_risk": "high" if route.get("required_claim_groups") else "cautious_framing",
            "internal_link_group": path.strip("/").split("/")[0] if path.strip("/") else "root",
            "sitemap_shard": shard,
            "canonical_url": SITE_BASE + (path if path.endswith("/") else path + "/"),
            "release_eligibility": "released" if indexable else "blocked",
            "internal_link_targets": links,
            "indexable": indexable,
        })
    payload = {
        "sprint": "99",
        "date": date.today().isoformat(),
        "route_count": len(records),
        "release_mode_distribution": dict(mode_counts),
        "sitemap_shard_distribution": dict(shard_counts),
        "released_count": sum(1 for r in records if r["release_eligibility"] == "released"),
        "blocked_count": sum(1 for r in records if r["release_eligibility"] == "blocked"),
        "routes": records,
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    lines = [
        "# 14K Public Reference Dossier Release Report",
        "",
        f"**Date:** {date.today().isoformat()}",
        f"**Routes audited:** {len(records)}",
        f"**Released (dossier):** {payload['released_count']}",
        f"**Blocked:** {payload['blocked_count']}",
        "",
        "## Release mode distribution",
        "",
        "| Mode | Count |",
        "|------|------:|",
    ]
    for mode, count in mode_counts.most_common():
        lines.append(f"| {mode} | {count} |")
    lines.extend(["", "## Sitemap shards", "", "| Shard | URLs |", "|-------|-----:|"])
    for shard, count in sorted(shard_counts.items()):
        lines.append(f"| {shard} | {count} |")
    lines.extend([
        "",
        "## Model",
        "",
        "- Default: cautious_reference_dossier",
        "- Blocked only: acquire, newsletter",
        "",
        f"Full audit: `{OUT_JSON.name}`",
    ])
    OUT_REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Audited: {len(records)}")
    print(f"Released: {payload['released_count']}")
    print(f"Blocked: {payload['blocked_count']}")
    print(f"Output: {OUT_JSON}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
