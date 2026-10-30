# Independent review packet — KO-MOS2-SCIENTIFIC-001

Route: `/molybdenum-disulfide/` · render spec `RSPEC-KO-MOS2-SCIENTIFIC-001@1.1.0` · prepared by `claude-code-agent` (automated; **cannot** act as reviewer).

## Reviewer requirements

- A named person who did not prepare this object, with competence in the subject domain.
- Declare conflicts of interest. Check every claim below against the cited source itself.
- Record the result in `main/data/release/reviews/KO-MOS2-SCIENTIFIC-001.json` (policy: `main/data/release/release_review_policy.json`). Verdicts: confirmed, confirmed_with_wording_change, rejected, out_of_competence. Validation counts only when every claim is `confirmed` and no finding is open.

## Claim 1: `CLM-MOS2-FORMULA`

**Statement:** The formula of molybdenum disulfide is MoS2.

**Scope:** Chemical composition identity only. Not structure, not a physical property.

| Evidence | Source | Status / lock | Admitted for | Record | Retrieved |
|---|---|---|---|---|---|
| `EVD-MOS2-FORMULA-PUBCHEM` | PubChem / NIH (National Center for Biotechnology Information): Molybdenum disulfide (PubChem Compound CID 14823) | verified / candidate | chemical_formula_identity | CID 14823 | 2026-09-20 |
| `EVD-MOS2-FORMULA-NIST` | NIST (National Institute of Standards and Technology) Chemistry WebBook: Molybdenum disulphide (NIST Chemistry WebBook, CAS 1317-33-5) | verified / candidate | chemical_formula_identity | CAS 1317-33-5 | 2026-09-20 |

Quoted passages / values:

- `EVD-MOS2-FORMULA-PUBCHEM`: {"MolecularFormula": "MoS2", "MolecularWeight": "160.1", "title": "MOLYBDENUM DISULFIDE"}
- `EVD-MOS2-FORMULA-NIST`: {"Formula": "MoS2", "molecularWeight": "160.09 amu", "title": "molybdenum disulphide"}

Reviewer checklist:

- [ ] Does each quoted passage/value appear in the cited source as recorded?
- [ ] Does the statement say no more than the evidence supports (scope, form, polytype, language)?
- [ ] Is the source an appropriate authority for this kind of claim?
- [ ] Is the rendered wording on the page faithful to the claim?

Verdict: ☐ confirmed ☐ confirmed with wording change ☐ rejected ☐ out of competence

## Claim 2: `CLM-MOS2-STRUCTURE-2H`

**Statement:** Bulk MoS2 is a layered material. In the 2H polytype, MoS2 has a hexagonal P63/mmc (No. 194) structure with lattice parameters near a ~ 3.15-3.16 A and c ~ 12.3 A in the admitted bulk crystallographic determinations.

**Scope:** The scientifically established chemical identity and BULK structural facts BISULFID can currently support for molybdenum disulfide: the formula MoS2; that bulk MoS2 is layered; the 2H polytype hexagon

| Evidence | Source | Status / lock | Admitted for | Record | Retrieved |
|---|---|---|---|---|---|
| `EVD-MOS2-STRUCTURE-DICKINSON` | Crystallography Open Database (COD) — public-domain crystallographic data repository: COD entry 1010993 — 2H-MoS2 (molybdenite) crystallographic data (structured record of Dickinson & Pauling 1923) | verified / candidate | crystal_structure_identity_2h | COD 1010993 | 2026-09-20 |
| `EVD-MOS2-STRUCTURE-ACTACRYST` | Crystallography Open Database (COD) — public-domain crystallographic data repository: COD entry 9007660 — 2H-MoS2 crystallographic data (structured record of Schonfeld, Huang & Moss 1983) | verified / candidate | crystal_structure_identity_2h | COD 9007660 | 2026-09-20 |
| `EVD-MOS2-2H-REF-RSC` | RSC Advances (Royal Society of Chemistry): Synthesis and properties of molybdenum disulphide: from bulk to atomic layers | verified / candidate | not rendered |  | 2026-09-20 |
| `EVD-MOS2-LAYERED-RSC` | RSC Advances (Royal Society of Chemistry): Synthesis and properties of molybdenum disulphide: from bulk to atomic layers | verified / candidate | layered_structure_mos2 | doi:10.1039/C4RA11852A | 2026-09-20 |
| `EVD-MOS2-POLYTYPES-RSC` | RSC Advances (Royal Society of Chemistry): Synthesis and properties of molybdenum disulphide: from bulk to atomic layers | verified / candidate | mos2_polytype_framework | doi:10.1039/C4RA11852A | 2026-09-20 |
| `EVD-MOS2-LAYERED-ACTA1983-EXCERPT` | Acta Crystallographica Section B (International Union of Crystallography): Anisotropic Mean-Square Displacements (MSD) in Single Crystals of 2H- and 3R-MoS2 (page-404 excerpt) | verified / candidate | mos2_2h_3r_terminology | doi:10.1107/S0108768183002645 | 2026-09-20 |
| `EVD-MOS2-MOLYBDENITE-JACS1923-EXCERPT` | Journal of the American Chemical Society (American Chemical Society): The Crystal Structure of Molybdenite (first-page excerpt, p.1466) | verified / candidate | molybdenite_mos2_hexagonal_identity | doi:10.1021/ja01659a020 | 2026-09-20 |
| `EVD-MOS2-LAYERED-HUANG1981` | University of Houston, Department of Physics (M.S. thesis): X-ray Study of Anisotropic Vibrations in MoS2 | verified / candidate | not rendered |  | 2026-09-20 |

Quoted passages / values:

- `EVD-MOS2-STRUCTURE-DICKINSON`: {"_symmetry_space_group_name_H-M": "P 63/m m c", "_space_group_IT_number": "194", "_cell_length_a": "3.15(2)", "_cell_length_c": "12.30(7)", "_chemical_name_mineral": "Molybdenite"}
- `EVD-MOS2-STRUCTURE-ACTACRYST`: {"_symmetry_space_group_name_H-M": "P 63/m m c", "_cell_length_a": "3.161", "_cell_length_c": "12.295", "_chemical_name_mineral": "Molybdenite"}
- `EVD-MOS2-2H-REF-RSC`: "2H ... P63/mmc ... AbA BaB ... a = 3.15 A and c = 12.30 A (ref. 35)"
- `EVD-MOS2-LAYERED-RSC`: "MoS2, like graphite, is a layered material, where each layer of MoS2 is composed of three-atom-thick S-Mo-S stacks."
- `EVD-MOS2-POLYTYPES-RSC`: "three known polytypes - namely 1T, 2H, and 3R - of MoS2 ... 2H and 3R commonly have trigonal prismatic coordination (D3h) of molybdenum atoms, but they have different stacking order."
- `EVD-MOS2-LAYERED-ACTA1983-EXCERPT`: "title: 'Anisotropic Mean-Square Displacements (MSD) in Single Crystals of 2H- and 3R-MoS2'; intro: 'MoS2 belongs to the layered dichalcogenides of transition metals ...'"
- `EVD-MOS2-MOLYBDENITE-JACS1923-EXCERPT`: "The mineral molybdenite, MoS2, is described as occurring in hexagonal crystals with a very complete basal cleavage. A study of its crystal structure has been carried out using X-ray spectral photographs and Laue photographs."
- `EVD-MOS2-LAYERED-HUANG1981`: "Molybdenite, 2H-MoS2, whose structure was first investigated by Dickinson and Pauling. The 2H-MoS2 is hexagonal and the structure is characterized by MoS2 layers with A-B-A stacking ... c = 12.30 A and a = 3.15 A ... sandwich-like layer stacking."

Reviewer checklist:

- [ ] Does each quoted passage/value appear in the cited source as recorded?
- [ ] Does the statement say no more than the evidence supports (scope, form, polytype, language)?
- [ ] Is the source an appropriate authority for this kind of claim?
- [ ] Is the rendered wording on the page faithful to the claim?

Verdict: ☐ confirmed ☐ confirmed with wording change ☐ rejected ☐ out of competence

## Claim 3: `CLM-MOS2-LATTICE-A-2H`

**Statement:** The in-plane hexagonal lattice parameter a of bulk 2H-MoS2 is reported by independent determinations as 3.15(2) A (Dickinson & Pauling 1923 lineage) and 3.161 A (Schonfeld, Huang & Moss 1983 lineage).

**Scope:** 2H bulk ONLY. A monolayer/few-layer or 3R value must never substitute for this.

| Evidence | Source | Status / lock | Admitted for | Record | Retrieved |
|---|---|---|---|---|---|
| `EVD-MOS2-LATTICE-A-DICKINSON` | Crystallography Open Database (COD) — public-domain crystallographic data repository: COD entry 1010993 — 2H-MoS2 (molybdenite) crystallographic data (structured record of Dickinson & Pauling 1923) | verified / candidate | lattice_parameter_2h | COD entry 1010993 | 2026-09-20 |
| `EVD-MOS2-LATTICE-A-ACTACRYST` | Crystallography Open Database (COD) — public-domain crystallographic data repository: COD entry 9007660 — 2H-MoS2 crystallographic data (structured record of Schonfeld, Huang & Moss 1983) | verified / candidate | lattice_parameter_2h | COD entry 9007660 | 2026-09-20 |

Quoted passages / values:

- `EVD-MOS2-LATTICE-A-DICKINSON`: null
- `EVD-MOS2-LATTICE-A-ACTACRYST`: null

Reviewer checklist:

- [ ] Does each quoted passage/value appear in the cited source as recorded?
- [ ] Does the statement say no more than the evidence supports (scope, form, polytype, language)?
- [ ] Is the source an appropriate authority for this kind of claim?
- [ ] Is the rendered wording on the page faithful to the claim?

Verdict: ☐ confirmed ☐ confirmed with wording change ☐ rejected ☐ out of competence

## Boundary records (support no claim)

- `EVD-MOS2-3R-BOUNDARY-RSC` (Synthesis and properties of molybdenum disulphide: from bulk to atomic layers): "3R ... R3m ... AbA BcB CaC ... a = 3.17 A and c = 18.38 A (ref. 36)"

## Stated as NOT established on the page

Band gap, electronic and optical behaviour, density, the properties of single layers, industrial and lubricant uses, market data, safety handling, and German terminology are outside the governed evidence for this object. They are open questions here, not implied facts. Any statement on them needs governed evidence first [SOURCE REQUIRED].

## Signature

Reviewer (name): ______  Affiliation: ______  Independent of preparer: ☐ yes  Date: ______
