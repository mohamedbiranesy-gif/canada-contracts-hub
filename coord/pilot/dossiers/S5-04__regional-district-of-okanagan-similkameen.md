# S5-04 — Regional District of Okanagan-Similkameen ⇄ ICEsoft Technologies Canada Corp. (Voyent Alert!)

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 2 · AP grade B · missing: the vendor's GST/HST number (BN9)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Regional District of Okanagan-Similkameen (RDOS) — RDOS, 101 Martin Street, Penticton, BC, Canada V2A 5J9
SUBMIT TO: finance@rdos.bc.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) | tender portal (not an invoice channel): Bonfire
REFERENCE: none in the record | PO rule: yes (as published: Purchase Order number must)
FROM / REMIT TO: ICEsoft Technologies Canada Corp. (Voyent Alert!) — 100 King Street West, Suite 7210, Toronto, (Ontario), M5X 1E1 | GST/HST number not public
TAX: Tax Exemption (as printed on https://www.rdos.bc.ca/finance/information-rates-forms/, re-read 2026-11-08) | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Regional District of Okanagan-Similkameen (municipality / local government, jurisdiction not stated) — active paid service of a Canada-HQ ve
```

## Relationship
- **rank_group**: T3
- **data_quality_score**: 74
- **ship_ready**: yes (finance mailbox, not AP)
- **sensitivity_flag**: no
- **evidence_age_days**: 12
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Regional District of Okanagan-Similkameen (municipality / local government, jurisdiction not stated) — active paid service of a Canada-HQ vendor seen on the buyer's own site: ICEsoft Technologies Canada Corp. (Voyent Alert!) | awarded 2026-11-03 | published by: the buyer's own website (service of a Canada-HQ vendor in use) | record: https://www.rdos.bc.ca/ | vendor in Canada because: service of a Canada-HQ vendor seen on the buyer's own site (tech)=ources Admin Support About Voyent Alert! Product Features Resources Admin Support About Voyent Alert! Contact Suite 340 600 Crowfoot Crescent NW Calgary,  | status rule: active service seen on the buyer's own site (2026-11-03): Canada-HQ vendor ICEsoft Technologies Canada Corp. (Voyent Alert!)
- **how_relationship_was_found**: tools/tech_portals2.py / tech_relationships.py found the buyer's own web property running the Canada-HQ vendor's paid platform (portal host or embedded service), dated by the page read
- **keys**: lead:b9dce403f6a17c06
- **tier**: T
- **grade**: 3
- **records_with_this_vendor**: 1 (relationship record: the buyer's own website (service of a Canada-HQ vendor in use); 0 in the contract dataset)

## Buyer
- **buyer**: Regional District of Okanagan-Similkameen
- **buyer_website**: https://rdos.bc.ca/
- **buyer_address**: RDOS, 101 Martin Street, Penticton, BC, Canada V2A 5J9
- **buyer_phone**: 250-492-0237
- **buyer_contact_evidence_url**: https://www.rdos.bc.ca/helpful-links/contact-us
- **buyer_legal_name_as_published**: Regional District of Okanagan-Similkameen (RDOS)
- **buyer_logo_url**: https://www.rdos.bc.ca/themes/rdos/images/logos/rdos-logo-45x60.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/regional-district-of-okanagan-similkameen/
- **buyer_type**: municipality / local government
- **buyer_sector**: government: municipal
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q1661516; regional district in British Columbia
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.rdos.bc.ca/helpful-links/contact-us (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_exempt_status**: Tax Exemption (as printed on https://www.rdos.bc.ca/finance/information-rates-forms/, re-read 2026-11-08)
- **buyer_tax_status_derived**: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Note: A municipality is not a government for purposes of the GST/HST"); charge GST/HST; derived from buyer type, not published by the buyer
- **buyer_esignature_preference**: DocuSign Envelope ID: 64ED74D0-E5A3-4A2D-BCEF-818C68F75835 Regional District of Okanagan (as printed on https://www.rdos.bc.ca/assets/COMMS-2024/RDOS-Consolidated-Financial-Statements-2023.pdf, re-read 2026-11-08)
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: finance@rdos.bc.ca
- **email_type**: finance/accounting dept or supplier-payment office
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); finance mailbox
- **email_evidence_url**: https://www.rdos.bc.ca/finance/information-rates-forms/
- **email_evidence_quote**: ing your application or wish to view the Property Tax Exemption Policy, please call the RDOS Finance Department at 250-492-0237 or email at finance@rdos.bc.ca. 2025 Property Tax Exemption Recipients Click here to view the 2025 Notice of Property Tax Exemption Annual Utilities Invoices will
- **email_evidence_context**: ts may be asked to publicly acknowledge the exemption . If you require further information, assistance completing your application or wish to view the Property Tax Exemption Policy, please call the RDOS Finance Department at 250-492-0237 or email at finance@rdos.bc.ca. 2025 Property Tax Exemption Recipients Click here to view the 2025 Notice of Property Tax Exemption Annual Utilities Invoices will be mailed the beginning of July 2025 - due date will be August 29, 2025. Annual utilities include: Garbage & Recyclin (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: finance@rdos.bc.ca (finance/accounting dept or supplier-payment office) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-10-28 | page: https://www.rdos.bc.ca/finance/information-rates-forms/ | quote: "ing your application or wish to view the Property Tax Exemption Policy, please call the RDOS Finance Department at 250-492-0237 or email at finance@rdos.bc.ca. " | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-WD-002789
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none; rua=mailto:934e6c46@mxtoolbox.dmarc-report.com; ruf=mailto:934e6c46@forensics.dmarc-report.com; fo=1
- **dmarc_record_domain**: rdos.bc.ca
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 include:spf.protection.outlook.com include:spf-ca.emailsignatures365.com -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_phone**: 250-492-0237 (as printed on https://www.rdos.bc.ca/finance/information-rates-forms/, re-read 2026-11-08)
- **po_required_as_published**: yes (as published: Purchase Order number must) (as printed on https://www.rdos.bc.ca/assets/FINANCE/RFPs/RDOSPOtermsandconditions.pdf, re-read 2026-11-08)
- **invoice_portal_url**: Bonfire
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **ap_system_hint**: named on the buyer's page: Bonfire (as printed on https://www.rdos.bc.ca/assets/COMMS-2026/ADVERTISEMENT-RFP-RDOS-26-FINANCE-097-Town-of-Osoyoos-Sunbowl-Arena-Roof.pdf, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "po_required": "yes (as published: Purchase Order number must) (as printed on https://www.rdos.bc.ca/assets/FINANCE/RFPs/RDOSPOtermsandconditions.pdf, re-read 2026-11-08)", "portal_url": "Bonfire", "portal_kind": "actionable supplier / invoice portal named by the buyer", "ap_phone": "250-492-0237 (as printed on https://www.rdos.bc.ca/finance/information-rates-forms/, re-read 2026-11-08)"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 2
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Regional District of Okanagan-Similkameen (RDOS) — RDOS, 101 Martin Street, Penticton, BC, Canada V2A 5J9 ⏎ SUBMIT TO: finance@rdos.bc.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) | tender portal (not an invoice channel): Bonfire ⏎ REFERENCE: none in the record | PO rule: yes (as published: Purchase Order number must) ⏎ FROM / REMIT TO: ICEsoft Technologies Canada Corp. (Voyent Alert!) — 100 King Street West, Suite 7210, Toronto, (Ontario), M5X 1E1 | GST/HST number not public ⏎ TAX: Tax Exemption (as printed on https://www.rdos.bc.ca/finance/information-rates-forms/, re-read 2026-11-08) | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Regional District of Okanagan-Similkameen (municipality / local government, jurisdiction not stated) — active paid service of a Canada-HQ ve
- **invoice_card_json**: {"bill_to": {"legal_name": "Regional District of Okanagan-Similkameen (RDOS)", "legal_name_is_published": true, "address": "RDOS, 101 Martin Street, Penticton, BC, Canada V2A 5J9", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "finance@rdos.bc.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "Bonfire", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: Bonfire (as printed on https://www.rdos.bc.ca/assets/COMMS-2026/ADVERTISEMENT-RFP-RDOS-26-FINANCE-097-Town-of-Osoyoos-Sunbowl-Arena-Roof.pdf, re-read 2026-11-08)", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "tender portal (not an invoice channel)"}, "references_required": {"po_required": "yes (as published: Purchase Order number must) (as printed on https://www.rdos.bc.ca/assets/FINANCE/RFPs/RDOSPOtermsandconditions.pdf, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: Purchase Order number must) (as printed on https://www.rdos.bc.ca/assets/FINANCE/RFPs/RDOSPOtermsandconditions.pdf, re-read 2026-11-08))"}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": "Docu
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number; vendor legal name
- **ap_grade**: B
- **ap_score**: 69
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; currency known; AP phone or AP contact | missing: invoicing / AP mailbox; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published payment terms
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms not published (buyer's default applies)
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: Purchase Order number must) (as printed on https://www.rdos.bc.ca/assets/FINANCE/RFPs/RDOSPOtermsandconditions.pdf, re-read 2026-11-08))

## Vendor
- **vendor**: ICEsoft Technologies Canada Corp. (Voyent Alert!)
- **vendor_address**: 100 King Street West, Suite 7210, Toronto, (Ontario), M5X 1E1
- **vendor_country_basis**: service of a Canada-HQ vendor seen on the buyer's own site (tech)=ources Admin Support About Voyent Alert! Product Features Resources Admin Support About Voyent Alert! Contact Suite 340 600 Crowfoot Crescent NW Calgary, AB, T3G 0B4 1-877-263-3822 product.sales@icesoft.com Social Co
- **vendor_website**: https://thecse.com/
- **vendor_emails**: info@thecse.com
- **vendor_contact_evidence_url**: https://thecse.com/fr/contact-us/
- **vendor_logo_url**: https://thecse.com/apple-touch-icon.png
- **vendor_website_basis**: found by a web search, confirmed by reading the site on 2026-11-08: https://thecse.com/listings/icesoft-technologies-canada-corp/ (ICEsoft Technologies Canada Corp. | The Canadian Securities Exchange (CSE) Search Symbol, Name or Keyword en en Quote About Disclosure ISFT 0.00% ISFT 0.00% ICE)
- **vendor_facts_provenance**: name and address: the record's vendor block (the buyer's own website (service of a Canada-HQ vendor in use)); phone / role e-mails / logo: the vendor's own site, https://thecse.com/fr/contact-us/ (tools/org_contacts.py, org_extras.py); website: https://thecse.com/
- **vendor_concentration_top_share**: no dataset record for this pair / buyer

## Contract
- **po_required_as_published**: yes (as published: Purchase Order number must) (as printed on https://www.rdos.bc.ca/assets/FINANCE/RFPs/RDOSPOtermsandconditions.pdf, re-read 2026-11-08)
- **contract_status**: active service seen on the buyer's own site (2026-11-03): Canada-HQ vendor ICEsoft Technologies Canada Corp. (Voyent Alert!)
- **award_date**: 2026-11-03
- **contract_link**: https://www.rdos.bc.ca/
- **source**: the buyer's own website (service of a Canada-HQ vendor in use)
- **contracts_with_canadian_suppliers**: 3
- **records_with_this_vendor**: 1 (relationship record: the buyer's own website (service of a Canada-HQ vendor in use); 0 in the contract dataset)
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Note: A municipality is not a government for purposes of the GST/HST"); charge GST/HST; derived from buyer type, not published by the buyer
- **tax_rate_indicative_derived**: GST 5% (BC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Regional District of Okanagan-Similkameen (RDOS) — RDOS, 101 Martin Street, Penticton, BC, Canada V2A 5J9 ⏎ SUBMIT TO: finance@rdos.bc.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) | tender portal (not an invoice channel): Bonfire ⏎ REFERENCE: none in the record | PO rule: yes (as published: Purchase Order number must) ⏎ FROM / REMIT TO: ICEsoft Technologies Canada Corp. (Voyent Alert!) — 100 King Street West, Suite 7210, Toronto, (Ontario), M5X 1E1 | GST/HST number not public ⏎ TAX: Tax Exemption (as printed on https://www.rdos.bc.ca/finance/information-rates-forms/, re-read 2026-11-08) | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Regional District of Okanagan-Similkameen (municipality / local government, jurisdiction not stated) — active paid service of a Canada-HQ ve
- **invoice_card_json**: {"bill_to": {"legal_name": "Regional District of Okanagan-Similkameen (RDOS)", "legal_name_is_published": true, "address": "RDOS, 101 Martin Street, Penticton, BC, Canada V2A 5J9", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "finance@rdos.bc.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "Bonfire", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: Bonfire (as printed on https://www.rdos.bc.ca/assets/COMMS-2026/ADVERTISEMENT-RFP-RDOS-26-FINANCE-097-Town-of-Osoyoos-Sunbowl-Arena-Roof.pdf, re-read 2026-11-08)", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "tender portal (not an invoice channel)"}, "references_required": {"po_required": "yes (as published: Purchase Order number must) (as printed on https://www.rdos.bc.ca/assets/FINANCE/RFPs/RDOSPOtermsandconditions.pdf, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: Purchase Order number must) (as printed on https://www.rdos.bc.ca/assets/FINANCE/RFPs/RDOSPOtermsandconditions.pdf, re-read 2026-11-08))"}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": "Docu
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number; vendor legal name
- **ap_grade**: B
- **ap_score**: 69
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; currency known; AP phone or AP contact | missing: invoicing / AP mailbox; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published payment terms
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms not published (buyer's default applies)
- **facts_provenance_json**: {"mailbox": ["finance@rdos.bc.ca (finance/accounting dept or supplier-payment office)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-10-28", "page: https://www.rdos.bc.ca/finance/information-rates-forms/", "quote: \"ing your application or wish to view the Property Tax Exemption Policy, please call the RDOS Finance Department at 250-492-0237 or email at finance@rdos.bc.ca. \"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-WD-002789"], "buyer_facts": ["address and phone: the buyer's own site, https://www.rdos.bc.ca/helpful-links/contact-us (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"],

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.rdos.bc.ca/finance/information-rates-forms/ | 2026-11-08 | ok |  |  |  | 250-492-0237 |  |  |  |  |  |

## Buyer site facts (org_extras, rdos.bc.ca)
- **status**: ok
- **pages**: 5
- **language**: en
- **legal_name**: Regional District of Okanagan-Similkameen (RDOS)
- **legal_name_url**: https://www.rdos.bc.ca/
- **legal_name_quote**: ons RDOS Facebook RDOS LinkedIn RDOS Twitter (X) EOC Twitter (X) RDOS YouTube Copyright © 2001-2026 Regional District of Okanagan-Similkameen (RDOS). All rights reserved. Disclaimer Privacy Statement Terms and Conditions Site by Tiraki
- **logo_url**: https://www.rdos.bc.ca/themes/rdos/images/logos/rdos-logo-45x60.png
- **logo_basis**: logo image in the site header
- **domain**: rdos.bc.ca
- **key**: lead:b9dce403f6a17c06
- **name**: Regional District of Okanagan-Similkameen
- **website**: https://rdos.bc.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Regional District of Okanagan-Similkameen
- **legal_name_stated_url**: https://www.rdos.bc.ca/legislative-services/privacy-management/
- **legal_name_stated_quote**: Freedom of Information and Privacy Management | RDOS --> Skip to Content Main Menu Regional District of Okanagan-Similkameen Agenda & Minutes Regional Bylaws Employment/Volunteer Opportunities Notifications I Want To... Appl
- **linkedin_url**: https://www.linkedin.com/company/regional-district-of-okanagan-similkameen/

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "RDOS, 101 Martin Street, Penticton, BC, Canada V2A 5J9", "address_country": "CA", "address_url": "https://www.rdos.bc.ca/helpful-links/contact-us", "address_method": "address-tag", "address_quote": "Conditions Site Search Contact Us Head Office RDOS 101 Martin St. Penticton, BC V2A 5J9 Canada Hours: Monday - Friday 8:30 am - 4:30 pm Closed on statutory holidays Ph", "phone": "250-492-0237", "phone_url": "https://www.rdos.bc.ca/helpful-links/contact-us", "emails": "info@rdos.bc.ca", "emails_url": "https://www.rdos.bc.ca/helpful-links/contact-us", "domain": "rdos.bc.ca", "key": "lead:b9dce403f6a17c06", "name": "Regional District of Okanagan-Similkameen", "website": "https://rdos.bc.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, thecse.com)
- **status**: ok
- **pages**: 4
- **v**: 2
- **linkedin_url**: https://www.linkedin.com/company/canadian-securities-exchange
- **language**: fr
- **legal_name**: CNSX Markets Inc
- **legal_name_url**: https://thecse.com/fr/
- **legal_name_quote**: Pender Street, Suite 305 Vancouver, (Colombie-Britannique), V6E 2M6 Communiquer avec nous fr © 2026 CNSX Markets Inc. Tous droits réservés. Modalités du site Énoncé sur la protection des renseignements personnels Acc
- **logo_url**: https://thecse.com/apple-touch-icon.png
- **logo_basis**: site icon (apple-touch-icon)
- **domain**: thecse.com
- **key**: vendor:ICEsoft Technologies Canada Corp. (Voyent Alert!)
- **name**: ICEsoft Technologies Canada Corp. (Voyent Alert!)
- **website**: https://thecse.com/
- **kind**: vendor
- **date**: 2026-11-09

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "address": "100 King Street West, Suite 7210, Toronto, (Ontario), M5X 1E1", "address_country": "CA", "address_url": "https://thecse.com/fr/contact-us/", "address_method": "address-tag", "address_quote": "416-572-4160 (télécopieur) 100 King Street West, Suite 7210 Toronto, (Ontario), M5X 1E1 Bureau de Vancouver 604-331-1213 604-687-1188 (télécopieur) 1095 West Pender St", "emails": "info@thecse.com", "emails_url": "https://thecse.com/fr/contact-us/", "domain": "thecse.com", "key": "vendor:ICEsoft Technologies Canada Corp. (Voyent Alert!)", "name": "ICEsoft Technologies Canada Corp. (Voyent Alert!)", "website": "https://thecse.com/", "kind": "vendor", "date": "2026-11-09"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Regional District of Okanagan-Similkameen | Q1661516 | official website on the organisation's domain (https://www.rdos.bc.ca/) + name |  | Regional District of Okanagan-Similkameen | district régional d'Okanagan-Similkameen | regional district in British Columbia |  | Canada |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
none
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

- the vendor's GST/HST number (BN9)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
