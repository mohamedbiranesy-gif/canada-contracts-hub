# S3-45 — Technicore Ltd ⇄ PM ERA Inc.

Stratum: **S3_routed_public_body_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Technicore Ltd — 102 Bales Dr E, Newmarket, Ontario, L3Y 8K3, Canada (schema.org JSON-LD PostalAddress on https://technicore.ca/)
SUBMIT TO: info@technicore.ca (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: PM ERA INC. (as registered: Canada's Business Registries, ON 2299303, 2026-11-08) — 5000 Yonge Street,, North York, ON, M2N 7E9, Canada | GST/HST 800435315 (Canada's Business Registries, ON 2299303, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Technicore Ltd (company (private sector), jurisdiction not stated) — named as a client by the Canada-located vendor (client list / customer 
```

## Relationship
- **rank_group**: D1
- **data_quality_score**: 42
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Technicore Ltd (company (private sector), jurisdiction not stated) — named as a client by the Canada-located vendor (client list / customer story), dated: PM ERA Inc. | published by: the Canada-located vendor's own website | record: https://www.pmera.com/ | vendor in Canada because: vendor located in Canada (wall)=pmera.com | status rule: client listing on the vendor's own site (undated)
- **how_relationship_was_found**: tools/client_lists.py / dated_stories.py read the vendor's dated customer story / case study naming the buyer
- **keys**: lead:cad27fcef0162c7f
- **tier**: D
- **grade**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: Technicore Ltd
- **buyer_website**: https://technicore.ca/
- **buyer_address**: 102 Bales Dr E, Newmarket, Ontario, L3Y 8K3, Canada (schema.org JSON-LD PostalAddress on https://technicore.ca/)
- **buyer_phone**: 905 898 4889
- **buyer_contact_evidence_url**: https://technicore.ca/contact/
- **buyer_legal_name_as_published**: Technicore Ltd
- **buyer_logo_url**: https://technicore.ca/wp-content/uploads/2022/03/technicore-logo@2x-1.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/technicore-underground/
- **buyer_type**: company (private sector)
- **buyer_sector**: private sector
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://technicore.ca/contact/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: info@technicore.ca
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://technicore.ca/
- **email_evidence_quote**: ss","Organization"],"@id":"https://technicore.ca/#organization","name":"Technicore Underground Inc.","url":"https://technicore.ca","email":"info@technicore.ca","address":{"@type":"PostalAddress","streetAddress":"102 Bales Dr E","addressLocality":"Newmarket","addressRegion":"Ontario","posta
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-06
- **mailbox_provenance**: info@technicore.ca (general) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://technicore.ca/ | quote: "ss","Organization"],"@id":"https://technicore.ca/#organization","name":"Technicore Underground Inc.","url":"https://technicore.ca","email":"info@technicore.ca"," | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-06126
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none; pct=100; rua=mailto:re+g857neki4qk@dmarc.postmarkapp.com; sp=none; aspf=r;
- **dmarc_record_domain**: technicore.ca
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 ip4:65.21.122.58 ip4:65.21.161.228 ip4:65.21.161.229 ip4:65.21.161.230 ip4:207.164.28.99 a:win3.barrieweb.net a mx a:remote.technicore.ca include:spf.protection.outlook.com -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Technicore Ltd — 102 Bales Dr E, Newmarket, Ontario, L3Y 8K3, Canada (schema.org JSON-LD PostalAddress on https://technicore.ca/) ⏎ SUBMIT TO: info@technicore.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: PM ERA INC. (as registered: Canada's Business Registries, ON 2299303, 2026-11-08) — 5000 Yonge Street,, North York, ON, M2N 7E9, Canada | GST/HST 800435315 (Canada's Business Registries, ON 2299303, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Technicore Ltd (company (private sector), jurisdiction not stated) — named as a client by the Canada-located vendor (client list / customer 
- **invoice_card_json**: {"bill_to": {"legal_name": "Technicore Ltd", "legal_name_is_published": true, "address": "102 Bales Dr E, Newmarket, Ontario, L3Y 8K3, Canada (schema.org JSON-LD PostalAddress on https://technicore.ca/)", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "info@technicore.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 13% (Ontario)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "800435315RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "PM ERA INC. (as registered: Canada's Business Registries, ON 2299303, 2026-11-08)", "bn9": "800435315 (Canada's Business Registries, ON 2299303, 2026-11-08)", "neq": "", "remit_add
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
- **vendor**: PM ERA Inc.
- **vendor_legal_name**: PM ERA INC. (as registered: Canada's Business Registries, ON 2299303, 2026-11-08)
- **vendor_registry_id**: 2299303 (ON)
- **vendor_registry_url**: https://ised-isde.canada.ca/cbr-rec/en/search?q=PM%20ERA%20Inc.
- **vendor_registered_address**: RICHMND HILL, Ontario (registered office city / province; Canada's Business Registries, ON 2299303, 2026-11-08)
- **vendor_legal_form**: ONTARIO BUSINESS CORP. (Canada's Business Registries, ON 2299303, 2026-11-08)
- **vendor_address**: 5000 Yonge Street,, North York, ON, M2N 7E9, Canada
- **vendor_country_basis**: vendor located in Canada (wall)=pmera.com
- **vendor_bn9**: 800435315 (Canada's Business Registries, ON 2299303, 2026-11-08)
- **vendor_gst_hst_derived**: 800435315RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://www.pmera.com/
- **vendor_emails**: info@pmera.com
- **vendor_phone**: +1 (416) 849 2149
- **vendor_contact_evidence_url**: https://www.pmera.com/contact-us/
- **vendor_logo_url**: https://www.pmera.com/wp-content/uploads/elementor/thumbs/logo-2-qip66l9iuiz2n5a07ujti3r92hmhu57r9z6bjec31e.png
- **vendor_website_status**: site answers
- **vendor_linkedin_url**: https://www.linkedin.com/company/pmerainc
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); registry identity: 2299303 (ON) status Active — incorporated (Canada's Business Registries, ON 2299303, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: registry: Canada's Business Registries, ON 2299303, 2026-11-08; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2011-09-19; phone / role e-mails / logo: the vendor's own site, https://www.pmera.com/contact-us/ (tools/org_contacts.py, org_extras.py); website: https://www.pmera.com/ (site answers)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Active — incorporated (Canada's Business Registries, ON 2299303, 2026-11-08)
- **vendor_incorporation_date**: 2011-09-19
- **vendor_years_in_business**: 15.1 (since 2011-09-19, registry date)
- **vendor_bn_source**: registry: Canada's Business Registries, ON 2299303, 2026-11-08

## Contract
- **contract_status**: client listing on the vendor's own site (undated)
- **contract_link**: https://www.pmera.com/
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: HST 13% (Ontario) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 800435315RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Technicore Ltd — 102 Bales Dr E, Newmarket, Ontario, L3Y 8K3, Canada (schema.org JSON-LD PostalAddress on https://technicore.ca/) ⏎ SUBMIT TO: info@technicore.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: PM ERA INC. (as registered: Canada's Business Registries, ON 2299303, 2026-11-08) — 5000 Yonge Street,, North York, ON, M2N 7E9, Canada | GST/HST 800435315 (Canada's Business Registries, ON 2299303, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Technicore Ltd (company (private sector), jurisdiction not stated) — named as a client by the Canada-located vendor (client list / customer 
- **invoice_card_json**: {"bill_to": {"legal_name": "Technicore Ltd", "legal_name_is_published": true, "address": "102 Bales Dr E, Newmarket, Ontario, L3Y 8K3, Canada (schema.org JSON-LD PostalAddress on https://technicore.ca/)", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "info@technicore.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 13% (Ontario)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "800435315RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "PM ERA INC. (as registered: Canada's Business Registries, ON 2299303, 2026-11-08)", "bn9": "800435315 (Canada's Business Registries, ON 2299303, 2026-11-08)", "neq": "", "remit_add
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["info@technicore.ca (general)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://technicore.ca/", "quote: \"ss\",\"Organization\"],\"@id\":\"https://technicore.ca/#organization\",\"name\":\"Technicore Underground Inc.\",\"url\":\"https://technicore.ca\",\"email\":\"info@technicore.ca\",\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-06126"], "buyer_facts": ["address and phone: the buyer's own site, https://technicore.ca/contact/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "registry identity: 2299303 (ON) status Active — incorporated (Canada's Business Registries, ON 2299303, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data", "match)", "BN9: registry: Canada's Business Registries, ON 2299303, 2026-11-08", "GST/HST derived BN9 + RT0001 (CRA registry is CAP

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://technicore.ca/ | 2026-11-06 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, technicore.ca)
- **status**: ok
- **pages**: 4
- **language**: en
- **legal_name**: Technicore Ltd
- **legal_name_url**: https://technicore.ca/
- **legal_name_quote**: onals with technical expertise in every aspect of tunnelling. 905 898 4889 [email protected] © 2023 Technicore Ltd. All Rights Reserved. Privacy Policy Contact Privacy Policy Contact Website Design by Adrian Martin
- **logo_url**: https://technicore.ca/wp-content/uploads/2022/03/technicore-logo@2x-1.png
- **logo_basis**: logo image on the site
- **domain**: technicore.ca
- **key**: lead:cad27fcef0162c7f
- **name**: Technicore Ltd
- **website**: https://technicore.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: HomeAndConstructionBusiness/Organization
- **jsonld_name**: Technicore Underground Inc.
- **jsonld_address**: 102 Bales Dr E, Newmarket, Ontario, L3Y 8K3, Canada
- **jsonld_phone**: 905 898 4889
- **jsonld_email**: info@technicore.ca
- **jsonld_logo**: https://technicore.ca/wp-content/uploads/2023/11/technicore-logo@2x.jpg
- **jsonld_url**: https://technicore.ca
- **jsonld_quote**: {"@context":"https://schema.org","@graph":[{"@type":"Place","@id":"https://technicore.ca/#place","address":{"@type":"PostalAddress","streetAddress":"102 Bales Dr E","addressLocality":"Newmarket","addressRegion":"Ontario","postalCode":"L3Y 8K3","addressCountry":"Canada"}},{"@type":["HomeAndConstructi
- **jsonld_page**: https://technicore.ca/
- **legal_name_stated**: Controlled Foam Injection
- **legal_name_stated_url**: https://technicore.ca/about/
- **legal_name_stated_quote**: Our numerous innovations have played key roles in advancing the industry, including the proprietary Controlled Foam Injection (CFI) technique, used to fracture rock and concrete so it becomes biodegradable, and customized Tun
- **mentions**: {'payment_method': {'text': 'interaction with that embedded content, including tracking your interaction with the em', 'url': 'https://technicore.ca/privacy-policy/', 'quote': 'es may collect data about you, use cookies, embed additional third-party tracking, and monitor your interaction with that embedded content, including tracking your interaction with the embedded content if you have an account and are logged in to that website.'}}
- **linkedin_url**: https://www.linkedin.com/company/technicore-underground/
- **tel_links**: 9058984889; 905 898 4889

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "102 Bales Dr E, Newmarket, Ontario, L3Y 8K3", "address_country": "Canada", "address_url": "https://technicore.ca/contact/", "address_method": "json-ld", "address_quote": "ces that we offer. 905 898 4889 [email protected] 102 Bales Dr E, Newmarket, ON L3Y 8K3 Connect on LinkedIn Name Email Phone Message Send Message © 2022 Technicore Und", "phone": "905 898 4889", "phone_url": "https://technicore.ca/contact/", "emails": "info@technicore.ca", "emails_url": "https://technicore.ca/contact/", "domain": "technicore.ca", "key": "lead:cad27fcef0162c7f", "name": "technicore.ca", "website": "https://technicore.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, pmera.com)
- **status**: ok
- **pages**: 4
- **language**: en
- **legal_name**: dge Center Events Learning Zone Company Customer Portal My Account About Us Jobs
- **legal_name_url**: https://www.pmera.com/
- **legal_name_quote**: fferent. Consulting Services Projects Business Intelligence Software Solutions Small Business Knowledge Center Events Learning Zone Company Customer Portal My Account About Us Jobs Contact Us © 2024 PM ERA All rights reserved. Privacy & Policy Terms Insert/edit link Close Enter t
- **logo_url**: https://www.pmera.com/wp-content/uploads/elementor/thumbs/logo-2-qip66l9iuiz2n5a07ujti3r92hmhu57r9z6bjec31e.png
- **logo_basis**: logo image on the site
- **domain**: pmera.com
- **key**: vendor:PM ERA Inc.
- **name**: PM ERA Inc.
- **website**: https://pmera.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: PM ERA Inc.
- **jsonld_logo**: https://pmera.comwp-content/uploads/2022/05/logo-2.png
- **jsonld_url**: https://www.pmera.com/
- **jsonld_same_as**: https://x.com/PMEra_Inc; https://www.linkedin.com/company/pmerainc; https://www.youtube.com/user/PMEraInc
- **jsonld_quote**: {"@context":"https:\/\/schema.org","@graph":[{"@type":"WebPage","@id":"https:\/\/www.pmera.com\/","url":"https:\/\/www.pmera.com\/","name":"PM ERA Inc. - Training. Consulting. Coaching.","isPartOf":{"@id":"https:\/\/www.pmera.com\/#website"},"about":{"@id":"https:\/\/www.pmera.com\/#organization"},"
- **jsonld_page**: https://www.pmera.com/
- **legal_name_stated**: Personal Information Protection and Electronic Documents Act
- **legal_name_stated_url**: https://www.pmera.com/privacy-policy/
- **legal_name_stated_quote**: have outlined below our Privacy Principles based on the Privacy Principles established in Canada’s Personal Information Protection and Electronic Documents Act (PIPEDA). Your use of the Website and any submission of any information by you to the Website (dire
- **mentions**: {'payment_method': {'text': 'interact with our service, and to monitor aggregate usage and web traffic routing on ou', 'url': 'https://www.pmera.com/privacy-policy/', 'quote': 'e may use “session cookies” to enable certain features of our service, to better understand how you interact with our service, and to monitor aggregate usage and web traffic routing on our service. You can change your browser options to stop accepting cookies'}}
- **linkedin_url**: https://www.linkedin.com/company/pmerainc

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "5000 Yonge Street, Suite 1901, Toronto, ON M2N 7E9", "address_country": "CA", "address_url": "https://www.pmera.com/contact-us/", "address_method": "pattern", "address_quote": "849 2149 Email info@pmera.com Address 5000 Yonge Street, Suite 1901 Toronto, ON M2N 7E9 Canada We hold ourselves to a higher standard. Integrity, Teamwork, Transparenc", "phone": "+1 (416) 849 2149", "phone_url": "https://www.pmera.com/contact-us/", "emails": "info@pmera.com", "emails_url": "https://www.pmera.com/contact-us/", "domain": "pmera.com", "key": "vd:pmera.com", "name": "PM ERA Inc.", "website": "https://pmera.com/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Technicore Ltd | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Technicore%20Ltd | 2026-11-08 |
| buyer | PM ERA Inc. | found | PM ERA INC. | 800435315 | 2299303 | ON | ONTARIO BUSINESS CORP. | Active | 2011-09-19 | RICHMND HILL | Ontario |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=PM%20ERA%20Inc. | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Technicore Ltd |  |  |  |  |  |  |  |  |  |  |
| b | PM ERA Inc. |  |  |  |  |  |  |  |  |  |  |
| v | PM ERA Inc. |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:cad27fcef0162c7f",
 "ap_contact_team": {
  "emails": [
   "info@technicore.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "info@technicore.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://technicore.ca/",
    "quote": "ss\",\"Organization\"],\"@id\":\"https://technicore.ca/#organization\",\"name\":\"Technicore Underground Inc.\",\"url\":\"https://technicore.ca\",\"email\":\"info@technicore.ca\",\"address\":{\"@type\":\"PostalAddress\",\"streetAddress\":\"102 Bales Dr E\",\"addressLocality\":\"Newmarket\",\"addressRegion\":\"Ontario\",\"posta",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "technicore.ca",
    "task_id": "CL-LD-06126"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of technicore.ca (7 pages, robots.txt respected), no AI, no search engine"
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

## The vendor's other buyers in the dataset (first 60 of 2)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_bidsandtenders:889ebb7b-f92d-4df8-adba-f63c271879a1:1 | City of Barrie | Schedule Consulting Services for Infrastructure Construction Projects | 816000.0 |  |  | https://barrie.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/889ebb7b-f92d-4df8-adba-f63c271879a1 |
| ca_bidsandtenders:87446b6b-4ab3-4d2e-883f-4610d5f32a1e:12 | Metro Vancouver | Infrastructure Project Advisory Consulting Services - Project Controls and Digitalization Support Services Category |  |  |  | https://metrovancouver.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/87446b6b-4ab3-4d2e-883f-4610d5f32a1e |

## Open questions for hand research (layer 2)

- an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed)
- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
