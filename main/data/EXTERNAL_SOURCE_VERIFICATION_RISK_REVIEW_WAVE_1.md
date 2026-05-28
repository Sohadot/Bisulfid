# External Source Verification Risk Review — Wave 1

**Sprint:** 5N-E  
**Date:** 2026-05-28

---

## Risk of premature source registry entry

Adding registry rows before human external verification completes would create **false verified status**, bypass guardrail intent, and weaken the trust root. Registry remains **inactive**; **0** entries added this sprint.

---

## Risk of weak source evidence

Accepting unsourced web content, AI summaries, or commercial pages without named authority would propagate unverified claims into future publication paths. Both drafts require **human-verified named candidates** before proposal or execution.

---

## Risk of using secondary summaries

AI-generated or tertiary summaries of databases/dictionaries are **not sources** per `SOURCE_POLICY.md`. Humans must verify against original authority tier, not summary pages.

---

## Risk of confusing database authority with nomenclature authority

Element-record database support for `sulfur_element_term_record` does **not** substitute for IUPAC or formal nomenclature where systematic names are asserted. Dictionary support for `de_core_mos2` does **not** cover formal nomenclature lines beyond lexicon scope.

---

## Risk of using dictionary support beyond its authority class

Chemistry dictionary entries support **compound/mineral naming** within scope. They do **not** authorize market data, safety advice, procurement claims, or broad sulfide-family generalizations.

---

## Risk of treating MoS2 source support as broad sulfide support

A verified DE MoS2 lexicon candidate would support **`de_core_mos2` only**. It must not be reused as authority for unrelated sulfide pages, iron sulfides, copper sulfides, or generic sulfide terminology without independent verification per draft.

---

## Risk of treating sulfur element source support as sufficient for all sulfur terminology pages

A verified element-record database for `sulfur_element_term_record` supports **element-level identity lines on that page only**. It does **not** authorize biogenic vocabulary, mineral sulfide pages, or multilingual equivalence claims on other routes.

---

## Risk of removing [SOURCE REQUIRED] markers too early

Verification documentation identifies evidence **classes**, not satisfied linkage. Markers remain until audited registry linkage and governance charter permit removal — not in verification or proposal sprints alone.

---

## Per-draft risk notes — `de_core_mos2`

| Risk | Mitigation |
| --- | --- |
| Lubricant/application market framing | Reject industrial lubricant market sources; naming scope only |
| DE lexicon misapplied to EN routes | DE authority class; independent EN verification where mirrored |
| Teaching as sole authority | Supporting context only |
| Premature proposal without named candidate | Human external verification required before 5N-F |
| Formal name drift | Flag formal nomenclature boundary if systematic names asserted |

---

## Per-draft risk notes — `sulfur_element_term_record`

| Risk | Mitigation |
| --- | --- |
| Teaching substituted for database tier | Reject; database authority required for element identity |
| Database misused for non-element claims | Scope to element-record lines on this page only |
| Safety/market fields in database record | Reject sources with safety/market content |
| Over-generalization to sulfur corpus | Explicit per-page authority boundary |
| Premature registry proposal | Block until human names database candidate |

---

## Why source verification does not equal source approval

This sprint classifies **evidence posture** and **verification gaps**. No candidate is marked approved, verified, or registry-ready. `source_registry.json` is unchanged.

---

## Why source verification does not equal publication readiness

Both drafts remain `draft` / `non_public`, routes remain `planned`, claim registries **inactive**, and matrix `publication-ready` = **no** for all rows. Verification advances governance only.

---

*Sprint 5N-E — External Source Verification Risk Review Wave 1*
