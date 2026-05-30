# COHORT_02 — Route-to-Draft Mapping (Wave 1)

**Sprint:** 6K  
**Date:** 2026-05-30  
**Registry:** `main/data/routes.json` (1,043 routes)

---

## Mapping summary

| Metric | Value |
| --- | ---: |
| COHORT_02 routes registered | **902** |
| Content path pattern | `main/content/en/pages/cohort-02-terminology/{route_id}.md` |
| Draft files exist on disk | **902/902** |
| route_id ↔ content_file unique | **902/902** |
| Front matter route_id alignment | **902/902** (Sprint 6J verified) |

Full unit listing: `main/data/COHORT_02_FULL_DRAFT_MANIFEST.json` (902 entries).

---

## Sample mapping (first entity: bisulfid)

| route_id | path | content_file | page_type_id |
| --- | --- | --- | --- |
| `cohort02_en_bisulfid_term_chem_acad` | `/en/terminology/bisulfid/term/chem/acad/` | `.../cohort02_en_bisulfid_term_chem_acad.md` | PT_TERM_CANONICAL |
| `cohort02_en_bisulfid_term_chem_know` | `/en/terminology/bisulfid/term/chem/know/` | `.../cohort02_en_bisulfid_term_chem_know.md` | PT_TERM_CANONICAL |
| `cohort02_en_bisulfid_aud_chem_know` | `/en/terminology/bisulfid/aud/chem/know/` | `.../cohort02_en_bisulfid_aud_chem_know.md` | PT_AUDIENCE_EXPLAINER |
| `cohort02_en_bisulfid_term_ai_tech` | `/en/terminology/bisulfid/term/ai/tech/` | `.../cohort02_en_bisulfid_term_ai_tech.md` | PT_AI_READABLE |
| `cohort02_en_bisulfid_vs_bisulfide_chem_ling` | `/en/terminology/compare/bisulfid-vs-bisulfide/chem/ling/` | `.../cohort02_en_bisulfid_vs_bisulfide_chem_ling.md` | PT_DIFFERENCE_COMPARISON |

---

## Comparison route path mapping (disambiguated)

| route_id | registered path |
| --- | --- |
| `cohort02_en_bisulfid_vs_bisulfide_chem_ling` | `/en/terminology/compare/bisulfid-vs-bisulfide/chem/ling/` |
| `cohort02_en_bisulfid_vs_bisulfide_res_res` | `/en/terminology/compare/bisulfid-vs-bisulfide/res/res/` |
| `cohort02_en_bisulfid_vs_bisulfide_stu_edu` | `/en/terminology/compare/bisulfid-vs-bisulfide/stu/edu/` |
| `cohort02_en_bisulfid_vs_bisulfide_ai_tech` | `/en/terminology/compare/bisulfid-vs-bisulfide/ai/tech/` |

Same disambiguation pattern applied to all **12** comparison pairs (**48** routes).

---

## Front matter alignment

Each draft front matter `route_id` matches its registry record:

- `status: draft` in content ↔ `status: planned` in registry (draft-backed discipline)
- `indexable: false` in both
- `in_sitemap: false` in both
- `in_navigation: false` in both
- `publication_status: non_public` in content
- `language` / `locale` / `source_language`: **en**

No draft file modifications required in Sprint 6K.

---

## Required internal links (pattern)

All COHORT_02 routes include at minimum:

- `en_foundation_sovereign_intro` (foundation bridge)
- Entity term hub `cohort02_en_{entity}_term_chem_know` where applicable
- Cohort cross-links per inventory `internal_link_targets`

Planning `glossary` token excluded from registry `required_internal_links` (not a registered route_id).

---

## Binding verification

| Check | Result |
| --- | --- |
| Unique route_id | ✓ (902 new; 0 duplicates) |
| Unique path | ✓ (1,043 total) |
| Unique content_file | ✓ |
| All COHORT_02 content files exist | ✓ (902/902) |
| All link targets registered or foundation | ✓ |
| No duplicate with existing 141 routes | ✓ |
| Existing 141 routes unchanged | ✓ |

---

*Sprint 6K — COHORT_02 Route-to-Draft Mapping Wave 1*
