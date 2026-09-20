# BISULFID — Concept ↔ Lexeme Model (design + minimal schema)

**Sprint:** concept-lexeme-resolution · **Date:** 2026-09-19 · **Status:** ratified-model / minimal-schema
**Baseline:** `DOCTRINE_TO_CORPUS_RECONCILIATION.md`, `BISULFID_AUTHORITY_DIMENSION_ARCHITECTURE.md` (incl. IP-16), scaffolding commit `ae7980fe06`.

**Read-only w.r.t. legacy:** no 14K route, release ledger, public HTML, sitemap, robots, indexation, source status, or claim status was modified. The live ontology `sulfur_terms.json` is **not mutated** this sprint (Option B, below).

---

## 1. Chosen architecture — Option B (concept ontology + separate lexeme registry)

**Concepts** stay in `main/data/ontology/sulfur_terms.json` and are henceforth **governed as language-neutral concept records** (their `term_id` is the `concept_id`). **Lexemes** (language-specific naming forms) live in a new `main/data/lexeme_registry.json`, each with a stable `lexeme_id` and a `concept_id` reference.

**Why Option B over A/C:**
- **Clean multilingual expansion.** Adding Arabic/Chinese/Japanese/French/Spanish forms adds *lexeme records*, never touching the concept graph or forcing English/German morphology onto other scripts.
- **No risky in-place mutation.** The existing 14-node ontology carries ambiguous historical semantics (`language_vector` on nodes that also act as concepts) and is referenced by public pointers; Option A would require editing every node now. Option B needs **zero** ontology edits this sprint.
- **No duplicated authority.** Concept identity lives in one place (ontology); lexical identity in one place (lexeme registry); each fact has one owner.

**Deprecation-in-place (documented, not executed):** `language_vector` on ontology nodes is **superseded** by lexeme records and should be treated as legacy metadata. It is **not deleted** this sprint (that is migration). Internal `concept_id` strings are identifiers, **not** language claims (`molybdenum_disulfide` is not "English").

---

## 2. Ontology node audit & migration mapping (no node modified)

Classification: **concept** (language-neutral thing), **lexeme** (naming form), **conflated** (currently both), **control** (disambiguation), **unresolved**.

| current term_id | current role | proposed future role | proposed concept_id | proposed lexeme_id(s) | migration risk | public URL depends? |
|---|---|---|---|---|---|---|
| `sulfur` | conflated (element S + EN name) | concept + EN lexeme | `sulfur` | `LEX-EN-SULFUR` | low | yes (/what-is-sulfur/) |
| `sulfide` | conflated (S²⁻ class + EN name) | concept + EN lexeme | `sulfide` | `LEX-EN-SULFIDE` | med | yes (/sulfid-vs-sulfide/) |
| `sulfid` | lexeme (DE form of S²⁻) | **lexeme of `sulfide`** | `sulfide` | `LEX-DE-SULFID` | med | yes (/sulfid-vs-sulfide/) |
| `disulfide` | conflated (S–S class + EN) | concept + EN lexeme | `disulfide` | `LEX-EN-DISULFIDE` | low | yes (/disulfide-bonds/) |
| `disulfid` | lexeme (DE form) | **lexeme of `disulfide`** | `disulfide` | `LEX-DE-DISULFID` | low | no |
| `hydrosulfide` | conflated (HS⁻ ion + EN) | concept + EN lexeme | `hydrosulfide` | `LEX-EN-HYDROSULFIDE` | med | yes |
| `bisulfid` | conflated (center; DE+EN identity) | concept-or-lexeme — **DEFER** | *hypothesis:* HS⁻ concept | `LEX-DE-BISULFID`, `LEX-EN-BISULFID` | **high** (center node) | yes (/what-is-bisulfid/) |
| `bisulfide` | conflated (EN form ≈ hydrosulfide) | lexeme/concept — **DEFER** | *hypothesis:* HS⁻ concept | `LEX-EN-BISULFIDE` | **high** | yes (/bisulfid-vs-bisulfide/) |
| `hydrogen_sulfide` | conflated (H₂S + EN) | concept + EN lexeme | `hydrogen_sulfide` | `LEX-EN-HYDROGEN-SULFIDE` | med (risk high) | yes |
| `sodium_bisulfide` | conflated (NaHS + EN) | concept + EN lexeme | `sodium_bisulfide` | `LEX-EN-SODIUM-BISULFIDE` | med | yes (/sodium-bisulfide/) |
| `sodium_hydrosulfide` | conflated (NaHS synonym) | **candidate synonym of `sodium_bisulfide`** — DEFER (needs equivalence evidence) | *pending* | `LEX-EN-SODIUM-HYDROSULFIDE` | med | yes (/sodium-bisulfide/) |
| `molybdenum_disulfide` | conflated (MoS₂ + EN) | **concept** (chain target) | `molybdenum_disulfide` | `LEX-EN-MOLYBDENUM-DISULFIDE`, `LEX-DE-MOS2-001` | low | yes (/molybdenum-disulfide/) |
| `molybdenum_disulfide_mos2` | duplicate/notation ("MoS₂") | **formula_alias lexeme of `molybdenum_disulfide`** — recommend fold (defer) | `molybdenum_disulfide` | `LEX-FORMULA-MOS2` | low | shares page |
| `bisulfite_disambiguation` | control object | **control** (unchanged) | n/a | n/a | low | no |

**Executed this sprint:** only the **`molybdenum_disulfide` concept + its German lexeme** are instantiated in the lexeme registry (evidence-backed). Every other row is a **proposal**, not executed. Nothing is collapsed: `sodium_bisulfide`/`sodium_hydrosulfide` stay distinct pending equivalence evidence (§8 of brief); `bisulfid`/`bisulfide`/`hydrosulfide` HS⁻ grouping is a high-risk hypothesis deferred to migration.

---

## 3. Lexical nuance vocabulary (designed; only what's supported is instantiated)

`lexical_relationship_type ∈` { `preferred`, `accepted`, `historical`, `synonym`, `alternative_spelling`, `formula_alias`, `translated_equivalent`, `partial_equivalence`, `false_friend`, `nomenclature_controlled`, `observed_usage`, `deprecated` }. Only `accepted` is instantiated this sprint (the German MoS₂ dictionary form).

---

## 4. Claim/evidence levels

`claim_level ∈ { concept, lexeme, relationship }`:
- **concept-level** ("Concept X has formula Y") requires `evidence_kind ∈ {scientific, quantitative, legal_regulatory}` — a lexical dictionary entry can **not** satisfy it.
- **lexeme-level** ("German source S records lexical form X") requires `evidence_kind == terminological` and non-empty `lexeme_ids`.
- **relationship-level** ("Lexeme X is an accepted form for Concept Y in context Z") requires a `relationship` reference.

The Spektrum source is **lexeme-level** German evidence only; it must never silently become concept-level chemical evidence for MoS₂.

---

## 5. Corrections made to prior scaffolding (no real data depended on them)

- **GEO-GULF → GEO-GCC.** The record's members were exactly the six GCC states, so it is renamed `GEO-GCC` / "GCC member states". A broader "Gulf region" geographic scope, if needed, will be defined as a separate governed object with its own definition — not silently equated to GCC.
- **Jurisdiction model separated.** `jurisdiction` (legal system/scope) → `authority` (issuing body, references `jurisdiction_id`) → `instrument` (references both). `authority` was **removed** from the jurisdiction record's required fields; a jurisdiction is no longer "authority + instrument." All record lists remain empty.
- **Evidence `risk_class` removed.** See §7.

---

## 6. Source-category gaps for trade/economic relationships (schema integrity only)

`REL-IMPORTER / REL-EXPORTER / REL-PRODUCER / REL-INDUSTRIAL-USER` previously accepted `market_report` / `industry_publication` as sufficient. That is **not** sovereign-grade for importer/exporter/producer instances. Proposed **primary/authoritative** source categories (added to `relationship_class_registry.json` as *proposals to the source taxonomy*, not activated, no sources invented):
`official_customs_data`, `official_trade_statistics`, `national_statistical_authority`, `intergovernmental_trade_database`, `official_production_statistics`.
`market_report` / `industry_publication` are reclassified **secondary/contextual only** for these classes. Adding these to `source_registry.json`'s approved categories is a later, separately-approved governance step.

---

## 7. Decision on evidence `risk_class`

**Removed from the mandatory evidence schema.** Evidence-level "risk" had no independent, defined meaning distinct from **route risk** (`routes.json.risk_level`), **claim risk** (`claims.*.risk_level`), and **source limitations** (`source_registry` `do_not_use_for`). Keeping an unowned scoring field invites drift and subjective labelling (same reason `confidence` was removed in IP-7). Evidentiary limits are expressed instead by `evidence_review_posture`, source lock status, `allowed_uses`/`prohibited_uses`, and `temporal_scope`. If a genuinely independent evidence-risk meaning is later defined with a rubric and owner, it may return.

---

## 8. MoS₂ chain (created this sprint; ends not_public/noindex)

```
concept_id:  molybdenum_disulfide            (ontology, unchanged)
   ↑ names
lexeme_id:   LEX-DE-MOS2-001  "Molybdän(IV)-sulfid"  (lexeme_registry; lexical_relationship_type=accepted; de)
   ↑ supported by
evidence_id: EVD-MOS2-DE-001  (claim_level=lexeme, evidence_kind=terminological, language_of_evidence=de)
   ↑ from
source_id:   SRC-SPEKTRUM-MOS2-DE   (verified; source_lock_status=candidate — UNCHANGED)
   ↳ backs
claim_id:    CLM-TERM-MOS2-DE-001   (approved; registry terminology_claims.json status=inactive — UNCHANGED)
```

**Derived Contract-C state of this object:** `governance=planned` (route `de_core_mos2` unchanged), `evidence=sufficient-but-not-locked` (source lock still `candidate`), `claim` registry inactive, `release=not_authorized`, `ig=not_reviewed` → **`derive()` = (not_public, noindex)**. The object exists and is fully traceable, and it is correctly **not publishable**. No page, no route authorization, no source/claim activation.

---

## 9. Public-URL independence (unchanged, absolute)

Creating a lexeme or evidence record creates **no** URL. `Knowledge Object Before URL` holds: a `/{language}/{term}/` surface is promoted only via evidence sufficiency + Information-Gain review under Contract C.

---

## 10. Semantic Integrity Hardening (sprint update, 2026-09-19)

Four drift risks were closed while the system held only the one MoS₂ chain:

1. **One-fact-one-owner in the lexeme model.** `source_ids`/`evidence_ids` were **removed** from lexeme records (now forbidden fields). The lexeme registry owns lexical identity only; evidence owns `evidence→lexeme/source/claim`. The reverse view `lexeme→evidence` is **derived** (scan evidence store), never stored.
2. **Registration vs derived support.** `lexeme.status = evidence_backed` was replaced by `registration_state` (lexical-identity state, manual). Whether a lexeme is evidence-supported is a **derived** fact from the evidence store — a single authority for that question.
3. **Concept eligibility is governed, not implied by existence.** New sidecar `main/data/ontology_node_roles.json` classifies all 14 legacy nodes; only `concept_eligible` nodes may be `concept_id` targets. Roles assigned: **concept_eligible (6):** sulfur, sulfide, disulfide, hydrosulfide, hydrogen_sulfide, molybdenum_disulfide · **legacy_lexeme (2):** sulfid, disulfid · **conflated_pending_migration (4):** bisulfid, bisulfide, sodium_bisulfide, sodium_hydrosulfide · **notation_alias (1):** molybdenum_disulfide_mos2 · **control_object (1):** bisulfite_disambiguation. The ontology itself is **not** mutated.
4. **MoS₂ claim not broadened.** `lexical_relationship_type` narrowed **`accepted` → `observed_usage`** (the approved claim establishes only that a dictionary entry exists supporting cautious framing, not a general "accepted" status). The evidence `claim_scope` now mirrors `CLM-TERM-MOS2-DE-001` verbatim in scope. The approved claim was **not** modified.

**Relationship grammar (before any instance exists).** Instances are typed directed propositions `subject_ref(subject_type) --[class]--> object_ref(object_type)` with controlled `endpoint_types` {concept, lexeme, geography, jurisdiction, authority, organization}. Each class declares allowed `subject_types`/`object_types`, so a reversed proposition (e.g. concept as subject of `REL-IMPORTER`) is structurally rejected. Canonical orientations: `GEO-* --imports/exports/produces/uses--> concept`; `LEX-* --terminology_context--> geography` (**separate from the lexeme's language**); `jurisdiction --regulates--> concept`. Inverse views are derived; both directions are never stored.

**Language ⟂ Geography.** A `LEX-DE-*` lexeme is German-**language**, not Germany-**geography**. Geography is never derived from lexeme language; it requires its own evidence-qualified relationship. Enforced by forbidding a geography field on lexeme records.

**Corrections to prior scaffolding:** `GEO-GULF → GEO-GCC` (§5); jurisdiction split into `jurisdiction → authority → instrument` (§5); trade/economic relationship classes require primary authoritative source categories (§6, proposals only). `risk_class` removed from evidence (§7).
