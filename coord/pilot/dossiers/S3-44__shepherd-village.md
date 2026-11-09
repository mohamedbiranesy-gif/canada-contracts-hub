# S3-44 — Shepherd Village ⇄ St-Aude Advocacy

Stratum: **S3_routed_public_body_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: SHEPHERD VILLAGE INC. (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (shepherdvillage.org) + name) — 3760 Sheppard Avenue East, Toronto, ON M1T 3K9 — buyer tax no. 105240485RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (shepherdvillage.org) + name)
SUBMIT TO: info@shepherdvillage.org (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: ST-AUDE ADVOCACY CORP. (as registered: Canada's Business Registries, ON 1001384834, 2026-11-08) — vendor_address_missing: False; firm_AddressLine1: 31 Ennerdale Rd, Unit 1; firm_AddressLine2: Unit 1; firm_City: York; firm_Province: ON; firm_Country: Canada; firm_PostalCode: M6E 4C2 | GST/HST 764054839 (Canada's Business Registries, ON 1001384834, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 
```

## Relationship
- **rank_group**: B1
- **data_quality_score**: 60
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 1
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Shepherd Village (municipality / local government, jurisdiction not stated) — public contract / purchase award in the last 12 months (dated record): St-Aude Advocacy | subject: Building Permits;Planning and Development;Seniors | awarded 2026-09-23, start 2026-09-23, end 2027-08-26 | published by: Firms/Firm/BusinessAddress (City of Toronto Lobbyist Registry open data) | record: https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/6a87b8bf-f4df-4762-b5dc-bf393336687b/resource/94c1fe59-7247-4b92-b213-950f71e04aff/download/lobbyactivity.zip | vendor in Canada because: Firms/Firm/BusinessAddress (City of Toronto Lobbyist Registry open data)=31 Ennerdale Rd, Unit 1, Unit 1, York, ON, Canada, M6E 4C2 | status rule: likely active (record dated in the last 12 months: Firms/Firm/BusinessAddress (City of Toronto Lobbyist Registry open data))
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: lead:5b677f12e14fea82
- **tier**: B
- **grade**: 1
- **records_with_this_vendor**: 1 (relationship record: Firms/Firm/BusinessAddress (City of Toronto Lobbyist Registry open data); 0 in the contract dataset)

## Buyer
- **buyer**: Shepherd Village
- **buyer_website**: https://shepherdvillage.org/
- **buyer_address**: 3760 Sheppard Avenue East, Toronto, ON M1T 3K9
- **buyer_phone**: 416.609.5700
- **buyer_contact_evidence_url**: https://shepherdvillage.org/contact-us/
- **buyer_legal_name_as_published**: SHEPHERD VILLAGE INC. (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (shepherdvillage.org) + name)
- **buyer_bn_as_published**: 105240485RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (shepherdvillage.org) + name)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 105240485RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_logo_url**: https://shepherdvillage.org/wp-content/themes/shepherdvillage/img/global/shepherdvillage-logo.svg
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://ca.linkedin.com/company/shepherd-village-inc.
- **buyer_type**: municipality / local government
- **buyer_sector**: government: municipal
- **buyer_charity_status**: registered (listed) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (shepherdvillage.org) + name)
- **buyer_charity_designation**: C; 0001
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://shepherdvillage.org/contact-us/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Note: A municipality is not a government for purposes of the GST/HST"); charge GST/HST; derived from buyer type, not published by the buyer
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: info@shepherdvillage.org
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://shepherdvillage.org/visitor-parking/
- **email_evidence_quote**: Accessibility Let’s Encrypt Carf BPSO Contact Information 3760 Sheppard Avenue East Toronto ON M1T 3K9 Tel: 416.609.5700 Fax: 416.609.8329 info@shepherdvillage.org Designed by Ledden Design iT
- **email_evidence_context**: pherd Village was built to bring people together and designed to stand apart. Go to top of page Privacy Policy Accessibility Let’s Encrypt Carf BPSO Contact Information 3760 Sheppard Avenue East Toronto ON M1T 3K9 Tel: 416.609.5700 Fax: 416.609.8329 info@shepherdvillage.org Designed by Ledden Design iT (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: info@shepherdvillage.org (general) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08 | page: https://shepherdvillage.org/visitor-parking/ | quote: "Accessibility Let’s Encrypt Carf BPSO Contact Information 3760 Sheppard Avenue East Toronto ON M1T 3K9 Tel: 416.609.5700 Fax: 416.609.8329 info@shepherdvillage." | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00292
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Microsoft 365
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1; p=quarantine; rua=mailto:ituser@shepherdvillage.org
- **dmarc_record_domain**: shepherdvillage.org
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 +a +mx ip4:216.208.136.82 ip4:216.208.136.84 ip4:172.96.179.225 include:spf.protection.outlook.com include:mailgun.org include:_spf.psm.knowbe4.com ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: SHEPHERD VILLAGE INC. (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (shepherdvillage.org) + name) — 3760 Sheppard Avenue East, Toronto, ON M1T 3K9 — buyer tax no. 105240485RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (shepherdvillage.org) + name) ⏎ SUBMIT TO: info@shepherdvillage.org (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: ST-AUDE ADVOCACY CORP. (as registered: Canada's Business Registries, ON 1001384834, 2026-11-08) — vendor_address_missing: False; firm_AddressLine1: 31 Ennerdale Rd, Unit 1; firm_AddressLine2: Unit 1; firm_City: York; firm_Province: ON; firm_Country: Canada; firm_PostalCode: M6E 4C2 | GST/HST 764054839 (Canada's Business Registries, ON 1001384834, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-
- **invoice_card_json**: {"bill_to": {"legal_name": "SHEPHERD VILLAGE INC. (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (shepherdvillage.org) + name)", "legal_name_is_published": true, "address": "3760 Sheppard Avenue East, Toronto, ON M1T 3K9", "address_is_the_invoice_address": false, "tax_number": "105240485RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (shepherdvillage.org) + name)", "language": "en"}, "submit_to": {"email": "info@shepherdvillage.org", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, htt
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: St-Aude Advocacy
- **vendor_legal_name**: ST-AUDE ADVOCACY CORP. (as registered: Canada's Business Registries, ON 1001384834, 2026-11-08)
- **vendor_registry_id**: 1001384834 (ON)
- **vendor_registry_url**: https://ised-isde.canada.ca/cbr-rec/en/search?q=St-Aude%20Advocacy
- **vendor_registered_address**: York, Ontario (registered office city / province; Canada's Business Registries, ON 1001384834, 2026-11-08)
- **vendor_legal_form**: ONTARIO BUSINESS CORP. (Canada's Business Registries, ON 1001384834, 2026-11-08)
- **vendor_address**: vendor_address_missing: False; firm_AddressLine1: 31 Ennerdale Rd, Unit 1; firm_AddressLine2: Unit 1; firm_City: York; firm_Province: ON; firm_Country: Canada; firm_PostalCode: M6E 4C2
- **vendor_country_basis**: Firms/Firm/BusinessAddress (City of Toronto Lobbyist Registry open data)=31 Ennerdale Rd, Unit 1, Unit 1, York, ON, Canada, M6E 4C2
- **vendor_bn9**: 764054839 (Canada's Business Registries, ON 1001384834, 2026-11-08)
- **vendor_gst_hst_derived**: 764054839RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://st-audeadvocacy.com/
- **vendor_emails**: info@st-audeadvocacy.com
- **vendor_contact_evidence_url**: https://st-audeadvocacy.com/
- **vendor_logo_url**: https://st-audeadvocacy.com/images/CTV_logo_2018.svg.png
- **vendor_website_basis**: found by a web search, confirmed by reading the site on 2026-11-08: https://st-audeadvocacy.com/ (St-Aude Advocacy — The right word, at the right moment. Services Our Story Our Partners Get in Touch → EN / FR --> --> --> --> --> --> Public Affairs · Boutique)
- **vendor_facts_provenance**: name and address: the record's vendor block (Firms/Firm/BusinessAddress (City of Toronto Lobbyist Registry open data)); registry identity: 1001384834 (ON) status Active — incorporated (Canada's Business Registries, ON 1001384834, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: registry: Canada's Business Registries, ON 1001384834, 2026-11-08; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2025-10-16; phone / role e-mails / logo: the vendor's own site, https://st-audeadvocacy.com/ (tools/org_contacts.py, org_extras.py); website: https://st-audeadvocacy.com/
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Active — incorporated (Canada's Business Registries, ON 1001384834, 2026-11-08)
- **vendor_incorporation_date**: 2025-10-16
- **vendor_years_in_business**: 1.1 (since 2025-10-16, registry date)
- **vendor_bn_source**: registry: Canada's Business Registries, ON 1001384834, 2026-11-08

## Contract
- **contract_status**: likely active (record dated in the last 12 months: Firms/Firm/BusinessAddress (City of Toronto Lobbyist Registry open data))
- **contract_title**: Building Permits;Planning and Development;Seniors
- **contract_description**: Building Permits;Planning and Development;Seniors (the record's title; the source publishes no separate description)
- **award_date**: 2026-09-23
- **start_date**: 2026-09-23
- **end_date**: 2027-08-26
- **contract_link**: https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/6a87b8bf-f4df-4762-b5dc-bf393336687b/resource/94c1fe59-7247-4b92-b213-950f71e04aff/download/lobbyactivity.zip
- **source**: Firms/Firm/BusinessAddress (City of Toronto Lobbyist Registry open data)
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: Firms/Firm/BusinessAddress (City of Toronto Lobbyist Registry open data); 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 105240485RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_tax_status_derived**: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Note: A municipality is not a government for purposes of the GST/HST"); charge GST/HST; derived from buyer type, not published by the buyer
- **tax_rate_indicative_derived**: HST 13% (Ontario) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 764054839RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: SHEPHERD VILLAGE INC. (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (shepherdvillage.org) + name) — 3760 Sheppard Avenue East, Toronto, ON M1T 3K9 — buyer tax no. 105240485RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (shepherdvillage.org) + name) ⏎ SUBMIT TO: info@shepherdvillage.org (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: ST-AUDE ADVOCACY CORP. (as registered: Canada's Business Registries, ON 1001384834, 2026-11-08) — vendor_address_missing: False; firm_AddressLine1: 31 Ennerdale Rd, Unit 1; firm_AddressLine2: Unit 1; firm_City: York; firm_Province: ON; firm_Country: Canada; firm_PostalCode: M6E 4C2 | GST/HST 764054839 (Canada's Business Registries, ON 1001384834, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-
- **invoice_card_json**: {"bill_to": {"legal_name": "SHEPHERD VILLAGE INC. (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (shepherdvillage.org) + name)", "legal_name_is_published": true, "address": "3760 Sheppard Avenue East, Toronto, ON M1T 3K9", "address_is_the_invoice_address": false, "tax_number": "105240485RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (shepherdvillage.org) + name)", "language": "en"}, "submit_to": {"email": "info@shepherdvillage.org", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, htt
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["info@shepherdvillage.org (general)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08", "page: https://shepherdvillage.org/visitor-parking/", "quote: \"Accessibility Let’s Encrypt Carf BPSO Contact Information 3760 Sheppard Avenue East Toronto ON M1T 3K9 Tel: 416.609.5700 Fax: 416.609.8329 info@shepherdvillage.\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00292"], "buyer_facts": ["address and phone: the buyer's own site, https://shepherdvillage.org/contact-us/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (Firms/Firm/BusinessAddress (City of Toronto Lobbyist Registry open data))", "registry identity: 1001384834 (ON) status Active — incorporated (Canada's Business Registries, ON 1001384834, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data"

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://shepherdvillage.org/ | 2026-11-08 | ok |  |  |  | 416.609.5700 | 3760 Sheppard Avenue East Toronto ON M1T 3K9 |  |  |  |  |

## Buyer site facts (org_extras, shepherdvillage.org)
- **status**: ok
- **pages**: 5
- **language**: en
- **logo_url**: https://shepherdvillage.org/wp-content/themes/shepherdvillage/img/global/shepherdvillage-logo.svg
- **logo_basis**: logo image in the site header
- **domain**: shepherdvillage.org
- **key**: lead:5b677f12e14fea82
- **name**: Shepherd Village
- **website**: https://shepherdvillage.org/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Best Practice Spotlight Organization
- **legal_name_stated_url**: https://shepherdvillage.org/accessibility/
- **legal_name_stated_quote**: dership, Empowerment, Achievement, and Determination. About Us What We Do Covid-19 Information Page Best Practice Spotlight Organization (BPSO) History Affiliates Publications Work Here Donate Visitor Parking Contact Us Work Here Donate
- **linkedin_url**: https://ca.linkedin.com/company/shepherd-village-inc.

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "3760 Sheppard Avenue East, Toronto, ON M1T 3K9", "address_country": "CA", "address_url": "https://shepherdvillage.org/contact-us/", "address_method": "pattern", "address_quote": "ax: 416.609.8329 info@shepherdvillage.org 3760 Sheppard Avenue East Toronto, ON M1T 3K9 Popular Extensions If you aren’t sure who to speak with, call our Receptionist", "phone": "416.609.5700", "phone_url": "https://shepherdvillage.org/contact-us/", "emails": "info@shepherdvillage.org", "emails_url": "https://shepherdvillage.org/contact-us/", "domain": "shepherdvillage.org", "key": "lead:5b677f12e14fea82", "name": "Shepherd Village", "website": "https://shepherdvillage.org/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, st-audeadvocacy.com)
- **status**: ok
- **pages**: 2
- **v**: 2
- **language**: en
- **logo_url**: https://st-audeadvocacy.com/images/CTV_logo_2018.svg.png
- **logo_basis**: logo image in the site header
- **domain**: st-audeadvocacy.com
- **key**: vendor:St-Aude Advocacy
- **name**: St-Aude Advocacy
- **website**: https://st-audeadvocacy.com/
- **kind**: vendor
- **date**: 2026-11-09

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 1, "address": "781 William Street · Suite 303, QC · H3C 1P1, +1 514 · 000 · 0000", "address_country": "", "address_url": "https://st-audeadvocacy.com/", "address_method": "address-tag", "address_quote": "call → The right word, at the right moment. 781 William Street · Suite 303 QC · H3C 1P1 +1 514 · 000 · 0000 --> Quick Links Home Our Story Our Partners Get in Touch Se", "emails": "info@st-audeadvocacy.com", "emails_url": "https://st-audeadvocacy.com/", "domain": "st-audeadvocacy.com", "key": "vendor:St-Aude Advocacy", "name": "St-Aude Advocacy", "website": "https://st-audeadvocacy.com/", "kind": "vendor", "date": "2026-11-09"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Shepherd Village |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:5b677f12e14fea82",
 "ap_contact_team": {
  "emails": [
   "info@shepherdvillage.org"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "info@shepherdvillage.org",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://shepherdvillage.org/",
    "quote": "Accessibility Let’s Encrypt Carf BPSO Contact Information 3760 Sheppard Avenue East Toronto ON M1T 3K9 Tel: 416.609.5700 Fax: 416.609.8329 info@shepherdvillage.org Designed by Ledden Design iT",
    "retrieved_date": "2026-11-02",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Shepherd Village",
    "task_id": "CL-SN-03496"
   },
   {
    "email": "info@shepherdvillage.org",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://shepherdvillage.org/visitor-parking/",
    "quote": "Accessibility Let’s Encrypt Carf BPSO Contact Information 3760 Sheppard Avenue East Toronto ON M1T 3K9 Tel: 416.609.5700 Fax: 416.609.8329 info@shepherdvillage.org Designed by Ledden Design iT",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Shepherd Village",
    "task_id": "CL-WS-00292"
   }
  ]
 },
 "research_status": {
  "found": 2
 },
 "queries_tried": [
  "site crawl of shepherdvillage.org (7 pages, robots.txt respected), no AI, no search engine",
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
- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
