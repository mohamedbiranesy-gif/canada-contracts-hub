# us_city_nyc — NYC Recent Contract Awards (City Record), vendor address in Canada

Reference date 2026-10-25. Output: `/home/claude/contracts/normalized/us_city_nyc.jsonl` (**2 records**: 1 `ongoing_inferred`, 1 `end_date_unknown`). Script: `scripts/us_city_nyc/normalize.py`.

## What was downloaded
- NYC Open Data `qyyg-4tf5` "Recent Contract Awards" (City Record award notices, 2003–2026; landing https://data.cityofnewyork.us/d/qyyg-4tf5), SODA JSON 2026-10-25 17:28:48 UTC → `downloads/us_city_nyc/recent_contract_awards_qyyg-4tf5.jsonl`, 53,953 rows. Columns: request_id, start_date/end_date (= publication date of the notice), agency_name, type_of_notice_description (all "Award"), category_description, short_title, selection_method_description, pin, contact fields, contract_amount, additional_description_1..3, other_info_1..3, printout_1..3, **vendor_name, vendor_address** (free text), document_links, agency address.
- Checkbook NYC API (https://www.checkbooknyc.com/api, XML POST) was probed: the Contracts domain works but exposes vendor name/code only (no vendor address; the vendor address is on the HTML site, which returns 403 to non-browser clients). Not used.
- Other NYC datasets checked: "Active Contracts" is not on the portal; DYCD Contracts (graj-69em) and Directory of Awarded Construction Contracts (j7gw-gcxi) have no vendor address.

## Canadian vendor
`vendor_address` free text containing "Canada", a Canadian province name, or a province code + Canadian postal code (76 of 53,953 notices; false positives like "242 Old New Brunswick Road" (NJ) and "Montreal Ave, Staten Island" are excluded by the rules). Names never used.

## Ongoing
Award notices carry only the notice date. `ongoing_inferred` when the description states a term (Radiation Solutions Inc: "3-year Sole Source Requirements Contract" published 2026-04-15 → 2029-04-15, arithmetic in status_basis); `end_date_unknown` for notices within the last 3 years without a stated term (Reliance Foundry, Surrey BC, Martello bollards for DOT, USD 1,009,694, 2024-11-26). 73 older notices (2003–2023) excluded as stale; 1 renewal (Softek, NJ address) excluded as non-Canadian/ended.

## Gaps
Vendor address is free text and often omits country for older notices; NYC's contract register (PASSPort / Checkbook) with vendor addresses is not bulk-accessible without a browser.
