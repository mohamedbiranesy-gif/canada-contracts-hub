# Ranked buyers — 2026-11-07T19:35Z

```
# Changelog — build 2026-11-07T19:32Z (f4383e7)

Build id = the commit that produced this folder; every build is a full regeneration from the same rules, so the delta below is the only thing downstream needs to apply.

- rows: 62780 → 62779
- Gold (P01): 561 → 563
- mailbox changed: 6
- package moved: 8
- row removed: 1

Row-level list: `rows_changed.csv` (change, buyer, rank_group, email, detail).
mailboxes taken from the verification log (better than org_mailboxes' single pick): 611
team vendor contacts (referee-verified): 8716 vendors; 171 with a billing / AR mailbox
leads with a borrowed mailbox: 2253 | rows upgraded by a newer dated record: 38 | rows upgraded to an active service seen on the buyer's site: 12
P12 organisations: 107 added: 22 {'no own confirmed mailbox': 68, 'same organisation already in a row': 17} | P13 added: 47379 | P13 skipped: {'bad mailbox': 181, 'not located in Canada (no honest inference)': 2481, "mailbox not the organisation's own": 2100, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 7513}
extras from the lanes' result rows: {'invoicing_requirements': 1622, 'invoice_portal_url': 67, 'ap_phone': 2008, 'invoice_mailing_address': 1898, 'ap_contact_name': 137}
org_extras: 78199 organisations read; filled {'vendor_logo': 8034, 'po_required': 150, 'buyer_legal_name': 9144, 'buyer_logo': 45216, 'payment_terms': 155, 'buyer_bn': 1853, 'vendor_neq': 31, 'vendor_legal_name': 1305, 'p13_name_from_legal_name': 3651, 'vendor_bn': 174, 'vendor_qst': 4, 'p13_name_from_domain': 4}
regional mailboxes of multinationals removed from other-country entities: 20
mx_check: 69534 domains known; 245 mailboxes on domains with no mail server removed; 212 webmail (freemail) addresses removed
dmarc/spf: 69530 domains known; rows {'enforced': 15601, 'exposed': 44632}
same organisation under another key folded into the row that holds its mailbox: 52
second mailbox of the same organisation (same site and mail domain, same name family) folded: 5
org_contacts: 70273 organisations read; filled {'vendor_phone': 19086, 'vendor_emails': 2258, 'buyer_phone': 31848, 'buyer_address': 28448, 'vendor_address': 2771}
ap_terms (evidence pages re-read): 56948 mailboxes read; filled {'format': 258, 'context': 44128, 'payment_method': 336, 'ap_phone': 32736, 'po_required': 321, 'payment_terms': 191, 'tax_exempt': 159, 'portal': 588, 'mailbox_gone': 196, 'address': 12247, 'ap_contact_name': 39, 'buyer_bn': 12, 'ap_cycle': 19, 'esignature': 47}
peppol: 77 Canadian participants; matched buyers 2, vendors 36
back-references: {'dataset rows with lead relationships': 9670, 'lead rows with dataset history': 9}
sensitivity tags: {'corrections / detention': 22, 'health: mental health / addiction / sexual health': 157, 'intelligence / security / defence': 13, 'police service / police board': 55, 'courts / tribunals / legal aid': 41, 'child / youth protection': 14, 'police oversight body': 3, 'shelter / crisis / sexual-assault service': 50, 'coroner / medical examiner': 1}
narrative columns: {'mailbox meta found': 57613, 'mailbox meta missing': 2145}
downstream pack: {'ship_ready_yes': 634, 'buyer_type_from_name': 4862, 'sensitivity_extra': 105, 'registry_warning': 362, 'currency_default': 2}
rows 62798
[('GOLD', 563), ('A0', 516), ('A1', 742), ('A2', 92), ('A3', 208), ('A4', 16), ('B0', 623), ('B1', 956), ('B2', 151), ('B3', 167), ('B4', 15), ('C0', 1013), ('C1', 314), ('C2', 15), ('C3', 33), ('C4', 25), ('D0', 118), ('D1', 3180), ('D2', 114), ('D3', 147), ('D4', 170), ('E0', 99), ('E1', 2584), ('E2', 42), ('E3', 72), ('E4', 57), ('F0', 1), ('F1', 11), ('F2', 2), ('F3', 3), ('F4', 5), ('GOLD-M', 18), ('GOLD-T', 91), ('I0', 416), ('I1', 45592), ('I2', 164), ('I3', 907), ('I4', 300), ('L0', 222), ('L1', 274), ('L2', 29), ('L3', 23), ('L4', 66), ('M0', 10), ('M1', 135), ('M2', 9), ('M3', 27), ('M4', 1), ('T0', 22), ('T1', 2317), ('T2', 47), ('T3', 73), ('T4', 1)]
with any email: 59758 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            563
P01T_active_service_seen_on_buyer_site_invoicing_AP_email     91
P02_active_relationship_finance_accounting_email           355
P03_active_relationship_purchasing_email                   224
P04_active_relationship_general_email                     1578
P05_likely_active_awarded_12_36_months_any_email           368
P06_client_listing_invoicing_AP_email                      154
P06T_active_service_seen_on_buyer_site_other_email        2366
P07_client_listing_finance_or_purchasing_email             236
P08_client_listing_general_email                          2992
P09_older_contract_or_payment_any_email                    355
P10_linked_from_vendor_site_any_email                     2538
P11_any_relationship_email_not_yet_confirmed               764
P12_weaker_relationship_within_5_years_own_email            19
P13_inferred_relationship_no_record_own_email (9 part files)  46932
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email     18
P06M_member_or_regulated_payer_of_canadian_body_other_email    164
Z_no_email_yet_not_delivered                              3081
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 4613463
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
