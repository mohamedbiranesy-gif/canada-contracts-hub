# Deep audit — 258661 delivered rows in 18 packages (102 files), 2026-11-11

Result: **PASS** — 11 hard checks, 17 soft checks; hard failures: 0. Every flagged row is listed in `audit_flags.csv` with its reasons.

| # | check | kind | rows flagged | verdict |
|---|---|---|---|---|
| 1 | header: identical columns in every file (106 since 2026-11-06) | hard | 0 | PASS |
| 2 | mailbox syntax | hard | 0 | PASS |
| 3 | mailbox referee-confirmed (all but P11) | hard | 0 | PASS |
| 4 | mail server (MX or A) on the mailbox domain | hard | 0 | PASS |
| 4b | mail server not yet checked (row newer than the last DNS pass) | soft | 192504 | REVIEW |
| 5 | no webmail domain | hard | 0 | PASS |
| 6 | no person-like local part | hard | 0 | PASS |
| 7 | role word in the local part | soft | 22284 | REVIEW |
| 8 | receivables-looking local part graded invoicing/AP | soft | 69 | REVIEW |
| 9 | shared government domain: page or quote names the body | soft | 4 | REVIEW |
| 10 | regional token of a multinational on a differently-located body | soft | 0 | PASS |
| 11 | quote contains the address | hard | 0 | PASS |
| 11b | quote shows the label next to the address (referee saw the address on the page) | soft | 1 | REVIEW |
| 12 | evidence page on the organisation's domain (or its site) | soft | 12639 | REVIEW |
| 13 | email_type label matches grade | hard | 0 | PASS |
| 14 | DMARC / SPF / provider columns filled | soft | 0 | PASS |
| 15 | tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m) | soft | 6 | REVIEW |
| 16 | vendor named and Canada proof present | hard | 0 | PASS |
| 17 | Canada proof is a source field or the vendor's site (never a name) | soft | 0 | PASS |
| 18 | record link present for dated-record tiers | soft | 0 | PASS |
| 19 | buyer name is a name (not a domain or a page title) | soft | 29397 | REVIEW |
| 20 | legal name is not a fragment or a platform copyright | soft | 59 | REVIEW |
| 21 | one row per mailbox | hard | 0 | PASS |
| 22 | one row per organisation name (same name twice) | soft | 71 | REVIEW |
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
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:21 Cameco Corporation | ap_cameco@cameco.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:49 New Relic | ap_ireland@newrelic.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:117 Scouts de Dieppe | paiement@scoutsdedieppe.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:166 Keyera | ap_inquiries@keyera.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:210 Ecce Terra | paiement@ecceterra.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:304 cvqvintage.ca | paiements@cvqvintage.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:276 Town of Oakville | ap_inquiries@oakville.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:300 University of Saskatchewan | connectionpoint@usask.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:302 Miami-Dade County (business unit CU05010 | invsubp@miamidade.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:392 BELL TEXTRON INC | APBell@textron.com
    - P02_active_relationship_finance_accounting_email:7 Agriculture and Agri-Food Canada | directdeposit.depotdirect@canada.ca
- **8 receivables-looking local part graded invoicing/AP**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:65 About | payment@birchfumigators.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:8 Texas Tech University | payment.strategies@ttu.edu
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:101 Furbaby Pet Care Saskatoon | payments@furbabysk.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:121 G&S Electric | payments@gandselectric.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:133 Lerners Lawyers | payments@lerners.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:146 Calgary Coin Gallery | payment@calgarycoin.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:182 WeirFoulds LLP | payments@weirfoulds.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:196 Whitefish River First Nation | payments@whitefishriver.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:205 Insight LLP CPA | payments@providinginsight.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:233 Kajabi | payments.support@kajabi.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:264 Atchison Plumbing | payments@atchisonplumbing.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:275 Flashing Canines Agility Club | payments@flashingcanines.ca
- **9 shared government domain: page or quote names the body**
    - P01_GOLD_active_relationship_invoicing_AP_email:43 Canadian Space Agency | invoicing.csa-asc.facturation@canada.ca ← https://www.canada.ca/en/public-services-procurement/services/payments-to-from-g
    - P01_GOLD_active_relationship_invoicing_AP_email:514 Tennessee Department of Transportation | pln.invoices@tn.gov ← https://www.tn.gov/tdot/long-range-planning-home/longrange-administration/longra
    - P07_client_listing_finance_or_purchasing_email:23 transportation.ky.gov | finance.crcgroup@ky.gov ← https://finance.ky.gov/eProcurement/Pages/doing-business-with-the-commonwealth.a
    - P13_inferred_relationship_no_record_own_email_part1_of_7:178 Landlord and Tenant Board | ltbpayments@ontario.ca ← https://tribunalsontario.ca/ltb/contact/
- **11b quote shows the label next to the address (referee saw the address on the page)**
    - P10R_ca_domain_registration_contract_own_email_part15_of_38:2137 Vancouvery Vintages | LET’S STAY IN TOUCH Keep updated with the latest and greates
- **12 evidence page on the organisation's domain (or its site)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:18 ATTIS LEBLANC | payable@attis-leblanc.com on attis-leblanc.ca (site attis-leblanc.com)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:80 PROVINCIAL HEALTH SERVICES AUTHORITY | phsainventory_apinvoices@hssbc.ca on phsa.ca (site hssbc.ca)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:85 Coca-Cola Ltd. | krinvoice@coca-cola.com on coca-colacompany.com (site coca-cola.com)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:90 Oil City Drywall North | accounting@oilcitydrywall.ca on oilcitydrywallnorth.ca (site oilcitydrywall.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:23 Motorola Solutions | recepcionfacturas@motorolasolutions.com on web.archive.org (site motorolasolutions.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:114 WOMEN'S PLACE (ST CATHARINES & DISTRICT) | finance@gilliansplace.com on gilliansplace.ca (site gilliansplace.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:182 WeirFoulds LLP | payments@weirfoulds.com on weirfoulds.ca (site weirfoulds.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:265 Canadian Research Knowledge Network | finance@crkn.ca on crkn-rcdr.ca (site crkn.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:273 dabc.ca | ap@dabc.ca on disabilityalliancebc.org (site dabc.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:274 transbec.ca | payables@transbec.ca on transbec.com (site transbec.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:297 KSAN Society | accountspayable@ksansociety.ca on ksansociety.com (site ksansociety.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:304 cvqvintage.ca | paiements@cvqvintage.ca on coursesvintagequebec.ca (site cvqvintage.ca)
- **15 tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m)**
    - P01_GOLD_active_relationship_invoicing_AP_email:83 Municipalité de Rawdon | A with end 2026-11-10
    - P02_active_relationship_finance_accounting_email:67 Ville de Repentigny | A with end 2026-11-10
    - P04_active_relationship_general_email_part1_of_2:223 Municipalité de Saint-Calixte | A with end 2026-11-10
    - P04_active_relationship_general_email_part1_of_2:242 Municipalité de Marston-Canton | A with end 2026-11-10
    - P04_active_relationship_general_email_part1_of_2:546 Village de Sainte-Jeanne-d'Arc | A with end 2026-11-10
    - P04_active_relationship_general_email_part1_of_2:623 Municipalité de Grande-Vallée | A with end 2026-11-10
- **19 buyer name is a name (not a domain or a page title)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:65 About | About
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:66 About | About
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:39 ovs.com | ovs.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:110 loulourentals.com | loulourentals.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:116 cstx.gov | cstx.gov
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:135 efifoodequip.com | efifoodequip.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:139 mmcorp.ca | mmcorp.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:163 cpaquebec.ca | cpaquebec.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:201 gatech.edu | gatech.edu
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:226 tbdssab.ca | tbdssab.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:228 dgchait.com | dgchait.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:245 chambresag.com | chambresag.com
- **20 legal name is not a fragment or a platform copyright**
    - P05_likely_active_awarded_12_36_months_any_email:59 Ameren Illinois Company | Ameren Corporation and/or its suppliers
    - P05_likely_active_awarded_12_36_months_any_email:340 LOVE WORTH FINDING MINISTRIES INC | LLC. 800-274-5683 2941 Kate Bond Rd, Memphis, TN 38133 CONNECT WITH LW
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part5_of_6:757 +ARTHRI-PLUS INC. | +ARTHRI-PLUS INC. (the Canadian trademarks register (owner of record),
    - P06T_active_service_seen_on_buyer_site_other_email_part11_of_24:2372 Beet & Yarrow | Introduction Welcome to Beet & Yarrow. Beet & Yarrow (stated on https:
    - P06T_active_service_seen_on_buyer_site_other_email_part12_of_24:925 LTD Commodities | LTD Commodities
    - P06T_active_service_seen_on_buyer_site_other_email_part15_of_24:1994 Prime Aesthetics | Inc. 2. Aesthetic Surgery Education and Research Foundation (stated on
    - P06T_active_service_seen_on_buyer_site_other_email_part15_of_24:2728 The Barkshire Club | Introduction Welcome to The Barkshire Club (stated on https://thebarks
    - P06T_active_service_seen_on_buyer_site_other_email_part16_of_24:1626 La Leche League Canada | LLC Leaders will use the words individuals prefer in personal communic
    - P06T_active_service_seen_on_buyer_site_other_email_part17_of_24:783 Project TEMBO | Introduction Welcome to TEMBO Canada (stated on https://www.projectemb
    - P06T_active_service_seen_on_buyer_site_other_email_part22_of_24:1246 Wellness Way | the WELLNESS WAY co Inc. (as registered: Corporations Canada (open dat
    - P06T_active_service_seen_on_buyer_site_other_email_part22_of_24:1728 Landscaping | LTD Landscaping Inc. (as registered: Corporations Canada (open data), 
    - P06T_active_service_seen_on_buyer_site_other_email_part24_of_24:3058 Feb 2th, 2024 Acceptance of Terms Welcom | Feb 2th, 2024 Acceptance of Terms Welcome to NTWIST (stated on https:/
- **22 one row per organisation name (same name twice)**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:68 City of Pitt Meadows | 2 rows, same mail domain: pittmeadows.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:112 Collings Insurance | 2 rows, same mail domain: collingsinsurance.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:188 Niagara Children Centre | 2 rows, same mail domain: niagarachildrenscentre.com
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
    - P13_inferred_relationship_no_record_own_email_part1_of_7:155 Rheinmetall AG | CA / rheinmetall.com.au
    - P13_inferred_relationship_no_record_own_email_part1_of_7:163 Westpac | CA / westpac.com.au
    - P13_inferred_relationship_no_record_own_email_part1_of_7:180 United States Postal Service | CA / usps.gov
    - P13_inferred_relationship_no_record_own_email_part1_of_7:377 Randstad Deutschland | CA / randstad.de
    - P13_inferred_relationship_no_record_own_email_part1_of_7:573 LA MAISON DES JEUNES DE PLESSISVILLE INC | QC / lycos.fr
    - P13_inferred_relationship_no_record_own_email_part1_of_7:762 The Redeemed Christian Church of God Lov | SK / loveassembly.co.uk
    - P13_inferred_relationship_no_record_own_email_part1_of_7:1242 mgmarketing.fr | QC / mgmarketing.fr
    - P13_inferred_relationship_no_record_own_email_part2_of_7:1321 KNDS | CA / knds.de
    - P13_inferred_relationship_no_record_own_email_part2_of_7:1330 The Warehouse Group | CA / thewarehousegroup.co.nz
    - P13_inferred_relationship_no_record_own_email_part3_of_7:300 Akelius Real Estate Management LLC | CA / akelius.fr
    - P13_inferred_relationship_no_record_own_email_part3_of_7:309 Apex Auctions Limited | CA / apexauctions.co.uk
- **26 currency filled when a value is filled**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:28 RENTON SCHOOL DISTRICT #403 | 332345.13 (source field: amount)
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
- P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email: 125
- P01T_active_service_seen_on_buyer_site_invoicing_AP_email: 398
- P01_GOLD_active_relationship_invoicing_AP_email: 625
- P02_active_relationship_finance_accounting_email: 471
- P03_active_relationship_purchasing_email: 257
- P04_active_relationship_general_email: 3833
- P05_likely_active_awarded_12_36_months_any_email: 422
- P06M_member_or_regulated_payer_of_canadian_body_other_email: 13084
- P06T_active_service_seen_on_buyer_site_other_email: 74208
- P06_client_listing_invoicing_AP_email: 295
- P07_client_listing_finance_or_purchasing_email: 800
- P08_client_listing_general_email: 25539
- P09_older_contract_or_payment_any_email: 295
- P10R_ca_domain_registration_contract_own_email: 100545
- P10_linked_from_vendor_site_any_email: 2642
- P11_any_relationship_email_not_yet_confirmed: 17418
- P12_weaker_relationship_within_5_years_own_email: 7
- P13_inferred_relationship_no_record_own_email: 17697

## Field fill across all delivered rows (value present, not `not_published`)
- buyer_website: 258661 (100.0%)
- vendor_address: 256414 (99.1%)
- vendor_website: 249772 (96.6%)
- contract_link: 240964 (93.2%)
- vendor_legal_name: 213807 (82.7%)
- award_date: 208747 (80.7%)
- buyer_logo_url: 198314 (76.7%)
- buyer_address: 188883 (73.0%)
- vendor_bn9: 157392 (60.8%)
- vendor_registry_id: 156837 (60.6%)
- vendor_incorporation_date: 156799 (60.6%)
- buyer_phone: 152174 (58.8%)
- vendor_logo_url: 135707 (52.5%)
- buyer_legal_name_as_published: 116713 (45.1%)
- vendor_phone: 98416 (38.0%)
- vendor_emails: 47978 (18.5%)
- vendor_neq: 42652 (16.5%)
- buyer_bn_as_published: 25590 (9.9%)
- end_date: 12449 (4.8%)
- contract_value: 6956 (2.7%)
- payment_terms_as_published: 4453 (1.7%)
- ap_phone: 3144 (1.2%)
- invoice_mailing_address: 2514 (1.0%)
- invoicing_requirements: 2321 (0.9%)
- po_required_as_published: 2086 (0.8%)
- invoice_portal_url: 2069 (0.8%)
- ap_contact_name_as_published: 1096 (0.4%)

## Canada-proof families
- source field: 234490; other: 24171

## Buyer types
- organisation (type not stated in the record): 143451
- company (private sector): 40592
- company (private sector) (from the organisation's name / web domain): 36407
- non-profit / association / cultural body: 14701
- government ministry / agency: 6029
- non-profit / association / cultural body (from the organisation's name / web domain): 3156
- hospital / health authority: 2656
- utility / public corporation: 2583
- municipality / local government: 1677
- municipality / local government (from the organisation's name / web domain): 1621
- university / college: 1381
- transport / transit authority: 773
- hospital / health authority (from the organisation's name / web domain): 680
- university / college (from the organisation's name / web domain): 547
- utility / public corporation (from the organisation's name / web domain): 542
- government ministry / agency (from the organisation's name / web domain): 465
- religious organisation (from the organisation's name / web domain): 330
- First Nation / Indigenous government: 298
- transport / transit authority (from the organisation's name / web domain): 252
- First Nation / Indigenous government (from the organisation's name / web domain): 209
- school board / school district: 190
- library (from the organisation's name / web domain): 48
- school board / school district (from the organisation's name / web domain): 33
- US government body (federal, state or local): 29
- US city / county / local government: 11

## DMARC posture of the delivered mailboxes
- no DMARC record: 106502
- v=DMARC1; p=none (monitor only, no enforcement): 101858
- p=quarantine: 33382
- p=reject: 16632
- invalid DMARC record: 202
- DNS lookup failed: 85
