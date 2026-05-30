# COHORT_02 Full Draft Generation Validation Report

**Sprint:** 6I  
**Date:** 2026-05-30  
**Validation phase:** Post-generation (after 902 draft files written)

---

## Verdict

**PASS** — all L1/L2 runtimes and lock validators passed after COHORT_02 full draft generation.

---

## Pre-flight validation (before generation)

| Runtime / Validator | Result |
| --- | --- |
| `corpus_production_runtime_l2.py` | **PASS** |
| `corpus_validation_runtime_l1.py` | **PASS** |
| `source_claim_guardrail_runtime_l1.py` | **PASS** |
| `corpus_production_planner_l2.py` | **PASS** |
| `validate_source_registry_lock_l1.py` | **PASS** |
| `validate_claim_registry_lock_l1.py` | **PASS** |
| `validate_corpus_claims_l1.py` | **PASS** |

Pre-flight confirmed: `production_can_safely_proceed: no`; all corpus locks **LOCKED**.

---

## Post-generation validation (after 902 drafts)

| Runtime / Validator | Result |
| --- | --- |
| `corpus_production_runtime_l2.py` | **PASS** |
| `corpus_validation_runtime_l1.py` | **PASS** |
| `source_claim_guardrail_runtime_l1.py` | **PASS** |
| `corpus_production_planner_l2.py` | **PASS** |
| `validate_source_registry_lock_l1.py` | **PASS** (0 errors, 2 warnings) |
| `validate_claim_registry_lock_l1.py` | **PASS** (0 errors, 3 warnings) |
| `validate_corpus_claims_l1.py` | **PASS** (0 errors, 5 warnings) |

Warnings are governance informational only — no blocking errors.

---

## Engine validation summary

| Metric | Value |
| --- | ---: |
| Inventory rows processed | 902 |
| Rows passing field validation | 902 |
| Rows passing quality scan | 902 |
| Rows rejected | 0 |
| Draft files on disk | 902 |
| Manifest `generated_count` | 902 |
| Blueprint `generated_count` | 902 |

---

## Registry cross-check

| Registry | Read-only | Modified |
| --- | --- | --- |
| `routes.json` | Yes | **No** (141 routes) |
| `source_registry.json` | Yes | **No** |
| `terminology_claims.json` | Yes | **No** |
| `page_type_registry.json` | Yes | **No** |
| `audience_layer_registry.json` | Yes | **No** |

---

## Production planner post-generation snapshot

| Field | Value |
| --- | --- |
| current_route_count | 141 |
| production_can_safely_proceed | **no** |
| route_publication_lock | LOCKED |
| indexation_lock | LOCKED |
| sitemap_lock | LOCKED |
| navigation_lock | LOCKED |
| next_eligible_planning_wave_type | route_registration_wave_2_planning (dry-run) |

---

## Initial generation blocker (resolved)

First engine run rejected all 902 rows due to incorrect registry key `audience_layers` (actual key: `audiences`). Fixed in `generate_cohort_02_full_draft_wave_v1.py`. Second run: **902/902 PASS**.

---

## Summary

| Phase | Errors | Warnings | Status |
| --- | ---: | ---: | --- |
| Pre-flight | 0 | governance | **PASS** |
| Engine generation | 0 | 0 rejections | **PASS** |
| Post-generation | 0 | governance | **PASS** |
