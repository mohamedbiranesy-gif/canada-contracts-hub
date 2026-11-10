# Canadian municipal purchase-order datasets on open-data portals

## Method
Sweep of Socrata open data portals for Canadian municipalities searching for purchase orders datasets.
Found datasets on Edmonton's portal (`data.edmonton.ca`):
- `y9rm-5xha`: Purchase Orders Over $10,000
- `ydv5-y4pu`: Outline Agreements over $10,000
- `gnse-cass`: Hired Equipment Contracts over $10,000

The portal has no explicit vendor address/country fields. We use the Canadian vendor dictionary `contrib/claude/buyer_pages/vendors_ca.tsv.gz` to determine if a supplier is a verified Canadian vendor by checking exact match on the supplier name.

Socrata's internal `:id` is mapped to both `po_number` in `contract.identifiers` and used as the `record_id` suffix as no explicit PO number column is provided.

## Stats
- Total rows seen: 10,574
- Canadian vendor rows (dictionary match): 3,623
- Ongoing rows (with explicit end dates later than the reference date): 6

Most rows have no explicit end date, and thus their status is `end_date_unknown` rather than `ongoing`. Historical rows where the end date is past the reference date are also kept as `end_date_unknown` for posterity in tracking contracts.

## Quirks
- The `validity_period_end` or `create_date` provide dates. If "end" is in the column name, it's used to calculate "ongoing" status.
