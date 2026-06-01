# Pages Artifact Sample Exclusion Validation Report — Sprint 6N-C-P1

**Date:** 2026-06-01  
**Branch:** `claude/sprint-6n-c-p1-pages-artifact-sample-exclusion-patch`

## Validation date

2026-06-01

## Scripts run

| Script | Result |
|--------|--------|
| `validate_pages_deployment_gate_l1.py` | **PASS** |
| `validate_14000_design_system_public_refresh_l1.py` | **PASS** |
| `validate_bisulfid_design_system_integration_l1.py` | **PASS** |
| `validate_live_site_visibility_l1.py` | **PASS** |
| `validate_public_output_l1.py` | **PASS** |
| `validate_bisulfid_design_system_l1.py` | **PASS** |
| `validate_14000_public_launch_foundation_l1.py` | **PASS** |
| `validate_release_candidate_batch_l1.py` | **PASS** |
| `validate_template_registry_l1.py` | **PASS** |
| `validate_template_layer_l1.py` | **PASS** |
| `validate_sample_output_l1.py` | **PASS** |
| `validate_build_engine_l1.py` | **PASS** |
| `build.py --dry-run` | **PASS** |
| `build.py --dry-run --strict` | **PASS** |
| `corpus_production_runtime_l2.py` | **PASS** |
| `corpus_validation_runtime_l1.py` | **PASS** |
| `source_claim_guardrail_runtime_l1.py` | **PASS** |
| `corpus_production_planner_l2.py` | **PASS** |

## Workflow checked

`.github/workflows/pages-public-deploy.yml`

- `workflow_dispatch` only — **PASS**
- Minimal permissions (`contents: read`, `pages: write`, `id-token: write`) — **PASS**
- Stages temporary artifact excluding `_integration_sample/` — **PASS**
- Uploads staged `artifact_dir`, not raw `site/public/` — **PASS**
- No `build.py`, no dependency install, no secrets, no Cloudflare — **PASS**

## Deploy artifact scope checked

| Check | Result |
|-------|--------|
| Repository root excluded | **PASS** |
| `site/_sample/` excluded | **PASS** |
| `_integration_sample/` excluded from deploy artifact | **PASS** |
| Staged artifact derived from `site/public/` | **PASS** |

## 14,000 page count result

**PASS** — 14,000 foundation `index.html` files in repository; workflow verifies staged artifact equals 14,000.

## _integration_sample exclusion result

**PASS** — 7 integration sample pages remain in repository; workflow excludes directory from staged artifact and asserts `! -e _integration_sample` in staging.

## CNAME result

**PASS** — `site/public/CNAME` present (`bisulfid.com`); copied into staged artifact.

## .nojekyll result

**PASS** — `site/public/.nojekyll` present; copied into staged artifact.

## Asset preservation result

**PASS** — `site/public/assets/bisulfid-design-system/` present; verified in staged artifact step.

## No sitemap result

**PASS** — No sitemap artifact under `site/public/`.

## No navigation result

**PASS** — No navigation artifact under `site/public/`.

## No indexation result

**PASS** — `noindex,nofollow` preserved on sampled foundation pages; manifest gates closed.

## No source/claim approval result

**PASS** — No registry changes; source/claim approval not implied on public pages.

## Final validation conclusion

**PASS** — Sprint 6N-C-P1 deployment-artifact patch validated. Ready for merge and governed Pages public deploy.
