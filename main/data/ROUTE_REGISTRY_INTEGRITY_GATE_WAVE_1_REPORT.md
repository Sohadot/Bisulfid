# Route Registry Integrity Gate — Wave 1 Report

**Sprint:** 6L  
**Date:** 2026-05-30  
**Scope:** Full audit of `main/data/routes.json` after COHORT_02 registration (Sprint 6K)  
**Posture:** Integrity validation only — no route publication, no content generation

---

## Verdict

**PASS** — all **1,043** route records audited; COHORT_02 route-to-draft mapping confirmed; no duplicate collisions; no publication/indexation leakage; `routes.json` unchanged.

---

## Registry scale

| Metric | Value |
| --- | ---: |
| Total routes audited | **1,043** |
| Pre-COHORT routes | **126** |
| COHORT_01 foundation routes | **15** |
| COHORT_02 terminology routes | **902** |
| Draft-backed routes | **985** |
| Missing draft files (pre-existing) | **58** |
| Published routes | **0** |
| `production_can_safely_proceed` | **no** |

---

## Integrity summary

| Check | Result |
| --- | --- |
| Duplicate `route_id` | **0** |
| Duplicate `route_path` | **0** |
| Duplicate `content_file` | **0** |
| COHORT_02 count | **902/902** |
| COHORT_02 draft files exist | **902/902** |
| COHORT_02 manifest alignment | **902/902** |
| Broken internal-link targets | **0** |
| `indexable: true` | **0** |
| `in_sitemap: true` | **0** |
| `in_navigation: true` | **0** |
| `status: published` | **0** |
| `status != planned` | **0** |
| Slug validator issues | **0** |
| `routes.json` corrections required | **0** |

---

## Cohort breakdown

| Cohort | Routes | Draft-backed | Layer | Notes |
| --- | ---: | ---: | --- | --- |
| Pre-COHORT (Wave 1 + legacy) | 126 | 68 | mixed | 58 planned routes without content (pre-existing) |
| COHORT_01 foundation | 15 | 15 | foundation/methodology | Sprint 6F registration |
| COHORT_02 terminology | 902 | 902 | terminology_system | Sprint 6K registration |

---

## COHORT_02 registration posture (902/902)

| Field | Value |
| --- | --- |
| status | `planned` |
| indexable | `false` |
| in_sitemap | `false` |
| in_navigation | `false` |
| source_required | `true` |
| required_claim_groups | `["terminology_claims"]` |
| content_file pattern | `main/content/en/pages/cohort-02-terminology/{route_id}.md` |
| Sprint 6K notes marker | 902/902 |

---

## Pre-existing missing drafts (not COHORT_02)

**58** routes reference content files that do not yet exist on disk. These are **pre-COHORT** planned routes (EN + DE Wave 1 inventory) — unchanged by Sprint 6K and **not a COHORT_02 integrity defect**.

Examples: `sulfur_uses`, `de_term_sulfat`, `de_core_pbs`. Full list documented in duplicate/path audit report.

---

## Validator scope confirmation (Sprint 6K alignment)

`validate_corpus_routes_l1.py` contains a **single** scoped exception:

- Prefix: `main/content/en/pages/cohort-02-terminology/`
- Slug charset: `[a-z0-9_\-]*` (route_id-aligned underscore filenames)
- All other content paths: unchanged hyphen-only slug rule
- No publication, indexation, sitemap, or navigation logic modified

---

## Explicit non-actions (verified)

- `routes.json` not modified in Sprint 6L
- No content pages created
- No public HTML generated
- No route publication activation
- No sitemap/navigation/indexation activation
- No validator weakening beyond confirmed narrow slug scope

---

## Recommended next step

After merge: resume large-scale corpus production — likely **multilingual / reference-layer wave** toward 14,000-page launch target, subject to source/claim gates and `production_can_safely_proceed: no`.

---

*Sprint 6L — Route Registry Integrity Gate Wave 1 Report*
