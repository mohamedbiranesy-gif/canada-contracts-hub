# S2-28 — City of Miami ⇄ geotab.com

Stratum: **S2_complete_no_published_PO_rule** · pay on sight: yes — reference rule not published (quote the buyer's PO / order number when one is issued) · channel tier 1 · AP grade C · missing: (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: City of Miami (stated on https://miamigardens-fl.gov/) — 18605 NW 27th Avenue, Miami Gardens, FL 33056
SUBMIT TO: accountspayable@miamigardens-fl.gov (invoicing/AP mailbox, confirmed by the referee) | portal (not confirmed as an invoice channel): supplier / vendor portal
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Geotab Inc. — 2440 Winston Park Dr, Oakville, ON, L6H 7V2, CA | GST/HST 825605769 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2019-08-01; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) | NEQ 1174740010
TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state  | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Miami Gardens saves $60,000+ annually and generates $1.1M from vehicle resales with Geotab | Geotab
```

## Relationship
- **rank_group**: D4
- **data_quality_score**: 70
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: City of Miami (municipality / local government, jurisdiction not stated) — named as a client by the Canada-located vendor (client list / customer story), dated: geotab.com | subject: Miami Gardens saves $60,000+ annually and generates $1.1M from vehicle resales with Geotab | Geotab | published by: the Canada-located vendor's own website | record: https://www.geotab.com/case-study/city-of-miami-gardens-cutting-costs-with-geotab/ | vendor in Canada because: vendor located in Canada (stories)=geotab.com | status rule: client listing on the vendor's own site (undated)
- **how_relationship_was_found**: tools/client_lists.py / dated_stories.py read the vendor's dated customer story / case study naming the buyer
- **keys**: lead:383e3b7756cc37be
- **tier**: D
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: City of Miami
- **buyer_website**: https://miamigardens-fl.gov/
- **buyer_address**: 18605 NW 27th Avenue, Miami Gardens, FL 33056
- **buyer_phone**: 305-622-8000
- **buyer_contact_evidence_url**: https://miamigardens-fl.gov/
- **buyer_legal_name_as_published**: City of Miami (stated on https://miamigardens-fl.gov/)
- **buyer_website_status**: site answers
- **buyer_type**: municipality / local government
- **buyer_sector**: government: municipal
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://miamigardens-fl.gov/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); website: site answers; invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); AP contact name: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: accountspayable@miamigardens-fl.gov
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.miamigardens-fl.gov/201/Documents-Forms
- **email_evidence_quote**: itle field p-name"> Accounts Payable </h4> <div class="field p-job-title">Accounts Payable</div> <div class="field u-email"><a href="mailto:accountspayable@miamigardens-fl.gov">Email Accounts Payable </a></div> <div class="field p-tel">Phone: 305-622-8000, ext. 2405</div> <br /> </li> <li
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: accountspayable@miamigardens-fl.gov (invoicing/AP) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-01 | page: https://www.miamigardens-fl.gov/201/Documents-Forms | quote: "itle field p-name"> Accounts Payable </h4> <div class="field p-job-title">Accounts Payable</div> <div class="field u-email"><a href="mailto:accountspayable@miam" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by Proofpoint | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00157
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by Proofpoint
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject; rua=mailto:fekmyvt3@ag.us.dmarcian.com, mailto:dmarc@miamigardens-fl.gov; ruf=mailto:dmarc@miamigardens-fl.gov; fo=1; adkim=r; aspf=r
- **dmarc_record_domain**: miamigardens-fl.gov
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 include:spf-00866001.pphosted.com include:us._netblocks.mimecast.com include:spf.constantcontact.com include:spf.protection.outlook.com ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_contact_name_as_published**: Lisa Fuentes Chief (Chief Financial Officer) (as printed by the organisation on its own accounts-payable page (as printed on https://www.miamigardens-fl.gov/201/Documents-Forms, re-read 2026-11-08))
- **invoice_portal_url**: supplier / vendor portal
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "portal_url": "supplier / vendor portal", "portal_kind": "actionable supplier / invoice portal named by the buyer"}
- **invoice_currency_derived**: USD (derived from the buyer's country; CAD if the parties agreed so)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: City of Miami (stated on https://miamigardens-fl.gov/) — 18605 NW 27th Avenue, Miami Gardens, FL 33056 ⏎ SUBMIT TO: accountspayable@miamigardens-fl.gov (invoicing/AP mailbox, confirmed by the referee) | portal (not confirmed as an invoice channel): supplier / vendor portal ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Geotab Inc. — 2440 Winston Park Dr, Oakville, ON, L6H 7V2, CA | GST/HST 825605769 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2019-08-01; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) | NEQ 1174740010 ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state  | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Miami Gardens saves $60,000+ annually and generates $1.1M from vehicle resales with Geotab | Geotab
- **invoice_card_json**: {"bill_to": {"legal_name": "City of Miami (stated on https://miamigardens-fl.gov/)", "legal_name_is_published": true, "address": "18605 NW 27th Avenue, Miami Gardens, FL 33056", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "accountspayable@miamigardens-fl.gov", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "supplier / vendor portal", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "portal (not confirmed as an invoice channel)"}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state ", "buyer_tax_status_is_published": false, "indicative_rate": "", "currency": "DERIVED: USD (derived from the buyer's country; C", "currency_is_published": false, "vendor_gst_hst": "825605769RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "Geotab Inc.", "bn9": "825605769 (recipient_business_number in the federal grant
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 73
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: finance mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: geotab.com
- **vendor_legal_name**: Geotab Inc.
- **vendor_trading_name**: geotab.com
- **vendor_registry_id**: Québec REQ (NEQ): 1174740010
- **vendor_registry_url**: https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises
- **vendor_registered_address**: 2440 Winston Park Drive, Oakville, (Ontario), L6H7V2
- **vendor_neq**: 1174740010 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_legal_form**: Société par actions ou compagnie — ONTARIO : Loi sur les sociétés par actions, L.R.O. 1990, c. B.16
- **vendor_activity_code**: CAE 3359 — - | secondary: -
- **vendor_employees_quebec**: De 11 à 25
- **vendor_last_annual_filing**: REQ annual declaration 2025
- **vendor_address**: 2440 Winston Park Dr, Oakville, ON, L6H 7V2, CA
- **vendor_country_basis**: vendor located in Canada (stories)=geotab.com
- **vendor_bn9**: 825605769 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2019-08-01; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)
- **vendor_gst_hst_derived**: 825605769RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://www.geotab.com/
- **vendor_phone**: 1-877-513-5167
- **vendor_contact_evidence_url**: https://www.geotab.com/contact-us/
- **vendor_logo_url**: https://www.geotab.com/images/geotabShareImage.4ca250e7efb65d78a8b5.jpg
- **vendor_website_status**: site answers
- **vendor_linkedin_url**: https://www.linkedin.com/company/geotab
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); registry identity: Québec REQ (NEQ): 1174740010 status Québec REQ (NEQ): Immatriculée (2019-07-26) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: federal grants & contributions disclosure (recipient_business_number); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2019-01-01; phone / role e-mails / logo: the vendor's own site, https://www.geotab.com/contact-us/ (tools/org_contacts.py, org_extras.py); website: https://www.geotab.com/ (site answers); NEQ: 1174740010 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Québec REQ (NEQ): Immatriculée (2019-07-26)
- **vendor_incorporation_date**: 2019-01-01
- **vendor_years_in_business**: 7.9 (since 2019-01-01, registry date)
- **vendor_bn_source**: federal grants & contributions disclosure (recipient_business_number)

## Contract
- **contract_status**: client listing on the vendor's own site (undated)
- **contract_title**: Miami Gardens saves $60,000+ annually and generates $1.1M from vehicle resales with Geotab | Geotab
- **contract_description**: Miami Gardens saves $60,000+ annually and generates $1.1M from vehicle resales with Geotab | Geotab (the record's title; the source publishes no separate description)
- **contract_link**: https://www.geotab.com/case-study/city-of-miami-gardens-cutting-costs-with-geotab/
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **invoice_currency_derived**: USD (derived from the buyer's country; CAD if the parties agreed so)
- **vendor_gst_hst_derived**: 825605769RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: yes — reference rule not published (quote the buyer's PO / order number when one is issued)
- **pay_on_sight_missing**: (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: City of Miami (stated on https://miamigardens-fl.gov/) — 18605 NW 27th Avenue, Miami Gardens, FL 33056 ⏎ SUBMIT TO: accountspayable@miamigardens-fl.gov (invoicing/AP mailbox, confirmed by the referee) | portal (not confirmed as an invoice channel): supplier / vendor portal ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Geotab Inc. — 2440 Winston Park Dr, Oakville, ON, L6H 7V2, CA | GST/HST 825605769 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2019-08-01; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) | NEQ 1174740010 ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state  | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Miami Gardens saves $60,000+ annually and generates $1.1M from vehicle resales with Geotab | Geotab
- **invoice_card_json**: {"bill_to": {"legal_name": "City of Miami (stated on https://miamigardens-fl.gov/)", "legal_name_is_published": true, "address": "18605 NW 27th Avenue, Miami Gardens, FL 33056", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "accountspayable@miamigardens-fl.gov", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "supplier / vendor portal", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "portal (not confirmed as an invoice channel)"}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state ", "buyer_tax_status_is_published": false, "indicative_rate": "", "currency": "DERIVED: USD (derived from the buyer's country; C", "currency_is_published": false, "vendor_gst_hst": "825605769RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "Geotab Inc.", "bn9": "825605769 (recipient_business_number in the federal grant
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 73
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: finance mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["accountspayable@miamigardens-fl.gov (invoicing/AP)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-01", "page: https://www.miamigardens-fl.gov/201/Documents-Forms", "quote: \"itle field p-name\"> Accounts Payable </h4> <div class=\"field p-job-title\">Accounts Payable</div> <div class=\"field u-email\"><a href=\"mailto:accountspayable@miam\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by Proofpoint", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00157"], "buyer_facts": ["address and phone: the buyer's own site, https://miamigardens-fl.gov/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "website: site answers", "invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "AP contact name: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "registry identity: Québec REQ (NEQ): 1174740010 status Québec REQ (NEQ): Immatriculée (2019-07-26) (scripts/enrichment_*: Corporations Canada / REQ / BC Or

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.miamigardens-fl.gov/201/Documents-Forms | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, miamigardens-fl.gov)
- **status**: ok
- **pages**: 3
- **v**: 2
- **legal_name_stated**: City of Miami
- **legal_name_stated_url**: https://miamigardens-fl.gov/
- **legal_name_stated_quote**: ith endless possibilities. It’s Where You Want to Be! News & Trending Topics Miami Dade College and City of Miami Gardens Partner to Develop 911 Dispatcher Workforce New registered apprenticeship program offers mu
- **tel_links**: 3056228000
- **language**: en
- **domain**: miamigardens-fl.gov
- **key**: lead:383e3b7756cc37be
- **name**: miamigardens-fl.gov
- **website**: https://miamigardens-fl.gov/
- **kind**: buyer
- **date**: 2026-11-08

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 1, "address": "18605 NW 27th Avenue, Miami Gardens, FL 33056", "address_country": "US", "address_url": "https://miamigardens-fl.gov/", "address_method": "pattern", "address_quote": "w All Events /Calendar.aspx Miami Gardens Social Media Contact Us MIAMI GARDENS 18605 NW 27th Avenue Miami Gardens, FL 33056 Phone: 305-622-8000 Hours: 7:00am - 7:00pm Days: Monday", "phone": "305-622-8000", "phone_url": "https://miamigardens-fl.gov/", "domain": "miamigardens-fl.gov", "key": "lead:383e3b7756cc37be", "name": "miamigardens-fl.gov", "website": "https://miamigardens-fl.gov/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, geotab.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: Geotab Inc
- **legal_name_url**: https://www.geotab.com/
- **legal_name_quote**: ns | MyAdmin Open in new window | Legal | Modern Slavery Statement | Terms of Use | Copyright 2026. Geotab Inc. and/or its affiliates. All Rights Reserved Open in new window Open in new window Open in new windo
- **logo_url**: https://www.geotab.com/images/geotabShareImage.4ca250e7efb65d78a8b5.jpg
- **logo_basis**: og:image of the home page (looks like a photo, not a logo: check before use)
- **domain**: geotab.com
- **key**: vendor:geotab.com
- **name**: geotab.com
- **website**: https://geotab.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Corporation
- **jsonld_name**: Geotab
- **jsonld_logo**: https://www.geotab.com/CMS-Media-production/Misc/logos/geotab-logo(full-colour-rgb).svg
- **jsonld_url**: https://www.geotab.com/
- **jsonld_same_as**: https://www.facebook.com/Geotab; https://twitter.com/geotab; https://www.linkedin.com/company/geotab; https://www.youtube.com/user/MyGeotab
- **jsonld_quote**: { "@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type":"Question","name":"What does Geotab do?","acceptedAnswer":{"@type":"Answer","text":"Geotab is the world’s #1 commercial telematics provider. We connect vehicles to the internet and provide web-based analytics to help org
- **jsonld_page**: https://www.geotab.com/
- **legal_name_stated**: Software Development Kit
- **legal_name_stated_url**: https://www.geotab.com/about/
- **legal_name_stated_quote**: nsight with Geotab’s unique open platform for fleet management. Integration is easy with the Geotab Software Development Kit (SDK) and APIs. Find customized solutions on the Geotab Marketplace, such as in-vehicle cameras, re
- **mentions**: {'payment_method': {'text': 'interact with other users', 'url': 'https://www.geotab.com/', 'quote': 'an average call wait-time of 26 seconds or less. Contact us Support Community Tap into experts and interact with other users. Open in new window Knowledge Base Access how-to guides, tips, and expertise. Open in new window Su'}}
- **linkedin_url**: https://www.linkedin.com/company/geotab

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "2440 Winston Park Drive, Oakville, Ontario, L6H 7V2", "address_country": "CA", "address_url": "https://www.geotab.com/contact-us/", "address_method": "pattern", "address_quote": "resses Canada Head Office Geotab Inc. 2440 Winston Park Drive Oakville, Ontario L6H 7V2, Canada Geotab Inc. 137 Glasgow Street, Unit 340 Kitchener, Ontario N2G 4X8, Ca", "phone": "1-877-513-5167", "phone_url": "https://www.geotab.com/contact-us/", "domain": "geotab.com", "key": "vendor:Geotab (Altitude by Geotab)", "name": "Geotab (Altitude by Geotab)", "website": "https://geotab.com/", "kind": "vendor", "date": "2026-11-08"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| v | Geotab Inc. | Q18164878 | official website on the organisation's domain (https://www.geotab.com/) + name |  | Geotab | Geotab | business | business corporation | Canada | 2000-00-00 | Oakville |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:383e3b7756cc37be",
 "ap_contact_team": {
  "emails": [
   "accountspayable@miamigardens-fl.gov"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "accountspayable@miamigardens-fl.gov",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.miamigardens-fl.gov/201/Documents-Forms",
    "quote": "itle field p-name\"> Accounts Payable </h4> <div class=\"field p-job-title\">Accounts Payable</div> <div class=\"field u-email\"><a href=\"mailto:accountspayable@miamigardens-fl.gov\">Email Accounts Payable </a></div> <div class=\"field p-tel\">Phone: 305-622-8000, ext. 2405</div> <br /> </li> <li",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "miamigardens-fl.gov",
    "task_id": "CL-WS-00157"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "web search for the buyer's invoicing / accounts payable page (the search only gave the address); the page then read by tools/deep_pages.py with the crawler's rules, no AI"
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
