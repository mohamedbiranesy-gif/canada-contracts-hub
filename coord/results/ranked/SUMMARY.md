# Ranked buyers — 2026-11-10T02:15Z

```
# Changelog — build 2026-11-10T02:10Z (1017166)

Build id = the commit that produced this folder; every build is a full regeneration from the same rules, so the delta below is the only thing downstream needs to apply.

- rows: 66674 → 67602
- Gold (P01): 624 → 624
- field changed: buyer_address: 4
- field changed: buyer_legal_name_as_published: 101
- field changed: contract_reference: 3
- field changed: email_check: 3
- field changed: ship_ready: 3
- field changed: vendor_address: 3
mailboxes taken from the verification log (better than org_mailboxes' single pick): 685
team vendor contacts (referee-verified): 8781 vendors; 172 with a billing / AR mailbox
same-pair fill (facts from another record of the same buyer-vendor pair): {'solicitation_or_tender_number': 11, 'number_of_bids': 10, 'award_or_notice_id': 2, 'buyer_vendor_id': 2, 'commodity_codes': 9, 'end_date_inferred': 123, 'contract_value': 7, 'procurement_method': 3, 'contract_description': 3, 'po_number_as_published': 3, 'buyer_org_codes': 1, 'start_from_signed': 497, 'end_date': 3, 'contract_or_agreement_number': 2, 'contract_title': 1}
leads: 80477 (9487 from the cloud row factory)
leads with a borrowed mailbox: 2335 | rows upgraded by a newer dated record: 39 | rows upgraded to an active service seen on the buyer's site: 11
P12 organisations: 107 added: 19 {'no own confirmed mailbox': 69, 'same organisation already in a row': 19} | P13 added: 50802 | P13 skipped: {"mailbox not the organisation's own": 2139, 'bad mailbox': 186, 'not located in Canada (no honest inference)': 2938, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 8154}
extras from the lanes' result rows: {'invoice_mailing_address': 1959, 'invoicing_requirements': 1963, 'ap_phone': 2058, 'invoice_portal_url': 74, 'ap_contact_name': 145}
org_extras: 83533 organisations read; filled {'vendor_logo': 8911, 'vendor_phone_v2': 4956, 'po_required': 180, 'vendor_trading_name_jsonld': 1139, 'buyer_legal_name': 22134, 'buyer_phone_v2': 32156, 'buyer_payment_method_preference_mention_rejected': 17870, 'buyer_logo': 54548, 'payment_terms': 290, 'buyer_tax_exempt_status_mention_rejected': 268, 'buyer_legal_name_v2_rejected_no_overlap': 25730, 'buyer_legal_name_v2_legal_name_stated': 6594, 'buyer_bn': 2162, 'buyer_legal_name_v2_jsonld_name': 2052, 'buyer_legal_name_v2_jsonld_legal_name': 2581, 'ap_system_hint_links': 307, 'buyer_payment_method_preference_mention': 290, 'vendor_legal_name': 1586, 'vendor_neq': 32, 'buyer_esignature_preference_mention_rejected': 486, 'vendor_legal_name_v2': 913, 'buyer_address_v2': 6174, 'p13_name_from_legal_name': 9821, 'buyer_esignature_preference_mention': 18, 'vendor_bn': 198, 'invoice_portal_links': 24, 'buyer_tax_exempt_status_mention': 27, 'vendor_address_v2': 416, 'vendor_bn_jsonld': 20, 'buyer_bn_jsonld': 65, 'buyer_ap_cycle_published_mention': 11, 'vendor_qst': 4, 'buyer_ap_cycle_published_mention_rejected': 31, 'p13_name_from_domain': 2}
regional mailboxes of multinationals removed from other-country entities: 20
mx_check: 69559 domains known; 263 mailboxes on domains with no mail server removed; 226 webmail (freemail) addresses removed
dmarc/spf: 73924 domains known; rows {'enforced': 16510, 'exposed': 48546}
same organisation under another key folded into the row that holds its mailbox: 52
second mailbox of the same organisation (same site and mail domain, same name family) folded: 7
org_contacts: 75023 organisations read; filled {'vendor_phone': 20042, 'vendor_emails': 2639, 'buyer_phone': 36438, 'buyer_address': 27100, 'vendor_address': 2505}
ap_terms (evidence pages re-read): 64855 keys read, 85935 pages used across rows; filled {'payment_terms': 1778, 'po_required': 1350, 'payment_method': 620, 'ap_cycle': 95, 'tax_exempt': 781, 'portal': 1700, 'format': 603, 'context': 46005, 'esignature': 403, 'ap_system_portal': 1517, 'ap_phone': 858, 'buyer_bn': 31, 'ap_contact_name': 794, 'address': 474, 'mailbox_gone': 296, 'ap_system': 221, 'setup_url': 195, 'buyer_phone_from_page': 10091, 'buyer_address_from_page': 1764}
peppol: 77 Canadian participants; matched buyers 2, vendors 36
municipal / organisation directories: {'matched': 1818, 'legal_name': 754, 'address': 52, 'phone': 298, 'matched_by_place_name': 11, 'website': 17}
charity buyers: {'matched': 7390, 'bn': 6112, 'legal_name': 4023, 'address': 321, 'website': 26}
wikidata: {'vendors': 1047, 'buyers': 5422, 'buyer_legal_name': 2422, 'buyer_phone': 85, 'buyer_address': 660, 'buyer_website': 109, 'vendor_legal_name': 36, 'vendor_address': 290, 'vendor_website': 203, 'vendor_neq': 6}
crown-corporation BNs applied to inferred-vendor rows: 46601
vendor websites confirmed from search proposals: 502 applied: 3083
inferred vendors' published phone / address applied: {'phone': 36917}
registry bulk rows added (no API row for the key): 7508
Canada's Business Registries + registry open data: 2798 vendors, 14357 buyers found; filled {'buyer_bn': 5587, 'buyer_legal_name': 7968, 'vendor_registered_address': 3142, 'vendor_bn9': 3257, 'vendor_legal_name': 3096, 'vendor_registry_status': 3097, 'vendor_incorporation_date': 3298, 'vendor_legal_form': 3097, 'vendor_neq': 513, 'vendor_trading_name': 110, 'buyer_address': 253, 'vendor_skipped_legal_form': 1, 'vendor_bn9_other_registry': 4}
award facts from the buyers' own award pages: 237 pairs with a page; filled {'contract_value': 41, 'end_date': 17, 'start_date': 10, 'number_of_bids': 2, 'contract_or_agreement_number': 3, 'solicitation_or_tender_number': 7, 'term': 2, 'po_number_as_published': 1}
grants & contributions recipient BNs: 3202 buyers, 454 vendors in file; filled {'buyer_bn': 1651, 'buyer_bn_conflict_noted': 93, 'vendor_bn9': 823, 'buyer_legal_name': 334}
buyers' PO / contract open data joined: {'pairs': 9, 'po_filled': 8, 'contract_filled': 1} | records: 555539
back-references: {'dataset rows with lead relationships': 11199, 'lead rows with dataset history': 115}
sensitivity tags: {'corrections / detention': 25, 'health: mental health / addiction / sexual health': 185, 'intelligence / security / defence': 15, 'police service / police board': 63, 'courts / tribunals / legal aid': 44, 'child / youth protection': 17, 'police oversight body': 3, 'shelter / crisis / sexual-assault service': 53, 'coroner / medical examiner': 1}
site readers, second pass (websites found late): {'buyer_logo': 605, 'vendor_emails': 544, 'vendor_phone': 893, 'vendor_logo': 45205, 'buyer_phone': 48, 'vendor_address': 291, 'buyer_address': 6}
same-vendor carry-over (BN9 / address from the vendor's other rows): {'bn9': 47, 'address': 58}
narrative columns: {'mailbox meta found': 62383, 'contract_description_from_title': 9335, 'contract_title_from_description': 163, 'invoice_reference_hint_po_rule': 785, 'records_with_this_vendor_lead': 12068, 'mailbox meta missing': 2156}
downstream pack: {'tax_derived_foreign': 2229, 'pay_on_sight_yes': 1658, 'ap_payable_today': 989, 'ship_ready_yes': 637, 'tax_derived': 50149, 'registry_note': 219, 'prompt_payment_default': 134, 'pay_on_sight_no': 40712, 'buyer_type_from_name': 8165, 'sensitivity_extra': 119, 'registry_warning': 997, 'invoice_currency_derived': 59367, 'pay_on_sight_routed': 22169, 'currency_default': 2}
rows 67621
[('GOLD', 624), ('A0', 519), ('A1', 710), ('A2', 92), ('A3', 225), ('A4', 8), ('B0', 626), ('B1', 915), ('B2', 128), ('B3', 183), ('B4', 11), ('C0', 1004), ('C1', 319), ('C2', 20), ('C3', 34), ('C4', 29), ('D0', 137), ('D1', 4487), ('D2', 126), ('D3', 177), ('D4', 190), ('E0', 98), ('E1', 2579), ('E2', 45), ('E3', 74), ('E4', 59), ('F0', 1), ('F1', 11), ('F2', 2), ('F3', 3), ('F4', 2), ('GOLD-M', 18), ('GOLD-T', 92), ('I0', 447), ('I1', 48953), ('I2', 172), ('I3', 924), ('I4', 306), ('L0', 220), ('L1', 272), ('L2', 34), ('L3', 23), ('L4', 68), ('M0', 10), ('M1', 135), ('M2', 9), ('M3', 26), ('M4', 1), ('T0', 20), ('T1', 2319), ('T2', 48), ('T3', 84), ('T4', 2)]
with any email: 64539 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            624
P01T_active_service_seen_on_buyer_site_invoicing_AP_email     92
P02_active_relationship_finance_accounting_email           404
P03_active_relationship_purchasing_email                   208
P04_active_relationship_general_email                     1566
P05_likely_active_awarded_12_36_months_any_email           384
P06_client_listing_invoicing_AP_email                      180
P06T_active_service_seen_on_buyer_site_other_email        2440
P07_client_listing_finance_or_purchasing_email             286
P08_client_listing_general_email (2 part files)           4314
P09_older_contract_or_payment_any_email                    381
P10_linked_from_vendor_site_any_email                     2590
P11_any_relationship_email_not_yet_confirmed               508
P12_weaker_relationship_within_5_years_own_email            18
P13_inferred_relationship_no_record_own_email (18 part files)  50355
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email     18
P06M_member_or_regulated_payer_of_canadian_body_other_email    168
Z_no_email_yet_not_delivered                              3085
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 7744882

# coverage vs the downstream targets (COVERAGE_VS_TARGETS.md)
benchmarks met 101 / 438 (23.1%); near 75; written out/ranked/COVERAGE_VS_TARGETS.md
  gap buyer_ap_cycle_published           P13        0.0% ->  20%  rows needed 10063
  gap ap_system_hint                     P13        0.6% ->  20%  rows needed 9784
  gap buyer_address                      P13       76.0% ->  95%  rows needed 9545
  gap buyer_phone                        P13       79.2% ->  95%  rows needed 7941
  gap buyer_tax_exempt_status            P13        0.1% ->  15%  rows needed 7518
  gap buyer_esignature_preference        P13        0.1% ->  15%  rows needed 7515
  gap buyer_payment_method_preference    P13        0.5% ->  15%  rows needed 7282
  gap buyer_logo_url                     P13       84.2% ->  95%  rows needed 5458
  gap buyer_legal_name_as_published      P13       52.5% ->  60%  rows needed 3789
  gap buyer_bn_as_published              P13       25.9% ->  30%  rows needed 2057
  gap buyer_legal_name_as_published      P08       29.6% ->  75%  rows needed 1957
  gap buyer_address                      P08       54.6% ->  95%  rows needed 1744
  gap vendor_emails                      P08       40.5% ->  75%  rows needed 1487
  gap buyer_phone                        P08       61.3% ->  95%  rows needed 1455
  gap vendor_registered_address          P08       37.2% ->  70%  rows needed 1415
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
