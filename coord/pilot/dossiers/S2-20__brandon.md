# S2-20 — Brandon ⇄ MNP LLP

Stratum: **S2_complete_no_published_PO_rule** · pay on sight: yes — reference rule not published (quote the buyer's PO / order number when one is issued) · channel tier 1 · AP grade C · missing: (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: City of Brandon City of Brandon — 410 9th Street, Brandon, MB R7A 6A2
SUBMIT TO: payables@brandon.ca (invoicing/AP mailbox, confirmed by the referee) | tender portal (not an invoice channel): MERX
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: MNP LLP — 200, 5019 - 49 Ave, Leduc, AB, T9E 6T5 (carried from this vendor's row with Thorhild County) | GST/HST 103697215RT0001 (account derived from the BN9)
TAX: DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https: | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Brandon (organisation (type not stated in the record), jurisdiction not stated) — public contract / purchase award in the last 12 months (da
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 82
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 1
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Brandon (organisation (type not stated in the record), jurisdiction not stated) — public contract / purchase award in the last 12 months (dated record): MNP LLP | awarded 2026-08-12 | published by: auditor of record (own audited financial statements, auditor's report signed in Brandon, M | record: https://media-002-ca.cdn.govstack.com/brandon-013-ca/media/vaiaudx5/2025-financial-statement.pdf | vendor in Canada because: auditor of record (own audited financial statements, auditor's report signed in Brandon, Manitoba)=rol matters prior to their approval of the consolidated financial statements. | MNP LLP, as the City's appointed external | status rule: likely active (record dated in the last 12 months: auditor of record (own audited financial statements, auditor's report signed in Brandon, M)
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: lead:fe80ccbe26b8e2a4
- **tier**: B
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: auditor of record (own audited financial statements, auditor's report signed in Brandon, M; 0 in the contract dataset)

## Buyer
- **buyer**: Brandon
- **buyer_website**: https://purchasing.brandon.ca/
- **buyer_address**: 410 9th Street, Brandon, MB R7A 6A2
- **buyer_phone**: 204.729.2186
- **buyer_contact_evidence_url**: https://www.brandon.ca/city-hall/contact-us/
- **buyer_legal_name_as_published**: City of Brandon City of Brandon
- **buyer_logo_url**: https://purchasing.brandon.ca/images/logo.svg
- **buyer_website_status**: site answers
- **buyer_type**: municipality / local government (from the organisation's name / web domain)
- **buyer_sector**: government: municipal
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q61432; city; municipal government in Canada
- **buyer_founded**: 1882-00-00 (Wikidata Q61432, official website on the organisation's domain (http://www.brandon.ca/) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.brandon.ca/city-hall/contact-us/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Note: A municipality is not a government for purposes of the GST/HST"); charge GST/HST; derived from buyer type, not published by the buyer
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: payables@brandon.ca
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://purchasing.brandon.ca/docs/Conducting_Business_with_Procurement_Services.pdf
- **email_evidence_quote**: r – City Hall 410 - 9th Street Brandon, Manitoba R7A 6A2 Procurement Services contact information is: Accounts Payable Clerk (204) 729-2224 payables@brandon.ca Procurement Clerk – Purchase Orders (204) 729-2261
- **email_evidence_context**: s and is located at the following address: City of Brandon - Procurement Services Finance Department Main Floor – City Hall 410 - 9th Street Brandon, Manitoba R7A 6A2 Procurement Services contact information is: Accounts Payable Clerk (204) 729-2224 payables@brandon.ca Procurement Clerk – Purchase Orders (204) 729-2261 purchorder@brandon.ca Procurement Clerk - Bid Opportunities (204) 729-2251 purchasing@brandon.ca Procurement Specialist (204) 729-2526 purchasing@brandon.ca Procurement Manager (204) 729-2252 purcha (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: payables@brandon.ca (invoicing/AP) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08 | page: https://purchasing.brandon.ca/docs/Conducting_Business_with_Procurement_Services.pdf | quote: "r – City Hall 410 - 9th Street Brandon, Manitoba R7A 6A2 Procurement Services contact information is: Accounts Payable Clerk (204) 729-2224 payables@brandon.ca " | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00096
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by Microsoft 365
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject; pct=100; rua=mailto:dmarc@brandon.ca; ruf=mailto:dmarc@brandon.ca; fo=1
- **dmarc_record_domain**: brandon.ca
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 ip4:38.64.148.42/27 ip4:216.36.151.192/27 ip4:67.231.158.158 ip4:67.231.151.29 ip4:170.153.166.12 ip4:170.153.166.13 ip4:170.153.66.12 ip4:170.153.66.13 ip4:67.231.152.177 ip4:208.84.65.220 include:spf.protection.outlook.com include:mandrillapp.com ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_phone**: (204) 729-2224 (as printed on https://purchasing.brandon.ca/docs/Conducting_Business_with_Procurement_Services.pdf, re-read 2026-11-08)
- **invoice_portal_url**: MERX
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **ap_system_hint**: named on the buyer's page: MERX (as printed on https://purchasing.brandon.ca/docs/Conducting_Business_with_Procurement_Services.pdf, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "portal_url": "MERX", "portal_kind": "actionable supplier / invoice portal named by the buyer", "ap_phone": "(204) 729-2224 (as printed on https://purchasing.brandon.ca/docs/Conducting_Business_with_Procurement_Services.pdf, re-read 2026-11-08)"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: City of Brandon City of Brandon — 410 9th Street, Brandon, MB R7A 6A2 ⏎ SUBMIT TO: payables@brandon.ca (invoicing/AP mailbox, confirmed by the referee) | tender portal (not an invoice channel): MERX ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: MNP LLP — 200, 5019 - 49 Ave, Leduc, AB, T9E 6T5 (carried from this vendor's row with Thorhild County) | GST/HST 103697215RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https: | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Brandon (organisation (type not stated in the record), jurisdiction not stated) — public contract / purchase award in the last 12 months (da
- **invoice_card_json**: {"bill_to": {"legal_name": "City of Brandon City of Brandon", "legal_name_is_published": true, "address": "410 9th Street, Brandon, MB R7A 6A2", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "payables@brandon.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "MERX", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: MERX (as printed on https://purchasing.brandon.ca/docs/Conducting_Business_with_Procurement_Services.pdf, re-read 2026-11-08)", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "tender portal (not an invoice channel)"}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.can", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (MB)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "", "vendor_qst": ""}, "vendor_identity": {"legal_name": "MNP LLP", "bn9": "103697215", "neq": "", "remit_address": "200, 50
- **invoice_readiness**: 6/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number; vendor legal name
- **ap_grade**: C
- **ap_score**: 73
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: finance mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: MNP LLP
- **vendor_registered_address**: 200, 5019 - 49 Ave, Leduc, AB, T9E 6T5 (carried from this vendor's row with Thorhild County)
- **vendor_country_basis**: auditor of record (own audited financial statements, auditor's report signed in Brandon, Manitoba)=rol matters prior to their approval of the consolidated financial statements. | MNP LLP, as the City's appointed external audit ... uards. | August 12, 2026 Brandon, Manitoba
- **vendor_bn9**: 103697215
- **vendor_facts_provenance**: name and address: the record's vendor block (auditor of record (own audited financial statements, auditor's report signed in Brandon, M); BN9: corporations_canada 1695592 (exact match) — carried from this vendor's row with Thorhild County; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_bn_source**: corporations_canada 1695592 (exact match) — carried from this vendor's row with Thorhild County

## Contract
- **contract_status**: likely active (record dated in the last 12 months: auditor of record (own audited financial statements, auditor's report signed in Brandon, M)
- **award_date**: 2026-08-12
- **contract_link**: https://media-002-ca.cdn.govstack.com/brandon-013-ca/media/vaiaudx5/2025-financial-statement.pdf
- **source**: auditor of record (own audited financial statements, auditor's report signed in Brandon, M
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: auditor of record (own audited financial statements, auditor's report signed in Brandon, M; 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Note: A municipality is not a government for purposes of the GST/HST"); charge GST/HST; derived from buyer type, not published by the buyer
- **tax_rate_indicative_derived**: GST 5% (MB) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)

## Pay on sight / grades
- **pay_on_sight**: yes — reference rule not published (quote the buyer's PO / order number when one is issued)
- **pay_on_sight_missing**: (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: City of Brandon City of Brandon — 410 9th Street, Brandon, MB R7A 6A2 ⏎ SUBMIT TO: payables@brandon.ca (invoicing/AP mailbox, confirmed by the referee) | tender portal (not an invoice channel): MERX ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: MNP LLP — 200, 5019 - 49 Ave, Leduc, AB, T9E 6T5 (carried from this vendor's row with Thorhild County) | GST/HST 103697215RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https: | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Brandon (organisation (type not stated in the record), jurisdiction not stated) — public contract / purchase award in the last 12 months (da
- **invoice_card_json**: {"bill_to": {"legal_name": "City of Brandon City of Brandon", "legal_name_is_published": true, "address": "410 9th Street, Brandon, MB R7A 6A2", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "payables@brandon.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "MERX", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: MERX (as printed on https://purchasing.brandon.ca/docs/Conducting_Business_with_Procurement_Services.pdf, re-read 2026-11-08)", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "tender portal (not an invoice channel)"}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.can", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (MB)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "", "vendor_qst": ""}, "vendor_identity": {"legal_name": "MNP LLP", "bn9": "103697215", "neq": "", "remit_address": "200, 50
- **invoice_readiness**: 6/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number; vendor legal name
- **ap_grade**: C
- **ap_score**: 73
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: finance mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["payables@brandon.ca (invoicing/AP)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08", "page: https://purchasing.brandon.ca/docs/Conducting_Business_with_Procurement_Services.pdf", "quote: \"r – City Hall 410 - 9th Street Brandon, Manitoba R7A 6A2 Procurement Services contact information is: Accounts Payable Clerk (204) 729-2224 payables@brandon.ca \"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00096"], "buyer_facts": ["address and phone: the buyer's own site, https://www.brandon.ca/city-hall/contact-us/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (auditor of record (own audited financial statements, auditor's report signed in Brandon, M)", "BN9: corporations_canada 16955

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://purchasing.brandon.ca/docs/Conducting_Business_with_Procurement_Services.pdf | 2026-11-08 | ok |  |  | MERX | (204) 729-2224 |  |  |  |  |  |

## Buyer site facts (org_extras, domain unknown)
_not read_

## Buyer role mailboxes found on its site (org_contacts)
_not read_

## Vendor site facts (org_extras, domain unknown)
_not read_

## Vendor role mailboxes found on its site (org_contacts)
_not read_

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | api_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Brandon | not_found |  |  |  | Corporations Canada (open data) |  |  |  |  |  |  | https://open.canada.ca/data/en/dataset/0032ce54-c5dd-4b66-99a0-320a7b5e99f2 | 2026-11-08 |

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Brandon | Q61432 | official website on the organisation's domain (http://www.brandon.ca/) + name |  | Brandon | Brandon | city; municipal government in Canada |  | Canada | 1882-00-00 |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:fe80ccbe26b8e2a4",
 "ap_contact_team": {
  "emails": [
   "payables@brandon.ca",
   "purchasing@brandon.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "payables@brandon.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://purchasing.brandon.ca/docs/Conducting_Business_with_Procurement_Services.pdf",
    "quote": "r – City Hall 410 - 9th Street Brandon, Manitoba R7A 6A2 Procurement Services contact information is: Accounts Payable Clerk (204) 729-2224 payables@brandon.ca Procurement Clerk – Purchase Orders (204) 729-2261",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Brandon",
    "task_id": "CL-LD-32964"
   },
   {
    "email": "payables@brandon.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://purchasing.brandon.ca/docs/Conducting_Business_with_Procurement_Services.pdf",
    "quote": "r – City Hall 410 - 9th Street Brandon, Manitoba R7A 6A2 Procurement Services contact information is: Accounts Payable Clerk (204) 729-2224 payables@brandon.ca Procurement Clerk – Purchase Orders (204) 729-2261",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Brandon",
    "task_id": "CL-WS-00096"
   },
   {
    "email": "purchasing@brandon.ca",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://purchasing.brandon.ca/",
    "quote": "6) Type PROPOSAL Status OPEN Additional Information Bidders are advised that the signed Confidentiality Acknowledgement form can be sent to purchasing@brandon.ca. You are required to submit your information to obtain the documents. See instructions above. Award Documents Bid Documents Unev",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Brandon",
    "task_id": "CL-LD-32964"
   },
   {
    "email": "purchasing@brandon.ca",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://purchasing.brandon.ca/docs/Conducting_Business_with_Procurement_Services.pdf",
    "quote": "Procurement Clerk - Bid Opportunities (204) 729-2251 purchasing@brandon.ca Procurement Specialist (204) 729-2526",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Brandon",
    "task_id": "CL-WS-00096"
   }
  ]
 },
 "research_status": {
  "found": 4
 },
 "queries_tried": [
  "site crawl of purchasing.brandon.ca (22 pages, robots.txt respected), no AI, no search engine",
  "site crawl of purchasing.brandon.ca (22 pages, robots.txt respected), no AI, no search engine",
  "web search for the buyer's invoicing / accounts payable page (the search only gave the address); the page then read by tools/deep_pages.py with the crawler's rules, no AI",
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

- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
