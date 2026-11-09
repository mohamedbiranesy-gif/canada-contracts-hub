# S2-21 — Pima County Public Library ⇄ BiblioCommons Corp.

Stratum: **S2_complete_no_published_PO_rule** · pay on sight: yes — reference rule not published (quote the buyer's PO / order number when one is issued) · channel tier 1 · AP grade C · missing: (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Pima County (stated on https://www.pima.gov/) — 115 N Church Avenue, 2nd Floor, Suite 231, Tucson, AZ 85701
SUBMIT TO: vendors@pima.gov (purchasing mailbox, confirmed by the referee) | invoice portal: Workday supplier portal
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: BIBLIOCOMMONS CORP. (as registered: Canada's Business Registries, ON 2733173, 2026-11-08) — 119 Spadina Avenue , Toronto , ON, M5V 2L1, Canada | GST/HST 755272937 (Canada's Business Registries, ON 2733173, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state  | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Recent Activity | Pima County Public Library | BiblioCommons
```

## Relationship
- **rank_group**: T2
- **data_quality_score**: 61
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Pima County Public Library (non-profit / association / cultural body, jurisdiction not stated) — active paid service of a Canada-HQ vendor seen on the buyer's own site: BiblioCommons Corp. | subject: Recent Activity | Pima County Public Library | BiblioCommons | awarded 2026-11-02 | published by: the buyer's own website (service of a Canada-HQ vendor in use) | record: https://pima.bibliocommons.com/ | vendor in Canada because: service of a Canada-HQ vendor seen on the buyer's own site (tech)=BiblioCommons Corp. 5060 Spectrum Way, Suite 100 Mississauga, ON L4W 5N5 | status rule: active service seen on the buyer's own site (2026-11-02): Canada-HQ vendor BiblioCommons Corp.
- **how_relationship_was_found**: tools/tech_portals2.py / tech_relationships.py found the buyer's own web property running the Canada-HQ vendor's paid platform (portal host or embedded service), dated by the page read
- **keys**: lead:2e70e9a9f333657a
- **tier**: T
- **grade**: 2
- **records_with_this_vendor**: 1 (relationship record: the buyer's own website (service of a Canada-HQ vendor in use); 0 in the contract dataset)

## Buyer
- **buyer**: Pima County Public Library
- **buyer_website**: https://www.pima.gov/
- **buyer_address**: 115 N Church Avenue, 2nd Floor, Suite 231, Tucson, AZ 85701
- **buyer_phone**: 520-724-8028
- **buyer_contact_evidence_url**: https://www.pima.gov/
- **buyer_legal_name_as_published**: Pima County (stated on https://www.pima.gov/)
- **buyer_logo_url**: https://content.civicplus.com/api/assets/79167038-e4aa-4958-bbce-4c1a80603e4d?cache=180
- **buyer_website_status**: site answers
- **buyer_type**: non-profit / association / cultural body
- **buyer_sector**: non-profit
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q7194577; library network
- **buyer_budget_or_revenue**: revenue 48090946 Q4917 (Wikidata Q7194577, official website on the organisation's domain (http://www.library.pima.gov/) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.pima.gov/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: vendors@pima.gov
- **email_type**: purchasing
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); purchasing mailbox
- **email_evidence_url**: https://www.pima.gov/vendor-registration
- **email_evidence_quote**: ed help?<\/h2><ul><li>Contact Bidnet directly at 800-835-4603, Option 2 for assistance with registering.<\/li><li>Contact <a href=\\"mailto:vendors@pima.gov\\">vendors@pima.gov<\/a> for assistance with updating your Workday supplier account.<\/li><\/ul>"}},"titles":{"name":{"en":"Vendor Se
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: vendors@pima.gov (purchasing) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://www.pima.gov/vendor-registration | quote: "ed help?<\/h2><ul><li>Contact Bidnet directly at 800-835-4603, Option 2 for assistance with registering.<\/li><li>Contact <a href=\\"mailto:vendors@pima.gov\\">" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-42124
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Microsoft 365
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none; rua=mailto:bf2af98513ae.a@dmarcinput.com,mailto:dmarc_reports@pima.gov; ruf=mailto:bf2af98513ae.f@dmarcinput.com,mailto:dmarc_reports@pima.gov; fo=1; pct=100
- **dmarc_record_domain**: pima.gov
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 mx ip4:159.233.0.0/16 a:librarycatalog.pima.gov include:spf.protection.outlook.com include:_spf-sg.accela.com include:_spf-eus.teamdynamix.com include:amazonses.com include:zcsend.net include:librarymsg.com ~all
- **mta_sts**: yes (v=STSv1; id=1678311826)
- **tls_rpt**: yes (v=TLSRPTv1; rua=mailto:bf2af98513ae.m@dmarcinput.com)
- **bimi**: no BIMI record
- **invoice_portal_url**: Workday supplier portal
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **ap_system_hint**: named on the buyer's page: Workday
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "portal_url": "Workday supplier portal", "portal_kind": "actionable supplier / invoice portal named by the buyer"}
- **invoice_currency_derived**: USD (derived from the buyer's country; CAD if the parties agreed so)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Pima County (stated on https://www.pima.gov/) — 115 N Church Avenue, 2nd Floor, Suite 231, Tucson, AZ 85701 ⏎ SUBMIT TO: vendors@pima.gov (purchasing mailbox, confirmed by the referee) | invoice portal: Workday supplier portal ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: BIBLIOCOMMONS CORP. (as registered: Canada's Business Registries, ON 2733173, 2026-11-08) — 119 Spadina Avenue , Toronto , ON, M5V 2L1, Canada | GST/HST 755272937 (Canada's Business Registries, ON 2733173, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state  | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Recent Activity | Pima County Public Library | BiblioCommons
- **invoice_card_json**: {"bill_to": {"legal_name": "Pima County (stated on https://www.pima.gov/)", "legal_name_is_published": true, "address": "115 N Church Avenue, 2nd Floor, Suite 231, Tucson, AZ 85701", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "vendors@pima.gov", "email_type": "purchasing", "supplier_setup_url": "", "portal_url": "Workday supplier portal", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: Workday", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state ", "buyer_tax_status_is_published": false, "indicative_rate": "", "currency": "DERIVED: USD (derived from the buyer's country; C", "currency_is_published": false, "vendor_gst_hst": "755272937RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "BIBLIOCOMMONS CORP. (as registered: Canada's Business Registries, ON 2733173, 2026-11-08)
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
- **vendor**: BiblioCommons Corp.
- **vendor_legal_name**: BIBLIOCOMMONS CORP. (as registered: Canada's Business Registries, ON 2733173, 2026-11-08)
- **vendor_registry_id**: 2733173 (ON)
- **vendor_registry_url**: https://ised-isde.canada.ca/cbr-rec/en/search?q=BiblioCommons%20Corp.
- **vendor_registered_address**: Mississauga, Ontario (registered office city / province; Canada's Business Registries, ON 2733173, 2026-11-08)
- **vendor_legal_form**: ONTARIO BUSINESS CORP. (Canada's Business Registries, ON 2733173, 2026-11-08)
- **vendor_address**: 119 Spadina Avenue , Toronto , ON, M5V 2L1, Canada
- **vendor_country_basis**: service of a Canada-HQ vendor seen on the buyer's own site (tech)=BiblioCommons Corp. 5060 Spectrum Way, Suite 100 Mississauga, ON L4W 5N5
- **vendor_bn9**: 755272937 (Canada's Business Registries, ON 2733173, 2026-11-08)
- **vendor_gst_hst_derived**: 755272937RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_facts_provenance**: name and address: the record's vendor block (the buyer's own website (service of a Canada-HQ vendor in use)); registry identity: 2733173 (ON) status Active — incorporated (Canada's Business Registries, ON 2733173, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: registry: Canada's Business Registries, ON 2733173, 2026-11-08; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2019-12-19
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Active — incorporated (Canada's Business Registries, ON 2733173, 2026-11-08)
- **vendor_incorporation_date**: 2019-12-19
- **vendor_years_in_business**: 6.9 (since 2019-12-19, registry date)
- **vendor_bn_source**: registry: Canada's Business Registries, ON 2733173, 2026-11-08

## Contract
- **contract_status**: active service seen on the buyer's own site (2026-11-02): Canada-HQ vendor BiblioCommons Corp.
- **contract_title**: Recent Activity | Pima County Public Library | BiblioCommons
- **contract_description**: Recent Activity | Pima County Public Library | BiblioCommons (the record's title; the source publishes no separate description)
- **award_date**: 2026-11-02
- **contract_link**: https://pima.bibliocommons.com/
- **source**: the buyer's own website (service of a Canada-HQ vendor in use)
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the buyer's own website (service of a Canada-HQ vendor in use); 0 in the contract dataset)
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **invoice_currency_derived**: USD (derived from the buyer's country; CAD if the parties agreed so)
- **vendor_gst_hst_derived**: 755272937RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: yes — reference rule not published (quote the buyer's PO / order number when one is issued)
- **pay_on_sight_missing**: (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Pima County (stated on https://www.pima.gov/) — 115 N Church Avenue, 2nd Floor, Suite 231, Tucson, AZ 85701 ⏎ SUBMIT TO: vendors@pima.gov (purchasing mailbox, confirmed by the referee) | invoice portal: Workday supplier portal ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: BIBLIOCOMMONS CORP. (as registered: Canada's Business Registries, ON 2733173, 2026-11-08) — 119 Spadina Avenue , Toronto , ON, M5V 2L1, Canada | GST/HST 755272937 (Canada's Business Registries, ON 2733173, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state  | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Recent Activity | Pima County Public Library | BiblioCommons
- **invoice_card_json**: {"bill_to": {"legal_name": "Pima County (stated on https://www.pima.gov/)", "legal_name_is_published": true, "address": "115 N Church Avenue, 2nd Floor, Suite 231, Tucson, AZ 85701", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "vendors@pima.gov", "email_type": "purchasing", "supplier_setup_url": "", "portal_url": "Workday supplier portal", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: Workday", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state ", "buyer_tax_status_is_published": false, "indicative_rate": "", "currency": "DERIVED: USD (derived from the buyer's country; C", "currency_is_published": false, "vendor_gst_hst": "755272937RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "BIBLIOCOMMONS CORP. (as registered: Canada's Business Registries, ON 2733173, 2026-11-08)
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["vendors@pima.gov (purchasing)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://www.pima.gov/vendor-registration", "quote: \"ed help?<\\/h2><ul><li>Contact Bidnet directly at 800-835-4603, Option 2 for assistance with registering.<\\/li><li>Contact <a href=\\\\\"mailto:vendors@pima.gov\\\\\">\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-42124"], "buyer_facts": ["address and phone: the buyer's own site, https://www.pima.gov/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (the buyer's own website (service of a Canada-HQ vendor in use))", "registry identity: 2733173 (ON) status Active — incorporated (Canada's Business Registries, ON 2733173, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook b

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.pima.gov/vendor-registration | 2026-11-08 | ok |  |  | Workday supplier portal |  |  |  |  |  |  |

## Buyer site facts (org_extras, pima.gov)
- **status**: ok
- **pages**: 1
- **language**: en
- **logo_url**: https://content.civicplus.com/api/assets/79167038-e4aa-4958-bbce-4c1a80603e4d?cache=180
- **logo_basis**: logo image on the site
- **domain**: pima.gov
- **key**: lead:2e70e9a9f333657a
- **name**: Pima County Public Library
- **website**: https://pima.gov/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Pima County
- **legal_name_stated_url**: https://www.pima.gov/
- **legal_name_stated_quote**: Pima County, AZ | Official Website Skip to Main Content Government Departments & Offices Services I want to...

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 1, "address": "115 N Church Avenue, 2nd Floor, Suite 231, Tucson, AZ 85701", "address_country": "US", "address_url": "https://www.pima.gov/", "address_method": "pattern", "address_quote": "b9ec4e1e03bd\",\"data\":{\"name\":{\"en\":\"Contact Us\"},\"article\":{\"en\":\" Pima County 115 N Church Avenue 2nd Floor, Suite 231 Tucson, AZ 85701 Phone: 520-724-9999 Toll Free: 800-775-74", "phone": "520-724-8028", "phone_url": "https://www.pima.gov/", "domain": "pima.gov", "key": "lead:2e70e9a9f333657a", "name": "Pima County Public Library", "website": "https://pima.gov/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, domain unknown)
_not read_

## Vendor role mailboxes found on its site (org_contacts)
_not read_

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Pima County Public Library | Q7194577 | official website on the organisation's domain (http://www.library.pima.gov/) + name |  | Pima County Public Library |  | library network |  | United States |  | Tucson |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:2e70e9a9f333657a",
 "ap_contact_team": {
  "emails": [
   "vendors@pima.gov"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "vendors@pima.gov",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.pima.gov/vendor-registration",
    "quote": "ed help?<\\/h2><ul><li>Contact Bidnet directly at 800-835-4603, Option 2 for assistance with registering.<\\/li><li>Contact <a href=\\\\\"mailto:vendors@pima.gov\\\\\">vendors@pima.gov<\\/a> for assistance with updating your Workday supplier account.<\\/li><\\/ul>\"}},\"titles\":{\"name\":{\"en\":\"Vendor Se",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Pima County Public Library",
    "task_id": "CL-LD-42124"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of www.pima.gov (25 pages, robots.txt respected), no AI, no search engine"
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

## The vendor's other buyers in the dataset (first 60 of 6)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_bidsandtenders:32761475-333e-41ac-b891-ffddc5f83ade:1 | City of Mississauga | Library Online Resource Discovery & Mobile App |  |  |  | https://mississauga.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/32761475-333e-41ac-b891-ffddc5f83ade |
| us_county_fulton_ga:81357d5a48e75900-650 | Fulton County, Georgia — Library | Books-Library | 1042856.5700000001 |  |  | https://data.fultoncountyga.gov/d/mxhc-krcg |
| us_socrata_sweep_continue:data.fultoncountyga.gov:2jx8-2ffx:_vendor_id_:_81357d5a48e75900_vendor_name_:_Bi~75a33202896d | Fulton County Government (GA) |  |  |  |  | https://data.fultoncountyga.gov/d/2jx8-2ffx |
| us_socrata_sweep_continue:data.fultoncountyga.gov:2jx8-2ffx:_vendor_id_:_81357d5a48e75900_vendor_name_:_Bi~1e00a517d323 | Fulton County Government (GA) |  |  |  |  | https://data.fultoncountyga.gov/d/2jx8-2ffx |
| us_socrata_sweep_continue:data.fultoncountyga.gov:2jx8-2ffx:_vendor_id_:_ccc6a7f05b8387ab_vendor_name_:_Bi~c355691972d8 | Fulton County Government (GA) |  |  |  |  | https://data.fultoncountyga.gov/d/2jx8-2ffx |
| us_socrata_sweep_continue:data.fultoncountyga.gov:2jx8-2ffx:_vendor_id_:_ccc6a7f05b8387ab_vendor_name_:_Bi~f8057c8ad9ef | Fulton County Government (GA) |  |  |  |  | https://data.fultoncountyga.gov/d/2jx8-2ffx |

## Open questions for hand research (layer 2)

- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
