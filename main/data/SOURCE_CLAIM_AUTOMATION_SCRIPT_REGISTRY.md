# Source and Claim Automation Script Registry

**Sprint:** 5N-B  
**Status:** Active reference for source/claim guardrail automation  
**Last updated:** 2026-05-28

---

## Why this script registry exists

Sprint **5N-A** produced source registration **proposals** for **5** low-risk drafts without touching `source_registry.json` or claim registries. Before the corpus advances to **candidate source discovery** (5N-C) or **source registry execution**, Bisulfid.com requires a specialized automation layer that verifies proposal documents, evidence matrices, claim-boundary preparation, and registry locks remain **controlled, non-public, non-approved, and non-misleading**.

This registry documents the Sprint **5N-B** guardrail scripts — what they read, what they must never modify, and how they relate to the general corpus L1 runtime from Sprint **5K**.

---

## Relationship to corpus automation runtime L1

| Layer | Script | Scope |
| --- | --- | --- |
| **Corpus L1** | `scripts/corpus_validation_runtime_l1.py` | Routes, drafts, publication lock, general claims, references |
| **Source/claim guardrail L1** | `scripts/source_claim_guardrail_runtime_l1.py` | Source proposals, evidence requirements, claim-boundary prep, registry locks |

Both runtimes are **read-only**, **stdlib-only**, and **merge-blocking when wired to CI**. Operators should run **both** before source registration or claim registry work.

---

## Script inventory

### Runtime orchestrator (source/claim guardrail L1)

| Script | Purpose |
| --- | --- |
| `scripts/source_claim_guardrail_runtime_l1.py` | Orchestrates all five source/claim guardrail validators; prints PASS/FAIL summary |

### Source proposal validators

| Script | Purpose |
| --- | --- |
| `scripts/validate_source_registration_proposals_l1.py` | Validates Sprint 5N-A proposal files, matrix posture, and forbidden approval/lock language |

### Source evidence validators

| Script | Purpose |
| --- | --- |
| `scripts/validate_source_evidence_requirements_l1.py` | Validates evidence requirement matrix rows, authority boundaries, and linked proposal posture |

### Claim boundary validators

| Script | Purpose |
| --- | --- |
| `scripts/validate_claim_boundary_preparation_l1.py` | Validates Sprint 5M medium-risk claim-boundary prep (20 drafts) |

### Source registry lock validator

| Script | Purpose |
| --- | --- |
| `scripts/validate_source_registry_lock_l1.py` | Validates `source_registry.json` inactive posture and proposal consistency |

### Claim registry lock validator

| Script | Purpose |
| --- | --- |
| `scripts/validate_claim_registry_lock_l1.py` | Validates inactive claim registries, no approved claims, and no implied approval in governance docs |

---

## Per-script specification

### `source_claim_guardrail_runtime_l1.py`

| Field | Value |
| --- | --- |
| **Reads** | Invokes guardrail validators only |
| **Must not modify** | Any repository file |
| **Read-only** | Yes |
| **Dependencies** | Python standard library only |
| **Network** | Not required |
| **Can block merge** | Yes — when run in CI (future); locally advisory until wired |
| **Can block publication** | Yes — intended pre-source-registration gate |
| **Human review** | Operator must review console output and validation report |

---

### `validate_source_registration_proposals_l1.py`

| Field | Value |
| --- | --- |
| **Reads** | `main/data/SOURCE_REGISTRATION_PROPOSAL_WAVE_1_REPORT.md`, `SOURCE_REGISTRATION_PROPOSAL_MATRIX_WAVE_1.md`, `SOURCE_EVIDENCE_REQUIREMENT_MATRIX_WAVE_1.md`, `SOURCE_REGISTRATION_RISK_REVIEW_WAVE_1.md`, `SOURCE_REGISTRATION_NEXT_ACTIONS_WAVE_1.md` |
| **Must not modify** | Proposal files, registries, routes, content pages |
| **Read-only** | Yes |
| **Dependencies** | Python standard library only |
| **Can block merge** | Yes — proposal posture violations |
| **Can block publication** | Yes — false approval/lock language |
| **Human review** | Required for warnings on candidate vs verified language |

**Checks:** Files exist; **5** proposal matrix rows; `source registry entry allowed now: no`; `claim approval allowed now: no`; `publication-ready: no`; no raw URLs; no bibliographic fabrication; no source-lock/publication-ready claims; candidate families distinguished from registry rows; registry unchanged posture.

---

### `validate_source_evidence_requirements_l1.py`

| Field | Value |
| --- | --- |
| **Reads** | `main/data/SOURCE_EVIDENCE_REQUIREMENT_MATRIX_WAVE_1.md`, `SOURCE_REGISTRATION_PROPOSAL_MATRIX_WAVE_1.md` |
| **Must not modify** | Evidence or proposal matrices, registries, content |
| **Read-only** | Yes |
| **Dependencies** | Python standard library only |
| **Can block merge** | Yes — authority boundary violations |
| **Can block publication** | Yes — doctrine-only or teaching-as-authority drift |
| **Human review** | Required for dictionary/teaching tier warnings |

**Checks:** Matrix exists; **5** evidence rows; acceptable/unacceptable classes present; internal doctrine not sole authority; teaching not formal authority; dictionary not chemical authority; formal authority preserved where required; linked proposal `publication-ready: no`.

---

### `validate_claim_boundary_preparation_l1.py`

| Field | Value |
| --- | --- |
| **Reads** | `main/data/DRAFT_WAVE_1_MEDIUM_RISK_CLAIM_BOUNDARY_PREP.md` |
| **Must not modify** | Prep file, claim registries, content |
| **Read-only** | Yes |
| **Dependencies** | Python standard library only |
| **Can block merge** | Yes — premature claim/source mapping flags |
| **Can block publication** | Yes — implied claim approval |
| **Human review** | Required for blocked-claim-type completeness |

**Checks:** Prep file exists; **20** medium-risk rows; `claim registration allowed now: no`; `publication-ready: no`; `source mapping allowed now: no`; blocked claim types documented; no claim approval language; no registry modification claims.

---

### `validate_source_registry_lock_l1.py`

| Field | Value |
| --- | --- |
| **Reads** | `main/data/sources/source_registry.json`, proposal/guardrail reports |
| **Must not modify** | `source_registry.json`, any registry or content file |
| **Read-only** | Yes |
| **Dependencies** | Python standard library only |
| **Can block merge** | Yes — verified/approved source status |
| **Can block publication** | Yes — registry activation without charter |
| **Human review** | Required before any registry edit sprint |

**Checks:** Registry status **inactive**; no verified/approved/locked sources; governed by SOURCE_POLICY; proposal docs do not contradict unchanged registry posture.

---

### `validate_claim_registry_lock_l1.py`

| Field | Value |
| --- | --- |
| **Reads** | `main/data/claims/*.json`, `main/data/routes.json`, proposal and prep documents |
| **Must not modify** | Claim registries, routes, content |
| **Read-only** | Yes |
| **Dependencies** | Python standard library only |
| **Can block merge** | Yes — approved claims or implied approval |
| **Can block publication** | Yes — claim gate bypass |
| **Human review** | Required before claim registry activation |

**Checks:** All claim registries **inactive**; **0** approved claims; no `claim approval allowed now: yes`; negation-aware source-locking scan on draft content; `[SOURCE REQUIRED]` unresolved posture warnings.

---

## Dependency status

| Dependency | Status |
| --- | --- |
| Python standard library | **Only** allowed dependency |
| External packages | **None** |
| Network access | **Not required** |
| GitHub Actions / workflows | **Not created in this sprint** |

---

## Merge-blocking and publication-blocking role

| Gate | Guardrail scripts |
| --- | --- |
| **Pre-merge (future CI)** | Full guardrail runtime must PASS before source/claim governance PRs merge |
| **Pre-source-registration** | Proposal + evidence + registry lock validators must PASS |
| **Pre-claim-activation** | Claim boundary + claim registry lock validators must PASS |
| **Pre-publication** | Guardrail runtime + corpus L1 runtime must both PASS |

Warnings are **non-blocking** unless elevated by human charter.

---

## Future L2 / L3 / L4 source automation layers

| Layer | Planned scope |
| --- | --- |
| **L2** | Candidate source discovery manifest validation (named candidates, no registry writes) |
| **L3** | Source registry execution validation (chartered row additions, marker mapping manifest) |
| **L4** | Claim registry activation validation (approved claim boundaries, registry linkage) |

Sprint **5N-B** establishes **L1 guardrails only**. No L2+ scripts were created.

---

## Human review requirement

Automation verifies **document posture and registry locks**. It does **not**:

- Approve sources or claims
- Select candidate bibliographic entries
- Remove `[SOURCE REQUIRED]` markers
- Authorize publication

Human governance charter remains mandatory at every transition: proposal → discovery → registry entry → claim activation → publication.

---

*Sprint 5N-B — Source and Claim Automation Script Registry*
