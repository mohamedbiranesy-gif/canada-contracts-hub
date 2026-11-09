# S5-48 — WorkplaceNL ⇄ Bursey Cleaners(2010) Limited

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 1 · AP grade A · missing: the vendor's GST/HST number (BN9)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Workplace Health, Safety and Compensation Commission (official name per Wikidata Q142084579, official website on the organisation's domain (https://workplacenl.ca/) + name; 2026-11-08) — 146-148 Forest Road, P.O. Box 9000, St. John's, NL A1A 3B8, Canada
SUBMIT TO: accounts.payable@workplacenl.ca (invoicing/AP mailbox, confirmed by the referee) | invoice portal: https://idcs-0344f1b8d1824f39b1211dc0abc4ced5.identity.oraclecloud.com/ui/v1/myconsole
REFERENCE: contract 0000270309 (merx_reference_number) | PO rule: purchase-order terms published (as published: shall not enter into any contract or commitment in the name Purchase order
FROM / REMIT TO: Bursey Cleaners(2010) Limited — P.O. Box 23010, St John's, NL, A1B 4J9 | GST/HST number not public
TAX: price plus HST for the performance of the Services in accordance with the (as printed on https://workplacenl.ca/site/uploads/2020/05/2020-04-T-Landscape-Mainten | CURRENCY: CAD | TERMS: 15 days of receipt (as printed on https://workplacenl.ca/site/uploads/2025/08/2025-43-P-External-Aud
DESCRIPTION: 2024-13-T Cleaning Services for WorkplaceNL's St. John's Building | AMOUNT: 652,551.80 CAD
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 92
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 13
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: WorkplaceNL (organisation (type not stated in the record), CA) — public contract / purchase award with a published end date (dated record): Bursey Cleaners(2010) Limited | subject: 2024-13-T Cleaning Services for WorkplaceNL's St. John's Building | instrument: contract | contract number: 0000270309 (merx_reference_number) | all identifiers: {"merx_id": "2917212805", "merx_reference_number": "0000270309", "contract_number": null, "awardee_index": 1} | value: 652551.8 CAD | awarded 2024-07-01, start 2024-07-01, end 2027-06-30 | published by: MERX public Awarded Solicitations (award notices) | record: https://www.merx.com/govnl/workplacenl/solicitations/2024-13-T-Cleaning-Services-for-WorkplaceNL-s-St-John-s-Building/0000270309?origin=0 | vendor in Canada because: MERX award notice 'Address' block, last line = 'Canada' (with city/province/postal code lines as published) | status rule: active (published end date today or later) | this buyer has 58 records with Canada-located vendors (51 distinct vendors; 1 in the last 12 months; latest 2026-06-01)
- **how_relationship_was_found**: the award record was harvested from the public procurement source named in `source` (scripts/<source> pipeline), matched to the buyer by its canonical name/key, and the vendor's Canada location read from the source's own vendor address/country field (`vendor_country_basis`)
- **keys**: b:94108db353030cbc|b:9b201589516aba2a
- **tier**: A
- **grade**: 4
- **records_with_this_vendor**: 1

## Buyer
- **buyer**: WorkplaceNL
- **buyer_website**: https://workplacenl.ca
- **buyer_phone**: +1-800-563-9000; +1-709-778-1000 (Wikidata Q142084579, official website on the organisation's domain (https://workplacenl.ca/) + name; 2026-11-08)
- **buyer_legal_name_as_published**: Workplace Health, Safety and Compensation Commission (official name per Wikidata Q142084579, official website on the organisation's domain (https://workplacenl.ca/) + name; 2026-11-08)
- **buyer_type**: government ministry / agency (from the organisation's name / web domain)
- **buyer_sector**: government: provincial / federal
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q142084579; government agency
- **buyer_founded**: 1951-04-01 (Wikidata Q142084579, official website on the organisation's domain (https://workplacenl.ca/) + name; 2026-11-08)
- **buyer_facts_provenance**: legal name: the site's copyright / footer line (tools/org_extras.py); AP phone: the lane's AP page (https://workplacenl.ca/site/uploads/2023/11/Managing-Invoices-and-Payments-Revised-June-2024.pdf); invoice mailing address: the lane's AP page (https://workplacenl.ca/site/uploads/2023/11/Managing-Invoices-and-Payments-Revised-June-2024.pdf); invoicing requirements: the lane's AP page (https://workplacenl.ca/site/uploads/2023/11/Managing-Invoices-and-Payments-Revised-June-2024.pdf); payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoice portal: the lane's AP page (https://workplacenl.ca/site/uploads/2023/11/Managing-Invoices-and-Payments-Revised-June-2024.pdf)
- **buyer_payment_method_preference**: required and described in this Tender by check (as printed on https://workplacenl.ca/site/uploads/2020/07/2020-07-T-Standing-Offer-for-the-Supply-of-Computer-Systems-FINAL-Fillable.pdf, re-read 2026-11-08)
- **buyer_tax_exempt_status**: price plus HST for the performance of the Services in accordance with the (as printed on https://workplacenl.ca/site/uploads/2020/05/2020-04-T-Landscape-Maintenance-Services-FINAL.pdf, re-read 2026-11-08)
- **buyer_esignature_preference**: electronic signature, and each counterpart shall be deemed an original, but all of them together sha (as printed on https://workplacenl.ca/site/uploads/2020/05/2020-04-T-Landscape-Maintenance-Services-FINAL.pdf, re-read 2026-11-08)
- **buyer_keys**: 2

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: accounts.payable@workplacenl.ca
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://workplacenl.ca/site/uploads/2023/11/Managing-Invoices-and-Payments-Revised-June-2024.pdf
- **email_evidence_quote**: accounts.payable@workplacenl.ca
- **email_evidence_context**: it the invoice. If they do not match, select Save and the system will recalculate the amounts. 7 Once the Invoice Amount and Due amount match, click Submit. Note: If an invoice is submitted in error or was submitted with incorrect information, email accounts.payable@workplacenl.ca to have the information corrected or the invoice cancelled with a credit note issued, if applicable. 8 Creating Invoices without PO Select Create Invoice without PO from the left-hand Task menu. Enter invoice details: Supplier Site: Select LOCAL fro (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: accounts.payable@workplacenl.ca (invoicing/AP) | researched by the ChatGPT/Codex agent (lane chatgpt) (page opened and quoted) on 2026-10-27 | page: https://workplacenl.ca/site/uploads/2023/11/Managing-Invoices-and-Payments-Revised-June-2024.pdf | quote: "accounts.payable@workplacenl.ca" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; DNS lookup failed; mail handled by self-hosted or other (xmail.workplacenl.ca) | lane file: chatgpt/chatgpt_buyer_ap_results_batch05.csv task CH-AP-00488
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; DNS lookup failed; mail handled by self-hosted or other (xmail.workplacenl.ca)
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1; p=quarantine; rua=mailto:dmarc.rua@workplacenl.ca; ruf=mailto:dmarc.ruf@workplacenl.ca
- **dmarc_record_domain**: workplacenl.ca
- **spf_policy**: DNS lookup failed
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_phone**: 709-778-1000
- **invoice_mailing_address**: 146-148 Forest Road, P.O. Box 9000, St. John's, NL A1A 3B8, Canada
- **invoicing_requirements**: Health-provider/vendor OracleSupplierPortal supports PO and non-PO invoices/paymentstatus. Use LOCALsite, invoice#, serviceidentifiers and date; non-PO requires requestoremployeeemail; enter pretaxlines, taxclassification and calculatetax; invoiceamount/due mustmatch. Email AP for erroneousinvoices/
- **payment_terms_as_published**: 15 days of receipt (as printed on https://workplacenl.ca/site/uploads/2025/08/2025-43-P-External-Audit-Services.pdf, re-read 2026-11-08)
- **po_required_as_published**: purchase-order terms published (as published: shall not enter into any contract or commitment in the name Purchase order) (as printed on https://workplacenl.ca/site/uploads/2020/02/2020-06-T-Standing-Offer-Supply-of-Headsets.pdf, re-read 2026-11-08)
- **invoice_portal_url**: https://idcs-0344f1b8d1824f39b1211dc0abc4ced5.identity.oraclecloud.com/ui/v1/myconsole
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel published by the buyer; the e-mail is the contact)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "payment_terms": "15 days of receipt (as printed on https://workplacenl.ca/site/uploads/2025/08/2025-43-P-External-Audit-Services.pdf, re-read 2026-11-08)", "po_required": "purchase-order terms published (as published: shall not enter into any contract or commitment in the name Purchase order) (as printed on https://workplacenl.ca/site/uploads/2020/02/2020-06-T-Standing-Offer-Supply-of-Headsets.pdf, re-read 2026-11-08)", "portal_url": "https://idcs-0344f1b8d1824f39b1211dc0abc4ced5.identity.oraclecloud.com/ui/v1/myconsole", "portal_kind": "actionable supplier / invoice portal named by the buyer", "ap_phone": "709-778-1000", "mailing_address": "146-148 Forest Road, P.O. Box 9000, St. John's, NL A1A 3B8, Canada", "requirements_text": "Health-provider/vendor OracleSupplierPortal supports PO and non-PO invoices/paymentstatus. Use LOCALsite, invoice#, serviceidentifiers and date; non-PO requires requestoremployeeemail; enter pretaxlines, taxclassification and calculatetax; invoiceamount/due mustmatch. Email AP for erroneousinvoices/"}
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Workplace Health, Safety and Compensation Commission (official name per Wikidata Q142084579, official website on the organisation's domain (https://workplacenl.ca/) + name; 2026-11-08) — 146-148 Forest Road, P.O. Box 9000, St. John's, NL A1A 3B8, Canada ⏎ SUBMIT TO: accounts.payable@workplacenl.ca (invoicing/AP mailbox, confirmed by the referee) | invoice portal: https://idcs-0344f1b8d1824f39b1211dc0abc4ced5.identity.oraclecloud.com/ui/v1/myconsole ⏎ REFERENCE: contract 0000270309 (merx_reference_number) | PO rule: purchase-order terms published (as published: shall not enter into any contract or commitment in the name Purchase order ⏎ FROM / REMIT TO: Bursey Cleaners(2010) Limited — P.O. Box 23010, St John's, NL, A1B 4J9 | GST/HST number not public ⏎ TAX: price plus HST for the performance of the Services in accordance with the (as printed on https://workplacenl.ca/site/uploads/2020/05/2020-04-T-Landscape-Mainten | CURRENCY: CAD | TERMS: 15 days of receipt (as printed on https://workplacenl.ca/site/uploads/2025/08/2025-43-P-External-Aud ⏎ DESCRIPTION: 2024-13-T Cleaning Services for WorkplaceNL's St. John's Building | AMOUNT: 652,551.80 CAD
- **invoice_card_json**: {"bill_to": {"legal_name": "Workplace Health, Safety and Compensation Commission (official name per Wikidata Q142084579, official website on the organisation's domain (https://workplacenl.ca/) + name; 2026-11-08)", "legal_name_is_published": true, "address": "146-148 Forest Road, P.O. Box 9000, St. John's, NL A1A 3B8, Canada", "address_is_the_invoice_address": true, "tax_number": "", "language": "en"}, "submit_to": {"email": "accounts.payable@workplacenl.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "https://idcs-0344f1b8d1824f39b1211dc0abc4ced5.identity.oraclecloud.com/ui/v1/myconsole", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "146-148 Forest Road, P.O. Box 9000, St. John's, NL A1A 3B8, Canada", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "purchase-order terms published (as published: shall not enter into any contract or commitment in the name Purchase order) (as printed on https://workplacenl.ca/site/uploads/2020/02/2020-06-T-Standing-Offer-Supply-of-Headsets.pdf, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "0000270309 (merx_reference_number)", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: 0000270309 (merx_reference_number) — source ca_merx"}, "terms": {"payment_terms": "15 days of receipt (as printed on https://work
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: vendor GST/HST number; vendor legal name
- **ap_grade**: A
- **ap_score**: 90
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | missing: finance mailbox
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: contract or agreement number: 0000270309 (merx_reference_number) — source ca_merx

## Vendor
- **vendor**: Bursey Cleaners(2010) Limited
- **vendor_address**: P.O. Box 23010, St John's, NL, A1B 4J9
- **vendor_country_basis**: MERX award notice 'Address' block, last line = 'Canada' (with city/province/postal code lines as published)
- **vendor_website**: https://bursey-cleaners.ca/
- **vendor_contact_evidence_url**: https://bursey-cleaners.ca/contact/
- **vendor_logo_url**: https://bursey-cleaners.ca/wp-content/uploads/2020/09/Bursey-Cleaners-Updated-Logo-1.png
- **vendor_website_basis**: found by a web search, confirmed by reading the site on 2026-11-08: https://bursey-cleaners.ca/ (Commercial Cleaning Services in St. John's | Bursey Cleaners Skip to content Home About Us Services Commercial Building Cleaning Services Disinfection Services )
- **vendor_facts_provenance**: name and address: the record's vendor block (MERX public Awarded Solicitations (award notices)); phone / role e-mails / logo: the vendor's own site, https://bursey-cleaners.ca/contact/ (tools/org_contacts.py, org_extras.py); website: https://bursey-cleaners.ca/
- **vendor_concentration_top_share**: Trampoline: 3% of 58 records
- **vendor_registry_match_level**: no_match

## Contract
- **po_required_as_published**: purchase-order terms published (as published: shall not enter into any contract or commitment in the name Purchase order) (as printed on https://workplacenl.ca/site/uploads/2020/02/2020-06-T-Standing-Offer-Supply-of-Headsets.pdf, re-read 2026-11-08)
- **contract_status**: active (published end date today or later)
- **contract_reference**: {"merx_id": "2917212805", "merx_reference_number": "0000270309", "contract_number": null, "awardee_index": 1}
- **contract_title**: 2024-13-T Cleaning Services for WorkplaceNL's St. John's Building
- **contract_description**: 2024-13-T Cleaning Services for WorkplaceNL's St. John's Building (the record's title; the source publishes no separate description)
- **contract_or_agreement_number**: 0000270309 (merx_reference_number)
- **award_or_notice_id**: 2917212805 (merx_id); 1 (awardee_index)
- **contract_value**: 652551.8
- **currency**: CAD
- **award_date**: 2024-07-01
- **start_date**: 2024-07-01
- **end_date**: 2027-06-30
- **contract_link**: https://www.merx.com/govnl/workplacenl/solicitations/2024-13-T-Cleaning-Services-for-WorkplaceNL-s-St-John-s-Building/0000270309?origin=0
- **source**: MERX public Awarded Solicitations (award notices)
- **contracts_with_canadian_suppliers**: 58
- **records_last_12_months**: 1
- **record_sources**: MERX public Awarded Solicitations (award notices) (57); NL Public Procurement Agency - Contract Awards Reports (semi-monthly PDF reports to the Chief Procurement Officer, s.31 Public Procurement Regulations) (1)
- **records_with_this_vendor**: 1
- **records_in_contract_dataset**: 58 records with Canada-located vendors (this row's organisation)

## Tax / currency / terms (derived)
_nothing recorded_

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Workplace Health, Safety and Compensation Commission (official name per Wikidata Q142084579, official website on the organisation's domain (https://workplacenl.ca/) + name; 2026-11-08) — 146-148 Forest Road, P.O. Box 9000, St. John's, NL A1A 3B8, Canada ⏎ SUBMIT TO: accounts.payable@workplacenl.ca (invoicing/AP mailbox, confirmed by the referee) | invoice portal: https://idcs-0344f1b8d1824f39b1211dc0abc4ced5.identity.oraclecloud.com/ui/v1/myconsole ⏎ REFERENCE: contract 0000270309 (merx_reference_number) | PO rule: purchase-order terms published (as published: shall not enter into any contract or commitment in the name Purchase order ⏎ FROM / REMIT TO: Bursey Cleaners(2010) Limited — P.O. Box 23010, St John's, NL, A1B 4J9 | GST/HST number not public ⏎ TAX: price plus HST for the performance of the Services in accordance with the (as printed on https://workplacenl.ca/site/uploads/2020/05/2020-04-T-Landscape-Mainten | CURRENCY: CAD | TERMS: 15 days of receipt (as printed on https://workplacenl.ca/site/uploads/2025/08/2025-43-P-External-Aud ⏎ DESCRIPTION: 2024-13-T Cleaning Services for WorkplaceNL's St. John's Building | AMOUNT: 652,551.80 CAD
- **invoice_card_json**: {"bill_to": {"legal_name": "Workplace Health, Safety and Compensation Commission (official name per Wikidata Q142084579, official website on the organisation's domain (https://workplacenl.ca/) + name; 2026-11-08)", "legal_name_is_published": true, "address": "146-148 Forest Road, P.O. Box 9000, St. John's, NL A1A 3B8, Canada", "address_is_the_invoice_address": true, "tax_number": "", "language": "en"}, "submit_to": {"email": "accounts.payable@workplacenl.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "https://idcs-0344f1b8d1824f39b1211dc0abc4ced5.identity.oraclecloud.com/ui/v1/myconsole", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "146-148 Forest Road, P.O. Box 9000, St. John's, NL A1A 3B8, Canada", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "purchase-order terms published (as published: shall not enter into any contract or commitment in the name Purchase order) (as printed on https://workplacenl.ca/site/uploads/2020/02/2020-06-T-Standing-Offer-Supply-of-Headsets.pdf, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "0000270309 (merx_reference_number)", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: 0000270309 (merx_reference_number) — source ca_merx"}, "terms": {"payment_terms": "15 days of receipt (as printed on https://work
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: vendor GST/HST number; vendor legal name
- **ap_grade**: A
- **ap_score**: 90
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | missing: finance mailbox
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **facts_provenance_json**: {"mailbox": ["accounts.payable@workplacenl.ca (invoicing/AP)", "researched by the ChatGPT/Codex agent (lane chatgpt) (page opened and quoted) on 2026-10-27", "page: https://workplacenl.ca/site/uploads/2023/11/Managing-Invoices-and-Payments-Revised-June-2024.pdf", "quote: \"accounts.payable@workplacenl.ca\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; DNS lookup failed; mail handled by self-hosted or other (xmail.workplacenl.ca)", "lane file: chatgpt/chatgpt_buyer_ap_results_batch05.csv task CH-AP-00488"], "buyer_facts": ["legal name: the site's copyright / footer line (tools/org_extras.py)", "AP phone: the lane's AP page (https://workplacenl.ca/site/uploads/2023/11/Managing-Invoices-and-Payments-Revised-June-2024.pdf)", "invoice mailing address: the lane's AP page (https://workplacenl.ca/site/uploads/2023/11/Managing-Invoices-and-Payments-Revised-June-2024.pdf)", "invoicing requirements: the lane's AP page (https://workplacenl.ca/site/uploads/2023/11/Managing-Invoices-and-Payments-Revised-June-2024.pdf)", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoice portal: the lane's AP page (https://workplacenl.ca/site/uploads/2023/11/Mana

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://workplacenl.ca/site/uploads/2023/11/Managing-Invoices-and-Payments-Revised-June-2024.pdf | 2026-11-08 | ok |  |  | supplier / vendor portal |  |  |  |  |  |  |

## Buyer site facts (org_extras, domain unknown)
_not read_

## Buyer role mailboxes found on its site (org_contacts)
_not read_

## Vendor site facts (org_extras, bursey-cleaners.ca)
- **status**: ok
- **pages**: 3
- **v**: 2
- **jsonld_type**: ProfessionalService/Organization
- **jsonld_name**: Bursey Cleaners | Commercial Janitor Services in St. Johns, NL
- **jsonld_address**: PO Box 23010, St. Johns, Newfoundland, A1B4J9, Canada
- **jsonld_logo**: https://bursey-cleaners.ca/wp-content/uploads/2024/03/Bursey-Cleaners-Updated-Logo-1.png
- **jsonld_url**: https://bursey-cleaners.ca
- **jsonld_quote**: {"@context":"https://schema.org","@graph":[{"@type":"Place","@id":"https://bursey-cleaners.ca/#place","address":{"@type":"PostalAddress","streetAddress":"PO Box 23010","addressLocality":"St. Johns","addressRegion":"Newfoundland","postalCode":"A1B4J9","addressCountry":"Canada"}},{"@type":["Profession
- **jsonld_page**: https://bursey-cleaners.ca/
- **tel_links**: +1-709-722-9576; +17097229576
- **tel_links_url**: https://bursey-cleaners.ca/
- **language**: en
- **logo_url**: https://bursey-cleaners.ca/wp-content/uploads/2020/09/Bursey-Cleaners-Updated-Logo-1.png
- **logo_basis**: logo image in the site header
- **domain**: bursey-cleaners.ca
- **key**: vendor:Bursey Cleaners(2010) Limited
- **name**: Bursey Cleaners(2010) Limited
- **website**: https://bursey-cleaners.ca/
- **kind**: vendor
- **date**: 2026-11-08

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "PO Box 23010, St. Johns, Newfoundland, A1B4J9", "address_country": "Canada", "address_url": "https://bursey-cleaners.ca/contact/", "address_method": "json-ld", "address_quote": "information to respond to your enquiry. Contact Info PO Box 23010 St. Johns, NL A1B4J9 Phone: (709) 722-9576 Fax: (709) 722-9578 Email: bursey@bclservicegroup.com Abo", "phone": "+17097229576", "phone_url": "https://bursey-cleaners.ca/contact/", "domain": "bursey-cleaners.ca", "key": "vendor:Bursey Cleaners(2010) Limited", "name": "Bursey Cleaners(2010) Limited", "website": "https://bursey-cleaners.ca/", "kind": "vendor", "date": "2026-11-08"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | WorkplaceNL | Q142084579 | official website on the organisation's domain (https://workplacenl.ca/) + name | Workplace Health, Safety and Compensation Commission [en] | WorkplaceNL |  | government agency |  | Canada | 1951-04-01 |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "b:94108db353030cbc",
 "ap_contact_team": {
  "emails": [
   "accounts.payable@workplacenl.ca",
   "purchasing@workplacenl.ca",
   "payment.remittances@workplacenl.ca"
  ],
  "invoice_portal": "https://idcs-0344f1b8d1824f39b1211dc0abc4ced5.identity.oraclecloud.com/ui/v1/myconsole",
  "phone": "1-800-563-9000 (supplier registration)",
  "mailing_address": null,
  "invoicing_requirements": "Health-provider/vendor OracleSupplierPortal supports PO and non-PO invoices/paymentstatus. Use LOCALsite, invoice#, serviceidentifiers and date; non-PO requires requestoremployeeemail; enter pretaxlines, taxclassification and calculatetax; invoiceamount/due mustmatch. Email AP for erroneousinvoices/cancellation/creditnotes. Registration requires bankingdetails/voidcheque fordirectdeposit. Portal not entered.",
  "evidence": [
   {
    "email": "accounts.payable@workplacenl.ca",
    "type": "accounts_payable",
    "invoice_portal": "https://idcs-0344f1b8d1824f39b1211dc0abc4ced5.identity.oraclecloud.com/ui/v1/myconsole",
    "phone": null,
    "mailing_address": null,
    "requirements": "Health-provider/vendor OracleSupplierPortal supports PO and non-PO invoices/paymentstatus. Use LOCALsite, invoice#, serviceidentifiers and date; non-PO requires requestoremployeeemail; enter pretaxlines, taxclassification and calculatetax; invoiceamount/due mustmatch. Email AP for erroneousinvoices/cancellation/creditnotes. Registration requires bankingdetails/voidcheque fordirectdeposit. Portal not entered.",
    "applies_to": "this_unit_only",
    "page_url": "https://workplacenl.ca/site/uploads/2023/11/Managing-Invoices-and-Payments-Revised-June-2024.pdf",
    "quote": "accounts.payable@workplacenl.ca",
    "retrieved_date": "2026-10-27",
    "found_by": "chatgpt",
    "verification": "verified",
    "source_file": "chatgpt_buyer_ap_results_batch05.csv",
    "org": "WorkplaceNL",
    "task_id": "CH-AP-00488"
   },
   {
    "email": "purchasing@workplacenl.ca",
    "type": "supplier_payment",
    "invoice_portal": "https://idcs-0344f1b8d1824f39b1211dc0abc4ced5.identity.oraclecloud.com/ui/v1/myconsole",
    "phone": "1-800-563-9000 (supplier registration)",
    "mailing_address": null,
    "requirements": "Health-provider/vendor OracleSupplierPortal supports PO and non-PO invoices/paymentstatus. Use LOCALsite, invoice#, serviceidentifiers and date; non-PO requires requestoremployeeemail; enter pretaxlines, taxclassification and calculatetax; invoiceamount/due mustmatch. Email AP for erroneousinvoices/cancellation/creditnotes. Registration requires bankingdetails/voidcheque fordirectdeposit. Portal not entered.",
    "applies_to": "this_unit_only",
    "page_url": "https://workplacenl.ca/site/uploads/2023/11/Submitting-Your-Registration-Health-Care-Providers-and-Vendors.pdf",
    "quote": "purchasing@workplacenl.ca",
    "retrieved_date": "2026-10-27",
    "found_by": "chatgpt",
    "verification": "verified",
    "source_file": "chatgpt_buyer_ap_results_batch05.csv",
    "org": "WorkplaceNL",
    "task_id": "CH-AP-00488"
   },
   {
    "email": "payment.remittances@workplacenl.ca",
    "type": "supplier_payment",
    "invoice_portal": "https://idcs-0344f1b8d1824f39b1211dc0abc4ced5.identity.oraclecloud.com/ui/v1/myconsole",
    "phone": "709-778-2927 (missing payment remittances)",
    "mailing_address": null,
    "requirements": "Health-provider/vendor OracleSupplierPortal supports PO and non-PO invoices/paymentstatus. Use LOCALsite, invoice#, serviceidentifiers and date; non-PO requires requestoremployeeemail; enter pretaxlines, taxclassification and calculatetax; invoiceamount/due mustmatch. Email AP for erroneousinvoices/cancellation/creditnotes. Registration requires bankingdetails/voidcheque fordirectdeposit. Portal not entered.",
    "applies_to": "this_unit_only",
    "page_url": "https://workplacenl.ca/site/uploads/2023/11/Managing-Invoices-and-Payments-Revised-June-2024.pdf",
    "quote": "payment.remittances@workplacenl.ca",
    "retrieved_date": "2026-10-27",
    "found_by": "chatgpt",
    "verification": "verified",
    "source_file": "chatgpt_buyer_ap_results_batch05.csv",
    "org": "WorkplaceNL",
    "task_id": "CH-AP-00488"
   },
   {
    "email": "purchasing@workplacenl.ca",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://workplacenl.ca/site/uploads/2023/12/2023-35-T-Modified-Vehicle-for-Client.pdf",
    "quote": "m issued by WorkplaceNL. 2.3 QUESTIONS AND CLARIFICATION 2.3.1 All questions related to this Tender must be directed in writing by email to purchasing@workplacenl.ca or through the Tender posting on www.merx.com and received by WorkplaceNL before 4:00 PM Newfoundland Time on December 15, 2",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "WorkplaceNL",
    "task_id": "CL-WS-00201"
   },
   {
    "email": "purchasing@workplacenl.ca",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://workplacenl.ca/site/uploads/2026/06/2026-04-P-Global-Custodian-Services.pdf",
    "quote": "th the Public Procurement Regulations, as amended. The names of all Applicants will be provided at the public opening. Applicants may email purchasing@workplacenl.ca to request a Webex meeting invite to attend the public opening. Applicants must include their 7 WorkplaceNL 2026-04-P Global",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "WorkplaceNL",
    "task_id": "CL-WS-00114"
   }
  ]
 },
 "research_status": {
  "found": 4,
  "unclear": 1
 },
 "queries_tried": [
  "site:workplacenl.ca \"acco
```

## PO-level open data naming this buyer
_none_

## Contract records between the pair (dataset)
| record_id | source | status | title | value | currency | start | end | identifiers | link |
|---|---|---|---|---|---|---|---|---|---|
| ca_merx:2917212805:1 | ca_merx | ongoing | 2024-13-T Cleaning Services for WorkplaceNL's St. John's Building | 652551.8 | CAD |  |  | {"merx_id": "2917212805", "merx_reference_number": "0000270309", "contract_number": null, "awardee_index": 1} | https://www.merx.com/govnl/workplacenl/solicitations/2024-13-T-Cleaning-Services-for-WorkplaceNL-s-St-John-s-Building/0000270309?origin=0 |

## The buyer's other Canadian-vendor records (first 60 of 57)
| record_id | vendor | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_merx:3882774001:1 | Trampoline | Media Placement Management Services |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Media-Placement-Management-Services/0000317904?origin=0 |
| ca_merx:2484892026:1 | Trampoline | Media Placement Management Services |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Media-Placement-Management-Services/0000246669?origin=0 |
| ca_merx:2617396054:1 | Clay Oates Landscaping & Construction Ltd. | Snow Clearing & Ice Control Services for Injured Workers (Carbonear) |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Snow-Clearing-Ice-Control-Services-for-Injured-Workers-Carbonear/0000256075?origin=0 |
| ca_merx:2617396052:1 | exploits valley paving ltd | Snow Clearing & Ice Control Services for Injured Workers (Grand Falls-Windsor B) |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Snow-Clearing-Ice-Control-Services-for-Injured-Workers-Grand-Falls-Windsor-B/0000256070?origin=0 |
| ca_merx:3553746057:1 | Hennessey's Trucking Limited | Snow Clearing and Ice Control Services for Injured Workers (Kilbride) |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Snow-Clearing-and-Ice-Control-Services-for-Injured-Workers-Kilbride/0000299861?origin=0 |
| ca_merx:3553746064:1 | Top Notch Landscaping | Snow Clearing and Ice Control Services for Injured Workers (Green Bay) |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Snow-Clearing-and-Ice-Control-Services-for-Injured-Workers-Green-Bay/0000299872?origin=0 |
| ca_merx:3553746062:1 | House’s transport ltd | Snow Clearing and Ice Control Services for Injured Workers (Port au Ch |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Snow-Clearing-and-Ice-Control-Services-for-Injured-Workers-Port-au-Ch/0000299869?origin=0 |
| ca_merx:2617396055:1 | Hennessey's Trucking Limited | Snow Clearing & Ice Control Services for Injured Workers (Paradise) |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Snow-Clearing-Ice-Control-Services-for-Injured-Workers-Paradise/0000256077?origin=0 |
| ca_merx:2617396053:1 | All Clear Asphalt Maintenance Ltd | Snow Clearing & Ice Control Services for Injured Workers (St. John's) |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Snow-Clearing-Ice-Control-Services-for-Injured-Workers-St-John-s/0000256072?origin=0 |
| ca_merx:2617396051:1 | exploits valley paving ltd | Snow Clearing & Ice Control Services for Injured Workers (Grand Falls-Windsor A) |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Snow-Clearing-Ice-Control-Services-for-Injured-Workers-Grand-Falls-Windsor-A/0000256065?origin=0 |
| ca_merx:3553746055:1 | Hickey Construction Limited | Snow Clearing and Ice Control Services for Injured Workers (Goose Bay) |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Snow-Clearing-and-Ice-Control-Services-for-Injured-Workers-Goose-Bay/0000299856?origin=0 |
| ca_merx:3193854757:1 | Lifemark Health Corp. | Labour Market Re-Entry (LMR) Services for Injured Workers |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Labour-Market-Re-Entry-LMR-Services-for-Injured-Workers/0000281088?origin=0 |
| ca_merx:3193854757:2 | ProVo Consulting Inc | Labour Market Re-Entry (LMR) Services for Injured Workers |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Labour-Market-Re-Entry-LMR-Services-for-Injured-Workers/0000281088?origin=0 |
| ca_merx:3193854757:3 | Vocational Rehab Assessments | Labour Market Re-Entry (LMR) Services for Injured Workers |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Labour-Market-Re-Entry-LMR-Services-for-Injured-Workers/0000281088?origin=0 |
| ca_merx:3212599561:1 | College of the North Atlantic | Supply of Introductory Computer Training for Injured Workers |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Supply-of-Introductory-Computer-Training-for-Injured-Workers/0000281700?origin=0 |
| ca_merx:2523617001:1 | Regional Medical Products Limited | Standing Offer for the Supply of Transcutaneous Electrical Nerve Stimulation (TE |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Standing-Offer-for-the-Supply-of-Transcutaneous-Electrical-Nerve-Stimulation-TE/0000250020?origin=0 |
| ca_merx:2765026611:1 | Eastern Medical | Standing Offer for the Supply of Homestyle Adjustable Beds, Mattresses & Rails |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Standing-Offer-for-the-Supply-of-Homestyle-Adjustable-Beds-Mattresses-Rails/0000262606?origin=0 |
| ca_merx:3042754257:1 | Atlantic Offshore Medical Services Limited | Medical Consulting Services |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Medical-Consulting-Services/0000276338?origin=0 |
| ca_merx:3042754257:2 | Dr. Trevor Humes PMC | Medical Consulting Services |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Medical-Consulting-Services/0000276338?origin=0 |
| ca_merx:2829934452:1 | Nadine Jacob, Audiologist | Audiology Consultant |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Audiology-Consultant/0000265952?origin=0 |
| ca_merx:2931379132:1 | Norbert Lake, Chiropractor | Chiropractic Consulting Services |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Chiropractic-Consulting-Services/0000271020?origin=0 |
| ca_merx:2931379132:2 | Trillium Health Partners -Insight Health Solutions | Chiropractic Consulting Services |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Chiropractic-Consulting-Services/0000271020?origin=0 |
| ca_merx:3470776711:1 | InMotion Health Centre | Home Assessments |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Home-Assessments/0000295109?origin=0 |
| ca_merx:3470776711:2 | IOHS | Home Assessments |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Home-Assessments/0000295109?origin=0 |
| ca_merx:3470776711:3 | Lifemark Health Corp. | Home Assessments |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Home-Assessments/0000295109?origin=0 |
| ca_merx:3470776711:4 | Occupational Therapy Consultant | Home Assessments |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Home-Assessments/0000295109?origin=0 |
| ca_merx:3601189403:1 | Respiratory Therapy Specialists Inc. | Standing Offer for the Supply of Home Oxygen and Sleep Apnea Equipment |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Standing-Offer-for-the-Supply-of-Home-Oxygen-and-Sleep-Apnea-Equipment/0000302917?origin=0 |
| ca_merx:3253312404:1 | Beltone Canada | Standing Offer for the Supply of Hearing Aids and Associated Devices |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Standing-Offer-for-the-Supply-of-Hearing-Aids-and-Associated-Devices/0000283302?origin=0 |
| ca_merx:3253312404:2 | Beltone Canada | Standing Offer for the Supply of Hearing Aids and Associated Devices |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Standing-Offer-for-the-Supply-of-Hearing-Aids-and-Associated-Devices/0000283302?origin=0 |
| ca_merx:3253312404:3 | Bernafon Canada | Standing Offer for the Supply of Hearing Aids and Associated Devices |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Standing-Offer-for-the-Supply-of-Hearing-Aids-and-Associated-Devices/0000283302?origin=0 |
| ca_merx:3253312404:4 | Oticon Canada | Standing Offer for the Supply of Hearing Aids and Associated Devices |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Standing-Offer-for-the-Supply-of-Hearing-Aids-and-Associated-Devices/0000283302?origin=0 |
| ca_merx:3253312404:5 | Sonova Canada Inc O/A Phonak Canada | Standing Offer for the Supply of Hearing Aids and Associated Devices |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Standing-Offer-for-the-Supply-of-Hearing-Aids-and-Associated-Devices/0000283302?origin=0 |
| ca_merx:3253312404:6 | Sonova Canada Inc O/A Unitron Canada | Standing Offer for the Supply of Hearing Aids and Associated Devices |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Standing-Offer-for-the-Supply-of-Hearing-Aids-and-Associated-Devices/0000283302?origin=0 |
| ca_merx:3253312404:7 | Starkey Canada | Standing Offer for the Supply of Hearing Aids and Associated Devices |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Standing-Offer-for-the-Supply-of-Hearing-Aids-and-Associated-Devices/0000283302?origin=0 |
| ca_merx:3253312404:8 | WS Audiology Canada Inc. | Standing Offer for the Supply of Hearing Aids and Associated Devices |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Standing-Offer-for-the-Supply-of-Hearing-Aids-and-Associated-Devices/0000283302?origin=0 |
| ca_merx:3462901805:1 | NFLD Hearing Health Centre | Standing Offer for the Supply of Hearing Aid Batteries |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Standing-Offer-for-the-Supply-of-Hearing-Aid-Batteries/0000294571?origin=0 |
| ca_merx:2898308304:1 | Beltone Audiology and Hearing Clinic | Service Providers of Hearing Aid Devices |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Service-Providers-of-Hearing-Aid-Devices/0000269260?origin=0 |
| ca_merx:2898308304:2 | Beltone Hearing Service | Service Providers of Hearing Aid Devices |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Service-Providers-of-Hearing-Aid-Devices/0000269260?origin=0 |
| ca_merx:2898308304:3 | Exploits Hearing Aid Center | Service Providers of Hearing Aid Devices |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Service-Providers-of-Hearing-Aid-Devices/0000269260?origin=0 |
| ca_merx:2898308304:4 | HearingLife Canada | Service Providers of Hearing Aid Devices |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Service-Providers-of-Hearing-Aid-Devices/0000269260?origin=0 |
| ca_merx:2898308304:5 | Maico Hearing Service | Service Providers of Hearing Aid Devices |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Service-Providers-of-Hearing-Aid-Devices/0000269260?origin=0 |
| ca_merx:2898308304:6 | Miracle-Ear Canada, Ltd. | Service Providers of Hearing Aid Devices |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Service-Providers-of-Hearing-Aid-Devices/0000269260?origin=0 |
| ca_merx:2898308304:7 | Newfoundland Hearing Health Centre | Service Providers of Hearing Aid Devices |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Service-Providers-of-Hearing-Aid-Devices/0000269260?origin=0 |
| ca_merx:2898308304:8 | Quality Care Hearing unit 103 | Service Providers of Hearing Aid Devices |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Service-Providers-of-Hearing-Aid-Devices/0000269260?origin=0 |
| ca_merx:2898308304:9 | Red Door Hearing & Speech Inc | Service Providers of Hearing Aid Devices |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Service-Providers-of-Hearing-Aid-Devices/0000269260?origin=0 |
| ca_merx:2898308304:10 | SOUND ISLAND HEARING INC | Service Providers of Hearing Aid Devices |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Service-Providers-of-Hearing-Aid-Devices/0000269260?origin=0 |
| ca_merx:3557933051:1 | Eastern Medical | Standing Offer for Health Care Devices and Adaptive Equipment |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Standing-Offer-for-Health-Care-Devices-and-Adaptive-Equipment/0000300106?origin=0 |
| ca_merx:2498636907:1 | GRAND & TOY | Standing Offer for the Supply of Lexmark Toner Cartridges |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Standing-Offer-for-the-Supply-of-Lexmark-Toner-Cartridges/0000247893?origin=0 |
| ca_merx:2380217570:1 | IMP Solutions | Laptops, Desktops and Peripheral Computer Equipment for Injured Workers |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Laptops-Desktops-and-Peripheral-Computer-Equipment-for-Injured-Workers/0000238687?origin=0 |
| ca_merx:2437712454:1 | IMP Solutions | Standing Offer for the Supply of Computer Systems |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Standing-Offer-for-the-Supply-of-Computer-Systems/0000242834?origin=0 |
| ca_merx:2099221313:1 | Ricoh Canada | Standing Offer for the Supply of Computer Systems |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Standing-Offer-for-the-Supply-of-Computer-Systems/0000216342?origin=0 |
| ca_merx:1948816620:1 | Eckler Ltd. | Investment Consulting Services |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Investment-Consulting-Services/0000208236?origin=0 |
| ca_merx:1892945827:1 | CIBC Mellon | Global Custodian and Performance Measurement |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Global-Custodian-and-Performance-Measurement/0000205476?origin=0 |
| ca_merx:1790743703:1 | Bell | Telecommunication Services |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Telecommunication-Services/0000198095?origin=0 |
| ca_merx:1804032265:1 | Deloitte MAIN ACCOUNT | Electronic Document and Records Management System |  |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Electronic-Document-and-Records-Management-System/0000199269?origin=0 |
| ca_merx:1955493709:1 | LAKEVIEW CHRYSLER | Wheelchair Accessible Van with Custom Modifications | 75779.0 |  |  | https://www.merx.com/govnl/workplacenl/solicitations/Wheelchair-Accessible-Van-with-Custom-Modifications/0000208452?origin=0 |
| ca_newfoundland:b4edb2e00ddab650 | Inergex Canada, Inc. (dba Crossfuze) | ServiceNow Subscription Renewal Licensing for MyWorkplaceNL Online Services | 488612.04 |  |  | https://www.gov.nl.ca/ppa/files/Contract-and-Exception-Awards-December-16-31-2023.pdf |

## The vendor's other buyers in the dataset (first 60 of 4)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_bidsandtenders:156daa1c-514b-4e3e-a540-3396e54bee26:1 | Newfoundland Labrador Hydro | Janitorial Services: Soldiers’ Pond Office Building - Soldier's Pond, NL | 184970.85 |  |  | https://nlhydro.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/156daa1c-514b-4e3e-a540-3396e54bee26 |
| ca_merx:2686739209:1 | Newfoundland Labrador Liquor Corporation | Cleaning Services - Corporate Offices |  |  |  | https://www.merx.com/govnl/nlliquorcorp/solicitations/Cleaning-Services-Corporate-Offices/0000259615?origin=0 |
| canada_federal:dfo-mpo:4500064602 | Fisheries and Oceans Canada | Contracted building cleaning | 107595.04 |  |  | https://search.open.canada.ca/contracts/record/dfo-mpo,C-2023-2024-Q4-02271 |
| canada_federal:nrc-cnrc:1003963 | National Research Council Canada | Contracted building cleaning | 500231.24 |  |  | https://search.open.canada.ca/contracts/record/nrc-cnrc,C-2022-2023-Q4-00825 |

## Open questions for hand research (layer 2)

- the vendor's GST/HST number (BN9)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
