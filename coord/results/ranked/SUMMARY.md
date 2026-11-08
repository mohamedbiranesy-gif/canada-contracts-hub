# Ranked buyers — 2026-11-08T15:29Z

```
# Changelog — build 2026-11-08T15:25Z (f93272c)

Build id = the commit that produced this folder; every build is a full regeneration from the same rules, so the delta below is the only thing downstream needs to apply.

- rows: 66630 → 66630
- Gold (P01): 585 → 585
- field changed: buyer_address: 1056
- field changed: buyer_bn_as_published: 6284
- field changed: buyer_legal_name_as_published: 7600
- field changed: buyer_phone: 756
- field changed: buyer_website: 57
- field changed: invoice_portal_url: 2
mailboxes taken from the verification log (better than org_mailboxes' single pick): 626
team vendor contacts (referee-verified): 8716 vendors; 172 with a billing / AR mailbox
same-pair fill (facts from another record of the same buyer-vendor pair): {'solicitation_or_tender_number': 11, 'award_or_notice_id': 3, 'buyer_vendor_id': 2, 'commodity_codes': 8, 'end_date_inferred': 121, 'contract_value': 7, 'procurement_method': 3, 'contract_description': 3, 'number_of_bids': 1, 'po_number_as_published': 3, 'buyer_org_codes': 1, 'start_from_signed': 500, 'contract_or_agreement_number': 15, 'end_date': 1, 'contract_title': 1}
leads with a borrowed mailbox: 2246 | rows upgraded by a newer dated record: 38 | rows upgraded to an active service seen on the buyer's site: 12
P12 organisations: 107 added: 22 {'no own confirmed mailbox': 68, 'same organisation already in a row': 17} | P13 added: 51234 | P13 skipped: {'bad mailbox': 185, 'not located in Canada (no honest inference)': 2498, "mailbox not the organisation's own": 2130, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 7643}
extras from the lanes' result rows: {'invoicing_requirements': 1626, 'invoice_portal_url': 68, 'ap_phone': 2012, 'invoice_mailing_address': 1901, 'ap_contact_name': 139}
org_extras: 78457 organisations read; filled {'vendor_logo': 8163, 'vendor_phone_v2': 1069, 'po_required': 154, 'buyer_legal_name': 10873, 'buyer_phone_v2': 1414, 'buyer_payment_method_preference_mention': 1147, 'buyer_logo': 48380, 'buyer_tax_exempt_status_mention': 38, 'payment_terms': 178, 'buyer_legal_name_v2_legal_name_stated': 1143, 'buyer_bn': 1900, 'buyer_legal_name_v2_jsonld_legal_name': 33, 'ap_system_hint_links': 135, 'buyer_legal_name_v2_jsonld_name': 21, 'vendor_legal_name': 1372, 'vendor_legal_name_v2': 203, 'vendor_neq': 31, 'buyer_esignature_preference_mention': 11, 'buyer_address_v2': 69, 'p13_name_from_legal_name': 3986, 'vendor_bn': 179, 'invoice_portal_links': 1, 'vendor_address_v2': 21, 'buyer_bn_jsonld': 1, 'vendor_qst': 4, 'p13_name_from_domain': 4}
regional mailboxes of multinationals removed from other-country entities: 20
mx_check: 69559 domains known; 263 mailboxes on domains with no mail server removed; 226 webmail (freemail) addresses removed
dmarc/spf: 69555 domains known; rows {'enforced': 16187, 'exposed': 47896}
same organisation under another key folded into the row that holds its mailbox: 54
second mailbox of the same organisation (same site and mail domain, same name family) folded: 5
org_contacts: 71137 organisations read; filled {'vendor_phone': 19698, 'vendor_emails': 2324, 'buyer_phone': 34078, 'buyer_address': 30861, 'vendor_address': 2837}
ap_terms (evidence pages re-read): 57047 mailboxes read; filled {'format': 261, 'context': 46042, 'payment_method': 354, 'ap_phone': 825, 'po_required': 335, 'payment_terms': 209, 'tax_exempt': 161, 'portal': 607, 'mailbox_gone': 257, 'address': 436, 'ap_contact_name': 39, 'buyer_bn': 12, 'ap_cycle': 19, 'esignature': 51, 'buyer_phone_from_page': 13413, 'buyer_address_from_page': 2295}
peppol: 77 Canadian participants; matched buyers 2, vendors 36
municipal / organisation directories: {'matched': 1715, 'legal_name': 923, 'address': 49, 'phone': 332, 'website': 18}
charity buyers: {'matched': 7454, 'bn': 6270, 'legal_name': 5792, 'address': 339, 'website': 25}
wikidata: {'buyers': 857, 'buyer_legal_name': 224, 'vendors': 64, 'buyer_phone': 26, 'buyer_address': 60, 'buyer_website': 19, 'vendor_legal_name': 6, 'vendor_address': 15, 'vendor_website': 31}
crown-corporation BNs applied to inferred-vendor rows: 46996
inferred vendors' published phone / address applied: {'phone': 37244}
Canada's Business Registries: 0 vendors, 0 buyers found; filled {}
grants & contributions recipient BNs: 0 buyers, 0 vendors in file; filled {}
buyers' PO / contract open data joined: {'pairs': 8, 'po_filled': 6, 'contract_filled': 1} | records: 555539
back-references: {'dataset rows with lead relationships': 9675, 'lead rows with dataset history': 16}
sensitivity tags: {'corrections / detention': 25, 'health: mental health / addiction / sexual health': 169, 'intelligence / security / defence': 13, 'police service / police board': 58, 'courts / tribunals / legal aid': 41, 'child / youth protection': 14, 'police oversight body': 3, 'shelter / crisis / sexual-assault service': 51, 'coroner / medical examiner': 1}
narrative columns: {'mailbox meta found': 61438, 'records_with_this_vendor_lead': 10666, 'mailbox meta missing': 2144}
downstream pack: {'ship_ready_yes': 628, 'registry_warning': 727, 'buyer_type_from_name': 5253, 'sensitivity_extra': 107, 'currency_default': 2}
rows 66649
[('GOLD', 585), ('A0', 515), ('A1', 742), ('A2', 92), ('A3', 208), ('A4', 9), ('B0', 622), ('B1', 955), ('B2', 144), ('B3', 164), ('B4', 10), ('C0', 1012), ('C1', 316), ('C2', 15), ('C3', 33), ('C4', 25), ('D0', 117), ('D1', 3178), ('D2', 115), ('D3', 148), ('D4', 169), ('E0', 98), ('E1', 2584), ('E2', 42), ('E3', 72), ('E4', 57), ('F0', 1), ('F1', 11), ('F2', 2), ('F3', 3), ('F4', 5), ('GOLD-M', 20), ('GOLD-T', 91), ('I0', 448), ('I1', 49371), ('I2', 174), ('I3', 930), ('I4', 311), ('L0', 223), ('L1', 273), ('L2', 30), ('L3', 23), ('L4', 66), ('M0', 10), ('M1', 134), ('M2', 9), ('M3', 26), ('M4', 1), ('T0', 21), ('T1', 2318), ('T2', 48), ('T3', 72), ('T4', 1)]
with any email: 63582 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            585
P01T_active_service_seen_on_buyer_site_invoicing_AP_email     91
P02_active_relationship_finance_accounting_email           367
P03_active_relationship_purchasing_email                   224
P04_active_relationship_general_email                     1615
P05_likely_active_awarded_12_36_months_any_email           378
P06_client_listing_invoicing_AP_email                      160
P06T_active_service_seen_on_buyer_site_other_email        2429
P07_client_listing_finance_or_purchasing_email             246
P08_client_listing_general_email                          3038
P09_older_contract_or_payment_any_email                    368
P10_linked_from_vendor_site_any_email                     2587
P11_any_relationship_email_not_yet_confirmed               497
P12_weaker_relationship_within_5_years_own_email            21
P13_inferred_relationship_no_record_own_email (12 part files)  50786
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email     20
P06M_member_or_regulated_payer_of_canadian_body_other_email    167
Z_no_email_yet_not_delivered                              3070
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 6546417

# coverage vs the downstream targets (COVERAGE_VS_TARGETS.md)
benchmarks met 76 / 438 (17.4%); near 35; written out/ranked/COVERAGE_VS_TARGETS.md
  gap buyer_legal_name_as_published      P13       24.0% ->  60%  rows needed 18264
  gap buyer_address                      P13       71.8% ->  95%  rows needed 11764
  gap buyer_logo_url                     P13       73.4% ->  95%  rows needed 10972
  gap buyer_phone                        P13       74.7% ->  95%  rows needed 10330
  gap buyer_ap_cycle_published           P13        0.0% ->  20%  rows needed 10157
  gap ap_system_hint                     P13        0.3% ->  20%  rows needed 10000
  gap buyer_bn_as_published              P13       14.3% ->  30%  rows needed 7955
  gap buyer_esignature_preference        P13        0.1% ->  15%  rows needed 7591
  gap buyer_tax_exempt_status            P13        0.1% ->  15%  rows needed 7567
  gap buyer_payment_method_preference    P13        0.6% ->  15%  rows needed 7336
  gap buyer_legal_name_as_published      P08       20.9% ->  75%  rows needed 1645
  gap buyer_legal_name_as_published      P10       15.3% ->  70%  rows needed 1416
  gap vendor_registered_address          P10       16.0% ->  70%  rows needed 1398
  gap vendor_registered_address          P08       24.9% ->  70%  rows needed 1370
  gap vendor_bn9                         P08       14.1% ->  50%  rows needed 1092
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
