# External Source Verification Next Actions — Wave 1

**Sprint:** 5N-E  
**Date:** 2026-05-28

---

## Recommended next sprint

**Sprint 5N-F — Source registry proposal drafting wave 1** (maximum **1–3** drafts) **only after** humans externally verify and name acceptable candidates. Prioritize `de_core_mos2` if DE specialist lexicon candidate is confirmed. Still **no** `source_registry.json` row writes unless execution sprint chartered separately.

Alternative parallel track: **claim-boundary registration report** for medium-risk drafts (unchanged from prior recommendations).

Run before and after:

```bash
python scripts/source_claim_guardrail_runtime_l1.py
python scripts/corpus_validation_runtime_l1.py
```

---

## Whether next step should be source registry proposal drafting

**Yes — conditional.**

| Draft | Proposal drafting next |
| --- | --- |
| `de_core_mos2` | **Yes** — after human names acceptable DE specialist lexicon candidate |
| `sulfur_element_term_record` | **No** — until human names and verifies element-record database tier |

Maximum **1–3** drafts per proposal sprint. **No** marker removal in proposal sprint.

---

## Whether next step should be source registry editing

**No.**

Registry execution requires: human external verification complete, proposal sprint chartered, governance charter for execution, guardrail **PASS**. Current verified entries: **0** for both priority drafts.

---

## Whether next step should be claim-boundary registration/reporting

**Parallel, not blocking.**

Medium-risk drafts still need claim-boundary registration **report**. Do not activate claim registries.

---

## Whether legacy draft hardening should happen before draft wave 2

**Schedule separately; do not block 5N-F.**

Legacy pre-5J L1 warnings remain incremental debt.

---

## Whether draft wave 2 should still wait

**Yes.**

| Debt | Status |
| --- | --- |
| Human external verification | **0** named verified candidates |
| Registry rows for wave-1 drafts | **0** |
| Policy extension (`de_core_biogenic_lang`) | **Pending** |
| Medium-risk claim boundaries | Prep only |
| Publication-ready | **0** |

---

## Recommended order of operations

```
1. Sprint 5N-E (complete) — external source verification documentation
2. Human external verification — name DE lexicon (de_core_mos2) and database (sulfur_element_term_record)
3. Sprint 5N-F — source registry proposal drafting (1–3 drafts max)
4. Human governance charter for registry execution
5. Sprint 5N-G — source registry execution (small batch, 1–3 rows)
6. Marker satisfaction audit (no auto-removal)
7. Parallel: claim-boundary registration report (medium-risk)
8. Draft wave 2 — only after governance debt milestones
```

---

## Criteria for moving verified evidence into a future source registry proposal

All must be true:

1. 5N-E external verification row with `evidence_family_identified` or better
2. Human externally verifies and **names** specific candidate (outside repo — not invented bibliographic lines in governance docs)
3. Candidate category confirmed under `SOURCE_POLICY.md`
4. Acceptance criteria in `HUMAN_SOURCE_ACCEPTANCE_CRITERIA_WAVE_1.md` met
5. Rejection decisions clearance
6. Guardrail runtime **PASS**
7. Registry proposal sprint chartered
8. **No** marker removal in proposal sprint

---

## Criteria for rejecting evidence

Reject if fails any rejection decision in `HUMAN_SOURCE_REJECTION_DECISIONS_WAVE_1.md` or:

- Unsourced web, AI summaries, commercial pages without authority
- Teaching as sole formal authority
- Dictionary/database used beyond authority class
- MoS2 lubricant market sources
- Element database treated as corpus-wide sulfur authority
- Cannot human-verify named publisher/database/lexicon

---

## Criteria for requiring additional human verification

Required when:

- Evidence posture is `candidate_evidence_requires_human_review` or external status is `human_external_verification_required`
- Applies to **both** priority drafts in 5N-E
- Named candidate, category fit, scope boundary, and marker mapping must be confirmed externally

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
| Verification gate | Closes naming gap without fabrication |
| Per-draft authority boundaries | Prevents over-generalization of MoS2 or element support |
| Rejection discipline | Protects trust root |
| No false progress | Markers and planned routes unchanged |
| Conditional proposal path | `de_core_mos2` may advance first after human naming |

**500 governed pages** require verified sources and approved claims — verification documentation alone does not increment governed publication count.

---

*Sprint 5N-E — External Source Verification Next Actions Wave 1*
