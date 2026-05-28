# Source and Claim Automation Next Actions

**Sprint:** 5N-B  
**Date:** 2026-05-28

---

## Recommended next sprint

**Sprint 5N-C — Candidate source discovery wave 1** for the **5** Sprint 5N-A proposed drafts.

Run **both** runtimes before and after:

```bash
python scripts/corpus_validation_runtime_l1.py
python scripts/source_claim_guardrail_runtime_l1.py
```

---

## Whether 5N-C should be candidate source discovery

**Yes.** Identify **named candidate** sources per proposed draft for human review. Still **no** `source_registry.json` edits unless a separate execution sprint is chartered and guardrails pass.

---

## Whether 5N-D should be actual source registry entry proposals

**Not immediately.** After 5N-C discovery and human review, a dedicated **source registry execution** sprint (5N-D or 5O) may add **3–5** registry rows maximum. Guardrail + corpus L1 must **PASS** at execution time.

---

## Whether claim-boundary registration/reporting should happen before source registry edits

**Parallel, not blocking for low-risk proposals.**

- Medium-risk **20** drafts still need claim-boundary **registration report** (separate sprint)
- Low-risk **5** proposal drafts may proceed to discovery without waiting for all **20** boundary reports
- **No** claim registry activation before human charter in any case

---

## Whether legacy draft hardening should happen before draft wave 2

**Schedule separately; do not block 5N-C.**

**18** legacy pre-5J draft warnings remain in corpus L1. Harden incrementally; do not use as gate for source discovery on the **5** proposed drafts.

---

## Why draft wave 2 should still wait

| Debt item | Status |
| --- | --- |
| Source proposals | **5** of **12** cohort-A |
| Candidate discovery | **0** completed |
| Registry verified rows for wave-1 drafts | **0** |
| Medium-risk claim boundaries | **20** prep only |
| Guardrail runtime | **Established (5N-B)** |
| Publication-ready pages | **0** |

Draft wave 2 adds pages without reducing source/claim governance debt.

---

## How to move from proposal to candidate source discovery

1. Guardrail runtime **PASS**
2. For each of **5** proposed drafts, name candidate source (publisher/edition/database) in discovery report
3. Map candidate to evidence matrix row and draft markers
4. Human review rejects weak candidates (see rejection criteria in `SOURCE_REGISTRATION_NEXT_ACTIONS_WAVE_1.md`)
5. **No** registry row until execution sprint chartered

---

## How to move from candidate source discovery to source registry entry

1. Discovery report complete; guardrails **PASS**
2. SOURCE_POLICY category confirmed or extended
3. Marker-to-row mapping manifest documented
4. Human governance charter approves registry edit sprint
5. Add **3–5** rows maximum; registry status may remain **inactive** until broader activation review
6. **Do not** remove `[SOURCE REQUIRED]` markers without marker audit

---

## How to reject weak sources

Reject candidates that:

- Lack named publisher, edition, or database authority
- Are AI-generated, uncited, or unstable
- Primary purpose is market, procurement, safety, medical, or trade advice
- Cannot map to approved SOURCE_POLICY category
- Would partially satisfy markers while implying full source-lock

Guardrail validators re-run after any governance document update.

---

## How to keep human review in the loop

| Transition | Human gate |
| --- | --- |
| Proposal → discovery | Review candidate list and evidence mapping |
| Discovery → registry row | Charter + source policy alignment |
| Registry row → marker satisfaction | Marker audit (no auto-removal) |
| Claim boundary → claim activation | Registry activation charter |
| Any → publication | Quality Gate + corpus L1 + guardrail PASS |

Automation **blocks accidents**; humans **authorize transitions**.

---

## How to preserve 500-page launch threshold integrity

- Run guardrail runtime on every source/claim governance PR
- Keep registries **inactive** until explicit activation sprint
- Maintain **0** approved claims until claim charter
- Keep all routes `planned` / non-indexable until launch authorization
- Count **governed** pages with verified sources — not draft count alone

---

*Sprint 5N-B — Source and Claim Automation Next Actions*
