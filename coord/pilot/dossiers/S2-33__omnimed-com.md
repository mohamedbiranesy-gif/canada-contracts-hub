# S2-33 — omnimed.com ⇄ Vigilance Santé inc.

Stratum: **S2_complete_no_published_PO_rule** · pay on sight: yes — reference rule not published (quote the buyer's PO / order number when one is issued) · channel tier 1 · AP grade C · missing: (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: OMNI-MED.COM INC. (as registered: Registraire des entreprises du Québec (open data), NEQ 1147798178, 2026-11-08) — 819 875-3929, ADRESSE, 160, rue Pope, Cookshire (Québec) J0B 1M0
SUBMIT TO: facturation@omnimed.com (invoicing/AP mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Vigilance Santé inc. — 440 Notre-Dame, suite 202, Repentigny, QC, J6A 2T4, CAN | GST/HST 116463720RT0001 (account derived from the BN9) | NEQ 1141978040
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: omnimed.com (organisation (type not stated in the record), jurisdiction not stated) — named as a client by the Canada-located vendor (client
```

## Relationship
- **rank_group**: D4
- **data_quality_score**: 72
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: omnimed.com (organisation (type not stated in the record), jurisdiction not stated) — named as a client by the Canada-located vendor (client list / customer story), dated: Vigilance Santé inc. | published by: the Canada-located vendor's own website | record: https://www.vigilance.ca/ | vendor in Canada because: vendor located in Canada (wall)=vigilance.ca | status rule: client listing on the vendor's own site (undated)
- **how_relationship_was_found**: tools/client_lists.py / dated_stories.py read the vendor's dated customer story / case study naming the buyer
- **keys**: lead:43112b95d7b10794
- **tier**: D
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: omnimed.com
- **buyer_website**: https://omnimed.com/
- **buyer_address**: 819 875-3929, ADRESSE, 160, rue Pope, Cookshire (Québec) J0B 1M0
- **buyer_phone**: +1-888-780-6081 (tel: link on https://omnimed.com/)
- **buyer_contact_evidence_url**: https://www.omnimed.com/fr/nous-joindre
- **buyer_legal_name_as_published**: OMNI-MED.COM INC. (as registered: Registraire des entreprises du Québec (open data), NEQ 1147798178, 2026-11-08)
- **buyer_logo_url**: https://www.omnimed.com/hs-fs/hubfs/Site%20Web/logotype-1.png?width=484&height=150&name=logotype-1.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://fr.linkedin.com/company/omnimed.com
- **buyer_registry_id**: NEQ 1147798178 (Registraire des entreprises du Québec (open data); https://www.registreentreprises.gouv.qc.ca/RQAnonymeGR/GR/GR03/GR03A2_19A_PIU_RechEnt_PC/PageRechSimple.aspx)
- **buyer_type**: company (private sector) (from the organisation's name / web domain)
- **buyer_sector**: private sector
- **buyer_legal_form**: CIE (société par actions (compagnie)) (Registraire des entreprises du Québec (open data), NEQ 1147798178, 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.omnimed.com/fr/nous-joindre (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: facturation@omnimed.com
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.omnimed.com/en/nous-joindre
- **email_evidence_quote**: ers): comptabilite@omnimed.com Billing department (clients): facturation@omnimed.com
- **email_evidence_context**: itate to contact us! 160, Pope Cookshire (Quebec) J0B 1M0 Tél. : 1 888 780-6081 Téléc. : 819 875-3929 EMR support: support@omnimed.com General info: info@omnimed.com Accounting team (suppliers): comptabilite@omnimed.com Billing department (clients): facturation@omnimed.com I want a demo of the electronic medical record. Privacy Policy Cookies Policy © Omnimed - All rights reserved (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: facturation@omnimed.com (invoicing/AP) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-01 | page: https://www.omnimed.com/en/nous-joindre | quote: "ers): comptabilite@omnimed.com Billing department (clients): facturation@omnimed.com" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; DNS lookup failed; mail handled by Google Workspace | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00094
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; DNS lookup failed; mail handled by Google Workspace
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1; p=quarantine; rua=mailto:dmarc@omnimed.uriports.com; ruf=mailto:dmarc@omnimed.uriports.com; fo=1
- **dmarc_record_domain**: omnimed.com
- **spf_policy**: DNS lookup failed
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_phone**: 1 888 780-6081 (as printed on https://www.omnimed.com/en/nous-joindre, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "ap_phone": "1 888 780-6081 (as printed on https://www.omnimed.com/en/nous-joindre, re-read 2026-11-08)"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: OMNI-MED.COM INC. (as registered: Registraire des entreprises du Québec (open data), NEQ 1147798178, 2026-11-08) — 819 875-3929, ADRESSE, 160, rue Pope, Cookshire (Québec) J0B 1M0 ⏎ SUBMIT TO: facturation@omnimed.com (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Vigilance Santé inc. — 440 Notre-Dame, suite 202, Repentigny, QC, J6A 2T4, CAN | GST/HST 116463720RT0001 (account derived from the BN9) | NEQ 1141978040 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: omnimed.com (organisation (type not stated in the record), jurisdiction not stated) — named as a client by the Canada-located vendor (client
- **invoice_card_json**: {"bill_to": {"legal_name": "OMNI-MED.COM INC. (as registered: Registraire des entreprises du Québec (open data), NEQ 1147798178, 2026-11-08)", "legal_name_is_published": true, "address": "819 875-3929, ADRESSE, 160, rue Pope, Cookshire (Québec) J0B 1M0", "address_is_the_invoice_address": false, "tax_number": "", "language": "fr (Québec buyer; French first; its invoicing page is in English, English also accepted)"}, "submit_to": {"email": "facturation@omnimed.com", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (QC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "116463720RT0001", "vendor_qst": ""}, "vendor_identity": {"legal_name": "Vigilance Santé inc.", "bn9": "116463720", "neq": "1141978040 (Registraire des entreprises du Québec
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 73
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: finance mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: fr (Québec buyer; French first; its invoicing page is in English, English also accepted)

## Vendor
- **vendor**: Vigilance Santé inc.
- **vendor_legal_name**: Vigilance Santé inc.
- **vendor_trading_name**: CLINIMOND SERVICES PROFESSIONNELS INC.; CONSULTANTS VIGILANCE-SANTÉ (1999) INC.; Consultants Vigilance-Santé (1999); Les Entreprises MedSafer; MedSécure; RX Vigilance®; VIGILANCE SANTÉ; Vigilance Santé (other names in the registry)
- **vendor_registry_id**: Corporations Canada (corporation number): 2327961; NEQ 1141978040 (Registraire des entreprises du Québec (open data))
- **vendor_registry_url**: https://ised-isde.canada.ca/cc/lgcy/fdrlCrpDtls.html?corpId=2327961
- **vendor_registered_address**: 440 RUE NOTRE-DAME, SUTE 202, REPENTIGNY, QC, J6A 2T4, CA
- **vendor_neq**: 1141978040 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_legal_form**: Société par actions ou compagnie — CANADA: Loi canadienne sur les sociétés par actions, L.R.C. (1985), c. C-44
- **vendor_activity_code**: CAE 7721 — DÉVELOPPEMENT ET VENTE DE LOGICIELS
- **vendor_employees_quebec**: De 50 à 99
- **vendor_directors_range**: 1 to 10 directors (Corporations Canada)
- **vendor_last_annual_filing**: REQ annual declaration 2026; Corporations Canada anniversary 1988-05-02
- **vendor_address**: 440 Notre-Dame, suite 202, Repentigny, QC, J6A 2T4, CAN
- **vendor_country_basis**: vendor located in Canada (wall)=vigilance.ca
- **vendor_bn9**: 116463720
- **vendor_gst_hst_derived**: 116463720RT0001
- **vendor_website**: https://www.vigilance.ca/
- **vendor_emails**: info@vigilance.ca
- **vendor_phone**: 450 582-3917
- **vendor_contact_evidence_url**: https://www.vigilance.ca/contactez-nous
- **vendor_logo_url**: https://www.vigilance.ca/build/images/logo-vigilance-hori.svg
- **vendor_website_status**: site answers
- **vendor_linkedin_url**: https://www.linkedin.com/company/vigilance-sant-/
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); registry identity: Corporations Canada (corporation number): 2327961; NEQ 1141978040 (Registraire des entreprises du Québec (open data)) status Corporations Canada (corporation number): Active; Québec REQ (NEQ): Immatriculée (1995-01-17) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: registry match; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 1988-05-02; phone / role e-mails / logo: the vendor's own site, https://www.vigilance.ca/contactez-nous (tools/org_contacts.py, org_extras.py); website: https://www.vigilance.ca/ (site answers); NEQ: 1141978040 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Corporations Canada (corporation number): Active; Québec REQ (NEQ): Immatriculée (1995-01-17)
- **vendor_incorporation_date**: 1988-05-02
- **vendor_years_in_business**: 38.5 (since 1988-05-02, registry date)

## Contract
- **contract_status**: client listing on the vendor's own site (undated)
- **contract_link**: https://www.vigilance.ca/
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (QC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 116463720RT0001

## Pay on sight / grades
- **pay_on_sight**: yes — reference rule not published (quote the buyer's PO / order number when one is issued)
- **pay_on_sight_missing**: (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: OMNI-MED.COM INC. (as registered: Registraire des entreprises du Québec (open data), NEQ 1147798178, 2026-11-08) — 819 875-3929, ADRESSE, 160, rue Pope, Cookshire (Québec) J0B 1M0 ⏎ SUBMIT TO: facturation@omnimed.com (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Vigilance Santé inc. — 440 Notre-Dame, suite 202, Repentigny, QC, J6A 2T4, CAN | GST/HST 116463720RT0001 (account derived from the BN9) | NEQ 1141978040 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: omnimed.com (organisation (type not stated in the record), jurisdiction not stated) — named as a client by the Canada-located vendor (client
- **invoice_card_json**: {"bill_to": {"legal_name": "OMNI-MED.COM INC. (as registered: Registraire des entreprises du Québec (open data), NEQ 1147798178, 2026-11-08)", "legal_name_is_published": true, "address": "819 875-3929, ADRESSE, 160, rue Pope, Cookshire (Québec) J0B 1M0", "address_is_the_invoice_address": false, "tax_number": "", "language": "fr (Québec buyer; French first; its invoicing page is in English, English also accepted)"}, "submit_to": {"email": "facturation@omnimed.com", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (QC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "116463720RT0001", "vendor_qst": ""}, "vendor_identity": {"legal_name": "Vigilance Santé inc.", "bn9": "116463720", "neq": "1141978040 (Registraire des entreprises du Québec
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 73
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: finance mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["facturation@omnimed.com (invoicing/AP)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-01", "page: https://www.omnimed.com/en/nous-joindre", "quote: \"ers): comptabilite@omnimed.com Billing department (clients): facturation@omnimed.com\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; DNS lookup failed; mail handled by Google Workspace", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00094"], "buyer_facts": ["address and phone: the buyer's own site, https://www.omnimed.com/fr/nous-joindre (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "registry identity: Corporations Canada (corporation number): 2327961", "NEQ 1141978040 (Registraire des entreprises du Québec (open data)) status Corporations Canada (corporation number): Active", "Québec REQ (NEQ): Immatriculée (1995-01-17) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data", "ma

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.omnimed.com/en/nous-joindre | 2026-11-08 | ok |  |  |  | 1 888 780-6081 |  |  |  |  |  |

## Buyer site facts (org_extras, omnimed.com)
- **status**: ok
- **pages**: 3
- **language**: fr
- **logo_url**: https://www.omnimed.com/hs-fs/hubfs/Site%20Web/logotype-1.png?width=484&height=150&name=logotype-1.png
- **logo_basis**: logo image in the site header
- **domain**: omnimed.com
- **key**: lead:43112b95d7b10794
- **name**: omnimed.com
- **website**: https://omnimed.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **linkedin_url**: https://fr.linkedin.com/company/omnimed.com
- **tel_links**: +1-888-780-6081

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "address": "819 875-3929, ADRESSE, 160, rue Pope, Cookshire (Québec) J0B 1M0", "address_country": "CA", "address_url": "https://www.omnimed.com/fr/nous-joindre", "address_method": "pattern", "address_quote": "888 780-6081 TÉLÉCOPIEUR 819 875-3929 ADRESSE 160, rue Pope, Cookshire (Québec) J0B 1M0 Service à la clientèle du DME support@omnimed.com Pour tout ce qui concerne l'u", "emails": "comptabilite@omnimed.com; facturation@omnimed.com; info@omnimed.com; support@omnimed.com", "emails_url": "https://www.omnimed.com/fr/nous-joindre", "domain": "omnimed.com", "key": "lead:43112b95d7b10794", "name": "omnimed.com", "website": "https://omnimed.com/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, vigilance.ca)
- **status**: ok
- **pages**: 3
- **language**: fr
- **logo_url**: https://www.vigilance.ca/build/images/logo-vigilance-hori.svg
- **logo_basis**: logo image in the site header
- **domain**: vigilance.ca
- **key**: vendor:Vigilance Santé inc.
- **name**: Vigilance Santé inc.
- **website**: https://vigilance.ca/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Vigilance Santé
- **jsonld_url**: https://www.vigilance.ca/contactez-nous
- **jsonld_quote**: { "@context" : "http://schema.org", "@type" : "Organization", "name" : "Vigilance Santé", "lastReviewed" : "2026", "relatedLink" : "https://www.vigilance.ca/contactez-nous", "reviewedBy" : "Vigilance Santé", "image" : "https://www.vigilance.ca/build/images/logo-vigilance-hori.svg", "url" : "https://
- **jsonld_page**: https://www.vigilance.ca/contactez-nous
- **legal_name_stated**: Université de Montréal
- **legal_name_stated_url**: https://www.vigilance.ca/a-propos-de-vigilance-sante
- **legal_name_stated_quote**: en gestion de projet de HEC Montréal, baccalauréat en ergothérapie et mineure en informatique de l’Université de Montréal. En plus d’avoir à cœur de réaliser la mission de Vigilance Santé, elle travaille actuellement à en
- **linkedin_url**: https://www.linkedin.com/company/vigilance-sant-/
- **tel_links**: 450-582-3917

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "440, rue Notre-Dame, suite 202, Repentigny (Québec) J6A 2T4", "address_country": "CA", "address_url": "https://www.vigilance.ca/contactez-nous", "address_method": "pattern", "address_quote": "its. Adresse Vigilance Santé 440, rue Notre-Dame, suite 202 Repentigny (Québec) J6A 2T4, Canada 450 582-3917 450 582-3917 1 844 582-3917 1 844 582-3917 info@vigilance.", "phone": "450 582-3917", "phone_url": "https://www.vigilance.ca/contactez-nous", "emails": "info@vigilance.ca", "emails_url": "https://www.vigilance.ca/contactez-nous", "domain": "vigilance.ca", "key": "vd:vigilance.ca", "name": "Vigilance Santé inc.", "website": "https://vigilance.ca/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | api_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | omnimed.com | found | OMNI-MED.COM INC. |  | NEQ 1147798178 | Registraire des entreprises du Québec (open data) | CIE (société par actions (compagnie)) | immatriculée | 1998-06-18 | Cookshire-Eaton | QC | 4-160 rue Pope, Cookshire-Eaton (Québec), J0B1M0 | https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises | 2026-11-08 |

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Les consultants vigilance santé |  |  |  |  |  |  |  |  |  |  |
| v | Vigilance Santé inc. |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:43112b95d7b10794",
 "ap_contact_team": {
  "emails": [
   "facturation@omnimed.com",
   "comptabilite@omnimed.com",
   "%20comptabilite@omnimed.com",
   "info@omnimed.com"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "facturation@omnimed.com",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.omnimed.com/en/nous-joindre",
    "quote": "ers): comptabilite@omnimed.com Billing department (clients): facturation@omnimed.com",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "omnimed.com",
    "task_id": "CL-LD-06158"
   },
   {
    "email": "facturation@omnimed.com",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.omnimed.com/en/nous-joindre",
    "quote": "ers): comptabilite@omnimed.com Billing department (clients): facturation@omnimed.com",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Omnimed",
    "task_id": "CL-WS-00094"
   },
   {
    "email": "comptabilite@omnimed.com",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.omnimed.com/en/nous-joindre",
    "quote": "General info: info@omnimed.com Accounting team (suppliers): comptabilite@omnimed.com Billing",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Omnimed",
    "task_id": "CL-WS-00094"
   },
   {
    "email": "%20comptabilite@omnimed.com",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.omnimed.com/en/facturation-connexion",
    "quote": "r: #000000;\"><span style=\"font-size: 14px;\">Contact our accounting department:<br><span style=\"text-decoration: underline;\"><a href=\"mailto:%20comptabilite@omnimed.com\" target=\"_self\" data-content=\"%20comptabilite@omnimed.com\" data-type=\"mail\">",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "omnimed.com",
    "task_id": "CL-LD-06158"
   },
   {
    "email": "comptabilite@omnimed.com",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.omnimed.com/en/facturation-connexion",
    "quote": "e refunds makes you ineligible for billing based on the number of days of use mentioned above. Question? Contact our accounting department: comptabilite@omnimed.com | 1 888 780-6081 option 2 Terms of Use Privacy Policy Cookies Policy © Omnimed - All rights reserved",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "omnimed.com",
    "task_id": "CL-LD-06158"
   },
   {
    "email": "info@omnimed.com",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.omnimed.com/en/nous-joindre",
    "quote": "General info: info@omnimed.com Accounting team (suppliers): comptabilite@omnimed.com Billing department (clients): facturation@omnimed.com I want a demo of the elec",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Omnimed",
    "task_id": "CL-WS-00094"
   }
  ]
 },
 "research_status": {
  "found": 6
 },
 "queries_tried": [
  "site crawl of omnimed.com (10 pages, robots.txt respected), no AI, no search engine",
  "site crawl of omnimed.com (10 pages, robots.txt respected), no AI, no search engine",
  "site crawl of omnimed.com (10 pages, robots.txt respected), no AI, no search engine",
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

## The vendor's other buyers in the dataset (first 60 of 81)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| canada_federal:isc-sac:5A09024281 | Indigenous Services Canada | Client Software | 280692.0 |  |  | https://search.open.canada.ca/contracts/record/isc-sac,C-2025-2026-Q3-00138 |
| seao_quebec:1071894:vigilance-sante | Centre intégré de santé et de services sociaux (CISSS) des Laurentides | Logiciel RxVigilance | 28444.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=3404eb8a-9d19-4a94-8fcf-6d96c8192f61 |
| seao_quebec:1160625:vigilance-sante | Centre intégré de santé et de services sociaux (CISSS) des Laurentides | LICENCE RX VIGILANCE - VIGILANCE SANTE | 33072.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=34c692d5-03ec-45f2-8e8c-4b9aca2dc099 |
| seao_quebec:1231149:vigilance-sante | Centre intégré de santé et de services sociaux de la Montérégie-Est | Contrat de service - Abonnement logiciel RX Vigilance - Pharmacie | 25480.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=e1a62628-7a05-4d6d-8f88-d3941b585e89 |
| seao_quebec:1238302:vigilance-sante-inc | Centre intégré universitaire de santé et de services sociaux de l’Est-de-l’Île-de-Montréal (CIUSSS) | Licences - Logiciel RxVigilance (Pharmacie) | 32084.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=30b19bca-bbdc-48ba-9373-3b7c19180e20 |
| seao_quebec:1254135:vigilance-sante-inc | Centre Hospitalier de l'Université de Montréal. CHUM | LICENCE D'UTILISATION DU LOGICIEL RX VIGILANCE | 71100.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=f57c8b28-bce7-4194-b0a3-eea6a7ebf2ed |
| seao_quebec:1358766:vigilance-sante | Centre intégré universitaire de santé et de services sociaux de la Capitale-Nationale 1 | Renouvellement RX Vigilance | 44668.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=73ffaf8c-1839-4266-9300-819d4d3109e5 |
| seao_quebec:1359475:vigilance-sante | CIUSSS du Centre-Sud-de-l'Île-de-Montréal | Renouvellement de l'abonnement au licence RxVigilence | 36764.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=830cb857-4518-4452-88e2-f68a91908f68 |
| seao_quebec:1360113:vigilance-sante | Centre Intégré de Santé et de Services Sociaux de l'Outaouais | ABONNEMENT A RX VIGILENCE | 33020.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=96bfb81c-1cce-4956-bb17-329bdef2d3db |
| seao_quebec:1363538:vigilance-sante | CHU de Québec-Université Laval | Contrat de services licences locale et flottante CHU | 40976.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=807515a2-06c6-467d-854a-584f4be5d77f |
| seao_quebec:1364192:vigilance-sante | Centre intégré universitaire de santé et de services sociaux de l’Est-de-l’Île-de-Montréal (CIUSSS) | Licences - Logiciel RxVigilance (Pharmacie) | 33956.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=edf1e46b-11c4-42f2-8444-a08cfe540399 |
| seao_quebec:1368380:vigilance-sante-inc | CIUSSS du Nord-de-l'Île-de-Montréal | Service maintenance support de logiciel | 32384.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=72a94162-bc42-4093-8bb5-bf495ff84087 |
| seao_quebec:1378189:vigilance-sante | CIUSSS du Nord-de-l'Île-de-Montréal | Contrat de licence RxVigilance web et flottante | 32084.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=3217b2a7-9848-4aa7-8e23-68b93ccea819 |
| seao_quebec:1386602:vigilance-sante-inc | Centre Hospitalier de l'Université de Montréal. CHUM | LICENCE D'UTILISATION DU LOGICIEL RX VIGILANCE | 72067.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=e4afaa12-4f68-48f9-9057-ece856fd66eb |
| seao_quebec:1393598:vigilance-sante | CIUSSS du Centre-ouest-de-l'Île-de-Montréal | RxVigilance renouvellement licences 12 mois (PHARMACY) | 43429.75 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=adc11ede-66a1-4336-88e3-08bbf72ad116 |
| seao_quebec:1394249:vigilance-sante | CIUSSS du Centre-ouest-de-l'Île-de-Montréal | RxVigilance renouvellement licences 12 mois (QUALITY) | 35793.75 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=e3e8c795-7295-483d-987d-ee9e745fbaff |
| seao_quebec:1403469:vigilance-sante | CHU Ste-Justine | SERV SUPPORT LICENCE ILLIMITEE  RXVIGILANCE WEB | 74970.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=8252fc1a-e26e-439d-97ef-bcf9e2c5884f |
| seao_quebec:1460166:vigilance-sante | Centre intégré de santé et de services sociaux de la Montérégie-Est | CONTRAT SERVICE - ABONNEMENT LOGICIEL RX VIGILANCE - PHARMACIE | 62400.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=b75fb4e9-c354-461e-a4a7-b4851c9c86a3 |
| seao_quebec:1463953:vigilance-sante | Centre Intégré de Santé et de Services Sociaux de l'Outaouais | ABONNEMENT À RX VIGILANCE | 33800.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=562b085b-e46e-4593-bc11-977c509ea353 |
| seao_quebec:1467552:vigilance-sante | CIUSSS du Centre-Sud-de-l'Île-de-Montréal | SUPPORT ET MISE  A  JOUR DES LICENCES RXVIGILANCES (Renouvellement 2021-2022) | 37960.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=fd4c77cf-b48a-4b97-8db3-e944a32cf85a |
| seao_quebec:1476047:vigilance-sante | Centre intégré universitaire de santé et de services sociaux de l’Est-de-l’Île-de-Montréal (CIUSSS) | Licences - Logiciel RxVigilance (Pharmacie) | 34892.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=76ad58ab-96d8-4ea2-aa66-9f2a57fe95e4 |
| seao_quebec:1487025:vigilance-sante | CIUSSS du Nord-de-l'Île-de-Montréal | Support logiciel RX Vigilance | 33060.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=d510a160-85fa-456a-8690-be7051ac1d97 |
| seao_quebec:1508681:vigilance-sante | Centre universitaire de santé McGill. | Renouvellement licences Rx Vigilance | 85097.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=831e5c5b-513f-46f0-bb80-a54a4a45349f |
| seao_quebec:1588131:vigilance-sante-inc | Centre intégré universitaire de santé et de services sociaux de l’Est-de-l’Île-de-Montréal (CIUSSS) | Licences - Logiciels RxVigilance et RxPhotos (Pharmacie) | 46106.55 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=855eb637-e790-46c4-a153-a8d4cd7eb0c1 |
| seao_quebec:1599798:vigilance-sante-inc | CIUSSS du Nord-de-l'Île-de-Montréal | Maintenance et support RxVigilance | 40216.05 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=33a0bdd5-ebcf-41b8-afeb-b4b13e1abda1 |
| seao_quebec:1607704:vigilance-sante-inc | Centre intégré de santé et de services sociaux de Lanaudière | Serv_abon_licences_RxVigilance | 44018.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=cf9717b9-8123-4481-8a24-168987d5f3bf |
| seao_quebec:1624973:vigilance-sante-inc | CISSS Montérégie-Ouest | Abonnement LICENCE RXVIGILENCE  en accès illimité CISSS Montérégie-Ouest 2022-2023 | 35212.14 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=2bf7a7c7-56f6-41f8-a029-f126e47ae519 |
| seao_quebec:1624981:vigilance-sante-inc | Centre universitaire de santé McGill. | Renouvellement licences RX Vigilance | 86859.9 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=f1619677-3d01-4d64-9a9f-6beec6831849 |
| seao_quebec:1701594:vigilance-sante-inc | Centre intégré universitaire de santé et de services sociaux de la Capitale-Nationale 1 | Renouvellement licences RxVigilance | 175488.12 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=669d5aa7-708b-48e5-9470-6371adb8180b |
| seao_quebec:1703780:vigilance-sante | CIUSSS du Centre-Sud-de-l'Île-de-Montréal | SUPPORT ET MISE  A  JOUR DES LICENCES RXVIGILANCES | 42757.56 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=8b744351-88c5-40c4-8f28-73f62931153e |
| seao_quebec:1703937:vigilance-sante-inc | Centre intégré universitaire de santé et de services sociaux de l’Est-de-l’Île-de-Montréal (CIUSSS) | Licences - Logiciels RxVigilance et RxPhotos (Pharmacie) | 54368.06 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=693f01ad-00d5-4590-a135-09dc2615c8ab |
| seao_quebec:1708530:vigilance-sante-inc | Centre Hospitalier de l'Université de Montréal. CHUM | LICENCE D'UTILISATION DU LOGICIEL RX VIGILANCE | 77162.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=4db31920-5aaf-47c4-9ee5-8e6509e32d89 |
| seao_quebec:1711739:vigilance-sante-inc | Centre intégré de santé et de services sociaux de l'Abitibi-Témiscamingue | RENOUVELLEMENT D'UN ABONNEMENT AUX LICENCES DE VIGILANCE SANTÉ | 29801.52 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=bd946de1-50a7-499b-b8ce-e94e9cde0a1f |
| seao_quebec:1714242:vigilance-sante-inc | Université de Montréal. | ABONNEMENT À UNE SOLUTION WEB DE BASE DE DONNÉES ET D’ANALYSE DE MÉDICAMENTS | 126009.55 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=93f641da-9bb2-4f99-8cf4-5c1f98803497 |
| seao_quebec:1722719:vigilance-sante-inc | CIUSSS du Saguenay - Lac-Saint-Jean | Abonnement Rx Vigilance | 64209.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=a3b96a68-1cd1-4544-98c8-bc93059c2181 |
| seao_quebec:1749222:vigilance-sante-inc | CISSS Montérégie-Ouest | ABONNEMENT LICENCE RXVIGILANCE EN ACCÈS ILLIMITE 2023-2024 CISSSMO | 39270.39 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=3759aa8c-3971-4716-942a-bc30c469c650 |
| seao_quebec:1774093:vigilance-sante-inc | Fonds des ressources informationnelles du secteur de la Santé et des Services sociaux (FRISSSS) | Développement personnalisé du moteur d'analyse des interactions médicamenteusese pour les établissements qui devront utiliser Syphac après le 31 décembre 2023. | 100000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=3f107d42-c3b9-45d8-9316-6724af48caa9 |
| seao_quebec:1785671:vigilance-sante-inc | Centre intégré universitaire de santé et de services sociaux de l'Ouest-de-l'Île-de-Montréal | Contrat Accès illimité aux bases de données RxVigilence et RxPhotos | 29565.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=c23a7c65-f041-4abf-8dda-31186b0ee9a8 |
| seao_quebec:1797898:vigilance-sante-inc | Université de Sherbrooke -Service des ressources financières-  Section de l'approvisionnement | Abonnement RXV vigilance | 8633.04 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=0b435645-fa2e-4185-8954-c93b60a8765c |
| seao_quebec:1811639:vigilance-sante-inc | CIUSSS du Centre-Sud-de-l'Île-de-Montréal | SUPPORT ET MISE  A  JOUR DES LICENCES RXVIGILANCES | 44467.95 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=92304b9e-9cd4-43cc-8adf-b8e8570d0e82 |
| seao_quebec:1826185:vigilance-sante-inc | Centre intégré universitaire de santé et de services sociaux de l’Est-de-l’Île-de-Montréal (CIUSSS-EMTL) | Licences - Logiciels RxVigilance et RxPhotos (Pharmacie) | 70257.6 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=3d9b8073-cea0-440a-a068-0c9b64eedeee |
| seao_quebec:1841608:vigilance-sante-inc | Centre intégré de santé et de services sociaux de la Gaspésie. | Licences d'accès illimité à RxVigilance et RxPhotos | 55842.02 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=5310d01a-74e9-4ce7-9fb6-6d05fb7c21ec |
| seao_quebec:1848201:vigilance-sante | Centre intégré de santé et de services sociaux de l'Abitibi-Témiscamingue | RENOUVELLEMENT D'UN ABONNEMENT AUX LICENCES DE VIGILANCE SANTÉ | 34440.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=a0479f47-4dbb-4812-8895-02e61dd17feb |
| seao_quebec:20014503:vigilance-sante-inc | Collecto Services regroupés en éducation | Abonnement à des ressources électroniques | 280779.5 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=fda03134-4d48-4376-80a9-6dc11386435b |
| seao_quebec:20036818:vigilance-sante-inc | Centre intégré universitaire de santé et de services sociaux de l'Ouest-de-l'Île-de-Montréal | ACCÈS ILLIMITÉ AUX BASES DE DONNÉES RxVIGILANCE ET RxPHOTOS | 30750.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=15ff5995-8ff0-427f-a6ea-5d736ae20b24 |
| seao_quebec:20046198:vigilance-sante-inc | Santé Québec Outaouais | RENOUVELLEMENT ABONNEMENT A  RX VIGILANCE (2025-2026) | 65843.12 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=9dae2513-19bf-41da-bb43-117404e4f8b5 |
| seao_quebec:20047795:vigilance-sante | Santé Québec - CHU de Québec - Université Laval  | ABONNEMENT AUX MISES À JOUR DES BASES DE DONNÉES | 107472.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=0443ea16-7918-47dd-ab6e-d8045c58079e |
| seao_quebec:20051961:vigilance-sante | Santé Québec - Centre-Sud-de-l’Île-de-Montréal Universitaire | SUPPORT ET MISE  A  JOUR DES LICENCES RXVIGILANCES | 45798.01 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=1e632ff2-c6a3-449f-900f-0c59ade99c1a |
| seao_quebec:20054024:vigilance-sante-inc | Santé Québec | L’acquisition de 60 licences concurrentes du système RxVigilance et de la liste de produits pharmaceutiques incluant la mise à jour mensuelle | 133717.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=e0319a28-00c6-4ca4-b950-50ec07201b0f |
| seao_quebec:20057351:vigilance-sante-inc | Centre intégré de santé et de services sociaux de la Montérégie-Est | ABONNEMENT LOGICIEL RX VIGILANCE - PHARMACIE | 31368.5 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=1d27538a-b605-4bf3-ab97-bc07903206d4 |
| seao_quebec:20058018:vigilance-sante-inc | Santé Québec Est-de-l’Île-de-Montréal – Universitaire | Licences - Logiciels Rx Vigllance et RxPhotos (Pharmacie) | 74417.71 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=6a7d04ea-d22f-4ebb-b55e-1b1531cd7c0c |
| seao_quebec:20063624:vigilance-sante-inc | CENTRE INTÉGRÉ DE SANTÉ ET DE SERVICES SOCIAUX DU BAS-SAINT-LAURENT | Renouvellement Vigilance Santé 2025-2028 | 165672.37 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=9bee463e-e21d-4de9-9b86-ebecda37c9cb |
| seao_quebec:20085588:vigilance-sante | Santé Québec - Centre universitaire de santé McGill | Contrat RX Vigilance | 38513.76 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=d50d86f3-2e95-4f67-a47e-c9e1af95a1ea |
| seao_quebec:20085883:vigilance-sante | CIUSSS du Centre-ouest-de-l'Île-de-Montréal | DROIT D'UTILISATION LOGICIEL RX VIGILANCE | 104143.42 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=f05bd637-4496-4d42-aca5-4e0983375df1 |
| seao_quebec:20106132:vigilance-sante-inc | Centre intégré universitaire de santé et de services sociaux de l'Ouest-de-l'Île-de-Montréal | ACCES ILLIMITE AUX BASES DE DONNEES RxVIGILANCE RxPHOTOS 2025 - 2026 | 31672.5 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=93c1a62c-d174-42a3-973e-a96d1df074ea |
| seao_quebec:20106580:vigilance-sante | Santé Québec Estrie - Centre hospitalier universitaire de Sherbrooke | RX VIGILANCE ET RX PHOTOS EN ACCES ILLIMITÉ  | 292026.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=c9abed8e-e48b-41d9-a93f-3819695a5efe |
| seao_quebec:20108109:vigilance-sante-inc | Santé Québec Nord-de-l'Île-de-Montréal – Universitaire | Support Logiciel RxVIGILANCE - INTEGRATION DSN | 125967.87 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=5c75368f-5aae-40ac-b9d9-21cb186e2e5a |
| seao_quebec:20123965:vigilance-sante | Santé Québec-Institut de Cardiologie de Montréal | CONTRAT D'ABONNEMENT  ACCÈS  ILLIMITÉ À RxVIGILANCE ET RxPHOTOS | 48681.17 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=04302a95-c99d-40bb-9969-fde66c4e1edc |
| seao_quebec:20124082:vigilance-sante-inc | Santé Québec Chaudière-Appalaches | Renouvellement des droits d'utilisation du logiciel RxVigilance | 44767.8 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=8d159fd4-a1cb-493b-9f27-f6733ad8878d |
| seao_quebec:20124562:vigilance-sante-inc | Santé Québec – Centre hospitalier de l’Université de Montréal | Licence d'utilisation logiciel RX Vigilance | 74412.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=70ea18ec-4831-492a-951e-c9288b73f461 |
| … 21 more rows in the .json | ||||||

## Open questions for hand research (layer 2)

- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_
