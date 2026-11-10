# Ranked buyers — 2026-11-10T22:39Z

```
[   14s +  14s  1.6G] mailboxes taken from the verification log (better than org_mailboxes' single pick): 776 | referee mailbox rows whose last label is not a top-level domain: {'left out': 15, 'cut back to the address the page prints': 62}
[   23s +   9s  0.7G] vendor table: registry matches not used because the legal form differs (partnership vs corporation): 55 | 'websites' that are a web host's own site (dropped with their mailboxes): 5 | websites not used for a look-up by domain (unverified, name does not fit): 0 | look-ups by domain: 8051
[   23s +   0s  0.7G] team vendor contacts (referee-verified): 8782 vendors; 172 with a billing / AR mailbox
[  153s + 131s  2.1G] same-pair fill (facts from another record of the same buyer-vendor pair): {'solicitation_or_tender_number': 11, 'number_of_bids': 10, 'award_or_notice_id': 2, 'buyer_vendor_id': 2, 'commodity_codes': 9, 'end_date_inferred': 120, 'contract_value': 7, 'procurement_method': 3, 'po_number_as_published': 3, 'buyer_org_codes': 1, 'start_from_signed': 497, 'end_date': 3, 'contract_description': 2, 'contract_or_agreement_number': 2, 'contract_title': 1}
[  153s +   0s  2.1G] contract records whose vendor's registry match pairs a partnership with a corporation (registry cells not used): 2244
[  159s +   6s  2.8G] tenant leads from the shards: 15232
[  159s +   0s  2.8G] leads: 414510 (328288 from the cloud row factory; 63 websites from the lead site finder)
[  182s +  22s  2.9G] registry leads (.ca domains carrying a confirmed mailbox of their own organisation): 145307
[  203s +  22s  3.2G] lead rows: facts from the buyer's own pages / the vendor's link label: {'buyer_address_from_own_page': 116183, 'buyer_name_from_own_home_page': 117138, 'facts of another host of the domain not taken': 285, 'vendor_address_cut_out_of_its_quote': 26252, 'buyer_legal_name_from_register': 7578, 'buyer_address_from_member_directory': 6030, 'buyer_name_from_vendor_link_label': 2914} | sites named again from their stored home-page title: 1144
[  203s +   0s  3.2G] client-page links judged (cloud row factory): {'client listing: label names the site': 3782, 'link only, and the site has a .ca registration: the registration takes the row': 1734, "not shown to be a client: the link's label does not name the linked site": 1408, "client listing: 'visit website' on a client page": 299, 'client listing: portfolio page': 227, 'client listing: page address names the site': 191, 'not shown to be a client: a page for clients (forms, resources, login), not a list of them': 188, "not shown to be a client: an organisation's 'our work' programme page": 158, "not shown to be a client: sister site of the page's owner": 97, 'not shown to be a client: article: the client word sits in a slug of 4 words': 47, 'not shown to be a client: dated article': 21, 'not shown to be a client: article: the client word sits in a slug of 5 words': 15, 'not shown to be a client: article: the client word sits in a slug of 6 words': 1}
[  208s +   5s  3.2G] leads with a borrowed mailbox: 106873 | rows upgraded by a newer dated record: 43 | rows upgraded to an active service seen on the buyer's site: 402
[  218s +  10s  3.3G] P12 organisations: 93 added: 9 {'no own confirmed mailbox': 66, 'same organisation already in a row': 18} | P13 added: 18531 | P13 skipped: {"mailbox not the organisation's own": 2159, 'bad mailbox': 188, 'not located in Canada (no honest inference)': 13619, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 66997, '… of which by the NAME alone (its own mailbox and domain are in no row)': 127}
[  218s +   0s  3.3G] lead rows that took the organisation's own key (registry facts attach): {'rows': 44985, 'buyer_address': 4962, 'buyer_name': 3391}
[  237s +  19s  3.3G] extras from the lanes' result rows: {'invoice_mailing_address': 2308, 'invoicing_requirements': 2115, 'ap_phone': 2404, 'invoice_portal_url': 73, 'ap_contact_name': 258}
[  246s +   9s  3.4G] words too common to prove a name (in more than 1 in 2,000 of the 171993 names of organisations whose site was read): 462; names printed on 3+ sites: 1406
[  278s +  32s  3.4G] org_extras: 173134 organisations read; filled {'vendor_logo': 71128, 'vendor_phone_v2': 45650, 'po_required': 253, 'vendor_trading_name_jsonld': 7157, 'buyer_legal_name': 48928, 'buyer_phone_v2': 77525, 'buyer_payment_method_preference_mention_rejected': 18044, 'buyer_logo': 139988, 'payment_terms': 839, 'buyer_tax_exempt_status_mention_rejected': 298, 'buyer_legal_name_v2_printed_on_many_sites': 8410, 'buyer_legal_name_v2_legal_name_stated': 12418, "vendor site is a foreign organisation's: its legal / trading name not taken for the Canada-located vendor": 1381, 'buyer_bn': 3005, 'buyer_legal_name_v2_rejected_no_overlap': 40855, 'buyer_legal_name_v2_jsonld_name': 5364, 'buyer_legal_name_v2_jsonld_legal_name': 5563, 'ap_system_hint_links': 427, 'buyer_legal_name_government_template_credit': 40, 'buyer_payment_method_preference_mention': 801, 'vendor_legal_name': 10865, 'vendor_neq': 128, 'buyer_esignature_preference_mention_rejected': 520, 'vendor_legal_name_v2': 6446, 'buyer_address_v2': 6060, 'p13_name_from_legal_name': 8975, 'buyer_esignature_preference_mention': 52, 'buyer_legal_name_v2_jsonld_legal_name_own_site_node': 385, 'invoice_portal_links': 58, 'buyer_legal_name_v2_jsonld_name_own_site_node': 382, 'vendor_bn': 642, 'buyer_tax_exempt_status_mention': 65, 'vendor_bn_jsonld': 54, 'buyer_bn_jsonld': 137, 'buyer_legal_name_kept_from_the_trademarks_register': 738, 'vendor_address_v2': 296, 'vendor_address_v2_outside_canada_not_taken': 114, 'buyer_ap_cycle_published_mention': 36, 'vendor_legal_name_v2_site_says': 115, 'buyer_legal_name_v2_stated_as_operator': 118, 'vendor_qst': 17, 'buyer_legal_name_v2_doing_business_as': 16, 'buyer_ap_cycle_published_mention_rejected': 33, 'buyer_legal_name_franchisor_copyright_not_taken': 7, 'p13_name_from_domain': 1}
[  278s +   0s  3.4G] regional mailboxes of multinationals removed from other-country entities: 47
[  278s +   0s  3.4G] mx_check: 69559 domains known; 185 mailboxes on domains with no mail server removed; 785 webmail (freemail) addresses removed
[  281s +   3s  3.6G] dmarc/spf: 243423 domains known; rows {'enforced': 44986, 'exposed': 185260}
[  281s +   0s  3.6G] same organisation under another key folded into the row that holds its mailbox: 52
[  284s +   3s  3.7G] second mailbox of the same organisation (same site and mail domain, same name family) folded: 6
[  288s +   4s  3.8G] org_contacts: 162071 organisations read; filled {'vendor_phone': 59221, 'vendor_emails': 37178, 'buyer_phone': 88404, 'vendor site prints an address outside Canada: address and telephone not taken': 1129, 'buyer_address': 16435, 'vendor_address': 2009}
[  288s +   0s  3.8G] site-reader records read on another host of the row's domain (look-ups): {'org_contacts: not taken': 2573, 'org_extras: not taken': 3028, 'org_contacts: taken, read on another host for the same organisation (same name)': 1896, "org_extras: taken, the row's host is the member directory of the body whose own site was read": 1642, "org_contacts: taken, the row's host is the member directory of the body whose own site was read": 4677, 'org_extras: taken, read on another host for the same organisation (same name)': 947}
[  295s +   7s  4.3G] ap_terms (evidence pages re-read): 82907 keys read, 109207 pages used across rows; filled {'payment_terms': 3558, 'po_required': 1912, 'payment_method': 702, 'ap_cycle': 108, 'tax_exempt': 1015, 'portal': 1974, 'format': 743, 'context': 45803, 'esignature': 609, 'ap_system_portal': 1709, 'ap_phone': 1111, 'buyer_bn': 55, 'ap_contact_name': 833, 'address': 554, 'mailbox_gone': 335, 'ap_system': 450, 'setup_url': 323, 'buyer_phone_from_page': 9703, 'buyer_address_from_page': 646}
[  297s +   2s  4.3G] peppol: 77 Canadian participants; matched buyers 5, vendors 38
[  297s +   0s  4.3G] directories: 2338 entries reachable by their own site; 112 sites given by entries of different names, left out
[  299s +   2s  4.3G] municipal / organisation directories: {'matched': 1745, 'legal_name': 798, 'phone': 323, 'address': 46, 'matched_by_place_name': 11, 'website': 18}
[  299s +   0s  4.3G] charity buyers: {'matched': 7243, 'bn': 5987, 'legal_name': 4241, 'address': 298, 'website': 25}
[  300s +   1s  4.3G] wikidata: {'vendors': 1160, 'buyers': 5229, 'buyer_legal_name': 2454, 'buyer_address': 635, 'buyer_phone': 90, 'buyer_website': 109, 'vendor_legal_name': 44, 'vendor_address': 415, 'vendor_website': 239, 'vendor_neq': 7}
[  301s +   0s  4.3G] crown-corporation BNs applied to inferred-vendor rows: 16877
[  301s +   0s  4.3G] vendor websites confirmed from search proposals: 502 applied: 16103
[  301s +   0s  4.3G] inferred vendors' published phone / address applied: {'phone': 13571}
[  301s +   0s  4.4G] registry bulk rows added (no API row for the key): 22305 | registry rows left out, the registered name is only legal-form and place words: 0
[  303s +   1s  4.4G] Canada's Business Registries + registry open data: 3706 vendors, 28246 buyers found; filled {'buyer_bn': 9354, 'buyer_legal_name': 14768, 'vendor_registered_address': 15537, 'vendor_bn9': 20969, 'vendor_legal_name': 15468, 'vendor_registry_status': 15470, 'vendor_incorporation_date': 15756, 'vendor_legal_form': 15477, 'vendor_neq': 4405, 'vendor_trading_name': 266, 'buyer_address': 2167, 'vendor_skipped_legal_form': 1, 'buyer record looked up under a name the row no longer carries, not taken': 6, 'vendor_bn9_other_registry': 4, 'buyer record of another name than the legal person the site itself states, not taken': 19}
[  303s +   0s  4.4G] award facts from the buyers' own award pages: 237 pairs with a page; filled {'contract_value': 39, 'end_date': 17, 'start_date': 9, 'contract_or_agreement_number': 3, 'solicitation_or_tender_number': 6, 'term': 2, 'po_number_as_published': 1, 'number_of_bids': 1}
[  303s +   1s  4.4G] grants & contributions recipient BNs: 3202 buyers, 454 vendors in file; filled {'buyer_bn': 1612, 'buyer_bn_conflict_noted': 86, 'vendor_bn9': 780, 'buyer_legal_name': 336}
[  314s +  11s  4.5G] buyers' PO / contract open data joined: {'pairs': 5, 'po_filled': 4, 'contract_filled': 1} | records read: 330978 | kept (a row's own buyer-vendor pair): 143
[  325s +  11s  4.8G] back-references: {'dataset rows with lead relationships': 144369, 'lead rows with dataset history': 49}
[  333s +   8s  4.6G] sensitivity tags: {'corrections / detention': 36, 'health: mental health / addiction / sexual health': 419, 'intelligence / security / defence': 25, 'police service / police board': 94, 'courts / tribunals / legal aid': 74, 'child / youth protection': 26, 'police oversight body': 5, 'shelter / crisis / sexual-assault service': 83, 'coroner / medical examiner': 1}
[  339s +   6s  4.6G] site readers, second pass (websites found late): {'buyer_logo': 588, 'vendor_emails': 572, 'vendor_phone': 754, 'vendor_logo': 31601, 'vendor_address': 237, 'buyer_address': 6, 'buyer_phone': 42}
[  339s +   0s  4.6G] listings on a site that is not the Canada-located vendor's own (-> tier E): {'kept — the site prints an address in Canada': 3540, "kept — Wikidata: the site's organisation has its headquarters in Canada": 1416, 'kept — no evidence about whose site it is': 1628, "the site's own address is outside Canada": 107, 'from tier D': 768, "Wikidata: the site's organisation has its headquarters outside Canada": 517, "kept — the listing is in the site's Canadian section (/ca/, /en-ca/, ca.…)": 49, 'Canadian arm of a group, site not shown to be its own': 30, "kept although the site reader's address is abroad (Wikidata: headquarters in Canada)": 39, "the vendor's published terms: its Canadian entity does not contract with customers of this buyer's country": 114, "kept — address abroad on the site, but a corporation of the site's name is registered in Canada": 11}
[  342s +   2s  4.6G] same-vendor carry-over (BN9, identity facts and address from the vendor's other rows): {'address': 129, 'bn9': 99561, 'legal_name': 99557, 'trading_name': 99558, 'phone': 5, 'gst_hst_derived': 99561, 'registry_id': 99554, 'registry_url': 99554, 'registered_address': 99554, 'legal_form': 99554, 'registry_status': 99554, 'registry_match_level': 99555, 'incorporation_date': 99554, 'logo_url': 4, 'neq': 1}
[  428s +  87s  4.5G] rows written: 100000 of 233316
[  515s +  86s  4.4G] rows written: 200000 of 233316
[  542s +  28s  4.2G] narrative columns: {'mailbox meta found': 226176, 'contract_description_from_title': 167730, 'contract_title_from_description': 142, 'invoice_reference_hint_po_rule': 1160, 'records_with_this_vendor_lead': 210143, 'mailbox meta missing': 1410}
[  542s +   0s  4.2G] downstream pack: {'tax_derived_foreign': 19190, 'pay_on_sight_yes': 2232, 'ap_payable_today': 1905, 'ship_ready_yes': 958, 'buyer_trade_name_as_published': 166668, 'tax_derived': 149028, 'registry_note': 222, 'prompt_payment_default': 735, 'pay_on_sight_no': 152469, 'buyer_type_from_name': 27702, 'sensitivity_extra': 188, 'buyer_address_from_own_page': 4578, 'registry_warning': 1346, 'invoice_currency_derived': 213217, 'pay_on_sight_routed': 72885, 'currency_default': 2}
[  542s +   0s  4.2G] rows 233316
[  542s +   0s  4.2G] [('GOLD', 626), ('A0', 519), ('A1', 712), ('A2', 92), ('A3', 223), ('A4', 8), ('B0', 623), ('B1', 1007), ('B2', 131), ('B3', 186), ('B4', 11), ('C0', 1003), ('C1', 252), ('C2', 19), ('C3', 26), ('C4', 26), ('D0', 548), ('D1', 23827), ('D2', 169), ('D3', 603), ('D4', 301), ('E0', 243), ('E1', 4436), ('E2', 95), ('E3', 118), ('E4', 100), ('F0', 1), ('F1', 4), ('F2', 1), ('F3', 2), ('F4', 1), ('GOLD-M', 97), ('GOLD-T', 332), ('I0', 709), ('I1', 17420), ('I2', 60), ('I3', 237), ('I4', 105), ('L0', 217), ('L1', 317), ('L2', 33), ('L3', 19), ('L4', 71), ('M0', 80), ('M1', 9263), ('M2', 30), ('M3', 133), ('M4', 1), ('R0', 180), ('R1', 98136), ('R2', 100), ('R3', 962), ('R4', 174), ('T0', 1607), ('T1', 66043), ('T2', 149), ('T3', 916), ('T4', 12)]
[  542s +   0s  4.2G] with any email: 227586 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            626
P01T_active_service_seen_on_buyer_site_invoicing_AP_email    332
P02_active_relationship_finance_accounting_email           465
P03_active_relationship_purchasing_email                   256
P04_active_relationship_general_email (2 part files)      3409
P05_likely_active_awarded_12_36_months_any_email           427
P06_client_listing_invoicing_AP_email                      290
P06T_active_service_seen_on_buyer_site_other_email (19 part files)  59340
P07_client_listing_finance_or_purchasing_email             749
P08_client_listing_general_email (7 part files)          23364
P09_older_contract_or_payment_any_email                    303
P10_linked_from_vendor_site_any_email                     2699
P10R_ca_domain_registration_contract_own_email (37 part files)  98530
P11_any_relationship_email_not_yet_confirmed (3 part files)   9442
P12_weaker_relationship_within_5_years_own_email             8
P13_inferred_relationship_no_record_own_email (6 part files)  17822
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email     97
P06M_member_or_regulated_payer_of_canadian_body_other_email (4 part files)   9350
Z_no_email_yet_not_delivered (2 part files)               5807
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 26038993
package files: compressed (.csv.gz); packages written straight from the table (already in order): 17 of 19; sorted from a working copy: P11 (9442 rows); sorted from a working copy: Z (5807 rows)

# coverage vs the downstream targets (COVERAGE_VS_TARGETS.md)
benchmarks met 93 / 446 (20.9%); near 56; written out/ranked/COVERAGE_VS_TARGETS.md
  gap buyer_ap_cycle_published           P10R       0.0% ->  20%  rows needed 19689
  gap ap_system_hint                     P10R       0.2% ->  20%  rows needed 19513
  gap buyer_tax_exempt_status            P10R       0.0% ->  15%  rows needed 14760
  gap buyer_esignature_preference        P10R       0.0% ->  15%  rows needed 14748
  gap buyer_payment_method_preference    P10R       0.4% ->  15%  rows needed 14386
  gap vendor_registered_address          P08       14.1% ->  70%  rows needed 13071
  gap buyer_ap_cycle_published           P06T       0.0% ->  20%  rows needed 11848
  gap ap_system_hint                     P06T       0.7% ->  20%  rows needed 11434
  gap vendor_bn9                         P08       10.9% ->  50%  rows needed 9129
  gap buyer_esignature_preference        P06T       0.2% ->  15%  rows needed 8764
  gap buyer_tax_exempt_status            P06T       0.3% ->  15%  rows needed 8728
  gap buyer_payment_method_preference    P06T       0.4% ->  15%  rows needed 8640
  gap buyer_legal_name_as_published      P08       38.5% ->  75%  rows needed 8519
  gap buyer_phone                        P08       58.8% ->  95%  rows needed 8453
  gap buyer_phone                        P13       47.6% ->  95%  rows needed 8441
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
