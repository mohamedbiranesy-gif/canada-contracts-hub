# us_state_portals

## Endpoints and parameters
- Data was pulled from Socrata endpoints `https://data.texas.gov/resource/w64c-ndf7.json` (ARCHIVE DIR Cooperative Contract Sales Data) using SoQL to query Canadian provinces directly to limit processing overhead.
- Other portals like CA eProcure and NY OpenBook datasets mentioned (w9ak-a7zi, n8q6-4twj, etc.) were either returning 404, connection reset, missing from the portal, or blocked.
- SoQL filter for Canada: `$where=vendor_state='PROV_CODE'`

## Fields
- vendor location fields: `vendor_state`, `vendor_country`
- status fields: `contract_start_date`, `contract_end_date`, `contract_termination_date`
- buyer information: `customer_name`, `customer_type`, `customer_city`, `customer_state`, `customer_zip`
- contract values: `purchase_amount`, `rfo_description`

## Rows
- Found 2 ongoing contracts with a Canadian vendor (BC) from the DIR dataset for Texas.

## Quirks
- CA eProcure returns `403 Forbidden`.
- NY OpenBook API returns connection reset.
- A lot of the NY datasets are missing from `data.ny.gov` (e.g. `ehig-g5x3` works but doesn't have an address, `w9ak-a7zi` is gone).
