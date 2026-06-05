#!/usr/bin/env python3
"""Sprint 98 — Build release ledger from corpus classification."""
from __future__ import annotations

import json
import sys
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLASS_PATH = ROOT / "main/data/14K_CORPUS_CLASSIFICATION.json"
ROUTES_PATH = ROOT / "main/data/routes.json"
OUT_LEDGER = ROOT / "main/data/release_ledger.json"
OUT_REPORT = ROOT / "main/data/RELEASE_LEDGER_REPORT.md"

ATLAS_HUB_LINKS: dict[str, list[str]] = {
    "home": ["en_foundation_sovereign_intro", "en_index_terminology_spine", "en_index_disambiguation_map", "sources", "corpus_methodology_overview", "en_foundation_methodology", "en_index_multilingual_map"],
    "sources": ["home", "corpus_methodology_overview", "en_foundation_source_policy", "en_foundation_methodology", "en_index_terminology_spine", "en_gov_claim_registry_explainer", "en_foundation_sovereign_intro"],
    "corpus_methodology_overview": ["home", "en_foundation_methodology", "internal_linking_discipline", "quality_gate_public_explainer", "sources", "en_foundation_knowledge_reliability", "en_index_terminology_spine"],
    "internal_linking_discipline": ["corpus_methodology_overview", "en_foundation_methodology", "en_index_terminology_spine", "home", "sources", "en_foundation_reference_layers", "en_foundation_audience_layers"],
    "quality_gate_public_explainer": ["corpus_methodology_overview", "en_foundation_methodology", "en_foundation_knowledge_reliability", "home", "sources", "en_foundation_claim_policy", "en_foundation_source_policy"],
    "en_gov_claim_registry_explainer": ["en_foundation_claim_policy", "sources", "corpus_methodology_overview", "home", "en_foundation_methodology", "en_foundation_knowledge_reliability", "en_foundation_source_policy"],
    "en_gov_hreflang_policy": ["en_foundation_multilingual_overview", "en_index_multilingual_map", "home", "corpus_methodology_overview", "en_foundation_methodology", "sources", "en_index_terminology_spine"],
    "en_index_disambiguation_map": ["en_index_terminology_spine", "home", "en_foundation_sovereign_intro", "sources", "corpus_methodology_overview", "en_foundation_chemical_language_governance", "en_index_multilingual_map"],
    "en_index_multilingual_map": ["en_foundation_multilingual_overview", "en_gov_hreflang_policy", "home", "en_index_terminology_spine", "sources", "corpus_methodology_overview", "en_foundation_methodology"],
    "en_index_terminology_spine": ["home", "en_index_disambiguation_map", "en_index_multilingual_map", "sources", "corpus_methodology_overview", "en_foundation_sovereign_intro", "en_foundation_reference_layers"],
    "de_method_corpus_map": ["home", "en_index_multilingual_map", "en_foundation_multilingual_overview", "corpus_methodology_overview", "sources", "en_foundation_methodology", "de_method_translator_playbook"],
    "de_method_translator_playbook": ["de_method_corpus_map", "en_foundation_multilingual_overview", "en_gov_hreflang_policy", "corpus_methodology_overview", "home", "sources", "en_foundation_methodology"],
}

FOUNDATION_LINKS = [
    "home", "en_foundation_sovereign_intro", "en_foundation_methodology", "sources",
    "corpus_methodology_overview", "en_index_terminology_spine", "en_index_disambiguation_map",
]

for fid in [
    "en_foundation_sovereign_intro", "en_foundation_institutional_purpose", "en_foundation_methodology",
    "en_foundation_source_policy", "en_foundation_claim_policy", "en_foundation_knowledge_reliability",
    "en_foundation_multilingual_overview", "en_foundation_reference_layers", "en_foundation_audience_layers",
    "en_foundation_chemical_language_governance", "en_foundation_ai_readable_policy",
    "en_foundation_child_safe_policy", "en_foundation_economic_institutional_restrictions",
    "en_foundation_corpus_status", "en_foundation_launch_status",
]:
    ATLAS_HUB_LINKS.setdefault(fid, FOUNDATION_LINKS)


def sitemap_shard(route: dict, lane: str) -> str:
    path = route.get("path", "")
    if route.get("route_id") == "home":
        return "sitemap-core.xml"
    if "/foundation/" in path:
        return "sitemap-core.xml"
    if path.startswith("/de/"):
        return "sitemap-languages.xml"
    if "disambiguation" in path or "terminology-spine" in path or "multilingual" in path:
        return "sitemap-languages.xml"
    if "methodology" in path or "quality-gate" in path or "internal-linking" in path:
        return "sitemap-context.xml"
    return "sitemap-core.xml"


def main() -> int:
    print("=" * 60)
    print("Sprint 98 — Release Ledger Builder")
    print("=" * 60)
    if not CLASS_PATH.is_file():
        print("ERROR: run atlas_corpus_classifier_l2.py first")
        return 1
    classification = json.loads(CLASS_PATH.read_text(encoding="utf-8"))
    routes_by_id = {r["route_id"]: r for r in json.loads(ROUTES_PATH.read_text(encoding="utf-8"))["routes"]}
    class_by_id = {r["route_id"]: r for r in classification["routes"]}
    records = []
    released = 0
    blocked = 0
    for rid, cls in class_by_id.items():
        route = routes_by_id.get(rid)
        if not route:
            continue
        elig = cls["release_eligibility"]
        if elig == "eligible_atlas_hub_wave":
            status = "released"
            blockers = []
            released += 1
        else:
            status = "blocked"
            blockers = [elig]
            blocked += 1
        records.append({
            "route_id": rid,
            "route_path": route.get("path", ""),
            "production_lane": cls["proposed_production_lane"],
            "page_type": cls["template_type"],
            "source_pack_id": "SPK-CAUTIOUS-FRAMING" if status == "released" else None,
            "cautious_framing_basis": "CLM-CAUTIOUS-ATLAS-001" if status == "released" else None,
            "claim_set_id": "cautious_framing" if status == "released" else None,
            "release_status": status,
            "indexable": status == "released",
            "sitemap_file": sitemap_shard(route, cls["proposed_production_lane"]) if status == "released" else None,
            "validation_status": "pending" if status == "released" else "not_applicable",
            "blockers": blockers,
            "internal_link_targets": ATLAS_HUB_LINKS.get(rid, []) if status == "released" else [],
        })
    ledger = {
        "sprint": "98",
        "date": date.today().isoformat(),
        "total_routes": len(records),
        "released_count": released,
        "blocked_count": blocked,
        "records": records,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, indent=2), encoding="utf-8")
    lines = [
        "# Release Ledger Report",
        "",
        f"**Date:** {date.today().isoformat()}",
        f"**Total routes:** {len(records)}",
        f"**Released (wave 2 atlas hubs):** {released}",
        f"**Blocked:** {blocked}",
        "",
        "## Release status distribution",
        "",
        f"| Status | Count |",
        f"|--------|------:|",
        f"| released | {released} |",
        f"| blocked | {blocked} |",
        "",
        "Source of truth: `main/data/release_ledger.json`",
    ]
    OUT_REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Released: {released}")
    print(f"Blocked: {blocked}")
    print(f"Ledger: {OUT_LEDGER}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
