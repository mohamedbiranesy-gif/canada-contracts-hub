# Ranked buyers — 2026-11-08T17:32Z

```
# Changelog — build 2026-11-08T17:27Z (43d9bda)

Build id = the commit that produced this folder; every build is a full regeneration from the same rules, so the delta below is the only thing downstream needs to apply.

- rows: 66641 → 66641
- Gold (P01): 583 → 583
- field changed: ap_contact_name_as_published: 4
- field changed: ap_phone: 1
- field changed: buyer_address: 1283
- field changed: buyer_bn_as_published: 847
- field changed: buyer_legal_name_as_published: 2415
- field changed: buyer_phone: 784
mailboxes taken from the verification log (better than org_mailboxes' single pick): 630
team vendor contacts (referee-verified): 8716 vendors; 172 with a billing / AR mailbox
same-pair fill (facts from another record of the same buyer-vendor pair): {'solicitation_or_tender_number': 11, 'number_of_bids': 10, 'award_or_notice_id': 3, 'buyer_vendor_id': 2, 'commodity_codes': 8, 'end_date_inferred': 123, 'contract_value': 7, 'procurement_method': 3, 'contract_description': 3, 'po_number_as_published': 3, 'buyer_org_codes': 1, 'start_from_signed': 496, 'contract_or_agreement_number': 15, 'end_date': 1, 'contract_title': 1}
leads with a borrowed mailbox: 2249 | rows upgraded by a newer dated record: 38 | rows upgraded to an active service seen on the buyer's site: 12
P12 organisations: 108 added: 22 {'no own confirmed mailbox': 69, 'same organisation already in a row': 17} | P13 added: 51237 | P13 skipped: {'bad mailbox': 185, 'not located in Canada (no honest inference)': 2596, "mailbox not the organisation's own": 2128, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 7644}
extras from the lanes' result rows: {'invoicing_requirements': 1623, 'ap_phone': 2010, 'invoice_mailing_address': 1899, 'invoice_portal_url': 66, 'ap_contact_name': 139}
org_extras: 80603 organisations read; filled {'vendor_logo': 8425, 'vendor_phone_v2': 4554, 'po_required': 154, 'buyer_legal_name': 17663, 'buyer_phone_v2': 19956, 'buyer_payment_method_preference_mention_rejected': 11672, 'buyer_logo': 51344, 'buyer_tax_exempt_status_mention_rejected': 184, 'payment_terms': 178, 'buyer_legal_name_v2_rejected_no_overlap': 15325, 'buyer_legal_name_v2_legal_name_stated': 4567, 'buyer_bn': 2075, 'buyer_legal_name_v2_jsonld_legal_name': 1463, 'ap_system_hint_links': 267, 'buyer_legal_name_v2_jsonld_name': 1275, 'buyer_payment_method_preference_mention': 201, 'vendor_legal_name': 1474, 'vendor_neq': 32, 'buyer_esignature_preference_mention_rejected': 284, 'vendor_legal_name_v2': 905, 'buyer_address_v2': 3226, 'p13_name_from_legal_name': 7228, 'buyer_esignature_preference_mention': 12, 'vendor_bn': 183, 'invoice_portal_links': 16, 'buyer_tax_exempt_status_mention': 17, 'vendor_address_v2': 409, 'vendor_bn_jsonld': 6, 'buyer_bn_jsonld': 46, 'buyer_ap_cycle_published_mention': 8, 'vendor_qst': 4, 'buyer_ap_cycle_published_mention_rejected': 19, 'p13_name_from_domain': 2}
regional mailboxes of multinationals removed from other-country entities: 20
mx_check: 69559 domains known; 263 mailboxes on domains with no mail server removed; 226 webmail (freemail) addresses removed
dmarc/spf: 69555 domains known; rows {'enforced': 16188, 'exposed': 47895}
same organisation under another key folded into the row that holds its mailbox: 53
second mailbox of the same organisation (same site and mail domain, same name family) folded: 5
org_contacts: 73857 organisations read; filled {'vendor_phone': 19709, 'vendor_emails': 2322, 'buyer_phone': 35832, 'buyer_address': 29430, 'vendor_address': 2451}
ap_terms (evidence pages re-read): 57400 keys read, 57774 pages used across rows; filled {'payment_terms': 272, 'portal': 658, 'format': 287, 'context': 46213, 'payment_method': 389, 'ap_phone': 859, 'tax_exempt': 189, 'po_required': 415, 'ap_cycle': 25, 'address': 459, 'mailbox_gone': 249, 'ap_contact_name': 130, 'buyer_bn': 12, 'esignature': 52, 'buyer_phone_from_page': 11083, 'buyer_address_from_page': 1868}
peppol: 77 Canadian participants; matched buyers 2, vendors 36
municipal / organisation directories: {'matched': 1792, 'legal_name': 820, 'address': 52, 'phone': 337, 'matched_by_place_name': 11, 'website': 18}
charity buyers: {'matched': 7454, 'bn': 6172, 'legal_name': 4158, 'address': 318, 'website': 25}
wikidata: {'buyers': 1667, 'buyer_legal_name': 619, 'vendors': 121, 'buyer_phone': 40, 'buyer_address': 165, 'buyer_website': 72, 'vendor_legal_name': 6, 'vendor_address': 23, 'vendor_website': 51}
crown-corporation BNs applied to inferred-vendor rows: 46999
vendor websites confirmed from search proposals: 206 applied: 597
inferred vendors' published phone / address applied: {'phone': 37247}
Canada's Business Registries: 1513 vendors, 954 buyers found; filled {'buyer_bn': 793, 'buyer_legal_name': 369, 'vendor_bn9': 3044, 'vendor_legal_name': 2472, 'vendor_registered_address': 2436, 'vendor_registry_status': 2472, 'vendor_incorporation_date': 2470, 'vendor_legal_form': 2472, 'vendor_trading_name': 67}
grants & contributions recipient BNs: 3202 buyers, 454 vendors in file; filled {'buyer_bn': 2206, 'buyer_bn_conflict_noted': 71, 'vendor_bn9': 891, 'buyer_legal_name': 1135}
buyers' PO / contract open data joined: {'pairs': 9, 'po_filled': 8, 'contract_filled': 1} | records: 555539
back-references: {'dataset rows with lead relationships': 9734, 'lead rows with dataset history': 89}
sensitivity tags: {'corrections / detention': 26, 'health: mental health / addiction / sexual health': 184, 'intelligence / security / defence': 13, 'police service / police board': 59, 'courts / tribunals / legal aid': 42, 'child / youth protection': 17, 'police oversight body': 3, 'shelter / crisis / sexual-assault service': 53, 'coroner / medical examiner': 1}
narrative columns: {'mailbox meta found': 61449, 'records_with_this_vendor_lead': 10674, 'mailbox meta missing': 2144}
downstream pack skipped: ValueError unsupported format character '(' (0x28) at index 7
rows 66660
[('GOLD', 583), ('A0', 512), ('A1', 742), ('A2', 92), ('A3', 207), ('A4', 9), ('B0', 624), ('B1', 955), ('B2', 145), ('B3', 166), ('B4', 10), ('C0', 1013), ('C1', 315), ('C2', 16), ('C3', 34), ('C4', 25), ('D0', 117), ('D1', 3177), ('D2', 116), ('D3', 148), ('D4', 170), ('E0', 98), ('E1', 2584), ('E2', 43), ('E3', 72), ('E4', 57), ('F0', 1), ('F1', 11), ('F2', 2), ('F3', 3), ('F4', 5), ('GOLD-M', 20), ('GOLD-T', 91), ('I0', 448), ('I1', 49373), ('I2', 174), ('I3', 930), ('I4', 312), ('L0', 223), ('L1', 273), ('L2', 30), ('L3', 23), ('L4', 67), ('M0', 10), ('M1', 134), ('M2', 9), ('M3', 26), ('M4', 1), ('T0', 21), ('T1', 2320), ('T2', 50), ('T3', 72), ('T4', 1)]
with any email: 63593 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            583
P01T_active_service_seen_on_buyer_site_invoicing_AP_email     91
P02_active_relationship_finance_accounting_email           368
P03_active_relationship_purchasing_email                   225
P04_active_relationship_general_email                     1615
P05_likely_active_awarded_12_36_months_any_email           378
P06_client_listing_invoicing_AP_email                      161
P06T_active_service_seen_on_buyer_site_other_email        2432
P07_client_listing_finance_or_purchasing_email             247
P08_client_listing_general_email                          3037
P09_older_contract_or_payment_any_email                    369
P10_linked_from_vendor_site_any_email                     2588
P11_any_relationship_email_not_yet_confirmed               499
P12_weaker_relationship_within_5_years_own_email            21
P13_inferred_relationship_no_record_own_email (10 part files)  50789
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email     20
P06M_member_or_regulated_payer_of_canadian_body_other_email    167
Z_no_email_yet_not_delivered                              3070
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 8912637

# coverage vs the downstream targets (COVERAGE_VS_TARGETS.md)
benchmarks met 15 / 438 (3.4%); near 41; written out/ranked/COVERAGE_VS_TARGETS.md
  gap mta_sts                            P13        0.0% -> 100%  rows needed 50789
  gap tls_rpt                            P13        0.0% -> 100%  rows needed 50789
  gap bimi                               P13        0.0% -> 100%  rows needed 50789
  gap buyer_legal_name_as_published      P13       33.2% ->  60%  rows needed 13632
  gap buyer_address                      P13       74.3% ->  95%  rows needed 10498
  gap buyer_ap_cycle_published           P13        0.0% ->  20%  rows needed 10153
  gap ap_system_hint                     P13        0.1% ->  20%  rows needed 10129
  gap buyer_phone                        P13       77.6% ->  95%  rows needed 8826
  gap buyer_logo_url                     P13       78.3% ->  95%  rows needed 8472
  gap buyer_esignature_preference        P13        0.1% ->  15%  rows needed 7587
  gap buyer_tax_exempt_status            P13        0.1% ->  15%  rows needed 7559
  gap buyer_payment_method_preference    P13        0.7% ->  15%  rows needed 7241
  gap buyer_bn_as_published              P13       17.7% ->  30%  rows needed 6243
  gap mta_sts                            P08        0.0% -> 100%  rows needed 3037
  gap tls_rpt                            P08        0.0% -> 100%  rows needed 3037
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
