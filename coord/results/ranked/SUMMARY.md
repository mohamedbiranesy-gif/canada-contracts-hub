# Ranked buyers — 2026-11-09T19:39Z

```
# Changelog — build 2026-11-09T19:35Z (b11ccfb)

Build id = the commit that produced this folder; every build is a full regeneration from the same rules, so the delta below is the only thing downstream needs to apply.

- rows: 66673 → 66674
- Gold (P01): 624 → 624
- field changed: ap_contact_name_as_published: 1
- field changed: ap_phone: 1
- field changed: buyer_address: 51
- field changed: buyer_bn_as_published: 1
- field changed: buyer_legal_name_as_published: 388
- field changed: buyer_phone: 62
mailboxes taken from the verification log (better than org_mailboxes' single pick): 682
team vendor contacts (referee-verified): 8781 vendors; 172 with a billing / AR mailbox
same-pair fill (facts from another record of the same buyer-vendor pair): {'solicitation_or_tender_number': 11, 'number_of_bids': 10, 'award_or_notice_id': 2, 'buyer_vendor_id': 2, 'commodity_codes': 9, 'end_date_inferred': 123, 'contract_value': 7, 'procurement_method': 3, 'contract_description': 3, 'po_number_as_published': 3, 'buyer_org_codes': 1, 'start_from_signed': 496, 'end_date': 1, 'contract_or_agreement_number': 2, 'contract_title': 1}
leads with a borrowed mailbox: 1907 | rows upgraded by a newer dated record: 39 | rows upgraded to an active service seen on the buyer's site: 11
P12 organisations: 107 added: 20 {'no own confirmed mailbox': 69, 'same organisation already in a row': 18} | P13 added: 51255 | P13 skipped: {"mailbox not the organisation's own": 2139, 'bad mailbox': 186, 'not located in Canada (no honest inference)': 2925, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 7661}
extras from the lanes' result rows: {'invoice_mailing_address': 1951, 'invoicing_requirements': 1959, 'ap_phone': 2050, 'invoice_portal_url': 73, 'ap_contact_name': 144}
org_extras: 83533 organisations read; filled {'vendor_logo': 8565, 'vendor_phone_v2': 4714, 'po_required': 180, 'vendor_trading_name_jsonld': 1070, 'buyer_legal_name': 22099, 'buyer_phone_v2': 32161, 'buyer_payment_method_preference_mention_rejected': 17876, 'buyer_logo': 54534, 'payment_terms': 284, 'buyer_tax_exempt_status_mention_rejected': 268, 'buyer_legal_name_v2_rejected_no_overlap': 25787, 'buyer_legal_name_v2_legal_name_stated': 6586, 'buyer_bn': 2162, 'buyer_legal_name_v2_jsonld_name': 2046, 'buyer_legal_name_v2_jsonld_legal_name': 2563, 'ap_system_hint_links': 307, 'buyer_payment_method_preference_mention': 290, 'vendor_legal_name': 1485, 'vendor_neq': 32, 'buyer_esignature_preference_mention_rejected': 486, 'vendor_legal_name_v2': 852, 'buyer_address_v2': 6162, 'p13_name_from_legal_name': 9708, 'buyer_esignature_preference_mention': 18, 'vendor_bn': 184, 'invoice_portal_links': 24, 'buyer_tax_exempt_status_mention': 27, 'vendor_address_v2': 416, 'vendor_bn_jsonld': 6, 'buyer_bn_jsonld': 65, 'buyer_ap_cycle_published_mention': 11, 'vendor_qst': 4, 'buyer_ap_cycle_published_mention_rejected': 31, 'p13_name_from_domain': 2}
regional mailboxes of multinationals removed from other-country entities: 20
mx_check: 69559 domains known; 262 mailboxes on domains with no mail server removed; 226 webmail (freemail) addresses removed
dmarc/spf: 73035 domains known; rows {'enforced': 16210, 'exposed': 47921}
same organisation under another key folded into the row that holds its mailbox: 52
second mailbox of the same organisation (same site and mail domain, same name family) folded: 7
org_contacts: 75023 organisations read; filled {'vendor_phone': 19857, 'vendor_emails': 2356, 'buyer_phone': 36431, 'buyer_address': 27042, 'vendor_address': 2502}
ap_terms (evidence pages re-read): 64855 keys read, 85977 pages used across rows; filled {'payment_terms': 1779, 'po_required': 1351, 'payment_method': 622, 'ap_cycle': 95, 'tax_exempt': 781, 'portal': 1701, 'format': 603, 'context': 46012, 'esignature': 403, 'ap_system_portal': 1518, 'ap_phone': 858, 'buyer_bn': 32, 'ap_contact_name': 794, 'address': 474, 'mailbox_gone': 294, 'ap_system': 222, 'setup_url': 195, 'buyer_phone_from_page': 10083, 'buyer_address_from_page': 1760}
peppol: 77 Canadian participants; matched buyers 2, vendors 36
municipal / organisation directories: {'matched': 1819, 'legal_name': 754, 'address': 52, 'phone': 299, 'matched_by_place_name': 11, 'website': 17}
charity buyers: {'matched': 7452, 'bn': 6153, 'legal_name': 4061, 'address': 327, 'website': 26}
wikidata: {'vendors': 1047, 'buyers': 5504, 'buyer_legal_name': 2459, 'buyer_phone': 88, 'buyer_address': 665, 'buyer_website': 109, 'vendor_legal_name': 36, 'vendor_address': 290, 'vendor_website': 203, 'vendor_neq': 6}
crown-corporation BNs applied to inferred-vendor rows: 47017
vendor websites confirmed from search proposals: 502 applied: 3083
inferred vendors' published phone / address applied: {'phone': 37250}
registry bulk rows added (no API row for the key): 7355
Canada's Business Registries + registry open data: 2787 vendors, 13355 buyers found; filled {'buyer_bn': 4976, 'buyer_legal_name': 7236, 'vendor_registered_address': 3137, 'vendor_bn9': 3327, 'vendor_legal_name': 3092, 'vendor_registry_status': 3093, 'vendor_incorporation_date': 3295, 'vendor_legal_form': 3093, 'vendor_neq': 421, 'vendor_trading_name': 116, 'buyer_address': 203, 'vendor_skipped_legal_form': 1}
award facts from the buyers' own award pages: 237 pairs with a page; filled {'contract_value': 41, 'end_date': 17, 'start_date': 10, 'number_of_bids': 2, 'contract_or_agreement_number': 3, 'solicitation_or_tender_number': 7, 'term': 2, 'po_number_as_published': 1}
grants & contributions recipient BNs: 3202 buyers, 454 vendors in file; filled {'buyer_bn': 1675, 'buyer_bn_conflict_noted': 93, 'vendor_bn9': 817, 'buyer_legal_name': 339}
buyers' PO / contract open data joined: {'pairs': 9, 'po_filled': 8, 'contract_filled': 1} | records: 555539
back-references: {'dataset rows with lead relationships': 9786, 'lead rows with dataset history': 116}
sensitivity tags: {'corrections / detention': 25, 'health: mental health / addiction / sexual health': 191, 'intelligence / security / defence': 15, 'police service / police board': 62, 'courts / tribunals / legal aid': 44, 'child / youth protection': 18, 'police oversight body': 3, 'shelter / crisis / sexual-assault service': 54, 'coroner / medical examiner': 1}
site readers, second pass (websites found late): {'buyer_logo': 605, 'vendor_emails': 544, 'vendor_phone': 894, 'vendor_logo': 45585, 'buyer_phone': 48, 'vendor_address': 291, 'buyer_address': 6}
same-vendor carry-over (BN9 / address from the vendor's other rows): {'bn9': 47, 'address': 58}
narrative columns: {'mailbox meta found': 61487, 'contract_description_from_title': 9329, 'contract_title_from_description': 163, 'invoice_reference_hint_po_rule': 785, 'records_with_this_vendor_lead': 10690, 'mailbox meta missing': 2154}
downstream pack: {'tax_derived_foreign': 2194, 'pay_on_sight_yes': 1670, 'ap_payable_today': 990, 'ship_ready_yes': 637, 'tax_derived': 50106, 'registry_note': 219, 'prompt_payment_default': 135, 'pay_on_sight_no': 39704, 'buyer_type_from_name': 7827, 'sensitivity_extra': 120, 'registry_warning': 1004, 'invoice_currency_derived': 59027, 'pay_on_sight_routed': 22267, 'currency_default': 2}
rows 66693
[('GOLD', 624), ('A0', 518), ('A1', 710), ('A2', 92), ('A3', 226), ('A4', 8), ('B0', 626), ('B1', 915), ('B2', 128), ('B3', 182), ('B4', 11), ('C0', 1002), ('C1', 319), ('C2', 20), ('C3', 34), ('C4', 29), ('D0', 113), ('D1', 3178), ('D2', 120), ('D3', 149), ('D4', 176), ('E0', 94), ('E1', 2585), ('E2', 45), ('E3', 74), ('E4', 59), ('F0', 1), ('F1', 11), ('F2', 2), ('F3', 3), ('F4', 3), ('GOLD-M', 18), ('GOLD-T', 92), ('I0', 448), ('I1', 49392), ('I2', 174), ('I3', 930), ('I4', 311), ('L0', 220), ('L1', 272), ('L2', 34), ('L3', 23), ('L4', 68), ('M0', 10), ('M1', 135), ('M2', 9), ('M3', 26), ('M4', 1), ('T0', 20), ('T1', 2319), ('T2', 48), ('T3', 84), ('T4', 2)]
with any email: 63641 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            624
P01T_active_service_seen_on_buyer_site_invoicing_AP_email     92
P02_active_relationship_finance_accounting_email           404
P03_active_relationship_purchasing_email                   208
P04_active_relationship_general_email                     1566
P05_likely_active_awarded_12_36_months_any_email           384
P06_client_listing_invoicing_AP_email                      166
P06T_active_service_seen_on_buyer_site_other_email        2440
P07_client_listing_finance_or_purchasing_email             252
P08_client_listing_general_email                          3039
P09_older_contract_or_payment_any_email                    381
P10_linked_from_vendor_site_any_email                     2596
P11_any_relationship_email_not_yet_confirmed               474
P12_weaker_relationship_within_5_years_own_email            19
P13_inferred_relationship_no_record_own_email (18 part files)  50807
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email     18
P06M_member_or_regulated_payer_of_canadian_body_other_email    168
Z_no_email_yet_not_delivered                              3055
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 7625728

# coverage vs the downstream targets (COVERAGE_VS_TARGETS.md)
benchmarks met 101 / 438 (23.1%); near 83; written out/ranked/COVERAGE_VS_TARGETS.md
  gap buyer_ap_cycle_published           P13        0.0% ->  20%  rows needed 10154
  gap ap_system_hint                     P13        0.6% ->  20%  rows needed 9871
  gap buyer_address                      P13       76.0% ->  95%  rows needed 9645
  gap buyer_phone                        P13       79.3% ->  95%  rows needed 7989
  gap buyer_tax_exempt_status            P13        0.1% ->  15%  rows needed 7586
  gap buyer_esignature_preference        P13        0.1% ->  15%  rows needed 7583
  gap buyer_payment_method_preference    P13        0.5% ->  15%  rows needed 7344
  gap buyer_logo_url                     P13       84.2% ->  95%  rows needed 5474
  gap buyer_legal_name_as_published      P13       52.3% ->  60%  rows needed 3916
  gap buyer_bn_as_published              P13       24.7% ->  30%  rows needed 2713
  gap buyer_legal_name_as_published      P08       36.8% ->  75%  rows needed 1161
  gap buyer_legal_name_as_published      P10       32.0% ->  70%  rows needed 986
  gap buyer_address                      P08       66.2% ->  95%  rows needed 876
  gap vendor_emails                      P08       48.7% ->  75%  rows needed 801
  gap buyer_address                      P10       65.1% ->  95%  rows needed 777
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
