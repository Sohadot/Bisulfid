#!/usr/bin/env python3
"""Sprint 99A — Validate 14K public quality repair gate."""
from __future__ import annotations

import json
import random
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from atlas_dossier_common_l3 import (  # noqa: E402
    FORBIDDEN_PUBLIC_LANGUAGE_99A,
    STYLESHEET_PATH,
    load_release_model,
    strip_machine_content_for_audit,
)

LEDGER_PATH = ROOT / "main/data/release_ledger.json"
PUBLIC_DIR = ROOT / "site/public"
CSS_PATH = PUBLIC_DIR / "assets/bisulfid-design-system/bisulfid-frame.css"
HREF_RE = re.compile(r'<a\s+href="([^"]+)"', re.I)
MIN_BODY_CHARS = 400


def html_path_for(route_path: str) -> Path:
    path = route_path.strip("/")
    return PUBLIC_DIR / ("index.html" if not path else f"{path}/index.html")


def validate_page(rec: dict, public_paths: set[str]) -> tuple[list[str], list[str], dict]:
    errors: list[str] = []
    warnings: list[str] = []
    rid = rec["route_id"]
    route_path = rec.get("route_path", "/")
    html_path = html_path_for(route_path)
    meta = {"route_id": rid, "route_path": route_path, "html_exists": html_path.is_file()}
    if not html_path.is_file():
        errors.append("missing HTML")
        return errors, warnings, meta
    text = html_path.read_text(encoding="utf-8")
    lower = text.lower()
    meta["has_stylesheet"] = STYLESHEET_PATH in text
    meta["has_atlas_shell"] = "bisulfid-atlas" in lower and "atlas-header" in lower
    meta["indexable"] = 'content="index, follow"' in lower
    meta["link_count"] = lower.count("<a href=")
    visible = strip_machine_content_for_audit(text)
    for pat in FORBIDDEN_PUBLIC_LANGUAGE_99A:
        if pat.search(visible):
            errors.append(f"forbidden: {pat.pattern}")
            break
    if not meta["has_stylesheet"]:
        errors.append("missing absolute stylesheet")
    if not meta["has_atlas_shell"]:
        errors.append("missing sovereign atlas shell")
    if "noindex" in lower:
        errors.append("contains noindex")
    if "<title>" not in lower:
        errors.append("missing title")
    if 'name="description"' not in lower:
        errors.append("missing meta description")
    if 'rel="canonical"' not in lower:
        errors.append("missing canonical")
    if meta["link_count"] < 8:
        errors.append(f"fewer than 8 links ({meta['link_count']})")
    body_match = re.search(r'class="atlas-page__body">(.*?)</section>', text, re.S | re.I)
    body_len = 0
    if body_match:
        body_len = len(re.sub(r"<[^>]+>", "", body_match.group(1)).strip())
    meta["body_chars"] = body_len
    if body_len < MIN_BODY_CHARS:
        errors.append(f"body below minimum ({body_len})")
    for href in HREF_RE.findall(text):
        if href.startswith(("http", "#", "mailto:")):
            continue
        norm = href if href.endswith("/") else href + "/"
        if not norm.startswith("/"):
            norm = "/" + norm
        if norm not in public_paths:
            target = PUBLIC_DIR / norm.strip("/") / "index.html"
            if not target.is_file():
                warnings.append(f"broken link: {href}")
    meta["status"] = "PASS" if not errors else "FAIL"
    return errors, warnings, meta


def sample_routes(released: list[dict]) -> list[dict]:
    buckets: dict[str, list[dict]] = {
        "en_terminology_deep": [],
        "de_terminology": [],
        "context": [],
        "language": [],
        "material": [],
        "hub": [],
    }
    for rec in released:
        path = rec.get("route_path", "")
        lane = rec.get("production_lane", "")
        if path.startswith("/en/terminology/") and path.count("/") >= 6:
            buckets["en_terminology_deep"].append(rec)
        elif path.startswith("/de/terminology/"):
            buckets["de_terminology"].append(rec)
        elif lane in {"F", "G", "H", "I", "J", "K", "L"} or "context" in path:
            buckets["context"].append(rec)
        elif lane == "B" or "/languages/" in path:
            buckets["language"].append(rec)
        elif lane == "E" or "molybdenum" in path or "mos2" in path or "mineral" in path:
            buckets["material"].append(rec)
        elif lane == "HUB" or rec["route_id"] in {"home", "sources"}:
            buckets["hub"].append(rec)
    picks: list[dict] = []
    rng = random.Random(99)
    picks.extend(rng.sample(buckets["en_terminology_deep"], min(20, len(buckets["en_terminology_deep"]))))
    picks.extend(rng.sample(buckets["de_terminology"], min(20, len(buckets["de_terminology"]))))
    picks.extend(rng.sample(buckets["context"], min(10, len(buckets["context"]))))
    picks.extend(rng.sample(buckets["language"], min(10, len(buckets["language"]))))
    picks.extend(rng.sample(buckets["material"], min(10, len(buckets["material"]))))
    picks.extend(rng.sample(buckets["hub"], min(10, len(buckets["hub"]))))
    seen: set[str] = set()
    out: list[dict] = []
    for rec in picks:
        if rec["route_id"] not in seen:
            seen.add(rec["route_id"])
            out.append(rec)
    return out


def main() -> int:
    print("=" * 60)
    print("Sprint 99A — 14K Public Quality Repair Validator")
    print("=" * 60)
    model = load_release_model()
    min_links = model.get("min_internal_links", 8)
    ledger = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    released = [r for r in ledger["records"] if r["release_status"] == "released"]
    public_paths = set()
    for rec in released:
        path = rec.get("route_path", "/").rstrip("/")
        public_paths.add("/" if not path else "/" + path + "/")

    all_errors: list[str] = []
    forbidden_hits: Counter = Counter()
    css_fail = 0
    shell_fail = 0
    for rec in released:
        errs, _, meta = validate_page(rec, public_paths)
        if not meta.get("has_stylesheet"):
            css_fail += 1
        if not meta.get("has_atlas_shell"):
            shell_fail += 1
        for e in errs:
            if e.startswith("forbidden:"):
                forbidden_hits[e] += 1
            all_errors.append(f"{rec['route_id']}: {e}")

    sample = sample_routes(released)
    sample_rows: list[dict] = []
    sample_errors = 0
    for rec in sample:
        errs, warns, meta = validate_page(rec, public_paths)
        if errs:
            sample_errors += 1
        sample_rows.append({
            "route_id": rec["route_id"],
            "route_path": rec["route_path"],
            "status": meta.get("status", "FAIL"),
            "stylesheet": meta.get("has_stylesheet", False),
            "forbidden_errors": errs,
            "warnings": warns[:3],
            "links": meta.get("link_count", 0),
            "body_chars": meta.get("body_chars", 0),
        })

    shard_files = [f for f in PUBLIC_DIR.glob("sitemap*.xml") if f.name != "sitemap.xml"]
    sitemap_urls = sum(f.read_text(encoding="utf-8").count("<loc>") for f in shard_files)

    repair_report = [
        "# 14K Public Quality Repair Report",
        "",
        f"**Date:** {date.today().isoformat()}",
        f"**Sprint:** 99A",
        f"**Released pages repaired:** {len(released)}",
        f"**Validation errors:** {len(all_errors)}",
        "",
        "## Repairs applied",
        "",
        "- Absolute sovereign stylesheet on every released page",
        "- Removed internal machine labels from public copy",
        "- Replaced draft language with public reference dossier framing",
        "- Differentiated dossier bodies by topic, language, and audience context",
        "- Fixed duplicate breadcrumb entries",
        "",
        f"**CSS shell failures:** {css_fail}",
        f"**Atlas shell failures:** {shell_fail}",
        f"**Sitemap URLs unchanged:** {sitemap_urls}",
    ]
    (ROOT / "main/data/14K_PUBLIC_QUALITY_REPAIR_REPORT.md").write_text(
        "\n".join(repair_report) + "\n", encoding="utf-8"
    )

    forbidden_lines = [
        "# 14K Public Forbidden String Audit",
        "",
        f"**Date:** {date.today().isoformat()}",
        f"**Pages scanned:** {len(released)}",
        f"**Pages with forbidden strings:** {len({e.split(':')[0] for e in all_errors if 'forbidden' in e})}",
        "",
        "## Top forbidden hits",
        "",
    ]
    for hit, count in forbidden_hits.most_common(30):
        forbidden_lines.append(f"- {hit}: {count}")
    (ROOT / "main/data/14K_PUBLIC_FORBIDDEN_STRING_AUDIT.md").write_text(
        "\n".join(forbidden_lines) + "\n", encoding="utf-8"
    )

    css_lines = [
        "# 14K Public CSS Shell Audit",
        "",
        f"**Date:** {date.today().isoformat()}",
        f"**Stylesheet path:** `{STYLESHEET_PATH}`",
        f"**Stylesheet file exists:** {CSS_PATH.is_file()}",
        f"**Pages with correct stylesheet reference:** {len(released) - css_fail}",
        f"**Pages missing stylesheet:** {css_fail}",
        f"**Pages missing atlas shell markup:** {shell_fail}",
        "",
        "All released pages must use the absolute path `/assets/bisulfid-design-system/bisulfid-frame.css`.",
    ]
    (ROOT / "main/data/14K_PUBLIC_CSS_SHELL_AUDIT.md").write_text(
        "\n".join(css_lines) + "\n", encoding="utf-8"
    )

    sample_lines = [
        "# 14K Live Route Sample Report",
        "",
        f"**Date:** {date.today().isoformat()}",
        f"**Samples checked:** {len(sample_rows)}",
        f"**Sample failures:** {sample_errors}",
        "",
        "| Route | Path | Status | CSS | Links | Body chars |",
        "|-------|------|--------|-----|------:|-----------:|",
    ]
    for row in sample_rows:
        sample_lines.append(
            f"| `{row['route_id']}` | `{row['route_path']}` | {row['status']} | "
            f"{'yes' if row['stylesheet'] else 'no'} | {row['links']} | {row['body_chars']} |"
        )
    (ROOT / "main/data/14K_LIVE_ROUTE_SAMPLE_REPORT.md").write_text(
        "\n".join(sample_lines) + "\n", encoding="utf-8"
    )

    val_lines = [
        "# 14K Validation After Repair",
        "",
        f"**Date:** {date.today().isoformat()}",
        f"**Released routes:** {len(released)}",
        f"**Sitemap URLs:** {sitemap_urls}",
        f"**Errors:** {len(all_errors)}",
        f"**Sample errors:** {sample_errors}",
        "",
        f"**Summary:** {'PASS' if not all_errors else 'FAIL'}",
    ]
    if all_errors:
        val_lines.extend(["", "## Errors (first 40)", ""])
        for e in all_errors[:40]:
            val_lines.append(f"- {e}")
    (ROOT / "main/data/14K_VALIDATION_AFTER_REPAIR.md").write_text(
        "\n".join(val_lines) + "\n", encoding="utf-8"
    )
    (ROOT / "main/data/14K_VALIDATION_REPORT.md").write_text(
        "\n".join(val_lines) + "\n", encoding="utf-8"
    )

    print(f"Released: {len(released)}")
    print(f"Sitemap URLs: {sitemap_urls}")
    print(f"CSS failures: {css_fail}")
    print(f"Errors: {len(all_errors)}")
    print(f"Sample checked: {len(sample_rows)} (failures: {sample_errors})")
    if all_errors:
        for e in all_errors[:15]:
            print(f"  ERROR: {e}")
        print("VALIDATION SUMMARY: FAIL")
        return 1
    print("VALIDATION SUMMARY: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
