# Design System Template Integration Next Actions — Sprint 6N-B

**Date:** 2026-05-31

## Is the integration pilot ready for wider public re-render?

**Not yet automatically.** The 7-route integration sample **PASS**es validation. A wider re-render requires explicit sprint authorization and full validator suite on the refreshed cohort.

## Criteria for refreshing all 14,000 pages

1. Integration sample PASS on all DEF-01 through DEF-05 checks
2. Full validator suite PASS after `--render-public-launch-foundation --limit 14000`
3. Live site re-verification (`validate_live_site_visibility_l1.py`)
4. No QA placeholder text in output
5. No raw Markdown in sampled gateway/glossary routes
6. Design-system CSS linked on all pages
7. Indexation/sitemap/navigation gates remain **CLOSED** unless separately authorized

## Criteria for adding missing-E motion

- Template integration stable on pilot + sample cohort
- `motion-governor.js` opt-in only; reduced-motion fallback verified
- No JS required for core content readability

## Criteria for adding source-crystal visuals

- Registry-bound state transitions only
- Never default to `--approved`
- `[SOURCE REQUIRED]` always visible when unresolved

## Criteria for adding language-depth visuals

- Per-route language token from routes.json
- RTL routes validated before AR wave

## Criteria for future raw WebGL prototype

- Dedicated governed sprint
- Quarantined path (not live foundation)
- No external 3D libraries
- Indexation remains closed during prototype

## Criteria for future raw WebXR prototype

- Same as WebGL plus accessibility and motion governance review
- Experimental layer only

## Why indexation should remain closed until public rendering is mature

Opening indexation before sovereign presentation remediation would index QA placeholders, raw Markdown, and unstyled governance walls on 14,000 URLs.

## Recommended next sprint

**6N-C — Controlled 14,000-Page Design System Re-Render** (or scoped cohort re-render) after integration pilot review merge, followed by live site re-check before any indexation/sitemap/navigation gate discussion.
