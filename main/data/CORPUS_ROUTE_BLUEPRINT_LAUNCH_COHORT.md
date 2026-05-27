# Corpus Route Blueprint — Launch Cohort (Sprint 5A, revised Sprint 5H)

## Charter

This document lists **proposed** page concepts for the **minimum public launch cohort** (**≥ 500 governed pages** as of Sprint 5H) and aligned multilingual expansion. It is a **blueprint only**: **no** `routes.json` edits were made in Sprint 5A or 5H; **no** `content_file` bodies were created in those sprints; **no** publication occurred.

- **500 governed pages** = minimum first-launch threshold (Sprint 5H upgrade from 300), **not** the final corpus size.
- **300 pages is no longer sufficient** for the owner’s sovereign-grade launch standard.
- Each row is a **planning record** with a declared corpus role, source posture, risk, eligibility, linking cluster, and priority.

## Column definitions

| Column | Meaning |
| --- | --- |
| proposed_route_id | Intended registry id when routed (not yet in `routes.json` for blueprint-only rows) |
| proposed_path | Intended public URL path |
| language | `en`, `de`, `ar`, `zh`, or `ja` |
| corpus_category | Architecture category |
| page_role | One-line corpus purpose |
| source_requirement_level | e.g. strict_registry, governance_meta |
| claim_risk_level | low / medium / high |
| public_launch_eligibility | gating summary |
| internal_linking_cluster | Planned hub/spoke cluster id |
| priority_level | P0 / P1 / P2 / P3 |

## Full blueprint table

| proposed_route_id | proposed_path | language | corpus_category | page_role | source_requirement_level | claim_risk_level | public_launch_eligibility | internal_linking_cluster | priority_level |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| home | / | en | gateway | Primary gateway page. Hub of the internal link graph. Features the Interactive Term Map. | governance_meta | low | eligible_after_full_source_lock | gateway | P1 |
| what_is_sulfur | /what-is-sulfur/ | en | gateway | Entry-point page for general readers. Layer 01 — Public Gateway. | strict_registry | low | eligible_after_full_source_lock | gateway | P1 |
| sulfur_compounds | /sulfur-compounds/ | en | gateway | Layer 01 — Public Gateway. Bridge between public entry point and terminology system. | strict_registry | low | eligible_after_full_source_lock | gateway | P1 |
| sulfur_uses | /sulfur-uses/ | en | gateway | Layer 01 — Public Gateway. Entry point toward industrial intelligence layer. | strict_registry | low | eligible_after_full_source_lock | gateway | P1 |
| what_is_bisulfid | /what-is-bisulfid/ | en | de_en_chemical_language | Layer 02 — Core terminology page. Center concept of the asset. High authority requirement. | strict_registry | medium | eligible_after_full_source_lock | de_en_bridge | P0 |
| bisulfid_vs_bisulfide | /bisulfid-vs-bisulfide/ | en | de_en_chemical_language | Layer 02 — Core DE/EN boundary page. Central to asset thesis. | strict_registry | medium | eligible_after_full_source_lock | de_en_bridge | P1 |
| sulfid_vs_sulfide | /sulfid-vs-sulfide/ | en | de_en_chemical_language | Layer 02 — Terminology system. Supports and parallels bisulfid-vs-bisulfide argument. | strict_registry | low | eligible_after_full_source_lock | de_en_bridge | P1 |
| bisulfide_hydrosulfide_sulfide | /bisulfide-hydrosulfide-sulfide/ | en | disambiguation_authority | Layer 02 — Terminology disambiguation. Chemical precision required. | strict_registry | medium | eligible_after_full_source_lock | disambiguation | P0 |
| sodium_bisulfide | /sodium-bisulfide/ | en | industrial_economic_interpretation | Layer 03 — Industrial Intelligence. High risk: safety context required. No handling instructions. | strict_registry | high | deferred_high_risk_review | industrial_interpretation | P2 |
| disulfide_bonds | /disulfide-bonds/ | en | core_terminology | Layer 05 — Future Materials. Bridges terminology system to biochemistry and materials science. | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P1 |
| industrial_sulfur_systems | /industrial-sulfur-systems/ | en | industrial_economic_interpretation | Layer 03 — Industrial Intelligence. No unverified market data. | strict_registry | medium | eligible_after_full_source_lock | industrial_interpretation | P1 |
| sulfur_safety_context | /sulfur-safety-context/ | en | safety_context | Layer 04 — Safety Governance. Strict: no handling instructions, no dosage, no prescriptive thresholds. | strict_registry | high | deferred_high_risk_review | safety_context | P2 |
| hydrogen_sulfide_risk | /hydrogen-sulfide-risk/ | en | safety_context | Layer 04 — Safety Governance. Highest risk page. H2S is acutely hazardous. No prescriptive thresholds, no emergency r... | strict_registry | high | deferred_high_risk_review | safety_context | P2 |
| sds_and_sulfur_terms | /sds-and-sulfur-terms/ | en | safety_context | Layer 04 — Safety Governance. Explains SDS terminology context only. No prescriptive advice. | strict_registry | high | deferred_high_risk_review | safety_context | P2 |
| protein_disulfide_structure | /protein-disulfide-structure/ | en | core_terminology | Layer 05 — Future Materials. Establishes asset relevance in biochemistry and advanced materials. | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P1 |
| molybdenum_disulfide | /molybdenum-disulfide/ | en | industrial_economic_interpretation | Layer 05 — Future Materials. Extends terminology system into advanced industrial materials. | strict_registry | low | eligible_after_full_source_lock | industrial_interpretation | P1 |
| german_english_chemical_terms | /german-english-chemical-terms/ | en | de_en_chemical_language | Layer 02 — Terminology System. Supports the German identity layer argument. | strict_registry | low | eligible_after_full_source_lock | de_en_bridge | P1 |
| glossary | /glossary/ | en | core_terminology | Central reference page. Driven by sulfur_terms.json ontology. All terms must be source-validated before page publishes. | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P0 |
| sources | /sources/ | en | source_governance | Driven by source_registry.json. Only published when source registry has verified entries. | governance_meta | low | eligible_after_full_source_lock | governance | P1 |
| newsletter | /newsletter/ | en | utility | Phase 02 revenue layer. No factual claims requiring sources. | governance_meta | low | eligible_after_full_source_lock | operations | P1 |
| acquire | /acquire/ | en | utility | Layer 05 / Quality Gate 10. Must not name specific company targets. Strategic asset value framing only. | governance_meta | low | eligible_after_full_source_lock | operations | P1 |
| bisulfid | /bisulfid/ | en | core_terminology | Standalone DE brand-center Bisulfid record blueprint pending route registration | strict_registry | medium | non_public_until_route_registered | terminology_spine | P0 |
| sulfid | /sulfid/ | en | core_terminology | Standalone DE lexical Sulfid record blueprint pending route registration | strict_registry | low | non_public_until_route_registered | terminology_spine | P0 |
| hydrosulfide | /hydrosulfide/ | en | core_terminology | English hydrosulfide label record complement to triad page | strict_registry | medium | non_public_until_route_registered | terminology_spine | P1 |
| corpus_methodology_overview | /reference/corpus-methodology/ | en | methodology_reference | How bisulfid authors sovereign reference pages | governance_meta | low | non_public_until_editorial_signoff | governance | P1 |
| nomenclature_governance_overview | /reference/nomenclature-governance/ | en | source_governance | Readable nomenclature discipline tied to SOURCE_POLICY | strict_registry | low | eligible_after_full_source_lock | governance | P1 |
| multilingual_corpus_map | /reference/multilingual-corpus-map/ | en | index_map | Planned multilingual hub index non-thin | governance_meta | low | non_public_until_hreflang_wiring | index_map | P2 |
| economic_document_language_sulfur | /reference/economic-document-language-sulfur/ | en | industrial_economic_interpretation | Sulfur language in filings and sector docs terminology only | strict_registry | medium | eligible_after_full_source_lock | industrial_interpretation | P2 |
| supply_chain_vocabulary_sulfur | /reference/supply-chain-vocabulary-sulfur/ | en | industrial_economic_interpretation | Logistics and trade document vocabulary without market statistics | strict_registry | medium | eligible_after_full_source_lock | industrial_interpretation | P2 |
| quality_gate_public_explainer | /reference/quality-gate/ | en | methodology_reference | Public explainer of Quality Gate expectations | governance_meta | low | non_public_until_owner_review | governance | P2 |
| translator_playbook_bisulfide_family | /reference/translator-playbook-bisulfide-family/ | en | methodology_reference | Controlled DE/EN playbook for translators | strict_registry | low | eligible_after_full_source_lock | governance | P1 |
| ontology_alignment_primer | /reference/ontology-alignment-primer/ | en | methodology_reference | How sulfur_terms ontology ties to pages | strict_registry | low | non_public_until_registry_activation | governance | P2 |
| internal_linking_discipline | /reference/internal-linking-discipline/ | en | methodology_reference | Cluster and density rules for editors | governance_meta | low | non_public_until_editorial_signoff | governance | P2 |
| citation_discipline_primer | /reference/citation-discipline/ | en | source_governance | How citations surface from source_registry | strict_registry | low | eligible_after_full_source_lock | governance | P2 |
| academic_teaching_source_boundary | /reference/academic-teaching-source-boundary/ | en | source_governance | Teaching reference limits per SOURCE_POLICY | strict_registry | low | eligible_after_full_source_lock | governance | P2 |
| bisulfite_wall_explainer | /reference/bisulfite-wall/ | en | disambiguation_authority | Public explainer of bisulfite vs bisulfide family boundary | strict_registry | medium | eligible_after_full_source_lock | disambiguation | P1 |
| sulfur_element_term_record | /terminology/sulfur-element/ | en | core_terminology | Canonical element-level terminology record | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P1 |
| sulfide_anion_term_record | /terminology/sulfide-anion/ | en | core_terminology | Sulfide anion terminology record | strict_registry | medium | eligible_after_full_source_lock | terminology_spine | P1 |
| hydrogen_sulfide_term_record | /terminology/hydrogen-sulfide/ | en | core_terminology | H2S identity terminology non-manual | strict_registry | high | deferred_high_risk_review | terminology_spine | P2 |
| sulfate_terminology | /terminology/sulfate/ | en | core_terminology | Sulfate ion and salt naming vocabulary | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| sulfite_terminology | /terminology/sulfite/ | en | core_terminology | Sulfite family vocabulary separate from bisulfide | strict_registry | medium | eligible_after_full_source_lock | terminology_spine | P2 |
| thiosulfate_terminology | /terminology/thiosulfate/ | en | core_terminology | Thiosulfate terminology record | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| polysulfide_terminology | /terminology/polysulfide/ | en | core_terminology | Polysulfide terminology | strict_registry | medium | eligible_after_full_source_lock | terminology_spine | P2 |
| sulfane_chain_language | /terminology/sulfane/ | en | core_terminology | Sulfane chain nomenclature language | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| carbon_disulfide_terms | /terminology/carbon-disulfide/ | en | core_terminology | CS2 terminology industrial vocabulary | strict_registry | medium | eligible_after_full_source_lock | terminology_spine | P2 |
| carbonyl_sulfide_terms | /terminology/carbonyl-sulfide/ | en | core_terminology | COS terminology record | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| mercaptan_class_language | /terminology/mercaptan-class/ | en | core_terminology | Thiol mercaptan class naming | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| sulfonic_acid_class_language | /terminology/sulfonic-acid-class/ | en | core_terminology | Sulfonic acid family naming | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| sulfoxide_sulfone_language | /terminology/sulfoxide-sulfone/ | en | core_terminology | Sulfoxide and sulfone naming | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| frasch_process_vocabulary | /industrial/frasch-process-vocabulary/ | en | industrial_economic_interpretation | Historical process naming without production advice | strict_registry | low | eligible_after_full_source_lock | industrial_interpretation | P3 |
| claus_process_vocabulary | /industrial/claus-process-vocabulary/ | en | industrial_economic_interpretation | SRU Claus terminology | strict_registry | low | eligible_after_full_source_lock | industrial_interpretation | P2 |
| contact_process_vocabulary | /industrial/contact-process-vocabulary/ | en | industrial_economic_interpretation | Sulfuric acid contact process vocabulary | strict_registry | low | eligible_after_full_source_lock | industrial_interpretation | P2 |
| fgd_document_language | /industrial/fgd-document-language/ | en | industrial_economic_interpretation | Flue gas desulfurization document vocabulary | strict_registry | medium | eligible_after_full_source_lock | industrial_interpretation | P2 |
| sour_gas_document_language | /industrial/sour-gas-document-language/ | en | industrial_economic_interpretation | Sour gas terminology non-operational | strict_registry | high | deferred_high_risk_review | industrial_interpretation | P2 |
| hydrotreating_desulfurization_terms | /industrial/hydrotreating-desulfurization-terms/ | en | industrial_economic_interpretation | Refinery desulfurization vocabulary | strict_registry | medium | eligible_after_full_source_lock | industrial_interpretation | P2 |
| sodium_sulfide_salts_language | /terminology/sodium-sulfide-salts/ | en | core_terminology | Na2S family naming disambiguation | strict_registry | medium | eligible_after_full_source_lock | terminology_spine | P2 |
| iron_sulfides_mineral_language | /terminology/iron-sulfides/ | en | core_terminology | Pyrite pyrrhotite terminology | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| copper_sulfides_language | /terminology/copper-sulfides/ | en | core_terminology | Chalcocite covellite terminology | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| zinc_lead_sulfides_language | /terminology/zinc-lead-sulfides/ | en | core_terminology | Sphalerite galena vocabulary subset | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| arsenic_antimony_sulfides_language | /terminology/arsenic-antimony-sulfides/ | en | core_terminology | Orpiment stibnite related vocabulary | strict_registry | medium | eligible_after_full_source_lock | terminology_spine | P3 |
| tungsten_disulfide_terms | /terminology/tungsten-disulfide/ | en | core_terminology | WS2 materials vocabulary | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| tin_sulfides_terms | /terminology/tin-sulfides/ | en | core_terminology | Tin sulfide naming | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P3 |
| silver_gold_sulfides_terms | /terminology/precious-metal-sulfides/ | en | core_terminology | Argentite etc vocabulary caution | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P3 |
| de_home | /de/ | de | gateway | Language gateway sovereign framing | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P0 |
| de_what_is_bisulfid | /de/what-is-bisulfid/ | de | core_terminology | Canonical Bisulfid record in target language | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P0 |
| de_what_is_sulfur | /de/what-is-sulfur/ | de | gateway | Sulfur gateway in target language | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_sulfur_compounds | /de/sulfur-compounds/ | de | gateway | Compounds map vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_sulfur_uses | /de/sulfur-uses/ | de | gateway | Uses framing vocabulary not market data | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_bisulfid_vs_bisulfide | /de/bisulfid-vs-bisulfide/ | de | de_en_chemical_language | Orthography boundary narrative | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_sulfid_vs_sulfide | /de/sulfid-vs-sulfide/ | de | de_en_chemical_language | Sulfid sulfide boundary | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_bisulfide_hydrosulfide_sulfide | /de/bisulfide-hydrosulfide-sulfide/ | de | disambiguation_authority | Triad disambiguation authority | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P0 |
| de_german_english_chemical_terms | /de/german-english-chemical-terms/ | de | de_en_chemical_language | Cross-language chemical term table | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_glossary | /de/glossary/ | de | core_terminology | Controlled glossary chamber | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P0 |
| de_sources | /de/sources/ | de | source_governance | Sources face localized | strict_registry | high | deferred_high_risk_review | multilingual_de | P2 |
| de_industrial_sulfur_systems | /de/industrial-sulfur-systems/ | de | core_terminology | Industrial systems vocabulary | strict_registry | medium | eligible_after_full_source_lock | multilingual_de | P1 |
| de_sodium_bisulfide | /de/sodium-bisulfide/ | de | core_terminology | Substance terminology high scrutiny | strict_registry | high | deferred_high_risk_review | multilingual_de | P2 |
| de_sulfur_safety_context | /de/sulfur-safety-context/ | de | core_terminology | Safety context non-manual | strict_registry | high | deferred_high_risk_review | multilingual_de | P2 |
| de_hydrogen_sulfide_risk | /de/hydrogen-sulfide-risk/ | de | core_terminology | H2S awareness terminology | strict_registry | high | deferred_high_risk_review | multilingual_de | P2 |
| de_sds_and_sulfur_terms | /de/sds-and-sulfur-terms/ | de | core_terminology | SDS naming vocabulary | strict_registry | high | deferred_high_risk_review | multilingual_de | P2 |
| de_disulfide_bonds | /de/disulfide-bonds/ | de | core_terminology | Disulfide bond terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_protein_disulfide_structure | /de/protein-disulfide-structure/ | de | core_terminology | Protein disulfide terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_molybdenum_disulfide | /de/molybdenum-disulfide/ | de | core_terminology | MoS2 vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_newsletter | /de/newsletter/ | de | utility | Newsletter surface localized | governance_meta | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_acquire | /de/acquire/ | de | utility | Acquisition inquiry localized | governance_meta | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_term_sulfate | /de/terminology/sulfate/ | de | core_terminology | Sulfate terminology localized | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_term_sulfite | /de/terminology/sulfite/ | de | core_terminology | Sulfite terminology localized | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_term_thiosulfate | /de/terminology/thiosulfate/ | de | core_terminology | Thiosulfate terminology localized | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_term_hydrogen_sulfide | /de/terminology/hydrogen-sulfide/ | de | core_terminology | H2S terminology localized | strict_registry | high | deferred_high_risk_review | multilingual_de | P2 |
| de_term_elemental_sulfur | /de/terminology/elemental-sulfur/ | de | core_terminology | Elemental sulfur forms vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_term_acid_gas | /de/terminology/acid-gas/ | de | core_terminology | Acid gas document vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_term_sour_crude | /de/terminology/sour-crude/ | de | core_terminology | Sour crude language only | strict_registry | high | deferred_high_risk_review | multilingual_de | P2 |
| de_term_claus | /de/terminology/claus-sru/ | de | core_terminology | Claus SRU vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_term_fgd | /de/terminology/fgd/ | de | core_terminology | FGD vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_term_mercaptan | /de/terminology/mercaptan/ | de | core_terminology | Mercaptan naming localized | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_term_sulfonic | /de/terminology/sulfonic-acid/ | de | core_terminology | Sulfonic acid naming localized | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_term_carbon_disulfide | /de/terminology/carbon-disulfide/ | de | core_terminology | CS2 localized | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_term_carbonyl_sulfide | /de/terminology/carbonyl-sulfide/ | de | core_terminology | COS localized | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_ind_filing_language | /de/industrial/filing-language/ | de | industrial_economic_interpretation | Filing sulfur language only | strict_registry | medium | eligible_after_full_source_lock | multilingual_de | P1 |
| de_ind_hs_code_language | /de/industrial/hs-code-language/ | de | industrial_economic_interpretation | Trade classification vocabulary not statistics | strict_registry | medium | eligible_after_full_source_lock | multilingual_de | P1 |
| de_method_corpus_map | /de/reference/corpus-map/ | de | methodology_reference | Localized corpus map hub | governance_meta | low | non_public_until_editorial_signoff | multilingual_de | P1 |
| de_method_translator_playbook | /de/reference/translator-playbook/ | de | methodology_reference | Localized translator playbook | governance_meta | low | non_public_until_editorial_signoff | multilingual_de | P1 |
| de_dis_bisulfite_wall | /de/reference/bisulfite-wall/ | de | disambiguation_authority | Bisulfite wall localized | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_gov_nomenclature | /de/reference/nomenclature-governance/ | de | source_governance | Nomenclature governance localized | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_core_na2s | /de/terminology/sodium-sulfide/ | de | core_terminology | Na2S salt naming localized | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_core_k2s | /de/terminology/potassium-sulfide/ | de | core_terminology | K2S naming localized | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_core_cas | /de/terminology/calcium-sulfide/ | de | core_terminology | CaS naming localized | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_core_fes | /de/terminology/iron-sulfides/ | de | core_terminology | Iron sulfides localized | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_core_cus | /de/terminology/copper-sulfides/ | de | core_terminology | Copper sulfides localized | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_core_zns | /de/terminology/zinc-sulfide/ | de | core_terminology | Zinc sulfide localized | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_core_pbs | /de/terminology/lead-sulfide/ | de | core_terminology | Lead sulfide localized | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_core_cds | /de/terminology/cadmium-sulfide/ | de | core_terminology | Cadmium sulfide localized | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_core_mos2 | /de/terminology/molybdenum-disulfide/ | de | core_terminology | MoS2 specialist localized | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_core_ws2 | /de/terminology/tungsten-disulfide/ | de | core_terminology | WS2 localized | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_core_h2s_aware | /de/terminology/h2s-awareness/ | de | core_terminology | H2S duplicate awareness localized | strict_registry | high | deferred_high_risk_review | multilingual_de | P2 |
| de_core_sulfur_allotropes | /de/terminology/sulfur-allotropes/ | de | core_terminology | Allotrope naming localized | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_core_sulfur_acid | /de/terminology/sulfuric-acid/ | de | core_terminology | Sulfuric acid terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_core_oleum | /de/terminology/oleum/ | de | core_terminology | Oleum terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_core_liquid_sulfur | /de/terminology/liquid-sulfur/ | de | core_terminology | Molten sulfur language non-handling | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_core_sulfur_recovery | /de/terminology/sulfur-recovery/ | de | core_terminology | Recovery terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_core_tail_gas | /de/terminology/tail-gas/ | de | core_terminology | Tail gas vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_core_amines_gas_treat | /de/terminology/amines-gas-treating/ | de | core_terminology | Amine treating vocabulary language | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_core_scavenger_terms | /de/terminology/h2s-scavenger-terms/ | de | core_terminology | Scavenger naming language | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_core_biogenic_lang | /de/terminology/biogenic-sulfur-language/ | de | core_terminology | Biogenic vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_core_vapor_pressure_lang | /de/terminology/vapor-pressure-language/ | de | core_terminology | Vapor pressure language only | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| ar_home | /ar/ | ar | gateway | Language gateway sovereign framing | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P0 |
| ar_what_is_bisulfid | /ar/what-is-bisulfid/ | ar | core_terminology | Canonical Bisulfid record in target language | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P0 |
| ar_what_is_sulfur | /ar/what-is-sulfur/ | ar | gateway | Sulfur gateway in target language | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_sulfur_compounds | /ar/sulfur-compounds/ | ar | gateway | Compounds map vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_sulfur_uses | /ar/sulfur-uses/ | ar | gateway | Uses framing vocabulary not market data | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_bisulfid_vs_bisulfide | /ar/bisulfid-vs-bisulfide/ | ar | de_en_chemical_language | Orthography boundary narrative | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_sulfid_vs_sulfide | /ar/sulfid-vs-sulfide/ | ar | de_en_chemical_language | Sulfid sulfide boundary | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_bisulfide_hydrosulfide_sulfide | /ar/bisulfide-hydrosulfide-sulfide/ | ar | disambiguation_authority | Triad disambiguation authority | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P0 |
| ar_german_english_chemical_terms | /ar/german-english-chemical-terms/ | ar | de_en_chemical_language | Cross-language chemical term table | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_glossary | /ar/glossary/ | ar | core_terminology | Controlled glossary chamber | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P0 |
| ar_sources | /ar/sources/ | ar | source_governance | Sources face localized | strict_registry | high | deferred_high_risk_review | multilingual_ar | P2 |
| ar_industrial_sulfur_systems | /ar/industrial-sulfur-systems/ | ar | core_terminology | Industrial systems vocabulary | strict_registry | medium | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_sodium_bisulfide | /ar/sodium-bisulfide/ | ar | core_terminology | Substance terminology high scrutiny | strict_registry | high | deferred_high_risk_review | multilingual_ar | P2 |
| ar_sulfur_safety_context | /ar/sulfur-safety-context/ | ar | core_terminology | Safety context non-manual | strict_registry | high | deferred_high_risk_review | multilingual_ar | P2 |
| ar_hydrogen_sulfide_risk | /ar/hydrogen-sulfide-risk/ | ar | core_terminology | H2S awareness terminology | strict_registry | high | deferred_high_risk_review | multilingual_ar | P2 |
| ar_sds_and_sulfur_terms | /ar/sds-and-sulfur-terms/ | ar | core_terminology | SDS naming vocabulary | strict_registry | high | deferred_high_risk_review | multilingual_ar | P2 |
| ar_disulfide_bonds | /ar/disulfide-bonds/ | ar | core_terminology | Disulfide bond terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_protein_disulfide_structure | /ar/protein-disulfide-structure/ | ar | core_terminology | Protein disulfide terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_molybdenum_disulfide | /ar/molybdenum-disulfide/ | ar | core_terminology | MoS2 vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_newsletter | /ar/newsletter/ | ar | utility | Newsletter surface localized | governance_meta | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_acquire | /ar/acquire/ | ar | utility | Acquisition inquiry localized | governance_meta | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_term_sulfate | /ar/terminology/sulfate/ | ar | core_terminology | Sulfate terminology localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_term_sulfite | /ar/terminology/sulfite/ | ar | core_terminology | Sulfite terminology localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_term_thiosulfate | /ar/terminology/thiosulfate/ | ar | core_terminology | Thiosulfate terminology localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_term_hydrogen_sulfide | /ar/terminology/hydrogen-sulfide/ | ar | core_terminology | H2S terminology localized | strict_registry | high | deferred_high_risk_review | multilingual_ar | P2 |
| ar_term_elemental_sulfur | /ar/terminology/elemental-sulfur/ | ar | core_terminology | Elemental sulfur forms vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_term_acid_gas | /ar/terminology/acid-gas/ | ar | core_terminology | Acid gas document vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_term_sour_crude | /ar/terminology/sour-crude/ | ar | core_terminology | Sour crude language only | strict_registry | high | deferred_high_risk_review | multilingual_ar | P2 |
| ar_term_claus | /ar/terminology/claus-sru/ | ar | core_terminology | Claus SRU vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_term_fgd | /ar/terminology/fgd/ | ar | core_terminology | FGD vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_term_mercaptan | /ar/terminology/mercaptan/ | ar | core_terminology | Mercaptan naming localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_term_sulfonic | /ar/terminology/sulfonic-acid/ | ar | core_terminology | Sulfonic acid naming localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_term_carbon_disulfide | /ar/terminology/carbon-disulfide/ | ar | core_terminology | CS2 localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_term_carbonyl_sulfide | /ar/terminology/carbonyl-sulfide/ | ar | core_terminology | COS localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_ind_filing_language | /ar/industrial/filing-language/ | ar | industrial_economic_interpretation | Filing sulfur language only | strict_registry | medium | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_ind_hs_code_language | /ar/industrial/hs-code-language/ | ar | industrial_economic_interpretation | Trade classification vocabulary not statistics | strict_registry | medium | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_method_corpus_map | /ar/reference/corpus-map/ | ar | methodology_reference | Localized corpus map hub | governance_meta | low | non_public_until_editorial_signoff | multilingual_ar | P1 |
| ar_method_translator_playbook | /ar/reference/translator-playbook/ | ar | methodology_reference | Localized translator playbook | governance_meta | low | non_public_until_editorial_signoff | multilingual_ar | P1 |
| ar_dis_bisulfite_wall | /ar/reference/bisulfite-wall/ | ar | disambiguation_authority | Bisulfite wall localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_gov_nomenclature | /ar/reference/nomenclature-governance/ | ar | source_governance | Nomenclature governance localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_core_na2s | /ar/terminology/sodium-sulfide/ | ar | core_terminology | Na2S salt naming localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_core_k2s | /ar/terminology/potassium-sulfide/ | ar | core_terminology | K2S naming localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_core_cas | /ar/terminology/calcium-sulfide/ | ar | core_terminology | CaS naming localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_core_fes | /ar/terminology/iron-sulfides/ | ar | core_terminology | Iron sulfides localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_core_cus | /ar/terminology/copper-sulfides/ | ar | core_terminology | Copper sulfides localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_core_zns | /ar/terminology/zinc-sulfide/ | ar | core_terminology | Zinc sulfide localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_core_pbs | /ar/terminology/lead-sulfide/ | ar | core_terminology | Lead sulfide localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_core_cds | /ar/terminology/cadmium-sulfide/ | ar | core_terminology | Cadmium sulfide localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_core_mos2 | /ar/terminology/molybdenum-disulfide/ | ar | core_terminology | MoS2 specialist localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_core_ws2 | /ar/terminology/tungsten-disulfide/ | ar | core_terminology | WS2 localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_core_h2s_aware | /ar/terminology/h2s-awareness/ | ar | core_terminology | H2S duplicate awareness localized | strict_registry | high | deferred_high_risk_review | multilingual_ar | P2 |
| ar_core_sulfur_allotropes | /ar/terminology/sulfur-allotropes/ | ar | core_terminology | Allotrope naming localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_core_sulfur_acid | /ar/terminology/sulfuric-acid/ | ar | core_terminology | Sulfuric acid terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_core_oleum | /ar/terminology/oleum/ | ar | core_terminology | Oleum terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_core_liquid_sulfur | /ar/terminology/liquid-sulfur/ | ar | core_terminology | Molten sulfur language non-handling | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_core_sulfur_recovery | /ar/terminology/sulfur-recovery/ | ar | core_terminology | Recovery terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_core_tail_gas | /ar/terminology/tail-gas/ | ar | core_terminology | Tail gas vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_core_amines_gas_treat | /ar/terminology/amines-gas-treating/ | ar | core_terminology | Amine treating vocabulary language | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_core_scavenger_terms | /ar/terminology/h2s-scavenger-terms/ | ar | core_terminology | Scavenger naming language | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_core_biogenic_lang | /ar/terminology/biogenic-sulfur-language/ | ar | core_terminology | Biogenic vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_core_vapor_pressure_lang | /ar/terminology/vapor-pressure-language/ | ar | core_terminology | Vapor pressure language only | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| zh_home | /zh/ | zh | gateway | Language gateway sovereign framing | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P0 |
| zh_what_is_bisulfid | /zh/what-is-bisulfid/ | zh | core_terminology | Canonical Bisulfid record in target language | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P0 |
| zh_what_is_sulfur | /zh/what-is-sulfur/ | zh | gateway | Sulfur gateway in target language | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_sulfur_compounds | /zh/sulfur-compounds/ | zh | gateway | Compounds map vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_sulfur_uses | /zh/sulfur-uses/ | zh | gateway | Uses framing vocabulary not market data | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_bisulfid_vs_bisulfide | /zh/bisulfid-vs-bisulfide/ | zh | de_en_chemical_language | Orthography boundary narrative | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_sulfid_vs_sulfide | /zh/sulfid-vs-sulfide/ | zh | de_en_chemical_language | Sulfid sulfide boundary | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_bisulfide_hydrosulfide_sulfide | /zh/bisulfide-hydrosulfide-sulfide/ | zh | disambiguation_authority | Triad disambiguation authority | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P0 |
| zh_german_english_chemical_terms | /zh/german-english-chemical-terms/ | zh | de_en_chemical_language | Cross-language chemical term table | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_glossary | /zh/glossary/ | zh | core_terminology | Controlled glossary chamber | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P0 |
| zh_sources | /zh/sources/ | zh | source_governance | Sources face localized | strict_registry | high | deferred_high_risk_review | multilingual_zh | P2 |
| zh_industrial_sulfur_systems | /zh/industrial-sulfur-systems/ | zh | core_terminology | Industrial systems vocabulary | strict_registry | medium | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_sodium_bisulfide | /zh/sodium-bisulfide/ | zh | core_terminology | Substance terminology high scrutiny | strict_registry | high | deferred_high_risk_review | multilingual_zh | P2 |
| zh_sulfur_safety_context | /zh/sulfur-safety-context/ | zh | core_terminology | Safety context non-manual | strict_registry | high | deferred_high_risk_review | multilingual_zh | P2 |
| zh_hydrogen_sulfide_risk | /zh/hydrogen-sulfide-risk/ | zh | core_terminology | H2S awareness terminology | strict_registry | high | deferred_high_risk_review | multilingual_zh | P2 |
| zh_sds_and_sulfur_terms | /zh/sds-and-sulfur-terms/ | zh | core_terminology | SDS naming vocabulary | strict_registry | high | deferred_high_risk_review | multilingual_zh | P2 |
| zh_disulfide_bonds | /zh/disulfide-bonds/ | zh | core_terminology | Disulfide bond terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_protein_disulfide_structure | /zh/protein-disulfide-structure/ | zh | core_terminology | Protein disulfide terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_molybdenum_disulfide | /zh/molybdenum-disulfide/ | zh | core_terminology | MoS2 vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_newsletter | /zh/newsletter/ | zh | utility | Newsletter surface localized | governance_meta | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_acquire | /zh/acquire/ | zh | utility | Acquisition inquiry localized | governance_meta | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_term_sulfate | /zh/terminology/sulfate/ | zh | core_terminology | Sulfate terminology localized | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_term_sulfite | /zh/terminology/sulfite/ | zh | core_terminology | Sulfite terminology localized | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_term_thiosulfate | /zh/terminology/thiosulfate/ | zh | core_terminology | Thiosulfate terminology localized | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_term_hydrogen_sulfide | /zh/terminology/hydrogen-sulfide/ | zh | core_terminology | H2S terminology localized | strict_registry | high | deferred_high_risk_review | multilingual_zh | P2 |
| zh_term_elemental_sulfur | /zh/terminology/elemental-sulfur/ | zh | core_terminology | Elemental sulfur forms vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_term_acid_gas | /zh/terminology/acid-gas/ | zh | core_terminology | Acid gas document vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_term_sour_crude | /zh/terminology/sour-crude/ | zh | core_terminology | Sour crude language only | strict_registry | high | deferred_high_risk_review | multilingual_zh | P2 |
| zh_term_claus | /zh/terminology/claus-sru/ | zh | core_terminology | Claus SRU vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_term_fgd | /zh/terminology/fgd/ | zh | core_terminology | FGD vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_term_mercaptan | /zh/terminology/mercaptan/ | zh | core_terminology | Mercaptan naming localized | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_term_sulfonic | /zh/terminology/sulfonic-acid/ | zh | core_terminology | Sulfonic acid naming localized | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_term_carbon_disulfide | /zh/terminology/carbon-disulfide/ | zh | core_terminology | CS2 localized | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_term_carbonyl_sulfide | /zh/terminology/carbonyl-sulfide/ | zh | core_terminology | COS localized | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_ind_filing_language | /zh/industrial/filing-language/ | zh | industrial_economic_interpretation | Filing sulfur language only | strict_registry | medium | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_ind_hs_code_language | /zh/industrial/hs-code-language/ | zh | industrial_economic_interpretation | Trade classification vocabulary not statistics | strict_registry | medium | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_method_corpus_map | /zh/reference/corpus-map/ | zh | methodology_reference | Localized corpus map hub | governance_meta | low | non_public_until_editorial_signoff | multilingual_zh | P1 |
| zh_method_translator_playbook | /zh/reference/translator-playbook/ | zh | methodology_reference | Localized translator playbook | governance_meta | low | non_public_until_editorial_signoff | multilingual_zh | P1 |
| zh_dis_bisulfite_wall | /zh/reference/bisulfite-wall/ | zh | disambiguation_authority | Bisulfite wall localized | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_gov_nomenclature | /zh/reference/nomenclature-governance/ | zh | source_governance | Nomenclature governance localized | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_core_na2s | /zh/terminology/sodium-sulfide/ | zh | core_terminology | Na2S salt naming localized | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_core_k2s | /zh/terminology/potassium-sulfide/ | zh | core_terminology | K2S naming localized | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_core_cas | /zh/terminology/calcium-sulfide/ | zh | core_terminology | CaS naming localized | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_core_fes | /zh/terminology/iron-sulfides/ | zh | core_terminology | Iron sulfides localized | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_core_cus | /zh/terminology/copper-sulfides/ | zh | core_terminology | Copper sulfides localized | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_core_zns | /zh/terminology/zinc-sulfide/ | zh | core_terminology | Zinc sulfide localized | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_core_pbs | /zh/terminology/lead-sulfide/ | zh | core_terminology | Lead sulfide localized | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_core_cds | /zh/terminology/cadmium-sulfide/ | zh | core_terminology | Cadmium sulfide localized | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_core_mos2 | /zh/terminology/molybdenum-disulfide/ | zh | core_terminology | MoS2 specialist localized | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_core_ws2 | /zh/terminology/tungsten-disulfide/ | zh | core_terminology | WS2 localized | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_core_h2s_aware | /zh/terminology/h2s-awareness/ | zh | core_terminology | H2S duplicate awareness localized | strict_registry | high | deferred_high_risk_review | multilingual_zh | P2 |
| zh_core_sulfur_allotropes | /zh/terminology/sulfur-allotropes/ | zh | core_terminology | Allotrope naming localized | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_core_sulfur_acid | /zh/terminology/sulfuric-acid/ | zh | core_terminology | Sulfuric acid terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_core_oleum | /zh/terminology/oleum/ | zh | core_terminology | Oleum terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_core_liquid_sulfur | /zh/terminology/liquid-sulfur/ | zh | core_terminology | Molten sulfur language non-handling | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_core_sulfur_recovery | /zh/terminology/sulfur-recovery/ | zh | core_terminology | Recovery terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_core_tail_gas | /zh/terminology/tail-gas/ | zh | core_terminology | Tail gas vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_core_amines_gas_treat | /zh/terminology/amines-gas-treating/ | zh | core_terminology | Amine treating vocabulary language | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_core_scavenger_terms | /zh/terminology/h2s-scavenger-terms/ | zh | core_terminology | Scavenger naming language | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_core_biogenic_lang | /zh/terminology/biogenic-sulfur-language/ | zh | core_terminology | Biogenic vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_core_vapor_pressure_lang | /zh/terminology/vapor-pressure-language/ | zh | core_terminology | Vapor pressure language only | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| ja_home | /ja/ | ja | gateway | Language gateway sovereign framing | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P0 |
| ja_what_is_bisulfid | /ja/what-is-bisulfid/ | ja | core_terminology | Canonical Bisulfid record in target language | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P0 |
| ja_what_is_sulfur | /ja/what-is-sulfur/ | ja | gateway | Sulfur gateway in target language | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_sulfur_compounds | /ja/sulfur-compounds/ | ja | gateway | Compounds map vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_sulfur_uses | /ja/sulfur-uses/ | ja | gateway | Uses framing vocabulary not market data | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_bisulfid_vs_bisulfide | /ja/bisulfid-vs-bisulfide/ | ja | de_en_chemical_language | Orthography boundary narrative | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_sulfid_vs_sulfide | /ja/sulfid-vs-sulfide/ | ja | de_en_chemical_language | Sulfid sulfide boundary | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_bisulfide_hydrosulfide_sulfide | /ja/bisulfide-hydrosulfide-sulfide/ | ja | disambiguation_authority | Triad disambiguation authority | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P0 |
| ja_german_english_chemical_terms | /ja/german-english-chemical-terms/ | ja | de_en_chemical_language | Cross-language chemical term table | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_glossary | /ja/glossary/ | ja | core_terminology | Controlled glossary chamber | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P0 |
| ja_sources | /ja/sources/ | ja | source_governance | Sources face localized | strict_registry | high | deferred_high_risk_review | multilingual_ja | P2 |
| ja_industrial_sulfur_systems | /ja/industrial-sulfur-systems/ | ja | core_terminology | Industrial systems vocabulary | strict_registry | medium | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_sodium_bisulfide | /ja/sodium-bisulfide/ | ja | core_terminology | Substance terminology high scrutiny | strict_registry | high | deferred_high_risk_review | multilingual_ja | P2 |
| ja_sulfur_safety_context | /ja/sulfur-safety-context/ | ja | core_terminology | Safety context non-manual | strict_registry | high | deferred_high_risk_review | multilingual_ja | P2 |
| ja_hydrogen_sulfide_risk | /ja/hydrogen-sulfide-risk/ | ja | core_terminology | H2S awareness terminology | strict_registry | high | deferred_high_risk_review | multilingual_ja | P2 |
| ja_sds_and_sulfur_terms | /ja/sds-and-sulfur-terms/ | ja | core_terminology | SDS naming vocabulary | strict_registry | high | deferred_high_risk_review | multilingual_ja | P2 |
| ja_disulfide_bonds | /ja/disulfide-bonds/ | ja | core_terminology | Disulfide bond terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_protein_disulfide_structure | /ja/protein-disulfide-structure/ | ja | core_terminology | Protein disulfide terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_molybdenum_disulfide | /ja/molybdenum-disulfide/ | ja | core_terminology | MoS2 vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_newsletter | /ja/newsletter/ | ja | utility | Newsletter surface localized | governance_meta | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_acquire | /ja/acquire/ | ja | utility | Acquisition inquiry localized | governance_meta | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_term_sulfate | /ja/terminology/sulfate/ | ja | core_terminology | Sulfate terminology localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_term_sulfite | /ja/terminology/sulfite/ | ja | core_terminology | Sulfite terminology localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_term_thiosulfate | /ja/terminology/thiosulfate/ | ja | core_terminology | Thiosulfate terminology localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_term_hydrogen_sulfide | /ja/terminology/hydrogen-sulfide/ | ja | core_terminology | H2S terminology localized | strict_registry | high | deferred_high_risk_review | multilingual_ja | P2 |
| ja_term_elemental_sulfur | /ja/terminology/elemental-sulfur/ | ja | core_terminology | Elemental sulfur forms vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_term_acid_gas | /ja/terminology/acid-gas/ | ja | core_terminology | Acid gas document vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_term_sour_crude | /ja/terminology/sour-crude/ | ja | core_terminology | Sour crude language only | strict_registry | high | deferred_high_risk_review | multilingual_ja | P2 |
| ja_term_claus | /ja/terminology/claus-sru/ | ja | core_terminology | Claus SRU vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_term_fgd | /ja/terminology/fgd/ | ja | core_terminology | FGD vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_term_mercaptan | /ja/terminology/mercaptan/ | ja | core_terminology | Mercaptan naming localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_term_sulfonic | /ja/terminology/sulfonic-acid/ | ja | core_terminology | Sulfonic acid naming localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_term_carbon_disulfide | /ja/terminology/carbon-disulfide/ | ja | core_terminology | CS2 localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_term_carbonyl_sulfide | /ja/terminology/carbonyl-sulfide/ | ja | core_terminology | COS localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_ind_filing_language | /ja/industrial/filing-language/ | ja | industrial_economic_interpretation | Filing sulfur language only | strict_registry | medium | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_ind_hs_code_language | /ja/industrial/hs-code-language/ | ja | industrial_economic_interpretation | Trade classification vocabulary not statistics | strict_registry | medium | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_method_corpus_map | /ja/reference/corpus-map/ | ja | methodology_reference | Localized corpus map hub | governance_meta | low | non_public_until_editorial_signoff | multilingual_ja | P1 |
| ja_method_translator_playbook | /ja/reference/translator-playbook/ | ja | methodology_reference | Localized translator playbook | governance_meta | low | non_public_until_editorial_signoff | multilingual_ja | P1 |
| ja_dis_bisulfite_wall | /ja/reference/bisulfite-wall/ | ja | disambiguation_authority | Bisulfite wall localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_gov_nomenclature | /ja/reference/nomenclature-governance/ | ja | source_governance | Nomenclature governance localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_core_na2s | /ja/terminology/sodium-sulfide/ | ja | core_terminology | Na2S salt naming localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_core_k2s | /ja/terminology/potassium-sulfide/ | ja | core_terminology | K2S naming localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_core_cas | /ja/terminology/calcium-sulfide/ | ja | core_terminology | CaS naming localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_core_fes | /ja/terminology/iron-sulfides/ | ja | core_terminology | Iron sulfides localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_core_cus | /ja/terminology/copper-sulfides/ | ja | core_terminology | Copper sulfides localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_core_zns | /ja/terminology/zinc-sulfide/ | ja | core_terminology | Zinc sulfide localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_core_pbs | /ja/terminology/lead-sulfide/ | ja | core_terminology | Lead sulfide localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_core_cds | /ja/terminology/cadmium-sulfide/ | ja | core_terminology | Cadmium sulfide localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_core_mos2 | /ja/terminology/molybdenum-disulfide/ | ja | core_terminology | MoS2 specialist localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_core_ws2 | /ja/terminology/tungsten-disulfide/ | ja | core_terminology | WS2 localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_core_h2s_aware | /ja/terminology/h2s-awareness/ | ja | core_terminology | H2S duplicate awareness localized | strict_registry | high | deferred_high_risk_review | multilingual_ja | P2 |
| ja_core_sulfur_allotropes | /ja/terminology/sulfur-allotropes/ | ja | core_terminology | Allotrope naming localized | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_core_sulfur_acid | /ja/terminology/sulfuric-acid/ | ja | core_terminology | Sulfuric acid terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_core_oleum | /ja/terminology/oleum/ | ja | core_terminology | Oleum terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_core_liquid_sulfur | /ja/terminology/liquid-sulfur/ | ja | core_terminology | Molten sulfur language non-handling | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_core_sulfur_recovery | /ja/terminology/sulfur-recovery/ | ja | core_terminology | Recovery terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_core_tail_gas | /ja/terminology/tail-gas/ | ja | core_terminology | Tail gas vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_core_amines_gas_treat | /ja/terminology/amines-gas-treating/ | ja | core_terminology | Amine treating vocabulary language | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_core_scavenger_terms | /ja/terminology/h2s-scavenger-terms/ | ja | core_terminology | Scavenger naming language | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_core_biogenic_lang | /ja/terminology/biogenic-sulfur-language/ | ja | core_terminology | Biogenic vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_core_vapor_pressure_lang | /ja/terminology/vapor-pressure-language/ | ja | core_terminology | Vapor pressure language only | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |

## Blueprint row count (Sprint 5A original table)

**Total proposed concepts (Sprint 5A table below):** 307

---

## Sprint 5H — 500-page standard and insufficiency of 307 concepts

The Sprint **5A** blueprint table contains **307** proposed reference page concepts. Under the Sprint **5H** strategic correction, **307 is insufficient** for the minimum **500-page sovereign launch cohort**.

| Gap | Detail |
| --- | --- |
| **Shortfall** | 500 − 307 = **193** concepts minimum required beyond the original table |
| **Owner standard** | First public launch requires **≥ 500** real governed pages (`CORPUS_LAUNCH_THRESHOLD.md`) |
| **This sprint** | Adds expansion register below; **does not** register routes in `routes.json` |

---

## 500-page launch cohort — layer allocation (planning)

| Strategic layer | Target pages | Notes |
| --- | ---: | --- |
| English global base layer | 95 | Gateway, EN spine, EN core terminology |
| German–English terminology layer | 55 | Bridge, orthography, crosswalk |
| German authority & lexical boundary layer | 70 | DE records, DE methodology |
| Arabic technical reference layer | 45 | AR hub + terminology |
| Chinese technical reference layer | 45 | ZH hub + terminology |
| Japanese technical reference layer | 45 | JP hub + precision language |
| Compound-family records | 40 | Sulfide, oxo-anion, organosulfur classes |
| Disambiguation authority pages | 25 | Triads, bisulfite wall, near-miss |
| Source & nomenclature governance | 20 | Citation, teaching boundary, policy |
| Methodology / reference system | 15 | Corpus ops, linking, Quality Gate |
| Index / map pages | 15 | Multilingual maps, cluster indexes |
| Industrial/economic interpretation (no market drift) | 20 | Document/process vocabulary |
| Documentation/compliance language (no legal/safety advice) | 10 | SDS-term framing, compliance language |
| **Total minimum launch cohort** | **500** | Floor for first public launch |

---

## Sprint 5H expansion register (193 additional concepts)

The following **193** proposed concepts extend the Sprint 5A table to **500** total blueprint rows. **None** are in `routes.json` until a future route-registration wave.

### EN terminology & compound-family expansion (+50)

| proposed_route_id | proposed_path | language | corpus_category | page_role | source_requirement_level | claim_risk_level | public_launch_eligibility | internal_linking_cluster | priority_level |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| en_term_sulfate_salts | /terminology/sulfate-salts/ | en | core_terminology | Sulfate salt naming vocabulary | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_sulfite_salts | /terminology/sulfite-salts/ | en | core_terminology | Sulfite salt naming vocabulary | strict_registry | medium | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_thiosulfate_salts | /terminology/thiosulfate-salts/ | en | core_terminology | Thiosulfate salt naming | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_polysulfide_salts | /terminology/polysulfide-salts/ | en | core_terminology | Polysulfide salt vocabulary | strict_registry | medium | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_alkyl_sulfides | /terminology/alkyl-sulfides/ | en | core_terminology | Alkyl sulfide class language | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_aryl_sulfides | /terminology/aryl-sulfides/ | en | core_terminology | Aryl sulfide class language | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_thioethers | /terminology/thioethers/ | en | core_terminology | Thioether naming vocabulary | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_thiols | /terminology/thiols/ | en | core_terminology | Thiol mercaptan naming | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_sulfenyl | /terminology/sulfenyl/ | en | core_terminology | Sulfenyl group vocabulary | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_sulfinyl | /terminology/sulfinyl/ | en | core_terminology | Sulfinyl group vocabulary | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_sulfonyl | /terminology/sulfonyl/ | en | core_terminology | Sulfonyl group vocabulary | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_sulfate_esters | /terminology/sulfate-esters/ | en | core_terminology | Sulfate ester naming | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_sulfonate_esters | /terminology/sulfonate-esters/ | en | core_terminology | Sulfonate ester naming | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_sulfur_dioxide | /terminology/sulfur-dioxide/ | en | core_terminology | SO2 terminology non-operational | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_sulfur_trioxide | /terminology/sulfur-trioxide/ | en | core_terminology | SO3 terminology non-operational | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_sulfuric_acid | /terminology/sulfuric-acid/ | en | core_terminology | Sulfuric acid naming vocabulary | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_fuming_sulfuric | /terminology/fuming-sulfuric-acid/ | en | core_terminology | Oleum fuming acid language | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_hydrogen_sulfide_aq | /terminology/hydrogen-sulfide-aqueous/ | en | core_terminology | Aqueous H2S naming non-manual | strict_registry | high | deferred_high_risk_review | terminology_spine | P2 |
| en_term_sulfide_minerals_index | /terminology/sulfide-minerals-index/ | en | index_map | Index of sulfide mineral vocabulary | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_nickel_sulfides | /terminology/nickel-sulfides/ | en | core_terminology | Nickel sulfide mineral vocabulary | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_cobalt_sulfides | /terminology/cobalt-sulfides/ | en | core_terminology | Cobalt sulfide vocabulary | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_manganese_sulfides | /terminology/manganese-sulfides/ | en | core_terminology | Manganese sulfide vocabulary | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_mercury_sulfides | /terminology/mercury-sulfides/ | en | core_terminology | Cinnabar etc vocabulary | strict_registry | medium | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_lead_sulfides | /terminology/lead-sulfides/ | en | core_terminology | Galena family vocabulary | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_zinc_sulfides | /terminology/zinc-sulfides/ | en | core_terminology | Sphalerite family vocabulary | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_copper_sulfides_extended | /terminology/copper-sulfides-extended/ | en | core_terminology | Extended chalcocite covellite vocabulary | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_iron_sulfides_extended | /terminology/iron-sulfides-extended/ | en | core_terminology | Extended pyrite marcasite vocabulary | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_antimony_sulfides | /terminology/antimony-sulfides/ | en | core_terminology | Stibnite family vocabulary | strict_registry | medium | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_arsenic_sulfides | /terminology/arsenic-sulfides/ | en | core_terminology | Orpiment realgar vocabulary | strict_registry | medium | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_molybdenum_sulfides | /terminology/molybdenum-sulfides/ | en | core_terminology | MoS2 MoS3 vocabulary | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_tungsten_sulfides | /terminology/tungsten-sulfides/ | en | core_terminology | WS2 vocabulary | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_tin_sulfides_extended | /terminology/tin-sulfides-extended/ | en | core_terminology | Tin sulfide vocabulary | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_silver_sulfides | /terminology/silver-sulfides/ | en | core_terminology | Argentite vocabulary | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_gold_sulfides | /terminology/gold-sulfides/ | en | core_terminology | Gold sulfide vocabulary | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_selenium_sulfides | /terminology/selenium-sulfides/ | en | core_terminology | Selenium sulfide vocabulary | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_tellurium_sulfides | /terminology/tellurium-sulfides/ | en | core_terminology | Tellurium sulfide vocabulary | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_phosphorus_sulfides | /terminology/phosphorus-sulfides/ | en | core_terminology | Phosphorus sulfide vocabulary | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_boron_sulfides | /terminology/boron-sulfides/ | en | core_terminology | Boron sulfide vocabulary | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_ammonium_sulfides | /terminology/ammonium-sulfides/ | en | core_terminology | Ammonium sulfide salt vocabulary | strict_registry | medium | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_calcium_sulfides | /terminology/calcium-sulfides/ | en | core_terminology | Calcium sulfide vocabulary | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_barium_sulfides | /terminology/barium-sulfides/ | en | core_terminology | Barium sulfide vocabulary | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_strontium_sulfides | /terminology/strontium-sulfides/ | en | core_terminology | Strontium sulfide vocabulary | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_lithium_sulfides | /terminology/lithium-sulfides/ | en | core_terminology | Lithium sulfide vocabulary | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_potassium_sulfides | /terminology/potassium-sulfides/ | en | core_terminology | Potassium sulfide vocabulary | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_sulfur_nitrogen_compounds | /terminology/sulfur-nitrogen-compounds/ | en | core_terminology | Sulfur-nitrogen class vocabulary | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_sulfur_halogens | /terminology/sulfur-halogen-compounds/ | en | core_terminology | Sulfur halide vocabulary | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_sulfur_oxygen_halides | /terminology/sulfur-oxyhalides/ | en | core_terminology | Thionyl sulfuryl vocabulary | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_sulfoximines | /terminology/sulfoximines/ | en | core_terminology | Sulfoximine class vocabulary | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_sulfilimines | /terminology/sulfilimines/ | en | core_terminology | Sulfilimine class vocabulary | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |
| en_term_sulfur_carbon_bonds | /terminology/sulfur-carbon-bond-language/ | en | core_terminology | S-C bond terminology | strict_registry | low | eligible_after_full_source_lock | terminology_spine | P2 |

### DE authority & lexical boundary expansion (+35)

| proposed_route_id | proposed_path | language | corpus_category | page_role | source_requirement_level | claim_risk_level | public_launch_eligibility | internal_linking_cluster | priority_level |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| de_term_bisulfit | /de/terminology/bisulfit/ | de | core_terminology | Bisulfit DE terminology record | strict_registry | medium | eligible_after_full_source_lock | multilingual_de | P1 |
| de_term_disulfit | /de/terminology/disulfit/ | de | core_terminology | Disulfit DE terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_term_polysulfid | /de/terminology/polysulfid/ | de | core_terminology | Polysulfid DE terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_term_sulfat | /de/terminology/sulfat/ | de | core_terminology | Sulfat DE terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_term_sulfit | /de/terminology/sulfit/ | de | core_terminology | Sulfit DE terminology | strict_registry | medium | eligible_after_full_source_lock | multilingual_de | P1 |
| de_term_thiosulfat | /de/terminology/thiosulfat/ | de | core_terminology | Thiosulfat DE terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_term_schwefelsaeure | /de/terminology/schwefelsaeure/ | de | core_terminology | Schwefelsäure vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_term_schwefelwasserstoff | /de/terminology/schwefelwasserstoff/ | de | core_terminology | H2S DE naming non-manual | strict_registry | high | deferred_high_risk_review | multilingual_de | P2 |
| de_term_natriumsulfid | /de/terminology/natriumsulfid/ | de | core_terminology | Natriumsulfid vocabulary | strict_registry | medium | eligible_after_full_source_lock | multilingual_de | P1 |
| de_term_eisensulfid | /de/terminology/eisensulfid/ | de | core_terminology | Eisensulfid mineral vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_term_kupfersulfid | /de/terminology/kupfersulfid/ | de | core_terminology | Kupfersulfid vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_term_zinksulfid | /de/terminology/zinksulfid/ | de | core_terminology | Zinksulfid vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_term_bleisulfid | /de/terminology/bleisulfid/ | de | core_terminology | Bleisulfid vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_term_molybdaensulfid | /de/terminology/molybdansulfid/ | de | core_terminology | MoS2 DE vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_term_wolframsulfid | /de/terminology/wolframsulfid/ | de | core_terminology | WS2 DE vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_term_kohlenstoffdisulfid | /de/terminology/kohlenstoffdisulfid/ | de | core_terminology | CS2 DE vocabulary | strict_registry | medium | eligible_after_full_source_lock | multilingual_de | P1 |
| de_term_mercaptan | /de/terminology/mercaptan/ | de | core_terminology | Mercaptan/thiol DE vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_term_sulfonyl | /de/terminology/sulfonyl/ | de | core_terminology | Sulfonyl DE vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_term_sulfoxid | /de/terminology/sulfoxid/ | de | core_terminology | Sulfoxid DE vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_term_sulfonsaeure | /de/terminology/sulfonsaeure/ | de | core_terminology | Sulfonsäure class DE | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_gov_claim_boundary | /de/reference/claim-boundary/ | de | source_governance | DE claim boundary explainer | strict_registry | low | non_public_until_editorial_signoff | multilingual_de | P2 |
| de_gov_source_locking | /de/reference/source-locking/ | de | source_governance | DE source-locking primer | strict_registry | low | non_public_until_editorial_signoff | multilingual_de | P2 |
| de_method_editorial_standards | /de/reference/editorial-standards/ | de | methodology_reference | DE editorial standards | governance_meta | low | non_public_until_editorial_signoff | multilingual_de | P2 |
| de_index_terminology_map | /de/reference/terminology-map/ | de | index_map | DE terminology cluster map | governance_meta | low | non_public_until_hreflang_wiring | multilingual_de | P2 |
| de_index_disambiguation_map | /de/reference/disambiguation-map/ | de | index_map | DE disambiguation index | governance_meta | low | non_public_until_hreflang_wiring | multilingual_de | P2 |
| de_industrial_claus_vocab | /de/industrial/claus-vocabulary/ | de | industrial_economic_interpretation | Claus SRU DE document language | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P2 |
| de_industrial_fgd_vocab | /de/industrial/fgd-vocabulary/ | de | industrial_economic_interpretation | FGD DE document language | strict_registry | medium | eligible_after_full_source_lock | multilingual_de | P2 |
| de_industrial_supply_doc | /de/industrial/supply-document-language/ | de | industrial_economic_interpretation | Supply doc DE vocabulary no stats | strict_registry | medium | eligible_after_full_source_lock | multilingual_de | P2 |
| de_compliance_sds_terms | /de/compliance/sds-term-language/ | de | documentation_compliance | SDS DE term language non-manual | strict_registry | high | deferred_high_risk_review | multilingual_de | P2 |
| de_compliance_regulatory_lang | /de/compliance/regulatory-language/ | de | documentation_compliance | Regulatory language framing only | strict_registry | medium | eligible_after_full_source_lock | multilingual_de | P2 |
| de_dis_bisulfid_bisulfite | /de/reference/bisulfid-bisulfit-wall/ | de | disambiguation_authority | Bisulfid vs Bisulfit DE wall | strict_registry | medium | eligible_after_full_source_lock | multilingual_de | P1 |
| de_dis_sulfid_sulfat | /de/reference/sulfid-sulfat-boundary/ | de | disambiguation_authority | Sulfid vs Sulfat boundary | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P2 |
| de_dis_hydrosulfid | /de/reference/hydrosulfid-boundary/ | de | disambiguation_authority | Hydrosulfid naming boundary | strict_registry | medium | eligible_after_full_source_lock | multilingual_de | P2 |
| de_bridge_en_de_suffix | /de/reference/suffix-bridge/ | de | de_en_chemical_language | -id/-ide suffix bridge DE | strict_registry | low | eligible_after_full_source_lock | multilingual_de | P1 |
| de_bridge_iupac_de | /de/reference/iupac-de-boundary/ | de | de_en_chemical_language | IUPAC DE boundary non-normative | strict_registry | medium | eligible_after_full_source_lock | multilingual_de | P1 |

### Arabic technical reference expansion (+30)

| proposed_route_id | proposed_path | language | corpus_category | page_role | source_requirement_level | claim_risk_level | public_launch_eligibility | internal_linking_cluster | priority_level |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ar_hub_terminology | /ar/reference/terminology-hub/ | ar | index_map | AR terminology hub | governance_meta | low | non_public_until_hreflang_wiring | multilingual_ar | P1 |
| ar_core_sulfide | /ar/terminology/sulfide/ | ar | core_terminology | Sulfide AR terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_core_bisulfide | /ar/terminology/bisulfide/ | ar | core_terminology | Bisulfide AR terminology | strict_registry | medium | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_core_hydrosulfide | /ar/terminology/hydrosulfide/ | ar | core_terminology | Hydrosulfide AR terminology | strict_registry | medium | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_core_disulfide | /ar/terminology/disulfide/ | ar | core_terminology | Disulfide AR terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_core_sulfate | /ar/terminology/sulfate/ | ar | core_terminology | Sulfate AR terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_core_sulfite | /ar/terminology/sulfite/ | ar | core_terminology | Sulfite AR terminology | strict_registry | medium | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_core_hydrogen_sulfide | /ar/terminology/hydrogen-sulfide/ | ar | core_terminology | H2S AR naming non-manual | strict_registry | high | deferred_high_risk_review | multilingual_ar | P2 |
| ar_core_elemental_sulfur | /ar/terminology/elemental-sulfur/ | ar | core_terminology | Elemental sulfur AR | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_core_sulfuric_acid | /ar/terminology/sulfuric-acid/ | ar | core_terminology | Sulfuric acid AR vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_core_iron_sulfide | /ar/terminology/iron-sulfide/ | ar | core_terminology | Iron sulfide AR vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_core_copper_sulfide | /ar/terminology/copper-sulfide/ | ar | core_terminology | Copper sulfide AR vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_core_zinc_sulfide | /ar/terminology/zinc-sulfide/ | ar | core_terminology | Zinc sulfide AR vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_core_mos2 | /ar/terminology/molybdenum-disulfide/ | ar | core_terminology | MoS2 AR vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_gov_source_policy | /ar/reference/source-policy/ | ar | source_governance | AR source policy face | strict_registry | low | non_public_until_editorial_signoff | multilingual_ar | P2 |
| ar_gov_nomenclature | /ar/reference/nomenclature/ | ar | source_governance | AR nomenclature discipline | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P2 |
| ar_method_translator | /ar/reference/translator-playbook/ | ar | methodology_reference | AR translator playbook | strict_registry | low | non_public_until_editorial_signoff | multilingual_ar | P2 |
| ar_index_corpus_map | /ar/reference/corpus-map/ | ar | index_map | AR corpus map | governance_meta | low | non_public_until_hreflang_wiring | multilingual_ar | P2 |
| ar_industrial_claus | /ar/industrial/claus-vocabulary/ | ar | industrial_economic_interpretation | Claus AR document language | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P2 |
| ar_industrial_sour_gas | /ar/industrial/sour-gas-language/ | ar | industrial_economic_interpretation | Sour gas AR vocabulary non-operational | strict_registry | high | deferred_high_risk_review | multilingual_ar | P2 |
| ar_industrial_refinery | /ar/industrial/refinery-sulfur-language/ | ar | industrial_economic_interpretation | Refinery sulfur doc language | strict_registry | medium | eligible_after_full_source_lock | multilingual_ar | P2 |
| ar_dis_bisulfite_wall | /ar/reference/bisulfite-wall/ | ar | disambiguation_authority | Bisulfite wall AR | strict_registry | medium | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_dis_sulfide_sulfite | /ar/reference/sulfide-sulfite-boundary/ | ar | disambiguation_authority | Sulfide sulfite AR boundary | strict_registry | medium | eligible_after_full_source_lock | multilingual_ar | P2 |
| ar_bridge_en_ar | /ar/reference/en-ar-bridge/ | ar | multilingual_terminology_control | EN-AR terminology bridge | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_bridge_de_ar | /ar/reference/de-ar-bridge/ | ar | multilingual_terminology_control | DE-AR terminology bridge | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P2 |
| ar_compliance_sds_lang | /ar/compliance/sds-term-language/ | ar | documentation_compliance | SDS AR term language non-manual | strict_registry | high | deferred_high_risk_review | multilingual_ar | P2 |
| ar_compliance_trade_docs | /ar/compliance/trade-document-language/ | ar | documentation_compliance | Trade doc AR vocabulary no stats | strict_registry | medium | eligible_after_full_source_lock | multilingual_ar | P2 |
| ar_nav_reference_index | /ar/reference/navigation-index/ | ar | index_map | AR internal reference navigation | governance_meta | low | non_public_until_hreflang_wiring | multilingual_ar | P2 |
| ar_term_thiosulfate | /ar/terminology/thiosulfate/ | ar | core_terminology | Thiosulfate AR terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |
| ar_term_polysulfide | /ar/terminology/polysulfide/ | ar | core_terminology | Polysulfide AR terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_ar | P1 |

### Chinese technical reference expansion (+30)

| proposed_route_id | proposed_path | language | corpus_category | page_role | source_requirement_level | claim_risk_level | public_launch_eligibility | internal_linking_cluster | priority_level |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| zh_hub_terminology | /zh/reference/terminology-hub/ | zh | index_map | ZH terminology hub | governance_meta | low | non_public_until_hreflang_wiring | multilingual_zh | P1 |
| zh_core_sulfide | /zh/terminology/sulfide/ | zh | core_terminology | Sulfide ZH terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_core_bisulfide | /zh/terminology/bisulfide/ | zh | core_terminology | Bisulfide ZH terminology | strict_registry | medium | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_core_hydrosulfide | /zh/terminology/hydrosulfide/ | zh | core_terminology | Hydrosulfide ZH terminology | strict_registry | medium | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_core_disulfide | /zh/terminology/disulfide/ | zh | core_terminology | Disulfide ZH terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_core_sulfate | /zh/terminology/sulfate/ | zh | core_terminology | Sulfate ZH terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_core_sulfite | /zh/terminology/sulfite/ | zh | core_terminology | Sulfite ZH terminology | strict_registry | medium | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_core_hydrogen_sulfide | /zh/terminology/hydrogen-sulfide/ | zh | core_terminology | H2S ZH naming non-manual | strict_registry | high | deferred_high_risk_review | multilingual_zh | P2 |
| zh_core_elemental_sulfur | /zh/terminology/elemental-sulfur/ | zh | core_terminology | Elemental sulfur ZH | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_core_sulfuric_acid | /zh/terminology/sulfuric-acid/ | zh | core_terminology | Sulfuric acid ZH vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_core_iron_sulfide | /zh/terminology/iron-sulfide/ | zh | core_terminology | Iron sulfide ZH vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_core_copper_sulfide | /zh/terminology/copper-sulfide/ | zh | core_terminology | Copper sulfide ZH vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_core_zinc_sulfide | /zh/terminology/zinc-sulfide/ | zh | core_terminology | Zinc sulfide ZH vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_core_mos2 | /zh/terminology/molybdenum-disulfide/ | zh | core_terminology | MoS2 ZH vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_gov_source_policy | /zh/reference/source-policy/ | zh | source_governance | ZH source policy face | strict_registry | low | non_public_until_editorial_signoff | multilingual_zh | P2 |
| zh_gov_nomenclature | /zh/reference/nomenclature/ | zh | source_governance | ZH nomenclature discipline | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P2 |
| zh_method_translator | /zh/reference/translator-playbook/ | zh | methodology_reference | ZH translator playbook | strict_registry | low | non_public_until_editorial_signoff | multilingual_zh | P2 |
| zh_index_corpus_map | /zh/reference/corpus-map/ | zh | index_map | ZH corpus map | governance_meta | low | non_public_until_hreflang_wiring | multilingual_zh | P2 |
| zh_industrial_claus | /zh/industrial/claus-vocabulary/ | zh | industrial_economic_interpretation | Claus ZH document language | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P2 |
| zh_industrial_fgd | /zh/industrial/fgd-vocabulary/ | zh | industrial_economic_interpretation | FGD ZH document language | strict_registry | medium | eligible_after_full_source_lock | multilingual_zh | P2 |
| zh_industrial_battery_lang | /zh/industrial/battery-sulfur-language/ | zh | industrial_economic_interpretation | Battery sector sulfur doc language | strict_registry | medium | eligible_after_full_source_lock | multilingual_zh | P2 |
| zh_dis_bisulfite_wall | /zh/reference/bisulfite-wall/ | zh | disambiguation_authority | Bisulfite wall ZH | strict_registry | medium | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_dis_sulfide_sulfite | /zh/reference/sulfide-sulfite-boundary/ | zh | disambiguation_authority | Sulfide sulfite ZH boundary | strict_registry | medium | eligible_after_full_source_lock | multilingual_zh | P2 |
| zh_bridge_en_zh | /zh/reference/en-zh-bridge/ | zh | multilingual_terminology_control | EN-ZH terminology bridge | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_compliance_sds_lang | /zh/compliance/sds-term-language/ | zh | documentation_compliance | SDS ZH term language non-manual | strict_registry | high | deferred_high_risk_review | multilingual_zh | P2 |
| zh_compliance_customs_docs | /zh/compliance/customs-document-language/ | zh | documentation_compliance | Customs doc ZH vocabulary | strict_registry | medium | eligible_after_full_source_lock | multilingual_zh | P2 |
| zh_nav_reference_index | /zh/reference/navigation-index/ | zh | index_map | ZH internal reference navigation | governance_meta | low | non_public_until_hreflang_wiring | multilingual_zh | P2 |
| zh_term_thiosulfate | /zh/terminology/thiosulfate/ | zh | core_terminology | Thiosulfate ZH terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_term_polysulfide | /zh/terminology/polysulfide/ | zh | core_terminology | Polysulfide ZH terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_zh | P1 |
| zh_term_carbon_disulfide | /zh/terminology/carbon-disulfide/ | zh | core_terminology | CS2 ZH vocabulary | strict_registry | medium | eligible_after_full_source_lock | multilingual_zh | P2 |

### Japanese technical reference expansion (+30)

| proposed_route_id | proposed_path | language | corpus_category | page_role | source_requirement_level | claim_risk_level | public_launch_eligibility | internal_linking_cluster | priority_level |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ja_hub_terminology | /ja/reference/terminology-hub/ | ja | index_map | JA terminology hub | governance_meta | low | non_public_until_hreflang_wiring | multilingual_ja | P1 |
| ja_core_sulfide | /ja/terminology/sulfide/ | ja | core_terminology | Sulfide JA terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_core_bisulfide | /ja/terminology/bisulfide/ | ja | core_terminology | Bisulfide JA terminology | strict_registry | medium | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_core_hydrosulfide | /ja/terminology/hydrosulfide/ | ja | core_terminology | Hydrosulfide JA terminology | strict_registry | medium | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_core_disulfide | /ja/terminology/disulfide/ | ja | core_terminology | Disulfide JA terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_core_sulfate | /ja/terminology/sulfate/ | ja | core_terminology | Sulfate JA terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_core_sulfite | /ja/terminology/sulfite/ | ja | core_terminology | Sulfite JA terminology | strict_registry | medium | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_core_hydrogen_sulfide | /ja/terminology/hydrogen-sulfide/ | ja | core_terminology | H2S JA naming non-manual | strict_registry | high | deferred_high_risk_review | multilingual_ja | P2 |
| ja_core_elemental_sulfur | /ja/terminology/elemental-sulfur/ | ja | core_terminology | Elemental sulfur JA | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_core_sulfuric_acid | /ja/terminology/sulfuric-acid/ | ja | core_terminology | Sulfuric acid JA vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_core_iron_sulfide | /ja/terminology/iron-sulfide/ | ja | core_terminology | Iron sulfide JA vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_core_copper_sulfide | /ja/terminology/copper-sulfide/ | ja | core_terminology | Copper sulfide JA vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_core_zinc_sulfide | /ja/terminology/zinc-sulfide/ | ja | core_terminology | Zinc sulfide JA vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_core_mos2 | /ja/terminology/molybdenum-disulfide/ | ja | core_terminology | MoS2 JA vocabulary | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_gov_source_policy | /ja/reference/source-policy/ | ja | source_governance | JA source policy face | strict_registry | low | non_public_until_editorial_signoff | multilingual_ja | P2 |
| ja_gov_nomenclature | /ja/reference/nomenclature/ | ja | source_governance | JA nomenclature discipline | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P2 |
| ja_method_translator | /ja/reference/translator-playbook/ | ja | methodology_reference | JA translator playbook | strict_registry | low | non_public_until_editorial_signoff | multilingual_ja | P2 |
| ja_index_corpus_map | /ja/reference/corpus-map/ | ja | index_map | JA corpus map | governance_meta | low | non_public_until_hreflang_wiring | multilingual_ja | P2 |
| ja_industrial_claus | /ja/industrial/claus-vocabulary/ | ja | industrial_economic_interpretation | Claus JA document language | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P2 |
| ja_industrial_semiconductor | /ja/industrial/semiconductor-sulfur-language/ | ja | industrial_economic_interpretation | Semiconductor sulfur doc language | strict_registry | medium | eligible_after_full_source_lock | multilingual_ja | P2 |
| ja_industrial_battery_lang | /ja/industrial/battery-sulfur-language/ | ja | industrial_economic_interpretation | Battery sulfur doc language JA | strict_registry | medium | eligible_after_full_source_lock | multilingual_ja | P2 |
| ja_dis_bisulfite_wall | /ja/reference/bisulfite-wall/ | ja | disambiguation_authority | Bisulfite wall JA | strict_registry | medium | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_dis_sulfide_sulfite | /ja/reference/sulfide-sulfite-boundary/ | ja | disambiguation_authority | Sulfide sulfite JA boundary | strict_registry | medium | eligible_after_full_source_lock | multilingual_ja | P2 |
| ja_bridge_en_ja | /ja/reference/en-ja-bridge/ | ja | multilingual_terminology_control | EN-JA terminology bridge | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_compliance_sds_lang | /ja/compliance/sds-term-language/ | ja | documentation_compliance | SDS JA term language non-manual | strict_registry | high | deferred_high_risk_review | multilingual_ja | P2 |
| ja_compliance_export_docs | /ja/compliance/export-document-language/ | ja | documentation_compliance | Export doc JA vocabulary | strict_registry | medium | eligible_after_full_source_lock | multilingual_ja | P2 |
| ja_nav_reference_index | /ja/reference/navigation-index/ | ja | index_map | JA internal reference navigation | governance_meta | low | non_public_until_hreflang_wiring | multilingual_ja | P2 |
| ja_term_thiosulfate | /ja/terminology/thiosulfate/ | ja | core_terminology | Thiosulfate JA terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_term_polysulfide | /ja/terminology/polysulfide/ | ja | core_terminology | Polysulfide JA terminology | strict_registry | low | eligible_after_full_source_lock | multilingual_ja | P1 |
| ja_term_iupac_ja_boundary | /ja/reference/iupac-ja-boundary/ | ja | de_en_chemical_language | IUPAC JA boundary non-normative | strict_registry | medium | eligible_after_full_source_lock | multilingual_ja | P1 |

### Disambiguation, governance, index & industrial expansion (+18)

| proposed_route_id | proposed_path | language | corpus_category | page_role | source_requirement_level | claim_risk_level | public_launch_eligibility | internal_linking_cluster | priority_level |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| en_dis_sulfate_sulfite | /reference/sulfate-sulfite-boundary/ | en | disambiguation_authority | Sulfate vs sulfite boundary | strict_registry | medium | eligible_after_full_source_lock | disambiguation | P2 |
| en_dis_thiosulfate_sulfite | /reference/thiosulfate-sulfite-boundary/ | en | disambiguation_authority | Thiosulfate vs sulfite boundary | strict_registry | medium | eligible_after_full_source_lock | disambiguation | P2 |
| en_dis_sulfide_sulfite | /reference/sulfide-sulfite-boundary/ | en | disambiguation_authority | Sulfide vs sulfite boundary | strict_registry | medium | eligible_after_full_source_lock | disambiguation | P2 |
| en_dis_hydrogen_sulfide_hydrosulfide | /reference/h2s-hydrosulfide-boundary/ | en | disambiguation_authority | H2S vs hydrosulfide naming | strict_registry | high | deferred_high_risk_review | disambiguation | P2 |
| en_dis_carbon_disulfide_bisulfide | /reference/cs2-bisulfide-boundary/ | en | disambiguation_authority | CS2 vs bisulfide family boundary | strict_registry | medium | eligible_after_full_source_lock | disambiguation | P2 |
| en_gov_claim_registry_explainer | /reference/claim-registry-explainer/ | en | source_governance | How claim registries work | governance_meta | low | non_public_until_registry_activation | governance | P2 |
| en_gov_ontology_governance | /reference/ontology-governance/ | en | source_governance | Ontology governance primer | strict_registry | low | non_public_until_registry_activation | governance | P2 |
| en_gov_hreflang_policy | /reference/hreflang-policy/ | en | methodology_reference | hreflang governance explainer | governance_meta | low | non_public_until_hreflang_wiring | governance | P2 |
| en_index_terminology_spine | /reference/terminology-spine-map/ | en | index_map | Terminology spine index | governance_meta | low | non_public_until_link_wiring | index_map | P2 |
| en_index_disambiguation_map | /reference/disambiguation-map/ | en | index_map | Disambiguation cluster index | governance_meta | low | non_public_until_link_wiring | index_map | P2 |
| en_index_multilingual_map | /reference/multilingual-layer-map/ | en | index_map | Multilingual layer overview | governance_meta | low | non_public_until_hreflang_wiring | index_map | P2 |
| en_nav_internal_reference | /reference/internal-navigation/ | en | index_map | Internal reference navigation guide | governance_meta | low | non_public_until_link_wiring | index_map | P2 |
| en_industrial_vessel_sulfur_lang | /industrial/vessel-sulfur-language/ | en | industrial_economic_interpretation | Vessel sulfur doc vocabulary | strict_registry | medium | eligible_after_full_source_lock | industrial_interpretation | P2 |
| en_industrial_mining_sulfur_lang | /industrial/mining-sulfur-language/ | en | industrial_economic_interpretation | Mining sulfur doc vocabulary | strict_registry | medium | eligible_after_full_source_lock | industrial_interpretation | P2 |
| en_industrial_pharma_sulfur_lang | /industrial/pharma-sulfur-language/ | en | industrial_economic_interpretation | Pharma sulfur doc vocabulary non-medical | strict_registry | medium | eligible_after_full_source_lock | industrial_interpretation | P2 |
| en_compliance_export_doc_lang | /compliance/export-document-language/ | en | documentation_compliance | Export doc sulfur vocabulary | strict_registry | medium | eligible_after_full_source_lock | industrial_interpretation | P2 |
| en_compliance_customs_sulfur_lang | /compliance/customs-sulfur-language/ | en | documentation_compliance | Customs sulfur doc language | strict_registry | medium | eligible_after_full_source_lock | industrial_interpretation | P2 |
| en_compliance_reach_language | /compliance/reach-document-language/ | en | documentation_compliance | REACH doc language framing only | strict_registry | medium | eligible_after_full_source_lock | industrial_interpretation | P2 |

---

## Total blueprint row count (Sprint 5A + Sprint 5H expansion)

| Register | Concepts |
| --- | ---: |
| Sprint 5A original table | 307 |
| Sprint 5H expansion register | 193 |
| **Total proposed concepts** | **500** |

**Publication readiness:** **Not ready for publication.** Blueprint only. **No** `routes.json` modifications in Sprint 5H.

**Recommended next sprint:** Route registration wave 1 (80–120 planned routes from blueprint priority rows) — see `CORPUS_PRODUCTION_WAVE_MODEL.md`.

---

*Sprint 5H blueprint revision — 500-page minimum launch cohort. No registry edits.*
