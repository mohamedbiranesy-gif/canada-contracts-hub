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

## Raw-field audit (bids&tenders / Biddingo / MERX full files) — done 2026-11-08 14:3xZ
- bids&tenders (69,975 records): 46,780 without a value; `stores.Submitted[].VerifiedValue` carries the awarded vendor's submitted price for 7,876 of the first 60,001 → implemented in tools/patch_dataset.py (9,213 records on the full file); `len(stores.Submitted)` = number of bids (58,304 records).
- Biddingo (4,522): `bidInfo.valueRange` = "Not Applicable"; bidder prices only in `bidResultInfoMap.<id>.priceChar` (ambiguous mapping to the winner → not used); `bidReceivedBidderList` length = number of bids.
- MERX (12,863): 4,868 "Awarded Value: Undisclosed" → truly not published.
| Canada's Business Registries search API | ISED (front-end config.js names it) | https://ised-isde.canada.ca/cbr/srch/api/v3/search?fq=keyword:{name}&lang=en&queryaction=fieldquery | 2026-11-08 | response fields: Company_Name, BN, Juri_ID, Registry_Source, Entity_Type, Status_State, Date_Incorporated, Reg_office_city, Reg_office_province, XP_TYPE | yes (primary) |
| G&C disclosure carries recipient BNs | open.canada.ca dataset 432527ab-7aac-45b5-81d6-7597107a7013 | https://open.canada.ca/data/en/dataset/432527ab-7aac-45b5-81d6-7597107a7013 | 2026-11-08 | column recipient_business_number; 1,383,199 rows, 228,065 recipient names with a BN | yes (primary) |
| G&C BN vs CRA charity BN | both files | — | 2026-11-08 | 827 of 873 overlapping buyers carry the same BN9; 46 differ (related entities or keying) | — |
