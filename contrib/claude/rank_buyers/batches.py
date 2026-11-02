import csv, collections, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
rows = list(csv.DictReader(open(ROOT + "/out/ranked/ranked_buyers.csv", encoding="utf-8")))
OK = ("confirmed", "from dataset enrichment")
def rel(r):
    st = r["contract_status"]
    return ("client" if st.startswith("client listing") else "other_link" if st.startswith("linked from") else
            "older" if st.startswith(("end date unknown", "payment / subaward")) else "likely" if st.startswith("likely active (awarded 12-36") else "active")
# One row per buyer, in the best package it qualifies for (owner's layout, 2026-11-01): every package row has an email.
B = collections.OrderedDict([
 ("P01_GOLD_active_relationship_invoicing_AP_email", lambda r: r["rank_group"] == "GOLD"),
 ("P02_active_relationship_finance_accounting_email", lambda r: rel(r) == "active" and r["grade"] == "3" and r["email_check"] in OK),
 ("P03_active_relationship_purchasing_email", lambda r: rel(r) == "active" and r["grade"] == "2" and r["email_check"] in OK),
 ("P04_active_relationship_general_email", lambda r: rel(r) == "active" and r["grade"] == "1" and r["email_check"] in OK),
 ("P05_likely_active_awarded_12_36_months_any_email", lambda r: rel(r) == "likely" and r["email"] and r["email_check"] in OK),
 ("P06_client_listing_invoicing_AP_email", lambda r: rel(r) == "client" and r["grade"] == "4" and r["email_check"] in OK),
 ("P07_client_listing_finance_or_purchasing_email", lambda r: rel(r) == "client" and r["grade"] in ("2", "3") and r["email_check"] in OK),
 ("P08_client_listing_general_email", lambda r: rel(r) == "client" and r["grade"] == "1" and r["email_check"] in OK),
 ("P09_older_contract_or_payment_any_email", lambda r: rel(r) == "older" and r["email"] and r["email_check"] in OK),
 ("P10_linked_from_vendor_site_any_email", lambda r: rel(r) == "other_link" and r["email"] and r["email_check"] in OK),
 ("P11_any_relationship_email_not_yet_confirmed", lambda r: bool(r["email"])),
 ("Z_no_email_yet_not_delivered", lambda r: True),
])
os.makedirs(ROOT + "/out/ranked/batches", exist_ok=True)
used, summary = set(), []
for name, f in B.items():
    sel = [r for i, r in enumerate(rows) if i not in used and f(r)]
    for i, r in enumerate(rows):
        if i not in used and f(r): used.add(i)
    sel.sort(key=lambda r: -int(float(r["completeness_score"] or 0)))
    with open(ROOT + "/out/ranked/batches/%s.csv" % name, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(sel)
    summary.append((name, len(sel)))
left = [r for i, r in enumerate(rows) if i not in used]
for n, c in summary: print("%-55s %6d" % (n, c))
print("unassigned", len(left), collections.Counter(r["rank_group"] for r in left).most_common(5))
