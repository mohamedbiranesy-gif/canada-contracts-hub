# Deep audit — 206885 delivered rows in 18 packages (92 files), 2026-11-12

Result: **FAIL** — 11 hard checks, 17 soft checks; hard failures: 1. Every flagged row is listed in `audit_flags.csv` with its reasons.

| # | check | kind | rows flagged | verdict |
|---|---|---|---|---|
| 1 | header: identical columns in every file (106 since 2026-11-06) | hard | 1 | FAIL |
| 2 | mailbox syntax | hard | 0 | PASS |
| 3 | mailbox referee-confirmed (all but P11) | hard | 0 | PASS |
| 4 | mail server (MX or A) on the mailbox domain | hard | 0 | PASS |
| 4b | mail server not yet checked (row newer than the last DNS pass) | soft | 156146 | REVIEW |
| 5 | no webmail domain | hard | 0 | PASS |
| 6 | no person-like local part | hard | 0 | PASS |
| 7 | role word in the local part | soft | 15217 | REVIEW |
| 8 | receivables-looking local part graded invoicing/AP | soft | 61 | REVIEW |
| 9 | shared government domain: page or quote names the body | soft | 3 | REVIEW |
| 10 | regional token of a multinational on a differently-located body | soft | 0 | PASS |
| 11 | quote contains the address | hard | 0 | PASS |
| 11b | quote shows the label next to the address (referee saw the address on the page) | soft | 0 | PASS |
| 12 | evidence page on the organisation's domain (or its site) | soft | 9385 | REVIEW |
| 13 | email_type label matches grade | hard | 0 | PASS |
| 14 | DMARC / SPF / provider columns filled | soft | 24801 | REVIEW |
| 15 | tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m) | soft | 3 | REVIEW |
| 16 | vendor named and Canada proof present | hard | 0 | PASS |
| 17 | Canada proof is a source field or the vendor's site (never a name) | soft | 0 | PASS |
| 18 | record link present for dated-record tiers | soft | 0 | PASS |
| 19 | buyer name is a name (not a domain or a page title) | soft | 21954 | REVIEW |
| 20 | legal name is not a fragment or a platform copyright | soft | 43 | REVIEW |
| 21 | one row per mailbox | hard | 0 | PASS |
| 22 | one row per organisation name (same name twice) | soft | 96 | REVIEW |
| 23 | one row per site domain (two rows, different mailboxes, same domain) | soft | 64 | REVIEW |
| 24 | no blank cell | hard | 0 | PASS |
| 25 | jurisdiction vs mailbox top-level domain | soft | 60 | REVIEW |
| 26 | currency filled when a value is filled | soft | 51 | REVIEW |

## Examples of flagged rows (first 12 per check)
- **1 header: identical columns in every file (106 since 2026-11-06)**
    - files | 2 distinct headers; widths [0, 248]
- **4b mail server not yet checked (row newer than the last DNS pass)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:2 Algonquin College | algonquincollege.co
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:19 ATTIS LEBLANC | attis-leblanc.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:23 Cologix Canada inc. | cologix.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:25 Edmond Nolin Ltée | constructionenl.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:28 Daikin Applied Canada inc. | daikinapplied.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:29 Deblois réfrigération inc. | debloisrefrigeration.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:31 Construction D.M. Turcotte J.M. inc. | dmturcotte.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:32 Dyno Nobel Canada inc. | dynonobel.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:34 Constructions Fabmec inc. | fabmec.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:35 Filspec inc. | filspec.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:37 Électricité de la Capitale Inc. | groleaudev.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:38 Groupe Lalonde inc. | groupelalonde.com
- **7 role word in the local part**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:121 Taylor-Listug, Inc. | ap_group@taylorguitars.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:95 Cameco Corporation | ap_cameco@cameco.com
    - P01_GOLD_active_relationship_invoicing_AP_email:276 Town of Oakville | ap_inquiries@oakville.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:300 University of Saskatchewan | connectionpoint@usask.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:302 Miami-Dade County (business unit CU05010 | invsubp@miamidade.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:392 BELL TEXTRON INC | APBell@textron.com
    - P02_active_relationship_finance_accounting_email:7 Agriculture and Agri-Food Canada | directdeposit.depotdirect@canada.ca
    - P02_active_relationship_finance_accounting_email:13 Crown-Indigenous Relations and Northern  | depotdirect-directdeposit@sac-isc.gc.ca
    - P02_active_relationship_finance_accounting_email:14 Department of Justice Canada | mdv_dpf@justice.gc.ca
    - P02_active_relationship_finance_accounting_email:18 Health Canada | hc.direct.deposit.requests-demande.de.depot.direct.sc@canada.ca
    - P02_active_relationship_finance_accounting_email:19 Innovation, Science and Economic Develop | ifmscustomer-clientsifm@ised-isde.gc.ca
    - P02_active_relationship_finance_accounting_email:21 National Defence | ddenrol-inscriredd@forces.gc.ca
- **8 receivables-looking local part graded invoicing/AP**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:68 birchfumigators.ca | payment@birchfumigators.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:82 Calgary Coin Gallery | payment@calgarycoin.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:5 Texas Tech University | payment.strategies@ttu.edu
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:14 Awninginabox.ca | payment@awninginabox.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:19 Lerners Lawyers | payments@lerners.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:26 Whitefish River First Nation | payments@whitefishriver.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:79 Nicol Insurance | payments@nicolinsurance.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:155 Facility Solutions Canada Limited | payments@facilitysolutionscanada.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:157 Furbaby Pet Care Saskatoon | payments@furbabysk.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:169 Insight LLP CPA | payments@providinginsight.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:181 bakercornwall.com | payments@bakercornwall.com
    - P01_GOLD_active_relationship_invoicing_AP_email:39 Environment and Climate Change Canada | renseignement-paiements-payments-inquiry@ec.gc.ca
- **9 shared government domain: page or quote names the body**
    - P01_GOLD_active_relationship_invoicing_AP_email:43 Canadian Space Agency | invoicing.csa-asc.facturation@canada.ca ← https://www.canada.ca/en/public-services-procurement/services/payments-to-from-g
    - P01_GOLD_active_relationship_invoicing_AP_email:513 Tennessee Department of Transportation | pln.invoices@tn.gov ← https://www.tn.gov/tdot/long-range-planning-home/longrange-administration/longra
    - P07_client_listing_finance_or_purchasing_email:13 transportation.ky.gov | finance.crcgroup@ky.gov ← https://finance.ky.gov/eProcurement/Pages/doing-business-with-the-commonwealth.a
- **12 evidence page on the organisation's domain (or its site)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:19 ATTIS LEBLANC | payable@attis-leblanc.com on attis-leblanc.ca (site attis-leblanc.com)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:81 COCA-COLA LTD./ COCA-COLA LTEE | krinvoice@coca-cola.com on coca-colacompany.com (site coca-cola.com)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:87 Oil City Drywall North | accounting@oilcitydrywall.ca on oilcitydrywallnorth.ca (site oilcitydrywall.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:46 Capital Regional District | accountspayable@crd.bc.ca on crd.ca (site crd.bc.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:54 ibiosolutions.com | payables@ibiosolutions.com on immunebiosolutions.com (site ibiosolutions.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:86 dabc.ca | ap@dabc.ca on disabilityalliancebc.org (site dabc.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:97 Motorola Solutions, Inc | recepcionfacturas@motorolasolutions.com on web.archive.org (site motorolasolutions.com)
    - P01_GOLD_active_relationship_invoicing_AP_email:2 Department of Defence | invoices@defence.gov.au on web.archive.org (site defence.gov.au)
    - P01_GOLD_active_relationship_invoicing_AP_email:3 Department of Industry, Science and Reso | einvoicingqueries@industry.gov.au on directory.peppol.eu (site industry.gov.au)
    - P01_GOLD_active_relationship_invoicing_AP_email:51 Natural Sciences and Engineering Researc | payables@nserc-crsng.gc.ca on nserc-crsng.canada.ca (site nserc-crsng.gc.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:66 Ville de Montréal | facture@montreal.ca on ville.montreal.qc.ca (site montreal.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:95 Ville de Farnham | comptespayables@ville.farnham.qc.ca on web.archive.org (site ville.farnham.qc.ca)
- **14 DMARC / SPF / provider columns filled**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:130 Climatisation chauffage Sorel-Tracy inc. | not checked yet | not checked yet | not checked
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:132 Owen Bird Law Corporation | not checked yet | not checked yet | not checked
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:78 Kimball Midwest | not checked yet | not checked yet | not checked
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:80 Morton Salt | not checked yet | not checked yet | not checked
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:154 Military & Federal Construction | not checked yet | not checked yet | not checked
    - P01_GOLD_active_relationship_invoicing_AP_email:547 SHORELINE SCHOOL DISTRICT #412 | not checked yet | not checked yet | not checked
    - P02_active_relationship_finance_accounting_email:382 Sun Life Financial Inc. | not checked yet | not checked yet | not checked
    - P03_active_relationship_purchasing_email:204 Salt Lake City International Airport | not checked yet | not checked yet | not checked
    - P03_active_relationship_purchasing_email:216 emcinsurance.com | not checked yet | not checked yet | not checked
    - P04_active_relationship_general_email_part1_of_2:1115 Ansaldo Energia | not checked yet | not checked yet | not checked
    - P04_active_relationship_general_email_part1_of_2:1507 City, Water, Light and Power | not checked yet | not checked yet | not checked
    - P04_active_relationship_general_email_part1_of_2:1534 Restaurants Canada | not checked yet | not checked yet | not checked
- **15 tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m)**
    - P02_active_relationship_finance_accounting_email:160 Ville de Causapscal | A with end 2026-11-11
    - P04_active_relationship_general_email_part1_of_2:251 Régie intermunicipale de gestion des mat | A with end 2026-11-11
    - P04_active_relationship_general_email_part1_of_2:417 Paroisse de Sainte-Irène | A with end 2026-11-11
- **19 buyer name is a name (not a domain or a page title)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:68 birchfumigators.ca | birchfumigators.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:69 dfcdiesel.com | dfcdiesel.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:12 airweld.com | airweld.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:14 Awninginabox.ca | Awninginabox.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:22 efifoodequip.com | efifoodequip.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:41 lpsg.ca | lpsg.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:44 apsurveys.ca | apsurveys.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:47 ep.com | ep.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:48 ctwater.com | ctwater.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:54 ibiosolutions.com | ibiosolutions.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:60 guardian.law | guardian.law
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:64 my.honorhealth.com | my.honorhealth.com
- **20 legal name is not a fragment or a platform copyright**
    - P05_likely_active_awarded_12_36_months_any_email:58 Ameren Illinois Company | Ameren Corporation and/or its suppliers
    - P05_likely_active_awarded_12_36_months_any_email:340 LOVE WORTH FINDING MINISTRIES INC | LLC. 800-274-5683 2941 Kate Bond Rd, Memphis, TN 38133 CONNECT WITH LW
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part5_of_7:864 +ARTHRI-PLUS INC. | +ARTHRI-PLUS INC. (the Canadian trademarks register (owner of record),
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part6_of_7:1597 LITCO LAW IS A TRADEMARK AND TRADE NAME  | LITCO LAW IS A TRADEMARK AND TRADE NAME OF LITWINIUK LLP
    - P06T_active_service_seen_on_buyer_site_other_email_part12_of_15:224 Landscaping | LTD Landscaping Inc. (as registered: Corporations Canada (open data), 
    - P06T_active_service_seen_on_buyer_site_other_email_part12_of_15:2073 Reimer Construction | Introduction Welcome to Reimer Construction (stated on https://reimerc
    - P06T_active_service_seen_on_buyer_site_other_email_part12_of_15:2589 Punta Cana Spa | Introduction Welcome to Punta Cana Spa (stated on https://puntacanaspa
    - P06T_active_service_seen_on_buyer_site_other_email_part13_of_15:666 Caleb Creations | Introduction Welcome to Caleb Creations (stated on https://calebcreati
    - P06T_active_service_seen_on_buyer_site_other_email_part14_of_15:673 Toronto Comedy Festival | Introduction Welcome to the Toronto Comedy Festival (stated on https:/
    - P06T_active_service_seen_on_buyer_site_other_email_part15_of_15:257 We Will Walk You | Introduction Welcome to We Will Walk You (stated on https://www.wewill
    - P06T_active_service_seen_on_buyer_site_other_email_part15_of_15:2479 Feb 2th, 2024 Acceptance of Terms Welcom | Feb 2th, 2024 Acceptance of Terms Welcome to NTWIST (stated on https:/
    - P06T_active_service_seen_on_buyer_site_other_email_part1_of_15:1457 Beet & Yarrow | Introduction Welcome to Beet & Yarrow. Beet & Yarrow (stated on https:
- **22 one row per organisation name (same name twice)**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:193 Cascades | 2 rows, same mail domain: cascades.com
    - P01_GOLD_active_relationship_invoicing_AP_email:16 Rocky View County | 2 rows, same mail domain: rockyview.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:26 University of Lethbridge | 2 rows, same mail domain: uleth.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:146 Municipalité de Boischatel | 2 rows, same mail domain: boischatel.net
    - P01_GOLD_active_relationship_invoicing_AP_email:234 Metrolinx | 2 rows, same mail domain: metrolinx.com
    - P01_GOLD_active_relationship_invoicing_AP_email:257 City of Brantford | 2 rows, same mail domain: brantford.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:277 City of Port Moody | 2 rows, same mail domain: portmoody.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:284 Township of Scugog | 2 rows, same mail domain: scugog.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:498 City of Edmonton | 2 rows, same mail domain: edmonton.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:617 Nicola Valley Institute of Technology | 2 rows, same mail domain: nvit.ca
    - P02_active_relationship_finance_accounting_email:137 Ville de Princeville | 2 rows, same mail domain: princeville.quebec
    - P02_active_relationship_finance_accounting_email:160 Ville de Causapscal | 2 rows, same mail domain: causapscal.quebec
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
    - P01_GOLD_active_relationship_invoicing_AP_email:231 Musée canadien de l'histoire/Canadian Mu | historymuseum.ca: 2 rows, payables@historymuseum.ca; membership@historymuseum.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:234 Metrolinx | metrolinx.com: 2 rows, it.invoices@metrolinx.com; rti.invoices@metrolinx.com
    - P01_GOLD_active_relationship_invoicing_AP_email:259 Niagara Region | niagararegion.ca: 2 rows, constructioninvoices@niagararegion.ca; NRHCapitalWorks@niagararegion.ca
- **25 jurisdiction vs mailbox top-level domain**
    - P01_GOLD_active_relationship_invoicing_AP_email:248 Utilities Kingston | CA / kingston.gov.uk
    - P13_inferred_relationship_no_record_own_email_part11_of_47:2066 Alenti | ON / alenti.fr
    - P13_inferred_relationship_no_record_own_email_part11_of_47:2115 Rep iPhone Médoc | QC / rep-iphone.fr
    - P13_inferred_relationship_no_record_own_email_part12_of_47:765 Wajos | ON / wajos.de
    - P13_inferred_relationship_no_record_own_email_part13_of_47:660 SurePay | ON / surepay.co.uk
    - P13_inferred_relationship_no_record_own_email_part14_of_47:150 Denso | ON / denso.co.nz
    - P13_inferred_relationship_no_record_own_email_part14_of_47:376 The Islands of The Bahamas | ON / bahamas.co.uk
    - P13_inferred_relationship_no_record_own_email_part17_of_47:2055 OPAL | QC / opal.fr
    - P13_inferred_relationship_no_record_own_email_part19_of_47:905 Charles Faram | ON / charlesfaram.co.uk
    - P13_inferred_relationship_no_record_own_email_part19_of_47:2071 Wireline Services Group | ON / wirelineservices.com.au
    - P13_inferred_relationship_no_record_own_email_part1_of_47:157 Met Office | QC / metoffice.gov.uk
    - P13_inferred_relationship_no_record_own_email_part1_of_47:290 ONEJOON | QC / onejoon.de
- **26 currency filled when a value is filled**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:101 RENTON SCHOOL DISTRICT #403 | 332345.13 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:444 Rectorado de la Universitat de València | 12698.25 (source field: PayableAmount)
    - P01_GOLD_active_relationship_invoicing_AP_email:456 BRINKS DE COLOMBIA S.A. | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:475 University of North Dakota | 145.850 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:503 BELLEVUE, CITY OF | 35488873.2 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:511 UNIVERSITY PLACE SCHOOL DISTRICT #83 | 685477.9 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:530 North Dakota State University | 35.000 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:535 BELLEVUE SCHOOL DISTRICT #405 | 5395.88 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:541 SNOQUALMIE VALLEY SCHOOL DISTRICT #410 | 23980.42 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:547 SHORELINE SCHOOL DISTRICT #412 | 919904.69 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:549 MARYLAND STADIUM AUTHORITY | 251569.05 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:552 BANCOLOMBIA S.A. | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)

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
- P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email: 131
- P01T_active_service_seen_on_buyer_site_invoicing_AP_email: 194
- P01_GOLD_active_relationship_invoicing_AP_email: 627
- P02_active_relationship_finance_accounting_email: 466
- P03_active_relationship_purchasing_email: 265
- P04_active_relationship_general_email: 3733
- P05_likely_active_awarded_12_36_months_any_email: 424
- P06M_member_or_regulated_payer_of_canadian_body_other_email: 15579
- P06T_active_service_seen_on_buyer_site_other_email: 40041
- P06_client_listing_invoicing_AP_email: 272
- P07_client_listing_finance_or_purchasing_email: 697
- P08_client_listing_general_email: 22230
- P09_older_contract_or_payment_any_email: 307
- P10R_ca_domain_registration_contract_own_email: 0
- P10_linked_from_vendor_site_any_email: 2389
- P11_any_relationship_email_not_yet_confirmed: 1527
- P12_weaker_relationship_within_5_years_own_email: 15
- P13_inferred_relationship_no_record_own_email: 117988

## Field fill across all delivered rows (value present, not `not_published`)
- buyer_website: 206885 (100.0%)
- vendor_address: 205167 (99.2%)
- vendor_website: 196612 (95.0%)
- buyer_address: 180922 (87.5%)
- vendor_phone: 165637 (80.1%)
- vendor_logo_url: 152943 (73.9%)
- buyer_logo_url: 151692 (73.3%)
- buyer_phone: 124206 (60.0%)
- buyer_legal_name_as_published: 93711 (45.3%)
- vendor_legal_name: 91252 (44.1%)
- contract_link: 88897 (43.0%)
- vendor_registry_id: 72771 (35.2%)
- vendor_incorporation_date: 72754 (35.2%)
- vendor_bn9: 66770 (32.3%)
- award_date: 60375 (29.2%)
- vendor_emails: 49267 (23.8%)
- vendor_neq: 42501 (20.5%)
- buyer_bn_as_published: 20643 (10.0%)
- end_date: 13879 (6.7%)
- contract_value: 8003 (3.9%)
- payment_terms_as_published: 4218 (2.0%)
- ap_phone: 3111 (1.5%)
- po_required_as_published: 2411 (1.2%)
- invoice_mailing_address: 2372 (1.1%)
- invoicing_requirements: 2334 (1.1%)
- invoice_portal_url: 2068 (1.0%)
- ap_contact_name_as_published: 1061 (0.5%)

## Canada-proof families
- source field: 118399; other: 88486

## Buyer types
- organisation (type not stated in the record): 106632
- company (private sector): 36108
- company (private sector) (from the organisation's name / web domain): 28679
- non-profit / association / cultural body: 12676
- government ministry / agency: 5220
- municipality / local government (from the organisation's name / web domain): 3190
- non-profit / association / cultural body (from the organisation's name / web domain): 2921
- hospital / health authority: 2610
- utility / public corporation: 2139
- municipality / local government: 1591
- university / college: 1204
- transport / transit authority: 766
- hospital / health authority (from the organisation's name / web domain): 650
- university / college (from the organisation's name / web domain): 523
- utility / public corporation (from the organisation's name / web domain): 390
- government ministry / agency (from the organisation's name / web domain): 372
- religious organisation (from the organisation's name / web domain): 268
- First Nation / Indigenous government: 238
- transport / transit authority (from the organisation's name / web domain): 225
- school board / school district: 190
- First Nation / Indigenous government (from the organisation's name / web domain): 186
- library (from the organisation's name / web domain): 34
- school board / school district (from the organisation's name / web domain): 33
- US government body (federal, state or local): 29
- US city / county / local government: 11

## DMARC posture of the delivered mailboxes
- no DMARC record: 71421
- v=DMARC1; p=none (monitor only, no enforcement): 71240
- p=quarantine: 25785
- not checked yet: 24801
- p=reject: 13092
- DNS lookup failed: 404
- invalid DMARC record: 142
