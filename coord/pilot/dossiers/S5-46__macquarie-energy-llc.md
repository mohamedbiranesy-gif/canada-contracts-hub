# S5-46 — MACQUARIE ENERGY LLC ⇄ Brookfield Renewable Trading and Marketing LP

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 1 · AP grade C · missing: the vendor's GST/HST number (BN9)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: MACQUARIE ENERGY LLC — 3100, 31st Floor, 421 7th Avenue S.W., Calgary, Alberta T2P 4K9
SUBMIT TO: mcsm-einvoice@macquarie.com (invoicing/AP mailbox, confirmed by the referee) | invoice portal: https://supplier.coupahost.com/ — Coupa
REFERENCE: none in the record | PO rule: yes (as published: must include a purchase order number)
FROM / REMIT TO: BROOKFIELD RENEWABLE TRADING AND MARKETING LP (as registered: Canada's Business Registries, ON 281056739, 2026-11-08) — TORONTO, Ontario (registered office city / province; Canada's Business Registries, ON 281056739, 2026-11-08) | GST/HST number not public
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: 30 days from receipt (as printed on https://www.macquarie.com/ae/en/about/suppliers.html, re-read 20
DESCRIPTION: C28
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 84
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 6
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: MACQUARIE ENERGY LLC (utility / public corporation, jurisdiction not stated) — public contract / purchase award in the last 12 months (dated record): Brookfield Renewable Trading and Marketing LP | subject: C28 | all identifiers: {"ferc_tariff_reference": "MBR Tariff, FERC Electric Tariff, Volume No. 1, 4.0.0"} | awarded 2026-06-30 | published by: contact_address/contact_country_name (FERC EQR seller identity, 2026q2) | record: https://s3.us-west-2.amazonaws.com/pudl.catalyst.coop/ferceqr/core_ferceqr__contracts/2026q2.parquet | vendor in Canada because: contact_address/contact_country_name (FERC EQR seller identity, 2026q2)=41 Victoria Street, Gatineau, QC J8X2A1, CA | status rule: likely active (record dated in the last 12 months: contact_address/contact_country_name (FERC EQR seller identity, 2026q2))
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: lead:b0f5591160dbb6d2
- **tier**: B
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: contact_address/contact_country_name (FERC EQR seller identity, 2026q2); 0 in the contract dataset)

## Buyer
- **buyer**: MACQUARIE ENERGY LLC
- **buyer_website**: https://macquarie.com
- **buyer_address**: 3100, 31st Floor, 421 7th Avenue S.W., Calgary, Alberta T2P 4K9
- **buyer_contact_evidence_url**: https://www.macquarie.com/us/en/about/contact/locations.html
- **buyer_logo_url**: https://www.macquarie.com/assets/macq/site-wide-assets/common-icons/macquarie-logo.svg
- **buyer_type**: utility / public corporation
- **buyer_sector**: utility
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.macquarie.com/us/en/about/contact/locations.html (tools/org_contacts.py: JSON-LD / contact page; no AI); logo: og:image / logo image of the buyer's site; payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: mcsm-einvoice@macquarie.com
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.macquarie.com/assets/macq/about/supplier-portal/government-legislated-e-invoicing-malaysia.pdf
- **email_evidence_quote**: gistrant. Either Resident or Non-Resident Level 10, Menara Generali, 27 Jalan Sultan Ismail, 50250 Kuala Full Address Lumpur. Email Address mcsm-einvoice@macquarie.com Contact Number +603 2059 8833 (Country + Area Code) Macquarie Group Limited 1
- **email_evidence_context**: e 1 November 2018 Note: Applicable for SST registrant SST Resident Status Resident Note: Applicable for SST registrant. Either Resident or Non-Resident Level 10, Menara Generali, 27 Jalan Sultan Ismail, 50250 Kuala Full Address Lumpur. Email Address mcsm-einvoice@macquarie.com Contact Number +603 2059 8833 (Country + Area Code) Macquarie Group Limited 1 (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: mcsm-einvoice@macquarie.com (invoicing/AP) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-03 | page: https://www.macquarie.com/assets/macq/about/supplier-portal/government-legislated-e-invoicing-malaysia.pdf | quote: "gistrant. Either Resident or Non-Resident Level 10, Menara Generali, 27 Jalan Sultan Ismail, 50250 Kuala Full Address Lumpur. Email Address mcsm-einvoice@macqua" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Proofpoint | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-DT10-00032
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Proofpoint
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject; sp=reject; fo=1; rua=mailto:dmarc_rua@emaildefense.proofpoint.com; ruf=mailto:dmarc_ruf@emaildefense.proofpoint.com,mailto:DMARC_Forensic@macquarie.com
- **dmarc_record_domain**: macquarie.com
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 include:spf.messagelabs.com ip4:103.3.196.47 ip4:203.32.185.199 ip4:220.244.206.213 ip4:103.139.123.11 mx include:spf-005e7502.pphosted.com -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: yes (v=BIMI1; l=https://bimi.entrust.net/communications.macquarie.com/logo.svg; a=htt)
- **payment_terms_as_published**: 30 days from receipt (as printed on https://www.macquarie.com/ae/en/about/suppliers.html, re-read 2026-11-08)
- **po_required_as_published**: yes (as published: must include a purchase order number) (as printed on https://www.macquarie.com/ae/en/about/suppliers.html, re-read 2026-11-08)
- **invoice_portal_url**: https://supplier.coupahost.com/ — Coupa
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **ap_system_hint**: named on the buyer's page: Coupa
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "payment_terms": "30 days from receipt (as printed on https://www.macquarie.com/ae/en/about/suppliers.html, re-read 2026-11-08)", "po_required": "yes (as published: must include a purchase order number) (as printed on https://www.macquarie.com/ae/en/about/suppliers.html, re-read 2026-11-08)", "portal_url": "https://supplier.coupahost.com/ — Coupa", "portal_kind": "actionable supplier / invoice portal named by the buyer"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: MACQUARIE ENERGY LLC — 3100, 31st Floor, 421 7th Avenue S.W., Calgary, Alberta T2P 4K9 ⏎ SUBMIT TO: mcsm-einvoice@macquarie.com (invoicing/AP mailbox, confirmed by the referee) | invoice portal: https://supplier.coupahost.com/ — Coupa ⏎ REFERENCE: none in the record | PO rule: yes (as published: must include a purchase order number) ⏎ FROM / REMIT TO: BROOKFIELD RENEWABLE TRADING AND MARKETING LP (as registered: Canada's Business Registries, ON 281056739, 2026-11-08) — TORONTO, Ontario (registered office city / province; Canada's Business Registries, ON 281056739, 2026-11-08) | GST/HST number not public ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: 30 days from receipt (as printed on https://www.macquarie.com/ae/en/about/suppliers.html, re-read 20 ⏎ DESCRIPTION: C28
- **invoice_card_json**: {"bill_to": {"legal_name": "MACQUARIE ENERGY LLC", "legal_name_is_published": false, "address": "3100, 31st Floor, 421 7th Avenue S.W., Calgary, Alberta T2P 4K9", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "mcsm-einvoice@macquarie.com", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "https://supplier.coupahost.com/ — Coupa", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: Coupa", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "yes (as published: must include a purchase order number) (as printed on https://www.macquarie.com/ae/en/about/suppliers.html, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: must include a purchase order number) (as printed on https://www.macquarie.com/ae/en/about/suppliers.html, re-read 2026-11-08))"}, "terms": {"payment_terms": "30 days from receipt (as printed on https://www.macquarie.com/ae/en/about/suppliers.html, re-read 2026-11-08)", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); c
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: bill-to legal name (published); reference to quote (PO / contract / vendor id); vendor GST/HST number; AP phone or contact for follow-up
- **ap_grade**: C
- **ap_score**: 75
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); invoice or billing address; PO rule published; payment terms published; currency known | missing: finance mailbox; bill-to legal name published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published bill-to legal name
- **ap_payability**: not yet payable — missing: bill-to legal name and address
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: must include a purchase order number) (as printed on https://www.macquarie.com/ae/en/about/suppliers.html, re-read 2026-11-08))

## Vendor
- **vendor**: Brookfield Renewable Trading and Marketing LP
- **vendor_legal_name**: BROOKFIELD RENEWABLE TRADING AND MARKETING LP (as registered: Canada's Business Registries, ON 281056739, 2026-11-08)
- **vendor_registry_id**: 281056739 (ON)
- **vendor_registry_url**: https://ised-isde.canada.ca/cbr-rec/en/search?q=Brookfield%20Renewable%20Trading%20and%20Marketing%20LP
- **vendor_registered_address**: TORONTO, Ontario (registered office city / province; Canada's Business Registries, ON 281056739, 2026-11-08)
- **vendor_legal_form**: LIMITED PARTNERSHIP ON (Canada's Business Registries, ON 281056739, 2026-11-08)
- **vendor_country_basis**: contact_address/contact_country_name (FERC EQR seller identity, 2026q2)=41 Victoria Street, Gatineau, QC J8X2A1, CA
- **vendor_facts_provenance**: name and address: the record's vendor block (contact_address/contact_country_name (FERC EQR seller identity, 2026q2)); registry identity: 281056739 (ON) status Active (Canada's Business Registries, ON 281056739, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); incorporated / registered: 2018-10-05
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Active (Canada's Business Registries, ON 281056739, 2026-11-08)
- **vendor_incorporation_date**: 2018-10-05
- **vendor_years_in_business**: 8.1 (since 2018-10-05, registry date)

## Contract
- **po_required_as_published**: yes (as published: must include a purchase order number) (as printed on https://www.macquarie.com/ae/en/about/suppliers.html, re-read 2026-11-08)
- **contract_status**: likely active (record dated in the last 12 months: contact_address/contact_country_name (FERC EQR seller identity, 2026q2))
- **contract_reference**: {"ferc_tariff_reference": "MBR Tariff, FERC Electric Tariff, Volume No. 1, 4.0.0"}
- **contract_title**: C28
- **contract_description**: C28 (the record's title; the source publishes no separate description)
- **award_date**: 2026-06-30
- **contract_link**: https://s3.us-west-2.amazonaws.com/pudl.catalyst.coop/ferceqr/core_ferceqr__contracts/2026q2.parquet
- **source**: contact_address/contact_country_name (FERC EQR seller identity, 2026q2)
- **contracts_with_canadian_suppliers**: 7
- **records_with_this_vendor**: 1 (relationship record: contact_address/contact_country_name (FERC EQR seller identity, 2026q2); 0 in the contract dataset)
- **records_in_contract_dataset**: 7 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (AB) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: MACQUARIE ENERGY LLC — 3100, 31st Floor, 421 7th Avenue S.W., Calgary, Alberta T2P 4K9 ⏎ SUBMIT TO: mcsm-einvoice@macquarie.com (invoicing/AP mailbox, confirmed by the referee) | invoice portal: https://supplier.coupahost.com/ — Coupa ⏎ REFERENCE: none in the record | PO rule: yes (as published: must include a purchase order number) ⏎ FROM / REMIT TO: BROOKFIELD RENEWABLE TRADING AND MARKETING LP (as registered: Canada's Business Registries, ON 281056739, 2026-11-08) — TORONTO, Ontario (registered office city / province; Canada's Business Registries, ON 281056739, 2026-11-08) | GST/HST number not public ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: 30 days from receipt (as printed on https://www.macquarie.com/ae/en/about/suppliers.html, re-read 20 ⏎ DESCRIPTION: C28
- **invoice_card_json**: {"bill_to": {"legal_name": "MACQUARIE ENERGY LLC", "legal_name_is_published": false, "address": "3100, 31st Floor, 421 7th Avenue S.W., Calgary, Alberta T2P 4K9", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "mcsm-einvoice@macquarie.com", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "https://supplier.coupahost.com/ — Coupa", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: Coupa", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "yes (as published: must include a purchase order number) (as printed on https://www.macquarie.com/ae/en/about/suppliers.html, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: must include a purchase order number) (as printed on https://www.macquarie.com/ae/en/about/suppliers.html, re-read 2026-11-08))"}, "terms": {"payment_terms": "30 days from receipt (as printed on https://www.macquarie.com/ae/en/about/suppliers.html, re-read 2026-11-08)", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); c
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: bill-to legal name (published); reference to quote (PO / contract / vendor id); vendor GST/HST number; AP phone or contact for follow-up
- **ap_grade**: C
- **ap_score**: 75
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); invoice or billing address; PO rule published; payment terms published; currency known | missing: finance mailbox; bill-to legal name published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published bill-to legal name
- **ap_payability**: not yet payable — missing: bill-to legal name and address
- **facts_provenance_json**: {"mailbox": ["mcsm-einvoice@macquarie.com (invoicing/AP)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-03", "page: https://www.macquarie.com/assets/macq/about/supplier-portal/government-legislated-e-invoicing-malaysia.pdf", "quote: \"gistrant. Either Resident or Non-Resident Level 10, Menara Generali, 27 Jalan Sultan Ismail, 50250 Kuala Full Address Lumpur. Email Address mcsm-einvoice@macqua\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Proofpoint", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-DT10-00032"], "buyer_facts": ["address and phone: the buyer's own site, https://www.macquarie.com/us/en/about/contact/locations.html (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "logo: og:image / logo image of the buyer's site", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (contact_address/contact_country_name (FERC EQR

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.macquarie.com/assets/macq/about/supplier-portal/government-legislated-e-invoicing-malaysia.pdf | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, macquarie.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: Macquarie Group Limited Important information Disclosures USA PATRIOT Act
- **legal_name_url**: https://www.macquarie.com/us/en.html
- **legal_name_quote**: on this site is not a reliable indication of future performance. Follow us Contact Discover News © Macquarie Group Limited Important information Disclosures USA PATRIOT Act Privacy and cookies Manage cookie settings Sitemap
- **logo_url**: https://www.macquarie.com/assets/macq/site-wide-assets/common-icons/macquarie-logo.svg
- **logo_basis**: logo image in the site header
- **domain**: macquarie.com
- **key**: lead:b0f5591160dbb6d2
- **name**: MACQUARIE ENERGY LLC
- **website**: https://macquarie.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Macquarie Asset Management
- **legal_name_stated_url**: https://www.macquarie.com/us/en/about/company.html
- **legal_name_stated_quote**: rnance Corporate Governance Board of Directors Executive Committee Risk management Operating groups Macquarie Asset Management Banking and Financial Services Commodities and Global Markets Macquarie Capital Investors Investors
- **linkedin_url**: https://www.linkedin.com/company/macquariegroup/
- **tel_links**: +61282322336; +12122311310; +85239224772; +442030374014

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "phone": "+61 2 8550 5777", "phone_url": "https://www.macquarie.com/us/en/about/contact.html", "address": "3100, 31st Floor, 421 7th Avenue S.W., Calgary, Alberta T2P 4K9", "address_country": "CA", "address_url": "https://www.macquarie.com/us/en/about/contact/locations.html", "address_method": "pattern", "address_quote": "anada Trust Tower, Suite 3100, 31st Floor 421 7th Avenue S.W., Calgary, Alberta T2P 4K9, Canada Get directions Macquarie Group +1 403 294 9541 Level 32, Suite 3200, Br", "domain": "macquarie.com", "key": "lead:b0f5591160dbb6d2", "name": "MACQUARIE ENERGY LLC", "website": "https://macquarie.com/", "kind": "buyer", "date": "2026-11-03"}

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
| b | MACQUARIE ENERGY LLC |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:b0f5591160dbb6d2",
 "ap_contact_team": {
  "emails": [
   "mcsm-einvoice@macquarie.com",
   "cogbsdsustainableprocurement@macquarie.com",
   "vendor.support@macquarie.com"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "mcsm-einvoice@macquarie.com",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.macquarie.com/assets/macq/about/supplier-portal/government-legislated-e-invoicing-malaysia.pdf",
    "quote": "gistrant. Either Resident or Non-Resident Level 10, Menara Generali, 27 Jalan Sultan Ismail, 50250 Kuala Full Address Lumpur. Email Address mcsm-einvoice@macquarie.com Contact Number +603 2059 8833 (Country + Area Code) Macquarie Group Limited 1",
    "retrieved_date": "2026-11-03",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "MACQUARIE ENERGY LLC",
    "task_id": "CL-DT10-00032"
   },
   {
    "email": "cogbsdsustainableprocurement@macquarie.com",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.macquarie.com/us/en/about/inclusive-supply-chains.html",
    "quote": "a-component=\"link-stack\" class=\"cmp-link-stack\"> <div class=\"cmp-link-stack__container\"> <div> <a class=\"cmp-link-stack__link\" href=\"mailto:COGBSDSustainableProcurement@macquarie.com\" target=\"_self\"> <h3 class=\"cmp-link-stack__label\">Contact us</h3> <span class=\"cmp-link-stack__icon icon-a",
    "retrieved_date": "2026-11-03",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "MACQUARIE ENERGY LLC",
    "task_id": "CL-DT10-00032"
   },
   {
    "email": "vendor.support@macquarie.com",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.macquarie.com/us/en/about/suppliers.html",
    "quote": "ly Asked Questions PDF 663 KB Need further support with Macquarie MySupplier? Please contact your relationship manager or our support team: vendor.support@macquarie.com . Ensure you include ‘MySupplier’ in the subject line. Principles for Suppliers The Principles for Suppliers outline Macq",
    "retrieved_date": "2026-11-03",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "MACQUARIE ENERGY LLC",
    "task_id": "CL-DT10-00032"
   },
   {
    "email": "vendor.support@macquarie.com",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.macquarie.com/assets/macq/about/supplier-portal/coupa-supplier-invoice-submission-channels.pdf",
    "quote": ".........................................................................9 For further assistance please contact Macquarie Vendor Support – vendor.support@macquarie.com 1 1. Registration and Legal Entity / Remit-To Setup To register on CSP, simply click the link you received in invitation",
    "retrieved_date": "2026-11-03",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "MACQUARIE ENERGY LLC",
    "task_id": "CL-WS-00034"
   },
   {
    "email": "vendor.support@macquarie.com",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.macquarie.com/ae/en/about/suppliers.html",
    "quote": "ly Asked Questions PDF 663 KB Need further support with Macquarie MySupplier? Please contact your relationship manager or our support team: vendor.support@macquarie.com . Ensure you include ‘MySupplier’ in the subject line. Principles for Suppliers The Principles for Suppliers outline Macq",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "MACQUARIE ENERGY LLC",
    "task_id": "CL-WS-00030"
   }
  ]
 },
 "research_status": {
  "found": 5
 },
 "queries_tried": [
  "site crawl of www.macquarie.com (57 pages, robots.txt respected), no AI, no search engine",
  "site crawl of www.macquarie.com (57 pages, robots.txt respected), no AI, no search engine",
  "site crawl of www.macquarie.com (57 pages, robots.txt respected), no AI, no search engine",
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

## The vendor's other buyers in the dataset (first 60 of 0)
_none_

## Open questions for hand research (layer 2)

- the vendor's GST/HST number (BN9)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
