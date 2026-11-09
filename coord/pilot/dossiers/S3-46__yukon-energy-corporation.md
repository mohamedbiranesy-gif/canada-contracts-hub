# S3-46 — Yukon Energy Corporation ⇄ Electricity Canada

Stratum: **S3_routed_public_body_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Yukon University (stated on https://yukonenergy.ca/information/contact-us/) — Miles Canyon Road, Box 5920, Whitehorse, Yukon Y1A 6S7 — buyer tax no. 123007494 (recipient_business_number in the federal grants & contributions disclosure, 1 agreement(s), last 2026-07-29; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)
SUBMIT TO: procurement@yec.yk.ca (purchasing mailbox, confirmed by the referee) | tender portal (not an invoice channel): https://www.merx.com/ — MERX
REFERENCE: none in the record | PO rule: purchase-order terms published (as published: Purchase Orders shall)
FROM / REMIT TO: Electricity Canada (as registered: Corporations Canada (open data), corporation number 346098, 2026-11-08) — 275 Slater Street, Suite 1500, Ottawa, ON, K1P 5H9 | GST/HST 121356901 (Corporations Canada (open data), corporation number 346098, 2026-11-08)RT0001 (account derived from the BN9)
TAX: GST registration number must be shown on all invoices and the Purchase Order (“PO”), including the (as printed on https://yukonenergy.ca/media/site_documents/CT | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: net 30 days (as printed on https://yukonenergy.ca/media/site_documents/CTR005_POTermsAndConditions_S
DESCRIPTION: Yukon Energy Corporation (utility / pub
```

## Relationship
- **rank_group**: M2
- **data_quality_score**: 64
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 1
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Yukon Energy Corporation (utility / public corporation, jurisdiction not stated) — member or regulated payer of a Canadian body (current list): Electricity Canada | awarded 2026-11-03 | published by: the Canadian body's own current member / participant list | record: https://www.electricity.ca/membership/list-of-members/ | vendor in Canada because: membership / statutory fee relationship: current list published by the Canadian body (Electricity Canada)=Electricity Canada 275 Slater Street, Suite 1500 Ottawa, Ontario, Canada K1P 5H9 | status rule: member / regulated payer of a Canadian body (current list read 2026-11-03): Electricity Canada
- **how_relationship_was_found**: tools/member_lists.py read the Canadian body's current member / regulated-payer list and matched the buyer by name
- **keys**: lead:a43875d61d737252
- **tier**: M
- **grade**: 2
- **records_with_this_vendor**: 1 (relationship record: the Canadian body's own current member / participant list; 0 in the contract dataset)

## Buyer
- **buyer**: Yukon Energy Corporation
- **buyer_website**: https://yukonenergy.ca/
- **buyer_address**: Miles Canyon Road, Box 5920, Whitehorse, Yukon Y1A 6S7
- **buyer_phone**: (867) 393-5335 (printed next to the organisation's mailbox (as printed on https://yukonenergy.ca/about-us/purchasing-tenders/inquiries/, re-read 2026-11-08))
- **buyer_contact_evidence_url**: https://yukonenergy.ca/information/contact-us
- **buyer_legal_name_as_published**: Yukon University (stated on https://yukonenergy.ca/information/contact-us/)
- **buyer_bn_as_published**: 123007494 (recipient_business_number in the federal grants & contributions disclosure, 1 agreement(s), last 2026-07-29; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 123007494RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_logo_url**: https://yukonenergy.ca/assets/layout/favicon.png
- **buyer_website_status**: site answers
- **buyer_type**: utility / public corporation
- **buyer_sector**: utility
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://yukonenergy.ca/information/contact-us (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers; payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_exempt_status**: GST registration number must be shown on all invoices and the Purchase Order (“PO”), including the (as printed on https://yukonenergy.ca/media/site_documents/CTR005_POTermsAndConditions_Sep2026.pdf, re-read 2026-11-08)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of YT on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: procurement@yec.yk.ca
- **email_type**: purchasing
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); purchasing mailbox
- **email_evidence_url**: https://yukonenergy.ca/about-us/purchasing-tenders/inquiries/
- **email_evidence_quote**: t #2 Miles Canyon Road Box 5920 Whitehorse, Yukon Canada Y1A 6S7 Phone: (867) 393-5335 Fax: (867) 393-5301 Toll-free: 1-866-926-3749 Email: procurement@yec.yk.ca About Us Who We Are News & Events Purchasing and Tenders Careers Business Documents Energy in Yukon Electricity 101 Projects and
- **email_evidence_context**: Order Terms and Conditions Careers Business Documents Inquiries Yukon Energy Corporation Attention: Procurement #2 Miles Canyon Road Box 5920 Whitehorse, Yukon Canada Y1A 6S7 Phone: (867) 393-5335 Fax: (867) 393-5301 Toll-free: 1-866-926-3749 Email: procurement@yec.yk.ca About Us Who We Are News & Events Purchasing and Tenders Careers Business Documents Energy in Yukon Electricity 101 Projects and Facilities Energy Future Saving Energy Small-Scale Renewable Power Environment Commitment Conservation Climate Change Cu (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: procurement@yec.yk.ca (purchasing) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08 | page: https://yukonenergy.ca/about-us/purchasing-tenders/inquiries/ | quote: "t #2 Miles Canyon Road Box 5920 Whitehorse, Yukon Canada Y1A 6S7 Phone: (867) 393-5335 Fax: (867) 393-5301 Toll-free: 1-866-926-3749 Email: procurement@yec.yk.c" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Cisco | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00013
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Cisco
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject; rua=mailto:fc632220@mxtoolbox.dmarc-report.com,mailto:pcashaback@yec.yk.ca; ruf=mailto:fc632220@forensics.dmarc-report.com,mailto:pcashaback@yec.yk.ca; fo=1; pct=10
- **dmarc_record_domain**: yec.yk.ca
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 mx a ip4:216.71.132.34 ip4:199.85.230.166 ip4:216.71.129.24 include:_spf.psm.knowbe4.com include:spf.protection.outlook.com include:_phishspf.knowbe4.com include:spf.ca.exclaimer.net -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **payment_terms_as_published**: net 30 days (as printed on https://yukonenergy.ca/media/site_documents/CTR005_POTermsAndConditions_Sep2026.pdf, re-read 2026-11-08)
- **po_required_as_published**: purchase-order terms published (as published: Purchase Orders shall) (as printed on https://yukonenergy.ca/media/site_documents/542_GS-003%20Purchasing%20Agreements%20Guideline.pdf, re-read 2026-11-08)
- **invoice_portal_url**: https://www.merx.com/ — MERX
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **ap_system_hint**: named on the buyer's page: MERX (as printed on https://yukonenergy.ca/about-us/purchasing-tenders/tenders-proposals-registry/, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "payment_terms": "net 30 days (as printed on https://yukonenergy.ca/media/site_documents/CTR005_POTermsAndConditions_Sep2026.pdf, re-read 2026-11-08)", "po_required": "purchase-order terms published (as published: Purchase Orders shall) (as printed on https://yukonenergy.ca/media/site_documents/542_GS-003%20Purchasing%20Agreements%20Guideline.pdf, re-read 2026-11-08)", "portal_url": "https://www.merx.com/ — MERX", "portal_kind": "actionable supplier / invoice portal named by the buyer"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Yukon University (stated on https://yukonenergy.ca/information/contact-us/) — Miles Canyon Road, Box 5920, Whitehorse, Yukon Y1A 6S7 — buyer tax no. 123007494 (recipient_business_number in the federal grants & contributions disclosure, 1 agreement(s), last 2026-07-29; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv) ⏎ SUBMIT TO: procurement@yec.yk.ca (purchasing mailbox, confirmed by the referee) | tender portal (not an invoice channel): https://www.merx.com/ — MERX ⏎ REFERENCE: none in the record | PO rule: purchase-order terms published (as published: Purchase Orders shall) ⏎ FROM / REMIT TO: Electricity Canada (as registered: Corporations Canada (open data), corporation number 346098, 2026-11-08) — 275 Slater Street, Suite 1500, Ottawa, ON, K1P 5H9 | GST/HST 121356901 (Corporations Canada (open data), corporation number 346098, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: GST registration number must be shown on all invoices and the Purchase Order (“PO”), including the (as printed on https://yukonenergy.ca/media/site_documents/CT | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: net 30 days (as printed on https://yukonenergy.ca/media/site_documents/CTR005_POTermsAndConditions_S ⏎ DESCRIPTION: Yukon Energy Corporation (u
- **invoice_card_json**: {"bill_to": {"legal_name": "Yukon University (stated on https://yukonenergy.ca/information/contact-us/)", "legal_name_is_published": true, "address": "Miles Canyon Road, Box 5920, Whitehorse, Yukon Y1A 6S7", "address_is_the_invoice_address": false, "tax_number": "123007494 (recipient_business_number in the federal grants & contributions disclosure, 1 agreement(s), last 2026-07-29; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)", "language": "en"}, "submit_to": {"email": "procurement@yec.yk.ca", "email_type": "purchasing", "supplier_setup_url": "", "portal_url": "https://www.merx.com/ — MERX", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: MERX (as printed on https://yukonenergy.ca/about-us/purchasing-tenders/tenders-proposals-registry/, re-read 2026-11-08)", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "tender portal (not an invoice channel)"}, "references_required": {"po_required": "purchase-order terms published (as published: Purchase Orders shall) (as printed on https://yukonenergy.ca/media/site_documents/542_GS-003%20Purchasing%20Agreements%20Guideline.pdf, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes purchase-order t
- **invoice_readiness**: 10/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id)
- **ap_grade**: C
- **ap_score**: 63
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known | missing: invoicing / AP mailbox; finance mailbox; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general)
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: the buyer's purchase-order number: the buyer publishes purchase-order terms, so the PO number is the reference to quote (purchase-order terms published (as published: Purchase Orders shall) (as printed on https://yukonenergy.ca/media/site_documents/542_GS-003%20Purchasing%20Agreements%20Guideline.pdf, re-read 2026-11-08)

## Vendor
- **vendor**: Electricity Canada
- **vendor_legal_name**: Electricity Canada (as registered: Corporations Canada (open data), corporation number 346098, 2026-11-08)
- **vendor_trading_name**: Électricité Canada (alternate names in the registry)
- **vendor_registry_id**: corporation number 346098 (Corporations Canada (open data))
- **vendor_registry_url**: https://ised-isde.canada.ca/cc/lgcy/fdrlCrpDtls.html?corpId=346098
- **vendor_registered_address**: 275 SLATER STREET, SUITE 1500, OTTAWA, ON, K1P 5H9 (registered address; Corporations Canada (open data), corporation number 346098, 2026-11-08)
- **vendor_legal_form**: Canada Not-for-profit Corporations Act (Corporations Canada (open data), corporation number 346098, 2026-11-08)
- **vendor_address**: 275 Slater Street, Suite 1500, Ottawa, ON, K1P 5H9
- **vendor_country_basis**: membership / statutory fee relationship: current list published by the Canadian body (Electricity Canada)=Electricity Canada 275 Slater Street, Suite 1500 Ottawa, Ontario, Canada K1P 5H9
- **vendor_bn9**: 121356901 (Corporations Canada (open data), corporation number 346098, 2026-11-08)
- **vendor_gst_hst_derived**: 121356901RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://electricity.ca/
- **vendor_emails**: info@electricity.ca
- **vendor_phone**: +1-613-230-9263
- **vendor_contact_evidence_url**: https://www.electricity.ca/about/contact
- **vendor_logo_url**: https://www.electricity.ca/favicons/apple-touch-icon.png
- **vendor_website_basis**: found by a web search, confirmed by reading the site on 2026-11-08: https://www.electricity.ca/ (Home | Electricity Canada Search EFIC Course Member Login News FR Search About Membership Advocacy Programs Educational Resources Events Back About Strategic Pl)
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canadian body's own current member / participant list); registry identity: corporation number 346098 (Corporations Canada (open data)) status Active (Corporations Canada (open data), corporation number 346098, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: registry: Corporations Canada (open data), corporation number 346098, 2026-11-08; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2016-10-27; phone / role e-mails / logo: the vendor's own site, https://www.electricity.ca/about/contact (tools/org_contacts.py, org_extras.py); website: https://electricity.ca/
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Active (Corporations Canada (open data), corporation number 346098, 2026-11-08)
- **vendor_incorporation_date**: 2016-10-27
- **vendor_years_in_business**: 10.0 (since 2016-10-27, registry date)
- **vendor_bn_source**: registry: Corporations Canada (open data), corporation number 346098, 2026-11-08

## Contract
- **po_required_as_published**: purchase-order terms published (as published: Purchase Orders shall) (as printed on https://yukonenergy.ca/media/site_documents/542_GS-003%20Purchasing%20Agreements%20Guideline.pdf, re-read 2026-11-08)
- **contract_status**: member / regulated payer of a Canadian body (current list read 2026-11-03): Electricity Canada
- **award_date**: 2026-11-03
- **contract_link**: https://www.electricity.ca/membership/list-of-members/
- **source**: the Canadian body's own current member / participant list
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canadian body's own current member / participant list; 0 in the contract dataset)
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 123007494RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of YT on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (YT) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 121356901RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Yukon University (stated on https://yukonenergy.ca/information/contact-us/) — Miles Canyon Road, Box 5920, Whitehorse, Yukon Y1A 6S7 — buyer tax no. 123007494 (recipient_business_number in the federal grants & contributions disclosure, 1 agreement(s), last 2026-07-29; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv) ⏎ SUBMIT TO: procurement@yec.yk.ca (purchasing mailbox, confirmed by the referee) | tender portal (not an invoice channel): https://www.merx.com/ — MERX ⏎ REFERENCE: none in the record | PO rule: purchase-order terms published (as published: Purchase Orders shall) ⏎ FROM / REMIT TO: Electricity Canada (as registered: Corporations Canada (open data), corporation number 346098, 2026-11-08) — 275 Slater Street, Suite 1500, Ottawa, ON, K1P 5H9 | GST/HST 121356901 (Corporations Canada (open data), corporation number 346098, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: GST registration number must be shown on all invoices and the Purchase Order (“PO”), including the (as printed on https://yukonenergy.ca/media/site_documents/CT | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: net 30 days (as printed on https://yukonenergy.ca/media/site_documents/CTR005_POTermsAndConditions_S ⏎ DESCRIPTION: Yukon Energy Corporation (u
- **invoice_card_json**: {"bill_to": {"legal_name": "Yukon University (stated on https://yukonenergy.ca/information/contact-us/)", "legal_name_is_published": true, "address": "Miles Canyon Road, Box 5920, Whitehorse, Yukon Y1A 6S7", "address_is_the_invoice_address": false, "tax_number": "123007494 (recipient_business_number in the federal grants & contributions disclosure, 1 agreement(s), last 2026-07-29; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)", "language": "en"}, "submit_to": {"email": "procurement@yec.yk.ca", "email_type": "purchasing", "supplier_setup_url": "", "portal_url": "https://www.merx.com/ — MERX", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: MERX (as printed on https://yukonenergy.ca/about-us/purchasing-tenders/tenders-proposals-registry/, re-read 2026-11-08)", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "tender portal (not an invoice channel)"}, "references_required": {"po_required": "purchase-order terms published (as published: Purchase Orders shall) (as printed on https://yukonenergy.ca/media/site_documents/542_GS-003%20Purchasing%20Agreements%20Guideline.pdf, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes purchase-order t
- **invoice_readiness**: 10/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id)
- **ap_grade**: C
- **ap_score**: 63
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known | missing: invoicing / AP mailbox; finance mailbox; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general)
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel
- **facts_provenance_json**: {"mailbox": ["procurement@yec.yk.ca (purchasing)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08", "page: https://yukonenergy.ca/about-us/purchasing-tenders/inquiries/", "quote: \"t #2 Miles Canyon Road Box 5920 Whitehorse, Yukon Canada Y1A 6S7 Phone: (867) 393-5335 Fax: (867) 393-5301 Toll-free: 1-866-926-3749 Email: procurement@yec.yk.c\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Cisco", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00013"], "buyer_facts": ["address and phone: the buyer's own site, https://yukonenergy.ca/information/contact-us (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://yukonenergy.ca/about-us/purchasing-tenders/inquiries/ | 2026-11-08 | ok |  |  |  | (867) 393-5335 |  |  |  |  |  |

## Buyer site facts (org_extras, yukonenergy.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **domain**: yukonenergy.ca
- **key**: lead:a43875d61d737252
- **name**: Yukon Energy Corporation
- **website**: https://yukonenergy.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Yukon University
- **legal_name_stated_url**: https://yukonenergy.ca/information/contact-us/
- **legal_name_stated_quote**: an return your call. In-person bill support in Dawson City: October 13, 2026 from 6pm to 8pm at the Yukon University, Dawson campus. October 14, 2026 from 9am to 2pm at Yukon Energy's office Office Address Fifth and
- **logo_url**: https://yukonenergy.ca/assets/layout/favicon.png
- **logo_basis**: site icon (icon link)

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "Miles Canyon Road, Box 5920, Whitehorse, Yukon Y1A 6S7", "address_country": "CA", "address_url": "https://yukonenergy.ca/information/contact-us", "address_method": "pattern", "address_quote": "nd mailing addresses Whitehorse #2 Miles Canyon Road Box 5920 Whitehorse, Yukon Y1A 6S7 For Whitehorse warehouse deliveries #5 Lindeman Road Whitehorse, Yukon Y1A 5Z7", "emails": "billing@yec.yk.ca; communications@yec.yk.ca", "emails_url": "https://yukonenergy.ca/information/contact-us", "domain": "yukonenergy.ca", "key": "lead:a43875d61d737252", "name": "Yukon Energy Corporation", "website": "https://yukonenergy.ca/", "kind": "buyer", "date": "2026-11-04"}

## Vendor site facts (org_extras, electricity.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://www.electricity.ca/favicons/apple-touch-icon.png
- **logo_basis**: site icon (apple-touch-icon)
- **domain**: electricity.ca
- **key**: wd:Q30294979
- **name**: Canadian Electricity Association
- **website**: https://electricity.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Electricity Canada
- **jsonld_address**: 275 Slater Street, Suite 1500, Ottawa, ON, K1P 5H9, Canada
- **jsonld_phone**: +1-613-230-9263
- **jsonld_logo**: https://www.electricity.ca/dist/ec-logo-en.png
- **jsonld_url**: https://www.electricity.ca/
- **jsonld_same_as**: http://www.facebook.com/electricitycanada; https://twitter.com/Electricity_CA; http://www.linkedin.com/company/electricity-canada; https://www.youtube.com/channel/UC5psDKH4ZerAyb6EBd4x5nA
- **jsonld_quote**: { "@context":"https://schema.org", "@graph":[ { "@type":"WebPage", "author":{ "@id":"https://www.electricity.ca/#identity" }, "copyrightHolder":{ "@id":"https://www.electricity.ca/#identity" }, "copyrightYear":"2022-03-01T10:00:00-05:00", "dateModified":"2026-10-28T14:02:22-04:00", "datePublished":"
- **jsonld_page**: https://www.electricity.ca/
- **legal_name_stated**: Independent Electricity System Operator
- **legal_name_stated_url**: https://www.electricity.ca/about/our-team/
- **legal_name_stated_quote**: & Chief Executive Officer FortisAlberta Inc., Calgary, Alberta Jason Fitzsimmons President and CEO Independent Electricity System Operator (IESO), Toronto, Ontario Jason Roberts President & Chief Executive Officer Maritime Electric Compan
- **mentions**: {'payment_method': {'text': 'interactions between its members, governments, and regulators at all levels', 'url': 'https://www.electricity.ca/about/our-purpose/', 'quote': 'ble solutions to the nation’s energy transition, energy security and resiliency goals, and supports interactions between its members, governments, and regulators at all levels. It also facilitates its members’ relationships with key industry partners, and with'}}
- **linkedin_url**: http://www.linkedin.com/company/electricity-canada
- **tel_links**: +16132309263

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "address": "275 Slater Street, Suite 1500, Ottawa, ON, K1P 5H9", "address_country": "Canada", "address_url": "https://www.electricity.ca/about/contact", "address_method": "json-ld", "address_quote": "ty.ca 613.230.9263 Address 275 Slater Street, Suite 1500 Ottawa, Ontario Canada K1P 5H9 Media Inquiries media@electricity.ca 613.809.0720 Contact us by email Contact E", "phone": "+1-613-230-9263", "phone_url": "https://www.electricity.ca/about/contact", "emails": "info@electricity.ca", "emails_url": "https://www.electricity.ca/about/contact", "domain": "electricity.ca", "key": "vd:electricity.ca", "name": "Canadian Electricity Association", "website": "https://electricity.ca/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Yukon Energy Corporation | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Yukon%20Energy%20Corporation | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Yukon Energy Corporation |  |  |  |  |  |  |  |  |  |  |
| b | Canadian Electricity Association | Q30294979 | official website on the organisation's domain (http://www.electricity.ca/) + name |  | Canadian Electricity Association | Association canadienne de l'électricité | nonprofit organization |  | Canada | 1891-01-01 |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:a43875d61d737252",
 "ap_contact_team": {
  "emails": [
   "procurement@yec.yk.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "procurement@yec.yk.ca",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://yukonenergy.ca/about-us/purchasing-tenders/inquiries/",
    "quote": "t #2 Miles Canyon Road Box 5920 Whitehorse, Yukon Canada Y1A 6S7 Phone: (867) 393-5335 Fax: (867) 393-5301 Toll-free: 1-866-926-3749 Email: procurement@yec.yk.ca About Us Who We Are News & Events Purchasing and Tenders Careers Business Documents Energy in Yukon Electricity 101 Projects and",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Yukon Energy Corporation",
    "task_id": "CL-LD-15850"
   },
   {
    "email": "procurement@yec.yk.ca",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://yukonenergy.ca/about-us/purchasing-tenders/inquiries/",
    "quote": "t #2 Miles Canyon Road Box 5920 Whitehorse, Yukon Canada Y1A 6S7 Phone: (867) 393-5335 Fax: (867) 393-5301 Toll-free: 1-866-926-3749 Email: procurement@yec.yk.ca About Us Who We Are News & Events Purchasing and Tenders Careers Business Documents Energy in Yukon Electricity 101 Projects and",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Yukon Energy Corporation",
    "task_id": "CL-WS-00013"
   }
  ]
 },
 "research_status": {
  "found": 2
 },
 "queries_tried": [
  "site crawl of yukonenergy.ca (25 pages, robots.txt respected), no AI, no search engine",
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

- an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
