# COHORT_02 English Terminology Route Generation Report

**Sprint:** 6H  
**Cohort:** `COHORT_02_EN_TERMINOLOGY_SPINE`  
**Date:** 2026-05-30  
**Posture:** Route inventory only — no content, no routes.json merge

---

## Summary

| Metric | Value |
| --- | ---: |
| Inventory rows generated | **902** |
| Target range | 500–1,000 |
| Entities in spine | **50** |
| Comparison pairs | **12** |
| Language | **en** (primary launch spine) |
| `routes.json` modified | **No** |
| Content files created | **0** |
| LLM used | **No** |

---

## Generation method

Deterministic inventory emission from:

- `main/data/ontology/sulfur_terms.json` (center-node and core terms)
- Sprint **6G** COHORT_02 sequencing charter
- `SOVEREIGN_ROUTE_GENERATION_MATRIX_WAVE_1.json` eligibility rules
- `SOVEREIGN_TEMPLATE_CONTRACT_MODEL_WAVE_1.json` template bindings
- `SOVEREIGN_ROUTE_INVENTORY_SCHEMA_WAVE_1.json` row schema

Each row is a **valid dimensional intersection** — not Cartesian inflation. Invalid combinations rejected at generation time.

---

## Row distribution by page type

| page_type_id | Rows |
| --- | ---: |
| PT_TERM_CANONICAL | 300 |
| PT_AUDIENCE_EXPLAINER | 250 |
| PT_COMPOUND_ENTITY | 128 |
| PT_AI_READABLE | 100 |
| PT_CHILD_SAFE_EDU | 76 |
| PT_DIFFERENCE_COMPARISON | 48 |
| **Total** | **902** |

---

## Row distribution by reference layer

| reference_layer_id | Rows |
| --- | ---: |
| REF_KNOWLEDGE | 232 |
| REF_RESEARCH | 194 |
| REF_TECHNICAL | 144 |
| REF_EDUCATIONAL | 138 |
| REF_ACADEMIC | 82 |
| REF_LINGUISTIC | 62 |
| REF_INSTITUTIONAL | 50 |

---

## Row distribution by audience

| audience_id | Rows |
| --- | ---: |
| AUD_STUDENT | 232 |
| AUD_CHEMIST | 194 |
| AUD_RESEARCHER | 194 |
| AUD_AI_SYSTEM | 144 |
| AUD_ANALYST | 50 |
| AUD_GOVERNMENT | 50 |
| AUD_CHILD_EDU | 38 |

---

## Default safety posture (all 902 rows)

| Field | Value |
| --- | --- |
| route_state | inventory_planned |
| indexation_state | noindex_default |
| source_posture | source_required_unresolved |
| claim_posture | claim_pending_review |
| knowledge_reliability_level | L2_draft_cautious |
| generation_eligibility | conditional |
| publication_eligibility | false |
| noindex_default | true |
| sitemap_default | false |
| navigation_default | false |
| production_route_registry | false |

---

## Entity spine coverage

50 EN terminology entities spanning:

- Core ontology terms (bisulfid, bisulfide, sulfid, sulfide, etc.)
- Compound class (sulfates, sulfides, disulfides, industrial naming)
- Concept class (nomenclature, suffix boundaries, procurement naming language)
- 12 comparison pairs (linguistic and technical distinction intent)

High-risk entities (`hydrogen_sulfide`, `sodium_bisulfide`, `sodium_hydrosulfide`) **exclude** child-safe educational inventory rows.

---

## Multilingual expansion readiness

Each row includes `hreflang_group` for future DE/FR/ES/AR/JA/ZH mirror inventory waves. English rows are the **institutional spine** — alternates require separate cohort with verified equivalence governance.

---

## Next steps (not Sprint 6H)

1. Human review of inventory sample (≥10%)
2. COHORT_02 draft generation charter (separate sprint)
3. Selective `routes.json` merge wave when authorized
4. Never bulk auto-write routes.json

---

*Sprint 6H — COHORT_02 Route Generation Report*
