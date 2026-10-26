import sys
sys.path.insert(0, "scripts/sec_edgar")
from harvest_efts import run
import time
# Second wave: EX-10 oriented terms & customer-facing contract words (6-K/8-K/10-K/10-Q/20-F/40-F)
Q2 = [
 ('"supply agreement" customer', "8-K,6-K,10-K,10-Q,20-F,40-F", "supply_cust"),
 ('"master services agreement" customer', "8-K,6-K,10-K,10-Q,20-F,40-F", "msa_cust"),
 ('"software license agreement"', None, "sw_license"),
 ('"software as a service" agreement', "8-K,6-K,10-K,10-Q", "saas"),
 ('"contract manufacturing agreement"', None, "cmo"),
 ('"toll manufacturing" OR "tolling agreement"', None, "toll"),
 ('"exclusive distribution agreement"', None, "excl_dist"),
 ('"licensing and supply agreement" OR "license and supply agreement"', None, "lic_supply"),
 ('"sales agreement" product OR products', "6-K,8-K", "sales_agmt"),
 ('"purchase order" "term of" years', "6-K,8-K", "po_term"),
 ('"concentrate sales agreement" OR "offtake" copper OR zinc OR nickel OR lithium', "6-K,8-K,40-F,20-F", "offtake_metal"),
 ('"gas sales agreement" OR "crude oil sales agreement" OR "transportation services agreement"', "6-K,8-K,40-F,10-K", "oilgas_sales"),
 ('"agreement" "Item 1.01"', "8-K", "item101b"),
 ('"material definitive agreement" supply OR services OR license', "8-K", "mda_supply"),
 ('"strategic agreement" OR "strategic supply agreement"', None, "strategic"),
 ('"collaboration and license agreement"', None, "collab_lic"),
 ('"option and license agreement"', None, "option_lic"),
 ('"letter agreement" supply', "6-K,8-K", "letter_supply"),
 ('"hosting agreement" OR "colocation agreement" OR "hosting services agreement"', None, "hosting"),
 ('"managed services agreement"', None, "managed_services"),
 ('"deployment agreement" OR "installation agreement"', None, "deployment"),
 ('"royalty" agreement customer license', "6-K,8-K,40-F,20-F", "royalty_cust"),
 ('"non-exclusive license" agreement', "6-K,8-K", "nonexcl"),
 ('"fleet" "purchase agreement" OR "vehicle purchase agreement" OR "vessel construction"', None, "fleet"),
 ('"engineering services" agreement', "6-K,8-K", "eng_services"),
 ('"consulting services agreement" company provides', "6-K,8-K", "consult_services"),
 ('"term of the agreement" years customer', "6-K,8-K", "term_cust"),
 ('"renewal" agreement customer "five years" OR "three years" OR "ten years"', "6-K,8-K", "renewal"),
 ('"ambulance" OR "transit" OR "buses" agreement supply', "6-K,8-K", "transit"),
 ('"nuclear" OR "SMR" OR "fuel" supply agreement', "6-K,8-K,40-F", "nuclear"),
]
for qtext, forms, label in Q2:
    run(qtext, forms, label)
    time.sleep(0.3)
print("DONE wave 2")
