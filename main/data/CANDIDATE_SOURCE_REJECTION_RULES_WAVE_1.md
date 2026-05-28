# Candidate Source Rejection Rules — Wave 1

**Sprint:** 5N-C  
**Date:** 2026-05-28

---

## General rejection rules for weak candidate sources

Reject any candidate that:

- Lacks a nameable publisher, database authority, dictionary edition class, or institutional owner
- Is AI-generated, uncited, crowd-edited without governance, or unstable over time
- Cannot be assigned an approved SOURCE_POLICY category
- Would satisfy only part of a draft's markers while implying full source-lock
- Primary purpose is persuasion, marketing, investment, or uncited aggregation
- Conflicts with doctrine or existing seeded candidate rows without human review

---

## Rejection rules for teaching sources

Reject teaching references that:

- Are used as **sole** formal nomenclature or element identity authority
- Contain safety handling, medical, exposure, or operational instructions
- Present suffix rules or multilingual equivalences as universal law
- Lack named university/department/program attribution for registry consideration
- Would justify removing `[SOURCE REQUIRED]` markers without stronger paired authority

**Allowed posture:** supporting terminology context only, scoped to draft markers, candidate tier until human review.

---

## Rejection rules for dictionaries

Reject dictionary sources that:

- Are used to prove chemical reactivity, safety, toxicology, or medical effects
- Are used for market classifications, trade designations, or procurement language
- Are English-only sources assigned to DE-only naming lines without DE lexical authority
- Are general-purpose web dictionaries without stable editorial governance
- Conflate mineral **names** with ore **economics** or mining market data

**Allowed posture:** lexical usage, spelling, and naming-surface support within scoped lines.

---

## Rejection rules for multilingual equivalents

Reject multilingual sources that:

- Establish universal EN↔DE equivalence without term-pair scoping
- Treat bridge or suffix pages as IUPAC or DIN rule sources
- Import EN dictionary authority onto DE mirror drafts without independent DE mapping
- Generalize one compound mapping to a family-wide transformation rule

**Note:** This wave's **5** drafts are not bridge/crosswalk pages; rules apply if candidates drift into equivalence claims.

---

## Rejection rules for industry/document-language references

Reject industry or document-language sources that:

- Provide process design, yields, production statistics, or plant operations advice
- Read as legal, customs, export-control, or regulatory compliance verdicts
- Frame procurement, pricing, or acquisition targeting language
- Substitute for terminology dictionaries on core naming pages

**Note:** None of the **5** selected drafts are industrial/compliance document-language pages; reject if candidates drift into that framing.

---

## Rejection rules for safety/market/procurement/medical sources

Reject candidates whose primary content is:

- Safety data sheets, handling instructions, exposure thresholds, or emergency advice
- Market research, CAGR, market-share, pricing, or investment analysis
- Medical or therapeutic claims
- Procurement, assay, ore-grade, or commodity trading language
- Production/trade statistics presented as terminology authority

Applies especially to `de_core_fes` (pyrite/commodity drift), `de_core_mos2` (lubricant market drift), and `de_core_biogenic_lang` (climate/emissions drift).

---

## Rejection rules for AI-generated or unsourced content

Reject:

- AI summaries presented as sources
- Uncited blog posts, forums, wikis without editorial governance charter
- Generated bibliographic metadata without verification
- "Tool output" substituted for publisher-attributed records

Aligns with SOURCE_POLICY blocked uses and Sprint **5N-B** guardrails.

---

## Rejection rules for pages that provide raw claims without authority

Reject candidate pages that:

- Assert identity, nomenclature, or equivalence sentences without citable authority structure
- Mix terminology lines with operational, legal, or economic claims
- Cannot be mapped line-by-line to draft `[SOURCE REQUIRED]` markers
- Would require removing markers before registry row and human audit exist

---

## Per-draft rejection notes

| route_id | Reject especially |
| --- | --- |
| `sulfur_element_term_record` | Teaching-only element identity; safety/market fields; uncited element summaries |
| `de_core_biogenic_lang` | Climate/emissions statistics; regulatory compliance verdicts; unscoped EN environmental sources for DE lines |
| `copper_sulfides_language` | Mining market data; assay/procurement claims; nomenclature sources used for ore economics |
| `de_core_fes` | Commodity/pyrite market reports; production statistics; handling/SDS operational content |
| `de_core_mos2` | Lubricant/industrial application market data; performance claims; EN-only sources for DE naming lines |

---

## Why rejected candidates must not enter source_registry.json

- Registry rows imply **governed** source status under human charter
- Weak candidates create false audit trails and downstream publication risk
- Seeded/candidate registry posture must not be confused with verified entries
- Guardrail runtime and SOURCE_POLICY category alignment would fail or require retrospective cleanup

---

## Why rejected candidates must not be used to remove `[SOURCE REQUIRED]` markers

- Markers denote **unresolved authority**, not missing prose
- Partial candidate satisfaction creates false source-lock narrative
- Claim registries remain **inactive**; marker removal requires audited registry linkage and human signoff
- Publication remains blocked regardless of discovery documentation

---

*Sprint 5N-C — Candidate Source Rejection Rules Wave 1*
