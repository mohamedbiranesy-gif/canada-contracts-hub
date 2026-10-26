# ca_bidsandtenders — bids&tenders (eSolutions Group) awarded bids, all client portals

Status: COMPLETE for the crawl window described below (final counts at the bottom).

## Source
- Aggregator listing (public): `https://opportunities.bidsandtenders.com/bid-opportunities/Embed?status=Awarded&page=N&pageSize=50&sort=UtcClosingDate&dir=DESC`
  crawled 2026-10-25T17:27:40Z–18:17:36Z, pages 0–2046, total_results 102,310, 102,260 rows
  (`downloads/ca_bidsandtenders/listing.jsonl`, page HTML in `pages/`). Covers ~300 client portals
  (`<client>.bidsandtenders.ca`; a few US `.net` portals): municipalities across ON/AB/SK/MB/NS/NB/NL/BC,
  Government of Yukon, Newfoundland and Labrador Hydro, school boards (e.g. TDSB), utilities.
- Detail page per bid: `https://<client>.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/<uuid>` — public
  "Bid Details" table (Bid Number, Bid Status, Published/Closing/Awarded dates, Duration in months, Categories,
  Description …) plus the embedded Ext.NET stores (Awarded vendors with Address/City/ProvinceState/PostalCode/Country/
  Value, Submitted/PlanTakers when public, Addendums, Documents, PurchasingReps). Parsed into
  `downloads/ca_bidsandtenders/details.jsonl` (one line per bid, all stores kept verbatim).
- Detail crawl newest closing first: 17:29Z–19:08Z (21,603 bids; killed by reboot), resumed 19:16Z at 3 req/s total
  (across client sub-domains). Scripts: `scripts/ca_bidsandtenders/crawl_listing.py`, `crawl_details.py`, `normalize.py`.
- No bot challenge encountered.

## Canadian vendor
Awarded store field `Country` (`Canada` -> main file, with ProvinceState/City/PostalCode as published). Non-Canada
values (United States 37, others ≤2) excluded. Blank Country -> `normalized/ca_bidsandtenders_unverified_country.jsonl`
(vendor.country null, basis "not published"; 0 so far — the portal publishes a country for every awarded vendor).

## Ongoing logic
- `ongoing_inferred`: field "Duration in months" + "Bid Awarded Date" (or closing date) -> end = award + N months ≥
  2026-10-25 (arithmetic in status_basis).
- `end_date_unknown`: award published, no duration.
- Excluded: inferred end < ref, award date in the future, non-CA vendor.
- One record per awarded vendor row: `record_id = ca_bidsandtenders:<tender uuid>:<row index>`.

## record_url
The detail page URL itself (e.g. `https://brazeau.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/4a1624d4-7959-47e6-b0fa-d8a0a737965a`), fetched HTTP 200 during the crawl.

## Counts
First normalization (7,762 bids): ongoing_inferred 4,578; end_date_unknown 4,698 (9,276 records); top buyers
Newfoundland Labrador Hydro 256, Government of Yukon 210, City of Saskatoon 182, Halifax Regional Municipality 181.
Final counts: see bottom.

## Known gaps
- Older bids (closing before the point reached at cut-off) not detail-fetched; listing has all 102k for later resume.
- No explicit contract start/end dates on the public page; status relies on Duration in months.


## Final counts (resumed crawl, normalized 2026-10-26 01:52 UTC)
- Detail pages parsed: 67872
- Records: main file 69975; unverified-country file 12
- normalize_stats.json: {"stats": {"details": 67872, "no_awarded_vendors": 2528, "excluded_ended_by_duration": 15051, "excluded_non_canada_vendor": 3122, "vendor_country:Denmark": 1, "vendor_country:United States": 3064, "vendor_country:India": 2, "vendor_country:Germany": 3, "vendor_country:Austria": 1, "vendor_country:United Kingdom": 17, "vendor_country:Chile": 1, "vendor_country:Poland": 1, "vendor_country:France": 5, "vendor_country:United Arab Emirates": 2, "vendor_country:Belgium": 2, "excluded_future_award": 2, "vendor_country:Brazil": 1, "vendor_country:Netherlands": 4, "vendor_country:Australia": 6, "vendor_country:Ireland": 3, "http_not_200": 47, "unverified_country_rows": 12, "vendor_country:Taiwan, Province of China": 1, "vendor_country:Japan": 3, "vendor_country:Korea, Republic of": 1, "vendor_country:Switzerland": 1, "vendor_country:Spain": 1, "vendor_country:Czech Republic": 1, "vendor_country:Iceland": 1, "records_main": 69975, "records_unverified": 12}, "by_status": {"ongoing_inferred": 14845, "end_date_unknown": 55130}, "n_orgs": 365, "orgs": [["Newfoundland Labrador Hydro", 2308], ["Toronto District School Board", 1495], ["Government of Yukon", 1345], ["Region of Peel", 1059], ["York Region", 899], ["Region of Waterloo", 862], ["City of Cornwall", 829], ["City of Hamilton", 808], ["Region of Halton", 747], ["City of Vaughan", 720], ["City of Barrie", 667], ["Halifax Regional Municipality", 653], ["City of Burnaby", 614], ["City of Kitchener", 612], ["Niagara Region", 609], ["Region of Durham", 595], ["City of Timmins", 581], ["City of Guelph", 562], ["City of Brampton", 558], ["City of Mississauga", 544], ["Toronto Catholic District School Board", 541], ["City of Markham", 537], ["Metro Vancouver", 508], ["City of London", 479], ["City of Thunder Bay", 454], ["City of Burlington", 442], ["Norfolk County", 438], ["City of Oshawa", 412], ["City of St. John's", 396], ["City of Brantford", 387], ["County of Simcoe", 379], ["Waterloo Region District School Board", 361], ["Town of Milton", 361], ["Dufferin-Peel Catholic District School Board", 353], ["Regional Municipality of Wood Buffalo", 351], ["City of Saskatoon", 347], ["City of Medicine Hat", 346], ["City of Greater Sudbury", 338], ["Town of Caledon", 338], ["Town of Oakville", 336], ["Oxford County", 335], ["City of Red Deer", 335], ["City of Grande Prairie", 335], ["Kawartha Pine Ridge District School Board", 331], ["Township of Langley", 329], ["City of Lethbridge", 313], ["City Of Peterborough", 309], ["Conseil scolaire catholique MonAvenir", 308], ["Durham District School Board", 305], ["Town of Georgina", 304], ["Town of Ajax", 292], ["District of Thunder Bay Social Services Administration Board", 287], ["City of Richmond Hill", 275], ["Town of Newmarket", 265], ["City of Yellowknife", 262], ["Town of Whitby", 250], ["Municipality of Clarington", 247], ["City of Richmond", 237], ["United Counties of Prescott and Russell", 236], ["City of Nanaimo", 234], ["City of Kawartha Lakes", 234], ["Simcoe
- Crawl window: newest awards first; bids&tenders details fetched for awards closing 2023-2026 in full and 2021-2022 as far as reached; MERX award tabs fetched newest first as far as reached (older backlog listed in downloads/<source>/listing.jsonl).
