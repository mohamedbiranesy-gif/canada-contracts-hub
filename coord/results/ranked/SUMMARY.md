# Ranked buyers — 2026-11-08T06:58Z

```
# Changelog — build 2026-11-08T06:54Z (5ffa635)

Build id = the commit that produced this folder; every build is a full regeneration from the same rules, so the delta below is the only thing downstream needs to apply.

- rows: 62780 → 66630
- Gold (P01): 565 → 581
- mailbox changed: 32
- package moved: 27
- row added: 3862
- row removed: 12

Row-level list: `rows_changed.csv` (change, buyer, rank_group, email, detail).
mailboxes taken from the verification log (better than org_mailboxes' single pick): 627
team vendor contacts (referee-verified): 8716 vendors; 172 with a billing / AR mailbox
leads with a borrowed mailbox: 2241 | rows upgraded by a newer dated record: 38 | rows upgraded to an active service seen on the buyer's site: 12
P12 organisations: 107 added: 22 {'no own confirmed mailbox': 68, 'same organisation already in a row': 17} | P13 added: 51234 | P13 skipped: {'bad mailbox': 185, 'not located in Canada (no honest inference)': 2497, "mailbox not the organisation's own": 2130, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 7643}
extras from the lanes' result rows: {'invoicing_requirements': 1626, 'invoice_portal_url': 68, 'ap_phone': 2011, 'invoice_mailing_address': 1901, 'ap_contact_name': 138}
org_extras: 78199 organisations read; filled {'vendor_logo': 8032, 'po_required': 153, 'buyer_legal_name': 9449, 'buyer_logo': 48071, 'payment_terms': 178, 'buyer_bn': 1898, 'vendor_legal_name': 1305, 'vendor_neq': 31, 'p13_name_from_legal_name': 3915, 'vendor_bn': 174, 'vendor_qst': 4, 'p13_name_from_domain': 4}
regional mailboxes of multinationals removed from other-country entities: 20
mx_check: 69559 domains known; 263 mailboxes on domains with no mail server removed; 226 webmail (freemail) addresses removed
dmarc/spf: 69555 domains known; rows {'enforced': 16187, 'exposed': 47896}
same organisation under another key folded into the row that holds its mailbox: 54
second mailbox of the same organisation (same site and mail domain, same name family) folded: 5
org_contacts: 70273 organisations read; filled {'vendor_phone': 19544, 'vendor_emails': 2256, 'buyer_phone': 33463, 'buyer_address': 30374, 'vendor_address': 2770}
ap_terms (evidence pages re-read): 56985 mailboxes read; filled {'format': 261, 'context': 46046, 'payment_method': 354, 'ap_phone': 828, 'po_required': 336, 'payment_terms': 209, 'tax_exempt': 161, 'portal': 609, 'mailbox_gone': 255, 'address': 437, 'ap_contact_name': 39, 'buyer_bn': 12, 'ap_cycle': 19, 'esignature': 51, 'buyer_phone_from_page': 13692, 'buyer_address_from_page': 2356}
peppol: 77 Canadian participants; matched buyers 2, vendors 36
municipal directory: {'matched': 1398, 'legal_name': 1247, 'phone': 318, 'website': 5, 'address': 21}
back-references: {'dataset rows with lead relationships': 9666, 'lead rows with dataset history': 9}
sensitivity tags: {'corrections / detention': 23, 'health: mental health / addiction / sexual health': 161, 'intelligence / security / defence': 13, 'police service / police board': 55, 'courts / tribunals / legal aid': 41, 'child / youth protection': 14, 'police oversight body': 3, 'shelter / crisis / sexual-assault service': 50, 'coroner / medical examiner': 1}
narrative columns: {'mailbox meta found': 61439, 'mailbox meta missing': 2144}
downstream pack: {'ship_ready_yes': 653, 'buyer_type_from_name': 5031, 'sensitivity_extra': 105, 'registry_warning': 362, 'currency_default': 2}
rows 66649
[('GOLD', 581), ('A0', 515), ('A1', 741), ('A2', 92), ('A3', 208), ('A4', 10), ('B0', 622), ('B1', 955), ('B2', 145), ('B3', 166), ('B4', 11), ('C0', 1012), ('C1', 316), ('C2', 15), ('C3', 33), ('C4', 25), ('D0', 117), ('D1', 3178), ('D2', 115), ('D3', 148), ('D4', 169), ('E0', 98), ('E1', 2584), ('E2', 42), ('E3', 72), ('E4', 57), ('F0', 1), ('F1', 11), ('F2', 2), ('F3', 3), ('F4', 5), ('GOLD-M', 19), ('GOLD-T', 91), ('I0', 448), ('I1', 49371), ('I2', 174), ('I3', 930), ('I4', 311), ('L0', 222), ('L1', 273), ('L2', 30), ('L3', 23), ('L4', 67), ('M0', 10), ('M1', 134), ('M2', 9), ('M3', 27), ('M4', 1), ('T0', 21), ('T1', 2318), ('T2', 48), ('T3', 72), ('T4', 1)]
with any email: 63583 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            581
P01T_active_service_seen_on_buyer_site_invoicing_AP_email     91
P02_active_relationship_finance_accounting_email           369
P03_active_relationship_purchasing_email                   225
P04_active_relationship_general_email                     1614
P05_likely_active_awarded_12_36_months_any_email           379
P06_client_listing_invoicing_AP_email                      160
P06T_active_service_seen_on_buyer_site_other_email        2429
P07_client_listing_finance_or_purchasing_email             246
P08_client_listing_general_email                          3038
P09_older_contract_or_payment_any_email                    368
P10_linked_from_vendor_site_any_email                     2587
P11_any_relationship_email_not_yet_confirmed               499
P12_weaker_relationship_within_5_years_own_email            21
P13_inferred_relationship_no_record_own_email (10 part files)  50786
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email     19
P06M_member_or_regulated_payer_of_canadian_body_other_email    168
Z_no_email_yet_not_delivered                              3069
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 5210850
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
