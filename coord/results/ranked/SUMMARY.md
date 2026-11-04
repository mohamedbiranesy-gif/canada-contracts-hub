# Ranked buyers — 2026-11-04T08:45Z

```
leads with a borrowed mailbox: 2425 | rows upgraded by a newer dated record: 41 | rows upgraded to an active service seen on the buyer's site: 12
P12 organisations: 108 added: 23 {'no own confirmed mailbox': 64, 'same organisation already in a row': 21} | P13 added: 28396 | P13 skipped: {'bad mailbox': 84, 'not located in Canada (no honest inference)': 1212, "mailbox not the organisation's own": 2131, 'same organisation already in a row (domain / mailbox / name)': 6891}
extras from the lanes' result rows: {'invoicing_requirements': 1847, 'invoice_portal_url': 84, 'ap_phone': 2103, 'invoice_mailing_address': 2040, 'ap_contact_name': 109}
org_extras: 46185 organisations read; filled {'vendor_logo': 7770, 'po_required': 191, 'buyer_legal_name': 7149, 'buyer_logo': 27827, 'payment_terms': 133, 'buyer_bn': 1548, 'vendor_legal_name': 1411, 'vendor_neq': 31, 'vendor_bn': 169, 'vendor_qst': 4}
mx_check: 45279 domains known; 164 mailboxes on domains with no mail server removed
org_contacts: 40004 organisations read; filled {'vendor_phone': 15427, 'vendor_emails': 2198, 'buyer_phone': 19691, 'buyer_address': 15103, 'vendor_address': 2649}
rows 43472
[('GOLD', 561), ('A0', 532), ('A1', 803), ('A2', 92), ('A3', 146), ('A4', 14), ('B0', 649), ('B1', 886), ('B2', 153), ('B3', 130), ('B4', 10), ('C0', 1034), ('C1', 320), ('C2', 14), ('C3', 27), ('C4', 23), ('D0', 108), ('D1', 2976), ('D2', 112), ('D3', 120), ('D4', 151), ('E0', 92), ('E1', 2599), ('E2', 42), ('E3', 54), ('E4', 59), ('F1', 14), ('F2', 2), ('F3', 2), ('F4', 5), ('GOLD-M', 16), ('GOLD-T', 90), ('I0', 128), ('I1', 27347), ('I2', 122), ('I3', 563), ('I4', 236), ('L0', 220), ('L1', 273), ('L2', 32), ('L3', 17), ('L4', 63), ('M0', 9), ('M1', 133), ('M2', 9), ('M3', 27), ('M4', 1), ('T0', 15), ('T1', 2329), ('T2', 52), ('T3', 58), ('T4', 2)]
with any email: 40685 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            561
P01T_active_service_seen_on_buyer_site_invoicing_AP_email     90
P02_active_relationship_finance_accounting_email           261
P03_active_relationship_purchasing_email                   236
P04_active_relationship_general_email                     1617
P05_likely_active_awarded_12_36_months_any_email           373
P06_client_listing_invoicing_AP_email                      142
P06T_active_service_seen_on_buyer_site_other_email        2421
P07_client_listing_finance_or_purchasing_email             214
P08_client_listing_general_email                          2854
P09_older_contract_or_payment_any_email                    364
P10_linked_from_vendor_site_any_email                     2600
P11_any_relationship_email_not_yet_confirmed               475
P12_weaker_relationship_within_5_years_own_email            23
P13_inferred_relationship_no_record_own_email            28268
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email     16
P06M_member_or_regulated_payer_of_canadian_body_other_email    167
Z_no_email_yet_not_delivered                              2790
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 1460090
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
