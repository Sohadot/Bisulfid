# Bisulfid Design System Public Refresh 14,000 Report — Sprint 6N-C

**Date:** 2026-06-01  
**Branch:** `claude/sprint-6n-c-controlled-14000-design-system-public-refresh`  
**Command:** `python scripts/build.py --render-public-design-system-refresh --limit 14000`

## Why this sprint exists

Sprint 6N-B proved the design-system integration on a 7-route pilot. The live site still served 14,000 browser-default foundation pages. Sprint 6N-C applies the integrated templates to the full public corpus while keeping all sensitive gates closed.

## Why the 7-route pilot justified full refresh

The integration sample passed all validators: local assets, structured governance UI, no raw Markdown, no QA placeholders, preserved `[SOURCE REQUIRED]`, and closed indexation/sitemap/navigation gates. The template and build pipeline were stable enough for deterministic full-scale re-render.

## Why the live site cannot remain browser-default

Live visibility (6M-I) exposed DEF-01 through DEF-05. Browser-default rendering undermines sovereign chemical-language identity and leaves engineering defects visible on `bisulfid.com` after deployment.

## 6M-I defects addressed

| ID | Defect | Status after 6N-C |
|----|--------|---------------------|
| DEF-01 | Default browser styling | **Closed** — design-system CSS on all 14,000 pages |
| DEF-02 | Raw Markdown markers | **Closed** — 0 files with `**` markers |
| DEF-03 | QA placeholder leakage | **Closed** — 0 files with QA slot text |
| DEF-04 | Governance raw-text overload | **Reduced** — `bs-governance-banner` structured UI |
| DEF-05 | Design system not integrated | **Closed** — 14,000/14,000 pages linked |

## Public output refreshed

- **14,000** foundation pages under `site/public/` (excluding `_integration_sample/`)
- `site/public/public_launch_manifest.json` updated with `design_system_refresh: true`, sprint **6N-C**
- `site/public/assets/bisulfid-design-system/` preserved and synced
- `site/public/_integration_sample/` **preserved** (7 pilot routes unchanged)

## Design-system layers now present

- `/assets/bisulfid-design-system/bisulfid-frame.css` bundle
- `bs-control-room` body framing
- `bs-governance-banner` gate visibility
- `bs-source-crystal` source states
- `bs-term-card` + `bs-language-depth` term/reference frames
- Missing-E boundary SVG motif

## Out of scope

- Indexation, sitemap, navigation opening
- Source/claim approval
- WebGL / WebXR / AR
- Routes, content, registry changes
- External CSS/JS, npm, CDN, tracking

## Gates remain closed

| Gate | Status |
|------|--------|
| Indexation | **CLOSED** — `noindex,nofollow` on all pages |
| Sitemap | **CLOSED** — no sitemap artifact |
| Navigation | **CLOSED** — no navigation artifact |
| Source approval | **CLOSED** |
| Claim approval | **CLOSED** |
| Visibility | **OPEN** |

## Source/claim truth preserved

- `[SOURCE REQUIRED]` markers remain visible where unresolved
- Default source crystal states: `--required` / `--candidate`, never `--approved`
- `claim_approval_state`: `no_claims_approved`
- No registry or content modifications

## Scale support

Single local CSS bundle, CSS custom properties, no JS required for core content — suitable for 14,000 pages today and 100,000+ governed routes tomorrow.

## Next step

Governed GitHub Pages redeploy, then **Sprint 6M-J — Post-Refresh Live Site Verification** (indexation remains closed).
