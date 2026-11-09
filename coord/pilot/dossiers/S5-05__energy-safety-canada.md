# S5-05 — Energy Safety Canada ⇄ Martell Refrigeration & Air Conditioning

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 2 · AP grade C · missing: the vendor's GST/HST number (BN9); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: ENERGY SAFETY CANADA (as registered: Corporations Canada (open data), corporation number 10340871, 2026-11-08) — 150 - 2 Smed Lane SE, Calgary, AB, T2C 4T5, CA (schema.org JSON-LD PostalAddress on https://www.energysafetycanada.com/) — buyer tax no. 825722879 (Corporations Canada (open data), corporation number 10340871, 2026-11-08)
SUBMIT TO: accounting@energysafetycanada.com (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Coral Canada Wide Ltd (as printed on the vendor's site: https://coralcanadawide.com/) — 30, 2150 29 Street NE, Calgary, Alberta, Canada, T1Y 7G4 | GST/HST number not public
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Energy Safety Canada | D2L
```

## Relationship
- **rank_group**: D3
- **data_quality_score**: 60
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Energy Safety Canada (utility / public corporation, jurisdiction not stated) — named as a client by the Canada-located vendor (client list / customer story), dated: Martell Refrigeration & Air Conditioning | subject: Energy Safety Canada | D2L | published by: the Canada-located vendor's own website | record: https://coralcanadawide.com/locations/nanaimo-hvac-r/ | vendor in Canada because: vendor located in Canada (wall)=coralcanadawide.com | status rule: client listing on the vendor's own site (undated)
- **how_relationship_was_found**: tools/client_lists.py / dated_stories.py read the vendor's dated customer story / case study naming the buyer
- **keys**: lead:288361125e71bc1f
- **tier**: D
- **grade**: 3
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: Energy Safety Canada
- **buyer_website**: https://energysafetycanada.com/
- **buyer_address**: 150 - 2 Smed Lane SE, Calgary, AB, T2C 4T5, CA (schema.org JSON-LD PostalAddress on https://www.energysafetycanada.com/)
- **buyer_phone**: 1-800-667-5557
- **buyer_contact_evidence_url**: https://www.energysafetycanada.com/contact-us
- **buyer_legal_name_as_published**: ENERGY SAFETY CANADA (as registered: Corporations Canada (open data), corporation number 10340871, 2026-11-08)
- **buyer_bn_as_published**: 825722879 (Corporations Canada (open data), corporation number 10340871, 2026-11-08)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 825722879RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_logo_url**: https://www.energysafetycanada.com/themes/custom/esc/logo.svg
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/energy-safety-canada/
- **buyer_registry_id**: corporation number 10340871 (Corporations Canada (open data); https://ised-isde.canada.ca/cc/lgcy/fdrlCrpDtls.html?corpId=10340871)
- **buyer_type**: utility / public corporation
- **buyer_sector**: utility
- **buyer_legal_form**: Canada Not-for-profit Corporations Act (Corporations Canada (open data), corporation number 10340871, 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.energysafetycanada.com/contact-us (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_esignature_preference**: Docusign Envelope ID: AEE04535-9B2E-4491-9BE6-AA985DBE9672 ENERGY SAFETY CANADA Statemen (as printed on https://www.energysafetycanada.com/sites/default/files/2026-04/Energy-Safety-Canada-Annual-Financial-Statements-2024.pdf, re-read 2026-11-08)
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: accounting@energysafetycanada.com
- **email_type**: finance/accounting dept or supplier-payment office
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); finance mailbox
- **email_evidence_url**: https://www.energysafetycanada.com/contact-us
- **email_evidence_quote**: d grow leading-5 min-h-0 lg:min-h-px min-w-px relative shrink-0 text-sm text-brand-primary underline break-words" aria-label="Send email to Accounting@EnergySafetyCanada.com"> <span class="__cf_email__" data-cfemail="adeccecec2d8c3d9c4c3caede8c3c8dfcad4fecccbc8d9d4eeccc3ccc9cc83cec2c0">[em
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: accounting@energysafetycanada.com (finance/accounting dept or supplier-payment office) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://www.energysafetycanada.com/contact-us | quote: "d grow leading-5 min-h-0 lg:min-h-px min-w-px relative shrink-0 text-sm text-brand-primary underline break-words" aria-label="Send email to Accounting@EnergySaf" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-01649
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by Microsoft 365
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject; rua=mailto:a61d01d6592d42278ea85b1d00f0b40c@dmarc-reports.cloudflare.net,mailto:gkjhix2d@ag.ca.dmarcian.com
- **dmarc_record_domain**: energysafetycanada.com
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 ip4:204.191.79.192/27 ip4:209.89.104.64/27 ip4:207.102.182.193/30 ip4:64.110.238.78/32 include:spf.protection.outlook.com include:spf.ca.exclaimer.net ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 2
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: ENERGY SAFETY CANADA (as registered: Corporations Canada (open data), corporation number 10340871, 2026-11-08) — 150 - 2 Smed Lane SE, Calgary, AB, T2C 4T5, CA (schema.org JSON-LD PostalAddress on https://www.energysafetycanada.com/) — buyer tax no. 825722879 (Corporations Canada (open data), corporation number 10340871, 2026-11-08) ⏎ SUBMIT TO: accounting@energysafetycanada.com (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Coral Canada Wide Ltd (as printed on the vendor's site: https://coralcanadawide.com/) — 30, 2150 29 Street NE, Calgary, Alberta, Canada, T1Y 7G4 | GST/HST number not public ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Energy Safety Canada | D2L
- **invoice_card_json**: {"bill_to": {"legal_name": "ENERGY SAFETY CANADA (as registered: Corporations Canada (open data), corporation number 10340871, 2026-11-08)", "legal_name_is_published": true, "address": "150 - 2 Smed Lane SE, Calgary, AB, T2C 4T5, CA (schema.org JSON-LD PostalAddress on https://www.energysafetycanada.com/)", "address_is_the_invoice_address": false, "tax_number": "825722879 (Corporations Canada (open data), corporation number 10340871, 2026-11-08)", "language": "en"}, "submit_to": {"email": "accounting@energysafetycanada.com", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": "Docusign Envelope ID: AEE04535-9B2E-4491-9BE6-AA985DBE9672 ENERGY SAFETY CANADA Statemen (as printed on https://www.energysafetycanada.com/sites/default/files/2026-04/Energy-Safety-Canada-Annual-Financial-Statements-2024.pdf, re-read 2026-11-08)"}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their", "buyer_tax_status
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number
- **ap_grade**: C
- **ap_score**: 61
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: Martell Refrigeration & Air Conditioning
- **vendor_legal_name**: Coral Canada Wide Ltd (as printed on the vendor's site: https://coralcanadawide.com/)
- **vendor_trading_name**: Martell Refrigeration & Air Conditioning
- **vendor_address**: 30, 2150 29 Street NE, Calgary, Alberta, Canada, T1Y 7G4
- **vendor_country_basis**: vendor located in Canada (wall)=coralcanadawide.com
- **vendor_website**: https://coralcanadawide.com
- **vendor_emails**: info@coralcanadawide.com
- **vendor_phone**: 1-800-380-8008
- **vendor_contact_evidence_url**: https://coralcanadawide.com/contact-us/
- **vendor_logo_url**: https://coralcanadawide.com/wp-content/uploads/2020/07/logo.png
- **vendor_website_status**: site answers
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); phone / role e-mails / logo: the vendor's own site, https://coralcanadawide.com/contact-us/ (tools/org_contacts.py, org_extras.py); website: https://coralcanadawide.com (site answers)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer

## Contract
- **contract_status**: client listing on the vendor's own site (undated)
- **contract_title**: Energy Safety Canada | D2L
- **contract_description**: Energy Safety Canada | D2L (the record's title; the source publishes no separate description)
- **contract_link**: https://coralcanadawide.com/locations/nanaimo-hvac-r/
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 3
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: 3 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 825722879RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (AB) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: ENERGY SAFETY CANADA (as registered: Corporations Canada (open data), corporation number 10340871, 2026-11-08) — 150 - 2 Smed Lane SE, Calgary, AB, T2C 4T5, CA (schema.org JSON-LD PostalAddress on https://www.energysafetycanada.com/) — buyer tax no. 825722879 (Corporations Canada (open data), corporation number 10340871, 2026-11-08) ⏎ SUBMIT TO: accounting@energysafetycanada.com (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Coral Canada Wide Ltd (as printed on the vendor's site: https://coralcanadawide.com/) — 30, 2150 29 Street NE, Calgary, Alberta, Canada, T1Y 7G4 | GST/HST number not public ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Energy Safety Canada | D2L
- **invoice_card_json**: {"bill_to": {"legal_name": "ENERGY SAFETY CANADA (as registered: Corporations Canada (open data), corporation number 10340871, 2026-11-08)", "legal_name_is_published": true, "address": "150 - 2 Smed Lane SE, Calgary, AB, T2C 4T5, CA (schema.org JSON-LD PostalAddress on https://www.energysafetycanada.com/)", "address_is_the_invoice_address": false, "tax_number": "825722879 (Corporations Canada (open data), corporation number 10340871, 2026-11-08)", "language": "en"}, "submit_to": {"email": "accounting@energysafetycanada.com", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": "Docusign Envelope ID: AEE04535-9B2E-4491-9BE6-AA985DBE9672 ENERGY SAFETY CANADA Statemen (as printed on https://www.energysafetycanada.com/sites/default/files/2026-04/Energy-Safety-Canada-Annual-Financial-Statements-2024.pdf, re-read 2026-11-08)"}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their", "buyer_tax_status
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number
- **ap_grade**: C
- **ap_score**: 61
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["accounting@energysafetycanada.com (finance/accounting dept or supplier-payment office)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://www.energysafetycanada.com/contact-us", "quote: \"d grow leading-5 min-h-0 lg:min-h-px min-w-px relative shrink-0 text-sm text-brand-primary underline break-words\" aria-label=\"Send email to Accounting@EnergySaf\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-01649"], "buyer_facts": ["address and phone: the buyer's own site, https://www.energysafetycanada.com/contact-us (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "phone / role e-mails / logo: the vendor's own site, https://coralcanadawide.com/contact-us/ (tools/org_contacts.py, org_extras.py)", "website: https://coralcanadawi

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.energysafetycanada.com/contact-us | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, energysafetycanada.com)
- **status**: ok
- **pages**: 5
- **language**: en
- **logo_url**: https://www.energysafetycanada.com/themes/custom/esc/logo.svg
- **logo_basis**: logo image on the site
- **domain**: energysafetycanada.com
- **key**: lead:288361125e71bc1f
- **name**: energysafetycanada.com
- **website**: https://energysafetycanada.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Energy Safety Canada
- **jsonld_address**: 150 - 2 Smed Lane SE, Calgary, AB, T2C 4T5, CA
- **jsonld_phone**: 1-800-667-5557
- **jsonld_logo**: https://www.energysafetycanada.com/themes/custom/esc/logo.svg
- **jsonld_url**: https://www.energysafetycanada.com/
- **jsonld_same_as**: https://www.linkedin.com/company/energy-safety-canada/; https://www.youtube.com/@energysafetycanada1628/
- **jsonld_quote**: { "@context": "https://schema.org", "@graph": [ { "@type": "Organization", "@id": "https://www.energysafetycanada.com/#organization", "description": "Energy Safety Canada - Providing safety training, certification, and resources for the energy industry across Canada.", "sameAs": [ "https://www.linke
- **jsonld_page**: https://www.energysafetycanada.com/
- **legal_name_stated**: Energy Safety Canada
- **legal_name_stated_url**: https://www.energysafetycanada.com/about-us
- **legal_name_stated_quote**: About Us | Energy Safety Canada Skip to main content About Us Certificate Validation News & Events Store DACC/IRPs Cart 0 Learners
- **mentions**: {'payment_method': {'text': 'interact with Energy Safety Canada, such as when you visit our Site or when you purchas', 'url': 'https://www.energysafetycanada.com/legal', 'quote': 'e, and disclosure of personal information that may be collected by Energy Safety Canada anytime you interact with Energy Safety Canada, such as when you visit our Site or when you purchase Energy Safety Canada products and services. Your privacy is a priority.'}}
- **linkedin_url**: https://www.linkedin.com/company/energy-safety-canada/
- **tel_links**: 1-250-794-0100; 1-855-436-3676; 1-800-667-5557 ext.6; 1-306-842-9822; 1-877-336-3676; 1-403-516-8000; 1-800-667-5557; 1-

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "150 - 2 Smed Lane SE, Calgary, AB, T2C 4T5", "address_country": "CA", "address_url": "https://www.energysafetycanada.com/contact-us", "address_method": "json-ld", "address_quote": "See Details Calgary Head Office Location 150 - 2 Smed Lane SE Calgary, Alberta, T2C 4T5 Contact 403-516-8000 1-800-667-5557 Nisku Location 1803 - 11th St Nisku, Albert", "phone": "1-800-667-5557", "phone_url": "https://www.energysafetycanada.com/contact-us", "emails": "accounting@energysafetycanada.com; customerservice@energysafetycanada.com", "emails_url": "https://www.energysafetycanada.com/contact-us", "domain": "energysafetycanada.com", "key": "lead:288361125e71bc1f", "name": "energysafetycanada.com", "website": "https://energysafetycanada.com/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, coralcanadawide.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: Coral Canada Wide Ltd
- **legal_name_url**: https://coralcanadawide.com/
- **legal_name_quote**: Coral Canada Wide Ltd. – Commercial HVAC-R EN | FR For 24/7 Service Anywhere In Canada, Please Call 1-800-380-8008 Get an
- **logo_url**: https://coralcanadawide.com/wp-content/uploads/2020/07/logo.png
- **logo_basis**: logo image in the site header
- **domain**: coralcanadawide.com
- **key**: vendor:Martell Refrigeration & Air Conditioning
- **name**: Martell Refrigeration & Air Conditioning
- **website**: https://coralcanadawide.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **tel_links**: 1-800-380-8008

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "30, 2150 29 Street NE, Calgary, Alberta, Canada, T1Y 7G4", "address_country": "CA", "address_url": "https://coralcanadawide.com/contact-us/", "address_method": "pattern", "address_quote": "Office Coral Canada Wide Ltd. #30, 2150 29 Street NE, Calgary, Alberta, Canada, T1Y 7G4 Eastern Regional Office Coral Canada Wide Ltd. Unit #1, 41 Horner Avenue, Etobi", "phone": "1-800-380-8008", "phone_url": "https://coralcanadawide.com/contact-us/", "emails": "info@coralcanadawide.com", "emails_url": "https://coralcanadawide.com/contact-us/", "domain": "coralcanadawide.com", "key": "vd:coralcanadawide.com", "name": "Martell Refrigeration & Air Conditioning", "website": "https://coralcanadawide.com/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | api_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Energy Safety Canada | found | ENERGY SAFETY CANADA | 825722879 | corporation number 10340871 | Corporations Canada (open data) | Canada Not-for-profit Corporations Act | Active | 2017-09-30 | Calgary | AB | 250 2 Street Southwest, Suite 1000, Calgary, AB, T2P 0C1 | https://open.canada.ca/data/en/dataset/0032ce54-c5dd-4b66-99a0-320a7b5e99f2 | 2026-11-08 |

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Martell Refrigeration & Air Conditioning |  |  |  |  |  |  |  |  |  |  |
| v | Coral Canada Wide Ltd |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:288361125e71bc1f",
 "ap_contact_team": {
  "emails": [
   "accounting@energysafetycanada.com"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "accounting@energysafetycanada.com",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.energysafetycanada.com/contact-us",
    "quote": "d grow leading-5 min-h-0 lg:min-h-px min-w-px relative shrink-0 text-sm text-brand-primary underline break-words\" aria-label=\"Send email to Accounting@EnergySafetyCanada.com\"> <span class=\"__cf_email__\" data-cfemail=\"adeccecec2d8c3d9c4c3caede8c3c8dfcad4fecccbc8d9d4eeccc3ccc9cc83cec2c0\">[em",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "energysafetycanada.com",
    "task_id": "CL-LD-01649"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of energysafetycanada.com (15 pages, robots.txt respected), no AI, no search engine"
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

- the vendor's GST/HST number (BN9)
- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
