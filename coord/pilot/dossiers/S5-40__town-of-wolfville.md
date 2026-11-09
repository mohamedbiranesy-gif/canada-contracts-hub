# S5-40 — Town of Wolfville ⇄ Doane Grant Thornton

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 2 · AP grade C · missing: the vendor's GST/HST number (BN9)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Town of Wolfville — NS, CA
SUBMIT TO: financeinfo@wolfville.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) | format: PDF format (as printed on https://wolfville.ca/sites/default/files/2024-08/Wolfville%20Tender%20Supplementary%20Specifications%2000%2074%2000.pdf, re-read 2026-11-08)
REFERENCE: contract WOL019-2025 (tender_id) — the source publishes the award under this tender / notice number and no separate contract number; tender WOL019-2025 (tender_id) | PO rule: not published
FROM / REMIT TO: DOANE GRANT THORNTON LLP — 200 King Street West, Toronto, ON, M5H 3T4, Canada | GST/HST number not public | NEQ 3370676739
TAX: Tax Exemption Property Tax Sale Tenders and Procurement Planning Notices Bylaws and Policies Financial Statements (as printed on https://wolfville.ca/town-hall/ | CURRENCY: CAD | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: External Audit Services | AMOUNT: 265,500.00 CAD
```

## Relationship
- **rank_group**: F3
- **data_quality_score**: 60
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Town of Wolfville (municipality / local government, NS) — older contract or payment (more than 36 months, or ended): Doane Grant Thornton | subject: External Audit Services | instrument: contract | contract number: WOL019-2025 (tender_id) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference | solicitation: WOL019-2025 (tender_id) | all identifiers: {"tender_id": "WOL019-2025"} | value: 265500.0 CAD | awarded 2026-01-27 | published by: Awarded Public Tenders (Nova Scotia open data, m6ps-8j6u) | record: https://data.novascotia.ca/resource/m6ps-8j6u.json?tender_id=WOL019-2025 | vendor in Canada because: registry match only (exact): quebec_req 3370676739 'DOANE GRANT THORNTON LLP', registered office 2000-200 ST King W, Toronto (Ontario), M5H3T4 (https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises); th | status rule: weaker relationship (within 5 years): contract awarded 2026-01-27; vendor located in Canada only through a business-registry match
- **how_relationship_was_found**: an older or ended record in the contract dataset (release tables)
- **keys**: b:014b5aa5afdd4fce
- **tier**: F
- **grade**: 3
- **records_with_this_vendor**: 1 (relationship record: Awarded Public Tenders (Nova Scotia open data, m6ps-8j6u); 0 in the contract dataset)

## Buyer
- **buyer**: Town of Wolfville
- **buyer_website**: https://wolfville.ca
- **buyer_address**: NS, CA
- **buyer_phone**: 902-542-5767
- **buyer_contact_evidence_url**: https://wolfville.ca/contact-wolfville
- **buyer_legal_name_as_published**: Town of Wolfville
- **buyer_logo_url**: https://wolfville.ca/themes/custom/wolfville/assets/img/brand/logo.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://ca.linkedin.com/company/town-of-wolfville
- **buyer_type**: municipality / local government
- **buyer_sector**: government: municipal
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://wolfville.ca/contact-wolfville (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; invoicing requirements: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_exempt_status**: Tax Exemption Property Tax Sale Tenders and Procurement Planning Notices Bylaws and Policies Financial Statements (as printed on https://wolfville.ca/town-hall/rates-and-finances/financial-statements, re-read 2026-11-08)
- **buyer_tax_status_derived**: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Note: A municipality is not a government for purposes of the GST/HST"); charge GST/HST; derived from buyer type, not published by the buyer
- **buyer_esignature_preference**: Docusign Envelope ID: 4B8B7E60-3237-4443-B047-8CF216C1AFC8 Docusign Envelope ID: 4B8B7E6 (as printed on https://wolfville.ca/sites/default/files/2024-11/Consolidated%20Financials%20-%20March%202024.pdf, re-read 2026-11-08)
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: financeinfo@wolfville.ca
- **email_type**: finance/accounting dept or supplier-payment office
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); finance mailbox
- **email_evidence_url**: https://wolfville.ca/town-hall/rates-and-finances/financial-statements
- **email_evidence_quote**: paragraph--view-mode--default"> <div class="widget-wrapper"> <div class="title"> <h5>Contact</h5> </div> <div class="body"> <a href="mailto:Financeinfo@wolfville.ca" class="field-email">Email</a> </div> </div> </div> </div></div></div> </div> </div> </div> </div> </main> </div> <div id="fo
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: financeinfo@wolfville.ca (finance/accounting dept or supplier-payment office) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://wolfville.ca/town-hall/rates-and-finances/financial-statements | quote: "paragraph--view-mode--default"> <div class="widget-wrapper"> <div class="title"> <h5>Contact</h5> </div> <div class="body"> <a href="mailto:Financeinfo@wolfvill" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: no DMARC record; SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CH-AP-00236
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: no DMARC record; SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: no DMARC record
- **dmarc_record**: no DMARC record at _dmarc.wolfville.ca; confirmed by 8.8.8.8
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 ip4:192.69.69.106 include:spf.protection.outlook.com -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements**: invoice format as published: PDF format (as printed on https://wolfville.ca/sites/default/files/2024-08/Wolfville%20Tender%20Supplementary%20Specifications%2000%2074%2000.pdf, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "invoice_format": "PDF format (as printed on https://wolfville.ca/sites/default/files/2024-08/Wolfville%20Tender%20Supplementary%20Specifications%2000%2074%2000.pdf, re-read 2026-11-08)", "requirements_text": "invoice format as published: PDF format (as printed on https://wolfville.ca/sites/default/files/2024-08/Wolfville%20Tender%20Supplementary%20Specifications%2000%2074%2000.pdf, re-read 2026-11-08)"}
- **channel_tier**: 2
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Town of Wolfville — NS, CA ⏎ SUBMIT TO: financeinfo@wolfville.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) | format: PDF format (as printed on https://wolfville.ca/sites/default/files/2024-08/Wolfville%20Tender%20Supplementary%20Specifications%2000%2074%2000.pdf, re-read 2026-11-08) ⏎ REFERENCE: contract WOL019-2025 (tender_id) — the source publishes the award under this tender / notice number and no separate contract number; tender WOL019-2025 (tender_id) | PO rule: not published ⏎ FROM / REMIT TO: DOANE GRANT THORNTON LLP — 200 King Street West, Toronto, ON, M5H 3T4, Canada | GST/HST number not public | NEQ 3370676739 ⏎ TAX: Tax Exemption Property Tax Sale Tenders and Procurement Planning Notices Bylaws and Policies Financial Statements (as printed on https://wolfville.ca/town-hall/ | CURRENCY: CAD | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: External Audit Services | AMOUNT: 265,500.00 CAD
- **invoice_card_json**: {"bill_to": {"legal_name": "Town of Wolfville", "legal_name_is_published": true, "address": "NS, CA", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "financeinfo@wolfville.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "PDF format (as printed on https://wolfville.ca/sites/default/files/2024-08/Wolfville%20Tender%20Supplementary%20Specifications%2000%2074%2000.pdf, re-read 2026-11-08)", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "WOL019-2025 (tender_id) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: WOL019-2025 (tender_id) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference — source ca_nova_scotia"}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": "Docusign Envelope ID: 4B8B7E60-3237-4443-B047-8CF216C1AFC8 Docusign Envelope ID: 4B8B7E6 (as printed on https://wolfville.ca/sites/default/files/2024-11/Consolidated%20Financials%20-%20March%202024.pdf, re-read 2026-11-08)"}, "tax"
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; payment terms; vendor GST/HST number
- **ap_grade**: C
- **ap_score**: 64
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; invoice format / requirements published | missing: invoicing / AP mailbox; PO rule published; payment terms published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms not published (buyer's default applies)
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: contract or agreement number: WOL019-2025 (tender_id) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference — source ca_nova_scotia

## Vendor
- **vendor**: Doane Grant Thornton
- **vendor_legal_name**: DOANE GRANT THORNTON LLP
- **vendor_trading_name**: Doane Grant Thornton
- **vendor_registry_id**: Québec REQ (NEQ): 3370676739
- **vendor_registry_url**: https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises
- **vendor_registered_address**: 2000-200 ST King W, Toronto (Ontario), M5H3T4
- **vendor_neq**: 3370676739 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_legal_form**: Société non constituée au Québec
- **vendor_activity_code**: CAE 7731 — Certification et Fiscalité
- **vendor_employees_quebec**: Aucun
- **vendor_last_annual_filing**: REQ annual declaration 2026
- **vendor_address**: 200 King Street West, Toronto, ON, M5H 3T4, Canada
- **vendor_country_basis**: registry match only (exact): quebec_req 3370676739 'DOANE GRANT THORNTON LLP', registered office 2000-200 ST King W, Toronto (Ontario), M5H3T4 (https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises); the source publishes no vendor country
- **vendor_facts_provenance**: name and address: the record's vendor block (Awarded Public Tenders (Nova Scotia open data, m6ps-8j6u)); registry identity: Québec REQ (NEQ): 3370676739 status Québec REQ (NEQ): Immatriculée (2015-01-27) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); incorporated / registered: 1998-06-15; NEQ: 3370676739 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Québec REQ (NEQ): Immatriculée (2015-01-27)
- **vendor_incorporation_date**: 1998-06-15
- **vendor_years_in_business**: 28.4 (since 1998-06-15, registry date)

## Contract
- **contract_status**: weaker relationship (within 5 years): contract awarded 2026-01-27; vendor located in Canada only through a business-registry match
- **contract_reference**: {"tender_id": "WOL019-2025"}
- **contract_title**: External Audit Services
- **contract_description**: External Audit Services
- **contract_or_agreement_number**: WOL019-2025 (tender_id) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference
- **solicitation_or_tender_number**: WOL019-2025 (tender_id)
- **award_or_notice_id**: WOL019-2025 (tender_id) — notice id; the award is published within this notice, the source assigns no separate award id
- **contract_value**: 265500.0
- **currency**: CAD
- **award_date**: 2026-01-27
- **contract_link**: https://data.novascotia.ca/resource/m6ps-8j6u.json?tender_id=WOL019-2025
- **source**: Awarded Public Tenders (Nova Scotia open data, m6ps-8j6u)
- **contracts_with_canadian_suppliers**: 4
- **records_with_this_vendor**: 1 (relationship record: Awarded Public Tenders (Nova Scotia open data, m6ps-8j6u); 0 in the contract dataset)
- **records_in_contract_dataset**: 4 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Note: A municipality is not a government for purposes of the GST/HST"); charge GST/HST; derived from buyer type, not published by the buyer
- **tax_rate_indicative_derived**: HST 15% (Nova Scotia) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Town of Wolfville — NS, CA ⏎ SUBMIT TO: financeinfo@wolfville.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) | format: PDF format (as printed on https://wolfville.ca/sites/default/files/2024-08/Wolfville%20Tender%20Supplementary%20Specifications%2000%2074%2000.pdf, re-read 2026-11-08) ⏎ REFERENCE: contract WOL019-2025 (tender_id) — the source publishes the award under this tender / notice number and no separate contract number; tender WOL019-2025 (tender_id) | PO rule: not published ⏎ FROM / REMIT TO: DOANE GRANT THORNTON LLP — 200 King Street West, Toronto, ON, M5H 3T4, Canada | GST/HST number not public | NEQ 3370676739 ⏎ TAX: Tax Exemption Property Tax Sale Tenders and Procurement Planning Notices Bylaws and Policies Financial Statements (as printed on https://wolfville.ca/town-hall/ | CURRENCY: CAD | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: External Audit Services | AMOUNT: 265,500.00 CAD
- **invoice_card_json**: {"bill_to": {"legal_name": "Town of Wolfville", "legal_name_is_published": true, "address": "NS, CA", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "financeinfo@wolfville.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "PDF format (as printed on https://wolfville.ca/sites/default/files/2024-08/Wolfville%20Tender%20Supplementary%20Specifications%2000%2074%2000.pdf, re-read 2026-11-08)", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "WOL019-2025 (tender_id) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: WOL019-2025 (tender_id) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference — source ca_nova_scotia"}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": "Docusign Envelope ID: 4B8B7E60-3237-4443-B047-8CF216C1AFC8 Docusign Envelope ID: 4B8B7E6 (as printed on https://wolfville.ca/sites/default/files/2024-11/Consolidated%20Financials%20-%20March%202024.pdf, re-read 2026-11-08)"}, "tax"
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; payment terms; vendor GST/HST number
- **ap_grade**: C
- **ap_score**: 64
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; invoice format / requirements published | missing: invoicing / AP mailbox; PO rule published; payment terms published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms not published (buyer's default applies)
- **facts_provenance_json**: {"mailbox": ["financeinfo@wolfville.ca (finance/accounting dept or supplier-payment office)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://wolfville.ca/town-hall/rates-and-finances/financial-statements", "quote: \"paragraph--view-mode--default\"> <div class=\"widget-wrapper\"> <div class=\"title\"> <h5>Contact</h5> </div> <div class=\"body\"> <a href=\"mailto:Financeinfo@wolfvill\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: no DMARC record; SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CH-AP-00236"], "buyer_facts": ["address and phone: the buyer's own site, https://wolfville.ca/contact-wolfville (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "invoicing requirements: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (Awarded Public Tenders (Nova Scotia open data, m6ps-8j6u))", "registry identity: Québec REQ (NEQ): 3370676739 status Québec REQ (NEQ): Immatriculée (2015-01-27) (scripts/enric

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://wolfville.ca/town-hall/rates-and-finances/financial-statements | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |
| https://wolfville.ca/sites/default/files/2025-06/2025_06_17%20Town%20Council%20Agenda%20Package%20for%20Public.pdf | 2026-11-08 | ok | 45 days following receipt |  |  | 902-245-4769 |  |  |  | Valley Regional Services Board of Directors in the same manner as approval of the annual budget and operating plan. (2) No later than 45 days following receipt of the recommendation from the General Manager, supplementar |  |

## Buyer site facts (org_extras, wolfville.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: Town of Wolfville
- **legal_name_url**: https://wolfville.ca/
- **legal_name_quote**: Town of Wolfville, Nova Scotia Skip to main content About Visit News Events Contact Town Menu Contact About Wolfville
- **logo_url**: https://wolfville.ca/themes/custom/wolfville/assets/img/brand/logo.png
- **logo_basis**: logo image in the site header
- **domain**: wolfville.ca
- **key**: b:014b5aa5afdd4fce
- **name**: Town of Wolfville
- **website**: https://wolfville.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Town of Wolfville
- **legal_name_stated_url**: https://wolfville.ca/about-wolfville
- **legal_name_stated_quote**: About Wolfville | Town of Wolfville, Nova Scotia Skip to main content About Visit News Events Contact Town Menu Contact About Wolfville
- **linkedin_url**: https://ca.linkedin.com/company/town-of-wolfville
- **tel_links**: 1-877-999-7117; 902-542-7000; 902-542-5767; 902-679-9124; (902) 542-7722; (902) 679-9124; 902-599-2866; 902.680.6453; 90

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "359 Main Street, Wolfville, Nova Scotia, Canada B4P 1A1", "address_country": "CA", "address_url": "https://wolfville.ca/contact-wolfville", "address_method": "pattern", "address_quote": "le Contact Print: Share: Contact Wolfville Town Hall 359 Main St Wolfville , NS B4P 1A1 Directions Monday to Friday 8:30am - 4:30pm 902-542-5767 Contact Wolfville Emer", "phone": "902-542-5767", "phone_url": "https://wolfville.ca/contact-wolfville", "domain": "wolfville.ca", "key": "b:014b5aa5afdd4fce", "name": "Town of Wolfville", "website": "https://wolfville.ca/", "kind": "buyer", "date": "2026-11-03"}

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
| b | Town of Wolfville |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "b:014b5aa5afdd4fce",
 "ap_contact_team": {
  "emails": [
   "towncouncil@wolfville.ca",
   "info@wbdc.me",
   "financeinfo@wolfville.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "towncouncil@wolfville.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "this_unit_only",
    "page_url": "https://wolfville.ca/town-hall/town-council",
    "quote": "towncouncil@wolfville.ca",
    "retrieved_date": "2026-10-28",
    "found_by": "chatgpt",
    "verification": "verified",
    "source_file": "chatgpt_buyer_ap_results_batch03.csv",
    "org": "Town of Wolfville - Mayor and Town Council distribution list",
    "task_id": "CH-AP-00236"
   },
   {
    "email": "info@wbdc.me",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://wolfville.ca/community/community-resources-directory",
    "quote": ">902 542 4842</a> </div> <div class=\"website\"> <a href=\"wolfvillebusiness.com\">Visit Website</a> </div> <div class=\"email\"> <a href=\"mailto:info@wbdc.me\">Email</a> </div> <div class=\"categories\"> <div class=\"label\">Categories:</div> <div class=\"content\"> <div class=\"community-resource__fie",
    "retrieved_date": "2026-10-28",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Town of Wolfville",
    "task_id": "CH-AP-00236"
   },
   {
    "email": "financeinfo@wolfville.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://wolfville.ca/town-hall/rates-and-finances/financial-statements",
    "quote": "paragraph--view-mode--default\"> <div class=\"widget-wrapper\"> <div class=\"title\"> <h5>Contact</h5> </div> <div class=\"body\"> <a href=\"mailto:Financeinfo@wolfville.ca\" class=\"field-email\">Email</a> </div> </div> </div> </div></div></div> </div> </div> </div> </div> </main> </div> <div id=\"fo",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Town of Wolfville",
    "task_id": "CH-AP-00236"
   }
  ]
 },
 "research_status": {
  "not_published": 1,
  "found": 3
 },
 "queries_tried": [
  "site:wolfville.ca invoices accounts payable; site:wolfville.ca \"invoice\" \"email\"; opened current Corporate Services, Tenders and Procurement and linked August2024 CCDC18 supplementary specifications",
  "site:wolfville.ca town hall email contact; official Corporate Services, Tenders and Procurement, Contact; site:wolfville.ca contact email towncouncil; current Town Council page",
  "site crawl of wolfville.ca (33 pages, robots.txt respected), no AI, no search engine",
  "site crawl of wolfville.ca (25 pages, robots.txt respected), no AI, no search engine"
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
