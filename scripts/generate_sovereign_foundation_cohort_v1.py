#!/usr/bin/env python3
"""Sovereign Content Automation Engine v1 — COHORT_01 foundation drafts (Sprint 6D).

Registry-constrained, deterministic draft generation. No LLM. No routes.json writes.
Read-only on source/claim registries. Stdlib only.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REGISTRY_PATHS = {
    "corpus_route_formula": ROOT / "main/data/corpus_route_formula.json",
    "page_type_registry": ROOT / "main/data/page_type_registry.json",
    "audience_layer_registry": ROOT / "main/data/audience_layer_registry.json",
    "reference_layer_registry": ROOT / "main/data/reference_layer_registry.json",
    "generator_schema": ROOT / "main/data/SOVEREIGN_CORPUS_GENERATOR_SCHEMA_WAVE_1.json",
    "template_contract": ROOT / "main/data/SOVEREIGN_TEMPLATE_CONTRACT_MODEL_WAVE_1.json",
    "evidence_grades": ROOT / "main/data/SOVEREIGN_EVIDENCE_GRADE_REGISTRY_WAVE_1.json",
    "source_hierarchy": ROOT / "main/data/SOVEREIGN_SOURCE_HIERARCHY_MODEL_WAVE_1.json",
    "source_registry": ROOT / "main/data/sources/source_registry.json",
    "terminology_claims": ROOT / "main/data/claims/terminology_claims.json",
    "routes": ROOT / "main/data/routes.json",
}

OUTPUT_MANIFEST = ROOT / "main/data/SOVEREIGN_CONTENT_AUTOMATION_ENGINE_V1_DRY_RUN_MANIFEST.json"
OUTPUT_BLUEPRINTS = ROOT / "main/data/SOVEREIGN_CONTENT_AUTOMATION_ENGINE_V1_DRAFT_BLUEPRINTS.json"

FOUNDATION_TEMPLATE_ID = "TPL_FOUNDATION_GOV_V1"
COHORT_ID = "COHORT_01_FOUNDATION_GOV"

EXCLUDED_CLAIM_CLASSES = [
    "safety", "medical", "market", "procurement", "production", "pricing",
    "trade", "CAGR", "acquisition", "operational_handling_guidance",
]

FORBIDDEN_BODY_PHRASES = [
    "market share", "cagr", "handling instructions", "medical advice",
    "procurement guide", "investment recommendation", "production data",
]

COHORT_01_UNITS = [
    {
        "theme_id": 1,
        "route_id": "en_foundation_sovereign_intro",
        "slug": "sovereign-reference-introduction",
        "h1": "Sovereign Reference Introduction",
        "page_type_id": "PT_FOUNDATION",
        "reference_layer_id": "REF_KNOWLEDGE",
        "internal_link_role": "language_hub",
        "summary": "What bisulfid.com is as a governed multilingual reference asset.",
        "bullets": [
            "Defines the sovereign reference mission",
            "Explains visible foundation versus hidden governance",
            "States 14,000-page governed corpus direction without claiming completion",
        ],
    },
    {
        "theme_id": 2,
        "route_id": "en_foundation_institutional_purpose",
        "slug": "institutional-purpose",
        "h1": "Institutional Purpose",
        "page_type_id": "PT_FOUNDATION",
        "reference_layer_id": "REF_INSTITUTIONAL",
        "internal_link_role": "language_hub",
        "summary": "Why bisulfid.com exists as an institutional reference surface.",
        "bullets": [
            "Institutional trust posture",
            "Not a marketplace or textbook",
            "Governed terminology and source discipline",
        ],
    },
    {
        "theme_id": 3,
        "route_id": "en_foundation_methodology",
        "slug": "methodology",
        "h1": "Corpus Methodology",
        "page_type_id": "PT_METHODOLOGY_GOVERNANCE",
        "reference_layer_id": "REF_ACADEMIC",
        "internal_link_role": "language_hub",
        "summary": "How governed pages are authored, validated, and batched.",
        "bullets": [
            "Wave protocol reference",
            "Validator gates G0 through G7",
            "Human review triggers",
        ],
    },
    {
        "theme_id": 4,
        "route_id": "en_foundation_source_policy",
        "slug": "source-policy-overview",
        "h1": "Source Policy Overview",
        "page_type_id": "PT_METHODOLOGY_GOVERNANCE",
        "reference_layer_id": "REF_INSTITUTIONAL",
        "internal_link_role": "source_hub",
        "summary": "How sources are registered, verified, and bound to pages.",
        "bullets": [
            "No source entry equals no published claim",
            "Source hierarchy is not flattened",
            "Registry inactive posture documented",
        ],
    },
    {
        "theme_id": 5,
        "route_id": "en_foundation_claim_policy",
        "slug": "claim-policy-overview",
        "h1": "Claim Policy Overview",
        "page_type_id": "PT_METHODOLOGY_GOVERNANCE",
        "reference_layer_id": "REF_INSTITUTIONAL",
        "internal_link_role": "claim_hub",
        "summary": "How claims are registered, approved, and bounded.",
        "bullets": [
            "Claim registries inactive for publication",
            "Narrow approval_limited posture",
            "Approved does not mean publication",
        ],
    },
    {
        "theme_id": 6,
        "route_id": "en_foundation_knowledge_reliability",
        "slug": "knowledge-reliability-model",
        "h1": "Knowledge Reliability Model",
        "page_type_id": "PT_METHODOLOGY_GOVERNANCE",
        "reference_layer_id": "REF_RESEARCH",
        "internal_link_role": "language_hub",
        "summary": "Epistemic credibility: evidence grades and reliability profiles.",
        "bullets": [
            "Eight evidence grades",
            "Reliability profile required on every page",
            "Never state more than evidence allows",
        ],
    },
    {
        "theme_id": 7,
        "route_id": "en_foundation_multilingual_overview",
        "slug": "multilingual-corpus-overview",
        "h1": "Multilingual Corpus Overview",
        "page_type_id": "PT_FOUNDATION",
        "reference_layer_id": "REF_LINGUISTIC",
        "internal_link_role": "language_hub",
        "summary": "Seven language layers and hreflang readiness.",
        "bullets": [
            "English institutional base",
            "Expansion languages ar de fr es ja zh",
            "No machine-translation spam",
        ],
    },
    {
        "theme_id": 8,
        "route_id": "en_foundation_reference_layers",
        "slug": "reference-layer-overview",
        "h1": "Reference Layer Overview",
        "page_type_id": "PT_FOUNDATION",
        "reference_layer_id": "REF_KNOWLEDGE",
        "internal_link_role": "language_hub",
        "summary": "Nine reference layers and anti-duplication rules.",
        "bullets": [
            "Academic through logistical layers",
            "Layer changes page purpose",
            "Not repetition by audience label only",
        ],
    },
    {
        "theme_id": 9,
        "route_id": "en_foundation_audience_layers",
        "slug": "audience-layer-overview",
        "h1": "Audience Layer Overview",
        "page_type_id": "PT_FOUNDATION",
        "reference_layer_id": "REF_KNOWLEDGE",
        "internal_link_role": "audience_hub",
        "summary": "Nine audience layers and claim class restrictions.",
        "bullets": [
            "Chemists through child_edu audiences",
            "Audience is a route dimension",
            "Forbidden classes per audience",
        ],
    },
    {
        "theme_id": 10,
        "route_id": "en_foundation_chemical_language_governance",
        "slug": "chemical-language-governance-framework",
        "h1": "Chemical-Language Governance Framework",
        "page_type_id": "PT_METHODOLOGY_GOVERNANCE",
        "reference_layer_id": "REF_ACADEMIC",
        "internal_link_role": "term_hub",
        "summary": "Governance of chemical-language meaning across languages.",
        "bullets": [
            "Terminology versus operational instruction",
            "Dictionary versus market evidence separation",
            "Comparison intent as core reference class",
        ],
    },
    {
        "theme_id": 11,
        "route_id": "en_foundation_ai_readable_policy",
        "slug": "ai-readable-reference-policy",
        "h1": "AI-Readable Reference Policy",
        "page_type_id": "PT_METHODOLOGY_GOVERNANCE",
        "reference_layer_id": "REF_TECHNICAL",
        "internal_link_role": "AI_reference_hub",
        "summary": "Machine-readable pages with provenance disclosure.",
        "bullets": [
            "Structured provenance blocks",
            "Excluded claims visible",
            "No inferred facts beyond registry",
        ],
    },
    {
        "theme_id": 12,
        "route_id": "en_foundation_child_safe_policy",
        "slug": "child-safe-educational-policy",
        "h1": "Child-Safe Educational Policy",
        "page_type_id": "PT_METHODOLOGY_GOVERNANCE",
        "reference_layer_id": "REF_EDUCATIONAL",
        "internal_link_role": "education_hub",
        "summary": "Educational pages without hazard or experiment instruction.",
        "bullets": [
            "Vocabulary ladder",
            "No handling or medical content",
            "Educational simplification limits",
        ],
    },
    {
        "theme_id": 13,
        "route_id": "en_foundation_economic_institutional_restrictions",
        "slug": "economic-institutional-claim-restrictions",
        "h1": "Economic and Institutional Claim Restrictions",
        "page_type_id": "PT_METHODOLOGY_GOVERNANCE",
        "reference_layer_id": "REF_ECONOMIC",
        "internal_link_role": "language_hub",
        "summary": "Blocks on unsupported market and institutional claims.",
        "bullets": [
            "No unsourced CAGR or pricing",
            "Terminology source is not market evidence",
            "Not investment advice",
        ],
    },
    {
        "theme_id": 14,
        "route_id": "en_foundation_corpus_status",
        "slug": "corpus-status",
        "h1": "Corpus Status",
        "page_type_id": "PT_CORPUS_STATUS",
        "reference_layer_id": "REF_INSTITUTIONAL",
        "internal_link_role": "language_hub",
        "summary": "Current corpus locks and production posture.",
        "bullets": [
            "Registered routes posture from planner",
            "production_can_safely_proceed remains no",
            "Locks documented",
        ],
    },
    {
        "theme_id": 15,
        "route_id": "en_foundation_launch_status",
        "slug": "launch-status-non-public-corpus",
        "h1": "Launch Status and Non-Public Corpus",
        "page_type_id": "PT_CORPUS_STATUS",
        "reference_layer_id": "REF_INSTITUTIONAL",
        "internal_link_role": "language_hub",
        "summary": "Why the corpus remains non-public and pre-launch.",
        "bullets": [
            "No indexation",
            "Foundation cohort pre-route",
            "Controlled visibility plan deferred",
        ],
    },
]


def load_json(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"Missing registry: {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def load_registries() -> dict:
    return {key: load_json(path) for key, path in REGISTRY_PATHS.items()}


def index_page_types(reg: dict) -> dict[str, dict]:
    return {p["page_type_id"]: p for p in reg.get("page_types", [])}


def index_reference_layers(reg: dict) -> dict[str, dict]:
    return {r["reference_layer_id"]: r for r in reg.get("reference_layers", [])}


def index_templates(reg: dict) -> dict[str, dict]:
    return {t["template_id"]: t for t in reg.get("templates", [])}


def evidence_grade_for_unit(unit: dict) -> str:
    if unit["reference_layer_id"] == "REF_ECONOMIC":
        return "economic_context_pending"
    return "claim_not_required"


def build_reliability_profile(unit: dict, evidence_grade: str) -> dict:
    return {
        "knowledge_reliability_level": "L2_draft_cautious",
        "evidence_grade": evidence_grade,
        "source_hierarchy": "unsourced_pending",
        "source_count_required": 0,
        "primary_source_required": False,
        "secondary_source_allowed": False,
        "claim_boundary_required": False,
        "claim_confidence": "unsettled",
        "citation_mode": "doctrine_reference",
        "provenance_note": "Governance doctrine and 6A-6C architecture — not chemical fact claims",
        "last_reviewed_policy": "cohort_generation_date",
        "unresolved_fields": [
            "public_route_merge",
            "multilingual_expansion",
            "indexation",
        ],
        "excluded_claim_classes": EXCLUDED_CLAIM_CLASSES,
        "conflict_resolution_policy": "defer_to_registry",
        "human_review_required": True,
        "machine_readability_level": "standard" if unit["reference_layer_id"] != "REF_TECHNICAL" else "structured",
        "audience_simplification_limit": "n/a",
        "page_assertion_limit": "governance_framing_only",
    }


def validate_unit(
    unit: dict,
    page_types: dict[str, dict],
    ref_layers: dict[str, dict],
    template: dict,
) -> list[str]:
    errors: list[str] = []
    pt = unit.get("page_type_id")
    rl = unit.get("reference_layer_id")
    if pt not in page_types:
        errors.append(f"{unit['route_id']}: unknown page_type_id {pt!r}")
    if rl not in ref_layers:
        errors.append(f"{unit['route_id']}: unknown reference_layer_id {rl!r}")
    applicable = template.get("applicable_page_types", [])
    if pt not in applicable:
        errors.append(f"{unit['route_id']}: page_type {pt!r} not in {FOUNDATION_TEMPLATE_ID} applicable types")
    if unit.get("indexable") is True or unit.get("in_sitemap") is True or unit.get("in_navigation") is True:
        errors.append(f"{unit['route_id']}: public activation forbidden")
    for field in ("route_id", "slug", "h1", "summary", "bullets"):
        if not unit.get(field):
            errors.append(f"{unit['route_id']}: missing required field {field!r}")
    return errors


def build_draft_unit(unit: dict, registries: dict) -> dict:
    evidence_grade = evidence_grade_for_unit(unit)
    profile = build_reliability_profile(unit, evidence_grade)
    content_file = f"main/content/en/pages/foundation/{unit['slug']}.md"
    path = f"/en/foundation/{unit['slug']}/"
    return {
        "theme_id": unit["theme_id"],
        "route_id": unit["route_id"],
        "language": "en",
        "locale": "en",
        "source_language": "en",
        "page_type_id": unit["page_type_id"],
        "audience_id": "ALL",
        "reference_layer_id": unit["reference_layer_id"],
        "template_id": FOUNDATION_TEMPLATE_ID,
        "source_posture": "source_not_required",
        "claim_posture": "claim_not_required",
        "route_state": "draft_backed",
        "indexation_state": "noindex_default",
        "internal_link_role": unit["internal_link_role"],
        "indexable": False,
        "in_sitemap": False,
        "in_navigation": False,
        "noindex_default": True,
        "production_route_registry": False,
        "evidence_grade": evidence_grade,
        "knowledge_reliability_profile": profile,
        "excluded_claim_classes": EXCLUDED_CLAIM_CLASSES,
        "unresolved_field_behavior": "status_fields_from_planner",
        "validation_gates": ["G0", "G1", "G2", "G4", "G7"],
        "content_file": content_file,
        "path": path,
        "title": f"{unit['h1']} — bisulfid.com",
        "h1": unit["h1"],
        "hreflang_group": f"foundation_{unit['slug'].replace('-', '_')}",
        "cohort_id": COHORT_ID,
    }


def render_draft_markdown(draft: dict, unit: dict) -> str:
    bullets = "\n".join(f"- {b}" for b in unit["bullets"])
    excluded = ", ".join(EXCLUDED_CLAIM_CLASSES)
    profile = draft["knowledge_reliability_profile"]
    return f"""---
route_id: {draft['route_id']}
status: draft
publication_status: non_public
indexable: false
in_sitemap: false
language: en
locale: en
source_language: en
template_id: {draft['template_id']}
page_type_id: {draft['page_type_id']}
audience_id: ALL
reference_layer_id: {draft['reference_layer_id']}
evidence_grade: {draft['evidence_grade']}
knowledge_reliability_level: {profile['knowledge_reliability_level']}
cohort_id: {COHORT_ID}
generated: true
engine: sovereign_content_automation_engine_v1
noindex_default: true
---
# {unit['h1']}

**Draft status:** This page is a **non-public** foundation cohort draft generated by Content Automation Engine v1. It is **not published**, **not indexable**, **not in the sitemap**, **not in navigation**, and **not publication-ready**. Content describes governance posture only. **No claim is approved** for publication from this page alone.

## Page role

Controlled **foundation cohort** page (`route_id`: `{draft['route_id']}`) for **{unit['h1']}** — {COHORT_ID}. {unit['summary']}

## Core content

{bullets}

Factual chemistry, market, safety, or industrial lines on terminology routes remain **[SOURCE REQUIRED]** until separately governed. This page does not remove markers elsewhere.

## Knowledge reliability profile

| Field | Value |
| --- | --- |
| knowledge_reliability_level | {profile['knowledge_reliability_level']} |
| evidence_grade | {profile['evidence_grade']} (governance framing) |
| source_posture | source_not_required |
| claim_posture | claim_not_required |
| excluded_claim_classes | {excluded} |
| unresolved_fields | public route merge; multilingual expansion; indexation |
| provenance_note | {profile['provenance_note']} |

## Source and claim status

- Source registries: **inactive** for publication; individual verified sources may exist.
- Approved claims: **do not** imply this foundation page is publication-ready.
- Source-locking: **not complete** for the wider corpus.

## Publication blockers

- Route not in production routes.json until merge charter.
- `indexable: false`; `in_sitemap: false`; `in_navigation: false`.
- `production_can_safely_proceed: no`.

## Internal reference role

Foundation hub slice — internal reference by `route_id` `{draft['route_id']}` only; no markdown links in this draft.

*Non-public foundation draft — {COHORT_ID} — engine v1.*
"""


def scan_narrative_forbidden(unit: dict) -> list[str]:
    """Scan only author-facing narrative fields — not reliability metadata tables."""
    narrative = " ".join([unit["h1"], unit["summary"], *unit["bullets"]]).lower()
    hits = []
    for phrase in FORBIDDEN_BODY_PHRASES:
        if phrase in narrative:
            idx = narrative.find(phrase)
            window = narrative[max(0, idx - 40):idx]
            negated = any(n in window for n in ("not ", "no ", "never ", "without "))
            if not negated:
                hits.append(phrase)
    return hits


def run_engine(write_drafts: bool) -> int:
    print("=== Sovereign Content Automation Engine v1 ===")
    print(f"Date: {date.today().isoformat()}")
    print(f"Mode: {'write_drafts' if write_drafts else 'dry_run_manifest_only'}")
    print(f"Root: {ROOT}")
    print()

    registries = load_registries()
    page_types = index_page_types(registries["page_type_registry"])
    ref_layers = index_reference_layers(registries["reference_layer_registry"])
    templates = index_templates(registries["template_contract"])
    foundation_tpl = templates.get(FOUNDATION_TEMPLATE_ID)
    if not foundation_tpl:
        print(f"FAIL — template {FOUNDATION_TEMPLATE_ID} not found")
        return 1

    routes_count = len(registries["routes"].get("routes", []))
    errors: list[str] = []
    drafts: list[dict] = []

    for unit in COHORT_01_UNITS:
        unit_errors = validate_unit(unit, page_types, ref_layers, foundation_tpl)
        if unit_errors:
            errors.extend(unit_errors)
            continue
        draft = build_draft_unit(unit, registries)
        for forbidden in ("indexable", "in_sitemap", "in_navigation"):
            if draft.get(forbidden):
                errors.append(f"{draft['route_id']}: {forbidden} must be false")
        body = render_draft_markdown(draft, unit)
        forbidden_hits = scan_narrative_forbidden(unit)
        if forbidden_hits:
            errors.append(f"{draft['route_id']}: forbidden phrases: {forbidden_hits}")
        draft["body_byte_length"] = len(body.encode("utf-8"))
        draft["engine_validated"] = True
        drafts.append({**draft, "_unit": unit, "_body": body})

    if errors:
        print("FAIL — validation errors:")
        for e in errors:
            print(f"  - {e}")
        return 1

    manifest = {
        "version": "1.0.0",
        "engine": "sovereign_content_automation_engine_v1",
        "sprint": "6D",
        "cohort_id": COHORT_ID,
        "date": date.today().isoformat(),
        "mode": "write_drafts" if write_drafts else "dry_run",
        "deterministic": True,
        "llm_used": False,
        "routes_json_modified": False,
        "production_route_registry": False,
        "unit_count": len(drafts),
        "registered_routes_unchanged": routes_count,
        "registries_read": list(REGISTRY_PATHS.keys()),
        "units": [{k: v for k, v in d.items() if not k.startswith("_")} for d in drafts],
    }

    blueprints = {
        "version": "1.0.0",
        "engine": "sovereign_content_automation_engine_v1",
        "cohort_id": COHORT_ID,
        "production_route_registry": False,
        "routes": [
            {
                "route_id": d["route_id"],
                "path": d["path"],
                "title": d["title"],
                "h1": d["h1"],
                "content_file": d["content_file"],
                "page_type_id": d["page_type_id"],
                "reference_layer_id": d["reference_layer_id"],
                "template_id": d["template_id"],
                "indexable": False,
                "in_sitemap": False,
                "in_navigation": False,
            }
            for d in drafts
        ],
    }

    OUTPUT_MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    OUTPUT_BLUEPRINTS.write_text(json.dumps(blueprints, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT_MANIFEST.relative_to(ROOT)}")
    print(f"Wrote {OUTPUT_BLUEPRINTS.relative_to(ROOT)}")

    written = 0
    if write_drafts:
        for d in drafts:
            out = ROOT / d["content_file"]
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(d["_body"], encoding="utf-8")
            written += 1
        print(f"Wrote {written} draft files under main/content/en/pages/foundation/")
    else:
        print("Draft files not written (use --write-drafts to emit content)")

    print()
    print(f"PASS — {len(drafts)} COHORT_01 units validated")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Sovereign Content Automation Engine v1")
    parser.add_argument(
        "--write-drafts",
        action="store_true",
        help="Write non-public foundation draft markdown files (schema-safe)",
    )
    args = parser.parse_args()
    return run_engine(write_drafts=args.write_drafts)


if __name__ == "__main__":
    sys.exit(main())
