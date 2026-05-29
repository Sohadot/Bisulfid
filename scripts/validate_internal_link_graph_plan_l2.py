#!/usr/bin/env python3
"""L2 internal link graph plan validator — read-only, stdlib only (Sprint 5O-A)."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

LINK_MODEL_PATH = ROOT / "main/data/CORPUS_PRODUCTION_LINK_GRAPH_MODEL.md"
ROUTES_PATH = ROOT / "main/data/routes.json"
INTERNAL_LINKS_PATH = ROOT / "main/data/internal_links.json"

REQUIRED_SECTIONS = (
    "hub-to-record",
    "record-to-disambiguation",
    "disambiguation-to-source",
    "forbidden link",
    "unpublished route",
    "broken-link",
    "multilingual map",
    "index/map",
)

FORBIDDEN_PLAN = (
    re.compile(r"unpublished\s+routes?\s+(are|is)\s+live", re.I),
    re.compile(r"broken\s+public\s+links?\s+allowed", re.I),
    re.compile(r"publication-ready\s+without\s+internal\s+link", re.I),
)


def run_validation() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not LINK_MODEL_PATH.exists():
        errors.append("Missing CORPUS_PRODUCTION_LINK_GRAPH_MODEL.md")
        return errors, warnings

    text = LINK_MODEL_PATH.read_text(encoding="utf-8")
    lower = text.lower()

    if "internal link" not in lower and "link graph" not in lower:
        errors.append("Link graph model must treat internal linking as required before publication")

    for section in REQUIRED_SECTIONS:
        key = section.replace("-", " ").replace("/", " ")
        if (
            section not in lower
            and key not in lower
            and section.replace("-", "_") not in lower
        ):
            errors.append(f"Link graph model missing required topic: {section}")

    for pat in FORBIDDEN_PLAN:
        if pat.search(text):
            errors.append(f"Forbidden link plan pattern: {pat.pattern}")

    if "route_id" not in lower:
        errors.append("Link graph planning must prefer route_id references in planning stages")

    for role in ("hub", "terminology record", "disambiguation", "source", "governance", "index"):
        if role not in lower:
            warnings.append(f"Link graph model may not cover role: {role}")

    if ROUTES_PATH.exists():
        routes = json.loads(ROUTES_PATH.read_text(encoding="utf-8"))["routes"]
        published = [r["route_id"] for r in routes if r.get("status") == "published"]
        if published:
            errors.append(f"Published routes exist during L2 planning lock: {published[:5]}")

    if INTERNAL_LINKS_PATH.exists():
        links = json.loads(INTERNAL_LINKS_PATH.read_text(encoding="utf-8"))
        if links.get("status") not in ("inactive", "planned", None):
            warnings.append(f"internal_links.json status is {links.get('status')!r}")
        edges = links.get("edges", links.get("links", []))
        if isinstance(edges, list) and edges:
            for edge in edges[:20]:
                target = edge.get("target_route_id") or edge.get("to") or edge.get("target")
                if target and ROUTES_PATH.exists():
                    routes = json.loads(ROUTES_PATH.read_text(encoding="utf-8"))["routes"]
                    by_id = {r["route_id"]: r for r in routes}
                    if target in by_id and by_id[target].get("status") != "published":
                        pass  # planned targets OK in planning graph
    else:
        warnings.append("internal_links.json not found")

    return errors, warnings


def main() -> int:
    errors, warnings = run_validation()
    print("=== Internal Link Graph Plan L2 Validation ===")
    if errors:
        print("FAIL — errors:")
        for e in errors:
            print(f"  - {e}")
    else:
        print("PASS — no blocking errors")
    if warnings:
        print("\nWarnings:")
        for w in warnings:
            print(f"  - {w}")
    print(f"\nSummary: {'FAIL' if errors else 'PASS'} ({len(errors)} errors, {len(warnings)} warnings)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
