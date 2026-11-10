# Ranked buyers — 2026-11-10T04:42Z

```
# Changelog — build 2026-11-10T04:37Z (1b8683a)

Build id = the commit that produced this folder; every build is a full regeneration from the same rules, so the delta below is the only thing downstream needs to apply.

- rows: 68855 → 72030
- Gold (P01): 624 → 625
- field changed: ap_contact_name_as_published: 4
- field changed: ap_phone: 8
- field changed: buyer_address: 1174
- field changed: buyer_bn_as_published: 33
- field changed: buyer_legal_name_as_published: 63
- field changed: buyer_phone: 11
mailboxes taken from the verification log (better than org_mailboxes' single pick): 732
team vendor contacts (referee-verified): 8781 vendors; 172 with a billing / AR mailbox
same-pair fill (facts from another record of the same buyer-vendor pair): {'solicitation_or_tender_number': 11, 'number_of_bids': 10, 'award_or_notice_id': 2, 'buyer_vendor_id': 2, 'commodity_codes': 9, 'end_date_inferred': 123, 'contract_value': 7, 'procurement_method': 3, 'contract_description': 3, 'po_number_as_published': 3, 'buyer_org_codes': 1, 'start_from_signed': 497, 'end_date': 3, 'contract_or_agreement_number': 2, 'contract_title': 1}
leads: 98145 (27155 from the cloud row factory; 0 websites from the lead site finder)
lead rows: facts from the buyer's own pages / the vendor's link label: {'buyer_address_from_own_page': 6689, 'buyer_name_from_own_home_page': 6938, 'buyer_name_from_vendor_link_label': 1624, 'buyer_address_from_member_directory': 201}
leads with a borrowed mailbox: 2846 | rows upgraded by a newer dated record: 39 | rows upgraded to an active service seen on the buyer's site: 11
P12 organisations: 106 added: 19 {'no own confirmed mailbox': 69, 'same organisation already in a row': 18} | P13 added: 49412 | P13 skipped: {"mailbox not the organisation's own": 2154, 'bad mailbox': 186, 'not located in Canada (no honest inference)': 3211, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 10056}
lead rows that took the organisation's own key (registry facts attach): {'rows': 5250, 'buyer_address': 537, 'buyer_name': 815}
extras from the lanes' result rows: {'invoice_mailing_address': 2004, 'invoicing_requirements': 1986, 'ap_phone': 2103, 'invoice_portal_url': 74, 'ap_contact_name': 153}
org_extras: 83559 organisations read; filled {'vendor_logo': 11119, 'vendor_phone_v2': 6296, 'po_required': 186, 'vendor_trading_name_jsonld': 1190, 'buyer_legal_name': 22273, 'buyer_phone_v2': 32167, 'buyer_payment_method_preference_mention_rejected': 17870, 'buyer_logo': 54761, 'payment_terms': 306, 'buyer_tax_exempt_status_mention_rejected': 268, 'buyer_legal_name_v2_rejected_no_overlap': 25630, 'buyer_legal_name_v2_legal_name_stated': 6670, 'buyer_bn': 2165, 'buyer_legal_name_v2_jsonld_name': 2064, 'buyer_legal_name_v2_jsonld_legal_name': 2582, 'ap_system_hint_links': 307, 'buyer_payment_method_preference_mention': 290, 'vendor_legal_name': 2046, 'vendor_neq': 36, 'buyer_esignature_preference_mention_rejected': 487, 'vendor_legal_name_v2': 1203, 'buyer_address_v2': 5809, 'p13_name_from_legal_name': 8822, 'buyer_esignature_preference_mention': 18, 'vendor_bn': 285, 'invoice_portal_links': 24, 'buyer_tax_exempt_status_mention': 27, 'vendor_address_v2': 416, 'vendor_bn_jsonld': 20, 'buyer_bn_jsonld': 65, 'buyer_ap_cycle_published_mention': 11, 'vendor_qst': 4, 'buyer_ap_cycle_published_mention_rejected': 31, 'p13_name_from_domain': 2}
regional mailboxes of multinationals removed from other-country entities: 31
mx_check: 69559 domains known; 263 mailboxes on domains with no mail server removed; 233 webmail (freemail) addresses removed
dmarc/spf: 79269 domains known; rows {'enforced': 17618, 'exposed': 51854}
same organisation under another key folded into the row that holds its mailbox: 52
second mailbox of the same organisation (same site and mail domain, same name family) folded: 6
org_contacts: 75051 organisations read; filled {'vendor_phone': 21265, 'vendor_emails': 4471, 'buyer_phone': 36594, 'buyer_address': 23940, 'vendor_address': 2510}
ap_terms (evidence pages re-read): 64855 keys read, 85913 pages used across rows; filled {'payment_terms': 1778, 'po_required': 1349, 'payment_method': 622, 'ap_cycle': 95, 'tax_exempt': 782, 'portal': 1700, 'format': 603, 'context': 45950, 'esignature': 401, 'ap_system_portal': 1517, 'ap_phone': 855, 'buyer_bn': 32, 'ap_contact_name': 794, 'address': 474, 'mailbox_gone': 298, 'ap_system': 221, 'setup_url': 194, 'buyer_phone_from_page': 10084, 'buyer_address_from_page': 1602}
peppol: 77 Canadian participants; matched buyers 3, vendors 36
municipal / organisation directories: {'matched': 1820, 'legal_name': 762, 'address': 53, 'phone': 298, 'matched_by_place_name': 10, 'website': 17}
charity buyers: {'matched': 7399, 'bn': 6112, 'legal_name': 4025, 'address': 318, 'website': 26}
wikidata: {'vendors': 1053, 'buyers': 5432, 'buyer_legal_name': 2416, 'buyer_phone': 88, 'buyer_address': 649, 'buyer_website': 109, 'vendor_legal_name': 36, 'vendor_address': 292, 'vendor_website': 204, 'vendor_neq': 6}
crown-corporation BNs applied to inferred-vendor rows: 45349
vendor websites confirmed from search proposals: 502 applied: 3352
inferred vendors' published phone / address applied: {'phone': 35945}
registry bulk rows added (no API row for the key): 7508
Canada's Business Registries + registry open data: 2798 vendors, 14357 buyers found; filled {'buyer_bn': 5613, 'buyer_legal_name': 7990, 'vendor_registered_address': 3371, 'vendor_bn9': 3532, 'vendor_legal_name': 3325, 'vendor_registry_status': 3326, 'vendor_incorporation_date': 3527, 'vendor_legal_form': 3326, 'vendor_neq': 572, 'vendor_trading_name': 110, 'buyer_address': 250, 'vendor_skipped_legal_form': 1, 'vendor_bn9_other_registry': 4}
award facts from the buyers' own award pages: 237 pairs with a page; filled {'contract_value': 41, 'end_date': 17, 'start_date': 10, 'number_of_bids': 2, 'contract_or_agreement_number': 3, 'solicitation_or_tender_number': 7, 'term': 2, 'po_number_as_published': 1}
grants & contributions recipient BNs: 3202 buyers, 454 vendors in file; filled {'buyer_bn': 1649, 'buyer_bn_conflict_noted': 94, 'vendor_bn9': 840, 'buyer_legal_name': 327}
buyers' PO / contract open data joined: {'pairs': 10, 'po_filled': 9, 'contract_filled': 1} | records: 555539
back-references: {'dataset rows with lead relationships': 16533, 'lead rows with dataset history': 113}
sensitivity tags: {'corrections / detention': 26, 'health: mental health / addiction / sexual health': 196, 'intelligence / security / defence': 15, 'police service / police board': 66, 'courts / tribunals / legal aid': 46, 'child / youth protection': 18, 'police oversight body': 3, 'shelter / crisis / sexual-assault service': 58, 'coroner / medical examiner': 1}
site readers, second pass (websites found late): {'buyer_logo': 607, 'vendor_emails': 545, 'vendor_phone': 895, 'vendor_logo': 44309, 'buyer_phone': 48, 'vendor_address': 292, 'buyer_address': 6}
same-vendor carry-over (BN9 / address from the vendor's other rows): {'bn9': 48, 'address': 136}
narrative columns: {'mailbox meta found': 66703, 'contract_description_from_title': 9431, 'contract_title_from_description': 163, 'invoice_reference_hint_po_rule': 790, 'records_with_this_vendor_lead': 17886, 'mailbox meta missing': 2207}
downstream pack: {'tax_derived_foreign': 3165, 'pay_on_sight_yes': 2026, 'ap_payable_today': 1010, 'ship_ready_yes': 639, 'buyer_trade_name_as_published': 32019, 'tax_derived': 54467, 'registry_note': 220, 'prompt_payment_default': 137, 'pay_on_sight_no': 30604, 'buyer_type_from_name': 8708, 'sensitivity_extra': 126, 'registry_warning': 1002, 'invoice_currency_derived': 63405, 'buyer_address_from_own_page': 2818, 'pay_on_sight_routed': 36280, 'currency_default': 2}
rows 72049
[('GOLD', 625), ('A0', 516), ('A1', 713), ('A2', 92), ('A3', 225), ('A4', 8), ('B0', 624), ('B1', 916), ('B2', 129), ('B3', 182), ('B4', 11), ('C0', 1002), ('C1', 321), ('C2', 20), ('C3', 34), ('C4', 29), ('D0', 188), ('D1', 9195), ('D2', 159), ('D3', 311), ('D4', 237), ('E0', 112), ('E1', 2841), ('E2', 54), ('E3', 84), ('E4', 61), ('F0', 1), ('F1', 11), ('F2', 2), ('F3', 3), ('F4', 2), ('GOLD-M', 18), ('GOLD-T', 93), ('I0', 444), ('I1', 47634), ('I2', 162), ('I3', 889), ('I4', 283), ('L0', 219), ('L1', 273), ('L2', 35), ('L3', 23), ('L4', 68), ('M0', 10), ('M1', 135), ('M2', 9), ('M3', 26), ('M4', 1), ('T0', 23), ('T1', 2856), ('T2', 49), ('T3', 89), ('T4', 2)]
with any email: 68910 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            625
P01T_active_service_seen_on_buyer_site_invoicing_AP_email     93
P02_active_relationship_finance_accounting_email           403
P03_active_relationship_purchasing_email                   209
P04_active_relationship_general_email                     1570
P05_likely_active_awarded_12_36_months_any_email           386
P06_client_listing_invoicing_AP_email                      227
P06T_active_service_seen_on_buyer_site_other_email (2 part files)   2983
P07_client_listing_finance_or_purchasing_email             449
P08_client_listing_general_email (3 part files)           8926
P09_older_contract_or_payment_any_email                    383
P10_linked_from_vendor_site_any_email                     2874
P11_any_relationship_email_not_yet_confirmed               607
P12_weaker_relationship_within_5_years_own_email            18
P13_inferred_relationship_no_record_own_email (18 part files)  48968
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email     18
P06M_member_or_regulated_payer_of_canadian_body_other_email    168
Z_no_email_yet_not_delivered                              3142
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 8345415

# coverage vs the downstream targets (COVERAGE_VS_TARGETS.md)
benchmarks met 102 / 438 (23.3%); near 69; written out/ranked/COVERAGE_VS_TARGETS.md
  gap buyer_ap_cycle_published           P13        0.0% ->  20%  rows needed 9786
  gap ap_system_hint                     P13        0.6% ->  20%  rows needed 9519
  gap buyer_phone                        P13       78.8% ->  95%  rows needed 7943
  gap buyer_tax_exempt_status            P13        0.1% ->  15%  rows needed 7312
  gap buyer_esignature_preference        P13        0.1% ->  15%  rows needed 7310
  gap buyer_payment_method_preference    P13        0.5% ->  15%  rows needed 7081
  gap buyer_address                      P13       81.2% ->  95%  rows needed 6752
  gap buyer_logo_url                     P13       83.7% ->  95%  rows needed 5517
  gap buyer_phone                        P08       44.0% ->  95%  rows needed 4557
  gap vendor_registered_address          P08       20.0% ->  70%  rows needed 4461
  gap buyer_legal_name_as_published      P08       25.2% ->  75%  rows needed 4446
  gap buyer_logo_url                     P08       50.5% -> 100%  rows needed 4421
  gap buyer_legal_name_as_published      P13       51.8% ->  60%  rows needed 4006
  gap vendor_logo_url                    P08       55.5% -> 100%  rows needed 3968
  gap vendor_phone                       P08       43.0% ->  85%  rows needed 3750
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
