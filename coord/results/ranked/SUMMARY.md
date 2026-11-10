# Ranked buyers — 2026-11-10T10:17Z

```
[    5s +   5s  0.7G] mailboxes taken from the verification log (better than org_mailboxes' single pick): 747
[   13s +   9s  0.4G] team vendor contacts (referee-verified): 8781 vendors; 172 with a billing / AR mailbox
[  139s + 125s  1.9G] same-pair fill (facts from another record of the same buyer-vendor pair): {'solicitation_or_tender_number': 11, 'number_of_bids': 10, 'award_or_notice_id': 2, 'buyer_vendor_id': 2, 'commodity_codes': 9, 'end_date_inferred': 123, 'contract_value': 7, 'procurement_method': 3, 'contract_description': 3, 'po_number_as_published': 3, 'buyer_org_codes': 1, 'start_from_signed': 497, 'end_date': 3, 'contract_or_agreement_number': 2, 'contract_title': 1}
[  143s +   4s  2.0G] tenant leads from the shards: 0
[  143s +   0s  2.0G] leads: 258574 (187584 from the cloud row factory; 49 websites from the lead site finder)
[  146s +   3s  2.2G] registry leads (.ca domains carrying a confirmed mailbox of their own organisation): 51194
[  154s +   8s  2.3G] lead rows: facts from the buyer's own pages / the vendor's link label: {'buyer_address_from_own_page': 37199, 'buyer_name_from_own_home_page': 35444, 'buyer_address_from_member_directory': 3905, 'buyer_legal_name_from_register': 3497, 'buyer_name_from_vendor_link_label': 2737}
[  156s +   2s  2.3G] leads with a borrowed mailbox: 75954 | rows upgraded by a newer dated record: 42 | rows upgraded to an active service seen on the buyer's site: 307
[  163s +   8s  2.4G] P12 organisations: 97 added: 8 {'no own confirmed mailbox': 67, 'same organisation already in a row': 22} | P13 added: 10983 | P13 skipped: {"mailbox not the organisation's own": 2155, 'bad mailbox': 186, 'not located in Canada (no honest inference)': 4575, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 51348}
[  163s +   0s  2.4G] lead rows that took the organisation's own key (registry facts attach): {'rows': 43928, 'buyer_address': 5167, 'buyer_name': 3264}
[  173s +   9s  2.4G] extras from the lanes' result rows: {'invoice_mailing_address': 2267, 'invoicing_requirements': 2091, 'ap_phone': 2362, 'invoice_portal_url': 74, 'ap_contact_name': 178}
[  182s +  10s  2.5G] org_extras: 83559 organisations read; filled {'vendor_logo': 22179, 'vendor_phone_v2': 11197, 'po_required': 204, 'vendor_trading_name_jsonld': 2094, 'buyer_legal_name': 23089, 'buyer_phone_v2': 30938, 'buyer_payment_method_preference_mention_rejected': 17927, 'buyer_logo': 56943, 'payment_terms': 404, 'buyer_tax_exempt_status_mention_rejected': 271, 'buyer_legal_name_v2_rejected_no_overlap': 25499, 'buyer_legal_name_v2_legal_name_stated': 6801, 'buyer_bn': 2186, 'buyer_legal_name_v2_jsonld_name': 2094, 'buyer_legal_name_v2_jsonld_legal_name': 2600, 'ap_system_hint_links': 317, 'buyer_payment_method_preference_mention': 294, 'vendor_legal_name': 3553, 'vendor_neq': 60, 'buyer_esignature_preference_mention_rejected': 489, 'vendor_legal_name_v2': 2589, 'buyer_address_v2': 4238, 'p13_name_from_legal_name': 6358, 'buyer_esignature_preference_mention': 18, 'vendor_bn': 458, 'invoice_portal_links': 24, 'buyer_tax_exempt_status_mention': 29, 'vendor_address_v2': 428, 'buyer_bn_jsonld': 65, 'buyer_ap_cycle_published_mention': 11, 'vendor_qst': 5, 'vendor_bn_jsonld': 21, 'buyer_ap_cycle_published_mention_rejected': 31, 'p13_name_from_domain': 1}
[  182s +   0s  2.5G] regional mailboxes of multinationals removed from other-country entities: 41
[  183s +   0s  2.5G] mx_check: 69559 domains known; 262 mailboxes on domains with no mail server removed; 277 webmail (freemail) addresses removed
[  184s +   1s  2.6G] dmarc/spf: 100787 domains known; rows {'enforced': 23885, 'exposed': 69597}
[  184s +   0s  2.6G] same organisation under another key folded into the row that holds its mailbox: 52
[  185s +   2s  2.6G] second mailbox of the same organisation (same site and mail domain, same name family) folded: 6
[  187s +   2s  2.6G] org_contacts: 75051 organisations read; filled {'vendor_phone': 19982, 'vendor_emails': 12116, 'buyer_phone': 37961, 'buyer_address': 14466, 'vendor_address': 2514}
[  192s +   5s  3.0G] ap_terms (evidence pages re-read): 64855 keys read, 85034 pages used across rows; filled {'payment_terms': 1745, 'po_required': 1333, 'payment_method': 613, 'ap_cycle': 93, 'tax_exempt': 772, 'portal': 1682, 'format': 596, 'context': 45894, 'esignature': 396, 'ap_system_portal': 1506, 'ap_phone': 851, 'buyer_bn': 32, 'ap_contact_name': 792, 'address': 474, 'mailbox_gone': 335, 'ap_system': 219, 'setup_url': 194, 'buyer_phone_from_page': 9642, 'buyer_address_from_page': 660}
[  193s +   1s  2.9G] peppol: 77 Canadian participants; matched buyers 5, vendors 39
[  194s +   1s  2.9G] municipal / organisation directories: {'matched': 1790, 'legal_name': 784, 'address': 56, 'phone': 307, 'matched_by_place_name': 9, 'website': 17}
[  194s +   0s  2.9G] charity buyers: {'matched': 7320, 'bn': 6054, 'legal_name': 3990, 'address': 309, 'website': 26}
[  195s +   1s  2.9G] wikidata: {'vendors': 1159, 'buyers': 5314, 'buyer_legal_name': 2359, 'buyer_phone': 87, 'buyer_address': 640, 'buyer_website': 109, 'vendor_legal_name': 38, 'vendor_address': 360, 'vendor_website': 233, 'vendor_neq': 6}
[  195s +   0s  2.9G] crown-corporation BNs applied to inferred-vendor rows: 9778
[  195s +   0s  2.9G] vendor websites confirmed from search proposals: 502 applied: 5786
[  195s +   0s  2.9G] inferred vendors' published phone / address applied: {'phone': 6904}
[  195s +   0s  3.0G] registry bulk rows added (no API row for the key): 7508
[  196s +   0s  3.0G] Canada's Business Registries + registry open data: 2798 vendors, 14357 buyers found; filled {'buyer_bn': 5532, 'buyer_legal_name': 6956, 'vendor_registered_address': 3625, 'vendor_bn9': 6105, 'vendor_legal_name': 3583, 'vendor_registry_status': 3585, 'vendor_incorporation_date': 3803, 'vendor_legal_form': 3585, 'vendor_neq': 569, 'vendor_trading_name': 153, 'buyer_address': 242, 'vendor_skipped_legal_form': 1, 'vendor_bn9_other_registry': 6}
[  196s +   0s  3.0G] award facts from the buyers' own award pages: 237 pairs with a page; filled {'contract_value': 41, 'end_date': 17, 'start_date': 10, 'number_of_bids': 2, 'contract_or_agreement_number': 3, 'solicitation_or_tender_number': 7, 'term': 2, 'po_number_as_published': 1}
[  196s +   0s  3.0G] grants & contributions recipient BNs: 3202 buyers, 454 vendors in file; filled {'buyer_bn': 1604, 'buyer_bn_conflict_noted': 93, 'vendor_bn9': 858, 'buyer_legal_name': 305}
[  204s +   7s  3.0G] buyers' PO / contract open data joined: {'pairs': 14, 'po_filled': 13, 'contract_filled': 1} | records read: 330978 | kept (a row's own buyer-vendor pair): 302
[  210s +   6s  3.2G] back-references: {'dataset rows with lead relationships': 61591, 'lead rows with dataset history': 105}
[  214s +   4s  3.1G] sensitivity tags: {'corrections / detention': 27, 'health: mental health / addiction / sexual health': 225, 'intelligence / security / defence': 18, 'police service / police board': 70, 'courts / tribunals / legal aid': 55, 'child / youth protection': 20, 'police oversight body': 3, 'shelter / crisis / sexual-assault service': 69, 'coroner / medical examiner': 1}
[  216s +   2s  3.1G] site readers, second pass (websites found late): {'buyer_logo': 599, 'vendor_emails': 565, 'vendor_phone': 937, 'vendor_logo': 14238, 'buyer_phone': 48, 'vendor_address': 302, 'buyer_address': 6}
[  217s +   1s  3.1G] same-vendor carry-over (BN9 / address from the vendor's other rows): {'bn9': 25962, 'address': 123}
[  311s +  95s  2.9G] narrative columns: {'mailbox meta found': 90327, 'contract_description_from_title': 56483, 'contract_title_from_description': 161, 'invoice_reference_hint_po_rule': 766, 'records_with_this_vendor_lead': 80378, 'mailbox meta missing': 2104}
[  311s +   0s  2.9G] downstream pack: {'tax_derived_foreign': 6532, 'pay_on_sight_yes': 1762, 'ap_payable_today': 1329, 'ship_ready_yes': 785, 'buyer_trade_name_as_published': 48891, 'tax_derived': 69627, 'registry_note': 226, 'prompt_payment_default': 332, 'pay_on_sight_no': 61899, 'buyer_type_from_name': 10432, 'sensitivity_extra': 154, 'registry_warning': 1137, 'invoice_currency_derived': 82094, 'buyer_address_from_own_page': 415, 'pay_on_sight_routed': 28770, 'currency_default': 2}# Changelog — build 2026-11-10T10:13Z (6eb4193)

Build id = the commit that produced this folder; every build is a full regeneration from the same rules, so the delta below is the only thing downstream needs to apply.

- rows: 77036 → 96093
- Gold (P01): 626 → 626
- field changed: ap_phone: 2
- field changed: buyer_address: 380
- field changed: buyer_bn_as_published: 11
- field changed: buyer_legal_name_as_published: 13
- field changed: buyer_phone: 11
- field changed: buyer_website: 3

[  328s +  16s  2.9G] rows 96112
[  328s +   0s  2.9G] [('GOLD', 626), ('A0', 516), ('A1', 713), ('A2', 92), ('A3', 225), ('A4', 8), ('B0', 625), ('B1', 985), ('B2', 132), ('B3', 183), ('B4', 11), ('C0', 1000), ('C1', 260), ('C2', 19), ('C3', 27), ('C4', 26), ('D0', 435), ('D1', 21514), ('D2', 213), ('D3', 550), ('D4', 358), ('E0', 159), ('E1', 3382), ('E2', 52), ('E3', 89), ('E4', 63), ('F0', 1), ('F1', 4), ('F2', 1), ('F3', 1), ('F4', 1), ('GOLD-M', 53), ('GOLD-T', 203), ('I0', 431), ('I1', 10225), ('I2', 57), ('I3', 180), ('I4', 90), ('L0', 220), ('L1', 307), ('L2', 34), ('L3', 20), ('L4', 69), ('M0', 14), ('M1', 4237), ('M2', 18), ('M3', 62), ('M4', 1), ('R0', 71), ('R1', 25198), ('R2', 62), ('R3', 502), ('R4', 79), ('T0', 209), ('T1', 20969), ('T2', 106), ('T3', 416), ('T4', 8)]
[  328s +   0s  2.9G] with any email: 92431 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            626
P01T_active_service_seen_on_buyer_site_invoicing_AP_email    203
P02_active_relationship_finance_accounting_email           404
P03_active_relationship_purchasing_email                   212
P04_active_relationship_general_email                     1639
P05_likely_active_awarded_12_36_months_any_email           417
P06_client_listing_invoicing_AP_email                      342
P06T_active_service_seen_on_buyer_site_other_email (7 part files)  19524
P07_client_listing_finance_or_purchasing_email             737
P08_client_listing_general_email (6 part files)          21048
P09_older_contract_or_payment_any_email                    312
P10_linked_from_vendor_site_any_email                     3417
P10R_ca_domain_registration_contract_own_email (9 part files)  25308
P11_any_relationship_email_not_yet_confirmed              3312
P12_weaker_relationship_within_5_years_own_email             7
P13_inferred_relationship_no_record_own_email (4 part files)  10552
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email     53
P06M_member_or_regulated_payer_of_canadian_body_other_email (2 part files)   4248
Z_no_email_yet_not_delivered                              3751
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 11083150

# coverage vs the downstream targets (COVERAGE_VS_TARGETS.md)
benchmarks met 94 / 446 (21.1%); near 62; written out/ranked/COVERAGE_VS_TARGETS.md
  gap buyer_logo_url                     P08       33.4% -> 100%  rows needed 14012
  gap buyer_phone                        P08       28.5% ->  95%  rows needed 13997
  gap vendor_registered_address          P08        9.7% ->  70%  rows needed 12701
  gap buyer_legal_name_as_published      P08       18.0% ->  75%  rows needed 11987
  gap vendor_logo_url                    P08       46.1% -> 100%  rows needed 11335
  gap vendor_phone                       P08       33.6% ->  85%  rows needed 10818
  gap vendor_bn9                         P08        8.3% ->  50%  rows needed 8770
  gap vendor_emails                      P08       34.2% ->  75%  rows needed 8592
  gap vendor_trading_name                P08       18.0% ->  50%  rows needed 6728
  gap buyer_bn_as_published              P08        7.6% ->  35%  rows needed 5760
  gap invoice_reference_hint             P08        0.4% ->  25%  rows needed 5185
  gap buyer_ap_cycle_published           P10R       0.0% ->  20%  rows needed 5058
  gap ap_system_hint                     P10R       0.4% ->  20%  rows needed 4958
  gap buyer_address                      P08       73.5% ->  95%  rows needed 4519
  gap buyer_ap_cycle_published           P08        0.0% ->  20%  rows needed 4205
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
