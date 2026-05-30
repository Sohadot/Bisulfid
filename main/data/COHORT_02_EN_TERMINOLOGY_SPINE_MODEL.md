# COHORT_02 English Terminology Spine Model

**Sprint:** 6H  
**Cohort:** `COHORT_02_EN_TERMINOLOGY_SPINE`  
**Date:** 2026-05-30

---

## Purpose

Define the **English terminology spine** — the first major dimensional expansion toward the 14,000-page launch corpus. COHORT_02 inventory rows represent governed reference surfaces for sulfur terminology, compounds, and nomenclature concepts.

---

## Spine architecture

```text
COHORT_01 Foundation (15 routes, registered)
        │
        ▼
COHORT_02 EN Terminology Spine (902 inventory rows, planned)
        │
        ├── PT_TERM_CANONICAL (300) — canonical reference surfaces
        ├── PT_AUDIENCE_EXPLAINER (250) — audience-specific vocabulary
        ├── PT_COMPOUND_ENTITY (128) — compound naming records
        ├── PT_AI_READABLE (100) — machine-readable provenance pages
        ├── PT_CHILD_SAFE_EDU (76) — educational naming only (low-risk entities)
        └── PT_DIFFERENCE_COMPARISON (48) — distinction intent pages
        │
        ▼
Future: COHORT_03+ multilingual mirrors (de, fr, es, ar, ja, zh)
```

---

## Entity classes

| Class | Count | Examples |
| --- | ---: | --- |
| term | 12 | bisulfid, bisulfide, sulfide, sulfur, disulfide |
| compound | 28 | molybdenum_disulfide, sulfate, iron_sulfides, oleum |
| concept | 8 | suffix_id_ide, german_english_nomenclature, sour_gas |
| comparison_pair | 12 | bisulfid_vs_bisulfide, sulfid_vs_sulfide |

**Center node:** `bisulfid` (ontology center_node)

---

## Dimensional combinations per entity

### Standard term/concept (non-compound)

| page_type | Combinations | Notes |
| --- | ---: | --- |
| PT_TERM_CANONICAL | 6 | chemist/academic, chemist/knowledge, researcher/research, student/knowledge, AI/technical, student/linguistic |
| PT_AUDIENCE_EXPLAINER | 5 | chemist, researcher, student, analyst, government |
| PT_AI_READABLE | 2 | AI/technical, researcher/research |
| PT_CHILD_SAFE_EDU | 0–2 | low-risk only; REF_EDUCATIONAL |

### Compound class entities

Additional **PT_COMPOUND_ENTITY** × 4 combinations (chemist/academic, researcher/research, student/knowledge, AI/technical).

---

## Route path pattern

```text
/en/terminology/{entity_slug}/{page_type_code}/{audience_code}/{reference_code}/
```

Example:

```text
/en/terminology/bisulfid/term/chem/acad/
```

Comparison paths:

```text
/en/terminology/compare/{comparison_slug}/{audience_code}/{reference_code}/
```

---

## route_id convention

```text
cohort02_en_{entity_id}_{page_type_code}_{audience_code}_{reference_code}
```

Example: `cohort02_en_bisulfid_term_chem_acad`

**Distinct from** existing `routes.json` route_ids — merge charter required before production registry.

---

## Internal link spine

Every row links (planning graph) to:

- `en_foundation_sovereign_intro` (COHORT_01 root)
- `glossary` (terminology hub)
- Primary term canonical row for entity (where applicable)

Link role by page type: `term_spine`, `audience_cluster`, `ai_readable_cluster`, `child_safe_cluster`, `comparison_cluster`.

---

## Knowledge reliability posture

| page_type | evidence_grade (inventory) | reliability level |
| --- | --- | --- |
| PT_TERM_CANONICAL | terminology_dictionary | L2_draft_cautious |
| PT_COMPOUND_ENTITY | terminology_dictionary | L2_draft_cautious |
| PT_AUDIENCE_EXPLAINER | unsourced_pending | L2_draft_cautious |
| PT_AI_READABLE | unsourced_pending | L2_draft_cautious |
| PT_CHILD_SAFE_EDU | educational_simplification | L2_draft_cautious |
| PT_DIFFERENCE_COMPARISON | comparative_boundary | L2_draft_cautious |

No row implies final factual authority at inventory stage.

---

## High-risk entity exclusions

| Entity | PT_CHILD_SAFE_EDU | Notes |
| --- | --- | --- |
| hydrogen_sulfide | **Excluded** | High risk; no child-safe inventory |
| sodium_bisulfide | **Excluded** | High risk |
| sodium_hydrosulfide | **Excluded** | High risk |
| All low/medium risk | Included | Educational naming only |

---

## Anti-fake / anti-thin rules

- Every row requires valid page_type × audience × reference_layer intersection
- Duplicate `route_id` rejected at generation
- No row without `term_entity_id`
- No free-form generation
- Content generation deferred — inventory only

---

*Sprint 6H — Terminology Spine Model*
