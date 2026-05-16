# Core Term Drafts Batch 2 Report

## Why this sprint exists

Sprint 4L was chartered to extend the **non-public terminology reference infrastructure** with a second small batch of **core term drafts** (`bisulfid`, `sulfid`, `hydrosulfide`) aligned with Sprint 4K’s boundary posture: governed term records, not generic chemistry articles, safety guides, or market copy. The sprint assumes each target already has a **`route_id`** and **`content_file`** in `main/data/routes.json` so drafts can be created **without** inventing routes.

## Why this is core term draft creation, not generic page creation

When route records exist, the intended deliverables are **controlled term drafts**: draft notices, **candidate support** language, **`[SOURCE REQUIRED]`** discipline, bisulfite boundaries, explicit **non-publication** status, and deferral of formal authority (DIN, official German IUPAC, teaching PDFs as nomenclature proof). This sprint does **not** publish content, approve claims, or activate registries.

## Sprint 4I inventory basis

Sprint 4I mapped **21** English planned routes: **7** draft-backed on disk at the time, **14** missing `content_file` bodies. That inventory grounded later spine and gateway prioritization.

## Sprint 4K boundary-review basis

Sprint 4K confirmed the first spine (`glossary`, `sulfur_compounds`, `bisulfide_hydrosulfide_sulfide`) stays **non-public reference infrastructure**, preserves bisulfite disambiguation, separates teaching support from formal authority, and keeps claim registries **inactive**. Batch 2 was meant to anchor **individual core labels** (German center-node **Bisulfid**, German lexical **Sulfid**, English **Hydrosulfide**) into the same governance tone **adjacent** to that spine.

## Target route_ids (planned for this sprint)

- `bisulfid`
- `sulfid`
- `hydrosulfide`

## Route existence check (pre-flight)

**Result: targets absent from `routes.json`.**

A full read of `main/data/routes.json` on the sprint branch shows **no** English route entries with `route_id` exactly `bisulfid`, `sulfid`, or `hydrosulfide`. The charter forbids inventing routes or orphan `content_file` paths.

**Nearest existing terminology routes (for alignment context only):**

| Intended core term | Closest existing `route_id` | Declared `content_file` |
| --- | --- | --- |
| Bisulfid (center-node framing) | `what_is_bisulfid` | `main/content/en/pages/what-is-bisulfid.md` *(draft already on disk)* |
| Sulfid vs sulfide boundary | `sulfid_vs_sulfide` | `main/content/en/pages/sulfid-vs-sulfide.md` *(draft already on disk)* |
| Hydrosulfide in triad | `bisulfide_hydrosulfide_sulfide` | `main/content/en/pages/bisulfide-hydrosulfide-sulfide.md` *(draft on disk)* |

No standalone `hydrosulfide` route exists; hydrosulfide language is intentionally grouped under the triad disambiguation draft today.

## Files created

| File | Action |
| --- | --- |
| `main/data/CORE_TERM_DRAFTS_BATCH_2_REPORT.md` | **Created** — this report |
| `main/content/en/pages/bisulfid.md` | **Not created** — no matching route |
| `main/content/en/pages/sulfid.md` | **Not created** — no matching route |
| `main/content/en/pages/hydrosulfide.md` | **Not created** — no matching route |

## Frontmatter status for each draft

**Not applicable** — no new draft pages were added because prerequisite `route_id` / `content_file` records do not exist.

## Why these three routes were prioritized (conceptual)

- **`bisulfid`** —German identity-layer anchor for the asset name and ontology center-node narrative [SOURCE REQUIRED].
- **`sulfid`** —German **-id** lexical lane feeding `sulfid_vs_sulfide` and the glossary chamber without a universal suffix rule as approved fact.
- **`hydrosulfide`** —English label that intersects **bisulfide** and **sulfide** and sustains `bisulfide_hydrosulfide_sulfide` discipline.

Execution of that prioritization **requires** explicit `routes.json` rows (or retargeting batch 2 to existing `route_id` values) in a future routing sprint.

## How each draft would connect to the terminology spine (if routes existed)

- **`bisulfid`** would tighten the **German center-node** record referenced from `glossary`, `sulfur_compounds`, and comparison routes.
- **`sulfid`** would hold a **single-term German lexical record** complementing `sulfid_vs_sulfide` and `german_english_chemical_terms`.
- **`hydrosulfide`** would extend **triad** vocabulary precision for `bisulfide_hydrosulfide_sulfide` and sodium-salt naming boundaries **without** safety or market copy.

## How the batch would support the sovereign reference system (if created)

Same spine principles as 4J/4K: **terminology governance**, **source-locking discipline**, **claim boundary discipline**, DE/EN separation, bisulfite wall, no textbook drift. This report records that **no additional governed bodies** were added in 4L because route prerequisites failed pre-flight.

## Why routes.json was not modified

Doctrine for this sprint: add drafts only where routes already exist. Adding new routes is out of scope for 4L and would mix routing architecture with content drafting.

## Why internal_links.json was not modified

Planned graph records stay unchanged; no new routable pages were introduced.

## Why no claim was approved

Claim registries remain **inactive**; no draft pages were added and no workflow was run.

## Why [SOURCE REQUIRED] markers remain

No spine or core-term bodies were written in this sprint; existing pages retain their markers unchanged.

## Why no routes were published

No route metadata or publication flags were changed; **`status: planned`**, **`indexable: false`**, **`in_sitemap: false`** remain for all routes.

## Remaining missing draft routes after this sprint

Unchanged versus pre-sprint: **11** English routes still lack `content_file` bodies on disk (same set as after Sprint 4J; Sprint 4K was review-only).

Typical remaining `route_id` list (verify against current `routes.json` and disk):

- `what_is_sulfur`
- `sulfur_uses`
- `sodium_bisulfide`
- `disulfide_bonds`
- `industrial_sulfur_systems`
- `sulfur_safety_context`
- `hydrogen_sulfide_risk`
- `sds_and_sulfur_terms`
- `protein_disulfide_structure`
- `molybdenum_disulfide`
- `newsletter`

## Remaining missing draft count after this sprint

**11.**

If the three target routes had existed and three drafts had been added successfully, the modeled count would have been **8** (14 baseline missing from Sprint 4I, minus **3** from Sprint 4J, minus **3** from Sprint 4L). **That decrement did not occur** because Sprint 4L did not create those files.

## Remaining blockers before publication

- Missing English `content_file` bodies for the **11** routes above (until addressed).
- Terminology claims, source-locking, Quality Gate, and ontology alignment for any public wording.
- High **`risk_level`** routes require separate authorized drafting discipline.

## Recommended next sprint

1. **Routing / architecture sprint (prerequisite):** Add `route_id` rows with exact `content_file` paths for `bisulfid`, `sulfid`, and/or `hydrosulfide` **if** the product intent is standalone pages — **or** formally retarget Batch 2 to expand existing `what_is_bisulfid`, `sulfid_vs_sulfide`, and `bisulfide_hydrosulfide_sulfide` drafts instead of new slugs.
2. **Draft-creation sprint:** Re-run Batch 2 once `content_file` paths are authoritative in `routes.json`.
3. **Gateway draft:** `what_is_sulfur` or `sulfur_uses` from the remaining-11 list (low **risk_level**), per 4K suggestion.

## Historical accounting (for continuity)

- Sprint 4I found **14** missing English drafts (baseline).
- Sprint 4J created **3** terminology spine drafts (`glossary`, `sulfur_compounds`, `bisulfide_hydrosulfide_sulfide`).
- Sprint 4K reviewed spine boundaries (no new bodies).
- Sprint 4L was **intended to create** **3** additional core term drafts (`bisulfid`, `sulfid`, `hydrosulfide`). **No such draft files were added** because those `route_id` values are **absent** from `routes.json`; had they existed and all three drafts been created successfully, modeled remaining missing count would have been **8** after 4L (14 baseline minus 3 from 4J minus 3 from 4L).

## Publication posture

**New drafts:** none added in this sprint.

**This sprint does not recommend publication.** All routes remain **planned** and non-indexable; no Batch 2 pages entered the corpus.

## Sprint 4L file change scope

**Created:** `main/data/CORE_TERM_DRAFTS_BATCH_2_REPORT.md`.

**Updated:** `DECISION_LOG.md`.

**Not modified:** `routes.json`, `internal_links.json`, sitemap/navigation/hreflang/translation JSON, `main/data/sources/source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, all existing content pages, templates, root `README.md`, packages, workflows, generated HTML.
