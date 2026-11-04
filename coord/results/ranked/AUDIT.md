# Deep audit — 55914 delivered rows in 17 packages (21 files), 2026-11-04

Result: **FAIL** — 11 hard checks, 16 soft checks; hard failures: 1. Every flagged row is listed in `audit_flags.csv` with its reasons.

| # | check | kind | rows flagged | verdict |
|---|---|---|---|---|
| 1 | header: 92 identical columns in every file | hard | 0 | PASS |
| 2 | mailbox syntax | hard | 0 | PASS |
| 3 | mailbox referee-confirmed (all but P11) | hard | 0 | PASS |
| 4 | mail server (MX or A) on the mailbox domain | hard | 0 | PASS |
| 4b | mail server not yet checked (row newer than the last DNS pass) | soft | 3641 | REVIEW |
| 5 | no webmail domain | hard | 0 | PASS |
| 6 | no person-like local part | hard | 0 | PASS |
| 7 | role word in the local part | soft | 2974 | REVIEW |
| 8 | receivables-looking local part graded invoicing/AP | soft | 32 | REVIEW |
| 9 | shared government domain: page or quote names the body | soft | 2 | REVIEW |
| 10 | regional token of a multinational on a differently-located body | soft | 0 | PASS |
| 11 | quote contains the address | hard | 1 | FAIL |
| 12 | evidence page on the organisation's domain (or its site) | soft | 3360 | REVIEW |
| 13 | email_type label matches grade | hard | 0 | PASS |
| 14 | DMARC / SPF / provider columns filled | soft | 3639 | REVIEW |
| 15 | tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m) | soft | 0 | PASS |
| 16 | vendor named and Canada proof present | hard | 0 | PASS |
| 17 | Canada proof is a source field or the vendor's site (never a name) | soft | 0 | PASS |
| 18 | record link present for dated-record tiers | soft | 0 | PASS |
| 19 | buyer name is a name (not a domain or a page title) | soft | 23335 | REVIEW |
| 20 | legal name is not a fragment or a platform copyright | soft | 0 | PASS |
| 21 | one row per mailbox | hard | 0 | PASS |
| 22 | one row per organisation name (same name twice) | soft | 3 | REVIEW |
| 23 | one row per site domain (two rows, different mailboxes, same domain) | soft | 66 | REVIEW |
| 24 | no blank cell | hard | 0 | PASS |
| 25 | jurisdiction vs mailbox top-level domain | soft | 38 | REVIEW |
| 26 | currency filled when a value is filled | soft | 46 | REVIEW |

## Examples of flagged rows (first 12 per check)
- **4b mail server not yet checked (row newer than the last DNS pass)**
    - P06M_member_or_regulated_payer_of_canadian_body_other_email:59 Selkirk College | selkirk.ca
    - P08_client_listing_general_email:1083 royallepage.ca | royallepage.ca
    - P08_client_listing_general_email:2451 Strike | strikegroup.ca
    - P10_linked_from_vendor_site_any_email:564 centris.ca | centris.ca
    - P13_inferred_relationship_no_record_own_email_part1_of_5:17 sun-nurses.sk.ca | sun-nurses.sk.ca
    - P13_inferred_relationship_no_record_own_email_part1_of_5:135 rdubz.ca | rdubz.ca
    - P13_inferred_relationship_no_record_own_email_part1_of_5:136 sapm.qc.ca | sapm.qc.ca
    - P13_inferred_relationship_no_record_own_email_part1_of_5:137 soccerlsl.qc.ca | soccerlsl.qc.ca
    - P13_inferred_relationship_no_record_own_email_part1_of_5:138 thegolfdome.ca | thegolfdome.ca
    - P13_inferred_relationship_no_record_own_email_part1_of_5:139 townofshellbrook.ca | townofshellbrook.ca
    - P13_inferred_relationship_no_record_own_email_part1_of_5:222 townofcoronach.ca | townofcoronach.ca
    - P13_inferred_relationship_no_record_own_email_part1_of_5:372 relianceproperties.ca | relianceproperties.ca
- **7 role word in the local part**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:16 Cameco Corporation | ap_cameco@cameco.com
    - P01_GOLD_active_relationship_invoicing_AP_email:263 Town of Oakville | ap_inquiries@oakville.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:282 Miami-Dade County (business unit CU05010 | invsubp@miamidade.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:377 BELL TEXTRON INC | APBell@textron.com
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
    - P01_GOLD_active_relationship_invoicing_AP_email:38 Environment and Climate Change Canada | renseignement-paiements-payments-inquiry@ec.gc.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:466 Township of Georgian Bay | payments@gbtownship.ca
    - P05_likely_active_awarded_12_36_months_any_email:26 Martensville | payments@martensville.ca
    - P06_client_listing_invoicing_AP_email:27 University of Bath | payments@bath.ac.uk
    - P06_client_listing_invoicing_AP_email:69 teamviewer.com | payments@teamviewer.com
    - P06_client_listing_invoicing_AP_email:143 blomidonnurseries.com | payments@blomidonnurseries.com
    - P10_linked_from_vendor_site_any_email:12 gov.scot | online_payments@gov.scot
    - P10_linked_from_vendor_site_any_email:29 WeirFoulds LLP | payments@weirfoulds.com
    - P10_linked_from_vendor_site_any_email:36 bcica.org | payments@bcica.org
    - P13_inferred_relationship_no_record_own_email_part1_of_5:10 THE ROYAL CANADIAN COLLEGE OF ORGANISTS- | payment@rcco-ottawa.ca
- **9 shared government domain: page or quote names the body**
    - P01_GOLD_active_relationship_invoicing_AP_email:42 Canadian Space Agency | invoicing.csa-asc.facturation@canada.ca ← https://www.canada.ca/en/public-services-procurement/services/payments-to-from-g
    - P13_inferred_relationship_no_record_own_email_part1_of_5:503 Landlord and Tenant Board | ltbpayments@ontario.ca ← https://tribunalsontario.ca/ltb/contact/
- **11 quote contains the address**
    - P02_active_relationship_finance_accounting_email:13 Crown-Indigenous Relations and Northern  | Crown-Indigenous Relations and Northern Affairs Canada Refer
- **12 evidence page on the organisation's domain (or its site)**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:18 Motorola Solutions, Inc | recepcionfacturas@motorolasolutions.com on web.archive.org (site motorolasolutions.com)
    - P01_GOLD_active_relationship_invoicing_AP_email:2 Department of Defence | peppol.einvoices@defence.gov.au on directory.peppol.eu (site defence.gov.au)
    - P01_GOLD_active_relationship_invoicing_AP_email:3 Department of Industry, Science and Reso | einvoicingqueries@industry.gov.au on directory.peppol.eu (site industry.gov.au)
    - P01_GOLD_active_relationship_invoicing_AP_email:50 Natural Sciences and Engineering Researc | payables@nserc-crsng.gc.ca on nserc-crsng.canada.ca (site nserc-crsng.gc.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:65 Ville de Montréal | facture@montreal.ca on ville.montreal.qc.ca (site montreal.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:95 Ville de Farnham | comptespayables@ville.farnham.qc.ca on web.archive.org (site ville.farnham.qc.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:113 UK Atomic Energy Authority | finance@uk-atomic-energy.org.uk on assets.publishing.service.gov.uk (site gov.uk)
    - P01_GOLD_active_relationship_invoicing_AP_email:126 City of Chestermere | city.ap@chestermere.ca on thecityofchestermere.ca (site chestermere.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:132 Newfoundland and Labrador Liquor Corpora | Accounts.Payable@nlliquor.com on nlliquorcorp.com (site nlliquor.com)
    - P01_GOLD_active_relationship_invoicing_AP_email:134 The Ottawa Hospital | tohaccountspayable@toh.ca on ottawahospital.on.ca (site toh.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:157 UK Research and Innovation | finance@uksbs.co.uk on ukri.org (site uksbs.co.uk)
    - P01_GOLD_active_relationship_invoicing_AP_email:163 Department of Foreign Affairs and Trade | dfat.e-invoicing.prod@dfat.gov.au on directory.peppol.eu (site dfat.gov.au)
- **14 DMARC / SPF / provider columns filled**
    - P06M_member_or_regulated_payer_of_canadian_body_other_email:59 Selkirk College | not checked yet | not checked yet | not checked
    - P08_client_listing_general_email:1083 royallepage.ca | not checked yet | not checked yet | not checked
    - P08_client_listing_general_email:2451 Strike | not checked yet | not checked yet | not checked
    - P10_linked_from_vendor_site_any_email:564 centris.ca | not checked yet | not checked yet | not checked
    - P13_inferred_relationship_no_record_own_email_part1_of_5:17 sun-nurses.sk.ca | not checked yet | not checked yet | not checked
    - P13_inferred_relationship_no_record_own_email_part1_of_5:135 rdubz.ca | not checked yet | not checked yet | not checked
    - P13_inferred_relationship_no_record_own_email_part1_of_5:136 sapm.qc.ca | not checked yet | not checked yet | not checked
    - P13_inferred_relationship_no_record_own_email_part1_of_5:137 soccerlsl.qc.ca | not checked yet | not checked yet | not checked
    - P13_inferred_relationship_no_record_own_email_part1_of_5:138 thegolfdome.ca | not checked yet | not checked yet | not checked
    - P13_inferred_relationship_no_record_own_email_part1_of_5:139 townofshellbrook.ca | not checked yet | not checked yet | not checked
    - P13_inferred_relationship_no_record_own_email_part1_of_5:222 townofcoronach.ca | not checked yet | not checked yet | not checked
    - P13_inferred_relationship_no_record_own_email_part1_of_5:372 relianceproperties.ca | not checked yet | not checked yet | not checked
- **19 buyer name is a name (not a domain or a page title)**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:13 uwindsor.ca | uwindsor.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:28 thebigcarrot.ca | thebigcarrot.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:33 ovs.com | ovs.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:79 hacc.edu | hacc.edu
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:91 cognizant.com | cognizant.com
    - P01_GOLD_active_relationship_invoicing_AP_email:430 capreit.ca | capreit.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:471 gov.edmonton.ab.ca | gov.edmonton.ab.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:475 arthomson.com | arthomson.com
    - P01_GOLD_active_relationship_invoicing_AP_email:521 bcib.ca | bcib.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:537 toronto.ca | toronto.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:564 slrd.bc.ca | slrd.bc.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:579 corporate.exxonmobil.com | corporate.exxonmobil.com
- **22 one row per organisation name (same name twice)**
    - P03_active_relationship_purchasing_email:226 Westbank First Nation | 2 rows, same mail domain: wfn.ca
    - P04_active_relationship_general_email:336 Cégep de Victoriaville. | 2 rows, same mail domain: cegepvicto.ca
    - P05_likely_active_awarded_12_36_months_any_email:6 Brandon University | 2 rows, same mail domain: brandonu.ca
- **23 one row per site domain (two rows, different mailboxes, same domain)**
    - P01_GOLD_active_relationship_invoicing_AP_email:26 University of Toronto | utoronto.ca: 2 rows, ap.fsd@utoronto.ca; fmdinvoice.utsc@utoronto.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:56 Ville de Gatineau | gatineau.ca: 2 rows, gatineau.factures@gatineau.ca; idgatineau@gatineau.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:65 Ville de Montréal | montreal.ca: 2 rows, facture@montreal.ca; comptesapayer@montreal.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:82 Ville de Laval | laval.ca: 3 rows, comptespayables@laval.ca; lavaleconomique@laval.ca; info@laval.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:91 Ville de Blainville | blainville.ca: 2 rows, approvisionnements@blainville.ca; finances@blainville.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:114 Texas Department of Insurance | texas.gov: 7 rows, invoices@tdi.texas.gov; ap@tsl.texas.gov; accounts.payable@tpwd.texas.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:128 University of Ottawa | uottawa.ca: 2 rows, payables@uottawa.ca; info@emba.uottawa.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:195 Oregon Department of Transportation | oregon.gov: 3 rows, opoinvoiceinquiries@odot.oregon.gov; omdaccounts.payable@omd.oregon.gov; odf.accountspayable@oregon.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:197 Texas Tech University Health Sciences Ce | ttuhsc.edu: 2 rows, Accounts.Payable@ttuhsc.edu; accountspayableelp@ttuhsc.edu
    - P01_GOLD_active_relationship_invoicing_AP_email:229 Metrolinx | metrolinx.com: 2 rows, it.invoices@metrolinx.com; rti.invoices@metrolinx.com
    - P01_GOLD_active_relationship_invoicing_AP_email:249 Niagara Region | niagararegion.ca: 2 rows, constructioninvoices@niagararegion.ca; NRHCapitalWorks@niagararegion.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:340 Virginia State Police | virginia.gov: 5 rows, ap@vsp.virginia.gov; accountspayable@energy.virginia.gov; support@dhrm.virginia.gov
- **25 jurisdiction vs mailbox top-level domain**
    - P13_inferred_relationship_no_record_own_email_part1_of_5:456 Rheinmetall AG | CA / rheinmetall.com.au
    - P13_inferred_relationship_no_record_own_email_part1_of_5:468 Westpac | CA / westpac.com.au
    - P13_inferred_relationship_no_record_own_email_part1_of_5:507 United States Postal Service | CA / usps.gov
    - P13_inferred_relationship_no_record_own_email_part1_of_5:1222 Randstad Deutschland | CA / randstad.de
    - P13_inferred_relationship_no_record_own_email_part1_of_5:2561 LA MAISON DES JEUNES DE PLESSISVILLE INC | QC / lycos.fr
    - P13_inferred_relationship_no_record_own_email_part1_of_5:3140 The Redeemed Christian Church of God Lov | SK / loveassembly.co.uk
    - P13_inferred_relationship_no_record_own_email_part1_of_5:7073 Trotec Laser Canada | QC / troteclaser.com.au
    - P13_inferred_relationship_no_record_own_email_part2_of_5:2731 KNDS | CA / knds.de
    - P13_inferred_relationship_no_record_own_email_part2_of_5:2750 The Warehouse Group | CA / thewarehousegroup.co.nz
    - P13_inferred_relationship_no_record_own_email_part2_of_5:8539 akelius.ca | CA / akelius.fr
    - P13_inferred_relationship_no_record_own_email_part3_of_5:249 apexauctions.ca | CA / apexauctions.co.uk
    - P13_inferred_relationship_no_record_own_email_part3_of_5:3817 dermfix.ca | CA / dermfix.uk
- **26 currency filled when a value is filled**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:22 RENTON SCHOOL DISTRICT #403 | 332345.13 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:423 Rectorado de la Universitat de València | 12698.25 (source field: PayableAmount)
    - P01_GOLD_active_relationship_invoicing_AP_email:434 BRINKS DE COLOMBIA S.A. | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:453 University of North Dakota | 145.850 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:476 BELLEVUE, CITY OF | 35488873.2 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:483 UNIVERSITY PLACE SCHOOL DISTRICT #83 | 685477.9 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:500 North Dakota State University | 35.000 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:505 BELLEVUE SCHOOL DISTRICT #405 | 5395.88 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:510 SNOQUALMIE VALLEY SCHOOL DISTRICT #410 | 23980.42 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:515 MARYLAND STADIUM AUTHORITY | 251569.05 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:528 ECOPETROL S A | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:556 Fundación para la Investigación del Hosp | 1236.23 (source field: PayableAmount)

## Rows per package
- P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email: 18
- P01T_active_service_seen_on_buyer_site_invoicing_AP_email: 90
- P01_GOLD_active_relationship_invoicing_AP_email: 579
- P02_active_relationship_finance_accounting_email: 366
- P03_active_relationship_purchasing_email: 225
- P04_active_relationship_general_email: 1571
- P05_likely_active_awarded_12_36_months_any_email: 375
- P06M_member_or_regulated_payer_of_canadian_body_other_email: 169
- P06T_active_service_seen_on_buyer_site_other_email: 2423
- P06_client_listing_invoicing_AP_email: 160
- P07_client_listing_finance_or_purchasing_email: 245
- P08_client_listing_general_email: 3059
- P09_older_contract_or_payment_any_email: 364
- P10_linked_from_vendor_site_any_email: 2605
- P11_any_relationship_email_not_yet_confirmed: 457
- P12_weaker_relationship_within_5_years_own_email: 22
- P13_inferred_relationship_no_record_own_email: 43186

## Field fill across all delivered rows (value present, not `not_published`)
- buyer_website: 55914 (100.0%)
- vendor_address: 52762 (94.4%)
- vendor_website: 51380 (91.9%)
- buyer_logo_url: 31077 (55.6%)
- buyer_address: 30543 (54.6%)
- buyer_phone: 21867 (39.1%)
- vendor_phone: 17406 (31.1%)
- contract_link: 12728 (22.8%)
- vendor_logo_url: 6774 (12.1%)
- buyer_legal_name_as_published: 6551 (11.7%)
- vendor_legal_name: 6440 (11.5%)
- award_date: 6420 (11.5%)
- vendor_registry_id: 5231 (9.4%)
- vendor_emails: 4276 (7.6%)
- vendor_bn9: 2444 (4.4%)
- contract_value: 2282 (4.1%)
- vendor_incorporation_date: 2067 (3.7%)
- ap_phone: 1754 (3.1%)
- invoice_mailing_address: 1669 (3.0%)
- end_date: 1653 (3.0%)
- buyer_bn_as_published: 1615 (2.9%)
- invoicing_requirements: 1345 (2.4%)
- payment_terms_as_published: 158 (0.3%)
- ap_contact_name_as_published: 132 (0.2%)
- po_required_as_published: 125 (0.2%)
- invoice_portal_url: 48 (0.1%)
- vendor_neq: 23 (0.0%)

## Canada-proof families
- other: 40110; source field: 15804

## Buyer types
- organisation (type not stated in the record): 37621
- company (private sector): 8018
- non-profit / association / cultural body: 6175
- municipality / local government: 1108
- government ministry / agency: 960
- hospital / health authority: 659
- university / college: 422
- utility / public corporation: 409
- transport / transit authority: 178
- school board / school district: 170
- First Nation / Indigenous government: 154
- US government body (federal, state or local): 29
- US city / county / local government: 11

## DMARC posture of the delivered mailboxes
- v=DMARC1; p=none (monitor only, no enforcement): 20820
- no DMARC record: 17617
- p=quarantine: 9010
- p=reject: 4777
- not checked yet: 3639
- invalid DMARC record: 45
- DNS lookup failed: 6
