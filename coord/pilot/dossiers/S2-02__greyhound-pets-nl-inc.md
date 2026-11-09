# S2-02 — Greyhound Pets - NL Inc. ⇄ inferred: Canada Post Corporation

Stratum: **S2_complete_no_published_PO_rule** · pay on sight: yes — reference rule not published (quote the buyer's PO / order number when one is issued) · channel tier 2 · AP grade C · missing: (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Greyhound Pets - NL Inc. (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (gpnl.ca) + name) — 19 CARROLL DR, Mount Pearl, NL, A1N3A9 — buyer tax no. 825231970 RR0001 (as printed: Registration No. 825231970RR0001; https://gpnl.ca/)
SUBMIT TO: treasurer@gpnl.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is | CURRENCY: DERIVED: EUR (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Greyhound Pets - NL Inc. (company (private sector), NL) — inferred: no record; the organisation's type and province make a Canadian supplier
```

## Relationship
- **rank_group**: I3
- **data_quality_score**: 48
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: LOW (plausible supplier only)
- **relationship_detail**: Greyhound Pets - NL Inc. (company (private sector), NL) — inferred: no record; the organisation's type and province make a Canadian supplier relationship near-certain: inferred: Canada Post Corporation | published by: inference from the buyer's type and province (no contract, payment or listing record) | vendor in Canada because: the vendor's own site, https://www.canadapost-postescanada.ca/cpc/en/our-company/transparency-and-trust/privacy-centre/info-source/additional-information.page: 'Access to Information and Privacy Canada Post Corporation 2 | status rule: inferred relationship (no record): low confidence; the buyer is an organisation located in Canada (Newfoundland and Labrador) (province from its registered address in the CRA List of charities 2024 (open.canada.ca)); gen
- **how_relationship_was_found**: no record; tools/org_lists.py / osm_orgs.py / the crawlers placed the organisation in Canada by type and province; the vendor named is the Canada-located supplier such bodies almost always pay (see `vendor_country_basis`)
- **keys**: cra:825231970
- **tier**: I
- **grade**: 3

## Buyer
- **buyer**: Greyhound Pets - NL Inc.
- **buyer_website**: https://gpnl.ca
- **buyer_address**: 19 CARROLL DR, Mount Pearl, NL, A1N3A9
- **buyer_contact_evidence_url**: https://gpnl.ca/contact/
- **buyer_legal_name_as_published**: Greyhound Pets - NL Inc. (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (gpnl.ca) + name)
- **buyer_bn_as_published**: 825231970 RR0001 (as printed: Registration No. 825231970RR0001; https://gpnl.ca/)
- **buyer_bn_program**: RR (registered charity program account)
- **buyer_gst_hst_derived**: 825231970RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_logo_url**: https://gpnl.ca/wp-content/uploads/2021/07/gpnl-header-logo-nb.png
- **buyer_website_status**: site answers
- **buyer_type**: company (private sector)
- **buyer_sector**: private sector
- **buyer_charity_status**: registered (listed) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (gpnl.ca) + name)
- **buyer_charity_designation**: C; 0180
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://gpnl.ca/contact/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers; AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); AP contact name: the lane's AP page (https://gpnl.ca/contact/)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is accounted for by the buyer under the reverse charge where applicable
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: treasurer@gpnl.ca
- **email_type**: finance/accounting dept or supplier-payment office
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); finance mailbox
- **email_evidence_url**: https://gpnl.ca/contact/
- **email_evidence_quote**: Kelly Walsh // Treasurer Email: treasurer@gpnl.ca Board Members: Adam Watkins Email: awatkins@gpnl.ca Andrea Squires Email: asquires@gpnl.ca Chesley Green Ward Email: cgreenward@gpnl
- **email_evidence_context**: /Foster Available to Adopt How to Adopt/Foster Adoption/Fostering Form How You Can Help FAQ Contact Us Donate Contact Us GPNL Executive Committee Kim Powell // President Emergencies: (709) 693-8895 Email: info@gpnl.ca Kelly Walsh // Treasurer Email: treasurer@gpnl.ca Board Members: Adam Watkins Email: awatkins@gpnl.ca Andrea Squires Email: asquires@gpnl.ca Chesley Green Ward Email: cgreenward@gpnl.ca Marissa Walsh Email: mwalsh@gpnl.ca Pam Carter Email: pcarter@gpnl.ca Search for: Greyt Links GPNL Adoption Handb (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: treasurer@gpnl.ca (finance/accounting dept or supplier-payment office) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://gpnl.ca/contact/ | quote: "Kelly Walsh // Treasurer Email: treasurer@gpnl.ca Board Members: Adam Watkins Email: awatkins@gpnl.ca Andrea Squires Email: asquires@gpnl.ca Chesley Green Ward " | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Google Workspace | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-CRA-16684
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Google Workspace
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none;
- **dmarc_record_domain**: gpnl.ca
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 ip4:54.39.51.72 +a +mx ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_contact_name_as_published**: Kelly Walsh (as printed by the organisation next to its invoicing mailbox)
- **ap_phone**: (709) 693-8895 (as printed on https://gpnl.ca/contact/, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "ap_phone": "(709) 693-8895 (as printed on https://gpnl.ca/contact/, re-read 2026-11-08)"}
- **invoice_currency_derived**: EUR (derived from the buyer's country; CAD if the parties agreed so)
- **channel_tier**: 2
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Greyhound Pets - NL Inc. (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (gpnl.ca) + name) — 19 CARROLL DR, Mount Pearl, NL, A1N3A9 — buyer tax no. 825231970 RR0001 (as printed: Registration No. 825231970RR0001; https://gpnl.ca/) ⏎ SUBMIT TO: treasurer@gpnl.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is | CURRENCY: DERIVED: EUR (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Greyhound Pets - NL Inc. (company (private sector), NL) — inferred: no record; the organisation's type and province make a Canadian supplier
- **invoice_card_json**: {"bill_to": {"legal_name": "Greyhound Pets - NL Inc. (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (gpnl.ca) + name)", "legal_name_is_published": true, "address": "19 CARROLL DR, Mount Pearl, NL, A1N3A9", "address_is_the_invoice_address": false, "tax_number": "825231970 RR0001 (as printed: Registration No. 825231970RR0001; https://gpnl.ca/)", "language": "en"}, "submit_to": {"email": "treasurer@gpnl.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is", "buyer_tax_status_is_published": false, "indicative_rate": "", "currency": "DERIVED: EUR (derived from the buyer's country; C", "currency_is_published": false, "vendor_gst_hst": "119321495RT0001 (GST/HST 11
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 63
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
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
- **contract_status**: inferred relationship (no record): low confidence; the buyer is an organisation located in Canada (Newfoundland and Labrador) (province from its registered address in the CRA List of charities 2024 (open.canada.ca)); generic: Canada Post holds the exclusive privilege of collecting, transmitting and delivering letters within Canada (Canada Post Corporation Act, s. 14); most organisations mail some letters, but not every one does
- **source**: inference from the buyer's type and province (no contract, payment or listing record)
- **contracts_with_canadian_suppliers**: 0
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 825231970RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is accounted for by the buyer under the reverse charge where applicable
- **invoice_currency_derived**: EUR (derived from the buyer's country; CAD if the parties agreed so)
- **vendor_gst_hst_derived**: 119321495RT0001 (GST/HST 119321495 (RT program; account suffix not printed); QST 1006393299)

## Pay on sight / grades
- **pay_on_sight**: yes — reference rule not published (quote the buyer's PO / order number when one is issued)
- **pay_on_sight_missing**: (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Greyhound Pets - NL Inc. (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (gpnl.ca) + name) — 19 CARROLL DR, Mount Pearl, NL, A1N3A9 — buyer tax no. 825231970 RR0001 (as printed: Registration No. 825231970RR0001; https://gpnl.ca/) ⏎ SUBMIT TO: treasurer@gpnl.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is | CURRENCY: DERIVED: EUR (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Greyhound Pets - NL Inc. (company (private sector), NL) — inferred: no record; the organisation's type and province make a Canadian supplier
- **invoice_card_json**: {"bill_to": {"legal_name": "Greyhound Pets - NL Inc. (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (gpnl.ca) + name)", "legal_name_is_published": true, "address": "19 CARROLL DR, Mount Pearl, NL, A1N3A9", "address_is_the_invoice_address": false, "tax_number": "825231970 RR0001 (as printed: Registration No. 825231970RR0001; https://gpnl.ca/)", "language": "en"}, "submit_to": {"email": "treasurer@gpnl.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is", "buyer_tax_status_is_published": false, "indicative_rate": "", "currency": "DERIVED: EUR (derived from the buyer's country; C", "currency_is_published": false, "vendor_gst_hst": "119321495RT0001 (GST/HST 11
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 63
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["treasurer@gpnl.ca (finance/accounting dept or supplier-payment office)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://gpnl.ca/contact/", "quote: \"Kelly Walsh // Treasurer Email: treasurer@gpnl.ca Board Members: Adam Watkins Email: awatkins@gpnl.ca Andrea Squires Email: asquires@gpnl.ca Chesley Green Ward \"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Google Workspace", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-CRA-16684"], "buyer_facts": ["address and phone: the buyer's own site, https://gpnl.ca/contact/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers", "AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "AP contact name: the lane's AP page (https://gpnl.ca/contact/)"], "vendor_facts": ["name and address: the record's vendor block (inference from the buyer's type a

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://gpnl.ca/contact/ | 2026-11-08 | ok |  |  |  | (709) 693-8895 |  |  |  |  |  |

## Buyer site facts (org_extras, gpnl.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **bn**: 825231970
- **bn_program**: RR0001
- **bn_label**: Registration No. 825231970RR0001
- **bn_url**: https://gpnl.ca/
- **bn_quote**: me Contact Us (709) 693-8895 info@gpnl.ca GreyhoundPetsNL greyhound_pets_nl GreyhoundPetsNL Charity Registration No. 825231970RR0001 SUBSCRIBE TO OUR NEWSLETTER! © 2026 Greyhound Pets NL. Proudly powered by Sydney
- **logo_url**: https://gpnl.ca/wp-content/uploads/2021/07/gpnl-header-logo-nb.png
- **logo_basis**: logo image in the site header
- **domain**: gpnl.ca
- **key**: cra:825231970
- **name**: Greyhound Pets - NL Inc.
- **website**: https://gpnl.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Electronic Money Transfer
- **legal_name_stated_url**: https://gpnl.ca/donate/
- **legal_name_stated_quote**: se dogs and care for the many thousands still waiting for their families. To donate, please send an Electronic Money Transfer (EMT) to treasurer@gpnl.ca . CONTACT US Search for: Greyt Links GPNL Adoption Handbook Grey Talk Gr

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "emails": "info@gpnl.ca", "emails_url": "https://gpnl.ca/contact/", "domain": "gpnl.ca", "key": "cra:825231970", "name": "Greyhound Pets - NL Inc.", "website": "https://gpnl.ca/", "kind": "buyer", "date": "2026-11-03"}

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
| buyer | Greyhound Pets - NL Inc. | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Greyhound%20Pets%20-%20NL%20Inc. | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Canada Post | Q1032001 | official website on the organisation's domain (https://www.canadapost-postescanada.ca/) + name |  | Canada Post | Postes Canada | business; state-owned enterprise | business corporation | Canada | 1867-07-01 | Ottawa |
| b | Greyhound Pets - NL Inc. |  |  |  |  |  |  |  |  |  |  |
| v | SOCIÉTÉ CANADIENNE DES POSTES | Q1032001 | official website on the organisation's domain (https://www.canadapost-postescanada.ca/) + name |  | Canada Post | Postes Canada | business; state-owned enterprise | business corporation | Canada | 1867-07-01 | Ottawa |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "cra:825231970",
 "ap_contact_team": {
  "emails": [
   "treasurer@gpnl.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "treasurer@gpnl.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://gpnl.ca/contact/",
    "quote": "Kelly Walsh // Treasurer Email: treasurer@gpnl.ca Board Members: Adam Watkins Email: awatkins@gpnl.ca Andrea Squires Email: asquires@gpnl.ca Chesley Green Ward Email: cgreenward@gpnl",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Greyhound Pets - NL Inc.",
    "task_id": "CL-CRA-16684"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of www.gpnl.ca (8 pages, robots.txt respected), no AI, no search engine"
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
