# Ranked buyers — 2026-11-11T04:48Z

```
[   24s +  24s  1.6G] mailboxes taken from the verification log (better than org_mailboxes' single pick): 786 | referee mailbox rows whose last label is not a top-level domain: {'left out': 15, 'cut back to the address the page prints': 62}
[   40s +  16s  0.7G] vendor table: registry matches not used because the legal form differs (partnership vs corporation): 55 | 'websites' that are a web host's own site (dropped with their mailboxes): 6 | websites not used for a look-up by domain (unverified, name does not fit): 0 | look-ups by domain: 8050
[   40s +   0s  0.7G] team vendor contacts (referee-verified): 8782 vendors; 172 with a billing / AR mailbox
[  292s + 252s  2.1G] same-pair fill (facts from another record of the same buyer-vendor pair): {'solicitation_or_tender_number': 11, 'number_of_bids': 10, 'award_or_notice_id': 2, 'buyer_vendor_id': 2, 'commodity_codes': 9, 'end_date_inferred': 120, 'contract_value': 7, 'procurement_method': 3, 'po_number_as_published': 3, 'buyer_org_codes': 1, 'start_from_signed': 497, 'end_date': 3, 'contract_description': 2, 'contract_or_agreement_number': 2, 'contract_title': 1}
[  292s +   0s  2.1G] contract records whose vendor's registry match pairs a partnership with a corporation (registry cells not used): 2244
[  305s +  13s  3.3G] tenant leads from the shards: 20143
[  305s +   0s  3.3G] leads: 539458 (448325 from the cloud row factory; 64 websites from the lead site finder)
[  350s +  44s  3.5G] registry leads (.ca domains carrying a confirmed mailbox of their own organisation): 148819
[  394s +  45s  3.8G] lead rows: facts from the buyer's own pages / the vendor's link label: {'buyer_address_from_own_page': 128102, 'buyer_name_from_own_home_page': 123319, 'facts of another host of the domain not taken': 293, 'vendor_address_cut_out_of_its_quote': 31066, 'buyer_legal_name_from_register': 9247, 'buyer_address_from_member_directory': 6192, 'buyer_name_from_vendor_link_label': 2801} | sites named again from their stored home-page title: 1144
[  394s +   0s  3.8G] client-page links judged (cloud row factory): {'client listing: label names the site': 4634, "not shown to be a client: the link's label does not name the linked site": 1739, 'link only, and the site has a .ca registration: the registration takes the row': 1712, "client listing: 'visit website' on a client page": 448, 'client listing: portfolio page': 315, 'client listing: page address names the site': 227, 'not shown to be a client: a page for clients (forms, resources, login), not a list of them': 202, "not shown to be a client: an organisation's 'our work' programme page": 187, "not shown to be a client: sister site of the page's owner": 102, 'not shown to be a client: article: the client word sits in a slug of 4 words': 65, 'not shown to be a client: dated article': 19, 'not shown to be a client: article: the client word sits in a slug of 5 words': 14, 'not shown to be a client: article: the client word sits in a slug of 6 words': 1}
[  402s +   8s  3.8G] leads with a borrowed mailbox: 117279 | rows upgraded by a newer dated record: 44 | rows upgraded to an active service seen on the buyer's site: 499
[  421s +  19s  3.9G] P12 organisations: 90 added: 8 {'no own confirmed mailbox': 64, 'same organisation already in a row': 18} | P13 added: 18547 | P13 skipped: {"mailbox not the organisation's own": 2275, 'bad mailbox': 189, 'not located in Canada (no honest inference)': 15269, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 72993, '… of which by the NAME alone (its own mailbox and domain are in no row)': 127}
[  421s +   0s  3.9G] lead rows that took the organisation's own key (registry facts attach): {'rows': 45128, 'buyer_address': 4949, 'buyer_name': 3599}
[  457s +  35s  3.9G] extras from the lanes' result rows: {'invoice_mailing_address': 2318, 'invoicing_requirements': 2121, 'ap_phone': 2415, 'invoice_portal_url': 73, 'ap_contact_name': 275}
[  477s +  20s  4.0G] words too common to prove a name (in more than 1 in 2,000 of the 227685 names of organisations whose site was read): 529; names printed on 3+ sites: 1596
[  548s +  71s  4.0G] org_extras: 230575 organisations read; filled {'vendor_logo': 82270, 'vendor_phone_v2': 59567, 'po_required': 263, 'vendor_trading_name_jsonld': 12642, 'buyer_legal_name': 71562, 'buyer_phone_v2': 106497, 'buyer_payment_method_preference_mention_rejected': 18158, 'buyer_logo': 192226, 'payment_terms': 927, 'buyer_tax_exempt_status_mention_rejected': 333, 'buyer_legal_name_v2_legal_name_stated': 19684, "vendor site is a foreign organisation's: its legal / trading name not taken for the Canada-located vendor": 1322, 'buyer_bn': 3421, 'buyer_legal_name_v2_rejected_no_overlap': 53024, 'buyer_legal_name_v2_jsonld_name': 7005, 'buyer_legal_name_v2_printed_on_many_sites': 7698, 'buyer_legal_name_v2_jsonld_legal_name': 7140, 'ap_system_hint_links': 505, 'buyer_legal_name_government_template_credit': 40, 'buyer_payment_method_preference_mention': 1380, 'vendor_legal_name': 14488, 'vendor_neq': 145, 'buyer_esignature_preference_mention_rejected': 537, 'vendor_legal_name_v2': 10744, 'invoice_portal_links': 75, 'buyer_ap_cycle_published_mention': 55, 'vendor_legal_name_v3_stated_as_operator': 82, 'buyer_address_v2': 7405, 'buyer_legal_name_v3_stated_as_operator': 1885, 'p13_name_from_legal_name': 12328, 'buyer_esignature_preference_mention': 84, 'buyer_legal_name_v3_legal_person_behind_the_site_name': 1874, 'buyer_legal_name_v2_jsonld_legal_name_own_site_node': 435, 'buyer_legal_name_v2_jsonld_name_own_site_node': 520, 'vendor_legal_name_v3_legal_person_behind_the_site_name': 1196, 'vendor_bn': 755, 'vendor_legal_name_v2_site_says': 853, 'buyer_tax_exempt_status_mention': 125, 'vendor_bn_jsonld': 71, 'buyer_bn_jsonld': 167, 'buyer_legal_name_kept_from_the_trademarks_register': 1057, 'vendor_address_v2': 302, 'vendor_address_v2_outside_canada_not_taken': 114, 'buyer_legal_name_v2_stated_as_operator': 59, 'vendor_qst': 19, 'buyer_ap_cycle_published_mention_rejected': 32, 'buyer_legal_name_franchisor_copyright_not_taken': 11, 'buyer_legal_name_v2_doing_business_as': 11, 'p13_name_from_domain': 1}
[  548s +   0s  4.0G] regional mailboxes of multinationals removed from other-country entities: 50
[  549s +   1s  4.0G] mx_check: 69559 domains known; 185 mailboxes on domains with no mail server removed; 833 webmail (freemail) addresses removed
[  553s +   5s  4.2G] dmarc/spf: 255097 domains known; rows {'enforced': 48112, 'exposed': 194063}
[  554s +   0s  4.3G] same organisation under another key folded into the row that holds its mailbox: 52
[  558s +   5s  4.3G] second mailbox of the same organisation (same site and mail domain, same name family) folded: 6
[  565s +   7s  4.5G] org_contacts: 217822 organisations read; filled {'vendor_phone': 66569, 'vendor_emails': 41364, 'buyer_phone': 118996, 'vendor site prints an address outside Canada: address and telephone not taken': 1059, 'buyer_address': 18449, 'vendor_address': 1947}
[  565s +   0s  4.5G] site-reader records read on another host of the row's domain (look-ups): {'org_extras: not taken': 792, 'org_contacts: not taken': 1283, 'org_contacts: taken, read on another host for the same organisation (same name)': 128, 'org_extras: taken, read on another host for the same organisation (same name)': 60, "org_contacts: taken, the row's host is the member directory of the body whose own site was read": 763, "org_extras: taken, the row's host is the member directory of the body whose own site was read": 200}
[  576s +  11s  5.0G] ap_terms (evidence pages re-read): 82907 keys read, 108210 pages used across rows; filled {'payment_terms': 3486, 'po_required': 1871, 'payment_method': 695, 'ap_cycle': 107, 'tax_exempt': 1000, 'portal': 1957, 'format': 737, 'context': 45789, 'esignature': 603, 'ap_system_portal': 1698, 'ap_phone': 1104, 'buyer_bn': 52, 'ap_contact_name': 828, 'address': 551, 'mailbox_gone': 336, 'ap_system': 437, 'setup_url': 318, 'buyer_phone_from_page': 9494, 'buyer_address_from_page': 614}
[  579s +   3s  5.0G] peppol: 77 Canadian participants; matched buyers 7, vendors 39
[  579s +   0s  5.0G] directories: 2338 entries reachable by their own site; 112 sites given by entries of different names, left out
[  582s +   3s  5.0G] municipal / organisation directories: {'matched': 1752, 'legal_name': 779, 'phone': 323, 'address': 47, 'matched_by_place_name': 12, 'website': 19}
[  582s +   0s  5.0G] charity buyers: {'matched': 9544, 'bn': 7817, 'legal_name': 6423, 'address': 614, 'website': 32}
[  583s +   1s  5.1G] charity registration numbers found in the CRA list: {'matched': 901, 'legal_name': 557, 'address': 75, 'name_from_the_register': 91, 'holder is a foundation / trust under another name: reported only': 34} | list: 83761
[  585s +   2s  5.1G] wikidata: {'vendors': 1145, 'buyers': 5214, 'buyer_legal_name': 2249, 'buyer_phone': 90, 'buyer_address': 617, 'buyer_website': 107, 'vendor_legal_name': 42, 'vendor_address': 405, 'vendor_website': 233, 'vendor_neq': 7}
[  586s +   1s  5.1G] crown-corporation BNs applied to inferred-vendor rows: 16855
[  586s +   0s  5.1G] vendor websites confirmed from search proposals: 502 applied: 644 {"search proposal not taken: a directory / quote page / register, or a host that does not carry the vendor's name": 485, 'vetted vendor: the site of its own terms page': 24388}
[  586s +   0s  5.1G] inferred vendors' published phone / address applied: {'phone': 13618}
[  587s +   1s  5.2G] registry bulk rows added (no API row for the key): 22305 | registry rows left out, the registered name is only legal-form and place words: 0
[  589s +   2s  5.2G] Canada's Business Registries + registry open data: 3706 vendors, 28246 buyers found; filled {'buyer_bn': 8989, 'buyer_legal_name': 13555, 'vendor_registered_address': 16136, 'vendor_bn9': 25960, 'vendor_legal_name': 16072, 'vendor_registry_status': 16074, 'vendor_incorporation_date': 16353, 'vendor_legal_form': 16081, 'vendor_neq': 4610, 'vendor_trading_name': 244, 'buyer_address': 1985, 'vendor_skipped_legal_form': 1, 'buyer record of another name than the legal person the site itself states, not taken': 132, 'buyer record looked up under a name the row no longer carries, not taken': 8, 'vendor_bn9_other_registry': 4}
[  589s +   0s  5.2G] award facts from the buyers' own award pages: 237 pairs with a page; filled {'contract_value': 39, 'end_date': 17, 'start_date': 9, 'contract_or_agreement_number': 3, 'solicitation_or_tender_number': 6, 'term': 2, 'po_number_as_published': 1, 'number_of_bids': 1}
[  591s +   2s  5.2G] legal names read off a page, tidied: {'tidied': 578, 'owner': 71, 'fragment': 47}
[  592s +   1s  5.2G] legal name: the organisation's own name carries its legal form (cells still empty after every register and site statement): 3781
[  592s +   0s  5.2G] grants & contributions recipient BNs: 8183 buyers, 1075 vendors in file; filled {'buyer_bn': 5571, 'buyer_legal_name': 2568, 'vendor_bn9': 4018, 'buyer_bn_conflict_noted': 92}
[  594s +   2s  5.2G] vendor legal name, last links of the chain: {"the vendor's own name carries its legal form": 3441, "the vendor's own terms, read by hand": 11608}
[  614s +  20s  5.3G] buyers' PO / contract open data joined: {'pairs': 5, 'po_filled': 4, 'contract_filled': 1} | records read: 330978 | kept (a row's own buyer-vendor pair): 143
[  631s +  17s  5.7G] back-references: {'dataset rows with lead relationships': 147792, 'lead rows with dataset history': 61}
[  648s +  17s  5.4G] sensitivity tags: {'corrections / detention': 37, 'health: mental health / addiction / sexual health': 450, 'intelligence / security / defence': 25, 'police service / police board': 101, 'courts / tribunals / legal aid': 86, 'child / youth protection': 29, 'police oversight body': 5, 'shelter / crisis / sexual-assault service': 95, 'coroner / medical examiner': 1}
[  659s +  11s  5.4G] site readers, second pass (websites found late): {'buyer_logo': 595, 'vendor_phone': 5346, 'vendor_logo': 39960, 'vendor_emails': 1169, 'vendor_address': 830, 'buyer_address': 5, 'buyer_phone': 46}
[  659s +   1s  5.4G] listings on a site that is not the Canada-located vendor's own (-> tier E): {'kept — the site prints an address in Canada': 5936, "kept — Wikidata: the site's organisation has its headquarters in Canada": 1478, 'kept — no evidence about whose site it is': 1492, "the site's own address is outside Canada": 178, 'from tier D': 811, "Wikidata: the site's organisation has its headquarters outside Canada": 489, "kept — the listing is in the site's Canadian section (/ca/, /en-ca/, ca.…)": 47, 'Canadian arm of a group, site not shown to be its own': 31, "kept although the site reader's address is abroad (Wikidata: headquarters in Canada)": 38, "the vendor's published terms: its Canadian entity does not contract with customers of this buyer's country": 113, "kept — address abroad on the site, but a corporation of the site's name is registered in Canada": 11}
[  663s +   3s  5.4G] same-vendor carry-over (BN9, identity facts and address from the vendor's other rows): {'address': 127, 'bn9': 98234, 'legal_name': 98231, 'trading_name': 98232, 'gst_hst_derived': 98234, 'registry_id': 98226, 'registry_url': 98226, 'registered_address': 98226, 'legal_form': 98226, 'registry_status': 98226, 'registry_match_level': 98227, 'incorporation_date': 98226, 'phone': 3, 'logo_url': 4, 'neq': 1}
[  829s + 166s  5.3G] rows written: 100000 of 246898
[  989s + 160s  5.2G] rows written: 200000 of 246898
[ 1066s +  77s  4.9G] narrative columns: {'mailbox meta found': 239284, 'contract_description_from_title': 173875, 'contract_title_from_description': 142, 'invoice_reference_hint_po_rule': 1132, 'records_with_this_vendor_lead': 223718, 'mailbox meta missing': 1342}
[ 1066s +   0s  4.9G] downstream pack: {'tax_derived_foreign': 22846, 'pay_on_sight_yes': 2333, 'ap_payable_today': 2203, 'ship_ready_yes': 1000, 'buyer_trade_name_as_published': 178190, 'tax_derived': 158670, 'registry_note': 220, 'prompt_payment_default': 775, 'pay_on_sight_no': 159704, 'buyer_type_from_name': 35235, 'sensitivity_extra': 201, 'buyer_address_from_own_page': 3003, 'registry_warning': 1397, 'invoice_currency_derived': 225455, 'pay_on_sight_routed': 78589, 'currency_default': 2}
[ 1066s +   0s  4.9G] rows 246898
[ 1066s +   0s  4.9G] [('GOLD', 625), ('A0', 519), ('A1', 712), ('A2', 92), ('A3', 223), ('A4', 8), ('B0', 624), ('B1', 1006), ('B2', 131), ('B3', 186), ('B4', 11), ('C0', 1004), ('C1', 245), ('C2', 18), ('C3', 26), ('C4', 26), ('D0', 558), ('D1', 26086), ('D2', 173), ('D3', 649), ('D4', 309), ('E0', 246), ('E1', 4807), ('E2', 95), ('E3', 122), ('E4', 101), ('F0', 1), ('F1', 3), ('F2', 1), ('F3', 2), ('F4', 1), ('GOLD-M', 106), ('GOLD-T', 366), ('I0', 731), ('I1', 17415), ('I2', 60), ('I3', 238), ('I4', 103), ('L0', 216), ('L1', 314), ('L2', 33), ('L3', 19), ('L4', 70), ('M0', 208), ('M1', 11021), ('M2', 34), ('M3', 158), ('M4', 1), ('R0', 175), ('R1', 96815), ('R2', 95), ('R3', 963), ('R4', 176), ('T0', 1990), ('T1', 75791), ('T2', 166), ('T3', 1009), ('T4', 15)]
[ 1066s +   0s  4.9G] with any email: 240626 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            625
P01T_active_service_seen_on_buyer_site_invoicing_AP_email    366
P02_active_relationship_finance_accounting_email           470
P03_active_relationship_purchasing_email                   257
P04_active_relationship_general_email (2 part files)      3818
P05_likely_active_awarded_12_36_months_any_email           423
P06_client_listing_invoicing_AP_email                      298
P06T_active_service_seen_on_buyer_site_other_email (22 part files)  65815
P07_client_listing_finance_or_purchasing_email             800
P08_client_listing_general_email (8 part files)          25619
P09_older_contract_or_payment_any_email                    295
P10_linked_from_vendor_site_any_email                     2658
P10R_ca_domain_registration_contract_own_email (36 part files)  97211
P11_any_relationship_email_not_yet_confirmed (5 part files)  12828
P12_weaker_relationship_within_5_years_own_email             7
P13_inferred_relationship_no_record_own_email (6 part files)  17816
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email    106
P06M_member_or_regulated_payer_of_canadian_body_other_email (5 part files)  11132
Z_no_email_yet_not_delivered (2 part files)               6354
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 27276624
package files: compressed (.csv.gz); packages written straight from the table (already in order): 17 of 19; sorted from a working copy: P11 (12828 rows); sorted from a working copy: Z (6354 rows)

# coverage vs the downstream targets (COVERAGE_VS_TARGETS.md)
benchmarks met 58 / 446 (13.0%); near 90; written out/ranked/COVERAGE_VS_TARGETS.md
  gap buyer_ap_cycle_published           P10R       0.0% ->  20%  rows needed 19417
  gap ap_system_hint                     P10R       0.2% ->  20%  rows needed 19245
  gap vendor_registered_address          P08       12.6% ->  70%  rows needed 14699
  gap buyer_tax_exempt_status            P10R       0.0% ->  15%  rows needed 14552
  gap buyer_esignature_preference        P10R       0.0% ->  15%  rows needed 14535
  gap buyer_payment_method_preference    P10R       0.7% ->  15%  rows needed 13948
  gap buyer_ap_cycle_published           P06T       0.0% ->  20%  rows needed 13140
  gap ap_system_hint                     P06T       0.7% ->  20%  rows needed 12703
  gap buyer_phone                        P08       56.9% ->  95%  rows needed 9759
  gap buyer_esignature_preference        P06T       0.2% ->  15%  rows needed 9730
  gap buyer_tax_exempt_status            P06T       0.3% ->  15%  rows needed 9686
  gap buyer_payment_method_preference    P06T       0.7% ->  15%  rows needed 9439
  gap vendor_bn9                         P08       14.5% ->  50%  rows needed 9105
  gap vendor_phone                       P11        5.6% ->  75%  rows needed 8907
  gap vendor_emails                      P11        4.1% ->  70%  rows needed 8459
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
