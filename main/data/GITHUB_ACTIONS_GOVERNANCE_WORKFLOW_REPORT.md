# GitHub Actions Governance Workflow — Report

**Sprint:** 5P-A  
**Date:** 2026-05-29  
**Branch:** `claude/sprint-5p-a-github-actions-governance-workflow-layer`

---

## Why this sprint exists

Bisulfid.com must scale from **126** planned routes toward **500** governed launch pages and eventually **1,000+**, **3,000+**, and a much larger sovereign reference corpus. Local validation alone cannot enforce governance at pull-request scale. Sprint **5P-A** establishes the **first GitHub Actions governance workflow layer** — automated, read-only CI checks that mirror existing local runtimes — without deployment, publishing, or registry mutation.

---

## Why GitHub Actions are needed now

| Factor | Detail |
| --- | --- |
| Automation maturity | L1 (Sprint **5K**), guardrails (Sprint **5N-B**), L2 production (Sprint **5O-A**) runtimes all **PASS** locally |
| Corpus scale path | **126 → 500 → 1,000+** requires merge-blocking gates before registry/content waves |
| Human error risk | PRs could bypass local validation if CI does not enforce the same scripts |
| Dry-run discipline | Sprint **5O-B** documented wave planning; CI must hold locks on every merge to `main` |

GitHub Actions turn **documented governance** into **enforced governance** at merge time.

---

## Why workflows were not created earlier

Prior sprints intentionally built **local read-only validators first** (L0 → L1 → guardrails → L2) and **documentation-only** source and production waves (5N-G, 5O-B). Deployment and publishing automation were explicitly deferred until:

1. Validator runtimes stabilized and passed consistently.
2. Source/claim and publication locks were documented.
3. A governance-only CI layer could be added without coupling to Cloudflare, GitHub Pages, or HTML generation.

Sprint **5P-A** is the first sprint chartered specifically for **governance CI**, not deployment.

---

## Relationship to Sprint 5K L1 automation

Sprint **5K** established `corpus_validation_runtime_l1.py` and L1 validators for routes, drafts, publication lock, claims, and references. The governance workflow runs this runtime on every qualifying pull request — same checks, CI-enforced.

---

## Relationship to Sprint 5N-B source/claim guardrails

Sprint **5N-B** established `source_claim_guardrail_runtime_l1.py`. The workflow runs guardrail validators on every PR — blocking merges that would weaken source registry lock, claim registry lock, or proposal discipline.

---

## Relationship to Sprint 5O-A L2 production automation

Sprint **5O-A** established L2 production planning and validation runtimes. The workflow runs `corpus_production_runtime_l2.py` and `corpus_production_planner_l2.py` (dry-run report) to enforce production gate posture — including `production_can_safely_proceed: no` when locks are held.

---

## Relationship to Sprint 5O-B dry-run planning

Sprint **5O-B** documented Route Registration Wave 2 dry-run candidates without registry execution. CI ensures **production_can_safely_proceed** and publication locks remain enforced on every merge — dry-run planning does not bypass merge gates.

---

## Relationship to 500-page launch threshold

| Metric | Value |
| --- | ---: |
| Launch threshold | **500** governed pages |
| Current routes | **126** (all `planned`) |
| CI role | Block merges that violate publication/indexation locks or validator discipline |
| CI does not | Increment governed page count or authorize launch |

Governance CI protects threshold integrity; it does not substitute for launch authorization.

---

## Workflow created

| File | Purpose |
| --- | --- |
| `.github/workflows/corpus-governance-ci.yml` | **Corpus Governance CI** — read-only validator orchestration |

---

## Triggers

| Trigger | Behavior |
| --- | --- |
| `pull_request` → `main` | Runs full governance validation on PRs targeting `main` |
| `workflow_dispatch` | Manual on-demand validation without deployment |

**Not included:** `push` to `main` deployment, release automation, or scheduled publish jobs.

---

## Scripts run (in workflow order)

1. `scripts/corpus_validation_runtime_l1.py`
2. `scripts/source_claim_guardrail_runtime_l1.py`
3. `scripts/corpus_production_runtime_l2.py`
4. `scripts/corpus_production_planner_l2.py`
5. `scripts/validate_route_registry_l0.py` (if present — required in this repository)
6. `scripts/validate_content_drafts_l0.py` (if present — required in this repository)

All scripts are **read-only** / **dry-run**; stdlib-only; no file writes.

---

## What the workflow enforces

- Route registry integrity (L0/L1)
- Draft and publication lock discipline
- Claim registry inactivity and guardrails
- Source registry lock and proposal discipline
- L2 production wave, link graph, SEO/indexation, and multilingual **planning** validators
- Production planner dry-run posture (route counts, locks, `production_can_safely_proceed`)

**Failure behavior:** Any script returning nonzero **fails the job** and blocks PR merge (subject to branch protection configuration).

---

## What the workflow does not do

- Deploy to Cloudflare, GitHub Pages, or any host
- Generate public HTML
- Run `build.py`, `generate_sitemap.py`, or `generate_robots.py`
- Modify `routes.json`, registries, or content
- Approve claims or register sources
- Use repository secrets or deployment environments
- Run npm/pip/package managers (validators are stdlib-only)
- Upload deployment artifacts

---

## Why this is governance CI, not deployment CI

| Governance CI (5P-A) | Deployment CI (not created) |
| --- | --- |
| Read-only validators | Build and publish artifacts |
| `contents: read` | Often `contents: write`, secrets, environments |
| Blocks bad merges | Ships public output |
| No network beyond checkout/setup | CDN, Pages, Cloudflare API |

Deployment automation requires a **separate sprint** with explicit launch authorization and security review.

---

## Why no routes were added

CI enforcement does not change the route registry. **126** routes remain `planned`.

---

## Why no content pages were created

Governance CI validates existing corpus discipline; it does not create or edit Markdown drafts.

---

## Why no sources were added

Source registry remains **inactive**. CI runs guardrail lock validators only.

---

## Why no claims were approved

Claim registries remain **inactive** with **0** approved claims.

---

## Why no routes were published

All routes remain `planned`, non-indexable, out of sitemap and navigation. CI validates publication lock — it does not publish.

---

## Recommended next sprint

**Sprint 5N-H prep — human external verification** for `de_core_mos2` named candidates (Spektrum primary; PubChem/NIST supporting; Chemie.de secondary). Parallel: Draft Wave 1 backlog reduction (**58** missing drafts).

**Do not proceed to:** Route Registration Wave 2 execution, Draft Wave 2, deployment workflows, or GitHub Pages/Cloudflare integration without separate sprint charter.

**Optional follow-up:** Branch protection rule requiring **Corpus Governance CI** pass on `main` (repository settings — outside this sprint).

---

## Sprint 5P-A deliverables

| File | Purpose |
| --- | --- |
| `.github/workflows/corpus-governance-ci.yml` | Governance workflow |
| `GITHUB_ACTIONS_GOVERNANCE_WORKFLOW_REPORT.md` | This report |
| `GITHUB_ACTIONS_GOVERNANCE_SECURITY_MODEL.md` | Security model |
| `GITHUB_ACTIONS_GOVERNANCE_VALIDATION_REPORT.md` | Local + workflow validation |
| `GITHUB_ACTIONS_GOVERNANCE_NEXT_ACTIONS.md` | Next sprint guidance |

**Not modified:** `routes.json`, registries, content pages, package files, deployment configs, root `README.md`.
