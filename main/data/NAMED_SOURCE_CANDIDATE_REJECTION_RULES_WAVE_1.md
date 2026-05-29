# Named Source Candidate Rejection Rules — Wave 1

**Sprint:** 5N-G  
**Scope:** `de_core_mos2` named source intake  
**Date:** 2026-05-29

---

## Purpose

These rules define when a named source candidate must be **rejected**, **deferred**, or classified as **`named_candidate_absent`** / **`named_candidate_rejected`**. Rejected candidates must **not** enter `source_registry.json` or be used to remove `[SOURCE REQUIRED]` markers.

---

## Rejection rules for unsourced or vague named candidates

| Rule | Action |
| --- | --- |
| No specific work named | Classify **`named_candidate_absent`** — current Sprint 5N-G finding |
| Family-only label ("a German chemistry dictionary") | Reject as **`candidate_family_only`** — not a named candidate |
| Vague reference ("standard lexicon", "common dictionary") | Reject — insufficient for external verification |
| Repository cannot verify identity | Defer until human supplies verifiable identifier |

---

## Rejection rules for AI-generated or unverified sources

| Rule | Action |
| --- | --- |
| AI-suggested title without human confirmation | Reject — not human-provided |
| Invented DOI, ISBN, edition, author, publisher, date | Reject — forbidden in all sprints |
| "Likely" or "probably" bibliographic details | Reject — treat as unverified |
| Automation-generated citation blocks | Reject for intake — human must name and verify |

---

## Rejection rules for general web pages without authority

| Rule | Action |
| --- | --- |
| Blog posts, forums, Q&A sites | Reject — no reference authority |
| Wikipedia or crowd-sourced pages as primary authority | Reject for strict-registry terminology |
| Marketing landing pages | Reject |
| SEO glossary farms | Reject — thin generic chemistry content |

---

## Rejection rules for commercial pages without reference authority

| Rule | Action |
| --- | --- |
| Lubricant manufacturer product pages | Reject — market/application drift for MoS2 route |
| Procurement or supplier catalog pages | Reject |
| Industrial equipment vendor marketing | Reject |
| Paywalled content without verifiable reference edition | Defer — human must confirm access and edition |

---

## Rejection rules for dictionaries used beyond their authority class

| Rule | Action |
| --- | --- |
| General bilingual dictionary for specialist MoS2 naming | Reject or defer — scope mismatch |
| EN dictionary as sole authority for DE page | Reject without DE verification path |
| Dictionary cited for systematic IUPAC names beyond lexicon scope | Reject for those lines — requires formal nomenclature authority |
| Teaching textbook as sole authority for strict-registry page | Reject — supporting context only per 5N-E |

---

## Rejection rules for sources not aligned with SOURCE_POLICY

Reject when candidate would require:

- Market data, CAGR, market-share, or trade statistics
- Safety handling instructions or exposure thresholds
- Medical or pharmaceutical claims beyond document-language vocabulary
- Procurement advice or operational guidance
- Acquisition-target or investment framing
- Universal suffix transformation rules without formal authority

---

## Rejection rules for candidates that cannot be human-verified

| Rule | Action |
| --- | --- |
| No human can access or confirm entry | Defer — not intake-ready |
| Out-of-print work with no verifiable edition | Defer until human confirms edition |
| Candidate scope cannot cover MoS2 German naming | Reject for this draft |
| Conflicting authority classes across proposed sources | Reject composite until scoped |

---

## Why rejected candidates must not enter source_registry.json

Registry rows imply **governance commitment** and future source-locking paths. Rejected or absent candidates have **0** verified evidence. Adding rows would:

- Bypass human external verification (5N-E)
- Bypass proposal readiness gates (5N-F)
- Create false authority signal for `de_core_mos2`
- Violate inactive registry discipline

---

## Why rejected candidates must not be used to remove [SOURCE REQUIRED] markers

Markers protect against unverified factual publication. A rejected or family-only candidate does not resolve lexical or document-form lines. Removal requires **approved** source linkage after registry execution and content audit — not intake classification alone.

---

## Sprint 5N-G application

| Candidate type | Disposition |
| --- | --- |
| No human-named specific lexicon | **`named_candidate_absent`** |
| Evidence family only (5N-C / 5N-E) | **`candidate_not_provided`** — not rejection of a named work, but absence of naming |
| Future human-named candidate | Evaluate against these rules in re-intake or verification sprint |

---

## Related documents

- `NAMED_SOURCE_CANDIDATE_ACCEPTANCE_RULES_WAVE_1.md`
- `NAMED_SOURCE_CANDIDATE_INTAKE_WAVE_1_REPORT.md`
- `CANDIDATE_SOURCE_REJECTION_RULES_WAVE_1.md` (Sprint 5N-C)
- `HUMAN_SOURCE_REJECTION_RULES_WAVE_1.md` (Sprint 5N-D)
- `doctrine/SOURCE_POLICY.md`
