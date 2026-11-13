# Deep audit — 320461 delivered rows in 18 packages (151 files), 2026-11-13

Result: **FAIL** — 11 hard checks, 17 soft checks; hard failures: 1. Every flagged row is listed in `audit_flags.csv` with its reasons.

| # | check | kind | rows flagged | verdict |
|---|---|---|---|---|
| 1 | header: identical columns in every file (106 since 2026-11-06) | hard | 1 | FAIL |
| 2 | mailbox syntax | hard | 0 | PASS |
| 3 | mailbox referee-confirmed (all but P11) | hard | 0 | PASS |
| 4 | mail server (MX or A) on the mailbox domain | hard | 0 | PASS |
| 4b | mail server not yet checked (row newer than the last DNS pass) | soft | 265714 | REVIEW |
| 5 | no webmail domain | hard | 0 | PASS |
| 6 | no person-like local part | hard | 0 | PASS |
| 7 | role word in the local part | soft | 26332 | REVIEW |
| 8 | receivables-looking local part graded invoicing/AP | soft | 72 | REVIEW |
| 9 | shared government domain: page or quote names the body | soft | 2 | REVIEW |
| 10 | regional token of a multinational on a differently-located body | soft | 0 | PASS |
| 11 | quote contains the address | hard | 0 | PASS |
| 11b | quote shows the label next to the address (referee saw the address on the page) | soft | 0 | PASS |
| 12 | evidence page on the organisation's domain (or its site) | soft | 15289 | REVIEW |
| 13 | email_type label matches grade | hard | 0 | PASS |
| 14 | DMARC / SPF / provider columns filled | soft | 0 | PASS |
| 15 | tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m) | soft | 4 | REVIEW |
| 16 | vendor named and Canada proof present | hard | 0 | PASS |
| 17 | Canada proof is a source field or the vendor's site (never a name) | soft | 0 | PASS |
| 18 | record link present for dated-record tiers | soft | 0 | PASS |
| 19 | buyer name is a name (not a domain or a page title) | soft | 33435 | REVIEW |
| 20 | legal name is not a fragment or a platform copyright | soft | 638 | REVIEW |
| 21 | one row per mailbox | hard | 0 | PASS |
| 22 | one row per organisation name (same name twice) | soft | 0 | PASS |
| 23 | one row per site domain (two rows, different mailboxes, same domain) | soft | 43 | REVIEW |
| 24 | no blank cell | hard | 0 | PASS |
| 25 | jurisdiction vs mailbox top-level domain | soft | 105 | REVIEW |
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
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:20 ATTIS LEBLANC | attis-leblanc.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:24 Cologix Canada inc. | cologix.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:26 Edmond Nolin Ltée | constructionenl.com
- **7 role word in the local part**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:3 Keyera Corp. | ap_inquiries@keyera.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:156 TAYLOR-LISTUG, INC. d/b/a TAYLOR GUITARS | ap_group@taylorguitars.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:309 TAE TECHNOLOGIES, INC. | ap_tps@tae.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:333 CENTERPOINT ENERGY, INC. | ap_helpdesk@centerpointenergy.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:7 Scouts de Dieppe | paiement@scoutsdedieppe.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:19 cvqvintage.ca | paiements@cvqvintage.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:32 Clic-Informatique | paiements@clic-informatique.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:115 Cameco Corporation | ap_cameco@cameco.com
    - P01_GOLD_active_relationship_invoicing_AP_email:275 University of Saskatchewan | connectionpoint@usask.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:277 Miami-Dade County (business unit CU05010 | invsubp@miamidade.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:291 Town of Oakville | ap_inquiries@oakville.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:378 BELL TEXTRON INC | APBell@textron.com
- **8 receivables-looking local part graded invoicing/AP**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:72 Calgary Coin Gallery | payment@calgarycoin.com
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:263 Empress | payments@villageofempress.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:273 birchfumigators.ca | payment@birchfumigators.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:18 Flashing Canines Agility Club | payments@flashingcanines.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:36 McNamee & Kilpatrick | payments@mcnameekilpatrick.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:41 Stein Works | payments@steinworks.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:51 Penner Auctions | morden.payments@pennerauctions.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:59 Vocal Euphoria | payments@vocaleuphoria.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:61 ThePrintedCopy | payment@theprintedcopy.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:63 Awninginabox.ca | payment@awninginabox.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:91 Nicol Insurance | payments@nicolinsurance.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:107 Texas Tech University | payment.strategies@ttu.edu
- **9 shared government domain: page or quote names the body**
    - P01_GOLD_active_relationship_invoicing_AP_email:557 Tennessee Department of Transportation | pln.invoices@tn.gov ← https://www.tn.gov/tdot/long-range-planning-home/longrange-administration/longra
    - P07_client_listing_finance_or_purchasing_email:568 transportation.ky.gov | finance.crcgroup@ky.gov ← https://finance.ky.gov/eProcurement/Pages/doing-business-with-the-commonwealth.a
- **12 evidence page on the organisation's domain (or its site)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:20 ATTIS LEBLANC | payable@attis-leblanc.com on attis-leblanc.ca (site attis-leblanc.com)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:77 Oil City Drywall North | accounting@oilcitydrywall.ca on oilcitydrywallnorth.ca (site oilcitydrywall.ca)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:129 COCA-COLA LTD./ COCA-COLA LTEE | krinvoice@coca-cola.com on coca-colacompany.com (site coca-cola.com)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:219 TRATON SE | invoices.to@se.traton.com on supplier.scania.com (site traton.com)
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:332 SANDOZ INC. | comptes.payables@sandoz.com on sandoz.ca (site sandoz.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:19 cvqvintage.ca | paiements@cvqvintage.ca on coursesvintagequebec.ca (site cvqvintage.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:22 regieincendiekam-ouest.ca | payables@regieincendiekam-ouest.ca on regieincendiekam-ouest.com (site regieincendiekam-ouest.ca)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:76 ibiosolutions.com | payables@ibiosolutions.com on immunebiosolutions.com (site ibiosolutions.com)
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:162 dabc.ca | ap@dabc.ca on disabilityalliancebc.org (site dabc.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:32 Natural Sciences and Engineering Researc | payables@nserc-crsng.gc.ca on nserc-crsng.canada.ca (site nserc-crsng.gc.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:45 Ville de Montréal | facture@montreal.ca on ville.montreal.qc.ca (site montreal.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:67 Ville de Farnham | comptespayables@ville.farnham.qc.ca on web.archive.org (site ville.farnham.qc.ca)
- **15 tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m)**
    - P04_active_relationship_general_email_part1_of_2:8 Canadian Centre of Recovery Excellence | A with end 2026-11-12
    - P04_active_relationship_general_email_part1_of_2:69 Municipalité de Saint-Lambert-de-Lauzon | A with end 2026-11-12
    - P04_active_relationship_general_email_part1_of_2:172 Municipalité régionale de comté La Matap | A with end 2026-11-12
    - P04_active_relationship_general_email_part1_of_2:221 Centre de services scolaire des Hautes-L | A with end 2026-11-12
- **19 buyer name is a name (not a domain or a page title)**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:273 birchfumigators.ca | birchfumigators.ca
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:274 dfcdiesel.com | dfcdiesel.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:4 fs.ca | fs.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:19 cvqvintage.ca | cvqvintage.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:22 regieincendiekam-ouest.ca | regieincendiekam-ouest.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:31 nrgqc.com | nrgqc.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:33 it-desgens.ca | it-desgens.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:42 wasonlandscaping.com | wasonlandscaping.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:60 llanteralincoln.com | llanteralincoln.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:63 Awninginabox.ca | Awninginabox.ca
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:70 efifoodequip.com | efifoodequip.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:75 ep.com | ep.com
- **20 legal name is not a fragment or a platform copyright**
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:2 Braemed Ltd. | Braemed Ltd. (Health Canada's Medical Devices Establishment Licence li
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:8 Myco Medical Supplies Inc. | Myco Medical Supplies Inc. (Health Canada's Medical Devices Establishm
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:15 ZIMMER INC. | ZIMMER INC. (Health Canada's Medical Devices Active Licence Listing (t
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:108 LIN-ZHI INTERNATIONAL, INC. | LIN-ZHI INTERNATIONAL, INC. (Health Canada's Medical Devices Active Li
    - P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email:113 VASCUTEK LIMITED | VASCUTEK LIMITED (Health Canada's Medical Devices Active Licence Listi
    - P04_active_relationship_general_email_part2_of_2:415 True Millwork | Introduction Welcome to True Millwork (stated on https://www.truemillw
    - P05_likely_active_awarded_12_36_months_any_email:61 Ameren Illinois Company | Ameren Corporation and/or its suppliers (the copyright line of https:/
    - P05_likely_active_awarded_12_36_months_any_email:216 LOVE WORTH FINDING MINISTRIES INC | LLC. 800-274-5683 2941 Kate Bond Rd, Memphis, TN 38133 CONNECT WITH LW
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part11_of_13:960 LITCO LAW IS A TRADEMARK AND TRADE NAME  | LITCO LAW IS A TRADEMARK AND TRADE NAME OF LITWINIUK LLP (the copyrigh
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part13_of_13:727 Dentaurum Canada Inc. | Dentaurum Canada Inc. (Health Canada's Medical Devices Establishment L
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part13_of_13:1013 SEIGLA MEDICAL, INC. | SEIGLA MEDICAL, INC. (Health Canada's Medical Devices Active Licence L
    - P06M_member_or_regulated_payer_of_canadian_body_other_email_part13_of_13:1984 GRANICUS, LLC | GRANICUS, LLC (the Canadian trademarks register (owner of record), ext
- **23 one row per site domain (two rows, different mailboxes, same domain)**
    - P01_GOLD_active_relationship_invoicing_AP_email:36 Ville de Gatineau | gatineau.ca: 2 rows, gatineau.factures@gatineau.ca; idgatineau@gatineau.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:45 Ville de Montréal | montreal.ca: 2 rows, facture@montreal.ca; comptesapayer@montreal.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:58 Ville de Laval | laval.ca: 3 rows, comptespayables@laval.ca; lavaleconomique@laval.ca; info@laval.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:110 Texas Department of Insurance | texas.gov: 7 rows, invoices@tdi.texas.gov; payableteam@trs.texas.gov; ap@ers.texas.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:125 University of Ottawa | uottawa.ca: 2 rows, payables@uottawa.ca; info@emba.uottawa.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:181 Oregon Department of Transportation | oregon.gov: 3 rows, opoinvoiceinquiries@odot.oregon.gov; omdaccounts.payable@omd.oregon.gov; odf.accountspayable@oregon.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:182 Texas Tech University Health Sciences Ce | ttuhsc.edu: 2 rows, accountspayableelp@ttuhsc.edu; accounts.payable@ttuhsc.edu
    - P01_GOLD_active_relationship_invoicing_AP_email:242 Newfoundland and Labrador Hydro | nlhydro.com: 2 rows, hydroapinvoices@nlh.nl.ca; NalcorAPInvoices@nalcorenergy.com
    - P01_GOLD_active_relationship_invoicing_AP_email:266 Township of Scugog | scugog.ca: 2 rows, invoice@scugog.ca; mail@scugog.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:363 NATO Joint Warfare Centre (Stavanger) | nato.int: 3 rows, invoice@jwc.nato.int; accountspayable.mailbox@hq.nato.int; accountspayable@ncia.nato.int
    - P01_GOLD_active_relationship_invoicing_AP_email:364 Commonwealth of Australia (Royal Austral | defence.gov.au: 2 rows, invoices@defence.gov.au; procurement.asdefcon@defence.gov.au
    - P01_GOLD_active_relationship_invoicing_AP_email:372 Virginia Department of Energy | virginia.gov: 6 rows, accountspayable@energy.virginia.gov; ap@vsp.virginia.gov; support@dhrm.virginia.gov
- **25 jurisdiction vs mailbox top-level domain**
    - P01_GOLD_active_relationship_invoicing_AP_email:295 Utilities Kingston | CA / kingston.gov.uk
    - P13_inferred_relationship_no_record_own_email_part10_of_90:1306 julienphoto.fr | CA / julienphoto.fr
    - P13_inferred_relationship_no_record_own_email_part12_of_90:2064 Alenti | ON / alenti.fr
    - P13_inferred_relationship_no_record_own_email_part13_of_90:1226 Immigrar Canada | QC / immigrar.fr
    - P13_inferred_relationship_no_record_own_email_part14_of_90:1414 LS telcom | ON / lstelcom.fr
    - P13_inferred_relationship_no_record_own_email_part15_of_90:165 SurePay | ON / surepay.co.uk
    - P13_inferred_relationship_no_record_own_email_part16_of_90:56 Denso | ON / denso.co.nz
    - P13_inferred_relationship_no_record_own_email_part16_of_90:2066 LA MAISON DES JEUNES DE PLESSISVILLE INC | QC / lycos.fr
    - P13_inferred_relationship_no_record_own_email_part17_of_90:765 The Redeemed Christian Church of God Lov | SK / loveassembly.co.uk
    - P13_inferred_relationship_no_record_own_email_part1_of_90:151 Miele | ON / miele.de
    - P13_inferred_relationship_no_record_own_email_part1_of_90:296 ONEJOON | QC / onejoon.de
    - P13_inferred_relationship_no_record_own_email_part1_of_90:1389 Mole Valley District Council | SK / molevalley.gov.uk
- **26 currency filled when a value is filled**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:64 RENTON SCHOOL DISTRICT #403 | 332345.13 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:446 Rectorado de la Universitat de València | 12698.25 (source field: PayableAmount)
    - P01_GOLD_active_relationship_invoicing_AP_email:457 BELLEVUE, CITY OF | 35488873.2 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:459 UNIVERSITY PLACE SCHOOL DISTRICT #83 | 685477.9 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:465 BELLEVUE SCHOOL DISTRICT #405 | 5395.88 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:468 SNOQUALMIE VALLEY SCHOOL DISTRICT #410 | 23980.42 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:470 SHORELINE SCHOOL DISTRICT #412 | 919904.69 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:471 MARYLAND STADIUM AUTHORITY | 251569.05 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:500 University of North Dakota | 145.850 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:503 North Dakota State University | 35.000 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:524 BRINKS DE COLOMBIA S.A. | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:582 BANCOLOMBIA S.A. | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)

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
- P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email: 377
- P01T_active_service_seen_on_buyer_site_invoicing_AP_email: 211
- P01_GOLD_active_relationship_invoicing_AP_email: 653
- P02_active_relationship_finance_accounting_email: 491
- P03_active_relationship_purchasing_email: 279
- P04_active_relationship_general_email: 4868
- P05_likely_active_awarded_12_36_months_any_email: 429
- P06M_member_or_regulated_payer_of_canadian_body_other_email: 28835
- P06T_active_service_seen_on_buyer_site_other_email: 55504
- P06_client_listing_invoicing_AP_email: 259
- P07_client_listing_finance_or_purchasing_email: 791
- P08_client_listing_general_email: 29605
- P09_older_contract_or_payment_any_email: 276
- P10R_ca_domain_registration_contract_own_email: 0
- P10_linked_from_vendor_site_any_email: 2080
- P11_any_relationship_email_not_yet_confirmed: 1799
- P12_weaker_relationship_within_5_years_own_email: 11
- P13_inferred_relationship_no_record_own_email: 193993

## Field fill across all delivered rows (value present, not `not_published`)
- buyer_website: 320461 (100.0%)
- vendor_address: 319036 (99.6%)
- vendor_website: 297902 (93.0%)
- buyer_address: 290667 (90.7%)
- vendor_legal_name: 278232 (86.8%)
- vendor_phone: 260278 (81.2%)
- vendor_registry_id: 252406 (78.8%)
- buyer_logo_url: 244281 (76.2%)
- vendor_logo_url: 234306 (73.1%)
- buyer_phone: 192236 (60.0%)
- buyer_legal_name_as_published: 148165 (46.2%)
- vendor_incorporation_date: 143931 (44.9%)
- vendor_bn9: 138068 (43.1%)
- contract_link: 126468 (39.5%)
- award_date: 100234 (31.3%)
- vendor_neq: 80571 (25.1%)
- vendor_emails: 57886 (18.1%)
- buyer_bn_as_published: 40600 (12.7%)
- end_date: 21053 (6.6%)
- contract_value: 9335 (2.9%)
- payment_terms_as_published: 4821 (1.5%)
- ap_phone: 3041 (0.9%)
- po_required_as_published: 2648 (0.8%)
- invoice_mailing_address: 2263 (0.7%)
- invoicing_requirements: 2243 (0.7%)
- invoice_portal_url: 2183 (0.7%)
- ap_contact_name_as_published: 1124 (0.4%)

## Canada-proof families
- source field: 182337; other: 138124

## Buyer types
- organisation (type not stated in the record): 165878
- company (private sector): 60889
- company (private sector) (from the organisation's name / web domain): 45623
- non-profit / association / cultural body: 16680
- government ministry / agency: 8275
- municipality / local government (from the organisation's name / web domain): 4138
- non-profit / association / cultural body (from the organisation's name / web domain): 3671
- hospital / health authority: 3274
- utility / public corporation: 3137
- municipality / local government: 1783
- university / college: 1765
- transport / transit authority: 1152
- hospital / health authority (from the organisation's name / web domain): 879
- utility / public corporation (from the organisation's name / web domain): 593
- government ministry / agency (from the organisation's name / web domain): 590
- university / college (from the organisation's name / web domain): 578
- religious organisation (from the organisation's name / web domain): 390
- transport / transit authority (from the organisation's name / web domain): 326
- First Nation / Indigenous government: 300
- First Nation / Indigenous government (from the organisation's name / web domain): 236
- school board / school district: 202
- school board / school district (from the organisation's name / web domain): 31
- US government body (federal, state or local): 31
- library (from the organisation's name / web domain): 29
- US city / county / local government: 11

## DMARC posture of the delivered mailboxes
- no DMARC record: 131062
- v=DMARC1; p=none (monitor only, no enforcement): 124713
- p=quarantine: 43432
- p=reject: 20896
- invalid DMARC record: 244
- DNS lookup failed: 114
