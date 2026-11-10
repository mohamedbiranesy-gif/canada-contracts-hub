# Ranked buyers — 2026-11-10T03:50Z

```
# Changelog — build 2026-11-10T03:45Z (a094218)

Build id = the commit that produced this folder; every build is a full regeneration from the same rules, so the delta below is the only thing downstream needs to apply.

- rows: 67602 → 68855
- Gold (P01): 624 → 624
- field changed: buyer_address: 6244
- field changed: buyer_bn_as_published: 103
- field changed: buyer_legal_name_as_published: 235
- field changed: buyer_phone: 40
- field changed: buyer_website: 1
- field changed: dmarc_policy: 31
mailboxes taken from the verification log (better than org_mailboxes' single pick): 687
team vendor contacts (referee-verified): 8781 vendors; 172 with a billing / AR mailbox
same-pair fill (facts from another record of the same buyer-vendor pair): {'solicitation_or_tender_number': 11, 'number_of_bids': 10, 'award_or_notice_id': 2, 'buyer_vendor_id': 2, 'commodity_codes': 9, 'end_date_inferred': 123, 'contract_value': 7, 'procurement_method': 3, 'contract_description': 3, 'po_number_as_published': 3, 'buyer_org_codes': 1, 'start_from_signed': 497, 'end_date': 3, 'contract_or_agreement_number': 2, 'contract_title': 1}
leads: 97771 (26781 from the cloud row factory; 0 websites from the lead site finder)
lead rows: facts from the buyer's own pages / the vendor's link label: {'buyer_address_from_own_page': 3238, 'buyer_name_from_own_home_page': 3336, 'buyer_name_from_vendor_link_label': 2294, 'buyer_address_from_member_directory': 223}
leads with a borrowed mailbox: 3917 | rows upgraded by a newer dated record: 39 | rows upgraded to an active service seen on the buyer's site: 11
P12 organisations: 106 added: 19 {'no own confirmed mailbox': 69, 'same organisation already in a row': 18} | P13 added: 49313 | P13 skipped: {"mailbox not the organisation's own": 2139, 'bad mailbox': 186, 'not located in Canada (no honest inference)': 2944, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 9695}
lead rows that took the organisation's own key (registry facts attach): {'rows': 5209, 'buyer_address': 809, 'buyer_name': 1106}
extras from the lanes' result rows: {'invoice_mailing_address': 1998, 'invoicing_requirements': 1975, 'ap_phone': 2097, 'invoice_portal_url': 74, 'ap_contact_name': 146}
org_extras: 83559 organisations read; filled {'vendor_logo': 9863, 'vendor_phone_v2': 5568, 'po_required': 181, 'vendor_trading_name_jsonld': 1161, 'buyer_legal_name': 22248, 'buyer_phone_v2': 32171, 'buyer_payment_method_preference_mention_rejected': 17874, 'buyer_logo': 54617, 'payment_terms': 298, 'buyer_tax_exempt_status_mention_rejected': 268, 'buyer_legal_name_v2_rejected_no_overlap': 25604, 'buyer_legal_name_v2_legal_name_stated': 6680, 'buyer_bn': 2166, 'buyer_legal_name_v2_jsonld_name': 2070, 'buyer_legal_name_v2_jsonld_legal_name': 2582, 'ap_system_hint_links': 307, 'buyer_payment_method_preference_mention': 290, 'vendor_legal_name': 1771, 'vendor_neq': 35, 'buyer_esignature_preference_mention_rejected': 486, 'vendor_legal_name_v2': 1048, 'buyer_address_v2': 5892, 'p13_name_from_legal_name': 8871, 'buyer_esignature_preference_mention': 18, 'vendor_bn': 242, 'invoice_portal_links': 24, 'buyer_tax_exempt_status_mention': 27, 'vendor_address_v2': 416, 'vendor_bn_jsonld': 20, 'buyer_bn_jsonld': 65, 'buyer_ap_cycle_published_mention': 11, 'vendor_qst': 4, 'buyer_ap_cycle_published_mention_rejected': 31, 'p13_name_from_domain': 2}
regional mailboxes of multinationals removed from other-country entities: 22
mx_check: 69559 domains known; 263 mailboxes on domains with no mail server removed; 227 webmail (freemail) addresses removed
dmarc/spf: 75077 domains known; rows {'enforced': 16952, 'exposed': 49352}
same organisation under another key folded into the row that holds its mailbox: 52
second mailbox of the same organisation (same site and mail domain, same name family) folded: 6
org_contacts: 75051 organisations read; filled {'vendor_phone': 20279, 'vendor_emails': 3443, 'buyer_phone': 36492, 'buyer_address': 24497, 'vendor_address': 2507}
ap_terms (evidence pages re-read): 64855 keys read, 85966 pages used across rows; filled {'payment_terms': 1780, 'po_required': 1351, 'payment_method': 623, 'ap_cycle': 95, 'tax_exempt': 781, 'portal': 1702, 'format': 603, 'context': 45996, 'esignature': 403, 'ap_system_portal': 1519, 'ap_phone': 858, 'buyer_bn': 32, 'ap_contact_name': 794, 'address': 474, 'mailbox_gone': 298, 'ap_system': 221, 'setup_url': 195, 'buyer_phone_from_page': 10082, 'buyer_address_from_page': 1623}
peppol: 77 Canadian participants; matched buyers 3, vendors 36
municipal / organisation directories: {'matched': 1814, 'legal_name': 755, 'address': 53, 'phone': 298, 'matched_by_place_name': 10, 'website': 17}
charity buyers: {'matched': 7442, 'bn': 6146, 'legal_name': 4047, 'address': 322, 'website': 26}
wikidata: {'vendors': 1048, 'buyers': 5476, 'buyer_legal_name': 2442, 'buyer_phone': 88, 'buyer_address': 657, 'buyer_website': 109, 'vendor_legal_name': 36, 'vendor_address': 290, 'vendor_website': 203, 'vendor_neq': 6}
crown-corporation BNs applied to inferred-vendor rows: 45254
vendor websites confirmed from search proposals: 502 applied: 3233
inferred vendors' published phone / address applied: {'phone': 35928}
registry bulk rows added (no API row for the key): 7508
Canada's Business Registries + registry open data: 2798 vendors, 14357 buyers found; filled {'buyer_bn': 5622, 'buyer_legal_name': 8017, 'vendor_registered_address': 3175, 'vendor_bn9': 3410, 'vendor_legal_name': 3129, 'vendor_registry_status': 3130, 'vendor_incorporation_date': 3331, 'vendor_legal_form': 3130, 'vendor_neq': 542, 'vendor_trading_name': 110, 'buyer_address': 254, 'vendor_skipped_legal_form': 1, 'vendor_bn9_other_registry': 4}
award facts from the buyers' own award pages: 237 pairs with a page; filled {'contract_value': 41, 'end_date': 17, 'start_date': 10, 'number_of_bids': 2, 'contract_or_agreement_number': 3, 'solicitation_or_tender_number': 7, 'term': 2, 'po_number_as_published': 1}
grants & contributions recipient BNs: 3202 buyers, 454 vendors in file; filled {'buyer_bn': 1660, 'buyer_bn_conflict_noted': 94, 'vendor_bn9': 831, 'buyer_legal_name': 333}
buyers' PO / contract open data joined: {'pairs': 10, 'po_filled': 9, 'contract_filled': 1} | records: 555539
back-references: {'dataset rows with lead relationships': 13847, 'lead rows with dataset history': 111}
sensitivity tags: {'corrections / detention': 25, 'health: mental health / addiction / sexual health': 193, 'intelligence / security / defence': 15, 'police service / police board': 65, 'courts / tribunals / legal aid': 46, 'child / youth protection': 18, 'police oversight body': 3, 'shelter / crisis / sexual-assault service': 56, 'coroner / medical examiner': 1}
site readers, second pass (websites found late): {'buyer_logo': 605, 'vendor_emails': 544, 'vendor_phone': 893, 'vendor_logo': 44163, 'buyer_phone': 48, 'vendor_address': 291, 'buyer_address': 6}
same-vendor carry-over (BN9 / address from the vendor's other rows): {'bn9': 48, 'address': 136}
narrative columns: {'mailbox meta found': 63565, 'contract_description_from_title': 9340, 'contract_title_from_description': 163, 'invoice_reference_hint_po_rule': 787, 'records_with_this_vendor_lead': 14810, 'mailbox meta missing': 2194}
downstream pack: {'tax_derived_foreign': 2880, 'pay_on_sight_yes': 2019, 'ap_payable_today': 1010, 'ship_ready_yes': 638, 'buyer_trade_name_as_published': 28425, 'tax_derived': 52111, 'registry_note': 219, 'prompt_payment_default': 137, 'pay_on_sight_no': 27616, 'buyer_type_from_name': 8537, 'sensitivity_extra': 128, 'registry_warning': 997, 'invoice_currency_derived': 60621, 'buyer_address_from_own_page': 2740, 'pay_on_sight_routed': 36124, 'currency_default': 2}
rows 68874
[('GOLD', 624), ('A0', 519), ('A1', 710), ('A2', 92), ('A3', 225), ('A4', 8), ('B0', 626), ('B1', 915), ('B2', 128), ('B3', 183), ('B4', 11), ('C0', 1004), ('C1', 319), ('C2', 20), ('C3', 34), ('C4', 29), ('D0', 171), ('D1', 7107), ('D2', 154), ('D3', 249), ('D4', 221), ('E0', 98), ('E1', 2370), ('E2', 43), ('E3', 68), ('E4', 56), ('F0', 1), ('F1', 11), ('F2', 2), ('F3', 3), ('F4', 2), ('GOLD-M', 18), ('GOLD-T', 93), ('I0', 446), ('I1', 47548), ('I2', 157), ('I3', 880), ('I4', 282), ('L0', 220), ('L1', 272), ('L2', 34), ('L3', 23), ('L4', 68), ('M0', 10), ('M1', 135), ('M2', 9), ('M3', 26), ('M4', 1), ('T0', 20), ('T1', 2493), ('T2', 48), ('T3', 86), ('T4', 2)]
with any email: 65759 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            624
P01T_active_service_seen_on_buyer_site_invoicing_AP_email     93
P02_active_relationship_finance_accounting_email           404
P03_active_relationship_purchasing_email                   208
P04_active_relationship_general_email                     1566
P05_likely_active_awarded_12_36_months_any_email           384
P06_client_listing_invoicing_AP_email                      210
P06T_active_service_seen_on_buyer_site_other_email        2616
P07_client_listing_finance_or_purchasing_email             384
P08_client_listing_general_email (3 part files)           6837
P09_older_contract_or_payment_any_email                    381
P10_linked_from_vendor_site_any_email                     2386
P11_any_relationship_email_not_yet_confirmed               592
P12_weaker_relationship_within_5_years_own_email            18
P13_inferred_relationship_no_record_own_email (17 part files)  48867
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email     18
P06M_member_or_regulated_payer_of_canadian_body_other_email    168
Z_no_email_yet_not_delivered                              3118
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 7935145

# coverage vs the downstream targets (COVERAGE_VS_TARGETS.md)
benchmarks met 98 / 438 (22.4%); near 76; written out/ranked/COVERAGE_VS_TARGETS.md
  gap buyer_ap_cycle_published           P13        0.0% ->  20%  rows needed 9766
  gap ap_system_hint                     P13        0.6% ->  20%  rows needed 9498
  gap buyer_phone                        P13       79.1% ->  95%  rows needed 7767
  gap buyer_tax_exempt_status            P13        0.1% ->  15%  rows needed 7296
  gap buyer_esignature_preference        P13        0.1% ->  15%  rows needed 7294
  gap buyer_payment_method_preference    P13        0.5% ->  15%  rows needed 7066
  gap buyer_address                      P13       81.2% ->  95%  rows needed 6743
  gap buyer_logo_url                     P13       84.0% ->  95%  rows needed 5363
  gap buyer_legal_name_as_published      P13       52.1% ->  60%  rows needed 3867
  gap vendor_registered_address          P08       26.1% ->  70%  rows needed 3002
  gap vendor_logo_url                    P08       59.1% -> 100%  rows needed 2798
  gap buyer_legal_name_as_published      P08       34.5% ->  75%  rows needed 2769
  gap vendor_phone                       P08       46.4% ->  85%  rows needed 2639
  gap vendor_emails                      P08       37.3% ->  75%  rows needed 2576
  gap buyer_phone                        P08       58.4% ->  95%  rows needed 2501
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
