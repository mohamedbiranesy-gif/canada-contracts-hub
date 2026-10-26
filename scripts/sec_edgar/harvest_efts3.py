import sys
sys.path.insert(0, "scripts/sec_edgar")
from harvest_efts import run
import time
Q3 = [
 ('"Supplier shall" OR "Seller shall deliver" OR "Vendor shall provide"', None, "supplier_shall"),
 ('"Purchase Orders" "Products" "Customer"', "8-K,6-K,10-K,10-Q,20-F,40-F", "po_products_customer"),
 ('"Service Level" OR "Service Levels" agreement "Customer"', "8-K,6-K,10-K,10-Q", "sla"),
 ('"Licensee shall pay" royalty', "8-K,6-K,10-K,10-Q,20-F,40-F", "licensee_pays"),
 ('"exclusive distributor" agreement', None, "excl_distributor"),
 ('"colocation" OR "co-location" agreement megawatts', None, "colo_mw"),
 ('"hosting services" agreement miners OR "mining machines"', None, "hosting_miners"),
 ('"agreement" "Department of National Defence" OR "Public Services and Procurement Canada" contract award', None, "canada_gov_contract"),
 ('"contract" awarded "U.S. Army" OR "U.S. Navy" OR "U.S. Air Force" OR "Department of Defense"', "6-K,8-K", "us_dod_contract"),
 ('"master services agreement" OR "statement of work" "data center"', None, "msa_datacenter"),
 ('"supply agreement" lithium OR nickel OR graphite OR uranium OR copper', "6-K,8-K,40-F,20-F,10-K", "supply_minerals"),
 ('"offtake agreement" OR "off-take agreement"', "6-K,40-F,20-F", "offtake_6k"),
 ('"distribution and supply agreement" OR "supply and distribution agreement"', None, "dist_supply"),
 ('"manufacturing and supply agreement"', None, "mfg_supply"),
 ('"software license" OR "software licence" agreement "annual fee" OR "subscription fee"', "6-K,8-K,10-K,10-Q", "sw_fee"),
]
for qtext, forms, label in Q3:
    run(qtext, forms, label); time.sleep(0.3)
print("DONE wave 3")
