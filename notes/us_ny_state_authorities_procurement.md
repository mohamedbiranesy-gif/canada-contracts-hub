# New York State Authorities Procurement

Datasets:
- Procurement Report for State Authorities (ehig-g5x3)
- Procurement Report for Local Authorities (8w5p-k45m)
- Procurement Report for Local Development Corporations (d84c-dk28)
- Procurement Report for Industrial Development Agencies (p3p6-xqr5)
Publisher: New York State

This dataset contains a point-in-time snapshot of active contract records for NYS Authorities, including State Authorities, Local Authorities, LDCs, and IDAs.

## Method
* For each dataset, filtered on server-side using SoQL: `$where=upper(vendor_country) = 'CAN' OR upper(vendor_country) = 'CANADA' OR upper(vendor_country) = 'CA' OR upper(vendor_country) = 'ONTARIO, CANADA'`
* Total records matched:
  - state_authorities: 3519
  - local_authorities: 296
  - local_development_corps: 26
  - industrial_development_agencies: 2
* Filtered out records with an end date before the reference date (2026-11-02) and those with start dates in the future.
* Yielded 786 valid ongoing or end_date_unknown records across all sets.

## Quirks
* `vendor_country` is free-text and we fetch the CA / CAN / CANADA variants.
* `transaction_number` is often 'NONE' or not provided. To ensure unique `record_id`s, we create a stable SHA-256 hash using the dataset key, `authority_name`, `vendor_name`, `award_date`, `begin_date`, `end_date`, `contract_amount`, `amount_expended_for_fiscal_year`, `transaction_number` and `fiscal_year_end_date`. If collisions still occur, we append an incrementing number suffix.
* Monetary amounts can contain $ and comma characters; `parse_float` cleans them up.
* There is no direct link to a record so we link back to the source dataset URL for each record.

## Counts
* Canadian vendor rows: 3843
* Ongoing/unknown end date rows: 786
