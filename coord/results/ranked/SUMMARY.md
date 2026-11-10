# Ranked buyers — 2026-11-10T09:29Z

```
[    6s +   6s  0.6G] mailboxes taken from the verification log (better than org_mailboxes' single pick): 734
[   17s +  11s  0.4G] team vendor contacts (referee-verified): 8781 vendors; 172 with a billing / AR mailbox
[  182s + 165s  1.8G] same-pair fill (facts from another record of the same buyer-vendor pair): {'solicitation_or_tender_number': 11, 'number_of_bids': 10, 'award_or_notice_id': 2, 'buyer_vendor_id': 2, 'commodity_codes': 9, 'end_date_inferred': 123, 'contract_value': 7, 'procurement_method': 3, 'contract_description': 3, 'po_number_as_published': 3, 'buyer_org_codes': 1, 'start_from_signed': 497, 'end_date': 3, 'contract_or_agreement_number': 2, 'contract_title': 1}
[  184s +   2s  1.9G] tenant leads from the shards: 13228
[  184s +   0s  1.9G] leads: 252372 (168154 from the cloud row factory; 49 websites from the lead site finder)
[  190s +   6s  2.1G] registry leads (.ca domains carrying a confirmed mailbox of their own organisation): 42626
[  198s +   8s  2.2G] lead rows: facts from the buyer's own pages / the vendor's link label: {'buyer_address_from_own_page': 23354, 'buyer_name_from_own_home_page': 24028, 'buyer_address_from_member_directory': 3398, 'buyer_legal_name_from_register': 3400, 'buyer_name_from_vendor_link_label': 2307}
[  200s +   2s  2.2G] leads with a borrowed mailbox: 64967 | rows upgraded by a newer dated record: 40 | rows upgraded to an active service seen on the buyer's site: 261
[  209s +   9s  2.3G] P12 organisations: 97 added: 8 {'no own confirmed mailbox': 67, 'same organisation already in a row': 22} | P13 added: 11075 | P13 skipped: {"mailbox not the organisation's own": 2154, 'bad mailbox': 186, 'not located in Canada (no honest inference)': 4105, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 50111}
[  209s +   0s  2.3G] lead rows that took the organisation's own key (registry facts attach): {'rows': 43887, 'buyer_address': 5387, 'buyer_name': 3295}
[  218s +   9s  2.3G] extras from the lanes' result rows: {'invoice_mailing_address': 2257, 'invoicing_requirements': 2085, 'ap_phone': 2353, 'invoice_portal_url': 74, 'ap_contact_name': 162}
[  228s +  10s  2.4G] org_extras: 83559 organisations read; filled {'vendor_logo': 14737, 'vendor_phone_v2': 7577, 'po_required': 187, 'vendor_trading_name_jsonld': 1433, 'buyer_legal_name': 22520, 'buyer_phone_v2': 30918, 'buyer_payment_method_preference_mention_rejected': 17896, 'buyer_logo': 55085, 'payment_terms': 351, 'buyer_tax_exempt_status_mention_rejected': 270, 'buyer_legal_name_v2_rejected_no_overlap': 25462, 'buyer_legal_name_v2_legal_name_stated': 6801, 'buyer_bn': 2169, 'buyer_legal_name_v2_jsonld_name': 2091, 'buyer_legal_name_v2_jsonld_legal_name': 2598, 'ap_system_hint_links': 317, 'buyer_payment_method_preference_mention': 292, 'vendor_legal_name': 2405, 'vendor_neq': 36, 'buyer_esignature_preference_mention_rejected': 487, 'vendor_legal_name_v2': 1460, 'buyer_address_v2': 4246, 'p13_name_from_legal_name': 6314, 'buyer_esignature_preference_mention': 18, 'vendor_bn': 301, 'invoice_portal_links': 24, 'buyer_tax_exempt_status_mention': 28, 'vendor_address_v2': 347, 'buyer_bn_jsonld': 65, 'buyer_ap_cycle_published_mention': 11, 'vendor_qst': 4, 'vendor_bn_jsonld': 18, 'buyer_ap_cycle_published_mention_rejected': 31, 'p13_name_from_domain': 1}
[  228s +   0s  2.4G] regional mailboxes of multinationals removed from other-country entities: 31
[  228s +   0s  2.4G] mx_check: 69559 domains known; 262 mailboxes on domains with no mail server removed; 238 webmail (freemail) addresses removed
[  229s +   1s  2.5G] dmarc/spf: 81640 domains known; rows {'enforced': 18686, 'exposed': 55788}
[  229s +   0s  2.5G] same organisation under another key folded into the row that holds its mailbox: 52
[  230s +   1s  2.5G] second mailbox of the same organisation (same site and mail domain, same name family) folded: 6
[  231s +   1s  2.5G] org_contacts: 75051 organisations read; filled {'vendor_phone': 14738, 'vendor_emails': 7106, 'buyer_phone': 36831, 'buyer_address': 14420, 'vendor_address': 2119}
[  236s +   5s  2.9G] ap_terms (evidence pages re-read): 64855 keys read, 85064 pages used across rows; filled {'payment_terms': 1746, 'po_required': 1333, 'payment_method': 613, 'ap_cycle': 93, 'tax_exempt': 772, 'portal': 1681, 'format': 596, 'context': 45924, 'esignature': 396, 'ap_system_portal': 1505, 'ap_phone': 852, 'buyer_bn': 32, 'ap_contact_name': 792, 'address': 474, 'mailbox_gone': 337, 'ap_system': 219, 'setup_url': 194, 'buyer_phone_from_page': 9631, 'buyer_address_from_page': 662}
[  238s +   1s  2.8G] peppol: 77 Canadian participants; matched buyers 3, vendors 36
[  239s +   1s  2.8G] municipal / organisation directories: {'matched': 1772, 'legal_name': 767, 'address': 56, 'phone': 304, 'matched_by_place_name': 9, 'website': 17}
[  239s +   0s  2.8G] charity buyers: {'matched': 7333, 'bn': 6066, 'legal_name': 3997, 'address': 309, 'website': 26}
[  239s +   1s  2.8G] wikidata: {'vendors': 978, 'buyers': 5326, 'buyer_legal_name': 2364, 'buyer_phone': 87, 'buyer_address': 640, 'buyer_website': 109, 'vendor_legal_name': 29, 'vendor_address': 281, 'vendor_website': 191, 'vendor_neq': 5}
[  240s +   0s  2.8G] crown-corporation BNs applied to inferred-vendor rows: 9861
[  240s +   0s  2.8G] vendor websites confirmed from search proposals: 502 applied: 5678
[  240s +   0s  2.8G] inferred vendors' published phone / address applied: {'phone': 6954}
[  240s +   0s  2.9G] registry bulk rows added (no API row for the key): 7508
[  241s +   0s  2.9G] Canada's Business Registries + registry open data: 2798 vendors, 14357 buyers found; filled {'buyer_bn': 5537, 'buyer_legal_name': 6968, 'vendor_registered_address': 3186, 'vendor_bn9': 5762, 'vendor_legal_name': 3148, 'vendor_registry_status': 3149, 'vendor_incorporation_date': 3331, 'vendor_legal_form': 3149, 'vendor_neq': 513, 'vendor_trading_name': 101, 'buyer_address': 242, 'vendor_skipped_legal_form': 1, 'vendor_bn9_other_registry': 4}
[  241s +   0s  2.9G] award facts from the buyers' own award pages: 237 pairs with a page; filled {'contract_value': 41, 'end_date': 17, 'start_date': 10, 'number_of_bids': 2, 'contract_or_agreement_number': 3, 'solicitation_or_tender_number': 7, 'term': 2, 'po_number_as_published': 1}
[  241s +   0s  2.9G] grants & contributions recipient BNs: 3202 buyers, 454 vendors in file; filled {'buyer_bn': 1611, 'buyer_bn_conflict_noted': 93, 'vendor_bn9': 733, 'buyer_legal_name': 307}
[  249s +   9s  2.9G] buyers' PO / contract open data joined: {'pairs': 14, 'po_filled': 13, 'contract_filled': 1} | records read: 330978 | kept (a row's own buyer-vendor pair): 302
[  256s +   6s  3.1G] back-references: {'dataset rows with lead relationships': 49134, 'lead rows with dataset history': 104}
[  261s +   5s  2.9G] sensitivity tags: {'corrections / detention': 25, 'health: mental health / addiction / sexual health': 199, 'intelligence / security / defence': 16, 'police service / police board': 67, 'courts / tribunals / legal aid': 54, 'child / youth protection': 20, 'police oversight body': 3, 'shelter / crisis / sexual-assault service': 66, 'coroner / medical examiner': 1}
[  263s +   2s  2.9G] site readers, second pass (websites found late): {'buyer_logo': 599, 'vendor_emails': 532, 'vendor_phone': 875, 'vendor_logo': 14150, 'buyer_phone': 48, 'vendor_address': 288, 'buyer_address': 6}
[  264s +   1s  2.9G] same-vendor carry-over (BN9 / address from the vendor's other rows): {'bn9': 26130, 'address': 107}
[  365s + 101s  4.0G] narrative columns: {'mailbox meta found': 71219, 'contract_description_from_title': 48330, 'contract_title_from_description': 161, 'invoice_reference_hint_po_rule': 749, 'records_with_this_vendor_lead': 61229, 'mailbox meta missing': 2453}
[  365s +   0s  4.0G] downstream pack: {'tax_derived_foreign': 4778, 'pay_on_sight_yes': 1753, 'ap_payable_today': 1325, 'ship_ready_yes': 749, 'buyer_trade_name_as_published': 32680, 'tax_derived': 56992, 'registry_note': 214, 'prompt_payment_default': 260, 'pay_on_sight_no': 43467, 'buyer_type_from_name': 9536, 'sensitivity_extra': 141, 'registry_warning': 997, 'invoice_currency_derived': 65602, 'buyer_address_from_own_page': 416, 'pay_on_sight_routed': 28452, 'currency_default': 2}# Changelog — build 2026-11-10T09:23Z (16ba0e7)

Build id = the commit that produced this folder; every build is a full regeneration from the same rules, so the delta below is the only thing downstream needs to apply.

- rows: 76916 → 77036
- Gold (P01): 626 → 626
- field changed: ap_contact_name_as_published: 1
- field changed: buyer_address: 12
- field changed: buyer_bn_as_published: 9
- field changed: buyer_legal_name_as_published: 29
- field changed: buyer_phone: 6
- field changed: buyer_website: 7

[  386s +  21s  4.0G] rows 77055
[  386s +   0s  4.0G] [('GOLD', 626), ('A0', 516), ('A1', 713), ('A2', 92), ('A3', 225), ('A4', 8), ('B0', 625), ('B1', 915), ('B2', 129), ('B3', 182), ('B4', 11), ('C0', 1000), ('C1', 259), ('C2', 19), ('C3', 27), ('C4', 26), ('D0', 265), ('D1', 10734), ('D2', 171), ('D3', 353), ('D4', 276), ('E0', 130), ('E1', 2388), ('E2', 48), ('E3', 73), ('E4', 54), ('F0', 1), ('F1', 4), ('F2', 1), ('F3', 1), ('F4', 1), ('GOLD-M', 47), ('GOLD-T', 173), ('I0', 431), ('I1', 10315), ('I2', 58), ('I3', 178), ('I4', 93), ('L0', 219), ('L1', 261), ('L2', 32), ('L3', 20), ('L4', 65), ('M0', 9), ('M1', 4099), ('M2', 17), ('M3', 57), ('M4', 1), ('R0', 45), ('R1', 25386), ('R2', 62), ('R3', 507), ('R4', 82), ('T0', 142), ('T1', 14461), ('T2', 96), ('T3', 318), ('T4', 8)]
[  386s +   0s  4.0G] with any email: 73672 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            626
P01T_active_service_seen_on_buyer_site_invoicing_AP_email    173
P02_active_relationship_finance_accounting_email           403
P03_active_relationship_purchasing_email                   209
P04_active_relationship_general_email                     1569
P05_likely_active_awarded_12_36_months_any_email           365
P06_client_listing_invoicing_AP_email                      263
P06T_active_service_seen_on_buyer_site_other_email (5 part files)  12949
P07_client_listing_finance_or_purchasing_email             501
P08_client_listing_general_email (3 part files)          10340
P09_older_contract_or_payment_any_email                    312
P10_linked_from_vendor_site_any_email                     2406
P10R_ca_domain_registration_contract_own_email (9 part files)  25497
P11_any_relationship_email_not_yet_confirmed              3187
P12_weaker_relationship_within_5_years_own_email             7
P13_inferred_relationship_no_record_own_email (4 part files)  10644
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email     47
P06M_member_or_regulated_payer_of_canadian_body_other_email (2 part files)   4103
Z_no_email_yet_not_delivered                              3454
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 8648534

# coverage vs the downstream targets (COVERAGE_VS_TARGETS.md)
benchmarks met 99 / 446 (22.2%); near 64; written out/ranked/COVERAGE_VS_TARGETS.md
  gap vendor_registered_address          P08       14.7% ->  70%  rows needed 5715
  gap buyer_ap_cycle_published           P10R       0.0% ->  20%  rows needed 5096
  gap vendor_logo_url                    P08       51.4% -> 100%  rows needed 5022
  gap ap_system_hint                     P10R       0.4% ->  20%  rows needed 4994
  gap vendor_phone                       P08       37.9% ->  85%  rows needed 4865
  gap buyer_phone                        P08       50.7% ->  95%  rows needed 4577
  gap buyer_logo_url                     P08       56.5% -> 100%  rows needed 4496
  gap buyer_legal_name_as_published      P08       32.7% ->  75%  rows needed 4371
  gap vendor_emails                      P08       36.8% ->  75%  rows needed 3946
  gap vendor_bn9                         P08       12.4% ->  50%  rows needed 3892
  gap buyer_tax_exempt_status            P10R       0.1% ->  15%  rows needed 3809
  gap buyer_esignature_preference        P10R       0.1% ->  15%  rows needed 3808
  gap buyer_payment_method_preference    P10R       0.6% ->  15%  rows needed 3682
  gap vendor_trading_name                P08       21.7% ->  50%  rows needed 2931
  gap buyer_ap_cycle_published           P06T       0.1% ->  20%  rows needed 2583
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
