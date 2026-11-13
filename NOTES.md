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
