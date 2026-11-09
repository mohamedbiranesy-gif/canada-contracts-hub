# S2-07 — GOSPEL FELLOWSHIP CHURCH ⇄ inferred: Manitoba Hydro

Stratum: **S2_complete_no_published_PO_rule** · pay on sight: yes — reference rule not published (quote the buyer's PO / order number when one is issued) · channel tier 2 · AP grade C · missing: (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: GOSPEL FELLOWSHIP CHURCH (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (gospelfellowshipchurch.ca) + name) — 860 MAIN ST, Steinbach, MB, R5G2H4 — buyer tax no. 118942317RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (gospelfellowshipchurch.ca) + name)
SUBMIT TO: finance@gospelfellowshipchurch.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Manitoba Hydro — 360 Portage Avenue, Winnipeg, MB R3C 0G8 | GST/HST 122063779 (GST/HST registration number printed by the organisation itself: https://www.hydro.mb.ca/cwd/BillInfo/PymtOptnsMybillE.htm, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of MB on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's
```

## Relationship
- **rank_group**: I3
- **data_quality_score**: 47
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: MEDIUM (typical supplier for this type of organisation)
- **relationship_detail**: GOSPEL FELLOWSHIP CHURCH (non-profit / association / cultural body, MB) — inferred: no record; the organisation's type and province make a Canadian supplier relationship near-certain: inferred: Manitoba Hydro | published by: inference from the buyer's type and province (no contract, payment or listing record) | vendor in Canada because: the vendor's own site, https://www.hydro.mb.ca/support/contact/: 'Mail Manitoba Hydro 360 Portage Avenue Winnipeg, MB Canada R3C 0G8' | status rule: inferred relationship (no record): medium confidence; the buyer is an organisation in Manitoba (province from its registered address in the CRA List of charities 2024 (open.canada.ca)); Manitoba Hydro is the only electri
- **how_relationship_was_found**: no record; tools/org_lists.py / osm_orgs.py / the crawlers placed the organisation in Canada by type and province; the vendor named is the Canada-located supplier such bodies almost always pay (see `vendor_country_basis`)
- **keys**: cra:118942317
- **tier**: I
- **grade**: 3

## Buyer
- **buyer**: GOSPEL FELLOWSHIP CHURCH
- **buyer_website**: https://gospelfellowshipchurch.ca
- **buyer_address**: 860 MAIN ST, Steinbach, MB, R5G2H4
- **buyer_legal_name_as_published**: GOSPEL FELLOWSHIP CHURCH (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (gospelfellowshipchurch.ca) + name)
- **buyer_bn_as_published**: 118942317RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (gospelfellowshipchurch.ca) + name)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 118942317RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_type**: non-profit / association / cultural body
- **buyer_sector**: non-profit
- **buyer_charity_status**: registered (listed) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (gospelfellowshipchurch.ca) + name)
- **buyer_charity_designation**: C; 0030
- **buyer_facts_provenance**: address: the buyer's record / buyer table; legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of MB on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: finance@gospelfellowshipchurch.ca
- **email_type**: finance/accounting dept or supplier-payment office
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); finance mailbox
- **email_evidence_url**: https://www.gospelfellowshipchurch.ca/
- **email_evidence_quote**: tyle="font-size:16px;" class="wixui-rich-text__text"><span style="text-decoration:underline;" class="wixui-rich-text__text"><a href="mailto:finance@gospelfellowshipchurch.ca?subject=Pre-authorized Bank Withdrawal" target="_self" class="wixui-rich-text__text"><span style="letter-spacing:nor
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: finance@gospelfellowshipchurch.ca (finance/accounting dept or supplier-payment office) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://www.gospelfellowshipchurch.ca/ | quote: "tyle="font-size:16px;" class="wixui-rich-text__text"><span style="text-decoration:underline;" class="wixui-rich-text__text"><a href="mailto:finance@gospelfellow" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: no DMARC record; no SPF record; mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-CRA-02507
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: no DMARC record; no SPF record; mail handled by Microsoft 365
- **dmarc_policy**: no DMARC record
- **dmarc_record**: no DMARC record at _dmarc.gospelfellowshipchurch.ca; confirmed by 8.8.8.8
- **spf_policy**: no SPF record
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 2
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: GOSPEL FELLOWSHIP CHURCH (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (gospelfellowshipchurch.ca) + name) — 860 MAIN ST, Steinbach, MB, R5G2H4 — buyer tax no. 118942317RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (gospelfellowshipchurch.ca) + name) ⏎ SUBMIT TO: finance@gospelfellowshipchurch.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Manitoba Hydro — 360 Portage Avenue, Winnipeg, MB R3C 0G8 | GST/HST 122063779 (GST/HST registration number printed by the organisation itself: https://www.hydro.mb.ca/cwd/BillInfo/PymtOptnsMybillE.htm, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of MB on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS
- **invoice_card_json**: {"bill_to": {"legal_name": "GOSPEL FELLOWSHIP CHURCH (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (gospelfellowshipchurch.ca) + name)", "legal_name_is_published": true, "address": "860 MAIN ST, Steinbach, MB, R5G2H4", "address_is_the_invoice_address": false, "tax_number": "118942317RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (gospelfellowshipchurch.ca) + name)", "language": "en"}, "submit_to": {"email": "finance@gospelfellowshipchurch.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-
- **invoice_readiness**: 6/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name; AP phone or contact for follow-up
- **ap_grade**: C
- **ap_score**: 61
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: inferred: Manitoba Hydro
- **vendor_address**: 360 Portage Avenue, Winnipeg, MB R3C 0G8
- **vendor_country_basis**: the vendor's own site, https://www.hydro.mb.ca/support/contact/: 'Mail Manitoba Hydro 360 Portage Avenue Winnipeg, MB Canada R3C 0G8'
- **vendor_bn9**: 122063779 (GST/HST registration number printed by the organisation itself: https://www.hydro.mb.ca/cwd/BillInfo/PymtOptnsMybillE.htm, 2026-11-08)
- **vendor_gst_hst_derived**: 122063779RT0001 (R122063779RT (printed in the older 'R' format))
- **vendor_website**: https://www.hydro.mb.ca
- **vendor_phone**: 1‑888‑624‑9376
- **vendor_contact_evidence_url**: https://www.hydro.mb.ca/support/contact/
- **vendor_logo_url**: https://www.hydro.mb.ca/mht/images/mb-hydro-logo-efl.svg
- **vendor_facts_provenance**: name and address: the record's vendor block (inference from the buyer's type and province (no contract, payment or listing record)); BN9: printed on the organisation's own page (https://www.hydro.mb.ca/cwd/BillInfo/PymtOptnsMybillE.htm); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); phone / role e-mails / logo: the vendor's own site, https://www.hydro.mb.ca/support/contact/ (tools/org_contacts.py, org_extras.py); website: https://www.hydro.mb.ca
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_bn_source**: printed on the organisation's own page (https://www.hydro.mb.ca/cwd/BillInfo/PymtOptnsMybillE.htm)

## Contract
- **contract_status**: inferred relationship (no record): medium confidence; the buyer is an organisation in Manitoba (province from its registered address in the CRA List of charities 2024 (open.canada.ca)); Manitoba Hydro is the only electricity distributor in Manitoba (The Manitoba Hydro Act; it took over Winnipeg Hydro in 2002); an organisation with premises there buys its electricity from it, unless its landlord pays it through the lease
- **source**: inference from the buyer's type and province (no contract, payment or listing record)
- **contracts_with_canadian_suppliers**: 0
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 118942317RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of MB on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (MB) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 122063779RT0001 (R122063779RT (printed in the older 'R' format))

## Pay on sight / grades
- **pay_on_sight**: yes — reference rule not published (quote the buyer's PO / order number when one is issued)
- **pay_on_sight_missing**: (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: GOSPEL FELLOWSHIP CHURCH (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (gospelfellowshipchurch.ca) + name) — 860 MAIN ST, Steinbach, MB, R5G2H4 — buyer tax no. 118942317RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (gospelfellowshipchurch.ca) + name) ⏎ SUBMIT TO: finance@gospelfellowshipchurch.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Manitoba Hydro — 360 Portage Avenue, Winnipeg, MB R3C 0G8 | GST/HST 122063779 (GST/HST registration number printed by the organisation itself: https://www.hydro.mb.ca/cwd/BillInfo/PymtOptnsMybillE.htm, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of MB on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS
- **invoice_card_json**: {"bill_to": {"legal_name": "GOSPEL FELLOWSHIP CHURCH (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (gospelfellowshipchurch.ca) + name)", "legal_name_is_published": true, "address": "860 MAIN ST, Steinbach, MB, R5G2H4", "address_is_the_invoice_address": false, "tax_number": "118942317RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (gospelfellowshipchurch.ca) + name)", "language": "en"}, "submit_to": {"email": "finance@gospelfellowshipchurch.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-
- **invoice_readiness**: 6/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name; AP phone or contact for follow-up
- **ap_grade**: C
- **ap_score**: 61
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["finance@gospelfellowshipchurch.ca (finance/accounting dept or supplier-payment office)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://www.gospelfellowshipchurch.ca/", "quote: \"tyle=\"font-size:16px;\" class=\"wixui-rich-text__text\"><span style=\"text-decoration:underline;\" class=\"wixui-rich-text__text\"><a href=\"mailto:finance@gospelfellow\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: no DMARC record; no SPF record; mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-CRA-02507"], "buyer_facts": ["address: the buyer's record / buyer table", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed"], "vendor_facts": ["name and address: the record's vendor block (inference from the buyer's type and province (no contract, payment or listing record))", "BN9: printed on the organisation's own page (https://www.hydro.mb.ca/cwd/BillInfo/PymtOptnsMybillE.htm)", "GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected", "not automated)", "phone / role e-mails / logo: the vendor's own site, https://www.hydro.mb.ca/support/contact

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.gospelfellowshipchurch.ca/ | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, domain unknown)
_not read_

## Buyer role mailboxes found on its site (org_contacts)
_not read_

## Vendor site facts (org_extras, hydro.mb.ca)
- **status**: ok
- **pages**: 5
- **language**: en
- **logo_url**: https://www.hydro.mb.ca/mht/images/mb-hydro-logo-efl.svg
- **logo_basis**: logo image in the site header
- **domain**: hydro.mb.ca
- **key**: b:d9bf0d3b2e8b3b19
- **name**: Manitoba Hydro
- **website**: https://hydro.mb.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Manitoba Hydro
- **legal_name_stated_url**: https://www.hydro.mb.ca/terms-of-use/
- **legal_name_stated_quote**: eral Related information Last updated August 11, 2021. This website domain is owned and operated by Manitoba Hydro. Agreement These terms form the entire agreement between you and Manitoba Hydro with respect to you
- **mentions**: {'payment_method': {'text': 'interact with the public on behalf of the corporation', 'url': 'https://www.hydro.mb.ca/accessibility/', 'quote': 'ent procedure was strengthened to include AMA standard requirements for relevant contracts that may interact with the public on behalf of the corporation. The internal “Accessibility at Manitoba Hydro" webpage is regularly reviewed and updated. It inclu'}}
- **linkedin_url**: https://www.linkedin.com/company/manitoba-hydro
- **tel_links**: 18886249376

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "Manitoba Hydro, 360 Portage Avenue, Winnipeg, MB, Canada R3C 0G8", "address_country": "CA", "address_url": "https://www.hydro.mb.ca/support/contact/", "address_method": "address-tag", "address_quote": ") TTY 1‑855‑287‑6809 Mail Manitoba Hydro 360 Portage Avenue Winnipeg, MB Canada R3C 0G8 About us Media Careers Engage with us Community Environment For landlords For b", "phone": "1‑888‑624‑9376", "phone_url": "https://www.hydro.mb.ca/support/contact/", "domain": "hydro.mb.ca", "key": "b:d9bf0d3b2e8b3b19", "name": "Manitoba Hydro", "website": "https://hydro.mb.ca/", "kind": "buyer", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | GOSPEL FELLOWSHIP CHURCH | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=GOSPEL%20FELLOWSHIP%20CHURCH | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Manitoba Hydro | Q3285979 | official website on the organisation's domain (http://www.hydro.mb.ca) + name |  | Manitoba Hydro | Manitoba Hydro | business; electricity supply company | state-owned enterprise | Canada | 1961-01-01 | Winnipeg |
| b | GOSPEL FELLOWSHIP CHURCH |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "cra:118942317",
 "ap_contact_team": {
  "emails": [
   "finance@gospelfellowshipchurch.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "finance@gospelfellowshipchurch.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.gospelfellowshipchurch.ca/",
    "quote": "tyle=\"font-size:16px;\" class=\"wixui-rich-text__text\"><span style=\"text-decoration:underline;\" class=\"wixui-rich-text__text\"><a href=\"mailto:finance@gospelfellowshipchurch.ca?subject=Pre-authorized Bank Withdrawal\" target=\"_self\" class=\"wixui-rich-text__text\"><span style=\"letter-spacing:nor",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "GOSPEL FELLOWSHIP CHURCH",
    "task_id": "CL-CRA-02507"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of gospelfellowshipchurch.ca (8 pages, robots.txt respected), no AI, no search engine"
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
