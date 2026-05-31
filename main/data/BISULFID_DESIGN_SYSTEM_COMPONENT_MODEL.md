# Bisulfid Design System Component Model — Sprint 6N-A

## Term node component (`term-node.css`)

Visual identity for a governed terminology node. Supports `--source-required` and `--source-candidate` modifiers. Approval modifiers reserved for registry-bound integration.

## Term card component (`term-card.css`)

Page-level card: title, route type, language badge, body, source bar, disclaimer. Language badges for EN/DE. Approval badge hidden unless explicit approved classes applied.

## Source crystal component (`source-crystal.css`)

Visual authority object with states:

| Modifier | Meaning |
|----------|---------|
| `--required` | Unresolved — shows `[SOURCE REQUIRED]` |
| `--candidate` | Candidate — explicitly not approved |
| `--verified` | Evidence present — not mass approval |
| `--approved` | Registry-bound only |

## Governance banner component (`governance-banner.css`)

Displays public visibility, noindex, gate locks. Compatible with existing publication-frame governance banners at integration time. Does not hide source-required inline markers.

## Language depth component (`language-depth.css`)

Layer chips for EN/DE active; AR/FR/ES/JA/ZH marked planned/inactive. RTL-ready via logical properties.

## Relation lattice component (`relation-lattice.css`)

Controlled relationship visualization. Edges require `data-link-status` and parent `data-edges`. Does not invent links — empty state when no data.

## Source/claim boundary rules

1. Default component posture is **unresolved** or **no claims approved**
2. `.bs-*--source-approved` and `.bs-*--claim-approved` require registry authorization at integration
3. Components **display** governance; they do not **determine** governance
4. `[SOURCE REQUIRED]` must remain visible in source-required states

## What components may never imply

- Source approval without registry data
- Claim approval without claim registry data
- Final publication readiness
- Indexation or sitemap inclusion
- Scientific certainty on unresolved terms
- Operational handling, safety, medical, or market guidance
