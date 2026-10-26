# us_city_la — Checkbook L.A. (Los Angeles City Controller), supplier_country = CA

Reference date 2026-10-25. Output: `/home/claude/contracts/normalized/us_city_la.jsonl` (**58 records**, all `end_date_unknown`). Script: `scripts/us_city_la/normalize.py`.

## What was downloaded
- Dataset `pggv-e4fn` "Checkbook L.A. Data" on controllerdata.lacity.org (landing https://controllerdata.lacity.org/d/pggv-e4fn → /Purchasing/Checkbook-L-A-Data/pggv-e4fn): city payments since FY2018 (~6.6 M rows). Columns include fiscal_year, department_name, vendor_name, transaction_date, dollar_amount, po_num, po_date, description, detailed_item_description, item_code(_name), account_code/name, vendor_id, zip, **supplier_city, supplier_country**, procurement_organization, buyer_name, currency, value_of_spend, vendor_num, inv_num, inv_date, authority/authority_name/authority_link.
- Pulled via SODA with `$where=supplier_country='CA'` (`scripts/us_common/soda_pull.py`, 2026-10-25 18:04:22 UTC) → `downloads/us_city_la/checkbook_la_ca_pggv-e4fn.jsonl`, 1,524 rows. Country distribution in the dataset: US 4.30 M, blank 1.44 M, USA 0.84 M, **CA 1,524**, GB 107, ES 75 …

## How "Canadian vendor" was determined
Structured `supplier_country = 'CA'`; cross-checked against `supplier_city` (Quebec, Ottawa, Richmond, Hawkesbury, Langley, Burnaby, Winnipeg, Montreal, Mississauga, Victoria …) and `zip` (Canadian postal codes, e.g. G1P 0A4, K1G 6L3, H4Z 1G8). Names never used.

## How "ongoing" was determined
Payment-level data; no contract dates. One record per (po_num, vendor_id) with all payments in `raw.rows`; kept as `end_date_unknown` iff the latest payment date is within the 12 months before the reference date (58 of 619 POs; 561 excluded, 3 rows had no PO number). `contract.dates.start` = po_date, `amended_last` = last payment; `related.first_payment/last_payment`; `value` = sum of payments on the PO.

## Record construction
`record_id` = `us_city_la:<po_num>:<vendor_id>`; buyer = "City of Los Angeles - <department_name>"; instrument_type derived from PO prefix (BPO blanket / OPO open / C contract). No per-PO page on the Controller's site (`record_url` null).

## Counts
58 end_date_unknown. Vendors: FLO Services USA, Inc. (Quebec G1P 0A4; EV charging maintenance for Bureau of Street Lighting) 51 POs; ICOR Technology (Ottawa; Mini-Caliber robot, USD 174,502, Mayor's office/LAPD); DART Aerospace (Hawkesbury); VertiGIS North America (Victoria); InWater Technologies; Lotek Wireless; Hummingbird Drones; Enviro World Corporation. Sum of payments USD 315,524.

## 5 samples
- us_city_la:OPO46260000300482:000045689 | ICOR TECHNOLOGY INC. (Ottawa K1G 6L3) | Mayor | Robot, Mini-Caliber | USD 174,502.50 | PO 2025-11-20, paid 2026-01-09
- us_city_la:OPO84260000300825:000051012 | FLO SERVICES USA, INC. (Quebec) | Public Works - Street Lighting | FLO services invoice | USD 74,750 | PO 2026-02-27
- us_city_la:BPO84260000212146:000051012 | FLO SERVICES USA, INC. | Street Lighting | AUI-10234 | USD 613.40 | PO 2026-01-07
- us_city_la:BPO40260000203635:000045802 | DART AEROSPACE LTD (Hawkesbury K6A 1K7) | General Services | USD 2,820 | 2025-08-18
- us_city_la:OPO88260000300683:000044327 | VERTIGIS NORTH AMERICA LTD (Victoria V8W 1T7) | Recreation and Parks | USD 7,361 | 2026-01-22

## Known gaps / limits
- No contract terms; the Controller's "contracts" view is not a separate dataset. The City Clerk's Council File / contract register (CARS) is not on the open-data portal.
- 1.44 M payment rows have a blank supplier_country; Canadian vendors among them are not detectable (no vendor address columns beyond city/zip for those rows).
