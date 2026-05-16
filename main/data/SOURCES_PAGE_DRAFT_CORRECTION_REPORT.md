# Sources Page Draft Correction Report — Sprint 3D

**Date:** 2026-05-16  
**Branch:** claude/sprint-3d-sources-page-draft-correction  
**Governed by:** doctrine/SOURCE_POLICY.md

---

## Why This Correction Was Necessary

Sprint 3 (seeding 8 candidate sources) and Sprint 3B (adding a 9th candidate source for the bisulfid center node) populated `main/data/sources/source_registry.json` with real seeded entries. Sprint 3C’s `SOURCE_CLAIM_ALIGNMENT_REPORT.md` explicitly flagged the following statement in `main/content/en/pages/sources.md` as stale and factually inaccurate:

> “The source registry is not populated yet.”

This statement was written during Sprint 2 when no sources had been seeded. After Sprint 3 and Sprint 3B, it was factually incorrect. Leaving it in the non-public draft creates an internal inconsistency between the governed draft page and the actual state of the repository. Sprint 3D corrects this.

---

## Stale Statement Corrected

**Original wording (replaced):**

> The source registry is not populated yet.
>
> `main/data/sources/source_registry.json` exists as a governed structure but contains no source entries. Draft content across the site contains `[SOURCE REQUIRED]` markers where claims await source-locking.
>
> Draft content is not public evidence. The existence of a draft page does not mean the claims on that page are verified, approved, or ready for publication.

**Replacement wording:**

> The source registry now contains seeded candidate sources. These sources are not final publication locks. They remain governed by SOURCE_POLICY.md, claim review, and Quality Gate enforcement. No claim is approved for publication merely because a candidate source exists.
>
> `main/data/sources/source_registry.json` currently holds seeded candidate entries across authoritative dictionaries, a chemical nomenclature standard, government scientific databases, and one industry publication. All entries carry `status: seeded` and `source_lock_status: candidate`. None are final.
>
> Candidate source entries are not the same as approved claims. Source registry presence does not make a page publishable. Claims remain pending_review unless explicitly approved. [SOURCE REQUIRED] markers remain until source-locking review. Draft content remains non-public.

---

## New Wording Summary

The corrected “Current Registry Status” section now:

1. Accurately reflects that seeded candidate sources exist in the registry.
2. States explicitly that candidate sources are not final publication locks.
3. Distinguishes candidate source entries from approved claims.
4. States that source registry presence does not make a page publishable.
5. States that all claims remain `pending_review` until explicitly approved.
6. States that `[SOURCE REQUIRED]` markers remain until source-locking review.
7. States that draft content remains non-public regardless of candidate source presence.

---

## Files Modified

| File | Change |
|---|---|
| `main/content/en/pages/sources.md` | “Current Registry Status” section rewritten to reflect seeded candidate sources and distinguish them from approved claims |

---

## Files Not Modified

| File | Status |
|---|---|
| `main/data/sources/source_registry.json` | Not modified |
| `main/data/claims/terminology_claims.json` | Not modified |
| `main/data/claims/science_claims.json` | Not modified |
| `main/data/ontology/sulfur_terms.json` | Not modified |
| `main/data/routes.json` | Not modified |
| `main/data/sitemap_policy.json` | Not modified |
| `main/config/navigation.json` | Not modified |
| All other content pages | Not modified |
| Root README.md | Not modified |

---

## Publication Status: Unchanged

| Field | Value |
|---|---|
| status | draft (unchanged) |
| publication_status | non_public (unchanged) |
| indexable | false (unchanged) |
| in_sitemap | false (unchanged) |
| generated | false (unchanged) |

The page remains `status: draft` and `publication_status: non_public`. No route was published. No route status, indexable, or in_sitemap value was changed.

---

## No Claims Approved

No terminology claim, science claim, or any other claim was approved in this sprint. All claims remain `status: pending_review`. Claim registries remain `inactive`. The correction to the sources draft does not constitute or trigger claim approval.

---

## No Routes Changed

No route was published. No route in `routes.json` was modified. No route status, indexable, in_sitemap, or in_navigation value was changed.

---

## No Source Registry Changes

`main/data/sources/source_registry.json` was not modified in this sprint. The sprint corrects a draft page description of the registry; it does not modify the registry itself.

---

## No [SOURCE REQUIRED] Markers Removed

No `[SOURCE REQUIRED]` marker was removed from any content page. The sources.md page does not contain `[SOURCE REQUIRED]` markers — it describes source governance policy rather than making chemistry claims. No other content page was modified.
