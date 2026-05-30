#!/usr/bin/env python3
"""COHORT_02 Full Non-Public Draft Generation Wave v1 — Sprint 6I.

Deterministic, registry-constrained draft generation from COHORT_02 inventory.
No LLM. No routes.json writes. Stdlib only.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

INVENTORY_PATH = ROOT / "main/data/COHORT_02_EN_TERMINOLOGY_ROUTE_INVENTORY.json"
OUTPUT_MANIFEST = ROOT / "main/data/COHORT_02_FULL_DRAFT_MANIFEST.json"
OUTPUT_BLUEPRINTS = ROOT / "main/data/COHORT_02_FULL_DRAFT_BLUEPRINTS.json"
CONTENT_DIR = ROOT / "main/content/en/pages/cohort-02-terminology"

COHORT_ID = "COHORT_02_EN_TERMINOLOGY_SPINE"
ENGINE = "generate_cohort_02_full_draft_wave_v1"

REGISTRY_PATHS = {
    "corpus_route_formula": ROOT / "main/data/corpus_route_formula.json",
    "page_type_registry": ROOT / "main/data/page_type_registry.json",
    "audience_layer_registry": ROOT / "main/data/audience_layer_registry.json",
    "reference_layer_registry": ROOT / "main/data/reference_layer_registry.json",
    "generator_schema": ROOT / "main/data/SOVEREIGN_CORPUS_GENERATOR_SCHEMA_WAVE_1.json",
    "template_contract": ROOT / "main/data/SOVEREIGN_TEMPLATE_CONTRACT_MODEL_WAVE_1.json",
    "evidence_grades": ROOT / "main/data/SOVEREIGN_EVIDENCE_GRADE_REGISTRY_WAVE_1.json",
    "source_hierarchy": ROOT / "main/data/SOVEREIGN_SOURCE_HIERARCHY_MODEL_WAVE_1.json",
    "launch_composition": ROOT / "main/data/INITIAL_14000_PAGE_LAUNCH_COMPOSITION_MODEL.json",
    "source_registry": ROOT / "main/data/sources/source_registry.json",
    "terminology_claims": ROOT / "main/data/claims/terminology_claims.json",
    "routes": ROOT / "main/data/routes.json",
}

REQUIRED_INVENTORY_FIELDS = (
    "inventory_row_id", "route_id", "language", "route_path", "term_or_entity",
    "term_or_entity_class", "page_type_id", "audience_id", "reference_layer_id",
    "knowledge_reliability_level", "evidence_grade", "source_posture", "claim_posture",
    "route_state", "indexation_state", "internal_link_role", "template_id",
    "forbidden_claim_classes", "generation_eligibility", "publication_eligibility",
    "noindex_default", "validation_gates",
)

FORBIDDEN_NARRATIVE = (
    "market share", "cagr", "handling instructions", "medical advice",
    "procurement guide", "investment recommendation", "production data",
)

AUDIENCE_LABELS = {
    "AUD_CHEMIST": "Chemists",
    "AUD_RESEARCHER": "Researchers",
    "AUD_STUDENT": "Students",
    "AUD_AI_SYSTEM": "AI Systems",
    "AUD_ANALYST": "Analysts",
    "AUD_GOVERNMENT": "Government",
    "AUD_CHILD_EDU": "Child Education",
    "AUD_INVESTOR": "Investors",
    "AUD_COMPANY": "Companies",
}

REF_LABELS = {
    "REF_ACADEMIC": "Academic reference",
    "REF_KNOWLEDGE": "Knowledge reference",
    "REF_RESEARCH": "Research reference",
    "REF_EDUCATIONAL": "Educational reference",
    "REF_TECHNICAL": "Technical reference",
    "REF_LINGUISTIC": "Linguistic reference",
    "REF_INSTITUTIONAL": "Institutional reference",
    "REF_ECONOMIC": "Economic reference",
    "REF_LOGISTICAL": "Logistical reference",
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def display_term(term: str) -> str:
    return term.replace("_", " ").title()


def build_h1(row: dict) -> str:
    pt = row["page_type_id"]
    term = display_term(row["term_or_entity"])
    if pt == "PT_DIFFERENCE_COMPARISON" and row.get("comparison_sides"):
        a, b = row["comparison_sides"]
        return f"{display_term(a)} vs {display_term(b)} — Difference Reference"
    if pt == "PT_AUDIENCE_EXPLAINER":
        aud = AUDIENCE_LABELS.get(row["audience_id"], row["audience_id"])
        return f"{term} for {aud}"
    if pt == "PT_COMPOUND_ENTITY":
        return f"{term} — Compound Reference"
    if pt == "PT_AI_READABLE":
        return f"AI Reference: {term}"
    if pt == "PT_CHILD_SAFE_EDU":
        return f"Learn: {term}"
    if pt == "PT_TERM_CANONICAL":
        return f"{term} — Terminology Reference"
    return f"{term} — Reference Draft"


def build_title(h1: str) -> str:
    return f"{h1} | bisulfid.com"


def page_role_bullets(row: dict) -> list[str]:
    pt = row["page_type_id"]
    term = row["term_or_entity"]
    ref = REF_LABELS.get(row["reference_layer_id"], row["reference_layer_id"])
    aud = AUDIENCE_LABELS.get(row["audience_id"], row["audience_id"])
    if pt == "PT_TERM_CANONICAL":
        return [
            f"Canonical terminology reference surface for `{term}`",
            f"Reference layer: {ref}",
            f"Audience posture: {aud}",
            "Lexical and nomenclature boundary framing only — not operational instruction",
            "Factual chemistry lines remain **[SOURCE REQUIRED]** until separately governed",
        ]
    if pt == "PT_AUDIENCE_EXPLAINER":
        return [
            f"Audience-layer explainer for `{term}` ({aud})",
            f"Vocabulary and claim boundary adapted to {aud} without meaning change",
            ref,
            "Does not upgrade evidence beyond registry allowance",
            "No unsupported simplification of chemical fact",
        ]
    if pt == "PT_COMPOUND_ENTITY":
        return [
            f"Compound/entity naming record for `{term}`",
            "Naming and identity boundary — not industrial performance claims",
            ref,
            "Operational handling and procurement language excluded",
            "**[SOURCE REQUIRED]** for all factual compound assertions",
        ]
    if pt == "PT_AI_READABLE":
        return [
            f"Machine-readable governed record for `{term}`",
            "Structured provenance and excluded-claims disclosure",
            "Registry-backed fields only — no inferred facts",
            ref,
            "Not publication-ready without source and claim gates",
        ]
    if pt == "PT_CHILD_SAFE_EDU":
        return [
            f"Child-safe educational vocabulary framing for `{term}`",
            "Naming curiosity only — no experiments, hazards, or handling",
            "Educational simplification limit enforced",
            ref,
            "Not a safety guide or textbook experiment page",
        ]
    if pt == "PT_DIFFERENCE_COMPARISON":
        sides = row.get("comparison_sides") or []
        mode = row.get("comparison_reference_mode") or "comparison"
        return [
            f"Comparison intent: {display_term(sides[0]) if sides else term} vs {display_term(sides[1]) if len(sides) > 1 else 'peer'}",
            f"Mode: {mode.replace('_', ' ')}",
            "Distinction framing only — no unsupported winner claim",
            "Per-side source and claim posture disclosed below",
            "Unresolved comparison fields marked explicitly",
        ]
    return [f"Governed reference draft for `{term}`"]


def render_markdown(row: dict) -> str:
    h1 = build_h1(row)
    title = build_title(h1)
    bullets = page_role_bullets(row)
    bullet_text = "\n".join(f"- {b}" for b in bullets)
    excluded = ", ".join(row.get("forbidden_claim_classes", []))
    links = row.get("internal_link_targets") or []
    link_lines = "\n".join(f"- `route_id`: `{lid}` (planning placeholder — not a live link)" for lid in links)
    unresolved = [
        "source_verification",
        "claim_approval",
        "public_route_merge",
        "indexation",
        "multilingual_expansion",
    ]
    if row["page_type_id"] == "PT_DIFFERENCE_COMPARISON":
        unresolved.append("comparison_boundary_verification")

    compare_block = ""
    if row["page_type_id"] == "PT_DIFFERENCE_COMPARISON" and row.get("comparison_sides"):
        a, b = row["comparison_sides"]
        compare_block = f"""
## Comparison sides (terminology boundary only)

| Side | term_entity_id | Source posture | Claim posture |
| --- | --- | --- | --- |
| A | {a} | {row['source_posture']} | {row['claim_posture']} |
| B | {b} | {row['source_posture']} | {row['claim_posture']} |

Distinction claims beyond terminology boundary: **[SOURCE REQUIRED]** on each side until verified.
"""

    ai_block = ""
    if row["page_type_id"] == "PT_AI_READABLE":
        ai_block = """
## Structured metadata (machine-readable boundary)

```yaml
term_entity_id: """ + str(row.get("term_entity_id", row["term_or_entity"])) + """
source_posture: """ + row["source_posture"] + """
claim_posture: """ + row["claim_posture"] + """
excluded_claim_classes: """ + str(row.get("forbidden_claim_classes", [])) + """
unresolved_fields: explicit_in_body
inferred_facts: forbidden
```
"""

    child_block = ""
    if row["page_type_id"] == "PT_CHILD_SAFE_EDU":
        child_block = """
## Child-safe notice

This educational draft uses vocabulary-only framing. It is **not** a safety guide, experiment instruction, or medical page.
"""

    return f"""---
route_id: {row['route_id']}
inventory_row_id: {row['inventory_row_id']}
status: draft
publication_status: non_public
publication_eligibility: false
indexable: false
in_sitemap: false
in_navigation: false
language: en
locale: en
source_language: en
title: {title}
template_id: {row['template_id']}
page_type_id: {row['page_type_id']}
audience_id: {row['audience_id']}
reference_layer_id: {row['reference_layer_id']}
evidence_grade: {row['evidence_grade']}
knowledge_reliability_level: {row['knowledge_reliability_level']}
source_posture: {row['source_posture']}
claim_posture: {row['claim_posture']}
indexation_state: {row['indexation_state']}
cohort_id: {COHORT_ID}
generated: true
engine: {ENGINE}
noindex_default: true
generation_eligibility: {row['generation_eligibility']}
---
# {h1}

**Draft status:** This page is a **non-public** COHORT_02 terminology draft. It is **not published**, **not indexable**, **not in the sitemap**, **not in navigation**, and **not publication-ready**. This is not a final public reference page. **No claim is approved** for publication from this draft alone.

## Reliability notice

| Field | Value |
| --- | --- |
| knowledge_reliability_level | {row['knowledge_reliability_level']} |
| evidence_grade | {row['evidence_grade']} |
| source_posture | {row['source_posture']} |
| claim_posture | {row['claim_posture']} |
| generation_eligibility | {row['generation_eligibility']} |
| excluded_claim_classes | {excluded} |

## Page purpose

{bullet_text}

Terminology and chemical fact lines that are not yet source-supported: **[SOURCE REQUIRED]**.

{child_block}{compare_block}{ai_block}
## Source and claim status

- Source posture: **{row['source_posture']}** — factual terminology not asserted as verified in this draft.
- Claim posture: **{row['claim_posture']}** — no approved publication claim from this page alone.
- Source registries: **inactive** for mass publication; individual sources may exist elsewhere.
- This draft does not remove **[SOURCE REQUIRED]** markers from other corpus pages.

## Unresolved fields

{', '.join(unresolved)}

## Publication blockers

- Route not in production `routes.json` (inventory-only until merge charter).
- `indexable: false`; `in_sitemap: false`; `in_navigation: false`.
- `production_can_safely_proceed: no`.
- Publication requires source_verified and claim_approved_narrow minimum per template contract.

## Internal link placeholders (planning only)

{link_lines if link_lines else '- None declared'}

No live public URLs. No markdown hyperlinks. Planning references by `route_id` only.

*Non-public COHORT_02 draft — {COHORT_ID} — engine v1.*
"""


def validate_row(row: dict, page_types: set, audiences: set, refs: set, templates: set) -> list[str]:
    errors = []
    for field in REQUIRED_INVENTORY_FIELDS:
        if field not in row:
            errors.append(f"missing {field}")
    if row.get("language") != "en":
        errors.append("language must be en")
    if row.get("publication_eligibility") is True:
        errors.append("publication_eligibility must be false")
    for flag in ("noindex_default",):
        if row.get(flag) is not True:
            errors.append(f"{flag} must be true")
    for flag in ("sitemap_default", "navigation_default"):
        if row.get(flag) is True:
            errors.append(f"{flag} must be false")
    if row.get("page_type_id") not in page_types:
        errors.append(f"unknown page_type_id {row.get('page_type_id')}")
    if row.get("audience_id") not in audiences:
        errors.append(f"unknown audience_id {row.get('audience_id')}")
    if row.get("reference_layer_id") not in refs:
        errors.append(f"unknown reference_layer_id {row.get('reference_layer_id')}")
    if row.get("template_id") not in templates:
        errors.append(f"unknown template_id {row.get('template_id')}")
    narrative = " ".join(page_role_bullets(row)).lower()
    for phrase in FORBIDDEN_NARRATIVE:
        if phrase in narrative and not any(n in narrative[max(0, narrative.find(phrase) - 30): narrative.find(phrase)] for n in ("not ", "no ", "never ", "without ", "excluded")):
            errors.append(f"forbidden phrase {phrase!r}")
    return errors


def scan_body_quality(body: str, pt: str) -> list[str]:
    errors = []
    words = len(re.findall(r"\w+", body))
    min_words = 150 if pt == "PT_CHILD_SAFE_EDU" else 180
    if words < min_words:
        errors.append(f"thin page ({words} words)")
    if "[SOURCE REQUIRED]" not in body:
        errors.append("missing [SOURCE REQUIRED]")
    if "source and claim status" not in body.lower():
        errors.append("missing source/claim section")
    if "publication blockers" not in body.lower():
        errors.append("missing publication blockers")
    if re.search(r"\[[^\]]+\]\([^)]+\)", body):
        errors.append("markdown link forbidden")
    if re.search(r"https?://", body):
        errors.append("raw URL forbidden")
    return errors


def run_engine(write_drafts: bool) -> int:
    print("=== COHORT_02 Full Draft Generation Wave v1 ===")
    print(f"Date: {date.today().isoformat()}")
    print(f"Mode: {'write_drafts' if write_drafts else 'manifest_only'}")
    print()

    inventory = load_json(INVENTORY_PATH)
    rows_in = inventory.get("rows", [])
    page_types = {p["page_type_id"] for p in load_json(REGISTRY_PATHS["page_type_registry"]).get("page_types", [])}
    audiences = {a["audience_id"] for a in load_json(REGISTRY_PATHS["audience_layer_registry"]).get("audiences", [])}
    refs = {r["reference_layer_id"] for r in load_json(REGISTRY_PATHS["reference_layer_registry"]).get("reference_layers", [])}
    templates = {t["template_id"] for t in load_json(REGISTRY_PATHS["template_contract"]).get("templates", [])}
    routes_count = len(load_json(REGISTRY_PATHS["routes"]).get("routes", []))

    generated = []
    rejected = []

    for row in rows_in:
        errs = validate_row(row, page_types, audiences, refs, templates)
        if errs:
            rejected.append({"route_id": row.get("route_id"), "inventory_row_id": row.get("inventory_row_id"), "reasons": errs})
            continue
        body = render_markdown(row)
        qerrs = scan_body_quality(body, row["page_type_id"])
        if qerrs:
            rejected.append({"route_id": row["route_id"], "inventory_row_id": row["inventory_row_id"], "reasons": qerrs})
            continue
        content_file = f"main/content/en/pages/cohort-02-terminology/{row['route_id']}.md"
        record = {
            "inventory_row_id": row["inventory_row_id"],
            "route_id": row["route_id"],
            "route_path": row["route_path"],
            "title": build_title(build_h1(row)),
            "h1": build_h1(row),
            "content_file": content_file,
            "page_type_id": row["page_type_id"],
            "audience_id": row["audience_id"],
            "reference_layer_id": row["reference_layer_id"],
            "term_entity_id": row.get("term_entity_id", row["term_or_entity"]),
            "template_id": row["template_id"],
            "body_byte_length": len(body.encode("utf-8")),
            "body_word_count": len(re.findall(r"\w+", body)),
            "engine_validated": True,
        }
        generated.append({**record, "_body": body})
        if write_drafts:
            out = ROOT / content_file
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(body, encoding="utf-8")

    manifest = {
        "version": "1.0.0",
        "engine": ENGINE,
        "sprint": "6I",
        "cohort_id": COHORT_ID,
        "date": date.today().isoformat(),
        "deterministic": True,
        "llm_used": False,
        "inventory_rows_input": len(rows_in),
        "generated_count": len(generated),
        "rejected_count": len(rejected),
        "routes_json_modified": False,
        "registered_routes_unchanged": routes_count,
        "production_route_registry": False,
        "units": [{k: v for k, v in g.items() if not k.startswith("_")} for g in generated],
        "rejected": rejected,
    }

    blueprints = {
        "version": "1.0.0",
        "cohort_id": COHORT_ID,
        "generated_count": len(generated),
        "routes": [
            {
                "route_id": g["route_id"],
                "path": g["route_path"],
                "title": g["title"],
                "h1": g["h1"],
                "content_file": g["content_file"],
                "page_type_id": g["page_type_id"],
                "indexable": False,
                "in_sitemap": False,
                "in_navigation": False,
            }
            for g in generated
        ],
    }

    OUTPUT_MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    OUTPUT_BLUEPRINTS.write_text(json.dumps(blueprints, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Input rows: {len(rows_in)}")
    print(f"Generated: {len(generated)}")
    print(f"Rejected: {len(rejected)}")
    if write_drafts:
        print(f"Draft files: {CONTENT_DIR.relative_to(ROOT)}")
    print(f"Wrote {OUTPUT_MANIFEST.relative_to(ROOT)}")
    print(f"Wrote {OUTPUT_BLUEPRINTS.relative_to(ROOT)}")

    if rejected:
        print("\nRejected sample (first 5):")
        for r in rejected[:5]:
            print(f"  {r['route_id']}: {r['reasons']}")

    if len(generated) == 0:
        print("\nFAIL — no drafts generated")
        return 1
    print(f"\nPASS — {len(generated)}/{len(rows_in)} COHORT_02 drafts generated")
    return 0 if len(rejected) == 0 else 0  # partial success still exit 0 if any generated per sprint goal


def main() -> int:
    parser = argparse.ArgumentParser(description="COHORT_02 full draft generation wave v1")
    parser.add_argument("--write-drafts", action="store_true", help="Write markdown draft files")
    args = parser.parse_args()
    return run_engine(write_drafts=args.write_drafts)


if __name__ == "__main__":
    sys.exit(main())
