# Bisulfid Design System Template Integration Report — Sprint 6N-B

**Date:** 2026-05-31  
**Branch:** `claude/sprint-6n-b-design-system-template-integration-pilot`  
**Sprint:** 6N-B — Design System Template Integration Pilot

## Why this sprint exists

Sprint 6M-I verified live public visibility and registered five rendering defects (DEF-01 through DEF-05). The proprietary design system foundation (6N-A) existed but was not wired into publication templates. This sprint begins closing that gap through a **controlled pilot** before any full 14,000-page re-render.

## Why live visibility exposed the need

Once `bisulfid.com` served `site/public/`, default browser styling, raw Markdown, and QA placeholder text became user-visible. Engineering truth was preserved, but presentation was not sovereign-grade.

## Why browser-default styling is not acceptable

Bisulfid is a governed chemical-language reference asset. Default browser typography and layout fail to express term-node identity, source-crystal authority, language depth, or the missing-E boundary motif that define the Bisulfid control room.

## Why raw Markdown rendering must be fixed

Raw `**bold**` markers signal an unfinished pipeline and undermine trust on gateway and glossary routes. The build engine now converts inline and table-cell Markdown to HTML.

## Why QA placeholder text must not appear publicly

`Slot reserved — not populated in QA render.` is engineering language. Integration and public render modes now emit hidden empty slots instead of QA placeholders.

## Templates modified

| Template | Change |
|----------|--------|
| `main/templates/base.html` | `bs-control-room` frame class |
| `main/templates/home.html` | Term card + language depth |
| `main/templates/page.html` | Term card + language depth |
| `main/templates/reference.html` | Term card + language depth |
| `main/templates/term.html` | Term card + relation lattice slots |
| `main/templates/partials/head.html` | Local design-system CSS link |
| `main/templates/partials/governance_banner.html` | `bs-governance-banner` structure |
| `main/templates/partials/source_bar.html` | `bs-source-crystal` states |
| `main/templates/partials/internal_links.html` | Design-system disclaimer class |

## Design-system layers integrated

- **Tokens:** colors, typography, spacing, motion, depth, governance (`--bs-*`)
- **Components:** governance banner, source crystal, term card, language depth, relation lattice
- **Assets:** missing-E boundary SVG, source crystal SVG (local `/assets/`)
- **Bundle:** `site/public/assets/bisulfid-design-system/bisulfid-frame.css`

## Kept out of scope

- Full 14,000-page public re-render (pilot sample only)
- WebGL / WebXR / AR layers
- Indexation, sitemap, navigation gate opening
- Source or claim approval
- External CSS/JS libraries, npm, CDN, Google Fonts, tracking

## Why WebGL/WebXR are deferred

Motion and chemical-space visualization require governed stages after template integration and missing-E motion layer validation. Raw WebGL/WebXR remain experimental layers in the visual engine roadmap.

## Source/claim truth preserved

- `[SOURCE REQUIRED]` markers remain visible and styled
- Default source crystal state: `--required` or `--candidate`, never `--approved`
- `claim_approval_state`: `no_claims_approved`
- No registry or content modifications

## 14,000-page scale support

Single local CSS bundle, CSS custom properties, no JS required for core content, `prefers-reduced-motion` respected. Lightweight enough for static generation at 14,000+ routes.

## 100,000+ future scale

Token-driven styling and component classes scale horizontally; integration sample validates the template contract before corpus-wide re-render.

## Integration sample output

**Path:** `site/public/_integration_sample/`  
**Routes:** 7 deterministic pilot routes  
**Manifest:** `integration_sample_manifest.json`

The 14,000-page foundation corpus under `site/public/` (excluding `_integration_sample/`) was **not** modified.
