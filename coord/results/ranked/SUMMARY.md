# Ranked buyers — 2026-11-04T11:06Z

```
leads with a borrowed mailbox: 2372 | rows upgraded by a newer dated record: 39 | rows upgraded to an active service seen on the buyer's site: 12
P12 organisations: 108 added: 23 {'no own confirmed mailbox': 64, 'same organisation already in a row': 21} | P13 added: 33252 | P13 skipped: {'bad mailbox': 84, 'not located in Canada (no honest inference)': 2408, "mailbox not the organisation's own": 2131, 'same organisation already in a row (domain / mailbox / name)': 7110}
extras from the lanes' result rows: {'invoicing_requirements': 1845, 'invoice_portal_url': 84, 'ap_phone': 2100, 'invoice_mailing_address': 2038, 'ap_contact_name': 112}
org_extras: 51730 organisations read; filled {'vendor_logo': 7940, 'po_required': 193, 'buyer_legal_name': 7860, 'buyer_logo': 32081, 'payment_terms': 142, 'buyer_bn': 1622, 'vendor_legal_name': 1462, 'vendor_neq': 31, 'vendor_bn': 174, 'vendor_qst': 4}
regional mailboxes of multinationals removed from other-country entities: 16
mx_check: 51103 domains known; 183 mailboxes on domains with no mail server removed
org_contacts: 45050 organisations read; filled {'vendor_phone': 16872, 'vendor_emails': 2249, 'buyer_phone': 22545, 'buyer_address': 18313, 'vendor_address': 2720}
rows 48548
[('GOLD', 568), ('A0', 532), ('A1', 803), ('A2', 92), ('A3', 146), ('A4', 14), ('B0', 649), ('B1', 913), ('B2', 151), ('B3', 127), ('B4', 10), ('C0', 1034), ('C1', 320), ('C2', 14), ('C3', 27), ('C4', 23), ('D0', 114), ('D1', 3133), ('D2', 118), ('D3', 127), ('D4', 162), ('E0', 94), ('E1', 2600), ('E2', 43), ('E3', 55), ('E4', 58), ('F1', 14), ('F2', 2), ('F3', 2), ('F4', 5), ('GOLD-M', 17), ('GOLD-T', 88), ('I0', 149), ('I1', 32044), ('I2', 142), ('I3', 655), ('I4', 262), ('L0', 219), ('L1', 273), ('L2', 32), ('L3', 17), ('L4', 63), ('M0', 11), ('M1', 132), ('M2', 8), ('M3', 27), ('M4', 1), ('T0', 19), ('T1', 2326), ('T2', 52), ('T3', 59), ('T4', 2)]
with any email: 45727 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            568
P01T_active_service_seen_on_buyer_site_invoicing_AP_email     88
P02_active_relationship_finance_accounting_email           258
P03_active_relationship_purchasing_email                   234
P04_active_relationship_general_email                     1644
P05_likely_active_awarded_12_36_months_any_email           373
P06_client_listing_invoicing_AP_email                      153
P06T_active_service_seen_on_buyer_site_other_email        2419
P07_client_listing_finance_or_purchasing_email             227
P08_client_listing_general_email                          3010
P09_older_contract_or_payment_any_email                    364
P10_linked_from_vendor_site_any_email                     2602
P11_any_relationship_email_not_yet_confirmed               476
P12_weaker_relationship_within_5_years_own_email            23
P13_inferred_relationship_no_record_own_email            33103
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email     17
P06M_member_or_regulated_payer_of_canadian_body_other_email    165
Z_no_email_yet_not_delivered                              2824
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 1649113
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
