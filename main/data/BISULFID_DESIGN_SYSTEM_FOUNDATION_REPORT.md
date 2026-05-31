# Bisulfid Design System Foundation Report — Sprint 6N-A

**Date:** 2026-05-31  
**Branch:** `claude/sprint-6n-a-bisulfid-design-system-foundation`  
**Status:** Complete — proprietary design-system foundation established

## Why this sprint exists

Sprint 6M-G/H delivered 14,000 public foundation pages and a GitHub Pages deployment gate. The asset now needs a **sovereign visual language** — not generic framework styling — before template integration at scale.

## Why Bisulfid needs its own design system

Bisulfid is a chemical-language control room. Terms are governed nodes with source authority, language depth, and spelling boundaries. Generic UI kits cannot express this identity or preserve source/claim truth at 14,000+ pages.

## Why external libraries are rejected

Bootstrap, Tailwind, React, Vue, Three.js, and CDN delivery introduce dependency graphs, visual homogeneity, and upgrade risk incompatible with sovereign static HTML at 100,000+ page scale. Zero npm, zero CDN, zero tracking.

## Why the designer leads the code

Visual grammar (tokens, shapes, motion principles) is authored first. Code translates grammar into CSS custom properties and lightweight components — not the reverse.

## How the design system supports 14,000 pages

- Static CSS custom properties — no runtime framework
- Lightweight components suitable for static HTML
- Governance and source-required states built into tokens/components
- Multilingual depth tokens for EN/DE now, AR/FR/ES/JA/ZH later

## How it scales toward 100,000+ pages

Token-driven styling avoids per-page bespoke CSS. Components compose from shared primitives. Motion is opt-in via vanilla `motion-governor.js`. No bundle graph grows with corpus size.

## How it preserves source/claim truth

- `[SOURCE REQUIRED]` tokens and component modifiers
- Approval states are bounded — classes require registry authorization
- Components never hide disclaimers or imply approval by default

## What was created

| Layer | Files |
|-------|-------|
| Doctrine | `DESIGN_SYSTEM_DOCTRINE.md`, README |
| Tokens | colors, typography, spacing, motion, depth, governance |
| Components | term-node, term-card, source-crystal, governance-banner, language-depth, relation-lattice |
| Assets | 4 original SVG identity files |
| Engine | `motion-governor.js`, WebGL boundary README |

## What was not integrated yet

- No changes to `site/public/` HTML
- No template frame integration (`base.html`, term/reference frames)
- No GitHub Pages deployment workflow changes
- No WebGL/WebXR implementation

## Why WebGL/WebXR are deferred

Static token/component system must integrate and validate on live pages first. WebGL/WebXR documented as future engine boundary in `engine/README.md` only.

## Next integration steps

See `BISULFID_DESIGN_SYSTEM_NEXT_ACTIONS.md` — template integration sprint after foundation review and PR merge.
