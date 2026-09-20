# IG Governance Ratification — MoS₂ Reference Object

**Date:** 2026-09-20 · **Baseline:** commit `9b3746d8ad` (Reference Production 01) · **Policy:** `IG-GOVERNANCE 1.0.0`

Ratifies a machine-discoverable, deterministic, **non-numeric** Information-Gain (IG) decision authority and resolves the `KO-MOS2-SCIENTIFIC-001` IG posture under it. **Not** a publication/route/acquisition/migration sprint. No web, no new sources, no band gap, no route/HTML/sitemap/robots/release-ledger/legacy change, no claim activation, no source lock, no PR. This report **supersedes §7 of `REFERENCE_PRODUCTION_01_MOS2.md`** (the "no ratified IG-pass authority yet" note).

## 1. Baseline confirmed
`KO-MOS2-SCIENTIFIC-001` and `PC-MOS2-SCIENTIFIC-001` exist; the PC IG posture was `ig_not_reviewed`; Contract-C recomputed to `(not_public, noindex)`; the three RP01 calibration relationships were present; no RP01 public route exists. No material discrepancy.

## 2. Ratified authority (machine-discoverable, versioned)
- **Policy:** `main/data/information_gain/ig_governance_policy.json` — `policy_id: IG-GOVERNANCE`, `version: 1.0.0`, `status: ratified`.
- **Engine:** `scripts/governance_scaffolding/information_gain_gate.py:evaluate` — deterministic, non-numeric, fail-closed. The ONLY sanctioned way to advance an IG posture.

## 3. Four governed route-distinctness classifications
| Classification | Route-eligible | Posture | Meaning |
|---|---|---|---|
| `valid_domain_specific_reference` | **yes** | `ig_reviewed_pass` | distinct governed knowledge **and** a distinct reference task (positive independent value) |
| `near_duplicate` | no | `ig_reviewed_no_new_route` | same reference task as an existing surface → no NEW URL |
| `module_relationship` | no | `ig_reviewed_no_new_route` | endpoints are modules of ONE object → not sibling URLs |
| `unresolved` | no | `ig_review_required` | unresolved on governed signals → human review (fail-closed) |

## 4. Multi-signal & non-numeric
Decision signals: evidence/claim/source overlap, relationship/geography-jurisdiction/temporal difference, module-section overlap, user-task difference. Values are **categorical** (disjoint/low/partial/high/na), never numbers. **No threshold/weight/cutoff/score** is defined or permitted (validator forbids those substrings as keys anywhere). `textual_similarity` is `diagnostic_only`: it never decides a classification and never upgrades a same-task surface. **"Not a duplicate" alone is not independent reference value.**

## 5. Deterministic, fail-closed evaluation
`evaluate()` → `classification / posture / route_eligible / reasons / signals_considered / unresolved_signals / endpoints / policy_version`. Missing/unknown required signals, self-comparison (A==B), or ambiguous/contradictory signals → `unresolved` (`ig_review_required`), never a pass. Identical inputs → identical output.

## 6. `ig_reviewed_pass` — positive-only, necessary-not-sufficient
Granted ONLY for a positive independent-reference classification (`valid_domain_specific_reference` / `valid_sibling` / `valid_localization`) with **no** unresolved signals. `near_duplicate`, `module_relationship`, and `unresolved` are never eligible for a sibling-route pass. A pass is **necessary but not sufficient** for a URL — every other Contract-C gate still applies.

## 7. Gate separation
IG classifies route-distinctness and object validity **only**. It may not mutate evidence/claim/independence/admissibility/source-lock/validation/Contract-C/release/indexation, routes, sitemap, robots, the release ledger, or legacy visibility. `contract_c_derive.py` stays canonical; IG supplies one input posture, which the engine normalizes.

## 8. RP01 pairs re-evaluated
- **Pair 1** (`KO-MOS2-SCIENTIFIC-001` vs `de_core_mos2`) → `valid_domain_specific_reference` → `ig_reviewed_pass` (route-eligible).
- **Pair 2** (KO vs legacy `/molybdenum-disulfide/`) → `near_duplicate` → `ig_reviewed_no_new_route`.
- **Pair 3** (`#formula` vs `#structure` modules) → `module_relationship` → `ig_reviewed_no_new_route` (supersedes the RP01 near_duplicate seed label).

`calibration_pairs.json` upgraded to **governed fixtures (v0.3.0)**: each normative pair carries `expected_classification / expected_posture / expected_route_eligible / fixture_kind / policy_version` and the gate MUST reproduce it.

## 9. KO IG posture resolved — object validity ≠ new-route distinctness
`KO-MOS2-SCIENTIFIC-001.ig_resolution`:
- `object_informational_validity = object_valid_governed` — the object holds distinct governed knowledge (vs the German lexical object); worth governing and retrieving.
- `new_route_distinctness = no_new_route_warranted` (`near_duplicate` vs the legacy same-task route) — it does **not** earn a new independent URL.

Only new-route distinctness feeds the Contract-C `information_gain_posture` (`ig_reviewed_no_new_route`).

## 10. Contract-C recomputed, still closed
`contract_c_derive.py` normalizes governed postures (`ig_reviewed_pass→ig_passed`, `ig_reviewed_no_new_route→ig_failed`, `ig_review_required→ig_not_reviewed`) and gates route eligibility with a **fail-closed positive allow-list** (any unknown IG value denies a URL). Derived Contract-C for the KO/PC = **(not_public, noindex)** — governance `reference_draft` alone denies a URL; every other blocker also stands. PC disposition → `governed_reference_no_new_route`.

## 11. One-Fact-One-Owner held
The IG layer carries no scientific values (no `source_literal`/`normalized_value`/measurements). Evidence owns literals; claims own propositions; the KO owns composition/scope; IG owns route-distinctness classification only.

## 12. Contract-C canonical suite unaffected
The exhaustive `IG` domain is unchanged, so `contract_c_property_tests.py` (23040 combinations) still passes all 7 canonical properties. Governed postures are handled by normalization + allow-list.

## 13. Tests
- `ig_governance_tests.py` — **25 proofs** PASS.
- `validate_scaffolding.py` — `validate_information_gain_governance()` added; **759 checks** PASS.
- `reference_production_tests.py` — updated to the ratified posture/disposition; PASS.
- All Pilot-01/02/03 + independence + Contract-C property + governance regressions PASS.
- Wired **L0/L1/L2 CI** PASS.

## 14. Scope guard (verified)
No route/HTML/sitemap/robots/release-ledger/legacy change; no claim activation; no source lock; Pilot 01/02/03 claim outcomes and all evidence values unchanged; the legacy 14K corpus is not made authoritative over the Knowledge Object model.

## 15. Files
New: `ig_governance_policy.json`, `information_gain_gate.py`, `ig_governance_tests.py`, this report.
Modified: `calibration_pairs.json`, `knowledge_object_registry.json`, `PC-MOS2-SCIENTIFIC-001.json`, `contract_c_derive.py`, `validate_scaffolding.py`, `reference_production_tests.py`, `DECISION_LOG.md`.

## 16. Blockers before ANY MoS₂ URL (unchanged, IG resolved)
IG is now reviewed but classifies the object as `no_new_route_warranted` vs the legacy same-task route; a NEW URL would require `ig_reviewed_pass` (a positive independent-reference classification). Plus: claims non-operational (`claim_pending`); `not_validated`; `not_authorized`; all source locks `candidate` (not `evidence_locked`); no route/HTML/sitemap/robots exists or is authorized.

## 17. Stop
IG authority ratified; nothing published. No public route. **No Reference Production 02.**
