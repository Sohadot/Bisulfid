# Named Source Candidate Acceptance Rules — Wave 1

**Sprint:** 5N-G  
**Scope:** `de_core_mos2` — German specialist lexicon intake  
**Date:** 2026-05-29

---

## Purpose

These rules define when a **human-provided named source candidate** for `de_core_mos2` may be accepted for **future** source registry proposal drafting. Acceptance in intake is **not** source approval, registry entry, or publication authorization.

---

## Criteria for accepting a named source candidate

A named candidate may be accepted for intake classification upgrade (e.g. to `named_candidate_provided_by_human` or `named_candidate_requires_external_verification`) when **all** apply:

1. **Human-provided** — candidate identity supplied by corpus owner or designated human reviewer, not inferred by automation alone.
2. **Specific enough to review** — identifiable work (title + publisher or equivalent stable identifier) sufficient for external verification without inventing bibliographic details.
3. **Authority-class alignment** — candidate fits `chemistry_dictionary_authority` / `authoritative_dictionary` (DE) per `SOURCE_POLICY.md` and Sprint 5N-E findings.
4. **Scope alignment** — lexicon entry supports **MoS2 compound naming in German** — not lubricant market data, application performance claims, or EN-only dictionary substituted without DE verification.
5. **Verifiable later** — human can perform external verification (edition, entry scope, MoS2 naming line) in a subsequent sprint.
6. **Not pre-approved** — intake acceptance classifies candidate as **candidate only**; registry proposal and approval remain separate gates.

---

## Criteria for rejecting a named source candidate

Reject or defer (classify `named_candidate_rejected`) when any apply — see `NAMED_SOURCE_CANDIDATE_REJECTION_RULES_WAVE_1.md` for full rules.

---

## Criteria for German specialist lexicon candidates

| Criterion | Requirement |
| --- | --- |
| Language | **German** lexicon or DE specialist chemistry dictionary — not EN-only without DE verification path |
| Entry scope | MoS2 / Molybdändisulfid / equivalent compound naming — not generic sulfide market vocabulary |
| Authority tier | Recognized reference lexicon or specialist chemistry dictionary class per `SOURCE_POLICY` |
| Drift block | Must not support lubricant industry market framing, procurement, or operational claims |
| Formal nomenclature | Systematic name lines beyond lexicon scope require separate formal authority — lexicon alone insufficient |

---

## Criteria for chemistry dictionary candidates

| Criterion | Requirement |
| --- | --- |
| Dictionary type | Specialist chemistry or chemical terminology dictionary — not general web glossary |
| DE page fit | DE route requires DE-verifiable lexicon source class |
| Claim scope | Compound **naming** and document-language support only |
| Supporting role | Academic teaching reference may be **supporting context only** — not sole authority unless policy allows |
| No market extension | Dictionary entry must not be stretched to industrial economics or trade statistics |

---

## Criteria for human external verification

After a named candidate is accepted for intake, external verification (future sprint) requires:

1. Human confirms entry exists and covers MoS2 German naming scope claimed.
2. Human confirms edition/version identity without repository inventing bibliographic lines.
3. Human confirms no authority-class drift (market, safety, medical, procurement).
4. Verification documented in governance artifacts — still **not** registry approval.

---

## Criteria for authority-class alignment

Named candidate must map to:

- Primary: `authoritative_dictionary` (DE) or equivalent `chemistry_dictionary_authority` tier from Sprint 5N-E.
- Supporting (optional, scoped): `academic_teaching_reference` for terminology context only — not sole authority for contested lines.
- **Forbidden:** market research, safety data sheets as prescriptive authority, procurement guides, lubricant industry reports, unverified web pages.

---

## Criteria for moving from named candidate to future source registry proposal draft

All must be true before Sprint 5N-H (proposal drafting) may be chartered:

1. Intake status ≥ `named_candidate_provided_by_human`.
2. External human verification completed (or `named_candidate_requires_external_verification` cleared).
3. Guardrail + corpus L1 runtimes **PASS**.
4. `source_registry.json` still **not modified** until separate execution sprint.
5. Proposal draft contains **human-verified** bibliographic details only — no AI-invented DOI/ISBN/edition.
6. Claim boundaries for MoS2 lines documented — claim approval still separate.
7. `[SOURCE REQUIRED]` markers **remain** until audited linkage sprint.

---

## Why named source intake does not equal source approval

| Intake | Approval |
| --- | --- |
| Records candidate identity for review | Confirms verified registry entry |
| Classifies governance posture | Activates source-backed claim paths |
| Permits **future** proposal drafting when cleared | Permits source-locking and publication consideration |
| **0** registry rows | Requires inactive → verified registry transition with human sign-off |

---

## Why named source intake does not remove [SOURCE REQUIRED] markers

Markers indicate **unresolved factual lines** pending audited source linkage. Intake names a **candidate** — not an approved, linked source. Removal requires separate source-locking sprint after registry approval and content audit.

---

## Why named source intake does not permit publication

| Gate | Posture |
| --- | --- |
| Route status | `planned` |
| Draft | `non_public` |
| Indexation | false |
| Named candidate | **Absent** in Sprint 5N-G |
| Publication-ready | **0** pages |

Publication requires governed-page threshold, source lock, claim approval, and owner sign-off — none satisfied by intake documentation.

---

## Related documents

- `NAMED_SOURCE_CANDIDATE_REJECTION_RULES_WAVE_1.md`
- `NAMED_SOURCE_CANDIDATE_INTAKE_WAVE_1_REPORT.md`
- `SOURCE_REGISTRY_PROPOSAL_DRAFTING_CRITERIA_WAVE_1.md`
- `doctrine/SOURCE_POLICY.md`
