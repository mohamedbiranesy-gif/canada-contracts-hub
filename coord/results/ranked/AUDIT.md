# Deep audit — 63322 delivered rows in 17 packages (22 files), 2026-11-07

Result: **PASS** — 11 hard checks, 17 soft checks; hard failures: 0. Every flagged row is listed in `audit_flags.csv` with its reasons.

| # | check | kind | rows flagged | verdict |
|---|---|---|---|---|
| 1 | header: identical columns in every file (106 since 2026-11-06) | hard | 0 | PASS |
| 2 | mailbox syntax | hard | 0 | PASS |
| 3 | mailbox referee-confirmed (all but P11) | hard | 0 | PASS |
| 4 | mail server (MX or A) on the mailbox domain | hard | 0 | PASS |
| 4b | mail server not yet checked (row newer than the last DNS pass) | soft | 11010 | REVIEW |
| 5 | no webmail domain | hard | 0 | PASS |
| 6 | no person-like local part | hard | 0 | PASS |
| 7 | role word in the local part | soft | 3523 | REVIEW |
| 8 | receivables-looking local part graded invoicing/AP | soft | 35 | REVIEW |
| 9 | shared government domain: page or quote names the body | soft | 2 | REVIEW |
| 10 | regional token of a multinational on a differently-located body | soft | 0 | PASS |
| 11 | quote contains the address | hard | 0 | PASS |
| 11b | quote shows the label next to the address (referee saw the address on the page) | soft | 1 | REVIEW |
| 12 | evidence page on the organisation's domain (or its site) | soft | 3756 | REVIEW |
| 13 | email_type label matches grade | hard | 0 | PASS |
| 14 | DMARC / SPF / provider columns filled | soft | 11008 | REVIEW |
| 15 | tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m) | soft | 4 | REVIEW |
| 16 | vendor named and Canada proof present | hard | 0 | PASS |
| 17 | Canada proof is a source field or the vendor's site (never a name) | soft | 0 | PASS |
| 18 | record link present for dated-record tiers | soft | 0 | PASS |
| 19 | buyer name is a name (not a domain or a page title) | soft | 30712 | REVIEW |
| 20 | legal name is not a fragment or a platform copyright | soft | 0 | PASS |
| 21 | one row per mailbox | hard | 0 | PASS |
| 22 | one row per organisation name (same name twice) | soft | 3 | REVIEW |
| 23 | one row per site domain (two rows, different mailboxes, same domain) | soft | 66 | REVIEW |
| 24 | no blank cell | hard | 0 | PASS |
| 25 | jurisdiction vs mailbox top-level domain | soft | 40 | REVIEW |
| 26 | currency filled when a value is filled | soft | 46 | REVIEW |

## How to read the REVIEW lines (none of them is a rule break; each is a known limit, stated so nothing is hidden)
- **4b** — rows whose mail domain entered after the last DNS pass; checked on the next pass.
- **7** — the audit's role-word vocabulary is narrower than the referee's (`ap_cameco@`, `invsubp@`, `acquisitions@`, `beschaffung@` are role boxes it does not recognise by word); every one was referee-verified on the organisation's own page.
- **8** — `payments@`-style boxes graded invoicing/AP only where the page itself says invoices or suppliers go there.
- **9** — government-wide domains where the page names the body only loosely; clear misattributions were removed on 2026-11-04.
- **11b** — the referee saw the address on the page; the stored quote shows the label next to it.
- **12** — the evidence page is on a different domain than the mailbox / website (a second domain of the same organisation, a PDF host, a shared government site); the same-organisation check passed on the name.
- **19** — P13 organisations known only by their site's domain (no better name on the site); mailbox, DNS and inferred relationship unaffected.
- **22 / 23** — same short name used by different entities, or two bodies on one site domain; treated as distinct on purpose.
- **25** — Canadian-jurisdiction rows whose mailbox is on a foreign TLD (a multinational's or a network's shared mailbox); kept, flagged.
- **26** — a value published without a currency by the source; left as published.

## Examples of flagged rows (first 12 per check)
- **4b mail server not yet checked (row newer than the last DNS pass)**
    - P06M_member_or_regulated_payer_of_canadian_body_other_email:59 Selkirk College | selkirk.ca
    - P06M_member_or_regulated_payer_of_canadian_body_other_email:133 Holden | holden.ca
    - P08_client_listing_general_email:1077 royallepage.ca | royallepage.ca
    - P08_client_listing_general_email:2332 Total Fitness | totalfitnesslangley.com
    - P08_client_listing_general_email:2443 Strike | strikegroup.ca
    - P08_client_listing_general_email:2831 performance.ca | performance.ca
    - P10_linked_from_vendor_site_any_email:186 whiwh.com | whiwh.com
    - P10_linked_from_vendor_site_any_email:322 Dependable Truck & Tank Limited | dependable.ca
    - P10_linked_from_vendor_site_any_email:565 centris.ca | centris.ca
    - P13_inferred_relationship_no_record_own_email_part1_of_6:13 aliasformation.ca | aliasformation.ca
    - P13_inferred_relationship_no_record_own_email_part1_of_6:18 sun-nurses.sk.ca | sun-nurses.sk.ca
    - P13_inferred_relationship_no_record_own_email_part1_of_6:123 aventuriers.qc.ca | aventuriers.qc.ca
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
    - P13_inferred_relationship_no_record_own_email_part1_of_6:10 THE ROYAL CANADIAN COLLEGE OF ORGANISTS- | payment@rcco-ottawa.ca
- **9 shared government domain: page or quote names the body**
    - P01_GOLD_active_relationship_invoicing_AP_email:42 Canadian Space Agency | invoicing.csa-asc.facturation@canada.ca ← https://www.canada.ca/en/public-services-procurement/services/payments-to-from-g
    - P13_inferred_relationship_no_record_own_email_part1_of_6:540 Landlord and Tenant Board | ltbpayments@ontario.ca ← https://tribunalsontario.ca/ltb/contact/
- **11b quote shows the label next to the address (referee saw the address on the page)**
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
    - P06M_member_or_regulated_payer_of_canadian_body_other_email:133 Holden | not checked yet | not checked yet | not checked
    - P08_client_listing_general_email:1077 royallepage.ca | not checked yet | not checked yet | not checked
    - P08_client_listing_general_email:2332 Total Fitness | not checked yet | not checked yet | not checked
    - P08_client_listing_general_email:2443 Strike | not checked yet | not checked yet | not checked
    - P08_client_listing_general_email:2831 performance.ca | not checked yet | not checked yet | not checked
    - P10_linked_from_vendor_site_any_email:186 whiwh.com | not checked yet | not checked yet | not checked
    - P10_linked_from_vendor_site_any_email:322 Dependable Truck & Tank Limited | not checked yet | not checked yet | not checked
    - P10_linked_from_vendor_site_any_email:565 centris.ca | not checked yet | not checked yet | not checked
    - P13_inferred_relationship_no_record_own_email_part1_of_6:13 aliasformation.ca | not checked yet | not checked yet | not checked
    - P13_inferred_relationship_no_record_own_email_part1_of_6:18 sun-nurses.sk.ca | not checked yet | not checked yet | not checked
    - P13_inferred_relationship_no_record_own_email_part1_of_6:123 aventuriers.qc.ca | not checked yet | not checked yet | not checked
- **15 tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m)**
    - P01_GOLD_active_relationship_invoicing_AP_email:141 Commission scolaire New Frontiers | A with end 2026-11-06
    - P02_active_relationship_finance_accounting_email:40 Cégep Édouard-Montpetit | A with end 2026-11-06
    - P02_active_relationship_finance_accounting_email:131 Municipalité de Rivière-Ouelle | A with end 2026-11-06
    - P04_active_relationship_general_email:116 Municipalité de Brébeuf | A with end 2026-11-06
- **19 buyer name is a name (not a domain or a page title)**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:13 uwindsor.ca | uwindsor.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:28 thebigcarrot.ca | thebigcarrot.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:33 ovs.com | ovs.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:79 hacc.edu | hacc.edu
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:92 cognizant.com | cognizant.com
    - P01_GOLD_active_relationship_invoicing_AP_email:430 capreit.ca | capreit.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:471 gov.edmonton.ab.ca | gov.edmonton.ab.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:521 bcib.ca | bcib.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:537 toronto.ca | toronto.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:564 slrd.bc.ca | slrd.bc.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:579 corporate.exxonmobil.com | corporate.exxonmobil.com
    - P02_active_relationship_finance_accounting_email:279 saddlehills.ab.ca | saddlehills.ab.ca
- **22 one row per organisation name (same name twice)**
    - P03_active_relationship_purchasing_email:226 Westbank First Nation | 2 rows, same mail domain: wfn.ca
    - P04_active_relationship_general_email:334 Cégep de Victoriaville. | 2 rows, same mail domain: cegepvicto.ca
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
    - P13_inferred_relationship_no_record_own_email_part1_of_6:493 Rheinmetall AG | CA / rheinmetall.com.au
    - P13_inferred_relationship_no_record_own_email_part1_of_6:505 Westpac | CA / westpac.com.au
    - P13_inferred_relationship_no_record_own_email_part1_of_6:544 United States Postal Service | CA / usps.gov
    - P13_inferred_relationship_no_record_own_email_part1_of_6:1365 Randstad Deutschland | CA / randstad.de
    - P13_inferred_relationship_no_record_own_email_part1_of_6:2705 LA MAISON DES JEUNES DE PLESSISVILLE INC | QC / lycos.fr
    - P13_inferred_relationship_no_record_own_email_part1_of_6:3286 The Redeemed Christian Church of God Lov | SK / loveassembly.co.uk
    - P13_inferred_relationship_no_record_own_email_part1_of_6:7873 Trotec Laser Canada | QC / troteclaser.com.au
    - P13_inferred_relationship_no_record_own_email_part2_of_6:3756 KNDS | CA / knds.de
    - P13_inferred_relationship_no_record_own_email_part2_of_6:3775 The Warehouse Group | CA / thewarehousegroup.co.nz
    - P13_inferred_relationship_no_record_own_email_part3_of_6:1311 akelius.ca | CA / akelius.fr
    - P13_inferred_relationship_no_record_own_email_part3_of_6:1765 apexauctions.ca | CA / apexauctions.co.uk
    - P13_inferred_relationship_no_record_own_email_part3_of_6:6044 custompens.ca | CA / custompens.com.au
- **26 currency filled when a value is filled**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:22 RENTON SCHOOL DISTRICT #403 | 332345.13 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:423 Rectorado de la Universitat de València | 12698.25 (source field: PayableAmount)
    - P01_GOLD_active_relationship_invoicing_AP_email:434 BRINKS DE COLOMBIA S.A. | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:453 University of North Dakota | 145.850 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:475 BELLEVUE, CITY OF | 35488873.2 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:483 UNIVERSITY PLACE SCHOOL DISTRICT #83 | 685477.9 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:500 North Dakota State University | 35.000 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:505 BELLEVUE SCHOOL DISTRICT #405 | 5395.88 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:510 SNOQUALMIE VALLEY SCHOOL DISTRICT #410 | 23980.42 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:515 MARYLAND STADIUM AUTHORITY | 251569.05 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:528 ECOPETROL S A | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:556 Fundación para la Investigación del Hosp | 1236.23 (source field: PayableAmount)

## Rows per package
- P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email: 18
- P01T_active_service_seen_on_buyer_site_invoicing_AP_email: 91
- P01_GOLD_active_relationship_invoicing_AP_email: 579
- P02_active_relationship_finance_accounting_email: 368
- P03_active_relationship_purchasing_email: 225
- P04_active_relationship_general_email: 1625
- P05_likely_active_awarded_12_36_months_any_email: 377
- P06M_member_or_regulated_payer_of_canadian_body_other_email: 170
- P06T_active_service_seen_on_buyer_site_other_email: 2422
- P06_client_listing_invoicing_AP_email: 160
- P07_client_listing_finance_or_purchasing_email: 246
- P08_client_listing_general_email: 3051
- P09_older_contract_or_payment_any_email: 367
- P10_linked_from_vendor_site_any_email: 2606
- P11_any_relationship_email_not_yet_confirmed: 459
- P12_weaker_relationship_within_5_years_own_email: 22
- P13_inferred_relationship_no_record_own_email: 50536

## Field fill across all delivered rows (value present, not `not_published`)
- buyer_website: 63322 (100.0%)
- vendor_address: 60144 (95.0%)
- vendor_website: 58740 (92.8%)
- buyer_logo_url: 31081 (49.1%)
- buyer_address: 30569 (48.3%)
- buyer_phone: 21869 (34.5%)
- vendor_phone: 18459 (29.2%)
- contract_link: 12786 (20.2%)
- vendor_logo_url: 6789 (10.7%)
- buyer_legal_name_as_published: 6554 (10.4%)
- award_date: 6478 (10.2%)
- vendor_legal_name: 6472 (10.2%)
- vendor_registry_id: 5264 (8.3%)
- vendor_emails: 4277 (6.8%)
- vendor_bn9: 2468 (3.9%)
- contract_value: 2281 (3.6%)
- vendor_incorporation_date: 2068 (3.3%)
- ap_phone: 1758 (2.8%)
- invoice_mailing_address: 1671 (2.6%)
- end_date: 1648 (2.6%)
- buyer_bn_as_published: 1615 (2.6%)
- invoicing_requirements: 1349 (2.1%)
- payment_terms_as_published: 169 (0.3%)
- ap_contact_name_as_published: 134 (0.2%)
- po_required_as_published: 127 (0.2%)
- invoice_portal_url: 48 (0.1%)
- vendor_neq: 23 (0.0%)

## Canada-proof families
- other: 47031; source field: 16291

## Buyer types
- organisation (type not stated in the record): 44999
- company (private sector): 8024
- non-profit / association / cultural body: 6194
- municipality / local government: 1110
- government ministry / agency: 960
- hospital / health authority: 660
- university / college: 422
- utility / public corporation: 411
- transport / transit authority: 178
- school board / school district: 170
- First Nation / Indigenous government: 154
- US government body (federal, state or local): 29
- US city / county / local government: 11

## DMARC posture of the delivered mailboxes
- v=DMARC1; p=none (monitor only, no enforcement): 20842
- no DMARC record: 17630
- not checked yet: 11008
- p=quarantine: 9011
- p=reject: 4779
- invalid DMARC record: 45
- DNS lookup failed: 7
