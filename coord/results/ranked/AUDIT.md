# Deep audit — 59751 delivered rows in 17 packages (25 files), 2026-11-08

Result: **PASS** — 11 hard checks, 17 soft checks; hard failures: 0. Every flagged row is listed in `audit_flags.csv` with its reasons.

| # | check | kind | rows flagged | verdict |
|---|---|---|---|---|
| 1 | header: identical columns in every file (106 since 2026-11-06) | hard | 0 | PASS |
| 2 | mailbox syntax | hard | 0 | PASS |
| 3 | mailbox referee-confirmed (all but P11) | hard | 0 | PASS |
| 4 | mail server (MX or A) on the mailbox domain | hard | 0 | PASS |
| 4b | mail server not yet checked (row newer than the last DNS pass) | soft | 1 | REVIEW |
| 5 | no webmail domain | hard | 0 | PASS |
| 6 | no person-like local part | hard | 0 | PASS |
| 7 | role word in the local part | soft | 3100 | REVIEW |
| 8 | receivables-looking local part graded invoicing/AP | soft | 35 | REVIEW |
| 9 | shared government domain: page or quote names the body | soft | 3 | REVIEW |
| 10 | regional token of a multinational on a differently-located body | soft | 0 | PASS |
| 11 | quote contains the address | hard | 0 | PASS |
| 11b | quote shows the label next to the address (referee saw the address on the page) | soft | 0 | PASS |
| 12 | evidence page on the organisation's domain (or its site) | soft | 3281 | REVIEW |
| 13 | email_type label matches grade | hard | 0 | PASS |
| 14 | DMARC / SPF / provider columns filled | soft | 0 | PASS |
| 15 | tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m) | soft | 6 | REVIEW |
| 16 | vendor named and Canada proof present | hard | 0 | PASS |
| 17 | Canada proof is a source field or the vendor's site (never a name) | soft | 0 | PASS |
| 18 | record link present for dated-record tiers | soft | 0 | PASS |
| 19 | buyer name is a name (not a domain or a page title) | soft | 25374 | REVIEW |
| 20 | legal name is not a fragment or a platform copyright | soft | 0 | PASS |
| 21 | one row per mailbox | hard | 0 | PASS |
| 22 | one row per organisation name (same name twice) | soft | 3 | REVIEW |
| 23 | one row per site domain (two rows, different mailboxes, same domain) | soft | 65 | REVIEW |
| 24 | no blank cell | hard | 0 | PASS |
| 25 | jurisdiction vs mailbox top-level domain | soft | 34 | REVIEW |
| 26 | currency filled when a value is filled | soft | 46 | REVIEW |

## Examples of flagged rows (first 12 per check)
- **4b mail server not yet checked (row newer than the last DNS pass)**
    - P13_inferred_relationship_no_record_own_email_part2_of_9:1736 Everest Services Ltd | everest.ca
- **7 role word in the local part**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:16 Cameco Corporation | ap_cameco@cameco.com
    - P01_GOLD_active_relationship_invoicing_AP_email:253 Town of Oakville | ap_inquiries@oakville.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:272 Miami-Dade County (business unit CU05010 | invsubp@miamidade.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:369 BELL TEXTRON INC | APBell@textron.com
    - P02_active_relationship_finance_accounting_email:7 Agriculture and Agri-Food Canada | directdeposit.depotdirect@canada.ca
    - P02_active_relationship_finance_accounting_email:13 Crown-Indigenous Relations and Northern  | depotdirect-directdeposit@sac-isc.gc.ca
    - P02_active_relationship_finance_accounting_email:14 Department of Justice Canada | mdv_dpf@justice.gc.ca
    - P02_active_relationship_finance_accounting_email:18 Health Canada | hc.direct.deposit.requests-demande.de.depot.direct.sc@canada.ca
    - P02_active_relationship_finance_accounting_email:19 Innovation, Science and Economic Develop | ifmscustomer-clientsifm@ised-isde.gc.ca
    - P02_active_relationship_finance_accounting_email:21 National Defence | ddenrol-inscriredd@forces.gc.ca
    - P02_active_relationship_finance_accounting_email:29 Social Sciences and Humanities Research  | directdeposit-depotdirect@crsh-sshrc.gc.ca
    - P02_active_relationship_finance_accounting_email:31 Veterans Affairs Canada | directdeposit-depotdirect@vac-acc.gc.ca
- **8 receivables-looking local part graded invoicing/AP**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:10 Empress | payments@villageofempress.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:4 Texas Tech University | payment.strategies@ttu.edu
    - P01_GOLD_active_relationship_invoicing_AP_email:37 Environment and Climate Change Canada | renseignement-paiements-payments-inquiry@ec.gc.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:456 Township of Georgian Bay | payments@gbtownship.ca
    - P05_likely_active_awarded_12_36_months_any_email:25 Martensville | payments@martensville.ca
    - P06_client_listing_invoicing_AP_email:26 University of Bath | payments@bath.ac.uk
    - P06_client_listing_invoicing_AP_email:67 teamviewer.com | payments@teamviewer.com
    - P06_client_listing_invoicing_AP_email:140 blomidonnurseries.com | payments@blomidonnurseries.com
    - P10_linked_from_vendor_site_any_email:12 gov.scot | online_payments@gov.scot
    - P10_linked_from_vendor_site_any_email:29 WeirFoulds LLP | payments@weirfoulds.com
    - P10_linked_from_vendor_site_any_email:36 bcica.org | payments@bcica.org
    - P13_inferred_relationship_no_record_own_email_part1_of_9:10 THE ROYAL CANADIAN COLLEGE OF ORGANISTS- | payment@rcco-ottawa.ca
- **9 shared government domain: page or quote names the body**
    - P01_GOLD_active_relationship_invoicing_AP_email:41 Canadian Space Agency | invoicing.csa-asc.facturation@canada.ca ← https://www.canada.ca/en/public-services-procurement/services/payments-to-from-g
    - P03_active_relationship_purchasing_email:200 Tennessee Department of Transportation | supplier.maintenance@tn.gov ← https://www.tn.gov/generalservices/procurement/central-procurement-office--cpo-/
    - P13_inferred_relationship_no_record_own_email_part1_of_9:529 Landlord and Tenant Board | ltbpayments@ontario.ca ← https://tribunalsontario.ca/ltb/contact/
- **12 evidence page on the organisation's domain (or its site)**
    - P01_GOLD_active_relationship_invoicing_AP_email:2 Department of Defence | peppol.einvoices@defence.gov.au on directory.peppol.eu (site defence.gov.au)
    - P01_GOLD_active_relationship_invoicing_AP_email:3 Department of Industry, Science and Reso | einvoicingqueries@industry.gov.au on directory.peppol.eu (site industry.gov.au)
    - P01_GOLD_active_relationship_invoicing_AP_email:49 Natural Sciences and Engineering Researc | payables@nserc-crsng.gc.ca on nserc-crsng.canada.ca (site nserc-crsng.gc.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:64 Ville de Montréal | facture@montreal.ca on ville.montreal.qc.ca (site montreal.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:109 UK Atomic Energy Authority | finance@uk-atomic-energy.org.uk on assets.publishing.service.gov.uk (site gov.uk)
    - P01_GOLD_active_relationship_invoicing_AP_email:122 City of Chestermere | city.ap@chestermere.ca on thecityofchestermere.ca (site chestermere.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:128 Newfoundland and Labrador Liquor Corpora | Accounts.Payable@nlliquor.com on nlliquorcorp.com (site nlliquor.com)
    - P01_GOLD_active_relationship_invoicing_AP_email:130 The Ottawa Hospital | tohaccountspayable@toh.ca on ottawahospital.on.ca (site toh.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:153 UK Research and Innovation | finance@uksbs.co.uk on ukri.org (site uksbs.co.uk)
    - P01_GOLD_active_relationship_invoicing_AP_email:159 Department of Foreign Affairs and Trade | dfat.e-invoicing.prod@dfat.gov.au on directory.peppol.eu (site dfat.gov.au)
    - P01_GOLD_active_relationship_invoicing_AP_email:186 HM Land Registry | apinvoices@landregistry.gov.uk on assets.publishing.service.gov.uk (site gov.uk)
    - P01_GOLD_active_relationship_invoicing_AP_email:192 Texas Tech University Health Sciences Ce | accountspayableelp@ttuhsc.edu on ttuhscep.edu (site elpaso.ttuhsc.edu)
- **15 tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m)**
    - P01_GOLD_active_relationship_invoicing_AP_email:137 Commission scolaire New Frontiers | A with end 2026-11-06
    - P02_active_relationship_finance_accounting_email:40 Cégep Édouard-Montpetit | A with end 2026-11-06
    - P02_active_relationship_finance_accounting_email:132 Municipalité de Rivière-Ouelle | A with end 2026-11-06
    - P02_active_relationship_finance_accounting_email:185 Municipalité de Ripon | A with end 2026-11-07
    - P04_active_relationship_general_email:112 Municipalité de Brébeuf | A with end 2026-11-06
    - P11_any_relationship_email_not_yet_confirmed:13 Municipalité de Saint-Apollinaire | A with end 2026-11-07
- **19 buyer name is a name (not a domain or a page title)**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:13 uwindsor.ca | uwindsor.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:28 thebigcarrot.ca | thebigcarrot.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:33 ovs.com | ovs.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:79 hacc.edu | hacc.edu
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:92 cognizant.com | cognizant.com
    - P01_GOLD_active_relationship_invoicing_AP_email:421 capreit.ca | capreit.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:461 gov.edmonton.ab.ca | gov.edmonton.ab.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:508 bcib.ca | bcib.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:524 toronto.ca | toronto.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:550 slrd.bc.ca | slrd.bc.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:565 corporate.exxonmobil.com | corporate.exxonmobil.com
    - P02_active_relationship_finance_accounting_email:278 saddlehills.ab.ca | saddlehills.ab.ca
- **22 one row per organisation name (same name twice)**
    - P03_active_relationship_purchasing_email:228 Westbank First Nation | 2 rows, same mail domain: wfn.ca
    - P04_active_relationship_general_email:325 Cégep de Victoriaville. | 2 rows, same mail domain: cegepvicto.ca
    - P05_likely_active_awarded_12_36_months_any_email:5 Brandon University | 2 rows, same mail domain: brandonu.ca
- **23 one row per site domain (two rows, different mailboxes, same domain)**
    - P01_GOLD_active_relationship_invoicing_AP_email:25 University of Toronto | utoronto.ca: 2 rows, ap.fsd@utoronto.ca; fmdinvoice.utsc@utoronto.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:55 Ville de Gatineau | gatineau.ca: 2 rows, gatineau.factures@gatineau.ca; idgatineau@gatineau.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:64 Ville de Montréal | montreal.ca: 2 rows, facture@montreal.ca; comptesapayer@montreal.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:79 Ville de Laval | laval.ca: 3 rows, comptespayables@laval.ca; lavaleconomique@laval.ca; info@laval.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:88 Ville de Blainville | blainville.ca: 2 rows, approvisionnements@blainville.ca; finances@blainville.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:110 Texas Department of Insurance | texas.gov: 7 rows, invoices@tdi.texas.gov; ap@tsl.texas.gov; accounts.payable@tpwd.texas.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:124 University of Ottawa | uottawa.ca: 2 rows, payables@uottawa.ca; info@emba.uottawa.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:189 Oregon Department of Transportation | oregon.gov: 3 rows, opoinvoiceinquiries@odot.oregon.gov; omdaccounts.payable@omd.oregon.gov; odf.accountspayable@oregon.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:191 Texas Tech University Health Sciences Ce | ttuhsc.edu: 2 rows, Accounts.Payable@ttuhsc.edu; accountspayableelp@ttuhsc.edu
    - P01_GOLD_active_relationship_invoicing_AP_email:222 Metrolinx | metrolinx.com: 2 rows, it.invoices@metrolinx.com; rti.invoices@metrolinx.com
    - P01_GOLD_active_relationship_invoicing_AP_email:331 Virginia State Police | virginia.gov: 5 rows, ap@vsp.virginia.gov; accountspayable@energy.virginia.gov; support@dhrm.virginia.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:365 DELOITTE & TOUCHE LLP | deloitte.com: 2 rows, accountspayable@deloitte.be; financeservices@deloitte.com
- **25 jurisdiction vs mailbox top-level domain**
    - P13_inferred_relationship_no_record_own_email_part1_of_9:482 Rheinmetall AG | CA / rheinmetall.com.au
    - P13_inferred_relationship_no_record_own_email_part1_of_9:494 Westpac | CA / westpac.com.au
    - P13_inferred_relationship_no_record_own_email_part1_of_9:533 United States Postal Service | CA / usps.gov
    - P13_inferred_relationship_no_record_own_email_part1_of_9:1333 Randstad Deutschland | CA / randstad.de
    - P13_inferred_relationship_no_record_own_email_part1_of_9:2685 LA MAISON DES JEUNES DE PLESSISVILLE INC | QC / lycos.fr
    - P13_inferred_relationship_no_record_own_email_part1_of_9:3261 The Redeemed Christian Church of God Lov | SK / loveassembly.co.uk
    - P13_inferred_relationship_no_record_own_email_part2_of_9:2373 Trotec Laser Canada | QC / troteclaser.com.au
    - P13_inferred_relationship_no_record_own_email_part3_of_9:1450 KNDS | CA / knds.de
    - P13_inferred_relationship_no_record_own_email_part3_of_9:1468 The Warehouse Group | CA / thewarehousegroup.co.nz
    - P13_inferred_relationship_no_record_own_email_part4_of_9:2098 akelius.ca | CA / akelius.fr
    - P13_inferred_relationship_no_record_own_email_part4_of_9:2492 apexauctions.ca | CA / apexauctions.co.uk
    - P13_inferred_relationship_no_record_own_email_part5_of_9:986 custompens.ca | CA / custompens.com.au
- **26 currency filled when a value is filled**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:22 RENTON SCHOOL DISTRICT #403 | 332345.13 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:415 Rectorado de la Universitat de València | 12698.25 (source field: PayableAmount)
    - P01_GOLD_active_relationship_invoicing_AP_email:425 BRINKS DE COLOMBIA S.A. | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:443 University of North Dakota | 145.850 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:465 BELLEVUE, CITY OF | 35488873.2 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:473 UNIVERSITY PLACE SCHOOL DISTRICT #83 | 685477.9 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:489 North Dakota State University | 35.000 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:494 BELLEVUE SCHOOL DISTRICT #405 | 5395.88 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:502 MARYLAND STADIUM AUTHORITY | 251569.05 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:515 ECOPETROL S A | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:542 Fundación para la Investigación del Hosp | 1236.23 (source field: PayableAmount)
    - P02_active_relationship_finance_accounting_email:325 CLARK COUNTY | 499992.43 (source field: amount)

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
- P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email: 18
- P01T_active_service_seen_on_buyer_site_invoicing_AP_email: 91
- P01_GOLD_active_relationship_invoicing_AP_email: 565
- P02_active_relationship_finance_accounting_email: 368
- P03_active_relationship_purchasing_email: 227
- P04_active_relationship_general_email: 1586
- P05_likely_active_awarded_12_36_months_any_email: 371
- P06M_member_or_regulated_payer_of_canadian_body_other_email: 167
- P06T_active_service_seen_on_buyer_site_other_email: 2393
- P06_client_listing_invoicing_AP_email: 157
- P07_client_listing_finance_or_purchasing_email: 243
- P08_client_listing_general_email: 3016
- P09_older_contract_or_payment_any_email: 359
- P10_linked_from_vendor_site_any_email: 2572
- P11_any_relationship_email_not_yet_confirmed: 636
- P12_weaker_relationship_within_5_years_own_email: 21
- P13_inferred_relationship_no_record_own_email: 46961

## Field fill across all delivered rows (value present, not `not_published`)
- buyer_website: 59751 (100.0%)
- vendor_address: 56593 (94.7%)
- vendor_website: 55167 (92.3%)
- buyer_phone: 44291 (74.1%)
- buyer_logo_url: 44135 (73.9%)
- buyer_address: 42840 (71.7%)
- vendor_phone: 18116 (30.3%)
- contract_link: 12790 (21.4%)
- buyer_legal_name_as_published: 8699 (14.6%)
- vendor_logo_url: 6818 (11.4%)
- vendor_legal_name: 6481 (10.8%)
- award_date: 6478 (10.8%)
- vendor_registry_id: 5268 (8.8%)
- vendor_emails: 4281 (7.2%)
- ap_phone: 2583 (4.3%)
- vendor_bn9: 2470 (4.1%)
- contract_value: 2284 (3.8%)
- invoice_mailing_address: 2096 (3.5%)
- vendor_incorporation_date: 2071 (3.5%)
- buyer_bn_as_published: 1856 (3.1%)
- end_date: 1647 (2.8%)
- invoicing_requirements: 1580 (2.6%)
- invoice_portal_url: 638 (1.1%)
- po_required_as_published: 447 (0.7%)
- payment_terms_as_published: 335 (0.6%)
- ap_contact_name_as_published: 172 (0.3%)
- vendor_neq: 23 (0.0%)

## Canada-proof families
- other: 43570; source field: 16181

## Buyer types
- organisation (type not stated in the record): 35427
- company (private sector): 9143
- non-profit / association / cultural body: 6430
- company (private sector) (from the organisation's name / web domain): 1504
- municipality / local government: 1128
- government ministry / agency: 1043
- non-profit / association / cultural body (from the organisation's name / web domain): 869
- municipality / local government (from the organisation's name / web domain): 817
- hospital / health authority: 752
- university / college: 454
- utility / public corporation: 434
- hospital / health authority (from the organisation's name / web domain): 363
- university / college (from the organisation's name / web domain): 313
- transport / transit authority: 182
- school board / school district: 170
- First Nation / Indigenous government: 156
- government ministry / agency (from the organisation's name / web domain): 149
- religious organisation (from the organisation's name / web domain): 136
- utility / public corporation (from the organisation's name / web domain): 105
- transport / transit authority (from the organisation's name / web domain): 67
- First Nation / Indigenous government (from the organisation's name / web domain): 40
- US government body (federal, state or local): 29
- library (from the organisation's name / web domain): 20
- US city / county / local government: 11
- school board / school district (from the organisation's name / web domain): 9

## DMARC posture of the delivered mailboxes
- v=DMARC1; p=none (monitor only, no enforcement): 24367
- no DMARC record: 20071
- p=quarantine: 10046
- p=reject: 5204
- invalid DMARC record: 57
- DNS lookup failed: 6
