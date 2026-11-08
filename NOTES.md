# NOTES.md — findings, hypotheses, sources (Claude lane)

## Question: why are the P01 Gold buyer/vendor facts below target, and which lever closes each gap?
Evidence base: `~/cch-tasks/ranked_latest.csv.gz` (13:28Z build) joined to the readers' resume files on the Mac (2026-11-08 14:20Z).

| candidate cause | evidence for | evidence against | confidence (2026-11-08 16:05Z) |
|---|---|---|---|
| H1 sites never read | 363 of 65,431 delivered domains unread (site_tasks.py) | only 363, none in priority 0–1 | ruled out for Gold |
| H2 fetch fails on redirects | 55 of 262 Gold rows missing buyer_phone had status http_308; 56 of 268 missing logo | — | established: fixed 14:3xZ; the refresh log shows no http_308 statuses since |
| H3 read OK but extractor misses | legal name: 226 of 344 missing were status ok | — | established: after JSON-LD / terms-page extractors + registries, Gold buyer_legal_name 41.2 → 87.5 % in one build (15:48Z) |
| H4 shared domains keyed once per domain | calgary.ca, canada.ca departments, mcmaster.ca all "no_contact" | — | established: canada.ca ECCC now read from its own URL (test 14:5xZ); effect on rows pending the refresh |
| H5 vendor has no known website | 247 of 419 Gold rows missing vendor_phone had no vendor site | — | established; lever: search → reader confirmation (125 confirmed of 160 proposals by 16:00Z) |
| H6 contract value missing because the source has none | 205 Gold rows: bids&tenders 46, auditor-of-record 31, contact leads 24, BC registrar 16, customer stories 13, TEC 11, Biddingo 8, MERX 6 | bids&tenders raw stores held the awarded bidder's submitted price (9,213 records recovered) | likely for the rest: lobbying / news / auditor / client-list proofs have no value by nature (≈17 % of Gold) |

## Question 2 (owner 11:38 EST): what blocks AP grade A on delivered rows, and which lever closes each blocker?
Evidence: P01 Gold batch of the 16:12Z build (585 rows), checked 16:46Z with the grade's own criteria.

| blocker | rows (Gold) | lever | confidence that the lever closes most of it |
|---|---|---|---|
| payment terms not published | 475 | AP walker pages + PDFs → ap_terms (2-hourly); per-buyer searches for PO terms & conditions / supplier guides (PC waves); statutory construction default in its own column | medium: many small buyers publish terms only inside PO T&C PDFs; some publish none |
| PO rule not published | 409 | same pages (PO T&Cs, supplier guides, AP pages) | medium |
| DMARC not enforced (penalty) | 190 | none — the buyer's DNS; reported, never "fixed" | n/a (documented ceiling for A) |
| mailbox not on the buyer's own domain | 75 | shared-service / parent-domain cases: check whether the buyer's own site publishes that mailbox domain (deep_pages); otherwise the criterion stands | low–medium |
| bill-to legal name not published | 73 | registries (CBR buyers pass running), REQ bulk (QC public bodies), JSON-LD, G&C recipients | high |
| billing address not published | 45 | org_extras refresh (address_v2), AP pages (invoice_mailing_address), registries | high |

## Question 3 (owner 12:23 EST): are the "ceilings" real — which untried source families exist for each capped field?
| field | untried source family (2026-11-08 17:30Z scouting) | what it can do under AGENTS §2 | status |
|---|---|---|---|
| contract value / relationship recency for provincial-ministry buyers | Public Accounts payee schedules: Ontario "Detailed Schedule of Payments" (data.ontario.ca, CSV 2014-15 … 2025-26: Amount, Ministry, Category, Payment Detail, Recipient — no payee address); Alberta "Selected payments from the General Revenue Fund (data files)" (open.alberta.ca, XLSX, 27 files); BC "CRF Detailed Schedules of Payments – Other Supplier Payments" (BC Data Catalogue, CSV) | pair facts (annual amount, fiscal year) for buyer–vendor pairs already in the ranked file (BC / AB / QC ministries are buyers; Ontario ministries are NOT buyers yet — the schedule has no vendor address, so it cannot create records on its own under rule 1) | to build next: BC + AB pair facts; Ontario noted as a buyer source that needs a vendor-location source alongside |
| PO numbers | PO / cheque registers: Edmonton "Purchase Orders over $10,000" (Socrata y9rm-5xha, last updated 2019-12-18 — stale), Ottawa / Calgary / Winnipeg / Vancouver catalogues returned no PO-level dataset for "purchase order" / "cheque register"; US checkbooks are already sources (us_city_chicago, nyc, la, austin …) | pair facts only (no vendor address) | partially capped: Montréal / Laval / Toronto done; others lack PO-level open data as of today |
| contracts from Nova Scotia | "Awarded Public Tenders" (data.novascotia.ca m6ps-8j6u, updated 2026-10-20) | already assessed by the team: `ca_nova_scotia` REJECTED — no supplier location in any accessible source | capped by rule 1 unless a vendor-location field appears |
| buyer legal name / NEQ / BN / registered address | REQ open data (JeuDonnees.zip 270 MB, Nom.csv 290 MB, Entreprise.csv 650 MB) + Corporations Canada CSVs (1.58 M corporations, BN) matched offline | values with source URL + quote | DONE 17:30Z: 11,286 organisations matched (9,330 buyers, 1,956 vendors; 2,719 with BN, 11,452 with a registered address), daily rerun in claude-engines |
| GST number / cheque-run cadence / PO rule / e-signature as published | purchasing bylaws and AP policy PDFs (search waves now ask for them), PO terms & conditions | values as published | in progress (PC waves, walker PDFs) |

## What is established / likely / unknown (for the owner)
- Established: 57 → 87 of 438 benchmarks in one day with no rule relaxed except the owner's own (named AP person allowed); gates PASS on every build.
- Likely: 120–160 benchmarks by 2026-11-09 morning as the refresh (65k domains), registry lookups and AP walker finish; the P13 long tail (orgs without websites) stays below target.
- Unknown: the yield of the AP walker pages for payment terms / PO rules (first extraction pass over them at ~17:00Z); whether Canada's Business Registries rate-limits a 4,000-request run (none so far at 1 req/s).

## Source table
| claim | source | URL | accessed | quote | independent |
|---|---|---|---|---|---|
| Python 3.9 urllib does not follow 308 | Python docs, urllib.request HTTPRedirectHandler | https://docs.python.org/3/library/urllib.request.html | 2026-11-08 | "Changed in version 3.11: Support for HTTP 308" (to confirm on the page; observed: 55 Gold sites returned http_308 to our fetcher) | yes (observation) |
| CRA charities list carries BN, legal name, address | open.canada.ca dataset 80c00cdb-1358-415c-bb8b-0de7f12675b8 | https://open.canada.ca/data/en/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8 | 2026-11-08 | ident file columns "BN, Category, Sub Category, Designation, Legal Name, Account Name, Address Line 1/2, City, Province, Postal Code, Country" | yes |
| Wikidata NEQ property is P10503 | Wikidata | https://www.wikidata.org/wiki/Property:P10503 | 2026-11-08 | resolved by label at runtime in tools/wikidata_orgs.py | yes |
| Montréal / Laval / Toronto publish PO-level open data | city portals (CKAN) | see contrib/claude/po_sources.json | 2026-11-08 | 330,978 PO rows harvested (Montréal 300,283; Laval 19,864; Toronto 7,803 + 3,028) | yes |
| Canada's Business Registries search API | ISED (front-end config.js names it) | https://ised-isde.canada.ca/cbr/srch/api/v3/search?fq=keyword:{name}&lang=en&queryaction=fieldquery | 2026-11-08 | response fields: Company_Name, BN, Juri_ID, Registry_Source, Entity_Type, Status_State, Date_Incorporated, Reg_office_city, Reg_office_province, XP_TYPE | yes (primary) |
| G&C disclosure carries recipient BNs | open.canada.ca dataset 432527ab-7aac-45b5-81d6-7597107a7013 | https://open.canada.ca/data/en/dataset/432527ab-7aac-45b5-81d6-7597107a7013 | 2026-11-08 | column recipient_business_number; 1,383,199 rows, 228,065 recipient names with a BN | yes (primary) |
| G&C BN vs CRA charity BN | both files | — | 2026-11-08 | 827 of 873 overlapping buyers carry the same BN9; 46 differ (related entities or keying) | — |
| Federal construction owners must pay a proper invoice within 28 days | Federal Prompt Payment for Construction Work Act, S.C. 2019, c. 29, s. 387 (Justice Laws, current to 2026-10-19, last amended 2023-12-09) | https://laws-lois.justice.gc.ca/eng/acts/F-7.7/FullText.html | 2026-11-08 | s. 9(2): "no later than the 28th day after the day on which the proper invoice is received"; s. 10(1) contractor → subcontractor 35th day; s. 11(1) 42nd day | yes (primary) |
| Ontario owners (Crown bound, s. 3(1)) must pay a proper invoice within 28 days | Construction Act, R.S.O. 1990, c. C.30 (e-Laws, consolidation from 2026-01-01) | https://www.ontario.ca/laws/statute/90c30 | 2026-11-08 | s. 6.4(1): "an owner shall pay the amount payable under a proper invoice no later than 28 days after receiving the proper invoice from the contractor" (in force 01/10/2019); s. 6.5(1) contractor → subcontractor 7 days after payment | yes (primary; the e-Laws HTML carries the text server-side although the page says it needs JavaScript) |
| Alberta owners must pay a proper invoice within 28 days; Act does not apply to Crown public works | Prompt Payment and Construction Lien Act, R.S.A. 2000, c. P-26.4 (King's Printer, current as of 2025-04-01) | https://kings-printer.alberta.ca/documents/Acts/P26P4.pdf | 2026-11-08 | s. 32.2(1): "an owner who owes money under a proper invoice must pay the amount payable under a proper invoice no later than 28 days after receiving the proper invoice"; s. 1.1(1.1): "Except as provided in the Public Works Act, this Act does not apply in respect of a public work" | yes (primary PDF) |
| Ontario Detailed Schedule of Payments columns | data.ontario.ca package public-accounts-detailed-schedule-of-payments | https://data.ontario.ca/dataset/public-accounts-detailed-schedule-of-payments | 2026-11-08 | header of the 2025-26 CSV: "Amount $,Ministry,Category,Payment Detail,Recipient,Statutory,Additional Detail"; categories Transfer Payments 8,810 rows, Other Payments 5,330, Travel Expenses 1,489 | yes (primary) |
| Saskatchewan / Manitoba / Nova Scotia / New Brunswick / Québec / BC prompt-payment rules | — | publications.saskatchewan.ca unreachable from the cloud (HTTP 000) | 2026-11-08 | not verified today → not applied | — |

## Raw-field audit (bids&tenders / Biddingo / MERX full files) — done 2026-11-08 14:3xZ
- bids&tenders (69,975 records): 46,780 without a value; `stores.Submitted[].VerifiedValue` carries the awarded vendor's submitted price for 7,876 of the first 60,001 → implemented in tools/patch_dataset.py (9,213 records on the full file); `len(stores.Submitted)` = number of bids (58,304 records).
- Biddingo (4,522): `bidInfo.valueRange` = "Not Applicable"; bidder prices only in `bidResultInfoMap.<id>.priceChar` (ambiguous mapping to the winner → not used); `bidReceivedBidderList` length = number of bids.
- MERX (12,863): 4,868 "Awarded Value: Undisclosed" → truly not published.
