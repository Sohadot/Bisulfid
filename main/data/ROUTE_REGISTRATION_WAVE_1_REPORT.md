# Route Registration Wave 1 — Report

**Sprint:** 5I-B  
**Date:** 2026-05-27  
**Branch:** `claude/sprint-5i-b-route-registration-wave-1`

---

## Why this sprint exists

Sprint **5I-B** registers the **first large wave** of low-risk planned routes toward the **500-page sovereign launch threshold**. The sprint adds **route records only** under the automation control doctrine established in Sprint **5I-A**, without creating content pages, publishing routes, or approving claims.

---

## Relationship to the 500-page launch threshold

| Metric | Value |
| --- | ---: |
| Minimum launch threshold (Sprint 5H) | **500** governed pages |
| Routes registered before this sprint | **26** |
| Routes added in wave 1 | **100** |
| Routes registered after this sprint | **126** |
| Remaining registration toward 500 | **374** |

Wave 1 covers ~**20%** of the registration gap (100 / 474 pre-wave gap). Additional registration waves (80–120 routes each) are required before draft production can scale to the full cohort.

---

## Relationship to the automation control layer

This sprint executes **Stage S1 — Route registration** per `CORPUS_AUTOMATION_CONTROL_LAYER.md` and `CORPUS_AUTOMATION_WAVE_PROTOCOL.md`:

- Wave size: **100 routes** (within 80–120 band)
- Validation gate: **L0** (`validate_route_registry_l0.py`)
- Publication lock: **held** — all routes remain `planned`, non-indexable, out of sitemap and navigation
- Claim lock: **held** — no claim approval; registries remain inactive
- Content lock: **held** — no draft bodies created

---

## Files modified by Sprint 5I-B

Sprint **5I-B intentionally modified** the route registry:

| File | Change |
| --- | --- |
| `main/data/routes.json` | **Modified** — 100 new **planned** route records added |

**Registry outcome:**

- **100** new planned route records were added to `routes.json`.
- Route count changed from **26** to **126**.
- **No** content pages were created in this sprint.
- **No** routes were published; all new records remain `status: planned`, non-indexable, and out of sitemap/navigation.

No other registry, content, workflow, or dependency files were modified in Sprint 5I-B.

---

## Files reviewed

- `main/data/CORPUS_ROUTE_BLUEPRINT_LAUNCH_COHORT.md`
- `main/data/LAUNCH_COHORT_BLUEPRINT_QUALITY_REVIEW.md`
- `main/data/LAUNCH_COHORT_REFINEMENT_RECOMMENDATIONS.md`
- `main/data/LAUNCH_COHORT_IMPLEMENTATION_BATCH_1.md`
- `main/data/ROUTE_IMPLEMENTATION_READINESS_MATRIX.md`
- `main/data/FIVE_HUNDRED_PAGE_SOVEREIGN_LAUNCH_PROGRAM.md`
- `main/data/CORPUS_PRODUCTION_WAVE_MODEL.md`
- `main/data/CORPUS_LAUNCH_THRESHOLD.md`
- `main/data/CORPUS_AUTOMATION_CONTROL_LAYER.md`
- `main/data/CORPUS_AUTOMATION_MANIFEST.md`
- `main/data/CORPUS_AUTOMATION_WAVE_PROTOCOL.md`
- `main/data/CORPUS_AUTOMATION_VALIDATION_REQUIREMENTS.md`
- `main/data/routes.json`
- `DECISION_LOG.md`

---

## Route selection method

1. Parsed blueprint table rows (`proposed_route_id`, path, language, category, risk, eligibility, priority).
2. Excluded existing 26 `route_id` values, safety/utility/acquisition categories, `deferred_high_risk_review`, high claim risk, ar/zh/ja languages, and forbidden market/procurement/medical/handling concepts.
3. Sorted by priority (P0 → P3) and language (EN structural spine first within equal priority, then DE boundary layer).
4. Selected top **100** eligible concepts.
5. Deduplicated blueprint duplicate `de_term_mercaptan`; replaced with `sulfate_terminology` to maintain count.

---

## Route counts

| Metric | Count |
| --- | ---: |
| Existing routes before sprint | **26** |
| New routes added | **100** |
| Total routes after sprint | **126** |

---

## Selected route categories

See `ROUTE_REGISTRATION_WAVE_1_MANIFEST.md` for full category table. Summary: **64** core terminology, **8** disambiguation, **6** source governance, **5** DE/EN bridge, **5** industrial document-language, **3** compliance terminology, **3** index maps, **2** methodology, **4** DE gateway mirrors.

---

## Selected languages

| Language | New routes |
| --- | ---: |
| `en` | 30 |
| `de` | 70 |

### German-heavy wave rationale (30 EN / 70 DE)

The **30 English / 70 German** split is **intentional**, not an accidental imbalance.

**Why the wave is German-heavy:**

- **Bisulfid.com has a German lexical and naming identity.** The asset thesis centers on German chemical language (`Bisulfid`, `Sulfid`, `-id`/`-ide` boundaries) as a sovereign terminology layer, not as a secondary translation locale.
- **The German layer is strategically central.** Wave 1 registers DE lexical records, DE disambiguation walls, DE methodology/reference routes, and DE gateway mirrors because German terminology sovereignty must be established before multilingual expansion can be governed safely.
- **German lexical/boundary routes support the German–English chemical-language bridge.** Routes such as `de_bridge_en_de_suffix`, `de_dis_bisulfid_bisulfite`, and the DE terminology spine directly reinforce the DE/EN boundary work that defines the asset.
- **The German-heavy wave strengthens terminology sovereignty, source-boundary work, and future multilingual authority.** Registering DE routes now creates the governed foundation for hreflang wiring, translator playbooks, and controlled expansion without translation spam.

**English remains the global base layer:**

- The **30 English routes** preserve EN as the international reference spine: terminology records (`bisulfid`, `sulfid`, `hydrosulfide`, `sulfate_terminology`), disambiguation authority (`en_dis_*`), source governance (`nomenclature_governance_overview`, `citation_discipline_primer`), and index/map infrastructure (`en_index_*`).
- English is not deprioritized; it holds the **global base layer** while German holds the **lexical identity layer** in this wave.

**Multilingual deferral (ar/zh/ja):**

- The German-heavy split **does not mean ar/zh/ja are ignored.** Arabic, Chinese, and Japanese mirror routes remain **deferred** until the EN/DE spine, hreflang policy, and translation governance are stronger—per Sprint 5I-B charter and blueprint gating (`non_public_until_hreflang_wiring`).

See also `ROUTE_REGISTRATION_WAVE_1_MANIFEST.md` for the parallel language-distribution table.

---

## Included route_id list (100)

```
academic_teaching_source_boundary
bisulfid
bisulfite_wall_explainer
carbon_disulfide_terms
carbonyl_sulfide_terms
citation_discipline_primer
claus_process_vocabulary
contact_process_vocabulary
copper_sulfides_language
de_bisulfid_vs_bisulfide
de_bisulfide_hydrosulfide_sulfide
de_bridge_en_de_suffix
de_bridge_iupac_de
de_core_amines_gas_treat
de_core_biogenic_lang
de_core_cas
de_core_cds
de_core_cus
de_core_fes
de_core_k2s
de_core_liquid_sulfur
de_core_mos2
de_core_na2s
de_core_oleum
de_core_pbs
de_core_scavenger_terms
de_core_sulfur_acid
de_core_sulfur_allotropes
de_core_sulfur_recovery
de_core_tail_gas
de_core_vapor_pressure_lang
de_core_ws2
de_core_zns
de_dis_bisulfid_bisulfite
de_dis_bisulfite_wall
de_disulfide_bonds
de_german_english_chemical_terms
de_glossary
de_gov_nomenclature
de_home
de_ind_filing_language
de_ind_hs_code_language
de_industrial_sulfur_systems
de_molybdenum_disulfide
de_protein_disulfide_structure
de_sulfid_vs_sulfide
de_sulfur_compounds
de_sulfur_uses
de_term_acid_gas
de_term_bisulfit
de_term_bleisulfid
de_term_carbon_disulfide
de_term_carbonyl_sulfide
de_term_claus
de_term_disulfit
de_term_eisensulfid
de_term_elemental_sulfur
de_term_fgd
de_term_kohlenstoffdisulfid
de_term_kupfersulfid
de_term_mercaptan
de_term_molybdaensulfid
de_term_natriumsulfid
de_term_polysulfid
de_term_schwefelsaeure
de_term_sulfat
de_term_sulfate
de_term_sulfit
de_term_sulfite
de_term_sulfonic
de_term_sulfonsaeure
de_term_sulfonyl
de_term_sulfoxid
de_term_thiosulfat
de_term_thiosulfate
de_term_wolframsulfid
de_term_zinksulfid
de_what_is_bisulfid
de_what_is_sulfur
economic_document_language_sulfur
en_compliance_customs_sulfur_lang
en_compliance_export_doc_lang
en_compliance_reach_language
en_dis_carbon_disulfide_bisulfide
en_dis_sulfate_sulfite
en_dis_sulfide_sulfite
en_dis_thiosulfate_sulfite
en_gov_claim_registry_explainer
en_gov_hreflang_policy
en_gov_ontology_governance
en_index_disambiguation_map
en_index_multilingual_map
en_index_terminology_spine
hydrosulfide
nomenclature_governance_overview
sulfate_terminology
sulfid
sulfide_anion_term_record
sulfur_element_term_record
translator_playbook_bisulfide_family
```

---

## Excluded categories and why

| Category / concept type | Reason |
| --- | --- |
| Safety context (H2S risk, SDS, sulfur safety) | High risk; requires dedicated source-locking before route scale |
| Utility (newsletter, acquire) | Not structural foundation; already registered separately |
| High-risk industrial (sodium bisulfide) | `deferred_high_risk_review` |
| ar/zh/ja expansion register | Deferred to controlled multilingual waves |
| Market data / CAGR / trade statistics | Explicit sprint exclusion |
| Medical / handling / procurement | Explicit sprint exclusion |
| Blueprint duplicate rows | Deduplicated at registration |

---

## Duplicate prevention method

- Pre-sprint `route_id` and `path` inventory (26 routes)
- Blueprint row deduplication
- L0 validator duplicate checks post-merge
- One duplicate `de_term_mercaptan` removed; `sulfate_terminology` added as replacement

---

## Why no content pages were created

Sprint charter limits scope to **route registration** under automation stage S1. Content creation belongs to **draft production waves** (S2, 40–60 drafts per wave) after editorial review. Creating bodies without registry stability would violate wave protocol ordering.

---

## Why no routes were published

Publication requires Quality Gate passage, source/claim signoff, and S9 launch authorization. All routes remain `status: planned` with publication locks from Sprint 5I-A.

---

## Why all new routes remain planned

Route registration records intent and governs future content paths without implying publication readiness. The 500-page threshold requires hundreds of additional registry, draft, source-lock, and validation steps.

---

## Why all new routes remain non-indexable and out of sitemap

Pre-launch corpus must not leak into search indexes or sitemaps. Every new route: `indexable: false`, `in_sitemap: false`, `in_navigation: false`.

---

## Why internal_links.json was not modified

Internal link wiring is a separate automation stage (post-draft, pre-publication). Registering routes without content would create false link graph edges.

---

## Why no claim was approved

Claim registries remain **inactive**. No terminology, science, industry, or safety claims were approved. `required_claim_groups` on new routes declare **future** claim boundaries only.

---

## Why no generated HTML was created

This sprint is registry-only. HTML generation belongs to build/preview stages after draft and template readiness.

---

## Remaining route-registration work toward 500

| Item | Estimate |
| --- | ---: |
| Routes registered | 126 |
| Target at launch | 500 |
| Gap | **374** routes |
| At ~100 routes/wave | ~**4** additional registration waves |

Plus: draft production (~374+ bodies), source locking, claim boundary review, internal link wiring, hreflang activation, and Quality Gate validation.

---

## Recommended next sprint

**Sprint 5I-C — Draft production wave 1** (40–60 governed draft bodies for highest-priority newly registered EN terminology spine and DE boundary routes, using existing draft templates; no publication).

Secondary: **Route registration wave 2** (next 80–120 blueprint rows: remaining EN terminology expansion, DE governance/index routes, controlled disambiguation completion).

---

*Sprint 5I-B — Route Registration Wave 1 Report*
