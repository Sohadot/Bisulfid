# COHORT_02 Full Non-Public Draft Generation Report

**Sprint:** 6I  
**Cohort:** `COHORT_02_EN_TERMINOLOGY_SPINE`  
**Date:** 2026-05-30  
**Engine:** `scripts/generate_cohort_02_full_draft_wave_v1.py`  
**Posture:** Non-public draft generation only — no route registration, no publication, no public HTML

---

## Summary

| Metric | Value |
| --- | ---: |
| Inventory rows input | **902** |
| Drafts generated | **902** |
| Rows rejected | **0** |
| Target (full cohort) | **902** |
| Achievement | **100%** |
| `routes.json` modified | **No** |
| Registered routes (unchanged) | **141** |
| Public HTML generated | **No** |
| LLM used | **No** |
| Deterministic engine | **Yes** |

---

## Blocker status

**No hard blocker.** Initial generator run failed on a registry key mismatch (`audience_layers` vs `audiences` in `audience_layer_registry.json`). Corrected in-engine; full 902-row generation succeeded on second run.

No schema rejection of output location `main/content/en/pages/cohort-02-terminology/`. All 902 markdown drafts written.

---

## Generation method

Deterministic, registry-constrained emission from:

- `main/data/COHORT_02_EN_TERMINOLOGY_ROUTE_INVENTORY.json` (902 rows)
- `main/data/corpus_route_formula.json`
- `main/data/page_type_registry.json`
- `main/data/audience_layer_registry.json`
- `main/data/reference_layer_registry.json`
- `main/data/SOVEREIGN_CORPUS_GENERATOR_SCHEMA_WAVE_1.json`
- `main/data/SOVEREIGN_TEMPLATE_CONTRACT_MODEL_WAVE_1.json`
- `main/data/SOVEREIGN_EVIDENCE_GRADE_REGISTRY_WAVE_1.json`
- `main/data/SOVEREIGN_SOURCE_HIERARCHY_MODEL_WAVE_1.json`
- `main/data/INITIAL_14000_PAGE_LAUNCH_COMPOSITION_MODEL.json`
- `main/data/sources/source_registry.json` (read-only)
- `main/data/claims/terminology_claims.json` (read-only)

Each draft includes: reliability notice, source/claim transparency, excluded claim classes, unresolved fields, publication blockers, internal-link placeholders by `route_id` only, and `[SOURCE REQUIRED]` markers for unsupported factual lines.

---

## Draft distribution by page type

| page_type_id | Drafts |
| --- | ---: |
| PT_TERM_CANONICAL | 300 |
| PT_AUDIENCE_EXPLAINER | 250 |
| PT_COMPOUND_ENTITY | 128 |
| PT_AI_READABLE | 100 |
| PT_CHILD_SAFE_EDU | 76 |
| PT_DIFFERENCE_COMPARISON | 48 |
| **Total** | **902** |

---

## Draft quality envelope

| Metric | Value |
| --- | ---: |
| Min word count | 311 |
| Max word count | 360 |
| Mean word count | ~320 |
| Min body size (bytes) | ~3,200 |
| All include `[SOURCE REQUIRED]` | Yes |
| All include source/claim section | Yes |
| All include publication blockers | Yes |
| Markdown hyperlinks | 0 |
| Raw URLs | 0 |

---

## Default safety posture (all 902 drafts)

| Field | Value |
| --- | --- |
| status | draft |
| publication_status | non_public |
| publication_eligibility | false |
| indexable | false |
| in_sitemap | false |
| in_navigation | false |
| noindex_default | true |
| source_posture | source_required_unresolved |
| claim_posture | claim_pending_review |
| knowledge_reliability_level | L2_draft_cautious |
| production_can_safely_proceed | no |

---

## Output artifacts

| Artifact | Path |
| --- | --- |
| Generator script | `scripts/generate_cohort_02_full_draft_wave_v1.py` |
| Manifest | `main/data/COHORT_02_FULL_DRAFT_MANIFEST.json` |
| Blueprints | `main/data/COHORT_02_FULL_DRAFT_BLUEPRINTS.json` |
| Draft files | `main/content/en/pages/cohort-02-terminology/*.md` (902 files) |
| Quality report | `main/data/COHORT_02_FULL_DRAFT_QUALITY_ANTI_THIN_VALIDATION_REPORT.md` |
| Guardrail report | `main/data/COHORT_02_FULL_DRAFT_NO_PUBLICATION_NO_ROUTE_REGISTRATION_GUARDRAIL.md` |
| Validation report | `main/data/COHORT_02_FULL_DRAFT_GENERATION_VALIDATION_REPORT.md` |

---

## Explicit non-actions (verified)

- `routes.json` not modified (141 routes)
- No COHORT_02 routes registered
- No sitemap activation
- No navigation activation
- No indexation approval
- No source_registry.json changes
- No terminology_claims.json changes
- No public HTML generation
- No new claims approved
- No new sources registered

---

## Recommended next step

Sprint **6J** (or equivalent): COHORT_02 draft validation charter, internal-link graph planning, and controlled route-registration wave planning — still subject to source/claim gates and `production_can_safely_proceed: no`.
