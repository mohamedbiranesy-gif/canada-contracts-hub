# Ranked buyers — 2026-11-11T07:17Z

```
[   19s +  19s  1.7G] mailboxes taken from the verification log (better than org_mailboxes' single pick): 795 | referee mailbox rows whose last label is not a top-level domain: {'left out': 15, 'cut back to the address the page prints': 62}
[   31s +  12s  0.8G] vendor table: registry matches not used because the legal form differs (partnership vs corporation): 55 | 'websites' that are a web host's own site (dropped with their mailboxes): 6 | websites not used for a look-up by domain (unverified, name does not fit): 0 | look-ups by domain: 8050
[   31s +   0s  0.8G] team vendor contacts (referee-verified): 8782 vendors; 172 with a billing / AR mailbox
[  212s + 181s  2.1G] same-pair fill (facts from another record of the same buyer-vendor pair): {'solicitation_or_tender_number': 11, 'number_of_bids': 10, 'award_or_notice_id': 2, 'buyer_vendor_id': 2, 'commodity_codes': 9, 'end_date_inferred': 120, 'contract_value': 7, 'procurement_method': 3, 'po_number_as_published': 3, 'buyer_org_codes': 1, 'start_from_signed': 497, 'end_date': 3, 'contract_description': 2, 'contract_or_agreement_number': 2, 'contract_title': 1}
[  212s +   0s  2.1G] contract records whose vendor's registry match pairs a partnership with a corporation (registry cells not used): 2244
[  224s +  12s  3.3G] tenant leads from the shards: 23323
[  224s +   0s  3.3G] leads: 542678 (448365 from the cloud row factory; 64 websites from the lead site finder)
[  259s +  35s  3.5G] registry leads (.ca domains carrying a confirmed mailbox of their own organisation): 150733
[  259s +   0s  3.5G] organisations' second domain names (the name on file answers at their site under another domain): 0 {}
[  291s +  32s  3.8G] lead rows: facts from the buyer's own pages / the vendor's link label: {'buyer_address_from_own_page': 133961, 'buyer_name_from_own_home_page': 124741, 'facts of another host of the domain not taken': 299, 'vendor_address_cut_out_of_its_quote': 34276, 'buyer_legal_name_from_register': 10839, 'buyer_address_from_member_directory': 6314, 'buyer_name_from_vendor_link_label': 2809} | sites named again from their stored home-page title: 1144
[  291s +   0s  3.8G] client-page links judged (cloud row factory): {'client listing: label names the site': 4640, "not shown to be a client: the link's label does not name the linked site": 1744, 'link only, and the site has a .ca registration: the registration takes the row': 1721, "client listing: 'visit website' on a client page": 448, 'client listing: portfolio page': 314, 'client listing: page address names the site': 228, 'not shown to be a client: a page for clients (forms, resources, login), not a list of them': 202, "not shown to be a client: an organisation's 'our work' programme page": 187, "not shown to be a client: sister site of the page's owner": 102, 'not shown to be a client: article: the client word sits in a slug of 4 words': 65, 'not shown to be a client: dated article': 19, 'not shown to be a client: article: the client word sits in a slug of 5 words': 14, 'not shown to be a client: article: the client word sits in a slug of 6 words': 1}
[  298s +   7s  3.8G] leads with a borrowed mailbox: 117713 | rows upgraded by a newer dated record: 43 | rows upgraded to an active service seen on the buyer's site: 500
[  311s +  14s  3.9G] P12 organisations: 90 added: 8 {'no own confirmed mailbox': 64, 'same organisation already in a row': 18} | P13 added: 18772 | P13 skipped: {"mailbox not the organisation's own": 2278, 'bad mailbox': 198, 'not located in Canada (no honest inference)': 15454, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 73450, '… of which by the NAME alone (its own mailbox and domain are in no row)': 128}
[  311s +   0s  3.9G] lead rows that took the organisation's own key (registry facts attach): {'rows': 45149, 'buyer_address': 4954, 'buyer_name': 3608}
[  340s +  28s  3.9G] extras from the lanes' result rows: {'invoice_mailing_address': 2322, 'invoicing_requirements': 2124, 'ap_phone': 2418, 'invoice_portal_url': 73, 'ap_contact_name': 278}
[  355s +  15s  4.0G] words too common to prove a name (in more than 1 in 2,000 of the 227685 names of organisations whose site was read): 529; names printed on 3+ sites: 1596
[  410s +  55s  4.0G] org_extras: 230575 organisations read; filled {'vendor_logo': 82784, 'vendor_phone_v2': 59799, 'po_required': 269, 'vendor_trading_name_jsonld': 12703, 'buyer_legal_name': 71600, 'buyer_phone_v2': 106513, 'buyer_payment_method_preference_mention_rejected': 18158, 'buyer_logo': 192364, 'payment_terms': 995, 'buyer_tax_exempt_status_mention_rejected': 333, 'buyer_legal_name_v2_legal_name_stated': 19681, "vendor site is a foreign organisation's: its legal / trading name not taken for the Canada-located vendor": 1328, 'buyer_bn': 3422, 'buyer_legal_name_v2_rejected_no_overlap': 53028, 'buyer_legal_name_v2_jsonld_name': 7007, 'buyer_legal_name_v2_printed_on_many_sites': 7698, 'buyer_legal_name_v2_jsonld_legal_name': 7143, 'ap_system_hint_links': 506, 'buyer_legal_name_government_template_credit': 40, 'buyer_payment_method_preference_mention': 1381, 'vendor_legal_name': 14544, 'vendor_neq': 145, 'buyer_esignature_preference_mention_rejected': 537, 'vendor_legal_name_v2': 10854, 'invoice_portal_links': 76, 'buyer_ap_cycle_published_mention': 55, 'vendor_legal_name_v3_stated_as_operator': 82, 'buyer_address_v2': 7390, 'buyer_legal_name_v3_stated_as_operator': 1886, 'p13_name_from_legal_name': 12301, "vendor named by its own site's name instead of its domain": 15481, 'buyer_esignature_preference_mention': 84, 'buyer_legal_name_v3_legal_person_behind_the_site_name': 1875, 'buyer_legal_name_v2_jsonld_legal_name_own_site_node': 435, 'buyer_legal_name_v2_jsonld_name_own_site_node': 520, 'vendor_legal_name_v3_legal_person_behind_the_site_name': 1200, 'vendor_bn': 756, 'vendor_legal_name_v2_site_says': 858, 'buyer_tax_exempt_status_mention': 125, 'vendor_bn_jsonld': 72, 'buyer_bn_jsonld': 167, 'buyer_legal_name_kept_from_the_trademarks_register': 1058, 'vendor_address_v2': 304, 'vendor_address_v2_outside_canada_not_taken': 115, 'buyer_legal_name_v2_stated_as_operator': 59, 'vendor_qst': 19, 'buyer_ap_cycle_published_mention_rejected': 32, 'buyer_legal_name_franchisor_copyright_not_taken': 11, 'buyer_legal_name_v2_doing_business_as': 11, 'p13_name_from_domain': 1}
[  410s +   0s  4.0G] regional mailboxes of multinationals removed from other-country entities: 55
[  411s +   1s  4.0G] mx_check: 69559 domains known; 185 mailboxes on domains with no mail server removed; 858 webmail (freemail) addresses removed
[  415s +   4s  4.3G] dmarc/spf: 263366 domains known; rows {'enforced': 49255, 'exposed': 201503}
[  415s +   0s  4.3G] same organisation under another key folded into the row that holds its mailbox: 52
[  419s +   4s  4.4G] second mailbox of the same organisation (same site and mail domain, same name family) folded: 6
[  425s +   6s  4.6G] org_contacts: 217822 organisations read; filled {'vendor_phone': 67061, 'vendor_emails': 41500, 'buyer_phone': 119087, 'vendor site prints an address outside Canada: address and telephone not taken': 1063, 'buyer_address': 18408, 'vendor_address': 1971}
[  425s +   0s  4.6G] site-reader records read on another host of the row's domain (look-ups): {'org_extras: not taken': 798, 'org_contacts: not taken': 1293, 'org_contacts: taken, read on another host for the same organisation (same name)': 312, 'org_extras: taken, read on another host for the same organisation (same name)': 60, "org_contacts: taken, the row's host is the member directory of the body whose own site was read": 582, "org_extras: taken, the row's host is the member directory of the body whose own site was read": 201}
[  434s +  10s  5.1G] ap_terms (evidence pages re-read): 82907 keys read, 108123 pages used across rows; filled {'payment_terms': 3479, 'po_required': 1869, 'payment_method': 695, 'ap_cycle': 107, 'tax_exempt': 998, 'portal': 1956, 'format': 736, 'context': 45784, 'esignature': 602, 'ap_system_portal': 1697, 'ap_phone': 1103, 'buyer_bn': 52, 'ap_contact_name': 828, 'address': 551, 'mailbox_gone': 336, 'ap_system': 437, 'setup_url': 318, 'buyer_phone_from_page': 9502, 'buyer_address_from_page': 614}
[  437s +   2s  5.0G] peppol: 77 Canadian participants; matched buyers 7, vendors 39
[  437s +   0s  5.0G] directories: 2338 entries reachable by their own site; 112 sites given by entries of different names, left out
[  439s +   2s  5.0G] municipal / organisation directories: {'matched': 1753, 'legal_name': 780, 'phone': 323, 'address': 47, 'matched_by_place_name': 12, 'website': 19}
[  440s +   1s  5.0G] charity buyers: {'matched': 9543, 'bn': 7816, 'legal_name': 6422, 'address': 613, 'website': 32}
[  441s +   1s  5.1G] charity registration numbers found in the CRA list: {'matched': 902, 'legal_name': 558, 'address': 75, 'name_from_the_register': 91, 'holder is a foundation / trust under another name: reported only': 34} | list: 83761
[  442s +   2s  5.2G] wikidata: {'vendors': 1363, 'buyers': 5213, 'buyer_legal_name': 2249, 'buyer_phone': 90, 'buyer_address': 616, 'buyer_website': 107, 'vendor_legal_name': 43, 'vendor_address': 571, 'vendor_website': 232, 'vendor_neq': 6}
[  443s +   1s  5.2G] crown-corporation BNs applied to inferred-vendor rows: 17065
[  443s +   0s  5.2G] vendor websites confirmed from search proposals: 502 applied: 645 {"search proposal not taken: a directory / quote page / register, or a host that does not carry the vendor's name": 496, 'vetted vendor: the site of its own terms page': 27564}
[  444s +   0s  5.2G] inferred vendors' published phone / address applied: {'phone': 13805}
[  444s +   1s  5.2G] registry bulk rows added (no API row for the key): 22305 | registry rows left out, the registered name is only legal-form and place words: 0
[  446s +   2s  5.3G] Canada's Business Registries + registry open data: 3706 vendors, 28246 buyers found; filled {'buyer_bn': 8976, 'buyer_legal_name': 13538, 'vendor_registered_address': 19470, 'vendor_bn9': 29335, 'vendor_legal_name': 19406, 'vendor_registry_status': 19408, 'vendor_incorporation_date': 19695, 'vendor_legal_form': 19415, 'vendor_neq': 7614, 'vendor_trading_name': 245, 'buyer_address': 1983, 'vendor_skipped_legal_form': 1, 'buyer record of another name than the legal person the site itself states, not taken': 132, 'buyer record looked up under a name the row no longer carries, not taken': 8, 'vendor_bn9_other_registry': 4}
[  446s +   0s  5.3G] award facts from the buyers' own award pages: 237 pairs with a page; filled {'contract_value': 39, 'end_date': 17, 'start_date': 9, 'contract_or_agreement_number': 3, 'solicitation_or_tender_number': 6, 'term': 2, 'po_number_as_published': 1, 'number_of_bids': 1}
[  448s +   2s  5.3G] legal names read off a page, tidied: {'tidied': 578, 'owner': 71, 'fragment': 47}
[  449s +   1s  5.3G] legal name: the organisation's own name carries its legal form (cells still empty after every register and site statement): 3944
[  449s +   0s  5.3G] grants & contributions recipient BNs: 8183 buyers, 1075 vendors in file; filled {'buyer_bn': 5558, 'buyer_legal_name': 2563, 'vendor_bn9': 3893, 'buyer_bn_conflict_noted': 92}
[  451s +   2s  5.3G] vendor legal name, last links of the chain: {"the vendor's own name carries its legal form": 3883, "the vendor's own terms, read by hand": 25614}
[  453s +   2s  5.3G] vendors that are organisations of this table (same name, same province): facts carried from their own row: {'vendor_phone': 4268, 'vendor_website': 4838, 'vendor_legal_name': 661, 'vendor_bn9': 8}
[  469s +  16s  5.4G] buyers' PO / contract open data joined: {'pairs': 5, 'po_filled': 4, 'contract_filled': 1} | records read: 330978 | kept (a row's own buyer-vendor pair): 143
[  484s +  15s  5.8G] back-references: {'dataset rows with lead relationships': 151169, 'lead rows with dataset history': 62}
[  497s +  13s  5.5G] sensitivity tags: {'corrections / detention': 37, 'health: mental health / addiction / sexual health': 458, 'intelligence / security / defence': 25, 'police service / police board': 102, 'courts / tribunals / legal aid': 87, 'child / youth protection': 29, 'police oversight body': 5, 'shelter / crisis / sexual-assault service': 95, 'coroner / medical examiner': 1}
[  506s +   9s  5.5G] site readers, second pass (websites found late): {'buyer_logo': 595, 'vendor_phone': 5386, 'vendor_logo': 48173, 'vendor_emails': 1173, 'vendor_address': 834, 'buyer_address': 5, 'buyer_phone': 46}
[  506s +   0s  5.5G] listings on a site that is not the Canada-located vendor's own (-> tier E): {'kept — the site prints an address in Canada': 5950, "kept — Wikidata: the site's organisation has its headquarters in Canada": 1484, 'kept — no evidence about whose site it is': 1493, "the site's own address is outside Canada": 177, 'from tier D': 814, "Wikidata: the site's organisation has its headquarters outside Canada": 493, "kept — the listing is in the site's Canadian section (/ca/, /en-ca/, ca.…)": 48, 'Canadian arm of a group, site not shown to be its own': 31, "kept although the site reader's address is abroad (Wikidata: headquarters in Canada)": 39, "the vendor's published terms: its Canadian entity does not contract with customers of this buyer's country": 113, "kept — address abroad on the site, but a corporation of the site's name is registered in Canada": 11}
[  509s +   3s  5.5G] same-vendor carry-over (BN9, identity facts and address from the vendor's other rows): {'address': 138, 'bn9': 99626, 'legal_name': 99622, 'trading_name': 99612, 'gst_hst_derived': 99626, 'phone': 14, 'emails': 11, 'logo_url': 15, 'registry_id': 99606, 'registry_url': 99606, 'registered_address': 99606, 'legal_form': 99606, 'registry_status': 99606, 'registry_match_level': 99608, 'incorporation_date': 99606, 'neq': 1}
[  640s + 130s  5.4G] rows written: 100000 of 253908
[  768s + 129s  5.3G] rows written: 200000 of 253908
[  838s +  70s  5.3G] narrative columns: {'mailbox meta found': 246189, 'contract_description_from_title': 177470, 'contract_title_from_description': 142, 'invoice_reference_hint_po_rule': 1134, 'records_with_this_vendor_lead': 230503, 'mailbox meta missing': 1359}
[  838s +   0s  5.3G] downstream pack: {'tax_derived_foreign': 26837, 'pay_on_sight_yes': 2355, 'ap_payable_today': 2234, 'ship_ready_yes': 1023, 'buyer_trade_name_as_published': 184631, 'tax_derived': 160787, 'registry_note': 222, 'prompt_payment_default': 816, 'pay_on_sight_no': 165011, 'buyer_type_from_name': 35533, 'sensitivity_extra': 201, 'buyer_address_from_own_page': 3130, 'registry_warning': 1448, 'invoice_currency_derived': 232424, 'pay_on_sight_routed': 80182, 'currency_default': 2}
[  838s +   0s  5.3G] rows 253908
[  838s +   0s  5.3G] [('GOLD', 625), ('A0', 519), ('A1', 712), ('A2', 92), ('A3', 223), ('A4', 8), ('B0', 623), ('B1', 1008), ('B2', 131), ('B3', 186), ('B4', 11), ('C0', 1004), ('C1', 245), ('C2', 18), ('C3', 26), ('C4', 26), ('D0', 569), ('D1', 26116), ('D2', 174), ('D3', 649), ('D4', 309), ('E0', 250), ('E1', 4834), ('E2', 95), ('E3', 123), ('E4', 103), ('F0', 1), ('F1', 3), ('F2', 1), ('F3', 2), ('F4', 1), ('GOLD-M', 126), ('GOLD-T', 370), ('I0', 744), ('I1', 17626), ('I2', 60), ('I3', 239), ('I4', 103), ('L0', 216), ('L1', 314), ('L2', 33), ('L3', 20), ('L4', 70), ('M0', 220), ('M1', 12859), ('M2', 56), ('M3', 178), ('M4', 1), ('R0', 178), ('R1', 98164), ('R2', 96), ('R3', 989), ('R4', 177), ('T0', 2036), ('T1', 79134), ('T2', 169), ('T3', 1026), ('T4', 17)]
[  838s +   0s  5.3G] with any email: 247548 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            625
P01T_active_service_seen_on_buyer_site_invoicing_AP_email    370
P02_active_relationship_finance_accounting_email           470
P03_active_relationship_purchasing_email                   257
P04_active_relationship_general_email (2 part files)      3821
P05_likely_active_awarded_12_36_months_any_email           424
P06_client_listing_invoicing_AP_email                      298
P06T_active_service_seen_on_buyer_site_other_email (22 part files)  67038
P07_client_listing_finance_or_purchasing_email             801
P08_client_listing_general_email (8 part files)          25648
P09_older_contract_or_payment_any_email                    295
P10_linked_from_vendor_site_any_email                     2685
P10R_ca_domain_registration_contract_own_email (37 part files)  98583
P11_any_relationship_email_not_yet_confirmed (5 part files)  14978
P12_weaker_relationship_within_5_years_own_email             7
P13_inferred_relationship_no_record_own_email (7 part files)  18028
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email    126
P06M_member_or_regulated_payer_of_canadian_body_other_email (5 part files)  13001
Z_no_email_yet_not_delivered (2 part files)               6453
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 27994358
package files: compressed (.csv.gz); packages written straight from the table (already in order): 17 of 19; sorted from a working copy: P11 (14978 rows); sorted from a working copy: Z (6453 rows)

# coverage vs the downstream targets (COVERAGE_VS_TARGETS.md)
benchmarks met 94 / 446 (21.1%); near 54; written out/ranked/COVERAGE_VS_TARGETS.md
  gap buyer_ap_cycle_published           P10R       0.0% ->  20%  rows needed 19691
  gap ap_system_hint                     P10R       0.2% ->  20%  rows needed 19517
  gap buyer_tax_exempt_status            P10R       0.0% ->  15%  rows needed 14758
  gap buyer_esignature_preference        P10R       0.0% ->  15%  rows needed 14741
  gap vendor_registered_address          P08       13.2% ->  70%  rows needed 14580
  gap buyer_payment_method_preference    P10R       0.6% ->  15%  rows needed 14157
  gap buyer_ap_cycle_published           P06T       0.0% ->  20%  rows needed 13385
  gap ap_system_hint                     P06T       0.7% ->  20%  rows needed 12947
  gap vendor_phone                       P11        4.8% ->  75%  rows needed 10511
  gap vendor_emails                      P11        3.5% ->  70%  rows needed 9961
  gap buyer_esignature_preference        P06T       0.2% ->  15%  rows needed 9913
  gap buyer_tax_exempt_status            P06T       0.3% ->  15%  rows needed 9869
  gap buyer_phone                        P08       56.8% ->  95%  rows needed 9791
  gap buyer_payment_method_preference    P06T       0.7% ->  15%  rows needed 9619
  gap vendor_bn9                         P08       14.5% ->  50%  rows needed 9106
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
