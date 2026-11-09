# S5-42 — BANK OF ENGLAND ⇄ CanDeal.ca, Inc.

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 1 · AP grade B · missing: the vendor's GST/HST number (BN9)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Bank of England (provincial municipal directory: https://www.gov.uk/api/organisations?page=4, 2026-11-08) — Threadneedle Street, LONDON, EC2R 8AH, England
SUBMIT TO: financedivisionpaymentsteam@bankofengland.co.uk (invoicing/AP mailbox, confirmed by the referee)
REFERENCE: contract CON/1001115 (tender_id) — the source publishes the award under this tender / notice number and no separate contract number; tender CON/1001115 (tender_id) | PO rule: not published
FROM / REMIT TO: CanDeal.ca, Inc. — 50 Bay Street, Suite 1200, Toronto, Ontario, M5J 3A5 | GST/HST number not public
TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); UK VAT is | CURRENCY: GBP | TERMS: within 30 days
DESCRIPTION: Candeal Subscription Licenses | AMOUNT: 77,059.00 GBP
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 88
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 0
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: BANK OF ENGLAND (company (private sector), UK) — public contract / purchase award with a published end date (dated record): CanDeal.ca, Inc. | subject: Candeal Subscription Licenses | instrument: contract | contract number: CON/1001115 (tender_id) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference | solicitation: CON/1001115 (tender_id) | all identifiers: {"ocid": "ocds-b5fd17-28677ccb-f2e8-46ea-a565-c0102b434930", "award_id": "ocds-b5fd17-28677ccb-f2e8-46ea-a565-c0102b434930-1", "notice_guid": "6f72f272-7a7f-4613-b3fd-c2f24b75cbad", "tender_id": "CON/1001115", "compiled_release_id": "ocds-b5fd17-28677ccb-f2e8-46ea-a565-c0102b434930-2023-09-20T13:03: | value: 77059.0 GBP | awarded 2023-06-01, start 2023-06-01, end 2027-05-31 | published by: Contracts Finder (UK) - OCDS award notices | record: https://www.contractsfinder.service.gov.uk/Notice/6f72f272-7a7f-4613-b3fd-c2f24b75cbad | vendor in Canada because: address.streetAddress has Canadian postal code pattern + province | status rule: active (published end date today or later) | this buyer has 1 records with Canada-located vendors (1 distinct vendors; 0 in the last 12 months; latest 2023-06-01)
- **how_relationship_was_found**: the award record was harvested from the public procurement source named in `source` (scripts/<source> pipeline), matched to the buyer by its canonical name/key, and the vendor's Canada location read from the source's own vendor address/country field (`vendor_country_basis`)
- **keys**: b:dac6dcd3c14e2d02
- **tier**: A
- **grade**: 4
- **records_with_this_vendor**: 1

## Buyer
- **buyer**: BANK OF ENGLAND
- **buyer_website**: https://www.gov.uk/government/organisations/bank-of-england
- **buyer_address**: Threadneedle Street, LONDON, EC2R 8AH, England
- **buyer_legal_name_as_published**: Bank of England (provincial municipal directory: https://www.gov.uk/api/organisations?page=4, 2026-11-08)
- **buyer_logo_url**: https://www.gov.uk/assets/frontend/govuk-icon-180-d45a306f0549414cfa5085f16e4a3816a77558b139e5bc226f23162d1d0decb0.png
- **buyer_type**: company (private sector)
- **buyer_sector**: private sector
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q183231; central bank; business; printing company
- **buyer_founded**: 1694-07-27; 1694-00-00 (Wikidata Q183231, exact name match + country + organisation claims; 2026-11-08)
- **buyer_facts_provenance**: address: the buyer's record / buyer table; legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; invoicing requirements: the lane's AP page (https://www.bankofengland.co.uk/contact/supplying-goods-and-services/invoicing-and-po-policies); payment terms: the lane's AP page (https://www.bankofengland.co.uk/contact/supplying-goods-and-services/invoicing-and-po-policies)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); UK VAT is accounted for by the buyer under the reverse charge where applicable
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: financedivisionpaymentsteam@bankofengland.co.uk
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.bankofengland.co.uk/contact/supplying-goods-and-services/invoicing-and-po-policies
- **email_evidence_quote**: Supplier invoices are required to be submitted to the Bank via the email address financedivisionpaymentsteam@bankofengland.co.uk.
- **mailbox_provenance**: financedivisionpaymentsteam@bankofengland.co.uk (invoicing/AP) | researched by the ChatGPT/Codex agent (lane chatgpt) (page opened and quoted) on 2026-11-09 | page: https://www.bankofengland.co.uk/contact/supplying-goods-and-services/invoicing-and-po-policies | quote: "Supplier invoices are required to be submitted to the Bank via the email address financedivisionpaymentsteam@bankofengland.co.uk." | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: not checked yet | DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by not checked | lane file: chatgpt/chatgpt_verify_buyer_ap_results_batch01.csv task CH-VF-00083
- **email_deliverability**: not checked yet
- **email_security_posture**: DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by not checked
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject; rua=mailto:24d91a69e293813@rep.dmarcanalyzer.com; ruf=mailto:dmarc@bankofengland.co.uk; pct=100; fo=1
- **dmarc_record_domain**: bankofengland.co.uk
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 include:b52694b4-spf.mta.getcheckrecipient.com include:eu._netblocks.mimecast.com include:servers.mcsv.net include:_spf1.bankofengland.co.uk include:_spf.qualtrics.com include:spf.protection.outlook.com include:spf1.worldapp.com ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements**: Email invoices as attachments. No PO, no payment. Include the Bank’s valid Official Order Reference, invoice number, supplier name, address and VAT number, supply and issue dates, description, and customer name and address. The Bank aims to pay undisputed invoices with a valid PO within 30 days. Its
- **payment_terms_as_published**: within 30 days
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "payment_terms": "within 30 days", "requirements_text": "Email invoices as attachments. No PO, no payment. Include the Bank’s valid Official Order Reference, invoice number, supplier name, address and VAT number, supply and issue dates, description, and customer name and address. The Bank aims to pay undisputed invoices with a valid PO within 30 days. Its"}
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Bank of England (provincial municipal directory: https://www.gov.uk/api/organisations?page=4, 2026-11-08) — Threadneedle Street, LONDON, EC2R 8AH, England ⏎ SUBMIT TO: financedivisionpaymentsteam@bankofengland.co.uk (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: contract CON/1001115 (tender_id) — the source publishes the award under this tender / notice number and no separate contract number; tender CON/1001115 (tender_id) | PO rule: not published ⏎ FROM / REMIT TO: CanDeal.ca, Inc. — 50 Bay Street, Suite 1200, Toronto, Ontario, M5J 3A5 | GST/HST number not public ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); UK VAT is | CURRENCY: GBP | TERMS: within 30 days ⏎ DESCRIPTION: Candeal Subscription Licenses | AMOUNT: 77,059.00 GBP
- **invoice_card_json**: {"bill_to": {"legal_name": "Bank of England (provincial municipal directory: https://www.gov.uk/api/organisations?page=4, 2026-11-08)", "legal_name_is_published": true, "address": "Threadneedle Street, LONDON, EC2R 8AH, England", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "financedivisionpaymentsteam@bankofengland.co.uk", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "CON/1001115 (tender_id) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: CON/1001115 (tender_id) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference — source uk_contracts_finder"}, "terms": {"payment_terms": "within 30 days", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); UK VAT is", "buyer_tax_status_is_published": false, "indicative_rate": "
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; vendor GST/HST number; vendor legal name; AP phone or contact for follow-up
- **ap_grade**: B
- **ap_score**: 68
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; bill-to legal name published; invoice or billing address; payment terms published; currency known; invoice format / requirements published | missing: finance mailbox; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); PO rule published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: a mailbox on the buyer's own domain or published on its own site; MX record for the mailbox domain; published PO rule
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms published
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: contract or agreement number: CON/1001115 (tender_id) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference — source uk_contracts_finder

## Vendor
- **vendor**: CanDeal.ca, Inc.
- **vendor_address**: 50 Bay Street, Suite 1200, Toronto, Ontario, M5J 3A5
- **vendor_country_basis**: address.streetAddress has Canadian postal code pattern + province
- **vendor_facts_provenance**: name and address: the record's vendor block (Contracts Finder (UK) - OCDS award notices)
- **vendor_concentration_top_share**: CanDeal.ca, Inc.: 100% of 1 records
- **vendor_registry_match_level**: weak_candidates_only

## Contract
- **contract_status**: active (published end date today or later)
- **contract_reference**: {"ocid": "ocds-b5fd17-28677ccb-f2e8-46ea-a565-c0102b434930", "award_id": "ocds-b5fd17-28677ccb-f2e8-46ea-a565-c0102b434930-1", "notice_guid": "6f72f272-7a7f-4613-b3fd-c2f24b75cbad", "tender_id": "CON/1001115", "compiled_release_id": "ocds-b5fd17-28677ccb-f2e8-46ea-a565-c0102b434930-2023-09-20T13:03:57+01:00"}
- **contract_title**: Candeal Subscription Licenses
- **contract_description**: Provision of Candeal Subscription Licenses.
- **contract_or_agreement_number**: CON/1001115 (tender_id) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference
- **solicitation_or_tender_number**: CON/1001115 (tender_id)
- **award_or_notice_id**: ocds-b5fd17-28677ccb-f2e8-46ea-a565-c0102b434930-1 (award_id); ocds-b5fd17-28677ccb-f2e8-46ea-a565-c0102b434930-2023-09-20T13:03:57+01:00 (compiled_release_id); ocds-b5fd17-28677ccb-f2e8-46ea-a565-c0102b434930 (ocid); 6f72f272-7a7f-4613-b3fd-c2f24b75cbad (notice_guid)
- **commodity_codes**: CPV 48000000 (Software package and information systems)
- **contract_value**: 77059.0
- **currency**: GBP
- **award_date**: 2023-06-01
- **start_date**: 2023-06-01
- **end_date**: 2027-05-31
- **contract_link**: https://www.contractsfinder.service.gov.uk/Notice/6f72f272-7a7f-4613-b3fd-c2f24b75cbad
- **source**: Contracts Finder (UK) - OCDS award notices
- **contracts_with_canadian_suppliers**: 1
- **records_last_12_months**: 0
- **record_sources**: Contracts Finder (UK) - OCDS award notices (1)
- **records_with_this_vendor**: 1
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); UK VAT is accounted for by the buyer under the reverse charge where applicable

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Bank of England (provincial municipal directory: https://www.gov.uk/api/organisations?page=4, 2026-11-08) — Threadneedle Street, LONDON, EC2R 8AH, England ⏎ SUBMIT TO: financedivisionpaymentsteam@bankofengland.co.uk (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: contract CON/1001115 (tender_id) — the source publishes the award under this tender / notice number and no separate contract number; tender CON/1001115 (tender_id) | PO rule: not published ⏎ FROM / REMIT TO: CanDeal.ca, Inc. — 50 Bay Street, Suite 1200, Toronto, Ontario, M5J 3A5 | GST/HST number not public ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); UK VAT is | CURRENCY: GBP | TERMS: within 30 days ⏎ DESCRIPTION: Candeal Subscription Licenses | AMOUNT: 77,059.00 GBP
- **invoice_card_json**: {"bill_to": {"legal_name": "Bank of England (provincial municipal directory: https://www.gov.uk/api/organisations?page=4, 2026-11-08)", "legal_name_is_published": true, "address": "Threadneedle Street, LONDON, EC2R 8AH, England", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "financedivisionpaymentsteam@bankofengland.co.uk", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "CON/1001115 (tender_id) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: CON/1001115 (tender_id) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference — source uk_contracts_finder"}, "terms": {"payment_terms": "within 30 days", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); UK VAT is", "buyer_tax_status_is_published": false, "indicative_rate": "
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; vendor GST/HST number; vendor legal name; AP phone or contact for follow-up
- **ap_grade**: B
- **ap_score**: 68
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; bill-to legal name published; invoice or billing address; payment terms published; currency known; invoice format / requirements published | missing: finance mailbox; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); PO rule published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: a mailbox on the buyer's own domain or published on its own site; MX record for the mailbox domain; published PO rule
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms published
- **facts_provenance_json**: {"mailbox": ["financedivisionpaymentsteam@bankofengland.co.uk (invoicing/AP)", "researched by the ChatGPT/Codex agent (lane chatgpt) (page opened and quoted) on 2026-11-09", "page: https://www.bankofengland.co.uk/contact/supplying-goods-and-services/invoicing-and-po-policies", "quote: \"Supplier invoices are required to be submitted to the Bank via the email address financedivisionpaymentsteam@bankofengland.co.uk.\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: not checked yet", "DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by not checked", "lane file: chatgpt/chatgpt_verify_buyer_ap_results_batch01.csv task CH-VF-00083"], "buyer_facts": ["address: the buyer's record / buyer table", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "invoicing requirements: the lane's AP page (https://www.bankofengland.co.uk/contact/supplying-goods-and-services/invoicing-and-po-policies)", "payment terms: the lane's AP page (https://www.bankofengland.co.uk/contact/supplying-goods-and-services/invoicing-and-po-policies)"], "vendor_facts": ["name and address: the record's vendor block (Contracts Finder (UK) - OCDS award notices)"], "relationship": "the award record was harvested from the public procurement source named in `source` (scripts/<source> pipeline), matched to the buyer by its canonical name/key, and the vendor's C

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.gov.uk/government/organisations/ministry-of-justice/about/procurement | 2026-11-08 | ok | paid within 5 days % of invoices paid within 30 days | yes (as published: Purchase order numbers need) |  |  |  | pdf file format |  | included: its prompt payment data will be published on the GFSL pages . 2025-2026 Financial year 2025/2026 % of invoices paid within 5 days % of invoices paid within 30 days Total Amount of Liability to Pay (£) First qua | these aren’t in place, we require orders to be supported by a purchase order before you provide any goods or services to the MOJ. Purchase order numbers need to be quoted on your invoice, and this will avoid any delays t |
| https://www.gov.uk/government/organisations/cabinet-office/about/procurement | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |
| https://www.gov.uk/government/organisations/the-coal-authority/about/complaints-procedure | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |
| https://www.gov.uk/government/organisations/ministry-of-defence/about/procurement | 2026-11-08 | ok | paid within 30 days |  |  |  |  |  |  | to pay 90% of undisputed and valid invoices from SMEs within 5 days. Additionally, 100% of all undisputed and valid invoices should be paid within 30 days. MOD’s supplier payment information can be found here . For FY 20 |  |
| https://www.gov.uk/government/organisations/home-office/about/procurement | 2026-11-08 | ok |  | yes (as published: No purchase order, no payment) | Jaggaer |  |  |  |  |  | for new businesses, entrepreneurs, start-ups, SMEs, VCSEs and mutuals Social value in procurement Information security eSourcing No purchase order, no payment: how to ensure your invoice is not rejected Summary Invoicing |
| https://www.gov.uk/government/organisations/intellectual-property-office | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |
| https://www.gov.uk/government/organisations/competition-and-markets-authority/about/procurement | 2026-11-08 | ok |  | yes (as published: quotes a valid CMA purchase order) |  |  |  |  |  |  | 30 days, through the inclusion of a contractual condition in the prime contract. Invoicing us Please ensure that your invoice quotes a valid CMA purchase order reference. You should email your invoice to Invoices@cma.gov |
| https://www.gov.uk/government/publications/crown-representatives-and-strategic-suppliers | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |
| https://www.gov.uk/government/publications/procurement-act-2023-guidance-documents-plan-phase/guidance-transitional-and-saving-arrangements-html | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |
| https://www.gov.uk/government/organisations/uk-hydrographic-office/about/procurement | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, gov.uk)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://www.gov.uk/assets/frontend/govuk-icon-180-d45a306f0549414cfa5085f16e4a3816a77558b139e5bc226f23162d1d0decb0.png
- **logo_basis**: site icon (apple-touch-icon)
- **domain**: gov.uk
- **key**: b:94e501dfe24f7926
- **name**: Ministry of Justice
- **website**: https://gov.uk/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: GOV.UK
- **jsonld_logo**: https://www.gov. .png
- **jsonld_url**: https://www.gov.uk
- **jsonld_quote**: { "@context": "http://schema.org", "@type": "BreadcrumbList", "itemListElement": [ { "@type": "ListItem", "position": 1, "item": { "name": "Home", "@id": "https://www.gov.uk/" } } ] }
- **jsonld_page**: https://www.gov.uk/help/privacy-notice
- **legal_name_stated**: Real User Monitoring
- **legal_name_stated_url**: https://www.gov.uk/help/privacy-notice
- **legal_name_stated_quote**: s and page tagging techniques Where you provide your consent, we use Google Analytics cookies and a Real User Monitoring ( RUM ) cookie from SpeedCurve to collect information about how you use GOV.UK. Google Analytics pr

## Buyer role mailboxes found on its site (org_contacts)
_not read_

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
| b | OFCOM | Q1529532 | exact name match + country + organisation claims |  | Ofcom | Office of Communications | government agency |  | United Kingdom | 2003-00-00 | London |
| b | HM TREASURY |  |  |  |  |  |  |  |  |  |  |
| b | NHS Blood and Transplant | Q16957766 | exact name match + country + organisation claims |  | NHS Blood and Transplant | NHS Blood and Transplant | organization |  | United Kingdom | 2005-10-01 |  |
| b | Met Office | Q1851405 | official website on the organisation's domain (https://www.metoffice.gov.uk/) + name |  | Met Office | Met Office | meteorological service organization; governmental meteorological service; government agency |  | United Kingdom | 1854-08-01 | Exeter; Bracknell |
| b | National Highways | Q5760006 | exact name match + country + organisation claims |  | National Highways | National Highways | organization | state-owned enterprise | United Kingdom | 2015-00-00 | Birmingham Snow Hill |
| b | Network Rail |  |  |  |  |  |  |  |  |  |  |
| b | UK Hydrographic Office | Q2495231 | official website on the organisation's domain (https://gov.uk/ukho) + name |  | United Kingdom Hydrographic Office | Institut hydrographique du Royaume-Uni | government agency |  | United Kingdom | 1795-00-00 | Taunton |
| b | Government Commercial Agency | Q140984181 | official website on the organisation's domain (https://www.gca.gov.uk/) + name |  | Government Commercial Agency |  | government agency |  | United Kingdom | 2026-04-01 |  |
| b | The Minister for the Cabinet Office acting through Crown Commercial Service |  |  |  |  |  |  |  |  |  |  |
| b | UK Atomic Energy Authority |  |  |  |  |  |  |  |  |  |  |
| b | Defence Science and Technology Laboratory | Q5251253 | official website on the organisation's domain (http://www.dstl.gov.uk/) + name |  | Defence Science and Technology Laboratory | Defence Science and Technology Laboratory | government agency; Executive  agency |  | United Kingdom | 2001-07-02 | Porton Down |
| b | BRITISH COUNCIL(THE) |  |  |  |  |  |  |  |  |  |  |
| b | Ministry of Defence, Information Systems and Services, ISS Commercial Sourcing Team |  |  |  |  |  |  |  |  |  |  |
| b | Home Office |  |  |  |  |  |  |  |  |  |  |
| b | Invest Northern Ireland |  |  |  |  |  |  |  |  |  |  |
| b | Crown Commercial Service | Q5589070 | official website on the organisation's domain (http://gps.cabinetoffice.gov.uk) + name |  | Crown Commercial Service |  | central purchasing body; Executive  agency |  | United Kingdom | 1991-00-00 | Liverpool |
| b | Ministry of Defence, ISTAR, Chemical, Biological, Radiological and Nuclear Delivery Team (CBRN DT) |  |  |  |  |  |  |  |  |  |  |
| b | Department for Business and Trade |  |  |  |  |  |  |  |  |  |  |
| b | Ministry of Defence, Land Equipment, Soldier Systems Programme (SSP) |  |  |  |  |  |  |  |  |  |  |
| b | FCO Services | Q5424773 | official website on the organisation's domain (https://www.fcdoservices.gov.uk) + name |  | FCDO Services |  | government agency |  | United Kingdom | 2006-04-00 |  |
| b | Defence Equipment and Support | Q5251177 | official website on the organisation's domain (https://www.gov.uk/government/organisations/defence-equipment-and-support) + name |  | Defence Equipment and Support |  | government agency |  | United Kingdom | 2007-01-01 | Bristol |
| b | Ministry of Justice |  |  |  |  |  |  |  |  |  |  |
| b | Agriculture and Horticulture Development Board |  |  |  |  |  |  |  |  |  |  |
| b | Care Quality Commission | Q5038860 | exact name match + country + organisation claims |  | Care Quality Commission |  | non-departmental public body; regulatory agency |  | United Kingdom | 2009-00-00 | London |
| b | Maritime and Coastguard Agency | Q693667 | official website on the organisation's domain (https://www.gov.uk/government/organisations/maritime-and-coastguard-agency) + name |  | Maritime and Coastguard Agency | Maritime and Coastguard Agency | Executive  agency; sea rescue organization |  | United Kingdom |  | Southampton |
| b | BANK OF ENGLAND | Q183231 | exact name match + country + organisation claims |  | Bank of England | banque d'Angleterre | central bank; business; printing company |  | United Kingdom | 1694-07-27; 1694-00-00 | Bank of England building in London |
| b | Ministry of Defence |  |  |  |  |  |  |  |  |  |  |
| b | Cabinet Office | Q6865995 | official website on the organisation's domain (http://www.cabinetoffice.gov.uk/) + name |  | Minister for the Cabinet Office | ministre pour le Bureau du Cabinet | position; public office |  | United Kingdom |  |  |
| b | The Pensions Regulator | Q7756572 | official website on the organisation's domain (http://www.thepensionsregulator.gov.uk/) + name |  | The Pensions Regulator |  | non-departmental public body; registration authority |  | United Kingdom |  |  |
| b | HM Land Registry | Q5635120 | official website on the organisation's domain (https://www.gov.uk/government/organisations/land-registry) + name |  | HM Land Registry |  | non-ministerial government department; Land and Property Service Organization |  | United Kingdom | 1862-00-00 |  |
| b | Competition and Markets Authority | Q18363996 | official website on the organisation's domain (https://gov.uk/cma) + name |  | Competition and Markets Authority | Competition and Markets Authority | non-ministerial government department; competition regulator |  | United Kingdom | 2014-04-01; 2013-10-01 | Victoria House |
| b | Ministry of Defence, C&C, C&C |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "b:dac6dcd3c14e2d02",
 "ap_contact_team": {
  "emails": [
   "financedivisionpaymentsteam@bankofengland.co.uk",
   "finance.operations@bankofengland.co.uk"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": "Threadneedle Street, London EC2R 8AH, United Kingdom",
  "invoicing_requirements": "Email invoices as attachments. No PO, no payment. Include the Bank’s valid Official Order Reference, invoice number, supplier name, address and VAT number, supply and issue dates, description, and customer name and address. The Bank aims to pay undisputed invoices with a valid PO within 30 days. Its published standard terms provide 30 days from receipt of a valid undisputed invoice submitted monthly in arrears. The supplier portal tracks status only.",
  "evidence": [
   {
    "email": "financedivisionpaymentsteam@bankofengland.co.uk",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": "Email invoices as attachments. No PO, no payment. Include the Bank’s valid Official Order Reference, invoice number, supplier name, address and VAT number, supply and issue dates, description, and customer name and address. The Bank aims to pay undisputed invoices with a valid PO within 30 days. Its published standard terms provide 30 days from receipt of a valid undisputed invoice submitted monthly in arrears. The supplier portal tracks status only.",
    "applies_to": "whole_organisation",
    "page_url": "https://www.bankofengland.co.uk/contact/supplying-goods-and-services/invoicing-and-po-policies",
    "quote": "Supplier invoices are required to be submitted to the Bank via the email address financedivisionpaymentsteam@bankofengland.co.uk.",
    "retrieved_date": "2026-11-08",
    "found_by": "chatgpt",
    "verification": "verified",
    "source_file": "chatgpt_verify_buyer_ap_results_batch01.csv",
    "org": "Bank of England",
    "task_id": "CH-VF-00091"
   },
   {
    "email": "financedivisionpaymentsteam@bankofengland.co.uk",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": "NoPO/noPay: obtain validPO before starting; missingPO returnedunpaid. Invoice andqueryemails attachinvoice with officialorderref, uniqueinvoice#, suppliername/address/VAT#, supplydate, issuedate, goods/servicedescription andcustomername/address. Aim undisputedvalidPOinvoicepayment within30days submission. Linkedterms specify monthlyinarrears validinvoices for satisfactorilycompletedwork, net30receipt; detailedbreakdown/supportingdocuments asmanagerrequires. PricesexcludeVAT (paid onvalidVATinvoice), includeotherduties/deliverycosts. Lateundisputedinterest2%aboveBoEbase. Subcontractpaymentwithin30daysofvalidinvoice. OracleFusionSupplierPortal showsinvoice/paymentstatus but explicitlycannot acceptinvoices, queries ormessages; emailrequired.",
    "applies_to": "whole_organisation",
    "page_url": "https://www.bankofengland.co.uk/contact/supplying-goods-and-services/invoicing-and-po-policies",
    "quote": "Supplier invoices are required to be submitted to the Bank via the email address financedivisionpaymentsteam@bankofengland.co.uk . Invoice queries should be submitted to finance.operations@bankofengland.co.uk . Although the Supplier Portal allows for Suppliers",
    "retrieved_date": "2026-11-09",
    "found_by": "codex",
    "verification": "verified",
    "source_file": "codex_buyer_ap_results_batch04.csv",
    "org": "Bank of England",
    "task_id": "CO-AP-00381"
   },
   {
    "email": "finance.operations@bankofengland.co.uk",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": "Email invoices as attachments. No PO, no payment. Include the Bank’s valid Official Order Reference, invoice number, supplier name, address and VAT number, supply and issue dates, description, and customer name and address. The Bank aims to pay undisputed invoices with a valid PO within 30 days. Its published standard terms provide 30 days from receipt of a valid undisputed invoice submitted monthly in arrears. The supplier portal tracks status only.",
    "applies_to": "whole_organisation",
    "page_url": "https://www.bankofengland.co.uk/contact/supplying-goods-and-services/invoicing-and-po-policies",
    "quote": "Invoice queries should be submitted to finance.operations@bankofengland.co.uk.",
    "retrieved_date": "2026-11-08",
    "found_by": "chatgpt",
    "verification": "verified",
    "source_file": "chatgpt_verify_buyer_ap_results_batch01.csv",
    "org": "Bank of England",
    "task_id": "CH-VF-00091"
   },
   {
    "email": "finance.operations@bankofengland.co.uk",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.bankofengland.co.uk/contact/supplying-goods-and-services/invoicing-and-po-policies",
    "quote": "Invoice queries should be submitted to finance.operations@bankofengland.co.uk . Although the Supplier Portal allows for Suppliers to review invoice status, the Supplier Portal does not allow Suppliers to submit invoices, raise invoice queries or conduct commun",
    "retrieved_date": "2026-11-09",
    "found_by": "codex",
    "verification": "verified",
    "source_file": "codex_buyer_ap_results_batch04.csv",
    "org": "Bank of England",
    "task_id": "CO-AP-00381"
   },
   {
    "email": "financedivisionpaymentsteam@bankofengland.co.uk",
    "type": "supplier_payment",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": null,
    "page_url": "https://www.bankofengland.co.uk/contact/supplying-goods-and-services/invoicing-and-po-policies",
    "quote": "0 days of the invoice being submitted. Supplier invoices are required to be submitted to the Bank via the
```

## PO-level open data naming this buyer
_none_

## Contract records between the pair (dataset)
| record_id | source | status | title | value | currency | start | end | identifiers | link |
|---|---|---|---|---|---|---|---|---|---|
| uk_contracts_finder:ocds-b5fd17-28677ccb-f2e8-46ea-a565-c0102b434930-1 | uk_contracts_finder | ongoing | Candeal Subscription Licenses | 77059.0 | GBP |  |  | {"ocid": "ocds-b5fd17-28677ccb-f2e8-46ea-a565-c0102b434930", "award_id": "ocds-b5fd17-28677ccb-f2e8-46ea-a565-c0102b434930-1", "notice_guid": "6f72f272-7a7f-4613-b3fd-c2f24b75cbad", "tender_id": "CON/ | https://www.contractsfinder.service.gov.uk/Notice/6f72f272-7a7f-4613-b3fd-c2f24b75cbad |

## The buyer's other Canadian-vendor records (first 60 of 0)
_none_

## The vendor's other buyers in the dataset (first 60 of 16)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_montreal_contrats:fonctionnaires-175-1175284 | Ville de Montréal | CANDEAL - Renouvellement du système de négociation parallèle de titres et produits du marché monétaire - Année 2017 | 9952.81 |  |  | https://donnees.montreal.ca/dataset/0b7955a7-8523-4254-8f95-81a59684866d/resource/e4b758ab-3edb-4b6a-8764-2a443b6b9404/download/contratsfonctionnaires.csv |
| ca_montreal_contrats:fonctionnaires-42124-823998 | Ville de Montréal | ABONNEMENT AU SYSTEME DE NÉGOCATION PARALLÈLE (SNP) | 8578.05 |  |  | https://donnees.montreal.ca/dataset/0b7955a7-8523-4254-8f95-81a59684866d/resource/e4b758ab-3edb-4b6a-8764-2a443b6b9404/download/contratsfonctionnaires.csv |
| ca_montreal_contrats:fonctionnaires-43547-1514829 | Ville de Montréal | Ser Finances-Bon de commande ouvert Année 2022-CanDeal - Abonnement au système de négociation parallèle de titres et produits du marché monétaire pour l'année 2 | 10960.69 |  |  | https://donnees.montreal.ca/dataset/0b7955a7-8523-4254-8f95-81a59684866d/resource/e4b758ab-3edb-4b6a-8764-2a443b6b9404/download/contratsfonctionnaires.csv |
| ca_montreal_contrats:fonctionnaires-58035-1576703 | Ville de Montréal | FIN/BCO 2023 -Service Abonnement au système de négociation parallèle de titres et produits du marché monétaire | 10960.69 |  |  | https://donnees.montreal.ca/dataset/0b7955a7-8523-4254-8f95-81a59684866d/resource/e4b758ab-3edb-4b6a-8764-2a443b6b9404/download/contratsfonctionnaires.csv |
| ca_montreal_contrats:fonctionnaires-76502-1450593 | Ville de Montréal | BCO  - Abonnement au système de négociation parallèle de titres et produits du marché monétaire pour l'année 2021 | 11128.67 |  |  | https://donnees.montreal.ca/dataset/0b7955a7-8523-4254-8f95-81a59684866d/resource/e4b758ab-3edb-4b6a-8764-2a443b6b9404/download/contratsfonctionnaires.csv |
| ca_montreal_contrats:fonctionnaires-85071-1696217 | Ville de Montréal | FIN / Abonnement au système de négociation parallèle de titres et produits du marché monétaire pour l'année 2025 - 2026. | 11905.58 |  |  | https://donnees.montreal.ca/dataset/0b7955a7-8523-4254-8f95-81a59684866d/resource/e4b758ab-3edb-4b6a-8764-2a443b6b9404/download/contratsfonctionnaires.csv |
| ca_montreal_contrats:fonctionnaires-93777-923435 | Ville de Montréal | ABONNEMENT AU SYSTEME DE NÉGOCATION PARALLÈLE (SNP) | 4976.41 |  |  | https://donnees.montreal.ca/dataset/0b7955a7-8523-4254-8f95-81a59684866d/resource/e4b758ab-3edb-4b6a-8764-2a443b6b9404/download/contratsfonctionnaires.csv |
| ca_montreal_contrats:fonctionnaires-97773-923435 | Ville de Montréal | ABONNEMENT AU SYSTEME DE NÉGOCATION PARALLÈLE (SNP) | 10267.36 |  |  | https://donnees.montreal.ca/dataset/0b7955a7-8523-4254-8f95-81a59684866d/resource/e4b758ab-3edb-4b6a-8764-2a443b6b9404/download/contratsfonctionnaires.csv |
| ca_montreal_contrats:fonctionnaires-113179-1318830 | Ville de Montréal | Abonnement que nous faisons depuis plusieurs années. Ci-joint la facture du mois de janvier 2019 le montant du BC est pour 12 mois. | 9952.81 |  |  | https://donnees.montreal.ca/dataset/0b7955a7-8523-4254-8f95-81a59684866d/resource/e4b758ab-3edb-4b6a-8764-2a443b6b9404/download/contratsfonctionnaires.csv |
| ca_montreal_contrats:fonctionnaires-116112-743249 | Ville de Montréal | ABONNEMENT AU SYSTEME DE NÉGOCATION PARALLÈLE (SNP) | 6433.54 |  |  | https://donnees.montreal.ca/dataset/0b7955a7-8523-4254-8f95-81a59684866d/resource/e4b758ab-3edb-4b6a-8764-2a443b6b9404/download/contratsfonctionnaires.csv |
| ca_montreal_contrats:fonctionnaires-141794-1252394 | Ville de Montréal | CanDeal - Abonnement au système de négociation parallèle de titres et produits du marché monétaire pour l'année 2018. | 9952.81 |  |  | https://donnees.montreal.ca/dataset/0b7955a7-8523-4254-8f95-81a59684866d/resource/e4b758ab-3edb-4b6a-8764-2a443b6b9404/download/contratsfonctionnaires.csv |
| ca_montreal_contrats:fonctionnaires-172884-1633954 | Ville de Montréal | FIN // Service d'abonnement au système de négociation parallèle de titres et produits du marché monétaire pour l'année 2024  | 11527.63 |  |  | https://donnees.montreal.ca/dataset/0b7955a7-8523-4254-8f95-81a59684866d/resource/e4b758ab-3edb-4b6a-8764-2a443b6b9404/download/contratsfonctionnaires.csv |
| ca_montreal_contrats:fonctionnaires-205831-1696217 | Ville de Montréal | FIN / Abonnement au système de négociation parallèle de titres et produits du marché monétaire pour l'année 2025 - 2026. | 11905.58 |  |  | https://donnees.montreal.ca/dataset/0b7955a7-8523-4254-8f95-81a59684866d/resource/e4b758ab-3edb-4b6a-8764-2a443b6b9404/download/contratsfonctionnaires.csv |
| ca_montreal_contrats:fonctionnaires-209057-1059773 | Ville de Montréal | Abonnement au système de négociation parallèle de titres et produits du marché monétaire - juillet à décembre 2015 | 4976.41 |  |  | https://donnees.montreal.ca/dataset/0b7955a7-8523-4254-8f95-81a59684866d/resource/e4b758ab-3edb-4b6a-8764-2a443b6b9404/download/contratsfonctionnaires.csv |
| ca_montreal_contrats:fonctionnaires-246172-1392331 | Ville de Montréal | BCO - CanDeal - Abonnement au système de négociation parallèle de titres et produits du marché monétaire pour l'année 2020 - Service des finances. | 8294.01 |  |  | https://donnees.montreal.ca/dataset/0b7955a7-8523-4254-8f95-81a59684866d/resource/e4b758ab-3edb-4b6a-8764-2a443b6b9404/download/contratsfonctionnaires.csv |
| ca_montreal_contrats:fonctionnaires-247828-1097292 | Ville de Montréal | Abonnement au système de négociation parallèle de titres et produits du marché monétaire - Année 2016 C'est un abonnement que nous renouvelons à toutes les anné | 9952.81 |  |  | https://donnees.montreal.ca/dataset/0b7955a7-8523-4254-8f95-81a59684866d/resource/e4b758ab-3edb-4b6a-8764-2a443b6b9404/download/contratsfonctionnaires.csv |

## Open questions for hand research (layer 2)

- the vendor's GST/HST number (BN9)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
