# Content Drafts L0 Validation Report

**Sprint:** 5J  
**Validation date:** 2026-05-27

---

## Validator

| Field | Value |
| --- | --- |
| Validator file | `scripts/validate_content_drafts_l0.py` |
| Mode | Read-only (stdlib only) |
| Network | Not required |

---

## Files checked

- `main/data/routes.json` (registry reference)
- `main/data/DRAFT_PRODUCTION_WAVE_1_MANIFEST.md` (target list)
- **50** wave-1 draft Markdown files under `main/content/`

---

## Summary counts

| Metric | Value |
| --- | ---: |
| Routes in registry | **126** |
| Drafts expected (wave 1) | **50** |
| Drafts created | **50** |
| Draft-backed routes before wave 1 | **18** |
| Draft-backed routes after wave 1 | **68** |

---

## Validation results

| Check | Result |
| --- | --- |
| Draft files exist at registered paths | **PASS** |
| Frontmatter required fields | **PASS** |
| `route_id` matches `routes.json` | **PASS** |
| `language` / `locale` / `source_language` match | **PASS** |
| `status: draft` | **PASS** |
| `publication_status: non_public` | **PASS** |
| `indexable: false` | **PASS** |
| `in_sitemap: false` | **PASS** |
| Raw URLs | **PASS** — none detected |
| Markdown links | **PASS** — none detected |
| `[SOURCE REQUIRED]` markers | **PASS** — present on all wave-1 drafts |
| Banned / risky frame screen | **PASS** — negated non-goals handled correctly |
| Content file overwrite | **PASS** — no existing files overwritten |
| `routes.json` modified | **PASS** — not modified in Sprint 5J |

---

## Unresolved warnings

**None.**

---

## Final validation conclusion

**PASS**

Sprint 5J draft production wave 1 meets L0 content validation requirements. Fifty non-public drafts exist at exact `content_file` paths, with correct frontmatter, source markers, and boundary discipline.

---

*Generated from `py scripts/validate_content_drafts_l0.py` — 2026-05-27*
