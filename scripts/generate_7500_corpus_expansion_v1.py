#!/usr/bin/env python3
"""Sprint 6M-F — governed corpus expansion toward 7,500 renderable non-public pages.

Deterministic, stdlib-only. Adds planned routes + draft content only.
Does not modify source/claim registries, sitemap, or navigation policy.
"""
from __future__ import annotations

import argparse
import itertools
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROUTES_PATH = ROOT / "main/data/routes.json"
INTERNAL_LINKS_PATH = ROOT / "main/data/internal_links.json"
INVENTORY_OUT = ROOT / "main/data/COHORT_04_7500_EXPANSION_INVENTORY.json"
MANIFEST_OUT = ROOT / "main/data/COHORT_04_7500_EXPANSION_MANIFEST.json"

COHORT_ID = "COHORT_04_7500_PIPELINE_EXPANSION"
ENGINE = "generate_7500_corpus_expansion_v1"
TARGET_NEW_ROUTES = 6000
EN_ENTITY_COUNT = 725
SINGLE_ROUTE_COUNT = 200

FORBIDDEN_CLAIM_CLASSES = [
    "safety", "medical", "market", "procurement", "production", "pricing",
    "trade", "CAGR", "acquisition", "operational_handling_guidance",
]

AUDIENCE_LABELS = {
    "AUD_CHEMIST": "Chemists",
    "AUD_RESEARCHER": "Researchers",
    "AUD_STUDENT": "Students",
    "AUD_AI_SYSTEM": "AI Systems",
    "AUD_ANALYST": "Analysts",
    "AUD_GOVERNMENT": "Government",
    "AUD_CHILD_EDU": "Child Education",
}

REF_LABELS = {
    "REF_ACADEMIC": "Academic reference",
    "REF_KNOWLEDGE": "Knowledge reference",
    "REF_RESEARCH": "Research reference",
    "REF_EDUCATIONAL": "Educational reference",
    "REF_TECHNICAL": "Technical reference",
    "REF_LINGUISTIC": "Linguistic reference",
    "REF_INSTITUTIONAL": "Institutional reference",
}

ENTITY_VARIANTS = (
    ("term", "chem", "know", "PT_TERM_CANONICAL", "AUD_CHEMIST", "REF_KNOWLEDGE", "reference_page.html"),
    ("term", "chem", "acad", "PT_TERM_CANONICAL", "AUD_CHEMIST", "REF_ACADEMIC", "reference_page.html"),
    ("term", "res", "res", "PT_TERM_CANONICAL", "AUD_RESEARCHER", "REF_RESEARCH", "reference_page.html"),
    ("aud", "stu", "edu", "PT_AUDIENCE_EXPLAINER", "AUD_STUDENT", "REF_EDUCATIONAL", "reference_page.html"),
    ("aud", "ai", "tech", "PT_AI_READABLE", "AUD_AI_SYSTEM", "REF_TECHNICAL", "reference_page.html"),
    ("cmp", "chem", "acad", "PT_COMPOUND_ENTITY", "AUD_CHEMIST", "REF_ACADEMIC", "reference_page.html"),
    ("air", "res", "res", "PT_AUDIENCE_EXPLAINER", "AUD_RESEARCHER", "REF_RESEARCH", "reference_page.html"),
    ("child", "stu", "edu", "PT_CHILD_SAFE_EDU", "AUD_CHILD_EDU", "REF_EDUCATIONAL", "reference_page.html"),
)

METAL_SULFIDE_BASES = (
    "scandium", "titanium", "vanadium", "chromium", "manganese", "iron", "cobalt", "nickel",
    "copper", "zinc", "gallium", "germanium", "rubidium", "strontium", "yttrium", "zirconium",
    "niobium", "molybdenum", "technetium", "ruthenium", "rhodium", "palladium", "silver",
    "cadmium", "indium", "tin", "antimony", "tellurium", "cesium", "barium", "lanthanum",
    "cerium", "praseodymium", "neodymium", "samarium", "europium", "gadolinium", "terbium",
    "dysprosium", "holmium", "erbium", "thulium", "ytterbium", "lutetium", "hafnium",
    "tantalum", "tungsten", "rhenium", "osmium", "iridium", "platinum", "gold", "mercury",
    "thallium", "lead", "bismuth", "polonium", "radium", "actinium", "thorium", "protactinium",
    "uranium", "neptunium", "plutonium", "americium", "curium", "berkelium", "californium",
    "aluminum", "magnesium", "calcium", "sodium", "potassium", "lithium", "beryllium", "boron",
    "phosphorus", "silicon", "selenium", "sulfur", "chlorine", "fluorine", "iodine", "bromine",
    "rhenium_disulfide", "molybdenum_trisulfide", "tungsten_trisulfide", "niobium_sulfide",
    "tantalum_sulfide", "hafnium_sulfide", "zirconium_sulfide", "vanadium_sulfide",
    "chromium_sulfide", "manganese_sulfide", "iron_disulfide", "iron_trisulfide",
    "cobalt_disulfide", "nickel_disulfide", "copper_monosulfide", "copper_disulfide",
    "zinc_blende", "sphalerite", "galena", "pyrite", "marcasite", "chalcopyrite", "bornite",
    "covellite", "chalcocite", "molybdenite", "cinnabar", "realgar", "orpiment", "stibnite",
    "bismuthinite", "argentite", "acanthite", "pentahedrite", "tetrahedrite", "enargite",
    "millerite", "violarite", "greigite", "mackinawite", "pyrrhotite", "pentlandite",
    "cobaltite", "arsenopyrite", "germanite", "renierite", "carrollite", "linnaeite",
    "siegenite", "glaucodot", "lautite", "luzonite", "famatinite", "tennantite",
)

ORGANO_ROOTS = (
    "thio", "sulfo", "mercapto", "dithio", "trithio", "sulfenyl", "sulfinyl", "sulfonyl",
    "thionyl", "sulfonimidoyl", "sulfamoyl", "sulfinate", "sulfonate", "thiolate", "thioether",
    "thioester", "thioamide", "thioimide", "thioacetal", "thiohemiacetal", "thiocyanate",
    "isothiocyanate", "dithiocarbamate", "xanthate", "trithiocarbonate", "thioaldehyde",
    "thioketone", "thioacid", "dithioacid", "trithioacid", "sulfenic", "sulfinic", "sulfonic",
    "thioanhydride", "sulfilimine", "sulfoximine", "sulfonamide", "sulfone", "sulfoxide",
    "sulfide_bridge", "disulfide_bridge", "trisulfide_bridge", "thiophene", "thiazole",
    "thiazine", "thiofuran", "dithiolane", "dithiane", "thiolane", "thiane", "thioxane",
    "sulfonium", "sulfur_ylide", "sulfenate", "sulfinate_ester", "sulfonate_ester",
    "thiophosphate", "thiophosphonate", "thiosulfonate", "sulfenamide", "sulfonohydrazide",
    "sulfonyl_hydrazide", "sulfonyl_chloride", "sulfonyl_fluoride", "sulfonyl_azide",
    "thiocarbamate", "dithiocarbamate_metal", "xanthogenate", "thioxanthate", "thiol_oxidation",
    "sulfide_oxidation", "sulfur_insertion", "desulfurization", "sulfurization", "thiolation",
    "sulfenylation", "sulfinylation", "sulfonylation", "thioetherification", "thiol_disulfide",
    "sulfur_nitrogen", "sulfur_phosphorus", "sulfur_halogen", "sulfur_oxygen", "sulfur_carbon",
    "organosulfur_ligand", "thiolate_ligand", "sulfide_ligand", "polysulfide_ligand",
    "thioamide_ligand", "dithiocarbamate_ligand", "xanthate_ligand", "thioxanthate_ligand",
    "mercaptide", "thiolate_salt", "sulfonium_salt", "sulfonamide_drug_class", "sulfa_class",
    "thiopeptide", "sulfated_polysaccharide", "sulfated_lipid", "sulfated_protein",
    "thio_sugar", "sulfated_glycosaminoglycan", "heparan_sulfate_lang", "chondroitin_sulfate_lang",
    "dermatan_sulfate_lang", "keratan_sulfate_lang", "sulfated_steroid", "sulfated_terpene",
    "sulfated_flavonoid", "sulfated_alkaloid", "sulfated_peptide", "sulfated_carbohydrate",
    "thio_sugar_terminology", "sulfate_ester_terminology", "sulfate_ether_terminology",
    "sulfate_amide_terminology", "sulfate_imide_terminology", "sulfate_anhydride_terminology",
    "sulfate_halide_terminology", "sulfate_metal_terminology", "sulfate_organic_terminology",
    "sulfate_inorganic_terminology", "sulfate_mineral_terminology", "sulfate_industrial_terminology",
    "sulfate_environmental_terminology", "sulfate_analytical_terminology", "sulfate_spectroscopic",
    "sulfate_crystallographic", "sulfate_electrochemical", "sulfate_thermodynamic",
)

ORGANO_SUFFIXES = ("ether", "ester", "acid", "amide", "imine", "ketone", "alcohol", "salt")

INORGANIC_BASES = (
    "hydrogen_sulfide", "hydrogen_polysulfide", "hydrogen_disulfide", "ammonium_hydrosulfide",
    "sodium_hydrosulfide", "potassium_hydrosulfide", "calcium_hydrosulfide", "magnesium_hydrosulfide",
    "lithium_hydrosulfide", "barium_hydrosulfide", "strontium_hydrosulfide", "zinc_hydrosulfide",
    "iron_hydrosulfide", "copper_hydrosulfide", "nickel_hydrosulfide", "cobalt_hydrosulfide",
    "manganese_hydrosulfide", "chromium_hydrosulfide", "aluminum_hydrosulfide", "tin_hydrosulfide",
    "lead_hydrosulfide", "mercury_hydrosulfide", "silver_hydrosulfide", "gold_hydrosulfide",
    "platinum_hydrosulfide", "palladium_hydrosulfide", "rhodium_hydrosulfide", "iridium_hydrosulfide",
    "osmium_hydrosulfide", "rhenium_hydrosulfide", "tungsten_hydrosulfide", "molybdenum_hydrosulfide",
    "niobium_hydrosulfide", "tantalum_hydrosulfide", "vanadium_hydrosulfide", "titanium_hydrosulfide",
    "zirconium_hydrosulfide", "hafnium_hydrosulfide", "cerium_hydrosulfide", "lanthanum_hydrosulfide",
    "neodymium_hydrosulfide", "samarium_hydrosulfide", "europium_hydrosulfide", "gadolinium_hydrosulfide",
    "ytterbium_hydrosulfide", "lutetium_hydrosulfide", "actinium_hydrosulfide", "thorium_hydrosulfide",
    "uranium_hydrosulfide", "plutonium_hydrosulfide", "polonium_hydrosulfide", "radium_hydrosulfide",
    "sulfur_dioxide_aqueous", "sulfur_trioxide_aqueous", "sulfuric_acid_dilute", "sulfuric_acid_concentrated",
    "oleum_terminology", "fuming_sulfuric_terminology", "sulfurous_acid_terminology", "sulfur_dioxide_hydrate",
    "sulfur_trioxide_hydrate", "sulfite_ion_terminology", "sulfate_ion_terminology", "thiosulfate_ion",
    "polysulfide_ion", "disulfide_ion", "trisulfide_ion", "tetrasulfide_ion", "pentasulfide_ion",
    "hexasulfide_ion", "heptasulfide_ion", "octasulfide_ion", "sulfide_ion", "sulfur_anion",
    "sulfur_cation", "sulfur_radical", "sulfur_cluster", "sulfur_ring", "cyclo_sulfur", "catena_sulfur",
    "sulfur_allotrope", "alpha_sulfur", "beta_sulfur", "gamma_sulfur", "lambda_sulfur", "mu_sulfur",
    "sulfur_vapor", "sulfur_melt", "sulfur_substrate", "sulfur_deposit", "native_sulfur",
    "volcanic_sulfur", "biogenic_sulfur", "elemental_sulfur", "recovered_sulfur", "refined_sulfur",
    "sulfur_flake", "sulfur_pastille", "sulfur_powder", "sulfur_lump", "sulfur_granule",
    "sulfur_pellet", "sulfur_prill", "sulfur_emulsion", "sulfur_suspension", "sulfur_colloid",
    "sulfur_aerosol", "sulfur_fume", "sulfur_dust", "sulfur_slurry", "sulfur_paste",
    "sulfur_compound_class", "sulfur_halide", "sulfur_nitride", "sulfur_phosphide", "sulfur_carbide",
    "sulfur_selenide", "sulfur_telluride", "sulfur_oxide", "sulfur_oxoacid", "sulfur_oxoanion",
    "sulfur_oxocation", "sulfur_fluoride", "sulfur_chloride", "sulfur_bromide", "sulfur_iodide",
    "sulfur_nitrate", "sulfur_nitrite", "sulfur_cyanide", "sulfur_thiocyanate", "sulfur_isothiocyanate",
    "sulfur_carbamate", "sulfur_dithiocarbamate", "sulfur_xanthate", "sulfur_phosphonate",
    "sulfur_phosphate", "sulfur_borate", "sulfur_silicate", "sulfur_aluminate", "sulfur_ferrate",
    "sulfur_chromate", "sulfur_manganate", "sulfur_molybdate", "sulfur_tungstate", "sulfur_vanadate",
    "sulfur_niobate", "sulfur_tantalate", "sulfur_zirconate", "sulfur_hafnate", "sulfur_titanate",
    "sulfur_cerate", "sulfur_lanthanate", "sulfur_actinate", "sulfur_uranyl", "sulfur_plutonyl",
    "sulfur_organometallic", "sulfur_ligand_complex", "sulfur_cluster_complex", "sulfur_cage_complex",
    "sulfur_chelate", "sulfur_bridge_complex", "sulfur_polynuclear", "sulfur_binuclear",
    "sulfur_trinuclear", "sulfur_tetranuclear", "sulfur_pentanuclear", "sulfur_hexanuclear",
)

INDUSTRIAL_BASES = (
    "sulfur_recovery_unit", "claus_process_terminology", "tail_gas_treatment", "sulfur_plant",
    "sulfur_block", "sulfur_pit", "sulfur_storage", "sulfur_handling_language", "sulfur_logistics",
    "sulfur_inventory", "sulfur_specification", "sulfur_grade", "sulfur_purity", "sulfur_quality",
    "sulfur_analysis", "sulfur_assay", "sulfur_sampling", "sulfur_testing", "sulfur_certification",
    "sulfur_traceability", "sulfur_batch", "sulfur_lot", "sulfur_shipment", "sulfur_receipt",
    "sulfur_dispatch", "sulfur_transfer", "sulfur_loading", "sulfur_unloading", "sulfur_conveying",
    "sulfur_melting", "sulfur_solidification", "sulfur_granulation", "sulfur_pelletizing",
    "sulfur_pastillation", "sulfur_forming", "sulfur_packaging", "sulfur_labeling", "sulfur_marking",
    "sulfur_documentation", "sulfur_regulatory", "sulfur_compliance", "sulfur_permit", "sulfur_license",
    "sulfur_emission", "sulfur_release", "sulfur_discharge", "sulfur_waste", "sulfur_residue",
    "sulfur_byproduct", "sulfur_coproduct", "sulfur_recycle", "sulfur_reuse", "sulfur_disposal",
    "sulfur_reclamation", "sulfur_regeneration", "sulfur_purification", "sulfur_refining",
    "sulfur_distillation", "sulfur_extraction", "sulfur_leaching", "sulfur_precipitation",
    "sulfur_crystallization", "sulfur_filtration", "sulfur_centrifugation", "sulfur_drying",
    "sulfur_cooling", "sulfur_heating", "sulfur_oxidation_process", "sulfur_reduction_process",
    "sulfur_hydrogenation", "sulfur_desulfurization", "sulfur_hydrodesulfurization", "sulfur_biodesulfurization",
    "sulfur_oxidation_catalyst", "sulfur_reduction_catalyst", "sulfur_process_catalyst",
    "sulfur_process_solvent", "sulfur_process_reagent", "sulfur_process_additive",
    "sulfur_process_inhibitor", "sulfur_process_promoter", "sulfur_process_stabilizer",
    "sulfur_process_emulsifier", "sulfur_process_surfactant", "sulfur_process_antifoam",
    "sulfur_process_corrosion", "sulfur_process_fouling", "sulfur_process_scaling",
    "sulfur_process_deposit", "sulfur_process_sludge", "sulfur_process_emission",
    "sulfur_process_effluent", "sulfur_process_wastewater", "sulfur_process_air",
    "sulfur_process_vent", "sulfur_process_flare", "sulfur_process_scrubber", "sulfur_process_absorber",
    "sulfur_process_adsorber", "sulfur_process_filter", "sulfur_process_separator",
    "sulfur_process_reactor", "sulfur_process_furnace", "sulfur_process_boiler",
    "sulfur_process_condenser", "sulfur_process_exchanger", "sulfur_process_pump",
    "sulfur_process_compressor", "sulfur_process_blower", "sulfur_process_fan",
    "sulfur_process_valve", "sulfur_process_piping", "sulfur_process_vessel",
    "sulfur_process_tank", "sulfur_process_silo", "sulfur_process_bin", "sulfur_process_hopper",
    "sulfur_process_conveyor", "sulfur_process_screw", "sulfur_process_belt", "sulfur_process_bucket",
    "sulfur_process_pneumatic", "sulfur_process_hydraulic", "sulfur_process_mechanical",
    "sulfur_process_electrical", "sulfur_process_instrument", "sulfur_process_control",
    "sulfur_process_automation", "sulfur_process_monitoring", "sulfur_process_alarm",
    "sulfur_process_shutdown", "sulfur_process_startup", "sulfur_process_turnaround",
    "sulfur_process_maintenance", "sulfur_process_inspection", "sulfur_process_audit",
    "sulfur_process_review", "sulfur_process_improvement", "sulfur_process_optimization",
    "sulfur_process_efficiency", "sulfur_process_yield", "sulfur_process_recovery",
    "sulfur_process_loss", "sulfur_process_balance", "sulfur_process_inventory",
    "sulfur_process_accounting", "sulfur_process_reporting", "sulfur_process_kpi",
    "sulfur_process_benchmark", "sulfur_process_standard", "sulfur_process_guideline",
    "sulfur_process_procedure", "sulfur_process_work_instruction", "sulfur_process_manual",
    "sulfur_process_handbook", "sulfur_process_glossary", "sulfur_process_terminology",
)

MINERAL_BASES = (
    "pyrite_crystal", "marcasite_crystal", "pyrrhotite_crystal", "pentlandite_crystal",
    "chalcopyrite_crystal", "bornite_crystal", "covellite_crystal", "chalcocite_crystal",
    "molybdenite_crystal", "galena_crystal", "sphalerite_crystal", "cinnabar_crystal",
    "realgar_crystal", "orpiment_crystal", "stibnite_crystal", "bismuthinite_crystal",
    "argentite_crystal", "acanthite_crystal", "millerite_crystal", "violarite_crystal",
    "greigite_crystal", "mackinawite_crystal", "cobaltite_crystal", "arsenopyrite_crystal",
    "enargite_crystal", "tennantite_crystal", "tetrahedrite_crystal", "famatinite_crystal",
    "luzonite_crystal", "carrollite_crystal", "linnaeite_crystal", "siegenite_crystal",
    "glaucodot_crystal", "lautite_crystal", "renierite_crystal", "germanite_crystal",
    "sulfide_vein", "sulfide_lode", "sulfide_deposit", "sulfide_ore", "sulfide_concentrate",
    "sulfide_tailings", "sulfide_gangue", "sulfide_gossan", "sulfide_supergene", "sulfide_hypogene",
    "sulfide_primary", "sulfide_secondary", "sulfide_tertiary", "sulfide_metamorphic",
    "sulfide_sedimentary", "sulfide_volcanogenic", "sulfide_seafloor", "sulfide_hydrothermal",
    "sulfide_epithermal", "sulfide_mesothermal", "sulfide_porphyry", "sulfide_skarn",
    "sulfide_replacement", "sulfide_disseminated", "sulfide_massive", "sulfide_banded",
    "sulfide_laminated", "sulfide_breccia", "sulfide_stockwork", "sulfide_stringer",
    "sulfide_fracture", "sulfide_cavity", "sulfide_vug", "sulfide_geode", "sulfide_nodule",
    "sulfide_concretion", "sulfide_stromatolite", "sulfide_bacterial", "sulfide_biogenic",
    "sulfide_diagenetic", "sulfide_authigenic", "sulfide_allogenic", "sulfide_detrital",
    "sulfide_clastic", "sulfide_chemical", "sulfide_evaporite", "sulfide_lacustrine",
    "sulfide_marine", "sulfide_continental", "sulfide_shallow", "sulfide_deep",
    "sulfide_subsurface", "sulfide_surface", "sulfide_weathering", "sulfide_oxidation_zone",
    "sulfide_reduction_zone", "sulfide_transition_zone", "sulfide_alteration", "sulfide_metasomatism",
    "sulfide_recrystallization", "sulfide_replacement_texture", "sulfide_colloform",
    "sulfide_banded_texture", "sulfide_massive_texture", "sulfide_disseminated_texture",
    "sulfide_porphyritic_texture", "sulfide_granular_texture", "sulfide_fibrous_texture",
    "sulfide_platy_texture", "sulfide_euhedral", "sulfide_subhedral", "sulfide_anhedral",
    "sulfide_intergrowth", "sulfide_exsolution", "sulfide_solid_solution", "sulfide_end_member",
    "sulfide_series", "sulfide_group", "sulfide_family", "sulfide_supergroup", "sulfide_class",
    "sulfide_subclass", "sulfide_order", "sulfide_genus", "sulfide_species", "sulfide_variety",
    "sulfide_polytype", "sulfide_polymorph", "sulfide_allotrope_mineral", "sulfide_pseudomorph",
    "sulfide_twin", "sulfide_crystal_system", "sulfide_space_group", "sulfide_unit_cell",
    "sulfide_lattice", "sulfide_bonding", "sulfide_coordination", "sulfide_polyhedral",
    "sulfide_morphology", "sulfide_habit", "sulfide_cleavage", "sulfide_fracture_mineral",
    "sulfide_hardness", "sulfide_streak", "sulfide_luster", "sulfide_color", "sulfide_transparency",
    "sulfide_specific_gravity", "sulfide_density", "sulfide_magnetic", "sulfide_electrical",
    "sulfide_thermal", "sulfide_optical", "sulfide_spectroscopic_mineral", "sulfide_raman",
    "sulfide_infrared", "sulfide_xray", "sulfide_electron", "sulfide_microprobe",
)

DISAMBIG_BASES = (
    "sulfide_sulfite_boundary", "sulfate_sulfite_boundary", "sulfate_sulfide_boundary",
    "sulfite_sulfide_boundary", "thiosulfate_sulfate_boundary", "thiosulfate_sulfite_boundary",
    "polysulfide_sulfide_boundary", "disulfide_sulfide_boundary", "sulfone_sulfoxide_boundary",
    "sulfoxide_sulfide_boundary", "sulfonic_sulfate_boundary", "sulfonic_sulfite_boundary",
    "mercaptan_thiol_boundary", "thiol_thiolate_boundary", "thioether_sulfide_boundary",
    "sulfenyl_sulfinyl_boundary", "sulfinyl_sulfonyl_boundary", "sulfonyl_sulfonic_boundary",
    "sulfur_dioxide_sulfite_boundary", "sulfur_trioxide_sulfate_boundary", "oleum_sulfuric_boundary",
    "hydrogen_sulfide_sulfide_salt_boundary", "native_sulfur_sulfide_boundary",
    "elemental_sulfur_compound_boundary", "inorganic_organosulfur_boundary",
    "mineral_synthetic_sulfide_boundary", "ore_concentrate_sulfide_boundary",
    "sulfide_oxide_boundary", "sulfide_halide_boundary", "sulfide_carbide_boundary",
    "sulfide_nitride_boundary", "sulfide_phosphide_boundary", "sulfide_selenide_boundary",
    "sulfide_telluride_boundary", "sulfide_arsenide_boundary", "sulfide_antimonide_boundary",
    "sulfide_bismuthide_boundary", "mono_disulfide_boundary", "di_trisulfide_boundary",
    "catena_cyclo_sulfur_boundary", "alpha_beta_sulfur_boundary", "volcanic_biogenic_sulfur_boundary",
    "sulfur_recovery_byproduct_boundary", "claus_wet_sulfur_boundary", "frasch_mined_sulfur_boundary",
    "sulfur_specification_grade_boundary", "industrial_reagent_sulfur_boundary",
    "sulfur_emission_release_boundary", "sulfur_waste_residue_boundary", "sulfur_recycle_disposal_boundary",
    "sulfur_process_product_boundary", "sulfur_catalyst_inhibitor_boundary",
    "sulfur_solvent_reagent_boundary", "sulfur_additive_stabilizer_boundary",
    "sulfur_plant_unit_boundary", "sulfur_storage_handling_boundary", "sulfur_logistics_inventory_boundary",
    "sulfur_analysis_assay_boundary", "sulfur_certification_traceability_boundary",
    "sulfur_regulatory_compliance_boundary", "sulfur_permit_license_boundary",
    "sulfur_emission_discharge_boundary", "sulfur_effluent_wastewater_boundary",
    "sulfur_process_reactor_furnace_boundary", "sulfur_process_condenser_exchanger_boundary",
    "sulfur_process_pump_compressor_boundary", "sulfur_process_valve_piping_boundary",
    "sulfur_process_vessel_tank_boundary", "sulfur_process_conveyor_screw_boundary",
    "sulfur_process_control_automation_boundary", "sulfur_process_monitoring_alarm_boundary",
    "sulfur_process_shutdown_startup_boundary", "sulfur_process_maintenance_inspection_boundary",
    "sulfur_process_audit_review_boundary", "sulfur_process_improvement_optimization_boundary",
    "sulfur_process_efficiency_yield_boundary", "sulfur_process_recovery_loss_boundary",
    "sulfur_process_balance_inventory_boundary", "sulfur_process_reporting_kpi_boundary",
    "sulfur_process_standard_guideline_boundary", "sulfur_process_procedure_instruction_boundary",
    "sulfur_process_manual_handbook_boundary", "sulfur_process_glossary_terminology_boundary",
    "en_de_sulfide_terminology_boundary", "en_de_sulfate_terminology_boundary",
    "en_de_sulfite_terminology_boundary", "en_de_thiosulfate_terminology_boundary",
    "en_de_polysulfide_terminology_boundary", "en_de_mercaptan_terminology_boundary",
    "en_de_thioether_terminology_boundary", "en_de_sulfoxide_terminology_boundary",
    "en_de_sulfone_terminology_boundary", "en_de_sulfonic_terminology_boundary",
    "en_de_sulfur_dioxide_terminology_boundary", "en_de_sulfur_trioxide_terminology_boundary",
    "en_de_hydrogen_sulfide_terminology_boundary", "en_de_native_sulfur_terminology_boundary",
    "en_de_mineral_sulfide_terminology_boundary", "en_de_industrial_sulfur_terminology_boundary",
    "en_de_sulfur_process_terminology_boundary", "en_de_sulfur_emission_terminology_boundary",
    "en_de_sulfur_waste_terminology_boundary", "en_de_sulfur_recycle_terminology_boundary",
    "en_de_sulfur_specification_terminology_boundary", "en_de_sulfur_analysis_terminology_boundary",
    "en_de_sulfur_regulatory_terminology_boundary", "en_de_sulfur_plant_terminology_boundary",
    "en_de_sulfur_storage_terminology_boundary", "en_de_sulfur_handling_terminology_boundary",
    "en_de_sulfur_logistics_terminology_boundary", "en_de_sulfur_inventory_terminology_boundary",
    "en_de_sulfur_quality_terminology_boundary", "en_de_sulfur_purity_terminology_boundary",
    "en_de_sulfur_grade_terminology_boundary", "en_de_sulfur_batch_terminology_boundary",
    "en_de_sulfur_lot_terminology_boundary", "en_de_sulfur_shipment_terminology_boundary",
    "en_de_sulfur_receipt_terminology_boundary", "en_de_sulfur_dispatch_terminology_boundary",
    "en_de_sulfur_transfer_terminology_boundary", "en_de_sulfur_loading_terminology_boundary",
    "en_de_sulfur_unloading_terminology_boundary", "en_de_sulfur_conveying_terminology_boundary",
    "en_de_sulfur_melting_terminology_boundary", "en_de_sulfur_solidification_terminology_boundary",
    "en_de_sulfur_granulation_terminology_boundary", "en_de_sulfur_pelletizing_terminology_boundary",
    "en_de_sulfur_pastillation_terminology_boundary", "en_de_sulfur_forming_terminology_boundary",
    "en_de_sulfur_packaging_terminology_boundary", "en_de_sulfur_labeling_terminology_boundary",
    "en_de_sulfur_marking_terminology_boundary", "en_de_sulfur_documentation_terminology_boundary",
)

DE_TERM_BASES = (
    "kupfer_sulfid", "zink_sulfid", "blei_sulfid", "eisen_sulfid", "nickel_sulfid",
    "kobalt_sulfid", "mangan_sulfid", "chrom_sulfid", "vanadium_sulfid", "molybdaen_sulfid",
    "wolfram_sulfid", "niob_sulfid", "tantal_sulfid", "zirkonium_sulfid", "hafnium_sulfid",
    "titan_sulfid", "scandium_sulfid", "yttrium_sulfid", "lanthan_sulfid", "cer_sulfid",
    "praseodym_sulfid", "neodym_sulfid", "samarium_sulfid", "europium_sulfid", "gadolinium_sulfid",
    "terbium_sulfid", "dysprosium_sulfid", "holmium_sulfid", "erbium_sulfid", "thulium_sulfid",
    "ytterbium_sulfid", "lutetium_sulfid", "actinium_sulfid", "thorium_sulfid", "uran_sulfid",
    "neptunium_sulfid", "plutonium_sulfid", "americium_sulfid", "curium_sulfid", "berkelium_sulfid",
    "kalifornium_sulfid", "einsteinium_sulfid", "fermium_sulfid", "mendelevium_sulfid", "nobelium_sulfid",
    "lawrencium_sulfid", "rutherfordium_sulfid", "dubnium_sulfid", "seaborgium_sulfid", "bohrium_sulfid",
    "hassium_sulfid", "meitnerium_sulfid", "darmstadtium_sulfid", "roentgenium_sulfid", "copernicium_sulfid",
    "nihonium_sulfid", "flerovium_sulfid", "moscovium_sulfid", "livermorium_sulfid", "tenness_sulfid",
    "oganesson_sulfid", "natrium_sulfid", "kalium_sulfid", "lithium_sulfid", "magnesium_sulfid",
    "calcium_sulfid", "strontium_sulfid", "barium_sulfid", "rubidium_sulfid", "caesium_sulfid",
    "aluminium_sulfid", "gallium_sulfid", "indium_sulfid", "thallium_sulfid", "germanium_sulfid",
    "zinn_sulfid", "antimon_sulfid", "wismut_sulfid", "selen_sulfid", "tellur_sulfid",
    "silber_sulfid", "gold_sulfid", "quecksilber_sulfid", "platin_sulfid", "palladium_sulfid",
    "rhodium_sulfid", "iridium_sulfid", "osmium_sulfid", "rhenium_sulfid", "ruthenium_sulfid",
    "technetium_sulfid", "cadmiun_sulfid", "bor_sulfid", "phosphor_sulfid", "silicium_sulfid",
    "schwefeldioxid", "schwefeltrioxid", "schwefelsaeure", "schwefliger_saeure", "schwefelwasserstoff",
    "polysulfid_salze", "thiosulfat_salze", "sulfat_salze", "sulfit_salze", "sulfid_salze",
    "thioether_terminologie", "mercaptan_terminologie", "sulfonyl_terminologie", "sulfinyl_terminologie",
    "sulfenyl_terminologie", "sulfonsaeure_terminologie", "sulfoxid_terminologie", "sulfon_terminologie",
    "thioamid_terminologie", "thioester_terminologie", "dithiocarbamat_terminologie", "xanthogenat_terminologie",
    "thiocyanat_terminologie", "isothiocyanat_terminologie", "schwefel_allotrop_terminologie",
    "elementar_schwefel_terminologie", "vulkanischer_schwefel_terminologie", "biogener_schwefel_terminologie",
    "schwefel_erz_terminologie", "schwefel_konzentrat_terminologie", "schwefel_rückstand_terminologie",
    "schwefel_nebenprodukt_terminologie", "schwefel_rückgewinnung_terminologie", "claus_prozess_terminologie",
    "schwefel_lagerung_terminologie", "schwefel_handhabung_terminologie", "schwefel_logistik_terminologie",
    "schwefel_qualität_terminologie", "schwefel_reinheit_terminologie", "schwefel_spezifikation_terminologie",
    "schwefel_analyse_terminologie", "schwefel_prüfung_terminologie", "schwefel_zertifizierung_terminologie",
    "schwefel_rückverfolgbarkeit_terminologie", "schwefel_charge_terminologie", "schwefel_partie_terminologie",
    "schwefel_lieferung_terminologie", "schwefel_versand_terminologie", "schwefel_empfang_terminologie",
    "schwefel_umlagerung_terminologie", "schwefel_verladung_terminologie", "schwefel_entladung_terminologie",
    "schwefel_förderung_terminologie", "schwefel_schmelzen_terminologie", "schwefel_erstarren_terminologie",
    "schwefel_granulierung_terminologie", "schwefel_pelletierung_terminologie", "schwefel_pastillierung_terminologie",
    "schwefel_formgebung_terminologie", "schwefel_verpackung_terminologie", "schwefel_kennzeichnung_terminologie",
    "schwefel_dokumentation_terminologie", "schwefel_regulierung_terminologie", "schwefel_compliance_terminologie",
    "schwefel_genehmigung_terminologie", "schwefel_emission_terminologie", "schwefel_abgabe_terminologie",
    "schwefel_abfall_terminologie", "schwefel_entsorgung_terminologie", "schwefel_recycling_terminologie",
    "schwefel_wiederverwertung_terminologie", "schwefel_aufbereitung_terminologie", "schwefel_raffination_terminologie",
    "schwefel_destillation_terminologie", "schwefel_extraktion_terminologie", "schwefel_auslaugung_terminologie",
    "schwefel_fällung_terminologie", "schwefel_kristallisation_terminologie", "schwefel_filtration_terminologie",
    "schwefel_zentrifugation_terminologie", "schwefel_trocknung_terminologie", "schwefel_kühlung_terminologie",
    "schwefel_erwärmung_terminologie", "schwefel_oxidation_prozess_terminologie", "schwefel_reduktion_prozess_terminologie",
    "schwefel_entschwefelung_terminologie", "schwefel_hydroentschwefelung_terminologie", "schwefel_bioentschwefelung_terminologie",
    "schwefel_katalysator_terminologie", "schwefel_lösungsmittel_terminologie", "schwefel_reagenz_terminologie",
    "schwefel_additiv_terminologie", "schwefel_inhibitor_terminologie", "schwefel_promotor_terminologie",
    "schwefel_stabilisator_terminologie", "schwefel_emulgator_terminologie", "schwefel_tensid_terminologie",
    "schwefel_antischäumer_terminologie", "schwefel_korrosion_terminologie", "schwefel_verschmutzung_terminologie",
    "schwefel_ablagerung_terminologie", "schwefel_schlamm_terminologie", "schwefel_prozess_emission_terminologie",
    "schwefel_prozess_abwasser_terminologie", "schwefel_prozess_luft_terminologie", "schwefel_prozess_abgas_terminologie",
    "schwefel_prozess_fackel_terminologie", "schwefel_prozess_wäscher_terminologie", "schwefel_prozess_absorber_terminologie",
    "schwefel_prozess_adsorber_terminologie", "schwefel_prozess_filter_terminologie", "schwefel_prozess_abscheider_terminologie",
    "schwefel_prozess_reaktor_terminologie", "schwefel_prozess_ofen_terminologie", "schwefel_prozess_kessel_terminologie",
    "schwefel_prozess_kondensator_terminologie", "schwefel_prozess_wärmetauscher_terminologie", "schwefel_prozess_pumpe_terminologie",
    "schwefel_prozess_verdichter_terminologie", "schwefel_prozess_gebläse_terminologie", "schwefel_prozess_ventilator_terminologie",
    "schwefel_prozess_ventil_terminologie", "schwefel_prozess_rohrleitung_terminologie", "schwefel_prozess_behälter_terminologie",
    "schwefel_prozess_tank_terminologie", "schwefel_prozess_silo_terminologie", "schwefel_prozess_trichter_terminologie",
    "schwefel_prozess_förderer_terminologie", "schwefel_prozess_schnecke_terminologie", "schwefel_prozess_band_terminologie",
    "schwefel_prozess_eimer_terminologie", "schwefel_prozess_pneumatik_terminologie", "schwefel_prozess_hydraulik_terminologie",
    "schwefel_prozess_mechanik_terminologie", "schwefel_prozess_elektrik_terminologie", "schwefel_prozess_instrumentierung_terminologie",
    "schwefel_prozess_steuerung_terminologie", "schwefel_prozess_automatisierung_terminologie", "schwefel_prozess_überwachung_terminologie",
    "schwefel_prozess_alarm_terminologie", "schwefel_prozess_abschaltung_terminologie", "schwefel_prozess_inbetriebnahme_terminologie",
    "schwefel_prozess_wartung_terminologie", "schwefel_prozess_inspektion_terminologie", "schwefel_prozess_audit_terminologie",
    "schwefel_prozess_prüfung_terminologie", "schwefel_prozess_verbesserung_terminologie", "schwefel_prozess_optimierung_terminologie",
    "schwefel_prozess_effizienz_terminologie", "schwefel_prozess_ausbeute_terminologie", "schwefel_prozess_rückgewinnung_terminologie",
    "schwefel_prozess_verlust_terminologie", "schwefel_prozess_bilanz_terminologie", "schwefel_prozess_inventar_terminologie",
    "schwefel_prozess_buchführung_terminologie", "schwefel_prozess_berichterstattung_terminologie", "schwefel_prozess_kpi_terminologie",
    "schwefel_prozess_benchmark_terminologie", "schwefel_prozess_standard_terminologie", "schwefel_prozess_richtlinie_terminologie",
    "schwefel_prozess_verfahren_terminologie", "schwefel_prozess_arbeitsanweisung_terminologie", "schwefel_prozess_handbuch_terminologie",
    "schwefel_prozess_glossar_terminologie", "schwefel_prozess_terminologie_terminologie", "schwefel_prozess_sprache_terminologie",
)


def display_term(term: str) -> str:
    return term.replace("_", " ").title()


def path_slug(term: str) -> str:
    return term.replace("_", "-")


def build_en_entity_catalog() -> list[tuple[str, str]]:
    """Return (entity_key, category) — exactly EN_ENTITY_COUNT entries."""
    catalog: list[tuple[str, str]] = []
    seen: set[str] = set()

    def add(key: str, category: str) -> None:
        if key in seen:
            return
        seen.add(key)
        catalog.append((key, category))

    for base in METAL_SULFIDE_BASES:
        add(f"c04_metal_{base}", "metal_sulfide_language")
        if len(catalog) >= 145:
            break

    for root, suffix in itertools.islice(itertools.product(ORGANO_ROOTS, ORGANO_SUFFIXES), 145):
        add(f"c04_organo_{root}_{suffix}", "organosulfur_language")
        if len(catalog) >= 290:
            break

    for base in INORGANIC_BASES:
        add(f"c04_inorg_{base}", "inorganic_sulfur_language")
        if len(catalog) >= 435:
            break

    for base in INDUSTRIAL_BASES:
        add(f"c04_ind_{base}", "industrial_language")
        if len(catalog) >= 580:
            break

    for base in MINERAL_BASES:
        add(f"c04_min_{base}", "mineral_geology_language")
        if len(catalog) >= 725:
            break

    for base in DISAMBIG_BASES:
        add(f"c04_dis_{base}", "disambiguation_prep")
        if len(catalog) >= EN_ENTITY_COUNT:
            break

    if len(catalog) < EN_ENTITY_COUNT:
        raise ValueError(f"expected {EN_ENTITY_COUNT} EN entities, built {len(catalog)}")
    return catalog[:EN_ENTITY_COUNT]


def build_single_routes() -> list[tuple[str, str, str, str, str, str]]:
    """Return (lang, route_id, path, h1, page_family, template)."""
    singles: list[tuple[str, str, str, str, str, str]] = []

    for i, base in enumerate(DE_TERM_BASES[:120]):
        slug = path_slug(base)
        rid = f"cohort04_de_{base}"
        singles.append((
            "de", rid, f"/de/terminology/cohort04/{slug}/",
            f"{display_term(base)} — DE Terminologie", "de_terminology", "term_page.html",
        ))

    en_disambig = DISAMBIG_BASES[:30]
    for base in en_disambig:
        slug = path_slug(base)
        rid = f"cohort04_en_dis_{base}"
        singles.append((
            "en", rid, f"/reference/cohort04/{slug}/",
            f"{display_term(base)} — Disambiguation", "disambiguation", "reference_page.html",
        ))

    gov_topics = (
        ("en_gov_7500_rc_posture", "/foundation/7500-rc-posture/", "7,500-page RC posture foundation"),
        ("en_gov_14000_corpus_bridge", "/foundation/14000-corpus-bridge/", "14,000-page corpus bridge"),
        ("en_gov_cohort04_spine", "/reference/cohort-04-spine/", "Cohort 04 terminology spine index"),
        ("en_gov_batch_render_7500", "/reference/batch-render-7500/", "7,500 batch render discipline"),
        ("en_gov_source_claim_7500", "/reference/source-claim-7500/", "7,500 source/claim boundary explainer"),
        ("en_gov_multilingual_7500", "/reference/multilingual-7500/", "Multilingual 7,500 corpus map"),
        ("en_gov_pipeline_status_7500", "/reference/pipeline-status-7500/", "7,500 pipeline status explainer"),
        ("en_gov_future_100k", "/reference/future-100k-expansion/", "Future 100k+ expansion primer"),
        ("en_gov_stratified_selection", "/reference/stratified-selection-7500/", "Stratified 7,500 selection explainer"),
        ("en_gov_rc_quarantine", "/reference/rc-quarantine-7500/", "7,500 RC quarantine discipline"),
        ("de_gov_7500_rc_posture", "/de/reference/7500-rc-posture/", "7.500-Seiten-RC-Haltung"),
        ("de_gov_14000_corpus_bridge", "/de/reference/14000-corpus-bridge/", "14.000-Seiten-Korpus-Brücke"),
        ("de_gov_cohort04_spine", "/de/reference/cohort-04-spine/", "Cohort-04-Terminologie-Spine"),
        ("de_gov_source_claim_7500", "/de/reference/source-claim-7500/", "7.500 Quellen/Claim-Grenze"),
        ("de_gov_multilingual_7500", "/de/reference/multilingual-7500/", "Mehrsprachige 7.500-Karte"),
    )
    for rid_suffix, path, h1 in gov_topics:
        lang = "de" if path.startswith("/de/") else "en"
        rid = f"cohort04_{rid_suffix}"
        singles.append((lang, rid, path, h1, "reference_governance", "reference_page.html"))

    gateway_topics = (
        ("en_index_cohort04_spine", "/reference/cohort-04-index/", "Cohort 04 index hub"),
        ("en_index_7500_families", "/reference/7500-families-index/", "7,500 route families index"),
        ("en_index_en_terminology_7500", "/reference/en-terminology-7500/", "EN terminology 7,500 hub"),
        ("en_index_de_terminology_7500", "/reference/de-terminology-7500/", "DE terminology 7,500 hub"),
        ("en_index_disambiguation_7500", "/reference/disambiguation-7500/", "Disambiguation 7,500 hub"),
        ("en_index_governance_7500", "/reference/governance-7500/", "Governance 7,500 hub"),
        ("en_index_industrial_7500", "/reference/industrial-language-7500/", "Industrial language 7,500 hub"),
        ("en_index_mineral_7500", "/reference/mineral-language-7500/", "Mineral language 7,500 hub"),
        ("en_index_source_required_7500", "/reference/source-required-7500/", "Source-required 7,500 hub"),
        ("en_index_14000_pipeline", "/reference/14000-pipeline-index/", "14,000 pipeline index hub"),
        ("de_index_cohort04_spine", "/de/reference/cohort-04-index/", "Cohort-04-Index-Hub"),
        ("de_index_7500_families", "/de/reference/7500-families-index/", "7.500-Routenfamilien-Index"),
        ("de_index_en_terminology_7500", "/de/reference/en-terminology-7500/", "EN-Terminologie-7.500-Hub"),
        ("de_index_de_terminology_7500", "/de/reference/de-terminology-7500/", "DE-Terminologie-7.500-Hub"),
        ("de_index_disambiguation_7500", "/de/reference/disambiguation-7500/", "Disambiguation-7.500-Hub"),
        ("de_index_governance_7500", "/de/reference/governance-7500/", "Governance-7.500-Hub"),
        ("de_index_industrial_7500", "/de/reference/industrial-language-7500/", "Industrielle-Sprache-7.500-Hub"),
        ("de_index_mineral_7500", "/de/reference/mineral-language-7500/", "Mineral-Sprache-7.500-Hub"),
        ("de_index_source_required_7500", "/de/reference/source-required-7500/", "Quellenpflicht-7.500-Hub"),
        ("de_index_14000_pipeline", "/de/reference/14000-pipeline-index/", "14.000-Pipeline-Index-Hub"),
        ("en_index_claim_boundary_7500", "/reference/claim-boundary-7500/", "Claim boundary 7,500 hub"),
        ("en_index_multilingual_arch_7500", "/reference/multilingual-arch-7500/", "Multilingual architecture 7,500 hub"),
        ("en_index_future_corpus_7500", "/reference/future-corpus-7500/", "Future corpus families 7,500 hub"),
        ("de_index_claim_boundary_7500", "/de/reference/claim-boundary-7500/", "Claim-Grenze-7.500-Hub"),
        ("de_index_multilingual_arch_7500", "/de/reference/multilingual-arch-7500/", "Mehrsprachige-Architektur-7.500-Hub"),
        ("de_index_future_corpus_7500", "/de/reference/future-corpus-7500/", "Zukünftige-Korpusfamilien-7.500-Hub"),
        ("en_gov_render_idempotency_7500", "/reference/render-idempotency-7500/", "7,500 render idempotency explainer"),
        ("en_gov_manifest_integrity_7500", "/reference/manifest-integrity-7500/", "7,500 manifest integrity explainer"),
        ("de_gov_render_idempotency_7500", "/de/reference/render-idempotency-7500/", "7.500-Render-Idempotenz"),
        ("de_gov_manifest_integrity_7500", "/de/reference/manifest-integrity-7500/", "7.500-Manifest-Integrität"),
        ("en_gov_corpus_validation_7500", "/reference/corpus-validation-7500/", "7,500 corpus validation explainer"),
        ("de_gov_corpus_validation_7500", "/de/reference/corpus-validation-7500/", "7.500-Korpus-Validierung"),
        ("en_gov_non_public_posture_7500", "/reference/non-public-posture-7500/", "7,500 non-public posture explainer"),
        ("de_gov_non_public_posture_7500", "/de/reference/non-public-posture-7500/", "7.500-Nichtöffentlich-Haltung"),
        ("en_index_pipeline_lock_7500", "/reference/pipeline-lock-7500/", "14,000 pipeline lock 7,500 hub"),
    )
    for rid_suffix, path, h1 in gateway_topics:
        lang = "de" if path.startswith("/de/") else "en"
        rid = f"cohort04_{rid_suffix}"
        singles.append((lang, rid, path, h1, "gateway", "reference_page.html"))

    if len(singles) != SINGLE_ROUTE_COUNT:
        raise ValueError(f"expected {SINGLE_ROUTE_COUNT} single routes, built {len(singles)}")
    return singles


def build_h1(row: dict) -> str:
    pt = row["page_type_id"]
    term = display_term(row["term_or_entity"])
    if pt == "PT_AUDIENCE_EXPLAINER":
        aud = AUDIENCE_LABELS.get(row["audience_id"], row["audience_id"])
        return f"{term} for {aud}"
    if pt == "PT_COMPOUND_ENTITY":
        return f"{term} — Compound Reference"
    if pt == "PT_AI_READABLE":
        return f"AI Reference: {term}"
    if pt == "PT_CHILD_SAFE_EDU":
        return f"Learn: {term}"
    if pt == "PT_TERM_CANONICAL":
        return f"{term} — Terminology Reference"
    return row.get("h1_override") or f"{term} — Reference Draft"


def page_role_bullets(row: dict) -> list[str]:
    pt = row["page_type_id"]
    term = row["term_or_entity"]
    ref = REF_LABELS.get(row["reference_layer_id"], row["reference_layer_id"])
    aud = AUDIENCE_LABELS.get(row["audience_id"], row["audience_id"])
    category = row.get("entity_category", "governed_terminology")
    if pt == "PT_TERM_CANONICAL":
        return [
            f"Canonical terminology reference surface for `{term}` ({category})",
            f"Reference layer: {ref}",
            f"Audience posture: {aud}",
            "Lexical and nomenclature boundary framing only — not operational instruction",
            "Factual chemistry lines remain **[SOURCE REQUIRED]** until separately governed",
        ]
    if pt == "PT_AUDIENCE_EXPLAINER":
        return [
            f"Audience-layer explainer for `{term}` ({aud})",
            f"Vocabulary and claim boundary adapted to {aud} without meaning change",
            ref,
            "Does not upgrade evidence beyond registry allowance",
            "No unsupported simplification of chemical fact",
        ]
    if pt == "PT_COMPOUND_ENTITY":
        return [
            f"Compound/entity naming record for `{term}`",
            "Naming and identity boundary — not industrial performance claims",
            ref,
            "Operational handling and procurement language excluded",
            "**[SOURCE REQUIRED]** for all factual compound assertions",
        ]
    if pt == "PT_AI_READABLE":
        return [
            f"Machine-readable governed record for `{term}`",
            "Structured provenance and excluded-claims disclosure",
            "Registry-backed fields only — no inferred facts",
            ref,
            "Not publication-ready without source and claim gates",
        ]
    if pt == "PT_CHILD_SAFE_EDU":
        return [
            f"Child-safe educational vocabulary framing for `{term}`",
            "Naming curiosity only — no experiments, hazards, or handling",
            "Educational simplification limit enforced",
            ref,
            "Not a safety guide or textbook experiment page",
        ]
    return [
        f"Governed non-public reference draft for `{term}`",
        "Corpus expansion for 14,000-page launch pipeline — not a reduced launch",
        ref if row.get("reference_layer_id") else "Governance/reference layer",
        "**[SOURCE REQUIRED]** for unresolved factual lines",
        "No source approval or claim approval implied",
    ]


def render_en_markdown(row: dict) -> str:
    h1 = build_h1(row)
    title = f"{h1} | bisulfid.com"
    bullets = page_role_bullets(row)
    bullet_text = "\n".join(f"- {b}" for b in bullets)
    excluded = ", ".join(FORBIDDEN_CLAIM_CLASSES)
    return f"""---
route_id: {row['route_id']}
inventory_row_id: {row['inventory_row_id']}
status: draft
publication_status: non_public
publication_eligibility: false
indexable: false
in_sitemap: false
in_navigation: false
language: en
locale: en
source_language: en
title: {title}
page_type_id: {row['page_type_id']}
audience_id: {row.get('audience_id', 'ALL')}
reference_layer_id: {row.get('reference_layer_id', 'REF_KNOWLEDGE')}
source_posture: source_required_unresolved
claim_posture: claim_pending_review
cohort_id: {COHORT_ID}
generated: true
engine: {ENGINE}
noindex_default: true
---
# {h1}

**Draft status:** This page is a **non-public** COHORT_04 pipeline expansion draft. It is **not published**, **not indexable**, **not in the sitemap**, **not in navigation**, and **not publication-ready**. This is not a public launch page. **No claim is approved** for publication from this draft alone.

## Reliability notice

| Field | Value |
| --- | --- |
| knowledge_reliability_level | L2_draft_cautious |
| evidence_grade | terminology_dictionary |
| source_posture | source_required_unresolved |
| claim_posture | claim_pending_review |
| excluded_claim_classes | {excluded} |

## Page purpose

{bullet_text}

Terminology and chemical fact lines that are not yet source-supported: **[SOURCE REQUIRED]**.

## Source and claim status

- Source posture: **source_required_unresolved** — factual terminology not asserted as verified in this draft.
- Claim posture: **claim_pending_review** — no approved publication claim from this page alone.
- Source registries: **inactive** for mass publication; individual sources may exist elsewhere.
- This draft does not remove **[SOURCE REQUIRED]** markers from other corpus pages.

## Publication blockers

- Route remains `planned`; `indexable: false`; `in_sitemap: false`; `in_navigation: false`.
- `production_can_safely_proceed: no`.
- **14,000-page minimum launch corpus** objective unchanged — this page is pipeline expansion only.

## Internal link placeholders (planning only)

- `route_id`: `en_foundation_sovereign_intro` (planning placeholder — not a live link)
- `route_id`: `en_index_cohort04_spine` (planning placeholder — not a live link)

*Non-public COHORT_04 draft — {COHORT_ID} — engine v1.*
"""


def render_de_markdown(row: dict) -> str:
    h1 = row.get("h1_override") or build_h1(row)
    rid = row["route_id"]
    return f"""---
route_id: {rid}
status: draft
publication_status: non_public
indexable: false
in_sitemap: false
language: de
locale: de
source_language: de
cohort_id: {COHORT_ID}
generated: true
engine: {ENGINE}
---
# {h1}

**Entwurfsstatus:** Diese Seite ist ein **nichtöffentlicher Entwurf** für die **14.000-Seiten-Pipeline**. Sie ist **nicht veröffentlicht**, **nicht indexierbar**, **nicht in der Sitemap**, **nicht in der Navigation** und **nicht veröffentlichungsreif**. Dies ist **kein öffentlicher Launch**. **Kein Claim ist freigegeben**. **Keine Quellenfreigabe** wird impliziert.

## Seitenrolle

Kontrollierter **Terminologie-/Referenz-Eintrag** (`route_id`: `{rid}`) — keine Lehrbuch-, Blog-, Pilot- oder Glossar-Ersatzseite. Die Seite dient der **governed corpus expansion** innerhalb des festen **14.000-Seiten-Mindestziels**, nicht einem reduzierten Publikationsumfang.

## Terminologie-Schichten (Entwurfsprüfung)

- **Lexikalische Form** — Oberflächenschreibung, IUPAC-/Dokumentsprache und DE/EN-Grenzfragen under review **[SOURCE REQUIRED]**.
- **Chemische / Dokumentform** — beabsichtigter Geltungsbereich und Abgrenzung zu Nachbarbegriffen **[SOURCE REQUIRED]**.
- **Claim-Status** — **keine freigegebenen Claims**; Claim-Registries bleiben **inaktiv** für Massenpublikation.
- **Referenzschicht** — nomenklatur- und grenzorientiert; keine Betriebs-, Beschaffungs-, Markt- oder Sicherheitsanleitung.

## Abgrenzungen

Keine universellen Suffix-Regeln, keine Normansprüche, keine Betriebsanleitung, keine medizinischen oder Beschaffungsempfehlungen, keine Markt-/Handels-/CAGR-Inhalte. Stärkere Quellenbindung erforderlich **[SOURCE REQUIRED]**.

## Quellen- und Claim-Status

- Claim-Registries: **inaktiv**.
- Freigegebene Claims: **keine**.
- Source-locking: **nicht abgeschlossen**; `[SOURCE REQUIRED]` markiert offene Faktenzeilen.
- Dieser Entwurf entfernt **keine** `[SOURCE REQUIRED]`-Markierungen anderswo im Korpus.

## Veröffentlichungsblocker

- Route bleibt `planned`.
- Entwurf: `non_public`, nicht indexierbar, nicht in Sitemap/Navigation.
- `production_can_safely_proceed: no`.
- **14.000-Seiten-Mindestziel** unverändert — Pipeline-Expansion only.

## Interne Referenzrolle

Spätere Verlinkung per `route_id` `{rid}` — hier nur Planungsreferenz, keine Markdown-Links, keine Live-URLs.

*Nicht veröffentlichungsreifer Pipeline-Entwurf — {COHORT_ID} — `{rid}`.*
"""


def build_cohort04_rows(existing_ids: set[str], existing_paths: set[str]) -> list[dict]:
    rows: list[dict] = []
    seq = 1

    for entity, category in build_en_entity_catalog():
        for vkey, aud_key, ref_key, pt, aud, ref, template in ENTITY_VARIANTS:
            rid = f"cohort04_en_{entity}_{vkey}_{aud_key}_{ref_key}"
            if rid in existing_ids:
                continue
            path = f"/en/terminology/cohort04/{path_slug(entity)}/{vkey}/{aud_key}/{ref_key}/"
            if path in existing_paths:
                raise ValueError(f"path collision: {path}")
            rows.append({
                "inventory_row_id": f"INV-C04-{seq:05d}",
                "route_id": rid,
                "language": "en",
                "route_path": path,
                "term_or_entity": entity,
                "entity_category": category,
                "page_type_id": pt,
                "audience_id": aud,
                "reference_layer_id": ref,
                "template": template,
                "content_subdir": "cohort-04-expansion",
            })
            seq += 1

    for lang, rid, path, h1, page_family, template in build_single_routes():
        if rid in existing_ids:
            continue
        if path in existing_paths:
            raise ValueError(f"path collision: {path}")
        rows.append({
            "inventory_row_id": f"INV-C04-{seq:05d}",
            "route_id": rid,
            "language": lang,
            "route_path": path,
            "term_or_entity": rid,
            "h1_override": h1,
            "page_type_id": "PT_TERM_CANONICAL" if "terminology" in path else "PT_FOUNDATION",
            "audience_id": "ALL",
            "reference_layer_id": "REF_KNOWLEDGE",
            "template": template,
            "page_family": page_family,
            "content_subdir": "cohort-04-expansion/de" if lang == "de" else "cohort-04-expansion",
        })
        seq += 1

    if len(rows) != TARGET_NEW_ROUTES:
        raise ValueError(f"expected {TARGET_NEW_ROUTES} new rows, built {len(rows)}")
    return rows


def route_record_from_row(row: dict) -> dict:
    h1 = build_h1(row)
    title = f"{h1} | bisulfid.com"
    lang = row["language"]
    content_file = (
        f"main/content/{lang}/pages/{row['content_subdir']}/{row['route_id'].replace('_', '-')}.md"
    )
    layer = "terminology_system"
    pf = row.get("page_family", row.get("entity_category", ""))
    if pf in ("reference_governance",):
        layer = "foundation_reference"
    elif pf == "disambiguation":
        layer = "methodology_reference"
    elif pf == "gateway":
        layer = "gateway"
    elif pf == "de_terminology":
        layer = "terminology_system"
    return {
        "route_id": row["route_id"],
        "path": row["route_path"],
        "language": lang,
        "locale": lang,
        "source_language": lang,
        "title": title,
        "description": f"A governed reference draft: {h1} (planned route; non-public).",
        "h1": h1,
        "layer": layer,
        "template": row["template"],
        "content_file": content_file,
        "status": "planned",
        "indexable": False,
        "in_sitemap": False,
        "in_navigation": False,
        "translation_status": "source_planned",
        "hreflang_group": row["route_id"],
        "alternate_routes": {},
        "required_internal_links": ["en_foundation_sovereign_intro"],
        "required_claim_groups": ["terminology_claims"],
        "source_required": True,
        "risk_level": "medium",
        "notes": (
            f"Sprint 6M-F. COHORT_04 7,500-page pipeline expansion ({row.get('page_type_id', 'governed')}). "
            f"draft-backed; non-public; noindex. 14,000-page objective unchanged."
        ),
    }


def run(write: bool) -> int:
    print("=== Sprint 6M-F Corpus Expansion v1 ===")
    print(f"Date: {date.today().isoformat()}")
    print(f"Mode: {'write' if write else 'dry_run'}")
    print()

    routes_data = json.loads(ROUTES_PATH.read_text(encoding="utf-8"))
    routes = routes_data["routes"]
    existing_ids = {r["route_id"] for r in routes}
    existing_paths = {r["path"] for r in routes}
    before_count = len(routes)
    before_backed = sum(
        1 for r in routes if r.get("content_file") and (ROOT / r["content_file"]).is_file()
    )

    new_rows = build_cohort04_rows(existing_ids, existing_paths)
    new_routes = [route_record_from_row(r) for r in new_rows]
    for nr in new_routes:
        if nr["route_id"] in existing_ids:
            print(f"FAIL — duplicate route_id {nr['route_id']}")
            return 1
        if nr["path"] in existing_paths:
            print(f"FAIL — duplicate path {nr['path']}")
            return 1

    if write:
        routes_data["routes"] = routes + new_routes
        ROUTES_PATH.write_text(
            json.dumps(routes_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )

    fill_errors: list[str] = []
    drafts_written = 0
    for row in new_rows:
        body = render_de_markdown(row) if row["language"] == "de" else render_en_markdown(row)
        words = len(re.findall(r"\w+", body))
        if words < 150:
            fill_errors.append(f"{row['route_id']}: thin draft ({words} words)")
            continue
        if "[SOURCE REQUIRED]" not in body:
            fill_errors.append(f"{row['route_id']}: missing [SOURCE REQUIRED]")
            continue
        cf = route_record_from_row(row)["content_file"]
        if write:
            out = ROOT / cf
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(body, encoding="utf-8")
        drafts_written += 1

    if fill_errors:
        print("FAIL — validation errors:")
        for e in fill_errors[:20]:
            print(f"  - {e}")
        if len(fill_errors) > 20:
            print(f"  ... and {len(fill_errors) - 20} more")
        return 1

    after_routes = before_count + len(new_routes)
    after_backed = before_backed + drafts_written

    manifest = {
        "version": "1.0.0",
        "sprint": "6M-F",
        "cohort_id": COHORT_ID,
        "engine": ENGINE,
        "date": date.today().isoformat(),
        "routes_before": before_count,
        "routes_after": after_routes,
        "draft_backed_before": before_backed,
        "draft_backed_after": after_backed,
        "new_routes_added": len(new_routes),
        "target_new_routes": TARGET_NEW_ROUTES,
        "target_renderable": 7500,
        "en_entity_count": EN_ENTITY_COUNT,
        "single_route_count": SINGLE_ROUTE_COUNT,
    }
    inventory = {"version": "1.0.0", "cohort_id": COHORT_ID, "row_count": len(new_rows), "rows": new_rows}

    if write:
        INVENTORY_OUT.write_text(json.dumps(inventory, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        MANIFEST_OUT.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        links_data = json.loads(INTERNAL_LINKS_PATH.read_text(encoding="utf-8"))
        links_data["link_groups"].append({
            "from_route_id": "en_index_cohort04_spine",
            "status": "planned",
            "intended_links": ["en_foundation_sovereign_intro", "en_index_terminology_spine"],
        })
        INTERNAL_LINKS_PATH.write_text(
            json.dumps(links_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )

    print(f"Routes: {before_count} -> {after_routes}")
    print(f"Draft-backed (projected): {after_backed}")
    print(f"New COHORT_04 routes: {len(new_routes)}")
    print("PASS — expansion plan validated")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="Write routes, content, and manifests")
    args = parser.parse_args()
    return run(write=args.write)


if __name__ == "__main__":
    sys.exit(main())
