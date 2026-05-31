# GitHub Pages Public Deployment Gate Report — Sprint 6M-H

**Date:** 2026-05-31  
**Branch:** `claude/sprint-6m-h-github-pages-public-deployment-gate`  
**Status:** Complete — governed Pages deployment gate established

## Why this sprint exists

Sprint 6M-G proved the 14,000-page controlled public launch foundation inside the repository (`site/public/`). Visitors cannot see that output until a governed deployment path serves `site/public/` as the web root. Sprint 6M-H closes that gap without corpus expansion or gate opening.

## Why public deployment must follow the 14,000-page foundation

The foundation HTML, manifest, governance banners, and `noindex,nofollow` posture already exist and validate. Deployment must expose that artifact — not regenerate, rewrite, or replace it.

## Why GitHub Pages main/root is not sufficient

If GitHub Pages serves the repository root (`/`), visitors see governance files, scripts, `main/`, and `site/_sample/` paths — not the 14,000 public foundation pages under `site/public/`. That would misrepresent the launch foundation and break the sovereign output boundary.

## Why site/public/ must be the web root

All 14,000 public foundation pages live at `site/public/{route_path}/index.html`. Deploying `site/public/` as the artifact root maps `/acquire/` → `site/public/acquire/index.html` correctly. The manifest, CNAME, and `.nojekyll` travel with the artifact.

## Why direct CNAME commit from GitHub UI is blocked

`main` is branch-protected. GitHub Pages UI CNAME changes can commit directly to the default branch, bypassing PR review and Corpus Governance CI. CNAME belongs in `site/public/CNAME` and merges via PR.

## Why branch protection must not be disabled

Branch protection preserves PR review, CI validation, and fail-closed governance before any production-facing change — including deployment configuration.

## Chosen deployment model

**GitHub Actions → upload `site/public/` artifact → deploy to GitHub Pages**

Workflow: `.github/workflows/pages-public-deploy.yml`

## Workflow trigger model

- **Initial:** `workflow_dispatch` only (explicit human trigger).
- **Future (optional):** `push` to `main` after live deployment verification — not enabled in this sprint.

## Artifact root

`site/public/` — and only `site/public/`.

Pre-deploy check verifies 14,000 `index.html` files and manifest presence.

## CNAME handling

- File: `site/public/CNAME`
- Content: `bisulfid.com`
- Merged via PR; not via GitHub Pages UI direct commit.

## .nojekyll handling

- File: `site/public/.nojekyll` (empty marker file)
- Prevents Jekyll from processing paths with underscores or skipping raw HTML assets.

## What this sprint does not authorize

- Corpus or content expansion
- Sitemap publication (`sitemap.xml`)
- Navigation artifact publication
- Indexation opening (`indexable: true`, `index,follow`)
- Source or claim approval
- Removal of `[SOURCE REQUIRED]`
- Deployment of repository root or `site/_sample/`
- Cloudflare API automation
- Dependency install or build-time corpus regeneration

## Relationship to indexation/sitemap/navigation gates

Deployment makes HTML **reachable** at the public URL. It does **not** open indexation (pages remain `noindex,nofollow`), sitemap, or navigation gates. Search exposure and wayfinding remain separate authorized sprints.

## Relationship to future public search exposure

Live deployment with `noindex,nofollow` allows human/CDN/hosting verification before any indexation pilot. Sitemap and navigation sprints follow only after live-site checks confirm correct artifact serving.
