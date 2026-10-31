#!/usr/bin/env python3
"""recovery03_terminology_admission.py — governed admission of the BISULFID identity evidence.

One idempotent transaction, applied ONLY from the verbatim capture file
main/data/evidence/captures/R03_TERMINOLOGY_CAPTURES.json (every quoted passage below must be
listed there as found; otherwise the script aborts and writes nothing):

  ontology      + concept `hydrogen_sulfite` (HSO3-), concept-eligible (bisulfite needed a concept target)
  lexemes       + EN/DE lexemes; each resolves to ONE concept-eligible node. 'bisulfide' is POLYSEMOUS and
                  gets two lexemes (dictionary sense -> disulfide; database synonym -> hydrosulfide)
  sources       identity verified (C1–C8) -> status verified, identity_revision rev-2026-10-30-1,
                  source_lock_status stays candidate; unreachable sources stay seeded with the reason
  qualifications  qualified_narrow, enumerated uses only (industry publication NOT qualified for terminology)
  evidence      EVD-TERM-* records quoting the captured passages, with locators
  claims        claim review: new precise claims approved (approval_limited posture, listed in
                approval_ready_claims); vague legacy claims superseded; unsupported claims keep
                pending_review with a recorded boundary. Registries stay inactive; nothing is published.
Run: python3 scripts/governance_scaffolding/recovery03_terminology_admission.py [--check]
"""

import json
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(ROOT, "main", "data")
REV = "rev-2026-10-30-1"
DAY = "2026-10-30"
SPRINT = "recovery-03"
CAPTURE = "main/data/evidence/captures/R03_TERMINOLOGY_CAPTURES.json"
ROUTES = ["bisulfid_vs_bisulfide", "de_bisulfid_vs_bisulfide"]
REQUIRED_PROHIBITED = ["chemical safety", "medical claims", "market data", "route publication",
                       "removal of [SOURCE REQUIRED] markers", "source-locking by itself"]


def load(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return json.load(fh)


def dump(rel, obj):
    with open(os.path.join(ROOT, rel), "w", encoding="utf-8") as fh:
        json.dump(obj, fh, indent=2, ensure_ascii=False)
        fh.write("\n")


# --------------------------------------------------------------------------- the decisions

NEW_SOURCES = {
    "SRC-MW-DISULFIDE": {"category": "authoritative_dictionary", "publisher": "Merriam-Webster", "title": "disulfide",
                         "author_or_organization": "Merriam-Webster, Incorporated", "language": "en",
                         "url": "https://www.merriam-webster.com/dictionary/disulfide",
                         "use_for": ["English lexical entry and definitions for disulfide"]},
    "SRC-DWDS-SULFID": {"category": "authoritative_dictionary", "publisher": "DWDS — Digitales Wörterbuch der deutschen Sprache (Berlin-Brandenburgische Akademie der Wissenschaften)",
                        "title": "Sulfid", "author_or_organization": "Berlin-Brandenburgische Akademie der Wissenschaften", "language": "de",
                        "url": "https://www.dwds.de/wb/Sulfid", "use_for": ["German lexical entry and eWDG (1976) sense for Sulfid"]},
    "SRC-DWDS-BISULFID": {"category": "authoritative_dictionary", "publisher": "DWDS — Digitales Wörterbuch der deutschen Sprache (Berlin-Brandenburgische Akademie der Wissenschaften)",
                          "title": "Bisulfid (lookup result)", "author_or_organization": "Berlin-Brandenburgische Akademie der Wissenschaften", "language": "de",
                          "url": "https://www.dwds.de/wb/Bisulfid", "use_for": ["DWDS statement on whether Bisulfid is in its contemporary lexical sources"]},
    "SRC-DWDS-HYDROGENSULFID": {"category": "authoritative_dictionary", "publisher": "DWDS — Digitales Wörterbuch der deutschen Sprache (Berlin-Brandenburgische Akademie der Wissenschaften)",
                                "title": "Hydrogensulfid (lookup result)", "author_or_organization": "Berlin-Brandenburgische Akademie der Wissenschaften", "language": "de",
                                "url": "https://www.dwds.de/wb/Hydrogensulfid", "use_for": ["DWDS statement on whether Hydrogensulfid is in its contemporary lexical sources"]},
    "SRC-SPEKTRUM-SCHWEFELWASSERSTOFF-DE": {"category": "authoritative_dictionary", "publisher": "Spektrum Akademischer Verlag, Heidelberg",
                                            "title": "Schwefelwasserstoff - Lexikon der Chemie", "author_or_organization": "Spektrum der Wissenschaft Verlagsgesellschaft", "language": "de",
                                            "url": "https://www.spektrum.de/lexikon/chemie/schwefelwasserstoff/8309",
                                            "use_for": ["German chemistry-lexicon naming of the salt series of hydrogen sulfide (Hydrogensulfide, Sulfide)"]},
    "SRC-IUPAC-RED-BOOK-2005": {"category": "chemical_nomenclature_standard", "publisher": "International Union of Pure and Applied Chemistry / Royal Society of Chemistry",
                                "title": "Nomenclature of Inorganic Chemistry — IUPAC Recommendations 2005 (Red Book), ISBN 0-85404-438-8",
                                "author_or_organization": "IUPAC (N. G. Connelly, T. Damhus, R. M. Hartshorn, A. T. Hutton, eds.)", "language": "en",
                                "url": "https://iupac.org/wp-content/uploads/2016/07/Red_Book_2005.pdf",
                                "use_for": ["IUPAC-recommended names of inorganic anions (HS-, S2 2-, HSO3-)"]},
    "SRC-PUBCHEM-BISULFITE": {"category": "government_scientific_database", "publisher": "PubChem / NIH (National Center for Biotechnology Information)",
                              "title": "Bisulfite (PubChem Compound CID 104748)", "author_or_organization": "PubChem, U.S. National Library of Medicine / NIH", "language": "en",
                              "url": "https://pubchem.ncbi.nlm.nih.gov/compound/104748",
                              "use_for": ["record identity of the bisulfite anion HSO3- (formula, computed IUPAC name)"]},
}
VERIFY_EXISTING = ["SRC-MW-BISULFIDE", "SRC-MW-SULFIDE", "SRC-MW-BISULFITE", "SRC-DUDEN-SULFID",
                   "SRC-FH-MUENSTER-ANORGANISCHE-NOMENKLATUR", "SRC-PUBCHEM-HYDROSULFIDE", "SRC-BADGER-BISULFID-H2S"]
UNREACHABLE = {"SRC-IUPAC-HYDROSULFIDES": "HTTP 403 (bot challenge) on 2026-10-30; not bypassed (C6). Stays seeded.",
               "SRC-UNI-ROSTOCK-NOMENKLATUR-ID-ANIONEN": "HTTP 404 on 2026-10-30: artifact no longer at the declared URL. Stays seeded."}

ONTOLOGY_TERM = {
    "term_id": "hydrogen_sulfite", "display_name": "Hydrogen sulfite (HSO3-)", "status": "planned", "language_vector": ["en", "de"],
    "chemical_field": "inorganic chemistry, nomenclature", "industrial_signal": "sulfite / bisulfite chemistry",
    "safety_context": "requires source validation before any safety statements are made",
    "related_terms": ["bisulfite_disambiguation"], "not_to_be_confused_with": ["hydrosulfide", "bisulfide"],
    "public_page": None, "source_required": True, "source_ids": ["SRC-IUPAC-RED-BOOK-2005", "SRC-PUBCHEM-BISULFITE"],
    "risk_level": "low", "spatial_node": None,
    "notes": "Recovery-03: concept target for the lexemes 'bisulfite' and 'hydrogensulfite' (HSO3-). Added so the bisulfite/bisulfide distinction can be evidenced at lexeme level; it creates no route."}

LEXEMES = [
    ("LEX-EN-BISULFIDE-001", "disulfide", "en", "bisulfide", "synonym", "Dictionary sense: Merriam-Webster defines 'bisulfide' as 'disulfide' (first known use 1831). 'bisulfide' is polysemous; see LEX-EN-BISULFIDE-002."),
    ("LEX-EN-BISULFIDE-002", "hydrosulfide", "en", "bisulfide", "synonym", "Database-synonym sense: PubChem lists 'bisulfide' among the synonyms of HS- (CID 5047209). Supported only by boundary (database) evidence, not by an admitted lexical authority."),
    ("LEX-EN-SULFIDE-001", "sulfide", "en", "sulfide", "preferred", "Merriam-Webster headword."),
    ("LEX-EN-DISULFIDE-001", "disulfide", "en", "disulfide", "preferred", "Merriam-Webster headword."),
    ("LEX-EN-BISULFITE-001", "hydrogen_sulfite", "en", "bisulfite", "synonym", "Merriam-Webster: 'an acid sulfite'. Not a sulfide."),
    ("LEX-EN-HYDROGENSULFITE-001", "hydrogen_sulfite", "en", "hydrogensulfite", "nomenclature_controlled", "IUPAC 2005 IR-8.5 accepted abbreviated hydrogen name for HSO3-."),
    ("LEX-EN-SULFANIDE-001", "hydrosulfide", "en", "sulfanide", "nomenclature_controlled", "IUPAC 2005 substitutive name for HS-."),
    ("LEX-EN-HYDRIDOSULFATE-001", "hydrosulfide", "en", "hydridosulfate(1−)", "nomenclature_controlled", "IUPAC 2005 additive name for HS-."),
    ("LEX-EN-DISULFIDE-2MINUS-001", "disulfide", "en", "disulfide(2−)", "nomenclature_controlled", "IUPAC 2005 name for the S2 2- anion."),
    ("LEX-EN-DISULFANEDIIDE-001", "disulfide", "en", "disulfanediide", "nomenclature_controlled", "IUPAC 2005 name for S2 2- derived from the parent hydride."),
    ("LEX-DE-SULFID-001", "sulfide", "de", "Sulfid", "preferred", "Duden and DWDS headword."),
    ("LEX-DE-HYDROGENSULFID-001", "hydrosulfide", "de", "Hydrogensulfid", "observed_usage", "Spektrum Lexikon der Chemie uses 'Hydrogensulfide' for the salts MIHS; DWDS does not list it in its contemporary lexical sources."),
    ("LEX-DE-BISULFID-001", "hydrosulfide", "de", "Bisulfid", "observed_usage", "Observed in German industry usage for HS- (Badger Meter; contextual, not admitted). DWDS does not list it in its contemporary lexical sources; Duden has no entry. Not a lexicographically established German term."),
]

# qualification: source -> (domains, kind, level, role, allowed_uses, scope)
QUALS = {
    "SRC-MW-BISULFIDE": (["SD-TERMINOLOGY", "SD-LINGUISTICS"], "terminological", "lexeme", "primary_authoritative", ["en_lexical_entry_definition"], "Merriam-Webster entry 'bisulfide': headword, definition and first known use only."),
    "SRC-MW-SULFIDE": (["SD-TERMINOLOGY", "SD-LINGUISTICS"], "terminological", "lexeme", "primary_authoritative", ["en_lexical_entry_definition"], "Merriam-Webster entry 'sulfide': headword and definitions only."),
    "SRC-MW-BISULFITE": (["SD-TERMINOLOGY", "SD-LINGUISTICS"], "terminological", "lexeme", "primary_authoritative", ["en_lexical_entry_definition"], "Merriam-Webster entry 'bisulfite': headword, definition and first known use only."),
    "SRC-MW-DISULFIDE": (["SD-TERMINOLOGY", "SD-LINGUISTICS"], "terminological", "lexeme", "primary_authoritative", ["en_lexical_entry_definition"], "Merriam-Webster entry 'disulfide': headword and definitions only."),
    "SRC-DUDEN-SULFID": (["SD-TERMINOLOGY", "SD-LINGUISTICS"], "terminological", "lexeme", "primary_authoritative", ["de_lexical_entry_definition"], "Duden entry 'Sulfid': spelling, hyphenation and meaning only."),
    "SRC-DWDS-SULFID": (["SD-TERMINOLOGY", "SD-LINGUISTICS"], "terminological", "lexeme", "primary_authoritative", ["de_lexical_entry_definition"], "DWDS entry 'Sulfid': eWDG (1976) sense only."),
    "SRC-DWDS-BISULFID": (["SD-TERMINOLOGY", "SD-LINGUISTICS"], "terminological", "lexeme", "primary_authoritative", ["de_lexicographic_coverage_statement"], "DWDS lookup result for 'Bisulfid': the explicit statement that it is not in DWDS contemporary lexical sources. Not a statement about German usage in general."),
    "SRC-DWDS-HYDROGENSULFID": (["SD-TERMINOLOGY", "SD-LINGUISTICS"], "terminological", "lexeme", "primary_authoritative", ["de_lexicographic_coverage_statement"], "DWDS lookup result for 'Hydrogensulfid': the explicit coverage statement only."),
    "SRC-SPEKTRUM-SCHWEFELWASSERSTOFF-DE": (["SD-TERMINOLOGY", "SD-LINGUISTICS"], "terminological", "lexeme", "primary_authoritative", ["de_technical_term_usage"], "Spektrum Lexikon der Chemie, entry 'Schwefelwasserstoff': the naming of the two salt series only (no properties, no safety)."),
    "SRC-IUPAC-RED-BOOK-2005": (["SD-NOMENCLATURE", "SD-TERMINOLOGY"], "terminological", "lexeme", "primary_authoritative", ["iupac_recommended_name"], "IUPAC Red Book 2005: recommended/accepted names of the anions HS-, S2 2- and HSO3- (sections IR-5.3.3, IR-8.5) only."),
    "SRC-FH-MUENSTER-ANORGANISCHE-NOMENKLATUR": (["SD-NOMENCLATURE"], "terminological", "lexeme", "secondary_scholarly", ["de_nomenclature_teaching_rule"], "FH Münster teaching sheet: the German -id rule for binary anions and its table row for S2- only. Teaching material: secondary, never a standard."),
    "SRC-PUBCHEM-HYDROSULFIDE": (["SD-INORGANIC-CHEMISTRY"], "scientific", "concept", "primary_authoritative", ["database_record_identity_and_synonyms"], "PubChem CID 5047209 (HS-): record formula, computed IUPAC name and synonym list as a RECORD fact only; a synonym list is not a lexical authority."),
    "SRC-PUBCHEM-BISULFITE": (["SD-INORGANIC-CHEMISTRY"], "scientific", "concept", "primary_authoritative", ["database_record_identity_and_synonyms"], "PubChem CID 104748 (HSO3-): record formula, title and computed IUPAC name only."),
}

# evidence: id -> (source, claim|None, kind/level from qual, concept_ids, lexeme_ids, use, quotes, lexical block, capture key)
EVIDENCE = {
    "EVD-TERM-MW-BISULFIDE": ("SRC-MW-BISULFIDE", "CLM-TERM-BISULFIDE-EN-SENSE-001", ["disulfide"], ["LEX-EN-BISULFIDE-001"],
                              {"headword": "bisulfide", "part_of_speech": "noun", "definition_quoted": "disulfide", "first_known_use": "1831"},
                              ["bisulfide noun", ": disulfide", "First Known Use 1831"]),
    "EVD-TERM-MW-SULFIDE": ("SRC-MW-SULFIDE", "CLM-TERM-SULFIDE-EN-SENSE-001", ["sulfide"], ["LEX-EN-SULFIDE-001"],
                            {"headword": "sulfide", "part_of_speech": "noun",
                             "sense_1_quoted": "any of various organic compounds characterized by a sulfur atom attached to two carbon atoms",
                             "sense_2_quoted": "a binary compound (such as CuS) of sulfur usually with a more electropositive element or group : a salt of hydrogen sulfide",
                             "first_known_use": "1836"},
                            ["1 : any of various organic compounds characterized by a sulfur atom attached to two carbon atoms",
                             "2 : a binary compound (such as CuS) of sulfur usually with a more electropositive element or group : a salt of hydrogen sulfide"]),
    "EVD-TERM-MW-DISULFIDE": ("SRC-MW-DISULFIDE", "CLM-TERM-DISULFIDE-EN-SENSE-001", ["disulfide"], ["LEX-EN-DISULFIDE-001"],
                              {"headword": "disulfide", "part_of_speech": "noun",
                               "sense_1_quoted": "a compound containing two atoms of sulfur combined with an element or radical",
                               "sense_2_quoted": "an organic compound containing the divalent group SS composed of two sulfur atoms",
                               "first_known_use": "1869"},
                              ["1 : a compound containing two atoms of sulfur combined with an element or radical",
                               "2 : an organic compound containing the divalent group SS composed of two sulfur atoms", "First Known Use 1869"]),
    "EVD-TERM-MW-BISULFITE": ("SRC-MW-BISULFITE", "CLM-TERM-BISULFITE-EN-SENSE-001", ["hydrogen_sulfite"], ["LEX-EN-BISULFITE-001"],
                              {"headword": "bisulfite", "part_of_speech": "noun", "definition_quoted": "an acid sulfite", "first_known_use": "1819"},
                              ["bisulfite noun", ": an acid sulfite", "First Known Use 1819"]),
    "EVD-TERM-DUDEN-SULFID": ("SRC-DUDEN-SULFID", "CLM-TERM-SULFID-DE-SENSE-001", ["sulfide"], ["LEX-DE-SULFID-001"],
                              {"headword": "Sulfid", "hyphenation": "Sul|fid", "definition_quoted": "salzartige Verbindung des Schwefelwasserstoffs"},
                              ["Worttrennung Sul|fid", "Bedeutung ⓘ salzartige Verbindung des Schwefelwasserstoffs"]),
    "EVD-TERM-DWDS-SULFID": ("SRC-DWDS-SULFID", "CLM-TERM-SULFID-DE-SENSE-001", ["sulfide"], ["LEX-DE-SULFID-001"],
                             {"headword": "Sulfid", "dictionary": "eWDG (1976) via DWDS", "domain_label": "Chemie", "definition_quoted": "Salz des Schwefelwasserstoffs"},
                             ["Bedeutung eWDG 1976 Chemie Salz des Schwefelwasserstoffs"]),
    "EVD-TERM-DWDS-BISULFID": ("SRC-DWDS-BISULFID", "CLM-TERM-BISULFID-DE-LEXICOGRAPHY-001", ["hydrosulfide"], ["LEX-DE-BISULFID-001"],
                               {"headword": "Bisulfid", "coverage_statement_quoted": "Es tut uns leid, Ihre Anfrage Bisulfid ist nicht in unseren gegenwartssprachlichen lexikalischen Quellen vorhanden.",
                                "forms_shown": "computer-generated grammatical forms only"},
                               ["Es tut uns leid, Ihre Anfrage Bisulfid ist nicht in unseren gegenwartssprachlichen lexikalischen Quellen vorhanden.",
                                "Nominativ Plural: Bisulfide (computergeneriert)"]),
    "EVD-TERM-DWDS-HYDROGENSULFID": ("SRC-DWDS-HYDROGENSULFID", "CLM-TERM-BISULFID-DE-LEXICOGRAPHY-001", ["hydrosulfide"], ["LEX-DE-HYDROGENSULFID-001"],
                                     {"headword": "Hydrogensulfid", "coverage_statement_quoted": "Es tut uns leid, Ihre Anfrage Hydrogensulfid ist nicht in unseren gegenwartssprachlichen lexikalischen Quellen vorhanden."},
                                     ["Es tut uns leid, Ihre Anfrage Hydrogensulfid ist nicht in unseren gegenwartssprachlichen lexikalischen Quellen vorhanden."]),
    "EVD-TERM-SPEKTRUM-HYDROGENSULFIDE": ("SRC-SPEKTRUM-SCHWEFELWASSERSTOFF-DE", "CLM-TERM-HYDROGENSULFID-DE-SPEKTRUM-001", ["hydrosulfide", "sulfide"],
                                          ["LEX-DE-HYDROGENSULFID-001", "LEX-DE-SULFID-001"],
                                          {"entry": "Schwefelwasserstoff", "passage_quoted": "S. bildet zwei Reihen von Salzen, die Hydrogensulfide M I HS und die Sulfide M I 2 S.",
                                           "salt_series": "Hydrogensulfide (MIHS) and Sulfide (MI2S)"},
                                          ["S. bildet zwei Reihen von Salzen, die Hydrogensulfide M I HS und die Sulfide M I 2 S."]),
    "EVD-TERM-IUPAC-HS-NAMES": ("SRC-IUPAC-RED-BOOK-2005", "CLM-TERM-IUPAC-HS-NAMES-001", ["hydrosulfide"], ["LEX-EN-SULFANIDE-001", "LEX-EN-HYDRIDOSULFATE-001"],
                                {"anion": "HS⁻", "substitutive_name": "sulfanide", "additive_name": "hydridosulfate(1−)", "section": "IR-5.3.3.4 (heteropolyatomic anions), Example 3"},
                                ["3. HS sulfanide (substitutive), or hydridosulfate(1 ) (additive)"]),
    "EVD-TERM-IUPAC-S2-NAMES": ("SRC-IUPAC-RED-BOOK-2005", "CLM-TERM-IUPAC-S2-NAMES-001", ["disulfide"], ["LEX-EN-DISULFIDE-2MINUS-001", "LEX-EN-DISULFANEDIIDE-001"],
                                {"anion": "S₂²⁻", "homopolyatomic_name": "disulfide(2−)", "parent_hydride_name": "disulfanediide", "section": "IR-5.3.3 (homopolyatomic anions), Examples 8 and 12"},
                                ["8. S22 disulﬁde(2 )", "12. S2 disulfanediide"]),
    "EVD-TERM-IUPAC-HSO3-NAME": ("SRC-IUPAC-RED-BOOK-2005", "CLM-TERM-IUPAC-HSO3-NAME-001", ["hydrogen_sulfite"], ["LEX-EN-HYDROGENSULFITE-001"],
                                 {"anion": "HSO₃⁻", "accepted_abbreviated_name": "hydrogensulfite", "full_hydrogen_name": "hydrogen(trioxidosulfate)(1−)",
                                  "section": "IR-8.5 (abbreviated hydrogen names for certain anions)", "list_status_quoted": "It is strongly recommended that this list be viewed as limiting"},
                                 ["HSO3 hydrogensulﬁte hydrogen(trioxidosulfate)(1 )",
                                  "It is strongly recommended that this list be viewed as limiting due to the ambiguities that may arise in many other cases."]),
    "EVD-TERM-FHM-ID-RULE": ("SRC-FH-MUENSTER-ANORGANISCHE-NOMENKLATUR", "CLM-TERM-GERMAN-ID-RULE-001", ["sulfide"], ["LEX-DE-SULFID-001"],
                             {"rule_quoted": "Das nachgestellte Nichtmetallatom bzw. -ion binärer Verbindungen mit negativer Oxidationszahl endet auf -id.",
                              "example_row": "S2- Sulfid"},
                             ["Das nachgestellte Nichtmetallatom bzw. -ion binärer Verbindungen mit negativer Oxidationszahl endet auf -id.", "S2- Sulfid"]),
    # Boundary (claim-less) record facts from a government database: never a lexical authority.
    "EVD-TERM-PUBCHEM-HS-SYNONYMS": ("SRC-PUBCHEM-HYDROSULFIDE", None, ["hydrosulfide"], [],
                                     {"cid": "5047209", "molecular_formula": "HS⁻", "computed_iupac_name": "sulfanide", "record_title": "Hydrosulfide",
                                      "synonym_listed": "bisulfide"},
                                     ['"MolecularFormula": "HS-"', '"IUPACName": "sulfanide"', '"bisulfide"']),
    "EVD-TERM-PUBCHEM-BISULFITE": ("SRC-PUBCHEM-BISULFITE", None, ["hydrogen_sulfite"], [],
                                   {"cid": "104748", "molecular_formula": "HSO₃⁻", "computed_iupac_name": "hydrogen sulfite", "record_title": "Bisulfite"},
                                   ['"MolecularFormula": "HO3S-"', '"IUPACName": "hydrogen sulfite"', '"Title": "Bisulfite"']),
    # Attested industry usage: verified verbatim but NOT qualified for terminology -> never admitted.
    "EVD-TERM-BADGER-BISULFID-USAGE": ("SRC-BADGER-BISULFID-H2S", "CLM-TERM-BISULFID-001", ["hydrosulfide"], ["LEX-DE-BISULFID-001"],
                                       {"usage_quoted": "Bisulfid und Schwefelwasserstoff (HS- / H₂S)",
                                        "usage_quoted_2": "Bisulfid hingegen ist seine konjugierte Base"},
                                       ["Bisulfid und Schwefelwasserstoff (HS- / H₂S)", "Bisulfid hingegen ist seine konjugierte Base"]),
}
CAPTURE_KEY = {"EVD-TERM-PUBCHEM-HS-SYNONYMS": ["SRC-PUBCHEM-HYDROSULFIDE", "SRC-PUBCHEM-HYDROSULFIDE#synonyms"]}

NEW_CLAIMS = {
    "CLM-TERM-BISULFIDE-EN-SENSE-001": ("Merriam-Webster defines the English noun 'bisulfide' as 'disulfide' and dates its first known use to 1831.", ["SRC-MW-BISULFIDE"], "CLM-TERM-001"),
    "CLM-TERM-SULFIDE-EN-SENSE-001": ("Merriam-Webster defines 'sulfide' as (1) any of various organic compounds characterized by a sulfur atom attached to two carbon atoms, and (2) a binary compound of sulfur usually with a more electropositive element or group: a salt of hydrogen sulfide.", ["SRC-MW-SULFIDE"], "CLM-TERM-002"),
    "CLM-TERM-DISULFIDE-EN-SENSE-001": ("Merriam-Webster defines 'disulfide' as (1) a compound containing two atoms of sulfur combined with an element or radical, and (2) an organic compound containing the divalent group SS; first known use 1869.", ["SRC-MW-DISULFIDE"], None),
    "CLM-TERM-BISULFITE-EN-SENSE-001": ("Merriam-Webster defines 'bisulfite' as 'an acid sulfite' (first known use 1819), a different entry from 'bisulfide'.", ["SRC-MW-BISULFITE"], "CLM-TERM-004"),
    "CLM-TERM-SULFID-DE-SENSE-001": ("Duden defines the German noun 'Sulfid' as 'salzartige Verbindung des Schwefelwasserstoffs'; the DWDS (eWDG 1976) sense is 'Salz des Schwefelwasserstoffs'.", ["SRC-DUDEN-SULFID", "SRC-DWDS-SULFID"], "CLM-TERM-003"),
    "CLM-TERM-BISULFID-DE-LEXICOGRAPHY-001": ("DWDS states that neither 'Bisulfid' nor 'Hydrogensulfid' is in its contemporary lexical sources; it shows only computer-generated grammatical forms for them.", ["SRC-DWDS-BISULFID", "SRC-DWDS-HYDROGENSULFID"], None),
    "CLM-TERM-HYDROGENSULFID-DE-SPEKTRUM-001": ("The Spektrum Lexikon der Chemie entry 'Schwefelwasserstoff' names the two series of salts of hydrogen sulfide 'Hydrogensulfide' (MIHS) and 'Sulfide' (MI2S).", ["SRC-SPEKTRUM-SCHWEFELWASSERSTOFF-DE"], None),
    "CLM-TERM-IUPAC-HS-NAMES-001": ("The IUPAC 2005 recommendations name the anion HS⁻ 'sulfanide' (substitutive) or 'hydridosulfate(1−)' (additive).", ["SRC-IUPAC-RED-BOOK-2005"], "CLM-TERM-005"),
    "CLM-TERM-IUPAC-S2-NAMES-001": ("The IUPAC 2005 recommendations name the anion S₂²⁻ 'disulfide(2−)' or, as derived from its parent hydride, 'disulfanediide'.", ["SRC-IUPAC-RED-BOOK-2005"], None),
    "CLM-TERM-IUPAC-HSO3-NAME-001": ("The IUPAC 2005 recommendations accept 'hydrogensulfite' as an abbreviated hydrogen name for HSO₃⁻, in a list IUPAC asks to be viewed as limiting.", ["SRC-IUPAC-RED-BOOK-2005"], None),
    "CLM-TERM-GERMAN-ID-RULE-001": ("A German university nomenclature sheet (FH Münster) states that the anion name of a binary compound with negative oxidation number ends in '-id', listing 'Sulfid' for S²⁻.", ["SRC-FH-MUENSTER-ANORGANISCHE-NOMENKLATUR"], "CLM-TERM-GERMAN-ID-ACADEMIC-001"),
}
CLAIM_EVIDENCE = {}
for _eid, (_sid, _cid, *_rest) in EVIDENCE.items():
    if _cid:
        CLAIM_EVIDENCE.setdefault(_cid, []).append(_eid)

REVIEW_ONLY = {  # legacy claims that stay pending, with the recorded boundary
    "CLM-TERM-BISULFID-001": "NOT APPROVABLE under current policy: the only attestation (Badger Meter, industry_publication) is verified verbatim but the terminology domain admits only dictionaries, nomenclature standards and teaching references. DWDS does not list 'Bisulfid'; Duden has no entry. Boundary recorded: attested German industry usage for HS-, not a lexicographically established term.",
    "CLM-TERM-OXID-001": "Not reviewed for approval: 'Oxid' needs an ontology concept outside the sulfur scope; not required for the identity record.",
    "CLM-TERM-CHLORID-001": "Not reviewed for approval: 'Chlorid' needs an ontology concept outside the sulfur scope; not required for the identity record.",
    "CLM-TERM-GERMAN-ID-PATTERN-001": "Not approved: depends on Oxid/Chlorid evidence outside scope. The -id rule itself is covered by CLM-TERM-GERMAN-ID-RULE-001.",
    "CLM-TERM-ENGLISH-IDE-CONTEXT-001": "Not approved: the 1971 IUPAC source was not re-verified this sprint; current IUPAC naming is covered by the 2005 Red Book claims.",
}
SUPERSEDED_NOTE = "Superseded by {new}: the legacy claim only asserted that an entry exists; the new claim states what the entry says, quoted from the captured artifact."
SCI_NOTE = {"CLM-SCI-001": "Evidence recorded as claim-less BOUNDARY record EVD-TERM-PUBCHEM-HS-SYNONYMS (PubChem CID 5047209). Claim stays pending: the approval_limited posture covers terminology claims only."}


def main(check_only=False):
    cap = load(CAPTURE)["captures"]
    # 0. every quote must be in the capture as found
    for eid, (sid, cid, concepts, lexemes, lexical, quotes) in EVIDENCE.items():
        keys = CAPTURE_KEY.get(eid, [sid])
        found = {p["quote"] for k in keys for p in cap.get(k, {}).get("passages", []) if p["found"]}
        missing = [q for q in quotes if q not in found]
        if missing:
            print(f"ABORT: {eid}: passages not in capture: {missing}")
            return 1
    if check_only:
        print("capture covers every quoted passage")
        return 0

    # 1. ontology
    st = load("main/data/ontology/sulfur_terms.json")
    if not any(t["term_id"] == "hydrogen_sulfite" for t in st["terms"]):
        st["terms"].append(ONTOLOGY_TERM)
        dump("main/data/ontology/sulfur_terms.json", st)
    roles = load("main/data/ontology_node_roles.json")
    if not any(n["term_id"] == "hydrogen_sulfite" for n in roles["node_roles"]):
        roles["node_roles"].append({"term_id": "hydrogen_sulfite", "role": "concept_eligible",
                                    "note": "HSO3- (hydrogensulfite / bisulfite) — concept (Recovery-03)."})
    for n in roles["node_roles"]:
        if n["term_id"] == "bisulfide":
            n["note"] = ("EN form is POLYSEMOUS (Recovery-03 evidence): Merriam-Webster 'bisulfide' = 'disulfide' (1831); PubChem lists "
                         "'bisulfide' as a synonym of HS-. Lexemes LEX-EN-BISULFIDE-001 (-> disulfide) and -002 (-> hydrosulfide) "
                         "carry the two senses. The node stays non-concept: it names a word, not one substance.")
        if n["term_id"] == "bisulfid":
            n["note"] = ("German form: not in DWDS contemporary lexical sources, no Duden entry (Recovery-03); observed industry usage for HS- "
                         "(LEX-DE-BISULFID-001, contextual). Brand name of this site; not a concept target.")
    roles["concept_eligible_count"] = sum(1 for n in roles["node_roles"] if n["role"] == "concept_eligible")
    dump("main/data/ontology_node_roles.json", roles)

    # 2. lexemes
    lr = load("main/data/lexeme_registry.json")
    have = {l["lexeme_id"] for l in lr["lexemes"]}
    for lid, concept, lang, form, rel, note in LEXEMES:
        if lid not in have:
            lr["lexemes"].append({"lexeme_id": lid, "concept_id": concept, "language": lang, "script": "Latn",
                                  "display_form": form, "normalized_form": form.lower(), "lexical_relationship_type": rel,
                                  "registration_state": "registered", "notes": note + " (Recovery-03)"})
    dump("main/data/lexeme_registry.json", lr)

    # 3. sources
    sr = load("main/data/sources/source_registry.json")
    by = {s["source_id"]: s for s in sr["sources"]}
    for sid, meta in NEW_SOURCES.items():
        if sid not in by:
            rec = {"source_id": sid, "identity_revision": REV, **{k: meta[k] for k in ("category", "publisher", "title", "author_or_organization", "url", "language")},
                   "status": "verified", "source_lock_status": "candidate", "last_reviewed": DAY, "use_for": meta["use_for"],
                   "do_not_use_for": ["chemical safety", "market data", "medical claims", "route publication", "source-locking by itself"],
                   "risk_notes": [f"NEW source (Recovery-03). Identity verified {DAY}: HTTP 200, media type and sha256 recorded in {CAPTURE}; quoted passages verified verbatim (C1–C6). No credentials. verification_limited; source_lock_status candidate."],
                   "notes": "Recovery-03 terminology identity evidence."}
            sr["sources"].append(rec)
            by[sid] = rec
    for sid in VERIFY_EXISTING:
        s = by[sid]
        s["status"] = "verified"
        s.setdefault("identity_revision", REV)
        s["last_reviewed"] = DAY
        note = f"Recovery-03: identity verified {DAY} (HTTP 200, sha256 and verbatim passages in {CAPTURE}); source_lock_status stays candidate."
        s["risk_notes"] = [n for n in s.get("risk_notes", []) if not n.startswith("Recovery-03:")] + [note]
        if sid == "SRC-BADGER-BISULFID-H2S":
            s["risk_notes"].append("Recovery-03: industry_publication — identity verified, but NOT qualified for terminology claims (terminology domain admits dictionaries, nomenclature standards and teaching references only). Contextual usage only.")
    for sid, why in UNREACHABLE.items():
        s = by[sid]
        s["risk_notes"] = [n for n in s.get("risk_notes", []) if not n.startswith("Recovery-03:")] + ["Recovery-03: " + why]
    vr = sr["verification_lock_resolution"]["verification_ready_sources"]
    listed = {v["source_id"] for v in vr}
    for sid in list(NEW_SOURCES) + VERIFY_EXISTING:
        if sid not in listed:
            vr.append({"source_id": sid, "evidence_sprint": SPRINT, "identity_verification_checklist": CAPTURE,
                       "evidence_sufficient": True, "current_status": "verified", "target_status_after_guardrail_transition": "verified",
                       "source_lock_status_unchanged": "candidate"})
    dump("main/data/sources/source_registry.json", sr)

    # 4. qualifications
    qr = load("main/data/source_use_qualification_registry.json")
    qids = {q["qualification_id"] for q in qr["qualifications"]}
    qual_of = {}
    for sid, (domains, kind, level, role, uses, scope) in QUALS.items():
        qid = "QUAL-" + sid[4:] + "-R03-001"
        qual_of[sid] = qid
        if qid not in qids:
            qr["qualifications"].append({
                "qualification_id": qid, "source_id": sid, "qualified_against_source_revision": by[sid]["identity_revision"],
                "applicable_subject_domains": domains, "permitted_evidence_kinds": [kind], "permitted_claim_levels": [level],
                "evidence_roles": [role], "scope": f"REVIEWED {DAY} against the captured artifact: {scope}", "allowed_uses": uses,
                "prohibited_uses": ["chemical_safety", "medical", "market_data", "procurement_or_trade", "route_publication",
                                    "claim_approval_by_itself", "source_locking_by_itself"],
                "qualification_state": "qualified_narrow", "review_date": DAY, "geography_limitation": None,
                "jurisdiction_limitation": None, "temporal_boundary": None,
                "note": "Recovery-03. Deny-by-default outside the enumerated use. Language is not geography."})
    dump("main/data/source_use_qualification_registry.json", qr)

    # 5. evidence
    for eid, (sid, cid, concepts, lexemes, lexical, quotes) in EVIDENCE.items():
        if sid in QUALS:
            domains, kind, level, role, uses, _ = QUALS[sid]
        else:  # industry usage: terminological record without any qualification
            domains, kind, level, role, uses = ["SD-TERMINOLOGY"], "terminological", "lexeme", "contextual", ["observed_industry_usage_de"]
        keys = CAPTURE_KEY.get(eid, [sid])
        loc = {"capture_file": CAPTURE, "capture_keys": keys, "url": cap[keys[0]]["url"],
               "sha256": cap[keys[0]]["sha256"], "retrieval_date": cap[keys[0]]["retrieved_on"],
               "verbatim": quotes}
        pages = sorted({p.get("pdf_page") for k in keys for p in cap[k]["passages"] if p.get("pdf_page") and p["quote"] in quotes})
        if pages:
            loc["pdf_pages"] = pages
        rec = {"evidence_id": eid, "governed": True, "test_fixture": False, "evidence_kind": kind, "claim_level": level,
               "concept_ids": concepts, "lexeme_ids": lexemes, "relationship": None, "subject_domain": domains,
               "geography": [], "jurisdiction": None, "language_of_evidence": by[sid]["language"],
               "claim_scope": f"Captured {DAY} from {by[sid]['title']} ({by[sid]['publisher']}). Quoted passages only; see lexical.",
               "source_id": sid, "claim_id": cid, "publication_date": None, "retrieval_date": DAY,
               "temporal_scope": {"as_of": DAY, "valid_from": None, "valid_to": None},
               "evidence_review_posture": "evidence_verified", "evidence_role": role,
               "allowed_uses": uses, "prohibited_uses": ["chemical_safety", "medical", "market_data", "route_publication",
                                                         "source_locking_by_itself", "claim_approval_by_itself"],
               "lexical": lexical, "locator": loc,
               "governance_note": ("Recovery-03 terminology identity evidence. " +
                                   ("Claim-less BOUNDARY record (database record fact; not a lexical authority). " if cid is None else "") +
                                   ("NOT admissible: source has no terminology qualification (industry_publication). " if sid not in QUALS else "") +
                                   "Contract C for any route using it is derived, never implied.")}
        dump(f"main/data/evidence/{eid}.json", rec)

    # 6. claims
    tc = load("main/data/claims/terminology_claims.json")
    cl = {c["claim_id"]: c for c in tc["claims"]}
    for cid, (statement, sources, supersedes) in NEW_CLAIMS.items():
        cl.setdefault(cid, {})
        c = cl[cid]
        c.update({"claim_id": cid, "claim_type": "terminology", "status": "approved", "statement": statement, "source_ids": sources,
                  "related_terms": sorted({l[1] for l in LEXEMES for e in CLAIM_EVIDENCE[cid] if l[0] in EVIDENCE[e][3]}),
                  "related_routes": ROUTES, "allowed_pages": ROUTES,
                  "prohibited_uses": REQUIRED_PROHIBITED + ["formal nomenclature authority beyond the quoted passage",
                                                            "inference of chemical equivalence from spelling"],
                  "risk_level": "low", "last_reviewed": DAY,
                  "supporting_evidence_ids": CLAIM_EVIDENCE[cid],
                  "review_record": {"reviewed_on": DAY, "sprint": SPRINT, "decision": "approved (narrow, approval_limited)",
                                    "basis": "admitted evidence quoting the captured artifact verbatim; single_authoritative_sufficient (terminology domain)"},
                  "notes": "Approved at claim level only. Registry stays inactive: no operational activation, no publication."})
        if supersedes and supersedes in cl:
            old = cl[supersedes]
            old["status"] = "superseded"
            old["review_record"] = {"reviewed_on": DAY, "sprint": SPRINT, "decision": "superseded", "superseded_by": cid,
                                    "basis": SUPERSEDED_NOTE.format(new=cid)}
    for cid, why in REVIEW_ONLY.items():
        cl[cid]["review_record"] = {"reviewed_on": DAY, "sprint": SPRINT, "decision": "remains pending_review", "basis": why}
    tc["claims"] = list(cl.values())
    ready = tc["claim_approval_lock_resolution"]["approval_ready_claims"]
    have = {r["claim_id"] for r in ready}
    for cid, (statement, sources, _) in NEW_CLAIMS.items():
        if cid not in have:
            ready.append({"claim_id": cid, "source_ids": sources, "evidence_sprint": SPRINT, "evidence_sufficient": True,
                          "current_status": "approved", "target_status_after_guardrail_transition": "approved"})
    dump("main/data/claims/terminology_claims.json", tc)
    sc = load("main/data/claims/science_claims.json")
    for c in sc["claims"]:
        if c["claim_id"] in SCI_NOTE:
            c["review_record"] = {"reviewed_on": DAY, "sprint": SPRINT, "decision": "remains pending_review", "basis": SCI_NOTE[c["claim_id"]]}
    dump("main/data/claims/science_claims.json", sc)
    print(f"admitted: {len(NEW_SOURCES)} new + {len(VERIFY_EXISTING)} verified sources, {len(QUALS)} qualifications, "
          f"{len(LEXEMES)} lexemes, {len(EVIDENCE)} evidence records, {len(NEW_CLAIMS)} approved claims")
    return 0


if __name__ == "__main__":
    sys.exit(main("--check" in sys.argv))
