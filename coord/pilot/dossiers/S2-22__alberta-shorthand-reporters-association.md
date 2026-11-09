# S2-22 — Alberta Shorthand Reporters Association ⇄ Dicta Court Reporting Inc.

Stratum: **S2_complete_no_published_PO_rule** · pay on sight: yes — reference rule not published (quote the buyer's PO / order number when one is issued) · channel tier 2 · AP grade C · missing: (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Alberta Shorthand Reporters Association — 17008 – 90 Avenue NW, Edmonton, Alberta, T5T 1L6
SUBMIT TO: treasurer@asraonline.com (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: DICTA COURT REPORTING INC. (as registered: Canada's Business Registries, AB 2012832453, 2026-11-08) — Calgary, AB, Canada (inferred from province/territory code) | GST/HST 830171765 (Canada's Business Registries, AB 2012832453, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Alberta Shorthand Reporters Association (non-profit / association / cultural body, jurisdiction not stated) — named as a client by the Canad
```

## Relationship
- **rank_group**: D3
- **data_quality_score**: 58
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Alberta Shorthand Reporters Association (non-profit / association / cultural body, jurisdiction not stated) — named as a client by the Canada-located vendor (client list / customer story), dated: Dicta Court Reporting Inc. | published by: the Canada-located vendor's own website | record: https://www.dictacourtreporting.com/ | vendor in Canada because: vendor located in Canada (wall)=dictacourtreporting.com | status rule: client listing on the vendor's own site (undated)
- **how_relationship_was_found**: tools/client_lists.py / dated_stories.py read the vendor's dated customer story / case study naming the buyer
- **keys**: lead:6d0148c61e750f73
- **tier**: D
- **grade**: 3
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: Alberta Shorthand Reporters Association
- **buyer_website**: https://asraonline.com/
- **buyer_address**: 17008 – 90 Avenue NW, Edmonton, Alberta, T5T 1L6
- **buyer_contact_evidence_url**: https://asraonline.com/who-we-are/council-members/
- **buyer_legal_name_as_published**: Alberta Shorthand Reporters Association
- **buyer_logo_url**: https://asraonline.com/wp-content/themes/asra-2015/images/asra-logo.svg
- **buyer_website_status**: site answers
- **buyer_type**: non-profit / association / cultural body
- **buyer_sector**: non-profit
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://asraonline.com/who-we-are/council-members/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: treasurer@asraonline.com
- **email_type**: finance/accounting dept or supplier-payment office
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); finance mailbox
- **email_evidence_url**: https://asraonline.com/who-we-are/council-members/
- **email_evidence_quote**: asurer Calgary, Alberta treasurer@asraonline.com Jessica Norris Secretary Calgary, Alberta jessinorris14@gmail.com Sandie Murphy Practice Review Committee Calgary, Alberta ce
- **email_evidence_context**: President Edmonton Alberta hannah.leddy124@gmail.com Kaylene Davidsen 2nd Vice President Calgary, Alberta concerns@asraonline.com Cindy James Registration Committee Edmonton, Alberta registrar@asraonline.com Deanna DiPaolo Treasurer Calgary, Alberta treasurer@asraonline.com Jessica Norris Secretary Calgary, Alberta jessinorris14@gmail.com Sandie Murphy Practice Review Committee Calgary, Alberta cecredits@asraonline.com Sheralee Morrison Special Projects Calgary, Alberta sheralee@dictacourtreporting.com Student Members (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: treasurer@asraonline.com (finance/accounting dept or supplier-payment office) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://asraonline.com/who-we-are/council-members/ | quote: "asurer Calgary, Alberta treasurer@asraonline.com Jessica Norris Secretary Calgary, Alberta jessinorris14@gmail.com Sandie Murphy Practice Review Committee Calga" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); no SPF record; mail handled by Google Workspace | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-14441
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); no SPF record; mail handled by Google Workspace
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none; pct=100; rua=mailto:re+iaaivbekwjv@dmarc.postmarkapp.com; sp=none; aspf=r;
- **dmarc_record_domain**: asraonline.com
- **spf_policy**: no SPF record
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 2
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Alberta Shorthand Reporters Association — 17008 – 90 Avenue NW, Edmonton, Alberta, T5T 1L6 ⏎ SUBMIT TO: treasurer@asraonline.com (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: DICTA COURT REPORTING INC. (as registered: Canada's Business Registries, AB 2012832453, 2026-11-08) — Calgary, AB, Canada (inferred from province/territory code) | GST/HST 830171765 (Canada's Business Registries, AB 2012832453, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Alberta Shorthand Reporters Association (non-profit / association / cultural body, jurisdiction not stated) — named as a client by the Canad
- **invoice_card_json**: {"bill_to": {"legal_name": "Alberta Shorthand Reporters Association", "legal_name_is_published": true, "address": "17008 – 90 Avenue NW, Edmonton, Alberta, T5T 1L6", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "treasurer@asraonline.com", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (AB)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "830171765RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "DICTA COURT REPORTING INC. (as registered: Canada's Business Registries, AB 2012832453, 2026-11-08)", "bn9": "830171765 (Canada's Business Registries, AB 2012832453, 2026-11-08
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; AP phone or contact for follow-up
- **ap_grade**: C
- **ap_score**: 61
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: Dicta Court Reporting Inc.
- **vendor_legal_name**: DICTA COURT REPORTING INC. (as registered: Canada's Business Registries, AB 2012832453, 2026-11-08)
- **vendor_registry_id**: 2012832453 (AB)
- **vendor_registry_url**: https://ised-isde.canada.ca/cbr-rec/en/search?q=Dicta%20Court%20Reporting%20Inc.
- **vendor_registered_address**: CALGARY, AB (registered office city / province; Canada's Business Registries, AB 2012832453, 2026-11-08)
- **vendor_legal_form**: Alberta Business Corporation (Canada's Business Registries, AB 2012832453, 2026-11-08)
- **vendor_address**: Calgary, AB, Canada (inferred from province/territory code)
- **vendor_country_basis**: vendor located in Canada (wall)=dictacourtreporting.com
- **vendor_bn9**: 830171765 (Canada's Business Registries, AB 2012832453, 2026-11-08)
- **vendor_gst_hst_derived**: 830171765RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://www.dictacourtreporting.com/
- **vendor_emails**: info@dictacourtreporting.com
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); registry identity: 2012832453 (AB) status Active (Canada's Business Registries, AB 2012832453, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: registry: Canada's Business Registries, AB 2012832453, 2026-11-08; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2006-11-22; website: https://www.dictacourtreporting.com/
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Active (Canada's Business Registries, AB 2012832453, 2026-11-08)
- **vendor_incorporation_date**: 2006-11-22
- **vendor_years_in_business**: 20.0 (since 2006-11-22, registry date)
- **vendor_bn_source**: registry: Canada's Business Registries, AB 2012832453, 2026-11-08

## Contract
- **contract_status**: client listing on the vendor's own site (undated)
- **contract_link**: https://www.dictacourtreporting.com/
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (AB) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 830171765RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: yes — reference rule not published (quote the buyer's PO / order number when one is issued)
- **pay_on_sight_missing**: (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Alberta Shorthand Reporters Association — 17008 – 90 Avenue NW, Edmonton, Alberta, T5T 1L6 ⏎ SUBMIT TO: treasurer@asraonline.com (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: DICTA COURT REPORTING INC. (as registered: Canada's Business Registries, AB 2012832453, 2026-11-08) — Calgary, AB, Canada (inferred from province/territory code) | GST/HST 830171765 (Canada's Business Registries, AB 2012832453, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Alberta Shorthand Reporters Association (non-profit / association / cultural body, jurisdiction not stated) — named as a client by the Canad
- **invoice_card_json**: {"bill_to": {"legal_name": "Alberta Shorthand Reporters Association", "legal_name_is_published": true, "address": "17008 – 90 Avenue NW, Edmonton, Alberta, T5T 1L6", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "treasurer@asraonline.com", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (AB)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "830171765RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "DICTA COURT REPORTING INC. (as registered: Canada's Business Registries, AB 2012832453, 2026-11-08)", "bn9": "830171765 (Canada's Business Registries, AB 2012832453, 2026-11-08
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; AP phone or contact for follow-up
- **ap_grade**: C
- **ap_score**: 61
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["treasurer@asraonline.com (finance/accounting dept or supplier-payment office)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://asraonline.com/who-we-are/council-members/", "quote: \"asurer Calgary, Alberta treasurer@asraonline.com Jessica Norris Secretary Calgary, Alberta jessinorris14@gmail.com Sandie Murphy Practice Review Committee Calga\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); no SPF record; mail handled by Google Workspace", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-14441"], "buyer_facts": ["address and phone: the buyer's own site, https://asraonline.com/who-we-are/council-members/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "registry identity: 2012832453 (AB) status Active (Canada's Business Registries, AB 2012832453, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data", "match)", "BN9: registry: Canada's Business Registries, AB 2012832

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://asraonline.com/who-we-are/council-members/ | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, asraonline.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: Alberta Shorthand Reporters Association
- **legal_name_url**: https://asraonline.com/
- **legal_name_quote**: Alberta Shorthand Reporters Association - Home Member Directory Apply Now My Account Cart Search Who We Are Who We Are What We Do Scholarsh
- **logo_url**: https://asraonline.com/wp-content/themes/asra-2015/images/asra-logo.svg
- **logo_basis**: logo image in the site header
- **domain**: asraonline.com
- **key**: lead:6d0148c61e750f73
- **name**: Alberta Shorthand Reporters Association
- **website**: https://asraonline.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Alberta Shorthand Reporters Association
- **legal_name_stated_url**: https://asraonline.com/privacy-policy/
- **legal_name_stated_quote**: Privacy Policy - Alberta Shorthand Reporters Association Member Directory Apply Now My Account Cart Search Who We Are Who We Are What We Do Scholarships Cou

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "17008 – 90 Avenue NW, Edmonton, Alberta, T5T 1L6", "address_country": "CA", "address_url": "https://asraonline.com/who-we-are/council-members/", "address_method": "pattern", "address_quote": "Contact Council Members Address: #309, 17008 – 90 Avenue NW, Edmonton, Alberta, T5T 1L6 2025-2026 ASRA Executive Council Kristen Di Rocco President Calgary, Alberta pr", "domain": "asraonline.com", "key": "lead:6d0148c61e750f73", "name": "asraonline.com", "website": "https://asraonline.com/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, domain unknown)
_not read_

## Vendor role mailboxes found on its site (org_contacts)
_not read_

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Alberta Shorthand Reporters Association | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Alberta%20Shorthand%20Reporters%20Association | 2026-11-08 |
| buyer | Dicta Court Reporting Inc. | found | DICTA COURT REPORTING INC. | 830171765 | 2012832453 | AB | Alberta Business Corporation | Active | 2006-11-22 | CALGARY | AB |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Dicta%20Court%20Reporting%20Inc. | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Alberta Shorthand Reporters Association |  |  |  |  |  |  |  |  |  |  |
| b | Dicta Court Reporting Inc. |  |  |  |  |  |  |  |  |  |  |
| v | Dicta Court Reporting Inc. |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:6d0148c61e750f73",
 "ap_contact_team": {
  "emails": [
   "treasurer@asraonline.com"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "treasurer@asraonline.com",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://asraonline.com/who-we-are/council-members/",
    "quote": "asurer Calgary, Alberta treasurer@asraonline.com Jessica Norris Secretary Calgary, Alberta jessinorris14@gmail.com Sandie Murphy Practice Review Committee Calgary, Alberta ce",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "asraonline.com",
    "task_id": "CL-LD-14441"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of asraonline.com (14 pages, robots.txt respected), no AI, no search engine"
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
| ca_nwt:0000003683 | Justice | Court Reporting Services | 1325000.0 |  |  | https://www.fin.gov.nt.ca/en/resources/contracts-over-5000-report?f%5B0%5D=field_resource_category_legacy%3A582 |

## Open questions for hand research (layer 2)

- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
