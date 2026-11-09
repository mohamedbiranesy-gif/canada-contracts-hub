# S5-13 — North East School Division No. 200 ⇄ Sparkrock

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 2 · AP grade C · missing: the vendor's GST/HST number (BN9)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: NORTH EAST SCHOOL DIVISION NO. 200 (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (nesd.ca) + name) — 400, 701 93rd Avenue, Tisdale, SK S0E 1T0 — buyer tax no. 816324073RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (nesd.ca) + name)
SUBMIT TO: accounting@nesd.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee)
REFERENCE: contract RFPNESD2007-001 (competition_number) — the source publishes the award under this tender / notice number and no separate contract number; tender RFPNESD2007-001 (competition_number) | PO rule: not published
FROM / REMIT TO: Sparkrock Edsembli Inc (stated on the vendor's legal page: https://sparkrock.com/privacy-policy/) — Toronto, ON | GST/HST number not public
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their | CURRENCY: CAD | TERMS: vendor's standard terms (buy
```

## Relationship
- **rank_group**: C3
- **data_quality_score**: 64
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: North East School Division No. 200 (school board / school district, SK) — named as a client by the Canada-located vendor (client list / customer story / case study): Sparkrock | subject: Enterprise Resource Planning (ERP) Software and Implementation Services | instrument: contract award (tender competition) | contract number: RFPNESD2007-001 (competition_number) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contrac | solicitation: RFPNESD2007-001 (competition_number) | all identifiers: {"competition_number": "RFPNESD2007-001", "competition_guid": "c4e14d13-01a8-405e-a34c-0de962831abc"} | value: 602886.0 CAD | awarded 2020-11-06 | published by: SaskTenders - awarded competitions (Government of Saskatchewan public tender portal) | record: https://www.sasktenders.ca/Competitions/Print?id=c4e14d13-01a8-405e-a34c-0de962831abc | vendor in Canada because: province name 'ont' in award location 'Toronto, ONT' | status rule: end date unknown, awarded over 3 years ago | this buyer has 3 records with Canada-located vendors (3 distinct vendors; 0 in the last 12 months; latest 2021-01-27)
- **how_relationship_was_found**: tools/client_lists.py / customer_stories.py read the vendor's own client list or customer story naming the buyer
- **keys**: b:a1d711bf6ca6e326
- **tier**: C
- **grade**: 3
- **records_with_this_vendor**: 1

## Buyer
- **buyer**: North East School Division No. 200
- **buyer_website**: https://nesd.ca
- **buyer_address**: 400, 701 93rd Avenue, Tisdale, SK S0E 1T0
- **buyer_phone**: 1-306-752-5741
- **buyer_contact_evidence_url**: https://nesd.ca/Division/Contacts
- **buyer_legal_name_as_published**: NORTH EAST SCHOOL DIVISION NO. 200 (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (nesd.ca) + name)
- **buyer_bn_as_published**: 816324073RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (nesd.ca) + name)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 816324073RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_logo_url**: https://nesd.ca/file/32270083/79132654/50155490/orig
- **buyer_type**: school board / school district
- **buyer_sector**: education: K-12
- **buyer_charity_status**: registered (listed) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (nesd.ca) + name)
- **buyer_charity_designation**: C; 0010
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://nesd.ca/Division/Contacts (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); AP contact name: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: accounting@nesd.ca
- **email_type**: finance/accounting dept or supplier-payment office
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); finance mailbox
- **email_evidence_url**: https://nesd.ca/Division/Contacts/
- **email_evidence_quote**: Trena Puetz Payroll Technician - Pam Folden Finance Info Finance Phone: 1.306.752-1214 Toll Free: 1.888.752-5741 Fax: 1.306.752-1933 Email: accounting@nesd.ca Finance Contacts Finance People Superintendent of Business Administration - Wanda McLeod Business Manager - Tanya Biesenthal Manage
- **email_evidence_context**: payroll@nesd.ca Payroll Contacts Payroll people Supervisor of Payroll - Jacqui Broeckel Payroll Technician - Trena Puetz Payroll Technician - Pam Folden Finance Info Finance Phone: 1.306.752-1214 Toll Free: 1.888.752-5741 Fax: 1.306.752-1933 Email: accounting@nesd.ca Finance Contacts Finance People Superintendent of Business Administration - Wanda McLeod Business Manager - Tanya Biesenthal Manager of Finance - Donna Eberle Accounting Clerks - Melissa Bolen, Tatiana Colodeajnaia, Jamie Gagnon Administrative Assis (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: accounting@nesd.ca (finance/accounting dept or supplier-payment office) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://nesd.ca/Division/Contacts/ | quote: "Trena Puetz Payroll Technician - Pam Folden Finance Info Finance Phone: 1.306.752-1214 Toll Free: 1.888.752-5741 Fax: 1.306.752-1933 Email: accounting@nesd.ca F" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; DNS lookup failed; mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CH-AP-01246
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; DNS lookup failed; mail handled by Microsoft 365
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1; p=quarantine; pct=25; rua=mailto:dmarc@nesd.ca; ruf=mailto:dmarc@nesd.ca; fo=1
- **dmarc_record_domain**: nesd.ca
- **spf_policy**: DNS lookup failed
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_contact_name_as_published**: Melissa Bolen (Manager of Finance) (as printed by the organisation on its own accounts-payable page (as printed on https://nesd.ca/Division/Contacts/, re-read 2026-11-08))
- **ap_phone**: 1.306.752-1214 (as printed on https://nesd.ca/Division/Contacts/, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "ap_phone": "1.306.752-1214 (as printed on https://nesd.ca/Division/Contacts/, re-read 2026-11-08)"}
- **channel_tier**: 2
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: NORTH EAST SCHOOL DIVISION NO. 200 (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (nesd.ca) + name) — 400, 701 93rd Avenue, Tisdale, SK S0E 1T0 — buyer tax no. 816324073RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (nesd.ca) + name) ⏎ SUBMIT TO: accounting@nesd.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: contract RFPNESD2007-001 (competition_number) — the source publishes the award under this tender / notice number and no separate contract number; tender RFPNESD2007-001 (competition_number) | PO rule: not published ⏎ FROM / REMIT TO: Sparkrock Edsembli Inc (stated on the vendor's legal page: https://sparkrock.com/privacy-policy/) — Toronto, ON | GST/HST number not public ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their | CURRENCY: CAD | TERMS: vendor's standard 
- **invoice_card_json**: {"bill_to": {"legal_name": "NORTH EAST SCHOOL DIVISION NO. 200 (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (nesd.ca) + name)", "legal_name_is_published": true, "address": "400, 701 93rd Avenue, Tisdale, SK S0E 1T0", "address_is_the_invoice_address": false, "tax_number": "816324073RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (nesd.ca) + name)", "language": "en"}, "submit_to": {"email": "accounting@nesd.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "RFPNESD2007-001 (competition_number) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: RFPNESD2007-001 (competition_number) — the source publishes th
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; payment terms; vendor GST/HST number
- **ap_grade**: C
- **ap_score**: 63
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms not published (buyer's default applies)
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: contract or agreement number: RFPNESD2007-001 (competition_number) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference — source ca_saskatchewan

## Vendor
- **vendor**: Sparkrock
- **vendor_legal_name**: Sparkrock Edsembli Inc (stated on the vendor's legal page: https://sparkrock.com/privacy-policy/)
- **vendor_trading_name**: Sparkrock
- **vendor_address**: Toronto, ON
- **vendor_country_basis**: province name 'ont' in award location 'Toronto, ONT'
- **vendor_website**: https://sparkrock.com/
- **vendor_phone**: +1 866-878-5552
- **vendor_contact_evidence_url**: https://sparkrock.com/contact/
- **vendor_logo_url**: https://sparkrock.com/wp-content/uploads/2025/04/Spakrock-logo-1.svg
- **vendor_website_status**: site answers
- **vendor_linkedin_url**: https://www.linkedin.com/company/sparkrock
- **vendor_facts_provenance**: name and address: the record's vendor block (SaskTenders - awarded competitions (Government of Saskatchewan public tender portal)); phone / role e-mails / logo: the vendor's own site, https://sparkrock.com/contact/ (tools/org_contacts.py, org_extras.py); website: https://sparkrock.com/ (site answers)
- **vendor_concentration_top_share**: Matrix Video Communications: 33% of 3 records
- **vendor_registry_match_level**: no_match

## Contract
- **contract_status**: end date unknown, awarded over 3 years ago
- **contract_reference**: {"competition_number": "RFPNESD2007-001", "competition_guid": "c4e14d13-01a8-405e-a34c-0de962831abc"}
- **contract_title**: Enterprise Resource Planning (ERP) Software and Implementation Services
- **contract_description**: The North East School Division No. 200 (NESD) is issuing this Request for Proposal (RFP) for an Enterprise Resource Planning Software, and its related installation, conversion, migration, and implementation services. …
- **contract_or_agreement_number**: RFPNESD2007-001 (competition_number) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference
- **solicitation_or_tender_number**: RFPNESD2007-001 (competition_number)
- **award_or_notice_id**: c4e14d13-01a8-405e-a34c-0de962831abc (competition_guid) — notice id; the award is published within this notice, the source assigns no separate award id
- **contract_value**: 602886.0
- **currency**: CAD
- **award_date**: 2020-11-06
- **contract_link**: https://www.sasktenders.ca/Competitions/Print?id=c4e14d13-01a8-405e-a34c-0de962831abc
- **source**: SaskTenders - awarded competitions (Government of Saskatchewan public tender portal)
- **contracts_with_canadian_suppliers**: 3
- **records_last_12_months**: 0
- **record_sources**: SaskTenders - awarded competitions (Government of Saskatchewan public tender portal) (3)
- **records_with_this_vendor**: 1
- **records_in_contract_dataset**: 3 records with Canada-located vendors (this row's organisation)

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 816324073RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (SK) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: NORTH EAST SCHOOL DIVISION NO. 200 (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (nesd.ca) + name) — 400, 701 93rd Avenue, Tisdale, SK S0E 1T0 — buyer tax no. 816324073RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (nesd.ca) + name) ⏎ SUBMIT TO: accounting@nesd.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: contract RFPNESD2007-001 (competition_number) — the source publishes the award under this tender / notice number and no separate contract number; tender RFPNESD2007-001 (competition_number) | PO rule: not published ⏎ FROM / REMIT TO: Sparkrock Edsembli Inc (stated on the vendor's legal page: https://sparkrock.com/privacy-policy/) — Toronto, ON | GST/HST number not public ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their | CURRENCY: CAD | TERMS: vendor's standard 
- **invoice_card_json**: {"bill_to": {"legal_name": "NORTH EAST SCHOOL DIVISION NO. 200 (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (nesd.ca) + name)", "legal_name_is_published": true, "address": "400, 701 93rd Avenue, Tisdale, SK S0E 1T0", "address_is_the_invoice_address": false, "tax_number": "816324073RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (nesd.ca) + name)", "language": "en"}, "submit_to": {"email": "accounting@nesd.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "RFPNESD2007-001 (competition_number) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: RFPNESD2007-001 (competition_number) — the source publishes th
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; payment terms; vendor GST/HST number
- **ap_grade**: C
- **ap_score**: 63
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms not published (buyer's default applies)
- **facts_provenance_json**: {"mailbox": ["accounting@nesd.ca (finance/accounting dept or supplier-payment office)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://nesd.ca/Division/Contacts/", "quote: \"Trena Puetz Payroll Technician - Pam Folden Finance Info Finance Phone: 1.306.752-1214 Toll Free: 1.888.752-5741 Fax: 1.306.752-1933 Email: accounting@nesd.ca F\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; DNS lookup failed; mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CH-AP-01246"], "buyer_facts": ["address and phone: the buyer's own site, https://nesd.ca/Division/Contacts (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "AP contact name: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (SaskTenders - awarded competitions (G

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://nesd.ca/Division/Contacts/ | 2026-11-08 | ok |  |  |  | 1.306.752-1214 |  |  |  |  |  |

## Buyer site facts (org_extras, nesd.ca)
- **status**: ok
- **pages**: 5
- **language**: en
- **logo_url**: https://nesd.ca/file/32270083/79132654/50155490/orig
- **logo_basis**: logo image in the site header
- **domain**: nesd.ca
- **key**: b:a1d711bf6ca6e326
- **name**: North East School Division No. 200
- **website**: https://nesd.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Page About Us The North East School Division
- **legal_name_stated_url**: https://nesd.ca/Division/AboutUs/
- **legal_name_stated_quote**: chool will be closed today due to [reason]. We expect to re-open tomorrow at our regular time. Main Page About Us The North East School Division exists to foster growth, achievement, and wellbeing for our students through responsive learning in
- **mentions**: {'payment_method': {'text': 'interaction with a barrier, hinders an individual’s full and equal participation in soc', 'url': 'https://nesd.ca/Programs/Accessibility/', 'quote': 'What is a disability? The Accessible Saskatchewan Act defines disability as any impairment that, in interaction with a barrier, hinders an individual’s full and equal participation in society. It includes physical, mental, intellectual, cognitive, learning, co'}}
- **tel_links**: 1-306-752-5741; 1-888-752-5741

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "400, 701 93rd Avenue, Tisdale, SK S0E 1T0", "address_country": "CA", "address_url": "https://nesd.ca/Division/Contacts", "address_method": "pattern", "address_quote": "ansportation Transportation Info Address: Box 400, 701 93rd Avenue, Tisdale, SK S0E 1T0 Phone: 1-306-873-4555 Toll Free: 1-888-884-0240 General Email: Transportation@n", "phone": "1-306-752-5741", "phone_url": "https://nesd.ca/Division/Contacts", "emails": "accounting@nesd.ca", "emails_url": "https://nesd.ca/Division/Contacts", "domain": "nesd.ca", "key": "b:a1d711bf6ca6e326", "name": "North East School Division No. 200", "website": "https://nesd.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, sparkrock.com)
- **status**: ok
- **pages**: 5
- **language**: en
- **logo_url**: https://sparkrock.com/wp-content/uploads/2025/04/Spakrock-logo-1.svg
- **logo_basis**: logo image in the site header
- **domain**: sparkrock.com
- **key**: vendor:Sparkrock
- **name**: Sparkrock
- **website**: https://sparkrock.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Sparkrock
- **jsonld_logo**: https://sparkrock.com/wp-content/uploads/2025/04/Spakrock-logo-1.svg
- **jsonld_url**: https://sparkrock.com/
- **jsonld_same_as**: https://www.facebook.com/sparkrock; https://bsky.app/profile/sparkrock.bsky.social; https://www.linkedin.com/company/sparkrock; https://www.instagram.com/sparkrock.inc/; https://www.youtube.com/c/Sparkrock365
- **jsonld_quote**: {"@context": "http://schema.org","@type": "LocalBusiness","image": "https://sparkrock.com/wp-content/uploads/2025/04/Spakrock-logo-1.svg","description": "Sparkrock provides purpose-built enterprise software for nonprofits, school boards, and public sector organizations across North America.","url": 
- **jsonld_page**: https://sparkrock.com/
- **legal_name_stated**: Sparkrock Edsembli Inc
- **legal_name_stated_url**: https://sparkrock.com/privacy-policy/
- **legal_name_stated_quote**: ies Last Updated: February 12th, 2025 Privacy Policy Home >> Privacy Policy Introduction Welcome to Sparkrock Edsembli Inc. (“we,” “our,” or “the Company”). We are committed to protecting your privacy and ensuring the secu
- **mentions**: {'payment_method': {'text': 'interact with the system day-to-day Attend Webinar SPARK CHANGE IN YOUR ORGANIZATION Wa', 'url': 'https://sparkrock.com/', 'quote': 'uce reconciliation and manual work A short demo showing how CFOs, Controllers, and Finance Managers interact with the system day-to-day Attend Webinar SPARK CHANGE IN YOUR ORGANIZATION Watch: Why Sparkrock? Secure In Microsoft Sparkrock Finance and Sparkrock I'}}
- **linkedin_url**: https://www.linkedin.com/company/sparkrock
- **tel_links**: 18668785552; 18445577275; 14165160050

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "address": "7111 SYNTEX DR. 3RD FLOOR , MISSISSAUGA, ON , L5N 8C3", "address_country": "CA", "address_url": "https://sparkrock.com/contact/", "address_method": "pattern", "address_quote": "Follow Us embed-googlemap.com Toronto 7111 SYNTEX DR. 3RD FLOOR MISSISSAUGA, ON L5N 8C3 CANADA +1 416-516-0050 Austin 21750 HARDY OAK BLVD, SUITE 104 PMB 62757 SAN ANT", "phone": "+1 866-878-5552", "phone_url": "https://sparkrock.com/contact/", "domain": "sparkrock.com", "key": "vd:sparkrock.com", "name": "Sparkrock", "website": "https://sparkrock.com/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | North East School Division No. 200 |  |  |  |  |  |  |  |  |  |  |
| v | Sparkrock |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "b:a1d711bf6ca6e326",
 "ap_contact_team": {
  "emails": [
   "accounting@nesd.ca",
   "divisionoffice@nesd.ca"
  ],
  "invoice_portal": null,
  "phone": "306-752-5741",
  "mailing_address": "402 Main Street, Melfort, SK, Canada",
  "invoicing_requirements": "School division inquiries handled via divisionoffice@nesd.ca; finance department phone: 1-306-752-1214.",
  "evidence": [
   {
    "email": "accounting@nesd.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://nesd.ca/Division/Contacts/",
    "quote": "Trena Puetz Payroll Technician - Pam Folden Finance Info Finance Phone: 1.306.752-1214 Toll Free: 1.888.752-5741 Fax: 1.306.752-1933 Email: accounting@nesd.ca Finance Contacts Finance People Superintendent of Business Administration - Wanda McLeod Business Manager - Tanya Biesenthal Manage",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "North East School Division No. 200",
    "task_id": "CH-AP-01246"
   },
   {
    "email": "divisionoffice@nesd.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": "306-752-5741",
    "mailing_address": "402 Main Street, Melfort, SK, Canada",
    "requirements": "School division inquiries handled via divisionoffice@nesd.ca; finance department phone: 1-306-752-1214.",
    "applies_to": "North East School Division No. 200",
    "page_url": "https://nesd.ca/Division/Contacts/",
    "quote": "To contact the North East School Division Office: divisionoffice@nesd.ca. PH: 306-752-5741. FAX: 306-752-1933. NESD Department Contacts. (see below). Employee Directory. Finance Info. Finance. Phone: 1.306.752-1214. Toll Free: 1.888.752-5741.",
    "retrieved_date": "2026-11-02",
    "found_by": "gemini",
    "verification": "verified",
    "source_file": "gemini_buyer_ap_results_batch32.csv",
    "org": "North East School Division No. 200",
    "task_id": "CH-AP-01246"
   }
  ]
 },
 "research_status": {
  "found": 2
 },
 "queries_tried": [
  "site crawl of www.nesd.ca (30 pages, robots.txt respected), no AI, no search engine"
 ],
 "ingested_at": "2026-11-09T16:04:50Z"
}
```

## PO-level open data naming this buyer
_none_

## Contract records between the pair (dataset)
| record_id | source | status | title | value | currency | start | end | identifiers | link |
|---|---|---|---|---|---|---|---|---|---|
| ca_saskatchewan:c4e14d13-01a8-405e-a34c-0de962831abc:0 | ca_saskatchewan | end_date_unknown | Enterprise Resource Planning (ERP) Software and Implementation Services | 602886.0 | CAD |  |  | {"competition_number": "RFPNESD2007-001", "competition_guid": "c4e14d13-01a8-405e-a34c-0de962831abc"} | https://www.sasktenders.ca/Competitions/Print?id=c4e14d13-01a8-405e-a34c-0de962831abc |

## The buyer's other Canadian-vendor records (first 60 of 2)
| record_id | vendor | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_saskatchewan:618faa63-693a-49a3-8249-312b5795d868:0 | Matrix Video Communications | Technology Equipment - Sound Field Systems | 240382.55 |  |  | https://www.sasktenders.ca/Competitions/Print?id=618faa63-693a-49a3-8249-312b5795d868 |
| ca_saskatchewan:fb763462-c316-4bd3-81c3-47249a44b58c:0 | ENS Energy Network Services | Lighting LED Upgrade Program | 908257.0 |  |  | https://www.sasktenders.ca/Competitions/Print?id=fb763462-c316-4bd3-81c3-47249a44b58c |

## The vendor's other buyers in the dataset (first 60 of 1)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_bidsandtenders:3f093624-b5ed-4536-a746-f15860a5d88a:1 | London District Catholic School Board | HRIS ERP SYSTEM |  |  |  | https://ldcsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/3f093624-b5ed-4536-a746-f15860a5d88a |

## Open questions for hand research (layer 2)

- the vendor's GST/HST number (BN9)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
