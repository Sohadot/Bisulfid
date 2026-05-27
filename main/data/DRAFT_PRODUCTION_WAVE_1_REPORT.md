# Draft Production Wave 1 — Report

**Sprint:** 5J  
**Date:** 2026-05-27  
**Branch:** `claude/sprint-5j-draft-production-wave-1`

---

## Why this sprint exists

Sprint **5J** creates the **first large draft production wave**—**50 non-public Markdown drafts** for the safest planned routes registered in Sprint **5I-B**, advancing the **500-page sovereign launch program** without publishing routes or modifying `routes.json`.

---

## Relationship to the 500-page launch threshold

| Metric | Value |
| --- | ---: |
| Launch threshold | **500** governed pages |
| Routes in registry | **126** |
| Draft-backed routes before wave 1 | **18** |
| Drafts created in wave 1 | **50** |
| Draft-backed routes after wave 1 | **68** |
| Routes still missing drafts | **58** |
| Remaining toward 500 | **432** governed pages (registration + drafts + validation) |

---

## Relationship to route registration wave 1

All **50** created drafts target **Sprint 5I-B** routes that had **no prior content file**. Wave 1 registration supplied the `route_id` and `content_file` paths; this sprint supplied controlled draft bodies only.

---

## Files reviewed

- `main/data/routes.json`
- `main/data/ROUTE_REGISTRATION_WAVE_1_REPORT.md`
- `main/data/ROUTE_REGISTRATION_WAVE_1_MANIFEST.md`
- `main/data/ROUTE_REGISTRY_L0_VALIDATION_REPORT.md`
- `main/data/CORPUS_AUTOMATION_CONTROL_LAYER.md`
- `main/data/CORPUS_AUTOMATION_MANIFEST.md`
- `main/data/CORPUS_AUTOMATION_WAVE_PROTOCOL.md`
- `main/data/CORPUS_AUTOMATION_VALIDATION_REQUIREMENTS.md`
- `main/data/CORPUS_PRODUCTION_WAVE_MODEL.md`
- `main/data/CORPUS_LAUNCH_THRESHOLD.md`
- `main/data/FIVE_HUNDRED_PAGE_SOVEREIGN_LAUNCH_PROGRAM.md`
- `main/data/LAUNCH_COHORT_BLUEPRINT_QUALITY_REVIEW.md`
- `main/data/LAUNCH_COHORT_REFINEMENT_RECOMMENDATIONS.md`
- `main/data/LAUNCH_COHORT_IMPLEMENTATION_BATCH_1.md`
- `main/data/ROUTE_IMPLEMENTATION_READINESS_MATRIX.md`
- `DECISION_LOG.md`
- Existing draft pages under `main/content/` (style reference)

---

## Draft selection method

1. Inventory **126** routes and **18** existing content files.
2. Exclude routes with existing `content_file` on disk (no overwrite).
3. Filter Sprint **5I-B** routes: low/medium risk, EN/DE only, no safety/utility/acquisition.
4. Score by blueprint priority, EN structural categories, then DE bridge/lexical routes.
5. Select top **50** eligible targets.

---

## Draft counts

| Metric | Count |
| --- | ---: |
| Routes in registry (unchanged) | **126** |
| Draft-backed routes before sprint | **18** |
| Drafts created this sprint | **50** |
| Draft-backed routes after sprint | **68** |
| Routes still missing drafts | **58** |

---

## Selected route_id list (50)

```
bisulfid
sulfid
hydrosulfide
sulfide_anion_term_record
sulfur_element_term_record
bisulfite_wall_explainer
nomenclature_governance_overview
translator_playbook_bisulfide_family
carbon_disulfide_terms
carbonyl_sulfide_terms
copper_sulfides_language
sulfate_terminology
academic_teaching_source_boundary
citation_discipline_primer
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
de_glossary
de_what_is_bisulfid
de_bisulfide_hydrosulfide_sulfide
claus_process_vocabulary
contact_process_vocabulary
economic_document_language_sulfur
en_compliance_customs_sulfur_lang
en_compliance_export_doc_lang
en_compliance_reach_language
de_bisulfid_vs_bisulfide
de_bridge_en_de_suffix
de_bridge_iupac_de
de_german_english_chemical_terms
de_home
de_sulfid_vs_sulfide
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
```

---

## Selected content_file path list (50)

```
main/content/en/pages/bisulfid.md
main/content/en/pages/sulfid.md
main/content/en/pages/hydrosulfide.md
main/content/en/pages/terminology/sulfide-anion.md
main/content/en/pages/terminology/sulfur-element.md
main/content/en/pages/bisulfite-wall.md
main/content/en/pages/nomenclature-governance.md
main/content/en/pages/translator-playbook-bisulfide-family.md
main/content/en/pages/terminology/carbon-disulfide.md
main/content/en/pages/terminology/carbonyl-sulfide.md
main/content/en/pages/terminology/copper-sulfides.md
main/content/en/pages/terminology/sulfate.md
main/content/en/pages/academic-teaching-source-boundary.md
main/content/en/pages/citation-discipline.md
main/content/en/pages/cs2-bisulfide-boundary.md
main/content/en/pages/sulfate-sulfite-boundary.md
main/content/en/pages/sulfide-sulfite-boundary.md
main/content/en/pages/thiosulfate-sulfite-boundary.md
main/content/en/pages/claim-registry-explainer.md
main/content/en/pages/hreflang-policy.md
main/content/en/pages/ontology-governance.md
main/content/en/pages/disambiguation-map.md
main/content/en/pages/multilingual-layer-map.md
main/content/en/pages/terminology-spine-map.md
main/content/de/pages/glossary.md
main/content/de/pages/what-is-bisulfid.md
main/content/de/pages/bisulfide-hydrosulfide-sulfide.md
main/content/en/pages/industrial/claus-process-vocabulary.md
main/content/en/pages/industrial/contact-process-vocabulary.md
main/content/en/pages/economic-document-language-sulfur.md
main/content/en/pages/compliance/customs-sulfur-language.md
main/content/en/pages/compliance/export-document-language.md
main/content/en/pages/compliance/reach-document-language.md
main/content/de/pages/bisulfid-vs-bisulfide.md
main/content/de/pages/suffix-bridge.md
main/content/de/pages/iupac-de-boundary.md
main/content/de/pages/german-english-chemical-terms.md
main/content/de/pages/de.md
main/content/de/pages/sulfid-vs-sulfide.md
main/content/de/pages/terminology/amines-gas-treating.md
main/content/de/pages/terminology/biogenic-sulfur-language.md
main/content/de/pages/terminology/calcium-sulfide.md
main/content/de/pages/terminology/cadmium-sulfide.md
main/content/de/pages/terminology/copper-sulfides.md
main/content/de/pages/terminology/iron-sulfides.md
main/content/de/pages/terminology/potassium-sulfide.md
main/content/de/pages/terminology/liquid-sulfur.md
main/content/de/pages/terminology/molybdenum-disulfide.md
main/content/de/pages/terminology/sodium-sulfide.md
main/content/de/pages/terminology/oleum.md
```

---

## Selected route categories

**22** core terminology, **6** disambiguation, **5** source governance, **5** DE/EN bridge, **3** industrial document-language, **3** compliance terminology, **3** index maps, **2** methodology, **1** DE gateway.

---

## Selected languages

| Language | Drafts |
| --- | ---: |
| `en` | 30 |
| `de` | 20 |

---

## Skipped categories and why

| Skipped | Reason |
| --- | --- |
| 18 routes with pre-existing drafts | No-overwrite rule |
| Safety / high-risk substance routes | Not eligible for safe drafting |
| Utility routes | Out of scope |
| ar/zh/ja | Deferred |
| Remaining 50 Sprint 5I-B routes | Lower priority vs selected 50; reserved for wave 2 |

---

## Why no routes.json changes were made

Route registration is complete for wave 1 targets. Draft production (S2) is **separate** from registry mutation (S1). Publication flags remain on routes, not draft files.

---

## Why no routes were published

Quality Gate, source-locking, claim review, and S9 launch authorization are **not satisfied**. All routes remain `planned`.

---

## Why all created drafts remain non-public

Every draft uses `status: draft`, `publication_status: non_public`, and explicit non-public / not-publication-ready notices. No HTML output was generated.

---

## Why no claims were approved

Claim registries remain **inactive**. Drafts state **no approved claims** and use `[SOURCE REQUIRED]` for factual lines.

---

## Why internal_links.json was not modified

Link graph wiring follows draft stabilization and editorial review—separate automation stage.

---

## Why no generated HTML was created

Sprint scope is Markdown draft bodies only.

---

## Source and claim boundary posture

- **Source-locking:** not complete on new drafts.
- **Claims:** none approved; illustrative language is candidate support only.
- **Markers:** `[SOURCE REQUIRED]` present on authority-sensitive lines.
- **Links:** no raw URLs; no markdown links to unpublished routes.

---

## Remaining work toward 500 governed pages

| Workstream | Estimate |
| --- | ---: |
| Routes still without drafts | **58** |
| Routes not yet registered | **374** |
| Draft waves remaining | ~**8–10** at 40–60 drafts/wave |
| Source-lock + claim + link + publication gates | All pending |

---

## Recommended next sprint

**Sprint 5J-B or 5K — Draft production wave 2** (next 40–60 drafts for remaining Sprint 5I-B DE lexical routes and EN terminology expansion), **or** **route registration wave 2** if registry gap is prioritized.

---

*Sprint 5J — Draft Production Wave 1 Report*
