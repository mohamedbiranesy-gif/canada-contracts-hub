# Deep audit — 68907 delivered rows in 17 packages (37 files), 2026-11-10

Result: **FAIL** — 11 hard checks, 17 soft checks; hard failures: 1. Every flagged row is listed in `audit_flags.csv` with its reasons.

| # | check | kind | rows flagged | verdict |
|---|---|---|---|---|
| 1 | header: identical columns in every file (106 since 2026-11-06) | hard | 0 | PASS |
| 2 | mailbox syntax | hard | 0 | PASS |
| 3 | mailbox referee-confirmed (all but P11) | hard | 0 | PASS |
| 4 | mail server (MX or A) on the mailbox domain | hard | 0 | PASS |
| 4b | mail server not yet checked (row newer than the last DNS pass) | soft | 5092 | REVIEW |
| 5 | no webmail domain | hard | 1 | FAIL |
| 6 | no person-like local part | hard | 0 | PASS |
| 7 | role word in the local part | soft | 3945 | REVIEW |
| 8 | receivables-looking local part graded invoicing/AP | soft | 39 | REVIEW |
| 9 | shared government domain: page or quote names the body | soft | 3 | REVIEW |
| 10 | regional token of a multinational on a differently-located body | soft | 0 | PASS |
| 11 | quote contains the address | hard | 0 | PASS |
| 11b | quote shows the label next to the address (referee saw the address on the page) | soft | 0 | PASS |
| 12 | evidence page on the organisation's domain (or its site) | soft | 3817 | REVIEW |
| 13 | email_type label matches grade | hard | 0 | PASS |
| 14 | DMARC / SPF / provider columns filled | soft | 0 | PASS |
| 15 | tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m) | soft | 0 | PASS |
| 16 | vendor named and Canada proof present | hard | 0 | PASS |
| 17 | Canada proof is a source field or the vendor's site (never a name) | soft | 0 | PASS |
| 18 | record link present for dated-record tiers | soft | 0 | PASS |
| 19 | buyer name is a name (not a domain or a page title) | soft | 20599 | REVIEW |
| 20 | legal name is not a fragment or a platform copyright | soft | 64 | REVIEW |
| 21 | one row per mailbox | hard | 0 | PASS |
| 22 | one row per organisation name (same name twice) | soft | 9 | REVIEW |
| 23 | one row per site domain (two rows, different mailboxes, same domain) | soft | 63 | REVIEW |
| 24 | no blank cell | hard | 0 | PASS |
| 25 | jurisdiction vs mailbox top-level domain | soft | 41 | REVIEW |
| 26 | currency filled when a value is filled | soft | 46 | REVIEW |

## Examples of flagged rows (first 12 per check)
- **4b mail server not yet checked (row newer than the last DNS pass)**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:91 Cleveland State University | csu.ohio.edu
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:93 Calgary Coin Gallery | calgarycoin.com
    - P01_GOLD_active_relationship_invoicing_AP_email:161 Department of Homeland Security | dhs.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:224 BRITISH COUNCIL(THE) | sutton.gov.uk
    - P01_GOLD_active_relationship_invoicing_AP_email:237 BANK OF ENGLAND | bankofengland.co.uk
    - P01_GOLD_active_relationship_invoicing_AP_email:248 Utilities Kingston | kingston.gov.uk
    - P01_GOLD_active_relationship_invoicing_AP_email:370 NATO Joint Warfare Centre (Stavanger) | jwc.nato.int
    - P01_GOLD_active_relationship_invoicing_AP_email:404 Debiopharm International SA | debiopharm.com
    - P01_GOLD_active_relationship_invoicing_AP_email:426 Max-Planck-Gesellschaft zur Förderung de | gv.mpg.de
    - P01_GOLD_active_relationship_invoicing_AP_email:457 The Clorox Company of Canada Ltd. | uberfreight.com
    - P01_GOLD_active_relationship_invoicing_AP_email:496 New York State Energy Research and Devel | nyserda.ny.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:551 BANCOLOMBIA S.A. | bancolombia.com.co
- **5 no webmail domain**
    - P08_client_listing_general_email_part3_of_3:2061 Palmer College of Chiropractic | palmerfinancialaidmaincampus@live.palmer.edu
- **7 role word in the local part**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:16 Cameco Corporation | ap_cameco@cameco.com
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:43 New Relic | ap_ireland@newrelic.com
    - P01_GOLD_active_relationship_invoicing_AP_email:276 Town of Oakville | ap_inquiries@oakville.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:301 University of Saskatchewan | connectionpoint@usask.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:303 Miami-Dade County (business unit CU05010 | invsubp@miamidade.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:391 BELL TEXTRON INC | APBell@textron.com
    - P02_active_relationship_finance_accounting_email:7 Agriculture and Agri-Food Canada | directdeposit.depotdirect@canada.ca
    - P02_active_relationship_finance_accounting_email:13 Crown-Indigenous Relations and Northern  | depotdirect-directdeposit@sac-isc.gc.ca
    - P02_active_relationship_finance_accounting_email:14 Department of Justice Canada | mdv_dpf@justice.gc.ca
    - P02_active_relationship_finance_accounting_email:18 Health Canada | hc.direct.deposit.requests-demande.de.depot.direct.sc@canada.ca
    - P02_active_relationship_finance_accounting_email:19 Innovation, Science and Economic Develop | ifmscustomer-clientsifm@ised-isde.gc.ca
    - P02_active_relationship_finance_accounting_email:21 National Defence | ddenrol-inscriredd@forces.gc.ca
- **8 receivables-looking local part graded invoicing/AP**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:4 Texas Tech University | payment.strategies@ttu.edu
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:93 Calgary Coin Gallery | payment@calgarycoin.com
    - P01_GOLD_active_relationship_invoicing_AP_email:39 Environment and Climate Change Canada | renseignement-paiements-payments-inquiry@ec.gc.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:215 County of Minburn No. 27 | payments@minburncounty.ab.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:585 TMX Group Limited | payments@tmx.com
    - P05_likely_active_awarded_12_36_months_any_email:27 Martensville | payments@martensville.ca
    - P06_client_listing_invoicing_AP_email:28 University of Bath | payments@bath.ac.uk
    - P06_client_listing_invoicing_AP_email:70 TeamViewer | payments@teamviewer.com
    - P06_client_listing_invoicing_AP_email:149 Blomidon Nurseries (1970) Limited | payments@blomidonnurseries.com
    - P06_client_listing_invoicing_AP_email:185 bvca.ca | payments@bvca.ca
    - P06_client_listing_invoicing_AP_email:203 Lerners Lawyers | payments@lerners.ca
    - P06_client_listing_invoicing_AP_email:211 Sullivan Mahoney | payments@sullivanmahoney.com
- **9 shared government domain: page or quote names the body**
    - P01_GOLD_active_relationship_invoicing_AP_email:43 Canadian Space Agency | invoicing.csa-asc.facturation@canada.ca ← https://www.canada.ca/en/public-services-procurement/services/payments-to-from-g
    - P07_client_listing_finance_or_purchasing_email:25 transportation.ky.gov | finance.crcgroup@ky.gov ← https://finance.ky.gov/eProcurement/Pages/doing-business-with-the-commonwealth.a
    - P13_inferred_relationship_no_record_own_email_part1_of_18:499 Landlord and Tenant Board | ltbpayments@ontario.ca ← https://tribunalsontario.ca/ltb/contact/
- **12 evidence page on the organisation's domain (or its site)**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:18 Motorola Solutions | recepcionfacturas@motorolasolutions.com on web.archive.org (site motorolasolutions.com)
    - P01_GOLD_active_relationship_invoicing_AP_email:2 Department of Defence | invoices@defence.gov.au on web.archive.org (site defence.gov.au)
    - P01_GOLD_active_relationship_invoicing_AP_email:3 Department of Industry, Science and Reso | einvoicingqueries@industry.gov.au on directory.peppol.eu (site industry.gov.au)
    - P01_GOLD_active_relationship_invoicing_AP_email:51 Natural Sciences and Engineering Researc | payables@nserc-crsng.gc.ca on nserc-crsng.canada.ca (site nserc-crsng.gc.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:66 Ville de Montréal | facture@montreal.ca on ville.montreal.qc.ca (site montreal.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:95 Ville de Farnham | comptespayables@ville.farnham.qc.ca on web.archive.org (site ville.farnham.qc.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:114 UK Atomic Energy Authority | finance@uk-atomic-energy.org.uk on assets.publishing.service.gov.uk (site gov.uk)
    - P01_GOLD_active_relationship_invoicing_AP_email:126 City of Chestermere | city.ap@chestermere.ca on thecityofchestermere.ca (site chestermere.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:132 Newfoundland and Labrador Liquor Corpora | Accounts.Payable@nlliquor.com on nlliquorcorp.com (site nlliquor.com)
    - P01_GOLD_active_relationship_invoicing_AP_email:134 The Ottawa Hospital | tohaccountspayable@toh.ca on ottawahospital.on.ca (site toh.ca)
    - P01_GOLD_active_relationship_invoicing_AP_email:162 Department of Foreign Affairs and Trade | dfat.e-invoicing.prod@dfat.gov.au on directory.peppol.eu (site dfat.gov.au)
    - P01_GOLD_active_relationship_invoicing_AP_email:192 HM Land Registry | apinvoices@landregistry.gov.uk on assets.publishing.service.gov.uk (site gov.uk)
- **19 buyer name is a name (not a domain or a page title)**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:33 ovs.com | ovs.com
    - P01_GOLD_active_relationship_invoicing_AP_email:554 bcib.ca | bcib.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:625 corporate.exxonmobil.com | corporate.exxonmobil.com
    - P02_active_relationship_finance_accounting_email:389 OneChurch.To | OneChurch.To
    - P04_active_relationship_general_email:946 theonn.ca | theonn.ca
    - P04_active_relationship_general_email:947 cipf.ca | cipf.ca
    - P04_active_relationship_general_email:982 cpha.ca | cpha.ca
    - P04_active_relationship_general_email:1065 mhrc-rsmc.ca | mhrc-rsmc.ca
    - P04_active_relationship_general_email:1528 coalitionhumanitaire.ca | coalitionhumanitaire.ca
    - P04_active_relationship_general_email:1570 energy.ca.gov | energy.ca.gov
    - P06T_active_service_seen_on_buyer_site_other_email_part1_of_2:432 Bloom.wine | Bloom.wine
    - P06T_active_service_seen_on_buyer_site_other_email_part1_of_2:489 realtyprinting.ca | realtyprinting.ca
- **20 legal name is not a fragment or a platform copyright**
    - P03_active_relationship_purchasing_email:196 onsemi | onsemi (label per Wikidata Q1671509, official website on the organisat
    - P04_active_relationship_general_email:111 Ministère de la Culture et des Communica | ministère de la Culture et des Communications (label per Wikidata Q331
    - P04_active_relationship_general_email:156 Ministère de la Cybersécurité et du Numé | ministère de la Cybersécurité et du Numérique (label per Wikidata Q110
    - P06T_active_service_seen_on_buyer_site_other_email_part1_of_2:385 Uppdoo | uppdoo Inc. (as registered: Corporations Canada (open data), corporati
    - P06T_active_service_seen_on_buyer_site_other_email_part1_of_2:1080 MyHealth Inc | myhealth inc. (as registered: Canada's Business Registries, CC 3660222
    - P06T_active_service_seen_on_buyer_site_other_email_part1_of_2:1250 do+dare undie co. | do+dare undie co. (label per Wikidata Q141143888, official website on 
    - P06T_active_service_seen_on_buyer_site_other_email_part1_of_2:1413 de Montigny Contemporain | de Montigny Contemporain (label per Wikidata Q139820434, official webs
    - P07_client_listing_finance_or_purchasing_email:84 Lepointdevente.com | lepointdevente.com (recipient legal name in the federal grants & contr
    - P08_client_listing_general_email_part1_of_3:2106 Christian Life Community | Christian Life Community (stated on https://www.christianlifecommunity
    - P08_client_listing_general_email_part2_of_3:948 few-cycle | few-cycle Inc. (as registered: Canada's Business Registries, CC 867257
    - P08_client_listing_general_email_part2_of_3:2101 Mackinaw danse | compagnie de danse Mackinaw (label per Wikidata Q105064449, official w
    - P10_linked_from_vendor_site_any_email:1485 Digify SEO Company | digify seo company Incorporated (as registered: Corporations Canada (o
- **22 one row per organisation name (same name twice)**
    - P01_GOLD_active_relationship_invoicing_AP_email:26 University of Lethbridge | 2 rows, same mail domain: uleth.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:155 MRC de Manicouagan | 2 rows, same mail domain: mrcmanicouagan.qc.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:234 Metrolinx | 2 rows, same mail domain: metrolinx.com
    - P01_GOLD_active_relationship_invoicing_AP_email:439 City of Kamloops | 2 rows, same mail domain: kamloops.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:553 Enbridge Inc. | 2 rows, same mail domain: enbridge.com
    - P04_active_relationship_general_email:321 Cégep de Victoriaville. | 2 rows, same mail domain: cegepvicto.ca
    - P05_likely_active_awarded_12_36_months_any_email:5 Brandon University | 2 rows, same mail domain: brandonu.ca
    - P06T_active_service_seen_on_buyer_site_other_email_part2_of_2:400 Town of Lincoln | 2 rows, same mail domain: lincoln.ca
    - P08_client_listing_general_email_part1_of_3:422 Calcul Québec | 2 rows, same mail domain: calculquebec.ca
- **23 one row per site domain (two rows, different mailboxes, same domain)**
    - P01_GOLD_active_relationship_invoicing_AP_email:2 Department of Defence | defence.gov.au: 2 rows, invoices@defence.gov.au; peppol.einvoices@defence.gov.au
    - P01_GOLD_active_relationship_invoicing_AP_email:27 University of Toronto | utoronto.ca: 2 rows, ap.fsd@utoronto.ca; fmdinvoice.utsc@utoronto.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:57 Ville de Gatineau | gatineau.ca: 2 rows, gatineau.factures@gatineau.ca; idgatineau@gatineau.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:66 Ville de Montréal | montreal.ca: 2 rows, facture@montreal.ca; comptesapayer@montreal.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:82 Ville de Laval | laval.ca: 3 rows, comptespayables@laval.ca; lavaleconomique@laval.ca; info@laval.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:115 Texas Department of Insurance | texas.gov: 7 rows, invoices@tdi.texas.gov; ap@ers.texas.gov; ap@tsl.texas.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:128 University of Ottawa | uottawa.ca: 2 rows, payables@uottawa.ca; info@emba.uottawa.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:195 Oregon Department of Transportation | oregon.gov: 3 rows, opoinvoiceinquiries@odot.oregon.gov; omdaccounts.payable@omd.oregon.gov; odf.accountspayable@oregon.gov
    - P01_GOLD_active_relationship_invoicing_AP_email:198 Texas Tech University Health Sciences Ce | ttuhsc.edu: 2 rows, Accounts.Payable@ttuhsc.edu; accountspayableelp@ttuhsc.edu
    - P01_GOLD_active_relationship_invoicing_AP_email:234 Metrolinx | metrolinx.com: 2 rows, it.invoices@metrolinx.com; rti.invoices@metrolinx.com
    - P01_GOLD_active_relationship_invoicing_AP_email:259 Niagara Region | niagararegion.ca: 2 rows, constructioninvoices@niagararegion.ca; NRHCapitalWorks@niagararegion.ca
    - P01_GOLD_active_relationship_invoicing_AP_email:355 Virginia State Police | virginia.gov: 5 rows, ap@vsp.virginia.gov; accountspayable@energy.virginia.gov; support@dhrm.virginia.gov
- **25 jurisdiction vs mailbox top-level domain**
    - P01_GOLD_active_relationship_invoicing_AP_email:248 Utilities Kingston | CA / kingston.gov.uk
    - P13_inferred_relationship_no_record_own_email_part10_of_18:2701 AO Kaspersky Lab | CA / kaspersky.de
    - P13_inferred_relationship_no_record_own_email_part11_of_18:1005 lifelyhome.ca | CA / lifely.com.au
    - P13_inferred_relationship_no_record_own_email_part12_of_18:209 nakie.ca | CA / nakie.com.au
    - P13_inferred_relationship_no_record_own_email_part12_of_18:1205 opal-canada.ca | CA / opal.fr
    - P13_inferred_relationship_no_record_own_email_part12_of_18:1734 pccarx.ca | CA / pccarx.com.au
    - P13_inferred_relationship_no_record_own_email_part12_of_18:2385 practs.ca | CA / practs.de
    - P13_inferred_relationship_no_record_own_email_part13_of_18:820 Roka Harness Pty Ltd | CA / rokaharness.com.au
    - P13_inferred_relationship_no_record_own_email_part13_of_18:1971 Skin Cupid | CA / skincupid.co.uk
    - P13_inferred_relationship_no_record_own_email_part13_of_18:2165 Snowdonia Cheese Ltd | CA / snowdonia-cheese.co.uk
    - P13_inferred_relationship_no_record_own_email_part17_of_18:52 Beckhoff Automation Ltd. | CA / beckhoff.de
    - P13_inferred_relationship_no_record_own_email_part17_of_18:1057 Bernafon Canada | ON / bernafon.com.au
- **26 currency filled when a value is filled**
    - P01T_active_service_seen_on_buyer_site_invoicing_AP_email:23 RENTON SCHOOL DISTRICT #403 | 332345.13 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:443 Rectorado de la Universitat de València | 12698.25 (source field: PayableAmount)
    - P01_GOLD_active_relationship_invoicing_AP_email:455 BRINKS DE COLOMBIA S.A. | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:474 University of North Dakota | 145.850 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:503 BELLEVUE, CITY OF | 35488873.2 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:511 UNIVERSITY PLACE SCHOOL DISTRICT #83 | 685477.9 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:530 North Dakota State University | 35.000 (source field: Amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:535 BELLEVUE SCHOOL DISTRICT #405 | 5395.88 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:541 SNOQUALMIE VALLEY SCHOOL DISTRICT #410 | 23980.42 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:548 MARYLAND STADIUM AUTHORITY | 251569.05 (source field: amount)
    - P01_GOLD_active_relationship_invoicing_AP_email:551 BANCOLOMBIA S.A. | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)
    - P01_GOLD_active_relationship_invoicing_AP_email:562 ECOPETROL S A | 0 (source field: TOTAL_LIQUIDADO_ARANCEL)

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
- P01T_active_service_seen_on_buyer_site_invoicing_AP_email: 93
- P01_GOLD_active_relationship_invoicing_AP_email: 625
- P02_active_relationship_finance_accounting_email: 403
- P03_active_relationship_purchasing_email: 209
- P04_active_relationship_general_email: 1570
- P05_likely_active_awarded_12_36_months_any_email: 386
- P06M_member_or_regulated_payer_of_canadian_body_other_email: 168
- P06T_active_service_seen_on_buyer_site_other_email: 2983
- P06_client_listing_invoicing_AP_email: 227
- P07_client_listing_finance_or_purchasing_email: 449
- P08_client_listing_general_email: 8926
- P09_older_contract_or_payment_any_email: 383
- P10_linked_from_vendor_site_any_email: 2874
- P11_any_relationship_email_not_yet_confirmed: 607
- P12_weaker_relationship_within_5_years_own_email: 18
- P13_inferred_relationship_no_record_own_email: 48968

## Field fill across all delivered rows (value present, not `not_published`)
- buyer_website: 68907 (100.0%)
- vendor_website: 67225 (97.6%)
- vendor_address: 66444 (96.4%)
- vendor_phone: 57297 (83.2%)
- buyer_address: 54400 (78.9%)
- buyer_logo_url: 54184 (78.6%)
- vendor_logo_url: 53620 (77.8%)
- vendor_bn9: 51841 (75.2%)
- buyer_phone: 49964 (72.5%)
- buyer_legal_name_as_published: 33772 (49.0%)
- contract_link: 19939 (28.9%)
- buyer_bn_as_published: 15456 (22.4%)
- vendor_legal_name: 11186 (16.2%)
- vendor_registry_id: 8886 (12.9%)
- vendor_incorporation_date: 8860 (12.9%)
- award_date: 7051 (10.2%)
- vendor_emails: 6989 (10.1%)
- vendor_neq: 5555 (8.1%)
- ap_phone: 2705 (3.9%)
- contract_value: 2379 (3.5%)
- invoice_mailing_address: 2236 (3.2%)
- invoicing_requirements: 2147 (3.1%)
- payment_terms_as_published: 2051 (3.0%)
- end_date: 1771 (2.6%)
- invoice_portal_url: 1766 (2.6%)
- po_required_as_published: 1496 (2.2%)
- ap_contact_name_as_published: 938 (1.4%)

## Canada-proof families
- other: 45589; source field: 23318

## Buyer types
- organisation (type not stated in the record): 36543
- company (private sector): 11184
- non-profit / association / cultural body: 7516
- company (private sector) (from the organisation's name / web domain): 4756
- government ministry / agency: 1377
- municipality / local government: 1351
- municipality / local government (from the organisation's name / web domain): 1082
- hospital / health authority: 977
- non-profit / association / cultural body (from the organisation's name / web domain): 972
- university / college: 609
- utility / public corporation: 555
- university / college (from the organisation's name / web domain): 457
- hospital / health authority (from the organisation's name / web domain): 354
- transport / transit authority: 216
- school board / school district: 178
- First Nation / Indigenous government: 169
- government ministry / agency (from the organisation's name / web domain): 159
- religious organisation (from the organisation's name / web domain): 148
- utility / public corporation (from the organisation's name / web domain): 109
- transport / transit authority (from the organisation's name / web domain): 62
- First Nation / Indigenous government (from the organisation's name / web domain): 53
- US government body (federal, state or local): 29
- school board / school district (from the organisation's name / web domain): 22
- library (from the organisation's name / web domain): 18
- US city / county / local government: 11

## DMARC posture of the delivered mailboxes
- v=DMARC1; p=none (monitor only, no enforcement): 28732
- no DMARC record: 22876
- p=quarantine: 11300
- p=reject: 5899
- invalid DMARC record: 65
- DNS lookup failed: 35
