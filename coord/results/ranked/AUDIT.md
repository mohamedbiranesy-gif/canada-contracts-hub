# Deep audit — 52620 delivered rows in 17 packages (21 files), 2026-11-04

Result: **PASS** — 11 hard checks, 16 soft checks; hard failures: 0. Every flagged row is listed in `audit_flags.csv` with its reasons.

| # | check | kind | rows flagged | verdict |
|---|---|---|---|---|
| 1 | header: 92 identical columns in every file | hard | 0 | PASS |
| 2 | mailbox syntax | hard | 0 | PASS |
| 3 | mailbox referee-confirmed (all but P11) | hard | 0 | PASS |
| 4 | mail server (MX or A) on the mailbox domain | hard | 0 | PASS |
| 4b | mail server not yet checked (row newer than the last DNS pass) | soft | 419 | REVIEW |
| 5 | no webmail domain | hard | 0 | PASS |
| 6 | no person-like local part | hard | 0 | PASS |
| 7 | role word in the local part | soft | 2719 | REVIEW |
| 8 | receivables-looking local part graded invoicing/AP | soft | 32 | REVIEW |
| 9 | shared government domain: page or quote names the body | soft | 2 | REVIEW |
| 10 | regional token of a multinational on a differently-located body | soft | 0 | PASS |
| 11 | quote contains the address | hard | 0 | PASS |
| 12 | evidence page on the organisation's domain (or its site) | soft | 3167 | REVIEW |
| 13 | email_type label matches grade | hard | 0 | PASS |
| 14 | DMARC / SPF / provider columns filled | soft | 417 | REVIEW |
| 15 | tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m) | soft | 0 | PASS |
| 16 | vendor named and Canada proof present | hard | 0 | PASS |
| 17 | Canada proof is a source field or the vendor's site (never a name) | soft | 0 | PASS |
| 18 | record link present for dated-record tiers | soft | 0 | PASS |
| 19 | buyer name is a name (not a domain or a page title) | soft | 20113 | REVIEW |
| 20 | legal name is not a fragment or a platform copyright | soft | 0 | PASS |
| 21 | one row per mailbox | hard | 0 | PASS |
| 22 | one row per organisation name (same name twice) | soft | 3 | REVIEW |
| 23 | one row per site domain (two rows, different mailboxes, same domain) | soft | 66 | REVIEW |
| 24 | no blank cell | hard | 0 | PASS |
| 25 | jurisdiction vs mailbox top-level domain | soft | 36 | REVIEW |
| 26 | currency filled when a value is filled | soft | 46 | REVIEW |

## How to read the REVIEW lines (none of them is a rule break; each is a known limit, stated so nothing is hidden)
- **4b (419)** — rows that entered after the 14:10 DNS pass; their domains are checked on the next pass and `email_deliverability` / DMARC columns fill then.
- **7 (2,719)** — the audit's role-word vocabulary is narrower than the referee's: `ap_cameco@`, `invsubp@`, `acquisitions@`, `beschaffung@` are role boxes it does not recognise by word; every one was referee-verified on the organisation's own page.
- **8 (32)** — `payments@`-style boxes graded invoicing/AP only where the page itself says invoices or suppliers go there; listed so they can be eyeballed.
- **9 (2)** — government-wide domains where the page names the body only loosely; the 20 clear misattributions found today were removed.
- **12 (3,167)** — the evidence page is on a different domain than the mailbox / website (a second domain of the same organisation, a PDF host, a shared government site); the same-organisation check passed on the name, not the domain.
- **19 (20,113)** — P13 organisations known only by their site's domain (the crawler had no better name and the site prints no legal name); the mailbox, DNS and inferred relationship are unaffected.
- **22 / 23 (3 / 66)** — same short name used by different entities, or two bodies on one site domain (a municipality and its economic-development corporation, several ministries on texas.gov); treated as distinct on purpose.
- **25 (36)** — Canadian-jurisdiction rows whose mailbox is on a foreign TLD (a multinational's or a church network's shared mailbox); kept, flagged.
- **26 (46)** — a value published without a currency by the source; left as published.

## Examples of flagged rows (first 12 per check)
- **4b mail server not yet checked (row newer than the last DNS pass)**
    - P13_inferred_relationship_no_record_own_email_part1_of_5:134 rdubz.ca | rdubz.ca
    - P13_inferred_relationship_no_record_own_email_part1_of_5:366 relianceproperties.ca | relianceproperties.ca
    - P13_inferred_relationship_no_record_own_email_part1_of_5:367 rentlgh.ca | rentlgh.ca
    - P13_inferred_relationship_no_record_own_email_part1_of_5:1049 randonneursontario.ca | randonneursontario.ca
    - P13_inferred_relationship_no_record_own_email_part1_of_5:1050 raysolar.ca | raysolar.ca
    - P13_inferred_relationship_no_record_own_email_part1_of_5:1051 reliance.ca | reliance.ca
    - P13_inferred_relationship_no_record_own_email_part1_of_5:1052 restigouche-hockey.ca | restigouche-hockey.ca
    - P13_inferred_relationship_no_record_own_email_part1_of_5:1053 reyrey.ca | reyrey.com
    - P13_inferred_relationship_no_record_own_email_part1_of_5:5509 ramassagevip.ca | ramassagevip.ca
    - P13_inferred_relationship_no_record_own_email_part1_of_5:5510 ranchwinslow.ca | ranchwinslow.com
    - P13_inferred_relationship_no_record_own_email_part1_of_5:5511 ras-nsa.ca | ras-nsa.ca
    - P13_inferred_relationship_no_record_own_email_part1_of_5:5512 rcentres.qc.ca | rcentres.qc.ca
- **7 role word in the local part**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:16 Cameco Corporation | ap_cameco@cameco.com
    - P01_GOLD_active_relationship_invoicing_AP_email:248 Town of Oakville | ap_inquiries@oakville.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:267 Miami-Dade County (business unit CU05010 | invsubp@miamidade.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:362 BELL TEXTRON INC | APBell@textron.com
    - P02_active_relationship_finance_accounting_email:73 Municipalité de Sainte-Sophie | evaluation@stesophie.ca
    - P02_active_relationship_finance_accounting_email:137 Centre de services scolaire des Phares | sec.ress.fin@cssphares.gouv.qc.ca
    - P03_active_relationship_purchasing_email:5 MacEwan University | pacs@macewan.ca
    - P03_active_relationship_purchasing_email:23 Technische Universität Dresden, Dezernat | beschaffung@tu-dresden.de
    - P03_active_relationship_purchasing_email:25 Centre intégré de santé et de services s | gestion-contractuelle.cissslau@ssss.gouv.qc.ca
    - P03_active_relationship_purchasing_email:36 Ville de Rouyn-Noranda | acquisitions@rouyn-noranda.ca
    - P03_active_relationship_purchasing_email:56 Calgary Housing Company | chcsupplymanagement@calgary.ca
    - P03_active_relationship_purchasing_email:59 École nationale d'administration publiqu | acquisitions@enap.ca
- **8 receivables-looking local part graded invoicing/AP**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:10 Empress | payments@villageofempress.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:4 Texas Tech University | payment.strategies@ttu.edu
    - P01_GOLD_active_relationship_invoicing_AP_email:451 Township of Georgian Bay | payments@gbtownship.ca
    - P05_likely_active_awarded_12_36_months_any_email:26 Martensville | payments@martensville.ca
    - P06_client_listing_invoicing_AP_email:27 University of Bath | payments@bath.ac.uk
    - P06_client_listing_invoicing_AP_email:69 teamviewer.com | payments@teamviewer.com
    - P06_client_listing_invoicing_AP_email:143 blomidonnurseries.com | payments@blomidonnurseries.com
    - P10_linked_from_vendor_site_any_email:12 gov.scot | online_payments@gov.scot
    - P10_linked_from_vendor_site_any_email:29 WeirFoulds LLP | payments@weirfoulds.com
    - P10_linked_from_vendor_site_any_email:36 bcica.org | payments@bcica.org
    - P11_any_relationship_email_not_yet_confirmed:3 Environment and Climate Change Canada | renseignement-paiements-payments-inquiry@ec.gc.ca
    - P13_inferred_relationship_no_record_own_email_part1_of_5:10 THE ROYAL CANADIAN COLLEGE OF ORGANISTS- | payment@rcco-ottawa.ca
- **9 shared government domain: page or quote names the body**
    - P11_any_relationship_email_not_yet_confirmed:5 Canadian Space Agency | invoicing.csa-asc.facturation@canada.ca ← https://www.canada.ca/en/public-services-procurement/services/payments-to-from-g
    - P13_inferred_relationship_no_record_own_email_part1_of_5:489 Landlord and Tenant Board | ltbpayments@ontario.ca ← https://tribunalsontario.ca/ltb/contact/
- **12 evidence page on the organisation's domain (or its site)**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:18 Motorola Solutions, Inc | recepcionfacturas@motorolasolutions.com on web.archive.org (site motorolasolutions.com)
    - P01_GOLD_active_relationship_invoicing_AP_email:2 Department of Defence | peppol.einvoices@defence.gov.au on directory.peppol.eu (site defence.gov.au)
    - P01_GOLD_active_relationship_invoicing_AP_email:3 Department of Industry, Science and Reso | einvoicingqueries@industry.gov.au on directory.peppol.eu (site industry.gov.au)
    - P01_GOLD_active_relationship_invoicing_AP_email:42 Natural Sciences and Engineering Researc | payables@nserc-crsng.gc.ca on nserc-crsng.canada.ca (site nserc-crsng.gc.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:54 Ville de Montréal | facture@montreal.ca on ville.montreal.qc.ca (site montreal.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:84 Ville de Farnham | comptespayables@ville.farnham.qc.ca on web.archive.org (site ville.farnham.qc.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:102 UK Atomic Energy Authority | finance@uk-atomic-energy.org.uk on assets.publishing.service.gov.uk (site gov.uk)
    - P01_GOLD_active_relationship_invoicing_AP_email:115 City of Chestermere | city.ap@chestermere.ca on thecityofchestermere.ca (site chestermere.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:121 Newfoundland and Labrador Liquor Corpora | Accounts.Payable@nlliquor.com on nlliquorcorp.com (site nlliquor.com)
    - P01_GOLD_active_relationship_invoicing_AP_email:123 The Ottawa Hospital | tohaccountspayable@toh.ca on ottawahospital.on.ca (site toh.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:145 UK Research and Innovation | finance@uksbs.co.uk on ukri.org (site uksbs.co.uk)
    - P01_GOLD_active_relationship_invoicing_AP_email:151 Department of Foreign Affairs and Trade | dfat.e-invoicing.prod@dfat.gov.au on directory.peppol.eu (site dfat.gov.au)
- **14 DMARC / SPF / provider columns filled**
    - P13_inferred_relationship_no_record_own_email_part1_of_5:134 rdubz.ca | not checked yet | not checked yet | not checked
    - P13_inferred_relationship_no_record_own_email_part1_of_5:366 relianceproperties.ca | not checked yet | not checked yet | not checked
    - P13_inferred_relationship_no_record_own_email_part1_of_5:367 rentlgh.ca | not checked yet | not checked yet | not checked
    - P13_inferred_relationship_no_record_own_email_part1_of_5:1049 randonneursontario.ca | not checked yet | not checked yet | not checked
    - P13_inferred_relationship_no_record_own_email_part1_of_5:1050 raysolar.ca | not checked yet | not checked yet | not checked
    - P13_inferred_relationship_no_record_own_email_part1_of_5:1051 reliance.ca | not checked yet | not checked yet | not checked
    - P13_inferred_relationship_no_record_own_email_part1_of_5:1052 restigouche-hockey.ca | not checked yet | not checked yet | not checked
    - P13_inferred_relationship_no_record_own_email_part1_of_5:1053 reyrey.ca | not checked yet | not checked yet | not checked
    - P13_inferred_relationship_no_record_own_email_part1_of_5:5509 ramassagevip.ca | not checked yet | not checked yet | not checked
    - P13_inferred_relationship_no_record_own_email_part1_of_5:5510 ranchwinslow.ca | not checked yet | not checked yet | not checked
    - P13_inferred_relationship_no_record_own_email_part1_of_5:5511 ras-nsa.ca | not checked yet | not checked yet | not checked
    - P13_inferred_relationship_no_record_own_email_part1_of_5:5512 rcentres.qc.ca | not checked yet | not checked yet | not checked
- **19 buyer name is a name (not a domain or a page title)**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:13 uwindsor.ca | uwindsor.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:28 thebigcarrot.ca | thebigcarrot.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:33 ovs.com | ovs.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:79 hacc.edu | hacc.edu
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:91 cognizant.com | cognizant.com
    - P01_GOLD_active_relationship_invoicing_AP_email:415 capreit.ca | capreit.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:456 gov.edmonton.ab.ca | gov.edmonton.ab.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:460 arthomson.com | arthomson.com
    - P01_GOLD_active_relationship_invoicing_AP_email:506 bcib.ca | bcib.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:522 toronto.ca | toronto.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:549 slrd.bc.ca | slrd.bc.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:564 corporate.exxonmobil.com | corporate.exxonmobil.com
- **22 one row per organisation name (same name twice)**
    - P03_active_relationship_purchasing_email:227 Westbank First Nation | 2 rows, same mail domain: wfn.ca
    - P04_active_relationship_general_email:341 Cégep de Victoriaville. | 2 rows, same mail domain: cegepvicto.ca
    - P05_likely_active_awarded_12_36_months_any_email:6 Brandon University | 2 rows, same mail domain: brandonu.ca
- **23 one row per site domain (two rows, different mailboxes, same domain)**
    - P01_GOLD_active_relationship_invoicing_AP_email:26 University of Toronto | utoronto.ca: 2 rows, ap.fsd@utoronto.ca; fmdinvoice.utsc@utoronto.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:45 Ville de Gatineau | gatineau.ca: 2 rows, gatineau.factures@gatineau.ca; idgatineau@gatineau.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:54 Ville de Montréal | montreal.ca: 2 rows, facture@montreal.ca; comptesapayer@montreal.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:71 Ville de Laval | laval.ca: 3 rows, comptespayables@laval.ca; lavaleconomique@laval.ca; info@laval.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:80 Ville de Blainville | blainville.ca: 2 rows, approvisionnements@blainville.ca; finances@blainville.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:103 Texas Department of Insurance | texas.gov: 7 rows, invoices@tdi.texas.gov; ap@tsl.texas.gov; accounts.payable@tpwd.texas.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:117 University of Ottawa | uottawa.ca: 2 rows, payables@uottawa.ca; info@emba.uottawa.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:181 Oregon Department of Transportation | oregon.gov: 3 rows, opoinvoiceinquiries@odot.oregon.gov; omdaccounts.payable@omd.oregon.gov; odf.accountspayable@oregon.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:183 Texas Tech University Health Sciences Ce | ttuhsc.edu: 2 rows, Accounts.Payable@ttuhsc.edu; accountspayableelp@ttuhsc.edu
    - P01_GOLD_active_relationship_invoicing_AP_email:214 Metrolinx | metrolinx.com: 2 rows, it.invoices@metrolinx.com; rti.invoices@metrolinx.com
    - P01_GOLD_active_relationship_invoicing_AP_email:234 Niagara Region | niagararegion.ca: 2 rows, constructioninvoices@niagararegion.ca; NRHCapitalWorks@niagararegion.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:325 Virginia State Police | virginia.gov: 5 rows, ap@vsp.virginia.gov; accountspayable@energy.virginia.gov; support@dhrm.virginia.gov
- **25 jurisdiction vs mailbox top-level domain**
    - P13_inferred_relationship_no_record_own_email_part1_of_5:442 Rheinmetall AG | CA / rheinmetall.com.au
    - P13_inferred_relationship_no_record_own_email_part1_of_5:454 Westpac | CA / westpac.com.au
    - P13_inferred_relationship_no_record_own_email_part1_of_5:493 United States Postal Service | CA / usps.gov
    - P13_inferred_relationship_no_record_own_email_part1_of_5:1153 Randstad Deutschland | CA / randstad.de
    - P13_inferred_relationship_no_record_own_email_part1_of_5:2492 LA MAISON DES JEUNES DE PLESSISVILLE INC | QC / lycos.fr
    - P13_inferred_relationship_no_record_own_email_part1_of_5:3071 The Redeemed Christian Church of God Lov | SK / loveassembly.co.uk
    - P13_inferred_relationship_no_record_own_email_part1_of_5:6748 Trotec Laser Canada | QC / troteclaser.com.au
    - P13_inferred_relationship_no_record_own_email_part2_of_5:3059 KNDS | CA / knds.de
    - P13_inferred_relationship_no_record_own_email_part2_of_5:3078 The Warehouse Group | CA / thewarehousegroup.co.nz
    - P13_inferred_relationship_no_record_own_email_part3_of_5:887 akelius.ca | CA / akelius.fr
    - P13_inferred_relationship_no_record_own_email_part3_of_5:1235 apexauctions.ca | CA / apexauctions.co.uk
    - P13_inferred_relationship_no_record_own_email_part3_of_5:4803 dermfix.ca | CA / dermfix.uk
- **26 currency filled when a value is filled**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:22 RENTON SCHOOL DISTRICT #403 | 332345.13 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:408 Rectorado de la Universitat de València | 12698.25 (source field: PayableAmount)
    - P01_GOLD_active_relationship_invoicing_AP_email:419 BRINKS DE COLOMBIA S.A. | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:438 University of North Dakota | 145.850 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:461 BELLEVUE, CITY OF | 35488873.2 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:468 UNIVERSITY PLACE SCHOOL DISTRICT #83 | 685477.9 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:485 North Dakota State University | 35.000 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:490 BELLEVUE SCHOOL DISTRICT #405 | 5395.88 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:495 SNOQUALMIE VALLEY SCHOOL DISTRICT #410 | 23980.42 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:500 MARYLAND STADIUM AUTHORITY | 251569.05 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:513 ECOPETROL S A | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:541 Fundación para la Investigación del Hosp | 1236.23 (source field: PayableAmount)

## Rows per package
- P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email: 18
- P01T_active_service_seen_on_buyer_site_invoicing_AP_email: 90
- P01_GOLD_active_relationship_invoicing_AP_email: 564
- P02_active_relationship_finance_accounting_email: 338
- P03_active_relationship_purchasing_email: 226
- P04_active_relationship_general_email: 1570
- P05_likely_active_awarded_12_36_months_any_email: 375
- P06M_member_or_regulated_payer_of_canadian_body_other_email: 168
- P06T_active_service_seen_on_buyer_site_other_email: 2423
- P06_client_listing_invoicing_AP_email: 160
- P07_client_listing_finance_or_purchasing_email: 245
- P08_client_listing_general_email: 3054
- P09_older_contract_or_payment_any_email: 364
- P10_linked_from_vendor_site_any_email: 2600
- P11_any_relationship_email_not_yet_confirmed: 504
- P12_weaker_relationship_within_5_years_own_email: 22
- P13_inferred_relationship_no_record_own_email: 39899

## Field fill across all delivered rows (value present, not `not_published`)
- buyer_website: 52620 (100.0%)
- vendor_address: 49472 (94.0%)
- vendor_website: 48090 (91.4%)
- buyer_logo_url: 31076 (59.1%)
- buyer_address: 30542 (58.0%)
- buyer_phone: 21864 (41.6%)
- vendor_phone: 17017 (32.3%)
- contract_link: 12721 (24.2%)
- vendor_logo_url: 6772 (12.9%)
- buyer_legal_name_as_published: 6549 (12.4%)
- vendor_legal_name: 6439 (12.2%)
- award_date: 6416 (12.2%)
- vendor_registry_id: 5230 (9.9%)
- vendor_emails: 4274 (8.1%)
- vendor_bn9: 2442 (4.6%)
- contract_value: 2285 (4.3%)
- vendor_incorporation_date: 2069 (3.9%)
- ap_phone: 1758 (3.3%)
- invoice_mailing_address: 1673 (3.2%)
- end_date: 1656 (3.1%)
- buyer_bn_as_published: 1615 (3.1%)
- invoicing_requirements: 1344 (2.6%)
- payment_terms_as_published: 153 (0.3%)
- ap_contact_name_as_published: 129 (0.2%)
- po_required_as_published: 124 (0.2%)
- invoice_portal_url: 48 (0.1%)
- vendor_neq: 23 (0.0%)

## Canada-proof families
- other: 36963; source field: 15657

## Buyer types
- organisation (type not stated in the record): 34350
- company (private sector): 8015
- non-profit / association / cultural body: 6164
- municipality / local government: 1107
- government ministry / agency: 960
- hospital / health authority: 655
- university / college: 421
- utility / public corporation: 409
- transport / transit authority: 176
- school board / school district: 170
- First Nation / Indigenous government: 153
- US government body (federal, state or local): 29
- US city / county / local government: 11

## DMARC posture of the delivered mailboxes
- v=DMARC1; p=none (monitor only, no enforcement): 20793
- no DMARC record: 17585
- p=quarantine: 9002
- p=reject: 4773
- not checked yet: 417
- invalid DMARC record: 44
- DNS lookup failed: 6
