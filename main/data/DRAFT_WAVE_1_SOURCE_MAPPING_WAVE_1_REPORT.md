# Draft Wave 1 — Source Mapping Wave 1 Report

**Sprint:** 5M  
**Date:** 2026-05-27  
**Branch:** `claude/sprint-5m-draft-wave-1-source-mapping-wave-1`

---

## Why this sprint exists

Sprint **5L** classified **50** Sprint **5J** drafts and identified **12** as `ready_for_source_mapping`. Sprint **5M** executes the first **source-mapping wave** for that cohort—defining source categories, gaps, and claim posture **without** registering sources, editing drafts, or implying source-lock completion.

---

## Why source mapping comes before draft wave 2

| If skipped | Consequence |
| --- | --- |
| Another **50** drafts without mapping | **100+** pages with unresolved authority lines |
| Source registration without mapping plan | Ad hoc registry rows without marker alignment |
| Draft wave 2 first | Governance debt compounds; L1 warnings become noise |

Sprint **5L** and **5K** both recommended mapping before the next production wave.

---

## Relationship to Sprint 5L

Sprint **5L** produced requirement matrices and cohort A list. Sprint **5M** consumes that classification:

- **Maps:** 12 cohort-A drafts (`DRAFT_WAVE_1_SOURCE_MAPPING_MATRIX.md`)
- **Prepares:** 20 medium-risk drafts for claim-boundary work (`DRAFT_WAVE_1_MEDIUM_RISK_CLAIM_BOUNDARY_PREP.md`)
- **Does not change:** 5L classifications or draft content

---

## Relationship to Sprint 5K automation runtime

Pre-flight: `python scripts/corpus_validation_runtime_l1.py` — **PASS** (2026-05-27).

L1 confirms structural discipline. Sprint **5M** adds **source-mapping governance artifacts** that L1 does not generate: category gaps, marker-to-source plans, and claim-boundary prep.

---

## Relationship to 500-page sovereign launch threshold

| Metric | Value |
| --- | ---: |
| Launch threshold | **500** governed pages |
| Routes registered | **126** |
| Draft-backed routes | **68** |
| Cohort A mapped this sprint | **12** |
| Publication-ready after mapping | **0** |

Source mapping moves **12** drafts toward future source-locking; it does **not** advance publication eligibility.

---

## Files reviewed

- `main/data/routes.json`
- `main/data/DRAFT_WAVE_1_SOURCE_CLAIM_BOUNDARY_REVIEW.md`
- `main/data/DRAFT_WAVE_1_SOURCE_REQUIREMENT_MATRIX.md`
- `main/data/DRAFT_WAVE_1_CLAIM_RISK_MATRIX.md`
- `main/data/DRAFT_WAVE_1_PUBLICATION_BLOCKER_MATRIX.md`
- `main/data/DRAFT_WAVE_1_NEXT_ACTIONS.md`
- `main/data/CORPUS_L1_VALIDATION_REPORT.md`
- `main/data/CORPUS_AUTOMATION_NEXT_WAVE_RECOMMENDATIONS.md`
- `main/data/CORPUS_AUTOMATION_VALIDATION_REQUIREMENTS.md`
- `main/data/CORPUS_LAUNCH_THRESHOLD.md`
- `main/data/FIVE_HUNDRED_PAGE_SOVEREIGN_LAUNCH_PROGRAM.md`
- `doctrine/SOURCE_POLICY.md`
- `main/data/sources/source_registry.json` (read-only)
- `main/data/claims/terminology_claims.json` (read-only)
- All **12** cohort-A draft content files (read-only)
- All **20** medium-risk draft content files (read-only reference)

---

## Pre-flight confirmation

| Check | Result |
| --- | --- |
| Cohort A drafts identified | **12** from Sprint 5L |
| Draft files exist | **12/12** |
| Match `routes.json` | **12/12** |
| `draft` / `non_public` / non-indexable | **12/12** |
| Medium-risk drafts for prep | **20/20** |
| L1 runtime | **PASS** |
| Content modified | **0** |
| Sources registered | **0** |
| Claims approved | **0** |

---

## Mapped drafts (12)

```
sulfid
sulfur_element_term_record
carbonyl_sulfide_terms
copper_sulfides_language
de_glossary
de_bridge_en_de_suffix
de_german_english_chemical_terms
de_core_biogenic_lang
de_core_cas
de_core_cus
de_core_fes
de_core_mos2
```

---

## Language split (12 mapped drafts)

| Language | Count |
| --- | ---: |
| English (`en`) | **4** |
| German (`de`) | **8** |

---

## Route category / layer split (12 mapped drafts)

| Category | Count |
| --- | ---: |
| Core terminology (`terminology_system`) | **12** |

All cohort-A drafts are low-risk terminology records or DE localized mirrors—no industrial, compliance, or disambiguation routes in this wave.

---

## Source mapping methodology

1. Import cohort-A list from Sprint **5L** boundary review.
2. Read Sprint **5L** source requirement level per draft.
3. Read each draft frontmatter and marker placement (read-only).
4. Review `source_registry.json` categories and seeded rows (registry **inactive**; read-only).
5. Assign Sprint **5M** source mapping category per draft.
6. Document source gap, discovery need, and formal authority need.
7. Assign claim category; confirm **no** registration or approval actions now.
8. Prepare medium-risk claim-boundary notes separately (no source mapping for those **20**).

---

## Source category principles

- **Mapping ≠ registration** — this sprint defines needs; it does not add registry rows.
- **Candidate ≠ approved** — seeded registry rows remain `candidate`; mapping references categories only.
- **Doctrine-first** — internal governance pages may remain doctrine-linked until external discovery sprints.
- **DE authority separate** — German lexical pages require DE authority paths, not EN dictionary substitution.
- **No raw URLs in mapping docs** — describe source **types**, not live links.

---

## Claim boundary principles

- Claim registries **inactive**; **claim approval allowed now: always no**.
- Cohort A drafts: mostly `terminology_claim_candidate_later` or `multilingual_boundary_claim_candidate_later`.
- Medium-risk drafts: claim-boundary prep **before** source mapping.
- No content language may imply claim approval or source-lock completion.

---

## What source mapping means in this sprint

- Audit-grade **plans** linking draft markers to source **categories** and **gaps**
- Identification of **existing registry categories** that may apply later
- Flagging **external source discovery** needs
- Claim-category assignment for future registry review

---

## What source mapping does not mean in this sprint

| Not in scope | Reason |
| --- | --- |
| Adding `source_registry.json` rows | Registry modification forbidden |
| Removing `[SOURCE REQUIRED]` markers | Source-locking not complete |
| Stating source-lock complete | False authority |
| Publication readiness | Quality Gate not met |
| Claim approval | Registries inactive |
| Content edits | Mapping sprint only |

---

## Overall findings

| Finding | Detail |
| --- | --- |
| Drafts mapped | **12** |
| Source registration performed | **0** |
| All mapped drafts need external discovery later | **12/12** (`yes`) |
| Formal authority needed later | **11/12** (`de_core_biogenic_lang` exception: dictionary tier only) |
| Publication-ready | **0** |
| Medium-risk prep completed | **20** drafts |
| Source mapping deferred for medium-risk | **20/20** (`source mapping allowed now: no`) |

---

## Drafts closest to future source registration

After a future **source registration sprint** (not this sprint), first candidates for **verified row proposals**:

1. `sulfur_element_term_record` — element tier; lowest drift
2. `de_core_biogenic_lang` — environmental vocabulary; no formal nomenclature lock required first
3. `copper_sulfides_language` / `de_core_cus` — paired EN/DE mineral naming
4. `sulfid` — DE lexical spine (requires DE authority discovery first)

---

## Drafts needing external source discovery later

**All 12** cohort-A drafts flag `source discovery needed later: yes`. No draft can satisfy markers from doctrine or seeded candidates alone.

---

## Drafts needing formal authority later

**11** of **12** (all except `de_core_biogenic_lang` at dictionary-only tier). Nomenclature and DE lexical pages require IUPAC, dictionary, or bilingual authority candidates before registration.

---

## Why no source entries were added

`source_registry.json` modification is explicitly forbidden. Registry remains **inactive**. Mapping defines **future** registration candidates only.

---

## Why no claims were approved

Claim registries inactive; sprint is mapping/preparation only. **Zero** `status: approved`.

---

## Why no content pages were modified

Editing drafts would conflate mapping with production. Markers remain untouched.

---

## Why `[SOURCE REQUIRED]` markers remain

Markers indicate unresolved authority. Mapping identifies **what** source type is needed; it does not **satisfy** markers.

---

## Why no routes were published

All **126** routes remain `planned`, non-indexable, out of sitemap/navigation. **500-page** program authorization not granted.

---

## Unresolved source gaps

| Gap | Affected drafts |
| --- | ---: |
| DE lexical authority not mapped to registry rows | **8** DE drafts |
| EN specialist compound naming unmapped | **3** EN drafts |
| Bilingual crosswalk row-level mapping | **2** DE bridge/table drafts |
| Element-tier database mapping | **1** EN draft |
| Biogenic/environmental reference tier | **1** DE draft |

---

## Unresolved claim gaps

| Gap | Affected |
| --- | ---: |
| Terminology claim boundaries undefined for cohort A | **12** (future candidates only) |
| Medium-risk claim boundaries not registered | **20** |
| Claim registries inactive | all |
| Internal link wiring | all draft-backed routes |

---

## Recommended next sprint

**Sprint 5N-A — Source registration proposal wave 1** (report-only candidate rows for **4–6** lowest-gap cohort-A drafts, still **no** registry modification unless explicitly chartered) **and** **Sprint 5N-B — Claim boundary registration report** for **20** medium-risk drafts. **Defer draft production wave 2** until 5N-A/5N-B complete and L1 passes.

See `DRAFT_WAVE_1_SOURCE_MAPPING_NEXT_ACTIONS.md`.

---

*Sprint 5M — Draft Wave 1 Source Mapping Wave 1 Report*
