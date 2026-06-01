#!/usr/bin/env python3
"""L1 GitHub Pages deployment gate validator — read-only, stdlib only (Sprint 6M-H, 6N-C-P1).

Validates that the governed Pages workflow stages site/public/ into a temporary
artifact excluding _integration_sample/, deploys 14,000 foundation pages only,
preserves gate separation, and does not weaken deployment safety.
Does not modify any files.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_PATH = ROOT / ".github/workflows/pages-public-deploy.yml"
PUBLIC_DIR = ROOT / "site/public"
SAMPLE_DIR = ROOT / "site/_sample"
INTEGRATION_SAMPLE_DIR = PUBLIC_DIR / "_integration_sample"
MANIFEST_PATH = PUBLIC_DIR / "public_launch_manifest.json"
CNAME_PATH = PUBLIC_DIR / "CNAME"
NOJEKYLL_PATH = PUBLIC_DIR / ".nojekyll"
DS_ASSETS = PUBLIC_DIR / "assets/bisulfid-design-system"

PUBLIC_LAUNCH_EXACT = 14000


def foundation_public_html_files() -> list[Path]:
    if not PUBLIC_DIR.is_dir():
        return []
    return sorted(
        p for p in PUBLIC_DIR.rglob("index.html")
        if not (p.relative_to(PUBLIC_DIR).parts and p.relative_to(PUBLIC_DIR).parts[0] == "_integration_sample")
    )


def integration_sample_html_files() -> list[Path]:
    if not INTEGRATION_SAMPLE_DIR.is_dir():
        return []
    return sorted(INTEGRATION_SAMPLE_DIR.rglob("index.html"))

FORBIDDEN_WORKFLOW_PATTERNS = (
    re.compile(r"\bnpm\s+install\b", re.I),
    re.compile(r"\bpip\s+install\b", re.I),
    re.compile(r"\bpoetry\s+install\b", re.I),
    re.compile(r"\bbuild\.py\b", re.I),
    re.compile(r"render-public-launch-foundation", re.I),
    re.compile(r"render-quarantined", re.I),
    re.compile(r"\bsecrets\.", re.I),
    re.compile(r"cloudflare", re.I),
    re.compile(r"CLOUDFLARE", re.I),
)

FORBIDDEN_ARTIFACT_PATHS = (
    re.compile(r"path:\s*['\"]?\.", re.I),
    re.compile(r"path:\s*['\"]?site/_sample", re.I),
    re.compile(r"path:\s*['\"]?site['\"]?\s*$", re.I),
    re.compile(r"path:\s*['\"]?main/", re.I),
    re.compile(r"path:\s*['\"]?site/public['\"]?\s*$", re.I),
)

REQUIRED_WORKFLOW_MARKERS = (
    "workflow_dispatch",
    "contents: read",
    "pages: write",
    "id-token: write",
    "site/public",
    "upload-pages-artifact",
    "deploy-pages",
    "_integration_sample",
    "rsync",
    "pages-artifact",
    "artifact_dir",
    "14000",
)

HTML_FORBIDDEN = (
    re.compile(r"index,\s*follow", re.I),
    re.compile(r"<script\s+src=", re.I),
)


def read_workflow() -> str:
    if not WORKFLOW_PATH.is_file():
        return ""
    return WORKFLOW_PATH.read_text(encoding="utf-8")


def validate_workflow(text: str) -> list[str]:
    errors: list[str] = []
    if not text:
        errors.append("pages-public-deploy.yml missing")
        return errors

    for marker in REQUIRED_WORKFLOW_MARKERS:
        if marker not in text:
            errors.append(f"workflow missing required marker: {marker!r}")

    for pattern in FORBIDDEN_WORKFLOW_PATTERNS:
        if pattern.search(text):
            errors.append(f"workflow forbidden pattern: {pattern.pattern}")

    for pattern in FORBIDDEN_ARTIFACT_PATHS:
        if pattern.search(text):
            errors.append(f"workflow may deploy unsafe path: {pattern.pattern}")

    if not re.search(r"--exclude=['\"]?_integration_sample/", text):
        errors.append("workflow must rsync with --exclude='_integration_sample/'")

    if not re.search(r"steps\.stage\.outputs\.artifact_dir", text):
        errors.append("workflow must upload staged artifact_dir, not raw site/public")

    if re.search(r"path:\s*['\"]?site/public['\"]?\s*$", text, re.M):
        errors.append("workflow must not upload site/public directly (use staged artifact)")

    if "environment:" in text and "github-pages" not in text:
        errors.append("workflow should target github-pages environment")

    if re.search(r"on:\s*\n\s*push:", text):
        errors.append("workflow must remain workflow_dispatch only")

    return errors


def find_disallowed_html_outside_public() -> list[str]:
    site = ROOT / "site"
    if not site.is_dir():
        return []
    bad: list[str] = []
    for path in site.rglob("*.html"):
        rel = path.relative_to(site)
        if rel.parts and rel.parts[0] not in ("public", "_sample"):
            bad.append(str(rel))
    return bad


def validate_public_sample(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    lower = text.lower()
    if "noindex" not in lower or "nofollow" not in lower:
        errors.append(f"{path.name}: missing noindex,nofollow")
    if "public launch foundation" not in lower and "public_visible_foundation" not in lower:
        errors.append(f"{path.name}: missing public foundation governance marker")
    if "source approval not implied" not in lower and "no source approval" not in lower:
        errors.append(f"{path.name}: missing source non-approval posture")
    for pattern in HTML_FORBIDDEN:
        if pattern.search(text):
            errors.append(f"{path.name}: forbidden HTML pattern {pattern.pattern}")
    return errors


def main() -> int:
    print("=" * 60)
    print("Bisulfid Pages Deployment Gate Validator — Layer 1")
    print(f"Date: {date.today().isoformat()}")
    print(f"Workflow: {WORKFLOW_PATH.relative_to(ROOT)}")
    print("Mode: read-only")
    print("=" * 60)
    print()

    all_errors: list[str] = []

    wf_text = read_workflow()
    all_errors.extend(validate_workflow(wf_text))

    if not CNAME_PATH.is_file():
        all_errors.append("site/public/CNAME missing")
    else:
        cname = CNAME_PATH.read_text(encoding="utf-8").strip()
        if cname != "bisulfid.com":
            all_errors.append(f"CNAME unexpected value: {cname!r}")
        print(f"CNAME: {cname}")

    if not NOJEKYLL_PATH.is_file():
        all_errors.append("site/public/.nojekyll missing (required for Jekyll bypass)")
    else:
        print(".nojekyll: present")

    if not DS_ASSETS.is_dir():
        all_errors.append("site/public/assets/bisulfid-design-system/ missing")
    else:
        print("Design-system assets: present")

    public_files = foundation_public_html_files()
    integration_files = integration_sample_html_files()
    print(f"Public foundation pages: {len(public_files)}")
    print(f"Integration sample pages (repo only, excluded from deploy): {len(integration_files)}")
    if len(public_files) != PUBLIC_LAUNCH_EXACT:
        all_errors.append(
            f"expected {PUBLIC_LAUNCH_EXACT} public pages, found {len(public_files)}"
        )

    if not MANIFEST_PATH.is_file():
        all_errors.append("public_launch_manifest.json missing")
    else:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        if manifest.get("rendered_count") != PUBLIC_LAUNCH_EXACT:
            all_errors.append("manifest rendered_count != 14000")
        if manifest.get("design_system_refresh") is not True:
            all_errors.append("manifest design_system_refresh not true")
        for gate in ("indexation_gate", "sitemap_gate", "navigation_gate"):
            if manifest.get(gate) != "closed":
                all_errors.append(f"manifest {gate} not closed")

    for artifact in ("sitemap.xml", "sitemap_index.xml", "navigation.html"):
        if (PUBLIC_DIR / artifact).is_file():
            all_errors.append(f"unauthorized artifact under site/public/: {artifact}")

    bad_html = find_disallowed_html_outside_public()
    if bad_html:
        all_errors.append(f"HTML outside site/public/ or site/_sample/: {len(bad_html)}")

    sample_checked = min(20, len(public_files))
    for path in public_files[:sample_checked]:
        all_errors.extend(validate_public_sample(path))
    print(f"Public HTML sample checked: {sample_checked}")

    if wf_text and re.search(r"_sample", wf_text) and "site/public" not in wf_text:
        all_errors.append("workflow references _sample without site/public artifact root")

    print()
    if all_errors:
        print("--- Errors ---")
        for e in all_errors[:30]:
            print(f"  ERROR: {e}")
        if len(all_errors) > 30:
            print(f"  ... and {len(all_errors) - 30} more")
        print()
        print("VALIDATION SUMMARY: FAIL")
        print("=" * 60)
        return 1

    print("VALIDATION SUMMARY: PASS")
    print("=" * 60)
    return 0


if __name__ == "__main__":
    sys.exit(main())
