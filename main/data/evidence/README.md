# Atomic Evidence Store — scaffolding (schema only)

**Sprint:** authority-dimension-impl-1 · **Status:** scaffolding_active · **READ-ONLY governance scaffolding.**

This directory holds the atomic evidence architecture defined in
`BISULFID_AUTHORITY_DIMENSION_ARCHITECTURE.md` (Deliverable 3 + Integrity Pass §IP-5/§IP-6/§IP-7/§IP-16.3).

## What exists in this sprint
- `evidence_schema.json` — the atomic evidence schema/specification.
- `fixtures/` — **test-only, non-governed** fixtures (synthetic IDs), used solely by
  `scripts/governance_scaffolding/` tests and validators.

## What does NOT exist in this sprint
- **No real (governed) evidence record.** In particular, `EVD-MOS2-DE-001` is **not** created.
  The German lexeme "Molybdän(IV)-sulfid" has no governed `lexeme_id` yet because the
  Concept↔Lexeme representation is unresolved (IP-9). Creating a real evidence record whose
  subject is an ungoverned free-text lexical string would produce the first semantic orphan.

## The chain (for reference; not instantiated here)
```
source_id -> evidence_id -> claim_id
   \-> entities (concept_id [+ future lexeme_id])
   \-> subject_domain / geography / jurisdiction (where applicable)
   \-> temporal_scope
```

## Invariants enforced by the schema + validator
- **One fact → one owner.** Evidence never copies `source_type` (derive from `source_id`).
- **No editable `used_by`.** Reverse usage is derived, not hand-maintained.
- **No ungoverned `confidence`.**
- **Source ≠ Evidence ≠ Claim postures** are independently owned.
- **Test vs production separation:** production IDs start `EVD-`; fixtures start `TEST-EVD-`
  with `governed: false`, `test_fixture: true`, and reference only `TEST-` synthetic IDs.
- **Missing values stay explicitly missing** — never synthesized.

## Not wired to anything
These artifacts are validated only by `scripts/governance_scaffolding/validate_scaffolding.py`.
They are not referenced by build, deploy, sitemap, robots, routes, release ledger, or CI hard-fail.
