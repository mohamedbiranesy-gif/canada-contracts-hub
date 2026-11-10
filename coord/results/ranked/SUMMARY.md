# Ranked buyers — 2026-11-10T08:20Z

```
# Changelog — build 2026-11-10T08:15Z (9209b554)

Build id = the commit that produced this folder; every build is a full regeneration from the same rules, so the delta below is the only thing downstream needs to apply.

- rows: 73828 → 76183
- Gold (P01): 625 → 626
- field changed: buyer_address: 12512
- field changed: buyer_bn_as_published: 7
- field changed: buyer_legal_name_as_published: 171
- field changed: buyer_phone: 18
- field changed: buyer_website: 125
- field changed: dmarc_policy: 20
[    6s +   6s] mailboxes taken from the verification log (better than org_mailboxes' single pick): 734
[   17s +  11s] team vendor contacts (referee-verified): 8781 vendors; 172 with a billing / AR mailbox
[  234s + 217s] same-pair fill (facts from another record of the same buyer-vendor pair): {'solicitation_or_tender_number': 11, 'number_of_bids': 10, 'award_or_notice_id': 2, 'buyer_vendor_id': 2, 'commodity_codes': 9, 'end_date_inferred': 123, 'contract_value': 7, 'procurement_method': 3, 'contract_description': 3, 'po_number_as_published': 3, 'buyer_org_codes': 1, 'start_from_signed': 497, 'end_date': 3, 'contract_or_agreement_number': 2, 'contract_title': 1}
[  235s +   1s] tenant leads from the shards: 2226
[  235s +   0s] leads: 178209 (104993 from the cloud row factory; 49 websites from the lead site finder)
[  240s +   5s] registry leads (.ca domains carrying a confirmed mailbox of their own organisation): 42626
[  248s +   8s] lead rows: facts from the buyer's own pages / the vendor's link label: {'buyer_address_from_own_page': 23053, 'buyer_name_from_own_home_page': 22359, 'buyer_address_from_member_directory': 1378, 'buyer_legal_name_from_register': 1003, 'buyer_name_from_vendor_link_label': 2557}
[  251s +   3s] leads with a borrowed mailbox: 57061 | rows upgraded by a newer dated record: 39 | rows upgraded to an active service seen on the buyer's site: 161
[  261s +  10s] P12 organisations: 96 added: 9 {'no own confirmed mailbox': 67, 'same organisation already in a row': 20} | P13 added: 12655 | P13 skipped: {"mailbox not the organisation's own": 2154, 'bad mailbox': 186, 'not located in Canada (no honest inference)': 3830, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 47936}
[  261s +   0s] lead rows that took the organisation's own key (registry facts attach): {'rows': 42586, 'buyer_address': 5261, 'buyer_name': 1947}
[  508s + 247s] extras from the lanes' result rows: {'invoice_mailing_address': 2230, 'invoicing_requirements': 2066, 'ap_phone': 2325, 'invoice_portal_url': 74, 'ap_contact_name': 160}
[  519s +  12s] org_extras: 83559 organisations read; filled {'vendor_logo': 14448, 'vendor_phone_v2': 7850, 'po_required': 187, 'vendor_trading_name_jsonld': 1514, 'buyer_legal_name': 22498, 'buyer_phone_v2': 32125, 'buyer_payment_method_preference_mention_rejected': 17886, 'buyer_logo': 55002, 'payment_terms': 349, 'buyer_tax_exempt_status_mention_rejected': 269, 'buyer_legal_name_v2_rejected_no_overlap': 25449, 'buyer_legal_name_v2_legal_name_stated': 6799, 'buyer_bn': 2168, 'buyer_legal_name_v2_jsonld_name': 2090, 'buyer_legal_name_v2_jsonld_legal_name': 2598, 'ap_system_hint_links': 316, 'buyer_payment_method_preference_mention': 292, 'vendor_legal_name': 2500, 'vendor_neq': 43, 'buyer_esignature_preference_mention_rejected': 486, 'vendor_legal_name_v2': 1569, 'buyer_address_v2': 4349, 'p13_name_from_legal_name': 6335, 'buyer_esignature_preference_mention': 18, 'vendor_bn': 324, 'invoice_portal_links': 24, 'buyer_tax_exempt_status_mention': 27, 'vendor_address_v2': 371, 'buyer_bn_jsonld': 65, 'buyer_ap_cycle_published_mention': 11, 'vendor_qst': 4, 'vendor_bn_jsonld': 18, 'buyer_ap_cycle_published_mention_rejected': 31, 'p13_name_from_domain': 1}
[  520s +   0s] regional mailboxes of multinationals removed from other-country entities: 31
[  520s +   0s] mx_check: 69559 domains known; 263 mailboxes on domains with no mail server removed; 238 webmail (freemail) addresses removed
[  521s +   1s] dmarc/spf: 81640 domains known; rows {'enforced': 18530, 'exposed': 55090}
[  521s +   0s] same organisation under another key folded into the row that holds its mailbox: 52
[  522s +   1s] second mailbox of the same organisation (same site and mail domain, same name family) folded: 6
[  523s +   1s] org_contacts: 75051 organisations read; filled {'vendor_phone': 15632, 'vendor_emails': 6845, 'buyer_phone': 36773, 'buyer_address': 14813, 'vendor_address': 2278}
[  528s +   5s] ap_terms (evidence pages re-read): 64855 keys read, 85523 pages used across rows; filled {'payment_terms': 1760, 'po_required': 1342, 'payment_method': 619, 'ap_cycle': 94, 'tax_exempt': 777, 'portal': 1691, 'format': 601, 'context': 45925, 'esignature': 398, 'ap_system_portal': 1510, 'ap_phone': 853, 'buyer_bn': 32, 'ap_contact_name': 793, 'address': 474, 'mailbox_gone': 336, 'ap_system': 221, 'setup_url': 194, 'buyer_phone_from_page': 10054, 'buyer_address_from_page': 663}
[  529s +   0s] peppol: 77 Canadian participants; matched buyers 3, vendors 36
[  530s +   1s] municipal / organisation directories: {'matched': 1778, 'legal_name': 769, 'address': 57, 'phone': 305, 'matched_by_place_name': 9, 'website': 17}
[  530s +   0s] charity buyers: {'matched': 7339, 'bn': 6070, 'legal_name': 3991, 'address': 310, 'website': 26}
[  530s +   1s] wikidata: {'vendors': 1016, 'buyers': 5361, 'buyer_legal_name': 2374, 'buyer_phone': 88, 'buyer_address': 644, 'buyer_website': 109, 'vendor_legal_name': 33, 'vendor_address': 285, 'vendor_website': 196, 'vendor_neq': 5}
[  531s +   0s] crown-corporation BNs applied to inferred-vendor rows: 11381
[  531s +   0s] vendor websites confirmed from search proposals: 502 applied: 5700
[  531s +   0s] inferred vendors' published phone / address applied: {'phone': 7347}
[  531s +   0s] registry bulk rows added (no API row for the key): 7508
[  532s +   0s] Canada's Business Registries + registry open data: 2798 vendors, 14357 buyers found; filled {'buyer_bn': 5561, 'buyer_legal_name': 7849, 'vendor_registered_address': 3287, 'vendor_bn9': 5841, 'vendor_legal_name': 3245, 'vendor_registry_status': 3246, 'vendor_incorporation_date': 3436, 'vendor_legal_form': 3246, 'vendor_neq': 544, 'vendor_trading_name': 108, 'buyer_address': 248, 'vendor_skipped_legal_form': 1, 'vendor_bn9_other_registry': 4}
[  532s +   0s] award facts from the buyers' own award pages: 237 pairs with a page; filled {'contract_value': 41, 'end_date': 17, 'start_date': 10, 'number_of_bids': 2, 'contract_or_agreement_number': 3, 'solicitation_or_tender_number': 7, 'term': 2, 'po_number_as_published': 1}
[  532s +   0s] grants & contributions recipient BNs: 3202 buyers, 454 vendors in file; filled {'buyer_bn': 1626, 'buyer_bn_conflict_noted': 94, 'vendor_bn9': 776, 'buyer_legal_name': 320}
[  544s +  12s] buyers' PO / contract open data joined: {'pairs': 12, 'po_filled': 11, 'contract_filled': 1} | records: 555539
[  548s +   4s] back-references: {'dataset rows with lead relationships': 50184, 'lead rows with dataset history': 91}
[  553s +   5s] sensitivity tags: {'corrections / detention': 25, 'health: mental health / addiction / sexual health': 200, 'intelligence / security / defence': 16, 'police service / police board': 67, 'courts / tribunals / legal aid': 54, 'child / youth protection': 20, 'police oversight body': 3, 'shelter / crisis / sexual-assault service': 65, 'coroner / medical examiner': 1}
[  555s +   2s] site readers, second pass (websites found late): {'buyer_logo': 603, 'vendor_emails': 536, 'vendor_phone': 881, 'vendor_logo': 14647, 'buyer_phone': 48, 'vendor_address': 289, 'buyer_address': 6}
[  555s +   1s] same-vendor carry-over (BN9 / address from the vendor's other rows): {'bn9': 28497, 'address': 111}
[  558s +   3s] narrative columns: {'mailbox meta found': 70457, 'contract_description_from_title': 44909, 'contract_title_from_description': 162, 'invoice_reference_hint_po_rule': 755, 'records_with_this_vendor_lead': 58796, 'mailbox meta missing': 2402}
[  596s +  38s] downstream pack: {'tax_derived_foreign': 4795, 'pay_on_sight_yes': 1839, 'ap_payable_today': 1326, 'ship_ready_yes': 692, 'buyer_trade_name_as_published': 33564, 'tax_derived': 56040, 'registry_note': 217, 'prompt_payment_default': 212, 'pay_on_sight_no': 39354, 'buyer_type_from_name': 9818, 'sensitivity_extra': 141, 'registry_warning': 1006, 'invoice_currency_derived': 66877, 'buyer_address_from_own_page': 537, 'pay_on_sight_routed': 31666, 'currency_default': 2}
[  687s +  91s] rows 76202
[  687s +   0s] [('GOLD', 626), ('A0', 516), ('A1', 713), ('A2', 92), ('A3', 225), ('A4', 8), ('B0', 624), ('B1', 917), ('B2', 129), ('B3', 182), ('B4', 11), ('C0', 1001), ('C1', 288), ('C2', 20), ('C3', 33), ('C4', 28), ('D0', 274), ('D1', 11779), ('D2', 182), ('D3', 373), ('D4', 293), ('E0', 135), ('E1', 2604), ('E2', 51), ('E3', 82), ('E4', 62), ('F0', 1), ('F1', 5), ('F2', 1), ('F3', 1), ('F4', 1), ('GOLD-M', 26), ('GOLD-T', 137), ('I0', 432), ('I1', 11874), ('I2', 61), ('I3', 187), ('I4', 101), ('L0', 219), ('L1', 266), ('L2', 34), ('L3', 23), ('L4', 68), ('M0', 9), ('M1', 1741), ('M2', 19), ('M3', 40), ('M4', 1), ('R0', 52), ('R1', 27677), ('R2', 65), ('R3', 556), ('R4', 99), ('T0', 80), ('T1', 10877), ('T2', 68), ('T3', 228), ('T4', 5)]
[  688s +   0s] with any email: 72859 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            626
P01T_active_service_seen_on_buyer_site_invoicing_AP_email    137
P02_active_relationship_finance_accounting_email           403
P03_active_relationship_purchasing_email                   209
P04_active_relationship_general_email                     1571
P05_likely_active_awarded_12_36_months_any_email           378
P06_client_listing_invoicing_AP_email                      279
P06T_active_service_seen_on_buyer_site_other_email (4 part files)   9335
P07_client_listing_finance_or_purchasing_email             532
P08_client_listing_general_email (4 part files)          11352
P09_older_contract_or_payment_any_email                    349
P10_linked_from_vendor_site_any_email                     2631
P10R_ca_domain_registration_contract_own_email (10 part files)  27809
P11_any_relationship_email_not_yet_confirmed              3190
P12_weaker_relationship_within_5_years_own_email             8
P13_inferred_relationship_no_record_own_email (5 part files)  12223
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email     26
P06M_member_or_regulated_payer_of_canadian_body_other_email   1795
Z_no_email_yet_not_delivered                              3349
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 8592312

# coverage vs the downstream targets (COVERAGE_VS_TARGETS.md)
benchmarks met 103 / 446 (23.1%); near 67; written out/ranked/COVERAGE_VS_TARGETS.md
  gap vendor_registered_address          P08       14.5% ->  70%  rows needed 6296
  gap buyer_ap_cycle_published           P10R       0.0% ->  20%  rows needed 5558
  gap vendor_logo_url                    P08       51.5% -> 100%  rows needed 5509
  gap ap_system_hint                     P10R       0.4% ->  20%  rows needed 5448
  gap vendor_phone                       P08       38.2% ->  85%  rows needed 5319
  gap buyer_phone                        P08       51.5% ->  95%  rows needed 4942
  gap buyer_logo_url                     P08       57.1% -> 100%  rows needed 4865
  gap buyer_legal_name_as_published      P08       33.3% ->  75%  rows needed 4730
  gap vendor_bn9                         P08       11.9% ->  50%  rows needed 4322
  gap vendor_emails                      P08       37.1% ->  75%  rows needed 4302
  gap buyer_tax_exempt_status            P10R       0.1% ->  15%  rows needed 4156
  gap buyer_esignature_preference        P10R       0.1% ->  15%  rows needed 4152
  gap buyer_payment_method_preference    P10R       0.6% ->  15%  rows needed 4003
  gap vendor_trading_name                P08       21.6% ->  50%  rows needed 3228
  gap invoice_reference_hint             P08        0.7% ->  25%  rows needed 2763
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
