# Sovereign Generator — No Publication Guardrail — Wave 1

**Sprint:** 6C  
**Posture:** Generator schema and template design only — no execution

---

## Sprint boundary

| Action | Performed? |
| --- | --- |
| Generator schema designed | **Yes** |
| Template contracts defined | **Yes** |
| Knowledge reliability model defined | **Yes** (scope amendment) |
| Evidence grade registry | **Yes** |
| Source hierarchy model | **Yes** |
| Validation gates specified | **Yes** |
| Pages generated | **No** |
| Content files created | **No** |
| Public HTML | **No** |
| routes.json modified | **No** |
| indexable / sitemap / navigation | **No** |

---

## Generator output locks (6D defaults)

Every future generated draft **must** have:

```yaml
status: draft
publication_status: non_public
indexable: false
in_sitemap: false
noindex_default: true
evidence_grade: <from registry — not upgraded>
knowledge_reliability_level: L2_draft_cautious minimum
```

---

## Forbidden generator behaviors

- Free-form LLM generation without registry binding  
- Publish routes or set indexable true  
- Remove [SOURCE REQUIRED] markers  
- Approve claims or register sources  
- Present draft as final without reliability notice  
- Hide excluded_claim_classes  
- Upgrade evidence_grade without registry change  
- Generate public HTML in 6D without separate charter  

---

## Governance unchanged

| Gate | Status |
| --- | --- |
| production_can_safely_proceed | **no** |
| routes.json | **126 rows — unchanged** |
| Existing validators | **not weakened** |
| Workflows / packages | **unchanged** |

---

## Epistemic guardrail

Generator design enforces: **never convert absence of evidence into factual conclusion.**

Weak-evidence pages remain **noindex / non-public** unless explicit status-page charter.
