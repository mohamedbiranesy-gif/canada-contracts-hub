"""Wave 4: press-release-style phrasing inside 6-K / 8-K exhibits by Canadian-located filers
(announced contract awards with named counterparties)."""
import sys
sys.path.insert(0, "scripts/sec_edgar")
from harvest_efts import run
import time
Q4 = [
 ('"awarded a contract" OR "has been awarded" OR "contract award"', "6-K,8-K", "pr_awarded"),
 ('"signed a contract" OR "signs contract" OR "entered into a contract with"', "6-K,8-K", "pr_signed_contract"),
 ('"purchase order" received OR awarded', "6-K,8-K", "pr_purchase_order"),
 ('"selected by" OR "has selected" OR "chosen by"', "6-K,8-K", "pr_selected"),
 ('"multi-year" agreement OR contract', "6-K,8-K", "pr_multiyear"),
 ('"five-year" OR "ten-year" OR "three-year" contract OR agreement', "6-K,8-K", "pr_nyear"),
 ('"long-term" "supply agreement" OR "offtake agreement" OR "service agreement"', "6-K,8-K", "pr_longterm"),
 ('"binding" "offtake" agreement signed', "6-K,8-K", "pr_binding_offtake"),
 ('"power purchase agreement" signed OR executed OR awarded', "6-K,8-K,40-F", "pr_ppa"),
 ('"Department of National Defence" OR "Canadian Armed Forces" contract awarded', "6-K,8-K,40-F", "pr_dnd"),
 ('"U.S. Army" OR "U.S. Navy" OR "U.S. Air Force" OR "Department of Defense" OR "Department of War" contract awarded', "6-K,8-K", "pr_usdod"),
 ('"Public Services and Procurement Canada" OR "Government of Canada" contract awarded OR "has awarded"', "6-K,8-K", "pr_govcan"),
 ('"transit" OR "buses" contract awarded "transit authority" OR "transit agency"', "6-K,8-K", "pr_transit"),
 ('"hospital" OR "health authority" OR "NHS" contract OR agreement signed deploy', "6-K,8-K", "pr_health"),
 ('"utility" OR "hydro" contract awarded OR signed "megawatt" OR "MW"', "6-K,8-K", "pr_utility"),
 ('"mining" "contract" awarded OR signed "services" "mine"', "6-K,8-K", "pr_mining_services"),
 ('"software" "agreement" "customer" signed OR selected "enterprise"', "6-K,8-K", "pr_software_customer"),
 ('"subscription" OR "SaaS" "contract" "annual recurring revenue" signed customer', "6-K,8-K", "pr_saas"),
 ('"order" "units" OR "systems" OR "vehicles" delivered OR deliveries "customer" named', "6-K,8-K", "pr_order_units"),
 ('"framework agreement" OR "standing offer" OR "supply arrangement" awarded', "6-K,8-K,40-F", "pr_framework"),
]
for qtext, forms, label in Q4:
    run(qtext, forms, label); time.sleep(0.3)
print("DONE wave 4")
