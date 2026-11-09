# S1-07 — University of the Fraser Valley ⇄ Clark Builders Inc.

Stratum: **S1_gold_complete_published_PO_rule** · pay on sight: yes · channel tier 1 · AP grade A · missing: —

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: University of the Fraser Valley (stated on https://www.ufv.ca/about/) — University of the Fraser Valley Accounts Payable A291- 33844 King Road Abbotsford, BC V2S 7M8 — buyer tax no. 107403701RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (ufv.ca) + name)
SUBMIT TO: acctspayable@ufv.ca (invoicing/AP mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: yes (as published: purchase order, all invoices must)
FROM / REMIT TO: Clark Builders Inc. (as registered: Canada's Business Registries, CC 8786364, 2026-11-08) — 206, 349 Old Airport Road, Yellowknife, NT, X1A2N5, Canada | GST/HST 826552572 (Canada's Business Registries, CC 8786364, 2026-11-08)RT0001 (account derived from the BN9)
TAX: Status Indian Tax Exemption Guidelines Status Indian Tax Exemption Guidelines Status Indian Tax Exemption Claim F (as printed on https://www.ufv.ca/finance/form | CURRENCY: CAD (derived from the source's government) | TERMS: payment is not received within 90 days (as printed on https://www.ufv.ca/finance/accounting-operatio
DESCRIPTION: University of the Fraser Valley (organisation (type not stated in the record)
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 96
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 6
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: University of the Fraser Valley (organisation (type not stated in the record), jurisdiction not stated) — public contract / purchase award in the last 12 months (dated record): Clark Builders Inc. | value: 49817412.0 (source field: amount) CAD (derived from the source's government) | awarded 2026-03-31, start 2025-03-21 (as printed in the buyer's own buyer page: https://blogs.ufv.ca/campus-planning/category/project-updates/, read 2026-11-08: "17, 2025 March 12, 2025 by ashleyhunter WHO: Clark Builders Construction, Tyler Gagan, Project Manager WHEN: Starting March 21, 2025, to March 31, 2025 WHERE: Gillis Ave., in front of Lá:lem te Baker "), end 2025-03-31 (as printed in the buyer's own buyer page: https://blogs.ufv.ca/campus-planning/category/project-updates/, read 2026-11-08: "17, 2025 March 12, 2025 by ashleyhunter WHO: Clark Builders Construction, Tyler Gagan, Project Manager WHEN: Starting March 21, 2025, to March 31, 2025 WHERE: Gillis Ave., in front of Lá:lem te Baker ") | published by: supplier's own site address (University of the Fraser Valley SOFI FY2025-26 schedule of pa | record: https://www.ufv.ca/media/assets/finance/Statement-of-Financial-Information-Year-Ended-March-2026.pdf | vendor in Canada because: supplier's own site address (University of the Fraser Valley SOFI FY2025-26 schedule of payments)=306, 275 Lawrence Avenue Kelowna, BC V1Y 6L2 | status rule: likely active (record dated in the last 12 months: supplier's own site address (University of the Fras
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: lead:3100eb358ecd387a
- **tier**: B
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: supplier's own site address (University of the Fraser Valley SOFI FY2025-26 schedule of pa; 0 in the contract dataset)

## Buyer
- **buyer**: University of the Fraser Valley
- **buyer_website**: https://www.ufv.ca/
- **buyer_address**: 33844 King Road, Abbotsford, BC, V2S 7M8
- **buyer_phone**: 604-504-7441
- **buyer_contact_evidence_url**: https://www.ufv.ca/contact_us/
- **buyer_legal_name_as_published**: University of the Fraser Valley (stated on https://www.ufv.ca/about/)
- **buyer_bn_as_published**: 107403701RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (ufv.ca) + name)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 107403701RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_logo_url**: https://www.ufv.ca/media/web/logos/UFV-Logo-Horiz_Colour-White_RGB.svg
- **buyer_website_status**: site answers
- **buyer_type**: university / college (from the organisation's name / web domain)
- **buyer_sector**: education: post-secondary
- **buyer_charity_status**: registered (listed) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (ufv.ca) + name)
- **buyer_charity_designation**: C; 0010
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q2495961; university in British Columbia; charitable organization
- **buyer_founded**: 1974-00-00 (Wikidata Q2495961, official website on the organisation's domain (https://www.ufv.ca/) + name; 2026-11-08)
- **buyer_budget_or_revenue**: revenue 743342 Q1104069; 1009886 Q1104069; 1286991 Q1104069; 1378419 Q1104069; 1271826 Q1104069; 1792127 Q1104069; 1795694 Q1104 (Wikidata Q2495961, official website on the organisation's domain (https://www.ufv.ca/) + name; 2026-11-08)
- **buyer_employees**: 1; 4; 7; 5; 1034; 1814; 1841; 1849; 1780; 1833; 1933; 2065; 1895; 1958; 2038; 2343 (Wikidata Q2495961, official website on the organisation's domain (https://www.ufv.ca/) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.ufv.ca/contact_us/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers; invoice mailing address: the lane's AP page (https://www.ufv.ca/finance/accounting-operations/accounts-payable/vendor-payment/); invoicing requirements: the lane's AP page (https://www.ufv.ca/finance/accounting-operations/accounts-payable/vendor-payment/); payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_payment_method_preference**: Direct Deposit (EFT) Canadian vendors are strongly encourag (as printed on https://www.ufv.ca/finance/accounting-operations/accounts-payable/vendor-payment/, re-read 2026-11-08)
- **buyer_tax_exempt_status**: Status Indian Tax Exemption Guidelines Status Indian Tax Exemption Guidelines Status Indian Tax Exemption Claim F (as printed on https://www.ufv.ca/finance/forms/, re-read 2026-11-08)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: acctspayable@ufv.ca
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.ufv.ca/finance/accounting-operations/accounts-payable/vendor-payment/
- **email_evidence_quote**: counts Payable has a dedicated email address for receiving PDF invoices for payment processing. Please forward all invoices for payment to: acctspayable@ufv.ca . Vendor Direct Deposit (EFT) Canadian vendors are strongly encouraged to use direct deposit, as it will allow payments to be dire
- **email_evidence_context**: il to: University of the Fraser Valley Accounts Payable A291- 33844 King Road Abbotsford, BC V2S 7M8 Email: Accounts Payable has a dedicated email address for receiving PDF invoices for payment processing. Please forward all invoices for payment to: acctspayable@ufv.ca . Vendor Direct Deposit (EFT) Canadian vendors are strongly encouraged to use direct deposit, as it will allow payments to be directly deposited into a specified Canadian bank account. This will help to eliminate delays associated with cheques and w (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: acctspayable@ufv.ca (invoicing/AP) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-03 | page: https://www.ufv.ca/finance/accounting-operations/accounts-payable/vendor-payment/ | quote: "counts Payable has a dedicated email address for receiving PDF invoices for payment processing. Please forward all invoices for payment to: acctspayable@ufv.ca " | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00005
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Microsoft 365
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1; p=quarantine; pct=100; rua=mailto:DMARC.Admin@ufv.ca,mailto:dmarc_agg@vali.email
- **dmarc_record_domain**: ufv.ca
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 ip4:205.201.128.0/20 ip4:198.2.128.0/18 ip4:148.105.0.0/16 ip4:216.24.224.0/20 ip4:209.87.231.8 ip4:198.37.148.61 ip4:149.72.116.150 ip4:198.162.98.202 ip4:207.194.163.107 include:spf.protection.outlook.com include:spf-flat.symplicity.com include:amazonses.com include:outboundmail.blackbaud.n
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoice_mailing_address**: University of the Fraser Valley Accounts Payable A291- 33844 King Road Abbotsford, BC V2S 7M8
- **invoicing_requirements**: Invoices submitted by email (PDF) or by mail to Accounts Payable
- **payment_terms_as_published**: payment is not received within 90 days (as printed on https://www.ufv.ca/finance/accounting-operations/accounts-receivable/invoice-request/, re-read 2026-11-08)
- **po_required_as_published**: yes (as published: purchase order, all invoices must) (as printed on https://www.ufv.ca/finance/accounting-operations/accounts-payable/vendor-payment/, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "payment_terms": "payment is not received within 90 days (as printed on https://www.ufv.ca/finance/accounting-operations/accounts-receivable/invoice-request/, re-read 2026-11-08)", "po_required": "yes (as published: purchase order, all invoices must) (as printed on https://www.ufv.ca/finance/accounting-operations/accounts-payable/vendor-payment/, re-read 2026-11-08)", "mailing_address": "University of the Fraser Valley Accounts Payable A291- 33844 King Road Abbotsford, BC V2S 7M8", "requirements_text": "Invoices submitted by email (PDF) or by mail to Accounts Payable"}
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: University of the Fraser Valley (stated on https://www.ufv.ca/about/) — University of the Fraser Valley Accounts Payable A291- 33844 King Road Abbotsford, BC V2S 7M8 — buyer tax no. 107403701RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (ufv.ca) + name) ⏎ SUBMIT TO: acctspayable@ufv.ca (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: yes (as published: purchase order, all invoices must) ⏎ FROM / REMIT TO: Clark Builders Inc. (as registered: Canada's Business Registries, CC 8786364, 2026-11-08) — 206, 349 Old Airport Road, Yellowknife, NT, X1A2N5, Canada | GST/HST 826552572 (Canada's Business Registries, CC 8786364, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: Status Indian Tax Exemption Guidelines Status Indian Tax Exemption Guidelines Status Indian Tax Exemption Claim F (as printed on https://www.ufv.ca/finance/form | CURRENCY: CAD (derived from the source's government) | TERMS: payment is not received within 90 days (as printed on https://www.ufv.ca/finance/accounting-operatio ⏎ DESCRIPTION: University of the Fraser Valley (organisation (type not stated in
- **invoice_card_json**: {"bill_to": {"legal_name": "University of the Fraser Valley (stated on https://www.ufv.ca/about/)", "legal_name_is_published": true, "address": "University of the Fraser Valley Accounts Payable A291- 33844 King Road Abbotsford, BC V2S 7M8", "address_is_the_invoice_address": true, "tax_number": "107403701RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (ufv.ca) + name)", "language": "en"}, "submit_to": {"email": "acctspayable@ufv.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "University of the Fraser Valley Accounts Payable A291- 33844 King Road Abbotsford, BC V2S 7M8", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "yes (as published: purchase order, all invoices must) (as printed on https://www.ufv.ca/finance/accounting-operations/accounts-payable/vendor-payment/, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: purchase order, all invoices must) (as printed on https://www.ufv.ca/finance/accou
- **invoice_readiness**: 10/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id)
- **ap_grade**: A
- **ap_score**: 88
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published; payment cycle or method published (plausibility) | missing: finance mailbox; AP phone or AP contact
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms published
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: purchase order, all invoices must) (as printed on https://www.ufv.ca/finance/accounting-operations/accounts-payable/vendor-payment/, re-read 2026-11-08))

## Vendor
- **vendor**: Clark Builders Inc.
- **vendor_legal_name**: Clark Builders Inc. (as registered: Canada's Business Registries, CC 8786364, 2026-11-08)
- **vendor_registry_id**: 8786364 (CC)
- **vendor_registry_url**: https://ised-isde.canada.ca/cbr-rec/en/search?q=Clark%20Builders%20Inc.
- **vendor_registered_address**: Calgary, Alberta (registered office city / province; Canada's Business Registries, CC 8786364, 2026-11-08)
- **vendor_legal_form**: Business Corporation (Canada's Business Registries, CC 8786364, 2026-11-08)
- **vendor_address**: 206, 349 Old Airport Road, Yellowknife, NT, X1A2N5, Canada
- **vendor_country_basis**: supplier's own site address (University of the Fraser Valley SOFI FY2025-26 schedule of payments)=306, 275 Lawrence Avenue Kelowna, BC V1Y 6L2
- **vendor_bn9**: 826552572 (Canada's Business Registries, CC 8786364, 2026-11-08)
- **vendor_gst_hst_derived**: 826552572RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://www.clarkbuilders.com/
- **vendor_emails**: compliance@clarkbuilders.com; reception-rd@clarkbuilders.com
- **vendor_phone**: 780.395.3300
- **vendor_contact_evidence_url**: https://www.clarkbuilders.com/contact-us
- **vendor_logo_url**: https://www.clarkbuilders.com/hubfs/CB%20Logo.svg
- **vendor_website_status**: site answers
- **vendor_linkedin_url**: https://www.linkedin.com/company/clark-builders_2/
- **vendor_facts_provenance**: name and address: the record's vendor block (supplier's own site address (University of the Fraser Valley SOFI FY2025-26 schedule of pa); registry identity: 8786364 (CC) status Active (Canada's Business Registries, CC 8786364, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: registry: Canada's Business Registries, CC 8786364, 2026-11-08; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2014-02-11; phone / role e-mails / logo: the vendor's own site, https://www.clarkbuilders.com/contact-us (tools/org_contacts.py, org_extras.py); website: https://www.clarkbuilders.com/ (site answers)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Active (Canada's Business Registries, CC 8786364, 2026-11-08)
- **vendor_incorporation_date**: 2014-02-11
- **vendor_years_in_business**: 12.7 (since 2014-02-11, registry date)
- **vendor_bn_source**: registry: Canada's Business Registries, CC 8786364, 2026-11-08

## Contract
- **po_required_as_published**: yes (as published: purchase order, all invoices must) (as printed on https://www.ufv.ca/finance/accounting-operations/accounts-payable/vendor-payment/, re-read 2026-11-08)
- **contract_status**: likely active (record dated in the last 12 months: supplier's own site address (University of the Fraser Valley SOFI FY2025-26 schedule of pa)
- **contract_value**: 49817412.0 (source field: amount)
- **currency**: CAD (derived from the source's government)
- **award_date**: 2026-03-31
- **start_date**: 2025-03-21 (as printed in the buyer's own buyer page: https://blogs.ufv.ca/campus-planning/category/project-updates/, read 2026-11-08: "17, 2025 March 12, 2025 by ashleyhunter WHO: Clark Builders Construction, Tyler Gagan, Project Manager WHEN: Starting March 21, 2025, to March 31, 2025 WHERE: Gillis Ave., in front of Lá:lem te Baker ")
- **end_date**: 2025-03-31 (as printed in the buyer's own buyer page: https://blogs.ufv.ca/campus-planning/category/project-updates/, read 2026-11-08: "17, 2025 March 12, 2025 by ashleyhunter WHO: Clark Builders Construction, Tyler Gagan, Project Manager WHEN: Starting March 21, 2025, to March 31, 2025 WHERE: Gillis Ave., in front of Lá:lem te Baker ")
- **contract_link**: https://www.ufv.ca/media/assets/finance/Statement-of-Financial-Information-Year-Ended-March-2026.pdf
- **source**: supplier's own site address (University of the Fraser Valley SOFI FY2025-26 schedule of pa
- **contracts_with_canadian_suppliers**: 3
- **records_with_this_vendor**: 1 (relationship record: supplier's own site address (University of the Fraser Valley SOFI FY2025-26 schedule of pa; 0 in the contract dataset)
- **records_in_contract_dataset**: 3 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 107403701RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (BC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **vendor_gst_hst_derived**: 826552572RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: yes
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: University of the Fraser Valley (stated on https://www.ufv.ca/about/) — University of the Fraser Valley Accounts Payable A291- 33844 King Road Abbotsford, BC V2S 7M8 — buyer tax no. 107403701RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (ufv.ca) + name) ⏎ SUBMIT TO: acctspayable@ufv.ca (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: yes (as published: purchase order, all invoices must) ⏎ FROM / REMIT TO: Clark Builders Inc. (as registered: Canada's Business Registries, CC 8786364, 2026-11-08) — 206, 349 Old Airport Road, Yellowknife, NT, X1A2N5, Canada | GST/HST 826552572 (Canada's Business Registries, CC 8786364, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: Status Indian Tax Exemption Guidelines Status Indian Tax Exemption Guidelines Status Indian Tax Exemption Claim F (as printed on https://www.ufv.ca/finance/form | CURRENCY: CAD (derived from the source's government) | TERMS: payment is not received within 90 days (as printed on https://www.ufv.ca/finance/accounting-operatio ⏎ DESCRIPTION: University of the Fraser Valley (organisation (type not stated in
- **invoice_card_json**: {"bill_to": {"legal_name": "University of the Fraser Valley (stated on https://www.ufv.ca/about/)", "legal_name_is_published": true, "address": "University of the Fraser Valley Accounts Payable A291- 33844 King Road Abbotsford, BC V2S 7M8", "address_is_the_invoice_address": true, "tax_number": "107403701RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (ufv.ca) + name)", "language": "en"}, "submit_to": {"email": "acctspayable@ufv.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "University of the Fraser Valley Accounts Payable A291- 33844 King Road Abbotsford, BC V2S 7M8", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "yes (as published: purchase order, all invoices must) (as printed on https://www.ufv.ca/finance/accounting-operations/accounts-payable/vendor-payment/, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: purchase order, all invoices must) (as printed on https://www.ufv.ca/finance/accou
- **invoice_readiness**: 10/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id)
- **ap_grade**: A
- **ap_score**: 88
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published; payment cycle or method published (plausibility) | missing: finance mailbox; AP phone or AP contact
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms published
- **facts_provenance_json**: {"mailbox": ["acctspayable@ufv.ca (invoicing/AP)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-03", "page: https://www.ufv.ca/finance/accounting-operations/accounts-payable/vendor-payment/", "quote: \"counts Payable has a dedicated email address for receiving PDF invoices for payment processing. Please forward all invoices for payment to: acctspayable@ufv.ca \"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00005"], "buyer_facts": ["address and phone: the buyer's own site, https://www.ufv.ca/contact_us/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers", "invoice mailing address: the lane's AP page (https://www.ufv.ca/finance/accounting-operations/accounts-payable/vendor-payment/)", "invoicing requirements: the lane's AP page (https://www.ufv.ca/finance/accounting-operations/accounts-payable/vendor-payment/)", "payment terms: the mailbox's evidence page re

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.ufv.ca/finance/accounting-operations/accounts-payable/vendor-payment/ | 2026-11-08 | ok |  | yes (as published: purchase order, all invoices must) |  |  | 33844 King Road Abbotsford, BC V2S 7M8 |  |  |  | must be rendered for each shipment. Invoices must not be submitted until goods/services are shipped/performed. As indicated in the purchase order, all invoices must be submitted via email or mail to: University of the Fr |

## Buyer site facts (org_extras, ufv.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://www.ufv.ca/media/web/logos/UFV-Logo-Horiz_Colour-White_RGB.svg
- **logo_basis**: logo image in the site header
- **domain**: ufv.ca
- **key**: lead:3100eb358ecd387a
- **name**: University of the Fraser Valley
- **website**: https://ufv.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: University of the Fraser Valley
- **legal_name_stated_url**: https://www.ufv.ca/about/
- **legal_name_stated_quote**: Information about University of the Fraser Valley Future Students International Current Students Alumni Donors Calendar myUFV myClass Library Careers
- **mentions**: {'payment_method': {'text': 'interacting with UFV', 'url': 'https://www.ufv.ca/accessible-ufv/', 'quote': 'bility Plan The Accessibility Plan will identify, remove, and prevent barriers to individuals in or interacting with UFV. A tool to receive feedback --> A tool to receive feedback Use the online form to share your experi'}}
- **tel_links**: 604-504-7441; 1-604-504-7441; 1-888-504-7441; 604-557-4045; 18005678911; 18778207444; 18552827770; 18552397654; 60485952

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "33844 King Road, Abbotsford, BC, V2S 7M8", "address_country": "CA", "address_url": "https://www.ufv.ca/contact_us/", "address_method": "microdata", "address_quote": "tact us University of the Fraser Valley 33844 King Road , Abbotsford, BC Canada V2S 7M8 604-504-7441 The University of the Fraser Valley is situated in the traditional", "phone": "604-504-7441", "phone_url": "https://www.ufv.ca/contact_us/", "emails": "info@ufv.ca", "emails_url": "https://www.ufv.ca/contact_us/", "domain": "ufv.ca", "key": "vd:ufv.ca", "name": "University of the Fraser Valley", "website": "https://ufv.ca/", "kind": "vendor", "date": "2026-11-03"}

## Vendor site facts (org_extras, clarkbuilders.com)
- **status**: ok
- **pages**: 4
- **language**: en
- **logo_url**: https://www.clarkbuilders.com/hubfs/CB%20Logo.svg
- **logo_basis**: logo image in the site header
- **domain**: clarkbuilders.com
- **key**: vendor:Clark Builders Inc.
- **name**: Clark Builders Inc.
- **website**: https://clarkbuilders.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Red Deer Regional Hospital
- **legal_name_stated_url**: https://www.clarkbuilders.com/
- **legal_name_stated_quote**: ward-Winning Community Landmark Clark Builders Read More Clark Builders to Self-Perform Concrete at Red Deer Regional Hospital Shaping the future of Alberta's Healthcare Clark Builders Read More Clark Builders to Lead Preconst
- **linkedin_url**: https://www.linkedin.com/company/clark-builders_2/
- **tel_links**: 780.395.3300; 7803953300; 403.253.0565; 4032530565; 604.428.5374; 6044285374; 867.873.6337; 8678736337; 18889725275; 403

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "800 – 5555 Calgary Trail NW , Edmonton, AB, Canada T6H 5P9", "address_country": "CA", "address_url": "https://www.clarkbuilders.com/contact-us", "address_method": "pattern", "address_quote": "EDMONTON Clark Builders Place 800 – 5555 Calgary Trail NW Edmonton, AB, Canada T6H 5P9 780.395.3300 edmonton@clarkbuilders.com Email Us Call Us × CALGARY 222, 4000 –", "phone": "780.395.3300", "phone_url": "https://www.clarkbuilders.com/contact-us", "emails": "reception-rd@clarkbuilders.com", "emails_url": "https://www.clarkbuilders.com/contact-us", "domain": "clarkbuilders.com", "key": "vd:clarkbuilders.com", "name": "Clark Builders Inc.", "website": "https://clarkbuilders.com/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | University of the Fraser Valley | Q2495961 | official website on the organisation's domain (https://www.ufv.ca/) + name |  | University of the Fraser Valley | Université de la Vallée de Fraser | university in British Columbia; charitable organization |  | Canada | 1974-00-00 |  |
| v | Clark Builders Inc. |  |  |  |  |  |  |  |  |  |  |
| v | University of the Fraser Valley | Q2495961 | official website on the organisation's domain (https://www.ufv.ca/) + name |  | University of the Fraser Valley | Université de la Vallée de Fraser | university in British Columbia; charitable organization |  | Canada | 1974-00-00 |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:3100eb358ecd387a",
 "ap_contact_team": {
  "emails": [
   "acctspayable@ufv.ca",
   "purchasing@ufv.ca",
   "procurement@ufv.ca",
   "finance@ufv-fsa.ca",
   "info@ufv.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "acctspayable@ufv.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.ufv.ca/finance/accounting-operations/accounts-payable/vendor-payment/",
    "quote": "counts Payable has a dedicated email address for receiving PDF invoices for payment processing. Please forward all invoices for payment to: acctspayable@ufv.ca . Vendor Direct Deposit (EFT) Canadian vendors are strongly encouraged to use direct deposit, as it will allow payments to be dire",
    "retrieved_date": "2026-11-03",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "University of the Fraser Valley",
    "task_id": "CL-WS-00005"
   },
   {
    "email": "acctspayable@ufv.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.ufv.ca/finance/accounting-operations/accounts-payable/",
    "quote": "ugh the entire procurement and payment cycle. If you have questions we are here to help, please contact a member of our team or email us at acctspayable@ufv.ca . Payments are prepared on a weekly basis, every Thursday. If you are planning to pick up your cheque at Financial Services, pleas",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "University of the Fraser Valley",
    "task_id": "CL-WS-00013"
   },
   {
    "email": "acctspayable@ufv.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.ufv.ca/finance/accounting-operations/accounts-payable/expense-claims/",
    "quote": "also the spending authority, an approval from the one-over-one of the employee must also be received. Submit the form to Accounts Payable ( acctspayable@ufv.ca ), A291 for processing. Note: If this expense claim relates to In-Service PD, please submit to",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "University of the Fraser Valley",
    "task_id": "CL-WS-00386"
   },
   {
    "email": "purchasing@ufv.ca",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.ufv.ca/finance/faq/faq-purchasing-/",
    "quote": "ch code to use, contact your FAL or Accounts Payable. Account Code List Return to Frequently Asked Questions Not sure who to contact? Email purchasing@ufv.ca or call us at 604-504-7441 ext 4010, we would be happy to put you in touch with a member of our team. Download Finance Forms Year En",
    "retrieved_date": "2026-11-03",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "University of the Fraser Valley",
    "task_id": "CL-WS-00005"
   },
   {
    "email": "procurement@ufv.ca",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.ufv.ca/supply-chain/procurement/direct-purchases/",
    "quote": "class=\"well\">Note: If terms and conditions (even under $5,000) apply to your purchase of goods or services, please contact <a href=\"mailto:procurement@ufv.ca\" target=\"_blank\" rel=\"noopener\">Procurement Services</a>. If you require a contract not related to goods and services, please conta",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "University of the Fraser Valley",
    "task_id": "CL-WS-00013"
   },
   {
    "email": "finance@ufv-fsa.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.ufv.ca/directory/",
    "quote": "4-504-7441,,2531\",\"location\":\"Chilliwack - Building A - Room CEPA-1325\",\"department\":\"Academic Advising Centre\",\"onLeave\":\"\"},{\"email_two\":\"finance@ufv-fsa.ca\",\"firstname\":\"Andrea\",\"email_one\":\"",
    "retrieved_date": "2026-11-03",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "University of the Fraser Valley",
    "task_id": "CL-SM-00010"
   },
   {
    "email": "info@ufv.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.ufv.ca/supply-chain/procurement/direct-purchases/",
    "quote": "ervices Distribution Shipping Services Moves Warehousing Asset Disposal & Recycling General Inquiries Event Support Services 1-604-504-7441 info@ufv.ca Future students Academic Calendar Find your program How to Apply Book a tour Transfer credits Tuition & fees FAQs Help Ask a question A to",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "University of the Fraser Valley",

```

## PO-level open data naming this buyer
_none_

## Contract records between the pair (dataset)
_none_

## The buyer's other Canadian-vendor records (first 60 of 0)
_none_

## The vendor's other buyers in the dataset (first 60 of 9)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_alberta_apc:AB-2024-03752:87fa1220-5ea8-4019-9801-12aa494922f1 | Infrastructure | Infrastructure - Request for Proposal - Request for Proposals for Construction Management Services for Red Deer Regional Hospital Centre (RDRHC) Redevelopment - | 147298000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2024-03752 |
| ca_alberta_apc:AB-2025-05056:c5ab9cb3-f972-41b5-86a1-6adc2c9980a9 | NorQuest College | NorQuest College - Request for Proposal - RFP-00078 CSC CM services | 175000000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-05056 |
| ca_alberta_apc:AB-2025-05685:745d99cf-5b1f-4322-9c72-61103209a8a7 | Infrastructure | Infrastructure - Request for Proposal - Request for Proposals (RFP) for Construction Management Services for Red Deer Regional Hospital Centre (RDRHC) Redevelop | 48100000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-05685 |
| ca_bidsandtenders:8d901c86-4f32-4a0b-b5da-651350cc5a25:1 | District of Squamish | Valleycliffe New Daycare CM @ Risk |  |  |  | https://squamish.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/8d901c86-4f32-4a0b-b5da-651350cc5a25 |
| ca_bidsandtenders:6e5a9e22-b46f-42bc-8024-9242fd6a726d:1 | City of Yellowknife | Request for Qualifications - Yellowknife Aquatic Centre |  |  |  | https://yellowknife.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/6e5a9e22-b46f-42bc-8024-9242fd6a726d |
| ca_bidsandtenders:7c35ae86-74b4-4387-bc44-56b39ada5dd2:1 | Government of Yukon | RFB - Carmacks Fire Hall | 6847845.0 |  |  | https://yukon.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/7c35ae86-74b4-4387-bc44-56b39ada5dd2 |
| ca_merx:3566777252:1 | University Of Calgary | IPD General Contractor - Student Housing |  |  |  | https://www.merx.com/universityofcalgary/solicitations/IPD-General-Contractor-Student-Housing/0000300713?origin=0 |
| ca_nwt:0000007060 | Infrastructure | Tulita Health and Social Services Centre New Construction Management Contract | 295048.28 |  |  | https://www.fin.gov.nt.ca/en/resources/contracts-over-5000-report?f%5B0%5D=field_resource_category_legacy%3A582 |
| ca_saskatchewan:8c12de29-d0f7-498c-b123-44bb2b3f02d6:0 | City of Regina | Construction Management Services for Food and Beverage Space Construction and Equipment Procurement |  |  |  | https://www.sasktenders.ca/Competitions/Print?id=8c12de29-d0f7-498c-b123-44bb2b3f02d6 |

## Open questions for hand research (layer 2)

- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

Read 2026-11-09 (Claude, integrator lane).

**The project behind the relationship.** ReNew Canada, "January 30, 2023", https://www.renewcanada.net/contract-awarded-to-build-student-housing-for-university-of-fraser-valley/:
"Turner Construction Company and Clark Builders are pleased to announce that they have been selected" — "The $73.7-million new student housing facility",
"The six-storey, $73 million mass timber building will provide 398 beds", Abbotsford campus, occupancy slated for fall 2024; funding "received $62.3
million from the Province of British Columbian [sic], with $11.4 million funded by UFV." → a construction contract (Turner / Clark Builders joint venture):
invoices are progress claims against the construction contract (BC Builders Lien Act holdback 10 %), not a PO invoice; UFV's AP rule "purchase order, all
invoices must" (row) applies to goods/services — for this contract quote the contract/project number on the certified progress claim. Confirm which entity
bills: the JV, Clark Builders Inc. (row) or Turner — the row's vendor is Clark Builders Inc. (the Canadian partner).
