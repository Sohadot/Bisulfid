# Sovereign Visual Interface Next Actions — Sprint 6N-D

**Date:** 2026-06-01

## Step 1 — Visual proof first (mandatory)

```bash
python scripts/build.py --render-visual-proof-sample
python scripts/validate_visual_proof_sample_l1.py
```

Review these 7 routes under `site/public/_visual_proof_sample/` **with human eyes**:

- `/` (home)
- `/what-is-bisulfid/`
- `/de/core/mos2/` (or mapped path)
- disambiguation map route
- bisulfide cluster route
- sources
- corpus methodology

**Do not proceed** if the proof does not feel like the BISULFID chemical-language control room.

## Step 2 — Approve or iterate

If weak: improve `bisulfid-design-system/` tokens/components → re-run proof only.

If strong: edit `site/public/_visual_proof_sample/visual_proof_manifest.json`:

```json
"visual_review_status": "approved"
```

## Step 3 — Full refresh (only after approval)

```bash
python scripts/build.py --render-public-design-system-refresh --limit 14000
```

Build engine **refuses** full refresh until proof manifest is `approved`.

## Step 4 — Deploy and live check

- Pages public deploy (excludes `_visual_proof_sample/` and `_integration_sample/`)
- Sprint **6M-J** live verification
- Indexation remains **CLOSED**

## Official material identity

**Carbon gray + sulfur yellow + molybdenum silver** — fixed Bisulfid palette for all future visual work.

## Optional follow-ups (after live PASS)

- Missing-E motion enhancement
- Source crystal state refinement
- Relation lattice data-bound expansion
- WebGL prototype — **wait** until CSS/SVG proof passes live
