# Ranked buyers — 2026-11-10T14:30Z

```
[   11s +  11s  1.1G] mailboxes taken from the verification log (better than org_mailboxes' single pick): 784 | referee mailbox rows whose last label is not a top-level domain: {'left out': 156, 'cut back to the address the page prints': 706}
[   23s +  12s  0.6G] vendor table: registry matches not used because the legal form differs (partnership vs corporation): 55 | 'websites' that are a web host's own site (dropped with their mailboxes): 5 | websites not used for a look-up by domain (unverified, name does not fit): 0 | look-ups by domain: 8051
[   23s +   0s  0.6G] team vendor contacts (referee-verified): 8781 vendors; 172 with a billing / AR mailbox
[  200s + 177s  2.0G] same-pair fill (facts from another record of the same buyer-vendor pair): {'solicitation_or_tender_number': 11, 'number_of_bids': 10, 'award_or_notice_id': 2, 'buyer_vendor_id': 2, 'commodity_codes': 9, 'end_date_inferred': 120, 'contract_value': 7, 'procurement_method': 3, 'po_number_as_published': 3, 'buyer_org_codes': 1, 'start_from_signed': 497, 'end_date': 3, 'contract_description': 2, 'contract_or_agreement_number': 2, 'contract_title': 1}
[  200s +   0s  2.0G] contract records whose vendor's registry match pairs a partnership with a corporation (registry cells not used): 2244
[  207s +   7s  2.5G] tenant leads from the shards: 7673
[  207s +   0s  2.5G] leads: 366664 (288001 from the cloud row factory; 49 websites from the lead site finder)
[  228s +  21s  2.6G] registry leads (.ca domains carrying a confirmed mailbox of their own organisation): 112851
[  247s +  19s  2.8G] lead rows: facts from the buyer's own pages / the vendor's link label: {'buyer_address_from_own_page': 79541, 'buyer_name_from_own_home_page': 88597, 'vendor_address_cut_out_of_its_quote': 12317, 'buyer_legal_name_from_register': 4050, 'buyer_address_from_member_directory': 3831, 'buyer_name_from_vendor_link_label': 1922} | sites named again from their stored home-page title: 1079
[  247s +   0s  2.8G] client-page links judged (cloud row factory): {'client listing: label names the site': 3266, 'link only, and the site has a .ca registration: the registration takes the row': 1570, "not shown to be a client: the link's label does not name the linked site": 1187, "client listing: 'visit website' on a client page": 248, 'client listing: portfolio page': 177, 'client listing: page address names the site': 174, 'not shown to be a client: a page for clients (forms, resources, login), not a list of them': 167, "not shown to be a client: an organisation's 'our work' programme page": 121, "not shown to be a client: sister site of the page's owner": 87, 'not shown to be a client: article: the client word sits in a slug of 4 words': 34, 'not shown to be a client: dated article': 20, 'not shown to be a client: article: the client word sits in a slug of 5 words': 11, 'not shown to be a client: article: the client word sits in a slug of 6 words': 1}
[  252s +   5s  2.8G] leads with a borrowed mailbox: 92565 | rows upgraded by a newer dated record: 42 | rows upgraded to an active service seen on the buyer's site: 384
[  262s +  11s  2.9G] P12 organisations: 93 added: 9 {'no own confirmed mailbox': 66, 'same organisation already in a row': 18} | P13 added: 14858 | P13 skipped: {"mailbox not the organisation's own": 2152, 'bad mailbox': 188, 'not located in Canada (no honest inference)': 7175, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 59038}
[  262s +   0s  2.9G] lead rows that took the organisation's own key (registry facts attach): {'rows': 44346, 'buyer_address': 4963, 'buyer_name': 3242}
[  281s +  19s  2.9G] extras from the lanes' result rows: {'invoice_mailing_address': 2278, 'invoicing_requirements': 2098, 'ap_phone': 2373, 'invoice_portal_url': 73, 'ap_contact_name': 224}
[  301s +  20s  2.9G] org_extras: 83559 organisations read; filled {'vendor_logo': 26483, 'vendor_phone_v2': 12433, 'po_required': 226, 'vendor_trading_name_jsonld': 1915, 'buyer_legal_name': 22362, 'buyer_phone_v2': 30908, 'buyer_payment_method_preference_mention_rejected': 17918, 'buyer_logo': 57645, 'payment_terms': 554, 'buyer_tax_exempt_status_mention_rejected': 271, 'buyer_legal_name_v2_rejected_no_overlap': 26312, 'buyer_legal_name_v2_legal_name_stated': 6220, "vendor site is a foreign organisation's: its legal / trading name not taken for the Canada-located vendor": 1152, 'buyer_bn': 2186, 'buyer_legal_name_v2_jsonld_name': 2258, 'buyer_legal_name_v2_jsonld_legal_name': 2665, 'ap_system_hint_links': 317, 'buyer_legal_name_government_template_credit': 43, 'buyer_payment_method_preference_mention': 293, 'vendor_legal_name': 3225, 'vendor_neq': 65, 'buyer_esignature_preference_mention_rejected': 487, 'vendor_legal_name_v2': 2258, 'buyer_address_v2': 4030, 'p13_name_from_legal_name': 5865, 'buyer_esignature_preference_mention': 18, 'vendor_bn': 430, 'invoice_portal_links': 24, 'buyer_tax_exempt_status_mention': 29, 'vendor_address_v2': 280, 'vendor_address_v2_outside_canada_not_taken': 105, 'buyer_bn_jsonld': 65, 'buyer_ap_cycle_published_mention': 11, 'vendor_qst': 7, 'vendor_bn_jsonld': 22, 'buyer_ap_cycle_published_mention_rejected': 31, 'p13_name_from_domain': 1}
[  302s +   0s  2.9G] regional mailboxes of multinationals removed from other-country entities: 44
[  302s +   0s  2.9G] mx_check: 69559 domains known; 184 mailboxes on domains with no mail server removed; 591 webmail (freemail) addresses removed
[  305s +   2s  2.9G] dmarc/spf: 150756 domains known; rows {'enforced': 30974, 'exposed': 109589}
[  305s +   0s  2.9G] same organisation under another key folded into the row that holds its mailbox: 52
[  307s +   2s  2.9G] second mailbox of the same organisation (same site and mail domain, same name family) folded: 6
[  310s +   3s  3.0G] org_contacts: 75051 organisations read; filled {'vendor_phone': 22867, 'vendor_emails': 14557, 'buyer_phone': 38445, 'vendor site prints an address outside Canada: address and telephone not taken': 815, 'buyer_address': 13647, 'vendor_address': 1983}
[  318s +   8s  3.3G] ap_terms (evidence pages re-read): 77239 keys read, 101816 pages used across rows; filled {'payment_terms': 2918, 'po_required': 1771, 'payment_method': 675, 'ap_cycle': 104, 'tax_exempt': 955, 'portal': 1913, 'format': 710, 'context': 45840, 'esignature': 550, 'ap_system_portal': 1669, 'ap_phone': 1040, 'buyer_bn': 52, 'ap_contact_name': 824, 'address': 539, 'mailbox_gone': 334, 'ap_system': 377, 'setup_url': 289, 'buyer_phone_from_page': 9669, 'buyer_address_from_page': 632}
[  320s +   2s  3.3G] peppol: 77 Canadian participants; matched buyers 5, vendors 38
[  321s +   2s  3.3G] municipal / organisation directories: {'matched': 1776, 'legal_name': 804, 'address': 56, 'phone': 309, 'matched_by_place_name': 10, 'website': 17}
[  322s +   0s  3.3G] charity buyers: {'matched': 7283, 'bn': 6022, 'legal_name': 4207, 'address': 304, 'website': 25}
[  323s +   1s  3.3G] wikidata: {'vendors': 1156, 'buyers': 5268, 'buyer_legal_name': 2454, 'buyer_phone': 86, 'buyer_address': 630, 'buyer_website': 109, 'vendor_legal_name': 42, 'vendor_address': 405, 'vendor_website': 237, 'vendor_neq': 7}
[  323s +   0s  3.3G] crown-corporation BNs applied to inferred-vendor rows: 13458
[  323s +   0s  3.3G] vendor websites confirmed from search proposals: 502 applied: 8581
[  323s +   0s  3.3G] inferred vendors' published phone / address applied: {'phone': 10409}
[  324s +   0s  3.3G] registry bulk rows added (no API row for the key): 7455 | registry rows left out, the registered name is only legal-form and place words: 0
[  325s +   1s  3.3G] Canada's Business Registries + registry open data: 2781 vendors, 14321 buyers found; filled {'buyer_bn': 5469, 'buyer_legal_name': 6868, 'vendor_registered_address': 4405, 'vendor_bn9': 8817, 'vendor_legal_name': 4362, 'vendor_registry_status': 4364, 'vendor_incorporation_date': 4574, 'vendor_legal_form': 4371, 'vendor_neq': 456, 'vendor_trading_name': 134, 'buyer_address': 228, 'vendor_skipped_legal_form': 1, 'vendor_bn9_other_registry': 4}
[  325s +   0s  3.3G] award facts from the buyers' own award pages: 237 pairs with a page; filled {'contract_value': 39, 'end_date': 17, 'start_date': 9, 'contract_or_agreement_number': 3, 'solicitation_or_tender_number': 6, 'term': 2, 'po_number_as_published': 1, 'number_of_bids': 1}# Changelog — build 2026-11-10T14:21Z (e6420d0)

Build id = the commit that produced this folder; every build is a full regeneration from the same rules, so the delta below is the only thing downstream needs to apply.

- rows: 169750 → 169749
- Gold (P01): 625 → 625
- field changed: ap_contact_name_as_published: 34
- field changed: ap_phone: 191
- field changed: buyer_address: 226
- field changed: buyer_bn_as_published: 22
- field changed: buyer_legal_name_as_published: 1999
- field changed: buyer_phone: 1

[  325s +   1s  3.3G] grants & contributions recipient BNs: 3202 buyers, 454 vendors in file; filled {'buyer_bn': 1585, 'buyer_bn_conflict_noted': 89, 'vendor_bn9': 772, 'buyer_legal_name': 312}
[  337s +  11s  3.4G] buyers' PO / contract open data joined: {'pairs': 7, 'po_filled': 6, 'contract_filled': 1} | records read: 330978 | kept (a row's own buyer-vendor pair): 238
[  347s +  11s  3.6G] back-references: {'dataset rows with lead relationships': 111564, 'lead rows with dataset history': 47}
[  354s +   7s  3.5G] sensitivity tags: {'corrections / detention': 33, 'health: mental health / addiction / sexual health': 308, 'intelligence / security / defence': 21, 'police service / police board': 84, 'courts / tribunals / legal aid': 64, 'child / youth protection': 23, 'police oversight body': 4, 'shelter / crisis / sexual-assault service': 76, 'coroner / medical examiner': 1}
[  359s +   5s  3.5G] site readers, second pass (websites found late): {'buyer_logo': 597, 'vendor_emails': 571, 'vendor_phone': 772, 'vendor_logo': 20747, 'buyer_phone': 48, 'vendor_address': 239, 'buyer_address': 6}
[  359s +   0s  3.5G] listings on a site that is not the Canada-located vendor's own (-> tier E): {'kept — the site prints an address in Canada': 1561, "kept — Wikidata: the site's organisation has its headquarters in Canada": 1230, 'kept — no evidence about whose site it is': 379, "the site's own address is outside Canada": 98, 'from tier D': 710, "Wikidata: the site's organisation has its headquarters outside Canada": 478, "kept — the listing is in the site's Canadian section (/ca/, /en-ca/, ca.…)": 50, 'Canadian arm of a group, site not shown to be its own': 30, "kept although the site reader's address is abroad (Wikidata: headquarters in Canada)": 34, "the vendor's published terms: its Canadian entity does not contract with customers of this buyer's country": 104, "kept — address abroad on the site, but a corporation of the site's name is registered in Canada": 10}
[  361s +   2s  3.5G] same-vendor carry-over (BN9, identity facts and address from the vendor's other rows): {'address': 119, 'bn9': 75863, 'legal_name': 75859, 'trading_name': 75860, 'gst_hst_derived': 75863, 'registry_id': 75857, 'registry_url': 75857, 'registered_address': 75857, 'legal_form': 75857, 'registry_status': 75857, 'registry_match_level': 75858, 'incorporation_date': 75857, 'phone': 3, 'logo_url': 4, 'neq': 1}
[  498s + 137s  3.4G] rows written: 100000 of 169768
[  598s +  99s  3.4G] narrative columns: {'mailbox meta found': 163733, 'contract_description_from_title': 122667, 'contract_title_from_description': 142, 'invoice_reference_hint_po_rule': 1086, 'records_with_this_vendor_lead': 150268, 'mailbox meta missing': 1587}
[  598s +   0s  3.4G] downstream pack: {'tax_derived_foreign': 8083, 'pay_on_sight_yes': 2067, 'ap_payable_today': 1545, 'ship_ready_yes': 859, 'buyer_trade_name_as_published': 115353, 'tax_derived': 112971, 'registry_note': 221, 'prompt_payment_default': 504, 'pay_on_sight_no': 109995, 'buyer_type_from_name': 12458, 'sensitivity_extra': 171, 'registry_warning': 1130, 'invoice_currency_derived': 154365, 'buyer_address_from_own_page': 2950, 'pay_on_sight_routed': 53258, 'currency_default': 2}
[  644s +  46s  3.4G] rows 169768
[  644s +   0s  3.4G] [('GOLD', 625), ('A0', 516), ('A1', 713), ('A2', 92), ('A3', 225), ('A4', 8), ('B0', 623), ('B1', 992), ('B2', 130), ('B3', 186), ('B4', 12), ('C0', 1002), ('C1', 253), ('C2', 19), ('C3', 26), ('C4', 26), ('D0', 404), ('D1', 19877), ('D2', 162), ('D3', 512), ('D4', 286), ('E0', 204), ('E1', 4146), ('E2', 92), ('E3', 114), ('E4', 101), ('F0', 1), ('F1', 4), ('F2', 1), ('F3', 2), ('F4', 1), ('GOLD-M', 61), ('GOLD-T', 269), ('I0', 621), ('I1', 13847), ('I2', 63), ('I3', 225), ('I4', 102), ('L0', 217), ('L1', 304), ('L2', 32), ('L3', 19), ('L4', 71), ('M0', 23), ('M1', 4999), ('M2', 21), ('M3', 64), ('M4', 1), ('R0', 122), ('R1', 74579), ('R2', 91), ('R3', 899), ('R4', 164), ('T0', 715), ('T1', 40104), ('T2', 122), ('T3', 668), ('T4', 10)]
[  644s +   0s  3.4G] with any email: 165320 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            625
P01T_active_service_seen_on_buyer_site_invoicing_AP_email    269
P02_active_relationship_finance_accounting_email           462
P03_active_relationship_purchasing_email                   255
P04_active_relationship_general_email (2 part files)      3204
P05_likely_active_awarded_12_36_months_any_email           413
P06_client_listing_invoicing_AP_email                      276
P06T_active_service_seen_on_buyer_site_other_email (12 part files)  37441
P07_client_listing_finance_or_purchasing_email             653
P08_client_listing_general_email (6 part files)          19441
P09_older_contract_or_payment_any_email                    305
P10_linked_from_vendor_site_any_email                     2591
P10R_ca_domain_registration_contract_own_email (28 part files)  74764
P11_any_relationship_email_not_yet_confirmed (2 part files)   5230
P12_weaker_relationship_within_5_years_own_email             8
P13_inferred_relationship_no_record_own_email (5 part files)  14237
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email     61
P06M_member_or_regulated_payer_of_canadian_body_other_email (2 part files)   5017
Z_no_email_yet_not_delivered                              4516
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 19452879

# coverage vs the downstream targets (COVERAGE_VS_TARGETS.md)
benchmarks met 48 / 446 (10.8%); near 87; written out/ranked/COVERAGE_VS_TARGETS.md
  gap mta_sts                            P10R      75.5% -> 100%  rows needed 18315
  gap tls_rpt                            P10R      75.5% -> 100%  rows needed 18315
  gap bimi                               P10R      75.5% -> 100%  rows needed 18315
  gap buyer_ap_cycle_published           P10R       0.0% ->  20%  rows needed 14949
  gap ap_system_hint                     P10R       0.2% ->  20%  rows needed 14816
  gap buyer_logo_url                     P08       30.9% -> 100%  rows needed 13426
  gap buyer_phone                        P08       26.7% ->  95%  rows needed 13276
  gap vendor_registered_address          P08        9.1% ->  70%  rows needed 11834
  gap buyer_legal_name_as_published      P08       16.6% ->  75%  rows needed 11363
  gap buyer_esignature_preference        P10R       0.0% ->  15%  rows needed 11199
  gap buyer_tax_exempt_status            P10R       0.0% ->  15%  rows needed 11198
  gap buyer_payment_method_preference    P10R       0.2% ->  15%  rows needed 11070
  gap vendor_logo_url                    P08       45.5% -> 100%  rows needed 10598
  gap vendor_phone                       P08       33.5% ->  85%  rows needed 10004
  gap vendor_bn9                         P08        8.0% ->  50%  rows needed 8171
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
