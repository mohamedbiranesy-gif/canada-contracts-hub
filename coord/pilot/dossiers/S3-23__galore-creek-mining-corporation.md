# S3-23 — Galore Creek Mining Corporation ⇄ Teck Resources

Stratum: **S3_routed_public_body_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Galore Creek Mining Corporation — 788 – 550 Burrard Street, Vancouver, BC, V6C 2B5 — buyer tax no. 860004613 (Canada's Business Registries, BC BC0794294, 2026-11-08)
SUBMIT TO: info@gcmc.ca (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Teck Resources Limited (as registered: Canada's Business Registries, CC 4460561, 2026-11-08) — 550 Burrard Street , Vancouver, B.C., Canada V6C 0B3 | GST/HST 893110981 (Canada's Business Registries, CC 4460561, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Galore Creek Project
```

## Relationship
- **rank_group**: E1
- **data_quality_score**: 38
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Galore Creek Mining Corporation (company (private sector), jurisdiction not stated) — linked from the Canada-located vendor's site (weakest listed relationship): Teck Resources | subject: Galore Creek Project | published by: the Canada-located vendor's own website | record: https://www.teck.com/operations/canada/projects/galore-creek-project/ | vendor in Canada because: vendor located in Canada (wd)=teck.com | status rule: linked from a page of the Canada-located vendor's site (not a client page)
- **how_relationship_was_found**: tools/provider_mentions.py / news_match.py found the buyer linked from the vendor's own site or release
- **keys**: lead:32a7661988fb7ef3
- **tier**: E
- **grade**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: Galore Creek Mining Corporation
- **buyer_website**: https://gcmc.ca/
- **buyer_address**: 788 – 550 Burrard Street, Vancouver, BC, V6C 2B5
- **buyer_phone**: 604 900 3338
- **buyer_contact_evidence_url**: https://gcmc.ca/contact-us/
- **buyer_legal_name_as_published**: Galore Creek Mining Corporation
- **buyer_bn_as_published**: 860004613 (Canada's Business Registries, BC BC0794294, 2026-11-08)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 860004613RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_logo_url**: https://gcmc.ca/wp-content/uploads/2026/08/gcmc_logo_white.svg
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/galore-creek-mining-corporation/
- **buyer_registry_id**: BC0794294 (BC; https://ised-isde.canada.ca/cbr-rec/en/search?q=Galore%20Creek%20Mining%20Corporation)
- **buyer_type**: company (private sector)
- **buyer_sector**: private sector
- **buyer_legal_form**: BC Company (Canada's Business Registries, BC BC0794294, 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://gcmc.ca/contact-us/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: info@gcmc.ca
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://gcmc.ca/contact-us/
- **email_evidence_quote**: " content="Galore Creek Mining Corporation is located at Suite 788 - 550 Burrard Street Vancouver, BC Canada. Please contact us by email at info@gcmc.ca" /> <link rel="canonical" href="https://gcmc.ca/contact-us/" /> <meta property="og:locale" content="en_US" /> <meta property="og:type" co
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: info@gcmc.ca (general) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://gcmc.ca/contact-us/ | quote: "" content="Galore Creek Mining Corporation is located at Suite 788 - 550 Burrard Street Vancouver, BC Canada. Please contact us by email at info@gcmc.ca" /> <li" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Proofpoint | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-09967
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Proofpoint
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject; pct=100; rua=mailto:dmarc-rejections@gcmc.ca
- **dmarc_record_domain**: gcmc.ca
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 ip4:198.161.238.0/24 ip4:209.89.177.128/26 ip4:164.77.153.0/26 ip4:208.98.204.244/29 ip4:142.230.0.253/32 ip4:209.145.114.7/32 include:spf.protection.outlook.com include:spf-ca.emailsignatures365.com include:spf-0031b101.pphosted.com -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Galore Creek Mining Corporation — 788 – 550 Burrard Street, Vancouver, BC, V6C 2B5 — buyer tax no. 860004613 (Canada's Business Registries, BC BC0794294, 2026-11-08) ⏎ SUBMIT TO: info@gcmc.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Teck Resources Limited (as registered: Canada's Business Registries, CC 4460561, 2026-11-08) — 550 Burrard Street , Vancouver, B.C., Canada V6C 0B3 | GST/HST 893110981 (Canada's Business Registries, CC 4460561, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Galore Creek Project
- **invoice_card_json**: {"bill_to": {"legal_name": "Galore Creek Mining Corporation", "legal_name_is_published": true, "address": "788 – 550 Burrard Street, Vancouver, BC, V6C 2B5", "address_is_the_invoice_address": false, "tax_number": "860004613 (Canada's Business Registries, BC BC0794294, 2026-11-08)", "language": "en"}, "submit_to": {"email": "info@gcmc.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (BC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "893110981RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "Teck Resources Limited (as registered: Canada's Business Registries, CC 4460561, 2026-11-08)", "bn9": "893110981 (Canada's Business Registries, CC 4460561, 2026-11-08)", "ne
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
- **vendor**: Teck Resources
- **vendor_legal_name**: Teck Resources Limited (as registered: Canada's Business Registries, CC 4460561, 2026-11-08)
- **vendor_trading_name**: Teck Resources
- **vendor_registry_id**: 4460561 (CC)
- **vendor_registry_url**: https://ised-isde.canada.ca/cbr-rec/en/search?q=Teck%20Resources
- **vendor_registered_address**: VANCOUVER, British Columbia (registered office city / province; Canada's Business Registries, CC 4460561, 2026-11-08)
- **vendor_legal_form**: Business Corporation (Canada's Business Registries, CC 4460561, 2026-11-08)
- **vendor_address**: 550 Burrard Street , Vancouver, B.C., Canada V6C 0B3
- **vendor_country_basis**: vendor located in Canada (wd)=teck.com
- **vendor_bn9**: 893110981 (Canada's Business Registries, CC 4460561, 2026-11-08)
- **vendor_gst_hst_derived**: 893110981RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://teck.com
- **vendor_phone**: t: 604.699.4000
- **vendor_contact_evidence_url**: https://www.teck.com/about/contact
- **vendor_logo_url**: https://www.teck.com/media/logo-teck-64x26-ffffff.svg
- **vendor_website_status**: site answers
- **vendor_linkedin_url**: https://www.linkedin.com/company/teck-resources-limited
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); registry identity: 4460561 (CC) status Active (Canada's Business Registries, CC 4460561, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: registry: Canada's Business Registries, CC 4460561, 2026-11-08; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2008-01-01; phone / role e-mails / logo: the vendor's own site, https://www.teck.com/about/contact (tools/org_contacts.py, org_extras.py); website: https://teck.com (site answers)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Active (Canada's Business Registries, CC 4460561, 2026-11-08)
- **vendor_incorporation_date**: 2008-01-01
- **vendor_years_in_business**: 18.9 (since 2008-01-01, registry date)
- **vendor_bn_source**: registry: Canada's Business Registries, CC 4460561, 2026-11-08

## Contract
- **contract_status**: linked from a page of the Canada-located vendor's site (not a client page)
- **contract_title**: Galore Creek Project
- **contract_description**: Galore Creek Project (the record's title; the source publishes no separate description)
- **contract_link**: https://www.teck.com/operations/canada/projects/galore-creek-project/
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 860004613RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (BC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 893110981RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Galore Creek Mining Corporation — 788 – 550 Burrard Street, Vancouver, BC, V6C 2B5 — buyer tax no. 860004613 (Canada's Business Registries, BC BC0794294, 2026-11-08) ⏎ SUBMIT TO: info@gcmc.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Teck Resources Limited (as registered: Canada's Business Registries, CC 4460561, 2026-11-08) — 550 Burrard Street , Vancouver, B.C., Canada V6C 0B3 | GST/HST 893110981 (Canada's Business Registries, CC 4460561, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Galore Creek Project
- **invoice_card_json**: {"bill_to": {"legal_name": "Galore Creek Mining Corporation", "legal_name_is_published": true, "address": "788 – 550 Burrard Street, Vancouver, BC, V6C 2B5", "address_is_the_invoice_address": false, "tax_number": "860004613 (Canada's Business Registries, BC BC0794294, 2026-11-08)", "language": "en"}, "submit_to": {"email": "info@gcmc.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (BC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "893110981RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "Teck Resources Limited (as registered: Canada's Business Registries, CC 4460561, 2026-11-08)", "bn9": "893110981 (Canada's Business Registries, CC 4460561, 2026-11-08)", "ne
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["info@gcmc.ca (general)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://gcmc.ca/contact-us/", "quote: \"\" content=\"Galore Creek Mining Corporation is located at Suite 788 - 550 Burrard Street Vancouver, BC Canada. Please contact us by email at info@gcmc.ca\" /> <li\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Proofpoint", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-09967"], "buyer_facts": ["address and phone: the buyer's own site, https://gcmc.ca/contact-us/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "registry identity: 4460561 (CC) status Active (Canada's Business Registries, CC 4460561, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data", "match)", "BN9: registry: Canada's Business Registries, CC 4460561, 2026-11-08", "GST/HST d

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://gcmc.ca/contact-us/ | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, gcmc.ca)
- **status**: ok
- **pages**: 5
- **language**: en
- **legal_name**: Galore Creek Mining Corporation
- **legal_name_url**: https://gcmc.ca/
- **legal_name_quote**: Galore Creek Mining Corporation - Developing World Class Copper Deposit Skip to content About Us Project Status Development Regulat
- **logo_url**: https://gcmc.ca/wp-content/uploads/2026/08/gcmc_logo_white.svg
- **logo_basis**: logo image in the site header
- **domain**: gcmc.ca
- **key**: lead:32a7661988fb7ef3
- **name**: Galore Creek Mining Corporation
- **website**: https://gcmc.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Galore Creek Mining Corporation
- **jsonld_logo**: https://gcmc.ca/wp-content/uploads/2026/09/gcmc-logo-colour.png
- **jsonld_url**: https://gcmc.ca/
- **jsonld_same_as**: https://www.facebook.com/profile.php?id=100085128400187#; https://www.linkedin.com/company/galore-creek-mining-corporation?originalSubdomain=ca
- **jsonld_quote**: {"@context":"https:\/\/schema.org","@graph":[{"@type":"WebPage","@id":"https:\/\/gcmc.ca\/","url":"https:\/\/gcmc.ca\/","name":"Galore Creek Mining Corporation - Developing World Class Copper Deposit","isPartOf":{"@id":"https:\/\/gcmc.ca\/#website"},"about":{"@id":"https:\/\/gcmc.ca\/#organization"}
- **jsonld_page**: https://gcmc.ca/
- **legal_name_stated**: Use Galore Creek Mining Corporation
- **legal_name_stated_url**: https://gcmc.ca/legal/
- **legal_name_stated_quote**: Supporting Local Tahltan Bursaries Community Investment News Careers Contact Legal Notice Terms of Use Galore Creek Mining Corporation including its affiliates (“GCMC”) makes available to you this website (the “Website”) subject to yo
- **linkedin_url**: https://www.linkedin.com/company/galore-creek-mining-corporation/
- **tel_links**: 6049003338; 2366011231

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "788 – 550 Burrard Street, Vancouver, BC, V6C 2B5", "address_country": "CA", "address_url": "https://gcmc.ca/contact-us/", "address_method": "pattern", "address_quote": "west British Columbia. Vancouver Office 788 – 550 Burrard Street, Vancouver, BC V6C 2B5 604 900 3338 [email protected] Smithers Office 3851 Broadway Ave, Smithers, BC", "phone": "604 900 3338", "phone_url": "https://gcmc.ca/contact-us/", "emails": "info@gcmc.ca", "emails_url": "https://gcmc.ca/contact-us/", "domain": "gcmc.ca", "key": "lead:32a7661988fb7ef3", "name": "gcmc.ca", "website": "https://gcmc.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, teck.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: Teck Resources Limited Do Not Sell or Share My Personal Information
- **legal_name_url**: https://www.teck.com/
- **legal_name_quote**: ples Health and Safety Human Rights Our People Tailings Management Water Tulsequah Chief Mine ©2026 Teck Resources Limited Do Not Sell or Share My Personal Information Legal Notice Privacy Notice Cookie Settings Accessibility Plan Browser Opt-out Honored Our site use
- **logo_url**: https://www.teck.com/media/logo-teck-64x26-ffffff.svg
- **logo_basis**: logo image in the site header
- **domain**: teck.com
- **key**: vendor:Teck Resources
- **name**: Teck Resources
- **website**: https://teck.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: California Consumer Privacy Act
- **legal_name_stated_url**: https://www.teck.com/about/
- **legal_name_stated_quote**: ia residents have the right to opt out of “sales” and “sharing” for targeted advertising, under the California Consumer Privacy Act (“CCPA”). You can opt out of ‘sales’ and ‘sharing’ under CCPA, via your browser by using this prefe
- **mentions**: {'payment_method': {'text': 'Interactive Analyst Centre Analyst Coverage Share Price Merger of Teck and Anglo Americ', 'url': 'https://www.teck.com/', 'quote': 'Investors / Financial Reports Events & Presentations Sustainability Information Investor Resources Interactive Analyst Centre Analyst Coverage Share Price Merger of Teck and Anglo American Contact Us Financial Reports Events & Presentations Sustainability Inf'}}
- **linkedin_url**: https://www.linkedin.com/company/teck-resources-limited

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "550 Burrard Street , Vancouver, B.C., Canada V6C 0B3", "address_country": "CA", "address_url": "https://www.teck.com/about/contact", "address_method": "pattern", "address_quote": "sources Limited Suite 3300, Bentall 5 550 Burrard Street Vancouver, B.C. Canada V6C 0B3 t: 604.699.4000 f: 604.699.4750 Teck American Incorporated 501 North Riverpoint", "phone": "t: 604.699.4000", "phone_url": "https://www.teck.com/about/contact", "domain": "teck.com", "key": "vd:teck.com", "name": "Teck Resources", "website": "https://teck.com/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Galore Creek Mining Corporation | found | GALORE CREEK MINING CORPORATION | 860004613 | BC0794294 | BC | BC Company | Active | 2007-06-14 | Vancouver | BC |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Galore%20Creek%20Mining%20Corporation | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Teck Metals Ltd. |  |  |  |  |  |  |  |  |  |  |
| b | Galore Creek Mining Corporation |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:32a7661988fb7ef3",
 "ap_contact_team": {
  "emails": [
   "info@gcmc.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "info@gcmc.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://gcmc.ca/contact-us/",
    "quote": "\" content=\"Galore Creek Mining Corporation is located at Suite 788 - 550 Burrard Street Vancouver, BC Canada. Please contact us by email at info@gcmc.ca\" /> <link rel=\"canonical\" href=\"https://gcmc.ca/contact-us/\" /> <meta property=\"og:locale\" content=\"en_US\" /> <meta property=\"og:type\" co",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "gcmc.ca",
    "task_id": "CL-LD-09967"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of gcmc.ca (7 pages, robots.txt respected), no AI, no search engine"
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
