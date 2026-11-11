# Ranked buyers — 2026-11-11T03:30Z

```
[   21s +  21s  1.6G] mailboxes taken from the verification log (better than org_mailboxes' single pick): 784 | referee mailbox rows whose last label is not a top-level domain: {'left out': 15, 'cut back to the address the page prints': 62}
[   38s +  17s  0.7G] vendor table: registry matches not used because the legal form differs (partnership vs corporation): 55 | 'websites' that are a web host's own site (dropped with their mailboxes): 6 | websites not used for a look-up by domain (unverified, name does not fit): 0 | look-ups by domain: 8050
[   38s +   0s  0.7G] team vendor contacts (referee-verified): 8782 vendors; 172 with a billing / AR mailbox
[  301s + 263s  2.1G] same-pair fill (facts from another record of the same buyer-vendor pair): {'solicitation_or_tender_number': 11, 'number_of_bids': 10, 'award_or_notice_id': 2, 'buyer_vendor_id': 2, 'commodity_codes': 9, 'end_date_inferred': 120, 'contract_value': 7, 'procurement_method': 3, 'po_number_as_published': 3, 'buyer_org_codes': 1, 'start_from_signed': 497, 'end_date': 3, 'contract_description': 2, 'contract_or_agreement_number': 2, 'contract_title': 1}
[  301s +   0s  2.1G] contract records whose vendor's registry match pairs a partnership with a corporation (registry cells not used): 2244
[  311s +  10s  2.8G] tenant leads from the shards: 18213
[  311s +   0s  2.8G] leads: 427832 (338629 from the cloud row factory; 64 websites from the lead site finder)
[  352s +  41s  3.0G] registry leads (.ca domains carrying a confirmed mailbox of their own organisation): 147244
[  396s +  44s  3.3G] lead rows: facts from the buyer's own pages / the vendor's link label: {'buyer_address_from_own_page': 124505, 'buyer_name_from_own_home_page': 122139, 'facts of another host of the domain not taken': 258, 'vendor_address_cut_out_of_its_quote': 29088, 'buyer_legal_name_from_register': 8703, 'buyer_address_from_member_directory': 6455, 'buyer_name_from_vendor_link_label': 2926} | sites named again from their stored home-page title: 1144
[  396s +   0s  3.3G] client-page links judged (cloud row factory): {'client listing: label names the site': 4830, "not shown to be a client: the link's label does not name the linked site": 1781, 'link only, and the site has a .ca registration: the registration takes the row': 1765, "client listing: 'visit website' on a client page": 461, 'client listing: portfolio page': 336, 'client listing: page address names the site': 246, 'not shown to be a client: a page for clients (forms, resources, login), not a list of them': 206, "not shown to be a client: an organisation's 'our work' programme page": 197, "not shown to be a client: sister site of the page's owner": 102, 'not shown to be a client: article: the client word sits in a slug of 4 words': 66, 'not shown to be a client: dated article': 22, 'not shown to be a client: article: the client word sits in a slug of 5 words': 17, 'not shown to be a client: article: the client word sits in a slug of 6 words': 1}
[  403s +   8s  3.3G] leads with a borrowed mailbox: 109196 | rows upgraded by a newer dated record: 43 | rows upgraded to an active service seen on the buyer's site: 401
[  422s +  19s  3.4G] P12 organisations: 91 added: 8 {'no own confirmed mailbox': 65, 'same organisation already in a row': 18} | P13 added: 18769 | P13 skipped: {"mailbox not the organisation's own": 2163, 'bad mailbox': 189, 'not located in Canada (no honest inference)': 14009, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 68410, '… of which by the NAME alone (its own mailbox and domain are in no row)': 131}
[  422s +   0s  3.4G] lead rows that took the organisation's own key (registry facts attach): {'rows': 44986, 'buyer_address': 4879, 'buyer_name': 3334}
[  459s +  36s  3.4G] extras from the lanes' result rows: {'invoice_mailing_address': 2308, 'invoicing_requirements': 2114, 'ap_phone': 2404, 'invoice_portal_url': 73, 'ap_contact_name': 268}
[  479s +  20s  3.6G] words too common to prove a name (in more than 1 in 2,000 of the 227937 names of organisations whose site was read): 468; names printed on 3+ sites: 1578
[  549s +  71s  3.6G] org_extras: 229712 organisations read; filled {'vendor_logo': 77990, 'vendor_phone_v2': 48509, 'po_required': 259, 'vendor_trading_name_jsonld': 7674, 'buyer_legal_name': 66148, 'buyer_phone_v2': 104115, 'buyer_payment_method_preference_mention_rejected': 18335, 'buyer_logo': 192484, 'payment_terms': 904, 'buyer_tax_exempt_status_mention_rejected': 317, 'buyer_legal_name_v2_printed_on_many_sites': 8955, 'buyer_legal_name_v2_legal_name_stated': 17681, "vendor site is a foreign organisation's: its legal / trading name not taken for the Canada-located vendor": 1478, 'buyer_bn': 3323, 'buyer_legal_name_v2_rejected_no_overlap': 54958, 'buyer_legal_name_v2_jsonld_name': 7274, 'buyer_legal_name_v2_jsonld_legal_name': 7316, 'ap_system_hint_links': 468, 'buyer_legal_name_government_template_credit': 40, 'buyer_payment_method_preference_mention': 1174, 'vendor_legal_name': 12041, 'vendor_neq': 138, 'buyer_esignature_preference_mention_rejected': 547, 'vendor_legal_name_v2': 7029, 'buyer_address_v2': 7243, 'p13_name_from_legal_name': 11702, 'buyer_esignature_preference_mention': 76, 'buyer_legal_name_v2_jsonld_legal_name_own_site_node': 502, 'invoice_portal_links': 70, 'buyer_legal_name_v2_jsonld_name_own_site_node': 512, 'vendor_bn': 756, 'buyer_ap_cycle_published_mention': 45, 'buyer_tax_exempt_status_mention': 110, 'vendor_bn_jsonld': 69, 'buyer_bn_jsonld': 160, 'buyer_legal_name_kept_from_the_trademarks_register': 1024, 'vendor_address_v2': 303, 'vendor_address_v2_outside_canada_not_taken': 111, 'vendor_legal_name_v2_site_says': 122, 'buyer_legal_name_v2_stated_as_operator': 135, 'vendor_qst': 18, 'buyer_legal_name_v2_doing_business_as': 19, 'buyer_ap_cycle_published_mention_rejected': 35, 'buyer_legal_name_franchisor_copyright_not_taken': 11, 'p13_name_from_domain': 1}
[  550s +   0s  3.6G] regional mailboxes of multinationals removed from other-country entities: 50
[  550s +   1s  3.6G] mx_check: 69559 domains known; 185 mailboxes on domains with no mail server removed; 817 webmail (freemail) addresses removed
[  555s +   5s  3.9G] dmarc/spf: 252188 domains known; rows {'enforced': 46862, 'exposed': 192350}
[  556s +   0s  4.0G] same organisation under another key folded into the row that holds its mailbox: 52
[  561s +   5s  4.0G] second mailbox of the same organisation (same site and mail domain, same name family) folded: 6
[  568s +   7s  4.2G] org_contacts: 216504 organisations read; filled {'vendor_phone': 62754, 'vendor_emails': 39899, 'buyer_phone': 118579, 'vendor site prints an address outside Canada: address and telephone not taken': 1226, 'buyer_address': 18568, 'vendor_address': 1985}
[  568s +   0s  4.2G] site-reader records read on another host of the row's domain (look-ups): {'org_extras: not taken': 847, 'org_contacts: not taken': 1413, 'org_contacts: taken, read on another host for the same organisation (same name)': 120, 'org_extras: taken, read on another host for the same organisation (same name)': 54, "org_contacts: taken, the row's host is the member directory of the body whose own site was read": 801, "org_extras: taken, the row's host is the member directory of the body whose own site was read": 210}
[  581s +  13s  4.7G] ap_terms (evidence pages re-read): 82907 keys read, 108944 pages used across rows; filled {'payment_terms': 3534, 'po_required': 1901, 'payment_method': 700, 'ap_cycle': 108, 'tax_exempt': 1014, 'portal': 1971, 'format': 742, 'context': 45791, 'esignature': 607, 'ap_system_portal': 1708, 'ap_phone': 1110, 'buyer_bn': 55, 'ap_contact_name': 831, 'address': 554, 'mailbox_gone': 335, 'ap_system': 444, 'setup_url': 321, 'buyer_phone_from_page': 9515, 'buyer_address_from_page': 613}
[  584s +   3s  4.6G] peppol: 77 Canadian participants; matched buyers 6, vendors 39
[  585s +   0s  4.6G] directories: 2338 entries reachable by their own site; 112 sites given by entries of different names, left out
[  587s +   3s  4.6G] municipal / organisation directories: {'matched': 1748, 'legal_name': 797, 'phone': 321, 'address': 46, 'matched_by_place_name': 12, 'website': 18}
[  588s +   1s  4.6G] charity buyers: {'matched': 9728, 'bn': 7979, 'legal_name': 6645, 'address': 624, 'website': 32}
[  589s +   1s  4.7G] charity registration numbers found in the CRA list: {'matched': 858, 'legal_name': 557, 'address': 74, 'name_from_the_register': 87, 'holder is a foundation / trust under another name: reported only': 34} | list: 83761
[  591s +   2s  4.8G] wikidata: {'vendors': 1154, 'buyers': 5225, 'buyer_legal_name': 2370, 'buyer_phone': 90, 'buyer_address': 618, 'buyer_website': 106, 'vendor_legal_name': 44, 'vendor_address': 410, 'vendor_website': 238, 'vendor_neq': 7}
[  592s +   1s  4.8G] crown-corporation BNs applied to inferred-vendor rows: 17095
[  592s +   0s  4.8G] vendor websites confirmed from search proposals: 502 applied: 18972
[  592s +   0s  4.8G] inferred vendors' published phone / address applied: {'phone': 13756}
[  593s +   1s  4.9G] registry bulk rows added (no API row for the key): 22305 | registry rows left out, the registered name is only legal-form and place words: 0
[  595s +   2s  4.9G] Canada's Business Registries + registry open data: 3706 vendors, 28246 buyers found; filled {'buyer_bn': 9151, 'buyer_legal_name': 13840, 'vendor_registered_address': 15607, 'vendor_bn9': 23830, 'vendor_legal_name': 15540, 'vendor_registry_status': 15542, 'vendor_incorporation_date': 15825, 'vendor_legal_form': 15549, 'vendor_neq': 4470, 'vendor_trading_name': 259, 'buyer_address': 2053, 'vendor_skipped_legal_form': 1, 'buyer record looked up under a name the row no longer carries, not taken': 6, 'vendor_bn9_other_registry': 4, 'buyer record of another name than the legal person the site itself states, not taken': 19}
[  595s +   0s  4.9G] award facts from the buyers' own award pages: 237 pairs with a page; filled {'contract_value': 39, 'end_date': 17, 'start_date': 9, 'contract_or_agreement_number': 3, 'solicitation_or_tender_number': 6, 'term': 2, 'po_number_as_published': 1, 'number_of_bids': 1}
[  597s +   2s  4.9G] legal name: the organisation's own name carries its legal form (cells still empty after every register and site statement): 3716
[  597s +   0s  4.9G] grants & contributions recipient BNs: 8183 buyers, 1075 vendors in file; filled {'buyer_bn': 5742, 'buyer_legal_name': 2700, 'vendor_bn9': 3934, 'buyer_bn_conflict_noted': 97}
[  617s +  20s  5.0G] buyers' PO / contract open data joined: {'pairs': 5, 'po_filled': 4, 'contract_filled': 1} | records read: 330978 | kept (a row's own buyer-vendor pair): 143
[  635s +  17s  5.3G] back-references: {'dataset rows with lead relationships': 150321, 'lead rows with dataset history': 52}
[  651s +  16s  5.0G] sensitivity tags: {'corrections / detention': 36, 'health: mental health / addiction / sexual health': 450, 'intelligence / security / defence': 25, 'police service / police board': 99, 'courts / tribunals / legal aid': 84, 'child / youth protection': 28, 'police oversight body': 5, 'shelter / crisis / sexual-assault service': 94, 'coroner / medical examiner': 1}
[  662s +  11s  5.0G] site readers, second pass (websites found late): {'buyer_logo': 593, 'vendor_emails': 575, 'vendor_phone': 780, 'vendor_logo': 34699, 'vendor_address': 239, 'buyer_address': 5, 'buyer_phone': 46}
[  663s +   1s  5.0G] listings on a site that is not the Canada-located vendor's own (-> tier E): {'kept — the site prints an address in Canada': 6147, "kept — Wikidata: the site's organisation has its headquarters in Canada": 1512, 'kept — no evidence about whose site it is': 1518, "the site's own address is outside Canada": 186, 'from tier D': 843, "Wikidata: the site's organisation has its headquarters outside Canada": 512, "kept — the listing is in the site's Canadian section (/ca/, /en-ca/, ca.…)": 48, 'Canadian arm of a group, site not shown to be its own': 31, "kept although the site reader's address is abroad (Wikidata: headquarters in Canada)": 40, "the vendor's published terms: its Canadian entity does not contract with customers of this buyer's country": 114, "kept — address abroad on the site, but a corporation of the site's name is registered in Canada": 11}
[  667s +   4s  5.0G] same-vendor carry-over (BN9, identity facts and address from the vendor's other rows): {'address': 130, 'bn9': 100038, 'legal_name': 100034, 'trading_name': 100035, 'gst_hst_derived': 100038, 'registry_id': 100031, 'registry_url': 100031, 'registered_address': 100031, 'legal_form': 100031, 'registry_status': 100031, 'registry_match_level': 100032, 'incorporation_date': 100031, 'phone': 3, 'logo_url': 4, 'neq': 1}
[  836s + 169s  5.0G] rows written: 100000 of 242317
[ 1004s + 168s  4.9G] rows written: 200000 of 242317
[ 1075s +  71s  4.5G] narrative columns: {'mailbox meta found': 235000, 'contract_description_from_title': 169587, 'contract_title_from_description': 142, 'invoice_reference_hint_po_rule': 1153, 'records_with_this_vendor_lead': 218906, 'mailbox meta missing': 1341}
[ 1075s +   0s  4.5G] downstream pack: {'tax_derived_foreign': 21929, 'pay_on_sight_yes': 2352, 'ap_payable_today': 2147, 'ship_ready_yes': 967, 'buyer_trade_name_as_published': 178488, 'tax_derived': 156206, 'registry_note': 222, 'prompt_payment_default': 781, 'pay_on_sight_no': 154898, 'buyer_type_from_name': 33258, 'sensitivity_extra': 198, 'buyer_address_from_own_page': 2903, 'registry_warning': 1362, 'invoice_currency_derived': 221238, 'pay_on_sight_routed': 79091, 'currency_default': 2}
[ 1075s +   0s  4.5G] rows 242317
[ 1075s +   0s  4.5G] [('GOLD', 625), ('A0', 519), ('A1', 712), ('A2', 92), ('A3', 223), ('A4', 8), ('B0', 623), ('B1', 1007), ('B2', 131), ('B3', 186), ('B4', 11), ('C0', 1003), ('C1', 252), ('C2', 19), ('C3', 26), ('C4', 26), ('D0', 602), ('D1', 27131), ('D2', 181), ('D3', 681), ('D4', 323), ('E0', 258), ('E1', 4950), ('E2', 95), ('E3', 127), ('E4', 103), ('F0', 1), ('F1', 4), ('F2', 1), ('F3', 1), ('F4', 1), ('GOLD-M', 105), ('GOLD-T', 334), ('I0', 716), ('I1', 17644), ('I2', 61), ('I3', 242), ('I4', 106), ('L0', 217), ('L1', 317), ('L2', 33), ('L3', 19), ('L4', 71), ('M0', 191), ('M1', 10527), ('M2', 34), ('M3', 147), ('M4', 1), ('R0', 187), ('R1', 98588), ('R2', 100), ('R3', 975), ('R4', 179), ('T0', 1659), ('T1', 68853), ('T2', 151), ('T3', 923), ('T4', 15)]
[ 1075s +   0s  4.5G] with any email: 236341 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            625
P01T_active_service_seen_on_buyer_site_invoicing_AP_email    334
P02_active_relationship_finance_accounting_email           474
P03_active_relationship_purchasing_email                   257
P04_active_relationship_general_email (2 part files)      3887
P05_likely_active_awarded_12_36_months_any_email           427
P06_client_listing_invoicing_AP_email                      312
P06T_active_service_seen_on_buyer_site_other_email (20 part files)  60045
P07_client_listing_finance_or_purchasing_email             838
P08_client_listing_general_email (8 part files)          26652
P09_older_contract_or_payment_any_email                    303
P10_linked_from_vendor_site_any_email                     2735
P10R_ca_domain_registration_contract_own_email (37 part files)  98993
P11_any_relationship_email_not_yet_confirmed (4 part files)  11585
P12_weaker_relationship_within_5_years_own_email             7
P13_inferred_relationship_no_record_own_email (6 part files)  18053
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email    105
P06M_member_or_regulated_payer_of_canadian_body_other_email (5 part files)  10630
Z_no_email_yet_not_delivered (2 part files)               6055
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 26826909
package files: compressed (.csv.gz); packages written straight from the table (already in order): 17 of 19; sorted from a working copy: P11 (11585 rows); sorted from a working copy: Z (6055 rows)

# coverage vs the downstream targets (COVERAGE_VS_TARGETS.md)
benchmarks met 93 / 446 (20.9%); near 58; written out/ranked/COVERAGE_VS_TARGETS.md
  gap buyer_ap_cycle_published           P10R       0.0% ->  20%  rows needed 19778
  gap ap_system_hint                     P10R       0.2% ->  20%  rows needed 19598
  gap vendor_registered_address          P08       12.6% ->  70%  rows needed 15302
  gap buyer_tax_exempt_status            P10R       0.0% ->  15%  rows needed 14819
  gap buyer_esignature_preference        P10R       0.0% ->  15%  rows needed 14804
  gap buyer_payment_method_preference    P10R       0.6% ->  15%  rows needed 14247
  gap buyer_ap_cycle_published           P06T       0.0% ->  20%  rows needed 11988
  gap ap_system_hint                     P06T       0.7% ->  20%  rows needed 11560
  gap buyer_phone                        P08       56.5% ->  95%  rows needed 10273
  gap vendor_bn9                         P08       14.3% ->  50%  rows needed 9517
  gap buyer_legal_name_as_published      P08       40.8% ->  75%  rows needed 9111
  gap buyer_esignature_preference        P06T       0.2% ->  15%  rows needed 8867
  gap buyer_tax_exempt_status            P06T       0.3% ->  15%  rows needed 8821
  gap buyer_payment_method_preference    P06T       0.6% ->  15%  rows needed 8659
  gap vendor_phone                       P11        5.5% ->  75%  rows needed 8051
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
