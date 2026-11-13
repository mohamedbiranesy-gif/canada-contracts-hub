# Deep audit — 337627 delivered rows in 18 packages (160 files), 2026-11-13

Result: **FAIL** — 11 hard checks, 17 soft checks; hard failures: 2. Every flagged row is listed in `audit_flags.csv` with its reasons.

| # | check | kind | rows flagged | verdict |
|---|---|---|---|---|
| 1 | header: identical columns in every file (106 since 2026-11-06) | hard | 1 | FAIL |
| 2 | mailbox syntax | hard | 0 | PASS |
| 3 | mailbox referee-confirmed (all but P11) | hard | 0 | PASS |
| 4 | mail server (MX or A) on the mailbox domain | hard | 0 | PASS |
| 4b | mail server not yet checked (row newer than the last DNS pass) | soft | 281863 | REVIEW |
| 5 | no webmail domain | hard | 0 | PASS |
| 6 | no person-like local part | hard | 0 | PASS |
| 7 | role word in the local part | soft | 28145 | REVIEW |
| 8 | receivables-looking local part graded invoicing/AP | soft | 75 | REVIEW |
| 9 | shared government domain: page or quote names the body | soft | 2 | REVIEW |
| 10 | regional token of a multinational on a differently-located body | soft | 0 | PASS |
| 11 | quote contains the address | hard | 0 | PASS |
| 11b | quote shows the label next to the address (referee saw the address on the page) | soft | 0 | PASS |
| 12 | evidence page on the organisation's domain (or its site) | soft | 16402 | REVIEW |
| 13 | email_type label matches grade | hard | 0 | PASS |
| 14 | DMARC / SPF / provider columns filled | soft | 0 | PASS |
| 15 | tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m) | soft | 0 | PASS |
| 16 | vendor named and Canada proof present | hard | 2 | FAIL |
| 17 | Canada proof is a source field or the vendor's site (never a name) | soft | 0 | PASS |
| 18 | record link present for dated-record tiers | soft | 2 | REVIEW |
| 19 | buyer name is a name (not a domain or a page title) | soft | 37638 | REVIEW |
| 20 | legal name is not a fragment or a platform copyright | soft | 571 | REVIEW |
| 21 | one row per mailbox | hard | 0 | PASS |
| 22 | one row per organisation name (same name twice) | soft | 0 | PASS |
| 23 | one row per site domain (two rows, different mailboxes, same domain) | soft | 45 | REVIEW |
| 24 | no blank cell | hard | 0 | PASS |
| 25 | jurisdiction vs mailbox top-level domain | soft | 122 | REVIEW |
| 26 | currency filled when a value is filled | soft | 51 | REVIEW |

## Examples of flagged rows (first 12 per check)
- **1 header: identical columns in every file (106 since 2026-11-06)**
    - files | 2 distinct headers; widths [0, 253]
- **4b mail server not yet checked (row newer than the last DNS pass)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:2 Braemed Ltd. | braemed.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:6 Gold Terra Resource Corp. | goldterracorp.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:7 ALK-ABELLÓ A/S | alk.net
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:8 Myco Medical Supplies Inc. | mycomedical.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:9 TILLOTTS PHARMA GMBH | tillotts.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:10 INTER PIPELINE (Corridor) INC. (re COR & | interpipeline.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:12 AltaSteel Inc. | altasteel.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:13 Martineau Coffrage inc. | martineaucoffrage.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:17 Sanjel Energy Services Inc. | sanjel.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:18 Entrada Resources Inc. | entradaresources.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:19 West Lake Energy Corp. | westlakeenergy.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:20 Bighorn Energy Corporation | bighornenergy.ca
- **7 role word in the local part**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:3 Keyera Corp. | ap_inquiries@keyera.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:166 Taylor-Listug, Inc. | ap_group@taylorguitars.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:348 TAE TECHNOLOGIES, INC. | ap_tps@tae.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:372 CENTERPOINT ENERGY, INC. | ap_helpdesk@centerpointenergy.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:8 Scouts de Dieppe | paiement@scoutsdedieppe.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:20 cvqvintage.ca | paiements@cvqvintage.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:33 Clic-Informatique | paiements@clic-informatique.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:113 Cameco Corporation | ap_cameco@cameco.com
    - P01_GOLD_active_relationship_invoicing_AP_email:275 University of Saskatchewan | connectionpoint@usask.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:277 Miami-Dade County (business unit CU05010 | invsubp@miamidade.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:291 Town of Oakville | ap_inquiries@oakville.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:373 BELL TEXTRON INC | APBell@textron.com
- **8 receivables-looking local part graded invoicing/AP**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:77 Calgary Coin Gallery | payment@calgarycoin.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:302 Empress | payments@villageofempress.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:312 birchfumigators.ca | payment@birchfumigators.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:419 Clean Exteriors Ltd. | payments@cleanexteriors.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:422 Twin City Tile Co. Ltd. | payments@twincitytile.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:423 elliottandassociates.ca | payments@elliottandassociates.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:424 Paradisus Window Cleaning & House Washin | payment@paradisuswindowcleaning.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:19 Flashing Canines Agility Club | payments@flashingcanines.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:37 McNamee & Kilpatrick | payments@mcnameekilpatrick.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:42 Stein Works | payments@steinworks.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:53 Penner Auctions | morden.payments@pennerauctions.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:61 Vocal Euphoria | payments@vocaleuphoria.com
- **9 shared government domain: page or quote names the body**
    - P01_GOLD_active_relationship_invoicing_AP_email:549 Tennessee Department of Transportation | pln.invoices@tn.gov ← https://www.tn.gov/tdot/long-range-planning-home/longrange-administration/longra
    - P07_client_listing_finance_or_purchasing_email:548 transportation.ky.gov | finance.crcgroup@ky.gov ← https://finance.ky.gov/eProcurement/Pages/doing-business-with-the-commonwealth.a
- **12 evidence page on the organisation's domain (or its site)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:22 Aluminerie Alouette Inc. | compteapayer@alouette.qc.ca on alouette.com (site alouette.qc.ca)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:25 ATTIS LEBLANC | payable@attis-leblanc.com on attis-leblanc.ca (site attis-leblanc.com)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:82 Oil City Drywall North | accounting@oilcitydrywall.ca on oilcitydrywallnorth.ca (site oilcitydrywall.ca)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:229 TRATON SE | invoices.to@se.traton.com on supplier.scania.com (site traton.com)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:295 National Veterinary Associates, Inc. | payables.canada@nva.com on nvacanada.ca (site nva.com)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:371 SANDOZ INC. | comptes.payables@sandoz.com on sandoz.ca (site sandoz.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:20 cvqvintage.ca | paiements@cvqvintage.ca on coursesvintagequebec.ca (site cvqvintage.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:23 regieincendiekam-ouest.ca | payables@regieincendiekam-ouest.ca on regieincendiekam-ouest.com (site regieincendiekam-ouest.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:76 ibiosolutions.com | payables@ibiosolutions.com on immunebiosolutions.com (site ibiosolutions.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:158 dabc.ca | ap@dabc.ca on disabilityalliancebc.org (site dabc.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:32 Natural Sciences and Engineering Researc | payables@nserc-crsng.gc.ca on nserc-crsng.canada.ca (site nserc-crsng.gc.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:45 Ville de Montréal | facture@montreal.ca on ville.montreal.qc.ca (site montreal.ca)
- **16 vendor named and Canada proof present**
    - P04_active_relationship_general_email_part1_of_2:2193 TC IP, Ltd
    - P04_active_relationship_general_email_part1_of_2:2194 us.benetton.com
- **18 record link present for dated-record tiers**
    - P04_active_relationship_general_email_part1_of_2:2193 TC IP, Ltd | relationship record
    - P04_active_relationship_general_email_part1_of_2:2194 us.benetton.com | relationship record
- **19 buyer name is a name (not a domain or a page title)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:312 birchfumigators.ca | birchfumigators.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:313 dfcdiesel.com | dfcdiesel.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:423 elliottandassociates.ca | elliottandassociates.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:425 ambroseplumbing.ca | ambroseplumbing.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:4 fs.ca | fs.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:20 cvqvintage.ca | cvqvintage.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:23 regieincendiekam-ouest.ca | regieincendiekam-ouest.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:32 nrgqc.com | nrgqc.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:34 it-desgens.ca | it-desgens.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:43 wasonlandscaping.com | wasonlandscaping.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:62 llanteralincoln.com | llanteralincoln.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:65 Awninginabox.ca | Awninginabox.ca
- **20 legal name is not a fragment or a platform copyright**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:2 Braemed Ltd. | Braemed Ltd. (Health Canada's Medical Devices Establishment Licence li
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:15 ZIMMER INC. | ZIMMER INC. (Health Canada's Medical Devices Active Licence Listing (t
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:111 LIN-ZHI INTERNATIONAL, INC. | LIN-ZHI INTERNATIONAL, INC. (Health Canada's Medical Devices Active Li
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:116 VASCUTEK LIMITED | VASCUTEK LIMITED (Health Canada's Medical Devices Active Licence Listi
    - P04_active_relationship_general_email_part2_of_2:451 True Millwork | Introduction Welcome to True Millwork (stated on https://www.truemillw
    - P05_likely_active_awarded_12_36_months_any_email:61 Ameren Illinois Company | Ameren Corporation and/or its suppliers (the copyright line of https:/
    - P05_likely_active_awarded_12_36_months_any_email:215 LOVE WORTH FINDING MINISTRIES INC | LLC. 800-274-5683 2941 Kate Bond Rd, Memphis, TN 38133 CONNECT WITH LW
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part11_of_14:1748 LITCO LAW IS A TRADEMARK AND TRADE NAME  | LITCO LAW IS A TRADEMARK AND TRADE NAME OF LITWINIUK LLP (the copyrigh
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part14_of_14:1357 Dentaurum Canada Inc. | Dentaurum Canada Inc. (Health Canada's Medical Devices Establishment L
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part14_of_14:1393 SEIGLA MEDICAL, INC. | SEIGLA MEDICAL, INC. (Health Canada's Medical Devices Active Licence L
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part14_of_14:2015 GRANICUS, LLC | GRANICUS, LLC (the Canadian trademarks register (owner of record), ext
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part1_of_14:3 Centennial Optical Ltd. | Centennial Optical Ltd. (Health Canada's Medical Devices Establishment
- **23 one row per site domain (two rows, different mailboxes, same domain)**
    - P01_GOLD_active_relationship_invoicing_AP_email:36 Ville de Gatineau | gatineau.ca: 2 rows, gatineau.factures@gatineau.ca; idgatineau@gatineau.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:45 Ville de Montréal | montreal.ca: 2 rows, facture@montreal.ca; comptesapayer@montreal.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:58 Ville de Laval | laval.ca: 3 rows, comptespayables@laval.ca; info@laval.ca; lavaleconomique@laval.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:110 Texas Department of Insurance | texas.gov: 7 rows, invoices@tdi.texas.gov; payableteam@trs.texas.gov; ap@ers.texas.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:125 University of Ottawa | uottawa.ca: 2 rows, payables@uottawa.ca; info@emba.uottawa.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:181 Oregon Department of Transportation | oregon.gov: 3 rows, opoinvoiceinquiries@odot.oregon.gov; omdaccounts.payable@omd.oregon.gov; odf.accountspayable@oregon.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:182 Texas Tech University Health Sciences Ce | ttuhsc.edu: 2 rows, accountspayableelp@ttuhsc.edu; accounts.payable@ttuhsc.edu
    - P01_GOLD_active_relationship_invoicing_AP_email:242 Newfoundland and Labrador Hydro | nlhydro.com: 2 rows, hydroapinvoices@nlh.nl.ca; NalcorAPInvoices@nalcorenergy.com
    - P01_GOLD_active_relationship_invoicing_AP_email:266 Township of Scugog | scugog.ca: 2 rows, invoice@scugog.ca; mail@scugog.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:358 NATO Joint Warfare Centre (Stavanger) | nato.int: 3 rows, invoice@jwc.nato.int; accountspayable.mailbox@hq.nato.int; accountspayable@ncia.nato.int
    - P01_GOLD_active_relationship_invoicing_AP_email:359 Commonwealth of Australia (Royal Austral | defence.gov.au: 2 rows, invoices@defence.gov.au; procurement.asdefcon@defence.gov.au
    - P01_GOLD_active_relationship_invoicing_AP_email:367 Virginia Department of Energy | virginia.gov: 6 rows, accountspayable@energy.virginia.gov; ap@vsp.virginia.gov; support@dhrm.virginia.gov
- **25 jurisdiction vs mailbox top-level domain**
    - P01_GOLD_active_relationship_invoicing_AP_email:295 Utilities Kingston | CA / kingston.gov.uk
    - P13_inferred_relationship_no_record_own_email_part11_of_98:772 julienphoto.fr | CA / julienphoto.fr
    - P13_inferred_relationship_no_record_own_email_part13_of_98:1751 Alenti | ON / alenti.fr
    - P13_inferred_relationship_no_record_own_email_part14_of_98:985 Immigrar Canada | QC / immigrar.fr
    - P13_inferred_relationship_no_record_own_email_part14_of_98:2070 Nicoletta Pty Ltd | QC / nicoletta.com.au
    - P13_inferred_relationship_no_record_own_email_part15_of_98:664 HURON GRAFFENSTADEN SAS | QC / huron.fr
    - P13_inferred_relationship_no_record_own_email_part15_of_98:803 Alto-Shaam, Inc. | ON / alto-shaam.de
    - P13_inferred_relationship_no_record_own_email_part16_of_98:328 LS telcom | ON / lstelcom.fr
    - P13_inferred_relationship_no_record_own_email_part16_of_98:565 EnterOne Corporation | CA / enterone.co.uk
    - P13_inferred_relationship_no_record_own_email_part16_of_98:1242 SurePay | ON / surepay.co.uk
    - P13_inferred_relationship_no_record_own_email_part17_of_98:972 C. & E. Fein GmbH | ON / fein.de
    - P13_inferred_relationship_no_record_own_email_part17_of_98:1218 Denso | ON / denso.co.nz
- **26 currency filled when a value is filled**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:66 RENTON SCHOOL DISTRICT #403 | 332345.13 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:439 Rectorado de la Universitat de València | 12698.25 (source field: PayableAmount)
    - P01_GOLD_active_relationship_invoicing_AP_email:450 BELLEVUE, CITY OF | 35488873.2 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:452 UNIVERSITY PLACE SCHOOL DISTRICT #83 | 685477.9 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:458 BELLEVUE SCHOOL DISTRICT #405 | 5395.88 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:461 SNOQUALMIE VALLEY SCHOOL DISTRICT #410 | 23980.42 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:463 SHORELINE SCHOOL DISTRICT #412 | 919904.69 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:464 MARYLAND STADIUM AUTHORITY | 251569.05 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:492 University of North Dakota | 145.850 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:495 North Dakota State University | 35.000 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:516 BRINKS DE COLOMBIA S.A. | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:574 BANCOLOMBIA S.A. | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)

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
- P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email: 434
- P01T_active_service_seen_on_buyer_site_invoicing_AP_email: 203
- P01_GOLD_active_relationship_invoicing_AP_email: 645
- P02_active_relationship_finance_accounting_email: 484
- P03_active_relationship_purchasing_email: 274
- P04_active_relationship_general_email: 4762
- P05_likely_active_awarded_12_36_months_any_email: 429
- P06M_member_or_regulated_payer_of_canadian_body_other_email: 32175
- P06T_active_service_seen_on_buyer_site_other_email: 55107
- P06_client_listing_invoicing_AP_email: 241
- P07_client_listing_finance_or_purchasing_email: 758
- P08_client_listing_general_email: 28706
- P09_older_contract_or_payment_any_email: 71
- P10R_ca_domain_registration_contract_own_email: 0
- P10_linked_from_vendor_site_any_email: 2005
- P11_any_relationship_email_not_yet_confirmed: 1800
- P12_weaker_relationship_within_5_years_own_email: 11
- P13_inferred_relationship_no_record_own_email: 209522

## Field fill across all delivered rows (value present, not `not_published`)
- buyer_website: 337627 (100.0%)
- vendor_address: 336225 (99.6%)
- vendor_website: 312196 (92.5%)
- buyer_address: 309555 (91.7%)
- vendor_legal_name: 295426 (87.5%)
- vendor_phone: 271340 (80.4%)
- vendor_registry_id: 266862 (79.0%)
- buyer_logo_url: 259858 (77.0%)
- vendor_logo_url: 243017 (72.0%)
- buyer_phone: 198434 (58.8%)
- buyer_legal_name_as_published: 162611 (48.2%)
- vendor_incorporation_date: 152087 (45.0%)
- vendor_bn9: 146631 (43.4%)
- contract_link: 128105 (37.9%)
- award_date: 102736 (30.4%)
- vendor_neq: 85803 (25.4%)
- vendor_emails: 58353 (17.3%)
- buyer_bn_as_published: 54739 (16.2%)
- end_date: 21776 (6.4%)
- contract_value: 9229 (2.7%)
- payment_terms_as_published: 6032 (1.8%)
- po_required_as_published: 3348 (1.0%)
- ap_phone: 3204 (0.9%)
- invoice_portal_url: 2481 (0.7%)
- invoicing_requirements: 2358 (0.7%)
- invoice_mailing_address: 2348 (0.7%)
- ap_contact_name_as_published: 1184 (0.4%)

## Canada-proof families
- source field: 185831; other: 151796

## Buyer types
- organisation (type not stated in the record): 170739
- company (private sector): 64575
- company (private sector) (from the organisation's name / web domain): 52306
- non-profit / association / cultural body: 17203
- government ministry / agency: 8591
- municipality / local government (from the organisation's name / web domain): 4524
- non-profit / association / cultural body (from the organisation's name / web domain): 3777
- hospital / health authority: 3366
- utility / public corporation: 3297
- university / college: 1842
- municipality / local government: 1807
- transport / transit authority: 1194
- hospital / health authority (from the organisation's name / web domain): 915
- utility / public corporation (from the organisation's name / web domain): 635
- government ministry / agency (from the organisation's name / web domain): 619
- university / college (from the organisation's name / web domain): 595
- religious organisation (from the organisation's name / web domain): 417
- transport / transit authority (from the organisation's name / web domain): 361
- First Nation / Indigenous government: 306
- First Nation / Indigenous government (from the organisation's name / web domain): 252
- school board / school district: 204
- school board / school district (from the organisation's name / web domain): 31
- US government body (federal, state or local): 31
- library (from the organisation's name / web domain): 29
- US city / county / local government: 11

## DMARC posture of the delivered mailboxes
- no DMARC record: 138435
- v=DMARC1; p=none (monitor only, no enforcement): 131358
- p=quarantine: 45532
- p=reject: 21920
- invalid DMARC record: 252
- DNS lookup failed: 130
