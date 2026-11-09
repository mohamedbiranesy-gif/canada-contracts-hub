# S4-45 — All Saints Anglican Parish CBS ⇄ inferred: Canada Post Corporation

Stratum: **S4_routed_company_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: All Saints Anglican Parish CBS — 419 Conception Bay Highway , Conception Bay South, NL A1X 7A2 (printed next to the organisation's mailbox (as printed on http://allsaintsparish.ca/, re-read 2026-11-08))
SUBMIT TO: office@allsaintsparish.ca (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is | CURRENCY: DERIVED: EUR (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: All Saints Anglican Parish CBS (municipality / local government, NL) — inferred: no record; the organisation's type and province make a Cana
```

## Relationship
- **rank_group**: I1
- **data_quality_score**: 29
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 5
- **reverify_due**: no
- **inference_confidence**: LOW (plausible supplier only)
- **relationship_detail**: All Saints Anglican Parish CBS (municipality / local government, NL) — inferred: no record; the organisation's type and province make a Canadian supplier relationship near-certain: inferred: Canada Post Corporation | published by: inference from the buyer's type and province (no contract, payment or listing record) | vendor in Canada because: the vendor's own site, https://www.canadapost-postescanada.ca/cpc/en/our-company/transparency-and-trust/privacy-centre/info-source/additional-information.page: 'Access to Information and Privacy Canada Post Corporation 2 | status rule: inferred relationship (no record): low confidence; the buyer is an organisation located in Canada (Newfoundland and Labrador) (province from the postal code on its own page (A1X 7A2)); generic: Canada Post holds the excl
- **how_relationship_was_found**: no record; tools/org_lists.py / osm_orgs.py / the crawlers placed the organisation in Canada by type and province; the vendor named is the Canada-located supplier such bodies almost always pay (see `vendor_country_basis`)
- **keys**: ap:d07936b687c21c4a
- **tier**: I
- **grade**: 1

## Buyer
- **buyer**: All Saints Anglican Parish CBS
- **buyer_website**: https://allsaintsparish.ca
- **buyer_address**: 419 Conception Bay Highway , Conception Bay South, NL A1X 7A2 (printed next to the organisation's mailbox (as printed on http://allsaintsparish.ca/, re-read 2026-11-08))
- **buyer_phone**: 709-834-4501 (printed next to the organisation's mailbox (as printed on http://allsaintsparish.ca/, re-read 2026-11-08))
- **buyer_type**: municipality / local government
- **buyer_sector**: government: municipal
- **buyer_facts_provenance**: address: the buyer's record / buyer table
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is accounted for by the buyer under the reverse charge where applicable
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: office@allsaintsparish.ca
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: http://allsaintsparish.ca/
- **email_evidence_quote**: All Saints Anglican Parish CBS Skip to main content 709-834-4501 office@allsaintsparish.ca 419 Conception Bay Highway , Conception Bay South, NL A1X 7A2 Menu All Saints Anglican Parish CBS Leading people into a growing relationship with God through Christian Education, Pastoral Care, Outr
- **email_evidence_context**: All Saints Anglican Parish CBS Skip to main content 709-834-4501 office@allsaintsparish.ca 419 Conception Bay Highway , Conception Bay South, NL A1X 7A2 Menu All Saints Anglican Parish CBS Leading people into a growing relationship with God through Christian Education, Pastoral Care, Outreach and Fellowship Facebook now deletes Livestream (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: office@allsaintsparish.ca (general) | page from the owner's earlier extract, re-read by tools/ap_pages.py without AI on 2026-11-04 | page: http://allsaintsparish.ca/ | quote: "All Saints Anglican Parish CBS Skip to main content 709-834-4501 office@allsaintsparish.ca 419 Conception Bay Highway , Conception Bay South, NL A1X 7A2 Menu Al" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by self-hosted or other (mx.bellaliant.com) | lane file: claude/claude_buyer_ap_results_apfirst01.csv task CL-APF-000122
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by self-hosted or other (mx.bellaliant.com)
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none; sp=none; rua=mailto:dmarc.abuse@bell.ca; ri=86400; fo=1
- **dmarc_record_domain**: allsaintsparish.ca
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 mx a include:spf.bellaliant.net -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: EUR (derived from the buyer's country; CAD if the parties agreed so)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: All Saints Anglican Parish CBS — 419 Conception Bay Highway , Conception Bay South, NL A1X 7A2 (printed next to the organisation's mailbox (as printed on http://allsaintsparish.ca/, re-read 2026-11-08)) ⏎ SUBMIT TO: office@allsaintsparish.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is | CURRENCY: DERIVED: EUR (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: All Saints Anglican Parish CBS (municipality / local government, NL) — inferred: no record; the organisation's type and province make a Cana
- **invoice_card_json**: {"bill_to": {"legal_name": "All Saints Anglican Parish CBS", "legal_name_is_published": false, "address": "419 Conception Bay Highway , Conception Bay South, NL A1X 7A2 (printed next to the organisation's mailbox (as printed on http://allsaintsparish.ca/, re-read 2026-11-08))", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "office@allsaintsparish.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is", "buyer_tax_status_is_published": false, "indicative_rate": "", "currency": "DERIVED: EUR (derived from the buyer's country; C", "currency_is_published": false, "vendor_gst_hst": "119321495RT0001 (GST/HST 119321495 (RT program; account suffix not printed); QST 1006393299)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "inferred: Canada Post Corporation", "bn9": "119321495 (GST/HST registration number printed by the o
- **invoice_readiness**: 6/11 invoice elements present
- **invoice_missing**: bill-to legal name (published); PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 43
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; bill-to legal name published; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published bill-to legal name; published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; bill-to legal name and address; the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: inferred: Canada Post Corporation
- **vendor_address**: 2701 Riverside Drive, Ottawa ON K1A 0B1
- **vendor_country_basis**: the vendor's own site, https://www.canadapost-postescanada.ca/cpc/en/our-company/transparency-and-trust/privacy-centre/info-source/additional-information.page: 'Access to Information and Privacy Canada Post Corporation 2701 Riverside Drive, N1160 Ottawa ON K1A 0B1'
- **vendor_bn9**: 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)
- **vendor_gst_hst_derived**: 119321495RT0001 (GST/HST 119321495 (RT program; account suffix not printed); QST 1006393299)
- **vendor_website**: https://www.canadapost-postescanada.ca
- **vendor_phone**: 1-800-267-7651 (Credit Management Group (invoices and billing); https://www.canadapost-postescanada.ca/cpc/en/support/kb/billing/payments/what-address-should-i-send-payment-to)
- **vendor_contact_evidence_url**: https://www.canadapost-postescanada.ca/cpc/en/support/kb/billing/payments/what-address-should-i-send-payment-to
- **vendor_logo_url**: https://www.canadapost-postescanada.ca/cpc/assets/cpc/uploads/banners/personal/ccmopc-36907-secondary-hero-large.svg
- **vendor_facts_provenance**: name and address: the record's vendor block (inference from the buyer's type and province (no contract, payment or listing record)); BN9: printed on the organisation's own page (https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); phone / role e-mails / logo: the vendor's own site, https://www.canadapost-postescanada.ca/cpc/en/support/kb/billing/payments/what-address-should-i-send-payment-to (tools/org_contacts.py, org_extras.py); website: https://www.canadapost-postescanada.ca
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_bn_source**: printed on the organisation's own page (https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf)

## Contract
- **contract_status**: inferred relationship (no record): low confidence; the buyer is an organisation located in Canada (Newfoundland and Labrador) (province from the postal code on its own page (A1X 7A2)); generic: Canada Post holds the exclusive privilege of collecting, transmitting and delivering letters within Canada (Canada Post Corporation Act, s. 14); most organisations mail some letters, but not every one does
- **source**: inference from the buyer's type and province (no contract, payment or listing record)
- **contracts_with_canadian_suppliers**: 0
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is accounted for by the buyer under the reverse charge where applicable
- **invoice_currency_derived**: EUR (derived from the buyer's country; CAD if the parties agreed so)
- **vendor_gst_hst_derived**: 119321495RT0001 (GST/HST 119321495 (RT program; account suffix not printed); QST 1006393299)

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: All Saints Anglican Parish CBS — 419 Conception Bay Highway , Conception Bay South, NL A1X 7A2 (printed next to the organisation's mailbox (as printed on http://allsaintsparish.ca/, re-read 2026-11-08)) ⏎ SUBMIT TO: office@allsaintsparish.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is | CURRENCY: DERIVED: EUR (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: All Saints Anglican Parish CBS (municipality / local government, NL) — inferred: no record; the organisation's type and province make a Cana
- **invoice_card_json**: {"bill_to": {"legal_name": "All Saints Anglican Parish CBS", "legal_name_is_published": false, "address": "419 Conception Bay Highway , Conception Bay South, NL A1X 7A2 (printed next to the organisation's mailbox (as printed on http://allsaintsparish.ca/, re-read 2026-11-08))", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "office@allsaintsparish.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is", "buyer_tax_status_is_published": false, "indicative_rate": "", "currency": "DERIVED: EUR (derived from the buyer's country; C", "currency_is_published": false, "vendor_gst_hst": "119321495RT0001 (GST/HST 119321495 (RT program; account suffix not printed); QST 1006393299)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "inferred: Canada Post Corporation", "bn9": "119321495 (GST/HST registration number printed by the o
- **invoice_readiness**: 6/11 invoice elements present
- **invoice_missing**: bill-to legal name (published); PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 43
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; bill-to legal name published; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published bill-to legal name; published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; bill-to legal name and address; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["office@allsaintsparish.ca (general)", "page from the owner's earlier extract, re-read by tools/ap_pages.py without AI on 2026-11-04", "page: http://allsaintsparish.ca/", "quote: \"All Saints Anglican Parish CBS Skip to main content 709-834-4501 office@allsaintsparish.ca 419 Conception Bay Highway , Conception Bay South, NL A1X 7A2 Menu Al\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by self-hosted or other (mx.bellaliant.com)", "lane file: claude/claude_buyer_ap_results_apfirst01.csv task CL-APF-000122"], "buyer_facts": ["address: the buyer's record / buyer table"], "vendor_facts": ["name and address: the record's vendor block (inference from the buyer's type and province (no contract, payment or listing record))", "BN9: printed on the organisation's own page (https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf)", "GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected", "not automated)", "phone / role e-mails / logo: the vendor's own site, https://www.canadapost-postescanada.ca/cpc/en/support/kb/billing/payments/what-address-should-i-send-payment-to (tools/org_contacts.py, org_extras.py)", "website: https://www.canadapost-postescanada.ca"], "relationship": "no record; tools/org_lis

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http://allsaintsparish.ca/ | 2026-11-08 | ok |  |  |  | 709-834-4501 | 419 Conception Bay Highway , Conception Bay South, NL A1X 7A2 |  |  |  |  |

## Buyer site facts (org_extras, domain unknown)
_not read_

## Buyer role mailboxes found on its site (org_contacts)
_not read_

## Vendor site facts (org_extras, canadapost-postescanada.ca)
- **status**: ok
- **pages**: 1
- **language**: en
- **logo_url**: https://www.canadapost-postescanada.ca/cpc/assets/cpc/uploads/banners/personal/ccmopc-36907-secondary-hero-large.svg
- **logo_basis**: logo image on the site
- **domain**: canadapost-postescanada.ca
- **key**: b:2aa5e3d1f7b796f4
- **name**: Canada Post
- **website**: https://canadapost-postescanada.ca/
- **kind**: buyer
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
| b | All Saints Anglican Parish CBS |  |  |  |  |  |  |  |  |  |  |
| b | Canada Post | Q1032001 | official website on the organisation's domain (https://www.canadapost-postescanada.ca/) + name |  | Canada Post | Postes Canada | business; state-owned enterprise | business corporation | Canada | 1867-07-01 | Ottawa |
| v | SOCIÉTÉ CANADIENNE DES POSTES | Q1032001 | official website on the organisation's domain (https://www.canadapost-postescanada.ca/) + name |  | Canada Post | Postes Canada | business; state-owned enterprise | business corporation | Canada | 1867-07-01 | Ottawa |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "ap:d07936b687c21c4a",
 "ap_contact_team": {
  "emails": [
   "office@allsaintsparish.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "office@allsaintsparish.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "http://allsaintsparish.ca/",
    "quote": "All Saints Anglican Parish CBS Skip to main content 709-834-4501 office@allsaintsparish.ca 419 Conception Bay Highway , Conception Bay South, NL A1X 7A2 Menu All Saints Anglican Parish CBS Leading people into a growing relationship with God through Christian Education, Pastoral Care, Outr",
    "retrieved_date": "2026-11-04",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_apfirst01.csv",
    "org": "All Saints Anglican Parish CBS",
    "task_id": "CL-APF-000122"
   },
   {
    "email": "office@allsaintsparish.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "http://allsaintsparish.ca/",
    "quote": "All Saints Anglican Parish CBS Skip to main content 709-834-4501 office@allsaintsparish.ca 419 Conception Bay Highway , Conception Bay South, NL A1X 7A2 Menu All Saints Anglican Parish CBS Leading people into a growing relationship with God through Christian Education, Pastoral Care, Outr",
    "retrieved_date": "2026-11-04",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_apfirst01.csv",
    "org": "All Saints Anglican Parish CBS",
    "task_id": "CL-APF-000006"
   }
  ]
 },
 "research_status": {
  "found": 2
 },
 "queries_tried": [
  "page located by a web search for invoicing pages, read by tools/ap_pages.py, no AI",
  "page located by a web search for invoicing pages, read by tools/ap_pages.py, no AI"
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

- an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed)
- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
