# S2-35 — Queen Elizabeth II Health Sciences Centre Foundation Inc. ⇄ inferred: Canada Post Corporation

Stratum: **S2_complete_no_published_PO_rule** · pay on sight: yes — reference rule not published (quote the buyer's PO / order number when one is issued) · channel tier 1 · AP grade C · missing: (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: QEII Foundation — 301-7051 Bayers Road Halifax, Nova Scotia B3L 2C1 (as printed on https://qe2foundation.ca/contact-us, re-read 2026-11-08) — buyer tax no. 886463496RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (qe2foundation.ca) + name)
SUBMIT TO: finance@qe2foundation.ca (invoicing/AP mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NS on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Queen Elizabeth II Health Sciences Centre Foundation Inc. (non-profit / association / cultural body, NS) — inferred: no record; the organisa
```

## Relationship
- **rank_group**: I4
- **data_quality_score**: 61
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: LOW (small organisation: mailing volume unknown)
- **relationship_detail**: Queen Elizabeth II Health Sciences Centre Foundation Inc. (non-profit / association / cultural body, NS) — inferred: no record; the organisation's type and province make a Canadian supplier relationship near-certain: inferred: Canada Post Corporation | published by: inference from the buyer's type and province (no contract, payment or listing record) | vendor in Canada because: the vendor's own site, https://www.canadapost-postescanada.ca/cpc/en/our-company/transparency-and-trust/privacy-centre/info-source/additional-information.page: 'Access to Information and Privacy Canada Post Corporation 2 | status rule: inferred relationship (no record): low confidence; the buyer is an organisation located in Canada (Nova Scotia) (province from its registered address in the CRA List of charities 2024 (open.canada.ca)); generic: Canada P
- **how_relationship_was_found**: no record; tools/org_lists.py / osm_orgs.py / the crawlers placed the organisation in Canada by type and province; the vendor named is the Canada-located supplier such bodies almost always pay (see `vendor_country_basis`)
- **keys**: cra:886463496
- **tier**: I
- **grade**: 4

## Buyer
- **buyer**: Queen Elizabeth II Health Sciences Centre Foundation Inc.
- **buyer_website**: https://qe2foundation.ca
- **buyer_address**: 3005-5657 SPRING GARDEN ROAD PARK LANE MALL BOX 231, Halifax, NS, B3J3R4
- **buyer_phone**: 902 220 7682
- **buyer_contact_evidence_url**: https://qe2foundation.ca/contact-us
- **buyer_legal_name_as_published**: QEII Foundation
- **buyer_bn_as_published**: 886463496RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (qe2foundation.ca) + name)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 886463496RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_logo_url**: https://qe2foundation.ca/themes/custom/qe2/logo.svg
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://linkedin.com/company/qeii-health-sciences-centre-foundation/
- **buyer_registry_id**: 3334251 (NS; https://ised-isde.canada.ca/cbr-rec/en/search?q=Queen%20Elizabeth%20II%20Health%20Sciences%20Centre%20Foundation%20Inc.)
- **buyer_type**: non-profit / association / cultural body
- **buyer_sector**: non-profit
- **buyer_charity_status**: registered (listed) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (qe2foundation.ca) + name)
- **buyer_charity_designation**: A; 0210
- **buyer_legal_form**: Limited by Guarantee (Canada's Business Registries, NS 3334251, 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://qe2foundation.ca/contact-us (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers; AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoice mailing address: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NS on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: finance@qe2foundation.ca
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://qe2foundation.ca/contact-us
- **email_evidence_quote**: QEII Foundation Payables finance@qe2foundation.ca Full width Gutter Without gutter Sign up to receive updates on QEII news and ways to support health care Email Address Sign u
- **email_evidence_context**: nts & Partnerships Coordinator 902 456 4598 Sarah J. White - Direct Marketing & Engagement Officer 902 266 5029 Jennifer Grover - Donor Services Administrator - Memorial/Tribute 902 442 7163 j ennifer.grover@qe2foundation.ca QEII Foundation Payables finance@qe2foundation.ca Full width Gutter Without gutter Sign up to receive updates on QEII news and ways to support health care Email Address Sign up Footer menu Financials About Contact News Careers QEII Staff Portal QEII Health Sciences Centre Foundation 301-7051 Bayers (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: finance@qe2foundation.ca (invoicing/AP) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://qe2foundation.ca/contact-us | quote: "QEII Foundation Payables finance@qe2foundation.ca Full width Gutter Without gutter Sign up to receive updates on QEII news and ways to support health care Email" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-CRA-21278
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject; rua=mailto:8367dd2b5f014042a8eb7ff855ceb1d2@dmarc-reports.cloudflare.net,mailto:45a96ae46ebc.a@dmarcinput.com; ruf=mailto:45a96ae46ebc.f@dmarcinput.com; fo=1
- **dmarc_record_domain**: qe2foundation.ca
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 include:spf.protection.outlook.com include:servers.mcsv.net include:mailgun.org include:spf.constantcontact.com include:outboundmail.blackbaud.net +ip4:184.107.41.89 -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_phone**: 902 456 4598 (as printed on https://qe2foundation.ca/contact-us, re-read 2026-11-08)
- **invoice_mailing_address**: 301-7051 Bayers Road Halifax, Nova Scotia B3L 2C1 (as printed on https://qe2foundation.ca/contact-us, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "ap_phone": "902 456 4598 (as printed on https://qe2foundation.ca/contact-us, re-read 2026-11-08)", "mailing_address": "301-7051 Bayers Road Halifax, Nova Scotia B3L 2C1 (as printed on https://qe2foundation.ca/contact-us, re-read 2026-11-08)"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: QEII Foundation — 301-7051 Bayers Road Halifax, Nova Scotia B3L 2C1 (as printed on https://qe2foundation.ca/contact-us, re-read 2026-11-08) — buyer tax no. 886463496RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (qe2foundation.ca) + name) ⏎ SUBMIT TO: finance@qe2foundation.ca (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NS on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Queen Elizabeth II Health Sciences Centre Foundation Inc. (non-profit / association / cultural body, NS) — inferred: no record; the orga
- **invoice_card_json**: {"bill_to": {"legal_name": "QEII Foundation", "legal_name_is_published": true, "address": "301-7051 Bayers Road Halifax, Nova Scotia B3L 2C1 (as printed on https://qe2foundation.ca/contact-us, re-read 2026-11-08)", "address_is_the_invoice_address": true, "tax_number": "886463496RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (qe2foundation.ca) + name)", "language": "en"}, "submit_to": {"email": "finance@qe2foundation.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "301-7051 Bayers Road Halifax, Nova Scotia B3L 2C1 (as printed on https://qe2foundation.ca/contact-us, re-read 2026-11-08)", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NS on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicati
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 73
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: finance mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility)
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
- **contract_status**: inferred relationship (no record): low confidence; the buyer is an organisation located in Canada (Nova Scotia) (province from its registered address in the CRA List of charities 2024 (open.canada.ca)); generic: Canada Post holds the exclusive privilege of collecting, transmitting and delivering letters within Canada (Canada Post Corporation Act, s. 14); most organisations mail some letters, but not every one does
- **source**: inference from the buyer's type and province (no contract, payment or listing record)
- **contracts_with_canadian_suppliers**: 0
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 886463496RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NS on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: HST 15% (Nova Scotia) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 119321495RT0001 (GST/HST 119321495 (RT program; account suffix not printed); QST 1006393299)

## Pay on sight / grades
- **pay_on_sight**: yes — reference rule not published (quote the buyer's PO / order number when one is issued)
- **pay_on_sight_missing**: (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: QEII Foundation — 301-7051 Bayers Road Halifax, Nova Scotia B3L 2C1 (as printed on https://qe2foundation.ca/contact-us, re-read 2026-11-08) — buyer tax no. 886463496RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (qe2foundation.ca) + name) ⏎ SUBMIT TO: finance@qe2foundation.ca (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NS on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Queen Elizabeth II Health Sciences Centre Foundation Inc. (non-profit / association / cultural body, NS) — inferred: no record; the orga
- **invoice_card_json**: {"bill_to": {"legal_name": "QEII Foundation", "legal_name_is_published": true, "address": "301-7051 Bayers Road Halifax, Nova Scotia B3L 2C1 (as printed on https://qe2foundation.ca/contact-us, re-read 2026-11-08)", "address_is_the_invoice_address": true, "tax_number": "886463496RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (qe2foundation.ca) + name)", "language": "en"}, "submit_to": {"email": "finance@qe2foundation.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "301-7051 Bayers Road Halifax, Nova Scotia B3L 2C1 (as printed on https://qe2foundation.ca/contact-us, re-read 2026-11-08)", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NS on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicati
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 73
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: finance mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["finance@qe2foundation.ca (invoicing/AP)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://qe2foundation.ca/contact-us", "quote: \"QEII Foundation Payables finance@qe2foundation.ca Full width Gutter Without gutter Sign up to receive updates on QEII news and ways to support health care Email\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-CRA-21278"], "buyer_facts": ["address and phone: the buyer's own site, https://qe2foundation.ca/contact-us (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers", "AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoice mailing address: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (inference from the buyer's type a

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://qe2foundation.ca/contact-us | 2026-11-08 | ok |  |  |  | 902 456 4598 | 301-7051 Bayers Road Halifax, Nova Scotia B3L 2C1 |  |  |  |  |

## Buyer site facts (org_extras, qe2foundation.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: QEII Foundation
- **legal_name_url**: https://qe2foundation.ca/
- **legal_name_quote**: Create a lasting impact Leave a gift in your will See All The Ways To Give Get To Know Us About The QEII Foundation Strategic Directions 2022-2025 QEII Health Sciences Centre Why We Need You Frequently Asked Questio
- **logo_url**: https://qe2foundation.ca/themes/custom/qe2/logo.svg
- **logo_basis**: logo image in the site header
- **domain**: qe2foundation.ca
- **key**: cra:886463496
- **name**: Queen Elizabeth II Health Sciences Centre Foundation Inc.
- **website**: https://qe2foundation.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: QEII Foundation
- **jsonld_logo**: https://qe2foundation.ca//logo.png
- **jsonld_url**: https://qe2foundation.ca/
- **jsonld_quote**: { "@context": "https://schema.org", "@graph": [ { "@type": "WebSite", "name": "QEII Foundation", "url": "https://qe2foundation.ca/", "publisher": { "@type": "Organization", "name": "QEII Foundation", "url": "https://qe2foundation.ca/", "logo": { "@type": "ImageObject", "url": "https://qe2foundation.
- **jsonld_page**: https://qe2foundation.ca/
- **legal_name_stated**: QEII Health Sciences Centre
- **legal_name_stated_url**: https://qe2foundation.ca/
- **legal_name_stated_quote**: QEII Health Sciences Centre Foundation Skip to main content Menu Search Search Donate ❤ Fundraise Login Main navigation Home Wa
- **mentions**: {'payment_method': {'text': 'Interac e-Transfer Make a donation using Interac e-Transfer', 'url': 'https://my.qe2foundation.ca/donations', 'quote': 'es Make a donation of stocks, bonds and mutual funds, and take advantage of tax benefits. Donate by Interac e-Transfer Make a donation using Interac e-Transfer. --> QEII Health Sciences Centre Foundation 301-7051 Bayers Road Halifax, Nova Scotia B3L 2C1 Phone'}}
- **linkedin_url**: https://linkedin.com/company/qeii-health-sciences-centre-foundation/
- **tel_links**: 19023341546; 18884280220; 9022665029

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "Bayers Road, Halifax, NS B3L 2C1", "address_country": "CA", "address_url": "https://qe2foundation.ca/contact-us", "address_method": "pattern", "address_quote": "undation? Don't hesitate to reach out. Address 301-7051 Bayers Road Halifax, NS B3L 2C1 Hours Monday - Friday, 8:30 a.m. - 4:30 p.m. Contact Us Phone: 902 334 1546 Tol", "phone": "902 220 7682", "phone_url": "https://qe2foundation.ca/contact-us", "emails": "info@qe2foundation.ca", "emails_url": "https://qe2foundation.ca/contact-us", "domain": "qe2foundation.ca", "key": "cra:886463496", "name": "Queen Elizabeth II Health Sciences Centre Foundation Inc.", "website": "https://qe2foundation.ca/", "kind": "buyer", "date": "2026-11-03"}

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
| buyer | Queen Elizabeth II Health Sciences Centre Foundation Inc. | found | QUEEN ELIZABETH II HEALTH SCIENCES CENTRE FOUNDATION INC. | 886463496 | 3334251 | NS | Limited by Guarantee | Active | 2020-01-22 | HALIFAX | NOVA SCOTIA |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Queen%20Elizabeth%20II%20Health%20Sciences%20Centre%20Foundation%20Inc. | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Canada Post | Q1032001 | official website on the organisation's domain (https://www.canadapost-postescanada.ca/) + name |  | Canada Post | Postes Canada | business; state-owned enterprise | business corporation | Canada | 1867-07-01 | Ottawa |
| b | Queen Elizabeth II Health Sciences Centre Foundation Inc. |  |  |  |  |  |  |  |  |  |  |
| v | SOCIÉTÉ CANADIENNE DES POSTES | Q1032001 | official website on the organisation's domain (https://www.canadapost-postescanada.ca/) + name |  | Canada Post | Postes Canada | business; state-owned enterprise | business corporation | Canada | 1867-07-01 | Ottawa |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "cra:886463496",
 "ap_contact_team": {
  "emails": [
   "finance@qe2foundation.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "finance@qe2foundation.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://qe2foundation.ca/contact-us",
    "quote": "QEII Foundation Payables finance@qe2foundation.ca Full width Gutter Without gutter Sign up to receive updates on QEII news and ways to support health care Email Address Sign u",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Queen Elizabeth II Health Sciences Centre Foundation Inc.",
    "task_id": "CL-CRA-21278"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of www.qe2foundation.ca (25 pages, robots.txt respected), no AI, no search engine"
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
