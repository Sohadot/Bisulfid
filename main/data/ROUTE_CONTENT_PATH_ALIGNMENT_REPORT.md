# Route Content Path Alignment Report — Sprint 2C

**Date:** 2026-05-15  
**Sprint:** 2C — Route Content Path Alignment  
**Branch:** claude/sprint-2c-route-content-path-alignment  
**File modified:** `main/data/routes.json`

---

## Issue Found

All 21 `content_file` fields in `routes.json` pointed to `main/content/en/*.md` (root of the language directory). The actual English draft pages created in Sprint 2 and corrected in Sprint 2B reside in `main/content/en/pages/*.md` (the `pages/` subdirectory established in Sprint 0C).

Additionally, the `home` route pointed to `main/content/en/home.md`, but the actual homepage draft is `main/content/en/pages/index.md`.

---

## Corrected Path Pattern

| Was | Now |
|-----|-----|
| `main/content/en/<slug>.md` | `main/content/en/pages/<slug>.md` |
| `main/content/en/home.md` (home route only) | `main/content/en/pages/index.md` |

No other fields in `routes.json` were modified. All routes remain `status: planned`, `indexable: false`, `in_sitemap: false`.

---

## Six Confirmed Existing Draft Paths

The following six routes now point to content files that exist in the repository:

| route_id | content_file | File exists |
|----------|-------------|-------------|
| `home` | `main/content/en/pages/index.md` | YES |
| `what_is_bisulfid` | `main/content/en/pages/what-is-bisulfid.md` | YES |
| `bisulfid_vs_bisulfide` | `main/content/en/pages/bisulfid-vs-bisulfide.md` | YES |
| `sulfid_vs_sulfide` | `main/content/en/pages/sulfid-vs-sulfide.md` | YES |
| `sources` | `main/content/en/pages/sources.md` | YES |
| `acquire` | `main/content/en/pages/acquire.md` | YES |

---

## Remaining Planned-Only Routes

The following 15 routes have their `content_file` paths corrected to the `pages/` structure but do not yet have content files. They remain `status: planned` and are non-public.

| route_id | content_file (updated) | File exists |
|----------|----------------------|-------------|
| `what_is_sulfur` | `main/content/en/pages/what-is-sulfur.md` | NO — planned |
| `sulfur_compounds` | `main/content/en/pages/sulfur-compounds.md` | NO — planned |
| `sulfur_uses` | `main/content/en/pages/sulfur-uses.md` | NO — planned |
| `bisulfide_hydrosulfide_sulfide` | `main/content/en/pages/bisulfide-hydrosulfide-sulfide.md` | NO — planned |
| `sodium_bisulfide` | `main/content/en/pages/sodium-bisulfide.md` | NO — planned |
| `disulfide_bonds` | `main/content/en/pages/disulfide-bonds.md` | NO — planned |
| `industrial_sulfur_systems` | `main/content/en/pages/industrial-sulfur-systems.md` | NO — planned |
| `sulfur_safety_context` | `main/content/en/pages/sulfur-safety-context.md` | NO — planned |
| `hydrogen_sulfide_risk` | `main/content/en/pages/hydrogen-sulfide-risk.md` | NO — planned |
| `sds_and_sulfur_terms` | `main/content/en/pages/sds-and-sulfur-terms.md` | NO — planned |
| `protein_disulfide_structure` | `main/content/en/pages/protein-disulfide-structure.md` | NO — planned |
| `molybdenum_disulfide` | `main/content/en/pages/molybdenum-disulfide.md` | NO — planned |
| `german_english_chemical_terms` | `main/content/en/pages/german-english-chemical-terms.md` | NO — planned |
| `glossary` | `main/content/en/pages/glossary.md` | NO — planned |
| `newsletter` | `main/content/en/pages/newsletter.md` | NO — planned |

---

## Governance State: Unchanged

- All 21 routes: `status: planned` — UNCHANGED
- All 21 routes: `indexable: false` — UNCHANGED
- All 21 routes: `in_sitemap: false` — UNCHANGED
- All 21 routes: `in_navigation: false` — UNCHANGED
- No route published.
- `sitemap_policy.json` — NOT MODIFIED
- `navigation.json` — NOT MODIFIED
- `source_registry.json` — NOT MODIFIED
- Claim files — NOT MODIFIED
- Content draft pages — NOT MODIFIED
- Root `README.md` — NOT MODIFIED
- No new content pages created.
- No generated HTML route pages created.

---

## Publication Status

**Unchanged. Non-public.**

No route has been published. No route is indexable. No route is in the sitemap. This sprint corrected only the `content_file` path values so the build system can locate the existing draft files. It did not change any publication, governance, or indexation state.
