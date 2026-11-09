# S3-10 — RPC ⇄ Genome Atlantic

Stratum: **S3_routed_public_body_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: RPC (schema.org JSON-LD legalName on https://rpc.ca/) — 921 College Hill Rd Fredericton, NB Canada (schema.org JSON-LD PostalAddress on https://rpc.ca/)
SUBMIT TO: info@rpc.ca (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: GENOME ATLANTIC (as registered: Corporations Canada (open data), corporation number 3784665, 2026-11-08) — 1344 Summer Street, #47, Halifax, NS, B3H 0A8 (registered address; Corporations Canada (open data), corporation number 3784665, 2026-11-08) | GST/HST 862657525 (Corporations Canada (open data), corporation number 3784665, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NB on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Our Projects - Genome Atlantic
```

## Relationship
- **rank_group**: E1
- **data_quality_score**: 36
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: RPC (organisation (type not stated in the record), jurisdiction not stated) — linked from the Canada-located vendor's site (weakest listed relationship): Genome Atlantic | subject: Our Projects - Genome Atlantic | published by: the Canada-located vendor's own website | record: https://genomeatlantic.ca/genome-projects/ | vendor in Canada because: vendor located in Canada (wd)=genomeatlantic.ca | status rule: linked from a page of the Canada-located vendor's site (not a client page)
- **how_relationship_was_found**: tools/provider_mentions.py / news_match.py found the buyer linked from the vendor's own site or release
- **keys**: lead:92fb9165fa5243aa
- **tier**: E
- **grade**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: RPC
- **buyer_website**: https://rpc.ca/
- **buyer_address**: 921 College Hill Rd Fredericton, NB Canada (schema.org JSON-LD PostalAddress on https://rpc.ca/)
- **buyer_phone**: 506.452.1212
- **buyer_contact_evidence_url**: https://rpc.ca/contact
- **buyer_legal_name_as_published**: RPC (schema.org JSON-LD legalName on https://rpc.ca/)
- **buyer_logo_url**: https://images.squarespace-cdn.com/content/v1/65fd8b03213af95c3d229c4a/b481ddb6-c461-48d6-934e-e6803502fa9f/RPC-logo-blue.png?format=1500w
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/research-
- **buyer_type**: organisation (type not stated in the record)
- **buyer_sector**: not stated
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://rpc.ca/contact (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NB on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: info@rpc.ca
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://rpc.ca/
- **email_evidence_quote**: ways satisfied with the level of quality of the lab and reporting.” —Yvon Richard, Chaleur Regional Service RELIABLE. ACCURATE. INNOVATIVE. info@rpc.ca Tel: 506.452.1212 Toll Free: 800.563.0844 RPC Fredericton: 921 College Hill Road, Fredericton, New Brunswick, Canada E3B 6Z9 RPC Moncton:
- **email_evidence_context**: w – we know that we can count on you to deliver what you promise!” —Jason Latouche, Jason Latouche Roofing “Always satisfied with the level of quality of the lab and reporting.” —Yvon Richard, Chaleur Regional Service RELIABLE. ACCURATE. INNOVATIVE. info@rpc.ca Tel: 506.452.1212 Toll Free: 800.563.0844 RPC Fredericton: 921 College Hill Road, Fredericton, New Brunswick, Canada E3B 6Z9 RPC Moncton: 115A Harrisville Boulevard, Moncton, New Brunswick, Canada E1H 3T3 CONTACT US CONNECT WITH US © 2026 RPC. All r (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: info@rpc.ca (general) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://rpc.ca/ | quote: "ways satisfied with the level of quality of the lab and reporting.” —Yvon Richard, Chaleur Regional Service RELIABLE. ACCURATE. INNOVATIVE. info@rpc.ca Tel: 506" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-21247
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none; rua=mailto:ibhrmulp@ag.ca.dmarcian.com, mailto:it@rpc.ca; ruf=mailto:it@rpc.ca; fo=0:1:d:s;
- **dmarc_record_domain**: rpc.ca
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 ip4:162.252.134.76 include:spf.protection.outlook.com include:secureserver.net -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: RPC (schema.org JSON-LD legalName on https://rpc.ca/) — 921 College Hill Rd Fredericton, NB Canada (schema.org JSON-LD PostalAddress on https://rpc.ca/) ⏎ SUBMIT TO: info@rpc.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: GENOME ATLANTIC (as registered: Corporations Canada (open data), corporation number 3784665, 2026-11-08) — 1344 Summer Street, #47, Halifax, NS, B3H 0A8 (registered address; Corporations Canada (open data), corporation number 3784665, 2026-11-08) | GST/HST 862657525 (Corporations Canada (open data), corporation number 3784665, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NB on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Our Projects - Genome Atlantic
- **invoice_card_json**: {"bill_to": {"legal_name": "RPC (schema.org JSON-LD legalName on https://rpc.ca/)", "legal_name_is_published": true, "address": "921 College Hill Rd Fredericton, NB Canada (schema.org JSON-LD PostalAddress on https://rpc.ca/)", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "info@rpc.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NB on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 15% (New Brunswick)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "862657525RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "GENOME ATLANTIC (as registered: Corporations Canada (open data), corporation number 3784665, 2026-11-08)", "bn9": "862657525 (Corporations Canada (open data),
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: Genome Atlantic
- **vendor_legal_name**: GENOME ATLANTIC (as registered: Corporations Canada (open data), corporation number 3784665, 2026-11-08)
- **vendor_registry_id**: corporation number 3784665 (Corporations Canada (open data))
- **vendor_registry_url**: https://ised-isde.canada.ca/cc/lgcy/fdrlCrpDtls.html?corpId=3784665
- **vendor_registered_address**: 1344 Summer Street, #47, Halifax, NS, B3H 0A8 (registered address; Corporations Canada (open data), corporation number 3784665, 2026-11-08)
- **vendor_legal_form**: Canada Not-for-profit Corporations Act (Corporations Canada (open data), corporation number 3784665, 2026-11-08)
- **vendor_country_basis**: vendor located in Canada (wd)=genomeatlantic.ca
- **vendor_bn9**: 862657525 (Corporations Canada (open data), corporation number 3784665, 2026-11-08)
- **vendor_gst_hst_derived**: 862657525RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://genomeatlantic.ca
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); registry identity: corporation number 3784665 (Corporations Canada (open data)) status Active (Corporations Canada (open data), corporation number 3784665, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: registry: Corporations Canada (open data), corporation number 3784665, 2026-11-08; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2014-06-27; website: https://genomeatlantic.ca
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Active (Corporations Canada (open data), corporation number 3784665, 2026-11-08)
- **vendor_incorporation_date**: 2014-06-27
- **vendor_years_in_business**: 12.4 (since 2014-06-27, registry date)
- **vendor_bn_source**: registry: Corporations Canada (open data), corporation number 3784665, 2026-11-08

## Contract
- **contract_status**: linked from a page of the Canada-located vendor's site (not a client page)
- **contract_title**: Our Projects - Genome Atlantic
- **contract_description**: Our Projects - Genome Atlantic (the record's title; the source publishes no separate description)
- **contract_link**: https://genomeatlantic.ca/genome-projects/
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NB on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: HST 15% (New Brunswick) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 862657525RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: RPC (schema.org JSON-LD legalName on https://rpc.ca/) — 921 College Hill Rd Fredericton, NB Canada (schema.org JSON-LD PostalAddress on https://rpc.ca/) ⏎ SUBMIT TO: info@rpc.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: GENOME ATLANTIC (as registered: Corporations Canada (open data), corporation number 3784665, 2026-11-08) — 1344 Summer Street, #47, Halifax, NS, B3H 0A8 (registered address; Corporations Canada (open data), corporation number 3784665, 2026-11-08) | GST/HST 862657525 (Corporations Canada (open data), corporation number 3784665, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NB on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Our Projects - Genome Atlantic
- **invoice_card_json**: {"bill_to": {"legal_name": "RPC (schema.org JSON-LD legalName on https://rpc.ca/)", "legal_name_is_published": true, "address": "921 College Hill Rd Fredericton, NB Canada (schema.org JSON-LD PostalAddress on https://rpc.ca/)", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "info@rpc.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NB on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 15% (New Brunswick)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "862657525RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "GENOME ATLANTIC (as registered: Corporations Canada (open data), corporation number 3784665, 2026-11-08)", "bn9": "862657525 (Corporations Canada (open data),
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["info@rpc.ca (general)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://rpc.ca/", "quote: \"ways satisfied with the level of quality of the lab and reporting.” —Yvon Richard, Chaleur Regional Service RELIABLE. ACCURATE. INNOVATIVE. info@rpc.ca Tel: 506\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-21247"], "buyer_facts": ["address and phone: the buyer's own site, https://rpc.ca/contact (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "registry identity: corporation number 3784665 (Corporations Canada (open data)) status Active (Corporations Canada (open data), corporation number 3784665, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data", "match)", "BN9: registry: Corporations Canada (open data), corporation number 3784665, 2026-11-08", "GST/HST derived BN9

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://rpc.ca/ | 2026-11-08 | ok |  |  |  | 506.452.1212 |  |  |  |  |  |

## Buyer site facts (org_extras, rpc.ca)
- **status**: ok
- **pages**: 3
- **language**: en
- **logo_url**: https://images.squarespace-cdn.com/content/v1/65fd8b03213af95c3d229c4a/b481ddb6-c461-48d6-934e-e6803502fa9f/RPC-logo-blue.png?format=1500w
- **logo_basis**: logo image in the site header
- **domain**: rpc.ca
- **key**: vendor:Research and Productivity Council
- **name**: Research and Productivity Council
- **website**: https://rpc.ca/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_legal_name**: RPC
- **jsonld_address**: 921 College Hill Rd Fredericton, NB Canada
- **jsonld_phone**: 506-452-1212
- **jsonld_email**: info@rpc.ca
- **jsonld_same_as**: https://www.linkedin.com/company/research-&-productivity-council/; https://www.facebook.com/NBRPC; https://www.youtube.com/RPCSciEng; https://www.instagram.com/nb_rpc/
- **jsonld_quote**: {"address":"921 College Hill Rd\nFredericton, NB\nCanada","image":"https://static1.squarespace.com/static/65fd8b03213af95c3d229c4a/t/6736074fca8fb030288b4000/1793992253998/","name":"RPC","openingHours":"Mo 08:30-16:30, Tu 08:30-16:30, We 08:30-16:30, Th 08:30-16:30, Fr 08:30-16:30, ","@context":"htt
- **jsonld_page**: https://rpc.ca/
- **legal_name_stated**: 921 College
- **legal_name_stated_url**: https://rpc.ca/
- **legal_name_stated_quote**: IABLE. ACCURATE. INNOVATIVE. info@rpc.ca Tel: 506.452.1212 Toll Free: 800.563.0844 RPC Fredericton: 921 College Hill Road, Fredericton, New Brunswick, Canada E3B 6Z9 RPC Moncton: 115A Harrisville Boulevard, Monc
- **linkedin_url**: https://www.linkedin.com/company/research-
- **tel_links**: 15064521212; 18005630844; 15068556472; 5064521212

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "address": "921 College Hill Road, Fredericton, New Brunswick, Canada, E3B 6Z9", "address_country": "CA", "address_url": "https://rpc.ca/contact", "address_method": "pattern", "address_quote": "h Back RPC FREDERICTON 921 College Hill Road Fredericton, New Brunswick, Canada E3B 6Z9 Tel: 506.452.1212 / Toll Free: 1.800.563.0844 Fax: 506.452.1395 RPC MONCTON 115", "phone": "506.452.1212", "phone_url": "https://rpc.ca/contact", "emails": "info@rpc.ca", "emails_url": "https://rpc.ca/contact", "domain": "rpc.ca", "key": "vd:rpc.ca", "name": "Research and Productivity Council", "website": "https://rpc.ca/", "kind": "vendor", "date": "2026-11-03"}

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
| v | Genome Atlantic |  |  |  |  |  |  |  |  |  |  |
| v | Research and Productivity Council | Q30283143 | official website on the organisation's domain (http://www.rpc.ca/) + name |  | Research and Productivity Council |  | government agency |  | Canada | 1962-01-01 |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:92fb9165fa5243aa",
 "ap_contact_team": {
  "emails": [
   "rpcfinance@rpc.ca",
   "info@rpc.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "rpcfinance@rpc.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://rpc.ca/contact",
    "quote": "Email Inquiries: General: info@rpc.ca Accounting: rpcfinance@rpc.ca Careers: careers@rpc.ca Bottle Orders: bottleor",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "rpc.ca",
    "task_id": "CL-LD-21247"
   },
   {
    "email": "info@rpc.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://rpc.ca/",
    "quote": "ways satisfied with the level of quality of the lab and reporting.” —Yvon Richard, Chaleur Regional Service RELIABLE. ACCURATE. INNOVATIVE. info@rpc.ca Tel: 506.452.1212 Toll Free: 800.563.0844 RPC Fredericton: 921 College Hill Road, Fredericton, New Brunswick, Canada E3B 6Z9 RPC Moncton:",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "rpc.ca",
    "task_id": "CL-LD-21247"
   }
  ]
 },
 "research_status": {
  "found": 2
 },
 "queries_tried": [
  "site crawl of rpc.ca (15 pages, robots.txt respected), no AI, no search engine",
  "site crawl of rpc.ca (15 pages, robots.txt respected), no AI, no search engine"
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
