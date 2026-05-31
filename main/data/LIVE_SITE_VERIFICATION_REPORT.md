# Live Site Verification Report — Sprint 6M-I

**Date:** 2026-05-31  
**Branch:** `claude/sprint-6m-i-live-site-verification-and-render-defect-register`  
**Live URL:** https://bisulfid.com

## Deployment success confirmation

GitHub Pages public deploy workflow completed successfully. `bisulfid.com` serves controlled `site/public/` foundation HTML — not repository root README.

## bisulfid.com serving site/public/

| Check | Result |
|-------|--------|
| `https://bisulfid.com/` | **200** — Public launch foundation HTML |
| `https://bisulfid.com/what-is-bisulfid/` | **200** — Foundation page with governance markers |
| Contains `bisulfid-frame` / public launch foundation | **Yes** |
| Serves README at root | **No** |

## Repository root exposure check

| Path | Live result |
|------|-------------|
| `/README.md` | **404** — not exposed |

## site/_sample exposure check

| Path | Live result |
|------|-------------|
| `/_sample/` | **404** — quarantine not exposed |

## scripts exposure check

| Path | Live result |
|------|-------------|
| `/scripts/` | **404** — not exposed |

## main exposure check

| Path | Live result |
|------|-------------|
| `/main/` | **404** — not exposed |

## noindex status

Live home and sample routes include `noindex, nofollow` in HTML. Local artifact: 14,000 pages with noindex posture. **Indexation gate: CLOSED.**

## sitemap status

| Check | Result |
|-------|--------|
| `https://bisulfid.com/sitemap.xml` | **404** |
| `site/public/sitemap.xml` | **Absent** |

**Sitemap gate: CLOSED.**

## navigation status

Navigation slot inactive in rendered HTML (`data-navigation-status="inactive"`). No production navigation artifact. **Navigation gate: CLOSED.**

## source/claim gate status

| Gate | Status |
|------|--------|
| Source approval | **CLOSED** — no approval implied in live HTML |
| Claim approval | **CLOSED** — `no_claims_approved` posture preserved |
| `[SOURCE REQUIRED]` | **Visible** where unresolved in content |

Registry files unchanged. Routes remain `planned`, not `published`.

## Live visibility conclusion

**PASS — controlled public visibility is operational.**

Deployment succeeded: `site/public/` is the live web root. Forbidden repository paths are not exposed. All publication gates except visibility remain closed.

**Caveat:** Public visibility exposes first-rendering defects (documented in `PUBLIC_RENDERING_DEFECT_REGISTER.md`). Visibility success does not mean indexation-ready presentation.
