# Source Registry Proposal Execution Blockers — Wave 1

**Sprint:** 5N-I  
**Scope:** Blockers before `source_registry.json` may be modified for `de_core_mos2`  
**Date:** 2026-05-29

---

## Blockers before source_registry.json may be modified

All must be cleared in a **separate execution sprint** — not Sprint 5N-I:

1. Proposal draft reviewed and accepted (`SOURCE_REGISTRY_PROPOSAL_DRAFT_WAVE_1_REPORT.md`, `SPEKTRUM_SOURCE_REGISTRY_PROPOSAL_DRAFT_WAVE_1.md`).
2. Explicit execution sprint charter issued — distinct from proposal drafting.
3. Human sign-off on inactive → verified registry transition.
4. Guardrail runtime **PASS** on proposed registry diff.
5. Corpus L1 runtime **PASS**.
6. No marker removal bundled with registry execution.

---

## Human bibliographic verification blockers

| Blocker | Detail |
| --- | --- |
| Invented bibliography forbidden | DOI, ISBN, edition, author, publisher, date, page numbers must come from direct human verification |
| Spektrum fields unverified | All `SOURCE_POLICY.md` required fields pending human confirmation at execution |
| Entry scope confirmation | Human must confirm live Spektrum entry covers proposed MoS2 German naming lines |
| Supporting row bibliography | If PubChem/NIST/Chemie.de rows included — each requires separate human verification |

Proposal draft **deliberately omits** unverified bibliographic values.

---

## SOURCE_POLICY alignment blockers

| Blocker | Detail |
| --- | --- |
| Category fit | Spektrum must map to `authoritative_dictionary` — proposed; execution must confirm |
| Blocked uses | No market, safety prescriptive, medical, procurement, or handling claims from lexicon row |
| Academic teaching tier | Not applicable as primary — Spektrum is specialist lexicon tier |
| Registry format | All required fields must be populated with verified values at execution |
| `linked_claims` | Empty until claim approval sprint — no premature claim linkage |

---

## Claim boundary blockers

| Blocker | Detail |
| --- | --- |
| Claim registries inactive | **0** approved claims |
| Claim boundary registration | MoS2 lexical/document-form boundaries not yet registered in claim artifacts |
| Claim approval sprint | Separate from registry execution |
| Terminology claims | `terminology_claims.json` **not modified** in 5N-I |

Registry execution does **not** auto-approve claims.

---

## Source registry schema blockers

| Blocker | Detail |
| --- | --- |
| Registry status | **inactive** — transition policy required |
| Proposed `source_id` | `SRC-SPEKTRUM-MOS2-DE` — label only; not inserted |
| Supporting optional IDs | PubChem/NIST/Chemie.de labels — not inserted |
| Verified status | No row may receive `verified` without human sign-off |
| Existing seeded rows | New rows must not conflict with existing `source_id` namespace |

---

## Content source-locking blockers

| Blocker | Detail |
| --- | --- |
| Content unchanged | `de_core_mos2` draft not edited in 5N-I |
| No audited linkage | Line-to-source mapping not performed |
| Source-locking sprint | Separate charter after registry execution |
| Marker discipline | `[SOURCE REQUIRED]` remains until content audit |

---

## [SOURCE REQUIRED] marker blockers

| Blocker | Detail |
| --- | --- |
| Markers present | Lexical and document-form lines still marked |
| Proposal ≠ resolution | Drafting does not resolve factual lines |
| Audit required | Marker removal requires approved source + audited mapping sprint |
| False confidence risk | Proposal must not imply markers are cleared |

---

## Publication readiness blockers

| Blocker | Status |
| --- | --- |
| Route status | `planned` |
| Draft | `non_public` |
| Indexation | false |
| Launch threshold | **126** / **500** — not met |
| Source lock | Not complete |
| Claim approval | **0** |
| Owner sign-off | Not performed |
| `production_can_safely_proceed` | **no** |

---

## CI governance blockers

| Blocker | Detail |
| --- | --- |
| Corpus Governance CI | Required on PR — validates discipline, not source approval |
| CI PASS ≠ execution authorization | Merge allowed ≠ registry edit authorized |
| Branch protection | Active on `main` |
| Execution diff | Future registry PR must pass guardrail + L1 runtimes |

---

## Human review blockers

| Blocker | Detail |
| --- | --- |
| Proposal review | Owner/designated reviewer must accept proposal draft before execution |
| Bibliographic review | Human must verify all registry field values |
| Scope review | Confirm Spektrum scope matches `de_core_mos2` lines only |
| Supporting elevation | Reject any attempt to elevate Chemie.de or database rows to primary |

---

## Why execution requires a separate future sprint

| Proposal drafting (5N-I) | Execution (future) |
| --- | --- |
| Documents intent | Modifies `source_registry.json` |
| No verified rows | Creates verified registry entries |
| No content edits | Enables future source-lock path |
| No claim activation | Precedes claim boundary work |
| Governance artifact | Operational registry change |

Sprint **5N-I** completes the **proposal layer**. Execution is a **distinct authorization event**.

---

## Related documents

- `SOURCE_REGISTRY_PROPOSAL_DRAFT_WAVE_1_REPORT.md`
- `SOURCE_REGISTRY_PROPOSAL_NEXT_ACTIONS_WAVE_1.md`
- `SOURCE_REGISTRY_PROPOSAL_BLOCKERS_WAVE_1.md` (Sprint 5N-F)
- `doctrine/SOURCE_POLICY.md`
