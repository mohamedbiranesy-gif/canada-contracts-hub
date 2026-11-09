# S1-19 — Pfizer Canada ULC/Pfizer Canada SRI ⇄ Graphite Public Affairs

Stratum: **S1_gold_complete_published_PO_rule** · pay on sight: yes · channel tier 1 · AP grade B · missing: —

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Pfizer Canada ULC (stated on https://www.pfizer.ca/en/terms-use-0-1) — PO Box 34600 Bartlett TN 38184-0600 (as printed on https://www.pfizer.ca/en/suppliers, re-read 2026-11-08)
SUBMIT TO: canadaapinvoices@pfizer.com (invoicing/AP mailbox, confirmed by the referee) | portal (not confirmed as an invoice channel): supplier / vendor portal | format: invoices, or send pdf images via (as printed on https://channels.pfizer.ca/en/supplier/invoicing, re-read 2026-11-08)
REFERENCE: none in the record | PO rule: yes (as published: must match the details of this Purchase Order)
FROM / REMIT TO: GRAPHITE PUBLIC AFFAIRS INC. (as registered: Canada's Business Registries, BC BC0944636, 2026-11-08) — FIRM_ADDRESS: 939 Boulderwood Rise, Victoria, BC, V8Y 3G5, CAN; vendor_address_missing: False | GST/HST 805353083 (Canada's Business Registries, BC BC0944636, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: null
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 90
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 1
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Pfizer Canada ULC/Pfizer Canada SRI (organisation (type not stated in the record), jurisdiction not stated) — public contract / purchase award in the last 12 months (dated record): Graphite Public Affairs | subject: null | awarded 2026-10-16, start 2026-10-15, end 2027-01-31 | published by: FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv) | record: https://www.lobbyistsregistrar.bc.ca/app/secure/orl/lrs/do/vwRg?cno=6379&regId=56585088 | vendor in Canada because: FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv)=939 Boulderwood Rise, Victoria, BC, V8Y 3G5, CAN | status rule: likely active (record dated in the last 12 months: FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv))
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: lead:b6d2a535e78f5691
- **tier**: B
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv); 0 in the contract dataset)

## Buyer
- **buyer**: Pfizer Canada ULC/Pfizer Canada SRI
- **buyer_website**: https://www.pfizer.ca/
- **buyer_address**: 17300 Trans-Canada Highway, Kirkland, Quebec H9J 2M5
- **buyer_phone**: 514 695-0500
- **buyer_contact_evidence_url**: https://www.pfizer.ca/en/contact-us
- **buyer_legal_name_as_published**: Pfizer Canada ULC (stated on https://www.pfizer.ca/en/terms-use-0-1)
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/pfizer
- **buyer_type**: organisation (type not stated in the record)
- **buyer_sector**: not stated
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.pfizer.ca/en/contact-us (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); website: site answers; invoice mailing address: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoicing requirements: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: canadaapinvoices@pfizer.com
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.pfizer.ca/en/suppliers
- **email_evidence_quote**: procurement contact listed on this Purchase Order. Invoice Submission Pfizer Canada Preferred Method: eMail Regular Mail Overnight/Courier CanadaAPInvoices@pfizer.com Pfizer Canada PO Box 34600 Bartlett TN 38184-0600 USA Pfizer Canada Attn: 6730 Lenox Center Court Memphis TN 38115 USA For
- **email_evidence_context**: in significant payment delay. Please confirm receipt of order, price and ship date via email to the authorized procurement contact listed on this Purchase Order. Invoice Submission Pfizer Canada Preferred Method: eMail Regular Mail Overnight/Courier CanadaAPInvoices@pfizer.com Pfizer Canada PO Box 34600 Bartlett TN 38184-0600 USA Pfizer Canada Attn: 6730 Lenox Center Court Memphis TN 38115 USA For assistance regarding all invoices submitted to Pfizer Canada Global Financial Shared Services, PO Box 34600, Bartlett, TN 3818 (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: canadaapinvoices@pfizer.com (invoicing/AP) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08 | page: https://www.pfizer.ca/en/suppliers | quote: "procurement contact listed on this Purchase Order. Invoice Submission Pfizer Canada Preferred Method: eMail Regular Mail Overnight/Courier CanadaAPInvoices@pfiz" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Proofpoint | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00092
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Proofpoint
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1;p=reject;fo=1;rua=mailto:dmarc_rua@emaildefense.proofpoint.com,mailto:dmarc.rua@pfizer.com;ruf=mailto:dmarc_ruf@emaildefense.proofpoint.com,mailto:dmarc.ruf@pfizer.com
- **dmarc_record_domain**: pfizer.com
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 include:%{ir}.%{v}.%{d}.spf.has.pphosted.com include:_spf.pfizer.com include:spf1.pfizer.com include:_spf2.pfizer.com include:_spf3.pfizer.com include:mktomail.com include:amazonses.com -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: yes (v=BIMI1;l=https://vmc.digicert.com/45c752eb-0853-4bc6-a07b-e3897306afc0.svg;a=ht)
- **invoice_mailing_address**: PO Box 34600 Bartlett TN 38184-0600 (as printed on https://www.pfizer.ca/en/suppliers, re-read 2026-11-08)
- **invoicing_requirements**: invoice format as published: invoices, or send pdf images via (as printed on https://channels.pfizer.ca/en/supplier/invoicing, re-read 2026-11-08)
- **po_required_as_published**: yes (as published: must match the details of this Purchase Order) (as printed on https://www.pfizer.ca/en/suppliers, re-read 2026-11-08)
- **invoice_portal_url**: supplier / vendor portal
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "po_required": "yes (as published: must match the details of this Purchase Order) (as printed on https://www.pfizer.ca/en/suppliers, re-read 2026-11-08)", "portal_url": "supplier / vendor portal", "portal_kind": "actionable supplier / invoice portal named by the buyer", "invoice_format": "invoices, or send pdf images via (as printed on https://channels.pfizer.ca/en/supplier/invoicing, re-read 2026-11-08)", "mailing_address": "PO Box 34600 Bartlett TN 38184-0600 (as printed on https://www.pfizer.ca/en/suppliers, re-read 2026-11-08)", "requirements_text": "invoice format as published: invoices, or send pdf images via (as printed on https://channels.pfizer.ca/en/supplier/invoicing, re-read 2026-11-08)"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Pfizer Canada ULC (stated on https://www.pfizer.ca/en/terms-use-0-1) — PO Box 34600 Bartlett TN 38184-0600 (as printed on https://www.pfizer.ca/en/suppliers, re-read 2026-11-08) ⏎ SUBMIT TO: canadaapinvoices@pfizer.com (invoicing/AP mailbox, confirmed by the referee) | portal (not confirmed as an invoice channel): supplier / vendor portal | format: invoices, or send pdf images via (as printed on https://channels.pfizer.ca/en/supplier/invoicing, re-read 2026-11-08) ⏎ REFERENCE: none in the record | PO rule: yes (as published: must match the details of this Purchase Order) ⏎ FROM / REMIT TO: GRAPHITE PUBLIC AFFAIRS INC. (as registered: Canada's Business Registries, BC BC0944636, 2026-11-08) — FIRM_ADDRESS: 939 Boulderwood Rise, Victoria, BC, V8Y 3G5, CAN; vendor_address_missing: False | GST/HST 805353083 (Canada's Business Registries, BC BC0944636, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: null
- **invoice_card_json**: {"bill_to": {"legal_name": "Pfizer Canada ULC (stated on https://www.pfizer.ca/en/terms-use-0-1)", "legal_name_is_published": true, "address": "PO Box 34600 Bartlett TN 38184-0600 (as printed on https://www.pfizer.ca/en/suppliers, re-read 2026-11-08)", "address_is_the_invoice_address": true, "tax_number": "", "language": "fr (Québec buyer; French first; its invoicing page is in English, English also accepted)"}, "submit_to": {"email": "canadaapinvoices@pfizer.com", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "supplier / vendor portal", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "PO Box 34600 Bartlett TN 38184-0600 (as printed on https://www.pfizer.ca/en/suppliers, re-read 2026-11-08)", "format": "invoices, or send pdf images via (as printed on https://channels.pfizer.ca/en/supplier/invoicing, re-read 2026-11-08)", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "portal (not confirmed as an invoice channel)"}, "references_required": {"po_required": "yes (as published: must match the details of this Purchase Order) (as printed on https://www.pfizer.ca/en/suppliers, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: must match the details of this Purchase Order) (as printed on http
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: B
- **ap_score**: 80
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; currency known; invoice format / requirements published | missing: finance mailbox; payment terms published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published payment terms
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms not published (buyer's default applies)
- **language_hint**: en
- **template_language**: fr (Québec buyer; French first; its invoicing page is in English, English also accepted)
- **invoice_reference_hint**: the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: must match the details of this Purchase Order) (as printed on https://www.pfizer.ca/en/suppliers, re-read 2026-11-08))

## Vendor
- **vendor**: Graphite Public Affairs
- **vendor_legal_name**: GRAPHITE PUBLIC AFFAIRS INC. (as registered: Canada's Business Registries, BC BC0944636, 2026-11-08)
- **vendor_registry_id**: BC0944636 (BC)
- **vendor_registry_url**: https://ised-isde.canada.ca/cbr-rec/en/search?q=Graphite%20Public%20Affairs
- **vendor_registered_address**: Sidney, BC (registered office city / province; Canada's Business Registries, BC BC0944636, 2026-11-08)
- **vendor_legal_form**: BC Company (Canada's Business Registries, BC BC0944636, 2026-11-08)
- **vendor_address**: FIRM_ADDRESS: 939 Boulderwood Rise, Victoria, BC, V8Y 3G5, CAN; vendor_address_missing: False
- **vendor_country_basis**: FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv)=939 Boulderwood Rise, Victoria, BC, V8Y 3G5, CAN
- **vendor_bn9**: 805353083 (Canada's Business Registries, BC BC0944636, 2026-11-08)
- **vendor_gst_hst_derived**: 805353083RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_facts_provenance**: name and address: the record's vendor block (FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv)); registry identity: BC0944636 (BC) status Active (Canada's Business Registries, BC BC0944636, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: registry: Canada's Business Registries, BC BC0944636, 2026-11-08; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2012-06-29
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Active (Canada's Business Registries, BC BC0944636, 2026-11-08)
- **vendor_incorporation_date**: 2012-06-29
- **vendor_years_in_business**: 14.4 (since 2012-06-29, registry date)
- **vendor_bn_source**: registry: Canada's Business Registries, BC BC0944636, 2026-11-08

## Contract
- **po_required_as_published**: yes (as published: must match the details of this Purchase Order) (as printed on https://www.pfizer.ca/en/suppliers, re-read 2026-11-08)
- **contract_status**: likely active (record dated in the last 12 months: FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv))
- **contract_title**: null
- **contract_description**: null (the record's title; the source publishes no separate description)
- **award_date**: 2026-10-16
- **start_date**: 2026-10-15
- **end_date**: 2027-01-31
- **contract_link**: https://www.lobbyistsregistrar.bc.ca/app/secure/orl/lrs/do/vwRg?cno=6379&regId=56585088
- **source**: FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv)
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv); 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (QC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 805353083RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: yes
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Pfizer Canada ULC (stated on https://www.pfizer.ca/en/terms-use-0-1) — PO Box 34600 Bartlett TN 38184-0600 (as printed on https://www.pfizer.ca/en/suppliers, re-read 2026-11-08) ⏎ SUBMIT TO: canadaapinvoices@pfizer.com (invoicing/AP mailbox, confirmed by the referee) | portal (not confirmed as an invoice channel): supplier / vendor portal | format: invoices, or send pdf images via (as printed on https://channels.pfizer.ca/en/supplier/invoicing, re-read 2026-11-08) ⏎ REFERENCE: none in the record | PO rule: yes (as published: must match the details of this Purchase Order) ⏎ FROM / REMIT TO: GRAPHITE PUBLIC AFFAIRS INC. (as registered: Canada's Business Registries, BC BC0944636, 2026-11-08) — FIRM_ADDRESS: 939 Boulderwood Rise, Victoria, BC, V8Y 3G5, CAN; vendor_address_missing: False | GST/HST 805353083 (Canada's Business Registries, BC BC0944636, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: null
- **invoice_card_json**: {"bill_to": {"legal_name": "Pfizer Canada ULC (stated on https://www.pfizer.ca/en/terms-use-0-1)", "legal_name_is_published": true, "address": "PO Box 34600 Bartlett TN 38184-0600 (as printed on https://www.pfizer.ca/en/suppliers, re-read 2026-11-08)", "address_is_the_invoice_address": true, "tax_number": "", "language": "fr (Québec buyer; French first; its invoicing page is in English, English also accepted)"}, "submit_to": {"email": "canadaapinvoices@pfizer.com", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "supplier / vendor portal", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "PO Box 34600 Bartlett TN 38184-0600 (as printed on https://www.pfizer.ca/en/suppliers, re-read 2026-11-08)", "format": "invoices, or send pdf images via (as printed on https://channels.pfizer.ca/en/supplier/invoicing, re-read 2026-11-08)", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "portal (not confirmed as an invoice channel)"}, "references_required": {"po_required": "yes (as published: must match the details of this Purchase Order) (as printed on https://www.pfizer.ca/en/suppliers, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: must match the details of this Purchase Order) (as printed on http
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: B
- **ap_score**: 80
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; currency known; invoice format / requirements published | missing: finance mailbox; payment terms published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published payment terms
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms not published (buyer's default applies)
- **facts_provenance_json**: {"mailbox": ["canadaapinvoices@pfizer.com (invoicing/AP)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08", "page: https://www.pfizer.ca/en/suppliers", "quote: \"procurement contact listed on this Purchase Order. Invoice Submission Pfizer Canada Preferred Method: eMail Regular Mail Overnight/Courier CanadaAPInvoices@pfiz\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Proofpoint", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00092"], "buyer_facts": ["address and phone: the buyer's own site, https://www.pfizer.ca/en/contact-us (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "website: site answers", "invoice mailing address: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoicing requirements: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and add

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.pfizer.ca/en/suppliers | 2026-11-08 | ok |  | yes (as published: must match the details of this Purchase Order) | supplier / vendor portal |  | PO Box 34600 Bartlett TN 38184-0600 |  |  |  | and / or services delivered, packing slip(s), and invoice details (price, quantity, including line numbers and freight terms) must match the details of this Purchase Order (include Purchase Order number of all packing sl |

## Buyer site facts (org_extras, pfizer.ca)
- **status**: ok
- **pages**: 5
- **language**: en
- **domain**: pfizer.ca
- **key**: lead:b6d2a535e78f5691
- **name**: Pfizer Canada ULC/Pfizer Canada SRI
- **website**: https://pfizer.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Pfizer Canada ULC
- **legal_name_stated_url**: https://www.pfizer.ca/en/terms-use-0-1
- **legal_name_stated_quote**: nada Contact Us Investors Careers Media Science Contact Us Terms Of Use This website is operated by Pfizer Canada ULC (the "Company") and contains information intended only for residents of Canada. Other countries may
- **linkedin_url**: https://www.linkedin.com/company/pfizer

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "17300 Trans-Canada Highway, Kirkland, Quebec H9J 2M5", "address_country": "CA", "address_url": "https://www.pfizer.ca/en/contact-us", "address_method": "pattern", "address_quote": "ess Head Office Pfizer Canada ULC, 17300 Trans-Canada Highway, Kirkland, Quebec H9J 2M5, Tel.: 514 695-0500 or 1 877 633-2001 Pfizer Global Supply (Brandon) 720-17th S", "phone": "514 695-0500", "phone_url": "https://www.pfizer.ca/en/contact-us", "emails": "corporate.affairs.canada@pfizer.com", "emails_url": "https://www.pfizer.ca/en/contact-us", "domain": "pfizer.ca", "key": "lead:b6d2a535e78f5691", "name": "Pfizer Canada ULC/Pfizer Canada SRI", "website": "https://pfizer.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, domain unknown)
_not read_

## Vendor role mailboxes found on its site (org_contacts)
_not read_

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Pfizer Canada ULC/Pfizer Canada SRI |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:b6d2a535e78f5691",
 "ap_contact_team": {
  "emails": [
   "canadaapinvoices@pfizer.com",
   "canadaprocurement@pfizer.com"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "canadaapinvoices@pfizer.com",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.pfizer.ca/en/suppliers",
    "quote": "procurement contact listed on this Purchase Order. Invoice Submission Pfizer Canada Preferred Method: eMail Regular Mail Overnight/Courier CanadaAPInvoices@pfizer.com Pfizer Canada PO Box 34600 Bartlett TN 38184-0600 USA Pfizer Canada Attn: 6730 Lenox Center Court Memphis TN 38115 USA For",
    "retrieved_date": "2026-11-02",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Pfizer Canada ULC/Pfizer Canada SRI",
    "task_id": "CL-LT-01689"
   },
   {
    "email": "canadaapinvoices@pfizer.com",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.pfizer.ca/en/suppliers",
    "quote": "procurement contact listed on this Purchase Order. Invoice Submission Pfizer Canada Preferred Method: eMail Regular Mail Overnight/Courier CanadaAPInvoices@pfizer.com Pfizer Canada PO Box 34600 Bartlett TN 38184-0600 USA Pfizer Canada Attn: 6730 Lenox Center Court Memphis TN 38115 USA For",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Pfizer Canada ULC/Pfizer Canada SRI",
    "task_id": "CL-WS-00092"
   },
   {
    "email": "canadaprocurement@pfizer.com",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.pfizer.ca/en/suppliers",
    "quote": "order terms and conditions. If you do not find the information you require on this site, please feel free to contact Canada Procurement at CanadaProcurement@pfizer.com Registration for New Suppliers Pfizer’s Canada Procurement has designed the Supplier Survey below to obtain basic informa",
    "retrieved_date": "2026-11-02",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Pfizer Canada ULC/Pfizer Canada SRI",
    "task_id": "CL-LT-01689"
   },
   {
    "email": "canadaprocurement@pfizer.com",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.pfizer.ca/en/suppliers",
    "quote": "order terms and conditions. If you do not find the information you require on this site, please feel free to contact Canada Procurement at CanadaProcurement@pfizer.com Registration for New Suppliers Pfizer’s Canada Procurement has designed the Supplier Survey below to obtain basic informa",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Pfizer Canada ULC/Pfizer Canada SRI",
    "task_id": "CL-WS-00092"
   }
  ]
 },
 "research_status": {
  "found": 4
 },
 "queries_tried": [
  "site crawl of www.pfizer.ca (12 pages, robots.txt respected), no AI, no search engine",
  "site crawl of www.pfizer.ca (12 pages, robots.txt respected), no AI, no search engine",
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

## The buyer's other Canadian-vendor records (first 60 of 0)
_none_

## The vendor's other buyers in the dataset (first 60 of 0)
_none_

## Open questions for hand research (layer 2)

- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
