# Sovereign Foundation COHORT_01 — Route Registration Report

**Sprint:** 6F  
**Cohort:** `COHORT_01_FOUNDATION_GOV`  
**Date:** 2026-05-30  
**Posture:** Route registration only — **not publication**

---

## Summary

| Metric | Before | After |
| --- | ---: | ---: |
| Registered routes | 126 | **141** |
| COHORT_01 routes registered | 0 | **15** |
| Routes published | 0 | **0** |
| Indexable routes | 0 | **0** |
| Sitemap routes | 0 | **0** |
| Navigation routes | 0 | **0** |
| Draft-backed routes | 68 | **83** |

All **15** COHORT_01 foundation drafts are now registered in `routes.json` as **planned**, **draft-backed**, **non-public** routes.

---

## Registration principle

Each new route conforms to the existing `routes.json` schema enforced by `validate_corpus_routes_l1.py`:

- `status`: **planned** (registry lock — not published)
- `indexable`: **false**
- `in_sitemap`: **false**
- `in_navigation`: **false**
- `source_required`: **false** (governance framing; claim_not_required)
- `required_claim_groups`: **[]**
- `required_internal_links`: populated from Sprint 6E internal-link graph
- `content_file`: bound to existing foundation draft under `main/content/en/pages/foundation/`

---

## Registered routes (15)

| route_id | path | layer | page type (notes) |
| --- | --- | --- | --- |
| `en_foundation_sovereign_intro` | `/en/foundation/sovereign-reference-introduction/` | foundation_reference | PT_FOUNDATION |
| `en_foundation_institutional_purpose` | `/en/foundation/institutional-purpose/` | foundation_reference | PT_FOUNDATION |
| `en_foundation_methodology` | `/en/foundation/methodology/` | methodology_reference | PT_METHODOLOGY_GOVERNANCE |
| `en_foundation_source_policy` | `/en/foundation/source-policy-overview/` | methodology_reference | PT_METHODOLOGY_GOVERNANCE |
| `en_foundation_claim_policy` | `/en/foundation/claim-policy-overview/` | methodology_reference | PT_METHODOLOGY_GOVERNANCE |
| `en_foundation_knowledge_reliability` | `/en/foundation/knowledge-reliability-model/` | methodology_reference | PT_METHODOLOGY_GOVERNANCE |
| `en_foundation_multilingual_overview` | `/en/foundation/multilingual-corpus-overview/` | foundation_reference | PT_FOUNDATION |
| `en_foundation_reference_layers` | `/en/foundation/reference-layer-overview/` | foundation_reference | PT_FOUNDATION |
| `en_foundation_audience_layers` | `/en/foundation/audience-layer-overview/` | foundation_reference | PT_FOUNDATION |
| `en_foundation_chemical_language_governance` | `/en/foundation/chemical-language-governance-framework/` | methodology_reference | PT_METHODOLOGY_GOVERNANCE |
| `en_foundation_ai_readable_policy` | `/en/foundation/ai-readable-reference-policy/` | methodology_reference | PT_METHODOLOGY_GOVERNANCE |
| `en_foundation_child_safe_policy` | `/en/foundation/child-safe-educational-policy/` | methodology_reference | PT_METHODOLOGY_GOVERNANCE |
| `en_foundation_economic_institutional_restrictions` | `/en/foundation/economic-institutional-claim-restrictions/` | methodology_reference | PT_METHODOLOGY_GOVERNANCE |
| `en_foundation_corpus_status` | `/en/foundation/corpus-status/` | foundation_reference | PT_CORPUS_STATUS |
| `en_foundation_launch_status` | `/en/foundation/launch-status-non-public-corpus/` | foundation_reference | PT_CORPUS_STATUS |

---

## Internal-link graph wiring

Each route's `required_internal_links` array reflects the Sprint 6E governed graph. Targets are **route_id** references only — no live markdown links added to draft content.

**Orphan count after registration:** **0** (all targets exist in registry).

---

## What was not done

- No route status set to `published`
- No indexation, sitemap, or navigation activation
- No public HTML generation
- No source or claim registry changes
- No draft content rewrites
- No validator weakening

---

## Governance unchanged

| Gate | Status |
| --- | --- |
| `production_can_safely_proceed` | **no** |
| Route publication lock | **LOCKED** (all planned) |
| Indexation lock | **LOCKED** |
| Sitemap lock | **LOCKED** |
| Navigation lock | **LOCKED** |

---

*Sprint 6F — COHORT_01 Route Registration*
