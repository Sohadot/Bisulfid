# Corpus Production Automation Next Actions — Layer 2

**Sprint:** 5O-A  
**Date:** 2026-05-29

---

## Recommended next sprint

**Sprint 5O-B — Production dry-run wave planning** (route registration wave 2 **planning manifest and validation only** — no `routes.json` edits unless separately chartered execution sprint).

Run before and after:

```bash
python scripts/corpus_production_runtime_l2.py
python scripts/corpus_validation_runtime_l1.py
python scripts/source_claim_guardrail_runtime_l1.py
```

---

## Whether to proceed to 5N-G named source candidate intake

**Yes — parallel, not blocking 5O-B.**

`de_core_mos2` remains the conditional proposal-readiness candidate. Named DE specialist lexicon intake (5N-G) should proceed under source program charter while L2 production planning matures.

---

## Whether to proceed to 5O-B production dry-run wave planning

**Yes — primary L2 follow-on.**

5O-B produces route registration wave 2 **manifest**, cluster targets, and dry-run validation — still **no** route rows unless execution sprint chartered.

---

## Whether to proceed to route registration wave 2

**Planning only — after 5O-B manifest.**

Do **not** edit `routes.json` in planning sprint. Use L2 wave control model maximum size (**80–120** routes) when chartering execution.

---

## Whether to proceed to draft wave 2

**No — draft wave 2 should still wait.**

| Debt | Status |
| --- | --- |
| Named verified source candidates | **0** |
| Registry rows for wave-1 drafts | **0** |
| Governance debt (5N-F blockers) | **Active** |
| L2 planning baseline | **Established (5O-A)** |
| Publication-ready drafts | **0** |

Draft wave 2 requires reduced governance debt + L2 manifest alignment.

---

## Why draft wave 2 should still wait

Source/claim gates incomplete; **58** routes still lack drafts from wave 1 registration; mass draft production without gates risks thin content. L2 automation does not bypass draft gate.

---

## Why route registration wave 2 should use L2 production planning first

L2 defines wave sizes, order of operations, and gate sequence. Registering **80–120** routes without link/SEO/multilingual planning documents risks orphan routes and broken cluster architecture.

---

## Why source/claim gates remain mandatory

- **0** approved claims; registries **inactive**
- `sulfur_element_term_record` blocked until database candidate named
- `de_core_mos2` conditional only after named lexicon intake
- No mass page generation without source/claim/link gates

---

## How to move safely toward 500 governed pages

```
1. L2 automation (5O-A complete)
2. 5N-G source candidate intake (parallel)
3. 5O-B route wave 2 planning manifest
4. Route registration execution (chartered; 80–120 max)
5. Draft production waves (40–60; vertical slices)
6. Source/claim waves per gate model
7. Internal link + SEO + multilingual planning waves
8. Publication readiness only after ≥ 500 pages pass ALL gates
```

Current: **126** routes, **68** draft-backed — **374** routes short of launch floor.

---

## How to eventually scale toward 1,000+ / 3,000+ / massive corpus scale without weakening standards

| Principle | Enforcement |
| --- | --- |
| Governance-first automation | L2 read-only; L3/L4 chartered separately |
| Wave discipline | Max sizes in wave control model |
| Gate sequence | Publication last |
| Audit + rollback | Every wave produces validation report |
| Authority over volume | Launch threshold + anti-thin rules |
| Human review | Registry, claims, publication always |

Massive scale is **optional** and **only** if governance remains non-negotiable at each layer.

---

*Sprint 5O-A — Corpus Production Automation Next Actions Layer 2*
