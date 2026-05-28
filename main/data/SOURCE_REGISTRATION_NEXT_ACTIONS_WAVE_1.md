# Source Registration Next Actions — Wave 1

**Sprint:** 5N-A  
**Date:** 2026-05-27

---

## Recommended next sprint

Run **two parallel governance sprints**:

| Sprint | Focus | Scope |
| --- | --- | --- |
| **5N-B** | Claim boundary registration report | **20** medium-risk drafts from Sprint 5M prep |
| **5N-C** | Candidate source discovery wave 1 | **5** drafts from this proposal wave |

Neither sprint should publish routes or approve claims without explicit charter.

---

## Whether to create actual source registry entries next

**No — not immediately.**

Create registry entries only after:

1. **5N-C** identifies concrete candidate sources per draft
2. Human review confirms source class, authority tier, and marker alignment
3. SOURCE_POLICY gaps are resolved or explicitly extended (especially DE lexical and biogenic tiers)
4. A dedicated **source registration execution** sprint is chartered

Proposals define **what** to register; discovery + review define **which row** to write.

---

## Whether to run a candidate source discovery sprint first

**Yes — recommended as Sprint 5N-C.**

For each of the **5** proposed drafts:

- Identify **named candidate** sources (publisher, database, dictionary edition) without adding registry rows
- Map candidates to draft markers and evidence matrix rows
- Flag weak or unacceptable candidates for rejection
- Produce a discovery report for human charter review

Discovery precedes registry execution.

---

## Whether to run claim-boundary registration for medium-risk drafts first

**Parallel, not blocking.**

- **5N-B** should proceed **in parallel** with **5N-C**
- Medium-risk claim-boundary work does not block low-risk source discovery for this **5**-draft subset
- Do **not** approve claims in either sprint
- Claim-boundary output informs future terminology_claims.json activation — not this wave's proposals

---

## Whether to harden legacy pre-5J drafts first

**No — not as a prerequisite for this wave.**

L1 documents **18** legacy pre-5J draft warnings. Hardening remains important corpus debt but should not delay:

- Source discovery for the **5** proposed drafts
- Claim-boundary report for **20** medium-risk drafts

Schedule legacy hardening as a **separate** sprint after 5N-B/5N-C or as incremental hygiene — not as a gate for proposal execution.

---

## Recommended order of operations

```
1. Sprint 5N-A (complete) — source registration proposals for 5 drafts
2. Parallel:
   a. Sprint 5N-B — claim boundary registration report (20 medium-risk)
   b. Sprint 5N-C — candidate source discovery (5 proposed drafts)
3. SOURCE_POLICY extension review (DE lexical, biogenic tier) if flagged
4. Human governance review of discovery candidates
5. Sprint 5N-D (or 5O) — source registry execution wave 1 (small batch, 3–5 rows max)
6. Marker satisfaction review (still no auto-removal without audit)
7. Terminology claim boundary registration (inactive registry → structured candidates only)
8. Deferred cohort-A drafts (7 remaining) — next proposal or discovery wave
9. Draft wave 2 — only after governance debt reduction milestones met
```

---

## Recommended batch size for future source registration

| Phase | Batch size | Rationale |
| --- | --- | --- |
| First registry execution | **3–5** rows | Human review capacity; accident prevention |
| Subsequent waves | **5–8** rows | After first execution retrospective |
| Maximum without retrospective | **10** | Avoid bulk false-verification |

Start with the **lowest-gap** draft (`de_core_mos2` — `proposal_ready_for_future_registration`) only after discovery confirms a named candidate.

---

## Criteria for moving from proposal to source registry entry

All must be true:

1. Proposal row exists in `SOURCE_REGISTRATION_PROPOSAL_MATRIX_WAVE_1.md`
2. Discovery sprint names at least one **acceptable** candidate per required evidence type
3. Candidate maps to specific draft markers (manifest documented)
4. SOURCE_POLICY category confirmed or policy extension merged
5. Human governance charter approves registry edit sprint
6. Source class passes weak-source rejection criteria
7. No safety, market, medical, procurement, or trade claim drift identified
8. Claim posture remains `terminology_claim_candidate_later` or lower — no approval
9. Route remains `planned` / non-indexable after registry row (registration ≠ publication)

---

## Criteria for rejecting weak source candidates

Reject candidates that:

- Lack named publisher, edition, or database authority
- Are AI-generated, uncited, or user-editable without stable governance
- Primary purpose is market research, procurement, pricing, or investment
- Primary purpose is safety handling, medical, or toxicology advice
- Conflate multilingual equivalents without scoped term-pair evidence
- Cannot be assigned an approved SOURCE_POLICY category
- Would satisfy markers only partially while implying full source-lock
- Conflict with doctrine or existing seeded candidate rows without review

---

## Criteria for allowing source mapping to proceed to source registration

| Criterion | Required |
| --- | --- |
| Sprint 5M mapping row exists | Yes |
| Sprint 5N-A proposal row exists | Yes |
| Discovery candidates human-reviewed | Yes |
| Policy gap resolved or extension merged | Yes (if flagged) |
| Claim boundary clear for draft risk tier | Yes |
| No blocked/reframe-required status | Yes |
| Registry execution sprint chartered | Yes |
| L1 runtime PASS at execution time | Yes |

Mapping alone is **insufficient**. Proposal + discovery + policy alignment + human charter required.

---

## How this moves the corpus toward 500 governed pages

| Contribution | Effect |
| --- | --- |
| Governance pipeline | Defines repeatable path: classify → map → propose → discover → register |
| Reduces source debt | **5** drafts move from "mapped" to "proposal-ready" |
| Prevents false progress | No phantom source-lock or publication signals |
| Enables batch registration | Future execution sprints can add rows with audit trail |
| Informs claim work | 5N-B parallel track clears medium-risk boundary debt |

**500-page threshold** requires governed pages with verified sources, approved claim boundaries, and publication gates — not draft count alone. This sprint advances **governance readiness** for **5** of **68** draft-backed routes without increasing published surface.

---

## Why draft wave 2 should still wait unless governance debt is reduced

| Debt item | Status |
| --- | --- |
| Cohort-A mapped but not proposed | **7** drafts remain |
| Medium-risk claim boundaries | **20** drafts await 5N-B |
| Registry entries | **0** verified rows for wave-1 drafts |
| Legacy pre-5J warnings | **18** drafts |
| Routes without drafts | **58** |
| Publication-ready pages | **0** |

Adding **50+** new drafts (wave 2) before completing proposal → discovery → registration for cohort-A would:

- Compound unmapped source debt
- Increase L1 warning surface
- Create false impression of corpus maturity
- Make 500-page threshold harder to audit

**Draft wave 2** should wait until:

- 5N-B claim-boundary report complete
- 5N-C discovery complete for first **5** proposals
- First registry execution retrospective complete (even if **0** rows added in retrospective, the process must be validated)
- Sprint 5M deferred **7** drafts have proposals or explicit defer rationale updated

---

*Sprint 5N-A — Source Registration Next Actions Wave 1*
