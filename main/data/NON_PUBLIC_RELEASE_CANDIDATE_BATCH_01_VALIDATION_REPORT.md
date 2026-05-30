# Non-Public Release Candidate Batch 01 Validation Report

**Sprint:** 6M-D  
**Validation date:** 2026-05-30  
**Branch:** `claude/sprint-6m-d-14k-pipeline-non-public-release-candidate-batch-01`

---

## Scripts run

| Script | Result |
|---|---|
| `scripts/validate_release_candidate_batch_l1.py` | **PASS** (250 files) |
| `scripts/validate_template_registry_l1.py` | **PASS** |
| `scripts/validate_template_layer_l1.py` | **PASS** |
| `scripts/validate_sample_output_l1.py` | **PASS** (250 files) |
| `scripts/validate_build_engine_l1.py` | **PASS** |
| `scripts/build.py --dry-run` | **PASS** |
| `scripts/build.py --dry-run --strict` | **PASS** |
| `scripts/build.py --render-quarantined-rc-batch --limit 250` | **PASS** (250 rendered) |
| `scripts/corpus_production_runtime_l2.py` | **PASS** |
| `scripts/corpus_validation_runtime_l1.py` | **PASS** |
| `scripts/source_claim_guardrail_runtime_l1.py` | **PASS** |
| `scripts/corpus_production_planner_l2.py` | **PASS** |

---

## Batch output checked

- **250** HTML files under `site/_sample/{route_id}.html`
- Manifest: `site/_sample/rc_batch_manifest.json`
- Matrix: `main/data/NON_PUBLIC_RELEASE_CANDIDATE_BATCH_01_MATRIX.md` (250 rows)

---

## Rendered count

**250** (target limit 250; minimum sprint target 100 met)

---

## Output path scope

All HTML under `site/_sample/` only. No HTML outside quarantine.

---

## Governance confirmation

| Check | Result |
|---|---|
| No public HTML outside `site/_sample/` | **PASS** |
| No sitemap output | **PASS** |
| No navigation output | **PASS** |
| No route status changes | **PASS** |
| No registry changes | **PASS** |
| No content changes | **PASS** |
| No source approval | **PASS** |
| No claim approval | **PASS** |
| No `[SOURCE REQUIRED]` removal | **PASS** |
| noindex on all RC pages | **PASS** |
| Non-public RC markers present | **PASS** |
| Publication locks remain LOCKED | **PASS** |
| `production_can_safely_proceed` | **no** |

---

## Corpus posture (unchanged)

| Metric | Value |
|---|---:|
| Routes | 1,043 |
| Draft-backed | 985 |
| Missing drafts | 58 |
| Published | 0 |
| Indexable | 0 |
| in_sitemap | 0 |
| in_navigation | 0 |

---

## Final validation conclusion

**PASS** — RC Batch 01 completed successfully. All listed validators and runtimes pass. The publication frame renders 250 non-public pages under quarantine without weakening publication, indexation, sitemap, navigation, source, or claim locks. Corpus Governance CI remains required on PR merge.

**This sprint does not authorize public launch.**
