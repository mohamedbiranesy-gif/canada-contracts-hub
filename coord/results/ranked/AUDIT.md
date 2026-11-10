# Deep audit — 73601 delivered rows in 18 packages (36 files), 2026-11-10

Result: **FAIL** — 11 hard checks, 17 soft checks; hard failures: 1. Every flagged row is listed in `audit_flags.csv` with its reasons.

| # | check | kind | rows flagged | verdict |
|---|---|---|---|---|
| 1 | header: identical columns in every file (106 since 2026-11-06) | hard | 0 | PASS |
| 2 | mailbox syntax | hard | 0 | PASS |
| 3 | mailbox referee-confirmed (all but P11) | hard | 0 | PASS |
| 4 | mail server (MX or A) on the mailbox domain | hard | 0 | PASS |
| 4b | mail server not yet checked (row newer than the last DNS pass) | soft | 8025 | REVIEW |
| 5 | no webmail domain | hard | 1 | FAIL |
| 6 | no person-like local part | hard | 0 | PASS |
| 7 | role word in the local part | soft | 4346 | REVIEW |
| 8 | receivables-looking local part graded invoicing/AP | soft | 39 | REVIEW |
| 9 | shared government domain: page or quote names the body | soft | 3 | REVIEW |
| 10 | regional token of a multinational on a differently-located body | soft | 0 | PASS |
| 11 | quote contains the address | hard | 0 | PASS |
| 11b | quote shows the label next to the address (referee saw the address on the page) | soft | 0 | PASS |
| 12 | evidence page on the organisation's domain (or its site) | soft | 4089 | REVIEW |
| 13 | email_type label matches grade | hard | 0 | PASS |
| 14 | DMARC / SPF / provider columns filled | soft | 0 | PASS |
| 15 | tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m) | soft | 0 | PASS |
| 16 | vendor named and Canada proof present | hard | 0 | PASS |
| 17 | Canada proof is a source field or the vendor's site (never a name) | soft | 0 | PASS |
| 18 | record link present for dated-record tiers | soft | 0 | PASS |
| 19 | buyer name is a name (not a domain or a page title) | soft | 6495 | REVIEW |
| 20 | legal name is not a fragment or a platform copyright | soft | 2541 | REVIEW |
| 21 | one row per mailbox | hard | 0 | PASS |
| 22 | one row per organisation name (same name twice) | soft | 9 | REVIEW |
| 23 | one row per site domain (two rows, different mailboxes, same domain) | soft | 59 | REVIEW |
| 24 | no blank cell | hard | 0 | PASS |
| 25 | jurisdiction vs mailbox top-level domain | soft | 40 | REVIEW |
| 26 | currency filled when a value is filled | soft | 46 | REVIEW |

## Examples of flagged rows (first 12 per check)
- **4b mail server not yet checked (row newer than the last DNS pass)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:36 Constructions Fabmec inc. | fabmec.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:94 Cleveland State University | csu.ohio.edu
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:100 Space Credibility | credibility.space
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:105 Infinite Cables US | infinitecables.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:111 Calgary Coin Gallery | calgarycoin.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:137 FNCIAS | fncias.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:142 De Grandpré Chait | dgchait.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:146 Musée canadien de l’histoire | museedelhistoire.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:159 Bubble Technology Industries | bubbletech.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:161 Department of Homeland Security | dhs.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:224 BRITISH COUNCIL(THE) | sutton.gov.uk
    - P01_GOLD_active_relationship_invoicing_AP_email:237 BANK OF ENGLAND | bankofengland.co.uk
- **5 no webmail domain**
    - P08_client_listing_general_email_part3_of_3:2270 Palmer College of Chiropractic | palmerfinancialaidmaincampus@live.palmer.edu
- **7 role word in the local part**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:19 Cameco Corporation | ap_cameco@cameco.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:46 New Relic | ap_ireland@newrelic.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:120 Keyera | ap_inquiries@keyera.com
    - P01_GOLD_active_relationship_invoicing_AP_email:276 Town of Oakville | ap_inquiries@oakville.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:301 University of Saskatchewan | connectionpoint@usask.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:303 Miami-Dade County (business unit CU05010 | invsubp@miamidade.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:391 BELL TEXTRON INC | APBell@textron.com
    - P02_active_relationship_finance_accounting_email:7 Agriculture and Agri-Food Canada | directdeposit.depotdirect@canada.ca
    - P02_active_relationship_finance_accounting_email:13 Crown-Indigenous Relations and Northern  | depotdirect-directdeposit@sac-isc.gc.ca
    - P02_active_relationship_finance_accounting_email:14 Department of Justice Canada | mdv_dpf@justice.gc.ca
    - P02_active_relationship_finance_accounting_email:18 Health Canada | hc.direct.deposit.requests-demande.de.depot.direct.sc@canada.ca
    - P02_active_relationship_finance_accounting_email:19 Innovation, Science and Economic Develop | ifmscustomer-clientsifm@ised-isde.gc.ca
- **8 receivables-looking local part graded invoicing/AP**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:19 About | payment@birchfumigators.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:7 Texas Tech University | payment.strategies@ttu.edu
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:96 Furbaby Pet Care Saskatoon | payments@furbabysk.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:106 Lerners Lawyers | payments@lerners.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:111 Calgary Coin Gallery | payment@calgarycoin.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:125 WeirFoulds LLP | payments@weirfoulds.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:126 PSM Law | payment@psmlaw.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:163 Whitefish River First Nation | payments@whitefishriver.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:39 Environment and Climate Change Canada | renseignement-paiements-payments-inquiry@ec.gc.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:215 County of Minburn No. 27 | payments@minburncounty.ab.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:586 TMX Group Limited | payments@tmx.com
    - P05_likely_active_awarded_12_36_months_any_email:27 Martensville | payments@martensville.ca
- **9 shared government domain: page or quote names the body**
    - P01_GOLD_active_relationship_invoicing_AP_email:43 Canadian Space Agency | invoicing.csa-asc.facturation@canada.ca ← https://www.canada.ca/en/public-services-procurement/services/payments-to-from-g
    - P07_client_listing_finance_or_purchasing_email:20 transportation.ky.gov | finance.crcgroup@ky.gov ← https://finance.ky.gov/eProcurement/Pages/doing-business-with-the-commonwealth.a
    - P13_inferred_relationship_no_record_own_email_part1_of_4:168 Landlord and Tenant Board | ltbpayments@ontario.ca ← https://tribunalsontario.ca/ltb/contact/
- **12 evidence page on the organisation's domain (or its site)**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:21 Motorola Solutions | recepcionfacturas@motorolasolutions.com on web.archive.org (site motorolasolutions.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:141 Outil Mag | factures@outilmag.com on outilmag.qc.ca (site outilmag.com)
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
- **19 buyer name is a name (not a domain or a page title)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:19 About | About
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:36 ovs.com | ovs.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:101 cstx.gov | cstx.gov
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:109 mmcorp.ca | mmcorp.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:119 cpaquebec.ca | cpaquebec.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:122 ahbl.ca | ahbl.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:131 gatech.edu | gatech.edu
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:132 wrm.ca | wrm.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:138 fswe.ca | fswe.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:173 ingrammicro.com | ingrammicro.com
    - P01_GOLD_active_relationship_invoicing_AP_email:555 bcib.ca | bcib.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:626 corporate.exxonmobil.com | corporate.exxonmobil.com
- **20 legal name is not a fragment or a platform copyright**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:22 Reliance | Reliance Developments Ltd (the City of Vancouver's open data list of b
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:29 Ascenseurs Design Inc. | Ascenseurs Design Inc. (the Régie du bâtiment du Québec's list of acti
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:31 BGIS O&M Solutions inc. | BGIS O&M Solutions inc. (the Régie du bâtiment du Québec's list of act
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:33 Construction et Rénovation Denis Inc. | Construction et Rénovation Denis Inc. (the Régie du bâtiment du Québec
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:34 Construction Finition inc. | Construction Finition inc. (the Régie du bâtiment du Québec's list of 
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:35 Dion électrique inc. | Dion électrique inc. (the Régie du bâtiment du Québec's list of active
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:36 Constructions Fabmec inc. | Constructions Fabmec inc. (the Régie du bâtiment du Québec's list of a
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:37 Groupe Nordfab inc. | Groupe Nordfab inc. (the Régie du bâtiment du Québec's list of active 
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:38 JBPA Holdings Ltd. | JBPA Holdings Ltd. (the Régie du bâtiment du Québec's list of active l
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:40 2900297 Canada inc. | 2900297 Canada inc. (the Régie du bâtiment du Québec's list of active 
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:41 Ottawa Compressor Services inc. | Ottawa Compressor Services inc. (the Régie du bâtiment du Québec's lis
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:42 Plomberie Richard Jubinville inc. | Plomberie Richard Jubinville inc. (the Régie du bâtiment du Québec's l
- **22 one row per organisation name (same name twice)**
    - P01_GOLD_active_relationship_invoicing_AP_email:26 University of Lethbridge | 2 rows, same mail domain: uleth.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:155 MRC de Manicouagan | 2 rows, same mail domain: mrcmanicouagan.qc.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:234 Metrolinx | 2 rows, same mail domain: metrolinx.com
    - P01_GOLD_active_relationship_invoicing_AP_email:439 City of Kamloops | 2 rows, same mail domain: kamloops.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:554 Enbridge Inc. | 2 rows, same mail domain: enbridge.com
    - P04_active_relationship_general_email:321 Cégep de Victoriaville. | 2 rows, same mail domain: cegepvicto.ca
    - P05_likely_active_awarded_12_36_months_any_email:5 Brandon University | 2 rows, same mail domain: brandonu.ca
    - P06T_active_service_seen_on_buyer_site_other_email_part1_of_5:2210 Town of Lincoln | 2 rows, same mail domain: lincoln.ca
    - P08_client_listing_general_email_part2_of_3:846 SIC MARKING | 2 rows, same mail domain: sic-marking.com
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
    - P01_GOLD_active_relationship_invoicing_AP_email:355 Virginia State Police | virginia.gov: 5 rows, ap@vsp.virginia.gov; accountspayable@energy.virginia.gov; support@dhrm.virginia.gov
- **25 jurisdiction vs mailbox top-level domain**
    - P01_GOLD_active_relationship_invoicing_AP_email:248 Utilities Kingston | CA / kingston.gov.uk
    - P13_inferred_relationship_no_record_own_email_part1_of_4:143 Rheinmetall AG | CA / rheinmetall.com.au
    - P13_inferred_relationship_no_record_own_email_part1_of_4:151 Westpac | CA / westpac.com.au
    - P13_inferred_relationship_no_record_own_email_part1_of_4:170 United States Postal Service | CA / usps.gov
    - P13_inferred_relationship_no_record_own_email_part1_of_4:309 Randstad Deutschland | CA / randstad.de
    - P13_inferred_relationship_no_record_own_email_part1_of_4:562 LA MAISON DES JEUNES DE PLESSISVILLE INC | QC / lycos.fr
    - P13_inferred_relationship_no_record_own_email_part1_of_4:801 The Redeemed Christian Church of God Lov | SK / loveassembly.co.uk
    - P13_inferred_relationship_no_record_own_email_part1_of_4:1321 mgmarketing.fr | QC / mgmarketing.fr
    - P13_inferred_relationship_no_record_own_email_part2_of_4:817 KNDS | CA / knds.de
    - P13_inferred_relationship_no_record_own_email_part2_of_4:829 The Warehouse Group | CA / thewarehousegroup.co.nz
    - P13_inferred_relationship_no_record_own_email_part2_of_4:2495 akelius.ca | CA / akelius.fr
    - P13_inferred_relationship_no_record_own_email_part2_of_4:2516 apexauctions.ca | CA / apexauctions.co.uk
- **26 currency filled when a value is filled**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:26 RENTON SCHOOL DISTRICT #403 | 332345.13 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:443 Rectorado de la Universitat de València | 12698.25 (source field: PayableAmount)
    - P01_GOLD_active_relationship_invoicing_AP_email:455 BRINKS DE COLOMBIA S.A. | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:474 University of North Dakota | 145.850 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:503 BELLEVUE, CITY OF | 35488873.2 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:511 UNIVERSITY PLACE SCHOOL DISTRICT #83 | 685477.9 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:530 North Dakota State University | 35.000 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:536 BELLEVUE SCHOOL DISTRICT #405 | 5395.88 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:542 SNOQUALMIE VALLEY SCHOOL DISTRICT #410 | 23980.42 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:549 MARYLAND STADIUM AUTHORITY | 251569.05 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:552 BANCOLOMBIA S.A. | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:563 ECOPETROL S A | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)

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
- P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email: 47
- P01T_active_service_seen_on_buyer_site_invoicing_AP_email: 173
- P01_GOLD_active_relationship_invoicing_AP_email: 626
- P02_active_relationship_finance_accounting_email: 403
- P03_active_relationship_purchasing_email: 209
- P04_active_relationship_general_email: 1569
- P05_likely_active_awarded_12_36_months_any_email: 365
- P06M_member_or_regulated_payer_of_canadian_body_other_email: 4103
- P06T_active_service_seen_on_buyer_site_other_email: 12949
- P06_client_listing_invoicing_AP_email: 263
- P07_client_listing_finance_or_purchasing_email: 501
- P08_client_listing_general_email: 10340
- P09_older_contract_or_payment_any_email: 312
- P10R_ca_domain_registration_contract_own_email: 25497
- P10_linked_from_vendor_site_any_email: 2406
- P11_any_relationship_email_not_yet_confirmed: 3187
- P12_weaker_relationship_within_5_years_own_email: 7
- P13_inferred_relationship_no_record_own_email: 10644

## Field fill across all delivered rows (value present, not `not_published`)
- buyer_website: 73601 (100.0%)
- vendor_address: 71336 (96.9%)
- vendor_website: 68026 (92.4%)
- contract_link: 62957 (85.5%)
- buyer_address: 58425 (79.4%)
- buyer_logo_url: 54320 (73.8%)
- buyer_phone: 50874 (69.1%)
- award_date: 48906 (66.4%)
- vendor_bn9: 44468 (60.4%)
- buyer_legal_name_as_published: 35405 (48.1%)
- vendor_logo_url: 26993 (36.7%)
- vendor_phone: 21786 (29.6%)
- vendor_legal_name: 18038 (24.5%)
- buyer_bn_as_published: 15290 (20.8%)
- vendor_registry_id: 15057 (20.5%)
- vendor_incorporation_date: 15009 (20.4%)
- vendor_neq: 11861 (16.1%)
- vendor_emails: 9645 (13.1%)
- end_date: 5297 (7.2%)
- contract_value: 4808 (6.5%)
- ap_phone: 2866 (3.9%)
- invoice_mailing_address: 2403 (3.3%)
- invoicing_requirements: 2163 (2.9%)
- payment_terms_as_published: 2051 (2.8%)
- invoice_portal_url: 1746 (2.4%)
- po_required_as_published: 1479 (2.0%)
- ap_contact_name_as_published: 942 (1.3%)

## Canada-proof families
- source field: 60186; other: 13415

## Buyer types
- organisation (type not stated in the record): 37832
- company (private sector): 12397
- non-profit / association / cultural body: 8098
- company (private sector) (from the organisation's name / web domain): 5357
- government ministry / agency: 1617
- municipality / local government: 1418
- municipality / local government (from the organisation's name / web domain): 1353
- hospital / health authority: 1289
- non-profit / association / cultural body (from the organisation's name / web domain): 940
- university / college: 682
- utility / public corporation: 662
- university / college (from the organisation's name / web domain): 494
- transport / transit authority: 256
- hospital / health authority (from the organisation's name / web domain): 246
- school board / school district: 178
- First Nation / Indigenous government: 175
- government ministry / agency (from the organisation's name / web domain): 156
- religious organisation (from the organisation's name / web domain): 138
- utility / public corporation (from the organisation's name / web domain): 100
- First Nation / Indigenous government (from the organisation's name / web domain): 67
- transport / transit authority (from the organisation's name / web domain): 56
- US government body (federal, state or local): 29
- school board / school district (from the organisation's name / web domain): 27
- library (from the organisation's name / web domain): 23
- US city / county / local government: 11

## DMARC posture of the delivered mailboxes
- v=DMARC1; p=none (monitor only, no enforcement): 31107
- no DMARC record: 24255
- p=quarantine: 11962
- p=reject: 6201
- invalid DMARC record: 65
- DNS lookup failed: 11
