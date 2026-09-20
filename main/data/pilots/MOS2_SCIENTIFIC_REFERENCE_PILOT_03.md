# Pilot 03 — MoS₂ Scientific Reference Chain

**Date:** 2026-09-20 · **Baseline:** commit `fc72d805f4` · **Concept:** `molybdenum_disulfide`
**Objective:** test the concept-level SCIENTIFIC evidence path, independently of the existing German lexical chain. Max three concept-level claims.
**Constraints honored:** no Morocco expansion, no GCC/China/Germany geography program, no 14K migration, no public routes, no publication/indexation, no weakening of existing source/evidence rules. Search located sources only; no AI summaries or snippets used as evidence. The lexical chain (`molybdenum_disulfide → LEX-DE-MOS2-001 → EVD-MOS2-DE-001 → SRC-SPEKTRUM-MOS2-DE`) is untouched.

## Scientific sources acquired (all verified, lock candidate)

| Source | Category | Retrieved (verbatim) |
|---|---|---|
| `SRC-PUBCHEM-MOS2` | government_scientific_database | PubChem CID 14823 → MolecularFormula `MoS2`, MW `160.1`, CAS 1317-33-5 |
| `SRC-NIST-MOS2` | government_scientific_database | NIST Chemistry WebBook (CAS 1317-33-5) → Formula `MoS2`, MW `160.09 amu` |
| `SRC-COD-MOS2-DICKINSON-1923` | peer_reviewed_journal (via COD 1010993) | Dickinson & Pauling, JACS 45, 1466 (1923), doi 10.1021/ja01659a020 → `P 6₃/m m c` (No. 194), a=3.15(2) Å, c=12.30(7) Å |
| `SRC-COD-MOS2-ACTACRYST-1983` | peer_reviewed_journal (via COD 9007660) | Schönfeld, Huang & Moss, Acta Cryst. B 39, 404 (1983), doi 10.1107/S0108768183002645 → `P 6₃/m m c`, a=3.161 Å, c=12.295 Å |

No new source **category** was invented (§6): databases → `government_scientific_database`; crystallographic determinations → `peer_reviewed_journal` (COD is the retrieval artifact). No new evidence **role** was needed: databases use `primary_authoritative`, primary determinations use `primary_scientific` (already governed, and precise — a database vs a primary study are thereby distinguished).

## Three claims attempted → outcomes

### Proven

- **Claim A — chemical identity / formula** (`CLM-MOS2-FORMULA`): *Molybdenum disulfide has formula MoS₂.* **SUPPORTED.** Two independent government databases (PubChem + NIST) → `primary_plus_corroborating` satisfied → **evidence_sufficient**. Evidence: `EVD-MOS2-FORMULA-PUBCHEM`, `EVD-MOS2-FORMULA-NIST`.
- **Claim B — crystal/structural identity** (`CLM-MOS2-STRUCTURE-2H`): *2H-MoS₂ (molybdenite) crystallizes in hexagonal space group P 6₃/m m c (No. 194), a layered structure.* **SUPPORTED.** Two independent primary crystallographic determinations (1923 + 1983) → **evidence_sufficient**. Evidence: `EVD-MOS2-STRUCTURE-DICKINSON`, `EVD-MOS2-STRUCTURE-ACTACRYST`.

### Conditional

- **Claim C — one physical property: lattice parameter a of 2H-MoS₂** (`CLM-MOS2-LATTICE-A-2H`): reported **a = 3.15(2) Å** (1923) and **a = 3.161 Å** (1983). **SUPPORTED_CONDITIONAL** — scoped to **2H bulk**; the two independent determinations **coexist** (agree within uncertainty) and are preserved separately (no averaging, no forced single scalar). `primary_plus_corroborating` satisfied → **evidence_sufficient**. Evidence: `EVD-MOS2-LATTICE-A-DICKINSON`, `EVD-MOS2-LATTICE-A-ACTACRYST`. Numeric normalization: `NUM-EN-DOT-DECIMAL`; `source_literal` vs `normalized_value` distinct; uncertainty (0.02 Å) preserved; no unit conversion.

### Contested

- None forced. The lattice determinations agree; they are represented as coexisting records rather than a single value (the machinery for genuine disagreement is exercised by keeping both).

### Blocked / not attempted

- **Band gap** was considered for Claim C but **not asserted**: MoS₂'s band gap is strongly **form-dependent** (bulk 2H is an **indirect**-gap semiconductor; **monolayer** MoS₂ is a **direct**-gap semiconductor), and an authoritative **primary** source giving the exact values/conditions was not openly retrievable here (peer-reviewed publisher pages gated; no snippets/AI used). Recorded as a future target. No band-gap value is asserted.

## Not inferred

- No property was globalized across forms: the 2H-bulk lattice parameter must never be attached to monolayer/few-layer or 3R MoS₂ (enforced by `form_scope_rule` + a `polytype_3r_or_1t_or_monolayer` veto).
- The **3R polytype** (space group R3m, c ≈ 18.3 Å) is present in COD and is kept **distinct** from 2H; polytype-specific values are not collapsed into the generic concept.
- No electronic/optical property was inferred from a structural source (a structure/lattice qualification does **not** support band gap — §14).
- The German lexical source established nothing scientific; scientific sources established no lexeme.

## Policy findings

1. **Sufficiency held honestly.** The existing `chemistry_materials_physics` domain requires `primary_plus_corroborating`; it was **not weakened**. Each claim reached `evidence_sufficient` only because two genuinely independent sources exist. A single source would have left a claim `evidence_collecting`.
2. **Database vs primary-study roles** are already distinguishable (`primary_authoritative` vs `primary_scientific`); no vocabulary extension was necessary. A dedicated `authoritative_database` role remains a possible future refinement, not a need.
3. **Use-scoped qualification** works across fact types: the same crystallographic source is qualified for structure + lattice parameter but **prohibited** for band gap.
4. **Form/polytype as a scope qualifier** (in the evidence record) is sufficient for now; no per-form ontology concept was created.

## Future ontology needs (reported, not acted on)

- If durable, form-specific concepts are later required (e.g. `mos2_2h`, `mos2_3r`, `mos2_monolayer`), that is an ontology-governance decision, not a pilot action. For now, polytype/form is a **scope qualifier** on the evidence, and the generic `molybdenum_disulfide` concept is retained.
- A `sulfuric_acid`-style separate-species concept is **not** relevant here and was not created.
- Acquiring band-gap primary literature would exercise genuine `contested`/`conditional` handling (bulk indirect vs monolayer direct) and may motivate form-scoped modelling.

## Evidence postures & Contract-C

All six records: `admissible() = True`, review posture `evidence_verified`, source lock `candidate` (so **never** `evidence_locked`). Derived per-claim posture: A/B/C = **evidence_sufficient**. **Contract-C = (not_public, noindex)** for every object. No route, sitemap, robots, indexation, claim activation, or source-lock.

## Tests

`pilot_03_tests.py` (23 proofs) PASS — incl. Spektrum-cannot-support-scientific (A/B/C), scientific-cannot-establish-a-lexeme, concept resolution, polytype/form scope retained, form-value veto, numeric unit+conditions+normalization, coexisting values, category-alone-inadmissible, use-scoped qualification, verification≠lock, admission≠activation, no routes, no public page, Contract-C safe, Spektrum stays lexical-only. All Pilot-01/Pilot-02/governance regressions green; wired L0/L1/L2 CI PASS.
