# Source Registry — Qualification Audit (all 15 existing sources)

**Sprint:** source-qualification-evidence-admission · **Date:** 2026-09-19 · **No new sources. No `use_for` broadened. No status changed.**

Framework applied from `SOURCE_QUALIFICATION_PROTOCOL.md`. "Qualification granted?" reflects **only** what current repository review supports. All 15 sources are `source_lock_status: candidate`; only `SRC-SPEKTRUM-MOS2-DE` is `status: verified`. A source with `status: seeded` has **not** been reviewed enough to grant any use-scoped qualification → stays **pending**.

| source_id | category | status | lock | plausible narrow qualification (future) | qualification granted now? |
|---|---|---|---|---|---|
| SRC-MW-BISULFIDE | authoritative_dictionary | seeded | candidate | EN lexical existence (bisulfide) | **No — pending review** |
| SRC-MW-SULFIDE | authoritative_dictionary | seeded | candidate | EN lexical existence (sulfide) | **No — pending** |
| SRC-MW-BISULFITE | authoritative_dictionary | seeded | candidate | EN lexical existence (bisulfite, disambiguation control) | **No — pending** |
| SRC-DUDEN-SULFID | authoritative_dictionary | seeded | candidate | DE lexical existence (Sulfid) | **No — pending** |
| SRC-DUDEN-OXID | authoritative_dictionary | seeded | candidate | DE lexical existence (Oxid) | **No — pending** |
| SRC-DUDEN-CHLORID | authoritative_dictionary | seeded | candidate | DE lexical existence (Chlorid) | **No — pending** |
| SRC-IUPAC-INORGANIC-NOMENCLATURE-1971 | chemical_nomenclature_standard | seeded | candidate | nomenclature-rule context (edition-bound) | **No — pending** |
| SRC-IUPAC-HYDROSULFIDES | chemical_nomenclature_standard | seeded | candidate | hydrosulfide nomenclature context | **No — pending** |
| SRC-PUBCHEM-HYDROSULFIDE | government_scientific_database | seeded | candidate | HS⁻ compound identity/properties (record-bound) | **No — pending** |
| SRC-PUBCHEM-SODIUM-HYDROSULFIDE | government_scientific_database | seeded | candidate | NaHS identity/properties (record-bound) | **No — pending** |
| SRC-NIST-HYDROGEN-SULFIDE | government_scientific_database | seeded | candidate | H₂S identity/properties (record-bound) | **No — pending** |
| SRC-BADGER-BISULFID-H2S | industry_publication | seeded | candidate | scoped observed industrial context only (contextual role) | **No — pending** |
| SRC-FH-MUENSTER-ANORGANISCHE-NOMENKLATUR | academic_teaching_reference | seeded | candidate | secondary teaching context only (never sole formal authority) | **No — pending** |
| SRC-UNI-ROSTOCK-NOMENKLATUR-ID-ANIONEN | academic_teaching_reference | seeded | candidate | secondary teaching context only | **No — pending** |
| **SRC-SPEKTRUM-MOS2-DE** | authoritative_dictionary | **verified** | candidate | German MoS₂ dictionary-entry lexical form (terminology/lexeme, de) | **YES — `QUAL-SPEKTRUM-MOS2-DE-001` (qualified_narrow)** |

**Rationale for the single granted qualification:** `SRC-SPEKTRUM-MOS2-DE` was already `verified` and its `use_for`/`do_not_use_for` already reviewed (Sprint 5N-T). `QUAL-SPEKTRUM-MOS2-DE-001` re-expresses that exact reviewed boundary in the new machine-readable form (`applicable_subject_domains: [SD-TERMINOLOGY, SD-LINGUISTICS]`, `permitted_evidence_kinds: [terminological]`, `permitted_claim_levels: [lexeme]`), broadening nothing and prohibiting concept/market/safety/medical/procurement/EN-only/IUPAC-authority/publication uses.

**What remains unreviewed (the 14):** none has been reviewed against a specific scoped assertion; each would require a scope review (statement-does-not-exceed-source, correct target level/domain/boundary) before a `reviewed → qualified_narrow` transition. That review is **not** performed here (no acquisition). They stay pending; absence of a qualification = not admissible.

**Categories with zero sources:** `regulatory_body`, `peer_reviewed_journal`, `market_report` are approved categories but currently hold no sources; the 7 newly-ratified trade/regulatory/standard categories hold none. No admission is possible in those categories yet.
