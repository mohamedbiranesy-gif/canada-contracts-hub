# Ranked buyers — 2026-11-11T08:26Z

```
[   20s +  20s  1.7G] mailboxes taken from the verification log (better than org_mailboxes' single pick): 795 | referee mailbox rows whose last label is not a top-level domain: {'left out': 15, 'cut back to the address the page prints': 62}
[   37s +  16s  0.8G] vendor table: registry matches not used because the legal form differs (partnership vs corporation): 55 | 'websites' that are a web host's own site (dropped with their mailboxes): 6 | websites not used for a look-up by domain (unverified, name does not fit): 0 | look-ups by domain: 8050
[   37s +   0s  0.8G] team vendor contacts (referee-verified): 8782 vendors; 172 with a billing / AR mailbox
[  287s + 251s  2.1G] same-pair fill (facts from another record of the same buyer-vendor pair): {'solicitation_or_tender_number': 11, 'number_of_bids': 10, 'award_or_notice_id': 2, 'buyer_vendor_id': 2, 'commodity_codes': 9, 'end_date_inferred': 120, 'contract_value': 7, 'procurement_method': 3, 'po_number_as_published': 3, 'buyer_org_codes': 1, 'start_from_signed': 497, 'end_date': 3, 'contract_description': 2, 'contract_or_agreement_number': 2, 'contract_title': 1}
[  287s +   0s  2.1G] contract records whose vendor's registry match pairs a partnership with a corporation (registry cells not used): 2244
[  301s +  13s  3.3G] tenant leads from the shards: 23323
[  301s +   0s  3.3G] leads: 542678 (448365 from the cloud row factory; 64 websites from the lead site finder)
[  345s +  44s  3.5G] registry leads (.ca domains carrying a confirmed mailbox of their own organisation): 150733
[  345s +   0s  3.5G] organisations' second domain names (the name on file answers at their site under another domain): 0 {}
[  391s +  45s  3.8G] lead rows: facts from the buyer's own pages / the vendor's link label: {'buyer_address_from_own_page': 133961, 'buyer_name_from_own_home_page': 124741, 'facts of another host of the domain not taken': 299, 'vendor_address_cut_out_of_its_quote': 34276, 'buyer_legal_name_from_register': 10839, 'buyer_address_from_member_directory': 6314, 'buyer_name_from_vendor_link_label': 2809} | sites named again from their stored home-page title: 1144
[  391s +   0s  3.8G] client-page links judged (cloud row factory): {'client listing: label names the site': 4640, "not shown to be a client: the link's label does not name the linked site": 1744, 'link only, and the site has a .ca registration: the registration takes the row': 1721, "client listing: 'visit website' on a client page": 448, 'client listing: portfolio page': 314, 'client listing: page address names the site': 228, 'not shown to be a client: a page for clients (forms, resources, login), not a list of them': 202, "not shown to be a client: an organisation's 'our work' programme page": 187, "not shown to be a client: sister site of the page's owner": 102, 'not shown to be a client: article: the client word sits in a slug of 4 words': 65, 'not shown to be a client: dated article': 19, 'not shown to be a client: article: the client word sits in a slug of 5 words': 14, 'not shown to be a client: article: the client word sits in a slug of 6 words': 1}
[  399s +   8s  3.8G] leads with a borrowed mailbox: 117713 | rows upgraded by a newer dated record: 43 | rows upgraded to an active service seen on the buyer's site: 500
[  417s +  19s  3.9G] P12 organisations: 90 added: 8 {'no own confirmed mailbox': 64, 'same organisation already in a row': 18} | P13 added: 18772 | P13 skipped: {"mailbox not the organisation's own": 2278, 'bad mailbox': 198, 'not located in Canada (no honest inference)': 15454, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 73450, '… of which by the NAME alone (its own mailbox and domain are in no row)': 128}
[  417s +   0s  3.9G] lead rows that took the organisation's own key (registry facts attach): {'rows': 45149, 'buyer_address': 4954, 'buyer_name': 3608}
[  454s +  36s  3.9G] extras from the lanes' result rows: {'invoice_mailing_address': 2322, 'invoicing_requirements': 2124, 'ap_phone': 2418, 'invoice_portal_url': 73, 'ap_contact_name': 278}
[  474s +  20s  4.0G] words too common to prove a name (in more than 1 in 2,000 of the 227550 names of organisations whose site was read): 535; names printed on 3+ sites: 1616
[  551s +  77s  4.0G] org_extras: 230582 organisations read; filled {'vendor_logo': 82784, 'vendor_phone_v2': 59830, 'po_required': 269, 'vendor_trading_name_jsonld': 14149, 'buyer_legal_name': 82594, 'buyer_phone_v2': 106657, 'buyer_payment_method_preference_mention_rejected': 18168, 'buyer_logo': 192377, 'payment_terms': 995, 'buyer_tax_exempt_status_mention_rejected': 336, 'buyer_legal_name_v3_spelled_by_the_domain': 16644, 'buyer_legal_name_v2_legal_name_stated': 17726, "vendor site is a foreign organisation's: its legal / trading name not taken for the Canada-located vendor": 1330, 'buyer_bn': 3443, 'buyer_legal_name_v2_rejected_no_overlap': 48603, 'buyer_legal_name_v2_jsonld_name': 5321, 'buyer_legal_name_v2_printed_on_many_sites': 7196, 'buyer_legal_name_v2_jsonld_legal_name': 6331, 'ap_system_hint_links': 508, 'buyer_legal_name_government_template_credit': 40, 'buyer_payment_method_preference_mention': 1397, 'vendor_legal_name': 14543, 'vendor_legal_name_v3_spelled_by_the_domain': 4311, 'vendor_neq': 145, 'buyer_esignature_preference_mention_rejected': 539, 'vendor_legal_name_v2': 10927, 'invoice_portal_links': 77, 'buyer_ap_cycle_published_mention': 57, 'buyer_address_v2': 7399, 'buyer_legal_name_v3_stated_as_operator': 1557, 'p13_name_from_legal_name': 13420, "vendor named by its own site's name instead of its domain": 17072, 'buyer_esignature_preference_mention': 83, 'buyer_legal_name_v3_legal_person_behind_the_site_name': 1547, 'buyer_legal_name_v2_jsonld_name_own_site_node': 492, 'vendor_legal_name_v3_legal_person_behind_the_site_name': 1069, 'vendor_bn': 771, 'vendor_legal_name_v2_site_says': 858, 'buyer_tax_exempt_status_mention': 126, 'vendor_bn_jsonld': 72, 'buyer_bn_jsonld': 167, 'buyer_legal_name_v2_jsonld_legal_name_own_site_node': 387, 'buyer_legal_name_kept_from_the_trademarks_register': 1066, 'vendor_address_v2': 304, 'vendor_address_v2_outside_canada_not_taken': 115, 'vendor_legal_name_v3_stated_as_operator': 70, 'buyer_legal_name_v2_stated_as_operator': 52, 'vendor_qst': 19, 'buyer_ap_cycle_published_mention_rejected': 32, 'buyer_legal_name_franchisor_copyright_not_taken': 11, 'buyer_legal_name_v2_doing_business_as': 9, 'p13_name_from_domain': 1}
[  552s +   0s  4.0G] regional mailboxes of multinationals removed from other-country entities: 55
[  552s +   1s  4.0G] mx_check: 69559 domains known; 185 mailboxes on domains with no mail server removed; 858 webmail (freemail) addresses removed
[  557s +   5s  4.3G] dmarc/spf: 263367 domains known; rows {'enforced': 49239, 'exposed': 201520}
[  557s +   0s  4.4G] same organisation under another key folded into the row that holds its mailbox: 52
[  562s +   5s  4.4G] second mailbox of the same organisation (same site and mail domain, same name family) folded: 6
[  569s +   7s  4.6G] org_contacts: 224502 organisations read; filled {'vendor_phone': 67556, 'vendor_emails': 41754, 'buyer_phone': 122772, 'vendor site prints an address outside Canada: address and telephone not taken': 1089, 'buyer_address': 18872, 'vendor_address': 1973}
[  569s +   0s  4.6G] site-reader records read on another host of the row's domain (look-ups): {'org_extras: not taken': 798, 'org_contacts: not taken': 1271, 'org_contacts: taken, read on another host for the same organisation (same name)': 308, 'org_extras: taken, read on another host for the same organisation (same name)': 60, "org_contacts: taken, the row's host is the member directory of the body whose own site was read": 582, "org_extras: taken, the row's host is the member directory of the body whose own site was read": 201}
[  580s +  11s  5.1G] ap_terms (evidence pages re-read): 82907 keys read, 108123 pages used across rows; filled {'payment_terms': 3479, 'po_required': 1869, 'payment_method': 695, 'ap_cycle': 107, 'tax_exempt': 998, 'portal': 1956, 'format': 736, 'context': 45784, 'esignature': 602, 'ap_system_portal': 1697, 'ap_phone': 1103, 'buyer_bn': 52, 'ap_contact_name': 828, 'address': 551, 'mailbox_gone': 336, 'ap_system': 437, 'setup_url': 318, 'buyer_phone_from_page': 9483, 'buyer_address_from_page': 612}
[  583s +   3s  5.1G] peppol: 77 Canadian participants; matched buyers 7, vendors 39
[  583s +   0s  5.1G] directories: 2338 entries reachable by their own site; 112 sites given by entries of different names, left out
[  586s +   3s  5.1G] municipal / organisation directories: {'matched': 1753, 'legal_name': 780, 'phone': 322, 'address': 47, 'matched_by_place_name': 12, 'website': 19}
[  586s +   0s  5.1G] charity buyers: {'matched': 9543, 'bn': 7816, 'legal_name': 6403, 'address': 613, 'website': 32}
[  588s +   1s  5.2G] charity registration numbers found in the CRA list: {'matched': 905, 'legal_name': 556, 'address': 75, 'name_from_the_register': 87, 'holder is a foundation / trust under another name: reported only': 35} | list: 83761
[  589s +   2s  5.2G] wikidata: {'vendors': 1363, 'buyers': 5213, 'buyer_legal_name': 2172, 'buyer_phone': 90, 'buyer_address': 615, 'buyer_website': 107, 'vendor_legal_name': 43, 'vendor_address': 571, 'vendor_website': 232, 'vendor_neq': 6}
[  590s +   1s  5.2G] crown-corporation BNs applied to inferred-vendor rows: 17065
[  590s +   1s  5.2G] vendor websites confirmed from search proposals: 502 applied: 645 {"search proposal not taken: a directory / quote page / register, or a host that does not carry the vendor's name": 496, 'vetted vendor: the site of its own terms page': 27564}
[  591s +   0s  5.2G] inferred vendors' published phone / address applied: {'phone': 13805}
[  591s +   1s  5.3G] registry bulk rows added (no API row for the key): 22305 | registry rows left out, the registered name is only legal-form and place words: 0
[  593s +   2s  5.3G] Canada's Business Registries + registry open data: 3706 vendors, 28246 buyers found; filled {'buyer_bn': 8996, 'buyer_legal_name': 13687, 'vendor_registered_address': 19597, 'vendor_bn9': 29462, 'vendor_registry_status': 19535, 'vendor_incorporation_date': 19822, 'vendor_legal_form': 19542, 'vendor_legal_name': 18408, 'vendor_neq': 7614, 'vendor_trading_name': 180, 'buyer_address': 1987, 'vendor_skipped_legal_form': 1, 'buyer record of another name than the legal person the site itself states, not taken': 85, 'buyer record looked up under a name the row no longer carries, not taken': 9, 'vendor_bn9_other_registry': 4}
[  594s +   0s  5.3G] award facts from the buyers' own award pages: 237 pairs with a page; filled {'contract_value': 39, 'end_date': 17, 'start_date': 9, 'contract_or_agreement_number': 3, 'solicitation_or_tender_number': 6, 'term': 2, 'po_number_as_published': 1, 'number_of_bids': 1}
[  596s +   3s  5.4G] legal names read off a page, tidied: {'tidied': 555, 'owner': 70, 'fragment': 45}
[  597s +   1s  5.4G] legal name: the organisation's own name carries its legal form (cells still empty after every register and site statement): 2564
[  598s +   1s  5.4G] legal names from validated certificate subjects (Certificate Transparency): domains on file 199; {'buyer_legal_name': 6, "subject does not carry the organisation's own name: not taken": 10}
[  598s +   0s  5.4G] grants & contributions recipient BNs: 8183 buyers, 1075 vendors in file; filled {'buyer_bn': 5554, 'buyer_legal_name': 2567, 'vendor_bn9': 4024, 'buyer_bn_conflict_noted': 93}
[  601s +   3s  5.4G] vendor legal name, last links of the chain: {"the vendor's own name carries its legal form": 3474, "the vendor's own terms, read by hand": 25614}
[  603s +   2s  5.4G] vendors that are organisations of this table (same name, same province): facts carried from their own row: {'vendor_phone': 4266, 'vendor_website': 4838, 'vendor_legal_name': 667, 'vendor_bn9': 8}
[  623s +  20s  5.5G] buyers' PO / contract open data joined: {'pairs': 5, 'po_filled': 4, 'contract_filled': 1} | records read: 330978 | kept (a row's own buyer-vendor pair): 143
[  640s +  17s  5.8G] back-references: {'dataset rows with lead relationships': 151164, 'lead rows with dataset history': 62}
[  659s +  19s  5.5G] sensitivity tags: {'corrections / detention': 37, 'health: mental health / addiction / sexual health': 458, 'intelligence / security / defence': 25, 'police service / police board': 102, 'courts / tribunals / legal aid': 92, 'child / youth protection': 29, 'police oversight body': 5, 'shelter / crisis / sexual-assault service': 95, 'coroner / medical examiner': 1}
[  670s +  11s  5.5G] site readers, second pass (websites found late): {'buyer_logo': 595, 'vendor_phone': 5392, 'vendor_logo': 48173, 'vendor_emails': 1173, 'vendor_address': 840, 'buyer_address': 5, 'buyer_phone': 46}
[  671s +   1s  5.5G] listings on a site that is not the Canada-located vendor's own (-> tier E): {'kept — the site prints an address in Canada': 6357, "kept — Wikidata: the site's organisation has its headquarters in Canada": 1486, 'kept — no evidence about whose site it is': 1064, "the site's own address is outside Canada": 196, 'from tier D': 834, "Wikidata: the site's organisation has its headquarters outside Canada": 495, "kept — the listing is in the site's Canadian section (/ca/, /en-ca/, ca.…)": 48, 'Canadian arm of a group, site not shown to be its own': 30, "kept although the site reader's address is abroad (Wikidata: headquarters in Canada)": 39, "the vendor's published terms: its Canadian entity does not contract with customers of this buyer's country": 113, "kept — address abroad on the site, but a corporation of the site's name is registered in Canada": 11}
[  674s +   4s  5.5G] same-vendor carry-over (BN9, identity facts and address from the vendor's other rows): {'address': 138, 'bn9': 99626, 'legal_name': 99622, 'trading_name': 99612, 'gst_hst_derived': 99626, 'phone': 14, 'emails': 11, 'logo_url': 15, 'registry_id': 99606, 'registry_url': 99606, 'registered_address': 99606, 'legal_form': 99606, 'registry_status': 99606, 'registry_match_level': 99608, 'incorporation_date': 99606, 'neq': 1}
[  838s + 164s  5.5G] rows written: 100000 of 253908
[  998s + 160s  5.4G] rows written: 200000 of 253908
[ 1087s +  89s  5.4G] narrative columns: {'mailbox meta found': 246189, 'contract_description_from_title': 177470, 'contract_title_from_description': 142, 'invoice_reference_hint_po_rule': 1134, 'records_with_this_vendor_lead': 230503, 'mailbox meta missing': 1359}
[ 1087s +   0s  5.4G] downstream pack: {'tax_derived_foreign': 26837, 'pay_on_sight_yes': 2364, 'ap_payable_today': 2311, 'ship_ready_yes': 1023, 'buyer_trade_name_as_published': 184631, 'tax_derived': 160927, 'registry_note': 222, 'prompt_payment_default': 816, 'pay_on_sight_no': 164464, 'buyer_type_from_name': 41752, 'sensitivity_extra': 202, 'buyer_address_from_own_page': 2899, 'registry_warning': 1448, 'invoice_currency_derived': 232510, 'pay_on_sight_routed': 80720, 'currency_default': 2}
[ 1087s +   0s  5.4G] rows 253908
[ 1087s +   0s  5.4G] [('GOLD', 625), ('A0', 519), ('A1', 712), ('A2', 92), ('A3', 223), ('A4', 8), ('B0', 623), ('B1', 1008), ('B2', 131), ('B3', 186), ('B4', 11), ('C0', 1004), ('C1', 245), ('C2', 18), ('C3', 26), ('C4', 26), ('D0', 569), ('D1', 26098), ('D2', 174), ('D3', 648), ('D4', 308), ('E0', 250), ('E1', 4852), ('E2', 95), ('E3', 124), ('E4', 104), ('F0', 1), ('F1', 3), ('F2', 1), ('F3', 2), ('F4', 1), ('GOLD-M', 126), ('GOLD-T', 370), ('I0', 744), ('I1', 17626), ('I2', 60), ('I3', 239), ('I4', 103), ('L0', 216), ('L1', 314), ('L2', 33), ('L3', 20), ('L4', 70), ('M0', 220), ('M1', 12859), ('M2', 56), ('M3', 178), ('M4', 1), ('R0', 178), ('R1', 98164), ('R2', 96), ('R3', 989), ('R4', 177), ('T0', 2036), ('T1', 79134), ('T2', 169), ('T3', 1026), ('T4', 17)]
[ 1087s +   0s  5.4G] with any email: 247548 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            625
P01T_active_service_seen_on_buyer_site_invoicing_AP_email    370
P02_active_relationship_finance_accounting_email           471
P03_active_relationship_purchasing_email                   257
P04_active_relationship_general_email (2 part files)      3839
P05_likely_active_awarded_12_36_months_any_email           424
P06_client_listing_invoicing_AP_email                      297
P06T_active_service_seen_on_buyer_site_other_email (22 part files)  67038
P07_client_listing_finance_or_purchasing_email             800
P08_client_listing_general_email (8 part files)          25630
P09_older_contract_or_payment_any_email                    295
P10_linked_from_vendor_site_any_email                     2685
P10R_ca_domain_registration_contract_own_email (37 part files)  98583
P11_any_relationship_email_not_yet_confirmed (5 part files)  14979
P12_weaker_relationship_within_5_years_own_email             7
P13_inferred_relationship_no_record_own_email (7 part files)  18028
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email    126
P06M_member_or_regulated_payer_of_canadian_body_other_email (5 part files)  13001
Z_no_email_yet_not_delivered (2 part files)               6453
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 27958626
package files: compressed (.csv.gz); packages written straight from the table (already in order): 17 of 19; sorted from a working copy: P11 (14979 rows); sorted from a working copy: Z (6453 rows)

# coverage vs the downstream targets (COVERAGE_VS_TARGETS.md)
benchmarks met 94 / 446 (21.1%); near 54; written out/ranked/COVERAGE_VS_TARGETS.md
  gap buyer_ap_cycle_published           P10R       0.0% ->  20%  rows needed 19690
  gap ap_system_hint                     P10R       0.2% ->  20%  rows needed 19517
  gap buyer_tax_exempt_status            P10R       0.0% ->  15%  rows needed 14758
  gap buyer_esignature_preference        P10R       0.0% ->  15%  rows needed 14741
  gap vendor_registered_address          P08       13.6% ->  70%  rows needed 14450
  gap buyer_payment_method_preference    P10R       0.6% ->  15%  rows needed 14153
  gap buyer_ap_cycle_published           P06T       0.0% ->  20%  rows needed 13384
  gap ap_system_hint                     P06T       0.7% ->  20%  rows needed 12946
  gap vendor_phone                       P11        4.8% ->  75%  rows needed 10511
  gap vendor_emails                      P11        3.5% ->  70%  rows needed 9961
  gap buyer_esignature_preference        P06T       0.2% ->  15%  rows needed 9913
  gap buyer_tax_exempt_status            P06T       0.3% ->  15%  rows needed 9869
  gap buyer_payment_method_preference    P06T       0.7% ->  15%  rows needed 9615
  gap contract_value                     P11        0.6% ->  60%  rows needed 8903
  gap award_or_notice_id                 P11        0.6% ->  60%  rows needed 8902
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
