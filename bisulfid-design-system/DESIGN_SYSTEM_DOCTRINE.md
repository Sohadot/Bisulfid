# Bisulfid Design System Doctrine

## Identity

Bisulfid is a **chemical-language control room**. A term is a governed node — not decorative copy. Each node carries:

- element / ion / compound posture
- spelling boundary (e.g. Bisulfid vs Bisulfide)
- source authority state
- language depth
- translation ambiguity
- industrial context (bounded, not operational guidance)
- governance state (visibility, indexation, source, claim)

## Designer leads code

1. Visual grammar is authored first (tokens, shapes, motion principles).
2. Code translates grammar into CSS custom properties and lightweight components.
3. No framework dictates layout; Bisulfid identity dictates layout.

## Rejected approaches

- Bootstrap, Tailwind, Material, or any third-party UI kit
- Visual clones of other reference sites
- npm/CDN delivery
- Motion or WebGL that obscures source-required status

## Source and claim truth

Components **display** governance data; they **never invent** approval. `[SOURCE REQUIRED]` must remain visible. Approved states use explicit data-bound classes only.

## Scale

Foundation must work on static HTML at 14,000 pages today and 100,000+ tomorrow — lightweight CSS, no runtime dependency graph.

## Progressive layers (6N-A scope: 1–5 only)

| Layer | Sprint 6N-A |
|-------|-------------|
| Tokens | Created |
| Components | Created |
| SVG identity | Created |
| Motion grammar | motion-governor.js |
| Progressive interaction | Documented |
| WebGL/WebXR | **Deferred** — boundary documented in engine/README.md |

## Accessibility

- Semantic HTML when integrated
- `prefers-reduced-motion` honored
- Contrast tokens for ink on foundation backgrounds
- RTL readiness via logical properties and typography notes
