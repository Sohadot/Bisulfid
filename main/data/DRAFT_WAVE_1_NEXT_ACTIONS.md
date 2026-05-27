# Draft Wave 1 — Next Actions

**Sprint:** 5L  
**Date:** 2026-05-27  
**Context:** 50 Sprint 5J drafts classified; L1 runtime **PASS**; 0 publication-ready drafts

---

## Recommended next sprint

**Sprint 5M — Source mapping wave 1** for the **12** lowest-risk terminology drafts (cohort A in `DRAFT_WAVE_1_SOURCE_CLAIM_BOUNDARY_REVIEW.md`).

Run `python scripts/corpus_validation_runtime_l1.py` before and after 5M. Archive results in an updated validation report.

---

## Should Sprint 5M be source mapping for selected low-risk drafts?

**Yes — primary recommendation.**

| Parameter | Value |
| --- | --- |
| Batch size | **10–15** drafts (start with **12** cohort A) |
| Target routes | `sulfid`, `sulfur_element_term_record`, `carbonyl_sulfide_terms`, `copper_sulfides_language`, `de_glossary`, `de_bridge_en_de_suffix`, `de_german_english_chemical_terms`, `de_core_biogenic_lang`, `de_core_cas`, `de_core_cus`, `de_core_fes`, `de_core_mos2` |
| Scope | Propose source registry **candidate rows** and marker-to-source mapping report only |
| Forbidden | Marker removal, registry activation, claim approval, content edits without charter |

---

## Should Sprint 5M be claim boundary registration?

**Partially — parallel report-only track for medium-risk drafts.**

| Parameter | Value |
| --- | --- |
| Batch size | **15–20** drafts (medium-risk disambiguation, compliance, industrial language) |
| Output | Claim boundary registration **report** mapping drafts to future `terminology_claims` / `industry_claims` boundaries |
| Forbidden | Registry activation, `status: approved`, content modification |

Claim boundary registration can run **in parallel** with source-mapping cohort A but must **not** replace source mapping for terminology drafts.

---

## Should Sprint 5M be draft wave 2?

**No — defer to Sprint 5N or later.**

Adding **40–60** new drafts before resolving wave-1 source/claim classifications would grow governance debt from **50** to **90–110** classified-but-unmapped pages. Sprint **5K/5L** explicitly prioritized boundary review before the next production wave.

Draft wave 2 should resume only after:

1. Source-mapping cohort A complete (10–15 drafts mapped as candidates).
2. Claim boundary report filed for medium-risk cohort.
3. L1 runtime **PASS**.
4. No new blocking drift in industrial/compliance drafts.

---

## Why governance debt must be reduced before another 50-page wave

| Current debt | Count |
| --- | ---: |
| Unresolved `[SOURCE REQUIRED]` on wave-1 drafts | **50** pages |
| Drafts needing claim boundary before lock | **20** |
| Blocked/reframe drafts | **3** |
| Routes without any draft | **58** |

A second **50**-draft wave doubles review surface area before the first wave is source-classified. Automation (L1) catches structural failures but not authority satisfaction.

---

## Recommended batch sizes (post-5L)

| Workstream | Batch size | Sprint slot |
| --- | --- | --- |
| Source mapping | **10–15** drafts | 5M |
| Claim boundary registration (report) | **15–20** drafts | 5M (parallel) |
| Content structure hardening | **4** doctrine drafts | 5O |
| Formal authority source lock | **6** nomenclature drafts | 5P |
| Blocked draft reframe review | **3** drafts | Dedicated review |
| Draft production wave 2 | **40–60** drafts | 5N+ (after 5M) |
| Route registration wave 2 | **80–120** routes | After draft wave 2 stabilizes |

---

## Recommended order of operations

1. **5M-A** — Source mapping cohort A (**12** terminology drafts).
2. **5M-B** — Claim boundary registration report (medium-risk **20** drafts).
3. **5M validation** — L1 runtime PASS; update validation report.
4. **5N** — Draft production wave 2 (**40–60** routes still missing drafts).
5. **5O** — Source mapping cohort B (disambiguation + multilingual bridge).
6. **5P** — Internal-link wiring wave 1 (cluster-scoped).
7. **5Q** — Route registration wave 2 toward 500-page floor.

---

## Drafts closest to source mapping (cohort A — 12)

| route_id | Rationale |
| --- | --- |
| `sulfid` | Low terminology control; DE lexical record |
| `sulfur_element_term_record` | Element record; low drift |
| `carbonyl_sulfide_terms` | Specialist naming; medium-low risk |
| `copper_sulfides_language` | Mineral vocabulary; EN anchor |
| `de_glossary` | DE chamber; dictionary tier |
| `de_bridge_en_de_suffix` | Morphological bridge |
| `de_german_english_chemical_terms` | Bilingual table |
| `de_core_biogenic_lang` | Environmental vocabulary |
| `de_core_cas` | Localized salt naming |
| `de_core_cus` | Localized mineral naming |
| `de_core_fes` | Localized iron sulfides |
| `de_core_mos2` | Specialist compound naming |

---

## Drafts to defer

| route_id | Reason |
| --- | --- |
| `en_gov_hreflang_policy` | hreflang not active |
| `en_index_disambiguation_map` | Spine incomplete; links unwired |
| `en_index_multilingual_map` | Multilingual layers deferred |
| `en_index_terminology_spine` | Index depends on future drafts |
| `de_home` | Gateway; not publication candidate |

---

## Drafts needing formal authority before progress (6)

`bisulfid`, `hydrosulfide`, `sulfide_anion_term_record`, `sulfate_terminology`, `de_what_is_bisulfid`, `de_bridge_iupac_de`

Require IUPAC or formal nomenclature authority candidates before source-mapping proceeds.

---

## Drafts needing multilingual governance before progress

DE bridge and mirror routes: `de_bisulfid_vs_bisulfide`, `de_sulfid_vs_sulfide`, `de_bisulfide_hydrosulfide_sulfide`, `de_what_is_bisulfid`, `translator_playbook_bisulfide_family`, plus `en_gov_hreflang_policy`.

Coordinate EN source-lock with DE mirror mapping; no independent DE authority claims.

---

## Drafts blocked until reframe (3)

`carbon_disulfide_terms`, `en_dis_carbon_disulfide_bisulfide`, `economic_document_language_sulfur`

Do not include in source-mapping batches until boundary reframe is human-approved.

---

## Path toward 500 governed pages without weakening quality

1. **Classify before scale** — 5L complete; repeat after each draft wave.
2. **Map sources in small batches** — 10–15 pages per source-mapping sprint.
3. **Register claim boundaries before approval** — report-only until registry activation sprint.
4. **Alternate production and review** — draft wave → L1 → source/claim sprint → next draft wave.
5. **Keep publication locked** — no `indexable`, no sitemap, no HTML until 500-page program authorization.
6. **Use L1 as merge gate** — run runtime after every wave; block on FAIL.

At current cadence (~50 drafts + ~100 routes per cycle), reaching **500** governed pages requires **~8–10** more production waves **plus** parallel source/claim/link workstreams—quality preserved by batch discipline, not speed.

---

*Sprint 5L — Draft Wave 1 Next Actions*
