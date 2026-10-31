#!/usr/bin/env python3
"""test_bisulfid_reference.py — KO-BISULFID-TERMINOLOGY-001 reference depth and precision (Release-01 PR-E)."""

import copy
import json
import os
import re
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import render_ko_reference as rk  # noqa: E402

SPEC_P = os.path.join(ROOT, "main", "data", "reference_production", "render_specs", "KO-BISULFID-TERMINOLOGY-001.json")
STAGED = os.path.join(ROOT, "main", "data", "release", "staged", "bisulfid-vs-bisulfide", "index.html")
MOS2 = os.path.join(ROOT, "main", "data", "release", "staged", "molybdenum-disulfide", "index.html")


def spec():
    return json.load(open(SPEC_P, encoding="utf-8"))


def page_text():
    t = open(STAGED, encoding="utf-8").read()
    return t, " ".join(re.sub(r"<[^>]+>", " ", t).split())


class Precision(unittest.TestCase):

    def test_headings_are_limited_to_their_sources(self):
        heads = [m["heading"] for m in spec()["modules"]]
        self.assertFalse([h for h in heads if "not in the dictionary" in h or h.lower().startswith("german bisulfid is")])
        bis = next(m for m in spec()["modules"] if m["module_id"] == "de_bisulfid")
        self.assertIn("DWDS", bis["heading"])

    def test_no_equivalence_or_exhaustive_absence_wording(self):
        _, s = page_text()
        for bad in ("same underlying compound", "is the German spelling of bisulfide", "German dictionaries do not record",
                    "general German lexicography does not record", "German dictionaries consulted record Sulfid but not Bisulfid"):
            self.assertNotIn(bad, s)
        self.assertIn("it explains a spelling, not which species a word denotes", s)
        self.assertNotIn("the meaning is the same", s)
        self.assertIn("Not to be inferred from similar spelling", s)

    def test_all_named_terms_are_covered(self):
        _, s = page_text()
        for term in ("Bisulfid", "bisulfide", "Sulfid", "sulfide", "disulfide", "hydrosulfide", "Hydrogensulfid",
                     "bisulfite", "sulfanide", "disulfide(2−)", "hydrogensulfite"):
            self.assertIn(term, s)


class Synthesis(unittest.TestCase):

    def test_three_verdict_groups_with_ko_evidence(self):
        r = rk.build(spec())
        self.assertEqual([g["verdict"] for g in r["synthesis"]["groups"]], ["supported", "open", "not_inferable"])
        ko = set(r["ko"]["evidence_ids"]) | set(r["ko"]["boundary_evidence_ids"])
        for g in r["synthesis"]["groups"]:
            for it in g["items"]:
                self.assertTrue(set(it["evidence_ids"]) <= ko)
                self.assertNotIn("{{", it["text"])

    def test_synthesis_refuses_foreign_evidence_and_unknown_verdicts(self):
        s = spec()
        bad = copy.deepcopy(s)
        bad["synthesis"]["groups"][0]["items"][0]["evidence_ids"] = ["EVD-MOS2-FORMULA-PUBCHEM"]
        with self.assertRaises(rk.RenderError):
            rk.build(bad)
        bad = copy.deepcopy(s)
        bad["synthesis"]["groups"][0]["verdict"] = "proven"
        with self.assertRaises(rk.RenderError):
            rk.build(bad)
        bad = copy.deepcopy(s)
        bad["synthesis"]["groups"][0]["items"][0]["evidence_ids"] = []
        with self.assertRaises(rk.RenderError):
            rk.build(bad)


class EvidenceNavigation(unittest.TestCase):

    def test_every_evidence_link_has_a_row(self):
        t, _ = page_text()
        links = set(re.findall(r'href="#(ev-[^"]+)"', t))
        ids = set(re.findall(r'id="(ev-[^"]+)"', t))
        self.assertTrue(links)
        self.assertEqual(links - ids, set())

    def test_reverification_shown_and_refused_when_a_passage_is_missing(self):
        t, _ = page_text()
        self.assertIn("every quoted passage re-verified 2026-10-31", t)
        cap_p = os.path.join(ROOT, *spec()["reverified_by"].split("/"))
        cap = json.load(open(cap_p, encoding="utf-8"))
        cap["captures"]["SRC-MW-BISULFIDE"]["passages"][0]["found"] = False
        tmp = os.path.join(ROOT, "main", "data", "evidence", "captures", "_test_broken_recapture.json")
        json.dump(cap, open(tmp, "w", encoding="utf-8"))
        try:
            bad = dict(spec(), reverified_by="main/data/evidence/captures/_test_broken_recapture.json")
            with self.assertRaises(rk.RenderError):
                rk.build(bad)
        finally:
            os.unlink(tmp)

    def test_valence_filter_display_only(self):
        self.assertEqual(rk._f_valence("Hydrogensulfide (MIHS) and Sulfide (MI2S)"), "Hydrogensulfide (MᴵHS) and Sulfide (Mᴵ₂S)")


class Isolation(unittest.TestCase):

    def test_mos2_reference_is_unaffected(self):
        t = open(MOS2, encoding="utf-8").read()
        self.assertNotIn("what-the-sources-support", t)
        self.assertNotIn('href="#ev-', t)
        self.assertNotIn("re-verified", t)

    def test_route_and_canonical_unchanged(self):
        t, _ = page_text()
        self.assertIn('<link rel="canonical" href="https://bisulfid.com/bisulfid-vs-bisulfide/">', t)
        self.assertEqual(spec()["canonical_route_id"], "bisulfid_vs_bisulfide")


if __name__ == "__main__":
    unittest.main(verbosity=1)
