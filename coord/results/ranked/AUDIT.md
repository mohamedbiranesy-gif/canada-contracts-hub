# Deep audit — 59716 delivered rows in 17 packages (25 files), 2026-11-07

Result: **FAIL** — 11 hard checks, 17 soft checks; hard failures: 1. Every flagged row is listed in `audit_flags.csv` with its reasons.

| # | check | kind | rows flagged | verdict |
|---|---|---|---|---|
| 1 | header: identical columns in every file (106 since 2026-11-06) | hard | 0 | PASS |
| 2 | mailbox syntax | hard | 0 | PASS |
| 3 | mailbox referee-confirmed (all but P11) | hard | 7 | FAIL |
| 4 | mail server (MX or A) on the mailbox domain | hard | 0 | PASS |
| 4b | mail server not yet checked (row newer than the last DNS pass) | soft | 25 | REVIEW |
| 5 | no webmail domain | hard | 0 | PASS |
| 6 | no person-like local part | hard | 0 | PASS |
| 7 | role word in the local part | soft | 3097 | REVIEW |
| 8 | receivables-looking local part graded invoicing/AP | soft | 35 | REVIEW |
| 9 | shared government domain: page or quote names the body | soft | 2 | REVIEW |
| 10 | regional token of a multinational on a differently-located body | soft | 0 | PASS |
| 11 | quote contains the address | hard | 0 | PASS |
| 11b | quote shows the label next to the address (referee saw the address on the page) | soft | 0 | PASS |
| 12 | evidence page on the organisation's domain (or its site) | soft | 3281 | REVIEW |
| 13 | email_type label matches grade | hard | 0 | PASS |
| 14 | DMARC / SPF / provider columns filled | soft | 24 | REVIEW |
| 15 | tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m) | soft | 4 | REVIEW |
| 16 | vendor named and Canada proof present | hard | 0 | PASS |
| 17 | Canada proof is a source field or the vendor's site (never a name) | soft | 0 | PASS |
| 18 | record link present for dated-record tiers | soft | 0 | PASS |
| 19 | buyer name is a name (not a domain or a page title) | soft | 25359 | REVIEW |
| 20 | legal name is not a fragment or a platform copyright | soft | 0 | PASS |
| 21 | one row per mailbox | hard | 0 | PASS |
| 22 | one row per organisation name (same name twice) | soft | 3 | REVIEW |
| 23 | one row per site domain (two rows, different mailboxes, same domain) | soft | 65 | REVIEW |
| 24 | no blank cell | hard | 0 | PASS |
| 25 | jurisdiction vs mailbox top-level domain | soft | 34 | REVIEW |
| 26 | currency filled when a value is filled | soft | 46 | REVIEW |

## Examples of flagged rows (first 12 per check)
- **3 mailbox referee-confirmed (all but P11)**
    - P01_GOLD_active_relationship_invoicing_AP_email:31 City of Ottawa | confirmed; mailbox no longer seen on the page when re-read 2026-11-06 (check before use)
    - P01_GOLD_active_relationship_invoicing_AP_email:56 Santé Québec – CHU de Québec – Universit | confirmed; mailbox no longer seen on the page when re-read 2026-11-06 (check before use)
    - P01_GOLD_active_relationship_invoicing_AP_email:82 La Municipalité de La Pêche | confirmed; mailbox no longer seen on the page when re-read 2026-11-06 (check before use)
    - P01_GOLD_active_relationship_invoicing_AP_email:89 École Polytechnique | confirmed; mailbox no longer seen on the page when re-read 2026-11-06 (check before use)
    - P01_GOLD_active_relationship_invoicing_AP_email:123 Clear Hills County | confirmed; mailbox no longer seen on the page when re-read 2026-11-06 (check before use)
    - P01_GOLD_active_relationship_invoicing_AP_email:245 City of Timmins | confirmed; mailbox no longer seen on the page when re-read 2026-11-06 (check before use)
    - P01_GOLD_active_relationship_invoicing_AP_email:511 ECOPETROL S A | confirmed; mailbox no longer seen on the page when re-read 2026-11-06 (check before use)
- **4b mail server not yet checked (row newer than the last DNS pass)**
    - P02_active_relationship_finance_accounting_email:270 Pennsylvania State University | psu.edu
    - P04_active_relationship_general_email:893 Institut National des Mines | inmq.gouv.qc.ca
    - P06T_active_service_seen_on_buyer_site_other_email:2124 The hatch | thehatchwines.com
    - P08_client_listing_general_email:507 scaleai.ca | scaleai.ca
    - P10_linked_from_vendor_site_any_email:361 papcom.qc.ca | papcom.qc.ca
    - P10_linked_from_vendor_site_any_email:846 goeastofedmonton.com | goeastofedmonton.com
    - P11_any_relationship_email_not_yet_confirmed:154 RAYTHEON COMPANY | raytheon.com
    - P13_inferred_relationship_no_record_own_email_part2_of_9:1736 Everest Services Ltd | everest.ca
    - P13_inferred_relationship_no_record_own_email_part2_of_9:2298 ALPHACO | alphaco.ca
    - P13_inferred_relationship_no_record_own_email_part2_of_9:2645 MULTI COMBUSTION | multicombustion.com
    - P13_inferred_relationship_no_record_own_email_part2_of_9:3233 ORTHODONTIE FACE & PROFIL INC. | faceprofil.ca
    - P13_inferred_relationship_no_record_own_email_part2_of_9:3336 SERVICE RÉGIONAL D'INTERPRÉTARIAT DE L'E | srieq.ca
- **7 role word in the local part**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:16 Cameco Corporation | ap_cameco@cameco.com
    - P01_GOLD_active_relationship_invoicing_AP_email:252 Town of Oakville | ap_inquiries@oakville.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:270 Miami-Dade County (business unit CU05010 | invsubp@miamidade.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:367 BELL TEXTRON INC | APBell@textron.com
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
    - P01_GOLD_active_relationship_invoicing_AP_email:453 Township of Georgian Bay | payments@gbtownship.ca
    - P05_likely_active_awarded_12_36_months_any_email:25 Martensville | payments@martensville.ca
    - P06_client_listing_invoicing_AP_email:25 University of Bath | payments@bath.ac.uk
    - P06_client_listing_invoicing_AP_email:65 teamviewer.com | payments@teamviewer.com
    - P06_client_listing_invoicing_AP_email:136 blomidonnurseries.com | payments@blomidonnurseries.com
    - P10_linked_from_vendor_site_any_email:12 gov.scot | online_payments@gov.scot
    - P10_linked_from_vendor_site_any_email:29 WeirFoulds LLP | payments@weirfoulds.com
    - P10_linked_from_vendor_site_any_email:36 bcica.org | payments@bcica.org
    - P13_inferred_relationship_no_record_own_email_part1_of_9:10 THE ROYAL CANADIAN COLLEGE OF ORGANISTS- | payment@rcco-ottawa.ca
- **9 shared government domain: page or quote names the body**
    - P01_GOLD_active_relationship_invoicing_AP_email:41 Canadian Space Agency | invoicing.csa-asc.facturation@canada.ca ← https://www.canada.ca/en/public-services-procurement/services/payments-to-from-g
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
    - P01_GOLD_active_relationship_invoicing_AP_email:158 Department of Foreign Affairs and Trade | dfat.e-invoicing.prod@dfat.gov.au on directory.peppol.eu (site dfat.gov.au)
    - P01_GOLD_active_relationship_invoicing_AP_email:185 HM Land Registry | apinvoices@landregistry.gov.uk on assets.publishing.service.gov.uk (site gov.uk)
    - P01_GOLD_active_relationship_invoicing_AP_email:191 Texas Tech University Health Sciences Ce | accountspayableelp@ttuhsc.edu on ttuhscep.edu (site elpaso.ttuhsc.edu)
- **14 DMARC / SPF / provider columns filled**
    - P02_active_relationship_finance_accounting_email:270 Pennsylvania State University | not checked yet | not checked yet | not checked
    - P04_active_relationship_general_email:893 Institut National des Mines | not checked yet | not checked yet | not checked
    - P06T_active_service_seen_on_buyer_site_other_email:2124 The hatch | not checked yet | not checked yet | not checked
    - P08_client_listing_general_email:507 scaleai.ca | not checked yet | not checked yet | not checked
    - P10_linked_from_vendor_site_any_email:361 papcom.qc.ca | not checked yet | not checked yet | not checked
    - P10_linked_from_vendor_site_any_email:846 goeastofedmonton.com | not checked yet | not checked yet | not checked
    - P11_any_relationship_email_not_yet_confirmed:154 RAYTHEON COMPANY | not checked yet | not checked yet | not checked
    - P13_inferred_relationship_no_record_own_email_part2_of_9:2298 ALPHACO | not checked yet | not checked yet | not checked
    - P13_inferred_relationship_no_record_own_email_part2_of_9:2645 MULTI COMBUSTION | not checked yet | not checked yet | not checked
    - P13_inferred_relationship_no_record_own_email_part2_of_9:3233 ORTHODONTIE FACE & PROFIL INC. | not checked yet | not checked yet | not checked
    - P13_inferred_relationship_no_record_own_email_part2_of_9:3336 SERVICE RÉGIONAL D'INTERPRÉTARIAT DE L'E | not checked yet | not checked yet | not checked
    - P13_inferred_relationship_no_record_own_email_part2_of_9:3630 AtmODC inc. | not checked yet | not checked yet | not checked
- **15 tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m)**
    - P01_GOLD_active_relationship_invoicing_AP_email:137 Commission scolaire New Frontiers | A with end 2026-11-06
    - P02_active_relationship_finance_accounting_email:40 Cégep Édouard-Montpetit | A with end 2026-11-06
    - P02_active_relationship_finance_accounting_email:127 Municipalité de Rivière-Ouelle | A with end 2026-11-06
    - P04_active_relationship_general_email:111 Municipalité de Brébeuf | A with end 2026-11-06
- **19 buyer name is a name (not a domain or a page title)**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:13 uwindsor.ca | uwindsor.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:28 thebigcarrot.ca | thebigcarrot.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:33 ovs.com | ovs.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:79 hacc.edu | hacc.edu
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:91 cognizant.com | cognizant.com
    - P01_GOLD_active_relationship_invoicing_AP_email:419 capreit.ca | capreit.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:458 gov.edmonton.ab.ca | gov.edmonton.ab.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:504 bcib.ca | bcib.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:520 toronto.ca | toronto.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:546 slrd.bc.ca | slrd.bc.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:561 corporate.exxonmobil.com | corporate.exxonmobil.com
    - P02_active_relationship_finance_accounting_email:265 saddlehills.ab.ca | saddlehills.ab.ca
- **22 one row per organisation name (same name twice)**
    - P03_active_relationship_purchasing_email:222 Westbank First Nation | 2 rows, same mail domain: wfn.ca
    - P04_active_relationship_general_email:321 Cégep de Victoriaville. | 2 rows, same mail domain: cegepvicto.ca
    - P05_likely_active_awarded_12_36_months_any_email:5 Brandon University | 2 rows, same mail domain: brandonu.ca
- **23 one row per site domain (two rows, different mailboxes, same domain)**
    - P01_GOLD_active_relationship_invoicing_AP_email:25 University of Toronto | utoronto.ca: 2 rows, ap.fsd@utoronto.ca; fmdinvoice.utsc@utoronto.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:55 Ville de Gatineau | gatineau.ca: 2 rows, gatineau.factures@gatineau.ca; idgatineau@gatineau.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:64 Ville de Montréal | montreal.ca: 2 rows, facture@montreal.ca; comptesapayer@montreal.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:79 Ville de Laval | laval.ca: 3 rows, comptespayables@laval.ca; lavaleconomique@laval.ca; info@laval.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:88 Ville de Blainville | blainville.ca: 2 rows, approvisionnements@blainville.ca; finances@blainville.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:110 Texas Department of Insurance | texas.gov: 7 rows, invoices@tdi.texas.gov; ap@tsl.texas.gov; accounts.payable@tpwd.texas.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:124 University of Ottawa | uottawa.ca: 2 rows, payables@uottawa.ca; info@emba.uottawa.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:188 Oregon Department of Transportation | oregon.gov: 3 rows, opoinvoiceinquiries@odot.oregon.gov; omdaccounts.payable@omd.oregon.gov; odf.accountspayable@oregon.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:190 Texas Tech University Health Sciences Ce | ttuhsc.edu: 2 rows, Accounts.Payable@ttuhsc.edu; accountspayableelp@ttuhsc.edu
    - P01_GOLD_active_relationship_invoicing_AP_email:221 Metrolinx | metrolinx.com: 2 rows, it.invoices@metrolinx.com; rti.invoices@metrolinx.com
    - P01_GOLD_active_relationship_invoicing_AP_email:329 Virginia State Police | virginia.gov: 5 rows, ap@vsp.virginia.gov; accountspayable@energy.virginia.gov; support@dhrm.virginia.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:363 DELOITTE & TOUCHE LLP | deloitte.com: 2 rows, accountspayable@deloitte.be; financeservices@deloitte.com
- **25 jurisdiction vs mailbox top-level domain**
    - P13_inferred_relationship_no_record_own_email_part1_of_9:482 Rheinmetall AG | CA / rheinmetall.com.au
    - P13_inferred_relationship_no_record_own_email_part1_of_9:494 Westpac | CA / westpac.com.au
    - P13_inferred_relationship_no_record_own_email_part1_of_9:533 United States Postal Service | CA / usps.gov
    - P13_inferred_relationship_no_record_own_email_part1_of_9:1332 Randstad Deutschland | CA / randstad.de
    - P13_inferred_relationship_no_record_own_email_part1_of_9:2684 LA MAISON DES JEUNES DE PLESSISVILLE INC | QC / lycos.fr
    - P13_inferred_relationship_no_record_own_email_part1_of_9:3259 The Redeemed Christian Church of God Lov | SK / loveassembly.co.uk
    - P13_inferred_relationship_no_record_own_email_part2_of_9:2373 Trotec Laser Canada | QC / troteclaser.com.au
    - P13_inferred_relationship_no_record_own_email_part3_of_9:1449 KNDS | CA / knds.de
    - P13_inferred_relationship_no_record_own_email_part3_of_9:1467 The Warehouse Group | CA / thewarehousegroup.co.nz
    - P13_inferred_relationship_no_record_own_email_part4_of_9:2097 akelius.ca | CA / akelius.fr
    - P13_inferred_relationship_no_record_own_email_part4_of_9:2490 apexauctions.ca | CA / apexauctions.co.uk
    - P13_inferred_relationship_no_record_own_email_part5_of_9:984 custompens.ca | CA / custompens.com.au
- **26 currency filled when a value is filled**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:22 RENTON SCHOOL DISTRICT #403 | 332345.13 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:413 Rectorado de la Universitat de València | 12698.25 (source field: PayableAmount)
    - P01_GOLD_active_relationship_invoicing_AP_email:423 BRINKS DE COLOMBIA S.A. | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:441 University of North Dakota | 145.850 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:462 BELLEVUE, CITY OF | 35488873.2 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:470 UNIVERSITY PLACE SCHOOL DISTRICT #83 | 685477.9 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:486 North Dakota State University | 35.000 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:491 BELLEVUE SCHOOL DISTRICT #405 | 5395.88 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:499 MARYLAND STADIUM AUTHORITY | 251569.05 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:511 ECOPETROL S A | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:538 Fundación para la Investigación del Hosp | 1236.23 (source field: PayableAmount)
    - P02_active_relationship_finance_accounting_email:312 CLARK COUNTY | 499992.43 (source field: amount)

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
- P01T_active_service_seen_on_buyer_site_invoicing_AP_email: 90
- P01_GOLD_active_relationship_invoicing_AP_email: 561
- P02_active_relationship_finance_accounting_email: 355
- P03_active_relationship_purchasing_email: 221
- P04_active_relationship_general_email: 1569
- P05_likely_active_awarded_12_36_months_any_email: 368
- P06M_member_or_regulated_payer_of_canadian_body_other_email: 164
- P06T_active_service_seen_on_buyer_site_other_email: 2364
- P06_client_listing_invoicing_AP_email: 153
- P07_client_listing_finance_or_purchasing_email: 236
- P08_client_listing_general_email: 2987
- P09_older_contract_or_payment_any_email: 355
- P10_linked_from_vendor_site_any_email: 2535
- P11_any_relationship_email_not_yet_confirmed: 789
- P12_weaker_relationship_within_5_years_own_email: 19
- P13_inferred_relationship_no_record_own_email: 46932

## Field fill across all delivered rows (value present, not `not_published`)
- buyer_website: 59716 (100.0%)
- vendor_address: 56560 (94.7%)
- vendor_website: 55138 (92.3%)
- buyer_logo_url: 44113 (73.9%)
- buyer_address: 40545 (67.9%)
- ap_phone: 34500 (57.8%)
- buyer_phone: 31141 (52.1%)
- vendor_phone: 18109 (30.3%)
- invoice_mailing_address: 13910 (23.3%)
- contract_link: 12784 (21.4%)
- buyer_legal_name_as_published: 8694 (14.6%)
- vendor_logo_url: 6819 (11.4%)
- vendor_legal_name: 6478 (10.8%)
- award_date: 6471 (10.8%)
- vendor_registry_id: 5265 (8.8%)
- vendor_emails: 4281 (7.2%)
- vendor_bn9: 2467 (4.1%)
- contract_value: 2280 (3.8%)
- vendor_incorporation_date: 2070 (3.5%)
- buyer_bn_as_published: 1854 (3.1%)
- end_date: 1646 (2.8%)
- invoicing_requirements: 1579 (2.6%)
- invoice_portal_url: 635 (1.1%)
- po_required_as_published: 449 (0.8%)
- payment_terms_as_published: 335 (0.6%)
- ap_contact_name_as_published: 172 (0.3%)
- vendor_neq: 23 (0.0%)

## Canada-proof families
- other: 43539; source field: 16177

## Buyer types
- organisation (type not stated in the record): 35408
- company (private sector): 9138
- non-profit / association / cultural body: 6425
- company (private sector) (from the organisation's name / web domain): 1504
- municipality / local government: 1124
- government ministry / agency: 1042
- non-profit / association / cultural body (from the organisation's name / web domain): 867
- municipality / local government (from the organisation's name / web domain): 817
- hospital / health authority: 752
- university / college: 455
- utility / public corporation: 433
- hospital / health authority (from the organisation's name / web domain): 363
- university / college (from the organisation's name / web domain): 312
- transport / transit authority: 182
- school board / school district: 170
- First Nation / Indigenous government: 156
- government ministry / agency (from the organisation's name / web domain): 150
- religious organisation (from the organisation's name / web domain): 137
- utility / public corporation (from the organisation's name / web domain): 105
- transport / transit authority (from the organisation's name / web domain): 67
- First Nation / Indigenous government (from the organisation's name / web domain): 40
- US government body (federal, state or local): 29
- library (from the organisation's name / web domain): 20
- US city / county / local government: 11
- school board / school district (from the organisation's name / web domain): 9

## DMARC posture of the delivered mailboxes
- v=DMARC1; p=none (monitor only, no enforcement): 24342
- no DMARC record: 20057
- p=quarantine: 10031
- p=reject: 5197
- invalid DMARC record: 57
- not checked yet: 24
- DNS lookup failed: 8
