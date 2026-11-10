# Ranked buyers — 2026-11-10T20:38Z

```
[   22s +  22s  1.5G] mailboxes taken from the verification log (better than org_mailboxes' single pick): 774 | referee mailbox rows whose last label is not a top-level domain: {'left out': 15, 'cut back to the address the page prints': 62}
[   39s +  17s  0.7G] vendor table: registry matches not used because the legal form differs (partnership vs corporation): 55 | 'websites' that are a web host's own site (dropped with their mailboxes): 5 | websites not used for a look-up by domain (unverified, name does not fit): 0 | look-ups by domain: 8051
[   39s +   0s  0.7G] team vendor contacts (referee-verified): 8782 vendors; 172 with a billing / AR mailbox
[  297s + 258s  2.1G] same-pair fill (facts from another record of the same buyer-vendor pair): {'solicitation_or_tender_number': 11, 'number_of_bids': 10, 'award_or_notice_id': 2, 'buyer_vendor_id': 2, 'commodity_codes': 9, 'end_date_inferred': 120, 'contract_value': 7, 'procurement_method': 3, 'po_number_as_published': 3, 'buyer_org_codes': 1, 'start_from_signed': 497, 'end_date': 3, 'contract_description': 2, 'contract_or_agreement_number': 2, 'contract_title': 1}
[  297s +   0s  2.1G] contract records whose vendor's registry match pairs a partnership with a corporation (registry cells not used): 2244
[  305s +   8s  2.6G] tenant leads from the shards: 12466
[  305s +   0s  2.6G] leads: 379226 (295770 from the cloud row factory; 63 websites from the lead site finder)
[  341s +  35s  2.8G] registry leads (.ca domains carrying a confirmed mailbox of their own organisation): 143029
[  379s +  38s  3.0G] lead rows: facts from the buyer's own pages / the vendor's link label: {'buyer_address_from_own_page': 109830, 'buyer_name_from_own_home_page': 115902, 'facts of another host of the domain not taken': 271, 'vendor_address_cut_out_of_its_quote': 23432, 'buyer_legal_name_from_register': 5207, 'buyer_address_from_member_directory': 4674, 'buyer_name_from_vendor_link_label': 2277} | sites named again from their stored home-page title: 1144
[  379s +   0s  3.0G] client-page links judged (cloud row factory): {'client listing: label names the site': 3409, 'link only, and the site has a .ca registration: the registration takes the row': 1598, "not shown to be a client: the link's label does not name the linked site": 1257, "client listing: 'visit website' on a client page": 266, 'client listing: portfolio page': 180, 'client listing: page address names the site': 176, 'not shown to be a client: a page for clients (forms, resources, login), not a list of them': 174, "not shown to be a client: an organisation's 'our work' programme page": 128, "not shown to be a client: sister site of the page's owner": 89, 'not shown to be a client: article: the client word sits in a slug of 4 words': 33, 'not shown to be a client: dated article': 21, 'not shown to be a client: article: the client word sits in a slug of 5 words': 13, 'not shown to be a client: article: the client word sits in a slug of 6 words': 1}
[  385s +   7s  3.1G] leads with a borrowed mailbox: 97532 | rows upgraded by a newer dated record: 42 | rows upgraded to an active service seen on the buyer's site: 388
[  403s +  18s  3.2G] P12 organisations: 93 added: 9 {'no own confirmed mailbox': 66, 'same organisation already in a row': 18} | P13 added: 19080 | P13 skipped: {"mailbox not the organisation's own": 2157, 'bad mailbox': 188, 'not located in Canada (no honest inference)': 13239, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 63647, '… of which by the NAME alone (its own mailbox and domain are in no row)': 131}
[  403s +   0s  3.2G] lead rows that took the organisation's own key (registry facts attach): {'rows': 44369, 'buyer_address': 4888, 'buyer_name': 3247}
[  437s +  33s  3.1G] extras from the lanes' result rows: {'invoice_mailing_address': 2288, 'invoicing_requirements': 2104, 'ap_phone': 2384, 'invoice_portal_url': 73, 'ap_contact_name': 250}
[  452s +  15s  3.3G] words too common to prove a name (in more than 1 in 2,000 of the 171993 names of organisations whose site was read): 462; names printed on 3+ sites: 1406
[  509s +  58s  3.3G] org_extras: 173134 organisations read; filled {'vendor_logo': 68844, 'vendor_phone_v2': 44053, 'po_required': 248, 'vendor_trading_name_jsonld': 7047, 'buyer_legal_name': 49578, 'buyer_phone_v2': 77536, 'buyer_payment_method_preference_mention_rejected': 18040, 'buyer_logo': 139676, 'payment_terms': 762, 'buyer_tax_exempt_status_mention_rejected': 298, 'buyer_legal_name_v2_printed_on_many_sites': 8413, 'buyer_legal_name_v2_legal_name_stated': 12408, "vendor site is a foreign organisation's: its legal / trading name not taken for the Canada-located vendor": 1348, 'buyer_bn': 3001, 'buyer_legal_name_v2_rejected_no_overlap': 40836, 'buyer_legal_name_v2_jsonld_name': 5364, 'buyer_legal_name_v2_jsonld_legal_name': 5562, 'ap_system_hint_links': 426, 'buyer_legal_name_government_template_credit': 40, 'buyer_payment_method_preference_mention': 801, 'vendor_legal_name': 10354, 'vendor_neq': 127, 'buyer_esignature_preference_mention_rejected': 520, 'vendor_legal_name_v2': 6345, 'buyer_address_v2': 6180, 'p13_name_from_legal_name': 9291, 'buyer_esignature_preference_mention': 52, 'buyer_legal_name_v2_jsonld_legal_name_own_site_node': 388, 'invoice_portal_links': 58, 'buyer_legal_name_v2_jsonld_name_own_site_node': 383, 'vendor_bn': 630, 'buyer_tax_exempt_status_mention': 65, 'vendor_bn_jsonld': 54, 'buyer_bn_jsonld': 137, 'vendor_address_v2': 295, 'vendor_address_v2_outside_canada_not_taken': 110, 'buyer_ap_cycle_published_mention': 36, 'vendor_legal_name_v2_site_says': 114, 'buyer_legal_name_v2_stated_as_operator': 120, 'vendor_qst': 16, 'buyer_legal_name_v2_doing_business_as': 16, 'buyer_ap_cycle_published_mention_rejected': 33, 'buyer_legal_name_franchisor_copyright_not_taken': 7, 'p13_name_from_domain': 1}
[  510s +   0s  3.3G] regional mailboxes of multinationals removed from other-country entities: 46
[  510s +   1s  3.3G] mx_check: 69559 domains known; 184 mailboxes on domains with no mail server removed; 753 webmail (freemail) addresses removed
[  515s +   4s  3.5G] dmarc/spf: 223147 domains known; rows {'enforced': 42366, 'exposed': 167937}
[  515s +   0s  3.5G] same organisation under another key folded into the row that holds its mailbox: 52
[  519s +   4s  3.6G] second mailbox of the same organisation (same site and mail domain, same name family) folded: 6
[  525s +   6s  3.7G] org_contacts: 162071 organisations read; filled {'vendor_phone': 57592, 'vendor_emails': 35638, 'buyer_phone': 88215, 'vendor site prints an address outside Canada: address and telephone not taken': 1105, 'buyer_address': 16807, 'vendor_address': 2019}
[  525s +   0s  3.7G] site-reader records read on another host of the row's domain (look-ups): {'org_contacts: not taken': 2475, 'org_extras: not taken': 2920, 'org_contacts: taken, read on another host for the same organisation (same name)': 882, "org_extras: taken, the row's host is the member directory of the body whose own site was read": 1323, "org_contacts: taken, the row's host is the member directory of the body whose own site was read": 3277, 'org_extras: taken, read on another host for the same organisation (same name)': 437}
[  536s +  11s  4.2G] ap_terms (evidence pages re-read): 82907 keys read, 109694 pages used across rows; filled {'payment_terms': 3592, 'po_required': 1923, 'payment_method': 703, 'ap_cycle': 108, 'tax_exempt': 1021, 'portal': 1977, 'format': 743, 'context': 45807, 'esignature': 614, 'ap_system_portal': 1712, 'ap_phone': 1121, 'buyer_bn': 56, 'ap_contact_name': 833, 'address': 555, 'mailbox_gone': 334, 'ap_system': 452, 'setup_url': 325, 'buyer_phone_from_page': 9690, 'buyer_address_from_page': 657}
[  538s +   2s  4.2G] peppol: 77 Canadian participants; matched buyers 5, vendors 38
[  539s +   0s  4.2G] directories: 2338 entries reachable by their own site; 112 sites given by entries of different names, left out
[  541s +   3s  4.2G] municipal / organisation directories: {'matched': 1744, 'legal_name': 799, 'phone': 323, 'address': 46, 'matched_by_place_name': 11, 'website': 18}
[  542s +   0s  4.2G] charity buyers: {'matched': 7263, 'bn': 6004, 'legal_name': 4280, 'address': 304, 'website': 25}
[  543s +   2s  4.2G] wikidata: {'vendors': 1162, 'buyers': 5247, 'buyer_legal_name': 2499, 'buyer_address': 636, 'buyer_phone': 90, 'buyer_website': 109, 'vendor_legal_name': 43, 'vendor_address': 414, 'vendor_website': 244, 'vendor_neq': 7}
[  544s +   1s  4.2G] crown-corporation BNs applied to inferred-vendor rows: 17382
[  544s +   0s  4.2G] vendor websites confirmed from search proposals: 502 applied: 13339
[  544s +   0s  4.2G] inferred vendors' published phone / address applied: {'phone': 13822}
[  545s +   1s  4.2G] registry bulk rows added (no API row for the key): 22305 | registry rows left out, the registered name is only legal-form and place words: 0
[  546s +   2s  4.3G] Canada's Business Registries + registry open data: 3706 vendors, 28246 buyers found; filled {'buyer_bn': 9554, 'buyer_legal_name': 15274, 'vendor_registered_address': 15162, 'vendor_bn9': 18019, 'vendor_legal_name': 15092, 'vendor_registry_status': 15094, 'vendor_incorporation_date': 15382, 'vendor_legal_form': 15101, 'vendor_neq': 4239, 'vendor_trading_name': 277, 'buyer_address': 2249, 'vendor_skipped_legal_form': 1, 'buyer record looked up under a name the row no longer carries, not taken': 5, 'vendor_bn9_other_registry': 4, 'buyer record of another name than the legal person the site itself states, not taken': 20}
[  547s +   0s  4.3G] award facts from the buyers' own award pages: 237 pairs with a page; filled {'contract_value': 39, 'end_date': 17, 'start_date': 9, 'contract_or_agreement_number': 3, 'solicitation_or_tender_number': 6, 'term': 2, 'po_number_as_published': 1, 'number_of_bids': 1}
[  548s +   1s  4.3G] grants & contributions recipient BNs: 3202 buyers, 454 vendors in file; filled {'buyer_bn': 1613, 'buyer_bn_conflict_noted': 87, 'vendor_bn9': 781, 'buyer_legal_name': 340}
[  566s +  19s  4.4G] buyers' PO / contract open data joined: {'pairs': 5, 'po_filled': 4, 'contract_filled': 1} | records read: 330978 | kept (a row's own buyer-vendor pair): 143
[  580s +  14s  4.6G] back-references: {'dataset rows with lead relationships': 139734, 'lead rows with dataset history': 48}
[  592s +  12s  4.4G] sensitivity tags: {'corrections / detention': 36, 'health: mental health / addiction / sexual health': 407, 'intelligence / security / defence': 25, 'police service / police board': 91, 'courts / tribunals / legal aid': 71, 'child / youth protection': 26, 'police oversight body': 5, 'shelter / crisis / sexual-assault service': 83, 'coroner / medical examiner': 1}
[  602s +  10s  4.4G] site readers, second pass (websites found late): {'buyer_logo': 588, 'vendor_emails': 568, 'vendor_phone': 753, 'vendor_logo': 29151, 'vendor_address': 235, 'buyer_address': 6, 'buyer_phone': 42}
[  603s +   0s  4.4G] listings on a site that is not the Canada-located vendor's own (-> tier E): {'kept — the site prints an address in Canada': 2240, "kept — Wikidata: the site's organisation has its headquarters in Canada": 1331, 'kept — no evidence about whose site it is': 554, "the site's own address is outside Canada": 104, 'from tier D': 743, "Wikidata: the site's organisation has its headquarters outside Canada": 500, "kept — the listing is in the site's Canadian section (/ca/, /en-ca/, ca.…)": 50, 'Canadian arm of a group, site not shown to be its own': 28, "kept although the site reader's address is abroad (Wikidata: headquarters in Canada)": 38, "the vendor's published terms: its Canadian entity does not contract with customers of this buyer's country": 111, "kept — address abroad on the site, but a corporation of the site's name is registered in Canada": 11}
[  606s +   3s  4.4G] same-vendor carry-over (BN9, identity facts and address from the vendor's other rows): {'address': 130, 'bn9': 100955, 'legal_name': 100951, 'trading_name': 100952, 'phone': 5, 'gst_hst_derived': 100955, 'registry_id': 100948, 'registry_url': 100948, 'registered_address': 100948, 'legal_form': 100948, 'registry_status': 100948, 'registry_match_level': 100949, 'incorporation_date': 100948, 'logo_url': 4, 'neq': 1}
[  770s + 164s  4.4G] rows written: 100000 of 225515
[  944s + 174s  4.3G] rows written: 200000 of 225515
[  982s +  38s  4.0G] narrative columns: {'mailbox meta found': 218532, 'contract_description_from_title': 164883, 'contract_title_from_description': 142, 'invoice_reference_hint_po_rule': 1173, 'records_with_this_vendor_lead': 201793, 'mailbox meta missing': 1450}
[  982s +   0s  4.0G] downstream pack: {'tax_derived_foreign': 16563, 'pay_on_sight_yes': 2286, 'ap_payable_today': 1875, 'ship_ready_yes': 922, 'buyer_trade_name_as_published': 162691, 'tax_derived': 144569, 'registry_note': 223, 'prompt_payment_default': 650, 'pay_on_sight_no': 143640, 'buyer_type_from_name': 27523, 'sensitivity_extra': 185, 'buyer_address_from_own_page': 4374, 'registry_warning': 1322, 'invoice_currency_derived': 206576, 'pay_on_sight_routed': 74056, 'currency_default': 2}
[  982s +   0s  4.0G] rows 225515
[  982s +   0s  4.0G] [('GOLD', 626), ('A0', 519), ('A1', 712), ('A2', 92), ('A3', 223), ('A4', 8), ('B0', 623), ('B1', 1003), ('B2', 131), ('B3', 186), ('B4', 11), ('C0', 1003), ('C1', 252), ('C2', 19), ('C3', 26), ('C4', 26), ('D0', 489), ('D1', 21310), ('D2', 165), ('D3', 548), ('D4', 292), ('E0', 226), ('E1', 4314), ('E2', 92), ('E3', 117), ('E4', 100), ('F0', 1), ('F1', 4), ('F2', 1), ('F3', 2), ('F4', 1), ('GOLD-M', 67), ('GOLD-T', 325), ('I0', 694), ('I1', 17961), ('I2', 64), ('I3', 250), ('I4', 111), ('L0', 217), ('L1', 309), ('L2', 33), ('L3', 19), ('L4', 71), ('M0', 56), ('M1', 6254), ('M2', 22), ('M3', 82), ('M4', 1), ('R0', 170), ('R1', 99510), ('R2', 100), ('R3', 985), ('R4', 181), ('T0', 1535), ('T1', 62330), ('T2', 145), ('T3', 890), ('T4', 11)]
[  982s +   0s  4.0G] with any email: 219982 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            626
P01T_active_service_seen_on_buyer_site_invoicing_AP_email    325
P02_active_relationship_finance_accounting_email           464
P03_active_relationship_purchasing_email                   256
P04_active_relationship_general_email (2 part files)      3315
P05_likely_active_awarded_12_36_months_any_email           419
P06_client_listing_invoicing_AP_email                      281
P06T_active_service_seen_on_buyer_site_other_email (19 part files)  57911
P07_client_listing_finance_or_purchasing_email             690
P08_client_listing_general_email (7 part files)          20898
P09_older_contract_or_payment_any_email                    303
P10_linked_from_vendor_site_any_email                     2665
P10R_ca_domain_registration_contract_own_email (37 part files)  99903
P11_any_relationship_email_not_yet_confirmed (3 part files)   7106
P12_weaker_relationship_within_5_years_own_email             8
P13_inferred_relationship_no_record_own_email (7 part files)  18386
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email     67
P06M_member_or_regulated_payer_of_canadian_body_other_email (3 part files)   6303
Z_no_email_yet_not_delivered (2 part files)               5589
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 25191752
package files: compressed (.csv.gz); packages written straight from the table (already in order): 17 of 19; sorted from a working copy: P11 (7106 rows); sorted from a working copy: Z (5589 rows)

# coverage vs the downstream targets (COVERAGE_VS_TARGETS.md)
benchmarks met 52 / 446 (11.7%); near 97; written out/ranked/COVERAGE_VS_TARGETS.md
  gap buyer_ap_cycle_published           P10R       0.0% ->  20%  rows needed 19964
  gap ap_system_hint                     P10R       0.2% ->  20%  rows needed 19782
  gap buyer_tax_exempt_status            P10R       0.0% ->  15%  rows needed 14965
  gap buyer_esignature_preference        P10R       0.0% ->  15%  rows needed 14952
  gap buyer_payment_method_preference    P10R       0.4% ->  15%  rows needed 14585
  gap buyer_ap_cycle_published           P06T       0.0% ->  20%  rows needed 11563
  gap vendor_registered_address          P08       15.0% ->  70%  rows needed 11490
  gap ap_system_hint                     P06T       0.7% ->  20%  rows needed 11150
  gap buyer_esignature_preference        P06T       0.2% ->  15%  rows needed 8550
  gap buyer_tax_exempt_status            P06T       0.3% ->  15%  rows needed 8514
  gap buyer_payment_method_preference    P06T       0.5% ->  15%  rows needed 8426
  gap buyer_phone                        P13       49.6% ->  95%  rows needed 8355
  gap vendor_bn9                         P08       11.7% ->  50%  rows needed 8014
  gap buyer_logo_url                     P13       52.9% ->  95%  rows needed 7745
  gap buyer_legal_name_as_published      P08       42.2% ->  75%  rows needed 6856
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
