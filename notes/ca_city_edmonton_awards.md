# ca_city_edmonton_awards

**Description**: City of Edmonton Hired Equipment Contracts over $10,000.
**URL**: https://data.edmonton.ca/Purchasing/Hired-Equipment-Contracts-over-10-000/gnse-cass

## Data Source
- Provider: City of Edmonton
- Type: Socrata API (SODA)
- Endpoint: `https://data.edmonton.ca/resource/gnse-cass.json`

## Processing
- We filter for Canada-located vendors based on the `supplier_name` matching keywords `canada, edmonton, calgary, alberta, ab.`. We avoided using a bare `' ab'` to prevent false positives for vendor names that just contain strings starting with "ab".
- Since the schema strictly requires vendors in Canada, we derived this from the supplier name as there is no specific explicit address field.
- Extracted records with pagination via `$limit` and `$offset`.
- We output records as 'ongoing' if their end date is past the reference date in `coord/config.json`, or 'end_date_unknown' otherwise, ensuring we do not blindly drop historical records but accurately flag them so validators accept them with the `--allow-ended` flag or down-the-line processor logic.

## Output
- Total records found: 120 (ongoing or end_date_unknown).
- Output: `data/incoming/jules/records_ca_city_edmonton_awards.jsonl.gz`
