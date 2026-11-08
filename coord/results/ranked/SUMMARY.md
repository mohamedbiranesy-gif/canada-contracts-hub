# Ranked buyers — 2026-11-08T16:55Z

```
# Changelog — build 2026-11-08T16:51Z (48c9ec1)

Build id = the commit that produced this folder; every build is a full regeneration from the same rules, so the delta below is the only thing downstream needs to apply.

- rows: 66629 → 66641
- Gold (P01): 585 → 583
- field changed: ap_contact_name_as_published: 114
- field changed: ap_phone: 437
- field changed: buyer_address: 579
- field changed: buyer_bn_as_published: 296
- field changed: buyer_legal_name_as_published: 6117
- field changed: buyer_phone: 1464
mailboxes taken from the verification log (better than org_mailboxes' single pick): 630
team vendor contacts (referee-verified): 8716 vendors; 172 with a billing / AR mailbox
same-pair fill (facts from another record of the same buyer-vendor pair): {'solicitation_or_tender_number': 11, 'number_of_bids': 10, 'award_or_notice_id': 3, 'buyer_vendor_id': 2, 'commodity_codes': 8, 'end_date_inferred': 123, 'contract_value': 7, 'procurement_method': 3, 'contract_description': 3, 'po_number_as_published': 3, 'buyer_org_codes': 1, 'start_from_signed': 496, 'contract_or_agreement_number': 15, 'end_date': 1, 'contract_title': 1}
leads with a borrowed mailbox: 2249 | rows upgraded by a newer dated record: 38 | rows upgraded to an active service seen on the buyer's site: 12
P12 organisations: 108 added: 22 {'no own confirmed mailbox': 69, 'same organisation already in a row': 17} | P13 added: 51237 | P13 skipped: {'bad mailbox': 185, 'not located in Canada (no honest inference)': 2596, "mailbox not the organisation's own": 2128, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 7644}
extras from the lanes' result rows: {'invoicing_requirements': 1623, 'ap_phone': 2010, 'invoice_mailing_address': 1899, 'invoice_portal_url': 66, 'ap_contact_name': 139}
org_extras: 79793 organisations read; filled {'vendor_logo': 8426, 'vendor_phone_v2': 4552, 'po_required': 154, 'buyer_legal_name': 15697, 'buyer_phone_v2': 14742, 'buyer_payment_method_preference_mention_rejected': 8649, 'buyer_logo': 50318, 'buyer_tax_exempt_status_mention_rejected': 146, 'payment_terms': 178, 'buyer_legal_name_v2_rejected_no_overlap': 10717, 'buyer_legal_name_v2_legal_name_stated': 3571, 'buyer_bn': 2041, 'buyer_legal_name_v2_jsonld_legal_name': 995, 'ap_system_hint_links': 257, 'buyer_legal_name_v2_jsonld_name': 934, 'buyer_payment_method_preference_mention': 150, 'vendor_legal_name': 1475, 'vendor_neq': 32, 'buyer_esignature_preference_mention_rejected': 203, 'vendor_legal_name_v2': 904, 'buyer_address_v2': 1968, 'p13_name_from_legal_name': 5335, 'buyer_esignature_preference_mention': 10, 'vendor_bn': 183, 'invoice_portal_links': 14, 'buyer_tax_exempt_status_mention': 13, 'vendor_address_v2': 409, 'vendor_bn_jsonld': 5, 'buyer_bn_jsonld': 36, 'buyer_ap_cycle_published_mention': 6, 'vendor_qst': 4, 'buyer_ap_cycle_published_mention_rejected': 9, 'p13_name_from_domain': 2}
regional mailboxes of multinationals removed from other-country entities: 20
mx_check: 69559 domains known; 263 mailboxes on domains with no mail server removed; 226 webmail (freemail) addresses removed
dmarc/spf: 69555 domains known; rows {'enforced': 16188, 'exposed': 47895}
same organisation under another key folded into the row that holds its mailbox: 53
second mailbox of the same organisation (same site and mail domain, same name family) folded: 5
org_contacts: 73857 organisations read; filled {'vendor_phone': 19710, 'vendor_emails': 2322, 'buyer_phone': 35832, 'buyer_address': 30661, 'vendor_address': 2452}
ap_terms (evidence pages re-read): 57272 mailboxes read; filled {'format': 278, 'context': 46213, 'payment_method': 367, 'ap_phone': 858, 'payment_terms': 229, 'po_required': 376, 'ap_cycle': 21, 'tax_exempt': 175, 'portal': 628, 'address': 459, 'mailbox_gone': 250, 'ap_contact_name': 126, 'buyer_bn': 14, 'esignature': 51, 'buyer_phone_from_page': 11517, 'buyer_address_from_page': 1870}
peppol: 77 Canadian participants; matched buyers 2, vendors 36
municipal / organisation directories: {'matched': 1787, 'legal_name': 822, 'address': 52, 'phone': 337, 'matched_by_place_name': 11, 'website': 18}
charity buyers: {'matched': 7454, 'bn': 6175, 'legal_name': 4231, 'address': 318, 'website': 25}
wikidata: {'buyers': 1494, 'buyer_legal_name': 553, 'vendors': 121, 'buyer_phone': 37, 'buyer_address': 141, 'buyer_website': 71, 'vendor_legal_name': 6, 'vendor_address': 23, 'vendor_website': 51}
crown-corporation BNs applied to inferred-vendor rows: 46999
vendor websites confirmed from search proposals: 156 applied: 546
inferred vendors' published phone / address applied: {'phone': 37247}
Canada's Business Registries: 823 vendors, 0 buyers found; filled {'vendor_bn9': 2256, 'vendor_legal_name': 1533, 'vendor_registered_address': 1512, 'vendor_registry_status': 1533, 'vendor_incorporation_date': 1534, 'vendor_legal_form': 1533, 'vendor_trading_name': 49}
grants & contributions recipient BNs: 3202 buyers, 454 vendors in file; filled {'buyer_bn': 2291, 'buyer_bn_conflict_noted': 62, 'vendor_bn9': 1046, 'buyer_legal_name': 1169}
buyers' PO / contract open data joined: {'pairs': 9, 'po_filled': 8, 'contract_filled': 1} | records: 555539
back-references: {'dataset rows with lead relationships': 9697, 'lead rows with dataset history': 53}
sensitivity tags: {'corrections / detention': 26, 'health: mental health / addiction / sexual health': 179, 'intelligence / security / defence': 13, 'police service / police board': 59, 'courts / tribunals / legal aid': 42, 'child / youth protection': 17, 'police oversight body': 3, 'shelter / crisis / sexual-assault service': 53, 'coroner / medical examiner': 1}
narrative columns: {'mailbox meta found': 61449, 'records_with_this_vendor_lead': 10674, 'mailbox meta missing': 2144}
downstream pack: {'ship_ready_yes': 585, 'registry_warning': 1007, 'buyer_type_from_name': 5991, 'sensitivity_extra': 114, 'currency_default': 2}
rows 66660
[('GOLD', 583), ('A0', 512), ('A1', 742), ('A2', 92), ('A3', 207), ('A4', 9), ('B0', 624), ('B1', 955), ('B2', 145), ('B3', 166), ('B4', 10), ('C0', 1013), ('C1', 315), ('C2', 16), ('C3', 34), ('C4', 25), ('D0', 117), ('D1', 3177), ('D2', 117), ('D3', 148), ('D4', 170), ('E0', 98), ('E1', 2584), ('E2', 43), ('E3', 72), ('E4', 57), ('F0', 1), ('F1', 11), ('F2', 2), ('F3', 3), ('F4', 5), ('GOLD-M', 20), ('GOLD-T', 91), ('I0', 448), ('I1', 49373), ('I2', 174), ('I3', 930), ('I4', 312), ('L0', 223), ('L1', 273), ('L2', 30), ('L3', 23), ('L4', 67), ('M0', 10), ('M1', 134), ('M2', 9), ('M3', 26), ('M4', 1), ('T0', 21), ('T1', 2320), ('T2', 49), ('T3', 72), ('T4', 1)]
with any email: 63593 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            583
P01T_active_service_seen_on_buyer_site_invoicing_AP_email     91
P02_active_relationship_finance_accounting_email           368
P03_active_relationship_purchasing_email                   225
P04_active_relationship_general_email                     1615
P05_likely_active_awarded_12_36_months_any_email           378
P06_client_listing_invoicing_AP_email                      161
P06T_active_service_seen_on_buyer_site_other_email        2431
P07_client_listing_finance_or_purchasing_email             248
P08_client_listing_general_email                          3037
P09_older_contract_or_payment_any_email                    369
P10_linked_from_vendor_site_any_email                     2588
P11_any_relationship_email_not_yet_confirmed               499
P12_weaker_relationship_within_5_years_own_email            21
P13_inferred_relationship_no_record_own_email (15 part files)  50789
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email     20
P06M_member_or_regulated_payer_of_canadian_body_other_email    167
Z_no_email_yet_not_delivered                              3070
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 7568237

# coverage vs the downstream targets (COVERAGE_VS_TARGETS.md)
benchmarks met 51 / 438 (11.6%); near 55; written out/ranked/COVERAGE_VS_TARGETS.md
  gap buyer_legal_name_as_published      P13       29.4% ->  60%  rows needed 15529
  gap buyer_address                      P13       74.3% ->  95%  rows needed 10523
  gap buyer_ap_cycle_published           P13        0.0% ->  20%  rows needed 10155
  gap ap_system_hint                     P13        0.3% ->  20%  rows needed 9986
  gap buyer_logo_url                     P13       76.3% ->  95%  rows needed 9498
  gap buyer_phone                        P13       76.9% ->  95%  rows needed 9173
  gap buyer_esignature_preference        P13        0.1% ->  15%  rows needed 7589
  gap buyer_tax_exempt_status            P13        0.1% ->  15%  rows needed 7563
  gap buyer_payment_method_preference    P13        0.6% ->  15%  rows needed 7292
  gap buyer_bn_as_published              P13       17.6% ->  30%  rows needed 6283
  gap vendor_registered_address          P10       17.9% ->  70%  rows needed 1348
  gap vendor_registered_address          P08       29.1% ->  70%  rows needed 1241
  gap buyer_legal_name_as_published      P08       35.8% ->  75%  rows needed 1191
  gap buyer_legal_name_as_published      P10       32.1% ->  70%  rows needed 981
  gap buyer_address                      P08       64.5% ->  95%  rows needed 928
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
