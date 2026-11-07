# UNOPS contract awards

URL: `https://data.unops.org`
API endpoint: `https://api.data.dev.unops.org/api/v1/unops-data-dev/journey_project_contract_table_001`

- Filtered out records without Canadian supplier using `Supplier_Country == CA` or `Supplier_Country_Description == CANADA`.
- Paging was implemented by fetching chunks sorted by Contract ID and processing unique records.
- 14 Canadian records found.
