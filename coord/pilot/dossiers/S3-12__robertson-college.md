# S3-12 — Robertson College ⇄ D2L Corporation

Stratum: **S3_routed_public_body_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Robertson College Let's get started Book your 15 — 180 Main Street, Winnipeg, MB R3C 1A6
SUBMIT TO: info@robertsoncollege.com (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: D2L Corporation — Kitchener, ON, CA | GST/HST 812930345RT0001 (account derived from the BN9) | NEQ 1177781433
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of MB on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Robertson College (university / college, jurisdiction not stated) — active paid service of a Canada-HQ vendor seen on the buyer's own site: 
```

## Relationship
- **rank_group**: T1
- **data_quality_score**: 54
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 12
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Robertson College (university / college, jurisdiction not stated) — active paid service of a Canada-HQ vendor seen on the buyer's own site: D2L Corporation | awarded 2026-11-03 | published by: the buyer's own website (service of a Canada-HQ vendor in use) | record: https://www.robertsoncollege.com/ | vendor in Canada because: service of a Canada-HQ vendor seen on the buyer's own site (tech)=ment opportunities 1.2 Data Controller and Contact Information Data Controller D2L Corporation Email: [email protected] 137 Glasgow Street, Suite 560 Kitc | status rule: active service seen on the buyer's own site (2026-11-03): Canada-HQ vendor D2L Corporation
- **how_relationship_was_found**: tools/tech_portals2.py / tech_relationships.py found the buyer's own web property running the Canada-HQ vendor's paid platform (portal host or embedded service), dated by the page read
- **keys**: lead:e78dde905f893c38
- **tier**: T
- **grade**: 1
- **records_with_this_vendor**: 1 (relationship record: the buyer's own website (service of a Canada-HQ vendor in use); 0 in the contract dataset)

## Buyer
- **buyer**: Robertson College
- **buyer_website**: https://robertsoncollege.com/
- **buyer_address**: 180 Main Street, Winnipeg, MB R3C 1A6
- **buyer_phone**: 1-431-668-2680
- **buyer_contact_evidence_url**: https://www.robertsoncollege.com/contact/
- **buyer_legal_name_as_published**: Robertson College Let's get started Book your 15
- **buyer_logo_url**: https://www.robertsoncollege.com/wp-content/uploads/2026/05/logo.svg
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://linkedin.com/school/robertson-college/
- **buyer_registry_id**: 2220393 (MB; https://ised-isde.canada.ca/cbr-rec/en/search?q=Robertson%20College)
- **buyer_type**: university / college
- **buyer_sector**: education: post-secondary
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q7352092; private career college in Alberta
- **buyer_founded**: 1911-00-00 (Wikidata Q7352092, official website on the organisation's domain (http://www.robertsoncollege.com) + name; 2026-11-08)
- **buyer_legal_form**: MB SHARE CORPORATION (Canada's Business Registries, MB 2220393, 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.robertsoncollege.com/contact/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of MB on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: info@robertsoncollege.com
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://www.robertsoncollege.com/contact/
- **email_evidence_quote**: zens or permanent residents for our diploma programs at this time. Contact info Browse Micro-courses General Other Inquiries Contact info E info@robertsoncollege.com Contact by Campus Find a campus Campus-specific contact details. Phone numbers and addresses are tappable on mobile. Winnipe
- **email_evidence_context**: rnational Application Inquiries Due to current Canadian government regulations, we can only take Canadian citizens or permanent residents for our diploma programs at this time. Contact info Browse Micro-courses General Other Inquiries Contact info E info@robertsoncollege.com Contact by Campus Find a campus Campus-specific contact details. Phone numbers and addresses are tappable on mobile. Winnipeg Physical campus Contact info P (204) 943-5661 E [email protected] A 180 Main Street, Winnipeg, MB R3C 1A6 H Mon–Fri 8:00 am (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: info@robertsoncollege.com (general) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-10-28 | page: https://www.robertsoncollege.com/contact/ | quote: "zens or permanent residents for our diploma programs at this time. Contact info Browse Micro-courses General Other Inquiries Contact info E info@robertsoncolleg" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Mimecast | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-WD-011185
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Mimecast
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1;p=none
- **dmarc_record_domain**: robertsoncollege.com
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 include:ca._netblocks.mimecast.com ip4:64.201.171.8/32 include:googlemail.com include:_spf.google.com include:spf.myconnectwise.net include:mailgun.org include:aspmx.pardot.com include:spf.watermarkinsights.com include:spf.salesforce.com ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Robertson College Let's get started Book your 15 — 180 Main Street, Winnipeg, MB R3C 1A6 ⏎ SUBMIT TO: info@robertsoncollege.com (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: D2L Corporation — Kitchener, ON, CA | GST/HST 812930345RT0001 (account derived from the BN9) | NEQ 1177781433 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of MB on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Robertson College (university / college, jurisdiction not stated) — active paid service of a Canada-HQ vendor seen on the buyer's own site: 
- **invoice_card_json**: {"bill_to": {"legal_name": "Robertson College Let's get started Book your 15", "legal_name_is_published": true, "address": "180 Main Street, Winnipeg, MB R3C 1A6", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "info@robertsoncollege.com", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of MB on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (MB)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "812930345RT0001", "vendor_qst": ""}, "vendor_identity": {"legal_name": "D2L Corporation", "bn9": "812930345", "neq": "1177781433 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)", "remit_address": "137 Glasgow Street, Suite 560, Kitchener, ON, N2G 4X8,
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
- **vendor**: D2L Corporation
- **vendor_legal_name**: D2L Corporation
- **vendor_trading_name**: D2L® (other names in the registry)
- **vendor_registry_id**: Québec REQ (NEQ): 1177781433
- **vendor_registry_url**: https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises
- **vendor_registered_address**: 137 Glasgow Street, Suite 560, Kitchener, ON, N2G 4X8, CA
- **vendor_neq**: 1177781433 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_legal_form**: Société par actions ou compagnie — ONTARIO : Loi sur les sociétés par actions, L.R.O. 1990, c. B.16
- **vendor_activity_code**: CAE 9999 — Systèmes de logiciels d'apprentissage
- **vendor_employees_quebec**: De 11 à 25
- **vendor_directors_range**: 3 to 15 directors (Corporations Canada)
- **vendor_last_annual_filing**: REQ annual declaration 2026; Corporations Canada anniversary 2014-06-20
- **vendor_address**: Kitchener, ON, CA
- **vendor_country_basis**: service of a Canada-HQ vendor seen on the buyer's own site (tech)=ment opportunities 1.2 Data Controller and Contact Information Data Controller D2L Corporation Email: [email protected] 137 Glasgow Street, Suite 560 Kitchener, ON, Canada N2G 4X8 Data Protection Officer Name: Taylor Bur
- **vendor_bn9**: 812930345
- **vendor_gst_hst_derived**: 812930345RT0001
- **vendor_website**: https://www.d2l.com/
- **vendor_phone**: 1-519-772-0325
- **vendor_contact_evidence_url**: https://www.d2l.com/about/locations/
- **vendor_logo_url**: https://www.d2l.com/wp-content/uploads/2022/08/logo.svg
- **vendor_website_basis**: found by a web search, confirmed by reading the site on 2026-11-08: https://www.d2l.com/ (D2L Brightspace Learning Platform With Built-In AI Skip to main content English English English (APAC) English (IN) Spanish (EU) Español (LATAM) Français (CA) N)
- **vendor_facts_provenance**: name and address: the record's vendor block (the buyer's own website (service of a Canada-HQ vendor in use)); registry identity: Québec REQ (NEQ): 1177781433 status Québec REQ (NEQ): Immatriculée (2022-07-05); Corporations Canada (corporation number): Active (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: registry match; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2014-01-01; phone / role e-mails / logo: the vendor's own site, https://www.d2l.com/about/locations/ (tools/org_contacts.py, org_extras.py); website: https://www.d2l.com/; NEQ: 1177781433 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Québec REQ (NEQ): Immatriculée (2022-07-05); Corporations Canada (corporation number): Active
- **vendor_incorporation_date**: 2014-01-01
- **vendor_years_in_business**: 12.9 (since 2014-01-01, registry date)

## Contract
- **contract_status**: active service seen on the buyer's own site (2026-11-03): Canada-HQ vendor D2L Corporation
- **award_date**: 2026-11-03
- **contract_link**: https://www.robertsoncollege.com/
- **source**: the buyer's own website (service of a Canada-HQ vendor in use)
- **contracts_with_canadian_suppliers**: 2
- **records_with_this_vendor**: 1 (relationship record: the buyer's own website (service of a Canada-HQ vendor in use); 0 in the contract dataset)
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of MB on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (MB) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 812930345RT0001

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Robertson College Let's get started Book your 15 — 180 Main Street, Winnipeg, MB R3C 1A6 ⏎ SUBMIT TO: info@robertsoncollege.com (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: D2L Corporation — Kitchener, ON, CA | GST/HST 812930345RT0001 (account derived from the BN9) | NEQ 1177781433 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of MB on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Robertson College (university / college, jurisdiction not stated) — active paid service of a Canada-HQ vendor seen on the buyer's own site: 
- **invoice_card_json**: {"bill_to": {"legal_name": "Robertson College Let's get started Book your 15", "legal_name_is_published": true, "address": "180 Main Street, Winnipeg, MB R3C 1A6", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "info@robertsoncollege.com", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of MB on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (MB)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "812930345RT0001", "vendor_qst": ""}, "vendor_identity": {"legal_name": "D2L Corporation", "bn9": "812930345", "neq": "1177781433 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)", "remit_address": "137 Glasgow Street, Suite 560, Kitchener, ON, N2G 4X8,
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["info@robertsoncollege.com (general)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-10-28", "page: https://www.robertsoncollege.com/contact/", "quote: \"zens or permanent residents for our diploma programs at this time. Contact info Browse Micro-courses General Other Inquiries Contact info E info@robertsoncolleg\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Mimecast", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-WD-011185"], "buyer_facts": ["address and phone: the buyer's own site, https://www.robertsoncollege.com/contact/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (the buyer's own website (service of a Canada-HQ vendor in use))", "registry identity: Québec REQ (NEQ): 1177781433 status Québec REQ (NEQ): Immatriculée (2022-07-05)", "Corporations Canada (corporation number): Active (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data", "match)", "BN9: registry match", "GST/HST derived BN9 + RT0

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.robertsoncollege.com/contact/ | 2026-11-08 | ok |  |  |  | (204) 943-5661 | 180 Main Street, Winnipeg, MB R3C 1A6 |  |  |  |  |

## Buyer site facts (org_extras, robertsoncollege.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: Robertson College Let's get started Book your 15
- **legal_name_url**: https://www.robertsoncollege.com/
- **legal_name_quote**: ny time. See our Privacy Policy for details. Search Policies Established in 1911 | © Copyright 2026 Robertson College Let's get started Book your 15-minute call Simply fill out the form below and one of our Student Advisors will provide any extra i
- **logo_url**: https://www.robertsoncollege.com/wp-content/uploads/2026/05/logo.svg
- **logo_basis**: logo image in the site header
- **domain**: robertsoncollege.com
- **key**: lead:e78dde905f893c38
- **name**: Robertson College
- **website**: https://robertsoncollege.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Robertson College
- **jsonld_logo**: https://www.robertsoncollege.com/wp-content/uploads/2026/05/logo.svg
- **jsonld_url**: https://www.robertsoncollege.com/
- **jsonld_same_as**: https://www.facebook.com/OfficialRobertsonCollege/
- **jsonld_quote**: { "@context": "https://schema.org", "@type": "LocalBusiness", "name": "Robertson College", "sameAs": "https://ai.robertsoncollege.com", "@id": "https://robertsoncollege.com/#business", "url": "https://robertsoncollege.com" }
- **jsonld_page**: https://www.robertsoncollege.com/
- **legal_name_stated**: Robertson College
- **legal_name_stated_url**: https://www.robertsoncollege.com/privacy-policy/
- **legal_name_stated_quote**: Privacy Policy | Robertson College Our Programs 1 School of Business and Technology Preparing students for business careers online and
- **linkedin_url**: https://linkedin.com/school/robertson-college/
- **tel_links**: +14316682680; 2049435661; 14039200070; 17807056633

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "address": "180 Main Street, Winnipeg, MB R3C 1A6", "address_country": "CA", "address_url": "https://www.robertsoncollege.com/contact/", "address_method": "pattern", "address_quote": "ntact info P (204) 943-5661 E [email protected] A 180 Main Street, Winnipeg, MB R3C 1A6 H Mon–Fri 8:00 am – 4:30 pm CT Campus page Calgary Physical campus Contact info", "phone": "1-431-668-2680", "phone_url": "https://www.robertsoncollege.com/contact/", "emails": "info@robertsoncollege.com", "emails_url": "https://www.robertsoncollege.com/contact/", "domain": "robertsoncollege.com", "key": "lead:e78dde905f893c38", "name": "Robertson College", "website": "https://robertsoncollege.com/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, d2l.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: D2L Corporation
- **legal_name_url**: https://www.d2l.com/
- **legal_name_quote**: hat is an LMS? What is Asynchronous Learning? What’s new at D2L Best Corporate LMS Copyright © 2026 D2L Corporation. All rights reserved. Status Privacy Notice Do Not Sell My PI Terms of Use Accessibility Conformanc
- **logo_url**: https://www.d2l.com/wp-content/uploads/2022/08/logo.svg
- **logo_basis**: logo image in the site header
- **domain**: d2l.com
- **key**: vendor:d2l.com
- **name**: d2l.com
- **website**: https://d2l.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: D2L
- **jsonld_legal_name**: D2L Inc.
- **jsonld_alternate_name**: Desire2Learn
- **jsonld_phone**: 1-888-772-0325
- **jsonld_logo**: https://www.d2l.com/wp-content/uploads/2026/04/img-logo-D2L_author.png
- **jsonld_url**: https://www.d2l.com/
- **jsonld_founding_date**: 1999-04-01
- **jsonld_same_as**: https://www.facebook.com/D2Linc; https://x.com/D2L; https://www.linkedin.com/company/d2l/; https://www.youtube.com/user/desire2learninc; https://www.instagram.com/d2l/; https://en.wikipedia.org/wiki/D2L; https://www.wikidata.org/wiki/Q5264469; https://www.crunchbase.com/organization/desire2learn
- **jsonld_quote**: {"@context":"https:\/\/schema.org","@graph":[{"@type":"WebPage","@id":"https:\/\/www.d2l.com\/","url":"https:\/\/www.d2l.com\/","name":"D2L Brightspace Learning Platform With Built-In AI","isPartOf":{"@id":"https:\/\/www.d2l.com\/#website"},"about":{"@id":"https:\/\/www.d2l.com\/#organization"},"pri
- **jsonld_page**: https://www.d2l.com/
- **legal_name_stated**: Rideau Hall Foundation
- **legal_name_stated_url**: https://www.d2l.com/about/leadership/
- **legal_name_stated_quote**: Director David Johnston was Canada’s 28th governor general. During his mandate, he established the Rideau Hall Foundation (RHF), a registered charity that supports and amplifies the Office of the Governor General in its w
- **mentions**: {'payment_method': {'text': 'interactive learning experiences', 'url': 'https://www.d2l.com/', 'quote': 'nuing Education Faculty Burn Out Streamline Workflows D2L for K-12 Engage and inspire students with interactive learning experiences. Learn More use case Personalized and Engaged Learning Professional Learning for Educators Reduce T'}}
- **linkedin_url**: https://www.linkedin.com/company/d2l/

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "137 Glasgow Street Suite 560, Kitchener, ON, N2G 4X8", "address_country": "CA", "address_url": "https://www.d2l.com/about/locations/", "address_method": "address-tag", "address_quote": "D2L Corporation Global Headquarters 137 Glasgow Street Suite 560 Kitchener, ON N2G 4X8 1-519-772-0325 (Local) 1-888-772-0325 (Toll Free, North America) 1-519-772-0324", "phone": "1-519-772-0325", "phone_url": "https://www.d2l.com/about/locations/", "domain": "d2l.com", "key": "vd:d2l.com", "name": "d2l.com", "website": "https://d2l.com/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Robertson College | found | ROBERTSON COLLEGE INC. |  | 2220393 | MB | MB SHARE CORPORATION | Inactive | 1988-01-01 | WINNIPEG | MB |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Robertson%20College | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Robertson College | Q7352092 | official website on the organisation's domain (http://www.robertsoncollege.com) + name |  | Robertson College |  | private career college in Alberta |  | Canada | 1911-00-00 |  |

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

## The vendor's other buyers in the dataset (first 60 of 19)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_alberta_apc:AB-2025-01951:e8fa37de-e5b3-4690-9330-afe42c0586e6 | Red Deer Polytechnic | Red Deer Polytechnic - Negotiated Request for Proposal - Learning Management System (LMS ) | 1.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-01951 |
| ca_bidsandtenders:852b0bf1-b12e-4541-8487-7045b6dacafa:1 | Municipality of Clarington | Learning Management System |  |  |  | https://clarington.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/852b0bf1-b12e-4541-8487-7045b6dacafa |
| ca_bidsandtenders:156b602d-cf79-4b84-a630-c854f0f21834:1 | City of Waterloo | Learning Management System |  |  |  | https://waterloo.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/156b602d-cf79-4b84-a630-c854f0f21834 |
| ca_merx:2486883468:1 | University Of Calgary | Learning Management System (LMS) |  |  |  | https://www.merx.com/universityofcalgary/solicitations/Learning-Management-System-LMS/0000246846?origin=0 |
| ca_merx:2165019645:1 | George Brown College | Learning Management System | 1.0 |  |  | https://www.merx.com/oupma/georgebrown/solicitations/Learning-Management-System/0000221122?origin=0 |
| ca_merx:2006612454:1 | Brock University | Modern Cloud-Based Learning Management System |  |  |  | https://www.merx.com/oupma/brocku/solicitations/Modern-Cloud-Based-Learning-Management-System/0000211285?origin=0 |
| canada_federal:cb:CW2355334 | Department of Public Works and Government Services (PSPC) | ProServices SA – D2L Corporation |  |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cw2355334 |
| canada_federal:cb:CW2441855 | Department of Public Works and Government Services (PSPC) | TSPS SA (Task Based) – D2L Corporation |  |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cw2441855 |
| private_press:794233bb4145c8e7cdf17b99547974a1e07a80c6 | Van Lang Investment and Education Management Group Corporation (Van Lang Education Group) | D2L Signs First Strategic Vietnam Customer as Van Lang Education Group Adopts D2L Brightspace |  |  |  | https://www.newswire.ca/news-releases/d2l-signs-first-strategic-vietnam-customer-as-van-lang-education-group-adopts-d2l-brightspace-812975353.html |
| private_press:0c3794d5505bc42d10b62c4866618e482928a3a5 | University of Ottawa | University of Ottawa Deepens Strategic Relationship with a 12-Year Renewal of D2L Brightspace |  |  |  | https://www.newswire.ca/news-releases/university-of-ottawa-deepens-strategic-relationship-with-a-12-year-renewal-of-d2l-brightspace-873135986.html |
| private_press:ddd6a291a865fced13db2a5d62c5291716fcca43 | Loyola University Chicago | Loyola University Chicago Selects D2L Brightspace as Its Next-Generation Learning Platform |  |  |  | https://www.newswire.ca/news-releases/loyola-university-chicago-selects-d2l-brightspace-as-its-next-generation-learning-platform-836650163.html |
| private_press:db2e14eb0dcc26197c337d59e67ead66646bf28b | Midwestern University | Midwestern University Selects D2L to Support AI Innovation in Teaching and Learning |  |  |  | https://www.newswire.ca/news-releases/midwestern-university-selects-d2l-to-support-ai-innovation-in-teaching-and-learning-868245884.html |
| private_press:a36d3c0f4638d63ef4ccc49d981ccecd62100b0b | Rasmussen University (American Public Education, Inc.) | Rasmussen University Selects D2L Brightspace to Deliver Inclusive AI in Education |  |  |  | https://www.newswire.ca/news-releases/rasmussen-university-selects-d2l-brightspace-to-deliver-inclusive-ai-in-education-894898316.html |
| seao_quebec:1222576:d2l-corporation | Université McGill | Learning Management System | 3373502.52 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=d760a2a3-1284-4bfd-bfa3-c7e409c63390 |
| seao_quebec:1250822:d2l-corporation | CEGEP de Saint-Hyacinthe | Plateforme de formation en ligne | 69548.81 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=cee99611-3295-40db-9ca4-6af2373e2033 |
| us_state_delaware:5775:D2L_Ltd | State of Delaware - Government Support Services (Contracting) | DTCC Learning Management System |  |  |  | http://mmp.delaware.gov/Contracts/Details/5775 |
| usaspending:CONT_AWD_140A2325P0187_1450_-NONE-_-NONE- | Department of the Interior | SIPI BRIGHTSPACE LICENSING | 247223.01 |  |  | https://www.usaspending.gov/award/CONT_AWD_140A2325P0187_1450_-NONE-_-NONE-/ |
| ca_canadabuys_contract_history:an:E60ZH-1700LS:034:ZH | Public Works and Government Services Canada | End-to-End Learning Services (Excludes COTS Training) |  |  |  | https://open.canada.ca/data/en/dataset/a1acb126-9ce8-40a9-b889-5da2b1dd20cb |
| canada_sosa:CW2382809 | Public Works and Government Services Canada | PSPC Cloud Method of Supply ? D2L Corporation |  |  |  | https://buyandsell.gc.ca/procurement-data/standing-offers-and-supply-arrangements/CW2382809 |

## Open questions for hand research (layer 2)

- an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed)
- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
