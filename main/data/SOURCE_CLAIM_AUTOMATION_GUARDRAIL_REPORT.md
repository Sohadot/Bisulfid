# Source and Claim Automation Guardrail Report

**Sprint:** 5N-B  
**Date:** 2026-05-28  
**Branch:** `claude/sprint-5n-b-source-claim-automation-guardrails`

---

## Why this sprint exists

Sprint **5N-A** prepared source registration proposals for **5** low-risk drafts. Sprint **5M** mapped **12** cohort-A drafts and prepared **20** medium-risk drafts for claim-boundary work. Before moving to candidate source discovery or registry edits, the corpus needs **specialized automation** that verifies proposals, evidence requirements, and claim-boundary documents remain controlled and non-misleading.

---

## Why source/claim automation is necessary before source_registry edits

| Risk without guardrails | Guardrail response |
| --- | --- |
| Candidate sources treated as approved | Proposal validator blocks approval language |
| Teaching sources as formal authority | Evidence validator checks authority tiers |
| Dictionaries as chemical authority | Evidence validator scopes dictionary rows |
| Premature claim approval | Claim registry lock validator |
| Registry edits without charter | Source registry lock validator |
| Marker removal / false source-lock | Claim lock + corpus draft validators |

Registry edits require human charter **and** passing guardrail runtime.

---

## Why sources are the trust root of Bisulfid.com

Every public terminology, science, safety, market, and industry claim on Bisulfid.com must trace to governed sources in `source_registry.json` under `doctrine/SOURCE_POLICY.md`. If candidate sources are mistaken for verified sources, or teaching tiers substitute for formal nomenclature authority, the **500-page sovereign launch threshold** loses audit integrity.

---

## Relationship to Sprint 5M source mapping

Sprint **5M** mapped **12** low-risk drafts and produced medium-risk claim-boundary **preparation** for **20** drafts. Guardrail validators read those artifacts and enforce `no` posture on registration, approval, and publication flags.

---

## Relationship to Sprint 5N-A source registration proposals

Sprint **5N-A** created five proposal documents for **5** selected drafts. `validate_source_registration_proposals_l1.py` and `validate_source_evidence_requirements_l1.py` directly guard those files.

---

## Relationship to Sprint 5K corpus automation runtime

Sprint **5K** established general corpus L1 validation (routes, drafts, publication lock, claims, references). Sprint **5N-B** adds a **parallel** source/claim guardrail runtime that operators run alongside corpus L1 — not as a replacement.

---

## Scripts created

| Script | Role |
| --- | --- |
| `scripts/source_claim_guardrail_runtime_l1.py` | Orchestrator |
| `scripts/validate_source_registration_proposals_l1.py` | Proposal posture |
| `scripts/validate_source_evidence_requirements_l1.py` | Evidence authority boundaries |
| `scripts/validate_claim_boundary_preparation_l1.py` | Medium-risk prep lock |
| `scripts/validate_source_registry_lock_l1.py` | Source registry lock |
| `scripts/validate_claim_registry_lock_l1.py` | Claim registry lock |

---

## What each script validates

### Proposal validator

- Five proposal files exist; matrix has **5** rows
- All rows: registry entry / claim approval / publication-ready = **no**
- No approved-source, source-lock, or URL/bibliography violations

### Evidence validator

- Five evidence rows with acceptable/unacceptable classes
- Internal doctrine not sole authority; teaching not formal authority
- Formal authority preserved for mineral/compound rows

### Claim boundary prep validator

- **20** medium-risk rows; claim registration / publication / source mapping = **no**
- Blocked claim types documented; no approval language

### Source registry lock validator

- Registry **inactive**; **14** seeded candidates; **0** verified/approved
- Proposal docs consistent with unchanged registry

### Claim registry lock validator

- **6** claim registries **inactive**; **0** approved; **14** pending_review
- No implied approval in governance docs; negation-aware source-lock scan

---

## Why no sources were added

Sprint charter: **automation and documentation only**. Guardrails verify posture; they do not register sources.

---

## Why source_registry.json was not modified

Explicit sprint rule. Registry remains **inactive** with seeded **candidate** rows only.

---

## Why no claims were approved

Claim registries remain **inactive**. Guardrails block implied approval language in governance documents.

---

## Why claim registries were not modified

Sprint **5N-B** creates validators only. No claim registry activation path was opened.

---

## Why no content pages were modified

Automation reads content for lock/ marker posture only. No draft edits were authorized.

---

## Why `[SOURCE REQUIRED]` markers remain

Guardrails treat unresolved markers as expected. Claim registry lock validator warns on drafts missing markers (e.g. `acquire` landing page — non-blocking).

---

## Why no routes were published

All **126** routes remain `planned`, non-indexable, out of sitemap/navigation. Corpus L1 publication lock **PASS**.

---

## How this protects the future 500-page launch threshold

| Protection | Mechanism |
| --- | --- |
| Proposal integrity | Automated checks before discovery/registration sprints |
| Registry lock | Verified-source drift blocked at validation time |
| Claim lock | No silent approval before registry activation |
| Scale discipline | Repeatable guardrail runtime for every governance wave |

**500 governed pages** require verified sources and approved claim boundaries — not proposal documents alone.

---

## How this protects future 1,000+ / 3,000+ scaling

Guardrail scripts are **additive** and **composable**. Future L2–L4 layers (discovery manifests, registry execution, claim activation) can plug into the same runtime without weakening L1 locks. Human review remains at every layer transition.

---

## Recommended next sprint

**Sprint 5N-C — Candidate source discovery wave 1** for the **5** proposed drafts, running guardrail + corpus L1 validators before and after. Claim-boundary **registration report** for **20** medium-risk drafts may proceed in parallel once guardrails are on main.

See `SOURCE_CLAIM_AUTOMATION_NEXT_ACTIONS.md`.

---

*Sprint 5N-B — Source and Claim Automation Guardrail Report*
