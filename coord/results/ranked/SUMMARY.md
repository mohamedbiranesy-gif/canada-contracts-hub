# Ranked buyers — 2026-11-04T12:22Z

```
leads with a borrowed mailbox: 2289 | rows upgraded by a newer dated record: 38 | rows upgraded to an active service seen on the buyer's site: 12
P12 organisations: 108 added: 22 {'no own confirmed mailbox': 70, 'same organisation already in a row': 16} | P13 added: 34616 | P13 skipped: {'bad mailbox': 84, 'not located in Canada (no honest inference)': 2459, "mailbox not the organisation's own": 2135, 'same organisation already in a row (domain / mailbox / name)': 7179}
extras from the lanes' result rows: {'invoicing_requirements': 1846, 'invoice_portal_url': 84, 'ap_phone': 2101, 'invoice_mailing_address': 2040, 'ap_contact_name': 113}
org_extras: 51730 organisations read; filled {'vendor_logo': 7974, 'po_required': 194, 'buyer_legal_name': 7870, 'buyer_logo': 32133, 'payment_terms': 146, 'buyer_bn': 1623, 'vendor_legal_name': 1493, 'vendor_neq': 31, 'vendor_bn': 175, 'vendor_qst': 4}
regional mailboxes of multinationals removed from other-country entities: 16
mx_check: 51946 domains known; 187 mailboxes on domains with no mail server removed
org_contacts: 45050 organisations read; filled {'vendor_phone': 17096, 'vendor_emails': 2251, 'buyer_phone': 22584, 'buyer_address': 18345, 'vendor_address': 2752}
rows 49984
[('GOLD', 551), ('A0', 532), ('A1', 802), ('A2', 92), ('A3', 149), ('A4', 27), ('B0', 649), ('B1', 913), ('B2', 151), ('B3', 126), ('B4', 15), ('C0', 1034), ('C1', 320), ('C2', 14), ('C3', 27), ('C4', 23), ('D0', 116), ('D1', 3186), ('D2', 121), ('D3', 130), ('D4', 173), ('E0', 94), ('E1', 2599), ('E2', 43), ('E3', 55), ('E4', 58), ('F1', 13), ('F2', 2), ('F3', 2), ('F4', 5), ('GOLD-M', 17), ('GOLD-T', 88), ('I0', 153), ('I1', 33374), ('I2', 144), ('I3', 679), ('I4', 266), ('L0', 218), ('L1', 274), ('L2', 32), ('L3', 16), ('L4', 64), ('M0', 11), ('M1', 132), ('M2', 8), ('M3', 27), ('M4', 1), ('T0', 19), ('T1', 2326), ('T2', 52), ('T3', 59), ('T4', 2)]
with any email: 47158 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            551
P01T_active_service_seen_on_buyer_site_invoicing_AP_email     88
P02_active_relationship_finance_accounting_email           247
P03_active_relationship_purchasing_email                   222
P04_active_relationship_general_email                     1610
P05_likely_active_awarded_12_36_months_any_email           373
P06_client_listing_invoicing_AP_email                      164
P06T_active_service_seen_on_buyer_site_other_email        2419
P07_client_listing_finance_or_purchasing_email             233
P08_client_listing_general_email                          3061
P09_older_contract_or_payment_any_email                    364
P10_linked_from_vendor_site_any_email                     2601
P11_any_relationship_email_not_yet_confirmed               555
P12_weaker_relationship_within_5_years_own_email            22
P13_inferred_relationship_no_record_own_email            34463
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email     17
P06M_member_or_regulated_payer_of_canadian_body_other_email    165
Z_no_email_yet_not_delivered                              2829
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 1708565
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
