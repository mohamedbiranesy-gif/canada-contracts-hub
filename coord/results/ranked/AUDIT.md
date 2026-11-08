# Deep audit — 63580 delivered rows in 17 packages (26 files), 2026-11-08

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
| 7 | role word in the local part | soft | 3534 | REVIEW |
| 8 | receivables-looking local part graded invoicing/AP | soft | 35 | REVIEW |
| 9 | shared government domain: page or quote names the body | soft | 2 | REVIEW |
| 10 | regional token of a multinational on a differently-located body | soft | 0 | PASS |
| 11 | quote contains the address | hard | 0 | PASS |
| 11b | quote shows the label next to the address (referee saw the address on the page) | soft | 0 | PASS |
| 12 | evidence page on the organisation's domain (or its site) | soft | 3731 | REVIEW |
| 13 | email_type label matches grade | hard | 0 | PASS |
| 14 | DMARC / SPF / provider columns filled | soft | 0 | PASS |
| 15 | tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m) | soft | 6 | REVIEW |
| 16 | vendor named and Canada proof present | hard | 0 | PASS |
| 17 | Canada proof is a source field or the vendor's site (never a name) | soft | 0 | PASS |
| 18 | record link present for dated-record tiers | soft | 0 | PASS |
| 19 | buyer name is a name (not a domain or a page title) | soft | 28688 | REVIEW |
| 20 | legal name is not a fragment or a platform copyright | soft | 0 | PASS |
| 21 | one row per mailbox | hard | 0 | PASS |
| 22 | one row per organisation name (same name twice) | soft | 3 | REVIEW |
| 23 | one row per site domain (two rows, different mailboxes, same domain) | soft | 65 | REVIEW |
| 24 | no blank cell | hard | 0 | PASS |
| 25 | jurisdiction vs mailbox top-level domain | soft | 40 | REVIEW |
| 26 | currency filled when a value is filled | soft | 46 | REVIEW |

## Examples of flagged rows (first 12 per check)
- **4b mail server not yet checked (row newer than the last DNS pass)**
    - P13_inferred_relationship_no_record_own_email_part2_of_10:2207 Everest Services Ltd | everest.ca
- **7 role word in the local part**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:16 Cameco Corporation | ap_cameco@cameco.com
    - P01_GOLD_active_relationship_invoicing_AP_email:262 Town of Oakville | ap_inquiries@oakville.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:281 Miami-Dade County (business unit CU05010 | invsubp@miamidade.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:378 BELL TEXTRON INC | APBell@textron.com
    - P02_active_relationship_finance_accounting_email:7 Agriculture and Agri-Food Canada | directdeposit.depotdirect@canada.ca
    - P02_active_relationship_finance_accounting_email:13 Crown-Indigenous Relations and Northern  | depotdirect-directdeposit@sac-isc.gc.ca
    - P02_active_relationship_finance_accounting_email:14 Department of Justice Canada | mdv_dpf@justice.gc.ca
    - P02_active_relationship_finance_accounting_email:18 Health Canada | hc.direct.deposit.requests-demande.de.depot.direct.sc@canada.ca
    - P02_active_relationship_finance_accounting_email:19 Innovation, Science and Economic Develop | ifmscustomer-clientsifm@ised-isde.gc.ca
    - P02_active_relationship_finance_accounting_email:21 National Defence | ddenrol-inscriredd@forces.gc.ca
    - P02_active_relationship_finance_accounting_email:29 Social Sciences and Humanities Research  | directdeposit-depotdirect@crsh-sshrc.gc.ca
    - P02_active_relationship_finance_accounting_email:31 Veterans Affairs Canada | directdeposit-depotdirect@vac-acc.gc.ca
- **8 receivables-looking local part graded invoicing/AP**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:11 Empress | payments@villageofempress.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:4 Texas Tech University | payment.strategies@ttu.edu
    - P01_GOLD_active_relationship_invoicing_AP_email:38 Environment and Climate Change Canada | renseignement-paiements-payments-inquiry@ec.gc.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:467 Township of Georgian Bay | payments@gbtownship.ca
    - P05_likely_active_awarded_12_36_months_any_email:26 Martensville | payments@martensville.ca
    - P06_client_listing_invoicing_AP_email:27 University of Bath | payments@bath.ac.uk
    - P06_client_listing_invoicing_AP_email:69 teamviewer.com | payments@teamviewer.com
    - P06_client_listing_invoicing_AP_email:143 blomidonnurseries.com | payments@blomidonnurseries.com
    - P10_linked_from_vendor_site_any_email:12 gov.scot | online_payments@gov.scot
    - P10_linked_from_vendor_site_any_email:29 WeirFoulds LLP | payments@weirfoulds.com
    - P10_linked_from_vendor_site_any_email:36 bcica.org | payments@bcica.org
    - P13_inferred_relationship_no_record_own_email_part1_of_10:10 THE ROYAL CANADIAN COLLEGE OF ORGANISTS- | payment@rcco-ottawa.ca
- **9 shared government domain: page or quote names the body**
    - P01_GOLD_active_relationship_invoicing_AP_email:42 Canadian Space Agency | invoicing.csa-asc.facturation@canada.ca ← https://www.canada.ca/en/public-services-procurement/services/payments-to-from-g
    - P13_inferred_relationship_no_record_own_email_part1_of_10:542 Landlord and Tenant Board | ltbpayments@ontario.ca ← https://tribunalsontario.ca/ltb/contact/
- **12 evidence page on the organisation's domain (or its site)**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:18 Motorola Solutions, Inc | recepcionfacturas@motorolasolutions.com on web.archive.org (site motorolasolutions.com)
    - P01_GOLD_active_relationship_invoicing_AP_email:2 Department of Defence | peppol.einvoices@defence.gov.au on directory.peppol.eu (site defence.gov.au)
    - P01_GOLD_active_relationship_invoicing_AP_email:3 Department of Industry, Science and Reso | einvoicingqueries@industry.gov.au on directory.peppol.eu (site industry.gov.au)
    - P01_GOLD_active_relationship_invoicing_AP_email:50 Natural Sciences and Engineering Researc | payables@nserc-crsng.gc.ca on nserc-crsng.canada.ca (site nserc-crsng.gc.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:65 Ville de Montréal | facture@montreal.ca on ville.montreal.qc.ca (site montreal.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:94 Ville de Farnham | comptespayables@ville.farnham.qc.ca on web.archive.org (site ville.farnham.qc.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:112 UK Atomic Energy Authority | finance@uk-atomic-energy.org.uk on assets.publishing.service.gov.uk (site gov.uk)
    - P01_GOLD_active_relationship_invoicing_AP_email:125 City of Chestermere | city.ap@chestermere.ca on thecityofchestermere.ca (site chestermere.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:131 Newfoundland and Labrador Liquor Corpora | Accounts.Payable@nlliquor.com on nlliquorcorp.com (site nlliquor.com)
    - P01_GOLD_active_relationship_invoicing_AP_email:133 The Ottawa Hospital | tohaccountspayable@toh.ca on ottawahospital.on.ca (site toh.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:156 UK Research and Innovation | finance@uksbs.co.uk on ukri.org (site uksbs.co.uk)
    - P01_GOLD_active_relationship_invoicing_AP_email:162 Department of Foreign Affairs and Trade | dfat.e-invoicing.prod@dfat.gov.au on directory.peppol.eu (site dfat.gov.au)
- **15 tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m)**
    - P01_GOLD_active_relationship_invoicing_AP_email:140 Commission scolaire New Frontiers | A with end 2026-11-06
    - P02_active_relationship_finance_accounting_email:40 Cégep Édouard-Montpetit | A with end 2026-11-06
    - P02_active_relationship_finance_accounting_email:132 Municipalité de Rivière-Ouelle | A with end 2026-11-06
    - P02_active_relationship_finance_accounting_email:185 Municipalité de Ripon | A with end 2026-11-07
    - P04_active_relationship_general_email:114 Municipalité de Brébeuf | A with end 2026-11-06
    - P11_any_relationship_email_not_yet_confirmed:9 Municipalité de Saint-Apollinaire | A with end 2026-11-07
- **19 buyer name is a name (not a domain or a page title)**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:13 uwindsor.ca | uwindsor.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:28 thebigcarrot.ca | thebigcarrot.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:33 ovs.com | ovs.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:79 hacc.edu | hacc.edu
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:92 cognizant.com | cognizant.com
    - P01_GOLD_active_relationship_invoicing_AP_email:431 capreit.ca | capreit.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:472 gov.edmonton.ab.ca | gov.edmonton.ab.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:522 bcib.ca | bcib.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:538 toronto.ca | toronto.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:566 slrd.bc.ca | slrd.bc.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:581 corporate.exxonmobil.com | corporate.exxonmobil.com
    - P02_active_relationship_finance_accounting_email:280 saddlehills.ab.ca | saddlehills.ab.ca
- **22 one row per organisation name (same name twice)**
    - P03_active_relationship_purchasing_email:226 Westbank First Nation | 2 rows, same mail domain: wfn.ca
    - P04_active_relationship_general_email:331 Cégep de Victoriaville. | 2 rows, same mail domain: cegepvicto.ca
    - P05_likely_active_awarded_12_36_months_any_email:5 Brandon University | 2 rows, same mail domain: brandonu.ca
- **23 one row per site domain (two rows, different mailboxes, same domain)**
    - P01_GOLD_active_relationship_invoicing_AP_email:26 University of Toronto | utoronto.ca: 2 rows, ap.fsd@utoronto.ca; fmdinvoice.utsc@utoronto.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:56 Ville de Gatineau | gatineau.ca: 2 rows, gatineau.factures@gatineau.ca; idgatineau@gatineau.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:65 Ville de Montréal | montreal.ca: 2 rows, facture@montreal.ca; comptesapayer@montreal.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:81 Ville de Laval | laval.ca: 3 rows, comptespayables@laval.ca; lavaleconomique@laval.ca; info@laval.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:90 Ville de Blainville | blainville.ca: 2 rows, approvisionnements@blainville.ca; finances@blainville.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:113 Texas Department of Insurance | texas.gov: 7 rows, invoices@tdi.texas.gov; ap@tsl.texas.gov; accounts.payable@tpwd.texas.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:127 University of Ottawa | uottawa.ca: 2 rows, payables@uottawa.ca; info@emba.uottawa.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:194 Oregon Department of Transportation | oregon.gov: 3 rows, opoinvoiceinquiries@odot.oregon.gov; omdaccounts.payable@omd.oregon.gov; odf.accountspayable@oregon.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:196 Texas Tech University Health Sciences Ce | ttuhsc.edu: 2 rows, Accounts.Payable@ttuhsc.edu; accountspayableelp@ttuhsc.edu
    - P01_GOLD_active_relationship_invoicing_AP_email:228 Metrolinx | metrolinx.com: 2 rows, it.invoices@metrolinx.com; rti.invoices@metrolinx.com
    - P01_GOLD_active_relationship_invoicing_AP_email:248 Niagara Region | niagararegion.ca: 2 rows, constructioninvoices@niagararegion.ca; NRHCapitalWorks@niagararegion.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:340 Virginia State Police | virginia.gov: 5 rows, ap@vsp.virginia.gov; accountspayable@energy.virginia.gov; support@dhrm.virginia.gov
- **25 jurisdiction vs mailbox top-level domain**
    - P13_inferred_relationship_no_record_own_email_part10_of_10:311 Bernafon Canada | ON / bernafon.com.au
    - P13_inferred_relationship_no_record_own_email_part10_of_10:2340 Déontologie : approche comparée FR / QC | CA / univ-droit.fr
    - P13_inferred_relationship_no_record_own_email_part10_of_10:2833 Shah's Halal Food | CA / shahshalalfood.co.uk
    - P13_inferred_relationship_no_record_own_email_part10_of_10:2892 Hochtief | CA / hochtief.de
    - P13_inferred_relationship_no_record_own_email_part10_of_10:3412 Canada at the 2013 World Aquatics Champi | CA / dsv.de
    - P13_inferred_relationship_no_record_own_email_part10_of_10:3441 Pro Seniore | CA / pro-seniore.de
    - P13_inferred_relationship_no_record_own_email_part10_of_10:3602 Marienhaus | CA / marienhaus.de
    - P13_inferred_relationship_no_record_own_email_part10_of_10:3616 Singa | CA / singa.fr
    - P13_inferred_relationship_no_record_own_email_part10_of_10:3629 SRH Holding | CA / srh.de
    - P13_inferred_relationship_no_record_own_email_part10_of_10:3639 Sparkassen-Finanzgruppe | CA / dsgv.de
    - P13_inferred_relationship_no_record_own_email_part10_of_10:3650 Stihl | CA / stihl.de
    - P13_inferred_relationship_no_record_own_email_part10_of_10:3668 TÜV Nord | CA / tuev-nord.de
- **26 currency filled when a value is filled**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:22 RENTON SCHOOL DISTRICT #403 | 332345.13 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:424 Rectorado de la Universitat de València | 12698.25 (source field: PayableAmount)
    - P01_GOLD_active_relationship_invoicing_AP_email:435 BRINKS DE COLOMBIA S.A. | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:454 University of North Dakota | 145.850 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:476 BELLEVUE, CITY OF | 35488873.2 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:484 UNIVERSITY PLACE SCHOOL DISTRICT #83 | 685477.9 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:501 North Dakota State University | 35.000 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:506 BELLEVUE SCHOOL DISTRICT #405 | 5395.88 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:511 SNOQUALMIE VALLEY SCHOOL DISTRICT #410 | 23980.42 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:516 MARYLAND STADIUM AUTHORITY | 251569.05 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:529 ECOPETROL S A | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:558 Fundación para la Investigación del Hosp | 1236.23 (source field: PayableAmount)

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
- P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email: 19
- P01T_active_service_seen_on_buyer_site_invoicing_AP_email: 91
- P01_GOLD_active_relationship_invoicing_AP_email: 581
- P02_active_relationship_finance_accounting_email: 369
- P03_active_relationship_purchasing_email: 225
- P04_active_relationship_general_email: 1614
- P05_likely_active_awarded_12_36_months_any_email: 379
- P06M_member_or_regulated_payer_of_canadian_body_other_email: 168
- P06T_active_service_seen_on_buyer_site_other_email: 2429
- P06_client_listing_invoicing_AP_email: 160
- P07_client_listing_finance_or_purchasing_email: 246
- P08_client_listing_general_email: 3038
- P09_older_contract_or_payment_any_email: 368
- P10_linked_from_vendor_site_any_email: 2587
- P11_any_relationship_email_not_yet_confirmed: 499
- P12_weaker_relationship_within_5_years_own_email: 21
- P13_inferred_relationship_no_record_own_email: 50786

## Field fill across all delivered rows (value present, not `not_published`)
- buyer_website: 63580 (100.0%)
- vendor_address: 60419 (95.0%)
- vendor_website: 58992 (92.8%)
- buyer_logo_url: 46980 (73.9%)
- buyer_phone: 46697 (73.4%)
- buyer_address: 44972 (70.7%)
- vendor_phone: 18573 (29.2%)
- contract_link: 12794 (20.1%)
- buyer_legal_name_as_published: 10099 (15.9%)
- vendor_logo_url: 6819 (10.7%)
- award_date: 6483 (10.2%)
- vendor_legal_name: 6482 (10.2%)
- vendor_registry_id: 5268 (8.3%)
- vendor_emails: 4281 (6.7%)
- ap_phone: 2600 (4.1%)
- vendor_bn9: 2470 (3.9%)
- contract_value: 2284 (3.6%)
- invoice_mailing_address: 2106 (3.3%)
- vendor_incorporation_date: 2071 (3.3%)
- buyer_bn_as_published: 1901 (3.0%)
- end_date: 1648 (2.6%)
- invoicing_requirements: 1587 (2.5%)
- invoice_portal_url: 657 (1.0%)
- po_required_as_published: 466 (0.7%)
- payment_terms_as_published: 376 (0.6%)
- ap_contact_name_as_published: 173 (0.3%)
- vendor_neq: 23 (0.0%)

## Canada-proof families
- other: 47251; source field: 16329

## Buyer types
- organisation (type not stated in the record): 38711
- company (private sector): 9410
- non-profit / association / cultural body: 6506
- company (private sector) (from the organisation's name / web domain): 1539
- municipality / local government: 1133
- government ministry / agency: 1057
- municipality / local government (from the organisation's name / web domain): 892
- non-profit / association / cultural body (from the organisation's name / web domain): 889
- hospital / health authority: 760
- university / college: 460
- utility / public corporation: 437
- hospital / health authority (from the organisation's name / web domain): 367
- university / college (from the organisation's name / web domain): 316
- transport / transit authority: 185
- school board / school district: 170
- First Nation / Indigenous government: 160
- government ministry / agency (from the organisation's name / web domain): 149
- religious organisation (from the organisation's name / web domain): 141
- utility / public corporation (from the organisation's name / web domain): 119
- transport / transit authority (from the organisation's name / web domain): 67
- First Nation / Indigenous government (from the organisation's name / web domain): 42
- US government body (federal, state or local): 29
- library (from the organisation's name / web domain): 21
- US city / county / local government: 11
- school board / school district (from the organisation's name / web domain): 9

## DMARC posture of the delivered mailboxes
- v=DMARC1; p=none (monitor only, no enforcement): 26422
- no DMARC record: 21266
- p=quarantine: 10429
- p=reject: 5394
- invalid DMARC record: 59
- DNS lookup failed: 10
