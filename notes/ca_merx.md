# ca_merx — MERX public "Awarded Solicitations" (award notices)

Status: COMPLETE for the crawl window described below (final counts at the bottom).

## Source
- Publisher: MERX (mdf commerce) on behalf of each issuing organization (Ontario/Manitoba/Atlantic/Prairie
  municipalities, universities, colleges, hospitals and health shared services, utilities, provincial ministries
  such as Manitoba Finance / Manitoba Transportation & Infrastructure, federal crown corporations such as CBC,
  BDC, FCC, EDC, CATSA, Marine Atlantic).
- Listing: `https://www.merx.com/public/solicitations/awarded?keywords=&sortBy=awardedDate&sortDirection=DESC&pageNumber=N`
  (25 rows/page; site total 57,750 awarded rows on 2026-10-25T17:50Z). MERX caps any listing at 1,000 rows (40 pages),
  so the crawl is partitioned by `location=<id>&category=<id>` (675 partitions in
  `downloads/ca_merx/partitions.txt`) and stops each partition when award dates fall below 2021-06-01.
  Pages saved in `downloads/ca_merx/pages/`, parsed rows in `downloads/ca_merx/listing.jsonl` (49k+ rows,
  22.8k+ distinct ids; row_type `solicitation` = MERX-hosted with public abstract; row_type `notice` = interception
  mirrors of other portals which redirect to login and are not fetched).
- Award tab (public, no login): `https://www.merx.com/public/solicitations/<merx_id>/abstract/award`
  -> `downloads/ca_merx/detail_pages/<id>_award.html`, parsed into `downloads/ca_merx/details.jsonl`
  (awardee blocks: Supplier Awarded, Address lines, Awarded Value, Award Date, Contract Dates, Contract Number,
  Description; header fields: Reference Number, Solicitation Title, Publication Date, Closing Date). The notice tab
  was fetched for the first ~150 only (dropped to save requests).
- Crawl start 2026-10-25T17:50Z; killed by machine reboot 19:08Z; resumed 19:16Z (listing: skips partitions whose
  log shows they finished; details: skips merx_ids already in details.jsonl). Rate: listing 1 req/s, details 2 req/s.
- Sporadic HTTP 403 on individual abstract URLs (≈10% of first attempts; retries usually succeed — no CAPTCHA /
  challenge page seen). 125 award tabs return 404 (no public award). Failed rows are kept with http_status null.
- Scripts: `scripts/ca_merx/crawl_listing.py`, `crawl_details.py`, `normalize.py`.

## Canadian vendor
Last line of the awardee "Address" block (`Canada` kept; `United States` 157, `Germany`, `France`, `United Kingdom`…
excluded, values in normalize_stats.json). City/province/postal parsed from the second-last line
("City, Province, Postal"). Awardees whose country line is `Undisclosed` or blank go to
`normalized/ca_merx_unverified_country.jsonl` with `vendor.country = null`, `country_basis = "not published …"`.
Quebec-located buyers (listing location contains QC) are skipped (SEAO covers Quebec).

## Ongoing logic
- `ongoing`: awardee "Contract Dates" = `YYYY/MM/DD - YYYY/MM/DD` with start ≤ 2026-10-25 ≤ end.
- `end_date_unknown`: award notice published without contract end date (Award Date / Contract Start Date in basis).
- Excluded: end < ref, start > ref, future award date.
- One record per awardee: `record_id = ca_merx:<merx_id>:<awardee index>`.

## record_url
`https://www.merx.com` + listing href, e.g.
`https://www.merx.com/mbgov/cityofwinnipeg/solicitations/Water-Meter-and-AMI-Radio-Transmitter-Installation-Contractor/0000306654?origin=0`
(verified HTTP 200 by the earlier worker; award tab URL kept in `contract.related.award_tab_url`).

## Counts
First normalization (1,770 details, 14:33 local): ongoing 830, end_date_unknown 967. Final counts: see bottom.

## Samples (from first normalization)
- ca_merx:3660948766:1 | ongoing | The City of Winnipeg | Neptune Technology Group Canada Co., Mississauga | 23,004,210.41 | 2026-09-24 – 2030-06-30
- ca_merx:4058516406:1 | ongoing | Manitoba Transportation and Infrastructure | Selkirk Machine Works (1982) Ltd., Selkirk | 155,873 | 2026-09-23 – 2027-03-20
- ca_merx:4091403356:1 | ongoing | York University | INTERFAX SYSTEMS INC., Saint Laurent | 137,131 | 2026-10-23 – 2026-11-30
- ca_merx:3987670261:1 | ongoing | Public Service Delivery (Manitoba) | Veolia Water Technologies & Solutions, Winnipeg | 2,826.77 | 2026-08-01 – 2027-07-31
- ca_merx:4058516407:1 | ongoing | Manitoba Transportation and Infrastructure | Selkirk Machine Works (1982) Ltd. | 91,496 | 2026-09-23 – 2027-03-20

## Known gaps
- Awards older than 2021-06 not crawled (partitions stopped there); `notice` rows (mirrors of other portals) not fetched.
- Details crawled newest award first; any remaining backlog at cut-off is older awards.


## Final counts (resumed crawl, normalized 2026-10-26 01:52 UTC)
- Detail pages parsed: 16070
- Records: main file 12863; unverified-country file 260
- normalize_stats.json: {"stats": {"details": 16070, "excluded_vendor_country": 835, "excluded_ended": 4248, "excluded_not_started": 23, "no_awardees": 1350, "no_award_tab": 1795, "excluded_quebec_buyer_location": 4, "records": 12863}, "by_status": {"ongoing": 3054, "end_date_unknown": 9809}, "by_status_unverified": {"end_date_unknown": 241, "ongoing": 19}, "n_buyers": 197, "buyers": [["City of Ottawa", 1242], ["Toronto Transit Commission - PCM Operating", 1206], ["Manitoba Hydro", 961], ["Saskatchewan Power Corporation (SaskPower)", 827], ["The City of Winnipeg", 702], ["Newfoundland and Labrador Housing Corporation (NLHC)", 504], ["NL Provincial Health Shared Services Supply Chain", 368], ["Government of Newfoundland and Labrador (GNL) - Public Procurement Agency", 341], ["Public Service Delivery", 317], ["NLSchools", 316], ["University Of Calgary", 297], ["University of Toronto – St. George Campus – Procurement Services", 279], ["Toronto Transit Commission - PCM Capital", 252], ["Humber Polytechnic", 228], ["Manitoba Liquor and Lotteries Corporation", 221], ["York University", 211], ["Infrastructure Ontario", 193], ["McMaster University", 180], ["Manitoba Public Insurance", 179], ["University of Toronto Mississauga", 158], ["CreateTO (Build Toronto, TPLC)", 156], ["Greater Toronto Airports Authority", 151], ["Business Development Bank of Canada", 147], ["Mohawk Medbuy Corporation - CAPsource", 136], ["City of Airdrie", 132], ["Toronto Metropolitan University", 130], ["Government of Newfoundland and Labrador (GNL) - Transportation & Infrastructure", 121], ["Colliers Project Leaders", 120], ["Ottawa Community Housing", 118], ["Environment and Climate Change", 102], ["Manitoba Transportation and Infrastructure - Tendering and Contracts", 98], ["CBC/Radio Canada", 97], ["Toronto Police Service", 95], ["Carleton University", 91], ["Export Development Canada - EDC", 89], ["St Clair College of Applied Arts and Technology", 87], ["Brock University", 84], ["Government of Newfoundland and Labrador (GNL) - Municipal Infrastructure (TI)", 83], ["Asset Management Division", 83], ["University of Toronto Scarborough", 64], ["Farm Credit Canada (FCC)", 63], ["Canadian Air Transport Security Authority", 63], ["AIMCo Alberta Investment Management Corporation", 63], ["Sudbury Catholic District School Board", 63], ["University of Ottawa", 61], ["Manitoba Housing Renewal Corporation", 60], ["La Cité Collégiale", 59], ["WorkplaceNL", 57], ["The Ottawa Hospital", 56], ["College of the North Atlantic", 54], ["Ornge", 53], ["Ontario Lottery and Gaming Corporation (OLG)", 42], ["Newfoundland Labrador Liquor Corporation", 39], ["Canada Post Corporation", 38], ["Technical Standards and Safety Authority", 36], ["Efficiency Manitoba", 34], ["Marine Atlantic", 34], ["Centennial College", 32], ["University of Toronto – OREP", 31], ["Town of Arnprior", 30], ["University of Toronto", 28], ["SMS Engineering Ltd", 26], ["Conseil des Écoles Catholiques du Centre-Est", 26], ["University of Guelph", 26], 
- Crawl window: newest awards first; bids&tenders details fetched for awards closing 2023-2026 in full and 2021-2022 as far as reached; MERX award tabs fetched newest first as far as reached (older backlog listed in downloads/<source>/listing.jsonl).
