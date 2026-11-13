# Deep audit — 330174 delivered rows in 18 packages (156 files), 2026-11-13

Result: **FAIL** — 11 hard checks, 17 soft checks; hard failures: 1. Every flagged row is listed in `audit_flags.csv` with its reasons.

| # | check | kind | rows flagged | verdict |
|---|---|---|---|---|
| 1 | header: identical columns in every file (106 since 2026-11-06) | hard | 1 | FAIL |
| 2 | mailbox syntax | hard | 0 | PASS |
| 3 | mailbox referee-confirmed (all but P11) | hard | 0 | PASS |
| 4 | mail server (MX or A) on the mailbox domain | hard | 0 | PASS |
| 4b | mail server not yet checked (row newer than the last DNS pass) | soft | 274797 | REVIEW |
| 5 | no webmail domain | hard | 0 | PASS |
| 6 | no person-like local part | hard | 0 | PASS |
| 7 | role word in the local part | soft | 27567 | REVIEW |
| 8 | receivables-looking local part graded invoicing/AP | soft | 75 | REVIEW |
| 9 | shared government domain: page or quote names the body | soft | 2 | REVIEW |
| 10 | regional token of a multinational on a differently-located body | soft | 0 | PASS |
| 11 | quote contains the address | hard | 0 | PASS |
| 11b | quote shows the label next to the address (referee saw the address on the page) | soft | 0 | PASS |
| 12 | evidence page on the organisation's domain (or its site) | soft | 16029 | REVIEW |
| 13 | email_type label matches grade | hard | 0 | PASS |
| 14 | DMARC / SPF / provider columns filled | soft | 0 | PASS |
| 15 | tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m) | soft | 4 | REVIEW |
| 16 | vendor named and Canada proof present | hard | 0 | PASS |
| 17 | Canada proof is a source field or the vendor's site (never a name) | soft | 0 | PASS |
| 18 | record link present for dated-record tiers | soft | 0 | PASS |
| 19 | buyer name is a name (not a domain or a page title) | soft | 34303 | REVIEW |
| 20 | legal name is not a fragment or a platform copyright | soft | 561 | REVIEW |
| 21 | one row per mailbox | hard | 0 | PASS |
| 22 | one row per organisation name (same name twice) | soft | 0 | PASS |
| 23 | one row per site domain (two rows, different mailboxes, same domain) | soft | 40 | REVIEW |
| 24 | no blank cell | hard | 0 | PASS |
| 25 | jurisdiction vs mailbox top-level domain | soft | 114 | REVIEW |
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
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:167 TAYLOR-LISTUG, INC. d/b/a TAYLOR GUITARS | ap_group@taylorguitars.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:344 TAE TECHNOLOGIES, INC. | ap_tps@tae.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:368 CENTERPOINT ENERGY, INC. | ap_helpdesk@centerpointenergy.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:7 Scouts de Dieppe | paiement@scoutsdedieppe.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:19 cvqvintage.ca | paiements@cvqvintage.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:32 Clic-Informatique | paiements@clic-informatique.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:112 Cameco Corporation | ap_cameco@cameco.com
    - P01_GOLD_active_relationship_invoicing_AP_email:278 University of Saskatchewan | connectionpoint@usask.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:280 Miami-Dade County (business unit CU05010 | invsubp@miamidade.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:295 Town of Oakville | ap_inquiries@oakville.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:380 BELL TEXTRON INC | APBell@textron.com
- **8 receivables-looking local part graded invoicing/AP**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:75 Calgary Coin Gallery | payment@calgarycoin.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:269 GUILD INSURANCE GROUP INC. | payment@guild.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:308 birchfumigators.ca | payment@birchfumigators.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:18 Flashing Canines Agility Club | payments@flashingcanines.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:36 McNamee & Kilpatrick | payments@mcnameekilpatrick.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:41 Stein Works | payments@steinworks.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:51 Penner Auctions | morden.payments@pennerauctions.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:59 Vocal Euphoria | payments@vocaleuphoria.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:61 ThePrintedCopy | payment@theprintedcopy.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:63 Awninginabox.ca | payment@awninginabox.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:105 Texas Tech University | payment.strategies@ttu.edu
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:169 PSM Law | payment@psmlaw.ca
- **9 shared government domain: page or quote names the body**
    - P01_GOLD_active_relationship_invoicing_AP_email:559 Tennessee Department of Transportation | pln.invoices@tn.gov ← https://www.tn.gov/tdot/long-range-planning-home/longrange-administration/longra
    - P07_client_listing_finance_or_purchasing_email:562 transportation.ky.gov | finance.crcgroup@ky.gov ← https://finance.ky.gov/eProcurement/Pages/doing-business-with-the-commonwealth.a
- **12 evidence page on the organisation's domain (or its site)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:24 ATTIS LEBLANC | payable@attis-leblanc.com on attis-leblanc.ca (site attis-leblanc.com)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:80 Oil City Drywall North | accounting@oilcitydrywall.ca on oilcitydrywallnorth.ca (site oilcitydrywall.ca)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:140 COCA-COLA LTD./ COCA-COLA LTEE | krinvoice@coca-cola.com on coca-colacompany.com (site coca-cola.com)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:173 The Mosaic Company | mosaic.accountspayable@mosaicco.com on mosaicincanada.com (site mosaicco.com)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:230 TRATON SE | invoices.to@se.traton.com on supplier.scania.com (site traton.com)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:367 SANDOZ INC. | comptes.payables@sandoz.com on sandoz.ca (site sandoz.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:19 cvqvintage.ca | paiements@cvqvintage.ca on coursesvintagequebec.ca (site cvqvintage.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:22 regieincendiekam-ouest.ca | payables@regieincendiekam-ouest.ca on regieincendiekam-ouest.com (site regieincendiekam-ouest.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:75 ibiosolutions.com | payables@ibiosolutions.com on immunebiosolutions.com (site ibiosolutions.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:114 Motorola Solutions, Inc | recepcionfacturas@motorolasolutions.com on web.archive.org (site motorolasolutions.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:160 dabc.ca | ap@dabc.ca on disabilityalliancebc.org (site dabc.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:2 Department of Defence | invoices@defence.gov.au on web.archive.org (site defence.gov.au)
- **15 tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m)**
    - P04_active_relationship_general_email_part1_of_2:8 Canadian Centre of Recovery Excellence | A with end 2026-11-12
    - P04_active_relationship_general_email_part1_of_2:69 Municipalité de Saint-Lambert-de-Lauzon | A with end 2026-11-12
    - P04_active_relationship_general_email_part1_of_2:173 Municipalité régionale de comté La Matap | A with end 2026-11-12
    - P04_active_relationship_general_email_part1_of_2:221 Centre de services scolaire des Hautes-L | A with end 2026-11-12
- **19 buyer name is a name (not a domain or a page title)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:308 birchfumigators.ca | birchfumigators.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:309 dfcdiesel.com | dfcdiesel.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:4 fs.ca | fs.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:19 cvqvintage.ca | cvqvintage.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:22 regieincendiekam-ouest.ca | regieincendiekam-ouest.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:31 nrgqc.com | nrgqc.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:33 it-desgens.ca | it-desgens.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:42 wasonlandscaping.com | wasonlandscaping.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:60 llanteralincoln.com | llanteralincoln.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:63 Awninginabox.ca | Awninginabox.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:74 ep.com | ep.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:75 ibiosolutions.com | ibiosolutions.com
- **20 legal name is not a fragment or a platform copyright**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:2 Braemed Ltd. | Braemed Ltd. (Health Canada's Medical Devices Establishment Licence li
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:15 ZIMMER INC. | ZIMMER INC. (Health Canada's Medical Devices Active Licence Listing (t
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:112 LIN-ZHI INTERNATIONAL, INC. | LIN-ZHI INTERNATIONAL, INC. (Health Canada's Medical Devices Active Li
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:117 VASCUTEK LIMITED | VASCUTEK LIMITED (Health Canada's Medical Devices Active Licence Listi
    - P04_active_relationship_general_email_part2_of_2:437 True Millwork | Introduction Welcome to True Millwork (stated on https://www.truemillw
    - P05_likely_active_awarded_12_36_months_any_email:62 Ameren Illinois Company | Ameren Corporation and/or its suppliers (the copyright line of https:/
    - P05_likely_active_awarded_12_36_months_any_email:215 LOVE WORTH FINDING MINISTRIES INC | LLC. 800-274-5683 2941 Kate Bond Rd, Memphis, TN 38133 CONNECT WITH LW
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part10_of_14:50 the airscreen company GmbH & Co. KG | the airscreen company GmbH & Co. KG (the Canadian trademarks register 
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part12_of_14:515 LITCO LAW IS A TRADEMARK AND TRADE NAME  | LITCO LAW IS A TRADEMARK AND TRADE NAME OF LITWINIUK LLP (the copyrigh
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part14_of_14:674 Dentaurum Canada Inc. | Dentaurum Canada Inc. (Health Canada's Medical Devices Establishment L
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part14_of_14:961 SEIGLA MEDICAL, INC. | SEIGLA MEDICAL, INC. (Health Canada's Medical Devices Active Licence L
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part14_of_14:1937 GRANICUS, LLC | GRANICUS, LLC (the Canadian trademarks register (owner of record), ext
- **23 one row per site domain (two rows, different mailboxes, same domain)**
    - P01_GOLD_active_relationship_invoicing_AP_email:2 Department of Defence | defence.gov.au: 2 rows, invoices@defence.gov.au; peppol.einvoices@defence.gov.au
    - P01_GOLD_active_relationship_invoicing_AP_email:37 Ville de Gatineau | gatineau.ca: 2 rows, gatineau.factures@gatineau.ca; idgatineau@gatineau.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:45 Ville de Montréal | montreal.ca: 2 rows, facture@montreal.ca; comptesapayer@montreal.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:57 Ville de Laval | laval.ca: 3 rows, comptespayables@laval.ca; lavaleconomique@laval.ca; info@laval.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:109 Texas Department of Insurance | texas.gov: 7 rows, invoices@tdi.texas.gov; payableteam@trs.texas.gov; ap@ers.texas.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:125 University of Ottawa | uottawa.ca: 2 rows, payables@uottawa.ca; info@emba.uottawa.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:182 Oregon Department of Transportation | oregon.gov: 3 rows, opoinvoiceinquiries@odot.oregon.gov; omdaccounts.payable@omd.oregon.gov; odf.accountspayable@oregon.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:183 Texas Tech University Health Sciences Ce | ttuhsc.edu: 2 rows, accountspayableelp@ttuhsc.edu; Accounts.Payable@ttuhsc.edu
    - P01_GOLD_active_relationship_invoicing_AP_email:269 Township of Scugog | scugog.ca: 2 rows, invoice@scugog.ca; mail@scugog.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:365 NATO Joint Warfare Centre (Stavanger) | nato.int: 3 rows, invoice@jwc.nato.int; accountspayable.mailbox@hq.nato.int; accountspayable@ncia.nato.int
    - P01_GOLD_active_relationship_invoicing_AP_email:374 Virginia Department of Energy | virginia.gov: 6 rows, accountspayable@energy.virginia.gov; ap@vsp.virginia.gov; support@dhrm.virginia.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:377 DELOITTE & TOUCHE LLP | deloitte.com: 2 rows, accountspayable@deloitte.be; financeservices@deloitte.com
- **25 jurisdiction vs mailbox top-level domain**
    - P01_GOLD_active_relationship_invoicing_AP_email:300 Utilities Kingston | CA / kingston.gov.uk
    - P13_inferred_relationship_no_record_own_email_part10_of_94:1982 julienphoto.fr | CA / julienphoto.fr
    - P13_inferred_relationship_no_record_own_email_part13_of_94:723 Alenti | ON / alenti.fr
    - P13_inferred_relationship_no_record_own_email_part13_of_94:2083 Immigrar Canada | QC / immigrar.fr
    - P13_inferred_relationship_no_record_own_email_part15_of_94:276 LS telcom | ON / lstelcom.fr
    - P13_inferred_relationship_no_record_own_email_part15_of_94:508 EnterOne Corporation | CA / enterone.co.uk
    - P13_inferred_relationship_no_record_own_email_part15_of_94:1192 SurePay | ON / surepay.co.uk
    - P13_inferred_relationship_no_record_own_email_part16_of_94:900 C. & E. Fein GmbH | ON / fein.de
    - P13_inferred_relationship_no_record_own_email_part16_of_94:1148 Denso | ON / denso.co.nz
    - P13_inferred_relationship_no_record_own_email_part17_of_94:1000 LA MAISON DES JEUNES DE PLESSISVILLE INC | QC / lycos.fr
    - P13_inferred_relationship_no_record_own_email_part17_of_94:1862 The Redeemed Christian Church of God Lov | SK / loveassembly.co.uk
    - P13_inferred_relationship_no_record_own_email_part1_of_94:160 Miele | ON / miele.de
- **26 currency filled when a value is filled**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:64 RENTON SCHOOL DISTRICT #403 | 332345.13 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:447 Rectorado de la Universitat de València | 12698.25 (source field: PayableAmount)
    - P01_GOLD_active_relationship_invoicing_AP_email:458 BELLEVUE, CITY OF | 35488873.2 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:460 UNIVERSITY PLACE SCHOOL DISTRICT #83 | 685477.9 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:466 BELLEVUE SCHOOL DISTRICT #405 | 5395.88 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:469 SNOQUALMIE VALLEY SCHOOL DISTRICT #410 | 23980.42 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:471 SHORELINE SCHOOL DISTRICT #412 | 919904.69 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:472 MARYLAND STADIUM AUTHORITY | 251569.05 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:501 University of North Dakota | 145.850 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:504 North Dakota State University | 35.000 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:525 BRINKS DE COLOMBIA S.A. | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:583 BANCOLOMBIA S.A. | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)

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
- P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email: 420
- P01T_active_service_seen_on_buyer_site_invoicing_AP_email: 206
- P01_GOLD_active_relationship_invoicing_AP_email: 657
- P02_active_relationship_finance_accounting_email: 486
- P03_active_relationship_purchasing_email: 275
- P04_active_relationship_general_email: 4816
- P05_likely_active_awarded_12_36_months_any_email: 428
- P06M_member_or_regulated_payer_of_canadian_body_other_email: 30514
- P06T_active_service_seen_on_buyer_site_other_email: 55144
- P06_client_listing_invoicing_AP_email: 249
- P07_client_listing_finance_or_purchasing_email: 780
- P08_client_listing_general_email: 29302
- P09_older_contract_or_payment_any_email: 278
- P10R_ca_domain_registration_contract_own_email: 0
- P10_linked_from_vendor_site_any_email: 2052
- P11_any_relationship_email_not_yet_confirmed: 1813
- P12_weaker_relationship_within_5_years_own_email: 10
- P13_inferred_relationship_no_record_own_email: 202744

## Field fill across all delivered rows (value present, not `not_published`)
- buyer_website: 330174 (100.0%)
- vendor_address: 328761 (99.6%)
- vendor_website: 306253 (92.8%)
- buyer_address: 300794 (91.1%)
- vendor_legal_name: 287394 (87.0%)
- vendor_phone: 266132 (80.6%)
- vendor_registry_id: 259660 (78.6%)
- buyer_logo_url: 258281 (78.2%)
- vendor_logo_url: 240030 (72.7%)
- buyer_phone: 197329 (59.8%)
- buyer_legal_name_as_published: 153541 (46.5%)
- vendor_incorporation_date: 147862 (44.8%)
- vendor_bn9: 141857 (43.0%)
- contract_link: 127430 (38.6%)
- award_date: 101546 (30.8%)
- vendor_neq: 81962 (24.8%)
- vendor_emails: 58617 (17.8%)
- buyer_bn_as_published: 40713 (12.3%)
- end_date: 22067 (6.7%)
- contract_value: 9462 (2.9%)
- payment_terms_as_published: 4884 (1.5%)
- ap_phone: 3128 (0.9%)
- po_required_as_published: 2652 (0.8%)
- invoice_mailing_address: 2340 (0.7%)
- invoicing_requirements: 2308 (0.7%)
- invoice_portal_url: 2191 (0.7%)
- ap_contact_name_as_published: 1144 (0.3%)

## Canada-proof families
- source field: 184480; other: 145694

## Buyer types
- organisation (type not stated in the record): 170740
- company (private sector): 62794
- company (private sector) (from the organisation's name / web domain): 47142
- non-profit / association / cultural body: 17073
- government ministry / agency: 8507
- municipality / local government (from the organisation's name / web domain): 4494
- non-profit / association / cultural body (from the organisation's name / web domain): 3750
- hospital / health authority: 3340
- utility / public corporation: 3237
- university / college: 1818
- municipality / local government: 1803
- transport / transit authority: 1178
- hospital / health authority (from the organisation's name / web domain): 904
- utility / public corporation (from the organisation's name / web domain): 616
- government ministry / agency (from the organisation's name / web domain): 592
- university / college (from the organisation's name / web domain): 586
- religious organisation (from the organisation's name / web domain): 410
- transport / transit authority (from the organisation's name / web domain): 339
- First Nation / Indigenous government: 305
- First Nation / Indigenous government (from the organisation's name / web domain): 239
- school board / school district: 205
- school board / school district (from the organisation's name / web domain): 32
- US government body (federal, state or local): 30
- library (from the organisation's name / web domain): 29
- US city / county / local government: 11

## DMARC posture of the delivered mailboxes
- no DMARC record: 135278
- v=DMARC1; p=none (monitor only, no enforcement): 128405
- p=quarantine: 44650
- p=reject: 21469
- invalid DMARC record: 250
- DNS lookup failed: 122
