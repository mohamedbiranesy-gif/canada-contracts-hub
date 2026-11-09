# S3-32 — The Branding Firm Inc ⇄ Forever Homes Inc.

Stratum: **S3_routed_public_body_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: The Branding Firm Inc — 1108 Dundas St Suite 100, London ON N5W 3A7 — buyer tax no. 787845726 (Canada's Business Registries, ON 2500805, 2026-11-08)
SUBMIT TO: info@thebrandingfirminc.com (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: FOREVER HOMES INC. (as registered: Canada's Business Registries, ON 1016780, 2026-11-08) — 1956 Mallard Road, London, ON, N6H5M1, Canada | GST/HST 136506847 (Canada's Business Registries, ON 1016780, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Past Communities | Quality Homes in London, Ontario
```

## Relationship
- **rank_group**: E1
- **data_quality_score**: 40
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: The Branding Firm Inc (company (private sector), jurisdiction not stated) — linked from the Canada-located vendor's site (weakest listed relationship): Forever Homes Inc. | subject: Past Communities | Quality Homes in London, Ontario | published by: the Canada-located vendor's own website | record: https://www.foreverhomes.ca/past-communities/ | vendor in Canada because: vendor located in Canada (v)=foreverhomes.ca | status rule: linked from a page of the Canada-located vendor's site (not a client page)
- **how_relationship_was_found**: tools/provider_mentions.py / news_match.py found the buyer linked from the vendor's own site or release
- **keys**: lead:c1ab8ef02bb71381
- **tier**: E
- **grade**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: The Branding Firm Inc
- **buyer_website**: https://thebrandingfirminc.com/
- **buyer_address**: 1108 Dundas St Suite 100, London ON N5W 3A7
- **buyer_phone**: (519) 914-2810
- **buyer_contact_evidence_url**: https://thebrandingfirminc.com/contact/
- **buyer_legal_name_as_published**: The Branding Firm Inc
- **buyer_bn_as_published**: 787845726 (Canada's Business Registries, ON 2500805, 2026-11-08)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 787845726RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_logo_url**: https://thebrandingfirminc.com/wp-content/uploads/2025/05/DWD-Logo.svg
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://ca.linkedin.com/company/thebrandingfirminc
- **buyer_registry_id**: 2500805 (ON; https://ised-isde.canada.ca/cbr-rec/en/search?q=The%20Branding%20Firm%20Inc)
- **buyer_type**: company (private sector)
- **buyer_sector**: private sector
- **buyer_legal_form**: ONTARIO BUSINESS CORP. (Canada's Business Registries, ON 2500805, 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://thebrandingfirminc.com/contact/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: info@thebrandingfirminc.com
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://thebrandingfirminc.com/
- **email_evidence_quote**: cdn-cgi/l/email-protection#b2dbdcd4ddf2c6dad7d0c0d3dcd6dbdcd5d4dbc0dfdbdcd19cd1dddf" target="_self" data-type="url" aria-label="Email us at info@thebrandingfirminc.com"> <span class="__cf_email__" data-cfemail="4a23242c250a3e222f28382b242e23242d2c23382723242964292527">[email protected]</sp
- **mailbox_provenance**: info@thebrandingfirminc.com (general) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://thebrandingfirminc.com/ | quote: "cdn-cgi/l/email-protection#b2dbdcd4ddf2c6dad7d0c0d3dcd6dbdcd5d4dbc0dfdbdcd19cd1dddf" target="_self" data-type="url" aria-label="Email us at info@thebrandingfirm" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-02263
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none;
- **dmarc_record_domain**: thebrandingfirminc.com
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 include:spf.protection.outlook.com -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: The Branding Firm Inc — 1108 Dundas St Suite 100, London ON N5W 3A7 — buyer tax no. 787845726 (Canada's Business Registries, ON 2500805, 2026-11-08) ⏎ SUBMIT TO: info@thebrandingfirminc.com (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: FOREVER HOMES INC. (as registered: Canada's Business Registries, ON 1016780, 2026-11-08) — 1956 Mallard Road, London, ON, N6H5M1, Canada | GST/HST 136506847 (Canada's Business Registries, ON 1016780, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Past Communities | Quality Homes in London, Ontario
- **invoice_card_json**: {"bill_to": {"legal_name": "The Branding Firm Inc", "legal_name_is_published": true, "address": "1108 Dundas St Suite 100, London ON N5W 3A7", "address_is_the_invoice_address": false, "tax_number": "787845726 (Canada's Business Registries, ON 2500805, 2026-11-08)", "language": "en"}, "submit_to": {"email": "info@thebrandingfirminc.com", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 13% (Ontario)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "136506847RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "FOREVER HOMES INC. (as registered: Canada's Business Registries, ON 1016780, 2026-11-08)", "bn9": "136506847 (Canada's Business Registries, ON 1016780, 2026-11-08)", "ne
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
- **vendor**: Forever Homes Inc.
- **vendor_legal_name**: FOREVER HOMES INC. (as registered: Canada's Business Registries, ON 1016780, 2026-11-08)
- **vendor_registry_id**: 1016780 (ON)
- **vendor_registry_url**: https://ised-isde.canada.ca/cbr-rec/en/search?q=Forever%20Homes%20Inc.
- **vendor_registered_address**: London, Ontario (registered office city / province; Canada's Business Registries, ON 1016780, 2026-11-08)
- **vendor_legal_form**: ONTARIO BUSINESS CORP. (Canada's Business Registries, ON 1016780, 2026-11-08)
- **vendor_address**: 1956 Mallard Road, London, ON, N6H5M1, Canada
- **vendor_country_basis**: vendor located in Canada (v)=foreverhomes.ca
- **vendor_bn9**: 136506847 (Canada's Business Registries, ON 1016780, 2026-11-08)
- **vendor_gst_hst_derived**: 136506847RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://www.foreverhomes.ca/
- **vendor_emails**: info@foreverhomes.ca
- **vendor_phone**: 519-686-3075
- **vendor_contact_evidence_url**: https://www.foreverhomes.ca/contact/
- **vendor_logo_url**: https://www.foreverhomes.ca/wp-content/uploads/2026/02/Trademarked-FH-Logo.svg
- **vendor_website_status**: site answers
- **vendor_linkedin_url**: https://ca.linkedin.com/company/forever-homes
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); registry identity: 1016780 (ON) status Active — incorporated (Canada's Business Registries, ON 1016780, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: registry: Canada's Business Registries, ON 1016780, 2026-11-08; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 1993-03-30; phone / role e-mails / logo: the vendor's own site, https://www.foreverhomes.ca/contact/ (tools/org_contacts.py, org_extras.py); website: https://www.foreverhomes.ca/ (site answers)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Active — incorporated (Canada's Business Registries, ON 1016780, 2026-11-08)
- **vendor_incorporation_date**: 1993-03-30
- **vendor_years_in_business**: 33.6 (since 1993-03-30, registry date)
- **vendor_bn_source**: registry: Canada's Business Registries, ON 1016780, 2026-11-08

## Contract
- **contract_status**: linked from a page of the Canada-located vendor's site (not a client page)
- **contract_title**: Past Communities | Quality Homes in London, Ontario
- **contract_description**: Past Communities | Quality Homes in London, Ontario (the record's title; the source publishes no separate description)
- **contract_link**: https://www.foreverhomes.ca/past-communities/
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 2
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 787845726RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: HST 13% (Ontario) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 136506847RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: The Branding Firm Inc — 1108 Dundas St Suite 100, London ON N5W 3A7 — buyer tax no. 787845726 (Canada's Business Registries, ON 2500805, 2026-11-08) ⏎ SUBMIT TO: info@thebrandingfirminc.com (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: FOREVER HOMES INC. (as registered: Canada's Business Registries, ON 1016780, 2026-11-08) — 1956 Mallard Road, London, ON, N6H5M1, Canada | GST/HST 136506847 (Canada's Business Registries, ON 1016780, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Past Communities | Quality Homes in London, Ontario
- **invoice_card_json**: {"bill_to": {"legal_name": "The Branding Firm Inc", "legal_name_is_published": true, "address": "1108 Dundas St Suite 100, London ON N5W 3A7", "address_is_the_invoice_address": false, "tax_number": "787845726 (Canada's Business Registries, ON 2500805, 2026-11-08)", "language": "en"}, "submit_to": {"email": "info@thebrandingfirminc.com", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 13% (Ontario)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "136506847RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "FOREVER HOMES INC. (as registered: Canada's Business Registries, ON 1016780, 2026-11-08)", "bn9": "136506847 (Canada's Business Registries, ON 1016780, 2026-11-08)", "ne
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["info@thebrandingfirminc.com (general)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://thebrandingfirminc.com/", "quote: \"cdn-cgi/l/email-protection#b2dbdcd4ddf2c6dad7d0c0d3dcd6dbdcd5d4dbc0dfdbdcd19cd1dddf\" target=\"_self\" data-type=\"url\" aria-label=\"Email us at info@thebrandingfirm\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-02263"], "buyer_facts": ["address and phone: the buyer's own site, https://thebrandingfirminc.com/contact/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "registry identity: 1016780 (ON) status Active — incorporated (Canada's Business Registries, ON 1016780, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook 

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://thebrandingfirminc.com/ | 2026-11-06 | http_0 |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, thebrandingfirminc.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: The Branding Firm Inc
- **legal_name_url**: https://thebrandingfirminc.com/
- **legal_name_quote**: Marketing Campaigns Experience Design Strategic Consulting Web Development Content Creation © 2026 The Branding Firm Inc. Privacy Policy Terms & Conditions Site Map Accessibility About The Branding Firm Inc. The Branding
- **logo_url**: https://thebrandingfirminc.com/wp-content/uploads/2025/05/DWD-Logo.svg
- **logo_basis**: logo image on the site
- **domain**: thebrandingfirminc.com
- **key**: lead:c1ab8ef02bb71381
- **name**: The Branding Firm Inc
- **website**: https://thebrandingfirminc.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: The Branding Firm Inc
- **jsonld_logo**: https://thebrandingfirminc.com/wp-content/uploads/2024/04/TBF_Logo_Black.png
- **jsonld_url**: https://thebrandingfirminc.com/
- **jsonld_same_as**: https://www.facebook.com/thebrandingfirminc/; https://www.instagram.com/thebrandingfirminc/; https://ca.linkedin.com/company/the-branding-firm-inc
- **jsonld_quote**: {"@context":"https:\/\/schema.org","@graph":[{"@type":"WebPage","@id":"https:\/\/thebrandingfirminc.com\/","url":"https:\/\/thebrandingfirminc.com\/","name":"The Branding Firm | Boutique Marketing Agency | London, Ontario","isPartOf":{"@id":"https:\/\/thebrandingfirminc.com\/#website"},"about":{"@id
- **jsonld_page**: https://thebrandingfirminc.com/
- **legal_name_stated**: Canada’s Anti-Spam laws
- **legal_name_stated_url**: https://thebrandingfirminc.com/privacy-policy/
- **legal_name_stated_quote**: y information during any electronic exchange. The Branding Firm will endeavour to be compliant with Canada’s Anti-Spam laws (“CASL”) in the company’s commercial electronic communication with you. Should you fail to provide
- **mentions**: {'payment_method': {'text': 'interactions and contributions to our clients, our team and the communities we proudly', 'url': 'https://thebrandingfirminc.com/', 'quote': 'respect for each other’s talents, and an unwavering dedication to providing positive and inclusive interactions and contributions to our clients, our team and the communities we proudly serve. Professional development is integral to who we are, as our industr'}}
- **linkedin_url**: https://ca.linkedin.com/company/thebrandingfirminc
- **tel_links**: 5199142810; +15199142810

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "1108 Dundas St Suite 100, London ON N5W 3A7", "address_country": "CA", "address_url": "https://thebrandingfirminc.com/contact/", "address_method": "pattern", "address_quote": "connecting. 519-914-2810 [email protected] 1108 Dundas St Suite 100, London ON N5W 3A7 Contact Us Name * Email * Phone * Message * Submit If you are human, leave this", "phone": "(519) 914-2810", "phone_url": "https://thebrandingfirminc.com/contact/", "emails": "info@thebrandingfirminc.com", "emails_url": "https://thebrandingfirminc.com/contact/", "domain": "thebrandingfirminc.com", "key": "lead:c1ab8ef02bb71381", "name": "thebrandingfirminc.com", "website": "https://thebrandingfirminc.com/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, foreverhomes.ca)
- **status**: ok
- **pages**: 4
- **language**: en
- **logo_url**: https://www.foreverhomes.ca/wp-content/uploads/2026/02/Trademarked-FH-Logo.svg
- **logo_basis**: logo image in the site header
- **domain**: foreverhomes.ca
- **key**: vendor:Forever Homes Inc.
- **name**: Forever Homes Inc.
- **website**: https://foreverhomes.ca/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Forever Homes Inc
- **jsonld_logo**: https://www.foreverhomes.ca/#/schema/logo/image/
- **jsonld_url**: https://www.foreverhomes.ca/
- **jsonld_same_as**: https://www.facebook.com/foreverhomeslondon/; https://www.instagram.com/foreverhomesinc/; https://ca.linkedin.com/company/forever-homes
- **jsonld_quote**: {"@context":"https:\/\/schema.org","@graph":[{"@type":"WebPage","@id":"https:\/\/www.foreverhomes.ca\/","url":"https:\/\/www.foreverhomes.ca\/","name":"Townhomes for Rent | London Ontario | Townhouse Rentals","isPartOf":{"@id":"https:\/\/www.foreverhomes.ca\/#website"},"about":{"@id":"https:\/\/www.
- **jsonld_page**: https://www.foreverhomes.ca/
- **legal_name_stated**: Canada Revenue Agency
- **legal_name_stated_url**: https://www.foreverhomes.ca/privacy-policy/
- **legal_name_stated_quote**: . From time to time, we may be required to collect information directly from third parties such as: Canada Revenue Agency (CRA), or other government agency or registry or third parties with whom you have had or have a pro
- **linkedin_url**: https://ca.linkedin.com/company/forever-homes
- **tel_links**: 519-686-3075

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "address": "1956 Mallard Rd, London, ON , N6H 5M1", "address_country": "CA", "address_url": "https://www.foreverhomes.ca/contact/", "address_method": "pattern", "address_quote": "y Contact Us Built With Heart And Skill Visit us at 1956 Mallard Rd, London, ON N6H 5M1 Call us at 519-686-3075 Email us at info@foreverhomes.ca Contact Forever Homes", "phone": "519-686-3075", "phone_url": "https://www.foreverhomes.ca/contact/", "emails": "info@foreverhomes.ca", "emails_url": "https://www.foreverhomes.ca/contact/", "domain": "foreverhomes.ca", "key": "vd:foreverhomes.ca", "name": "Forever Homes Inc.", "website": "https://foreverhomes.ca/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | The Branding Firm Inc | found | THE BRANDING FIRM INC. | 787845726 | 2500805 | ON | ONTARIO BUSINESS CORP. | Active | 2016-01-19 | LONDON | Ontario |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=The%20Branding%20Firm%20Inc | 2026-11-08 |
| buyer | Forever Homes Inc. | found | FOREVER HOMES INC. | 136506847 | 1016780 | ON | ONTARIO BUSINESS CORP. | Active | 1993-03-30 | London | Ontario |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Forever%20Homes%20Inc. | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | The Branding Firm Inc |  |  |  |  |  |  |  |  |  |  |
| b | Forever Homes Inc. |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:c1ab8ef02bb71381",
 "ap_contact_team": {
  "emails": [
   "info@thebrandingfirminc.com"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "info@thebrandingfirminc.com",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://thebrandingfirminc.com/",
    "quote": "cdn-cgi/l/email-protection#b2dbdcd4ddf2c6dad7d0c0d3dcd6dbdcd5d4dbc0dfdbdcd19cd1dddf\" target=\"_self\" data-type=\"url\" aria-label=\"Email us at info@thebrandingfirminc.com\"> <span class=\"__cf_email__\" data-cfemail=\"4a23242c250a3e222f28382b242e23242d2c23382723242964292527\">[email protected]</sp",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "thebrandingfirminc.com",
    "task_id": "CL-LD-02263"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of thebrandingfirminc.com (8 pages, robots.txt respected), no AI, no search engine"
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

## The vendor's other buyers in the dataset (first 60 of 1)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_bidsandtenders:f89c0af7-7f8b-4365-8eef-efb837518769:8 | City of London | Affordable Housing Development Partners - Year 2 |  |  |  | https://london.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/f89c0af7-7f8b-4365-8eef-efb837518769 |

## Open questions for hand research (layer 2)

- an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed)
- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
