# Manitoba government contract awards (proactive disclosure)

## Source
- URL: `https://web32.gov.mb.ca/DisclosureOfContracts/`
- Method: Uses the internal API endpoint `https://web32.gov.mb.ca/DisclosureOfContracts/json/en/contracts/ALL/CSV?year={year}&month=13` to download a CSV for each year (month=13 returns all months for the year).
- Paging: None. Loop over years (2014-2026).

## Notes
- The instruction states to prefer sources with high NEW distinct buyers. This source provides Manitoba ministries and departments.
- No `vendor_country` field exists, but the instruction is to infer from the dataset scope (build ON THE MAC / ca_manitoba_awards). Vendor country is set to `CA`.
- Buyer websites are not provided in this dataset.

## Counts
- Rows seen: ~3000
- Canadian-vendor rows: ~3000 (all assumed `CA`)
- Ongoing rows: ~2032 (due to most being `end_date_unknown` since `validityEnd` is missing for many, or actual `ongoing` if end date is provided).

## Quirks
- Has many duplicate contracts listed for different reporting periods or change dates. The ID is a compound of `contractNumber-reportingPeriod-changeDate`.
- No explicit single `record_url`, links to the dataset landing page.
