# Ranked buyers — 2026-11-04T07:30Z

```
leads with a borrowed mailbox: 2377 | rows upgraded by a newer dated record: 40 | rows upgraded to an active service seen on the buyer's site: 12
P12 organisations: 108 added: 23 {'no own confirmed mailbox': 64, 'same organisation already in a row': 21} | P13 added: 27562 | P13 skipped: {'bad mailbox': 84, 'not located in Canada (no honest inference)': 1113, "mailbox not the organisation's own": 2130, 'same organisation already in a row (domain / mailbox / name)': 6800}
extras from the lanes' result rows: {'invoicing_requirements': 1846, 'invoice_portal_url': 84, 'ap_phone': 2100, 'invoice_mailing_address': 2038, 'ap_contact_name': 95}
org_extras: 28904 organisations read; filled {'vendor_logo': 7552, 'po_required': 190, 'buyer_legal_name': 6420, 'buyer_logo': 25634, 'payment_terms': 131, 'buyer_bn': 1365, 'vendor_legal_name': 1330, 'vendor_neq': 31, 'vendor_bn': 165, 'vendor_qst': 4}
mx_check: 44037 domains known; 159 mailboxes on domains with no mail server removed
org_contacts: 40004 organisations read; filled {'vendor_phone': 15229, 'vendor_emails': 2187, 'buyer_phone': 19688, 'buyer_address': 15099, 'vendor_address': 2630}
rows 42464
[('GOLD', 560), ('A0', 532), ('A1', 803), ('A2', 92), ('A3', 146), ('A4', 14), ('B0', 649), ('B1', 869), ('B2', 153), ('B3', 130), ('B4', 10), ('C0', 1034), ('C1', 320), ('C2', 14), ('C3', 27), ('C4', 23), ('D0', 106), ('D1', 2840), ('D2', 99), ('D3', 115), ('D4', 146), ('E0', 92), ('E1', 2601), ('E2', 43), ('E3', 54), ('E4', 59), ('F1', 14), ('F2', 2), ('F3', 2), ('F4', 5), ('GOLD-M', 16), ('GOLD-T', 90), ('I0', 123), ('I1', 26535), ('I2', 123), ('I3', 548), ('I4', 233), ('L0', 219), ('L1', 273), ('L2', 32), ('L3', 17), ('L4', 64), ('M0', 9), ('M1', 134), ('M2', 9), ('M3', 27), ('M4', 1), ('T0', 15), ('T1', 2330), ('T2', 52), ('T3', 58), ('T4', 2)]
with any email: 39685 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            560
P01T_active_service_seen_on_buyer_site_invoicing_AP_email     90
P02_active_relationship_finance_accounting_email           261
P03_active_relationship_purchasing_email                   236
P04_active_relationship_general_email                     1600
P05_likely_active_awarded_12_36_months_any_email           374
P06_client_listing_invoicing_AP_email                      137
P06T_active_service_seen_on_buyer_site_other_email        2422
P07_client_listing_finance_or_purchasing_email             196
P08_client_listing_general_email                          2717
P09_older_contract_or_payment_any_email                    364
P10_linked_from_vendor_site_any_email                     2603
P11_any_relationship_email_not_yet_confirmed               476
P12_weaker_relationship_within_5_years_own_email            23
P13_inferred_relationship_no_record_own_email            27439
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email     16
P06M_member_or_regulated_payer_of_canadian_body_other_email    168
Z_no_email_yet_not_delivered                              2782
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 1422343
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
