# Template Validation Report

**Sprint:** 6M-B  
**Validation date:** 2026-05-30  
**Branch:** `claude/sprint-6m-b-fourteen-thousand-publication-frame-template-layer`

---

## Verdict

**PASS** — publication frame hardened; all required runtimes PASS; all locks preserved; no public HTML committed.

---

## Files created / updated

| File | Action |
| --- | --- |
| `main/templates/base.html` | Hardened |
| `main/templates/home.html` | Hardened |
| `main/templates/page.html` | Created |
| `main/templates/reference.html` | Created |
| `main/templates/term.html` | Created |
| `main/templates/partials/*.html` | Hardened (9 partials) |
| `scripts/validate_template_layer_l1.py` | Created |
| `scripts/validate_sample_output_l1.py` | Created |
| `site/_sample/.gitkeep` | Quarantine path reserved |

---

## Scripts run

| Script | Result |
| --- | --- |
| `validate_template_layer_l1.py` | **PASS** (3 legacy skeleton warnings) |
| `validate_sample_output_l1.py` | **PASS** (no committed HTML — quarantine empty) |
| `build.py --dry-run` | **PASS** |
| `build.py --dry-run --strict` | **PASS** |
| `corpus_production_runtime_l2.py` | **PASS** |
| `corpus_validation_runtime_l1.py` | **PASS** |
| `source_claim_guardrail_runtime_l1.py` | **PASS** |
| `corpus_production_planner_l2.py` | **PASS** |

---

## Corpus posture (unchanged)

| Field | Value |
| --- | --- |
| Routes | **1,043** |
| Draft-backed | **985** |
| Missing drafts | **58** |
| Eligible for public output | **0** |
| Publication lock | **LOCKED** |
| Indexation lock | **LOCKED** |
| Sitemap lock | **LOCKED** |
| Navigation lock | **LOCKED** |
| `production_can_safely_proceed` | **no** |

---

## QA sample note

`site/_sample/` path established. No HTML committed — L1 publication lock scans all `site/**/*.html`. Local uncommitted QA renders documented for next sprint.

---

## Final validation conclusion

Sprint **6M-B** successfully hardened the sovereign template publication frame for the **14,000-page** launch corpus pipeline without weakening any governance lock.
