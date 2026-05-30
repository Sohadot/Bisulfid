# COHORT_02 Full Draft Quality / Anti-Thin / Anti-Blog Validation Report

**Sprint:** 6I  
**Date:** 2026-05-30  
**Scope:** 902 non-public COHORT_02 terminology drafts  
**Validator:** `generate_cohort_02_full_draft_wave_v1.py` inline quality scan + post-generation corpus scan

---

## Verdict

**PASS** — all 902 drafts meet minimum governed draft quality thresholds. No thin pages. No blog-style pages detected.

---

## Anti-thin checks

| Check | Threshold | Result |
| --- | --- | --- |
| Minimum word count (standard page types) | ≥ 180 words | **PASS** (min 311) |
| Minimum word count (PT_CHILD_SAFE_EDU) | ≥ 150 words | **PASS** (min 311) |
| `[SOURCE REQUIRED]` marker present | Required | **PASS** (902/902) |
| Source and claim status section | Required | **PASS** (902/902) |
| Publication blockers section | Required | **PASS** (902/902) |
| Reliability notice table | Required | **PASS** (902/902) |
| Unresolved fields disclosed | Required | **PASS** (902/902) |
| Excluded claim classes listed | Required | **PASS** (902/902) |

---

## Anti-blog checks

| Check | Result |
| --- | --- |
| No narrative blog framing ("In this post", "Today we explore") | **PASS** |
| No opinion/editorial voice | **PASS** |
| No unsupported chemical assertions | **PASS** |
| No market/CAGR/pricing/procurement language in narrative | **PASS** |
| No safety/handling/medical instruction language | **PASS** |
| No experiment or lab procedure guidance (child-safe type) | **PASS** |
| No markdown hyperlinks | **PASS** (0 found) |
| No raw URLs | **PASS** (0 found) |
| No fake "published" posture | **PASS** (all `non_public`) |

---

## Page-type-specific posture verification

| page_type_id | Count | Posture verified |
| --- | ---: | --- |
| PT_TERM_CANONICAL | 300 | Terminology boundary only; no operational instruction |
| PT_AUDIENCE_EXPLAINER | 250 | Audience vocabulary framing; no meaning upgrade |
| PT_COMPOUND_ENTITY | 128 | Naming/identity boundary; no performance claims |
| PT_AI_READABLE | 100 | Structured provenance YAML; no inferred facts |
| PT_CHILD_SAFE_EDU | 76 | Child-safe notice; no experiments/hazards |
| PT_DIFFERENCE_COMPARISON | 48 | Per-side source/claim table; no winner claims |

---

## Duplication assessment

Drafts share structural templates by design (registry-constrained engine). Content varies by:

- `route_id`, `term_or_entity`, `page_type_id`, `audience_id`, `reference_layer_id`
- Page-purpose bullets and H1/title per page type
- Comparison-side tables where applicable
- Internal-link placeholder lists per inventory row

No shallow duplicate rejection triggered. Structural similarity is expected for governed draft waves; each file maps 1:1 to a unique inventory row and route_id.

---

## Forbidden phrase scan (narrative)

Engine rejects forbidden narrative phrases unless negated in context. Post-generation scan: **0 violations** across 902 files.

---

## Summary

| Metric | Value |
| --- | ---: |
| Drafts scanned | 902 |
| Thin page failures | 0 |
| Blog-style failures | 0 |
| Quality failures | 0 |
| **Overall** | **PASS** |
