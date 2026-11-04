# Ranked buyers — 2026-11-04T09:47Z

```
leads with a borrowed mailbox: 2400 | rows upgraded by a newer dated record: 41 | rows upgraded to an active service seen on the buyer's site: 12
P12 organisations: 108 added: 23 {'no own confirmed mailbox': 64, 'same organisation already in a row': 21} | P13 added: 31997 | P13 skipped: {'bad mailbox': 84, 'not located in Canada (no honest inference)': 2396, "mailbox not the organisation's own": 2131, 'same organisation already in a row (domain / mailbox / name)': 7055}
extras from the lanes' result rows: {'invoicing_requirements': 1847, 'invoice_portal_url': 84, 'ap_phone': 2102, 'invoice_mailing_address': 2040, 'ap_contact_name': 112}
org_extras: 46185 organisations read; filled {'vendor_logo': 7814, 'po_required': 193, 'buyer_legal_name': 7150, 'buyer_logo': 27835, 'payment_terms': 140, 'buyer_bn': 1550, 'vendor_legal_name': 1418, 'vendor_neq': 31, 'vendor_bn': 173, 'vendor_qst': 4}
mx_check: 49934 domains known; 181 mailboxes on domains with no mail server removed
org_contacts: 40004 organisations read; filled {'vendor_phone': 16626, 'vendor_emails': 2210, 'buyer_phone': 19697, 'buyer_address': 15143, 'vendor_address': 2664}
rows 47204
[('GOLD', 566), ('A0', 532), ('A1', 803), ('A2', 92), ('A3', 146), ('A4', 14), ('B0', 649), ('B1', 911), ('B2', 151), ('B3', 127), ('B4', 10), ('C0', 1034), ('C1', 320), ('C2', 14), ('C3', 27), ('C4', 23), ('D0', 109), ('D1', 3062), ('D2', 116), ('D3', 126), ('D4', 157), ('E0', 93), ('E1', 2600), ('E2', 43), ('E3', 55), ('E4', 59), ('F1', 14), ('F2', 2), ('F3', 2), ('F4', 5), ('GOLD-M', 17), ('GOLD-T', 90), ('I0', 144), ('I1', 30834), ('I2', 124), ('I3', 639), ('I4', 256), ('L0', 219), ('L1', 272), ('L2', 32), ('L3', 17), ('L4', 63), ('M0', 9), ('M1', 133), ('M2', 9), ('M3', 27), ('M4', 1), ('T0', 15), ('T1', 2329), ('T2', 52), ('T3', 58), ('T4', 2)]
with any email: 44400 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            566
P01T_active_service_seen_on_buyer_site_invoicing_AP_email     90
P02_active_relationship_finance_accounting_email           258
P03_active_relationship_purchasing_email                   234
P04_active_relationship_general_email                     1642
P05_likely_active_awarded_12_36_months_any_email           372
P06_client_listing_invoicing_AP_email                      148
P06T_active_service_seen_on_buyer_site_other_email        2421
P07_client_listing_finance_or_purchasing_email             224
P08_client_listing_general_email                          2939
P09_older_contract_or_payment_any_email                    364
P10_linked_from_vendor_site_any_email                     2603
P11_any_relationship_email_not_yet_confirmed               476
P12_weaker_relationship_within_5_years_own_email            23
P13_inferred_relationship_no_record_own_email            31853
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email     17
P06M_member_or_regulated_payer_of_canadian_body_other_email    167
Z_no_email_yet_not_delivered                              2807
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 1613753
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
