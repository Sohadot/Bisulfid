# Named Source Candidate Intake Wave 1 — Report

**Sprint:** 5N-G  
**Date:** 2026-05-29  
**Branch:** `claude/sprint-5n-g-named-source-candidate-intake-wave-1`

---

## Why this sprint exists

Sprint **5N-F** identified `de_core_mos2` as the **only conditional** source-registry-proposal-readiness candidate, but explicitly recorded **named source candidate present: no**. Proposal readiness is not proposal drafting, and proposal drafting is not registry execution. Sprint **5N-G** performs **named source candidate intake** — determining whether a human has actually provided a **specific, reviewable** German specialist lexicon candidate for MoS2 compound naming under `SOURCE_POLICY` — without adding registry rows, approving sources, or modifying content.

---

## Why named source intake comes after proposal readiness

| Stage | Sprint | Question answered |
| --- | --- | --- |
| External verification | 5N-E | What evidence **family** and authority class apply? |
| Proposal readiness | 5N-F | May proposal **drafting** be considered later, and under what conditions? |
| **Named candidate intake** | **5N-G** | Has a human **named** a specific candidate for review? |
| Proposal drafting (future) | 5N-H (planned) | Can a registry **proposal document** be authored? |
| Registry execution (future) | separate sprint | May `source_registry.json` be modified? |

Readiness without a named candidate cannot advance to proposal drafting without inventing bibliographic details — forbidden by doctrine.

---

## Why named intake still comes before source_registry edits

| Reason | Detail |
| --- | --- |
| Registry inactive | `source_registry.json` status **inactive** |
| Intake ≠ registration | Naming a candidate class is not a registry entry |
| Intake ≠ approval | Named candidate remains **candidate only** until verified and approved in separate sprints |
| Guardrail gate | Sprint **5N-B** runtime must **PASS** |
| Marker discipline | `[SOURCE REQUIRED]` remains until audited linkage |
| No invented bibliography | DOI, ISBN, edition, author, publisher, date, page numbers forbidden without human verification |

---

## Relationship to Sprint 5N-F

Sprint **5N-F** set `de_core_mos2` to `proposal_readiness_conditional` with posture `can_prepare_proposal_draft_after_named_source` and **named source candidate present: no**. Sprint **5N-G** executes the intake step 5N-F deferred: confirm whether a named candidate exists and document intake posture.

**Original repository-internal finding:** **`named_candidate_absent`** — no human-named specific lexicon work in repository artifacts at initial intake review.

**Updated finding (after external human review):** External human review identified **named candidate targets** for `de_core_mos2`. Intake re-classified to **`named_candidate_requires_external_verification`**. All listed targets remain **candidates only — not approved**. Source registry proposal drafting **remains blocked** until human verification confirms authority fit and `SOURCE_POLICY` fit.

---

## Relationship to Sprint 5N-E

Sprint **5N-E** classified `de_core_mos2` as `human_external_verification_required` with authority class `chemistry_dictionary_authority` and evidence family **DE specialist chemistry lexicon entry for MoS2 compound naming**. That is an **evidence family**, not a named source. Sprint **5N-G** confirms the family was never replaced by a human-named specific lexicon work in repository governance artifacts.

---

## Relationship to Sprint 5N-B guardrail automation

Pre-flight and post-sprint: guardrail + corpus L1 + L2 production runtimes **PASS**. Intake documents must not introduce approval language, raw URLs (unless `SOURCE_POLICY` allows — it does not for these docs), registry-edit implications, or source-locking language.

---

## Relationship to Sprint 5O-A production automation

Sprint **5O-A** established L2 read-only production planning. L2 planner reports `production_can_safely_proceed: no` and source registry **inactive**. Named source intake advances **source governance sequencing** without triggering production waves, route registration, or draft mass generation.

---

## Relationship to Sprint 5O-B production dry-run planning

Sprint **5O-B** documented **83** dry-run route candidates with per-row **source gate required: yes** for terminology pages. Dry-run planning explicitly recommended **5N-G** as the next source-track sprint for `de_core_mos2`. Route Registration Wave 2 execution remains **not approved**; source intake does not clear route-registration blockers.

---

## Relationship to 500-page sovereign launch threshold

| Metric | Value |
| --- | ---: |
| Launch threshold | **500** governed pages |
| Current route count (`routes.json`) | **126** |
| Named intake target | **1** draft (`de_core_mos2`) |
| Named candidate targets documented | **4** (all **unapproved**) |
| Registry entries added | **0** |
| Publication-ready pages | **0** |

Named source intake advances **authority discipline** toward governed pages without incrementing launch-eligible page count.

---

## Files reviewed

- `main/data/SOURCE_REGISTRY_PROPOSAL_READINESS_WAVE_1_REPORT.md`
- `main/data/SOURCE_REGISTRY_PROPOSAL_READINESS_MATRIX_WAVE_1.md`
- `main/data/SOURCE_REGISTRY_PROPOSAL_DRAFTING_CRITERIA_WAVE_1.md`
- `main/data/SOURCE_REGISTRY_PROPOSAL_BLOCKERS_WAVE_1.md`
- `main/data/SOURCE_REGISTRY_PROPOSAL_NEXT_ACTIONS_WAVE_1.md`
- `main/data/SOURCE_REGISTRY_PROPOSAL_READINESS_VALIDATION_REPORT.md`
- `main/data/EXTERNAL_SOURCE_VERIFICATION_WAVE_1_REPORT.md`
- `main/data/EXTERNAL_SOURCE_VERIFICATION_MATRIX_WAVE_1.md`
- `main/data/EXTERNAL_SOURCE_VERIFICATION_AUTHORITY_REVIEW_WAVE_1.md`
- `main/data/HUMAN_CANDIDATE_SOURCE_REVIEW_MATRIX_WAVE_1.md`
- `main/data/CANDIDATE_SOURCE_DISCOVERY_MATRIX_WAVE_1.md`
- `main/data/SOURCE_CLAIM_AUTOMATION_VALIDATION_REPORT.md`
- `main/data/PRODUCTION_DRY_RUN_WAVE_PLANNING_REPORT.md`
- `main/data/PRODUCTION_DRY_RUN_NEXT_ACTIONS.md`
- `doctrine/SOURCE_POLICY.md`
- `scripts/corpus_production_runtime_l2.py` (read-only)
- `scripts/corpus_production_planner_l2.py` (read-only)
- `scripts/corpus_validation_runtime_l1.py` (read-only)
- `scripts/source_claim_guardrail_runtime_l1.py` (read-only)
- `main/data/routes.json` (read-only)
- `main/data/internal_links.json` (read-only)
- `main/data/sources/source_registry.json` (read-only)
- `main/data/claims/terminology_claims.json` (read-only)
- `main/content/de/pages/terminology/molybdenum-disulfide.md` (read-only)
- `DECISION_LOG.md`

---

## Pre-flight confirmation

| Check | Result |
| --- | --- |
| Branch based on main after Sprint 5O-B | **Yes** |
| L2 production runtime | **PASS** |
| Corpus L1 runtime | **PASS** |
| Guardrail runtime | **PASS** |
| Planner: 126 routes, 68 draft-backed, 58 missing, all locks **LOCKED**, `production_can_safely_proceed: no` | **Yes** |
| `de_core_mos2` exists in routes + content | **Yes** |
| draft / non_public / non-indexable / not in sitemap | **Yes** |
| `source_registry.json` unchanged pre-sprint | **Yes** |
| `terminology_claims.json` unchanged pre-sprint | **Yes** |

---

## Selected draft count

**1** — intake scope is `de_core_mos2` only.

---

## Selected route_id list

```
de_core_mos2
```

---

## Current route count from routes.json

**126** routes (all `planned`; read from `routes.json` `routes` array length, 2026-05-29).

---

## Selected draft status

| route_id | content_file | route status | draft posture |
| --- | --- | --- | --- |
| `de_core_mos2` | `main/content/de/pages/terminology/molybdenum-disulfide.md` | `planned` | draft / non_public / indexable false / in_sitemap false |

---

## Named candidate intake methodology

1. Reviewed Sprint **5N-C** through **5N-F** artifacts for human-provided **named** German specialist lexicon candidates.
2. Applied initial repository-internal intake review — classified **`named_candidate_absent`** when no named targets appeared in repository governance artifacts.
3. Incorporated **external human review** identifying specific named candidate targets for MoS2 (documented below as **candidates only**).
4. Read `de_core_mos2` draft content (read-only) — retains `[SOURCE REQUIRED]` markers; no named source citation added to content.
5. Re-classified intake to **`named_candidate_requires_external_verification`** / **`candidate_requires_human_verification`**.
6. Documented acceptance/rejection rules and role boundaries (primary DE lexicon vs supporting database/technical vs secondary DE support) without inventing bibliographic details or adding registry rows.

---

## What named source candidate intake means in this sprint

- Records whether a **specific, human-provided** source candidate exists for `de_core_mos2`.
- Classifies intake posture for future proposal drafting and registry execution gates.
- Preserves distinction between **evidence family** (DE specialist chemistry lexicon) and **named candidate** (specific work a human can verify).
- Documents rules for accepting or rejecting candidates when humans provide them later.

---

## What named source candidate intake does not mean in this sprint

- **Not** source registration or `source_registry.json` modification.
- **Not** source approval or verified registry status.
- **Not** claim approval or claim registry activation.
- **Not** source-locking or removal of `[SOURCE REQUIRED]` markers.
- **Not** publication readiness or route publication.
- **Not** treating evidence family labels as named candidates.
- **Not** inventing DOI, ISBN, edition, author, publisher, date, or page numbers.

---

## de_core_mos2 intake findings

| Field | Finding |
| --- | --- |
| Evidence family (from 5N-C / 5N-E) | DE specialist chemistry lexicon entry for MoS2 compound naming |
| Authority class | `chemistry_dictionary_authority` |
| Original repository-internal status | **`named_candidate_absent`** |
| External human review | **Named candidate targets identified** (see table below) |
| **Named candidate status** | **`named_candidate_requires_external_verification`** |
| **Source candidate posture** | **`candidate_requires_human_verification`** |
| **Future registry posture** | **`can_prepare_registry_proposal_after_human_verification`** |

### Named candidate targets (candidates only — not approved)

| Role | Candidate target | Candidate function |
| --- | --- | --- |
| **Primary German specialist lexicon** | Spektrum Lexikon der Chemie — Molybdän(IV)-sulfid | German specialist chemistry lexicon candidate for Molybdän(IV)-sulfid / Molybdändisulfid / MoS2 naming |
| **Supporting database** | PubChem — Molybdenum disulfide / CID 14823 | Database support for MoS2 identity — **not** a substitute for German lexical authority |
| **Supporting technical data** | NIST Chemistry WebBook — molybdenum disulphide | Technical data support for formula / CAS / thermochemistry context — **not** primary DE lexicon authority |
| **Secondary German support** | Chemie.de Lexikon — Molybdän(IV)-sulfid | Secondary German-language support only — **not** primary authority |

**Authority boundary:** For the DE route `de_core_mos2`, **Spektrum Lexikon der Chemie** is the **primary** German specialist lexicon candidate. PubChem and NIST are **supporting** candidates for identity and technical context only. Chemie.de is **secondary DE support only** and must not replace Spektrum as primary lexical authority without human verification confirming fit.

All four targets remain **unapproved**, **not source-locked**, and **not** registry entries.

---

## Whether a named candidate was actually provided

**Yes — named candidate targets were provided through external human review** after the original repository-internal finding of **`named_candidate_absent`**.

**No candidate is approved.** Intake records **identities for verification**, not verified registry authority. Human external verification must confirm edition scope, MoS2 naming coverage, `SOURCE_POLICY` alignment, and rejection of lubricant-market drift before proposal drafting may be considered.

---

## Registry proposal drafting status

**Blocked until human verification completes.** Named targets are documented, but source registry proposal drafting (planned Sprint 5N-H) **must not proceed** until human verification confirms:

1. Spektrum entry scope fits MoS2 German naming claims on `de_core_mos2`.
2. PubChem / NIST supporting roles stay within supporting-only boundaries.
3. Chemie.de remains secondary — not elevated to primary without explicit verification.
4. All candidates pass acceptance rules and none trigger rejection rules.

**Source registry execution** remains blocked and requires a **separate future sprint** even after verification clears proposal drafting.

---

## Why sulfur_element_term_record remains on the separate database-candidate track

| Factor | Detail |
| --- | --- |
| Sprint scope | **5N-G** intake is **`de_core_mos2` only** |
| 5N-F posture | `needs_scientific_database_candidate_first` — **blocked** |
| Authority class | `scientific_database_authority` — distinct from DE lexicon track |
| Named database candidate | **Not provided** (unchanged) |
| Action this sprint | **Not advanced** into registry proposal drafting |

`sulfur_element_term_record` requires a **scientific database candidate naming track** — parallel to but separate from MoS2 lexicon intake. No matrix row in this sprint; remains documented as blocked parallel track in next actions.

---

## Why no source entries were added

Intake documents governance posture only. Adding registry rows would bypass named-candidate → verification → proposal → execution sequence.

---

## Why source_registry.json was not modified

Registry remains **inactive** with **0** verified entries. Intake is not registry execution.

---

## Why no claims were approved

Claim registries remain **inactive**. Source intake does not authorize terminology claim approval for MoS2 lines.

---

## Why terminology_claims.json was not modified

No claim boundary registration or approval occurred. Intake precedes claim linkage.

---

## Why no content pages were modified

Draft content is read-only reference. Named intake must not embed unverified citations or remove `[SOURCE REQUIRED]` markers.

---

## Why [SOURCE REQUIRED] markers remain

`de_core_mos2` draft retains markers on lexical and document-form lines. No audited source linkage exists. Intake does not equal source-locking.

---

## Why no routes were published

All **126** routes remain `planned`, non-indexable, out of sitemap and navigation.

---

## Publication blocker summary

| Blocker | Status |
| --- | --- |
| Named source candidate targets | **Documented** — **4** candidates; all **unapproved** |
| Human external verification | **Required** — not yet completed |
| Source registry proposal drafting | **Blocked** until verification confirms authority and policy fit |
| Source registry execution | **Blocked** — separate future sprint |
| Source registry | **inactive** — blocks registry execution |
| Claim registries | **inactive** — 0 approved claims |
| `[SOURCE REQUIRED]` markers | **Unresolved** on `de_core_mos2` |
| Route publication lock | **LOCKED** |
| `production_can_safely_proceed` | **no** |

---

## Recommended next sprint

**Sprint 5N-H prep — human external verification for `de_core_mos2` named candidates** — verify Spektrum primary lexicon fit, PubChem/NIST supporting scope, and Chemie.de secondary-only role under `SOURCE_POLICY` and acceptance/rejection rules.

**Do not proceed to:** source registry proposal drafting (5N-H) until verification completes; source registry editing; claim approval; or content source-locking.

**Parallel (unchanged):** `sulfur_element_term_record` scientific database candidate naming track — **not advanced** in this sprint; Draft Wave 1 backlog reduction (**58** missing drafts); Route Registration Wave 2 execution **not approved**.

---

## Sprint 5N-G deliverables

| File | Purpose |
| --- | --- |
| `NAMED_SOURCE_CANDIDATE_INTAKE_WAVE_1_REPORT.md` | This report |
| `NAMED_SOURCE_CANDIDATE_INTAKE_MATRIX_WAVE_1.md` | Intake matrix (1 row) |
| `NAMED_SOURCE_CANDIDATE_ACCEPTANCE_RULES_WAVE_1.md` | Acceptance criteria |
| `NAMED_SOURCE_CANDIDATE_REJECTION_RULES_WAVE_1.md` | Rejection criteria |
| `NAMED_SOURCE_CANDIDATE_NEXT_ACTIONS_WAVE_1.md` | Next sprint guidance |
| `NAMED_SOURCE_CANDIDATE_VALIDATION_REPORT.md` | Runtime validation |

**Not modified:** `source_registry.json`, `terminology_claims.json`, `routes.json`, content pages, registries, workflows, dependencies, root `README.md`.
