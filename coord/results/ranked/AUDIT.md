# Deep audit — 275700 delivered rows in 18 packages (130 files), 2026-11-12

Result: **FAIL** — 11 hard checks, 17 soft checks; hard failures: 1. Every flagged row is listed in `audit_flags.csv` with its reasons.

| # | check | kind | rows flagged | verdict |
|---|---|---|---|---|
| 1 | header: identical columns in every file (106 since 2026-11-06) | hard | 1 | FAIL |
| 2 | mailbox syntax | hard | 0 | PASS |
| 3 | mailbox referee-confirmed (all but P11) | hard | 0 | PASS |
| 4 | mail server (MX or A) on the mailbox domain | hard | 0 | PASS |
| 4b | mail server not yet checked (row newer than the last DNS pass) | soft | 220749 | REVIEW |
| 5 | no webmail domain | hard | 0 | PASS |
| 6 | no person-like local part | hard | 0 | PASS |
| 7 | role word in the local part | soft | 22180 | REVIEW |
| 8 | receivables-looking local part graded invoicing/AP | soft | 70 | REVIEW |
| 9 | shared government domain: page or quote names the body | soft | 2 | REVIEW |
| 10 | regional token of a multinational on a differently-located body | soft | 0 | PASS |
| 11 | quote contains the address | hard | 0 | PASS |
| 11b | quote shows the label next to the address (referee saw the address on the page) | soft | 0 | PASS |
| 12 | evidence page on the organisation's domain (or its site) | soft | 12614 | REVIEW |
| 13 | email_type label matches grade | hard | 0 | PASS |
| 14 | DMARC / SPF / provider columns filled | soft | 0 | PASS |
| 15 | tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m) | soft | 0 | PASS |
| 16 | vendor named and Canada proof present | hard | 0 | PASS |
| 17 | Canada proof is a source field or the vendor's site (never a name) | soft | 0 | PASS |
| 18 | record link present for dated-record tiers | soft | 0 | PASS |
| 19 | buyer name is a name (not a domain or a page title) | soft | 27286 | REVIEW |
| 20 | legal name is not a fragment or a platform copyright | soft | 431 | REVIEW |
| 21 | one row per mailbox | hard | 0 | PASS |
| 22 | one row per organisation name (same name twice) | soft | 0 | PASS |
| 23 | one row per site domain (two rows, different mailboxes, same domain) | soft | 42 | REVIEW |
| 24 | no blank cell | hard | 0 | PASS |
| 25 | jurisdiction vs mailbox top-level domain | soft | 68 | REVIEW |
| 26 | currency filled when a value is filled | soft | 51 | REVIEW |

## Examples of flagged rows (first 12 per check)
- **1 header: identical columns in every file (106 since 2026-11-06)**
    - files | 2 distinct headers; widths [0, 253]
- **4b mail server not yet checked (row newer than the last DNS pass)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:2 Braemed Ltd. | braemed.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:6 Gold Terra Resource Corp. | goldterracorp.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:7 INTER PIPELINE (Corridor) INC. (re COR & | interpipeline.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:9 AltaSteel Inc. | altasteel.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:10 Martineau Coffrage inc. | martineaucoffrage.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:12 ATTIS LEBLANC | attis-leblanc.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:16 Cologix Canada inc. | cologix.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:18 Edmond Nolin Ltée | constructionenl.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:20 Daikin Applied Canada inc. | daikinapplied.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:21 Deblois réfrigération inc. | debloisrefrigeration.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:23 Construction D.M. Turcotte J.M. inc. | dmturcotte.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:24 Dyno Nobel Canada inc. | dynonobel.com
- **7 role word in the local part**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:3 Keyera Corp. | ap_inquiries@keyera.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:136 Taylor-Listug, Inc. | ap_group@taylorguitars.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:7 Scouts de Dieppe | paiement@scoutsdedieppe.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:32 cvqvintage.ca | paiements@cvqvintage.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:54 Clic-Informatique | paiements@clic-informatique.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:128 Cameco Corporation | ap_cameco@cameco.com
    - P01_GOLD_active_relationship_invoicing_AP_email:275 University of Saskatchewan | connectionpoint@usask.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:277 Miami-Dade County (business unit CU05010 | invsubp@miamidade.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:291 Town of Oakville | ap_inquiries@oakville.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:378 BELL TEXTRON INC | APBell@textron.com
    - P02_active_relationship_finance_accounting_email:6 Agriculture and Agri-Food Canada | directdeposit.depotdirect@canada.ca
    - P02_active_relationship_finance_accounting_email:9 Social Sciences and Humanities Research  | directdeposit-depotdirect@crsh-sshrc.gc.ca
- **8 receivables-looking local part graded invoicing/AP**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:65 Calgary Coin Gallery | payment@calgarycoin.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:206 Empress | payments@villageofempress.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:216 birchfumigators.ca | payment@birchfumigators.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:9 Lerners Lawyers | payments@lerners.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:29 Flashing Canines Agility Club | payments@flashingcanines.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:58 McNamee & Kilpatrick | payments@mcnameekilpatrick.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:70 Awninginabox.ca | payment@awninginabox.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:96 Nicol Insurance | payments@nicolinsurance.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:111 Texas Tech University | payment.strategies@ttu.edu
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:113 Whitefish River First Nation | payments@whitefishriver.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:185 PSM Law | payment@psmlaw.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:188 Facility Solutions Canada Limited | payments@facilitysolutionscanada.ca
- **9 shared government domain: page or quote names the body**
    - P01_GOLD_active_relationship_invoicing_AP_email:537 Tennessee Department of Transportation | pln.invoices@tn.gov ← https://www.tn.gov/tdot/long-range-planning-home/longrange-administration/longra
    - P07_client_listing_finance_or_purchasing_email:579 transportation.ky.gov | finance.crcgroup@ky.gov ← https://finance.ky.gov/eProcurement/Pages/doing-business-with-the-commonwealth.a
- **12 evidence page on the organisation's domain (or its site)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:12 ATTIS LEBLANC | payable@attis-leblanc.com on attis-leblanc.ca (site attis-leblanc.com)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:70 Oil City Drywall North | accounting@oilcitydrywall.ca on oilcitydrywallnorth.ca (site oilcitydrywall.ca)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:109 COCA-COLA LTD./ COCA-COLA LTEE | krinvoice@coca-cola.com on coca-colacompany.com (site coca-cola.com)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:198 TRATON SE | invoices.to@se.traton.com on supplier.scania.com (site traton.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:32 cvqvintage.ca | paiements@cvqvintage.ca on coursesvintagequebec.ca (site cvqvintage.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:35 Capital Regional District | accountspayable@crd.bc.ca on crd.ca (site crd.bc.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:37 regieincendiekam-ouest.ca | payables@regieincendiekam-ouest.ca on regieincendiekam-ouest.com (site regieincendiekam-ouest.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:85 ibiosolutions.com | payables@ibiosolutions.com on immunebiosolutions.com (site ibiosolutions.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:115 Intermedia | ap@intermedia.com on intermedia.ca (site go.intermedia.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:175 dabc.ca | ap@dabc.ca on disabilityalliancebc.org (site dabc.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:32 Natural Sciences and Engineering Researc | payables@nserc-crsng.gc.ca on nserc-crsng.canada.ca (site nserc-crsng.gc.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:45 Ville de Montréal | facture@montreal.ca on ville.montreal.qc.ca (site montreal.ca)
- **19 buyer name is a name (not a domain or a page title)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:216 birchfumigators.ca | birchfumigators.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:217 dfcdiesel.com | dfcdiesel.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:30 lpsg.ca | lpsg.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:32 cvqvintage.ca | cvqvintage.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:34 apsurveys.ca | apsurveys.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:37 regieincendiekam-ouest.ca | regieincendiekam-ouest.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:45 guardian.law | guardian.law
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:52 nrgqc.com | nrgqc.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:55 it-desgens.ca | it-desgens.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:70 Awninginabox.ca | Awninginabox.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:78 efifoodequip.com | efifoodequip.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:83 ep.com | ep.com
- **20 legal name is not a fragment or a platform copyright**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:2 Braemed Ltd. | Braemed Ltd. (Health Canada's Medical Devices Establishment Licence li
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:100 LIN-ZHI INTERNATIONAL, INC. | LIN-ZHI INTERNATIONAL, INC. (Health Canada's Medical Devices Active Li
    - P05_likely_active_awarded_12_36_months_any_email:60 Ameren Illinois Company | Ameren Corporation and/or its suppliers (the copyright line of https:/
    - P05_likely_active_awarded_12_36_months_any_email:209 LOVE WORTH FINDING MINISTRIES INC | LLC. 800-274-5683 2941 Kate Bond Rd, Memphis, TN 38133 CONNECT WITH LW
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part10_of_10:1377 SEIGLA MEDICAL, INC. | SEIGLA MEDICAL, INC. (Health Canada's Medical Devices Active Licence L
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part10_of_10:2121 GRANICUS, LLC | GRANICUS, LLC (the Canadian trademarks register (owner of record), ext
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part1_of_10:3 Centennial Optical Ltd. | Centennial Optical Ltd. (Health Canada's Medical Devices Establishment
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part1_of_10:139 MIM SOFTWARE INC. | MIM SOFTWARE INC. (Health Canada's Medical Devices Active Licence List
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part1_of_10:140 BIOCHROM LTD | BIOCHROM LTD (Health Canada's Medical Devices Active Licence Listing (
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part1_of_10:141 SEERS CO., LTD. | SEERS CO., LTD. (Health Canada's Medical Devices Active Licence Listin
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part1_of_10:470 Csp Medical | Csp Medical (Health Canada's Medical Devices Establishment Licence lis
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part1_of_10:471 Harding Medical Supplies, A Division Of  | Harding Medical Supplies, A Division Of Imp Group Limited (Health Cana
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
    - P13_inferred_relationship_no_record_own_email_part10_of_71:240 belledebrillet.org | ON / brillet.fr
    - P13_inferred_relationship_no_record_own_email_part14_of_71:753 Alenti | ON / alenti.fr
    - P13_inferred_relationship_no_record_own_email_part16_of_71:408 SurePay | ON / surepay.co.uk
    - P13_inferred_relationship_no_record_own_email_part17_of_71:268 Denso | ON / denso.co.nz
    - P13_inferred_relationship_no_record_own_email_part18_of_71:134 LA MAISON DES JEUNES DE PLESSISVILLE INC | QC / lycos.fr
    - P13_inferred_relationship_no_record_own_email_part18_of_71:987 The Redeemed Christian Church of God Lov | SK / loveassembly.co.uk
    - P13_inferred_relationship_no_record_own_email_part1_of_71:160 Miele | ON / miele.de
    - P13_inferred_relationship_no_record_own_email_part1_of_71:287 ONEJOON | QC / onejoon.de
    - P13_inferred_relationship_no_record_own_email_part1_of_71:1341 Mole Valley District Council | SK / molevalley.gov.uk
    - P13_inferred_relationship_no_record_own_email_part21_of_71:1917 OPAL | QC / opal.fr
    - P13_inferred_relationship_no_record_own_email_part23_of_71:1928 Charles Faram | ON / charlesfaram.co.uk
- **26 currency filled when a value is filled**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:71 RENTON SCHOOL DISTRICT #403 | 332345.13 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:446 Rectorado de la Universitat de València | 12698.25 (source field: PayableAmount)
    - P01_GOLD_active_relationship_invoicing_AP_email:458 BELLEVUE, CITY OF | 35488873.2 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:460 UNIVERSITY PLACE SCHOOL DISTRICT #83 | 685477.9 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:466 BELLEVUE SCHOOL DISTRICT #405 | 5395.88 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:469 SNOQUALMIE VALLEY SCHOOL DISTRICT #410 | 23980.42 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:471 SHORELINE SCHOOL DISTRICT #412 | 919904.69 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:472 MARYLAND STADIUM AUTHORITY | 251569.05 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:492 University of North Dakota | 145.850 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:495 North Dakota State University | 35.000 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:504 BRINKS DE COLOMBIA S.A. | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:562 BANCOLOMBIA S.A. | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)

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
- P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email: 250
- P01T_active_service_seen_on_buyer_site_invoicing_AP_email: 225
- P01_GOLD_active_relationship_invoicing_AP_email: 626
- P02_active_relationship_finance_accounting_email: 467
- P03_active_relationship_purchasing_email: 265
- P04_active_relationship_general_email: 3572
- P05_likely_active_awarded_12_36_months_any_email: 424
- P06M_member_or_regulated_payer_of_canadian_body_other_email: 22195
- P06T_active_service_seen_on_buyer_site_other_email: 59830
- P06_client_listing_invoicing_AP_email: 276
- P07_client_listing_finance_or_purchasing_email: 820
- P08_client_listing_general_email: 30285
- P09_older_contract_or_payment_any_email: 275
- P10R_ca_domain_registration_contract_own_email: 0
- P10_linked_from_vendor_site_any_email: 2126
- P11_any_relationship_email_not_yet_confirmed: 1807
- P12_weaker_relationship_within_5_years_own_email: 11
- P13_inferred_relationship_no_record_own_email: 152246

## Field fill across all delivered rows (value present, not `not_published`)
- buyer_website: 275700 (100.0%)
- vendor_address: 274149 (99.4%)
- vendor_website: 259441 (94.1%)
- buyer_address: 243054 (88.2%)
- vendor_legal_name: 237220 (86.0%)
- buyer_logo_url: 225634 (81.8%)
- vendor_phone: 221241 (80.2%)
- vendor_registry_id: 210661 (76.4%)
- vendor_logo_url: 207837 (75.4%)
- buyer_phone: 180035 (65.3%)
- buyer_legal_name_as_published: 134637 (48.8%)
- vendor_incorporation_date: 126068 (45.7%)
- contract_link: 123454 (44.8%)
- vendor_bn9: 121861 (44.2%)
- award_date: 96706 (35.1%)
- vendor_neq: 65579 (23.8%)
- vendor_emails: 59452 (21.6%)
- buyer_bn_as_published: 35036 (12.7%)
- end_date: 17364 (6.3%)
- contract_value: 8653 (3.1%)
- payment_terms_as_published: 4859 (1.8%)
- ap_phone: 3076 (1.1%)
- po_required_as_published: 2723 (1.0%)
- invoice_mailing_address: 2284 (0.8%)
- invoicing_requirements: 2261 (0.8%)
- invoice_portal_url: 2215 (0.8%)
- ap_contact_name_as_published: 1109 (0.4%)

## Canada-proof families
- source field: 165790; other: 109910

## Buyer types
- organisation (type not stated in the record): 137561
- company (private sector): 51070
- company (private sector) (from the organisation's name / web domain): 43448
- non-profit / association / cultural body: 15389
- government ministry / agency: 7157
- municipality / local government (from the organisation's name / web domain): 3668
- non-profit / association / cultural body (from the organisation's name / web domain): 3508
- hospital / health authority: 3080
- utility / public corporation: 2794
- municipality / local government: 1710
- university / college: 1505
- transport / transit authority: 995
- hospital / health authority (from the organisation's name / web domain): 804
- university / college (from the organisation's name / web domain): 566
- utility / public corporation (from the organisation's name / web domain): 524
- government ministry / agency (from the organisation's name / web domain): 476
- religious organisation (from the organisation's name / web domain): 350
- First Nation / Indigenous government: 290
- transport / transit authority (from the organisation's name / web domain): 287
- First Nation / Indigenous government (from the organisation's name / web domain): 215
- school board / school district: 197
- school board / school district (from the organisation's name / web domain): 33
- US government body (federal, state or local): 31
- library (from the organisation's name / web domain): 31
- US city / county / local government: 11

## DMARC posture of the delivered mailboxes
- no DMARC record: 112223
- v=DMARC1; p=none (monitor only, no enforcement): 107649
- p=quarantine: 37472
- p=reject: 18050
- invalid DMARC record: 212
- DNS lookup failed: 94
