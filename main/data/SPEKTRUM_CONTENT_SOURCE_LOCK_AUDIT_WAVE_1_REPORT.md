# Spektrum Content Source-Lock Audit — Wave 1 Report

**Sprint:** 5N-V  
**Date:** 2026-05-30  
**Branch:** `claude/sprint-5n-v-spektrum-content-source-lock-audit`  
**Scope:** Read-only audit of `de_core_mos2` draft against `SRC-SPEKTRUM-MOS2-DE` and `CLM-TERM-MOS2-DE-001`

---

## Why this sprint exists

Sprint **5N-U** approved **`CLM-TERM-MOS2-DE-001`** under **`approval_limited`** posture with **`SRC-SPEKTRUM-MOS2-DE`** bibliographically **`verified`**. The next governed step is to audit whether the **`de_core_mos2`** draft content can be source-locked to that verified source and approved narrow terminology claim — without marker resolution, content rewrite, route publication, or registry source-lock activation.

---

## Pre-flight confirmation

| Check | Result |
| --- | --- |
| Branch based on main after Sprint 5N-U | **Yes** |
| All L1/L2 runtimes (pre) | **PASS** |
| `production_can_safely_proceed` | **no** |
| All corpus locks **LOCKED** | **Yes** |
| `SRC-SPEKTRUM-MOS2-DE` `status` | **verified** |
| `SRC-SPEKTRUM-MOS2-DE` `source_lock_status` | **candidate** |
| `CLM-TERM-MOS2-DE-001` `status` | **approved** |
| `de_core_mos2` draft posture | draft / non_public / non-indexable |
| `[SOURCE REQUIRED]` markers (pre-audit) | **4** occurrences — **present** |
| Content file modified (pre-audit) | **No** |

---

## Audit target

| Artifact | Path / ID |
| --- | --- |
| Route | `de_core_mos2` |
| Content file | `main/content/de/pages/terminology/molybdenum-disulfide.md` |
| Source | `SRC-SPEKTRUM-MOS2-DE` |
| Claim | `CLM-TERM-MOS2-DE-001` |
| Approved boundary | German Lexikon der Chemie dictionary-entry terminology for `de_core_mos2` only |

---

## Content read-only summary

The draft is a **structural Wave 1 boilerplate** page (Sprint 5J pattern). It contains:

- Non-public draft notice with explicit source-locking-required language
- Page role as controlled terminology entry for `de_core_mos2`
- Three terminology-layer placeholders (lexical form, chemical/document form, claim status) — all marked **`[SOURCE REQUIRED]`** or stating no approved claims
- Boundary exclusions (no universal suffix rules, no normative claims, no operating instructions)
- Source/claim status section stating inactive registries, zero approved claims, incomplete source-locking
- Publication blockers and internal reference role

**No factual MoS2 terminology** (e.g. Molybdän(IV)-sulfid spelling, Spektrum lexicon entry text, or document-language examples) appears in the body. All substantive terminology lines await future marker-resolution charter.

---

## Audit findings

### Inside approved boundary

1. **Page role** — Controlled terminology entry scoped to `de_core_mos2` aligns with claim `related_routes` and `allowed_pages`.
2. **Boundary exclusions** — Sections excluding universal suffix rules, normative authority, and operating instructions align with claim `prohibited_uses` and source `do_not_use_for`.
3. **Draft governance posture** — Non-public, non-indexable, non-sitemap language is governance framing, not an expanded claim class.
4. **Publication blockers** — Accurate; route remains `planned`.

### Outside or unsupported boundary

1. **Lexikalische Form** — Placeholder only; no dictionary-entry terminology present to lock. **`[SOURCE REQUIRED]`**.
2. **Chemische / Dokumentform** — Placeholder only; no document-language terminology present to lock. **`[SOURCE REQUIRED]`**.
3. **Abgrenzungen factual binding** — Exclusion framing only; stronger source binding still marked **`[SOURCE REQUIRED]`**.
4. **Excluded claim classes** — No safety, medical, market, production, procurement, pricing, trade, CAGR, industrial, or acquisition content detected (audit PASS on exclusions).

### Registry ↔ content consistency gap

The body states **"Kein Claim ist freigegeben"**, **"Freigegebene Claims: keine"**, and **"keine freigegebenen Claims"**, while **`CLM-TERM-MOS2-DE-001`** is **`approved`** at registry layer. This is a **documentation lag**, not a validator failure (negated phrasing passes draft validators), but it blocks honest source-lock annotation without content body updates.

---

## Source-lock eligibility determination

| Criterion | Assessment |
| --- | --- |
| Verified source available | **Yes** — `SRC-SPEKTRUM-MOS2-DE` verified |
| Approved narrow claim available | **Yes** — `CLM-TERM-MOS2-DE-001` approved |
| Factual terminology content present to lock | **No** — placeholders only |
| Content schema supports partial source-lock metadata | **No** — DE Wave 1 drafts require 9 frontmatter fields only; no governed `source_lock_*` or partial-lock fields |
| Registry `source_lock_status` allows content lock | **No** — remains **`candidate`**; locked status blocked and implies full source-lock per guardrails |
| Body can receive lock annotation without rewrite | **No** — status section contradicts approved claim; correction requires body edit |
| Validators permit "source-locking complete" language | **No** — L0/L1 draft and claim validators **error** on unnegated source-locking-complete claims |
| Marker removal required for lock | **Would be** — factual lines remain `[SOURCE REQUIRED]`; lock without markers is incomplete |

---

## Audit verdict

**Content source-locking: DEFERRED**

Source-locking is **not applied** in this sprint. Audit documentation records readiness at registry layer and blockers at content/schema/guardrail layer.

**Primary blockers:**

1. No governed content schema for non-public partial source-lock metadata on DE Wave 1 drafts.
2. Draft body contains no factual terminology lines to lock — only `[SOURCE REQUIRED]` placeholders.
3. Body source/claim status section is stale relative to approved claim; reconciling requires content body edit (out of scope).
4. Registry `source_lock_status: candidate` — full source-lock not authorized; changing to `locked` is explicitly out of scope.
5. L1 validators block content implying source-locking complete or unqualified claim approval.

---

## Recommended next charter

1. **Content schema extension** (if desired) — governed partial source-lock frontmatter values under separate sprint.
2. **Marker resolution sprint** — populate narrow dictionary-entry terminology from Spektrum boundary; separate from source-lock audit.
3. **Registry source-lock sprint** — only after content and markers align; `source_lock_status: locked` remains blocked until then.

---

## Related documents

- `SPEKTRUM_CONTENT_BOUNDARY_MATRIX_WAVE_1.md`
- `SPEKTRUM_CONTENT_SOURCE_LOCK_NO_MARKER_REMOVAL_NO_PUBLICATION_WAVE_1.md`
- `SPEKTRUM_CONTENT_SOURCE_LOCK_AUDIT_VALIDATION_REPORT.md`
- `SPEKTRUM_APPROVED_CLAIM_TRANSITION_WAVE_1_REPORT.md` (5N-U)
