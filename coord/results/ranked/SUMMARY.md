# Ranked buyers — 2026-11-10T10:55Z

```
[    6s +   6s  0.7G] mailboxes taken from the verification log (better than org_mailboxes' single pick): 747
[   18s +  12s  0.4G] vendor table: registry matches not used because the legal form differs (partnership vs corporation): 55
[   18s +   0s  0.4G] team vendor contacts (referee-verified): 8781 vendors; 172 with a billing / AR mailbox
[  192s + 174s  1.9G] same-pair fill (facts from another record of the same buyer-vendor pair): {'solicitation_or_tender_number': 11, 'number_of_bids': 10, 'award_or_notice_id': 2, 'buyer_vendor_id': 2, 'commodity_codes': 9, 'end_date_inferred': 120, 'contract_value': 7, 'procurement_method': 3, 'po_number_as_published': 3, 'buyer_org_codes': 1, 'start_from_signed': 497, 'end_date': 3, 'contract_description': 2, 'contract_or_agreement_number': 2, 'contract_title': 1}
[  192s +   0s  1.9G] contract records whose vendor's registry match pairs a partnership with a corporation (registry cells not used): 2244
[  197s +   5s  2.0G] tenant leads from the shards: 0
[  197s +   0s  2.0G] leads: 258853 (187863 from the cloud row factory; 49 websites from the lead site finder)
[  201s +   4s  2.2G] registry leads (.ca domains carrying a confirmed mailbox of their own organisation): 51194
[  211s +  10s  2.3G] lead rows: facts from the buyer's own pages / the vendor's link label: {'buyer_address_from_own_page': 37191, 'buyer_name_from_own_home_page': 35386, 'buyer_address_from_member_directory': 4015, 'buyer_legal_name_from_register': 3644, 'buyer_name_from_vendor_link_label': 2642}
[  211s +   0s  2.3G] client-page links judged (cloud row factory): {'client listing: label names the site': 3165, 'link only, and the site has a .ca registration: the registration takes the row': 1548, "not shown to be a client: the link's label does not name the linked site": 1139, "client listing: 'visit website' on a client page": 216, 'client listing: page address names the site': 184, 'client listing: portfolio page': 178, 'not shown to be a client: a page for clients (forms, resources, login), not a list of them': 159, "not shown to be a client: an organisation's 'our work' programme page": 116, "not shown to be a client: sister site of the page's owner": 85, 'not shown to be a client: article: the client word sits in a slug of 4 words': 29, 'not shown to be a client: dated article': 14, 'not shown to be a client: article: the client word sits in a slug of 5 words': 10, 'not shown to be a client: article: the client word sits in a slug of 6 words': 1}
[  213s +   2s  2.3G] leads with a borrowed mailbox: 76168 | rows upgraded by a newer dated record: 40 | rows upgraded to an active service seen on the buyer's site: 290
[  223s +  10s  2.4G] P12 organisations: 93 added: 9 {'no own confirmed mailbox': 66, 'same organisation already in a row': 18} | P13 added: 10946 | P13 skipped: {"mailbox not the organisation's own": 2155, 'bad mailbox': 186, 'not located in Canada (no honest inference)': 4583, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 52573}
[  223s +   0s  2.4G] lead rows that took the organisation's own key (registry facts attach): {'rows': 43965, 'buyer_address': 5143, 'buyer_name': 3124}
[  235s +  12s  2.4G] extras from the lanes' result rows: {'invoice_mailing_address': 2260, 'invoicing_requirements': 2082, 'ap_phone': 2354, 'invoice_portal_url': 73, 'ap_contact_name': 178}
[  247s +  12s  2.5G] org_extras: 83559 organisations read; filled {'vendor_logo': 21306, 'vendor_phone_v2': 10747, 'po_required': 203, 'vendor_trading_name_jsonld': 2093, 'buyer_legal_name': 23084, 'buyer_phone_v2': 30843, 'buyer_payment_method_preference_mention_rejected': 17924, 'buyer_logo': 56932, 'payment_terms': 404, 'buyer_tax_exempt_status_mention_rejected': 270, 'buyer_legal_name_v2_rejected_no_overlap': 25490, 'buyer_legal_name_v2_legal_name_stated': 6802, 'buyer_bn': 2186, 'buyer_legal_name_v2_jsonld_name': 2094, 'buyer_legal_name_v2_jsonld_legal_name': 2600, 'ap_system_hint_links': 317, 'buyer_payment_method_preference_mention': 294, 'vendor_legal_name': 3404, 'vendor_neq': 56, 'buyer_esignature_preference_mention_rejected': 489, 'vendor_legal_name_v2': 2449, 'buyer_address_v2': 4232, 'p13_name_from_legal_name': 6375, 'buyer_esignature_preference_mention': 18, 'vendor_bn': 414, 'invoice_portal_links': 24, 'buyer_tax_exempt_status_mention': 29, 'vendor_address_v2': 388, 'buyer_bn_jsonld': 65, 'buyer_ap_cycle_published_mention': 11, 'vendor_qst': 5, 'vendor_bn_jsonld': 22, 'buyer_ap_cycle_published_mention_rejected': 31, 'p13_name_from_domain': 1}
[  247s +   0s  2.5G] regional mailboxes of multinationals removed from other-country entities: 41
[  247s +   0s  2.5G] mx_check: 69559 domains known; 262 mailboxes on domains with no mail server removed; 277 webmail (freemail) addresses removed
[  249s +   1s  2.6G] dmarc/spf: 100787 domains known; rows {'enforced': 23855, 'exposed': 69613}
[  249s +   0s  2.6G] same organisation under another key folded into the row that holds its mailbox: 52
[  250s +   2s  2.6G] second mailbox of the same organisation (same site and mail domain, same name family) folded: 6
[  252s +   2s  2.6G] org_contacts: 75051 organisations read; filled {'vendor_phone': 19342, 'vendor_emails': 11645, 'buyer_phone': 37950, 'buyer_address': 14444, 'vendor_address': 2122}
[  258s +   6s  3.0G] ap_terms (evidence pages re-read): 64855 keys read, 84592 pages used across rows; filled {'payment_terms': 1723, 'po_required': 1326, 'payment_method': 604, 'ap_cycle': 91, 'tax_exempt': 769, 'portal': 1677, 'format': 594, 'context': 45893, 'esignature': 394, 'ap_system_portal': 1501, 'ap_phone': 850, 'buyer_bn': 32, 'ap_contact_name': 792, 'address': 474, 'mailbox_gone': 335, 'ap_system': 218, 'setup_url': 193, 'buyer_phone_from_page': 9612, 'buyer_address_from_page': 658}
[  260s +   1s  2.9G] peppol: 77 Canadian participants; matched buyers 5, vendors 38
[  261s +   1s  2.9G] municipal / organisation directories: {'matched': 1786, 'legal_name': 783, 'address': 56, 'phone': 307, 'matched_by_place_name': 9, 'website': 17}
[  261s +   0s  2.9G] charity buyers: {'matched': 7307, 'bn': 6042, 'legal_name': 3989, 'address': 306, 'website': 25}
[  262s +   1s  3.0G] wikidata: {'vendors': 1141, 'buyers': 5300, 'buyer_legal_name': 2358, 'buyer_phone': 86, 'buyer_address': 640, 'buyer_website': 109, 'vendor_legal_name': 37, 'vendor_address': 359, 'vendor_website': 234, 'vendor_neq': 6}
[  262s +   0s  3.0G] crown-corporation BNs applied to inferred-vendor rows: 9738
[  262s +   0s  3.0G] vendor websites confirmed from search proposals: 502 applied: 5785
[  262s +   0s  3.0G] inferred vendors' published phone / address applied: {'phone': 6919}
[  263s +   0s  3.0G] registry bulk rows added (no API row for the key): 7508
[  263s +   1s  3.0G] Canada's Business Registries + registry open data: 2798 vendors, 14357 buyers found; filled {'buyer_bn': 5507, 'buyer_legal_name': 6886, 'vendor_registered_address': 3451, 'vendor_bn9': 5997, 'vendor_legal_name': 3407, 'vendor_registry_status': 3409, 'vendor_incorporation_date': 3618, 'vendor_legal_form': 3416, 'vendor_neq': 513, 'vendor_trading_name': 134, 'buyer_address': 232, 'vendor_skipped_legal_form': 1, 'vendor_bn9_other_registry': 6}
[  263s +   0s  3.0G] award facts from the buyers' own award pages: 237 pairs with a page; filled {'contract_value': 39, 'end_date': 17, 'start_date': 9, 'contract_or_agreement_number': 3, 'solicitation_or_tender_number': 6, 'term': 2, 'po_number_as_published': 1, 'number_of_bids': 1}
[  263s +   0s  3.0G] grants & contributions recipient BNs: 3202 buyers, 454 vendors in file; filled {'buyer_bn': 1600, 'buyer_bn_conflict_noted': 93, 'vendor_bn9': 778, 'buyer_legal_name': 305}
[  273s +   9s  3.0G] buyers' PO / contract open data joined: {'pairs': 14, 'po_filled': 13, 'contract_filled': 1} | records read: 330978 | kept (a row's own buyer-vendor pair): 254
[  279s +   7s  3.2G] back-references: {'dataset rows with lead relationships': 61692, 'lead rows with dataset history': 100}
[  285s +   6s  3.1G] sensitivity tags: {'corrections / detention': 27, 'health: mental health / addiction / sexual health': 225, 'intelligence / security / defence': 18, 'police service / police board': 70, 'courts / tribunals / legal aid': 54, 'child / youth protection': 20, 'police oversight body': 3, 'shelter / crisis / sexual-assault service': 69, 'coroner / medical examiner': 1}# Changelog — build 2026-11-10T10:48Z (7d767f6)

Build id = the commit that produced this folder; every build is a full regeneration from the same rules, so the delta below is the only thing downstream needs to apply.

- rows: 96093 → 96079
- Gold (P01): 626 → 625
- field changed: buyer_address: 15
- field changed: buyer_legal_name_as_published: 3
- field changed: buyer_phone: 3
- field changed: buyer_website: 1
- field changed: contract_reference: 31
- field changed: dmarc_policy: 31

[  288s +   3s  3.1G] site readers, second pass (websites found late): {'buyer_logo': 599, 'vendor_emails': 568, 'vendor_phone': 938, 'vendor_logo': 14258, 'buyer_phone': 48, 'vendor_address': 302, 'buyer_address': 6}
[  289s +   1s  3.1G] same-vendor carry-over (BN9, identity facts and address from the vendor's other rows): {'address': 124, 'bn9': 27293, 'legal_name': 27289, 'trading_name': 27290, 'gst_hst_derived': 27293, 'registry_id': 27287, 'registry_url': 27287, 'registered_address': 27287, 'legal_form': 27287, 'registry_status': 27287, 'registry_match_level': 27288, 'incorporation_date': 27287, 'phone': 3, 'logo_url': 4, 'neq': 1}
[  424s + 135s  2.9G] narrative columns: {'mailbox meta found': 90328, 'contract_description_from_title': 57195, 'contract_title_from_description': 161, 'invoice_reference_hint_po_rule': 756, 'records_with_this_vendor_lead': 80401, 'mailbox meta missing': 2104}
[  424s +   0s  2.9G] downstream pack: {'tax_derived_foreign': 6531, 'pay_on_sight_yes': 1719, 'ap_payable_today': 1345, 'ship_ready_yes': 785, 'buyer_trade_name_as_published': 48191, 'tax_derived': 69600, 'registry_note': 222, 'prompt_payment_default': 329, 'pay_on_sight_no': 61875, 'buyer_type_from_name': 10396, 'sensitivity_extra': 153, 'registry_warning': 1112, 'invoice_currency_derived': 81960, 'buyer_address_from_own_page': 415, 'pay_on_sight_routed': 28838, 'currency_default': 2}
[  451s +  27s  2.9G] rows 96098
[  451s +   0s  2.9G] [('GOLD', 625), ('A0', 516), ('A1', 713), ('A2', 92), ('A3', 225), ('A4', 8), ('B0', 624), ('B1', 985), ('B2', 132), ('B3', 183), ('B4', 11), ('C0', 1000), ('C1', 260), ('C2', 19), ('C3', 27), ('C4', 26), ('D0', 387), ('D1', 20090), ('D2', 208), ('D3', 528), ('D4', 343), ('E0', 188), ('E1', 3414), ('E2', 45), ('E3', 79), ('E4', 54), ('F0', 1), ('F1', 4), ('F2', 1), ('F3', 2), ('F4', 1), ('GOLD-M', 53), ('GOLD-T', 203), ('I0', 431), ('I1', 10172), ('I2', 61), ('I3', 188), ('I4', 94), ('L0', 219), ('L1', 307), ('L2', 34), ('L3', 20), ('L4', 70), ('M0', 14), ('M1', 4383), ('M2', 19), ('M3', 62), ('M4', 1), ('R0', 78), ('R1', 26510), ('R2', 72), ('R3', 525), ('R4', 100), ('T0', 208), ('T1', 20957), ('T2', 103), ('T3', 415), ('T4', 8)]
[  451s +   0s  2.9G] with any email: 92432 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            625
P01T_active_service_seen_on_buyer_site_invoicing_AP_email    203
P02_active_relationship_finance_accounting_email           429
P03_active_relationship_purchasing_email                   218
P04_active_relationship_general_email                     2588
P05_likely_active_awarded_12_36_months_any_email           418
P06_client_listing_invoicing_AP_email                      329
P06T_active_service_seen_on_buyer_site_other_email (7 part files)  19508
P07_client_listing_finance_or_purchasing_email             710
P08_client_listing_general_email (6 part files)          19644
P09_older_contract_or_payment_any_email                    312
P10_linked_from_vendor_site_any_email                     2472
P10R_ca_domain_registration_contract_own_email (11 part files)  26614
P11_any_relationship_email_not_yet_confirmed (2 part files)   3321
P12_weaker_relationship_within_5_years_own_email             8
P13_inferred_relationship_no_record_own_email (4 part files)  10515
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email     53
P06M_member_or_regulated_payer_of_canadian_body_other_email (2 part files)   4395
Z_no_email_yet_not_delivered                              3736
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 10780161

# coverage vs the downstream targets (COVERAGE_VS_TARGETS.md)
benchmarks met 95 / 446 (21.3%); near 54; written out/ranked/COVERAGE_VS_TARGETS.md
  gap buyer_phone                        P08       29.2% ->  95%  rows needed 12928
  gap buyer_logo_url                     P08       34.3% -> 100%  rows needed 12902
  gap vendor_registered_address          P08       10.2% ->  70%  rows needed 11739
  gap buyer_legal_name_as_published      P08       18.4% ->  75%  rows needed 11125
  gap vendor_logo_url                    P08       47.8% -> 100%  rows needed 10263
  gap vendor_phone                       P08       34.7% ->  85%  rows needed 9882
  gap vendor_bn9                         P08        8.7% ->  50%  rows needed 8106
  gap vendor_emails                      P08       35.2% ->  75%  rows needed 7809
  gap vendor_trading_name                P08       18.7% ->  50%  rows needed 6146
  gap buyer_bn_as_published              P08        7.7% ->  35%  rows needed 5371
  gap buyer_ap_cycle_published           P10R       0.0% ->  20%  rows needed 5318
  gap ap_system_hint                     P10R       0.4% ->  20%  rows needed 5213
  gap invoice_reference_hint             P08        0.4% ->  25%  rows needed 4834
  gap buyer_esignature_preference        P10R       0.1% ->  15%  rows needed 3977
  gap buyer_tax_exempt_status            P10R       0.1% ->  15%  rows needed 3976
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
