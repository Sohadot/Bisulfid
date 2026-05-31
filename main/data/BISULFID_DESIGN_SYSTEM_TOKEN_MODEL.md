# Bisulfid Design System Token Model — Sprint 6N-A

## Color token model

| Family | Prefix | Purpose |
|--------|--------|---------|
| Foundation | `--bs-color-foundation-*` | Deep control-room backgrounds |
| Sulfur signal | `--bs-color-sulfur-*` | Bisulfid brand accent |
| Graphite/ink | `--bs-color-ink-*`, `--bs-color-graphite-*` | Text and grid lines |
| Source state | `--bs-color-source-*` | Authority progression (not default approval) |
| Unresolved source | `--bs-color-source-required-*` | `[SOURCE REQUIRED]` visibility |
| Language depth | `--bs-color-lang-*` | EN/DE/future language layers |
| Boundary/accent | `--bs-color-boundary-*` | Spelling, ion, compound boundaries |

## Typography token model

- **Institutional title scale** — `--bs-font-size-title-*`, institutional family
- **Term label scale** — primary/secondary/meta term typography
- **Source annotation scale** — small caps emphasis for governance labels
- **Multilingual fallback** — Latin, CJK, Arabic font stacks declared
- **RTL readiness** — logical properties documented; `dir="rtl"` support notes

## Spacing token model

- **Page rhythm** — inline/block/section gutters
- **Card rhythm** — padding and header/footer gaps
- **Lattice rhythm** — node, edge, cluster spacing
- **Source bar spacing** — marker and inline padding
- **Governance banner spacing** — lock list and item gaps

## Motion token model

- **Missing-E principle** — subtle boundary shift; not approval signal
- **Relation pulse** — data-bound lattice edges only
- **Source-state transition** — border/background transitions on class change
- **Reduced-motion fallback** — `@media (prefers-reduced-motion: reduce)` zeroes durations

## Depth token model

- **Chemical-space depth** — semantic z-index layers
- **Card elevation** — flat, raised, floating, source-required ring
- **Perspective limits** — CSS-only caps; WebGL separate

## Governance token model

| State | Token prefix |
|-------|--------------|
| Public visibility | `--bs-gov-visibility-*` |
| Noindex | `--bs-gov-noindex-*` |
| Source required | `--bs-gov-source-required-*` |
| Source candidate | `--bs-gov-source-candidate-*` |
| Source approved (boundary) | `--bs-gov-source-approved-*` |
| Claim approved (boundary) | `--bs-gov-claim-approved-*` |

## Accessibility considerations

- Contrast: ink on foundation surfaces
- Motion: reduced-motion honored at token and component level
- Semantic HTML required at integration time
- SVG assets include `role="img"` and `aria-label`

## Multilingual considerations

- EN/DE active color depth tokens
- AR/FR/ES/JA/ZH reserved as future/inactive layers
- RTL via logical properties and `[dir="rtl"]` component rules
