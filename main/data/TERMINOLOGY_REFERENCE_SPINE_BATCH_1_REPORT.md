# Terminology Reference Spine Batch 1 Report

## Why this sprint exists

Sprint 4I mapped English planned routes to missing drafts and prioritized **`glossary`**, **`sulfur_compounds`**, and **`bisulfide_hydrosulfide_sulfide`** as high-value terminology spine targets.

## Why this is reference spine creation, not generic page creation

Sprint 4J **does not** add generic marketing or chemistry-blog pages. It adds **internal reference infrastructure**: a **controlled terminology chamber** (`glossary`), a **sulfur terminology scope map** (`sulfur_compounds`), and a **triad disambiguation authority draft** (`bisulfide_hydrosulfide_sulfide`) so bisulfid.com can grow as a **governed terminology asset** rather than undifferentiated educational copy. All three remain **`status: draft`**, **`publication_status: non_public`**, **not indexable**, **not in sitemap**, and **not publication-ready**.

A **completion patch** after the initial batch then expanded term coverage, scope-map sections, bisulfite boundaries, and inventory accounting in this report - still without publishing routes or approving claims.

## Sprint 4I inventory basis

Sprint 4I reported **21** English planned routes, **7** with existing drafts, and **14** routes whose `content_file` was **missing** on disk.

## Target route_ids (batch one)

- `glossary`
- `sulfur_compounds`
- `bisulfide_hydrosulfide_sulfide`

## Route existence check

Each target was confirmed in `routes.json` as `language: en`, `status: planned`, with **`content_file`** paths:

| route_id | content_file |
| --- | --- |
| `glossary` | `main/content/en/pages/glossary.md` |
| `sulfur_compounds` | `main/content/en/pages/sulfur-compounds.md` |
| `bisulfide_hydrosulfide_sulfide` | `main/content/en/pages/bisulfide-hydrosulfide-sulfide.md` |

## Files created (initial batch) and patched

- `main/content/en/pages/glossary.md` - controlled terminology chamber (expanded via completion patch).
- `main/content/en/pages/sulfur-compounds.md` - sulfur terminology scope map (expanded via completion patch).
- `main/content/en/pages/bisulfide-hydrosulfide-sulfide.md` - triad disambiguation draft (completion patch: bisulfite boundary, dedicated non-claim and source sections).

## Frontmatter (all three drafts)

Each file uses:

- `route_id` matching `routes.json`
- `status: draft`
- `publication_status: non_public`
- `indexable: false`
- `in_sitemap: false`
- `language: en`, `locale: en`, `source_language: en`

## Why these three routes were prioritized

Per Sprint 4I, **`glossary`** carried the highest planned internal-link demand among missing drafts, with **`sodium_bisulfide`**, **`industrial_sulfur_systems`**, and related clusters depending on shared terminology spine coherence. Establishing **`glossary`**, **`sulfur_compounds`**, and **`bisulfide_hydrosulfide_sulfide`** first anchors the **controlled chamber**, the **scope map**, and the **highest-friction ion-label triad** before expanding gateway or industrial drafts.

## How each draft supports the sovereign reference system

- **Glossary** - holds **draft-level controlled entries** and boundary discipline for core DE/EN and sulfur-anion vocabulary **without** pretending ontology rows are verified.
- **Sulfur compounds** - maps **terminology groups** (sulfide/sulfid, bisulfide/hydrosulfide, disulfide/disulfid, pattern context, teaching vs authority) for internal alignment.
- **Bisulfide / hydrosulfide / sulfide** - isolates **label confusion** and preserves a **separate bisulfite boundary** so oxyanion wording cannot collapse into sulfide-anion lanes.

## Missing draft arithmetic (post Sprint 4J)

- Sprint 4I found **14** missing English `content_file` drafts.
- Sprint 4J created **3** of those missing drafts (`glossary`, `sulfur_compounds`, `bisulfide_hydrosulfide_sulfide`).
- **Remaining missing draft count after Sprint 4J: 11.**

## Remaining missing drafts (11)

Listed from Sprint 4I `content_file` expectations (paths per `routes.json` at time of inventory; **routes were not modified** in Sprint 4J):

| route_id | Expected `content_file` |
| --- | --- |
| `what_is_sulfur` | `main/content/en/pages/what-is-sulfur.md` |
| `sulfur_uses` | `main/content/en/pages/sulfur-uses.md` |
| `sodium_bisulfide` | `main/content/en/pages/sodium-bisulfide.md` |
| `disulfide_bonds` | `main/content/en/pages/disulfide-bonds.md` |
| `industrial_sulfur_systems` | `main/content/en/pages/industrial-sulfur-systems.md` |
| `sulfur_safety_context` | `main/content/en/pages/sulfur-safety-context.md` |
| `hydrogen_sulfide_risk` | `main/content/en/pages/hydrogen-sulfide-risk.md` |
| `sds_and_sulfur_terms` | `main/content/en/pages/sds-and-sulfur-terms.md` |
| `protein_disulfide_structure` | `main/content/en/pages/protein-disulfide-structure.md` |
| `molybdenum_disulfide` | `main/content/en/pages/molybdenum-disulfide.md` |
| `newsletter` | `main/content/en/pages/newsletter.md` |

## Why `routes.json` was not modified

Route metadata was already correct; Sprint 4J and this patch add **draft bodies** only. Keeping `routes.json` unchanged avoids accidental publication semantics.

## Why `internal_links.json` was not modified

Planned internal link groups remain **planned**; adding draft files does not activate links or change graph records in this sprint.

## Why no claim was approved

Claim registries remain **inactive**; `terminology_claims.json` was **not** modified. Drafts use **candidate** and **`[SOURCE REQUIRED]`** language exclusively.

## Why `[SOURCE REQUIRED]` markers remain

Source-locking sprints have not run; drafts **add** markers where public-grade support is absent and **do not** strip markers from other pages.

## Why no routes were published

All routes remain **`planned`** with **`indexable: false`** and **`in_sitemap: false`**. No Quality Gate publication step was executed.

## Remaining blockers before publication (summary)

- **11** English routes still lack `content_file` bodies (table above).
- Terminology claims, source registry alignment, and Quality Gate work remain outstanding for spine routes and the rest of the English layer.
- **`sulfur_terms.json`** was not modified; ontology alignment for a public glossary is still a future sprint.
- High **`risk_level`** routes (for example safety-layer pages) require separate authorized drafting discipline.

**This sprint does not recommend publication.** All three spine drafts remain **non-public** and **not publication-ready**.

## Recommended next sprint

- Narrow English draft creation for the next gateway or industrial target from the remaining-11 table (with explicit constraints for high-risk routes), **or**
- Terminology **source-locking** keyed to spine tables - still without claim approval until registry rules permit.

## Registry discipline (unchanged)

**Not modified in Sprint 4J or this patch:** `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, templates, root `README.md`, packages, workflows, deployment configs, generated HTML.

## Change log

- **Initial batch:** three draft files, this report skeleton, `DECISION_LOG.md` entry.
- **Completion patch:** expanded three drafts for acceptance completeness; expanded this report with 11-missing accounting and explicit spine-vs-generic framing; appended corrective `DECISION_LOG` entry.
