# Ranked buyers — 2026-11-04T16:43Z

```
mailboxes taken from the verification log (better than org_mailboxes' single pick): 611
leads with a borrowed mailbox: 2264 | rows upgraded by a newer dated record: 38 | rows upgraded to an active service seen on the buyer's site: 12
P12 organisations: 108 added: 23 {'no own confirmed mailbox': 66, 'same organisation already in a row': 19} | P13 added: 37568 | P13 skipped: {'bad mailbox': 71, 'not located in Canada (no honest inference)': 2483, "mailbox not the organisation's own": 2155, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 7314}
extras from the lanes' result rows: {'invoicing_requirements': 1870, 'invoice_portal_url': 83, 'ap_phone': 2088, 'invoice_mailing_address': 2024, 'ap_contact_name': 126}
org_extras: 51730 organisations read; filled {'vendor_logo': 7992, 'po_required': 193, 'buyer_legal_name': 7498, 'buyer_logo': 32161, 'payment_terms': 156, 'buyer_bn': 1623, 'vendor_legal_name': 1417, 'vendor_neq': 31, 'vendor_bn': 175, 'vendor_qst': 4, 'p13_name_from_domain': 5, 'p13_name_from_legal_name': 795}
regional mailboxes of multinationals removed from other-country entities: 19
mx_check: 55015 domains known; 198 mailboxes on domains with no mail server removed; 169 webmail (freemail) addresses removed
dmarc/spf: 48937 domains known; rows {'enforced': 13757, 'exposed': 36155}
org_contacts: 45050 organisations read; filled {'vendor_phone': 17638, 'vendor_emails': 2259, 'buyer_phone': 22606, 'buyer_address': 18371, 'vendor_address': 2761}
narrative columns: {'mailbox meta found': 47885, 'mailbox meta missing': 2142}
rows 52979
[('GOLD', 565), ('A0', 499), ('A1', 780), ('A2', 96), ('A3', 197), ('A4', 26), ('B0', 631), ('B1', 904), ('B2', 145), ('B3', 161), ('B4', 13), ('C0', 1030), ('C1', 315), ('C2', 15), ('C3', 33), ('C4', 25), ('D0', 118), ('D1', 3183), ('D2', 115), ('D3', 144), ('D4', 173), ('E0', 100), ('E1', 2590), ('E2', 42), ('E3', 66), ('E4', 61), ('F0', 1), ('F1', 11), ('F2', 2), ('F3', 4), ('F4', 5), ('GOLD-M', 18), ('GOLD-T', 89), ('I0', 324), ('I1', 36112), ('I2', 148), ('I3', 708), ('I4', 276), ('L0', 217), ('L1', 273), ('L2', 31), ('L3', 22), ('L4', 66), ('M0', 11), ('M1', 133), ('M2', 9), ('M3', 27), ('M4', 1), ('T0', 21), ('T1', 2322), ('T2', 48), ('T3', 71), ('T4', 2)]
with any email: 50027 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            565
P01T_active_service_seen_on_buyer_site_invoicing_AP_email     89
P02_active_relationship_finance_accounting_email           332
P03_active_relationship_purchasing_email                   230
P04_active_relationship_general_email                     1601
P05_likely_active_awarded_12_36_months_any_email           380
P06_client_listing_invoicing_AP_email                      164
P06T_active_service_seen_on_buyer_site_other_email        2423
P07_client_listing_finance_or_purchasing_email             241
P08_client_listing_general_email                          3058
P09_older_contract_or_payment_any_email                    368
P10_linked_from_vendor_site_any_email                     2606
P11_any_relationship_email_not_yet_confirmed               516
P12_weaker_relationship_within_5_years_own_email            22
P13_inferred_relationship_no_record_own_email (4 part files)  37244
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email     18
P06M_member_or_regulated_payer_of_canadian_body_other_email    167
Z_no_email_yet_not_delivered                              2955
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 2330671
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
