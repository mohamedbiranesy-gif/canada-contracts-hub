# S5-33 — SOAS University of London (School of Oriental and African Studies) ⇄ Centre on International Policy Studies

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 1 · AP grade B · missing: the vendor's GST/HST number (BN9)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: SOAS University of London (School of Oriental and African Studies) — 10 Thornhaugh Street, Russell Square, London, WC1H 0XG
SUBMIT TO: accounts.payable@soas.ac.uk (invoicing/AP mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: yes (as published: must be sent to the specified department and must quote the full Contract reference or Purchase Order
FROM / REMIT TO: Centre for International (stated on the vendor's legal page: https://www.cips-cepi.ca/about/) — 120 University Ave., Ottawa, ON K1N 6N5 | GST/HST number not public
TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); UK VAT is | CURRENCY: DERIVED: GBP (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: CIPS 10th Anniversary – Centre for International Policy Studies
```

## Relationship
- **rank_group**: E4
- **data_quality_score**: 68
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: SOAS University of London (School of Oriental and African Studies) (university / college, jurisdiction not stated) — linked from the Canada-located vendor's site (weakest listed relationship): Centre on International Policy Studies | subject: CIPS 10th Anniversary – Centre for International Policy Studies | published by: the Canada-located vendor's own website | record: https://www.cips-cepi.ca/projects/cips-10th-anniversary/ | vendor in Canada because: vendor located in Canada (wd)=cips-cepi.ca | status rule: linked from a page of the Canada-located vendor's site (not a client page)
- **how_relationship_was_found**: tools/provider_mentions.py / news_match.py found the buyer linked from the vendor's own site or release
- **keys**: lead:54cef5c2ed23dc72
- **tier**: E
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: SOAS University of London (School of Oriental and African Studies)
- **buyer_website**: https://soas.ac.uk/
- **buyer_address**: 10 Thornhaugh Street, Russell Square, London, WC1H 0XG
- **buyer_phone**: +44 (0)20 3510 6974
- **buyer_contact_evidence_url**: https://www.soas.ac.uk/contacts
- **buyer_legal_name_as_published**: SOAS University of London (School of Oriental and African Studies)
- **buyer_logo_url**: https://www.soas.ac.uk/themes/custom/numiko/favicons/apple-touch-icon-57x57.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/school/soas-university-of-london
- **buyer_type**: university / college
- **buyer_sector**: education: post-secondary
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.soas.ac.uk/contacts (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); UK VAT is accounted for by the buyer under the reverse charge where applicable
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: accounts.payable@soas.ac.uk
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.soas.ac.uk/contacts
- **email_evidence_quote**: Accounts Payable t: +44 (0)20 7074 5033 e: accounts.payable@soas.ac.uk Press office t: +44 (0)20 7898 4135 e: press@soas.ac.uk HR support If you need to contact the HR team, please log a call o
- **email_evidence_context**: ent and progression t: +44 (0)20 7898 4780 Academic Services t: +44 (0)20 7898 4050 Careers t: +44 (0)20 7898 4115 Finance Office Accounts Receivable t: +44 (0)20 7074 5009 e: accounts.receivable@soas.ac.uk Accounts Payable t: +44 (0)20 7074 5033 e: accounts.payable@soas.ac.uk Press office t: +44 (0)20 7898 4135 e: press@soas.ac.uk HR support If you need to contact the HR team, please log a call on the SOAS Service Portal . If you are not a registered SOAS user, you can contact us by using this specific HR Contact Form . (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: accounts.payable@soas.ac.uk (invoicing/AP) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-01 | page: https://www.soas.ac.uk/contacts | quote: "Accounts Payable t: +44 (0)20 7074 5033 e: accounts.payable@soas.ac.uk Press office t: +44 (0)20 7898 4135 e: press@soas.ac.uk HR support If you need to contact" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by self-hosted or other (mx1.it.soas.ac.uk) | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00152
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by self-hosted or other (mx1.it.soas.ac.uk)
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1; p=quarantine; rua=mailto:dmarc@soas.ac.uk; ruf=mailto:dmarc@soas.ac.uk; fo=1; pct=100; rf=afrf
- **dmarc_record_domain**: soas.ac.uk
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 mx:soas.ac.uk +include:_spf.salesforce.com +include:amazonses.com +include:spf.protection.outlook.com +include:cust-spf.exacttarget.com +include:spf.planoncloud.com ip4:212.219.139.47 ip4:20.162.120.167 ip4:51.140.33.170 ip4:51.140.64.42 ip4:51.140.71.9 ip4:52.151.82.88 ip4:52.151.85.181 ip4:
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **po_required_as_published**: yes (as published: must be sent to the specified department and must quote the full Contract reference or Purchase Order number) (as printed on https://www.soas.ac.uk/sites/default/files/2026-08/SOAS%20Standard%20Terms%20and%20Conditions%20of%20Purchase.pdf, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "po_required": "yes (as published: must be sent to the specified department and must quote the full Contract reference or Purchase Order number) (as printed on https://www.soas.ac.uk/sites/default/files/2026-08/SOAS%20Standard%20Terms%20and%20Conditions%20of%20Purchase.pdf, re-read 2026-11-08)"}
- **invoice_currency_derived**: GBP (derived from the buyer's country; CAD if the parties agreed so)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: SOAS University of London (School of Oriental and African Studies) — 10 Thornhaugh Street, Russell Square, London, WC1H 0XG ⏎ SUBMIT TO: accounts.payable@soas.ac.uk (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: yes (as published: must be sent to the specified department and must quote the full Contract reference or Purchase Order ⏎ FROM / REMIT TO: Centre for International (stated on the vendor's legal page: https://www.cips-cepi.ca/about/) — 120 University Ave., Ottawa, ON K1N 6N5 | GST/HST number not public ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); UK VAT is | CURRENCY: DERIVED: GBP (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: CIPS 10th Anniversary – Centre for International Policy Studies
- **invoice_card_json**: {"bill_to": {"legal_name": "SOAS University of London (School of Oriental and African Studies)", "legal_name_is_published": true, "address": "10 Thornhaugh Street, Russell Square, London, WC1H 0XG", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "accounts.payable@soas.ac.uk", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "yes (as published: must be sent to the specified department and must quote the full Contract reference or Purchase Order number) (as printed on https://www.soas.ac.uk/sites/default/files/2026-08/SOAS%20Standard%20Terms%20and%20Conditions%20of%20Purchase.pdf, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: must be sent to the specified department and must quote the full Contract reference or Purchase Order number) (as printed on https://www.soas.ac.uk/sites/default/files/2026-08/SOAS%)"}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number
- **ap_grade**: B
- **ap_score**: 77
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; currency known | missing: finance mailbox; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published payment terms
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms not published (buyer's default applies)
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: must be sent to the specified department and must quote the full Contract reference or Purchase Order number) (as printed on https://www.soas.ac.uk/sites/default/files/2026-08/SOAS%)

## Vendor
- **vendor**: Centre on International Policy Studies
- **vendor_legal_name**: Centre for International (stated on the vendor's legal page: https://www.cips-cepi.ca/about/)
- **vendor_trading_name**: Centre on International Policy Studies
- **vendor_address**: 120 University Ave., Ottawa, ON K1N 6N5
- **vendor_country_basis**: vendor located in Canada (wd)=cips-cepi.ca
- **vendor_website**: https://cips-cepi.ca
- **vendor_phone**: 613-562-5800
- **vendor_contact_evidence_url**: https://www.cips-cepi.ca/visiting-scholars-and-postdoctoral-fellows-at-cips/
- **vendor_logo_url**: https://www.cips-cepi.ca/wp-content/themes/pressroom-child/images/uottawa-logo.png
- **vendor_website_status**: site answers
- **vendor_linkedin_url**: https://www.linkedin.com/company/cepi-cips/
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); phone / role e-mails / logo: the vendor's own site, https://www.cips-cepi.ca/visiting-scholars-and-postdoctoral-fellows-at-cips/ (tools/org_contacts.py, org_extras.py); website: https://cips-cepi.ca (site answers)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer

## Contract
- **po_required_as_published**: yes (as published: must be sent to the specified department and must quote the full Contract reference or Purchase Order number) (as printed on https://www.soas.ac.uk/sites/default/files/2026-08/SOAS%20Standard%20Terms%20and%20Conditions%20of%20Purchase.pdf, re-read 2026-11-08)
- **contract_status**: linked from a page of the Canada-located vendor's site (not a client page)
- **contract_title**: CIPS 10th Anniversary – Centre for International Policy Studies
- **contract_description**: CIPS 10th Anniversary – Centre for International Policy Studies (the record's title; the source publishes no separate description)
- **contract_link**: https://www.cips-cepi.ca/projects/cips-10th-anniversary/
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); UK VAT is accounted for by the buyer under the reverse charge where applicable
- **invoice_currency_derived**: GBP (derived from the buyer's country; CAD if the parties agreed so)

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: SOAS University of London (School of Oriental and African Studies) — 10 Thornhaugh Street, Russell Square, London, WC1H 0XG ⏎ SUBMIT TO: accounts.payable@soas.ac.uk (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: yes (as published: must be sent to the specified department and must quote the full Contract reference or Purchase Order ⏎ FROM / REMIT TO: Centre for International (stated on the vendor's legal page: https://www.cips-cepi.ca/about/) — 120 University Ave., Ottawa, ON K1N 6N5 | GST/HST number not public ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); UK VAT is | CURRENCY: DERIVED: GBP (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: CIPS 10th Anniversary – Centre for International Policy Studies
- **invoice_card_json**: {"bill_to": {"legal_name": "SOAS University of London (School of Oriental and African Studies)", "legal_name_is_published": true, "address": "10 Thornhaugh Street, Russell Square, London, WC1H 0XG", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "accounts.payable@soas.ac.uk", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "yes (as published: must be sent to the specified department and must quote the full Contract reference or Purchase Order number) (as printed on https://www.soas.ac.uk/sites/default/files/2026-08/SOAS%20Standard%20Terms%20and%20Conditions%20of%20Purchase.pdf, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: must be sent to the specified department and must quote the full Contract reference or Purchase Order number) (as printed on https://www.soas.ac.uk/sites/default/files/2026-08/SOAS%)"}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number
- **ap_grade**: B
- **ap_score**: 77
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; currency known | missing: finance mailbox; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published payment terms
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms not published (buyer's default applies)
- **facts_provenance_json**: {"mailbox": ["accounts.payable@soas.ac.uk (invoicing/AP)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-01", "page: https://www.soas.ac.uk/contacts", "quote: \"Accounts Payable t: +44 (0)20 7074 5033 e: accounts.payable@soas.ac.uk Press office t: +44 (0)20 7898 4135 e: press@soas.ac.uk HR support If you need to contact\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by self-hosted or other (mx1.it.soas.ac.uk)", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00152"], "buyer_facts": ["address and phone: the buyer's own site, https://www.soas.ac.uk/contacts (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "phone / role e-mails / logo: the vendor's own site, https://www.cips-cepi.ca/visiting-scholars-and-postdoctoral-fellows-at-cips/ (tools/org_contacts.py, org_extras.py)", "website: https://cips-cepi.ca (site answers)"], "re

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.soas.ac.uk/contacts | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, soas.ac.uk)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: SOAS University of London (School of Oriental and African Studies)
- **legal_name_url**: https://www.soas.ac.uk/
- **legal_name_quote**: but support gradually helped her feel like she belonged. More blogs Latest news All news All news © SOAS University of London (School of Oriental and African Studies) 2022. All rights reserved. SOAS University of London 10 Thornhaugh Street, Russell Square, London W
- **logo_url**: https://www.soas.ac.uk/themes/custom/numiko/favicons/apple-touch-icon-57x57.png
- **logo_basis**: site icon (apple-touch-icon)
- **domain**: soas.ac.uk
- **key**: lead:54cef5c2ed23dc72
- **name**: SOAS University of London (School of Oriental and African Studies)
- **website**: https://soas.ac.uk/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: SOAS University
- **legal_name_stated_url**: https://www.soas.ac.uk/about
- **legal_name_stated_quote**: past and present Jump to: Notable alumni Jump to: Explore SOAS Jump to: Follow us SOAS at a glance SOAS University of London is a specialist public research university focused on the study of Asia, Africa and the M
- **linkedin_url**: https://www.linkedin.com/school/soas-university-of-london
- **tel_links**: +44(0)2076372388; +44(0)2035106974

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "10 Thornhaugh Street, Russell Square, London, WC1H 0XG", "address_country": "GB", "address_url": "https://www.soas.ac.uk/contacts", "address_method": "pattern", "address_quote": "ental and African Studies) 2022. All rights reserved. SOAS University of London 10 Thornhaugh Street, Russell Square, London WC1H 0XG Switchboard: +44 (0)20 7637 2388 Study Enquiri", "phone": "+44 (0)20 3510 6974", "phone_url": "https://www.soas.ac.uk/contacts", "domain": "soas.ac.uk", "key": "lead:54cef5c2ed23dc72", "name": "soas.ac.uk", "website": "https://soas.ac.uk/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, cips-cepi.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://www.cips-cepi.ca/wp-content/themes/pressroom-child/images/uottawa-logo.png
- **logo_basis**: logo image in the site header
- **domain**: cips-cepi.ca
- **key**: vendor:Centre on International Policy Studies
- **name**: Centre on International Policy Studies
- **website**: https://cips-cepi.ca/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Centre for International
- **legal_name_stated_url**: https://www.cips-cepi.ca/about/
- **legal_name_stated_quote**: About the Centre – Centre for International Policy Studies Subscribe to the CIPS Newsletter No spam, only authentic content. Categories 2483 An
- **linkedin_url**: https://www.linkedin.com/company/cepi-cips/

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "120 University Ave., Ottawa, ON K1N 6N5", "address_country": "CA", "address_url": "https://www.cips-cepi.ca/visiting-scholars-and-postdoctoral-fellows-at-cips/", "address_method": "pattern", "address_quote": "at [email protected] Social Sciences Building 120 University Ave. Ottawa, ON K1N 6N5 Tel. 613-562-5800 ext. 2664 Email: [email protected] Subscribe to the CIPS News", "phone": "613-562-5800", "phone_url": "https://www.cips-cepi.ca/visiting-scholars-and-postdoctoral-fellows-at-cips/", "domain": "cips-cepi.ca", "key": "vd:cips-cepi.ca", "name": "Centre on International Policy Studies", "website": "https://cips-cepi.ca/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | SOAS University of London (School of Oriental and African Studies) |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:54cef5c2ed23dc72",
 "ap_contact_team": {
  "emails": [
   "accounts.payable@soas.ac.uk",
   "procurement@soas.ac.uk"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "accounts.payable@soas.ac.uk",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.soas.ac.uk/contacts",
    "quote": "Accounts Payable t: +44 (0)20 7074 5033 e: accounts.payable@soas.ac.uk Press office t: +44 (0)20 7898 4135 e: press@soas.ac.uk HR support If you need to contact the HR team, please log a call o",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "soas.ac.uk",
    "task_id": "CL-WS-00152"
   },
   {
    "email": "procurement@soas.ac.uk",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.soas.ac.uk/about/governance/procurement",
    "quote": "he University does not have an approved supplier list. If you are interested in supplying goods or services to the University, please email procurement@soas.ac.uk . SOAS uses Intend for the provision of its Electronic Tendering Portal. Register to find out more information . Fraudulent e-m",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "soas.ac.uk",
    "task_id": "CL-LD-09029"
   }
  ]
 },
 "research_status": {
  "found": 2
 },
 "queries_tried": [
  "site crawl of soas.ac.uk (25 pages, robots.txt respected), no AI, no search engine",
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

## The vendor's other buyers in the dataset (first 60 of 0)
_none_

## Open questions for hand research (layer 2)

- the vendor's GST/HST number (BN9)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
