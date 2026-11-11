# Deep audit — 236262 delivered rows in 18 packages (93 files), 2026-11-11

Result: **PASS** — 11 hard checks, 17 soft checks; hard failures: 0. Every flagged row is listed in `audit_flags.csv` with its reasons.

| # | check | kind | rows flagged | verdict |
|---|---|---|---|---|
| 1 | header: identical columns in every file (106 since 2026-11-06) | hard | 0 | PASS |
| 2 | mailbox syntax | hard | 0 | PASS |
| 3 | mailbox referee-confirmed (all but P11) | hard | 0 | PASS |
| 4 | mail server (MX or A) on the mailbox domain | hard | 0 | PASS |
| 4b | mail server not yet checked (row newer than the last DNS pass) | soft | 170246 | REVIEW |
| 5 | no webmail domain | hard | 0 | PASS |
| 6 | no person-like local part | hard | 0 | PASS |
| 7 | role word in the local part | soft | 19567 | REVIEW |
| 8 | receivables-looking local part graded invoicing/AP | soft | 69 | REVIEW |
| 9 | shared government domain: page or quote names the body | soft | 4 | REVIEW |
| 10 | regional token of a multinational on a differently-located body | soft | 0 | PASS |
| 11 | quote contains the address | hard | 0 | PASS |
| 11b | quote shows the label next to the address (referee saw the address on the page) | soft | 1 | REVIEW |
| 12 | evidence page on the organisation's domain (or its site) | soft | 12251 | REVIEW |
| 13 | email_type label matches grade | hard | 0 | PASS |
| 14 | DMARC / SPF / provider columns filled | soft | 0 | PASS |
| 15 | tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m) | soft | 6 | REVIEW |
| 16 | vendor named and Canada proof present | hard | 0 | PASS |
| 17 | Canada proof is a source field or the vendor's site (never a name) | soft | 0 | PASS |
| 18 | record link present for dated-record tiers | soft | 0 | PASS |
| 19 | buyer name is a name (not a domain or a page title) | soft | 27801 | REVIEW |
| 20 | legal name is not a fragment or a platform copyright | soft | 4806 | REVIEW |
| 21 | one row per mailbox | hard | 0 | PASS |
| 22 | one row per organisation name (same name twice) | soft | 50 | REVIEW |
| 23 | one row per site domain (two rows, different mailboxes, same domain) | soft | 64 | REVIEW |
| 24 | no blank cell | hard | 0 | PASS |
| 25 | jurisdiction vs mailbox top-level domain | soft | 78 | REVIEW |
| 26 | currency filled when a value is filled | soft | 49 | REVIEW |

## Examples of flagged rows (first 12 per check)
- **4b mail server not yet checked (row newer than the last DNS pass)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:4 Algonquin College | algonquincollege.co
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:20 ATTIS LEBLANC | attis-leblanc.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:24 Cologix Canada inc. | cologix.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:26 Edmond Nolin Ltée | constructionenl.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:28 Daikin Applied Canada inc. | daikinapplied.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:29 Deblois réfrigération inc. | debloisrefrigeration.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:31 Construction D.M. Turcotte J.M. inc. | dmturcotte.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:32 Dyno Nobel Canada inc. | dynonobel.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:34 Constructions Fabmec inc. | fabmec.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:35 Filspec inc. | filspec.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:37 331265 Ontario Limited / G&P Welding and | gpwelding.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:38 Électricité de la Capitale Inc. | groleaudev.com
- **7 role word in the local part**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:20 Cameco Corporation | ap_cameco@cameco.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:48 New Relic | ap_ireland@newrelic.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:116 Scouts de Dieppe | paiement@scoutsdedieppe.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:168 Keyera | ap_inquiries@keyera.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:213 Ecce Terra | paiement@ecceterra.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:312 Courses Vintage Québec | paiements@cvqvintage.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:276 Town of Oakville | ap_inquiries@oakville.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:300 University of Saskatchewan | connectionpoint@usask.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:302 Miami-Dade County (business unit CU05010 | invsubp@miamidade.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:392 BELL TEXTRON INC | APBell@textron.com
    - P02_active_relationship_finance_accounting_email:7 Agriculture and Agri-Food Canada | directdeposit.depotdirect@canada.ca
    - P02_active_relationship_finance_accounting_email:13 Crown-Indigenous Relations and Northern  | depotdirect-directdeposit@sac-isc.gc.ca
- **8 receivables-looking local part graded invoicing/AP**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:70 About | payment@birchfumigators.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:7 Texas Tech University | payment.strategies@ttu.edu
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:100 Furbaby Pet Care Saskatoon | payments@furbabysk.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:121 G&S Electric | payments@gandselectric.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:134 Lerners Lawyers | payments@lerners.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:147 Calgary Coin Gallery | payment@calgarycoin.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:184 WeirFoulds LLP | payments@weirfoulds.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:199 Whitefish River First Nation | payments@whitefishriver.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:208 Insight CPA | payments@providinginsight.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:238 Kajabi | payments.support@kajabi.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:270 Atchison Plumbing | payments@atchisonplumbing.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:283 Flashing Canines Agility Club | payments@flashingcanines.ca
- **9 shared government domain: page or quote names the body**
    - P01_GOLD_active_relationship_invoicing_AP_email:43 Canadian Space Agency | invoicing.csa-asc.facturation@canada.ca ← https://www.canada.ca/en/public-services-procurement/services/payments-to-from-g
    - P01_GOLD_active_relationship_invoicing_AP_email:514 Tennessee Department of Transportation | pln.invoices@tn.gov ← https://www.tn.gov/tdot/long-range-planning-home/longrange-administration/longra
    - P07_client_listing_finance_or_purchasing_email:24 transportation.ky.gov | finance.crcgroup@ky.gov ← https://finance.ky.gov/eProcurement/Pages/doing-business-with-the-commonwealth.a
    - P13_inferred_relationship_no_record_own_email_part1_of_6:183 Landlord and Tenant Board | ltbpayments@ontario.ca ← https://tribunalsontario.ca/ltb/contact/
- **11b quote shows the label next to the address (referee saw the address on the page)**
    - P10R_ca_domain_registration_contract_own_email_part15_of_37:401 Vancouvery Vintages | LET’S STAY IN TOUCH Keep updated with the latest and greates
- **12 evidence page on the organisation's domain (or its site)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:20 ATTIS LEBLANC | payable@attis-leblanc.com on attis-leblanc.ca (site attis-leblanc.com)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:86 PROVINCIAL HEALTH SERVICES AUTHORITY | phsainventory_apinvoices@hssbc.ca on phsa.ca (site hssbc.ca)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:91 Coca-Cola Ltd. | krinvoice@coca-cola.com on coca-colacompany.com (site coca-cola.com)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:97 Oil City Drywall North | accounting@oilcitydrywall.ca on oilcitydrywallnorth.ca (site oilcitydrywall.ca)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:104 Terumo Medical Corporation | accountspayable@terumomedical.com on terumocanada.ca (site terumomedical.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:22 Motorola Solutions | recepcionfacturas@motorolasolutions.com on web.archive.org (site motorolasolutions.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:113 WOMEN'S PLACE (ST CATHARINES & DISTRICT) | finance@gilliansplace.com on gilliansplace.ca (site gilliansplace.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:271 Canadian Research Knowledge Network | finance@crkn.ca on crkn-rcdr.ca (site crkn.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:281 dabc.ca | ap@dabc.ca on disabilityalliancebc.org (site dabc.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:282 transbec.ca | payables@transbec.ca on transbec.com (site transbec.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:305 KSAN Society | accountspayable@ksansociety.ca on ksansociety.com (site ksansociety.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:312 Courses Vintage Québec | paiements@cvqvintage.ca on coursesvintagequebec.ca (site cvqvintage.ca)
- **15 tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m)**
    - P01_GOLD_active_relationship_invoicing_AP_email:83 Municipalité de Rawdon | A with end 2026-11-10
    - P02_active_relationship_finance_accounting_email:67 Ville de Repentigny | A with end 2026-11-10
    - P04_active_relationship_general_email_part1_of_2:223 Municipalité de Saint-Calixte | A with end 2026-11-10
    - P04_active_relationship_general_email_part1_of_2:242 Municipalité de Marston-Canton | A with end 2026-11-10
    - P04_active_relationship_general_email_part1_of_2:546 Village de Sainte-Jeanne-d'Arc | A with end 2026-11-10
    - P04_active_relationship_general_email_part1_of_2:623 Municipalité de Grande-Vallée | A with end 2026-11-10
- **19 buyer name is a name (not a domain or a page title)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:70 About | About
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:71 About | About
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:106 About | About
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:38 ovs.com | ovs.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:109 loulourentals.com | loulourentals.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:115 cstx.gov | cstx.gov
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:136 efifoodequip.com | efifoodequip.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:140 mmcorp.ca | mmcorp.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:165 cpaquebec.ca | cpaquebec.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:204 gatech.edu | gatech.edu
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:229 tbdssab.ca | tbdssab.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:257 fs.ca | fs.ca
- **20 legal name is not a fragment or a platform copyright**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:20 ATTIS LEBLANC | 9395-4477 Québec inc. (the Régie du bâtiment du Québec's list of activ
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:22 BGIS O&M Solutions inc. | BGIS O&M Solutions inc. (the Régie du bâtiment du Québec's list of act
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:25 Construction et Rénovation Denis Inc. | Construction et Rénovation Denis Inc. (the Régie du bâtiment du Québec
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:26 Edmond Nolin Ltée | Edmond Nolin Ltée (the Régie du bâtiment du Québec's list of active li
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:27 Construction Finition inc. | Construction Finition inc. (the Régie du bâtiment du Québec's list of 
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:28 Daikin Applied Canada inc. | Daikin Applied Canada inc. (the Régie du bâtiment du Québec's list of 
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:29 Deblois réfrigération inc. | Deblois réfrigération inc. (the Régie du bâtiment du Québec's list of 
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:30 Dion électrique inc. | Dion électrique inc. (the Régie du bâtiment du Québec's list of active
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:31 Construction D.M. Turcotte J.M. inc. | Construction D.M. Turcotte J.M. inc. (the Régie du bâtiment du Québec'
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:32 Dyno Nobel Canada inc. | Dyno Nobel Canada inc. (the Régie du bâtiment du Québec's list of acti
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:34 Constructions Fabmec inc. | Constructions Fabmec inc. (the Régie du bâtiment du Québec's list of a
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:35 Filspec inc. | Filspec inc. (the Régie du bâtiment du Québec's list of active licence
- **22 one row per organisation name (same name twice)**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:111 Collings Insurance Brokers | 2 rows, same mail domain: collingsinsurance.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:190 Niagara Children Centre | 2 rows, same mail domain: niagarachildrenscentre.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:335 Cascades | 2 rows, same mail domain: cascades.com
    - P01_GOLD_active_relationship_invoicing_AP_email:16 Rocky View County | 2 rows, same mail domain: rockyview.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:26 University of Lethbridge | 2 rows, same mail domain: uleth.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:234 Metrolinx | 2 rows, same mail domain: metrolinx.com
    - P01_GOLD_active_relationship_invoicing_AP_email:257 City of Brantford | 2 rows, same mail domain: brantford.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:277 City of Port Moody | 2 rows, same mail domain: portmoody.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:320 City of Kitchener | 2 rows, same mail domain: kitchener.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:499 City of Edmonton | 2 rows, same mail domain: edmonton.ca
    - P02_active_relationship_finance_accounting_email:137 Ville de Princeville | 2 rows, same mail domain: princeville.quebec
    - P02_active_relationship_finance_accounting_email:440 Saint Mary's University | 2 rows, same mail domain: smu.ca
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
    - P13_inferred_relationship_no_record_own_email_part1_of_6:160 Rheinmetall AG | CA / rheinmetall.com.au
    - P13_inferred_relationship_no_record_own_email_part1_of_6:168 Westpac | CA / westpac.com.au
    - P13_inferred_relationship_no_record_own_email_part1_of_6:185 United States Postal Service | CA / usps.gov
    - P13_inferred_relationship_no_record_own_email_part1_of_6:384 Randstad Deutschland | CA / randstad.de
    - P13_inferred_relationship_no_record_own_email_part1_of_6:591 LA MAISON DES JEUNES DE PLESSISVILLE INC | QC / lycos.fr
    - P13_inferred_relationship_no_record_own_email_part1_of_6:788 The Redeemed Christian Church of God Lov | SK / loveassembly.co.uk
    - P13_inferred_relationship_no_record_own_email_part1_of_6:1285 mgmarketing.fr | QC / mgmarketing.fr
    - P13_inferred_relationship_no_record_own_email_part2_of_6:1024 KNDS | CA / knds.de
    - P13_inferred_relationship_no_record_own_email_part2_of_6:1033 The Warehouse Group | CA / thewarehousegroup.co.nz
    - P13_inferred_relationship_no_record_own_email_part2_of_6:2569 akelius.ca | CA / akelius.fr
    - P13_inferred_relationship_no_record_own_email_part2_of_6:2578 apexauctions.ca | CA / apexauctions.co.uk
- **26 currency filled when a value is filled**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:27 RENTON SCHOOL DISTRICT #403 | 332345.13 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:444 Rectorado de la Universitat de València | 12698.25 (source field: PayableAmount)
    - P01_GOLD_active_relationship_invoicing_AP_email:456 BRINKS DE COLOMBIA S.A. | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:475 University of North Dakota | 145.850 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:504 BELLEVUE, CITY OF | 35488873.2 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:512 UNIVERSITY PLACE SCHOOL DISTRICT #83 | 685477.9 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:531 North Dakota State University | 35.000 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:537 BELLEVUE SCHOOL DISTRICT #405 | 5395.88 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:543 SNOQUALMIE VALLEY SCHOOL DISTRICT #410 | 23980.42 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:550 MARYLAND STADIUM AUTHORITY | 251569.05 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:553 BANCOLOMBIA S.A. | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:564 ECOPETROL S A | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)

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
- P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email: 105
- P01T_active_service_seen_on_buyer_site_invoicing_AP_email: 334
- P01_GOLD_active_relationship_invoicing_AP_email: 625
- P02_active_relationship_finance_accounting_email: 474
- P03_active_relationship_purchasing_email: 257
- P04_active_relationship_general_email: 3887
- P05_likely_active_awarded_12_36_months_any_email: 427
- P06M_member_or_regulated_payer_of_canadian_body_other_email: 10630
- P06T_active_service_seen_on_buyer_site_other_email: 60045
- P06_client_listing_invoicing_AP_email: 312
- P07_client_listing_finance_or_purchasing_email: 838
- P08_client_listing_general_email: 26652
- P09_older_contract_or_payment_any_email: 303
- P10R_ca_domain_registration_contract_own_email: 98993
- P10_linked_from_vendor_site_any_email: 2735
- P11_any_relationship_email_not_yet_confirmed: 11585
- P12_weaker_relationship_within_5_years_own_email: 7
- P13_inferred_relationship_no_record_own_email: 18053

## Field fill across all delivered rows (value present, not `not_published`)
- buyer_website: 236262 (100.0%)
- vendor_address: 233241 (98.7%)
- vendor_website: 220494 (93.3%)
- contract_link: 218209 (92.4%)
- buyer_logo_url: 191209 (80.9%)
- award_date: 184668 (78.2%)
- buyer_address: 171286 (72.5%)
- vendor_legal_name: 158137 (66.9%)
- vendor_bn9: 146502 (62.0%)
- buyer_phone: 143127 (60.6%)
- vendor_registry_id: 141914 (60.1%)
- vendor_incorporation_date: 141872 (60.0%)
- vendor_logo_url: 108613 (46.0%)
- buyer_legal_name_as_published: 96368 (40.8%)
- vendor_phone: 78893 (33.4%)
- vendor_emails: 42610 (18.0%)
- vendor_neq: 30554 (12.9%)
- buyer_bn_as_published: 26096 (11.0%)
- end_date: 10634 (4.5%)
- contract_value: 7280 (3.1%)
- payment_terms_as_published: 4364 (1.8%)
- ap_phone: 3148 (1.3%)
- invoice_mailing_address: 2509 (1.1%)
- invoicing_requirements: 2324 (1.0%)
- po_required_as_published: 2111 (0.9%)
- invoice_portal_url: 2081 (0.9%)
- ap_contact_name_as_published: 1085 (0.5%)

## Canada-proof families
- source field: 211759; other: 24503

## Buyer types
- organisation (type not stated in the record): 139580
- company (private sector): 35205
- company (private sector) (from the organisation's name / web domain): 24944
- non-profit / association / cultural body: 14122
- government ministry / agency: 5715
- non-profit / association / cultural body (from the organisation's name / web domain): 2968
- hospital / health authority: 2586
- utility / public corporation: 2385
- municipality / local government: 1635
- municipality / local government (from the organisation's name / web domain): 1633
- university / college: 1305
- transport / transit authority: 734
- hospital / health authority (from the organisation's name / web domain): 637
- university / college (from the organisation's name / web domain): 543
- utility / public corporation (from the organisation's name / web domain): 499
- government ministry / agency (from the organisation's name / web domain): 441
- religious organisation (from the organisation's name / web domain): 312
- First Nation / Indigenous government: 285
- transport / transit authority (from the organisation's name / web domain): 239
- First Nation / Indigenous government (from the organisation's name / web domain): 193
- school board / school district: 187
- library (from the organisation's name / web domain): 43
- school board / school district (from the organisation's name / web domain): 31
- US government body (federal, state or local): 29
- US city / county / local government: 11

## DMARC posture of the delivered mailboxes
- no DMARC record: 98565
- v=DMARC1; p=none (monitor only, no enforcement): 91846
- p=quarantine: 30500
- p=reject: 15098
- invalid DMARC record: 182
- DNS lookup failed: 71
