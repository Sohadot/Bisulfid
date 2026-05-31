# Bisulfid Design System Template Integration Matrix — Sprint 6N-B

**Date:** 2026-05-31

| Template | Design-system layer | Asset path | Source-required preserved | noindex preserved | Sitemap unchanged | Navigation unchanged | Source approval implied | Claim approval implied | Notes |
|----------|---------------------|------------|---------------------------|-------------------|-------------------|----------------------|-------------------------|------------------------|-------|
| `partials/head.html` | Token bundle link | `/assets/bisulfid-design-system/bisulfid-frame.css` | Yes (meta) | Yes (`noindex, nofollow`) | Yes | Yes | No | No | Local CSS only |
| `partials/governance_banner.html` | Governance banner | `components/governance-banner.css` | Yes (inline marker) | Yes (robots lock list) | Yes (gate display) | Yes (gate display) | No | No | `bs-governance-banner--noindex` |
| `partials/source_bar.html` | Source crystal | `components/source-crystal.css` + SVG | Yes | Yes | Yes | Yes | No | No | `--required` / `--candidate` only |
| `term.html` | Term card + language depth | `components/term-card.css`, `language-depth.css` | Yes | Yes | Yes | Yes | No | No | Relation lattice slot |
| `reference.html` | Term card + language depth | Same | Yes | Yes | Yes | Yes | No | No | Reference layer framing |
| `page.html` | Term card + language depth | Same | Yes | Yes | Yes | Yes | No | No | Generic page frame |
| `home.html` | Term card + language depth | Same | Yes | Yes | Yes | Yes | No | No | Gateway control room |
| `base.html` | Control room shell | `bisulfid-frame.css` | Yes | Yes | Yes | Yes | No | No | `bs-control-room` body class |
| `partials/internal_links.html` | Disclaimer typography | Token inheritance | Yes | Yes | Yes | Yes | No | No | Empty state, not QA placeholder |
| `partials/footer.html` | Unchanged structure | Token inheritance | Yes | Yes | Yes | Yes | No | No | Governance language preserved |

## Integration sample routes

| route_id | Output path | DS linked | Raw MD | QA placeholder |
|----------|-------------|-----------|--------|----------------|
| `home` | `_integration_sample/index.html` | Yes | No | No |
| `what_is_bisulfid` | `_integration_sample/what-is-bisulfid/index.html` | Yes | No | No |
| `de_core_mos2` | `_integration_sample/de/terminology/molybdenum-disulfide/index.html` | Yes | No | No |
| `en_index_disambiguation_map` | `_integration_sample/reference/disambiguation-map/index.html` | Yes | No | No |
| `bisulfide_hydrosulfide_sulfide` | `_integration_sample/bisulfide-hydrosulfide-sulfide/index.html` | Yes | No | No |
| `sources` | `_integration_sample/sources/index.html` | Yes | No | No |
| `corpus_methodology_overview` | `_integration_sample/reference/corpus-methodology/index.html` | Yes | No | No |
