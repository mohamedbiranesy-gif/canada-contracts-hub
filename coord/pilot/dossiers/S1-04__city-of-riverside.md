# S1-04 — City of Riverside ⇄ Powerex Corp.

Stratum: **S1_gold_complete_published_PO_rule** · pay on sight: yes · channel tier 1 · AP grade A · missing: —

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: City of Riverside — 3901 Orange Street , Riverside, CA 92501
SUBMIT TO: fleetinvoices@riversideca.gov (invoicing/AP mailbox, confirmed by the referee) | portal (not confirmed as an invoice channel): supplier / vendor portal
REFERENCE: none in the record | PO rule: purchase-order terms published (as published: PURCHASE ORDER AND PURCHASE REQUIS)
FROM / REMIT TO: POWEREX CORP. (as registered: Canada's Business Registries, BC BC0356343, 2026-11-08) — P.O. Box 8910, Vancouver, B.C., V6B 4X3 | GST/HST 123030231 (Canada's Business Registries, BC BC0356343, 2026-11-08)RT0001 (account derived from the BN9)
TAX: Tax Exempt? N Tax Exempt ID: ni¢natrh via Print Contract ID RIVCO-40523-001-05/21 Page 1 of 1 Contract Dates C (as printed on https://aquarius.riversideca.gov/c | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: 45 days after receipt (as printed on https://aquarius.riversideca.gov/clerkdb/DocView.aspx?id=197747
DESCRIPTION: RVS-WSPP-ENERGY
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 90
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 1
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: City of Riverside (municipality / local government, jurisdiction not stated) — public contract / purchase award in the last 12 months (dated record): Powerex Corp. | subject: RVS-WSPP-ENERGY | all identifiers: {"ferc_tariff_reference": "tariff_id:68, filing_id:557, record_id:1, option_code:A"} | awarded 2026-06-30 | published by: contact_address/contact_country_name (FERC EQR seller identity, 2026q2) | record: https://s3.us-west-2.amazonaws.com/pudl.catalyst.coop/ferceqr/core_ferceqr__contracts/2026q2.parquet | vendor in Canada because: contact_address/contact_country_name (FERC EQR seller identity, 2026q2)=1300-666 Burrard Street, Vancouver, BC V6C2X8, CA | status rule: likely active (record dated in the last 12 months: contact_address/contact_country_name (FERC EQR seller identity, 2026q2))
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: lead:38248c5359ce9c78
- **tier**: B
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: contact_address/contact_country_name (FERC EQR seller identity, 2026q2); 0 in the contract dataset)

## Buyer
- **buyer**: City of Riverside
- **buyer_website**: https://riversideca.gov/
- **buyer_address**: 3901 Orange Street , Riverside, CA 92501
- **buyer_contact_evidence_url**: https://www.riversideca.gov/utilities/residents/contact-us
- **buyer_legal_name_as_published**: City of Riverside
- **buyer_logo_url**: https://riversideca.gov/images/corweb-homepage/cor-logo.jpg
- **buyer_website_status**: site answers
- **buyer_type**: municipality / local government
- **buyer_sector**: government: municipal
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q49243; city of California; big city; charter city; county seat
- **buyer_founded**: 1870-00-00 (Wikidata Q49243, official website on the organisation's domain (https://www.riversideca.gov/) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.riversideca.gov/utilities/residents/contact-us (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); AP contact name: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_payment_method_preference**: Payments shall be remitted via wire transfer in compliance with the wire ~ansfer instructions provided on each invo (as printed on https://aquarius.riversideca.gov/clerkdb/DocView.aspx?id=34911&dbid=0&repo=Clerk, re-read 2026-11-08)
- **buyer_tax_exempt_status**: Tax Exempt? N Tax Exempt ID: ni¢natrh via Print Contract ID RIVCO-40523-001-05/21 Page 1 of 1 Contract Dates C (as printed on https://aquarius.riversideca.gov/clerkdb/DocView.aspx?id=310726&dbid=0, re-read 2026-11-08)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **buyer_esignature_preference**: Electronic Signatures and DocumentTransmission (as printed on https://aquarius.riversideca.gov/clerkdb/DocView.aspx?id=325594&dbid=0&repo=Clerk, re-read 2026-11-08)
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: fleetinvoices@riversideca.gov
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://riversideca.gov/bids/docs/7487/_Bid%207487-%20Fuel%20for%20City%20Vehicles%202017.pdf
- **email_evidence_quote**: delivery copy, - The total amount due. - The final invoice must be emailed not later than 24 hrs after delivery. Invoices to be emailed to fleetinvoices@riversideca.gov * Invoices must have fuel prices based on the OPIS Unbranded Rack Average, from the Colton, Ca. fuel Terminal. Fuel pric
- **mailbox_provenance**: fleetinvoices@riversideca.gov (invoicing/AP) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08 | page: https://riversideca.gov/bids/docs/7487/_Bid%207487-%20Fuel%20for%20City%20Vehicles%202017.pdf | quote: "delivery copy, - The total amount due. - The final invoice must be emailed not later than 24 hrs after delivery. Invoices to be emailed to fleetinvoices@riversi" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); DNS lookup failed; mail handled by Proofpoint | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00117
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); DNS lookup failed; mail handled by Proofpoint
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none; rua=mailto:990f98b47fa045a2bc64fae4d42ba350@dmarc-reports.cloudflare.net,mailto:dmarc@riversideca.gov; ruf=mailto:dmarc@riversideca.gov; ri=84600;
- **dmarc_record_domain**: riversideca.gov
- **spf_policy**: DNS lookup failed
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_contact_name_as_published**: Real Property (approved by the Manager) (as printed by the organisation on its own accounts-payable page (as printed on https://aquarius.riversideca.gov/clerkdb/DocView.aspx?dbid=0&id=250670&page=1, re-read 2026-11-08))
- **payment_terms_as_published**: 45 days after receipt (as printed on https://aquarius.riversideca.gov/clerkdb/DocView.aspx?id=197747&dbid=0&repo=Clerk, re-read 2026-11-08)
- **po_required_as_published**: purchase-order terms published (as published: PURCHASE ORDER AND PURCHASE REQUIS) (as printed on https://aquarius.riversideca.gov/clerkdb/DocView.aspx?dbid=0&id=250670&page=1, re-read 2026-11-08)
- **invoice_portal_url**: supplier / vendor portal
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "payment_terms": "45 days after receipt (as printed on https://aquarius.riversideca.gov/clerkdb/DocView.aspx?id=197747&dbid=0&repo=Clerk, re-read 2026-11-08)", "po_required": "purchase-order terms published (as published: PURCHASE ORDER AND PURCHASE REQUIS) (as printed on https://aquarius.riversideca.gov/clerkdb/DocView.aspx?dbid=0&id=250670&page=1, re-read 2026-11-08)", "portal_url": "supplier / vendor portal", "portal_kind": "actionable supplier / invoice portal named by the buyer"}
- **invoice_currency_derived**: USD (derived from the buyer's country; CAD if the parties agreed so)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: City of Riverside — 3901 Orange Street , Riverside, CA 92501 ⏎ SUBMIT TO: fleetinvoices@riversideca.gov (invoicing/AP mailbox, confirmed by the referee) | portal (not confirmed as an invoice channel): supplier / vendor portal ⏎ REFERENCE: none in the record | PO rule: purchase-order terms published (as published: PURCHASE ORDER AND PURCHASE REQUIS) ⏎ FROM / REMIT TO: POWEREX CORP. (as registered: Canada's Business Registries, BC BC0356343, 2026-11-08) — P.O. Box 8910, Vancouver, B.C., V6B 4X3 | GST/HST 123030231 (Canada's Business Registries, BC BC0356343, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: Tax Exempt? N Tax Exempt ID: ni¢natrh via Print Contract ID RIVCO-40523-001-05/21 Page 1 of 1 Contract Dates C (as printed on https://aquarius.riversideca.gov/c | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: 45 days after receipt (as printed on https://aquarius.riversideca.gov/clerkdb/DocView.aspx?id=197747 ⏎ DESCRIPTION: RVS-WSPP-ENERGY
- **invoice_card_json**: {"bill_to": {"legal_name": "City of Riverside", "legal_name_is_published": true, "address": "3901 Orange Street , Riverside, CA 92501", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "fleetinvoices@riversideca.gov", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "supplier / vendor portal", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "portal (not confirmed as an invoice channel)"}, "references_required": {"po_required": "purchase-order terms published (as published: PURCHASE ORDER AND PURCHASE REQUIS) (as printed on https://aquarius.riversideca.gov/clerkdb/DocView.aspx?dbid=0&id=250670&page=1, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes purchase-order terms, so the PO number is the reference to quote (purchase-order terms published (as published: PURCHASE ORDER AND PURCHASE REQUIS) (as printed on https://aquarius.riversideca.gov/clerkdb/DocView.aspx?dbid=0&id=250670&page=1, re-read 2026-11-08))"}, "terms": {"payment_terms": "45 days after receipt (as printed on https://aquarius.riversideca.gov/clerkdb/DocView.aspx?id=197747&dbid=0&repo=Clerk, re-read 2026-11-08)", "payment_method": "Payments shall be remitted via w
- **invoice_readiness**: 10/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id)
- **ap_grade**: A
- **ap_score**: 87
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; AP phone or AP contact; payment cycle or method published (plausibility) | missing: finance mailbox; invoice format / requirements published | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: the buyer's purchase-order number: the buyer publishes purchase-order terms, so the PO number is the reference to quote (purchase-order terms published (as published: PURCHASE ORDER AND PURCHASE REQUIS) (as printed on https://aquarius.riversideca.gov/clerkdb/DocView.aspx?dbid=0&id=250670&page=1, re-read 2026-11-08))

## Vendor
- **vendor**: Powerex Corp.
- **vendor_legal_name**: POWEREX CORP. (as registered: Canada's Business Registries, BC BC0356343, 2026-11-08)
- **vendor_registry_id**: BC0356343 (BC)
- **vendor_registry_url**: https://ised-isde.canada.ca/cbr-rec/en/search?q=Powerex%20Corp.
- **vendor_registered_address**: Vancouver, BC (registered office city / province; Canada's Business Registries, BC BC0356343, 2026-11-08)
- **vendor_legal_form**: BC Company (Canada's Business Registries, BC BC0356343, 2026-11-08)
- **vendor_address**: P.O. Box 8910, Vancouver, B.C., V6B 4X3
- **vendor_country_basis**: contact_address/contact_country_name (FERC EQR seller identity, 2026q2)=1300-666 Burrard Street, Vancouver, BC V6C2X8, CA
- **vendor_bn9**: 123030231 (Canada's Business Registries, BC BC0356343, 2026-11-08)
- **vendor_gst_hst_derived**: 123030231RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://www.bchydro.com/
- **vendor_phone**: 1 800 224 9376
- **vendor_contact_evidence_url**: https://www.bchydro.com/toolbar/contact.html
- **vendor_logo_url**: https://www.bchydro.com/content/experience-fragments/bchydro-web/header/master/_jcr_content/root/container/container/image.coreimg.svg/1723787760686/logo-bchydro.svg
- **vendor_website_basis**: found by a web search, confirmed by reading the site on 2026-11-08: https://www.bchydro.com/about/who_we_are/subsidiaries.html (volved in other activities that are more diversified and international in nature. Our subsidiaries reflect this diversity. Powerex Powerex Corp , a wholly owned)
- **vendor_facts_provenance**: name and address: the record's vendor block (contact_address/contact_country_name (FERC EQR seller identity, 2026q2)); registry identity: BC0356343 (BC) status Active (Canada's Business Registries, BC BC0356343, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: registry: Canada's Business Registries, BC BC0356343, 2026-11-08; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 1988-12-13; phone / role e-mails / logo: the vendor's own site, https://www.bchydro.com/toolbar/contact.html (tools/org_contacts.py, org_extras.py); website: https://www.bchydro.com/
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Active (Canada's Business Registries, BC BC0356343, 2026-11-08)
- **vendor_incorporation_date**: 1988-12-13
- **vendor_years_in_business**: 37.9 (since 1988-12-13, registry date)
- **vendor_bn_source**: registry: Canada's Business Registries, BC BC0356343, 2026-11-08

## Contract
- **po_required_as_published**: purchase-order terms published (as published: PURCHASE ORDER AND PURCHASE REQUIS) (as printed on https://aquarius.riversideca.gov/clerkdb/DocView.aspx?dbid=0&id=250670&page=1, re-read 2026-11-08)
- **contract_status**: likely active (record dated in the last 12 months: contact_address/contact_country_name (FERC EQR seller identity, 2026q2))
- **contract_reference**: {"ferc_tariff_reference": "tariff_id:68, filing_id:557, record_id:1, option_code:A"}
- **contract_title**: RVS-WSPP-ENERGY
- **contract_description**: RVS-WSPP-ENERGY (the record's title; the source publishes no separate description)
- **award_date**: 2026-06-30
- **contract_link**: https://s3.us-west-2.amazonaws.com/pudl.catalyst.coop/ferceqr/core_ferceqr__contracts/2026q2.parquet
- **source**: contact_address/contact_country_name (FERC EQR seller identity, 2026q2)
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: contact_address/contact_country_name (FERC EQR seller identity, 2026q2); 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **invoice_currency_derived**: USD (derived from the buyer's country; CAD if the parties agreed so)
- **vendor_gst_hst_derived**: 123030231RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: yes
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: City of Riverside — 3901 Orange Street , Riverside, CA 92501 ⏎ SUBMIT TO: fleetinvoices@riversideca.gov (invoicing/AP mailbox, confirmed by the referee) | portal (not confirmed as an invoice channel): supplier / vendor portal ⏎ REFERENCE: none in the record | PO rule: purchase-order terms published (as published: PURCHASE ORDER AND PURCHASE REQUIS) ⏎ FROM / REMIT TO: POWEREX CORP. (as registered: Canada's Business Registries, BC BC0356343, 2026-11-08) — P.O. Box 8910, Vancouver, B.C., V6B 4X3 | GST/HST 123030231 (Canada's Business Registries, BC BC0356343, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: Tax Exempt? N Tax Exempt ID: ni¢natrh via Print Contract ID RIVCO-40523-001-05/21 Page 1 of 1 Contract Dates C (as printed on https://aquarius.riversideca.gov/c | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: 45 days after receipt (as printed on https://aquarius.riversideca.gov/clerkdb/DocView.aspx?id=197747 ⏎ DESCRIPTION: RVS-WSPP-ENERGY
- **invoice_card_json**: {"bill_to": {"legal_name": "City of Riverside", "legal_name_is_published": true, "address": "3901 Orange Street , Riverside, CA 92501", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "fleetinvoices@riversideca.gov", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "supplier / vendor portal", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "portal (not confirmed as an invoice channel)"}, "references_required": {"po_required": "purchase-order terms published (as published: PURCHASE ORDER AND PURCHASE REQUIS) (as printed on https://aquarius.riversideca.gov/clerkdb/DocView.aspx?dbid=0&id=250670&page=1, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes purchase-order terms, so the PO number is the reference to quote (purchase-order terms published (as published: PURCHASE ORDER AND PURCHASE REQUIS) (as printed on https://aquarius.riversideca.gov/clerkdb/DocView.aspx?dbid=0&id=250670&page=1, re-read 2026-11-08))"}, "terms": {"payment_terms": "45 days after receipt (as printed on https://aquarius.riversideca.gov/clerkdb/DocView.aspx?id=197747&dbid=0&repo=Clerk, re-read 2026-11-08)", "payment_method": "Payments shall be remitted via w
- **invoice_readiness**: 10/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id)
- **ap_grade**: A
- **ap_score**: 87
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; AP phone or AP contact; payment cycle or method published (plausibility) | missing: finance mailbox; invoice format / requirements published | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **facts_provenance_json**: {"mailbox": ["fleetinvoices@riversideca.gov (invoicing/AP)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08", "page: https://riversideca.gov/bids/docs/7487/_Bid%207487-%20Fuel%20for%20City%20Vehicles%202017.pdf", "quote: \"delivery copy, - The total amount due. - The final invoice must be emailed not later than 24 hrs after delivery. Invoices to be emailed to fleetinvoices@riversi\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); DNS lookup failed; mail handled by Proofpoint", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00117"], "buyer_facts": ["address and phone: the buyer's own site, https://www.riversideca.gov/utilities/residents/contact-us (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date i

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://riversideca.gov/finance/PDF/City%20of%20Riverside%20Vendor%20Webinar%201.22.26.pdf | 2026-11-08 | ok |  |  | supplier / vendor portal | 951-826-5279 |  |  |  |  |  |

## Buyer site facts (org_extras, riversideca.gov)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: City of Riverside
- **legal_name_url**: https://riversideca.gov/
- **legal_name_quote**: .gov Engage Riverside Shop Riverside Public Utilities Search RiversideCA.gov Search riversideca.gov City of Riverside Residents: Bain Fire Evacuation Updates --> Community Calendar | Government Meetings About Riversid
- **logo_url**: https://riversideca.gov/images/corweb-homepage/cor-logo.jpg
- **logo_basis**: logo image in the site header
- **domain**: riversideca.gov
- **key**: lead:38248c5359ce9c78
- **name**: City of Riverside
- **website**: https://riversideca.gov/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: City of Riverside
- **legal_name_stated_url**: https://riversideca.gov/about-riverside
- **legal_name_stated_quote**: .gov Engage Riverside Shop Riverside Public Utilities Search RiversideCA.gov Search riversideca.gov City of Riverside Residents: Bain Fire Evacuation Updates --> Community Calendar | Government Meetings About Riversid

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "3901 Orange Street , Riverside, CA 92501", "address_country": "US", "address_url": "https://www.riversideca.gov/utilities/residents/contact-us", "address_method": "pattern", "address_quote": "to help with all your water & electric needs. Downtown Customer Service Center 3901 Orange Street Riverside, CA 92501 Walk-In Hours Monday - Friday 9am to 5pm Saturday - CLOSED S", "domain": "riversideca.gov", "key": "lead:38248c5359ce9c78", "name": "City of Riverside", "website": "https://riversideca.gov/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, bchydro.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://www.bchydro.com/content/experience-fragments/bchydro-web/header/master/_jcr_content/root/container/container/image.coreimg.svg/1723787760686/logo-bchydro.svg
- **logo_basis**: logo image in the site header
- **domain**: bchydro.com
- **key**: lead:91f9dd8f8d8b6802
- **name**: BC Hydro and Power Authority
- **website**: https://bchydro.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: B.C. Utilities Commission
- **legal_name_stated_url**: https://www.bchydro.com/toolbar/about.html
- **legal_name_stated_quote**: cture, conserve, supply, acquire, and dispose of power and related products Regulatory power to the B.C. Utilities Commission (BCUC), to ensure our customers receive safe, reliable and non-discriminatory energy services at fa
- **linkedin_url**: https://ca.linkedin.com/company/bchydro
- **tel_links**: 18002249376; 1 800 224 9376

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "P.O. Box 8910, Vancouver, B.C., V6B 4X3", "address_country": "CA", "address_url": "https://www.bchydro.com/toolbar/contact.html", "address_method": "pattern", "address_quote": "even to eight business days. Mail Mailing address P.O. Box 8910 Vancouver, B.C. V6B 4X3 Corporate head office 333 Dunsmuir St. Vancouver, B.C. V6B 5R3 Corporate inform", "phone": "1 800 224 9376", "phone_url": "https://www.bchydro.com/toolbar/contact.html", "domain": "bchydro.com", "key": "lead:304f77e20b959d3b", "name": "bchydro.com", "website": "https://bchydro.com/", "kind": "buyer", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | City of Riverside | Q49243 | official website on the organisation's domain (https://www.riversideca.gov/) + name |  | Riverside | Riverside | city of California; big city; charter city; county seat |  | United States | 1870-00-00 |  |
| b | BC Hydro and Power Authority | Q795720 | official website on the organisation's domain (https://www.bchydro.com/) + name |  | B.C. Hydro | BC Hydro | state-owned enterprise | Crown corporation | Canada | 1961-01-01 | Vancouver |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:38248c5359ce9c78",
 "ap_contact_team": {
  "emails": [
   "fleetinvoices@riversideca.gov",
   "vendors@riversideca.gov"
  ],
  "invoice_portal": null,
  "phone": "(951) 826-5548",
  "mailing_address": null,
  "invoicing_requirements": "City vendor EFT application publishes AP supervisor phone (951) 826-5548. Suppliers may enroll in EFT. The application lists the AP office mailing address for the form.",
  "evidence": [
   {
    "email": "fleetinvoices@riversideca.gov",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://riversideca.gov/bids/docs/7487/_Bid%207487-%20Fuel%20for%20City%20Vehicles%202017.pdf",
    "quote": "delivery copy, - The total amount due. - The final invoice must be emailed not later than 24 hrs after delivery. Invoices to be emailed to fleetinvoices@riversideca.gov * Invoices must have fuel prices based on the OPIS Unbranded Rack Average, from the Colton, Ca. fuel Terminal. Fuel pric",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "City of Riverside",
    "task_id": "CL-WS-00117"
   },
   {
    "email": "vendors@riversideca.gov",
    "type": "procurement",
    "invoice_portal": null,
    "phone": "(951) 826-5548",
    "mailing_address": null,
    "requirements": "City vendor EFT application publishes AP supervisor phone (951) 826-5548. Suppliers may enroll in EFT. The application lists the AP office mailing address for the form.",
    "applies_to": "whole_organisation",
    "page_url": "https://www.riversideca.gov/finance/PDF/City%20of%20Riverside%20Vendor%20Webinar%201.22.26.pdf",
    "quote": "For questions related to Vendor Registration, reach out to vendors@riversideca.gov",
    "retrieved_date": "2026-11-08",
    "found_by": "chatgpt",
    "verification": "verified",
    "source_file": "chatgpt_buyer_ap_results_batch50.csv",
    "org": "City of Riverside",
    "task_id": "CH-AP-50089"
   },
   {
    "email": "vendors@riversideca.gov",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://riversideca.gov/finance/PDF/City%20of%20Riverside%20Vendor%20Webinar%201.22.26.pdf",
    "quote": "• For questions related to Vendor Registration, reach out to vendors@riversideca.gov • For questions related to Insurance, reach out to riskmanagement@riversideca.gov or 951-826-5279 • For questions related to B",
    "retrieved_date": "2026-11-02",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "City of Riverside",
    "task_id": "CL-SN-00945"
   }
  ]
 },
 "research_status": {
  "found": 3
 },
 "queries_tried": [
  "site:riversideca.gov accounts payable invoice vendor City Riverside | \"City of Riverside\" accounts payable \"riversideca.gov\" vendor invoice payment | site:riversideca.gov \"accounts payable\" \"@riversideca.gov\" EFT vendor",
  "site crawl of riversideca.gov (60 pages, robots.txt respected), no AI, no search engine",
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

Read 2026-11-09 (Claude, integrator lane). Budget rule (PLAN §4d): layer 1 already carries this buyer's confirmed channel, PO rule and terms with quotes; the notes below add only what changes how the invoice is built.

**Nature of the contract changes the channel.** Powerex Corp. (BC Hydro's trading subsidiary) sells wholesale electricity / capacity to Riverside Public
Utilities; such sales are invoiced under the WSPP Agreement / the parties' confirmation, with netting and payment on the 20th of the month following
delivery (WSPP Agreement s. 9 — inference from the contract type, not from a Riverside page; confirm the confirmation sheet). The City's AP terms in the
row ("45 days after receipt", PO terms published) govern ordinary vendor invoices; for power purchases the trading confirmation prevails. Bill to
"City of Riverside, Riverside Public Utilities" (the utility is a city department, not a separate legal entity). USD; no Canadian GST (export).
