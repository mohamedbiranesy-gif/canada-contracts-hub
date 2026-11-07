# Ranked buyers — 2026-11-07T06:14Z

```
# Changelog — build 2026-11-07T06:10Z (9cc0940)

Build id = the commit that produced this folder; every build is a full regeneration from the same rules, so the delta below is the only thing downstream needs to apply.

- rows: 66357 → 66372
- Gold (P01): 580 → 581
- mailbox changed: 3
- package moved: 3
- row added: 16
- row removed: 1

Row-level list: `rows_changed.csv` (change, buyer, rank_group, email, detail).
mailboxes taken from the verification log (better than org_mailboxes' single pick): 630
team vendor contacts (referee-verified): 8719 vendors; 171 with a billing / AR mailbox
leads with a borrowed mailbox: 2258 | rows upgraded by a newer dated record: 38 | rows upgraded to an active service seen on the buyer's site: 12
P12 organisations: 107 added: 23 {'no own confirmed mailbox': 66, 'same organisation already in a row': 18} | P13 added: 50975 | P13 skipped: {'bad mailbox': 187, 'not located in Canada (no honest inference)': 2492, "mailbox not the organisation's own": 2146, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 7640}
extras from the lanes' result rows: {'invoicing_requirements': 1627, 'invoice_portal_url': 68, 'ap_phone': 2012, 'invoice_mailing_address': 1902, 'ap_contact_name': 138}
org_extras: 52137 organisations read; filled {'vendor_logo': 8000, 'po_required': 154, 'buyer_legal_name': 7080, 'buyer_logo': 32497, 'payment_terms': 178, 'buyer_bn': 1637, 'vendor_legal_name': 1299, 'vendor_neq': 31, 'p13_name_from_legal_name': 1871, 'vendor_bn': 174, 'vendor_qst': 4, 'p13_name_from_domain': 5}
regional mailboxes of multinationals removed from other-country entities: 20
mx_check: 69534 domains known; 260 mailboxes on domains with no mail server removed; 224 webmail (freemail) addresses removed
dmarc/spf: 69530 domains known; rows {'enforced': 16162, 'exposed': 47656}
same organisation under another key folded into the row that holds its mailbox: 54
second mailbox of the same organisation (same site and mail domain, same name family) folded: 5
org_contacts: 61923 organisations read; filled {'vendor_phone': 19466, 'vendor_emails': 2256, 'buyer_phone': 33498, 'buyer_address': 30406, 'vendor_address': 2769}
ap_terms (evidence pages re-read): 21984 mailboxes read; filled {'format': 194, 'context': 16102, 'payment_method': 129, 'ap_phone': 13042, 'po_required': 315, 'payment_terms': 175, 'tax_exempt': 89, 'portal': 500, 'mailbox_gone': 198, 'address': 3527, 'ap_contact_name': 40, 'buyer_bn': 10, 'ap_cycle': 15, 'esignature': 28}
peppol: 77 Canadian participants; matched buyers 2, vendors 36
back-references: {'dataset rows with lead relationships': 9660, 'lead rows with dataset history': 8}
sensitivity tags: {'corrections / detention': 23, 'health: mental health / addiction / sexual health': 154, 'intelligence / security / defence': 13, 'police service / police board': 52, 'courts / tribunals / legal aid': 40, 'child / youth protection': 14, 'police oversight body': 3, 'shelter / crisis / sexual-assault service': 49, 'coroner / medical examiner': 1}
narrative columns: {'mailbox meta found': 61180, 'mailbox meta missing': 2149}
downstream pack: {'ship_ready_yes': 651, 'buyer_type_from_name': 4995, 'sensitivity_extra': 101, 'registry_warning': 362, 'currency_default': 2}
rows 66391
[('GOLD', 581), ('A0', 514), ('A1', 743), ('A2', 92), ('A3', 207), ('A4', 9), ('B0', 623), ('B1', 955), ('B2', 145), ('B3', 167), ('B4', 11), ('C0', 1012), ('C1', 315), ('C2', 15), ('C3', 33), ('C4', 25), ('D0', 117), ('D1', 3178), ('D2', 115), ('D3', 148), ('D4', 169), ('E0', 99), ('E1', 2583), ('E2', 42), ('E3', 72), ('E4', 57), ('F0', 1), ('F1', 11), ('F2', 2), ('F3', 4), ('F4', 5), ('GOLD-M', 18), ('GOLD-T', 91), ('I0', 443), ('I1', 49122), ('I2', 174), ('I3', 927), ('I4', 309), ('L0', 222), ('L1', 273), ('L2', 30), ('L3', 23), ('L4', 67), ('M0', 10), ('M1', 136), ('M2', 9), ('M3', 27), ('M4', 1), ('T0', 21), ('T1', 2317), ('T2', 48), ('T3', 72), ('T4', 1)]
with any email: 63329 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            581
P01T_active_service_seen_on_buyer_site_invoicing_AP_email     91
P02_active_relationship_finance_accounting_email           356
P03_active_relationship_purchasing_email                   221
P04_active_relationship_general_email                     1602
P05_likely_active_awarded_12_36_months_any_email           379
P06_client_listing_invoicing_AP_email                      159
P06T_active_service_seen_on_buyer_site_other_email        2419
P07_client_listing_finance_or_purchasing_email             246
P08_client_listing_general_email                          3038
P09_older_contract_or_payment_any_email                    358
P10_linked_from_vendor_site_any_email                     2594
P11_any_relationship_email_not_yet_confirmed               540
P12_weaker_relationship_within_5_years_own_email            19
P13_inferred_relationship_no_record_own_email (10 part files)  50504
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email     18
P06M_member_or_regulated_payer_of_canadian_body_other_email    170
Z_no_email_yet_not_delivered                              3096
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 4983267
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
