# S5-14 — Weyburn No. 67 ⇄ ICEsoft Technologies Canada Corp. (Voyent Alert!)

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 2 · AP grade C · missing: the vendor's GST/HST number (BN9); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Environment Ministry of Highways and Infrastructure Control Burn Number facebook Copyright — 1633 1st Ave. NE, Weyburn, SK S4H 3E7
SUBMIT TO: finance@rmweyburn.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: ICEsoft Technologies Canada Corp. (Voyent Alert!) — 100 King Street West, Suite 7210, Toronto, (Ontario), M5X 1E1 | GST/HST number not public
TAX: DERIVED: provincial government entity in Saskatchewan: a LISTED entity does not pay GST/HST at the point of purchase when an authorized official certifies the p | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Weyburn No. 67 (organisation (type not stated in the record), jurisdiction not stated) — active paid service of a Canada-HQ vendor seen on t
```

## Relationship
- **rank_group**: T3
- **data_quality_score**: 70
- **ship_ready**: yes (finance mailbox, not AP)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Weyburn No. 67 (organisation (type not stated in the record), jurisdiction not stated) — active paid service of a Canada-HQ vendor seen on the buyer's own site: ICEsoft Technologies Canada Corp. (Voyent Alert!) | awarded 2026-11-03 | published by: the buyer's own website (service of a Canada-HQ vendor in use) | record: https://www.rmweyburn.ca/ | vendor in Canada because: service of a Canada-HQ vendor seen on the buyer's own site (tech)=ources Admin Support About Voyent Alert! Product Features Resources Admin Support About Voyent Alert! Contact Suite 340 600 Crowfoot Crescent NW Calgary,  | status rule: active service seen on the buyer's own site (2026-11-03): Canada-HQ vendor ICEsoft Technologies Canada Corp. (Voyent Alert!)
- **how_relationship_was_found**: tools/tech_portals2.py / tech_relationships.py found the buyer's own web property running the Canada-HQ vendor's paid platform (portal host or embedded service), dated by the page read
- **keys**: lead:9cbfa674939b5eb0
- **tier**: T
- **grade**: 3
- **records_with_this_vendor**: 1 (relationship record: the buyer's own website (service of a Canada-HQ vendor in use); 0 in the contract dataset)

## Buyer
- **buyer**: Weyburn No. 67
- **buyer_website**: https://rmweyburn.ca/
- **buyer_address**: 1633 1st Ave. NE, Weyburn, SK S4H 3E7
- **buyer_contact_evidence_url**: https://www.rmweyburn.ca/contact/
- **buyer_legal_name_as_published**: Environment Ministry of Highways and Infrastructure Control Burn Number facebook Copyright
- **buyer_logo_url**: https://www.rmweyburn.ca/wp-content/uploads/2022/12/cropped-RMWeyburn-Logo-2-150x150.png
- **buyer_website_status**: site answers
- **buyer_type**: government ministry / agency (from the organisation's name / web domain)
- **buyer_sector**: government: provincial / federal
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q7990301; rural municipality of Canada
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.rmweyburn.ca/contact/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: provincial government entity in Saskatchewan: a LISTED entity does not pay GST/HST at the point of purchase when an authorized official certifies the purchase — ask for the exemption certificate or certification clause before invoicing without tax — GST/HST Memorandum 18-2 para. 24 (https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Listed entities in Manitoba, Saskatchewan, Alberta, the Northwest Territories and Yukon do not pay the GST/HST on purchases of taxable property and services, provided that an authorized official of the listed entity provides sufficient evidence"); derived from buyer type and province, not published by the buyer; whether this body is a listed entity is not verified
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: finance@rmweyburn.ca
- **email_type**: finance/accounting dept or supplier-payment office
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); finance mailbox
- **email_evidence_url**: https://www.rmweyburn.ca/contact/
- **email_evidence_quote**: Email for E-transfers: finance@rmweyburn.ca R.M. Map May 2025 Contact Us Quick Links City of Weyburn Weyburn Economic Development Weyburn Review Townfolio SARM Southeast Reg
- **email_evidence_context**: t Alert Weyburn Utility Board WUB Voyent Alerts Handy Information Billing New Users Reports Contact Phone: (306) 842-2314 Fax: (306) 842-1002 Address: 1633 1st Ave. NE Weyburn, SK S4H 3E7 Email for Inquiries: rm.67@sasktel.net Email for E-transfers: finance@rmweyburn.ca R.M. Map May 2025 Contact Us Quick Links City of Weyburn Weyburn Economic Development Weyburn Review Townfolio SARM Southeast Regional Library Highway Hotline Ministry of Agriculture Ministry of Environment Ministry of Highways and Infrastructure Co (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: finance@rmweyburn.ca (finance/accounting dept or supplier-payment office) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://www.rmweyburn.ca/contact/ | quote: "Email for E-transfers: finance@rmweyburn.ca R.M. Map May 2025 Contact Us Quick Links City of Weyburn Weyburn Economic Development Weyburn Review Townfolio SARM " | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: no DMARC record; SPF ~all (soft fail); mail handled by self-hosted or other (mx.rmweyburn.ca) | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-05489
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: no DMARC record; SPF ~all (soft fail); mail handled by self-hosted or other (mx.rmweyburn.ca)
- **dmarc_policy**: no DMARC record
- **dmarc_record**: no DMARC record at _dmarc.rmweyburn.ca; confirmed by 8.8.8.8
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 include:spf.ehosting.ca ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_phone**: (306) 842-2314 (as printed on https://www.rmweyburn.ca/contact/, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "ap_phone": "(306) 842-2314 (as printed on https://www.rmweyburn.ca/contact/, re-read 2026-11-08)"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 2
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Environment Ministry of Highways and Infrastructure Control Burn Number facebook Copyright — 1633 1st Ave. NE, Weyburn, SK S4H 3E7 ⏎ SUBMIT TO: finance@rmweyburn.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: ICEsoft Technologies Canada Corp. (Voyent Alert!) — 100 King Street West, Suite 7210, Toronto, (Ontario), M5X 1E1 | GST/HST number not public ⏎ TAX: DERIVED: provincial government entity in Saskatchewan: a LISTED entity does not pay GST/HST at the point of purchase when an authorized official certifies the p | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Weyburn No. 67 (organisation (type not stated in the record), jurisdiction not stated) — active paid service of a Canada-HQ vendor seen on t
- **invoice_card_json**: {"bill_to": {"legal_name": "Environment Ministry of Highways and Infrastructure Control Burn Number facebook Copyright", "legal_name_is_published": true, "address": "1633 1st Ave. NE, Weyburn, SK S4H 3E7", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "finance@rmweyburn.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: provincial government entity in Saskatchewan: a LISTED entity does not pay GST/HST at the point of purchase when an authorized official certifies the purchase —", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (SK)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "", "vendor_qst": ""}, "vendor_identity": {"legal_name": "ICEsoft Technologies Canada Corp. (Voyent Alert!)", "bn9": "", "neq": "", "remit_address": "100 King Street West, Suite 7210, Toronto, (Ontario), M5X 1E1"}, "follow_up": {"ap_phone": "(306) 842-2314 (as printed on h
- **invoice_readiness**: 6/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number; vendor legal name
- **ap_grade**: C
- **ap_score**: 63
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: ICEsoft Technologies Canada Corp. (Voyent Alert!)
- **vendor_address**: 100 King Street West, Suite 7210, Toronto, (Ontario), M5X 1E1
- **vendor_country_basis**: service of a Canada-HQ vendor seen on the buyer's own site (tech)=ources Admin Support About Voyent Alert! Product Features Resources Admin Support About Voyent Alert! Contact Suite 340 600 Crowfoot Crescent NW Calgary, AB, T3G 0B4 1-877-263-3822 product.sales@icesoft.com Social Co
- **vendor_website**: https://thecse.com/
- **vendor_emails**: info@thecse.com
- **vendor_contact_evidence_url**: https://thecse.com/fr/contact-us/
- **vendor_logo_url**: https://thecse.com/apple-touch-icon.png
- **vendor_website_basis**: found by a web search, confirmed by reading the site on 2026-11-08: https://thecse.com/listings/icesoft-technologies-canada-corp/ (ICEsoft Technologies Canada Corp. | The Canadian Securities Exchange (CSE) Search Symbol, Name or Keyword en en Quote About Disclosure ISFT 0.00% ISFT 0.00% ICE)
- **vendor_facts_provenance**: name and address: the record's vendor block (the buyer's own website (service of a Canada-HQ vendor in use)); phone / role e-mails / logo: the vendor's own site, https://thecse.com/fr/contact-us/ (tools/org_contacts.py, org_extras.py); website: https://thecse.com/
- **vendor_concentration_top_share**: no dataset record for this pair / buyer

## Contract
- **contract_status**: active service seen on the buyer's own site (2026-11-03): Canada-HQ vendor ICEsoft Technologies Canada Corp. (Voyent Alert!)
- **award_date**: 2026-11-03
- **contract_link**: https://www.rmweyburn.ca/
- **source**: the buyer's own website (service of a Canada-HQ vendor in use)
- **contracts_with_canadian_suppliers**: 2
- **records_with_this_vendor**: 1 (relationship record: the buyer's own website (service of a Canada-HQ vendor in use); 0 in the contract dataset)
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: provincial government entity in Saskatchewan: a LISTED entity does not pay GST/HST at the point of purchase when an authorized official certifies the purchase — ask for the exemption certificate or certification clause before invoicing without tax — GST/HST Memorandum 18-2 para. 24 (https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Listed entities in Manitoba, Saskatchewan, Alberta, the Northwest Territories and Yukon do not pay the GST/HST on purchases of taxable property and services, provided that an authorized official of the listed entity provides sufficient evidence"); derived from buyer type and province, not published by the buyer; whether this body is a listed entity is not verified
- **tax_rate_indicative_derived**: GST 5% (SK) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Environment Ministry of Highways and Infrastructure Control Burn Number facebook Copyright — 1633 1st Ave. NE, Weyburn, SK S4H 3E7 ⏎ SUBMIT TO: finance@rmweyburn.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: ICEsoft Technologies Canada Corp. (Voyent Alert!) — 100 King Street West, Suite 7210, Toronto, (Ontario), M5X 1E1 | GST/HST number not public ⏎ TAX: DERIVED: provincial government entity in Saskatchewan: a LISTED entity does not pay GST/HST at the point of purchase when an authorized official certifies the p | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Weyburn No. 67 (organisation (type not stated in the record), jurisdiction not stated) — active paid service of a Canada-HQ vendor seen on t
- **invoice_card_json**: {"bill_to": {"legal_name": "Environment Ministry of Highways and Infrastructure Control Burn Number facebook Copyright", "legal_name_is_published": true, "address": "1633 1st Ave. NE, Weyburn, SK S4H 3E7", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "finance@rmweyburn.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: provincial government entity in Saskatchewan: a LISTED entity does not pay GST/HST at the point of purchase when an authorized official certifies the purchase —", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (SK)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "", "vendor_qst": ""}, "vendor_identity": {"legal_name": "ICEsoft Technologies Canada Corp. (Voyent Alert!)", "bn9": "", "neq": "", "remit_address": "100 King Street West, Suite 7210, Toronto, (Ontario), M5X 1E1"}, "follow_up": {"ap_phone": "(306) 842-2314 (as printed on h
- **invoice_readiness**: 6/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number; vendor legal name
- **ap_grade**: C
- **ap_score**: 63
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["finance@rmweyburn.ca (finance/accounting dept or supplier-payment office)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://www.rmweyburn.ca/contact/", "quote: \"Email for E-transfers: finance@rmweyburn.ca R.M. Map May 2025 Contact Us Quick Links City of Weyburn Weyburn Economic Development Weyburn Review Townfolio SARM \"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: no DMARC record; SPF ~all (soft fail); mail handled by self-hosted or other (mx.rmweyburn.ca)", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-05489"], "buyer_facts": ["address and phone: the buyer's own site, https://www.rmweyburn.ca/contact/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (the buyer's own website (service of a Canada-HQ vendor in use))", "phone / role e-mails / logo: the vendor's own site, https://thecse.com/fr/contact-us/ (tools/org_contacts.py, org_extras.py)", "website: https://thecse

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.rmweyburn.ca/contact/ | 2026-11-08 | ok |  |  |  | (306) 842-2314 |  |  |  |  |  |

## Buyer site facts (org_extras, rmweyburn.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: Environment Ministry of Highways and Infrastructure Control Burn Number facebook Copyright
- **legal_name_url**: https://www.rmweyburn.ca/
- **legal_name_quote**: eview Townfolio SARM Southeast Regional Library Highway Hotline Ministry of Agriculture Ministry of Environment Ministry of Highways and Infrastructure Control Burn Number facebook Copyright © 2024 — RM of Weyburn No. 67. All Rights Reserved Designed by WPZOOM
- **logo_url**: https://www.rmweyburn.ca/wp-content/uploads/2022/12/cropped-RMWeyburn-Logo-2-150x150.png
- **logo_basis**: logo image in the site header
- **domain**: rmweyburn.ca
- **key**: lead:9cbfa674939b5eb0
- **name**: Weyburn No. 67
- **website**: https://rmweyburn.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: RM of Weyburn No. 67
- **jsonld_logo**: https://www.rmweyburn.ca/wp-content/uploads/2022/12/cropped-RMWeyburn-Logo-2.png
- **jsonld_url**: https://www.rmweyburn.ca/
- **jsonld_quote**: {"@context":"https:\/\/schema.org","@graph":[{"@type":"BreadcrumbList","@id":"https:\/\/www.rmweyburn.ca\/#breadcrumblist","itemListElement":[{"@type":"ListItem","@id":"https:\/\/www.rmweyburn.ca#listItem","position":1,"name":"Home"}]},{"@type":"Organization","@id":"https:\/\/www.rmweyburn.ca\/#orga
- **jsonld_page**: https://www.rmweyburn.ca/
- **legal_name_stated**: City of Weyburn
- **legal_name_stated_url**: https://www.rmweyburn.ca/about/
- **legal_name_stated_quote**: sified and rapidly growing rural municipality situated in south east Saskatchewan. It surrounds the City of Weyburn and Village of McTaggart and includes the Organized Hamlet of North Weyburn. The municipality compr
- **mentions**: {'payment_method': {'text': 'E-transfers: finance@rmweyburn', 'url': 'https://www.rmweyburn.ca/contact/', 'quote': '1002 Address: 1633 1st Ave. NE Weyburn, SK S4H 3E7 Email for Inquiries: rm.67@sasktel.net Email for E-transfers: finance@rmweyburn.ca R.M. Map May 2025 Contact Us Quick Links City of Weyburn Weyburn Economic Development Weyburn Re'}}

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "1633 1st Ave. NE, Weyburn, SK S4H 3E7", "address_country": "CA", "address_url": "https://www.rmweyburn.ca/contact/", "address_method": "pattern", "address_quote": "Phone: (306) 842-2314 Fax: (306) 842-1002 Address: 1633 1st Ave. NE Weyburn, SK S4H 3E7 Email for Inquiries: rm.67@sasktel.net Email for E-transfers: finance@rmweyburn", "domain": "rmweyburn.ca", "key": "lead:9cbfa674939b5eb0", "name": "Weyburn No. 67", "website": "https://rmweyburn.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, thecse.com)
- **status**: ok
- **pages**: 4
- **v**: 2
- **linkedin_url**: https://www.linkedin.com/company/canadian-securities-exchange
- **language**: fr
- **legal_name**: CNSX Markets Inc
- **legal_name_url**: https://thecse.com/fr/
- **legal_name_quote**: Pender Street, Suite 305 Vancouver, (Colombie-Britannique), V6E 2M6 Communiquer avec nous fr © 2026 CNSX Markets Inc. Tous droits réservés. Modalités du site Énoncé sur la protection des renseignements personnels Acc
- **logo_url**: https://thecse.com/apple-touch-icon.png
- **logo_basis**: site icon (apple-touch-icon)
- **domain**: thecse.com
- **key**: vendor:ICEsoft Technologies Canada Corp. (Voyent Alert!)
- **name**: ICEsoft Technologies Canada Corp. (Voyent Alert!)
- **website**: https://thecse.com/
- **kind**: vendor
- **date**: 2026-11-09

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "address": "100 King Street West, Suite 7210, Toronto, (Ontario), M5X 1E1", "address_country": "CA", "address_url": "https://thecse.com/fr/contact-us/", "address_method": "address-tag", "address_quote": "416-572-4160 (télécopieur) 100 King Street West, Suite 7210 Toronto, (Ontario), M5X 1E1 Bureau de Vancouver 604-331-1213 604-687-1188 (télécopieur) 1095 West Pender St", "emails": "info@thecse.com", "emails_url": "https://thecse.com/fr/contact-us/", "domain": "thecse.com", "key": "vendor:ICEsoft Technologies Canada Corp. (Voyent Alert!)", "name": "ICEsoft Technologies Canada Corp. (Voyent Alert!)", "website": "https://thecse.com/", "kind": "vendor", "date": "2026-11-09"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Weyburn No. 67 | Q7990301 | official website on the organisation's domain (http://rmweyburn.ca) + name |  | Weyburn No. 67 |  | rural municipality of Canada |  | Canada |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:9cbfa674939b5eb0",
 "ap_contact_team": {
  "emails": [
   "finance@rmweyburn.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "finance@rmweyburn.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.rmweyburn.ca/contact/",
    "quote": "Email for E-transfers: finance@rmweyburn.ca R.M. Map May 2025 Contact Us Quick Links City of Weyburn Weyburn Economic Development Weyburn Review Townfolio SARM Southeast Reg",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Weyburn No. 67",
    "task_id": "CL-LD-05489"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of rmweyburn.ca (18 pages, robots.txt respected), no AI, no search engine"
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

- the vendor's GST/HST number (BN9)
- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
