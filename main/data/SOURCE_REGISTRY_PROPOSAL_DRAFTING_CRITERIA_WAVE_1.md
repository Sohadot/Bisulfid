# Source Registry Proposal Drafting Criteria — Wave 1

**Sprint:** 5N-F  
**Date:** 2026-05-29

---

## Criteria for source registry proposal drafting

All must be true before a proposal **drafting** sprint (not execution):

1. External verification complete (5N-E) with `source registry proposal allowed next` = **yes** or readiness status `proposal_readiness_conditional`
2. Proposal readiness documented (5N-F)
3. Human has **named** acceptable source candidate (outside repo — not invented bibliographic lines in governance docs)
4. Authority class aligns with draft page role
5. Acceptance criteria in `HUMAN_SOURCE_ACCEPTANCE_CRITERIA_WAVE_1.md` met for candidate class
6. Rejection decisions clearance in `HUMAN_SOURCE_REJECTION_DECISIONS_WAVE_1.md`
7. Guardrail runtime **PASS**
8. Proposal drafting sprint chartered
9. **No** marker removal in proposal drafting sprint

---

## Criteria for a named source candidate

A named source candidate must:

- Be a **specific** publisher, database, or lexicon **class** human-verified externally
- Fit an approved `SOURCE_POLICY.md` category
- Map to scoped draft markers — not corpus-wide authority
- Exclude safety, medical, procurement, market, and AI-summary sources
- Be documented in intake/proposal sprint without raw URLs unless SOURCE_POLICY explicitly allows (it does not for these governance docs)

**Not sufficient:** evidence family alone (e.g., “chemistry dictionary reference” without named candidate).

---

## Criteria for human external verification

Required when:

- `human verification required` = **yes** on readiness matrix
- `named source candidate present` = **no**
- Applies to **both** target drafts in 5N-F

Human must confirm: candidate identity, category fit, scope boundary, marker mapping, and rejection-rule clearance.

---

## Criteria for authority-class alignment

| Draft | Required authority | Misalignment examples |
| --- | --- | --- |
| `de_core_mos2` | `chemistry_dictionary_authority` | Lubricant market source; teaching as sole authority; EN dictionary for DE page without DE verification |
| `sulfur_element_term_record` | `scientific_database_authority` | Dictionary as element identity; teaching as sole tier; database used for non-element claims |

---

## Criteria for rejecting proposal drafting

Reject proposal drafting when:

- Readiness status is `needs_scientific_database_candidate_first`, `blocked_from_proposal_now`, or `not_ready_for_registry_proposal`
- No named human-verified candidate
- Fails any rejection decision in `HUMAN_SOURCE_REJECTION_DECISIONS_WAVE_1.md`
- Source policy extension required but not merged
- Guardrail runtime **FAIL**

**Current:** `sulfur_element_term_record` — reject proposal drafting until database candidate named.

---

## Criteria for separating proposal drafting from registry execution

| Activity | Proposal drafting sprint | Registry execution sprint |
| --- | --- | --- |
| Output | Proposal documents with scoped linkage plan | Rows in `source_registry.json` |
| Registry edits | **No** | **Yes** — chartered only |
| Bibliographic details | Human-verified; no fabrication | Full registry fields per SOURCE_POLICY |
| Charter | Proposal sprint charter | Separate execution charter + guardrail **PASS** |
| Markers | **No** removal | **No** auto-removal |

---

## Criteria for preserving claim gates

- Claim registries remain **inactive** through proposal readiness and drafting
- **0** approved claims until verified source linkage exists
- Proposal documents must not imply claim approval
- `terminology_claims.json` not modified in readiness or drafting sprints

---

## Criteria for preserving publication blockers

- Routes remain `planned`
- Drafts remain `non_public`, `indexable: false`, `in_sitemap: false`
- No page stated publication-ready
- Quality Gate and editorial signoff not satisfied

---

## Criteria for using guardrail runtime before and after proposal drafting

| Event | Action |
| --- | --- |
| Before readiness/proposal/execution doc merge | Run guardrail + corpus L1 |
| After governance doc updates | Re-run guardrail |
| Before proposal drafting sprint merge | Guardrail **PASS** |
| Before any registry edit | Guardrail **PASS** + human execution charter |

---

## Criteria for allowing a future separate execution sprint

All must be true:

1. Proposal draft complete for scoped draft(s)
2. Human governance charter for registry execution approved
3. Named candidate human-verified with full bibliographic details (outside governance-doc fabrication rule)
4. Guardrail + claim lock validators **PASS**
5. Maximum **1–3** registry rows per execution batch
6. Marker satisfaction audit scheduled — no auto-removal
7. **No** route publication in execution sprint

---

*Sprint 5N-F — Source Registry Proposal Drafting Criteria Wave 1*
