# Ranked buyers — 2026-11-11T12:35Z

```
[   29s +  29s  1.8G] mailboxes taken from the verification log (better than org_mailboxes' single pick): 808 | referee mailbox rows whose last label is not a top-level domain: {'left out': 15, 'cut back to the address the page prints': 62}
[   44s +  14s  0.8G] vendor table: registry matches not used because the legal form differs (partnership vs corporation): 55 | 'websites' that are a web host's own site (dropped with their mailboxes): 6 | websites not used for a look-up by domain (unverified, name does not fit): 0 | look-ups by domain: 8050
[   44s +   0s  0.8G] team vendor contacts (referee-verified): 8782 vendors; 172 with a billing / AR mailbox
[  241s + 198s  2.2G] same-pair fill (facts from another record of the same buyer-vendor pair): {'solicitation_or_tender_number': 11, 'number_of_bids': 10, 'award_or_notice_id': 2, 'buyer_vendor_id': 2, 'commodity_codes': 9, 'end_date_inferred': 120, 'contract_value': 7, 'procurement_method': 3, 'po_number_as_published': 3, 'buyer_org_codes': 1, 'start_from_signed': 497, 'end_date': 3, 'contract_description': 2, 'contract_or_agreement_number': 2, 'contract_title': 1}
[  241s +   0s  2.2G] contract records whose vendor's registry match pairs a partnership with a corporation (registry cells not used): 2244
[  261s +  19s  3.7G] tenant leads from the shards: 26922
[  261s +   0s  3.7G] leads: 659050 (561138 from the cloud row factory; 64 websites from the lead site finder)
[  303s +  43s  4.1G] registry leads (.ca domains carrying a confirmed mailbox of their own organisation): 152415
[  304s +   0s  4.1G] organisations' second domain names (the name on file answers at their site under another domain): 9984 {'registry lead for a .ca name whose site lives under another ending': 3583, '.ca name answering at another .ca site (that site has its own registry lead)': 3495, 'lead of another lane: its site is the one that answers': 2902, 'no confirmed mailbox on the site that answers (yet)': 4}
[  343s +  39s  4.4G] lead rows: facts from the buyer's own pages / the vendor's link label: {'buyer_address_from_own_page': 143460, 'buyer_name_from_own_home_page': 131527, 'facts of another host of the domain not taken': 341, 'vendor_address_cut_out_of_its_quote': 38651, 'buyer_legal_name_from_register': 10916, 'buyer_address_from_member_directory': 6254, 'buyer_name_from_vendor_link_label': 2779} | sites named again from their stored home-page title: 1145
[  343s +   0s  4.4G] client-page links judged (cloud row factory): {'client listing: label names the site': 4609, 'link only, and the site has a .ca registration: the registration takes the row': 1792, "not shown to be a client: the link's label does not name the linked site": 1776, "client listing: 'visit website' on a client page": 458, 'client listing: portfolio page': 312, 'client listing: page address names the site': 231, 'not shown to be a client: a page for clients (forms, resources, login), not a list of them': 204, "not shown to be a client: an organisation's 'our work' programme page": 185, "not shown to be a client: sister site of the page's owner": 104, 'not shown to be a client: article: the client word sits in a slug of 4 words': 64, 'not shown to be a client: dated article': 19, 'not shown to be a client: article: the client word sits in a slug of 5 words': 14, 'not shown to be a client: article: the client word sits in a slug of 6 words': 1}
[  351s +   8s  4.4G] leads with a borrowed mailbox: 119755 | rows upgraded by a newer dated record: 43 | rows upgraded to an active service seen on the buyer's site: 473
[  367s +  16s  4.5G] P12 organisations: 90 added: 8 {'no own confirmed mailbox': 64, 'same organisation already in a row': 18} | P13 added: 18436 | P13 skipped: {"mailbox not the organisation's own": 2337, 'bad mailbox': 271, 'not located in Canada (no honest inference)': 17124, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 79952, '… of which by the NAME alone (its own mailbox and domain are in no row)': 135}
[  367s +   0s  4.5G] lead rows that took the organisation's own key (registry facts attach): {'rows': 45247, 'buyer_address': 4835, 'buyer_name': 3556}
[  395s +  28s  4.5G] extras from the lanes' result rows: {'invoice_mailing_address': 2330, 'invoicing_requirements': 2133, 'ap_phone': 2425, 'invoice_portal_url': 73, 'ap_contact_name': 286}
[  412s +  17s  4.5G] words too common to prove a name (in more than 1 in 2,000 of the 235603 names of organisations whose site was read): 535; names printed on 3+ sites: 1658
[  474s +  62s  4.5G] org_extras: 238794 organisations read; filled {'vendor_logo': 89614, 'vendor_phone_v2': 65038, 'po_required': 276, 'vendor_trading_name_jsonld': 15404, 'buyer_legal_name': 89034, 'buyer_phone_v2': 109858, 'buyer_payment_method_preference_mention_rejected': 18172, 'buyer_logo': 199852, 'payment_terms': 1077, 'buyer_tax_exempt_status_mention_rejected': 346, 'buyer_legal_name_v3_spelled_by_the_domain': 22141, 'buyer_legal_name_v2_legal_name_stated': 18409, "vendor site is a foreign organisation's: its legal / trading name not taken for the Canada-located vendor": 1367, 'buyer_bn': 3495, 'buyer_legal_name_v2_rejected_no_overlap': 49191, 'buyer_legal_name_v2_jsonld_name': 5025, 'buyer_legal_name_v2_printed_on_many_sites': 7017, 'buyer_legal_name_v2_jsonld_legal_name': 6282, 'ap_system_hint_links': 519, 'buyer_legal_name_government_template_credit': 40, 'buyer_payment_method_preference_mention': 1428, 'vendor_legal_name': 15329, 'vendor_legal_name_v3_spelled_by_the_domain': 5993, 'vendor_neq': 161, 'buyer_esignature_preference_mention_rejected': 548, 'vendor_legal_name_v2': 11600, 'invoice_portal_links': 78, 'buyer_ap_cycle_published_mention': 61, 'buyer_address_v2': 7366, 'buyer_legal_name_v3_stated_as_operator': 1507, 'p13_name_from_legal_name': 14091, "vendor named by its own site's name instead of its domain": 18965, 'buyer_esignature_preference_mention': 88, 'buyer_legal_name_v2_jsonld_name_own_site_node': 497, 'vendor_legal_name_v3_legal_person_behind_the_site_name': 1060, 'vendor_bn': 785, 'buyer_legal_name_v3_legal_person_behind_the_site_name': 1452, 'vendor_legal_name_v2_site_says': 964, 'buyer_tax_exempt_status_mention': 138, 'vendor_bn_jsonld': 77, 'buyer_bn_jsonld': 171, 'buyer_legal_name_v2_jsonld_legal_name_own_site_node': 382, 'buyer_legal_name_kept_from_the_trademarks_register': 1474, 'vendor_address_v2': 299, 'vendor_address_v2_outside_canada_not_taken': 117, 'vendor_legal_name_v3_stated_as_operator': 60, 'buyer_legal_name_v2_stated_as_operator': 54, 'vendor_qst': 18, 'buyer_ap_cycle_published_mention_rejected': 32, 'buyer_legal_name_franchisor_copyright_not_taken': 10, 'buyer_legal_name_v2_doing_business_as': 9}
[  474s +   0s  4.5G] regional mailboxes of multinationals removed from other-country entities: 57
[  475s +   1s  4.5G] mx_check: 69559 domains known; 186 mailboxes on domains with no mail server removed; 877 webmail (freemail) addresses removed
[  479s +   4s  4.8G] dmarc/spf: 274286 domains known; rows {'enforced': 51631, 'exposed': 211197}
[  480s +   0s  4.8G] same organisation under another key folded into the row that holds its mailbox: 52
[  484s +   4s  4.8G] second mailbox of the same organisation (same site and mail domain, same name family) folded: 6
[  489s +   6s  5.0G] org_contacts: 232435 organisations read; filled {'vendor_phone': 72265, 'vendor_emails': 44041, 'buyer_phone': 127154, 'vendor site prints an address outside Canada: address and telephone not taken': 1115, 'buyer_address': 18756, 'vendor_address': 1950}
[  489s +   0s  5.0G] site-reader records read on another host of the row's domain (look-ups): {'org_extras: not taken': 685, 'org_contacts: not taken': 1332, 'org_contacts: taken, read on another host for the same organisation (same name)': 326, 'org_extras: taken, read on another host for the same organisation (same name)': 71, "org_contacts: taken, the row's host is the member directory of the body whose own site was read": 1002, "org_extras: taken, the row's host is the member directory of the body whose own site was read": 200}
[  498s +   9s  5.5G] ap_terms (evidence pages re-read): 82907 keys read, 107737 pages used across rows; filled {'payment_terms': 3460, 'po_required': 1861, 'payment_method': 692, 'ap_cycle': 107, 'tax_exempt': 998, 'portal': 1951, 'format': 735, 'context': 45769, 'esignature': 600, 'ap_system_portal': 1693, 'ap_phone': 1101, 'buyer_bn': 52, 'ap_contact_name': 825, 'address': 552, 'mailbox_gone': 336, 'ap_system': 435, 'setup_url': 317, 'buyer_phone_from_page': 9486, 'buyer_address_from_page': 599}
[  501s +   2s  5.5G] peppol: 77 Canadian participants; matched buyers 9, vendors 39
[  501s +   0s  5.5G] directories: 2338 entries reachable by their own site; 112 sites given by entries of different names, left out
[  503s +   2s  5.5G] municipal / organisation directories: {'matched': 1752, 'legal_name': 777, 'phone': 321, 'address': 47, 'matched_by_place_name': 12, 'website': 19}
[  504s +   1s  5.5G] charity buyers: {'matched': 9513, 'bn': 7793, 'legal_name': 6378, 'address': 606, 'website': 32}
[  505s +   1s  5.6G] charity registration numbers found in the CRA list: {'matched': 939, 'legal_name': 571, 'address': 77, 'name_from_the_register': 89, 'holder is a foundation / trust under another name: reported only': 35} | list: 83761
[  506s +   2s  5.6G] wikidata: {'vendors': 1364, 'buyers': 5199, 'buyer_legal_name': 2143, 'buyer_phone': 90, 'buyer_address': 611, 'buyer_website': 107, 'vendor_legal_name': 43, 'vendor_address': 576, 'vendor_website': 232, 'vendor_neq': 6}
[  507s +   1s  5.6G] crown-corporation BNs applied to inferred-vendor rows: 16729
[  508s +   1s  5.6G] vendor websites confirmed from search proposals: 502 applied: 645 {"search proposal not taken: a directory / quote page / register, or a host that does not carry the vendor's name": 498, 'vetted vendor: the site of its own terms page': 30972}
[  508s +   0s  5.6G] inferred vendors' published phone / address applied: {'phone': 13566}
[  508s +   0s  5.7G] registry bulk rows added (no API row for the key): 22305 | registry rows left out, the registered name is only legal-form and place words: 0
[  510s +   2s  5.7G] Canada's Business Registries + registry open data: 3706 vendors, 28246 buyers found; filled {'buyer_bn': 8889, 'buyer_legal_name': 13340, 'vendor_registered_address': 20188, 'vendor_bn9': 33363, 'vendor_registry_status': 20126, 'vendor_incorporation_date': 20434, 'vendor_legal_form': 20133, 'vendor_legal_name': 18593, 'vendor_neq': 7707, 'vendor_trading_name': 180, 'buyer_address': 1955, 'buyer record found under a plain name, another name than the site prints with its legal form: not taken': 292, 'vendor_skipped_legal_form': 1, 'buyer record of another name than the legal person the site itself states, not taken': 59, 'buyer record looked up under a name the row no longer carries, not taken': 9, 'vendor_bn9_other_registry': 4}
[  510s +   0s  5.7G] award facts from the buyers' own award pages: 237 pairs with a page; filled {'contract_value': 39, 'end_date': 17, 'start_date': 9, 'contract_or_agreement_number': 3, 'solicitation_or_tender_number': 6, 'term': 2, 'po_number_as_published': 1, 'number_of_bids': 1}
[  513s +   2s  5.8G] legal names read off a page, tidied: {'tidied': 792, 'owner': 75, "row's own name tidied with it": 145, 'fragment': 51, "row's own name: a clause of the sentence cut off": 2}
[  513s +   1s  5.8G] legal name: the organisation's own name carries its legal form (cells still empty after every register and site statement): 2624
[  514s +   1s  5.8G] legal names from validated certificate subjects (Certificate Transparency): domains on file 1946; {'buyer_legal_name': 53, "subject does not carry the organisation's own name: not taken": 62}
[  514s +   0s  5.8G] grants & contributions recipient BNs: 8183 buyers, 1075 vendors in file; filled {'buyer_bn': 5515, 'buyer_legal_name': 2546, 'vendor_bn9': 4293, 'buyer_bn_conflict_noted': 91}
[  516s +   2s  5.8G] vendor legal name, last links of the chain: {"the vendor's own name carries its legal form": 3381, "the vendor's own terms, read by hand": 27419}
[  518s +   2s  5.8G] vendors that are organisations of this table (same name, same province): facts carried from their own row: {'vendor_phone': 4247, 'vendor_website': 4816, 'vendor_legal_name': 661, 'vendor_bn9': 8}
[  534s +  16s  5.9G] buyers' PO / contract open data joined: {'pairs': 6, 'po_filled': 5, 'contract_filled': 1} | records read: 330978 | kept (a row's own buyer-vendor pair): 179
[  551s +  16s  6.3G] back-references: {'dataset rows with lead relationships': 153194, 'lead rows with dataset history': 62}
[  566s +  16s  5.9G] sensitivity tags: {'corrections / detention': 38, 'health: mental health / addiction / sexual health': 467, 'intelligence / security / defence': 27, 'police service / police board': 103, 'courts / tribunals / legal aid': 93, 'child / youth protection': 29, 'police oversight body': 5, 'shelter / crisis / sexual-assault service': 96, 'coroner / medical examiner': 1}
[  576s +   9s  5.9G] site readers, second pass (websites found late): {'buyer_logo': 595, 'vendor_phone': 5515, 'vendor_logo': 51388, 'vendor_emails': 1243, 'vendor_address': 840, 'buyer_address': 5, 'buyer_phone': 46}
[  576s +   0s  5.9G] listings on a site that is not the Canada-located vendor's own (-> tier E): {'kept — the site prints an address in Canada': 6354, "kept — Wikidata: the site's organisation has its headquarters in Canada": 1487, 'kept — no evidence about whose site it is': 1053, "the site's own address is outside Canada": 197, 'from tier D': 837, "Wikidata: the site's organisation has its headquarters outside Canada": 497, "kept — the listing is in the site's Canadian section (/ca/, /en-ca/, ca.…)": 48, 'Canadian arm of a group, site not shown to be its own': 29, "kept although the site reader's address is abroad (Wikidata: headquarters in Canada)": 38, "the vendor's published terms: its Canadian entity does not contract with customers of this buyer's country": 114, "kept — address abroad on the site, but a corporation of the site's name is registered in Canada": 11}
[  579s +   3s  5.9G] same-vendor carry-over (BN9, identity facts and address from the vendor's other rows): {'address': 138, 'bn9': 101691, 'legal_name': 101686, 'trading_name': 101676, 'gst_hst_derived': 101691, 'phone': 14, 'emails': 11, 'logo_url': 14, 'registry_id': 101671, 'registry_url': 101671, 'registered_address': 101671, 'legal_form': 101671, 'registry_status': 101671, 'registry_match_level': 101673, 'incorporation_date': 101671}
[  716s + 137s  5.9G] rows written: 100000 of 265999
[  856s + 140s  5.8G] rows written: 200000 of 265999
[  950s +  94s  5.7G] narrative columns: {'mailbox meta found': 257425, 'contract_description_from_title': 186553, 'contract_title_from_description': 142, 'invoice_reference_hint_po_rule': 1129, 'records_with_this_vendor_lead': 242930, 'mailbox meta missing': 1332}
[  950s +   0s  5.7G] downstream pack: {'tax_derived_foreign': 30572, 'pay_on_sight_yes': 2402, 'ap_payable_today': 2374, 'ship_ready_yes': 1050, 'buyer_trade_name_as_published': 194815, 'tax_derived': 166098, 'registry_note': 221, 'prompt_payment_default': 821, 'pay_on_sight_no': 173540, 'buyer_type_from_name': 45204, 'sensitivity_extra': 206, 'buyer_address_from_own_page': 2524, 'registry_warning': 1489, 'invoice_currency_derived': 242143, 'pay_on_sight_routed': 82815, 'currency_default': 2}
[  950s +   0s  5.7G] rows 265999
[  950s +   0s  5.7G] [('GOLD', 625), ('A0', 519), ('A1', 712), ('A2', 92), ('A3', 223), ('A4', 8), ('B0', 623), ('B1', 1010), ('B2', 130), ('B3', 186), ('B4', 11), ('C0', 1004), ('C1', 245), ('C2', 18), ('C3', 26), ('C4', 26), ('D0', 603), ('D1', 26011), ('D2', 175), ('D3', 647), ('D4', 306), ('E0', 261), ('E1', 4805), ('E2', 96), ('E3', 123), ('E4', 104), ('F0', 1), ('F1', 3), ('F2', 1), ('F3', 2), ('F4', 1), ('GOLD-M', 125), ('GOLD-T', 398), ('I0', 739), ('I1', 17294), ('I2', 60), ('I3', 242), ('I4', 101), ('L0', 217), ('L1', 312), ('L2', 33), ('L3', 20), ('L4', 70), ('M0', 225), ('M1', 12944), ('M2', 57), ('M3', 178), ('M4', 1), ('R0', 237), ('R1', 100155), ('R2', 94), ('R3', 1004), ('R4', 180), ('T0', 2813), ('T1', 88551), ('T2', 193), ('T3', 1139), ('T4', 20)]
[  950s +   0s  5.7G] with any email: 258757 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            625
P01T_active_service_seen_on_buyer_site_invoicing_AP_email    398
P02_active_relationship_finance_accounting_email           471
P03_active_relationship_purchasing_email                   257
P04_active_relationship_general_email (2 part files)      3833
P05_likely_active_awarded_12_36_months_any_email           422
P06_client_listing_invoicing_AP_email                      295
P06T_active_service_seen_on_buyer_site_other_email (24 part files)  74208
P07_client_listing_finance_or_purchasing_email             800
P08_client_listing_general_email (8 part files)          25539
P09_older_contract_or_payment_any_email                    295
P10_linked_from_vendor_site_any_email                     2642
P10R_ca_domain_registration_contract_own_email (38 part files) 100545
P11_any_relationship_email_not_yet_confirmed (6 part files)  17418
P12_weaker_relationship_within_5_years_own_email             7
P13_inferred_relationship_no_record_own_email (7 part files)  17697
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email    125
P06M_member_or_regulated_payer_of_canadian_body_other_email (6 part files)  13084
Z_no_email_yet_not_delivered (2 part files)               7338
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 29231801
package files: compressed (.csv.gz); packages written straight from the table (already in order): 17 of 19; sorted from a working copy: P11 (17418 rows); sorted from a working copy: Z (7338 rows)

# coverage vs the downstream targets (COVERAGE_VS_TARGETS.md)
benchmarks met 94 / 446 (21.1%); near 57; written out/ranked/COVERAGE_VS_TARGETS.md
  gap buyer_ap_cycle_published           P10R       0.0% ->  20%  rows needed 20082
  gap ap_system_hint                     P10R       0.2% ->  20%  rows needed 19909
  gap buyer_tax_exempt_status            P10R       0.0% ->  15%  rows needed 15055
  gap buyer_esignature_preference        P10R       0.0% ->  15%  rows needed 15035
  gap buyer_ap_cycle_published           P06T       0.0% ->  20%  rows needed 14816
  gap buyer_payment_method_preference    P10R       0.6% ->  15%  rows needed 14445
  gap vendor_registered_address          P08       13.6% ->  70%  rows needed 14401
  gap ap_system_hint                     P06T       0.6% ->  20%  rows needed 14371
  gap vendor_phone                       P11        4.5% ->  75%  rows needed 12273
  gap vendor_emails                      P11        3.4% ->  70%  rows needed 11601
  gap buyer_esignature_preference        P06T       0.2% ->  15%  rows needed 10990
  gap buyer_tax_exempt_status            P06T       0.3% ->  15%  rows needed 10939
  gap buyer_payment_method_preference    P06T       0.6% ->  15%  rows needed 10674
  gap contract_value                     P11        0.5% ->  60%  rows needed 10366
  gap award_or_notice_id                 P11        0.5% ->  60%  rows needed 10365
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
