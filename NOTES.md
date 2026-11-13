# NOTES.md — lane `claude` research notes (started 2026-11-13 00:41Z)
## Hypothesis tree — Q: can 1,000,000 ready rows be reached under rules 1-17?
- H1 Yes, from Canadian organisations alone (by location + records). Against: ~1.4M Canadian organisation sites, ~500k with a role mailbox
  and a printed address (estimate; the reader finds a mailbox on 19 % of sites read). Confidence 10 %.
- H2 Yes, Canada (~550k) + organisations abroad tied by a record (~450k). For: trademark owners abroad 134,458 and patent owners abroad
  77,385 on file; certification bodies certify tens of thousands abroad (CSA Group, CWB). Against: website + mailbox conversion abroad
  ~25-45 %. Confidence 35 %.
- H3 Only with a rule decision (vendor client lists as labelled rows, +~30k; more if wider). Confidence 30 %.
- H4 Not reachable by end of November at the current growth (+~10-15k ready a day this week). Confidence 50 % — depends on H2's pools.
## Source table (claim | source | URL | accessed | quote | independent)
| Colombian import lines name the exporter's invoice and form of payment | DIAN microdata 2026-08 | https://www.dian.gov.co/dian/cifras/Basesestadisticasimportaciones/08_Importaciones_2026_Agosto.zip | 2026-11-12 | fields NUMERO_FACTURA, FECHA_FACTURA, FORMA_PAGO ("Giro directo") | yes |
| Sun Life Assurance Company of Canada insures 3,873 US employers' plans (2024 filings) | DOL Form 5500 Schedule A 2024 | https://askebsa.dol.gov/FOIA%20Files/2024/All/F_SCH_A_2024_All.zip | 2026-11-12 | INS_CARRIER_NAME, NAIC 80802 (counted) | yes |
| Sun Life's head office | Sun Life contact page | https://www.sunlife.com/en/contact-us/ | 2026-11-12 | "Our corporate head office is located at: 1 York Street Toronto, Ontario M5J 0B6 Canada" | primary |
| EDC buyer-financing rows 2025-2026: 87 | EDC individual transactions | https://www.edc.ca/en/about-us/corporate/disclosure/reporting-transactions/individual-transaction-information.html | 2026-11-12 | data-results-count="87" (filter Buyer Financing) | yes |
| Vancouver non-residential permits with a contractor, 12 months: 600 | City of Vancouver open data | https://opendata.vancouver.ca/ (issued-building-permits) | 2026-11-12 | total_count 600 | yes |
| PCAOB auditor search refused the reader | pcaobus.org | https://pcaobus.org/resources/auditorsearch | 2026-11-12 | HTTP 403 | — |
## Established / likely / unknown (as of 2026-11-13 00:41Z)
Established: 217,145 ready (build 22:02Z); 921,843 leads on file; pools counted above. Likely: +1-3k rows from the new lanes within a week.
Unknown: conversion abroad at scale; whether CSA Group's directory can be read from a runner.

## Mapping pass 2026-11-13 00:50Z (searches run; what each found)
| Ontario cannabis stores must buy from OCS, invoiced, paid by PAD | OCS Wholesale handbook Feb 2026 | https://learn.ocswholesale.ca/wp-content/uploads/2026/02/OCS-Wholesale-Authorized-Cannabis-Retailers-Handbook-February2026.pdf | 2026-11-13 | "Authorized Retailers of cannabis in Ontario may only purchase legal cannabis products through OCS Wholesale." | primary |
| 1,913 Ontario stores 'Authorized to Open' (2,679 records) | AGCO open data CSV | https://www.agco.ca/sites/default/files/opendata/AGCOWebSiteCRSANewProcessMapData.csv | 2026-11-13 | ApplicationStatusEn counts (counted) | primary |
| Service Alberta licensees list (Excel after a search form) | open.alberta.ca | https://open.alberta.ca/opendata/1b6cb20b-5d1d-443d-8e04-28558e9277f3 | 2026-11-13 | "A listing of all businesses, charities and fundraisers that hold an active licence or registration issued by Service Alberta" | primary |
| CWB directory is an antibot form | cwbgroup.org | https://www.cwbgroup.org/directory/certified-companies | 2026-11-13 | form action="/antibot" | blocked |
| No open import microdata with importer names found for Peru, Ecuador, Paraguay (only resellers such as Datasur) | searches | — | 2026-11-13 | — | unknown |
Hypothesis update: exclusive provincial wholesalers (cannabis: OCS, BC Cannabis Wholesale, AGLC, MBLL; liquor boards for licensees) give a
by-law, invoiced, bank-paid relationship for every licensed retailer — a new family of pools (~4,000 stores in Canada for cannabis alone).

## Mapping pass 2 (2026-11-13 01:17Z) — exclusive provincial wholesalers and regulators' firm registers
| B.C. stores: the LDB is "the sole wholesale distributor of non-medical cannabis throughout the province" | BC Cannabis Wholesale | https://www.bccannabiswholesale.com/pages/doing-business-with-bc-cannabis-wholesale | 2026-11-13 | quoted | primary |
| B.C. PAD agreement: "I authorize, the biller to withdraw funds from the bank account …"; "will provide a list of all invoices for goods ordered" | LDB PAD agreement | https://cdn.shopify.com/s/files/1/0007/0267/8860/files/LDB_Cannabis_Wholesale_PAD_Agreement_Final_Nov-2022.pdf | 2026-11-13 | quoted | primary |
| B.C. list: 563 licensed cannabis stores (Excel; no websites) — 133 stores' own sites found by postal code -> roster dl_bccw_bc (+72 leads) | gov.bc.ca | https://www2.gov.bc.ca/assets/gov/employment-business-and-economic-development/business-management/liquor-regulation-licensing/reports/cannabis_retail_stores_in_bc.xlsx | 2026-11-13 | counted | primary |
| Ontario roster dl_ocs_ontario: 1,265 stores taken, +348 leads (chains once) | AGCO CSV + OCS handbook | (above) | 2026-11-13 | counted | primary |
| Alberta: "AGLC is the only source of recreational cannabis products for private retailers in Alberta."; invoice by e-mail per order; PAD / bill payment | AGLC Cannabis Retailer Operations Manual 2024-09-05 | https://aglc.ca/sites/aglc.ca/files/forms/Cannabis_Retailer_Operations_Manual_20240905.pdf | 2026-11-13 | quoted | primary — but AGLC's licensee report pages are robots-disallowed: no list read |
| Manitoba: private distributors since 2022 (Delta 9, Fire & Flower) — MBLL not the sole wholesaler: no row | Benzinga 2022 | https://benzinga.com/markets/cannabis/22/04/26633511/delta-9-fire-flower-enter-into-separate-agreements-with-manitoba-to-become-cannabis-distributors | 2026-11-13 | — | secondary |
| LCBO wholesale: grocery / convenience default "is to pay by credit card when orders are placed" — card: no row (rule 6); invoice + 30-day terms only for customers buying $1M+ a year | LCBO Tender Type Operational Policy June 2026 | https://www.doingbusinesswithlcbo.com/content/dam/dbwl/wholesale/ordering/LCBO%20-%20Tender%20Type%20Operational%20Policy%20-%20June%202026.pdf | 2026-11-13 | quoted | primary |
| AGCO open data also lists 8,334 grocery / convenience liquor licences and 24,700 liquor sales licences (legal entity, premises, address) — no billing relationship on invoice found yet (LCBO card default) | AGCO data inventory | https://www.agco.ca/en/general/data-inventory | 2026-11-13 | counted | primary |
Next family (to map): regulators' public registers of FIRMS that pay yearly fees (PEO certificates of authorization, OAA practices, CPA firms,
OCP pharmacies, CVO accredited facilities, RECO brokerages, FSRA mortgage brokerages, RIBO firms, TICO, TSSA, RHRA, CMRAO) — each a
"licence or registration" row and a source of verified Canadian organisation sites; check robots and bulk access register by register.
| Standards Council of Canada accredited organisations: robots.txt names ClaudeBot (training crawlers) and the page answers 403 — not read | scc-ccn.ca | https://scc-ccn.ca/search/accredited-organizations | 2026-11-13 | HTTP 403 | blocked |
| tm-sites / pt-sites: +0 sites this run — every owner already looked for (144,583 trademark owners, 13,853 sites; 38,630 patent owners, 3,069 sites): the finders are exhausted with their methods | tm-sites / pt-sites runs | commits 23acdb4, f96a2d4 | 2026-11-13 | counted | primary |
| rank build 00:56Z failed (IndexError at the new contract-buyers-without-website list: a buyer with no key) — fixed and re-dispatched | rank-buyers run 43341013827 | — | 2026-11-13 | log | primary |

## Mapping pass 3 (2026-11-13 02:30Z) — owners' sites by address, SECOP websites, estimates from published totals
| Owners abroad with an Overture place at their own street address (ZIP + number + street; UK postcode) that lists a website: 13,115 trademark owners, 9,730 patent owners | tools/overture_names.py addr over Overture release 2026-10-21.0 (1,917,418 place rows at owners' addresses) | https://overturemaps-us-west-2.s3.amazonaws.com | 2026-11-13 | counted | primary (open data) |
| Runs with them: patent sites 3,069 -> 6,490 (+3,421: 1,756 by address, 1,689 by name); trademark 13,853 -> 14,351 (+498) | pt-sites / tm-sites runs of 01:42Z | commits 077e6e4, 268db76 | 2026-11-13 | counted | primary |
| Trademark owners left are mostly subsidiaries whose group site prints the group's name (PetSmart Home Office LLC / petsmart.com; Merck Sharp & Dohme LLC / merck.com; PPG Industries Ohio / ppg.com) | 60-owner test | — | 2026-11-13 | read | — |
| OCS 2024-25: "Wholesale revenue, excluding Data Subscription Fees, was $1,733.8 million in 2024–25"; "As of March 31, 2025, the total number of stores reached 1,719 … compared to 1,709" | OCS 2024-2025 Annual Report | https://www.doingbusinesswithocs.ca/wp-content/uploads/2026/02/OCS-2024-2025-Annual-Report.pdf | 2026-11-13 | quoted (pdftotext) | primary |
| B.C. LDB 2025/26: cannabis revenue $607.5 million, 551 licensed locations; no split between its own stores, online and wholesale -> no estimate | LDB Annual Service Plan Report 2025/26 | https://www.bcbudget.gov.bc.ca/Annual_Reports/2025_2026/pdf/agency/ldb.pdf | 2026-11-13 | WebFetch | primary |
| Colombian importers' websites in their own SECOP II supplier entry (by NIT): 544 of 1,160 importers without a site are registered, 404 give a real website; 147 tied in one run (NIT printed or the site names itself) | SECOP II - Proveedores Registrados | https://www.datos.gov.co/resource/qmzu-gj57.json | 2026-11-13 | counted | primary (open data) |
| Industrial design open data: roles 10/11/12 only (owner, applicant, proprietor) — no agent of record | CIPO Industrial Design Data CSV 2024-03-05 | https://opic-cipo.ca/cipo/client_downloads/ID_CSV_2024_03_07/ | 2026-11-13 | counted | primary |
| FEC 2025-26 operating expenditures to Canadian addresses: 355 lines, 41 committees, mostly card | FEC bulk oppexp26.zip | https://www.fec.gov/files/bulk-downloads/2026/oppexp26.zip | 2026-11-13 | counted | primary |
| SAQ's permit-holder page names cash-and-carry and order forms, no invoice / payment terms and no exclusivity sentence; RACJ site in maintenance (redirect) | saq.com / racj.gouv.qc.ca | https://www.saq.com/en/permit-holders | 2026-11-13 | WebFetch | primary |
| Québec alcohol retail permit holders (holder, NEQ, address, permit type; weekly; CC-BY) — a register to use once the RACJ's own sentence on its yearly duties can be read | Données Québec racj-alcool-detaillant | https://www.donneesquebec.ca/recherche/dataset/racj-alcool-detaillant | 2026-11-13 | WebFetch | primary |
| credit-scan cycle 2026-11-12 15:04Z read 697,172 sites (55,115 with a credit) and lost the merge to 12 refused pushes (12-minute merge recomputed per push) -> merge now computed once; salvage workflow dispatched on its artifacts | run 43243749246 log | — | 2026-11-13 | log | primary |
Hypothesis update: the lead supply, not the mailbox reader, is the limit now (mailbox-crawl runs end in 4-17 minutes); a lost scan merge
was the largest single leak found tonight.
