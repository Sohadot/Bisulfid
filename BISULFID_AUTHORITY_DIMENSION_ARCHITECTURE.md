# BISULFID — Authority & Dimension Reconciliation (Architecture Package)

**Type:** DESIGN / GOVERNANCE sprint. **READ-ONLY.**
**Date:** 2026-09-19 · **Branch:** `claude/bisulfid-weekly-health-review-x4b07y`
**Baseline:** `DOCTRINE_TO_CORPUS_RECONCILIATION.md` v2 (accepted)
**Authority decision:** Contract C — Derived Canonical State (adopted as target; **not implemented**).

> **Nothing in this document is executed.** No public HTML, sitemaps, robots directives, Search Console state, route publication/indexation flags, source statuses, claim statuses, or corpus content were modified. No pages generated. No state engine built. No 14K migration. This is a specification precise enough that implementation cannot recreate the two-authority fork.

---

## 0. Problem this package closes

Today two files silently disagree and a third (deploy) obeys the wrong one:

| State | File | Value today | Should it decide indexation? |
|---|---|---|---|
| Governed route posture | `routes.json` | 14,000 × `planned/indexable:false/in_sitemap:false` | Necessary, not sufficient |
| Release authorization | `release_ledger.json` | 13,998 `released/indexable:true`, `source_pack_id:null`, `validation:pending` | Necessary, not sufficient |
| Deployed HTML | `site/public/**` | 14,039/14,041 `index,follow` | **No — must be derived** |
| Sitemap / robots | `sitemap*.xml`,`robots.txt` | 13,998 URLs; `Allow:/` | **No — must be derived** |

Contract C removes the fork by construction: **no single file is "the boss."** Each layer owns the facts it is authoritative for; a pure function derives what deploy/sitemap/robots may do; and a state can go public only when *every* required layer independently permits it.

---

# Deliverable 1 — Publication Authority Contract (Contract C)

## 1.1 The seven posture layers and their owners

Publication is derived from six *input* postures plus one *authorization*, producing two *derived* states. Ownership is exclusive: exactly one system may write each input.

| # | Layer | Owner (sole writer) | Allowed values | Meaning |
|---|---|---|---|---|
| 1 | **governance_posture** | `routes.json` | `planned` → `relationship_qualified` → `reference_draft` → `governed` | Is this route a legitimate governed knowledge position, and how far through drafting? |
| 2 | **evidence_posture** | evidence store (D3) + `source_registry.json` | `evidence_not_required` · `evidence_collecting` · `evidence_sufficient` · `evidence_locked` | Does verified, locked evidence back every factual line? |
| 3 | **claim_posture** | `claims/*.json` | `claim_not_required` · `claim_pending` · `claim_approved_narrow` · `claim_approved` · `claim_forbidden` | Are the required claims approved *and their registry active*? |
| 4 | **validation_posture** | validators / Quality Gate | `not_validated` · `validated` · `validation_failed` | Do all 11 gates + corpus validators pass for this route? |
| 5 | **release_authorization** | `release_ledger.json` | `not_authorized` · `authorized` · `withdrawn` (+ append-only history) | Has an owner-level decision authorized public release? |
| 6 | **publication_state** (DERIVED) | derived-state function (read-only to all) | `not_public` · `public_noindex` · `public_indexable` | What deploy may do. |
| 7 | **indexation_state** (DERIVED) | derived-state function | `noindex` · `index_candidate` · `index_approved` | What sitemap/robots may do. |

**Key invariant:** layers 6–7 are **computed**, never written by hand and never stored as an editable source of truth. `routes.json.indexable` and `release_ledger.indexable` are *demoted from decisions to inputs* (or removed in favor of the postures above; see Migration Map).

## 1.2 The derived-state function (specification, not code)

```
publication_state, indexation_state = derive(
    governance_posture, evidence_posture, claim_posture,
    validation_posture, release_authorization )
```

Rules, in strict precedence (first matching rule wins):

1. **Floor rule (most restrictive wins).** If ANY of these hold → `publication_state = not_public`, `indexation_state = noindex`:
   - `governance_posture ∈ {planned, relationship_qualified}`
   - `evidence_posture ∈ {evidence_collecting}` while any factual line is `source_required`
   - `claim_posture ∈ {claim_pending, claim_forbidden, claim_required_unresolved}`
   - `validation_posture ∈ {not_validated, validation_failed}`
2. **Public-but-noindex rule.** If `governance_posture ∈ {reference_draft, governed}` AND `validation_posture = validated` AND (`evidence_posture ∈ {evidence_sufficient, evidence_locked, evidence_not_required}`) AND `release_authorization = authorized` AND **Information-Gain review not yet passed** → `public_noindex` / `noindex`. *(Reachable for humans/agents, excluded from sitemap.)*
3. **Reference-indexable rule.** `public_indexable` / `index_approved` **only if ALL** hold:
   - `governance_posture = governed`
   - `evidence_posture = evidence_locked` (every factual line)
   - `claim_posture ∈ {claim_approved, claim_approved_narrow}` in an **active** registry
   - `validation_posture = validated`
   - `release_authorization = authorized`
   - **Information-Gain review = passed** (Deliverable 7)
4. **Withdrawal override.** `release_authorization = withdrawn` forces at most `public_noindex` regardless of other layers (fast rollback path that never deletes the route).

**Anti-fork guarantee:** reaching `public_indexable` requires the simultaneous, independent consent of the registry, the evidence store, the claim registry, the validators, the release ledger, *and* the Information-Gain gate. No one file can promote a page; every one can veto it.

## 1.3 Ownership & transition table

| Transition | Who may trigger | Evidence required | On disagreement |
|---|---|---|---|
| governance `planned → relationship_qualified` | route governance (owner review) | a governed relationship hypothesis recorded (D4) | stays `planned` |
| governance `relationship_qualified → reference_draft` | authoring | draft body exists, markers on | stays qualified |
| governance `reference_draft → governed` | governance review | draft complete, no `[SOURCE REQUIRED]` markers | stays draft |
| evidence `collecting → sufficient` | evidence store | ≥1 `verified` source per factual line | stays collecting |
| evidence `sufficient → locked` | source governance | source `source_lock_status: locked` | stays sufficient |
| claim `pending → approved(_narrow)` | claim governance | approval recorded + registry **activated** | stays pending |
| validation `not_validated → validated` | validators (automated) | all gates PASS for the route | `validation_failed` |
| release `not_authorized → authorized` | **owner** (DECISION_LOG) | derived precondition ≥ `public_noindex` eligible | not authorized |
| release `authorized → withdrawn` | owner or auto (evidence/claim regressed) | any veto layer regressed | withdraws |
| **publication/indexation** | *nobody* (derived) | — | derived function recomputes; divergence flagged (audit-only) |

## 1.4 Conflict semantics (the point of Contract C)

- **Ledger says released, evidence/claim/validation insufficient →** derived state caps at `not_public`/`noindex`; a **divergence record** is emitted (audit-only, never a CI hard-fail during migration). The ledger entry remains as *history*; it simply no longer forces indexation.
- **routes.json `governed` but no release authorization →** caps at `not_public`. Registry alone cannot publish.
- **Everything green but Information-Gain not passed →** caps at `public_noindex`. Prevents thin pages from indexing even when individually "valid."

## 1.5 Supersession of Sprint 99 (historical fact preserved)

- **Preserved as historical fact:** On 2026-06-05, Sprint 99 authorized release of 13,998 dossier pages under "cautious reference framing," with the release ledger declared the public-route source of truth (`DECISION_LOG.md` ~L4416/4527/4551). This *happened* and stays in the log and in the ledger's history.
- **Operationally superseded:** From Contract C ratification, the release ledger is **no longer the sole determinant of indexation**. It becomes the **release-authorization + history owner**; indexation is derived (§1.2). The 13,998 pages are **not de-indexed by this sprint** (they remain operationally frozen per the stop condition) — but once the derived engine is live, their indexation will be recomputed from their true postures.
- The ratifying DECISION_LOG entry (Deliverable 9) states both explicitly.

---

# Deliverable 2 — Semantic Dimension Contract

Eleven concepts. Each has one semantic question, one owner, a cardinality, and an explicit non-overlap rule. **None alone creates a URL** (Deliverable "Knowledge object before URL", §law in D8/D11).

| Dimension | Semantic question | Owner registry | Cardinality on a knowledge object | Non-overlap rule |
|---|---|---|---|---|
| **entity** | *What thing is this about?* | `ontology/sulfur_terms.json` (+edges) | 1..n | An entity is a controlled ontology node, never a domain/audience/place. |
| **subject_domain** | *What field of knowledge?* | **new** `subject_domain_registry.json` (D-below) | 1..n | Domain ≠ presentation standard. Chemistry is a domain; "academic" is not. |
| **reference_layer** | *To what evidentiary/presentation standard is the surface organized?* | `reference_layer_registry.json` (existing, 9) | 1 | Layer ≠ domain and ≠ audience. Same fact can appear in academic *or* technical layer. |
| **audience** | *Which user constraints materially change vocabulary, claim boundary, evidence presentation, or task?* | `audience_layer_registry.json` (existing, 9) | 1..n | Audience is created only if it changes evidence/claim/structure/task (D9), never per profession. |
| **page_type** | *What structural reference form is rendered?* | `page_type_registry.json` (existing, 19) | 1 | Form only; carries no facts. |
| **language** | *In which language is this surface written?* | `languages.json` (existing, 7) | 1 | Language ≠ geography. `de` is a language, not "Germany." |
| **geography** | *Which place participates in a supported relationship?* | **new** `geography_registry.json` (D4) | 0..n | Geography attaches only via a governed, evidence-qualified relationship. |
| **jurisdiction** | *Which authority/legal system governs this specific statement?* | **new** `jurisdiction_registry.json` (D5) | 0..n | Jurisdiction ≠ geography (a jurisdiction is an authority+instrument, not a place). |
| **relationship** | *How does an entity connect to a place/domain/entity?* | **new** `relationship_class_registry.json` (D4) | 0..n | Relationship classes are governed + evidence-qualified, not free text. |
| **temporal_scope** | *For what period is this statement valid?* | evidence record fields (D3/D5) | 0..1 per statement | Temporal is per-statement, not per-route. |
| **evidence** | *What supports this?* | **new** `evidence/` store (D3) + `source_registry.json` + `claims/*.json` | 1..n per factual line | Evidence is the only thing that promotes a knowledge object toward a URL. |

**Standing rule (constitutional):** a URL exists only after (a) evidence sufficiency and (b) Information-Gain review — never because a dimension value exists. Adding a dimension value adds *precision*, never a page.

---

# Deliverable 3 — Evidence Architecture (atomic)

Bridges the existing registries; **does not replace them**. Chain:

```
source_registry.json → evidence/<id>.json → claims/*.json → ontology entity/relationship → knowledge_object → reference_surface(URL)
```

## 3.1 Why a new store (and not just source+claim)

`source_registry.json` records *sources*; `claims/*.json` records *approved statements*. Neither records the **atomic, reconstructable fact instance** with its geography/period/unit/methodology. The evidence object is the missing join row between a source and a claim, carrying provenance a claim reference alone cannot. It is additive: every evidence record must cite an existing `source_id` and, when it supports a public claim, an existing `claim_id`.

## 3.2 Core schema (proposed — `main/data/evidence/<evidence_id>.json`)

```jsonc
{
  "evidence_id": "EVD-…",                 // stable, unique
  "evidence_kind": "qualitative|quantitative|scientific|legal_regulatory|terminological",
  "entities": ["ontology term_id", …],    // >=1, resolve to ontology
  "relationship": "REL-… | null",         // -> relationship_class_registry (D4)
  "subject_domain": ["SD-…", …],          // -> subject_domain_registry (D-below); >=1
  "geography": ["GEO-… | null"],          // -> geography_registry (D4); only via relationship
  "jurisdiction": "JUR-… | null",         // -> jurisdiction_registry (D5); legal/regulatory only
  "language_of_evidence": "en|de|ar|…",
  "claim_scope": "exact statement this evidence supports",
  "source_id": "SRC-…",                   // REQUIRED, resolves to source_registry
  "source_type": "authoritative_dictionary|chemical_nomenclature_standard|government_scientific_database|industry_publication|academic_teaching_reference|market_report|regulatory_instrument|…",
  "claim_id": "CLM-… | null",             // set when it backs a registered claim
  "publication_date": "YYYY-MM-DD | null",
  "retrieval_date": "YYYY-MM-DD",
  "temporal_scope": { "as_of": "…|null", "valid_from": "…|null", "valid_to": "…|open|null" },
  "verification_state": "seeded|verified|locked",   // reuses source_registry vocabulary
  "confidence": "high|medium|low",
  "risk_class": "low|medium|high",
  "allowed_uses": [...],
  "prohibited_uses": [...],
  "used_by": ["route_id|knowledge_object_id", …]    // back-reference for audit
}
```

## 3.3 Field profiles by evidence_kind (only relevant fields required)

| evidence_kind | Additionally required | Must NOT force |
|---|---|---|
| **terminological** | entities, subject_domain, source_id, claim_scope | quantitative/legal blocks |
| **scientific** | entities, subject_domain, source_id, publication_date | economic/legal blocks |
| **quantitative** | `quantitative{ metric, definition, unit, value, geography, period, classification_code?, methodology, revision_state }` | legal instrument fields |
| **legal_regulatory** | `legal{ jurisdiction, authority, instrument, instrument_type, effective_date, amendment_state, valid_from, valid_to }` (D5) | quantitative unit block |
| **qualitative** | entities, subject_domain, source_id, claim_scope | quantitative/legal blocks |

**Missing-value law:** absent data is stored as explicit `null`/`missing`, never synthesized. A schema is never "completed" by inventing a value. Machine-readable output reflects governed truth, including its gaps.

---

# Deliverable — Subject-domain model (choice + justification)

**Choice: a small, dedicated `subject_domain_registry.json`, seeded from existing ontology signals.** Not a new large taxonomy; not an ontology-field extension.

**Why not extend the ontology field (`chemical_field`)?** Domain must attach to **evidence objects and relationships**, not only to ontology *terms*. A trade-flow evidence record or a Germany-jurisdiction relationship has a domain (economics; regulation) but no single ontology term owns it. A term-scoped field cannot express domain for non-term knowledge objects → semantic distortion.

**Why not free text?** The v1 failure mode. Domains must be governed and evidence-amended.

**Seed set (from what evidence/ontology actually support today):** `chemistry`, `inorganic_chemistry`, `nomenclature`, `materials_science`, `industrial` (from `ontology.chemical_field`/`industrial_signal`), `linguistics`/`terminology` (from the DE/EN suffix work), `safety_context` (governed, non-prescriptive). Nothing else is seeded because nothing else has evidence.

**Growth rule:** a domain enters the registry only via **evidence-backed amendment** — a `verified` evidence record introducing it — recorded in DECISION_LOG. Domains named in doctrine but unsupported today (physics, biology, biomedical, agriculture, environment, mining, energy, economics, trade, logistics, regulation) are **reserved names, not active domains**; they activate when evidence arrives. This lets the architecture *grow into* them without inventing them now.

---

# Deliverable 4 — Geography & Relationship Model

**Geography is a relationship system, never a page multiplier.** Model:

```
entity → relationship(class) → geography → subject_domain → evidence → temporal_scope
```

## 4.1 `geography_registry.json` (proposed)
Minimal governed place records: `geo_id`, `label`, `iso_3166` (or region code), `type` (country|region|supra), `status` (`reserved` | `evidence_qualified`). A place is `reserved` until an evidence-qualified relationship references it.

## 4.2 `relationship_class_registry.json` (proposed)
Relationship classes are **themselves governed and evidence-qualified** — the example list is *not* an authorized taxonomy:
`relationship_class_id`, `label`, `definition`, `directionality` (entity→geo | geo→entity | entity→entity), `evidence_requirement` (which `source_type`s can qualify it), `status` (`reserved`|`active`).
Candidate classes (activate only with evidence): importer, exporter, producer, industrial_user, processing_center, regulatory_jurisdiction, research_center, terminology_origin, supply_chain_node, manufacturing_center.

## 4.3 The three named traps — resolved by rule
- **Germany ≠ the German language.** `language:de` never creates a Germany geography. A Germany geographic object requires a `relationship + evidence` (e.g. `terminology_origin` with a German-nomenclature source, or `regulatory_jurisdiction` with a German instrument).
- **Morocco ≠ Arabic/French content.** Requires an evidence-qualified relationship (e.g. `importer`/`industrial_user` with a customs/trade source).
- **China ≠ `/zh/`.** Requires production/manufacturing/trade evidence.

**Status today (honest):** the source registry has **zero** trade/economic/production/regulatory sources. Therefore **all** of Morocco, Gulf, China, and even Germany-as-jurisdiction are `reserved` / `EVIDENCE_COLLECTING`. The model is wired; it currently qualifies **no** geographic object.

---

# Deliverable 5 — Temporal / Jurisdiction Model

First-class support for statements that **expire or change**, without becoming a legal-advice service.

## 5.1 `jurisdiction_registry.json` (proposed)
`jurisdiction_id`, `label`, `authority`, `legal_system`, `status`.

## 5.2 Instrument-level provenance (in `legal` block of evidence, D3.3)
`jurisdiction`, `authority`, `instrument`, `instrument_type` (statute|regulation|standard|guidance|directive|treaty), `effective_date`, `amendment_state` (in_force|amended|repealed|draft), `valid_from`, `valid_to`, `as_of`, `last_verification_date`.

## 5.3 Rules
- **Historical vs effective are distinguishable:** a repealed instrument keeps `amendment_state: repealed` + its `valid_from/valid_to`; it is never silently dropped and never presented as current.
- **Guidance ≠ law; draft ≠ in force** (enforced by `instrument_type` + `amendment_state`); no legal advice — reference/context only (consistent with `SOURCE_POLICY` blocked-content list).
- Temporal fields apply to **quantitative** and **scientific** evidence too (a trade figure has a reporting year; a datum has an as-of date).

---

# Deliverable 6 — MoS₂ Proof Trace (governance proof, NOT published)

One end-to-end trace through the architecture. **Nothing is changed, locked, activated, or published.** The point is to show the architecture can *explain why a seemingly supported object is still not publishable.*

| Step | Object (actual repo record) | State today | Contract-C posture | Verdict |
|---|---|---|---|---|
| Source | `SRC-SPEKTRUM-MOS2-DE` (Spektrum Lexikon der Chemie, MoS₂, de) | `verification_state: verified`, **`source_lock_status: candidate`** | evidence input present but **not locked** | ⚠ blocks `evidence_locked` |
| Source pack | `SPK-SPEKTRUM-MOS2-DE` | status **None** (not verified) | not a verified pack | ⚠ pack not verified |
| Evidence object | *(does not exist yet — no `evidence/` store)* | absent | `evidence_posture` cannot reach `sufficient/locked` via the atomic store | ⚠ store not built (this sprint only specifies it) |
| Claim | `CLM-TERM-MOS2-DE-001` → source `SRC-SPEKTRUM-MOS2-DE`, route `de_core_mos2` | **`status: approved`** but in **`terminology_claims.json` (`status: inactive`)**; `prohibited_uses` include "route publication", "source-locking by itself" | claim approved **but registry inactive** | ⚠ blocks `claim` layer (registry not active) |
| Ontology entity | `molybdenum_disulfide` / `molybdenum_disulfide_mos2` | `status: planned`, **`source_ids: []`**, `language_vector: ["en"]` | entity **not linked to the source**; language mismatch (evidence is `de`, entity tagged `en`) | ⚠ entity↔source link missing; language vector gap |
| Route | `de_core_mos2` → `/de/terminology/molybdenum-disulfide/` | `status: planned`, `indexable:false`, `in_sitemap:false`, `required_claim_groups:["terminology_claims"]` | `governance_posture: planned` | ⚠ blocks `governed` |
| Validation | — | not validated for this route | `not_validated` | ⚠ blocks |
| Release auth | release ledger | this DE route not among the 13,998 EN dossier releases | `not_authorized` | ⚠ blocks |
| **Derived publication_state** | — | — | **`not_public` (floor rule)** | **Correctly NOT publishable** |

**What is already satisfied:** exactly one verified source; exactly one approved claim correctly scoped and correctly forbidding its own publication; a registered route.
**What blocks (all must clear, none touched this sprint):** source-lock; claim-registry activation; an atomic evidence record; ontology entity↔source link + language vector; route → `governed`; validation; release authorization; Information-Gain review.

**Conclusion:** the architecture explains, mechanically, why MoS₂ — the single strongest object in the repo — is still not publishable. That is the desired behavior. (No status changed.)

---

# Deliverable 7 — Information Gain Calibration Plan (no arbitrary threshold)

**Gate question:** *"Does this knowledge surface independently add something worth preserving and retrieving?"* — never *"did we rewrite the prose enough?"*

## 7.1 Signals (evidence-first; text last)
1. evidence-set overlap (primary) · 2. claim-set overlap · 3. source-set overlap · 4. relationship difference · 5. geography/jurisdiction difference · 6. temporal difference · 7. module/section overlap · 8. user-task difference · 9. textual similarity (diagnostic only).

## 7.2 Labelled calibration dataset (design)
Assemble candidate pairs (drawn from the existing 14K + planned pilots) hand-labelled into **five classes**: `true_duplicate`, `near_duplicate`, `valid_sibling`, `valid_localization`, `valid_domain_specific_reference`. Target ≥ ~40 pairs per class, balanced across languages and lanes. Store as `main/data/information_gain/calibration_pairs.json` (design artifact; not built this sprint).

## 7.3 Procedure
1. Compute all nine signals per pair. 2. Fit thresholds/weights that separate {true, near} from {sibling, localization, domain-specific} at an agreed precision/recall — **localizations and domain-specific references must never be flagged duplicate.** 3. Ratify weights/thresholds in DECISION_LOG. 4. Re-calibrate on corpus-composition change. No numeric threshold is authoritative before this runs; similarity is never an optimization target.

---

# Deliverable 8 — Migration Impact Map (nothing modified now)

| Artifact | Eventual action | Rationale |
|---|---|---|
| `routes.json` | **Extend** schema: add `subject_domain[]`, `geography[]`, `jurisdiction[]`, `reference_layer`, `audience[]`, `relationship[]`, governance_posture; **demote** raw `indexable`/`in_sitemap` to derived (read-only) | wire the lost dimensions; stop hand-set indexation |
| `release_ledger.json` | **Re-scope** to release-authorization + append-only history; drop `indexable` as a decision field | Contract C role split |
| `sitemap_policy.json`, sitemap generators (`atlas_generate_sitemaps_*`), `generate_robots.py` | **Replace** inputs: consume derived `indexation_state` only | single derived source |
| `main/data/evidence/` | **New** store (D3) | atomic provenance |
| `subject_domain_registry.json`, `geography_registry.json`, `jurisdiction_registry.json`, `relationship_class_registry.json` | **New** registries (D2/D4/D5) | first-class dimensions |
| `ontology/sulfur_terms.json` | **Extend** entities with `source_ids` links + correct `language_vector`; add domain tags feeding the domain registry seed | fix MoS₂-type gaps |
| `claims/*.json` + `source_registry.json` | **No change this sprint**; later: activation policy + source-lock workflow | governance decision pending |
| Corpus generators (`generate_14000_…`, `generate_7500_…`, `generate_1500_…`) | **Deprecate** for public generation; replace with evidence→object→surface composer | kill Route→Template→Text |
| CI (`corpus-governance-ci.yml`) | **Add** derived-state + ledger↔routes consistency checks in **audit/report-only** mode first | no hard-fail on historical mismatch |
| `pages-public-deploy.yml` | later: gate on derived `public_indexable` count, not a hard 14,041 literal | deploy reads derived state |

---

# Deliverable 9 — Governance Ratification Draft (for DECISION_LOG.md)

> ### Sprint — Authority & Dimension Reconciliation: ratify Contract C + dimension/evidence architecture
> **Date:** _(ratification date)_ · **Scope:** governance architecture only; no production data, HTML, sitemap, robots, indexation flags, source/claim statuses, or corpus content modified.
>
> **Decision 1 — Publication authority (Contract C, Derived Canonical State).** Publication and indexation states are **derived** by a governed function from six input postures (governance/evidence/claim/validation + release authorization). No single file determines indexation. `routes.json` owns governed route posture; `release_ledger.json` owns release authorization and append-only history; evidence/claim/validators own knowledge sufficiency. Deploy, sitemap, and robots consume **only** the derived state.
>
> **Decision 2 — Supersession, with history preserved.** The Sprint 99 decision (2026-06-05) that made the release ledger the sole source of truth for public routes, and released 13,998 dossier pages under cautious framing, **remains a historical fact and is not erased.** Its **operational effect on indexation is superseded** by Contract C. Existing pages are not de-indexed by this ratification; their indexation will be recomputed from true postures when the derived engine is implemented under a later, separately-approved sprint.
>
> **Decision 3 — Semantic dimensions.** entity, subject_domain, reference_layer, audience, page_type, language, geography, jurisdiction, relationship, temporal_scope, and evidence are permanently distinct dimensions (Deliverable 2). None alone creates a URL.
>
> **Decision 4 — New governed registries** (subject_domain, geography, jurisdiction, relationship_class) and an atomic **evidence store**, all additive and evidence-amended; reserved domain/geography names activate only on verified evidence.
>
> **Decision 5 — Knowledge-object-before-URL law.** A governed knowledge object may be a section, table, data record, edge, timeline event, jurisdiction record, or machine node. Independent URL promotion requires evidence sufficiency **and** Information-Gain review.
>
> **Decision 6 — Information Gain.** No numeric duplicate threshold is ratified until calibration (Deliverable 7) on labelled pairs.
>
> **Not decided here (require owner judgment):** source-lock workflow, claim-registry activation policy, 14K per-route disposition, new-audience admissions, and the exact derived-state precedence constants — all deferred to later approved sprints.

---

# Deliverable "Knowledge object before URL" — architectural law

**Law.** The system may hold many governed knowledge objects that never become standalone pages. An object may instead be a *section, table, chart/data record, relationship edge, timeline event, jurisdiction record, machine-readable node,* or *part of a larger canonical page*. **Independent URL promotion occurs only after evidence sufficiency AND Information-Gain review.** This is the primary structural guard against a second Cartesian explosion: adding domains/geographies/relationships enriches objects; it does not add URLs.

---

# Final Report

## What architecture is now sufficiently resolved
- **Publication authority (Contract C)** — layers, owners, derived function, precedence, conflict semantics, and Sprint-99 supersession-with-history are specified precisely enough to implement without re-forking.
- **Semantic dimension contract** — 11 dimensions with owners and non-overlap rules; domain permanently separated from reference_layer; "no dimension creates a URL" is constitutional.
- **Evidence architecture** — atomic schema bridging source→evidence→claim→entity/relationship→object→surface, with kind-specific field profiles and a strict missing-value law.
- **Geography/relationship & temporal/jurisdiction models** — wired as evidence-qualified relationship systems; the Germany/Morocco/Gulf/China traps are closed by rule.
- **MoS₂ proof trace** — the architecture correctly explains why the strongest object is still not publishable, and surfaced two concrete data gaps (ontology entity `source_ids: []`; `de` evidence vs `en` entity language vector).
- **Information-Gain** — signal set + calibration methodology defined; no arbitrary threshold.
- **Knowledge-object-before-URL** — ratified as law.

## What still requires owner governance judgment
1. **Contract C precedence constants** — the exact posture values that gate each derived transition (owner sign-off on the state tables in §1.2–1.3).
2. **Source-lock workflow & claim-registry activation** — currently all sources `candidate`, all claim registries `inactive`; policy is an owner decision (nothing publishes until decided).
3. **Subject-domain / relationship-class admissions** — which reserved names activate, and on what evidence.
4. **14K per-route disposition** — module / consolidate / redirect / retire (and whether URL retirement is permitted).
5. **New-audience admissions** — which, if any, personas clear the "changes evidence/structure/claim/task" bar.
6. **Ratification of the DECISION_LOG entry** (Deliverable 9).

## Exact files the FIRST implementation sprint would touch
Design/scaffolding only — **no public HTML, sitemap, robots, or indexation changes:**
- `DECISION_LOG.md` — append the Deliverable-9 ratification entry.
- **New (empty/seed) registries:** `main/data/subject_domain_registry.json`, `main/data/geography_registry.json`, `main/data/jurisdiction_registry.json`, `main/data/relationship_class_registry.json`.
- **New store:** `main/data/evidence/` with `EVD-MOS2-DE-001.json` as the single seed record (from the existing verified source; no status change).
- `main/data/ontology/sulfur_terms.json` — link `molybdenum_disulfide*` `source_ids` and correct `language_vector` (data-integrity fix; no publication effect).
- **New spec docs** for the derived-state function + calibration dataset skeleton (`main/data/information_gain/calibration_pairs.json`, empty).
- **No change** to `routes.json`, `release_ledger.json`, `site/public/**`, sitemaps, robots, source statuses, claim statuses, CI behavior.

## What that first implementation sprint should do
Stand up the **governance scaffolding** only: ratify Contract C in the log; create the four new registries (empty + reserved names + seed domains); create the atomic evidence store with the one MoS₂ record; fix the two MoS₂ ontology data gaps; and lay down the derived-state function *specification tests* (given postures → expected derived state) **without wiring them to deploy**. It must write no public page, change no indexation, add no CI hard-fail, and publish nothing.

## Stop
Design package complete. **Not implemented.** No state engine built, no 14K migration, no source collection at scale, no indexation change, no production PR. Awaiting owner review and explicit approval of the first implementation sprint.

---
*Authority & Dimension Reconciliation — READ-ONLY design package. No production files modified.*
