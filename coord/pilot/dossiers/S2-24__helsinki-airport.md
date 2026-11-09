# S2-24 — Helsinki Airport ⇄ Airports Council International (ACI World)

Stratum: **S2_complete_no_published_PO_rule** · pay on sight: yes — reference rule not published (quote the buyer's PO / order number when one is issued) · channel tier 1 · AP grade C · missing: (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Helsinki Airport (label per Wikidata Q215327, official website on the organisation's domain (https://www.finavia.fi/en/airports/helsinki-airport) + name; 2026-11-08) — Lentäjäntie 3, Vantaa, Uusimaa, 01530, Finland (schema.org JSON-LD PostalAddress on https://www.finavia.fi/fi)
SUBMIT TO: airtrafficinvoices@finavia.fi (invoicing/AP mailbox, confirmed by the referee) | invoice portal: Basware
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: AIRPORTS COUNCIL INTERNATIONAL — MONTREAL-QUEBEC H4Z 1G8, 99999, CA | GST/HST 846678316RT0001 (account derived from the BN9) | NEQ 3363038947
TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is | CURRENCY: DERIVED: EUR (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Europe | 15 to 25 million passengers per year
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 88
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 1
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Helsinki Airport (transport / transit authority, jurisdiction not stated) — public contract / purchase award in the last 12 months (dated record): Airports Council International (ACI World) | subject: Europe | 15 to 25 million passengers per year | awarded 2025-12-31 | published by: paid programme participant named by the Canada-HQ provider (ACI World ASQ 2025) | record: https://aci.aero/programs-and-services/asq/asq-customer-experience-awards/ | vendor in Canada because: paid programme participant named by the Canada-HQ provider (ACI World ASQ 2025)=1500-800 rue du Square Victoria Montréal, Québec H3C 0B4 Canada | status rule: likely active (record dated in the last 12 months: paid programme participant named by the Canada-HQ provider (ACI World ASQ 2025))
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: lead:55296ea7815e00b5
- **tier**: B
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: paid programme participant named by the Canada-HQ provider (ACI World ASQ 2025); 0 in the contract dataset)

## Buyer
- **buyer**: Helsinki Airport
- **buyer_website**: https://www.finavia.fi/
- **buyer_address**: Lentäjäntie 3, Vantaa, Uusimaa, 01530, Finland (schema.org JSON-LD PostalAddress on https://www.finavia.fi/fi)
- **buyer_phone**: +358 20 708 000
- **buyer_contact_evidence_url**: https://www.finavia.fi/fi
- **buyer_legal_name_as_published**: Helsinki Airport (label per Wikidata Q215327, official website on the organisation's domain (https://www.finavia.fi/en/airports/helsinki-airport) + name; 2026-11-08)
- **buyer_logo_url**: https://www.finavia.fi/themes/custom/finavia/crop_180x180px.png
- **buyer_website_status**: site answers
- **buyer_type**: transport / transit authority
- **buyer_sector**: transport / transit
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q215327; international airport; airport; commercial traffic aerodrome
- **buyer_founded**: 1952-00-00 (Wikidata Q215327, official website on the organisation's domain (https://www.finavia.fi/en/airports/helsinki-airport) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.finavia.fi/fi (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is accounted for by the buyer under the reverse charge where applicable
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: airtrafficinvoices@finavia.fi
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.finavia.fi/sites/default/files/documents/Finavia_Terms_of_Services_01.01.2025.pdf
- **email_evidence_quote**: used in Finland for at least 50 years and that have a clear historical significance. The aircraft must be reported as a vintage aircraft to airtrafficinvoices@finavia.fi before operations in order for this exemption to apply. Exemptions 3, 4, and 5 do not apply at Helsinki Airport. Exempti
- **mailbox_provenance**: airtrafficinvoices@finavia.fi (invoicing/AP) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08 | page: https://www.finavia.fi/sites/default/files/documents/Finavia_Terms_of_Services_01.01.2025.pdf | quote: "used in Finland for at least 50 years and that have a clear historical significance. The aircraft must be reported as a vintage aircraft to airtrafficinvoices@f" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00407
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject; pct=100; rua=mailto:dmarc-rua@finavia.fi; ruf=mailto:dmarc-ruf@finavia.fi
- **dmarc_record_domain**: finavia.fi
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 ip4:95.214.64.0/22 ip4:149.96.13.2 ip4:149.96.14.2 ip4:149.96.3.26 ip4:149.96.4.26 ip4:199.91.136.26 ip4:199.91.136.28 ip4:199.91.137.26 ip4:199.91.140.26 ip4:199.91.140.28 ip4:37.98.232.12 ip4:81.22.169.250 ip4:81.22.169.251 ip4:37.98.232.26 ip4:37.98.234.2 ip4:37.98.235.2 ip4:95.175.113.181
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoice_portal_url**: Basware
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **ap_system_hint**: named on the buyer's page: Basware
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "portal_url": "Basware", "portal_kind": "actionable supplier / invoice portal named by the buyer"}
- **invoice_currency_derived**: EUR (derived from the buyer's country; CAD if the parties agreed so)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Helsinki Airport (label per Wikidata Q215327, official website on the organisation's domain (https://www.finavia.fi/en/airports/helsinki-airport) + name; 2026-11-08) — Lentäjäntie 3, Vantaa, Uusimaa, 01530, Finland (schema.org JSON-LD PostalAddress on https://www.finavia.fi/fi) ⏎ SUBMIT TO: airtrafficinvoices@finavia.fi (invoicing/AP mailbox, confirmed by the referee) | invoice portal: Basware ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: AIRPORTS COUNCIL INTERNATIONAL — MONTREAL-QUEBEC H4Z 1G8, 99999, CA | GST/HST 846678316RT0001 (account derived from the BN9) | NEQ 3363038947 ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is | CURRENCY: DERIVED: EUR (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Europe | 15 to 25 million passengers per year
- **invoice_card_json**: {"bill_to": {"legal_name": "Helsinki Airport (label per Wikidata Q215327, official website on the organisation's domain (https://www.finavia.fi/en/airports/helsinki-airport) + name; 2026-11-08)", "legal_name_is_published": true, "address": "Lentäjäntie 3, Vantaa, Uusimaa, 01530, Finland (schema.org JSON-LD PostalAddress on https://www.finavia.fi/fi)", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "airtrafficinvoices@finavia.fi", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "Basware", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: Basware", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is", "buyer_tax_status_is_published": false, "indicative_rate": "", "currency": "DERIVED: EUR (derived from the buyer's country; C", "currency_is_published": false, "vendor_gst_hst": "846678316RT0001", "vendor_qst": ""}, "vendor_identi
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 71
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: Airports Council International (ACI World)
- **vendor_legal_name**: AIRPORTS COUNCIL INTERNATIONAL
- **vendor_trading_name**: Airports Council International (ACI World)
- **vendor_registry_id**: Corporations Canada (corporation number): 7598637
- **vendor_registry_url**: https://ised-isde.canada.ca/cc/lgcy/fdrlCrpDtls.html?corpId=7598637
- **vendor_registered_address**: 800 rue du Square Victoria, Suite 1500, Montreal, QC, H3C 0B4, CA
- **vendor_neq**: 3363038947 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_legal_form**: Association
- **vendor_activity_code**: CAE 4521 — ADVANCE THE INTERESTS OF AIRPORTS PROMOTE PROFESSIONAL EXCELLENCE IN AIRPORT MANAGEMENT AND OPERATIONS
- **vendor_employees_quebec**: De 26 à 49
- **vendor_directors_range**: 3 to 29 directors (Corporations Canada)
- **vendor_last_annual_filing**: REQ annual declaration 2012; Corporations Canada anniversary 2014-10-15
- **vendor_address**: MONTREAL-QUEBEC H4Z 1G8, 99999, CA
- **vendor_country_basis**: paid programme participant named by the Canada-HQ provider (ACI World ASQ 2025)=1500-800 rue du Square Victoria Montréal, Québec H3C 0B4 Canada
- **vendor_bn9**: 846678316
- **vendor_gst_hst_derived**: 846678316RT0001
- **vendor_website**: https://aci.aero/
- **vendor_phone**: +1 514 373 1200
- **vendor_contact_evidence_url**: https://aci.aero/
- **vendor_logo_url**: https://aci.aero/wp-content/uploads/2026/03/Logo_Mainwebsite.svg
- **vendor_peppol_id**: iso6523-actorid-upis 0195:cauid846678316 (Peppol Directory, registered 2021-12-19; https://directory.peppol.eu/public/locale-en_US/menuitem-search?q=0195%3Acauid846678316)
- **vendor_facts_provenance**: name and address: the record's vendor block (paid programme participant named by the Canada-HQ provider (ACI World ASQ 2025)); registry identity: Corporations Canada (corporation number): 7598637 status Corporations Canada (corporation number): Active; Québec REQ (NEQ): Radiée sur demande (2012-12-10) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: registry match; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2005-06-08; phone / role e-mails / logo: the vendor's own site, https://aci.aero/ (tools/org_contacts.py, org_extras.py); website: https://aci.aero/; NEQ: 3363038947 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Corporations Canada (corporation number): Active; Québec REQ (NEQ): Radiée sur demande (2012-12-10)
- **vendor_registry_note**: another registry lists a lapsed registration (Québec REQ (NEQ): Radiée sur demande (2012-12-10)); the primary record is alive
- **vendor_incorporation_date**: 2005-06-08
- **vendor_years_in_business**: 21.4 (since 2005-06-08, registry date)
- **vendor_wikidata**: https://www.wikidata.org/wiki/Q409068; organization
- **vendor_founded**: 1970-00-00 (Wikidata Q409068, exact name match + country + organisation claims; 2026-11-08)

## Contract
- **contract_status**: likely active (record dated in the last 12 months: paid programme participant named by the Canada-HQ provider (ACI World ASQ 2025))
- **contract_title**: Europe | 15 to 25 million passengers per year
- **contract_description**: Europe | 15 to 25 million passengers per year (the record's title; the source publishes no separate description)
- **award_date**: 2025-12-31
- **contract_link**: https://aci.aero/programs-and-services/asq/asq-customer-experience-awards/
- **source**: paid programme participant named by the Canada-HQ provider (ACI World ASQ 2025)
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: paid programme participant named by the Canada-HQ provider (ACI World ASQ 2025); 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is accounted for by the buyer under the reverse charge where applicable
- **invoice_currency_derived**: EUR (derived from the buyer's country; CAD if the parties agreed so)
- **vendor_gst_hst_derived**: 846678316RT0001

## Pay on sight / grades
- **pay_on_sight**: yes — reference rule not published (quote the buyer's PO / order number when one is issued)
- **pay_on_sight_missing**: (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Helsinki Airport (label per Wikidata Q215327, official website on the organisation's domain (https://www.finavia.fi/en/airports/helsinki-airport) + name; 2026-11-08) — Lentäjäntie 3, Vantaa, Uusimaa, 01530, Finland (schema.org JSON-LD PostalAddress on https://www.finavia.fi/fi) ⏎ SUBMIT TO: airtrafficinvoices@finavia.fi (invoicing/AP mailbox, confirmed by the referee) | invoice portal: Basware ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: AIRPORTS COUNCIL INTERNATIONAL — MONTREAL-QUEBEC H4Z 1G8, 99999, CA | GST/HST 846678316RT0001 (account derived from the BN9) | NEQ 3363038947 ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is | CURRENCY: DERIVED: EUR (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Europe | 15 to 25 million passengers per year
- **invoice_card_json**: {"bill_to": {"legal_name": "Helsinki Airport (label per Wikidata Q215327, official website on the organisation's domain (https://www.finavia.fi/en/airports/helsinki-airport) + name; 2026-11-08)", "legal_name_is_published": true, "address": "Lentäjäntie 3, Vantaa, Uusimaa, 01530, Finland (schema.org JSON-LD PostalAddress on https://www.finavia.fi/fi)", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "airtrafficinvoices@finavia.fi", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "Basware", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: Basware", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is", "buyer_tax_status_is_published": false, "indicative_rate": "", "currency": "DERIVED: EUR (derived from the buyer's country; C", "currency_is_published": false, "vendor_gst_hst": "846678316RT0001", "vendor_qst": ""}, "vendor_identi
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 71
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["airtrafficinvoices@finavia.fi (invoicing/AP)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08", "page: https://www.finavia.fi/sites/default/files/documents/Finavia_Terms_of_Services_01.01.2025.pdf", "quote: \"used in Finland for at least 50 years and that have a clear historical significance. The aircraft must be reported as a vintage aircraft to airtrafficinvoices@f\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00407"], "buyer_facts": ["address and phone: the buyer's own site, https://www.finavia.fi/fi (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (paid programme participant named by the Canada-HQ provider (ACI World ASQ 2025))", "registry identity: Corporations Canada (corporation number): 7598637 status Corporations Canada (corporation number): Active", "Québec REQ (NEQ): Radiée su

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.finavia.fi/sites/default/files/documents/SupplierLetter_1.pdf | 2026-11-08 | ok |  |  | Basware |  |  |  |  |  |  |

## Buyer site facts (org_extras, finavia.fi)
- **status**: ok
- **pages**: 1
- **language**: fi
- **domain**: finavia.fi
- **key**: lead:55296ea7815e00b5
- **name**: Helsinki Airport
- **website**: https://finavia.fi/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Finavia
- **jsonld_address**: Lentäjäntie 3, Vantaa, Uusimaa, 01530, Finland
- **jsonld_phone**: +358 20 708 000
- **jsonld_logo**: https://www.finavia.fi/themes/custom/finavia/logo.png
- **jsonld_url**: https://www.finavia.fi/fi
- **jsonld_quote**: { "@context": "https://schema.org", "@graph": [ { "@type": "Organization", "@id": "https://www.finavia.fi/fi/etusivu", "name": "Finavia", "url": "https://www.finavia.fi/fi", "telephone": "+358 20 708 000", "image": { "@type": "ImageObject", "url": "https://www.finavia.fi/sites/default/files/styles/h
- **jsonld_page**: https://www.finavia.fi/fi
- **logo_url**: https://www.finavia.fi/themes/custom/finavia/crop_180x180px.png
- **logo_basis**: site icon (apple-touch-icon)

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 1, "address": "Lentäjäntie 3, Vantaa, Uusimaa, 01530", "address_country": "Finland", "address_url": "https://www.finavia.fi/fi", "address_method": "json-ld", "address_quote": "JSON-LD PostalAddress on the page: Lentäjäntie 3, Vantaa, Uusimaa, 01530", "phone": "+358 20 708 000", "phone_url": "https://www.finavia.fi/fi", "domain": "finavia.fi", "key": "lead:55296ea7815e00b5", "name": "Helsinki Airport", "website": "https://finavia.fi/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, aci.aero)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://aci.aero/wp-content/uploads/2026/03/Logo_Mainwebsite.svg
- **logo_basis**: logo image in the site header
- **domain**: aci.aero
- **key**: vendor:Airports Council International (ACI)
- **name**: Airports Council International (ACI)
- **website**: https://aci.aero/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Airports Council International
- **legal_name_stated_url**: https://aci.aero/about-aci/
- **legal_name_stated_quote**: t the collective interest of airports. See more Follow us on Home - About ACI World About ACI World Airports Council International (ACI) World is the voice of the world’s airports. ACI World is part of the ACI Federation . In repr
- **mentions**: {'payment_method': {'text': 'interact with travellers with disabilities or special needs', 'url': 'https://aci.aero/airport-advocacy/airport-and-passenger-facilitation/accessibility/', 'quote': 'facing staff at airports with the skills they need to more confidently and effectively approach and interact with travellers with disabilities or special needs. Learn more about this course Accessibility Publications Explore ACI World publications to access e'}}
- **linkedin_url**: https://www.linkedin.com/company/aciworld

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 1, "address": "1500-800 rue du Square Victoria, Montréal, Québec H3C 0B4", "address_country": "CA", "address_url": "https://aci.aero/", "address_method": "pattern", "address_quote": "Learn more Contact Us Address 1500-800 rue du Square Victoria Montréal, Québec H3C 0B4 Canada General Inquiries Tel: +1 514 373 1200 Fax: +1 514 373 1201 Email: aci@a", "phone": "+1 514 373 1200", "phone_url": "https://aci.aero/", "domain": "aci.aero", "key": "vd:aci.aero", "name": "Airports Council International", "website": "https://aci.aero/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Helsinki Airport | Q215327 | official website on the organisation's domain (https://www.finavia.fi/en/airports/helsinki-airport) + name |  | Helsinki Airport | aéroport d'Helsinki-Vantaa | international airport; airport; commercial traffic aerodrome |  | Finland | 1952-00-00 |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:55296ea7815e00b5",
 "ap_contact_team": {
  "emails": [
   "airtrafficinvoices@finavia.fi",
   "accountspayable@finavia.fi",
   "payments@finavia.fi"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "airtrafficinvoices@finavia.fi",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.finavia.fi/sites/default/files/documents/Finavia_Terms_of_Services_01.01.2025.pdf",
    "quote": "used in Finland for at least 50 years and that have a clear historical significance. The aircraft must be reported as a vintage aircraft to airtrafficinvoices@finavia.fi before operations in order for this exemption to apply. Exemptions 3, 4, and 5 do not apply at Helsinki Airport. Exempti",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Helsinki Airport",
    "task_id": "CL-WS-00407"
   },
   {
    "email": "accountspayable@finavia.fi",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.finavia.fi/sites/default/files/documents/SupplierLetter_1.pdf",
    "quote": "g Basware’s support personnel. We would like to kindly ask you to inform us of the number of your first online invoice by sending e-mail to accountspayable@finavia.fi. In this manner, we can ensure that your invoice has arrived. Kind regards, Finavia Corporation, Accounts Payable",
    "retrieved_date": "2026-11-03",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Helsinki Airport",
    "task_id": "CL-SM-00015"
   },
   {
    "email": "accountspayable@finavia.fi",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.finavia.fi/sites/default/files/documents/SupplierLetter_0.pdf",
    "quote": "g Basware’s support personnel. We would like to kindly ask you to inform us of the number of your first online invoice by sending e-mail to accountspayable@finavia.fi. In this manner, we can ensure that your invoice has arrived. Kind regards, Finavia Corporation, Accounts Payable",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Helsinki Airport",
    "task_id": "CL-WS-00008"
   },
   {
    "email": "payments@finavia.fi",
    "type": "supplier_payment",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.finavia.fi/sites/default/files/documents/Finavia_Terms_of_Services_01.01.2025.pdf",
    "quote": "en paid. 9.1. Methods of payment The air carrier shall agree on the method of payment with Finavia before starting operations by contacting payments@finavia.fi. Unless otherwise agreed with Finavia, the charges shall be paid to Finavia immediately, before departure from an airport operated",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Helsinki Airport",
    "task_id": "CL-WS-00407"
   }
  ]
 },
 "research_status": {
  "found": 4
 },
 "queries_tried": [
  "site crawl of www.finavia.fi (60 pages, robots.txt respected), no AI, no search engine",
  "web search for the buyer's invoicing / accounts payable page (the search only gave the address); the page then read by tools/deep_pages.py with the crawler's rules, no AI",
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

## The vendor's other buyers in the dataset (first 60 of 0)
_none_

## Open questions for hand research (layer 2)

- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
