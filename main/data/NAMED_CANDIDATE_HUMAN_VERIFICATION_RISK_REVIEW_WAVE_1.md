# Named Candidate Human Verification Risk Review — Wave 1

**Sprint:** 5N-H  
**Scope:** `de_core_mos2` human verification risks  
**Date:** 2026-05-27

---

## Risk of approving a candidate too early

| Risk | Consequence | Mitigation in 5N-H |
| --- | --- | --- |
| Registry row before verification | False authority signal in inactive registry | **0** registry rows added |
| Skipping proposal drafting | Bibliographic details invented or omitted | Verification only — proposal drafting is next sprint |
| Conflating verification with approval | Contributors treat candidates as source-locked | All candidates documented **unapproved** |
| Corpus-wide precedent | Other drafts inherit loose authority discipline | Role boundaries explicit per candidate |

Human verification records **role fit** — not approval. Approval requires registry execution, claim gates, and content audit sprints.

---

## Risk of treating Spektrum as source-locked before registry proposal

| Risk | Consequence | Mitigation |
| --- | --- | --- |
| `[SOURCE REQUIRED]` removed prematurely | Unverified lines published | Markers **remain** on `de_core_mos2` |
| Draft edited with unverified citation | Content drift before registry | Content **not modified** |
| Proposal skipped | Registry execution without documented proposal | Proposal drafting sprint required next |
| False merge confidence | CI PASS interpreted as source approval | Documents state CI ≠ source approval |

Spektrum is **`primary_candidate_verified_for_later_proposal`** — verified role, not source-locked.

---

## Risk of treating PubChem or NIST as German lexical authority

| Risk | Consequence | Mitigation |
| --- | --- | --- |
| EN database cited for DE lexical lines | Authority class violation on DE route | **`rejected_as_primary_german_authority`** |
| CID used as naming authority | Database identity conflated with lexicon | Supporting database role bounded |
| Thermochemistry stretched to operational claims | Safety/production drift | Technical data scope bounded |
| MoS2 lubricant market framing | Industrial drift on terminology page | Rejection rules applied |

PubChem and NIST remain **supporting-only** with explicit primary-authority rejection.

---

## Risk of treating Chemie.de as primary authority

| Risk | Consequence | Mitigation |
| --- | --- | --- |
| Web lexicon replaces specialist reference | Thin authority on strict-registry page | **`not_primary_authority`** |
| Secondary source elevated without verification | Spektrum bypassed | Primary candidate remains Spektrum |
| Inconsistent DE naming across corpus | Cross-page authority drift | Secondary-only classification documented |

Chemie.de is **secondary German support only** — not primary.

---

## Risk of removing [SOURCE REQUIRED] markers too early

| Risk | Consequence | Mitigation |
| --- | --- | --- |
| Verification treated as linkage | Unresolved factual lines appear resolved | Markers **remain** |
| No audited source IDs | Claims without registry backing | **0** registry entries |
| Publication path opened | Non-public draft appears ready | Route still `planned`, draft `non_public` |

Marker removal requires: approved registry entry → audited linkage → content audit sprint.

---

## Risk of approving claims before claim boundary registration

| Risk | Consequence | Mitigation |
| --- | --- | --- |
| Terminology claims activated early | Unverified MoS2 statements governed as approved | Claim registries **inactive** |
| Source verification conflated with claim approval | Lexical lines treated as claim-backed | **0** approved claims |
| Cross-registry drift | Industry or market claims enter terminology registry | Claim approval **not performed** |

Claim boundary registration may proceed in parallel with source track — claim **approval** remains blocked.

---

## Risk of publishing before source and claim gates clear

| Risk | Consequence | Mitigation |
| --- | --- | --- |
| Route publication before source lock | Public thin-authority page | All routes **`planned`**, locks **LOCKED** |
| Indexation enabled early | Search exposure of draft content | **indexable: false** on all routes |
| Launch threshold bypass | **126** pages treated as launch-ready | **500-page** threshold documented |
| `production_can_safely_proceed` ignored | Production wave triggered | Planner reports **no** |

Publication requires: launch threshold, source lock, claim approval, owner sign-off — none satisfied.

---

## Risk of using CI passing as source approval

| Risk | Consequence | Mitigation |
| --- | --- | --- |
| Corpus Governance CI PASS misread | Merge allowed ≠ sources approved | Documents state CI validates discipline only |
| Guardrail PASS misread | Lock validators pass ≠ registry activation | Registry **inactive** |
| Automated merge without human source review | Authority decisions delegated to CI | Human verification sprint separate from CI |

CI blocks **bad merges** — it does not **approve sources**.

---

## Risk of source registry editing without separate sprint

| Risk | Consequence | Mitigation |
| --- | --- | --- |
| Verification sprint edits registry | Bypasses proposal → execution sequence | `source_registry.json` **not modified** |
| Undocumented registry rows | Audit failure | **0** entries added |
| Guardrail bypass | Inactive registry discipline broken | Guardrail runtime **PASS** pre/post sprint |

Registry execution requires **separate sprint charter** after proposal drafting.

---

## Why human verification does not approve execution

| Verification completes | Execution still requires |
| --- | --- |
| Role-fit confirmation | Proposal document with human-verified bibliographic lines |
| Primary/supporting boundaries | Separate registry execution sprint charter |
| Risk documentation | Human sign-off on registry diff |
| Runtime PASS | Content audit and marker resolution sprints |

Sprint **5N-H** output is **governance documentation** — not registry execution authorization.

---

## Related documents

- `NAMED_CANDIDATE_HUMAN_VERIFICATION_WAVE_1_REPORT.md`
- `NAMED_CANDIDATE_HUMAN_VERIFICATION_NEXT_ACTIONS_WAVE_1.md`
- `GITHUB_ACTIONS_GOVERNANCE_WORKFLOW_REPORT.md`
- `SOURCE_CLAIM_AUTOMATION_GUARDRAIL_REPORT.md`
