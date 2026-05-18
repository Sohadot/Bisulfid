# Route Implementation Readiness Matrix — Launch Cohort Batch 1 (Sprint 5C)

## Purpose

This matrix classifies each of the **55** `proposed_route_id` values in `LAUNCH_COHORT_IMPLEMENTATION_BATCH_1.md` by **implementation readiness**. It does **not** modify `routes.json`, claim registries, or content.

## Readiness groups

| Group | Meaning |
| --- | --- |
| **ready_for_route_planning** | Safe to add as **planned** `route_id` rows with outlines next—minimal merge/source blockers beyond normal editorial signoff. |
| **needs_source_mapping_before_route** | Do not treat drafts as authoritative until each factual claim class maps to **`source_registry.json`** rows per `SOURCE_POLICY.md`. |
| **needs_claim_boundary_before_route** | Requires an explicit **outline + forbidden-claims list** (no market, procurement, operations, safety instructions, medical claims) before substantive drafting—typically industrial-language pages. |
| **needs_merge_or_scope_adjustment** | Editorial scope overlaps another page or a deferred blueprint row; align titles/claims **before** batch scale-out. |
| **defer_until_later_corpus_phase** | Still in Batch 1 **plan**, but intended for work **after** infrastructure wiring (hreflang, ontology activation, *etc.*). |

**Content risk level:** `low` / `medium` / `high` — editorial hazard if published without extra gates (not a prediction that Sprint 5C publishes anything).

---

## Matrix (55 concepts)

| route_id | readiness classification | reason | required source category | required claim group | content risk level | route dependency | internal-linking dependency | next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| home | ready_for_route_planning | Governance-meta gateway; chemistry facts minimal if scoped to hub role. | editorial_policy; optional_element_intro_sources | none_meta (policy-scoped) | low | None | Spins: gateway, terminology_spine hub edges | Approve hub outline; reserve Interactive Term Map linkage for future sprint. |
| what_is_sulfur | needs_source_mapping_before_route | Gateway chemistry claims need locked sources. | IUPAC_element; introductory_general_chemistry | science_claims; terminology_claims | low | None | Links to element record + gateway cluster | Map element basics to registry rows before draft expansion. |
| sulfur_compounds | needs_source_mapping_before_route | Taxonomy/overview statements need citations. | introductory_general_chemistry; nomenclature | terminology_claims; science_claims | low | `what_is_sulfur` outline stable | Bridge to triad + terminology_spine | Source-map class boundaries for sulfide family language. |
| sulfur_uses | needs_claim_boundary_before_route | Industrial uses tempt market/ops claims—outline must forbid stats and advice. | sector_docs_language_only | industry_claims (bounded) | medium | Gateway trio coherence | Bridge to `industrial_sulfur_systems` | Publish editor “allowed / forbidden” clause list before drafting body. |
| what_is_bisulfid | needs_source_mapping_before_route | Thesis page; every chemical assertion needs registry support. | nomenclature; authoritative_general_chemistry | terminology_claims | medium | `bisulfid` record planned | de_en_bridge cluster | Lock EN sources before DE mirror work. |
| bisulfid_vs_bisulfide | needs_source_mapping_before_route | Orthography + usage claims need evidence. | nomenclature; lexicography_reference | terminology_claims | medium | `what_is_bisulfid` | de_en_bridge | Select citation set for DE/EN spelling boundaries. |
| sulfid_vs_sulfide | needs_source_mapping_before_route | Language comparison requires governed sources. | nomenclature; german_english_reference | terminology_claims | low | EN/DE pair alignment | de_en_bridge | Pair with `de_sulfid_vs_sulfide` source plan. |
| bisulfide_hydrosulfide_sulfide | needs_source_mapping_before_route | Disambiguation is citation-sensitive. | nomenclature; inorganic_chemistry_reference | terminology_claims | medium | `hydrosulfide` scope | disambiguation | Define triad vs future H₂S operational pages (deferred). |
| german_english_chemical_terms | needs_source_mapping_before_route | Table rows imply factual equivalences—each needs support or “usage-only” labeling. | german_english_reference; nomenclature | terminology_claims | low | `bisulfid_vs_bisulfide` | de_en_bridge | Build per-row source or “document usage” disclaimer pattern. |
| glossary | needs_source_mapping_before_route | Term listings must track `sulfur_terms.json` verification—no Sprint 5C ontology edits. | ontology-backed_terms | terminology_claims | low | Ontology workflow later | terminology_spine | Define glossary row template + link depth minimums. |
| sources | ready_for_route_planning | Page is meta; value depends on populated registry, not page chemistry facts. | n/a until registry populated | none_meta | low | `source_registry.json` rows | governance cluster | Add planned route only after registry population schedule agreed. |
| bisulfid | needs_source_mapping_before_route | New `route_id` must be registered in a future sprint; content is high-authority. | nomenclature | terminology_claims | medium | `what_is_bisulfid` narrative | terminology_spine | Register route in planning sprint; map claims before draft. |
| sulfid | needs_source_mapping_before_route | Same as `bisulfid` for Germanic “Sulfid” anchor. | nomenclature | terminology_claims | low | `sulfid_vs_sulfide` | terminology_spine | Register + source-map before DE expansion references. |
| hydrosulfide | needs_source_mapping_before_route | Must stay naming-only; keep away from safety manual overlap. | nomenclature | terminology_claims | medium | `bisulfide_hydrosulfide_sulfide` locked | terminology_spine | Explicit boundary memo vs deferred H₂S safety pages. |
| corpus_methodology_overview | ready_for_route_planning | Editorial process page—S-meta discipline. | doctrine_corpus_docs | none_meta | low | None | governance | Editorial signoff on process statements. |
| nomenclature_governance_overview | needs_source_mapping_before_route | Nomenclature assertions cite external authorities. | nomenclature; policy_secondary | terminology_claims | low | `SOURCE_POLICY.md` alignment | governance | Map policy examples to sources. |
| multilingual_corpus_map | defer_until_later_corpus_phase | Requires `hreflang` + group registry strategy first. | editorial_policy; multilingual_doctrine | none_meta | low | `hreflang_groups.json` design | index_map | Complete hreflang policy sprint; then route planning. |
| translator_playbook_bisulfide_family | needs_source_mapping_before_route | Translation guidance still cites term facts. | nomenclature; german_english_reference | terminology_claims | low | EN bridge pages stable | governance | Align playbook rules with `de_method_translator_playbook`. |
| citation_discipline_primer | needs_source_mapping_before_route | Examples must not fabricate citations—tie to real registry IDs when illustrated. | registry_operational_docs | terminology_claims (light) | low | `sources` page plan | governance | Create example citation IDs in registry or use redacted placeholders per policy. |
| academic_teaching_source_boundary | needs_source_mapping_before_route | Teaching vs normative boundary examples need careful sourcing. | policy; education_reference | terminology_claims | low | `SOURCE_POLICY.md` | governance | Lock worked examples with source rows. |
| bisulfite_wall_explainer | needs_merge_or_scope_adjustment | Paired with DE bisulfite wall; 5B merge discipline. | nomenclature | terminology_claims | medium | `de_dis_bisulfite_wall` | disambiguation | Single scope doc for TE pair before drafting. |
| internal_linking_discipline | ready_for_route_planning | Methodology meta page. | doctrine_corpus_docs | none_meta | low | None | governance | Sign off outline; link to `internal_links.json` policy only by route_id mentions. |
| quality_gate_public_explainer | ready_for_route_planning | Process explainer; owner review gate. | QUALITY_GATE.md; PROJECT_DOCTRINE | none_meta | low | None | governance | Owner review of public-facing Quality Gate wording. |
| ontology_alignment_primer | defer_until_later_corpus_phase | Depends on ontology registry activation posture. | ontology_docs | terminology_claims | low | `sulfur_terms.json` workflow | governance | Run ontology governance sprint; then route planning + sources. |
| sulfur_element_term_record | needs_source_mapping_before_route | Term record density requires citations. | IUPAC_element; nomenclature | terminology_claims | low | `what_is_sulfur` | terminology_spine | Minimum section checklist per anti-thin rules. |
| sulfide_anion_term_record | needs_source_mapping_before_route | Anion naming and boundary claims. | inorganic_chemistry_reference | terminology_claims | medium | triad page | terminology_spine | Source-map redox-related sentences carefully. |
| disulfide_bonds | needs_source_mapping_before_route | Biochem bridge—avoid medical claims. | biochemistry_reference | science_claims; terminology_claims | low | protein page coordination | terminology_spine | Boundary doc: structure vocabulary only. |
| protein_disulfide_structure | needs_source_mapping_before_route | Same boundary as disulfide bonds. | biochemistry_reference | science_claims; terminology_claims | low | `disulfide_bonds` | terminology_spine | No clinical or therapeutic framing in outline. |
| sulfate_terminology | needs_source_mapping_before_route | Oxoanion nomenclature. | nomenclature | terminology_claims | low | sulfite/thiosulfate ordering | terminology_spine | Sequence internal links for oxo-anion ladder. |
| sulfite_terminology | needs_source_mapping_before_route | High collision risk with bisulfite wall—coordinate links only. | nomenclature | terminology_claims | medium | `bisulfite_wall_explainer` | terminology_spine | Cross-link discipline with disambiguation pages. |
| thiosulfate_terminology | needs_source_mapping_before_route | Requires clear separation from sulfate/sulfite ladder sources. | nomenclature | terminology_claims | low | sulfate/sulfite pages planned | terminology_spine | Source thiosulfate naming authorities early. |
| polysulfide_terminology | needs_source_mapping_before_route | Advanced naming—avoid thin list. | inorganic_chemistry_reference | terminology_claims | medium | `sulfane_chain_language` | terminology_spine | Co-draft outlines to prevent duplication. |
| sulfane_chain_language | needs_source_mapping_before_route | Chain nomenclature sources required. | nomenclature | terminology_claims | low | `polysulfide_terminology` | terminology_spine | Define non-operational scope statement. |
| sulfonic_acid_class_language | needs_source_mapping_before_route | Organosulfur class naming. | nomenclature | terminology_claims | low | sulfoxide/sulfone ordering | terminology_spine | Anti-generic: tie to Bisulfid thesis usage contexts. |
| sulfoxide_sulfone_language | needs_source_mapping_before_route | Oxidation state language—citation discipline. | nomenclature | terminology_claims | low | sulfonic page | terminology_spine | Keep definitions narrow; avoid reaction advice. |
| sodium_sulfide_salts_language | needs_claim_boundary_before_route | Na₂S chemistry naming slips into handling—outline forbids it. | inorganic_chemistry_reference | terminology_claims | medium | deferred substance safety pages | terminology_spine | Explicit “language-only” editor contract. |
| iron_sulfides_mineral_language | needs_source_mapping_before_route | Mineral names / forms vocabulary. | mineralogy_reference | terminology_claims | low | defer other mineral grids | terminology_spine | Cap scope to named mineral vocabulary subset. |
| molybdenum_disulfide | needs_merge_or_scope_adjustment | 5B: consolidate MoS₂/WS₂ overlap; WS₂ deferred from Batch 1. | materials_science_reference | industry_claims (bounded) | medium | deferred `tungsten_disulfide_terms` | industrial_interpretation | Editorial merge note: one EN hub now; WS₂ later fold-in. |
| industrial_sulfur_systems | needs_claim_boundary_before_route | Industrial systems language without market claims. | sector_docs_language_only | industry_claims (bounded) | medium | gateway industrial bridge | industrial_interpretation | Outline forbids procurement and production runbooks. |
| economic_document_language_sulfur | needs_claim_boundary_before_route | Filings vocabulary—ban numeric market assertions. | corporate_disclosure_language | industry_claims (bounded) | medium | `industrial_sulfur_systems` context | industrial_interpretation | Forbidden patterns list: CAGR, share, targets. |
| supply_chain_vocabulary_sulfur | needs_claim_boundary_before_route | Logistics terms—no trade route / tariff claims as facts. | logistics_document_language | industry_claims (bounded) | medium | economic doc language pairing | industrial_interpretation | Define “term-only” examples without data. |
| claus_process_vocabulary | needs_claim_boundary_before_route | Refinery terms—no operating procedures. | process_engineering_reference | industry_claims (bounded) | medium | hydrotreating ordering optional | industrial_interpretation | SRU vocabulary scope sheet for editors. |
| fgd_document_language | needs_claim_boundary_before_route | Environmental doc terms—no compliance advice. | environmental_reference | industry_claims (bounded) | medium | claus/energy docs separation | industrial_interpretation | Compliance/legal advice out of scope statement. |
| hydrotreating_desulfurization_terms | needs_claim_boundary_before_route | Hydrotreating jargon—no catalyst tuning advice. | refinery_process_reference | industry_claims (bounded) | medium | claus page cross-links | industrial_interpretation | Catalyst/ops claims explicitly banned in outline. |
| de_home | needs_source_mapping_before_route | DE gateway facts still require sources despite identity framing. | german_gateway_reference | terminology_claims | low | EN `home` thesis alignment | multilingual_de | Decide gateway strict_registry vs meta split in routing spec. |
| de_what_is_bisulfid | needs_source_mapping_before_route | DE thesis record—must follow EN lock order. | nomenclature; german_english_reference | terminology_claims | low | EN `what_is_bisulfid` source lock | multilingual_de | Source-lock EN first; then DE authorities. |
| de_bisulfide_hydrosulfide_sulfide | needs_source_mapping_before_route | Triad must mirror EN boundaries exactly. | nomenclature | terminology_claims | low | EN triad locked | multilingual_de | Bilingual boundary diff review before public draft. |
| de_glossary | needs_source_mapping_before_route | Same ontology dependency as EN glossary. | ontology-backed_terms | terminology_claims | low | EN glossary pattern | multilingual_de | Human editorial pass—no MT-only publication path. |
| de_german_english_chemical_terms | needs_source_mapping_before_route | Crosswalk table requires per-row governance. | german_english_reference | terminology_claims | low | EN crosswalk | multilingual_de | Match row semantics to EN column governance. |
| de_bisulfid_vs_bisulfide | needs_source_mapping_before_route | High-intent DE page—sources required. | nomenclature | terminology_claims | low | EN counterpart | multilingual_de | Parallel citation strategy with EN page. |
| de_sulfid_vs_sulfide | needs_source_mapping_before_route | Identity layer in DE—sources required. | nomenclature | terminology_claims | low | EN counterpart | multilingual_de | Same as above. |
| de_dis_bisulfite_wall | needs_merge_or_scope_adjustment | Must align with EN bisulfite explainer scope. | nomenclature | terminology_claims | medium | `bisulfite_wall_explainer` | multilingual_de | Joint EN/DE scope agreement before drafting. |
| de_gov_nomenclature | needs_source_mapping_before_route | Localized governance cites must be language-appropriate. | nomenclature; policy_secondary | terminology_claims | low | `nomenclature_governance_overview` | multilingual_de | Avoid English-only authority masquerading as DE norm. |
| de_method_corpus_map | ready_for_route_planning | Methodology meta; DE localization of process. | doctrine_corpus_docs | none_meta | low | EN methodology posture | multilingual_de | Editorial signoff on localized process statements. |
| de_method_translator_playbook | ready_for_route_planning | Playbook meta alignment—pair with EN governance sprint. | doctrine_corpus_docs; nomenclature (illustrative only) | terminology_claims (light) | low | `translator_playbook_bisulfide_family` | multilingual_de | Ensure EN/DE playbook rules do not contradict. |

---

## Summary counts

| Readiness group | Count (Batch 1) |
| --- | ---: |
| ready_for_route_planning | 7 |
| needs_source_mapping_before_route | 35 |
| needs_claim_boundary_before_route | 8 |
| needs_merge_or_scope_adjustment | 3 |
| defer_until_later_corpus_phase | 2 |

*Note: Counts sum to **55**. `molybdenum_disulfide` is classified under **needs_merge_or_scope_adjustment** (MoS₂/WS₂ editorial consolidation per Sprint 5B); drafting still uses **needs_claim_boundary_before_route** discipline—the matrix lists one primary classification per row.*

---

*Sprint 5C — readiness planning only.*
