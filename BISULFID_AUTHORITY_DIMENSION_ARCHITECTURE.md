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
| 7 | **indexation_state** (DERIVED) | derived-state function | `noindex` · `index_approved` (⚠ `index_candidate` **removed** — unreachable; see [Integrity Pass §IP-16.1](#ip-16--final-consistency-corrections)) | What sitemap/robots may do. |

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
   - `claim_posture ∈ {claim_pending, claim_forbidden}` (⚠ enum corrected — `claim_required_unresolved` was a v1 stray name, removed; see [Integrity Pass §3](#ip-3--posture-enum-canonicalization))
   - `validation_posture ∈ {not_validated, validation_failed}`
2. **Public-but-noindex rule.** If `governance_posture ∈ {reference_draft, governed}` AND `validation_posture = validated` AND (`evidence_posture ∈ {evidence_sufficient, evidence_locked, evidence_not_required}`) AND `release_authorization = authorized` AND **Information-Gain review not yet passed** → `public_noindex` / `noindex`. *(Reachable for humans/agents, excluded from sitemap.)*
3. **Reference-indexable rule.** `public_indexable` / `index_approved` **only if ALL** hold:
   - `governance_posture = governed`
   - `evidence_posture = evidence_locked` (every factual line)
   - `claim_posture ∈ {claim_approved, claim_approved_narrow}` in an **active** registry
   - `validation_posture = validated`
   - `release_authorization = authorized`
   - **Information-Gain review = passed** (Deliverable 7)
4. **Withdrawal override.** `release_authorization = withdrawn` → **`not_public` / `noindex`** (⚠ **corrected in [Integrity Pass §2](#ip-2--release-authorization-withdrawal-vs-suspension)** — v1 wrongly said "at most public_noindex," which broke the veto guarantee; a separate `indexation_hold` concept covers "authorized but temporarily out of search"). `not_authorized` on any otherwise-green combination also → `not_public` / `noindex` (never falls through).

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
  "evidence_review_posture": "unreviewed|extracted|scope_reviewed|evidence_verified", // ⚠ RENAMED from v1 "verification_state" — evidence review is NOT source verification; see Integrity Pass §5. Do NOT reuse source_registry vocabulary.
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
| Source pack | `SPK-SPEKTRUM-MOS2-DE` | **`verification_state: verified_limited`, `publication_status: narrow_release_only`** (registry `status: architecture_active`) — ⚠ **corrected, [Integrity Pass §8](#ip-8--corrected-mos-source-pack-interpretation)**; v1 wrongly read "status None = not verified" | a *narrow-verified* pack, not a general-release pack | ✓ verified-limited, but **not** route-publication authorization |
| Evidence object | *(does not exist yet — no `evidence/` store)* | absent | `evidence_posture` cannot reach `sufficient/locked` via the atomic store | ⚠ store not built (this sprint only specifies it) |
| Claim | `CLM-TERM-MOS2-DE-001` → source `SRC-SPEKTRUM-MOS2-DE`, route `de_core_mos2` | **`status: approved`** but in **`terminology_claims.json` (`status: inactive`)**; `prohibited_uses` include "route publication", "source-locking by itself" | claim approved **but registry inactive** | ⚠ blocks `claim` layer (registry not active) |
| Ontology entity | `molybdenum_disulfide` / `molybdenum_disulfide_mos2` | `status: planned`, `source_ids: []`, `language_vector: ["en"]` | ⚠ **NOT a data-integrity error** — [Integrity Pass §9/§10/§11](#ip-9--concept--lexeme-ontology-analysis). This is a **Concept↔Lexeme semantics question**: a narrow German lexeme source should link via an *evidence assertion*, not by mutating an en-tagged concept node. | **open semantic question**, no mutation justified yet |
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
| `ontology/sulfur_terms.json` | ⚠ **DEFERRED — no mutation until the Concept↔Lexeme audit resolves (Integrity Pass §9–§11).** The v1 "extend `source_ids` + correct `language_vector`" items are **removed** from the approved first sprint. | semantics unestablished; do not "repair" |
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
- **MoS₂ proof trace** — the architecture correctly explains why the strongest object is still not publishable. (⚠ The two "data gaps" v1 named are reclassified as an **open Concept↔Lexeme semantic question**, not errors to fix — Integrity Pass §9–§11.)
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
- **New store:** `main/data/evidence/` — directory + schema + validators + **test-only fixtures** (clearly marked non-governed). ⚠ **No real `EVD-MOS2-DE-001` record** (IP-16.3: no evidence object until a governed lexeme ID exists).
- ~~`main/data/ontology/sulfur_terms.json` — link `source_ids` / correct `language_vector`~~ **REMOVED from the first sprint (Integrity Pass §11).** No ontology mutation until the Concept↔Lexeme audit is decided by the owner.
- **New spec docs** for the derived-state function + calibration dataset skeleton (`main/data/information_gain/calibration_pairs.json`, empty).
- **No change** to `routes.json`, `release_ledger.json`, `site/public/**`, sitemaps, robots, source statuses, claim statuses, CI behavior.

## What that first implementation sprint should do
Stand up the **governance scaffolding** only: ratify Contract C in the log; create the four new registries (empty + reserved names + seed domains); create the atomic evidence store with the one MoS₂ record; fix the two MoS₂ ontology data gaps; and lay down the derived-state function *specification tests* (given postures → expected derived state) **without wiring them to deploy**. It must write no public page, change no indexation, add no CI hard-fail, and publish nothing.

## Stop
Design package complete. **Not implemented.** No state engine built, no 14K migration, no source collection at scale, no indexation change, no production PR. Awaiting owner review and explicit approval of the first implementation sprint.

---
---

# Architecture Integrity Pass

**READ-ONLY precision pass · 2026-09-19.** No production files, registries, ontology, evidence files, or DECISION_LOG modified. This section is **authoritative** wherever it corrects earlier deliverables. It closes state-machine ambiguities and prevents duplicated authority inside the evidence model.

## IP-1 — Contract C as a total, exhaustive state machine

Information Gain is now an **explicit input posture**, not an out-of-band check.

**Six input postures (exclusive owners):**
| Posture | Owner | Values |
|---|---|---|
| `governance_posture` | `routes.json` | `planned` · `relationship_qualified` · `reference_draft` · `governed` |
| `evidence_posture` (derived from source eligibility + evidence review — IP-5) | evidence store + `source_registry.json` | `evidence_not_required` · `evidence_collecting` · `evidence_sufficient` · `evidence_locked` |
| `claim_posture` | `claims/*.json` | `claim_not_required` · `claim_pending` · `claim_approved_narrow` · `claim_approved` · `claim_forbidden` |
| `validation_posture` | validators / Quality Gate | `not_validated` · `validated` · `validation_failed` |
| `information_gain_posture` | **Information-Gain reviewer (governance role)** | `ig_not_required` · `ig_not_reviewed` · `ig_passed` · `ig_failed` |
| `release_authorization` | `release_ledger.json` | `not_authorized` · `authorized` · `withdrawn` |

Plus two **independent modifiers**:
- (IP-2) `indexation_hold ∈ {none, held}`, owner = SEO/governance role — suspends indexation without changing publication.
- (⚠ IP-16.2) `legacy_holding ∈ {none, legacy_public_holding}`, owner = migration governance — a **migration-only** flag, assignable **only** to a route that was publicly deployed **before Contract C ratification** and whose disposition is incomplete. It **never grants indexation**, **cannot be assigned to a newly created route**, and **expires** when the route is consolidated, promoted, redirected, or retired.

**Total derive function** `derive(governance, evidence, claim, validation, ig, release, hold, legacy) → (publication_state, indexation_state)`, evaluated by first match; the ordered rules are provably exhaustive:

```
R0  release == withdrawn                                  -> (not_public,      noindex)
RL  legacy == legacy_public_holding                       -> (public_noindex,  noindex)
      # migration-only (IP-16.2). Precondition enforced by validator: route.pre_ratification_public == true
      # AND route is NOT newly created. Never index. Withdrawal (R0) still overrides. Not reachable for new objects.
R1  release == not_authorized                             -> (not_public,      noindex)
R2  governance ∈ {planned, relationship_qualified}        -> (not_public,      noindex)
R3  validation ∈ {not_validated, validation_failed}       -> (not_public,      noindex)
R4  claim ∈ {claim_pending, claim_forbidden}              -> (not_public,      noindex)
R5  evidence == evidence_collecting                       -> (not_public,      noindex)
    # From here: legacy == none, governance ∈ {reference_draft, governed}, validation == validated,
    # claim ∈ {not_required, approved_narrow, approved}, evidence ∈ {not_required, sufficient, locked},
    # release == authorized.
R6  governance == reference_draft                         -> (not_public,      noindex)   # ⚠ IP-16.2: NEW objects are not public while drafting (Knowledge-Object-Before-URL)
R7  ig == ig_not_reviewed                                 -> (not_public,      noindex)   # ⚠ IP-16.2: no URL before IG review
R8  ig == ig_failed                                       -> (not_public,      noindex)   # ⚠ IP-16.2: IG failure = does not justify an independent URL (becomes module/section/edge/node/consolidation input)
    # From here: governance == governed AND ig ∈ {ig_passed, ig_not_required}.
R9  evidence == evidence_sufficient (not yet locked)      -> (public_noindex,  noindex)   # passed IG + evidence sufficiency; awaits source-lock to index
R10 (factual path)  evidence == evidence_locked
     AND claim ∈ {claim_approved, claim_approved_narrow}  -> (public_indexable, index_approved*)
R11 (non-factual path, IP-4) evidence == evidence_not_required
     AND claim == claim_not_required
     AND non_factual_class_certified == true              -> (public_indexable, index_approved*)
R12 otherwise (e.g. evidence_not_required but claim still
     required, or mixed) -> SAFE DEFAULT                  -> (not_public,      noindex)   # ⚠ IP-16.2: default denies a URL, never a silent public_noindex
*  indexation_state = noindex if indexation_hold == held, else index_approved   (IP-2)
```

**Exhaustiveness argument (property-spec, not code):**
- Every input value appears in at least one guard; R0 (withdrawal) and RL (legacy) take highest precedence; R1–R5 catch all "any-blocking" values; R6–R9 partition the remaining `reference_draft`/`ig`/`evidence-sufficient` cases for **new** objects; R10–R11 are the only two doorways to `public_indexable`; **R12 is a catch-all SAFE DEFAULT** so **no combination is unmatched.** The default is now **`not_public`** (the most restrictive state), never a silent `public_noindex`.
- **Reachability:** every canonical state is returned by ≥1 rule — `not_public` (R0–R8,R12), `public_noindex` (RL, R9), `public_indexable` (R10–R11); `noindex` and `index_approved` both reachable (R10/R11 with `hold=none`). `index_candidate` was removed (IP-16.1) precisely because no rule returns it.
- **Property tests to encode — CANONICAL SET = SEVEN (⚠ reconciled, IP-16.4).** *Reconciliation of the earlier "four vs six" inconsistency:* the original draft named four (totality, monotonic veto, all-green, hold isolation); IP-16.2 correctly added two genuinely necessary invariants (new-object law, legacy isolation); the implementation approval additionally requires an explicit **determinism** test. Two additions beyond the original four are therefore justified and named below; the canonical set is **seven**, each with a precise invariant:
  1. *Totality:* for the full Cartesian product of input values, `derive` returns exactly one `(publication_state, indexation_state)` — no exception, no null.
  2. *Determinism:* identical inputs always yield identical outputs (pure function, no hidden state).
  3. *Monotonic veto:* flipping any single posture to a blocking value never *raises* the output above its prior level.
  4. *All-green indexability:* `index_approved` ⇒ legacy=`none` ∧ governance=`governed` ∧ validation=`validated` ∧ release=`authorized` ∧ ig∈{passed,not_required} ∧ hold=none ∧ ((evidence_locked ∧ claim_approved*) ∨ non-factual-certified).
  5. *Hold isolation:* `indexation_hold=held` changes only `indexation_state`, never `publication_state`.
  6. *New-object law (IP-16.2):* for `legacy=none`, no `reference_draft`/`ig_not_reviewed`/`ig_failed` route is ever public → new objects reach a URL only after evidence sufficiency **and** IG.
  7. *Legacy isolation:* `legacy_public_holding` ⇒ output is exactly `(public_noindex, noindex)` (never index), is rejected by validator for any newly created route, and is overridden only by withdrawal (R0).

  *Implemented as exactly these seven in `scripts/governance_scaffolding/contract_c_property_tests.py`; result PASS over 23,040 combinations.*

## IP-2 — Release authorization: withdrawal vs suspension (non-overlapping terms)

The five terms now have disjoint meanings:
| Term | Owner | Effect |
|---|---|---|
| **authorization** | release_ledger | permission to be public at all (`authorized`/`not_authorized`) |
| **publication** | derived | whether content is served (`not_public`/`public_noindex`/`public_indexable`) |
| **indexation** | derived | whether search may index (`noindex`/`index_approved`) |
| **withdrawal** | release_ledger | authorization revoked → **`not_public` + `noindex`** (content pulled; corrects v1's "at most public_noindex") |
| **suspension / `indexation_hold`** | SEO-governance role | authorization **intact**, page stays served, but temporarily **out of search** (`indexation_state = noindex`) |

"Keep an authorized page public but out of search" is now `indexation_hold=held`, **not** withdrawal. `not_authorized` is explicitly handled by R1 (never falls through).

## IP-3 — Posture-enum canonicalization

Audited every state name across posture definitions, transition tables, `derive()`, migration map, and the DECISION_LOG draft. Canonical enums are exactly those in IP-1. Corrections:
- **Removed** the stray `claim_required_unresolved` (v1 floor rule); the unresolved case is `claim_pending`.
- `evidence` uses the IP-1 four values only (no `source_required_unresolved` inside evidence; that condition lives in source posture, IP-5).
- Each name is now **defined once, used consistently**; no aliasing of semantically distinct states.

## IP-4 — Non-factual indexable pages (narrow, no loophole)

Some methodology / navigation / governance / corpus-orientation pages make **no externally factual assertion** and legitimately need no source-bound claim. They may reach `public_indexable` via **R11**, but only under a hard gate:
- The route's **`page_type` belongs to a governed `non_factual_class`** (e.g. `PT_METHODOLOGY_GOVERNANCE`, `PT_MULTILINGUAL_HUB`, index/map, corpus-status) **AND**
- a **validator certifies `non_factual_class_certified = true`** — i.e. it contains no sentence asserting an external fact that would require evidence (no chemistry/economic/legal/quantitative claim). **AND** governance=`governed`, validation=`validated`, release=`authorized`, ig∈{passed,not_required}, hold=none.
- `evidence_not_required` / `claim_not_required` are **only** honored for such certified classes. **A factual page cannot self-declare them** — the certifier inspects content and fails any page that makes an evidence-bearing assertion. This is *not* a rescue path for thin dossier pages (they assert facts and would fail certification, and would fail Information-Gain regardless).

## IP-5 — Source vs Evidence vs Claim: three independent postures

The atomic chain is redefined so no layer duplicates another's authority:

```
source  →  evidence assertion  →  claim  →  knowledge object
```
| Posture | Question | Owner (sole writer) | States |
|---|---|---|---|
| **source posture** | Is the *source* identified, authoritative for the permitted use, and locked? | `source_registry.json` (`status`, `source_lock_status`) | `seeded` · `verified` · `verified_limited` · lock: `candidate`/`locked` |
| **evidence_review_posture** | Was *this specific fact* extracted correctly from that source and scope-reviewed? | evidence record | `unreviewed` · `extracted` · `scope_reviewed` · `evidence_verified` |
| **claim posture** | Is the *statement we intend to make* approved for its use? | `claims/*.json` | per IP-1 |

**Derived `evidence_posture`** (used by Contract C) is a function of **both** source eligibility/lock **and** `evidence_review_posture` — e.g. `evidence_locked` requires `source_lock_status=locked` **and** `evidence_review_posture=evidence_verified`. They remain independent facts owned by different files; neither is copied into the other. This removes the v1 error of reusing `source_registry` verification vocabulary inside evidence files.

## IP-6 — De-duplicated evidence fields (one fact, one owner)

Applying *one fact → one authoritative owner → all else derived*:
- **`source_type` REMOVED from the evidence schema** — it is authoritative in `source_registry.json`; evidence **references `source_id` and derives** the type. (No drift.)
- **`used_by` REMOVED as an editable field.** Links are one-directional: **knowledge objects / claims → evidence_ids**. The reverse (`evidence → consumers`) is **derived by an index/validator**, never hand-maintained. (Prevents a second two-authority fork at the evidence layer.)
- General audit result: no other evidence field copies authoritative data from source/claim/ontology; all cross-references are by ID.

## IP-7 — `confidence` governed or removed

`confidence: high|medium|low` had no methodology → **removed from the minimal schema** for now. BISULFID will not expose subjective confidence labels. Evidentiary limitation is expressed instead by **governed, defined facts**: `evidence_review_posture`, `source.status`/`source_lock_status`, `risk_class`, and explicit `temporal_scope`/`allowed_uses`/`prohibited_uses`. A future `confidence` may return only with a written rubric (what it measures, who assigns it, criteria per level, whether it affects publication).

## IP-8 — Corrected MoS₂ source-pack interpretation

**Corrected (verified against `source_pack_registry.json`):** `SPK-SPEKTRUM-MOS2-DE` has **`verification_state: verified_limited`** and **`publication_status: narrow_release_only`**; the registry's own `status` is `architecture_active`. v1's "status None → not verified" was wrong (it looked for a generic `status` key that packs don't carry). **However, the conclusion stands:** `verified_limited` / `narrow_release_only` is *not* route-publication authorization — it explicitly scopes a narrow German dictionary entry (`allowed_claims: [CLM-TERM-MOS2-DE-001]`, `covered_route_patterns: [de_core_mos2]`) and does not, by itself, satisfy Contract C's `release_authorization`, `evidence_locked`, active-claim-registry, validation, or Information-Gain requirements. The MoS₂ proof-trace verdict (**not publishable**) is unchanged.

## IP-9 — Concept ↔ Lexeme ontology analysis

Auditing `sulfur_terms.json`, the ontology currently **conflates two things** in one node type:
- a **language-neutral Concept/Entity** (the chemical/material thing), and
- a **language-specific Lexeme/Term** (a textual form naming it), via `language_vector`.

Evidence: nodes like `sulfid` (`["de"]`) vs `sulfide` (`["en"]`) are really *lexemes* of one concept, while `molybdenum_disulfide` (`["en"]`) is being used as *both* the concept and its English lexeme. This conflation is safe at EN/DE scale but breaks when AR/ZH/JA/FR/ES arrive (a concept cannot "be" one language).

**Proposed minimal distinction (design only, no ontology change now):**
```
Concept/Entity   (language-neutral)   e.g. CONCEPT: molybdenum_disulfide (MoS₂)
   has-lexeme →  Lexeme (en): "Molybdenum disulfide"
   has-lexeme →  Lexeme (de): "Molybdän(IV)-sulfid"
```
Claims and evidence attach at the correct level: a **lexeme-level** claim (German dictionary form) vs a **concept-level** claim (identity/chemistry). This can likely be represented **within** `sulfur_terms.json` by adding an explicit `node_type: concept|lexeme` and a `concept_ref` on lexeme nodes — a *minimal* layering, not a new ontology. Final choice (in-file typing vs a small separate lexical layer) is an **owner semantics decision**, deferred.

## IP-10 — Does MoS₂ require an ontology mutation? (No — evidence/lexeme linkage)

`ontology.source_ids` semantics are **undefined today** — it could mean "source proves entity existence," "proves a lexical form," "supports the node generally," or "supports a relationship." Until defined, attaching the **narrow German Spektrum source** to the **en-tagged concept node** would **overstate** what the source proves (a German lexeme entry ≠ proof of the language-neutral entity). Therefore:
- **The correct linkage is via an atomic evidence assertion:** `German lexeme "Molybdän(IV)-sulfid" → EVD (Spektrum) → CLM-TERM-MOS2-DE-001 → concept molybdenum_disulfide`.
- **No `language_vector` change and no `source_ids` mutation is justified.** The MoS₂ "gaps" are **not data-integrity errors**; they are symptoms of the unresolved Concept↔Lexeme boundary (IP-9).

## IP-11 — Vocabulary registration vs instance evidence-qualification

Distinguish **existence of a controlled term** from **truth of an instantiated use**. Evidence is required only for the latter.

| Layer | Requires evidence to exist? | Requires evidence to be *used/asserted*? |
|---|---|---|
| **subject_domain** vocabulary (`registered`/`reserved`) | No — may register `physics` as a future domain | Yes — `evidence_active` domain requires a verified evidence record using it |
| **geography** record (controlled place identity) | No — Germany/Morocco/China exist as places | — |
| **relationship_class** (`importer`, `producer`, `terminology_origin`, …) | No — class is a schema concept, governed independently | — |
| **relationship *instance*** `entity → class → geography → period` | — | **Yes** — e.g. `ENTITY-X → importer → Morocco → 2025` needs a verified source |

**Refined geography model (corrects v1):** a place is **not** `reserved|evidence_qualified`. Instead:
- **geography record** = controlled place identity (always simply "exists").
- **relationship instance** carries the qualification: `unqualified | evidence_collecting | evidence_qualified`.

This removes the confusion between *"we have not proved a sulfur relationship with Morocco"* and *"Morocco is not a qualified geography."* Morocco is a valid place; the **relationship instance** is what remains `evidence_collecting`. Same split applies to subject_domain (reserved name vs evidence-active) and relationship-class (defined class vs evidenced instance).

## IP — Revised first implementation sprint file list (supersedes Deliverable 8 / final report)

Scaffolding only; **no public HTML, sitemap, robots, indexation, source status, or claim status changes:**
- `DECISION_LOG.md` — append the **principle-only** ratification (IP-15 below).
- **New empty/seed registries:** `subject_domain_registry.json` (with `registered` vs `evidence_active` split), `geography_registry.json` (place identities only), `jurisdiction_registry.json`, `relationship_class_registry.json` (classes defined, instances empty).
- **New evidence store** `main/data/evidence/` — directory + schema (IP-5 `evidence_review_posture`; **no `source_type`/`used_by`/`confidence`**, IP-6/IP-7) + schema validators + **test-only fixtures only**. ⚠ **No real `EVD-MOS2-DE-001` record** — deferred to the *next* sprint, after the Concept↔Lexeme representation is ratified and a governed lexeme ID exists (IP-16.3). No source/claim status changed.
- **Derived-state function specification + property tests** (IP-1) as spec artifacts, **unwired from deploy**.
- **Information-Gain calibration skeleton** `main/data/information_gain/calibration_pairs.json` (empty).
- **REMOVED from the sprint (deferred to owner decision):** any `ontology/sulfur_terms.json` mutation — no `language_vector` change, no `source_ids` addition (IP-9/IP-10).
- **No change** to `routes.json`, `release_ledger.json`, `site/public/**`, sitemaps, robots, CI behavior.

## IP-15 — Revised ratification draft (principle vs implementation constants)

Replace Deliverable 9's Decision 1 wording so the log claims only what is settled:

> **Ratified principle (owner-approved):** Contract C — Derived Canonical State — is the target publication authority: publication and indexation are **derived**; **no single legacy file (`routes.json` or `release_ledger.json`) independently controls indexation**; `routes.json` owns governed route posture, `release_ledger.json` owns release authorization + history, evidence/claim/validation/Information-Gain own knowledge sufficiency.
>
> **NOT yet ratified (pending this integrity pass being implemented and reviewed):** the exact transition constants and the total `derive` truth table (IP-1); withdrawal vs `indexation_hold` semantics (IP-2); the non-factual indexable path (IP-4); source/evidence/claim posture separation constants (IP-5); and the ontology **Concept↔Lexeme** semantics (IP-9). These are **implementation constants**, ratified only after the total state machine and the Concept/Lexeme decision are finalized.

Decisions 2–6 (supersession-with-history, semantic dimensions, new registries, knowledge-object-before-URL, no-arbitrary-IG-threshold) stand as principles.

---

# Integrity Pass — Final Report

**Which architecture decisions are now truly final:**
- Contract C **as a principle** (derived state; no single legacy file controls indexation).
- The **six-input + hold** posture model with **Information-Gain as an explicit posture** (IP-1).
- **Withdrawal = `not_public`+`noindex`; suspension = `indexation_hold`** (IP-2) — terms disjoint.
- **Source ≠ Evidence ≠ Claim** as three independently-owned postures (IP-5).
- **One-fact-one-owner**: `source_type` and `used_by` removed/derived; `confidence` removed (IP-6/IP-7).
- **Vocabulary existence ≠ instance truth**; geography qualification lives on the **relationship instance**, not the place (IP-11).
- **Knowledge-object-before-URL** law (unchanged).

**Which semantics remain unresolved (need owner judgment):**
- Ontology **Concept↔Lexeme** boundary — in-file `node_type` layering vs a small separate lexical layer (IP-9). *Blocks any MoS₂ ontology touch.*
- Exact **derive() transition constants** and the certified **`non_factual_class`** list (IP-1/IP-4).
- **Source-lock workflow + claim-registry activation** policy (unchanged from prior sprint).
- Which **reserved domains / relationship classes** activate, and **new-audience** admissions.

**Is Contract C now a total deterministic state machine?**
**Yes — as a specification, now also implemented and passing.** With Information-Gain as an explicit input, the ordered rules R0–R12 include a catch-all SAFE DEFAULT, so every combination of input postures maps to exactly one `(publication_state, indexation_state)`; the **canonical seven** property tests (totality, determinism, monotonic veto, all-green indexability, hold isolation, new-object law, legacy isolation — reconciled in IP-16.4) are specified and PASS over 23,040 combinations in `scripts/governance_scaffolding/`. It is deterministic and total; it remains **unwired from deploy/CI**, and its transition constants are not yet ratified.

**Does MoS₂ require an ontology mutation, or only evidence/lexeme linkage?**
**Only an evidence/lexeme linkage.** The correct path is a single atomic evidence assertion (German lexeme → Spektrum source → `CLM-TERM-MOS2-DE-001` → concept). **No `language_vector` change and no `source_ids` mutation is justified**, and both are removed from the first sprint until the Concept↔Lexeme audit is decided.

**Revised exact scope of the first implementation sprint:**
Governance **scaffolding only** — append the *principle-only* DECISION_LOG entry (IP-15); create the four new registries (with vocabulary-vs-instance splits); create the evidence **directory + schema + validators + test-only fixtures** (⚠ **no real evidence object**, IP-16.3); lay down the derive() **spec + property tests** unwired from deploy; create the empty Information-Gain calibration file. **No Concept/Lexeme records, no ontology mutation, no public HTML, no sitemap/robots/indexation change, no source/claim status change, no CI hard-fail, no PR.** The real MoS₂ evidence record is the first object of the *next* sprint, after Concept↔Lexeme ratification.

**Stop.** Design updated. Implementation **not** begun.

---

## IP-16 — Final consistency corrections

**READ-ONLY. 2026-09-19.** Three small closures; authoritative where they touch earlier text.

### IP-16.1 — `index_candidate` removed (unreachable)
No R-rule ever returned `index_candidate`. Rather than keep an unreachable state, it is **removed** from the canonical `indexation_state` enum. **Canonical enums are now:** `publication_state ∈ {not_public, public_noindex, public_indexable}`; `indexation_state ∈ {noindex, index_approved}`. Every canonical state is reachable (IP-1 reachability line).

### IP-16.2 — Knowledge-Object-Before-URL enforced in the state machine
The ratified law — *"independent URL promotion occurs only after evidence sufficiency AND Information-Gain review"* — is now enforced by `derive()`, not just stated. For **new** objects (`legacy=none`): `reference_draft → not_public/noindex` (R6), `ig_not_reviewed → not_public/noindex` (R7), `ig_failed → not_public/noindex` (R8), and the SAFE DEFAULT is `not_public` (R12). An IG failure means the object does **not** justify an independent URL; it may instead become a module, section, relationship edge, table/data object, machine-readable node, or a consolidation input.

**Legacy isolation (new-object law not weakened for legacy debt).** A separate migration-only posture `legacy_public_holding` (rule RL) keeps *already-public, pre-ratification* 14K URLs reachable as `public_noindex` during controlled migration. Its validator-enforced requirements: (a) route was publicly deployed **before** Contract C ratification; (b) disposition not yet complete; (c) **never grants indexation**; (d) **cannot be assigned to a newly created route**; (e) **expires** on consolidation / promotion / redirect / retire. This cleanly separates *new publication eligibility* from *temporary preservation of historically public URLs*, so `public_noindex` cannot become the next loophole for weak new pages.

### IP-16.3 — No real MoS₂ evidence object before a governed lexeme ID
The German lexeme "Molybdän(IV)-sulfid" has **no governed identity/ID** yet, because the Concept↔Lexeme decision (IP-9) is unresolved. Creating `EVD-MOS2-DE-001` now would make the first **semantic orphan** in the evidence system (an evidence record whose subject is an ungoverned, free-text lexical string). Therefore `EVD-MOS2-DE-001` is **removed from the first sprint.** The first sprint may create only the evidence **directory, schema, schema validators, and explicitly test-only fixtures** (non-governed). The real chain is created in the *next* sprint, after Concept↔Lexeme ratification, with stable IDs:
```
concept_id ↔ lexeme_id → evidence_id → source_id → claim_id
```
A free-text lexical string is never a substitute for a governed lexeme ID.

### IP-16.4 — Property-test count reconciled to seven
The earlier text was inconsistent (one place said "four," another "six"). Reconciled: the canonical set is **seven** — Totality, Determinism, Monotonic veto, All-green indexability, Hold isolation, New-object law, Legacy isolation. Justification: the original four omitted the two invariants IP-16.2 introduced (new-object law, legacy isolation) and the determinism check the implementation requires; these are genuinely necessary and now defined with precise invariants (IP-1 list). Implemented verbatim in `scripts/governance_scaffolding/contract_c_property_tests.py` (PASS, 23,040 combinations). No test was invented without a named invariant.

### Revised first implementation sprint (final — scaffolding only)
1. Append the **principle-only** Contract C entry to `DECISION_LOG.md`.
2. Create the four semantic registries: `subject_domain_registry.json`, `geography_registry.json`, `jurisdiction_registry.json`, `relationship_class_registry.json` (vocabulary defined; instances empty).
3. Create the empty atomic evidence architecture: directory + schema + spec + schema validators/tests; **test-only fixtures only; no real evidence object.**
4. Create the final Contract-C `derive()` specification + the **canonical seven** property tests (IP-16.4), **unwired from deploy.**
5. Create the empty Information-Gain calibration dataset/schema.
6. **No Concept/Lexeme records.**
7. **No ontology modification.**
8. **No route/release/source/claim state change.**
9. **No HTML/sitemap/robots/indexation change.**
10. **No CI hard-fail.** (No PR.)

---

# Integrity Pass — Closing Answer

1. **Final canonical enums.** `publication_state ∈ {not_public, public_noindex, public_indexable}`; `indexation_state ∈ {noindex, index_approved}`. (Inputs: governance, evidence, claim, validation, information_gain, release_authorization; modifiers: indexation_hold, legacy_holding.)
2. **Every canonical state reachable?** Yes. `not_public` ← R0–R8/R12; `public_noindex` ← RL (legacy) and R9; `public_indexable` ← R10/R11; `noindex` and `index_approved` both reachable via R10/R11 (with/without `indexation_hold`). The unreachable `index_candidate` was removed.
3. **Behavior of `reference_draft` / `ig_not_reviewed` / `ig_failed` for NEW objects.** All three → **`not_public / noindex`.** New objects are never public before evidence sufficiency **and** IG; an IG failure denies an independent URL (the object becomes a module/section/edge/table/node/consolidation input).
4. **Legacy `public_noindex` isolation.** Only routes carrying the migration-only `legacy_public_holding` flag (pre-ratification, already-public, disposition incomplete) may sit at `public_noindex` via RL; it never grants index, cannot be assigned to a new route, and expires on disposition. New-object rules are unchanged by it, so `public_noindex` is not a loophole for weak new pages.
5. **MoS₂ evidence.** Confirmed: **no real MoS₂ evidence object will be created before a governed lexeme ID exists.** The first sprint builds only the evidence directory/schema/validators and test-only fixtures; `EVD-MOS2-DE-001` is deferred to the post-Concept↔Lexeme sprint with stable `concept_id ↔ lexeme_id → evidence_id → source_id → claim_id`.
6. **Final first-sprint file scope.** `DECISION_LOG.md` (principle-only entry) · four new registries (`subject_domain_registry.json`, `geography_registry.json`, `jurisdiction_registry.json`, `relationship_class_registry.json`) · `main/data/evidence/` (dir + schema + validators + test-only fixtures) · derive() spec + property-test files · empty `main/data/information_gain/calibration_pairs.json`. **Untouched:** ontology, `routes.json`, `release_ledger.json`, sources, claims, `site/public/**`, sitemaps, robots, CI behavior.

**Stop.** Design updated; implementation **not** begun.

---
*Authority & Dimension Reconciliation + Architecture Integrity Pass (incl. IP-16) — READ-ONLY design package. No production files modified.*

---

> **Update — Concept↔Lexeme Resolution sprint (2026-09-19).** The Concept↔Lexeme question left open in IP-9/IP-10 is now resolved (Option B): concepts stay language-neutral in `sulfur_terms.json`; lexemes live in the new `main/data/lexeme_registry.json`. The Deliverable-3 evidence schema is updated accordingly — generic `entities` → `concept_ids` + `lexeme_ids`, new `claim_level ∈ {concept,lexeme,relationship}`, and **`risk_class` removed** (no independent meaning). The first real governed evidence record (`EVD-MOS2-DE-001`, lexeme-level) now exists and derives to `(not_public, noindex)`. Full design, ontology-node audit, and the GEO/jurisdiction/source-taxonomy corrections: `main/data/CONCEPT_LEXEME_MODEL.md` and the DECISION_LOG entry of the same date.
