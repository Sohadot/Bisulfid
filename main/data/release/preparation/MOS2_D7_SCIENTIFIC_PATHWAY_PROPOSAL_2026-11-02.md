# D7 — Proposed scoped documentary pathway for MoS2 science

**PREPARATORY ONLY — NOT ADOPTED — NO POLICY CHANGE**  
Prepared: 2026-11-02. PR #120, Draft. Owner: Sohadot.

## Present policy and mismatch

The adopted `DOCUMENTARY-VERIFICATION@1.0.0` currently lists `terminology` as its only eligible claim type. The three MoS2 pilot scientific claims have no formal approval status and no claim type. The KO also has not explicitly recorded the exact exclusion categories `chemical_safety` and `medical`. The declared low-risk classification in the publication candidate is preliminary, so `D7 = undetermined` remains correct. No policy, KO or claim record is changed by this proposal.

## Candidate scope for a future, separately reviewed amendment

Rather than admitting every scientific claim automatically, evaluate three narrow *candidate* categories:

| Proposed type, not presently valid | Permitted claim content | Proposed MoS2 association |
|---|---|---|
| `chemical_identity_descriptive` | Specific compound identity/formula without broader operational interpretation | `CLM-MOS2-FORMULA` |
| `crystal_structure_descriptive` | Attributed bulk structure, polytype and lattice symmetry, preserving source roles and boundaries | `CLM-MOS2-STRUCTURE-2H` |
| `crystallographic_parameter_source_specific` | Source-specific measured structural quantities with material form, polytype, units, uncertainty and originating-study attribution | `CLM-MOS2-LATTICE-A-2H` |

These are **proposed labels only**, not approved `claim_type` values. A simple addition to `eligible_claim_types` is insufficient; the evaluator must require the stated fields and qualified sources for each type. Measurement descriptions must remain explicitly scientific, attributed and non-operational. Unknown or out-of-scope material remains ineligible.

## Required conditions if a future amendment is considered

1. D1 must establish approval of the **exact** individual statement and its boundaries. Pilot evidence sufficiency is not a claim status.
2. D2 and D3 must establish valid source-use admission and claim-to-render mapping for every cited statement and interpreted value.
3. D4 L1–L5 must pass for every bound source on actual capture evidence, including separate valid capture dates for L3. A publisher access failure is not a successful source capture.
4. D5 must disclose unresolved questions and contradictions. D6 must establish reference quality and distinctiveness.
5. The KO must genuinely exclude the specified higher-risk content classes, including the exact required category keys. Adding keys solely to silence the checker is not acceptable.
6. Source lineage must not be double-counted: a COD record and its originating paper are manifestations of one scientific work. The Huang thesis supports history but is not an independent determination from the related 1983 study.
7. 2H bulk measurements cannot be generalized to 1T, 3R or single layers; reported uncertainty is not a universal guarantee. RSC review values remain secondary context rather than additional independent experiments.
8. Every author-controlled field, including SEO and structured data, stays within the admitted source scope. Existing lexical screening must be supplemented with machine-checkable scientific subtype and scope checks.
9. Documentary verification must remain labelled as automated verification, never as independent human review or an L6 signature. All owner and release decisions remain separate.

## Proposed negative regression coverage (not executed here)

- A scientific-type label without required source, material form or polytype scope fails.
- An unattributed or out-of-form lattice value fails.
- Double-counting the same originating work fails.
- An unsupported operational, healthcare, regulatory or performance claim is ineligible for this pathway.
- A missing D1 approval keeps whole-KO verification false even if D7 classification can be assessed in a fixture.
- A missing publisher capture or later retrieval keeps D4 false even if D1 and D7 are satisfied in an isolated fixture.
- A valid documentary result does not activate claims, release content or alter Contract C.
- Existing terminology-KO decisions and protections remain unchanged.

A policy amendment, if later expressly authorized, should have a new version, explicit adoption act and regression proof. **Do not modify `documentary_verification_policy.json`, `documentary_verification.py`, `PILOT_03_claims.json` or `owner_acts.json` merely to record this preparation.**

## Current blockers and next evidence work

D2, D3, D5 and D6 pass on current project records. D1 is pending individual approval; D7 remains undetermined; D4 remains pending for NIST's later capture and the RSC, 1923, 1983 and Huang source-access gaps. The next honest NIST recapture is 2026-11-03 UTC or later. Source-access restrictions cannot be bypassed by a policy amendment.

**Decision status:** all proposed claim types, policy changes, scientific approvals, owner acts and publication decisions remain UNDECIDED and NOT AUTHORIZED. The existing reference remains `not_verified`, `not_public/noindex`. 

**Related packet:** `main/data/release/preparation/MOS2_D1_CLAIM_REVIEW_CANDIDATE_2026-11-02.md`.

**Repository basis:** `main/data/release/documentary_verification_policy.json`, `scripts/release/documentary_verification.py`, `main/data/pilots/PILOT_03_claims.json`, `main/data/knowledge_objects/knowledge_object_registry.json`, `main/data/claim_activation_policy.json`, and current source-lock checklists.
