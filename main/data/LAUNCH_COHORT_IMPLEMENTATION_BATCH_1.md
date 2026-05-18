# Launch Cohort Implementation Batch 1 (Sprint 5C)

## Why Sprint 5C exists

Sprint **5A** defined the sovereign reference corpus architecture and a **307-row** launch-cohort blueprint. Sprint **5B** concluded that blueprint is a **strong scaffold** but **not** sufficient to ship a **300-page** governed launch cohort *as-is*. Sprint **5C** converts architecture + quality findings into a **single, governed first implementation batch**: **which** route concepts move through routing and content work **next**, under what **source**, **claim**, **linking**, and **multilingual** rules—**without** registering routes, **without** drafting public pages, and **without** publication.

## Relationship to Sprint 5A architecture

Batch 1 tracks **Sprint 5A** layers and categories: **gateway**, **DE/EN chemical language**, **disambiguation authority**, **core terminology** (controlled records—not thin glossaries), **methodology / reference system**, **source governance**, **index/map** infrastructure, and a **narrow** set of **industrial economic interpretation** pages that are **document-language** only (no market statistics, procurement, or operational prescriptions). All row semantics align with `SOVEREIGN_REFERENCE_CORPUS_ARCHITECTURE.md`, `CORPUS_LAUNCH_THRESHOLD.md`, and `CORPUS_EXPANSION_MODEL.md`.

## Relationship to Sprint 5B quality review

Selections follow **`LAUNCH_COHORT_REFINEMENT_RECOMMENDATIONS.md`**: **EN + narrow DE spine** first; **no** `newsletter` / `acquire` in the **reference** batch; **no** `ar` / `zh` / `ja` mirrors until **EN+DE** source-locking and **hreflang** design; **no** mass registration of **high-risk safety** pages in this batch (SDS/H₂S handling, sodium bisulfide substance pages, sour-gas operational framing, *etc.*—deferred or handled in a dedicated safety sprint). **Merge pressure** called out in 5B (H₂S family, MoS₂/WS₂) is **not** resolved here; Batch 1 **scopes** MoS₂ as the **English hub** page and **defers** separate `tungsten_disulfide_terms` and duplicate DE material pages to later corpus phases (see rejected/deferred logic).

## Why this is not direct creation of 300 pages

The **300-page** threshold remains the **minimum launch cohort** target for the **sovereign reference** layer. Batch 1 deliberately caps **55** concepts so editors can **prove** depth, citation discipline, and internal-link density before scaling. Implementing **all** blueprint rows at once would recreate the **thin-page and translation-spam** risks 5B flagged.

## Why this is not publication

This document is **strategy and precedence only**. It does **not** change `routes.json`, **does not** create `content_file` bodies, **does not** toggle `indexable` or `in_sitemap`, and **does not** activate claim registries. **Publication readiness** remains **negative** until Quality Gate conditions in doctrine are met.

## Selected implementation batch count

**55** proposed route concepts: **44** English (`en`), **11** German (`de`).

---

## Rejected / deferred concept logic (for this batch)

Explicitly **excluded** from Batch 1 (remain in the longer blueprint for later phases):

| Bucket | Examples / rule |
| --- | --- |
| **Utility / non-reference** | `newsletter`, `acquire` (all locales)—valid product routes but **not** counted toward the **300 sovereign reference** pages. |
| **Mirrored locales** | All `ar_*`, `zh_*`, `ja_*` blueprint rows—**deferred** until EN+DE source spine + **hreflang** per `MULTILINGUAL_POLICY.md`. |
| **High-risk safety / substance operations** | e.g. `hydrogen_sulfide_risk`, `sodium_bisulfide`, `sulfur_safety_context`, `sds_and_sulfur_terms`, `sour_gas_document_language`, `hydrogen_sulfide_term_record`, most DE `de_*` safety/Na₂S analogs—require **dedicated** boundary, sourcing, and editorial review before routing. |
| **Breadth / P3 mineral & specialty** | e.g. `frasch_process_vocabulary`, `arsenic_antimony_sulfides_language`, `tin_sulfides_terms`, `silver_gold_sulfides_terms`, `contact_process_vocabulary`, `tungsten_disulfide_terms`, `zinc_lead_sulfides_language`, `copper_sulfides_language`—**deferred** to avoid thin coverage; **WS₂** merged editorially with MoS₂ **language hub** in a later pass (per 5B). |
| **DE gateway breadth (trim)** | `de_what_is_sulfur`, `de_sulfur_compounds`, `de_sulfur_uses`, large `de_term_*` / `de_core_*` grids—**deferred** to Batch 2+ so Batch 1 stays within **40–55** total and preserves **editorial depth** on the DE identity core. |
| **Carbon sulfur small-molecule trio (trim)** | `carbon_disulfide_terms`, `carbonyl_sulfide_terms`, `mercaptan_class_language`—deferred to Batch 2 after sulfate family density is validated. |

---

## Internal linking logic

- **Gateway cluster** (`gateway`): `home`, English public gateway trio (`what_is_sulfur`, `sulfur_compounds`, `sulfur_uses`) links **down** to DE/EN bridge and terminology spine—**no** raw URL literals in copy; use `route_id` targets when `internal_links.json` is updated in a **future** routing sprint.
- **DE/EN bridge** (`de_en_bridge`): `what_is_bisulfid`, `bisulfid_vs_bisulfide`, `sulfid_vs_sulfide`, `german_english_chemical_terms` cross-link bidirectionally with `disambiguation` and core **Bisulfid** / **Sulfid** records.
- **Disambiguation** (`disambiguation`): `bisulfide_hydrosulfide_sulfide`, `bisulfite_wall_explainer`, paired **DE** `de_dis_bisulfite_wall`—must cite nomenclature governance and never collapse **bisulfite** into **bisulfide** claims.
- **Terminology spine** (`terminology_spine`): element + anion records, oxo-anion family (`sulfate` … `polysulfide`, `sulfane`), selected organosulfur class pages (`sulfonic`, `sulfoxide_sulfone`), `sodium_sulfide_salts_language`, `iron_sulfides_mineral_language`, `disulfide_bonds`, `protein_disulfide_structure`, standalone **`bisulfid`**, **`sulfid`**, **`hydrosulfide`**, **`glossary`**—each page lists **boundary** (“what this page does not claim”) and **related terms** edges.
- **Governance** (`governance`): `sources`, `nomenclature_governance_overview`, `citation_discipline_primer`, `academic_teaching_source_boundary`, **`de_gov_nomenclature`**, methodology docs.
- **Methodology / reference** (`methodology_reference`, `index_map`): `corpus_methodology_overview`, `translator_playbook_bisulfide_family`, `internal_linking_discipline`, `quality_gate_public_explainer`, `ontology_alignment_primer`, `multilingual_corpus_map`, **`de_method_*`**—tie pages to `SOURCE_POLICY.md` and the Quality Gate; many remain **non-public** until signoff or registry wiring.
- **Industrial interpretation** (`industrial_interpretation`): **language-only** exposure to Claus/FGD/hydrotreating and **document** vocabulary (`economic_document_language_sulfur`, `supply_chain_vocabulary_sulfur`, `industrial_sulfur_systems`)—**must not** introduce CAGR, market share, procurement lists, production instructions, or trade statistics.
- **Multilingual DE hub** (`multilingual_de`): **`de_home`** anchors **`de_what_is_bisulfid`**, **`de_glossary`**, triad and orthography pages, **governance** mirrors—future expansion reuses the same cluster ids.

---

## Source governance logic

- **`strict_registry`**: no public-tier factual statement without a **governed** row in `main/data/sources/source_registry.json` per `doctrine/SOURCE_POLICY.md`. Teaching sources remain **candidate-only** for normative claims.
- **`governance_meta`**: editorial/process pages—claims are **about** governance, not chemistry facts; still **no** fabricated citations.
- Multilingual: **DE** pages require **German-accessible** authority or explicit “term-only” scope where English sources are cited for **crosswalk**, not as a substitute for native-language review in later phases.
- **`[SOURCE REQUIRED]`** markers on existing drafts stay until replaced by registry-backed notes—**never** remove markers in service of tone.

---

## Claim governance logic

- All claim JSON registries remain **`inactive`** until an explicit **activation** sprint. Batch 1 pages still declare **expected** claim families (`terminology_claims`, `science_claims`, `industry_claims`) for future `routes.json` alignment—**no** `status: approved` claims.
- **High linguistic risk** pages (industrial language, disambiguation) get **explicit** `required_claim_groups` scoping in a **future** routing sprint—no free-form market or safety claims.
- **Safety / medical / handling / dosage** claims are **out of scope** for Batch 1 copy.

---

## Multilingual governance logic

- **Phase applied in Batch 1:** **EN** (44) + **DE** identity slice (11). **No** `ar` / `zh` / `ja`.
- **DE** paths in this plan follow the **blueprint** English-slug style for **planning continuity**; **locale-native** URL policy must be resolved in **`MULTILINGUAL_POLICY.md`** work **before** publication—not before **planning**.
- **Machine translation** alone is **disallowed** for public tier; Batch 1 DE selections are the minimum set expected to receive **human** editorial alignment with EN hubs.
- **`multilingual_corpus_map`** stays **planning** until **hreflang** groups and `hreflang_groups.json` strategy are executed.

---

## Anti-thin-content logic

Every terminology-oriented page in Batch 1 must be scoped as a **controlled record** or **methodology** article with: **scope**, **boundaries**, **non-claims**, **source posture**, **related terms**, and **planned internal links**—**not** a bare glossary list. List-only stubs **fail** Batch 1 intent.

---

## Anti-generic-content logic

Each page must **anchor** to the Bisulfid thesis: **German–English chemical language**, **bisulfide/sulfide family**, **disambiguation**, or **corpus governance**. Generic “intro to chemistry” tone without thesis linkage is **out of scope**.

---

## Publication readiness conclusion

**Not ready for publication.** Batch 1 is an **implementation batch plan** only. No route is published; no page is indexed; no claim is approved; the **300-page** launch threshold is **unchanged** and **not** weakened—only **sequenced**.

---

## Recommended next sprint

**Sprint 5D (suggested):** (“Route registration & internal graph slice”)—after leadership accepts this batch:

1. Register **Batch 1** `route_id` values in `routes.json` **still as `planned`** with `indexable: false`, `in_sitemap: false`.
2. Update `internal_links.json` with **route_id-only** edges for the clusters above—no raw external URLs in policy-violating ways.
3. Begin **non-public** English drafts for **P0–P1** terminology and DE/EN bridge only; defer industrial language until bridge quality is signed off.
4. Run **`CORPUS_ROUTE_BLUEPRINT_LAUNCH_COHORT.md` v2** merge pass for H₂S and MoS₂/WS₂ duplication **before** scaling to Batch 2 breadth.

---

## Selected route concepts

**Implementation status** for every row: **`planned_for_future_route_addition`** (not present in `routes.json` unless already pre-existing from earlier sprints—no Sprint 5C registry edits).

**Standard prerequisites (abbreviated in table):**

- **Src lock (`S-strict`)**: Map each factual statement to `source_registry.json` before public tier; teaching sources remain non-normative unless upgraded.
- **Src lock (`S-meta`)**: Governance/editorial claims only; no chemistry fact assertions without sources.
- **Claim pre (`C-inactive`)**: Claim registries stay **inactive**; drafts use descriptive, bounded language until activation sprint.
- **Claim pre (`C-boundary`)**: Document `required_claim_groups` and forbidden patterns (no market/safety/procurement) before substantive industry-language drafting.

### English (`en`) — 44 concepts

| proposed_route_id | proposed_path | language | corpus_category | page_role | source_requirement_level | claim_risk_level | implementation_status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| home | `/` | en | gateway | Primary gateway; hub of the internal link graph; Interactive Term Map host. | governance_meta | low | planned_for_future_route_addition |
| what_is_sulfur | `/what-is-sulfur/` | en | gateway | Public gateway entry: element introduction, industrial relevance framing, safety **context** only. | strict_registry | low | planned_for_future_route_addition |
| sulfur_compounds | `/sulfur-compounds/` | en | gateway | Bridge from gateway to terminology sulfide family. | strict_registry | low | planned_for_future_route_addition |
| sulfur_uses | `/sulfur-uses/` | en | gateway | Uses framing without market statistics. | strict_registry | low | planned_for_future_route_addition |
| what_is_bisulfid | `/what-is-bisulfid/` | en | de_en_chemical_language | Core Bisulfid branded terminology record (center concept). | strict_registry | medium | planned_for_future_route_addition |
| bisulfid_vs_bisulfide | `/bisulfid-vs-bisulfide/` | en | de_en_chemical_language | Orthography and search-intent boundary page. | strict_registry | medium | planned_for_future_route_addition |
| sulfid_vs_sulfide | `/sulfid-vs-sulfide/` | en | de_en_chemical_language | German **Sulfid** vs English sulfide family boundary. | strict_registry | low | planned_for_future_route_addition |
| bisulfide_hydrosulfide_sulfide | `/bisulfide-hydrosulfide-sulfide/` | en | disambiguation_authority | Triad disambiguation: hydrosulfide vs sulfide vs bisulfide naming. | strict_registry | medium | planned_for_future_route_addition |
| german_english_chemical_terms | `/german-english-chemical-terms/` | en | de_en_chemical_language | Cross-language chemical term crosswalk. | strict_registry | low | planned_for_future_route_addition |
| glossary | `/glossary/` | en | core_terminology | Ontology-driven glossary hub (`sulfur_terms.json` linkage planned). | strict_registry | low | planned_for_future_route_addition |
| sources | `/sources/` | en | source_governance | Public bibliography face driven by source registry. | governance_meta | low | planned_for_future_route_addition |
| bisulfid | `/bisulfid/` | en | core_terminology | Standalone Bisulfid lexical record (pending future route registration). | strict_registry | medium | planned_for_future_route_addition |
| sulfid | `/sulfid/` | en | core_terminology | Standalone Germanic **Sulfid** record (pending future route registration). | strict_registry | low | planned_for_future_route_addition |
| hydrosulfide | `/hydrosulfide/` | en | core_terminology | English hydrosulfide label complement to triad page. | strict_registry | medium | planned_for_future_route_addition |
| corpus_methodology_overview | `/reference/corpus-methodology/` | en | methodology_reference | How Bisulfid authors sovereign reference pages. | governance_meta | low | planned_for_future_route_addition |
| nomenclature_governance_overview | `/reference/nomenclature-governance/` | en | source_governance | Nomenclature discipline tied to `SOURCE_POLICY.md`. | strict_registry | low | planned_for_future_route_addition |
| multilingual_corpus_map | `/reference/multilingual-corpus-map/` | en | index_map | Multilingual hub index (non-thin); hreflang-gated. | governance_meta | low | planned_for_future_route_addition |
| translator_playbook_bisulfide_family | `/reference/translator-playbook-bisulfide-family/` | en | methodology_reference | Controlled DE/EN translator playbook. | strict_registry | low | planned_for_future_route_addition |
| citation_discipline_primer | `/reference/citation-discipline/` | en | source_governance | How citations surface from `source_registry.json`. | strict_registry | low | planned_for_future_route_addition |
| academic_teaching_source_boundary | `/reference/academic-teaching-source-boundary/` | en | source_governance | Teaching reference limits per policy. | strict_registry | low | planned_for_future_route_addition |
| bisulfite_wall_explainer | `/reference/bisulfite-wall/` | en | disambiguation_authority | Bisulfite vs bisulfide family boundary explainer. | strict_registry | medium | planned_for_future_route_addition |
| internal_linking_discipline | `/reference/internal-linking-discipline/` | en | methodology_reference | Cluster and density rules for editors. | governance_meta | low | planned_for_future_route_addition |
| quality_gate_public_explainer | `/reference/quality-gate/` | en | methodology_reference | Quality Gate expectations for readers/editors. | governance_meta | low | planned_for_future_route_addition |
| ontology_alignment_primer | `/reference/ontology-alignment-primer/` | en | methodology_reference | How `sulfur_terms.json` ties to pages—registry-gated. | strict_registry | low | planned_for_future_route_addition |
| sulfur_element_term_record | `/terminology/sulfur-element/` | en | core_terminology | Canonical elemental sulfur terminology record. | strict_registry | low | planned_for_future_route_addition |
| sulfide_anion_term_record | `/terminology/sulfide-anion/` | en | core_terminology | Sulfide anion terminology record. | strict_registry | medium | planned_for_future_route_addition |
| disulfide_bonds | `/disulfide-bonds/` | en | core_terminology | Disulfide bridge terminology (biochem/materials bridge). | strict_registry | low | planned_for_future_route_addition |
| protein_disulfide_structure | `/protein-disulfide-structure/` | en | core_terminology | Protein disulfide structure vocabulary—no medical advice. | strict_registry | low | planned_for_future_route_addition |
| sulfate_terminology | `/terminology/sulfate/` | en | core_terminology | Sulfate naming vocabulary. | strict_registry | low | planned_for_future_route_addition |
| sulfite_terminology | `/terminology/sulfite/` | en | core_terminology | Sulfite family vocabulary (separate from bisulfide). | strict_registry | medium | planned_for_future_route_addition |
| thiosulfate_terminology | `/terminology/thiosulfate/` | en | core_terminology | Thiosulfate terminology record. | strict_registry | low | planned_for_future_route_addition |
| polysulfide_terminology | `/terminology/polysulfide/` | en | core_terminology | Polysulfide terminology record. | strict_registry | medium | planned_for_future_route_addition |
| sulfane_chain_language | `/terminology/sulfane/` | en | core_terminology | Sulfane chain nomenclature language. | strict_registry | low | planned_for_future_route_addition |
| sulfonic_acid_class_language | `/terminology/sulfonic-acid-class/` | en | core_terminology | Sulfonic acid class naming. | strict_registry | low | planned_for_future_route_addition |
| sulfoxide_sulfone_language | `/terminology/sulfoxide-sulfone/` | en | core_terminology | Sulfoxide / sulfone naming. | strict_registry | low | planned_for_future_route_addition |
| sodium_sulfide_salts_language | `/terminology/sodium-sulfide-salts/` | en | core_terminology | Na₂S-family naming disambiguation—**language**, not handling. | strict_registry | medium | planned_for_future_route_addition |
| iron_sulfides_mineral_language | `/terminology/iron-sulfides/` | en | core_terminology | Pyrite/pyrrhotite **language** subset. | strict_registry | low | planned_for_future_route_addition |
| molybdenum_disulfide | `/molybdenum-disulfide/` | en | industrial_economic_interpretation | MoS₂ vocabulary hub; WS₂ overlap merged in a later editorial pass. | strict_registry | low | planned_for_future_route_addition |
| industrial_sulfur_systems | `/industrial-sulfur-systems/` | en | industrial_economic_interpretation | Industrial systems vocabulary—no market share/CAGR. | strict_registry | medium | planned_for_future_route_addition |
| economic_document_language_sulfur | `/reference/economic-document-language-sulfur/` | en | industrial_economic_interpretation | Filings/sector document **language** only. | strict_registry | medium | planned_for_future_route_addition |
| supply_chain_vocabulary_sulfur | `/reference/supply-chain-vocabulary-sulfur/` | en | industrial_economic_interpretation | Logistics document vocabulary—**no** trade stats. | strict_registry | medium | planned_for_future_route_addition |
| claus_process_vocabulary | `/industrial/claus-process-vocabulary/` | en | industrial_economic_interpretation | SRU Claus **terminology**—no runbooks. | strict_registry | low | planned_for_future_route_addition |
| fgd_document_language | `/industrial/fgd-document-language/` | en | industrial_economic_interpretation | FGD document vocabulary—non-operational. | strict_registry | medium | planned_for_future_route_addition |
| hydrotreating_desulfurization_terms | `/industrial/hydrotreating-desulfurization-terms/` | en | industrial_economic_interpretation | Refinery desulfurization **terms**—no tuning advice. | strict_registry | medium | planned_for_future_route_addition |

### German (`de`) — 11 concepts

| proposed_route_id | proposed_path | language | corpus_category | page_role | source_requirement_level | claim_risk_level | implementation_status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| de_home | `/de/` | de | gateway | German language gateway / sovereign framing. | strict_registry | low | planned_for_future_route_addition |
| de_what_is_bisulfid | `/de/what-is-bisulfid/` | de | core_terminology | Canonical Bisulfid record in German. | strict_registry | low | planned_for_future_route_addition |
| de_bisulfide_hydrosulfide_sulfide | `/de/bisulfide-hydrosulfide-sulfide/` | de | disambiguation_authority | Triad disambiguation authority in German. | strict_registry | low | planned_for_future_route_addition |
| de_glossary | `/de/glossary/` | de | core_terminology | Controlled German glossary chamber. | strict_registry | low | planned_for_future_route_addition |
| de_german_english_chemical_terms | `/de/german-english-chemical-terms/` | de | de_en_chemical_language | DE/EN chemical term table (identity layer). | strict_registry | low | planned_for_future_route_addition |
| de_bisulfid_vs_bisulfide | `/de/bisulfid-vs-bisulfide/` | de | de_en_chemical_language | Orthography and boundary narrative in German. | strict_registry | low | planned_for_future_route_addition |
| de_sulfid_vs_sulfide | `/de/sulfid-vs-sulfide/` | de | de_en_chemical_language | **Sulfid** vs sulfide boundary in German. | strict_registry | low | planned_for_future_route_addition |
| de_dis_bisulfite_wall | `/de/reference/bisulfite-wall/` | de | disambiguation_authority | Bisulfite wall localized—must stay aligned with EN explainer. | strict_registry | low | planned_for_future_route_addition |
| de_gov_nomenclature | `/de/reference/nomenclature-governance/` | de | source_governance | Nomenclature governance localized. | strict_registry | low | planned_for_future_route_addition |
| de_method_corpus_map | `/de/reference/corpus-map/` | de | methodology_reference | Localized corpus map hub—editorial signoff gated. | governance_meta | low | planned_for_future_route_addition |
| de_method_translator_playbook | `/de/reference/translator-playbook/` | de | methodology_reference | Localized translator playbook—editorial signoff gated. | governance_meta | low | planned_for_future_route_addition |

---

## Full specification per selected concept

**Legend — source-locking prerequisite:** **S-strict** = every public-tier chemistry fact maps to `main/data/sources/source_registry.json` per `SOURCE_POLICY.md`. **S-meta** = governance/editorial claims only (process/how-we-work).

**Legend — claim approval prerequisite:** **C-inactive** = claim JSON registries remain **inactive**; drafts stay descriptive. **C-inactive+boundary** = same, plus written outline forbids market figures, procurement, operations, safety instructions, medical claims.

Below, **implementation_status** is always **`planned_for_future_route_addition`**.

### English — specification table (part 1 of 2)

| proposed_route_id | proposed_path | language | corpus_category | page_role | source_requirement_level | claim_risk_level | source_locking_prerequisite | claim_approval_prerequisite | internal_linking_cluster | dependency_notes | priority_level | inclusion_rationale | public_launch_eligibility | implementation_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| home | `/` | en | gateway | Primary gateway / Interactive Term Map hub. | governance_meta | low | S-meta | C-inactive | gateway | Needs aligned gateway copy with `what_is_bisulfid` hub when routed. | P1 | Establishes the public entry and link graph anchor for the sovereign corpus. | eligible_after_full_source_lock | planned_for_future_route_addition |
| what_is_sulfur | `/what-is-sulfur/` | en | gateway | Element intro; safety context only, no advice. | strict_registry | low | S-strict | C-inactive | gateway | Feeds terminology spine; avoid operational thresholds. | P1 | Core reader on-ramp; governs tone for gateway layer. | eligible_after_full_source_lock | planned_for_future_route_addition |
| sulfur_compounds | `/sulfur-compounds/` | en | gateway | Bridge into sulfide / bisulfide family. | strict_registry | low | S-strict | C-inactive | gateway | Links to `bisulfide_hydrosulfide_sulfide` and term records. | P1 | Connects gateway layer to the sulfur compounds map. | eligible_after_full_source_lock | planned_for_future_route_addition |
| sulfur_uses | `/sulfur-uses/` | en | gateway | Uses framing without market statistics. | strict_registry | low | S-strict | C-inactive+boundary | gateway | Must not introduce CAGR/share/procurement lists. | P1 | Industrial relevance without market-intelligence claims. | eligible_after_full_source_lock | planned_for_future_route_addition |
| what_is_bisulfid | `/what-is-bisulfid/` | en | de_en_chemical_language | Center Bisulfid terminology / thesis record. | strict_registry | medium | S-strict | C-inactive | de_en_bridge | Depends on consistent naming with `bisulfid` standalone record. | P0 | Brand-center page for the asset thesis. | eligible_after_full_source_lock | planned_for_future_route_addition |
| bisulfid_vs_bisulfide | `/bisulfid-vs-bisulfide/` | en | de_en_chemical_language | DE/EN orthography + search boundary. | strict_registry | medium | S-strict | C-inactive | de_en_bridge | Cross-links `german_english_chemical_terms` and triad. | P1 | High-intent editorial authority for spelling family. | eligible_after_full_source_lock | planned_for_future_route_addition |
| sulfid_vs_sulfide | `/sulfid-vs-sulfide/` | en | de_en_chemical_language | **Sulfid** vs sulfide boundary. | strict_registry | low | S-strict | C-inactive | de_en_bridge | Pairs with DE mirror; supports identity layer. | P1 | German identity argument; reduces generic confusion. | eligible_after_full_source_lock | planned_for_future_route_addition |
| bisulfide_hydrosulfide_sulfide | `/bisulfide-hydrosulfide-sulfide/` | en | disambiguation_authority | Triad disambiguation (naming precision). | strict_registry | medium | S-strict | C-inactive | disambiguation | Foundation for `hydrosulfide` record; no handling claims. | P0 | Disambiguation spine; prevents conflation errors. | eligible_after_full_source_lock | planned_for_future_route_addition |
| german_english_chemical_terms | `/german-english-chemical-terms/` | en | de_en_chemical_language | Cross-language chemical crosswalk. | strict_registry | low | S-strict | C-inactive | de_en_bridge | Table density must avoid thin-list-only pages. | P1 | Operationalizes DE/EN bridge thesis. | eligible_after_full_source_lock | planned_for_future_route_addition |
| glossary | `/glossary/` | en | core_terminology | Ontology-driven glossary hub. | strict_registry | low | S-strict | C-inactive | terminology_spine | Future ties to verified `sulfur_terms.json` (no Sprint 5C edits). | P0 | Central catalog surface when ontology workflow is live. | eligible_after_full_source_lock | planned_for_future_route_addition |
| sources | `/sources/` | en | source_governance | Public sources face from registry. | governance_meta | low | S-meta (no chemical fact claims) | C-inactive | governance | Requires populated `source_registry.json` before public value. | P1 | Makes citation discipline visible to readers. | eligible_after_full_source_lock | planned_for_future_route_addition |
| bisulfid | `/bisulfid/` | en | core_terminology | Standalone Bisulfid lexical record. | strict_registry | medium | S-strict | C-inactive | terminology_spine | Blocked until `route_id` exists in `routes.json`; mirrors Sprint 4L note. | P0 | Completes lexical record trio with narrative page. | non_public_until_route_registered | planned_for_future_route_addition |
| sulfid | `/sulfid/` | en | core_terminology | Standalone **Sulfid** record. | strict_registry | low | S-strict | C-inactive | terminology_spine | Same registration dependency as `bisulfid`. | P0 | Locks Germanic sulfide-language anchor for EN readers. | non_public_until_route_registered | planned_for_future_route_addition |
| hydrosulfide | `/hydrosulfide/` | en | core_terminology | Hydrosulfide label complement to triad. | strict_registry | medium | S-strict | C-inactive | terminology_spine | Do not duplicate separate H₂S safety operational page in Batch 1. | P1 | Completes hydrosulfide naming system without safety manual drift. | non_public_until_route_registered | planned_for_future_route_addition |
| corpus_methodology_overview | `/reference/corpus-methodology/` | en | methodology_reference | How sovereign pages are authored. | governance_meta | low | S-meta | C-inactive | governance | Editorial signoff gated; not a chemistry-fact page. | P1 | Explains corpus operating model to editors and partners. | non_public_until_editorial_signoff | planned_for_future_route_addition |
| nomenclature_governance_overview | `/reference/nomenclature-governance/` | en | source_governance | Readable nomenclature discipline tied to policy. | strict_registry | low | S-strict | C-inactive | governance | Pairs with `de_gov_nomenclature` when DE is routed. | P1 | Pre-publication gate for naming disputes. | eligible_after_full_source_lock | planned_for_future_route_addition |
| multilingual_corpus_map | `/reference/multilingual-corpus-map/` | en | index_map | Multilingual hub index. | governance_meta | low | S-meta | C-inactive | index_map | Blocked on hreflang strategy + `hreflang_groups.json`. | P2 | Structural map; prevents mirror sprawl before wiring. | non_public_until_hreflang_wiring | planned_for_future_route_addition |
| translator_playbook_bisulfide_family | `/reference/translator-playbook-bisulfide-family/` | en | methodology_reference | DE/EN translator playbook. | strict_registry | low | S-strict | C-inactive | governance | Align with `de_method_translator_playbook`. | P1 | Reduces translation-spam risk via controlled rules. | eligible_after_full_source_lock | planned_for_future_route_addition |
| citation_discipline_primer | `/reference/citation-discipline/` | en | source_governance | Citations from `source_registry.json`. | strict_registry | low | S-strict | C-inactive | governance | Feeds `sources` page expectations. | P2 | Bridges registry mechanics to editorial practice. | eligible_after_full_source_lock | planned_for_future_route_addition |
| academic_teaching_source_boundary | `/reference/academic-teaching-source-boundary/` | en | source_governance | Teaching-source limits per policy. | strict_registry | low | S-strict | C-inactive | governance | Reinforces candidate-only posture for normative claims. | P2 | Keeps classroom references from leaking into normative claims. | eligible_after_full_source_lock | planned_for_future_route_addition |
| bisulfite_wall_explainer | `/reference/bisulfite-wall/` | en | disambiguation_authority | Bisulfite vs bisulfide boundary. | strict_registry | medium | S-strict | C-inactive | disambiguation | Must merge editorially with `de_dis_bisulfite_wall` scope. | P1 | Foundational authority page; thesis-aligned. | eligible_after_full_source_lock | planned_for_future_route_addition |
| internal_linking_discipline | `/reference/internal-linking-discipline/` | en | methodology_reference | Internal link density rules. | governance_meta | low | S-meta | C-inactive | governance | Enables future `internal_links.json` batch without URL dumping. | P2 | Corpus-structure prerequisite before scaling pages. | non_public_until_editorial_signoff | planned_for_future_route_addition |
| quality_gate_public_explainer | `/reference/quality-gate/` | en | methodology_reference | Quality Gate explainer. | governance_meta | low | S-meta | C-inactive | governance | Owner review gate per blueprint eligibility. | P2 | Aligns public/compliance expectations with doctrine. | non_public_until_owner_review | planned_for_future_route_addition |

### English — specification table (part 2 of 2)

| proposed_route_id | proposed_path | language | corpus_category | page_role | source_requirement_level | claim_risk_level | source_locking_prerequisite | claim_approval_prerequisite | internal_linking_cluster | dependency_notes | priority_level | inclusion_rationale | public_launch_eligibility | implementation_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ontology_alignment_primer | `/reference/ontology-alignment-primer/` | en | methodology_reference | Ontology ↔ pages mapping. | strict_registry | low | S-strict | C-inactive | governance | Gated on registry activation posture in blueprint. | P2 | Prevents page/ontology drift at scale. | non_public_until_registry_activation | planned_for_future_route_addition |
| sulfur_element_term_record | `/terminology/sulfur-element/` | en | core_terminology | Element terminology record. | strict_registry | low | S-strict | C-inactive | terminology_spine | Links from gateway and `glossary`. | P1 | Canonical element record for spine density. | eligible_after_full_source_lock | planned_for_future_route_addition |
| sulfide_anion_term_record | `/terminology/sulfide-anion/` | en | core_terminology | Sulfide anion terminology record. | strict_registry | medium | S-strict | C-inactive | terminology_spine | Pairs with triad page; watch redox-family slip. | P1 | Core anion anchor for naming system. | eligible_after_full_source_lock | planned_for_future_route_addition |
| disulfide_bonds | `/disulfide-bonds/` | en | core_terminology | Disulfide bridge vocabulary. | strict_registry | low | S-strict | C-inactive | terminology_spine | Bio/materials boundary—no medical advice. | P1 | Extends terminology into biochemistry bridge. | eligible_after_full_source_lock | planned_for_future_route_addition |
| protein_disulfide_structure | `/protein-disulfide-structure/` | en | core_terminology | Protein disulfide structure vocabulary. | strict_registry | low | S-strict | C-inactive | terminology_spine | No therapeutic or clinical claims. | P1 | Materials/biology relevance without medical drift. | eligible_after_full_source_lock | planned_for_future_route_addition |
| sulfate_terminology | `/terminology/sulfate/` | en | core_terminology | Sulfate naming vocabulary. | strict_registry | low | S-strict | C-inactive | terminology_spine | First of oxo-anion family ladder. | P2 | Terminology breadth without generic explainer tone. | eligible_after_full_source_lock | planned_for_future_route_addition |
| sulfite_terminology | `/terminology/sulfite/` | en | core_terminology | Sulfite family vocabulary. | strict_registry | medium | S-strict | C-inactive | terminology_spine | Must separate from bisulfide/bisulfite walls. | P2 | Prevents orthography collisions with bisulfite explainer. | eligible_after_full_source_lock | planned_for_future_route_addition |
| thiosulfate_terminology | `/terminology/thiosulfate/` | en | core_terminology | Thiosulfate terminology record. | strict_registry | low | S-strict | C-inactive | terminology_spine | Cross-links sulfate/sulfite ladder. | P2 | Completes common oxo-thio anion trio. | eligible_after_full_source_lock | planned_for_future_route_addition |
| polysulfide_terminology | `/terminology/polysulfide/` | en | core_terminology | Polysulfide terminology record. | strict_registry | medium | S-strict | C-inactive | terminology_spine | Coordinates with `sulfane_chain_language`. | P2 | Supports advanced naming without thin lists. | eligible_after_full_source_lock | planned_for_future_route_addition |
| sulfane_chain_language | `/terminology/sulfane/` | en | core_terminology | Sulfane chain nomenclature language. | strict_registry | low | S-strict | C-inactive | terminology_spine | Avoid confusing with polysulfide operational chemistry. | P2 | Backbone for chain sulfide naming precision. | eligible_after_full_source_lock | planned_for_future_route_addition |
| sulfonic_acid_class_language | `/terminology/sulfonic-acid-class/` | en | core_terminology | Sulfonic acid class naming. | strict_registry | low | S-strict | C-inactive | terminology_spine | Organosulfur class page—must stay term-centric. | P2 | Expands organosulfur coverage without generic orgchem blog. | eligible_after_full_source_lock | planned_for_future_route_addition |
| sulfoxide_sulfone_language | `/terminology/sulfoxide-sulfone/` | en | core_terminology | Sulfoxide / sulfone naming. | strict_registry | low | S-strict | C-inactive | terminology_spine | Pairs with sulfonic/sulfide family links. | P2 | Controlled organosulfur oxidation-state language. | eligible_after_full_source_lock | planned_for_future_route_addition |
| sodium_sulfide_salts_language | `/terminology/sodium-sulfide-salts/` | en | core_terminology | Na₂S-family naming—language not handling. | strict_registry | medium | S-strict | C-inactive+boundary | terminology_spine | Defer substance-safety pages to later sprint. | P2 | Salt naming disambiguation without SDS manual drift. | eligible_after_full_source_lock | planned_for_future_route_addition |
| iron_sulfides_mineral_language | `/terminology/iron-sulfides/` | en | core_terminology | Pyrite/pyrrhotite vocabulary subset. | strict_registry | low | S-strict | C-inactive | terminology_spine | One mineral batch page; defer extra mineral grids. | P2 | Keeps geology vocabulary inside naming discipline. | eligible_after_full_source_lock | planned_for_future_route_addition |
| molybdenum_disulfide | `/molybdenum-disulfide/` | en | industrial_economic_interpretation | MoS₂ vocabulary hub. | strict_registry | low | S-strict | C-inactive+boundary | industrial_interpretation | Coordinate later with deferred WS₂ page per 5B merge note. | P1 | Materials-industrial bridge without duplicate MoS₂/WS₂ stubs. | eligible_after_full_source_lock | planned_for_future_route_addition |
| industrial_sulfur_systems | `/industrial-sulfur-systems/` | en | industrial_economic_interpretation | Industrial systems vocabulary—no market stats. | strict_registry | medium | S-strict | C-inactive+boundary | industrial_interpretation | Category discipline: document language, not procurement. | P1 | Connects gateway to industrial interpretation layer safely. | eligible_after_full_source_lock | planned_for_future_route_addition |
| economic_document_language_sulfur | `/reference/economic-document-language-sulfur/` | en | industrial_economic_interpretation | Filings / sector doc language only. | strict_registry | medium | S-strict | C-inactive+boundary | industrial_interpretation | Ban figures, targets, share, CAGR language. | P2 | Non-market industrial intelligence thesis support. | eligible_after_full_source_lock | planned_for_future_route_addition |
| supply_chain_vocabulary_sulfur | `/reference/supply-chain-vocabulary-sulfur/` | en | industrial_economic_interpretation | Logistics vocabulary—no trade statistics. | strict_registry | medium | S-strict | C-inactive+boundary | industrial_interpretation | No tariffs, trade routes as claims—terms only. | P2 | Teaches document literacy without trade data claims. | eligible_after_full_source_lock | planned_for_future_route_addition |
| claus_process_vocabulary | `/industrial/claus-process-vocabulary/` | en | industrial_economic_interpretation | Claus SRU terminology—no runbooks. | strict_registry | low | S-strict | C-inactive+boundary | industrial_interpretation | Operational tuning deferred explicitly. | P2 | High-frequency refinery language, safely bounded. | eligible_after_full_source_lock | planned_for_future_route_addition |
| fgd_document_language | `/industrial/fgd-document-language/` | en | industrial_economic_interpretation | FGD document vocabulary—non-operational. | strict_registry | medium | S-strict | C-inactive+boundary | industrial_interpretation | Avoid emissions compliance advice in Batch 1. | P2 | Environmental-doc language without compliance manual. | eligible_after_full_source_lock | planned_for_future_route_addition |
| hydrotreating_desulfurization_terms | `/industrial/hydrotreating-desulfurization-terms/` | en | industrial_economic_interpretation | Hydrotreating desulfurization **terms**. | strict_registry | medium | S-strict | C-inactive+boundary | industrial_interpretation | No catalyst selection / operating-parameter advice. | P2 | Refinery vocabulary bounded to naming discipline. | eligible_after_full_source_lock | planned_for_future_route_addition |

### German — specification table

| proposed_route_id | proposed_path | language | corpus_category | page_role | source_requirement_level | claim_risk_level | source_locking_prerequisite | claim_approval_prerequisite | internal_linking_cluster | dependency_notes | priority_level | inclusion_rationale | public_launch_eligibility | implementation_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| de_home | `/de/` | de | gateway | German gateway / sovereign framing. | strict_registry | low | S-strict | C-inactive | multilingual_de | Must reconcile strict_registry vs gateway split in future routing spec (5B note). | P0 | DE identity entry; pairs with EN gateway thesis. | eligible_after_full_source_lock | planned_for_future_route_addition |
| de_what_is_bisulfid | `/de/what-is-bisulfid/` | de | core_terminology | Canonical Bisulfid record (DE). | strict_registry | low | S-strict | C-inactive | multilingual_de | Source-lock after EN `what_is_bisulfid` is locked. | P0 | German record for brand-center concept. | eligible_after_full_source_lock | planned_for_future_route_addition |
| de_bisulfide_hydrosulfide_sulfide | `/de/bisulfide-hydrosulfide-sulfide/` | de | disambiguation_authority | Triad authority (DE). | strict_registry | low | S-strict | C-inactive | multilingual_de | Must mirror EN triad boundaries exactly. | P0 | DE disambiguation spine—non-negotiable for trust. | eligible_after_full_source_lock | planned_for_future_route_addition |
| de_glossary | `/de/glossary/` | de | core_terminology | German glossary chamber. | strict_registry | low | S-strict | C-inactive | multilingual_de | Ontology verification dependency like EN `glossary`. | P0 | Controlled DE glossary—not MT list pages. | eligible_after_full_source_lock | planned_for_future_route_addition |
| de_german_english_chemical_terms | `/de/german-english-chemical-terms/` | de | de_en_chemical_language | DE/EN term table (identity). | strict_registry | low | S-strict | C-inactive | multilingual_de | Density rules: avoid thin tables without definitional prose. | P1 | Primary cross-language infrastructure in German. | eligible_after_full_source_lock | planned_for_future_route_addition |
| de_bisulfid_vs_bisulfide | `/de/bisulfid-vs-bisulfide/` | de | de_en_chemical_language | DE orthography boundary narrative. | strict_registry | low | S-strict | C-inactive | multilingual_de | Pairs with EN bisulfid/bisulfide page. | P1 | DE-side authority for high-intent spelling queries. | eligible_after_full_source_lock | planned_for_future_route_addition |
| de_sulfid_vs_sulfide | `/de/sulfid-vs-sulfide/` | de | de_en_chemical_language | **Sulfid** vs sulfide (DE). | strict_registry | low | S-strict | C-inactive | multilingual_de | Pairs with EN sulfid/sulfide. | P1 | Completes identity-layer boundary set in DE. | eligible_after_full_source_lock | planned_for_future_route_addition |
| de_dis_bisulfite_wall | `/de/reference/bisulfite-wall/` | de | disambiguation_authority | Bisulfite wall localized. | strict_registry | low | S-strict | C-inactive | multilingual_de | Must stay aligned with `bisulfite_wall_explainer`. | P1 | Prevents bilingual drift on bisulfite boundary. | eligible_after_full_source_lock | planned_for_future_route_addition |
| de_gov_nomenclature | `/de/reference/nomenclature-governance/` | de | source_governance | Nomenclature governance localized. | strict_registry | low | S-strict | C-inactive | multilingual_de | Keep normative citations language-appropriate. | P1 | Governance localization before scaling DE terms grid. | eligible_after_full_source_lock | planned_for_future_route_addition |
| de_method_corpus_map | `/de/reference/corpus-map/` | de | methodology_reference | Localized corpus map hub. | governance_meta | low | S-meta | C-inactive | multilingual_de | Editorial signoff; depends on EN methodology posture. | P1 | DE-side map for editors—supports phased expansion. | non_public_until_editorial_signoff | planned_for_future_route_addition |
| de_method_translator_playbook | `/de/reference/translator-playbook/` | de | methodology_reference | Localized translator playbook. | governance_meta | low | S-meta | C-inactive | multilingual_de | Must not diverge from EN playbook rules. | P1 | Controlled translation governance for identity layer. | non_public_until_editorial_signoff | planned_for_future_route_addition |

---

*Sprint 5C — planning only; no registry or content mutations from this document.*
