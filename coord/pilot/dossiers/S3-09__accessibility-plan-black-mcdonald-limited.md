# S3-09 — Accessibility Plan Black & Mcdonald Limited ⇄ Roberts Onsite Inc

Stratum: **S3_routed_public_body_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Accessibility Plan Black & Mcdonald Limited (stated on https://blackandmcdonald.com/accessibility/) — 2 Bloor Street East, Suite 2100, Toronto, ON M4W 1A8
SUBMIT TO: info@blackandmcdonald.com (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: ROBERTS ONSITE INC. (as registered: Canada's Business Registries, ON 1836813, 2026-11-08) — 209 Manitou Drive, Kitchener, ON, N2C 1L4, Canada | GST/HST 893346262 (Canada's Business Registries, ON 1836813, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Multiple Electric Vehicle Charger Installations | Roberts Onsite
```

## Relationship
- **rank_group**: E1
- **data_quality_score**: 37
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Accessibility Plan Black & Mcdonald Limited (organisation (type not stated in the record), jurisdiction not stated) — linked from the Canada-located vendor's site (weakest listed relationship): Roberts Onsite Inc | subject: Multiple Electric Vehicle Charger Installations | Roberts Onsite | published by: the Canada-located vendor's own website | record: https://robertsonsite.ca/project-profiles/multiple-electric-vehicle-charger-installations | vendor in Canada because: vendor located in Canada (v)=robertsonsite.ca | status rule: linked from a page of the Canada-located vendor's site (not a client page)
- **how_relationship_was_found**: tools/provider_mentions.py / news_match.py found the buyer linked from the vendor's own site or release
- **keys**: lead:3ef1d665f2c83904
- **tier**: E
- **grade**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: Accessibility Plan Black & Mcdonald Limited
- **buyer_website**: https://blackandmcdonald.com/
- **buyer_address**: 2 Bloor Street East, Suite 2100, Toronto, ON M4W 1A8
- **buyer_contact_evidence_url**: https://blackandmcdonald.com/contact/
- **buyer_legal_name_as_published**: Accessibility Plan Black & Mcdonald Limited (stated on https://blackandmcdonald.com/accessibility/)
- **buyer_logo_url**: https://blackandmcdonald.com/
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/black-
- **buyer_type**: company (private sector) (from the organisation's name / web domain)
- **buyer_sector**: private sector
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://blackandmcdonald.com/contact/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: info@blackandmcdonald.com
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://blackandmcdonald.com/fr/contact/
- **email_evidence_quote**: inlinescript" class="nitropack-inline-script">var addresses=[["2 Bloor Street East, Suite 2100, <br> Toronto, ON M4W 1A8","(416) 920-5100","info@blackandmcdonald.com",43.6705987,-79.3865914],["26A Dundee Avenue, <br> Mount Pearl, NL A1N 4R7","(709) 747-1406","",47.5164112,-52.8418526],["19
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: info@blackandmcdonald.com (general) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://blackandmcdonald.com/fr/contact/ | quote: "inlinescript" class="nitropack-inline-script">var addresses=[["2 Bloor Street East, Suite 2100, <br> Toronto, ON M4W 1A8","(416) 920-5100","info@blackandmcdonal" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Cisco | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-02619
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Cisco
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject; pct=100; fo=1; ri=3600; rua=mailto:a98e94ab@inbox.ondmarc.com; ruf=mailto:a98e94ab@inbox.ondmarc.com;
- **dmarc_record_domain**: blackandmcdonald.com
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 mx exists:%{i}.spf.hc671-35.ca.iphmx.com include:spf.protection.outlook.com include:amazonses.com include:342649528.spf02.hubspotemail.net ip4:207.35.3.114 ip4:207.35.238.225 ip4:13.111.68.98 ip4:70.25.134.16 ip4:70.28.250.215 ip4:184.151.35.24 ip4:23.249.209.24 ip4:23.249.209.23 ip4:216.71.1
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Accessibility Plan Black & Mcdonald Limited (stated on https://blackandmcdonald.com/accessibility/) — 2 Bloor Street East, Suite 2100, Toronto, ON M4W 1A8 ⏎ SUBMIT TO: info@blackandmcdonald.com (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: ROBERTS ONSITE INC. (as registered: Canada's Business Registries, ON 1836813, 2026-11-08) — 209 Manitou Drive, Kitchener, ON, N2C 1L4, Canada | GST/HST 893346262 (Canada's Business Registries, ON 1836813, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Multiple Electric Vehicle Charger Installations | Roberts Onsite
- **invoice_card_json**: {"bill_to": {"legal_name": "Accessibility Plan Black & Mcdonald Limited (stated on https://blackandmcdonald.com/accessibility/)", "legal_name_is_published": true, "address": "2 Bloor Street East, Suite 2100, Toronto, ON M4W 1A8", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "info@blackandmcdonald.com", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 13% (Ontario)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "893346262RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "ROBERTS ONSITE INC. (as registered: Canada's Business Registries, ON 1836813, 2026-11-08)", "bn9": "893346262 (Canada's Business Registries, ON 1836
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; AP phone or contact for follow-up
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: Roberts Onsite Inc
- **vendor_legal_name**: ROBERTS ONSITE INC. (as registered: Canada's Business Registries, ON 1836813, 2026-11-08)
- **vendor_registry_id**: 1836813 (ON)
- **vendor_registry_url**: https://ised-isde.canada.ca/cbr-rec/en/search?q=Roberts%20Onsite%20Inc
- **vendor_registered_address**: KITCHENER, Ontario (registered office city / province; Canada's Business Registries, ON 1836813, 2026-11-08)
- **vendor_legal_form**: ONTARIO BUSINESS CORP. (Canada's Business Registries, ON 1836813, 2026-11-08)
- **vendor_address**: 209 Manitou Drive, Kitchener, ON, N2C 1L4, Canada
- **vendor_country_basis**: vendor located in Canada (v)=robertsonsite.ca
- **vendor_bn9**: 893346262 (Canada's Business Registries, ON 1836813, 2026-11-08)
- **vendor_gst_hst_derived**: 893346262RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://robertsonsite.ca/
- **vendor_phone**: 1.800.265.8961
- **vendor_contact_evidence_url**: https://robertsonsite.ca/contact
- **vendor_logo_url**: https://robertsonsite.ca/assets/images/interface/logo.svg
- **vendor_website_status**: site answers
- **vendor_linkedin_url**: https://ca.linkedin.com/company/roberts-onsite
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); registry identity: 1836813 (ON) status Active — incorporated (Canada's Business Registries, ON 1836813, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: registry: Canada's Business Registries, ON 1836813, 2026-11-08; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2011-01-01; phone / role e-mails / logo: the vendor's own site, https://robertsonsite.ca/contact (tools/org_contacts.py, org_extras.py); website: https://robertsonsite.ca/ (site answers)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Active — incorporated (Canada's Business Registries, ON 1836813, 2026-11-08)
- **vendor_incorporation_date**: 2011-01-01
- **vendor_years_in_business**: 15.9 (since 2011-01-01, registry date)
- **vendor_bn_source**: registry: Canada's Business Registries, ON 1836813, 2026-11-08

## Contract
- **contract_status**: linked from a page of the Canada-located vendor's site (not a client page)
- **contract_title**: Multiple Electric Vehicle Charger Installations | Roberts Onsite
- **contract_description**: Multiple Electric Vehicle Charger Installations | Roberts Onsite (the record's title; the source publishes no separate description)
- **contract_link**: https://robertsonsite.ca/project-profiles/multiple-electric-vehicle-charger-installations
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 3
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: HST 13% (Ontario) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 893346262RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Accessibility Plan Black & Mcdonald Limited (stated on https://blackandmcdonald.com/accessibility/) — 2 Bloor Street East, Suite 2100, Toronto, ON M4W 1A8 ⏎ SUBMIT TO: info@blackandmcdonald.com (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: ROBERTS ONSITE INC. (as registered: Canada's Business Registries, ON 1836813, 2026-11-08) — 209 Manitou Drive, Kitchener, ON, N2C 1L4, Canada | GST/HST 893346262 (Canada's Business Registries, ON 1836813, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Multiple Electric Vehicle Charger Installations | Roberts Onsite
- **invoice_card_json**: {"bill_to": {"legal_name": "Accessibility Plan Black & Mcdonald Limited (stated on https://blackandmcdonald.com/accessibility/)", "legal_name_is_published": true, "address": "2 Bloor Street East, Suite 2100, Toronto, ON M4W 1A8", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "info@blackandmcdonald.com", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 13% (Ontario)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "893346262RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "ROBERTS ONSITE INC. (as registered: Canada's Business Registries, ON 1836813, 2026-11-08)", "bn9": "893346262 (Canada's Business Registries, ON 1836
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; AP phone or contact for follow-up
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["info@blackandmcdonald.com (general)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://blackandmcdonald.com/fr/contact/", "quote: \"inlinescript\" class=\"nitropack-inline-script\">var addresses=[[\"2 Bloor Street East, Suite 2100, <br> Toronto, ON M4W 1A8\",\"(416) 920-5100\",\"info@blackandmcdonal\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Cisco", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-02619"], "buyer_facts": ["address and phone: the buyer's own site, https://blackandmcdonald.com/contact/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "registry identity: 1836813 (ON) status Active — incorporated (Canada's Business Registries, ON 1836813, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data", "match)", "BN9: registry: Canada's Business Registries, ON 1836813, 2026-11-08", "GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected", "not automated)", "in

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://blackandmcdonald.com/fr/contact/ | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, blackandmcdonald.com)
- **status**: ok
- **pages**: 5
- **language**: en
- **logo_url**: https://blackandmcdonald.com/
- **logo_basis**: logo image in the site header
- **domain**: blackandmcdonald.com
- **key**: vendor:Black & McDonald Limited
- **name**: Black & McDonald Limited
- **website**: https://blackandmcdonald.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Black & McDonald
- **jsonld_logo**: https://blackandmcdonald.com/wp-content/uploads/2020/05/BlackMcDonald_Logo.png
- **jsonld_url**: https://blackandmcdonald.com/
- **jsonld_same_as**: https://www.facebook.com/BlackandMcDonald; https://x.com/bandmlimited; https://www.instagram.com/blackandmcdonald/; https://www.linkedin.com/company/black-&-mcdonald-limited; https://www.youtube.com/user/blackmcdonaldchannel
- **jsonld_quote**: {"@context":"https:\/\/schema.org","@graph":[{"@type":"WebPage","@id":"https:\/\/blackandmcdonald.com\/","url":"https:\/\/blackandmcdonald.com\/","name":"Construction, Utilities and Facilities Management Services | Black & McDonald","isPartOf":{"@id":"https:\/\/blackandmcdonald.com\/#website"},"abou
- **jsonld_page**: https://blackandmcdonald.com/
- **legal_name_stated**: Accessibility Plan Black & Mcdonald Limited
- **legal_name_stated_url**: https://blackandmcdonald.com/accessibility/
- **legal_name_stated_quote**: ts U.S. Sites FR U.S. Site Search Search × Accessibility for Ontarians with Disabilities Act (AODA) Accessibility Plan Black & Mcdonald Limited (“the Company”) The Black & McDonald Accessibility Plan outlines strategies and actions that will i
- **mentions**: {'payment_method': {'text': 'interaction and integration with the communities and stakeholders we serve', 'url': 'https://blackandmcdonald.com/about-us/', 'quote': 'Do it right” is a Black & McDonald core value, and that belief extends beyond project work into our interaction and integration with the communities and stakeholders we serve. Learn More Subsidiaries & Affiliates The Black & McDonald family of companies includ'}}
- **linkedin_url**: https://www.linkedin.com/company/black-

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "2 Bloor Street East, Suite 2100, Toronto, ON M4W 1A8", "address_country": "CA", "address_url": "https://blackandmcdonald.com/contact/", "address_method": "pattern", "address_quote": "Submit Listings Corporate Offices 2 Bloor Street East, Suite 2100, Toronto, ON M4W 1A8. (416) 920-5100 Branch Offices Atlantic Region Bathurst, NB – 1945 Miramichi Av", "emails": "info@blackandmcdonald.com", "emails_url": "https://blackandmcdonald.com/contact/", "domain": "blackandmcdonald.com", "key": "vd:blackandmcdonald.com", "name": "Black & McDonald Limited", "website": "https://blackandmcdonald.com/", "kind": "vendor", "date": "2026-11-03"}

## Vendor site facts (org_extras, robertsonsite.ca)
- **status**: ok
- **pages**: 4
- **language**: en
- **logo_url**: https://robertsonsite.ca/assets/images/interface/logo.svg
- **logo_basis**: logo image in the site header
- **domain**: robertsonsite.ca
- **key**: vendor:Roberts Onsite Inc
- **name**: Roberts Onsite Inc
- **website**: https://robertsonsite.ca/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **linkedin_url**: https://ca.linkedin.com/company/roberts-onsite
- **tel_links**: 18002658961

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "address": "209 Manitou Drive, Kitchener, Ontario, N2C 1L4", "address_country": "CA", "address_url": "https://robertsonsite.ca/contact", "address_method": "pattern", "address_quote": "ur consent at any time. Send Head Office 209 Manitou Drive, Kitchener, Ontario, N2C 1L4 Shipping Address 90 Otonabee Drive, Kitchener, Ontario, N2C 1L6 © 2026 Roberts", "phone": "1.800.265.8961", "phone_url": "https://robertsonsite.ca/contact", "domain": "robertsonsite.ca", "key": "vd:robertsonsite.ca", "name": "Roberts Onsite Inc", "website": "https://robertsonsite.ca/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Accessibility Plan Black & Mcdonald Limited | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Accessibility%20Plan%20Black%20%26%20Mcdonald%20Limited | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| v | BLACK & MCDONALD LIMITED |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:3ef1d665f2c83904",
 "ap_contact_team": {
  "emails": [
   "info@blackandmcdonald.com"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "info@blackandmcdonald.com",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://blackandmcdonald.com/fr/contact/",
    "quote": "inlinescript\" class=\"nitropack-inline-script\">var addresses=[[\"2 Bloor Street East, Suite 2100, <br> Toronto, ON M4W 1A8\",\"(416) 920-5100\",\"info@blackandmcdonald.com\",43.6705987,-79.3865914],[\"26A Dundee Avenue, <br> Mount Pearl, NL A1N 4R7\",\"(709) 747-1406\",\"\",47.5164112,-52.8418526],[\"19",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "blackandmcdonald.com",
    "task_id": "CL-LD-02619"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of blackandmcdonald.com (25 pages, robots.txt respected), no AI, no search engine"
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

## The vendor's other buyers in the dataset (first 60 of 10)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_bidsandtenders:63a6cb65-133b-48ba-94c5-a0ba96b9c6ac:5 | Region of Waterloo | Pre-Qualification of General Contractors, Mechanical and Electrical Subcontractors for WRPS Central Division 3rd Floor Alterations |  |  |  | https://regionofwaterloo.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/63a6cb65-133b-48ba-94c5-a0ba96b9c6ac |
| ca_bidsandtenders:8d9392d7-4a61-4fec-a5e6-9655631da0d0:2 | Waterloo Regional Police Service | Prequalification for Network/Communications Cabling |  |  |  | https://wrps.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/8d9392d7-4a61-4fec-a5e6-9655631da0d0 |
| ca_bidsandtenders:56fe2e04-b7b8-4798-8cc8-f34dcc1da75c:2 | City of Kitchener | Network Cabling Installation Services Roster |  |  |  | https://kitchener.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/56fe2e04-b7b8-4798-8cc8-f34dcc1da75c |
| ca_bidsandtenders:11d37aeb-c73c-4bae-a3f3-08cb91e1de65:22 | Upper Grand District School Board | Prequalification of General, Mechanical, Electrical, and Construction Management Contractors |  |  |  | https://ugdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/11d37aeb-c73c-4bae-a3f3-08cb91e1de65 |
| ca_bidsandtenders:11d37aeb-c73c-4bae-a3f3-08cb91e1de65:23 | Upper Grand District School Board | Prequalification of General, Mechanical, Electrical, and Construction Management Contractors |  |  |  | https://ugdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/11d37aeb-c73c-4bae-a3f3-08cb91e1de65 |
| ca_bidsandtenders:77346baa-8189-4c72-9706-beca1d145fdf:1 | Waterloo Region District School Board | Cedarbrae Public School – Boiler Plant & Controls Upgrade |  |  |  | https://wrdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/77346baa-8189-4c72-9706-beca1d145fdf |
| ca_bidsandtenders:14149b21-59ff-47d9-843d-f21eba17efaf:1 | Region of Waterloo | Airfield Lighting System – Installation / On Demand Services – Roster of Contractors |  |  |  | https://regionofwaterloo.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/14149b21-59ff-47d9-843d-f21eba17efaf |
| ca_bidsandtenders:5b9642d2-6869-4564-b776-4727337615ed:1 | City of Guelph | Pre-qualification of Electrical Sub-Contractors for the South End Community Centre |  |  |  | https://guelph.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/5b9642d2-6869-4564-b776-4727337615ed |
| ca_bidsandtenders:685e3931-9c3e-4910-aeea-0132116551d2:3 | City of Kitchener | Network Cabling Installation Services |  |  |  | https://kitchener.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/685e3931-9c3e-4910-aeea-0132116551d2 |
| ca_merx:2851101935:13 | McMaster University | VENDOR OF RECORD – MECHANICAL CONTRACTOR SERVICES | 1.0 |  |  | https://www.merx.com/oupma/mcmaster/solicitations/VENDOR-OF-RECORD-MECHANICAL-CONTRACTOR-SERVICES/0000267192?origin=0 |

## Open questions for hand research (layer 2)

- an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed)
- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
