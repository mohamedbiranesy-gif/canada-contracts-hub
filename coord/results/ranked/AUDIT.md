# Deep audit — 165252 delivered rows in 18 packages (68 files), 2026-11-10

Result: **FAIL** — 11 hard checks, 17 soft checks; hard failures: 1. Every flagged row is listed in `audit_flags.csv` with its reasons.

| # | check | kind | rows flagged | verdict |
|---|---|---|---|---|
| 1 | header: identical columns in every file (106 since 2026-11-06) | hard | 0 | PASS |
| 2 | mailbox syntax | hard | 0 | PASS |
| 3 | mailbox referee-confirmed (all but P11) | hard | 0 | PASS |
| 4 | mail server (MX or A) on the mailbox domain | hard | 0 | PASS |
| 4b | mail server not yet checked (row newer than the last DNS pass) | soft | 99432 | REVIEW |
| 5 | no webmail domain | hard | 1 | FAIL |
| 6 | no person-like local part | hard | 0 | PASS |
| 7 | role word in the local part | soft | 11803 | REVIEW |
| 8 | receivables-looking local part graded invoicing/AP | soft | 58 | REVIEW |
| 9 | shared government domain: page or quote names the body | soft | 3 | REVIEW |
| 10 | regional token of a multinational on a differently-located body | soft | 0 | PASS |
| 11 | quote contains the address | hard | 0 | PASS |
| 11b | quote shows the label next to the address (referee saw the address on the page) | soft | 1 | REVIEW |
| 12 | evidence page on the organisation's domain (or its site) | soft | 8308 | REVIEW |
| 13 | email_type label matches grade | hard | 0 | PASS |
| 14 | DMARC / SPF / provider columns filled | soft | 26293 | REVIEW |
| 15 | tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m) | soft | 0 | PASS |
| 16 | vendor named and Canada proof present | hard | 0 | PASS |
| 17 | Canada proof is a source field or the vendor's site (never a name) | soft | 0 | PASS |
| 18 | record link present for dated-record tiers | soft | 0 | PASS |
| 19 | buyer name is a name (not a domain or a page title) | soft | 21027 | REVIEW |
| 20 | legal name is not a fragment or a platform copyright | soft | 3198 | REVIEW |
| 21 | one row per mailbox | hard | 0 | PASS |
| 22 | one row per organisation name (same name twice) | soft | 23 | REVIEW |
| 23 | one row per site domain (two rows, different mailboxes, same domain) | soft | 62 | REVIEW |
| 24 | no blank cell | hard | 0 | PASS |
| 25 | jurisdiction vs mailbox top-level domain | soft | 60 | REVIEW |
| 26 | currency filled when a value is filled | soft | 48 | REVIEW |

## Examples of flagged rows (first 12 per check)
- **4b mail server not yet checked (row newer than the last DNS pass)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:4 Algonquin College | algonquincollege.co
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:19 ATTIS LEBLANC | attis-leblanc.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:23 Cologix Canada inc. | cologix.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:25 Edmond Nolin Ltée | constructionenl.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:28 Dyno Nobel Canada inc. | dynonobel.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:30 Constructions Fabmec inc. | fabmec.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:31 Filspec inc. | filspec.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:33 331265 Ontario Limited / G&P Welding and | gpwelding.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:35 Huppé réfrigération | hupperefrigeration.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:39 Métodex Métaux Ouvrés inc. | metodex.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:52 Signature JM Xtrême inc. | signaturejmxtreme.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:56 About | dfcdiesel.com
- **5 no webmail domain**
    - P08_client_listing_general_email_part6_of_6:832 Palmer College of Chiropractic | palmerfinancialaidmaincampus@live.palmer.edu
- **7 role word in the local part**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:20 Cameco Corporation | ap_cameco@cameco.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:47 New Relic | ap_ireland@newrelic.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:111 Scouts de Dieppe | paiement@scoutsdedieppe.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:151 Keyera | ap_inquiries@keyera.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:183 Ecce Terra | paiement@ecceterra.com
    - P01_GOLD_active_relationship_invoicing_AP_email:276 Town of Oakville | ap_inquiries@oakville.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:300 University of Saskatchewan | connectionpoint@usask.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:302 Miami-Dade County (business unit CU05010 | invsubp@miamidade.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:391 BELL TEXTRON INC | APBell@textron.com
    - P02_active_relationship_finance_accounting_email:7 Agriculture and Agri-Food Canada | directdeposit.depotdirect@canada.ca
    - P02_active_relationship_finance_accounting_email:13 Crown-Indigenous Relations and Northern  | depotdirect-directdeposit@sac-isc.gc.ca
    - P02_active_relationship_finance_accounting_email:14 Department of Justice Canada | mdv_dpf@justice.gc.ca
- **8 receivables-looking local part graded invoicing/AP**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:55 About | payment@birchfumigators.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:7 Texas Tech University | payment.strategies@ttu.edu
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:97 Furbaby Pet Care Saskatoon | payments@furbabysk.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:124 Lerners Lawyers | payments@lerners.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:134 Calgary Coin Gallery | payment@calgarycoin.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:163 WeirFoulds LLP | payments@weirfoulds.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:172 Whitefish River First Nation | payments@whitefishriver.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:179 Insight CPA | payments@providinginsight.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:224 Atchison Plumbing | payments@atchisonplumbing.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:240 Awninginabox.ca | payment@awninginabox.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:253 Penner Auctions | morden.payments@pennerauctions.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:262 Facility Solutions Canada Limited | payments@facilitysolutionscanada.ca
- **9 shared government domain: page or quote names the body**
    - P01_GOLD_active_relationship_invoicing_AP_email:43 Canadian Space Agency | invoicing.csa-asc.facturation@canada.ca ← https://www.canada.ca/en/public-services-procurement/services/payments-to-from-g
    - P07_client_listing_finance_or_purchasing_email:24 transportation.ky.gov | finance.crcgroup@ky.gov ← https://finance.ky.gov/eProcurement/Pages/doing-business-with-the-commonwealth.a
    - P13_inferred_relationship_no_record_own_email_part1_of_5:184 Landlord and Tenant Board | ltbpayments@ontario.ca ← https://tribunalsontario.ca/ltb/contact/
- **11b quote shows the label next to the address (referee saw the address on the page)**
    - P10R_ca_domain_registration_contract_own_email_part4_of_28:2518 Vancouvery Vintages | LET’S STAY IN TOUCH Keep updated with the latest and greates
- **12 evidence page on the organisation's domain (or its site)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:19 ATTIS LEBLANC | payable@attis-leblanc.com on attis-leblanc.ca (site attis-leblanc.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:22 Motorola Solutions | recepcionfacturas@motorolasolutions.com on web.archive.org (site motorolasolutions.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:225 Canadian Research Knowledge Network | finance@crkn.ca on crkn-rcdr.ca (site crkn.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:235 dabc.ca | ap@dabc.ca on disabilityalliancebc.org (site dabc.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:236 transbec.ca | payables@transbec.ca on transbec.com (site transbec.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:253 Penner Auctions | morden.payments@pennerauctions.com on pennerauctions.ca (site pennerauctions.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:257 crd.bc.ca | accountspayable@crd.bc.ca on crd.ca (site crd.bc.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:2 Department of Defence | invoices@defence.gov.au on web.archive.org (site defence.gov.au)
    - P01_GOLD_active_relationship_invoicing_AP_email:3 Department of Industry, Science and Reso | einvoicingqueries@industry.gov.au on directory.peppol.eu (site industry.gov.au)
    - P01_GOLD_active_relationship_invoicing_AP_email:51 Natural Sciences and Engineering Researc | payables@nserc-crsng.gc.ca on nserc-crsng.canada.ca (site nserc-crsng.gc.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:66 Ville de Montréal | facture@montreal.ca on ville.montreal.qc.ca (site montreal.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:95 Ville de Farnham | comptespayables@ville.farnham.qc.ca on web.archive.org (site ville.farnham.qc.ca)
- **14 DMARC / SPF / provider columns filled**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:52 Signature JM Xtrême inc. | not checked yet | not checked yet | not checked
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:100 TAG Canada | not checked yet | not checked yet | not checked
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:109 Pelletier et Picard inc. | not checked yet | not checked yet | not checked
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:111 Scouts de Dieppe | not checked yet | not checked yet | not checked
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:115 Proactive Utility Services Inc. | not checked yet | not checked yet | not checked
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:144 Northcoast Lumber | not checked yet | not checked yet | not checked
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:162 Synergy Controls | not checked yet | not checked yet | not checked
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:166 Partition Systems Ltd. | not checked yet | not checked yet | not checked
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:168 Sana Commerce | not checked yet | not checked yet | not checked
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:179 Insight CPA | not checked yet | not checked yet | not checked
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:185 Town of Pasadena | not checked yet | not checked yet | not checked
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:236 transbec.ca | not checked yet | not checked yet | not checked
- **19 buyer name is a name (not a domain or a page title)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:55 About | About
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:56 About | About
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:37 ovs.com | ovs.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:104 loulourentals.com | loulourentals.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:110 cstx.gov | cstx.gov
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:128 mmcorp.ca | mmcorp.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:141 abpilottruck.ca | abpilottruck.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:148 cpaquebec.ca | cpaquebec.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:175 gatech.edu | gatech.edu
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:196 tbdssab.ca | tbdssab.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:218 finiquip.ca | finiquip.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:222 glrinc.ca | glrinc.ca
- **20 legal name is not a fragment or a platform copyright**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:19 ATTIS LEBLANC | 9395-4477 Québec inc. (the Régie du bâtiment du Québec's list of activ
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:21 BGIS O&M Solutions inc. | BGIS O&M Solutions inc. (the Régie du bâtiment du Québec's list of act
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:23 Cologix Canada inc. | Cologix Canada inc. (the Régie du bâtiment du Québec's list of active 
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:24 Construction et Rénovation Denis Inc. | Construction et Rénovation Denis Inc. (the Régie du bâtiment du Québec
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:25 Edmond Nolin Ltée | Edmond Nolin Ltée (the Régie du bâtiment du Québec's list of active li
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:26 Construction Finition inc. | Construction Finition inc. (the Régie du bâtiment du Québec's list of 
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:27 Dion électrique inc. | Dion électrique inc. (the Régie du bâtiment du Québec's list of active
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:28 Dyno Nobel Canada inc. | Dyno Nobel Canada inc. (the Régie du bâtiment du Québec's list of acti
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:30 Constructions Fabmec inc. | Constructions Fabmec inc. (the Régie du bâtiment du Québec's list of a
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:31 Filspec inc. | Filspec inc. (the Régie du bâtiment du Québec's list of active licence
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:33 331265 Ontario Limited / G&P Welding and | 331265 Ontario Limited / G&P Welding and Ironworks (the Régie du bâtim
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:34 Groupe Nordfab inc. | Groupe Nordfab inc. (the Régie du bâtiment du Québec's list of active 
- **22 one row per organisation name (same name twice)**
    - P01_GOLD_active_relationship_invoicing_AP_email:26 University of Lethbridge | 2 rows, same mail domain: uleth.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:234 Metrolinx | 2 rows, same mail domain: metrolinx.com
    - P01_GOLD_active_relationship_invoicing_AP_email:277 City of Port Moody | 2 rows, same mail domain: portmoody.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:498 City of Edmonton | 2 rows, same mail domain: edmonton.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:554 Enbridge Inc. | 2 rows, same mail domain: enbridge.com
    - P02_active_relationship_finance_accounting_email:138 Ville de Princeville | 2 rows, same mail domain: princeville.quebec
    - P03_active_relationship_purchasing_email:109 City of North Bay | 2 rows, same mail domain: northbay.ca
    - P04_active_relationship_general_email_part1_of_2:319 Cégep de Victoriaville. | 2 rows, same mail domain: cegepvicto.ca
    - P04_active_relationship_general_email_part1_of_2:454 Cégep de Granby | 2 rows, same mail domain: cegepgranby.qc.ca
    - P04_active_relationship_general_email_part1_of_2:953 CANADIAN CANCER SOCIETY | 2 rows, same mail domain: cancer.ca
    - P04_active_relationship_general_email_part2_of_2:843 SIC MARKING | 2 rows, same mail domain: sic-marking.com
    - P05_likely_active_awarded_12_36_months_any_email:5 Brandon University | 2 rows, same mail domain: brandonu.ca
- **23 one row per site domain (two rows, different mailboxes, same domain)**
    - P01_GOLD_active_relationship_invoicing_AP_email:2 Department of Defence | defence.gov.au: 2 rows, invoices@defence.gov.au; peppol.einvoices@defence.gov.au
    - P01_GOLD_active_relationship_invoicing_AP_email:27 University of Toronto | utoronto.ca: 2 rows, ap.fsd@utoronto.ca; fmdinvoice.utsc@utoronto.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:57 Ville de Gatineau | gatineau.ca: 2 rows, gatineau.factures@gatineau.ca; idgatineau@gatineau.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:66 Ville de Montréal | montreal.ca: 2 rows, facture@montreal.ca; comptesapayer@montreal.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:82 Ville de Laval | laval.ca: 3 rows, comptespayables@laval.ca; lavaleconomique@laval.ca; info@laval.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:115 Texas Department of Insurance | texas.gov: 7 rows, invoices@tdi.texas.gov; ap@ers.texas.gov; ap@tsl.texas.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:128 University of Ottawa | uottawa.ca: 2 rows, payables@uottawa.ca; info@emba.uottawa.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:194 Oregon Department of Transportation | oregon.gov: 3 rows, opoinvoiceinquiries@odot.oregon.gov; omdaccounts.payable@omd.oregon.gov; odf.accountspayable@oregon.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:197 Texas Tech University Health Sciences Ce | ttuhsc.edu: 2 rows, Accounts.Payable@ttuhsc.edu; accountspayableelp@ttuhsc.edu
    - P01_GOLD_active_relationship_invoicing_AP_email:234 Metrolinx | metrolinx.com: 2 rows, it.invoices@metrolinx.com; rti.invoices@metrolinx.com
    - P01_GOLD_active_relationship_invoicing_AP_email:259 Niagara Region | niagararegion.ca: 2 rows, constructioninvoices@niagararegion.ca; NRHCapitalWorks@niagararegion.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:354 Virginia State Police | virginia.gov: 5 rows, ap@vsp.virginia.gov; accountspayable@energy.virginia.gov; support@dhrm.virginia.gov
- **25 jurisdiction vs mailbox top-level domain**
    - P01_GOLD_active_relationship_invoicing_AP_email:248 Utilities Kingston | CA / kingston.gov.uk
    - P13_inferred_relationship_no_record_own_email_part1_of_5:160 Rheinmetall AG | CA / rheinmetall.com.au
    - P13_inferred_relationship_no_record_own_email_part1_of_5:168 Westpac | CA / westpac.com.au
    - P13_inferred_relationship_no_record_own_email_part1_of_5:186 United States Postal Service | CA / usps.gov
    - P13_inferred_relationship_no_record_own_email_part1_of_5:368 Randstad Deutschland | CA / randstad.de
    - P13_inferred_relationship_no_record_own_email_part1_of_5:605 LA MAISON DES JEUNES DE PLESSISVILLE INC | QC / lycos.fr
    - P13_inferred_relationship_no_record_own_email_part1_of_5:828 The Redeemed Christian Church of God Lov | SK / loveassembly.co.uk
    - P13_inferred_relationship_no_record_own_email_part1_of_5:1335 mgmarketing.fr | QC / mgmarketing.fr
    - P13_inferred_relationship_no_record_own_email_part2_of_5:842 KNDS | CA / knds.de
    - P13_inferred_relationship_no_record_own_email_part2_of_5:852 The Warehouse Group | CA / thewarehousegroup.co.nz
    - P13_inferred_relationship_no_record_own_email_part2_of_5:2456 akelius.ca | CA / akelius.fr
    - P13_inferred_relationship_no_record_own_email_part2_of_5:2468 apexauctions.ca | CA / apexauctions.co.uk
- **26 currency filled when a value is filled**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:27 RENTON SCHOOL DISTRICT #403 | 332345.13 (source field: amount)
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
- P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email: 61
- P01T_active_service_seen_on_buyer_site_invoicing_AP_email: 269
- P01_GOLD_active_relationship_invoicing_AP_email: 625
- P02_active_relationship_finance_accounting_email: 462
- P03_active_relationship_purchasing_email: 255
- P04_active_relationship_general_email: 3204
- P05_likely_active_awarded_12_36_months_any_email: 413
- P06M_member_or_regulated_payer_of_canadian_body_other_email: 5017
- P06T_active_service_seen_on_buyer_site_other_email: 37441
- P06_client_listing_invoicing_AP_email: 276
- P07_client_listing_finance_or_purchasing_email: 653
- P08_client_listing_general_email: 19441
- P09_older_contract_or_payment_any_email: 305
- P10R_ca_domain_registration_contract_own_email: 74764
- P10_linked_from_vendor_site_any_email: 2591
- P11_any_relationship_email_not_yet_confirmed: 5230
- P12_weaker_relationship_within_5_years_own_email: 8
- P13_inferred_relationship_no_record_own_email: 14237

## Field fill across all delivered rows (value present, not `not_published`)
- buyer_website: 165252 (100.0%)
- vendor_address: 162310 (98.2%)
- vendor_website: 157782 (95.5%)
- contract_link: 151015 (91.4%)
- award_date: 125777 (76.1%)
- buyer_address: 115086 (69.6%)
- vendor_bn9: 100643 (60.9%)
- vendor_legal_name: 98901 (59.8%)
- vendor_registry_id: 94281 (57.1%)
- vendor_incorporation_date: 94181 (57.0%)
- buyer_logo_url: 56728 (34.3%)
- buyer_phone: 53025 (32.1%)
- vendor_logo_url: 44782 (27.1%)
- buyer_legal_name_as_published: 36184 (21.9%)
- vendor_phone: 33762 (20.4%)
- vendor_emails: 17584 (10.6%)
- buyer_bn_as_published: 15177 (9.2%)
- vendor_neq: 14000 (8.5%)
- end_date: 5992 (3.6%)
- contract_value: 5394 (3.3%)
- payment_terms_as_published: 3410 (2.1%)
- ap_phone: 3068 (1.9%)
- invoice_mailing_address: 2482 (1.5%)
- invoicing_requirements: 2287 (1.4%)
- invoice_portal_url: 1978 (1.2%)
- po_required_as_published: 1954 (1.2%)
- ap_contact_name_as_published: 1036 (0.6%)

## Canada-proof families
- source field: 147608; other: 17644

## Buyer types
- organisation (type not stated in the record): 108521
- company (private sector): 22241
- non-profit / association / cultural body: 11609
- company (private sector) (from the organisation's name / web domain): 7023
- government ministry / agency: 3806
- hospital / health authority: 1989
- utility / public corporation: 1688
- non-profit / association / cultural body (from the organisation's name / web domain): 1516
- municipality / local government: 1487
- municipality / local government (from the organisation's name / web domain): 1312
- university / college: 1098
- transport / transit authority: 526
- university / college (from the organisation's name / web domain): 428
- hospital / health authority (from the organisation's name / web domain): 423
- utility / public corporation (from the organisation's name / web domain): 311
- government ministry / agency (from the organisation's name / web domain): 267
- First Nation / Indigenous government: 240
- religious organisation (from the organisation's name / web domain): 215
- school board / school district: 183
- transport / transit authority (from the organisation's name / web domain): 139
- First Nation / Indigenous government (from the organisation's name / web domain): 135
- US government body (federal, state or local): 29
- library (from the organisation's name / web domain): 29
- school board / school district (from the organisation's name / web domain): 26
- US city / county / local government: 11

## DMARC posture of the delivered mailboxes
- v=DMARC1; p=none (monitor only, no enforcement): 55040
- no DMARC record: 53568
- not checked yet: 26293
- p=quarantine: 19974
- p=reject: 10202
- invalid DMARC record: 112
- DNS lookup failed: 63
