# Ranked buyers — 2026-11-04T19:38Z

```
mailboxes taken from the verification log (better than org_mailboxes' single pick): 614
leads with a borrowed mailbox: 2250 | rows upgraded by a newer dated record: 38 | rows upgraded to an active service seen on the buyer's site: 12
P12 organisations: 108 added: 23 {'no own confirmed mailbox': 67, 'same organisation already in a row': 18} | P13 added: 40247 | P13 skipped: {'bad mailbox': 187, 'not located in Canada (no honest inference)': 2483, "mailbox not the organisation's own": 2142, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 7315}
extras from the lanes' result rows: {'invoicing_requirements': 1607, 'invoice_portal_url': 68, 'ap_phone': 1990, 'invoice_mailing_address': 1903, 'ap_contact_name': 133}
org_extras: 51730 organisations read; filled {'vendor_logo': 7980, 'po_required': 146, 'buyer_legal_name': 6993, 'buyer_logo': 32108, 'payment_terms': 163, 'buyer_bn': 1623, 'vendor_legal_name': 1300, 'vendor_neq': 31, 'p13_name_from_legal_name': 1804, 'vendor_bn': 174, 'vendor_qst': 4, 'p13_name_from_domain': 5}
regional mailboxes of multinationals removed from other-country entities: 18
mx_check: 58354 domains known; 214 mailboxes on domains with no mail server removed; 177 webmail (freemail) addresses removed
dmarc/spf: 58350 domains known; rows {'enforced': 14127, 'exposed': 38567}
same organisation under another key folded into the row that holds its mailbox: 52
second mailbox of the same organisation (same site and mail domain, same name family) folded: 5
org_contacts: 45050 organisations read; filled {'vendor_phone': 17972, 'vendor_emails': 2250, 'buyer_phone': 22523, 'buyer_address': 18322, 'vendor_address': 2752}
narrative columns: {'mailbox meta found': 50497, 'mailbox meta missing': 2126}
rows 55589
[('GOLD', 564), ('A0', 512), ('A1', 750), ('A2', 94), ('A3', 202), ('A4', 25), ('B0', 627), ('B1', 900), ('B2', 142), ('B3', 163), ('B4', 11), ('C0', 1014), ('C1', 310), ('C2', 16), ('C3', 33), ('C4', 25), ('D0', 116), ('D1', 3177), ('D2', 115), ('D3', 148), ('D4', 169), ('E0', 99), ('E1', 2581), ('E2', 42), ('E3', 70), ('E4', 57), ('F0', 1), ('F1', 11), ('F2', 2), ('F3', 4), ('F4', 5), ('GOLD-M', 18), ('GOLD-T', 90), ('I0', 348), ('I1', 38711), ('I2', 158), ('I3', 763), ('I4', 267), ('L0', 218), ('L1', 269), ('L2', 30), ('L3', 22), ('L4', 66), ('M0', 10), ('M1', 134), ('M2', 9), ('M3', 27), ('M4', 1), ('T0', 21), ('T1', 2320), ('T2', 48), ('T3', 72), ('T4', 2)]
with any email: 52623 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            564
P01T_active_service_seen_on_buyer_site_invoicing_AP_email     90
P02_active_relationship_finance_accounting_email           338
P03_active_relationship_purchasing_email                   226
P04_active_relationship_general_email                     1570
P05_likely_active_awarded_12_36_months_any_email           375
P06_client_listing_invoicing_AP_email                      160
P06T_active_service_seen_on_buyer_site_other_email        2423
P07_client_listing_finance_or_purchasing_email             245
P08_client_listing_general_email                          3054
P09_older_contract_or_payment_any_email                    364
P10_linked_from_vendor_site_any_email                     2600
P11_any_relationship_email_not_yet_confirmed               504
P12_weaker_relationship_within_5_years_own_email            22
P13_inferred_relationship_no_record_own_email (5 part files)  39899
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email     18
P06M_member_or_regulated_payer_of_canadian_body_other_email    168
Z_no_email_yet_not_delivered                              2969
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 2467147
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
