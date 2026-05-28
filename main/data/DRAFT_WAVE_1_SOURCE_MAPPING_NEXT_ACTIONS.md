# Draft Wave 1 — Source Mapping Next Actions

**Sprint:** 5M  
**Date:** 2026-05-27  
**Context:** 12 cohort-A drafts mapped; 20 medium-risk drafts prepared; 0 publication-ready

---

## Recommended next sprint

**Sprint 5N-A — Source registration proposal wave 1** (report-only candidate rows for **4–6** lowest-gap cohort-A drafts) **in parallel with Sprint 5N-B — Claim boundary registration report** for **20** medium-risk drafts.

Run `python scripts/corpus_validation_runtime_l1.py` before and after each sprint. Archive validation results.

---

## Should Sprint 5N be source registration for selected mapped drafts?

**Yes — primary track (5N-A), report-only first.**

| Parameter | Value |
| --- | --- |
| Batch size | **4–6** drafts (subset of **12** mapped) |
| First candidates | `sulfur_element_term_record`, `de_core_biogenic_lang`, `copper_sulfides_language`, `de_core_cus`, `de_core_fes`, `de_core_mos2` |
| Output | Proposed registry rows + marker mapping manifest |
| Forbidden this sprint | Actual `source_registry.json` edits unless explicitly chartered; marker removal |

---

## Should Sprint 5N be claim-boundary registration for medium-risk drafts?

**Yes — parallel track (5N-B).**

| Parameter | Value |
| --- | --- |
| Batch size | **20** drafts (full medium-risk cohort) |
| Output | Claim boundary registration **report** only |
| Maps to | `terminology_claims`, `industry_claims` (future; registries stay inactive) |
| Forbidden | Claim approval; registry activation; content edits |

---

## Should Sprint 5N be content hardening for legacy drafts?

**Optional parallel (5N-C) — lower priority.**

| Parameter | Value |
| --- | --- |
| Batch size | **4** doctrine drafts + phased legacy normalization |
| Scope | **18** pre-5J legacy drafts (L1 warnings) |
| Rationale | Does not block 5N-A/5N-B but reduces L1 warning noise |

Not recommended as **primary** 5N track; can run if editorial capacity allows.

---

## Should Sprint 5N be draft wave 2?

**No — defer to Sprint 5O or later.**

Draft wave 2 (**40–60** routes still missing bodies) should wait until:

1. Source registration **proposals** filed for first cohort-A subset (5N-A).
2. Claim boundary **report** filed for **20** medium-risk drafts (5N-B).
3. L1 runtime **PASS**.
4. No new blocked drift in industrial/compliance cohort.

---

## Recommended order of operations

1. **5N-A** — Source registration **proposals** (4–6 cohort-A drafts).
2. **5N-B** — Claim boundary registration report (20 medium-risk drafts).
3. **5N validation** — L1 PASS; update validation report.
4. **5N-C** (optional) — Legacy draft structure hardening (4–18 drafts phased).
5. **5O** — Source registration **execution** sprint (human-chartered registry edits) if authorized.
6. **5P** — Draft production wave 2 (40–60 drafts).
7. **5Q** — Route registration wave 2 toward 500-page floor.

---

## Batch sizes

| Workstream | Batch size |
| --- | --- |
| Source registration proposals | **4–6** drafts |
| Claim boundary registration report | **20** drafts |
| Content hardening (legacy) | **4** per sprint |
| Draft production wave 2 | **40–60** drafts (after 5N complete) |

---

## Why draft wave 2 should still wait

| Debt remaining after 5M | Count |
| --- | ---: |
| Mapped but unregistered cohort A | **12** |
| Medium-risk without claim boundaries | **20** |
| Blocked/reframe drafts | **3** |
| Routes without drafts | **58** |

Adding **50** new drafts before registration proposals and claim-boundary reports would produce an **unsourced corpus** of **110+** pages.

---

## How source mapping wave 1 moves toward 500 governed pages

1. **12** drafts now have audit-grade source category plans (was: classified only).
2. **20** medium-risk drafts have claim-boundary prep (was: flagged only).
3. Future registration sprints can execute against **manifests** instead of ad hoc review.
4. Quality preserved: no false source-lock; no publication shortcut.
5. Repeat mapping pattern for each future draft wave before scaling production.

---

## How to avoid creating a large unsourced corpus

- **Map before scale** — every draft wave followed by mapping sprint.
- **Register in small batches** — 4–6 proposals per sprint.
- **Claim boundaries before industrial/compliance mapping** — medium-risk gate enforced.
- **L1 after every wave** — structural failures stop the line.
- **No marker removal** until verified registry + human authorization.

---

## How to use L1 validation before the next wave

```bash
python scripts/corpus_validation_runtime_l1.py
```

| When | Action |
| --- | --- |
| Before 5N-A / 5N-B | Confirm PASS baseline |
| After 5N deliverables | Confirm no accidental content/registry drift |
| Before draft wave 2 | Confirm PASS + triage warnings |
| Merge gate | Block on L1 FAIL |

Review `main/data/CORPUS_L1_VALIDATION_REPORT.md` and wave-specific reports each cycle.

---

*Sprint 5M — Source Mapping Next Actions*
