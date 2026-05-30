# Sovereign Foundation COHORT_01 — Route Registration Validation Report

**Sprint:** 6F  
**Date:** 2026-05-30  
**Branch:** `claude/sprint-6f-cohort-01-foundation-route-registration`

---

## Pre-flight (before registration)

| Script | Result |
| --- | --- |
| `corpus_production_runtime_l2.py` | **PASS** |
| `corpus_validation_runtime_l1.py` | **PASS** |
| `source_claim_guardrail_runtime_l1.py` | **PASS** |
| `corpus_production_planner_l2.py` | **PASS** |
| `validate_source_registry_lock_l1.py` | **PASS** |
| `validate_claim_registry_lock_l1.py` | **PASS** |
| `validate_corpus_claims_l1.py` | **PASS** |

**Pre-flight:** routes **126**; `production_can_safely_proceed: no`.

---

## Registration actions

| Action | Result |
| --- | --- |
| Routes added | **15** |
| New route count | **141** |
| Schema compliance | **PASS** (`validate_corpus_routes_l1.py`) |
| Draft binding | **15/15** content files exist |
| Draft validation | **PASS** (`validate_corpus_drafts_l1.py`) |
| Duplicate route_id / path / content_file | **None** |
| Published routes created | **0** |

---

## Post-registration validation

| Script | Result |
| --- | --- |
| `corpus_production_runtime_l2.py` | **PASS** |
| `corpus_validation_runtime_l1.py` | **PASS** |
| `source_claim_guardrail_runtime_l1.py` | **PASS** |
| `corpus_production_planner_l2.py` | **PASS** |
| `validate_source_registry_lock_l1.py` | **PASS** |
| `validate_claim_registry_lock_l1.py` | **PASS** |
| `validate_corpus_claims_l1.py` | **PASS** |
| `validate_corpus_routes_l1.py` | **PASS** (0 errors) |
| `validate_corpus_drafts_l1.py` | **PASS** (0 errors) |

---

## Post-registration posture

| Gate | Value |
| --- | --- |
| `production_can_safely_proceed` | **no** |
| Total routes | **141** |
| COHORT_01 routes | **15** (all planned) |
| Indexable routes | **0** |
| Sitemap routes | **0** |
| Navigation routes | **0** |
| Published routes | **0** |
| Draft-backed routes | **83** (+15) |
| Public HTML | **none** |

---

## New route lock verification (15/15)

All COHORT_01 routes confirmed:

- `status: planned`
- `indexable: false`
- `in_sitemap: false`
- `in_navigation: false`

---

## Warnings (non-blocking)

- Foundation drafts: `cagr` appears in excluded_claim_classes table (listed as exclusion, not assertion) — warnings only
- Pre-existing corpus draft warnings unchanged

---

## Conclusion

Sprint 6F **PASS** — 15 COHORT_01 foundation routes registered schema-compliantly. All L1/L2 runtimes **PASS**. Publication gates remain closed.
