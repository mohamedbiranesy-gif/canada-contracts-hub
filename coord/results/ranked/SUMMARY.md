# Ranked buyers — 2026-11-08T22:23Z

```
# Changelog — build 2026-11-08T22:20Z (757e25e)

Build id = the commit that produced this folder; every build is a full regeneration from the same rules, so the delta below is the only thing downstream needs to apply.

- rows: 66675 → 66673
- Gold (P01): 593 → 596
- field changed: ap_contact_name_as_published: 12
- field changed: ap_phone: 10
- field changed: buyer_address: 85
- field changed: buyer_bn_as_published: 22
- field changed: buyer_legal_name_as_published: 371
- field changed: buyer_phone: 40
mailboxes taken from the verification log (better than org_mailboxes' single pick): 640
team vendor contacts (referee-verified): 8716 vendors; 172 with a billing / AR mailbox
same-pair fill (facts from another record of the same buyer-vendor pair): {'solicitation_or_tender_number': 11, 'number_of_bids': 10, 'award_or_notice_id': 2, 'buyer_vendor_id': 2, 'commodity_codes': 8, 'end_date_inferred': 123, 'contract_value': 7, 'procurement_method': 3, 'contract_description': 3, 'po_number_as_published': 3, 'buyer_org_codes': 1, 'start_from_signed': 496, 'end_date': 1, 'contract_or_agreement_number': 2, 'contract_title': 1}
leads with a borrowed mailbox: 2257 | rows upgraded by a newer dated record: 38 | rows upgraded to an active service seen on the buyer's site: 11
P12 organisations: 108 added: 22 {'no own confirmed mailbox': 69, 'same organisation already in a row': 17} | P13 added: 51241 | P13 skipped: {'bad mailbox': 185, 'not located in Canada (no honest inference)': 2921, "mailbox not the organisation's own": 2127, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 7648}
extras from the lanes' result rows: {'invoicing_requirements': 1707, 'ap_phone': 2021, 'invoice_mailing_address': 1920, 'invoice_portal_url': 67, 'ap_contact_name': 138}
org_extras: 83059 organisations read; filled {'vendor_logo': 8457, 'vendor_phone_v2': 4636, 'po_required': 161, 'buyer_legal_name': 22245, 'buyer_phone_v2': 31941, 'buyer_payment_method_preference_mention_rejected': 17879, 'buyer_logo': 54226, 'payment_terms': 193, 'buyer_tax_exempt_status_mention_rejected': 268, 'buyer_legal_name_v2_rejected_no_overlap': 25255, 'buyer_legal_name_v2_legal_name_stated': 6843, 'buyer_bn': 2155, 'buyer_legal_name_v2_jsonld_legal_name': 2579, 'ap_system_hint_links': 293, 'buyer_legal_name_v2_jsonld_name': 2006, 'buyer_payment_method_preference_mention': 289, 'vendor_legal_name': 1482, 'vendor_neq': 32, 'buyer_esignature_preference_mention_rejected': 485, 'vendor_legal_name_v2': 913, 'buyer_address_v2': 6140, 'p13_name_from_legal_name': 9798, 'buyer_esignature_preference_mention': 17, 'vendor_bn': 184, 'invoice_portal_links': 22, 'buyer_tax_exempt_status_mention': 27, 'vendor_address_v2': 412, 'vendor_bn_jsonld': 6, 'buyer_bn_jsonld': 65, 'buyer_ap_cycle_published_mention': 11, 'vendor_qst': 4, 'buyer_ap_cycle_published_mention_rejected': 31, 'p13_name_from_domain': 2}
regional mailboxes of multinationals removed from other-country entities: 20
mx_check: 69559 domains known; 263 mailboxes on domains with no mail server removed; 226 webmail (freemail) addresses removed
dmarc/spf: 72920 domains known; rows {'enforced': 16199, 'exposed': 47915}
same organisation under another key folded into the row that holds its mailbox: 52
second mailbox of the same organisation (same site and mail domain, same name family) folded: 6
org_contacts: 73857 organisations read; filled {'vendor_phone': 19716, 'vendor_emails': 2323, 'buyer_phone': 35836, 'buyer_address': 26545, 'vendor_address': 2454}
ap_terms (evidence pages re-read): 61142 keys read, 72483 pages used across rows; filled {'payment_terms': 944, 'po_required': 918, 'payment_method': 721, 'ap_cycle': 68, 'tax_exempt': 499, 'portal': 1328, 'format': 464, 'context': 46137, 'esignature': 222, 'ap_system_portal': 1186, 'ap_phone': 842, 'buyer_bn': 28, 'ap_contact_name': 295, 'address': 454, 'mailbox_gone': 247, 'ap_system': 72, 'setup_url': 13, 'buyer_phone_from_page': 10276, 'buyer_address_from_page': 1864}
peppol: 77 Canadian participants; matched buyers 2, vendors 36
municipal / organisation directories: {'matched': 1817, 'legal_name': 800, 'address': 54, 'phone': 340, 'matched_by_place_name': 11, 'website': 18}
charity buyers: {'matched': 7454, 'bn': 6160, 'legal_name': 3999, 'address': 318, 'website': 25}
wikidata: {'vendors': 1047, 'buyers': 3020, 'buyer_legal_name': 1203, 'buyer_phone': 64, 'buyer_address': 315, 'buyer_website': 109, 'vendor_legal_name': 40, 'vendor_address': 291, 'vendor_website': 203, 'vendor_neq': 6}
crown-corporation BNs applied to inferred-vendor rows: 47003
vendor websites confirmed from search proposals: 467 applied: 3027
inferred vendors' published phone / address applied: {'phone': 37249}
registry bulk rows added (no API row for the key): 8816
Canada's Business Registries + registry open data: 2787 vendors, 11478 buyers found; filled {'buyer_bn': 3202, 'buyer_legal_name': 6408, 'vendor_registered_address': 3141, 'vendor_bn9': 3331, 'vendor_legal_name': 3096, 'vendor_registry_status': 3097, 'vendor_incorporation_date': 3299, 'vendor_legal_form': 3097, 'vendor_neq': 420, 'vendor_trading_name': 124, 'buyer_address': 348, 'vendor_skipped_legal_form': 1}
award facts from the buyers' own award pages: 237 pairs with a page; filled {'contract_value': 41, 'end_date': 17, 'start_date': 10, 'number_of_bids': 2, 'contract_or_agreement_number': 3, 'solicitation_or_tender_number': 7, 'term': 2, 'po_number_as_published': 1}
grants & contributions recipient BNs: 3202 buyers, 454 vendors in file; filled {'buyer_bn': 1876, 'buyer_bn_conflict_noted': 81, 'vendor_bn9': 819, 'buyer_legal_name': 474}
buyers' PO / contract open data joined: {'pairs': 9, 'po_filled': 8, 'contract_filled': 1} | records: 555539
back-references: {'dataset rows with lead relationships': 9798, 'lead rows with dataset history': 117}
sensitivity tags: {'corrections / detention': 26, 'health: mental health / addiction / sexual health': 191, 'intelligence / security / defence': 15, 'police service / police board': 62, 'courts / tribunals / legal aid': 44, 'child / youth protection': 18, 'police oversight body': 3, 'shelter / crisis / sexual-assault service': 54, 'coroner / medical examiner': 1}
narrative columns: {'mailbox meta found': 61473, 'contract_description_from_title': 9337, 'contract_title_from_description': 163, 'invoice_reference_hint_po_rule': 519, 'records_with_this_vendor_lead': 10703, 'mailbox meta missing': 2144}
downstream pack: {'ap_payable_today': 789, 'ship_ready_yes': 596, 'tax_derived': 48625, 'registry_warning': 1227, 'prompt_payment_default': 131, 'buyer_type_from_name': 7519, 'sensitivity_extra': 122, 'invoice_currency_derived': 57043, 'currency_default': 2}
rows 66693
[('GOLD', 596), ('A0', 524), ('A1', 713), ('A2', 89), ('A3', 220), ('A4', 11), ('B0', 624), ('B1', 932), ('B2', 144), ('B3', 184), ('B4', 9), ('C0', 1010), ('C1', 316), ('C2', 18), ('C3', 34), ('C4', 25), ('D0', 116), ('D1', 3178), ('D2', 120), ('D3', 149), ('D4', 174), ('E0', 97), ('E1', 2586), ('E2', 45), ('E3', 74), ('E4', 59), ('F0', 1), ('F1', 11), ('F2', 2), ('F3', 3), ('F4', 5), ('GOLD-M', 19), ('GOLD-T', 92), ('I0', 448), ('I1', 49378), ('I2', 174), ('I3', 930), ('I4', 311), ('L0', 225), ('L1', 272), ('L2', 31), ('L3', 23), ('L4', 67), ('M0', 10), ('M1', 135), ('M2', 9), ('M3', 26), ('M4', 1), ('T0', 21), ('T1', 2328), ('T2', 49), ('T3', 73), ('T4', 2)]
with any email: 63617 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            596
P01T_active_service_seen_on_buyer_site_invoicing_AP_email     92
P02_active_relationship_finance_accounting_email           399
P03_active_relationship_purchasing_email                   223
P04_active_relationship_general_email                     1580
P05_likely_active_awarded_12_36_months_any_email           379
P06_client_listing_invoicing_AP_email                      165
P06T_active_service_seen_on_buyer_site_other_email        2440
P07_client_listing_finance_or_purchasing_email             252
P08_client_listing_general_email                          3038
P09_older_contract_or_payment_any_email                    374
P10_linked_from_vendor_site_any_email                     2597
P11_any_relationship_email_not_yet_confirmed               478
P12_weaker_relationship_within_5_years_own_email            21
P13_inferred_relationship_no_record_own_email (16 part files)  50793
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email     19
P06M_member_or_regulated_payer_of_canadian_body_other_email    168
Z_no_email_yet_not_delivered                              3079
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 7622446

# coverage vs the downstream targets (COVERAGE_VS_TARGETS.md)
benchmarks met 94 / 438 (21.5%); near 65; written out/ranked/COVERAGE_VS_TARGETS.md
  gap buyer_ap_cycle_published           P13        0.0% ->  20%  rows needed 10151
  gap buyer_address                      P13       75.1% ->  95%  rows needed 10095
  gap ap_system_hint                     P13        0.5% ->  20%  rows needed 9919
  gap buyer_phone                        P13       79.1% ->  95%  rows needed 8100
  gap buyer_esignature_preference        P13        0.1% ->  15%  rows needed 7580
  gap buyer_tax_exempt_status            P13        0.1% ->  15%  rows needed 7548
  gap buyer_payment_method_preference    P13        0.9% ->  15%  rows needed 7154
  gap buyer_logo_url                     P13       83.9% ->  95%  rows needed 5625
  gap buyer_legal_name_as_published      P13       49.2% ->  60%  rows needed 5465
  gap buyer_bn_as_published              P13       21.6% ->  30%  rows needed 4244
  gap buyer_legal_name_as_published      P08       36.9% ->  75%  rows needed 1157
  gap buyer_legal_name_as_published      P10       32.4% ->  70%  rows needed 977
  gap buyer_address                      P08       65.6% ->  95%  rows needed 893
  gap vendor_emails                      P08       47.0% ->  75%  rows needed 852
  gap buyer_address                      P10       64.4% ->  95%  rows needed 796
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
