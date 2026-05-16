# Terminology Reference Spine Batch 1 Report

## Why This Sprint Exists

Sprint 4I mapped English planned routes to missing drafts and prioritized **`glossary`**, **`sulfur_compounds`**, and **`bisulfide_hydrosulfide_sulfide`** as high-value terminology spine targets. Sprint 4J **establishes batch one** of a **non-public** terminology reference layer: three internal drafts that strengthen governed vocabulary scaffolding for bisulfid.com **without** publishing routes, activating claims, editing registries, or removing **`[SOURCE REQUIRED]`** markers from any file.

## Pre-flight verification (`routes.json`)

Each target was confirmed present, `language: en`, `status: planned`, with the following **`content_file`** paths (unchanged; no invention):

| route_id | content_file |
| --- | --- |
| `glossary` | `main/content/en/pages/glossary.md` |
| `sulfur_compounds` | `main/content/en/pages/sulfur-compounds.md` |
| `bisulfide_hydrosulfide_sulfide` | `main/content/en/pages/bisulfide-hydrosulfide-sulfide.md` |

Prior to creation, none of these files existed on disk, so **no overwrite** conflict occurred.

## Files created

- `main/content/en/pages/glossary.md` - controlled terminology chamber (draft scaffold; ontology alignment deferred).
- `main/content/en/pages/sulfur-compounds.md` - sulfur compound **terminology scope map** (not a textbook survey).
- `main/content/en/pages/bisulfide-hydrosulfide-sulfide.md` - **disambiguation authority draft** for bisulfide / hydrosulfide / sulfide vocabulary roles.

## Frontmatter (all three)

Each file uses:

- `route_id` matching `routes.json`
- `status: draft`
- `publication_status: non_public`
- `indexable: false`
- `in_sitemap: false`
- `language: en`, `locale: en`, `source_language: en`

## Strategic intent

- **Glossary** - defines operating rules for a future governed glossary chamber; references **`sulfur_terms.json`** as the future driver without modifying it.
- **Sulfur compounds** - provides **lanes** for compound-class vocabulary that bridge gateway copy to the terminology system.
- **Bisulfide / hydrosulfide / sulfide** - isolates naming confusion **at the vocabulary layer** and explicitly deflects safety-page responsibilities.

## Why no routes were published

`routes.json` was not modified; all routes remain `planned`. No Quality Gate or publication workflow was executed.

## Why no claims were approved

Claim registries remain **inactive**; `terminology_claims.json` was not modified. Drafts use cautious language and **`[SOURCE REQUIRED]`** instead of assertions.

## Why **`[SOURCE REQUIRED]`** markers remain everywhere

No source-locking sprint ran. This batch adds markers on **new** pages and does **not** remove markers from **other** drafts.

## Registry and link discipline

**Not modified in this sprint:** `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, templates, root `README.md`, packages, workflows, deployment configs, generated HTML.

## Publication readiness

**Not publication-ready.** Three routes now have draft bodies, but source, claim, and Quality Gate work remains outstanding.

## Recommended next sprint

- Continue the spine (`what_is_sulfur` gateway draft and/or `sodium_bisulfide` only under **explicit** authorization given `risk_level: high`), **or**
- A **source-locking** sprint keyed to terminology rows these drafts reference, still without claim approval until registry rules permit.

## Sprint 4J scope summary

**Created:** three English page drafts under exact `routes.json` paths; this report.

**Updated:** `DECISION_LOG.md`.
