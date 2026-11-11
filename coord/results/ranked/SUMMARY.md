# Ranked buyers — 2026-11-11T01:52Z

```
[   16s +  16s  1.6G] mailboxes taken from the verification log (better than org_mailboxes' single pick): 784 | referee mailbox rows whose last label is not a top-level domain: {'left out': 15, 'cut back to the address the page prints': 62}
[   28s +  12s  0.7G] vendor table: registry matches not used because the legal form differs (partnership vs corporation): 55 | 'websites' that are a web host's own site (dropped with their mailboxes): 5 | websites not used for a look-up by domain (unverified, name does not fit): 0 | look-ups by domain: 8051
[   28s +   0s  0.7G] team vendor contacts (referee-verified): 8782 vendors; 172 with a billing / AR mailbox
[  206s + 178s  2.1G] same-pair fill (facts from another record of the same buyer-vendor pair): {'solicitation_or_tender_number': 11, 'number_of_bids': 10, 'award_or_notice_id': 2, 'buyer_vendor_id': 2, 'commodity_codes': 9, 'end_date_inferred': 120, 'contract_value': 7, 'procurement_method': 3, 'po_number_as_published': 3, 'buyer_org_codes': 1, 'start_from_signed': 497, 'end_date': 3, 'contract_description': 2, 'contract_or_agreement_number': 2, 'contract_title': 1}
[  206s +   0s  2.1G] contract records whose vendor's registry match pairs a partnership with a corporation (registry cells not used): 2244
[  214s +   8s  2.8G] tenant leads from the shards: 18213
[  214s +   0s  2.8G] leads: 422522 (333319 from the cloud row factory; 63 websites from the lead site finder)
[  244s +  30s  3.0G] registry leads (.ca domains carrying a confirmed mailbox of their own organisation): 147244
[  272s +  28s  3.3G] lead rows: facts from the buyer's own pages / the vendor's link label: {'buyer_address_from_own_page': 124376, 'buyer_name_from_own_home_page': 122182, 'facts of another host of the domain not taken': 275, 'vendor_address_cut_out_of_its_quote': 29093, 'buyer_legal_name_from_register': 8625, 'buyer_address_from_member_directory': 6302, 'buyer_name_from_vendor_link_label': 3065} | sites named again from their stored home-page title: 1144
[  272s +   0s  3.3G] client-page links judged (cloud row factory): {'client listing: label names the site': 4842, "not shown to be a client: the link's label does not name the linked site": 1789, 'link only, and the site has a .ca registration: the registration takes the row': 1766, "client listing: 'visit website' on a client page": 462, 'client listing: portfolio page': 337, 'client listing: page address names the site': 247, 'not shown to be a client: a page for clients (forms, resources, login), not a list of them': 206, "not shown to be a client: an organisation's 'our work' programme page": 199, "not shown to be a client: sister site of the page's owner": 102, 'not shown to be a client: article: the client word sits in a slug of 4 words': 66, 'not shown to be a client: dated article': 22, 'not shown to be a client: article: the client word sits in a slug of 5 words': 17, 'not shown to be a client: article: the client word sits in a slug of 6 words': 1}
[  278s +   6s  3.3G] leads with a borrowed mailbox: 108640 | rows upgraded by a newer dated record: 43 | rows upgraded to an active service seen on the buyer's site: 402
[  291s +  13s  3.4G] P12 organisations: 92 added: 8 {'no own confirmed mailbox': 66, 'same organisation already in a row': 18} | P13 added: 18767 | P13 skipped: {"mailbox not the organisation's own": 2162, 'bad mailbox': 189, 'not located in Canada (no honest inference)': 13896, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 68213, '… of which by the NAME alone (its own mailbox and domain are in no row)': 131}
[  291s +   0s  3.4G] lead rows that took the organisation's own key (registry facts attach): {'rows': 45000, 'buyer_address': 4883, 'buyer_name': 3336}
[  318s +  27s  3.3G] extras from the lanes' result rows: {'invoice_mailing_address': 2308, 'invoicing_requirements': 2114, 'ap_phone': 2404, 'invoice_portal_url': 73, 'ap_contact_name': 268}
[  329s +  12s  3.4G] words too common to prove a name (in more than 1 in 2,000 of the 171993 names of organisations whose site was read): 462; names printed on 3+ sites: 1406
[  373s +  44s  3.4G] org_extras: 173134 organisations read; filled {'vendor_logo': 72681, 'vendor_phone_v2': 46429, 'po_required': 259, 'vendor_trading_name_jsonld': 7319, 'buyer_legal_name': 48842, 'buyer_phone_v2': 77390, 'buyer_payment_method_preference_mention_rejected': 18045, 'buyer_logo': 140137, 'payment_terms': 904, 'buyer_tax_exempt_status_mention_rejected': 298, 'buyer_legal_name_v2_printed_on_many_sites': 8379, 'buyer_legal_name_v2_legal_name_stated': 12446, "vendor site is a foreign organisation's: its legal / trading name not taken for the Canada-located vendor": 1387, 'buyer_bn': 3006, 'buyer_legal_name_v2_rejected_no_overlap': 40858, 'buyer_legal_name_v2_jsonld_name': 5366, 'buyer_legal_name_v2_jsonld_legal_name': 5573, 'ap_system_hint_links': 427, 'buyer_legal_name_government_template_credit': 40, 'buyer_payment_method_preference_mention': 801, 'vendor_legal_name': 11310, 'vendor_neq': 132, 'buyer_esignature_preference_mention_rejected': 520, 'vendor_legal_name_v2': 6607, 'buyer_address_v2': 5928, 'p13_name_from_legal_name': 8888, 'buyer_esignature_preference_mention': 52, 'buyer_legal_name_v2_jsonld_legal_name_own_site_node': 382, 'invoice_portal_links': 58, 'buyer_legal_name_v2_jsonld_name_own_site_node': 381, 'vendor_bn': 663, 'buyer_tax_exempt_status_mention': 65, 'vendor_bn_jsonld': 54, 'buyer_bn_jsonld': 137, 'buyer_legal_name_kept_from_the_trademarks_register': 899, 'vendor_address_v2': 296, 'vendor_address_v2_outside_canada_not_taken': 114, 'buyer_ap_cycle_published_mention': 36, 'vendor_legal_name_v2_site_says': 117, 'buyer_legal_name_v2_stated_as_operator': 123, 'vendor_qst': 17, 'buyer_legal_name_v2_doing_business_as': 16, 'buyer_ap_cycle_published_mention_rejected': 33, 'buyer_legal_name_franchisor_copyright_not_taken': 7, 'p13_name_from_domain': 1}
[  374s +   0s  3.4G] regional mailboxes of multinationals removed from other-country entities: 50
[  374s +   0s  3.4G] mx_check: 69559 domains known; 185 mailboxes on domains with no mail server removed; 817 webmail (freemail) addresses removed
[  378s +   4s  3.7G] dmarc/spf: 252188 domains known; rows {'enforced': 46880, 'exposed': 192307}
[  378s +   0s  3.7G] same organisation under another key folded into the row that holds its mailbox: 52
[  381s +   3s  3.8G] second mailbox of the same organisation (same site and mail domain, same name family) folded: 6
[  386s +   5s  3.9G] org_contacts: 162071 organisations read; filled {'vendor_phone': 60392, 'vendor_emails': 38289, 'buyer_phone': 88514, 'vendor site prints an address outside Canada: address and telephone not taken': 1136, 'buyer_address': 15758, 'vendor_address': 2004}
[  386s +   0s  3.9G] site-reader records read on another host of the row's domain (look-ups): {'org_contacts: not taken': 2763, 'org_extras: not taken': 3123, 'org_contacts: taken, read on another host for the same organisation (same name)': 1934, "org_extras: taken, the row's host is the member directory of the body whose own site was read": 1637, "org_contacts: taken, the row's host is the member directory of the body whose own site was read": 4681, 'org_extras: taken, read on another host for the same organisation (same name)': 967}
[  396s +  10s  4.4G] ap_terms (evidence pages re-read): 82907 keys read, 109011 pages used across rows; filled {'payment_terms': 3542, 'po_required': 1907, 'payment_method': 700, 'ap_cycle': 108, 'tax_exempt': 1014, 'portal': 1973, 'format': 742, 'context': 45787, 'esignature': 607, 'ap_system_portal': 1708, 'ap_phone': 1110, 'buyer_bn': 55, 'ap_contact_name': 832, 'address': 554, 'mailbox_gone': 335, 'ap_system': 448, 'setup_url': 323, 'buyer_phone_from_page': 9711, 'buyer_address_from_page': 633}
[  398s +   2s  4.4G] peppol: 77 Canadian participants; matched buyers 6, vendors 39
[  398s +   0s  4.4G] directories: 2338 entries reachable by their own site; 112 sites given by entries of different names, left out
[  401s +   2s  4.4G] municipal / organisation directories: {'matched': 1748, 'legal_name': 800, 'phone': 325, 'address': 46, 'matched_by_place_name': 12, 'website': 18}
[  401s +   0s  4.4G] charity buyers: {'matched': 9729, 'bn': 8039, 'legal_name': 6746, 'address': 631, 'website': 32}
[  402s +   1s  4.5G] charity registration numbers found in the CRA list: {'matched': 745, 'legal_name': 491, 'address': 68, 'name_from_the_register': 66, 'holder is a foundation / trust under another name: reported only': 27} | list: 83761
[  403s +   1s  4.5G] wikidata: {'vendors': 1154, 'buyers': 5226, 'buyer_legal_name': 2377, 'buyer_address': 624, 'buyer_phone': 90, 'buyer_website': 106, 'vendor_legal_name': 44, 'vendor_address': 412, 'vendor_website': 238, 'vendor_neq': 7}
[  404s +   0s  4.5G] crown-corporation BNs applied to inferred-vendor rows: 17093
[  404s +   0s  4.5G] vendor websites confirmed from search proposals: 502 applied: 18972
[  404s +   0s  4.5G] inferred vendors' published phone / address applied: {'phone': 13768}
[  405s +   1s  4.6G] registry bulk rows added (no API row for the key): 22305 | registry rows left out, the registered name is only legal-form and place words: 0
[  406s +   1s  4.6G] Canada's Business Registries + registry open data: 3706 vendors, 28246 buyers found; filled {'buyer_bn': 9164, 'buyer_legal_name': 13865, 'vendor_registered_address': 15619, 'vendor_bn9': 23848, 'vendor_legal_name': 15552, 'vendor_registry_status': 15554, 'vendor_incorporation_date': 15838, 'vendor_legal_form': 15561, 'vendor_neq': 4471, 'vendor_trading_name': 262, 'buyer_address': 2078, 'vendor_skipped_legal_form': 1, 'buyer record looked up under a name the row no longer carries, not taken': 6, 'vendor_bn9_other_registry': 4, 'buyer record of another name than the legal person the site itself states, not taken': 19}
[  407s +   0s  4.6G] award facts from the buyers' own award pages: 237 pairs with a page; filled {'contract_value': 39, 'end_date': 17, 'start_date': 9, 'contract_or_agreement_number': 3, 'solicitation_or_tender_number': 6, 'term': 2, 'po_number_as_published': 1, 'number_of_bids': 1}
[  408s +   1s  4.6G] legal name: the organisation's own name carries its legal form (cells still empty after every register and site statement): 6110
[  408s +   0s  4.6G] grants & contributions recipient BNs: 3202 buyers, 454 vendors in file; filled {'buyer_bn': 1600, 'buyer_bn_conflict_noted': 86, 'vendor_bn9': 776, 'buyer_legal_name': 316}
[  423s +  15s  4.7G] buyers' PO / contract open data joined: {'pairs': 5, 'po_filled': 4, 'contract_filled': 1} | records read: 330978 | kept (a row's own buyer-vendor pair): 143
[  436s +  13s  5.0G] back-references: {'dataset rows with lead relationships': 150242, 'lead rows with dataset history': 49}
[  448s +  12s  4.8G] sensitivity tags: {'corrections / detention': 36, 'health: mental health / addiction / sexual health': 438, 'intelligence / security / defence': 25, 'police service / police board': 99, 'courts / tribunals / legal aid': 81, 'child / youth protection': 28, 'police oversight body': 5, 'shelter / crisis / sexual-assault service': 90, 'coroner / medical examiner': 1}
[  456s +   8s  4.8G] site readers, second pass (websites found late): {'buyer_logo': 591, 'vendor_emails': 572, 'vendor_phone': 754, 'vendor_logo': 34692, 'vendor_address': 237, 'buyer_address': 5, 'buyer_phone': 44}
[  456s +   0s  4.8G] listings on a site that is not the Canada-located vendor's own (-> tier E): {'kept — the site prints an address in Canada': 4358, "kept — Wikidata: the site's organisation has its headquarters in Canada": 1486, 'kept — no evidence about whose site it is': 3444, "the site's own address is outside Canada": 111, 'from tier D': 781, "Wikidata: the site's organisation has its headquarters outside Canada": 517, "kept — the listing is in the site's Canadian section (/ca/, /en-ca/, ca.…)": 48, 'Canadian arm of a group, site not shown to be its own': 39, "kept although the site reader's address is abroad (Wikidata: headquarters in Canada)": 40, "the vendor's published terms: its Canadian entity does not contract with customers of this buyer's country": 114, "kept — address abroad on the site, but a corporation of the site's name is registered in Canada": 11}
[  459s +   3s  4.8G] same-vendor carry-over (BN9, identity facts and address from the vendor's other rows): {'address': 130, 'bn9': 100214, 'legal_name': 100210, 'trading_name': 100211, 'phone': 5, 'gst_hst_derived': 100214, 'registry_id': 100207, 'registry_url': 100207, 'registered_address': 100207, 'legal_form': 100207, 'registry_status': 100207, 'registry_match_level': 100208, 'incorporation_date': 100207, 'logo_url': 4, 'neq': 1}
[  585s + 125s  4.7G] rows written: 100000 of 242292
[  707s + 122s  4.6G] rows written: 200000 of 242292
[  760s +  53s  4.4G] narrative columns: {'mailbox meta found': 234977, 'contract_description_from_title': 169424, 'contract_title_from_description': 142, 'invoice_reference_hint_po_rule': 1161, 'records_with_this_vendor_lead': 218883, 'mailbox meta missing': 1338}
[  760s +   0s  4.4G] downstream pack: {'tax_derived_foreign': 21978, 'pay_on_sight_yes': 2292, 'ap_payable_today': 2031, 'ship_ready_yes': 962, 'buyer_trade_name_as_published': 177936, 'tax_derived': 154501, 'registry_note': 222, 'prompt_payment_default': 750, 'pay_on_sight_no': 158877, 'buyer_type_from_name': 28152, 'sensitivity_extra': 195, 'buyer_address_from_own_page': 4905, 'registry_warning': 1362, 'invoice_currency_derived': 220904, 'pay_on_sight_routed': 75146, 'currency_default': 2}
[  760s +   0s  4.4G] rows 242292
[  760s +   0s  4.4G] [('GOLD', 625), ('A0', 519), ('A1', 712), ('A2', 92), ('A3', 223), ('A4', 8), ('B0', 623), ('B1', 1007), ('B2', 131), ('B3', 186), ('B4', 11), ('C0', 1003), ('C1', 252), ('C2', 19), ('C3', 26), ('C4', 26), ('D0', 602), ('D1', 27328), ('D2', 182), ('D3', 683), ('D4', 324), ('E0', 260), ('E1', 4910), ('E2', 96), ('E3', 126), ('E4', 103), ('F0', 1), ('F1', 4), ('F2', 1), ('F3', 1), ('F4', 1), ('GOLD-M', 100), ('GOLD-T', 334), ('I0', 716), ('I1', 17640), ('I2', 61), ('I3', 242), ('I4', 108), ('L0', 217), ('L1', 317), ('L2', 33), ('L3', 19), ('L4', 71), ('M0', 188), ('M1', 10178), ('M2', 31), ('M3', 144), ('M4', 1), ('R0', 189), ('R1', 98759), ('R2', 100), ('R3', 978), ('R4', 179), ('T0', 1659), ('T1', 68854), ('T2', 151), ('T3', 923), ('T4', 15)]
[  760s +   0s  4.4G] with any email: 236315 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            625
P01T_active_service_seen_on_buyer_site_invoicing_AP_email    334
P02_active_relationship_finance_accounting_email           473
P03_active_relationship_purchasing_email                   257
P04_active_relationship_general_email (2 part files)      3834
P05_likely_active_awarded_12_36_months_any_email           427
P06_client_listing_invoicing_AP_email                      313
P06T_active_service_seen_on_buyer_site_other_email (19 part files)  60046
P07_client_listing_finance_or_purchasing_email             841
P08_client_listing_general_email (8 part files)          26848
P09_older_contract_or_payment_any_email                    303
P10_linked_from_vendor_site_any_email                     2750
P10R_ca_domain_registration_contract_own_email (37 part files)  99167
P11_any_relationship_email_not_yet_confirmed (4 part files)  11585
P12_weaker_relationship_within_5_years_own_email             7
P13_inferred_relationship_no_record_own_email (6 part files)  18051
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email    100
P06M_member_or_regulated_payer_of_canadian_body_other_email (4 part files)  10275
Z_no_email_yet_not_delivered (2 part files)               6056
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 27096423
package files: compressed (.csv.gz); packages written straight from the table (already in order): 17 of 19; sorted from a working copy: P11 (11585 rows); sorted from a working copy: Z (6056 rows)

# coverage vs the downstream targets (COVERAGE_VS_TARGETS.md)
benchmarks met 92 / 446 (20.6%); near 54; written out/ranked/COVERAGE_VS_TARGETS.md
  gap buyer_ap_cycle_published           P10R       0.0% ->  20%  rows needed 19817
  gap ap_system_hint                     P10R       0.2% ->  20%  rows needed 19640
  gap vendor_registered_address          P08       12.5% ->  70%  rows needed 15425
  gap buyer_tax_exempt_status            P10R       0.0% ->  15%  rows needed 14856
  gap buyer_esignature_preference        P10R       0.0% ->  15%  rows needed 14844
  gap buyer_payment_method_preference    P10R       0.4% ->  15%  rows needed 14485
  gap buyer_ap_cycle_published           P06T       0.0% ->  20%  rows needed 11990
  gap buyer_phone                        P08       50.9% ->  95%  rows needed 11838
  gap ap_system_hint                     P06T       0.7% ->  20%  rows needed 11575
  gap vendor_bn9                         P08        9.6% ->  50%  rows needed 10843
  gap buyer_legal_name_as_published      P08       36.7% ->  75%  rows needed 10283
  gap buyer_logo_url                     P08       66.8% -> 100%  rows needed 8919
  gap buyer_esignature_preference        P06T       0.2% ->  15%  rows needed 8870
  gap buyer_tax_exempt_status            P06T       0.3% ->  15%  rows needed 8834
  gap buyer_payment_method_preference    P06T       0.4% ->  15%  rows needed 8745
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
