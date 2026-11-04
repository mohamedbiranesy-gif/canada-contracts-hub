# Ranked buyers — 2026-11-04T14:42Z

```
mailboxes taken from the verification log (better than org_mailboxes' single pick): 609
leads with a borrowed mailbox: 2259 | rows upgraded by a newer dated record: 38 | rows upgraded to an active service seen on the buyer's site: 12
P12 organisations: 108 added: 23 {'no own confirmed mailbox': 66, 'same organisation already in a row': 19} | P13 added: 36604 | P13 skipped: {'bad mailbox': 71, 'not located in Canada (no honest inference)': 2483, "mailbox not the organisation's own": 2155, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 7285}
extras from the lanes' result rows: {'invoicing_requirements': 1869, 'invoice_portal_url': 83, 'ap_phone': 2087, 'invoice_mailing_address': 2023, 'ap_contact_name': 124}
org_extras: 51730 organisations read; filled {'vendor_logo': 7990, 'po_required': 193, 'buyer_legal_name': 7498, 'buyer_logo': 32161, 'payment_terms': 152, 'buyer_bn': 1623, 'vendor_legal_name': 1417, 'vendor_neq': 31, 'vendor_bn': 175, 'vendor_qst': 4, 'p13_name_from_domain': 5, 'p13_name_from_legal_name': 794}
regional mailboxes of multinationals removed from other-country entities: 18
mx_check: 54323 domains known; 197 mailboxes on domains with no mail server removed
org_contacts: 45050 organisations read; filled {'vendor_phone': 17476, 'vendor_emails': 2259, 'buyer_phone': 22606, 'buyer_address': 18370, 'vendor_address': 2761}
rows 52009
[('GOLD', 564), ('A0', 498), ('A1', 780), ('A2', 96), ('A3', 198), ('A4', 26), ('B0', 633), ('B1', 900), ('B2', 144), ('B3', 160), ('B4', 13), ('C0', 1027), ('C1', 318), ('C2', 15), ('C3', 33), ('C4', 25), ('D0', 115), ('D1', 3185), ('D2', 115), ('D3', 145), ('D4', 173), ('E0', 99), ('E1', 2590), ('E2', 42), ('E3', 66), ('E4', 61), ('F1', 12), ('F2', 2), ('F3', 4), ('F4', 5), ('GOLD-M', 18), ('GOLD-T', 89), ('I0', 164), ('I1', 35305), ('I2', 148), ('I3', 710), ('I4', 277), ('L0', 217), ('L1', 273), ('L2', 31), ('L3', 22), ('L4', 66), ('M0', 11), ('M1', 133), ('M2', 9), ('M3', 27), ('M4', 1), ('T0', 19), ('T1', 2323), ('T2', 48), ('T3', 72), ('T4', 2)]
with any email: 49226 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            564
P01T_active_service_seen_on_buyer_site_invoicing_AP_email     89
P02_active_relationship_finance_accounting_email           332
P03_active_relationship_purchasing_email                   229
P04_active_relationship_general_email                     1597
P05_likely_active_awarded_12_36_months_any_email           380
P06_client_listing_invoicing_AP_email                      164
P06T_active_service_seen_on_buyer_site_other_email        2425
P07_client_listing_finance_or_purchasing_email             242
P08_client_listing_general_email                          3060
P09_older_contract_or_payment_any_email                    371
P10_linked_from_vendor_site_any_email                     2605
P11_any_relationship_email_not_yet_confirmed               517
P12_weaker_relationship_within_5_years_own_email            23
P13_inferred_relationship_no_record_own_email            36440
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email     18
P06M_member_or_regulated_payer_of_canadian_body_other_email    167
Z_no_email_yet_not_delivered                              2786
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 1793921
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
