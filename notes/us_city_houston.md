# us_city_houston — City of Houston (data.houstontx.gov CKAN): checked, rejected

- "Checkbook" datastore resource 3c5f1f22-41c5-47cd-a4a2-235a90e80e09 (73,641 rows: Payment Document Number, Fund, Department, WBS, GL Account, **Vendor Name**, Vendor Invoice, Fiscal Year, Clearing Date, Amount, Type of procurement, Purchase Order Number/Item, Contract Number) and "All City of Houston Procurement Contracts" (0c93d5a2-…, 2,310 rows: Contract Name/Number, Expiration Date, Total Value/Spent/Remaining; last updated 2023) — inspected 2026-10-25 ≈19:28 UTC via `datastore_search?limit=1`.
- **No vendor address/state/country field** in either. Rejected (vendor country undeterminable without names).
