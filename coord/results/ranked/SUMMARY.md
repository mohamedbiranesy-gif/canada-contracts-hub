# Ranked buyers — 2026-11-11T15:58Z

```
[   27s +  27s  2.0G] mailboxes taken from the verification log (better than org_mailboxes' single pick): 823 | referee mailbox rows whose last label is not a top-level domain: {'left out': 15, 'cut back to the address the page prints': 61}
[   44s +  17s  0.9G] vendor table: registry matches not used because the legal form differs (partnership vs corporation): 55 | 'websites' that are a web host's own site (dropped with their mailboxes): 6 | websites not used for a look-up by domain (unverified, name does not fit): 0 | look-ups by domain: 8050
[   44s +   0s  0.9G] team vendor contacts (referee-verified): 8782 vendors; 172 with a billing / AR mailbox
[  301s + 257s  2.2G] same-pair fill (facts from another record of the same buyer-vendor pair): {'solicitation_or_tender_number': 11, 'number_of_bids': 10, 'award_or_notice_id': 2, 'buyer_vendor_id': 2, 'commodity_codes': 9, 'end_date_inferred': 120, 'contract_value': 7, 'procurement_method': 3, 'po_number_as_published': 3, 'buyer_org_codes': 1, 'start_from_signed': 497, 'end_date': 3, 'contract_description': 2, 'contract_or_agreement_number': 2, 'contract_title': 1}
[  301s +   0s  2.2G] contract records whose vendor's registry match pairs a partnership with a corporation (registry cells not used): 2244
[  328s +  28s  3.9G] tenant leads from the shards: 34559
[  328s +   0s  3.9G] leads: 702096 (596547 from the cloud row factory; 64 websites from the lead site finder)
[  385s +  56s  4.3G] registry leads (.ca domains carrying a confirmed mailbox of their own organisation): 155471
[  386s +   1s  4.3G] organisations' second domain names (the name on file answers at their site under another domain): 19827 {'registry lead for a .ca name whose site lives under another ending': 6964, 'lead of another lane: its site is the one that answers': 6149, '.ca name answering at another .ca site (that site has its own registry lead)': 6618, 'the site answers for more than 30 names (a hub): left out': 72, 'no confirmed mailbox on the site that answers (yet)': 21}
[  467s +  81s  4.6G] lead rows: facts from the buyer's own pages / the vendor's link label: {'buyer_address_from_own_page': 155460, 'buyer_name_from_own_home_page': 139803, 'facts of another host of the domain not taken': 373, 'vendor_address_cut_out_of_its_quote': 46305, "reference: the account's own address on the vendor's platform": 34694, 'buyer_legal_name_from_register': 10919, 'buyer_address_from_member_directory': 6207, 'buyer_name_from_vendor_link_label': 2782} | sites named again from their stored home-page title: 1146
[  467s +   0s  4.6G] client-page links judged (cloud row factory): {'client listing: label names the site': 4608, 'link only, and the site has a .ca registration: the registration takes the row': 1860, "not shown to be a client: the link's label does not name the linked site": 1817, "client listing: 'visit website' on a client page": 466, 'client listing: portfolio page': 314, 'client listing: page address names the site': 230, 'not shown to be a client: a page for clients (forms, resources, login), not a list of them': 212, "not shown to be a client: an organisation's 'our work' programme page": 188, "not shown to be a client: sister site of the page's owner": 104, 'the same organisation on both sides (a firm that is its own agent of record): no row': 84, 'not shown to be a client: article: the client word sits in a slug of 4 words': 69, 'not shown to be a client: dated article': 18, 'not shown to be a client: article: the client word sits in a slug of 5 words': 15, 'not shown to be a client: article: the client word sits in a slug of 6 words': 1, 'not shown to be a client: sister bodies (names open with the same two words)': 1}
[  478s +  12s  4.7G] leads with a borrowed mailbox: 123024 | rows upgraded by a newer dated record: 43 | rows upgraded to an active service seen on the buyer's site: 477
[  500s +  22s  4.7G] P12 organisations: 90 added: 8 {'no own confirmed mailbox': 64, 'same organisation already in a row': 18} | P13 added: 18127 | P13 skipped: {"mailbox not the organisation's own": 2374, 'bad mailbox': 806, 'not located in Canada (no honest inference)': 19878, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 86849, '… of which by the NAME alone (its own mailbox and domain are in no row)': 135}
[  500s +   0s  4.7G] lead rows that took the organisation's own key (registry facts attach): {'rows': 45337, 'buyer_address': 4722, 'buyer_name': 3512}
[  543s +  43s  4.7G] extras from the lanes' result rows: {'invoice_mailing_address': 2328, 'invoicing_requirements': 2133, 'ap_phone': 2426, 'invoice_portal_url': 73, 'ap_contact_name': 295}
[  566s +  24s  4.8G] words too common to prove a name (in more than 1 in 2,000 of the 261375 names of organisations whose site was read): 531; names printed on 3+ sites: 1767
[  657s +  91s  4.8G] org_extras: 265267 organisations read; filled {'vendor_logo': 102432, 'vendor_phone_v2': 71029, 'po_required': 286, 'buyer_phone_v2': 123417, 'buyer_logo': 223869, 'vendor_trading_name_jsonld': 16409, 'buyer_legal_name': 99726, 'buyer_payment_method_preference_mention_rejected': 18228, 'payment_terms': 1197, 'buyer_tax_exempt_status_mention_rejected': 361, 'buyer_legal_name_v3_spelled_by_the_domain': 24771, 'buyer_legal_name_v2_legal_name_stated': 20850, "vendor site is a foreign organisation's: its legal / trading name not taken for the Canada-located vendor": 1593, 'buyer_bn': 3786, 'buyer_legal_name_v2_rejected_no_overlap': 55240, 'buyer_legal_name_v2_jsonld_name': 5851, 'buyer_legal_name_v2_printed_on_many_sites': 7245, 'buyer_legal_name_v2_jsonld_legal_name': 6528, 'ap_system_hint_links': 569, 'buyer_legal_name_government_template_credit': 40, 'buyer_payment_method_preference_mention': 1563, 'vendor_legal_name': 16811, 'vendor_legal_name_v3_spelled_by_the_domain': 8100, 'vendor_neq': 211, 'buyer_esignature_preference_mention_rejected': 560, 'vendor_legal_name_v2': 12393, 'buyer_address_v2': 8789, 'invoice_portal_links': 85, 'buyer_ap_cycle_published_mention': 70, 'buyer_legal_name_v3_stated_as_operator': 1661, 'p13_name_from_legal_name': 15280, "vendor named by its own site's name instead of its domain": 20997, 'buyer_esignature_preference_mention': 96, 'buyer_legal_name_v2_jsonld_name_own_site_node': 599, 'vendor_legal_name_v3_legal_person_behind_the_site_name': 1168, 'vendor_bn': 836, 'buyer_legal_name_v3_legal_person_behind_the_site_name': 1618, 'vendor_legal_name_v2_site_says': 1122, 'buyer_tax_exempt_status_mention': 159, 'vendor_bn_jsonld': 79, 'buyer_bn_jsonld': 182, 'buyer_legal_name_v2_jsonld_legal_name_own_site_node': 397, 'buyer_legal_name_kept_from_the_trademarks_register': 2839, 'vendor_address_v2': 324, 'vendor_address_v2_outside_canada_not_taken': 118, 'vendor_legal_name_v3_stated_as_operator': 70, 'buyer_legal_name_v2_stated_as_operator': 59, 'vendor_qst': 16, 'buyer_ap_cycle_published_mention_rejected': 32, 'buyer_legal_name_v2_doing_business_as': 9, 'buyer_legal_name_franchisor_copyright_not_taken': 12}
[  657s +   0s  4.8G] regional mailboxes of multinationals removed from other-country entities: 57
[  658s +   1s  4.8G] mx_check: 69559 domains known; 186 mailboxes on domains with no mail server removed; 919 webmail (freemail) addresses removed
[  663s +   6s  5.1G] dmarc/spf: 292278 domains known; rows {'enforced': 54249, 'exposed': 224745}
[  664s +   0s  5.1G] same organisation under another key folded into the row that holds its mailbox: 52
[  669s +   5s  5.1G] second mailbox of the same organisation (same site and mail domain, same name family) folded: 6
[  677s +   8s  5.4G] org_contacts: 242726 organisations read; filled {'vendor_phone': 77976, 'vendor_emails': 49287, 'buyer_phone': 133869, 'vendor site prints an address outside Canada: address and telephone not taken': 1332, 'buyer_address': 18913, 'vendor_address': 1983}
[  677s +   0s  5.4G] site-reader records read on another host of the row's domain (look-ups): {'org_extras: not taken': 700, 'org_contacts: not taken': 1386, 'org_contacts: taken, read on another host for the same organisation (same name)': 356, 'org_extras: taken, read on another host for the same organisation (same name)': 85, "org_contacts: taken, the row's host is the member directory of the body whose own site was read": 1005, "org_extras: taken, the row's host is the member directory of the body whose own site was read": 198}
[  691s +  14s  6.0G] ap_terms (evidence pages re-read): 101012 keys read, 130464 pages used across rows; filled {'payment_terms': 5984, 'po_required': 2397, 'payment_method': 744, 'ap_cycle': 110, 'tax_exempt': 1222, 'portal': 2150, 'format': 816, 'context': 45749, 'esignature': 764, 'ap_system_portal': 1824, 'ap_phone': 1374, 'buyer_bn': 60, 'ap_contact_name': 846, 'address': 654, 'mailbox_gone': 335, 'ap_system': 577, 'setup_url': 388, 'buyer_phone_from_page': 7452, 'buyer_address_from_page': 408}
[  694s +   3s  6.0G] peppol: 77 Canadian participants; matched buyers 9, vendors 39
[  694s +   0s  6.0G] directories: 2338 entries reachable by their own site; 112 sites given by entries of different names, left out
[  697s +   3s  6.0G] municipal / organisation directories: {'matched': 1755, 'legal_name': 716, 'phone': 293, 'address': 44, 'matched_by_place_name': 12, 'website': 19}
[  698s +   1s  6.0G] charity buyers: {'matched': 9374, 'bn': 7575, 'legal_name': 6137, 'address': 552, 'website': 32}
[  699s +   1s  6.1G] charity registration numbers found in the CRA list: {'matched': 1096, 'legal_name': 666, 'address': 90, 'name_from_the_register': 98, 'holder is a foundation / trust under another name: reported only': 40} | list: 83761
[  701s +   2s  6.1G] wikidata: {'vendors': 1366, 'buyers': 5169, 'buyer_legal_name': 2042, 'buyer_phone': 81, 'buyer_address': 552, 'buyer_website': 107, 'vendor_legal_name': 43, 'vendor_address': 561, 'vendor_website': 230, 'vendor_neq': 6}
[  702s +   1s  6.1G] crown-corporation BNs applied to inferred-vendor rows: 16500
[  703s +   1s  6.1G] vendor websites confirmed from search proposals: 502 applied: 645 {"search proposal not taken: a directory / quote page / register, or a host that does not carry the vendor's name": 495, 'vetted vendor: the site of its own terms page': 37293}
[  703s +   0s  6.1G] inferred vendors' published phone / address applied: {'phone': 13387}
[  704s +   1s  6.2G] registry bulk rows added (no API row for the key): 22383 | registry rows left out, the registered name is only legal-form and place words: 0
[  706s +   3s  6.2G] Canada's Business Registries + registry open data: 3706 vendors, 27886 buyers found; filled {'buyer_legal_name': 12784, 'vendor_registered_address': 20913, 'vendor_bn9': 39060, 'vendor_registry_status': 20853, 'vendor_incorporation_date': 21157, 'vendor_legal_form': 20860, 'vendor_legal_name': 19147, 'buyer_bn': 8474, 'vendor_neq': 7625, 'vendor_trading_name': 181, 'buyer_address': 1878, 'buyer record found under a plain name, another name than the site prints with its legal form: not taken': 295, 'vendor_skipped_legal_form': 1, 'buyer record looked up under a name the row no longer carries, not taken': 9, 'vendor_bn9_other_registry': 4, 'buyer record of another name than the legal person the site itself states, not taken': 55}
[  706s +   0s  6.2G] award facts from the buyers' own award pages: 237 pairs with a page; filled {'contract_value': 39, 'end_date': 17, 'start_date': 9, 'contract_or_agreement_number': 3, 'solicitation_or_tender_number': 6, 'term': 2, 'po_number_as_published': 1, 'number_of_bids': 1}
[  710s +   3s  6.2G] legal names read off a page, tidied: {'tidied': 870, 'fragment': 59, 'owner': 82, "row's own name tidied with it": 155, "row's own name: a clause of the sentence cut off": 2}
[  710s +   1s  6.2G] legal name: the organisation's own name carries its legal form (cells still empty after every register and site statement): 2561
[  712s +   1s  6.2G] legal names from validated certificate subjects (Certificate Transparency): domains on file 3353; {'buyer_legal_name': 88, "subject does not carry the organisation's own name: not taken": 127}
[  712s +   0s  6.2G] grants & contributions recipient BNs: 8183 buyers, 1075 vendors in file; filled {'buyer_bn': 5357, 'buyer_legal_name': 2384, 'vendor_bn9': 4418, 'buyer_bn_conflict_noted': 89}
[  714s +   3s  6.2G] vendor legal name, last links of the chain: {"the vendor's own name carries its legal form": 3559, "the vendor's own terms, read by hand": 31773}
[  717s +   3s  6.2G] vendors that are organisations of this table (same name, same province): facts carried from their own row: {'vendor_phone': 4249, 'vendor_website': 4902, 'vendor_legal_name': 727, 'vendor_bn9': 8}
[  740s +  22s  6.4G] buyers' PO / contract open data joined: {'pairs': 6, 'po_filled': 5, 'contract_filled': 1} | records read: 330978 | kept (a row's own buyer-vendor pair): 179
[  762s +  22s  6.8G] back-references: {'dataset rows with lead relationships': 155625, 'lead rows with dataset history': 60}
[  783s +  21s  6.4G] sensitivity tags: {'corrections / detention': 38, 'health: mental health / addiction / sexual health': 498, 'intelligence / security / defence': 28, 'police service / police board': 107, 'courts / tribunals / legal aid': 98, 'child / youth protection': 29, 'police oversight body': 5, 'shelter / crisis / sexual-assault service': 99, 'coroner / medical examiner': 1}
[  796s +  13s  6.4G] site readers, second pass (websites found late): {'buyer_logo': 618, 'vendor_phone': 6357, 'vendor_logo': 57491, 'vendor_emails': 1577, 'vendor_address': 792, 'buyer_address': 5, 'buyer_phone': 46}
[  796s +   1s  6.4G] listings on a site that is not the Canada-located vendor's own (-> tier E): {'kept — the site prints an address in Canada': 6614, "kept — Wikidata: the site's organisation has its headquarters in Canada": 1483, 'kept — no evidence about whose site it is': 746, "the site's own address is outside Canada": 204, 'from tier D': 841, "Wikidata: the site's organisation has its headquarters outside Canada": 497, "kept — the listing is in the site's Canadian section (/ca/, /en-ca/, ca.…)": 48, 'Canadian arm of a group, site not shown to be its own': 26, "kept although the site reader's address is abroad (Wikidata: headquarters in Canada)": 41, "the vendor's published terms: its Canadian entity does not contract with customers of this buyer's country": 114, "kept — address abroad on the site, but a corporation of the site's name is registered in Canada": 11}
[  801s +   4s  6.4G] same-vendor carry-over (BN9, identity facts and address from the vendor's other rows): {'address': 140, 'bn9': 103849, 'legal_name': 103845, 'trading_name': 103835, 'gst_hst_derived': 103849, 'phone': 14, 'emails': 11, 'logo_url': 14, 'registry_id': 103830, 'registry_url': 103830, 'registered_address': 103830, 'legal_form': 103830, 'registry_status': 103830, 'registry_match_level': 103832, 'incorporation_date': 103830}
[ 1003s + 202s  6.3G] rows written: 100000 of 282207
[ 1191s + 189s  6.2G] rows written: 200000 of 282207
[ 1346s + 155s  6.1G] narrative columns: {'mailbox meta found': 273332, 'contract_description_from_title': 196517, 'contract_title_from_description': 142, 'invoice_reference_hint_po_rule': 1155, 'records_with_this_vendor_lead': 259448, 'vendor shown under its legal name instead of its domain name': 7740, 'date written day-month: put in order': 535, 'mailbox meta missing': 1300, 'buyer shown under its legal name instead of its domain name': 105, 'buyer name: the page-title opening (Welcome to …) removed': 314, 'buyer named by a menu word (About, Home …): its domain name instead': 353, 'vendor name cut at an apostrophe: completed from the page title': 107}
[ 1346s +   0s  6.1G] recurring billing (owner's bar of 2026-11-11: billed monthly or every three months, systematically, by the vendor) — rows with a mailbox:
[ 1346s +   0s  6.1G]   1 monthly                35478   D 12 · T 35466
[ 1346s +   0s  6.1G]   1 quarterly                  4   D 4
[ 1346s +   0s  6.1G]   2 monthly or yearly      34446   D 369 · M 13 · T 34064
[ 1346s +   0s  6.1G]   3 yearly or longer      123451   A 4 · B 347 · D 2527 · L 1 · M 8270 · R 103559 · T 8743
[ 1346s +   0s  6.1G]   4 per transaction          161   M 161
[ 1346s +   0s  6.1G]   5 not published          81092   A 1271 · B 1380 · C 315 · D 24325 · E 5154 · F 7 · I 17390 · L 433 · M 4972 · T 25845
[ 1346s +   0s  6.1G]   rows that meet the bar as published (1 monthly + 1 quarterly): 35482 of 274632 rows with a mailbox | Shopify rows by the store's country: US 19985, CA 9926, country not read 288
[ 1346s +   0s  6.1G]   the bill's fields, rows with a mailbox that carry each: bill_amount_indicative 76465, bill_amount_basis 76465, bill_items_as_published 138597, bill_currency_as_published 58569, bill_delivery_as_published 30030, bill_payment_method_as_published 140348, bill_tax_rule_as_published 30030, bill_identifier_format 30030, service_stops_if_unpaid 142721, relationship_fact_basis 274632, billing_period_calculated 1128
[ 1346s +   0s  6.1G] invoice fields (owner 2026-11-11: every aspect within an invoice) — rows with a mailbox that carry each, of 274632: buyer legal name 125790 (46%) · buyer address 199384 (73%) · vendor legal name 230678 (84%) · vendor address 273468 (100%) · vendor tax number 165188 (60%) · what is billed 223897 (82%) · amount 79370 (29%) · billing period 193540 (70%) · reference 221062 (80%) · all but the amount 45548 (17%) · all nine 15704 (6%)
[ 1346s +   0s  6.1G]   rows by number of the nine fields, tier by tier: A: 9×3 8×706 7×501 6×51 5×10 4×4 | B: 9×1 8×311 7×352 6×345 5×380 4×211 3×88 | C: 8×113 7×143 6×36 5×15 4×6 3×2 | D: 7×36 6×702 5×2613 4×6686 3×9650 | E: 7×28 6×434 5×787 4×1193 3×1276 | F: 8×2 7×4 6×1 | I: 6×24 5×6831 4×4514 3×5446 | L: 8×37 7×71 6×128 5×119 4×53 3×22 | M: 8×4636 7×1566 6×3717 5×2510 4×848 3×73 | R: 8×29799 7×43504 6×30256 | T: 9×15700 8×24087 7×17825 6×23080 5×13890 4×7552 3×1963
[ 1346s +   0s  6.1G] downstream pack: {'tax_derived_foreign': 36121, 'pay_on_sight_yes': 2523, 'ap_payable_today': 2543, 'ship_ready_yes': 1084, 'buyer_trade_name_as_published': 211271, 'tax_derived': 173048, 'registry_note': 220, 'prompt_payment_default': 836, 'pay_on_sight_no': 185067, 'buyer_type_from_name': 49544, 'sensitivity_extra': 215, 'buyer_address_from_own_page': 1978, 'registry_warning': 1472, 'invoice_currency_derived': 254257, 'pay_on_sight_routed': 87042, 'currency_default': 2}
[ 1346s +   0s  6.1G] rows 282207
[ 1346s +   0s  6.1G] [('GOLD', 625), ('A0', 519), ('A1', 711), ('A2', 92), ('A3', 223), ('A4', 8), ('B0', 623), ('B1', 1016), ('B2', 130), ('B3', 186), ('B4', 11), ('C0', 1003), ('C1', 245), ('C2', 18), ('C3', 26), ('C4', 26), ('D0', 617), ('D1', 26103), ('D2', 175), ('D3', 650), ('D4', 309), ('E0', 268), ('E1', 4834), ('E2', 96), ('E3', 121), ('E4', 103), ('F0', 1), ('F1', 3), ('F2', 1), ('F3', 2), ('F4', 1), ('GOLD-M', 126), ('GOLD-T', 427), ('I0', 737), ('I1', 16990), ('I2', 60), ('I3', 240), ('I4', 100), ('L0', 217), ('L1', 312), ('L2', 33), ('L3', 20), ('L4', 69), ('M0', 230), ('M1', 13053), ('M2', 57), ('M3', 179), ('M4', 1), ('R0', 270), ('R1', 102256), ('R2', 93), ('R3', 1030), ('R4', 180), ('T0', 3090), ('T1', 102210), ('T2', 210), ('T3', 1250), ('T4', 21)]
[ 1346s +   0s  6.1G] with any email: 274632 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            625
P01T_active_service_seen_on_buyer_site_invoicing_AP_email    427
P02_active_relationship_finance_accounting_email           471
P03_active_relationship_purchasing_email                   257
P04_active_relationship_general_email (2 part files)      3859
P05_likely_active_awarded_12_36_months_any_email           421
P06_client_listing_invoicing_AP_email                      298
P06T_active_service_seen_on_buyer_site_other_email (30 part files)  84475
P07_client_listing_finance_or_purchasing_email             803
P08_client_listing_general_email (9 part files)          25629
P09_older_contract_or_payment_any_email                    295
P10_linked_from_vendor_site_any_email                     2648
P10R_ca_domain_registration_contract_own_email (43 part files) 102647
P11_any_relationship_email_not_yet_confirmed (9 part files)  20964
P12_weaker_relationship_within_5_years_own_email             7
P13_inferred_relationship_no_record_own_email (7 part files)  17390
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email    126
P06M_member_or_regulated_payer_of_canadian_body_other_email (6 part files)  13192
Z_no_email_yet_not_delivered (2 part files)               7673
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 32862111
package files: compressed (.csv.gz); packages written straight from the table (already in order): 17 of 19; sorted from a working copy: P11 (20964 rows); sorted from a working copy: Z (7673 rows)

# coverage vs the downstream targets (COVERAGE_VS_TARGETS.md)
benchmarks met 97 / 446 (21.7%); near 67; written out/ranked/COVERAGE_VS_TARGETS.md
  gap buyer_ap_cycle_published           P10R       0.0% ->  20%  rows needed 20501
  gap ap_system_hint                     P10R       0.2% ->  20%  rows needed 20326
  gap buyer_ap_cycle_published           P06T       0.0% ->  20%  rows needed 16869
  gap ap_system_hint                     P06T       0.7% ->  20%  rows needed 16338
  gap buyer_tax_exempt_status            P10R       0.0% ->  15%  rows needed 15370
  gap buyer_esignature_preference        P10R       0.0% ->  15%  rows needed 15349
  gap vendor_phone                       P11        4.0% ->  75%  rows needed 14882
  gap buyer_payment_method_preference    P10R       0.6% ->  15%  rows needed 14733
  gap vendor_registered_address          P08       13.6% ->  70%  rows needed 14451
  gap vendor_emails                      P11        3.3% ->  70%  rows needed 13986
  gap contract_value                     P11        0.4% ->  60%  rows needed 12494
  gap award_or_notice_id                 P11        0.4% ->  60%  rows needed 12493
  gap buyer_esignature_preference        P06T       0.2% ->  15%  rows needed 12493
  gap buyer_tax_exempt_status            P06T       0.3% ->  15%  rows needed 12423
  gap buyer_payment_method_preference    P06T       0.6% ->  15%  rows needed 12172
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
