# Deep audit — 213036 delivered rows in 18 packages (85 files), 2026-11-10

Result: **PASS** — 11 hard checks, 17 soft checks; hard failures: 0. Every flagged row is listed in `audit_flags.csv` with its reasons.

| # | check | kind | rows flagged | verdict |
|---|---|---|---|---|
| 1 | header: identical columns in every file (106 since 2026-11-06) | hard | 0 | PASS |
| 2 | mailbox syntax | hard | 0 | PASS |
| 3 | mailbox referee-confirmed (all but P11) | hard | 0 | PASS |
| 4 | mail server (MX or A) on the mailbox domain | hard | 0 | PASS |
| 4b | mail server not yet checked (row newer than the last DNS pass) | soft | 147132 | REVIEW |
| 5 | no webmail domain | hard | 0 | PASS |
| 6 | no person-like local part | hard | 0 | PASS |
| 7 | role word in the local part | soft | 17143 | REVIEW |
| 8 | receivables-looking local part graded invoicing/AP | soft | 63 | REVIEW |
| 9 | shared government domain: page or quote names the body | soft | 3 | REVIEW |
| 10 | regional token of a multinational on a differently-located body | soft | 0 | PASS |
| 11 | quote contains the address | hard | 0 | PASS |
| 11b | quote shows the label next to the address (referee saw the address on the page) | soft | 1 | REVIEW |
| 12 | evidence page on the organisation's domain (or its site) | soft | 10934 | REVIEW |
| 13 | email_type label matches grade | hard | 0 | PASS |
| 14 | DMARC / SPF / provider columns filled | soft | 8534 | REVIEW |
| 15 | tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m) | soft | 0 | PASS |
| 16 | vendor named and Canada proof present | hard | 0 | PASS |
| 17 | Canada proof is a source field or the vendor's site (never a name) | soft | 0 | PASS |
| 18 | record link present for dated-record tiers | soft | 0 | PASS |
| 19 | buyer name is a name (not a domain or a page title) | soft | 28240 | REVIEW |
| 20 | legal name is not a fragment or a platform copyright | soft | 3840 | REVIEW |
| 21 | one row per mailbox | hard | 0 | PASS |
| 22 | one row per organisation name (same name twice) | soft | 39 | REVIEW |
| 23 | one row per site domain (two rows, different mailboxes, same domain) | soft | 63 | REVIEW |
| 24 | no blank cell | hard | 0 | PASS |
| 25 | jurisdiction vs mailbox top-level domain | soft | 72 | REVIEW |
| 26 | currency filled when a value is filled | soft | 48 | REVIEW |

## Examples of flagged rows (first 12 per check)
- **4b mail server not yet checked (row newer than the last DNS pass)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:4 Algonquin College | algonquincollege.co
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:20 ATTIS LEBLANC | attis-leblanc.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:24 Cologix Canada inc. | cologix.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:26 Edmond Nolin Ltée | constructionenl.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:29 Dyno Nobel Canada inc. | dynonobel.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:31 Constructions Fabmec inc. | fabmec.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:32 Filspec inc. | filspec.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:34 331265 Ontario Limited / G&P Welding and | gpwelding.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:35 Électricité de la Capitale Inc. | groleaudev.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:38 Huppé réfrigération | hupperefrigeration.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:47 POMPAGE INDUSTRIEL, DIVISION SAGUENAY | pompageindustriel.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:55 Signature JM Xtrême inc. | signaturejmxtreme.ca
- **7 role word in the local part**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:20 Cameco Corporation | ap_cameco@cameco.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:47 New Relic | ap_ireland@newrelic.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:113 Scouts de Dieppe | paiement@scoutsdedieppe.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:164 Keyera | ap_inquiries@keyera.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:207 Ecce Terra | paiement@ecceterra.com
    - P01_GOLD_active_relationship_invoicing_AP_email:276 Town of Oakville | ap_inquiries@oakville.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:300 University of Saskatchewan | connectionpoint@usask.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:302 Miami-Dade County (business unit CU05010 | invsubp@miamidade.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:391 BELL TEXTRON INC | APBell@textron.com
    - P02_active_relationship_finance_accounting_email:7 Agriculture and Agri-Food Canada | directdeposit.depotdirect@canada.ca
    - P02_active_relationship_finance_accounting_email:13 Crown-Indigenous Relations and Northern  | depotdirect-directdeposit@sac-isc.gc.ca
    - P02_active_relationship_finance_accounting_email:14 Department of Justice Canada | mdv_dpf@justice.gc.ca
- **8 receivables-looking local part graded invoicing/AP**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:59 About | payment@birchfumigators.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:7 Texas Tech University | payment.strategies@ttu.edu
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:97 Furbaby Pet Care Saskatoon | payments@furbabysk.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:118 G&S Electric | payments@gandselectric.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:131 Lerners Lawyers | payments@lerners.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:144 Calgary Coin Gallery | payment@calgarycoin.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:180 WeirFoulds LLP | payments@weirfoulds.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:192 Whitefish River First Nation | payments@whitefishriver.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:201 Insight CPA | payments@providinginsight.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:250 Atchison Plumbing | payments@atchisonplumbing.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:266 Awninginabox.ca | payment@awninginabox.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:268 ck-ca.com | payments@ck-ca.com
- **9 shared government domain: page or quote names the body**
    - P01_GOLD_active_relationship_invoicing_AP_email:43 Canadian Space Agency | invoicing.csa-asc.facturation@canada.ca ← https://www.canada.ca/en/public-services-procurement/services/payments-to-from-g
    - P07_client_listing_finance_or_purchasing_email:25 transportation.ky.gov | finance.crcgroup@ky.gov ← https://finance.ky.gov/eProcurement/Pages/doing-business-with-the-commonwealth.a
    - P13_inferred_relationship_no_record_own_email_part1_of_6:195 Landlord and Tenant Board | ltbpayments@ontario.ca ← https://tribunalsontario.ca/ltb/contact/
- **11b quote shows the label next to the address (referee saw the address on the page)**
    - P10R_ca_domain_registration_contract_own_email_part13_of_36:616 Vancouvery Vintages | LET’S STAY IN TOUCH Keep updated with the latest and greates
- **12 evidence page on the organisation's domain (or its site)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:20 ATTIS LEBLANC | payable@attis-leblanc.com on attis-leblanc.ca (site attis-leblanc.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:22 Motorola Solutions | recepcionfacturas@motorolasolutions.com on web.archive.org (site motorolasolutions.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:110 WOMEN'S PLACE (ST CATHARINES & DISTRICT) | finance@gilliansplace.com on gilliansplace.ca (site gilliansplace.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:251 Canadian Research Knowledge Network | finance@crkn.ca on crkn-rcdr.ca (site crkn.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:261 dabc.ca | ap@dabc.ca on disabilityalliancebc.org (site dabc.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:262 transbec.ca | payables@transbec.ca on transbec.com (site transbec.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:284 Penner Auctions | morden.payments@pennerauctions.com on pennerauctions.ca (site pennerauctions.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:289 crd.bc.ca | accountspayable@crd.bc.ca on crd.ca (site crd.bc.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:296 Anna's Garden, Home & Wellness | accountspayable@annasflowers.ca on shopannas.ca (site annasflowers.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:2 Department of Defence | invoices@defence.gov.au on web.archive.org (site defence.gov.au)
    - P01_GOLD_active_relationship_invoicing_AP_email:3 Department of Industry, Science and Reso | einvoicingqueries@industry.gov.au on directory.peppol.eu (site industry.gov.au)
    - P01_GOLD_active_relationship_invoicing_AP_email:51 Natural Sciences and Engineering Researc | payables@nserc-crsng.gc.ca on nserc-crsng.canada.ca (site nserc-crsng.gc.ca)
- **14 DMARC / SPF / provider columns filled**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:57 Vitrerie TB inc. | not checked yet | not checked yet | not checked
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:121 Why Not Energy Services | not checked yet | not checked yet | not checked
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:173 Usinage SPS | not checked yet | not checked yet | not checked
    - P02_active_relationship_finance_accounting_email:441 The University of Tampa | not checked yet | not checked yet | not checked
    - P02_active_relationship_finance_accounting_email:445 Xpresso bar à vetements | not checked yet | not checked yet | not checked
    - P02_active_relationship_finance_accounting_email:457 Yoga Alliance | not checked yet | not checked yet | not checked
    - P04_active_relationship_general_email_part1_of_2:1590 UNIF | not checked yet | not checked yet | not checked
    - P04_active_relationship_general_email_part2_of_2:40 Upscale Audio | not checked yet | not checked yet | not checked
    - P04_active_relationship_general_email_part2_of_2:119 Ysé Paris | not checked yet | not checked yet | not checked
    - P04_active_relationship_general_email_part2_of_2:146 Webtech Industries | not checked yet | not checked yet | not checked
    - P04_active_relationship_general_email_part2_of_2:582 Yan Health | not checked yet | not checked yet | not checked
    - P04_active_relationship_general_email_part2_of_2:584 Upright Security | not checked yet | not checked yet | not checked
- **19 buyer name is a name (not a domain or a page title)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:59 About | About
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:60 About | About
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:37 ovs.com | ovs.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:106 loulourentals.com | loulourentals.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:112 cstx.gov | cstx.gov
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:133 efifoodequip.com | efifoodequip.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:137 mmcorp.ca | mmcorp.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:161 cpaquebec.ca | cpaquebec.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:197 gatech.edu | gatech.edu
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:220 tbdssab.ca | tbdssab.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:243 finiquip.ca | finiquip.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:248 glrinc.ca | glrinc.ca
- **20 legal name is not a fragment or a platform copyright**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:20 ATTIS LEBLANC | 9395-4477 Québec inc. (the Régie du bâtiment du Québec's list of activ
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:22 BGIS O&M Solutions inc. | BGIS O&M Solutions inc. (the Régie du bâtiment du Québec's list of act
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:25 Construction et Rénovation Denis Inc. | Construction et Rénovation Denis Inc. (the Régie du bâtiment du Québec
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:26 Edmond Nolin Ltée | Edmond Nolin Ltée (the Régie du bâtiment du Québec's list of active li
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:27 Construction Finition inc. | Construction Finition inc. (the Régie du bâtiment du Québec's list of 
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:28 Dion électrique inc. | Dion électrique inc. (the Régie du bâtiment du Québec's list of active
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:29 Dyno Nobel Canada inc. | Dyno Nobel Canada inc. (the Régie du bâtiment du Québec's list of acti
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:31 Constructions Fabmec inc. | Constructions Fabmec inc. (the Régie du bâtiment du Québec's list of a
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:32 Filspec inc. | Filspec inc. (the Régie du bâtiment du Québec's list of active licence
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:34 331265 Ontario Limited / G&P Welding and | 331265 Ontario Limited / G&P Welding and Ironworks (the Régie du bâtim
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:35 Électricité de la Capitale Inc. | Électricité de la Capitale Inc. (the Régie du bâtiment du Québec's lis
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:36 Groupe Nordfab inc. | Groupe Nordfab inc. (the Régie du bâtiment du Québec's list of active 
- **22 one row per organisation name (same name twice)**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:108 Collings Insurance Brokers | 2 rows, same mail domain: collingsinsurance.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:185 Niagara Children Centre | 2 rows, same mail domain: niagarachildrenscentre.com
    - P01_GOLD_active_relationship_invoicing_AP_email:16 Rocky View County | 2 rows, same mail domain: rockyview.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:26 University of Lethbridge | 2 rows, same mail domain: uleth.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:234 Metrolinx | 2 rows, same mail domain: metrolinx.com
    - P01_GOLD_active_relationship_invoicing_AP_email:257 City of Brantford | 2 rows, same mail domain: brantford.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:277 City of Port Moody | 2 rows, same mail domain: portmoody.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:498 City of Edmonton | 2 rows, same mail domain: edmonton.ca
    - P02_active_relationship_finance_accounting_email:137 Ville de Princeville | 2 rows, same mail domain: princeville.quebec
    - P02_active_relationship_finance_accounting_email:438 Saint Mary's University | 2 rows, same mail domain: smu.ca
    - P03_active_relationship_purchasing_email:109 City of North Bay | 2 rows, same mail domain: northbay.ca
    - P04_active_relationship_general_email_part1_of_2:317 Cégep de Victoriaville. | 2 rows, same mail domain: cegepvicto.ca
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
    - P01_GOLD_active_relationship_invoicing_AP_email:284 Township of Scugog | scugog.ca: 2 rows, invoice@scugog.ca; mail@scugog.ca
- **25 jurisdiction vs mailbox top-level domain**
    - P01_GOLD_active_relationship_invoicing_AP_email:248 Utilities Kingston | CA / kingston.gov.uk
    - P13_inferred_relationship_no_record_own_email_part1_of_6:171 Rheinmetall AG | CA / rheinmetall.com.au
    - P13_inferred_relationship_no_record_own_email_part1_of_6:179 Westpac | CA / westpac.com.au
    - P13_inferred_relationship_no_record_own_email_part1_of_6:197 United States Postal Service | CA / usps.gov
    - P13_inferred_relationship_no_record_own_email_part1_of_6:397 Randstad Deutschland | CA / randstad.de
    - P13_inferred_relationship_no_record_own_email_part1_of_6:626 LA MAISON DES JEUNES DE PLESSISVILLE INC | QC / lycos.fr
    - P13_inferred_relationship_no_record_own_email_part1_of_6:848 The Redeemed Christian Church of God Lov | SK / loveassembly.co.uk
    - P13_inferred_relationship_no_record_own_email_part1_of_6:1382 mgmarketing.fr | QC / mgmarketing.fr
    - P13_inferred_relationship_no_record_own_email_part2_of_6:1224 KNDS | CA / knds.de
    - P13_inferred_relationship_no_record_own_email_part2_of_6:1234 The Warehouse Group | CA / thewarehousegroup.co.nz
    - P13_inferred_relationship_no_record_own_email_part2_of_6:2823 akelius.ca | CA / akelius.fr
    - P13_inferred_relationship_no_record_own_email_part2_of_6:2834 apexauctions.ca | CA / apexauctions.co.uk
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
- P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email: 65
- P01T_active_service_seen_on_buyer_site_invoicing_AP_email: 304
- P01_GOLD_active_relationship_invoicing_AP_email: 625
- P02_active_relationship_finance_accounting_email: 462
- P03_active_relationship_purchasing_email: 255
- P04_active_relationship_general_email: 3254
- P05_likely_active_awarded_12_36_months_any_email: 413
- P06M_member_or_regulated_payer_of_canadian_body_other_email: 6002
- P06T_active_service_seen_on_buyer_site_other_email: 53606
- P06_client_listing_invoicing_AP_email: 278
- P07_client_listing_finance_or_purchasing_email: 680
- P08_client_listing_general_email: 20545
- P09_older_contract_or_payment_any_email: 303
- P10R_ca_domain_registration_contract_own_email: 96430
- P10_linked_from_vendor_site_any_email: 2607
- P11_any_relationship_email_not_yet_confirmed: 9344
- P12_weaker_relationship_within_5_years_own_email: 8
- P13_inferred_relationship_no_record_own_email: 17855

## Field fill across all delivered rows (value present, not `not_published`)
- buyer_website: 213036 (100.0%)
- vendor_address: 210107 (98.6%)
- vendor_website: 201734 (94.7%)
- contract_link: 195181 (91.6%)
- award_date: 168682 (79.2%)
- buyer_address: 148531 (69.7%)
- vendor_legal_name: 145637 (68.4%)
- buyer_logo_url: 138297 (64.9%)
- vendor_bn9: 135225 (63.5%)
- vendor_registry_id: 132257 (62.1%)
- vendor_incorporation_date: 132222 (62.1%)
- buyer_phone: 109452 (51.4%)
- vendor_logo_url: 88645 (41.6%)
- buyer_legal_name_as_published: 71021 (33.3%)
- vendor_phone: 70612 (33.1%)
- vendor_emails: 36927 (17.3%)
- vendor_neq: 20905 (9.8%)
- buyer_bn_as_published: 20127 (9.4%)
- end_date: 6862 (3.2%)
- contract_value: 6129 (2.9%)
- payment_terms_as_published: 4225 (2.0%)
- ap_phone: 3154 (1.5%)
- invoice_mailing_address: 2504 (1.2%)
- invoicing_requirements: 2323 (1.1%)
- po_required_as_published: 2120 (1.0%)
- invoice_portal_url: 2076 (1.0%)
- ap_contact_name_as_published: 1058 (0.5%)

## Canada-proof families
- source field: 191074; other: 21962

## Buyer types
- organisation (type not stated in the record): 129952
- company (private sector): 29734
- company (private sector) (from the organisation's name / web domain): 20166
- non-profit / association / cultural body: 13062
- government ministry / agency: 5192
- hospital / health authority: 2439
- non-profit / association / cultural body (from the organisation's name / web domain): 2350
- utility / public corporation: 2164
- municipality / local government: 1566
- municipality / local government (from the organisation's name / web domain): 1361
- university / college: 1216
- transport / transit authority: 675
- hospital / health authority (from the organisation's name / web domain): 583
- university / college (from the organisation's name / web domain): 493
- utility / public corporation (from the organisation's name / web domain): 466
- government ministry / agency (from the organisation's name / web domain): 397
- religious organisation (from the organisation's name / web domain): 274
- First Nation / Indigenous government: 266
- transport / transit authority (from the organisation's name / web domain): 213
- school board / school district: 184
- First Nation / Indigenous government (from the organisation's name / web domain): 173
- library (from the organisation's name / web domain): 40
- school board / school district (from the organisation's name / web domain): 30
- US government body (federal, state or local): 29
- US city / county / local government: 11

## DMARC posture of the delivered mailboxes
- no DMARC record: 85690
- v=DMARC1; p=none (monitor only, no enforcement): 78634
- p=quarantine: 26738
- p=reject: 13225
- not checked yet: 8534
- invalid DMARC record: 156
- DNS lookup failed: 59
