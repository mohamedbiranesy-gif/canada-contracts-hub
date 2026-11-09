# S5-03 — Town of Smithers ⇄ Doane Grant Thornton LLP

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 2 · AP grade B · missing: the vendor's GST/HST number (BN9)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Town of Smithers Footer — 1027 Aldous Street, PO Box 879, Smithers, BC V0J 2N0
SUBMIT TO: finance@smithers.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: yes (as published: quote the first and last name of the employee who requested goods or services Purchase Order Number)
FROM / REMIT TO: DOANE GRANT THORNTON LLP — 200 King Street West, Toronto, ON, M5H 3T4, Canada | GST/HST number not public | NEQ 3370676739
TAX: DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https: | CURRENCY: CAD (derived from the source's government) | TERMS: terms are net 30 (as printed on https://www.smithers.ca/node/363, re-read 2026-11-08)
DESCRIPTION: Town of Smithers (municipality / local government, jurisdiction not stated) — public contract / purchase award in the last 12 months (dated  | AMOUNT: 2508947.0 (source field: amount) CAD
```

## Relationship
- **rank_group**: B3
- **data_quality_score**: 82
- **ship_ready**: yes (finance mailbox, not AP)
- **sensitivity_flag**: no
- **evidence_age_days**: 6
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Town of Smithers (municipality / local government, jurisdiction not stated) — public contract / purchase award in the last 12 months (dated record): Doane Grant Thornton LLP | value: 2508947.0 (source field: amount) CAD (derived from the source's government) | awarded 2026-05-22 | published by: auditor of record (own audited financial statements, auditor's report signed in Smithers,  | record: https://www.smithers.ca/sites/default/files/2026-05/Town%20of%20Smithers%202025%20Financial%20Statements.pdf | vendor in Canada because: auditor of record (own audited financial statements, auditor's report signed in Smithers, Canada)=udit. | Smithers, Canada | Chartered Professional Accountants May 22, 2026 | Audit | Tax | Advisory | © Doane Grant Thornt | status rule: likely active (record dated in the last 12 months: auditor of record (own audited financial statements, auditor's report signed in Smithers, )
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: lead:6bc3d92fbd72d2ff
- **tier**: B
- **grade**: 3
- **records_with_this_vendor**: 1 (relationship record: auditor of record (own audited financial statements, auditor's report signed in Smithers, ; 0 in the contract dataset)

## Buyer
- **buyer**: Town of Smithers
- **buyer_website**: https://www.smithers.ca/
- **buyer_address**: 1027 Aldous Street, PO Box 879, Smithers, BC V0J 2N0
- **buyer_phone**: 250-847-1600
- **buyer_contact_evidence_url**: https://www.smithers.ca/contact-us
- **buyer_legal_name_as_published**: Town of Smithers Footer
- **buyer_logo_url**: https://www.smithers.ca/themes/custom/smithers/images/smithers-tagline-logo.png
- **buyer_website_status**: site answers
- **buyer_type**: municipality / local government
- **buyer_sector**: government: municipal
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.smithers.ca/contact-us (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Note: A municipality is not a government for purposes of the GST/HST"); charge GST/HST; derived from buyer type, not published by the buyer
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: finance@smithers.ca
- **email_type**: finance/accounting dept or supplier-payment office
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); finance mailbox
- **email_evidence_url**: https://www.smithers.ca/node/363
- **email_evidence_quote**: t the Election Office Career Opportunities Bylaws Our History Freedom of Information and Privacy Contact Us Finance Department 250-847-1600 finance@smithers.ca Accounts Payable Accounts Payable is a service of the Town's Financial Department and is responsible for paying all of the invoice
- **email_evidence_context**: tion Voter Information Candidate Information Working the Election Election Results Legislation & Bylaws Contact the Election Office Career Opportunities Bylaws Our History Freedom of Information and Privacy Contact Us Finance Department 250-847-1600 finance@smithers.ca Accounts Payable Accounts Payable is a service of the Town's Financial Department and is responsible for paying all of the invoices for goods and services purchased by the municipality. Accounts Payable also ensures that the municipality adheres to (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: finance@smithers.ca (finance/accounting dept or supplier-payment office) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-03 | page: https://www.smithers.ca/node/363 | quote: "t the Election Office Career Opportunities Bylaws Our History Freedom of Information and Privacy Contact Us Finance Department 250-847-1600 finance@smithers.ca " | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00032
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1; p=quarantine; pct=100; rua=mailto:itservices@rdffg.bc.ca,mailto:dmarc_agg@vali.email;
- **dmarc_record_domain**: smithers.ca
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 ip4:3.97.120.145 ip4:209.145.117.44 include:spfa.cpmails.com include:spf.protection.outlook.com -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_phone**: 250-847-1600 (as printed on https://www.smithers.ca/node/363, re-read 2026-11-08)
- **payment_terms_as_published**: terms are net 30 (as printed on https://www.smithers.ca/node/363, re-read 2026-11-08)
- **po_required_as_published**: yes (as published: quote the first and last name of the employee who requested goods or services Purchase Order Number) (as printed on https://www.smithers.ca/node/363, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "payment_terms": "terms are net 30 (as printed on https://www.smithers.ca/node/363, re-read 2026-11-08)", "po_required": "yes (as published: quote the first and last name of the employee who requested goods or services Purchase Order Number) (as printed on https://www.smithers.ca/node/363, re-read 2026-11-08)", "ap_phone": "250-847-1600 (as printed on https://www.smithers.ca/node/363, re-read 2026-11-08)"}
- **channel_tier**: 2
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Town of Smithers Footer — 1027 Aldous Street, PO Box 879, Smithers, BC V0J 2N0 ⏎ SUBMIT TO: finance@smithers.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: yes (as published: quote the first and last name of the employee who requested goods or services Purchase Order Number) ⏎ FROM / REMIT TO: DOANE GRANT THORNTON LLP — 200 King Street West, Toronto, ON, M5H 3T4, Canada | GST/HST number not public | NEQ 3370676739 ⏎ TAX: DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https: | CURRENCY: CAD (derived from the source's government) | TERMS: terms are net 30 (as printed on https://www.smithers.ca/node/363, re-read 2026-11-08) ⏎ DESCRIPTION: Town of Smithers (municipality / local government, jurisdiction not stated) — public contract / purchase award in the last 12 months (dated  | AMOUNT: 2508947.0 (source field: amount) CAD
- **invoice_card_json**: {"bill_to": {"legal_name": "Town of Smithers Footer", "legal_name_is_published": true, "address": "1027 Aldous Street, PO Box 879, Smithers, BC V0J 2N0", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "finance@smithers.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "yes (as published: quote the first and last name of the employee who requested goods or services Purchase Order Number) (as printed on https://www.smithers.ca/node/363, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: quote the first and last name of the employee who requested goods or services Purchase Order Number) (as printed on https://www.smithers.ca/node/363, re-read 2026-11-08))"}, "terms": {"payment_terms": "terms are net 30 (as printed on https://www.smithers.ca/node/363, re-read 2026-11-08)", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorand
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id); vendor GST/HST number
- **ap_grade**: B
- **ap_score**: 75
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; AP phone or AP contact | missing: invoicing / AP mailbox; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general)
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms published
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: quote the first and last name of the employee who requested goods or services Purchase Order Number) (as printed on https://www.smithers.ca/node/363, re-read 2026-11-08))

## Vendor
- **vendor**: Doane Grant Thornton LLP
- **vendor_legal_name**: DOANE GRANT THORNTON LLP
- **vendor_trading_name**: GRANT THORNTON, LLP; GRANT THORNTON, S.E.N.C.R.L. (other names in the registry)
- **vendor_registry_id**: Québec REQ (NEQ): 3370676739
- **vendor_registry_url**: https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises
- **vendor_registered_address**: 2000-200 ST King W, Toronto (Ontario), M5H3T4
- **vendor_neq**: 3370676739 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_legal_form**: Société non constituée au Québec
- **vendor_activity_code**: CAE 7731 — Certification et Fiscalité
- **vendor_employees_quebec**: Aucun
- **vendor_last_annual_filing**: REQ annual declaration 2026
- **vendor_address**: 200 King Street West, Toronto, ON, M5H 3T4, Canada
- **vendor_country_basis**: auditor of record (own audited financial statements, auditor's report signed in Smithers, Canada)=udit. | Smithers, Canada | Chartered Professional Accountants May 22, 2026 | Audit | Tax | Advisory | © Doane Grant Thornton LLP. A Canadi
- **vendor_website**: https://www.doanegrantthornton.ca/
- **vendor_phone**: +1 416 366 4240
- **vendor_contact_evidence_url**: https://www.doanegrantthornton.ca/contact-us/
- **vendor_logo_url**: https://www.doanegrantthornton.ca/dist/images/grantthornton_logo-57x57.png
- **vendor_website_basis**: found by a web search, confirmed by reading the site on 2026-11-08: https://www.doanegrantthornton.ca/ (Assurance, Tax & Accounting Firm Canada | Doane Grant Thornton LLP You are using an outdated browser. Please upgrade your browser to improve your experience. Sk)
- **vendor_facts_provenance**: name and address: the record's vendor block (auditor of record (own audited financial statements, auditor's report signed in Smithers, ); registry identity: Québec REQ (NEQ): 3370676739 status Québec REQ (NEQ): Immatriculée (2015-01-27) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); incorporated / registered: 1998-06-15; phone / role e-mails / logo: the vendor's own site, https://www.doanegrantthornton.ca/contact-us/ (tools/org_contacts.py, org_extras.py); website: https://www.doanegrantthornton.ca/; NEQ: 3370676739 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Québec REQ (NEQ): Immatriculée (2015-01-27)
- **vendor_incorporation_date**: 1998-06-15
- **vendor_years_in_business**: 28.4 (since 1998-06-15, registry date)

## Contract
- **po_required_as_published**: yes (as published: quote the first and last name of the employee who requested goods or services Purchase Order Number) (as printed on https://www.smithers.ca/node/363, re-read 2026-11-08)
- **contract_status**: likely active (record dated in the last 12 months: auditor of record (own audited financial statements, auditor's report signed in Smithers, )
- **contract_value**: 2508947.0 (source field: amount)
- **currency**: CAD (derived from the source's government)
- **award_date**: 2026-05-22
- **contract_link**: https://www.smithers.ca/sites/default/files/2026-05/Town%20of%20Smithers%202025%20Financial%20Statements.pdf
- **source**: auditor of record (own audited financial statements, auditor's report signed in Smithers, 
- **contracts_with_canadian_suppliers**: 4
- **records_with_this_vendor**: 1 (relationship record: auditor of record (own audited financial statements, auditor's report signed in Smithers, ; 0 in the contract dataset)
- **records_in_contract_dataset**: 4 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Note: A municipality is not a government for purposes of the GST/HST"); charge GST/HST; derived from buyer type, not published by the buyer
- **tax_rate_indicative_derived**: GST 5% (BC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Town of Smithers Footer — 1027 Aldous Street, PO Box 879, Smithers, BC V0J 2N0 ⏎ SUBMIT TO: finance@smithers.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: yes (as published: quote the first and last name of the employee who requested goods or services Purchase Order Number) ⏎ FROM / REMIT TO: DOANE GRANT THORNTON LLP — 200 King Street West, Toronto, ON, M5H 3T4, Canada | GST/HST number not public | NEQ 3370676739 ⏎ TAX: DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https: | CURRENCY: CAD (derived from the source's government) | TERMS: terms are net 30 (as printed on https://www.smithers.ca/node/363, re-read 2026-11-08) ⏎ DESCRIPTION: Town of Smithers (municipality / local government, jurisdiction not stated) — public contract / purchase award in the last 12 months (dated  | AMOUNT: 2508947.0 (source field: amount) CAD
- **invoice_card_json**: {"bill_to": {"legal_name": "Town of Smithers Footer", "legal_name_is_published": true, "address": "1027 Aldous Street, PO Box 879, Smithers, BC V0J 2N0", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "finance@smithers.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "yes (as published: quote the first and last name of the employee who requested goods or services Purchase Order Number) (as printed on https://www.smithers.ca/node/363, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: quote the first and last name of the employee who requested goods or services Purchase Order Number) (as printed on https://www.smithers.ca/node/363, re-read 2026-11-08))"}, "terms": {"payment_terms": "terms are net 30 (as printed on https://www.smithers.ca/node/363, re-read 2026-11-08)", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorand
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id); vendor GST/HST number
- **ap_grade**: B
- **ap_score**: 75
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; AP phone or AP contact | missing: invoicing / AP mailbox; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general)
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms published
- **facts_provenance_json**: {"mailbox": ["finance@smithers.ca (finance/accounting dept or supplier-payment office)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-03", "page: https://www.smithers.ca/node/363", "quote: \"t the Election Office Career Opportunities Bylaws Our History Freedom of Information and Privacy Contact Us Finance Department 250-847-1600 finance@smithers.ca \"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00032"], "buyer_facts": ["address and phone: the buyer's own site, https://www.smithers.ca/contact-us (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (auditor of record (own aud

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.smithers.ca/node/363 | 2026-11-08 | ok | terms are net 30 | yes (as published: quote the first and last name of the employee who requested goods or services Purchase Order Number) |  | 250-847-1600 |  |  |  | by the municipality. Accounts Payable also ensures that the municipality adheres to corporate financial policies. Town of Smithers standard terms are net 30 days from date of a valid and accurate invoice. Cheques are run | Town (on or after the date of shipment or service completion) and invoice number Contact Name - quote the first and last name of the employee who requested goods or services Purchase Order Number (PO#) - purchase order n |

## Buyer site facts (org_extras, smithers.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: Town of Smithers Footer menu
- **legal_name_url**: https://www.smithers.ca/
- **legal_name_quote**: ll Meetings 1027 Aldous Street, Box 879 Smithers, BC, V0J 2N0 Contact Us Join us on Facebook © 2026 Town of Smithers Footer menu Privacy Policy Website by Upanup
- **logo_url**: https://www.smithers.ca/themes/custom/smithers/images/smithers-tagline-logo.png
- **logo_basis**: logo image on the site
- **domain**: smithers.ca
- **key**: lead:6bc3d92fbd72d2ff
- **name**: Town of Smithers
- **website**: https://smithers.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Town of Smithers
- **legal_name_stated_url**: https://www.smithers.ca/about
- **legal_name_stated_quote**: About Smithers | Town of Smithers Skip to main content Skip to main menu Skip to footer Alerts Close Willowvale Walking Bridge Closur
- **tel_links**: 250-847-1600; 250-847-1649

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "1027 Aldous Street, PO Box 879, Smithers, BC V0J 2N0", "address_country": "CA", "address_url": "https://www.smithers.ca/contact-us", "address_method": "pattern", "address_quote": "of Information and Privacy Town Hall 1027 Aldous Street PO Box 879 Smithers, BC V0J 2N0 Phone: 250-847-1600 Fax: 250-847-1601 general@smithers.ca Hours of Operation Mo", "phone": "250-847-1600", "phone_url": "https://www.smithers.ca/contact-us", "emails": "general@smithers.ca", "emails_url": "https://www.smithers.ca/contact-us", "domain": "smithers.ca", "key": "lead:6bc3d92fbd72d2ff", "name": "Town of Smithers", "website": "https://smithers.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, doanegrantthornton.ca)
- **status**: ok
- **pages**: 6
- **v**: 2
- **legal_name_stated**: Grant Thornton International Ltd
- **legal_name_stated_url**: https://www.doanegrantthornton.ca/about-us/
- **legal_name_stated_quote**: ibility Cookie Preferences Follow us Follow us © 2026 Doane Grant Thornton LLP—A Canadian Member of Grant Thornton International Ltd. All rights reserved. "Grant Thornton” refers to the brand under which the Grant Thornton member fi
- **linkedin_url**: https://www.linkedin.com/company/doane-grant-thornton-llp/
- **language**: en
- **legal_name**: Doane Grant Thornton LLP—A Canadian Member of Grant Thornton International Ltd
- **legal_name_url**: https://www.doanegrantthornton.ca/
- **legal_name_quote**: Legal close Privacy Disclaimer Sitemap Accessibility Cookie Preferences Follow us Follow us © 2026 Doane Grant Thornton LLP—A Canadian Member of Grant Thornton International Ltd. All rights reserved. "Grant Thornton” refers to the brand under which the Grant Thornton member fi
- **logo_url**: https://www.doanegrantthornton.ca/dist/images/grantthornton_logo-57x57.png
- **logo_basis**: site icon (apple-touch-icon)
- **domain**: doanegrantthornton.ca
- **key**: vendor:Doane Grant Thornton LLP
- **name**: Doane Grant Thornton LLP
- **website**: https://doanegrantthornton.ca/
- **kind**: vendor
- **date**: 2026-11-08

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "200 King Street West, Toronto, ON M5H 3T4", "address_country": "CA", "address_url": "https://www.doanegrantthornton.ca/contact-us/", "address_method": "pattern", "address_quote": "l Address Doane Grant Thornton LLP 20th Floor, 200 King Street West Toronto, ON M5H 3T4 Our offices See our office locations across Canada Find my local office Follow", "phone": "+1 416 366 4240", "phone_url": "https://www.doanegrantthornton.ca/contact-us/", "domain": "doanegrantthornton.ca", "key": "vendor:Doane Grant Thornton LLP", "name": "Doane Grant Thornton LLP", "website": "https://doanegrantthornton.ca/", "kind": "vendor", "date": "2026-11-08"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Town of Smithers |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:6bc3d92fbd72d2ff",
 "ap_contact_team": {
  "emails": [
   "finance@smithers.ca",
   "general@smithers.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "finance@smithers.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.smithers.ca/node/363",
    "quote": "t the Election Office Career Opportunities Bylaws Our History Freedom of Information and Privacy Contact Us Finance Department 250-847-1600 finance@smithers.ca Accounts Payable Accounts Payable is a service of the Town's Financial Department and is responsible for paying all of the invoice",
    "retrieved_date": "2026-11-03",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Town of Smithers",
    "task_id": "CL-WS-00032"
   },
   {
    "email": "general@smithers.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.smithers.ca/contact-us",
    "quote": "story Freedom of Information and Privacy Town Hall 1027 Aldous Street PO Box 879 Smithers, BC V0J 2N0 Phone: 250-847-1600 Fax: 250-847-1601 general@smithers.ca Hours of Operation Monday to Friday 8:30am - 4:30pm Closed on Weekends & Stat Holidays Works & Operations 2888 19th Avenue PO Box",
    "retrieved_date": "2026-11-03",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Town of Smithers",
    "task_id": "CL-SM-00021"
   }
  ]
 },
 "research_status": {
  "found": 2
 },
 "queries_tried": [
  "site crawl of www.smithers.ca (40 pages, robots.txt respected), no AI, no search engine",
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

## The vendor's other buyers in the dataset (first 60 of 8)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_alberta_apc:AB-2025-03634:9359b000-c223-4471-9e91-c636cc8bd72b | Technology and Innovation | Technology and Innovation - Request for Proposal - SYSTEM AND ORGANIZATION CONTROLS (SOC) FOR SERVICE ORGANIZATIONS | 1.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-03634 |
| ca_bidsandtenders:8671d572-5ca2-4c65-82ad-64f2f8d68f3d:1 | Waterloo Catholic District School Board | External Auditing Services |  |  |  | https://wcdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/8671d572-5ca2-4c65-82ad-64f2f8d68f3d |
| ca_bidsandtenders:646f0b5c-5381-467a-8592-639fd4eee765:1 | City of Moncton / Ville de Moncton | Professional Consulting Services - Chart of Accounts | 142811.26 |  |  | https://moncton.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/646f0b5c-5381-467a-8592-639fd4eee765 |
| ca_bidsandtenders:ddf3a4f5-f9ce-477a-ae14-aab478beaab7:1 | City of Thorold | Audit Services for City of Thorold | 415400.0 |  |  | https://thorold.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/ddf3a4f5-f9ce-477a-ae14-aab478beaab7 |
| ca_bidsandtenders:ea3c0af2-ae5a-484a-ba74-06c69e17336b:1 | York Catholic District School Board | External Audit Services | 71500.0 |  |  | https://ycdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/ea3c0af2-ae5a-484a-ba74-06c69e17336b |
| ca_bidsandtenders:d6c09e57-e223-4a3f-99ab-ce4a00599903:1 | Dalhousie University | External Audit Services | 979600.0 |  |  | https://dal.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/d6c09e57-e223-4a3f-99ab-ce4a00599903 |
| ca_merx:2167726764:1 | Toronto Police Service | Financial Forensic accounting services |  |  |  | https://www.merx.com/torontopolice/solicitations/Financial-Forensic-accounting-services/0000221302?origin=0 |
| ca_merx:2295976914:1 | The City of Winnipeg | Water and Waste Department Cybersecurity Review | 63000.0 |  |  | https://www.merx.com/mbgov/cityofwinnipeg/solicitations/Water-and-Waste-Department-Cybersecurity-Review/0000232093?origin=0 |

## Open questions for hand research (layer 2)

- the vendor's GST/HST number (BN9)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
