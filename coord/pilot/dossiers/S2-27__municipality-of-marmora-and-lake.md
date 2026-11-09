# S2-27 — Municipality of Marmora and Lake ⇄ Baker Tilly KDN LLP

Stratum: **S2_complete_no_published_PO_rule** · pay on sight: yes — reference rule not published (quote the buyer's PO / order number when one is issued) · channel tier 2 · AP grade B · missing: (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: The Municipality of Marmora and Lake (schema.org JSON-LD legalName on https://marmoraandlake.ca/) — 12 Bursthall Street, P.O. Box 459, Marmora, ON, K0K 2M0
SUBMIT TO: treasurer@marmoraandlake.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: BAKER TILLY KDN LLP (as registered: Canada's Business Registries, ON 1000850218, 2026-11-08) — 272 Charlotte Street, Peterborough, ON, K9J 2V4, Canada | GST/HST 864673058 (Canada's Business Registries, ON 1000850218, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https: | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: paid in full within 14 calendar days (as printed on https://marmoraandlake.ca/tax-sales, re-read 202
DESCRIPTION: Municipality of Marmora and Lake (organisation (type not stated in the record), jurisdiction not stated) — public contract / purchase award 
```

## Relationship
- **rank_group**: B3
- **data_quality_score**: 80
- **ship_ready**: yes (finance mailbox, not AP)
- **sensitivity_flag**: no
- **evidence_age_days**: 1
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Municipality of Marmora and Lake (organisation (type not stated in the record), jurisdiction not stated) — public contract / purchase award in the last 12 months (dated record): Baker Tilly KDN LLP | awarded 2026-10-27 | published by: auditor of record (Ontario FIR 2025 Schedule 02) | record: https://efis.fma.csc.gov.on.ca/fir/wp-content/uploads/fir-files/reports-and-dashboards/by-year-and-municipality/2025//FI251241%20Marmora%20and%20Lake%20M.zip | vendor in Canada because: auditor of record (Ontario FIR 2025 Schedule 02)=Baker Tilly KDN LLP 17 Queen Street PO Box 87 Cobourg, ON K9A 4K2 | status rule: likely active (record dated in the last 12 months: auditor of record (Ontario FIR 2025 Schedule 02))
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: lead:f8c148cdc031e53a
- **tier**: B
- **grade**: 3
- **records_with_this_vendor**: 1 (relationship record: auditor of record (Ontario FIR 2025 Schedule 02); 0 in the contract dataset)

## Buyer
- **buyer**: Municipality of Marmora and Lake
- **buyer_website**: https://marmoraandlake.ca/
- **buyer_address**: 12 Bursthall Street, P.O. Box 459, Marmora, ON, K0K 2M0
- **buyer_phone**: 613-472-2629
- **buyer_contact_evidence_url**: https://marmoraandlake.ca/contact
- **buyer_legal_name_as_published**: The Municipality of Marmora and Lake (schema.org JSON-LD legalName on https://marmoraandlake.ca/)
- **buyer_logo_url**: https://images.squarespace-cdn.com/content/v1/59a0699b9f8dceeab4199b53/1547734618877-JF8I1I1DO4WUYYU8MJH7/Marmora-and-Lake-Logo_vector_2019_1500px.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/marmoraandlake/
- **buyer_type**: municipality / local government (from the organisation's name / web domain)
- **buyer_sector**: government: municipal
- **buyer_municipal_tier**: Lower Tier (within Hastings; Ontario MMAH list) (provincial municipal directory: https://data.ontario.ca/dataset/62e83cbc-0731-4d66-abdc-2f2b31bcd76c/resource/6783a586-6b05-4a73-9663-e60a6963c91e/download/municipalities_-_en_2026-0526.csv, 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://marmoraandlake.ca/contact (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Note: A municipality is not a government for purposes of the GST/HST"); charge GST/HST; derived from buyer type, not published by the buyer
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: treasurer@marmoraandlake.ca
- **email_type**: finance/accounting dept or supplier-payment office
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); finance mailbox
- **email_evidence_url**: https://marmoraandlake.ca/finance
- **email_evidence_quote**: ices Council Community News Contact Municipal Services Council Community News Contact Finance Department NANCY SINCLAIR Municipal Treasurer treasurer@marmoraandlake.ca 613-472-2629 ext. 2222 change of address form EBilling sign up form The Finance Department has the responsibility for coll
- **email_evidence_context**: Finance — Municipality of Marmora and Lake Municipal Services Council Community News Contact Municipal Services Council Community News Contact Finance Department NANCY SINCLAIR Municipal Treasurer treasurer@marmoraandlake.ca 613-472-2629 ext. 2222 change of address form EBilling sign up form The Finance Department has the responsibility for collection of property taxes, utility (water and sewer) billings and other revenues, coordination of the operating and capital budg (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: treasurer@marmoraandlake.ca (finance/accounting dept or supplier-payment office) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08 | page: https://marmoraandlake.ca/finance | quote: "ices Council Community News Contact Municipal Services Council Community News Contact Finance Department NANCY SINCLAIR Municipal Treasurer treasurer@marmoraand" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00486
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1; p=quarantine; fo=1;
- **dmarc_record_domain**: marmoraandlake.ca
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 include:spf.protection.outlook.com -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_phone**: 613-472-2629 ext. 2222 (as printed on https://marmoraandlake.ca/finance, re-read 2026-11-08)
- **payment_terms_as_published**: paid in full within 14 calendar days (as printed on https://marmoraandlake.ca/tax-sales, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "payment_terms": "paid in full within 14 calendar days (as printed on https://marmoraandlake.ca/tax-sales, re-read 2026-11-08)", "ap_phone": "613-472-2629 ext. 2222 (as printed on https://marmoraandlake.ca/finance, re-read 2026-11-08)"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 2
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: The Municipality of Marmora and Lake (schema.org JSON-LD legalName on https://marmoraandlake.ca/) — 12 Bursthall Street, P.O. Box 459, Marmora, ON, K0K 2M0 ⏎ SUBMIT TO: treasurer@marmoraandlake.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: BAKER TILLY KDN LLP (as registered: Canada's Business Registries, ON 1000850218, 2026-11-08) — 272 Charlotte Street, Peterborough, ON, K9J 2V4, Canada | GST/HST 864673058 (Canada's Business Registries, ON 1000850218, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https: | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: paid in full within 14 calendar days (as printed on https://marmoraandlake.ca/tax-sales, re-read 202 ⏎ DESCRIPTION: Municipality of Marmora and Lake (organisation (type not stated in the record), jurisdiction not stated) — public contract / purchase award 
- **invoice_card_json**: {"bill_to": {"legal_name": "The Municipality of Marmora and Lake (schema.org JSON-LD legalName on https://marmoraandlake.ca/)", "legal_name_is_published": true, "address": "12 Bursthall Street, P.O. Box 459, Marmora, ON, K0K 2M0", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "treasurer@marmoraandlake.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "paid in full within 14 calendar days (as printed on https://marmoraandlake.ca/tax-sales, re-read 2026-11-08)", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.can", "buyer_tax_status_is_published": false, "indicative_rate": "HST 13% (Ontario)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "864673058RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_na
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id)
- **ap_grade**: B
- **ap_score**: 69
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; payment terms published; currency known; AP phone or AP contact | missing: invoicing / AP mailbox; PO rule published; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: Baker Tilly KDN LLP
- **vendor_legal_name**: BAKER TILLY KDN LLP (as registered: Canada's Business Registries, ON 1000850218, 2026-11-08)
- **vendor_registry_id**: 1000850218 (ON)
- **vendor_registry_url**: https://ised-isde.canada.ca/cbr-rec/en/search?q=Baker%20Tilly%20KDN%20LLP
- **vendor_registered_address**: Peterborough, Ontario (registered office city / province; Canada's Business Registries, ON 1000850218, 2026-11-08)
- **vendor_legal_form**: LIMITED PARTNERSHIP ON (Canada's Business Registries, ON 1000850218, 2026-11-08)
- **vendor_address**: 272 Charlotte Street, Peterborough, ON, K9J 2V4, Canada
- **vendor_country_basis**: auditor of record (Ontario FIR 2025 Schedule 02)=Baker Tilly KDN LLP 17 Queen Street PO Box 87 Cobourg, ON K9A 4K2
- **vendor_bn9**: 864673058 (Canada's Business Registries, ON 1000850218, 2026-11-08)
- **vendor_gst_hst_derived**: 864673058RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://www.bakertilly.ca/
- **vendor_emails**: info@bakertilly.ca
- **vendor_phone**: (902) 404-4000
- **vendor_contact_evidence_url**: https://www.bakertilly.ca/locations
- **vendor_logo_url**: https://www.bakertilly.ca/assets/images/logo.svg
- **vendor_website_basis**: found by a web search, confirmed by reading the site on 2026-11-08: https://www.bakertilly.ca/ (Baker Tilly Canada | Canadian audit, tax, and advisory solutions. Skip to main content this.$refs.searchInput.focus()) }, closeSearch() { this.searchVisible = f)
- **vendor_facts_provenance**: name and address: the record's vendor block (auditor of record (Ontario FIR 2025 Schedule 02)); registry identity: 1000850218 (ON) status Active — registered (Canada's Business Registries, ON 1000850218, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: registry: Canada's Business Registries, ON 1000850218, 2026-11-08; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2024-04-02; phone / role e-mails / logo: the vendor's own site, https://www.bakertilly.ca/locations (tools/org_contacts.py, org_extras.py); website: https://www.bakertilly.ca/
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Active — registered (Canada's Business Registries, ON 1000850218, 2026-11-08)
- **vendor_incorporation_date**: 2024-04-02
- **vendor_years_in_business**: 2.6 (since 2024-04-02, registry date)
- **vendor_bn_source**: registry: Canada's Business Registries, ON 1000850218, 2026-11-08

## Contract
- **contract_status**: likely active (record dated in the last 12 months: auditor of record (Ontario FIR 2025 Schedule 02))
- **award_date**: 2026-10-27
- **contract_link**: https://efis.fma.csc.gov.on.ca/fir/wp-content/uploads/fir-files/reports-and-dashboards/by-year-and-municipality/2025//FI251241%20Marmora%20and%20Lake%20M.zip
- **source**: auditor of record (Ontario FIR 2025 Schedule 02)
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: auditor of record (Ontario FIR 2025 Schedule 02); 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Note: A municipality is not a government for purposes of the GST/HST"); charge GST/HST; derived from buyer type, not published by the buyer
- **tax_rate_indicative_derived**: HST 13% (Ontario) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 864673058RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: yes — reference rule not published (quote the buyer's PO / order number when one is issued)
- **pay_on_sight_missing**: (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: The Municipality of Marmora and Lake (schema.org JSON-LD legalName on https://marmoraandlake.ca/) — 12 Bursthall Street, P.O. Box 459, Marmora, ON, K0K 2M0 ⏎ SUBMIT TO: treasurer@marmoraandlake.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: BAKER TILLY KDN LLP (as registered: Canada's Business Registries, ON 1000850218, 2026-11-08) — 272 Charlotte Street, Peterborough, ON, K9J 2V4, Canada | GST/HST 864673058 (Canada's Business Registries, ON 1000850218, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https: | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: paid in full within 14 calendar days (as printed on https://marmoraandlake.ca/tax-sales, re-read 202 ⏎ DESCRIPTION: Municipality of Marmora and Lake (organisation (type not stated in the record), jurisdiction not stated) — public contract / purchase award 
- **invoice_card_json**: {"bill_to": {"legal_name": "The Municipality of Marmora and Lake (schema.org JSON-LD legalName on https://marmoraandlake.ca/)", "legal_name_is_published": true, "address": "12 Bursthall Street, P.O. Box 459, Marmora, ON, K0K 2M0", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "treasurer@marmoraandlake.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "paid in full within 14 calendar days (as printed on https://marmoraandlake.ca/tax-sales, re-read 2026-11-08)", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.can", "buyer_tax_status_is_published": false, "indicative_rate": "HST 13% (Ontario)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "864673058RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_na
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id)
- **ap_grade**: B
- **ap_score**: 69
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; payment terms published; currency known; AP phone or AP contact | missing: invoicing / AP mailbox; PO rule published; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["treasurer@marmoraandlake.ca (finance/accounting dept or supplier-payment office)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08", "page: https://marmoraandlake.ca/finance", "quote: \"ices Council Community News Contact Municipal Services Council Community News Contact Finance Department NANCY SINCLAIR Municipal Treasurer treasurer@marmoraand\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00486"], "buyer_facts": ["address and phone: the buyer's own site, https://marmoraandlake.ca/contact (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (auditor of record (Ontario FIR 2025 Schedule 02))", "registry identity: 1000850218 (ON) status Active — registered (Canada's Business Regi

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://marmoraandlake.ca/finance | 2026-11-08 | ok |  |  |  | 613-472-2629 ext. 2222 |  |  |  |  |  |

## Buyer site facts (org_extras, marmoraandlake.ca)
- **status**: ok
- **pages**: 3
- **language**: en
- **logo_url**: https://images.squarespace-cdn.com/content/v1/59a0699b9f8dceeab4199b53/1547734618877-JF8I1I1DO4WUYYU8MJH7/Marmora-and-Lake-Logo_vector_2019_1500px.png
- **logo_basis**: logo image on the site
- **domain**: marmoraandlake.ca
- **key**: lead:f8c148cdc031e53a
- **name**: Municipality of Marmora and Lake
- **website**: https://marmoraandlake.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_legal_name**: The Municipality of Marmora and Lake
- **jsonld_phone**: 613-472-2629
- **jsonld_same_as**: https://www.facebook.com/MarmoraAndLake/; https://twitter.com/MarmoraandLake; https://www.youtube.com/channel/UCoqnOpIVVJIZ8EAoYjP0ICg; https://www.linkedin.com/company/marmoraandlake/
- **jsonld_quote**: {"address":"Marmora and Lake, Ontario\nCanada","image":"https://static1.squarespace.com/static/59a0699b9f8dceeab4199b53/t/5c408e5a7ba7fc1e4305aa68/1793989675606/","name":"The Municipality of Marmora and Lake","openingHours":", ","@context":"http://schema.org","@type":"LocalBusiness"}
- **jsonld_page**: https://marmoraandlake.ca/
- **linkedin_url**: https://www.linkedin.com/company/marmoraandlake/
- **tel_links**: 613-472-2629

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "address": "12 Bursthall Street, P.O. Box 459, Marmora, ON, K0K 2M0", "address_country": "CA", "address_url": "https://marmoraandlake.ca/contact", "address_method": "pattern", "address_quote": "ontact Contact Municipal Office 12 Bursthall Street, P.O. Box 459, Marmora, ON, K0K 2M0 Call: 613-472-2629 or 1-866-518-2282 Fax: 613-472-5330 Hours Monday to Friday", "phone": "613-472-2629", "phone_url": "https://marmoraandlake.ca/contact", "emails": "ar@marmoraandlake.ca; service@marmoraandlake.ca", "emails_url": "https://marmoraandlake.ca/contact", "domain": "marmoraandlake.ca", "key": "lead:f8c148cdc031e53a", "name": "Municipality of Marmora and Lake", "website": "https://marmoraandlake.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, bakertilly.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://www.bakertilly.ca/assets/images/logo.svg
- **logo_basis**: logo image on the site
- **domain**: bakertilly.ca
- **key**: lead:7bc22d4cc3b6b17d
- **name**: Unlocking the highest value
- **website**: https://bakertilly.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: LocalBusiness
- **jsonld_name**: Baker Tilly Canada
- **jsonld_alternate_name**: BTI
- **jsonld_logo**: https://bti-global.transforms.svdcdn.com/production/network/canada/images/logos/Growth-symbol_Charcoal-RGB.jpg?w=600&h=600&q=82&fm=png&fit=max&dm=1727186527&s=a1012d09fd6f6cf603b582d82e80867b
- **jsonld_url**: https://www.bakertilly.ca
- **jsonld_quote**: {"@context":"https://schema.org","@graph":[{"@type":"WebSite","author":{"@id":"https://www.bakertilly.ca#identity"},"copyrightHolder":{"@id":"https://www.bakertilly.ca#identity"},"copyrightYear":"2025","creator":{"@id":"#creator"},"dateCreated":"2025-01-30T08:26:44-05:00","dateModified":"2026-11-06T
- **jsonld_page**: https://www.bakertilly.ca/
- **mentions**: {'payment_method': {'text': 'interactions or transactions with Baker Tilly or otherwise receive the full benefit of', 'url': 'https://www.bakertilly.ca/privacy-policy', 'quote': 'and on reasonable notice to Baker Tilly, but you then may not be able to proceed with your intended interactions or transactions with Baker Tilly or otherwise receive the full benefit of Baker Tilly’s products and services. Please refer to section 7 of this Pr'}}
- **linkedin_url**: https://www.linkedin.com/company/baker-tilly-canada/

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "130 Eileen Stubbs Ave, Suite 201, Dartmouth, NS, B3B 2C4", "address_country": "CA", "address_url": "https://www.bakertilly.ca/locations", "address_method": "pattern", "address_quote": "chewan Nationwide National office 130 Eileen Stubbs Ave Suite 201 Dartmouth, NS B3B 2C4 (902) 404-4000 info@bakertilly.ca Baker Tilly Canada Capital Corporation 900-40", "phone": "(902) 404-4000", "phone_url": "https://www.bakertilly.ca/locations", "emails": "info@bakertilly.ca", "emails_url": "https://www.bakertilly.ca/locations", "domain": "bakertilly.ca", "key": "lead:7bc22d4cc3b6b17d", "name": "Unlocking the highest value", "website": "https://bakertilly.ca/", "kind": "buyer", "date": "2026-11-04"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Unlocking the highest value |  |  |  |  |  |  |  |  |  |  |
| b | Municipality of Marmora and Lake |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:f8c148cdc031e53a",
 "ap_contact_team": {
  "emails": [
   "treasurer@marmoraandlake.ca",
   "clerk@marmoraandlake.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "treasurer@marmoraandlake.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://marmoraandlake.ca/finance",
    "quote": "ices Council Community News Contact Municipal Services Council Community News Contact Finance Department NANCY SINCLAIR Municipal Treasurer treasurer@marmoraandlake.ca 613-472-2629 ext. 2222 change of address form EBilling sign up form The Finance Department has the responsibility for coll",
    "retrieved_date": "2026-11-03",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Municipality of Marmora and Lake",
    "task_id": "CL-SM-00197"
   },
   {
    "email": "treasurer@marmoraandlake.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://marmoraandlake.ca/finance",
    "quote": "ices Council Community News Contact Municipal Services Council Community News Contact Finance Department NANCY SINCLAIR Municipal Treasurer treasurer@marmoraandlake.ca 613-472-2629 ext. 2222 change of address form EBilling sign up form The Finance Department has the responsibility for coll",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Municipality of Marmora and Lake",
    "task_id": "CL-WS-00486"
   },
   {
    "email": "clerk@marmoraandlake.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://marmoraandlake.ca/contact",
    "quote": "613-472-2629 ext. 2221 KRISTEN MCCONNELL Municipal Clerk clerk@marmoraandlake.ca 613-472-2629 ext. 2232 AMANDA LABOSSIERE Finance & Legislative Services Assistant",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Municipality of Marmora and Lake",
    "task_id": "CL-WS-00486"
   },
   {
    "email": "treasurer@marmoraandlake.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://marmoraandlake.ca/announcements/2025/8/28/sale-of-land-by-public-tender",
    "quote": "reasurer The Corporation of the Municipality of Marmora and Lake 12 Bursthall St., P.O. Box 459 Marmora, ON K0K 2M0 613-472-2629, Ext. 2222 treasurer@marmoraandlake.ca www.marmoraandlake.ca Kristen McConnell August 28, 2025 Facebook 0 0 Likes Previous No Trespassing on Land for Sale by Pub",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Municipality of Marmora and Lake",
    "task_id": "CL-WS-00431"
   }
  ]
 },
 "research_status": {
  "found": 4
 },
 "queries_tried": [
  "site crawl of marmoraandlake.ca (26 pages, robots.txt respected), no AI, no search engine",
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

## The vendor's other buyers in the dataset (first 60 of 9)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_bidsandtenders:f3a070d2-5349-435b-aaa0-62f529a829bf:1 | Township of Douro-Dummer | Financial Audit Services |  |  |  | https://dourodummer.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/f3a070d2-5349-435b-aaa0-62f529a829bf |
| ca_bidsandtenders:92388fee-5a36-474f-bc2b-33291ab1822b:1 | Municipality of Dysart et al | External Audit Services |  |  |  | https://dysartetal.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/92388fee-5a36-474f-bc2b-33291ab1822b |
| ca_bidsandtenders:613331b8-63ea-4896-95b9-d457f50b4484:1 | Municipality of Trent Lakes | Auditing Services |  |  |  | https://trentlakes.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/613331b8-63ea-4896-95b9-d457f50b4484 |
| ca_bidsandtenders:c1512b97-f488-40e6-99e9-a4a63582cb0f:1 | Loyalist Township | Financial Audit Services |  |  |  | https://loyalist.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/c1512b97-f488-40e6-99e9-a4a63582cb0f |
| ca_bidsandtenders:cd09c3b9-e6d5-49b6-bedf-bad4fe66fa58:1 | Peterborough Victoria Northumberland and Clarington Catholic District School Board | External Auditing Services |  |  |  | https://pvnccdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/cd09c3b9-e6d5-49b6-bedf-bad4fe66fa58 |
| ca_bidsandtenders:1dce5bd9-b5e8-40c4-a340-0e6bd57ba3d2:1 | City Of Peterborough | Audit Services |  |  |  | https://cityofpeterborough.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/1dce5bd9-b5e8-40c4-a340-0e6bd57ba3d2 |
| ca_bidsandtenders:b8cf84c5-4167-4105-b571-5592c583c50e:1 | County of Simcoe | External Audit Services |  |  |  | https://simcoecounty.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/b8cf84c5-4167-4105-b571-5592c583c50e |
| ca_bidsandtenders:bb3f28af-8020-4976-bb8f-75201a7beae5:1 | Township of Springwater | External Audit Services |  |  |  | https://springwater.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/bb3f28af-8020-4976-bb8f-75201a7beae5 |
| ca_bidsandtenders:c7eb4d73-8fb6-47fb-856a-4c3271129e9d:1 | Durham Catholic District School Board | External Audit Services |  |  |  | https://dcdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/c7eb4d73-8fb6-47fb-856a-4c3271129e9d |

## Open questions for hand research (layer 2)

- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
