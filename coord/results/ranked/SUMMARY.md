# Ranked buyers — 2026-11-08T18:18Z

```
# Changelog — build 2026-11-08T18:14Z (0dbb550)

Build id = the commit that produced this folder; every build is a full regeneration from the same rules, so the delta below is the only thing downstream needs to apply.

- rows: 66650 → 66650
- Gold (P01): 582 → 582
- field changed: ap_contact_name_as_published: 6
- field changed: buyer_address: 803
- field changed: buyer_bn_as_published: 174
- field changed: buyer_legal_name_as_published: 1574
- field changed: buyer_phone: 357
- field changed: buyer_website: 4
mailboxes taken from the verification log (better than org_mailboxes' single pick): 633
team vendor contacts (referee-verified): 8716 vendors; 172 with a billing / AR mailbox
same-pair fill (facts from another record of the same buyer-vendor pair): {'solicitation_or_tender_number': 11, 'number_of_bids': 10, 'award_or_notice_id': 3, 'buyer_vendor_id': 2, 'commodity_codes': 8, 'end_date_inferred': 123, 'contract_value': 7, 'procurement_method': 3, 'contract_description': 3, 'po_number_as_published': 3, 'buyer_org_codes': 1, 'start_from_signed': 496, 'contract_or_agreement_number': 15, 'end_date': 1, 'contract_title': 1}
leads with a borrowed mailbox: 2253 | rows upgraded by a newer dated record: 38 | rows upgraded to an active service seen on the buyer's site: 12
P12 organisations: 108 added: 22 {'no own confirmed mailbox': 69, 'same organisation already in a row': 17} | P13 added: 51236 | P13 skipped: {'bad mailbox': 185, 'not located in Canada (no honest inference)': 2682, "mailbox not the organisation's own": 2128, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 7645}
extras from the lanes' result rows: {'invoicing_requirements': 1623, 'ap_phone': 2010, 'invoice_mailing_address': 1899, 'invoice_portal_url': 66, 'ap_contact_name': 139}
org_extras: 82339 organisations read; filled {'vendor_logo': 8431, 'vendor_phone_v2': 4560, 'po_required': 154, 'buyer_legal_name': 20548, 'buyer_phone_v2': 27930, 'buyer_payment_method_preference_mention_rejected': 15994, 'buyer_logo': 53408, 'payment_terms': 180, 'buyer_tax_exempt_status_mention_rejected': 243, 'buyer_legal_name_v2_rejected_no_overlap': 22338, 'buyer_legal_name_v2_legal_name_stated': 5960, 'buyer_bn': 2127, 'buyer_legal_name_v2_jsonld_legal_name': 2192, 'ap_system_hint_links': 275, 'buyer_legal_name_v2_jsonld_name': 1732, 'buyer_payment_method_preference_mention': 263, 'vendor_legal_name': 1476, 'vendor_neq': 32, 'buyer_esignature_preference_mention_rejected': 432, 'vendor_legal_name_v2': 908, 'buyer_address_v2': 5252, 'p13_name_from_legal_name': 9783, 'buyer_esignature_preference_mention': 14, 'vendor_bn': 183, 'invoice_portal_links': 18, 'buyer_tax_exempt_status_mention': 26, 'vendor_address_v2': 411, 'vendor_bn_jsonld': 6, 'buyer_bn_jsonld': 58, 'buyer_ap_cycle_published_mention': 11, 'vendor_qst': 4, 'buyer_ap_cycle_published_mention_rejected': 29, 'p13_name_from_domain': 2}
regional mailboxes of multinationals removed from other-country entities: 20
mx_check: 69559 domains known; 263 mailboxes on domains with no mail server removed; 226 webmail (freemail) addresses removed
dmarc/spf: 72630 domains known; rows {'enforced': 16196, 'exposed': 47907}
same organisation under another key folded into the row that holds its mailbox: 53
second mailbox of the same organisation (same site and mail domain, same name family) folded: 5
org_contacts: 73857 organisations read; filled {'vendor_phone': 19712, 'vendor_emails': 2323, 'buyer_phone': 35835, 'buyer_address': 27420, 'vendor_address': 2453}
ap_terms (evidence pages re-read): 59193 keys read, 63830 pages used across rows; filled {'payment_terms': 412, 'portal': 849, 'format': 335, 'context': 46208, 'payment_method': 487, 'ap_phone': 858, 'tax_exempt': 247, 'po_required': 585, 'ap_cycle': 30, 'address': 459, 'mailbox_gone': 249, 'ap_contact_name': 162, 'buyer_bn': 12, 'esignature': 78, 'buyer_phone_from_page': 10546, 'buyer_address_from_page': 1866}
peppol: 77 Canadian participants; matched buyers 2, vendors 36
municipal / organisation directories: {'matched': 1801, 'legal_name': 820, 'address': 52, 'phone': 337, 'matched_by_place_name': 11, 'website': 18}
charity buyers: {'matched': 7454, 'bn': 6172, 'legal_name': 4148, 'address': 318, 'website': 25}
wikidata: {'buyers': 1903, 'buyer_legal_name': 704, 'vendors': 121, 'buyer_phone': 43, 'buyer_address': 196, 'buyer_website': 90, 'vendor_legal_name': 6, 'vendor_address': 23, 'vendor_website': 51}
crown-corporation BNs applied to inferred-vendor rows: 46998
vendor websites confirmed from search proposals: 206 applied: 598
inferred vendors' published phone / address applied: {'phone': 37246}
registry bulk rows added (no API row for the key): 9432
Canada's Business Registries + registry open data: 2787 vendors, 10233 buyers found; filled {'buyer_bn': 2176, 'buyer_legal_name': 5972, 'vendor_registered_address': 3136, 'vendor_bn9': 3322, 'vendor_legal_name': 3091, 'vendor_registry_status': 3092, 'vendor_incorporation_date': 3294, 'vendor_legal_form': 3092, 'vendor_neq': 422, 'vendor_trading_name': 124, 'buyer_address': 455, 'vendor_skipped_legal_form': 1}
award facts from the buyers' own award pages: 0 pairs with a page; filled {}
grants & contributions recipient BNs: 3202 buyers, 454 vendors in file; filled {'buyer_bn': 1993, 'buyer_bn_conflict_noted': 77, 'vendor_bn9': 818, 'buyer_legal_name': 648}
buyers' PO / contract open data joined: {'pairs': 9, 'po_filled': 8, 'contract_filled': 1} | records: 555539
back-references: {'dataset rows with lead relationships': 9783, 'lead rows with dataset history': 117}
sensitivity tags: {'corrections / detention': 26, 'health: mental health / addiction / sexual health': 187, 'intelligence / security / defence': 14, 'police service / police board': 62, 'courts / tribunals / legal aid': 44, 'child / youth protection': 18, 'police oversight body': 3, 'shelter / crisis / sexual-assault service': 54, 'coroner / medical examiner': 1}
narrative columns: {'mailbox meta found': 61458, 'records_with_this_vendor_lead': 10684, 'mailbox meta missing': 2144}
downstream pack: {'ship_ready_yes': 585, 'tax_derived': 48661, 'registry_warning': 1226, 'prompt_payment_default': 131, 'buyer_type_from_name': 7193, 'sensitivity_extra': 117, 'currency_default': 2}
rows 66669
[('GOLD', 582), ('A0', 512), ('A1', 742), ('A2', 92), ('A3', 207), ('A4', 9), ('B0', 624), ('B1', 955), ('B2', 145), ('B3', 167), ('B4', 10), ('C0', 1013), ('C1', 315), ('C2', 16), ('C3', 34), ('C4', 25), ('D0', 117), ('D1', 3177), ('D2', 118), ('D3', 148), ('D4', 172), ('E0', 98), ('E1', 2584), ('E2', 43), ('E3', 74), ('E4', 57), ('F0', 1), ('F1', 11), ('F2', 2), ('F3', 3), ('F4', 5), ('GOLD-M', 20), ('GOLD-T', 92), ('I0', 448), ('I1', 49373), ('I2', 174), ('I3', 930), ('I4', 311), ('L0', 223), ('L1', 273), ('L2', 31), ('L3', 23), ('L4', 67), ('M0', 10), ('M1', 134), ('M2', 9), ('M3', 26), ('M4', 1), ('T0', 21), ('T1', 2323), ('T2', 49), ('T3', 72), ('T4', 1)]
with any email: 63602 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            582
P01T_active_service_seen_on_buyer_site_invoicing_AP_email     92
P02_active_relationship_finance_accounting_email           369
P03_active_relationship_purchasing_email                   225
P04_active_relationship_general_email                     1615
P05_likely_active_awarded_12_36_months_any_email           379
P06_client_listing_invoicing_AP_email                      163
P06T_active_service_seen_on_buyer_site_other_email        2435
P07_client_listing_finance_or_purchasing_email             249
P08_client_listing_general_email                          3037
P09_older_contract_or_payment_any_email                    369
P10_linked_from_vendor_site_any_email                     2590
P11_any_relationship_email_not_yet_confirmed               498
P12_weaker_relationship_within_5_years_own_email            21
P13_inferred_relationship_no_record_own_email (16 part files)  50788
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email     20
P06M_member_or_regulated_payer_of_canadian_body_other_email    167
Z_no_email_yet_not_delivered                              3070
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 7647707

# coverage vs the downstream targets (COVERAGE_VS_TARGETS.md)
benchmarks met 68 / 438 (15.5%); near 46; written out/ranked/COVERAGE_VS_TARGETS.md
  gap buyer_ap_cycle_published           P13        0.0% ->  20%  rows needed 10150
  gap buyer_address                      P13       75.1% ->  95%  rows needed 10099
  gap ap_system_hint                     P13        0.4% ->  20%  rows needed 9970
  gap buyer_phone                        P13       78.6% ->  95%  rows needed 8311
  gap buyer_esignature_preference        P13        0.1% ->  15%  rows needed 7585
  gap buyer_tax_exempt_status            P13        0.1% ->  15%  rows needed 7550
  gap buyer_legal_name_as_published      P13       45.5% ->  60%  rows needed 7386
  gap buyer_payment_method_preference    P13        0.9% ->  15%  rows needed 7179
  gap buyer_logo_url                     P13       82.4% ->  95%  rows needed 6412
  gap buyer_bn_as_published              P13       19.8% ->  30%  rows needed 5177
  gap buyer_legal_name_as_published      P08       36.9% ->  75%  rows needed 1158
  gap buyer_legal_name_as_published      P10       32.3% ->  70%  rows needed 976
  gap buyer_address                      P08       65.6% ->  95%  rows needed 893
  gap vendor_emails                      P08       47.0% ->  75%  rows needed 851
  gap buyer_address                      P10       64.2% ->  95%  rows needed 799
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
