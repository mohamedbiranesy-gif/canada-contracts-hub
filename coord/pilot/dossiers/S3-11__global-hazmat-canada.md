# S3-11 — Global Hazmat Canada ⇄ Firstpage Marketing

Stratum: **S3_routed_public_body_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Global Hazmat Canada (schema.org JSON-LD Organization name on https://www.globalhazmat.com/) — PO Box 31046, Luckakuck PO Chilliwack, BC V2R 0C4
SUBMIT TO: info@globalhazmat.com (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: FIRSTPAGE MARKETING INC. (as registered: Canada's Business Registries, BC BC0789655, 2026-11-08) — 34334 Forrest Terrace #300, Abbotsford, BC, V2S 1G7 | GST/HST 851481796 (Canada's Business Registries, BC BC0789655, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Client Testimonials - FirstPage Marketing
```

## Relationship
- **rank_group**: D1
- **data_quality_score**: 42
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Global Hazmat Canada (organisation (type not stated in the record), jurisdiction not stated) — named as a client by the Canada-located vendor (client list / customer story), dated: Firstpage Marketing | subject: Client Testimonials - FirstPage Marketing | published by: the Canada-located vendor's own website | record: https://firstpagemarketing.com/company/testimonials/ | vendor in Canada because: vendor located in Canada (osm)=firstpagemarketing.com | status rule: client listing on the vendor's own site (undated)
- **how_relationship_was_found**: tools/client_lists.py / dated_stories.py read the vendor's dated customer story / case study naming the buyer
- **keys**: lead:075315a57a19e87e
- **tier**: D
- **grade**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: Global Hazmat Canada
- **buyer_website**: https://globalhazmat.com/
- **buyer_address**: PO Box 31046, Luckakuck PO Chilliwack, BC V2R 0C4
- **buyer_phone**: 1-877-744-4999
- **buyer_contact_evidence_url**: https://www.globalhazmat.com/locations/
- **buyer_legal_name_as_published**: Global Hazmat Canada (schema.org JSON-LD Organization name on https://www.globalhazmat.com/)
- **buyer_logo_url**: https://www.globalhazmat.com/wp-content/uploads/2026/07/logo.webp
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/global-hazmat/
- **buyer_type**: organisation (type not stated in the record)
- **buyer_sector**: not stated
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.globalhazmat.com/locations/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: info@globalhazmat.com
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://www.globalhazmat.com/us/contact-us/
- **email_evidence_quote**: ll 1-877-744-4999 . We will be happy to discuss your needs and provide more information about our services. Call Us 1-877-744-4999 Email Us info@globalhazmat.com Connect with us Follow us on social media for the latest industry news, safety tips, and updates. Help us serve you better. Scan
- **email_evidence_context**: uctors are among the most highly qualified in the industry. Please complete the form below to contact us or call 1-877-744-4999 . We will be happy to discuss your needs and provide more information about our services. Call Us 1-877-744-4999 Email Us info@globalhazmat.com Connect with us Follow us on social media for the latest industry news, safety tips, and updates. Help us serve you better. Scan the QR code to share your thoughts on Google. We appreciate your honest feedback! Send us a message How can we help? We’ (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: info@globalhazmat.com (general) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-01 | page: https://www.globalhazmat.com/us/contact-us/ | quote: "ll 1-877-744-4999 . We will be happy to discuss your needs and provide more information about our services. Call Us 1-877-744-4999 Email Us info@globalhazmat.co" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00130
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1;p=none;sp=reject;adkim=r;aspf=r;pct=100;fo=0;rf=afrf;ri=86400;ruf=mailto:michelle@globalhazmat.com
- **dmarc_record_domain**: globalhazmat.com
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 a mx include:_spf.elasticemail.com include:spf.protection.outlook.com include:servers.mcsv.net include:amazonses.com -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Global Hazmat Canada (schema.org JSON-LD Organization name on https://www.globalhazmat.com/) — PO Box 31046, Luckakuck PO Chilliwack, BC V2R 0C4 ⏎ SUBMIT TO: info@globalhazmat.com (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: FIRSTPAGE MARKETING INC. (as registered: Canada's Business Registries, BC BC0789655, 2026-11-08) — 34334 Forrest Terrace #300, Abbotsford, BC, V2S 1G7 | GST/HST 851481796 (Canada's Business Registries, BC BC0789655, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Client Testimonials - FirstPage Marketing
- **invoice_card_json**: {"bill_to": {"legal_name": "Global Hazmat Canada (schema.org JSON-LD Organization name on https://www.globalhazmat.com/)", "legal_name_is_published": true, "address": "PO Box 31046, Luckakuck PO Chilliwack, BC V2R 0C4", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "info@globalhazmat.com", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (BC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "851481796RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "FIRSTPAGE MARKETING INC. (as registered: Canada's Business Registries, BC BC0789655, 2026-11-08)", "bn9": "851481796 (Canada's Business Registries, BC BC0789655, 2026-1
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: Firstpage Marketing
- **vendor_legal_name**: FIRSTPAGE MARKETING INC. (as registered: Canada's Business Registries, BC BC0789655, 2026-11-08)
- **vendor_registry_id**: BC0789655 (BC)
- **vendor_registry_url**: https://ised-isde.canada.ca/cbr-rec/en/search?q=Firstpage%20Marketing
- **vendor_registered_address**: Abbotsford, BC (registered office city / province; Canada's Business Registries, BC BC0789655, 2026-11-08)
- **vendor_legal_form**: BC Company (Canada's Business Registries, BC BC0789655, 2026-11-08)
- **vendor_address**: 34334 Forrest Terrace #300, Abbotsford, BC, V2S 1G7
- **vendor_country_basis**: vendor located in Canada (osm)=firstpagemarketing.com
- **vendor_bn9**: 851481796 (Canada's Business Registries, BC BC0789655, 2026-11-08)
- **vendor_gst_hst_derived**: 851481796RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://firstpagemarketing.com
- **vendor_phone**: +1-604-866-2230
- **vendor_contact_evidence_url**: https://firstpagemarketing.com/company/contact-us/
- **vendor_logo_url**: https://firstpagemarketing.com/wp-content/uploads/2025/03/Logo_CLR_Rev.svg
- **vendor_website_status**: site answers
- **vendor_linkedin_url**: https://ca.linkedin.com/company/firstpage-marketing
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); registry identity: BC0789655 (BC) status Active (Canada's Business Registries, BC BC0789655, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: registry: Canada's Business Registries, BC BC0789655, 2026-11-08; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2007-04-30; phone / role e-mails / logo: the vendor's own site, https://firstpagemarketing.com/company/contact-us/ (tools/org_contacts.py, org_extras.py); website: https://firstpagemarketing.com (site answers)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Active (Canada's Business Registries, BC BC0789655, 2026-11-08)
- **vendor_incorporation_date**: 2007-04-30
- **vendor_years_in_business**: 19.5 (since 2007-04-30, registry date)
- **vendor_bn_source**: registry: Canada's Business Registries, BC BC0789655, 2026-11-08

## Contract
- **contract_status**: client listing on the vendor's own site (undated)
- **contract_title**: Client Testimonials - FirstPage Marketing
- **contract_description**: Client Testimonials - FirstPage Marketing (the record's title; the source publishes no separate description)
- **contract_link**: https://firstpagemarketing.com/company/testimonials/
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (BC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 851481796RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Global Hazmat Canada (schema.org JSON-LD Organization name on https://www.globalhazmat.com/) — PO Box 31046, Luckakuck PO Chilliwack, BC V2R 0C4 ⏎ SUBMIT TO: info@globalhazmat.com (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: FIRSTPAGE MARKETING INC. (as registered: Canada's Business Registries, BC BC0789655, 2026-11-08) — 34334 Forrest Terrace #300, Abbotsford, BC, V2S 1G7 | GST/HST 851481796 (Canada's Business Registries, BC BC0789655, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Client Testimonials - FirstPage Marketing
- **invoice_card_json**: {"bill_to": {"legal_name": "Global Hazmat Canada (schema.org JSON-LD Organization name on https://www.globalhazmat.com/)", "legal_name_is_published": true, "address": "PO Box 31046, Luckakuck PO Chilliwack, BC V2R 0C4", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "info@globalhazmat.com", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (BC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "851481796RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "FIRSTPAGE MARKETING INC. (as registered: Canada's Business Registries, BC BC0789655, 2026-11-08)", "bn9": "851481796 (Canada's Business Registries, BC BC0789655, 2026-1
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["info@globalhazmat.com (general)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-01", "page: https://www.globalhazmat.com/us/contact-us/", "quote: \"ll 1-877-744-4999 . We will be happy to discuss your needs and provide more information about our services. Call Us 1-877-744-4999 Email Us info@globalhazmat.co\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00130"], "buyer_facts": ["address and phone: the buyer's own site, https://www.globalhazmat.com/locations/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "registry identity: BC0789655 (BC) status Active (Canada's Business Registries, BC BC0789655, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data", "match)", "BN9: registry: Canada's Business Registries, BC BC0789655, 2026-11-08", "GST/HST derived BN9 + RT0001 (CRA registry is CAPT

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.globalhazmat.com/us/contact-us/ | 2026-11-08 | ok |  |  |  | 1-877-744-4999 |  |  |  |  |  |

## Buyer site facts (org_extras, globalhazmat.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://www.globalhazmat.com/wp-content/uploads/2026/07/logo.webp
- **logo_basis**: logo image in the site header
- **domain**: globalhazmat.com
- **key**: lead:075315a57a19e87e
- **name**: globalhazmat.com
- **website**: https://globalhazmat.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Global Hazmat Canada
- **jsonld_logo**: https://www.globalhazmat.com/wp-content/uploads/2026/07/logo.webp
- **jsonld_url**: https://www.globalhazmat.com/
- **jsonld_quote**: {"@context":"https:\/\/schema.org","@graph":[{"@type":"WebPage","@id":"https:\/\/www.globalhazmat.com\/","url":"https:\/\/www.globalhazmat.com\/","name":"TDG, Hazmat & WHMIS Compliance Training & Services | Global Hazmat","isPartOf":{"@id":"https:\/\/www.globalhazmat.com\/#website"},"about":{"@id":"
- **jsonld_page**: https://www.globalhazmat.com/
- **legal_name_stated**: Elgin College
- **legal_name_stated_url**: https://www.globalhazmat.com/about-us/
- **legal_name_stated_quote**: g dangerous goods, hazmat and hazardous waste. Kevin has a background in Environmental Science from Elgin College (Illinois), is a certified instructor for all modes of transportation of dangerous goods, CDGP (Cer
- **mentions**: {'payment_method': {'text': 'interactive training classes from our facility to yours using video conferencing and li', 'url': 'https://www.globalhazmat.com/', 'quote': 'health and safety requirements. Company Specific Webinar Company-specific, instructor led and fully interactive training classes from our facility to yours using video conferencing and live communication with the highest level of technology available. Consulti'}}
- **linkedin_url**: https://www.linkedin.com/company/global-hazmat/
- **tel_links**: 1-877-744-4999;; 18777444999; 1-877-744-4999

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "phone": "1-877-744-4999", "phone_url": "https://www.globalhazmat.com/contact-us/", "emails": "info@globalhazmat.com", "emails_url": "https://www.globalhazmat.com/contact-us/", "address": "PO Box 31046, Luckakuck PO Chilliwack, BC V2R 0C4", "address_country": "CA", "address_url": "https://www.globalhazmat.com/locations/", "address_method": "pattern", "address_quote": "ming soon Canada MAILING ADDRESS - BC PO Box 31046, Luckakuck PO Chilliwack, BC V2R 0C4 BRITISH COLUMBIA Surrey ALBERTA Calgary - Coming soon ONTARIO Toronto - Coming", "domain": "globalhazmat.com", "key": "lead:075315a57a19e87e", "name": "globalhazmat.com", "website": "https://globalhazmat.com/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, firstpagemarketing.com)
- **status**: ok
- **pages**: 4
- **language**: en
- **logo_url**: https://firstpagemarketing.com/wp-content/uploads/2025/03/Logo_CLR_Rev.svg
- **logo_basis**: logo image on the site
- **domain**: firstpagemarketing.com
- **key**: vendor:Firstpage Marketing
- **name**: Firstpage Marketing
- **website**: https://firstpagemarketing.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: FirstPage Marketing
- **jsonld_logo**: https://firstpagemarketing.com/wp-content/uploads/2025/12/FPM_LogoTagline_CLR.png
- **jsonld_url**: https://firstpagemarketing.com/
- **jsonld_quote**: { "@context": "https://schema.org", "@graph": [ { "@type": "Organization", "@id": "https://firstpagemarketing.com/#organization", "name": "FirstPage Marketing", "url": "https://firstpagemarketing.com/", "logo": "https://firstpagemarketing.com/images/FPM_Logo_Wht.png", "sameAs": [ "https://www.instag
- **jsonld_page**: https://firstpagemarketing.com/
- **mentions**: {'payment_method': {'text': 'interact with our website through behavioral metrics, heatmaps, and session replay to i', 'url': 'https://firstpagemarketing.com/privacy-policy/', 'quote': 'information. We partner with Microsoft Clarity and Microsoft Advertising to capture how you use and interact with our website through behavioral metrics, heatmaps, and session replay to improve and market our products/services. Website usage data is captured u'}}
- **linkedin_url**: https://ca.linkedin.com/company/firstpage-marketing
- **tel_links**: 6048662230; 6048708673; 604-866-2230

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "34334 Forrest Terrace #300, Abbotsford, BC, V2S 1G7", "address_country": "CA", "address_url": "https://firstpagemarketing.com/company/contact-us/", "address_method": "json-ld", "address_quote": "otsford Office 604-866-2230 Address: 34334 Forrest Terrace #300, Abbotsford, BC V2S 1G7 Monday – Friday: 8:30 pm to 4:30 pm Chilliwack Office 604-866-2230 Address: 846", "phone": "+1-604-866-2230", "phone_url": "https://firstpagemarketing.com/company/contact-us/", "domain": "firstpagemarketing.com", "key": "vd:firstpagemarketing.com", "name": "Firstpage Marketing", "website": "https://firstpagemarketing.com/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| v | Firstpage Marketing |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:075315a57a19e87e",
 "ap_contact_team": {
  "emails": [
   "info@globalhazmat.com"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "info@globalhazmat.com",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.globalhazmat.com/",
    "quote": "nt Materials are also available, additional charges apply) Register 1-877-744-4999 *Tax is additional. Course outline available on request: info@globalhazmat.com What We Do We provide certified hazmat services focused on safety, compliance, and reliability. Our expert team ensures all mate",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "globalhazmat.com",
    "task_id": "CL-LD-08331"
   },
   {
    "email": "info@globalhazmat.com",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.globalhazmat.com/us/contact-us/",
    "quote": "ll 1-877-744-4999 . We will be happy to discuss your needs and provide more information about our services. Call Us 1-877-744-4999 Email Us info@globalhazmat.com Connect with us Follow us on social media for the latest industry news, safety tips, and updates. Help us serve you better. Scan",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "globalhazmat.com",
    "task_id": "CL-WS-00130"
   }
  ]
 },
 "research_status": {
  "found": 2
 },
 "queries_tried": [
  "site crawl of globalhazmat.com (25 pages, robots.txt respected), no AI, no search engine",
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

- an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed)
- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
