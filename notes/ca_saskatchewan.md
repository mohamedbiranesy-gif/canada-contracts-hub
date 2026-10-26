# ca_saskatchewan — SaskTenders awarded competitions (Government of Saskatchewan + SK public sector), Canadian vendors

Reference date 2026-10-25. Output `/home/claude/contracts/normalized/ca_saskatchewan.jsonl` — **18,776 records, all `end_date_unknown`**.

## What was downloaded
- Portal: https://www.sasktenders.ca/ (SaskBuilds and Procurement; `https://sasktenders.ca` without `www` fails TLS, the `www` host works). The public search `https://www.sasktenders.ca/Search?statusId=83773de3-960f-416f-a511-bbd76ff1812f&sortField=closedate&sortDirection=desc&pageSize=100&pageNumber=N` (statusId = the "Awarded" option of the Status select) returns server-rendered HTML in which every competition card is fully expanded (synopsis, dates, Competition/Agreement Type, documents, **Award Details** = supplier name, "City, Province", amount, award date, response address, contact). 23,319 awarded competitions = 234 pages of 100, all fetched 2026-10-25 17:37:58–17:52:41 UTC (≈2.5 req/s) into `downloads/ca_saskatchewan/pages/page_0001..0234.html` (`scripts/ca_saskatchewan/crawl_sasktenders.py`, log `crawl.log`). The per-competition "Print" page (`/Competitions/Print?id=<guid>`) was verified to carry no extra award fields (it omits the award block), so the listing pages are the richer source.
- Parsed into `downloads/ca_saskatchewan/competitions.jsonl` (`parse_sasktenders.py`: 23,319 competitions, 0 duplicates across pages, 24,073 award rows; 4,206 competitions carry no Award Details block), then normalized (`normalize_sasktenders.py`, stats `normalize_stats.json`).

## How "Canadian vendor" was determined
From the award-details location line only (never the name). Accepted when it contains a Canadian province/territory **code** ("Regina, SK", "Saskatoon SK", "Calgary AB") or **name** ("Regina, Saskatchewan"), or a Canadian postal code, or the word "Canada". `vendor.country_basis` quotes the matched token and the full location string. Rejected: locations with USA/US or a US state code (685), and locations with no structured country/province information at all — a bare city ("Regina", "Saskatoon", 1,879 blank, "This price includes PST", "see attached", …; 4,380 award rows). Bare Saskatchewan city names were deliberately **not** accepted (city ≠ country field). 232 award rows had no supplier name.

## How "ongoing" was determined
SaskTenders publishes opening/closing dates and the award date; there is no contract start/end/term field anywhere on the competition (synopses occasionally mention completion dates in free text, not used). All records are `end_date_unknown`; `status_basis` quotes the award date. 0 awards dated after 2026-10-25.

## Record construction
- `record_id` = `ca_saskatchewan:<competition guid>:<award index>` (one record per supplier awarded on a competition; `contract.related.awards_on_competition` gives the count).
- `record_url` = `https://www.sasktenders.ca/Competitions/Print?id=<guid>` — verified 2026-10-25: https://www.sasktenders.ca/Competitions/Print?id=2d6781e0-b09b-467b-9f81-42f264989778 → "HWY-H26105 … Roadwork-SUPPLY&INSTALL 2 SMOOTH WALL STEEL PIPE CULVERTS … Status Awarded … Organization Highways".
- Buyer = "Organization Name" (ministries like "Highways and Infrastructure", "SaskBuilds and Procurement"; Crown corporations SaskPower/SaskEnergy/SaskTel/SGI; Saskatchewan Health Authority; universities; cities of Regina/Saskatoon and ~250 municipalities). Contact name/email/phone and response address kept under `buyer`.
- `raw` = the full parsed competition (all fields, document list, every award row) plus the specific `award_detail`.

## Counts
- Competitions 23,319 → award rows 24,073 → emitted 18,776. By award year: 2009 465 … 2019 1,235, 2020 1,416, 2021 1,444, 2022 1,313, 2023 1,464, 2024 1,280, 2025 1,239, 2026 1,078. Vendor region: SK 13,649, AB 1,872, ON 1,566, MB 704, BC 539, QC 330, NS 41, NB 24, PE 11, NL 9, YT 2, NT 1, postal-code-only 28. Total award value CAD 12.27 B.
- Top buyers: Highways and Infrastructure 2,755, City of Saskatoon 2,382, City of Regina 2,134, Highways 1,702, SaskBuilds and Procurement 701, Environment 554, Parks Culture and Sport 499, SaskEnergy 480.
- Status: `end_date_unknown` 18,776; `ongoing` 0; `ongoing_inferred` 0.

## 5 samples
- ca_saskatchewan:b4d4bb11-6e27-4fb2-8070-54eba4528c68:0 | Visions Electronics LP (Regina, SK) | SaskBuilds and Procurement | Two drones with thermal imaging | CAD 11,595 | awarded 2025-04-17
- ca_saskatchewan:97c892e6-19e8-4b73-ae8e-7680f14979a5:28 | Frontier Construction Products Ltd (Thorsby, AB) | Highways | CSP culverts (29 suppliers awarded) | CAD 70,486 | awarded 2026-05-08
- ca_saskatchewan:895c436c-fd6a-45a9-a5bf-f9984a145780:0 | Praxis Consulting (Regina, SK) | Regina School Division No. 4 | Provincial Education Plan community mapping | CAD 30,500 | awarded 2025-03-11
- ca_saskatchewan:beae9f88-3bf2-4ac5-8bbf-d128f69fc8f3:0 | Unicon Construction Inc. (North Battleford, SK S9A 3W2) | City of North Battleford | 110 Street UPAR Project | CAD 2,324,445.45 | awarded 2025-03-11
- ca_saskatchewan:9e0abb32-ea9b-45e9-b9a7-c74fb9bfd28f:0 | Harbuilt Construction Management Ltd. (Moosomin, SK) | Highways | Short span bridge on Hwy | CAD 1,683,585.10 | awarded 2025-01-06

## Known gaps / limits
- No end dates → everything `end_date_unknown`; awards from 2009-2019 (≈9,000) are very probably finished but the source does not say so.
- Vendor city/region parsing of free text: ~4,400 Canadian-looking but un-provinced rows (bare city) are excluded by the country rule; multi-supplier standing-offer awards may list the same supplier several times.
- Amounts: some $0 (rate-based/standing offers) and some include PST per the location note text.
