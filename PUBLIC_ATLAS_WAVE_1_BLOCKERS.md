# Public Atlas Wave 1 — Blockers

## Current Status

**No active blockers.** All 52 Wave 1 pages delivered and validated.

---

## Resolved Blockers

### B1: Output token limit during page generation (RESOLVED)
- **Description:** Initial approach (agent script generation) exceeded the 32K output token maximum.
- **Resolution:** Switched to direct Write tool calls in parallel batches of 3, writing HTML files directly without intermediate scripts.

### B2: Write-before-read error on scaffold files (RESOLVED)
- **Description:** The Write tool requires a prior Read for any existing file. Scaffold overwrite pages each required a Read call before Write.
- **Resolution:** Used parallel Read calls with `limit: 1` before each scaffold overwrite batch.

### B3: terminology/index.html did not exist (RESOLVED)
- **Description:** `site/public/terminology/index.html` was listed in the overwrite batch but the file did not exist in the scaffold. Write tool would have errored if Read was attempted first.
- **Resolution:** Created as a fresh new file (no Read needed). Updated page count arithmetic: 39 new pages (not 38) + 13 scaffold overwrites = 14,041 total.

### B4: Count arithmetic correction (RESOLVED)
- **Description:** Initial sprint plan estimated 14,040 pages (14,002 + 38 new). Actual count was 14,041 due to terminology being a new file, not a scaffold overwrite.
- **Resolution:** Deploy workflow gate updated from 14,040 to 14,041 to match verified actual count.

---

## Wave 2 Considerations

No blockers anticipated for Wave 2, but note:

1. **Count gate is strict:** Any future page additions require updating `pages-public-deploy.yml` count gate.
2. **Scaffold overwrites require Read first:** Any Wave 2 overwrite of existing scaffold pages requires `Read` before `Write`.
3. **Bisulfite boundary:** Future pages mentioning bisulfite must clearly disambiguate from bisulfide in the first paragraph.
4. **Corpus validators:** All new public content must remain under `site/public/` — corpus validators will block any content placed under `main/content/`.

---

## Non-Issues (Documented for Clarity)

- The 14K scaffold pages remain noindex and unlinked — this is intentional and correct.
- The deploy workflow is `workflow_dispatch` only — it does not trigger on push. Manual trigger required after each content push.
- sitemap.xml is served as a static file — no dynamic generation required.
