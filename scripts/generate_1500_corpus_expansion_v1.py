#!/usr/bin/env python3
"""Sprint 6M-E — governed corpus expansion toward 1,500 renderable non-public pages.

Deterministic, stdlib-only. Adds planned routes + draft content only.
Does not modify source/claim registries, sitemap, or navigation policy.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROUTES_PATH = ROOT / "main/data/routes.json"
INTERNAL_LINKS_PATH = ROOT / "main/data/internal_links.json"
INVENTORY_OUT = ROOT / "main/data/COHORT_03_1500_EXPANSION_INVENTORY.json"
MANIFEST_OUT = ROOT / "main/data/COHORT_03_1500_EXPANSION_MANIFEST.json"

COHORT_ID = "COHORT_03_1500_PIPELINE_EXPANSION"
ENGINE = "generate_1500_corpus_expansion_v1"
TARGET_NEW_ROUTES = 457

FORBIDDEN_CLAIM_CLASSES = [
    "safety", "medical", "market", "procurement", "production", "pricing",
    "trade", "CAGR", "acquisition", "operational_handling_guidance",
]

AUDIENCE_LABELS = {
    "AUD_CHEMIST": "Chemists",
    "AUD_RESEARCHER": "Researchers",
    "AUD_STUDENT": "Students",
    "AUD_AI_SYSTEM": "AI Systems",
    "AUD_ANALYST": "Analysts",
    "AUD_GOVERNMENT": "Government",
    "AUD_CHILD_EDU": "Child Education",
}

REF_LABELS = {
    "REF_ACADEMIC": "Academic reference",
    "REF_KNOWLEDGE": "Knowledge reference",
    "REF_RESEARCH": "Research reference",
    "REF_EDUCATIONAL": "Educational reference",
    "REF_TECHNICAL": "Technical reference",
    "REF_LINGUISTIC": "Linguistic reference",
    "REF_INSTITUTIONAL": "Institutional reference",
}

# Eight deterministic variants per EN terminology entity (51 × 8 = 408 routes)
ENTITY_VARIANTS = (
    ("term", "chem", "know", "PT_TERM_CANONICAL", "AUD_CHEMIST", "REF_KNOWLEDGE", "reference_page.html"),
    ("term", "chem", "acad", "PT_TERM_CANONICAL", "AUD_CHEMIST", "REF_ACADEMIC", "reference_page.html"),
    ("term", "res", "res", "PT_TERM_CANONICAL", "AUD_RESEARCHER", "REF_RESEARCH", "reference_page.html"),
    ("aud", "stu", "edu", "PT_AUDIENCE_EXPLAINER", "AUD_STUDENT", "REF_EDUCATIONAL", "reference_page.html"),
    ("aud", "ai", "tech", "PT_AI_READABLE", "AUD_AI_SYSTEM", "REF_TECHNICAL", "reference_page.html"),
    ("cmp", "chem", "acad", "PT_COMPOUND_ENTITY", "AUD_CHEMIST", "REF_ACADEMIC", "reference_page.html"),
    ("air", "res", "res", "PT_AUDIENCE_EXPLAINER", "AUD_RESEARCHER", "REF_RESEARCH", "reference_page.html"),
    ("child", "stu", "edu", "PT_CHILD_SAFE_EDU", "AUD_CHILD_EDU", "REF_EDUCATIONAL", "reference_page.html"),
)

# 51 EN entities — wave-2 terminology not present in COHORT_02 inventory
EN_ENTITIES = (
    "alkyl_sulfides", "aryl_sulfides", "barium_sulfides", "boron_sulfides",
    "cobalt_sulfides", "fuming_sulfuric", "gold_sulfides", "iron_sulfides_extended",
    "lead_sulfides", "lithium_sulfides", "manganese_sulfides", "molybdenum_sulfides",
    "nickel_sulfides", "phosphorus_sulfides", "potassium_sulfides", "selenium_sulfides",
    "silver_sulfides", "strontium_sulfides", "sulfate_esters", "sulfate_salts",
    "sulfenyl", "sulfilimines", "sulfinyl", "sulfonate_esters", "sulfonyl",
    "sulfoximines", "sulfur_carbon_bonds", "sulfur_halogens",
    "sulfur_nitrogen_compounds", "sulfur_oxygen_halides",
    "sulfuric_acid", "tellurium_sulfides", "thioethers", "thiosulfate_salts",
    "tin_sulfides_extended", "tungsten_sulfides", "zinc_sulfides",
    "iron_sulfides_mineral_language", "mercaptan_class_language", "sulfane_chain_language",
    "sulfonic_acid_class_language", "sulfoxide_sulfone_language", "thiosulfate_terminology",
    "tungsten_disulfide_terms", "zinc_lead_sulfides_language", "ammonium_sulfides",
    "antimony_sulfides", "arsenic_sulfides",     "mercury_sulfides", "chromium_sulfides", "vanadium_sulfides",
)

# 49 single-page routes: DE terminology, disambiguation, governance/index
SINGLE_ROUTES = (
    # DE wave-2 / pipeline terminology (11)
    ("de", "de_dis_sulfid_sulfat", "/de/reference/sulfid-sulfat-boundary/", "Sulfid vs Sulfat boundary", "disambiguation", "reference_page.html"),
    ("de", "de_gov_claim_boundary", "/de/reference/claim-boundary/", "DE claim boundary explainer", "reference_governance", "reference_page.html"),
    ("de", "de_gov_source_locking", "/de/reference/source-locking/", "DE source-locking primer", "reference_governance", "reference_page.html"),
    ("de", "de_index_disambiguation_map", "/de/reference/disambiguation-map/", "DE disambiguation index", "gateway", "reference_page.html"),
    ("de", "de_index_terminology_map", "/de/reference/terminology-map/", "DE terminology cluster map", "gateway", "reference_page.html"),
    ("de", "de_method_editorial_standards", "/de/reference/editorial-standards/", "DE editorial standards", "reference_governance", "reference_page.html"),
    ("de", "de_term_ammonium_sulfide", "/de/terminology/ammonium-sulfide/", "Ammonium sulfide DE", "de_terminology", "term_page.html"),
    ("de", "de_term_antimony_sulfide", "/de/terminology/antimony-sulfide/", "Antimony sulfide DE", "de_terminology", "term_page.html"),
    ("de", "de_term_arsenic_sulfide", "/de/terminology/arsenic-sulfide/", "Arsenic sulfide DE", "de_terminology", "term_page.html"),
    ("de", "de_term_mercury_sulfide", "/de/terminology/mercury-sulfide/", "Mercury sulfide DE", "de_terminology", "term_page.html"),
    ("de", "de_term_polysulfide_salts", "/de/terminology/polysulfide-salts/", "Polysulfide salts DE", "de_terminology", "term_page.html"),
    # Additional DE terminology expansion (18)
    ("de", "de_term_barium_sulfide", "/de/terminology/barium-sulfide/", "Barium sulfide DE", "de_terminology", "term_page.html"),
    ("de", "de_term_boron_sulfide", "/de/terminology/boron-sulfide/", "Boron sulfide DE", "de_terminology", "term_page.html"),
    ("de", "de_term_cobalt_sulfide", "/de/terminology/cobalt-sulfide/", "Cobalt sulfide DE", "de_terminology", "term_page.html"),
    ("de", "de_term_gold_sulfide", "/de/terminology/gold-sulfide/", "Gold sulfide DE", "de_terminology", "term_page.html"),
    ("de", "de_term_lead_sulfide", "/de/terminology/lead-sulfide/", "Lead sulfide DE", "de_terminology", "term_page.html"),
    ("de", "de_term_lithium_sulfide", "/de/terminology/lithium-sulfide/", "Lithium sulfide DE", "de_terminology", "term_page.html"),
    ("de", "de_term_nickel_sulfide", "/de/terminology/nickel-sulfide/", "Nickel sulfide DE", "de_terminology", "term_page.html"),
    ("de", "de_term_phosphorus_sulfide", "/de/terminology/phosphorus-sulfide/", "Phosphorus sulfide DE", "de_terminology", "term_page.html"),
    ("de", "de_term_selenium_sulfide", "/de/terminology/selenium-sulfide/", "Selenium sulfide DE", "de_terminology", "term_page.html"),
    ("de", "de_term_silver_sulfide", "/de/terminology/silver-sulfide/", "Silver sulfide DE", "de_terminology", "term_page.html"),
    ("de", "de_term_strontium_sulfide", "/de/terminology/strontium-sulfide/", "Strontium sulfide DE", "de_terminology", "term_page.html"),
    ("de", "de_term_tellurium_sulfide", "/de/terminology/tellurium-sulfide/", "Tellurium sulfide DE", "de_terminology", "term_page.html"),
    ("de", "de_term_thioether", "/de/terminology/thioether/", "Thioether DE", "de_terminology", "term_page.html"),
    ("de", "de_term_sulfenyl", "/de/terminology/sulfenyl/", "Sulfenyl DE", "de_terminology", "term_page.html"),
    ("de", "de_term_sulfinyl", "/de/terminology/sulfinyl/", "Sulfinyl DE", "de_terminology", "term_page.html"),
    ("de", "de_term_chromium_sulfide", "/de/terminology/chromium-sulfide/", "Chromium sulfide DE", "de_terminology", "term_page.html"),
    ("de", "de_term_sulfur_dioxide", "/de/terminology/sulfur-dioxide/", "Sulfur dioxide DE", "de_terminology", "term_page.html"),
    ("de", "de_term_sulfur_trioxide", "/de/terminology/sulfur-trioxide/", "Sulfur trioxide DE", "de_terminology", "term_page.html"),
    # EN governance / index / disambiguation (20)
    ("en", "en_nav_internal_reference", "/reference/internal-navigation/", "Internal reference navigation guide", "reference_governance", "reference_page.html"),
    ("en", "en_term_sulfide_minerals_index", "/terminology/sulfide-minerals-index/", "Sulfide minerals index", "gateway", "reference_page.html"),
    ("en", "multilingual_corpus_map", "/reference/multilingual-corpus-map/", "Multilingual corpus map", "gateway", "reference_page.html"),
    ("en", "ontology_alignment_primer", "/reference/ontology-alignment-primer/", "Ontology alignment primer", "reference_governance", "reference_page.html"),
    ("en", "en_term_polysulfide_salts", "/terminology/polysulfide-salts/", "Polysulfide salts EN", "en_terminology", "term_page.html"),
    ("en", "en_term_sulfite_salts", "/terminology/sulfite-salts/", "Sulfite salts EN", "en_terminology", "term_page.html"),
    ("en", "polysulfide_terminology", "/terminology/polysulfide/", "Polysulfide terminology", "en_terminology", "term_page.html"),
    ("en", "sodium_sulfide_salts_language", "/terminology/sodium-sulfide-salts/", "Sodium sulfide salts language", "en_terminology", "term_page.html"),
    ("en", "silver_gold_sulfides_terms", "/terminology/precious-metal-sulfides/", "Precious metal sulfides", "en_terminology", "term_page.html"),
    ("en", "tin_sulfides_terms", "/terminology/tin-sulfides/", "Tin sulfides terminology", "en_terminology", "term_page.html"),
    ("en", "en_dis_alkyl_aryl_sulfide", "/reference/alkyl-aryl-sulfide-boundary/", "Alkyl vs aryl sulfide boundary", "disambiguation", "reference_page.html"),
    ("en", "en_dis_sulfate_sulfonate", "/reference/sulfate-sulfonate-boundary/", "Sulfate vs sulfonate boundary", "disambiguation", "reference_page.html"),
    ("en", "en_dis_sulfide_sulfite_salt", "/reference/sulfide-sulfite-salt-boundary/", "Sulfide vs sulfite salt boundary", "disambiguation", "reference_page.html"),
    ("en", "en_gov_rc_pipeline_status", "/reference/rc-pipeline-status/", "RC pipeline status explainer", "reference_governance", "reference_page.html"),
    ("en", "en_gov_batch_render_discipline", "/reference/batch-render-discipline/", "Batch render discipline", "reference_governance", "reference_page.html"),
    ("en", "en_index_cohort03_spine", "/reference/cohort-03-spine/", "Cohort 03 terminology spine index", "gateway", "reference_page.html"),
    ("en", "en_foundation_1500_rc_posture", "/foundation/1500-rc-posture/", "1,500-page RC posture foundation", "reference_governance", "reference_page.html"),
    ("en", "en_foundation_7500_pipeline", "/foundation/7500-pipeline-bridge/", "7,500-page pipeline bridge", "reference_governance", "reference_page.html"),
    ("en", "en_foundation_14000_corpus_lock", "/foundation/14000-corpus-lock/", "14,000-page corpus lock foundation", "reference_governance", "reference_page.html"),
    ("en", "en_multilingual_de_expansion_hub", "/reference/de-expansion-hub/", "German expansion hub index", "gateway", "reference_page.html"),
)


def display_term(term: str) -> str:
    return term.replace("_", " ").title()


def path_slug(term: str) -> str:
    return term.replace("_", "-")


def build_h1(row: dict) -> str:
    pt = row["page_type_id"]
    term = display_term(row["term_or_entity"])
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
    return row.get("h1_override") or f"{term} — Reference Draft"


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
    return [
        f"Governed non-public reference draft for `{term}`",
        "Corpus expansion for 14,000-page launch pipeline — not a reduced launch",
        ref if row.get("reference_layer_id") else "Governance/reference layer",
        "**[SOURCE REQUIRED]** for unresolved factual lines",
        "No source approval or claim approval implied",
    ]


def render_en_markdown(row: dict) -> str:
    h1 = build_h1(row)
    title = f"{h1} | bisulfid.com"
    bullets = page_role_bullets(row)
    bullet_text = "\n".join(f"- {b}" for b in bullets)
    excluded = ", ".join(FORBIDDEN_CLAIM_CLASSES)
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
page_type_id: {row['page_type_id']}
audience_id: {row.get('audience_id', 'ALL')}
reference_layer_id: {row.get('reference_layer_id', 'REF_KNOWLEDGE')}
source_posture: source_required_unresolved
claim_posture: claim_pending_review
cohort_id: {COHORT_ID}
generated: true
engine: {ENGINE}
noindex_default: true
---
# {h1}

**Draft status:** This page is a **non-public** COHORT_03 pipeline expansion draft. It is **not published**, **not indexable**, **not in the sitemap**, **not in navigation**, and **not publication-ready**. This is not a public launch page. **No claim is approved** for publication from this draft alone.

## Reliability notice

| Field | Value |
| --- | --- |
| knowledge_reliability_level | L2_draft_cautious |
| evidence_grade | terminology_dictionary |
| source_posture | source_required_unresolved |
| claim_posture | claim_pending_review |
| excluded_claim_classes | {excluded} |

## Page purpose

{bullet_text}

Terminology and chemical fact lines that are not yet source-supported: **[SOURCE REQUIRED]**.

## Source and claim status

- Source posture: **source_required_unresolved** — factual terminology not asserted as verified in this draft.
- Claim posture: **claim_pending_review** — no approved publication claim from this page alone.
- Source registries: **inactive** for mass publication; individual sources may exist elsewhere.
- This draft does not remove **[SOURCE REQUIRED]** markers from other corpus pages.

## Publication blockers

- Route remains `planned`; `indexable: false`; `in_sitemap: false`; `in_navigation: false`.
- `production_can_safely_proceed: no`.
- **14,000-page minimum launch corpus** objective unchanged — this page is pipeline expansion only.

## Internal link placeholders (planning only)

- `route_id`: `en_foundation_sovereign_intro` (planning placeholder — not a live link)
- `route_id`: `en_index_terminology_spine` (planning placeholder — not a live link)

*Non-public COHORT_03 draft — {COHORT_ID} — engine v1.*
"""


def render_de_markdown(row: dict) -> str:
    h1 = row.get("h1_override") or build_h1(row)
    rid = row["route_id"]
    return f"""---
route_id: {rid}
status: draft
publication_status: non_public
indexable: false
in_sitemap: false
language: de
locale: de
source_language: de
cohort_id: {COHORT_ID}
generated: true
engine: {ENGINE}
---
# {h1}

**Entwurfsstatus:** Diese Seite ist ein **nichtöffentlicher Entwurf** für die **14.000-Seiten-Pipeline**. Sie ist **nicht veröffentlicht**, **nicht indexierbar**, **nicht in der Sitemap**, **nicht in der Navigation** und **nicht veröffentlichungsreif**. Dies ist **kein öffentlicher Launch**. **Kein Claim ist freigegeben**. **Keine Quellenfreigabe** wird impliziert.

## Seitenrolle

Kontrollierter **Terminologie-/Referenz-Eintrag** (`route_id`: `{rid}`) — keine Lehrbuch-, Blog-, Pilot- oder Glossar-Ersatzseite. Die Seite dient der **governed corpus expansion** innerhalb des festen **14.000-Seiten-Mindestziels**, nicht einem reduzierten Publikationsumfang.

## Terminologie-Schichten (Entwurfsprüfung)

- **Lexikalische Form** — Oberflächenschreibung, IUPAC-/Dokumentsprache und DE/EN-Grenzfragen under review **[SOURCE REQUIRED]**.
- **Chemische / Dokumentform** — beabsichtigter Geltungsbereich und Abgrenzung zu Nachbarbegriffen **[SOURCE REQUIRED]**.
- **Claim-Status** — **keine freigegebenen Claims**; Claim-Registries bleiben **inaktiv** für Massenpublikation.
- **Referenzschicht** — nomenklatur- und grenzorientiert; keine Betriebs-, Beschaffungs-, Markt- oder Sicherheitsanleitung.

## Abgrenzungen

Keine universellen Suffix-Regeln, keine Normansprüche, keine Betriebsanleitung, keine medizinischen oder Beschaffungsempfehlungen, keine Markt-/Handels-/CAGR-Inhalte. Stärkere Quellenbindung erforderlich **[SOURCE REQUIRED]**.

## Quellen- und Claim-Status

- Claim-Registries: **inaktiv**.
- Freigegebene Claims: **keine**.
- Source-locking: **nicht abgeschlossen**; `[SOURCE REQUIRED]` markiert offene Faktenzeilen.
- Dieser Entwurf entfernt **keine** `[SOURCE REQUIRED]`-Markierungen anderswo im Korpus.

## Veröffentlichungsblocker

- Route bleibt `planned`.
- Entwurf: `non_public`, nicht indexierbar, nicht in Sitemap/Navigation.
- `production_can_safely_proceed: no`.
- **14.000-Seiten-Mindestziel** unverändert — Pipeline-Expansion only.

## Interne Referenzrolle

Spätere Verlinkung per `route_id` `{rid}` — hier nur Planungsreferenz, keine Markdown-Links, keine Live-URLs.

*Nicht veröffentlichungsreifer Pipeline-Entwurf — {COHORT_ID} — `{rid}`.*
"""


def render_missing_en_markdown(route: dict) -> str:
    rid = route["route_id"]
    h1 = route.get("h1", display_term(rid))
    title = route.get("title", f"{h1} — bisulfid.com")
    return f"""---
route_id: {rid}
status: draft
publication_status: non_public
indexable: false
in_sitemap: false
language: en
locale: en
source_language: en
generated: true
engine: {ENGINE}
missing_draft_backfill: true
---
# {h1}

**Draft notice:** This page is a **non-public draft** for the **14,000-page launch corpus pipeline**. It is **not published**, **not indexable**, **not in the sitemap**, **not in navigation**, and **not publication-ready**. **Source approval not implied**. **No claim is approved**.

## Purpose

Controlled reference draft for `{rid}` — governed vocabulary and boundary framing only. Not a safety guide, procurement page, market analysis, or operational manual.

## Source boundary

Factual statements require registry-backed support before any public tier **[SOURCE REQUIRED]**. This draft does **not** claim source-locking is complete.

## Claim boundary

Required claim groups remain **inactive** for publication. **No science or industry claim is approved** from this draft alone.

## Publication blockers

- Route status: `planned`
- `indexable: false`; `in_sitemap: false`; `in_navigation: false`
- `production_can_safely_proceed: no`

*Missing-draft backfill — Sprint 6M-E — {rid}.*
"""


def build_cohort03_rows(existing_ids: set[str]) -> list[dict]:
    rows: list[dict] = []
    seq = 1

    for entity in EN_ENTITIES:
        for vkey, aud_key, ref_key, pt, aud, ref, template in ENTITY_VARIANTS:
            rid = f"cohort03_en_{entity}_{vkey}_{aud_key}_{ref_key}"
            if rid in existing_ids:
                continue
            path = f"/en/terminology/{path_slug(entity)}/{vkey}/{aud_key}/{ref_key}/"
            rows.append({
                "inventory_row_id": f"INV-C03-{seq:05d}",
                "route_id": rid,
                "language": "en",
                "route_path": path,
                "term_or_entity": entity,
                "page_type_id": pt,
                "audience_id": aud,
                "reference_layer_id": ref,
                "template": template,
                "content_subdir": "cohort-03-expansion",
            })
            seq += 1

    for lang, rid, path, h1, page_family, template in SINGLE_ROUTES:
        if rid in existing_ids:
            continue
        rows.append({
            "inventory_row_id": f"INV-C03-{seq:05d}",
            "route_id": rid,
            "language": lang,
            "route_path": path,
            "term_or_entity": rid,
            "h1_override": h1,
            "page_type_id": "PT_TERM_CANONICAL" if "terminology" in path else "PT_FOUNDATION",
            "audience_id": "ALL",
            "reference_layer_id": "REF_KNOWLEDGE",
            "template": template,
            "page_family": page_family,
            "content_subdir": "cohort-03-expansion/de" if lang == "de" else "cohort-03-expansion",
        })
        seq += 1

    if len(rows) != TARGET_NEW_ROUTES:
        raise ValueError(f"expected {TARGET_NEW_ROUTES} new rows, built {len(rows)}")
    return rows


def route_record_from_row(row: dict) -> dict:
    h1 = build_h1(row)
    title = f"{h1} | bisulfid.com"
    lang = row["language"]
    content_file = (
        f"main/content/{lang}/pages/{row['content_subdir']}/{row['route_id'].replace('_', '-')}.md"
    )
    layer = "terminology_system"
    if row.get("page_family") in ("reference_governance",):
        layer = "foundation_reference"
    elif row.get("page_family") == "disambiguation":
        layer = "methodology_reference"
    elif row.get("page_family") == "gateway":
        layer = "gateway" if "home" not in row["route_id"] else "public_gateway"
    return {
        "route_id": row["route_id"],
        "path": row["route_path"],
        "language": lang,
        "locale": lang,
        "source_language": lang,
        "title": title,
        "description": f"A governed reference draft: {h1} (planned route; non-public).",
        "h1": h1,
        "layer": layer,
        "template": row["template"],
        "content_file": content_file,
        "status": "planned",
        "indexable": False,
        "in_sitemap": False,
        "in_navigation": False,
        "translation_status": "source_planned",
        "hreflang_group": row["route_id"],
        "alternate_routes": {},
        "required_internal_links": ["en_foundation_sovereign_intro"],
        "required_claim_groups": ["terminology_claims"],
        "source_required": True,
        "risk_level": "medium",
        "notes": (
            f"Sprint 6M-E. COHORT_03 1,500-page pipeline expansion ({row.get('page_type_id', 'governed')}). "
            f"draft-backed; non-public; noindex. 14,000-page objective unchanged."
        ),
    }


def fill_missing_drafts(routes: list[dict], write: bool) -> tuple[int, list[str]]:
    filled = 0
    errors: list[str] = []
    for route in routes:
        cf = route.get("content_file", "")
        if not cf:
            continue
        path = ROOT / cf
        if path.is_file():
            continue
        body = render_de_markdown({"route_id": route["route_id"], "h1_override": route.get("h1")}) if route.get("language") == "de" else render_missing_en_markdown(route)
        if len(re.findall(r"\w+", body)) < 150:
            errors.append(f"{route['route_id']}: backfill too thin")
            continue
        if "[SOURCE REQUIRED]" not in body:
            errors.append(f"{route['route_id']}: backfill missing [SOURCE REQUIRED]")
            continue
        if write:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(body, encoding="utf-8")
        filled += 1
    return filled, errors


def run(write: bool) -> int:
    print("=== Sprint 6M-E Corpus Expansion v1 ===")
    print(f"Date: {date.today().isoformat()}")
    print(f"Mode: {'write' if write else 'dry_run'}")
    print()

    routes_data = json.loads(ROUTES_PATH.read_text(encoding="utf-8"))
    routes = routes_data["routes"]
    existing_ids = {r["route_id"] for r in routes}
    before_count = len(routes)
    before_backed = sum(1 for r in routes if r.get("content_file") and (ROOT / r["content_file"]).is_file())

    filled, fill_errors = fill_missing_drafts(routes, write)
    print(f"Missing drafts backfilled: {filled}")

    new_rows = build_cohort03_rows(existing_ids)
    new_routes = [route_record_from_row(r) for r in new_rows]
    for nr in new_routes:
        if nr["route_id"] in existing_ids:
            print(f"FAIL — duplicate route_id {nr['route_id']}")
            return 1

    if write:
        routes_data["routes"] = routes + new_routes
        ROUTES_PATH.write_text(json.dumps(routes_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    drafts_written = 0
    for row in new_rows:
        body = render_de_markdown(row) if row["language"] == "de" else render_en_markdown(row)
        words = len(re.findall(r"\w+", body))
        if words < 150:
            fill_errors.append(f"{row['route_id']}: thin draft ({words} words)")
            continue
        if "[SOURCE REQUIRED]" not in body:
            fill_errors.append(f"{row['route_id']}: missing [SOURCE REQUIRED]")
            continue
        cf = route_record_from_row(row)["content_file"]
        if write:
            out = ROOT / cf
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(body, encoding="utf-8")
        drafts_written += 1

    if fill_errors:
        print("FAIL — validation errors:")
        for e in fill_errors[:20]:
            print(f"  - {e}")
        return 1

    after_routes = before_count + len(new_routes) if write else before_count + len(new_routes)
    after_backed = before_backed + filled + drafts_written if write else before_backed + filled + len(new_rows)

    manifest = {
        "version": "1.0.0",
        "sprint": "6M-E",
        "cohort_id": COHORT_ID,
        "engine": ENGINE,
        "date": date.today().isoformat(),
        "routes_before": before_count,
        "routes_after": after_routes,
        "draft_backed_before": before_backed,
        "draft_backed_after": after_backed,
        "missing_drafts_filled": filled,
        "new_routes_added": len(new_routes),
        "target_new_routes": TARGET_NEW_ROUTES,
        "target_renderable": 1500,
    }
    inventory = {"version": "1.0.0", "cohort_id": COHORT_ID, "row_count": len(new_rows), "rows": new_rows}

    if write:
        INVENTORY_OUT.write_text(json.dumps(inventory, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        MANIFEST_OUT.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        links_data = json.loads(INTERNAL_LINKS_PATH.read_text(encoding="utf-8"))
        links_data["link_groups"].append({
            "from_route_id": "en_index_cohort03_spine",
            "status": "planned",
            "intended_links": ["en_foundation_sovereign_intro", "en_index_terminology_spine"],
        })
        INTERNAL_LINKS_PATH.write_text(json.dumps(links_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Routes: {before_count} -> {after_routes}")
    print(f"Draft-backed (projected): {after_backed}")
    print(f"New COHORT_03 routes: {len(new_routes)}")
    print("PASS — expansion plan validated")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="Write routes, content, and manifests")
    args = parser.parse_args()
    return run(write=args.write)


if __name__ == "__main__":
    sys.exit(main())
