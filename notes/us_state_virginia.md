# us_state_virginia — eVA Procurement Data (Virginia Open Data Portal), vendor address in Canada

Reference date 2026-10-25. Output: `/home/claude/contracts/normalized/us_state_virginia.jsonl` (**709 records**, all `end_date_unknown`). Script: `scripts/us_state_virginia/normalize.py`.

## What was downloaded
eVA (Virginia's statewide e-procurement system used by 245 state agencies/universities and 900+ local public bodies) publishes **purchase-order line data** per fiscal year on data.virginia.gov (CKAN). Columns: Entity Code/Description, NIGP #/Description, Item Description, Order #, Order Line Number, Quantity, Unit Price, UoM, Line Total, Line Total Change, Manufacturer Part #, Order Status, Shipping Name/Lines/City/State/Postal, Requisition Submitted/Approved Date, Ordered Date, Most Recent Receiving Date, SWAM flags, PO Category (Description), Procurement Transaction Type/Desc, Order Type, Contract Number, Contract Type, Registration Type, VLIN ID, eVA ID, Vendor Name, Vendor Location Name, Vendor Address Lines, Vendor Address City, **Vendor Address State**, Vendor Address Postal, Vendor Address Geolocation.

| File | How | Result |
|---|---|---|
| FY2026 (Jul 2025–Jun 2026) `https://data.virginia.gov/dataset/e6f7f6ba-23a1-4423-93cd-31697b89a26f/resource/76f6831d-fac7-4c1f-8313-cc7ff238ddca/download/eva_procurement_data_2026.csv` (959 MB, last_modified 2026-10-25) | streamed through `scripts/us_common/stream_filter_csv.py` (curl → python csv) keeping rows whose Vendor_Address_State is a Canadian province, 17:37:14–17:37:57 UTC | 1,901,705 rows scanned → 5,070 kept → `downloads/us_state_virginia/eva_2026_canada.csv` |
| FY2025 resource `b8dc22a8-e96e-460f-9d5c-8dede67fddda` (1.18 GB) | the download URL returns 404 (S3 object missing) — pulled instead via the CKAN datastore: `datastore_search_sql` with `WHERE "Vendor Address State" IN (provinces)` paginated 1,000 (`scripts/us_common/ckan_ds_pull.py`), 18:09 UTC | 2,473 rows → `eva_2025_canada.jsonl` |
| FY2024 and earlier | not pulled (orders > 15 months old cannot be "ongoing" under the 12-month rule below) | — |
Landing pages: https://data.virginia.gov/dataset/eva-procurement-data-2026-virginia , https://data.virginia.gov/dataset/eva-procurement-data-2025-virginia . Note the python urllib fetch of the FY2026 CSV got 403 from S3 (signed redirect) while curl worked; see script.

## How "Canadian vendor" was determined
Structured `Vendor Address State` ∈ {ON, QC, BC, AB, SK, NS, MB, NL, PE, NB, …} (values seen in kept rows: ON 4,263, BC 345, QC 299, AB 60, SK 33, NS 27, MB 22, NL 14, PE 6, NB 1 for FY2026). Vendor Address Postal is a Canadian postal code in these rows. No country column exists. Names never used.

## How "ongoing" was determined
eVA publishes orders, not contract terms, so every record is `end_date_unknown`. Rows are grouped into one record per (Order #, eVA ID) with all lines in `raw.rows`; a record is kept only if `Ordered Date` is within the 12 months before the reference date (2025-10-25 … 2026-10-25) and the order is not entirely Canceled/Denied. Of 2,112 Canadian orders: 709 kept, 1,361 older than 12 months, 42 cancelled/denied. 187 FY2026 lines reference a `Contract Number` (CTR…/VIT-…) — the contract number is carried in `contract.identifiers.contract_number` and `instrument_type` ("purchase order (EXT) under contract CTR040404-1"), but eVA does not publish the contract's term.

## Record construction
`record_id` = `us_state_virginia:<FY>:<Order #>:<eVA ID>`. Value = sum of non-cancelled Line Totals. Buyer = Entity Description (universities, agencies, Virginia Correctional Enterprises …) with eVA entity code; shipping address kept under buyer.address. No per-order public page (eVA's public reports are the CSVs) → `record_url` null.

## Counts
709 end_date_unknown; 0 ongoing. Top buyers: George Mason University 147, Virginia Correctional Enterprises 99 (office furniture from Links Contract Furniture, Concord ON; Nightingale Corp, Mississauga), VCU 89, DGS 64 (frozen food from The Inventory Exchange, Toronto), JMU 52, ODU 20. Top vendors: Links Contract Furniture 70, The Inventory Exchange 56, Hootsuite Media 43, Abebooks 41, Nightingale 29, BioRender 19, AudienceView Ticketing 18, InnoSoft Canada 14. Sum of line totals USD 83.7 M.

## 5 samples
- us_state_virginia:2026:PO05044436:VS0000249342 | Eco-Counter Inc (Montreal QC H2W 1Y5) | Library of Virginia | 3D stereo video people-counting sensors under contract CTR040404-1 | USD 22,535 | ordered 2025-12-22
- us_state_virginia:2026:PO05178030:SUP302197 | Infocorp Computer Solutions Ltd (Toronto ON M2L 2L3) | Library of Virginia | Access2Gov server licenses and support | USD 13,212 | 2025-11-05
- us_state_virginia:2026:PO05154001-V2:E84947 | The Inventory Exchange (Toronto ON M9A 1T4) | Department of General Services | FOODS, FROZEN | USD 39,600 | 2025-11-04
- us_state_virginia:2026:PO05255236:VS0000228263 | Hootsuite Media Inc (Vancouver BC) | Department of Education | annual subscription | USD 1,188 | 2026-02-11
- us_state_virginia:2026:… | International Road Dynamics Corporation (Saskatoon SK) | VDOT | under contract CTR044792 | 2026

## Known gaps / limits
- Purchase-order level only; multi-year contracts with Canadian vendors exist in eVA (CTR numbers) but their terms are not published in this dataset. Treat these records as evidence of an active supplier relationship, not a contract term.
- FY2025 datastore pull used `Vendor Address State` codes only (the FY2026 stream also accepted province names/CANADA; none occurred).
- Orders between 2026-07-01 and 2026-10-25 (FY2027) are not yet published (no FY2027 dataset existed at retrieval).
