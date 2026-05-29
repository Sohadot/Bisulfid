# GitHub Actions Governance — Validation Report

**Sprint:** 5P-A  
**Validation date:** 2026-05-29  
**Branch:** `claude/sprint-5p-a-github-actions-governance-workflow-layer`

---

## Scripts run locally

| Script | Exit | Result |
| --- | ---: | --- |
| `scripts/corpus_validation_runtime_l1.py` | 0 | **PASS** |
| `scripts/source_claim_guardrail_runtime_l1.py` | 0 | **PASS** |
| `scripts/corpus_production_runtime_l2.py` | 0 | **PASS** |
| `scripts/corpus_production_planner_l2.py` | 0 | **PASS** (dry-run report) |
| `scripts/validate_route_registry_l0.py` | 0 | **PASS** (present; included in workflow) |
| `scripts/validate_content_drafts_l0.py` | 0 | **PASS** (present; included in workflow) |

Local runs confirm workflow scripts pass before CI merge.

---

## Workflow file checked

| File | Status |
| --- | --- |
| `.github/workflows/corpus-governance-ci.yml` | **Created** — name **Corpus Governance CI** |

---

## Workflow trigger check

| Trigger | Present |
| --- | ---: |
| `pull_request` → `main` | **Yes** |
| `workflow_dispatch` | **Yes** |
| `push` deploy to `main` | **No** (correct) |

---

## Workflow permissions check

**PASS** — top-level `permissions: contents: read` only.

---

## Workflow no-secrets check

**PASS** — no `secrets.*` references; no `env` secret bindings; no deployment environments.

---

## Workflow no-deploy check

**PASS** — no Cloudflare, GitHub Pages, `peaceiris/actions-gh-pages`, Wrangler, or deploy steps.

---

## Workflow no-artifacts check

**PASS** — no `actions/upload-artifact`; no build output steps.

---

## Workflow no-package-install check

**PASS** — no `npm`, `pip`, `pnpm`, `yarn`, or `poetry` install steps. Only `actions/setup-python@v5` for interpreter.

---

## Corpus metrics (planner output)

| Metric | Value |
| --- | ---: |
| Route count | **126** |
| Draft-backed route count | **68** |
| Missing draft count | **58** |

---

## Lock posture (planner output)

| Lock | Result |
| --- | --- |
| Route publication lock | **LOCKED** (all `planned`) |
| Indexation lock | **LOCKED** |
| Sitemap lock | **LOCKED** |
| Navigation lock | **LOCKED** |
| Source registry lock | **inactive** |
| Claim registry lock | **inactive** (0 approved) |
| `production_can_safely_proceed` | **no** |

---

## Runtime results (local pre/post sprint)

| Runtime | Result |
| --- | --- |
| L1 corpus runtime | **PASS** |
| Source/claim guardrail runtime | **PASS** |
| L2 production runtime | **PASS** |
| L2 planner | **PASS** |

---

## Registry and content unchanged

| Check | Result |
| --- | --- |
| `routes.json` | **Not modified** |
| Registries / content / packages / README | **Not modified** |
| No HTML generated | **Confirmed** |

---

## Final validation conclusion

**PASS** — Sprint **5P-A** governance workflow layer established. `.github/workflows/corpus-governance-ci.yml` runs read-only L1, guardrail, L2, and L0 validators on `pull_request` to `main` and `workflow_dispatch` with `contents: read` only. No secrets, deploy, artifacts, or package managers. All local runtimes **PASS**. Corpus locks held. Ready for merge pending GitHub Actions first-run verification on PR.

---

## Post-merge recommendation

Enable branch protection on `main` requiring **Corpus Governance CI** success (repository settings). First PR after merge will validate workflow execution in GitHub-hosted runners.
