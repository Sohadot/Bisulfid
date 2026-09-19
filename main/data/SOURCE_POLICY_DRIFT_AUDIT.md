# SOURCE_POLICY Drift Audit

**Sprint:** pilot-01-evidence-admission-closure · **Date:** 2026-09-19
**Audited document:** `doctrine/SOURCE_POLICY.md` (the original, human-readable policy)
**Audited against:** `main/data/source_admissibility_policy.json`, `main/data/sources/source_registry.json`, `main/data/source_use_qualification_registry.json`, `main/data/evidence/evidence_schema.json`, `main/data/evidence_admission_policy.json`, `BISULFID_AUTHORITY_DIMENSION_ARCHITECTURE.md` (Contract C).

## Purpose & scope

This is a **read-mostly supersession audit**, not a rewrite. `SOURCE_POLICY.md` remains the doctrinal north star; several of its *mechanisms* have since been elaborated into machine-governed registries. Below, each drift point states which document is now authoritative for that mechanism. **Minimum sync only**: the sole change to `SOURCE_POLICY.md` itself is a short "Supersession & Layering" pointer appended at its end. No core rule is deleted or weakened.

## Still authoritative and unchanged (reaffirmed)

- **Core rule** — "No source entry = no published claim." Still binding; **strengthened**, not relaxed: a source entry is now necessary but not sufficient — admissibility (`admissible()`) and Contract C add further independent gates.
- **AI and Tool Use** — AI text/summaries are not sources; every claim traces to the original source. Unchanged and reaffirmed (Pilot 01 used no AI/search summaries as evidence).
- **Permanently Blocked Content** — market stats without verified methodology, bisulfite-as-bisulfide, safety thresholds as advice, medical/therapeutic claims, handling instructions, dosage, competitor/acquisition targeting. Unchanged.
- **Review and Dispute** — a source later found unreliable pulls its dependent claims from publication. Unchanged; now implemented as the monotonic regression rule in `evidence_admission_policy.json`.

## Drift points (mechanism superseded / elaborated)

| # | SOURCE_POLICY.md says | Now authoritative | Nature of drift |
|---|---|---|---|
| D1 | **Approved Source Categories** as an 8-item prose list. | `source_admissibility_policy.json → ratified_source_categories` (8 `existing_confirmed` machine ids + 8 `newly_ratified`, incl. `official_trade_statistics`, `customs_nomenclature_authority`, `official_standard`, `regulatory_instrument`, …) mirrored in `source_registry.json → source_categories`. | **Elaboration.** The prose list is a human summary; the machine vocabulary is the source of truth and has grown (trade/customs/statistics/standard categories added via ratified amendments). Category **alone is never admissible** — a new hard rule not present in the prose. |
| D2 | **Source Registry Format** requires a `linked_claims` array on each source entry. | One-directional linking: claim → `supporting_evidence_ids` → evidence → `source_id`. `evidence_schema.json` **forbids** `used_by` as an editable field; back-links are **derived**, never stored. | **Superseded.** Storing `linked_claims` on sources would duplicate a derivable reverse index and invite drift. Current sources carry no `linked_claims`; they carry governed `status`, `source_lock_status`, `identity_revision`, and scoped `use_for`/`do_not_use_for`. |
| D3 | **Claim Registry**: each claim in `main/data/claims/claim_registry.json` links **directly** to a source entry. | Claim → **evidence** → source (two hops). Pilot claims are **non-operational** and deliberately kept OUT of the canonical claim registry (`claim_activation_policy.json`; `PILOT_01_claims.json.operational = false`). | **Superseded.** The direct claim→source link is replaced by claim→evidence→source so that one fact has one owner (the evidence record binds the source; the claim binds evidence). |
| D4 | **This document takes precedence … where claims intersect**, with publication implied by a registered, sourced claim. | **Contract C** derives publication/indexation from six independent postures. A verified source, an admitted evidence record, and even an approved claim **do not** imply publication. | **Elaboration.** Publication authority was decoupled from sourcing; `SOURCE_POLICY.md` governs *sourcing*, Contract C governs *publication*. No conflict — they are now orthogonal layers. |
| D5 | **Validation** by `validate_sources.py` / `validate_claims.py`, "Gate 04". | Wired CI = `.github/workflows/corpus-governance-ci.yml` (L0/L1/L2 runtimes, incl. `validate_source_registry_lock_l1.py`). The newer semantic validators (`validate_scaffolding.py`, `validate_concept_lexeme.py`, `source_admissibility.py`, pilot test suites) are **intentionally unwired** from CI while the governance layer matures. | **Naming/wiring drift.** The named scripts may not exist under those exact names; the audit records the current wired set so the doc does not imply a stale gate. |
| D6 | Source entry lifecycle implicitly binary (present ⇒ usable). | Governed lifecycle: source `status` (`seeded` → `verified` under `verification_limited`) and `source_lock_status` (`candidate` → `locked`) are **separate**; use-qualification has its own state machine (`candidate`/`reviewed`/`qualified_narrow`/`qualified`/`suspended`/`superseded`). | **Elaboration.** "Verified" is bibliographic identity only; it is not "locked", "approved", or "publishable". Pilot 01 exercises exactly this: two sources verified, none locked, one qualification promoted to `qualified_narrow`, nothing published. |

## Conclusion

No drift point is a **contradiction** of `SOURCE_POLICY.md`; every one is an **elaboration or reverse-link/normalization change** that keeps the doctrine's intent (traceability, no unsourced claims, no AI-as-source, disputes pull publication) and makes it machine-enforceable and stricter. The doctrine still wins on *what may be claimed and sourced*; the newer JSON layers own the *mechanics* of categories, linking, admission, and publication.

**Sync action taken:** a short "Supersession & Layering (2026-09-19)" pointer appended to `doctrine/SOURCE_POLICY.md`. No core rule changed.
