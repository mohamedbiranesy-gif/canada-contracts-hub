# S1-29 — University of Regina ⇄ Softchoice

Stratum: **S1_gold_complete_published_PO_rule** · pay on sight: yes · channel tier 1 · AP grade A · missing: —

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: University of Regina We use cookies to give you the best — 3737 Wascana Parkway Regina, SK S4S 0A2 (as printed on https://www.uregina.ca/financial-services/assets/fs-forms/dd-form-vendors-and-non-employees-sep-2026-1.pdf, re-read 2026-11-08) — buyer tax no. 108162124RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (uregina.ca) + name)
SUBMIT TO: accounts.payable@uregina.ca (invoicing/AP mailbox, confirmed by the referee)
REFERENCE: contract UR-20800-18-26 (competition_number) — the source publishes the award under this tender / notice number and no separate contract number; tender UR-20800-18-26 (competition_number) | PO rule: yes (as published: Purchase Order include)
FROM / REMIT TO: SOFTCHOICE LP — Calgary, AB | GST/HST 124209297RT0001 (account derived from the BN9) | NEQ 3369689461
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their | CURRENCY: CAD | TERMS: Net30
DESCRIPTION: Veeam Support Renewal | AMOUNT: 36,365.00 CAD
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 95
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 14
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: University of Regina (organisation (type not stated in the record), SK) — public contract / purchase award in the last 12 months (dated record): Softchoice | subject: Veeam Support Renewal | instrument: contract award (tender competition) | contract number: UR-20800-18-26 (competition_number) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract | solicitation: UR-20800-18-26 (competition_number) | all identifiers: {"competition_number": "UR-20800-18-26", "competition_guid": "aff2dc1f-4a77-4fc4-8bb8-e43d212c7a89"} | value: 36365.0 CAD | awarded 2026-04-24 | published by: SaskTenders - awarded competitions (Government of Saskatchewan public tender portal) | record: https://www.sasktenders.ca/Competitions/Print?id=aff2dc1f-4a77-4fc4-8bb8-e43d212c7a89 | vendor in Canada because: province code 'AB' in award location 'Calgary, AB' | status rule: likely active (awarded in the last 12 months, no end date published) | this buyer has 209 records with Canada-located vendors (178 distinct vendors; 47 in the last 12 months; latest 2026-10-06)
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: b:c127a69d968d1bff
- **tier**: B
- **grade**: 4
- **records_with_this_vendor**: 2

## Buyer
- **buyer**: University of Regina
- **buyer_website**: https://www.uregina.ca
- **buyer_address**: 3737 Wascana Parkway, Regina, SK S4S 0A2
- **buyer_phone**: 306-585-4999
- **buyer_contact_evidence_url**: https://www.uregina.ca/about/contact/index.html
- **buyer_legal_name_as_published**: University of Regina We use cookies to give you the best
- **buyer_bn_as_published**: 108162124RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (uregina.ca) + name)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 108162124RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_logo_url**: https://www.uregina.ca/files/assets/images/uofr-og-image.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://ca.linkedin.com/school/university-of-regina/
- **buyer_type**: university / college (from the organisation's name / web domain)
- **buyer_sector**: education: post-secondary
- **buyer_charity_status**: registered (listed) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (uregina.ca) + name)
- **buyer_charity_designation**: C; 0010
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q3104287; university in Saskatchewan; open-access publisher; charitable organization in Canada; public research university
- **buyer_founded**: 1911-00-00 (Wikidata Q3104287, official website on the organisation's domain (https://www.uregina.ca/) + name; 2026-11-08)
- **buyer_budget_or_revenue**: revenue 145909000 Q1104069; 169141790 Q1104069; 197035093 Q1104069; 164583544 Q1104069; 197436673 Q1104069; 168641242 Q1104069; (Wikidata Q3104287, official website on the organisation's domain (https://www.uregina.ca/) + name; 2026-11-08)
- **buyer_employees**: 2097; 1915; 2202; 3127; 1770; 2042; 2169; 2317; 2353; 2325; 3642; 4008; 4016; 4213; 4354; 4609; 4677; 3951; 4281; 4686;  (Wikidata Q3104287, official website on the organisation's domain (https://www.uregina.ca/) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.uregina.ca/about/contact/index.html (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers; invoice mailing address: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoicing requirements: the lane's AP page (https://www.uregina.ca/financial-services/assets/fs-forms/dd-form-vendors-and-non-employees-sep-2026-1.pdf); payment terms: the lane's AP page (https://www.uregina.ca/financial-services/assets/fs-forms/dd-form-vendors-and-non-employees-sep-2026-1.pdf); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: accounts.payable@uregina.ca
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.uregina.ca/financial-services/assets/fs-forms/dd-form-vendors-and-non-employees-sep-2026-1.pdf
- **email_evidence_quote**: arkway Regina, SK S4S 0A2 OR Email the completed form and supporting banking document to: Accounts.Payable@uregina.ca
- **email_evidence_context**: porate cheque or an official document containing your banking information, by mail to: University of Regina Financial Services – Accounts Payable 3737 Wascana Parkway Regina, SK S4S 0A2 OR Email the completed form and supporting banking document to: Accounts.Payable@uregina.ca (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: accounts.payable@uregina.ca (invoicing/AP) | researched by the ChatGPT/Codex agent (lane chatgpt) (page opened and quoted) on 2026-10-26 | page: https://www.uregina.ca/financial-services/assets/fs-forms/dd-form-vendors-and-non-employees-sep-2026-1.pdf | quote: "arkway Regina, SK S4S 0A2 OR Email the completed form and supporting banking document to: Accounts.Payable@uregina.ca" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365 | lane file: chatgpt/chatgpt_buyer_ap_results_batch03.csv task CH-AP-00215
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1; p=quarantine; pct=2; rua=mailto:dmarc.reports@uregina.ca
- **dmarc_record_domain**: uregina.ca
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 ip4:142.3.100.0/24 ip4:142.3.152.0/24 ip4:142.3.102.0/24 ip4:142.3.220.0/24 ip4:159.203.33.209 ip4:147.182.144.101 ip4:69.167.139.85 ip4:69.167.139.85 ip4:198.187.196.100 ip4:198.187.196.130 ip4:159.183.195.16 ip4:199.244.78.223 ip4:199.244.78.224 ip4:208.75.120.0/22 ip4:205.207.104.0/22 ip4:
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoice_mailing_address**: 3737 Wascana Parkway Regina, SK S4S 0A2 (as printed on https://www.uregina.ca/financial-services/assets/fs-forms/dd-form-vendors-and-non-employees-sep-2026-1.pdf, re-read 2026-11-08)
- **invoicing_requirements**: Current vendor PO terms: Canadian funds, Net30 after later of delivery/invoice date unless agreed otherwise; PO number prominently on all documents; invoice processing after receipt/approval of all items. EFT onboarding: handwritten signature, completed authorization and void corporate cheque or off
- **payment_terms_as_published**: Net30
- **po_required_as_published**: yes (as published: Purchase Order include) (as printed on https://www.uregina.ca/supply-management-services/vendors.html, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "payment_terms": "Net30", "po_required": "yes (as published: Purchase Order include) (as printed on https://www.uregina.ca/supply-management-services/vendors.html, re-read 2026-11-08)", "mailing_address": "3737 Wascana Parkway Regina, SK S4S 0A2 (as printed on https://www.uregina.ca/financial-services/assets/fs-forms/dd-form-vendors-and-non-employees-sep-2026-1.pdf, re-read 2026-11-08)", "requirements_text": "Current vendor PO terms: Canadian funds, Net30 after later of delivery/invoice date unless agreed otherwise; PO number prominently on all documents; invoice processing after receipt/approval of all items. EFT onboarding: handwritten signature, completed authorization and void corporate cheque or off"}
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: University of Regina We use cookies to give you the best — 3737 Wascana Parkway Regina, SK S4S 0A2 (as printed on https://www.uregina.ca/financial-services/assets/fs-forms/dd-form-vendors-and-non-employees-sep-2026-1.pdf, re-read 2026-11-08) — buyer tax no. 108162124RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (uregina.ca) + name) ⏎ SUBMIT TO: accounts.payable@uregina.ca (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: contract UR-20800-18-26 (competition_number) — the source publishes the award under this tender / notice number and no separate contract number; tender UR-20800-18-26 (competition_number) | PO rule: yes (as published: Purchase Order include) ⏎ FROM / REMIT TO: SOFTCHOICE LP — Calgary, AB | GST/HST 124209297RT0001 (account derived from the BN9) | NEQ 3369689461 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their | CURRENCY: CAD | TERMS: Net30 ⏎ DESCRIPTION: Veeam Support Renewal | AMOUNT: 36,365.00 CAD
- **invoice_card_json**: {"bill_to": {"legal_name": "University of Regina We use cookies to give you the best", "legal_name_is_published": true, "address": "3737 Wascana Parkway Regina, SK S4S 0A2 (as printed on https://www.uregina.ca/financial-services/assets/fs-forms/dd-form-vendors-and-non-employees-sep-2026-1.pdf, re-read 2026-11-08)", "address_is_the_invoice_address": true, "tax_number": "108162124RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (uregina.ca) + name)", "language": "en"}, "submit_to": {"email": "accounts.payable@uregina.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "3737 Wascana Parkway Regina, SK S4S 0A2 (as printed on https://www.uregina.ca/financial-services/assets/fs-forms/dd-form-vendors-and-non-employees-sep-2026-1.pdf, re-read 2026-11-08)", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "yes (as published: Purchase Order include) (as printed on https://www.uregina.ca/supply-management-services/vendors.html, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "UR-20800-18-26 (competition_number) — the source publishes the award under this tender / notice n
- **invoice_readiness**: 11/11 invoice elements present
- **ap_grade**: A
- **ap_score**: 86
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published | missing: finance mailbox; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms published
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: contract or agreement number: UR-20800-18-26 (competition_number) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference — source ca_saskatchewan

## Vendor
- **vendor**: Softchoice
- **vendor_legal_name**: SOFTCHOICE LP
- **vendor_trading_name**: Softchoice
- **vendor_registry_id**: Québec REQ (NEQ): 3369689461
- **vendor_registry_url**: https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises
- **vendor_registered_address**: 173 Dufferin Street, Suite 200, Toronto, ON, M6K 3H7, CA
- **vendor_neq**: 3369689461 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_legal_form**: Société non constituée au Québec
- **vendor_activity_code**: CAE 5999 — Service d'informatique / solution technologique et fournisseur de services
- **vendor_employees_quebec**: De 50 à 99
- **vendor_establishments_quebec**: SOFTCHOICE (TMA394232): 3201-1751 rue Richardson, Montréal (Québec), H3K1G6; SOFTCHOICE (TMA394232): 380-1751 rue du Marais, Québec (Québec), G1M0A2
- **vendor_directors_range**: 1 to 10 directors (Corporations Canada)
- **vendor_last_annual_filing**: REQ annual declaration 2026; Corporations Canada anniversary 2019-12-31
- **vendor_address**: Calgary, AB
- **vendor_country_basis**: province code 'AB' in award location 'Calgary, AB'
- **vendor_bn9**: 124209297
- **vendor_gst_hst_derived**: 124209297RT0001
- **vendor_website**: https://www.softchoice.com
- **vendor_logo_url**: https://www.softchoice.com/assets/img/logos/softchoice-logo-new.svg
- **vendor_contacts_found_by**:  lane, referee-verified on 
- **vendor_facts_provenance**: name and address: the record's vendor block (SaskTenders - awarded competitions (Government of Saskatchewan public tender portal)); registry identity: Québec REQ (NEQ): 3369689461 status Québec REQ (NEQ): Immatriculée (2013-12-13); Corporations Canada (corporation number): Inactive (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; exact); BN9: corporations_canada 11816110 (strong match); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2013-11-21; role / billing mailboxes researched by the  lane, referee-verified on ; website: https://www.softchoice.com; NEQ: 3369689461 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_concentration_top_share**: HBI Office Plus: 2% of 209 records
- **vendor_registry_status**: Québec REQ (NEQ): Immatriculée (2013-12-13); Corporations Canada (corporation number): Inactive
- **vendor_registry_note**: another registry lists a lapsed registration (Corporations Canada (corporation number): Inactive); the primary record is alive
- **vendor_registry_match_level**: exact
- **vendor_incorporation_date**: 2013-11-21
- **vendor_years_in_business**: 13.0 (since 2013-11-21, registry date)
- **vendor_bn_source**: corporations_canada 11816110 (strong match)

## Contract
- **po_required_as_published**: yes (as published: Purchase Order include) (as printed on https://www.uregina.ca/supply-management-services/vendors.html, re-read 2026-11-08)
- **contract_status**: likely active (awarded in the last 12 months, no end date published)
- **contract_reference**: {"competition_number": "UR-20800-18-26", "competition_guid": "aff2dc1f-4a77-4fc4-8bb8-e43d212c7a89"}
- **contract_title**: Veeam Support Renewal
- **contract_description**: The University of Regina, on behalf of Information Services, is seeking renewal of support for our Veeam Data Platform Foundation.
- **contract_or_agreement_number**: UR-20800-18-26 (competition_number) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference
- **solicitation_or_tender_number**: UR-20800-18-26 (competition_number)
- **award_or_notice_id**: aff2dc1f-4a77-4fc4-8bb8-e43d212c7a89 (competition_guid) — notice id; the award is published within this notice, the source assigns no separate award id
- **contract_value**: 36365.0
- **currency**: CAD
- **award_date**: 2026-04-24
- **contract_link**: https://www.sasktenders.ca/Competitions/Print?id=aff2dc1f-4a77-4fc4-8bb8-e43d212c7a89
- **source**: SaskTenders - awarded competitions (Government of Saskatchewan public tender portal)
- **contracts_with_canadian_suppliers**: 209
- **records_last_12_months**: 47
- **record_sources**: SaskTenders - awarded competitions (Government of Saskatchewan public tender portal) (209)
- **records_with_this_vendor**: 2
- **records_in_contract_dataset**: 209 records with Canada-located vendors (this row's organisation)

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 108162124RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (SK) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **vendor_gst_hst_derived**: 124209297RT0001

## Pay on sight / grades
- **pay_on_sight**: yes
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: University of Regina We use cookies to give you the best — 3737 Wascana Parkway Regina, SK S4S 0A2 (as printed on https://www.uregina.ca/financial-services/assets/fs-forms/dd-form-vendors-and-non-employees-sep-2026-1.pdf, re-read 2026-11-08) — buyer tax no. 108162124RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (uregina.ca) + name) ⏎ SUBMIT TO: accounts.payable@uregina.ca (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: contract UR-20800-18-26 (competition_number) — the source publishes the award under this tender / notice number and no separate contract number; tender UR-20800-18-26 (competition_number) | PO rule: yes (as published: Purchase Order include) ⏎ FROM / REMIT TO: SOFTCHOICE LP — Calgary, AB | GST/HST 124209297RT0001 (account derived from the BN9) | NEQ 3369689461 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their | CURRENCY: CAD | TERMS: Net30 ⏎ DESCRIPTION: Veeam Support Renewal | AMOUNT: 36,365.00 CAD
- **invoice_card_json**: {"bill_to": {"legal_name": "University of Regina We use cookies to give you the best", "legal_name_is_published": true, "address": "3737 Wascana Parkway Regina, SK S4S 0A2 (as printed on https://www.uregina.ca/financial-services/assets/fs-forms/dd-form-vendors-and-non-employees-sep-2026-1.pdf, re-read 2026-11-08)", "address_is_the_invoice_address": true, "tax_number": "108162124RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (uregina.ca) + name)", "language": "en"}, "submit_to": {"email": "accounts.payable@uregina.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "3737 Wascana Parkway Regina, SK S4S 0A2 (as printed on https://www.uregina.ca/financial-services/assets/fs-forms/dd-form-vendors-and-non-employees-sep-2026-1.pdf, re-read 2026-11-08)", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "yes (as published: Purchase Order include) (as printed on https://www.uregina.ca/supply-management-services/vendors.html, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "UR-20800-18-26 (competition_number) — the source publishes the award under this tender / notice n
- **invoice_readiness**: 11/11 invoice elements present
- **ap_grade**: A
- **ap_score**: 86
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published | missing: finance mailbox; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms published
- **facts_provenance_json**: {"mailbox": ["accounts.payable@uregina.ca (invoicing/AP)", "researched by the ChatGPT/Codex agent (lane chatgpt) (page opened and quoted) on 2026-10-26", "page: https://www.uregina.ca/financial-services/assets/fs-forms/dd-form-vendors-and-non-employees-sep-2026-1.pdf", "quote: \"arkway Regina, SK S4S 0A2 OR Email the completed form and supporting banking document to: Accounts.Payable@uregina.ca\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365", "lane file: chatgpt/chatgpt_buyer_ap_results_batch03.csv task CH-AP-00215"], "buyer_facts": ["address and phone: the buyer's own site, https://www.uregina.ca/about/contact/index.html (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers", "invoice mailing address: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoicing requirements: the lane's AP page (https://www.uregina.ca/financial-services/assets/fs-forms/dd-form-vendors-and-non-employees-sep-2026-1.pdf)", "payment terms: the lane's AP page (https:/

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.uregina.ca/financial-services/assets/fs-forms/dd-form-vendors-and-non-employees-sep-2026-1.pdf | 2026-11-08 | ok |  |  |  |  | 3737 Wascana Parkway Regina, SK S4S 0A2 |  |  |  |  |

## Buyer site facts (org_extras, uregina.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: University of Regina We use cookies to give you the best
- **legal_name_url**: https://www.uregina.ca/
- **legal_name_quote**: Careers Contact U of R Campus Maps Policies Privacy & Terms of Use Student Central UR Source © 2026 University of Regina We use cookies to give you the best website experience. By continuing to use our website, you are agreeing to the Web Privacy and Terms
- **logo_url**: https://www.uregina.ca/files/assets/images/uofr-og-image.png
- **logo_basis**: og:image of the home page
- **domain**: uregina.ca
- **key**: b:c127a69d968d1bff
- **name**: University of Regina
- **website**: https://uregina.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: University
- **legal_name_stated_url**: https://www.uregina.ca/about/index.html
- **legal_name_stated_quote**: About the U of R | University of Regina Skip to main content Students Faculty & Staff Alumni & Friends Give Close Navigation Abou
- **mentions**: {'payment_method': {'text': 'interactive virtual tour and explore key landmarks, classrooms, and student spaces befo', 'url': 'https://www.uregina.ca/about/contact/maps-directions/index.html', 'quote': 'n Map Full Screen Map College Ave Campus Virtual Campus Tour Discover campus from anywhere! Take an interactive virtual tour and explore key landmarks, classrooms, and student spaces before you visit. Travel to Regina Campus Walk or Bike Through Wascana Centre'}}
- **linkedin_url**: https://ca.linkedin.com/school/university-of-regina/
- **tel_links**: 3065854999; 3065854407; 306-585-4776; 306-585-5487; +1-306-585-4503; +1-877-779-4723; +1-306-585-5480; +1-306-585-4926; 

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "3737 Wascana Parkway, Regina, SK S4S 0A2", "address_country": "CA", "address_url": "https://www.uregina.ca/about/contact/index.html", "address_method": "pattern", "address_quote": "culty Name, Contact Person University of Regina 3737 Wascana Parkway Regina, SK S4S 0A2 Emergency Numbers Emergency Number: 306-585-4999 (Available 24/7) Non-Emergency", "phone": "306-585-4999", "phone_url": "https://www.uregina.ca/about/contact/index.html", "emails": "service.desk@uregina.ca", "emails_url": "https://www.uregina.ca/about/contact/index.html", "domain": "uregina.ca", "key": "b:c127a69d968d1bff", "name": "University of Regina", "website": "https://uregina.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, softchoice.com)
- **status**: ok
- **pages**: 1
- **language**: en
- **logo_url**: https://www.softchoice.com/assets/img/logos/softchoice-logo-new.svg
- **logo_basis**: logo image in the site header
- **domain**: softchoice.com
- **key**: vendor:Softchoice Canada Corp
- **name**: Softchoice Canada Corp
- **website**: https://softchoice.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2

## Vendor role mailboxes found on its site (org_contacts)
_not read_

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | University of Regina | Q3104287 | official website on the organisation's domain (https://www.uregina.ca/) + name |  | University of Regina | Université de Regina | university in Saskatchewan; open-access publisher; charitable organization in Canada; public research university |  | Canada | 1911-00-00 | Regina |
| v | SOFTCHOICE LP |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "b:c127a69d968d1bff",
 "ap_contact_team": {
  "emails": [
   "financial.services@uregina.ca",
   "accounts.payable@uregina.ca",
   "Accounts.Payable@uregina.ca",
   "purchase@uregina.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": "Current vendor PO terms: Canadian funds, Net30 after later of delivery/invoice date unless agreed otherwise; PO number prominently on all documents; invoice processing after receipt/approval of all items. EFT onboarding: handwritten signature, completed authorization and void corporate cheque or official bank-information document; send to stated AP email or form-return address.",
  "evidence": [
   {
    "email": "financial.services@uregina.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.uregina.ca/financial-services/forms.html",
    "quote": "first check the Financial Services forms page in UR Source . If you can't find the form you seek, please reach out to Financial Services at financial.services@uregina.ca . Contact Us Front Counter Hours Monday to Friday 8:15 a.m. - 4:15 p.m. Location: Administration Humanities Building AH2",
    "retrieved_date": "2026-10-26",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "University of Regina",
    "task_id": "CH-AP-00215"
   },
   {
    "email": "accounts.payable@uregina.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.uregina.ca/financial-services/assets/fs-forms/dd-form-vendors-and-non-employees-dec-2019.pdf",
    "quote": "ounts Payable 3737 Wascana Parkway Regina, SK. S4S 0A2 OR, please fax/email this form and a void corporate cheque to: 306-585-5140 (FAX) OR Accounts.Payable@uregina.ca",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_deep01.csv",
    "org": "University of Regina",
    "task_id": "CL-DP-02039"
   },
   {
    "email": "financial.services@uregina.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.uregina.ca/financial-services/forms.html",
    "quote": "first check the Financial Services forms page in UR Source . If you can't find the form you seek, please reach out to Financial Services at financial.services@uregina.ca . Contact Us Front Counter Hours Monday to Friday 8:15 a.m. - 4:15 p.m. Location: Administration Humanities Building AH2",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "University of Regina",
    "task_id": "CL-WS-00051"
   },
   {
    "email": "accounts.payable@uregina.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.uregina.ca/financial-services/assets/fs-forms/dd-form-vendors-and-non-employees-dec-2019.pdf",
    "quote": "ounts Payable 3737 Wascana Parkway Regina, SK. S4S 0A2 OR, please fax/email this form and a void corporate cheque to: 306-585-5140 (FAX) OR Accounts.Payable@uregina.ca",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "University of Regina",
    "task_id": "CL-WS-00051"
   },
   {
    "email": "Accounts.Payable@uregina.ca",
    "type": "supplier_payment",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": "Current vendor PO terms: Canadian funds, Net30 after later of delivery/invoice date unless agreed otherwise; PO number prominently on all documents; invoice processing after receipt/approval of all items. EFT onboarding: handwritten signature, completed authorization and void corporate cheque or official bank-information document; send to stated AP email or form-return address.",
    "applies_to": "whole_organisation",
    "page_url": "https://www.uregina.ca/financial-services/assets/fs-forms/dd-form-vendors-and-non-employees-sep-2026-1.pdf",
    "quote": "arkway Regina, SK S4S 0A2 OR Email the completed form and supporting banking document to: Accounts.Payable@uregina.ca",
    "retrieved_date": "2026-10-26",
    "found_by": "chatgpt",
    "verification": "verified",
    "source_file": "chatgpt_buyer_ap_results_batch03.csv",
    "org": "University of Regina",
    "task_id": "CH-AP-00215"
   },
   {
    "email": "purchase@uregina.ca",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.uregina.ca/about/contact/index.html",
    "quote": "Student Affairs Supply Management Services E-mail: purchase@uregina.ca Phone: 306-585-5003 Fax: 306-585-4985 Supply Management Services University of Regina Logo Search U of R Search Ready to Discover",
    "retrieved_date": "2026-10-26",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "University of Regina",
    "task_id": "CH-AP-00215"
   },
   {
    "email": "purchase@uregina.ca",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.uregina.ca/supply-management-services/",
    "quote": "Regina, Saskatchewan Canada S4S 0A2 Fina
```

## PO-level open data naming this buyer
_none_

## Contract records between the pair (dataset)
| record_id | source | status | title | value | currency | start | end | identifiers | link |
|---|---|---|---|---|---|---|---|---|---|
| ca_saskatchewan:aff2dc1f-4a77-4fc4-8bb8-e43d212c7a89:0 | ca_saskatchewan | end_date_unknown | Veeam Support Renewal | 36365.0 | CAD |  |  | {"competition_number": "UR-20800-18-26", "competition_guid": "aff2dc1f-4a77-4fc4-8bb8-e43d212c7a89"} | https://www.sasktenders.ca/Competitions/Print?id=aff2dc1f-4a77-4fc4-8bb8-e43d212c7a89 |
| ca_saskatchewan:a49d43e8-fac2-4aa2-a958-fed4a6cf2bed:0 | ca_saskatchewan | end_date_unknown | Panoramic Cameras - FM | 26807.94 | CAD |  |  | {"competition_number": "88011-06-25", "competition_guid": "a49d43e8-fac2-4aa2-a958-fed4a6cf2bed"} | https://www.sasktenders.ca/Competitions/Print?id=a49d43e8-fac2-4aa2-a958-fed4a6cf2bed |

## The buyer's other Canadian-vendor records (first 60 of 207)
| record_id | vendor | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_saskatchewan:e660f858-fb9f-4177-9ab1-5633a070369a:0 | Benchmark Public Relations | Consultant for a Targeted Environmental Scan and Write a 5 Year Dimensions Action Plan | 27000.0 |  |  | https://www.sasktenders.ca/Competitions/Print?id=e660f858-fb9f-4177-9ab1-5633a070369a |
| ca_saskatchewan:7fc3af3e-5ff7-48fc-b427-414a71f630c3:0 | Compugen | FOURTEEN (14) APPLE M4 24-inch ALL-IN-ONE DESKSTOP COMPUTERS & TWENTY (20) APPLE iPAD AIR 11 | 81340.0 |  |  | https://www.sasktenders.ca/Competitions/Print?id=7fc3af3e-5ff7-48fc-b427-414a71f630c3 |
| ca_saskatchewan:18fee295-e439-442b-a98a-243d128073d6:0 | Fisher Scientific | Ultra-Low Temperature Freezer for Faculty of Biology | 24938.37 |  |  | https://www.sasktenders.ca/Competitions/Print?id=18fee295-e439-442b-a98a-243d128073d6 |
| ca_saskatchewan:c208259b-34d3-4a75-b471-b73ce76d7cad:0 | L.U.N.A. Restorations Inc. o/a Lydale Property Restoration | Emergency Disaster Restoration Services |  |  |  | https://www.sasktenders.ca/Competitions/Print?id=c208259b-34d3-4a75-b471-b73ce76d7cad |
| ca_saskatchewan:c208259b-34d3-4a75-b471-b73ce76d7cad:1 | Restorex Disaster Restoration | Emergency Disaster Restoration Services |  |  |  | https://www.sasktenders.ca/Competitions/Print?id=c208259b-34d3-4a75-b471-b73ce76d7cad |
| ca_saskatchewan:0fd6f2ed-de5f-4ffc-a3cf-7e26f5b83937:0 | MS Corp, dba Softlanding Solutions | Microsoft 365 Tenant Migration | 159900.0 |  |  | https://www.sasktenders.ca/Competitions/Print?id=0fd6f2ed-de5f-4ffc-a3cf-7e26f5b83937 |
| ca_saskatchewan:72e13e8d-8bf5-4d97-aa3b-d3c37f95e37e:0 | Wood Wyant Canada | Custodial Equipment - Service Maintenance |  |  |  | https://www.sasktenders.ca/Competitions/Print?id=72e13e8d-8bf5-4d97-aa3b-d3c37f95e37e |
| ca_saskatchewan:aa5beda2-8ac1-4a25-a29e-5aec45afe19d:0 | Safetech Pest Control | Pest Management and Restoration |  |  |  | https://www.sasktenders.ca/Competitions/Print?id=aa5beda2-8ac1-4a25-a29e-5aec45afe19d |
| ca_saskatchewan:7592919e-9b70-4e59-84e9-9577b1ba90d9:0 | Independent Construction Management | Education Building (ED) 227 & 228 Upgrades | 199900.0 |  |  | https://www.sasktenders.ca/Competitions/Print?id=7592919e-9b70-4e59-84e9-9577b1ba90d9 |
| ca_saskatchewan:3ce99357-ce7e-430b-9c41-4fd825cc3407:0 | Park Place Technologies | Aging Dell Hardware Support Services | 25250.0 |  |  | https://www.sasktenders.ca/Competitions/Print?id=3ce99357-ce7e-430b-9c41-4fd825cc3407 |
| ca_saskatchewan:44b50277-1dd9-432b-a07f-0fe9aa55ed47:0 | Biomed Recovery & Disposal Ltd. | Broken Glass, Sharps and Biological Waste Disposal |  |  |  | https://www.sasktenders.ca/Competitions/Print?id=44b50277-1dd9-432b-a07f-0fe9aa55ed47 |
| ca_saskatchewan:6e5b02b5-efce-464a-88c9-79de346d7364:0 | Purolator Inc | Courier Services (Domestic, Transborder, International) for U of R, U of S and SK Poly |  |  |  | https://www.sasktenders.ca/Competitions/Print?id=6e5b02b5-efce-464a-88c9-79de346d7364 |
| ca_saskatchewan:b1a004e0-6fe7-4e9b-ba55-a56ec0646072:0 | Proactive Consulting | Safety Training - Facilities Management |  |  |  | https://www.sasktenders.ca/Competitions/Print?id=b1a004e0-6fe7-4e9b-ba55-a56ec0646072 |
| ca_saskatchewan:8fe1e045-8b70-4348-8aac-e00f1a667cc7:0 | Tymark Construction Ltd. | CW Level 2 Accessible Washroom | 199948.88 |  |  | https://www.sasktenders.ca/Competitions/Print?id=8fe1e045-8b70-4348-8aac-e00f1a667cc7 |
| ca_saskatchewan:e08977ee-f8bc-465f-94d5-a6b7e397f95a:0 | Independent Construction Management | Repost of Paskwaw Tower (PA) 121 Parenting Room | 75000.0 |  |  | https://www.sasktenders.ca/Competitions/Print?id=e08977ee-f8bc-465f-94d5-a6b7e397f95a |
| ca_saskatchewan:3018a168-bd59-4e27-95ae-330eb57f575c:0 | Westpoint Construction Inc | Gym 2 Flooring Replacement | 313020.0 |  |  | https://www.sasktenders.ca/Competitions/Print?id=3018a168-bd59-4e27-95ae-330eb57f575c |
| ca_saskatchewan:8f519ac0-0ac4-4c5e-99e6-b9a1826db939:0 | Independent Construction Management | CM Services - Paskwaw Tower (PA) 121 Parenting Room | 75000.0 |  |  | https://www.sasktenders.ca/Competitions/Print?id=8f519ac0-0ac4-4c5e-99e6-b9a1826db939 |
| ca_saskatchewan:bf3c7682-73f9-4a09-9978-42d638a188c9:0 | Western Cycle | Hockey Equipment - Cougars | 93000.0 |  |  | https://www.sasktenders.ca/Competitions/Print?id=bf3c7682-73f9-4a09-9978-42d638a188c9 |
| ca_saskatchewan:32db9e09-b769-4985-8efa-910ddfe7540c:0 | Loraas Disposal North Ltd. | Saskatoon Campus - Garbage & Recyclables Collection and Removal Services |  |  |  | https://www.sasktenders.ca/Competitions/Print?id=32db9e09-b769-4985-8efa-910ddfe7540c |
| ca_saskatchewan:a47d173c-3f0d-4bf7-bbf9-969d5c65d2f5:0 | Clean Harbors Canada Inc. | High Hazard Waste Collection & Disposal |  |  |  | https://www.sasktenders.ca/Competitions/Print?id=a47d173c-3f0d-4bf7-bbf9-969d5c65d2f5 |
| ca_saskatchewan:d675330c-d220-445c-983a-7163aa41bd36:0 | Capital GMC | Used Vans for Facilities Management | 93016.0 |  |  | https://www.sasktenders.ca/Competitions/Print?id=d675330c-d220-445c-983a-7163aa41bd36 |
| ca_saskatchewan:99cf1b03-9b60-4680-b78e-4c7f3b29a067:0 | Indy Construction Management Ltd. | Road and Parking Lot(s) Maintenance |  |  |  | https://www.sasktenders.ca/Competitions/Print?id=99cf1b03-9b60-4680-b78e-4c7f3b29a067 |
| ca_saskatchewan:2b0bc0b0-274c-4964-ae9a-cbeca191ae83:0 | Insightrix Research Inc | Surveys in Four (4) Provinces for Johnson-Shoyama Graduate School of Policy | 37800.0 |  |  | https://www.sasktenders.ca/Competitions/Print?id=2b0bc0b0-274c-4964-ae9a-cbeca191ae83 |
| ca_saskatchewan:33e91ea5-07d2-479f-bb84-148044b3bfc7:0 | Capital GMC | New Vans for Facilities Management | 83100.0 |  |  | https://www.sasktenders.ca/Competitions/Print?id=33e91ea5-07d2-479f-bb84-148044b3bfc7 |
| ca_saskatchewan:cb6b3add-f588-4e22-b13d-dac6a6e1afe1:0 | Spartan Controls | Pressure Relief Valves | 49000.0 |  |  | https://www.sasktenders.ca/Competitions/Print?id=cb6b3add-f588-4e22-b13d-dac6a6e1afe1 |
| ca_saskatchewan:154b4714-16d0-4a08-812d-697dba4b0c2a:0 | Concept 3 Business | Furniture Requirements for the Faculty of Social Work and Nursing (Saskatoon Site) | 213241.32 |  |  | https://www.sasktenders.ca/Competitions/Print?id=154b4714-16d0-4a08-812d-697dba4b0c2a |
| ca_saskatchewan:8c34a6d3-2603-442d-bc44-357513f7f394:0 | Waters Limited | Mass Spectrometry (LC-MS/MS) System | 5596697.97 |  |  | https://www.sasktenders.ca/Competitions/Print?id=8c34a6d3-2603-442d-bc44-357513f7f394 |
| ca_saskatchewan:468d8616-2561-4217-8671-88bbe8858e8c:0 | Aprio Inc. | Electronic Board Meeting Solution |  |  |  | https://www.sasktenders.ca/Competitions/Print?id=468d8616-2561-4217-8671-88bbe8858e8c |
| ca_saskatchewan:28184e83-03e3-4409-b0b9-d320ccea41c4:0 | Titan Sports Systems Ltd | Wood Floor Refinishing | 27295.0 |  |  | https://www.sasktenders.ca/Competitions/Print?id=28184e83-03e3-4409-b0b9-d320ccea41c4 |
| ca_saskatchewan:d3666dd2-84cc-417e-b4ab-0e20f3e80649:0 | TK Elevator Canada Limited | Campus-wide Elevator Maintenance | 84000.0 |  |  | https://www.sasktenders.ca/Competitions/Print?id=d3666dd2-84cc-417e-b4ab-0e20f3e80649 |
| ca_saskatchewan:2a0132d0-c992-4d8a-8541-6edde12b5571:0 | Bravo Tango | Marketing Campaign- Hill Levene School of Business (HLSB) | 30000.0 |  |  | https://www.sasktenders.ca/Competitions/Print?id=2a0132d0-c992-4d8a-8541-6edde12b5571 |
| ca_saskatchewan:14eb0630-1479-421c-b232-45a4902f4590:0 | Heather Switzer | Consultant for Psychology | 46080.0 |  |  | https://www.sasktenders.ca/Competitions/Print?id=14eb0630-1479-421c-b232-45a4902f4590 |
| ca_saskatchewan:7b17b41c-931d-4c3c-b9bd-943286b5fa1c:0 | Powell Canada Inc. | Substation Switchgear Supply– Project 720020 Phase I | 853359.32 |  |  | https://www.sasktenders.ca/Competitions/Print?id=7b17b41c-931d-4c3c-b9bd-943286b5fa1c |
| ca_saskatchewan:cd4a4e00-c555-4bbd-a824-750fc88420d5:0 | Gilmore Printing Services | Printing of the University of Regina Examination Booklet | 9910.0 |  |  | https://www.sasktenders.ca/Competitions/Print?id=cd4a4e00-c555-4bbd-a824-750fc88420d5 |
| ca_saskatchewan:6b58c7cd-738a-4211-b699-a94cd4d030c4:0 | The Hotel Saskatchewan | Venue to Host 2026 Alumni Awards and Sports Hall of Fame Dinner | 40516.47 |  |  | https://www.sasktenders.ca/Competitions/Print?id=6b58c7cd-738a-4211-b699-a94cd4d030c4 |
| ca_saskatchewan:62a67b04-2023-44e3-b46d-eb9e3e29f2b4:0 | Sports Connection | Preferred Supplier of Sport Apparel- Under Armour Brand |  |  |  | https://www.sasktenders.ca/Competitions/Print?id=62a67b04-2023-44e3-b46d-eb9e3e29f2b4 |
| ca_saskatchewan:3b237dde-b228-4d0e-8e14-eb1c99e8f9ac:0 | Business Furnishings | Furniture for CL 343 Admin Hub Renovation | 20397.05 |  |  | https://www.sasktenders.ca/Competitions/Print?id=3b237dde-b228-4d0e-8e14-eb1c99e8f9ac |
| ca_saskatchewan:3b237dde-b228-4d0e-8e14-eb1c99e8f9ac:1 | HBI Office Plus | Furniture for CL 343 Admin Hub Renovation | 12135.0 |  |  | https://www.sasktenders.ca/Competitions/Print?id=3b237dde-b228-4d0e-8e14-eb1c99e8f9ac |
| ca_saskatchewan:ecf2a187-598b-4c3d-97b5-f7b31c65cc92:0 | The Action Security Group Inc | Sargent IN120 Wi-Fi Locks |  |  |  | https://www.sasktenders.ca/Competitions/Print?id=ecf2a187-598b-4c3d-97b5-f7b31c65cc92 |
| ca_saskatchewan:85418a24-4f9f-410c-ad97-bed95682ad6b:0 | SW Event Technology | Audio Visual Equipment, Staging & Decor for Inspiring Leadership Forum 2026 | 91140.11 |  |  | https://www.sasktenders.ca/Competitions/Print?id=85418a24-4f9f-410c-ad97-bed95682ad6b |
| ca_saskatchewan:a7cfe119-1c90-4a34-aff9-67ca0e5ebacd:0 | HUMBOLDT ELECTRIC LIMITED | 716085 - Power Factor Correction Phase 2 | 352203.0 |  |  | https://www.sasktenders.ca/Competitions/Print?id=a7cfe119-1c90-4a34-aff9-67ca0e5ebacd |
| ca_saskatchewan:3338ff43-cce2-4938-9123-9561dac1bfbc:0 | ITC Systems | Meal Card Program |  |  |  | https://www.sasktenders.ca/Competitions/Print?id=3338ff43-cce2-4938-9123-9561dac1bfbc |
| ca_saskatchewan:0a64620c-528f-4571-b076-bb50fa4a2c46:0 | Trans Canada Contracting Ltd | 725034 CL 343 Arts Admin Hub | 194369.0 |  |  | https://www.sasktenders.ca/Competitions/Print?id=0a64620c-528f-4571-b076-bb50fa4a2c46 |
| ca_saskatchewan:026bdd71-408c-42ea-b958-071f63cbb277:0 | Marshall Salloum | University of Regina- Campus Pharmacy |  |  |  | https://www.sasktenders.ca/Competitions/Print?id=026bdd71-408c-42ea-b958-071f63cbb277 |
| ca_saskatchewan:ef8859fe-8b47-4ef6-ac54-da55a067bf6e:0 | Restorex and Cameo | Asbestos Abatement & Repair - Source List |  |  |  | https://www.sasktenders.ca/Competitions/Print?id=ef8859fe-8b47-4ef6-ac54-da55a067bf6e |
| ca_saskatchewan:9605fece-84ab-4eea-ad3f-64a81dde6e11:0 | CDW Canada, Inc. | Meta Quest 3 with Meta Horizon Managed Services for Faculty of Nursing | 35768.45 |  |  | https://www.sasktenders.ca/Competitions/Print?id=9605fece-84ab-4eea-ad3f-64a81dde6e11 |
| ca_saskatchewan:6b224e79-cdf8-42cc-a004-ff4b28c720ba:0 | Convergint Technologies | CCTV Card Access |  |  |  | https://www.sasktenders.ca/Competitions/Print?id=6b224e79-cdf8-42cc-a004-ff4b28c720ba |
| ca_saskatchewan:7ba8da22-ca70-4b33-9fb7-821344789ef0:0 | Full Steam | Kitchen Exhaust Cleaning |  |  |  | https://www.sasktenders.ca/Competitions/Print?id=7ba8da22-ca70-4b33-9fb7-821344789ef0 |
| ca_saskatchewan:42e53ec8-ead2-43ba-b88b-3b249c8fd215:0 | Clean Harbors | Laboratory Exhaust System Decontamination and Cleaning | 350000.0 |  |  | https://www.sasktenders.ca/Competitions/Print?id=42e53ec8-ead2-43ba-b88b-3b249c8fd215 |
| ca_saskatchewan:6c0cbe1a-a221-443c-b4a5-9143d88c2ece:0 | Marchildon Media Inc. | Public Relations – Community Engagement - La Cité | 34875.0 |  |  | https://www.sasktenders.ca/Competitions/Print?id=6c0cbe1a-a221-443c-b4a5-9143d88c2ece |
| ca_saskatchewan:7925bbeb-5611-4760-a8f8-1e997db7b3b8:0 | Pinchin Ltd | Asbestos Bulk Sampling and Air Monitoring Testing |  |  |  | https://www.sasktenders.ca/Competitions/Print?id=7925bbeb-5611-4760-a8f8-1e997db7b3b8 |
| ca_saskatchewan:3eebb328-4680-4f32-8b04-f528ccb18dbf:0 | Skandacor | Cutter - Printing Services | 50585.0 |  |  | https://www.sasktenders.ca/Competitions/Print?id=3eebb328-4680-4f32-8b04-f528ccb18dbf |
| ca_saskatchewan:3d2495a8-bdb8-4032-a666-f01dee3a2f9d:0 | Concept 3 | Furniture for Educational Sessional Hub in ED 386 | 38040.64 |  |  | https://www.sasktenders.ca/Competitions/Print?id=3d2495a8-bdb8-4032-a666-f01dee3a2f9d |
| ca_saskatchewan:3ce1722b-7ca4-4ce4-b911-788a1d5bfba3:0 | Christie Lites Sales | LED Conversion for Main Stage in Riddell Centre | 692058.0 |  |  | https://www.sasktenders.ca/Competitions/Print?id=3ce1722b-7ca4-4ce4-b911-788a1d5bfba3 |
| ca_saskatchewan:1f276e54-4bfe-472e-abed-b37724663347:0 | Data Communications Corp. | Printing Services for the Student Recruitment Viewbook 2025 | 20051.0 |  |  | https://www.sasktenders.ca/Competitions/Print?id=1f276e54-4bfe-472e-abed-b37724663347 |
| ca_saskatchewan:4b93fd4b-3bea-48fe-972e-7a00daed49d7:0 | Melliecent Building & Yard Maintenance | Housekeeping Cleaning Services for Housing Services | 30000.0 |  |  | https://www.sasktenders.ca/Competitions/Print?id=4b93fd4b-3bea-48fe-972e-7a00daed49d7 |
| ca_saskatchewan:c740c67d-7989-42cb-8212-64ff8d92e230:0 | Engelheim Charter Inc | Bus Charter Services - University's Cougar Teams | 200000.0 |  |  | https://www.sasktenders.ca/Competitions/Print?id=c740c67d-7989-42cb-8212-64ff8d92e230 |
| ca_saskatchewan:6bddc87a-cac6-40c3-a80c-7f2aba534c9e:0 | Changemakers | Development of a National Marketing Strategy and Execution for CIPSRT | 103500.0 |  |  | https://www.sasktenders.ca/Competitions/Print?id=6bddc87a-cac6-40c3-a80c-7f2aba534c9e |
| ca_saskatchewan:e6c21756-0bcc-40c7-8a1a-5b1f857daf4c:0 | Priority Solutions | Review of the Clinical Psychology Training Program | 47600.0 |  |  | https://www.sasktenders.ca/Competitions/Print?id=e6c21756-0bcc-40c7-8a1a-5b1f857daf4c |
| ca_saskatchewan:451715d3-3706-42aa-8091-c105f2011733:0 | Archimedia | Digital Asset Management System |  |  |  | https://www.sasktenders.ca/Competitions/Print?id=451715d3-3706-42aa-8091-c105f2011733 |
| … 147 more rows in the .json | ||||||

## The vendor's other buyers in the dataset (first 60 of 300)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_alberta_apc:AB-2025-00890:663d1c0f-9142-46b4-b05b-23f899d45db0 | Alberta Electric System Operator | Alberta Electric System Operator - Request for Proposal - Penetration Testing Services | 40000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-00890 |
| ca_alberta_apc:AB-2025-04899:19184072-d010-4641-b548-d37e8cbbf49d | Technology and Innovation | Technology and Innovation - Request for Quotes - Adobe Experience Manager Forms Maintenance and Support Renewal | 80376.4 |  |  | https://purchasing.alberta.ca/posting/AB-2025-04899 |
| ca_alberta_apc:AB-2025-06674:17423463-d4d9-46f6-95f6-70813d00a7e6 | University of Alberta | University of Alberta - Request for Proposal - Solarwinds Observability Advanced for Enterprise AE2000 Software Subscription | 444391.01 |  |  | https://purchasing.alberta.ca/posting/AB-2025-06674 |
| ca_alberta_apc:AB-2026-00821:06cf7018-8237-4dc0-b4c3-7c0efd2691dd | Technology and Innovation | Technology and Innovation - Request for Quotes - SOLARWINDS SELF-HOSTED ADVANCED A250 Subscription Licence | 74571.39 |  |  | https://purchasing.alberta.ca/posting/AB-2026-00821 |
| ca_alberta_apc:AB-2026-01700:4c95ce4d-61eb-46a5-ba54-0ccf96ac9d27 | Technology and Innovation | Technology and Innovation - Request for Quotes - VMware SaaS Purchase 2026-2027 | 357067.1 |  |  | https://purchasing.alberta.ca/posting/AB-2026-01700 |
| ca_alberta_apc:AB-2026-01798:81c4d078-e871-4b40-8900-8c1feb63ed35 | University of Calgary | University of Calgary - Request for Quotes - Veeam License Renewal | 1.0 |  |  | https://purchasing.alberta.ca/posting/AB-2026-01798 |
| ca_alberta_apc:AB-2026-01814:35f7c74d-e76e-4954-8c1a-45e99993ea81 | The Good Samaritan Society (A Lutheran Social Service Organization) | The Good Samaritan Society (A Lutheran Social Service Organization) - Request for Proposal - Microsoft License | 732996.0 |  |  | https://purchasing.alberta.ca/posting/AB-2026-01814 |
| ca_alberta_apc:AB-2026-03029:7cd74eba-6ba6-4651-9f9c-620104022512 | Town of Okotoks | Town of Okotoks - Request for Quotes - Supply of Microsoft Software Licenses | 84386.4 |  |  | https://purchasing.alberta.ca/posting/AB-2026-03029 |
| ca_bc_ministry_awards:1eea79ae91f1303b | Ministry of Finance | IBM Content Manager Software Subscription & Support Renewal | 87695.8 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:167446e43a315706 | Ministry of Technology, Innovation and Citizens' Services | IBM Annual SW Subscription Renewal (Victoria) | 30891.09 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:26af234827ef750c | Ministry of Technology, Innovation and Citizens' Services | TOAD for Oracle (Victoria) | 7502.66 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:8a8989d609d0e3c1 | Ministry of Technology, Innovation and Citizens' Services | Annual Adobe Livecycle/Reader renwals (Victoria, BC) | 53129.52 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:c0c860279f64bb3a | Ministry of Technology, Innovation and Citizens' Services | Attachmate Licenses & Support (Victoria) | 22461.05 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:5cc06791be6cda95 | Ministry of Technology, Innovation and Citizens' Services | ieSpell Corporate License (Victoria) | 8923.07 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:c19db4b271c2d009 | Ministry of Technology, Innovation and Citizens' Services | SSO Plugin Standard License (Victoria, BC) | 13273.22 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:9e6510e1a6d49db4 | Ministry of Technology, Innovation and Citizens' Services | SDSI IBM DB2 Connect Support Renewal (Victoria, BC) | 20083.44 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:a5adf8e43f53db25 | Ministry of Technology, Innovation and Citizens' Services | Attachmate Licenses (Victoria) | 92799.9 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:eb42539b68e24c3b | Ministry of Technology, Innovation and Citizens' Services | IBM Cognos BI Analytics User Licenses and Support (Victoria, BC) | 118489.73 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:fb24218434cdf46d | Ministry of Technology, Innovation and Citizens' Services | Opentext SecureShell and Exceed Maintenance | 13976.93 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:5bf576ca45010761 | Ministry of Technology, Innovation and Citizens' Services | IPSwitch March 31, 2015- March 30, 2016 support renewal | 5648.13 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:867b259729dab772 | Ministry of Technology, Innovation and Citizens' Services | i-640571 MoH Splunk Enterprise License and Support | 64716.98 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:66d2c066c1105156 | Ministry of Technology, Innovation and Citizens' Services | Ipswitch Licenses (Victoria) | 6970.86 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:9fb61882d03e8df7 | Ministry of Technology, Innovation and Citizens' Services | Exceed Maintenance (Victoria, BC) | 17733.86 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:d087b323539d9034 | Ministry of Technology, Innovation and Citizens' Services | Allround Automations PL/SQL Developer (Victoria, BC) | 11013.01 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:d65d4e090f225b22 | Ministry of Technology, Innovation and Citizens' Services | ableau Software Desktop - Professional User (Victoria, BC) | 12004.2 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:3ecd8600f4cef245 | Ministry of Technology, Innovation and Citizens' Services | Nuance DNS support renewal (Victoria) | 15959.45 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:c71cb1fdf4297c16 | Ministry of Technology, Innovation and Citizens' Services | SmartTerm Office User Site Licences (Victoria, BC) | 129819.2 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:41b14adb5749b227 | Ministry of Technology, Innovation and Citizens' Services | Tableau Desktop Professional (Victoria, BC) | 19682.55 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:7117c2f994f9aa3e | Ministry of Technology, Innovation and Citizens' Services | Techsmith true up (Victoria, BC) | 8561.28 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:61150e3b76010049 | Ministry of Citizens' Services | Splunk Enterprise Support Renewal (Victoria) | 12327.54 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:3bbe27f345029f79 | Ministry of Citizens' Services | Nuance DNS Support Renewal (Victoria) | 15351.64 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:975d74244b99493a | Ministry of Citizens' Services | Content Matrix - SharePoint Managed Capacity - Perpetual License | 122101.63 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:c79bfc9d4d0d91e0 | Ministry of Citizens' Services | Content Matrix - SharePoint Managed Capacity - Perpetual License | 122101.63 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:e59d3c4ff1b9c7c9 | Ministry of Citizens' Services | Lansweeper Ultimate Edition (Victoria) | 8174.22 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:f130d481e9dabf8d | Ministry of Citizens' Services | REQUOTE-ERWin Data Modeler Workgroup & 1 year Enterprise Maint. | 15290.44 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:deb5a114b25f1870 | Ministry of Citizens' Services | Splunk Enterprise Software Support Renewal (Victoria, BC) | 11188.89 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:239341e273fe2374 | Ministry of Citizens' Services | Lansweeper Ultimate Edition (Victoria, BC) | 7697.24 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:b9cfe6d886ee38de | Ministry of Citizens' Services | Attachmate Reflections Desktop Licenses & Maintenance (Vic, BC) | 6955.76 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:154aab4003f11b4f | Ministry of Citizens' Services | Reflection Desktop for Unix & OpenVMS (Victoria) | 11624.93 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:cf266230f2bae27a | Ministry of Citizens' Services | Reflection Desktop for Unix & OpnenVMS Licences (Victoria) | 24156.73 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:965a3339d15b2a19 | Ministry of Citizens' Services | Tidal Software Support and Maintenance (Victoria) | 12649.85 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:4b51f495f7c9f7ad | Ministry of Citizens' Services | Shareplex Standard Edition Maintenance Renewal (Victoria) | 21262.5 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:438b1ed3613f7fc2 | Ministry of Citizens' Services | MySQL Enterprise Edition Subscription License | 15855.84 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/3ebd6010-3c30-4fa8-b95d-ed2362ce863f/download/ministry-contract-awards-2019.csv |
| ca_bc_ministry_awards:fc8699737b4bfa7a | Ministry of Citizens' Services | JIRA Software Licenses (Victoria) | 25263.39 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/3ebd6010-3c30-4fa8-b95d-ed2362ce863f/download/ministry-contract-awards-2019.csv |
| ca_bc_ministry_awards:af7d039553cd53d9 | Ministry of Citizens' Services | Oracle Xpert Edition W/Quest DBA Admin Module License | 14773.92 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/3ebd6010-3c30-4fa8-b95d-ed2362ce863f/download/ministry-contract-awards-2019.csv |
| ca_bc_ministry_awards:9fa7f6580879131c | Ministry of Citizens' Services | Quest Maintenance Renewals – Various Titles (Victoria) | 205704.71 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/3ebd6010-3c30-4fa8-b95d-ed2362ce863f/download/ministry-contract-awards-2019.csv |
| ca_bc_ministry_awards:c39ccea37402a60a | Ministry of Citizens' Services | Splunk Enterprise Support Renewal (Victoria) | 13753.6 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/3ebd6010-3c30-4fa8-b95d-ed2362ce863f/download/ministry-contract-awards-2019.csv |
| ca_bc_ministry_awards:ae81e88864348c79 | Ministry of Citizens' Services | SAP Crystal Server2016 License & Support (Victoria) | 5669.53 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/3ebd6010-3c30-4fa8-b95d-ed2362ce863f/download/ministry-contract-awards-2019.csv |
| ca_bc_ministry_awards:c4a3e071097eb61d | Ministry of Citizens' Services | RStudio Connect Standard Named User  (Victoria) | 42322.56 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/b113f1d3-3a78-4e10-a978-9a73a8c44be1/download/ministry-contract-awards-apr-jun-2022.csv |
| ca_bc_ministry_awards:97443a3d6c408d05 | Liquor Distribution Branch | ITQ2023-05-08 InformaCast Advanced Notification Subscription Endpoint | 3647.5 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/e948421d-a061-4aeb-be00-46f84bec8b32/download/ministry-contract-awards-apr-jun-2023.csv |
| ca_bc_ministry_awards:d14ff0c8c7bacf9b | Liquor Distribution Branch | ITQ2023-05-23 Purchase and Renewal of Camtasia Licenses | 6100.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/e948421d-a061-4aeb-be00-46f84bec8b32/download/ministry-contract-awards-apr-jun-2023.csv |
| ca_bc_ministry_awards:9dab6626a7fd10d2 | Ministry of Citizens' Services | Quest Annual Support Renewal | 272170.97 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/ee6045f4-dcaf-4a2b-80ef-8eeb876c64a1/download/ministry-contract-awards-apr-to-jun-2020.csv |
| ca_bc_ministry_awards:3bac3c0953691764 | Ministry of Citizens' Services | Cisco Adapters & Modules (Victoria) | 9008.22 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/ee6045f4-dcaf-4a2b-80ef-8eeb876c64a1/download/ministry-contract-awards-apr-to-jun-2020.csv |
| ca_bc_ministry_awards:81a7f73f825a9e5e | Ministry of Citizens' Services | MySQL Enterprise Edition Renewal | 14746.2 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/ee6045f4-dcaf-4a2b-80ef-8eeb876c64a1/download/ministry-contract-awards-apr-to-jun-2020.csv |
| ca_bc_ministry_awards:dbf79efeb21de4fa | Ministry of Citizens' Services | Red Hat JBoss EAP Renewal Subscription | 43445.53 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/ee6045f4-dcaf-4a2b-80ef-8eeb876c64a1/download/ministry-contract-awards-apr-to-jun-2020.csv |
| ca_bc_ministry_awards:a03d37b079105ea4 | Ministry of Citizens' Services | Quest Support Renewal for the period 01-Apr-21 to 31-May-22 | 125837.72 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/500eda3c-e5a9-405d-a7c2-7443ce237387/download/ministry-contract-awards-apr-to-june-2021.csv |
| ca_bc_ministry_awards:9694ae1c0256ae42 | Ministry of Citizens' Services | IBM InfoSphere Master Data Management (MDM) (Victoria BC) | 275755.2 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/500eda3c-e5a9-405d-a7c2-7443ce237387/download/ministry-contract-awards-apr-to-june-2021.csv |
| ca_bc_ministry_awards:b9b88db2c121d312 | Ministry of Health | Jira Software Upgrade 100 Users (from 25 users) | 6143.2 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/2ff7c805-5187-4ab4-a8ec-c0f85dca97fb/download/ministry-contract-awards-jan-to-apr-2020.csv |
| ca_bc_ministry_awards:58c6a40d6d342b0d | Ministry of Citizens' Services | IBM WebSphere Support Renewal | 85977.45 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/2ff7c805-5187-4ab4-a8ec-c0f85dca97fb/download/ministry-contract-awards-jan-to-apr-2020.csv |
| ca_bc_ministry_awards:0eab596ee23cf369 | Ministry of Citizens' Services | True-up of COTS TechSmith Camtasia and TechSmith Snag | 49415.66 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/b84ec72e-30ad-4f85-be66-a26dac65a137/download/ministry-contract-awards-jan-to-mar-2021.csv |
| … 240 more rows in the .json | ||||||

## Open questions for hand research (layer 2)

- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
