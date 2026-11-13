# Deep audit — 356279 delivered rows in 18 packages (169 files), 2026-11-13

Result: **FAIL** — 11 hard checks, 17 soft checks; hard failures: 2. Every flagged row is listed in `audit_flags.csv` with its reasons.

| # | check | kind | rows flagged | verdict |
|---|---|---|---|---|
| 1 | header: identical columns in every file (106 since 2026-11-06) | hard | 1 | FAIL |
| 2 | mailbox syntax | hard | 0 | PASS |
| 3 | mailbox referee-confirmed (all but P11) | hard | 0 | PASS |
| 4 | mail server (MX or A) on the mailbox domain | hard | 0 | PASS |
| 4b | mail server not yet checked (row newer than the last DNS pass) | soft | 300499 | REVIEW |
| 5 | no webmail domain | hard | 0 | PASS |
| 6 | no person-like local part | hard | 0 | PASS |
| 7 | role word in the local part | soft | 29960 | REVIEW |
| 8 | receivables-looking local part graded invoicing/AP | soft | 78 | REVIEW |
| 9 | shared government domain: page or quote names the body | soft | 2 | REVIEW |
| 10 | regional token of a multinational on a differently-located body | soft | 0 | PASS |
| 11 | quote contains the address | hard | 0 | PASS |
| 11b | quote shows the label next to the address (referee saw the address on the page) | soft | 0 | PASS |
| 12 | evidence page on the organisation's domain (or its site) | soft | 16998 | REVIEW |
| 13 | email_type label matches grade | hard | 0 | PASS |
| 14 | DMARC / SPF / provider columns filled | soft | 0 | PASS |
| 15 | tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m) | soft | 0 | PASS |
| 16 | vendor named and Canada proof present | hard | 65 | FAIL |
| 17 | Canada proof is a source field or the vendor's site (never a name) | soft | 0 | PASS |
| 18 | record link present for dated-record tiers | soft | 67 | REVIEW |
| 19 | buyer name is a name (not a domain or a page title) | soft | 38663 | REVIEW |
| 20 | legal name is not a fragment or a platform copyright | soft | 573 | REVIEW |
| 21 | one row per mailbox | hard | 0 | PASS |
| 22 | one row per organisation name (same name twice) | soft | 0 | PASS |
| 23 | one row per site domain (two rows, different mailboxes, same domain) | soft | 47 | REVIEW |
| 24 | no blank cell | hard | 0 | PASS |
| 25 | jurisdiction vs mailbox top-level domain | soft | 183 | REVIEW |
| 26 | currency filled when a value is filled | soft | 30 | REVIEW |

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
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:164 Taylor-Listug, Inc. | ap_group@taylorguitars.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:265 TAE TECHNOLOGIES, INC. | ap_tps@tae.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:289 CENTERPOINT ENERGY, INC. | ap_helpdesk@centerpointenergy.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:8 Scouts de Dieppe | paiement@scoutsdedieppe.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:20 cvqvintage.ca | paiements@cvqvintage.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:33 Clic-Informatique | paiements@clic-informatique.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:112 Cameco Corporation | ap_cameco@cameco.com
    - P01_GOLD_active_relationship_invoicing_AP_email:274 University of Saskatchewan | connectionpoint@usask.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:276 Miami-Dade County (business unit CU05010 | invsubp@miamidade.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:290 Town of Oakville | ap_inquiries@oakville.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:357 Institut national d'excellence en santé  | client@inesss.qc.ca
- **8 receivables-looking local part graded invoicing/AP**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:76 Calgary Coin Gallery | payment@calgarycoin.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:402 Empress | payments@villageofempress.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:413 birchfumigators.ca | payment@birchfumigators.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:420 Clean Exteriors Ltd. | payments@cleanexteriors.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:423 Twin City Tile Co. Ltd. | payments@twincitytile.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:424 elliottandassociates.ca | payments@elliottandassociates.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:425 Paradisus Window Cleaning & House Washin | payment@paradisuswindowcleaning.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:19 Flashing Canines Agility Club | payments@flashingcanines.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:37 McNamee & Kilpatrick | payments@mcnameekilpatrick.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:42 Stein Works | payments@steinworks.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:54 Penner Auctions | morden.payments@pennerauctions.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:61 Vocal Euphoria | payments@vocaleuphoria.com
- **9 shared government domain: page or quote names the body**
    - P01_GOLD_active_relationship_invoicing_AP_email:525 Tennessee Department of Transportation | pln.invoices@tn.gov ← https://www.tn.gov/tdot/long-range-planning-home/longrange-administration/longra
    - P07_client_listing_finance_or_purchasing_email:548 transportation.ky.gov | finance.crcgroup@ky.gov ← https://finance.ky.gov/eProcurement/Pages/doing-business-with-the-commonwealth.a
- **12 evidence page on the organisation's domain (or its site)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:22 Aluminerie Alouette Inc. | compteapayer@alouette.qc.ca on alouette.com (site alouette.qc.ca)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:25 ATTIS LEBLANC | payable@attis-leblanc.com on attis-leblanc.ca (site attis-leblanc.com)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:81 Oil City Drywall North | accounting@oilcitydrywall.ca on oilcitydrywallnorth.ca (site oilcitydrywall.ca)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:247 TRATON SE | invoices.to@se.traton.com on supplier.scania.com (site traton.com)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:288 SANDOZ INC. | comptes.payables@sandoz.com on sandoz.ca (site sandoz.com)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:393 National Veterinary Associates, Inc. | payables.canada@nva.com on nvacanada.ca (site nva.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:20 cvqvintage.ca | paiements@cvqvintage.ca on coursesvintagequebec.ca (site cvqvintage.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:23 regieincendiekam-ouest.ca | payables@regieincendiekam-ouest.ca on regieincendiekam-ouest.com (site regieincendiekam-ouest.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:75 ibiosolutions.com | payables@ibiosolutions.com on immunebiosolutions.com (site ibiosolutions.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:157 dabc.ca | ap@dabc.ca on disabilityalliancebc.org (site dabc.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:32 Natural Sciences and Engineering Researc | payables@nserc-crsng.gc.ca on nserc-crsng.canada.ca (site nserc-crsng.gc.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:45 Ville de Montréal | facture@montreal.ca on ville.montreal.qc.ca (site montreal.ca)
- **16 vendor named and Canada proof present**
    - P01_GOLD_active_relationship_invoicing_AP_email:627 GIW INDUSTRIES, INC.
    - P01_GOLD_active_relationship_invoicing_AP_email:630 The Kraft Heinz Company
    - P02_active_relationship_finance_accounting_email:408 Sherwin-Williams Paints, Stains, Supplie
    - P03_active_relationship_purchasing_email:221 multipleline.americannational.com
    - P03_active_relationship_purchasing_email:222 Elevance Health
    - P03_active_relationship_purchasing_email:223 American Family Insurance
    - P03_active_relationship_purchasing_email:224 DZYNE TECHNOLOGIES INCORPORATED
    - P03_active_relationship_purchasing_email:225 Quad/Graphics, Inc.
    - P03_active_relationship_purchasing_email:226 ultimatemedical.edu
    - P04_active_relationship_general_email_part1_of_2:2190 wildthymegroup.com
    - P04_active_relationship_general_email_part1_of_2:2191 Quisitive
    - P04_active_relationship_general_email_part1_of_2:2192 Get More with Kliken
- **18 record link present for dated-record tiers**
    - P01_GOLD_active_relationship_invoicing_AP_email:627 GIW INDUSTRIES, INC. | relationship record
    - P01_GOLD_active_relationship_invoicing_AP_email:630 The Kraft Heinz Company | relationship record
    - P02_active_relationship_finance_accounting_email:408 Sherwin-Williams Paints, Stains, Supplie | relationship record
    - P03_active_relationship_purchasing_email:221 multipleline.americannational.com | relationship record
    - P03_active_relationship_purchasing_email:222 Elevance Health | relationship record
    - P03_active_relationship_purchasing_email:223 American Family Insurance | relationship record
    - P03_active_relationship_purchasing_email:224 DZYNE TECHNOLOGIES INCORPORATED | relationship record
    - P03_active_relationship_purchasing_email:225 Quad/Graphics, Inc. | relationship record
    - P03_active_relationship_purchasing_email:226 ultimatemedical.edu | relationship record
    - P04_active_relationship_general_email_part1_of_2:2190 wildthymegroup.com | relationship record
    - P04_active_relationship_general_email_part1_of_2:2191 Quisitive | relationship record
    - P04_active_relationship_general_email_part1_of_2:2192 Get More with Kliken | relationship record
- **19 buyer name is a name (not a domain or a page title)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:413 birchfumigators.ca | birchfumigators.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:414 dfcdiesel.com | dfcdiesel.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:424 elliottandassociates.ca | elliottandassociates.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:426 ambroseplumbing.ca | ambroseplumbing.ca
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
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:109 LIN-ZHI INTERNATIONAL, INC. | LIN-ZHI INTERNATIONAL, INC. (Health Canada's Medical Devices Active Li
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:114 VASCUTEK LIMITED | VASCUTEK LIMITED (Health Canada's Medical Devices Active Licence Listi
    - P04_active_relationship_general_email_part2_of_2:478 True Millwork | Introduction Welcome to True Millwork (stated on https://www.truemillw
    - P05_likely_active_awarded_12_36_months_any_email:65 Ameren Illinois Company | Ameren Corporation and/or its suppliers (the copyright line of https:/
    - P05_likely_active_awarded_12_36_months_any_email:228 LOVE WORTH FINDING MINISTRIES INC | LLC. 800-274-5683 2941 Kate Bond Rd, Memphis, TN 38133 CONNECT WITH LW
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part10_of_15:35 the airscreen company GmbH & Co. KG | the airscreen company GmbH & Co. KG (the Canadian trademarks register 
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part14_of_15:496 LITCO LAW IS A TRADEMARK AND TRADE NAME  | LITCO LAW IS A TRADEMARK AND TRADE NAME OF LITWINIUK LLP (the copyrigh
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part15_of_15:1208 Dentaurum Canada Inc. | Dentaurum Canada Inc. (Health Canada's Medical Devices Establishment L
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part15_of_15:1244 SEIGLA MEDICAL, INC. | SEIGLA MEDICAL, INC. (Health Canada's Medical Devices Active Licence L
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part15_of_15:1875 GRANICUS, LLC | GRANICUS, LLC (the Canadian trademarks register (owner of record), ext
- **23 one row per site domain (two rows, different mailboxes, same domain)**
    - P01_GOLD_active_relationship_invoicing_AP_email:36 Ville de Gatineau | gatineau.ca: 2 rows, gatineau.factures@gatineau.ca; idgatineau@gatineau.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:43 Université de Montréal | umontreal.ca: 2 rows, comptesapayer@fin.umontreal.ca; pum@umontreal.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:45 Ville de Montréal | montreal.ca: 2 rows, facture@montreal.ca; comptesapayer@montreal.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:58 Ville de Laval | laval.ca: 3 rows, comptespayables@laval.ca; info@laval.ca; lavaleconomique@laval.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:109 Texas Department of Insurance | texas.gov: 7 rows, invoices@tdi.texas.gov; payableteam@trs.texas.gov; ap@ers.texas.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:112 University of Toronto | utoronto.ca: 2 rows, ap.fsd@utoronto.ca; vic.finance@utoronto.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:124 University of Ottawa | uottawa.ca: 2 rows, payables@uottawa.ca; info@emba.uottawa.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:181 Texas Tech University Health Sciences Ce | ttuhsc.edu: 2 rows, accountspayableelp@ttuhsc.edu; accounts.payable@ttuhsc.edu
    - P01_GOLD_active_relationship_invoicing_AP_email:206 Oregon Department of Transportation | oregon.gov: 3 rows, opoinvoiceinquiries@odot.oregon.gov; omdaccounts.payable@omd.oregon.gov; odf.accountspayable@oregon.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:241 Newfoundland and Labrador Hydro | nlhydro.com: 2 rows, hydroapinvoices@nlh.nl.ca; NalcorAPInvoices@nalcorenergy.com
    - P01_GOLD_active_relationship_invoicing_AP_email:265 Township of Scugog | scugog.ca: 2 rows, invoice@scugog.ca; mail@scugog.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:354 NATO Joint Warfare Centre (Stavanger) | nato.int: 3 rows, invoice@jwc.nato.int; accountspayable.mailbox@hq.nato.int; accountspayable@ncia.nato.int
- **25 jurisdiction vs mailbox top-level domain**
    - P01_GOLD_active_relationship_invoicing_AP_email:294 Utilities Kingston | CA / kingston.gov.uk
    - P13_inferred_relationship_no_record_own_email_part100_of_106:781 Pegasus Law Group Ltd. | ON / pegasuslaw.co.uk
    - P13_inferred_relationship_no_record_own_email_part100_of_106:1310 American Car Canada | QC / americancarcanada.fr
    - P13_inferred_relationship_no_record_own_email_part100_of_106:1685 SNACKSTER | ON / snackster-shop.de
    - P13_inferred_relationship_no_record_own_email_part100_of_106:2171 Annki | ON / annki-store.de
    - P13_inferred_relationship_no_record_own_email_part101_of_106:72 climbcs.co.uk | ON / climbcs.fr
    - P13_inferred_relationship_no_record_own_email_part101_of_106:211 GM PRO Talent Solutions | ON / gmprotalentsolutions.co.uk
    - P13_inferred_relationship_no_record_own_email_part101_of_106:563 Anthony Istar | QC / anthony-istar.fr
    - P13_inferred_relationship_no_record_own_email_part101_of_106:800 Exact Logistics | ON / exactlogistics.co.uk
    - P13_inferred_relationship_no_record_own_email_part101_of_106:1028 PSM Digital Agency Australia | ON / psmdigitalagency.com.au
    - P13_inferred_relationship_no_record_own_email_part101_of_106:1916 Capital Edge Church | ON / capitaledge.org.au
    - P13_inferred_relationship_no_record_own_email_part102_of_106:16 MSI60 | QC / msi60.fr
- **26 currency filled when a value is filled**
    - P01_GOLD_active_relationship_invoicing_AP_email:425 Rectorado de la Universitat de València | 12698.25 (source field: PayableAmount)
    - P01_GOLD_active_relationship_invoicing_AP_email:443 MARYLAND STADIUM AUTHORITY | 251569.05 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:465 University of North Dakota | 145.850 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:467 North Dakota State University | 35.000 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:491 BRINKS DE COLOMBIA S.A. | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:551 BANCOLOMBIA S.A. | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:559 ECOPETROL S A | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:612 Fundación para la Investigación del Hosp | 1236.23 (source field: PayableAmount)
    - P03_active_relationship_purchasing_email:175 CPS Energy | 21280.000000 (source field: purchase_amount)
    - P04_active_relationship_general_email_part1_of_2:977 Dirección General de la Fundación para l | 14000 (source field: PayableAmount)
    - P05_likely_active_awarded_12_36_months_any_email:30 Montgomery County Public Schools | 44824.88 (source field: amount)
    - P05_likely_active_awarded_12_36_months_any_email:31 Baltimore County Public Schools | 94850.00 (source field: amount)

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
- P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email: 435
- P01T_active_service_seen_on_buyer_site_invoicing_AP_email: 201
- P01_GOLD_active_relationship_invoicing_AP_email: 629
- P02_active_relationship_finance_accounting_email: 474
- P03_active_relationship_purchasing_email: 275
- P04_active_relationship_general_email: 4816
- P05_likely_active_awarded_12_36_months_any_email: 443
- P06M_member_or_regulated_payer_of_canadian_body_other_email: 32303
- P06T_active_service_seen_on_buyer_site_other_email: 53176
- P06_client_listing_invoicing_AP_email: 242
- P07_client_listing_finance_or_purchasing_email: 759
- P08_client_listing_general_email: 28712
- P09_older_contract_or_payment_any_email: 71
- P10R_ca_domain_registration_contract_own_email: 0
- P10_linked_from_vendor_site_any_email: 2004
- P11_any_relationship_email_not_yet_confirmed: 1809
- P12_weaker_relationship_within_5_years_own_email: 11
- P13_inferred_relationship_no_record_own_email: 229919

## Field fill across all delivered rows (value present, not `not_published`)
- buyer_website: 356279 (100.0%)
- vendor_address: 354818 (99.6%)
- vendor_website: 330671 (92.8%)
- buyer_address: 328087 (92.1%)
- vendor_legal_name: 307107 (86.2%)
- vendor_registry_id: 278146 (78.1%)
- vendor_phone: 276660 (77.7%)
- buyer_logo_url: 258201 (72.5%)
- vendor_logo_url: 251062 (70.5%)
- buyer_phone: 196817 (55.2%)
- buyer_legal_name_as_published: 163548 (45.9%)
- vendor_incorporation_date: 158753 (44.6%)
- vendor_bn9: 150855 (42.3%)
- contract_link: 126360 (35.5%)
- award_date: 100985 (28.3%)
- vendor_neq: 87777 (24.6%)
- vendor_emails: 58909 (16.5%)
- buyer_bn_as_published: 54554 (15.3%)
- end_date: 21857 (6.1%)
- contract_value: 9210 (2.6%)
- payment_terms_as_published: 6102 (1.7%)
- po_required_as_published: 3357 (0.9%)
- ap_phone: 3206 (0.9%)
- invoice_portal_url: 2479 (0.7%)
- invoicing_requirements: 2365 (0.7%)
- invoice_mailing_address: 2352 (0.7%)
- ap_contact_name_as_published: 1204 (0.3%)

## Canada-proof families
- source field: 199201; other: 157078

## Buyer types
- organisation (type not stated in the record): 183737
- company (private sector): 66973
- company (private sector) (from the organisation's name / web domain): 52698
- non-profit / association / cultural body: 18527
- government ministry / agency: 9088
- municipality / local government (from the organisation's name / web domain): 4600
- non-profit / association / cultural body (from the organisation's name / web domain): 3892
- hospital / health authority: 3568
- utility / public corporation: 3453
- university / college: 2009
- municipality / local government: 1871
- transport / transit authority: 1247
- hospital / health authority (from the organisation's name / web domain): 952
- utility / public corporation (from the organisation's name / web domain): 667
- government ministry / agency (from the organisation's name / web domain): 647
- university / college (from the organisation's name / web domain): 622
- religious organisation (from the organisation's name / web domain): 462
- transport / transit authority (from the organisation's name / web domain): 377
- First Nation / Indigenous government: 311
- First Nation / Indigenous government (from the organisation's name / web domain): 265
- school board / school district: 206
- school board / school district (from the organisation's name / web domain): 36
- US government body (federal, state or local): 31
- library (from the organisation's name / web domain): 29
- US city / county / local government: 11

## DMARC posture of the delivered mailboxes
- no DMARC record: 147713
- v=DMARC1; p=none (monitor only, no enforcement): 136888
- p=quarantine: 48070
- p=reject: 23185
- invalid DMARC record: 267
- DNS lookup failed: 156
