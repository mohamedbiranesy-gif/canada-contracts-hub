# S3-27 — Financial Services Skills Commission Limited ⇄ IAXOV Inc.

Stratum: **S3_routed_public_body_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Financial Services Skills Commission Limited — Sixth Floor, Fitzwilliam House, St. Mary Axe, London, EC3A 8BF
SUBMIT TO: info@financialservicesskills.org (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: IAXOV Inc. — 330 5th Ave SW, Suite 1800, Calgary, AB, T2P 0L4, CA | GST/HST 724821954RT0001 (account derived from the BN9)
TAX: DERIVED: pays GST/HST on purchases (pay-and-rebate model): charge GST/HST on the invoice — GST/HST Memorandum 18-2 para. 23 (https://www.canada.ca/en/revenue-ag | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: IAXOV — The Sovereign Intelligence Company
```

## Relationship
- **rank_group**: D1
- **data_quality_score**: 41
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Financial Services Skills Commission Limited (government ministry / agency, jurisdiction not stated) — named as a client by the Canada-located vendor (client list / customer story), dated: IAXOV Inc. | subject: IAXOV — The Sovereign Intelligence Company | published by: the Canada-located vendor's own website | record: https://www.iaxov.com/case-studies | vendor in Canada because: vendor located in Canada (v)=iaxov.com | status rule: client listing on the vendor's own site (undated)
- **how_relationship_was_found**: tools/client_lists.py / dated_stories.py read the vendor's dated customer story / case study naming the buyer
- **keys**: lead:d1fb55b044432f63
- **tier**: D
- **grade**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: Financial Services Skills Commission Limited
- **buyer_website**: https://financialservicesskills.org/
- **buyer_address**: Sixth Floor, Fitzwilliam House, St. Mary Axe, London, EC3A 8BF
- **buyer_phone**: 020 3696 0150
- **buyer_contact_evidence_url**: https://financialservicesskills.org/contact-us/
- **buyer_legal_name_as_published**: Financial Services Skills Commission Limited
- **buyer_logo_url**: https://financialservicesskills.org/wp-content/uploads/2026/08/Pro-Global-news-carousel-768x464.jpg
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/financial-services-skills/
- **buyer_type**: government ministry / agency
- **buyer_sector**: government: provincial / federal
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://financialservicesskills.org/contact-us/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; AP contact name: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: pays GST/HST on purchases (pay-and-rebate model): charge GST/HST on the invoice — GST/HST Memorandum 18-2 para. 23 (https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The governments of all the participating provinces, as well as Quebec, British Columbia and Nunavut, have agreed to use the pay and rebate model. Therefore, their government departments and all of their Crown agents will pay the GST/HST on their purchases"); derived from buyer type and province, not published by the buyer
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: info@financialservicesskills.org
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://financialservicesskills.org/contact-us/
- **email_evidence_quote**: nquiry, get in touch by email or phone: Financial Services Skills Commission Fitzwilliam House 10 St Mary Axe London EC3A 8BF 020 3696 0150 info@financialservicesskills.org If you would like information on our work please fill in the form below: First Name* Last Name* Email address* Messag
- **email_evidence_context**: Skills-Based Organisation Framework AI Research Skills Compact Menu Join us Contact Us If you have a general enquiry, get in touch by email or phone: Financial Services Skills Commission Fitzwilliam House 10 St Mary Axe London EC3A 8BF 020 3696 0150 info@financialservicesskills.org If you would like information on our work please fill in the form below: First Name* Last Name* Email address* Message* I agree to the FSSC {{privacy policy}} About Us Contact Us What We Do News Research Terms and Conditions Privacy Policy Data Poli (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: info@financialservicesskills.org (general) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-01 | page: https://financialservicesskills.org/contact-us/ | quote: "nquiry, get in touch by email or phone: Financial Services Skills Commission Fitzwilliam House 10 St Mary Axe London EC3A 8BF 020 3696 0150 info@financialservic" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00027
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none;
- **dmarc_record_domain**: financialservicesskills.org
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 include:spf.protection.outlook.com include:123456.spf03.hubspotemail.net -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_contact_name_as_published**: Mary Axe London (Financial Services Skills Commis) (as printed by the organisation on its own accounts-payable page (as printed on https://financialservicesskills.org/contact-us/, re-read 2026-11-08))
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Financial Services Skills Commission Limited — Sixth Floor, Fitzwilliam House, St. Mary Axe, London, EC3A 8BF ⏎ SUBMIT TO: info@financialservicesskills.org (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: IAXOV Inc. — 330 5th Ave SW, Suite 1800, Calgary, AB, T2P 0L4, CA | GST/HST 724821954RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: pays GST/HST on purchases (pay-and-rebate model): charge GST/HST on the invoice — GST/HST Memorandum 18-2 para. 23 (https://www.canada.ca/en/revenue-ag | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: IAXOV — The Sovereign Intelligence Company
- **invoice_card_json**: {"bill_to": {"legal_name": "Financial Services Skills Commission Limited", "legal_name_is_published": true, "address": "Sixth Floor, Fitzwilliam House, St. Mary Axe, London, EC3A 8BF", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "info@financialservicesskills.org", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: pays GST/HST on purchases (pay-and-rebate model): charge GST/HST on the invoice — GST/HST Memorandum 18-2 para. 23 (https://www.canada.ca/en/revenue-agency/serv", "buyer_tax_status_is_published": false, "indicative_rate": "HST 13% (Ontario)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "724821954RT0001", "vendor_qst": ""}, "vendor_identity": {"legal_name": "IAXOV Inc.", "bn9": "724821954", "neq": "", "remit_address": "1800-330 5 Ave SW, Calgary, AB, T2P 0L4, CA"}, "follow_up": {"ap_phone": "020 3696 0150", "ap_contact": "Mary Axe London (Financial Services Skills Commis) (as printed by the organisat
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 53
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: IAXOV Inc.
- **vendor_legal_name**: IAXOV Inc.
- **vendor_registry_id**: Corporations Canada (corporation number): 16186629; corporation number 16186629 (Corporations Canada (open data))
- **vendor_registry_url**: https://ised-isde.canada.ca/cc/lgcy/fdrlCrpDtls.html?corpId=16186629
- **vendor_registered_address**: 1800-330 5 Ave SW, Calgary, AB, T2P 0L4, CA
- **vendor_legal_form**: Canada Business Corporations Act (Canada (federal))
- **vendor_directors_range**: 1 to 9 directors (Corporations Canada)
- **vendor_last_annual_filing**: ; Corporations Canada anniversary 2024-07-05
- **vendor_address**: 330 5th Ave SW, Suite 1800, Calgary, AB, T2P 0L4, CA
- **vendor_country_basis**: vendor located in Canada (v)=iaxov.com
- **vendor_bn9**: 724821954
- **vendor_gst_hst_derived**: 724821954RT0001
- **vendor_website**: https://www.iaxov.com/
- **vendor_contact_evidence_url**: https://www.iaxov.com/
- **vendor_logo_url**: https://www.iaxov.com/images/logo.svg
- **vendor_website_status**: site answers
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); registry identity: Corporations Canada (corporation number): 16186629; corporation number 16186629 (Corporations Canada (open data)) status Corporations Canada (corporation number): Active (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: registry match; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2024-07-05; phone / role e-mails / logo: the vendor's own site, https://www.iaxov.com/ (tools/org_contacts.py, org_extras.py); website: https://www.iaxov.com/ (site answers)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Corporations Canada (corporation number): Active
- **vendor_incorporation_date**: 2024-07-05
- **vendor_years_in_business**: 2.3 (since 2024-07-05, registry date)

## Contract
- **contract_status**: client listing on the vendor's own site (undated)
- **contract_title**: IAXOV — The Sovereign Intelligence Company
- **contract_description**: IAXOV — The Sovereign Intelligence Company (the record's title; the source publishes no separate description)
- **contract_link**: https://www.iaxov.com/case-studies
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: pays GST/HST on purchases (pay-and-rebate model): charge GST/HST on the invoice — GST/HST Memorandum 18-2 para. 23 (https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The governments of all the participating provinces, as well as Quebec, British Columbia and Nunavut, have agreed to use the pay and rebate model. Therefore, their government departments and all of their Crown agents will pay the GST/HST on their purchases"); derived from buyer type and province, not published by the buyer
- **tax_rate_indicative_derived**: HST 13% (Ontario) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 724821954RT0001

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Financial Services Skills Commission Limited — Sixth Floor, Fitzwilliam House, St. Mary Axe, London, EC3A 8BF ⏎ SUBMIT TO: info@financialservicesskills.org (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: IAXOV Inc. — 330 5th Ave SW, Suite 1800, Calgary, AB, T2P 0L4, CA | GST/HST 724821954RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: pays GST/HST on purchases (pay-and-rebate model): charge GST/HST on the invoice — GST/HST Memorandum 18-2 para. 23 (https://www.canada.ca/en/revenue-ag | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: IAXOV — The Sovereign Intelligence Company
- **invoice_card_json**: {"bill_to": {"legal_name": "Financial Services Skills Commission Limited", "legal_name_is_published": true, "address": "Sixth Floor, Fitzwilliam House, St. Mary Axe, London, EC3A 8BF", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "info@financialservicesskills.org", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: pays GST/HST on purchases (pay-and-rebate model): charge GST/HST on the invoice — GST/HST Memorandum 18-2 para. 23 (https://www.canada.ca/en/revenue-agency/serv", "buyer_tax_status_is_published": false, "indicative_rate": "HST 13% (Ontario)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "724821954RT0001", "vendor_qst": ""}, "vendor_identity": {"legal_name": "IAXOV Inc.", "bn9": "724821954", "neq": "", "remit_address": "1800-330 5 Ave SW, Calgary, AB, T2P 0L4, CA"}, "follow_up": {"ap_phone": "020 3696 0150", "ap_contact": "Mary Axe London (Financial Services Skills Commis) (as printed by the organisat
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 53
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["info@financialservicesskills.org (general)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-01", "page: https://financialservicesskills.org/contact-us/", "quote: \"nquiry, get in touch by email or phone: Financial Services Skills Commission Fitzwilliam House 10 St Mary Axe London EC3A 8BF 020 3696 0150 info@financialservic\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00027"], "buyer_facts": ["address and phone: the buyer's own site, https://financialservicesskills.org/contact-us/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "AP contact name: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "registry identity: Corporations Canada (corporation number): 16186629", "corporation number 16186629 (Corporations Canada (open data)) status Corporations Canada (corpor

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://financialservicesskills.org/contact-us/ | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, financialservicesskills.org)
- **status**: ok
- **pages**: 5
- **language**: en
- **legal_name**: Financial Services Skills Commission Limited
- **legal_name_url**: https://financialservicesskills.org/
- **legal_name_quote**: Data Policy Cookies Careers Sixth Floor, Fitzwilliam House, St. Mary Axe, London EC3A 8BF Copyright Financial Services Skills Commission Limited 2026
- **logo_url**: https://financialservicesskills.org/wp-content/uploads/2026/08/Pro-Global-news-carousel-768x464.jpg
- **logo_basis**: logo image on the site
- **domain**: financialservicesskills.org
- **key**: lead:d1fb55b044432f63
- **name**: Financial Services Skills Commission Limited
- **website**: https://financialservicesskills.org/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **linkedin_url**: https://www.linkedin.com/company/financial-services-skills/
- **tel_links**: 020 3696 0150

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "Sixth Floor, Fitzwilliam House, St. Mary Axe, London, EC3A 8BF", "address_country": "GB", "address_url": "https://financialservicesskills.org/contact-us/", "address_method": "address-tag", "address_quote": "o News Research Terms and Conditions Privacy Policy Data Policy Cookies Careers Sixth Floor, Fitzwilliam House, St. Mary Axe, London EC3A 8BF Copyright Financial Services", "phone": "020 3696 0150", "phone_url": "https://financialservicesskills.org/contact-us/", "emails": "info@financialservicesskills.org", "emails_url": "https://financialservicesskills.org/contact-us/", "domain": "financialservicesskills.org", "key": "lead:d1fb55b044432f63", "name": "financialservicesskills.org", "website": "https://financialservicesskills.org/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, iaxov.com)
- **status**: ok
- **pages**: 4
- **language**: en
- **legal_name**: IAXOV Inc
- **legal_name_url**: https://www.iaxov.com/
- **legal_name_quote**: Solutions STRATEVITA UNIFYZE Bespoke Company About Leadership Investors Careers Publications © 2026 IAXOV Inc. All rights reserved. Privacy Policy Terms of Service Security © 2026 NVIDIA, the NVIDIA logo, and
- **logo_url**: https://www.iaxov.com/images/logo.svg
- **logo_basis**: logo image in the site header
- **domain**: iaxov.com
- **key**: vendor:IAXOV Inc.
- **name**: IAXOV Inc.
- **website**: https://iaxov.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: IAXOV Inc
- **legal_name_stated_url**: https://www.iaxov.com/terms
- **legal_name_stated_quote**: Terms of Service — IAXOV Inc. Skip to main content Home Request Sovereignty Assessment Legal Terms of Service Last updated: Apri
- **mentions**: {'payment_method': {'text': 'interactive tools, APIs, and platform interfaces', 'url': 'https://www.iaxov.com/terms', 'quote': 'related enterprise applications. Our Services include websites, marketing materials, publications, interactive tools, APIs, and platform interfaces. The specific features and capabilities available to you depend on the context in which you access'}}

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 1, "address": "330 5th Avenue SW, Suite 1800, Calgary, Alberta T2P 0L4", "address_country": "CA", "address_url": "https://www.iaxov.com/", "address_method": "pattern", "address_quote": "ce Sovereignty of Every Context” 330 5th Avenue SW, Suite 1800 Calgary, Alberta T2P 0L4 Canada Platform Legion Overview Architecture Security Compare Industries Govern", "domain": "iaxov.com", "key": "vd:iaxov.com", "name": "IAXOV Inc.", "website": "https://iaxov.com/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Financial Services Skills Commission Limited | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Financial%20Services%20Skills%20Commission%20Limited | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Financial Services Skills Commission Limited |  |  |  |  |  |  |  |  |  |  |
| v | IAXOV Inc. |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:d1fb55b044432f63",
 "ap_contact_team": {
  "emails": [
   "info@financialservicesskills.org"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "info@financialservicesskills.org",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://financialservicesskills.org/contact-us/",
    "quote": "nquiry, get in touch by email or phone: Financial Services Skills Commission Fitzwilliam House 10 St Mary Axe London EC3A 8BF 020 3696 0150 info@financialservicesskills.org If you would like information on our work please fill in the form below: First Name* Last Name* Email address* Messag",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "financialservicesskills.org",
    "task_id": "CL-LD-14008"
   },
   {
    "email": "info@financialservicesskills.org",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://financialservicesskills.org/contact-us/",
    "quote": "nquiry, get in touch by email or phone: Financial Services Skills Commission Fitzwilliam House 10 St Mary Axe London EC3A 8BF 020 3696 0150 info@financialservicesskills.org If you would like information on our work please fill in the form below: First Name* Last Name* Email address* Messag",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Financial Services Skills Commission",
    "task_id": "CL-WS-00027"
   }
  ]
 },
 "research_status": {
  "found": 2
 },
 "queries_tried": [
  "site crawl of financialservicesskills.org (19 pages, robots.txt respected), no AI, no search engine",
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

## The vendor's other buyers in the dataset (first 60 of 1)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_alberta_apc:AB-2026-00962:16c242ff-38ca-4e84-9f4f-fa9ae999fcc5 | Alberta Innovates | Alberta Innovates - Request for Proposal - Pre-Qualification of Vendors for Artificial Intelligence, Machine Learning, and Automation Services |  |  |  | https://purchasing.alberta.ca/posting/AB-2026-00962 |

## Open questions for hand research (layer 2)

- an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed)
- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
