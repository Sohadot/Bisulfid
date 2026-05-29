# Source Registry Proposal Next Actions — Wave 1

**Sprint:** 5N-F  
**Date:** 2026-05-29

---

## Recommended next sprint

**Sprint 5N-G — Named source candidate intake wave 1** for `de_core_mos2`: human names and externally verifies DE specialist lexicon candidate class. Output: intake report with named authority — still **no** `source_registry.json` edits.

Parallel track for `sulfur_element_term_record`: **scientific database candidate naming** — remain blocked from proposal drafting until complete.

After MoS2 intake: **Sprint 5N-H — Source registry proposal drafting wave 1** (maximum **1** draft: `de_core_mos2`). Still **no** registry row writes unless execution sprint chartered separately.

Run before and after:

```bash
python scripts/source_claim_guardrail_runtime_l1.py
python scripts/corpus_validation_runtime_l1.py
```

---

## Whether next step should be named source candidate intake for de_core_mos2

**Yes — recommended as Sprint 5N-G.**

Readiness is **conditional** but **no named candidate exists**. Intake must:

1. Name specific DE specialist lexicon candidate (human-verified externally)
2. Confirm `authoritative_dictionary` category fit
3. Confirm MoS2 naming scope and lubricant-market exclusion
4. Map to `[SOURCE REQUIRED]` markers

---

## Whether next step should be database candidate naming for sulfur_element_term_record

**Yes — parallel track; blocks proposal drafting.**

Human must name government/scientific element-record database candidate before any proposal readiness upgrade. `sulfur_element_term_record` remains `do_not_prepare_proposal_yet`.

---

## Whether next step should be source registry proposal drafting

**After 5N-G intake only — for `de_core_mos2`.**

| Draft | Proposal drafting next |
| --- | --- |
| `de_core_mos2` | **Yes** — after named candidate intake (5N-G) |
| `sulfur_element_term_record` | **No** — until database candidate named |

Maximum **1** draft in first proposal drafting sprint. **No** marker removal.

---

## Whether next step should be source registry editing

**No.**

Registry execution requires: named candidate intake, proposal draft complete, human execution charter, guardrail **PASS**. Current verified registry rows for wave-1 drafts: **0**.

---

## Whether claim-boundary registration/reporting should happen before registry execution

**Yes — parallel, not blocking.**

Medium-risk drafts still need claim-boundary registration **report**. Do not activate claim registries before or during registry execution planning.

---

## Whether legacy draft hardening should happen before draft wave 2

**Schedule separately; do not block 5N-G or proposal drafting.**

Legacy pre-5J L1 warnings remain incremental debt.

---

## Whether draft wave 2 should still wait

**Yes.**

| Debt | Status |
| --- | --- |
| Named verified candidates | **0** |
| Proposal drafts complete | **0** |
| Registry rows for wave-1 drafts | **0** |
| Policy extension (`de_core_biogenic_lang`) | **Pending** |
| Publication-ready | **0** |

---

## Recommended order of operations

```
1. Sprint 5N-F (complete) — proposal readiness documentation
2. Sprint 5N-G — named source candidate intake (de_core_mos2)
3. Parallel: database candidate naming (sulfur_element_term_record)
4. Sprint 5N-H — source registry proposal drafting (de_core_mos2 max)
5. Human governance charter for registry execution
6. Sprint 5N-I — source registry execution (small batch, 1–3 rows)
7. Marker satisfaction audit (no auto-removal)
8. Parallel: claim-boundary registration report (medium-risk)
9. Draft wave 2 — only after governance debt milestones
```

---

## Criteria for moving from readiness to proposal draft

All must be true for `de_core_mos2`:

1. Readiness status `proposal_readiness_conditional` (5N-F)
2. Named source candidate intake complete (5N-G)
3. Human external verification confirmed
4. Authority-class alignment verified
5. Acceptance/rejection criteria clearance
6. Guardrail runtime **PASS**
7. Proposal drafting sprint chartered

**Not met for `sulfur_element_term_record`** until database candidate named.

---

## Criteria for moving from proposal draft to registry execution

All must be true:

1. Proposal draft complete with scoped marker linkage plan
2. Human execution charter approved
3. Full human-verified bibliographic details available (not fabricated in repo governance docs)
4. Guardrail + claim lock validators **PASS**
5. Maximum **1–3** rows per execution batch
6. **No** marker auto-removal in execution sprint

---

## How guardrail runtime must be used before and after future source sprints

| Event | Action |
| --- | --- |
| Before intake/proposal/execution doc merge | Run guardrail + corpus L1 |
| After governance doc updates | Re-run guardrail |
| Before proposal drafting merge | Guardrail **PASS** |
| Before any registry edit | Guardrail **PASS** + human execution charter |

---

## How this moves the corpus toward 500 governed pages without weakening authority

| Contribution | Effect |
| --- | --- |
| Readiness gate | Sequences MoS2 ahead without false registry progress |
| Blocked sulfur path | Prevents weak database-less proposal drafting |
| Separation of drafting vs execution | Protects trust root |
| Named-candidate requirement | Closes fabrication gap |
| No false progress | Markers and planned routes unchanged |

**500 governed pages** require verified sources and approved claims — readiness documentation alone does not increment governed publication count.

---

*Sprint 5N-F — Source Registry Proposal Next Actions Wave 1*
