import csv, collections, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
rows = list(csv.DictReader(open(ROOT + "/out/ranked/ranked_buyers.csv", encoding="utf-8")))
OK = ("confirmed",)  # owner 2026-11-04 ("ironclad"): referee-confirmed only; dataset-enrichment mailboxes wait in P11 until the referee has seen them
def rel(r):
    st, t = r["contract_status"], r.get("tier", "")
    return ("weak" if t == "F" else "inferred" if t == "I" else "member" if t == "M" else
            "tech" if st.startswith("active service seen") else "client" if st.startswith("client listing") else "other_link" if st.startswith("linked from") else
            "older" if st.startswith(("end date unknown", "payment / subaward")) else "likely" if st.startswith("likely active (awarded 12-36") else "active")
# One row per buyer, in the best package it qualifies for (owner's layout, 2026-11-01): every package row has an email.
B = collections.OrderedDict([
 ("P01_GOLD_active_relationship_invoicing_AP_email", lambda r: r["rank_group"] == "GOLD"),
 ("P01T_active_service_seen_on_buyer_site_invoicing_AP_email", lambda r: r["rank_group"] == "GOLD-T"),
 ("P02_active_relationship_finance_accounting_email", lambda r: rel(r) == "active" and r["grade"] == "3" and r["email_check"] in OK),
 ("P03_active_relationship_purchasing_email", lambda r: rel(r) == "active" and r["grade"] == "2" and r["email_check"] in OK),
 ("P04_active_relationship_general_email", lambda r: rel(r) == "active" and r["grade"] == "1" and r["email_check"] in OK),
 ("P05_likely_active_awarded_12_36_months_any_email", lambda r: rel(r) == "likely" and r["email"] and r["email_check"] in OK),
 ("P06_client_listing_invoicing_AP_email", lambda r: rel(r) == "client" and r["grade"] == "4" and r["email_check"] in OK),
 ("P06T_active_service_seen_on_buyer_site_other_email", lambda r: rel(r) == "tech" and r["email"] and r["email_check"] in OK),
 ("P07_client_listing_finance_or_purchasing_email", lambda r: rel(r) == "client" and r["grade"] in ("2", "3") and r["email_check"] in OK),
 ("P08_client_listing_general_email", lambda r: rel(r) == "client" and r["grade"] == "1" and r["email_check"] in OK),
 ("P09_older_contract_or_payment_any_email", lambda r: rel(r) == "older" and r["email"] and r["email_check"] in OK),
 ("P10_linked_from_vendor_site_any_email", lambda r: rel(r) == "other_link" and r["email"] and r["email_check"] in OK),
 ("P11_any_relationship_email_not_yet_confirmed", lambda r: bool(r["email"]) and rel(r) not in ("weak", "inferred", "member")),
 # owner 2026-11-03: P12 weaker relationship within 5 years (ended contract, or vendor in Canada only by registry match),
 # P13 inferred relationship (no record) from the buyer's type and province; both need the buyer's own confirmed mailbox
 ("P12_weaker_relationship_within_5_years_own_email", lambda r: rel(r) == "weak" and r["email"] and r["email_check"] in OK),
 ("P13_inferred_relationship_no_record_own_email", lambda r: rel(r) == "inferred" and r["email"] and r["email_check"] in OK),
 # claude 2026-11-03 (owner: "no door closed"; own package, never mixed with P01): the organisation is on the CURRENT member /
 # participant / regulated-institution list that a Canadian body publishes, and pays that body (premiums, market charges,
 # assessments, dues; the fee basis is quoted); P01M needs the organisation's own confirmed invoicing mailbox
 ("P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email", lambda r: r["rank_group"] == "GOLD-M"),
 ("P06M_member_or_regulated_payer_of_canadian_body_other_email", lambda r: rel(r) == "member" and r["email"] and r["email_check"] in OK),
 ("Z_no_email_yet_not_delivered", lambda r: True),
])
# owner 2026-11-03 "make sure all the fields are populated": a field no source gives is written as the literal
# not_published (never blank); Z has no mailbox found yet, which is not the same as none published.
EMAIL_COLS = ("email", "email_type", "email_check", "email_evidence_url", "email_evidence_quote")
GST_LABEL = " (derived: BN9 + RT0001, not confirmed in the CRA registry)"
def filled(r, package):
    r = dict(r)
    if r.get("vendor_gst_hst_derived") and "derived" not in r["vendor_gst_hst_derived"]:
        r["vendor_gst_hst_derived"] += GST_LABEL
    for c in r:
        v = (r[c] or "").strip()
        if v in ("", "{}", "[]", "null", "None"):
            r[c] = "not_found_yet" if (package.startswith("Z") and c in EMAIL_COLS) else "not_published"
    return r
os.makedirs(ROOT + "/out/ranked/batches", exist_ok=True)
used, summary, blank = set(), [], collections.Counter()
for name, f in B.items():
    sel = [r for i, r in enumerate(rows) if i not in used and f(r)]
    for i, r in enumerate(rows):
        if i not in used and f(r): used.add(i)
    sel.sort(key=lambda r: -int(float(r["completeness_score"] or 0)))
    blank[name] = sum(1 for r in sel for c in r if (r[c] or "").strip() in ("", "{}"))
    with open(ROOT + "/out/ranked/batches/%s.csv" % name, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(filled(r, name) for r in sel)
    summary.append((name, len(sel)))
left = [r for i, r in enumerate(rows) if i not in used]
for n, c in summary: print("%-55s %6d" % (n, c))
print("unassigned", len(left), collections.Counter(r["rank_group"] for r in left).most_common(5))
print("blank cells filled with not_published (delivered P01-P13):", sum(v for k, v in blank.items() if not k.startswith("Z")))
