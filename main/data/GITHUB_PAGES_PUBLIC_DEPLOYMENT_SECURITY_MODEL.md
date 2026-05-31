# GitHub Pages Public Deployment Security Model — Sprint 6M-H

## Workflow permissions

| Permission | Value | Purpose |
|------------|-------|---------|
| `contents` | `read` | Checkout repository to read `site/public/` artifact |
| `pages` | `write` | Publish artifact to GitHub Pages |
| `id-token` | `write` | OIDC token for trusted Pages deployment |

## Why contents: read is enough

The workflow only reads the committed `site/public/` tree. It does not push commits, modify branches, or write repository files.

## Why pages: write is required

GitHub Pages deployment via Actions requires permission to publish the uploaded artifact to the Pages environment.

## Why id-token: write is required

`actions/deploy-pages` uses OIDC (`id-token`) for secure deployment without long-lived deploy tokens stored as secrets.

## Why no secrets are used

- No API keys, Cloudflare tokens, or custom deploy credentials.
- OIDC + built-in Pages permissions are sufficient.
- Reduces secret leakage and unauthorized external automation risk.

## Why no Cloudflare API is used

DNS/CDN configuration remains outside this workflow. Sprint 6M-H establishes the repository-side gate only; DNS for `bisulfid.com` is a separate operational step documented in next actions.

## Why no dependency install is needed

The artifact is pre-rendered static HTML committed in `site/public/`. No Node, Python packages, or build toolchain is required at deploy time.

## Why deployment does not mutate repository files

The workflow:
- Checks out read-only
- Verifies artifact counts
- Uploads `site/public/`
- Deploys to Pages

No commit, no corpus regeneration, no registry edits.

## Why site/_sample/ is excluded

7,500 non-public RC pages under `site/_sample/` are quarantined engineering output. Deploying them would expose non-public RC HTML as if it were the launch foundation.

## Why repository root is excluded

Repository root contains scripts, governance data, workflows, and non-public paths. Serving root as the website would violate the sovereign output boundary.

## Branch protection considerations

- Workflow merges via PR to protected `main`.
- Corpus Governance CI runs on PR.
- Pages deployment runs only via explicit `workflow_dispatch` after merge.
- CNAME lives in `site/public/CNAME` — reviewed in PR, not UI-pushed to `main`.

## Required PR/CI posture before merge

1. `corpus-governance-ci.yml` PASS on PR
2. `validate_pages_deployment_gate_l1.py` PASS locally and in review
3. All existing 6M-G public foundation validators PASS
4. No changes to routes, content, source/claim registries, sitemap, or navigation policy
5. Working tree clean after commit
