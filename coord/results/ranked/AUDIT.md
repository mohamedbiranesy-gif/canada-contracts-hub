# Deep audit — 63579 delivered rows in 17 packages (28 files), 2026-11-08

Result: **PASS** — 11 hard checks, 17 soft checks; hard failures: 0. Every flagged row is listed in `audit_flags.csv` with its reasons.

| # | check | kind | rows flagged | verdict |
|---|---|---|---|---|
| 1 | header: identical columns in every file (106 since 2026-11-06) | hard | 0 | PASS |
| 2 | mailbox syntax | hard | 0 | PASS |
| 3 | mailbox referee-confirmed (all but P11) | hard | 0 | PASS |
| 4 | mail server (MX or A) on the mailbox domain | hard | 0 | PASS |
| 4b | mail server not yet checked (row newer than the last DNS pass) | soft | 1 | REVIEW |
| 5 | no webmail domain | hard | 0 | PASS |
| 6 | no person-like local part | hard | 0 | PASS |
| 7 | role word in the local part | soft | 3534 | REVIEW |
| 8 | receivables-looking local part graded invoicing/AP | soft | 35 | REVIEW |
| 9 | shared government domain: page or quote names the body | soft | 2 | REVIEW |
| 10 | regional token of a multinational on a differently-located body | soft | 0 | PASS |
| 11 | quote contains the address | hard | 0 | PASS |
| 11b | quote shows the label next to the address (referee saw the address on the page) | soft | 0 | PASS |
| 12 | evidence page on the organisation's domain (or its site) | soft | 3733 | REVIEW |
| 13 | email_type label matches grade | hard | 0 | PASS |
| 14 | DMARC / SPF / provider columns filled | soft | 0 | PASS |
| 15 | tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m) | soft | 0 | PASS |
| 16 | vendor named and Canada proof present | hard | 0 | PASS |
| 17 | Canada proof is a source field or the vendor's site (never a name) | soft | 0 | PASS |
| 18 | record link present for dated-record tiers | soft | 0 | PASS |
| 19 | buyer name is a name (not a domain or a page title) | soft | 25581 | REVIEW |
| 20 | legal name is not a fragment or a platform copyright | soft | 26 | REVIEW |
| 21 | one row per mailbox | hard | 0 | PASS |
| 22 | one row per organisation name (same name twice) | soft | 8 | REVIEW |
| 23 | one row per site domain (two rows, different mailboxes, same domain) | soft | 64 | REVIEW |
| 24 | no blank cell | hard | 0 | PASS |
| 25 | jurisdiction vs mailbox top-level domain | soft | 40 | REVIEW |
| 26 | currency filled when a value is filled | soft | 46 | REVIEW |

## Examples of flagged rows (first 12 per check)
- **4b mail server not yet checked (row newer than the last DNS pass)**
    - P13_inferred_relationship_no_record_own_email_part2_of_12:3053 Everest Services Ltd | everest.ca
- **7 role word in the local part**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:16 Cameco Corporation | ap_cameco@cameco.com
    - P01_GOLD_active_relationship_invoicing_AP_email:266 Town of Oakville | ap_inquiries@oakville.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:292 Miami-Dade County (business unit CU05010 | invsubp@miamidade.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:380 BELL TEXTRON INC | APBell@textron.com
    - P02_active_relationship_finance_accounting_email:7 Agriculture and Agri-Food Canada | directdeposit.depotdirect@canada.ca
    - P02_active_relationship_finance_accounting_email:13 Crown-Indigenous Relations and Northern  | depotdirect-directdeposit@sac-isc.gc.ca
    - P02_active_relationship_finance_accounting_email:14 Department of Justice Canada | mdv_dpf@justice.gc.ca
    - P02_active_relationship_finance_accounting_email:18 Health Canada | hc.direct.deposit.requests-demande.de.depot.direct.sc@canada.ca
    - P02_active_relationship_finance_accounting_email:19 Innovation, Science and Economic Develop | ifmscustomer-clientsifm@ised-isde.gc.ca
    - P02_active_relationship_finance_accounting_email:21 National Defence | ddenrol-inscriredd@forces.gc.ca
    - P02_active_relationship_finance_accounting_email:29 Social Sciences and Humanities Research  | directdeposit-depotdirect@crsh-sshrc.gc.ca
    - P02_active_relationship_finance_accounting_email:31 Veterans Affairs Canada | directdeposit-depotdirect@vac-acc.gc.ca
- **8 receivables-looking local part graded invoicing/AP**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:11 Empress | payments@villageofempress.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:4 Texas Tech University | payment.strategies@ttu.edu
    - P01_GOLD_active_relationship_invoicing_AP_email:38 Environment and Climate Change Canada | renseignement-paiements-payments-inquiry@ec.gc.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:468 Township of Georgian Bay | payments@gbtownship.ca
    - P05_likely_active_awarded_12_36_months_any_email:25 Martensville | payments@martensville.ca
    - P06_client_listing_invoicing_AP_email:27 University of Bath | payments@bath.ac.uk
    - P06_client_listing_invoicing_AP_email:69 Edith Cowan University | payments@teamviewer.com
    - P06_client_listing_invoicing_AP_email:143 Blomidon Nurseries (1970) Limited | payments@blomidonnurseries.com
    - P10_linked_from_vendor_site_any_email:12 Equality and Human Rights Commission | online_payments@gov.scot
    - P10_linked_from_vendor_site_any_email:29 WeirFoulds LLP | payments@weirfoulds.com
    - P10_linked_from_vendor_site_any_email:36 British Columbia Insulation Contractors  | payments@bcica.org
    - P13_inferred_relationship_no_record_own_email_part1_of_12:10 THE ROYAL CANADIAN COLLEGE OF ORGANISTS- | payment@rcco-ottawa.ca
- **9 shared government domain: page or quote names the body**
    - P01_GOLD_active_relationship_invoicing_AP_email:42 Canadian Space Agency | invoicing.csa-asc.facturation@canada.ca ← https://www.canada.ca/en/public-services-procurement/services/payments-to-from-g
    - P13_inferred_relationship_no_record_own_email_part1_of_12:542 Landlord and Tenant Board | ltbpayments@ontario.ca ← https://tribunalsontario.ca/ltb/contact/
- **12 evidence page on the organisation's domain (or its site)**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:18 Motorola Solutions, Inc | recepcionfacturas@motorolasolutions.com on web.archive.org (site motorolasolutions.com)
    - P01_GOLD_active_relationship_invoicing_AP_email:2 Department of Defence | peppol.einvoices@defence.gov.au on directory.peppol.eu (site defence.gov.au)
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
    - P01_GOLD_active_relationship_invoicing_AP_email:585 corporate.exxonmobil.com | corporate.exxonmobil.com
    - P04_active_relationship_general_email:1319 goodroads.ca | goodroads.ca
    - P04_active_relationship_general_email:1335 researchns.ca | researchns.ca
    - P04_active_relationship_general_email:1344 innovatebc.ca | innovatebc.ca
    - P04_active_relationship_general_email:1483 bcscholarshipsociety.ca | bcscholarshipsociety.ca
    - P04_active_relationship_general_email:1485 OneChurch.To | OneChurch.To
    - P04_active_relationship_general_email:1548 ernestines.ca | ernestines.ca
    - P04_active_relationship_general_email:1613 microsoft.com | microsoft.com
    - P06T_active_service_seen_on_buyer_site_other_email:43 pier21.ca | pier21.ca
    - P06T_active_service_seen_on_buyer_site_other_email:92 tafeqld.edu.au | tafeqld.edu.au
    - P06T_active_service_seen_on_buyer_site_other_email:127 pangrampangram.com | pangrampangram.com
    - P06T_active_service_seen_on_buyer_site_other_email:168 kaslosourdoughpasta.com | kaslosourdoughpasta.com
- **20 legal name is not a fragment or a platform copyright**
    - P04_active_relationship_general_email:117 Ministère de la Culture et des Communica | ministère de la Culture et des Communications (label per Wikidata Q331
    - P04_active_relationship_general_email:161 Ministère de la Cybersécurité et du Numé | ministère de la Cybersécurité et du Numérique (label per Wikidata Q110
    - P07_client_listing_finance_or_purchasing_email:81 lepointdevente.com | lepointdevente.com (recipient legal name in the federal grants & contr
    - P08_client_listing_general_email:1767 Harvard University | Harvard University (stated on https://crosslight.com.cn/wordpress/abou
    - P08_client_listing_general_email:2050 Christian Life Community | Christian Life Community (stated on https://www.christianlifecommunity
    - P10_linked_from_vendor_site_any_email:1601 University of Toronto | University of Toronto (stated on https://www.camp1.ca/wordpress/)
    - P13_inferred_relationship_no_record_own_email_part11_of_12:386 Fowler Dental | fowler dental (recipient legal name in the federal grants & contributi
    - P13_inferred_relationship_no_record_own_email_part11_of_12:914 Musée des communications et d'histoire d | musée des communications et d'histoire de Sutton (recipient legal name
    - P13_inferred_relationship_no_record_own_email_part11_of_12:1363 Whiprsnapr Brewing Company | whiprsnapr brewing co inc. (recipient legal name in the federal grants
    - P13_inferred_relationship_no_record_own_email_part11_of_12:1591 eSentire | eSentire Inc. (recipient legal name in the federal grants & contributi
    - P13_inferred_relationship_no_record_own_email_part11_of_12:3214 eyecandy SIGNS | eyecandy SIGNS INC. (recipient legal name in the federal grants & cont
    - P13_inferred_relationship_no_record_own_email_part11_of_12:3965 adHOME Creative Inc | adHOME Creative Inc. (recipient legal name in the federal grants & con
- **22 one row per organisation name (same name twice)**
    - P01_GOLD_active_relationship_invoicing_AP_email:154 MRC de Manicouagan | 2 rows, same mail domain: mrcmanicouagan.qc.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:350 Town of Lincoln | 2 rows, same mail domain: lincoln.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:421 City of Kamloops | 2 rows, same mail domain: kamloops.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:522 Enbridge Inc. | 2 rows, same mail domain: enbridge.com
    - P02_active_relationship_finance_accounting_email:321 Mount Saint Vincent University | 2 rows, same mail domain: msvu.ca
    - P04_active_relationship_general_email:330 Cégep de Victoriaville. | 2 rows, same mail domain: cegepvicto.ca
    - P05_likely_active_awarded_12_36_months_any_email:5 Brandon University | 2 rows, same mail domain: brandonu.ca
    - P06T_active_service_seen_on_buyer_site_other_email:65 City of Dawson | 2 rows, same mail domain: cityofdawson.ca
- **23 one row per site domain (two rows, different mailboxes, same domain)**
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
    - P01_GOLD_active_relationship_invoicing_AP_email:344 Virginia State Police | virginia.gov: 5 rows, ap@vsp.virginia.gov; accountspayable@energy.virginia.gov; support@dhrm.virginia.gov
- **25 jurisdiction vs mailbox top-level domain**
    - P13_inferred_relationship_no_record_own_email_part11_of_12:2639 Beckhoff Automation Ltd. | CA / beckhoff.de
    - P13_inferred_relationship_no_record_own_email_part11_of_12:3692 Bernafon Canada | ON / bernafon.com.au
    - P13_inferred_relationship_no_record_own_email_part12_of_12:1488 Déontologie : approche comparée FR / QC | CA / univ-droit.fr
    - P13_inferred_relationship_no_record_own_email_part12_of_12:1981 Shah's Halal Food | CA / shahshalalfood.co.uk
    - P13_inferred_relationship_no_record_own_email_part12_of_12:2040 Hochtief | CA / hochtief.de
    - P13_inferred_relationship_no_record_own_email_part12_of_12:2560 Canada at the 2013 World Aquatics Champi | CA / dsv.de
    - P13_inferred_relationship_no_record_own_email_part12_of_12:2589 Pro Seniore | CA / pro-seniore.de
    - P13_inferred_relationship_no_record_own_email_part12_of_12:2750 Marienhaus | CA / marienhaus.de
    - P13_inferred_relationship_no_record_own_email_part12_of_12:2764 Singa | CA / singa.fr
    - P13_inferred_relationship_no_record_own_email_part12_of_12:2777 SRH Holding | CA / srh.de
    - P13_inferred_relationship_no_record_own_email_part12_of_12:2787 Sparkassen-Finanzgruppe | CA / dsgv.de
    - P13_inferred_relationship_no_record_own_email_part12_of_12:2798 Stihl | CA / stihl.de
- **26 currency filled when a value is filled**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:22 RENTON SCHOOL DISTRICT #403 | 332345.13 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:425 Rectorado de la Universitat de València | 12698.25 (source field: PayableAmount)
    - P01_GOLD_active_relationship_invoicing_AP_email:436 BRINKS DE COLOMBIA S.A. | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:455 University of North Dakota | 145.850 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:477 BELLEVUE, CITY OF | 35488873.2 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:485 UNIVERSITY PLACE SCHOOL DISTRICT #83 | 685477.9 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:502 North Dakota State University | 35.000 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:507 BELLEVUE SCHOOL DISTRICT #405 | 5395.88 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:512 SNOQUALMIE VALLEY SCHOOL DISTRICT #410 | 23980.42 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:517 MARYLAND STADIUM AUTHORITY | 251569.05 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:530 ECOPETROL S A | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:559 Fundación para la Investigación del Hosp | 1236.23 (source field: PayableAmount)

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
- P01T_active_service_seen_on_buyer_site_invoicing_AP_email: 91
- P01_GOLD_active_relationship_invoicing_AP_email: 585
- P02_active_relationship_finance_accounting_email: 366
- P03_active_relationship_purchasing_email: 224
- P04_active_relationship_general_email: 1615
- P05_likely_active_awarded_12_36_months_any_email: 378
- P06M_member_or_regulated_payer_of_canadian_body_other_email: 167
- P06T_active_service_seen_on_buyer_site_other_email: 2429
- P06_client_listing_invoicing_AP_email: 160
- P07_client_listing_finance_or_purchasing_email: 246
- P08_client_listing_general_email: 3038
- P09_older_contract_or_payment_any_email: 369
- P10_linked_from_vendor_site_any_email: 2587
- P11_any_relationship_email_not_yet_confirmed: 497
- P12_weaker_relationship_within_5_years_own_email: 21
- P13_inferred_relationship_no_record_own_email: 50786

## Field fill across all delivered rows (value present, not `not_published`)
- buyer_website: 63579 (100.0%)
- vendor_address: 60527 (95.2%)
- vendor_website: 59508 (93.6%)
- vendor_phone: 56168 (88.3%)
- vendor_bn9: 52836 (83.1%)
- buyer_phone: 48355 (76.1%)
- buyer_logo_url: 48253 (75.9%)
- buyer_address: 47123 (74.1%)
- buyer_legal_name_as_published: 23300 (36.6%)
- contract_link: 12793 (20.1%)
- buyer_bn_as_published: 10396 (16.4%)
- vendor_legal_name: 10275 (16.2%)
- vendor_registry_id: 7551 (11.9%)
- vendor_incorporation_date: 7339 (11.5%)
- vendor_logo_url: 7170 (11.3%)
- award_date: 6482 (10.2%)
- vendor_neq: 4595 (7.2%)
- vendor_emails: 4345 (6.8%)
- ap_phone: 2597 (4.1%)
- contract_value: 2334 (3.7%)
- invoice_mailing_address: 2105 (3.3%)
- end_date: 1757 (2.8%)
- invoicing_requirements: 1587 (2.5%)
- invoice_portal_url: 661 (1.0%)
- po_required_as_published: 466 (0.7%)
- payment_terms_as_published: 376 (0.6%)
- ap_contact_name_as_published: 174 (0.3%)

## Canada-proof families
- other: 47251; source field: 16328

## Buyer types
- organisation (type not stated in the record): 35818
- company (private sector): 9781
- non-profit / association / cultural body: 6958
- company (private sector) (from the organisation's name / web domain): 2185
- municipality / local government: 1447
- government ministry / agency: 1210
- municipality / local government (from the organisation's name / web domain): 1060
- non-profit / association / cultural body (from the organisation's name / web domain): 923
- hospital / health authority: 835
- university / college (from the organisation's name / web domain): 762
- university / college: 561
- utility / public corporation: 464
- hospital / health authority (from the organisation's name / web domain): 404
- transport / transit authority: 198
- school board / school district: 197
- First Nation / Indigenous government: 167
- government ministry / agency (from the organisation's name / web domain): 154
- religious organisation (from the organisation's name / web domain): 144
- utility / public corporation (from the organisation's name / web domain): 111
- transport / transit authority (from the organisation's name / web domain): 69
- First Nation / Indigenous government (from the organisation's name / web domain): 43
- US government body (federal, state or local): 29
- school board / school district (from the organisation's name / web domain): 26
- library (from the organisation's name / web domain): 22
- US city / county / local government: 11

## DMARC posture of the delivered mailboxes
- v=DMARC1; p=none (monitor only, no enforcement): 26421
- no DMARC record: 21266
- p=quarantine: 10429
- p=reject: 5394
- invalid DMARC record: 59
- DNS lookup failed: 10
