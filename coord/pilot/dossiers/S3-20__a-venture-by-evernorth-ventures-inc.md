# S3-20 — A venture by EverNorth Ventures Inc ⇄ EnVision Consultants Ltd.

Stratum: **S3_routed_public_body_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: A venture by EverNorth Ventures Inc — 425 Adelaide Street West, Toronto, ON, M5V 3C1, CA (schema.org JSON-LD PostalAddress on https://talentontap.ca/)
SUBMIT TO: hello@talentontap.ca (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: EnVision Consultants Ltd. — 6415 Northwest Drive, Mississauga, ON, L4V 1X1, Canada | GST/HST 760662544RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: statutory default for construction work
DESCRIPTION: Road Reconstruction & Soil Management | EnVision
```

## Relationship
- **rank_group**: E1
- **data_quality_score**: 38
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: A venture by EverNorth Ventures Inc (company (private sector), jurisdiction not stated) — linked from the Canada-located vendor's site (weakest listed relationship): EnVision Consultants Ltd. | subject: Road Reconstruction & Soil Management | EnVision | published by: the Canada-located vendor's own website | record: https://envisionconsultants.ca/projects/reconstruction-soil-management/ | vendor in Canada because: vendor located in Canada (v)=envisionconsultants.ca | status rule: linked from a page of the Canada-located vendor's site (not a client page)
- **how_relationship_was_found**: tools/provider_mentions.py / news_match.py found the buyer linked from the vendor's own site or release
- **keys**: lead:decaebf2da2e6899
- **tier**: E
- **grade**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: A venture by EverNorth Ventures Inc
- **buyer_website**: https://talentontap.ca/
- **buyer_address**: 425 Adelaide Street West, Toronto, ON, M5V 3C1, CA (schema.org JSON-LD PostalAddress on https://talentontap.ca/)
- **buyer_contact_evidence_url**: https://talentontap.ca/contact/
- **buyer_legal_name_as_published**: A venture by EverNorth Ventures Inc
- **buyer_logo_url**: https://talentontap.ca/wp-content/uploads/2024/03/talentontap.ca-logo.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/talentontapca/
- **buyer_type**: company (private sector)
- **buyer_sector**: private sector
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://talentontap.ca/contact/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: hello@talentontap.ca
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://talentontap.ca/
- **email_evidence_quote**: mage": "https://talentontap.ca/images/talentontap.ca-logo.png", "@id": "https://talentontap.ca", "url": "https://talentontap.ca", "email": "hello@talentontap.ca", "address": { "@type": "PostalAddress", "streetAddress": "425 Adelaide Street West", "addressLocality": "Toronto", "addressRegio
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: hello@talentontap.ca (general) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://talentontap.ca/ | quote: "mage": "https://talentontap.ca/images/talentontap.ca-logo.png", "@id": "https://talentontap.ca", "url": "https://talentontap.ca", "email": "hello@talentontap.ca" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: no DMARC record; SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-22768
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: no DMARC record; SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: no DMARC record
- **dmarc_record**: no DMARC record at _dmarc.talentontap.ca; confirmed by 8.8.8.8
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 include:spf.protection.outlook.com -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **payment_terms_default_policy**: statutory default for construction work (buyer published no terms): the owner must pay a proper invoice no later than 28 days after receiving it — Construction Act, R.S.O. 1990, c. C.30, s. 6.4(1), in force 2019-10-01; s. 3(1) binds the Crown (https://www.ontario.ca/laws/statute/90c30, read 2026-11-08: "an owner shall pay the amount payable under a proper invoice no later than 28 days after receiving the proper invoice from the contractor"); applies only if this contract is an improvement under the Act
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: A venture by EverNorth Ventures Inc — 425 Adelaide Street West, Toronto, ON, M5V 3C1, CA (schema.org JSON-LD PostalAddress on https://talentontap.ca/) ⏎ SUBMIT TO: hello@talentontap.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: EnVision Consultants Ltd. — 6415 Northwest Drive, Mississauga, ON, L4V 1X1, Canada | GST/HST 760662544RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: statutory default for construction work ⏎ DESCRIPTION: Road Reconstruction & Soil Management | EnVision
- **invoice_card_json**: {"bill_to": {"legal_name": "A venture by EverNorth Ventures Inc", "legal_name_is_published": true, "address": "425 Adelaide Street West, Toronto, ON, M5V 3C1, CA (schema.org JSON-LD PostalAddress on https://talentontap.ca/)", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "hello@talentontap.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "statutory default for construction work (buyer published no terms): the owner must pay a proper invoice no later than 28 days after receiving it — Construction Act, R.S.O. 1990, c. C.30, s. 6.4(1), in force 2019-10-01; s. 3(1) binds the Crown (https://www.ontario.ca/laws/statute/90c30, read 2026-11-08: \"an owner shall pay the amount payable under a proper invoice no later than 28 days after receiving the proper invoice from the contractor\"); applies only if this contract is an improvement under the Act", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public servi
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); AP phone or contact for follow-up
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: EnVision Consultants Ltd.
- **vendor_legal_name**: EnVision Consultants Ltd.
- **vendor_trading_name**: EnVision (schema.org Organization name on the vendor's site: https://envisionconsultants.ca/)
- **vendor_registry_id**: Corporations Canada (corporation number): 12994879; corporation number 12994879 (Corporations Canada (open data))
- **vendor_registry_url**: https://ised-isde.canada.ca/cc/lgcy/fdrlCrpDtls.html?corpId=12994879
- **vendor_registered_address**: 6415 Northwest Drive, Unit 40, Mississauga, ON, L4V 1X1, CA
- **vendor_legal_form**: Canada Business Corporations Act (Canada (federal))
- **vendor_directors_range**: 1 to 10 directors (Corporations Canada)
- **vendor_last_annual_filing**: ; Corporations Canada anniversary 2021-05-06
- **vendor_address**: 6415 Northwest Drive, Mississauga, ON, L4V 1X1, Canada
- **vendor_country_basis**: vendor located in Canada (v)=envisionconsultants.ca
- **vendor_bn9**: 760662544
- **vendor_gst_hst_derived**: 760662544RT0001
- **vendor_website**: https://envisionconsultants.ca/
- **vendor_emails**: office@envisionconsultants.ca; info@envisionconsultants.ca
- **vendor_phone**: 905-677-0202
- **vendor_contact_evidence_url**: https://envisionconsultants.ca/contact/
- **vendor_logo_url**: https://envisionconsultants.ca/wp-content/uploads/2025/07/envision-logo.svg
- **vendor_website_status**: site answers
- **vendor_linkedin_url**: https://www.linkedin.com/company/envision-consultants/
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); registry identity: Corporations Canada (corporation number): 12994879; corporation number 12994879 (Corporations Canada (open data)) status Corporations Canada (corporation number): Active (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: registry match; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2021-05-06; phone / role e-mails / logo: the vendor's own site, https://envisionconsultants.ca/contact/ (tools/org_contacts.py, org_extras.py); website: https://envisionconsultants.ca/ (site answers)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Corporations Canada (corporation number): Active
- **vendor_incorporation_date**: 2021-05-06
- **vendor_years_in_business**: 5.5 (since 2021-05-06, registry date)

## Contract
- **contract_status**: linked from a page of the Canada-located vendor's site (not a client page)
- **contract_title**: Road Reconstruction & Soil Management | EnVision
- **contract_description**: Road Reconstruction & Soil Management | EnVision (the record's title; the source publishes no separate description)
- **contract_link**: https://envisionconsultants.ca/projects/reconstruction-soil-management/
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **payment_terms_default_policy**: statutory default for construction work (buyer published no terms): the owner must pay a proper invoice no later than 28 days after receiving it — Construction Act, R.S.O. 1990, c. C.30, s. 6.4(1), in force 2019-10-01; s. 3(1) binds the Crown (https://www.ontario.ca/laws/statute/90c30, read 2026-11-08: "an owner shall pay the amount payable under a proper invoice no later than 28 days after receiving the proper invoice from the contractor"); applies only if this contract is an improvement under the Act
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: HST 13% (Ontario) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 760662544RT0001

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: A venture by EverNorth Ventures Inc — 425 Adelaide Street West, Toronto, ON, M5V 3C1, CA (schema.org JSON-LD PostalAddress on https://talentontap.ca/) ⏎ SUBMIT TO: hello@talentontap.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: EnVision Consultants Ltd. — 6415 Northwest Drive, Mississauga, ON, L4V 1X1, Canada | GST/HST 760662544RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: statutory default for construction work ⏎ DESCRIPTION: Road Reconstruction & Soil Management | EnVision
- **invoice_card_json**: {"bill_to": {"legal_name": "A venture by EverNorth Ventures Inc", "legal_name_is_published": true, "address": "425 Adelaide Street West, Toronto, ON, M5V 3C1, CA (schema.org JSON-LD PostalAddress on https://talentontap.ca/)", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "hello@talentontap.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "statutory default for construction work (buyer published no terms): the owner must pay a proper invoice no later than 28 days after receiving it — Construction Act, R.S.O. 1990, c. C.30, s. 6.4(1), in force 2019-10-01; s. 3(1) binds the Crown (https://www.ontario.ca/laws/statute/90c30, read 2026-11-08: \"an owner shall pay the amount payable under a proper invoice no later than 28 days after receiving the proper invoice from the contractor\"); applies only if this contract is an improvement under the Act", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public servi
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); AP phone or contact for follow-up
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["hello@talentontap.ca (general)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://talentontap.ca/", "quote: \"mage\": \"https://talentontap.ca/images/talentontap.ca-logo.png\", \"@id\": \"https://talentontap.ca\", \"url\": \"https://talentontap.ca\", \"email\": \"hello@talentontap.ca\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: no DMARC record; SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-22768"], "buyer_facts": ["address and phone: the buyer's own site, https://talentontap.ca/contact/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "registry identity: Corporations Canada (corporation number): 12994879", "corporation number 12994879 (Corporations Canada (open data)) status Corporations Canada (corporation number): Active (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data", "match)", "BN9: registry match", "GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-p

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://talentontap.ca/ | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, talentontap.ca)
- **status**: ok
- **pages**: 6
- **v**: 2
- **jsonld_type**: LocalBusiness
- **jsonld_name**: Talent on Tap
- **jsonld_address**: 425 Adelaide Street West, Toronto, ON, M5V 3C1, CA
- **jsonld_email**: hello@talentontap.ca
- **jsonld_url**: https://talentontap.ca
- **jsonld_same_as**: https://www.instagram.com/talentontapca/; https://www.linkedin.com/company/talentontapca/
- **jsonld_quote**: { "@context": "https://schema.org", "@type": "LocalBusiness", "name": "Talent on Tap", "image": "https://talentontap.ca/images/talentontap.ca-logo.png", "@id": "https://talentontap.ca", "url": "https://talentontap.ca", "email": "hello@talentontap.ca", "address": { "@type": "PostalAddress", "streetAd
- **jsonld_page**: https://talentontap.ca/
- **legal_name_stated**: EverNorth Ventures Inc
- **legal_name_stated_url**: https://talentontap.ca/terms/
- **legal_name_stated_quote**: e These rules are for using the website talentontap.ca. They form a legal agreement between you and EverNorth Ventures Inc. (also referred to as “Company,” “we,” “us,” “our”). These rules cover your use of the website, inc
- **mentions**: {'payment_method': {'text': 'Interactive Functions”) constitutes your consent to all actions we take with respect to', 'url': 'https://talentontap.ca/terms/', 'quote': 'nd other such functions, including storefront functions and data delivery functions (collectively, “Interactive Functions”) constitutes your consent to all actions we take with respect to such information consistent with our Privacy Policy. Any username, passw'}}
- **linkedin_url**: https://www.linkedin.com/company/talentontapca/
- **language**: en
- **legal_name**: A venture by EverNorth Ventures Inc
- **legal_name_url**: https://talentontap.ca/
- **legal_name_quote**: age at a time. LinkedIn Instagram Terms of Use Privacy Policy Copyright Policy Talent on Tap © 2026 A venture by EverNorth Ventures Inc. Build your custom Marketing Package today. Get Started! Build Your Package! Back Next
- **logo_url**: https://talentontap.ca/wp-content/uploads/2024/03/talentontap.ca-logo.png
- **logo_basis**: logo image in the site header
- **domain**: talentontap.ca
- **key**: lead:decaebf2da2e6899
- **name**: talentontap.ca
- **website**: https://talentontap.ca/
- **kind**: buyer
- **date**: 2026-11-08

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "425 Adelaide Street West, Toronto, ON, M5V 3C1", "address_country": "CA", "address_url": "https://talentontap.ca/contact/", "address_method": "json-ld", "address_quote": "JSON-LD PostalAddress on the page: 425 Adelaide Street West, Toronto, ON, M5V 3C1", "emails": "hello@talentontap.ca", "emails_url": "https://talentontap.ca/contact/", "domain": "talentontap.ca", "key": "lead:decaebf2da2e6899", "name": "talentontap.ca", "website": "https://talentontap.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, envisionconsultants.ca)
- **status**: ok
- **pages**: 5
- **language**: en
- **legal_name**: EnVision Consultants Ltd
- **legal_name_url**: https://envisionconsultants.ca/
- **legal_name_quote**: in Ontario. Creative strategies accounting for species at risk in the North Bruce Peninsula. © 2026 EnVision Consultants Ltd. All rights reserved. AODA Policy Privacy Policy Terms & Conditions Designed & developed by Talent
- **logo_url**: https://envisionconsultants.ca/wp-content/uploads/2025/07/envision-logo.svg
- **logo_basis**: logo image in the site header
- **domain**: envisionconsultants.ca
- **key**: vendor:EnVision Consultants Ltd.
- **name**: EnVision Consultants Ltd.
- **website**: https://envisionconsultants.ca/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: LocalBusiness
- **jsonld_name**: EnVision
- **jsonld_address**: 6415 Northwest Drive, Mississauga, Ontario, L4V 1X1, CA
- **jsonld_phone**: 905-677-0202
- **jsonld_email**: office@envisionconsultants.ca
- **jsonld_url**: https://envisionconsultants.ca
- **jsonld_same_as**: https://www.linkedin.com/company/envision-consultants/
- **jsonld_quote**: {"@context":"https:\/\/schema.org","url":"https:\/\/envisionconsultants.ca\/","@id":"https:\/\/envisionconsultants.ca\/","@type":"WebPage","name":"Homepage | EnVision","description":"EnVision delivers strategic, technical, and agile consulting across geotechnical, environmental, infrastructure, wate
- **jsonld_page**: https://envisionconsultants.ca/
- **legal_name_stated**: EnVision Consultants Ltd
- **legal_name_stated_url**: https://envisionconsultants.ca/terms/
- **legal_name_stated_quote**: ons”) govern the use of www.envisionconsultants.ca (the “Site”). This Site is owned and operated by EnVision Consultants Ltd., a consulting & engineering services provider. By using this Site, you indicate that you have read
- **linkedin_url**: https://www.linkedin.com/company/envision-consultants/
- **tel_links**: 9056770202

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "address": "6415 Northwest Drive, Mississauga, Ontario, L4V 1X1", "address_country": "CA", "address_url": "https://envisionconsultants.ca/contact/", "address_method": "json-ld", "address_quote": "Submit Head Office 6415 Northwest Drive Units 37-40 Mississauga Ontario Canada L4V 1X1 Pickering Office 925 Brock Road Unit 7 Pickering Ontario Canada L1W 2X9 Stoney", "phone": "905-677-0202", "phone_url": "https://envisionconsultants.ca/contact/", "emails": "info@envisionconsultants.ca; office@envisionconsultants.ca", "emails_url": "https://envisionconsultants.ca/contact/", "domain": "envisionconsultants.ca", "key": "vd:envisionconsultants.ca", "name": "EnVision Consultants Ltd.", "website": "https://envisionconsultants.ca/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | EnVision Consultants Ltd. | found | EnVision Consultants Ltd. | 760662544 | 12994879 | CC | Business Corporation | Active | 2021-05-06 | Mississauga | Ontario |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=EnVision%20Consultants%20Ltd. | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | api_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | EnVision Consultants Ltd. | found | EnVision Consultants Ltd. | 760662544 | corporation number 12994879 | Corporations Canada (open data) | Canada Business Corporations Act | Active | 2021-05-06 | Mississauga | ON | 6415 Northwest Drive, Unit 40, Mississauga, ON, L4V 1X1 | https://open.canada.ca/data/en/dataset/0032ce54-c5dd-4b66-99a0-320a7b5e99f2 | 2026-11-08 |

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | EnVision Consultants Ltd. |  |  |  |  |  |  |  |  |  |  |
| v | EnVision Consultants Ltd. |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:decaebf2da2e6899",
 "ap_contact_team": {
  "emails": [
   "hello@talentontap.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "hello@talentontap.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://talentontap.ca/",
    "quote": "mage\": \"https://talentontap.ca/images/talentontap.ca-logo.png\", \"@id\": \"https://talentontap.ca\", \"url\": \"https://talentontap.ca\", \"email\": \"hello@talentontap.ca\", \"address\": { \"@type\": \"PostalAddress\", \"streetAddress\": \"425 Adelaide Street West\", \"addressLocality\": \"Toronto\", \"addressRegio",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "talentontap.ca",
    "task_id": "CL-LD-22768"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of talentontap.ca (25 pages, robots.txt respected), no AI, no search engine"
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

## The vendor's other buyers in the dataset (first 60 of 25)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_bidsandtenders:78480db2-822f-40b3-9d27-c6ed3c4c0f04:1 | Region of Peel | GEOTECHNICAL, HYDROGEOLOGICAL AND EXCESS SOILS INVESTIGATIONS FOR THE FLOW SOUTH CALEDON WATER AND WASTEWATER INFRASTRUCTURE PROGRAM– PART 1 | 20972860.0 |  |  | https://peelregion.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/78480db2-822f-40b3-9d27-c6ed3c4c0f04 |
| ca_bidsandtenders:8a8a36f8-3e18-4cec-acb3-db2d3780a5cb:1 | Municipality of Greenstone | Engineering Services for Campground Sewage Works Compliance |  |  |  | https://greenstone.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/8a8a36f8-3e18-4cec-acb3-db2d3780a5cb |
| ca_bidsandtenders:8cb4bacb-e822-4b14-8949-f6befacde765:1 | Town of Caledon | Contract Administration and Construction Inspection Services for Wray Park | 243000.0 |  |  | https://caledon.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/8cb4bacb-e822-4b14-8949-f6befacde765 |
| ca_bidsandtenders:5f79d0ae-3c97-4aa9-a82c-c2aef44c0898:6 | City of Barrie | Geotechnical and Environmental Engineering Roster Services |  |  |  | https://barrie.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/5f79d0ae-3c97-4aa9-a82c-c2aef44c0898 |
| ca_bidsandtenders:09c65bbf-9fa9-409b-b6ce-a50d27b14a67:7 | York Region | Communal Water and Wastewater Systems Technical Services Roster |  |  |  | https://york.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/09c65bbf-9fa9-409b-b6ce-a50d27b14a67 |
| ca_bidsandtenders:7dba9c28-d8e9-4667-9a87-eda8e5774d51:1 | Township of Springwater | Designated Substances Surveys-Snow Valley Water & Waste Water Facilities |  |  |  | https://springwater.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/7dba9c28-d8e9-4667-9a87-eda8e5774d51 |
| ca_bidsandtenders:486d1f15-a165-4199-ab6f-1f2b371b0b37:1 | Township of King | Closed Landfill Monitoring and Reporting | 395500.0 |  |  | https://king.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/486d1f15-a165-4199-ab6f-1f2b371b0b37 |
| ca_bidsandtenders:ae8e15ad-851e-4fd3-bc99-e92abc6f0945:1 | City of Markham | Stormwater Management Guideline Update |  |  |  | https://markham.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/ae8e15ad-851e-4fd3-bc99-e92abc6f0945 |
| ca_bidsandtenders:1476dda9-e4a5-41e4-a7f8-d04cef98585f:1 | Hamilton-Wentworth Catholic District School Board | Guardian Angels Sewage Treatment System |  |  |  | https://hwcdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/1476dda9-e4a5-41e4-a7f8-d04cef98585f |
| ca_bidsandtenders:accccce4-2232-4a01-b930-4841ccaf9c51:10 | City of Port Colborne | Soils Testing for Operations and Maintenance on behalf of the Niagara Public Purchasing Committee |  |  |  | https://portcolborne.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/accccce4-2232-4a01-b930-4841ccaf9c51 |
| ca_bidsandtenders:d3e160c5-d00f-49aa-a011-ed5dd773d0b8:9 | York Region | Request for Pre-Qualification for Qualified Person Services under Ontario Regulation 406/19 |  |  |  | https://york.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/d3e160c5-d00f-49aa-a011-ed5dd773d0b8 |
| ca_bidsandtenders:db5700b7-d7ee-4842-9f77-ce36e9e9e8db:1 | City of Barrie | Geotechnical Consulting Services for Allandale B Neighbourhood Reconstruction | 313511.0 |  |  | https://barrie.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/db5700b7-d7ee-4842-9f77-ce36e9e9e8db |
| ca_bidsandtenders:d03f27c6-c78b-41e5-b0ba-c2a74733038b:1 | Region of Peel | Geotechnical and Hydrogeological Engineering Services for Sewer and Watermains on Old School and Dixie Roads, Contract 5, Town of Caledon, Projects 19-1189 and  | 949025.0 |  |  | https://peelregion.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/d03f27c6-c78b-41e5-b0ba-c2a74733038b |
| ca_bidsandtenders:5842491c-5919-4aa6-8c70-51477789f70a:3 | Town of Ajax | Pre-Qualification Consulting Firms ~ Geotechnical Services |  |  |  | https://ajax.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/5842491c-5919-4aa6-8c70-51477789f70a |
| ca_bidsandtenders:a84a209b-69a2-44a3-b99d-8805c1f30fa9:1 | Region of Halton | Environmental Monitoring Services at W.A. Bill Johnson Biosolids Management Centre | 73905.36 |  |  | https://haltonregion.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/a84a209b-69a2-44a3-b99d-8805c1f30fa9 |
| ca_bidsandtenders:a10475f2-58d5-4cc6-8a47-9f28502fa721:1 | City of Barrie | Geotechnical Services for Bayfield St Right of Way Expansion | 256550.0 |  |  | https://barrie.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/a10475f2-58d5-4cc6-8a47-9f28502fa721 |
| ca_bidsandtenders:256a5f2b-3556-40da-a936-bf0659c79379:1 | County of Frontenac | Natural Heritage Consulting Services |  |  |  | https://frontenaccounty.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/256a5f2b-3556-40da-a936-bf0659c79379 |
| ca_bidsandtenders:227ae27c-f016-48dd-ae73-35413ba2c9a0:1 | City of Belleville | Consulting Services for Geotechnical Investigations for the Reconstruction of Orchard Drive |  |  |  | https://belleville.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/227ae27c-f016-48dd-ae73-35413ba2c9a0 |
| ca_bidsandtenders:07cd47c9-2f74-475a-a9b6-7833fda0ba3b:2 | York Region | Prequalification for Qualified Person Services Under Ontario Regulation 406/19 |  |  |  | https://york.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/07cd47c9-2f74-475a-a9b6-7833fda0ba3b |
| ca_bidsandtenders:a3306b9c-f9c7-4212-adb6-7ae527ca470e:1 | City of Guelph | Geotechnical and Soil Investigation for Downtown Capital Implementation Plan |  |  |  | https://guelph.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/a3306b9c-f9c7-4212-adb6-7ae527ca470e |
| ca_bidsandtenders:e053e4b7-f1d7-4e0c-b286-91563dd1b478:3 | Region of Peel | GEOTECHNICAL, ENVIRONMENTAL, AND RELATED SERVICES FOR THE REGION OF PEEL | 3273300.0 |  |  | https://peelregion.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/e053e4b7-f1d7-4e0c-b286-91563dd1b478 |
| ca_bidsandtenders:e1a39041-8c6f-4b02-aeb2-7fbbeee846e7:1 | Town of South Bruce Peninsula | Sauble Beach Community Centre Campus Septic Assessment and Design |  |  |  | https://southbrucepeninsula.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/e1a39041-8c6f-4b02-aeb2-7fbbeee846e7 |
| ca_bidsandtenders:f5365b98-c457-45ff-997e-3fe1d8148541:1 | City of Belleville | Consulting Services for Geotechnical Investigations for the Reconstruction of Phillipston Road. |  |  |  | https://belleville.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/f5365b98-c457-45ff-997e-3fe1d8148541 |
| ca_merx:3651232467:3 | Greater Toronto Airports Authority | Environmental Consulting Services |  |  |  | https://www.merx.com/torontopearson/solicitations/Environmental-Consulting-Services/0000306005?origin=0 |
| ca_merx:2954403270:2 | CreateTO (Build Toronto, TPLC) | Environmental, Geotechnical and Hydrogeological Services Roster |  |  |  | https://www.merx.com/buildtorontotplc/solicitations/Environmental-Geotechnical-and-Hydrogeological-Services-Roster/0000272044?origin=0 |

## Open questions for hand research (layer 2)

- an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed)
- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
