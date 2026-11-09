# S1-28 — Virginia Department of Energy ⇄ Activation Laboratories Ltd

Stratum: **S1_gold_complete_published_PO_rule** · pay on sight: yes · channel tier 1 · AP grade A · missing: —

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Virginia Energy (label per Wikidata Q136351868, official website on the organisation's domain (https://www.energy.virginia.gov) + name; 2026-11-08) — Virginia Department of Energy 900 Natural Resources Drive Suite 500, Charlottesville, VA, 22903
SUBMIT TO: accountspayable@energy.virginia.gov (invoicing/AP mailbox, confirmed by the referee)
REFERENCE: PO PCO05351239-V3 (order_number); 2|3|4|5|7|8|9 (order_line_numbers) | PO rule: purchase-order terms published (as published: include the provisions of the three paragraphs above in every subcontract 
FROM / REMIT TO: ACTIVATION LABORATORIES LTD. — 41 Bittern St, Ancaster, ON, L9G 4V5 | GST/HST 121979355RT0001 (account derived from the BN9)
TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state  | CURRENCY: USD | TERMS: payment requests through Virginia Energy’s eForms web portal within 30 calendar days (as printed on 
DESCRIPTION: 4Lithores (11+) | AMOUNT: 8,416.00 USD
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 96
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 11
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Virginia Department of Energy (utility / public corporation, US) — public contract / purchase award in the last 12 months (dated record): Activation Laboratories Ltd | subject: 4Lithores (11+) | instrument: purchase order (PCO) | PO / procurement number: PCO05351239-V3 (order_number); 2|3|4|5|7|8|9 (order_line_numbers) | all identifiers: {"order_number": "PCO05351239-V3", "contract_number": null, "requisition_dates": null, "eva_vendor_id": "VS0000140410", "vlin_id": "VA00077715", "entity_code": "A409", "order_line_numbers": ["2", "3", "4", "5", "7", "8", "9"]} | value: 8416.0 USD | awarded 2026-06-01, start 2026-06-01 | published by: eVA Procurement Data (Virginia Open Data Portal, FY2026 file) | record: https://data.virginia.gov/dataset/eva-procurement-data-2026-virginia | vendor in Canada because: Vendor Address State = 'ON' (Canadian province code) | status rule: likely active (awarded in the last 12 months, no end date published) | this buyer has 6 records with Canada-located vendors (1 distinct vendors; 6 in the last 12 months; latest 2026-06-01)
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: b:3a236b011ab86698
- **tier**: B
- **grade**: 4
- **records_with_this_vendor**: 6

## Buyer
- **buyer**: Virginia Department of Energy
- **buyer_website**: https://energy.virginia.gov
- **buyer_address**: Virginia Department of Energy 900 Natural Resources Drive Suite 500, Charlottesville, VA, 22903
- **buyer_phone**: (804) 674-2000
- **buyer_contact_evidence_url**: https://vsp.virginia.gov/contact/
- **buyer_legal_name_as_published**: Virginia Energy (label per Wikidata Q136351868, official website on the organisation's domain (https://www.energy.virginia.gov) + name; 2026-11-08)
- **buyer_logo_url**: https://vsp.virginia.gov/wp-content/uploads/2021/09/VSP-logo-1.png
- **buyer_type**: utility / public corporation
- **buyer_sector**: utility
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q136351868; government agency
- **buyer_founded**: 1985-01-01 (Wikidata Q136351868, official website on the organisation's domain (https://www.energy.virginia.gov) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://vsp.virginia.gov/contact/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; invoicing requirements: the lane's AP page (https://energy.virginia.gov/energy/documents/SPARK/SPARK%20Application%20Draft%206-16-25_Clean_final_done.pdf); payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_payment_method_preference**: required AVS check (as printed on https://energy.virginia.gov/coal/mined-land-repurposing/AMLER/2025/AMLER%20Terms%20and%20Conditions%20VA%2020250306.pdf, re-read 2026-11-08)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **buyer_vendor_id**: VS0000140410 (eva_vendor_id)
- **buyer_org_codes**: A409 (entity_code)
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: accountspayable@energy.virginia.gov
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://energy.virginia.gov/energy/documents/SPARK/SPARK%20Application%20Draft%206-16-25_Clean_final_done.pdf
- **email_evidence_quote**: All invoices must be submitted to the Accounts Payable department via email at accountspayable@energy.virginia.gov Invoice MUST include the following
- **email_evidence_context**: Delivery for Sub-Awardees Payment Schedule and Invoices To receive payment, all applicants must confirm registration in the Electronic Virginia Registration (eVA) system. All invoices must be submitted to the Accounts Payable department via email at accountspayable@energy.virginia.gov Invoice MUST include the following (as applicable) to be considered for payment: a. Name and address of contractor materials sold to b. Materials on invoice must have line item from contract c. Invoice Date d. Invoice Number e. Project Number/Contra (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: accountspayable@energy.virginia.gov (invoicing/AP) | researched by the ChatGPT/Codex agent (lane chatgpt) (page opened and quoted) on 2026-10-29 | page: https://energy.virginia.gov/energy/documents/SPARK/SPARK%20Application%20Draft%206-16-25_Clean_final_done.pdf | quote: "All invoices must be submitted to the Accounts Payable department via email at accountspayable@energy.virginia.gov Invoice MUST include the following" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by self-hosted or other (mailstream-central.mxrecord.mx) | lane file: chatgpt/chatgpt_buyer_ap_results_batch11.csv task CH-AP-01039
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by self-hosted or other (mailstream-central.mxrecord.mx)
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject; sp=none; rua=mailto:rua.dmarc@vita.virginia.gov; ruf=mailto:ruf.dmarc@vita.virginia.gov; fo=1:d:s
- **dmarc_record_domain**: energy.virginia.gov
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 ip4:166.67.201.136 ip4:166.67.201.137 ip4:166.67.201.138 include:_spf.msg.virginia.gov ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements**: SPARK subaward guideline: confirm eVA registration; email AP invoices with applicable contractor name/address, contract line item, invoice date/number, project/contractnumber, materialdescription, unit ofmeasure, unitprice, extendedprice and freight/shipping.
- **payment_terms_as_published**: payment requests through Virginia Energy’s eForms web portal within 30 calendar days (as printed on https://energy.virginia.gov/coal/mined-land-repurposing/AMLER/2025/AMLER%20Terms%20and%20Conditions%20VA%2020250306.pdf, re-read 2026-11-08)
- **po_required_as_published**: purchase-order terms published (as published: include the provisions of the three paragraphs above in every subcontract of any amount and every purchase order) (as printed on https://energy.virginia.gov/coal/mined-land-repurposing/AMLER/2025/AMLER%20Terms%20and%20Conditions%20VA%2020250306.pdf, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "payment_terms": "payment requests through Virginia Energy’s eForms web portal within 30 calendar days (as printed on https://energy.virginia.gov/coal/mined-land-repurposing/AMLER/2025/AMLER%20Terms%20and%20Conditions%20VA%2020250306.pdf, re-read 2026-11-08)", "po_required": "purchase-order terms published (as published: include the provisions of the three paragraphs above in every subcontract of any amount and every purchase order) (as printed on https://energy.virginia.gov/coal/mined-land-repurposing/AMLER/2025/AMLER%20Terms%20and%20Conditions%20VA%2020250306.pdf, re-read 2026-11-08)", "requirements_text": "SPARK subaward guideline: confirm eVA registration; email AP invoices with applicable contractor name/address, contract line item, invoice date/number, project/contractnumber, materialdescription, unit ofmeasure, unitprice, extendedprice and freight/shipping."}
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Virginia Energy (label per Wikidata Q136351868, official website on the organisation's domain (https://www.energy.virginia.gov) + name; 2026-11-08) — Virginia Department of Energy 900 Natural Resources Drive Suite 500, Charlottesville, VA, 22903 ⏎ SUBMIT TO: accountspayable@energy.virginia.gov (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: PO PCO05351239-V3 (order_number); 2|3|4|5|7|8|9 (order_line_numbers) | PO rule: purchase-order terms published (as published: include the provisions of the three paragraphs above in every subcontract  ⏎ FROM / REMIT TO: ACTIVATION LABORATORIES LTD. — 41 Bittern St, Ancaster, ON, L9G 4V5 | GST/HST 121979355RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state  | CURRENCY: USD | TERMS: payment requests through Virginia Energy’s eForms web portal within 30 calendar days (as printed on  ⏎ DESCRIPTION: 4Lithores (11+) | AMOUNT: 8,416.00 USD
- **invoice_card_json**: {"bill_to": {"legal_name": "Virginia Energy (label per Wikidata Q136351868, official website on the organisation's domain (https://www.energy.virginia.gov) + name; 2026-11-08)", "legal_name_is_published": true, "address": "Virginia Department of Energy 900 Natural Resources Drive Suite 500, Charlottesville, VA, 22903", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "accountspayable@energy.virginia.gov", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "purchase-order terms published (as published: include the provisions of the three paragraphs above in every subcontract of any amount and every purchase order) (as printed on https://energy.virginia.gov/coal/mined-land-repurposing/AMLER/2025/AMLER%20Terms%20and%20Conditions%20VA%2020250306.pdf, re-read 2026-11-08)", "po_number": "PCO05351239-V3 (order_number); 2|3|4|5|7|8|9 (order_line_numbers)", "contract_or_agreement_number": "", "vendor_id_with_buyer": "VS0000140410 (eva_vendor_id)", "reference_hint": "purchase order / procurement number: PCO05351239-V3 (order_number) — source us_state_virginia"}, "terms": {"payment_terms": "payment requests through Virginia Energy’s eForms web portal within 30 calendar days (as printed on https://energy.virginia.gov/coal/min
- **invoice_readiness**: 11/11 invoice elements present
- **ap_grade**: A
- **ap_score**: 88
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published; payment cycle or method published (plausibility) | missing: finance mailbox; AP phone or AP contact
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **language_hint**: en
- **template_language**: en
- **po_number_as_published**: PCO05351239-V3 (order_number); 2|3|4|5|7|8|9 (order_line_numbers)
- **invoice_reference_hint**: purchase order / procurement number: PCO05351239-V3 (order_number) — source us_state_virginia

## Vendor
- **vendor**: Activation Laboratories Ltd
- **vendor_legal_name**: ACTIVATION LABORATORIES LTD.
- **vendor_registry_id**: BC OrgBook (BC registration): A0080502
- **vendor_registry_url**: https://orgbook.gov.bc.ca/entity/A0080502
- **vendor_legal_form**: Extraprovincial company (home jurisdiction ON)
- **vendor_address**: 41 Bittern St, Ancaster, ON, L9G 4V5
- **vendor_country_basis**: Vendor Address State = 'ON' (Canadian province code)
- **vendor_bn9**: 121979355
- **vendor_gst_hst_derived**: 121979355RT0001
- **vendor_website**: https://actlabs.com/
- **vendor_phone**: 1-888-228-5227
- **vendor_contact_evidence_url**: https://actlabs.com/locations/
- **vendor_logo_url**: https://actlabs.com/wp-content/uploads/2019/09/logo-e1571429772460.png
- **vendor_website_basis**: found by a web search, confirmed by reading the site on 2026-11-08: https://actlabs.com/ (Activation Laboratories Ltd. (Actlabs) - Analytical Lab Services Skip to content WebLIMS login ALADIN login Contact Us ABOUT ACTLABS About Corporate History Dr.)
- **vendor_facts_provenance**: name and address: the record's vendor block (eVA Procurement Data (Virginia Open Data Portal, FY2026 file)); registry identity: BC OrgBook (BC registration): A0080502 status BC OrgBook (BC registration): Active (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; strong); BN9: bc_orgbook A0080502 (strong match); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2010-06-25; phone / role e-mails / logo: the vendor's own site, https://actlabs.com/locations/ (tools/org_contacts.py, org_extras.py); website: https://actlabs.com/
- **vendor_concentration_top_share**: Activation Laboratories Ltd: 100% of 6 records
- **vendor_registry_status**: BC OrgBook (BC registration): Active
- **vendor_registry_match_level**: strong
- **vendor_incorporation_date**: 2010-06-25
- **vendor_years_in_business**: 16.4 (since 2010-06-25, registry date)
- **vendor_bn_source**: bc_orgbook A0080502 (strong match)

## Contract
- **po_required_as_published**: purchase-order terms published (as published: include the provisions of the three paragraphs above in every subcontract of any amount and every purchase order) (as printed on https://energy.virginia.gov/coal/mined-land-repurposing/AMLER/2025/AMLER%20Terms%20and%20Conditions%20VA%2020250306.pdf, re-read 2026-11-08)
- **contract_status**: likely active (awarded in the last 12 months, no end date published)
- **contract_reference**: {"order_number": "PCO05351239-V3", "contract_number": null, "requisition_dates": null, "eva_vendor_id": "VS0000140410", "vlin_id": "VA00077715", "entity_code": "A409", "order_line_numbers": ["2", "3", "4", "5", "7", "8", "9"]}
- **contract_title**: 4Lithores (11+)
- **contract_description**: 11-ABA Modified Sobek; 4B1; 4Lithores (11+); 9-Clay Speciation (Geomet); 9-XRD Quantitative Mineral ID (Rietveld) (Geomet); Disposal-pulps+rejects; RX1
- **po_number_as_published**: PCO05351239-V3 (order_number); 2|3|4|5|7|8|9 (order_line_numbers)
- **award_or_notice_id**: VA00077715 (vlin_id)
- **commodity_codes**: NIGP 96148 (Laboratory and Field Testing Services (Not Otherwise Classified) Incl. Hazardous)
- **contract_value**: 8416.0
- **currency**: USD
- **award_date**: 2026-06-01
- **start_date**: 2026-06-01
- **contract_link**: https://data.virginia.gov/dataset/eva-procurement-data-2026-virginia
- **source**: eVA Procurement Data (Virginia Open Data Portal, FY2026 file)
- **contracts_with_canadian_suppliers**: 6
- **records_last_12_months**: 6
- **record_sources**: eVA Procurement Data (Virginia Open Data Portal, FY2026 file) (6)
- **records_with_this_vendor**: 6
- **records_in_contract_dataset**: 6 records with Canada-located vendors (this row's organisation)

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **vendor_gst_hst_derived**: 121979355RT0001

## Pay on sight / grades
- **pay_on_sight**: yes
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Virginia Energy (label per Wikidata Q136351868, official website on the organisation's domain (https://www.energy.virginia.gov) + name; 2026-11-08) — Virginia Department of Energy 900 Natural Resources Drive Suite 500, Charlottesville, VA, 22903 ⏎ SUBMIT TO: accountspayable@energy.virginia.gov (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: PO PCO05351239-V3 (order_number); 2|3|4|5|7|8|9 (order_line_numbers) | PO rule: purchase-order terms published (as published: include the provisions of the three paragraphs above in every subcontract  ⏎ FROM / REMIT TO: ACTIVATION LABORATORIES LTD. — 41 Bittern St, Ancaster, ON, L9G 4V5 | GST/HST 121979355RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state  | CURRENCY: USD | TERMS: payment requests through Virginia Energy’s eForms web portal within 30 calendar days (as printed on  ⏎ DESCRIPTION: 4Lithores (11+) | AMOUNT: 8,416.00 USD
- **invoice_card_json**: {"bill_to": {"legal_name": "Virginia Energy (label per Wikidata Q136351868, official website on the organisation's domain (https://www.energy.virginia.gov) + name; 2026-11-08)", "legal_name_is_published": true, "address": "Virginia Department of Energy 900 Natural Resources Drive Suite 500, Charlottesville, VA, 22903", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "accountspayable@energy.virginia.gov", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "purchase-order terms published (as published: include the provisions of the three paragraphs above in every subcontract of any amount and every purchase order) (as printed on https://energy.virginia.gov/coal/mined-land-repurposing/AMLER/2025/AMLER%20Terms%20and%20Conditions%20VA%2020250306.pdf, re-read 2026-11-08)", "po_number": "PCO05351239-V3 (order_number); 2|3|4|5|7|8|9 (order_line_numbers)", "contract_or_agreement_number": "", "vendor_id_with_buyer": "VS0000140410 (eva_vendor_id)", "reference_hint": "purchase order / procurement number: PCO05351239-V3 (order_number) — source us_state_virginia"}, "terms": {"payment_terms": "payment requests through Virginia Energy’s eForms web portal within 30 calendar days (as printed on https://energy.virginia.gov/coal/min
- **invoice_readiness**: 11/11 invoice elements present
- **ap_grade**: A
- **ap_score**: 88
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published; payment cycle or method published (plausibility) | missing: finance mailbox; AP phone or AP contact
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **facts_provenance_json**: {"mailbox": ["accountspayable@energy.virginia.gov (invoicing/AP)", "researched by the ChatGPT/Codex agent (lane chatgpt) (page opened and quoted) on 2026-10-29", "page: https://energy.virginia.gov/energy/documents/SPARK/SPARK%20Application%20Draft%206-16-25_Clean_final_done.pdf", "quote: \"All invoices must be submitted to the Accounts Payable department via email at accountspayable@energy.virginia.gov Invoice MUST include the following\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by self-hosted or other (mailstream-central.mxrecord.mx)", "lane file: chatgpt/chatgpt_buyer_ap_results_batch11.csv task CH-AP-01039"], "buyer_facts": ["address and phone: the buyer's own site, https://vsp.virginia.gov/contact/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "invoicing requirements: the lane's AP page (https://energy.virginia.gov/energy/documents/SPARK/SPARK%20Application%20Draft%206-16-25_Clean_final_done.pdf)", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://energy.virginia.gov/energy/documents/SPARK/SPARK%20Application%20Draft%206-16-25_Clean_final_done.pdf | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, domain unknown)
_not read_

## Buyer role mailboxes found on its site (org_contacts)
_not read_

## Vendor site facts (org_extras, actlabs.com)
- **status**: ok
- **pages**: 4
- **v**: 2
- **legal_name_stated**: Activation Laboratories Ltd
- **legal_name_stated_url**: https://actlabs.com/about-actlabs/corporate-history/
- **legal_name_stated_quote**: Our History - Activation Laboratories Ltd. (Actlabs) Skip to content WebLIMS login ALADIN login Contact Us ABOUT ACTLABS About Corporate Hist
- **linkedin_url**: https://ca.linkedin.com/company/activation-laboratories-ltd
- **tel_links**: 1-888-228-5227
- **tel_links_url**: https://actlabs.com/
- **language**: en
- **logo_url**: https://actlabs.com/wp-content/uploads/2019/09/logo-e1571429772460.png
- **logo_basis**: logo image in the site header
- **domain**: actlabs.com
- **key**: vendor:Activation Laboratories Ltd
- **name**: Activation Laboratories Ltd
- **website**: https://actlabs.com/
- **kind**: vendor
- **date**: 2026-11-08

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "84623 Heroica Cdad. de Cananea, Son., Mexico , 184 Rue Principale, Sainte-Germaine-Boulé, QC J0Z 1M0", "address_country": "CA", "address_url": "https://actlabs.com/locations/", "address_method": "pattern", "address_quote": "ca Cdad. de Cananea, Son., Mexico 184 Rue Principale, Sainte-Germaine-Boulé, QC J0Z 1M0, Canada Learn More Calle Cantera # 3200 Conjunto Industrial de la Plata Guadalu", "phone": "1-888-228-5227", "phone_url": "https://actlabs.com/locations/", "domain": "actlabs.com", "key": "vendor:Activation Laboratories Ltd", "name": "Activation Laboratories Ltd", "website": "https://actlabs.com/", "kind": "vendor", "date": "2026-11-08"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Virginia Department of Energy | Q136351868 | official website on the organisation's domain (https://www.energy.virginia.gov) + name |  | Virginia Energy |  | government agency |  | United States | 1985-01-01 |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "b:3a236b011ab86698",
 "ap_contact_team": {
  "emails": [
   "accountspayable@energy.virginia.gov"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": "SPARK subaward guideline: confirm eVA registration; email AP invoices with applicable contractor name/address, contract line item, invoice date/number, project/contractnumber, materialdescription, unit ofmeasure, unitprice, extendedprice and freight/shipping.",
  "evidence": [
   {
    "email": "accountspayable@energy.virginia.gov",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": "SPARK subaward guideline: confirm eVA registration; email AP invoices with applicable contractor name/address, contract line item, invoice date/number, project/contractnumber, materialdescription, unit ofmeasure, unitprice, extendedprice and freight/shipping.",
    "applies_to": "this_unit_only",
    "page_url": "https://energy.virginia.gov/energy/documents/SPARK/SPARK%20Application%20Draft%206-16-25_Clean_final_done.pdf",
    "quote": "All invoices must be submitted to the Accounts Payable department via email at accountspayable@energy.virginia.gov Invoice MUST include the following",
    "retrieved_date": "2026-10-29",
    "found_by": "chatgpt",
    "verification": "verified",
    "source_file": "chatgpt_buyer_ap_results_batch11.csv",
    "org": "Virginia Department of Energy",
    "task_id": "CH-AP-01039"
   },
   {
    "email": "accountspayable@energy.virginia.gov",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://energy.virginia.gov/energy/documents/SPARK/SPARK%20Application%20Draft%206-16-25_Clean_final_done.pdf",
    "quote": "ration in the Electronic Virginia Registration (eVA) system. All invoices must be submitted to the Accounts Payable department via email at accountspayable@energy.virginia.gov Invoice MUST include the following (as applicable) to be considered for payment: a. Name and address of contractor",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Virginia Department of Energy",
    "task_id": "CL-WS-00311"
   }
  ]
 },
 "research_status": {
  "found": 2
 },
 "queries_tried": [
  "site:energy.virginia.gov invoice accounts payable; exactaccountspayable role search; opened Departmenthomepage, currentContact and publicSPARKYouthWorkforcePilotProgramSubAwardguidelines",
  "web search for the buyer's invoicing / accounts payable page (the search only gave the address); the page then read by tools/deep_pages.py with the crawler's rules, no AI"
 ],
 "ingested_at": "2026-11-09T16:04:50Z"
}
```

## PO-level open data naming this buyer
_none_

## Contract records between the pair (dataset)
| record_id | source | status | title | value | currency | start | end | identifiers | link |
|---|---|---|---|---|---|---|---|---|---|
| us_state_virginia:2026:PCO05267315:VS0000140410 | us_state_virginia | end_date_unknown | RX1 | 4136.4 | USD |  |  | {"order_number": "PCO05267315", "contract_number": null, "requisition_dates": null, "eva_vendor_id": "VS0000140410", "vlin_id": "VA00077715", "entity_code": "A409", "order_line_numbers": ["1", "2", "3 | https://data.virginia.gov/dataset/eva-procurement-data-2026-virginia |
| us_state_virginia:2026:PCO05267315-V2:VS0000140410 | us_state_virginia | end_date_unknown | RX1 | 4163.68 | USD |  |  | {"order_number": "PCO05267315-V2", "contract_number": null, "requisition_dates": null, "eva_vendor_id": "VS0000140410", "vlin_id": "VA00077715", "entity_code": "A409", "order_line_numbers": ["1", "2", | https://data.virginia.gov/dataset/eva-procurement-data-2026-virginia |
| us_state_virginia:2026:PCO05351239-V2:VS0000140410 | us_state_virginia | end_date_unknown | S1 | 8416.0 | USD |  |  | {"order_number": "PCO05351239-V2", "contract_number": null, "requisition_dates": null, "eva_vendor_id": "VS0000140410", "vlin_id": "VA00077715", "entity_code": "A409", "order_line_numbers": ["1", "2", | https://data.virginia.gov/dataset/eva-procurement-data-2026-virginia |
| us_state_virginia:2026:PCO05351239-V3:VS0000140410 | us_state_virginia | end_date_unknown | 4Lithores (11+) | 8416.0 | USD |  |  | {"order_number": "PCO05351239-V3", "contract_number": null, "requisition_dates": null, "eva_vendor_id": "VS0000140410", "vlin_id": "VA00077715", "entity_code": "A409", "order_line_numbers": ["2", "3", | https://data.virginia.gov/dataset/eva-procurement-data-2026-virginia |
| us_state_virginia:2026:PCO05182324:VS0000140410 | us_state_virginia | end_date_unknown | Modal Mineralogy 27x46 mm (MLA) | 6000.0 | USD |  |  | {"order_number": "PCO05182324", "contract_number": null, "requisition_dates": null, "eva_vendor_id": "VS0000140410", "vlin_id": "VA00077715", "entity_code": "A409", "order_line_numbers": ["1"]} | https://data.virginia.gov/dataset/eva-procurement-data-2026-virginia |
| us_state_virginia:2026:PCO05182324-V2:VS0000140410 | us_state_virginia | end_date_unknown | Modal Mineralogy 27x46 mm (MLA) | 6021.55 | USD |  |  | {"order_number": "PCO05182324-V2", "contract_number": null, "requisition_dates": null, "eva_vendor_id": "VS0000140410", "vlin_id": "VA00077715", "entity_code": "A409", "order_line_numbers": ["1", "2", | https://data.virginia.gov/dataset/eva-procurement-data-2026-virginia |

## The buyer's other Canadian-vendor records (first 60 of 0)
_none_

## The vendor's other buyers in the dataset (first 60 of 17)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_alberta_apc:AB-2026-04651:3be639cf-1157-40f5-b33c-399addc203de | Alberta Energy Regulator | Alberta Energy Regulator - Request for Proposal - 580-RFP Legacy Shield Rock & Sediment Reanalysis | 600000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2026-04651 |
| ca_newfoundland:7a6c2b1fe36fb0a7 | Industry, Energy & Technology | External Analysis and Disposal of Mercury | 11282.8 |  |  | https://www.gov.nl.ca/ppa/files/Contract-Award-Report-2024-03-16-To-2024-03-31-KD-Edits.pdf |
| canada_federal:aafc-aac:3000791913 | Agriculture and Agri-Food Canada | Scientific services | 25639.72 |  |  | https://search.open.canada.ca/contracts/record/aafc-aac,C-2025-2026-Q2-00318 |
| canada_federal:nrcan-rncan:3000717684 | Natural Resources Canada | Scientific services | 12351.06 |  |  | https://search.open.canada.ca/contracts/record/nrcan-rncan,C-2020-2021-Q3-00318 |
| canada_federal:nrcan-rncan:3000738159 | Natural Resources Canada | Scientific services | 29374.78 |  |  | https://search.open.canada.ca/contracts/record/nrcan-rncan,C-2021-2022-Q3-00456 |
| canada_federal:nrcan-rncan:7000004590 | Natural Resources Canada | N/A | 1.0 |  |  | https://search.open.canada.ca/contracts/record/nrcan-rncan,C-2025-2026-Q4-00091 |
| canada_federal:nrcan-rncan:7000004505 | Natural Resources Canada | N/A | 1.0 |  |  | https://search.open.canada.ca/contracts/record/nrcan-rncan,C-2025-2026-Q4-00090 |
| canada_federal:nrcan-rncan:3000815579 | Natural Resources Canada | Scientific services | 41908.98 |  |  | https://search.open.canada.ca/contracts/record/nrcan-rncan,C-2026-2027-Q1-00145 |
| canada_federal:cb:cb-790-93502694 | Agriculture and Agri-Food Canada | Minor Use Pesticide Program (MUPP) Good Laboratory Practices (GLP) Analysis of Pesticide Residues |  |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cb-790-93502694 |
| canada_federal:cb:cb-731-6854066 | Department of Agriculture and Agri-Food (AAFC) | AAFC REQUEST FOR SUPPLY ARRANGEMENT - PMC Analysis of Pesticide Residues |  |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cb-731-6854066 |
| seao_quebec:20056042:activation-laboratories-ltd | Ministère des Ressources naturelles et des Forêts | Analyses géochimiques de roche | 701555.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=e0c3fc28-676e-4aea-8bd0-5271a0e409f8 |
| usaspending:CONT_AWD_140G0126F0075_1434_140G0125D0009_1434 | Department of the Interior | TASK ORDER AGAINST U.S. GEOLOGICAL SURVEY IDIQ 140G0125D0009 FOR SAMPLE ANALYSIS | 12880.0 |  |  | https://www.usaspending.gov/award/CONT_AWD_140G0126F0075_1434_140G0125D0009_1434/ |
| usaspending:CONT_AWD_140G0126F0202_1434_140G0125D0009_1434 | Department of the Interior | TASK ORDER AGAINST U.S. GEOLOGICAL SURVEY IDIQ 140G0125D0009 FOR SAMPLE ANALYSIS | 9847.5 |  |  | https://www.usaspending.gov/award/CONT_AWD_140G0126F0202_1434_140G0125D0009_1434/ |
| usaspending:CONT_AWD_140G0126P0057_1434_-NONE-_-NONE- | Department of the Interior | RADIOCHEMICAL SAMPLE ANALYSIS | 8478.0 |  |  | https://www.usaspending.gov/award/CONT_AWD_140G0126P0057_1434_-NONE-_-NONE-/ |
| usaspending:CONT_IDV_140G0125D0009_1434 | Department of the Interior | IDIQ CONTRACT FOR GEOCHEMISTRY LAB SERVICES | 400000.0 |  |  | https://www.usaspending.gov/award/CONT_IDV_140G0125D0009_1434/ |
| ca_canadabuys_contract_history:an:PW-14-00626467-637450 | Health Canada | Analysis of pesticide residues in various matrices | 333332.0 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/pw-14-00626467-637450 |
| ca_canadabuys_contract_history:an:PW-18-00817291 | Natural Resources Canada | Geochemical Analysis |  |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/pw-18-00817291 |

## Open questions for hand research (layer 2)

- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
