# Sovereign Generator Reference Layer Duplication Guard — Wave 1

**Sprint:** 6C  
**Purpose:** Prevent shallow page duplication when generator processes reference_layer dimension.

---

## Problem

Without guardrails, batch generation could emit near-identical pages for the same `term + language + page_type` with only cosmetic audience labels — violating the sovereign reference matrix principle.

---

## Guard rule

A page may exist **only if** `reference_layer` changes at least one of:

1. **Structure** — different template sections (e.g. TPL_AI_READABLE vs TPL_CHILD_EDU)  
2. **Purpose** — different reference intent (research vs educational vs economic)  
3. **Evidence standard** — different evidence_grade or source hierarchy requirement  
4. **Vocabulary level** — audience_simplification_limit differs  
5. **Internal links** — different internal_link_role or hub cluster  
6. **Claim boundary** — different allowed/forbidden claim classes  

---

## Generator algorithm

```
1. Compute base_key = hash(language, term_entity_id, page_type_id)
2. For candidate (audience_id, reference_layer_id):
   a. Resolve template_id = select_template(page_type, reference_layer, audience)
   b. Compute row_key = hash(base_key, reference_layer_id, template_id, evidence_grade)
   c. If row_key exists in cohort → REJECT blocked_thin_duplicate
   d. If template_id identical to sibling with same base_key and same evidence_grade → REJECT
   e. Else EMIT inventory row / draft
```

---

## Examples (valid distinct routes)

| Route A | Route B | Distinction |
| --- | --- | --- |
| bisulfid + ar + researcher + REF_RESEARCH | bisulfid + ar + student + REF_EDUCATIONAL | vocabulary + template + evidence grade |
| bisulfid + ar + AI + REF_TECHNICAL | bisulfid + ar + investor + REF_ECONOMIC | structure + forbidden claims + sources |
| compare bisulfide/bisulfite + linguistic | compare bisulfide/bisulfite + educational | comparison_reference_mode + template |

---

## Examples (invalid — reject)

| Attempt | Reason |
| --- | --- |
| Same term + language + PT_TERM_CANONICAL + REF_KNOWLEDGE + REF_RESEARCH with identical template and grade | Shallow duplicate |
| Audience label swap only with same template output hash | Cosmetic duplicate |
| Copy EN draft to DE without linguistic reference layer sourcing | MT spam / unsourced equivalence |

---

## Template binding enforcement

`SOVEREIGN_TEMPLATE_CONTRACT_MODEL_WAVE_1.json` maps reference_layer → template. Generator **must not** reuse TPL_TERM_CANONICAL_V1 output structure for REF_EDUCATIONAL child pages — must use TPL_CHILD_EDU_V1.

---

## Validation

- G0 inventory: anti_duplication hash unique  
- G4 draft: content hash comparison within cohort sample  
- Human audit: flag pages >85% similar text structure  

---

## Registry reference

- `reference_layer_registry.json` — anti_duplication_rule  
- `SOVEREIGN_ROUTE_GENERATION_MATRIX_WAVE_1.json` — anti_shallow_duplication  
