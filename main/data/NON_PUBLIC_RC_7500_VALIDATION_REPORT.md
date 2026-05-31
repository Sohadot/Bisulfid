# Non-Public RC 7,500 Validation Report

**Sprint:** 6M-F  
**Validation date:** 2026-05-31  
**Branch:** `claude/sprint-6m-f-7500-page-14k-pipeline-non-public-rc`

---

## Scripts run

| Script | Result |
|--------|--------|
| `scripts/validate_7500_rc_batch_l1.py` | **PASS** (7,500 files) |
| `scripts/validate_release_candidate_batch_l1.py` | **PASS** (7,500 files) |
| `scripts/validate_template_registry_l1.py` | **PASS** |
| `scripts/validate_template_layer_l1.py` | **PASS** |
| `scripts/validate_sample_output_l1.py` | **PASS** (7,500 files) |
| `scripts/validate_build_engine_l1.py` | **PASS** |
| `scripts/build.py --dry-run` | **PASS** |
| `scripts/build.py --dry-run --strict` | **PASS** |
| `scripts/build.py --render-quarantined-rc-batch --limit 7500` | **PASS** (7,500 rendered, 0 skipped) |
| `scripts/corpus_production_runtime_l2.py` | **PASS** |
| `scripts/corpus_validation_runtime_l1.py` | **PASS** |
| `scripts/source_claim_guardrail_runtime_l1.py` | **PASS** |
| `scripts/corpus_production_planner_l2.py` | **PASS** |

---

## Batch output checked

| Check | Result |
|-------|--------|
| Rendered count | **7,500** |
| Skipped count | **0** |
| Batch ID | `rc_7500` |
| Output path scope | `site/_sample/` only |
| No public HTML outside `site/_sample/` | **PASS** |
| No sitemap output | **PASS** |
| No navigation output | **PASS** |
| No route status changes to published | **PASS** |
| No indexable route changes | **PASS** |
| No sitemap/navigation flag changes | **PASS** |
| No registry changes (source/claim/sitemap/nav policy) | **PASS** |
| Governed content expansion only | **PASS** |
| No source approval | **PASS** |
| No claim approval | **PASS** |
| No `[SOURCE REQUIRED]` removal | **PASS** |
| noindex on all RC pages | **PASS** |
| Non-public RC markers present | **PASS** |
| Publication locks remain LOCKED | **PASS** |

---

## Corpus posture (post-sprint)

| Metric | Value |
|--------|-------|
| Routes | 7,500 |
| Draft-backed | 7,500 |
| Published | 0 |
| Indexable | 0 |
| In sitemap | 0 |
| In navigation | 0 |
| `production_can_safely_proceed` | **no** |

---

## Final validation conclusion

**PASS** — Sprint 6M-F completed successfully. The 7,500-page non-public RC batch renders under quarantine without weakening publication, indexation, sitemap, navigation, source, or claim locks. Corpus Governance CI remains required on PR merge.
