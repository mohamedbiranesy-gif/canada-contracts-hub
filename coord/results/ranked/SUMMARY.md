# Ranked buyers — 2026-11-08T16:12Z

```
# Changelog — build 2026-11-08T16:10Z (b8b4279)

Build id = the commit that produced this folder; every build is a full regeneration from the same rules, so the delta below is the only thing downstream needs to apply.

- rows: 66629 → 66629
- Gold (P01): 585 → 585
- field changed: ap_contact_name_as_published: 39
- field changed: buyer_address: 725
- field changed: buyer_bn_as_published: 121
- field changed: buyer_legal_name_as_published: 3299
- field changed: buyer_phone: 581
- field changed: buyer_website: 3
mailboxes taken from the verification log (better than org_mailboxes' single pick): 626
team vendor contacts (referee-verified): 8716 vendors; 172 with a billing / AR mailbox
same-pair fill (facts from another record of the same buyer-vendor pair): {'solicitation_or_tender_number': 11, 'number_of_bids': 10, 'award_or_notice_id': 3, 'buyer_vendor_id': 2, 'commodity_codes': 8, 'end_date_inferred': 123, 'contract_value': 7, 'procurement_method': 3, 'contract_description': 3, 'po_number_as_published': 3, 'buyer_org_codes': 1, 'start_from_signed': 496, 'contract_or_agreement_number': 15, 'end_date': 1, 'contract_title': 1}
leads with a borrowed mailbox: 2246 | rows upgraded by a newer dated record: 38 | rows upgraded to an active service seen on the buyer's site: 12
P12 organisations: 108 added: 22 {'no own confirmed mailbox': 69, 'same organisation already in a row': 17} | P13 added: 51234 | P13 skipped: {'bad mailbox': 185, 'not located in Canada (no honest inference)': 2498, "mailbox not the organisation's own": 2130, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 7643}
extras from the lanes' result rows: {'invoicing_requirements': 1626, 'invoice_portal_url': 68, 'ap_phone': 2012, 'invoice_mailing_address': 1901, 'ap_contact_name': 139}
org_extras: 79110 organisations read; filled {'vendor_logo': 8423, 'vendor_phone_v2': 4479, 'po_required': 154, 'buyer_legal_name': 17158, 'buyer_phone_v2': 9312, 'buyer_payment_method_preference_mention': 5955, 'buyer_logo': 49360, 'buyer_tax_exempt_status_mention': 130, 'payment_terms': 178, 'buyer_legal_name_v2_legal_name_stated': 6257, 'buyer_bn': 1962, 'buyer_legal_name_v2_jsonld_legal_name': 632, 'ap_system_hint_links': 246, 'buyer_legal_name_v2_jsonld_name': 310, 'vendor_legal_name': 1474, 'vendor_legal_name_v2': 2170, 'vendor_neq': 32, 'buyer_esignature_preference_mention': 164, 'buyer_address_v2': 1457, 'p13_name_from_legal_name': 7059, 'vendor_bn': 183, 'invoice_portal_links': 11, 'vendor_address_v2': 409, 'vendor_bn_jsonld': 5, 'buyer_bn_jsonld': 28, 'buyer_ap_cycle_published_mention': 13, 'vendor_qst': 4, 'p13_name_from_domain': 4}
regional mailboxes of multinationals removed from other-country entities: 20
mx_check: 69559 domains known; 263 mailboxes on domains with no mail server removed; 226 webmail (freemail) addresses removed
dmarc/spf: 69555 domains known; rows {'enforced': 16187, 'exposed': 47896}
same organisation under another key folded into the row that holds its mailbox: 54
second mailbox of the same organisation (same site and mail domain, same name family) folded: 5
org_contacts: 73857 organisations read; filled {'vendor_phone': 19707, 'vendor_emails': 2322, 'buyer_phone': 35832, 'buyer_address': 31168, 'vendor_address': 2451}
ap_terms (evidence pages re-read): 57047 mailboxes read; filled {'format': 261, 'context': 46042, 'payment_method': 354, 'ap_phone': 825, 'po_required': 335, 'payment_terms': 209, 'tax_exempt': 161, 'portal': 602, 'mailbox_gone': 257, 'address': 436, 'ap_contact_name': 39, 'buyer_bn': 12, 'ap_cycle': 19, 'esignature': 51, 'buyer_phone_from_page': 11944, 'buyer_address_from_page': 1869}
peppol: 77 Canadian participants; matched buyers 3, vendors 36
municipal / organisation directories: {'matched': 1831, 'legal_name': 744, 'address': 57, 'phone': 340, 'matched_by_place_name': 12, 'website': 18}
charity buyers: {'matched': 7454, 'bn': 6241, 'legal_name': 4957, 'address': 319, 'website': 25}
wikidata: {'buyers': 1183, 'buyer_legal_name': 349, 'vendors': 126, 'buyer_phone': 33, 'buyer_address': 96, 'buyer_website': 69, 'vendor_legal_name': 6, 'vendor_address': 23, 'vendor_website': 51}
crown-corporation BNs applied to inferred-vendor rows: 46996
vendor websites confirmed from search proposals: 156 applied: 545
inferred vendors' published phone / address applied: {'phone': 37244}
Canada's Business Registries: 1356 vendors, 0 buyers found; filled {'vendor_bn9': 2991, 'vendor_legal_name': 1599, 'vendor_registered_address': 2347, 'vendor_registry_status': 2382, 'vendor_incorporation_date': 2376, 'vendor_legal_form': 2382, 'vendor_trading_name': 97}
grants & contributions recipient BNs: 3186 buyers, 453 vendors in file; filled {'buyer_bn': 2312, 'vendor_bn9': 913, 'buyer_legal_name': 1181, 'buyer_bn_conflict_noted': 46}
buyers' PO / contract open data joined: {'pairs': 19, 'po_filled': 16, 'contract_filled': 2} | records: 555539
back-references: {'dataset rows with lead relationships': 9726, 'lead rows with dataset history': 231}
sensitivity tags: {'corrections / detention': 25, 'health: mental health / addiction / sexual health': 189, 'intelligence / security / defence': 17, 'police service / police board': 67, 'courts / tribunals / legal aid': 43, 'child / youth protection': 15, 'police oversight body': 3, 'shelter / crisis / sexual-assault service': 53, 'coroner / medical examiner': 1}
narrative columns: {'mailbox meta found': 61438, 'records_with_this_vendor_lead': 10666, 'mailbox meta missing': 2144}
downstream pack: {'ship_ready_yes': 585, 'registry_warning': 1264, 'buyer_type_from_name': 6395, 'sensitivity_extra': 134, 'currency_default': 2}
rows 66648
[('GOLD', 585), ('A0', 512), ('A1', 742), ('A2', 92), ('A3', 207), ('A4', 9), ('B0', 623), ('B1', 955), ('B2', 144), ('B3', 164), ('B4', 10), ('C0', 1013), ('C1', 316), ('C2', 15), ('C3', 34), ('C4', 25), ('D0', 117), ('D1', 3178), ('D2', 115), ('D3', 148), ('D4', 169), ('E0', 98), ('E1', 2584), ('E2', 42), ('E3', 72), ('E4', 57), ('F0', 1), ('F1', 11), ('F2', 2), ('F3', 3), ('F4', 5), ('GOLD-M', 20), ('GOLD-T', 91), ('I0', 448), ('I1', 49371), ('I2', 174), ('I3', 930), ('I4', 311), ('L0', 223), ('L1', 273), ('L2', 30), ('L3', 23), ('L4', 66), ('M0', 10), ('M1', 134), ('M2', 9), ('M3', 26), ('M4', 1), ('T0', 21), ('T1', 2318), ('T2', 48), ('T3', 72), ('T4', 1)]
with any email: 63582 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            585
P01T_active_service_seen_on_buyer_site_invoicing_AP_email     91
P02_active_relationship_finance_accounting_email           366
P03_active_relationship_purchasing_email                   224
P04_active_relationship_general_email                     1615
P05_likely_active_awarded_12_36_months_any_email           378
P06_client_listing_invoicing_AP_email                      160
P06T_active_service_seen_on_buyer_site_other_email        2429
P07_client_listing_finance_or_purchasing_email             246
P08_client_listing_general_email                          3038
P09_older_contract_or_payment_any_email                    369
P10_linked_from_vendor_site_any_email                     2587
P11_any_relationship_email_not_yet_confirmed               497
P12_weaker_relationship_within_5_years_own_email            21
P13_inferred_relationship_no_record_own_email (12 part files)  50786
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email     20
P06M_member_or_regulated_payer_of_canadian_body_other_email    167
Z_no_email_yet_not_delivered                              3069
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 6599619

# coverage vs the downstream targets (COVERAGE_VS_TARGETS.md)
benchmarks met 94 / 438 (21.5%); near 46; written out/ranked/COVERAGE_VS_TARGETS.md
  gap buyer_legal_name_as_published      P13       28.8% ->  60%  rows needed 15861
  gap buyer_address                      P13       74.3% ->  95%  rows needed 10516
  gap buyer_logo_url                     P13       74.4% ->  95%  rows needed 10450
  gap buyer_ap_cycle_published           P13        0.0% ->  20%  rows needed 10153
  gap ap_system_hint                     P13        0.3% ->  20%  rows needed 9994
  gap buyer_phone                        P13       76.5% ->  95%  rows needed 9381
  gap buyer_esignature_preference        P13        0.1% ->  15%  rows needed 7563
  gap buyer_tax_exempt_status            P13        0.1% ->  15%  rows needed 7552
  gap buyer_bn_as_published              P13       17.6% ->  30%  rows needed 6294
  gap buyer_payment_method_preference    P13        3.8% ->  15%  rows needed 5689
  gap vendor_registered_address          P10       23.1% ->  70%  rows needed 1214
  gap buyer_address                      P08       64.5% ->  95%  rows needed 929
  gap buyer_bn_as_published              P08        6.5% ->  35%  rows needed 866
  gap vendor_emails                      P08       47.0% ->  75%  rows needed 851
  gap buyer_address                      P10       63.7% ->  95%  rows needed 811
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
