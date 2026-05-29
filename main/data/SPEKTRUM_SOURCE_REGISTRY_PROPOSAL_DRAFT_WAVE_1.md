# Spektrum Source Registry Proposal Draft — Wave 1

**Sprint:** 5N-I  
**Scope:** Primary proposal for `de_core_mos2`  
**Date:** 2026-05-29  
**Status:** Proposal draft only — **not executed**, **not approved**

---

## Proposed source label

**Proposed `source_id`:** `SRC-SPEKTRUM-MOS2-DE`  
**Status:** Label for future execution review only — **not present** in `source_registry.json`.

---

## Proposed source family

**German specialist chemistry reference lexicon** — Spektrum Lexikon der Chemie entry for Molybdän(IV)-sulfid / MoS2 compound naming.

---

## Proposed authority class

| Field | Proposed value |
| --- | --- |
| `category` | `authoritative_dictionary` |
| Authority tier | `chemistry_dictionary_authority` (DE) |
| Language | `de` |
| Human verification basis | **`primary_candidate_verified_for_later_proposal`** (Sprint 5N-H) |

---

## Proposed role for de_core_mos2

| Scope | Proposed support |
| --- | --- |
| Route | `de_core_mos2` only |
| Primary function | German specialist lexicon authority for MoS2 compound naming |
| Draft lines (future, post-execution audit) | Lexikalische Form; Chemische / Dokumentform — scoped to lexicon entry coverage |
| Claim groups (future) | Terminology naming context only — claim approval separate |

---

## Proposed route relationship

| Field | Value |
| --- | --- |
| `route_id` | `de_core_mos2` |
| `content_file` | `main/content/de/pages/terminology/molybdenum-disulfide.md` |
| Route status | `planned` (unchanged) |
| `source_required` | true (unchanged) |
| Proposed linkage | Future audited mapping from approved registry row to specific draft lines — **not performed in 5N-I** |

---

## Claim boundary limits

| Allowed (future, if approved) | Forbidden |
| --- | --- |
| German compound naming for MoS2 | Lubricant market or application performance claims |
| Document-language vocabulary within lexicon scope | Procurement, trade, or industrial operational guidance |
| Specialist dictionary tier for strict-registry DE page | Medical or safety prescriptive claims |
| Scoped terminology naming context | Systematic IUPAC lines beyond lexicon entry without formal nomenclature authority |
| | Universal suffix rules or normative regulatory claims |

**Claim approval:** **Not allowed now.** Even after execution, claim registry activation requires separate sprint.

---

## Why Spektrum is the primary proposal candidate

| Factor | Detail |
| --- | --- |
| Intake | Named primary target (Sprint 5N-G) |
| Verification | **`primary_candidate_verified_for_later_proposal`** (Sprint 5N-H) |
| DE page fit | DE route requires DE-verifiable specialist lexicon |
| Policy | `authoritative_dictionary` approved category |
| Supporting rejection | PubChem/NIST/Chemie.de explicitly not primary |

Spektrum is the **sole** primary proposal draft for Wave 1.

---

## What remains unverified

The following `SOURCE_POLICY.md` registry fields require **direct human verification at execution** — **not invented in this sprint**:

| Field | Status |
| --- | --- |
| `author_or_organization` | **Unverified** — human must confirm from source |
| `publisher` | **Unverified** — human must confirm imprint/edition publisher |
| `publication_date` | **Unverified** — human must confirm edition or access date |
| `url` or `doi` | **Unverified** — human must confirm if applicable; no invented links |
| Entry page-level citation | **Unverified** — human must confirm scope against live entry |
| `linked_claims` | **Empty** — no claims approved |

---

## Why this is only a proposal draft

| Proposal draft | Registry execution |
| --- | --- |
| Documents intended registry structure | Modifies `source_registry.json` |
| No verified status | Requires inactive → verified transition |
| No audited draft linkage | Requires content audit sprint |
| Review artifact for humans | Requires execution charter + sign-off |

Sprint **5N-I** output is **review documentation** — not registry mutation.

---

## Why source_registry.json is not modified

Registry remains **inactive**. Proposal draft does not authorize row insertion. Guardrail discipline requires execution sprint separation.

---

## Why approval is not allowed now

| Gate | Status |
| --- | --- |
| Proposal review | Pending future sprint |
| Human bibliographic verification | Incomplete |
| Execution charter | Not issued |
| Human sign-off | Not performed |
| Verified registry status | **0** new verified entries |

---

## Why source-locking is not allowed now

No approved registry entry exists. No audited line-to-source mapping performed. `[SOURCE REQUIRED]` markers remain on all open factual lines.

---

## Why [SOURCE REQUIRED] markers remain

Markers indicate **unresolved factual lines** pending audited linkage after registry execution and content audit. Proposal draft names **intent** — not approved linkage.

---

## What a future execution sprint would need to verify

1. Human supplies **directly verified** bibliographic fields from Spektrum entry — no AI invention.
2. Human confirms entry scope covers MoS2 German naming lines proposed for `de_core_mos2`.
3. Proposal draft reviewed and accepted by corpus owner or designated reviewer.
4. Guardrail + corpus L1 runtimes **PASS** on registry diff.
5. Separate execution sprint charter with explicit `source_registry.json` edit authorization.
6. Supporting rows (PubChem/NIST/Chemie.de) included only if bounded roles confirmed — optional.
7. Content source-locking and marker resolution — **separate sprints** after execution.

---

## Related documents

- `SOURCE_REGISTRY_PROPOSAL_DRAFT_WAVE_1_REPORT.md`
- `SOURCE_REGISTRY_PROPOSAL_DRAFT_MATRIX_WAVE_1.md`
- `SOURCE_REGISTRY_PROPOSAL_EXECUTION_BLOCKERS_WAVE_1.md`
- `SPEKTRUM_CANDIDATE_AUTHORITY_REVIEW_WAVE_1.md`
- `doctrine/SOURCE_POLICY.md`
