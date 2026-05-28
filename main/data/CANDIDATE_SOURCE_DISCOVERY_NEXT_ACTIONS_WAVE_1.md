# Candidate Source Discovery Next Actions — Wave 1

**Sprint:** 5N-C  
**Date:** 2026-05-28

---

## Recommended next sprint

**Sprint 5N-D — Human candidate source review wave 1** for the **5** discovery rows: humans name and evaluate specific candidates against rejection rules; still **no** registry edits unless a separate **registry execution** sprint is chartered.

Run before and after:

```bash
python scripts/source_claim_guardrail_runtime_l1.py
python scripts/corpus_validation_runtime_l1.py
```

---

## Whether next step should be human candidate source review

**Yes — immediately.**

Discovery produced **families and search targets**. Humans must:

1. Name specific dictionary/database/edition candidates (without auto-registering)
2. Map each to draft markers and evidence matrix rows
3. Apply rejection rules in `CANDIDATE_SOURCE_REJECTION_RULES_WAVE_1.md`
4. Record accept/reject/defer decisions in a review report (future sprint)

---

## Whether next step should be actual source registry entry proposal

**Not until after 5N-D human review.**

Registry execution requires:

- Named verified candidates accepted in human review
- Marker-to-row mapping manifest
- SOURCE_POLICY alignment (and policy extension if needed for biogenic tier)
- Guardrail + corpus L1 **PASS**
- Dedicated execution sprint charter

Batch size: **3–5** rows maximum for first execution.

---

## Whether claim-boundary registration/reporting should happen first

**Parallel, not blocking for this 5-draft cohort.**

- **20** medium-risk drafts still need claim-boundary registration **report** (separate sprint)
- Low-risk discovery cohort may proceed without waiting for all **20** reports
- **No** claim registry activation in either track

---

## Whether legacy draft hardening should happen before draft wave 2

**Schedule separately; do not block 5N-D.**

**18** legacy pre-5J L1 warnings remain. Harden incrementally; do not gate human review of the **5** discovery drafts.

---

## Why draft wave 2 should still wait

| Debt item | Status |
| --- | --- |
| Human-named candidates | **0** verified |
| Registry rows for wave-1 drafts | **0** |
| Medium-risk claim boundaries | **20** prep only |
| Discovery complete | **5** family/target rows only |
| Publication-ready pages | **0** |

Adding drafts compounds unmapped source debt.

---

## Criteria for moving a candidate source from discovery to registry proposal

All must be true:

1. Discovery matrix row exists (Sprint **5N-C**)
2. Human review names candidate with publisher/database/dictionary class
3. Candidate passes all rejection rules
4. Candidate maps to specific draft markers (manifest documented)
5. SOURCE_POLICY category confirmed or extension merged
6. Guardrail runtime **PASS**
7. Execution sprint chartered
8. Route remains `planned` / non-indexable after any registry row

---

## Criteria for rejecting candidates

See `CANDIDATE_SOURCE_REJECTION_RULES_WAVE_1.md`. Reject if weak publisher, AI/uncited, market/safety/medical/procurement primary purpose, wrong authority tier, partial marker satisfaction, or multilingual overreach.

---

## Criteria for human review

Human review must confirm:

- Named source identity (publisher/institution/database class — not fabricated bibliographic detail)
- Category fit under SOURCE_POLICY
- Scope limits (`use_for` / `do_not_use_for` equivalent reasoning)
- Marker alignment plan
- No claim approval or publication implication
- Explicit accept / reject / defer with rationale

---

## How guardrail runtime must be used before and after any future source sprint

| When | Action |
| --- | --- |
| Before discovery/review/execution docs merge | Run guardrail + corpus L1 |
| After any governance doc update | Re-run guardrail |
| Before registry edit sprint | Guardrail **PASS** required |
| Before claim activation | Claim lock validators **PASS** |
| Before publication | Both runtimes **PASS** + human launch charter |

Warnings are non-blocking unless elevated by human charter.

---

## How this moves the corpus toward 500 governed pages without weakening authority

| Contribution | Effect |
| --- | --- |
| Repeatable discovery → review → registry pipeline | Reduces ad-hoc source debt |
| Rejection rules | Prevents weak-source registry pollution |
| Authority requirements | Preserves formal/dictionary/teaching boundaries |
| No false progress | Markers and planned routes unchanged |

**500 governed pages** require verified sources and approved boundaries — discovery targets alone do not count as governed publication readiness.

---

*Sprint 5N-C — Candidate Source Discovery Next Actions Wave 1*
