# Ranked buyers — 2026-11-08T21:39Z

```
# Changelog — build 2026-11-08T21:36Z (28fecb8)

Build id = the commit that produced this folder; every build is a full regeneration from the same rules, so the delta below is the only thing downstream needs to apply.

- rows: 66650 → 66675
- Gold (P01): 581 → 593
- field changed: ap_contact_name_as_published: 110
- field changed: ap_phone: 49
- field changed: buyer_address: 26
- field changed: buyer_bn_as_published: 78
- field changed: buyer_legal_name_as_published: 186
- field changed: buyer_phone: 20
mailboxes taken from the verification log (better than org_mailboxes' single pick): 640
team vendor contacts (referee-verified): 8716 vendors; 172 with a billing / AR mailbox
same-pair fill (facts from another record of the same buyer-vendor pair): {'solicitation_or_tender_number': 11, 'number_of_bids': 10, 'award_or_notice_id': 3, 'buyer_vendor_id': 2, 'commodity_codes': 8, 'end_date_inferred': 123, 'contract_value': 7, 'procurement_method': 3, 'contract_description': 3, 'po_number_as_published': 3, 'buyer_org_codes': 1, 'start_from_signed': 496, 'end_date': 1, 'contract_or_agreement_number': 2, 'contract_title': 1}
leads with a borrowed mailbox: 2246 | rows upgraded by a newer dated record: 38 | rows upgraded to an active service seen on the buyer's site: 11
P12 organisations: 108 added: 22 {'no own confirmed mailbox': 69, 'same organisation already in a row': 17} | P13 added: 51241 | P13 skipped: {'bad mailbox': 185, 'not located in Canada (no honest inference)': 2921, "mailbox not the organisation's own": 2127, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 7648}
extras from the lanes' result rows: {'invoicing_requirements': 1714, 'ap_phone': 2031, 'invoice_mailing_address': 1930, 'invoice_portal_url': 67, 'ap_contact_name': 138}
org_extras: 82908 organisations read; filled {'vendor_logo': 8447, 'vendor_phone_v2': 4612, 'po_required': 160, 'buyer_legal_name': 22205, 'buyer_phone_v2': 31871, 'buyer_payment_method_preference_mention_rejected': 17879, 'buyer_logo': 54184, 'payment_terms': 195, 'buyer_tax_exempt_status_mention_rejected': 268, 'buyer_legal_name_v2_rejected_no_overlap': 25231, 'buyer_legal_name_v2_legal_name_stated': 6821, 'buyer_bn': 2152, 'buyer_legal_name_v2_jsonld_legal_name': 2576, 'ap_system_hint_links': 289, 'buyer_legal_name_v2_jsonld_name': 2002, 'buyer_payment_method_preference_mention': 288, 'vendor_legal_name': 1482, 'vendor_neq': 32, 'buyer_esignature_preference_mention_rejected': 485, 'vendor_legal_name_v2': 913, 'buyer_address_v2': 6133, 'p13_name_from_legal_name': 9787, 'buyer_esignature_preference_mention': 17, 'vendor_bn': 183, 'invoice_portal_links': 22, 'buyer_tax_exempt_status_mention': 27, 'vendor_address_v2': 412, 'vendor_bn_jsonld': 6, 'buyer_bn_jsonld': 65, 'buyer_ap_cycle_published_mention': 11, 'vendor_qst': 4, 'buyer_ap_cycle_published_mention_rejected': 31, 'p13_name_from_domain': 2}
regional mailboxes of multinationals removed from other-country entities: 20
mx_check: 69559 domains known; 263 mailboxes on domains with no mail server removed; 226 webmail (freemail) addresses removed
dmarc/spf: 72911 domains known; rows {'enforced': 16205, 'exposed': 47918}
same organisation under another key folded into the row that holds its mailbox: 52
second mailbox of the same organisation (same site and mail domain, same name family) folded: 5
org_contacts: 73857 organisations read; filled {'vendor_phone': 19717, 'vendor_emails': 2323, 'buyer_phone': 35837, 'buyer_address': 26550, 'vendor_address': 2454}
ap_terms (evidence pages re-read): 60941 keys read, 71996 pages used across rows; filled {'payment_terms': 881, 'portal': 1310, 'format': 454, 'context': 46141, 'payment_method': 699, 'esignature': 202, 'ap_system_portal': 1169, 'ap_phone': 842, 'buyer_bn': 25, 'tax_exempt': 474, 'po_required': 889, 'ap_cycle': 63, 'ap_contact_name': 283, 'address': 454, 'mailbox_gone': 247, 'ap_system': 53, 'setup_url': 8, 'buyer_phone_from_page': 10287, 'buyer_address_from_page': 1864}
peppol: 77 Canadian participants; matched buyers 2, vendors 36
municipal / organisation directories: {'matched': 1817, 'legal_name': 805, 'address': 54, 'phone': 341, 'matched_by_place_name': 11, 'website': 18}
charity buyers: {'matched': 7454, 'bn': 6162, 'legal_name': 4006, 'address': 318, 'website': 25}
wikidata: {'buyers': 2300, 'buyer_legal_name': 877, 'vendors': 1047, 'buyer_phone': 54, 'buyer_address': 242, 'buyer_website': 106, 'vendor_legal_name': 40, 'vendor_address': 291, 'vendor_website': 203, 'vendor_neq': 6}
crown-corporation BNs applied to inferred-vendor rows: 47003
vendor websites confirmed from search proposals: 275 applied: 2708
inferred vendors' published phone / address applied: {'phone': 37249}
registry bulk rows added (no API row for the key): 8819
Canada's Business Registries + registry open data: 2787 vendors, 11466 buyers found; filled {'buyer_bn': 3190, 'buyer_legal_name': 6498, 'vendor_registered_address': 3141, 'vendor_bn9': 3331, 'vendor_legal_name': 3096, 'vendor_registry_status': 3097, 'vendor_incorporation_date': 3299, 'vendor_legal_form': 3097, 'vendor_neq': 420, 'vendor_trading_name': 124, 'buyer_address': 360, 'vendor_skipped_legal_form': 1}
award facts from the buyers' own award pages: 237 pairs with a page; filled {'contract_value': 41, 'end_date': 17, 'start_date': 10, 'number_of_bids': 2, 'contract_or_agreement_number': 3, 'solicitation_or_tender_number': 7, 'term': 2, 'po_number_as_published': 1}
grants & contributions recipient BNs: 3202 buyers, 454 vendors in file; filled {'buyer_bn': 1877, 'buyer_bn_conflict_noted': 80, 'vendor_bn9': 819, 'buyer_legal_name': 488}
buyers' PO / contract open data joined: {'pairs': 9, 'po_filled': 8, 'contract_filled': 1} | records: 555539
back-references: {'dataset rows with lead relationships': 9799, 'lead rows with dataset history': 117}
sensitivity tags: {'corrections / detention': 26, 'health: mental health / addiction / sexual health': 191, 'intelligence / security / defence': 15, 'police service / police board': 62, 'courts / tribunals / legal aid': 44, 'child / youth protection': 18, 'police oversight body': 3, 'shelter / crisis / sexual-assault service': 54, 'coroner / medical examiner': 1}
narrative columns: {'mailbox meta found': 61483, 'contract_description_from_title': 9338, 'contract_title_from_description': 163, 'invoice_reference_hint_po_rule': 508, 'records_with_this_vendor_lead': 10704, 'mailbox meta missing': 2144}
downstream pack: {'ap_payable_today': 785, 'ship_ready_yes': 593, 'tax_derived': 48625, 'registry_warning': 1227, 'prompt_payment_default': 131, 'buyer_type_from_name': 7552, 'sensitivity_extra': 122, 'invoice_currency_derived': 57043, 'currency_default': 2}
rows 66695
[('GOLD', 593), ('A0', 516), ('A1', 717), ('A2', 95), ('A3', 217), ('A4', 12), ('B0', 623), ('B1', 938), ('B2', 144), ('B3', 183), ('B4', 9), ('C0', 1011), ('C1', 316), ('C2', 17), ('C3', 34), ('C4', 25), ('D0', 117), ('D1', 3178), ('D2', 120), ('D3', 149), ('D4', 174), ('E0', 96), ('E1', 2586), ('E2', 45), ('E3', 74), ('E4', 60), ('F0', 1), ('F1', 11), ('F2', 2), ('F3', 3), ('F4', 5), ('GOLD-M', 19), ('GOLD-T', 92), ('I0', 448), ('I1', 49378), ('I2', 174), ('I3', 930), ('I4', 311), ('L0', 225), ('L1', 272), ('L2', 31), ('L3', 23), ('L4', 67), ('M0', 10), ('M1', 135), ('M2', 9), ('M3', 26), ('M4', 1), ('T0', 21), ('T1', 2328), ('T2', 49), ('T3', 73), ('T4', 2)]
with any email: 63627 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            593
P01T_active_service_seen_on_buyer_site_invoicing_AP_email     92
P02_active_relationship_finance_accounting_email           395
P03_active_relationship_purchasing_email                   228
P04_active_relationship_general_email                     1583
P05_likely_active_awarded_12_36_months_any_email           379
P06_client_listing_invoicing_AP_email                      165
P06T_active_service_seen_on_buyer_site_other_email        2440
P07_client_listing_finance_or_purchasing_email             252
P08_client_listing_general_email                          3038
P09_older_contract_or_payment_any_email                    373
P10_linked_from_vendor_site_any_email                     2597
P11_any_relationship_email_not_yet_confirmed               488
P12_weaker_relationship_within_5_years_own_email            21
P13_inferred_relationship_no_record_own_email (16 part files)  50793
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email     19
P06M_member_or_regulated_payer_of_canadian_body_other_email    168
Z_no_email_yet_not_delivered                              3071
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 7626363

# coverage vs the downstream targets (COVERAGE_VS_TARGETS.md)
benchmarks met 93 / 438 (21.2%); near 63; written out/ranked/COVERAGE_VS_TARGETS.md
  gap buyer_address                      P13       75.0% ->  95%  rows needed 10156
  gap buyer_ap_cycle_published           P13        0.0% ->  20%  rows needed 10151
  gap ap_system_hint                     P13        0.5% ->  20%  rows needed 9919
  gap buyer_phone                        P13       79.0% ->  95%  rows needed 8123
  gap buyer_esignature_preference        P13        0.1% ->  15%  rows needed 7580
  gap buyer_tax_exempt_status            P13        0.1% ->  15%  rows needed 7548
  gap buyer_payment_method_preference    P13        0.9% ->  15%  rows needed 7155
  gap buyer_legal_name_as_published      P13       48.8% ->  60%  rows needed 5695
  gap buyer_logo_url                     P13       83.9% ->  95%  rows needed 5651
  gap buyer_bn_as_published              P13       21.6% ->  30%  rows needed 4255
  gap buyer_legal_name_as_published      P08       36.9% ->  75%  rows needed 1158
  gap buyer_legal_name_as_published      P10       32.3% ->  70%  rows needed 979
  gap buyer_address                      P08       65.6% ->  95%  rows needed 893
  gap vendor_emails                      P08       47.0% ->  75%  rows needed 852
  gap buyer_address                      P10       64.4% ->  95%  rows needed 796
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
