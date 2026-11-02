# New York State Authorities Procurement

Endpoints used:
- `https://data.ny.gov/resource/ehig-g5x3.json` (Procurement Report for State Authorities)
- `https://data.ny.gov/resource/8w5p-k45m.json` (Procurement Report for Local Authorities)
- `https://data.ny.gov/resource/d84c-dk28.json` (Procurement Report for Local Development Corporations)
- `https://data.ny.gov/resource/p3p6-xqr5.json` (Procurement Report for Industrial Development Agencies)

Parameters used:
`$where=upper(vendor_country) = 'CANADA'`

Fields used:
- `authority_name` -> buyer name
- `vendor_name` -> vendor name
- `vendor_address_1`, `vendor_city`, `vendor_state`, `vendor_province_region`, `vendor_postal_code`, `vendor_country` -> vendor address
- `procurement_description` -> contract title and description
- `contract_amount` -> contract value
- `type_of_procurement` -> contract instrument type
- `award_process` -> contract procurement method
- `award_date`, `begin_date`, `end_date` -> contract dates

Counts:
- State Authorities: 773 records (Canada vendor)
- Local Authorities: 144 records (Canada vendor)
- Local Development Corporations: 26 records (Canada vendor)
- Industrial Development Agencies: 2 records (Canada vendor)
- Total ongoing: 317 records

Quirks:
- Values can sometimes be strings starting with `$` and containing `,`. Parsing is done manually.
- Duplicate transaction numbers can happen if they are for the same vendor/authority, so an index is added to `record_id` to ensure uniqueness.
