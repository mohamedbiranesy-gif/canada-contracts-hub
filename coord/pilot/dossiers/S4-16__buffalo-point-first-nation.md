# S4-16 — Buffalo Point First Nation ⇄ inferred: Manitoba Hydro

Stratum: **S4_routed_company_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Buffalo Point Resort Centre (schema.org JSON-LD Organization name on https://buffalopoint.ca/) — 20 Buffalo Point Road, Buffalo Point, Manitoba, R0A 2W0, Canada (schema.org JSON-LD PostalAddress on https://buffalopoint.ca/)
SUBMIT TO: reception@buffalopoint.mb.ca (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Manitoba Hydro — 360 Portage Avenue, Winnipeg, MB R3C 0G8 | GST/HST 122063779 (GST/HST registration number printed by the organisation itself: https://www.hydro.mb.ca/cwd/BillInfo/PymtOptnsMybillE.htm, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: provincial government entity in Manitoba: a LISTED entity does not pay GST/HST at the point of purchase when an authorized official certifies the purch | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Buffalo Point First Nation (First Nation / Indigenous government, MB) — inferred: no record; the organisation's type and province make a Can
```

## Relationship
- **rank_group**: I1
- **data_quality_score**: 30
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 6
- **reverify_due**: no
- **inference_confidence**: HIGH (statutory or sole-provider relationship for this type of organisation)
- **relationship_detail**: Buffalo Point First Nation (First Nation / Indigenous government, MB) — inferred: no record; the organisation's type and province make a Canadian supplier relationship near-certain: inferred: Manitoba Hydro | published by: inference from the buyer's type and province (no contract, payment or listing record) | vendor in Canada because: the vendor's own site, https://www.hydro.mb.ca/support/contact/: 'Mail Manitoba Hydro 360 Portage Avenue Winnipeg, MB Canada R3C 0G8' | status rule: inferred relationship (no record): high confidence; the buyer is an institution (school, college, university, health or government body) in Manitoba (province from its domain buffalopoint.mb.ca); Manitoba Hydro is the on
- **how_relationship_was_found**: no record; tools/org_lists.py / osm_orgs.py / the crawlers placed the organisation in Canada by type and province; the vendor named is the Canada-located supplier such bodies almost always pay (see `vendor_country_basis`)
- **keys**: lead:0c1eb6157441812e
- **tier**: I
- **grade**: 1

## Buyer
- **buyer**: Buffalo Point First Nation
- **buyer_website**: https://buffalopoint.mb.ca
- **buyer_address**: 20 Buffalo Point Road, Buffalo Point, Manitoba, R0A 2W0, Canada (schema.org JSON-LD PostalAddress on https://buffalopoint.ca/)
- **buyer_phone**: 204-437-2133
- **buyer_contact_evidence_url**: https://buffalopoint.ca/contact-us/
- **buyer_legal_name_as_published**: Buffalo Point Resort Centre (schema.org JSON-LD Organization name on https://buffalopoint.ca/)
- **buyer_logo_url**: https://buffalopoint.gumlet.io/wp-content/uploads/2018/09/BPoint-logo.jpg?compress=true
- **buyer_website_status**: site answers
- **buyer_type**: First Nation / Indigenous government
- **buyer_sector**: government: provincial / federal
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q1002024; First Nation band
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://buffalopoint.ca/contact-us/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: provincial government entity in Manitoba: a LISTED entity does not pay GST/HST at the point of purchase when an authorized official certifies the purchase — ask for the exemption certificate or certification clause before invoicing without tax — GST/HST Memorandum 18-2 para. 24 (https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Listed entities in Manitoba, Saskatchewan, Alberta, the Northwest Territories and Yukon do not pay the GST/HST on purchases of taxable property and services, provided that an authorized official of the listed entity provides sufficient evidence"); derived from buyer type and province, not published by the buyer; whether this body is a listed entity is not verified
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: reception@buffalopoint.mb.ca
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://www.buffalopoint-firstnation.ca/
- **email_evidence_quote**: Resort Lake of the Sandhills Golf Course Buffalo Point First Nation PO Box 1037 Buffalo Point, Manitoba R0A 2W0 Phone: 204-437-2133 E-Mail: reception@buffalopoint.mb.ca Copyright © 2026 Buffalo Point First Nation All rights reserved.
- **email_evidence_context**: Tour | Contact Buffalo Point First Nation Buffalo Point First Nation Visit our commercial sites Buffalo Point Resort Lake of the Sandhills Golf Course Buffalo Point First Nation PO Box 1037 Buffalo Point, Manitoba R0A 2W0 Phone: 204-437-2133 E-Mail: reception@buffalopoint.mb.ca Copyright © 2026 Buffalo Point First Nation All rights reserved. (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: reception@buffalopoint.mb.ca (general) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-03 | page: https://www.buffalopoint-firstnation.ca/ | quote: "Resort Lake of the Sandhills Golf Course Buffalo Point First Nation PO Box 1037 Buffalo Point, Manitoba R0A 2W0 Phone: 204-437-2133 E-Mail: reception@buffalopoi" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by self-hosted or other (mail.datatracker.ca) | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-SM-00006
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by self-hosted or other (mail.datatracker.ca)
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none
- **dmarc_record_domain**: buffalopoint.mb.ca
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 include:_spf.datatracker.ca ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Buffalo Point Resort Centre (schema.org JSON-LD Organization name on https://buffalopoint.ca/) — 20 Buffalo Point Road, Buffalo Point, Manitoba, R0A 2W0, Canada (schema.org JSON-LD PostalAddress on https://buffalopoint.ca/) ⏎ SUBMIT TO: reception@buffalopoint.mb.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Manitoba Hydro — 360 Portage Avenue, Winnipeg, MB R3C 0G8 | GST/HST 122063779 (GST/HST registration number printed by the organisation itself: https://www.hydro.mb.ca/cwd/BillInfo/PymtOptnsMybillE.htm, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: provincial government entity in Manitoba: a LISTED entity does not pay GST/HST at the point of purchase when an authorized official certifies the purch | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Buffalo Point First Nation (First Nation / Indigenous government, MB) — inferred: no record; the organisation's type and province make a Can
- **invoice_card_json**: {"bill_to": {"legal_name": "Buffalo Point Resort Centre (schema.org JSON-LD Organization name on https://buffalopoint.ca/)", "legal_name_is_published": true, "address": "20 Buffalo Point Road, Buffalo Point, Manitoba, R0A 2W0, Canada (schema.org JSON-LD PostalAddress on https://buffalopoint.ca/)", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "reception@buffalopoint.mb.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: provincial government entity in Manitoba: a LISTED entity does not pay GST/HST at the point of purchase when an authorized official certifies the purchase — ask", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (MB)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "122063779RT0001 (R122063779RT (printed in the older 'R' format))", "vendor_qst": ""}, "vendor_identity": {"legal_name": "inferred: Manitoba Hydro", "bn9": "122063779 (GST/HST registration number printed by the orga
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
- **contract_status**: inferred relationship (no record): high confidence; the buyer is an institution (school, college, university, health or government body) in Manitoba (province from its domain buffalopoint.mb.ca); Manitoba Hydro is the only electricity distributor in Manitoba (The Manitoba Hydro Act; it took over Winnipeg Hydro in 2002); it pays electricity for the buildings it operates
- **source**: inference from the buyer's type and province (no contract, payment or listing record)
- **contracts_with_canadian_suppliers**: 0
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: provincial government entity in Manitoba: a LISTED entity does not pay GST/HST at the point of purchase when an authorized official certifies the purchase — ask for the exemption certificate or certification clause before invoicing without tax — GST/HST Memorandum 18-2 para. 24 (https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Listed entities in Manitoba, Saskatchewan, Alberta, the Northwest Territories and Yukon do not pay the GST/HST on purchases of taxable property and services, provided that an authorized official of the listed entity provides sufficient evidence"); derived from buyer type and province, not published by the buyer; whether this body is a listed entity is not verified
- **tax_rate_indicative_derived**: GST 5% (MB) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 122063779RT0001 (R122063779RT (printed in the older 'R' format))

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Buffalo Point Resort Centre (schema.org JSON-LD Organization name on https://buffalopoint.ca/) — 20 Buffalo Point Road, Buffalo Point, Manitoba, R0A 2W0, Canada (schema.org JSON-LD PostalAddress on https://buffalopoint.ca/) ⏎ SUBMIT TO: reception@buffalopoint.mb.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Manitoba Hydro — 360 Portage Avenue, Winnipeg, MB R3C 0G8 | GST/HST 122063779 (GST/HST registration number printed by the organisation itself: https://www.hydro.mb.ca/cwd/BillInfo/PymtOptnsMybillE.htm, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: provincial government entity in Manitoba: a LISTED entity does not pay GST/HST at the point of purchase when an authorized official certifies the purch | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Buffalo Point First Nation (First Nation / Indigenous government, MB) — inferred: no record; the organisation's type and province make a Can
- **invoice_card_json**: {"bill_to": {"legal_name": "Buffalo Point Resort Centre (schema.org JSON-LD Organization name on https://buffalopoint.ca/)", "legal_name_is_published": true, "address": "20 Buffalo Point Road, Buffalo Point, Manitoba, R0A 2W0, Canada (schema.org JSON-LD PostalAddress on https://buffalopoint.ca/)", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "reception@buffalopoint.mb.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: provincial government entity in Manitoba: a LISTED entity does not pay GST/HST at the point of purchase when an authorized official certifies the purchase — ask", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (MB)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "122063779RT0001 (R122063779RT (printed in the older 'R' format))", "vendor_qst": ""}, "vendor_identity": {"legal_name": "inferred: Manitoba Hydro", "bn9": "122063779 (GST/HST registration number printed by the orga
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["reception@buffalopoint.mb.ca (general)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-03", "page: https://www.buffalopoint-firstnation.ca/", "quote: \"Resort Lake of the Sandhills Golf Course Buffalo Point First Nation PO Box 1037 Buffalo Point, Manitoba R0A 2W0 Phone: 204-437-2133 E-Mail: reception@buffalopoi\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by self-hosted or other (mail.datatracker.ca)", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-SM-00006"], "buyer_facts": ["address and phone: the buyer's own site, https://buffalopoint.ca/contact-us/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (inference from the buyer's type and province (no contract, payment or listing record))", "BN9: printed on the organisation's own page (https://www.hydro.mb.ca/cwd/BillInfo/PymtOptnsMybillE.htm)", "GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected", "not automated)", "phone / role e-mails / logo: the vendor'

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.buffalopoint-firstnation.ca/ | 2026-11-08 | ok |  |  |  | 204-437-2133 | PO Box 1037 Buffalo Point, Manitoba R0A 2W0 |  |  |  |  |

## Buyer site facts (org_extras, buffalopoint.mb.ca)
- **status**: ok
- **pages**: 3
- **v**: 2
- **jsonld_type**: Place
- **jsonld_name**: Buffalo Point Resort Centre
- **jsonld_address**: 20 Buffalo Point Road, Buffalo Point, Manitoba, R0A 2W0, Canada
- **jsonld_phone**: 2044372777
- **jsonld_quote**: [{"@context":"http://schema.org","@type":"Event","name":"JETS GAMEDAY AT THE BISTRO!","description":"&lt;p&gt;JETS GAMEDAY AT THE BISTRO! Get ready for puck drop! \ud83c\udfd2 Join us at the Fire and Water Bistro / Island Green Lounge for our rotating Winnipeg Jets Gameday Specials&hellip;&lt;/p&gt;
- **jsonld_page**: https://buffalopoint.ca/
- **language**: en
- **logo_url**: https://buffalopoint.gumlet.io/wp-content/uploads/2018/09/BPoint-logo.jpg?compress=true
- **logo_basis**: logo image on the site
- **domain**: buffalopoint.mb.ca
- **key**: lead:0c1eb6157441812e
- **name**: Buffalo Point First Nation
- **website**: https://buffalopoint.mb.ca/
- **kind**: buyer
- **date**: 2026-11-08

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "1037 Buffalo Point, Manitoba Canada R0A 2W0", "address_country": "CA", "address_url": "https://buffalopoint.ca/contact-us/", "address_method": "pattern", "address_quote": "r feedback is important to us. Address: Box 1037 Buffalo Point, Manitoba Canada R0A 2W0 Accommodations & General Inquiries: 204-437-2777 Message This Department [conta", "phone": "204-437-2133", "phone_url": "https://buffalopoint.ca/contact-us/", "domain": "buffalopoint.mb.ca", "key": "lead:0c1eb6157441812e", "name": "Buffalo Point First Nation", "website": "https://buffalopoint.mb.ca/", "kind": "buyer", "date": "2026-11-03"}

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
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Manitoba Hydro | Q3285979 | official website on the organisation's domain (http://www.hydro.mb.ca) + name |  | Manitoba Hydro | Manitoba Hydro | business; electricity supply company | state-owned enterprise | Canada | 1961-01-01 | Winnipeg |
| b | Buffalo Point First Nation | Q1002024 | exact name match + country + organisation claims |  | Buffalo Point First Nation |  | First Nation band |  | Canada |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:0c1eb6157441812e",
 "ap_contact_team": {
  "emails": [
   "reception@buffalopoint.mb.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "reception@buffalopoint.mb.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.buffalopoint-firstnation.ca/",
    "quote": "Resort Lake of the Sandhills Golf Course Buffalo Point First Nation PO Box 1037 Buffalo Point, Manitoba R0A 2W0 Phone: 204-437-2133 E-Mail: reception@buffalopoint.mb.ca Copyright © 2026 Buffalo Point First Nation All rights reserved.",
    "retrieved_date": "2026-11-03",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Buffalo Point First Nation",
    "task_id": "CL-SM-00006"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of www.buffalopoint-firstnation.ca (8 pages, robots.txt respected), no AI, no search engine"
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
