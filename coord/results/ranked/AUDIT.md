# Deep audit — 229864 delivered rows in 18 packages (111 files), 2026-11-12

Result: **FAIL** — 11 hard checks, 17 soft checks; hard failures: 1. Every flagged row is listed in `audit_flags.csv` with its reasons.

| # | check | kind | rows flagged | verdict |
|---|---|---|---|---|
| 1 | header: identical columns in every file (106 since 2026-11-06) | hard | 1 | FAIL |
| 2 | mailbox syntax | hard | 0 | PASS |
| 3 | mailbox referee-confirmed (all but P11) | hard | 0 | PASS |
| 4 | mail server (MX or A) on the mailbox domain | hard | 0 | PASS |
| 4b | mail server not yet checked (row newer than the last DNS pass) | soft | 175522 | REVIEW |
| 5 | no webmail domain | hard | 0 | PASS |
| 6 | no person-like local part | hard | 0 | PASS |
| 7 | role word in the local part | soft | 17840 | REVIEW |
| 8 | receivables-looking local part graded invoicing/AP | soft | 65 | REVIEW |
| 9 | shared government domain: page or quote names the body | soft | 3 | REVIEW |
| 10 | regional token of a multinational on a differently-located body | soft | 0 | PASS |
| 11 | quote contains the address | hard | 0 | PASS |
| 11b | quote shows the label next to the address (referee saw the address on the page) | soft | 0 | PASS |
| 12 | evidence page on the organisation's domain (or its site) | soft | 11051 | REVIEW |
| 13 | email_type label matches grade | hard | 0 | PASS |
| 14 | DMARC / SPF / provider columns filled | soft | 12515 | REVIEW |
| 15 | tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m) | soft | 3 | REVIEW |
| 16 | vendor named and Canada proof present | hard | 0 | PASS |
| 17 | Canada proof is a source field or the vendor's site (never a name) | soft | 0 | PASS |
| 18 | record link present for dated-record tiers | soft | 0 | PASS |
| 19 | buyer name is a name (not a domain or a page title) | soft | 23433 | REVIEW |
| 20 | legal name is not a fragment or a platform copyright | soft | 51 | REVIEW |
| 21 | one row per mailbox | hard | 0 | PASS |
| 22 | one row per organisation name (same name twice) | soft | 104 | REVIEW |
| 23 | one row per site domain (two rows, different mailboxes, same domain) | soft | 72 | REVIEW |
| 24 | no blank cell | hard | 0 | PASS |
| 25 | jurisdiction vs mailbox top-level domain | soft | 68 | REVIEW |
| 26 | currency filled when a value is filled | soft | 51 | REVIEW |

## Examples of flagged rows (first 12 per check)
- **1 header: identical columns in every file (106 since 2026-11-06)**
    - files | 2 distinct headers; widths [0, 249]
- **4b mail server not yet checked (row newer than the last DNS pass)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:3 ATTIS LEBLANC | attis-leblanc.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:7 Cologix Canada inc. | cologix.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:9 Edmond Nolin Ltée | constructionenl.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:12 Daikin Applied Canada inc. | daikinapplied.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:13 Deblois réfrigération inc. | debloisrefrigeration.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:15 Construction D.M. Turcotte J.M. inc. | dmturcotte.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:16 Dyno Nobel Canada inc. | dynonobel.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:18 Constructions Fabmec inc. | fabmec.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:19 Filspec inc. | filspec.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:21 Électricité de la Capitale Inc. | groleaudev.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:22 Groupe Lalonde inc. | groupelalonde.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:25 Huppé réfrigération | hupperefrigeration.com
- **7 role word in the local part**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:115 Taylor-Listug, Inc. | ap_group@taylorguitars.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:92 Cameco Corporation | ap_cameco@cameco.com
    - P01_GOLD_active_relationship_invoicing_AP_email:281 Town of Oakville | ap_inquiries@oakville.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:303 University of Saskatchewan | connectionpoint@usask.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:305 Miami-Dade County (business unit CU05010 | invsubp@miamidade.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:389 BELL TEXTRON INC | APBell@textron.com
    - P02_active_relationship_finance_accounting_email:6 Agriculture and Agri-Food Canada | directdeposit.depotdirect@canada.ca
    - P02_active_relationship_finance_accounting_email:10 Crown-Indigenous Relations and Northern  | depotdirect-directdeposit@sac-isc.gc.ca
    - P02_active_relationship_finance_accounting_email:12 Health Canada | hc.direct.deposit.requests-demande.de.depot.direct.sc@canada.ca
    - P02_active_relationship_finance_accounting_email:13 Innovation, Science and Economic Develop | ifmscustomer-clientsifm@ised-isde.gc.ca
    - P02_active_relationship_finance_accounting_email:16 Social Sciences and Humanities Research  | directdeposit-depotdirect@crsh-sshrc.gc.ca
    - P02_active_relationship_finance_accounting_email:18 Veterans Affairs Canada | directdeposit-depotdirect@vac-acc.gc.ca
- **8 receivables-looking local part graded invoicing/AP**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:57 Calgary Coin Gallery | payment@calgarycoin.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:88 birchfumigators.ca | payment@birchfumigators.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:5 Lerners Lawyers | payments@lerners.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:36 Awninginabox.ca | payment@awninginabox.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:70 Nicol Insurance | payments@nicolinsurance.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:75 Texas Tech University | payment.strategies@ttu.edu
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:77 Whitefish River First Nation | payments@whitefishriver.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:148 Facility Solutions Canada Limited | payments@facilitysolutionscanada.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:150 Furbaby Pet Care Saskatoon | payments@furbabysk.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:162 Insight LLP CPA | payments@providinginsight.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:174 bakercornwall.com | payments@bakercornwall.com
    - P01_GOLD_active_relationship_invoicing_AP_email:33 Environment and Climate Change Canada | renseignement-paiements-payments-inquiry@ec.gc.ca
- **9 shared government domain: page or quote names the body**
    - P01_GOLD_active_relationship_invoicing_AP_email:37 Canadian Space Agency | invoicing.csa-asc.facturation@canada.ca ← https://www.canada.ca/en/public-services-procurement/services/payments-to-from-g
    - P01_GOLD_active_relationship_invoicing_AP_email:541 Tennessee Department of Transportation | pln.invoices@tn.gov ← https://www.tn.gov/tdot/long-range-planning-home/longrange-administration/longra
    - P07_client_listing_finance_or_purchasing_email:430 transportation.ky.gov | finance.crcgroup@ky.gov ← https://finance.ky.gov/eProcurement/Pages/doing-business-with-the-commonwealth.a
- **12 evidence page on the organisation's domain (or its site)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:3 ATTIS LEBLANC | payable@attis-leblanc.com on attis-leblanc.ca (site attis-leblanc.com)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:62 Oil City Drywall North | accounting@oilcitydrywall.ca on oilcitydrywallnorth.ca (site oilcitydrywall.ca)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:94 COCA-COLA LTD./ COCA-COLA LTEE | krinvoice@coca-cola.com on coca-colacompany.com (site coca-cola.com)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:124 Progressive Automations Inc. | accounting@progressiveautomations.com on progressiveautomations.ca (site progressiveautomations.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:22 Capital Regional District | accountspayable@crd.bc.ca on crd.ca (site crd.bc.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:44 dabc.ca | ap@dabc.ca on disabilityalliancebc.org (site dabc.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:59 ibiosolutions.com | payables@ibiosolutions.com on immunebiosolutions.com (site ibiosolutions.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:79 go.intermedia.com | ap@intermedia.com on intermedia.ca (site go.intermedia.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:94 Motorola Solutions, Inc | recepcionfacturas@motorolasolutions.com on web.archive.org (site motorolasolutions.com)
    - P01_GOLD_active_relationship_invoicing_AP_email:2 Department of Defence | invoices@defence.gov.au on web.archive.org (site defence.gov.au)
    - P01_GOLD_active_relationship_invoicing_AP_email:3 Department of Industry, Science and Reso | einvoicingqueries@industry.gov.au on directory.peppol.eu (site industry.gov.au)
    - P01_GOLD_active_relationship_invoicing_AP_email:44 Natural Sciences and Engineering Researc | payables@nserc-crsng.gc.ca on nserc-crsng.canada.ca (site nserc-crsng.gc.ca)
- **14 DMARC / SPF / provider columns filled**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:69 Owen Bird Law Corporation | not checked yet | not checked yet | not checked
    - P01_GOLD_active_relationship_invoicing_AP_email:480 SHORELINE SCHOOL DISTRICT #412 | not checked yet | not checked yet | not checked
    - P02_active_relationship_finance_accounting_email:379 Sun Life Financial Inc. | not checked yet | not checked yet | not checked
    - P03_active_relationship_purchasing_email:205 Salt Lake City International Airport | not checked yet | not checked yet | not checked
    - P04_active_relationship_general_email_part1_of_2:1465 Restaurants Canada | not checked yet | not checked yet | not checked
    - P04_active_relationship_general_email_part2_of_2:35 Christopher Raeburn | not checked yet | not checked yet | not checked
    - P04_active_relationship_general_email_part2_of_2:48 Hertford, NC | not checked yet | not checked yet | not checked
    - P04_active_relationship_general_email_part2_of_2:296 Sea Shepherd | not checked yet | not checked yet | not checked
    - P04_active_relationship_general_email_part2_of_2:387 tsusbengaluru.com | not checked yet | not checked yet | not checked
    - P04_active_relationship_general_email_part2_of_2:848 Should I Use It | not checked yet | not checked yet | not checked
    - P04_active_relationship_general_email_part2_of_2:860 welcome.taxcycle.com | not checked yet | not checked yet | not checked
    - P04_active_relationship_general_email_part2_of_2:946 Kansas Lottery | not checked yet | not checked yet | not checked
- **15 tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m)**
    - P02_active_relationship_finance_accounting_email:158 Ville de Causapscal | A with end 2026-11-11
    - P04_active_relationship_general_email_part1_of_2:254 Régie intermunicipale de gestion des mat | A with end 2026-11-11
    - P04_active_relationship_general_email_part1_of_2:418 Paroisse de Sainte-Irène | A with end 2026-11-11
- **19 buyer name is a name (not a domain or a page title)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:88 birchfumigators.ca | birchfumigators.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:89 dfcdiesel.com | dfcdiesel.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:19 lpsg.ca | lpsg.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:21 apsurveys.ca | apsurveys.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:28 guardian.law | guardian.law
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:36 Awninginabox.ca | Awninginabox.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:44 dabc.ca | dabc.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:52 efifoodequip.com | efifoodequip.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:57 ep.com | ep.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:58 ctwater.com | ctwater.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:59 ibiosolutions.com | ibiosolutions.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:63 dumptrucks.com | dumptrucks.com
- **20 legal name is not a fragment or a platform copyright**
    - P05_likely_active_awarded_12_36_months_any_email:56 Ameren Illinois Company | Ameren Corporation and/or its suppliers
    - P05_likely_active_awarded_12_36_months_any_email:208 LOVE WORTH FINDING MINISTRIES INC | LLC. 800-274-5683 2941 Kate Bond Rd, Memphis, TN 38133 CONNECT WITH LW
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part5_of_7:2093 +ARTHRI-PLUS INC. | +ARTHRI-PLUS INC. (the Canadian trademarks register (owner of record),
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part6_of_7:1713 LITCO LAW IS A TRADEMARK AND TRADE NAME  | LITCO LAW IS A TRADEMARK AND TRADE NAME OF LITWINIUK LLP
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part7_of_7:2252 the airscreen company GmbH & Co. KG | the airscreen company GmbH & Co. KG (the Canadian trademarks register 
    - P06T_active_service_seen_on_buyer_site_other_email_part11_of_14:1422 Landscaping | LTD Landscaping Inc. (as registered: Corporations Canada (open data), 
    - P06T_active_service_seen_on_buyer_site_other_email_part12_of_14:457 Reimer Construction | Introduction Welcome to Reimer Construction (stated on https://reimerc
    - P06T_active_service_seen_on_buyer_site_other_email_part12_of_14:902 Punta Cana Spa | Introduction Welcome to Punta Cana Spa (stated on https://puntacanaspa
    - P06T_active_service_seen_on_buyer_site_other_email_part13_of_14:1214 Toronto Comedy Festival | Introduction Welcome to the Toronto Comedy Festival (stated on https:/
    - P06T_active_service_seen_on_buyer_site_other_email_part14_of_14:2490 Feb 2th, 2024 Acceptance of Terms Welcom | Feb 2th, 2024 Acceptance of Terms Welcome to NTWIST (stated on https:/
    - P06T_active_service_seen_on_buyer_site_other_email_part3_of_14:326 Landscaping | LTD Landscaping Inc. (as registered: Corporations Canada (open data), 
    - P06T_active_service_seen_on_buyer_site_other_email_part3_of_14:1034 Landscaping | LTD Landscaping Inc. (as registered: Corporations Canada (open data), 
- **22 one row per organisation name (same name twice)**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:34 Cascades | 2 rows, same mail domain: cascades.com
    - P01_GOLD_active_relationship_invoicing_AP_email:16 Rocky View County | 2 rows, same mail domain: rockyview.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:105 University of Lethbridge | 2 rows, same mail domain: uleth.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:142 Municipalité de Boischatel | 2 rows, same mail domain: boischatel.net
    - P01_GOLD_active_relationship_invoicing_AP_email:239 Metrolinx | 2 rows, same mail domain: metrolinx.com
    - P01_GOLD_active_relationship_invoicing_AP_email:265 City of Brantford | 2 rows, same mail domain: brantford.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:282 City of Port Moody | 2 rows, same mail domain: portmoody.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:288 Township of Scugog | 2 rows, same mail domain: scugog.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:532 City of Edmonton | 2 rows, same mail domain: edmonton.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:607 Nicola Valley Institute of Technology | 2 rows, same mail domain: nvit.ca
    - P02_active_relationship_finance_accounting_email:135 Ville de Princeville | 2 rows, same mail domain: princeville.quebec
    - P02_active_relationship_finance_accounting_email:158 Ville de Causapscal | 2 rows, same mail domain: causapscal.quebec
- **23 one row per site domain (two rows, different mailboxes, same domain)**
    - P01_GOLD_active_relationship_invoicing_AP_email:2 Department of Defence | defence.gov.au: 2 rows, invoices@defence.gov.au; peppol.einvoices@defence.gov.au
    - P01_GOLD_active_relationship_invoicing_AP_email:48 Ville de Gatineau | gatineau.ca: 2 rows, gatineau.factures@gatineau.ca; idgatineau@gatineau.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:57 Ville de Montréal | montreal.ca: 2 rows, facture@montreal.ca; comptesapayer@montreal.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:69 Ville de Laval | laval.ca: 3 rows, comptespayables@laval.ca; lavaleconomique@laval.ca; info@laval.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:101 Texas Department of Insurance | texas.gov: 7 rows, invoices@tdi.texas.gov; ap@ers.texas.gov; accounts.payable@tpwd.texas.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:107 University of Toronto | utoronto.ca: 2 rows, ap.fsd@utoronto.ca; fmdinvoice.utsc@utoronto.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:127 University of Ottawa | uottawa.ca: 2 rows, payables@uottawa.ca; info@emba.uottawa.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:192 Oregon Department of Transportation | oregon.gov: 3 rows, opoinvoiceinquiries@odot.oregon.gov; omdaccounts.payable@omd.oregon.gov; odf.accountspayable@oregon.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:195 Texas Tech University Health Sciences Ce | ttuhsc.edu: 2 rows, Accounts.Payable@ttuhsc.edu; accountspayableelp@ttuhsc.edu
    - P01_GOLD_active_relationship_invoicing_AP_email:238 Musée canadien de l'histoire/Canadian Mu | historymuseum.ca: 2 rows, payables@historymuseum.ca; membership@historymuseum.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:239 Metrolinx | metrolinx.com: 2 rows, it.invoices@metrolinx.com; rti.invoices@metrolinx.com
    - P01_GOLD_active_relationship_invoicing_AP_email:266 Niagara Region | niagararegion.ca: 2 rows, constructioninvoices@niagararegion.ca; NRHCapitalWorks@niagararegion.ca
- **25 jurisdiction vs mailbox top-level domain**
    - P01_GOLD_active_relationship_invoicing_AP_email:256 Utilities Kingston | CA / kingston.gov.uk
    - P13_inferred_relationship_no_record_own_email_part14_of_67:423 Alenti | ON / alenti.fr
    - P13_inferred_relationship_no_record_own_email_part14_of_67:470 Rep iPhone Médoc | QC / rep-iphone.fr
    - P13_inferred_relationship_no_record_own_email_part15_of_67:2010 SurePay | ON / surepay.co.uk
    - P13_inferred_relationship_no_record_own_email_part16_of_67:1912 Denso | ON / denso.co.nz
    - P13_inferred_relationship_no_record_own_email_part17_of_67:1870 LA MAISON DES JEUNES DE PLESSISVILLE INC | QC / lycos.fr
    - P13_inferred_relationship_no_record_own_email_part18_of_67:665 The Redeemed Christian Church of God Lov | SK / loveassembly.co.uk
    - P13_inferred_relationship_no_record_own_email_part1_of_67:164 Miele | ON / miele.de
    - P13_inferred_relationship_no_record_own_email_part1_of_67:303 ONEJOON | QC / onejoon.de
    - P13_inferred_relationship_no_record_own_email_part1_of_67:1393 Mole Valley District Council | SK / molevalley.gov.uk
    - P13_inferred_relationship_no_record_own_email_part22_of_67:175 OPAL | QC / opal.fr
    - P13_inferred_relationship_no_record_own_email_part24_of_67:386 Charles Faram | ON / charlesfaram.co.uk
- **26 currency filled when a value is filled**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:45 RENTON SCHOOL DISTRICT #403 | 332345.13 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:456 Rectorado de la Universitat de València | 12698.25 (source field: PayableAmount)
    - P01_GOLD_active_relationship_invoicing_AP_email:467 BELLEVUE, CITY OF | 35488873.2 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:469 UNIVERSITY PLACE SCHOOL DISTRICT #83 | 685477.9 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:475 BELLEVUE SCHOOL DISTRICT #405 | 5395.88 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:478 SNOQUALMIE VALLEY SCHOOL DISTRICT #410 | 23980.42 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:480 SHORELINE SCHOOL DISTRICT #412 | 919904.69 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:496 University of North Dakota | 145.850 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:499 North Dakota State University | 35.000 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:566 BANCOLOMBIA S.A. | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:572 ECOPETROL S A | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:616 MARYLAND STADIUM AUTHORITY | 251569.05 (source field: amount)

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
- P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email: 146
- P01T_active_service_seen_on_buyer_site_invoicing_AP_email: 185
- P01_GOLD_active_relationship_invoicing_AP_email: 641
- P02_active_relationship_finance_accounting_email: 471
- P03_active_relationship_purchasing_email: 271
- P04_active_relationship_general_email: 3629
- P05_likely_active_awarded_12_36_months_any_email: 427
- P06M_member_or_regulated_payer_of_canadian_body_other_email: 15872
- P06T_active_service_seen_on_buyer_site_other_email: 37219
- P06_client_listing_invoicing_AP_email: 257
- P07_client_listing_finance_or_purchasing_email: 677
- P08_client_listing_general_email: 21626
- P09_older_contract_or_payment_any_email: 314
- P10R_ca_domain_registration_contract_own_email: 0
- P10_linked_from_vendor_site_any_email: 2168
- P11_any_relationship_email_not_yet_confirmed: 1512
- P12_weaker_relationship_within_5_years_own_email: 16
- P13_inferred_relationship_no_record_own_email: 144433

## Field fill across all delivered rows (value present, not `not_published`)
- buyer_website: 229864 (100.0%)
- vendor_address: 228290 (99.3%)
- vendor_website: 219296 (95.4%)
- buyer_address: 208339 (90.6%)
- vendor_legal_name: 199339 (86.7%)
- vendor_phone: 187283 (81.5%)
- buyer_logo_url: 179439 (78.1%)
- vendor_registry_id: 178643 (77.7%)
- vendor_logo_url: 169732 (73.8%)
- buyer_phone: 143012 (62.2%)
- buyer_legal_name_as_published: 105092 (45.7%)
- contract_link: 85431 (37.2%)
- vendor_incorporation_date: 76300 (33.2%)
- vendor_bn9: 71856 (31.3%)
- award_date: 57940 (25.2%)
- vendor_emails: 49307 (21.5%)
- vendor_neq: 47240 (20.6%)
- buyer_bn_as_published: 22130 (9.6%)
- end_date: 14184 (6.2%)
- contract_value: 8131 (3.5%)
- payment_terms_as_published: 4265 (1.9%)
- ap_phone: 3163 (1.4%)
- po_required_as_published: 2425 (1.1%)
- invoice_mailing_address: 2415 (1.1%)
- invoicing_requirements: 2378 (1.0%)
- invoice_portal_url: 2073 (0.9%)
- ap_contact_name_as_published: 1079 (0.5%)

## Canada-proof families
- source field: 125250; other: 104614

## Buyer types
- organisation (type not stated in the record): 119308
- company (private sector): 39608
- company (private sector) (from the organisation's name / web domain): 32662
- non-profit / association / cultural body: 13688
- government ministry / agency: 5840
- municipality / local government (from the organisation's name / web domain): 3231
- non-profit / association / cultural body (from the organisation's name / web domain): 3196
- hospital / health authority: 2761
- utility / public corporation: 2370
- municipality / local government: 1648
- university / college: 1333
- transport / transit authority: 827
- hospital / health authority (from the organisation's name / web domain): 710
- university / college (from the organisation's name / web domain): 538
- utility / public corporation (from the organisation's name / web domain): 439
- government ministry / agency (from the organisation's name / web domain): 422
- religious organisation (from the organisation's name / web domain): 299
- First Nation / Indigenous government: 249
- transport / transit authority (from the organisation's name / web domain): 235
- First Nation / Indigenous government (from the organisation's name / web domain): 199
- school board / school district: 194
- library (from the organisation's name / web domain): 34
- school board / school district (from the organisation's name / web domain): 33
- US government body (federal, state or local): 29
- US city / county / local government: 11

## DMARC posture of the delivered mailboxes
- no DMARC record: 87440
- v=DMARC1; p=none (monitor only, no enforcement): 85030
- p=quarantine: 29800
- p=reject: 14840
- not checked yet: 12515
- invalid DMARC record: 165
- DNS lookup failed: 74
