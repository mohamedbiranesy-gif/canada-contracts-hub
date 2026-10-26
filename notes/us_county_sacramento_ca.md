# us_county_sacramento_ca — Sacramento County (California) "County Contracts" + "Purchase Orders" (ArcGIS Online, SAP extracts), vendor address in Canada

Reference date 2026-10-25. Output: `/home/claude/contracts/normalized/us_county_sacramento_ca.jsonl` (**23 records**: 9 `ongoing`, 14 `end_date_unknown`). Script: `scripts/us_county_sacramento_ca/normalize.py` (`python3 -I normalize.py <county_contracts_ca.jsonl> <out.jsonl> <purchase_orders_ca.jsonl>`). Found by the W1c ArcGIS Online sweep (owner `SCGISAdmin`, org `5NARefyPVtAeuJPU` = "Sacramento County GIS", sacramentocounty.maps.arcgis.com).

## What was downloaded (ArcGIS REST query, `scripts/us_common/arcgis_pull.py`, where `UPPER(VendorState) IN (<province codes/names>,'CANADA','CAN') OR UPPER(VendorAddress) LIKE '%CANADA%' OR UPPER(VendorCity) LIKE '%CANADA%'`)
- "County Contracts" — item https://www.arcgis.com/home/item.html?id=d9e90b479cda4576a8ee393a3e9ac17c, layer https://services1.arcgis.com/5NARefyPVtAeuJPU/arcgis/rest/services/County_Contracts/FeatureServer/1 (6,494 outline-agreement item rows; item modified 2026-10-25). Fields: ContractDate, ContractType (MK quantity / WK value outline agreement), ContractNo, ContractItemNo, MaterialDescription, PurchGroup (buyer), ContractEndDate, EffectivePrice, VendorName, VendorAddress, VendorCity, **VendorState**, VendorZip. Pulled 2026-10-26T03:42:34Z–03:42:35Z → `downloads/us_county_sacramento_ca/county_contracts_ca.jsonl` (63 rows).
- "Purchase Orders" — layer https://services1.arcgis.com/5NARefyPVtAeuJPU/arcgis/rest/services/Purchase_Orders/FeatureServer/1 (620,159 PO line rows). Fields: PO_No, PO_Date, PO_ItemNo, Qty, UnitPrice, UOM, MaterialDescription, VendorName, VendorAddress, VendorCity, **VendorState**, VendorZip. Pulled 2026-10-26T03:48:11Z–03:48:20Z → `purchase_orders_ca.jsonl` (342 rows, 131 POs).
- VendorState distinct values were listed first (…, BC, ON, QC, NSW, QLD, VLG, '59' …); only BC/ON/QC (+ NB in POs) are Canadian. `CA` = California, never Canada.

## Canadian vendor
`VendorState` ∈ Canadian province codes with a Canadian postal code in `VendorZip` (e.g. V8W 1T7, K2B 7G1, G0R 2C0). Names never used.

## Ongoing
- Contracts: grouped by ContractNo; start = earliest ContractDate, end = latest ContractEndDate of the items; `ongoing` iff start ≤ 2026-10-25 ≤ end → all 9 Canadian contracts (end dates 2026-12-31 … 2027-12-17).
- Purchase orders: no term; one record per PO_No; `end_date_unknown` iff PO_Date within 2025-10-25…2026-10-25 (14 of 131; 117 older excluded). `contract.related.same_vendor_outline_agreements_in_county_contracts` lists the vendor's outline agreements (many POs are call-offs against them; the PO layer carries no contract reference, so they are kept as separate instruments).

## Record construction
record_id `us_county_sacramento_ca:<ContractNo>` / `us_county_sacramento_ca:PO:<PO_No>`; buyer = "County of Sacramento, California" (department not published; PurchGroup buyer name kept in raw). value = Σ EffectivePrice of the agreement items (contracts) or Σ Qty×UnitPrice (POs). All item rows in `raw.rows`. No per-record page (`record_url` null).

## Result: 23 records (9 ongoing, 14 end_date_unknown)
Ongoing: Versaterm Public Safety (Ottawa; CAD/mobile data software, USD 1.06 M, to 2027-08-31), Sodales Solutions (Toronto; implementation milestones, USD 1.06 M, to 2027-04-29), VertiGIS North America (Victoria; Geocortex maintenance, to 2027-12-17), Safe Software (Surrey; FME, to 2026-12-31), IGM Technology (Toronto; Gravity ACFR automation), Canada Ticket (Langley; boarding passes), Umano Medical (L'Islet QC; medical bed repair), Status Electrical (Abbotsford; core services), T2 Systems Canada (Burnaby; paystations). POs: Versaterm USD 402,746 (2026-07-22), Sodales USD 204,800, Transoft Solutions USD 93,927, Canada Ticket, Recollect Systems, Real Time Networks, Safe Software, VertiGIS, IGM, Status Electrical, Umano, T2.

## Samples
- `us_county_sacramento_ca:WA00044395` VERSATERM PUBLIC SAFETY INC. (2300 Carling Ave, Ottawa ON K2B 7G1) — CAD software / mobile data system — USD 1,056,062 — 2023-08-14 → 2027-08-31 — ongoing
- `us_county_sacramento_ca:WA00045403` SODALES SOLUTIONS (100 King St W Suite 5700, Toronto ON M5X 1C7) — implementation milestones — USD 1,058,998 — 2024-04-30 → 2027-04-29 — ongoing
- `us_county_sacramento_ca:MA00043326` VERTIGIS NORTH AMERICA LTD. (300-1117 Wharf St, Victoria BC V8W 1T7) — GCX Enterprise maintenance years 1–5 — USD 60,483 — 2022-11-02 → 2027-12-17 — ongoing
- `us_county_sacramento_ca:PO:CA81535591` VERSATERM PUBLIC SAFETY INC. — PO 2026-07-22 — USD 402,746 — end_date_unknown
- `us_county_sacramento_ca:PO:CA81519624` TRANSOFT SOLUTIONS INC (US) (601 W Hastings St, Vancouver BC V6B 1M8) — AutoTURN / AviPLAN licences — USD 93,927 — 2025-11-01 — end_date_unknown

## Gaps
Department/buyer unit not published; outline-agreement values are sums of item effective prices (some items carry a placeholder price of 1). Earlier POs (2009–2025-10) excluded under the 12-month rule.
