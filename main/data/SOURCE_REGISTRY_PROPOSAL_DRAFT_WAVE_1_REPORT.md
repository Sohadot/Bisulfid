# Source Registry Proposal Draft Wave 1 — Report

**Sprint:** 5N-I  
**Date:** 2026-05-29  
**Branch:** `claude/sprint-5n-i-source-registry-proposal-drafting-wave-1`

---

## Why this sprint exists

Sprint **5N-H** classified **Spektrum Lexikon der Chemie — Molybdän(IV)-sulfid** as **`primary_candidate_verified_for_later_proposal`** for `de_core_mos2`. Human verification confirmed authority role fit — not registry approval. Sprint **5N-I** performs **source registry proposal drafting** — documenting what a future registry entry **would** contain, which boundaries it may support, and what remains blocked before execution — without modifying `source_registry.json`, approving sources, or removing `[SOURCE REQUIRED]` markers.

---

## Why proposal drafting comes after human verification

| Stage | Sprint | Question answered |
| --- | --- | --- |
| Named candidate intake | 5N-G | Has a human named specific candidate targets? |
| Human verification | 5N-H | Do named targets fit authority roles and policy boundaries? |
| **Proposal drafting** | **5N-I** | What would a structured registry proposal contain for review? |
| Registry execution (future) | separate sprint | May `source_registry.json` be modified? |

Verification records role fit; proposal drafting records **structured draft intent** — still not execution or approval.

---

## Why proposal drafting still comes before source_registry edits

| Reason | Detail |
| --- | --- |
| Registry inactive | `source_registry.json` status **inactive** |
| Proposal ≠ execution | Draft document is not a registry row |
| Proposal ≠ approval | Proposed entry is not verified-in-registry |
| Guardrail gate | Sprint **5N-B** runtime must **PASS** |
| Marker discipline | `[SOURCE REQUIRED]` remains until audited linkage after execution |
| No invented bibliography | DOI, ISBN, edition, author, publisher, date, page numbers forbidden without direct human verification at execution |

---

## Relationship to Sprint 5N-H

Sprint **5N-H** verified Spektrum as primary German specialist lexicon candidate and bounded PubChem, NIST, and Chemie.de supporting roles. Sprint **5N-I** executes the proposal drafting step 5N-H deferred: author structured proposal documents for future registry review.

**Post-drafting posture:** Spektrum classified **`proposal_draft_primary_candidate`**, **`proposal_draft_allowed_for_review`**, **`registry_execution_not_allowed_now`**, **`source_approval_not_allowed_now`**. Supporting candidates remain **supporting-only**. All candidates remain **unapproved**.

---

## Relationship to Sprint 5N-G

Sprint **5N-G** documented named candidate intake and acceptance/rejection rules. Sprint **5N-I** builds on that intake chain without re-opening intake classification — proposal drafting assumes named targets and human verification are complete for `de_core_mos2`.

---

## Relationship to Sprint 5P-A GitHub Actions governance

Sprint **5P-A** established **Corpus Governance CI** on `main` with branch protection requiring **Corpus governance validation**. Sprint **5N-I** is documentation-only; governance CI must **PASS** before merge. CI passing does **not** constitute source approval, registry execution, source-locking, or publication readiness.

---

## Relationship to 500-page sovereign launch threshold

| Metric | Value |
| --- | ---: |
| Launch threshold | **500** governed pages |
| Current route count (`routes.json`) | **126** |
| Proposal drafting target | **1** draft (`de_core_mos2`) |
| Proposed registry rows added | **0** |
| Publication-ready pages | **0** |

Proposal drafting advances **source governance sequencing** without incrementing launch-eligible page count.

---

## Files reviewed

- `main/data/NAMED_CANDIDATE_HUMAN_VERIFICATION_WAVE_1_REPORT.md`
- `main/data/NAMED_CANDIDATE_HUMAN_VERIFICATION_MATRIX_WAVE_1.md`
- `main/data/SPEKTRUM_CANDIDATE_AUTHORITY_REVIEW_WAVE_1.md`
- `main/data/SUPPORTING_CANDIDATE_BOUNDARY_REVIEW_WAVE_1.md`
- `main/data/NAMED_CANDIDATE_HUMAN_VERIFICATION_RISK_REVIEW_WAVE_1.md`
- `main/data/NAMED_CANDIDATE_HUMAN_VERIFICATION_NEXT_ACTIONS_WAVE_1.md`
- `main/data/NAMED_CANDIDATE_HUMAN_VERIFICATION_VALIDATION_REPORT.md`
- `main/data/NAMED_SOURCE_CANDIDATE_INTAKE_WAVE_1_REPORT.md`
- `main/data/SOURCE_REGISTRY_PROPOSAL_READINESS_WAVE_1_REPORT.md`
- `main/data/SOURCE_REGISTRY_PROPOSAL_READINESS_MATRIX_WAVE_1.md`
- `main/data/SOURCE_REGISTRY_PROPOSAL_DRAFTING_CRITERIA_WAVE_1.md`
- `doctrine/SOURCE_POLICY.md`
- `main/data/GITHUB_ACTIONS_GOVERNANCE_WORKFLOW_REPORT.md`
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
| Branch based on main after Sprint 5N-H | **Yes** |
| L2 production runtime | **PASS** |
| Corpus L1 runtime | **PASS** |
| Guardrail runtime | **PASS** |
| Planner: 126 routes, 68 draft-backed, 58 missing, all locks **LOCKED**, `production_can_safely_proceed: no` | **Yes** |
| `de_core_mos2` exists in routes + content | **Yes** |
| draft / non_public / non-indexable / not in sitemap | **Yes** |
| `[SOURCE REQUIRED]` markers present | **Yes** |
| `source_registry.json` unchanged pre-sprint | **Yes** |
| `terminology_claims.json` unchanged pre-sprint | **Yes** |
| `sulfur_element_term_record` on separate database track | **Yes** — not advanced |

---

## Selected draft count

**1** — proposal scope is `de_core_mos2` only.

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

## Proposal drafting methodology

1. Reviewed Sprint **5N-G** through **5N-H** artifacts and `SOURCE_POLICY.md` registry format requirements.
2. Drafted structured proposal for Spektrum as primary German lexical authority candidate — **without** inventing bibliographic fields.
3. Documented supporting-only boundaries for PubChem, NIST, and Chemie.de in proposal context.
4. Read `de_core_mos2` draft (read-only) — mapped proposal scope to lexical and document-form marker lines only.
5. Documented execution blockers requiring separate future sprint.
6. Confirmed no registry rows, claim approvals, content edits, or marker removals.
7. Ran corpus L1, guardrail, and L2 runtimes — all **PASS** before and after documentation.

**Proposal boundary:** This sprint defines **proposed registry role, authority class, route relationship, and claim boundary limits**. Human-verified bibliographic fields (`author_or_organization`, `publisher`, `publication_date`, `url`/`doi`) remain **explicitly unverified placeholders** until execution sprint with direct human access — not invented here.

---

## What source registry proposal drafting means in this sprint

- Documents what a **future** Spektrum registry entry **would** look like in structure and governance scope.
- Defines which `de_core_mos2` draft lines the primary proposal **may support later** — not now.
- Defines what Spektrum **may not** support (market, safety, procurement, lubricant drift).
- Keeps PubChem/NIST/Chemie.de in supporting-only proposal roles.
- Records execution blockers before `source_registry.json` may be edited.

---

## What source registry proposal drafting does not mean in this sprint

- **Not** source registry execution or `source_registry.json` modification.
- **Not** source approval or verified registry status.
- **Not** source-locking or removal of `[SOURCE REQUIRED]` markers.
- **Not** claim approval or claim registry activation.
- **Not** publication readiness or route publication.
- **Not** treating proposal drafting as registry execution.
- **Not** inventing DOI, ISBN, edition, author, publisher, date, or page numbers.

---

## Spektrum proposal findings

| Field | Finding |
| --- | --- |
| Candidate target | Spektrum Lexikon der Chemie — Molybdän(IV)-sulfid |
| Proposal classification | **`proposal_draft_primary_candidate`**, **`proposal_draft_allowed_for_review`**, **`registry_execution_not_allowed_now`**, **`source_approval_not_allowed_now`** |
| Proposed registry role | Primary German specialist lexicon authority for MoS2 compound naming on `de_core_mos2` |
| Proposed category | `authoritative_dictionary` (DE) |
| Proposed source label (draft) | `SRC-SPEKTRUM-MOS2-DE` — **proposed ID only; not in registry** |
| Approved | **No** — proposal draft only |
| Execution allowed | **No** |

See `SPEKTRUM_SOURCE_REGISTRY_PROPOSAL_DRAFT_WAVE_1.md` for full proposal structure.

---

## PubChem boundary findings

| Field | Finding |
| --- | --- |
| Proposal classification | **`supporting_database_boundary_only`**, **`not_primary_german_authority`**, **`not_registry_primary_for_de_core_mos2_now`** |
| Proposed registry role | Optional supporting database identity reference — if included at execution |
| Primary authority | **No** — not registry primary for DE lexical lines |

---

## NIST boundary findings

| Field | Finding |
| --- | --- |
| Proposal classification | **`supporting_technical_boundary_only`**, **`not_primary_german_authority`**, **`not_registry_primary_for_de_core_mos2_now`** |
| Proposed registry role | Optional supporting technical data reference — if included at execution |
| Primary authority | **No** — not registry primary for DE lexical lines |

---

## Chemie.de boundary findings

| Field | Finding |
| --- | --- |
| Proposal classification | **`secondary_german_support_boundary_only`**, **`not_primary_authority`**, **`not_registry_primary_for_de_core_mos2_now`** |
| Proposed registry role | Optional secondary DE cross-check — if included at execution |
| Primary authority | **No** — Spektrum remains sole primary proposal |

---

## Why Spektrum can proceed as a proposal draft candidate

| Factor | Detail |
| --- | --- |
| Human verification | **`primary_candidate_verified_for_later_proposal`** (5N-H) |
| Authority class | `chemistry_dictionary_authority` / `authoritative_dictionary` (DE) |
| Policy category | Fits `SOURCE_POLICY.md` approved category |
| Scope | MoS2 German compound naming on `de_core_mos2` only |
| Guardrails | Runtime **PASS**; rejection rules not triggered |

Spektrum is the **only** primary proposal draft candidate for this wave.

---

## Why PubChem and NIST remain supporting candidates only

Database and technical data tiers cannot substitute for DE specialist lexicon authority on a German terminology route. Proposal draft documents optional supporting rows only — bounded to identity (PubChem) and technical context (NIST).

---

## Why Chemie.de remains secondary support only

Web lexicon secondary tier must not replace Spektrum as primary German authority in the proposal draft. Optional secondary cross-check role only.

---

## Why no source entries were added

Proposal drafting documents governance intent only. Adding registry rows would bypass proposal → review → execution sequence.

---

## Why source_registry.json was not modified

Registry remains **inactive** with **0** new verified entries. Proposal drafting is not registry execution.

---

## Why no claims were approved

Claim registries remain **inactive**. Proposal drafting does not authorize terminology claim approval.

---

## Why terminology_claims.json was not modified

No claim boundary registration or approval occurred. Proposal precedes claim linkage.

---

## Why no content pages were modified

Draft content is read-only reference. Proposal drafting must not embed citations or remove `[SOURCE REQUIRED]` markers.

---

## Why [SOURCE REQUIRED] markers remain

`de_core_mos2` draft retains markers on lexical and document-form lines. No audited source linkage exists. Proposal drafting does not equal source-locking.

---

## Why no routes were published

All **126** routes remain `planned`, non-indexable, out of sitemap and navigation.

---

## Execution blocker summary

| Blocker | Status |
| --- | --- |
| Proposal draft | **Complete** — Spektrum primary; supporting bounded |
| Human bibliographic verification | **Required** at execution — not in this sprint |
| Source registry execution | **Blocked** — separate future sprint |
| Source approval | **Blocked** |
| Claim approval | **Blocked** — inactive registries |
| Content source-locking | **Blocked** |
| `[SOURCE REQUIRED]` markers | **Unresolved** |
| Route publication lock | **LOCKED** |
| `production_can_safely_proceed` | **no** |
| Launch threshold | **500** pages — **126** routes |

See `SOURCE_REGISTRY_PROPOSAL_EXECUTION_BLOCKERS_WAVE_1.md` for full blocker set.

---

## Recommended next sprint

**Sprint 5N-J prep — source registry execution review for `de_core_mos2`** — human review of proposal draft, human-verified bibliographic fields supplied, guardrail **PASS**, separate execution charter — still requires explicit authorization before `source_registry.json` edit.

**Do not proceed to:** registry execution without review sprint; claim approval; content source-locking; marker removal; Route Registration Wave 2 execution; or Draft Wave 2 without separate charters.

**Parallel (unchanged):** `sulfur_element_term_record` scientific database candidate naming track — **not advanced**; Draft Wave 1 backlog (**58** missing drafts).

---

## Sprint 5N-I deliverables

| File | Purpose |
| --- | --- |
| `SOURCE_REGISTRY_PROPOSAL_DRAFT_WAVE_1_REPORT.md` | This report |
| `SOURCE_REGISTRY_PROPOSAL_DRAFT_MATRIX_WAVE_1.md` | Proposal matrix (4 rows) |
| `SPEKTRUM_SOURCE_REGISTRY_PROPOSAL_DRAFT_WAVE_1.md` | Spektrum primary proposal draft |
| `SUPPORTING_SOURCE_BOUNDARY_PROPOSAL_DRAFT_WAVE_1.md` | Supporting candidate boundaries |
| `SOURCE_REGISTRY_PROPOSAL_EXECUTION_BLOCKERS_WAVE_1.md` | Execution blockers |
| `SOURCE_REGISTRY_PROPOSAL_NEXT_ACTIONS_WAVE_1.md` | Next sprint guidance |
| `SOURCE_REGISTRY_PROPOSAL_DRAFT_VALIDATION_REPORT.md` | Runtime validation |

**Not modified:** `source_registry.json`, `terminology_claims.json`, `routes.json`, content pages, registries, workflows, dependencies, root `README.md`.
