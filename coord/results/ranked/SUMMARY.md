# Ranked buyers — 2026-11-10T18:19Z

```
[   14s +  14s  1.5G] mailboxes taken from the verification log (better than org_mailboxes' single pick): 773 | referee mailbox rows whose last label is not a top-level domain: {'left out': 15, 'cut back to the address the page prints': 63}
[   24s +  10s  0.7G] vendor table: registry matches not used because the legal form differs (partnership vs corporation): 55 | 'websites' that are a web host's own site (dropped with their mailboxes): 5 | websites not used for a look-up by domain (unverified, name does not fit): 0 | look-ups by domain: 8051
[   24s +   0s  0.7G] team vendor contacts (referee-verified): 8781 vendors; 172 with a billing / AR mailbox
[  160s + 136s  2.1G] same-pair fill (facts from another record of the same buyer-vendor pair): {'solicitation_or_tender_number': 11, 'number_of_bids': 10, 'award_or_notice_id': 2, 'buyer_vendor_id': 2, 'commodity_codes': 9, 'end_date_inferred': 120, 'contract_value': 7, 'procurement_method': 3, 'po_number_as_published': 3, 'buyer_org_codes': 1, 'start_from_signed': 497, 'end_date': 3, 'contract_description': 2, 'contract_or_agreement_number': 2, 'contract_title': 1}
[  160s +   0s  2.1G] contract records whose vendor's registry match pairs a partnership with a corporation (registry cells not used): 2244
[  165s +   6s  2.6G] tenant leads from the shards: 10037
[  165s +   0s  2.6G] leads: 376797 (295770 from the cloud row factory; 49 websites from the lead site finder)
[  187s +  22s  2.8G] registry leads (.ca domains carrying a confirmed mailbox of their own organisation): 141094
[  207s +  20s  3.0G] lead rows: facts from the buyer's own pages / the vendor's link label: {'buyer_address_from_own_page': 104554, 'buyer_name_from_own_home_page': 113870, 'facts of another host of the domain not taken': 267, 'vendor_address_cut_out_of_its_quote': 20569, 'buyer_legal_name_from_register': 4937, 'buyer_address_from_member_directory': 4623, 'buyer_name_from_vendor_link_label': 2255} | sites named again from their stored home-page title: 1144
[  207s +   0s  3.0G] client-page links judged (cloud row factory): {'client listing: label names the site': 3363, 'link only, and the site has a .ca registration: the registration takes the row': 1577, "not shown to be a client: the link's label does not name the linked site": 1235, "client listing: 'visit website' on a client page": 260, 'client listing: portfolio page': 177, 'client listing: page address names the site': 176, 'not shown to be a client: a page for clients (forms, resources, login), not a list of them': 170, "not shown to be a client: an organisation's 'our work' programme page": 124, "not shown to be a client: sister site of the page's owner": 87, 'not shown to be a client: article: the client word sits in a slug of 4 words': 32, 'not shown to be a client: dated article': 21, 'not shown to be a client: article: the client word sits in a slug of 5 words': 13, 'not shown to be a client: article: the client word sits in a slug of 6 words': 1}
[  211s +   4s  3.0G] leads with a borrowed mailbox: 95946 | rows upgraded by a newer dated record: 42 | rows upgraded to an active service seen on the buyer's site: 388
[  221s +  10s  3.1G] P12 organisations: 93 added: 9 {'no own confirmed mailbox': 66, 'same organisation already in a row': 18} | P13 added: 18533 | P13 skipped: {"mailbox not the organisation's own": 2153, 'bad mailbox': 188, 'not located in Canada (no honest inference)': 12567, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 63056, '… of which by the NAME alone (its own mailbox and domain are in no row)': 131}
[  221s +   0s  3.1G] lead rows that took the organisation's own key (registry facts attach): {'rows': 44366, 'buyer_address': 4905, 'buyer_name': 3261}
[  240s +  19s  3.1G] extras from the lanes' result rows: {'invoice_mailing_address': 2288, 'invoicing_requirements': 2104, 'ap_phone': 2384, 'invoice_portal_url': 73, 'ap_contact_name': 237}
[  249s +   9s  3.2G] words too common to prove a name (in more than 1 in 2,000 of the 171993 names of organisations whose site was read): 462; names printed on 3+ sites: 1406
[  276s +  27s  3.2G] org_extras: 173134 organisations read; filled {'vendor_logo': 66023, 'vendor_phone_v2': 42230, 'po_required': 243, 'vendor_trading_name_jsonld': 6745, 'buyer_legal_name': 49520, 'buyer_phone_v2': 77519, 'buyer_payment_method_preference_mention_rejected': 18038, 'buyer_logo': 139422, 'payment_terms': 696, 'buyer_tax_exempt_status_mention_rejected': 298, 'buyer_legal_name_v2_printed_on_many_sites': 8410, 'buyer_legal_name_v2_legal_name_stated': 12400, "vendor site is a foreign organisation's: its legal / trading name not taken for the Canada-located vendor": 1314, 'buyer_bn': 2999, 'buyer_legal_name_v2_rejected_no_overlap': 40821, 'buyer_legal_name_v2_jsonld_name': 5363, 'buyer_legal_name_v2_jsonld_legal_name': 5562, 'ap_system_hint_links': 426, 'buyer_legal_name_government_template_credit': 40, 'buyer_payment_method_preference_mention': 801, 'vendor_legal_name': 9978, 'vendor_neq': 120, 'buyer_esignature_preference_mention_rejected': 519, 'vendor_legal_name_v2': 6116, 'buyer_address_v2': 6183, 'p13_name_from_legal_name': 9286, 'buyer_esignature_preference_mention': 52, 'buyer_legal_name_v2_jsonld_legal_name_own_site_node': 388, 'invoice_portal_links': 58, 'buyer_legal_name_v2_jsonld_name_own_site_node': 383, 'vendor_bn': 624, 'buyer_tax_exempt_status_mention': 65, 'vendor_bn_jsonld': 53, 'buyer_bn_jsonld': 137, 'vendor_address_v2': 290, 'vendor_address_v2_outside_canada_not_taken': 107, 'buyer_ap_cycle_published_mention': 36, 'vendor_legal_name_v2_site_says': 114, 'buyer_legal_name_v2_stated_as_operator': 120, 'vendor_qst': 14, 'buyer_legal_name_v2_doing_business_as': 16, 'buyer_ap_cycle_published_mention_rejected': 33, 'buyer_legal_name_franchisor_copyright_not_taken': 7, 'p13_name_from_domain': 1}
[  276s +   0s  3.2G] regional mailboxes of multinationals removed from other-country entities: 44
[  277s +   0s  3.2G] mx_check: 69559 domains known; 184 mailboxes on domains with no mail server removed; 711 webmail (freemail) addresses removed
[  279s +   2s  3.5G] dmarc/spf: 220183 domains known; rows {'enforced': 41020, 'exposed': 165873}
[  279s +   0s  3.5G] same organisation under another key folded into the row that holds its mailbox: 52
[  282s +   2s  3.5G] second mailbox of the same organisation (same site and mail domain, same name family) folded: 6
[  286s +   4s  3.7G] org_contacts: 162071 organisations read; filled {'vendor_phone': 55205, 'vendor_emails': 34308, 'buyer_phone': 88070, 'vendor site prints an address outside Canada: address and telephone not taken': 1077, 'buyer_address': 16799, 'vendor_address': 2001}
[  286s +   0s  3.7G] site-reader records read on another host of the row's domain (look-ups): {'org_contacts: not taken': 2445, 'org_extras: not taken': 2788, 'org_contacts: taken, read on another host for the same organisation (same name)': 878, "org_extras: taken, the row's host is the member directory of the body whose own site was read": 1309, "org_contacts: taken, the row's host is the member directory of the body whose own site was read": 3243, 'org_extras: taken, read on another host for the same organisation (same name)': 435}
[  293s +   7s  4.2G] ap_terms (evidence pages re-read): 82907 keys read, 109751 pages used across rows; filled {'payment_terms': 3595, 'po_required': 1924, 'payment_method': 703, 'ap_cycle': 108, 'tax_exempt': 1022, 'portal': 1978, 'format': 743, 'context': 45815, 'esignature': 614, 'ap_system_portal': 1713, 'ap_phone': 1121, 'buyer_bn': 56, 'ap_contact_name': 834, 'address': 555, 'mailbox_gone': 334, 'ap_system': 452, 'setup_url': 325, 'buyer_phone_from_page': 9682, 'buyer_address_from_page': 656}
[  295s +   2s  4.1G] peppol: 77 Canadian participants; matched buyers 5, vendors 38
[  295s +   0s  4.1G] directories: 2338 entries reachable by their own site; 112 sites given by entries of different names, left out
[  296s +   1s  4.1G] municipal / organisation directories: {'matched': 1741, 'legal_name': 796, 'phone': 321, 'address': 45, 'matched_by_place_name': 11, 'website': 18}
[  297s +   0s  4.1G] charity buyers: {'matched': 7266, 'bn': 6007, 'legal_name': 4282, 'address': 304, 'website': 25}
[  298s +   1s  4.1G] wikidata: {'vendors': 1146, 'buyers': 5247, 'buyer_legal_name': 2499, 'buyer_address': 636, 'buyer_phone': 90, 'buyer_website': 109, 'vendor_legal_name': 43, 'vendor_address': 406, 'vendor_website': 239, 'vendor_neq': 7}
[  298s +   0s  4.1G] crown-corporation BNs applied to inferred-vendor rows: 16883
[  298s +   0s  4.2G] vendor websites confirmed from search proposals: 502 applied: 10917
[  298s +   0s  4.2G] inferred vendors' published phone / address applied: {'phone': 13384}
[  299s +   0s  4.2G] registry bulk rows added (no API row for the key): 22305 | registry rows left out, the registered name is only legal-form and place words: 0
[  300s +   1s  4.2G] Canada's Business Registries + registry open data: 3706 vendors, 28246 buyers found; filled {'buyer_bn': 9556, 'buyer_legal_name': 15276, 'vendor_registered_address': 14725, 'vendor_bn9': 15332, 'vendor_legal_name': 14656, 'vendor_registry_status': 14658, 'vendor_incorporation_date': 14943, 'vendor_legal_form': 14665, 'vendor_neq': 4093, 'vendor_trading_name': 273, 'buyer_address': 2248, 'vendor_skipped_legal_form': 1, 'buyer record looked up under a name the row no longer carries, not taken': 5, 'vendor_bn9_other_registry': 4, 'buyer record of another name than the legal person the site itself states, not taken': 20}
[  300s +   0s  4.2G] award facts from the buyers' own award pages: 237 pairs with a page; filled {'contract_value': 39, 'end_date': 17, 'start_date': 9, 'contract_or_agreement_number': 3, 'solicitation_or_tender_number': 6, 'term': 2, 'po_number_as_published': 1, 'number_of_bids': 1}
[  301s +   1s  4.2G] grants & contributions recipient BNs: 3202 buyers, 454 vendors in file; filled {'buyer_bn': 1613, 'buyer_bn_conflict_noted': 87, 'vendor_bn9': 774, 'buyer_legal_name': 340}
[  311s +  11s  4.3G] buyers' PO / contract open data joined: {'pairs': 5, 'po_filled': 4, 'contract_filled': 1} | records read: 330978 | kept (a row's own buyer-vendor pair): 143
[  321s +   9s  4.6G] back-references: {'dataset rows with lead relationships': 138541, 'lead rows with dataset history': 47}
[  328s +   7s  4.4G] sensitivity tags: {'corrections / detention': 35, 'health: mental health / addiction / sexual health': 397, 'intelligence / security / defence': 25, 'police service / police board': 90, 'courts / tribunals / legal aid': 71, 'child / youth protection': 25, 'police oversight body': 5, 'shelter / crisis / sexual-assault service': 83, 'coroner / medical examiner': 1}
[  334s +   6s  4.4G] site readers, second pass (websites found late): {'buyer_logo': 588, 'vendor_emails': 559, 'vendor_phone': 743, 'vendor_logo': 26235, 'vendor_address': 230, 'buyer_address': 6, 'buyer_phone': 42}
[  334s +   0s  4.4G] listings on a site that is not the Canada-located vendor's own (-> tier E): {'kept — the site prints an address in Canada': 2206, "kept — Wikidata: the site's organisation has its headquarters in Canada": 1303, 'kept — no evidence about whose site it is': 532, "the site's own address is outside Canada": 102, 'from tier D': 720, "Wikidata: the site's organisation has its headquarters outside Canada": 488, "kept — the listing is in the site's Canadian section (/ca/, /en-ca/, ca.…)": 50, 'Canadian arm of a group, site not shown to be its own': 27, "kept although the site reader's address is abroad (Wikidata: headquarters in Canada)": 38, "the vendor's published terms: its Canadian entity does not contract with customers of this buyer's country": 103, "kept — address abroad on the site, but a corporation of the site's name is registered in Canada": 11}
[  337s +   2s  4.4G] same-vendor carry-over (BN9, identity facts and address from the vendor's other rows): {'address': 129, 'bn9': 100496, 'legal_name': 100492, 'trading_name': 100493, 'phone': 5, 'gst_hst_derived': 100496, 'registry_id': 100489, 'registry_url': 100489, 'registered_address': 100489, 'legal_form': 100489, 'registry_status': 100489, 'registry_match_level': 100490, 'incorporation_date': 100489, 'logo_url': 4, 'neq': 1}
[  425s +  89s  4.3G] rows written: 100000 of 218446
[  514s +  89s  4.2G] rows written: 200000 of 218446
[  529s +  15s  4.0G] narrative columns: {'mailbox meta found': 211596, 'contract_description_from_title': 161075, 'contract_title_from_description': 142, 'invoice_reference_hint_po_rule': 1170, 'records_with_this_vendor_lead': 195271, 'mailbox meta missing': 1497}
[  529s +   0s  4.0G] downstream pack: {'tax_derived_foreign': 14099, 'pay_on_sight_yes': 2261, 'ap_payable_today': 1862, 'ship_ready_yes': 898, 'buyer_trade_name_as_published': 156509, 'tax_derived': 141234, 'registry_note': 222, 'prompt_payment_default': 635, 'pay_on_sight_no': 139934, 'buyer_type_from_name': 27262, 'sensitivity_extra': 183, 'buyer_address_from_own_page': 3987, 'registry_warning': 1302, 'invoice_currency_derived': 200222, 'pay_on_sight_routed': 70898, 'currency_default': 2}
[  529s +   0s  4.0G] rows 218446
[  529s +   0s  4.0G] [('GOLD', 625), ('A0', 519), ('A1', 713), ('A2', 91), ('A3', 223), ('A4', 8), ('B0', 623), ('B1', 992), ('B2', 130), ('B3', 186), ('B4', 12), ('C0', 1003), ('C1', 252), ('C2', 19), ('C3', 26), ('C4', 26), ('D0', 474), ('D1', 21032), ('D2', 163), ('D3', 540), ('D4', 289), ('E0', 221), ('E1', 4221), ('E2', 92), ('E3', 114), ('E4', 100), ('F0', 1), ('F1', 4), ('F2', 1), ('F3', 2), ('F4', 1), ('GOLD-M', 65), ('GOLD-T', 304), ('I0', 678), ('I1', 17434), ('I2', 64), ('I3', 247), ('I4', 110), ('L0', 217), ('L1', 304), ('L2', 32), ('L3', 19), ('L4', 71), ('M0', 52), ('M1', 5963), ('M2', 22), ('M3', 73), ('M4', 1), ('R0', 162), ('R1', 99072), ('R2', 100), ('R3', 973), ('R4', 180), ('T0', 1403), ('T1', 57223), ('T2', 137), ('T3', 824), ('T4', 13)]
[  529s +   0s  4.0G] with any email: 213093 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            625
P01T_active_service_seen_on_buyer_site_invoicing_AP_email    304
P02_active_relationship_finance_accounting_email           462
P03_active_relationship_purchasing_email                   255
P04_active_relationship_general_email (2 part files)      3254
P05_likely_active_awarded_12_36_months_any_email           413
P06_client_listing_invoicing_AP_email                      278
P06T_active_service_seen_on_buyer_site_other_email (17 part files)  53606
P07_client_listing_finance_or_purchasing_email             680
P08_client_listing_general_email (6 part files)          20545
P09_older_contract_or_payment_any_email                    303
P10_linked_from_vendor_site_any_email                     2607
P10R_ca_domain_registration_contract_own_email (36 part files)  96430
P11_any_relationship_email_not_yet_confirmed (4 part files)   9344
P12_weaker_relationship_within_5_years_own_email             8
P13_inferred_relationship_no_record_own_email (6 part files)  17855
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email     65
P06M_member_or_regulated_payer_of_canadian_body_other_email (3 part files)   6002
Z_no_email_yet_not_delivered (2 part files)               5410
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 24344455
package files: compressed (.csv.gz); packages written straight from the table (already in order): 17 of 19; sorted from a working copy: P11 (9344 rows); sorted from a working copy: Z (5410 rows)

# coverage vs the downstream targets (COVERAGE_VS_TARGETS.md)
benchmarks met 54 / 446 (12.1%); near 91; written out/ranked/COVERAGE_VS_TARGETS.md
  gap buyer_ap_cycle_published           P10R       0.0% ->  20%  rows needed 19269
  gap ap_system_hint                     P10R       0.2% ->  20%  rows needed 19092
  gap buyer_tax_exempt_status            P10R       0.0% ->  15%  rows needed 14444
  gap buyer_esignature_preference        P10R       0.0% ->  15%  rows needed 14431
  gap buyer_payment_method_preference    P10R       0.4% ->  15%  rows needed 14063
  gap vendor_registered_address          P08       15.0% ->  70%  rows needed 11305
  gap buyer_ap_cycle_published           P06T       0.0% ->  20%  rows needed 10703
  gap ap_system_hint                     P06T       0.8% ->  20%  rows needed 10298
  gap buyer_esignature_preference        P06T       0.2% ->  15%  rows needed 7910
  gap vendor_bn9                         P08       11.6% ->  50%  rows needed 7880
  gap buyer_tax_exempt_status            P06T       0.3% ->  15%  rows needed 7876
  gap buyer_phone                        P13       51.0% ->  95%  rows needed 7855
  gap buyer_payment_method_preference    P06T       0.5% ->  15%  rows needed 7782
  gap buyer_logo_url                     P13       54.4% ->  95%  rows needed 7247
  gap buyer_legal_name_as_published      P08       42.8% ->  75%  rows needed 6608
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
