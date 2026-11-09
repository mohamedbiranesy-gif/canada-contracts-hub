# S5-29 — Bruce Power L.P. ⇄ Nuclear Promise X (NPX)

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 1 · AP grade C · missing: the vendor's GST/HST number (BN9)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Bruce Power L.P. — 177 Tie Rd., R.R. 2, Tiverton ON, N0G 2T0 — buyer tax no. 870513959RT0001 (GST/HST number as printed on https://www.brucepower.com/wp-content/uploads/2020/01/Amended-and-Restated-Bruce-Power-Sharing-in-Transfers-and-Refinancings-Agreement.pdf: "on behalf of the Government of Ontario. (g) The Counterparty is registered for HST purposes under the ETA and its HST registration number is 870513959RT-0002. (")
SUBMIT TO: invoicesubmissions@brucepower.com (invoicing/AP mailbox, confirmed by the referee) | invoice portal: https://service.ariba.com/Supplier.aw/109525046/aw?awh=r&awssk=prDqvXAF&dard=1 — SAP Ariba
REFERENCE: tender 2026-03-19 (as printed in the buyer's own council / committee report or minutes: https://www.brucepower.com/2026/03/19/bruce-power-retains-npx-and-makwa-development-as-project-management-partner-to-support-the-early-phase-of-the-bruce-c-project/, read 2026-11-08: "wer retains NPX and Makwa Development as Project Management Partner to support the early phase of the Bruce C Project 2026-03-19 Bruce Power has retained Nuclear Promise X (NPX) as its Project Managem") | PO rule: yes (as published: must contain: A valid Purchase Order Number)
FROM / REMIT TO: Nuclear Promise X (NPX) — Port Elgin, ON | GST/HST number not public
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the p
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 90
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 1
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Bruce Power L.P. (utility / public corporation, CA) — public contract / purchase award in the last 12 months (dated record): Nuclear Promise X (NPX) | subject: Bruce Power signs multi-year agreement with NPX to drive innovation and growth | instrument: master services agreement (renewal) | solicitation: 2026-03-19 (as printed in the buyer's own council / committee report or minutes: https://www.brucepower.com/2026/03/19/b | all identifiers: {"record_id": "private_press:2481db493a50ab4c18a2750a5c07d816d870d0f8"} | value: 50000000 CAD | awarded 2025-12-02, start 2025-12-02 | published by: Cision newswire.ca (CNW Group) press releases | record: https://www.newswire.ca/news-releases/bruce-power-signs-multi-year-agreement-with-npx-to-drive-innovation-and-growth-858964255.html | vendor in Canada because: About section: Canadian consulting company; release datelined Port Elgin, ON | status rule: likely active (source marks it as continuing; awarded in the last 3 years, no end date published) | this buyer has 1 records with Canada-located vendors (1 distinct vendors; 1 in the last 12 months; latest 2025-12-02)
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: b:e433cfd3cd007432
- **tier**: B
- **grade**: 4
- **records_with_this_vendor**: 1

## Buyer
- **buyer**: Bruce Power L.P.
- **buyer_website**: https://brucepower.com
- **buyer_address**: 177 Tie Rd., R.R. 2, Tiverton ON, N0G 2T0
- **buyer_phone**: 519 361 2673
- **buyer_contact_evidence_url**: https://www.brucepower.com/contact/
- **buyer_bn_as_published**: 870513959RT0001 (GST/HST number as printed on https://www.brucepower.com/wp-content/uploads/2020/01/Amended-and-Restated-Bruce-Power-Sharing-in-Transfers-and-Refinancings-Agreement.pdf: "on behalf of the Government of Ontario. (g) The Counterparty is registered for HST purposes under the ETA and its HST registration number is 870513959RT-0002. (")
- **buyer_bn_program**: RT (GST/HST program account)
- **buyer_gst_hst_derived**: 870513959RT0001 (printed by the buyer itself; not derived)
- **buyer_logo_url**: https://s32829.pcdn.co/wp-content/uploads/2019/11/BrucePower.png
- **buyer_bn_note**: the federal grants & contributions disclosure lists recipient_business_number 867193245 for "BRUCE POWER L.P." (1 agreement(s)); kept the BN above, which comes from the CRA charities list or the buyer's own page
- **buyer_type**: utility / public corporation
- **buyer_sector**: utility
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.brucepower.com/contact/ (tools/org_contacts.py: JSON-LD / contact page; no AI); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); AP contact name: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: invoicesubmissions@brucepower.com
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.brucepower.com/supplier-covid-19-communication/
- **email_evidence_quote**: or InvoiceSubmissions@brucepower.com All inquiries regarding your account and payment information are to be sent to: BNPDAcctsPayableInquiriesOnly@brucep
- **mailbox_provenance**: invoicesubmissions@brucepower.com (invoicing/AP) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08 | page: https://www.brucepower.com/supplier-covid-19-communication/ | quote: "or InvoiceSubmissions@brucepower.com All inquiries regarding your account and payment information are to be sent to: BNPDAcctsPayableInquiriesOnly@brucep" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00345
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1; p=quarantine; rua=mailto:mailfail@brucepower.com; ruf=mailto:securitymailfail@brucepower.com; sp=quarantine; fo=d:s; ri=86400; adkim=r; aspf=s
- **dmarc_record_domain**: brucepower.com
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 mx a ip4:216.183.143.65/32 ip4:142.6.255.65/32 ip4:37.0.1.160/32 ip4:37.0.3.160/32 include:spf.protection.outlook.com include:_spf.salesforce.com include:servers.mcsv.net include:sendgrid.net -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_contact_name_as_published**: Richard Miller Manager (apso Director) (as printed by the organisation on its own accounts-payable page (as printed on https://www.brucepower.com/wp-content/uploads/2022/08/INPO-14-005-Principles-for-Excellence-in-Nuclear-Supplier-Performance.pdf, re-read 2026-11-08))
- **payment_terms_as_published**: 30 days of receipt (as printed on https://www.brucepower.com/wp-content/uploads/2021/03/BP-5-11-Standard-Terms-and-Conditions-for-Purchase-of-Goods-rev.-14.pdf, re-read 2026-11-08)
- **po_required_as_published**: yes (as published: must contain: A valid Purchase Order Number) (as printed on https://www.brucepower.com/become-a-supplier/accounts-payable/, re-read 2026-11-08)
- **invoice_portal_url**: https://service.ariba.com/Supplier.aw/109525046/aw?awh=r&awssk=prDqvXAF&dard=1 — SAP Ariba
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **ap_system_hint**: named on the buyer's page: SAP Ariba, ariba
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "payment_terms": "30 days of receipt (as printed on https://www.brucepower.com/wp-content/uploads/2021/03/BP-5-11-Standard-Terms-and-Conditions-for-Purchase-of-Goods-rev.-14.pdf, re-read 2026-11-08)", "po_required": "yes (as published: must contain: A valid Purchase Order Number) (as printed on https://www.brucepower.com/become-a-supplier/accounts-payable/, re-read 2026-11-08)", "portal_url": "https://service.ariba.com/Supplier.aw/109525046/aw?awh=r&awssk=prDqvXAF&dard=1 — SAP Ariba", "portal_kind": "actionable supplier / invoice portal named by the buyer"}
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Bruce Power L.P. — 177 Tie Rd., R.R. 2, Tiverton ON, N0G 2T0 — buyer tax no. 870513959RT0001 (GST/HST number as printed on https://www.brucepower.com/wp-content/uploads/2020/01/Amended-and-Restated-Bruce-Power-Sharing-in-Transfers-and-Refinancings-Agreement.pdf: "on behalf of the Government of Ontario. (g) The Counterparty is registered for HST purposes under the ETA and its HST registration number is 870513959RT-0002. (") ⏎ SUBMIT TO: invoicesubmissions@brucepower.com (invoicing/AP mailbox, confirmed by the referee) | invoice portal: https://service.ariba.com/Supplier.aw/109525046/aw?awh=r&awssk=prDqvXAF&dard=1 — SAP Ariba ⏎ REFERENCE: tender 2026-03-19 (as printed in the buyer's own council / committee report or minutes: https://www.brucepower.com/2026/03/19/bruce-power-retains-npx-and-makwa-development-as-project-management-partner-to-support-the-early-phase-of-the-bruce-c-project/, read 2026-11-08: "wer retains NPX and Makwa Development as Project Management Partner to support the early phase of the Bruce C Project 2026-03-19 Bruce Power has retained Nuclear Promise X (NPX) as its Project Managem") | PO rule: yes (as published: must contain: A valid Purchase Order Number) ⏎ FROM / REMIT TO: Nuclear Promise X (NPX) — Port Elgin, ON | GST/HST number not public ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HS
- **invoice_card_json**: {"bill_to": {"legal_name": "Bruce Power L.P.", "legal_name_is_published": false, "address": "177 Tie Rd., R.R. 2, Tiverton ON, N0G 2T0", "address_is_the_invoice_address": false, "tax_number": "870513959RT0001 (GST/HST number as printed on https://www.brucepower.com/wp-content/uploads/2020/01/Amended-and-Restated-Bruce-Power-Sharing-in-Transfers-and-Refinancings-Agreement.pdf: \"on behalf of the Government of Ontario. (g) The Counterparty is registered for HST purposes under the ETA and its HST registration number is 870513959RT-0002. (\")", "language": "en"}, "submit_to": {"email": "invoicesubmissions@brucepower.com", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "https://service.ariba.com/Supplier.aw/109525046/aw?awh=r&awssk=prDqvXAF&dard=1 — SAP Ariba", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: SAP Ariba, ariba", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "yes (as published: must contain: A valid Purchase Order Number) (as printed on https://www.brucepower.com/become-a-supplier/accounts-payable/, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: must contain: A valid Pur
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: bill-to legal name (published); reference to quote (PO / contract / vendor id); vendor GST/HST number; vendor legal name
- **ap_grade**: C
- **ap_score**: 75
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); invoice or billing address; PO rule published; payment terms published; currency known; AP phone or AP contact | missing: finance mailbox; bill-to legal name published; invoice format / requirements published; payment cycle or method published (plausibility) | penalties: BN conflict between sources
- **ap_gap_to_A**: published bill-to legal name; clear the penalty: BN conflict between sources
- **ap_payability**: not yet payable — missing: bill-to legal name and address
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: must contain: A valid Purchase Order Number) (as printed on https://www.brucepower.com/become-a-supplier/accounts-payable/, re-read 2026-11-08))

## Vendor
- **vendor**: Nuclear Promise X (NPX)
- **vendor_address**: Port Elgin, ON
- **vendor_country_basis**: About section: Canadian consulting company; release datelined Port Elgin, ON
- **vendor_website**: https://ccib.ca/
- **vendor_emails**: info@ccib.ca
- **vendor_phone**: 416-961-8663
- **vendor_contact_evidence_url**: https://www.ccib.ca/contact/
- **vendor_logo_url**: https://www.ccib.ca/wp-content/themes/ccab/images/CCIB-logoH-colour_400.png
- **vendor_website_basis**: found by a web search, confirmed by reading the site on 2026-11-08: https://www.ccib.ca/main/member/nuclear-promise-x/ (Nuclear Promise X - CCIB About About Building bridges between Indigenous businesses and corporate Canada CCIB Team Meet and learn more about CCIB’s staff Govern)
- **vendor_facts_provenance**: name and address: the record's vendor block (Cision newswire.ca (CNW Group) press releases); phone / role e-mails / logo: the vendor's own site, https://www.ccib.ca/contact/ (tools/org_contacts.py, org_extras.py); website: https://ccib.ca/
- **vendor_concentration_top_share**: Nuclear Promise X (NPX): 100% of 1 records
- **vendor_registry_match_level**: no_match

## Contract
- **po_required_as_published**: yes (as published: must contain: A valid Purchase Order Number) (as printed on https://www.brucepower.com/become-a-supplier/accounts-payable/, re-read 2026-11-08)
- **contract_status**: likely active (source marks it as continuing; awarded in the last 3 years, no end date published)
- **contract_reference**: {"record_id": "private_press:2481db493a50ab4c18a2750a5c07d816d870d0f8"}
- **contract_title**: Bruce Power signs multi-year agreement with NPX to drive innovation and growth
- **contract_description**: Renewed Master Services Agreement for innovation, AI, projects and new-nuclear advancement support at the Bruce site; five-year extension valued at more than $50 million with option for further extensions
- **solicitation_or_tender_number**: 2026-03-19 (as printed in the buyer's own council / committee report or minutes: https://www.brucepower.com/2026/03/19/bruce-power-retains-npx-and-makwa-development-as-project-management-partner-to-support-the-early-phase-of-the-bruce-c-project/, read 2026-11-08: "wer retains NPX and Makwa Development as Project Management Partner to support the early phase of the Bruce C Project 2026-03-19 Bruce Power has retained Nuclear Promise X (NPX) as its Project Managem")
- **contract_value**: 50000000
- **currency**: CAD
- **award_date**: 2025-12-02
- **start_date**: 2025-12-02
- **contract_link**: https://www.newswire.ca/news-releases/bruce-power-signs-multi-year-agreement-with-npx-to-drive-innovation-and-growth-858964255.html
- **source**: Cision newswire.ca (CNW Group) press releases
- **contracts_with_canadian_suppliers**: 1
- **records_last_12_months**: 1
- **record_sources**: Cision newswire.ca (CNW Group) press releases (1)
- **records_with_this_vendor**: 1
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 870513959RT0001 (printed by the buyer itself; not derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: HST 13% (Ontario) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Bruce Power L.P. — 177 Tie Rd., R.R. 2, Tiverton ON, N0G 2T0 — buyer tax no. 870513959RT0001 (GST/HST number as printed on https://www.brucepower.com/wp-content/uploads/2020/01/Amended-and-Restated-Bruce-Power-Sharing-in-Transfers-and-Refinancings-Agreement.pdf: "on behalf of the Government of Ontario. (g) The Counterparty is registered for HST purposes under the ETA and its HST registration number is 870513959RT-0002. (") ⏎ SUBMIT TO: invoicesubmissions@brucepower.com (invoicing/AP mailbox, confirmed by the referee) | invoice portal: https://service.ariba.com/Supplier.aw/109525046/aw?awh=r&awssk=prDqvXAF&dard=1 — SAP Ariba ⏎ REFERENCE: tender 2026-03-19 (as printed in the buyer's own council / committee report or minutes: https://www.brucepower.com/2026/03/19/bruce-power-retains-npx-and-makwa-development-as-project-management-partner-to-support-the-early-phase-of-the-bruce-c-project/, read 2026-11-08: "wer retains NPX and Makwa Development as Project Management Partner to support the early phase of the Bruce C Project 2026-03-19 Bruce Power has retained Nuclear Promise X (NPX) as its Project Managem") | PO rule: yes (as published: must contain: A valid Purchase Order Number) ⏎ FROM / REMIT TO: Nuclear Promise X (NPX) — Port Elgin, ON | GST/HST number not public ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HS
- **invoice_card_json**: {"bill_to": {"legal_name": "Bruce Power L.P.", "legal_name_is_published": false, "address": "177 Tie Rd., R.R. 2, Tiverton ON, N0G 2T0", "address_is_the_invoice_address": false, "tax_number": "870513959RT0001 (GST/HST number as printed on https://www.brucepower.com/wp-content/uploads/2020/01/Amended-and-Restated-Bruce-Power-Sharing-in-Transfers-and-Refinancings-Agreement.pdf: \"on behalf of the Government of Ontario. (g) The Counterparty is registered for HST purposes under the ETA and its HST registration number is 870513959RT-0002. (\")", "language": "en"}, "submit_to": {"email": "invoicesubmissions@brucepower.com", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "https://service.ariba.com/Supplier.aw/109525046/aw?awh=r&awssk=prDqvXAF&dard=1 — SAP Ariba", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: SAP Ariba, ariba", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "yes (as published: must contain: A valid Purchase Order Number) (as printed on https://www.brucepower.com/become-a-supplier/accounts-payable/, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: must contain: A valid Pur
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: bill-to legal name (published); reference to quote (PO / contract / vendor id); vendor GST/HST number; vendor legal name
- **ap_grade**: C
- **ap_score**: 75
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); invoice or billing address; PO rule published; payment terms published; currency known; AP phone or AP contact | missing: finance mailbox; bill-to legal name published; invoice format / requirements published; payment cycle or method published (plausibility) | penalties: BN conflict between sources
- **ap_gap_to_A**: published bill-to legal name; clear the penalty: BN conflict between sources
- **ap_payability**: not yet payable — missing: bill-to legal name and address
- **facts_provenance_json**: {"mailbox": ["invoicesubmissions@brucepower.com (invoicing/AP)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08", "page: https://www.brucepower.com/supplier-covid-19-communication/", "quote: \"or InvoiceSubmissions@brucepower.com All inquiries regarding your account and payment information are to be sent to: BNPDAcctsPayableInquiriesOnly@brucep\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00345"], "buyer_facts": ["address and phone: the buyer's own site, https://www.brucepower.com/contact/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "AP contact name: the mailbox's evidence page re-read i

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.brucepower.com/become-a-supplier/accounts-payable/ | 2026-11-08 | ok |  | yes (as published: must contain: A valid Purchase Order Number) | SAP Ariba |  |  |  |  |  | invoices for materials are to be submitted directly to Bruce Power via the SAP Business Network. All Material Invoices must contain: A valid Purchase Order Number Include an Invoice Date and Invoice Number Match the issu |
| https://www.brucepower.com/become-a-supplier/supply-chain-contacts/ | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, brucepower.com)
- **status**: ok
- **pages**: 6
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Bruce Power
- **jsonld_logo**: https://www.brucepower.com/wp-content/uploads/2019/11/BrucePower.png
- **jsonld_url**: https://www.brucepower.com/
- **jsonld_quote**: {"@context":"https:\/\/schema.org","@graph":[{"@type":"WebPage","@id":"https:\/\/www.brucepower.com\/","url":"https:\/\/www.brucepower.com\/","name":"Bruce Power","isPartOf":{"@id":"https:\/\/www.brucepower.com\/#website"},"about":{"@id":"https:\/\/www.brucepower.com\/#organization"},"primaryImageOf
- **jsonld_page**: https://www.brucepower.com/
- **legal_name_stated**: Saugeen Ojibway Nation
- **legal_name_stated_url**: https://www.brucepower.com/about-us/
- **legal_name_stated_quote**: uron near Tiverton, Ontario, within the traditional lands and treaty territory of the people of the Saugeen Ojibway Nation (SON), which includes the Chippewas of Nawash and Saugeen First Nation. Bruce Power is dedicated to
- **linkedin_url**: https://www.linkedin.com/company/bruce-power
- **language**: en
- **logo_url**: https://s32829.pcdn.co/wp-content/uploads/2019/11/BrucePower.png
- **logo_basis**: logo image in the site header
- **domain**: brucepower.com
- **key**: b:656de745c04d2e8f
- **name**: Bruce Power
- **website**: https://brucepower.com/
- **kind**: buyer
- **date**: 2026-11-08

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "177 Tie Rd., R.R. 2, Tiverton ON, N0G 2T0", "address_country": "CA", "address_url": "https://www.brucepower.com/contact/", "address_method": "pattern", "address_quote": "Name Last Name Email Submit ASK US A QUESTION 177 Tie Rd., R.R. 2, Tiverton ON, N0G 2T0 Phone: 519 361 2673 Toll Free: 1 866 748 4787 General inquiries: info@brucepowe", "phone": "519 361 2673", "phone_url": "https://www.brucepower.com/contact/", "emails": "info@brucepower.com", "emails_url": "https://www.brucepower.com/contact/", "domain": "brucepower.com", "key": "b:656de745c04d2e8f", "name": "Bruce Power", "website": "https://brucepower.com/", "kind": "buyer", "date": "2026-11-08"}

## Vendor site facts (org_extras, ccib.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://www.ccib.ca/wp-content/themes/ccab/images/CCIB-logoH-colour_400.png
- **logo_basis**: logo image in the site header
- **domain**: ccib.ca
- **key**: lead:be178031e465c96c
- **name**: ccib.ca
- **website**: https://ccib.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Canadian Council for Indigenous Business
- **jsonld_logo**: https://www.ccib.ca/wp-content/uploads/2024/10/CCIB-Site-Identity-Logo.png
- **jsonld_url**: https://www.ccib.ca/
- **jsonld_same_as**: https://www.facebook.com/CanadianCouncilforAboriginalBusiness/
- **jsonld_quote**: {"@context":"https:\/\/schema.org","@graph":[{"@type":"WebPage","@id":"https:\/\/www.ccib.ca\/","url":"https:\/\/www.ccib.ca\/","name":"Canadian Council for Indigenous Business | CCIB","isPartOf":{"@id":"https:\/\/www.ccib.ca\/#website"},"about":{"@id":"https:\/\/www.ccib.ca\/#organization"},"datePu
- **jsonld_page**: https://www.ccib.ca/
- **legal_name_stated**: Canadian Council for Indigenous Business
- **legal_name_stated_url**: https://www.ccib.ca/about-ccib/
- **legal_name_stated_quote**: About CCIB | Canadian Council for Indigenous Business About About Building bridges between Indigenous businesses and corporate Canada CCIB Team Meet and
- **mentions**: {'payment_method': {'text': 'interactive dashboard enabling businesses, policymakers, and communities to explore Ind', 'url': 'https://www.ccib.ca/', 'quote': 'hrough CCIB’s PAIR program. Read More → CCIB and BDL Launch Indigenous Business Insights Tracker An interactive dashboard enabling businesses, policymakers, and communities to explore Indigenous entrepreneurship data, economic trends, and business impact… Read'}}
- **linkedin_url**: https://www.linkedin.com/company/ccib-national/

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "2 Berkeley Street, Suite 202, Toronto, Ontario M5A 4J5", "address_country": "CA", "address_url": "https://www.ccib.ca/contact/", "address_method": "pattern", "address_quote": "n Council for Indigenous Business 2 Berkeley Street, Suite 202 Toronto, Ontario M5A 4J5 Telephone: 416-961-8663 Fax: 416-961-3995 Membership Related Inquiries: memberr", "phone": "416-961-8663", "phone_url": "https://www.ccib.ca/contact/", "emails": "info@ccib.ca", "emails_url": "https://www.ccib.ca/contact/", "domain": "ccib.ca", "key": "lead:be178031e465c96c", "name": "ccib.ca", "website": "https://ccib.ca/", "kind": "buyer", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Bruce Power | Q991772 | official website on the organisation's domain (http://www.brucepower.com/) + name |  | Bruce Power | Bruce Power | business; enterprise | commandite company | Canada | 2001-00-00 | Tiverton |
| b | Bruce Power L.P. |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "b:e433cfd3cd007432",
 "ap_contact_team": {
  "emails": [
   "invoicereview@brucepower.com",
   "invoicesubmissions@brucepower.com",
   "bnpdacctspayableinvoicesubmissions@brucepower.com",
   "bnpdacctspayableinquiriesonly@brucepower.com",
   "treasury@brucepower.com",
   "BNPDAcctsPayableInquiriesOnly@brucepower.com"
  ],
  "invoice_portal": "https://www.brucepower.com/become-a-supplier/accounts-payable/",
  "phone": "519 361 2673",
  "mailing_address": "177 Tie Rd., R.R. 2, Tiverton, ON N0G 2T0, Canada",
  "invoicing_requirements": "Nuclear power generator; supplier material invoices delivered via SAP Business Network; all inquiries, statements, and AP communications handled via BNPDAcctsPayableInquiriesOnly@brucepower.com.",
  "evidence": [
   {
    "email": "invoicereview@brucepower.com",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.brucepower.com/become-a-supplier/supply-chain-contacts/",
    "quote": "m) Lori Trowbridge (PMC Strategic Projects) Commercial Management Office Rohit Raina (Claims and disputes) Time & material invoice queries: invoicereview@brucepower.com Become a Supplier Working with Bruce Power Supplier Performance Management Policy Accounts Payable Supply Chain Contacts",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Bruce Power L.P.",
    "task_id": "CL-SQ-00685"
   },
   {
    "email": "invoicesubmissions@brucepower.com",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.brucepower.com/supplier-covid-19-communication/",
    "quote": "or InvoiceSubmissions@brucepower.com All inquiries regarding your account and payment information are to be sent to: BNPDAcctsPayableInquiriesOnly@brucep",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Bruce Power L.P.",
    "task_id": "CL-WS-00345"
   },
   {
    "email": "bnpdacctspayableinvoicesubmissions@brucepower.com",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.brucepower.com/supplier-covid-19-communication/",
    "quote": "rucepower.com Invoice Submissions, Inquiries, and Payments All invoices must to be submitted electronically to the following email address: BNPDAcctsPayableInvoiceSubmissions@brucepower.com or",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Bruce Power L.P.",
    "task_id": "CL-WS-00345"
   },
   {
    "email": "bnpdacctspayableinquiriesonly@brucepower.com",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.brucepower.com/become-a-supplier/accounts-payable/",
    "quote": "st be emailed to the Contract Management team. All inquiries, statements and other communications regarding your account are to be sent to: BNPDAcctsPayableInquiriesOnly@brucepower.com Bruce Power’s Accounts Payable Department is located in the B10 Administration Building on Bruce Power’s",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Bruce Power L.P.",
    "task_id": "CL-SQ-00685"
   },
   {
    "email": "treasury@brucepower.com",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.brucepower.com/become-a-supplier/accounts-payable/",
    "quote": "the Supplier with details of each payment. To be setup for electronic payments or to request a change in payment type, please reach out to treasury@brucepower.com for assistance. Financial Accounting Services Contact For Accounts Payable assistance, please email: BNPDacctspayableinquiries",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Bruce Power L.P.",
    "task_id": "CL-SQ-00685"
   },
   {
    "email": "treasury@brucepower.com",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.brucepower.com/become-a-supplier/accounts-payable/",
    "quote": "the Supplier with details of each payment. To be setup for electronic payments or to request a change in payment type, please reach out to treasury@brucepower.com for assistance. Financial Accounting Services Contact For Accounts Payable assistance, please email: BNPDacctspayableinquiries",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Bruce Power L.P.",
    "task_id": "CL-WS-00345"
   },
   {
    "email": "BNPDAcctsPayableInquiriesOnly@brucepower.com",
    "type": "accounts_payable",
    "invoice_portal": "https://www.brucepower.com/become-a-supplier/accounts-payable/",
    "phone": "519 361 2673",
    "mailing_address": "177 Tie Rd., R.R. 2, Tiverton, ON N0G 2T0, Canada",
    "requirements": "Nuclear power generator; supplier material invoices delivered via SAP Business Network; all inquiries, statements, and AP communica
```

## PO-level open data naming this buyer
_none_

## Contract records between the pair (dataset)
| record_id | source | status | title | value | currency | start | end | identifiers | link |
|---|---|---|---|---|---|---|---|---|---|
| private_press:2481db493a50ab4c18a2750a5c07d816d870d0f8 | private_press | ongoing_inferred | Bruce Power signs multi-year agreement with NPX to drive innovation and growth | 50000000 | CAD |  |  | {} | https://www.newswire.ca/news-releases/bruce-power-signs-multi-year-agreement-with-npx-to-drive-innovation-and-growth-858964255.html |

## The buyer's other Canadian-vendor records (first 60 of 0)
_none_

## The vendor's other buyers in the dataset (first 60 of 0)
_none_

## Open questions for hand research (layer 2)

- the vendor's GST/HST number (BN9)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
