# S5-49 — The Confluence Historic Site & Parkland ⇄ RSM Canada LLP

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 1 · AP grade C · missing: the vendor's GST/HST number (BN9); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: The Confluence Historic Site & Parkland (schema.org JSON-LD legalName on https://www.theconfluence.ca/) — 750 9th Ave SE Calgary Canada (schema.org JSON-LD PostalAddress on https://www.theconfluence.ca/)
SUBMIT TO: info@theconfluence.ca (general mailbox, confirmed by the referee) | invoice portal: Esker
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: RSM Canada LLP — 700-11 King St W, M5H 4C7, ON, M5H 4C7, Canada | GST/HST number not public | NEQ 3371139703
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: The Confluence Historic Site & Parkland (organisation (type not stated in the record), jurisdiction not stated) — public contract / purchase
```

## Relationship
- **rank_group**: B1
- **data_quality_score**: 56
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 1
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: The Confluence Historic Site & Parkland (organisation (type not stated in the record), jurisdiction not stated) — public contract / purchase award in the last 12 months (dated record): RSM Canada LLP | awarded 2026-04-09 | published by: auditor of record (own audited financial statements, auditor's report signed in Edmonton,  | record: https://static1.squarespace.com/static/66198f5a0583621cde5cfd1c/t/69deb2c01098af281abce180/1776202432715/2025+Audited+Financial+Statements.pdf | vendor in Canada because: auditor of record (own audited financial statements, auditor's report signed in Edmonton, Alberta)=signature block read from the page image (page 3, on-device OCR): RSM | THE POWER OF BEING UNDERSTOOD | ASSURANCE | TAX | | status rule: likely active (record dated in the last 12 months: auditor of record (own audited financial statements, auditor's report signed in Edmonton, )
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: lead:41f79961e054c34b
- **tier**: B
- **grade**: 1
- **records_with_this_vendor**: 1 (relationship record: auditor of record (own audited financial statements, auditor's report signed in Edmonton, ; 0 in the contract dataset)

## Buyer
- **buyer**: The Confluence Historic Site & Parkland
- **buyer_website**: https://theconfluence.ca/
- **buyer_address**: 750 9th Ave SE Calgary Canada (schema.org JSON-LD PostalAddress on https://www.theconfluence.ca/)
- **buyer_phone**: 403-537-7275
- **buyer_contact_evidence_url**: https://www.theconfluence.ca/contact
- **buyer_legal_name_as_published**: The Confluence Historic Site & Parkland (schema.org JSON-LD legalName on https://www.theconfluence.ca/)
- **buyer_logo_url**: https://images.squarespace-cdn.com/content/v1/66198f5a0583621cde5cfd1c/02a78bf5-8af8-49ae-bf2d-bd5053d0af1f/TheConfluence__Horizontal+nocturne+blkft.png?format=1500w
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://ca.linkedin.com/company/the-confluence-yyc
- **buyer_type**: organisation (type not stated in the record)
- **buyer_sector**: not stated
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.theconfluence.ca/contact (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_esignature_preference**: Docusign Envelope ID: 3E1E806E-18E3-4315-8DFD-CC09274ECF2E The Confluence Historic Site (as printed on https://static1.squarespace.com/static/66198f5a0583621cde5cfd1c/t/69deb2c01098af281abce180/1776202432715/2025+Audited+Financial+Statements.pdf, re-read 2026-11-08)
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: info@theconfluence.ca
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://www.theconfluence.ca/summercamps
- **email_evidence_quote**: ript type="application/ld+json">{"legalName":"The Confluence Historic Site & Parkland","address":"750 9th Ave SE\nCalgary\nCanada","email":"info@theconfluence.ca","telephone":"","sameAs":["https://www.instagram.com/theconfluence_yyc","https://www.threads.net/@theconfluence_yyc","https://ww
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: info@theconfluence.ca (general) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08 | page: https://www.theconfluence.ca/summercamps | quote: "ript type="application/ld+json">{"legalName":"The Confluence Historic Site & Parkland","address":"750 9th Ave SE\nCalgary\nCanada","email":"info@theconfluence.c" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00221
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1; p=quarantine; sp=quarantine; pct=100; rua=mailto:dmarc-admin@theconfluence.ca; ruf=mailto:dmarc-admin@theconfluence.ca; rf=afrf; fo=0:1:d:s; ri=86400; adkim=s; aspf=s
- **dmarc_record_domain**: theconfluence.ca
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 include:spf.protection.outlook.com -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoice_portal_url**: Esker
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **ap_system_hint**: named on the buyer's page: Esker
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "portal_url": "Esker", "portal_kind": "actionable supplier / invoice portal named by the buyer"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: The Confluence Historic Site & Parkland (schema.org JSON-LD legalName on https://www.theconfluence.ca/) — 750 9th Ave SE Calgary Canada (schema.org JSON-LD PostalAddress on https://www.theconfluence.ca/) ⏎ SUBMIT TO: info@theconfluence.ca (general mailbox, confirmed by the referee) | invoice portal: Esker ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: RSM Canada LLP — 700-11 King St W, M5H 4C7, ON, M5H 4C7, Canada | GST/HST number not public | NEQ 3371139703 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: The Confluence Historic Site & Parkland (organisation (type not stated in the record), jurisdiction not stated) — public contract / purchase
- **invoice_card_json**: {"bill_to": {"legal_name": "The Confluence Historic Site & Parkland (schema.org JSON-LD legalName on https://www.theconfluence.ca/)", "legal_name_is_published": true, "address": "750 9th Ave SE Calgary Canada (schema.org JSON-LD PostalAddress on https://www.theconfluence.ca/)", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "info@theconfluence.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "Esker", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: Esker", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": "Docusign Envelope ID: 3E1E806E-18E3-4315-8DFD-CC09274ECF2E The Confluence Historic Site (as printed on https://static1.squarespace.com/static/66198f5a0583621cde5cfd1c/t/69deb2c01098af281abce180/1776202432715/2025+Audited+Financial+Statements.pdf, re-read 2026-11-08)"}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: RSM Canada LLP
- **vendor_legal_name**: RSM Canada LLP
- **vendor_trading_name**: COLLINS BARROW TORONTO LLP; SERVICES COMPTABLES COLLINS BARROW TORONTO; SERVICES COMPTABLES RSM CANADA (other names in the registry)
- **vendor_registry_id**: Québec REQ (NEQ): 3371139703
- **vendor_registry_url**: https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises
- **vendor_registered_address**: 700-11 King Street West, Toronto (Ontario), M5H4C7
- **vendor_neq**: 3371139703 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_legal_form**: Société non constituée au Québec
- **vendor_activity_code**: CAE 7731 — -
- **vendor_employees_quebec**: De 1 à 5
- **vendor_last_annual_filing**: REQ annual declaration 2026
- **vendor_address**: 700-11 King St W, M5H 4C7, ON, M5H 4C7, Canada
- **vendor_country_basis**: auditor of record (own audited financial statements, auditor's report signed in Edmonton, Alberta)=signature block read from the page image (page 3, on-device OCR): RSM | THE POWER OF BEING UNDERSTOOD | ASSURANCE | TAX | CONSULTING | RSM Canada LLP is a limited liability partnership that provides public accounting services and is the Canadian member firm of RSM International, a… ... text layer:…
- **vendor_website**: https://www.rsmcanada.com/
- **vendor_logo_url**: about:error
- **vendor_linkedin_url**: https://www.linkedin.com/company/rsmcanada
- **vendor_facts_provenance**: name and address: the record's vendor block (auditor of record (own audited financial statements, auditor's report signed in Edmonton, ); registry identity: Québec REQ (NEQ): 3371139703 status Québec REQ (NEQ): Immatriculée (2015-08-03); BC OrgBook (BC registration): Active (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); incorporated / registered: 2008-07-15; website: https://www.rsmcanada.com/; NEQ: 3371139703 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Québec REQ (NEQ): Immatriculée (2015-08-03); BC OrgBook (BC registration): Active
- **vendor_incorporation_date**: 2008-07-15
- **vendor_years_in_business**: 18.3 (since 2008-07-15, registry date)

## Contract
- **contract_status**: likely active (record dated in the last 12 months: auditor of record (own audited financial statements, auditor's report signed in Edmonton, )
- **award_date**: 2026-04-09
- **contract_link**: https://static1.squarespace.com/static/66198f5a0583621cde5cfd1c/t/69deb2c01098af281abce180/1776202432715/2025+Audited+Financial+Statements.pdf
- **source**: auditor of record (own audited financial statements, auditor's report signed in Edmonton, 
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: auditor of record (own audited financial statements, auditor's report signed in Edmonton, ; 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (AB) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: The Confluence Historic Site & Parkland (schema.org JSON-LD legalName on https://www.theconfluence.ca/) — 750 9th Ave SE Calgary Canada (schema.org JSON-LD PostalAddress on https://www.theconfluence.ca/) ⏎ SUBMIT TO: info@theconfluence.ca (general mailbox, confirmed by the referee) | invoice portal: Esker ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: RSM Canada LLP — 700-11 King St W, M5H 4C7, ON, M5H 4C7, Canada | GST/HST number not public | NEQ 3371139703 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: The Confluence Historic Site & Parkland (organisation (type not stated in the record), jurisdiction not stated) — public contract / purchase
- **invoice_card_json**: {"bill_to": {"legal_name": "The Confluence Historic Site & Parkland (schema.org JSON-LD legalName on https://www.theconfluence.ca/)", "legal_name_is_published": true, "address": "750 9th Ave SE Calgary Canada (schema.org JSON-LD PostalAddress on https://www.theconfluence.ca/)", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "info@theconfluence.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "Esker", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: Esker", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": "Docusign Envelope ID: 3E1E806E-18E3-4315-8DFD-CC09274ECF2E The Confluence Historic Site (as printed on https://static1.squarespace.com/static/66198f5a0583621cde5cfd1c/t/69deb2c01098af281abce180/1776202432715/2025+Audited+Financial+Statements.pdf, re-read 2026-11-08)"}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["info@theconfluence.ca (general)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08", "page: https://www.theconfluence.ca/summercamps", "quote: \"ript type=\"application/ld+json\">{\"legalName\":\"The Confluence Historic Site & Parkland\",\"address\":\"750 9th Ave SE\\nCalgary\\nCanada\",\"email\":\"info@theconfluence.c\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00221"], "buyer_facts": ["address and phone: the buyer's own site, https://www.theconfluence.ca/contact (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (auditor of record (own audited financial statements, auditor's report signed in Edmonton, )", "registry identity: Québec REQ (NEQ): 3371139703 status Québec REQ (NEQ): Immatriculée (2015-08-03)", "BC OrgBook (BC registration): Active (scripts/enrichment_*: Corporations Canad

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.theconfluence.ca/ | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, theconfluence.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://images.squarespace-cdn.com/content/v1/66198f5a0583621cde5cfd1c/02a78bf5-8af8-49ae-bf2d-bd5053d0af1f/TheConfluence__Horizontal+nocturne+blkft.png?format=1500w
- **logo_basis**: logo image on the site
- **domain**: theconfluence.ca
- **key**: lead:41f79961e054c34b
- **name**: The Confluence Historic Site & Parkland
- **website**: https://theconfluence.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_legal_name**: The Confluence Historic Site & Parkland
- **jsonld_address**: 750 9th Ave SE Calgary Canada
- **jsonld_email**: info@theconfluence.ca
- **jsonld_same_as**: https://www.instagram.com/theconfluence_yyc; https://www.threads.net/@theconfluence_yyc; https://www.facebook.com/theconfluencehistoricsite; https://ca.linkedin.com/company/the-confluence-yyc
- **jsonld_quote**: {"address":"750 9th Ave SE\nCalgary\nCanada","image":"https://static1.squarespace.com/static/66198f5a0583621cde5cfd1c/t/669ecf1d7691935dc58f3223/1794115442598/","name":"The Confluence Historic Site & Parkland","openingHours":", Th 11:00-16:00, Fr 11:00-16:00, Sa 11:00-16:00, Su 11:00-16:00","@contex
- **jsonld_page**: https://www.theconfluence.ca/
- **legal_name_stated**: Canadian Pacific Railway
- **legal_name_stated_url**: https://www.theconfluence.ca/about-the-confluence
- **legal_name_stated_quote**: ange over time, evolving as the site itself has evolved, and impact how we live today. In 1883, the Canadian Pacific Railway (CPR) arrived at this site and brought with it a new settler population from Eastern Canada. The NW
- **mentions**: {'payment_method': {'text': 'interactive, engaging and curriculum-connected field trip where the Bow and Elbow river', 'url': 'https://www.theconfluence.ca/', 'quote': 'g field trip programs for Jr. High classes ! Spots fill up fast, so book your class in today for an interactive, engaging and curriculum-connected field trip where the Bow and Elbow rivers meet, a significant place to reflect on history and learn about the peo'}}
- **linkedin_url**: https://ca.linkedin.com/company/the-confluence-yyc

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "750 9th Ave SE Calgary Canada", "address_country": "", "address_url": "https://www.theconfluence.ca/contact", "address_method": "json-ld", "address_quote": "JSON-LD PostalAddress on the page: 750 9th Ave SE Calgary Canada", "emails": "info@theconfluence.ca", "emails_url": "https://www.theconfluence.ca/contact", "phone": "403-537-7275", "phone_url": "https://www.theconfluence.ca/visit", "domain": "theconfluence.ca", "key": "osm:w181683459", "name": "The Confluence Historic Site & Parkland", "website": "https://theconfluence.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, rsmcanada.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: about:error
- **logo_basis**: og:image of the home page
- **domain**: rsmcanada.com
- **key**: vendor:RSM Canada LLP
- **name**: RSM Canada LLP
- **website**: https://rsmcanada.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: RSM Canada | Experience the power of being understood
- **jsonld_logo**: https://publish-p194552-e2014559.adobeaemcloud.com/content/dam/rsm/utility/logo.png
- **jsonld_url**: https://www.rsmcanada.com
- **jsonld_same_as**: https://www.linkedin.com/company/rsmcanada; https://x.com/RSM_Canada; https://www.facebook.com/RSMCanada1
- **jsonld_quote**: { "@context": "https://schema.org", "@type": "Organization", "name": "RSM Canada | Experience the power of being understood", "url": "https://www.rsmcanada.com", "logo": "https://publish-p194552-e2014559.adobeaemcloud.com/content/dam/rsm/utility/logo.png", "description": "RSM Canada empowers middle 
- **jsonld_page**: https://www.rsmcanada.com/
- **legal_name_stated**: City of Kelowna
- **legal_name_stated_url**: https://www.rsmcanada.com/about/innovation
- **legal_name_stated_quote**: arget Same Tab Microsoft case study AI and automation elevate productivity and service delivery for City of Kelowna Read the case study "Without a strategic plan and a governance framework that operationalizes that
- **linkedin_url**: https://www.linkedin.com/company/rsmcanada

## Vendor role mailboxes found on its site (org_contacts)
_not read_

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | The Confluence Historic Site & Parkland |  |  |  |  |  |  |  |  |  |  |
| v | RSM Canada LLP |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:41f79961e054c34b",
 "ap_contact_team": {
  "emails": [
   "info@theconfluence.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "info@theconfluence.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.theconfluence.ca/",
    "quote": "ript type=\"application/ld+json\">{\"legalName\":\"The Confluence Historic Site & Parkland\",\"address\":\"750 9th Ave SE\\nCalgary\\nCanada\",\"email\":\"info@theconfluence.ca\",\"telephone\":\"\",\"sameAs\":[\"https://www.instagram.com/theconfluence_yyc\",\"https://www.threads.net/@theconfluence_yyc\",\"https://ww",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "The Confluence Historic Site & Parkland",
    "task_id": "CL-LD-45680"
   },
   {
    "email": "info@theconfluence.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.theconfluence.ca/summercamps",
    "quote": "ript type=\"application/ld+json\">{\"legalName\":\"The Confluence Historic Site & Parkland\",\"address\":\"750 9th Ave SE\\nCalgary\\nCanada\",\"email\":\"info@theconfluence.ca\",\"telephone\":\"\",\"sameAs\":[\"https://www.instagram.com/theconfluence_yyc\",\"https://www.threads.net/@theconfluence_yyc\",\"https://ww",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "The Confluence Historic Site & Parkland",
    "task_id": "CL-WS-00221"
   }
  ]
 },
 "research_status": {
  "found": 2
 },
 "queries_tried": [
  "site crawl of theconfluence.ca (21 pages, robots.txt respected), no AI, no search engine",
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

## The vendor's other buyers in the dataset (first 60 of 23)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_alberta_apc:AB-2024-09563:7c7ac64d-8d72-4888-a231-6f6071a36bfe | Public Safety and Emergency Services | Public Safety and Emergency Services - Request for Proposal - AEMA Actuary Services | 360000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2024-09563 |
| ca_alberta_apc:AB-2025-00268:6e2310b3-b457-4780-b860-d53ed4452451 | Sturgeon County | Sturgeon County - Request for Proposal - IT Planning & Delivery Services - Non-Mandatory Preferred Supplier |  |  |  | https://purchasing.alberta.ca/posting/AB-2025-00268 |
| ca_alberta_apc:AB-2025-04315:dcddaacb-9799-4a16-98e2-e8df9977d114 | Municipal Affairs | Municipal Affairs - Request for Proposal - AUDIT OF THE CANADA COMMUNITY-BUILDING FUND FINANCIAL REPORT | 75500.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-04315 |
| ca_bidsandtenders:7c8e07c9-0933-472b-9832-d22f31714ddd:1 | City of Lethbridge | Actuarial Review of the Insurance Reserve & Risk Financing Strategy | 34975.0 |  |  | https://lethbridge.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/7c8e07c9-0933-472b-9832-d22f31714ddd |
| ca_bidsandtenders:330eed5e-ddfc-4416-978c-cc22d1f3c662:1 | City of Vaughan | Actuarial Services for Determining Post-Employment Benefits Liability, WSIB Schedule 2 Claims Liability and Non-Vested Sick Leave Liability | 43800.0 |  |  | https://vaughan.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/330eed5e-ddfc-4416-978c-cc22d1f3c662 |
| ca_bidsandtenders:4d9fdcc5-1f68-4313-aec1-60765dc14a4d:1 | City of Mississauga | Actuarial Benefit Review Services |  |  |  | https://mississauga.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/4d9fdcc5-1f68-4313-aec1-60765dc14a4d |
| ca_bidsandtenders:e4e8d633-c0b9-4757-a280-7491b6b1d8fb:1 | Region of Waterloo | Child Care Centre Audits |  |  |  | https://regionofwaterloo.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/e4e8d633-c0b9-4757-a280-7491b6b1d8fb |
| ca_bidsandtenders:f256242f-1cdd-41fa-9527-ca7e511a0d75:3 | Region of Peel | Direct Engagement and Third-Party Funding Review (Compliance Audits) for Early Years and Child Care |  |  |  | https://peelregion.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/f256242f-1cdd-41fa-9527-ca7e511a0d75 |
| ca_bidsandtenders:75418a7f-d93b-4334-a37e-384200c9a734:3 | City of Burnaby | Pre-Qualification of QSA Services |  |  |  | https://burnaby.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/75418a7f-d93b-4334-a37e-384200c9a734 |
| ca_bidsandtenders:bc74edf4-4e7b-4fbd-9f61-aeb5616727f8:8 | City of Burnaby | Pre-Qualification for IT Consulting Services for ServiceNow & Microsoft 365 |  |  |  | https://burnaby.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/bc74edf4-4e7b-4fbd-9f61-aeb5616727f8 |
| ca_bidsandtenders:4f8bcf1e-c53e-4ffe-8f24-eebb9339e297:1 | Sturgeon County | IT Planning & Delivery Services - Non-Mandatory Preferred Supplier |  |  |  | https://sturgeoncounty.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/4f8bcf1e-c53e-4ffe-8f24-eebb9339e297 |
| ca_bidsandtenders:c0c2062f-dcaa-469c-9cfc-f5fbd91ec492:1 | City of Brantford | Provision of Actuarial Services | 20000.0 |  |  | https://brantford.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/c0c2062f-dcaa-469c-9cfc-f5fbd91ec492 |
| ca_bidsandtenders:4e06187c-e699-46b0-88c1-ceff421e6e29:1 | Norfolk County | Actuarial Review of Self-Insurance Reserve Fund |  |  |  | https://norfolk.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/4e06187c-e699-46b0-88c1-ceff421e6e29 |
| ca_bidsandtenders:90a8ee8c-4e94-4e4d-8213-1cd295951986:1 | Norfolk County | Actuarial Valuation Services | 11600.0 |  |  | https://norfolk.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/90a8ee8c-4e94-4e4d-8213-1cd295951986 |
| ca_bidsandtenders:02ef1f89-f2f0-4f57-a4e0-11a1214fa910:1 | City of Barrie | Actuarial Services | 145000.0 |  |  | https://barrie.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/02ef1f89-f2f0-4f57-a4e0-11a1214fa910 |
| ca_bidsandtenders:1d2f7b25-c663-477a-98b1-100618036188:1 | City of Vaughan | Actuarial Services |  |  |  | https://vaughan.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/1d2f7b25-c663-477a-98b1-100618036188 |
| ca_bidsandtenders:bce128fc-53f4-4336-b982-cb37e57869ba:2 | City of Mississauga | Internal Auditing Services for a 5 year period ( Roster) | 30000.0 |  |  | https://mississauga.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/bce128fc-53f4-4336-b982-cb37e57869ba |
| ca_bidsandtenders:e185ba2b-1bd7-466a-ac09-e4a88ddc78da:14 | City of Guelph | Pre-qualification of IT Professional Services for Various Technology Projects | 1.0 |  |  | https://guelph.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/e185ba2b-1bd7-466a-ac09-e4a88ddc78da |
| ca_merx:3915967117:1 | Export Development Canada - EDC | CyberArk Privilege Cloud | 2748437.35 |  |  | https://www.merx.com/exportdevelopmentcanadaedc/solicitations/CyberArk-Privilege-Cloud/0000320035?origin=0 |
| ca_merx:2854039313:1 | Manitoba Public Insurance | Request for Proposal #3245 Actuarial Consulting Services - Peer Review | 40000.0 |  |  | https://www.merx.com/mbgov/mpi/solicitations/Request-for-Proposal-3245-Actuarial-Consulting-Services-Peer-Review/0000267261?origin=0 |
| ca_merx:2056045638:16 | Greater Toronto Airports Authority | General Consulting Services |  |  |  | https://www.merx.com/torontopearson/solicitations/General-Consulting-Services/0000214400?origin=0 |
| canada_federal:hc-sc:4600002854 | Health Canada | Accounting and audit services | 142887.25 |  |  | https://search.open.canada.ca/contracts/record/hc-sc,C-2026-2027-Q1-00338 |
| canada_federal:cb:MX-444045159383 | Export Development Canada - EDC | CyberArk Privilege Cloud | 2748437.35 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/mx-444045159383 |

## Open questions for hand research (layer 2)

- the vendor's GST/HST number (BN9)
- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
