# Sovereign Visual Interface Reconstruction Report — Sprint 6N-D

**Date:** 2026-06-01  
**Branch:** `claude/sprint-6n-d-sovereign-visual-interface-reconstruction`

## Why this sprint exists

Sprint 6N-C proved the design-system integration was **structurally valid** — 14,000 pages linked local CSS, governance markers were present, and all gates remained closed. After deployment, the **live interface remained visually unacceptable**: flat, text-heavy, lacking spatial identity, and not expressing the BISULFID chemical-language world.

## Why 6N-C was structurally successful but visually insufficient

6N-C integrated templates and tokens at a **foundation level**. It closed DEF-01 through DEF-05 structurally but did not reconstruct the **first-screen experience**, material palette, or spatial depth required for a sovereign control-room interface.

## Why the live interface was not acceptable

Observed defects included broken top visuals, weak palette, governance text overload, raw `true`/`false` leakage, generic term cards, missing missing-E and source-crystal identity, absent relation lattice, browser-default feeling, and mobile typography crowding.

## Fixed material palette

| Material | Role | Usage |
|----------|------|-------|
| **Deep carbon gray** | Primary base | Backgrounds, control-room shell, panels, spatial voids |
| **Warm sulfur yellow** | Substance signal | Signal lines, missing-E boundary, active term nodes |
| **Molybdenum silver** | Future-material accent | Metallic frames, source-crystal edges, advanced nodes |

Tokens: `--bs-carbon-*`, `--bs-sulfur-*`, `--bs-molybdenum-*`.

## Visual defects addressed

See `SOVEREIGN_VISUAL_INTERFACE_DEFECT_CLOSURE_MATRIX.md` for full closure tracking.

## Chemical-language control room expression

- **Hero shell** with CSS perspective, chemical-space SVG, floating term nodes, missing-E boundary
- **Relation lattice** with layered SVG plane and governed term-node anchors
- **Source crystal** metallic visual with authority-state styling
- **Compact governance chips** replacing raw paragraph dumps
- **Term cards** with carbon panel gradient, sulfur accent rail, molybdenum typography

## CSS/SVG depth before WebGL

Perspective container, translateZ layer depths, chemical-space SVG lattice, depth gradients, and optional motion governed by `prefers-reduced-motion`. WebGL remains out of scope per engine boundary.

## Governance visibility without overload

Governance posture moved from multi-paragraph banners to **compact chips**: noindex, sitemap closed, navigation closed, route status, source-required. Screen-reader summary preserved; raw boolean values removed from visible text.

## Source/claim truth preserved

`[SOURCE REQUIRED]` remains visible. Source crystal states remain `--required` / `--candidate` — never default approved. No registry or content modifications.

## Mobile improvements

Responsive hero (perspective disabled on narrow viewports), chip-wrapped governance, balanced typography via clamp scales, no horizontal overflow, designed term-card hierarchy.

## Out of scope

Indexation, sitemap, navigation, source/claim approval, content expansion, WebXR/AR, external UI libraries, npm/CDN/fonts/tracking.

## Why indexation remains closed

Visual maturity is required but not sufficient for publication authorization. All pages retain `noindex,nofollow`.

## Visual proof gate before full 14,000 render

Sprint 6N-C showed that **validators can PASS while the eye says FAIL**. Sprint 6N-D adds a mandatory **Visual Proof Gate** before any full public refresh.

### Proof routes (deterministic 7)

- `home`
- `what_is_bisulfid`
- `de_core_mos2`
- `en_index_disambiguation_map`
- `bisulfide_hydrosulfide_sulfide`
- `sources`
- `corpus_methodology_overview`

### Command

```bash
python scripts/build.py --render-visual-proof-sample
```

Output: `site/public/_visual_proof_sample/` (7 pages + `visual_proof_manifest.json`).

### Proof must demonstrate

- Carbon / sulfur / molybdenum palette applied clearly
- No broken top visual
- No raw governance overload
- No leaked `true`/`false` in visible UI
- Compact governance chips
- Visible missing-E motif
- Visible source crystal / source-required state
- Visible relation lattice or chemical-space layer
- Visible CSS/SVG depth
- Mobile-first hierarchy improved
- No browser-default feeling

### Gate rule

**Do not run** `--render-public-design-system-refresh --limit 14000` until:

1. Visual proof sample renders successfully
2. Human eye review passes on proof routes
3. `visual_review_status` is set to `approved` in `visual_proof_manifest.json`

If proof remains weak, improve tokens/components and re-render proof only — **not** the full corpus.

## Build requirement (after proof approval)

```bash
python scripts/build.py --render-public-design-system-refresh --limit 14000
```

Blocked at build time until visual proof manifest is `approved`.

## Next step

1. Render and review visual proof sample
2. After approval → full 14,000 refresh
3. GitHub Pages redeploy → Sprint 6M-J live re-check

