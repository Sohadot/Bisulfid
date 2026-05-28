# Human Source Review Next Actions — Wave 1

**Sprint:** 5N-D  
**Date:** 2026-05-28

---

## Recommended next sprint

**Sprint 5N-E — External source verification wave 1** (1–2 drafts: `de_core_mos2`, `sulfur_element_term_record`) where humans **name and externally verify** specific candidates. Output: verification report with named authorities — still **no** `source_registry.json` edits unless execution sprint chartered.

Alternative parallel track: **claim-boundary registration report** for **20** medium-risk drafts (unchanged from prior recommendations).

Run before and after:

```bash
python scripts/source_claim_guardrail_runtime_l1.py
python scripts/corpus_validation_runtime_l1.py
```

---

## Whether next step should be source registry proposal drafting

**After 5N-E verification only.**

Registry **proposal drafting** (not execution) may begin for `de_core_mos2` first if human verification names acceptable DE specialist lexicon candidate. Maximum **1–3** drafts per proposal sprint.

**No** registry row writes in proposal drafting sprint.

---

## Whether next step should be claim-boundary registration/reporting

**Parallel, not blocking** for the **5** low-risk reviewed drafts.

Medium-risk **20** drafts still need claim-boundary registration **report**. Do not activate claim registries.

---

## Whether next step should be external source verification

**Yes — recommended as Sprint 5N-E.**

Human review (5N-D) documented **classes and gaps**. External verification must:

1. Name specific candidate (publisher/database/dictionary class)
2. Confirm category under SOURCE_POLICY
3. Map to markers
4. Record accept/reject with evidence of verification (outside governance docs — not invented bibliographic lines in repo)

---

## Whether legacy draft hardening should happen before draft wave 2

**Schedule separately; do not block 5N-E.**

**18** legacy pre-5J L1 warnings remain incremental debt.

---

## Whether draft wave 2 should still wait

**Yes.**

| Debt | Status |
| --- | --- |
| Human verification | **0** named verified candidates |
| Registry rows for wave-1 drafts | **0** |
| Policy extension (`de_core_biogenic_lang`) | **Pending** |
| Medium-risk claim boundaries | **20** prep only |
| Publication-ready | **0** |

---

## Recommended order of operations

```
1. Sprint 5N-D (complete) — human candidate source review
2. Sprint 5N-E — external source verification (1–2 drafts)
3. SOURCE_POLICY extension review (biogenic tier) if needed
4. Sprint 5N-F — source registry proposal drafting (1–3 drafts max)
5. Human governance charter for registry execution
6. Sprint 5N-G — source registry execution (small batch, 1–3 rows)
7. Marker satisfaction audit (no auto-removal)
8. Parallel: claim-boundary registration report (20 medium-risk)
9. Draft wave 2 — only after governance debt milestones
```

---

## Criteria for moving a reviewed candidate into future source registry proposal

All must be true:

1. 5N-D human review row with `potentially_suitable_for_future_registry_proposal` or `review_candidate_ready`
2. 5N-E external verification names candidate and confirms category
3. Acceptance criteria in `HUMAN_SOURCE_ACCEPTANCE_CRITERIA_WAVE_1.md` met
4. Rejection decisions clearance
5. Policy extension merged if required
6. Guardrail runtime **PASS**
7. Registry proposal sprint chartered
8. **No** marker removal in proposal sprint

---

## Criteria for rejecting a reviewed candidate

Reject if fails any rejection decision in `HUMAN_SOURCE_REJECTION_DECISIONS_WAVE_1.md` or lacks human-verifiable named authority.

---

## Criteria for requiring formal authority

Required when:

- Evidence matrix flags formal authority **yes**
- Systematic mineral/compound names asserted
- Applies to `copper_sulfides_language`, `de_core_fes`, `de_core_mos2`

Teaching or dictionary alone **insufficient** for formal lines.

---

## Criteria for requiring source policy extension

Required when:

- Source family lacks SOURCE_POLICY category tier
- Applies to `de_core_biogenic_lang` (biogenic/environmental DE lexical tier)
- Applies to `de_core_fes` (DE lexical path underspecification — flagged in 5N-A)

Extension must merge before registry proposal for affected drafts.

---

## How guardrail runtime must be used before and after future source sprints

| Event | Action |
| --- | --- |
| Before verification/proposal/execution doc merge | Run guardrail + corpus L1 |
| After governance doc updates | Re-run guardrail |
| Before any registry edit | Guardrail **PASS** + human charter |
| Before claim activation | Claim lock validators **PASS** |

---

## How this moves the corpus toward 500 governed pages without weakening authority

| Contribution | Effect |
| --- | --- |
| Human review gate | Prevents weak candidates reaching registry |
| Verification sprint | Closes naming gap without fabrication |
| Rejection discipline | Protects trust root |
| No false progress | Markers and planned routes unchanged |

**500 governed pages** require verified sources — human review alone does not increment governed publication count.

---

*Sprint 5N-D — Human Source Review Next Actions Wave 1*
