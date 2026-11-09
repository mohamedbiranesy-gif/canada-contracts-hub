# Deep audit — 63638 delivered rows in 17 packages (34 files), 2026-11-09

Result: **PASS** — 11 hard checks, 17 soft checks; hard failures: 0. Every flagged row is listed in `audit_flags.csv` with its reasons.

| # | check | kind | rows flagged | verdict |
|---|---|---|---|---|
| 1 | header: identical columns in every file (106 since 2026-11-06) | hard | 0 | PASS |
| 2 | mailbox syntax | hard | 0 | PASS |
| 3 | mailbox referee-confirmed (all but P11) | hard | 0 | PASS |
| 4 | mail server (MX or A) on the mailbox domain | hard | 0 | PASS |
| 4b | mail server not yet checked (row newer than the last DNS pass) | soft | 107 | REVIEW |
| 5 | no webmail domain | hard | 0 | PASS |
| 6 | no person-like local part | hard | 0 | PASS |
| 7 | role word in the local part | soft | 3532 | REVIEW |
| 8 | receivables-looking local part graded invoicing/AP | soft | 37 | REVIEW |
| 9 | shared government domain: page or quote names the body | soft | 3 | REVIEW |
| 10 | regional token of a multinational on a differently-located body | soft | 0 | PASS |
| 11 | quote contains the address | hard | 0 | PASS |
| 11b | quote shows the label next to the address (referee saw the address on the page) | soft | 0 | PASS |
| 12 | evidence page on the organisation's domain (or its site) | soft | 3732 | REVIEW |
| 13 | email_type label matches grade | hard | 0 | PASS |
| 14 | DMARC / SPF / provider columns filled | soft | 1 | REVIEW |
| 15 | tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m) | soft | 0 | PASS |
| 16 | vendor named and Canada proof present | hard | 0 | PASS |
| 17 | Canada proof is a source field or the vendor's site (never a name) | soft | 0 | PASS |
| 18 | record link present for dated-record tiers | soft | 0 | PASS |
| 19 | buyer name is a name (not a domain or a page title) | soft | 22946 | REVIEW |
| 20 | legal name is not a fragment or a platform copyright | soft | 62 | REVIEW |
| 21 | one row per mailbox | hard | 0 | PASS |
| 22 | one row per organisation name (same name twice) | soft | 7 | REVIEW |
| 23 | one row per site domain (two rows, different mailboxes, same domain) | soft | 60 | REVIEW |
| 24 | no blank cell | hard | 0 | PASS |
| 25 | jurisdiction vs mailbox top-level domain | soft | 41 | REVIEW |
| 26 | currency filled when a value is filled | soft | 46 | REVIEW |

## Examples of flagged rows (first 12 per check)
- **4b mail server not yet checked (row newer than the last DNS pass)**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:91 Cleveland State University | csu.ohio.edu
    - P01_GOLD_active_relationship_invoicing_AP_email:161 Department of Homeland Security | dhs.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:224 BRITISH COUNCIL(THE) | sutton.gov.uk
    - P01_GOLD_active_relationship_invoicing_AP_email:237 BANK OF ENGLAND | bankofengland.co.uk
    - P01_GOLD_active_relationship_invoicing_AP_email:248 Utilities Kingston | kingston.gov.uk
    - P01_GOLD_active_relationship_invoicing_AP_email:370 NATO Joint Warfare Centre (Stavanger) | jwc.nato.int
    - P01_GOLD_active_relationship_invoicing_AP_email:404 Debiopharm International SA | debiopharm.com
    - P01_GOLD_active_relationship_invoicing_AP_email:425 Max-Planck-Gesellschaft zur Förderung de | gv.mpg.de
    - P01_GOLD_active_relationship_invoicing_AP_email:456 The Clorox Company of Canada Ltd. | uberfreight.com
    - P01_GOLD_active_relationship_invoicing_AP_email:495 New York State Energy Research and Devel | nyserda.ny.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:550 BANCOLOMBIA S.A. | bancolombia.com.co
    - P01_GOLD_active_relationship_invoicing_AP_email:554 Indiana Department of Transportation | health.in.gov
- **7 role word in the local part**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:16 Cameco Corporation | ap_cameco@cameco.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:43 New Relic | ap_ireland@newrelic.com
    - P01_GOLD_active_relationship_invoicing_AP_email:276 Town of Oakville | ap_inquiries@oakville.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:302 Miami-Dade County (business unit CU05010 | invsubp@miamidade.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:391 BELL TEXTRON INC | APBell@textron.com
    - P02_active_relationship_finance_accounting_email:7 Agriculture and Agri-Food Canada | directdeposit.depotdirect@canada.ca
    - P02_active_relationship_finance_accounting_email:13 Crown-Indigenous Relations and Northern  | depotdirect-directdeposit@sac-isc.gc.ca
    - P02_active_relationship_finance_accounting_email:14 Department of Justice Canada | mdv_dpf@justice.gc.ca
    - P02_active_relationship_finance_accounting_email:18 Health Canada | hc.direct.deposit.requests-demande.de.depot.direct.sc@canada.ca
    - P02_active_relationship_finance_accounting_email:19 Innovation, Science and Economic Develop | ifmscustomer-clientsifm@ised-isde.gc.ca
    - P02_active_relationship_finance_accounting_email:21 National Defence | ddenrol-inscriredd@forces.gc.ca
    - P02_active_relationship_finance_accounting_email:29 Social Sciences and Humanities Research  | directdeposit-depotdirect@crsh-sshrc.gc.ca
- **8 receivables-looking local part graded invoicing/AP**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:4 Texas Tech University | payment.strategies@ttu.edu
    - P01_GOLD_active_relationship_invoicing_AP_email:39 Environment and Climate Change Canada | renseignement-paiements-payments-inquiry@ec.gc.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:215 County of Minburn No. 27 | payments@minburncounty.ab.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:584 TMX Group Limited | payments@tmx.com
    - P05_likely_active_awarded_12_36_months_any_email:27 Martensville | payments@martensville.ca
    - P06_client_listing_invoicing_AP_email:28 University of Bath | payments@bath.ac.uk
    - P06_client_listing_invoicing_AP_email:70 teamviewer.com | payments@teamviewer.com
    - P06_client_listing_invoicing_AP_email:148 Blomidon Nurseries (1970) Limited | payments@blomidonnurseries.com
    - P10_linked_from_vendor_site_any_email:13 gov.scot | online_payments@gov.scot
    - P10_linked_from_vendor_site_any_email:31 WeirFoulds LLP | payments@weirfoulds.com
    - P10_linked_from_vendor_site_any_email:39 bcica.org | payments@bcica.org
    - P11_any_relationship_email_not_yet_confirmed:23 His Majesty's Revenue and Customs (HMRC) | payments.team@hmrc.gov.uk
- **9 shared government domain: page or quote names the body**
    - P01_GOLD_active_relationship_invoicing_AP_email:43 Canadian Space Agency | invoicing.csa-asc.facturation@canada.ca ← https://www.canada.ca/en/public-services-procurement/services/payments-to-from-g
    - P07_client_listing_finance_or_purchasing_email:25 transportation.ky.gov | finance.crcgroup@ky.gov ← https://finance.ky.gov/eProcurement/Pages/doing-business-with-the-commonwealth.a
    - P13_inferred_relationship_no_record_own_email_part1_of_18:544 Landlord and Tenant Board | ltbpayments@ontario.ca ← https://tribunalsontario.ca/ltb/contact/
- **12 evidence page on the organisation's domain (or its site)**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:18 Motorola Solutions, Inc | recepcionfacturas@motorolasolutions.com on web.archive.org (site motorolasolutions.com)
    - P01_GOLD_active_relationship_invoicing_AP_email:2 Department of Defence | invoices@defence.gov.au on web.archive.org (site defence.gov.au)
    - P01_GOLD_active_relationship_invoicing_AP_email:3 Department of Industry, Science and Reso | einvoicingqueries@industry.gov.au on directory.peppol.eu (site industry.gov.au)
    - P01_GOLD_active_relationship_invoicing_AP_email:51 Natural Sciences and Engineering Researc | payables@nserc-crsng.gc.ca on nserc-crsng.canada.ca (site nserc-crsng.gc.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:66 Ville de Montréal | facture@montreal.ca on ville.montreal.qc.ca (site montreal.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:95 Ville de Farnham | comptespayables@ville.farnham.qc.ca on web.archive.org (site ville.farnham.qc.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:114 UK Atomic Energy Authority | finance@uk-atomic-energy.org.uk on assets.publishing.service.gov.uk (site gov.uk)
    - P01_GOLD_active_relationship_invoicing_AP_email:126 City of Chestermere | city.ap@chestermere.ca on thecityofchestermere.ca (site chestermere.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:132 Newfoundland and Labrador Liquor Corpora | Accounts.Payable@nlliquor.com on nlliquorcorp.com (site nlliquor.com)
    - P01_GOLD_active_relationship_invoicing_AP_email:134 The Ottawa Hospital | tohaccountspayable@toh.ca on ottawahospital.on.ca (site toh.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:162 Department of Foreign Affairs and Trade | dfat.e-invoicing.prod@dfat.gov.au on directory.peppol.eu (site dfat.gov.au)
    - P01_GOLD_active_relationship_invoicing_AP_email:192 HM Land Registry | apinvoices@landregistry.gov.uk on assets.publishing.service.gov.uk (site gov.uk)
- **14 DMARC / SPF / provider columns filled**
    - P13_inferred_relationship_no_record_own_email_part4_of_18:2600 GROUPE ERGO RESSOURCES INC. | not checked yet | not checked yet | not checked
- **19 buyer name is a name (not a domain or a page title)**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:33 ovs.com | ovs.com
    - P01_GOLD_active_relationship_invoicing_AP_email:450 capreit.ca | capreit.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:527 msvu.ca | msvu.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:553 bcib.ca | bcib.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:606 slrd.bc.ca | slrd.bc.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:624 corporate.exxonmobil.com | corporate.exxonmobil.com
    - P02_active_relationship_finance_accounting_email:308 healthpartners.ca | healthpartners.ca
    - P02_active_relationship_finance_accounting_email:314 osoyoos.ca | osoyoos.ca
    - P02_active_relationship_finance_accounting_email:382 werklundcentre.ca | werklundcentre.ca
    - P02_active_relationship_finance_accounting_email:386 ccib.ca | ccib.ca
    - P02_active_relationship_finance_accounting_email:390 OneChurch.To | OneChurch.To
    - P02_active_relationship_finance_accounting_email:397 apega.ca | apega.ca
- **20 legal name is not a fragment or a platform copyright**
    - P03_active_relationship_purchasing_email:195 onsemi | onsemi (label per Wikidata Q1671509, official website on the organisat
    - P04_active_relationship_general_email:111 Ministère de la Culture et des Communica | ministère de la Culture et des Communications (label per Wikidata Q331
    - P04_active_relationship_general_email:156 Ministère de la Cybersécurité et du Numé | ministère de la Cybersécurité et du Numérique (label per Wikidata Q110
    - P06T_active_service_seen_on_buyer_site_other_email:379 Uppdoo | uppdoo Inc. (as registered: Corporations Canada (open data), corporati
    - P06T_active_service_seen_on_buyer_site_other_email:1073 MyHealth Inc | myhealth inc. (as registered: Canada's Business Registries, CC 3660222
    - P06T_active_service_seen_on_buyer_site_other_email:1243 do+dare undie co. | do+dare undie co. (label per Wikidata Q141143888, official website on 
    - P06T_active_service_seen_on_buyer_site_other_email:1406 de Montigny Contemporain | de Montigny Contemporain (label per Wikidata Q139820434, official webs
    - P07_client_listing_finance_or_purchasing_email:82 lepointdevente.com | lepointdevente.com (recipient legal name in the federal grants & contr
    - P08_client_listing_general_email:2051 Christian Life Community | Christian Life Community (stated on https://www.christianlifecommunity
    - P10_linked_from_vendor_site_any_email:1502 Digify SEO Company | digify seo company Incorporated (as registered: Corporations Canada (o
    - P13_inferred_relationship_no_record_own_email_part11_of_18:2548 Mon-Proprio.ca Inc | mon-proprio.ca inc. (as registered: Canada's Business Registries, QC 1
    - P13_inferred_relationship_no_record_own_email_part15_of_18:1331 COD3 Corporation | cod3 corporation (as registered: Canada's Business Registries, CC 1190
- **22 one row per organisation name (same name twice)**
    - P01_GOLD_active_relationship_invoicing_AP_email:155 MRC de Manicouagan | 2 rows, same mail domain: mrcmanicouagan.qc.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:438 City of Kamloops | 2 rows, same mail domain: kamloops.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:552 Enbridge Inc. | 2 rows, same mail domain: enbridge.com
    - P04_active_relationship_general_email:319 Cégep de Victoriaville. | 2 rows, same mail domain: cegepvicto.ca
    - P05_likely_active_awarded_12_36_months_any_email:5 Brandon University | 2 rows, same mail domain: brandonu.ca
    - P06T_active_service_seen_on_buyer_site_other_email:78 City of Dawson | 2 rows, same mail domain: cityofdawson.ca
    - P06T_active_service_seen_on_buyer_site_other_email:1886 Town of Lincoln | 2 rows, same mail domain: lincoln.ca
- **23 one row per site domain (two rows, different mailboxes, same domain)**
    - P01_GOLD_active_relationship_invoicing_AP_email:2 Department of Defence | defence.gov.au: 2 rows, invoices@defence.gov.au; peppol.einvoices@defence.gov.au
    - P01_GOLD_active_relationship_invoicing_AP_email:27 University of Toronto | utoronto.ca: 2 rows, ap.fsd@utoronto.ca; fmdinvoice.utsc@utoronto.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:57 Ville de Gatineau | gatineau.ca: 2 rows, gatineau.factures@gatineau.ca; idgatineau@gatineau.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:66 Ville de Montréal | montreal.ca: 2 rows, facture@montreal.ca; comptesapayer@montreal.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:82 Ville de Laval | laval.ca: 3 rows, comptespayables@laval.ca; lavaleconomique@laval.ca; info@laval.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:115 Texas Department of Insurance | texas.gov: 7 rows, invoices@tdi.texas.gov; ap@ers.texas.gov; ap@tsl.texas.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:128 University of Ottawa | uottawa.ca: 2 rows, payables@uottawa.ca; info@emba.uottawa.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:195 Oregon Department of Transportation | oregon.gov: 3 rows, opoinvoiceinquiries@odot.oregon.gov; omdaccounts.payable@omd.oregon.gov; odf.accountspayable@oregon.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:198 Texas Tech University Health Sciences Ce | ttuhsc.edu: 2 rows, Accounts.Payable@ttuhsc.edu; accountspayableelp@ttuhsc.edu
    - P01_GOLD_active_relationship_invoicing_AP_email:234 Metrolinx | metrolinx.com: 2 rows, it.invoices@metrolinx.com; rti.invoices@metrolinx.com
    - P01_GOLD_active_relationship_invoicing_AP_email:259 Niagara Region | niagararegion.ca: 2 rows, constructioninvoices@niagararegion.ca; NRHCapitalWorks@niagararegion.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:354 Virginia State Police | virginia.gov: 5 rows, ap@vsp.virginia.gov; accountspayable@energy.virginia.gov; support@dhrm.virginia.gov
- **25 jurisdiction vs mailbox top-level domain**
    - P01_GOLD_active_relationship_invoicing_AP_email:248 Utilities Kingston | CA / kingston.gov.uk
    - P13_inferred_relationship_no_record_own_email_part11_of_18:11 AO Kaspersky Lab | CA / kaspersky.de
    - P13_inferred_relationship_no_record_own_email_part11_of_18:1057 lifelyhome.ca | CA / lifely.com.au
    - P13_inferred_relationship_no_record_own_email_part12_of_18:198 nakie.ca | CA / nakie.com.au
    - P13_inferred_relationship_no_record_own_email_part12_of_18:1218 opal-canada.ca | CA / opal.fr
    - P13_inferred_relationship_no_record_own_email_part12_of_18:1767 pccarx.ca | CA / pccarx.com.au
    - P13_inferred_relationship_no_record_own_email_part12_of_18:2434 practs.ca | CA / practs.de
    - P13_inferred_relationship_no_record_own_email_part13_of_18:805 Roka Harness Pty Ltd | CA / rokaharness.com.au
    - P13_inferred_relationship_no_record_own_email_part13_of_18:1973 Skin Cupid | CA / skincupid.co.uk
    - P13_inferred_relationship_no_record_own_email_part13_of_18:2170 Snowdonia Cheese Ltd | CA / snowdonia-cheese.co.uk
    - P13_inferred_relationship_no_record_own_email_part16_of_18:2641 Beckhoff Automation Ltd. | CA / beckhoff.de
    - P13_inferred_relationship_no_record_own_email_part17_of_18:871 Bernafon Canada | ON / bernafon.com.au
- **26 currency filled when a value is filled**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:23 RENTON SCHOOL DISTRICT #403 | 332345.13 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:442 Rectorado de la Universitat de València | 12698.25 (source field: PayableAmount)
    - P01_GOLD_active_relationship_invoicing_AP_email:454 BRINKS DE COLOMBIA S.A. | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:473 University of North Dakota | 145.850 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:502 BELLEVUE, CITY OF | 35488873.2 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:510 UNIVERSITY PLACE SCHOOL DISTRICT #83 | 685477.9 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:529 North Dakota State University | 35.000 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:534 BELLEVUE SCHOOL DISTRICT #405 | 5395.88 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:540 SNOQUALMIE VALLEY SCHOOL DISTRICT #410 | 23980.42 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:547 MARYLAND STADIUM AUTHORITY | 251569.05 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:550 BANCOLOMBIA S.A. | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:561 ECOPETROL S A | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)

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
- P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email: 18
- P01T_active_service_seen_on_buyer_site_invoicing_AP_email: 92
- P01_GOLD_active_relationship_invoicing_AP_email: 624
- P02_active_relationship_finance_accounting_email: 404
- P03_active_relationship_purchasing_email: 208
- P04_active_relationship_general_email: 1566
- P05_likely_active_awarded_12_36_months_any_email: 384
- P06M_member_or_regulated_payer_of_canadian_body_other_email: 168
- P06T_active_service_seen_on_buyer_site_other_email: 2440
- P06_client_listing_invoicing_AP_email: 166
- P07_client_listing_finance_or_purchasing_email: 252
- P08_client_listing_general_email: 3039
- P09_older_contract_or_payment_any_email: 381
- P10_linked_from_vendor_site_any_email: 2596
- P11_any_relationship_email_not_yet_confirmed: 474
- P12_weaker_relationship_within_5_years_own_email: 19
- P13_inferred_relationship_no_record_own_email: 50807

## Field fill across all delivered rows (value present, not `not_published`)
- buyer_website: 63638 (100.0%)
- vendor_website: 62163 (97.7%)
- vendor_address: 61180 (96.1%)
- vendor_phone: 57138 (89.8%)
- buyer_logo_url: 53976 (84.8%)
- vendor_bn9: 53135 (83.5%)
- vendor_logo_url: 52373 (82.3%)
- buyer_phone: 49818 (78.3%)
- buyer_address: 48223 (75.8%)
- buyer_legal_name_as_published: 33611 (52.8%)
- buyer_bn_as_published: 14885 (23.4%)
- contract_link: 12831 (20.2%)
- vendor_legal_name: 9677 (15.2%)
- vendor_registry_id: 8260 (13.0%)
- vendor_incorporation_date: 8249 (13.0%)
- award_date: 6499 (10.2%)
- vendor_neq: 5025 (7.9%)
- vendor_emails: 4883 (7.7%)
- ap_phone: 2670 (4.2%)
- contract_value: 2375 (3.7%)
- invoice_mailing_address: 2198 (3.5%)
- invoicing_requirements: 2135 (3.4%)
- payment_terms_as_published: 2032 (3.2%)
- end_date: 1769 (2.8%)
- invoice_portal_url: 1766 (2.8%)
- po_required_as_published: 1492 (2.3%)
- ap_contact_name_as_published: 930 (1.5%)

## Canada-proof families
- other: 47269; source field: 16369

## Buyer types
- organisation (type not stated in the record): 33175
- company (private sector): 10818
- non-profit / association / cultural body: 7187
- company (private sector) (from the organisation's name / web domain): 4044
- municipality / local government: 1337
- government ministry / agency: 1216
- municipality / local government (from the organisation's name / web domain): 1062
- hospital / health authority: 929
- non-profit / association / cultural body (from the organisation's name / web domain): 901
- university / college: 579
- utility / public corporation: 485
- university / college (from the organisation's name / web domain): 444
- hospital / health authority (from the organisation's name / web domain): 341
- transport / transit authority: 207
- school board / school district: 176
- First Nation / Indigenous government: 166
- government ministry / agency (from the organisation's name / web domain): 150
- religious organisation (from the organisation's name / web domain): 142
- utility / public corporation (from the organisation's name / web domain): 97
- transport / transit authority (from the organisation's name / web domain): 61
- First Nation / Indigenous government (from the organisation's name / web domain): 46
- US government body (federal, state or local): 29
- school board / school district (from the organisation's name / web domain): 20
- library (from the organisation's name / web domain): 15
- US city / county / local government: 11

## DMARC posture of the delivered mailboxes
- v=DMARC1; p=none (monitor only, no enforcement): 26440
- no DMARC record: 21275
- p=quarantine: 10439
- p=reject: 5417
- invalid DMARC record: 59
- DNS lookup failed: 7
- not checked yet: 1
