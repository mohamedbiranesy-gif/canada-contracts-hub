# S4-48 — Urgent Care Without the Emergency Hospital ⇄ inferred: Canada Post Corporation

Stratum: **S4_routed_company_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Urgent Care Without the Emergency Hospital (stated on https://nlurgentcare.ca/) — 193 Kenmount Road Unit 2, St. John's, Newfoundland and Labrador, A1B 3P9, Canada (schema.org JSON-LD PostalAddress on https://nlurgentcare.ca/)
SUBMIT TO: info@nlurgentcare.ca (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is | CURRENCY: DERIVED: EUR (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Urgent Care Without the Emergency Hospital (hospital / health authority, NL) — inferred: no record; the organisation's type and province mak
```

## Relationship
- **rank_group**: I1
- **data_quality_score**: 30
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 6
- **reverify_due**: no
- **inference_confidence**: LOW (plausible supplier only)
- **relationship_detail**: Urgent Care Without the Emergency Hospital (hospital / health authority, NL) — inferred: no record; the organisation's type and province make a Canadian supplier relationship near-certain: inferred: Canada Post Corporation | published by: inference from the buyer's type and province (no contract, payment or listing record) | vendor in Canada because: the vendor's own site, https://www.canadapost-postescanada.ca/cpc/en/our-company/transparency-and-trust/privacy-centre/info-source/additional-information.page: 'Access to Information and Privacy Canada Post Corporation 2 | status rule: inferred relationship (no record): low confidence; the buyer is an organisation located in Canada (Newfoundland and Labrador) (province from the postal code on its own page (A1B 3P9)); generic: Canada Post holds the excl
- **how_relationship_was_found**: no record; tools/org_lists.py / osm_orgs.py / the crawlers placed the organisation in Canada by type and province; the vendor named is the Canada-located supplier such bodies almost always pay (see `vendor_country_basis`)
- **keys**: crux:nlurgentcare.ca
- **tier**: I
- **grade**: 1

## Buyer
- **buyer**: Urgent Care Without the Emergency Hospital
- **buyer_website**: https://nlurgentcare.ca
- **buyer_address**: 193 Kenmount Road Unit 2, St. John's, Newfoundland and Labrador, A1B 3P9, Canada (schema.org JSON-LD PostalAddress on https://nlurgentcare.ca/)
- **buyer_phone**: 902-332-1808
- **buyer_contact_evidence_url**: https://nlurgentcare.ca/contact-us/
- **buyer_legal_name_as_published**: Urgent Care Without the Emergency Hospital (stated on https://nlurgentcare.ca/)
- **buyer_logo_url**: https://nlurgentcare.ca/wp-content/uploads/2026/08/nl-logo.svg
- **buyer_website_status**: site answers
- **buyer_type**: hospital / health authority
- **buyer_sector**: healthcare
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://nlurgentcare.ca/contact-us/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is accounted for by the buyer under the reverse charge where applicable
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: info@nlurgentcare.ca
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://nlurgentcare.ca/
- **email_evidence_quote**: PM – 12 AM 193 Kenmount Road Unit 2, St. John’s, NL, A1B 3P9, Canada 193 Kenmount Road Unit 2, St. John's, NL, A1B 3P9, Canada 902-332-1808 info@nlurgentcare.ca About Clinic About Us Our Team Flexible Payment Plans Frequently Asked Questions Careers Privacy Policy Other Pet Services Surgic
- **email_evidence_context**: AM Wednesday: 12 PM – 12 AM Thursday: 12 PM – 12 AM Friday: 12 PM – 12 AM Saturday: 12 PM – 12 AM Sunday: 12 PM – 12 AM 193 Kenmount Road Unit 2, St. John’s, NL, A1B 3P9, Canada 193 Kenmount Road Unit 2, St. John's, NL, A1B 3P9, Canada 902-332-1808 info@nlurgentcare.ca About Clinic About Us Our Team Flexible Payment Plans Frequently Asked Questions Careers Privacy Policy Other Pet Services Surgical Interventions Emergency Care Diagnostic Imaging Get in Touch Contact Us For Referring Vets Book an Appointment Powere (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: info@nlurgentcare.ca (general) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-03 | page: https://nlurgentcare.ca/ | quote: "PM – 12 AM 193 Kenmount Road Unit 2, St. John’s, NL, A1B 3P9, Canada 193 Kenmount Road Unit 2, St. John's, NL, A1B 3P9, Canada 902-332-1808 info@nlurgentcare.ca" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: no DMARC record; no SPF record; mail handled by Google Workspace | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-CRUX-048626
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: no DMARC record; no SPF record; mail handled by Google Workspace
- **dmarc_policy**: no DMARC record
- **dmarc_record**: no DMARC record at _dmarc.nlurgentcare.ca; confirmed by 8.8.8.8
- **spf_policy**: no SPF record
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: EUR (derived from the buyer's country; CAD if the parties agreed so)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Urgent Care Without the Emergency Hospital (stated on https://nlurgentcare.ca/) — 193 Kenmount Road Unit 2, St. John's, Newfoundland and Labrador, A1B 3P9, Canada (schema.org JSON-LD PostalAddress on https://nlurgentcare.ca/) ⏎ SUBMIT TO: info@nlurgentcare.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is | CURRENCY: DERIVED: EUR (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Urgent Care Without the Emergency Hospital (hospital / health authority, NL) — inferred: no record; the organisation's type and province mak
- **invoice_card_json**: {"bill_to": {"legal_name": "Urgent Care Without the Emergency Hospital (stated on https://nlurgentcare.ca/)", "legal_name_is_published": true, "address": "193 Kenmount Road Unit 2, St. John's, Newfoundland and Labrador, A1B 3P9, Canada (schema.org JSON-LD PostalAddress on https://nlurgentcare.ca/)", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "info@nlurgentcare.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is", "buyer_tax_status_is_published": false, "indicative_rate": "", "currency": "DERIVED: EUR (derived from the buyer's country; C", "currency_is_published": false, "vendor_gst_hst": "119321495RT0001 (GST/HST 119321495 (RT program; account suffix not printed); QST 1006393299)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "inferred: Canada Post Corporation", "bn9": "119321495 (GST/HST registration number
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
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
- **contract_status**: inferred relationship (no record): low confidence; the buyer is an organisation located in Canada (Newfoundland and Labrador) (province from the postal code on its own page (A1B 3P9)); generic: Canada Post holds the exclusive privilege of collecting, transmitting and delivering letters within Canada (Canada Post Corporation Act, s. 14); most organisations mail some letters, but not every one does
- **source**: inference from the buyer's type and province (no contract, payment or listing record)
- **contracts_with_canadian_suppliers**: 0
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is accounted for by the buyer under the reverse charge where applicable
- **invoice_currency_derived**: EUR (derived from the buyer's country; CAD if the parties agreed so)
- **vendor_gst_hst_derived**: 119321495RT0001 (GST/HST 119321495 (RT program; account suffix not printed); QST 1006393299)

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Urgent Care Without the Emergency Hospital (stated on https://nlurgentcare.ca/) — 193 Kenmount Road Unit 2, St. John's, Newfoundland and Labrador, A1B 3P9, Canada (schema.org JSON-LD PostalAddress on https://nlurgentcare.ca/) ⏎ SUBMIT TO: info@nlurgentcare.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is | CURRENCY: DERIVED: EUR (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Urgent Care Without the Emergency Hospital (hospital / health authority, NL) — inferred: no record; the organisation's type and province mak
- **invoice_card_json**: {"bill_to": {"legal_name": "Urgent Care Without the Emergency Hospital (stated on https://nlurgentcare.ca/)", "legal_name_is_published": true, "address": "193 Kenmount Road Unit 2, St. John's, Newfoundland and Labrador, A1B 3P9, Canada (schema.org JSON-LD PostalAddress on https://nlurgentcare.ca/)", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "info@nlurgentcare.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is", "buyer_tax_status_is_published": false, "indicative_rate": "", "currency": "DERIVED: EUR (derived from the buyer's country; C", "currency_is_published": false, "vendor_gst_hst": "119321495RT0001 (GST/HST 119321495 (RT program; account suffix not printed); QST 1006393299)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "inferred: Canada Post Corporation", "bn9": "119321495 (GST/HST registration number
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["info@nlurgentcare.ca (general)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-03", "page: https://nlurgentcare.ca/", "quote: \"PM – 12 AM 193 Kenmount Road Unit 2, St. John’s, NL, A1B 3P9, Canada 193 Kenmount Road Unit 2, St. John's, NL, A1B 3P9, Canada 902-332-1808 info@nlurgentcare.ca\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: no DMARC record; no SPF record; mail handled by Google Workspace", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-CRUX-048626"], "buyer_facts": ["address and phone: the buyer's own site, https://nlurgentcare.ca/contact-us/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (inference from the buyer's type and province (no contract, payment or listing record))", "BN9: printed on the organisation's own page (https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf)", "GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected", "not automated)", "phone / role e-mails / logo: the vendor's own site, https://www.canadapost-postescanada.ca/cpc/

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://nlurgentcare.ca/ | 2026-11-08 | ok |  |  |  | 902-332-1808 | 193 Kenmount Road Unit 2, St. John's, NL, A1B 3P9 |  |  |  |  |

## Buyer site facts (org_extras, nlurgentcare.ca)
- **status**: ok
- **pages**: 4
- **language**: en
- **logo_url**: https://nlurgentcare.ca/wp-content/uploads/2026/08/nl-logo.svg
- **logo_basis**: logo image in the site header
- **domain**: nlurgentcare.ca
- **key**: crux:nlurgentcare.ca
- **name**: nlurgentcare.ca
- **website**: https://nlurgentcare.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Galaxy Vets Urgent Care & Walk-in : Newfoundland
- **jsonld_alternate_name**: Galaxy Vets Urgent Care & Walk-in : Newfoundland
- **jsonld_address**: 193 Kenmount Road Unit 2, St. John's, Newfoundland and Labrador, A1B 3P9, Canada
- **jsonld_phone**: +1-902-332-1808
- **jsonld_logo**: https://nlurgentcare.ca/wp-content/uploads/2025/07/favicon.png
- **jsonld_url**: https://nlurgentcare.ca
- **jsonld_founding_date**: 2026-06-20
- **jsonld_employees**: 20
- **jsonld_same_as**: https://www.facebook.com/nlurgentcare; https://www.instagram.com/nlurgentcare/
- **jsonld_quote**: {"@context":"https://schema.org","@type":"VeterinaryCare","name":"Galaxy Vets Urgent Care \u0026 Walk-in : Newfoundland","image":"https://nlurgentcare.ca/wp-content/uploads/2025/07/favicon.png","url":"https://nlurgentcare.ca","telephone":"902-332-1808","priceRange":"$$","@id":"https://nlurgentcare.c
- **jsonld_page**: https://nlurgentcare.ca/
- **legal_name_stated**: Urgent Care Without the Emergency Hospital
- **legal_name_stated_url**: https://nlurgentcare.ca/
- **legal_name_stated_quote**: M to 12 AM every day, so your pet can receive care when your family veterinarian is unavailable. ✔️ Urgent Care Without the Emergency Hospital Price Get the care your pet needs for up to 40% less than at an emergency hospital, with quality tr
- **mentions**: {'payment_method': {'text': 'interactions with our clinic', 'url': 'https://nlurgentcare.ca/privacy-policy/', 'quote': 'ime. “ Message frequency Message frequency may vary depending on the type of communication and your interactions with our clinic. You may receive up to 2–4 SMS messages per month regarding your appointments or account status. Me'}}
- **tel_links**: +19023321808

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "193 Kenmount Road Unit 2, St. John's, Newfoundland and Labrador, A1B 3P9", "address_country": "Canada", "address_url": "https://nlurgentcare.ca/contact-us/", "address_method": "json-ld", "address_quote": "m 12 PM to 12 AM 🐾🎉 Menu 902-332-1808 193 Kenmount Road Unit 2, St. John's, NL, A1B 3P9, Canada Book an Appointment 902-332-1808 Book an Appointment About Us Our Team", "phone": "902-332-1808", "phone_url": "https://nlurgentcare.ca/contact-us/", "emails": "info@nlurgentcare.ca", "emails_url": "https://nlurgentcare.ca/contact-us/", "domain": "nlurgentcare.ca", "key": "crux:nlurgentcare.ca", "name": "nlurgentcare.ca", "website": "https://nlurgentcare.ca/", "kind": "buyer", "date": "2026-11-06"}

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
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | nlurgentcare.ca | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=nlurgentcare.ca | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Canada Post | Q1032001 | official website on the organisation's domain (https://www.canadapost-postescanada.ca/) + name |  | Canada Post | Postes Canada | business; state-owned enterprise | business corporation | Canada | 1867-07-01 | Ottawa |
| v | SOCIÉTÉ CANADIENNE DES POSTES | Q1032001 | official website on the organisation's domain (https://www.canadapost-postescanada.ca/) + name |  | Canada Post | Postes Canada | business; state-owned enterprise | business corporation | Canada | 1867-07-01 | Ottawa |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "crux:nlurgentcare.ca",
 "ap_contact_team": {
  "emails": [
   "info@nlurgentcare.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "info@nlurgentcare.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://nlurgentcare.ca/",
    "quote": "PM – 12 AM 193 Kenmount Road Unit 2, St. John’s, NL, A1B 3P9, Canada 193 Kenmount Road Unit 2, St. John's, NL, A1B 3P9, Canada 902-332-1808 info@nlurgentcare.ca About Clinic About Us Our Team Flexible Payment Plans Frequently Asked Questions Careers Privacy Policy Other Pet Services Surgic",
    "retrieved_date": "2026-11-03",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "nlurgentcare.ca",
    "task_id": "CL-CRUX-048626"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of nlurgentcare.ca (18 pages, robots.txt respected), no AI, no search engine"
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

- an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed)
- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
