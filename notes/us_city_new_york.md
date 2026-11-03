# Recent Contract Awards (City of New York)

- **URL:** https://data.cityofnewyork.us/resource/qyyg-4tf5.json
- **Publisher:** City of New York
- **Description:** Recent Contract Awards list containing basic information about contract awards in New York City.
- **Coverage:** US City
- **Method:** Fetched Socrata resource using a SoQL `$where` clause filtering for 'CANADA' in the `vendor_address` column. `https://data.cityofnewyork.us/resource/qyyg-4tf5.json?$where=upper(vendor_address)%20like%20'%25CANADA%25'&$limit=50000`
- **Stats:**
    - Raw hits: 40
    - Canadian vendor matches: 40 (based on `CANADA` string matching in `vendor_address`)
    - Ongoing/Recent matches: 2 (2024 and 2026 awards)
- **Status Basis:** The dataset has `start_date` and `end_date`, but many records have the exact same date for both which effectively serves as the award date. In those cases (and when there is only an event date), we use the 3-year stale cutoff rule, marking recent ones as `end_date_unknown`. Records with distinct start/end dates are evaluated against the reference date.
- **Link construction:** `link_type` is set to dataset and the link points to the individual record's JSON via `request_id`.
