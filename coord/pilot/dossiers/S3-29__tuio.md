# S3-29 — TUIO ⇄ Firestitch

Stratum: **S3_routed_public_body_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: TUIO Payments Inc (schema.org JSON-LD legalName on https://tuiopay.com/) — #1533-2967 Dundas St. W, Toronto, Ontario, M6P 1Z2 — buyer tax no. 705856490 (recipient_business_number in the federal grants & contributions disclosure, 2 agreement(s), last 2023-04-01; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)
SUBMIT TO: info@tuiopay.com (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Firestitch Inc. (as registered: Canada's Business Registries, CC 7539622, 2026-11-08) — Owen Sound, Ontario (registered office city / province; Canada's Business Registries, CC 7539622, 2026-11-08) | GST/HST 814173258 (Canada's Business Registries, CC 7539622, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: TUIO - Case Study | Digital Transformation Success Stories | Firestitch
```

## Relationship
- **rank_group**: D1
- **data_quality_score**: 40
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: TUIO (organisation (type not stated in the record), jurisdiction not stated) — named as a client by the Canada-located vendor (client list / customer story), dated: Firestitch | subject: TUIO - Case Study | Digital Transformation Success Stories | Firestitch | published by: the Canada-located vendor's own website | record: https://firestitch.com/case-studies/tuio | vendor in Canada because: vendor located in Canada (stories; Wikidata country + address on its site)=firestitch.com | status rule: client listing on the vendor's own site (undated)
- **how_relationship_was_found**: tools/client_lists.py / dated_stories.py read the vendor's dated customer story / case study naming the buyer
- **keys**: lead:4390f0cc973e8886
- **tier**: D
- **grade**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: TUIO
- **buyer_website**: https://tuiopay.com/
- **buyer_address**: #1533-2967 Dundas St. W, Toronto, Ontario, M6P 1Z2
- **buyer_phone**: 1-888-540-0160
- **buyer_contact_evidence_url**: https://tuiopay.com/
- **buyer_legal_name_as_published**: TUIO Payments Inc (schema.org JSON-LD legalName on https://tuiopay.com/)
- **buyer_bn_as_published**: 705856490 (recipient_business_number in the federal grants & contributions disclosure, 2 agreement(s), last 2023-04-01; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 705856490RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_logo_url**: https://tuiopay.com/wp-content/uploads/2022/12/tuio-favicon.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/tuio/
- **buyer_type**: company (private sector) (from the organisation's name / web domain)
- **buyer_sector**: private sector
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q136649061; technology company; payment processor; brand; online service; software; student information system
- **buyer_founded**: 2017-00-00 (Wikidata Q136649061, official website on the organisation's domain (https://tuiopay.com/) + name; 2026-11-08)
- **buyer_legal_form**: corporation (Wikidata Q136649061, official website on the organisation's domain (https://tuiopay.com/) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://tuiopay.com/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: info@tuiopay.com
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://tuiopay.com/
- **email_evidence_quote**: ogo","inLanguage":"en-US","width":"450","height":"161"},"image":"https://tuiopay.com/wp-content/uploads/2025/10/Tuio-Logo-2-1.png","email":"info@tuiopay.com","telephone":"1-888-540-0160","url":"https://tuiopay.com/","paymentAccepted":["credit card","invoice","amex","visa","e-transfer","mas
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: info@tuiopay.com (general) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://tuiopay.com/ | quote: "ogo","inLanguage":"en-US","width":"450","height":"161"},"image":"https://tuiopay.com/wp-content/uploads/2025/10/Tuio-Logo-2-1.png","email":"info@tuiopay.com","t" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; DNS lookup failed; mail handled by self-hosted or other (mx1-us1.ppe-hosted.com) | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-28756
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; DNS lookup failed; mail handled by self-hosted or other (mx1-us1.ppe-hosted.com)
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1; p=quarantine; rua=mailto:dmarc@tuiopay.com,mailto:re+b398482eaffd@inbound.dmarcdigests.com; ruf=mailto:dmarc@tuiopay.com; pct=100
- **dmarc_record_domain**: tuiopay.com
- **spf_policy**: DNS lookup failed
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: TUIO Payments Inc (schema.org JSON-LD legalName on https://tuiopay.com/) — #1533-2967 Dundas St. W, Toronto, Ontario, M6P 1Z2 — buyer tax no. 705856490 (recipient_business_number in the federal grants & contributions disclosure, 2 agreement(s), last 2023-04-01; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv) ⏎ SUBMIT TO: info@tuiopay.com (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Firestitch Inc. (as registered: Canada's Business Registries, CC 7539622, 2026-11-08) — Owen Sound, Ontario (registered office city / province; Canada's Business Registries, CC 7539622, 2026-11-08) | GST/HST 814173258 (Canada's Business Registries, CC 7539622, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: TUIO - Case Study | Digital Transformation Success Stories | Firestitch
- **invoice_card_json**: {"bill_to": {"legal_name": "TUIO Payments Inc (schema.org JSON-LD legalName on https://tuiopay.com/)", "legal_name_is_published": true, "address": "#1533-2967 Dundas St. W, Toronto, Ontario, M6P 1Z2", "address_is_the_invoice_address": false, "tax_number": "705856490 (recipient_business_number in the federal grants & contributions disclosure, 2 agreement(s), last 2023-04-01; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)", "language": "en"}, "submit_to": {"email": "info@tuiopay.com", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 13% (Ontario)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "814173258RT0001 (derived: BN9 + RT0001; GST/HST registratio
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: Firestitch
- **vendor_legal_name**: Firestitch Inc. (as registered: Canada's Business Registries, CC 7539622, 2026-11-08)
- **vendor_registry_id**: 7539622 (CC)
- **vendor_registry_url**: https://ised-isde.canada.ca/cbr-rec/en/search?q=Firestitch
- **vendor_registered_address**: Owen Sound, Ontario (registered office city / province; Canada's Business Registries, CC 7539622, 2026-11-08)
- **vendor_legal_form**: Business Corporation (Canada's Business Registries, CC 7539622, 2026-11-08)
- **vendor_country_basis**: vendor located in Canada (stories; Wikidata country + address on its site)=firestitch.com
- **vendor_bn9**: 814173258 (Canada's Business Registries, CC 7539622, 2026-11-08)
- **vendor_gst_hst_derived**: 814173258RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://firestitch.com
- **vendor_logo_url**: https://framerusercontent.com/images/i3tMYLpXdO58Fn5kNB6LEUOApLU.png?width=700&height=300
- **vendor_linkedin_url**: https://www.linkedin.com/company/firestitch/
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); registry identity: 7539622 (CC) status Active (Canada's Business Registries, CC 7539622, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: registry: Canada's Business Registries, CC 7539622, 2026-11-08; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2010-05-01; website: https://firestitch.com
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Active (Canada's Business Registries, CC 7539622, 2026-11-08)
- **vendor_incorporation_date**: 2010-05-01
- **vendor_years_in_business**: 16.5 (since 2010-05-01, registry date)
- **vendor_wikidata**: https://www.wikidata.org/wiki/Q136674328; organization
- **vendor_bn_source**: registry: Canada's Business Registries, CC 7539622, 2026-11-08

## Contract
- **contract_status**: client listing on the vendor's own site (undated)
- **contract_title**: TUIO - Case Study | Digital Transformation Success Stories | Firestitch
- **contract_description**: TUIO - Case Study | Digital Transformation Success Stories | Firestitch (the record's title; the source publishes no separate description)
- **contract_link**: https://firestitch.com/case-studies/tuio
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 705856490RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: HST 13% (Ontario) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 814173258RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: TUIO Payments Inc (schema.org JSON-LD legalName on https://tuiopay.com/) — #1533-2967 Dundas St. W, Toronto, Ontario, M6P 1Z2 — buyer tax no. 705856490 (recipient_business_number in the federal grants & contributions disclosure, 2 agreement(s), last 2023-04-01; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv) ⏎ SUBMIT TO: info@tuiopay.com (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Firestitch Inc. (as registered: Canada's Business Registries, CC 7539622, 2026-11-08) — Owen Sound, Ontario (registered office city / province; Canada's Business Registries, CC 7539622, 2026-11-08) | GST/HST 814173258 (Canada's Business Registries, CC 7539622, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: TUIO - Case Study | Digital Transformation Success Stories | Firestitch
- **invoice_card_json**: {"bill_to": {"legal_name": "TUIO Payments Inc (schema.org JSON-LD legalName on https://tuiopay.com/)", "legal_name_is_published": true, "address": "#1533-2967 Dundas St. W, Toronto, Ontario, M6P 1Z2", "address_is_the_invoice_address": false, "tax_number": "705856490 (recipient_business_number in the federal grants & contributions disclosure, 2 agreement(s), last 2023-04-01; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)", "language": "en"}, "submit_to": {"email": "info@tuiopay.com", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 13% (Ontario)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "814173258RT0001 (derived: BN9 + RT0001; GST/HST registratio
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["info@tuiopay.com (general)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://tuiopay.com/", "quote: \"ogo\",\"inLanguage\":\"en-US\",\"width\":\"450\",\"height\":\"161\"},\"image\":\"https://tuiopay.com/wp-content/uploads/2025/10/Tuio-Logo-2-1.png\",\"email\":\"info@tuiopay.com\",\"t\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; DNS lookup failed; mail handled by self-hosted or other (mx1-us1.ppe-hosted.com)", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-28756"], "buyer_facts": ["address and phone: the buyer's own site, https://tuiopay.com/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "registry identity: 7539622 (CC) status Active (Canada's Business Registries, CC 7539622, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data", "match)", "BN9: registry: Canada's Business Re

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://tuiopay.com/ | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, tuiopay.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://tuiopay.com/wp-content/uploads/2022/12/tuio-favicon.png
- **logo_basis**: site icon (apple-touch-icon)
- **domain**: tuiopay.com
- **key**: lead:4390f0cc973e8886
- **name**: TUIO
- **website**: https://tuiopay.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: TUIO
- **jsonld_legal_name**: TUIO Payments Inc.
- **jsonld_logo**: https://tuiopay.com/wp-content/uploads/2025/10/Tuio-Final.png
- **jsonld_url**: https://tuiopay.com/
- **jsonld_same_as**: https://www.facebook.com/tuiopay/; https://x.com/tuiopay; https://www.linkedin.com/company/tuio/; https://www.youtube.com/@tuio5034; https://www.capterra.ca/software/173831/tuio; https://www.capterra.com/p/173831/Tuio/; https://www.g2.com/products/tuio-tuio/reviews; https://www.trustpilot.com/review/tuiopay.com
- **jsonld_quote**: {"@context":"https:\/\/schema.org","@graph":[{"@type":"WebPage","@id":"https:\/\/tuiopay.com\/","url":"https:\/\/tuiopay.com\/","name":"TUIO - Simplify School Payments & Tuition Online","isPartOf":{"@id":"https:\/\/tuiopay.com\/#website"},"about":{"@id":"https:\/\/tuiopay.com\/#organization"},"prima
- **jsonld_page**: https://tuiopay.com/
- **legal_name_stated**: Tuio Payments Inc
- **legal_name_stated_url**: https://tuiopay.com/privacy/
- **legal_name_stated_quote**: Contact Us Book a demo Privacy Policy and Privacy Statement Last Updated: July 2026 STATEMENT We at Tuio Payments Inc. (“We”, “Tuio”, “our” or “us”) are firmly committed to privacy and transparency. We recognize that
- **mentions**: {'payment_method': {'text': 'interact with our Services (collectively “you” or “your” or the “Users”)', 'url': 'https://tuiopay.com/privacy/', 'quote': 'ness customers), parents and legal guardians, and all visitors, browsers, and other individuals who interact with our Services (collectively “you” or “your” or the “Users”). Please be advised that this policy applies to all Tuio websites, apps, and platforms m'}}
- **linkedin_url**: https://www.linkedin.com/company/tuio/
- **tel_links**: 18885400160

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 1, "address": "#1533-2967 Dundas St. W, Toronto, Ontario, M6P 1Z2", "address_country": "CA", "address_url": "https://tuiopay.com/", "address_method": "json-ld", "address_quote": "k a demo [email protected] 1 (888) 540-0160 #1533-2967 Dundas St. W Toronto, ON M6P 1Z2 Facebook-f Linkedin-in X-twitter Youtube Home About us Referrals Testimonials P", "phone": "1-888-540-0160", "phone_url": "https://tuiopay.com/", "emails": "info@tuiopay.com", "emails_url": "https://tuiopay.com/", "domain": "tuiopay.com", "key": "lead:4f7b0306b4c36ac1", "name": "tuiopay.com", "website": "https://tuiopay.com/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, firestitch.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://framerusercontent.com/images/i3tMYLpXdO58Fn5kNB6LEUOApLU.png?width=700&height=300
- **logo_basis**: logo image on the site
- **domain**: firestitch.com
- **key**: vendor:Firestitch
- **name**: Firestitch
- **website**: https://firestitch.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Do Not Track
- **legal_name_stated_url**: https://firestitch.com/privacy-policy
- **legal_name_stated_quote**: e means any device that can access the Service such as a computer, a cellphone or a digital tablet. Do Not Track (DNT) is a concept that has been promoted by US regulatory authorities, in particular the U.S. Fede
- **mentions**: {'payment_method': {'text': 'interact in the public areas with other users, such information may be viewed by all us', 'url': 'https://firestitch.com/privacy-policy', 'quote': 'roducts, services or promotions. With other users: when You share personal information or otherwise interact in the public areas with other users, such information may be viewed by all users and may be publicly distributed outside. With Your consent : We may d'}}
- **linkedin_url**: https://www.linkedin.com/company/firestitch/

## Vendor role mailboxes found on its site (org_contacts)
_not read_

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | TUIO | Q136649061 | official website on the organisation's domain (https://tuiopay.com/) + name | Tuio Payments Inc. [en] | TUIO | TUIO | technology company; payment processor; brand; online service; software; student information system | corporation | Canada | 2017-00-00 | Toronto |
| v | Firestitch | Q136674328 | official website on the organisation's domain (https://firestitch.com) + name |  | Firestitch |  | organization |  | Canada |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:4390f0cc973e8886",
 "ap_contact_team": {
  "emails": [
   "info@tuiopay.com"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "info@tuiopay.com",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://tuiopay.com/",
    "quote": "ogo\",\"inLanguage\":\"en-US\",\"width\":\"450\",\"height\":\"161\"},\"image\":\"https://tuiopay.com/wp-content/uploads/2025/10/Tuio-Logo-2-1.png\",\"email\":\"info@tuiopay.com\",\"telephone\":\"1-888-540-0160\",\"url\":\"https://tuiopay.com/\",\"paymentAccepted\":[\"credit card\",\"invoice\",\"amex\",\"visa\",\"e-transfer\",\"mas",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "TUIO",
    "task_id": "CL-LD-28756"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of tuiopay.com (17 pages, robots.txt respected), no AI, no search engine"
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
