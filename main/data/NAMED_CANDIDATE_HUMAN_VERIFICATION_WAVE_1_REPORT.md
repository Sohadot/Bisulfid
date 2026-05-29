# Named Candidate Human Verification Wave 1 — Report

**Sprint:** 5N-H  
**Date:** 2026-05-27  
**Branch:** `claude/sprint-5n-h-named-candidate-human-verification-wave-1`

---

## Why this sprint exists

Sprint **5N-G** documented **four named candidate targets** for `de_core_mos2` through external human review, re-classifying intake from **`named_candidate_absent`** to **`named_candidate_requires_external_verification`**. Naming candidates is not verifying them. Sprint **5N-H** performs **controlled human verification documentation** — confirming whether each named target fits its assigned authority role under `SOURCE_POLICY` — without adding registry rows, approving sources, modifying content, or removing `[SOURCE REQUIRED]` markers.

---

## Why human verification comes after named source intake

| Stage | Sprint | Question answered |
| --- | --- | --- |
| Named candidate intake | 5N-G | Has a human **named** specific candidate targets for review? |
| **Human verification** | **5N-H** | Do named targets fit their **authority roles** and policy boundaries? |
| Proposal drafting (future) | next sprint | Can a registry **proposal document** be authored with human-verified bibliographic lines? |
| Registry execution (future) | separate sprint | May `source_registry.json` be modified? |

Intake records identities; verification records **role-fit findings** — still not approval.

---

## Why human verification still comes before source_registry edits

| Reason | Detail |
| --- | --- |
| Registry inactive | `source_registry.json` status **inactive** |
| Verification ≠ registration | Role-fit confirmation is not a registry entry |
| Verification ≠ approval | Verified-for-proposal is not verified-in-registry |
| Guardrail gate | Sprint **5N-B** runtime must **PASS** |
| Marker discipline | `[SOURCE REQUIRED]` remains until audited linkage after registry execution |
| No invented bibliography | DOI, ISBN, edition, author, publisher, date, page numbers forbidden without direct human verification from the source |

---

## Relationship to Sprint 5N-G

Sprint **5N-G** documented named candidate targets and acceptance/rejection rules. Sprint **5N-H** executes the verification step 5N-G deferred: human review of **Spektrum** as primary German specialist lexicon candidate and bounded review of **PubChem**, **NIST**, and **Chemie.de** supporting roles.

**Post-verification posture:** Spektrum classified **`primary_candidate_verified_for_later_proposal`**. Supporting candidates remain **supporting-only** with explicit rejection as primary German lexical authority. All candidates remain **unapproved**.

---

## Relationship to Sprint 5P-A GitHub Actions governance

Sprint **5P-A** established **Corpus Governance CI** on `main` with branch protection requiring **Corpus governance validation**. Sprint **5N-H** is documentation-only; governance CI must **PASS** before merge. CI passing does **not** constitute source approval, source-locking, or publication readiness.

---

## Relationship to Sprint 5O-A L2 production automation

Sprint **5O-A** established L2 read-only production planning. L2 planner reports `production_can_safely_proceed: no` and source registry **inactive**. Human verification advances **source governance sequencing** without triggering production waves, route registration, or draft mass generation.

---

## Relationship to 500-page sovereign launch threshold

| Metric | Value |
| --- | ---: |
| Launch threshold | **500** governed pages |
| Current route count (`routes.json`) | **126** |
| Human verification target | **1** draft (`de_core_mos2`) |
| Named candidate targets verified | **4** (all **unapproved**) |
| Registry entries added | **0** |
| Publication-ready pages | **0** |

Human verification advances **authority discipline** toward governed pages without incrementing launch-eligible page count.

---

## Files reviewed

- `main/data/NAMED_SOURCE_CANDIDATE_INTAKE_WAVE_1_REPORT.md`
- `main/data/NAMED_SOURCE_CANDIDATE_INTAKE_MATRIX_WAVE_1.md`
- `main/data/NAMED_SOURCE_CANDIDATE_ACCEPTANCE_RULES_WAVE_1.md`
- `main/data/NAMED_SOURCE_CANDIDATE_REJECTION_RULES_WAVE_1.md`
- `main/data/NAMED_SOURCE_CANDIDATE_NEXT_ACTIONS_WAVE_1.md`
- `main/data/NAMED_SOURCE_CANDIDATE_VALIDATION_REPORT.md`
- `main/data/SOURCE_REGISTRY_PROPOSAL_READINESS_WAVE_1_REPORT.md`
- `main/data/SOURCE_REGISTRY_PROPOSAL_READINESS_MATRIX_WAVE_1.md`
- `main/data/EXTERNAL_SOURCE_VERIFICATION_MATRIX_WAVE_1.md`
- `main/data/HUMAN_CANDIDATE_SOURCE_REVIEW_MATRIX_WAVE_1.md`
- `main/data/SOURCE_CLAIM_AUTOMATION_VALIDATION_REPORT.md`
- `main/data/GITHUB_ACTIONS_GOVERNANCE_WORKFLOW_REPORT.md`
- `main/data/GITHUB_ACTIONS_GOVERNANCE_SECURITY_MODEL.md`
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
| Branch based on main after Sprint 5P-A | **Yes** |
| L2 production runtime | **PASS** |
| Corpus L1 runtime | **PASS** |
| Guardrail runtime | **PASS** |
| Planner: 126 routes, 68 draft-backed, 58 missing, all locks **LOCKED**, `production_can_safely_proceed: no` | **Yes** |
| `de_core_mos2` exists in routes + content | **Yes** |
| draft / non_public / non-indexable / not in sitemap | **Yes** |
| `source_registry.json` unchanged pre-sprint | **Yes** |
| `terminology_claims.json` unchanged pre-sprint | **Yes** |
| `sulfur_element_term_record` on separate database track | **Yes** — not advanced |

---

## Selected draft count

**1** — verification scope is `de_core_mos2` only.

---

## Selected route_id list

```
de_core_mos2
```

---

## Current route count from routes.json

**126** routes (all `planned`; read from `routes.json` `routes` array length, 2026-05-27).

---

## Selected draft status

| route_id | content_file | route status | draft posture |
| --- | --- | --- | --- |
| `de_core_mos2` | `main/content/de/pages/terminology/molybdenum-disulfide.md` | `planned` | draft / non_public / indexable false / in_sitemap false |

---

## Human verification methodology

1. Reviewed Sprint **5N-G** named candidate intake artifacts and acceptance/rejection rules.
2. Applied human verification against each named candidate target for **authority role fit** — not bibliographic invention.
3. Read `de_core_mos2` draft content (read-only) — confirms `[SOURCE REQUIRED]` markers on lexical and document-form lines.
4. Classified Spektrum as primary German specialist lexicon candidate using verification taxonomy.
5. Bounded PubChem, NIST, and Chemie.de to supporting roles with explicit primary-authority rejection.
6. Confirmed no registry rows, claim approvals, content edits, or marker removals.
7. Ran corpus L1, guardrail, and L2 runtimes — all **PASS** before and after documentation.

**Verification boundary:** Human verification confirms **candidate role and policy fit**. Edition-level bibliographic confirmation (publisher imprint, edition year, page-level citation) remains for a **future proposal drafting sprint** with direct human access to the source — not invented in this sprint.

---

## What human verification means in this sprint

- Confirms whether **Spektrum Lexikon der Chemie — Molybdän(IV)-sulfid** is an appropriate **primary German specialist lexicon candidate** for MoS2 compound naming on a DE terminology route.
- Confirms **PubChem** supports **database identity context only** — not German lexical authority.
- Confirms **NIST Chemistry WebBook** supports **technical data context only** — not German lexical authority.
- Confirms **Chemie.de Lexikon** is **secondary German support only** — not primary authority.
- Records whether Spektrum may **later** move toward source registry **proposal drafting** — not registry execution.
- Documents blockers before registry edits, marker removal, claim approval, and publication.

---

## What human verification does not mean in this sprint

- **Not** source registration or `source_registry.json` modification.
- **Not** source approval or verified registry status.
- **Not** source-locking or removal of `[SOURCE REQUIRED]` markers.
- **Not** claim approval or claim registry activation.
- **Not** publication readiness or route publication.
- **Not** treating PubChem or NIST as substitutes for German lexical authority.
- **Not** treating Chemie.de as primary authority.
- **Not** treating CI passing as source approval.
- **Not** inventing DOI, ISBN, edition, author, publisher, date, or page numbers.

---

## Spektrum verification findings

| Field | Finding |
| --- | --- |
| Candidate target | Spektrum Lexikon der Chemie — Molybdän(IV)-sulfid |
| Human verification classification | **`primary_candidate_verified_for_later_proposal`** |
| Authority class | `chemistry_dictionary_authority` / `authoritative_dictionary` (DE) |
| Role | **Primary German specialist lexicon candidate** for MoS2 naming |
| Scope fit | Entry subject **Molybdän(IV)-sulfid** aligns with MoS2 German compound naming scope on `de_core_mos2` |
| Drift check | No lubricant market, procurement, medical, or trade-statistics authority implied |
| Approved | **No** — candidate only |
| Source-locked | **No** |
| Proposal drafting | **Conditional** — may proceed to proposal drafting sprint with human-verified bibliographic lines |

Spektrum is verified as the **correct primary candidate class** for German lexical authority on this draft. Full edition bibliographic verification and entry-level citation lines remain for proposal drafting — not registry execution.

---

## PubChem boundary findings

| Field | Finding |
| --- | --- |
| Candidate target | PubChem — Molybdenum disulfide / CID 14823 |
| Human verification classification | **`supporting_database_candidate_only`**, **`supports_identity_not_german_lexical_authority`**, **`rejected_as_primary_german_authority`** |
| Role | Database identity support for MoS2 chemical identity (CID-level reference) |
| German lexical authority | **No** — English/database context; cannot substitute for DE lexicon |
| Approved | **No** |
| Registry proposal role | Supporting reference only in future proposal — bounded |

---

## NIST boundary findings

| Field | Finding |
| --- | --- |
| Candidate target | NIST Chemistry WebBook — molybdenum disulphide |
| Human verification classification | **`supporting_technical_data_candidate_only`**, **`supports_technical_context_not_german_lexical_authority`**, **`rejected_as_primary_german_authority`** |
| Role | Technical data support (formula, CAS, thermochemistry context) |
| German lexical authority | **No** — technical reference; not DE specialist lexicon |
| Approved | **No** |
| Registry proposal role | Supporting technical context only in future proposal — bounded |

---

## Chemie.de boundary findings

| Field | Finding |
| --- | --- |
| Candidate target | Chemie.de Lexikon — Molybdän(IV)-sulfid |
| Human verification classification | **`secondary_german_support_only`**, **`not_primary_authority`**, **`rejected_as_primary_authority`** |
| Role | Secondary German-language support — cross-check only |
| Primary authority | **No** — must not replace Spektrum without separate verification elevating tier |
| Approved | **No** |
| Registry proposal role | Secondary DE support only if included in future proposal |

---

## Whether Spektrum can proceed later toward source registry proposal drafting

**Yes — conditional.** Spektrum is **`primary_candidate_verified_for_later_proposal`**. A **separate proposal drafting sprint** may be chartered when:

1. Human supplies **directly verified** bibliographic details from Spektrum (no AI invention).
2. Guardrail + corpus L1 runtimes **PASS**.
3. Claim boundaries for MoS2 lines documented — claim approval still separate.
4. `[SOURCE REQUIRED]` markers **remain** until audited linkage sprint after registry execution.

Proposal drafting is **not** registry execution. `source_registry.json` remains **unchanged** until a future execution sprint.

---

## Why PubChem and NIST remain supporting candidates only

| Reason | Detail |
| --- | --- |
| Language | PubChem and NIST are **English/international database** contexts — not DE specialist lexicon |
| Authority class | Database and technical data tiers — not `authoritative_dictionary` (DE) |
| DE page requirement | `de_core_mos2` requires German-verifiable lexical authority for document-language lines |
| Drift risk | Database entries can be stretched to industrial or application claims — blocked |
| Verification finding | Explicitly **`rejected_as_primary_german_authority`** |

---

## Why Chemie.de remains secondary support only

| Reason | Detail |
| --- | --- |
| Authority tier | Web lexicon — secondary cross-check, not specialist reference lexicon tier |
| Primary candidate | Spektrum verified as primary DE specialist lexicon candidate |
| Elevation risk | Treating Chemie.de as primary would bypass specialist lexicon discipline |
| Verification finding | **`not_primary_authority`**, **`rejected_as_primary_authority`** |

---

## Why no source entries were added

Human verification documents governance findings only. Adding registry rows would bypass verification → proposal → execution sequence.

---

## Why source_registry.json was not modified

Registry remains **inactive** with **0** verified entries. Verification is not registry execution.

---

## Why no claims were approved

Claim registries remain **inactive**. Human verification does not authorize terminology claim approval for MoS2 lines.

---

## Why terminology_claims.json was not modified

No claim boundary registration or approval occurred. Verification precedes claim linkage.

---

## Why no content pages were modified

Draft content is read-only reference. Human verification must not embed unverified citations or remove `[SOURCE REQUIRED]` markers.

---

## Why [SOURCE REQUIRED] markers remain

`de_core_mos2` draft retains markers on lexical and document-form lines. No audited source linkage exists. Verification does not equal source-locking.

---

## Why no routes were published

All **126** routes remain `planned`, non-indexable, out of sitemap and navigation.

---

## Publication blocker summary

| Blocker | Status |
| --- | --- |
| Human verification | **Complete** for Wave 1 — role boundaries documented |
| Spektrum primary candidate | **Verified for later proposal** — **not approved** |
| Source registry proposal drafting | **Eligible for next sprint** — conditional on human-verified bibliographic lines |
| Source registry execution | **Blocked** — separate future sprint |
| Source registry | **inactive** |
| Claim registries | **inactive** — 0 approved claims |
| `[SOURCE REQUIRED]` markers | **Unresolved** on `de_core_mos2` |
| Route publication lock | **LOCKED** |
| `production_can_safely_proceed` | **no** |
| Launch threshold | **500** pages — **126** routes |

---

## Recommended next sprint

**Sprint 5N-I prep — source registry proposal drafting for `de_core_mos2`** — author proposal document with human-verified Spektrum bibliographic lines; keep PubChem/NIST/Chemie.de in supporting-only roles; still **no** `source_registry.json` modification.

**Do not proceed to:** source registry execution, claim approval, content source-locking, `[SOURCE REQUIRED]` marker removal, Route Registration Wave 2 execution, or Draft Wave 2 without separate sprint charters.

**Parallel (unchanged):** `sulfur_element_term_record` scientific database candidate naming track — **not advanced**; Draft Wave 1 backlog reduction (**58** missing drafts).

---

## Sprint 5N-H deliverables

| File | Purpose |
| --- | --- |
| `NAMED_CANDIDATE_HUMAN_VERIFICATION_WAVE_1_REPORT.md` | This report |
| `NAMED_CANDIDATE_HUMAN_VERIFICATION_MATRIX_WAVE_1.md` | Verification matrix (4 candidate rows) |
| `SPEKTRUM_CANDIDATE_AUTHORITY_REVIEW_WAVE_1.md` | Spektrum authority review |
| `SUPPORTING_CANDIDATE_BOUNDARY_REVIEW_WAVE_1.md` | PubChem/NIST/Chemie.de boundaries |
| `NAMED_CANDIDATE_HUMAN_VERIFICATION_RISK_REVIEW_WAVE_1.md` | Risk review |
| `NAMED_CANDIDATE_HUMAN_VERIFICATION_NEXT_ACTIONS_WAVE_1.md` | Next sprint guidance |
| `NAMED_CANDIDATE_HUMAN_VERIFICATION_VALIDATION_REPORT.md` | Runtime validation |

**Not modified:** `source_registry.json`, `terminology_claims.json`, `routes.json`, content pages, registries, workflows, dependencies, root `README.md`.
