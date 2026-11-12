# Deep audit — 259020 delivered rows in 18 packages (125 files), 2026-11-12

Result: **FAIL** — 11 hard checks, 17 soft checks; hard failures: 1. Every flagged row is listed in `audit_flags.csv` with its reasons.

| # | check | kind | rows flagged | verdict |
|---|---|---|---|---|
| 1 | header: identical columns in every file (106 since 2026-11-06) | hard | 1 | FAIL |
| 2 | mailbox syntax | hard | 0 | PASS |
| 3 | mailbox referee-confirmed (all but P11) | hard | 0 | PASS |
| 4 | mail server (MX or A) on the mailbox domain | hard | 0 | PASS |
| 4b | mail server not yet checked (row newer than the last DNS pass) | soft | 205076 | REVIEW |
| 5 | no webmail domain | hard | 0 | PASS |
| 6 | no person-like local part | hard | 0 | PASS |
| 7 | role word in the local part | soft | 20830 | REVIEW |
| 8 | receivables-looking local part graded invoicing/AP | soft | 69 | REVIEW |
| 9 | shared government domain: page or quote names the body | soft | 2 | REVIEW |
| 10 | regional token of a multinational on a differently-located body | soft | 0 | PASS |
| 11 | quote contains the address | hard | 0 | PASS |
| 11b | quote shows the label next to the address (referee saw the address on the page) | soft | 0 | PASS |
| 12 | evidence page on the organisation's domain (or its site) | soft | 12508 | REVIEW |
| 13 | email_type label matches grade | hard | 0 | PASS |
| 14 | DMARC / SPF / provider columns filled | soft | 0 | PASS |
| 15 | tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m) | soft | 0 | PASS |
| 16 | vendor named and Canada proof present | hard | 0 | PASS |
| 17 | Canada proof is a source field or the vendor's site (never a name) | soft | 0 | PASS |
| 18 | record link present for dated-record tiers | soft | 0 | PASS |
| 19 | buyer name is a name (not a domain or a page title) | soft | 28218 | REVIEW |
| 20 | legal name is not a fragment or a platform copyright | soft | 64 | REVIEW |
| 21 | one row per mailbox | hard | 0 | PASS |
| 22 | one row per organisation name (same name twice) | soft | 0 | PASS |
| 23 | one row per site domain (two rows, different mailboxes, same domain) | soft | 39 | REVIEW |
| 24 | no blank cell | hard | 0 | PASS |
| 25 | jurisdiction vs mailbox top-level domain | soft | 70 | REVIEW |
| 26 | currency filled when a value is filled | soft | 51 | REVIEW |

## Examples of flagged rows (first 12 per check)
- **1 header: identical columns in every file (106 since 2026-11-06)**
    - files | 2 distinct headers; widths [0, 253]
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
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:96 Taylor-Listug, Inc. | ap_group@taylorguitars.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:102 Cameco Corporation | ap_cameco@cameco.com
    - P01_GOLD_active_relationship_invoicing_AP_email:278 University of Saskatchewan | connectionpoint@usask.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:280 Miami-Dade County (business unit CU05010 | invsubp@miamidade.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:295 Town of Oakville | ap_inquiries@oakville.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:377 BELL TEXTRON INC | APBell@textron.com
    - P02_active_relationship_finance_accounting_email:6 Agriculture and Agri-Food Canada | directdeposit.depotdirect@canada.ca
    - P02_active_relationship_finance_accounting_email:9 Social Sciences and Humanities Research  | directdeposit-depotdirect@crsh-sshrc.gc.ca
    - P02_active_relationship_finance_accounting_email:48 Crown-Indigenous Relations and Northern  | depotdirect-directdeposit@sac-isc.gc.ca
    - P02_active_relationship_finance_accounting_email:50 Health Canada | hc.direct.deposit.requests-demande.de.depot.direct.sc@canada.ca
    - P02_active_relationship_finance_accounting_email:51 Innovation, Science and Economic Develop | ifmscustomer-clientsifm@ised-isde.gc.ca
    - P02_active_relationship_finance_accounting_email:54 Veterans Affairs Canada | directdeposit-depotdirect@vac-acc.gc.ca
- **8 receivables-looking local part graded invoicing/AP**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:57 Calgary Coin Gallery | payment@calgarycoin.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:159 birchfumigators.ca | payment@birchfumigators.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:5 Lerners Lawyers | payments@lerners.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:44 Awninginabox.ca | payment@awninginabox.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:70 Nicol Insurance | payments@nicolinsurance.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:85 Texas Tech University | payment.strategies@ttu.edu
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:87 Whitefish River First Nation | payments@whitefishriver.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:161 PSM Law | payment@psmlaw.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:164 Facility Solutions Canada Limited | payments@facilitysolutionscanada.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:166 furbabysk.ca | payments@furbabysk.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:178 Insight LLP CPA | payments@providinginsight.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:190 bakercornwall.com | payments@bakercornwall.com
- **9 shared government domain: page or quote names the body**
    - P01_GOLD_active_relationship_invoicing_AP_email:527 Tennessee Department of Transportation | pln.invoices@tn.gov ← https://www.tn.gov/tdot/long-range-planning-home/longrange-administration/longra
    - P07_client_listing_finance_or_purchasing_email:419 transportation.ky.gov | finance.crcgroup@ky.gov ← https://finance.ky.gov/eProcurement/Pages/doing-business-with-the-commonwealth.a
- **12 evidence page on the organisation's domain (or its site)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:3 ATTIS LEBLANC | payable@attis-leblanc.com on attis-leblanc.ca (site attis-leblanc.com)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:62 Oil City Drywall North | accounting@oilcitydrywall.ca on oilcitydrywallnorth.ca (site oilcitydrywall.ca)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:75 COCA-COLA LTD./ COCA-COLA LTEE | krinvoice@coca-cola.com on coca-colacompany.com (site coca-cola.com)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:102 The Mosaic Company | mosaic.accountspayable@mosaicco.com on mosaicincanada.com (site mosaicco.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:23 Capital Regional District | accountspayable@crd.bc.ca on crd.ca (site crd.bc.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:59 ibiosolutions.com | payables@ibiosolutions.com on immunebiosolutions.com (site ibiosolutions.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:89 Intermedia | ap@intermedia.com on intermedia.ca (site go.intermedia.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:104 Motorola Solutions, Inc | recepcionfacturas@motorolasolutions.com on web.archive.org (site motorolasolutions.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:151 dabc.ca | ap@dabc.ca on disabilityalliancebc.org (site dabc.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:2 Department of Defence | invoices@defence.gov.au on web.archive.org (site defence.gov.au)
    - P01_GOLD_active_relationship_invoicing_AP_email:33 Natural Sciences and Engineering Researc | payables@nserc-crsng.gc.ca on nserc-crsng.canada.ca (site nserc-crsng.gc.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:45 Ville de Montréal | facture@montreal.ca on ville.montreal.qc.ca (site montreal.ca)
- **19 buyer name is a name (not a domain or a page title)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:159 birchfumigators.ca | birchfumigators.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:160 dfcdiesel.com | dfcdiesel.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:20 lpsg.ca | lpsg.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:22 apsurveys.ca | apsurveys.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:30 guardian.law | guardian.law
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:44 Awninginabox.ca | Awninginabox.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:52 efifoodequip.com | efifoodequip.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:57 ep.com | ep.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:58 ctwater.com | ctwater.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:59 ibiosolutions.com | ibiosolutions.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:63 dumptrucks.com | dumptrucks.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:65 apextechusa.com | apextechusa.com
- **20 legal name is not a fragment or a platform copyright**
    - P05_likely_active_awarded_12_36_months_any_email:56 Ameren Illinois Company | Ameren Corporation and/or its suppliers (the copyright line of https:/
    - P05_likely_active_awarded_12_36_months_any_email:200 LOVE WORTH FINDING MINISTRIES INC | LLC. 800-274-5683 2941 Kate Bond Rd, Memphis, TN 38133 CONNECT WITH LW
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part1_of_9:390 FORMEDICA LTEE | FORMEDICA LTEE (Health Canada's Medical Devices Active Licence Listing
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part1_of_9:392 MEDSUP MEDICAL | MEDSUP MEDICAL (Health Canada's Medical Devices Active Licence Listing
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part5_of_9:1202 CENTRAL DENTAL SOLUTIONS INC. | CENTRAL DENTAL SOLUTIONS INC. (Health Canada's Medical Devices Active 
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part5_of_9:1203 REMINGTON MEDICAL EQUIPMENT LTD. | REMINGTON MEDICAL EQUIPMENT LTD. (Health Canada's Medical Devices Acti
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part5_of_9:1205 PHOENIX AIRMID BIOMEDICAL CORP. | PHOENIX AIRMID BIOMEDICAL CORP. (Health Canada's Medical Devices Activ
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part5_of_9:1206 ELIMEDICAL, INC. | ELIMEDICAL, INC. (Health Canada's Medical Devices Active Licence Listi
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part5_of_9:1208 EXCITON TECHNOLOGIES INC. | EXCITON TECHNOLOGIES INC. (Health Canada's Medical Devices Active Lice
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part5_of_9:1210 DIAGNOS INC. | DIAGNOS INC. (Health Canada's Medical Devices Active Licence Listing (
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part5_of_9:1211 OMNITECH LABS INC. | OMNITECH LABS INC. (Health Canada's Medical Devices Active Licence Lis
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part5_of_9:1216 NERV TECHNOLOGY INC. DOING BUSINESS AS F | NERV TECHNOLOGY INC. DOING BUSINESS AS FLUIDAI MEDICAL (Health Canada'
- **23 one row per site domain (two rows, different mailboxes, same domain)**
    - P01_GOLD_active_relationship_invoicing_AP_email:2 Department of Defence | defence.gov.au: 2 rows, invoices@defence.gov.au; peppol.einvoices@defence.gov.au
    - P01_GOLD_active_relationship_invoicing_AP_email:37 Ville de Gatineau | gatineau.ca: 2 rows, gatineau.factures@gatineau.ca; idgatineau@gatineau.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:45 Ville de Montréal | montreal.ca: 2 rows, facture@montreal.ca; comptesapayer@montreal.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:57 Ville de Laval | laval.ca: 3 rows, comptespayables@laval.ca; lavaleconomique@laval.ca; info@laval.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:107 Texas Department of Insurance | texas.gov: 7 rows, invoices@tdi.texas.gov; payableteam@trs.texas.gov; ap@ers.texas.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:125 University of Ottawa | uottawa.ca: 2 rows, payables@uottawa.ca; info@emba.uottawa.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:181 Oregon Department of Transportation | oregon.gov: 3 rows, opoinvoiceinquiries@odot.oregon.gov; omdaccounts.payable@omd.oregon.gov; odf.accountspayable@oregon.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:182 Texas Tech University Health Sciences Ce | ttuhsc.edu: 2 rows, accountspayableelp@ttuhsc.edu; Accounts.Payable@ttuhsc.edu
    - P01_GOLD_active_relationship_invoicing_AP_email:364 NATO Joint Warfare Centre (Stavanger) | nato.int: 3 rows, invoice@jwc.nato.int; accountspayable.mailbox@hq.nato.int; accountspayable@ncia.nato.int
    - P01_GOLD_active_relationship_invoicing_AP_email:372 Virginia Department of Energy | virginia.gov: 6 rows, accountspayable@energy.virginia.gov; ap@vsp.virginia.gov; support@dhrm.virginia.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:374 DELOITTE & TOUCHE LLP | deloitte.com: 2 rows, accountspayable@deloitte.be; financeservices@deloitte.com
    - P01_GOLD_active_relationship_invoicing_AP_email:401 Commission européenne, INTPA - Internati | europa.eu: 6 rows, ap.invoices@ecb.europa.eu; e-invoicing@emsa.europa.eu; invoices@esma.europa.eu
- **25 jurisdiction vs mailbox top-level domain**
    - P01_GOLD_active_relationship_invoicing_AP_email:300 Utilities Kingston | CA / kingston.gov.uk
    - P13_inferred_relationship_no_record_own_email_part10_of_77:170 Moment Rénovation | QC / momentrenovation.fr
    - P13_inferred_relationship_no_record_own_email_part10_of_77:761 belledebrillet.org | ON / brillet.fr
    - P13_inferred_relationship_no_record_own_email_part14_of_77:1806 Alenti | ON / alenti.fr
    - P13_inferred_relationship_no_record_own_email_part16_of_77:1560 SurePay | ON / surepay.co.uk
    - P13_inferred_relationship_no_record_own_email_part17_of_77:1460 Denso | ON / denso.co.nz
    - P13_inferred_relationship_no_record_own_email_part18_of_77:1412 LA MAISON DES JEUNES DE PLESSISVILLE INC | QC / lycos.fr
    - P13_inferred_relationship_no_record_own_email_part19_of_77:225 The Redeemed Christian Church of God Lov | SK / loveassembly.co.uk
    - P13_inferred_relationship_no_record_own_email_part1_of_77:163 Miele | ON / miele.de
    - P13_inferred_relationship_no_record_own_email_part1_of_77:310 ONEJOON | QC / onejoon.de
    - P13_inferred_relationship_no_record_own_email_part1_of_77:1448 Mole Valley District Council | SK / molevalley.gov.uk
    - P13_inferred_relationship_no_record_own_email_part22_of_77:1895 OPAL | QC / opal.fr
- **26 currency filled when a value is filled**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:45 RENTON SCHOOL DISTRICT #403 | 332345.13 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:444 Rectorado de la Universitat de València | 12698.25 (source field: PayableAmount)
    - P01_GOLD_active_relationship_invoicing_AP_email:455 BELLEVUE, CITY OF | 35488873.2 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:457 UNIVERSITY PLACE SCHOOL DISTRICT #83 | 685477.9 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:463 BELLEVUE SCHOOL DISTRICT #405 | 5395.88 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:466 SNOQUALMIE VALLEY SCHOOL DISTRICT #410 | 23980.42 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:468 SHORELINE SCHOOL DISTRICT #412 | 919904.69 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:485 University of North Dakota | 145.850 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:488 North Dakota State University | 35.000 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:551 BANCOLOMBIA S.A. | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:557 ECOPETROL S A | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:600 MARYLAND STADIUM AUTHORITY | 251569.05 (source field: amount)

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
- P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email: 190
- P01T_active_service_seen_on_buyer_site_invoicing_AP_email: 202
- P01_GOLD_active_relationship_invoicing_AP_email: 624
- P02_active_relationship_finance_accounting_email: 464
- P03_active_relationship_purchasing_email: 262
- P04_active_relationship_general_email: 3556
- P05_likely_active_awarded_12_36_months_any_email: 419
- P06M_member_or_regulated_payer_of_canadian_body_other_email: 18956
- P06T_active_service_seen_on_buyer_site_other_email: 43465
- P06_client_listing_invoicing_AP_email: 253
- P07_client_listing_finance_or_purchasing_email: 660
- P08_client_listing_general_email: 21363
- P09_older_contract_or_payment_any_email: 278
- P10R_ca_domain_registration_contract_own_email: 0
- P10_linked_from_vendor_site_any_email: 2137
- P11_any_relationship_email_not_yet_confirmed: 1596
- P12_weaker_relationship_within_5_years_own_email: 16
- P13_inferred_relationship_no_record_own_email: 164579

## Field fill across all delivered rows (value present, not `not_published`)
- buyer_website: 259020 (100.0%)
- vendor_address: 257455 (99.4%)
- vendor_website: 245908 (94.9%)
- buyer_address: 233474 (90.1%)
- vendor_legal_name: 226102 (87.3%)
- vendor_phone: 210322 (81.2%)
- vendor_registry_id: 201787 (77.9%)
- vendor_logo_url: 190683 (73.6%)
- buyer_logo_url: 178556 (68.9%)
- buyer_phone: 142355 (55.0%)
- vendor_incorporation_date: 111949 (43.2%)
- vendor_bn9: 109046 (42.1%)
- buyer_legal_name_as_published: 108671 (42.0%)
- contract_link: 94441 (36.5%)
- award_date: 67285 (26.0%)
- vendor_emails: 55000 (21.2%)
- vendor_neq: 52037 (20.1%)
- buyer_bn_as_published: 27718 (10.7%)
- end_date: 16656 (6.4%)
- contract_value: 8182 (3.2%)
- payment_terms_as_published: 4796 (1.9%)
- ap_phone: 3094 (1.2%)
- po_required_as_published: 2719 (1.0%)
- invoicing_requirements: 2312 (0.9%)
- invoice_mailing_address: 2308 (0.9%)
- invoice_portal_url: 2191 (0.8%)
- ap_contact_name_as_published: 1098 (0.4%)

## Canada-proof families
- source field: 141195; other: 117825

## Buyer types
- organisation (type not stated in the record): 140692
- company (private sector): 44152
- company (private sector) (from the organisation's name / web domain): 33073
- non-profit / association / cultural body: 14496
- government ministry / agency: 6475
- municipality / local government (from the organisation's name / web domain): 3672
- non-profit / association / cultural body (from the organisation's name / web domain): 3292
- hospital / health authority: 2954
- utility / public corporation: 2579
- municipality / local government: 1647
- university / college: 1442
- transport / transit authority: 921
- hospital / health authority (from the organisation's name / web domain): 765
- university / college (from the organisation's name / web domain): 546
- utility / public corporation (from the organisation's name / web domain): 486
- government ministry / agency (from the organisation's name / web domain): 442
- religious organisation (from the organisation's name / web domain): 329
- transport / transit authority (from the organisation's name / web domain): 275
- First Nation / Indigenous government: 271
- First Nation / Indigenous government (from the organisation's name / web domain): 211
- school board / school district: 195
- library (from the organisation's name / web domain): 33
- school board / school district (from the organisation's name / web domain): 32
- US government body (federal, state or local): 29
- US city / county / local government: 11

## DMARC posture of the delivered mailboxes
- no DMARC record: 105192
- v=DMARC1; p=none (monitor only, no enforcement): 101235
- p=quarantine: 35257
- p=reject: 17055
- invalid DMARC record: 191
- DNS lookup failed: 90
