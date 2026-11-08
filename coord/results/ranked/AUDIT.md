# Deep audit — 63624 delivered rows in 17 packages (32 files), 2026-11-08

Result: **PASS** — 11 hard checks, 17 soft checks; hard failures: 0. Every flagged row is listed in `audit_flags.csv` with its reasons.

| # | check | kind | rows flagged | verdict |
|---|---|---|---|---|
| 1 | header: identical columns in every file (106 since 2026-11-06) | hard | 0 | PASS |
| 2 | mailbox syntax | hard | 0 | PASS |
| 3 | mailbox referee-confirmed (all but P11) | hard | 0 | PASS |
| 4 | mail server (MX or A) on the mailbox domain | hard | 0 | PASS |
| 4b | mail server not yet checked (row newer than the last DNS pass) | soft | 57 | REVIEW |
| 5 | no webmail domain | hard | 0 | PASS |
| 6 | no person-like local part | hard | 0 | PASS |
| 7 | role word in the local part | soft | 3537 | REVIEW |
| 8 | receivables-looking local part graded invoicing/AP | soft | 36 | REVIEW |
| 9 | shared government domain: page or quote names the body | soft | 3 | REVIEW |
| 10 | regional token of a multinational on a differently-located body | soft | 0 | PASS |
| 11 | quote contains the address | hard | 0 | PASS |
| 11b | quote shows the label next to the address (referee saw the address on the page) | soft | 0 | PASS |
| 12 | evidence page on the organisation's domain (or its site) | soft | 3727 | REVIEW |
| 13 | email_type label matches grade | hard | 0 | PASS |
| 14 | DMARC / SPF / provider columns filled | soft | 0 | PASS |
| 15 | tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m) | soft | 0 | PASS |
| 16 | vendor named and Canada proof present | hard | 0 | PASS |
| 17 | Canada proof is a source field or the vendor's site (never a name) | soft | 0 | PASS |
| 18 | record link present for dated-record tiers | soft | 0 | PASS |
| 19 | buyer name is a name (not a domain or a page title) | soft | 22866 | REVIEW |
| 20 | legal name is not a fragment or a platform copyright | soft | 42 | REVIEW |
| 21 | one row per mailbox | hard | 0 | PASS |
| 22 | one row per organisation name (same name twice) | soft | 8 | REVIEW |
| 23 | one row per site domain (two rows, different mailboxes, same domain) | soft | 62 | REVIEW |
| 24 | no blank cell | hard | 0 | PASS |
| 25 | jurisdiction vs mailbox top-level domain | soft | 40 | REVIEW |
| 26 | currency filled when a value is filled | soft | 46 | REVIEW |

## Examples of flagged rows (first 12 per check)
- **4b mail server not yet checked (row newer than the last DNS pass)**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:91 Cleveland State University | csu.ohio.edu
    - P01_GOLD_active_relationship_invoicing_AP_email:160 Department of Homeland Security | dhs.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:234 BANK OF ENGLAND | bankofengland.co.uk
    - P01_GOLD_active_relationship_invoicing_AP_email:366 NATO Joint Warfare Centre (Stavanger) | jwc.nato.int
    - P01_GOLD_active_relationship_invoicing_AP_email:445 The Clorox Company of Canada Ltd. | uberfreight.com
    - P01_GOLD_active_relationship_invoicing_AP_email:447 California Department of Water Resources | dgs.ca.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:479 New York State Energy Research and Devel | nyserda.ny.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:532 Indiana Department of Transportation | health.in.gov
    - P02_active_relationship_finance_accounting_email:59 Institut national de la recherche scient | adm.inrs.ca
    - P02_active_relationship_finance_accounting_email:348 Trustees Of The University Of Pennsylvan | wharton.upenn.edu
    - P03_active_relationship_purchasing_email:206 Wynn Las Vegas LLC. | wynnlasvegas.com
    - P04_active_relationship_general_email:959 ACASTA PARTNERS US LLC - ACASTA GLOBAL M | acastapartners.com
- **7 role word in the local part**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:16 Cameco Corporation | ap_cameco@cameco.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:43 New Relic | ap_ireland@newrelic.com
    - P01_GOLD_active_relationship_invoicing_AP_email:272 Town of Oakville | ap_inquiries@oakville.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:298 Miami-Dade County (business unit CU05010 | invsubp@miamidade.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:387 BELL TEXTRON INC | APBell@textron.com
    - P02_active_relationship_finance_accounting_email:7 Agriculture and Agri-Food Canada | directdeposit.depotdirect@canada.ca
    - P02_active_relationship_finance_accounting_email:13 Crown-Indigenous Relations and Northern  | depotdirect-directdeposit@sac-isc.gc.ca
    - P02_active_relationship_finance_accounting_email:14 Department of Justice Canada | mdv_dpf@justice.gc.ca
    - P02_active_relationship_finance_accounting_email:18 Health Canada | hc.direct.deposit.requests-demande.de.depot.direct.sc@canada.ca
    - P02_active_relationship_finance_accounting_email:19 Innovation, Science and Economic Develop | ifmscustomer-clientsifm@ised-isde.gc.ca
    - P02_active_relationship_finance_accounting_email:21 National Defence | ddenrol-inscriredd@forces.gc.ca
    - P02_active_relationship_finance_accounting_email:29 Social Sciences and Humanities Research  | directdeposit-depotdirect@crsh-sshrc.gc.ca
- **8 receivables-looking local part graded invoicing/AP**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:4 Texas Tech University | payment.strategies@ttu.edu
    - P01_GOLD_active_relationship_invoicing_AP_email:38 Environment and Climate Change Canada | renseignement-paiements-payments-inquiry@ec.gc.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:214 County of Minburn No. 27 | payments@minburncounty.ab.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:557 TMX Group Limited | payments@tmx.com
    - P05_likely_active_awarded_12_36_months_any_email:25 Martensville | payments@martensville.ca
    - P06_client_listing_invoicing_AP_email:27 University of Bath | payments@bath.ac.uk
    - P06_client_listing_invoicing_AP_email:69 teamviewer.com | payments@teamviewer.com
    - P06_client_listing_invoicing_AP_email:147 Blomidon Nurseries (1970) Limited | payments@blomidonnurseries.com
    - P10_linked_from_vendor_site_any_email:13 gov.scot | online_payments@gov.scot
    - P10_linked_from_vendor_site_any_email:31 WeirFoulds LLP | payments@weirfoulds.com
    - P10_linked_from_vendor_site_any_email:39 bcica.org | payments@bcica.org
    - P11_any_relationship_email_not_yet_confirmed:83 Social Security Administration - Social  | payment.inquiries@ssa.gov
- **9 shared government domain: page or quote names the body**
    - P01_GOLD_active_relationship_invoicing_AP_email:42 Canadian Space Agency | invoicing.csa-asc.facturation@canada.ca ← https://www.canada.ca/en/public-services-procurement/services/payments-to-from-g
    - P07_client_listing_finance_or_purchasing_email:25 transportation.ky.gov | finance.crcgroup@ky.gov ← https://finance.ky.gov/eProcurement/Pages/doing-business-with-the-commonwealth.a
    - P13_inferred_relationship_no_record_own_email_part1_of_16:543 Landlord and Tenant Board | ltbpayments@ontario.ca ← https://tribunalsontario.ca/ltb/contact/
- **12 evidence page on the organisation's domain (or its site)**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:18 Motorola Solutions, Inc | recepcionfacturas@motorolasolutions.com on web.archive.org (site motorolasolutions.com)
    - P01_GOLD_active_relationship_invoicing_AP_email:2 Department of Defence | invoices@defence.gov.au on web.archive.org (site defence.gov.au)
    - P01_GOLD_active_relationship_invoicing_AP_email:3 Department of Industry, Science and Reso | einvoicingqueries@industry.gov.au on directory.peppol.eu (site industry.gov.au)
    - P01_GOLD_active_relationship_invoicing_AP_email:50 Natural Sciences and Engineering Researc | payables@nserc-crsng.gc.ca on nserc-crsng.canada.ca (site nserc-crsng.gc.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:65 Ville de Montréal | facture@montreal.ca on ville.montreal.qc.ca (site montreal.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:94 Ville de Farnham | comptespayables@ville.farnham.qc.ca on web.archive.org (site ville.farnham.qc.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:113 UK Atomic Energy Authority | finance@uk-atomic-energy.org.uk on assets.publishing.service.gov.uk (site gov.uk)
    - P01_GOLD_active_relationship_invoicing_AP_email:125 City of Chestermere | city.ap@chestermere.ca on thecityofchestermere.ca (site chestermere.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:131 Newfoundland and Labrador Liquor Corpora | Accounts.Payable@nlliquor.com on nlliquorcorp.com (site nlliquor.com)
    - P01_GOLD_active_relationship_invoicing_AP_email:133 The Ottawa Hospital | tohaccountspayable@toh.ca on ottawahospital.on.ca (site toh.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:161 Department of Foreign Affairs and Trade | dfat.e-invoicing.prod@dfat.gov.au on directory.peppol.eu (site dfat.gov.au)
    - P01_GOLD_active_relationship_invoicing_AP_email:191 HM Land Registry | apinvoices@landregistry.gov.uk on assets.publishing.service.gov.uk (site gov.uk)
- **19 buyer name is a name (not a domain or a page title)**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:33 ovs.com | ovs.com
    - P01_GOLD_active_relationship_invoicing_AP_email:439 capreit.ca | capreit.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:531 bcib.ca | bcib.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:576 slrd.bc.ca | slrd.bc.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:593 corporate.exxonmobil.com | corporate.exxonmobil.com
    - P02_active_relationship_finance_accounting_email:295 healthpartners.ca | healthpartners.ca
    - P02_active_relationship_finance_accounting_email:300 osoyoos.ca | osoyoos.ca
    - P02_active_relationship_finance_accounting_email:343 msvu.ca | msvu.ca
    - P02_active_relationship_finance_accounting_email:376 ccib.ca | ccib.ca
    - P02_active_relationship_finance_accounting_email:379 OneChurch.To | OneChurch.To
    - P03_active_relationship_purchasing_email:178 surreyplace.ca | surreyplace.ca
    - P03_active_relationship_purchasing_email:180 rrc.ca | rrc.ca
- **20 legal name is not a fragment or a platform copyright**
    - P03_active_relationship_purchasing_email:211 onsemi | onsemi (label per Wikidata Q1671509, official website on the organisat
    - P04_active_relationship_general_email:111 Ministère de la Culture et des Communica | ministère de la Culture et des Communications (label per Wikidata Q331
    - P04_active_relationship_general_email:156 Ministère de la Cybersécurité et du Numé | ministère de la Cybersécurité et du Numérique (label per Wikidata Q110
    - P06T_active_service_seen_on_buyer_site_other_email:370 Uppdoo | uppdoo Inc. (as registered: Corporations Canada (open data), corporati
    - P06T_active_service_seen_on_buyer_site_other_email:1068 MyHealth Inc | myhealth inc. (as registered: Corporations Canada (open data), corpora
    - P06T_active_service_seen_on_buyer_site_other_email:1239 do+dare undie co. | do+dare undie co. (label per Wikidata Q141143888, official website on 
    - P06T_active_service_seen_on_buyer_site_other_email:1405 de Montigny Contemporain | de Montigny Contemporain (label per Wikidata Q139820434, official webs
    - P07_client_listing_finance_or_purchasing_email:82 lepointdevente.com | lepointdevente.com (recipient legal name in the federal grants & contr
    - P08_client_listing_general_email:2050 Christian Life Community | Christian Life Community (stated on https://www.christianlifecommunity
    - P10_linked_from_vendor_site_any_email:1503 Digify SEO Company | digify seo company Incorporated (as registered: Corporations Canada (o
    - P13_inferred_relationship_no_record_own_email_part10_of_16:2190 Mon-Proprio.ca Inc | mon-proprio.ca inc. (as registered: Registraire des entreprises du Qué
    - P13_inferred_relationship_no_record_own_email_part13_of_16:2741 COD3 Corporation | cod3 corporation (as registered: Canada's Business Registries, CC 1190
- **22 one row per organisation name (same name twice)**
    - P01_GOLD_active_relationship_invoicing_AP_email:154 MRC de Manicouagan | 2 rows, same mail domain: mrcmanicouagan.qc.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:428 City of Kamloops | 2 rows, same mail domain: kamloops.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:530 Enbridge Inc. | 2 rows, same mail domain: enbridge.com
    - P04_active_relationship_general_email:320 Cégep de Victoriaville. | 2 rows, same mail domain: cegepvicto.ca
    - P04_active_relationship_general_email:1583 Acadia University | 2 rows, same mail domain: acadiau.ca
    - P05_likely_active_awarded_12_36_months_any_email:5 Brandon University | 2 rows, same mail domain: brandonu.ca
    - P06T_active_service_seen_on_buyer_site_other_email:67 City of Dawson | 2 rows, same mail domain: cityofdawson.ca
    - P06T_active_service_seen_on_buyer_site_other_email:1886 Town of Lincoln | 2 rows, same mail domain: lincoln.ca
- **23 one row per site domain (two rows, different mailboxes, same domain)**
    - P01_GOLD_active_relationship_invoicing_AP_email:2 Department of Defence | defence.gov.au: 2 rows, invoices@defence.gov.au; peppol.einvoices@defence.gov.au
    - P01_GOLD_active_relationship_invoicing_AP_email:26 University of Toronto | utoronto.ca: 2 rows, ap.fsd@utoronto.ca; fmdinvoice.utsc@utoronto.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:56 Ville de Gatineau | gatineau.ca: 2 rows, gatineau.factures@gatineau.ca; idgatineau@gatineau.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:65 Ville de Montréal | montreal.ca: 2 rows, facture@montreal.ca; comptesapayer@montreal.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:81 Ville de Laval | laval.ca: 3 rows, comptespayables@laval.ca; lavaleconomique@laval.ca; info@laval.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:114 Texas Department of Insurance | texas.gov: 7 rows, invoices@tdi.texas.gov; ap@tsl.texas.gov; accounts.payable@tpwd.texas.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:127 University of Ottawa | uottawa.ca: 2 rows, payables@uottawa.ca; info@emba.uottawa.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:194 Oregon Department of Transportation | oregon.gov: 3 rows, opoinvoiceinquiries@odot.oregon.gov; omdaccounts.payable@omd.oregon.gov; odf.accountspayable@oregon.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:196 Texas Tech University Health Sciences Ce | ttuhsc.edu: 2 rows, Accounts.Payable@ttuhsc.edu; accountspayableelp@ttuhsc.edu
    - P01_GOLD_active_relationship_invoicing_AP_email:231 Metrolinx | metrolinx.com: 2 rows, it.invoices@metrolinx.com; rti.invoices@metrolinx.com
    - P01_GOLD_active_relationship_invoicing_AP_email:255 Niagara Region | niagararegion.ca: 2 rows, constructioninvoices@niagararegion.ca; NRHCapitalWorks@niagararegion.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:350 Virginia State Police | virginia.gov: 5 rows, ap@vsp.virginia.gov; accountspayable@energy.virginia.gov; support@dhrm.virginia.gov
- **25 jurisdiction vs mailbox top-level domain**
    - P13_inferred_relationship_no_record_own_email_part10_of_16:699 lifelyhome.ca | CA / lifely.com.au
    - P13_inferred_relationship_no_record_own_email_part10_of_16:2663 nakie.ca | CA / nakie.com.au
    - P13_inferred_relationship_no_record_own_email_part11_of_16:508 opal-canada.ca | CA / opal.fr
    - P13_inferred_relationship_no_record_own_email_part11_of_16:1057 pccarx.ca | CA / pccarx.com.au
    - P13_inferred_relationship_no_record_own_email_part11_of_16:1724 practs.ca | CA / practs.de
    - P13_inferred_relationship_no_record_own_email_part11_of_16:2918 Roka Harness Pty Ltd | CA / rokaharness.com.au
    - P13_inferred_relationship_no_record_own_email_part12_of_16:911 Skin Cupid | CA / skincupid.co.uk
    - P13_inferred_relationship_no_record_own_email_part12_of_16:1108 Snowdonia Cheese Ltd | CA / snowdonia-cheese.co.uk
    - P13_inferred_relationship_no_record_own_email_part15_of_16:524 Beckhoff Automation Ltd. | CA / beckhoff.de
    - P13_inferred_relationship_no_record_own_email_part15_of_16:1577 Bernafon Canada | ON / bernafon.com.au
    - P13_inferred_relationship_no_record_own_email_part16_of_16:432 Déontologie : approche comparée FR / QC | CA / univ-droit.fr
    - P13_inferred_relationship_no_record_own_email_part16_of_16:925 Shah's Halal Food | CA / shahshalalfood.co.uk
- **26 currency filled when a value is filled**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:23 RENTON SCHOOL DISTRICT #403 | 332345.13 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:432 Rectorado de la Universitat de València | 12698.25 (source field: PayableAmount)
    - P01_GOLD_active_relationship_invoicing_AP_email:443 BRINKS DE COLOMBIA S.A. | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:462 University of North Dakota | 145.850 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:485 BELLEVUE, CITY OF | 35488873.2 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:493 UNIVERSITY PLACE SCHOOL DISTRICT #83 | 685477.9 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:510 North Dakota State University | 35.000 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:515 BELLEVUE SCHOOL DISTRICT #405 | 5395.88 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:520 SNOQUALMIE VALLEY SCHOOL DISTRICT #410 | 23980.42 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:526 MARYLAND STADIUM AUTHORITY | 251569.05 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:538 ECOPETROL S A | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:568 Fundación para la Investigación del Hosp | 1236.23 (source field: PayableAmount)

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
- P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email: 19
- P01T_active_service_seen_on_buyer_site_invoicing_AP_email: 92
- P01_GOLD_active_relationship_invoicing_AP_email: 593
- P02_active_relationship_finance_accounting_email: 395
- P03_active_relationship_purchasing_email: 228
- P04_active_relationship_general_email: 1583
- P05_likely_active_awarded_12_36_months_any_email: 379
- P06M_member_or_regulated_payer_of_canadian_body_other_email: 168
- P06T_active_service_seen_on_buyer_site_other_email: 2440
- P06_client_listing_invoicing_AP_email: 165
- P07_client_listing_finance_or_purchasing_email: 252
- P08_client_listing_general_email: 3038
- P09_older_contract_or_payment_any_email: 373
- P10_linked_from_vendor_site_any_email: 2597
- P11_any_relationship_email_not_yet_confirmed: 488
- P12_weaker_relationship_within_5_years_own_email: 21
- P13_inferred_relationship_no_record_own_email: 50793

## Field fill across all delivered rows (value present, not `not_published`)
- buyer_website: 63624 (100.0%)
- vendor_website: 61793 (97.1%)
- vendor_address: 60825 (95.6%)
- vendor_phone: 56193 (88.3%)
- vendor_bn9: 53090 (83.4%)
- buyer_logo_url: 53079 (83.4%)
- buyer_phone: 49627 (78.0%)
- buyer_address: 47667 (74.9%)
- buyer_legal_name_as_published: 31841 (50.0%)
- buyer_bn_as_published: 13301 (20.9%)
- contract_link: 12831 (20.2%)
- vendor_legal_name: 9737 (15.3%)
- vendor_registry_id: 8268 (13.0%)
- vendor_incorporation_date: 8257 (13.0%)
- vendor_logo_url: 7184 (11.3%)
- award_date: 6499 (10.2%)
- vendor_neq: 5027 (7.9%)
- vendor_emails: 4345 (6.8%)
- ap_phone: 2635 (4.1%)
- contract_value: 2372 (3.7%)
- invoice_mailing_address: 2156 (3.4%)
- invoicing_requirements: 1803 (2.8%)
- end_date: 1771 (2.8%)
- invoice_portal_url: 1373 (2.2%)
- payment_terms_as_published: 1057 (1.7%)
- po_required_as_published: 1021 (1.6%)
- ap_contact_name_as_published: 415 (0.7%)

## Canada-proof families
- other: 47258; source field: 16366

## Buyer types
- organisation (type not stated in the record): 33390
- company (private sector): 10800
- non-profit / association / cultural body: 7229
- company (private sector) (from the organisation's name / web domain): 3775
- municipality / local government: 1337
- government ministry / agency: 1214
- municipality / local government (from the organisation's name / web domain): 1055
- hospital / health authority: 938
- non-profit / association / cultural body (from the organisation's name / web domain): 882
- university / college: 590
- utility / public corporation: 483
- university / college (from the organisation's name / web domain): 458
- hospital / health authority (from the organisation's name / web domain): 342
- transport / transit authority: 207
- school board / school district: 180
- First Nation / Indigenous government: 166
- government ministry / agency (from the organisation's name / web domain): 148
- religious organisation (from the organisation's name / web domain): 141
- utility / public corporation (from the organisation's name / web domain): 98
- transport / transit authority (from the organisation's name / web domain): 61
- First Nation / Indigenous government (from the organisation's name / web domain): 45
- school board / school district (from the organisation's name / web domain): 30
- US government body (federal, state or local): 29
- library (from the organisation's name / web domain): 15
- US city / county / local government: 11

## DMARC posture of the delivered mailboxes
- v=DMARC1; p=none (monitor only, no enforcement): 26438
- no DMARC record: 21273
- p=quarantine: 10437
- p=reject: 5410
- invalid DMARC record: 59
- DNS lookup failed: 7
