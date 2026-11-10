# Ranked buyers — 2026-11-10T08:43Z

```
# Changelog — build 2026-11-10T08:38Z (db5c5f9)

Build id = the commit that produced this folder; every build is a full regeneration from the same rules, so the delta below is the only thing downstream needs to apply.

- rows: 76183 → 76916
- Gold (P01): 626 → 626
- field changed: buyer_address: 9
- field changed: buyer_bn_as_published: 2
- field changed: buyer_legal_name_as_published: 1
- field changed: buyer_phone: 3
- field changed: buyer_website: 15
- field changed: dmarc_policy: 9
[    5s +   5s] mailboxes taken from the verification log (better than org_mailboxes' single pick): 734
[   14s +  10s] team vendor contacts (referee-verified): 8781 vendors; 172 with a billing / AR mailbox
[  181s + 166s] same-pair fill (facts from another record of the same buyer-vendor pair): {'solicitation_or_tender_number': 11, 'number_of_bids': 10, 'award_or_notice_id': 2, 'buyer_vendor_id': 2, 'commodity_codes': 9, 'end_date_inferred': 123, 'contract_value': 7, 'procurement_method': 3, 'contract_description': 3, 'po_number_as_published': 3, 'buyer_org_codes': 1, 'start_from_signed': 497, 'end_date': 3, 'contract_or_agreement_number': 2, 'contract_title': 1}
[  181s +   1s] tenant leads from the shards: 12308
[  181s +   0s] leads: 203034 (119736 from the cloud row factory; 49 websites from the lead site finder)
[  187s +   5s] registry leads (.ca domains carrying a confirmed mailbox of their own organisation): 42626
[  194s +   8s] lead rows: facts from the buyer's own pages / the vendor's link label: {'buyer_address_from_own_page': 23265, 'buyer_name_from_own_home_page': 22305, 'buyer_address_from_member_directory': 3635, 'buyer_legal_name_from_register': 3670, 'buyer_name_from_vendor_link_label': 2464}
[  196s +   2s] leads with a borrowed mailbox: 60549 | rows upgraded by a newer dated record: 39 | rows upgraded to an active service seen on the buyer's site: 166
[  204s +   8s] P12 organisations: 96 added: 9 {'no own confirmed mailbox': 67, 'same organisation already in a row': 20} | P13 added: 11736 | P13 skipped: {"mailbox not the organisation's own": 2154, 'bad mailbox': 186, 'not located in Canada (no honest inference)': 3903, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 49007}
[  204s +   0s] lead rows that took the organisation's own key (registry facts attach): {'rows': 43516, 'buyer_address': 4989, 'buyer_name': 1881}
[  212s +   8s] extras from the lanes' result rows: {'invoice_mailing_address': 2233, 'invoicing_requirements': 2068, 'ap_phone': 2328, 'invoice_portal_url': 74, 'ap_contact_name': 161}
[  223s +  10s] org_extras: 83559 organisations read; filled {'vendor_logo': 14385, 'vendor_phone_v2': 7820, 'po_required': 187, 'vendor_trading_name_jsonld': 1502, 'buyer_legal_name': 22503, 'buyer_phone_v2': 30766, 'buyer_payment_method_preference_mention_rejected': 17888, 'buyer_logo': 55062, 'payment_terms': 349, 'buyer_tax_exempt_status_mention_rejected': 269, 'buyer_legal_name_v2_rejected_no_overlap': 25460, 'buyer_legal_name_v2_legal_name_stated': 6795, 'buyer_bn': 2168, 'buyer_legal_name_v2_jsonld_name': 2088, 'buyer_legal_name_v2_jsonld_legal_name': 2597, 'ap_system_hint_links': 316, 'buyer_payment_method_preference_mention': 292, 'vendor_legal_name': 2495, 'vendor_neq': 39, 'buyer_esignature_preference_mention_rejected': 487, 'vendor_legal_name_v2': 1559, 'buyer_address_v2': 4234, 'p13_name_from_legal_name': 6312, 'buyer_esignature_preference_mention': 18, 'vendor_bn': 326, 'invoice_portal_links': 24, 'buyer_tax_exempt_status_mention': 27, 'vendor_address_v2': 364, 'buyer_bn_jsonld': 65, 'buyer_ap_cycle_published_mention': 11, 'vendor_qst': 4, 'vendor_bn_jsonld': 18, 'buyer_ap_cycle_published_mention_rejected': 31, 'p13_name_from_domain': 1}
[  223s +   0s] regional mailboxes of multinationals removed from other-country entities: 31
[  223s +   0s] mx_check: 69559 domains known; 262 mailboxes on domains with no mail server removed; 238 webmail (freemail) addresses removed
[  224s +   1s] dmarc/spf: 81640 domains known; rows {'enforced': 18644, 'exposed': 55710}
[  224s +   0s] same organisation under another key folded into the row that holds its mailbox: 52
[  225s +   1s] second mailbox of the same organisation (same site and mail domain, same name family) folded: 6
[  226s +   1s] org_contacts: 75051 organisations read; filled {'vendor_phone': 14746, 'vendor_emails': 6826, 'buyer_phone': 36817, 'buyer_address': 14373, 'vendor_address': 2252}
[  230s +   5s] ap_terms (evidence pages re-read): 64855 keys read, 85430 pages used across rows; filled {'payment_terms': 1756, 'po_required': 1339, 'payment_method': 618, 'ap_cycle': 94, 'tax_exempt': 776, 'portal': 1687, 'format': 601, 'context': 45921, 'esignature': 398, 'ap_system_portal': 1507, 'ap_phone': 853, 'buyer_bn': 32, 'ap_contact_name': 793, 'address': 474, 'mailbox_gone': 337, 'ap_system': 221, 'setup_url': 194, 'buyer_phone_from_page': 9596, 'buyer_address_from_page': 662}
[  231s +   0s] peppol: 77 Canadian participants; matched buyers 3, vendors 36
[  232s +   1s] municipal / organisation directories: {'matched': 1780, 'legal_name': 770, 'address': 58, 'phone': 306, 'matched_by_place_name': 9, 'website': 17}
[  232s +   0s] charity buyers: {'matched': 7337, 'bn': 6069, 'legal_name': 3989, 'address': 310, 'website': 26}
[  233s +   1s] wikidata: {'vendors': 1013, 'buyers': 5360, 'buyer_legal_name': 2377, 'buyer_phone': 88, 'buyer_address': 643, 'buyer_website': 109, 'vendor_legal_name': 29, 'vendor_address': 285, 'vendor_website': 197, 'vendor_neq': 5}
[  233s +   0s] crown-corporation BNs applied to inferred-vendor rows: 10453
[  233s +   0s] vendor websites confirmed from search proposals: 502 applied: 5695
[  233s +   0s] inferred vendors' published phone / address applied: {'phone': 7283}
[  233s +   0s] registry bulk rows added (no API row for the key): 7508
[  234s +   0s] Canada's Business Registries + registry open data: 2798 vendors, 14357 buyers found; filled {'buyer_bn': 5552, 'buyer_legal_name': 6873, 'vendor_registered_address': 3275, 'vendor_bn9': 5823, 'vendor_legal_name': 3232, 'vendor_registry_status': 3233, 'vendor_incorporation_date': 3423, 'vendor_legal_form': 3233, 'vendor_neq': 535, 'vendor_trading_name': 102, 'buyer_address': 242, 'vendor_skipped_legal_form': 1, 'vendor_bn9_other_registry': 4}
[  234s +   0s] award facts from the buyers' own award pages: 237 pairs with a page; filled {'contract_value': 41, 'end_date': 17, 'start_date': 10, 'number_of_bids': 2, 'contract_or_agreement_number': 3, 'solicitation_or_tender_number': 7, 'term': 2, 'po_number_as_published': 1}
[  234s +   0s] grants & contributions recipient BNs: 3202 buyers, 454 vendors in file; filled {'buyer_bn': 1618, 'buyer_bn_conflict_noted': 94, 'vendor_bn9': 773, 'buyer_legal_name': 308}
[  245s +  11s] buyers' PO / contract open data joined: {'pairs': 12, 'po_filled': 11, 'contract_filled': 1} | records: 555539
[  249s +   4s] back-references: {'dataset rows with lead relationships': 51769, 'lead rows with dataset history': 92}
[  253s +   4s] sensitivity tags: {'corrections / detention': 25, 'health: mental health / addiction / sexual health': 201, 'intelligence / security / defence': 16, 'police service / police board': 67, 'courts / tribunals / legal aid': 54, 'child / youth protection': 20, 'police oversight body': 3, 'shelter / crisis / sexual-assault service': 65, 'coroner / medical examiner': 1}
[  255s +   2s] site readers, second pass (websites found late): {'buyer_logo': 602, 'vendor_emails': 536, 'vendor_phone': 881, 'vendor_logo': 14588, 'buyer_phone': 48, 'vendor_address': 289, 'buyer_address': 6}
[  256s +   1s] same-vendor carry-over (BN9 / address from the vendor's other rows): {'bn9': 27671, 'address': 111}
[  258s +   3s] narrative columns: {'mailbox meta found': 71142, 'contract_description_from_title': 46852, 'contract_title_from_description': 162, 'invoice_reference_hint_po_rule': 751, 'records_with_this_vendor_lead': 60448, 'mailbox meta missing': 2447}
[  290s +  32s] downstream pack: {'tax_derived_foreign': 4792, 'pay_on_sight_yes': 1817, 'ap_payable_today': 1355, 'ship_ready_yes': 712, 'buyer_trade_name_as_published': 33350, 'tax_derived': 57039, 'registry_note': 217, 'prompt_payment_default': 261, 'pay_on_sight_no': 41530, 'buyer_type_from_name': 9734, 'sensitivity_extra': 141, 'registry_warning': 1002, 'invoice_currency_derived': 67808, 'buyer_address_from_own_page': 437, 'pay_on_sight_routed': 30242, 'currency_default': 2}
[  370s +  80s] rows 76935
[  370s +   0s] [('GOLD', 626), ('A0', 516), ('A1', 713), ('A2', 92), ('A3', 225), ('A4', 8), ('B0', 624), ('B1', 916), ('B2', 129), ('B3', 182), ('B4', 11), ('C0', 1002), ('C1', 287), ('C2', 20), ('C3', 33), ('C4', 28), ('D0', 274), ('D1', 11468), ('D2', 182), ('D3', 370), ('D4', 290), ('E0', 135), ('E1', 2555), ('E2', 51), ('E3', 79), ('E4', 61), ('F0', 1), ('F1', 5), ('F2', 1), ('F3', 1), ('F4', 1), ('GOLD-M', 44), ('GOLD-T', 139), ('I0', 431), ('I1', 10963), ('I2', 61), ('I3', 185), ('I4', 96), ('L0', 219), ('L1', 266), ('L2', 34), ('L3', 22), ('L4', 68), ('M0', 10), ('M1', 4307), ('M2', 19), ('M3', 61), ('M4', 1), ('R0', 49), ('R1', 26867), ('R2', 67), ('R3', 549), ('R4', 91), ('T0', 85), ('T1', 11110), ('T2', 68), ('T3', 232), ('T4', 5)]
[  370s +   0s] with any email: 73589 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            626
P01T_active_service_seen_on_buyer_site_invoicing_AP_email    139
P02_active_relationship_finance_accounting_email           403
P03_active_relationship_purchasing_email                   209
P04_active_relationship_general_email                     1570
P05_likely_active_awarded_12_36_months_any_email           377
P06_client_listing_invoicing_AP_email                      276
P06T_active_service_seen_on_buyer_site_other_email (4 part files)   9559
P07_client_listing_finance_or_purchasing_email             529
P08_client_listing_general_email (4 part files)          11055
P09_older_contract_or_payment_any_email                    348
P10_linked_from_vendor_site_any_email                     2580
P10R_ca_domain_registration_contract_own_email (10 part files)  27005
P11_any_relationship_email_not_yet_confirmed              3168
P12_weaker_relationship_within_5_years_own_email             8
P13_inferred_relationship_no_record_own_email (4 part files)  11305
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email     44
P06M_member_or_regulated_payer_of_canadian_body_other_email (2 part files)   4314
Z_no_email_yet_not_delivered                              3420
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 8633869

# coverage vs the downstream targets (COVERAGE_VS_TARGETS.md)
benchmarks met 102 / 446 (22.9%); near 66; written out/ranked/COVERAGE_VS_TARGETS.md
  gap vendor_registered_address          P08       14.6% ->  70%  rows needed 6129
  gap buyer_ap_cycle_published           P10R       0.0% ->  20%  rows needed 5397
  gap vendor_logo_url                    P08       51.6% -> 100%  rows needed 5354
  gap ap_system_hint                     P10R       0.4% ->  20%  rows needed 5290
  gap vendor_phone                       P08       38.1% ->  85%  rows needed 5182
  gap buyer_phone                        P08       51.2% ->  95%  rows needed 4841
  gap buyer_logo_url                     P08       57.1% -> 100%  rows needed 4746
  gap buyer_legal_name_as_published      P08       33.1% ->  75%  rows needed 4637
  gap vendor_emails                      P08       37.1% ->  75%  rows needed 4194
  gap vendor_bn9                         P08       12.2% ->  50%  rows needed 4184
  gap buyer_tax_exempt_status            P10R       0.1% ->  15%  rows needed 4035
  gap buyer_esignature_preference        P10R       0.1% ->  15%  rows needed 4034
  gap buyer_payment_method_preference    P10R       0.6% ->  15%  rows needed 3890
  gap vendor_trading_name                P08       21.7% ->  50%  rows needed 3133
  gap invoice_reference_hint             P08        0.7% ->  25%  rows needed 2690
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
