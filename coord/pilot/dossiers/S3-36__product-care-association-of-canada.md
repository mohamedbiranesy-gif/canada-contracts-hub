# S3-36 — PRODUCT CARE ASSOCIATION OF CANADA ⇄ LOOP RECYCLED PRODUCTS INC

Stratum: **S3_routed_public_body_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Explore: About Us Members Service Partners Blog & — 420 – 2238 Yukon St. , Vancouver BC V5Y 3P2
SUBMIT TO: contact@productcare.org (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: LOOP RECYCLED PRODUCTS INC. (as registered: Canada's Business Registries, ON 2337398, 2026-11-08) — contractor_address: 600 READ ROAD, ST CATHARINES, ON, L2R 7K6 | GST/HST 800592289 (Canada's Business Registries, ON 2337398, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their | CURRENCY: USD (derived from the source's government) | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: COLLECTION SITE | AMOUNT: 2756580 (source field: amount) USD
```

## Relationship
- **rank_group**: L1
- **data_quality_score**: 46
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 7
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: PRODUCT CARE ASSOCIATION OF CANADA (non-profit / association / cultural body, jurisdiction not stated) — dated deal or payment 12 to 36 months ago: LOOP RECYCLED PRODUCTS INC | subject: COLLECTION SITE | value: 2756580 (source field: amount) USD (derived from the source's government) | awarded 2024-12-31, end 2024-12-31 | published by: contractor address country (IRS Form 990) | record: https://projects.propublica.org/nonprofits/organizations/980701785/202502239349302140/full | vendor in Canada because: contractor address country (IRS Form 990)=CA - 600 READ ROAD, ST CATHARINES, ON, L2R 7K6 | status rule: likely active (awarded 12-36 months ago; paid in a fiscal year ending 12-36 months ago: IRS Form 990 contractor located in Canada)
- **how_relationship_was_found**: a dated public record (payment register, subaward, vendor news release or EDC transaction) 12 to 36 months old, harvested by the lead scanners
- **keys**: lead:76709d2247f1b7ee
- **tier**: L
- **grade**: 1
- **records_with_this_vendor**: 1 (relationship record: contractor address country (IRS Form 990); 0 in the contract dataset)

## Buyer
- **buyer**: PRODUCT CARE ASSOCIATION OF CANADA
- **buyer_website**: https://productcare.org/
- **buyer_address**: 420 – 2238 Yukon St. , Vancouver BC V5Y 3P2
- **buyer_phone**: 1-877-592-2972, ext. 426
- **buyer_contact_evidence_url**: https://www.productcare.org/contact/
- **buyer_legal_name_as_published**: Explore: About Us Members Service Partners Blog &
- **buyer_logo_url**: https://www.productcare.org/wp-content/uploads/2018/12/Home_Hero-min.jpg
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/productcarerecycling/
- **buyer_type**: non-profit / association / cultural body
- **buyer_sector**: non-profit
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.productcare.org/contact/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: contact@productcare.org
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://www.productcare.org/
- **email_evidence_quote**: xplore: About Us Members Service Partners Blog & News Careers Privacy Policy Annual Reports Contact: 604-592-2972 Toll Free: 1-877-592-2972 contact@productcare.org Connect with us: 🇨🇦 Made with pride in Canada Find a Recycling Location
- **email_evidence_context**: rated not-for-profit company offering product stewardship services across Canada. 2026. All Rights Reserved. Explore: About Us Members Service Partners Blog & News Careers Privacy Policy Annual Reports Contact: 604-592-2972 Toll Free: 1-877-592-2972 contact@productcare.org Connect with us: 🇨🇦 Made with pride in Canada Find a Recycling Location (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: contact@productcare.org (general) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-02 | page: https://www.productcare.org/ | quote: "xplore: About Us Members Service Partners Blog & News Careers Privacy Policy Annual Reports Contact: 604-592-2972 Toll Free: 1-877-592-2972 contact@productcare." | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); DNS lookup failed; mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LT-01118
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); DNS lookup failed; mail handled by Microsoft 365
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none;
- **dmarc_record_domain**: productcare.org
- **spf_policy**: DNS lookup failed
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Explore: About Us Members Service Partners Blog & — 420 – 2238 Yukon St. , Vancouver BC V5Y 3P2 ⏎ SUBMIT TO: contact@productcare.org (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: LOOP RECYCLED PRODUCTS INC. (as registered: Canada's Business Registries, ON 2337398, 2026-11-08) — contractor_address: 600 READ ROAD, ST CATHARINES, ON, L2R 7K6 | GST/HST 800592289 (Canada's Business Registries, ON 2337398, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their | CURRENCY: USD (derived from the source's government) | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: COLLECTION SITE | AMOUNT: 2756580 (source field: amount) USD
- **invoice_card_json**: {"bill_to": {"legal_name": "Explore: About Us Members Service Partners Blog &", "legal_name_is_published": true, "address": "420 – 2238 Yukon St. , Vancouver BC V5Y 3P2", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "contact@productcare.org", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (BC)", "currency": "USD (derived from the source's government)", "currency_is_published": true, "vendor_gst_hst": "800592289RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "LOOP RECYCLED PRODUCTS INC. (as registered: Canada's Business Registries, ON 2337398, 2026-11-08)", "bn9": "800592289 (Canada's Business Registries, ON 2337398, 2026-11-08)", "neq": "", "remit_address": "Niagara Falls, Onta
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
- **vendor**: LOOP RECYCLED PRODUCTS INC
- **vendor_legal_name**: LOOP RECYCLED PRODUCTS INC. (as registered: Canada's Business Registries, ON 2337398, 2026-11-08)
- **vendor_registry_id**: 2337398 (ON)
- **vendor_registry_url**: https://ised-isde.canada.ca/cbr-rec/en/search?q=LOOP%20RECYCLED%20PRODUCTS%20INC
- **vendor_registered_address**: Niagara Falls, Ontario (registered office city / province; Canada's Business Registries, ON 2337398, 2026-11-08)
- **vendor_legal_form**: ONTARIO BUSINESS CORP. (Canada's Business Registries, ON 2337398, 2026-11-08)
- **vendor_address**: contractor_address: 600 READ ROAD, ST CATHARINES, ON, L2R 7K6
- **vendor_country_basis**: contractor address country (IRS Form 990)=CA - 600 READ ROAD, ST CATHARINES, ON, L2R 7K6
- **vendor_bn9**: 800592289 (Canada's Business Registries, ON 2337398, 2026-11-08)
- **vendor_gst_hst_derived**: 800592289RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_facts_provenance**: name and address: the record's vendor block (contractor address country (IRS Form 990)); registry identity: 2337398 (ON) status Active — incorporated (Canada's Business Registries, ON 2337398, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: registry: Canada's Business Registries, ON 2337398, 2026-11-08; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2012-07-31
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Active — incorporated (Canada's Business Registries, ON 2337398, 2026-11-08)
- **vendor_incorporation_date**: 2012-07-31
- **vendor_years_in_business**: 14.3 (since 2012-07-31, registry date)
- **vendor_bn_source**: registry: Canada's Business Registries, ON 2337398, 2026-11-08

## Contract
- **contract_status**: likely active (awarded 12-36 months ago; paid in a fiscal year ending 12-36 months ago: IRS Form 990 contractor located in Canada)
- **contract_title**: COLLECTION SITE
- **contract_description**: COLLECTION SITE (the record's title; the source publishes no separate description)
- **contract_value**: 2756580 (source field: amount)
- **currency**: USD (derived from the source's government)
- **award_date**: 2024-12-31
- **end_date**: 2024-12-31
- **contract_link**: https://projects.propublica.org/nonprofits/organizations/980701785/202502239349302140/full
- **source**: contractor address country (IRS Form 990)
- **contracts_with_canadian_suppliers**: 5
- **records_with_this_vendor**: 1 (relationship record: contractor address country (IRS Form 990); 0 in the contract dataset)
- **records_in_contract_dataset**: 5 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (BC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **vendor_gst_hst_derived**: 800592289RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Explore: About Us Members Service Partners Blog & — 420 – 2238 Yukon St. , Vancouver BC V5Y 3P2 ⏎ SUBMIT TO: contact@productcare.org (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: LOOP RECYCLED PRODUCTS INC. (as registered: Canada's Business Registries, ON 2337398, 2026-11-08) — contractor_address: 600 READ ROAD, ST CATHARINES, ON, L2R 7K6 | GST/HST 800592289 (Canada's Business Registries, ON 2337398, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their | CURRENCY: USD (derived from the source's government) | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: COLLECTION SITE | AMOUNT: 2756580 (source field: amount) USD
- **invoice_card_json**: {"bill_to": {"legal_name": "Explore: About Us Members Service Partners Blog &", "legal_name_is_published": true, "address": "420 – 2238 Yukon St. , Vancouver BC V5Y 3P2", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "contact@productcare.org", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (BC)", "currency": "USD (derived from the source's government)", "currency_is_published": true, "vendor_gst_hst": "800592289RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "LOOP RECYCLED PRODUCTS INC. (as registered: Canada's Business Registries, ON 2337398, 2026-11-08)", "bn9": "800592289 (Canada's Business Registries, ON 2337398, 2026-11-08)", "neq": "", "remit_address": "Niagara Falls, Onta
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["contact@productcare.org (general)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-02", "page: https://www.productcare.org/", "quote: \"xplore: About Us Members Service Partners Blog & News Careers Privacy Policy Annual Reports Contact: 604-592-2972 Toll Free: 1-877-592-2972 contact@productcare.\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); DNS lookup failed; mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LT-01118"], "buyer_facts": ["address and phone: the buyer's own site, https://www.productcare.org/contact/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (contractor address country (IRS Form 990))", "registry identity: 2337398 (ON) status Active — incorporated (Canada's Business Registries, ON 2337398, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data", "match)", "BN9: registry: Canada's Business Registries, ON 2337398, 2026-11-08", "GST/HST derived BN9 + RT0001 (CRA registry is CAPTCH

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.productcare.org/ | 2026-11-08 | ok |  |  |  | 604-592-2972 |  |  |  |  |  |

## Buyer site facts (org_extras, productcare.org)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: Explore: About Us Members Service Partners Blog & News Careers
- **legal_name_url**: https://www.productcare.org/
- **legal_name_quote**: for-profit company offering product stewardship services across Canada. 2026. All Rights Reserved. Explore: About Us Members Service Partners Blog & News Careers Privacy Policy Annual Reports Contact: 604-592-2972 Toll Free: 1-877-592-2972 contact@productcare.o
- **logo_url**: https://www.productcare.org/wp-content/uploads/2018/12/Home_Hero-min.jpg
- **logo_basis**: og:image of the home page (looks like a photo, not a logo: check before use)
- **domain**: productcare.org
- **key**: lead:76709d2247f1b7ee
- **name**: PRODUCT CARE ASSOCIATION OF CANADA
- **website**: https://productcare.org/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Product Care Association
- **legal_name_stated_url**: https://www.productcare.org/about/
- **legal_name_stated_quote**: s well as non-financial audits to verify the collection system and quantities managed and recycled. Product Care Association of Canada (PCA), is a federally incorporated not-for-profit company offering product stewardship se
- **linkedin_url**: https://www.linkedin.com/company/productcarerecycling/
- **tel_links**: 16045922972; 18775922972

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "420 – 2238 Yukon St. , Vancouver BC V5Y 3P2", "address_country": "CA", "address_url": "https://www.productcare.org/contact/", "address_method": "pattern", "address_quote": "a recycling location contact@productcare.org 420 – 2238 Yukon St. Vancouver BC V5Y 3P2 Canada 604-592-2972 Toll Free: 1 (877) 592-2972 Fax: 604-592-2982 Product Care", "phone": "1-877-592-2972, ext. 426", "phone_url": "https://www.productcare.org/contact/", "emails": "contact@productcare.org", "emails_url": "https://www.productcare.org/contact/", "domain": "productcare.org", "key": "lead:76709d2247f1b7ee", "name": "PRODUCT CARE ASSOCIATION OF CANADA", "website": "https://productcare.org/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, domain unknown)
_not read_

## Vendor role mailboxes found on its site (org_contacts)
_not read_

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | PRODUCT CARE ASSOCIATION OF CANADA | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=PRODUCT%20CARE%20ASSOCIATION%20OF%20CANADA | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | api_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | PRODUCT CARE ASSOCIATION OF CANADA | not_found |  |  |  | Corporations Canada (open data) |  |  |  |  |  |  | https://open.canada.ca/data/en/dataset/0032ce54-c5dd-4b66-99a0-320a7b5e99f2 | 2026-11-08 |

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | PRODUCT CARE ASSOCIATION OF CANADA |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:76709d2247f1b7ee",
 "ap_contact_team": {
  "emails": [
   "contact@productcare.org"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "contact@productcare.org",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.productcare.org/",
    "quote": "xplore: About Us Members Service Partners Blog & News Careers Privacy Policy Annual Reports Contact: 604-592-2972 Toll Free: 1-877-592-2972 contact@productcare.org Connect with us: 🇨🇦 Made with pride in Canada Find a Recycling Location",
    "retrieved_date": "2026-11-02",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "PRODUCT CARE ASSOCIATION OF CANADA",
    "task_id": "CL-LT-01118"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of productcare.org (8 pages, robots.txt respected), no AI, no search engine"
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
