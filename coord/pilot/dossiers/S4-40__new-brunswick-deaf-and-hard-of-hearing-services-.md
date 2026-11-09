# S4-40 — New Brunswick Deaf and Hard of Hearing Services Inc. / Services aux Sourds et Malentendants du Nouveau-Brunswick Inc. ⇄ inferred: Canada Post Corporation

Stratum: **S4_routed_company_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: New Brunswick Deaf and Hard of Hearing Services Inc — 324 DUKE ST W, Saint John, NB, E2M1V2 — buyer tax no. 135065613RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (nbdhhs.com) + name)
SUBMIT TO: info@nbdhhs.com (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: pays GST/HST on purchases (pay-and-rebate model): charge GST/HST on the invoice — GST/HST Memorandum 18-2 para. 23 (https://www.canada.ca/en/revenue-ag | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: New Brunswick Deaf and Hard of Hearing Services Inc. / Services aux Sourds et Malentendants du Nouveau-Brunswick Inc. (government ministry /
```

## Relationship
- **rank_group**: I1
- **data_quality_score**: 30
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: LOW (plausible supplier only)
- **relationship_detail**: New Brunswick Deaf and Hard of Hearing Services Inc. / Services aux Sourds et Malentendants du Nouveau-Brunswick Inc. (government ministry / agency, NB) — inferred: no record; the organisation's type and province make a Canadian supplier relationship near-certain: inferred: Canada Post Corporation | published by: inference from the buyer's type and province (no contract, payment or listing record) | vendor in Canada because: the vendor's own site, https://www.canadapost-postescanada.ca/cpc/en/our-company/transparency-and-trust/privacy-centre/info-source/additional-information.page: 'Access to Information and Privacy Canada Post Corporation 2 | status rule: inferred relationship (no record): low confidence; the buyer is an organisation located in Canada (New Brunswick) (province from its registered address in the CRA List of charities 2024 (open.canada.ca)); generic: Canada
- **how_relationship_was_found**: no record; tools/org_lists.py / osm_orgs.py / the crawlers placed the organisation in Canada by type and province; the vendor named is the Canada-located supplier such bodies almost always pay (see `vendor_country_basis`)
- **keys**: cra:135065613
- **tier**: I
- **grade**: 1

## Buyer
- **buyer**: New Brunswick Deaf and Hard of Hearing Services Inc. / Services aux Sourds et Malentendants du Nouveau-Brunswick Inc.
- **buyer_website**: https://nbdhhs.com
- **buyer_address**: 324 DUKE ST W, Saint John, NB, E2M1V2
- **buyer_phone**: (506) 633-0599 Ext. 1
- **buyer_contact_evidence_url**: https://nbdhhs.com/contact
- **buyer_legal_name_as_published**: New Brunswick Deaf and Hard of Hearing Services Inc
- **buyer_bn_as_published**: 135065613RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (nbdhhs.com) + name)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 135065613RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_logo_url**: https://nbdhhs.com/airo-assets/images/logo/horizontal
- **buyer_website_status**: site answers
- **buyer_type**: government ministry / agency
- **buyer_sector**: government: provincial / federal
- **buyer_charity_status**: registered (listed) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (nbdhhs.com) + name)
- **buyer_charity_designation**: C; 0100
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://nbdhhs.com/contact (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: pays GST/HST on purchases (pay-and-rebate model): charge GST/HST on the invoice — GST/HST Memorandum 18-2 para. 23 (https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The governments of all the participating provinces, as well as Quebec, British Columbia and Nunavut, have agreed to use the pay and rebate model. Therefore, their government departments and all of their Crown agents will pay the GST/HST on their purchases"); derived from buyer type and province, not published by the buyer
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: info@nbdhhs.com
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://www.nbdhhs.com/
- **email_evidence_quote**: rams & Support Book an Interpreter Activities Calendar Contact Us Head Office 324 Duke St West Saint John, NB E2M 1V2 (506) 633-0599 Ext. 1 info@nbdhhs.com View All Offices Language / Langue EN FR © 2026 New Brunswick Deaf and Hard of Hearing Services Inc. | nbdhhs.com Follow Us on Faceboo
- **email_evidence_context**: français. Quick Links Home About Us Store Contact Us Support Us Programs & Services Interpreting Services Programs & Support Book an Interpreter Activities Calendar Contact Us Head Office 324 Duke St West Saint John, NB E2M 1V2 (506) 633-0599 Ext. 1 info@nbdhhs.com View All Offices Language / Langue EN FR © 2026 New Brunswick Deaf and Hard of Hearing Services Inc. | nbdhhs.com Follow Us on Facebook Privacy Policy Terms of Use Accessibility (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: info@nbdhhs.com (general) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://www.nbdhhs.com/ | quote: "rams & Support Book an Interpreter Activities Calendar Contact Us Head Office 324 Duke St West Saint John, NB E2M 1V2 (506) 633-0599 Ext. 1 info@nbdhhs.com View" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-CRA-04162
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none; rua=mailto:support@nbdhhs.com; ruf=mailto:support@nbdhhs.com; fo=1;
- **dmarc_record_domain**: nbdhhs.com
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 include:spf.protection.outlook.com include:nbdhhs.com ip4:64.69.79.4 ip4:64.69.79.175 -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: New Brunswick Deaf and Hard of Hearing Services Inc — 324 DUKE ST W, Saint John, NB, E2M1V2 — buyer tax no. 135065613RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (nbdhhs.com) + name) ⏎ SUBMIT TO: info@nbdhhs.com (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: pays GST/HST on purchases (pay-and-rebate model): charge GST/HST on the invoice — GST/HST Memorandum 18-2 para. 23 (https://www.canada.ca/en/revenue-ag | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: New Brunswick Deaf and Hard of Hearing Services Inc. / Services aux Sourds et Malentendants du Nouveau-Brunswick Inc. (government ministry /
- **invoice_card_json**: {"bill_to": {"legal_name": "New Brunswick Deaf and Hard of Hearing Services Inc", "legal_name_is_published": true, "address": "324 DUKE ST W, Saint John, NB, E2M1V2", "address_is_the_invoice_address": false, "tax_number": "135065613RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (nbdhhs.com) + name)", "language": "en-fr (bilingual body: federal / New Brunswick; use the language of its invoicing page: en)"}, "submit_to": {"email": "info@nbdhhs.com", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: pays GST/HST on purchases (pay-and-rebate model): charge GST/HST on the invoice — GST/HST Memorandum 18-2 para. 23 (https://www.canada.ca/en/revenue-agency/serv", "buyer_tax_status_is_published": false, "indicative_rate": "HST 15% (New Brunswick)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en-fr (bilingual body: federal / New Brunswick; use the language of its invoicing page: en)

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
- **contract_status**: inferred relationship (no record): low confidence; the buyer is an organisation located in Canada (New Brunswick) (province from its registered address in the CRA List of charities 2024 (open.canada.ca)); generic: Canada Post holds the exclusive privilege of collecting, transmitting and delivering letters within Canada (Canada Post Corporation Act, s. 14); most organisations mail some letters, but not every one does
- **source**: inference from the buyer's type and province (no contract, payment or listing record)
- **contracts_with_canadian_suppliers**: 0
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 135065613RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_tax_status_derived**: pays GST/HST on purchases (pay-and-rebate model): charge GST/HST on the invoice — GST/HST Memorandum 18-2 para. 23 (https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The governments of all the participating provinces, as well as Quebec, British Columbia and Nunavut, have agreed to use the pay and rebate model. Therefore, their government departments and all of their Crown agents will pay the GST/HST on their purchases"); derived from buyer type and province, not published by the buyer
- **tax_rate_indicative_derived**: HST 15% (New Brunswick) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 119321495RT0001 (GST/HST 119321495 (RT program; account suffix not printed); QST 1006393299)

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: New Brunswick Deaf and Hard of Hearing Services Inc — 324 DUKE ST W, Saint John, NB, E2M1V2 — buyer tax no. 135065613RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (nbdhhs.com) + name) ⏎ SUBMIT TO: info@nbdhhs.com (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: pays GST/HST on purchases (pay-and-rebate model): charge GST/HST on the invoice — GST/HST Memorandum 18-2 para. 23 (https://www.canada.ca/en/revenue-ag | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: New Brunswick Deaf and Hard of Hearing Services Inc. / Services aux Sourds et Malentendants du Nouveau-Brunswick Inc. (government ministry /
- **invoice_card_json**: {"bill_to": {"legal_name": "New Brunswick Deaf and Hard of Hearing Services Inc", "legal_name_is_published": true, "address": "324 DUKE ST W, Saint John, NB, E2M1V2", "address_is_the_invoice_address": false, "tax_number": "135065613RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (nbdhhs.com) + name)", "language": "en-fr (bilingual body: federal / New Brunswick; use the language of its invoicing page: en)"}, "submit_to": {"email": "info@nbdhhs.com", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: pays GST/HST on purchases (pay-and-rebate model): charge GST/HST on the invoice — GST/HST Memorandum 18-2 para. 23 (https://www.canada.ca/en/revenue-agency/serv", "buyer_tax_status_is_published": false, "indicative_rate": "HST 15% (New Brunswick)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["info@nbdhhs.com (general)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://www.nbdhhs.com/", "quote: \"rams & Support Book an Interpreter Activities Calendar Contact Us Head Office 324 Duke St West Saint John, NB E2M 1V2 (506) 633-0599 Ext. 1 info@nbdhhs.com View\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-CRA-04162"], "buyer_facts": ["address and phone: the buyer's own site, https://nbdhhs.com/contact (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (inference from the buyer's type and province (no contract, payment or listing record))", "BN9: printed on the organisation's own page (https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf)", "GST/HST derived BN9 + RT0001 (CR

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.nbdhhs.com/ | 2026-11-08 | ok |  |  |  | (506) 633-0599 Ext. 1 | 324 Duke St West Saint John, NB E2M 1V2 |  |  |  |  |

## Buyer site facts (org_extras, nbdhhs.com)
- **status**: ok
- **pages**: 5
- **language**: en
- **legal_name**: New Brunswick Deaf and Hard of Hearing Services Inc
- **legal_name_url**: https://nbdhhs.com/
- **legal_name_quote**: NBDHHS — New Brunswick Deaf and Hard of Hearing Services Inc. Skip to main content EN | FR Home About Us Programs & Services Store Scholarships Book an Interpre
- **logo_url**: https://nbdhhs.com/airo-assets/images/logo/horizontal
- **logo_basis**: logo image on the site
- **domain**: nbdhhs.com
- **key**: cra:135065613
- **name**: New Brunswick Deaf and Hard of Hearing Services Inc. / Services aux Sourds et Malentendants du Nouveau-Brunswick Inc.
- **website**: https://nbdhhs.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: NonprofitOrganization
- **jsonld_name**: New Brunswick Deaf and Hard of Hearing Services Inc.
- **jsonld_alternate_name**: NBDHHS; SSMNB
- **jsonld_url**: https://nbdhhs.com
- **jsonld_quote**: {"@context":"https://schema.org","@graph":[{"@type":"NonprofitOrganization","@id":"https://nbdhhs.com/#organization","name":"New Brunswick Deaf and Hard of Hearing Services Inc.","alternateName":["NBDHHS","SSMNB"],"url":"https://nbdhhs.com","description":"Nonprofit organization serving Deaf, deafene
- **jsonld_page**: https://nbdhhs.com/
- **legal_name_stated**: New Brunswick Deaf and Hard of Hearing Services
- **legal_name_stated_url**: https://nbdhhs.com/about
- **legal_name_stated_quote**: Scholarships Book an Interpreter Calendar Contact Support Us EN FR Who We Are About NBDHHS / SSMNB New Brunswick Deaf and Hard of Hearing Services / Services aux Sourds et Malentendants du Nouveau-Brunswick Inc. (NBDHHS/SSMNB) was formed in Janua
- **tel_links**: +15066330599,1; 5066330599

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "Head Office, 324 Duke St West, Saint John, NB E2M 1V2, (506) 633-0599 Ext. 1", "address_country": "CA", "address_url": "https://nbdhhs.com/contact", "address_method": "address-tag", "address_quote": "sit one of our offices. Our Offices Head Office 324 Duke St West Saint John, NB E2M 1V2 Moncton Office 11 Leslie St Moncton, NB E1C 6M3 Fredericton Office 557 St Mary'", "phone": "(506) 633-0599 Ext. 1", "phone_url": "https://nbdhhs.com/contact", "emails": "info@nbdhhs.com", "emails_url": "https://nbdhhs.com/contact", "domain": "nbdhhs.com", "key": "cra:135065613", "name": "New Brunswick Deaf and Hard of Hearing Services Inc. / Services aux Sourds et Malentendants du Nouveau-Brunswick Inc.", "website": "https://nbdhhs.com/", "kind": "buyer", "date": "2026-11-03"}

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
| buyer | New Brunswick Deaf and Hard of Hearing Services Inc. / Services aux Sourds et Malentendants du Nouveau-Brunswick Inc. | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=New%20Brunswick%20Deaf%20and%20Hard%20of%20Hearing%20Services%20Inc.%20%2F%20Services%20aux%20Sourds%20et%20Malentendants%20du%20Nouveau-Brunswick%20Inc. | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Canada Post | Q1032001 | official website on the organisation's domain (https://www.canadapost-postescanada.ca/) + name |  | Canada Post | Postes Canada | business; state-owned enterprise | business corporation | Canada | 1867-07-01 | Ottawa |
| b | New Brunswick Deaf and Hard of Hearing Services Inc. / Services aux Sourds et Malentendants du Nouveau-Brunswick Inc. |  |  |  |  |  |  |  |  |  |  |
| v | SOCIÉTÉ CANADIENNE DES POSTES | Q1032001 | official website on the organisation's domain (https://www.canadapost-postescanada.ca/) + name |  | Canada Post | Postes Canada | business; state-owned enterprise | business corporation | Canada | 1867-07-01 | Ottawa |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "cra:135065613",
 "ap_contact_team": {
  "emails": [
   "info@nbdhhs.com"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "info@nbdhhs.com",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.nbdhhs.com/",
    "quote": "rams & Support Book an Interpreter Activities Calendar Contact Us Head Office 324 Duke St West Saint John, NB E2M 1V2 (506) 633-0599 Ext. 1 info@nbdhhs.com View All Offices Language / Langue EN FR © 2026 New Brunswick Deaf and Hard of Hearing Services Inc. | nbdhhs.com Follow Us on Faceboo",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "New Brunswick Deaf and Hard of Hearing Services Inc. / Services aux Sourds et Malentendants du Nouveau-Brunswick Inc.",
    "task_id": "CL-CRA-04162"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of www.nbdhhs.com (8 pages, robots.txt respected), no AI, no search engine"
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
