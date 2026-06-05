#!/usr/bin/env python3
"""Sprint 98 — 14K corpus classification audit (read-only classifier, writes audit artifacts)."""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROUTES_PATH = ROOT / "main/data/routes.json"
OUT_JSON = ROOT / "main/data/14K_CORPUS_CLASSIFICATION.json"
OUT_REPORT = ROOT / "main/data/14K_CORPUS_CLASSIFICATION_REPORT.md"

LANES = {
    "A": "Low-risk terminology pages",
    "B": "Language-boundary pages",
    "C": "Disambiguation pages",
    "D": "Compound-family pages",
    "E": "Material/mineral pages",
    "F": "Industrial-context pages",
    "G": "Biotechnology-context pages",
    "H": "Economic/investment-context pages",
    "I": "Journalistic/contextual explainer pages",
    "J": "Academic/reference pages",
    "K": "Institutional/government context pages",
    "L": "Student/general-reader explainer pages",
    "M": "Blocked/high-risk pages requiring source review",
    "HUB": "Atlas hub / foundation / methodology",
}

HUB_ROUTE_IDS = {
    "home", "sources", "corpus_methodology_overview", "internal_linking_discipline",
    "quality_gate_public_explainer", "de_method_corpus_map", "de_method_translator_playbook",
    "en_gov_claim_registry_explainer", "en_gov_hreflang_policy",
    "en_index_disambiguation_map", "en_index_multilingual_map", "en_index_terminology_spine",
}
HUB_ROUTE_PREFIX = "en_foundation_"
BLOCKED_ROUTE_IDS = {"acquire", "newsletter"}


def classify_lane(route: dict) -> str:
    rid = route.get("route_id", "")
    path = route.get("path", "").lower()
    layer = route.get("layer", "")
    if rid in BLOCKED_ROUTE_IDS or layer == "acquisition":
        return "M"
    if rid in HUB_ROUTE_IDS or rid.startswith(HUB_ROUTE_PREFIX) or layer in (
        "gateway", "methodology_reference", "foundation_reference", "utility"
    ):
        if layer == "utility" and rid not in {"sources"}:
            return "M"
        return "HUB"
    if "/dis-" in path or "disambiguation" in rid or layer == "disambiguation":
        return "C"
    if "-cmp-" in path or "/compound" in path:
        return "D"
    if "mos2" in path or "molybdenum" in path or "mineral" in path:
        return "E"
    if "-ind-" in path or layer == "industrial":
        return "F"
    if "biotech" in path or "bio-" in path:
        return "G"
    if "economic" in path or "investor" in path or "market" in path:
        return "H"
    if "-aud-ai-" in path or "-air-res-" in path:
        return "I"
    if "-term-chem-acad" in path or "-cmp-chem-acad" in path:
        return "J"
    if layer in ("foundation_reference",) or "gov" in rid:
        return "K"
    if "-child-" in path or "-aud-stu-" in path or "-term-chem-know" in path:
        return "L"
    if "german" in path or "spelling" in rid or "boundary" in rid:
        return "B"
    if layer == "terminology_system" or "-term-" in path:
        return "A"
    if route.get("risk_level") in ("high", "medium") and route.get("source_required"):
        return "M"
    return "A"


def lane_to_page_type(lane: str, route: dict) -> str:
    mapping = {
        "A": "terminology_node", "B": "language_boundary", "C": "disambiguation",
        "D": "compound_family", "E": "material_mineral", "F": "industrial_context",
        "G": "biotechnology_context", "H": "economic_context", "I": "journalistic_explainer",
        "J": "academic_reference", "K": "institutional_context", "L": "student_explainer",
        "M": "blocked", "HUB": "atlas_hub",
    }
    if route.get("route_id") == "home":
        return "gateway"
    return mapping.get(lane, "terminology_node")


def source_requirement_level(route: dict) -> str:
    if route.get("source_required"):
        return "required"
    if route.get("required_claim_groups"):
        return "claim_group_pending"
    return "cautious_framing_only"


def priority_score(route: dict, lane: str) -> int:
    base = {"HUB": 100, "C": 90, "B": 85, "A": 70, "D": 65, "E": 60, "J": 55,
            "L": 50, "I": 45, "F": 40, "G": 35, "H": 30, "K": 80, "M": 0}
    score = base.get(lane, 50)
    if route.get("risk_level") == "low":
        score += 10
    elif route.get("risk_level") == "high":
        score -= 20
    if not route.get("source_required"):
        score += 15
    return max(0, min(100, score))


def release_eligibility(route: dict, lane: str) -> str:
    rid = route.get("route_id", "")
    if rid in BLOCKED_ROUTE_IDS:
        return "blocked_acquisition_or_utility"
    if lane == "M":
        return "blocked_high_risk_or_source_review"
    if route.get("source_required"):
        return "blocked_source_required"
    if route.get("required_claim_groups") and lane != "HUB":
        return "blocked_claim_groups_pending"
    if lane == "HUB" or (not route.get("source_required") and route.get("risk_level") == "low"):
        return "eligible_atlas_hub_wave"
    return "blocked_pending_source_pack"


def classify_route(route: dict) -> dict:
    lane = classify_lane(route)
    return {
        "route_id": route["route_id"],
        "route_path": route.get("path", ""),
        "current_layer": route.get("layer", ""),
        "proposed_production_lane": lane,
        "production_lane_label": LANES.get(lane, lane),
        "risk_level": route.get("risk_level", "unknown"),
        "source_requirement_level": source_requirement_level(route),
        "template_type": lane_to_page_type(lane, route),
        "priority_score": priority_score(route, lane),
        "release_eligibility": release_eligibility(route, lane),
        "source_required": route.get("source_required", False),
        "status": route.get("status", "planned"),
    }


def write_report(rows: list[dict], lane_counts: Counter, elig_counts: Counter) -> None:
    lines = [
        "# 14K Corpus Classification Report",
        "",
        f"**Sprint:** 98",
        f"**Date:** {date.today().isoformat()}",
        f"**Routes classified:** {len(rows)}",
        "",
        "## Production lane distribution",
        "",
        "| Lane | Label | Count |",
        "|------|-------|------:|",
    ]
    for lane, label in LANES.items():
        lines.append(f"| {lane} | {label} | {lane_counts.get(lane, 0)} |")
    lines.extend([
        "",
        "## Release eligibility",
        "",
        "| Eligibility | Count |",
        "|-------------|------:|",
    ])
    for key, count in elig_counts.most_common():
        lines.append(f"| {key} | {count} |")
    lines.extend([
        "",
        "## Summary",
        "",
        f"- **Eligible atlas hub wave:** {elig_counts.get('eligible_atlas_hub_wave', 0)} routes",
        f"- **Blocked (source required):** {elig_counts.get('blocked_source_required', 0)} routes",
        f"- **Blocked (high risk / review):** {elig_counts.get('blocked_high_risk_or_source_review', 0)} routes",
        "",
        "Full per-route classification: `main/data/14K_CORPUS_CLASSIFICATION.json`",
    ])
    OUT_REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    print("=" * 60)
    print("Sprint 98 — 14K Corpus Classification Audit")
    print(f"Date: {date.today().isoformat()}")
    print("=" * 60)
    routes = json.loads(ROUTES_PATH.read_text(encoding="utf-8"))["routes"]
    rows = [classify_route(r) for r in routes]
    lane_counts = Counter(r["proposed_production_lane"] for r in rows)
    elig_counts = Counter(r["release_eligibility"] for r in rows)
    payload = {
        "sprint": "98",
        "date": date.today().isoformat(),
        "route_count": len(rows),
        "lane_distribution": dict(lane_counts),
        "release_eligibility_distribution": dict(elig_counts),
        "routes": rows,
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    write_report(rows, lane_counts, elig_counts)
    print(f"Classified: {len(rows)} routes")
    print(f"Eligible atlas hub wave: {elig_counts.get('eligible_atlas_hub_wave', 0)}")
    print(f"Blocked source required: {elig_counts.get('blocked_source_required', 0)}")
    print(f"Output: {OUT_JSON}")
    print(f"Report: {OUT_REPORT}")
    print("CLASSIFICATION: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
