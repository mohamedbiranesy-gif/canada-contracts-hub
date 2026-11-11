# Deep audit — 258733 delivered rows in 18 packages (110 files), 2026-11-11

Result: **PASS** — 11 hard checks, 17 soft checks; hard failures: 0. Every flagged row is listed in `audit_flags.csv` with its reasons.

| # | check | kind | rows flagged | verdict |
|---|---|---|---|---|
| 1 | header: identical columns in every file (106 since 2026-11-06) | hard | 0 | PASS |
| 2 | mailbox syntax | hard | 0 | PASS |
| 3 | mailbox referee-confirmed (all but P11) | hard | 0 | PASS |
| 4 | mail server (MX or A) on the mailbox domain | hard | 0 | PASS |
| 4b | mail server not yet checked (row newer than the last DNS pass) | soft | 192576 | REVIEW |
| 5 | no webmail domain | hard | 0 | PASS |
| 6 | no person-like local part | hard | 0 | PASS |
| 7 | role word in the local part | soft | 22295 | REVIEW |
| 8 | receivables-looking local part graded invoicing/AP | soft | 69 | REVIEW |
| 9 | shared government domain: page or quote names the body | soft | 4 | REVIEW |
| 10 | regional token of a multinational on a differently-located body | soft | 0 | PASS |
| 11 | quote contains the address | hard | 0 | PASS |
| 11b | quote shows the label next to the address (referee saw the address on the page) | soft | 1 | REVIEW |
| 12 | evidence page on the organisation's domain (or its site) | soft | 12650 | REVIEW |
| 13 | email_type label matches grade | hard | 0 | PASS |
| 14 | DMARC / SPF / provider columns filled | soft | 0 | PASS |
| 15 | tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m) | soft | 6 | REVIEW |
| 16 | vendor named and Canada proof present | hard | 0 | PASS |
| 17 | Canada proof is a source field or the vendor's site (never a name) | soft | 0 | PASS |
| 18 | record link present for dated-record tiers | soft | 0 | PASS |
| 19 | buyer name is a name (not a domain or a page title) | soft | 27750 | REVIEW |
| 20 | legal name is not a fragment or a platform copyright | soft | 64 | REVIEW |
| 21 | one row per mailbox | hard | 0 | PASS |
| 22 | one row per organisation name (same name twice) | soft | 73 | REVIEW |
| 23 | one row per site domain (two rows, different mailboxes, same domain) | soft | 64 | REVIEW |
| 24 | no blank cell | hard | 0 | PASS |
| 25 | jurisdiction vs mailbox top-level domain | soft | 80 | REVIEW |
| 26 | currency filled when a value is filled | soft | 50 | REVIEW |

## Examples of flagged rows (first 12 per check)
- **4b mail server not yet checked (row newer than the last DNS pass)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:2 Algonquin College | algonquincollege.co
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:18 ATTIS LEBLANC | attis-leblanc.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:22 Cologix Canada inc. | cologix.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:24 Edmond Nolin Ltée | constructionenl.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:26 Daikin Applied Canada inc. | daikinapplied.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:27 Deblois réfrigération inc. | debloisrefrigeration.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:29 Construction D.M. Turcotte J.M. inc. | dmturcotte.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:30 Dyno Nobel Canada inc. | dynonobel.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:32 Constructions Fabmec inc. | fabmec.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:33 Filspec inc. | filspec.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:35 Électricité de la Capitale Inc. | groleaudev.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:36 Groupe Lalonde inc. | groupelalonde.com
- **7 role word in the local part**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:122 Taylor-Listug, Inc. | ap_group@taylorguitars.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:39 Scouts de Dieppe | paiement@scoutsdedieppe.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:95 cvqvintage.ca | paiements@cvqvintage.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:167 Cameco Corporation | ap_cameco@cameco.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:191 New Relic | ap_ireland@newrelic.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:250 Keyera | ap_inquiries@keyera.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:353 Ecce Terra | paiement@ecceterra.com
    - P01_GOLD_active_relationship_invoicing_AP_email:276 Town of Oakville | ap_inquiries@oakville.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:300 University of Saskatchewan | connectionpoint@usask.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:302 Miami-Dade County (business unit CU05010 | invsubp@miamidade.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:392 BELL TEXTRON INC | APBell@textron.com
    - P02_active_relationship_finance_accounting_email:7 Agriculture and Agri-Food Canada | directdeposit.depotdirect@canada.ca
- **8 receivables-looking local part graded invoicing/AP**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:65 birchfumigators.ca | payment@birchfumigators.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:8 Texas Tech University | payment.strategies@ttu.edu
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:17 Calgary Coin Gallery | payment@calgarycoin.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:33 Awninginabox.ca | payment@awninginabox.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:43 Lerners Lawyers | payments@lerners.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:55 WeirFoulds LLP | payments@weirfoulds.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:59 Whitefish River First Nation | payments@whitefishriver.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:79 Flashing Canines Agility Club | payments@flashingcanines.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:86 Connelly & Koshy Professional Corporatio | payments@ck-ca.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:94 Penner Auctions | morden.payments@pennerauctions.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:262 Kajabi | payments.support@kajabi.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:308 Facility Solutions Canada Limited | payments@facilitysolutionscanada.ca
- **9 shared government domain: page or quote names the body**
    - P01_GOLD_active_relationship_invoicing_AP_email:43 Canadian Space Agency | invoicing.csa-asc.facturation@canada.ca ← https://www.canada.ca/en/public-services-procurement/services/payments-to-from-g
    - P01_GOLD_active_relationship_invoicing_AP_email:514 Tennessee Department of Transportation | pln.invoices@tn.gov ← https://www.tn.gov/tdot/long-range-planning-home/longrange-administration/longra
    - P07_client_listing_finance_or_purchasing_email:22 transportation.ky.gov | finance.crcgroup@ky.gov ← https://finance.ky.gov/eProcurement/Pages/doing-business-with-the-commonwealth.a
    - P13_inferred_relationship_no_record_own_email_part1_of_7:177 Landlord and Tenant Board | ltbpayments@ontario.ca ← https://tribunalsontario.ca/ltb/contact/
- **11b quote shows the label next to the address (referee saw the address on the page)**
    - P10R_ca_domain_registration_contract_own_email_part17_of_42:876 Vancouvery Vintages | LET’S STAY IN TOUCH Keep updated with the latest and greates
- **12 evidence page on the organisation's domain (or its site)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:18 ATTIS LEBLANC | payable@attis-leblanc.com on attis-leblanc.ca (site attis-leblanc.com)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:80 PROVINCIAL HEALTH SERVICES AUTHORITY | phsainventory_apinvoices@hssbc.ca on phsa.ca (site hssbc.ca)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:85 Coca-Cola Ltd. | krinvoice@coca-cola.com on coca-colacompany.com (site coca-cola.com)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:90 Oil City Drywall North | accounting@oilcitydrywall.ca on oilcitydrywallnorth.ca (site oilcitydrywall.ca)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:127 Birth Supplies Canada | ap@birthsuppliescanada.ca on midwiferysupplies.ca (site birthsuppliescanada.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:26 Anna's Garden, Home & Wellness | accountspayable@annasflowers.ca on shopannas.ca (site annasflowers.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:55 WeirFoulds LLP | payments@weirfoulds.com on weirfoulds.ca (site weirfoulds.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:95 cvqvintage.ca | paiements@cvqvintage.ca on coursesvintagequebec.ca (site cvqvintage.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:99 Capital Regional District | accountspayable@crd.bc.ca on crd.ca (site crd.bc.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:102 regieincendiekam-ouest.ca | payables@regieincendiekam-ouest.ca on regieincendiekam-ouest.com (site regieincendiekam-ouest.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:115 ibiosolutions.com | payables@ibiosolutions.com on immunebiosolutions.com (site ibiosolutions.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:134 nscminerals.com | accounting@nscminerals.com on nscminerals.ca (site nscminerals.com)
- **15 tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m)**
    - P01_GOLD_active_relationship_invoicing_AP_email:83 Municipalité de Rawdon | A with end 2026-11-10
    - P02_active_relationship_finance_accounting_email:67 Ville de Repentigny | A with end 2026-11-10
    - P04_active_relationship_general_email_part1_of_2:223 Municipalité de Saint-Calixte | A with end 2026-11-10
    - P04_active_relationship_general_email_part1_of_2:242 Municipalité de Marston-Canton | A with end 2026-11-10
    - P04_active_relationship_general_email_part1_of_2:546 Village de Sainte-Jeanne-d'Arc | A with end 2026-11-10
    - P04_active_relationship_general_email_part1_of_2:623 Municipalité de Grande-Vallée | A with end 2026-11-10
- **19 buyer name is a name (not a domain or a page title)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:65 birchfumigators.ca | birchfumigators.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:66 dfcdiesel.com | dfcdiesel.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:11 ovs.com | ovs.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:21 fs.ca | fs.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:33 Awninginabox.ca | Awninginabox.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:49 efifoodequip.com | efifoodequip.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:51 cpaquebec.ca | cpaquebec.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:88 lpsg.ca | lpsg.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:95 cvqvintage.ca | cvqvintage.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:97 apsurveys.ca | apsurveys.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:102 regieincendiekam-ouest.ca | regieincendiekam-ouest.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:106 ctwater.com | ctwater.com
- **20 legal name is not a fragment or a platform copyright**
    - P05_likely_active_awarded_12_36_months_any_email:59 Ameren Illinois Company | Ameren Corporation and/or its suppliers
    - P05_likely_active_awarded_12_36_months_any_email:340 LOVE WORTH FINDING MINISTRIES INC | LLC. 800-274-5683 2941 Kate Bond Rd, Memphis, TN 38133 CONNECT WITH LW
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part5_of_6:642 +ARTHRI-PLUS INC. | +ARTHRI-PLUS INC. (the Canadian trademarks register (owner of record),
    - P06T_active_service_seen_on_buyer_site_other_email_part13_of_27:1728 Project TEMBO | Introduction Welcome to TEMBO Canada (stated on https://www.projectemb
    - P06T_active_service_seen_on_buyer_site_other_email_part17_of_27:2563 La Leche League Canada | LLC Leaders will use the words individuals prefer in personal communic
    - P06T_active_service_seen_on_buyer_site_other_email_part18_of_27:1421 Reimer Bros Trucking Ltd. | Ltd
    - P06T_active_service_seen_on_buyer_site_other_email_part19_of_27:1159 DNN Corp | DNN Corp and/or its suppliers
    - P06T_active_service_seen_on_buyer_site_other_email_part21_of_27:2667 Landscaping | LTD Landscaping Inc. (as registered: Corporations Canada (open data), 
    - P06T_active_service_seen_on_buyer_site_other_email_part23_of_27:957 Punta Cana Spa | Introduction Welcome to Punta Cana Spa (stated on https://puntacanaspa
    - P06T_active_service_seen_on_buyer_site_other_email_part23_of_27:2439 Caleb Creations | Introduction Welcome to Caleb Creations (stated on https://calebcreati
    - P06T_active_service_seen_on_buyer_site_other_email_part24_of_27:1324 The Flag Shop | September 28th, 2025 Welcome to The Flag Shop (stated on https://flag-
    - P06T_active_service_seen_on_buyer_site_other_email_part25_of_27:2193 Toronto Comedy Festival | Introduction Welcome to the Toronto Comedy Festival (stated on https:/
- **22 one row per organisation name (same name twice)**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:57 Niagara Children Centre | 2 rows, same mail domain: niagarachildrenscentre.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:209 City of Pitt Meadows | 2 rows, same mail domain: pittmeadows.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:241 Collings Insurance | 2 rows, same mail domain: collingsinsurance.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:398 Cascades | 2 rows, same mail domain: cascades.com
    - P01_GOLD_active_relationship_invoicing_AP_email:16 Rocky View County | 2 rows, same mail domain: rockyview.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:26 University of Lethbridge | 2 rows, same mail domain: uleth.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:234 Metrolinx | 2 rows, same mail domain: metrolinx.com
    - P01_GOLD_active_relationship_invoicing_AP_email:257 City of Brantford | 2 rows, same mail domain: brantford.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:277 City of Port Moody | 2 rows, same mail domain: portmoody.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:320 City of Kitchener | 2 rows, same mail domain: kitchener.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:499 City of Edmonton | 2 rows, same mail domain: edmonton.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:619 Nicola Valley Institute of Technology | 2 rows, same mail domain: nvit.ca
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
    - P13_inferred_relationship_no_record_own_email_part1_of_7:154 Rheinmetall AG | CA / rheinmetall.com.au
    - P13_inferred_relationship_no_record_own_email_part1_of_7:162 Westpac | CA / westpac.com.au
    - P13_inferred_relationship_no_record_own_email_part1_of_7:179 United States Postal Service | CA / usps.gov
    - P13_inferred_relationship_no_record_own_email_part1_of_7:375 Randstad Deutschland | CA / randstad.de
    - P13_inferred_relationship_no_record_own_email_part1_of_7:571 LA MAISON DES JEUNES DE PLESSISVILLE INC | QC / lycos.fr
    - P13_inferred_relationship_no_record_own_email_part1_of_7:760 The Redeemed Christian Church of God Lov | SK / loveassembly.co.uk
    - P13_inferred_relationship_no_record_own_email_part1_of_7:1239 mgmarketing.fr | QC / mgmarketing.fr
    - P13_inferred_relationship_no_record_own_email_part2_of_7:1320 KNDS | CA / knds.de
    - P13_inferred_relationship_no_record_own_email_part2_of_7:1329 The Warehouse Group | CA / thewarehousegroup.co.nz
    - P13_inferred_relationship_no_record_own_email_part3_of_7:309 Akelius Real Estate Management LLC | CA / akelius.fr
    - P13_inferred_relationship_no_record_own_email_part3_of_7:318 Apex Auctions Limited | CA / apexauctions.co.uk
- **26 currency filled when a value is filled**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:174 RENTON SCHOOL DISTRICT #403 | 332345.13 (source field: amount)
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
- P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email: 126
- P01T_active_service_seen_on_buyer_site_invoicing_AP_email: 398
- P01_GOLD_active_relationship_invoicing_AP_email: 625
- P02_active_relationship_finance_accounting_email: 471
- P03_active_relationship_purchasing_email: 257
- P04_active_relationship_general_email: 3823
- P05_likely_active_awarded_12_36_months_any_email: 422
- P06M_member_or_regulated_payer_of_canadian_body_other_email: 13201
- P06T_active_service_seen_on_buyer_site_other_email: 75065
- P06_client_listing_invoicing_AP_email: 295
- P07_client_listing_finance_or_purchasing_email: 793
- P08_client_listing_general_email: 25303
- P09_older_contract_or_payment_any_email: 295
- P10R_ca_domain_registration_contract_own_email: 99941
- P10_linked_from_vendor_site_any_email: 2633
- P11_any_relationship_email_not_yet_confirmed: 17455
- P12_weaker_relationship_within_5_years_own_email: 7
- P13_inferred_relationship_no_record_own_email: 17623

## Field fill across all delivered rows (value present, not `not_published`)
- buyer_website: 258733 (100.0%)
- vendor_address: 256558 (99.2%)
- vendor_website: 249794 (96.5%)
- contract_link: 241110 (93.2%)
- buyer_logo_url: 221899 (85.8%)
- vendor_legal_name: 216949 (83.9%)
- award_date: 209156 (80.8%)
- buyer_address: 190832 (73.8%)
- buyer_phone: 161669 (62.5%)
- vendor_bn9: 158331 (61.2%)
- vendor_registry_id: 157904 (61.0%)
- vendor_incorporation_date: 157866 (61.0%)
- vendor_logo_url: 141294 (54.6%)
- buyer_legal_name_as_published: 125012 (48.3%)
- vendor_phone: 100640 (38.9%)
- vendor_emails: 49463 (19.1%)
- vendor_neq: 44061 (17.0%)
- buyer_bn_as_published: 25466 (9.8%)
- end_date: 12545 (4.8%)
- contract_value: 7021 (2.7%)
- payment_terms_as_published: 4380 (1.7%)
- ap_phone: 3137 (1.2%)
- invoice_mailing_address: 2512 (1.0%)
- invoicing_requirements: 2317 (0.9%)
- po_required_as_published: 2072 (0.8%)
- invoice_portal_url: 2061 (0.8%)
- ap_contact_name_as_published: 1088 (0.4%)

## Canada-proof families
- source field: 234446; other: 24287

## Buyer types
- organisation (type not stated in the record): 138669
- company (private sector): 41453
- company (private sector) (from the organisation's name / web domain): 39720
- non-profit / association / cultural body: 14858
- government ministry / agency: 6095
- non-profit / association / cultural body (from the organisation's name / web domain): 3400
- hospital / health authority: 2684
- utility / public corporation: 2611
- municipality / local government: 1685
- municipality / local government (from the organisation's name / web domain): 1661
- university / college: 1392
- transport / transit authority: 778
- hospital / health authority (from the organisation's name / web domain): 704
- university / college (from the organisation's name / web domain): 565
- utility / public corporation (from the organisation's name / web domain): 549
- government ministry / agency (from the organisation's name / web domain): 477
- religious organisation (from the organisation's name / web domain): 344
- First Nation / Indigenous government: 299
- transport / transit authority (from the organisation's name / web domain): 258
- First Nation / Indigenous government (from the organisation's name / web domain): 217
- school board / school district: 191
- library (from the organisation's name / web domain): 49
- school board / school district (from the organisation's name / web domain): 34
- US government body (federal, state or local): 29
- US city / county / local government: 11

## DMARC posture of the delivered mailboxes
- no DMARC record: 106529
- v=DMARC1; p=none (monitor only, no enforcement): 101896
- p=quarantine: 33389
- p=reject: 16637
- invalid DMARC record: 202
- DNS lookup failed: 80
