# Human Source Acceptance Criteria — Wave 1

**Sprint:** 5N-D  
**Date:** 2026-05-28

---

## General acceptance criteria for future source registry proposals

A candidate may be **accepted for future registry proposal drafting** only if all are true:

1. Human reviewer can name publisher, institution, database class, or dictionary edition **type** (verified externally — not invented in governance docs)
2. SOURCE_POLICY category confirmed
3. `use_for` / `do_not_use_for` scope documented before any registry row
4. Line-by-line marker mapping plan exists
5. Guardrail runtime **PASS** at proposal time
6. No safety, market, medical, procurement, or trade drift in source primary purpose
7. Route remains `planned` / non-indexable
8. **No** claim approval implied

Acceptance for **proposal drafting** ≠ registry entry ≠ marker satisfaction.

---

## Acceptance criteria for scientific database references

Accept when:

- Source is a **government or scientific database** with stable element/compound record tier
- Record scope is identity/naming only — no safety, market, or handling fields used
- Human verifies database authority and record stability
- Maps to element identity markers on `sulfur_element_term_record`

Reject when:

- Teaching site or wiki presented as database
- Record includes operational, medical, or economic fields as primary content

---

## Acceptance criteria for chemistry dictionary references

Accept when:

- Named dictionary or specialist chemistry lexicon with editorial governance
- Scope limited to **naming, spelling, variant labels** — not reactivity or applications
- Maps to mineral/compound naming markers only
- Supporting formal nomenclature tier identified separately where systematic names required

Reject when:

- General web dictionary without governance
- Dictionary used to justify ore grade, market, or application performance claims

---

## Acceptance criteria for German lexical dictionary references

Accept when:

- DE lexical authority with named publisher/class (human verified)
- Scope limited to **German naming and usage** for localized drafts
- Independent DE mapping — not EN dictionary mirror without review
- Applies to `de_core_biogenic_lang`, `de_core_fes`, `de_core_mos2`

Reject when:

- EN-only lexical source assigned to DE-only lines
- Environmental lexicon includes climate statistics or regulatory verdicts

---

## Acceptance criteria for formal nomenclature authority

Accept when:

- Source class is `chemical_nomenclature_standard` or equivalent formal tier (human verified)
- Used **only** for systematic names — supporting tier, not sole dictionary substitute
- Required where evidence matrix flags formal authority **yes**
- Applies to `copper_sulfides_language`, `de_core_fes`, `de_core_mos2`

Reject when:

- Teaching text treated as IUPAC rule source
- Nomenclature source used for mineral economics or mining claims

---

## Acceptance criteria for academic teaching sources

Accept when:

- Named university/department/program attribution (human verified)
- Category `academic_teaching_reference` with explicit scoped `use_for`
- **Supporting context only** — paired with stronger authority where formal lines exist

Reject when:

- Used as sole element identity, formal nomenclature, or DE lexical authority
- Contains handling, medical, or operational instructions

---

## Acceptance criteria for multilingual terminology sources

Accept when:

- Scoped **term-pair** evidence only
- Used for boundary/disambiguation drafts — not this wave's **5** core naming pages unless explicitly mapped

Reject when:

- Universal EN↔DE equivalence claimed from single dictionary row
- Bridge page rules generalized to all suffix mappings

**Note:** This wave's **5** drafts do not require multilingual equivalence proof except where DE localization is independent naming — not universal equivalence.

---

## Acceptance criteria for industry/document-language sources

Accept when:

- Used only on document-language drafts with explicit non-advice framing
- Describes **usage in documents** — not legal, compliance, or procurement verdicts

Reject when:

- Applied to core terminology naming pages in this wave
- Primary content is operations, legal advice, or market language

**Note:** None of the **5** selected drafts are industry document-language pages.

---

## Why teaching support cannot replace formal authority

Teaching references lack normative nomenclature status. SOURCE_POLICY forbids teaching tier alone for formal rule claims, marker removal, or route publication.

---

## Why dictionary support cannot replace chemical authority

Dictionaries document **usage and naming** — not reactivity, safety, toxicology, or market classification. Chemical authority requires appropriate database, nomenclature, or peer-reviewed tiers scoped to the claim type.

---

## Why multilingual equivalents cannot prove universal equivalence

Equivalence is **term-pair scoped**. DE localized naming requires DE lexical authority — not inference from EN dictionary rows or universal suffix rules.

---

## Why document-language support cannot become legal/compliance/procurement advice

Document-language references describe how terms appear in filings or sector docs. They do not constitute regulatory compliance, customs, export, or procurement guidance.

---

## Minimum human verification requirements

Before any future registry proposal, a human reviewer must confirm:

- Named source identity (publisher/institution/database/dictionary class)
- Edition or access stability plan (without inventing bibliographic details in governance docs)
- SOURCE_POLICY category assignment
- Marker-to-source line mapping draft
- Rejection-rule clearance
- Explicit **accept / defer / reject** decision with rationale

---

## Criteria for moving from human review to future registry proposal

| Criterion | Required |
| --- | --- |
| Human review matrix row exists (5N-D) | Yes |
| Human verification completed for named candidate | Yes |
| Acceptance criteria met for source class | Yes |
| Rejection decisions clearance | Yes |
| Policy extension merged (if flagged) | Yes for `de_core_biogenic_lang` |
| Guardrail runtime PASS | Yes |
| Registry execution sprint chartered | Yes |
| Still **no** marker removal without audit | Yes |

---

*Sprint 5N-D — Human Source Acceptance Criteria Wave 1*
