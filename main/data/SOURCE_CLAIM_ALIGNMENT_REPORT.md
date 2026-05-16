# Source-to-Claim Governance Alignment Report — Sprint 3C

**Date:** 2026-05-16  
**Branch:** claude/sprint-3c-source-claim-governance-alignment  
**Governed by:** doctrine/SOURCE_POLICY.md

---

## Reviewed Files

- `main/data/sources/source_registry.json`
- `main/data/claims/terminology_claims.json`
- `main/data/claims/science_claims.json`
- `main/data/ontology/sulfur_terms.json`
- `main/content/en/pages/index.md`
- `main/content/en/pages/what-is-bisulfid.md`
- `main/content/en/pages/bisulfid-vs-bisulfide.md`
- `main/content/en/pages/sulfid-vs-sulfide.md`
- `main/content/en/pages/sources.md`
- `main/content/en/pages/acquire.md`

---

## Source Registry Status

**Total sources:** 9  
**Registry status:** inactive  
**All source entries carry:** `status: seeded`, `source_lock_status: candidate`

| source_id | category | publisher | Fields complete |
|---|---|---|---|
| SRC-MW-BISULFIDE | authoritative_dictionary | Merriam-Webster | ✓ |
| SRC-MW-SULFIDE | authoritative_dictionary | Merriam-Webster | ✓ |
| SRC-MW-BISULFITE | authoritative_dictionary | Merriam-Webster | ✓ |
| SRC-DUDEN-SULFID | authoritative_dictionary | Duden | ✓ |
| SRC-IUPAC-HYDROSULFIDES | chemical_nomenclature_standard | IUPAC Gold Book | ✓ |
| SRC-PUBCHEM-HYDROSULFIDE | government_scientific_database | PubChem / NIH | ✓ |
| SRC-PUBCHEM-SODIUM-HYDROSULFIDE | government_scientific_database | PubChem / NIH | ✓ |
| SRC-NIST-HYDROGEN-SULFIDE | government_scientific_database | NIST Chemistry WebBook | ✓ |
| SRC-BADGER-BISULFID-H2S | industry_publication | Badger Meter | ✓ |

All 9 entries confirmed to have: `source_id`, `category`, `publisher`, `title`, `url`, `status: seeded`, `source_lock_status: candidate`, `use_for` (array), `do_not_use_for` (array), `risk_notes` (array), `last_reviewed`. No source entry has `source_lock_status: locked` or `final`. No source entry is approved.

**Source scope review — all sources confirmed within permitted scope:**

- **Merriam-Webster sources** (SRC-MW-BISULFIDE, SRC-MW-SULFIDE, SRC-MW-BISULFITE): scoped to English lexical and terminology context only. `do_not_use_for` explicitly excludes chemical safety, industrial usage, market data, medical claims. ✓
- **Duden** (SRC-DUDEN-SULFID): scoped to German spelling and linguistic identity only. Excludes English bisulfide claims, safety, industrial, market, and medical uses. ✓
- **IUPAC Gold Book** (SRC-IUPAC-HYDROSULFIDES): scoped to nomenclature context only. Excludes market data, safety instructions, medical claims, industrial procurement. ✓
- **PubChem** (SRC-PUBCHEM-HYDROSULFIDE, SRC-PUBCHEM-SODIUM-HYDROSULFIDE): scoped to database identity context only. Explicitly excludes handling instructions, medical advice, exposure thresholds, procurement language. ✓
- **NIST** (SRC-NIST-HYDROGEN-SULFIDE): scoped to chemical identity context only. Explicitly excludes safety guidance, handling instructions, emergency advice. ✓
- **Badger Meter** (SRC-BADGER-BISULFID-H2S): scoped to German technical usage observation only. Explicitly excludes formal nomenclature authority, safety advice, market data, medical claims, and proof of preferred IUPAC spelling. ✓

No source is used for market data, safety advice, exposure thresholds, handling instructions, medical advice, company acquisition targeting, or bisulfite data presented as bisulfide data.

---

## Terminology Claims Status

**Total terminology claims:** 6  
**Registry status:** inactive  
**All claims:** `status: pending_review`

### Structural Inconsistency Found and Corrected

CLM-TERM-001 through CLM-TERM-005 were missing three governance fields present in CLM-TERM-BISULFID-001: `allowed_pages`, `prohibited_uses`, `risk_level`. These fields were added to all five claims in this sprint as a structural correction. No claim status was changed. No claim was approved.

| claim_id | source_ids | allowed_pages | risk_level | status |
|---|---|---|---|---|
| CLM-TERM-001 | SRC-MW-BISULFIDE | bisulfid_vs_bisulfide, what_is_bisulfid, glossary | low | pending_review |
| CLM-TERM-002 | SRC-MW-SULFIDE | sulfid_vs_sulfide, what_is_bisulfid, glossary | low | pending_review |
| CLM-TERM-003 | SRC-DUDEN-SULFID | sulfid_vs_sulfide, german_english_chemical_terms, glossary | low | pending_review |
| CLM-TERM-004 | SRC-MW-BISULFITE | what_is_bisulfid, bisulfid_vs_bisulfide, glossary | medium | pending_review |
| CLM-TERM-005 | SRC-IUPAC-HYDROSULFIDES | bisulfide_hydrosulfide_sulfide, what_is_bisulfid, glossary | low | pending_review |
| CLM-TERM-BISULFID-001 | SRC-BADGER-BISULFID-H2S | what_is_bisulfid, bisulfid_vs_bisulfide, german_english_chemical_terms | medium | pending_review |

All 6 claims confirmed: no market data, no safety advice, no exposure thresholds, no handling instructions, no medical advice, no acquisition targeting. No bisulfite data used as bisulfide data.

---

## Science Claims Status

**Total science claims:** 3  
**Registry status:** inactive  
**All claims:** `status: pending_review`

### Structural Inconsistency Found and Corrected

CLM-SCI-001 through CLM-SCI-003 were missing three governance fields: `allowed_pages`, `prohibited_uses`, `risk_level`. These fields were added to all three claims in this sprint as a structural correction. No claim status was changed. No claim was approved.

| claim_id | source_ids | allowed_pages | risk_level | status |
|---|---|---|---|---|
| CLM-SCI-001 | SRC-PUBCHEM-HYDROSULFIDE | bisulfide_hydrosulfide_sulfide, glossary | low | pending_review |
| CLM-SCI-002 | SRC-PUBCHEM-SODIUM-HYDROSULFIDE | sodium_bisulfide, glossary | medium | pending_review |
| CLM-SCI-003 | SRC-NIST-HYDROGEN-SULFIDE | hydrogen_sulfide_risk, glossary | high | pending_review |

Note: CLM-SCI-003 carries `risk_level: high` because hydrogen sulfide is an acutely hazardous gas. A high risk level does not block the claim — it requires heightened governance attention before any related content reaches publication. No safety advice is contained in the claim statement.

All 3 claims confirmed: no market data, no safety advice as prescriptive instruction, no exposure thresholds as advice, no handling instructions, no medical advice.

---

## Ontology Source Mapping Status

**Total terms:** 14  
**All statuses:** planned  
**No term is marked verified.**

| term_id | source_ids | status |
|---|---|---|
| bisulfid | SRC-BADGER-BISULFID-H2S | planned |
| bisulfide | SRC-MW-BISULFIDE | planned |
| sulfide | SRC-MW-SULFIDE | planned |
| sulfid | SRC-DUDEN-SULFID | planned |
| bisulfite_disambiguation | SRC-MW-BISULFITE | planned |
| hydrosulfide | SRC-IUPAC-HYDROSULFIDES, SRC-PUBCHEM-HYDROSULFIDE | planned |
| sodium_bisulfide | SRC-PUBCHEM-SODIUM-HYDROSULFIDE | planned |
| sodium_hydrosulfide | SRC-PUBCHEM-SODIUM-HYDROSULFIDE | planned |
| hydrogen_sulfide | SRC-NIST-HYDROGEN-SULFIDE | planned |
| disulfide | (none) | planned |
| disulfid | (none) | planned |
| molybdenum_disulfide | (none) | planned |
| molybdenum_disulfide_mos2 | (none) | planned |
| sulfur | (none) | planned |

**bisulfid center node:** `source_ids` contains SRC-BADGER-BISULFID-H2S (candidate only, `industry_publication` tier — weakest source category). Status remains `planned`. Not verified. Stronger tier-1 source still required.

**bisulfite_disambiguation:** correctly scoped to disambiguation only. Not conflated with bisulfide. `not_to_be_confused_with` includes bisulfid, bisulfide, sulfide, and hydrosulfide. ✓

**Terms without any source_ids (5):** disulfide, disulfid, molybdenum_disulfide, molybdenum_disulfide_mos2, sulfur. These are lower priority than bisulfid center node source-locking. No source sprint addresses them yet.

---

## Pages Reviewed

### index.md (route: home)

- `route_id: home` | `status: draft` | `publication_status: non_public` | `indexable: false` | `in_sitemap: false` ✓
- **[SOURCE REQUIRED] areas:**
  - Nomenclature layer: "formal nomenclature authority citations" — no registered claim covers this
  - Industrial Reference layer — no registered claim covers industrial relevance
- **Relevant pending claims:** None directly map to the [SOURCE REQUIRED] areas on this page yet
- **Publication blocked:** Yes

### what-is-bisulfid.md (route: what_is_bisulfid)

- `route_id: what_is_bisulfid` | `status: draft` | `publication_status: non_public` | `indexable: false` | `in_sitemap: false` ✓
- **[SOURCE REQUIRED] areas:**
  1. Formal nomenclature authority for German vs English chemical naming conventions
  2. Ion assignment for bisulfide (HS⁻)
  3. Ion assignment for bisulfite (HSO₃⁻)
  4. Any further chemical detail added in future drafts
- **Relevant pending claims:**
  - CLM-TERM-BISULFID-001: partially supports German technical usage of Bisulfid — does not satisfy formal nomenclature authority requirement
  - CLM-TERM-004: supports bisulfite disambiguation — does not cover ion assignment directly
  - CLM-SCI-001 (pending): supports Hydrosulfide (HS⁻) compound identity — partial support for ion area after approval
- **Mapping gap:** No registered claim covers formal nomenclature authority for the EN/DE naming convention. Ion assignment for bisulfite (HSO₃⁻) has no corresponding registered claim or source.
- **Publication blocked:** Yes

### bisulfid-vs-bisulfide.md (route: bisulfid_vs_bisulfide)

- `route_id: bisulfid_vs_bisulfide` | `status: draft` | `publication_status: non_public` | `indexable: false` | `in_sitemap: false` ✓
- **[SOURCE REQUIRED] areas:**
  1. "compound with chemical and industrial relevance" — no approved claim
  2. Formal nomenclature authority citations on the EN/DE suffix pattern
- **Relevant pending claims:**
  - CLM-TERM-001: supports English-language lexical existence of bisulfide
  - CLM-TERM-BISULFID-001: partially supports German technical usage of Bisulfid
- **Mapping gap:** EN/DE suffix pattern requires formal nomenclature authority source (IUPAC, DIN, or authoritative German dictionary directly under Bisulfid). CLM-TERM-BISULFID-001 (Badger Meter, industry_publication) does not satisfy this requirement.
- **Publication blocked:** Yes

### sulfid-vs-sulfide.md (route: sulfid_vs_sulfide)

- `route_id: sulfid_vs_sulfide` | `status: draft` | `publication_status: non_public` | `indexable: false` | `in_sitemap: false` ✓
- **[SOURCE REQUIRED] areas:**
  1. The -id/-ide suffix as a systematic German/English distinction
  2. Oxide/Oxid and Chloride/Chlorid examples
  3. Formal IUPAC or DIN standard governing the suffix pattern
- **Relevant pending claims:**
  - CLM-TERM-003: supports Duden entry for Sulfid — partial support for the -id suffix in one example only
- **Mapping gap:** No registered claim covers Oxide/Oxid, Chloride/Chlorid, or a systematic suffix-pattern nomenclature standard. CLM-TERM-003 alone cannot support the broader pattern claim. This is the most heavily blocked page in this review — three distinct source gaps with no corresponding registered claims.
- **Publication blocked:** Yes

### sources.md (route: sources)

- `route_id: sources` | `status: draft` | `publication_status: non_public` | `indexable: false` | `in_sitemap: false` ✓
- **[SOURCE REQUIRED] areas:** None — this page describes source governance policy, not chemistry claims
- **Stale statement identified:** The page states "The source registry is not populated yet." As of Sprint 3, 9 sources are seeded. This statement is factually inaccurate. Content page modification is deferred per Sprint 3C governance; correction is noted as a required action in a future content update sprint.
- **Relevant pending claims:** N/A
- **Publication blocked:** Yes — contains inaccurate source registry status statement that must be corrected before publication

### acquire.md (route: acquire)

- `route_id: acquire` | `status: draft` | `publication_status: non_public` | `indexable: false` | `in_sitemap: false` ✓
- **[SOURCE REQUIRED] areas:** None — this page describes the acquisition surface and makes no chemistry, market, or regulatory claims
- No market data. No acquisition-target company claims. No safety content. ✓
- **Relevant pending claims:** N/A
- **Publication blocked:** Yes — no route is published

---

## Claim-to-Page Mapping Table

| claim_id | type | allowed_pages | status | source tier |
|---|---|---|---|---|
| CLM-TERM-001 | terminology | bisulfid_vs_bisulfide, what_is_bisulfid, glossary | pending_review | authoritative_dictionary |
| CLM-TERM-002 | terminology | sulfid_vs_sulfide, what_is_bisulfid, glossary | pending_review | authoritative_dictionary |
| CLM-TERM-003 | terminology | sulfid_vs_sulfide, german_english_chemical_terms, glossary | pending_review | authoritative_dictionary |
| CLM-TERM-004 | terminology | what_is_bisulfid, bisulfid_vs_bisulfide, glossary | pending_review | authoritative_dictionary |
| CLM-TERM-005 | terminology | bisulfide_hydrosulfide_sulfide, what_is_bisulfid, glossary | pending_review | chemical_nomenclature_standard |
| CLM-TERM-BISULFID-001 | terminology | what_is_bisulfid, bisulfid_vs_bisulfide, german_english_chemical_terms | pending_review | industry_publication |
| CLM-SCI-001 | chemical_identity | bisulfide_hydrosulfide_sulfide, glossary | pending_review | government_scientific_database |
| CLM-SCI-002 | chemical_identity | sodium_bisulfide, glossary | pending_review | government_scientific_database |
| CLM-SCI-003 | chemical_identity | hydrogen_sulfide_risk, glossary | pending_review | government_scientific_database |

---

## Claims That Are Candidates for Future Approval

The following claims are structurally sound, appropriately scoped, and may be candidates for approval in a future sprint. No approval is made in this sprint.

1. **CLM-TERM-001** — Bisulfide lexical entry in Merriam-Webster. `risk_level: low`. Direct lexical existence claim. Source is authoritative_dictionary. Strong candidate for future approval.
2. **CLM-TERM-002** — Sulfide lexical entry in Merriam-Webster. `risk_level: low`. Direct lexical existence claim. Source is authoritative_dictionary. Strong candidate for future approval.
3. **CLM-TERM-003** — Sulfid lexical entry in Duden. `risk_level: low`. Direct lexical existence claim. Source is authoritative_dictionary. Strong candidate for future approval.
4. **CLM-TERM-004** — Bisulfite is distinct from bisulfide per Merriam-Webster. `risk_level: medium`. Disambiguation claim with direct source support. Candidate for future approval.
5. **CLM-TERM-005** — Hydrosulfides entry in IUPAC Gold Book. `risk_level: low`. Database existence claim. Source is chemical_nomenclature_standard. Strong candidate for future approval.
6. **CLM-SCI-001** — Hydrosulfide compound record in PubChem. `risk_level: low`. Database existence claim. Source is government_scientific_database. Strong candidate for future approval.

---

## Claims Requiring Stronger Sources

- **CLM-TERM-BISULFID-001**: Source is `industry_publication` (weakest tier). Bisulfid center node requires at minimum a Duden 'Bisulfid' entry, IUPAC direct bisulfide/bisulfid entry, or German regulatory/government database entry before this claim can progress toward approval.
- **CLM-SCI-002**: Sodium hydrosulfide / NaHS mapping to sodium bisulfide remains candidate. Requires additional dedicated source-locking before the equivalence can be asserted on a public page.
- **CLM-SCI-003**: Hydrogen sulfide NIST entry is structurally sound, but `risk_level: high` requires heightened governance review before any H2S safety-adjacent content progresses toward publication.

---

## Claims That Must Remain Non-Public

All 9 claims must remain non-public until:
1. The claim registry `status` is explicitly changed from `inactive`.
2. Each individual claim is approved through an explicit approval sprint.
3. The corresponding route passes the Quality Gate.

No claim is approved in this sprint.

---

## [SOURCE REQUIRED] Areas Remaining

### what_is_bisulfid
- Formal nomenclature authority for German vs English chemical naming conventions — no registered claim with sufficient source tier
- Ion assignment for bisulfide (HS⁻) — partially addressable by CLM-SCI-001 pending future approval; not currently resolved
- Ion assignment for bisulfite (HSO₃⁻) — no registered claim and no registered source for bisulfite ion identity

### bisulfid_vs_bisulfide
- Chemical and industrial relevance of the bisulfid compound — no approved claim
- Formal nomenclature authority citations for EN/DE suffix pattern — no registered claim with formal nomenclature authority source tier

### sulfid_vs_sulfide
- The -id/-ide suffix pattern as a systematic German/English distinction — only CLM-TERM-003 (Sulfid in Duden) partially supports one example; no claim covers the pattern as a system
- Oxide/Oxid and Chloride/Chlorid examples — no registered claim, no registered source
- Formal IUPAC or DIN standard governing the suffix pattern — no registered claim, no registered source

### home (index.md)
- Formal nomenclature authority citations (Nomenclature layer) — no registered claim
- Industrial Reference layer — no registered claim for any industrial relevance statements

---

## Publication Readiness Conclusion

**Status: Not ready for publication.**

No route may be published. Specific blockers:

1. No claim has been approved.
2. Claim registries remain `inactive`.
3. All routes remain `planned`.
4. All draft pages carry `publication_status: non_public`.
5. Multiple [SOURCE REQUIRED] markers remain on all chemistry-facing pages.
6. The bisulfid center node still requires a tier-1 authoritative source (Duden Bisulfid, IUPAC direct entry, German regulatory/government database, or peer-reviewed academic reference).
7. The -id/-ide suffix pattern as a systematic distinction has no registered claim with a formal nomenclature authority source.
8. `sources.md` contains a stale statement ("The source registry is not populated yet") that must be corrected before publication.
9. No Quality Gate check has been run.

---

**No claim was approved in this sprint.**

---

*Report generated: Sprint 3C — docs(sources): align source and claim governance*
