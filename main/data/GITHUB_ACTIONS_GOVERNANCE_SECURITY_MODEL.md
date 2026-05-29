# GitHub Actions Governance — Security Model

**Sprint:** 5P-A  
**Date:** 2026-05-29  
**Scope:** `.github/workflows/corpus-governance-ci.yml`

---

## Workflow permission model

| Permission | Value | Rationale |
| --- | --- | --- |
| `contents` | `read` | Checkout and read scripts/data for validation only |
| `actions` | default (none requested) | No workflow mutation |
| `packages` | none | No package publish |
| `deployments` | none | No deployment API |
| `id-token` | none | No OIDC to cloud providers |

The workflow operates under **least privilege**: read repository contents, run Python validators, exit.

---

## Why contents: read is required

`actions/checkout@v4` needs read access to clone the PR head or default branch for validation. No write access is required because validators do not commit, push, or modify files.

---

## Why secrets are not used

| Reason | Detail |
| --- | --- |
| Validators are local/read-only | No API keys, tokens, or credentials needed |
| Attack surface | Secrets in CI expand breach impact |
| Doctrine | Source/claim and publication gates must not depend on external credentials for merge validation |
| Scope | Governance CI validates repository state — not live production systems |

Future deployment workflows may require secrets under a **separate security review** — not in Sprint **5P-A**.

---

## Why deployment is excluded

Deployment implies public output, environment promotion, and rollback responsibility. Bisulfid.com has **0** published routes and **500-page** launch threshold not met. Governance CI must not imply launch readiness or automate publication.

---

## Why Cloudflare is excluded

Cloudflare integration is **deployment/hosting** automation. Sprint **5P-A** charter explicitly prohibits Cloudflare workflows. No Wrangler, no CDN purge, no DNS mutation.

---

## Why GitHub Pages deploy is excluded

GitHub Pages deploy would generate or publish static HTML. All routes remain `planned` and non-indexable. Pages deploy is **publication automation** — forbidden in this sprint.

---

## Why package managers are excluded

| Reason | Detail |
| --- | --- |
| Validator scripts | Python **stdlib only** — no pip/npm dependencies |
| Supply chain | Package install in CI adds third-party risk without governance benefit |
| Reproducibility | Validator behavior must match local `python scripts/...` runs |

`actions/setup-python@v5` configures the interpreter only — no `pip install`.

---

## Why generated artifacts are excluded

Artifact upload is unnecessary for read-only validation. No build output, no HTML bundles, no deployment packages. Omitting artifacts reduces storage exposure and avoids implying deployable output from governance runs.

---

## Why validators must remain read-only

| Risk if validators write | Mitigation |
| --- | --- |
| CI mutates registries on PR | Forbidden — validators documented read-only |
| False merge confidence | Workflow runs existing runtime scripts unchanged |
| Audit failure | Git diff would show CI-side mutations |

Workflow steps run scripts only; no `>` redirects to tracked files, no code generation steps.

---

## PR governance model

1. Contributor opens PR targeting `main`.
2. **Corpus Governance CI** triggers automatically.
3. All L1, guardrail, L2, and L0 validators run sequentially with grouped step names.
4. Any nonzero exit → job failure → merge blocked (when branch protection enabled).
5. Human review remains required for source, claim, and publication decisions — CI does not approve content.

---

## Manual workflow_dispatch use

Maintainers may run **Corpus Governance CI** manually to:

- Validate `main` or a branch without opening a PR
- Re-check governance posture after documentation-only merges
- Confirm runtimes pass in GitHub-hosted environment

Manual dispatch uses the **same read-only steps** — no deployment mode.

---

## Failure behavior

| Outcome | Effect |
| --- | --- |
| All scripts exit 0 | Job **success** |
| Any script exits nonzero | Job **failure**; PR check red |
| Missing expected L0 script | Job **failure** (repository expects L0 validators) |

Logs are grouped by step name for auditability.

---

## What must happen before any future deployment workflow is allowed

All must be true:

1. **500-page** governed launch threshold met or explicit owner waiver with governance sign-off.
2. Publication/indexation locks cleared through documented sprint — not CI alone.
3. Source and claim registries active with verified entries where required.
4. Separate deployment sprint charter — distinct from governance CI.
5. Security review: secrets scope, environments, OIDC, Cloudflare/Pages policy.
6. Governance CI remains **required** on PRs — deployment does not replace validation.
7. No deployment workflow runs on every PR by default without path/filter discipline.
8. Rollback and audit logging documented.

Until then, **Corpus Governance CI** remains governance-only.

---

## Related documents

- `GITHUB_ACTIONS_GOVERNANCE_WORKFLOW_REPORT.md`
- `GITHUB_ACTIONS_GOVERNANCE_VALIDATION_REPORT.md`
- `SOURCE_CLAIM_AUTOMATION_GUARDRAIL_REPORT.md`
- `CORPUS_PRODUCTION_AUTOMATION_LAYER_2_REPORT.md`
