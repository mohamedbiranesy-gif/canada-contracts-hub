# S1-15 — Texas Department of Transportation (TxDOT) ⇄ AtkinsRéalis Group Inc.

Stratum: **S1_gold_complete_published_PO_rule** · pay on sight: yes · channel tier 1 · AP grade A · missing: —

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Texas Department of Transportation --> Copyright — 125 E. 11th Street, Austin, TX 78701
SUBMIT TO: peps_invoiceinquiries@txdot.gov (invoicing/AP mailbox, confirmed by the referee) | portal (not confirmed as an invoice channel): supplier / vendor portal | format: do not send other copies of this invoice via regular mail, fax or other means (as printed on https://ftp.txdot.gov/pub/txdot/commission/2023/0629/10.pdf, re-read 2026-11-08)
REFERENCE: none in the record | PO rule: yes (as published: shall be made under the purchase order)
FROM / REMIT TO: ATKINSRÉALIS GROUP INC. (as registered: Canada's Business Registries, CC 590410, 2026-11-08) — Montréal, Quebec (registered office city / province; Canada's Business Registries, CC 590410, 2026-11-08) | GST/HST 127983500 (Canada's Business Registries, CC 590410, 2026-11-08)RT0001 (account derived from the BN9) | NEQ 1143643345
TAX: Tax Exemption Certificate will be furnished by the Agency complete delivery in 14 calendar days (as printed on https://ftp.txdot.gov/pub/txdot-info/gsd/pdf/form | CURRENCY: CAD | TERMS: 30 days from receipt (as printed on https://ftp.txdot.gov/pub/txdot-info/gsd/pdf/form1994.pdf, re-re
DESCRIPTION: Texas Department of Transportation (TxDOT) (government ministry / agency, jurisdiction not stated) — public contract / purchase award in the | AMOUNT: 6000000.00 (as printed in th
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 89
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 5
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Texas Department of Transportation (TxDOT) (government ministry / agency, jurisdiction not stated) — public contract / purchase award in the last 12 months (dated record): AtkinsRéalis Group Inc. | value: 6000000.00 (as printed in the buyer's own buyer page: https://www.txdot.gov/content/dam/docs/division/ppd/selected-consultants/fy2025/601ct0000006044.pdf, read 2026-11-08: "citation Close Date: 10/11/2024 RFP Number: 601CT0000006044 Legacy # 365RFP5175 Total Value of all Contracts: $6,000,000.00 Wave 2025-1 Process Type: Non Fed No Int HUB El Paso Service Center Number o") CAD | awarded 2026-10-21 | published by: Canada-based vendor (release dateline) | record: https://www.newswire.ca/news-releases/atkinsrealis-to-operate-and-manage-austin-district-traffic-management-center-for-txdot-875038772.html | vendor in Canada because: Canada-based vendor (release dateline)=Share this article MONTREAL , Oct. 21, 2026 /CNW/ | status rule: likely active (contract announced by the Canada-based vendor in the last 12 months: press release / EDC transaction)
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: lead:dcf86d2afc0fd602
- **tier**: B
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: Canada-based vendor (release dateline); 0 in the contract dataset)

## Buyer
- **buyer**: Texas Department of Transportation (TxDOT)
- **buyer_website**: https://www.txdot.gov/
- **buyer_address**: 125 E. 11th Street, Austin, TX 78701
- **buyer_phone**: 281-875-3279
- **buyer_contact_evidence_url**: https://www.txdot.gov/about/contact-us/report-fraud.html
- **buyer_legal_name_as_published**: Texas Department of Transportation --> Copyright
- **buyer_logo_url**: https://www.txdot.gov/content/dam/images/abstract/txdot-homepage-social-thumbnail.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/texas-department-of-transportation
- **buyer_type**: government ministry / agency
- **buyer_sector**: government: provincial / federal
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.txdot.gov/about/contact-us/report-fraud.html (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; invoicing requirements: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_payment_method_preference**: Direct Deposit is the preferred (as printed on https://ftp.txdot.gov/pub/txdot/pro/vendor-letter.pdf, re-read 2026-11-08)
- **buyer_tax_exempt_status**: Tax Exemption Certificate will be furnished by the Agency complete delivery in 14 calendar days (as printed on https://ftp.txdot.gov/pub/txdot-info/gsd/pdf/form2006.pdf, re-read 2026-11-08)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **buyer_esignature_preference**: DocuSign CLM (as printed on https://www.txdot.gov/business/peps/manage-active-contracts/invoicing.html, re-read 2026-11-08)
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: peps_invoiceinquiries@txdot.gov
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.txdot.gov/business/peps/manage-active-contracts/invoicing.html
- **email_evidence_quote**: the current template. Do not submit the invoice more than once, as this will cause a delay in processing. Submit all invoice questions to: PEPS_InvoiceInquiries@txdot.gov Announcing: New email accounts for PEPS invoice submissions will be operational soon. TxDOT's PEPS Division is improvi
- **email_evidence_context**: acts --> Invoicing The invoice template published on the website will be the most current template. Always use the current template. Do not submit the invoice more than once, as this will cause a delay in processing. Submit all invoice questions to: PEPS_InvoiceInquiries@txdot.gov Announcing: New email accounts for PEPS invoice submissions will be operational soon. TxDOT's PEPS Division is improving the efficiency of invoice processing by employing automation strategies using DocuSign CLM. The email addresses are posted below (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: peps_invoiceinquiries@txdot.gov (invoicing/AP) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-04 | page: https://www.txdot.gov/business/peps/manage-active-contracts/invoicing.html | quote: "the current template. Do not submit the invoice more than once, as this will cause a delay in processing. Submit all invoice questions to: PEPS_InvoiceInquiries" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00135
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1; p=quarantine; pct=50; rua=mailto:spam@txdot.gov
- **dmarc_record_domain**: txdot.gov
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 ip4:32.66.21.6/31 ip4:32.66.21.8/29 ip4:32.66.21.16/30 ip4:32.66.21.20/31 ip4:144.45.191.15 ip4:204.64.21.50 ip4:204.64.21.74 ip4:204.64.21.82 ip4:204.64.21.246/31 ip4:204.64.21.250/31 ip4:198.207.147.224/27 ip4:204.239.0.224/27 ip4:216.230.14.224/27 include:spf.protection.outlook.com include
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements**: invoice format as published: do not send other copies of this invoice via regular mail, fax or other means (as printed on https://ftp.txdot.gov/pub/txdot/commission/2023/0629/10.pdf, re-read 2026-11-08)
- **payment_terms_as_published**: 30 days from receipt (as printed on https://ftp.txdot.gov/pub/txdot-info/gsd/pdf/form1994.pdf, re-read 2026-11-08)
- **po_required_as_published**: yes (as published: shall be made under the purchase order) (as printed on https://ftp.txdot.gov/pub/txdot/pro/vendor-letter.pdf, re-read 2026-11-08)
- **invoice_portal_url**: supplier / vendor portal
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "payment_terms": "30 days from receipt (as printed on https://ftp.txdot.gov/pub/txdot-info/gsd/pdf/form1994.pdf, re-read 2026-11-08)", "po_required": "yes (as published: shall be made under the purchase order) (as printed on https://ftp.txdot.gov/pub/txdot/pro/vendor-letter.pdf, re-read 2026-11-08)", "portal_url": "supplier / vendor portal", "portal_kind": "actionable supplier / invoice portal named by the buyer", "invoice_format": "do not send other copies of this invoice via regular mail, fax or other means (as printed on https://ftp.txdot.gov/pub/txdot/commission/2023/0629/10.pdf, re-read 2026-11-08)", "requirements_text": "invoice format as published: do not send other copies of this invoice via regular mail, fax or other means (as printed on https://ftp.txdot.gov/pub/txdot/commission/2023/0629/10.pdf, re-read 2026-11-08)"}
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Texas Department of Transportation --> Copyright — 125 E. 11th Street, Austin, TX 78701 ⏎ SUBMIT TO: peps_invoiceinquiries@txdot.gov (invoicing/AP mailbox, confirmed by the referee) | portal (not confirmed as an invoice channel): supplier / vendor portal | format: do not send other copies of this invoice via regular mail, fax or other means (as printed on https://ftp.txdot.gov/pub/txdot/commission/2023/0629/10.pdf, re-read 2026-11-08) ⏎ REFERENCE: none in the record | PO rule: yes (as published: shall be made under the purchase order) ⏎ FROM / REMIT TO: ATKINSRÉALIS GROUP INC. (as registered: Canada's Business Registries, CC 590410, 2026-11-08) — Montréal, Quebec (registered office city / province; Canada's Business Registries, CC 590410, 2026-11-08) | GST/HST 127983500 (Canada's Business Registries, CC 590410, 2026-11-08)RT0001 (account derived from the BN9) | NEQ 1143643345 ⏎ TAX: Tax Exemption Certificate will be furnished by the Agency complete delivery in 14 calendar days (as printed on https://ftp.txdot.gov/pub/txdot-info/gsd/pdf/form | CURRENCY: CAD | TERMS: 30 days from receipt (as printed on https://ftp.txdot.gov/pub/txdot-info/gsd/pdf/form1994.pdf, re-re ⏎ DESCRIPTION: Texas Department of Transportation (TxDOT) (government ministry / agency, jurisdiction not stated) — public contract / purchase award in the | AMOUNT: 6000000.00 (as p
- **invoice_card_json**: {"bill_to": {"legal_name": "Texas Department of Transportation --> Copyright", "legal_name_is_published": true, "address": "125 E. 11th Street, Austin, TX 78701", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "peps_invoiceinquiries@txdot.gov", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "supplier / vendor portal", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "do not send other copies of this invoice via regular mail, fax or other means (as printed on https://ftp.txdot.gov/pub/txdot/commission/2023/0629/10.pdf, re-read 2026-11-08)", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "portal (not confirmed as an invoice channel)"}, "references_required": {"po_required": "yes (as published: shall be made under the purchase order) (as printed on https://ftp.txdot.gov/pub/txdot/pro/vendor-letter.pdf, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: shall be made under the purchase order) (as printed on https://ftp.txdot.gov/pub/txdot/pro/vendor-letter.pdf, re-read 2026-11-08))"}, "terms": {"payment_terms": "30 days from receipt (as printed on https://ftp.txdot.gov/pub/txdot-info/gsd/pdf/form1994.pdf, re-read 2026-11-08
- **invoice_readiness**: 10/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id)
- **ap_grade**: A
- **ap_score**: 88
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published; payment cycle or method published (plausibility) | missing: finance mailbox; AP phone or AP contact
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: shall be made under the purchase order) (as printed on https://ftp.txdot.gov/pub/txdot/pro/vendor-letter.pdf, re-read 2026-11-08))

## Vendor
- **vendor**: AtkinsRéalis Group Inc.
- **vendor_legal_name**: ATKINSRÉALIS GROUP INC. (as registered: Canada's Business Registries, CC 590410, 2026-11-08)
- **vendor_trading_name**: GROUPE ATKINSRÉALIS INC. (alternate names in the registry)
- **vendor_registry_id**: 590410 (CC)
- **vendor_registry_url**: https://ised-isde.canada.ca/cbr-rec/en/search?q=AtkinsR%C3%A9alis%20Group%20Inc.
- **vendor_registered_address**: Montréal, Quebec (registered office city / province; Canada's Business Registries, CC 590410, 2026-11-08)
- **vendor_neq**: 1143643345 (Registraire des entreprises du Québec (open data), 2026-11-08)
- **vendor_legal_form**: Business Corporation (Canada's Business Registries, CC 590410, 2026-11-08)
- **vendor_country_basis**: Canada-based vendor (release dateline)=Share this article MONTREAL , Oct. 21, 2026 /CNW/
- **vendor_bn9**: 127983500 (Canada's Business Registries, CC 590410, 2026-11-08)
- **vendor_gst_hst_derived**: 127983500RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_facts_provenance**: name and address: the record's vendor block (Canada-based vendor (release dateline)); registry identity: 590410 (CC) status Active (Canada's Business Registries, CC 590410, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: registry: Canada's Business Registries, CC 590410, 2026-11-08; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 1980-03-24; NEQ: 1143643345 (Registraire des entreprises du Québec (open data), 2026-11-08)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Active (Canada's Business Registries, CC 590410, 2026-11-08)
- **vendor_incorporation_date**: 1980-03-24
- **vendor_years_in_business**: 46.6 (since 1980-03-24, registry date)
- **vendor_bn_source**: registry: Canada's Business Registries, CC 590410, 2026-11-08

## Contract
- **po_required_as_published**: yes (as published: shall be made under the purchase order) (as printed on https://ftp.txdot.gov/pub/txdot/pro/vendor-letter.pdf, re-read 2026-11-08)
- **contract_status**: likely active (contract announced by the Canada-based vendor in the last 12 months: press release / EDC transaction)
- **contract_value**: 6000000.00 (as printed in the buyer's own buyer page: https://www.txdot.gov/content/dam/docs/division/ppd/selected-consultants/fy2025/601ct0000006044.pdf, read 2026-11-08: "citation Close Date: 10/11/2024 RFP Number: 601CT0000006044 Legacy # 365RFP5175 Total Value of all Contracts: $6,000,000.00 Wave 2025-1 Process Type: Non Fed No Int HUB El Paso Service Center Number o")
- **currency**: CAD
- **award_date**: 2026-10-21
- **contract_link**: https://www.newswire.ca/news-releases/atkinsrealis-to-operate-and-manage-austin-district-traffic-management-center-for-txdot-875038772.html
- **source**: Canada-based vendor (release dateline)
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: Canada-based vendor (release dateline); 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **vendor_gst_hst_derived**: 127983500RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: yes
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Texas Department of Transportation --> Copyright — 125 E. 11th Street, Austin, TX 78701 ⏎ SUBMIT TO: peps_invoiceinquiries@txdot.gov (invoicing/AP mailbox, confirmed by the referee) | portal (not confirmed as an invoice channel): supplier / vendor portal | format: do not send other copies of this invoice via regular mail, fax or other means (as printed on https://ftp.txdot.gov/pub/txdot/commission/2023/0629/10.pdf, re-read 2026-11-08) ⏎ REFERENCE: none in the record | PO rule: yes (as published: shall be made under the purchase order) ⏎ FROM / REMIT TO: ATKINSRÉALIS GROUP INC. (as registered: Canada's Business Registries, CC 590410, 2026-11-08) — Montréal, Quebec (registered office city / province; Canada's Business Registries, CC 590410, 2026-11-08) | GST/HST 127983500 (Canada's Business Registries, CC 590410, 2026-11-08)RT0001 (account derived from the BN9) | NEQ 1143643345 ⏎ TAX: Tax Exemption Certificate will be furnished by the Agency complete delivery in 14 calendar days (as printed on https://ftp.txdot.gov/pub/txdot-info/gsd/pdf/form | CURRENCY: CAD | TERMS: 30 days from receipt (as printed on https://ftp.txdot.gov/pub/txdot-info/gsd/pdf/form1994.pdf, re-re ⏎ DESCRIPTION: Texas Department of Transportation (TxDOT) (government ministry / agency, jurisdiction not stated) — public contract / purchase award in the | AMOUNT: 6000000.00 (as p
- **invoice_card_json**: {"bill_to": {"legal_name": "Texas Department of Transportation --> Copyright", "legal_name_is_published": true, "address": "125 E. 11th Street, Austin, TX 78701", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "peps_invoiceinquiries@txdot.gov", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "supplier / vendor portal", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "do not send other copies of this invoice via regular mail, fax or other means (as printed on https://ftp.txdot.gov/pub/txdot/commission/2023/0629/10.pdf, re-read 2026-11-08)", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "portal (not confirmed as an invoice channel)"}, "references_required": {"po_required": "yes (as published: shall be made under the purchase order) (as printed on https://ftp.txdot.gov/pub/txdot/pro/vendor-letter.pdf, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: shall be made under the purchase order) (as printed on https://ftp.txdot.gov/pub/txdot/pro/vendor-letter.pdf, re-read 2026-11-08))"}, "terms": {"payment_terms": "30 days from receipt (as printed on https://ftp.txdot.gov/pub/txdot-info/gsd/pdf/form1994.pdf, re-read 2026-11-08
- **invoice_readiness**: 10/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id)
- **ap_grade**: A
- **ap_score**: 88
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published; payment cycle or method published (plausibility) | missing: finance mailbox; AP phone or AP contact
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **facts_provenance_json**: {"mailbox": ["peps_invoiceinquiries@txdot.gov (invoicing/AP)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-04", "page: https://www.txdot.gov/business/peps/manage-active-contracts/invoicing.html", "quote: \"the current template. Do not submit the invoice more than once, as this will cause a delay in processing. Submit all invoice questions to: PEPS_InvoiceInquiries\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00135"], "buyer_facts": ["address and phone: the buyer's own site, https://www.txdot.gov/about/contact-us/report-fraud.html (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "invoicing requirements: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoice portal: the mailbox's evidenc

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.txdot.gov/business/peps/manage-active-contracts/invoicing.html | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, txdot.gov)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: Texas Department of Transportation --> Copyright
- **legal_name_url**: https://www.txdot.gov/
- **legal_name_quote**: ans Portal Statewide services 211Texas.org Texas.gov Texas statewide search (TRAIL) Copyright 2026, Texas Department of Transportation --> Copyright 2026, Texas Department of Transportation Disclaimer Accessibility Policy Website Privacy Policy Com
- **logo_url**: https://www.txdot.gov/content/dam/images/abstract/txdot-homepage-social-thumbnail.png
- **logo_basis**: og:image of the home page (looks like a photo, not a logo: check before use)
- **domain**: txdot.gov
- **key**: lead:dcf86d2afc0fd602
- **name**: Texas Department of Transportation (TxDOT)
- **website**: https://txdot.gov/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Global Positioning System
- **legal_name_stated_url**: https://www.txdot.gov/about.html
- **legal_name_stated_quote**: s Traffic count maps Official travel maps Roadway inventory One-stop demographic data analysis tool Global Positioning System (GPS) Crash reports and records District and county statistics (DISCOS) Right-of-way maps Bicycle a
- **linkedin_url**: https://www.linkedin.com/company/texas-department-of-transportation

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "phone": "281-875-3279", "phone_url": "https://www.txdot.gov/about/contact-us.html", "address": "125 E. 11th Street, Austin, TX 78701", "address_country": "US", "address_url": "https://www.txdot.gov/about/contact-us/report-fraud.html", "address_method": "pattern", "address_quote": "ailing Address: Texas Department of Transportation – Attn. Compliance Division, 125 E. 11th Street, Austin, TX 78701 About Districts Divisions Leadership Newsroom Business Contra", "domain": "txdot.gov", "key": "lead:dcf86d2afc0fd602", "name": "Texas Department of Transportation (TxDOT)", "website": "https://txdot.gov/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, domain unknown)
_not read_

## Vendor role mailboxes found on its site (org_contacts)
_not read_

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Texas Department of Transportation (TxDOT) |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:dcf86d2afc0fd602",
 "ap_contact_team": {
  "emails": [
   "peps_invoiceinquiries@txdot.gov",
   "projectfinance@txdot.gov"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "peps_invoiceinquiries@txdot.gov",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.txdot.gov/business/peps/manage-active-contracts/invoicing.html",
    "quote": "the current template. Do not submit the invoice more than once, as this will cause a delay in processing. Submit all invoice questions to: PEPS_InvoiceInquiries@txdot.gov Announcing: New email accounts for PEPS invoice submissions will be operational soon. TxDOT's PEPS Division is improvi",
    "retrieved_date": "2026-11-04",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Texas Department of Transportation (TxDOT)",
    "task_id": "CL-WS-00135"
   },
   {
    "email": "projectfinance@txdot.gov",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.txdot.gov/about/financial-management/investor-relations.html",
    "quote": "ass=\"contact-card mb-5 no-inline-icon\"> <div class=\"contact-card-title\"> Project Finance and Toll Operations Division</div> <a href=\"mailto:projectfinance@txdot.gov\" class=\"contact-link\"> <div class=\"contact-card-wrapper\"> <div class=\"contact-card-icon-wrapper\"> <svg xmlns=\"http://www.w3.o",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Texas Department of Transportation (TxDOT)",
    "task_id": "CL-DT-00076"
   },
   {
    "email": "fin_invoices@txdot.gov",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://ftp.txdot.gov/pub/txdot/commission/2023/0629/10.pdf",
    "quote": "023 Change Notice Services > $25K and < $100K To: Agency To Invoice: TTEC Government Solutions, LLC 60144_Central Branch 9197 S. Peoria St. FIN_INVOICES@TXDOT.GOV Englewood CO 80112-5833 TXDOT -FIN, VOUCHER PROCESSING United States 125 E 11TH ST AUSTIN TX 78701-2483 United States VENDOR ID",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "unverified_page_unavailable",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Texas Department of Transportation (TxDOT)",
    "task_id": "CL-WS-00472"
   },
   {
    "email": "txdot-invoice@epp.oxygen-finance.com",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://ftp.txdot.gov/pub/txdot/commission/2023/0629/10.pdf",
    "quote": "s will not be issued to a vendor without a current Texas identification number. *NOTE TO VENDORS PARTICIPATING IN THE EPP: Send invoices to txdot-invoice@epp.oxygen-finance.com if vendor is participating in the Early Payment Program (EPP), not the address on page 1 of the purchase order. I",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "unverified_page_unavailable",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Texas Department of Transportation (TxDOT)",
    "task_id": "CL-WS-00472"
   }
  ]
 },
 "research_status": {
  "found": 4
 },
 "queries_tried": [
  "site crawl of www.txdot.gov (60 pages, robots.txt respected), no AI, no search engine",
  "web search for the buyer's invoicing / accounts payable page (the search only gave the address); the page then read by tools/deep_pages.py with the crawler's rules, no AI",
  "web search for the buyer's invoicing / accounts payable page (the search only gave the address); the page then read by tools/deep_pages.py with the crawler's rules, no AI",
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

## The vendor's other buyers in the dataset (first 60 of 300)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_alberta_apc:AB-2023-05730:47eb878b-3212-47d6-95d2-82c26c90a9fd | ENMAX | ENMAX - Request for Proposal - ENMAX 23-3038 RFP for Engineering Design Services |  |  |  | https://purchasing.alberta.ca/posting/AB-2023-05730 |
| ca_alberta_apc:AB-2023-06701:05f4ba71-5dd1-427c-b869-400505dddbb2 | ENMAX | ENMAX - Request for Proposal - ENMAX 23-3061 RFP for Owner’s Engineering and Engineering Study Services |  |  |  | https://purchasing.alberta.ca/posting/AB-2023-06701 |
| ca_alberta_apc:AB-2024-03904:0a3893d7-e72f-4e35-8848-7333909b4b93 | Primary and Preventative Health Services | Primary and Preventative Health Services - Request for Proposal - Review of Human Health Risk Assessments and Environmental Impact Assessments | 133550.0 |  |  | https://purchasing.alberta.ca/posting/AB-2024-03904 |
| ca_bidsandtenders:9283adcf-b473-47ad-9b3d-ef8a52552a10:1 | Newfoundland Labrador Hydro | RFP - HVAC System Feasibility Study for LIL | 21100.0 |  |  | https://nlhydro.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/9283adcf-b473-47ad-9b3d-ef8a52552a10 |
| ca_bidsandtenders:c26d2260-54d8-4ce2-a43e-55555eed75ca:1 | Newfoundland Labrador Hydro | RFQ - 2026 Fall Dam Inspections for Hydro Generation and Exploits Dams | 32001.0 |  |  | https://nlhydro.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/c26d2260-54d8-4ce2-a43e-55555eed75ca |
| ca_bidsandtenders:aae32c0a-2368-485e-830a-4eccb0d5337d:2 | Town of Halton Hills | Prequalification of Detailed Design Services Consultant for Eighth Line Widening from 10 Side Road to 15 Side Road |  |  |  | https://haltonhills.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/aae32c0a-2368-485e-830a-4eccb0d5337d |
| ca_bidsandtenders:2710d564-2b21-4dad-9fb1-eea2e23efd39:1 | Government of Yukon | Whitehorse area flood mapping study | 521699.5 |  |  | https://yukon.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/2710d564-2b21-4dad-9fb1-eea2e23efd39 |
| ca_bidsandtenders:5075594f-fd58-4c76-9574-38bb7043ad1b:15 | York Region | Research and Innovation Roster |  |  |  | https://york.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/5075594f-fd58-4c76-9574-38bb7043ad1b |
| ca_bidsandtenders:5075594f-fd58-4c76-9574-38bb7043ad1b:16 | York Region | Research and Innovation Roster |  |  |  | https://york.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/5075594f-fd58-4c76-9574-38bb7043ad1b |
| ca_bidsandtenders:5075594f-fd58-4c76-9574-38bb7043ad1b:17 | York Region | Research and Innovation Roster |  |  |  | https://york.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/5075594f-fd58-4c76-9574-38bb7043ad1b |
| ca_bidsandtenders:d72699a1-dcb6-4a99-8dad-fd3070fa7b5e:8 | Town of Aurora | GEOTECHNICAL ENGINEERING SERVICES FOR SOIL AND MATERIAL TESTING |  |  |  | https://aurora.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/d72699a1-dcb6-4a99-8dad-fd3070fa7b5e |
| ca_bidsandtenders:5c21e721-7c02-4af5-8351-413fdd8c38c0:4 | Government of Yukon | Aviation Technical Advisory and Engineering Services |  |  |  | https://yukon.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/5c21e721-7c02-4af5-8351-413fdd8c38c0 |
| ca_bidsandtenders:bfecb8d1-1b6e-4c59-be70-7ae847027563:2 | Town of Innisfil | Prequalification for On-Site Material Testing Services |  |  |  | https://innisfil.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/bfecb8d1-1b6e-4c59-be70-7ae847027563 |
| ca_bidsandtenders:0d064e83-17c9-44f5-adbb-55e354d78294:2 | Region of Durham | Services and quality assurance material testing on various Bus Rapid Transit projects in the Region of Durham | 177345.0 |  |  | https://durham.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/0d064e83-17c9-44f5-adbb-55e354d78294 |
| ca_bidsandtenders:2e0a02a0-7be2-4b7d-ba08-a41c499996fc:1 | Newfoundland Labrador Hydro | RFP - Bay d’Espoir Generating Station Major Projects - EPCM | 7558764.0 |  |  | https://nlhydro.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/2e0a02a0-7be2-4b7d-ba08-a41c499996fc |
| ca_bidsandtenders:7f726106-3b12-4eff-ab57-943c958ab504:1 | York Region | Design Services for Construction of the Hwy 7 East Bus Rapid Transit Median Rapidway and Stations |  |  |  | https://york.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/7f726106-3b12-4eff-ab57-943c958ab504 |
| ca_bidsandtenders:fd6798b7-8135-49a1-b622-c9026eee62c2:1 | Newfoundland Labrador Hydro | RFP - Cable Shaft Fans and Controls Replacement - Churchill Falls, NL | 361999.9 |  |  | https://nlhydro.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/fd6798b7-8135-49a1-b622-c9026eee62c2 |
| ca_bidsandtenders:a54b474c-d27f-45fb-ba19-c82994f20b74:21 | Region of Peel | ESTABLISHMENT OF A PEEL WATER AND WASTEWATER ENGINEERING SERVICES ROSTER |  |  |  | https://peelregion.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/a54b474c-d27f-45fb-ba19-c82994f20b74 |
| ca_bidsandtenders:a50c1d9a-62f0-4fbf-9c2d-feff07ef1451:1 | Newfoundland Labrador Hydro | RFP - Bay d'Espoir Flood Evacuation Alarm System Study 2025 | 142476.0 |  |  | https://nlhydro.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/a50c1d9a-62f0-4fbf-9c2d-feff07ef1451 |
| ca_bidsandtenders:86000c03-7124-4c50-b505-80c88c7a9cfb:3 | City of Mississauga | Environmental Consulting Roster |  |  |  | https://mississauga.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/86000c03-7124-4c50-b505-80c88c7a9cfb |
| ca_bidsandtenders:035bf623-daea-4e89-9ff1-424bfe723dbd:7 | Vancouver Island Health Authority | Mechanical Consulting Services_Initial Intake |  |  |  | https://islandhealthfdc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/035bf623-daea-4e89-9ff1-424bfe723dbd |
| ca_bidsandtenders:0939f9a2-6c42-43d8-b7a0-2d476564750d:1 | Newfoundland Labrador Hydro | RFP - Ebbegunbaeg Dam Remediation Options Study 2025 | 126941.0 |  |  | https://nlhydro.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/0939f9a2-6c42-43d8-b7a0-2d476564750d |
| ca_bidsandtenders:54ea85cb-cf48-4758-afcf-20915c646b56:13 | Government of Yukon | Mine Site Engineering Services 2025-2030 |  |  |  | https://yukon.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/54ea85cb-cf48-4758-afcf-20915c646b56 |
| ca_bidsandtenders:b524db52-8ded-42a6-8254-c037bc5532da:2 | York Region | Consultants for Detailed Design and Engineering Services for Various Structures |  |  |  | https://york.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/b524db52-8ded-42a6-8254-c037bc5532da |
| ca_bidsandtenders:d0587d6d-a8af-43e9-ae2f-df6ae1b38994:6 | City of Hamilton | Category 4 - Structures/Transportation |  |  |  | https://hamilton.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/d0587d6d-a8af-43e9-ae2f-df6ae1b38994 |
| ca_bidsandtenders:90afb8f1-ad89-4425-bb63-d8a1ae2f58a6:1 | City of Hamilton | Category 8 - Solid Waste Management |  |  |  | https://hamilton.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/90afb8f1-ad89-4425-bb63-d8a1ae2f58a6 |
| ca_bidsandtenders:a56d3411-6603-4841-96d7-e8427e706f7e:1 | York Region | Detailed Design, Construction Administration & Inspection Services Highway 27 (Y.R. 27) from Major Mackenzie Drive (Y.R. 25) to 770 m north of Nashville Road, C | 7027000.0 |  |  | https://york.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/a56d3411-6603-4841-96d7-e8427e706f7e |
| ca_bidsandtenders:d3e160c5-d00f-49aa-a011-ed5dd773d0b8:4 | York Region | Request for Pre-Qualification for Qualified Person Services under Ontario Regulation 406/19 |  |  |  | https://york.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/d3e160c5-d00f-49aa-a011-ed5dd773d0b8 |
| ca_bidsandtenders:63bfd385-9603-40f7-847d-fee070974cc0:1 | Region of Peel | ENGINEERING SERVICES TO SUPPORT TRAFFIC SIGNAL AND STREET LIGHT SUPPORT IN THE REGION OF PEEL | 480118.6 |  |  | https://peelregion.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/63bfd385-9603-40f7-847d-fee070974cc0 |
| ca_bidsandtenders:8e058c05-848d-40c0-b2a4-5c335fca9166:5 | Town of Innisfil | Geotechnical Peer Review Services |  |  |  | https://innisfil.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/8e058c05-848d-40c0-b2a4-5c335fca9166 |
| ca_bidsandtenders:63577390-f191-4e3e-8353-18766356999e:1 | Region of Peel | CONTRACT ADMINISTRATION SERVICES FOR MAYFIELD ROAD WIDENING, PROJECT 13-4055 | 1425556.6 |  |  | https://peelregion.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/63577390-f191-4e3e-8353-18766356999e |
| ca_bidsandtenders:d0f590bb-5f01-48ad-adae-541a008fd6fa:3 | Metro Vancouver | Geotechnical and Environmental Engineering Services |  |  |  | https://metrovancouver.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/d0f590bb-5f01-48ad-adae-541a008fd6fa |
| ca_bidsandtenders:1b729502-8266-48a8-bcda-5663439383e9:2 | Metro Vancouver | Consulting Engineering Service for Design and Construction of the South Fraser Works Yard Development |  |  |  | https://metrovancouver.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/1b729502-8266-48a8-bcda-5663439383e9 |
| ca_bidsandtenders:3f215072-8bec-4a99-9145-d05b359f5c5f:5 | Metro Vancouver | Process Safety Management Consulting Services |  |  |  | https://metrovancouver.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/3f215072-8bec-4a99-9145-d05b359f5c5f |
| ca_bidsandtenders:4400a39c-94f7-4670-b78a-d44477a1108a:2 | York Region | Detailed Design, Construction Administration & Inspection Services Highway 27 (Y.R. 27) from Major Mackenzie Drive (Y.R. 25) to 770 m north of Nashville Road, C |  |  |  | https://york.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/4400a39c-94f7-4670-b78a-d44477a1108a |
| ca_bidsandtenders:56022c23-d6ac-4105-aff6-dcbee08a44ec:1 | York Region | Consulting and Engineering Services, Detailed Design CA & SI for Leslie St. Improvement, from Green Lane to Colonel Wayling Boulevard, in Town of East Gwillimbu |  |  |  | https://york.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/56022c23-d6ac-4105-aff6-dcbee08a44ec |
| ca_bidsandtenders:6c20e08a-f497-43a2-a365-691ec952a707:1 | Newfoundland Labrador Hydro | RFP - Audit Dam Safety Review for West Forebay - Chuchill Falls |  |  |  | https://nlhydro.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/6c20e08a-f497-43a2-a365-691ec952a707 |
| ca_bidsandtenders:724b9a14-4e99-4854-b228-163add55efde:5 | Newfoundland Labrador Hydro | RFP - SOA Owner’s Team Support Services |  |  |  | https://nlhydro.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/724b9a14-4e99-4854-b228-163add55efde |
| ca_bidsandtenders:b9a832ec-4693-4bbd-a51d-82828633fd98:3 | City of New Westminster | NWRFQU-24-01 Electrical Utility - Design And Project Delivery Services |  |  |  | https://newwestcity.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/b9a832ec-4693-4bbd-a51d-82828633fd98 |
| ca_bidsandtenders:64229c23-6e60-417c-b9fa-bca174c2f770:1 | Government of Yukon | Bridge Engineering Services on Various Bridges |  |  |  | https://yukon.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/64229c23-6e60-417c-b9fa-bca174c2f770 |
| ca_bidsandtenders:86eeb380-2b9f-485a-b2d4-35db1e7ff534:5 | Government of Yukon | Materials Testing, Quality Assurance and Geotechnical Investigation Services, 2024 - 2027 |  |  |  | https://yukon.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/86eeb380-2b9f-485a-b2d4-35db1e7ff534 |
| ca_bidsandtenders:91cbafed-a58c-47bd-a7d5-48280289b383:5 | Government of Yukon | Environmental Services and Regulatory Submissions Support 2024-2027 | 20475.0 |  |  | https://yukon.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/91cbafed-a58c-47bd-a7d5-48280289b383 |
| ca_bidsandtenders:63578aad-5675-4029-9863-40856449134c:1 | Interior Health | RFP FWG Long-Term Care Replacement & Expansion - Geotechnical Services |  |  |  | https://interiorhealth.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/63578aad-5675-4029-9863-40856449134c |
| ca_bidsandtenders:904ccc98-2e73-43a9-90f8-0e97dfc51ed8:1 | Newfoundland Labrador Hydro | RFP Bay d’Espoir Unit 8 - Front End Engineering & Design |  |  |  | https://nlhydro.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/904ccc98-2e73-43a9-90f8-0e97dfc51ed8 |
| ca_bidsandtenders:87df5dba-ff1e-4416-afc4-c4620804e5cc:1 | Region of Peel | DETAILED DESIGN AND CONTRACT ADMINISTRATION FOR PART A ROADWAYS WITHIN HIGHWAY 427 SECONDARY PLAN AREA 47, CITY OF BRAMPTON, PROJECTS 20-4040 AND 21-4040 | 11167950.01 |  |  | https://peelregion.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/87df5dba-ff1e-4416-afc4-c4620804e5cc |
| ca_bidsandtenders:da838ad9-2dc1-49b8-9bc3-fca1e39d9575:6 | City of Vaughan | Vendors of Record for Geotechnical Services |  |  |  | https://vaughan.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/da838ad9-2dc1-49b8-9bc3-fca1e39d9575 |
| ca_bidsandtenders:e053e4b7-f1d7-4e0c-b286-91563dd1b478:4 | Region of Peel | GEOTECHNICAL, ENVIRONMENTAL, AND RELATED SERVICES FOR THE REGION OF PEEL | 2701485.0 |  |  | https://peelregion.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/e053e4b7-f1d7-4e0c-b286-91563dd1b478 |
| ca_bidsandtenders:c4e2b75f-c299-4767-b2b4-86ee842beda3:1 | Town of Innisfil | Geotechnical Peer Review |  |  |  | https://innisfil.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/c4e2b75f-c299-4767-b2b4-86ee842beda3 |
| ca_bidsandtenders:c53486fe-8592-4d1b-9c19-76a8b6fb1aaa:3 | York Region | Consultants for Detailed Design and Engineering Services For Active Transportation Infrastructure |  |  |  | https://york.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/c53486fe-8592-4d1b-9c19-76a8b6fb1aaa |
| ca_bidsandtenders:933a6a3f-05c2-46b6-828c-96053970d6d1:1 | York Region | Detailed Design and Engineering Services for 16th Avenue, from Woodbine Avenue to Kennedy Road |  |  |  | https://york.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/933a6a3f-05c2-46b6-828c-96053970d6d1 |
| ca_bidsandtenders:ca93bb80-9d38-428d-a1fb-455bd3cb333e:4 | Peterborough County | Request for Supplier Qualifications for the Creation of a Vendor of Record List for Geotechnical Engineering Services |  |  |  | https://ptbocounty.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/ca93bb80-9d38-428d-a1fb-455bd3cb333e |
| ca_bidsandtenders:aeb7d7b3-df56-4d0f-b556-3dacb3949a43:7 | Haldimand County | Geotechnical Services |  |  |  | https://haldimandcounty.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/aeb7d7b3-df56-4d0f-b556-3dacb3949a43 |
| ca_merx:4030755136:1 | The City of Winnipeg | Consulting Services for Cornish Lift Station Upgrades & St Charles Lift Station | 453085.0 |  |  | https://www.merx.com/mbgov/cityofwinnipeg/solicitations/Consulting-Services-for-Cornish-Lift-Station-Upgrades-St-Charles-Lift-Station/0000327902?origin=0 |
| ca_merx:3962864503:1 | Toronto Transit Commission - PCM Capital | P11PU26271-G85-443-STRUCTURAL ENGINEERING SERVICES - TRIENNIAL CONTRACT | 1000000.0 |  |  | https://www.merx.com/ttc/torontotransitcommission/solicitations/P11PU26271-G85-443-STRUCTURAL-ENGINEERING-SERVICES-TRIENNIAL-CONTRACT/0000322262?origin=0 |
| ca_merx:3867222155:1 | Saskatchewan Power Corporation (SaskPower) | Multi-Disciplined Engineering Services |  |  |  | https://www.merx.com/saskpower/solicitations/Multi-Disciplined-Engineering-Services/0000316345?origin=0 |
| ca_merx:3743862151:1 | Toronto Transit Commission - PCM Capital | R76RT25777-REQUEST FOR SUPPLIER QUALIFICATION –VEHICLE PROGRAMS PROFESSIONAL SER |  |  |  | https://www.merx.com/ttc/torontotransitcommission/solicitations/R76RT25777-REQUEST-FOR-SUPPLIER-QUALIFICATION-VEHICLE-PROGRAMS-PROFESSIONAL-SER/0000308403?origin=0 |
| ca_merx:3762109330:2 | Saskatchewan Power Corporation (SaskPower) | Environmental Consulting Services for SMR Development Project |  |  |  | https://www.merx.com/saskpower/solicitations/Environmental-Consulting-Services-for-SMR-Development-Project/0000309604?origin=0 |
| ca_merx:2955766152:1 | Toronto Transit Commission - PCM Capital | P58SR24135-LINE TWO SIGNALLING SYSTEM – CONDITION ASSESSMENT SERVICES |  |  |  | https://www.merx.com/ttc/torontotransitcommission/solicitations/P58SR24135-LINE-TWO-SIGNALLING-SYSTEM-CONDITION-ASSESSMENT-SERVICES/0000272066?origin=0 |
| ca_merx:2814503906:1 | Government of Newfoundland and Labrador (GNL) - Transportation & Infrastructure | RFP - Standing Offer for Professional Civil Engineering Services for NL | 456800.0 |  |  | https://www.merx.com/govnl/govnl/solicitations/RFP-Standing-Offer-for-Professional-Civil-Engineering-Services-for-NL/0000265122?origin=0 |
| ca_merx:2865796710:1 | Government of Newfoundland and Labrador (GNL) - Transportation & Infrastructure | Standing Offer for Professional Mechanical Engineering Services for GNL | 462432.0 |  |  | https://www.merx.com/govnl/govnl/solicitations/Standing-Offer-for-Professional-Mechanical-Engineering-Services-for-GNL/0000267763?origin=0 |
| … 240 more rows in the .json | ||||||

## Open questions for hand research (layer 2)

- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

Read 2026-11-09 (Claude, integrator lane). Budget rule (PLAN §4d): layer 1 already carries this buyer's confirmed channel, PO rule and terms with quotes; the notes below add only what changes how the invoice is built.

**Row is complete as published** (TxDOT: PO/contract number "shall be" on the invoice, 30 days from receipt, format rule "do not send…", supplier portal).
State of Texas: payment via the Comptroller (CAPPS / TINS vendor setup — the vendor needs a Texas Payee ID / TIN registration before the first payment);
Prompt Payment Act interest after 30 days (Tex. Gov't Code ch. 2251). No Texas sales tax on state purchases; AtkinsRéalis invoices from a US entity if the
contract was signed by its US subsidiary — the row's vendor is the Canadian parent per the source's own field; check which legal entity signed.
