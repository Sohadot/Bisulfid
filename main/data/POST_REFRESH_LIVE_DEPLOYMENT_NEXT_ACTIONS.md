# Post-Refresh Live Deployment Next Actions — Sprint 6N-C

**Date:** 2026-06-01

## Ready for GitHub Pages redeploy?

**Yes — after merge and local validation PASS.** The refreshed 14,000-page foundation under `site/public/` is ready for governed redeploy via the existing Pages workflow. **Do not open indexation.**

## Criteria for running Pages public deploy

1. Sprint 6N-C merged to `main`
2. `validate_14000_design_system_public_refresh_l1.py` — **PASS**
3. Full validator suite — **PASS**
4. Manifest shows `design_system_refresh: true`, sprint **6N-C**
5. 14,000 foundation pages with design-system CSS; 0 raw Markdown; 0 QA placeholders
6. Gates remain closed: indexation, sitemap, navigation, source, claim

**Action:** Run GitHub Pages public deploy workflow (`site/public/` only).

## Criteria for live-site verification after redeploy

**Sprint 6M-J — Post-Refresh Live Site Verification:**

1. `https://bisulfid.com/` serves design-system-integrated HTML (not browser-default)
2. Forbidden paths still 404 (`/scripts/`, `/main/`, `/_sample/`, `/README.md`)
3. `noindex,nofollow` present on live pages
4. No raw Markdown or QA placeholder text visible live
5. `[SOURCE REQUIRED]` visible where unresolved
6. Sitemap/navigation still absent live
7. Run `validate_live_site_visibility_l1.py` + refresh validator against deployed state

## Criteria for closing or downgrading 6M-I defects

| Defect | Close when live re-check confirms |
|--------|-------------------------------------|
| DEF-01 | Design-system CSS loads on live sample routes |
| DEF-02 | No raw `**` on live gateway/glossary pages |
| DEF-03 | No QA placeholder text live |
| DEF-04 | Structured governance banner live |
| DEF-05 | Design-system assets linked live |

Defect register update happens in **6M-J**, not at merge.

## Why indexation remains closed until live re-check

Local refresh success does not guarantee CDN/Pages deploy fidelity. Live verification must confirm presentation before any indexation discussion.

## Why sitemap and navigation remain closed

Presentation maturity is necessary but not sufficient. Sitemap and navigation require explicit sprint authorization after live PASS.

## Recommended next sprint after deployment

1. **Merge 6N-C** → **GitHub Pages redeploy**
2. **Sprint 6M-J — Post-Refresh Live Site Verification** (indexation **still CLOSED**)
3. Only after 6M-J PASS: consider **6N-D** motion layer or controlled gate-opening sprints (none authorized now)

**Important:** Do **not** open indexation after 6N-C merge. Redeploy first, verify live, then decide.
