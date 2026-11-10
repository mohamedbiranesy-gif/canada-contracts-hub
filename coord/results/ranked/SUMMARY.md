# Ranked buyers — 2026-11-10T15:46Z

```
[   12s +  12s  1.2G] mailboxes taken from the verification log (better than org_mailboxes' single pick): 765 | referee mailbox rows whose last label is not a top-level domain: {'left out': 16, 'cut back to the address the page prints': 66}
[   26s +  14s  0.6G] vendor table: registry matches not used because the legal form differs (partnership vs corporation): 55 | 'websites' that are a web host's own site (dropped with their mailboxes): 5 | websites not used for a look-up by domain (unverified, name does not fit): 0 | look-ups by domain: 8051
[   26s +   0s  0.6G] team vendor contacts (referee-verified): 8781 vendors; 172 with a billing / AR mailbox
[  218s + 192s  2.0G] same-pair fill (facts from another record of the same buyer-vendor pair): {'solicitation_or_tender_number': 11, 'number_of_bids': 10, 'award_or_notice_id': 2, 'buyer_vendor_id': 2, 'commodity_codes': 9, 'end_date_inferred': 120, 'contract_value': 7, 'procurement_method': 3, 'po_number_as_published': 3, 'buyer_org_codes': 1, 'start_from_signed': 497, 'end_date': 3, 'contract_description': 2, 'contract_or_agreement_number': 2, 'contract_title': 1}
[  218s +   0s  2.0G] contract records whose vendor's registry match pairs a partnership with a corporation (registry cells not used): 2244
[  225s +   7s  2.5G] tenant leads from the shards: 10037
[  225s +   0s  2.5G] leads: 369121 (288094 from the cloud row factory; 49 websites from the lead site finder)
[  249s +  24s  2.7G] registry leads (.ca domains carrying a confirmed mailbox of their own organisation): 113171
[  271s +  22s  2.8G] lead rows: facts from the buyer's own pages / the vendor's link label: {'buyer_address_from_own_page': 82634, 'buyer_name_from_own_home_page': 88658, 'vendor_address_cut_out_of_its_quote': 15257, 'buyer_legal_name_from_register': 4047, 'buyer_address_from_member_directory': 3805, 'buyer_name_from_vendor_link_label': 1921} | sites named again from their stored home-page title: 1144
[  271s +   0s  2.8G] client-page links judged (cloud row factory): {'client listing: label names the site': 3262, 'link only, and the site has a .ca registration: the registration takes the row': 1570, "not shown to be a client: the link's label does not name the linked site": 1187, "client listing: 'visit website' on a client page": 246, 'client listing: portfolio page': 175, 'client listing: page address names the site': 174, 'not shown to be a client: a page for clients (forms, resources, login), not a list of them': 167, "not shown to be a client: an organisation's 'our work' programme page": 120, "not shown to be a client: sister site of the page's owner": 87, 'not shown to be a client: article: the client word sits in a slug of 4 words': 32, 'not shown to be a client: dated article': 20, 'not shown to be a client: article: the client word sits in a slug of 5 words': 11, 'not shown to be a client: article: the client word sits in a slug of 6 words': 1}
[  276s +   4s  2.9G] leads with a borrowed mailbox: 91485 | rows upgraded by a newer dated record: 42 | rows upgraded to an active service seen on the buyer's site: 381
[  288s +  12s  2.9G] P12 organisations: 93 added: 9 {'no own confirmed mailbox': 66, 'same organisation already in a row': 18} | P13 added: 14798 | P13 skipped: {"mailbox not the organisation's own": 2152, 'bad mailbox': 188, 'not located in Canada (no honest inference)': 7316, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 59557, '… of which by the NAME alone (its own mailbox and domain are in no row)': 122}
[  288s +   0s  2.9G] lead rows that took the organisation's own key (registry facts attach): {'rows': 44319, 'buyer_address': 4932, 'buyer_name': 3211}
[  307s +  20s  2.9G] extras from the lanes' result rows: {'invoice_mailing_address': 2281, 'invoicing_requirements': 2099, 'ap_phone': 2376, 'invoice_portal_url': 73, 'ap_contact_name': 224}
[  327s +  19s  2.9G] org_extras: 83559 organisations read; filled {'vendor_logo': 26508, 'vendor_phone_v2': 12432, 'po_required': 226, 'vendor_trading_name_jsonld': 1915, 'buyer_legal_name': 22358, 'buyer_phone_v2': 30900, 'buyer_payment_method_preference_mention_rejected': 17914, 'buyer_logo': 57644, 'payment_terms': 554, 'buyer_tax_exempt_status_mention_rejected': 271, 'buyer_legal_name_v2_rejected_no_overlap': 26303, 'buyer_legal_name_v2_legal_name_stated': 6220, "vendor site is a foreign organisation's: its legal / trading name not taken for the Canada-located vendor": 1153, 'buyer_bn': 2186, 'buyer_legal_name_v2_jsonld_name': 2257, 'buyer_legal_name_v2_jsonld_legal_name': 2664, 'ap_system_hint_links': 317, 'buyer_legal_name_government_template_credit': 43, 'buyer_payment_method_preference_mention': 293, 'vendor_legal_name': 3226, 'vendor_neq': 65, 'buyer_esignature_preference_mention_rejected': 487, 'vendor_legal_name_v2': 2255, 'buyer_address_v2': 4024, 'p13_name_from_legal_name': 5856, 'buyer_esignature_preference_mention': 18, 'vendor_bn': 430, 'invoice_portal_links': 24, 'buyer_tax_exempt_status_mention': 29, 'vendor_address_v2': 280, 'vendor_address_v2_outside_canada_not_taken': 105, 'buyer_bn_jsonld': 65, 'buyer_ap_cycle_published_mention': 11, 'vendor_qst': 7, 'vendor_bn_jsonld': 22, 'buyer_ap_cycle_published_mention_rejected': 31, 'p13_name_from_domain': 1}
[  327s +   0s  2.9G] regional mailboxes of multinationals removed from other-country entities: 44
[  327s +   0s  2.9G] mx_check: 69559 domains known; 184 mailboxes on domains with no mail server removed; 604 webmail (freemail) addresses removed
[  330s +   3s  2.9G] dmarc/spf: 173249 domains known; rows {'enforced': 31141, 'exposed': 111199}
[  330s +   0s  2.9G] same organisation under another key folded into the row that holds its mailbox: 52
[  332s +   2s  2.9G] second mailbox of the same organisation (same site and mail domain, same name family) folded: 6
[  335s +   3s  3.0G] org_contacts: 75051 organisations read; filled {'vendor_phone': 22870, 'vendor_emails': 14565, 'buyer_phone': 38443, 'vendor site prints an address outside Canada: address and telephone not taken': 816, 'buyer_address': 13632, 'vendor_address': 1983}
[  343s +   8s  3.4G] ap_terms (evidence pages re-read): 82907 keys read, 109812 pages used across rows; filled {'payment_terms': 3597, 'po_required': 1924, 'payment_method': 704, 'ap_cycle': 108, 'tax_exempt': 1023, 'portal': 1980, 'format': 743, 'context': 45829, 'esignature': 614, 'ap_system_portal': 1714, 'ap_phone': 1122, 'buyer_bn': 86, 'ap_contact_name': 834, 'address': 555, 'mailbox_gone': 334, 'ap_system': 452, 'setup_url': 326, 'buyer_phone_from_page': 9673, 'buyer_address_from_page': 629}
[  345s +   2s  3.4G] peppol: 77 Canadian participants; matched buyers 5, vendors 38
[  347s +   2s  3.4G] municipal / organisation directories: {'matched': 1778, 'legal_name': 806, 'address': 56, 'phone': 309, 'matched_by_place_name': 10, 'website': 18}
[  347s +   0s  3.4G] charity buyers: {'matched': 7278, 'bn': 6018, 'legal_name': 4202, 'address': 303, 'website': 25}
[  348s +   1s  3.4G] wikidata: {'vendors': 1157, 'buyers': 5266, 'buyer_legal_name': 2453, 'buyer_phone': 86, 'buyer_address': 629, 'buyer_website': 109, 'vendor_legal_name': 42, 'vendor_address': 405, 'vendor_website': 238, 'vendor_neq': 7}
[  348s +   0s  3.4G] crown-corporation BNs applied to inferred-vendor rows: 13402
[  348s +   0s  3.4G] vendor websites confirmed from search proposals: 502 applied: 8626
[  349s +   0s  3.4G] inferred vendors' published phone / address applied: {'phone': 10354}
[  349s +   0s  3.4G] registry bulk rows added (no API row for the key): 7455 | registry rows left out, the registered name is only legal-form and place words: 0
[  350s +   1s  3.4G] Canada's Business Registries + registry open data: 2781 vendors, 14321 buyers found; filled {'buyer_bn': 5464, 'buyer_legal_name': 6864, 'vendor_registered_address': 6772, 'vendor_bn9': 8855, 'vendor_legal_name': 6729, 'vendor_registry_status': 6731, 'vendor_incorporation_date': 6942, 'vendor_legal_form': 6738, 'vendor_neq': 491, 'vendor_trading_name': 133, 'buyer_address': 228, 'vendor_skipped_legal_form': 1, 'vendor_bn9_other_registry': 4}
[  350s +   0s  3.4G] award facts from the buyers' own award pages: 237 pairs with a page; filled {'contract_value': 39, 'end_date': 17, 'start_date': 9, 'contract_or_agreement_number': 3, 'solicitation_or_tender_number': 6, 'term': 2, 'po_number_as_published': 1, 'number_of_bids': 1}
[  350s +   1s  3.4G] grants & contributions recipient BNs: 3202 buyers, 454 vendors in file; filled {'buyer_bn': 1584, 'buyer_bn_conflict_noted': 89, 'vendor_bn9': 772, 'buyer_legal_name': 312}
[  362s +  11s  3.5G] buyers' PO / contract open data joined: {'pairs': 7, 'po_filled': 6, 'contract_filled': 1} | records read: 330978 | kept (a row's own buyer-vendor pair): 238
[  371s +   9s  3.7G] back-references: {'dataset rows with lead relationships': 111503, 'lead rows with dataset history': 48}
[  378s +   7s  3.5G] sensitivity tags: {'corrections / detention': 33, 'health: mental health / addiction / sexual health': 325, 'intelligence / security / defence': 21, 'police service / police board': 84, 'courts / tribunals / legal aid': 64, 'child / youth protection': 23, 'police oversight body': 4, 'shelter / crisis / sexual-assault service': 76, 'coroner / medical examiner': 1}
[  382s +   4s  3.5G] site readers, second pass (websites found late): {'buyer_logo': 598, 'vendor_emails': 575, 'vendor_phone': 776, 'vendor_logo': 20729, 'buyer_phone': 49, 'vendor_address': 239, 'buyer_address': 6}
[  383s +   0s  3.5G] listings on a site that is not the Canada-located vendor's own (-> tier E): {'kept — the site prints an address in Canada': 1558, "kept — Wikidata: the site's organisation has its headquarters in Canada": 1229, 'kept — no evidence about whose site it is': 379, "the site's own address is outside Canada": 98, 'from tier D': 710, "Wikidata: the site's organisation has its headquarters outside Canada": 478, "kept — the listing is in the site's Canadian section (/ca/, /en-ca/, ca.…)": 50, 'Canadian arm of a group, site not shown to be its own': 30, "kept although the site reader's address is abroad (Wikidata: headquarters in Canada)": 34, "the vendor's published terms: its Canadian entity does not contract with customers of this buyer's country": 104, "kept — address abroad on the site, but a corporation of the site's name is registered in Canada": 10}
[  385s +   2s  3.5G] same-vendor carry-over (BN9, identity facts and address from the vendor's other rows): {'address': 120, 'bn9': 75860, 'legal_name': 75856, 'trading_name': 75857, 'gst_hst_derived': 75860, 'registry_id': 75854, 'registry_url': 75854, 'registered_address': 75854, 'legal_form': 75854, 'registry_status': 75854, 'registry_match_level': 75855, 'incorporation_date': 75854, 'phone': 3, 'logo_url': 4, 'neq': 1}
[  511s + 127s  3.5G] rows written: 100000 of 172770
[  608s +  97s  3.4G] narrative columns: {'mailbox meta found': 166738, 'contract_description_from_title': 122788, 'contract_title_from_description': 142, 'invoice_reference_hint_po_rule': 1167, 'records_with_this_vendor_lead': 153330, 'mailbox meta missing': 1507}
[  608s +   0s  3.4G] downstream pack: {'tax_derived_foreign': 9831, 'pay_on_sight_yes': 2077, 'ap_payable_today': 1544, 'ship_ready_yes': 861, 'buyer_trade_name_as_published': 118442, 'tax_derived': 114196, 'registry_note': 221, 'prompt_payment_default': 505, 'pay_on_sight_no': 112708, 'buyer_type_from_name': 12658, 'sensitivity_extra': 171, 'registry_warning': 1133, 'invoice_currency_derived': 157326, 'buyer_address_from_own_page': 2924, 'pay_on_sight_routed': 53460, 'currency_default': 2}
[  608s +   0s  3.4G] rows 172770
[  608s +   0s  3.4G] [('GOLD', 625), ('A0', 519), ('A1', 712), ('A2', 92), ('A3', 223), ('A4', 8), ('B0', 623), ('B1', 992), ('B2', 130), ('B3', 186), ('B4', 12), ('C0', 1003), ('C1', 252), ('C2', 19), ('C3', 26), ('C4', 26), ('D0', 408), ('D1', 19846), ('D2', 162), ('D3', 512), ('D4', 286), ('E0', 204), ('E1', 4143), ('E2', 92), ('E3', 114), ('E4', 101), ('F0', 1), ('F1', 4), ('F2', 1), ('F3', 2), ('F4', 1), ('GOLD-M', 60), ('GOLD-T', 272), ('I0', 616), ('I1', 13791), ('I2', 63), ('I3', 225), ('I4', 103), ('L0', 217), ('L1', 304), ('L2', 32), ('L3', 19), ('L4', 71), ('M0', 28), ('M1', 4991), ('M2', 21), ('M3', 64), ('M4', 1), ('R0', 122), ('R1', 74574), ('R2', 92), ('R3', 900), ('R4', 164), ('T0', 784), ('T1', 43120), ('T2', 122), ('T3', 679), ('T4', 10)]
[  608s +   0s  3.4G] with any email: 168245 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            625
P01T_active_service_seen_on_buyer_site_invoicing_AP_email    272
P02_active_relationship_finance_accounting_email           460
P03_active_relationship_purchasing_email                   255
P04_active_relationship_general_email (2 part files)      3199
P05_likely_active_awarded_12_36_months_any_email           413
P06_client_listing_invoicing_AP_email                      276
P06T_active_service_seen_on_buyer_site_other_email (13 part files)  40549
P07_client_listing_finance_or_purchasing_email             653
P08_client_listing_general_email (6 part files)          19414
P09_older_contract_or_payment_any_email                    303
P10_linked_from_vendor_site_any_email                     2588
P10R_ca_domain_registration_contract_own_email (28 part files)  75079
P11_any_relationship_email_not_yet_confirmed (2 part files)   4832
P12_weaker_relationship_within_5_years_own_email             8
P13_inferred_relationship_no_record_own_email (5 part files)  14182
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email     60
P06M_member_or_regulated_payer_of_canadian_body_other_email (2 part files)   5018
Z_no_email_yet_not_delivered                              4584
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 19837304
package files: compressed (.csv.gz); packages written straight from the table (already in order): 17 of 19; sorted from a working copy: P11 (4832 rows); sorted from a working copy: Z (4584 rows)

# coverage vs the downstream targets (COVERAGE_VS_TARGETS.md)
benchmarks met 52 / 446 (11.7%); near 85; written out/ranked/COVERAGE_VS_TARGETS.md
  gap mta_sts                            P10R      75.5% -> 100%  rows needed 18416
  gap tls_rpt                            P10R      75.5% -> 100%  rows needed 18416
  gap bimi                               P10R      75.5% -> 100%  rows needed 18416
  gap buyer_ap_cycle_published           P10R       0.0% ->  20%  rows needed 15012
  gap ap_system_hint                     P10R       0.2% ->  20%  rows needed 14879
  gap buyer_logo_url                     P08       31.0% -> 100%  rows needed 13401
  gap buyer_phone                        P08       26.7% ->  95%  rows needed 13251
  gap vendor_registered_address          P08        9.1% ->  70%  rows needed 11817
  gap buyer_legal_name_as_published      P08       16.6% ->  75%  rows needed 11343
  gap buyer_esignature_preference        P10R       0.0% ->  15%  rows needed 11246
  gap buyer_tax_exempt_status            P10R       0.0% ->  15%  rows needed 11245
  gap buyer_payment_method_preference    P10R       0.2% ->  15%  rows needed 11117
  gap vendor_logo_url                    P08       45.5% -> 100%  rows needed 10583
  gap vendor_phone                       P08       33.5% ->  85%  rows needed 9989
  gap vendor_bn9                         P08        8.0% ->  50%  rows needed 8158
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
