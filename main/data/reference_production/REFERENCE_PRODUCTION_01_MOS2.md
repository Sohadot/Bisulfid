# Reference Production 01 — MoS₂ Scientific Knowledge Object → Information Gain Candidate

**Date:** 2026-09-20 · **Baseline:** commit `48f4b7e583` · **Entity:** `molybdenum_disulfide`
First REFERENCE PRODUCTION sprint. Exercises the chain **Evidence → Claim Set → Knowledge Object → Information Gain review → Publication Candidate**. NOT a publication/route/acquisition/14K-migration sprint. No public URL is authorized. Uses only Pilot-03 governed evidence/claims; no web, no new sources, no band gap.

## 1. Knowledge Object

- **ID:** `KO-MOS2-SCIENTIFIC-001` (`main/data/knowledge_objects/knowledge_object_registry.json`).
- **Reference task:** "What scientifically established identity and bulk structural facts can BISULFID currently support for molybdenum disulfide?"
- **knowledge_role:** `scientific_reference`. **entity_ids:** `[molybdenum_disulfide]`. **subject_domains:** SD-INORGANIC-CHEMISTRY, SD-MATERIALS-SCIENCE. **language_neutral:** true. **claim_source:** `pilot_non_operational`.
- **One-Fact-One-Owner:** the KO owns only composition (which claims/evidence belong together), scope, boundaries, unresolved/excluded areas, and reference role. It copies **no** source literals or normalized values (forbidden fields enforced); display values derive from evidence.

## 2. Exact bindings

| Component | Claim (pilot, non-operational) | Evidence |
|---|---|---|
| Formula | `CLM-MOS2-FORMULA` | `EVD-MOS2-FORMULA-PUBCHEM`, `EVD-MOS2-FORMULA-NIST` |
| Structure (layered / 2H / P6₃/mmc) | `CLM-MOS2-STRUCTURE-2H` | `EVD-MOS2-STRUCTURE-DICKINSON`, `EVD-MOS2-STRUCTURE-ACTACRYST`, `EVD-MOS2-2H-REF-RSC`, `EVD-MOS2-LAYERED-RSC`, `EVD-MOS2-POLYTYPES-RSC`, `EVD-MOS2-LAYERED-ACTA1983-EXCERPT`, `EVD-MOS2-MOLYBDENITE-JACS1923-EXCERPT`, `EVD-MOS2-LAYERED-HUANG1981` |
| Lattice a (2H bulk) | `CLM-MOS2-LATTICE-A-2H` | `EVD-MOS2-LATTICE-A-DICKINSON`, `EVD-MOS2-LATTICE-A-ACTACRYST` |
| **Boundary (not a 2H claim)** | — | `EVD-MOS2-3R-BOUNDARY-RSC` (bound as `boundary_evidence_ids` only) |

Claims A/B/C are unchanged from Pilot 03 and remain non-operational (referenced, not activated).

## 3. Evidence posture (recomputed via the real engine)

A → evidence_sufficient, B → evidence_sufficient, C → evidence_sufficient; aggregate **evidence_sufficient**. Source locks remain **candidate** → **no** `evidence_locked`. No source was locked.

## 4. Unresolved / excluded

- **Unresolved:** band gap (form-dependent; future), other physical properties, 3R lattice as a primary fact (held only as boundary).
- **Excluded claim classes:** band_gap, electronic/optical property, density, monolayer/few-layer property, market, safety, industrial-use, German terminology.

## 5. Nearest legacy MoS₂ routes (found in `routes.json`; NOT modified)

- `molybdenum_disulfide` → `/molybdenum-disulfide/` (legacy English scientific/compound page; ungoverned).
- `de_core_mos2` → `/de/terminology/molybdenum-disulfide/` (German lexical surface; the lexical chain's route scope).
- `de_molybdenum_disulfide` → `/de/molybdenum-disulfide/`; `de_term_molybdaensulfid` → `/de/terminology/molybdansulfid/`.
- ~150 `cohort02_en_molybdenum_disulfide_*` thin term/compound/audience/AI variants (comparison candidates only). None modified, migrated, or retired.

## 6. Information Gain comparisons (calibration pairs seeded)

`main/data/information_gain/calibration_pairs.json` (status `seeded`; schema extended minimally for governed `object_a/object_b` endpoints; **no numeric threshold**). Real pairs:

1. **`PAIR-KO-MOS2-SCI-vs-DE-LEXICAL`** → **`valid_domain_specific_reference`**: scientific KO vs `de_core_mos2` — disjoint evidence/claims/sources; different task. Deleting one loses governed knowledge the other lacks.
2. **`PAIR-KO-MOS2-SCI-vs-LEGACY-SCI-ROUTE`** → **`near_duplicate`**: KO vs `molybdenum_disulfide` — same scientific task; the legacy route holds no governed knowledge, so a NEW independent URL is not warranted (the KO governs that topic; it does not add a second URL).
3. **`PAIR-KO-MOS2-FORMULA-vs-STRUCTURE-MODULE`** → **`near_duplicate`**: formula vs structure as separate hypothetical URLs — they are MODULES of one object, not sibling URLs.

## 7. Information Gain decision

Human-readable, evidence-based, multi-signal — **no numeric score, no threshold**, textual similarity diagnostic only (full Q&A in `PC-MOS2-SCIENTIFIC-001.ig_review`). Findings: distinct governed knowledge and reference task (independent reference value); ONE coherent object (formula/structure/property remain modules, not separate URLs); distinct from the German lexical object; same-task overlap with the legacy scientific route means no new URL is warranted.

**IG posture = `ig_not_reviewed`.** The review is complete, but current governance ratifies **no** non-numeric IG-pass authority, so the posture stays `ig_not_reviewed` pending ratification (an acceptable successful outcome per the sprint).

## 8. Formula/structure/property — modules or separate objects?

**Modules of one KO.** Splitting them into separate URLs would create redundant near-duplicate surfaces for one coherent reference task.

## 9. Distinction from the German lexical MoS₂ object

`CLM-TERM-MOS2-DE-001` / `LEX-DE-MOS2-001` / `EVD-MOS2-DE-001` (Spektrum) is a terminology knowledge role in a different domain with a disjoint evidence/claim set. It is **not** merged into `KO-MOS2-SCIENTIFIC-001` (enforced by validator + test).

## 10. Publication-candidate state & Contract-C

`main/data/publication_candidates/PC-MOS2-SCIENTIFIC-001.json`, status `internal_candidate`, disposition **`independent_reference_candidate`** (explicitly not published/indexable/public_noindex). **Contract-C = (not_public, noindex)**, DERIVED via `contract_c_derive.derive(reference_draft, evidence_sufficient, claim_pending, not_validated, ig_not_reviewed, not_authorized)` — never manually written. Legacy 14K visibility artifacts do not govern this object.

## 11. Exact blockers before ANY future URL

1. IG posture `ig_not_reviewed` → needs `ig_passed` under a ratified (currently non-existent) authority;
2. claims are pilot non-operational (`claim_pending`) → not activated;
3. `not_validated`;
4. `release_authorization = not_authorized`;
5. all source locks `candidate` (not `evidence_locked`) — indexation additionally requires `evidence_locked`;
6. no route/HTML/sitemap/robots exists or is authorized.

## 12. Tests

`reference_production_tests.py` (22 proofs) PASS + `validate_scaffolding` KO/IG checks; all Pilot-01/02/03 + independence + governance regressions green; wired L0/L1/L2 CI PASS. No route, HTML, sitemap, or robots change; no claim-registry activation; no source lock.
