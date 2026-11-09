# S2-36 — South Dundas ⇄ Welch LLP

Stratum: **S2_complete_no_published_PO_rule** · pay on sight: yes — reference rule not published (quote the buyer's PO / order number when one is issued) · channel tier 2 · AP grade C · missing: (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Municipality of South Dundas — 34 Ottawa Street, P.O. Box 740, Morrisburg, ON K0C 1X0
SUBMIT TO: finance@southdundas.com (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) | tender portal (not an invoice channel): https://southdundas.bidsandtenders.ca/Module/Tenders/en — bids&tenders
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: WELCH LLP — 123 SLATER ST 3 FL, OTTAWA, ON, K1P 5H2, CAN | GST/HST 114798614 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2022-04-25; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9)
TAX: DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https: | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: South Dundas (organisation (type not stated in the record), jurisdiction not stated) — public contract / purchase award in the last 12 month
```

## Relationship
- **rank_group**: B3
- **data_quality_score**: 75
- **ship_ready**: yes (finance mailbox, not AP)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: South Dundas (organisation (type not stated in the record), jurisdiction not stated) — public contract / purchase award in the last 12 months (dated record): Welch LLP | awarded 2026-07-08 | published by: auditor of record (own audited financial statements, auditor's report signed in Morrisburg | record: https://www.southdundas.com/sites/3/files/2026-08/2025%20Audited%20financial%20statements.pdf | vendor in Canada because: auditor of record (own audited financial statements, auditor's report signed in Morrisburg, Ontario)=financial statements and the external auditor’s report. The external auditors, Welch LLP, conduct an independent examin | status rule: likely active (record dated in the last 12 months: auditor of record (own audited financial statements, auditor's report signed in Morrisburg)
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: lead:426215246c9b4c8d|lead:bd20d0cd668cbbd1
- **tier**: B
- **grade**: 3
- **records_with_this_vendor**: 1 (relationship record: auditor of record (own audited financial statements, auditor's report signed in Morrisburg; 0 in the contract dataset)

## Buyer
- **buyer**: South Dundas
- **buyer_website**: https://www.southdundas.com/
- **buyer_address**: 34 Ottawa Street, P.O. Box 740, Morrisburg, ON K0C 1X0
- **buyer_phone**: 613-543-2673
- **buyer_contact_evidence_url**: https://www.southdundas.com/contact-us
- **buyer_legal_name_as_published**: Municipality of South Dundas
- **buyer_logo_url**: https://www.southdundas.com/sites/3/files/SouthDundasLogo_ex_horizontal.png
- **buyer_website_status**: site answers
- **buyer_type**: municipality / local government (from the organisation's name / web domain)
- **buyer_sector**: government: municipal
- **buyer_municipal_tier**: Lower Tier (within Stormont, Dundas and Glengarry; Ontario MMAH list) (provincial municipal directory: https://data.ontario.ca/dataset/62e83cbc-0731-4d66-abdc-2f2b31bcd76c/resource/6783a586-6b05-4a73-9663-e60a6963c91e/download/municipalities_-_en_2026-0526.csv, 2026-11-08)
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q4116598; lower-tier municipality of Ontario
- **buyer_founded**: 1785-00-00 (Wikidata Q4116598, official website on the organisation's domain (http://www.southdundas.com/) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.southdundas.com/contact-us (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Note: A municipality is not a government for purposes of the GST/HST"); charge GST/HST; derived from buyer type, not published by the buyer
- **buyer_keys**: 2

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: finance@southdundas.com
- **email_type**: finance/accounting dept or supplier-payment office
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); finance mailbox
- **email_evidence_url**: https://www.southdundas.com/financialprograms
- **email_evidence_quote**: y of purposes. The intake for the 2027 budget is now OPEN. Applications can be submitted in-person at the Municipal Office, or via email to finance@southdundas.com DEADLINE: December 23, 2026 Municipal Grants Programs Each year, the Municipality of South Dundas recognizes the contributions
- **email_evidence_context**: opportunities and financial assistance programs that residents can potentially take advantage of for a variety of purposes. The intake for the 2027 budget is now OPEN. Applications can be submitted in-person at the Municipal Office, or via email to finance@southdundas.com DEADLINE: December 23, 2026 Municipal Grants Programs Each year, the Municipality of South Dundas recognizes the contributions of the community and volunteer groups within the Municipality and the benefits they provide to residents by offering an op (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: finance@southdundas.com (finance/accounting dept or supplier-payment office) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://www.southdundas.com/financialprograms | quote: "y of purposes. The intake for the 2027 budget is now OPEN. Applications can be submitted in-person at the Municipal Office, or via email to finance@southdundas." | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-32993
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1;p=quarantine;pct=100;rua=mailto:dmarcmosd@southdundas.com
- **dmarc_record_domain**: southdundas.com
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 ip4:208.88.198.254 ip4:74.13.225.242 ip4:207.107.133.237 ip4:207.164.184.37 ip4:166.78.70.127 ip4:162.247.19.222 ip4:198.244.48.198 include:spf.protection.outlook.com include:sendgrid.net -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoice_portal_url**: https://southdundas.bidsandtenders.ca/Module/Tenders/en — bids&tenders
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **ap_system_hint**: named on the buyer's page: bids&tenders (as printed on https://www.southdundas.com/municipal-centre/tenders, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "portal_url": "https://southdundas.bidsandtenders.ca/Module/Tenders/en — bids&tenders", "portal_kind": "actionable supplier / invoice portal named by the buyer"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 2
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Municipality of South Dundas — 34 Ottawa Street, P.O. Box 740, Morrisburg, ON K0C 1X0 ⏎ SUBMIT TO: finance@southdundas.com (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) | tender portal (not an invoice channel): https://southdundas.bidsandtenders.ca/Module/Tenders/en — bids&tenders ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: WELCH LLP — 123 SLATER ST 3 FL, OTTAWA, ON, K1P 5H2, CAN | GST/HST 114798614 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2022-04-25; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https: | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: South Dundas (organisation (type not stated in the record), jurisdiction not stated) — public contract / purchase award in the last 12 month
- **invoice_card_json**: {"bill_to": {"legal_name": "Municipality of South Dundas", "legal_name_is_published": true, "address": "34 Ottawa Street, P.O. Box 740, Morrisburg, ON K0C 1X0", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "finance@southdundas.com", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "https://southdundas.bidsandtenders.ca/Module/Tenders/en — bids&tenders", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: bids&tenders (as printed on https://www.southdundas.com/municipal-centre/tenders, re-read 2026-11-08)", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "tender portal (not an invoice channel)"}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.can", "buyer_tax_status_is_published": false, "indicative_rate": "HST 13% (Ontario)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "114798614RT0001 (
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 61
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: Welch LLP
- **vendor_legal_name**: WELCH LLP
- **vendor_registry_id**: BC OrgBook (BC registration): XL0000128
- **vendor_registry_url**: https://orgbook.gov.bc.ca/entity/XL0000128
- **vendor_legal_form**: Extraprovincial LLP (home jurisdiction ON)
- **vendor_address**: 123 SLATER ST 3 FL, OTTAWA, ON, K1P 5H2, CAN
- **vendor_country_basis**: auditor of record (own audited financial statements, auditor's report signed in Morrisburg, Ontario)=financial statements and the external auditor’s report. The external auditors, Welch LLP, conduct an independent examination, in ... reasurer | Morrisburg, Ontario July 8, 2026
- **vendor_bn9**: 114798614 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2022-04-25; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)
- **vendor_gst_hst_derived**: 114798614RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://www.welchllp.com/
- **vendor_website_basis**: found by a web search, confirmed by reading the site on 2026-11-08: http://welchllp.com/about/ (About Welch LLP Accounting Firm - Welch LLP Skip to content Services Services Delivering quality service to our clients is our number one priority. Assurance an)
- **vendor_facts_provenance**: name and address: the record's vendor block (auditor of record (own audited financial statements, auditor's report signed in Morrisburg); registry identity: BC OrgBook (BC registration): XL0000128 status BC OrgBook (BC registration): Active (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: federal grants & contributions disclosure (recipient_business_number); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2024-04-03; website: https://www.welchllp.com/
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: BC OrgBook (BC registration): Active
- **vendor_incorporation_date**: 2024-04-03
- **vendor_years_in_business**: 2.6 (since 2024-04-03, registry date)
- **vendor_bn_source**: federal grants & contributions disclosure (recipient_business_number)

## Contract
- **contract_status**: likely active (record dated in the last 12 months: auditor of record (own audited financial statements, auditor's report signed in Morrisburg)
- **award_date**: 2026-07-08
- **contract_link**: https://www.southdundas.com/sites/3/files/2026-08/2025%20Audited%20financial%20statements.pdf
- **source**: auditor of record (own audited financial statements, auditor's report signed in Morrisburg
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: auditor of record (own audited financial statements, auditor's report signed in Morrisburg; 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Note: A municipality is not a government for purposes of the GST/HST"); charge GST/HST; derived from buyer type, not published by the buyer
- **tax_rate_indicative_derived**: HST 13% (Ontario) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 114798614RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: yes — reference rule not published (quote the buyer's PO / order number when one is issued)
- **pay_on_sight_missing**: (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Municipality of South Dundas — 34 Ottawa Street, P.O. Box 740, Morrisburg, ON K0C 1X0 ⏎ SUBMIT TO: finance@southdundas.com (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) | tender portal (not an invoice channel): https://southdundas.bidsandtenders.ca/Module/Tenders/en — bids&tenders ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: WELCH LLP — 123 SLATER ST 3 FL, OTTAWA, ON, K1P 5H2, CAN | GST/HST 114798614 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2022-04-25; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https: | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: South Dundas (organisation (type not stated in the record), jurisdiction not stated) — public contract / purchase award in the last 12 month
- **invoice_card_json**: {"bill_to": {"legal_name": "Municipality of South Dundas", "legal_name_is_published": true, "address": "34 Ottawa Street, P.O. Box 740, Morrisburg, ON K0C 1X0", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "finance@southdundas.com", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "https://southdundas.bidsandtenders.ca/Module/Tenders/en — bids&tenders", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: bids&tenders (as printed on https://www.southdundas.com/municipal-centre/tenders, re-read 2026-11-08)", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "tender portal (not an invoice channel)"}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.can", "buyer_tax_status_is_published": false, "indicative_rate": "HST 13% (Ontario)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "114798614RT0001 (
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 61
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["finance@southdundas.com (finance/accounting dept or supplier-payment office)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://www.southdundas.com/financialprograms", "quote: \"y of purposes. The intake for the 2027 budget is now OPEN. Applications can be submitted in-person at the Municipal Office, or via email to finance@southdundas.\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-32993"], "buyer_facts": ["address and phone: the buyer's own site, https://www.southdundas.com/contact-us (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (auditor of record (own audited financial statements, auditor's report signed in Morrisburg)", "registry identity: BC OrgBook (BC registration): XL0000128 status BC OrgBook (BC registration): Active (scripts/enrichment_*: Corporation

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.southdundas.com/financialprograms | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |
| https://www.southdundas.com/contact-us | 2026-11-06 | http_0 |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, southdundas.com)
- **status**: ok
- **pages**: 4
- **language**: en
- **legal_name**: Municipality of South Dundas
- **legal_name_url**: https://www.southdundas.com/
- **legal_name_quote**: nday - Thursday, 8:30 a.m. - 5:00 p.m. Friday, 8:30 a.m. - 12:00 p.m Subscribe to newsletter © 2026 Municipality of South Dundas Website by Upanup's Civikit Solution
- **logo_url**: https://www.southdundas.com/sites/3/files/SouthDundasLogo_ex_horizontal.png
- **logo_basis**: logo image in the site header
- **domain**: southdundas.com
- **key**: lead:426215246c9b4c8d
- **name**: South Dundas
- **website**: https://southdundas.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Accessibility Advisory Committee
- **legal_name_stated_url**: https://www.southdundas.com/municipal-centre/clerk-services/accessibility
- **legal_name_stated_quote**: and infrastructure for all residents. This page outlines the regulations we follow, introduces our Accessibility Advisory Committee, shares our updated Accessibility Plan and Compliance Report, and invites you to provide feedback o
- **tel_links**: 613-543-2673

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "34 Ottawa Street, P.O. Box 740, Morrisburg, ON K0C 1X0", "address_country": "CA", "address_url": "https://www.southdundas.com/contact-us", "address_method": "pattern", "address_quote": "Home Contact Us Municipal Centre 34 Ottawa Street, P.O. Box 740, Morrisburg, ON K0C 1X0 Phone: 613-543-2673 Toll Free: 1-800-265-0619 Fax 613-543-1076 mail@southdundas", "phone": "613-543-2673", "phone_url": "https://www.southdundas.com/contact-us", "emails": "mail@southdundas.com", "emails_url": "https://www.southdundas.com/contact-us", "domain": "southdundas.com", "key": "lead:426215246c9b4c8d", "name": "South Dundas", "website": "https://southdundas.com/", "kind": "buyer", "date": "2026-11-03"}

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
| b | Municipality of South Dundas |  |  |  |  |  |  |  |  |  |  |
| b | South Dundas | Q4116598 | official website on the organisation's domain (http://www.southdundas.com/) + name |  | South Dundas | South Dundas | lower-tier municipality of Ontario |  | Canada; Upper Canada | 1785-00-00 |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:426215246c9b4c8d",
 "ap_contact_team": {
  "emails": [
   "mail@southdundas.com",
   "finance@southdundas.com"
  ],
  "invoice_portal": null,
  "phone": "613-543-2673 ext. 4757",
  "mailing_address": null,
  "invoicing_requirements": "AP phone 613-543-2673 ext. 4757.",
  "evidence": [
   {
    "email": "mail@southdundas.com",
    "type": "general",
    "invoice_portal": null,
    "phone": "613-543-2673 ext. 4757",
    "mailing_address": null,
    "requirements": "AP phone 613-543-2673 ext. 4757.",
    "applies_to": "whole_organisation",
    "page_url": "https://www.southdundas.com/contact-us",
    "quote": "mail@southdundas.com",
    "retrieved_date": "2026-11-08",
    "found_by": "chatgpt",
    "verification": "verified",
    "source_file": "chatgpt_buyer_ap_results_batch50.csv",
    "org": "Municipality of South Dundas",
    "task_id": "CH-AP-50060"
   },
   {
    "email": "finance@southdundas.com",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.southdundas.com/financialprograms",
    "quote": "y of purposes. The intake for the 2027 budget is now OPEN. Applications can be submitted in-person at the Municipal Office, or via email to finance@southdundas.com DEADLINE: December 23, 2026 Municipal Grants Programs Each year, the Municipality of South Dundas recognizes the contributions",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Municipality of South Dundas",
    "task_id": "CL-LD-32993"
   }
  ]
 },
 "research_status": {
  "found": 2
 },
 "queries_tried": [
  "site:southdundas.com \"accounts payable\" invoice supplier South Dundas | site:southdundas.com \"finance@southdundas.com\" | site:southdundas.com \"accounts payable\" \"cheque\" supplier South Dundas",
  "site crawl of southdundas.com (25 pages, robots.txt respected), no AI, no search engine"
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

## The vendor's other buyers in the dataset (first 60 of 15)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_bidsandtenders:2e28ec8e-5076-4a84-a1e6-a59918520f15:1 | Township of North Dundas | Municipal Audit Services |  |  |  | https://northdundas.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/2e28ec8e-5076-4a84-a1e6-a59918520f15 |
| ca_bidsandtenders:6dd44456-33fe-4263-a41a-48998f632003:1 | Renfrew County District School Board | External Auditing Services |  |  |  | https://rcdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/6dd44456-33fe-4263-a41a-48998f632003 |
| canada_federal:dfatd-maecd:7474655 | Global Affairs Canada | Employer contribution to other pension programs including Judges Act | 178045.1 |  |  | https://search.open.canada.ca/contracts/record/dfatd-maecd,C-2026-2027-Q1-00220 |
| canada_federal:dfatd-maecd:7476966 | Global Affairs Canada | Accounting and audit services | 17718.4 |  |  | https://search.open.canada.ca/contracts/record/dfatd-maecd,C-2026-2027-Q1-00877 |
| canada_federal:dnd-mdn:W7681-25-R003 | National Defence | Accounting and audit services | 182574.1 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2025-2026-Q4-02465 |
| canada_federal:pwgsc-tpsgc:700865191 | Public Services and Procurement Canada | Accounting and audit services | 54388.03 |  |  | https://search.open.canada.ca/contracts/record/pwgsc-tpsgc,C-2026-2027-Q1-01613 |
| canada_federal:cb:CW2455609 | Department of Foreign Affairs, Trade and Development (GAC) | Audit and Support Services on Contribution Agreements for GAC 004 | 1053990.0 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cw2455609 |
| canada_federal:cb:PW-22-01011680-1029195 | Auditor General of Canada, Office of the | Request for Supply Arrangment (RFSA) # 369: Audit and Related Services |  |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/pw-22-01011680-1029195 |
| usaspending:CONT_AWD_273FCC24F0117_2700_GS23F0049U_4730 | Federal Communications Commission | NANPA BILLING AND COLLECTION AGENT. | 1199199.96 |  |  | https://www.usaspending.gov/award/CONT_AWD_273FCC24F0117_2700_GS23F0049U_4730/ |
| usaspending:CONT_IDV_GS23F0049U_4730 | General Services Administration | FEDERAL SUPPLY SCHEDULE CONTRACT | 4968170.0 |  |  | https://www.usaspending.gov/award/CONT_IDV_GS23F0049U_4730/ |
| ca_canadabuys_contract_history:EN578-172870/098/ZN | Public Works and Government Services Canada | WELCH LLP (EN578-172870/098/ZN~001) |  |  |  | https://open.canada.ca/data/en/dataset/4fe645a1-ffcd-40c1-9385-2c771be956a4 |
| ca_canadabuys_contract_history:an:PW-14-00651516-665641 | Department of National Defence | PASS – External Audit of Service Income Security Insurance Plan Financial Services (SISIP FS) | 71574.2 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/pw-14-00651516-665641 |
| ca_canadabuys_contract_history:an:PW-16-00740674-763290 | Auditor General of Canada, Office of the | Request for Standing Offers #264 (“RFSO”) Special Examination Auditing Services |  |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/pw-16-00740674-763290 |
| ca_canadabuys_contract_history:an:PW-16-00750714-776120 | Auditor General of Canada, Office of the | Audit and Related Services - Request for Standing Offers #256 (“RFSO”) |  |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/pw-16-00750714-776120 |
| ca_canadabuys_contract_history:an:E60ZQ-180001:025:ZQ | Public Works and Government Services Canada | Internal and External Audits (Supply Arrangement PASS) |  |  |  | https://open.canada.ca/data/en/dataset/a1acb126-9ce8-40a9-b889-5da2b1dd20cb |

## Open questions for hand research (layer 2)

- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
