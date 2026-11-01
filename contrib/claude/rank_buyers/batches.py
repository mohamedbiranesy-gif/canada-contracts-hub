import csv, collections, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
rows = list(csv.DictReader(open(ROOT + "/out/ranked/ranked_buyers.csv", encoding="utf-8")))
B = collections.OrderedDict([
 ("1_GOLD_active_contract_invoicing_email", lambda r: r["rank_group"] == "GOLD"),
 ("1b_active_contract_finance_accounting_email", lambda r: r["rank_group"] in ("A3", "B3") and r["email_check"] in ("confirmed", "from dataset enrichment")),
 ("2_active_contract_purchasing_email", lambda r: r["rank_group"] in ("A2", "B2") and r["email_check"] in ("confirmed", "from dataset enrichment")),
 ("3_active_contract_general_email", lambda r: r["rank_group"] in ("A1", "B1") and r["email_check"] in ("confirmed", "from dataset enrichment")),
 ("4_active_contract_email_not_yet_confirmed", lambda r: r["rank_group"][0] in "AB" and r["rank_group"] != "GOLD" and r["email"] and r["email_check"] not in ("confirmed", "from dataset enrichment")),
 ("5_active_contract_no_email_yet", lambda r: r["rank_group"] in ("A0", "B0")),
 ("6_payment_or_subaward_record_confirmed_email", lambda r: r["contract_status"] == "payment / subaward record" and r["email_check"] == "confirmed"),
 ("6b_client_listing_on_vendor_site_confirmed_email", lambda r: r["contract_status"].startswith("client listing") and r["email_check"] == "confirmed"),
 ("6c_relationship_email_not_yet_confirmed", lambda r: r["contract_status"] == "payment / subaward record" or r["contract_status"].startswith("client listing")),
 ("7_older_contract_with_email", lambda r: r["rank_group"] in ("C1", "C2", "C3", "C4") ),
 ("8_older_contract_no_email", lambda r: r["rank_group"] == "C0"),
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
