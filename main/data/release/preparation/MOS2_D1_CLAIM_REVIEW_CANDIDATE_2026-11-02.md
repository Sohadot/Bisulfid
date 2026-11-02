# MoS₂ — D1 scientific claim-review preparation
**Status:** PREPARATORY ONLY / NOT AN APPROVAL / NOT A SIGNED REVIEW  
**Prepared:** 2026-11-02 by automated project assistant  
**Repository:** Sohadot/Bisulfid; PR #120 Draft; reviewed against head `4beff5bc37500d66be490c571d48c5c7a5ae7bf4`  
**Knowledge object:** `KO-MOS2-SCIENTIFIC-001`  
**Reference route:** existing `/molybdenum-disulfide/` (candidate, non-public/noindex)

## 0. Decision separation and evidence standard

The purpose is to prepare evidence-to-claim decisions, **not** to perform them. `main/data/pilots/PILOT_03_claims.json` records scientific support outcomes but **no `status: approved|approved_narrow` and no `claim_type`** for the three claims. `SUPPORTED_BY_EVIDENCE` and `SUPPORTED_CONDITIONAL` are scientific preparer outcomes, **not** claim-approval statuses. `documentary_verification.py` therefore correctly fails D1. All three remain pilot/non-operational. Owner activation in `owner_acts.json` and route release authorization are additional, separate actions; no such signatures are implied here.

Internal evaluation presently reports D2, D3, D5 and D6 PASS; D1, D4 and D7 open. D4 is a source-level reproducibility test across the entire KO; even a D1-ready wording cannot be called documentary-verified until D4, D7 and other applicable conditions pass. The listed evidence roles/uses and originating-work lineage must be preserved.

## 1. Individual review candidates (no statuses changed)

### A. `CLM-MOS2-FORMULA` — chemical identity only

**Existing statement:** “The formula of molybdenum disulfide is MoS2.”

**Suggested narrow wording for a future claim-review decision:** “The chemical composition of molybdenum disulfide is represented by the formula MoS₂.”

**Admitted evidence (as presently recorded):**
- `EVD-MOS2-FORMULA-PUBCHEM` — PubChem CID 14823, field `MolecularFormula = MoS2`, use `chemical_formula_identity`; source `SRC-PUBCHEM-MOS2`. L2/L3 passed on two recorded successful dated recaptures (2026-10-30, 2026-11-02).
- `EVD-MOS2-FORMULA-NIST` — NIST Chemistry WebBook, CAS 1317-33-5, field `Formula = MoS2`, same narrow use; source `SRC-NIST-MOS2`. L2 passes based on 2026-10-30; L3 pending. A 2026-11-02 HTTP 200 response was rejected by an overly narrow content test and must not be retroactively counted.

**What may be concluded now:** two independent authoritative database records agree on the chemical formula; D2/D3 admissions and the preparer's evidence-sufficiency finding stand. The formula field does **not** demonstrate a molecular solid composed of discrete MoS₂ molecules, or identify a crystal polytype.

**Decision not yet made:** whether to confer a scoped D1 claim approval on exactly this wording. A reviewer should confirm source identity and the explicit statement boundary, verify that the registry format and an eventual eligible claim type are justified, and note pending NIST L3. Neither `approved_narrow` nor `claim_type` may be written as a convenience to make D1 pass.

### B. `CLM-MOS2-STRUCTURE-2H` — bulk structure and 2H-specific framework

**Existing statement (summary):** bulk MoS₂ is layered; 2H-MoS₂ has hexagonal P63/mmc (No. 194) structure with a near 3.15–3.16 Å and c near 12.3 Å in source-specific bulk determinations.

**Suggested narrow wording for future review:** “Bulk MoS₂ has an S–Mo–S layered structure. In the 2H polytype, crystallographic records tracing the independent Dickinson–Pauling (1923) and Schönfeld–Huang–Moss (1983) studies describe a hexagonal P6₃/mmc structure; the respective recorded bulk 2H lattice values must remain attributed to their source determinations.”

**Evidence by scientific role:**
- **Originating 1923 study:** `EVD-MOS2-STRUCTURE-DICKINSON` via COD 1010993, `WORK-DICKINSON-PAULING-1923`. Structured data for P6₃/mmc, a=3.15(2) Å, c=12.30(7) Å. The `EVD-MOS2-MOLYBDENITE-JACS1923-EXCERPT` belongs to the **same** originating work and does **not** count as an independent experiment.
- **Originating 1983 study:** `EVD-MOS2-STRUCTURE-ACTACRYST` via COD 9007660, `WORK-SCHONFELD-HUANG-MOSS-1983`. Structured data for P6₃/mmc, a=3.161 Å, c=12.295 Å. The `EVD-MOS2-LAYERED-ACTA1983-EXCERPT` is **the same** original study, not an independent third source.
- **Peer-reviewed secondary review:** `EVD-MOS2-LAYERED-RSC`, `EVD-MOS2-POLYTYPES-RSC`, and `EVD-MOS2-2H-REF-RSC`, from Song, Park & Choi, RSC Advances 2015, DOI 10.1039/C4RA11852A. Supports the layered, 1T/2H/3R, and summarized 2H structural framework, **not** a new primary experiment; RSC Table 1 summarizes prior literature. The §2.1 label-convention fragments are recorded from publisher-indexed HTML, **not** a raw publisher capture.
- **Supporting historical thesis:** `EVD-MOS2-LAYERED-HUANG1981`, a 1981 M.S. thesis. Supports historical/structural context, **not** peer-reviewed corroboration or an independent lattice determination. Its scientific lineage overlaps the 1983 research group.

**Boundaries requiring explicit confirmation:** 1T, 2H, and 3R are distinct; the unchanged MoS₂ formula does not establish a stacking configuration. The historic 1923 paper is **not** evidence for the later label “2H” being used in 1923. The 2H c-axis unit-cell repeat is **not** the thickness of an individual S–Mo–S sandwich. No band-gap, monolayer, toxicity, industrial-performance or safety conclusions.

**Unresolved:** source locks D4 L2/L3 for RSC 2015, 1983 article excerpt and 1923 article excerpt; Huang thesis L2/L3/L4. Distinguish source access gaps from the underlying crystallographic database record reproductions, which passed L2/L3. Do not automatically drop the historical records from the KO to bypass D4; any source scope reduction needs its own substantive editorial evaluation and a preservation plan.

**Decision not yet made:** claim-specific `approved_narrow` versus precise wording revision/pending, supported by a source-level review record. No approval recorded here.

### C. `CLM-MOS2-LATTICE-A-2H` — coexisting determinations, not a universal constant

**Existing statement:** independent 1923 and 1983 determinations report the bulk 2H in-plane lattice parameter a as 3.15(2) Å and 3.161 Å, respectively.

**Suggested narrow wording for future review:** “For bulk 2H-MoS₂, the crystallographic record derived from Dickinson & Pauling (1923) reports an in-plane a parameter of 3.15(2) Å; the independent record derived from Schönfeld, Huang & Moss (1983) reports 3.161 Å. These are **two attributed determinations**, not a universal value.”

**Evidence:** `EVD-MOS2-LATTICE-A-DICKINSON` (COD 1010993) and `EVD-MOS2-LATTICE-A-ACTACRYST` (COD 9007660), admitted for `lattice_parameter_2h`. Both underlying originating works are distinct; their source records have two successful dated captures, 2026-10-30 and 2026-11-02.

**Interpretation guardrails:** the notation `3.15(2) Å` is recorded as a 0.02 Å uncertainty in the final digits. 3.161 Å lies in the numerical range 3.13–3.17 Å; this does not itself establish a confidence interval or statistically prove equivalence under every experimental condition. Preserve the two source literals and the reported measurement conditions. Do **not** average them, universalize them to 1T/3R, or substitute monolayer/few-layer data. Never treat the 1923 article excerpt and its COD record as two independent originating studies.

**Decision not yet made:** review of exact wording and conditions for an `approved_narrow` candidate, not a generic physical-property approval; approval and activation both remain unperformed.

## 2. Decision matrix to complete later — presently NOT SIGNED

| Claim | Preliminary scholarly posture | Material remaining evidence question | Owner/qualified-review decision needed | Current formal D1 |
|---|---|---|---|---|
| `CLM-MOS2-FORMULA` | Supported within chemical-composition scope | NIST L3, source-exact recheck | Exact wording, scope, eligibility and claim status | FAIL (no approval status) |
| `CLM-MOS2-STRUCTURE-2H` | Supported within bulk/2H structural scope; secondary roles qualified | RSC/Acta/JACS/Huang locks; origin and scope of each passage | Whether the entire composite claim warrants narrow approval or needs splitting/rewording **within the same KO and URL** | FAIL (no approval status) |
| `CLM-MOS2-LATTICE-A-2H` | Supported conditionally as two attributed bulk 2H measurements | Historical notation/conditions review; avoid overstating uncertainty | Exact statement and source-specific measurement scope | FAIL (no approval status) |

### Decision form (blank; do not sign on behalf of owner)

- Claim ID: __________
- Reviewed statement (exact bytes): __________
- Scope / excluded inferences: __________
- Evidence IDs and source-use qualifications inspected: __________
- Originating-work independence checked: __________
- D4 / source capture exceptions visible: __________
- Reviewer and independent-review status (if applicable): __________
- Decision: **PENDING** — proposed approved_narrow / revise / reject (circle only upon actual decision)
- Claim registry status: **UNCHANGED**
- Owner activation: **NOT AUTHORIZED**
- Route publication: **NOT AUTHORIZED**

## 3. Scope/record integrity

No status, claim type, evidence record, policy, KO, owner act or released/public page is modified by this preparation document. This file has **no authority** for `D1 = pass`, `documentary_verified`, source locks, independent human review, `AMD-IG-R03-001` ratification, merge, deployment or search indexation. Current `Contract C = (not_public, noindex)`.

## 4. Primary repository trace

- `main/data/pilots/PILOT_03_claims.json`
- `main/data/knowledge_objects/knowledge_object_registry.json`
- `main/data/release/claim_dossiers/KO-MOS2-SCIENTIFIC-001.json`
- `main/data/release/documentary_verification/KO-MOS2-SCIENTIFIC-001.json`
- `main/data/release/documentary_verification_policy.json`
- `main/data/claim_activation_policy.json`
- `main/data/evidence/captures/R03_MOS2_RECAPTURE.json`
- `main/data/evidence/captures/MOS2_RECAPTURE_2026-11-02.json`
- `main/data/evidence/access_attempts/SRC-RSC-MOS2-REVIEW-2015_2026-11-02.json`
- `main/data/reference_production/render_specs/KO-MOS2-SCIENTIFIC-001.json`

**Source URLs for eventual independent inspection (not fresh source captures by this document):** [PubChem CID 14823](https://pubchem.ncbi.nlm.nih.gov/compound/14823), [NIST WebBook CAS 1317-33-5](https://webbook.nist.gov/cgi/cbook.cgi?ID=1317-33-5), [COD 1010993](https://www.crystallography.net/cod/1010993.html), [COD 9007660](https://www.crystallography.net/cod/9007660.html), [RSC 2015 DOI](https://doi.org/10.1039/C4RA11852A), [JACS 1923 DOI](https://doi.org/10.1021/ja01659a020), [Acta 1983 DOI](https://doi.org/10.1107/S0108768183002645).
