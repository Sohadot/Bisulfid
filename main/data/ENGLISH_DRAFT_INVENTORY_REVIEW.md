# English Draft Inventory Review

## Why This Sprint Exists

Sprint 4G documented a **broader planned-route and content inventory gap**: many `language: en` routes in `main/data/routes.json` pointed at `content_file` paths under `main/content/en/pages/` that did not exist. Sprint 4H closed the gap for `german_english_chemical_terms` only. Sprint 4I is a **diagnostic inventory review**: it maps every English planned route to its draft file state, lists on-disk English content assets, checks for orphan files and frontmatter alignment (read-only), summarizes internal link dependencies on **missing-draft** routes, and proposes a **non-publication** priority order for future draft-creation sprints. No routes, links, or content files were edited.

## Files Reviewed

- `main/data/routes.json`
- `main/data/internal_links.json`
- `main/content/en/pages/`
- `main/content/en/fragments/`
- `main/content/en/term-records/`
- `main/content/en/README.md`
- `main/data/GERMAN_ENGLISH_TERMS_DRAFT_PATH_REVIEW.md`
- `main/data/GERMAN_ENGLISH_TERMS_DRAFT_CREATION_REPORT.md`
- `DECISION_LOG.md`

## Summary Counts

| Metric | Count |
| --- | --- |
| Total English routes (`language: en` in `routes.json`) | 21 |
| English routes with existing `content_file` on disk | 7 |
| English routes with **missing** `content_file` | 14 |

`link_group_refs` below counts how many entries in `internal_links.json` `link_groups` list this `route_id` inside `intended_links` (including self-references). It approximates **planned internal link demand** on that route, not live traffic.

## Route-to-content table (all English routes)

| route_id | path | content_file | status | indexable | in_sitemap | file exists | draft state | required_internal_links | required_claim_groups | risk_level | link_group_refs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| home | `/` | `main/content/en/pages/index.md` | planned | false | false | yes | draft-backed | `[]` | `[]` | low | 3 |
| what_is_sulfur | `/what-is-sulfur/` | `main/content/en/pages/what-is-sulfur.md` | planned | false | false | no | missing draft | `[]` | `["science_claims"]` | low | 3 |
| sulfur_compounds | `/sulfur-compounds/` | `main/content/en/pages/sulfur-compounds.md` | planned | false | false | no | missing draft | `[]` | `["terminology_claims","science_claims"]` | low | 2 |
| sulfur_uses | `/sulfur-uses/` | `main/content/en/pages/sulfur-uses.md` | planned | false | false | no | missing draft | `[]` | `["science_claims","industry_claims"]` | low | 2 |
| what_is_bisulfid | `/what-is-bisulfid/` | `main/content/en/pages/what-is-bisulfid.md` | planned | false | false | yes | draft-backed | `[]` | `["terminology_claims","science_claims"]` | medium | 11 |
| bisulfid_vs_bisulfide | `/bisulfid-vs-bisulfide/` | `main/content/en/pages/bisulfid-vs-bisulfide.md` | planned | false | false | yes | draft-backed | `[]` | `["terminology_claims"]` | medium | 5 |
| sulfid_vs_sulfide | `/sulfid-vs-sulfide/` | `main/content/en/pages/sulfid-vs-sulfide.md` | planned | false | false | yes | draft-backed | `[]` | `["terminology_claims"]` | low | 4 |
| bisulfide_hydrosulfide_sulfide | `/bisulfide-hydrosulfide-sulfide/` | `main/content/en/pages/bisulfide-hydrosulfide-sulfide.md` | planned | false | false | no | missing draft | `[]` | `["terminology_claims","science_claims"]` | medium | 4 |
| sodium_bisulfide | `/sodium-bisulfide/` | `main/content/en/pages/sodium-bisulfide.md` | planned | false | false | no | missing draft | `[]` | `["terminology_claims","science_claims","industry_claims","safety_claims"]` | high | 7 |
| disulfide_bonds | `/disulfide-bonds/` | `main/content/en/pages/disulfide-bonds.md` | planned | false | false | no | missing draft | `[]` | `["science_claims"]` | low | 4 |
| industrial_sulfur_systems | `/industrial-sulfur-systems/` | `main/content/en/pages/industrial-sulfur-systems.md` | planned | false | false | no | missing draft | `[]` | `["industry_claims"]` | medium | 6 |
| sulfur_safety_context | `/sulfur-safety-context/` | `main/content/en/pages/sulfur-safety-context.md` | planned | false | false | no | missing draft | `[]` | `["safety_claims"]` | high | 5 |
| hydrogen_sulfide_risk | `/hydrogen-sulfide-risk/` | `main/content/en/pages/hydrogen-sulfide-risk.md` | planned | false | false | no | missing draft | `[]` | `["safety_claims"]` | high | 2 |
| sds_and_sulfur_terms | `/sds-and-sulfur-terms/` | `main/content/en/pages/sds-and-sulfur-terms.md` | planned | false | false | no | missing draft | `[]` | `["safety_claims","terminology_claims"]` | high | 2 |
| protein_disulfide_structure | `/protein-disulfide-structure/` | `main/content/en/pages/protein-disulfide-structure.md` | planned | false | false | no | missing draft | `[]` | `["science_claims"]` | low | 2 |
| molybdenum_disulfide | `/molybdenum-disulfide/` | `main/content/en/pages/molybdenum-disulfide.md` | planned | false | false | no | missing draft | `[]` | `["science_claims","industry_claims"]` | low | 3 |
| german_english_chemical_terms | `/german-english-chemical-terms/` | `main/content/en/pages/german-english-chemical-terms.md` | planned | false | false | yes | draft-backed | `[]` | `["terminology_claims"]` | low | 3 |
| glossary | `/glossary/` | `main/content/en/pages/glossary.md` | planned | false | false | no | missing draft | `[]` | `["terminology_claims"]` | low | 18 |
| sources | `/sources/` | `main/content/en/pages/sources.md` | planned | false | false | yes | draft-backed | `[]` | `[]` | low | 14 |
| newsletter | `/newsletter/` | `main/content/en/pages/newsletter.md` | planned | false | false | no | missing draft | `[]` | `[]` | low | 0 |
| acquire | `/acquire/` | `main/content/en/pages/acquire.md` | planned | false | false | yes | draft-backed | `[]` | `["acquisition_claims"]` | low | 4 |

## Existing draft inventory (`main/content/en/pages/`)

Files present (excluding `.gitkeep`):

- `index.md` (route `home`)
- `what-is-bisulfid.md`
- `bisulfid-vs-bisulfide.md`
- `sulfid-vs-sulfide.md`
- `german-english-chemical-terms.md`
- `sources.md`
- `acquire.md`

## Missing draft inventory (`content_file` absent)

These routes remain **missing draft** (path expected by `routes.json`):

- `what_is_sulfur` - `main/content/en/pages/what-is-sulfur.md`
- `sulfur_compounds` - `main/content/en/pages/sulfur-compounds.md`
- `sulfur_uses` - `main/content/en/pages/sulfur-uses.md`
- `bisulfide_hydrosulfide_sulfide` - `main/content/en/pages/bisulfide-hydrosulfide-sulfide.md`
- `sodium_bisulfide` - `main/content/en/pages/sodium-bisulfide.md`
- `disulfide_bonds` - `main/content/en/pages/disulfide-bonds.md`
- `industrial_sulfur_systems` - `main/content/en/pages/industrial-sulfur-systems.md`
- `sulfur_safety_context` - `main/content/en/pages/sulfur-safety-context.md`
- `hydrogen_sulfide_risk` - `main/content/en/pages/hydrogen-sulfide-risk.md`
- `sds_and_sulfur_terms` - `main/content/en/pages/sds-and-sulfur-terms.md`
- `protein_disulfide_structure` - `main/content/en/pages/protein-disulfide-structure.md`
- `molybdenum_disulfide` - `main/content/en/pages/molybdenum-disulfide.md`
- `glossary` - `main/content/en/pages/glossary.md`
- `newsletter` - `main/content/en/pages/newsletter.md`

## Other English content paths

- `main/content/en/fragments/` - only `.gitkeep` (no fragment drafts).
- `main/content/en/term-records/` - only `.gitkeep` (no term-record files).

## Orphan draft check

Every `.md` under `main/content/en/pages/` matches **exactly one** `content_file` basename declared for an English route in `routes.json`. No orphan page draft was found (no extra `.md` files without a corresponding route `content_file`).

## Route / content filename mismatch check

For all **existing** drafts, the on-disk filename matches the final segment of the route `content_file` path in `routes.json`. No filename/path mismatch was identified.

## Frontmatter `route_id` check (read-only)

For each existing `.md` draft, the YAML `route_id` matches the `route_id` of the route that owns that `content_file`:

| file | frontmatter `route_id` | Expected `route_id` | Match |
| --- | --- | --- | --- |
| `index.md` | `home` | `home` | yes |
| `what-is-bisulfid.md` | `what_is_bisulfid` | `what_is_bisulfid` | yes |
| `bisulfid-vs-bisulfide.md` | `bisulfid_vs_bisulfide` | `bisulfid_vs_bisulfide` | yes |
| `sulfid-vs-sulfide.md` | `sulfid_vs_sulfide` | `sulfid_vs_sulfide` | yes |
| `german-english-chemical-terms.md` | `german_english_chemical_terms` | `german_english_chemical_terms` | yes |
| `sources.md` | `sources` | `sources` | yes |
| `acquire.md` | `acquire` | `acquire` | yes |

**Note (cosmetic only):** `german-english-chemical-terms.md` uses a slimmer frontmatter block (no `source_status` / `claim_status` / `generated`) than some older drafts. This is not a `route_id` mismatch.

## Internal link dependency notes (`internal_links.json`)

- References are **`route_id` strings** inside `intended_links` only (no raw URLs in this registry).
- All `link_groups` entries remain `status: planned`. Nothing in this sprint changed the file.
- **Missing-draft routes** are still targeted by many planned groups. Examples by target (which `from_route_id` lists that target):

| Missing target `route_id` | `from_route_id` groups that reference it |
| --- | --- |
| `glossary` | `home`, `what_is_sulfur`, `sulfur_compounds`, `sulfur_uses`, `what_is_bisulfid`, `bisulfid_vs_bisulfide`, `sulfid_vs_sulfide`, `bisulfide_hydrosulfide_sulfide`, `sodium_bisulfide`, `disulfide_bonds`, `industrial_sulfur_systems`, `sulfur_safety_context`, `hydrogen_sulfide_risk`, `sds_and_sulfur_terms`, `protein_disulfide_structure`, `molybdenum_disulfide`, `german_english_chemical_terms`, `sources` |
| `sodium_bisulfide` | `sulfur_compounds`, `sulfur_uses`, `bisulfide_hydrosulfide_sulfide`, `industrial_sulfur_systems`, `sulfur_safety_context`, `hydrogen_sulfide_risk`, `glossary` |
| `industrial_sulfur_systems` | `home`, `sulfur_uses`, `sodium_bisulfide`, `disulfide_bonds`, `molybdenum_disulfide`, `acquire` |
| `sulfur_safety_context` | `bisulfide_hydrosulfide_sulfide`, `sodium_bisulfide`, `industrial_sulfur_systems`, `hydrogen_sulfide_risk`, `sds_and_sulfur_terms` |
| `bisulfide_hydrosulfide_sulfide` | `what_is_bisulfid`, `bisulfid_vs_bisulfide`, `sodium_bisulfide`, `glossary` |
| `disulfide_bonds` | `industrial_sulfur_systems`, `protein_disulfide_structure`, `molybdenum_disulfide`, `glossary` |
| `what_is_sulfur` | `home`, `sulfur_compounds`, `sulfur_uses` |
| `molybdenum_disulfide` | `disulfide_bonds`, `protein_disulfide_structure`, `glossary` |
| `sulfur_compounds` | `what_is_sulfur`, `sulfur_uses` |
| `sulfur_uses` | `what_is_sulfur`, `sulfur_compounds` |
| `hydrogen_sulfide_risk` | `sulfur_safety_context`, `sds_and_sulfur_terms` |
| `sds_and_sulfur_terms` | `sulfur_safety_context`, `hydrogen_sulfide_risk` |
| `protein_disulfide_structure` | `disulfide_bonds`, `molybdenum_disulfide` |
| `newsletter` | *(no other group lists `newsletter` as an intended target)* |

## Priority order for future draft creation (non-public sprints only)

This ordering supports **planned internal link density** and the **terminology spine**. It does **not** recommend publication or route activation.

**High**

1. `glossary` - central terminology hub; `link_group_refs` 18; bridges many layers.
2. `sodium_bisulfide` - high `link_group_refs` (7) and sits between terminology, industrial, and safety clusters; `risk_level` high in `routes.json` (future drafts must stay within safety doctrine).
3. `industrial_sulfur_systems` - six referring groups; connects gateway and acquisition-facing copy.
4. `bisulfide_hydrosulfide_sulfide` - terminology disambiguation; tied to core `what_is_bisulfid` / DE-EN pages.
5. `what_is_sulfur` - public-gateway entry; three referring groups including `home`.

**Medium**

6. `sulfur_compounds`, `sulfur_uses` - gateway pair; two referring groups each.
7. `sulfur_safety_context` - five referring groups; **high** route risk; must remain awareness-only per route notes.
8. `disulfide_bonds`, `molybdenum_disulfide`, `protein_disulfide_structure` - materials / biochemistry cluster (four, three, two referring groups respectively).
9. `sds_and_sulfur_terms`, `hydrogen_sulfide_risk` - safety layer; **high** route risk; two referring groups each.

**Low**

10. `newsletter` - zero incoming planned internal links; utility layer; lowest graph pressure.

## Why no routes were published

This sprint is **read-only inventory**. No `routes.json` edits, no `status` changes, and no Quality Gate actions were performed.

## Why no content pages were created

Draft creation is explicitly **out of scope** for Sprint 4I; the goal is mapping and prioritization only.

## Why no content pages were modified

All content inspection used **read-only** file reads. No draft text or frontmatter was changed, and no `[SOURCE REQUIRED]` markers were touched.

## Why no claims were approved

Claim registries remain **inactive** by design, and this sprint does not run claim review or source-locking workflows.

## Why `[SOURCE REQUIRED]` markers remain

Existing drafts still contain pending factual work; this sprint does not remove markers or satisfy claims.

## Publication readiness conclusion: not ready for publication

The English layer has **14** planned routes without `content_file` bodies, including `glossary` and other high-link targets. All routes remain `planned` with `indexable: false` and `in_sitemap: false`. The site remains **not publication-ready**.

## Recommended next sprint

A **narrow English draft-creation sprint** for the next **high-priority** missing route (recommended: `glossary` or `what_is_sulfur` first for gateway coherence, or `glossary` first for graph relief), governed under the same constraints as Sprint 4H: non-public frontmatter, no route JSON edits, no claim approval, no marker removal, no publication. Alternatively, a **safety-governed** draft sprint **only** after explicit authorization because `sodium_bisulfide` and safety routes carry `risk_level: high` in `routes.json`.

## Sprint 4I change scope

**Created:** `main/data/ENGLISH_DRAFT_INVENTORY_REVIEW.md` (this report)

**Updated:** `DECISION_LOG.md`

**Not modified:** `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, all English content drafts, templates, root `README.md`, package and CI configs, and generated HTML.
