# Deep audit — 206985 delivered rows in 18 packages (99 files), 2026-11-12

Result: **FAIL** — 11 hard checks, 17 soft checks; hard failures: 1. Every flagged row is listed in `audit_flags.csv` with its reasons.

| # | check | kind | rows flagged | verdict |
|---|---|---|---|---|
| 1 | header: identical columns in every file (106 since 2026-11-06) | hard | 1 | FAIL |
| 2 | mailbox syntax | hard | 0 | PASS |
| 3 | mailbox referee-confirmed (all but P11) | hard | 0 | PASS |
| 4 | mail server (MX or A) on the mailbox domain | hard | 0 | PASS |
| 4b | mail server not yet checked (row newer than the last DNS pass) | soft | 156268 | REVIEW |
| 5 | no webmail domain | hard | 0 | PASS |
| 6 | no person-like local part | hard | 0 | PASS |
| 7 | role word in the local part | soft | 15223 | REVIEW |
| 8 | receivables-looking local part graded invoicing/AP | soft | 61 | REVIEW |
| 9 | shared government domain: page or quote names the body | soft | 3 | REVIEW |
| 10 | regional token of a multinational on a differently-located body | soft | 0 | PASS |
| 11 | quote contains the address | hard | 0 | PASS |
| 11b | quote shows the label next to the address (referee saw the address on the page) | soft | 0 | PASS |
| 12 | evidence page on the organisation's domain (or its site) | soft | 9382 | REVIEW |
| 13 | email_type label matches grade | hard | 0 | PASS |
| 14 | DMARC / SPF / provider columns filled | soft | 24074 | REVIEW |
| 15 | tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m) | soft | 3 | REVIEW |
| 16 | vendor named and Canada proof present | hard | 0 | PASS |
| 17 | Canada proof is a source field or the vendor's site (never a name) | soft | 0 | PASS |
| 18 | record link present for dated-record tiers | soft | 0 | PASS |
| 19 | buyer name is a name (not a domain or a page title) | soft | 20962 | REVIEW |
| 20 | legal name is not a fragment or a platform copyright | soft | 48 | REVIEW |
| 21 | one row per mailbox | hard | 0 | PASS |
| 22 | one row per organisation name (same name twice) | soft | 97 | REVIEW |
| 23 | one row per site domain (two rows, different mailboxes, same domain) | soft | 64 | REVIEW |
| 24 | no blank cell | hard | 0 | PASS |
| 25 | jurisdiction vs mailbox top-level domain | soft | 59 | REVIEW |
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
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:97 Cameco Corporation | ap_cameco@cameco.com
    - P01_GOLD_active_relationship_invoicing_AP_email:277 Town of Oakville | ap_inquiries@oakville.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:299 University of Saskatchewan | connectionpoint@usask.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:301 Miami-Dade County (business unit CU05010 | invsubp@miamidade.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:384 BELL TEXTRON INC | APBell@textron.com
    - P02_active_relationship_finance_accounting_email:6 Agriculture and Agri-Food Canada | directdeposit.depotdirect@canada.ca
    - P02_active_relationship_finance_accounting_email:10 Crown-Indigenous Relations and Northern  | depotdirect-directdeposit@sac-isc.gc.ca
    - P02_active_relationship_finance_accounting_email:12 Health Canada | hc.direct.deposit.requests-demande.de.depot.direct.sc@canada.ca
    - P02_active_relationship_finance_accounting_email:13 Innovation, Science and Economic Develop | ifmscustomer-clientsifm@ised-isde.gc.ca
    - P02_active_relationship_finance_accounting_email:16 Social Sciences and Humanities Research  | directdeposit-depotdirect@crsh-sshrc.gc.ca
    - P02_active_relationship_finance_accounting_email:18 Veterans Affairs Canada | directdeposit-depotdirect@vac-acc.gc.ca
- **8 receivables-looking local part graded invoicing/AP**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:57 Calgary Coin Gallery | payment@calgarycoin.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:88 birchfumigators.ca | payment@birchfumigators.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:6 Lerners Lawyers | payments@lerners.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:37 Awninginabox.ca | payment@awninginabox.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:74 Nicol Insurance | payments@nicolinsurance.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:79 Texas Tech University | payment.strategies@ttu.edu
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:81 Whitefish River First Nation | payments@whitefishriver.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:156 Facility Solutions Canada Limited | payments@facilitysolutionscanada.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:158 Furbaby Pet Care Saskatoon | payments@furbabysk.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:170 Insight LLP CPA | payments@providinginsight.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:182 bakercornwall.com | payments@bakercornwall.com
    - P01_GOLD_active_relationship_invoicing_AP_email:33 Environment and Climate Change Canada | renseignement-paiements-payments-inquiry@ec.gc.ca
- **9 shared government domain: page or quote names the body**
    - P01_GOLD_active_relationship_invoicing_AP_email:37 Canadian Space Agency | invoicing.csa-asc.facturation@canada.ca ← https://www.canada.ca/en/public-services-procurement/services/payments-to-from-g
    - P01_GOLD_active_relationship_invoicing_AP_email:538 Tennessee Department of Transportation | pln.invoices@tn.gov ← https://www.tn.gov/tdot/long-range-planning-home/longrange-administration/longra
    - P07_client_listing_finance_or_purchasing_email:431 transportation.ky.gov | finance.crcgroup@ky.gov ← https://finance.ky.gov/eProcurement/Pages/doing-business-with-the-commonwealth.a
- **12 evidence page on the organisation's domain (or its site)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:3 ATTIS LEBLANC | payable@attis-leblanc.com on attis-leblanc.ca (site attis-leblanc.com)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:62 Oil City Drywall North | accounting@oilcitydrywall.ca on oilcitydrywallnorth.ca (site oilcitydrywall.ca)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:94 COCA-COLA LTD./ COCA-COLA LTEE | krinvoice@coca-cola.com on coca-colacompany.com (site coca-cola.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:23 Capital Regional District | accountspayable@crd.bc.ca on crd.ca (site crd.bc.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:45 dabc.ca | ap@dabc.ca on disabilityalliancebc.org (site dabc.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:62 ibiosolutions.com | payables@ibiosolutions.com on immunebiosolutions.com (site ibiosolutions.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:99 Motorola Solutions, Inc | recepcionfacturas@motorolasolutions.com on web.archive.org (site motorolasolutions.com)
    - P01_GOLD_active_relationship_invoicing_AP_email:2 Department of Defence | invoices@defence.gov.au on web.archive.org (site defence.gov.au)
    - P01_GOLD_active_relationship_invoicing_AP_email:3 Department of Industry, Science and Reso | einvoicingqueries@industry.gov.au on directory.peppol.eu (site industry.gov.au)
    - P01_GOLD_active_relationship_invoicing_AP_email:44 Natural Sciences and Engineering Researc | payables@nserc-crsng.gc.ca on nserc-crsng.canada.ca (site nserc-crsng.gc.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:57 Ville de Montréal | facture@montreal.ca on ville.montreal.qc.ca (site montreal.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:83 Ville de Farnham | comptespayables@ville.farnham.qc.ca on web.archive.org (site ville.farnham.qc.ca)
- **14 DMARC / SPF / provider columns filled**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:67 Climatisation chauffage Sorel-Tracy inc. | not checked yet | not checked yet | not checked
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:69 Owen Bird Law Corporation | not checked yet | not checked yet | not checked
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:73 Kimball Midwest | not checked yet | not checked yet | not checked
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:75 Morton Salt | not checked yet | not checked yet | not checked
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:155 Military & Federal Construction | not checked yet | not checked yet | not checked
    - P01_GOLD_active_relationship_invoicing_AP_email:475 SHORELINE SCHOOL DISTRICT #412 | not checked yet | not checked yet | not checked
    - P02_active_relationship_finance_accounting_email:371 Sun Life Financial Inc. | not checked yet | not checked yet | not checked
    - P03_active_relationship_purchasing_email:196 Salt Lake City International Airport | not checked yet | not checked yet | not checked
    - P03_active_relationship_purchasing_email:216 emcinsurance.com | not checked yet | not checked yet | not checked
    - P04_active_relationship_general_email_part1_of_2:1411 Restaurants Canada | not checked yet | not checked yet | not checked
    - P04_active_relationship_general_email_part1_of_2:1465 Cheese Boutique Ltd. | not checked yet | not checked yet | not checked
    - P04_active_relationship_general_email_part1_of_2:1631 City, Water, Light and Power | not checked yet | not checked yet | not checked
- **15 tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m)**
    - P02_active_relationship_finance_accounting_email:155 Ville de Causapscal | A with end 2026-11-11
    - P04_active_relationship_general_email_part1_of_2:237 Régie intermunicipale de gestion des mat | A with end 2026-11-11
    - P04_active_relationship_general_email_part1_of_2:396 Paroisse de Sainte-Irène | A with end 2026-11-11
- **19 buyer name is a name (not a domain or a page title)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:88 birchfumigators.ca | birchfumigators.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:89 dfcdiesel.com | dfcdiesel.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:20 lpsg.ca | lpsg.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:22 apsurveys.ca | apsurveys.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:29 guardian.law | guardian.law
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:37 Awninginabox.ca | Awninginabox.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:45 dabc.ca | dabc.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:53 efifoodequip.com | efifoodequip.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:60 ep.com | ep.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:61 ctwater.com | ctwater.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:62 ibiosolutions.com | ibiosolutions.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:67 dumptrucks.com | dumptrucks.com
- **20 legal name is not a fragment or a platform copyright**
    - P05_likely_active_awarded_12_36_months_any_email:56 Ameren Illinois Company | Ameren Corporation and/or its suppliers
    - P05_likely_active_awarded_12_36_months_any_email:205 LOVE WORTH FINDING MINISTRIES INC | LLC. 800-274-5683 2941 Kate Bond Rd, Memphis, TN 38133 CONNECT WITH LW
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part6_of_7:95 +ARTHRI-PLUS INC. | +ARTHRI-PLUS INC. (the Canadian trademarks register (owner of record),
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part6_of_7:2065 LITCO LAW IS A TRADEMARK AND TRADE NAME  | LITCO LAW IS A TRADEMARK AND TRADE NAME OF LITWINIUK LLP
    - P06T_active_service_seen_on_buyer_site_other_email_part12_of_15:339 Landscaping | LTD Landscaping Inc. (as registered: Corporations Canada (open data), 
    - P06T_active_service_seen_on_buyer_site_other_email_part12_of_15:2188 Reimer Construction | Introduction Welcome to Reimer Construction (stated on https://reimerc
    - P06T_active_service_seen_on_buyer_site_other_email_part13_of_15:35 Punta Cana Spa | Introduction Welcome to Punta Cana Spa (stated on https://puntacanaspa
    - P06T_active_service_seen_on_buyer_site_other_email_part13_of_15:782 Caleb Creations | Introduction Welcome to Caleb Creations (stated on https://calebcreati
    - P06T_active_service_seen_on_buyer_site_other_email_part14_of_15:790 Toronto Comedy Festival | Introduction Welcome to the Toronto Comedy Festival (stated on https:/
    - P06T_active_service_seen_on_buyer_site_other_email_part15_of_15:373 We Will Walk You | Introduction Welcome to We Will Walk You (stated on https://www.wewill
    - P06T_active_service_seen_on_buyer_site_other_email_part15_of_15:2507 Feb 2th, 2024 Acceptance of Terms Welcom | Feb 2th, 2024 Acceptance of Terms Welcome to NTWIST (stated on https:/
    - P06T_active_service_seen_on_buyer_site_other_email_part3_of_15:311 Landscaping | LTD Landscaping Inc. (as registered: Corporations Canada (open data), 
- **22 one row per organisation name (same name twice)**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:35 Cascades | 2 rows, same mail domain: cascades.com
    - P01_GOLD_active_relationship_invoicing_AP_email:16 Rocky View County | 2 rows, same mail domain: rockyview.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:105 University of Lethbridge | 2 rows, same mail domain: uleth.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:141 Municipalité de Boischatel | 2 rows, same mail domain: boischatel.net
    - P01_GOLD_active_relationship_invoicing_AP_email:236 Metrolinx | 2 rows, same mail domain: metrolinx.com
    - P01_GOLD_active_relationship_invoicing_AP_email:261 City of Brantford | 2 rows, same mail domain: brantford.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:278 City of Port Moody | 2 rows, same mail domain: portmoody.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:284 Township of Scugog | 2 rows, same mail domain: scugog.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:529 City of Edmonton | 2 rows, same mail domain: edmonton.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:602 Nicola Valley Institute of Technology | 2 rows, same mail domain: nvit.ca
    - P02_active_relationship_finance_accounting_email:132 Ville de Princeville | 2 rows, same mail domain: princeville.quebec
    - P02_active_relationship_finance_accounting_email:155 Ville de Causapscal | 2 rows, same mail domain: causapscal.quebec
- **23 one row per site domain (two rows, different mailboxes, same domain)**
    - P01_GOLD_active_relationship_invoicing_AP_email:2 Department of Defence | defence.gov.au: 2 rows, invoices@defence.gov.au; peppol.einvoices@defence.gov.au
    - P01_GOLD_active_relationship_invoicing_AP_email:48 Ville de Gatineau | gatineau.ca: 2 rows, gatineau.factures@gatineau.ca; idgatineau@gatineau.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:57 Ville de Montréal | montreal.ca: 2 rows, facture@montreal.ca; comptesapayer@montreal.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:69 Ville de Laval | laval.ca: 3 rows, comptespayables@laval.ca; lavaleconomique@laval.ca; info@laval.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:101 Texas Department of Insurance | texas.gov: 7 rows, invoices@tdi.texas.gov; ap@ers.texas.gov; accounts.payable@tpwd.texas.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:107 University of Toronto | utoronto.ca: 2 rows, ap.fsd@utoronto.ca; fmdinvoice.utsc@utoronto.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:126 University of Ottawa | uottawa.ca: 2 rows, payables@uottawa.ca; info@emba.uottawa.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:190 Oregon Department of Transportation | oregon.gov: 3 rows, opoinvoiceinquiries@odot.oregon.gov; omdaccounts.payable@omd.oregon.gov; odf.accountspayable@oregon.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:193 Texas Tech University Health Sciences Ce | ttuhsc.edu: 2 rows, Accounts.Payable@ttuhsc.edu; accountspayableelp@ttuhsc.edu
    - P01_GOLD_active_relationship_invoicing_AP_email:235 Musée canadien de l'histoire/Canadian Mu | historymuseum.ca: 2 rows, payables@historymuseum.ca; membership@historymuseum.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:236 Metrolinx | metrolinx.com: 2 rows, it.invoices@metrolinx.com; rti.invoices@metrolinx.com
    - P01_GOLD_active_relationship_invoicing_AP_email:262 Niagara Region | niagararegion.ca: 2 rows, constructioninvoices@niagararegion.ca; NRHCapitalWorks@niagararegion.ca
- **25 jurisdiction vs mailbox top-level domain**
    - P01_GOLD_active_relationship_invoicing_AP_email:253 Utilities Kingston | CA / kingston.gov.uk
    - P13_inferred_relationship_no_record_own_email_part12_of_54:1640 Alenti | ON / alenti.fr
    - P13_inferred_relationship_no_record_own_email_part12_of_54:1683 Rep iPhone Médoc | QC / rep-iphone.fr
    - P13_inferred_relationship_no_record_own_email_part14_of_54:562 SurePay | ON / surepay.co.uk
    - P13_inferred_relationship_no_record_own_email_part15_of_54:193 Denso | ON / denso.co.nz
    - P13_inferred_relationship_no_record_own_email_part19_of_54:274 OPAL | QC / opal.fr
    - P13_inferred_relationship_no_record_own_email_part1_of_54:149 Met Office | QC / metoffice.gov.uk
    - P13_inferred_relationship_no_record_own_email_part1_of_54:274 ONEJOON | QC / onejoon.de
    - P13_inferred_relationship_no_record_own_email_part1_of_54:1244 Mole Valley District Council | SK / molevalley.gov.uk
    - P13_inferred_relationship_no_record_own_email_part20_of_54:1747 Charles Faram | ON / charlesfaram.co.uk
    - P13_inferred_relationship_no_record_own_email_part21_of_54:649 Wireline Services Group | ON / wirelineservices.com.au
    - P13_inferred_relationship_no_record_own_email_part21_of_54:1697 M&G Marketing | QC / mgmarketing.fr
- **26 currency filled when a value is filled**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:46 RENTON SCHOOL DISTRICT #403 | 332345.13 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:451 Rectorado de la Universitat de València | 12698.25 (source field: PayableAmount)
    - P01_GOLD_active_relationship_invoicing_AP_email:462 BELLEVUE, CITY OF | 35488873.2 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:464 UNIVERSITY PLACE SCHOOL DISTRICT #83 | 685477.9 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:470 BELLEVUE SCHOOL DISTRICT #405 | 5395.88 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:473 SNOQUALMIE VALLEY SCHOOL DISTRICT #410 | 23980.42 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:475 SHORELINE SCHOOL DISTRICT #412 | 919904.69 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:491 University of North Dakota | 145.850 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:494 North Dakota State University | 35.000 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:495 BANCOLOMBIA S.A. | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:496 ECOPETROL S A | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:611 MARYLAND STADIUM AUTHORITY | 251569.05 (source field: amount)

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
- P01_GOLD_active_relationship_invoicing_AP_email: 636
- P02_active_relationship_finance_accounting_email: 466
- P03_active_relationship_purchasing_email: 265
- P04_active_relationship_general_email: 3733
- P05_likely_active_awarded_12_36_months_any_email: 424
- P06M_member_or_regulated_payer_of_canadian_body_other_email: 15579
- P06T_active_service_seen_on_buyer_site_other_email: 40065
- P06_client_listing_invoicing_AP_email: 272
- P07_client_listing_finance_or_purchasing_email: 697
- P08_client_listing_general_email: 22233
- P09_older_contract_or_payment_any_email: 307
- P10R_ca_domain_registration_contract_own_email: 0
- P10_linked_from_vendor_site_any_email: 2391
- P11_any_relationship_email_not_yet_confirmed: 1525
- P12_weaker_relationship_within_5_years_own_email: 15
- P13_inferred_relationship_no_record_own_email: 118052

## Field fill across all delivered rows (value present, not `not_published`)
- buyer_website: 206985 (100.0%)
- vendor_address: 205292 (99.2%)
- vendor_website: 196681 (95.0%)
- buyer_address: 181501 (87.7%)
- vendor_legal_name: 175484 (84.8%)
- buyer_logo_url: 169453 (81.9%)
- vendor_phone: 166449 (80.4%)
- vendor_logo_url: 154255 (74.5%)
- buyer_phone: 135988 (65.7%)
- vendor_registry_id: 128468 (62.1%)
- buyer_legal_name_as_published: 99613 (48.1%)
- contract_link: 88933 (43.0%)
- vendor_incorporation_date: 72748 (35.1%)
- vendor_bn9: 66758 (32.3%)
- award_date: 60406 (29.2%)
- vendor_emails: 50097 (24.2%)
- vendor_neq: 42495 (20.5%)
- buyer_bn_as_published: 20808 (10.1%)
- end_date: 13884 (6.7%)
- contract_value: 8059 (3.9%)
- payment_terms_as_published: 4221 (2.0%)
- ap_phone: 3113 (1.5%)
- po_required_as_published: 2415 (1.2%)
- invoice_mailing_address: 2375 (1.1%)
- invoicing_requirements: 2337 (1.1%)
- invoice_portal_url: 2073 (1.0%)
- ap_contact_name_as_published: 1061 (0.5%)

## Canada-proof families
- source field: 118410; other: 88575

## Buyer types
- organisation (type not stated in the record): 103378
- company (private sector): 36759
- company (private sector) (from the organisation's name / web domain): 30955
- non-profit / association / cultural body: 12786
- government ministry / agency: 5288
- municipality / local government (from the organisation's name / web domain): 3193
- non-profit / association / cultural body (from the organisation's name / web domain): 3061
- hospital / health authority: 2628
- utility / public corporation: 2161
- municipality / local government: 1598
- university / college: 1217
- transport / transit authority: 769
- hospital / health authority (from the organisation's name / web domain): 668
- university / college (from the organisation's name / web domain): 532
- utility / public corporation (from the organisation's name / web domain): 391
- government ministry / agency (from the organisation's name / web domain): 379
- religious organisation (from the organisation's name / web domain): 276
- First Nation / Indigenous government: 238
- transport / transit authority (from the organisation's name / web domain): 224
- school board / school district: 190
- First Nation / Indigenous government (from the organisation's name / web domain): 187
- library (from the organisation's name / web domain): 34
- school board / school district (from the organisation's name / web domain): 33
- US government body (federal, state or local): 29
- US city / county / local government: 11

## DMARC posture of the delivered mailboxes
- no DMARC record: 71740
- v=DMARC1; p=none (monitor only, no enforcement): 71557
- p=quarantine: 25900
- not checked yet: 24074
- p=reject: 13138
- DNS lookup failed: 433
- invalid DMARC record: 143
