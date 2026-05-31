# Design System Integration Urgency Report — Sprint 6M-I

**Date:** 2026-05-31  
**Trigger:** First live public visibility on bisulfid.com

## Why 6N-B is now urgent

Sprint 6M-I confirmed deployment success and live visibility. That visibility **exposed** presentation defects that were invisible when output lived only in the repository. The gap between foundation HTML and sovereign presentation is now user-visible on a custom domain.

**6N-B (Design System Template Integration Pilot)** is the immediate next sprint because:

1. Live site shows default browser styling across 14,000 pages.
2. QA placeholder text and raw Markdown are publicly visible.
3. Governance truth is correct but visually unstructured.
4. `bisulfid-design-system/` exists (6N-A) but is not wired into templates.

## Why bisulfid-design-system must move into templates

The design system is the governed presentation layer: tokens, components, motion governor, SVG assets. Templates are the publication frame. Without integration:

- Tokens never reach `site/public/` HTML.
- Components (governance banner, source crystal, term frame) remain unused.
- Every page renders as unstyled engineering output.

Integration path: template registry → frame partials → CSS/JS from `bisulfid-design-system/` → controlled re-render of pilot cohort → validate → expand.

## Why tokens/components should be integrated before sitemap/indexation

| Gate | Depends on presentation |
|------|-------------------------|
| Indexation | Search snippets and first impressions |
| Sitemap | Declares URLs as ready for discovery |
| Navigation | User journeys across styled routes |

Opening discovery gates before presentation integration would advertise:

- QA placeholder strings
- Raw `**markdown**` syntax
- Unstyled governance walls

**Order of operations:** visibility (done) → design integration (6N-B) → controlled re-render → live re-check → then consider indexation/sitemap/navigation.

## Why raw public visibility is acceptable as foundation but not as final presentation

**Foundation visibility (current):** Proves deployment boundary, gate separation, and controlled `site/public/` serving. `noindex,nofollow` limits search exposure while engineering truth is validated.

**Final presentation (not yet):** Sovereign typography, structured governance UI, no engineering leakage, designer-authored hierarchy. Required before indexation opening.

The sprint correctly treats live visibility as **verification infrastructure**, not **launch presentation**.

## Why designer-authored UI remains a strategic asset layer

Bisulfid is a governed reference asset, not a generic documentation site. Designer-authored UI encodes:

- Visual hierarchy for chemical-language authority
- Governance surfaces that communicate lock status without overwhelming prose
- Motion and depth governed by `motion-governor.js`
- Brand continuity across 14,000+ routes

Engineering can render truth; design system renders **trust**. Deferring integration after live visibility would accumulate public-facing debt on every indexed URL.

## Recommendation

Proceed immediately to **Sprint 6N-B — Design System Template Integration Pilot** before any indexation, sitemap, or navigation gate opening.
