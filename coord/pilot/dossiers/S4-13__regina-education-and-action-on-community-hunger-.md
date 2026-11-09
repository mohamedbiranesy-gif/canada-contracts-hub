# S4-13 — REGINA EDUCATION AND ACTION ON COMMUNITY HUNGER INCORPORATED ⇄ inferred: SaskPower

Stratum: **S4_routed_company_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: REGINA EDUCATION AND ACTION ON COMMUNITY HUNGER INCORPORATED (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (reachinregina.ca) + name) — P.O. BOX 4482 STN MAIN REACH, Regina, SK, S4P3W7 — buyer tax no. 131314650 RR0001 (as printed: Charity Number: 131314650RR0001; https://www.reachinregina.ca/)
SUBMIT TO: info@reachinregina.ca (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: SaskPower — 2025 Victoria Avenue, Regina, SK S4P 0S1 | GST/HST 119429678 (GST/HST registration number printed by the organisation itself: https://www.saskpower.com/accounts/billing/your-power-bill/how-to-read-your-bill/business, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: REGINA EDUCATION AND ACTION ON COMMUNITY HUNGER INCORPORATED (organisation (type not stated in the record), SK) — inferred: no record; the o
```

## Relationship
- **rank_group**: I1
- **data_quality_score**: 30
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: MEDIUM (typical supplier for this type of organisation)
- **relationship_detail**: REGINA EDUCATION AND ACTION ON COMMUNITY HUNGER INCORPORATED (organisation (type not stated in the record), SK) — inferred: no record; the organisation's type and province make a Canadian supplier relationship near-certain: inferred: SaskPower | published by: inference from the buyer's type and province (no contract, payment or listing record) | vendor in Canada because: the vendor's own site, https://saskpower.com/contact: 'Send us a letter: SaskPower Corporate Relations and Communications 9th Floor, 2025 Victoria Ave Regina, SK S4P 0S1' | status rule: inferred relationship (no record): medium confidence; the buyer is an organisation in Saskatchewan (province from its registered address in the CRA List of charities 2024 (open.canada.ca)); SaskPower holds the electricit
- **how_relationship_was_found**: no record; tools/org_lists.py / osm_orgs.py / the crawlers placed the organisation in Canada by type and province; the vendor named is the Canada-located supplier such bodies almost always pay (see `vendor_country_basis`)
- **keys**: cra:131314650
- **tier**: I
- **grade**: 1

## Buyer
- **buyer**: REGINA EDUCATION AND ACTION ON COMMUNITY HUNGER INCORPORATED
- **buyer_website**: https://reachinregina.ca
- **buyer_address**: P.O. BOX 4482 STN MAIN REACH, Regina, SK, S4P3W7
- **buyer_phone**: (306) 347-3224
- **buyer_contact_evidence_url**: https://www.reachinregina.ca/contact
- **buyer_legal_name_as_published**: REGINA EDUCATION AND ACTION ON COMMUNITY HUNGER INCORPORATED (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (reachinregina.ca) + name)
- **buyer_bn_as_published**: 131314650 RR0001 (as printed: Charity Number: 131314650RR0001; https://www.reachinregina.ca/)
- **buyer_bn_program**: RR (registered charity program account)
- **buyer_gst_hst_derived**: 131314650RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_logo_url**: https://www.reachinregina.ca/assets/reach-logo.svg
- **buyer_website_status**: site answers
- **buyer_type**: company (private sector) (from the organisation's name / web domain)
- **buyer_sector**: private sector
- **buyer_charity_status**: registered (listed) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (reachinregina.ca) + name)
- **buyer_charity_designation**: C; 0210
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.reachinregina.ca/contact (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: info@reachinregina.ca
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://www.reachinregina.ca/contact
- **email_evidence_quote**: d Box Frozen Meals Family Basket Child Nutrition Food Education mîcisotān Resources Get Involved Donate Volunteer Contact Donate Contact us info@reachinregina.ca (306) 347-3224 1350 Osler Street View on Google Maps Follow us Facebook Instagram Name (Required) First Last Email (Required) En
- **email_evidence_context**: REACH Regina » Contact About REACH About Us Our Team FAQ Community Programs Good Food Box Frozen Meals Family Basket Child Nutrition Food Education mîcisotān Resources Get Involved Donate Volunteer Contact Donate Contact us info@reachinregina.ca (306) 347-3224 1350 Osler Street View on Google Maps Follow us Facebook Instagram Name (Required) First Last Email (Required) Enter Email Confirm Email Comments (Required) Please let us know what's on your mind. Have a question for us? Ask away. Sub (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: info@reachinregina.ca (general) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://www.reachinregina.ca/contact | quote: "d Box Frozen Meals Family Basket Child Nutrition Food Education mîcisotān Resources Get Involved Donate Volunteer Contact Donate Contact us info@reachinregina.c" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-CRA-04640
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Microsoft 365
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1;p=quarantine;sp=reject;adkim=s;aspf=s;pct=100;fo=0:1:d:s;rf=afrf;ri=86400;rua=mailto:dmarc-admin@reachinregina.ca;ruf=mailto:dmarc-admin@reachinregina.ca
- **dmarc_record_domain**: reachinregina.ca
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 +a +mx +ip4:69.27.100.3 ip4:149.56.142.221 include:spf.protection.outlook.com include:spf.blacksun.ca ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: REGINA EDUCATION AND ACTION ON COMMUNITY HUNGER INCORPORATED (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (reachinregina.ca) + name) — P.O. BOX 4482 STN MAIN REACH, Regina, SK, S4P3W7 — buyer tax no. 131314650 RR0001 (as printed: Charity Number: 131314650RR0001; https://www.reachinregina.ca/) ⏎ SUBMIT TO: info@reachinregina.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: SaskPower — 2025 Victoria Avenue, Regina, SK S4P 0S1 | GST/HST 119429678 (GST/HST registration number printed by the organisation itself: https://www.saskpower.com/accounts/billing/your-power-bill/how-to-read-your-bill/business, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: REGINA EDUCATION AND ACTION ON COMMUNITY HUNGER INCORPORATED (organisation (type not stated in the record), SK) — inferred: no record; the o
- **invoice_card_json**: {"bill_to": {"legal_name": "REGINA EDUCATION AND ACTION ON COMMUNITY HUNGER INCORPORATED (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (reachinregina.ca) + name)", "legal_name_is_published": true, "address": "P.O. BOX 4482 STN MAIN REACH, Regina, SK, S4P3W7", "address_is_the_invoice_address": false, "tax_number": "131314650 RR0001 (as printed: Charity Number: 131314650RR0001; https://www.reachinregina.ca/)", "language": "en"}, "submit_to": {"email": "info@reachinregina.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (SK)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: inferred: SaskPower
- **vendor_address**: 2025 Victoria Avenue, Regina, SK S4P 0S1
- **vendor_country_basis**: the vendor's own site, https://saskpower.com/contact: 'Send us a letter: SaskPower Corporate Relations and Communications 9th Floor, 2025 Victoria Ave Regina, SK S4P 0S1'
- **vendor_bn9**: 119429678 (GST/HST registration number printed by the organisation itself: https://www.saskpower.com/accounts/billing/your-power-bill/how-to-read-your-bill/business, 2026-11-08)
- **vendor_gst_hst_derived**: 119429678RT0001 (R119429678 (printed in the older 'R' format on the sample business bill))
- **vendor_website**: https://www.saskpower.com
- **vendor_phone**: 310-2220
- **vendor_contact_evidence_url**: https://saskpower.com/contact-us
- **vendor_logo_url**: https://saskpower.com/-/media/saskpower/logo.png?la=en&h=92&w=344&hash=2F4CBFD7B403E69A4530EB778FAD7A1E
- **vendor_facts_provenance**: name and address: the record's vendor block (inference from the buyer's type and province (no contract, payment or listing record)); BN9: printed on the organisation's own page (https://www.saskpower.com/accounts/billing/your-power-bill/how-to-read-your-bill/business); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); phone / role e-mails / logo: the vendor's own site, https://saskpower.com/contact-us (tools/org_contacts.py, org_extras.py); website: https://www.saskpower.com
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_bn_source**: printed on the organisation's own page (https://www.saskpower.com/accounts/billing/your-power-bill/how-to-read-your-bill/business)

## Contract
- **contract_status**: inferred relationship (no record): medium confidence; the buyer is an organisation in Saskatchewan (province from its registered address in the CRA List of charities 2024 (open.canada.ca)); SaskPower holds the electricity franchise in Saskatchewan outside the Saskatoon and Swift Current municipal utilities (The Power Corporation Act); an organisation with premises there buys its electricity from it, unless its landlord pays it through the lease
- **source**: inference from the buyer's type and province (no contract, payment or listing record)
- **contracts_with_canadian_suppliers**: 0
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 131314650RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (SK) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 119429678RT0001 (R119429678 (printed in the older 'R' format on the sample business bill))

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: REGINA EDUCATION AND ACTION ON COMMUNITY HUNGER INCORPORATED (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (reachinregina.ca) + name) — P.O. BOX 4482 STN MAIN REACH, Regina, SK, S4P3W7 — buyer tax no. 131314650 RR0001 (as printed: Charity Number: 131314650RR0001; https://www.reachinregina.ca/) ⏎ SUBMIT TO: info@reachinregina.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: SaskPower — 2025 Victoria Avenue, Regina, SK S4P 0S1 | GST/HST 119429678 (GST/HST registration number printed by the organisation itself: https://www.saskpower.com/accounts/billing/your-power-bill/how-to-read-your-bill/business, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: REGINA EDUCATION AND ACTION ON COMMUNITY HUNGER INCORPORATED (organisation (type not stated in the record), SK) — inferred: no record; the o
- **invoice_card_json**: {"bill_to": {"legal_name": "REGINA EDUCATION AND ACTION ON COMMUNITY HUNGER INCORPORATED (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (reachinregina.ca) + name)", "legal_name_is_published": true, "address": "P.O. BOX 4482 STN MAIN REACH, Regina, SK, S4P3W7", "address_is_the_invoice_address": false, "tax_number": "131314650 RR0001 (as printed: Charity Number: 131314650RR0001; https://www.reachinregina.ca/)", "language": "en"}, "submit_to": {"email": "info@reachinregina.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (SK)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["info@reachinregina.ca (general)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://www.reachinregina.ca/contact", "quote: \"d Box Frozen Meals Family Basket Child Nutrition Food Education mîcisotān Resources Get Involved Donate Volunteer Contact Donate Contact us info@reachinregina.c\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-CRA-04640"], "buyer_facts": ["address and phone: the buyer's own site, https://www.reachinregina.ca/contact (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (inference from the buyer's type and province (no contract, payment or listing record))", "BN9: printed on the organisation's own page (https://www.saskpower.com/accounts/billing/your-power-bill/how-to-read-your-bill/business)", "GST/HST derived BN9 + RT0001 (CRA registry is CAP

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.reachinregina.ca/contact | 2026-11-08 | ok |  |  |  | (306) 347-3224 |  |  |  |  |  |

## Buyer site facts (org_extras, reachinregina.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **bn**: 131314650
- **bn_program**: RR0001
- **bn_label**: Charity Number: 131314650RR0001
- **bn_url**: https://www.reachinregina.ca/
- **bn_quote**: ur continued support of REACH! Our Partners and Investors Mailing Address Box 4482 Regina SK S4P3W7 Charity Number: 131314650RR0001 1350 Osler Street (306) 347-3224 Donate Volunteer About REACH About Us Our Team FAQ Community Progr
- **logo_url**: https://www.reachinregina.ca/assets/reach-logo.svg
- **logo_basis**: logo image in the site header
- **domain**: reachinregina.ca
- **key**: cra:131314650
- **name**: REGINA EDUCATION AND ACTION ON COMMUNITY HUNGER INCORPORATED
- **website**: https://reachinregina.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **mentions**: {'payment_method': {'text': 'eTransfer any amount to payments@reachinregina', 'url': 'https://www.reachinregina.ca/about/faq', 'quote': 'es REACH stand for? R egina E ducation and A ction on C ommunity H unger How can I donate to REACH? eTransfer any amount to payments@reachinregina.ca (Please leave a note in the eTransfer letting us know this is a donation.) Over the phone or at'}}
- **tel_links**: 306-347-3224

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "phone": "(306) 347-3224", "phone_url": "https://www.reachinregina.ca/contact", "emails": "info@reachinregina.ca", "emails_url": "https://www.reachinregina.ca/contact", "domain": "reachinregina.ca", "key": "cra:131314650", "name": "REGINA EDUCATION AND ACTION ON COMMUNITY HUNGER INCORPORATED", "website": "https://reachinregina.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, saskpower.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://saskpower.com/-/media/saskpower/logo.png?la=en&h=92&w=344&hash=2F4CBFD7B403E69A4530EB778FAD7A1E
- **logo_basis**: logo image in the site header
- **domain**: saskpower.com
- **key**: b:7c6184faae853053
- **name**: SaskPower
- **website**: https://saskpower.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Open Access Transmission Tariff
- **legal_name_stated_url**: https://saskpower.com/accounts/mysaskpower/your-account/terms-and-conditions
- **legal_name_stated_quote**: rical Services and other SaskPower Services with the exception of matters dealt with in SaskPower’s Open Access Transmission Tariff (OATT). SaskPower's Terms and Conditions of Service Cookies Our website uses cookies to personalize
- **mentions**: {'payment_method': {'text': 'Credit Card Payments Equalized Payment Plan Equalized Payment Plan Payment Arrangements Power Rates', 'url': 'https://saskpower.com/home', 'quote': 'Your Bill Pre-authorized Payments Payment History Trouble Paying Your Bill? Pre-authorized Payments Credit Card Payments Equalized Payment Plan Equalized Payment Plan Payment Arrangements Power Rates ← Power Rates Power Supply Rates 2026 and 2027 Rate Increase'}}
- **linkedin_url**: http://www.linkedin.com/company/saskpower
- **tel_links**: 1-888-355-5589; 18887576937; 18883555589; 3065362886

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "10,000 , PO Box 6300, STN Main, Regina, SK S4P 4J5", "address_country": "CA", "address_url": "https://saskpower.com/contact-us", "address_method": "pattern", "address_quote": "ail Us Send payments to: Cheques under $10,000 PO Box 6300, STN Main Regina, SK S4P 4J5 Cheques $10,000+ SaskPower Payment Support 10NE – 2025 Victoria Avenue Regina", "phone": "310-2220", "phone_url": "https://saskpower.com/contact-us", "domain": "saskpower.com", "key": "b:7c6184faae853053", "name": "SaskPower", "website": "https://saskpower.com/", "kind": "buyer", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | REGINA EDUCATION AND ACTION ON COMMUNITY HUNGER INCORPORATED | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=REGINA%20EDUCATION%20AND%20ACTION%20ON%20COMMUNITY%20HUNGER%20INCORPORATED | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | SaskPower | Q2225615 | official website on the organisation's domain (https://www.saskpower.com/) + name | Saskatchewan Power Corporation [en] | SaskPower | SaskPower | electricity supply company | state-owned enterprise | Canada | 1929-01-01 | Regina; SaskPower Building |
| b | REGINA EDUCATION AND ACTION ON COMMUNITY HUNGER INCORPORATED |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "cra:131314650",
 "ap_contact_team": {
  "emails": [
   "info@reachinregina.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "info@reachinregina.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.reachinregina.ca/contact",
    "quote": "d Box Frozen Meals Family Basket Child Nutrition Food Education mîcisotān Resources Get Involved Donate Volunteer Contact Donate Contact us info@reachinregina.ca (306) 347-3224 1350 Osler Street View on Google Maps Follow us Facebook Instagram Name (Required) First Last Email (Required) En",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "REGINA EDUCATION AND ACTION ON COMMUNITY HUNGER INCORPORATED",
    "task_id": "CL-CRA-04640"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of www.reachinregina.ca (7 pages, robots.txt respected), no AI, no search engine"
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
