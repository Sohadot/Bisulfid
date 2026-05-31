# GitHub Pages Public Deployment Next Actions — Post Sprint 6M-H

## Is the deployment workflow ready to run?

**Yes, after merge and repository settings update.** The workflow is configured for `workflow_dispatch`. It should not be run until:

1. PR merges to `main` with Corpus Governance CI PASS
2. GitHub repository **Settings → Pages → Source** is set to **GitHub Actions** (not Deploy from branch / root)

## GitHub Pages source setting

Change Pages source from branch/root to **GitHub Actions** so the workflow artifact (`site/public/`) becomes the served site — not repository root.

## Custom domain / DNS

- `site/public/CNAME` contains `bisulfid.com`
- DNS must point `bisulfid.com` (and optionally `www`) to GitHub Pages
- Verify HTTPS certificate provisioning after first deployment
- Do not configure CNAME via GitHub UI direct commit to protected `main`

## Indexation — remain closed initially

Keep `noindex,nofollow` on all foundation pages until live-site verification confirms correct serving. Indexation opening is a separate authorized sprint.

## Sitemap — remain closed initially

No `sitemap.xml` in artifact. Sitemap sprint follows indexation planning.

## Navigation — remain closed initially

No navigation artifact in artifact. Navigation curation sprint follows separately.

## Criteria for first deployment run

- [ ] Sprint 6M-H merged to `main`
- [ ] Pages source = GitHub Actions
- [ ] Run **Pages public deploy** workflow manually (`workflow_dispatch`)
- [ ] Workflow completes without error
- [ ] Artifact upload shows 14,000 pages from `site/public/`

## Criteria for post-deployment live-site verification

- [ ] `https://bisulfid.com/` serves foundation home (not repo README or 404 root)
- [ ] Sample routes resolve (e.g. `/acquire/`, `/what-is-bisulfid/`)
- [ ] `site/_sample/` paths are **not** reachable on live site
- [ ] Repository paths (`/scripts/`, `/main/`) are **not** reachable
- [ ] Response HTML includes `noindex,nofollow` and governance banners
- [ ] `[SOURCE REQUIRED]` visible where expected
- [ ] No sitemap or navigation artifacts at live URLs

## Criteria for future indexation-opening sprint

- Live deployment verified stable
- Robots/indexation policy explicitly authorized
- Source/claim posture reviewed for indexable subset
- Separate sprint — not part of deployment gate

## Criteria for future sitemap-opening sprint

- Indexation policy defined
- `sitemap_policy.json` activation planned
- Governed URL selection — no blind 14,000 URL dump

## Criteria for future navigation-opening sprint

- Editorial navigation model defined
- `navigation.json` curation for governed subsets
- No mass navigation of 14,000 planned routes

## Immediate next step after this sprint

**Run deployment workflow and perform live-site verification** — not corpus expansion, not content work, not indexation/sitemap/navigation opening until live serving is confirmed correct.
