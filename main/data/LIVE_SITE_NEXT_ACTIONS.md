# Live Site Next Actions — Sprint 6M-I

**Date:** 2026-05-31  
**Status:** Post live visibility verification

## Do not open yet

| Action | Status | Reason |
|--------|--------|--------|
| **Indexation** | Do not open | `noindex,nofollow` must remain until rendering defects remediated |
| **Sitemap** | Do not publish | No sitemap until presentation is indexation-ready |
| **Navigation** | Do not open | Nav inactive; presentation layer not integrated |

Also unchanged: **source approval CLOSED**, **claim approval CLOSED**, **`[SOURCE REQUIRED]` visible** where unresolved.

## Recommended next sprint: 6N-B

**Sprint 6N-B — Design System Template Integration Pilot**

- Wire `bisulfid-design-system/` tokens and components into publication templates.
- Pilot cohort re-render (not full 14,000 in first pass if scoped).
- Fix QA slot placeholder leakage in template/build path.
- Address raw Markdown body rendering for affected gateway pages.
- Structured governance UI via design-system components.

## After 6N-B: controlled public re-render

1. Run build with integrated templates on approved pilot scope.
2. Validate locally (all L1/L2 gates + design system validator).
3. Deploy via existing GitHub Pages workflow (`site/public/` only).

## After re-render: re-check live site

1. Run `scripts/validate_live_site_visibility_l1.py`.
2. Update live verification and defect register (close resolved DEF items).
3. Confirm forbidden paths still 404.
4. Confirm gates still closed unless explicitly authorized.

## Only then: consider gate opening

Indexation, sitemap, and navigation gate opening require:

- No QA placeholder text in public HTML
- No raw Markdown markers in visible body
- Design system integrated on production frames
- Live re-verification PASS
- Explicit sprint authorization for each gate

**Current authorization:** none. Proceed to 6N-B only.
