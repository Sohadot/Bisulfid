# COHORT_02 Controlled Route Registration Report

**Sprint:** 6K  
**Cohort:** `COHORT_02_EN_TERMINOLOGY_SPINE`  
**Date:** 2026-05-30  
**Posture:** Route registration only — no publication, no public HTML

---

## Summary

| Metric | Before | After |
| --- | ---: | ---: |
| Registered routes in `routes.json` | 141 | **1,043** |
| COHORT_02 routes registered | 0 | **902** |
| Existing routes preserved | 141 | **141** |
| COHORT_02 draft files created | 0 | **0** |
| Public HTML generated | 0 | **0** |
| Routes published | 0 | **0** |
| `production_can_safely_proceed` | no | **no** |

---

## Registration method

Deterministic merge from:

- `main/data/COHORT_02_EN_TERMINOLOGY_ROUTE_INVENTORY.json` (902 rows)
- `main/data/COHORT_02_FULL_DRAFT_MANIFEST.json` (902 units)
- `main/data/COHORT_02_FULL_DRAFT_BLUEPRINTS.json`
- `main/data/COHORT_02_INTERNAL_LINK_GRAPH.md` (required_internal_links)
- Sprint **6J** quality gate attestation

Each COHORT_02 route registered as:

| Field | Value |
| --- | --- |
| status | `planned` |
| indexable | `false` |
| in_sitemap | `false` |
| in_navigation | `false` |
| source_required | `true` |
| required_claim_groups | `["terminology_claims"]` |
| layer | `terminology_system` |
| risk_level | `medium` |

---

## Registration by page type

| page_type_id | Routes registered |
| --- | ---: |
| PT_TERM_CANONICAL | 300 |
| PT_AUDIENCE_EXPLAINER | 250 |
| PT_COMPOUND_ENTITY | 128 |
| PT_AI_READABLE | 100 |
| PT_CHILD_SAFE_EDU | 76 |
| PT_DIFFERENCE_COMPARISON | 48 |
| **Total** | **902** |

---

## Comparison route path disambiguation

Inventory contained **12** duplicate base paths across **48** comparison routes (4 reference-layer variants per pair). Registration disambiguated paths by appending reference-layer segments from `route_id`:

**Pattern:** `{inventory route_path}{ref}/{aud}/`  
**Example:** `/en/terminology/compare/bisulfid-vs-bisulfide/chem/ling/`

All **1,043** registry paths are unique after disambiguation.

---

## L1 schema alignment (content_file slug)

COHORT_02 draft files use route_id-aligned filenames with underscores under `cohort-02-terminology/`. `validate_corpus_routes_l1.py` was aligned to permit `[a-z0-9_\-]` slugs in that directory only. This is filename discipline alignment for the 6I generator convention — not a publication, indexation, or claim-gate change.

---

## Internal links

`required_internal_links` populated from inventory `internal_link_targets`, filtered to registered `route_id` values (excluding planning `glossary` token). Foundation bridge `en_foundation_sovereign_intro` included on all applicable routes.

---

## Explicit non-actions (verified)

- No new content pages created
- No COHORT_02 draft content modified
- No public HTML generated
- No sitemap/navigation/indexation activation
- No source/claim registry changes
- No routes set to `published`
- No validator publication-lock weakening

---

## Corpus scale note

Registered route count **1,043** exceeds the 500-page planning threshold. All routes remain **planned**, **non-indexable**, and **non-public**. `production_can_safely_proceed` remains **no**.

---

*Sprint 6K — COHORT_02 Controlled Route Registration Report*
