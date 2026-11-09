# S3-38 — BinaryLogic Inc ⇄ 10 Percent Recruiting Ltd.

Stratum: **S3_routed_public_body_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: BinaryLogic Inc — 10055-106 ST NW , Edmonton, AB T5J 2Y2 — buyer tax no. 779857127 (Canada's Business Registries, AB 2019517784, 2026-11-08)
SUBMIT TO: hello@01logic.ca (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: 10 PERCENT RECRUITING LTD. (as registered: Canada's Business Registries, AB 2019137591, 2026-11-08) — 10160 103 St NW, Edmonton, Alberta, T5J0X6, Canada | GST/HST 794817494 (Canada's Business Registries, AB 2019137591, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Success Stories – 10 Percent Recruiting Ltd. – Professional Recruitment Agency in Canada
```

## Relationship
- **rank_group**: D1
- **data_quality_score**: 44
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: BinaryLogic Inc (company (private sector), jurisdiction not stated) — named as a client by the Canada-located vendor (client list / customer story), dated: 10 Percent Recruiting Ltd. | subject: Success Stories – 10 Percent Recruiting Ltd. – Professional Recruitment Agency in Canada | published by: the Canada-located vendor's own website | record: https://www.10pr.ca/success-stories | vendor in Canada because: vendor located in Canada (v)=10pr.ca | status rule: client listing on the vendor's own site (undated)
- **how_relationship_was_found**: tools/client_lists.py / dated_stories.py read the vendor's dated customer story / case study naming the buyer
- **keys**: lead:6f7adb4bc49e33d5
- **tier**: D
- **grade**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: BinaryLogic Inc
- **buyer_website**: https://01logic.ca/
- **buyer_address**: 10055-106 ST NW , Edmonton, AB T5J 2Y2
- **buyer_phone**: +17806656677 (tel: link on https://01logic.ca/)
- **buyer_contact_evidence_url**: https://www.01logic.ca/contact/
- **buyer_legal_name_as_published**: BinaryLogic Inc
- **buyer_bn_as_published**: 779857127 (Canada's Business Registries, AB 2019517784, 2026-11-08)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 779857127RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_logo_url**: https://www.01logic.ca/wp-content/uploads/images/01LOGIC-Logo-Rev8-220x45.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/binarylogic/
- **buyer_registry_id**: 2019517784 (AB; https://ised-isde.canada.ca/cbr-rec/en/search?q=BinaryLogic%20Inc)
- **buyer_type**: company (private sector)
- **buyer_sector**: private sector
- **buyer_legal_form**: Alberta Business Corporation (Canada's Business Registries, AB 2019517784, 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.01logic.ca/contact/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: hello@01logic.ca
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://www.01logic.ca/
- **email_evidence_quote**: e. Discover actionable insights and connect with our team to start your journey toward a more secure, efficient, and future-ready business. hello@01logic.ca Get in Touch Today Focus on your business and not your IT Ready to transform your IT experience? BinaryLogic delivers expert guidance
- **email_evidence_context**: ic delivers expert guidance, hands-on support, and practical resources to help you move forward with confidence. Discover actionable insights and connect with our team to start your journey toward a more secure, efficient, and future-ready business. hello@01logic.ca Get in Touch Today Focus on your business and not your IT Ready to transform your IT experience? BinaryLogic delivers expert guidance, hands-on support, and practical resources to help you move forward with confidence. Discover actionable insights a (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: hello@01logic.ca (general) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://www.01logic.ca/ | quote: "e. Discover actionable insights and connect with our team to start your journey toward a more secure, efficient, and future-ready business. hello@01logic.ca Get" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-08429
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Microsoft 365
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1; p=quarantine; ruf=mailto:alerts@01logic.ca
- **dmarc_record_domain**: 01logic.ca
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 ip4:8.12.58.0/24 ip4:8.34.161.0/24 ip4:8.224.10.0/24 ip4:213.212.96.64/27 ip4:118.186.64.32/28 include:spf.protection.outlook.com include:_spf.atlassian.net include:autotask.net ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: BinaryLogic Inc — 10055-106 ST NW , Edmonton, AB T5J 2Y2 — buyer tax no. 779857127 (Canada's Business Registries, AB 2019517784, 2026-11-08) ⏎ SUBMIT TO: hello@01logic.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: 10 PERCENT RECRUITING LTD. (as registered: Canada's Business Registries, AB 2019137591, 2026-11-08) — 10160 103 St NW, Edmonton, Alberta, T5J0X6, Canada | GST/HST 794817494 (Canada's Business Registries, AB 2019137591, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Success Stories – 10 Percent Recruiting Ltd. – Professional Recruitment Agency in Canada
- **invoice_card_json**: {"bill_to": {"legal_name": "BinaryLogic Inc", "legal_name_is_published": true, "address": "10055-106 ST NW , Edmonton, AB T5J 2Y2", "address_is_the_invoice_address": false, "tax_number": "779857127 (Canada's Business Registries, AB 2019517784, 2026-11-08)", "language": "en"}, "submit_to": {"email": "hello@01logic.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (AB)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "794817494RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "10 PERCENT RECRUITING LTD. (as registered: Canada's Business Registries, AB 2019137591, 2026-11-08)", "bn9": "794817494 (Canada's Business Registries, AB 2019137591, 2026-11-08)", "neq": "", "re
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
- **vendor**: 10 Percent Recruiting Ltd.
- **vendor_legal_name**: 10 PERCENT RECRUITING LTD. (as registered: Canada's Business Registries, AB 2019137591, 2026-11-08)
- **vendor_registry_id**: 2019137591 (AB)
- **vendor_registry_url**: https://ised-isde.canada.ca/cbr-rec/en/search?q=10%20Percent%20Recruiting%20Ltd.
- **vendor_registered_address**: EDMONTON, AB (registered office city / province; Canada's Business Registries, AB 2019137591, 2026-11-08)
- **vendor_legal_form**: Alberta Business Corporation (Canada's Business Registries, AB 2019137591, 2026-11-08)
- **vendor_address**: 10160 103 St NW, Edmonton, Alberta, T5J0X6, Canada
- **vendor_country_basis**: vendor located in Canada (v)=10pr.ca
- **vendor_bn9**: 794817494 (Canada's Business Registries, AB 2019137591, 2026-11-08)
- **vendor_gst_hst_derived**: 794817494RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://www.10pr.ca/
- **vendor_emails**: hello@10pr.ca
- **vendor_phone**: +17806659290 (tel: link on https://10pr.ca/)
- **vendor_contact_evidence_url**: https://www.10pr.ca/contact
- **vendor_logo_url**: https://www.10pr.ca/wp-content/uploads/yootheme/cache/a6/10PR-Logo-Mobile-725x150-including-Canada-001b-a67ee5cb.png
- **vendor_website_status**: site answers
- **vendor_linkedin_url**: https://ca.linkedin.com/company/10percentrecruiting
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); registry identity: 2019137591 (AB) status Active (Canada's Business Registries, AB 2019137591, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: registry: Canada's Business Registries, AB 2019137591, 2026-11-08; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2015-08-10; phone / role e-mails / logo: the vendor's own site, https://www.10pr.ca/contact (tools/org_contacts.py, org_extras.py); website: https://www.10pr.ca/ (site answers)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Active (Canada's Business Registries, AB 2019137591, 2026-11-08)
- **vendor_incorporation_date**: 2015-08-10
- **vendor_years_in_business**: 11.2 (since 2015-08-10, registry date)
- **vendor_bn_source**: registry: Canada's Business Registries, AB 2019137591, 2026-11-08

## Contract
- **contract_status**: client listing on the vendor's own site (undated)
- **contract_title**: Success Stories – 10 Percent Recruiting Ltd. – Professional Recruitment Agency in Canada
- **contract_description**: Success Stories – 10 Percent Recruiting Ltd. – Professional Recruitment Agency in Canada (the record's title; the source publishes no separate description)
- **contract_link**: https://www.10pr.ca/success-stories
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 779857127RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (AB) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 794817494RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: BinaryLogic Inc — 10055-106 ST NW , Edmonton, AB T5J 2Y2 — buyer tax no. 779857127 (Canada's Business Registries, AB 2019517784, 2026-11-08) ⏎ SUBMIT TO: hello@01logic.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: 10 PERCENT RECRUITING LTD. (as registered: Canada's Business Registries, AB 2019137591, 2026-11-08) — 10160 103 St NW, Edmonton, Alberta, T5J0X6, Canada | GST/HST 794817494 (Canada's Business Registries, AB 2019137591, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Success Stories – 10 Percent Recruiting Ltd. – Professional Recruitment Agency in Canada
- **invoice_card_json**: {"bill_to": {"legal_name": "BinaryLogic Inc", "legal_name_is_published": true, "address": "10055-106 ST NW , Edmonton, AB T5J 2Y2", "address_is_the_invoice_address": false, "tax_number": "779857127 (Canada's Business Registries, AB 2019517784, 2026-11-08)", "language": "en"}, "submit_to": {"email": "hello@01logic.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (AB)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "794817494RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "10 PERCENT RECRUITING LTD. (as registered: Canada's Business Registries, AB 2019137591, 2026-11-08)", "bn9": "794817494 (Canada's Business Registries, AB 2019137591, 2026-11-08)", "neq": "", "re
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["hello@01logic.ca (general)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://www.01logic.ca/", "quote: \"e. Discover actionable insights and connect with our team to start your journey toward a more secure, efficient, and future-ready business. hello@01logic.ca Get\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-08429"], "buyer_facts": ["address and phone: the buyer's own site, https://www.01logic.ca/contact/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "registry identity: 2019137591 (AB) status Active (Canada's Business Registries, AB 2019137591, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data", "match)", "BN9: registry: Canada's Business Registries, AB 2019137591, 2026-1

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.01logic.ca/ | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, 01logic.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: BinaryLogic Inc
- **legal_name_url**: https://www.01logic.ca/
- **legal_name_quote**: utions Business Continuity IT Consulting & Staffing hello@01logic.ca (780) 665-6677 Follow Us ©2017 BinaryLogic Inc. | Privacy Policy | Terms & Conditions
- **logo_url**: https://www.01logic.ca/wp-content/uploads/images/01LOGIC-Logo-Rev8-220x45.png
- **logo_basis**: logo image in the site header
- **domain**: 01logic.ca
- **key**: lead:6f7adb4bc49e33d5
- **name**: BinaryLogic Inc
- **website**: https://01logic.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Search Engine Optimization
- **legal_name_stated_url**: https://www.01logic.ca/services/web-solutions/
- **legal_name_stated_quote**: ms like WordPress WordPress Management & Support – Plugin updates, content management, and training Search Engine Optimization (SEO) – Improve visibility and reach your audience effectively Security & Compliance – SSL, audits
- **mentions**: {'payment_method': {'text': 'interaction or does something unexpected, we express appreciation and recognition as lo', 'url': 'https://www.01logic.ca/', 'quote': 'yee and leader relationships. When a member of our team ‘wows’ one of our clients with a particular interaction or does something unexpected, we express appreciation and recognition as loudly as possible to help foster a positive workplace. Our aim has always'}}
- **linkedin_url**: https://www.linkedin.com/company/binarylogic/
- **tel_links**: +17806656677

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "10055-106 ST NW , Edmonton, AB T5J 2Y2", "address_country": "CA", "address_url": "https://www.01logic.ca/contact/", "address_method": "pattern", "address_quote": "eds. Book An Online Meeting Mailing address #1000, 10055-106 ST NW Edmonton, AB T5J 2Y2 Canada @theWORKUP Open in Map Let’s Talk hello@01logic.ca (780) 665-6677 OFFICE", "emails": "hello@01logic.ca", "emails_url": "https://www.01logic.ca/contact/", "domain": "01logic.ca", "key": "lead:6f7adb4bc49e33d5", "name": "01logic.ca", "website": "https://01logic.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, 10pr.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: 10 Percent Recruiting Ltd
- **legal_name_url**: https://www.10pr.ca/
- **legal_name_quote**: 10 Percent Recruiting Ltd. – Professional Recruitment Agency in Canada – The Evolution of Recruiting Skip to main content Hom
- **logo_url**: https://www.10pr.ca/wp-content/uploads/yootheme/cache/a6/10PR-Logo-Mobile-725x150-including-Canada-001b-a67ee5cb.png
- **logo_basis**: logo image in the site header
- **domain**: 10pr.ca
- **key**: vendor:10 Percent Recruiting Ltd.
- **name**: 10 Percent Recruiting Ltd.
- **website**: https://10pr.ca/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **mentions**: {'payment_method': {'text': 'interactions Embracing our fundamental business values provides our leaders and employe', 'url': 'https://www.10pr.ca/about', 'quote': 'd professionals, allows us to find your perfect fit. Our Core Values Guide our client and candidate interactions Embracing our fundamental business values provides our leaders and employees with a sense of purpose, creating the foundation for building a thrivi'}}
- **linkedin_url**: https://ca.linkedin.com/company/10percentrecruiting
- **tel_links**: +17806659290

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "10055-106 ST NW, Edmonton, AB T5J 2Y2", "address_country": "CA", "address_url": "https://www.10pr.ca/contact", "address_method": "pattern", "address_quote": "000, 10055-106 ST NW, Edmonton, AB Edmonton #1000, 10055-106 ST NW Edmonton, AB T5J 2Y2 (@theWORKUP) Contact Office: (780) 665-9290 Mail: hello@10pr.ca Hours: Mon – Fr", "phone": "+17806659290", "phone_url": "https://www.10pr.ca/contact", "emails": "hello@10pr.ca", "emails_url": "https://www.10pr.ca/contact", "domain": "10pr.ca", "key": "vd:10pr.ca", "name": "10 Percent Recruiting Ltd.", "website": "https://10pr.ca/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | BinaryLogic Inc | found | BINARYLOGIC INC. | 779857127 | 2019517784 | AB | Alberta Business Corporation | Active | 2016-03-09 | EDMONTON | AB |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=BinaryLogic%20Inc | 2026-11-08 |
| buyer | 10 Percent Recruiting Ltd. | found | 10 PERCENT RECRUITING LTD. | 794817494 | 2019137591 | AB | Alberta Business Corporation | Active | 2015-08-10 | EDMONTON | AB |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=10%20Percent%20Recruiting%20Ltd. | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | BinaryLogic Inc |  |  |  |  |  |  |  |  |  |  |
| b | 10 Percent Recruiting Ltd. |  |  |  |  |  |  |  |  |  |  |
| v | 10 Percent Recruiting Ltd |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:6f7adb4bc49e33d5",
 "ap_contact_team": {
  "emails": [
   "hello@01logic.ca",
   "info@01logic.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "hello@01logic.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.01logic.ca/",
    "quote": "e. Discover actionable insights and connect with our team to start your journey toward a more secure, efficient, and future-ready business. hello@01logic.ca Get in Touch Today Focus on your business and not your IT Ready to transform your IT experience? BinaryLogic delivers expert guidance",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "01logic.ca",
    "task_id": "CL-LD-08429"
   },
   {
    "email": "info@01logic.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.01logic.ca/assets/Manufacturing_eBook.pdf",
    "quote": "o safeguard the credibility of your practice the same way you safeguard the credibility of your clients. Call BinaryLogic today at 780-665- info@01logic.ca 6677 for a free assessment, no-obligation assessment of your practice’s www.01logic.ca backup and recovery needs. Sources: 1Beyond Tec",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "01logic.ca",
    "task_id": "CL-LD-08429"
   }
  ]
 },
 "research_status": {
  "found": 2
 },
 "queries_tried": [
  "site crawl of 01logic.ca (20 pages, robots.txt respected), no AI, no search engine",
  "site crawl of 01logic.ca (20 pages, robots.txt respected), no AI, no search engine"
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
| ca_alberta_apc:AB-2024-02159:13fd687f-b6fc-5d66-1dac-90835e090000 | Alberta Innovates | Alberta Innovates - Request for Proposal - Pre-Qualified Resource (PQR) Vendors for Information Technology Services |  |  |  | https://purchasing.alberta.ca/posting/AB-2024-02159 |

## Open questions for hand research (layer 2)

- an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed)
- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
