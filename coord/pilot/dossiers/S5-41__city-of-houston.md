# S5-41 — City of Houston ⇄ PerfectMind Inc. dba nextRec

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 1 · AP grade A · missing: the vendor's GST/HST number (BN9)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: City of Houston (stated on https://houstontx.gov/privacy.html) — City Hall, 901 Bagby, Second Floor, Houston, TX 77002
SUBMIT TO: finaccountspayable@houstontx.gov (invoicing/AP mailbox, confirmed by the referee) | invoice portal: https://support.ariba.com/item/view/212258 — SAP Ariba
REFERENCE: contract Project# Doc1355881683 (HPARD) (govtContractNumber) | PO rule: purchase-order terms published (as published: includes a City Purchase Order)
FROM / REMIT TO: PerfectMind Inc. dba nextRec — 4333 Still Creek Drive Floor 2, Burnaby, BC, V5C 6S6 | GST/HST number not public
TAX: Tax Exemptt Total $ 6,500 (as printed on https://houstontx.gov/housing/procurement/contracts/gci/4500300994-Gov_Connection_Inc-101122.pdf, re-read 2026-11-08) | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: net 30 (as printed on https://houstontx.gov/hcdrecovery/dr17/funding/contracts/2023/04/4500311107-sh
DESCRIPTION: Software as a Service - Project# Doc1355881683 (HPARD) PerfectMind Inc. dba NextRec
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 89
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 7
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: City of Houston (municipality / local government, jurisdiction not stated) — public contract / purchase award in the last 12 months (dated record): PerfectMind Inc. dba nextRec | subject: Software as a Service - Project# Doc1355881683 (HPARD) PerfectMind Inc. dba NextRec | contract number: Project# Doc1355881683 (HPARD) (govtContractNumber) | all identifiers: {"govtContractNumber": "Project# Doc1355881683 (HPARD)"} | awarded 2026-07-23 | published by: businessCountryCode (TEC Form 1295 CSV) | record: https://www.ethics.texas.gov/data/search/1295/1295Certificates_2026_to_2030.csv | vendor in Canada because: businessCountryCode (TEC Form 1295 CSV)=Burnaby, AE, CAN | status rule: likely active (record dated in the last 12 months: businessCountryCode (TEC Form 1295 CSV))
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: lead:1b46e2f40e85ced4
- **tier**: B
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: businessCountryCode (TEC Form 1295 CSV); 0 in the contract dataset)

## Buyer
- **buyer**: City of Houston
- **buyer_website**: https://www.houstontx.gov/
- **buyer_address**: City Hall, 901 Bagby, Second Floor, Houston, TX 77002
- **buyer_contact_evidence_url**: https://houstontx.gov/contactus/index.html
- **buyer_legal_name_as_published**: City of Houston (stated on https://houstontx.gov/privacy.html)
- **buyer_logo_url**: https://houstontx.gov/images/htvlogo-homepage.jpg
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/houstontx/
- **buyer_type**: municipality / local government
- **buyer_sector**: government: municipal
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q16555; city in the United States; big city; county seat; port city
- **buyer_founded**: 1836-08-01 (Wikidata Q16555, official website on the organisation's domain (https://houstontx.gov) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://houstontx.gov/contactus/index.html (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_exempt_status**: Tax Exemptt Total $ 6,500 (as printed on https://houstontx.gov/housing/procurement/contracts/gci/4500300994-Gov_Connection_Inc-101122.pdf, re-read 2026-11-08)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **buyer_esignature_preference**: DocuSign Envelope ID: 0C1D3D65-DCA3-49C1-, 3182459521A0 manufacture, distribution, dispe (as printed on https://houstontx.gov/hcdrecovery/dr17/funding/contracts/2023/04/4500311107-shannon_martin_finkelstein_alvarado_dunne_pc-040523.pdf, re-read 2026-11-08)
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: finaccountspayable@houstontx.gov
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.houstontx.gov/finance/acct_payable.html
- **email_evidence_quote**: vals. Additionally, all policies are adhered to and followed when processing payments. Vendor Questions Vendor questions can be directed to Finaccountspayable@houstontx.gov Note: For all other Departments, please refer to your Purchase Order for point of contact. Additional Information Pol
- **email_evidence_context**: liabilities for the City of Houston are paid accurately and timely based on the proper documentation and approvals. Additionally, all policies are adhered to and followed when processing payments. Vendor Questions Vendor questions can be directed to Finaccountspayable@houstontx.gov Note: For all other Departments, please refer to your Purchase Order for point of contact. Additional Information Policies and Executive Orders AP 2-5 Authorization and Reimbursement for Local and Out-of-Town Travel and Travel Related Expenses AP 4- (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: finaccountspayable@houstontx.gov (invoicing/AP) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-02 | page: https://www.houstontx.gov/finance/acct_payable.html | quote: "vals. Additionally, all policies are adhered to and followed when processing payments. Vendor Questions Vendor questions can be directed to Finaccountspayable@h" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00174
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1;p=none;fo=1;rua=mailto:dmarc_rua@emaildefense.proofpoint.com;ruf=mailto:dmarc_ruf@emaildefense.proofpoint.com
- **dmarc_record_domain**: houstontx.gov
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 a:tb01194smtp01.cohsmtp.houstontx.gov a:tb01194smtp02.cohsmtp.houstontx.gov a:argosapp04.sirsi.net include:spf.protection.outlook.com include:spf.mtasv.net include:_spf.salesforce.com include:spf.us.odmad.quest-on-demand.com ip4:185.250.239.105 ip4:204.235.229.87 ip4:204.235.229.88 ip4:192.23
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **payment_terms_as_published**: net 30 (as printed on https://houstontx.gov/hcdrecovery/dr17/funding/contracts/2023/04/4500311107-shannon_martin_finkelstein_alvarado_dunne_pc-040523.pdf, re-read 2026-11-08)
- **po_required_as_published**: purchase-order terms published (as published: includes a City Purchase Order) (as printed on https://houstontx.gov/hcdrecovery/dr17/funding/contracts/2023/04/4500311107-shannon_martin_finkelstein_alvarado_dunne_pc-040523.pdf, re-read 2026-11-08)
- **invoice_portal_url**: https://support.ariba.com/item/view/212258 — SAP Ariba
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **ap_system_hint**: named on the buyer's page: SAP Ariba, ariba
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "payment_terms": "net 30 (as printed on https://houstontx.gov/hcdrecovery/dr17/funding/contracts/2023/04/4500311107-shannon_martin_finkelstein_alvarado_dunne_pc-040523.pdf, re-read 2026-11-08)", "po_required": "purchase-order terms published (as published: includes a City Purchase Order) (as printed on https://houstontx.gov/hcdrecovery/dr17/funding/contracts/2023/04/4500311107-shannon_martin_finkelstein_alvarado_dunne_pc-040523.pdf, re-read 2026-11-08)", "portal_url": "https://support.ariba.com/item/view/212258 — SAP Ariba", "portal_kind": "actionable supplier / invoice portal named by the buyer"}
- **invoice_currency_derived**: USD (derived from the buyer's country; CAD if the parties agreed so)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: City of Houston (stated on https://houstontx.gov/privacy.html) — City Hall, 901 Bagby, Second Floor, Houston, TX 77002 ⏎ SUBMIT TO: finaccountspayable@houstontx.gov (invoicing/AP mailbox, confirmed by the referee) | invoice portal: https://support.ariba.com/item/view/212258 — SAP Ariba ⏎ REFERENCE: contract Project# Doc1355881683 (HPARD) (govtContractNumber) | PO rule: purchase-order terms published (as published: includes a City Purchase Order) ⏎ FROM / REMIT TO: PerfectMind Inc. dba nextRec — 4333 Still Creek Drive Floor 2, Burnaby, BC, V5C 6S6 | GST/HST number not public ⏎ TAX: Tax Exemptt Total $ 6,500 (as printed on https://houstontx.gov/housing/procurement/contracts/gci/4500300994-Gov_Connection_Inc-101122.pdf, re-read 2026-11-08) | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: net 30 (as printed on https://houstontx.gov/hcdrecovery/dr17/funding/contracts/2023/04/4500311107-sh ⏎ DESCRIPTION: Software as a Service - Project# Doc1355881683 (HPARD) PerfectMind Inc. dba NextRec
- **invoice_card_json**: {"bill_to": {"legal_name": "City of Houston (stated on https://houstontx.gov/privacy.html)", "legal_name_is_published": true, "address": "City Hall, 901 Bagby, Second Floor, Houston, TX 77002", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "finaccountspayable@houstontx.gov", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "https://support.ariba.com/item/view/212258 — SAP Ariba", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: SAP Ariba, ariba", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "purchase-order terms published (as published: includes a City Purchase Order) (as printed on https://houstontx.gov/hcdrecovery/dr17/funding/contracts/2023/04/4500311107-shannon_martin_finkelstein_alvarado_dunne_pc-040523.pdf, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "Project# Doc1355881683 (HPARD) (govtContractNumber)", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: Project# Doc1355881683 (HPARD) (govtContractNumber) — source us_tx_form1295"}, "terms": {"payment_terms": "net 30 (as printed on https://houstontx.gov/hcdrecovery/dr17/funding/contracts/2023/04/4500311107-shannon_martin_finkelstein_alvarado_dunne_pc-040523.pdf, re-read 2026-11-08)", "payment_method": ""
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: vendor GST/HST number; vendor legal name; AP phone or contact for follow-up
- **ap_grade**: A
- **ap_score**: 83
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known | missing: finance mailbox; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: contract or agreement number: Project# Doc1355881683 (HPARD) (govtContractNumber) — source us_tx_form1295

## Vendor
- **vendor**: PerfectMind Inc. dba nextRec
- **vendor_address**: 4333 Still Creek Drive Floor 2, Burnaby, BC, V5C 6S6
- **vendor_country_basis**: businessCountryCode (TEC Form 1295 CSV)=Burnaby, AE, CAN
- **vendor_website**: https://blog.nextrec.com/
- **vendor_emails**: support@perfectmind.com
- **vendor_phone**: 877-737-8030
- **vendor_contact_evidence_url**: https://www.nextrec.com/company/contact
- **vendor_logo_url**: https://blog.nextrec.com/hs-fs/hubfs/NextRec_Logo_Color-1.png?width=200&height=59&name=NextRec_Logo_Color-1.png
- **vendor_website_basis**: found by a web search, confirmed by reading the site on 2026-11-08: https://blog.nextrec.com/ (tudies White Papers Webinars E-books SUPPORT Knowledge Base Community Groups Contact Us About Us Xplor Recreation Software PerfectMind Software POLICIES Terms o)
- **vendor_facts_provenance**: name and address: the record's vendor block (businessCountryCode (TEC Form 1295 CSV)); phone / role e-mails / logo: the vendor's own site, https://www.nextrec.com/company/contact (tools/org_contacts.py, org_extras.py); website: https://blog.nextrec.com/
- **vendor_concentration_top_share**: no dataset record for this pair / buyer

## Contract
- **po_required_as_published**: purchase-order terms published (as published: includes a City Purchase Order) (as printed on https://houstontx.gov/hcdrecovery/dr17/funding/contracts/2023/04/4500311107-shannon_martin_finkelstein_alvarado_dunne_pc-040523.pdf, re-read 2026-11-08)
- **contract_status**: likely active (record dated in the last 12 months: businessCountryCode (TEC Form 1295 CSV))
- **contract_reference**: {"govtContractNumber": "Project# Doc1355881683 (HPARD)"}
- **contract_title**: Software as a Service - Project# Doc1355881683 (HPARD) PerfectMind Inc. dba NextRec
- **contract_description**: Software as a Service - Project# Doc1355881683 (HPARD) PerfectMind Inc. dba NextRec (the record's title; the source publishes no separate description)
- **contract_or_agreement_number**: Project# Doc1355881683 (HPARD) (govtContractNumber)
- **award_date**: 2026-07-23
- **contract_link**: https://www.ethics.texas.gov/data/search/1295/1295Certificates_2026_to_2030.csv
- **source**: businessCountryCode (TEC Form 1295 CSV)
- **contracts_with_canadian_suppliers**: 4
- **records_with_this_vendor**: 1 (relationship record: businessCountryCode (TEC Form 1295 CSV); 0 in the contract dataset)
- **records_in_contract_dataset**: 4 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **invoice_currency_derived**: USD (derived from the buyer's country; CAD if the parties agreed so)

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: City of Houston (stated on https://houstontx.gov/privacy.html) — City Hall, 901 Bagby, Second Floor, Houston, TX 77002 ⏎ SUBMIT TO: finaccountspayable@houstontx.gov (invoicing/AP mailbox, confirmed by the referee) | invoice portal: https://support.ariba.com/item/view/212258 — SAP Ariba ⏎ REFERENCE: contract Project# Doc1355881683 (HPARD) (govtContractNumber) | PO rule: purchase-order terms published (as published: includes a City Purchase Order) ⏎ FROM / REMIT TO: PerfectMind Inc. dba nextRec — 4333 Still Creek Drive Floor 2, Burnaby, BC, V5C 6S6 | GST/HST number not public ⏎ TAX: Tax Exemptt Total $ 6,500 (as printed on https://houstontx.gov/housing/procurement/contracts/gci/4500300994-Gov_Connection_Inc-101122.pdf, re-read 2026-11-08) | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: net 30 (as printed on https://houstontx.gov/hcdrecovery/dr17/funding/contracts/2023/04/4500311107-sh ⏎ DESCRIPTION: Software as a Service - Project# Doc1355881683 (HPARD) PerfectMind Inc. dba NextRec
- **invoice_card_json**: {"bill_to": {"legal_name": "City of Houston (stated on https://houstontx.gov/privacy.html)", "legal_name_is_published": true, "address": "City Hall, 901 Bagby, Second Floor, Houston, TX 77002", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "finaccountspayable@houstontx.gov", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "https://support.ariba.com/item/view/212258 — SAP Ariba", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: SAP Ariba, ariba", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "purchase-order terms published (as published: includes a City Purchase Order) (as printed on https://houstontx.gov/hcdrecovery/dr17/funding/contracts/2023/04/4500311107-shannon_martin_finkelstein_alvarado_dunne_pc-040523.pdf, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "Project# Doc1355881683 (HPARD) (govtContractNumber)", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: Project# Doc1355881683 (HPARD) (govtContractNumber) — source us_tx_form1295"}, "terms": {"payment_terms": "net 30 (as printed on https://houstontx.gov/hcdrecovery/dr17/funding/contracts/2023/04/4500311107-shannon_martin_finkelstein_alvarado_dunne_pc-040523.pdf, re-read 2026-11-08)", "payment_method": ""
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: vendor GST/HST number; vendor legal name; AP phone or contact for follow-up
- **ap_grade**: A
- **ap_score**: 83
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known | missing: finance mailbox; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **facts_provenance_json**: {"mailbox": ["finaccountspayable@houstontx.gov (invoicing/AP)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-02", "page: https://www.houstontx.gov/finance/acct_payable.html", "quote: \"vals. Additionally, all policies are adhered to and followed when processing payments. Vendor Questions Vendor questions can be directed to Finaccountspayable@h\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00174"], "buyer_facts": ["address and phone: the buyer's own site, https://houstontx.gov/contactus/index.html (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.houstontx.gov/finance/acct_payable.html | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, houstontx.gov)
- **status**: ok
- **pages**: 5
- **language**: en
- **logo_url**: https://houstontx.gov/images/htvlogo-homepage.jpg
- **logo_basis**: logo image on the site
- **domain**: houstontx.gov
- **key**: lead:1b46e2f40e85ced4
- **name**: City of Houston
- **website**: https://houstontx.gov/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: City of Houston
- **legal_name_stated_url**: https://houstontx.gov/privacy.html
- **legal_name_stated_quote**: City of Houston eGovernment Center - Privacy Policy RESIDENTS 311 Help and Info Animal Adoptions Trash / Recycling
- **linkedin_url**: https://www.linkedin.com/company/houstontx/

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "City Hall, 901 Bagby, Second Floor, Houston, TX 77002", "address_country": "US", "address_url": "https://houstontx.gov/contactus/index.html", "address_method": "address-tag", "address_quote": "Houston, TX 77251 Physical Address: City of Houston 901 Bagby Houston, TX 77002 City Hall Annex Address: 900 Bagby Houston, TX 77002 City Switchboard: 713.837.0311 or 3", "emails": "customer.service@houstontx.gov", "emails_url": "https://houstontx.gov/contactus/index.html", "domain": "houstontx.gov", "key": "lead:1b46e2f40e85ced4", "name": "City of Houston", "website": "https://houstontx.gov/", "kind": "buyer", "date": "2026-11-03"}

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
| b | City of Houston | Q16555 | official website on the organisation's domain (https://houstontx.gov) + name |  | Houston | Houston | city in the United States; big city; county seat; port city |  | United States | 1836-08-01 |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:1b46e2f40e85ced4",
 "ap_contact_team": {
  "emails": [
   "finaccountspayable@houstontx.gov",
   "houstonpurchasing@houstontx.gov",
   "finance.director@houstontx.gov"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "finaccountspayable@houstontx.gov",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.houstontx.gov/finance/acct_payable.html",
    "quote": "vals. Additionally, all policies are adhered to and followed when processing payments. Vendor Questions Vendor questions can be directed to Finaccountspayable@houstontx.gov Note: For all other Departments, please refer to your Purchase Order for point of contact. Additional Information Pol",
    "retrieved_date": "2026-11-02",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "City of Houston",
    "task_id": "CL-WS-00174"
   },
   {
    "email": "houstonpurchasing@houstontx.gov",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.houstontx.gov/bizwithhou/",
    "quote": "Supplier Management Team: 832.393.8800 Email: HoustonPurchasing@houstontx.gov SPD's Vision To promote fairness, innovation and sustainability through integrity and excellence. Home • 311 • CONTACT",
    "retrieved_date": "2026-11-02",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "City of Houston",
    "task_id": "CL-LT-00271"
   },
   {
    "email": "finance.director@houstontx.gov",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.houstontx.gov/finance/",
    "quote": "ort Finance Contact Melissa Dubowski, Finance Director Finance Department 611 Walker, 10th Floor Houston, TX 77002 Ph: 832.393.9120 E-Mail: finance.director@houstontx.gov Ambulance Billing Questions: Ph: 713.837.0311 E-Mail:",
    "retrieved_date": "2026-11-02",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "City of Houston",
    "task_id": "CL-LT-00271"
   }
  ]
 },
 "research_status": {
  "found": 3
 },
 "queries_tried": [
  "site crawl of www.houstontx.gov (60 pages, robots.txt respected), no AI, no search engine",
  "site crawl of www.houstontx.gov (60 pages, robots.txt respected), no AI, no search engine",
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

- the vendor's GST/HST number (BN9)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
