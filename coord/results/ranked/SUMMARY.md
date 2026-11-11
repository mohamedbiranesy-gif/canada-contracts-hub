# Ranked buyers — 2026-11-11T14:02Z

```
[   21s +  21s  1.9G] mailboxes taken from the verification log (better than org_mailboxes' single pick): 808 | referee mailbox rows whose last label is not a top-level domain: {'left out': 15, 'cut back to the address the page prints': 62}
[   33s +  12s  0.8G] vendor table: registry matches not used because the legal form differs (partnership vs corporation): 55 | 'websites' that are a web host's own site (dropped with their mailboxes): 6 | websites not used for a look-up by domain (unverified, name does not fit): 0 | look-ups by domain: 8050
[   33s +   0s  0.8G] team vendor contacts (referee-verified): 8782 vendors; 172 with a billing / AR mailbox
[  210s + 177s  2.2G] same-pair fill (facts from another record of the same buyer-vendor pair): {'solicitation_or_tender_number': 11, 'number_of_bids': 10, 'award_or_notice_id': 2, 'buyer_vendor_id': 2, 'commodity_codes': 9, 'end_date_inferred': 120, 'contract_value': 7, 'procurement_method': 3, 'po_number_as_published': 3, 'buyer_org_codes': 1, 'start_from_signed': 497, 'end_date': 3, 'contract_description': 2, 'contract_or_agreement_number': 2, 'contract_title': 1}
[  210s +   0s  2.2G] contract records whose vendor's registry match pairs a partnership with a corporation (registry cells not used): 2244
[  234s +  24s  3.9G] tenant leads from the shards: 31733
[  234s +   0s  3.9G] leads: 699270 (596547 from the cloud row factory; 64 websites from the lead site finder)
[  276s +  42s  4.3G] registry leads (.ca domains carrying a confirmed mailbox of their own organisation): 152415
[  277s +   0s  4.3G] organisations' second domain names (the name on file answers at their site under another domain): 19827 {'no confirmed mailbox on the site that answers (yet)': 9810, 'registry lead for a .ca name whose site lives under another ending': 3549, '.ca name answering at another .ca site (that site has its own registry lead)': 3495, 'lead of another lane: its site is the one that answers': 2899, 'the site answers for more than 30 names (a hub): left out': 72}
[  324s +  47s  4.6G] lead rows: facts from the buyer's own pages / the vendor's link label: {'buyer_address_from_own_page': 144739, 'buyer_name_from_own_home_page': 131294, 'facts of another host of the domain not taken': 345, 'vendor_address_cut_out_of_its_quote': 40491, 'buyer_legal_name_from_register': 10925, 'buyer_address_from_member_directory': 6187, 'buyer_name_from_vendor_link_label': 2732} | sites named again from their stored home-page title: 1146
[  324s +   0s  4.6G] client-page links judged (cloud row factory): {'client listing: label names the site': 4566, 'link only, and the site has a .ca registration: the registration takes the row': 1786, "not shown to be a client: the link's label does not name the linked site": 1764, "client listing: 'visit website' on a client page": 455, 'client listing: portfolio page': 310, 'client listing: page address names the site': 228, 'not shown to be a client: a page for clients (forms, resources, login), not a list of them': 204, "not shown to be a client: an organisation's 'our work' programme page": 184, "not shown to be a client: sister site of the page's owner": 104, 'the same organisation on both sides (a firm that is its own agent of record): no row': 84, 'not shown to be a client: article: the client word sits in a slug of 4 words': 63, 'not shown to be a client: dated article': 18, 'not shown to be a client: article: the client word sits in a slug of 5 words': 14, 'not shown to be a client: article: the client word sits in a slug of 6 words': 1}
[  333s +   9s  4.6G] leads with a borrowed mailbox: 121416 | rows upgraded by a newer dated record: 43 | rows upgraded to an active service seen on the buyer's site: 484
[  347s +  14s  4.6G] P12 organisations: 90 added: 8 {'no own confirmed mailbox': 64, 'same organisation already in a row': 18} | P13 added: 18362 | P13 skipped: {"mailbox not the organisation's own": 2338, 'bad mailbox': 271, 'not located in Canada (no honest inference)': 17853, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 81160, '… of which by the NAME alone (its own mailbox and domain are in no row)': 136}
[  347s +   0s  4.6G] lead rows that took the organisation's own key (registry facts attach): {'rows': 45248, 'buyer_address': 4723, 'buyer_name': 3484}
[  378s +  31s  4.7G] extras from the lanes' result rows: {'invoice_mailing_address': 2331, 'invoicing_requirements': 2134, 'ap_phone': 2426, 'invoice_portal_url': 73, 'ap_contact_name': 286}
[  395s +  18s  4.7G] words too common to prove a name (in more than 1 in 2,000 of the 261375 names of organisations whose site was read): 531; names printed on 3+ sites: 1767
[  458s +  62s  4.7G] org_extras: 265267 organisations read; filled {'vendor_logo': 93535, 'vendor_phone_v2': 66776, 'po_required': 276, 'buyer_phone_v2': 123307, 'buyer_logo': 223630, 'vendor_trading_name_jsonld': 15444, 'buyer_legal_name': 99614, 'buyer_payment_method_preference_mention_rejected': 18243, 'payment_terms': 1079, 'buyer_tax_exempt_status_mention_rejected': 361, 'buyer_legal_name_v3_spelled_by_the_domain': 24738, 'buyer_legal_name_v2_legal_name_stated': 20859, "vendor site is a foreign organisation's: its legal / trading name not taken for the Canada-located vendor": 1580, 'buyer_bn': 3781, 'buyer_legal_name_v2_rejected_no_overlap': 55228, 'buyer_legal_name_v2_jsonld_name': 5850, 'buyer_legal_name_v2_printed_on_many_sites': 7242, 'buyer_legal_name_v2_jsonld_legal_name': 6528, 'ap_system_hint_links': 570, 'buyer_legal_name_government_template_credit': 40, 'buyer_payment_method_preference_mention': 1563, 'vendor_legal_name': 15678, 'vendor_legal_name_v3_spelled_by_the_domain': 7398, 'vendor_neq': 152, 'buyer_esignature_preference_mention_rejected': 560, 'vendor_legal_name_v2': 11785, 'buyer_address_v2': 8847, 'invoice_portal_links': 85, 'buyer_ap_cycle_published_mention': 70, 'buyer_legal_name_v3_stated_as_operator': 1661, 'p13_name_from_legal_name': 15344, "vendor named by its own site's name instead of its domain": 19699, 'buyer_esignature_preference_mention': 96, 'buyer_legal_name_v2_jsonld_name_own_site_node': 596, 'vendor_legal_name_v3_legal_person_behind_the_site_name': 1111, 'vendor_bn': 826, 'buyer_legal_name_v3_legal_person_behind_the_site_name': 1616, 'vendor_legal_name_v2_site_says': 999, 'buyer_tax_exempt_status_mention': 159, 'vendor_bn_jsonld': 76, 'buyer_bn_jsonld': 182, 'buyer_legal_name_v2_jsonld_legal_name_own_site_node': 395, 'buyer_legal_name_kept_from_the_trademarks_register': 2867, 'vendor_address_v2': 323, 'vendor_address_v2_outside_canada_not_taken': 119, 'vendor_legal_name_v3_stated_as_operator': 69, 'buyer_legal_name_v2_stated_as_operator': 58, 'vendor_qst': 16, 'buyer_ap_cycle_published_mention_rejected': 32, 'buyer_legal_name_v2_doing_business_as': 9, 'buyer_legal_name_franchisor_copyright_not_taken': 12}
[  458s +   0s  4.7G] regional mailboxes of multinationals removed from other-country entities: 57
[  459s +   1s  4.7G] mx_check: 69559 domains known; 186 mailboxes on domains with no mail server removed; 876 webmail (freemail) addresses removed
[  463s +   4s  5.0G] dmarc/spf: 290603 domains known; rows {'enforced': 51650, 'exposed': 211306}
[  463s +   0s  5.0G] same organisation under another key folded into the row that holds its mailbox: 52
[  467s +   4s  5.0G] second mailbox of the same organisation (same site and mail domain, same name family) folded: 6
[  473s +   6s  5.2G] org_contacts: 242726 organisations read; filled {'vendor_phone': 73698, 'vendor_emails': 45725, 'buyer_phone': 133685, 'vendor site prints an address outside Canada: address and telephone not taken': 1312, 'buyer_address': 19120, 'vendor_address': 1986}
[  473s +   0s  5.2G] site-reader records read on another host of the row's domain (look-ups): {'org_extras: not taken': 691, 'org_contacts: not taken': 1368, 'org_contacts: taken, read on another host for the same organisation (same name)': 358, 'org_extras: taken, read on another host for the same organisation (same name)': 84, "org_contacts: taken, the row's host is the member directory of the body whose own site was read": 995, "org_extras: taken, the row's host is the member directory of the body whose own site was read": 198}
[  484s +  11s  5.8G] ap_terms (evidence pages re-read): 82907 keys read, 106812 pages used across rows; filled {'payment_terms': 3381, 'po_required': 1848, 'payment_method': 689, 'ap_cycle': 105, 'tax_exempt': 990, 'portal': 1936, 'format': 730, 'context': 45765, 'esignature': 595, 'ap_system_portal': 1679, 'ap_phone': 1094, 'buyer_bn': 52, 'ap_contact_name': 817, 'address': 549, 'mailbox_gone': 336, 'ap_system': 433, 'setup_url': 312, 'buyer_phone_from_page': 7438, 'buyer_address_from_page': 412}
[  486s +   2s  5.7G] peppol: 77 Canadian participants; matched buyers 9, vendors 39
[  486s +   0s  5.7G] directories: 2338 entries reachable by their own site; 112 sites given by entries of different names, left out
[  489s +   2s  5.7G] municipal / organisation directories: {'matched': 1753, 'legal_name': 714, 'phone': 293, 'address': 44, 'matched_by_place_name': 12, 'website': 19}
[  489s +   0s  5.7G] charity buyers: {'matched': 9410, 'bn': 7602, 'legal_name': 6161, 'address': 553, 'website': 32}
[  490s +   1s  5.8G] charity registration numbers found in the CRA list: {'matched': 1083, 'legal_name': 656, 'address': 89, 'name_from_the_register': 98, 'holder is a foundation / trust under another name: reported only': 40} | list: 83761
[  492s +   2s  5.9G] wikidata: {'vendors': 1361, 'buyers': 5178, 'buyer_legal_name': 2036, 'buyer_phone': 81, 'buyer_address': 557, 'buyer_website': 107, 'vendor_legal_name': 43, 'vendor_address': 557, 'vendor_website': 232, 'vendor_neq': 6}
[  493s +   1s  5.9G] crown-corporation BNs applied to inferred-vendor rows: 16665
[  493s +   1s  5.9G] vendor websites confirmed from search proposals: 502 applied: 645 {"search proposal not taken: a directory / quote page / register, or a host that does not carry the vendor's name": 491, 'vetted vendor: the site of its own terms page': 32830}
[  493s +   0s  5.9G] inferred vendors' published phone / address applied: {'phone': 13506}
[  494s +   1s  6.0G] registry bulk rows added (no API row for the key): 22305 | registry rows left out, the registered name is only legal-form and place words: 0
[  496s +   2s  6.0G] Canada's Business Registries + registry open data: 3706 vendors, 28246 buyers found; filled {'buyer_bn': 8800, 'buyer_legal_name': 12965, 'vendor_registered_address': 20329, 'vendor_bn9': 34920, 'vendor_registry_status': 20268, 'vendor_incorporation_date': 20570, 'vendor_legal_form': 20275, 'vendor_legal_name': 18701, 'vendor_neq': 7559, 'vendor_trading_name': 178, 'buyer_address': 1877, 'buyer record found under a plain name, another name than the site prints with its legal form: not taken': 295, 'vendor_skipped_legal_form': 1, 'buyer record looked up under a name the row no longer carries, not taken': 9, 'buyer record of another name than the legal person the site itself states, not taken': 59, 'vendor_bn9_other_registry': 4}
[  496s +   0s  6.0G] award facts from the buyers' own award pages: 237 pairs with a page; filled {'contract_value': 39, 'end_date': 17, 'start_date': 9, 'contract_or_agreement_number': 3, 'solicitation_or_tender_number': 6, 'term': 2, 'po_number_as_published': 1, 'number_of_bids': 1}
[  499s +   3s  6.0G] legal names read off a page, tidied: {'tidied': 867, 'fragment': 59, 'owner': 82, "row's own name tidied with it": 157, "row's own name: a clause of the sentence cut off": 2}
[  499s +   0s  6.0G] legal name: the organisation's own name carries its legal form (cells still empty after every register and site statement): 1857
[  500s +   1s  6.0G] legal names from validated certificate subjects (Certificate Transparency): domains on file 3353; {'buyer_legal_name': 79, "subject does not carry the organisation's own name: not taken": 128}
[  500s +   0s  6.0G] grants & contributions recipient BNs: 8183 buyers, 1075 vendors in file; filled {'buyer_bn': 5387, 'buyer_legal_name': 2400, 'vendor_bn9': 4289, 'buyer_bn_conflict_noted': 91}
[  502s +   2s  6.0G] vendor legal name, last links of the chain: {"the vendor's own name carries its legal form": 3210, "the vendor's own terms, read by hand": 27768}
[  504s +   2s  6.0G] vendors that are organisations of this table (same name, same province): facts carried from their own row: {'vendor_phone': 4225, 'vendor_website': 4885, 'vendor_legal_name': 733, 'vendor_bn9': 8}
[  520s +  16s  6.1G] buyers' PO / contract open data joined: {'pairs': 6, 'po_filled': 5, 'contract_filled': 1} | records read: 330978 | kept (a row's own buyer-vendor pair): 179
[  538s +  18s  6.6G] back-references: {'dataset rows with lead relationships': 152451, 'lead rows with dataset history': 61}
[  553s +  15s  6.2G] sensitivity tags: {'corrections / detention': 38, 'health: mental health / addiction / sexual health': 480, 'intelligence / security / defence': 28, 'police service / police board': 104, 'courts / tribunals / legal aid': 94, 'child / youth protection': 29, 'police oversight body': 5, 'shelter / crisis / sexual-assault service': 99, 'coroner / medical examiner': 1}
[  563s +  10s  6.2G] site readers, second pass (websites found late): {'buyer_logo': 618, 'vendor_phone': 5788, 'vendor_logo': 53312, 'vendor_emails': 1218, 'vendor_address': 802, 'buyer_address': 5, 'buyer_phone': 46}
[  563s +   0s  6.2G] listings on a site that is not the Canada-located vendor's own (-> tier E): {'kept — the site prints an address in Canada': 6571, "kept — Wikidata: the site's organisation has its headquarters in Canada": 1481, 'kept — no evidence about whose site it is': 739, "the site's own address is outside Canada": 203, 'from tier D': 837, "Wikidata: the site's organisation has its headquarters outside Canada": 495, "kept — the listing is in the site's Canadian section (/ca/, /en-ca/, ca.…)": 48, 'Canadian arm of a group, site not shown to be its own': 26, "kept although the site reader's address is abroad (Wikidata: headquarters in Canada)": 40, "the vendor's published terms: its Canadian entity does not contract with customers of this buyer's country": 113, "kept — address abroad on the site, but a corporation of the site's name is registered in Canada": 11}
[  567s +   3s  6.2G] same-vendor carry-over (BN9, identity facts and address from the vendor's other rows): {'address': 138, 'bn9': 101070, 'legal_name': 101066, 'trading_name': 101056, 'gst_hst_derived': 101070, 'phone': 14, 'emails': 11, 'logo_url': 14, 'registry_id': 101051, 'registry_url': 101051, 'registered_address': 101051, 'legal_form': 101051, 'registry_status': 101051, 'registry_match_level': 101053, 'incorporation_date': 101051}
[  716s + 149s  6.1G] rows written: 100000 of 266126
[  860s + 144s  5.9G] rows written: 200000 of 266126
[  954s +  94s  5.9G] narrative columns: {'mailbox meta found': 257527, 'contract_description_from_title': 185091, 'contract_title_from_description': 142, 'invoice_reference_hint_po_rule': 1123, 'records_with_this_vendor_lead': 243131, 'date written day-month: put in order': 532, 'mailbox meta missing': 1305, 'buyer name: the page-title opening (Welcome to …) removed': 314, 'buyer named by a menu word (About, Home …): its domain name instead': 350}
[  954s +   0s  5.9G] recurring billing (owner's bar of 2026-11-11: billed monthly or every three months, systematically, by the vendor) — rows with a mailbox:
[  954s +   0s  5.9G]   1 monthly                31311   T 31311
[  954s +   0s  5.9G]   2 monthly or yearly      27417   D 332 · M 13 · T 27072
[  954s +   0s  5.9G]   3 yearly or longer      121278   A 4 · B 347 · D 2248 · L 1 · M 11195 · R 100816 · T 6667
[  954s +   0s  5.9G]   4 per transaction          161   M 161
[  954s +   0s  5.9G]   5 not published          78665   A 1272 · B 1374 · C 315 · D 24315 · E 5109 · F 7 · I 17623 · L 434 · M 2057 · T 26159
[  954s +   0s  5.9G]   rows that meet the bar as published (1 monthly + 1 quarterly): 31311 of 258832 rows with a mailbox | Shopify rows by the store's country: US 17098, CA 9134, country not read 289
[  954s +   0s  5.9G]   the bill's fields, rows with a mailbox that carry each: bill_amount_indicative 60591, bill_amount_basis 60591, bill_items_as_published 127169, bill_currency_as_published 49605, bill_delivery_as_published 26353, bill_payment_method_as_published 133328, bill_tax_rule_as_published 26353, bill_identifier_format 26353, service_stops_if_unpaid 135610, relationship_fact_basis 258832
[  954s +   0s  5.9G] invoice fields (owner 2026-11-11: every aspect within an invoice) — rows with a mailbox that carry each, of 258832: buyer legal name 125105 (48%) · buyer address 189155 (73%) · vendor legal name 217015 (84%) · vendor address 257675 (100%) · vendor tax number 158333 (61%) · what is billed 208962 (81%) · amount 67654 (26%) · billing period 180167 (70%) · reference 175656 (68%) · all but the amount 31444 (12%) · all nine 1649 (1%)
[  954s +   0s  5.9G]   rows by number of the nine fields, tier by tier: A: 9×3 8×708 7×500 6×51 5×10 4×4 | B: 9×1 8×310 7×351 6×345 5×377 4×210 3×88 | C: 8×113 7×143 6×36 5×15 4×6 3×2 | D: 7×31 6×698 5×2509 4×6609 3×9618 | E: 7×27 6×438 5×789 4×1187 3×1271 | F: 8×2 7×4 6×1 | I: 6×24 5×6956 4×4607 3×5421 | L: 8×37 7×70 6×129 5×120 4×53 3×22 | M: 8×4158 7×3236 6×3870 5×1159 4×868 3×71 | R: 8×29749 7×42053 6×29014 | T: 9×1645 8×22912 7×24102 6×18440 5×14704 4×7218 3×2167
[  954s +   0s  5.9G] downstream pack: {'tax_derived_foreign': 30708, 'pay_on_sight_yes': 2441, 'ap_payable_today': 2460, 'ship_ready_yes': 1054, 'buyer_trade_name_as_published': 197241, 'tax_derived': 167841, 'registry_note': 221, 'prompt_payment_default': 830, 'pay_on_sight_no': 171074, 'buyer_type_from_name': 48959, 'sensitivity_extra': 211, 'buyer_address_from_own_page': 1955, 'registry_warning': 1465, 'invoice_currency_derived': 242576, 'pay_on_sight_routed': 85317, 'currency_default': 2}
[  954s +   0s  5.9G] rows 266126
[  954s +   0s  5.9G] [('GOLD', 625), ('A0', 519), ('A1', 712), ('A2', 92), ('A3', 223), ('A4', 8), ('B0', 623), ('B1', 1010), ('B2', 130), ('B3', 186), ('B4', 11), ('C0', 1004), ('C1', 245), ('C2', 18), ('C3', 26), ('C4', 26), ('D0', 604), ('D1', 25774), ('D2', 174), ('D3', 641), ('D4', 306), ('E0', 260), ('E1', 4786), ('E2', 96), ('E3', 123), ('E4', 104), ('F0', 1), ('F1', 3), ('F2', 1), ('F3', 2), ('F4', 1), ('GOLD-M', 126), ('GOLD-T', 398), ('I0', 739), ('I1', 17222), ('I2', 60), ('I3', 241), ('I4', 100), ('L0', 217), ('L1', 312), ('L2', 33), ('L3', 20), ('L4', 70), ('M0', 230), ('M1', 13061), ('M2', 58), ('M3', 180), ('M4', 1), ('R0', 234), ('R1', 99541), ('R2', 92), ('R3', 1003), ('R4', 180), ('T0', 2863), ('T1', 89452), ('T2', 195), ('T3', 1144), ('T4', 20)]
[  954s +   0s  5.9G] with any email: 258832 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            625
P01T_active_service_seen_on_buyer_site_invoicing_AP_email    398
P02_active_relationship_finance_accounting_email           471
P03_active_relationship_purchasing_email                   257
P04_active_relationship_general_email (2 part files)      3823
P05_likely_active_awarded_12_36_months_any_email           422
P06_client_listing_invoicing_AP_email                      295
P06T_active_service_seen_on_buyer_site_other_email (27 part files)  75065
P07_client_listing_finance_or_purchasing_email             793
P08_client_listing_general_email (8 part files)          25303
P09_older_contract_or_payment_any_email                    295
P10_linked_from_vendor_site_any_email                     2633
P10R_ca_domain_registration_contract_own_email (42 part files)  99941
P11_any_relationship_email_not_yet_confirmed (7 part files)  17455
P12_weaker_relationship_within_5_years_own_email             7
P13_inferred_relationship_no_record_own_email (7 part files)  17623
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email    126
P06M_member_or_regulated_payer_of_canadian_body_other_email (6 part files)  13201
Z_no_email_yet_not_delivered (2 part files)               7393
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 30818406
package files: compressed (.csv.gz); packages written straight from the table (already in order): 17 of 19; sorted from a working copy: P11 (17455 rows); sorted from a working copy: Z (7393 rows)

# coverage vs the downstream targets (COVERAGE_VS_TARGETS.md)
benchmarks met 95 / 446 (21.3%); near 68; written out/ranked/COVERAGE_VS_TARGETS.md
  gap buyer_ap_cycle_published           P10R       0.0% ->  20%  rows needed 19960
  gap ap_system_hint                     P10R       0.2% ->  20%  rows needed 19786
  gap buyer_ap_cycle_published           P06T       0.0% ->  20%  rows needed 14987
  gap buyer_tax_exempt_status            P10R       0.0% ->  15%  rows needed 14964
  gap buyer_esignature_preference        P10R       0.0% ->  15%  rows needed 14944
  gap ap_system_hint                     P06T       0.6% ->  20%  rows needed 14552
  gap buyer_payment_method_preference    P10R       0.7% ->  15%  rows needed 14323
  gap vendor_registered_address          P08       13.7% ->  70%  rows needed 14259
  gap vendor_phone                       P11        4.4% ->  75%  rows needed 12319
  gap vendor_emails                      P11        3.4% ->  70%  rows needed 11618
  gap buyer_esignature_preference        P06T       0.2% ->  15%  rows needed 11120
  gap buyer_tax_exempt_status            P06T       0.3% ->  15%  rows needed 11070
  gap buyer_payment_method_preference    P06T       0.6% ->  15%  rows needed 10783
  gap contract_value                     P11        0.5% ->  60%  rows needed 10388
  gap award_or_notice_id                 P11        0.5% ->  60%  rows needed 10387
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
