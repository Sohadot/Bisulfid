#!/usr/bin/env python3
"""test_acquire_page.py — /acquire/ correction (Release-01 PR-B, revision 2): wording and boundaries."""

import json
import os
import re
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import publication_authority as pa  # noqa: E402

PAGE = os.path.join(ROOT, "site", "public", "acquire", "index.html")
LINKS = ["/", "/what-is-bisulfid/", "/bisulfid-vs-bisulfide/", "/languages/", "/glossary/", "/sources/", "/acquire/", "/",
         "/languages/", "/glossary/", "/sources/", "mailto:agent@sohadot.com", "/what-is-bisulfid/",
         "/bisulfid-vs-bisulfide/", "/languages/", "/sources/", "/", "/what-is-bisulfid/", "/bisulfid-vs-bisulfide/",
         "/languages/", "/glossary/", "/sources/"]


def text():
    t = open(PAGE, encoding="utf-8").read()
    return t, " ".join(re.sub(r"<[^>]+>", " ", t).split())


class AcquireRevision2(unittest.TestCase):

    def test_directives_contact_and_links_preserved(self):
        t, _ = text()
        self.assertIn('<meta name="robots" content="noindex, follow">', t)
        self.assertIn('<link rel="canonical" href="https://bisulfid.com/acquire/">', t)
        self.assertEqual(re.findall(r'href="([^"]*)"', t)[3:], LINKS)  # canonical + 2 stylesheets first
        self.assertEqual(pa.Authority().resolve("/acquire/")["robots"], "noindex, follow")

    def test_commercial_availability_kept(self):
        _, s = text()
        for kept in ("Acquire bisulfid.com", "available for acquisition", "Acquisition enquiries:", "There is no listed price."):
            self.assertIn(kept, s)

    def test_no_exhaustive_dictionary_claim(self):
        _, s = text()
        for gone in ("general German dictionaries do not record", "German dictionaries do not record",
                     "English dictionaries and chemical databases"):
            self.assertNotIn(gone, s)
        self.assertIn("this describes that one dictionary, not every German dictionary or technical text", s)

    def test_id_ide_is_a_pattern_not_an_equivalence(self):
        _, s = text()
        self.assertIn("does not by itself establish Bisulfid as the standardized German equivalent of bisulfide", s)
        self.assertNotIn("that choice is deliberate", s)

    def test_terminology_reference_not_presented_as_published(self):
        _, s = text()
        self.assertIn("It has not been published yet", s)
        self.assertNotIn("How the two spellings relate", s)
        self.assertNotIn("documents that question with sources", s)

    def test_owner_approval_still_pending_and_ledger_unchanged(self):
        d = json.load(open(os.path.join(ROOT, "main", "data", "publication", "url_decisions.json")))
        x = next(x for x in d["decisions"] if x["decision_id"] == "URL-DEC-R03-ACQUIRE-001")
        self.assertEqual((x["status"], x["approved_by"], x["approved_on"]), ("proposed", None, None))
        led = json.load(open(os.path.join(ROOT, "main", "data", "release_ledger.json")))
        self.assertEqual(next(r for r in led["records"] if r["route_id"] == "acquire")["release_status"], "blocked")


if __name__ == "__main__":
    unittest.main(verbosity=1)
