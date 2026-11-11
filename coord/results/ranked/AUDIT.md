# Deep audit — 178227 delivered rows in 18 packages (81 files), 2026-11-11

Result: **FAIL** — 11 hard checks, 17 soft checks; hard failures: 1. Every flagged row is listed in `audit_flags.csv` with its reasons.

| # | check | kind | rows flagged | verdict |
|---|---|---|---|---|
| 1 | header: identical columns in every file (106 since 2026-11-06) | hard | 1 | FAIL |
| 2 | mailbox syntax | hard | 0 | PASS |
| 3 | mailbox referee-confirmed (all but P11) | hard | 0 | PASS |
| 4 | mail server (MX or A) on the mailbox domain | hard | 0 | PASS |
| 4b | mail server not yet checked (row newer than the last DNS pass) | soft | 128282 | REVIEW |
| 5 | no webmail domain | hard | 0 | PASS |
| 6 | no person-like local part | hard | 0 | PASS |
| 7 | role word in the local part | soft | 12259 | REVIEW |
| 8 | receivables-looking local part graded invoicing/AP | soft | 53 | REVIEW |
| 9 | shared government domain: page or quote names the body | soft | 3 | REVIEW |
| 10 | regional token of a multinational on a differently-located body | soft | 0 | PASS |
| 11 | quote contains the address | hard | 0 | PASS |
| 11b | quote shows the label next to the address (referee saw the address on the page) | soft | 0 | PASS |
| 12 | evidence page on the organisation's domain (or its site) | soft | 7800 | REVIEW |
| 13 | email_type label matches grade | hard | 0 | PASS |
| 14 | DMARC / SPF / provider columns filled | soft | 0 | PASS |
| 15 | tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m) | soft | 0 | PASS |
| 16 | vendor named and Canada proof present | hard | 0 | PASS |
| 17 | Canada proof is a source field or the vendor's site (never a name) | soft | 0 | PASS |
| 18 | record link present for dated-record tiers | soft | 0 | PASS |
| 19 | buyer name is a name (not a domain or a page title) | soft | 17171 | REVIEW |
| 20 | legal name is not a fragment or a platform copyright | soft | 43 | REVIEW |
| 21 | one row per mailbox | hard | 0 | PASS |
| 22 | one row per organisation name (same name twice) | soft | 71 | REVIEW |
| 23 | one row per site domain (two rows, different mailboxes, same domain) | soft | 62 | REVIEW |
| 24 | no blank cell | hard | 0 | PASS |
| 25 | jurisdiction vs mailbox top-level domain | soft | 44 | REVIEW |
| 26 | currency filled when a value is filled | soft | 50 | REVIEW |

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
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:90 Cameco Corporation | ap_cameco@cameco.com
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
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:18 Lerners Lawyers | payments@lerners.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:24 Whitefish River First Nation | payments@whitefishriver.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:150 Facility Solutions Canada Limited | payments@facilitysolutionscanada.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:152 Furbaby Pet Care Saskatoon | payments@furbabysk.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:165 Insight LLP CPA | payments@providinginsight.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:178 bakercornwall.com | payments@bakercornwall.com
    - P01_GOLD_active_relationship_invoicing_AP_email:39 Environment and Climate Change Canada | renseignement-paiements-payments-inquiry@ec.gc.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:215 County of Minburn No. 27 | payments@minburncounty.ab.ca
- **9 shared government domain: page or quote names the body**
    - P01_GOLD_active_relationship_invoicing_AP_email:43 Canadian Space Agency | invoicing.csa-asc.facturation@canada.ca ← https://www.canada.ca/en/public-services-procurement/services/payments-to-from-g
    - P01_GOLD_active_relationship_invoicing_AP_email:513 Tennessee Department of Transportation | pln.invoices@tn.gov ← https://www.tn.gov/tdot/long-range-planning-home/longrange-administration/longra
    - P07_client_listing_finance_or_purchasing_email:13 transportation.ky.gov | finance.crcgroup@ky.gov ← https://finance.ky.gov/eProcurement/Pages/doing-business-with-the-commonwealth.a
- **12 evidence page on the organisation's domain (or its site)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:19 ATTIS LEBLANC | payable@attis-leblanc.com on attis-leblanc.ca (site attis-leblanc.com)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:81 COCA-COLA LTD./ COCA-COLA LTEE | krinvoice@coca-cola.com on coca-colacompany.com (site coca-cola.com)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:87 Oil City Drywall North | accounting@oilcitydrywall.ca on oilcitydrywallnorth.ca (site oilcitydrywall.ca)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:126 Birth Supplies Canada | ap@birthsuppliescanada.ca on midwiferysupplies.ca (site birthsuppliescanada.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:43 Capital Regional District | accountspayable@crd.bc.ca on crd.ca (site crd.bc.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:51 ibiosolutions.com | payables@ibiosolutions.com on immunebiosolutions.com (site ibiosolutions.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:81 dabc.ca | ap@dabc.ca on disabilityalliancebc.org (site dabc.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:92 Motorola Solutions, Inc | recepcionfacturas@motorolasolutions.com on web.archive.org (site motorolasolutions.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:189 bimbc.ca | finance@bimbc.ca on bowenislandmunicipality.ca (site bimbc.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:2 Department of Defence | invoices@defence.gov.au on web.archive.org (site defence.gov.au)
    - P01_GOLD_active_relationship_invoicing_AP_email:3 Department of Industry, Science and Reso | einvoicingqueries@industry.gov.au on directory.peppol.eu (site industry.gov.au)
    - P01_GOLD_active_relationship_invoicing_AP_email:51 Natural Sciences and Engineering Researc | payables@nserc-crsng.gc.ca on nserc-crsng.canada.ca (site nserc-crsng.gc.ca)
- **19 buyer name is a name (not a domain or a page title)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:68 birchfumigators.ca | birchfumigators.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:69 dfcdiesel.com | dfcdiesel.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:12 airweld.com | airweld.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:14 Awninginabox.ca | Awninginabox.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:20 efifoodequip.com | efifoodequip.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:38 lpsg.ca | lpsg.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:41 apsurveys.ca | apsurveys.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:44 ep.com | ep.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:45 ctwater.com | ctwater.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:51 ibiosolutions.com | ibiosolutions.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:57 guardian.law | guardian.law
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:61 my.honorhealth.com | my.honorhealth.com
- **20 legal name is not a fragment or a platform copyright**
    - P05_likely_active_awarded_12_36_months_any_email:58 Ameren Illinois Company | Ameren Corporation and/or its suppliers
    - P05_likely_active_awarded_12_36_months_any_email:339 LOVE WORTH FINDING MINISTRIES INC | LLC. 800-274-5683 2941 Kate Bond Rd, Memphis, TN 38133 CONNECT WITH LW
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part5_of_7:1355 +ARTHRI-PLUS INC. | +ARTHRI-PLUS INC. (the Canadian trademarks register (owner of record),
    - P06T_active_service_seen_on_buyer_site_other_email_part11_of_14:267 Landscaping | LTD Landscaping Inc. (as registered: Corporations Canada (open data), 
    - P06T_active_service_seen_on_buyer_site_other_email_part11_of_14:2148 Reimer Construction | Introduction Welcome to Reimer Construction (stated on https://reimerc
    - P06T_active_service_seen_on_buyer_site_other_email_part12_of_14:65 Punta Cana Spa | Introduction Welcome to Punta Cana Spa (stated on https://puntacanaspa
    - P06T_active_service_seen_on_buyer_site_other_email_part12_of_14:843 Caleb Creations | Introduction Welcome to Caleb Creations (stated on https://calebcreati
    - P06T_active_service_seen_on_buyer_site_other_email_part13_of_14:970 Toronto Comedy Festival | Introduction Welcome to the Toronto Comedy Festival (stated on https:/
    - P06T_active_service_seen_on_buyer_site_other_email_part14_of_14:198 The Barkshire Club | Introduction Welcome to The Barkshire Club (stated on https://thebarks
    - P06T_active_service_seen_on_buyer_site_other_email_part14_of_14:680 We Will Walk You | Introduction Welcome to We Will Walk You (stated on https://www.wewill
    - P06T_active_service_seen_on_buyer_site_other_email_part14_of_14:2435 Feb 2th, 2024 Acceptance of Terms Welcom | Feb 2th, 2024 Acceptance of Terms Welcome to NTWIST (stated on https:/
    - P06T_active_service_seen_on_buyer_site_other_email_part1_of_14:1454 Beet & Yarrow | Introduction Welcome to Beet & Yarrow. Beet & Yarrow (stated on https:
- **22 one row per organisation name (same name twice)**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:191 Cascades | 2 rows, same mail domain: cascades.com
    - P01_GOLD_active_relationship_invoicing_AP_email:16 Rocky View County | 2 rows, same mail domain: rockyview.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:26 University of Lethbridge | 2 rows, same mail domain: uleth.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:234 Metrolinx | 2 rows, same mail domain: metrolinx.com
    - P01_GOLD_active_relationship_invoicing_AP_email:257 City of Brantford | 2 rows, same mail domain: brantford.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:277 City of Port Moody | 2 rows, same mail domain: portmoody.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:284 Township of Scugog | 2 rows, same mail domain: scugog.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:498 City of Edmonton | 2 rows, same mail domain: edmonton.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:617 Nicola Valley Institute of Technology | 2 rows, same mail domain: nvit.ca
    - P02_active_relationship_finance_accounting_email:137 Ville de Princeville | 2 rows, same mail domain: princeville.quebec
    - P02_active_relationship_finance_accounting_email:334 Regional District of North Okanagan | 2 rows, same mail domain: rdno.ca
    - P02_active_relationship_finance_accounting_email:405 Municipality of South Dundas | 2 rows, same mail domain: southdundas.com
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
    - P13_inferred_relationship_no_record_own_email_part10_of_37:2437 Alenti | ON / alenti.fr
    - P13_inferred_relationship_no_record_own_email_part10_of_37:2484 Rep iPhone Médoc | QC / rep-iphone.fr
    - P13_inferred_relationship_no_record_own_email_part11_of_37:727 Wajos | ON / wajos.de
    - P13_inferred_relationship_no_record_own_email_part12_of_37:2330 Denso | ON / denso.co.nz
    - P13_inferred_relationship_no_record_own_email_part13_of_37:12 The Islands of The Bahamas | ON / bahamas.co.uk
    - P13_inferred_relationship_no_record_own_email_part16_of_37:1267 OPAL | QC / opal.fr
    - P13_inferred_relationship_no_record_own_email_part17_of_37:2230 Charles Faram | ON / charlesfaram.co.uk
    - P13_inferred_relationship_no_record_own_email_part18_of_37:483 Wireline Services Group | ON / wirelineservices.com.au
    - P13_inferred_relationship_no_record_own_email_part18_of_37:1278 M&G Marketing | QC / mgmarketing.fr
    - P13_inferred_relationship_no_record_own_email_part19_of_37:1159 Dominion | QC / dominion.fr
    - P13_inferred_relationship_no_record_own_email_part1_of_37:150 Met Office | QC / metoffice.gov.uk
- **26 currency filled when a value is filled**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:96 RENTON SCHOOL DISTRICT #403 | 332345.13 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:444 Rectorado de la Universitat de València | 12698.25 (source field: PayableAmount)
    - P01_GOLD_active_relationship_invoicing_AP_email:456 BRINKS DE COLOMBIA S.A. | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:475 University of North Dakota | 145.850 (source field: Amount)
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
- P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email: 129
- P01T_active_service_seen_on_buyer_site_invoicing_AP_email: 192
- P01_GOLD_active_relationship_invoicing_AP_email: 626
- P02_active_relationship_finance_accounting_email: 466
- P03_active_relationship_purchasing_email: 263
- P04_active_relationship_general_email: 3723
- P05_likely_active_awarded_12_36_months_any_email: 422
- P06M_member_or_regulated_payer_of_canadian_body_other_email: 14643
- P06T_active_service_seen_on_buyer_site_other_email: 36661
- P06_client_listing_invoicing_AP_email: 273
- P07_client_listing_finance_or_purchasing_email: 696
- P08_client_listing_general_email: 22009
- P09_older_contract_or_payment_any_email: 307
- P10R_ca_domain_registration_contract_own_email: 0
- P10_linked_from_vendor_site_any_email: 2390
- P11_any_relationship_email_not_yet_confirmed: 1455
- P12_weaker_relationship_within_5_years_own_email: 15
- P13_inferred_relationship_no_record_own_email: 93957

## Field fill across all delivered rows (value present, not `not_published`)
- buyer_website: 178227 (100.0%)
- vendor_address: 176528 (99.0%)
- vendor_website: 168682 (94.6%)
- buyer_address: 155095 (87.0%)
- buyer_logo_url: 149186 (83.7%)
- vendor_phone: 141084 (79.2%)
- vendor_logo_url: 131838 (74.0%)
- buyer_phone: 121958 (68.4%)
- buyer_legal_name_as_published: 90207 (50.6%)
- contract_link: 84270 (47.3%)
- vendor_legal_name: 82553 (46.3%)
- vendor_registry_id: 64985 (36.5%)
- vendor_incorporation_date: 64966 (36.5%)
- vendor_bn9: 58926 (33.1%)
- award_date: 55983 (31.4%)
- vendor_emails: 45200 (25.4%)
- vendor_neq: 37142 (20.8%)
- buyer_bn_as_published: 20583 (11.5%)
- end_date: 13316 (7.5%)
- contract_value: 7661 (4.3%)
- payment_terms_as_published: 4173 (2.3%)
- ap_phone: 3096 (1.7%)
- po_required_as_published: 2397 (1.3%)
- invoice_mailing_address: 2360 (1.3%)
- invoicing_requirements: 2328 (1.3%)
- invoice_portal_url: 2068 (1.2%)
- ap_contact_name_as_published: 1037 (0.6%)

## Canada-proof families
- source field: 104852; other: 73375

## Buyer types
- organisation (type not stated in the record): 86586
- company (private sector): 32875
- company (private sector) (from the organisation's name / web domain): 28076
- non-profit / association / cultural body: 11464
- government ministry / agency: 4565
- non-profit / association / cultural body (from the organisation's name / web domain): 2690
- hospital / health authority: 2310
- utility / public corporation: 1931
- municipality / local government (from the organisation's name / web domain): 1670
- municipality / local government: 1525
- university / college: 1061
- transport / transit authority: 643
- hospital / health authority (from the organisation's name / web domain): 554
- university / college (from the organisation's name / web domain): 501
- government ministry / agency (from the organisation's name / web domain): 340
- utility / public corporation (from the organisation's name / web domain): 335
- religious organisation (from the organisation's name / web domain): 235
- First Nation / Indigenous government: 220
- transport / transit authority (from the organisation's name / web domain): 194
- school board / school district: 189
- First Nation / Indigenous government (from the organisation's name / web domain): 159
- library (from the organisation's name / web domain): 33
- school board / school district (from the organisation's name / web domain): 31
- US government body (federal, state or local): 29
- US city / county / local government: 11

## DMARC posture of the delivered mailboxes
- v=DMARC1; p=none (monitor only, no enforcement): 69938
- no DMARC record: 69828
- p=quarantine: 25336
- p=reject: 12938
- invalid DMARC record: 137
- DNS lookup failed: 50
