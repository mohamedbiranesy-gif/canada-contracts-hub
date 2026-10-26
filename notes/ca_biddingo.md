# ca_biddingo — Biddingo awarded bids (public no-authorize API)

Status: COMPLETE for awards posted 2019-01-01 .. 2026-10-25 (crawl finished 2026-10-25T20:47:27Z).

## Source
- Biddingo (biddingo.com) hosts bid opportunities for ~hundreds of public buyers, mostly Ontario municipalities,
  school boards and agencies (closing time zone ET), plus Saskatchewan (SK) and Atlantic (AT) buyers and a few US
  buyers (regionId 5, e.g. City of San José, Los Angeles Superior Court).
- List API: `GET https://api.biddingo.com/restapi/v2/noauthorize/bids?offset=<page>&limit=50&statuses=5&sort=postedDate%3Adesc`
  (statuses 5 = Awarded; bidCount 43,200 on 2026-10-25T18:39:38Z). Paged newest-posted first until posted date
  < 2022-01-01: 7,900 awarded bids -> `downloads/ca_biddingo/list.jsonl` (31 MB, finished 18:41:09Z); extended at
  20:01Z with `scripts/ca_biddingo/crawl_list_more.py` (resumes after the last saved page) back to posted 2019-01-01:
  12,900 awarded bids in total (pages 0–257).
- Detail API: `GET https://api.biddingo.com/restapi/bidding/noauthorize/<buyerSysId>/<buyerOrgId>/<biddingoTenderId>`
  -> `bidInfo` incl. `bidAwardInfoList[].successfulBidderInfoList[]` (bidderName, address, city, province, country,
  phoneNumber, contact name/email, totalPrice, postedDate) and unsuccessful bidders -> `downloads/ca_biddingo/details.jsonl`.
  Started 18:41Z, killed by reboot 19:08Z (3,466 done), resumed 19:16Z (skips ids already in details.jsonl), ~2.5 req/s;
  second pass 20:05Z–20:47Z for 2019–2021 rows. 12,828 detail records, 0 failures.
- Scripts: `scripts/ca_biddingo/crawl.py`, `scripts/ca_biddingo/normalize.py` (uses `scripts/_muni/terms.py`).
- No bot challenge; no 403.

## Canadian vendor
`successfulBidderInfoList[].country` (`Canada` -> main file; `United States`/`UNITED STATES` 1,177, UK 6, DE/IN/IE/NZ/LV/CN/AU 1
each excluded; blank -> `normalized/ca_biddingo_unverified_country.jsonl` with vendor.country null, basis "not published").
Province/city from the same row (no postal code published).
About 60% of awarded bids publish no successful bidder (buyer chose not to disclose) -> skipped.

## Ongoing logic
Biddingo publishes no contract start/end. Shared parser on tenderName + description (detailPreview HTML):
explicit period ending ≥ ref -> `ongoing`; stated term + anchor (successful bidder postedDate, else closing date)
-> `ongoing_inferred` (arithmetic in status_basis); else `end_date_unknown`. Ended -> excluded.
One record per successful bidder: `ca_biddingo:<biddingoTenderId>:<suplId>`.

## record_url
The public detail API URL, e.g. `https://api.biddingo.com/restapi/bidding/noauthorize/1/11004034/41757128`
(verified HTTP 200, 12 KB JSON, 2026-10-25). The web UI (`https://www.biddingo.com/...`) is an Angular SPA whose
bid route needs login verification, so no stable public HTML page per bid exists.

## Counts (final, 12,828 details; 6,473 successful-bidder rows; 7,880 bids publish no successful bidder)
Main `normalized/ca_biddingo.jsonl`: **ongoing 15; ongoing_inferred 117; end_date_unknown 4,567** (4,699).
Unverified `normalized/ca_biddingo_unverified_country.jsonl`: end_date_unknown 34; ongoing_inferred 2.
Excluded: non-Canada vendor 1,190 (US 1,177); ended per stated term/period 548.

## Samples
- ca_biddingo:41400928:41243764 | ongoing | City of Yorkton | GR Poier and Sons Construction, Langenburg SK | 2026-05-07 – 2027-04-30
- ca_biddingo:41400928:41242889 | ongoing | City of Yorkton | Yorkton Concrete 2012 Ltd, Yorkton SK | 2026-05-07 – 2027-04-30
- ca_biddingo:41276128:41089173 | ongoing_inferred | Town of Collingwood | Northern Sealants INC., Sault Ste. Marie ON | 57,600 | 2026-04-06 + 36 months
- ca_biddingo:41371428:45003567 | end_date_unknown | Aramark | Burnbrae Farms, Mississauga ON | awarded 2026-05-28
- ca_biddingo:36678728:41110994 | end_date_unknown | Upper Canada District School Board | Wayne McGill & Associates, Lunenburg ON | awarded 2022-02-22

## Known gaps
- Awards posted before 2019-01-01 not crawled (~30k older awarded bids exist).
- No postal code; no contract dates; award amounts often 0 (not published) -> value null.
