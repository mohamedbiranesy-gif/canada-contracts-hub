# S5-27 — The Ohio State University ⇄ STEPS Public Art

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 1 · AP grade C · missing: the vendor's GST/HST number (BN9); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: The Ohio State University — 2009 Millikin Road, Columbus, OH, 43210
SUBMIT TO: apinvoices@osu.edu (invoicing/AP mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: STEPS Public Art — 39 Queens Quay E, Toronto, ON, M5E0A4, Canada | GST/HST number not public
TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state  | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Resources | STEPS Public Art
```

## Relationship
- **rank_group**: E4
- **data_quality_score**: 64
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 1
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: The Ohio State University (organisation (type not stated in the record), jurisdiction not stated) — linked from the Canada-located vendor's site (weakest listed relationship): STEPS Public Art | subject: Resources | STEPS Public Art | published by: the Canada-located vendor's own website | record: https://stepspublicart.org/project/resources/ | vendor in Canada because: vendor located in Canada (wd)=stepspublicart.org | status rule: linked from a page of the Canada-located vendor's site (not a client page)
- **how_relationship_was_found**: tools/provider_mentions.py / news_match.py found the buyer linked from the vendor's own site or release
- **keys**: lead:0ae27d8e8d3307bc
- **tier**: E
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: The Ohio State University
- **buyer_website**: https://clas.osu.edu/
- **buyer_address**: 2009 Millikin Road, Columbus, OH, 43210
- **buyer_phone**: 614-292-3956
- **buyer_contact_evidence_url**: https://clas.osu.edu/contact
- **buyer_legal_name_as_published**: The Ohio State University
- **buyer_logo_url**: https://clas.osu.edu/modules/contrib/bux/dist/images/osu-logos/navbar/osu-navbar.svg
- **buyer_website_status**: site answers
- **buyer_type**: university / college (from the organisation's name / web domain)
- **buyer_sector**: education: post-secondary
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://clas.osu.edu/contact (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; invoicing requirements: the lane's AP page (https://busfin.osu.edu/university-business/controller/tips-and-tricks/supplier-invoice-process-tips-and-tricks)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: apinvoices@osu.edu
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://busfin.osu.edu/university-business/controller/tips-and-tricks/supplier-invoice-process-tips-and-tricks
- **email_evidence_quote**: ess will result in the timely payment of suppliers. 1. Supplier submits to Accounts Payable via EDI or email invoice to apinvoices@osu.edu 2. Brainware/Onbase system for the pairing process* 3. Workday for the matching process** 4. Requestor approves certain invoices (see roles section bel
- **mailbox_provenance**: apinvoices@osu.edu (invoicing/AP) | researched by the ChatGPT/Codex agent (lane chatgpt) (page opened and quoted) on 2026-11-08 | page: https://busfin.osu.edu/university-business/controller/tips-and-tricks/supplier-invoice-process-tips-and-tricks | quote: "ess will result in the timely payment of suppliers. 1. Supplier submits to Accounts Payable via EDI or email invoice to apinvoices@osu.edu 2. Brainware/Onbase s" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: not checked yet | DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by not checked | lane file: chatgpt/chatgpt_verify_buyer_ap_results_batch01.csv task CH-VF-00023
- **email_deliverability**: not checked yet
- **email_security_posture**: DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by not checked
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject; sp=reject; rua=mailto:dmarc_agg@vali.email,mailto:dmarc_rua@emaildefense.proofpoint.com; ruf=mailto:dmarc_ruf@emaildefense.proofpoint.com; fo=1;
- **dmarc_record_domain**: osu.edu
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 ip4:140.254.54.0/26 ip4:131.187.90.204 ip4:131.187.90.205 ip4:128.146.86.128/27 ip4:128.146.193.0/27 ip4:128.146.163.0/26 ip4:148.163.151.149 ip4:148.163.155.97 ip4:128.146.138.0/25 ip4:128.146.17.48 ip4:128.146.17.76 ip4:128.146.17.77 ip4:128.146.163.14 ip4:128.146.163.18 ip4:128.146.163.21 
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements**: No supplier invoicing address, AP mailbox, or invoice portal was found on the organisation's site. Suppliers have no published invoice route.
- **ap_system_hint**: named on the buyer's page: Workday
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "requirements_text": "No supplier invoicing address, AP mailbox, or invoice portal was found on the organisation's site. Suppliers have no published invoice route."}
- **invoice_currency_derived**: USD (derived from the buyer's country; CAD if the parties agreed so)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: The Ohio State University — 2009 Millikin Road, Columbus, OH, 43210 ⏎ SUBMIT TO: apinvoices@osu.edu (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: STEPS Public Art — 39 Queens Quay E, Toronto, ON, M5E0A4, Canada | GST/HST number not public ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state  | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Resources | STEPS Public Art
- **invoice_card_json**: {"bill_to": {"legal_name": "The Ohio State University", "legal_name_is_published": true, "address": "2009 Millikin Road, Columbus, OH, 43210", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "apinvoices@osu.edu", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "named on the buyer's page: Workday", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state ", "buyer_tax_status_is_published": false, "indicative_rate": "", "currency": "DERIVED: USD (derived from the buyer's country; C", "currency_is_published": false, "vendor_gst_hst": "", "vendor_qst": ""}, "vendor_identity": {"legal_name": "STEPS Public Art", "bn9": "", "neq": "", "remit_address": "39 Queens Quay E, Toronto, ON, M5E0A4, Canada"}, "follow_up": {"ap_phone": "614-292-3956", "ap_contact": "", "requirements_text": "No supplier invoicing address, AP mailbox, or invoice portal was found on the organisation's site. Suppli
- **invoice_readiness**: 6/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number; vendor legal name
- **ap_grade**: C
- **ap_score**: 66
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); bill-to legal name published; invoice or billing address; currency known | missing: finance mailbox; domain publishes a mail server (MX); PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: MX record for the mailbox domain; published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: STEPS Public Art
- **vendor_address**: 39 Queens Quay E, Toronto, ON, M5E0A4, Canada
- **vendor_country_basis**: vendor located in Canada (wd)=stepspublicart.org
- **vendor_website**: https://stepspublicart.org
- **vendor_contact_evidence_url**: https://stepspublicart.org/contact/
- **vendor_logo_url**: https://stepspublicart.org/
- **vendor_website_status**: site answers
- **vendor_linkedin_url**: https://linkedin.com/company/stepspublicart
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); phone / role e-mails / logo: the vendor's own site, https://stepspublicart.org/contact/ (tools/org_contacts.py, org_extras.py); website: https://stepspublicart.org (site answers)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer

## Contract
- **contract_status**: linked from a page of the Canada-located vendor's site (not a client page)
- **contract_title**: Resources | STEPS Public Art
- **contract_description**: Resources | STEPS Public Art (the record's title; the source publishes no separate description)
- **contract_link**: https://stepspublicart.org/project/resources/
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **invoice_currency_derived**: USD (derived from the buyer's country; CAD if the parties agreed so)

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: The Ohio State University — 2009 Millikin Road, Columbus, OH, 43210 ⏎ SUBMIT TO: apinvoices@osu.edu (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: STEPS Public Art — 39 Queens Quay E, Toronto, ON, M5E0A4, Canada | GST/HST number not public ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state  | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Resources | STEPS Public Art
- **invoice_card_json**: {"bill_to": {"legal_name": "The Ohio State University", "legal_name_is_published": true, "address": "2009 Millikin Road, Columbus, OH, 43210", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "apinvoices@osu.edu", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "named on the buyer's page: Workday", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state ", "buyer_tax_status_is_published": false, "indicative_rate": "", "currency": "DERIVED: USD (derived from the buyer's country; C", "currency_is_published": false, "vendor_gst_hst": "", "vendor_qst": ""}, "vendor_identity": {"legal_name": "STEPS Public Art", "bn9": "", "neq": "", "remit_address": "39 Queens Quay E, Toronto, ON, M5E0A4, Canada"}, "follow_up": {"ap_phone": "614-292-3956", "ap_contact": "", "requirements_text": "No supplier invoicing address, AP mailbox, or invoice portal was found on the organisation's site. Suppli
- **invoice_readiness**: 6/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number; vendor legal name
- **ap_grade**: C
- **ap_score**: 66
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); bill-to legal name published; invoice or billing address; currency known | missing: finance mailbox; domain publishes a mail server (MX); PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: MX record for the mailbox domain; published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["apinvoices@osu.edu (invoicing/AP)", "researched by the ChatGPT/Codex agent (lane chatgpt) (page opened and quoted) on 2026-11-08", "page: https://busfin.osu.edu/university-business/controller/tips-and-tricks/supplier-invoice-process-tips-and-tricks", "quote: \"ess will result in the timely payment of suppliers. 1. Supplier submits to Accounts Payable via EDI or email invoice to apinvoices@osu.edu 2. Brainware/Onbase s\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: not checked yet", "DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by not checked", "lane file: chatgpt/chatgpt_verify_buyer_ap_results_batch01.csv task CH-VF-00023"], "buyer_facts": ["address and phone: the buyer's own site, https://clas.osu.edu/contact (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "invoicing requirements: the lane's AP page (https://busfin.osu.edu/university-business/controller/tips-and-tricks/supplier-invoice-process-tips-and-tricks)"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "phone / role e-mails / logo: the vendor's own site, https://stepspublicart.org/contact/ (tools/org_contacts.py, org_extras.py)", "website: https://stepspublicart.org (site answers)"], "rela

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
_none_

## Buyer site facts (org_extras, domain unknown)
_not read_

## Buyer role mailboxes found on its site (org_contacts)
_not read_

## Vendor site facts (org_extras, stepspublicart.org)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://stepspublicart.org/
- **logo_basis**: logo image on the site
- **domain**: stepspublicart.org
- **key**: vendor:STEPS Public Art
- **name**: STEPS Public Art
- **website**: https://stepspublicart.org/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: STEPS Public Art
- **jsonld_logo**: https://stepspublicart.org/wp-content/uploads/2017/07/STEPS_logo_small.png
- **jsonld_url**: https://stepspublicart.org/
- **jsonld_same_as**: https://www.facebook.com/stepspublicart; https://www.instagram.com/stepspublicart; https://www.linkedin.com/company/stepspublicart; https://www.tiktok.com/stepspublicart
- **jsonld_quote**: {"@context":"https:\/\/schema.org","@graph":[{"@type":"WebPage","@id":"https:\/\/stepspublicart.org\/","url":"https:\/\/stepspublicart.org\/","name":"Home | STEPS Public Art","isPartOf":{"@id":"https:\/\/stepspublicart.org\/#website"},"about":{"@id":"https:\/\/stepspublicart.org\/#organization"},"pr
- **jsonld_page**: https://stepspublicart.org/
- **legal_name_stated**: City of Toronto
- **legal_name_stated_url**: https://stepspublicart.org/about/
- **legal_name_stated_quote**: rtBridges Arts AccessAbility Network Manitoba Buy Social Canada CARFAC Centre for Social Innovation City of Toronto Diverse Supplier Network CODAworx Creative City Network of Canada Creative Mornings CultureBrew.Art
- **linkedin_url**: https://linkedin.com/company/stepspublicart

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "39 Queens Quay E, Suite 100, Toronto, ON, M5E 0A4", "address_country": "CA", "address_url": "https://stepspublicart.org/contact/", "address_method": "pattern", "address_quote": "this time Our Location c/o Art Hub 27 39 Queens Quay E, Suite 100 Toronto, ON, M5E 0A4 P: 1-888-783-7780 Visit Art Hub 27 for visitor instructions. Please note our of", "domain": "stepspublicart.org", "key": "vd:stepspublicart.org", "name": "STEPS Public Art", "website": "https://stepspublicart.org/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
_none_

## Lanes' verified findings for this buyer (team_buyers)
```
none
```

## PO-level open data naming this buyer
_none_

## Contract records between the pair (dataset)
_none_

## The buyer's other Canadian-vendor records (first 60 of 0)
_none_

## The vendor's other buyers in the dataset (first 60 of 7)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_bidsandtenders:ac633389-2398-477e-8828-9be5f84b5b0b:1 | Township of Wilmot | Consulting Services for Development of the Township of Wilmot Arts & Culture Master Plan | 37718.0 |  |  | https://wilmot.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/ac633389-2398-477e-8828-9be5f84b5b0b |
| ca_bidsandtenders:4b948b13-ea28-433b-95cd-1685ed86568b:1 | City of Stratford | MUNICIPAL CULTURAL PLAN |  |  |  | https://stratford.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/4b948b13-ea28-433b-95cd-1685ed86568b |
| ca_bidsandtenders:b74de612-ed9f-490e-9cfc-4940a356dc27:13 | City of Mississauga | Culture Districts Implementation - Roster | 1.0 |  |  | https://mississauga.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/b74de612-ed9f-490e-9cfc-4940a356dc27 |
| ca_bidsandtenders:ad7699ab-96f5-4dc7-b327-30ad6f92651d:8 | City of Red Deer | Public Art G.H Dawe Community Centre Expansion | 1.0 |  |  | https://reddeer.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/ad7699ab-96f5-4dc7-b327-30ad6f92651d |
| ca_bidsandtenders:35d134c3-fce7-467d-a4ee-d0f8cfd2dc4f:2 | Dufferin-Peel Catholic District School Board | Mural Service Providers |  |  |  | https://dpcdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/35d134c3-fce7-467d-a4ee-d0f8cfd2dc4f |
| ca_merx:3935612728:2 | Toronto Transit Commission - PCM Capital | P11PJ26245-G85-429-ART CONSULTANT – TRIENNIAL SERVICES | 75000.0 |  |  | https://www.merx.com/ttc/torontotransitcommission/solicitations/P11PJ26245-G85-429-ART-CONSULTANT-TRIENNIAL-SERVICES/0000320814?origin=0 |
| ca_merx:2587370251:1 | Toronto Transit Commission - PCM Capital | P11PJ23430-G85-417-ART CONSULTANT – TRIENNIAL SERVICES | 150000.0 |  |  | https://www.merx.com/ttc/torontotransitcommission/solicitations/P11PJ23430-G85-417-ART-CONSULTANT-TRIENNIAL-SERVICES/0000254527?origin=0 |

## Open questions for hand research (layer 2)

- the vendor's GST/HST number (BN9)
- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
