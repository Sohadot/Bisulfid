# Governance scaffolding — sprint `authority-dimension-impl-1`

**READ-ONLY / UNWIRED specification + validators.** Nothing here is imported by the
build, deploy, sitemap generators, robots generator, routes, the release ledger, or the
CI workflow (`.github/workflows/corpus-governance-ci.yml` is untouched). These scripts
validate only the **new** architecture artifacts created in this sprint; they do not read,
validate, or gate the legacy 14K corpus.

## Contents
- `contract_c_derive.py` — pure specification of the Contract C derived-state function
  (publication_state / indexation_state). No repository state is read. `index_candidate`
  is intentionally absent (IP-16.1).
- `contract_c_property_tests.py` — the seven canonical property tests over the exhaustive
  Cartesian product of input postures.
- `validate_scaffolding.py` — schema/consistency validator for the four new registries,
  the evidence schema + fixtures, and the Information-Gain calibration scaffold.

## Canonical property tests (seven)
Reconciles the earlier "four vs six" documentation inconsistency (see
`BISULFID_AUTHORITY_DIMENSION_ARCHITECTURE.md` IP-1, reconciled to seven):
1. **Totality** — every input combination returns exactly one valid `(publication_state, indexation_state)`.
2. **Determinism** — identical inputs always return identical outputs.
3. **Monotonic veto** — moving any upstream posture to a blocking value never raises privilege.
4. **All-green indexability** — `index_approved` only via the permitted factual or certified non-factual paths, all gates green, no hold.
5. **Hold isolation** — an indexation hold changes indexation only, never publication.
6. **New-object law** — for `legacy=none`, `reference_draft`/`ig_not_reviewed`/`ig_failed` can never be public.
7. **Legacy isolation** — `legacy_public_holding` only ever yields `(public_noindex, noindex)` (never index) and can never be assigned to a newly created route.

## Run (manual only)
```
cd scripts/governance_scaffolding
python3 contract_c_property_tests.py
python3 validate_scaffolding.py
```
