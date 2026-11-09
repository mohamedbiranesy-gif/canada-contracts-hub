# S1-14 — Natural Resources Canada ⇄ OPAL-RT Technologies Inc.

Stratum: **S1_gold_complete_published_PO_rule** · pay on sight: yes · channel tier 1 · AP grade A · missing: —

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Natural Resources Canada (label per Wikidata Q349770, exact name match + country + organisation claims; 2026-11-08) — 580 Booth Street, Ottawa, ON K1A 0E4, Canada
SUBMIT TO: invoicing-facturation@nrcan-rncan.gc.ca (invoicing/AP mailbox, confirmed by the referee) | format: PDF file format (as printed on https://natural-resources.canada.ca/corporate/corporate-overview/procurement-contracting-natural-resources-canada, re-read 2026-11-08)
REFERENCE: contract CW2468736 (an_contract_number); tender WS5864388923 (an_solicitation_number) | PO rule: yes (as published: reference number (normally the purchase order number)
FROM / REMIT TO: OPAL-RT Technologies Inc. — 1751 Richardson st. suite 1060, Montreal, Quebec, H3K 1G6 | GST/HST 141839878RT0001 (account derived from the BN9) | NEQ 1146732749
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: CAD | TERMS: 60 days of the receipt (as printed on https://natural-resources.canada.ca/minerals-mining/services-m
DESCRIPTION: Real-Time Simulator for National Resources Canada | AMOUNT: 66,871.14 CAD
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 97
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 1
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Natural Resources Canada (company (private sector), FED) — public contract / purchase award with a published end date (dated record): OPAL-RT Technologies Inc. | subject: Real-Time Simulator for National Resources Canada | instrument: contract | contract number: CW2468736 (an_contract_number); CW2468736 (an_reference_numbers); CW2468736 (an_reference_number_latest) | solicitation: WS5864388923 (an_solicitation_number) | all identifiers: {"an_reference_number_latest": "CW2468736", "an_reference_numbers": ["CW2468736"], "an_contract_number": "CW2468736", "an_solicitation_number": "WS5864388923"} | value: 66871.14 CAD | awarded 2026-10-08, start 2026-10-08, end 2027-10-07 | published by: CanadaBuys award notices | record: https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cw2468736 | vendor in Canada because: supplierAddressCountry-fournisseurAdressePays-eng = 'CA' | status rule: active (published end date today or later) | this buyer has 1365 records with Canada-located vendors (1010 distinct vendors; 485 in the last 12 months; latest 2026-10-29)
- **how_relationship_was_found**: the award record was harvested from the public procurement source named in `source` (scripts/<source> pipeline), matched to the buyer by its canonical name/key, and the vendor's Canada location read from the source's own vendor address/country field (`vendor_country_basis`)
- **keys**: b:2cd4b5b6bc78a14d|b:48f4de3fce8d81ec|b:8290f81dc98bccfe|b:883f697ff92109de|b:d54110572c166491
- **tier**: A
- **grade**: 4
- **records_with_this_vendor**: 1

## Buyer
- **buyer**: Natural Resources Canada
- **buyer_website**: https://natural-resources.canada.ca/home
- **buyer_address**: 580 Booth St, Ottawa, Ontario, K1A 0E4, Canada
- **buyer_legal_name_as_published**: Natural Resources Canada (label per Wikidata Q349770, exact name match + country + organisation claims; 2026-11-08)
- **buyer_logo_url**: https://www.canada.ca/etc/designs/canada/wet-boew/assets/sig-blk-en.svg
- **buyer_type**: company (private sector)
- **buyer_sector**: private sector
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q349770; Canadian federal department; national mapping agency
- **buyer_founded**: 1995-00-00 (Wikidata Q349770, exact name match + country + organisation claims; 2026-11-08)
- **buyer_facts_provenance**: address: the buyer's record / buyer table; legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; invoice mailing address: the lane's AP page (https://natural-resources.canada.ca/corporate/corporate-overview/procurement-contracting-natural-resources-canada); invoicing requirements: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_payment_method_preference**: direct deposit only (as printed on https://natural-resources.canada.ca/sites/nrcan/files/r1617E.pdf, re-read 2026-11-08)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 5

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: invoicing-facturation@nrcan-rncan.gc.ca
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://natural-resources.canada.ca/corporate/corporate-overview/procurement-contracting-natural-resources-canada
- **email_evidence_quote**: RCan and will remain unpaid until valid payment referencing is provided. All invoices must be submitted using our invoicing e-mail address: Invoicing-Facturation@nrcan-rncan.gc.ca Notes: Only one copy of the invoice should be sent to the Department. Departmental contact (project authority)
- **email_evidence_context**: required for processing the payment be missing, the supplier’s invoice will be returned at the discretion of NRCan and will remain unpaid until valid payment referencing is provided. All invoices must be submitted using our invoicing e-mail address: Invoicing-Facturation@nrcan-rncan.gc.ca Notes: Only one copy of the invoice should be sent to the Department. Departmental contact (project authority) identified in the contract can be Cc’d on the email. Suppliers are required to use a PDF file format, as other formats are not compatible (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: invoicing-facturation@nrcan-rncan.gc.ca (invoicing/AP) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08 | page: https://natural-resources.canada.ca/corporate/corporate-overview/procurement-contracting-natural-resources-canada | quote: "RCan and will remain unpaid until valid payment referencing is provided. All invoices must be submitted using our invoicing e-mail address: Invoicing-Facturatio" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00041
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Microsoft 365
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none; sp=none; rua=mailto:dmarc@cyber.gc.ca
- **dmarc_record_domain**: nrcan-rncan.gc.ca
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 ip4:205.193.40.17 ip4:205.193.40.18  include:spf.protection.outlook.com include:emrs._spf.ssc-spc.gc.ca include:amazonses.com include:aspmx.pardot.com include:_spf.salesforce.com a:ovh-appl25.eduperformance.com ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoice_mailing_address**: 580 Booth Street, Ottawa, ON K1A 0E4, Canada
- **invoicing_requirements**: Natural Resources Canada (NRCan) Accounts Payable; all vendor invoices must be submitted in PDF format (one invoice per PDF) to Invoicing-Facturation@nrcan-rncan.gc.ca; payment status inquiries directed to invoicepaymentcentre-centredepaiementdefactures@nrcan-rncan.gc.ca. | invoice format as published: PDF file format (as printed on https://natural-resources.canada.ca/corporate/corporate-overview/procurement-contracting-natural-resources-canada, re-read 2026-11-08)
- **payment_terms_as_published**: 60 days of the receipt (as printed on https://natural-resources.canada.ca/minerals-mining/services-mining-industry/mining-certified-reference-materials/order, re-read 2026-11-08)
- **payment_terms_default_policy**: Government of Canada standard: payment within 30 days of receipt of a valid invoice (Treasury Board Directive on Payments) — policy default, not this buyer's published term
- **po_required_as_published**: yes (as published: reference number (normally the purchase order number) (as printed on https://natural-resources.canada.ca/corporate/corporate-overview/procurement-contracting-natural-resources-canada, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "payment_terms": "60 days of the receipt (as printed on https://natural-resources.canada.ca/minerals-mining/services-mining-industry/mining-certified-reference-materials/order, re-read 2026-11-08)", "po_required": "yes (as published: reference number (normally the purchase order number) (as printed on https://natural-resources.canada.ca/corporate/corporate-overview/procurement-contracting-natural-resources-canada, re-read 2026-11-08)", "invoice_format": "PDF file format (as printed on https://natural-resources.canada.ca/corporate/corporate-overview/procurement-contracting-natural-resources-canada, re-read 2026-11-08)", "mailing_address": "580 Booth Street, Ottawa, ON K1A 0E4, Canada", "requirements_text": "Natural Resources Canada (NRCan) Accounts Payable; all vendor invoices must be submitted in PDF format (one invoice per PDF) to Invoicing-Facturation@nrcan-rncan.gc.ca; payment status inquiries directed to invoicepaymentcentre-centredepaiementdefactures@nrcan-rncan.gc.ca. | invoice format as publish"}
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Natural Resources Canada (label per Wikidata Q349770, exact name match + country + organisation claims; 2026-11-08) — 580 Booth Street, Ottawa, ON K1A 0E4, Canada ⏎ SUBMIT TO: invoicing-facturation@nrcan-rncan.gc.ca (invoicing/AP mailbox, confirmed by the referee) | format: PDF file format (as printed on https://natural-resources.canada.ca/corporate/corporate-overview/procurement-contracting-natural-resources-canada, re-read 2026-11-08) ⏎ REFERENCE: contract CW2468736 (an_contract_number); tender WS5864388923 (an_solicitation_number) | PO rule: yes (as published: reference number (normally the purchase order number) ⏎ FROM / REMIT TO: OPAL-RT Technologies Inc. — 1751 Richardson st. suite 1060, Montreal, Quebec, H3K 1G6 | GST/HST 141839878RT0001 (account derived from the BN9) | NEQ 1146732749 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: CAD | TERMS: 60 days of the receipt (as printed on https://natural-resources.canada.ca/minerals-mining/services-m ⏎ DESCRIPTION: Real-Time Simulator for National Resources Canada | AMOUNT: 66,871.14 CAD
- **invoice_card_json**: {"bill_to": {"legal_name": "Natural Resources Canada (label per Wikidata Q349770, exact name match + country + organisation claims; 2026-11-08)", "legal_name_is_published": true, "address": "580 Booth Street, Ottawa, ON K1A 0E4, Canada", "address_is_the_invoice_address": true, "tax_number": "", "language": "en-fr (bilingual body: federal / New Brunswick; use the language of its invoicing page: en)"}, "submit_to": {"email": "invoicing-facturation@nrcan-rncan.gc.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "580 Booth Street, Ottawa, ON K1A 0E4, Canada", "format": "PDF file format (as printed on https://natural-resources.canada.ca/corporate/corporate-overview/procurement-contracting-natural-resources-canada, re-read 2026-11-08)", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "yes (as published: reference number (normally the purchase order number) (as printed on https://natural-resources.canada.ca/corporate/corporate-overview/procurement-contracting-natural-resources-canada, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "CW2468736 (an_contract_number); CW2468736 (an_reference_numbers); CW2468736 (an_reference_number_latest)", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: CW2468736 (an_contract_number) — source canada_federal"}, "terms": {"payment_terms": "60 days o
- **invoice_readiness**: 10/11 invoice elements present
- **invoice_missing**: AP phone or contact for follow-up
- **ap_grade**: A
- **ap_score**: 88
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published; payment cycle or method published (plausibility) | missing: finance mailbox; AP phone or AP contact | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms published
- **language_hint**: en
- **template_language**: en-fr (bilingual body: federal / New Brunswick; use the language of its invoicing page: en)
- **invoice_reference_hint**: contract or agreement number: CW2468736 (an_contract_number) — source canada_federal

## Vendor
- **vendor**: OPAL-RT Technologies Inc.
- **vendor_legal_name**: OPAL-RT Technologies Inc.
- **vendor_trading_name**: Opal-RT Technologies (schema.org Organization name on the vendor's site: https://www.opal-rt.com/)
- **vendor_registry_id**: Corporations Canada (corporation number): 2927560; NEQ 1146732749 (Registraire des entreprises du Québec (open data))
- **vendor_registry_url**: https://ised-isde.canada.ca/cc/lgcy/fdrlCrpDtls.html?corpId=2927560
- **vendor_registered_address**: 1751  RICHARDSON, BUR. 1060, MONTREAL, QC, H3K 1G6, CA
- **vendor_neq**: 1146732749 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_legal_form**: Société par actions ou compagnie — CANADA: Loi canadienne sur les sociétés par actions, L.R.C. (1985), c. C-44
- **vendor_activity_code**: CAE 7721 — DÉVELOPPEMENT ET COMMERCIALISATION D'ORDINATEUR PARALLÈLE TEMPS-RÉEL
- **vendor_employees_quebec**: De 250 à 499
- **vendor_establishments_quebec**: OPAL-RT TECHNOLOGIES INC.: 18152 rue J.-A.-Bombardier, Mirabel (Québec), J7J0H5
- **vendor_directors_range**: 1 to 9 directors (Corporations Canada)
- **vendor_last_annual_filing**: REQ annual declaration 2025; Corporations Canada anniversary 1993-06-07
- **vendor_address**: 1751 Richardson st. suite 1060, Montreal, Quebec, H3K 1G6
- **vendor_country_basis**: supplierAddressCountry-fournisseurAdressePays-eng = 'CA'
- **vendor_bn9**: 141839878
- **vendor_gst_hst_derived**: 141839878RT0001
- **vendor_website**: https://www.opal-rt.com
- **vendor_emails**: marketing@opal-rt.com
- **vendor_phone**: 0086 10 66116880
- **vendor_contact_evidence_url**: https://www.opal-rt.com/contact-us/
- **vendor_logo_url**: https://www.opal-rt.com/wp-content/uploads/2025/05/LOGO_GE.png?format=auto
- **vendor_website_status**: site answers
- **vendor_linkedin_url**: https://www.linkedin.com/company/opal-rt-technologies/
- **vendor_contacts_found_by**: gemini lane, referee-verified on https://www.opal-rt.com/press-room/opal-rt-user-community/
- **vendor_facts_provenance**: name and address: the record's vendor block (CanadaBuys award notices); registry identity: Corporations Canada (corporation number): 2927560; NEQ 1146732749 (Registraire des entreprises du Québec (open data)) status Corporations Canada (corporation number): Active; Québec REQ (NEQ): Immatriculée (1997-04-23) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; exact); BN9: corporations_canada 2927560 (exact match); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 1993-06-07; phone / role e-mails / logo: the vendor's own site, https://www.opal-rt.com/contact-us/ (tools/org_contacts.py, org_extras.py); role / billing mailboxes researched by the gemini lane, referee-verified on https://www.opal-rt.com/press-room/opal-rt-user-community/; website: https://www.opal-rt.com (site answers); NEQ: 1146732749 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_concentration_top_share**: AF LOGISTICS: 0% of 1365 records
- **vendor_registry_status**: Corporations Canada (corporation number): Active; Québec REQ (NEQ): Immatriculée (1997-04-23)
- **vendor_registry_match_level**: exact
- **vendor_incorporation_date**: 1993-06-07
- **vendor_years_in_business**: 33.4 (since 1993-06-07, registry date)
- **vendor_bn_source**: corporations_canada 2927560 (exact match)

## Contract
- **po_required_as_published**: yes (as published: reference number (normally the purchase order number) (as printed on https://natural-resources.canada.ca/corporate/corporate-overview/procurement-contracting-natural-resources-canada, re-read 2026-11-08)
- **contract_status**: active (published end date today or later)
- **contract_reference**: {"an_reference_number_latest": "CW2468736", "an_reference_numbers": ["CW2468736"], "an_contract_number": "CW2468736", "an_solicitation_number": "WS5864388923"}
- **contract_title**: Real-Time Simulator for National Resources Canada
- **commodity**: 41112100 Transducers
- **contract_description**: Real-Time Simulator for National Resources Canada (the record's title; the source publishes no separate description)
- **contract_or_agreement_number**: CW2468736 (an_contract_number); CW2468736 (an_reference_numbers); CW2468736 (an_reference_number_latest)
- **solicitation_or_tender_number**: WS5864388923 (an_solicitation_number)
- **commodity_codes**: UNSPSC 41112100 (Transducers)
- **contract_value**: 66871.14
- **currency**: CAD
- **award_date**: 2026-10-08
- **start_date**: 2026-10-08
- **end_date**: 2027-10-07
- **contract_link**: https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cw2468736
- **source**: CanadaBuys award notices
- **contracts_with_canadian_suppliers**: 1365
- **records_last_12_months**: 485
- **record_sources**: Proactive Publication – Contracts over $10,000 (624); CanadaBuys legacy award notices 2012-2022 (394); Proactive Publication – Contracts over $10,000 + CanadaBuys award notices (+ CanadaBuys tender notice) (82); CanadaBuys award notices (+ CanadaBuys tender notice) (55)
- **records_with_this_vendor**: 1
- **records_in_contract_dataset**: 1365 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: Other Business services not Elsewhere Specified (85); Scientific services (77); N/A (53)

## Tax / currency / terms (derived)
- **payment_terms_default_policy**: Government of Canada standard: payment within 30 days of receipt of a valid invoice (Treasury Board Directive on Payments) — policy default, not this buyer's published term
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: HST 13% (Ontario) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **vendor_gst_hst_derived**: 141839878RT0001

## Pay on sight / grades
- **pay_on_sight**: yes
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Natural Resources Canada (label per Wikidata Q349770, exact name match + country + organisation claims; 2026-11-08) — 580 Booth Street, Ottawa, ON K1A 0E4, Canada ⏎ SUBMIT TO: invoicing-facturation@nrcan-rncan.gc.ca (invoicing/AP mailbox, confirmed by the referee) | format: PDF file format (as printed on https://natural-resources.canada.ca/corporate/corporate-overview/procurement-contracting-natural-resources-canada, re-read 2026-11-08) ⏎ REFERENCE: contract CW2468736 (an_contract_number); tender WS5864388923 (an_solicitation_number) | PO rule: yes (as published: reference number (normally the purchase order number) ⏎ FROM / REMIT TO: OPAL-RT Technologies Inc. — 1751 Richardson st. suite 1060, Montreal, Quebec, H3K 1G6 | GST/HST 141839878RT0001 (account derived from the BN9) | NEQ 1146732749 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: CAD | TERMS: 60 days of the receipt (as printed on https://natural-resources.canada.ca/minerals-mining/services-m ⏎ DESCRIPTION: Real-Time Simulator for National Resources Canada | AMOUNT: 66,871.14 CAD
- **invoice_card_json**: {"bill_to": {"legal_name": "Natural Resources Canada (label per Wikidata Q349770, exact name match + country + organisation claims; 2026-11-08)", "legal_name_is_published": true, "address": "580 Booth Street, Ottawa, ON K1A 0E4, Canada", "address_is_the_invoice_address": true, "tax_number": "", "language": "en-fr (bilingual body: federal / New Brunswick; use the language of its invoicing page: en)"}, "submit_to": {"email": "invoicing-facturation@nrcan-rncan.gc.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "580 Booth Street, Ottawa, ON K1A 0E4, Canada", "format": "PDF file format (as printed on https://natural-resources.canada.ca/corporate/corporate-overview/procurement-contracting-natural-resources-canada, re-read 2026-11-08)", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "yes (as published: reference number (normally the purchase order number) (as printed on https://natural-resources.canada.ca/corporate/corporate-overview/procurement-contracting-natural-resources-canada, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "CW2468736 (an_contract_number); CW2468736 (an_reference_numbers); CW2468736 (an_reference_number_latest)", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: CW2468736 (an_contract_number) — source canada_federal"}, "terms": {"payment_terms": "60 days o
- **invoice_readiness**: 10/11 invoice elements present
- **invoice_missing**: AP phone or contact for follow-up
- **ap_grade**: A
- **ap_score**: 88
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published; payment cycle or method published (plausibility) | missing: finance mailbox; AP phone or AP contact | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms published
- **facts_provenance_json**: {"mailbox": ["invoicing-facturation@nrcan-rncan.gc.ca (invoicing/AP)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08", "page: https://natural-resources.canada.ca/corporate/corporate-overview/procurement-contracting-natural-resources-canada", "quote: \"RCan and will remain unpaid until valid payment referencing is provided. All invoices must be submitted using our invoicing e-mail address: Invoicing-Facturatio\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00041"], "buyer_facts": ["address: the buyer's record / buyer table", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "invoice mailing address: the lane's AP page (https://natural-resources.canada.ca/corporate/corporate-overview/procurement-contracting-natural-resources-canada)", "invoicing requirements: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "PO requirement: the mailbox's evidence

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://natural-resources.canada.ca/corporate/corporate-overview/procurement-contracting-natural-resources-canada | 2026-11-08 | ok |  | yes (as published: reference number (normally the purchase order number) |  |  |  | PDF file format |  |  | at the invoice clearly indicates “Paid by Credit Card” Valid NRCan reference number (normally the purchase order number). This number is 10 numeric digits long or 9 alphanumeric digits Each submitted invoice should conta |

## Buyer site facts (org_extras, domain unknown)
_not read_

## Buyer role mailboxes found on its site (org_contacts)
_not read_

## Vendor site facts (org_extras, opal-rt.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://www.opal-rt.com/wp-content/uploads/2025/05/LOGO_GE.png?format=auto
- **logo_basis**: logo image in the site header
- **bn**: 164968693
- **bn_label**: tps://www.facebook.com/help/164968693
- **bn_url**: https://www.opal-rt.com/privacy-policy/
- **bn_quote**: ook Inc. You can learn more about interest-based advertising from Facebook by visiting this page: https://www.facebook.com/help/164968693837950 To opt-out from Facebook’s interest-based ads, follow these instructions from Facebook: https
- **domain**: opal-rt.com
- **key**: vendor:OPAL-RT Technologies Inc.
- **name**: OPAL-RT Technologies Inc.
- **website**: https://opal-rt.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Opal-RT Technologies
- **jsonld_logo**: https://www.opal-rt.com/wp-content/uploads/2025/04/logo.svg
- **jsonld_url**: https://www.opal-rt.com/
- **jsonld_quote**: {"@context":"https:\/\/schema.org","@graph":[{"@type":"WebPage","@id":"https:\/\/www.opal-rt.com\/","url":"https:\/\/www.opal-rt.com\/","name":"OPAL-RT | Trusted Real-Time Simulation Solutions | Discover OPAL-RT Technologies for Innovation | Explore OPAL-RT Simulator Systems | OPAL-RT","isPartOf":{"
- **jsonld_page**: https://www.opal-rt.com/
- **legal_name_stated**: OPAL-RT TECHNOLOGIES INC
- **legal_name_stated_url**: https://www.opal-rt.com/legal-notice/
- **legal_name_stated_quote**: load center Skip to content / Legal Notice Legal Notice This website (the “Website”) is provided by OPAL-RT TECHNOLOGIES INC. (“OPAL-RT”) and is subject to the terms and conditions outlined in this Legal Notice (the “Agreeme
- **mentions**: {'payment_method': {'text': 'interaction so that we can offer better site experiences and tools in the future', 'url': 'https://www.opal-rt.com/privacy-policy/', 'quote': 'mproved services. We also use cookies to help us compile aggregate data about site traffic and site interaction so that we can offer better site experiences and tools in the future. We use cookies to: Understand and save user’s preferences for future visits. C'}}
- **linkedin_url**: https://www.linkedin.com/company/opal-rt-technologies/
- **tel_links**: +33 (0)4 43 55 77 26; 0086 10 66116880; +91-80-2520.0305 / 105; +1 734-418-2961; +1 877 935 2323; +33 1 75 60 24 89; +55
- **legal_name**: OPAL-RT TECHNOLOGIES, Inc
- **legal_name_url**: https://www.opal-rt.com/
- **legal_name_quote**: RT Community News Blog Power in Mind magazine Learning center Support center Portal | Logo du site OPAL-RT TECHNOLOGIES, Inc Products & services Software Software platforms Software toolboxes Software communication protocols

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "1751 Rue Richardson, Suite 1060, Montréal, QC H3K 1G6", "address_country": "CA", "address_url": "https://www.opal-rt.com/contact-us/", "address_method": "pattern", "address_quote": "1-877-935-2323 Fax. 514-935-4994 1751 Rue Richardson, Suite 1060, Montréal, QC H3K 1G6 OPAL-RT China Tel. 0086 10 66116880 Landgent Center Block A, 20 E 3rd Ring Midd", "phone": "0086 10 66116880", "phone_url": "https://www.opal-rt.com/contact-us/", "domain": "opal-rt.com", "key": "vd:opal-rt.com", "name": "OPAL-RT Technologies Inc.", "website": "https://opal-rt.com/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Natural Resources Canada | Q349770 | exact name match + country + organisation claims |  | Natural Resources Canada | Ressources naturelles Canada | Canadian federal department; national mapping agency |  | Canada | 1995-00-00 | Gatineau |
| v | OPAL-RT Technologies Inc. |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "b:2cd4b5b6bc78a14d",
 "ap_contact_team": {
  "emails": [
   "invoicing-facturation@nrcan-rncan.gc.ca",
   "invoicepaymentcentre-centredepaiementdefactures@nrcan-rncan.gc.ca",
   "nrcan.direct_deposit_inquiries-renseignements_sur_le_depot_direct.rncan@canada.ca"
  ],
  "invoice_portal": null,
  "phone": "343-292-8331",
  "mailing_address": null,
  "invoicing_requirements": "Federal supplier-payment / direct-deposit contact listed by PSPC for this institution.",
  "evidence": [
   {
    "email": "invoicing-facturation@nrcan-rncan.gc.ca",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://natural-resources.canada.ca/corporate/corporate-overview/procurement-contracting-natural-resources-canada",
    "quote": "RCan and will remain unpaid until valid payment referencing is provided. All invoices must be submitted using our invoicing e-mail address: Invoicing-Facturation@nrcan-rncan.gc.ca Notes: Only one copy of the invoice should be sent to the Department. Departmental contact (project authority)",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Natural Resources Canada",
    "task_id": "CL-WS-00041"
   },
   {
    "email": "invoicepaymentcentre-centredepaiementdefactures@nrcan-rncan.gc.ca",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://natural-resources.canada.ca/corporate/corporate-overview/procurement-contracting-natural-resources-canada",
    "quote": "ment inquiries). This e-mail address is to be used only for submitting invoices. For inquiries regarding payment status, send an e-mail to: invoicepaymentcentre-centredepaiementdefactures@nrcan-rncan.gc.ca NRCan can no longer accept invoices by courier or regular mail. We appreciate your w",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Natural Resources Canada",
    "task_id": "CL-WS-00041"
   },
   {
    "email": "nrcan.direct_deposit_inquiries-renseignements_sur_le_depot_direct.rncan@canada.ca",
    "type": "supplier_payment",
    "invoice_portal": null,
    "phone": "343-292-8331",
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.canada.ca/en/public-services-procurement/services/payments-to-from-government/direct-deposit/businesses/suppliers.html",
    "quote": "Natural Resources Canada Direct Deposit Inquiries Telephone: 343-292-8331 Email: nrcan.direct_deposit_inquiries-renseignements_sur_le_depot_direct.rncan@canada.ca",
    "retrieved_date": "2026-11-07",
    "found_by": "chatgpt",
    "verification": "verified",
    "source_file": "chatgpt_verify_buyer_ap_results_batch02.csv",
    "org": "Natural Resources Canada",
    "task_id": "CH-VF2-0121",
    "verified_via": "https://web.archive.org/web/20260710105949/https://www.canada.ca/en/public-services-procurement/services/payments-to-from-government/direct-deposit/businesses/suppliers.html"
   },
   {
    "email": "nrcan.direct_deposit_inquiries-renseignements_sur_le_depot_direct.rncan@canada.ca",
    "type": "supplier_payment",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": "Federal supplier-payment / direct-deposit contact listed by PSPC for this institution.",
    "applies_to": "parent_central_ap",
    "page_url": "https://www.canada.ca/en/public-services-procurement/services/payments-to-from-government/direct-deposit/businesses/suppliers.html",
    "quote": "Natural Resources Canada nrcan.direct_deposit_inquiries-renseignements_sur_le_depot_direct.rncan@canada.ca",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_federal01.csv",
    "org": "Natural Resources Canada",
    "task_id": "CL-FED-00121",
    "verified_via": "https://web.archive.org/web/20260710105949/https://www.canada.ca/en/public-services-procurement/services/payments-to-from-government/direct-deposit/businesses/suppliers.html"
   }
  ]
 },
 "research_status": {
  "found": 4
 },
 "queries_tried": [
  "Opened official PSPC Direct deposit for government suppliers English table and linked French table; exact institution/email comparison against assigned verification task",
  "PSPC 'Direct deposit for government suppliers' contact table",
  "web search for the buyer's invoicing / accounts payable page (the search only gave the address); the page then read by tools/deep_pages.py with the crawler's rules, no AI",
  "web search for the buyer's invoicing / accounts payable page (the search only gave the address); the page then read by tools/deep_pages.py with the crawler's rules, no AI"
 ],
 "ingested_at": "2026-11-09T16:04:50Z"
}
```

## PO-level open data naming this buyer
_none_

## Contract records between the pair (dataset)
_none_

## The buyer's other Canadian-vendor records (first 60 of 1)
| record_id | vendor | title | value | start | end | link |
|---|---|---|---|---|---|---|
| canada_federal:cb:CW2395414 | HARNOIS ÉNERGIES INC. | E60HL-250052-004-HL Bulk Aviation Fuel 2025-2027 | 62105332.8 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cw2395414 |

## The vendor's other buyers in the dataset (first 60 of 29)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| canada_federal:cb:CW2468736 | Department of Natural Resources  (NRCan) | Real-Time Simulator for National Resources Canada | 66871.14 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cw2468736 |
| seao_quebec:1107752:opal-rt-technologies-inc | Université McGill | P0549731 | 67809.8 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=7e7de5c0-7d46-43a9-82f1-709003e89cd5 |
| seao_quebec:1107753:opal-rt-technologies-inc | Université McGill | P0549732 | 32653.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=2aa2416d-f779-4e06-b20e-a078b251b16a |
| seao_quebec:1129942:opal-rt-technologies | Université Concordia | Real-Time License | 47345.35 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=5deea89f-cff7-4a53-9de6-a02e10e1bbeb |
| seao_quebec:1528992:opal-rt-technologies-inc | Université Concordia | ACQUISITION OF A Real-time simulator (HYPERSIM) | 46675.69 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=a350d331-ca64-4fad-b7db-bba198e27a3c |
| seao_quebec:1791472:opal-rt-technologies-inc | Université du Québec à Trois-Rivières | Simulateur en temps réel HIL | 612830.45 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=3c5a8082-4877-4452-b84d-e244fa948e79 |
| seao_quebec:20131348:opal-rt-technologies-inc | Université du Québec à Trois-Rivières | Simulateur HIL en temps réel | 73413.2 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=00ad42ad-4a49-4ec6-95fe-646e71558c71 |
| seao_quebec:280590:opal-rt-technologies-inc | Université de Sherbrooke -Service des ressources financières-  Secteur approvisionnement | Traitement et simulation mumériques en temps réel | 55323.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=e2121ae6-31a6-4035-b9c5-39964384f09f |
| seao_quebec:385942:opal-rt-technologies | Université Concordia | Achat de logiciel de simulation | 32346.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=ee83c4be-0567-4ddd-bae0-406121473a58 |
| seao_quebec:486801:opal-rt-technologies-inc | École Polytechnique | MEMS array control systems | 229290.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=c8443873-b8a2-4ed5-94cb-e7f0fc02da2a |
| seao_quebec:517156:opal-rt-technologies-inc | Université de Sherbrooke -Service des ressources financières-  Secteur approvisionnement | Plate forme de développement de contrôleurs | 81032.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=53ed5d9c-eb11-48e1-b40b-e762f270eac8 |
| seao_quebec:537683:opal-rt-technologies-inc | Université McGill | P0261116 | 72768.68 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=0d37c341-e551-46d4-86e6-5062d0f341f9 |
| seao_quebec:589386:opal-rt-technologies | École Polytechnique | Equipement scientifique - Simulateur FPGA | 190307.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=fc303d87-2e18-48a1-be05-06fec5f83877 |
| seao_quebec:873054:opal-rt-technologies-inc | Énergie Hydroélectrique Ouiatchouan | Fourniture de services professionnels pour les essais de validation des équipements | 75990.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=129aef31-6a02-4953-a04f-1a9708495d2a |
| us_state_ny_abo:ehig-g5x3:c1ba9ef3a97b1418 | Power Authority of the State of New York | FURNISH DELIVER INSTALL AND COMMISSION SIMULATORS FOR AGILE THAT WOULD PROVIDE MVSS AND ALLOW FOR FUTURE EXPANSION | 1808649.0 |  |  | https://data.ny.gov/d/ehig-g5x3 |
| us_state_ny_abo:ehig-g5x3:584a5f21007a9d7f | Power Authority of the State of New York | AGILE LAB SUPPORT SERVICES | 5000.0 |  |  | https://data.ny.gov/d/ehig-g5x3 |
| us_state_texas_lbb:714-PO 82278 | The University of Texas at Arlington | Simulation Network Bundle | 57927.0 |  |  | https://cms.lbb.texas.gov/Default.aspx?aid=714&cid=PO%2082278 |
| ny_procurement_ehig-g5x3:4600004390_power_authority_of_the_state_of_new_york_opal-rt_technologies_inc_555 | Power Authority of the State of New York | AGILE LAB SUPPORT SERVICES | 5000.0 |  |  | https://data.ny.gov/dataset/ehig-g5x3 |
| ny_procurement_ehig-g5x3:4600003373_power_authority_of_the_state_of_new_york_opal-rt_technologies_inc_556 | Power Authority of the State of New York | FURNISH, DELIVER, INSTALL, AND COMMISSION SIMULATORS FOR AGILE THAT WOULD PROVIDE MVSS AND ALLOW FOR FUTURE EXPANSION | 1745409.0 |  |  | https://data.ny.gov/dataset/ehig-g5x3 |
| ny_procurement_ehig-g5x3:4600004390_power_authority_of_the_state_of_new_york_opal-rt_technologies_inc_596 | Power Authority of the State of New York | AGILE LAB SUPPORT SERVICES | 5000.0 |  |  | https://data.ny.gov/dataset/ehig-g5x3 |
| ny_procurement_ehig-g5x3:4600003373_power_authority_of_the_state_of_new_york_opal-rt_technologies_inc_597 | Power Authority of the State of New York | FURNISH, DELIVER, INSTALL, AND COMMISSION SIMULATORS FOR AGILE THAT WOULD PROVIDE MVSS AND ALLOW FOR FUTURE EXPANSION | 1745409.0 |  |  | https://data.ny.gov/dataset/ehig-g5x3 |
| ny_procurement_ehig-g5x3:4600004390_power_authority_of_the_state_of_new_york_opal-rt_technologies_inc_633 | Power Authority of the State of New York | AGILE LAB SUPPORT SERVICES | 5000.0 |  |  | https://data.ny.gov/dataset/ehig-g5x3 |
| ny_procurement_ehig-g5x3:4600003373_power_authority_of_the_state_of_new_york_opal-rt_technologies_inc_634 | Power Authority of the State of New York | FURNISH DELIVER INSTALL AND COMMISSION SIMULATORS FOR AGILE THAT WOULD PROVIDE MVSS AND ALLOW FOR FUTURE EXPANSION | 1808649.0 |  |  | https://data.ny.gov/dataset/ehig-g5x3 |
| us_ny_state_authorities_procurement:bb0f385c358f5ce6 | Power Authority of the State of New York | AGILE LAB SUPPORT SERVICES | 5000.0 |  |  | https://data.ny.gov/dataset/Procurement-Report-for-State-Authorities/ehig-g5x3 |
| us_ny_state_authorities_procurement:a82c46f72dd2a375 | Power Authority of the State of New York | FURNISH, DELIVER, INSTALL, AND COMMISSION SIMULATORS FOR AGILE THAT WOULD PROVIDE MVSS AND ALLOW FOR FUTURE EXPANSION | 1745409.0 |  |  | https://data.ny.gov/dataset/Procurement-Report-for-State-Authorities/ehig-g5x3 |
| us_ny_state_authorities_procurement:2e194568d8aa3070 | Power Authority of the State of New York | AGILE LAB SUPPORT SERVICES | 5000.0 |  |  | https://data.ny.gov/dataset/Procurement-Report-for-State-Authorities/ehig-g5x3 |
| us_ny_state_authorities_procurement:211cc21fbf5a468b | Power Authority of the State of New York | FURNISH, DELIVER, INSTALL, AND COMMISSION SIMULATORS FOR AGILE THAT WOULD PROVIDE MVSS AND ALLOW FOR FUTURE EXPANSION | 1745409.0 |  |  | https://data.ny.gov/dataset/Procurement-Report-for-State-Authorities/ehig-g5x3 |
| us_ny_state_authorities_procurement:d41992de2ea85e1c | Power Authority of the State of New York | AGILE LAB SUPPORT SERVICES | 5000.0 |  |  | https://data.ny.gov/dataset/Procurement-Report-for-State-Authorities/ehig-g5x3 |
| us_ny_state_authorities_procurement:9043663e9970a977 | Power Authority of the State of New York | FURNISH DELIVER INSTALL AND COMMISSION SIMULATORS FOR AGILE THAT WOULD PROVIDE MVSS AND ALLOW FOR FUTURE EXPANSION | 1808649.0 |  |  | https://data.ny.gov/dataset/Procurement-Report-for-State-Authorities/ehig-g5x3 |

## Open questions for hand research (layer 2)

- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

Read 2026-11-09 (Claude, integrator lane). Budget rule (PLAN §4d): layer 1 already carries this buyer's confirmed channel, PO rule and terms with quotes; the notes below add only what changes how the invoice is built.

**Federal Canadian buyer.** Layer 1 holds NRCan's own AP instruction (PO/contract reference required; payment "60 days of the receipt" as quoted — check
the quote: the federal standard under the Financial Administration Act / PSPC general conditions is 30 days after receipt of a proper invoice, interest
after that (Treasury Board Directive on Payments; PSPC General Conditions 2010A s. 10); 60 days may refer to a specific instrument). Invoices to a federal
department must show the PSPC contract number and the department's reference / requisition number, GST/HST at 5 % (federal departments pay GST/HST and
recover it internally — TAX_FEDERAL in the row), remittance by direct deposit (Receiver General) — the vendor must be enrolled for direct deposit with
PSPC. The proactive-disclosure record in the row is the public reference; the contract number on the PWGSC/NRCan contract document is what AP matches.
