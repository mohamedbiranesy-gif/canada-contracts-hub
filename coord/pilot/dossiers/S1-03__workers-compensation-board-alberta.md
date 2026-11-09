# S1-03 — Workers' Compensation Board – Alberta ⇄ Like 10 Inc.

Stratum: **S1_gold_complete_published_PO_rule** · pay on sight: yes · channel tier 1 · AP grade B · missing: —

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: The Workers' Compensation Board — 9925 107 Street, Edmonton, T5J 2S5, CA — buyer tax no. 124072513RT0001 (GST/HST number as printed on https://www.wcb.ab.ca/assets/pdfs/public/General_Terms_and_Conditions.pdf: "/ HST) - The Supplier acknowledges that the WCB is not subject to the Goods and Services Tax (GST) or Harmonized Sales Tax (HST). Exempt #124072513RT0001. 43. G")
SUBMIT TO: mailbox.finaccountspayable@wcb.ab.ca (invoicing/AP mailbox, confirmed by the referee) | invoice portal: https://wcbalberta-supplier.ivalua.app/
REFERENCE: contract AB-2024-07911 (apc_reference_number); tender RFQ2438AS (solicitation_number) | PO rule: not published
FROM / REMIT TO: LIKE 10 INC. — First Canadian Place 5700-100 King Street West, Toronto, ON, M5X 1C7 | GST/HST 846658219RT0001 (account derived from the BN9)
TAX: GST exemption number is #R124072513 (as printed on https://www.wcb.ab.ca/about-wcb/bid-and-vendor-information.html, re-read 2026-11-08) | CURRENCY: CAD | TERMS: payment can be issued to the worker within 14 calendar days (as printed on https://www.wcb.ab.ca/abo
DESCRIPTION: Workers' Compensation Board of Alberta - Request for Quotes - RFQ # 2438AS REDGATE SQL TOOLBELT AND SQL MONITOR RENEWAL AND REDGATE TDM PURC | AMOUNT: 445,250.52 CAD
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 96
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 13
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Workers' Compensation Board – Alberta (government ministry / agency, AB) — public contract / purchase award with a published end date (dated record): Like 10 Inc. | subject: Workers' Compensation Board of Alberta - Request for Quotes - RFQ # 2438AS REDGATE SQL TOOLBELT AND SQL MONITOR RENEWAL AND REDGATE TDM PURCHASE  | instrument: contract award (OPEN-COMPETITIVE) | contract number: AB-2024-07911 (apc_reference_number) | solicitation: RFQ2438AS (solicitation_number); 19e4528b-a112-439c-bb6f-d25203c61e09 (opportunity_id) | all identifiers: {"apc_reference_number": "AB-2024-07911", "opportunity_id": "19e4528b-a112-439c-bb6f-d25203c61e09", "solicitation_number": "RFQ2438AS", "award_id": "f0567736-d88f-44a5-9597-0c4b0e0f847a", "supplier_id": null, "parent_id": null} | value: 445250.52 CAD | awarded 2024-11-18, start 2024-10-01, end 2027-11-18 | published by: Alberta Purchasing Connection (APC) - awarded opportunities | record: https://purchasing.alberta.ca/posting/AB-2024-07911 | vendor in Canada because: awards[].address.country == 'CA' (stateProvince 'CA-ON') | status rule: active (published end date today or later) | this buyer has 33 records with Canada-located vendors (31 distinct vendors; 20 in the last 12 months; latest 2026-09-29)
- **how_relationship_was_found**: the award record was harvested from the public procurement source named in `source` (scripts/<source> pipeline), matched to the buyer by its canonical name/key, and the vendor's Canada location read from the source's own vendor address/country field (`vendor_country_basis`)
- **keys**: b:8a39bba184eeb766
- **tier**: A
- **grade**: 4
- **records_with_this_vendor**: 1

## Buyer
- **buyer**: Workers' Compensation Board – Alberta
- **buyer_website**: https://www.wcb.ab.ca
- **buyer_address**: 9925 107 Street, Edmonton, T5J 2S5, CA
- **buyer_phone**: +1-855-498-7969
- **buyer_contact_evidence_url**: https://wcb.ab.ca/
- **buyer_legal_name_as_published**: The Workers' Compensation Board
- **buyer_bn_as_published**: 124072513RT0001 (GST/HST number as printed on https://www.wcb.ab.ca/assets/pdfs/public/General_Terms_and_Conditions.pdf: "/ HST) - The Supplier acknowledges that the WCB is not subject to the Goods and Services Tax (GST) or Harmonized Sales Tax (HST). Exempt #124072513RT0001. 43. G")
- **buyer_bn_program**: RT (GST/HST program account)
- **buyer_gst_hst_derived**: 124072513RT0001 (printed by the buyer itself; not derived)
- **buyer_logo_url**: https://wcb.ab.ca/assets/images/WCB-logo.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/wcbalberta
- **buyer_type**: government ministry / agency
- **buyer_sector**: government: provincial / federal
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://wcb.ab.ca/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers; AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoicing requirements: the lane's AP page (https://www.wcb.ab.ca/contact); payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoice portal: the lane's AP page (https://www.wcb.ab.ca/contact)
- **buyer_tax_exempt_status**: GST exemption number is #R124072513 (as printed on https://www.wcb.ab.ca/about-wcb/bid-and-vendor-information.html, re-read 2026-11-08)
- **buyer_tax_status_derived**: provincial government entity in Alberta: a LISTED entity does not pay GST/HST at the point of purchase when an authorized official certifies the purchase — ask for the exemption certificate or certification clause before invoicing without tax — GST/HST Memorandum 18-2 para. 24 (https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Listed entities in Manitoba, Saskatchewan, Alberta, the Northwest Territories and Yukon do not pay the GST/HST on purchases of taxable property and services, provided that an authorized official of the listed entity provides sufficient evidence"); derived from buyer type and province, not published by the buyer; whether this body is a listed entity is not verified
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: mailbox.finaccountspayable@wcb.ab.ca
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.wcb.ab.ca/contact
- **email_evidence_quote**: .ab.ca Accounts Payable Email: mailbox.finaccountspayable@wcb.ab.ca
- **email_evidence_context**: WCB bid opportunities and participate in the bidding process. Millard Health Business Office Tel: 780-498-3312 Fax: 780-498-3907 For physician contracts, contact Health Care Services . Medical Aid Email: medical.aid@wcb.ab.ca Accounts Payable Email: mailbox.finaccountspayable@wcb.ab.ca Dispute Resolution and Decision Review Body Tel: 780-498-4480 Fax: 780-498-7855 Toll-free In Alberta: 1-800-661-5419 Outside Alberta: 1-800-661-9608 Fax (in Alberta): 1-800-661-1993 Employer inquiries myWCB mobile app for employers Send us a message (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: mailbox.finaccountspayable@wcb.ab.ca (invoicing/AP) | researched by the ChatGPT/Codex agent (lane chatgpt) (page opened and quoted) on 2026-10-27 | page: https://www.wcb.ab.ca/contact | quote: ".ab.ca Accounts Payable Email: mailbox.finaccountspayable@wcb.ab.ca" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Proofpoint | lane file: chatgpt/chatgpt_buyer_ap_results_batch07.csv task CH-AP-00616
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Proofpoint
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject; fo=1; rua=mailto:dmarc_rua@emaildefense.proofpoint.com; ruf=mailto:dmarc_ruf@emaildefense.proofpoint.com
- **dmarc_record_domain**: wcb.ab.ca
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 ip4:207.229.57.13 ip4:207.229.57.14 ip4:204.191.37.70 ip4:207.229.10.238 include:oktamail.wcb.ab.ca include:spf.protection.outlook.com include:spf-0042bd01.pphosted.com include:spf-ca.emailsignatures365.com -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_phone**: 780-498-3312 (as printed on https://www.wcb.ab.ca/contact, re-read 2026-11-08)
- **invoicing_requirements**: Non-claim suppliers can submit invoices and track payments in the WCB-Alberta supplier portal. Public guidance expressly excludes healthcare providers from this portal; AP contact handles invoice inquiries and non-claim-related supplier payments. No public invoice-format requirements identified on r
- **payment_terms_as_published**: payment can be issued to the worker within 14 calendar days (as printed on https://www.wcb.ab.ca/about-wcb/procedures-manual/initial-entitlement-decision.html, re-read 2026-11-08)
- **invoice_portal_url**: https://wcbalberta-supplier.ivalua.app/
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel published by the buyer; the e-mail is the contact)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "payment_terms": "payment can be issued to the worker within 14 calendar days (as printed on https://www.wcb.ab.ca/about-wcb/procedures-manual/initial-entitlement-decision.html, re-read 2026-11-08)", "portal_url": "https://wcbalberta-supplier.ivalua.app/", "portal_kind": "actionable supplier / invoice portal named by the buyer", "ap_phone": "780-498-3312 (as printed on https://www.wcb.ab.ca/contact, re-read 2026-11-08)", "requirements_text": "Non-claim suppliers can submit invoices and track payments in the WCB-Alberta supplier portal. Public guidance expressly excludes healthcare providers from this portal; AP contact handles invoice inquiries and non-claim-related supplier payments. No public invoice-format requirements identified on r"}
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: The Workers' Compensation Board — 9925 107 Street, Edmonton, T5J 2S5, CA — buyer tax no. 124072513RT0001 (GST/HST number as printed on https://www.wcb.ab.ca/assets/pdfs/public/General_Terms_and_Conditions.pdf: "/ HST) - The Supplier acknowledges that the WCB is not subject to the Goods and Services Tax (GST) or Harmonized Sales Tax (HST). Exempt #124072513RT0001. 43. G") ⏎ SUBMIT TO: mailbox.finaccountspayable@wcb.ab.ca (invoicing/AP mailbox, confirmed by the referee) | invoice portal: https://wcbalberta-supplier.ivalua.app/ ⏎ REFERENCE: contract AB-2024-07911 (apc_reference_number); tender RFQ2438AS (solicitation_number) | PO rule: not published ⏎ FROM / REMIT TO: LIKE 10 INC. — First Canadian Place 5700-100 King Street West, Toronto, ON, M5X 1C7 | GST/HST 846658219RT0001 (account derived from the BN9) ⏎ TAX: GST exemption number is #R124072513 (as printed on https://www.wcb.ab.ca/about-wcb/bid-and-vendor-information.html, re-read 2026-11-08) | CURRENCY: CAD | TERMS: payment can be issued to the worker within 14 calendar days (as printed on https://www.wcb.ab.ca/abo ⏎ DESCRIPTION: Workers' Compensation Board of Alberta - Request for Quotes - RFQ # 2438AS REDGATE SQL TOOLBELT AND SQL MONITOR RENEWAL AND REDGATE TDM PURC | AMOUNT: 445,250.52 CAD
- **invoice_card_json**: {"bill_to": {"legal_name": "The Workers' Compensation Board", "legal_name_is_published": true, "address": "9925 107 Street, Edmonton, T5J 2S5, CA", "address_is_the_invoice_address": false, "tax_number": "124072513RT0001 (GST/HST number as printed on https://www.wcb.ab.ca/assets/pdfs/public/General_Terms_and_Conditions.pdf: \"/ HST) - The Supplier acknowledges that the WCB is not subject to the Goods and Services Tax (GST) or Harmonized Sales Tax (HST). Exempt #124072513RT0001. 43. G\")", "language": "en"}, "submit_to": {"email": "mailbox.finaccountspayable@wcb.ab.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "https://wcbalberta-supplier.ivalua.app/", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "AB-2024-07911 (apc_reference_number)", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: AB-2024-07911 (apc_reference_number) — source ca_alberta_apc"}, "terms": {"payment_terms": "payment can be issued to the worker within 14 calendar days (as printed on https://www.wcb.ab.ca/about-wcb/procedures-manual/initial-entitlement-decision.html, re-read 2026-11-08)", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "GST exemptio
- **invoice_readiness**: 10/11 invoice elements present
- **invoice_missing**: PO rule
- **ap_grade**: B
- **ap_score**: 82
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; payment terms published; currency known; invoice format / requirements published; AP phone or AP contact | missing: finance mailbox; PO rule published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published PO rule
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: contract or agreement number: AB-2024-07911 (apc_reference_number) — source ca_alberta_apc

## Vendor
- **vendor**: Like 10 Inc.
- **vendor_legal_name**: LIKE 10 INC.
- **vendor_registry_id**: Corporations Canada (corporation number): 6833934; corporation number 6833934 (Corporations Canada (open data))
- **vendor_registry_url**: https://ised-isde.canada.ca/cc/lgcy/fdrlCrpDtls.html?corpId=6833934
- **vendor_registered_address**: 100 King Street West, Suite 5700, Toronto, ON, M5X 1A9, CA
- **vendor_legal_form**: Canada Business Corporations Act (Canada (federal))
- **vendor_directors_range**: 1 to 1 directors (Corporations Canada)
- **vendor_last_annual_filing**: ; Corporations Canada anniversary 2007-09-04
- **vendor_address**: First Canadian Place 5700-100 King Street West, Toronto, ON, M5X 1C7
- **vendor_country_basis**: awards[].address.country == 'CA' (stateProvince 'CA-ON')
- **vendor_bn9**: 846658219
- **vendor_gst_hst_derived**: 846658219RT0001
- **vendor_website**: https://www.like10.com/
- **vendor_emails**: info@like10.com
- **vendor_facts_provenance**: name and address: the record's vendor block (Alberta Purchasing Connection (APC) - awarded opportunities); registry identity: Corporations Canada (corporation number): 6833934; corporation number 6833934 (Corporations Canada (open data)) status Corporations Canada (corporation number): Active (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; exact); BN9: corporations_canada 6833934 (exact match); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2007-09-04; website: https://www.like10.com/
- **vendor_concentration_top_share**: Optiv Canada Inc.: 6% of 33 records
- **vendor_registry_status**: Corporations Canada (corporation number): Active
- **vendor_registry_match_level**: exact
- **vendor_incorporation_date**: 2007-09-04
- **vendor_years_in_business**: 19.2 (since 2007-09-04, registry date)
- **vendor_bn_source**: corporations_canada 6833934 (exact match)

## Contract
- **contract_status**: active (published end date today or later)
- **contract_reference**: {"apc_reference_number": "AB-2024-07911", "opportunity_id": "19e4528b-a112-439c-bb6f-d25203c61e09", "solicitation_number": "RFQ2438AS", "award_id": "f0567736-d88f-44a5-9597-0c4b0e0f847a", "supplier_id": null, "parent_id": null}
- **contract_title**: Workers' Compensation Board of Alberta - Request for Quotes - RFQ # 2438AS REDGATE SQL TOOLBELT AND SQL MONITOR RENEWAL AND REDGATE TDM PURCHASE 
- **commodity**: 81000000 Engineering and Research and Technology Based Services > Computer services > Software maintenance and support > Database management system software mai
- **contract_description**: The Workers’ Compensation Board – Alberta (WCB) is requesting quotes for maintenance and support on the WCB’s existing Redgate SQL Toolbelt and SQL Monitor perpetual licenses, Redgate SQL Monitor subscriptions and Redgate Test Data Manager (TDM). 
- **contract_or_agreement_number**: AB-2024-07911 (apc_reference_number)
- **solicitation_or_tender_number**: RFQ2438AS (solicitation_number); 19e4528b-a112-439c-bb6f-d25203c61e09 (opportunity_id)
- **award_or_notice_id**: f0567736-d88f-44a5-9597-0c4b0e0f847a (award_id)
- **commodity_codes**: UNSPSC 81000000 (Engineering and Research and Technology Based Services > Computer services > Sof); GSIN J
- **contract_value**: 445250.52
- **currency**: CAD
- **award_date**: 2024-11-18
- **start_date**: 2024-10-01
- **end_date**: 2027-11-18
- **contract_link**: https://purchasing.alberta.ca/posting/AB-2024-07911
- **source**: Alberta Purchasing Connection (APC) - awarded opportunities
- **contracts_with_canadian_suppliers**: 33
- **records_last_12_months**: 20
- **record_sources**: Alberta Purchasing Connection (APC) - awarded opportunities (33)
- **records_with_this_vendor**: 1
- **records_in_contract_dataset**: 33 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: Building and Facility Construction and Maintenance Services  (10); Information Technology Broadcasting and Telecommunications > (6); Office Equipment and Accessories and Supplies > Office suppl (2)

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 124072513RT0001 (printed by the buyer itself; not derived)
- **buyer_tax_status_derived**: provincial government entity in Alberta: a LISTED entity does not pay GST/HST at the point of purchase when an authorized official certifies the purchase — ask for the exemption certificate or certification clause before invoicing without tax — GST/HST Memorandum 18-2 para. 24 (https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Listed entities in Manitoba, Saskatchewan, Alberta, the Northwest Territories and Yukon do not pay the GST/HST on purchases of taxable property and services, provided that an authorized official of the listed entity provides sufficient evidence"); derived from buyer type and province, not published by the buyer; whether this body is a listed entity is not verified
- **tax_rate_indicative_derived**: GST 5% (AB) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **vendor_gst_hst_derived**: 846658219RT0001

## Pay on sight / grades
- **pay_on_sight**: yes
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: The Workers' Compensation Board — 9925 107 Street, Edmonton, T5J 2S5, CA — buyer tax no. 124072513RT0001 (GST/HST number as printed on https://www.wcb.ab.ca/assets/pdfs/public/General_Terms_and_Conditions.pdf: "/ HST) - The Supplier acknowledges that the WCB is not subject to the Goods and Services Tax (GST) or Harmonized Sales Tax (HST). Exempt #124072513RT0001. 43. G") ⏎ SUBMIT TO: mailbox.finaccountspayable@wcb.ab.ca (invoicing/AP mailbox, confirmed by the referee) | invoice portal: https://wcbalberta-supplier.ivalua.app/ ⏎ REFERENCE: contract AB-2024-07911 (apc_reference_number); tender RFQ2438AS (solicitation_number) | PO rule: not published ⏎ FROM / REMIT TO: LIKE 10 INC. — First Canadian Place 5700-100 King Street West, Toronto, ON, M5X 1C7 | GST/HST 846658219RT0001 (account derived from the BN9) ⏎ TAX: GST exemption number is #R124072513 (as printed on https://www.wcb.ab.ca/about-wcb/bid-and-vendor-information.html, re-read 2026-11-08) | CURRENCY: CAD | TERMS: payment can be issued to the worker within 14 calendar days (as printed on https://www.wcb.ab.ca/abo ⏎ DESCRIPTION: Workers' Compensation Board of Alberta - Request for Quotes - RFQ # 2438AS REDGATE SQL TOOLBELT AND SQL MONITOR RENEWAL AND REDGATE TDM PURC | AMOUNT: 445,250.52 CAD
- **invoice_card_json**: {"bill_to": {"legal_name": "The Workers' Compensation Board", "legal_name_is_published": true, "address": "9925 107 Street, Edmonton, T5J 2S5, CA", "address_is_the_invoice_address": false, "tax_number": "124072513RT0001 (GST/HST number as printed on https://www.wcb.ab.ca/assets/pdfs/public/General_Terms_and_Conditions.pdf: \"/ HST) - The Supplier acknowledges that the WCB is not subject to the Goods and Services Tax (GST) or Harmonized Sales Tax (HST). Exempt #124072513RT0001. 43. G\")", "language": "en"}, "submit_to": {"email": "mailbox.finaccountspayable@wcb.ab.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "https://wcbalberta-supplier.ivalua.app/", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "AB-2024-07911 (apc_reference_number)", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: AB-2024-07911 (apc_reference_number) — source ca_alberta_apc"}, "terms": {"payment_terms": "payment can be issued to the worker within 14 calendar days (as printed on https://www.wcb.ab.ca/about-wcb/procedures-manual/initial-entitlement-decision.html, re-read 2026-11-08)", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "GST exemptio
- **invoice_readiness**: 10/11 invoice elements present
- **invoice_missing**: PO rule
- **ap_grade**: B
- **ap_score**: 82
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; payment terms published; currency known; invoice format / requirements published; AP phone or AP contact | missing: finance mailbox; PO rule published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published PO rule
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **facts_provenance_json**: {"mailbox": ["mailbox.finaccountspayable@wcb.ab.ca (invoicing/AP)", "researched by the ChatGPT/Codex agent (lane chatgpt) (page opened and quoted) on 2026-10-27", "page: https://www.wcb.ab.ca/contact", "quote: \".ab.ca Accounts Payable Email: mailbox.finaccountspayable@wcb.ab.ca\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Proofpoint", "lane file: chatgpt/chatgpt_buyer_ap_results_batch07.csv task CH-AP-00616"], "buyer_facts": ["address and phone: the buyer's own site, https://wcb.ab.ca/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers", "AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoicing requirements: the lane's AP page (https://www.wcb.ab.ca/contact)", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoice portal: the lane's AP page (https://www.wcb.ab.ca/contact)"], "vendor_facts": ["name and address: the record's vendor block (Alberta Purchasing Connection (APC) 

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.wcb.ab.ca/contact | 2026-11-08 | ok |  |  |  | 780-498-3312 |  |  |  |  |  |

## Buyer site facts (org_extras, wcb.ab.ca)
- **status**: ok
- **pages**: 4
- **language**: en
- **legal_name**: The Workers' Compensation Board
- **legal_name_url**: https://wcb.ab.ca/
- **legal_name_quote**: oll free at to reach a fatality claim specialist directly. View all contact information Copyright © The Workers' Compensation Board – Alberta. All rights reserved. Privacy & terms of use Accessibility Help Follow us on LinkedIn Soc
- **logo_url**: https://wcb.ab.ca/assets/images/WCB-logo.png
- **logo_basis**: logo image in the site header
- **domain**: wcb.ab.ca
- **key**: b:8a39bba184eeb766
- **name**: Workers' Compensation Board – Alberta
- **website**: https://wcb.ab.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Industry Custom Pricing
- **legal_name_stated_url**: https://wcb.ab.ca/about-wcb/careers/
- **legal_name_stated_quote**: emiums Partnerships in Injury Reduction (PIR) Occupational Injury Service (OIS) Safety associations Industry Custom Pricing Modified work programs Pay premiums Annual returns Premium review and appeal process Resources WCB
- **mentions**: {'payment_method': {'text': 'interactions with you', 'url': 'https://wcb.ab.ca/about-wcb/company-information/code-of-rights-and-conduct.html', 'quote': "what we believe in—a way to show you, our clients, exactly how we hold ourselves accountable in our interactions with you. Workplace injuries have the potential to profoundly impact workers' and employers' lives. When thi"}}
- **linkedin_url**: https://www.linkedin.com/company/wcbalberta
- **tel_links**: +1-855-498-7969

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 1, "phone": "+1-855-498-7969", "phone_url": "https://wcb.ab.ca/", "domain": "wcb.ab.ca", "key": "vd:wcb.ab.ca", "name": "Workers Compensation Board of Alberta", "website": "https://wcb.ab.ca/", "kind": "vendor", "date": "2026-11-03"}

## Vendor site facts (org_extras, domain unknown)
_not read_

## Vendor role mailboxes found on its site (org_contacts)
_not read_

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | LIKE 10 INC. | found | LIKE 10 INC. | 846658219 | 6833934 | CC | Business Corporation | Active | 2007-09-04 | Toronto | Ontario |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=LIKE%2010%20INC. | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | api_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | LIKE 10 INC. | found | LIKE 10 INC. | 846658219 | corporation number 6833934 | Corporations Canada (open data) | Canada Business Corporations Act | Active | 2007-09-04 | Toronto | ON | 100 King Street West, Suite 5700, Toronto, ON, M5X 1A9 | https://open.canada.ca/data/en/dataset/0032ce54-c5dd-4b66-99a0-320a7b5e99f2 | 2026-11-08 |

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Workers' Compensation Board – Alberta |  |  |  |  |  |  |  |  |  |  |
| b | LIKE 10 INC. |  |  |  |  |  |  |  |  |  |  |
| v | LIKE 10 INC. |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "b:8a39bba184eeb766",
 "ap_contact_team": {
  "emails": [
   "mailbox.finaccountspayable@wcb.ab.ca",
   "addressbooklibrarians@wcb.ab.ca",
   "contact.centre@wcb.ab.ca"
  ],
  "invoice_portal": "https://wcbalberta-supplier.ivalua.app/",
  "phone": "780-498-7704",
  "mailing_address": null,
  "invoicing_requirements": "Non-claim suppliers can submit invoices and track payments in the WCB-Alberta supplier portal. Public guidance expressly excludes healthcare providers from this portal; AP contact handles invoice inquiries and non-claim-related supplier payments. No public invoice-format requirements identified on reviewed pages.",
  "evidence": [
   {
    "email": "mailbox.finaccountspayable@wcb.ab.ca",
    "type": "accounts_payable",
    "invoice_portal": "https://wcbalberta-supplier.ivalua.app/",
    "phone": null,
    "mailing_address": null,
    "requirements": "Non-claim suppliers can submit invoices and track payments in the WCB-Alberta supplier portal. Public guidance expressly excludes healthcare providers from this portal; AP contact handles invoice inquiries and non-claim-related supplier payments. No public invoice-format requirements identified on reviewed pages.",
    "applies_to": "this_unit_only",
    "page_url": "https://www.wcb.ab.ca/contact",
    "quote": ".ab.ca Accounts Payable Email: mailbox.finaccountspayable@wcb.ab.ca",
    "retrieved_date": "2026-10-27",
    "found_by": "chatgpt",
    "verification": "verified",
    "source_file": "chatgpt_buyer_ap_results_batch07.csv",
    "org": "Workers' Compensation Board of Alberta",
    "task_id": "CH-AP-00616"
   },
   {
    "email": "addressbooklibrarians@wcb.ab.ca",
    "type": "supplier_payment",
    "invoice_portal": null,
    "phone": "780-498-7704",
    "mailing_address": null,
    "requirements": null,
    "applies_to": "this_unit_only",
    "page_url": "https://www.wcb.ab.ca/contact",
    "quote": "Claims Authorization & Processing Tel: 780-498-7704 Email: addressbooklibrarians@wcb.ab.ca",
    "retrieved_date": "2026-10-27",
    "found_by": "chatgpt",
    "verification": "verified",
    "source_file": "chatgpt_buyer_ap_results_batch07.csv",
    "org": "Workers' Compensation Board of Alberta",
    "task_id": "CH-AP-00616"
   },
   {
    "email": "contact.centre@wcb.ab.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.wcb.ab.ca/assets/pdfs/providers/pharmacy_billing.pdf",
    "quote": "es may be submitted:  By mail to PO Box 2415, Edmonton AB, T5J 2S5  By fax to (780) 427-5863 or toll free at 1-800-661-1993  By email to contact.centre@wcb.ab.ca Inquiries Please allow WCB six to eight weeks to process claims. If you have not received payment after this time, please fax",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Workers' Compensation Board – Alberta",
    "task_id": "CL-WS-00001"
   }
  ]
 },
 "research_status": {
  "found": 3
 },
 "queries_tried": [
  "site:wcb.ab.ca supplier invoice accounts payable; opened current home, Bid and vendor information and Contact us",
  "site:wcb.ab.ca supplier invoice accounts payable; opened official Contact us physician/healthcare-provider section",
  "web search for the buyer's invoicing / accounts payable page (the search only gave the address); the page then read by tools/deep_pages.py with the crawler's rules, no AI"
 ],
 "ingested_at": "2026-11-09T16:04:50Z"
}
```

## PO-level open data naming this buyer
_none_

## Contract records between the pair (dataset)
| record_id | source | status | title | value | currency | start | end | identifiers | link |
|---|---|---|---|---|---|---|---|---|---|
| ca_alberta_apc:AB-2024-07911:f0567736-d88f-44a5-9597-0c4b0e0f847a | ca_alberta_apc | ongoing | Workers' Compensation Board of Alberta - Request for Quotes - RFQ # 2438AS REDGATE SQL TOOLBELT AND SQL MONITOR RENEWAL AND REDGATE TDM PURCHASE  | 445250.52 | CAD |  |  | {"apc_reference_number": "AB-2024-07911", "opportunity_id": "19e4528b-a112-439c-bb6f-d25203c61e09", "solicitation_number": "RFQ2438AS", "award_id": "f0567736-d88f-44a5-9597-0c4b0e0f847a", "supplier_id | https://purchasing.alberta.ca/posting/AB-2024-07911 |

## The buyer's other Canadian-vendor records (first 60 of 32)
| record_id | vendor | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_alberta_apc:AB-2023-02547:b9576c1b-7921-4704-8aaf-a1dee83ea21d | Optiv Canada Inc. | Workers' Compensation Board of Alberta - Request for Expression of Interest - Privileged Access Management | 720335.73 |  |  | https://purchasing.alberta.ca/posting/AB-2023-02547 |
| ca_alberta_apc:AB-2023-06303:2f5aa8cd-6b8d-4f22-8b45-026794b8e258 | Optiv Canada Inc. | Workers' Compensation Board of Alberta - Request for Proposal - Privileged Access Management |  |  |  | https://purchasing.alberta.ca/posting/AB-2023-06303 |
| ca_alberta_apc:AB-2024-03857:f41fd17d-5fda-4fca-95b4-cf60fa132662 | Staples Canada ULC | Workers' Compensation Board of Alberta - Request for Proposal - Stationery and Office Products | 1080000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2024-03857 |
| ca_alberta_apc:AB-2024-03929:5525a5cd-2c8b-49e6-a634-4a1643cca180 | Connex Telecommunications Inc. | Workers' Compensation Board of Alberta - Request for Quotes - Calabrio Cloud - Call Recording & Quality Management Subscription Renewal | 293463.36 |  |  | https://purchasing.alberta.ca/posting/AB-2024-03929 |
| ca_alberta_apc:AB-2024-04073:1937f2cd-e0bd-407b-a19e-165098604c9e | PC Corp | Workers' Compensation Board of Alberta - Request for Quotes - Tripp Lite UPS Units | 170468.0 |  |  | https://purchasing.alberta.ca/posting/AB-2024-04073 |
| ca_alberta_apc:AB-2024-07238:dc413948-c395-4be2-a73f-e6ea0af04326 | Cattan Technologies Inc. | Workers' Compensation Board of Alberta - Request for Quotes - RFQ #2435AS-BROCADE G730 OR OEM EQUIVALENT SAN SWITCH   | 470194.22 |  |  | https://purchasing.alberta.ca/posting/AB-2024-07238 |
| ca_alberta_apc:AB-2024-07301:4fd8fc05-302b-4a89-93f6-8cf588604c9b | Pace Solutions Corp | Workers' Compensation Board of Alberta - Request for Quotes - RFQ2429 Chemical Water Treatment  | 97000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2024-07301 |
| ca_alberta_apc:AB-2024-09447:1aa9f181-33cd-4260-bbaa-0ecce10cf01d | Optrics Inc. | Workers' Compensation Board of Alberta - Request for Quotes - 2442JC ManageEngine Password Manager Pro Premium Subscription Renewal RFQ | 58024.77 |  |  | https://purchasing.alberta.ca/posting/AB-2024-09447 |
| ca_alberta_apc:AB-2025-00684:6feceba9-2deb-4491-acc2-f3c28ea7cb55 | Staples Professional Inc. | Workers' Compensation Board of Alberta - Request for Quotes - Bond Paper Requirements | 400000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-00684 |
| ca_alberta_apc:AB-2025-01246:599623f9-27dc-4161-bfcc-2adf5fcf8827 | Direct Energy Marketing Limited | Workers' Compensation Board of Alberta - Request for Proposal - 2508KF - Natural Gas Supply Services  | 796400.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-01246 |
| ca_alberta_apc:AB-2025-01701:5123299f-8d54-4c2a-b203-367564a720b7 | Edmonton Elevator Services Cor | Workers' Compensation Board of Alberta - Invitation to Bid - Central Building Elevator Modernization | 1284219.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-01701 |
| ca_alberta_apc:AB-2025-04765:e387b04f-38bc-4783-aa6d-e369719d75ff | 1186254 Alberta Ltd. | Workers' Compensation Board of Alberta - PQD 2416JC General Contractors for Minor Residential Home Modifications |  |  |  | https://purchasing.alberta.ca/posting/AB-2025-04765 |
| ca_alberta_apc:AB-2025-04765:ed648a0a-3203-4bf5-94cc-cc99ffd96142 | On Point Restore | Workers' Compensation Board of Alberta - PQD 2416JC General Contractors for Minor Residential Home Modifications |  |  |  | https://purchasing.alberta.ca/posting/AB-2025-04765 |
| ca_alberta_apc:AB-2025-04765:34067818-1f7c-4e7d-8406-bcfbed053a83 | Wenramp Inc. | Workers' Compensation Board of Alberta - PQD 2416JC General Contractors for Minor Residential Home Modifications |  |  |  | https://purchasing.alberta.ca/posting/AB-2025-04765 |
| ca_alberta_apc:AB-2025-04765:46b9a9d6-09e2-415f-bc17-668867f11277 | Finish First Builders Inc. | Workers' Compensation Board of Alberta - PQD 2416JC General Contractors for Minor Residential Home Modifications |  |  |  | https://purchasing.alberta.ca/posting/AB-2025-04765 |
| ca_alberta_apc:AB-2025-04765:e7517727-712a-40cf-848b-2d9ae9324adb | NSG CONTRACTORS LTD. | Workers' Compensation Board of Alberta - PQD 2416JC General Contractors for Minor Residential Home Modifications |  |  |  | https://purchasing.alberta.ca/posting/AB-2025-04765 |
| ca_alberta_apc:AB-2025-04850:2d3d3ea5-c566-440b-864f-4d0f7326fbef | Park Landscaping Ltd. | Workers' Compensation Board of Alberta - Request for Proposal - RFP 2514AM Grounds Maintenance Services | 1166704.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-04850 |
| ca_alberta_apc:AB-2025-06023:727f99ff-1b55-432d-9626-c7e2dee2f324 | StorageVault Canada O/A RecordXpress | Workers' Compensation Board of Alberta - Request for Proposal - RFP2524 Shredding Services - Edmonton & Calgary | 125449.78 |  |  | https://purchasing.alberta.ca/posting/AB-2025-06023 |
| ca_alberta_apc:AB-2025-06108:41310ac2-08c6-453f-bffe-d8f2a53b4dc9 | PricewaterhouseCoopers LLP MAIN NATIONAL ACCOUNT | Workers' Compensation Board of Alberta - Negotiated Request for Proposal - RFP2528KF - Customer Service Workload Intiative | 3000000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-06108 |
| ca_alberta_apc:AB-2025-07080:c41969ff-9a0e-4ef5-979b-b6d41071687d | Interworks Contracting Ltd | Workers' Compensation Board of Alberta - Invitation to Bid - 2534KF - Central Building C1 General Contractor  | 603125.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-07080 |
| ca_alberta_apc:AB-2025-07516:b02471e1-d3f9-4e26-a9df-b56ffda78cb4 | Cam Clark Ford Airdrie | Workers' Compensation Board of Alberta - Request for Quotes - 2536KF - Corporate Vehicle RFQ | 258000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-07516 |
| ca_alberta_apc:AB-2025-07966:4ddbdca0-1d42-4ccb-b3c3-3bd282cf4715 | Burke Group of Companies Ltd. | Workers' Compensation Board of Alberta - Request for Quotes - RFQ 2522SH Envelope Requirements | 347691.9 |  |  | https://purchasing.alberta.ca/posting/AB-2025-07966 |
| ca_alberta_apc:AB-2026-01840:1b945fc5-2fb3-465d-bfb7-0a428a7592ac | Fibertel Communications Canada Inc | Workers' Compensation Board of Alberta - Request for Proposal - RFP2605 Network Cabling Services | 250000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2026-01840 |
| ca_alberta_apc:AB-2026-02807:48ef1b71-ca99-4fa4-8af1-8ee1499f69c7 | AlecTech Inc. | Workers' Compensation Board of Alberta - Request for Proposal - 2608MM Request for Privacy Breach Reporting Software Solution | 243263.0 |  |  | https://purchasing.alberta.ca/posting/AB-2026-02807 |
| ca_alberta_apc:AB-2026-03246:78c762c0-04ce-44d3-b2c6-a4c01a554af1 | Mitratech Holdings (Canada) Inc. | Workers' Compensation Board of Alberta - Request for Quotes - RFQ 2615MM for Mitratech TeamConnect Maintenance and Support Renewal Services | 547942.0 |  |  | https://purchasing.alberta.ca/posting/AB-2026-03246 |
| ca_alberta_apc:AB-2026-03491:1595f935-6a2d-4d7a-84cb-bb50b79fadd8 | Calanah Builders Ltd. | Workers' Compensation Board of Alberta - Invitation to Bid - IFB 2619JC Residential Home Modification - Red Deer | 508825.0 |  |  | https://purchasing.alberta.ca/posting/AB-2026-03491 |
| ca_alberta_apc:AB-2026-03869:ac11203a-e254-4cd2-8579-5c0887805d61 | HOK Architects Corporation | Workers' Compensation Board of Alberta - Request for Proposal - RFP2620KF Multi Site Master Plan Consulting  | 359720.0 |  |  | https://purchasing.alberta.ca/posting/AB-2026-03869 |
| ca_alberta_apc:AB-2026-04505:6e573679-886c-4a98-972a-5ff5ad42ccd6 | M&A IT Tech Inc. | Workers' Compensation Board of Alberta - Request for Quotes - RFQ 2628TB Pluralsight Enterprise Subscription Renewal | 153158.4 |  |  | https://purchasing.alberta.ca/posting/AB-2026-04505 |
| ca_alberta_apc:AB-2026-04616:3aef7c67-6fd3-4dd5-a12c-6218fddc579c | Casman | Workers' Compensation Board of Alberta - Invitation to Bid - IFB2625KF - Home Modification Edmonton  | 135676.0 |  |  | https://purchasing.alberta.ca/posting/AB-2026-04616 |
| ca_alberta_apc:AB-2026-04962:207261a6-f722-4f94-bab3-27b0857ccceb | M&A IT Tech Inc. | Workers' Compensation Board of Alberta - Request for Quotes - RFQ2632 SurveyMonkey Enterprise Subscription Renewal | 172956.0 |  |  | https://purchasing.alberta.ca/posting/AB-2026-04962 |
| ca_alberta_apc:AB-2026-05315:3600fda0-9c11-42c1-b31a-47a9b083ca7c | Demke Enterprises Ltd | Workers' Compensation Board of Alberta - Invitation to Bid - IFB 2634JC Home Modification Grassy Lake | 720319.5 |  |  | https://purchasing.alberta.ca/posting/AB-2026-05315 |
| ca_alberta_apc:AB-2026-05442:85559b7d-8a9e-4c29-92f9-f9d18a9a96f0 | GlassHouse Systems | Workers' Compensation Board of Alberta - Request for Quotes - RFQ2644 Proofpoint Enterprise Licensing and Support Renewal | 918540.0 |  |  | https://purchasing.alberta.ca/posting/AB-2026-05442 |

## The vendor's other buyers in the dataset (first 60 of 10)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| canada_federal:crtc:26-0176 | Canadian Radio-television and Telecommunications Commission | License/Maintenance fees for client software related to Distributed Computing Environment (DCE) | 15272.4 |  |  | https://search.open.canada.ca/contracts/record/crtc,C-2026-2027-Q1-00022 |
| canada_federal:cic:7123623 | Immigration, Refugees and Citizenship Canada | License/Maintenance fees for client software related to Distributed Computing Environment (DCE) | 34750.89 |  |  | https://search.open.canada.ca/contracts/record/cic,C-2025-2026-Q3-00120 |
| canada_federal:nrcan-rncan:S124934 | Natural Resources Canada | Application software (including COTS) and application development and delivery software | 29884.14 |  |  | https://search.open.canada.ca/contracts/record/nrcan-rncan,C-2025-2026-Q4-00552 |
| canada_federal:cb:CW2334452 | Department of Public Works and Government Services (PSPC) | Software Licensing Supply Arrangement (SLSA) |  |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cw2334452 |
| ca_canadabuys_contract_history:E60ZT-180026/148/ZT | Department of Public Works and Government Services (PSPC) | ProServices SA - LIKE 10 INC. |  |  |  | https://open.canada.ca/data/en/dataset/4fe645a1-ffcd-40c1-9385-2c771be956a4 |
| ca_canadabuys_contract_history:EN578-170432/173/EI | Department of Public Works and Government Services (PSPC) | TBIPS SA - LIKE 10 INC. |  |  |  | https://open.canada.ca/data/en/dataset/4fe645a1-ffcd-40c1-9385-2c771be956a4 |
| ca_canadabuys_contract_history:an:PW-16-00727316-736923 | Elections Canada | System Administrator – Level 2 – TBIPS | 194020.31 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/pw-16-00727316-736923 |
| ca_canadabuys_contract_history:an:PW-17-00804596-819081 | Elections Canada | System Administrator Support Services | 296635.5 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/pw-17-00804596-819081 |
| ca_canadabuys_contract_history:an:PW-17-00786123-819898 | Natural Resources Canada | VSTS specialist | 101700.0 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/pw-17-00786123-819898 |
| canada_sosa:CW2334452 | Public Works and Government Services Canada | EN578-232335.051.SMS AMD 006 Like 10 Inc. (Redgate) |  |  |  | https://buyandsell.gc.ca/procurement-data/standing-offers-and-supply-arrangements/CW2334452 |

## Open questions for hand research (layer 2)

- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
