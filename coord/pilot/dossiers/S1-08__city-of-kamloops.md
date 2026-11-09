# S1-08 — City of Kamloops ⇄ BDO Canada LLP

Stratum: **S1_gold_complete_published_PO_rule** · pay on sight: yes · channel tier 1 · AP grade A · missing: —

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: City of Kamloops — 7 Victoria Street West, Kamloops BC V2C 1A2
SUBMIT TO: ap@kamloops.ca (invoicing/AP mailbox, confirmed by the referee) | tender portal (not an invoice channel): Bonfire
REFERENCE: contract 344842 (tender_no) — the source publishes the award under this tender / notice number and no separate contract number; tender 344842 (tender_no) | PO rule: yes (as published: quote the first and last name of the employee who requested goods or services Purchase Order Number)
FROM / REMIT TO: BDO Canada Limited — 20 Wellington Street East , Ontario, ON, M5E 1C5, Canada | GST/HST 101518124RT0001 (account derived from the BN9) | NEQ 3342011858
TAX: Tax Exemptions Property Tax Estimator Property Tax Sale Frequently Asked Questions Capital Projects Transportatio (as printed on https://www.kamloops.ca/city-ha | CURRENCY: CAD (derived from the source's government) | TERMS: terms are net 30 (as printed on https://www.kamloops.ca/city-hall/procurement-services/accounts-paya
DESCRIPTION: City of Kamloops (municipality / local government, BC) — public contract / purchase award in the last 12 months (dated record): BDO Canada L | AMOUNT: 17265535.0 (source field: amount) CAD
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 92
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 1
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: City of Kamloops (municipality / local government, BC) — public contract / purchase award in the last 12 months (dated record): BDO Canada LLP | instrument: contract award summary | contract number: 344842 (tender_no) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference | solicitation: 344842 (tender_no) | value: 17265535.0 (source field: amount) CAD (derived from the source's government) | awarded 2026-04-15 | published by: auditor of record (own audited financial statements, auditor's report signed in Kamloops,  | record: https://www.kamloops.ca/sites/default/files/2025%20Financial%20Statements%20-%20City%20of%20Kamloops.pdf | vendor in Canada because: auditor of record (own audited financial statements, auditor's report signed in Kamloops, British Columbia)=es in internal control that we identify during our audit. | Tel: 250 372 9505 | BDO Canada LLP | Fax: 250 374 63 | status rule: likely active (record dated in the last 12 months: auditor of record (own audited financial statements, auditor's report signed in Kamloops, ) | this buyer has 4 records with Canada-located vendors (4 distinct vendors; 0 in the last 12 months; latest 2022-08-12)
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: b:203ef6db95431178|lead:a962e62576ca5401
- **tier**: B
- **grade**: 4
- **records_with_this_vendor**: 1

## Buyer
- **buyer**: City of Kamloops
- **buyer_website**: https://kamloops.ca
- **buyer_address**: 7 Victoria Street West, Kamloops BC V2C 1A2
- **buyer_contact_evidence_url**: https://www.kamloops.ca/city-hall/contact-us
- **buyer_legal_name_as_published**: City of Kamloops
- **buyer_logo_url**: https://www.kamloops.ca/sites/default/files/kamloops-logo-home.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://ca.linkedin.com/company/city-of-kamloops
- **buyer_type**: municipality / local government
- **buyer_sector**: government: municipal
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q473209; city in British Columbia
- **buyer_founded**: 1811-00-00 (Wikidata Q473209, official website on the organisation's domain (https://kamloops.ca) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.kamloops.ca/city-hall/contact-us (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); AP contact name: the lane's AP page (https://www.kamloops.ca/city-hall/procurement-services/accounts-payable)
- **buyer_tax_exempt_status**: Tax Exemptions Property Tax Estimator Property Tax Sale Frequently Asked Questions Capital Projects Transportatio (as printed on https://www.kamloops.ca/city-hall/procurement-services/accounts-payable, re-read 2026-11-08)
- **buyer_tax_status_derived**: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Note: A municipality is not a government for purposes of the GST/HST"); charge GST/HST; derived from buyer type, not published by the buyer
- **buyer_keys**: 2

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: ap@kamloops.ca
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.kamloops.ca/city-hall/procurement-services/accounts-payable
- **email_evidence_quote**: teer with ESS Level One ESS Volunteers Related Contacts Accounts Payable - General Inquiries 7 Victoria Street West V2C 1A2 ph 250-828-3423 ap@kamloops.ca Accounts Payable - numbered companies to D 7 Victoria Street West V2C 1A2 ph 250-828-3512
- **email_evidence_context**: nity Wildfire Resiliency Plan FireSmart Assessment & Rebate Programs Flooding Emergency Support Services Volunteer with ESS Level One ESS Volunteers Related Contacts Accounts Payable - General Inquiries 7 Victoria Street West V2C 1A2 ph 250-828-3423 ap@kamloops.ca Accounts Payable - numbered companies to D 7 Victoria Street West V2C 1A2 ph 250-828-3512 ap@kamloops.ca Accounts Payable - companies E - Lomas 7 Victoria Street West V2C 1A2 ph 250-828-3426 ap@kamloops.ca Accounts Payable - companies Lordco - Z 7 V (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: ap@kamloops.ca (invoicing/AP) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08 | page: https://www.kamloops.ca/city-hall/procurement-services/accounts-payable | quote: "teer with ESS Level One ESS Volunteers Related Contacts Accounts Payable - General Inquiries 7 Victoria Street West V2C 1A2 ph 250-828-3423 ap@kamloops.ca Accou" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00041
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject; pct=100; rua=mailto:IT-NETOPS-Infrastructure-UnionStaff@kamloops.ca; ruf=mailto:IT-NETOPS-Infrastructure-UnionStaff@kamloops.ca
- **dmarc_record_domain**: kamloops.ca
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 ip4:198.162.157.0/24 include:spf.dynect.net include:servers.mcsv.net include:spf.protection.outlook.com a:smtp-ms-pv01.kamloops.ca a:smtp-ms-pv02.kamloops.ca include:sendgrid.net -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: yes (v=TLSRPTv1; rua=mailto:networksupport@kamloops.ca)
- **bimi**: no BIMI record
- **ap_contact_name_as_published**: Victoria Street West (as printed by the organisation next to its invoicing mailbox)
- **ap_phone**: 250-828-3423 (as printed on https://www.kamloops.ca/city-hall/procurement-services/accounts-payable, re-read 2026-11-08)
- **payment_terms_as_published**: terms are net 30 (as printed on https://www.kamloops.ca/city-hall/procurement-services/accounts-payable, re-read 2026-11-08)
- **po_required_as_published**: yes (as published: quote the first and last name of the employee who requested goods or services Purchase Order Number) (as printed on https://www.kamloops.ca/city-hall/procurement-services/accounts-payable, re-read 2026-11-08)
- **invoice_portal_url**: Bonfire
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **ap_system_hint**: named on the buyer's page: Bonfire (as printed on https://www.kamloops.ca/sites/default/files/2023-07/City%20of%20Kamloops_2022%20SOFI%20Attachment%20A.pdf, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "payment_terms": "terms are net 30 (as printed on https://www.kamloops.ca/city-hall/procurement-services/accounts-payable, re-read 2026-11-08)", "po_required": "yes (as published: quote the first and last name of the employee who requested goods or services Purchase Order Number) (as printed on https://www.kamloops.ca/city-hall/procurement-services/accounts-payable, re-read 2026-11-08)", "portal_url": "Bonfire", "portal_kind": "actionable supplier / invoice portal named by the buyer", "ap_phone": "250-828-3423 (as printed on https://www.kamloops.ca/city-hall/procurement-services/accounts-payable, re-read 2026-11-08)"}
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: City of Kamloops — 7 Victoria Street West, Kamloops BC V2C 1A2 ⏎ SUBMIT TO: ap@kamloops.ca (invoicing/AP mailbox, confirmed by the referee) | tender portal (not an invoice channel): Bonfire ⏎ REFERENCE: contract 344842 (tender_no) — the source publishes the award under this tender / notice number and no separate contract number; tender 344842 (tender_no) | PO rule: yes (as published: quote the first and last name of the employee who requested goods or services Purchase Order Number) ⏎ FROM / REMIT TO: BDO Canada Limited — 20 Wellington Street East , Ontario, ON, M5E 1C5, Canada | GST/HST 101518124RT0001 (account derived from the BN9) | NEQ 3342011858 ⏎ TAX: Tax Exemptions Property Tax Estimator Property Tax Sale Frequently Asked Questions Capital Projects Transportatio (as printed on https://www.kamloops.ca/city-ha | CURRENCY: CAD (derived from the source's government) | TERMS: terms are net 30 (as printed on https://www.kamloops.ca/city-hall/procurement-services/accounts-paya ⏎ DESCRIPTION: City of Kamloops (municipality / local government, BC) — public contract / purchase award in the last 12 months (dated record): BDO Canada L | AMOUNT: 17265535.0 (source field: amount) CAD
- **invoice_card_json**: {"bill_to": {"legal_name": "City of Kamloops", "legal_name_is_published": true, "address": "7 Victoria Street West, Kamloops BC V2C 1A2", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "ap@kamloops.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "Bonfire", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: Bonfire (as printed on https://www.kamloops.ca/sites/default/files/2023-07/City%20of%20Kamloops_2022%20SOFI%20Attachment%20A.pdf, re-read 2026-11-08)", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "tender portal (not an invoice channel)"}, "references_required": {"po_required": "yes (as published: quote the first and last name of the employee who requested goods or services Purchase Order Number) (as printed on https://www.kamloops.ca/city-hall/procurement-services/accounts-payable, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "344842 (tender_no) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: 344842 (tender_no) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference — source ca_bc_ministry_awards"},
- **invoice_readiness**: 11/11 invoice elements present
- **ap_grade**: A
- **ap_score**: 85
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; AP phone or AP contact | missing: finance mailbox; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: contract or agreement number: 344842 (tender_no) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference — source ca_bc_ministry_awards

## Vendor
- **vendor**: BDO Canada LLP
- **vendor_legal_name**: BDO Canada Limited
- **vendor_trading_name**: BDO Canada LLP
- **vendor_registry_id**: Corporations Canada (corporation number): 235661
- **vendor_registry_url**: https://ised-isde.canada.ca/cc/lgcy/fdrlCrpDtls.html?corpId=235661
- **vendor_registered_address**: 20 Wellington Street East, Suite 500, Toronto, ON, M5E 1C5, CA
- **vendor_neq**: 3342011858 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_legal_form**: Société non constituée au Québec
- **vendor_activity_code**: CAE 7731 — SOCIÉTÉ DE COMPTABLES
- **vendor_employees_quebec**: De 100 à 249
- **vendor_establishments_quebec**: BDO CANADA S.R.L./S.E.N.C.R.L.: 200-1000 rue De La Gauchetière O, Montréal (Québec), H3B4W5; BDO CANADA S.R.L./S.E.N.C.R.L.: 805-1100 boul. Crémazie E, Montréal (Québec), H2P2X2; BDO CANADA S.R.L./S.E.N.C.R.L.: 650-2875 Boulevard Laurier, Québec (Québec), G1V2M2
- **vendor_directors_range**: 3 to 20 directors (Corporations Canada)
- **vendor_last_annual_filing**: REQ annual declaration 2026; Corporations Canada anniversary 1977-09-29
- **vendor_address**: 20 Wellington Street East , Ontario, ON, M5E 1C5, Canada
- **vendor_country_basis**: auditor of record (own audited financial statements, auditor's report signed in Kamloops, British Columbia)=es in internal control that we identify during our audit. | Tel: 250 372 9505 | BDO Canada LLP | Fax: 250 374 6323 | 300-275 Lansdowne ... ountants | Kamloops, British Columbia April 15, 2026
- **vendor_bn9**: 101518124
- **vendor_gst_hst_derived**: 101518124RT0001
- **vendor_website**: https://ontruck.org/
- **vendor_phone**: 416-249-7401
- **vendor_contact_evidence_url**: https://ontruck.org/contact/
- **vendor_logo_url**: https://ontruck.org/wp-content/uploads/Ontario_Trucking_Association_Logo.svg
- **vendor_website_basis**: found by a web search, confirmed by reading the site on 2026-11-08: https://ontruck.org/supplier-listing/bdo-canada-llp/ (BDO Canada LLP – Ontario Trucking Association Skip to content Cart Login Join OTA Join OTA 100 Years 100 Years About About Us Board & Committees Community Partn)
- **vendor_facts_provenance**: name and address: the record's vendor block (auditor of record (own audited financial statements, auditor's report signed in Kamloops, ); registry identity: Corporations Canada (corporation number): 235661 status Corporations Canada (corporation number): Active; Québec REQ (NEQ): Immatriculée (1995-01-19) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; strong); BN9: bc_orgbook BC1271832 (strong match); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 1992-05-26; phone / role e-mails / logo: the vendor's own site, https://ontruck.org/contact/ (tools/org_contacts.py, org_extras.py); website: https://ontruck.org/; NEQ: 3342011858 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_concentration_top_share**: Valley Traffic Services Inc.: 40% of 5 records
- **vendor_registry_status**: Corporations Canada (corporation number): Active; Québec REQ (NEQ): Immatriculée (1995-01-19)
- **vendor_registry_match_level**: strong
- **vendor_incorporation_date**: 1992-05-26
- **vendor_years_in_business**: 34.5 (since 1992-05-26, registry date)
- **vendor_bn_source**: bc_orgbook BC1271832 (strong match)

## Contract
- **po_required_as_published**: yes (as published: quote the first and last name of the employee who requested goods or services Purchase Order Number) (as printed on https://www.kamloops.ca/city-hall/procurement-services/accounts-payable, re-read 2026-11-08)
- **contract_status**: likely active (record dated in the last 12 months: auditor of record (own audited financial statements, auditor's report signed in Kamloops, )
- **contract_or_agreement_number**: 344842 (tender_no) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference
- **solicitation_or_tender_number**: 344842 (tender_no)
- **award_or_notice_id**: 5a23f279-099c-4060-b7ce-207826ccc7ca (bc_data_catalogue_resource_id)
- **contract_value**: 17265535.0 (source field: amount)
- **currency**: CAD (derived from the source's government)
- **award_date**: 2026-04-15
- **contract_link**: https://www.kamloops.ca/sites/default/files/2025%20Financial%20Statements%20-%20City%20of%20Kamloops.pdf
- **source**: auditor of record (own audited financial statements, auditor's report signed in Kamloops, 
- **contracts_with_canadian_suppliers**: 4
- **records_last_12_months**: 0
- **record_sources**: Ministry Contract Awards - Province of British Columbia (BC Bid contract award summaries) (5)
- **records_with_this_vendor**: 1
- **records_in_contract_dataset**: 4 records with Canada-located vendors (this row's organisation)

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Note: A municipality is not a government for purposes of the GST/HST"); charge GST/HST; derived from buyer type, not published by the buyer
- **tax_rate_indicative_derived**: GST 5% (BC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **vendor_gst_hst_derived**: 101518124RT0001

## Pay on sight / grades
- **pay_on_sight**: yes
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: City of Kamloops — 7 Victoria Street West, Kamloops BC V2C 1A2 ⏎ SUBMIT TO: ap@kamloops.ca (invoicing/AP mailbox, confirmed by the referee) | tender portal (not an invoice channel): Bonfire ⏎ REFERENCE: contract 344842 (tender_no) — the source publishes the award under this tender / notice number and no separate contract number; tender 344842 (tender_no) | PO rule: yes (as published: quote the first and last name of the employee who requested goods or services Purchase Order Number) ⏎ FROM / REMIT TO: BDO Canada Limited — 20 Wellington Street East , Ontario, ON, M5E 1C5, Canada | GST/HST 101518124RT0001 (account derived from the BN9) | NEQ 3342011858 ⏎ TAX: Tax Exemptions Property Tax Estimator Property Tax Sale Frequently Asked Questions Capital Projects Transportatio (as printed on https://www.kamloops.ca/city-ha | CURRENCY: CAD (derived from the source's government) | TERMS: terms are net 30 (as printed on https://www.kamloops.ca/city-hall/procurement-services/accounts-paya ⏎ DESCRIPTION: City of Kamloops (municipality / local government, BC) — public contract / purchase award in the last 12 months (dated record): BDO Canada L | AMOUNT: 17265535.0 (source field: amount) CAD
- **invoice_card_json**: {"bill_to": {"legal_name": "City of Kamloops", "legal_name_is_published": true, "address": "7 Victoria Street West, Kamloops BC V2C 1A2", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "ap@kamloops.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "Bonfire", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: Bonfire (as printed on https://www.kamloops.ca/sites/default/files/2023-07/City%20of%20Kamloops_2022%20SOFI%20Attachment%20A.pdf, re-read 2026-11-08)", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "tender portal (not an invoice channel)"}, "references_required": {"po_required": "yes (as published: quote the first and last name of the employee who requested goods or services Purchase Order Number) (as printed on https://www.kamloops.ca/city-hall/procurement-services/accounts-payable, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "344842 (tender_no) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: 344842 (tender_no) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference — source ca_bc_ministry_awards"},
- **invoice_readiness**: 11/11 invoice elements present
- **ap_grade**: A
- **ap_score**: 85
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; AP phone or AP contact | missing: finance mailbox; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **facts_provenance_json**: {"mailbox": ["ap@kamloops.ca (invoicing/AP)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08", "page: https://www.kamloops.ca/city-hall/procurement-services/accounts-payable", "quote: \"teer with ESS Level One ESS Volunteers Related Contacts Accounts Payable - General Inquiries 7 Victoria Street West V2C 1A2 ph 250-828-3423 ap@kamloops.ca Accou\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00041"], "buyer_facts": ["address and phone: the buyer's own site, https://www.kamloops.ca/city-hall/contact-us (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.kamloops.ca/city-hall/procurement-services/accounts-payable | 2026-11-08 | ok | terms are net 30 | yes (as published: quote the first and last name of the employee who requested goods or services Purchase Order Number) |  | 250-828-3423 |  |  |  | by the municipality. Accounts Payable also ensures that the municipality adheres to corporate financial policies. City of Kamloops standard terms are net 30 days from date of a valid and accurate invoice. Cheques are run | City (on or after the date of shipment or service completion) and invoice number Contact Name - quote the first and last name of the employee who requested goods or services Purchase Order Number (PO#) - purchase order n |

## Buyer site facts (org_extras, kamloops.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: City of Kamloops
- **legal_name_url**: https://www.kamloops.ca/
- **legal_name_quote**: City of Kamloops Skip to main content Skip to main menu Skip to footer close Close City of Kamloops Main navigation
- **logo_url**: https://www.kamloops.ca/sites/default/files/kamloops-logo-home.png
- **logo_basis**: logo image on the site
- **domain**: kamloops.ca
- **key**: b:203ef6db95431178
- **name**: City of Kamloops
- **website**: https://kamloops.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: City of Kamloops
- **legal_name_stated_url**: https://www.kamloops.ca/our-community/about-kamloops
- **legal_name_stated_quote**: About Kamloops | City of Kamloops Skip to main content Skip to main menu Skip to footer City of Kamloops Main navigation Our Communit
- **mentions**: {'payment_method': {'text': 'Interactive Maps & Apps schedule Recreation Facility Hours & Rates dvr Program Registra', 'url': 'https://www.kamloops.ca/', 'quote': "s Search visibility Report an Issue credit_card Online Payments account_balance City Council public Interactive Maps & Apps schedule Recreation Facility Hours & Rates dvr Program Registration question_answer Let's Talk Kamloops perm_identity Career Opportuniti"}, 'tax_exempt': {'text': 'Tax Exemptions Property Tax Estimator Property Tax Sale Frequently Asked Questions Capital Pr', 'url': 'https://www.kamloops.ca/', 'quote': 'ty Info
- **linkedin_url**: https://ca.linkedin.com/company/city-of-kamloops

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "7 Victoria Street West, Kamloops BC V2C 1A2", "address_country": "CA", "address_url": "https://www.kamloops.ca/city-hall/contact-us", "address_method": "pattern", "address_quote": "ESS Level One ESS Volunteers Related Contacts City Hall 7 Victoria Street West V2C 1A2 ph 250-828-3311 info@kamloops.ca Related Pages Related Pages Related Links Rela", "emails": "info@kamloops.ca", "emails_url": "https://www.kamloops.ca/city-hall/contact-us", "domain": "kamloops.ca", "key": "vd:kamloops.ca", "name": "Kamloops", "website": "https://kamloops.ca/", "kind": "vendor", "date": "2026-11-03"}

## Vendor site facts (org_extras, ontruck.org)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: Ontario Trucking Association
- **legal_name_url**: https://ontruck.org/
- **legal_name_quote**: Ontario Trucking Association Skip to content Cart Login Join OTA Join OTA 100 Years 100 Years About About Us Board & Committees
- **logo_url**: https://ontruck.org/wp-content/uploads/Ontario_Trucking_Association_Logo.svg
- **logo_basis**: logo image in the site header
- **domain**: ontruck.org
- **key**: vendor:BDO Canada LLP
- **name**: BDO Canada LLP
- **website**: https://ontruck.org/
- **kind**: vendor
- **date**: 2026-11-09
- **v**: 2
- **linkedin_url**: https://www.linkedin.com/company/ontario-trucking-association/
- **tel_links**: 4162497401
- **tel_links_url**: https://ontruck.org/

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "555 Dixon Road, Toronto, ON M9W 1H8", "address_country": "CA", "address_url": "https://ontruck.org/contact/", "address_method": "pattern", "address_quote": "ucation Message CAPTCHA Reach Out Δ Where to Find Us 555 Dixon Road Toronto, ON M9W 1H8 8:30am to 5:00pm Monday to Friday How to Get in Touch Telephone: 416-249-7401 F", "phone": "416-249-7401", "phone_url": "https://ontruck.org/contact/", "domain": "ontruck.org", "key": "lead:b5d6e2f78488205e", "name": "ontruck.org", "website": "https://ontruck.org/", "kind": "buyer", "date": "2026-11-04"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | City of Kamloops | Q473209 | official website on the organisation's domain (https://kamloops.ca) + name |  | Kamloops | Kamloops | city in British Columbia |  | Canada | 1811-00-00 |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "b:203ef6db95431178",
 "ap_contact_team": {
  "emails": [
   "ap@kamloops.ca",
   "purchasing@kamloops.ca",
   "procurement@kamloops.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "ap@kamloops.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.kamloops.ca/city-hall/procurement-services/accounts-payable",
    "quote": "teer with ESS Level One ESS Volunteers Related Contacts Accounts Payable - General Inquiries 7 Victoria Street West V2C 1A2 ph 250-828-3423 ap@kamloops.ca Accounts Payable - numbered companies to D 7 Victoria Street West V2C 1A2 ph 250-828-3512 ap@kamloops.ca Accounts Payable - companies E",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_deep01.csv",
    "org": "City of Kamloops",
    "task_id": "CL-DP-02112"
   },
   {
    "email": "ap@kamloops.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.kamloops.ca/city-hall/procurement-services/accounts-payable",
    "quote": "teer with ESS Level One ESS Volunteers Related Contacts Accounts Payable - General Inquiries 7 Victoria Street West V2C 1A2 ph 250-828-3423 ap@kamloops.ca Accounts Payable - numbered companies to D 7 Victoria Street West V2C 1A2 ph 250-828-3512",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "City of Kamloops",
    "task_id": "CL-WS-00041"
   },
   {
    "email": "purchasing@kamloops.ca",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.kamloops.ca/city-hall/procurement-services/covid-19-vaccination-supplier-declaration",
    "quote": "supplier has proof of an approved accommodation the supplier is required to notify the City’s Procurement and Inventory Control Manager at purchasing@kamloops.ca and include the following: the number of such personnel the impacted work locations the steps the contractor proposes to undert",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_deep01.csv",
    "org": "City of Kamloops",
    "task_id": "CL-DP-02112"
   },
   {
    "email": "purchasing@kamloops.ca",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.kamloops.ca/city-hall/procurement-services/bid-tender-opportunities",
    "quote": "u will be able to continue your vendor profile. If you encounter difficulties, use this Bonfire Guide to set up an account or you can email purchasing@kamloops.ca . How do I create a submission to Bonfire? Log into your Bonfire Vendor account in order to access the opportunity and begin pr",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "City of Kamloops",
    "task_id": "CL-WS-00352"
   },
   {
    "email": "procurement@kamloops.ca",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.kamloops.ca/city-hall/procurement-services/bid-tender-opportunities",
    "quote": "ergency Support Services Volunteer with ESS Level One ESS Volunteers Related Contacts Procurement 955 Concordia Way V2C 6V3 ph 250-828-3834 procurement@kamloops.ca Related Pages Related Pages Related Links Related Links Related Documents Related Documents Related News Related News Share pa",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "City of Kamloops",
    "task_id": "CL-WS-00352"
   }
  ]
 },
 "research_status": {
  "found": 5
 },
 "queries_tried": [
  "Wayback Machine URL index of kamloops.ca (addresses about invoices / suppliers / finance), then 15 live pages read (robots.txt respected), no AI, no search engine",
  "Wayback Machine URL index of kamloops.ca (addresses about invoices / suppliers / finance), then 15 live pages read (robots.txt respected), no AI, no search engine",
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

## The buyer's other Canadian-vendor records (first 60 of 5)
| record_id | vendor | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_bc_ministry_awards:b5c942db108a3216 | Pacific Flow Control Ltd. | RFP Watermain Hot Tapping Services |  |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/5a23f279-099c-4060-b7ce-207826ccc7ca/download/ministry-contract-awards-jul-sep-2022.csv |
| ca_bc_ministry_awards:3c16a663e8a02e20 | Arrow Transportation Systems | RFP Materials Management for Biosolids and/or Organics |  |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/5a23f279-099c-4060-b7ce-207826ccc7ca/download/ministry-contract-awards-jul-sep-2022.csv |
| ca_bc_ministry_awards:57cc55886f4cad96 | Valley Traffic Services Inc. | RFQ Traffic Signs, Supplies and Materials |  |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/5a23f279-099c-4060-b7ce-207826ccc7ca/download/ministry-contract-awards-jul-sep-2022.csv |
| ca_bc_ministry_awards:e46a5af853409929 | Valley Traffic Services Inc. | RFQ Sign Posts, Mounts and Hardware |  |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/5a23f279-099c-4060-b7ce-207826ccc7ca/download/ministry-contract-awards-jul-sep-2022.csv |
| ca_bc_ministry_awards:aff599e7f7bda53d | Stantec Consulting Ltd. | Structural Engineering - Bridges and Structures |  |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/5a23f279-099c-4060-b7ce-207826ccc7ca/download/ministry-contract-awards-jul-sep-2022.csv |

## The vendor's other buyers in the dataset (first 60 of 112)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_alberta_apc:AB-2026-01336:9e1e6f08-db22-4bff-b52f-27297b48ba28 | Auditor General | Auditor General - Request for Proposal - Workers' Compensation Board (WCB) – Alberta Financial Statements Audit RFP | 1360501.0 |  |  | https://purchasing.alberta.ca/posting/AB-2026-01336 |
| ca_alberta_apc:AB-2026-02965:c8e04629-60b1-44f0-ace7-418f01bd89ff | Municipality of Jasper | Municipality of Jasper - Request for Proposal - Business Continuity Plan - Municipality of Jasper  | 51000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2026-02965 |
| ca_bc_ministry_awards:bb603932d7ebad3c | Ministry of Forests, Lands, Natural Resource Operations and R.D. | Team Facilitation and Development | 15000.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:c92be5af81a6120a | Ministry of Transportation and Infrastructure | BC Bid Procurement Application and Change Management Specialist | 150000.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/576417ba-791e-4727-8f74-f7f6955a5190/download/ministry-contract-awards-oct-to-dec-2020.csv |
| ca_biddingo:41124428:41001035 | Atlantic Lottery Corporation | AML Program Assessment Services / |  |  |  | https://api.biddingo.com/restapi/bidding/noauthorize/1/11003564/41124428 |
| ca_biddingo:40109628:41001035 | Skilled Trades Ontario | STO_Surveys_112024 RFP |  |  |  | https://api.biddingo.com/restapi/bidding/noauthorize/1/41160807/40109628 |
| ca_biddingo:37725228:41001035 | Town of Collingwood | Consulting Service for the Development of an HR Master Plan |  |  |  | https://api.biddingo.com/restapi/bidding/noauthorize/1/11003111/37725228 |
| ca_biddingo:37112928:41001035 | Atlantic Lottery Corporation | Fraud Risk Management Consultancy Services /  Services de conseil en gestion des risques de fraude | 312.0 |  |  | https://api.biddingo.com/restapi/bidding/noauthorize/1/11003564/37112928 |
| ca_bidsandtenders:b8786671-9491-4ac5-bd3c-4cb7b02c7e9b:1 | City of Thorold | Diversity, Equity, and Inclusion (DEI) Current State Assessment and Action Plan | 72500.0 |  |  | https://thorold.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/b8786671-9491-4ac5-bd3c-4cb7b02c7e9b |
| ca_bidsandtenders:9ae20fa0-e0bb-4050-b364-43b8c3973065:1 | Region of Peel | BUSINESS CONTINUITY PLANNING AND BUSINESS IMPACT ANALYSIS FUNDAMENTALS TRAINING AT THE REGION OF PEEL | 36000.0 |  |  | https://peelregion.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/9ae20fa0-e0bb-4050-b364-43b8c3973065 |
| ca_bidsandtenders:a6752ede-b992-4487-9bf6-6c0f95883c16:1 | City of Brampton | IT Service Continuity and Incident Response Audit | 45000.0 |  |  | https://brampton.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/a6752ede-b992-4487-9bf6-6c0f95883c16 |
| ca_bidsandtenders:7a10f930-e1e8-4661-9450-9c7dce5efdbc:1 | City of Elliot Lake | AUDIT SERVICE |  |  |  | https://elliotlake.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/7a10f930-e1e8-4661-9450-9c7dce5efdbc |
| ca_bidsandtenders:d12c5059-5a43-4849-a055-0a0a85b1fe82:1 | Municipal Property Assessment Corporation | Audit and Tax Services |  |  |  | https://mpac.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/d12c5059-5a43-4849-a055-0a0a85b1fe82 |
| ca_bidsandtenders:c7215ee2-b912-4dd5-9e4b-212bb24346a3:1 | City of St. John's | Microsoft Dynamics GP, eOne, Mekorma and Paramount WorkPlace Software Maintenance Renewal | 310661.161 |  |  | https://stjohns.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/c7215ee2-b912-4dd5-9e4b-212bb24346a3 |
| ca_bidsandtenders:3c4e6a32-3e60-4415-9e09-53471dd3af5e:1 | Town of Oakville | Disaster Recovery Consulting Services | 2.0 |  |  | https://oakville.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/3c4e6a32-3e60-4415-9e09-53471dd3af5e |
| ca_bidsandtenders:8f1ff161-6cde-4f12-81c7-a73e5c40ec5f:1 | District of Lake Country | External Audit Services |  |  |  | https://lakecountry.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/8f1ff161-6cde-4f12-81c7-a73e5c40ec5f |
| ca_bidsandtenders:4af89106-1f27-4d5c-b855-a21d3162c599:1 | City of Belleville | Supply & Implementation of a Human Resource Information System (HRIS) | 1423423.95 |  |  | https://belleville.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/4af89106-1f27-4d5c-b855-a21d3162c599 |
| ca_bidsandtenders:85c64e8c-4293-49b0-b1cb-335131c57ccd:1 | Lake Simcoe Region Conservation Authority | External Audit Services |  |  |  | https://lsrca.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/85c64e8c-4293-49b0-b1cb-335131c57ccd |
| ca_bidsandtenders:92021c6f-1686-4918-b0e4-264db8de6858:33 | Halifax Regional Municipality | RFSQ Information Technology Consultants |  |  |  | https://halifax.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/92021c6f-1686-4918-b0e4-264db8de6858 |
| ca_bidsandtenders:9e7897bd-676c-4396-b214-14e6c159b78b:1 | District of Squamish | Financial Audit Services |  |  |  | https://squamish.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/9e7897bd-676c-4396-b214-14e6c159b78b |
| ca_bidsandtenders:51bd039c-d597-4c9f-b6ec-7247347eba4a:1 | City of Clarence-Rockland | EXTERNAL AUDIT SERVICES |  |  |  | https://clarence-rockland.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/51bd039c-d597-4c9f-b6ec-7247347eba4a |
| ca_bidsandtenders:344c9161-f0ef-433a-b5d6-b3b57466fcc4:2 | Halifax Regional Municipality | Real Estate Appraisal |  |  |  | https://halifax.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/344c9161-f0ef-433a-b5d6-b3b57466fcc4 |
| ca_bidsandtenders:be841614-b691-4b41-b48b-3960f1f2d867:1 | County of Dufferin | Audit Services |  |  |  | https://dufferincounty.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/be841614-b691-4b41-b48b-3960f1f2d867 |
| ca_bidsandtenders:0c6d57df-5ce0-46f7-a012-c973fed1ffdc:1 | City of Sarnia | Financial Audit Services |  |  |  | https://sarnia.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/0c6d57df-5ce0-46f7-a012-c973fed1ffdc |
| ca_bidsandtenders:c3006080-e948-48f7-a633-0b49974d1a39:4 | City of Vaughan | Vendor of Record for Citizen Relationship Management Consulting Services |  |  |  | https://vaughan.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/c3006080-e948-48f7-a633-0b49974d1a39 |
| ca_bidsandtenders:d2069568-cd8f-443a-8d30-e9ef77ec7036:1 | EfficiencyOne | Enterprise Financial System & Implementation Partner |  |  |  | https://efficiencyone.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/d2069568-cd8f-443a-8d30-e9ef77ec7036 |
| ca_bidsandtenders:64346d1f-705c-4fdc-b02a-be51ff538832:2 | City of Hamilton | Proposal for Develop, Integrate and Support Microsoft Power Platform Applications Services for Microsoft Power Platform |  |  |  | https://hamilton.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/64346d1f-705c-4fdc-b02a-be51ff538832 |
| ca_bidsandtenders:12c8049a-5166-4428-8455-77ed62488661:1 | City of Hamilton | Proposal for Design and Implementation of Customer Relationship and Knowledge Management Software using Microsoft Dynamics 365 and Power Platform |  |  |  | https://hamilton.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/12c8049a-5166-4428-8455-77ed62488661 |
| ca_bidsandtenders:e93574e7-0d80-49c7-99e2-cebb9f71a4f7:1 | City of Mount Pearl | Provision of Financial Audit Services | 254950.0 |  |  | https://mountpearl.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/e93574e7-0d80-49c7-99e2-cebb9f71a4f7 |
| ca_bidsandtenders:dea1a9ea-ae9b-4ed0-aec0-4c2d58e24432:3 | Newfoundland Labrador Hydro | Master Standing Offer - Regulatory, Accounting, and Treasury Support Services |  |  |  | https://nlhydro.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/dea1a9ea-ae9b-4ed0-aec0-4c2d58e24432 |
| ca_bidsandtenders:acc8f058-cdee-4854-b27f-3979a76142d7:1 | NT Power | RFP - Finance Management and ERP Solution |  |  |  | https://ntpower.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/acc8f058-cdee-4854-b27f-3979a76142d7 |
| ca_bidsandtenders:17398506-dfd9-4856-89a8-0e0f623c304f:1 | Norfolk County | Consulting Services for Norfolk County's People Plan |  |  |  | https://norfolk.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/17398506-dfd9-4856-89a8-0e0f623c304f |
| ca_bidsandtenders:45f7bfab-8f08-49ef-8baf-90b170754d82:6 | City of Brampton | To Establish a Roster of Vendors to Provide Professional and Auditing Services Specializing in Investigative and Forensic Services for a Four (4) Year Period |  |  |  | https://brampton.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/45f7bfab-8f08-49ef-8baf-90b170754d82 |
| ca_bidsandtenders:554ca9ea-a488-4402-b03b-4a9e2a04c48a:1 | City of St. John's | Audit Services | 870435.0 |  |  | https://stjohns.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/554ca9ea-a488-4402-b03b-4a9e2a04c48a |
| ca_bidsandtenders:0e583252-f82b-4450-b630-237982184210:2 | York Region | Request for Supplier Qualifications for Audit Services Consultants |  |  |  | https://york.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/0e583252-f82b-4450-b630-237982184210 |
| ca_bidsandtenders:afd541b0-a683-4bbc-b55c-223b9a6556c9:1 | City of St. John's | Microsoft Dynamics GP, eOne, Mekorma and Paramount Workplace Software Maintenance Renewal |  |  |  | https://bids.stjohns.ca/Module/Tenders/en/Tender/Detail/afd541b0-a683-4bbc-b55c-223b9a6556c9 |
| ca_bidsandtenders:0f3ce951-52a2-4370-8d71-4737f50e8a23:1 | Kawartha Conservation | Financial Statement Audit Services |  |  |  | https://kawarthaconservation.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/0f3ce951-52a2-4370-8d71-4737f50e8a23 |
| ca_bidsandtenders:4f6c516b-0230-4be3-8a1e-853df7beed91:1 | Simcoe Muskoka Catholic District School Board | External Audit Services | 269650.0 |  |  | https://smcdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/4f6c516b-0230-4be3-8a1e-853df7beed91 |
| ca_bidsandtenders:0d505939-171f-4f9b-b442-4ce7869f27f9:1 | City of Owen Sound | External Audit Services |  |  |  | https://owensound.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/0d505939-171f-4f9b-b442-4ce7869f27f9 |
| ca_bidsandtenders:1e796fd0-51ca-49d8-bfba-85c6ee719009:1 | Municipality of North Perth | External Audit Services |  |  |  | https://northperth.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/1e796fd0-51ca-49d8-bfba-85c6ee719009 |
| ca_bidsandtenders:4d36ae47-5bd7-4154-9047-5756212e390c:1 | Grey Bruce Public Health | For External Audit Services |  |  |  | https://publichealthgreybruce.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/4d36ae47-5bd7-4154-9047-5756212e390c |
| ca_bidsandtenders:cfc8fb13-b0d9-4b30-b99f-c64be35eb1d4:1 | City of Mississauga | Election Campaign Financial Compliance Auditing Services | 104800.0 |  |  | https://mississauga.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/cfc8fb13-b0d9-4b30-b99f-c64be35eb1d4 |
| ca_bidsandtenders:4047d9f7-7351-4f11-b674-be5faac41fb3:1 | City of Thunder Bay | City of Thunder Bay Human Resources Strategy |  |  |  | https://thunderbay.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/4047d9f7-7351-4f11-b674-be5faac41fb3 |
| ca_bidsandtenders:d445ab59-1bce-4b26-b20d-15a5dab9f0e6:1 | Lakehead University | Financial Audit Services |  |  |  | https://lakeheadu.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/d445ab59-1bce-4b26-b20d-15a5dab9f0e6 |
| ca_bidsandtenders:14565bf9-d202-4127-8d00-d76fb1977f3c:2 | City of Lethbridge | IT Consulting Services |  |  |  | https://lethbridge.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/14565bf9-d202-4127-8d00-d76fb1977f3c |
| ca_bidsandtenders:28a9425d-caa1-4b2e-b47d-10d1d720c15c:1 | Town of Paradise | Audit Services |  |  |  | https://paradise.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/28a9425d-caa1-4b2e-b47d-10d1d720c15c |
| ca_bidsandtenders:5d0126c5-08c6-4f0c-9f5d-6618dc29da5c:1 | Regional District of Central Okanagan | External Audit Services |  |  |  | https://rdco.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/5d0126c5-08c6-4f0c-9f5d-6618dc29da5c |
| ca_bidsandtenders:004c98f3-9a07-45d8-8208-e1b6429b0a92:1 | City of West Kelowna | Financial Audit Service | 1.0 |  |  | https://westkelowna.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/004c98f3-9a07-45d8-8208-e1b6429b0a92 |
| ca_bidsandtenders:2b8e3289-e882-4f74-b8f6-016b84ed42ef:1 | City of Thunder Bay | External Audit Services |  |  |  | https://thunderbay.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/2b8e3289-e882-4f74-b8f6-016b84ed42ef |
| ca_bidsandtenders:d6afa05f-722f-4485-9b2f-e0a858b2d9fb:1 | Town of Caledon | Consulting Services to Develop an Equity, Diversity and Inclusion Framework | 57520.0 |  |  | https://caledon.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/d6afa05f-722f-4485-9b2f-e0a858b2d9fb |
| ca_bidsandtenders:8489aa15-b9ce-4d0f-872d-3182e4bf5fcd:1 | Hamilton-Wentworth Catholic District School Board | External Audit Services |  |  |  | https://hwcdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/8489aa15-b9ce-4d0f-872d-3182e4bf5fcd |
| ca_bidsandtenders:8489aa15-b9ce-4d0f-872d-3182e4bf5fcd:2 | Hamilton-Wentworth Catholic District School Board | External Audit Services |  |  |  | https://hwcdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/8489aa15-b9ce-4d0f-872d-3182e4bf5fcd |
| ca_merx:3894018704:1 | Office of the Chief Information Officer | Managed Security Services | 1.0 |  |  | https://www.merx.com/govnl/officeofthechiefinformationofficer/solicitations/Managed-Security-Services/0000318719?origin=0 |
| ca_merx:3130294697:1 | Farm Credit Canada (FCC) | Pre-qualification for Risk Optimization Consulting Services | 1.0 |  |  | https://www.merx.com/farmcreditcanadafcc/solicitations/Pre-qualification-for-Risk-Optimization-Consulting-Services/0000278816?origin=0 |
| ca_merx:3568234115:1 | Manitoba Public Insurance | Request for Proposal #3405 Managed Vulnerability Solution | 832471.0 |  |  | https://www.merx.com/mbgov/mpi/solicitations/Request-for-Proposal-3405-Managed-Vulnerability-Solution/0000300844?origin=0 |
| ca_merx:3616879403:1 | CreateTO (Build Toronto, TPLC) | AI Strategy and Roadmap |  |  |  | https://www.merx.com/buildtorontotplc/solicitations/AI-Strategy-and-Roadmap/0000303942?origin=0 |
| ca_merx:3420908405:1 | City of Ottawa | FCS/BSS/Service Excellence Services |  |  |  | https://www.merx.com/cityofottawa/buyer-6700/solicitations/FCS-BSS-Service-Excellence-Services/0000292093?origin=0 |
| ca_merx:3264227602:1 | City of Ottawa | AG/ Audit and Support Services and Forensic and Investigative Services |  |  |  | https://www.merx.com/cityofottawa/buyer-6700/solicitations/AG-Audit-and-Support-Services-and-Forensic-and-Investigative-Services/0000283877?origin=0 |
| ca_merx:3205143352:1 | Atomic Energy of Canada Ltd. | AECL RFP 20241101 - Internal Audit Services | 2000000.0 |  |  | https://www.merx.com/aecl/solicitations/AECL-RFP-20241101-Internal-Audit-Services/0000281354?origin=0 |
| ca_merx:2588592321:1 | Infrastructure Ontario | RFP For External Auditor Services |  |  |  | https://www.merx.com/infrastructureontario/solicitations/RFP-For-External-Auditor-Services/0000254656?origin=0 |
| … 52 more rows in the .json | ||||||

## Open questions for hand research (layer 2)

- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

Read 2026-11-09 (Claude, integrator lane).

**The relationship in the buyer's own statements.** "City of Kamloops" financial statements "For the year ended December 31, 2025", independent
auditor's report on BDO letterhead ("BDO Canada LLP"), signed "Chartered Professional Accountants", "Kamloops, British Columbia", "April 15, 2026" —
https://www.kamloops.ca/sites/default/files/2025%20Financial%20Statements%20-%20City%20of%20Kamloops.pdf. Note 1: "The City of Kamloops (the "City") was
incorporated in 1893." — the statements use "City of Kamloops", not "The Corporation of the City of Kamloops": bill to "City of Kamloops". Note 20:
"accounts payable maturities are all within the next fiscal year" (no vendor payment terms in the notes).
**Reference.** Tender 344842 (bids&tenders, row) is the audit-services award; the auditor's report date (April 15, 2026) dates the latest deliverable.
A June 2026 external audit of the City's procurement found the system "sound but modernization needed" (radionl.com 2026-06-02) — expect PO discipline.
