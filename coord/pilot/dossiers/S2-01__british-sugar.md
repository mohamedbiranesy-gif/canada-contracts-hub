# S2-01 — British Sugar ⇄ IBM Canada

Stratum: **S2_complete_no_published_PO_rule** · pay on sight: yes — reference rule not published (quote the buyer's PO / order number when one is issued) · channel tier 1 · AP grade C · missing: (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Associated British Foods plc (stated on https://www.britishsugar.co.uk/about-us/what-we-do/) — 315158 at Weston Centre, 10 Grosvenor Street, London W1K 4QY
SUBMIT TO: accounts.payable@britishsugar.com (invoicing/AP mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: IBM Canada — IBM Canada Head Office Building (headquarters per Wikidata Q1653092; not the registered address) | GST/HST 102444452 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2011-07-04; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9)
TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); UK VAT is | CURRENCY: DERIVED: GBP (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: British Sugar | IBM
```

## Relationship
- **rank_group**: D4
- **data_quality_score**: 68
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: British Sugar (organisation (type not stated in the record), jurisdiction not stated) — named as a client by the Canada-located vendor (client list / customer story), dated: IBM Canada | subject: British Sugar | IBM | published by: the Canada-located vendor's own website | record: https://www.ibm.com/case-studies/british-sugar | vendor in Canada because: vendor located in Canada (stories; Wikidata country + address on its site)=ibm.com | status rule: client listing on the vendor's own site (undated)
- **how_relationship_was_found**: tools/client_lists.py / dated_stories.py read the vendor's dated customer story / case study naming the buyer
- **keys**: lead:98df879d001d807e
- **tier**: D
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: British Sugar
- **buyer_website**: https://britishsugar.co.uk/
- **buyer_address**: 315158 at Weston Centre, 10 Grosvenor Street, London W1K 4QY
- **buyer_phone**: +44 (0) 1733 563171
- **buyer_contact_evidence_url**: https://www.britishsugar.co.uk/contact-us
- **buyer_legal_name_as_published**: Associated British Foods plc (stated on https://www.britishsugar.co.uk/about-us/what-we-do/)
- **buyer_logo_url**: https://www.britishsugar.co.uk/images/bs-logo-white.svg
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/22922/
- **buyer_type**: company (private sector) (from the organisation's name / web domain)
- **buyer_sector**: private sector
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q4971114; business
- **buyer_founded**: 1936-01-01 (Wikidata Q4971114, official website on the organisation's domain (http://www.britishsugar.co.uk) + name; 2026-11-08)
- **buyer_legal_form**: public limited company (Wikidata Q4971114, official website on the organisation's domain (http://www.britishsugar.co.uk) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.britishsugar.co.uk/contact-us (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); UK VAT is accounted for by the buyer under the reverse charge where applicable
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: accounts.payable@britishsugar.com
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.britishsugar.co.uk/contact-us.php
- **email_evidence_quote**: lass="half"> <p><strong>Accounts Payable</strong></p> <p><strong>T: </strong>+44 (0) 8450 230051</p> <p><strong>E:</strong> <a href="mailto:accounts.payable@britishsugar.com">accounts.payable@britishsugar.com</a></p> <p> </p> </div> </div> <div class="clear"></div> </div> </div> <div id="r
- **mailbox_provenance**: accounts.payable@britishsugar.com (invoicing/AP) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://www.britishsugar.co.uk/contact-us.php | quote: "lass="half"> <p><strong>Accounts Payable</strong></p> <p><strong>T: </strong>+44 (0) 8450 230051</p> <p><strong>E:</strong> <a href="mailto:accounts.payable@bri" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-06353
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by Microsoft 365
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1;p=reject;rua=mailto:bstnx4lf@ag.eu.dmarcadvisor.com
- **dmarc_record_domain**: britishsugar.com
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 include:spf.protection.outlook.com include:spf.abfoods.com include:spf-001e4301.pphosted.com include:_spf.salesforce.com ip4:62.32.118.235 ip4:52.59.58.195 ip4:3.122.45.38 ip4:52.58.98.157 ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: GBP (derived from the buyer's country; CAD if the parties agreed so)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Associated British Foods plc (stated on https://www.britishsugar.co.uk/about-us/what-we-do/) — 315158 at Weston Centre, 10 Grosvenor Street, London W1K 4QY ⏎ SUBMIT TO: accounts.payable@britishsugar.com (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: IBM Canada — IBM Canada Head Office Building (headquarters per Wikidata Q1653092; not the registered address) | GST/HST 102444452 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2011-07-04; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); UK VAT is | CURRENCY: DERIVED: GBP (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: British Sugar | IBM
- **invoice_card_json**: {"bill_to": {"legal_name": "Associated British Foods plc (stated on https://www.britishsugar.co.uk/about-us/what-we-do/)", "legal_name_is_published": true, "address": "315158 at Weston Centre, 10 Grosvenor Street, London W1K 4QY", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "accounts.payable@britishsugar.com", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); UK VAT is", "buyer_tax_status_is_published": false, "indicative_rate": "", "currency": "DERIVED: GBP (derived from the buyer's country; C", "currency_is_published": false, "vendor_gst_hst": "102444452RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "IBM Canada", "bn9": "102444452 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2011-07-04; https://open.can
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 71
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: IBM Canada
- **vendor_address**: IBM Canada Head Office Building (headquarters per Wikidata Q1653092; not the registered address)
- **vendor_country_basis**: vendor located in Canada (stories; Wikidata country + address on its site)=ibm.com
- **vendor_bn9**: 102444452 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2011-07-04; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)
- **vendor_gst_hst_derived**: 102444452RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://ibm.com
- **vendor_logo_url**: https://assets.ibm.com/is/image/ibm/blue-pearl-logo-2x1-v2-1?ts=1782225217040&dpr=off
- **vendor_linkedin_url**: https://www.linkedin.com/company/ibm
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); BN9: federal grants & contributions disclosure (recipient_business_number); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); website: https://ibm.com
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_wikidata**: https://www.wikidata.org/wiki/Q1653092; business
- **vendor_founded**: 1917-00-00 (Wikidata Q1653092, official website on the organisation's domain (http://www.ibm.com/ca/en/) + name; 2026-11-08)
- **vendor_bn_source**: federal grants & contributions disclosure (recipient_business_number)

## Contract
- **contract_status**: client listing on the vendor's own site (undated)
- **contract_title**: British Sugar | IBM
- **contract_description**: British Sugar | IBM (the record's title; the source publishes no separate description)
- **contract_link**: https://www.ibm.com/case-studies/british-sugar
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 2
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: 2 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); UK VAT is accounted for by the buyer under the reverse charge where applicable
- **invoice_currency_derived**: GBP (derived from the buyer's country; CAD if the parties agreed so)
- **vendor_gst_hst_derived**: 102444452RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: yes — reference rule not published (quote the buyer's PO / order number when one is issued)
- **pay_on_sight_missing**: (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Associated British Foods plc (stated on https://www.britishsugar.co.uk/about-us/what-we-do/) — 315158 at Weston Centre, 10 Grosvenor Street, London W1K 4QY ⏎ SUBMIT TO: accounts.payable@britishsugar.com (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: IBM Canada — IBM Canada Head Office Building (headquarters per Wikidata Q1653092; not the registered address) | GST/HST 102444452 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2011-07-04; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); UK VAT is | CURRENCY: DERIVED: GBP (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: British Sugar | IBM
- **invoice_card_json**: {"bill_to": {"legal_name": "Associated British Foods plc (stated on https://www.britishsugar.co.uk/about-us/what-we-do/)", "legal_name_is_published": true, "address": "315158 at Weston Centre, 10 Grosvenor Street, London W1K 4QY", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "accounts.payable@britishsugar.com", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); UK VAT is", "buyer_tax_status_is_published": false, "indicative_rate": "", "currency": "DERIVED: GBP (derived from the buyer's country; C", "currency_is_published": false, "vendor_gst_hst": "102444452RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "IBM Canada", "bn9": "102444452 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2011-07-04; https://open.can
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 71
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["accounts.payable@britishsugar.com (invoicing/AP)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://www.britishsugar.co.uk/contact-us.php", "quote: \"lass=\"half\"> <p><strong>Accounts Payable</strong></p> <p><strong>T: </strong>+44 (0) 8450 230051</p> <p><strong>E:</strong> <a href=\"mailto:accounts.payable@bri\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-06353"], "buyer_facts": ["address and phone: the buyer's own site, https://www.britishsugar.co.uk/contact-us (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "BN9: federal grants & contributions disclosure (recipient_business_number)", "GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected", "not automated)", "website: https://ibm.com"], "relationship": "tools/client_lists.py / dated_stories.py read the vendor's dated customer story / case study naming the buyer"}

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.britishsugar.co.uk/contact-us.php | 2026-11-08 | blocked |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, britishsugar.co.uk)
- **status**: ok
- **pages**: 3
- **language**: en
- **logo_url**: https://www.britishsugar.co.uk/images/bs-logo-white.svg
- **logo_basis**: logo image in the site header
- **domain**: britishsugar.co.uk
- **key**: lead:98df879d001d807e
- **name**: British Sugar
- **website**: https://britishsugar.co.uk/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Associated British Foods plc
- **legal_name_stated_url**: https://www.britishsugar.co.uk/about-us/what-we-do/
- **legal_name_stated_quote**: r is part of ABF Sugar , which is wholly owned by international food, ingredients and retail group, Associated British Foods plc (ABF)? Click here to learn more. Accessibility BS User Cookies ABF Modern Slavery Statement Privacy
- **linkedin_url**: https://www.linkedin.com/company/22922/

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "315158 at Weston Centre, 10 Grosvenor Street, London W1K 4QY", "address_country": "GB", "address_url": "https://www.britishsugar.co.uk/contact-us", "address_method": "pattern", "address_quote": "Terms Site map Terms and Conditions British Sugar plc Registered in England No. 315158 at Weston Centre 10 Grosvenor Street London W1K 4QY", "phone": "+44 (0) 1733 563171", "phone_url": "https://www.britishsugar.co.uk/contact-us", "emails": "communications@britishsugar.com", "emails_url": "https://www.britishsugar.co.uk/contact-us", "domain": "britishsugar.co.uk", "key": "lead:98df879d001d807e", "name": "British Sugar", "website": "https://britishsugar.co.uk/", "kind": "buyer", "date": "2026-11-04"}

## Vendor site facts (org_extras, ibm.com)
- **status**: ok
- **pages**: 2
- **language**: fr
- **logo_url**: https://assets.ibm.com/is/image/ibm/blue-pearl-logo-2x1-v2-1?ts=1782225217040&dpr=off
- **logo_basis**: logo image in the site header
- **domain**: ibm.com
- **key**: vendor:IBM Canada
- **name**: IBM Canada
- **website**: https://ibm.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Corporation
- **jsonld_name**: IBM
- **jsonld_legal_name**: International Business Machines Corporation
- **jsonld_logo**: https://www.ibm.com/brand/experienceguides/developer/b1db1ae501d522a1a4b49613fe07c9f1/01_8-bar-positive.svg
- **jsonld_url**: https://www.ibm.com/
- **jsonld_founding_date**: 1911-06-16
- **jsonld_same_as**: https://en.wikipedia.org/wiki/IBM; https://www.wikidata.org/wiki/Q37156; https://www.linkedin.com/company/ibm; https://x.com/IBM; https://www.youtube.com/ibm; https://github.com/IBM
- **jsonld_quote**: { "@context": "https://schema.org", "@graph": [ { "@type": "Corporation", "@id": "https://www.ibm.com/#organization", "name": "IBM", "legalName": "International Business Machines Corporation", "url": "https://www.ibm.com/", "logo": "https://www.ibm.com/brand/experienceguides/developer/b1db1ae501d522
- **jsonld_page**: https://www.ibm.com/ca-fr
- **linkedin_url**: https://www.linkedin.com/company/ibm

## Vendor role mailboxes found on its site (org_contacts)
_not read_

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | British Sugar | Q4971114 | official website on the organisation's domain (http://www.britishsugar.co.uk) + name |  | British Sugar | British Sugar | business | public limited company | United Kingdom | 1936-01-01 | Peterborough |
| b | IBM | Q37156 | official website on the organisation's domain (https://www.ibm.com/) + name | International Business Machines Corporation [en] | IBM |  | software company; business; enterprise; technology company; public company; professional services firm; multinational corporation; organization | corporation | United States | 1911-06-16 | Armonk |
| v | IBM Canada | Q1653092 | official website on the organisation's domain (http://www.ibm.com/ca/en/) + name |  | IBM Canada |  | business |  | Canada | 1917-00-00 | IBM Canada Head Office Building |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:98df879d001d807e",
 "ap_contact_team": {
  "emails": [
   "accounts.payable@britishsugar.com"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "accounts.payable@britishsugar.com",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.britishsugar.co.uk/contact-us.php",
    "quote": "lass=\"half\"> <p><strong>Accounts Payable</strong></p> <p><strong>T: </strong>+44 (0) 8450 230051</p> <p><strong>E:</strong> <a href=\"mailto:accounts.payable@britishsugar.com\">accounts.payable@britishsugar.com</a></p> <p> </p> </div> </div> <div class=\"clear\"></div> </div> </div> <div id=\"r",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "British Sugar",
    "task_id": "CL-LD-06353"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of britishsugar.co.uk (8 pages, robots.txt respected), no AI, no search engine"
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

## The vendor's other buyers in the dataset (first 60 of 300)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_alberta_apc:AB-2024-10023:812dc76f-d7e3-4530-8d19-23bea5dedaff | Alberta Energy Regulator | Alberta Energy Regulator - Request for Proposal - Cloud Service Providers |  |  |  | https://purchasing.alberta.ca/posting/AB-2024-10023 |
| ca_alberta_apc:AB-2024-10126:fd66811c-5720-4d6a-ae55-e84e5066a9c0 | Technology and Innovation | Technology and Innovation - Negotiated Request for Proposal - Application Services for Motor Vehicle Application Maintenance Services for MV Suite of custom-bui | 11265710.0 |  |  | https://purchasing.alberta.ca/posting/AB-2024-10126 |
| ca_alberta_apc:AB-2025-00890:cfc18834-c88a-447c-b6f8-2bf001391670 | Alberta Electric System Operator | Alberta Electric System Operator - Request for Proposal - Penetration Testing Services | 40000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-00890 |
| ca_alberta_apc:AB-2025-06207:33e9d8ce-06f3-4829-9ade-c4092ae4088d | City of Red Deer | City of Red Deer - Negotiated Request for Proposal - Contact Center as a Service and Implementation Services | 265577.32 |  |  | https://purchasing.alberta.ca/posting/AB-2025-06207 |
| ca_alberta_sole_source:7af2a4d0121c8009 | Health | To provide an Enterprise License Agreement between Alberta Health and IBM for the current IBM subscription and support renewals. | 24821058.0 |  |  | https://www.alberta.ca/sole-source-contracts-disclosure-table |
| ca_bc_ministry_awards:67991fcaa8a4bebb | Ministry of Health | IBM WebSphere License Renewal (Victoria) | 321863.94 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:bfdbac5fb5f693c7 | Ministry of Social Development and Social Innovation | IBM DB2 Connect Enterprise Edition, Subscription Renewal | 14295.67 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:0111a98464320707 | Ministry of Social Development and Poverty Reduction | IBM Support Renewal (Victoria) | 15181.49 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:7e07f85f77777852 | Ministry of Education | ShareEdBC Operational Management and Support | 3600000.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/7fed5fea-1b3d-4714-ab76-20b69a62a674/download/ministry-contract-awards-oct-to-dec-2021.csv |
| ca_bidsandtenders:ff869080-dcee-485d-9fc4-fdf35fef0010:1 | City of Burnaby | Re-Opening Pre-Qualification for System Implementation Partners S4 HANA ERP Transformation Project |  |  |  | https://burnaby.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/ff869080-dcee-485d-9fc4-fdf35fef0010 |
| ca_bidsandtenders:9504e211-1eb1-4fb8-a608-6af5df27e810:1 | Region of Peel | IBM MAXIMO ENTERPRISE ASSET MANAGEMENT (EAM) SYSTEM IMPLEMENTATION SERVICES FOR THE REGION OF PEEL | 13483357.47 |  |  | https://peelregion.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/9504e211-1eb1-4fb8-a608-6af5df27e810 |
| ca_bidsandtenders:a26df980-64ac-4b42-a0ab-c1390787da0e:1 | City of Red Deer | Contact Center as a Service and Implementation Services | 265577.32 |  |  | https://reddeer.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/a26df980-64ac-4b42-a0ab-c1390787da0e |
| ca_bidsandtenders:763d4435-eb99-46d8-9543-c13283893d62:1 | City of Kitchener | SAP SuccessFactors Implementation |  |  |  | https://kitchener.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/763d4435-eb99-46d8-9543-c13283893d62 |
| ca_bidsandtenders:39aa8b76-dbcb-482d-81bc-69d7ee76cc39:1 | Lambton Kent District School Board | Consulting Services - Business Continuity Plan |  |  |  | https://lkdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/39aa8b76-dbcb-482d-81bc-69d7ee76cc39 |
| ca_bidsandtenders:42f31c2f-4d4c-4475-9154-66eff6347990:1 | York Region | Microsoft Data Warehouse and Business Intelligence |  |  |  | https://york.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/42f31c2f-4d4c-4475-9154-66eff6347990 |
| ca_bidsandtenders:9fabcfb3-6206-43d7-a755-73f9323651ab:5 | Government of Yukon | Identity Management Solutions and Partners |  |  |  | https://yukon.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/9fabcfb3-6206-43d7-a755-73f9323651ab |
| ca_bidsandtenders:919952cf-7ca8-4535-aceb-d780ba4bdda7:1 | York Catholic District School Board | Supply and Delivery of Chromebooks |  |  |  | https://ycdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/919952cf-7ca8-4535-aceb-d780ba4bdda7 |
| ca_bidsandtenders:fc80b599-def0-484e-9ef6-1c82d74573b7:4 | Government of Yukon | PeopleSoft Development and Support |  |  |  | https://yukon.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/fc80b599-def0-484e-9ef6-1c82d74573b7 |
| ca_bidsandtenders:ad5fe2db-6367-4b6f-98fb-01aee39dc455:1 | Government of Yukon | K-12 Request for Professional Services to Change Email Platforms | 135000.0 |  |  | https://yukon.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/ad5fe2db-6367-4b6f-98fb-01aee39dc455 |
| ca_bidsandtenders:b8f48352-f44b-477c-8d7d-3db78e82db33:1 | Region of Peel | Supply and Delivery of Lenovo Standalone Server Bundles | 590019.89 |  |  | https://peelregion.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/b8f48352-f44b-477c-8d7d-3db78e82db33 |
| ca_bidsandtenders:68c58ce8-4a64-4c6a-b72b-334538d1974a:1 | Government of Yukon | K-12 Education Student Bring Your Own Device Business Case | 74000.0 |  |  | https://yukon.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/68c58ce8-4a64-4c6a-b72b-334538d1974a |
| ca_bidsandtenders:c1913e0c-151b-4a8c-8273-280e6692f5f1:1 | Regional Municipality of Wood Buffalo | SAP SuccessFactors Implementation |  |  |  | https://rmwb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/c1913e0c-151b-4a8c-8273-280e6692f5f1 |
| ca_merx:2639653417:3 | Farm Credit Canada (FCC) | RFP – PRE-QUALIFICATION FOR STRATEGIC TRANSFORMATION SERVICES | 1250000.0 |  |  | https://www.merx.com/farmcreditcanadafcc/solicitations/RFP-PRE-QUALIFICATION-FOR-STRATEGIC-TRANSFORMATION-SERVICES/0000257329?origin=0 |
| ca_merx:2397807073:1 | Canadian Air Transport Security Authority | Time and Attendance System | 9400000.0 |  |  | https://www.merx.com/catsa/solicitations/Time-and-Attendance-System/0000240292?origin=0 |
| ca_merx:3287992050:1 | City of Ottawa | FCS/CFS/ Enterprise Resource Planning Renewal SAP S/4 HANA Modernization |  |  |  | https://www.merx.com/cityofottawa/buyer-6700/solicitations/FCS-CFS-Enterprise-Resource-Planning-Renewal-SAP-S-4-HANA-Modernization/0000284969?origin=0 |
| ca_merx:3262746104:1 | Greater Toronto Airports Authority | Maximo Application Health Assessment and options for Cloud Migration |  |  |  | https://www.merx.com/torontopearson/solicitations/Maximo-Application-Health-Assessment-and-options-for-Cloud-Migration/0000283812?origin=0 |
| ca_merx:2273662869:1 | Manitoba Public Insurance | Request for Proposal #3153 Vulnerability Management Solution | 227580.0 |  |  | https://www.merx.com/mbgov/mpi/solicitations/Request-for-Proposal-3153-Vulnerability-Management-Solution/0000230461?origin=0 |
| ca_merx:2274814047:1 | Manitoba Public Insurance | Request for Proposal #3154 Application Security Testing | 787656.9 |  |  | https://www.merx.com/mbgov/mpi/solicitations/Request-for-Proposal-3154-Application-Security-Testing/0000230648?origin=0 |
| ca_merx:2279836121:1 | The City of Winnipeg | PROVISION OF F5 MAINTENANCE | 108312.0 |  |  | https://www.merx.com/mbgov/cityofwinnipeg/solicitations/PROVISION-OF-F5-MAINTENANCE/0000231082?origin=0 |
| ca_merx:2156999902:6 | Export Development Canada - EDC | Enterprise Professional Services Supply Arrangement | 1.0 |  |  | https://www.merx.com/exportdevelopmentcanadaedc/solicitations/Enterprise-Professional-Services-Supply-Arrangement/0000220460?origin=0 |
| ca_newfoundland:7386daf6bde5c271 | Office of the Chief Information Officer | IBM And Lenovo Annual Post Warranty And Support | 547055.59 |  |  | https://www.gov.nl.ca/ppa/files/2026-Apr-1-15-Contract-Awards-Report.pdf |
| ca_newfoundland:cf4749cb854585d3 | Executive Council - Office of the Chief Information Officer | IBM and Lenovo - Annual Post Warranty and Support | 273119.37 |  |  | https://www.gov.nl.ca/ppa/files/Contract-Award-Report-2024-03-16-To-2024-03-31-KD-Edits.pdf |
| ca_newfoundland:082df8ad9d218966 | NL Health Services | Maintenance contract for software that comprises the HIAL of the provincial EHR | 69691.43 |  |  | https://www.gov.nl.ca/ppa/files/Contract-Award-Report-2025-08-16-To-2025-08-31.pdf |
| ca_newfoundland:0478b3d2cefa9677 | Executive Council | IBM and Lenovo Annual Post Warranty and Support | 261230.79 |  |  | https://www.gov.nl.ca/ppa/files/Contract-and-Exception-Awards-April-1-15-2023.pdf |
| ca_nwt:0000001480 | Finance | SAM-HRIS IBM Developer | 725760.0 |  |  | https://www.fin.gov.nt.ca/en/resources/contracts-over-5000-report?f%5B0%5D=field_resource_category_legacy%3A582 |
| ca_saskatchewan:ed3d2929-73f1-49de-961e-59c564839a65:2 | University of Saskatchewan | Negotiated Request for Proposals - Telephony Hardware and Services |  |  |  | https://www.sasktenders.ca/Competitions/Print?id=ed3d2929-73f1-49de-961e-59c564839a65 |
| ca_saskatchewan:64d8dc80-5920-4729-b6c0-11f7aed9d038:0 | Saskatchewan Health Authority | Sustainability Data Management System | 356267.92 |  |  | https://www.sasktenders.ca/Competitions/Print?id=64d8dc80-5920-4729-b6c0-11f7aed9d038 |
| ca_saskatchewan:3e273246-5f94-496a-a2f5-e15cda240411:0 | Highways | Request for Proposal - Fleet Management Solution | 3692689.0 |  |  | https://www.sasktenders.ca/Competitions/Print?id=3e273246-5f94-496a-a2f5-e15cda240411 |
| ca_saskatchewan:a82916c8-4a47-43c3-a04f-ff6bd8cc8fb0:1 | Northwest School Division No. 203 | Supply of Desktops Request for Proposal |  |  |  | https://www.sasktenders.ca/Competitions/Print?id=a82916c8-4a47-43c3-a04f-ff6bd8cc8fb0 |
| ca_saskatchewan:90353642-3879-4546-99cf-5c9863b07929:0 | City of Saskatoon | Standing Offer - Cisco Products | 2050000.0 |  |  | https://www.sasktenders.ca/Competitions/Print?id=90353642-3879-4546-99cf-5c9863b07929 |
| ca_saskatchewan:253ed11f-25c4-4169-b271-dd2021e61178:0 | Chinook School Division No. 211 | Chromebook Tender | 276156.9 |  |  | https://www.sasktenders.ca/Competitions/Print?id=253ed11f-25c4-4169-b271-dd2021e61178 |
| ca_saskatchewan:c1db04bd-076e-4cbf-a826-5d06be70eae9:0 | Central Services - IT Division | Project Management Services for the Criminal Justice Information Management Systems (CJIMS) developm |  |  |  | https://www.sasktenders.ca/Competitions/Print?id=c1db04bd-076e-4cbf-a826-5d06be70eae9 |
| ca_saskatchewan:6087a75d-5143-4df2-8c9f-1a1ae7d9f583:0 | City of Saskatoon | Cisco Network Device Maintenance | 268600.6 |  |  | https://www.sasktenders.ca/Competitions/Print?id=6087a75d-5143-4df2-8c9f-1a1ae7d9f583 |
| ca_saskatchewan:ca7e0a30-1060-456d-bf0a-26cd683f8873:0 | Finance | Consulting Services for Accounts Payable Consolidation Project |  |  |  | https://www.sasktenders.ca/Competitions/Print?id=ca7e0a30-1060-456d-bf0a-26cd683f8873 |
| ca_saskatchewan:f08e4dc8-aa1e-4146-89b9-a02053bcc5c1:0 | Information Technology Office | IT Consulting Services for the Support, Enhancement and Maintenance of Hyperion Essbase |  |  |  | https://www.sasktenders.ca/Competitions/Print?id=f08e4dc8-aa1e-4146-89b9-a02053bcc5c1 |
| ca_saskatchewan:1bea7b48-3720-4c19-872f-7a2aeb975b67:4 | Information Technology Office | RFP to establish a Supply Arrangement for Resources for the ITO Category 1 |  |  |  | https://www.sasktenders.ca/Competitions/Print?id=1bea7b48-3720-4c19-872f-7a2aeb975b67 |
| ca_saskatchewan:2f46d604-4b66-4c8e-93ce-07885c4407c0:12 | Information Technology Office | RFP to establish a Supply Arrangement for Resources for the ITO Category 2 |  |  |  | https://www.sasktenders.ca/Competitions/Print?id=2f46d604-4b66-4c8e-93ce-07885c4407c0 |
| ca_saskatchewan:400e2357-dc22-4e8f-9c32-7dc5ae37a01b:7 | Information Technology Office | RFP to establish a Supply Arrangement for Resources for the ITO Category 3 |  |  |  | https://www.sasktenders.ca/Competitions/Print?id=400e2357-dc22-4e8f-9c32-7dc5ae37a01b |
| canada_federal:cbsa-asfc:4741968970 | Canada Border Services Agency | Application Software (including COTS) and Application Development and Delivery Software | 582510.09 |  |  | https://search.open.canada.ca/contracts/record/cbsa-asfc,C-2015-2016-Q4-00159 |
| canada_federal:cbsa-asfc:4741968575 | Canada Border Services Agency | Application Software (including COTS) and Application Development and Delivery Software | 45791.67 |  |  | https://search.open.canada.ca/contracts/record/cbsa-asfc,C-2015-2016-Q4-00160 |
| canada_federal:cbsa-asfc:4741979053 | Canada Border Services Agency | Computer Equipment related to Distributed Computing Environment (DCE) | 50574.27 |  |  | https://search.open.canada.ca/contracts/record/cbsa-asfc,C-2015-2016-Q4-00161 |
| canada_federal:cbsa-asfc:2B15010093 | Canada Border Services Agency | Computer Equipment related to Distributed Computing Environment (DCE) | 1390881.97 |  |  | https://search.open.canada.ca/contracts/record/cbsa-asfc,C-2015-2016-Q4-00162 |
| canada_federal:csa-asc:7016470 | Canadian Space Agency | Information technology and telecommunications consultants | 93129.75 |  |  | https://search.open.canada.ca/contracts/record/csa-asc,C-2025-2026-Q4-00010 |
| canada_federal:csa-asc:7016786 | Canadian Space Agency | License/Maintenance fees for application software (including COTS) and application development and delivery software | 24352.85 |  |  | https://search.open.canada.ca/contracts/record/csa-asc,C-2026-2027-Q1-00025 |
| canada_federal:csc-scc:21155-23-4320788 | Correctional Service of Canada | Computer Services | 3006408.18 |  |  | https://search.open.canada.ca/contracts/record/csc-scc,C-2023-2024-Q2-00261 |
| canada_federal:esdc-edsc:4500014465 | Employment and Social Development Canada | Information technology and telecommunications consultants | 912335.97 |  |  | https://search.open.canada.ca/contracts/record/esdc-edsc,C-2026-2027-Q1-00053 |
| canada_federal:esdc-edsc:2BSCS13170 | Employment and Social Development Canada | Information technology and telecommunications consultants | 12264154.1 |  |  | https://search.open.canada.ca/contracts/record/esdc-edsc,C-2026-2027-Q1-00012 |
| canada_federal:esdc-edsc:4500014885 | Employment and Social Development Canada | Information technology and telecommunications consultants | 727172.47 |  |  | https://search.open.canada.ca/contracts/record/esdc-edsc,C-2026-2027-Q1-00057 |
| canada_federal:esdc-edsc:4500015167 | Employment and Social Development Canada | Information technology and telecommunications consultants | 756817.24 |  |  | https://search.open.canada.ca/contracts/record/esdc-edsc,C-2026-2027-Q1-00062 |
| canada_federal:esdc-edsc:4500015840 | Employment and Social Development Canada | Information technology and telecommunications consultants | 539471.86 |  |  | https://search.open.canada.ca/contracts/record/esdc-edsc,C-2026-2027-Q1-00069 |
| … 240 more rows in the .json | ||||||

## Open questions for hand research (layer 2)

- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
