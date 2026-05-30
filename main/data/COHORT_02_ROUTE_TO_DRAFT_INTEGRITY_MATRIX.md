# COHORT_02 — Route-to-Draft Integrity Matrix

**Sprint:** 6L  
**Date:** 2026-05-30  
**Scope:** Integrity audit of 902 COHORT_02 registered routes vs draft files

---

## Verdict

**PASS** — **902/902** COHORT_02 routes have valid, unique, existing draft bindings.

---

## Aggregate integrity matrix

| Dimension | Count | Draft exists | Planned | noindex | Mapping unique |
| --- | ---: | :---: | :---: | :---: | :---: |
| **COHORT_02 total** | **902** | ✓ | ✓ | ✓ | ✓ |
| PT_TERM_CANONICAL | 300 | ✓ | ✓ | ✓ | ✓ |
| PT_AUDIENCE_EXPLAINER | 250 | ✓ | ✓ | ✓ | ✓ |
| PT_COMPOUND_ENTITY | 128 | ✓ | ✓ | ✓ | ✓ |
| PT_AI_READABLE | 100 | ✓ | ✓ | ✓ | ✓ |
| PT_CHILD_SAFE_EDU | 76 | ✓ | ✓ | ✓ | ✓ |
| PT_DIFFERENCE_COMPARISON | 48 | ✓ | ✓ | ✓ | ✓ |

**Legend:** ✓ = pass for all rows in dimension.

---

## Binding rules verified (902/902)

| Rule | Result |
| --- | --- |
| `route_id` unique in registry | ✓ |
| `content_file` unique in registry | ✓ |
| `content_file` = `main/content/en/pages/cohort-02-terminology/{route_id}.md` | ✓ |
| Draft file exists on disk | ✓ (902/902) |
| Draft front matter `route_id` matches registry | ✓ (Sprint 6J verified) |
| Manifest unit alignment | ✓ (902/902) |
| Filename slug = `route_id` (underscore-aligned) | ✓ |
| L1 slug validator pass under cohort-02 prefix | ✓ |

---

## Registry field matrix (902/902)

| Field | Expected | Actual |
| --- | --- | ---: |
| status | planned | 902 |
| indexable | false | 902 |
| in_sitemap | false | 902 |
| in_navigation | false | 902 |
| source_required | true | 902 |
| required_claim_groups | terminology_claims | 902 |
| layer | terminology_system | 902 |
| language | en | 902 |

---

## Internal-link binding

| Metric | Value |
| --- | ---: |
| Routes with 2 required_internal_links | 854 |
| Routes with 3 required_internal_links | 48 (comparison cluster) |
| Broken link targets | **0** |
| Planning `glossary` token in registry links | **0** (correctly excluded) |
| Foundation bridge `en_foundation_sovereign_intro` | present where required |

---

## Comparison route path integrity (48 routes)

All **48** PT_DIFFERENCE_COMPARISON routes have **unique** disambiguated paths (Sprint 6K):

**Pattern:** `/en/terminology/compare/{pair}/{ref}/{aud}/`

| Pair example | Paths registered | Collisions |
| --- | ---: | ---: |
| bisulfid-vs-bisulfide | 4 | 0 |
| All 12 comparison pairs | 48 total | 0 |

---

## Sample binding verification

| route_id | path (truncated) | draft exists |
| --- | --- | :---: |
| `cohort02_en_bisulfid_term_chem_acad` | `/en/terminology/bisulfid/term/chem/acad/` | ✓ |
| `cohort02_en_sulfide_term_chem_know` | `/en/terminology/sulfide/term/chem/know/` | ✓ |
| `cohort02_en_bisulfid_vs_bisulfide_chem_ling` | `/en/terminology/compare/bisulfid-vs-bisulfide/chem/ling/` | ✓ |

Full listing: `main/data/COHORT_02_FULL_DRAFT_MANIFEST.json`.

---

## Corrections required

**None.** COHORT_02 route-to-draft integrity confirmed without registry or content modifications.

---

*Sprint 6L — COHORT_02 Route-to-Draft Integrity Matrix*
