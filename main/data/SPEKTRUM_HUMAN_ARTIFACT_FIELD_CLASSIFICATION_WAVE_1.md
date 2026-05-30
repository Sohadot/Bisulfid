# Spektrum Human Artifact Field Classification — Wave 1

**Sprint:** 5N-N  
**Scope:** Human-reviewed Spektrum receipt for `de_core_mos2`  
**Date:** 2026-05-30

| field_name | human_reviewed_value | classification | may_enter_future_registry | must_remain_blank_if_unverified | must_not_be_invented | execution_impact | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| source_title | Molybdän(IV)-sulfid - Lexikon der Chemie | verified_from_human_artifact | yes | no | yes | Low — title confirmed | Matches intake subject |
| author_or_organization | Fachkoordination: Hans-Dieter Jakubke, Ruth Karcher; Redaktion: Sabine Bartels, Ruth Karcher, Sonja Nagel; Die Autoren: [full lexicon author list reviewed on page] | verified_from_human_artifact | yes | no | yes | Medium — registry row may summarize editorial team rather than repeat full list | Entry-specific single author not named; collective lexicon authorship model |
| publisher | Spektrum Akademischer Verlag, Heidelberg | verified_from_human_artifact | yes | no | yes | Low — publisher confirmed | From copyright line on reviewed page |
| publication_date | *(blank)* | not_visible_from_source; must_remain_blank; rejected_if_unverified | no | yes | yes | **High — field blank at execution** | Copyright 1998 **not** used as publication_date |
| copyright_year | 1998 (Spektrum Akademischer Verlag) | visible_but_policy_sensitive | no | not_applicable | yes | Low — rights evidence only | **Not** `publication_date`; supports rights_or_license_posture only |
| url_or_doi | https://www.spektrum.de/lexikon/chemie/molybdaen-iv-sulfid/5985 | verified_from_human_artifact | yes | no | yes | Low — stable URL confirmed | No DOI on reviewed page |
| edition_or_version | *(blank)* | not_visible_from_source; must_remain_blank | conditional | yes | yes | Medium — omit at execution if unverified | Do not infer from copyright year |
| page_or_entry_citation | entry: Molybdän(IV)-sulfid, in Lexikon der Chemie | verified_from_human_artifact | yes | no | yes | Low — entry locator confirmed | Online path: `/lexikon/chemie/molybdaen-iv-sulfid/5985` |
| access_date | 2026-05-30 | verified_from_human_artifact | yes | no | yes | Low — access documented | Repository owner direct review date |
| rights_or_license_posture | Copyright 1998 Spektrum Akademischer Verlag, Heidelberg; bibliographic reference only; no full copyrighted text copied | verified_from_human_artifact | yes | no | yes | Medium — governs registry/public use scope | Full digital license terms not exhaustively reviewed |
| verification_note | Reviewed directly by repository owner from live Spektrum page; publicly accessible; no body text copied | verified_from_human_artifact | yes | no | yes | Low — provenance confirmed | Human sign-off on receipt; not execution approval |

*Rows: 11* (includes separate `copyright_year` policy row)

**Governance carry-forward (5N-K — unchanged):** `SRC-SPEKTRUM-MOS2-DE`, source family, `authoritative_dictionary`, `de`, `de_core_mos2`, claim boundary scope.

**Classification summary:**

| Classification | Count |
| --- | ---: |
| verified_from_human_artifact | **8** |
| not_visible_from_source / must_remain_blank | **2** (`publication_date`, `edition_or_version`) |
| visible_but_policy_sensitive | **1** (`copyright_year`) |
| rejected_if_unverified | **1** (`publication_date` if invented) |

**Posture:** **`execution_candidate_after_artifact_review`** · **`source_registry_execution_not_allowed_now`** · **`source_approval_not_allowed_now`**
