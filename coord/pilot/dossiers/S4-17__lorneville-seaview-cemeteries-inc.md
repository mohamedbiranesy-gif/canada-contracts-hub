# S4-17 — LORNEVILLE & SEAVIEW CEMETERIES INC. ⇄ inferred: Canada Post Corporation

Stratum: **S4_routed_company_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: LORNEVILLE & SEAVIEW CEMETERIES INC. (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (lornevilleseaviewcemeteries.ca) + name) — 1475 LORNEVILLE RD, Saint John, NB, E2M7H5 — buyer tax no. 119024750RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (lornevilleseaviewcemeteries.ca) + name)
SUBMIT TO: info@lornevilleseaviewcemeteries.ca (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NB on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in 
```

## Relationship
- **rank_group**: I1
- **data_quality_score**: 30
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: LOW (plausible supplier only)
- **relationship_detail**: LORNEVILLE & SEAVIEW CEMETERIES INC. (company (private sector), NB) — inferred: no record; the organisation's type and province make a Canadian supplier relationship near-certain: inferred: Canada Post Corporation | published by: inference from the buyer's type and province (no contract, payment or listing record) | vendor in Canada because: the vendor's own site, https://www.canadapost-postescanada.ca/cpc/en/our-company/transparency-and-trust/privacy-centre/info-source/additional-information.page: 'Access to Information and Privacy Canada Post Corporation 2 | status rule: inferred relationship (no record): low confidence; the buyer is an organisation located in Canada (New Brunswick) (province from its registered address in the CRA List of charities 2024 (open.canada.ca)); generic: Canada
- **how_relationship_was_found**: no record; tools/org_lists.py / osm_orgs.py / the crawlers placed the organisation in Canada by type and province; the vendor named is the Canada-located supplier such bodies almost always pay (see `vendor_country_basis`)
- **keys**: cra:119024750
- **tier**: I
- **grade**: 1

## Buyer
- **buyer**: LORNEVILLE & SEAVIEW CEMETERIES INC.
- **buyer_website**: https://lornevilleseaviewcemeteries.ca
- **buyer_address**: 1475 LORNEVILLE RD, Saint John, NB, E2M7H5
- **buyer_contact_evidence_url**: https://lornevilleseaviewcemeteries.ca/contact-us/
- **buyer_legal_name_as_published**: LORNEVILLE & SEAVIEW CEMETERIES INC. (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (lornevilleseaviewcemeteries.ca) + name)
- **buyer_bn_as_published**: 119024750RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (lornevilleseaviewcemeteries.ca) + name)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 119024750RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_logo_url**: https://lornevilleseaviewcemeteries.ca/wp-content/uploads/2016/02/LornevilleSeaview_LogoPhilip.png
- **buyer_website_status**: site answers
- **buyer_type**: company (private sector)
- **buyer_sector**: private sector
- **buyer_charity_status**: registered (listed) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (lornevilleseaviewcemeteries.ca) + name)
- **buyer_charity_designation**: C; 0160
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://lornevilleseaviewcemeteries.ca/contact-us/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers; payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NB on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: info@lornevilleseaviewcemeteries.ca
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://lornevilleseaviewcemeteries.ca/wp-content/uploads/2023/08/LSCI-Plot-Purchase-Terms-and-Conditions-1st-Adopted.pdf
- **email_evidence_quote**: entatives must notify us in writing and deliver it personally, send it by first class post to our registered address (below) or by email to info@lornevilleseaviewcemeteries.ca before the funeral arrangements are publicly announced. We must have at least 3 working days notice in advance of
- **email_evidence_context**: PURCHASE TERMS & CONDITIONS FOR GRAVE PLOTS & EXCLUSIVE RIGHTS OF INTERMENT 9. Notifying us You or your representatives must notify us in writing and deliver it personally, send it by first class post to our registered address (below) or by email to info@lornevilleseaviewcemeteries.ca before the funeral arrangements are publicly announced. We must have at least 3 working days notice in advance of the interment. We do not accept any responsibility for errors or omissions arising out of the transmission to us of any information by (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: info@lornevilleseaviewcemeteries.ca (general) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://lornevilleseaviewcemeteries.ca/wp-content/uploads/2023/08/LSCI-Plot-Purchase-Terms-and-Conditions-1st-Adopted.pdf | quote: "entatives must notify us in writing and deliver it personally, send it by first class post to our registered address (below) or by email to info@lornevilleseavi" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: no DMARC record; SPF -all (hard fail); mail handled by self-hosted or other (mx1-us1.ppe-hosted.com) | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-CRA-03706
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: no DMARC record; SPF -all (hard fail); mail handled by self-hosted or other (mx1-us1.ppe-hosted.com)
- **dmarc_policy**: no DMARC record
- **dmarc_record**: no DMARC record at _dmarc.lornevilleseaviewcemeteries.ca; confirmed by 8.8.8.8
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 a:dispatch-us.ppe-hosted.com include:secureserver.net -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **payment_terms_as_published**: paid to us within 28 days (as printed on https://lornevilleseaviewcemeteries.ca/wp-content/uploads/2023/08/LSCI-Plot-Purchase-Terms-and-Conditions-1st-Adopted.pdf, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "payment_terms": "paid to us within 28 days (as printed on https://lornevilleseaviewcemeteries.ca/wp-content/uploads/2023/08/LSCI-Plot-Purchase-Terms-and-Conditions-1st-Adopted.pdf, re-read 2026-11-08)"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: LORNEVILLE & SEAVIEW CEMETERIES INC. (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (lornevilleseaviewcemeteries.ca) + name) — 1475 LORNEVILLE RD, Saint John, NB, E2M7H5 — buyer tax no. 119024750RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (lornevilleseaviewcemeteries.ca) + name) ⏎ SUBMIT TO: info@lornevilleseaviewcemeteries.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NB on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the bu
- **invoice_card_json**: {"bill_to": {"legal_name": "LORNEVILLE & SEAVIEW CEMETERIES INC. (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (lornevilleseaviewcemeteries.ca) + name)", "legal_name_is_published": true, "address": "1475 LORNEVILLE RD, Saint John, NB, E2M7H5", "address_is_the_invoice_address": false, "tax_number": "119024750RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (lornevilleseaviewcemeteries.ca) + name)", "language": "en-fr (bilingual body: federal / New Brunswick; use the language of its invoicing page: en)"}, "submit_to": {"email": "info@lornevilleseaviewcemeteries.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "paid to us within 28 days (as printed on https://lornevilleseaviewcemeteries.ca/wp-content/uploads/2023/08/LSCI-Plot-Pu
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); vendor legal name; AP phone or contact for follow-up
- **ap_grade**: C
- **ap_score**: 57
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; payment terms published; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule
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
- **buyer_gst_hst_derived**: 119024750RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NB on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: HST 15% (New Brunswick) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 119321495RT0001 (GST/HST 119321495 (RT program; account suffix not printed); QST 1006393299)

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: LORNEVILLE & SEAVIEW CEMETERIES INC. (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (lornevilleseaviewcemeteries.ca) + name) — 1475 LORNEVILLE RD, Saint John, NB, E2M7H5 — buyer tax no. 119024750RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (lornevilleseaviewcemeteries.ca) + name) ⏎ SUBMIT TO: info@lornevilleseaviewcemeteries.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NB on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the bu
- **invoice_card_json**: {"bill_to": {"legal_name": "LORNEVILLE & SEAVIEW CEMETERIES INC. (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (lornevilleseaviewcemeteries.ca) + name)", "legal_name_is_published": true, "address": "1475 LORNEVILLE RD, Saint John, NB, E2M7H5", "address_is_the_invoice_address": false, "tax_number": "119024750RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (lornevilleseaviewcemeteries.ca) + name)", "language": "en-fr (bilingual body: federal / New Brunswick; use the language of its invoicing page: en)"}, "submit_to": {"email": "info@lornevilleseaviewcemeteries.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "paid to us within 28 days (as printed on https://lornevilleseaviewcemeteries.ca/wp-content/uploads/2023/08/LSCI-Plot-Pu
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); vendor legal name; AP phone or contact for follow-up
- **ap_grade**: C
- **ap_score**: 57
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; payment terms published; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["info@lornevilleseaviewcemeteries.ca (general)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://lornevilleseaviewcemeteries.ca/wp-content/uploads/2023/08/LSCI-Plot-Purchase-Terms-and-Conditions-1st-Adopted.pdf", "quote: \"entatives must notify us in writing and deliver it personally, send it by first class post to our registered address (below) or by email to info@lornevilleseavi\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: no DMARC record; SPF -all (hard fail); mail handled by self-hosted or other (mx1-us1.ppe-hosted.com)", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-CRA-03706"], "buyer_facts": ["address and phone: the buyer's own site, https://lornevilleseaviewcemeteries.ca/contact-us/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block 

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://lornevilleseaviewcemeteries.ca/wp-content/uploads/2023/08/LSCI-Plot-Purchase-Terms-and-Conditions-1st-Adopted.pdf | 2026-11-08 | ok | paid to us within 28 days |  |  |  |  |  |  | do not agree to such alternative arrangements, then we will cancel the Selected Rights of Interment and will return all monies you have paid to us within 28 days of notification of cancellation, following which we will h |  |

## Buyer site facts (org_extras, lornevilleseaviewcemeteries.ca)
- **status**: ok
- **pages**: 3
- **language**: en
- **logo_url**: https://lornevilleseaviewcemeteries.ca/wp-content/uploads/2016/02/LornevilleSeaview_LogoPhilip.png
- **logo_basis**: logo image on the site
- **domain**: lornevilleseaviewcemeteries.ca
- **key**: cra:119024750
- **name**: LORNEVILLE & SEAVIEW CEMETERIES INC.
- **website**: https://lornevilleseaviewcemeteries.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "3462 Lorneville Road, Saint John, NB E2M 7K9", "address_country": "CA", "address_url": "https://lornevilleseaviewcemeteries.ca/contact-us/", "address_method": "pattern", "address_quote": "Send Mail Map & Directions Seaview Cemetery 3462 Lorneville Road Saint John, NB E2M 7K9 Send Mail Map & Directions Donations We need your financial help to properly ma", "domain": "lornevilleseaviewcemeteries.ca", "key": "cra:119024750", "name": "LORNEVILLE & SEAVIEW CEMETERIES INC.", "website": "https://lornevilleseaviewcemeteries.ca/", "kind": "buyer", "date": "2026-11-03"}

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
| buyer | LORNEVILLE & SEAVIEW CEMETERIES INC. | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=LORNEVILLE%20%26%20SEAVIEW%20CEMETERIES%20INC. | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Canada Post | Q1032001 | official website on the organisation's domain (https://www.canadapost-postescanada.ca/) + name |  | Canada Post | Postes Canada | business; state-owned enterprise | business corporation | Canada | 1867-07-01 | Ottawa |
| b | LORNEVILLE & SEAVIEW CEMETERIES INC. |  |  |  |  |  |  |  |  |  |  |
| v | SOCIÉTÉ CANADIENNE DES POSTES | Q1032001 | official website on the organisation's domain (https://www.canadapost-postescanada.ca/) + name |  | Canada Post | Postes Canada | business; state-owned enterprise | business corporation | Canada | 1867-07-01 | Ottawa |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "cra:119024750",
 "ap_contact_team": {
  "emails": [
   "info@lornevilleseaviewcemeteries.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "info@lornevilleseaviewcemeteries.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://lornevilleseaviewcemeteries.ca/wp-content/uploads/2023/08/LSCI-Plot-Purchase-Terms-and-Conditions-1st-Adopted.pdf",
    "quote": "entatives must notify us in writing and deliver it personally, send it by first class post to our registered address (below) or by email to info@lornevilleseaviewcemeteries.ca before the funeral arrangements are publicly announced. We must have at least 3 working days notice in advance of",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "LORNEVILLE & SEAVIEW CEMETERIES INC.",
    "task_id": "CL-CRA-03706"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of www.lornevilleseaviewcemeteries.ca (11 pages, robots.txt respected), no AI, no search engine"
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
