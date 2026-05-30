# Sovereign Content Automation Engine v1 — Validation Report

**Sprint:** 6D  
**Date:** 2026-05-30  
**Branch:** `claude/sprint-6d-sovereign-content-automation-engine-v1`  
**Base:** main @ Sprint 6C merge (`b605f6c`)

---

## Pre-flight (before engine changes)

| Script | Result |
| --- | --- |
| `corpus_production_runtime_l2.py` | **PASS** |
| `corpus_validation_runtime_l1.py` | **PASS** |
| `source_claim_guardrail_runtime_l1.py` | **PASS** |
| `corpus_production_planner_l2.py` | **PASS** |
| `validate_source_registry_lock_l1.py` | **PASS** |
| `validate_claim_registry_lock_l1.py` | **PASS** |
| `validate_corpus_claims_l1.py` | **PASS** |

**Pre-flight posture:** `production_can_safely_proceed: no`; all locks **LOCKED**.

---

## Engine run

| Check | Result |
| --- | --- |
| Engine script | `scripts/generate_sovereign_foundation_cohort_v1.py` |
| Mode | `--write-drafts` |
| Units validated | **15 / 15** |
| LLM used | **false** |
| routes.json modified | **false** |
| Registered routes unchanged | **126** |

---

## Post-run validation (after engine + drafts)

| Script | Result |
| --- | --- |
| `corpus_production_runtime_l2.py` | **PASS** |
| `corpus_validation_runtime_l1.py` | **PASS** |
| `source_claim_guardrail_runtime_l1.py` | **PASS** |
| `corpus_production_planner_l2.py` | **PASS** |
| `validate_source_registry_lock_l1.py` | **PASS** (0 errors, 2 warnings) |
| `validate_claim_registry_lock_l1.py` | **PASS** (0 errors, 3 warnings) |
| `validate_corpus_claims_l1.py` | **PASS** (0 errors, 5 warnings) |

---

## Post-run posture

| Gate | Value |
| --- | --- |
| `production_can_safely_proceed` | **no** |
| `routes.json` row count | **126 (unchanged)** |
| Indexation lock | **LOCKED** |
| Sitemap lock | **LOCKED** |
| Navigation lock | **LOCKED** |
| Source registry | **inactive** |
| Claim registry | **inactive** |

---

## Draft file checks

- **15** files under `main/content/en/pages/foundation/`
- All have `status: draft`, `publication_status: non_public`
- All have `indexable: false`, `in_sitemap: false`, `noindex_default: true`
- All have `generated: true`, `engine: sovereign_content_automation_engine_v1`
- No draft sets `indexable`, `in_sitemap`, or `in_navigation` true

---

## Conclusion

Content Automation Engine v1 **PASS** — registry-constrained COHORT_01 drafts generated safely. All L1/L2 runtimes **PASS**. Publication gates remain closed.
