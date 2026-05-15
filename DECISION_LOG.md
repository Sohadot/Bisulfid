# DECISION LOG

This document records decisions that affect the architecture, doctrine, data, or direction of bisulfid.com.

All structural decisions require an entry here. Changes to doctrine require an entry here.

---

## Log Format

Each entry includes:

- **Date**
- **Sprint / Phase**
- **Decision**
- **Rationale**
- **Doctrine reference** (if applicable)
- **Files affected**

---

## Entries

### 2026-05-15 — Sprint 0A: Doctrine Foundation

**Decision:** Establish the minimum sovereign doctrine foundation for bisulfid.com.

**Rationale:** The README defines bisulfid.com as a Global Sovereign Sulfur Intelligence Gateway with a governed doctrine folder. Before any content, code, or deployment decisions are made, the governing documents that define what this asset is, how it operates, and what conditions must be met before launch must exist in the repository. These documents serve as the single source of truth for all future decisions.

**Doctrine reference:** `ASSET_THESIS.md` — all documents flow from it.

**Files created:**

- `doctrine/ASSET_THESIS.md` — top doctrine document; defines what this asset is.
- `doctrine/PROJECT_DOCTRINE.md` — governs all operations.
- `doctrine/MULTILINGUAL_POLICY.md` — governs language architecture and hreflang integrity.
- `doctrine/GLOBAL_REFERENCE_STANDARD.md` — governs global reference quality.
- `doctrine/SOURCE_POLICY.md` — governs claims and sources.
- `doctrine/QUALITY_GATE.md` — defines the 11 launch conditions.
- `doctrine/SECURITY_POLICY.md` — governs security posture.
- `DECISION_LOG.md` — this document.
- `main/data/languages.json` — machine-readable language registry.

**Not created in this sprint:** frontend UI, HTML, CSS, JS, images, GitHub Actions, scripts, package.json, CURSOR_RULES.md, generated site output, placeholder content pages.
