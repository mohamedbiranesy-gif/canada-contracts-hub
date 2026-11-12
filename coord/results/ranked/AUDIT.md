# Deep audit — 260141 delivered rows in 18 packages (124 files), 2026-11-12

Result: **FAIL** — 11 hard checks, 17 soft checks; hard failures: 1. Every flagged row is listed in `audit_flags.csv` with its reasons.

| # | check | kind | rows flagged | verdict |
|---|---|---|---|---|
| 1 | header: identical columns in every file (106 since 2026-11-06) | hard | 1 | FAIL |
| 2 | mailbox syntax | hard | 0 | PASS |
| 3 | mailbox referee-confirmed (all but P11) | hard | 0 | PASS |
| 4 | mail server (MX or A) on the mailbox domain | hard | 0 | PASS |
| 4b | mail server not yet checked (row newer than the last DNS pass) | soft | 206099 | REVIEW |
| 5 | no webmail domain | hard | 0 | PASS |
| 6 | no person-like local part | hard | 0 | PASS |
| 7 | role word in the local part | soft | 20909 | REVIEW |
| 8 | receivables-looking local part graded invoicing/AP | soft | 69 | REVIEW |
| 9 | shared government domain: page or quote names the body | soft | 2 | REVIEW |
| 10 | regional token of a multinational on a differently-located body | soft | 0 | PASS |
| 11 | quote contains the address | hard | 0 | PASS |
| 11b | quote shows the label next to the address (referee saw the address on the page) | soft | 0 | PASS |
| 12 | evidence page on the organisation's domain (or its site) | soft | 12472 | REVIEW |
| 13 | email_type label matches grade | hard | 0 | PASS |
| 14 | DMARC / SPF / provider columns filled | soft | 0 | PASS |
| 15 | tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m) | soft | 0 | PASS |
| 16 | vendor named and Canada proof present | hard | 0 | PASS |
| 17 | Canada proof is a source field or the vendor's site (never a name) | soft | 0 | PASS |
| 18 | record link present for dated-record tiers | soft | 0 | PASS |
| 19 | buyer name is a name (not a domain or a page title) | soft | 28124 | REVIEW |
| 20 | legal name is not a fragment or a platform copyright | soft | 140 | REVIEW |
| 21 | one row per mailbox | hard | 0 | PASS |
| 22 | one row per organisation name (same name twice) | soft | 0 | PASS |
| 23 | one row per site domain (two rows, different mailboxes, same domain) | soft | 42 | REVIEW |
| 24 | no blank cell | hard | 0 | PASS |
| 25 | jurisdiction vs mailbox top-level domain | soft | 69 | REVIEW |
| 26 | currency filled when a value is filled | soft | 51 | REVIEW |

## Examples of flagged rows (first 12 per check)
- **1 header: identical columns in every file (106 since 2026-11-06)**
    - files | 2 distinct headers; widths [0, 253]
- **4b mail server not yet checked (row newer than the last DNS pass)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:2 Braemed Ltd. | braemed.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:3 Intersurgical Ltd. | intersurgical.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:4 INTER PIPELINE (Corridor) INC. (re COR & | interpipeline.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:7 ATTIS LEBLANC | attis-leblanc.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:11 Cologix Canada inc. | cologix.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:13 Edmond Nolin Ltée | constructionenl.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:16 Daikin Applied Canada inc. | daikinapplied.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:17 Deblois réfrigération inc. | debloisrefrigeration.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:19 Construction D.M. Turcotte J.M. inc. | dmturcotte.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:20 Dyno Nobel Canada inc. | dynonobel.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:22 Constructions Fabmec inc. | fabmec.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:23 Filspec inc. | filspec.com
- **7 role word in the local part**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:129 Taylor-Listug, Inc. | ap_group@taylorguitars.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:101 Cameco Corporation | ap_cameco@cameco.com
    - P01_GOLD_active_relationship_invoicing_AP_email:275 University of Saskatchewan | connectionpoint@usask.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:277 Miami-Dade County (business unit CU05010 | invsubp@miamidade.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:291 Town of Oakville | ap_inquiries@oakville.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:378 BELL TEXTRON INC | APBell@textron.com
    - P02_active_relationship_finance_accounting_email:6 Agriculture and Agri-Food Canada | directdeposit.depotdirect@canada.ca
    - P02_active_relationship_finance_accounting_email:9 Social Sciences and Humanities Research  | directdeposit-depotdirect@crsh-sshrc.gc.ca
    - P02_active_relationship_finance_accounting_email:47 Crown-Indigenous Relations and Northern  | depotdirect-directdeposit@sac-isc.gc.ca
    - P02_active_relationship_finance_accounting_email:49 Health Canada | hc.direct.deposit.requests-demande.de.depot.direct.sc@canada.ca
    - P02_active_relationship_finance_accounting_email:50 Innovation, Science and Economic Develop | ifmscustomer-clientsifm@ised-isde.gc.ca
    - P02_active_relationship_finance_accounting_email:53 Veterans Affairs Canada | directdeposit-depotdirect@vac-acc.gc.ca
- **8 receivables-looking local part graded invoicing/AP**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:62 Calgary Coin Gallery | payment@calgarycoin.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:195 Empress | payments@villageofempress.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:205 birchfumigators.ca | payment@birchfumigators.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:5 Lerners Lawyers | payments@lerners.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:43 Awninginabox.ca | payment@awninginabox.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:69 Nicol Insurance | payments@nicolinsurance.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:84 Texas Tech University | payment.strategies@ttu.edu
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:86 Whitefish River First Nation | payments@whitefishriver.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:158 PSM Law | payment@psmlaw.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:161 Facility Solutions Canada Limited | payments@facilitysolutionscanada.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:163 furbabysk.ca | payments@furbabysk.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:175 Insight LLP CPA | payments@providinginsight.ca
- **9 shared government domain: page or quote names the body**
    - P01_GOLD_active_relationship_invoicing_AP_email:536 Tennessee Department of Transportation | pln.invoices@tn.gov ← https://www.tn.gov/tdot/long-range-planning-home/longrange-administration/longra
    - P07_client_listing_finance_or_purchasing_email:446 transportation.ky.gov | finance.crcgroup@ky.gov ← https://finance.ky.gov/eProcurement/Pages/doing-business-with-the-commonwealth.a
- **12 evidence page on the organisation's domain (or its site)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:3 Intersurgical Ltd. | finance@intersurgical.ca on ca.intersurgical.com (site intersurgical.ca)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:7 ATTIS LEBLANC | payable@attis-leblanc.com on attis-leblanc.ca (site attis-leblanc.com)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:67 Oil City Drywall North | accounting@oilcitydrywall.ca on oilcitydrywallnorth.ca (site oilcitydrywall.ca)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:95 ED'S Concrete Products Ltd. | ap@edsconcrete.com on edsconcrete.ca (site edsconcrete.com)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:102 COCA-COLA LTD./ COCA-COLA LTEE | krinvoice@coca-cola.com on coca-colacompany.com (site coca-cola.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:22 Capital Regional District | accountspayable@crd.bc.ca on crd.ca (site crd.bc.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:58 ibiosolutions.com | payables@ibiosolutions.com on immunebiosolutions.com (site ibiosolutions.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:88 Intermedia | ap@intermedia.com on intermedia.ca (site go.intermedia.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:148 dabc.ca | ap@dabc.ca on disabilityalliancebc.org (site dabc.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:32 Natural Sciences and Engineering Researc | payables@nserc-crsng.gc.ca on nserc-crsng.canada.ca (site nserc-crsng.gc.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:45 Ville de Montréal | facture@montreal.ca on ville.montreal.qc.ca (site montreal.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:67 Ville de Farnham | comptespayables@ville.farnham.qc.ca on web.archive.org (site ville.farnham.qc.ca)
- **19 buyer name is a name (not a domain or a page title)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:205 birchfumigators.ca | birchfumigators.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:206 dfcdiesel.com | dfcdiesel.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:19 lpsg.ca | lpsg.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:21 apsurveys.ca | apsurveys.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:29 guardian.law | guardian.law
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:43 Awninginabox.ca | Awninginabox.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:51 efifoodequip.com | efifoodequip.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:56 ep.com | ep.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:57 ctwater.com | ctwater.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:58 ibiosolutions.com | ibiosolutions.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:62 dumptrucks.com | dumptrucks.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:64 apextechusa.com | apextechusa.com
- **20 legal name is not a fragment or a platform copyright**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:2 Braemed Ltd. | Braemed Ltd. (Health Canada's Medical Devices Establishment Licence li
    - P05_likely_active_awarded_12_36_months_any_email:60 Ameren Illinois Company | Ameren Corporation and/or its suppliers (the copyright line of https:/
    - P05_likely_active_awarded_12_36_months_any_email:209 LOVE WORTH FINDING MINISTRIES INC | LLC. 800-274-5683 2941 Kate Bond Rd, Memphis, TN 38133 CONNECT WITH LW
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part1_of_9:3 Centennial Optical Ltd. | Centennial Optical Ltd. (Health Canada's Medical Devices Establishment
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part1_of_9:433 Csp Medical | Csp Medical (Health Canada's Medical Devices Establishment Licence lis
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part1_of_9:434 Harding Medical Supplies, A Division Of  | Harding Medical Supplies, A Division Of Imp Group Limited (Health Cana
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part1_of_9:435 Rescue 7 Inc. | Rescue 7 Inc. (Health Canada's Medical Devices Establishment Licence l
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part1_of_9:438 Ultraray Group Inc. | Ultraray Group Inc. (Health Canada's Medical Devices Establishment Lic
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part1_of_9:439 Clarion Medical Technologies Inc. | Clarion Medical Technologies Inc. (Health Canada's Medical Devices Est
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part1_of_9:440 Advanced Medical Solutions Inc. O/A Mnn, | Advanced Medical Solutions Inc. O/A Mnn, Eams (Health Canada's Medical
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part1_of_9:441 Innomar Strategies Inc. | Innomar Strategies Inc. (Health Canada's Medical Devices Establishment
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part1_of_9:442 Michel Cullen Medical Inc. | Michel Cullen Medical Inc. (Health Canada's Medical Devices Establishm
- **23 one row per site domain (two rows, different mailboxes, same domain)**
    - P01_GOLD_active_relationship_invoicing_AP_email:36 Ville de Gatineau | gatineau.ca: 2 rows, gatineau.factures@gatineau.ca; idgatineau@gatineau.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:45 Ville de Montréal | montreal.ca: 2 rows, facture@montreal.ca; comptesapayer@montreal.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:58 Ville de Laval | laval.ca: 3 rows, comptespayables@laval.ca; lavaleconomique@laval.ca; info@laval.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:110 Texas Department of Insurance | texas.gov: 7 rows, invoices@tdi.texas.gov; payableteam@trs.texas.gov; ap@ers.texas.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:125 University of Ottawa | uottawa.ca: 2 rows, payables@uottawa.ca; info@emba.uottawa.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:181 Oregon Department of Transportation | oregon.gov: 3 rows, opoinvoiceinquiries@odot.oregon.gov; omdaccounts.payable@omd.oregon.gov; odf.accountspayable@oregon.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:182 Texas Tech University Health Sciences Ce | ttuhsc.edu: 2 rows, accountspayableelp@ttuhsc.edu; accounts.payable@ttuhsc.edu
    - P01_GOLD_active_relationship_invoicing_AP_email:242 Newfoundland and Labrador Hydro | nlhydro.com: 2 rows, hydroapinvoices@nlh.nl.ca; NalcorAPInvoices@nalcorenergy.com
    - P01_GOLD_active_relationship_invoicing_AP_email:363 NATO Joint Warfare Centre (Stavanger) | nato.int: 3 rows, invoice@jwc.nato.int; accountspayable.mailbox@hq.nato.int; accountspayable@ncia.nato.int
    - P01_GOLD_active_relationship_invoicing_AP_email:364 Commonwealth of Australia (Royal Austral | defence.gov.au: 2 rows, invoices@defence.gov.au; procurement.asdefcon@defence.gov.au
    - P01_GOLD_active_relationship_invoicing_AP_email:372 Virginia Department of Energy | virginia.gov: 6 rows, accountspayable@energy.virginia.gov; ap@vsp.virginia.gov; support@dhrm.virginia.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:375 DELOITTE & TOUCHE LLP | deloitte.com: 2 rows, accountspayable@deloitte.be; financeservices@deloitte.com
- **25 jurisdiction vs mailbox top-level domain**
    - P01_GOLD_active_relationship_invoicing_AP_email:295 Utilities Kingston | CA / kingston.gov.uk
    - P13_inferred_relationship_no_record_own_email_part10_of_76:41 Moment Rénovation | QC / momentrenovation.fr
    - P13_inferred_relationship_no_record_own_email_part10_of_76:631 belledebrillet.org | ON / brillet.fr
    - P13_inferred_relationship_no_record_own_email_part14_of_76:1635 Alenti | ON / alenti.fr
    - P13_inferred_relationship_no_record_own_email_part16_of_76:1348 SurePay | ON / surepay.co.uk
    - P13_inferred_relationship_no_record_own_email_part17_of_76:1213 Denso | ON / denso.co.nz
    - P13_inferred_relationship_no_record_own_email_part18_of_76:1161 LA MAISON DES JEUNES DE PLESSISVILLE INC | QC / lycos.fr
    - P13_inferred_relationship_no_record_own_email_part18_of_76:2100 The Redeemed Christian Church of God Lov | SK / loveassembly.co.uk
    - P13_inferred_relationship_no_record_own_email_part1_of_76:164 Miele | ON / miele.de
    - P13_inferred_relationship_no_record_own_email_part1_of_76:303 ONEJOON | QC / onejoon.de
    - P13_inferred_relationship_no_record_own_email_part1_of_76:1424 Mole Valley District Council | SK / molevalley.gov.uk
    - P13_inferred_relationship_no_record_own_email_part22_of_76:1508 OPAL | QC / opal.fr
- **26 currency filled when a value is filled**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:44 RENTON SCHOOL DISTRICT #403 | 332345.13 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:446 Rectorado de la Universitat de València | 12698.25 (source field: PayableAmount)
    - P01_GOLD_active_relationship_invoicing_AP_email:458 BELLEVUE, CITY OF | 35488873.2 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:460 UNIVERSITY PLACE SCHOOL DISTRICT #83 | 685477.9 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:466 BELLEVUE SCHOOL DISTRICT #405 | 5395.88 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:469 SNOQUALMIE VALLEY SCHOOL DISTRICT #410 | 23980.42 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:471 SHORELINE SCHOOL DISTRICT #412 | 919904.69 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:472 MARYLAND STADIUM AUTHORITY | 251569.05 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:492 University of North Dakota | 145.850 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:495 North Dakota State University | 35.000 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:503 BRINKS DE COLOMBIA S.A. | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:561 BANCOLOMBIA S.A. | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)

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
- P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email: 218
- P01T_active_service_seen_on_buyer_site_invoicing_AP_email: 197
- P01_GOLD_active_relationship_invoicing_AP_email: 625
- P02_active_relationship_finance_accounting_email: 468
- P03_active_relationship_purchasing_email: 264
- P04_active_relationship_general_email: 3568
- P05_likely_active_awarded_12_36_months_any_email: 424
- P06M_member_or_regulated_payer_of_canadian_body_other_email: 20094
- P06T_active_service_seen_on_buyer_site_other_email: 43524
- P06_client_listing_invoicing_AP_email: 251
- P07_client_listing_finance_or_purchasing_email: 679
- P08_client_listing_general_email: 22779
- P09_older_contract_or_payment_any_email: 276
- P10R_ca_domain_registration_contract_own_email: 0
- P10_linked_from_vendor_site_any_email: 2134
- P11_any_relationship_email_not_yet_confirmed: 1612
- P12_weaker_relationship_within_5_years_own_email: 11
- P13_inferred_relationship_no_record_own_email: 163017

## Field fill across all delivered rows (value present, not `not_published`)
- buyer_website: 260141 (100.0%)
- vendor_address: 258579 (99.4%)
- vendor_website: 245822 (94.5%)
- buyer_address: 234379 (90.1%)
- vendor_legal_name: 225260 (86.6%)
- vendor_phone: 209633 (80.6%)
- vendor_registry_id: 200726 (77.2%)
- vendor_logo_url: 190645 (73.3%)
- buyer_logo_url: 178846 (68.7%)
- buyer_phone: 142819 (54.9%)
- vendor_incorporation_date: 111702 (42.9%)
- buyer_legal_name_as_published: 109695 (42.2%)
- vendor_bn9: 108672 (41.8%)
- contract_link: 97124 (37.3%)
- award_date: 70263 (27.0%)
- vendor_emails: 55748 (21.4%)
- vendor_neq: 51777 (19.9%)
- buyer_bn_as_published: 27518 (10.6%)
- end_date: 17136 (6.6%)
- contract_value: 8614 (3.3%)
- payment_terms_as_published: 4769 (1.8%)
- ap_phone: 3034 (1.2%)
- po_required_as_published: 2705 (1.0%)
- invoice_mailing_address: 2254 (0.9%)
- invoicing_requirements: 2252 (0.9%)
- invoice_portal_url: 2186 (0.8%)
- ap_contact_name_as_published: 1089 (0.4%)

## Canada-proof families
- source field: 142313; other: 117828

## Buyer types
- organisation (type not stated in the record): 140643
- company (private sector): 45243
- company (private sector) (from the organisation's name / web domain): 32942
- non-profit / association / cultural body: 14567
- government ministry / agency: 6560
- municipality / local government (from the organisation's name / web domain): 3665
- non-profit / association / cultural body (from the organisation's name / web domain): 3288
- hospital / health authority: 2963
- utility / public corporation: 2604
- municipality / local government: 1670
- university / college: 1443
- transport / transit authority: 928
- hospital / health authority (from the organisation's name / web domain): 762
- university / college (from the organisation's name / web domain): 547
- utility / public corporation (from the organisation's name / web domain): 486
- government ministry / agency (from the organisation's name / web domain): 441
- religious organisation (from the organisation's name / web domain): 329
- First Nation / Indigenous government: 277
- transport / transit authority (from the organisation's name / web domain): 274
- First Nation / Indigenous government (from the organisation's name / web domain): 208
- school board / school district: 195
- school board / school district (from the organisation's name / web domain): 32
- library (from the organisation's name / web domain): 32
- US government body (federal, state or local): 31
- US city / county / local government: 11

## DMARC posture of the delivered mailboxes
- no DMARC record: 105607
- v=DMARC1; p=none (monitor only, no enforcement): 101626
- p=quarantine: 35447
- p=reject: 17182
- invalid DMARC record: 190
- DNS lookup failed: 89
