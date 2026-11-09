# S3-33 — Actsafe Safety Association ⇄ MNP LLP

Stratum: **S3_routed_public_body_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Actsafe Safety Association — 140 - 4259 Canada Way, Burnaby, BC V5G 1H1
SUBMIT TO: info@actsafe.ca (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: MNP LLP — 200, 5019 - 49 Ave, Leduc, AB, T9E 6T5 (carried from this vendor's row with Thorhild County) | GST/HST 103697215RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Actsafe Safety Association (non-profit / association / cultural body, jurisdiction not stated) — public contract / purchase award in the las
```

## Relationship
- **rank_group**: B1
- **data_quality_score**: 53
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 1
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Actsafe Safety Association (non-profit / association / cultural body, jurisdiction not stated) — public contract / purchase award in the last 12 months (dated record): MNP LLP | awarded 2026-06-17 | published by: auditor of record (own audited financial statements, auditor's report signed in Port Moody | record: https://actsafe.ca/wp-content/uploads/2026/07/2025-Annual-ReportV6-FINAL.pdf | vendor in Canada because: auditor of record (own audited financial statements, auditor's report signed in Port Moody, British Columbia)=are responsible for overseeing the Association’s financial reporting process. | MNP LLP 601 - 205 Newport Dr,  | status rule: likely active (record dated in the last 12 months: auditor of record (own audited financial statements, auditor's report signed in Port Moody)
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: lead:b0187831c0411fe4
- **tier**: B
- **grade**: 1
- **records_with_this_vendor**: 1 (relationship record: auditor of record (own audited financial statements, auditor's report signed in Port Moody; 0 in the contract dataset)

## Buyer
- **buyer**: Actsafe Safety Association
- **buyer_website**: https://actsafe.ca/
- **buyer_address**: 140 - 4259 Canada Way, Burnaby, BC V5G 1H1
- **buyer_phone**: 604-733-4682
- **buyer_contact_evidence_url**: https://actsafe.ca/contact-us/
- **buyer_legal_name_as_published**: Actsafe Safety Association
- **buyer_logo_url**: https://actsafe.ca/wp-content/uploads/2022/03/png-Logo_Actsafe.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/885054
- **buyer_type**: non-profit / association / cultural body
- **buyer_sector**: non-profit
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q129294549; organization
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://actsafe.ca/contact-us/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: info@actsafe.ca
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://actsafe.ca/wp-content/uploads/2025/10/WHMISFS8.pdf
- **email_evidence_quote**: claim, liability or damages of any kind resulting from the use or reliance on the product for any purpose. Website: www.actsafe.ca | Email: info@actsafe.ca 3/3
- **email_evidence_context**: ation is within our policy, you can sign in to your STAR account and click on the Calendar tab. In the upper right corner, select “Courses” to view your registered training. To cancel, select “Withdraw.” If you wish to reschedule, please email us at info@actsafe.ca or call 604-733-4682 How do I access or download my certificate from my STAR profile? To access and download your certificates, log in to your STAR profile . Navigate to the Home tab, scroll down to the Completed section, and click on the certificat (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: info@actsafe.ca (general) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08 | page: https://actsafe.ca/wp-content/uploads/2025/10/WHMISFS8.pdf | quote: "claim, liability or damages of any kind resulting from the use or reliance on the product for any purpose. Website: www.actsafe.ca | Email: info@actsafe.ca 3/3" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00457
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none; ruf=mailto:info@northshore.digital
- **dmarc_record_domain**: actsafe.ca
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 ip4:108.172.94.189 include:spf.protection.outlook.com include:_spf.elasticemail.com -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Actsafe Safety Association — 140 - 4259 Canada Way, Burnaby, BC V5G 1H1 ⏎ SUBMIT TO: info@actsafe.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: MNP LLP — 200, 5019 - 49 Ave, Leduc, AB, T9E 6T5 (carried from this vendor's row with Thorhild County) | GST/HST 103697215RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Actsafe Safety Association (non-profit / association / cultural body, jurisdiction not stated) — public contract / purchase award in the las
- **invoice_card_json**: {"bill_to": {"legal_name": "Actsafe Safety Association", "legal_name_is_published": true, "address": "140 - 4259 Canada Way, Burnaby, BC V5G 1H1", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "info@actsafe.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (BC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "", "vendor_qst": ""}, "vendor_identity": {"legal_name": "MNP LLP", "bn9": "103697215", "neq": "", "remit_address": "200, 5019 - 49 Ave, Leduc, AB, T9E 6T5 (carried from this vendor's row with Thorhild County)"}, "follow_up": {"ap_phone": "604-733-4682", "ap_contact": "", "requirements_text": ""}}
- **invoice_readiness**: 6/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number; vendor legal name
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: MNP LLP
- **vendor_registered_address**: 200, 5019 - 49 Ave, Leduc, AB, T9E 6T5 (carried from this vendor's row with Thorhild County)
- **vendor_country_basis**: auditor of record (own audited financial statements, auditor's report signed in Port Moody, British Columbia)=are responsible for overseeing the Association’s financial reporting process. | MNP LLP 601 - 205 Newport Dr, Port Moody BC, V3 ... year. | Port Moody, British Columbia | June 17, 2026
- **vendor_bn9**: 103697215
- **vendor_facts_provenance**: name and address: the record's vendor block (auditor of record (own audited financial statements, auditor's report signed in Port Moody); BN9: corporations_canada 1695592 (exact match) — carried from this vendor's row with Thorhild County; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_bn_source**: corporations_canada 1695592 (exact match) — carried from this vendor's row with Thorhild County

## Contract
- **contract_status**: likely active (record dated in the last 12 months: auditor of record (own audited financial statements, auditor's report signed in Port Moody)
- **award_date**: 2026-06-17
- **contract_link**: https://actsafe.ca/wp-content/uploads/2026/07/2025-Annual-ReportV6-FINAL.pdf
- **source**: auditor of record (own audited financial statements, auditor's report signed in Port Moody
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: auditor of record (own audited financial statements, auditor's report signed in Port Moody; 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (BC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Actsafe Safety Association — 140 - 4259 Canada Way, Burnaby, BC V5G 1H1 ⏎ SUBMIT TO: info@actsafe.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: MNP LLP — 200, 5019 - 49 Ave, Leduc, AB, T9E 6T5 (carried from this vendor's row with Thorhild County) | GST/HST 103697215RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Actsafe Safety Association (non-profit / association / cultural body, jurisdiction not stated) — public contract / purchase award in the las
- **invoice_card_json**: {"bill_to": {"legal_name": "Actsafe Safety Association", "legal_name_is_published": true, "address": "140 - 4259 Canada Way, Burnaby, BC V5G 1H1", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "info@actsafe.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (BC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "", "vendor_qst": ""}, "vendor_identity": {"legal_name": "MNP LLP", "bn9": "103697215", "neq": "", "remit_address": "200, 5019 - 49 Ave, Leduc, AB, T9E 6T5 (carried from this vendor's row with Thorhild County)"}, "follow_up": {"ap_phone": "604-733-4682", "ap_contact": "", "requirements_text": ""}}
- **invoice_readiness**: 6/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number; vendor legal name
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["info@actsafe.ca (general)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08", "page: https://actsafe.ca/wp-content/uploads/2025/10/WHMISFS8.pdf", "quote: \"claim, liability or damages of any kind resulting from the use or reliance on the product for any purpose. Website: www.actsafe.ca", "Email: info@actsafe.ca 3/3\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00457"], "buyer_facts": ["address and phone: the buyer's own site, https://actsafe.ca/contact-us/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (auditor of record (own audited financial statements, auditor's report signed in Port Moody)", "BN9: corporations_canada 1695592 (exact match) — carried from this vendor's row with Thorhild County", "GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected", "not automated)"], "relationship": "same as above: a dated award record from the public sour

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://actsafe.ca/ | 2026-11-08 | ok |  |  |  | 604-733-4682 |  |  |  |  |  |

## Buyer site facts (org_extras, actsafe.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: Actsafe Safety Association
- **legal_name_url**: https://actsafe.ca/
- **legal_name_quote**: Actsafe Safety Association | Arts & Entertainment Industry in BC Skip to content Subscribe Menu Actsafe partners with B.C.’s a
- **logo_url**: https://actsafe.ca/wp-content/uploads/2022/03/png-Logo_Actsafe.png
- **logo_basis**: logo image in the site header
- **domain**: actsafe.ca
- **key**: lead:b0187831c0411fe4
- **name**: Actsafe Safety Association
- **website**: https://actsafe.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: NGO
- **jsonld_name**: Actsafe Safety Association
- **jsonld_legal_name**: Actsafe Safety Association
- **jsonld_url**: https://actsafe.ca
- **jsonld_same_as**: https://www.facebook.com/actsafe; https://twitter.com/actsafe; https://www.instagram.com/actsafe/; https://www.linkedin.com/company/885054; https://www.youtube.com/user/ActsafeBC
- **jsonld_quote**: [{"@context":"https:\/\/schema.org","@type":"WebPage","mainEntityOfPage":{"@type":"WebPage","@id":"https:\/\/actsafe.ca\/"},"headline":"Home","datePublished":"2024-11-15T04:37:06+05:30","dateModified":"2026-11-06T03:04:52+05:30","description":""}]
- **jsonld_page**: https://actsafe.ca/
- **legal_name_stated**: Canadian Media Producers Association
- **legal_name_stated_url**: https://actsafe.ca/about-us/governance/
- **legal_name_stated_quote**: ple Studios Association of Canadian Film Craftspeople (ACFC) West BC Council of Film Unions (BCCFU) Canadian Media Producers Association (CMPA) – BC Producer’s Branch Contract Services Administration Trust Fund (CSATF) Directors Guild o
- **linkedin_url**: https://www.linkedin.com/company/885054
- **tel_links**: 604-733-4682

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "140 - 4259 Canada Way, Burnaby, BC V5G 1H1", "address_country": "CA", "address_url": "https://actsafe.ca/contact-us/", "address_method": "pattern", "address_quote": "With Us Monday to Friday: 9:00 AM – 5:00 PM 140 - 4259 Canada Way, Burnaby, BC V5G 1H1 Message us here now Email us at info@actsafe.ca Call us at 604-733-4682. The Ac", "phone": "604-733-4682", "phone_url": "https://actsafe.ca/contact-us/", "emails": "communications@actsafe.ca; info@actsafe.ca", "emails_url": "https://actsafe.ca/contact-us/", "domain": "actsafe.ca", "key": "wd:Q129294549", "name": "Actsafe Safety Association", "website": "https://actsafe.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, domain unknown)
_not read_

## Vendor role mailboxes found on its site (org_contacts)
_not read_

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Actsafe Safety Association | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Actsafe%20Safety%20Association | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Actsafe Safety Association | Q129294549 | official website on the organisation's domain (https://actsafe.ca) + name |  | Actsafe Safety Association | Actsafe Safety Association | organization |  | Canada |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:b0187831c0411fe4",
 "ap_contact_team": {
  "emails": [
   "info@actsafe.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "info@actsafe.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://actsafe.ca/",
    "quote": "ight corner, select “Courses” to view your registered training. To cancel, select “Withdraw.” If you wish to reschedule, please email us at info@actsafe.ca or call 604-733-4682 How do I access or download my certificate from my STAR profile? To access and download your certificates, log in",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Actsafe Safety Association",
    "task_id": "CL-LD-45697"
   },
   {
    "email": "info@actsafe.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://actsafe.ca/wp-content/uploads/2025/10/WHMISFS8.pdf",
    "quote": "claim, liability or damages of any kind resulting from the use or reliance on the product for any purpose. Website: www.actsafe.ca | Email: info@actsafe.ca 3/3",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Actsafe Safety Association",
    "task_id": "CL-WS-00457"
   }
  ]
 },
 "research_status": {
  "found": 2
 },
 "queries_tried": [
  "site crawl of actsafe.ca (14 pages, robots.txt respected), no AI, no search engine",
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

## The vendor's other buyers in the dataset (first 60 of 286)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_alberta_apc:AB-2016-07214:1d136c14-ea28-495b-b2d2-eef5593a7bd0 | Jobs, Economy, Trade and Immigration | Jobs, Economy, Trade and Immigration - Request for Proposal - Self Employment Tranining Provincial RFP | 451463.0 |  |  | https://purchasing.alberta.ca/posting/AB-2016-07214 |
| ca_alberta_apc:AB-2016-07214:7fde9715-27a3-4654-b738-5781a4b82548 | Jobs, Economy, Trade and Immigration | Jobs, Economy, Trade and Immigration - Request for Proposal - Self Employment Tranining Provincial RFP | 797759.0 |  |  | https://purchasing.alberta.ca/posting/AB-2016-07214 |
| ca_alberta_apc:AB-2019-00123:28c75f05-ea22-4743-80a3-f1ab5d4ee962 | Jobs, Economy, Trade and Immigration | Jobs, Economy, Trade and Immigration - Request for Proposal - Self Employment | 1120000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2019-00123 |
| ca_alberta_apc:AB-2020-04108:f2ac6032-5f57-5a5f-0b8c-39c2ed490000 | Alberta Gaming, Liquor and Cannabis Commission | Alberta Gaming, Liquor and Cannabis Commission - Negotiated Request for Proposal - ERP Consultant | 225000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2020-04108 |
| ca_alberta_apc:AB-2024-07618:ab5a9523-df9b-4804-bddd-63a2aebd98fb | Thorhild County | Thorhild County - Request for Proposal - Request for Proposals: Auditing Services | 40000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2024-07618 |
| ca_alberta_apc:AB-2024-07622:cc542c10-44dc-4a4e-bc0e-e23dc8a86ac9 | City of Grande Prairie | City of Grande Prairie - Negotiated Request for Proposal - Financial Audit Services |  |  |  | https://purchasing.alberta.ca/posting/AB-2024-07622 |
| ca_alberta_apc:AB-2024-07821:29a83e05-f833-4a0e-82d5-cd536f072e14 | Brazeau County | Brazeau County - Economic Impact Assessment | 49720.0 |  |  | https://purchasing.alberta.ca/posting/AB-2024-07821 |
| ca_alberta_apc:AB-2025-00723:e84633e8-1c31-438d-a2e9-7eb8e0574f05 | Transportation and Economic Corridors | Transportation and Economic Corridors - Request for Proposal - CON0025120 - CLASS 1 LEARNING GRANT PROGRAM ADMINISTRATOR | 2000000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-00723 |
| ca_alberta_apc:AB-2025-02163:c6fcd43f-5e1f-468b-a28f-3bef7946d38b | Forestry and Parks | Forestry and Parks - Request for Proposal - Timber Dues System Surveys and Analysis | 600000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-02163 |
| ca_alberta_apc:AB-2025-02697:afabdfae-b18e-4bfa-91c1-920e9c55b520 | TransAlta Tri Leisure Centre | TransAlta Tri Leisure Centre - Negotiated Request for Proposal - External Audit Services | 94625.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-02697 |
| ca_alberta_apc:AB-2025-02939:85b84aaf-bbc1-4e42-8684-ae1df587a5a0 | Red Deer Catholic Separate School Division | Red Deer Catholic Separate School Division - Request for Proposal - External Audit Services |  |  |  | https://purchasing.alberta.ca/posting/AB-2025-02939 |
| ca_alberta_apc:AB-2025-03282:1f29db9b-b194-4f47-8b60-cde1cf6e9973 | Beaver County | Beaver County - Request for Proposal - Beaver County 2025-2029 Audit and Financials Compilation Engagement | 234500.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-03282 |
| ca_alberta_apc:AB-2025-03681:3c389919-4686-4281-bfec-3445e6827dce | Auditor General | Auditor General - Request for Proposal - Alberta University of the Arts Financial Statements Audits | 198408.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-03681 |
| ca_alberta_apc:AB-2025-03687:39b35f1c-8b9d-4d0d-959e-c58b049b39a4 | Auditor General | Auditor General - Request for Proposal - Mount Royal University Financial Statements Audit | 483210.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-03687 |
| ca_alberta_apc:AB-2025-04559:eef98eb3-daf3-437b-aa88-9875935add5e | Calgary Housing Company | Calgary Housing Company - Request for Proposal -  Recruitment Services for Calgary Housing (CH) | 1.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-04559 |
| ca_alberta_apc:AB-2025-05210:83802425-2faa-4c1f-919a-2e2785dd796b | City of Lethbridge | City of Lethbridge - Request for Quotes - Talent Acquisition Services |  |  |  | https://purchasing.alberta.ca/posting/AB-2025-05210 |
| ca_alberta_apc:AB-2025-06825:b3a1c57e-f945-4b66-9c48-ef41a0f89df4 | City of Leduc | City of Leduc - Request for Proposal - Request for Proposals to Provide External Audit Services for the Capital Region Southwest Water Services Commission | 91800.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-06825 |
| ca_alberta_apc:AB-2025-07558:ea12746e-86d0-4c50-bc09-e254772c725a | Forestry and Parks | Forestry and Parks - Request for Proposal - Forest Products Trade - Expert Services | 2000000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-07558 |
| ca_alberta_apc:AB-2026-00555:3ba16a9f-d398-4358-aceb-452981cbcbaa | City of Medicine Hat | City of Medicine Hat - Negotiated Request for Proposal - CMH26-20 - Whistleblower Hotline Services  | 500000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2026-00555 |
| ca_alberta_apc:AB-2026-00678:f93af533-081d-4f71-8827-d8d7a55dafb6 | Parkland County | Parkland County - Negotiated Request for Proposal - Organizational Service Level Review | 285000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2026-00678 |
| ca_alberta_apc:AB-2026-05301:f26537bc-1f0c-4518-ba5b-7878a2e45d13 | City of St. Albert | City of St. Albert - Request for Proposal - Policing Services Consultant | 278000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2026-05301 |
| ca_bc_ministry_awards:815e2c9b3ddc44a7 | Ministry of Justice | ACTIVITY-BASED COSTING ANALYSIS | 69000.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:8c918bd88756d83c | Ministry of Agriculture | Food Preparations for Manufacturing Report | 40000.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:b96aa99dba0617e8 | Ministry of Tourism, Arts and Culture | Request for Proposals for Creative Futures Process Evaluation | 25000.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:274a79ea89f06a2c | Ministry of Agriculture | Local Food Procurement in Post-Secondary Institutions Consultati | 75000.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:381e64386497a41f | Ministry of Agriculture | BC Food Hub Network Industry Survey | 76500.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:9a61bc59eba20a2c | Ministry of Education | Request for Qualifications for K-12 Education Sector Consultants |  |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:57254584cf7f3452 | Ministry of Environment and Climate Change Strategy | Review of Recreation Service Delivery Models | 144900.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:2ee1daef11f1ef93 | Ministry of Transportation and Infrastructure | CVSE: Strategic Plan Development and Implementation Support | 175000.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/3ebd6010-3c30-4fa8-b95d-ed2362ce863f/download/ministry-contract-awards-2019.csv |
| ca_bc_ministry_awards:ea2b4f2ce2240106 | Ministry of Forests, Lands, Natural Resource Operations and R.D. | Trails Strategy for BC Review and Update | 64250.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/3ebd6010-3c30-4fa8-b95d-ed2362ce863f/download/ministry-contract-awards-2019.csv |
| ca_bc_ministry_awards:35b6b8457e0c1876 | Ministry of Citizens' Services | Check Point Software & Hardware Maintenance Renewal | 1834416.43 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/b113f1d3-3a78-4e10-a978-9a73a8c44be1/download/ministry-contract-awards-apr-jun-2022.csv |
| ca_bc_ministry_awards:4e16aae66461faea | Ministry of Jobs, Economic Recovery and Innovation | Economic Recovery Grants Program Evaluation | 109000.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/b113f1d3-3a78-4e10-a978-9a73a8c44be1/download/ministry-contract-awards-apr-jun-2022.csv |
| ca_bc_ministry_awards:82e91e533b6aa69d | Ministry of Transportation and Infrastructure | OnRouteBC Financial Risk & Controls Review | 44500.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/e948421d-a061-4aeb-be00-46f84bec8b32/download/ministry-contract-awards-apr-jun-2023.csv |
| ca_bc_ministry_awards:5819de1bc75b902b | Ministry of Municipal Affairs and Housing | Performance Audit Services: Capital Project Management | 100000.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/ee6045f4-dcaf-4a2b-80ef-8eeb876c64a1/download/ministry-contract-awards-apr-to-jun-2020.csv |
| ca_bc_ministry_awards:da415d9d6fc299d5 | Ministry of Agriculture, Food and Fisheries | Audit Work | 90000.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/500eda3c-e5a9-405d-a7c2-7443ce237387/download/ministry-contract-awards-apr-to-june-2021.csv |
| ca_bc_ministry_awards:45cb600ec15a0901 | Ministry of Citizens' Services | Req 45459  Check Point 6400 x2 and related licenses | 121221.78 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/fd7fdcab-dd3e-44a5-82d1-0bb72c78f4c0/download/ministry-contract-awards-jan-mar-2024.csv |
| ca_bc_ministry_awards:bfeffc30a46045b3 | Ministry of Citizens' Services | Req 46559 Check Point Smart-1 6000-L Base Gen-6 Security Management appliance & support (12 month term) | 57520.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/fbeba6e0-4d60-4cf1-a62f-c4849f617194/download/ministry-contract-awards-jan-mar-2025.xlsx |
| ca_bc_ministry_awards:ac65800139c5432e | Procurement Services Branch | MCFD Professional and Consulting Services RSA | 1.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/fbeba6e0-4d60-4cf1-a62f-c4849f617194/download/ministry-contract-awards-jan-mar-2025.xlsx |
| ca_bc_ministry_awards:2877ce9705eded62 | Ministry of Energy, Mines, and Petroleum Resources | Request for Proposals - ARC Program Phase II | 5000000.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/2ff7c805-5187-4ab4-a8ec-c0f85dca97fb/download/ministry-contract-awards-jan-to-apr-2020.csv |
| ca_bc_ministry_awards:8479a7a9964549c1 | Ministry of Energy, Mines, and Petroleum Resources | Request for Proposals Go Electric Commercial Vehicle Program | 6000000.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/2ff7c805-5187-4ab4-a8ec-c0f85dca97fb/download/ministry-contract-awards-jan-to-apr-2020.csv |
| ca_bc_ministry_awards:a6a30487832c46cf | Ministry of Environment and Climate Change Strategy | CleanBC Industry Fund Studies Call Administration | 879798.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/b84ec72e-30ad-4f85-be66-a26dac65a137/download/ministry-contract-awards-jan-to-mar-2021.csv |
| ca_bc_ministry_awards:3043459f281d7fc6 | Ministry of Citizens' Services | NOI SRFP_RPD_FRCR_2021 | 95000.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/0aaa523e-12d2-4c71-867d-156bcb8fb59f/download/ministry-contract-awards-jan-to-mar-2022.csv |
| ca_bc_ministry_awards:b6410139ceb1226a | Ministry of Agriculture and Food | New Entrant Access to Capital Analysis | 47790.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/5bda7834-e5fe-4ac2-b26f-7e994ac120f6/download/ministry-contract-awards-oct-dec-2022.csv |
| ca_bc_ministry_awards:2ad12c8f14fafaab | Ministry of Agriculture and Food | CanadaGAP Strategic Project | 50000.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/5bda7834-e5fe-4ac2-b26f-7e994ac120f6/download/ministry-contract-awards-oct-dec-2022.csv |
| ca_bc_ministry_awards:f1b9e762f0e600c8 | Ministry of Citizens' Services | RFP 201496-Request for Proposal COMPLIANCE AUDIT OF STRATEGIC TRANSFORMATION AND MAINFRAME SERVICES (“STMS”) AGREEMENT BETWEEN THE PROVINCE AND ESIT ADVANCED SO | 395000.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/d8dd9bc0-fd7a-434c-b6ae-fd87700dbb05/download/ministry-contract-awards-oct-dec-2024.xlsx |
| ca_bc_ministry_awards:3dfd58b11cd8f25f | Low Carbon Fuels Branch | Initiative Agreement Program Design | 179200.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/d8dd9bc0-fd7a-434c-b6ae-fd87700dbb05/download/ministry-contract-awards-oct-dec-2024.xlsx |
| ca_bc_ministry_awards:05c2c0edfaabae22 | Ministry of Citizens' Services | Lean Services- Request for Standing Arrangement |  |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/7fed5fea-1b3d-4714-ab76-20b69a62a674/download/ministry-contract-awards-oct-to-dec-2021.csv |
| ca_bc_ministry_awards:9e1d2fc4e10b692a | Ministry of Attorney General | Performance Audit of Technical Safety BC | 169000.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/7fed5fea-1b3d-4714-ab76-20b69a62a674/download/ministry-contract-awards-oct-to-dec-2021.csv |
| ca_biddingo:36159128:41077488 | Atlantic Lottery Corporation | Change Management Services / Services  de gestion du changement | 178.0 |  |  | https://api.biddingo.com/restapi/bidding/noauthorize/1/11003564/36159128 |
| ca_biddingo:34396228:41077488 | Workplace Safety and Insurance Board (WSIB) | QualysGuard Annual Renewal |  |  |  | https://api.biddingo.com/restapi/bidding/noauthorize/1/11003099/34396228 |
| ca_biddingo:32325028:41174288 | City of Welland | External Audit Services |  |  |  | https://api.biddingo.com/restapi/bidding/noauthorize/1/11003043/32325028 |
| ca_bidsandtenders:3e23d5e0-31f7-40d5-bbbb-58440c5d8bb5:1 | City of St. Albert | Policing Services Consultant | 278000.0 |  |  | https://stalbert.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/3e23d5e0-31f7-40d5-bbbb-58440c5d8bb5 |
| ca_bidsandtenders:6c19144b-2bf6-44f5-b4f3-ffdd54bde7b2:1 | City of Thunder Bay | External Audit Services |  |  |  | https://thunderbay.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/6c19144b-2bf6-44f5-b4f3-ffdd54bde7b2 |
| ca_bidsandtenders:1fc2f1c1-0ba4-489b-927f-d054399f366f:1 | United Counties of Prescott and Russell | External Audit Services | 292500.0 |  |  | https://prescott-russell.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/1fc2f1c1-0ba4-489b-927f-d054399f366f |
| ca_bidsandtenders:a3b3c3e7-d5cc-41f8-8c83-157fb2216011:1 | City of Yellowknife | Business Continuity Plan 2026 |  |  |  | https://yellowknife.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/a3b3c3e7-d5cc-41f8-8c83-157fb2216011 |
| ca_bidsandtenders:96081593-0f3d-426d-9181-4d481a0ee986:1 | City of London | Internal Audit Services |  |  |  | https://london.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/96081593-0f3d-426d-9181-4d481a0ee986 |
| ca_bidsandtenders:1b4c88d9-211b-49ae-a7d2-68897920e4ca:1 | City of Medicine Hat | Whistleblower Hotline Services | 100000.0 |  |  | https://medicinehat.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/1b4c88d9-211b-49ae-a7d2-68897920e4ca |
| ca_bidsandtenders:cdcb7d8c-efb4-47e5-a3b0-695dc405218d:11 | City of Maple Ridge | Project Management Services |  |  |  | https://mapleridge.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/cdcb7d8c-efb4-47e5-a3b0-695dc405218d |
| ca_bidsandtenders:b6c46967-7b52-4781-86e5-29062eb30491:1 | City of Leduc | Request for Proposals to Provide External Audit Services for the Capital Region Southwest Water Services Commission |  |  |  | https://leduc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/b6c46967-7b52-4781-86e5-29062eb30491 |
| ca_bidsandtenders:d71f6c63-6d64-45c1-aa10-ffec49c8aa66:1 | City of Saskatoon | Whistleblower Hotline Services | 65490.0 |  |  | https://saskatoon.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/d71f6c63-6d64-45c1-aa10-ffec49c8aa66 |
| … 226 more rows in the .json | ||||||

## Open questions for hand research (layer 2)

- an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed)
- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
