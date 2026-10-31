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


class BuyerAccessIndexingPolicy(unittest.TestCase):
    """IDX-POL-ACQUIRE-001: /acquire/ is a commercial access page, permanently 'noindex, follow' and out of
    sitemaps, accessible by direct URL; indexing is decided separately from access and publication."""

    POL = os.path.join(ROOT, "main", "data", "publication", "indexing_policies.json")

    def test_policy_record_is_owner_confirmed_without_a_manufactured_signature(self):
        p = json.load(open(self.POL))["policies"]
        self.assertEqual([x["path"] for x in p], ["/acquire/"])
        x = p[0]
        self.assertEqual((x["page_class"], x["indexing"], x["status"]), ("commercial_access", "noindex, follow", "owner_confirmed_policy"))
        self.assertIsNone(x["provenance"]["formal_signature"])
        self.assertNotIn("approved_by", x)

    def test_access_and_canonical_unchanged_by_the_ceiling(self):
        r = pa.Authority().resolve("/acquire/")
        self.assertTrue(r["render"], "the page stays accessible")
        self.assertEqual((r["robots"], r["sitemap"], r["canonical"], r["policy_enforced"]),
                         ("noindex, follow", False, "/acquire/", True))

    def test_future_ledger_release_does_not_make_it_indexable(self):
        a = pa.Authority()
        a.ledger["acquire"] = dict(a.ledger["acquire"], release_status="released", blockers=[])
        r = a.resolve("/acquire/")
        self.assertFalse(r["ledger_enforced"])
        self.assertEqual((r["robots"], r["sitemap"]), ("noindex, follow", False))
        a.ceilings = {}
        self.assertEqual(a.resolve("/acquire/")["robots"], "index, follow",
                         "without the policy a released ledger would restore index: the policy is what decouples them")

    def test_contract_c_or_r11_cannot_lift_the_ceiling(self):
        green = {"governance": "governed", "evidence": "evidence_not_required", "claim": "claim_not_required",
                 "validation": "validated", "ig": "ig_not_required", "release": "authorized", "non_factual_class_certified": True}
        a = pa.Authority(postures_override={"/acquire/": (green, "simulated R11")})
        self.assertEqual(a.contract_c("/acquire/")[0], ("public_indexable", "index_approved"))
        self.assertEqual((a.resolve("/acquire/")["robots"], a.resolve("/acquire/")["sitemap"]), ("noindex, follow", False))

    def test_ceiling_is_refused_for_reference_routes_and_wrong_classes(self):
        import tempfile
        bad = {"policies": [
            {"policy_id": "X1", "path": "/molybdenum-disulfide/", "page_class": "commercial_access", "indexing": "noindex, follow", "status": "owner_confirmed_policy"},
            {"policy_id": "X2", "path": "/what-is-bisulfid/", "page_class": "reference", "indexing": "noindex, follow", "status": "owner_confirmed_policy"},
            {"policy_id": "X3", "path": "/glossary/", "page_class": "commercial_access", "indexing": "noindex, follow", "status": "proposed"}]}
        f = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False)
        json.dump(bad, f)
        f.close()
        try:
            a = pa.Authority(indexing_policies_path=f.name)
        finally:
            os.unlink(f.name)
        self.assertEqual(a.ceilings, {})
        self.assertEqual(len(a.ceiling_errors), 3)
        self.assertEqual(a.resolve("/what-is-bisulfid/")["robots"], "index, follow")

    def test_no_other_url_changes_indexing(self):
        with_pol, without = pa.Authority(), pa.Authority()
        without.ceilings = {}
        changed = [p for p in with_pol.baseline if with_pol.resolve(p) != without.resolve(p)]
        self.assertEqual(changed, ["/acquire/"])

    def test_excluded_from_sitemaps_and_not_blocked_by_robots_txt(self):
        import generate_sitemaps as gs
        a = pa.Authority()
        for policy in ("status_quo", "approved_only"):
            self.assertFalse(a.resolve("/acquire/", policy)["sitemap"])
        for f in os.listdir(os.path.join(ROOT, "site", "public")):
            if f.startswith("sitemap") and f.endswith(".xml"):
                self.assertNotIn("/acquire/", open(os.path.join(ROOT, "site", "public", f), encoding="utf-8").read())
        robots = open(os.path.join(ROOT, "site", "public", "robots.txt"), encoding="utf-8").read()
        self.assertNotIn("Disallow: /acquire", robots, "crawlers must be able to read the noindex directive")
        self.assertTrue(hasattr(gs, "main"))


if __name__ == "__main__":
    unittest.main(verbosity=1)
