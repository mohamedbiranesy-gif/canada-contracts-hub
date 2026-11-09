# S2-14 — United States Postal Service ⇄ inferred: Canada Post Corporation

Stratum: **S2_complete_no_published_PO_rule** · pay on sight: yes — reference rule not published (quote the buyer's PO / order number when one is issued) · channel tier 1 · AP grade C · missing: (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: United States Postal Service (schema.org JSON-LD legalName on https://www.usps.com/) — L'Enfant Plaza; Washington, D.C. (Wikidata Q668687, official website on the organisation's domain (http://www.usps.gov/) + name; 2026-11-08)
SUBMIT TO: accountspayablesuppliermaintenance@usps.gov (invoicing/AP mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state  | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: United States Postal Service (government ministry / agency, CA) — inferred: no record; the organisation's type and province make a Canadian 
```

## Relationship
- **rank_group**: I4
- **data_quality_score**: 58
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 6
- **reverify_due**: no
- **inference_confidence**: LOW (plausible supplier only)
- **relationship_detail**: United States Postal Service (government ministry / agency, CA) — inferred: no record; the organisation's type and province make a Canadian supplier relationship near-certain: inferred: Canada Post Corporation | published by: inference from the buyer's type and province (no contract, payment or listing record) | vendor in Canada because: the vendor's own site, https://www.canadapost-postescanada.ca/cpc/en/our-company/transparency-and-trust/privacy-centre/info-source/additional-information.page: 'Access to Information and Privacy Canada Post Corporation 2 | status rule: inferred relationship (no record): low confidence; the buyer is an organisation located in Canada; generic: Canada Post holds the exclusive privilege of collecting, transmitting and delivering letters within Canada (Cana
- **how_relationship_was_found**: no record; tools/org_lists.py / osm_orgs.py / the crawlers placed the organisation in Canada by type and province; the vendor named is the Canada-located supplier such bodies almost always pay (see `vendor_country_basis`)
- **keys**: wd:Q668687
- **tier**: I
- **grade**: 4

## Buyer
- **buyer**: United States Postal Service
- **buyer_website**: https://usps.gov
- **buyer_address**: L'Enfant Plaza; Washington, D.C. (Wikidata Q668687, official website on the organisation's domain (http://www.usps.gov/) + name; 2026-11-08)
- **buyer_phone**: 1-800-222-1811
- **buyer_contact_evidence_url**: https://www.usps.com/help/contact-us.htm
- **buyer_legal_name_as_published**: United States Postal Service (schema.org JSON-LD legalName on https://www.usps.com/)
- **buyer_logo_url**: https://www.usps.com/global-elements/images/logo_mobile.svg
- **buyer_website_status**: site answers
- **buyer_type**: government ministry / agency
- **buyer_sector**: government: provincial / federal
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q668687; independent agency of the United States government; postal service; business
- **buyer_founded**: 1971-07-01 (Wikidata Q668687, official website on the organisation's domain (http://www.usps.gov/) + name; 2026-11-08)
- **buyer_budget_or_revenue**: revenue 79324000000 Q4917 (Wikidata Q668687, official website on the organisation's domain (http://www.usps.gov/) + name; 2026-11-08)
- **buyer_employees**: 546000; 625113 (Wikidata Q668687, official website on the organisation's domain (http://www.usps.gov/) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.usps.com/help/contact-us.htm (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_payment_method_preference**: Electronic Funds Transfer (EFT) Enrol (as printed on https://about.usps.com/what/business-services/facilities-leasing-property-management/assets/pdf/supplier-EFT-enrollment-form.pdf, re-read 2026-11-08)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: accountspayablesuppliermaintenance@usps.gov
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://about.usps.com/what/business-services/facilities-leasing-property-management/assets/pdf/supplier-EFT-enrollment-form.pdf
- **email_evidence_quote**: acting Officer Representative, Postmaster, or USPS contact. USPS Personnel: Send completed form via one of the following methods: By email: accountspayablesuppliermaintenance@usps.gov By fax: (650) 577-4640 B. Supplier/Payee Information (Supplier/Payee completes.) Privacy Act Statement: Yo
- **email_evidence_context**: y used for domestic bank EFT enrollment. Suppliers/Payees: Submit completed form to Contracting Officer, Contracting Officer Representative, Postmaster, or USPS contact. USPS Personnel: Send completed form via one of the following methods: By email: accountspayablesuppliermaintenance@usps.gov By fax: (650) 577-4640 B. Supplier/Payee Information (Supplier/Payee completes.) Privacy Act Statement: Your information will be used to support the transmittal of electronic payment data to your financial institution. Collection is authorized by 39 (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: accountspayablesuppliermaintenance@usps.gov (invoicing/AP) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-03 | page: https://about.usps.com/what/business-services/facilities-leasing-property-management/assets/pdf/supplier-EFT-enrollment-form.pdf | quote: "acting Officer Representative, Postmaster, or USPS contact. USPS Personnel: Send completed form via one of the following methods: By email: accountspayablesuppl" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Proofpoint | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-BIG-00009
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Proofpoint
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject; fo=1; ri=3600; rua=mailto:reports@dmarc.cyber.dhs.gov,mailto:dmarc_rua@emaildefense.proofpoint.com; ruf=mailto:dmarc_ruf@emaildefense.proofpoint.com
- **dmarc_record_domain**: usps.gov
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 ip4:56.0.84.0/24 ip4:56.0.103.0/24 ip4:56.0.143.0/24 ip4:56.0.146.0/24 ip4:56.0.86.0/24 include:spf.protection.outlook.com -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: USD (derived from the buyer's country; CAD if the parties agreed so)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: United States Postal Service (schema.org JSON-LD legalName on https://www.usps.com/) — L'Enfant Plaza; Washington, D.C. (Wikidata Q668687, official website on the organisation's domain (http://www.usps.gov/) + name; 2026-11-08) ⏎ SUBMIT TO: accountspayablesuppliermaintenance@usps.gov (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state  | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: United States Postal Service (government ministry / agency, CA) — inferred: no record; the organisation's type and province make a Canadian 
- **invoice_card_json**: {"bill_to": {"legal_name": "United States Postal Service (schema.org JSON-LD legalName on https://www.usps.com/)", "legal_name_is_published": true, "address": "L'Enfant Plaza; Washington, D.C. (Wikidata Q668687, official website on the organisation's domain (http://www.usps.gov/) + name; 2026-11-08)", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "accountspayablesuppliermaintenance@usps.gov", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "Electronic Funds Transfer (EFT) Enrol (as printed on https://about.usps.com/what/business-services/facilities-leasing-property-management/assets/pdf/supplier-EFT-enrollment-form.pdf, re-read 2026-11-08)", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state ", "buyer_tax_status_is_published": false, "indicative_rate": "", "currency": "DERIVED: USD (derived from the buyer's country; C", "currency_is_published": false, "vendor_gst_hst": 
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 73
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; payment cycle or method published (plausibility) | missing: finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact
- **ap_gap_to_A**: published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: inferred: Canada Post Corporation
- **vendor_address**: 2701 Riverside Drive, Ottawa ON K1A 0B1
- **vendor_country_basis**: the vendor's own site, https://www.canadapost-postescanada.ca/cpc/en/our-company/transparency-and-trust/privacy-centre/info-source/additional-information.page: 'Access to Information and Privacy Canada Post Corporation 2701 Riverside Drive, N1160 Ottawa ON K1A 0B1'
- **vendor_bn9**: 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)
- **vendor_gst_hst_derived**: 119321495RT0001 (GST/HST 119321495 (RT program; account suffix not printed); QST 1006393299)
- **vendor_website**: https://www.canadapost-postescanada.ca
- **vendor_phone**: 1-800-267-7651 (Credit Management Group (invoices and billing); https://www.canadapost-postescanada.ca/cpc/en/support/kb/billing/payments/what-address-should-i-send-payment-to)
- **vendor_contact_evidence_url**: https://www.canadapost-postescanada.ca/cpc/en/support/kb/billing/payments/what-address-should-i-send-payment-to
- **vendor_logo_url**: https://www.canadapost-postescanada.ca/cpc/assets/cpc/uploads/banners/personal/ccmopc-36907-secondary-hero-large.svg
- **vendor_facts_provenance**: name and address: the record's vendor block (inference from the buyer's type and province (no contract, payment or listing record)); BN9: printed on the organisation's own page (https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); phone / role e-mails / logo: the vendor's own site, https://www.canadapost-postescanada.ca/cpc/en/support/kb/billing/payments/what-address-should-i-send-payment-to (tools/org_contacts.py, org_extras.py); website: https://www.canadapost-postescanada.ca
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_bn_source**: printed on the organisation's own page (https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf)

## Contract
- **contract_status**: inferred relationship (no record): low confidence; the buyer is an organisation located in Canada; generic: Canada Post holds the exclusive privilege of collecting, transmitting and delivering letters within Canada (Canada Post Corporation Act, s. 14); most organisations mail some letters, but not every one does
- **source**: inference from the buyer's type and province (no contract, payment or listing record)
- **contracts_with_canadian_suppliers**: 0
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **invoice_currency_derived**: USD (derived from the buyer's country; CAD if the parties agreed so)
- **vendor_gst_hst_derived**: 119321495RT0001 (GST/HST 119321495 (RT program; account suffix not printed); QST 1006393299)

## Pay on sight / grades
- **pay_on_sight**: yes — reference rule not published (quote the buyer's PO / order number when one is issued)
- **pay_on_sight_missing**: (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: United States Postal Service (schema.org JSON-LD legalName on https://www.usps.com/) — L'Enfant Plaza; Washington, D.C. (Wikidata Q668687, official website on the organisation's domain (http://www.usps.gov/) + name; 2026-11-08) ⏎ SUBMIT TO: accountspayablesuppliermaintenance@usps.gov (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state  | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: United States Postal Service (government ministry / agency, CA) — inferred: no record; the organisation's type and province make a Canadian 
- **invoice_card_json**: {"bill_to": {"legal_name": "United States Postal Service (schema.org JSON-LD legalName on https://www.usps.com/)", "legal_name_is_published": true, "address": "L'Enfant Plaza; Washington, D.C. (Wikidata Q668687, official website on the organisation's domain (http://www.usps.gov/) + name; 2026-11-08)", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "accountspayablesuppliermaintenance@usps.gov", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "Electronic Funds Transfer (EFT) Enrol (as printed on https://about.usps.com/what/business-services/facilities-leasing-property-management/assets/pdf/supplier-EFT-enrollment-form.pdf, re-read 2026-11-08)", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state ", "buyer_tax_status_is_published": false, "indicative_rate": "", "currency": "DERIVED: USD (derived from the buyer's country; C", "currency_is_published": false, "vendor_gst_hst": 
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 73
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; payment cycle or method published (plausibility) | missing: finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact
- **ap_gap_to_A**: published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["accountspayablesuppliermaintenance@usps.gov (invoicing/AP)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-03", "page: https://about.usps.com/what/business-services/facilities-leasing-property-management/assets/pdf/supplier-EFT-enrollment-form.pdf", "quote: \"acting Officer Representative, Postmaster, or USPS contact. USPS Personnel: Send completed form via one of the following methods: By email: accountspayablesuppl\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Proofpoint", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-BIG-00009"], "buyer_facts": ["address and phone: the buyer's own site, https://www.usps.com/help/contact-us.htm (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (inference from the buyer's type and province (no contract, payment or listing record))", "BN9: printed on the organisation's own page (https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf)", "GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://about.usps.com/what/business-services/facilities-leasing-property-management/assets/pdf/supplier-EFT-enrollment-form.pdf | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, usps.gov)
- **status**: ok
- **pages**: 5
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_legal_name**: United States Postal Service
- **jsonld_alternate_name**: USPS
- **jsonld_logo**: https://www.usps.com/global-elements/header/images/utility-header/logo-sb.svg
- **jsonld_url**: https://www.usps.com/
- **jsonld_same_as**: https://www.facebook.com/USPS; https://twitter.com/usps; http://www.pinterest.com/uspsstamps/; https://www.youtube.com/usps
- **jsonld_quote**: [{"@context":"http://schema.org","@id":"https://www.usps.com/#organization","@type":"Organization","legalName":"United States Postal Service","alternateName":"USPS","url":"https://www.usps.com/","logo":"https://www.usps.com/global-elements/header/images/utility-header/logo-sb.svg","contactPoint":[{"
- **jsonld_page**: https://www.usps.com/
- **legal_name_stated**: European Union
- **legal_name_stated_url**: https://www.usps.com/
- **legal_name_stated_quote**: July 1, 2026, when you send a package with merchandise valued up to €150 to a country that follows European Union (EU) customs rules, new import duties and requirements may apply. Learn More --> New Requirements f
- **language**: en
- **logo_url**: https://www.usps.com/global-elements/images/logo_mobile.svg
- **logo_basis**: logo image in the site header
- **domain**: usps.gov
- **key**: wd:Q668687
- **name**: United States Postal Service
- **website**: https://usps.gov/
- **kind**: buyer
- **date**: 2026-11-08

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "phone": "1-800-222-1811", "phone_url": "https://www.usps.com/help/contact-us.htm", "domain": "usps.gov", "key": "wd:Q668687", "name": "United States Postal Service", "website": "https://usps.gov/", "kind": "buyer", "date": "2026-11-08"}

## Vendor site facts (org_extras, canadapost-postescanada.ca)
- **status**: ok
- **pages**: 1
- **language**: en
- **logo_url**: https://www.canadapost-postescanada.ca/cpc/assets/cpc/uploads/banners/personal/ccmopc-36907-secondary-hero-large.svg
- **logo_basis**: logo image on the site
- **domain**: canadapost-postescanada.ca
- **key**: b:2aa5e3d1f7b796f4
- **name**: Canada Post
- **website**: https://canadapost-postescanada.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2

## Vendor role mailboxes found on its site (org_contacts)
_not read_

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Canada Post | Q1032001 | official website on the organisation's domain (https://www.canadapost-postescanada.ca/) + name |  | Canada Post | Postes Canada | business; state-owned enterprise | business corporation | Canada | 1867-07-01 | Ottawa |
| b | United States Postal Service | Q668687 | official website on the organisation's domain (http://www.usps.gov/) + name |  | United States Postal Service | United States Postal Service | independent agency of the United States government; postal service; business |  | United States | 1971-07-01 | L'Enfant Plaza; Washington, D.C. |
| v | SOCIÉTÉ CANADIENNE DES POSTES | Q1032001 | official website on the organisation's domain (https://www.canadapost-postescanada.ca/) + name |  | Canada Post | Postes Canada | business; state-owned enterprise | business corporation | Canada | 1867-07-01 | Ottawa |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "wd:Q668687",
 "ap_contact_team": {
  "emails": [
   "accountspayablesuppliermaintenance@usps.gov"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "accountspayablesuppliermaintenance@usps.gov",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://about.usps.com/what/business-services/facilities-leasing-property-management/assets/pdf/supplier-EFT-enrollment-form.pdf",
    "quote": "acting Officer Representative, Postmaster, or USPS contact. USPS Personnel: Send completed form via one of the following methods: By email: accountspayablesuppliermaintenance@usps.gov By fax: (650) 577-4640 B. Supplier/Payee Information (Supplier/Payee completes.) Privacy Act Statement: Yo",
    "retrieved_date": "2026-11-03",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "United States Postal Service",
    "task_id": "CL-BIG-00009"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of www.usps.com (60 pages, robots.txt respected), no AI, no search engine"
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

- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
