# S1-30 — Windsor Essex Community Housing Corporation ⇄ MCAM CONSTRUCTION INC

Stratum: **S1_gold_complete_published_PO_rule** · pay on sight: yes · channel tier 1 · AP grade B · missing: —

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: WINDSOR ESSEX COMMUNITY HOUSING CORPORATION (as registered: Canada's Business Registries, ON 1718200, 2026-11-08) — 945 McDougall Street , Windsor, Ontario, Canada , N9A 1L9 — buyer tax no. 888174612 (Canada's Business Registries, ON 1718200, 2026-11-08)
SUBMIT TO: ap@wechc.com (invoicing/AP mailbox, confirmed by the referee) | tender portal (not an invoice channel): https://wechc.bidsandtenders.ca/ — bids&tenders
REFERENCE: contract RFPc 26-RR-07-01 (bid_number) — the source publishes the award under this tender / notice number and no separate contract number; tender RFPc 26-RR-07-01 (bid_number) | PO rule: purchase-order terms published (as published: shall promptly notify CHC in writing and shall not proceed until CHC issue
FROM / REMIT TO: MCAM Construction Inc. — 8-2605 Meadowbrook Lane, Windsor, ON, N8T2X9 | GST/HST 789127552RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: CAD | TERMS: statutory default for construction work
DESCRIPTION: Kitchen Renovation-Family & Warren Park | AMOUNT: 328,800.00 CAD
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 92
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 13
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Windsor Essex Community Housing Corporation (company (private sector), CA) — public contract / purchase award in the last 12 months (dated record): MCAM CONSTRUCTION INC | subject: Kitchen Renovation-Family & Warren Park | instrument: contract | contract number: RFPc 26-RR-07-01 (bid_number) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract refer | solicitation: RFPc 26-RR-07-01 (bid_number) | all identifiers: {"bid_number": "RFPc 26-RR-07-01", "bidsandtenders_tender_id": "e3efe57a-bfc0-4e73-b18a-ca8ff6e2fda2", "portal": "wechc.bidsandtenders.ca", "submission_name": "Submission 1"} | value: 328800.0 CAD | awarded 2026-06-04 | published by: bids&tenders (eSolutions) public procurement portals - awarded bids | record: https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/e3efe57a-bfc0-4e73-b18a-ca8ff6e2fda2 | vendor in Canada because: bids&tenders 'Awarded' vendor table field 'Country' = 'Canada' (with ProvinceState/City/PostalCode as published) | status rule: likely active (awarded in the last 12 months, no end date published) | this buyer has 111 records with Canada-located vendors (62 distinct vendors; 46 in the last 12 months; latest 2026-10-05)
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: b:c6ee81e5edbdf58e
- **tier**: B
- **grade**: 4
- **records_with_this_vendor**: 4

## Buyer
- **buyer**: Windsor Essex Community Housing Corporation
- **buyer_website**: https://wechc.com
- **buyer_address**: 945 McDougall Street , Windsor, Ontario, Canada , N9A 1L9
- **buyer_phone**: (519) 254-1681
- **buyer_contact_evidence_url**: https://www.wechc.com/contact-us
- **buyer_legal_name_as_published**: WINDSOR ESSEX COMMUNITY HOUSING CORPORATION (as registered: Canada's Business Registries, ON 1718200, 2026-11-08)
- **buyer_bn_as_published**: 888174612 (Canada's Business Registries, ON 1718200, 2026-11-08)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 888174612RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_logo_url**: https://www.wechc.com/themes/custom/wechc/logo.svg
- **buyer_registry_id**: 1718200 (ON; https://ised-isde.canada.ca/cbr-rec/en/search?q=Windsor%20Essex%20Community%20Housing%20Corporation)
- **buyer_type**: company (private sector)
- **buyer_sector**: private sector
- **buyer_legal_form**: ONTARIO BUSINESS CORP. (Canada's Business Registries, ON 1718200, 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.wechc.com/contact-us (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; invoicing requirements: the lane's AP page (https://www.wechc.com/procurement-information); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: ap@wechc.com
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.wechc.com/procurement-information
- **email_evidence_quote**: If you are not registered for VendorCafé, all invoices should be sent to ap@wechc.com
- **email_evidence_context**: to VendorCafé, all changes can be made through the portal. If you are not registered for VendorCafé, please email vendorsupport@wechc.com with the requested changes. Invoicing If you are not registered for VendorCafé, all invoices should be sent to ap@wechc.com If you have been invited and registered to Vendor Café, all invoices should be submitted through the portal. VendorCafé VendorCafé is CHC’s online vendor management system. Use VendorCafé to: Manage your account information from within VendorCafé in (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: ap@wechc.com (invoicing/AP) | researched by the ChatGPT/Codex agent (lane chatgpt) (page opened and quoted) on 2026-10-27 | page: https://www.wechc.com/procurement-information | quote: "If you are not registered for VendorCafé, all invoices should be sent to ap@wechc.com" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by self-hosted or other (mx-cluster-ca-fallback.hornetsecurity.com) | lane file: chatgpt/chatgpt_buyer_ap_results_batch04.csv task CH-AP-00327
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by self-hosted or other (mx-cluster-ca-fallback.hornetsecurity.com)
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none;
- **dmarc_record_domain**: wechc.com
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 a a:server.wechc.com ip4:50.115.179.242 ip4:162.214.7.143 ip4:69.46.98.132 ip4:162.214.6.142 include:spf.hornetsecurity.com include:spf.protection.outlook.com include:asp-spf1.yardi.com include:asp-spf2.yardi.com -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements**: Vendors without VendorCafe registration email all invoices to AP. Invited/registered vendors submit all invoices through VendorCafe. Portal permits invoices against completed work orders and purchase orders and tracks approvals/payments.
- **payment_terms_default_policy**: statutory default for construction work (buyer published no terms): the owner must pay a proper invoice no later than 28 days after receiving it — Construction Act, R.S.O. 1990, c. C.30, s. 6.4(1), in force 2019-10-01; s. 3(1) binds the Crown (https://www.ontario.ca/laws/statute/90c30, read 2026-11-08: "an owner shall pay the amount payable under a proper invoice no later than 28 days after receiving the proper invoice from the contractor"); applies only if this contract is an improvement under the Act
- **po_required_as_published**: purchase-order terms published (as published: shall promptly notify CHC in writing and shall not proceed until CHC issues a revised, written Purchase Order) (as printed on https://www.wechc.com/sites/default/files/2025-01/chc_purchase_order_and_work_order_terms_and_conditions.pdf, re-read 2026-11-08)
- **invoice_portal_url**: https://wechc.bidsandtenders.ca/ — bids&tenders
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **ap_system_hint**: named on the buyer's page: bids&tenders (as printed on https://www.wechc.com/procurement-information, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "po_required": "purchase-order terms published (as published: shall promptly notify CHC in writing and shall not proceed until CHC issues a revised, written Purchase Order) (as printed on https://www.wechc.com/sites/default/files/2025-01/chc_purchase_order_and_work_order_terms_and_conditions.pdf, re-read 2026-11-08)", "portal_url": "https://wechc.bidsandtenders.ca/ — bids&tenders", "portal_kind": "actionable supplier / invoice portal named by the buyer", "requirements_text": "Vendors without VendorCafe registration email all invoices to AP. Invited/registered vendors submit all invoices through VendorCafe. Portal permits invoices against completed work orders and purchase orders and tracks approvals/payments."}
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: WINDSOR ESSEX COMMUNITY HOUSING CORPORATION (as registered: Canada's Business Registries, ON 1718200, 2026-11-08) — 945 McDougall Street , Windsor, Ontario, Canada , N9A 1L9 — buyer tax no. 888174612 (Canada's Business Registries, ON 1718200, 2026-11-08) ⏎ SUBMIT TO: ap@wechc.com (invoicing/AP mailbox, confirmed by the referee) | tender portal (not an invoice channel): https://wechc.bidsandtenders.ca/ — bids&tenders ⏎ REFERENCE: contract RFPc 26-RR-07-01 (bid_number) — the source publishes the award under this tender / notice number and no separate contract number; tender RFPc 26-RR-07-01 (bid_number) | PO rule: purchase-order terms published (as published: shall promptly notify CHC in writing and shall not proceed until CHC issue ⏎ FROM / REMIT TO: MCAM Construction Inc. — 8-2605 Meadowbrook Lane, Windsor, ON, N8T2X9 | GST/HST 789127552RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: CAD | TERMS: statutory default for construction work ⏎ DESCRIPTION: Kitchen Renovation-Family & Warren Park | AMOUNT: 328,800.00 CAD
- **invoice_card_json**: {"bill_to": {"legal_name": "WINDSOR ESSEX COMMUNITY HOUSING CORPORATION (as registered: Canada's Business Registries, ON 1718200, 2026-11-08)", "legal_name_is_published": true, "address": "945 McDougall Street , Windsor, Ontario, Canada , N9A 1L9", "address_is_the_invoice_address": false, "tax_number": "888174612 (Canada's Business Registries, ON 1718200, 2026-11-08)", "language": "en"}, "submit_to": {"email": "ap@wechc.com", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "https://wechc.bidsandtenders.ca/ — bids&tenders", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: bids&tenders (as printed on https://www.wechc.com/procurement-information, re-read 2026-11-08)", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "tender portal (not an invoice channel)"}, "references_required": {"po_required": "purchase-order terms published (as published: shall promptly notify CHC in writing and shall not proceed until CHC issues a revised, written Purchase Order) (as printed on https://www.wechc.com/sites/default/files/2025-01/chc_purchase_order_and_work_order_terms_and_conditions.pdf, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "RFPc 26-RR-07-01 (bid_number) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference", "vendor_id_with_buyer
- **invoice_readiness**: 11/11 invoice elements present
- **ap_grade**: B
- **ap_score**: 80
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; currency known; invoice format / requirements published | missing: finance mailbox; payment terms published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: published payment terms
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms not published (buyer's default applies)
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: contract or agreement number: RFPc 26-RR-07-01 (bid_number) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference — source ca_bidsandtenders

## Vendor
- **vendor**: MCAM CONSTRUCTION INC
- **vendor_legal_name**: MCAM Construction Inc.
- **vendor_registry_id**: Corporations Canada (corporation number): 15366356; corporation number 15366356 (Corporations Canada (open data))
- **vendor_registry_url**: https://ised-isde.canada.ca/cc/lgcy/fdrlCrpDtls.html?corpId=15366356
- **vendor_registered_address**: 8 - 2605 Meadowbrook Ln, Windsor, ON, N8T 1G2, CA
- **vendor_legal_form**: Canada Business Corporations Act (Canada (federal))
- **vendor_directors_range**: 1 to 10 directors (Corporations Canada)
- **vendor_last_annual_filing**: ; Corporations Canada anniversary 2023-09-15
- **vendor_address**: 8-2605 Meadowbrook Lane, Windsor, ON, N8T2X9
- **vendor_country_basis**: bids&tenders 'Awarded' vendor table field 'Country' = 'Canada' (with ProvinceState/City/PostalCode as published)
- **vendor_bn9**: 789127552
- **vendor_gst_hst_derived**: 789127552RT0001
- **vendor_website**: https://www.mcamconstruction.ca/
- **vendor_facts_provenance**: name and address: the record's vendor block (bids&tenders (eSolutions) public procurement portals - awarded bids); registry identity: Corporations Canada (corporation number): 15366356; corporation number 15366356 (Corporations Canada (open data)) status Corporations Canada (corporation number): Active (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; exact); BN9: corporations_canada 15366356 (exact match); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2023-09-15; website: https://www.mcamconstruction.ca/
- **vendor_concentration_top_share**: Supreme Services: 8% of 111 records
- **vendor_registry_status**: Corporations Canada (corporation number): Active
- **vendor_registry_match_level**: exact
- **vendor_incorporation_date**: 2023-09-15
- **vendor_years_in_business**: 3.2 (since 2023-09-15, registry date)
- **vendor_bn_source**: corporations_canada 15366356 (exact match)

## Contract
- **po_required_as_published**: purchase-order terms published (as published: shall promptly notify CHC in writing and shall not proceed until CHC issues a revised, written Purchase Order) (as printed on https://www.wechc.com/sites/default/files/2025-01/chc_purchase_order_and_work_order_terms_and_conditions.pdf, re-read 2026-11-08)
- **contract_status**: likely active (awarded in the last 12 months, no end date published)
- **contract_reference**: {"bid_number": "RFPc 26-RR-07-01", "bidsandtenders_tender_id": "e3efe57a-bfc0-4e73-b18a-ca8ff6e2fda2", "portal": "wechc.bidsandtenders.ca", "submission_name": "Submission 1"}
- **contract_title**: Kitchen Renovation-Family & Warren Park
- **contract_description**: The scope of work in this RFPc is outcome oriented. The Proponent is required to achieve the below listed outcomes: Windsor Essex Community Housing Corporation (CHC) is seeking proponents to submit a single proposal for Kitchen Renovation Services across two (2) developments located in Windsor and …
- **number_of_bids**: 10
- **contract_or_agreement_number**: RFPc 26-RR-07-01 (bid_number) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference
- **solicitation_or_tender_number**: RFPc 26-RR-07-01 (bid_number)
- **award_or_notice_id**: e3efe57a-bfc0-4e73-b18a-ca8ff6e2fda2 (bidsandtenders_tender_id) — notice id; the award is published within this notice, the source assigns no separate award id
- **contract_value**: 328800.0
- **currency**: CAD
- **award_date**: 2026-06-04
- **contract_link**: https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/e3efe57a-bfc0-4e73-b18a-ca8ff6e2fda2
- **source**: bids&tenders (eSolutions) public procurement portals - awarded bids
- **contracts_with_canadian_suppliers**: 111
- **records_last_12_months**: 46
- **record_sources**: bids&tenders (eSolutions) public procurement portals - awarded bids (111)
- **records_with_this_vendor**: 4
- **records_in_contract_dataset**: 111 records with Canada-located vendors (this row's organisation)

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 888174612RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **payment_terms_default_policy**: statutory default for construction work (buyer published no terms): the owner must pay a proper invoice no later than 28 days after receiving it — Construction Act, R.S.O. 1990, c. C.30, s. 6.4(1), in force 2019-10-01; s. 3(1) binds the Crown (https://www.ontario.ca/laws/statute/90c30, read 2026-11-08: "an owner shall pay the amount payable under a proper invoice no later than 28 days after receiving the proper invoice from the contractor"); applies only if this contract is an improvement under the Act
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: HST 13% (Ontario) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **vendor_gst_hst_derived**: 789127552RT0001

## Pay on sight / grades
- **pay_on_sight**: yes
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: WINDSOR ESSEX COMMUNITY HOUSING CORPORATION (as registered: Canada's Business Registries, ON 1718200, 2026-11-08) — 945 McDougall Street , Windsor, Ontario, Canada , N9A 1L9 — buyer tax no. 888174612 (Canada's Business Registries, ON 1718200, 2026-11-08) ⏎ SUBMIT TO: ap@wechc.com (invoicing/AP mailbox, confirmed by the referee) | tender portal (not an invoice channel): https://wechc.bidsandtenders.ca/ — bids&tenders ⏎ REFERENCE: contract RFPc 26-RR-07-01 (bid_number) — the source publishes the award under this tender / notice number and no separate contract number; tender RFPc 26-RR-07-01 (bid_number) | PO rule: purchase-order terms published (as published: shall promptly notify CHC in writing and shall not proceed until CHC issue ⏎ FROM / REMIT TO: MCAM Construction Inc. — 8-2605 Meadowbrook Lane, Windsor, ON, N8T2X9 | GST/HST 789127552RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: CAD | TERMS: statutory default for construction work ⏎ DESCRIPTION: Kitchen Renovation-Family & Warren Park | AMOUNT: 328,800.00 CAD
- **invoice_card_json**: {"bill_to": {"legal_name": "WINDSOR ESSEX COMMUNITY HOUSING CORPORATION (as registered: Canada's Business Registries, ON 1718200, 2026-11-08)", "legal_name_is_published": true, "address": "945 McDougall Street , Windsor, Ontario, Canada , N9A 1L9", "address_is_the_invoice_address": false, "tax_number": "888174612 (Canada's Business Registries, ON 1718200, 2026-11-08)", "language": "en"}, "submit_to": {"email": "ap@wechc.com", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "https://wechc.bidsandtenders.ca/ — bids&tenders", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: bids&tenders (as printed on https://www.wechc.com/procurement-information, re-read 2026-11-08)", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "tender portal (not an invoice channel)"}, "references_required": {"po_required": "purchase-order terms published (as published: shall promptly notify CHC in writing and shall not proceed until CHC issues a revised, written Purchase Order) (as printed on https://www.wechc.com/sites/default/files/2025-01/chc_purchase_order_and_work_order_terms_and_conditions.pdf, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "RFPc 26-RR-07-01 (bid_number) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference", "vendor_id_with_buyer
- **invoice_readiness**: 11/11 invoice elements present
- **ap_grade**: B
- **ap_score**: 80
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; currency known; invoice format / requirements published | missing: finance mailbox; payment terms published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: published payment terms
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms not published (buyer's default applies)
- **facts_provenance_json**: {"mailbox": ["ap@wechc.com (invoicing/AP)", "researched by the ChatGPT/Codex agent (lane chatgpt) (page opened and quoted) on 2026-10-27", "page: https://www.wechc.com/procurement-information", "quote: \"If you are not registered for VendorCafé, all invoices should be sent to ap@wechc.com\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by self-hosted or other (mx-cluster-ca-fallback.hornetsecurity.com)", "lane file: chatgpt/chatgpt_buyer_ap_results_batch04.csv task CH-AP-00327"], "buyer_facts": ["address and phone: the buyer's own site, https://www.wechc.com/contact-us (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "invoicing requirements: the lane's AP page (https://www.wechc.com/procurement-information)", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the re

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.wechc.com/procurement-information | 2026-11-08 | ok |  |  | bids&tenders |  |  |  |  |  |  |

## Buyer site facts (org_extras, wechc.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: Windsor Essex Community Housing Corporation
- **legal_name_url**: https://www.wechc.com/
- **legal_name_quote**: Windsor Essex Community Housing Corporation | Windsor Essex Community Housing Corporation Skip to main content Main utility About CHC Our Team
- **logo_url**: https://www.wechc.com/themes/custom/wechc/logo.svg
- **logo_basis**: logo image in the site header
- **domain**: wechc.com
- **key**: b:c6ee81e5edbdf58e
- **name**: Windsor Essex Community Housing Corporation
- **website**: https://wechc.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Centralized Housing Registry
- **legal_name_stated_url**: https://www.wechc.com/about-chc
- **legal_name_stated_quote**: mited number of market rent opportunities for qualifying individuals. Additionally, CHC manages the Centralized Housing Registry (CHR) – Windsor Essex County Waitlist on behalf of the Service Manager, ensuring equitable access t
- **tel_links**: (519)254-1681

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "address": "945 McDougall Street , Windsor, Ontario, Canada , N9A 1L9", "address_country": "CA", "address_url": "https://www.wechc.com/contact-us", "address_method": "pattern", "address_quote": "s Contact Us Main Office Location 945 McDougall Street Windsor, Ontario, Canada N9A 1L9 519-254-1681 Mailing Address Windsor Essex Community Housing Corporation P.O. B", "phone": "(519) 254-1681", "phone_url": "https://www.wechc.com/contact-us", "domain": "wechc.com", "key": "b:c6ee81e5edbdf58e", "name": "Windsor Essex Community Housing Corporation", "website": "https://wechc.com/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, domain unknown)
_not read_

## Vendor role mailboxes found on its site (org_contacts)
_not read_

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Windsor Essex Community Housing Corporation | found | WINDSOR ESSEX COMMUNITY HOUSING CORPORATION | 888174612 | 1718200 | ON | ONTARIO BUSINESS CORP. | Active | 2007-01-01 | WINDSOR | Ontario |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Windsor%20Essex%20Community%20Housing%20Corporation | 2026-11-08 |
| buyer | MCAM CONSTRUCTION INC | found | MCAM Construction Inc. | 789127552 | 15366356 | CC | Business Corporation | Active | 2023-09-15 | Windsor | Ontario |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=MCAM%20CONSTRUCTION%20INC | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | api_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | MCAM CONSTRUCTION INC | found | MCAM Construction Inc. | 789127552 | corporation number 15366356 | Corporations Canada (open data) | Canada Business Corporations Act | Active | 2023-09-15 | Windsor | ON | 8 - 2605 Meadowbrook Ln, Windsor, ON, N8T 1G2 | https://open.canada.ca/data/en/dataset/0032ce54-c5dd-4b66-99a0-320a7b5e99f2 | 2026-11-08 |

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Windsor Essex Community Housing Corporation |  |  |  |  |  |  |  |  |  |  |
| b | MCAM CONSTRUCTION INC |  |  |  |  |  |  |  |  |  |  |
| v | MCAM Construction Inc. |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "b:c6ee81e5edbdf58e",
 "ap_contact_team": {
  "emails": [
   "ap@wechc.com",
   "vendorsupport@wechc.com",
   "info@wechc.com"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": "Vendors without VendorCafe registration email all invoices to AP. Invited/registered vendors submit all invoices through VendorCafe. Portal permits invoices against completed work orders and purchase orders and tracks approvals/payments.",
  "evidence": [
   {
    "email": "ap@wechc.com",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": "Vendors without VendorCafe registration email all invoices to AP. Invited/registered vendors submit all invoices through VendorCafe. Portal permits invoices against completed work orders and purchase orders and tracks approvals/payments.",
    "applies_to": "whole_organisation",
    "page_url": "https://www.wechc.com/procurement-information",
    "quote": "If you are not registered for VendorCafé, all invoices should be sent to ap@wechc.com",
    "retrieved_date": "2026-10-27",
    "found_by": "chatgpt",
    "verification": "verified",
    "source_file": "chatgpt_buyer_ap_results_batch04.csv",
    "org": "Windsor Essex Community Housing Corporation",
    "task_id": "CH-AP-00327"
   },
   {
    "email": "ap@wechc.com",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.wechc.com/procurement-information",
    "quote": "with the requested changes. Invoicing If you are not registered for VendorCafé, all invoices should be sent to ap@wechc.com If you have been invited and registered to Vendor Café, all invoices should be submitted through the portal. VendorCafé VendorCafé is CHC",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Windsor Essex Community Housing Corporation",
    "task_id": "CL-WS-00039"
   },
   {
    "email": "vendorsupport@wechc.com",
    "type": "supplier_payment",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": "Vendors without VendorCafe registration email all invoices to AP. Invited/registered vendors submit all invoices through VendorCafe. Portal permits invoices against completed work orders and purchase orders and tracks approvals/payments.",
    "applies_to": "whole_organisation",
    "page_url": "https://www.wechc.com/procurement-information",
    "quote": "Connect with a member of the CHC procurement team at vendorsupport@wechc.com.",
    "retrieved_date": "2026-10-27",
    "found_by": "chatgpt",
    "verification": "verified",
    "source_file": "chatgpt_buyer_ap_results_batch04.csv",
    "org": "Windsor Essex Community Housing Corporation",
    "task_id": "CH-AP-00327"
   },
   {
    "email": "vendorsupport@wechc.com",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.wechc.com/procurement-information",
    "quote": ". Connect with a member of the CHC procurement team at vendorsupport@wechc.com. Purchase Order / Work Order Terms & Conditions CHC Purchase Order and Work Order Terms and Conditions If you'd like to work w",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Windsor Essex Community Housing Corporation",
    "task_id": "CL-WS-00039"
   },
   {
    "email": "info@wechc.com",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.wechc.com/current-tenants/payment-options",
    "quote": "yment options to accommodate your needs. For any questions or inquiries, please contact our finance team at 519-254-1681 ext. 2259 or email info@wechc.com. Please note: Rent payments not received by the 1st of the month will be considered late. Cheques or Money Orders Secure drop boxes are",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Windsor Essex Community Housing Corporation",
    "task_id": "CL-WS-00227"
   }
  ]
 },
 "research_status": {
  "found": 5
 },
 "queries_tried": [
  "site:wechc.com supplier invoices accounts payable; site:wechc.com \"ap@wechc.com\" invoice; site:wechc.com procurement information VendorCafe; direct/web-reader pages returned502; opened actual official procurement page in browser and expanded CurrentVendors, Invoicing and VendorCafe sections",
  "site:wechc.com supplier invoices accounts payable; site:wechc.com \"ap@wechc.com\" invoice; site:wechc.com procurement information VendorCafe; direct/web-reader pages returned502; opened actual official procurement page in browser and expanded CurrentVendors, Invoicing and VendorCafe sections",
  "web search for the buyer's invoicing / accounts payable page (the search only gave the address); the page then read by tools/deep_pages.py with the crawler's rules, no AI",
  "web search for the buyer's invoicing / accounts payable page (the search only gave the address); the page then read by tools/deep_pages.py with the crawler's rules, no AI",
  "web search for the buyer's invoicing / accounts payable page (the search only gave the address); the page then read by tools/deep_pages.py with the crawler's rules, no AI"
 ],
 "ingested_at": "2026-11-09T16:04:50Z"
}
```

## PO-level open data naming this buyer
_none_

## Contract records between the pair (dataset)
| record_id | source | status | title | value | currency | start | end | identifiers | link |
|---|---|---|---|---|---|---|---|---|---|
| ca_bidsandtenders:4243df00-0f8f-4fa2-85da-f90d80238ec3:1 | ca_bidsandtenders | end_date_unknown | Essex Court - Bathroom Upgrades | 355200.0 | CAD |  |  | {"bid_number": "RFT-26-32-02", "bidsandtenders_tender_id": "4243df00-0f8f-4fa2-85da-f90d80238ec3", "portal": "wechc.bidsandtenders.ca", "submission_name": "Submission 1"} | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/4243df00-0f8f-4fa2-85da-f90d80238ec3 |
| ca_bidsandtenders:e3efe57a-bfc0-4e73-b18a-ca8ff6e2fda2:1 | ca_bidsandtenders | end_date_unknown | Kitchen Renovation-Family & Warren Park | 328800.0 | CAD |  |  | {"bid_number": "RFPc 26-RR-07-01", "bidsandtenders_tender_id": "e3efe57a-bfc0-4e73-b18a-ca8ff6e2fda2", "portal": "wechc.bidsandtenders.ca", "submission_name": "Submission 1"} | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/e3efe57a-bfc0-4e73-b18a-ca8ff6e2fda2 |
| ca_bidsandtenders:c67c8b47-f09b-4041-a729-46c31a4acadf:1 | ca_bidsandtenders | ongoing_inferred | 415 University - Retaining Wall | 129000.0 | CAD |  |  | {"bid_number": "RFT-26-30-01", "bidsandtenders_tender_id": "c67c8b47-f09b-4041-a729-46c31a4acadf", "portal": "wechc.bidsandtenders.ca", "submission_name": "Submission 1"} | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/c67c8b47-f09b-4041-a729-46c31a4acadf |
| ca_bidsandtenders:1b829cc5-8b40-42e3-a88f-3c1bea118286:1 | ca_bidsandtenders | end_date_unknown | Curry McKay-1745 McKay Restoration | 98800.0 | CAD |  |  | {"bid_number": "RFT-26-03-03", "bidsandtenders_tender_id": "1b829cc5-8b40-42e3-a88f-3c1bea118286", "portal": "wechc.bidsandtenders.ca", "submission_name": "Submission 1"} | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/1b829cc5-8b40-42e3-a88f-3c1bea118286 |

## The buyer's other Canadian-vendor records (first 60 of 107)
| record_id | vendor | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_bidsandtenders:18ebe66d-76ae-44f5-890c-ea57a7a69f06:1 | jimmy hvac services | Water Heaters Replacement – Various Locations | 191134.5 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/18ebe66d-76ae-44f5-890c-ea57a7a69f06 |
| ca_bidsandtenders:6c758a18-4539-4e12-a3b9-70031bfd3251:1 | Piera Con Enterprises Inc. | Parking Lot Reconstruction and Other Civil Works – Nancy Court, Leamington, ON | 300500.0 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/6c758a18-4539-4e12-a3b9-70031bfd3251 |
| ca_bidsandtenders:b0e5bd52-caf1-4e24-904c-5a985c7f2a6c:1 | RC White Ltd | 920 Ouellette Storm Piping Replacement | 113250.0 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/b0e5bd52-caf1-4e24-904c-5a985c7f2a6c |
| ca_bidsandtenders:10551c81-df98-460b-af80-c2fe52bb67ca:1 | Ecowall Systems Ltd. | Essex Court-Concrete Replacement | 385000.0 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/10551c81-df98-460b-af80-c2fe52bb67ca |
| ca_bidsandtenders:10b50f27-acd0-4887-bcba-1e13be08b8b4:1 | Gvoltz | Accessible Unit Renovations - 605 Mill St | 105308.94 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/10b50f27-acd0-4887-bcba-1e13be08b8b4 |
| ca_bidsandtenders:4570b2dc-bf1c-480c-8e0a-e2138b1419f0:1 | Home Shield Exteriors Inc | Exterior Envelope Rehabilitation - Nancy Court (Townhouses) | 291435.0 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/4570b2dc-bf1c-480c-8e0a-e2138b1419f0 |
| ca_bidsandtenders:48aef0b9-c493-4bc2-baa1-2885f2a5e756:1 | Aura Concepts Inc | Kitchen Reno-Arbour & 14 King | 139200.0 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/48aef0b9-c493-4bc2-baa1-2885f2a5e756 |
| ca_bidsandtenders:48aef0b9-c493-4bc2-baa1-2885f2a5e756:2 | 14451139 Canada Inc | Kitchen Reno-Arbour & 14 King | 218300.0 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/48aef0b9-c493-4bc2-baa1-2885f2a5e756 |
| ca_bidsandtenders:35dab1e3-263a-4376-ba7d-9359671bf968:1 | Aum 306 Inc. | Accessible Unit Renovations - 111 Brien & 165 Talbot | 160320.0 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/35dab1e3-263a-4376-ba7d-9359671bf968 |
| ca_bidsandtenders:29b37794-dd6c-4c2a-acc7-bd6d65dfaa03:1 | Humo Restorations | Exterior Envelope & Balcony Restoration – 445 Glengarry | 461860.0 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/29b37794-dd6c-4c2a-acc7-bd6d65dfaa03 |
| ca_bidsandtenders:63ab41db-c755-49e7-8cd7-7d3e825a11a4:1 | Supreme Services | 2455 Rivard Mail Room | 45000.0 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/63ab41db-c755-49e7-8cd7-7d3e825a11a4 |
| ca_bidsandtenders:3fbbcbc9-8fbd-4d72-8131-464933d27851:1 | Powerserve Inc | Exhaust Fan & Switch Replacement – Ford Ferndale | 148.97 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/3fbbcbc9-8fbd-4d72-8131-464933d27851 |
| ca_bidsandtenders:6b69047b-3881-4b47-bad1-9487515f4847:1 | RAINFORCES LTD. | 17 Nancy & 29 Lutsch–Exterior Envelope Upgrades | 499500.0 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/6b69047b-3881-4b47-bad1-9487515f4847 |
| ca_bidsandtenders:34256804-1131-4004-8d8e-19646cf32d16:1 | 14451139 Canada Inc | Essex Court-Kitchen Upgrades | 604450.0 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/34256804-1131-4004-8d8e-19646cf32d16 |
| ca_bidsandtenders:e796e7ef-e45d-446a-baff-b8e80d9460ba:1 | 14451139 Canada Inc | Accessible Unit Renovations - 642 St Charles St. | 97000.0 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/e796e7ef-e45d-446a-baff-b8e80d9460ba |
| ca_bidsandtenders:a9b7c9a1-f439-417b-823e-d9cc6d62fde5:1 | Powerserve Inc | Mechanical Upgrades _165 Talbot | 507479.0 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/a9b7c9a1-f439-417b-823e-d9cc6d62fde5 |
| ca_bidsandtenders:bb715b8f-ed7c-4714-9b24-dfeb0a84530a:1 | Powerserve Inc | Make-Up Air & Boiler Replacements – 2455 Rivard | 389514.0 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/bb715b8f-ed7c-4714-9b24-dfeb0a84530a |
| ca_bidsandtenders:4243df00-0f8f-4fa2-85da-f90d80238ec3:2 | 14451139 Canada Inc | Essex Court - Bathroom Upgrades | 180000.0 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/4243df00-0f8f-4fa2-85da-f90d80238ec3 |
| ca_bidsandtenders:4243df00-0f8f-4fa2-85da-f90d80238ec3:3 | Supreme Services | Essex Court - Bathroom Upgrades | 182400.0 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/4243df00-0f8f-4fa2-85da-f90d80238ec3 |
| ca_bidsandtenders:eeccfeed-2a46-43fb-a626-b4bfe777b4ab:1 | Gillett Roofing Inc | Metal Roof Replacement - 642 St. Charles, Belle River | 122950.0 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/eeccfeed-2a46-43fb-a626-b4bfe777b4ab |
| ca_bidsandtenders:2485323f-0fab-4466-b38e-507db922406b:1 | T.P. Crawford Limited | Flat Roof Replacement | 805000.0 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/2485323f-0fab-4466-b38e-507db922406b |
| ca_bidsandtenders:2485323f-0fab-4466-b38e-507db922406b:2 | Semple Gooder Roofing Corporation | Flat Roof Replacement | 830000.0 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/2485323f-0fab-4466-b38e-507db922406b |
| ca_bidsandtenders:f17cc709-3c8a-4b7a-b20b-74f28c10a3d1:1 | AVI CONSTRUCTION INC. | St. Joseph-Building Envelope and Civil Upgrades | 2770000.0 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/f17cc709-3c8a-4b7a-b20b-74f28c10a3d1 |
| ca_bidsandtenders:e223dae4-8fcd-4192-a14d-543c6d30da47:1 | BRADA CONSTRUCTION LIMITED | 920 Ouellette - Balcony Restoration | 1637088.8 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/e223dae4-8fcd-4192-a14d-543c6d30da47 |
| ca_bidsandtenders:44053349-5314-48d8-a3a9-e6c3298c020c:1 | Powerserve Inc | Mechanical Upgrades - 605 Mill | 229750.0 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/44053349-5314-48d8-a3a9-e6c3298c020c |
| ca_bidsandtenders:bf37002e-5b79-43a5-8f55-b9f8af0564a6:1 | 9079653 Canada Corporation o/a Combustion Techs | Boiler Replacement – 140 Bridge | 119288.0 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/bf37002e-5b79-43a5-8f55-b9f8af0564a6 |
| ca_bidsandtenders:b097433b-ae4f-4803-aca3-721cef070ee5:1 | Tac Group Incorporated | Asphalt Parking Lot Reconstruction - Slater (2) | 816700.0 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/b097433b-ae4f-4803-aca3-721cef070ee5 |
| ca_bidsandtenders:ecb6eb99-4f6a-4686-9571-742f25010760:1 | NAILED IT ROOFING & CONSTRUCTION LTD. | Shingled Roof Replacement - VL | 259441.0 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/ecb6eb99-4f6a-4686-9571-742f25010760 |
| ca_bidsandtenders:bffb8453-ebd6-422d-ac92-2c3ba13825ff:1 | avanti paving | Curry McKay – Asphalt Driveway Replacement – Phase 2 | 634000.0 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/bffb8453-ebd6-422d-ac92-2c3ba13825ff |
| ca_bidsandtenders:331cea34-5eb1-43e7-95f5-06c4afdb9d98:1 | Powerserve Inc | Electrical Services | 109100.0 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/331cea34-5eb1-43e7-95f5-06c4afdb9d98 |
| ca_bidsandtenders:331cea34-5eb1-43e7-95f5-06c4afdb9d98:2 | Studerus Electric Inc. | Electrical Services | 113000.0 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/331cea34-5eb1-43e7-95f5-06c4afdb9d98 |
| ca_bidsandtenders:0205c6a3-d8c9-4d4c-bcf4-af663c2080e8:1 | chad hartman construction | Concrete Driveways and Civil Works Slater 1 (Hartford & Slater) & Woodward (Woodward Blvd & Chaviva Ct) | 260350.0 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/0205c6a3-d8c9-4d4c-bcf4-af663c2080e8 |
| ca_bidsandtenders:f64889a6-2c8d-4865-9949-5acef6dac4c8:1 | 1000997393 ONTARIO INC. | Unit Conversions - 920 Ouellette | 115970.0 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/f64889a6-2c8d-4865-9949-5acef6dac4c8 |
| ca_bidsandtenders:42824670-7055-48c0-84dc-822236a2b156:1 | RC White Ltd | 920 Ouellette Basement Lateral Piping Replacement | 331000.0 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/42824670-7055-48c0-84dc-822236a2b156 |
| ca_bidsandtenders:52be58ed-8939-40b1-a148-f239446fd310:1 | Etka Construction inc. | Bloomfield-Exterior Envelope Upgrades | 829000.0 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/52be58ed-8939-40b1-a148-f239446fd310 |
| ca_bidsandtenders:3a37ad30-d383-4491-9e8e-b137c5f3cb42:1 | 14451139 Canada Inc | St. Joseph-Bathroom Renovations | 371430.0 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/3a37ad30-d383-4491-9e8e-b137c5f3cb42 |
| ca_bidsandtenders:341b5166-4af2-42b2-8281-1bb347ada1b8:1 | jimmy hvac services | Water Heater-2BD-Curry McKay | 159879.65 |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/341b5166-4af2-42b2-8281-1bb347ada1b8 |
| ca_bidsandtenders:0e0e0591-5426-4c3e-a9d1-5e154d2acc94:1 | 14451139 Canada Inc | St. Joseph – Kitchen Renovations |  |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/0e0e0591-5426-4c3e-a9d1-5e154d2acc94 |
| ca_bidsandtenders:14813a20-4a82-41d8-8022-5168e790fd38:1 | Opulence Development | Barrier Free Conversions - 120 Oak & 140 Bridge |  |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/14813a20-4a82-41d8-8022-5168e790fd38 |
| ca_bidsandtenders:6b1b50f3-2736-4757-9b3c-0c61245a1f41:1 | D.C. McCloskey Engineering Ltd. | Consulting Services for Civil Works Project - VL |  |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/6b1b50f3-2736-4757-9b3c-0c61245a1f41 |
| ca_bidsandtenders:4bb6df9d-bbc7-4b70-94a3-2cb6d555833d:1 | Sandal Building Limited | Curry McKay-Exterior Envelope Upgrades |  |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/4bb6df9d-bbc7-4b70-94a3-2cb6d555833d |
| ca_bidsandtenders:15c8cfe3-0c96-450b-a6cd-dcd123817887:1 | Orkin Canada | Pest Control Services |  |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/15c8cfe3-0c96-450b-a6cd-dcd123817887 |
| ca_bidsandtenders:1c9e971e-5b87-46c9-81c6-a7d57072287a:1 | Supreme Services | Office Vestibule Accessibility Retrofit – 605 Mill Street |  |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/1c9e971e-5b87-46c9-81c6-a7d57072287a |
| ca_bidsandtenders:a839546e-6bd4-4361-bb3e-9c12cea89b4a:1 | Talis Group Inc | Winter Maintenance |  |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/a839546e-6bd4-4361-bb3e-9c12cea89b4a |
| ca_bidsandtenders:1daa4185-6552-4747-9034-2c10ffded76b:1 | Accent Building Sciences Inc. | Exterior Envelope Assessment - VL |  |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/1daa4185-6552-4747-9034-2c10ffded76b |
| ca_bidsandtenders:ce6f387d-c429-4ecf-b663-e3e355aa5c35:1 | Optimus SBR Inc. | Organizational Review |  |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/ce6f387d-c429-4ecf-b663-e3e355aa5c35 |
| ca_bidsandtenders:ad4a51f5-1bb0-44bf-992e-04bc1131b8f6:1 | Aura Concepts Inc | Bathroom & Kitchen Renovation - Lauzon Road |  |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/ad4a51f5-1bb0-44bf-992e-04bc1131b8f6 |
| ca_bidsandtenders:dcf4a943-f379-4a52-832b-67d6fe6f80c5:1 | Aura Concepts Inc | Bathroom & Kitchen Renovation – 140 Bridge |  |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/dcf4a943-f379-4a52-832b-67d6fe6f80c5 |
| ca_bidsandtenders:c8c37a18-5787-4026-a984-a29189ce4027:1 | Supreme Services | Entry Door Replacement - 255 Riverside |  |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/c8c37a18-5787-4026-a984-a29189ce4027 |
| ca_bidsandtenders:8c7ab602-1b8a-46ee-99b2-9697811e7f21:1 | IRS Locks Inc. | Door Hardware Upgrades - VL |  |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/8c7ab602-1b8a-46ee-99b2-9697811e7f21 |
| ca_bidsandtenders:bba40dde-edb2-40f5-9614-e067989e75c6:1 | P & G Landscaping & Snow Removal Inc. | Concrete Civil Works - Devon III |  |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/bba40dde-edb2-40f5-9614-e067989e75c6 |
| ca_bidsandtenders:06a4c114-328f-4335-9eaf-2536616f4143:1 | P & G Landscaping & Snow Removal Inc. | Concrete Civil Works - Devon II |  |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/06a4c114-328f-4335-9eaf-2536616f4143 |
| ca_bidsandtenders:473e5a67-a1eb-4dc0-8552-64b55c86bfe5:1 | Tac Group Incorporated | Asphalt Civil Works - Devon I |  |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/473e5a67-a1eb-4dc0-8552-64b55c86bfe5 |
| ca_bidsandtenders:0df669f9-3981-4117-b188-33e95e10bcb3:1 | Piera Con Enterprises Inc. | Asphalt Civil Works - VL |  |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/0df669f9-3981-4117-b188-33e95e10bcb3 |
| ca_bidsandtenders:0f6af6eb-0c5d-48c8-8824-e604ed1e2926:1 | Haller Mechanical Contractors Inc. | Supply Fan Replacement _VL |  |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/0f6af6eb-0c5d-48c8-8824-e604ed1e2926 |
| ca_bidsandtenders:1fa3b720-ed8a-4251-991e-7a07c56344a0:1 | Sandal Building Limited | Curry McKay - Window and Door Replacement |  |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/1fa3b720-ed8a-4251-991e-7a07c56344a0 |
| ca_bidsandtenders:cbe9444c-5851-45d3-b1a2-9657983111d0:1 | Pinchin Ltd | Exterior Envelope Consulting Services - VL |  |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/cbe9444c-5851-45d3-b1a2-9657983111d0 |
| ca_bidsandtenders:15e893f9-8953-4b7d-80ac-414bfe441767:1 | P & G Landscaping & Snow Removal Inc. | Curry McKay - Concrete Replacement |  |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/15e893f9-8953-4b7d-80ac-414bfe441767 |
| ca_bidsandtenders:85073aed-bbb3-478a-8e9e-db7ae04291e3:1 | KG Building Restoration Inc. | Balcony Restoration - 120 Oak Street |  |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/85073aed-bbb3-478a-8e9e-db7ae04291e3 |
| ca_bidsandtenders:1bc0d01a-0b31-4841-b380-342c43063bf5:1 | CSK ARCHITECTS INC | Barrier Free Conversion Architectural Consulting Services – VL |  |  |  | https://wechc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/1bc0d01a-0b31-4841-b380-342c43063bf5 |
| … 47 more rows in the .json | ||||||

## The vendor's other buyers in the dataset (first 60 of 0)
_none_

## Open questions for hand research (layer 2)

- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
