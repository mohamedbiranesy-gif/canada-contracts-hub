# Ranked buyers — 2026-11-10T06:15Z

```
# Changelog — build 2026-11-10T06:09Z (7a55358)

Build id = the commit that produced this folder; every build is a full regeneration from the same rules, so the delta below is the only thing downstream needs to apply.

- rows: 72030 → 73828
- Gold (P01): 625 → 625
- field changed: ap_contact_name_as_published: 4
- field changed: buyer_address: 5
- field changed: buyer_phone: 9
- field changed: buyer_website: 2
- field changed: contract_reference: 36
- field changed: dmarc_policy: 10
mailboxes taken from the verification log (better than org_mailboxes' single pick): 732
team vendor contacts (referee-verified): 8781 vendors; 172 with a billing / AR mailbox
same-pair fill (facts from another record of the same buyer-vendor pair): {'solicitation_or_tender_number': 11, 'number_of_bids': 10, 'award_or_notice_id': 2, 'buyer_vendor_id': 2, 'commodity_codes': 9, 'end_date_inferred': 123, 'contract_value': 7, 'procurement_method': 3, 'contract_description': 3, 'po_number_as_published': 3, 'buyer_org_codes': 1, 'start_from_signed': 497, 'end_date': 3, 'contract_or_agreement_number': 2, 'contract_title': 1}
leads: 126185 (55195 from the cloud row factory; 0 websites from the lead site finder)
registry leads (.ca domains carrying a confirmed mailbox of their own organisation): 42258
lead rows: facts from the buyer's own pages / the vendor's link label: {'buyer_address_from_own_page': 6768, 'buyer_name_from_own_home_page': 7102, 'buyer_name_from_vendor_link_label': 1545, 'buyer_address_from_member_directory': 200}
leads with a borrowed mailbox: 49961 | rows upgraded by a newer dated record: 39 | rows upgraded to an active service seen on the buyer's site: 133
P12 organisations: 96 added: 9 {'no own confirmed mailbox': 67, 'same organisation already in a row': 20} | P13 added: 14040 | P13 skipped: {"mailbox not the organisation's own": 2154, 'bad mailbox': 186, 'not located in Canada (no honest inference)': 3522, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 46229}
lead rows that took the organisation's own key (registry facts attach): {'rows': 41242, 'buyer_address': 5248, 'buyer_name': 1413}
extras from the lanes' result rows: {'invoice_mailing_address': 2174, 'invoicing_requirements': 2035, 'ap_phone': 2269, 'invoice_portal_url': 74, 'ap_contact_name': 158}
org_extras: 83559 organisations read; filled {'vendor_logo': 13197, 'vendor_phone_v2': 7318, 'po_required': 187, 'vendor_trading_name_jsonld': 1408, 'buyer_legal_name': 22328, 'buyer_phone_v2': 32209, 'buyer_payment_method_preference_mention_rejected': 17893, 'buyer_logo': 54962, 'payment_terms': 314, 'buyer_tax_exempt_status_mention_rejected': 269, 'buyer_legal_name_v2_rejected_no_overlap': 25672, 'buyer_legal_name_v2_legal_name_stated': 6679, 'buyer_bn': 2167, 'buyer_legal_name_v2_jsonld_name': 2071, 'buyer_legal_name_v2_jsonld_legal_name': 2583, 'ap_system_hint_links': 316, 'buyer_payment_method_preference_mention': 291, 'vendor_legal_name': 2405, 'vendor_neq': 39, 'buyer_esignature_preference_mention_rejected': 487, 'vendor_legal_name_v2': 1325, 'buyer_address_v2': 5821, 'p13_name_from_legal_name': 8214, 'buyer_esignature_preference_mention': 18, 'vendor_bn': 290, 'invoice_portal_links': 24, 'buyer_tax_exempt_status_mention': 27, 'vendor_address_v2': 382, 'buyer_ap_cycle_published_mention': 11, 'buyer_bn_jsonld': 65, 'vendor_qst': 4, 'vendor_bn_jsonld': 19, 'buyer_ap_cycle_published_mention_rejected': 31, 'p13_name_from_domain': 1}
regional mailboxes of multinationals removed from other-country entities: 33
mx_check: 69559 domains known; 264 mailboxes on domains with no mail server removed; 232 webmail (freemail) addresses removed
dmarc/spf: 81639 domains known; rows {'enforced': 18058, 'exposed': 53209}
same organisation under another key folded into the row that holds its mailbox: 52
second mailbox of the same organisation (same site and mail domain, same name family) folded: 6
org_contacts: 75051 organisations read; filled {'vendor_phone': 15388, 'vendor_emails': 5769, 'buyer_phone': 36738, 'buyer_address': 24291, 'vendor_address': 2311}
ap_terms (evidence pages re-read): 64855 keys read, 85604 pages used across rows; filled {'payment_terms': 1760, 'po_required': 1342, 'payment_method': 620, 'ap_cycle': 94, 'tax_exempt': 778, 'portal': 1694, 'format': 602, 'context': 45938, 'esignature': 399, 'ap_system_portal': 1513, 'ap_phone': 854, 'buyer_bn': 32, 'ap_contact_name': 794, 'address': 474, 'mailbox_gone': 333, 'ap_system': 221, 'setup_url': 194, 'buyer_phone_from_page': 10085, 'buyer_address_from_page': 1608}
peppol: 77 Canadian participants; matched buyers 3, vendors 36
municipal / organisation directories: {'matched': 1776, 'legal_name': 767, 'address': 56, 'phone': 303, 'matched_by_place_name': 9, 'website': 17}
charity buyers: {'matched': 7372, 'bn': 6093, 'legal_name': 4023, 'address': 313, 'website': 26}
wikidata: {'vendors': 1004, 'buyers': 5414, 'buyer_legal_name': 2419, 'buyer_phone': 88, 'buyer_address': 647, 'buyer_website': 109, 'vendor_legal_name': 33, 'vendor_address': 289, 'vendor_website': 198, 'vendor_neq': 5}
crown-corporation BNs applied to inferred-vendor rows: 12559
vendor websites confirmed from search proposals: 502 applied: 3355
inferred vendors' published phone / address applied: {'phone': 8176}
registry bulk rows added (no API row for the key): 7508
Canada's Business Registries + registry open data: 2798 vendors, 14357 buyers found; filled {'buyer_bn': 5594, 'buyer_legal_name': 7951, 'vendor_registered_address': 3288, 'vendor_bn9': 3507, 'vendor_legal_name': 3245, 'vendor_registry_status': 3246, 'vendor_incorporation_date': 3437, 'vendor_legal_form': 3246, 'vendor_neq': 540, 'vendor_trading_name': 105, 'buyer_address': 251, 'vendor_skipped_legal_form': 1, 'vendor_bn9_other_registry': 4}
award facts from the buyers' own award pages: 237 pairs with a page; filled {'contract_value': 41, 'end_date': 17, 'start_date': 10, 'number_of_bids': 2, 'contract_or_agreement_number': 3, 'solicitation_or_tender_number': 7, 'term': 2, 'po_number_as_published': 1}
grants & contributions recipient BNs: 3202 buyers, 454 vendors in file; filled {'buyer_bn': 1636, 'buyer_bn_conflict_noted': 94, 'vendor_bn9': 779, 'buyer_legal_name': 327}
buyers' PO / contract open data joined: {'pairs': 13, 'po_filled': 12, 'contract_filled': 1} | records: 555539
back-references: {'dataset rows with lead relationships': 48574, 'lead rows with dataset history': 106}
sensitivity tags: {'corrections / detention': 25, 'health: mental health / addiction / sexual health': 202, 'intelligence / security / defence': 15, 'police service / police board': 66, 'courts / tribunals / legal aid': 48, 'child / youth protection': 20, 'police oversight body': 3, 'shelter / crisis / sexual-assault service': 59, 'coroner / medical examiner': 1}
site readers, second pass (websites found late): {'buyer_logo': 603, 'vendor_emails': 538, 'vendor_phone': 882, 'vendor_logo': 13363, 'buyer_phone': 48, 'vendor_address': 289, 'buyer_address': 6}
same-vendor carry-over (BN9 / address from the vendor's other rows): {'bn9': 31665, 'address': 114}
narrative columns: {'mailbox meta found': 68202, 'contract_description_from_title': 46453, 'contract_title_from_description': 162, 'invoice_reference_hint_po_rule': 752, 'records_with_this_vendor_lead': 55056, 'mailbox meta missing': 2365}
downstream pack: {'tax_derived_foreign': 3130, 'pay_on_sight_yes': 1942, 'ap_payable_today': 1352, 'ship_ready_yes': 679, 'buyer_trade_name_as_published': 32122, 'tax_derived': 54540, 'registry_note': 217, 'prompt_payment_default': 194, 'pay_on_sight_no': 33783, 'buyer_type_from_name': 9563, 'sensitivity_extra': 128, 'registry_warning': 1009, 'invoice_currency_derived': 64816, 'buyer_address_from_own_page': 2741, 'pay_on_sight_routed': 34842, 'currency_default': 2}
rows 73847
[('GOLD', 625), ('A0', 516), ('A1', 713), ('A2', 92), ('A3', 225), ('A4', 8), ('B0', 624), ('B1', 914), ('B2', 129), ('B3', 182), ('B4', 11), ('C0', 1001), ('C1', 288), ('C2', 20), ('C3', 33), ('C4', 28), ('D0', 204), ('D1', 9039), ('D2', 159), ('D3', 305), ('D4', 230), ('E0', 135), ('E1', 2715), ('E2', 54), ('E3', 82), ('E4', 60), ('F0', 1), ('F1', 5), ('F2', 1), ('F3', 1), ('F4', 1), ('GOLD-M', 15), ('GOLD-T', 136), ('I0', 438), ('I1', 13186), ('I2', 77), ('I3', 214), ('I4', 125), ('L0', 219), ('L1', 266), ('L2', 34), ('L3', 23), ('L4', 68), ('M0', 8), ('M1', 116), ('M2', 8), ('M3', 21), ('M4', 1), ('R0', 71), ('R1', 30717), ('R2', 78), ('R3', 614), ('R4', 137), ('T0', 63), ('T1', 8528), ('T2', 65), ('T3', 216), ('T4', 2)]
with any email: 70567 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            625
P01T_active_service_seen_on_buyer_site_invoicing_AP_email    136
P02_active_relationship_finance_accounting_email           403
P03_active_relationship_purchasing_email                   209
P04_active_relationship_general_email                     1568
P05_likely_active_awarded_12_36_months_any_email           378
P06_client_listing_invoicing_AP_email                      220
P06T_active_service_seen_on_buyer_site_other_email (3 part files)   8765
P07_client_listing_finance_or_purchasing_email             443
P08_client_listing_general_email (3 part files)           8765
P09_older_contract_or_payment_any_email                    349
P10_linked_from_vendor_site_any_email                     2746
P10R_ca_domain_registration_contract_own_email (11 part files)  30880
P11_any_relationship_email_not_yet_confirmed              1309
P12_weaker_relationship_within_5_years_own_email             8
P13_inferred_relationship_no_record_own_email (5 part files)  13602
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email     15
P06M_member_or_regulated_payer_of_canadian_body_other_email    143
Z_no_email_yet_not_delivered                              3283
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 8316626

# coverage vs the downstream targets (COVERAGE_VS_TARGETS.md)
benchmarks met 99 / 446 (22.2%); near 76; written out/ranked/COVERAGE_VS_TARGETS.md
  gap buyer_ap_cycle_published           P10R       0.0% ->  20%  rows needed 6171
  gap ap_system_hint                     P10R       0.4% ->  20%  rows needed 6049
  gap buyer_phone                        P08       40.2% ->  95%  rows needed 4807
  gap buyer_logo_url                     P08       46.5% -> 100%  rows needed 4691
  gap buyer_tax_exempt_status            P10R       0.1% ->  15%  rows needed 4609
  gap buyer_esignature_preference        P10R       0.1% ->  15%  rows needed 4609
  gap buyer_legal_name_as_published      P08       23.2% ->  75%  rows needed 4539
  gap vendor_registered_address          P08       18.7% ->  70%  rows needed 4494
  gap buyer_payment_method_preference    P10R       0.6% ->  15%  rows needed 4449
  gap vendor_logo_url                    P08       53.6% -> 100%  rows needed 4065
  gap vendor_phone                       P08       40.6% ->  85%  rows needed 3891
  gap vendor_emails                      P08       36.7% ->  75%  rows needed 3356
  gap vendor_bn9                         P08       15.1% ->  50%  rows needed 3062
  gap buyer_ap_cycle_published           P13        0.0% ->  20%  rows needed 2719
  gap buyer_address                      P08       65.1% ->  95%  rows needed 2618
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
