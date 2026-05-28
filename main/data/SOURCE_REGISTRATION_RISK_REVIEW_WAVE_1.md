# Source Registration Risk Review — Wave 1

**Sprint:** 5N-A  
**Scope:** 5 selected drafts from Sprint 5M cohort-A  
**Date:** 2026-05-27

---

## Source proposal risk summary

| Risk dimension | Level | Notes |
| --- | --- | --- |
| Overall proposal sprint risk | **Low** | Report-only; no registry or content edits |
| Premature registration risk | **Medium** (if ignored) | Proposals must not be read as permission to register |
| Weak-source risk | **Medium** | Dictionary/teaching tiers can drift into claims |
| Formal-authority confusion | **Low–Medium** | Mineral/compound pages need nomenclature boundaries |
| Multilingual equivalence risk | **Low** (this wave) | No bridge/crosswalk drafts selected |
| Document-language misread | **Low** | No procurement/compliance pages selected |
| Publication accident risk | **Low** | All routes remain `planned` / non-indexable |

This sprint **reduces** future accident risk by documenting evidence standards before any registry row is written.

---

## Risk per selected draft

### `sulfur_element_term_record`

| Factor | Assessment |
| --- | --- |
| Proposal risk | **Low** |
| Registration risk if rushed | **Medium** — element identity lines can absorb safety or market framing if sources are weak |
| Primary guard | Use element-record tier only; teaching sources supporting, not sole authority |
| Claim posture | `terminology_claim_candidate_later` only |

### `de_core_biogenic_lang`

| Factor | Assessment |
| --- | --- |
| Proposal risk | **Low–Medium** |
| Registration risk if rushed | **Medium** — biogenic vocabulary can drift into climate/emissions statistics |
| Primary guard | Lexical/environmental teaching scope only; policy extension before registry row |
| Claim posture | `terminology_claim_candidate_later`; block emissions/market language |

### `copper_sulfides_language`

| Factor | Assessment |
| --- | --- |
| Proposal risk | **Low–Medium** |
| Registration risk if rushed | **Medium** — mineral naming can drift into ore grade, mining, or procurement claims |
| Primary guard | Nomenclature + dictionary tier; formal authority for systematic names only |
| Claim posture | `terminology_claim_candidate_later`; DE mirror deferred |

### `de_core_fes`

| Factor | Assessment |
| --- | --- |
| Proposal risk | **Low–Medium** |
| Registration risk if rushed | **Medium** — pyrite and iron sulfide naming can attract commodity/market language |
| Primary guard | DE lexical/mineral naming only; reject production or procurement sources |
| Claim posture | `terminology_claim_candidate_later` |

### `de_core_mos2`

| Factor | Assessment |
| --- | --- |
| Proposal risk | **Low** |
| Registration risk if rushed | **Low–Medium** — specialist compound naming can drift into lubricant market claims |
| Primary guard | Material naming dictionary tier; block application-performance framing |
| Claim posture | `terminology_claim_candidate_later` |

---

## Risk of premature source registration

Registering sources before discovery and human review would:

- Imply **verified** status while registry is **inactive**
- Satisfy markers without evidence audit
- Create false **source-lock** narrative for downstream publication
- Bypass SOURCE_POLICY category and authority checks
- Pre-empt claim-boundary work on related medium-risk drafts

**Mitigation:** All matrix rows state `source registry entry allowed now: no`.

---

## Risk of weak sources

| Weak source type | Failure mode |
| --- | --- |
| AI summaries / uncited web pages | Unverifiable terminology claims |
| Market or industry reports | Economic/procurement drift |
| Safety SDS sheets | Handling/medical claim drift |
| Generic Wikipedia-tier pages | Unstable authority; editorial drift |
| Blog or forum posts | No governance tier |

**Mitigation:** Evidence matrix lists acceptable and unacceptable source classes per draft.

---

## Risk of treating teaching sources as formal authority

Academic teaching references are **useful** for `sulfur_element_term_record`, `copper_sulfides_language`, `de_core_fes`, and `de_core_mos2` but must not:

- Replace IUPAC or formal nomenclature where systematic names are asserted
- Become sole authority for element identity records
- Justify safety, toxicology, or handling statements

Teaching tier = **supporting evidence only** unless SOURCE_POLICY explicitly elevates a teaching row.

---

## Risk of treating dictionaries as chemical authority

Dictionaries and lexical authorities support **usage and naming** but must not:

- Prove chemical reactivity, safety, or medical effects
- Validate market classifications or trade designations
- Establish universal equivalence across languages

For DE drafts (`de_core_biogenic_lang`, `de_core_fes`, `de_core_mos2`), DE lexical tier is required but bounded to **naming and usage**, not compliance verdicts.

---

## Risk of treating multilingual equivalents as universal equivalence

**Not in this wave's selection** — bridge and crosswalk drafts were deferred. If future sprints register multilingual sources:

- Equivalence must be **scoped per term pair**
- DE suffix rules must not generalize to all EN `-ide` mappings
- Glossary chamber rows need row-level mapping, not blanket dictionary approval

---

## Risk of treating document-language pages as legal/compliance advice

None of the **5** selected drafts are procurement, trade, or compliance document-language pages. If similar pages enter later waves:

- Industry document-language references describe **usage in documents**, not legal advice
- Registration must not imply regulatory compliance endorsement

---

## Risk of using external sources without source policy alignment

| Gap | Risk |
| --- | --- |
| DE lexical path underspecified | Wrong category assignment in registry |
| Biogenic tier missing | `de_core_biogenic_lang` registered under wrong family |
| Candidate rows unverified | Seeded registry rows mistaken for approved sources |
| No marker-to-row manifest | Partial marker satisfaction |

**Mitigation:** Policy extension flagged where needed; discovery sprint before registry execution.

---

## Why source registration is still not allowed now

1. Registry status is **inactive**
2. No candidate sources have been discovered or human-reviewed for these **5** drafts
3. Marker-to-row mapping manifest does not exist
4. SOURCE_POLICY gaps remain (DE lexical, biogenic tier)
5. Sprint charter is **proposal-only**
6. Human governance charter for registry edits has not been executed

---

## Why no claim approval is allowed now

1. `terminology_claims.json` remains **inactive**
2. **0** claims may be `approved` under current governance
3. Evidence has not been collected or verified
4. Medium-risk cohort (**20** drafts) still awaits 5N-B claim-boundary report
5. Proposals assign `terminology_claim_candidate_later` at most

---

## Why publication remains blocked

| Blocker | Status |
| --- | --- |
| Unresolved `[SOURCE REQUIRED]` markers | **Yes** — all 5 drafts |
| Source registry inactive | **Yes** |
| Route status `planned` | **Yes** — all 126 routes |
| `indexable: false` | **Yes** |
| `in_sitemap: false` | **Yes** |
| Internal link wiring | **Not done** |
| Quality Gate / sovereign launch threshold | **Not met** (126 / 500) |
| Publication-ready drafts | **0** |

---

*Sprint 5N-A — Source Registration Risk Review Wave 1*
