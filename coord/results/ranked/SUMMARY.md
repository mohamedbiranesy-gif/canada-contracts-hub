# Ranked buyers — 2026-11-09T02:25Z

```
# Changelog — build 2026-11-09T02:22Z (6e33c67)

Build id = the commit that produced this folder; every build is a full regeneration from the same rules, so the delta below is the only thing downstream needs to apply.

- rows: 66671 → 66671
- Gold (P01): 597 → 597
- field changed: ap_contact_name_as_published: 19
- field changed: buyer_address: 85
- field changed: buyer_legal_name_as_published: 177
- field changed: buyer_phone: 10
- field changed: invoice_mailing_address: 2
- field changed: invoice_portal_url: 35
mailboxes taken from the verification log (better than org_mailboxes' single pick): 640
team vendor contacts (referee-verified): 8716 vendors; 172 with a billing / AR mailbox
same-pair fill (facts from another record of the same buyer-vendor pair): {'solicitation_or_tender_number': 11, 'number_of_bids': 10, 'award_or_notice_id': 2, 'buyer_vendor_id': 2, 'commodity_codes': 8, 'end_date_inferred': 123, 'contract_value': 7, 'procurement_method': 3, 'contract_description': 3, 'po_number_as_published': 3, 'buyer_org_codes': 1, 'start_from_signed': 496, 'end_date': 1, 'contract_or_agreement_number': 2, 'contract_title': 1}
leads with a borrowed mailbox: 2256 | rows upgraded by a newer dated record: 39 | rows upgraded to an active service seen on the buyer's site: 11
P12 organisations: 108 added: 22 {'no own confirmed mailbox': 69, 'same organisation already in a row': 17} | P13 added: 51244 | P13 skipped: {'bad mailbox': 185, 'not located in Canada (no honest inference)': 2923, "mailbox not the organisation's own": 2131, 'is the inferred vendor itself': 4, 'same organisation already in a row (domain / mailbox / name)': 7643}
extras from the lanes' result rows: {'invoicing_requirements': 1739, 'ap_phone': 2033, 'invoice_mailing_address': 1929, 'invoice_portal_url': 70, 'ap_contact_name': 135}
org_extras: 83347 organisations read; filled {'vendor_logo': 8557, 'vendor_phone_v2': 4704, 'vendor_trading_name_jsonld': 1124, 'po_required': 166, 'buyer_legal_name': 22384, 'buyer_phone_v2': 32117, 'buyer_payment_method_preference_mention_rejected': 17880, 'buyer_logo': 54481, 'payment_terms': 199, 'buyer_tax_exempt_status_mention_rejected': 268, 'buyer_legal_name_v2_rejected_no_overlap': 25307, 'buyer_legal_name_v2_legal_name_stated': 6902, 'buyer_bn': 2160, 'buyer_legal_name_v2_jsonld_legal_name': 2583, 'ap_system_hint_links': 304, 'buyer_legal_name_v2_jsonld_name': 2010, 'buyer_payment_method_preference_mention': 290, 'vendor_legal_name': 1487, 'vendor_neq': 32, 'buyer_esignature_preference_mention_rejected': 486, 'vendor_legal_name_v2': 927, 'buyer_address_v2': 6153, 'p13_name_from_legal_name': 9820, 'buyer_esignature_preference_mention': 17, 'vendor_bn': 184, 'invoice_portal_links': 23, 'buyer_tax_exempt_status_mention': 27, 'vendor_address_v2': 416, 'vendor_bn_jsonld': 6, 'buyer_bn_jsonld': 65, 'buyer_ap_cycle_published_mention': 11, 'vendor_qst': 4, 'buyer_ap_cycle_published_mention_rejected': 31, 'p13_name_from_domain': 2}
regional mailboxes of multinationals removed from other-country entities: 20
mx_check: 69559 domains known; 263 mailboxes on domains with no mail server removed; 226 webmail (freemail) addresses removed
dmarc/spf: 72956 domains known; rows {'enforced': 16194, 'exposed': 47914}
same organisation under another key folded into the row that holds its mailbox: 52
second mailbox of the same organisation (same site and mail domain, same name family) folded: 6
org_contacts: 74819 organisations read; filled {'vendor_phone': 19841, 'vendor_emails': 2359, 'buyer_phone': 36368, 'buyer_address': 26924, 'vendor_address': 2496}
ap_terms (evidence pages re-read): 64735 keys read, 85459 pages used across rows; filled {'payment_terms': 1764, 'po_required': 1339, 'payment_method': 622, 'ap_cycle': 94, 'tax_exempt': 772, 'portal': 1683, 'format': 602, 'context': 46082, 'esignature': 399, 'ap_system_portal': 1505, 'ap_phone': 865, 'buyer_bn': 32, 'ap_contact_name': 794, 'address': 473, 'mailbox_gone': 299, 'ap_system': 216, 'setup_url': 188, 'buyer_phone_from_page': 10110, 'buyer_address_from_page': 1772}
peppol: 77 Canadian participants; matched buyers 2, vendors 36
municipal / organisation directories: {'matched': 1817, 'legal_name': 733, 'address': 52, 'phone': 300, 'matched_by_place_name': 11, 'website': 18}
charity buyers: {'matched': 7454, 'bn': 6157, 'legal_name': 3991, 'address': 307, 'website': 25}
wikidata: {'vendors': 1047, 'buyers': 4121, 'buyer_legal_name': 1739, 'buyer_phone': 84, 'buyer_address': 505, 'buyer_website': 109, 'vendor_legal_name': 36, 'vendor_address': 290, 'vendor_website': 203, 'vendor_neq': 6}
crown-corporation BNs applied to inferred-vendor rows: 47006
vendor websites confirmed from search proposals: 502 applied: 3084
inferred vendors' published phone / address applied: {'phone': 37249}
registry bulk rows added (no API row for the key): 7355
Canada's Business Registries + registry open data: 2787 vendors, 13355 buyers found; filled {'buyer_bn': 4976, 'buyer_legal_name': 7379, 'vendor_registered_address': 3137, 'vendor_bn9': 3327, 'vendor_legal_name': 3092, 'vendor_registry_status': 3093, 'vendor_incorporation_date': 3295, 'vendor_legal_form': 3093, 'vendor_neq': 420, 'vendor_trading_name': 116, 'buyer_address': 213, 'vendor_skipped_legal_form': 1}
award facts from the buyers' own award pages: 237 pairs with a page; filled {'contract_value': 41, 'end_date': 17, 'start_date': 10, 'number_of_bids': 2, 'contract_or_agreement_number': 3, 'solicitation_or_tender_number': 7, 'term': 2, 'po_number_as_published': 1}
grants & contributions recipient BNs: 3202 buyers, 454 vendors in file; filled {'buyer_bn': 1676, 'buyer_bn_conflict_noted': 93, 'vendor_bn9': 818, 'buyer_legal_name': 365}
buyers' PO / contract open data joined: {'pairs': 9, 'po_filled': 8, 'contract_filled': 1} | records: 555539
back-references: {'dataset rows with lead relationships': 9796, 'lead rows with dataset history': 118}
sensitivity tags: {'corrections / detention': 26, 'health: mental health / addiction / sexual health': 190, 'intelligence / security / defence': 15, 'police service / police board': 62, 'courts / tribunals / legal aid': 44, 'child / youth protection': 18, 'police oversight body': 3, 'shelter / crisis / sexual-assault service': 54, 'coroner / medical examiner': 1}
site readers, second pass (websites found late): {'buyer_logo': 604, 'vendor_emails': 444, 'vendor_phone': 761, 'vendor_logo': 45298, 'buyer_phone': 47, 'vendor_address': 206, 'buyer_address': 5}
same-vendor carry-over (BN9 / address from the vendor's other rows): {'bn9': 47, 'address': 58}
narrative columns: {'mailbox meta found': 61468, 'contract_description_from_title': 9334, 'contract_title_from_description': 163, 'invoice_reference_hint_po_rule': 775, 'records_with_this_vendor_lead': 10698, 'mailbox meta missing': 2144}
downstream pack: {'tax_derived_foreign': 887, 'pay_on_sight_yes': 1887, 'ap_payable_today': 905, 'ship_ready_yes': 612, 'tax_derived': 49884, 'registry_note': 220, 'prompt_payment_default': 131, 'pay_on_sight_no': 40182, 'buyer_type_from_name': 7880, 'sensitivity_extra': 122, 'registry_warning': 1004, 'invoice_currency_derived': 58376, 'pay_on_sight_routed': 21543, 'currency_default': 2}
rows 66691
[('GOLD', 597), ('A0', 528), ('A1', 710), ('A2', 89), ('A3', 220), ('A4', 10), ('B0', 623), ('B1', 928), ('B2', 144), ('B3', 184), ('B4', 9), ('C0', 1011), ('C1', 316), ('C2', 18), ('C3', 34), ('C4', 25), ('D0', 116), ('D1', 3178), ('D2', 120), ('D3', 149), ('D4', 174), ('E0', 97), ('E1', 2586), ('E2', 45), ('E3', 74), ('E4', 59), ('F0', 1), ('F1', 11), ('F2', 2), ('F3', 3), ('F4', 5), ('GOLD-M', 18), ('GOLD-T', 92), ('I0', 448), ('I1', 49381), ('I2', 174), ('I3', 930), ('I4', 311), ('L0', 224), ('L1', 272), ('L2', 31), ('L3', 23), ('L4', 67), ('M0', 10), ('M1', 135), ('M2', 9), ('M3', 26), ('M4', 1), ('T0', 21), ('T1', 2328), ('T2', 49), ('T3', 73), ('T4', 2)]
with any email: 63612 | contract buyers: 0
P01_GOLD_active_relationship_invoicing_AP_email            597
P01T_active_service_seen_on_buyer_site_invoicing_AP_email     92
P02_active_relationship_finance_accounting_email           399
P03_active_relationship_purchasing_email                   223
P04_active_relationship_general_email                     1575
P05_likely_active_awarded_12_36_months_any_email           379
P06_client_listing_invoicing_AP_email                      165
P06T_active_service_seen_on_buyer_site_other_email        2440
P07_client_listing_finance_or_purchasing_email             252
P08_client_listing_general_email                          3038
P09_older_contract_or_payment_any_email                    374
P10_linked_from_vendor_site_any_email                     2597
P11_any_relationship_email_not_yet_confirmed               475
P12_weaker_relationship_within_5_years_own_email            21
P13_inferred_relationship_no_record_own_email (18 part files)  50796
P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email     18
P06M_member_or_regulated_payer_of_canadian_body_other_email    168
Z_no_email_yet_not_delivered                              3082
unassigned 0 []
blank cells filled with not_published (delivered P01-P13): 7565519

# coverage vs the downstream targets (COVERAGE_VS_TARGETS.md)
benchmarks met 105 / 438 (24.0%); near 79; written out/ranked/COVERAGE_VS_TARGETS.md
  gap buyer_ap_cycle_published           P13        0.0% ->  20%  rows needed 10152
  gap ap_system_hint                     P13        0.6% ->  20%  rows needed 9870
  gap buyer_address                      P13       75.7% ->  95%  rows needed 9811
  gap buyer_phone                        P13       79.3% ->  95%  rows needed 7998
  gap buyer_tax_exempt_status            P13        0.1% ->  15%  rows needed 7584
  gap buyer_esignature_preference        P13        0.1% ->  15%  rows needed 7581
  gap buyer_payment_method_preference    P13        0.5% ->  15%  rows needed 7342
  gap buyer_logo_url                     P13       84.2% ->  95%  rows needed 5495
  gap buyer_legal_name_as_published      P13       51.5% ->  60%  rows needed 4338
  gap buyer_bn_as_published              P13       24.7% ->  30%  rows needed 2708
  gap buyer_legal_name_as_published      P08       37.1% ->  75%  rows needed 1153
  gap buyer_legal_name_as_published      P10       32.6% ->  70%  rows needed 972
  gap buyer_address                      P08       66.1% ->  95%  rows needed 879
  gap vendor_emails                      P08       48.7% ->  75%  rows needed 800
  gap buyer_address                      P10       65.1% ->  95%  rows needed 778
```

Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md
