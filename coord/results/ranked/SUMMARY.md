# Ranked buyers — 2026-11-07T00:02Z

```
mailboxes taken from the verification log (better than org_mailboxes' single pick): 625
leads with a borrowed mailbox: 2254 | rows upgraded by a newer dated record: 38 | rows upgraded to an active service seen on the buyer's site: 12
P12 organisations: 107 added: 23 {'no own confirmed mailbox': 66, 'same organisation already in a row': 18} | P13 added: 50931 | P13 skipped: {'bad mailbox': 187, 'not located in Canada (no honest inference)': 2492, "mailbox not the organisation's own": 2142, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 7622}
extras from the lanes' result rows: {'invoicing_requirements': 1618, 'invoice_portal_url': 68, 'ap_phone': 1990, 'invoice_mailing_address': 1901, 'ap_contact_name': 138}
org_extras: 51730 organisations read; filled {'vendor_logo': 7998, 'po_required': 149, 'buyer_legal_name': 6998, 'buyer_logo': 32116, 'payment_terms': 179, 'buyer_bn': 1623, 'vendor_legal_name': 1299, 'vendor_neq': 31, 'p13_name_from_legal_name': 1806, 'vendor_bn': 174, 'vendor_qst': 4, 'p13_name_from_domain': 5}
regional mailboxes of multinationals removed from other-country entities: 18
mx_check: 58354 domains known; 215 mailboxes on domains with no mail server removed; 223 webmail (freemail) addresses removed
dmarc/spf: 58350 domains known; rows {'enforced': 14145, 'exposed': 38666}
same organisation under another key folded into the row that holds its mailbox: 53
second mailbox of the same organisation (same site and mail domain, same name family) folded: 5
org_contacts: 45050 organisations read; filled {'vendor_phone': 19420, 'vendor_emails': 2252, 'buyer_phone': 22528, 'buyer_address': 18333, 'vendor_address': 2752}
narrative columns: {'mailbox meta found': 61198, 'mailbox meta missing': 2127}
rows 66344
[('GOLD', 579), ('A0', 515), ('A1', 743), ('A2', 92), ('A3', 206), ('A4', 9), ('B0', 627), ('B1', 960), ('B2', 143), ('B3', 166), ('B4', 11), ('C0', 1014), ('C1', 312), ('C2', 16), ('C3', 33), ('C4', 25), ('D0', 116), ('D1', 3178), ('D2', 115), ('D3', 148), ('D4', 169), ('E0', 99), ('E1', 2581), ('E2', 42), ('E3', 72), ('E4', 57), ('F0', 1), ('F1', 11), ('F2', 2), ('F3', 4), ('F4', 5), ('GOLD-M', 18), ('GOLD-T', 91), ('I0', 395), ('I1', 49124), ('I2', 174), ('I3', 929), ('I4', 309), ('L0', 221), ('L1', 271), ('L2', 30), ('L3', 23), ('L4', 67), ('M0', 10), ('M1', 136), ('M2', 9), ('M3', 27), ('M4', 1), ('T0', 21), ('T1', 2316), ('T2', 48), ('T3', 72), ('T4', 1)]
with any email: 63325 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            579
P01T_active_service_seen_on_buyer_site_invoicing_AP_email     91
P02_active_relationship_finance_accounting_email           368
P03_active_relationship_purchasing_email                   225
P04_active_relationship_general_email                     1625
P05_likely_active_awarded_12_36_months_any_email           377
P06_client_listing_invoicing_AP_email                      160
P06T_active_service_seen_on_buyer_site_other_email        2422
P07_client_listing_finance_or_purchasing_email             246
P08_client_listing_general_email                          3051
P09_older_contract_or_payment_any_email                    367
P10_linked_from_vendor_site_any_email                     2606
P11_any_relationship_email_not_yet_confirmed               459
P12_weaker_relationship_within_5_years_own_email            22
P13_inferred_relationship_no_record_own_email (6 part files)  50536
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email     18
P06M_member_or_regulated_payer_of_canadian_body_other_email    170
Z_no_email_yet_not_delivered                              3022
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 3942977
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
