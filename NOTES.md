# NOTES.md — findings, hypotheses, sources (Claude lane)

## Question: why are the P01 Gold buyer/vendor facts below target, and which lever closes each gap?
Evidence base: `~/cch-tasks/ranked_latest.csv.gz` (13:28Z build) joined to the readers' resume files on the Mac (2026-11-08 14:20Z).

| candidate cause | evidence for | evidence against | confidence |
|---|---|---|---|
| H1 sites never read | 363 of 65,431 delivered domains unread (site_tasks.py) | only 363, none in priority 0–1 | low (ruled out for Gold) |
| H2 fetch fails on redirects | 55 of 262 Gold rows missing buyer_phone have status http_308; 56 of 268 missing logo | — | high → fixed (fetch follows 3xx by hand) |
| H3 read OK but extractor misses | legal name: 226 of 344 missing are status ok; logo: 86 ok; phone: 54 no_contact + 53 ok | — | high → org_extras v2 |
| H4 shared domains (canada.ca, …) keyed once per domain | calgary.ca, canada.ca departments, mcmaster.ca all "no_contact" | — | high → per-URL start for shared hosts |
| H5 vendor has no known website | 247 of 419 Gold rows missing vendor_phone have no vendor site | — | high → Wikidata + registry + search waves |
| H6 contract value missing because the source has none | 205 Gold rows: bids&tenders 46, auditor-of-record 31, contact leads 24, BC registrar 16, customer stories 13, TEC 11, Biddingo 8, MERX 6 | raw files may hold amounts (audit running) | medium |

## Source table
| claim | source | URL | accessed | quote | independent |
|---|---|---|---|---|---|
| Python 3.9 urllib does not follow 308 | Python docs, urllib.request HTTPRedirectHandler | https://docs.python.org/3/library/urllib.request.html | 2026-11-08 | "Changed in version 3.11: Support for HTTP 308" (to confirm on the page; observed: 55 Gold sites returned http_308 to our fetcher) | yes (observation) |
| CRA charities list carries BN, legal name, address | open.canada.ca dataset 80c00cdb-1358-415c-bb8b-0de7f12675b8 | https://open.canada.ca/data/en/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8 | 2026-11-08 | ident file columns "BN, Category, Sub Category, Designation, Legal Name, Account Name, Address Line 1/2, City, Province, Postal Code, Country" | yes |
| Wikidata NEQ property is P10503 | Wikidata | https://www.wikidata.org/wiki/Property:P10503 | 2026-11-08 | resolved by label at runtime in tools/wikidata_orgs.py | yes |
| Montréal / Laval / Toronto publish PO-level open data | city portals (CKAN) | see contrib/claude/po_sources.json | 2026-11-08 | 330,978 PO rows harvested (Montréal 300,283; Laval 19,864; Toronto 7,803 + 3,028) | yes |

## Raw-field audit (bids&tenders / Biddingo / MERX full files) — pending (background job, cloud)
