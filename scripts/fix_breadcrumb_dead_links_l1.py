#!/usr/bin/env python3
"""Rewrite dead intermediate breadcrumb links to plain text.

Historic renders emitted a ``<a href="/ancestor/">`` link for every breadcrumb
ancestor, even when that ancestor directory has no ``index.html``. Crawlers
follow those links and receive a 404 (observed in Search Console as
"Introuvable (404)" on directory URLs such as ``/en/terminology/``).

This pass repairs the already-published HTML in ``site/public`` without
re-rendering (which would revert later hand-tuned hub refinements): inside each
page's ``<ol class="breadcrumb-list">`` it converts every anchor whose target
path has no generated ``index.html`` into a plain ``<span>``. The current page
marker and links to real pages are left untouched. The renderers themselves are
fixed separately (``build_breadcrumbs`` now takes a valid-path set), so future
builds never reintroduce these dead links.

Idempotent: re-running produces no further changes.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_DIR = ROOT / "site/public"

BREADCRUMB_OL_RE = re.compile(
    r'(<ol class="breadcrumb-list">)(.*?)(</ol>)', re.S
)
# <li><a href="/some/path/">Label</a></li>  (breadcrumb ancestor anchors only)
ANCHOR_LI_RE = re.compile(
    r'<li><a href="(/[^"]*)">(.*?)</a></li>', re.S
)


def valid_page_paths() -> set[str]:
    """All directory paths under site/public that contain an index.html.

    Paths are normalised without leading/trailing slashes; the site root is the
    empty string.
    """
    paths: set[str] = set()
    for index in PUBLIC_DIR.rglob("index.html"):
        rel = index.parent.relative_to(PUBLIC_DIR).as_posix()
        paths.add("" if rel == "." else rel)
    return paths


def href_to_path(href: str) -> str:
    return href.strip("/")


def repair_html(text: str, valid: set[str]) -> tuple[str, int]:
    unlinked = 0

    def fix_block(block: re.Match) -> str:
        nonlocal unlinked

        def fix_anchor(a: re.Match) -> str:
            nonlocal unlinked
            href, label = a.group(1), a.group(2)
            if href_to_path(href) in valid:
                return a.group(0)
            unlinked += 1
            return f"<li><span>{label}</span></li>"

        inner = ANCHOR_LI_RE.sub(fix_anchor, block.group(2))
        return block.group(1) + inner + block.group(3)

    new_text = BREADCRUMB_OL_RE.sub(fix_block, text)
    return new_text, unlinked


def main() -> int:
    valid = valid_page_paths()
    print(f"Valid page paths on disk: {len(valid)}")
    files_changed = 0
    total_unlinked = 0
    for index in PUBLIC_DIR.rglob("index.html"):
        text = index.read_text(encoding="utf-8")
        if 'class="breadcrumb-list"' not in text:
            continue
        new_text, unlinked = repair_html(text, valid)
        if unlinked:
            index.write_text(new_text, encoding="utf-8")
            files_changed += 1
            total_unlinked += unlinked
    print(f"Files repaired: {files_changed}")
    print(f"Dead breadcrumb links converted to text: {total_unlinked}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
