# Deep audit — 63599 delivered rows in 17 packages (32 files), 2026-11-08

Result: **PASS** — 11 hard checks, 17 soft checks; hard failures: 0. Every flagged row is listed in `audit_flags.csv` with its reasons.

| # | check | kind | rows flagged | verdict |
|---|---|---|---|---|
| 1 | header: identical columns in every file (106 since 2026-11-06) | hard | 0 | PASS |
| 2 | mailbox syntax | hard | 0 | PASS |
| 3 | mailbox referee-confirmed (all but P11) | hard | 0 | PASS |
| 4 | mail server (MX or A) on the mailbox domain | hard | 0 | PASS |
| 4b | mail server not yet checked (row newer than the last DNS pass) | soft | 23 | REVIEW |
| 5 | no webmail domain | hard | 0 | PASS |
| 6 | no person-like local part | hard | 0 | PASS |
| 7 | role word in the local part | soft | 3535 | REVIEW |
| 8 | receivables-looking local part graded invoicing/AP | soft | 35 | REVIEW |
| 9 | shared government domain: page or quote names the body | soft | 2 | REVIEW |
| 10 | regional token of a multinational on a differently-located body | soft | 0 | PASS |
| 11 | quote contains the address | hard | 0 | PASS |
| 11b | quote shows the label next to the address (referee saw the address on the page) | soft | 0 | PASS |
| 12 | evidence page on the organisation's domain (or its site) | soft | 3734 | REVIEW |
| 13 | email_type label matches grade | hard | 0 | PASS |
| 14 | DMARC / SPF / provider columns filled | soft | 0 | PASS |
| 15 | tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m) | soft | 0 | PASS |
| 16 | vendor named and Canada proof present | hard | 0 | PASS |
| 17 | Canada proof is a source field or the vendor's site (never a name) | soft | 0 | PASS |
| 18 | record link present for dated-record tiers | soft | 0 | PASS |
| 19 | buyer name is a name (not a domain or a page title) | soft | 22853 | REVIEW |
| 20 | legal name is not a fragment or a platform copyright | soft | 42 | REVIEW |
| 21 | one row per mailbox | hard | 0 | PASS |
| 22 | one row per organisation name (same name twice) | soft | 8 | REVIEW |
| 23 | one row per site domain (two rows, different mailboxes, same domain) | soft | 63 | REVIEW |
| 24 | no blank cell | hard | 0 | PASS |
| 25 | jurisdiction vs mailbox top-level domain | soft | 40 | REVIEW |
| 26 | currency filled when a value is filled | soft | 46 | REVIEW |

## Examples of flagged rows (first 12 per check)
- **4b mail server not yet checked (row newer than the last DNS pass)**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:90 Cleveland State University | csu.ohio.edu
    - P01_GOLD_active_relationship_invoicing_AP_email:438 The Clorox Company of Canada Ltd. | uberfreight.com
    - P03_active_relationship_purchasing_email:203 Wynn Las Vegas LLC. | wynnlasvegas.com
    - P05_likely_active_awarded_12_36_months_any_email:135 California Institute Of Technology | caltech.edu
    - P06T_active_service_seen_on_buyer_site_other_email:1081 bomodels.es | bomodels.es
    - P06T_active_service_seen_on_buyer_site_other_email:1350 metrovac.com | metrovac.com
    - P06T_active_service_seen_on_buyer_site_other_email:1395 bareoriginskin.com | bareoriginskin.com
    - P06T_active_service_seen_on_buyer_site_other_email:1537 phoxydesign.com | phoxydesign.co.uk
    - P06T_active_service_seen_on_buyer_site_other_email:2084 niafreshmarket.com | niafreshmarket.com
    - P06_client_listing_invoicing_AP_email:110 repository.cam.ac.uk | admin.cam.ac.uk
    - P06_client_listing_invoicing_AP_email:134 A campus of The California State Univers | cpp.edu
    - P06_client_listing_invoicing_AP_email:144 KBCC | lehman.cuny.edu
- **7 role word in the local part**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:16 Cameco Corporation | ap_cameco@cameco.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:43 New Relic | ap_ireland@newrelic.com
    - P01_GOLD_active_relationship_invoicing_AP_email:266 Town of Oakville | ap_inquiries@oakville.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:292 Miami-Dade County (business unit CU05010 | invsubp@miamidade.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:381 BELL TEXTRON INC | APBell@textron.com
    - P02_active_relationship_finance_accounting_email:7 Agriculture and Agri-Food Canada | directdeposit.depotdirect@canada.ca
    - P02_active_relationship_finance_accounting_email:13 Crown-Indigenous Relations and Northern  | depotdirect-directdeposit@sac-isc.gc.ca
    - P02_active_relationship_finance_accounting_email:14 Department of Justice Canada | mdv_dpf@justice.gc.ca
    - P02_active_relationship_finance_accounting_email:18 Health Canada | hc.direct.deposit.requests-demande.de.depot.direct.sc@canada.ca
    - P02_active_relationship_finance_accounting_email:19 Innovation, Science and Economic Develop | ifmscustomer-clientsifm@ised-isde.gc.ca
    - P02_active_relationship_finance_accounting_email:21 National Defence | ddenrol-inscriredd@forces.gc.ca
    - P02_active_relationship_finance_accounting_email:29 Social Sciences and Humanities Research  | directdeposit-depotdirect@crsh-sshrc.gc.ca
- **8 receivables-looking local part graded invoicing/AP**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:11 Empress | payments@villageofempress.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:4 Texas Tech University | payment.strategies@ttu.edu
    - P01_GOLD_active_relationship_invoicing_AP_email:38 Environment and Climate Change Canada | renseignement-paiements-payments-inquiry@ec.gc.ca
    - P05_likely_active_awarded_12_36_months_any_email:25 Martensville | payments@martensville.ca
    - P06_client_listing_invoicing_AP_email:27 University of Bath | payments@bath.ac.uk
    - P06_client_listing_invoicing_AP_email:69 teamviewer.com | payments@teamviewer.com
    - P06_client_listing_invoicing_AP_email:146 Blomidon Nurseries (1970) Limited | payments@blomidonnurseries.com
    - P10_linked_from_vendor_site_any_email:12 gov.scot | online_payments@gov.scot
    - P10_linked_from_vendor_site_any_email:29 WeirFoulds LLP | payments@weirfoulds.com
    - P10_linked_from_vendor_site_any_email:36 bcica.org | payments@bcica.org
    - P11_any_relationship_email_not_yet_confirmed:92 Social Security Administration - Social  | payment.inquiries@ssa.gov
    - P13_inferred_relationship_no_record_own_email_part1_of_16:10 THE ROYAL CANADIAN COLLEGE OF ORGANISTS- | payment@rcco-ottawa.ca
- **9 shared government domain: page or quote names the body**
    - P01_GOLD_active_relationship_invoicing_AP_email:42 Canadian Space Agency | invoicing.csa-asc.facturation@canada.ca ← https://www.canada.ca/en/public-services-procurement/services/payments-to-from-g
    - P13_inferred_relationship_no_record_own_email_part1_of_16:542 Landlord and Tenant Board | ltbpayments@ontario.ca ← https://tribunalsontario.ca/ltb/contact/
- **12 evidence page on the organisation's domain (or its site)**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:18 Motorola Solutions, Inc | recepcionfacturas@motorolasolutions.com on web.archive.org (site motorolasolutions.com)
    - P01_GOLD_active_relationship_invoicing_AP_email:2 Department of Defence | invoices@defence.gov.au on web.archive.org (site defence.gov.au)
    - P01_GOLD_active_relationship_invoicing_AP_email:3 Department of Industry, Science and Reso | einvoicingqueries@industry.gov.au on directory.peppol.eu (site industry.gov.au)
    - P01_GOLD_active_relationship_invoicing_AP_email:50 Natural Sciences and Engineering Researc | payables@nserc-crsng.gc.ca on nserc-crsng.canada.ca (site nserc-crsng.gc.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:65 Ville de Montréal | facture@montreal.ca on ville.montreal.qc.ca (site montreal.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:94 Ville de Farnham | comptespayables@ville.farnham.qc.ca on web.archive.org (site ville.farnham.qc.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:112 UK Atomic Energy Authority | finance@uk-atomic-energy.org.uk on assets.publishing.service.gov.uk (site gov.uk)
    - P01_GOLD_active_relationship_invoicing_AP_email:125 City of Chestermere | city.ap@chestermere.ca on thecityofchestermere.ca (site chestermere.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:131 Newfoundland and Labrador Liquor Corpora | Accounts.Payable@nlliquor.com on nlliquorcorp.com (site nlliquor.com)
    - P01_GOLD_active_relationship_invoicing_AP_email:133 The Ottawa Hospital | tohaccountspayable@toh.ca on ottawahospital.on.ca (site toh.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:155 UK Research and Innovation | finance@uksbs.co.uk on ukri.org (site uksbs.co.uk)
    - P01_GOLD_active_relationship_invoicing_AP_email:161 Department of Foreign Affairs and Trade | dfat.e-invoicing.prod@dfat.gov.au on directory.peppol.eu (site dfat.gov.au)
- **19 buyer name is a name (not a domain or a page title)**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:33 ovs.com | ovs.com
    - P01_GOLD_active_relationship_invoicing_AP_email:432 capreit.ca | capreit.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:521 bcib.ca | bcib.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:565 slrd.bc.ca | slrd.bc.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:582 corporate.exxonmobil.com | corporate.exxonmobil.com
    - P02_active_relationship_finance_accounting_email:280 healthpartners.ca | healthpartners.ca
    - P02_active_relationship_finance_accounting_email:285 osoyoos.ca | osoyoos.ca
    - P02_active_relationship_finance_accounting_email:322 msvu.ca | msvu.ca
    - P02_active_relationship_finance_accounting_email:351 ccib.ca | ccib.ca
    - P03_active_relationship_purchasing_email:175 surreyplace.ca | surreyplace.ca
    - P03_active_relationship_purchasing_email:177 rrc.ca | rrc.ca
    - P03_active_relationship_purchasing_email:207 smu.ca | smu.ca
- **20 legal name is not a fragment or a platform copyright**
    - P03_active_relationship_purchasing_email:208 onsemi | onsemi (label per Wikidata Q1671509, official website on the organisat
    - P04_active_relationship_general_email:117 Ministère de la Culture et des Communica | ministère de la Culture et des Communications (label per Wikidata Q331
    - P04_active_relationship_general_email:161 Ministère de la Cybersécurité et du Numé | ministère de la Cybersécurité et du Numérique (label per Wikidata Q110
    - P06T_active_service_seen_on_buyer_site_other_email:369 Uppdoo | uppdoo Inc. (as registered: Corporations Canada (open data), corporati
    - P06T_active_service_seen_on_buyer_site_other_email:1065 MyHealth Inc | myhealth inc. (as registered: Corporations Canada (open data), corpora
    - P06T_active_service_seen_on_buyer_site_other_email:1236 do+dare undie co. | do+dare undie co. (label per Wikidata Q141143888, official website on 
    - P06T_active_service_seen_on_buyer_site_other_email:1402 de Montigny Contemporain | de Montigny Contemporain (label per Wikidata Q139820434, official webs
    - P07_client_listing_finance_or_purchasing_email:81 lepointdevente.com | lepointdevente.com (recipient legal name in the federal grants & contr
    - P08_client_listing_general_email:2049 Christian Life Community | Christian Life Community (stated on https://www.christianlifecommunity
    - P10_linked_from_vendor_site_any_email:1497 Digify SEO Company | digify seo company Incorporated (as registered: Corporations Canada (o
    - P13_inferred_relationship_no_record_own_email_part10_of_16:2187 Mon-Proprio.ca Inc | mon-proprio.ca inc. (as registered: Registraire des entreprises du Qué
    - P13_inferred_relationship_no_record_own_email_part14_of_16:710 Weedjar | weedjar Inc. (as registered: Corporations Canada (open data), corporat
- **22 one row per organisation name (same name twice)**
    - P01_GOLD_active_relationship_invoicing_AP_email:154 MRC de Manicouagan | 2 rows, same mail domain: mrcmanicouagan.qc.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:350 Town of Lincoln | 2 rows, same mail domain: lincoln.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:421 City of Kamloops | 2 rows, same mail domain: kamloops.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:520 Enbridge Inc. | 2 rows, same mail domain: enbridge.com
    - P04_active_relationship_general_email:330 Cégep de Victoriaville. | 2 rows, same mail domain: cegepvicto.ca
    - P04_active_relationship_general_email:1615 Acadia University | 2 rows, same mail domain: acadiau.ca
    - P05_likely_active_awarded_12_36_months_any_email:5 Brandon University | 2 rows, same mail domain: brandonu.ca
    - P06T_active_service_seen_on_buyer_site_other_email:65 City of Dawson | 2 rows, same mail domain: cityofdawson.ca
- **23 one row per site domain (two rows, different mailboxes, same domain)**
    - P01_GOLD_active_relationship_invoicing_AP_email:2 Department of Defence | defence.gov.au: 2 rows, invoices@defence.gov.au; peppol.einvoices@defence.gov.au
    - P01_GOLD_active_relationship_invoicing_AP_email:26 University of Toronto | utoronto.ca: 2 rows, ap.fsd@utoronto.ca; fmdinvoice.utsc@utoronto.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:56 Ville de Gatineau | gatineau.ca: 2 rows, gatineau.factures@gatineau.ca; idgatineau@gatineau.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:65 Ville de Montréal | montreal.ca: 2 rows, facture@montreal.ca; comptesapayer@montreal.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:81 Ville de Laval | laval.ca: 3 rows, comptespayables@laval.ca; lavaleconomique@laval.ca; info@laval.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:90 Ville de Blainville | blainville.ca: 2 rows, approvisionnements@blainville.ca; finances@blainville.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:113 Texas Department of Insurance | texas.gov: 7 rows, invoices@tdi.texas.gov; ap@tsl.texas.gov; accounts.payable@tpwd.texas.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:127 University of Ottawa | uottawa.ca: 2 rows, payables@uottawa.ca; info@emba.uottawa.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:193 Oregon Department of Transportation | oregon.gov: 3 rows, opoinvoiceinquiries@odot.oregon.gov; omdaccounts.payable@omd.oregon.gov; odf.accountspayable@oregon.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:195 Texas Tech University Health Sciences Ce | ttuhsc.edu: 2 rows, Accounts.Payable@ttuhsc.edu; accountspayableelp@ttuhsc.edu
    - P01_GOLD_active_relationship_invoicing_AP_email:227 Metrolinx | metrolinx.com: 2 rows, it.invoices@metrolinx.com; rti.invoices@metrolinx.com
    - P01_GOLD_active_relationship_invoicing_AP_email:249 Niagara Region | niagararegion.ca: 2 rows, constructioninvoices@niagararegion.ca; NRHCapitalWorks@niagararegion.ca
- **25 jurisdiction vs mailbox top-level domain**
    - P13_inferred_relationship_no_record_own_email_part10_of_16:696 lifelyhome.ca | CA / lifely.com.au
    - P13_inferred_relationship_no_record_own_email_part10_of_16:2660 nakie.ca | CA / nakie.com.au
    - P13_inferred_relationship_no_record_own_email_part11_of_16:505 opal-canada.ca | CA / opal.fr
    - P13_inferred_relationship_no_record_own_email_part11_of_16:1054 pccarx.ca | CA / pccarx.com.au
    - P13_inferred_relationship_no_record_own_email_part11_of_16:1721 practs.ca | CA / practs.de
    - P13_inferred_relationship_no_record_own_email_part11_of_16:2915 Roka Harness Pty Ltd | CA / rokaharness.com.au
    - P13_inferred_relationship_no_record_own_email_part12_of_16:908 Skin Cupid | CA / skincupid.co.uk
    - P13_inferred_relationship_no_record_own_email_part12_of_16:1105 Snowdonia Cheese Ltd | CA / snowdonia-cheese.co.uk
    - P13_inferred_relationship_no_record_own_email_part15_of_16:520 Beckhoff Automation Ltd. | CA / beckhoff.de
    - P13_inferred_relationship_no_record_own_email_part15_of_16:1573 Bernafon Canada | ON / bernafon.com.au
    - P13_inferred_relationship_no_record_own_email_part16_of_16:428 Déontologie : approche comparée FR / QC | CA / univ-droit.fr
    - P13_inferred_relationship_no_record_own_email_part16_of_16:921 Shah's Halal Food | CA / shahshalalfood.co.uk
- **26 currency filled when a value is filled**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:22 RENTON SCHOOL DISTRICT #403 | 332345.13 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:425 Rectorado de la Universitat de València | 12698.25 (source field: PayableAmount)
    - P01_GOLD_active_relationship_invoicing_AP_email:436 BRINKS DE COLOMBIA S.A. | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:454 University of North Dakota | 145.850 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:476 BELLEVUE, CITY OF | 35488873.2 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:484 UNIVERSITY PLACE SCHOOL DISTRICT #83 | 685477.9 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:501 North Dakota State University | 35.000 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:506 BELLEVUE SCHOOL DISTRICT #405 | 5395.88 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:511 SNOQUALMIE VALLEY SCHOOL DISTRICT #410 | 23980.42 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:516 MARYLAND STADIUM AUTHORITY | 251569.05 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:528 ECOPETROL S A | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:557 Fundación para la Investigación del Hosp | 1236.23 (source field: PayableAmount)

## Independent QA audit of dataset records (lane chatgpt, 200 random records re-opened at the publishing source)
- link_opened: yes 187, blocked 13
- buyer_match: yes 181, not_shown 14, no 5
- vendor_match: yes 173, not_shown 27
- title_match: yes 181, not_shown 13, no 6
- value_match: yes 120, not_shown 77, no 3
- dates_match: not_shown 109, yes 83, no 8
- status_supported: unclear 100, yes 89, no 11
- reading: a `no` on buyer_match in the sample was a ministry renamed since the award (same body); `status_supported = unclear / no` concentrates in SEAO records marked ongoing_inferred, which the packages rank as B/C, never as A.

## Rows per package
- P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email: 20
- P01T_active_service_seen_on_buyer_site_invoicing_AP_email: 92
- P01_GOLD_active_relationship_invoicing_AP_email: 582
- P02_active_relationship_finance_accounting_email: 369
- P03_active_relationship_purchasing_email: 225
- P04_active_relationship_general_email: 1615
- P05_likely_active_awarded_12_36_months_any_email: 379
- P06M_member_or_regulated_payer_of_canadian_body_other_email: 167
- P06T_active_service_seen_on_buyer_site_other_email: 2435
- P06_client_listing_invoicing_AP_email: 163
- P07_client_listing_finance_or_purchasing_email: 249
- P08_client_listing_general_email: 3037
- P09_older_contract_or_payment_any_email: 369
- P10_linked_from_vendor_site_any_email: 2590
- P11_any_relationship_email_not_yet_confirmed: 498
- P12_weaker_relationship_within_5_years_own_email: 21
- P13_inferred_relationship_no_record_own_email: 50788

## Field fill across all delivered rows (value present, not `not_published`)
- buyer_website: 63599 (100.0%)
- vendor_address: 60541 (95.2%)
- vendor_website: 59553 (93.6%)
- vendor_phone: 56175 (88.3%)
- vendor_bn9: 53073 (83.4%)
- buyer_logo_url: 52301 (82.2%)
- buyer_phone: 49441 (77.7%)
- buyer_address: 47710 (75.0%)
- buyer_legal_name_as_published: 30146 (47.4%)
- contract_link: 12811 (20.1%)
- buyer_bn_as_published: 12371 (19.5%)
- vendor_legal_name: 9691 (15.2%)
- vendor_registry_id: 8256 (13.0%)
- vendor_incorporation_date: 8245 (13.0%)
- vendor_logo_url: 7178 (11.3%)
- award_date: 6492 (10.2%)
- vendor_neq: 5017 (7.9%)
- vendor_emails: 4346 (6.8%)
- ap_phone: 2628 (4.1%)
- contract_value: 2332 (3.7%)
- invoice_mailing_address: 2126 (3.3%)
- end_date: 1757 (2.8%)
- invoicing_requirements: 1644 (2.6%)
- invoice_portal_url: 911 (1.4%)
- po_required_as_published: 716 (1.1%)
- payment_terms_as_published: 581 (0.9%)
- ap_contact_name_as_published: 297 (0.5%)

## Canada-proof families
- other: 47253; source field: 16346

## Buyer types
- organisation (type not stated in the record): 33728
- company (private sector): 10794
- non-profit / association / cultural body: 7226
- company (private sector) (from the organisation's name / web domain): 3571
- municipality / local government: 1336
- government ministry / agency: 1213
- municipality / local government (from the organisation's name / web domain): 1011
- hospital / health authority: 936
- non-profit / association / cultural body (from the organisation's name / web domain): 831
- university / college: 591
- utility / public corporation: 482
- university / college (from the organisation's name / web domain): 426
- hospital / health authority (from the organisation's name / web domain): 328
- transport / transit authority: 207
- school board / school district: 181
- First Nation / Indigenous government: 166
- government ministry / agency (from the organisation's name / web domain): 147
- religious organisation (from the organisation's name / web domain): 143
- utility / public corporation (from the organisation's name / web domain): 97
- transport / transit authority (from the organisation's name / web domain): 60
- First Nation / Indigenous government (from the organisation's name / web domain): 43
- US government body (federal, state or local): 29
- school board / school district (from the organisation's name / web domain): 27
- library (from the organisation's name / web domain): 15
- US city / county / local government: 11

## DMARC posture of the delivered mailboxes
- v=DMARC1; p=none (monitor only, no enforcement): 26429
- no DMARC record: 21269
- p=quarantine: 10431
- p=reject: 5403
- invalid DMARC record: 59
- DNS lookup failed: 8
