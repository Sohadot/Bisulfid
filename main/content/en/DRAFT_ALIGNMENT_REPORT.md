# Draft Alignment Report — Sprint 2B

**Date:** 2026-05-15  
**Sprint:** 2B — English Draft Alignment  
**Branch:** claude/sprint-2b-english-draft-alignment  
**Status:** Review complete. No route is ready for publication.

---

## Reviewed Files

| File | Route ID (Before) | Route ID (After) |
|------|-------------------|------------------|
| `main/content/en/pages/index.md` | `en-home` | `home` |
| `main/content/en/pages/what-is-bisulfid.md` | `en-what-is-bisulfid` | `what_is_bisulfid` |
| `main/content/en/pages/bisulfid-vs-bisulfide.md` | `en-bisulfid-vs-bisulfide` | `bisulfid_vs_bisulfide` |
| `main/content/en/pages/sulfid-vs-sulfide.md` | `en-sulfid-vs-sulfide` | `sulfid_vs_sulfide` |
| `main/content/en/pages/sources.md` | `en-sources` | `sources` |
| `main/content/en/pages/acquire.md` | `en-acquire` | `acquire` |
| `main/content/en/README.md` | — | No changes required |

---

## Route ID Alignment

**Issue found:** All six draft pages used an `en-` prefix and hyphen-separated route IDs (e.g., `en-home`, `en-what-is-bisulfid`). The actual `routes.json` uses underscore-separated IDs without the language prefix (e.g., `home`, `what_is_bisulfid`).

**Resolution:** Frontmatter `route_id` corrected in all six files.

| Page | Was | Now | routes.json Match |
|------|-----|-----|-------------------|
| index.md | `en-home` | `home` | PASS |
| what-is-bisulfid.md | `en-what-is-bisulfid` | `what_is_bisulfid` | PASS |
| bisulfid-vs-bisulfide.md | `en-bisulfid-vs-bisulfide` | `bisulfid_vs_bisulfide` | PASS |
| sulfid-vs-sulfide.md | `en-sulfid-vs-sulfide` | `sulfid_vs_sulfide` | PASS |
| sources.md | `en-sources` | `sources` | PASS |
| acquire.md | `en-acquire` | `acquire` | PASS |

**Infrastructure note:** `routes.json` `content_file` fields point to `main/content/en/*.md` (e.g., `main/content/en/home.md`), while the actual files reside in `main/content/en/pages/*.md`. This path discrepancy is noted for resolution in a future sprint. `routes.json` was not modified in this sprint per sprint rules.

---

## Frontmatter Alignment

All six files verified after correction:

| Field | Required Value | Result |
|-------|---------------|--------|
| `language` | `en` | PASS — all files |
| `status` | `draft` | PASS — all files |
| `publication_status` | `non_public` | PASS — all files |
| `source_status` | `pending_source_review` | PASS — all files |
| `claim_status` | `no_claims_approved` | PASS — all files |
| `indexable` | `false` | PASS — all files |
| `in_sitemap` | `false` | PASS — all files |
| `generated` | `false` | PASS — all files |

---

## Internal Link Intent Alignment

**Issues found:**
1. All planned link references used the wrong route ID format (`en-*` with hyphens instead of `route_id` format with underscores).
2. Several pages were missing links that `internal_links.json` plans for them.
3. `index.md` referenced `en-term-bisulfid`, which does not exist in `routes.json`.
4. `sources.md` and `acquire.md` had no planned link sections.

**Resolutions:**
- All inline route ID references corrected to use `routes.json` format.
- `en-term-bisulfid` removed from `index.md` (no corresponding route in `routes.json`).
- Missing links per `internal_links.json` added to each page.
- Planned link sections added to `sources.md` and `acquire.md`.

**Per-page alignment with `internal_links.json`:**

| Page (route_id) | Links added in this sprint |
|---|---|
| `home` | Added `what_is_sulfur`, `industrial_sulfur_systems`; removed nonexistent `en-term-bisulfid` |
| `what_is_bisulfid` | Added `bisulfide_hydrosulfide_sulfide`, `german_english_chemical_terms` |
| `bisulfid_vs_bisulfide` | Added `german_english_chemical_terms`, `bisulfide_hydrosulfide_sulfide` |
| `sulfid_vs_sulfide` | Added `what_is_bisulfid`, `glossary`, `sources` |
| `sources` | Added full planned link section: `what_is_bisulfid`, `glossary`, `home` |
| `acquire` | Added full planned link section: `home`, `what_is_bisulfid`, `industrial_sulfur_systems` |

---

## Ontology Alignment

Reviewed against `main/data/ontology/sulfur_terms.json` (center_node: `bisulfid`).

| Check | Result |
|-------|--------|
| Bisulfid treated as center node | PASS — stated explicitly in `what-is-bisulfid.md` |
| Bisulfide treated as English-form boundary | PASS — all pages use correct framing |
| Sulfid/Sulfide as spelling boundary | PASS — `sulfid-vs-sulfide.md` documents the pattern correctly |
| Bisulfite used only as disambiguation, never as part of bisulfide meaning system | PASS — explicit disambiguation in `what-is-bisulfid.md`; no conflation found in any file |
| No bisulfite data presented as bisulfide data | PASS |

No ontology corrections were required.

---

## Source Discipline Verification

| Check | Result |
|-------|--------|
| Nomenclature claims marked [SOURCE REQUIRED] | PASS |
| Chemical identity claims marked [SOURCE REQUIRED] | PASS |
| Ion assignments marked [SOURCE REQUIRED] | PASS |
| Industrial relevance claims marked [SOURCE REQUIRED] | PASS |
| Oxide/Oxid and Chloride/Chlorid examples marked [SOURCE REQUIRED] | PASS |
| No fake citations | PASS |
| No external links presented as verified sources | PASS |
| No numerical market claims | PASS |
| No company acquisition targeting | PASS |
| No medical or therapeutic claims | PASS |
| No handling instructions | PASS |
| No exposure thresholds or dosage advice | PASS |
| No [SOURCE REQUIRED] markers removed | PASS |

---

## Acquisition Discipline Verification (`acquire.md`)

| Check | Result |
|-------|--------|
| Not framed as a cheap "domain for sale" page | PASS |
| No specific target companies named | PASS |
| No price included | PASS |
| No urgency language | PASS |
| Acquisition framed as selective strategic inquiry | PASS |
| Contact email `agent@sohadot.com` included | PASS |
| Draft and non-public status maintained | PASS |

---

## Source Discipline Page Verification (`sources.md`)

| Check | Result |
|-------|--------|
| "No source entry = no published claim" stated | PASS |
| Source registry not populated — stated | PASS |
| AI summaries blocked | PASS |
| Bisulfite-as-bisulfide data blocked | PASS |
| Unsourced market statistics blocked | PASS |
| Safety thresholds as advice blocked | PASS |
| Medical claims blocked | PASS |
| Handling instructions blocked | PASS |

---

## Issues Found and Resolved

| Issue | Severity | Resolution |
|-------|----------|------------|
| All 6 pages: incorrect `route_id` format (`en-*` prefix with hyphens) | High — prevents build system from matching pages to routes | Fixed |
| All inline route references: wrong ID format | Medium — would break future link resolution | Fixed |
| `index.md`: referenced `en-term-bisulfid` — no such route in routes.json | Medium — orphaned reference | Removed |
| Missing planned links per `internal_links.json` | Low — governance alignment | Added |
| No planned link sections in `sources.md` and `acquire.md` | Low — governance alignment | Added |
| `routes.json` `content_file` paths point to `main/content/en/*.md` but files are in `main/content/en/pages/*.md` | Medium — infrastructure discrepancy | Noted; not fixed (routes.json not modified per sprint rules) |

---

## Remaining Source-Required Areas

The following claims remain marked [SOURCE REQUIRED] and must be source-locked before any page can be published:

- German/English chemical nomenclature conventions for the -id/-ide suffix pattern
- Formal nomenclature authority citations (IUPAC, DIN, or equivalent)
- Ion assignments for bisulfide (HS⁻) and bisulfite (HSO₃⁻)
- Industrial relevance of bisulfid across chemical, energy, and industrial sectors
- Chemical and industrial relevance claims in `bisulfid-vs-bisulfide.md`
- Oxide/Oxid and Chloride/Chlorid as examples of the -id/-ide pattern
- Any reference to IUPAC or DIN standards governing this suffix pattern

---

## Infrastructure Note

`routes.json` `content_file` fields use `main/content/en/*.md` paths (without `pages/` subdirectory), while Sprint 2 created files in `main/content/en/pages/*.md`. This discrepancy must be resolved in a future sprint — either by moving the content files or updating `routes.json`. It was not resolved in this sprint because `routes.json` modification was not permitted.

---

## Publication Status

**Not ready for publication.**

All six draft pages remain `status: draft` and `publication_status: non_public`. No route may be published until:
1. All [SOURCE REQUIRED] markers are resolved with entries in `main/data/sources/source_registry.json`.
2. All 11 Quality Gate conditions in `doctrine/QUALITY_GATE.md` are met.
3. The `content_file` path discrepancy between `routes.json` and actual file locations is resolved.
4. `routes.json` route status is updated to `published` by an authorised sprint.
