# Ranked buyers — 2026-11-04T23:48Z

```
mailboxes taken from the verification log (better than org_mailboxes' single pick): 625
leads with a borrowed mailbox: 2253 | rows upgraded by a newer dated record: 38 | rows upgraded to an active service seen on the buyer's site: 12
P12 organisations: 108 added: 23 {'no own confirmed mailbox': 67, 'same organisation already in a row': 18} | P13 added: 43545 | P13 skipped: {'bad mailbox': 187, 'not located in Canada (no honest inference)': 2485, "mailbox not the organisation's own": 2142, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 7401}
extras from the lanes' result rows: {'invoicing_requirements': 1614, 'invoice_portal_url': 68, 'ap_phone': 1986, 'invoice_mailing_address': 1899, 'ap_contact_name': 136}
org_extras: 51730 organisations read; filled {'vendor_logo': 7983, 'po_required': 147, 'buyer_legal_name': 6995, 'buyer_logo': 32112, 'payment_terms': 168, 'buyer_bn': 1623, 'vendor_legal_name': 1300, 'vendor_neq': 31, 'p13_name_from_legal_name': 1804, 'vendor_bn': 174, 'vendor_qst': 4, 'p13_name_from_domain': 5}
regional mailboxes of multinationals removed from other-country entities: 18
mx_check: 58354 domains known; 215 mailboxes on domains with no mail server removed; 187 webmail (freemail) addresses removed
dmarc/spf: 58350 domains known; rows {'enforced': 14141, 'exposed': 38631}
same organisation under another key folded into the row that holds its mailbox: 53
second mailbox of the same organisation (same site and mail domain, same name family) folded: 5
org_contacts: 45050 organisations read; filled {'vendor_phone': 18363, 'vendor_emails': 2252, 'buyer_phone': 22526, 'buyer_address': 18329, 'vendor_address': 2753}
narrative columns: {'mailbox meta found': 53791, 'mailbox meta missing': 2126}
rows 58895
[('GOLD', 579), ('A0', 514), ('A1', 745), ('A2', 93), ('A3', 206), ('A4', 9), ('B0', 626), ('B1', 906), ('B2', 142), ('B3', 164), ('B4', 11), ('C0', 1014), ('C1', 310), ('C2', 16), ('C3', 33), ('C4', 25), ('D0', 116), ('D1', 3179), ('D2', 115), ('D3', 148), ('D4', 169), ('E0', 99), ('E1', 2580), ('E2', 42), ('E3', 72), ('E4', 57), ('F0', 1), ('F1', 11), ('F2', 2), ('F3', 4), ('F4', 5), ('GOLD-M', 18), ('GOLD-T', 90), ('I0', 359), ('I1', 41925), ('I2', 163), ('I3', 822), ('I4', 276), ('L0', 218), ('L1', 269), ('L2', 30), ('L3', 22), ('L4', 66), ('M0', 10), ('M1', 135), ('M2', 9), ('M3', 27), ('M4', 1), ('T0', 21), ('T1', 2319), ('T2', 48), ('T3', 72), ('T4', 2)]
with any email: 55917 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            579
P01T_active_service_seen_on_buyer_site_invoicing_AP_email     90
P02_active_relationship_finance_accounting_email           366
P03_active_relationship_purchasing_email                   225
P04_active_relationship_general_email                     1571
P05_likely_active_awarded_12_36_months_any_email           375
P06_client_listing_invoicing_AP_email                      160
P06T_active_service_seen_on_buyer_site_other_email        2423
P07_client_listing_finance_or_purchasing_email             245
P08_client_listing_general_email                          3059
P09_older_contract_or_payment_any_email                    364
P10_linked_from_vendor_site_any_email                     2605
P11_any_relationship_email_not_yet_confirmed               457
P12_weaker_relationship_within_5_years_own_email            22
P13_inferred_relationship_no_record_own_email (5 part files)  43186
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email     18
P06M_member_or_regulated_payer_of_canadian_body_other_email    169
Z_no_email_yet_not_delivered                              2981
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 2654187
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
