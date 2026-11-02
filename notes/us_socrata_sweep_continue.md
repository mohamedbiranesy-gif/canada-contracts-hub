# US Socrata Sweep Continue

## Endpoint and Parameters
- **Source**: Various US Socrata datasets discovered via `out.jsonl` (generated from `scripts/us_discovery_sweep`).
- **Endpoint**: `https://{domain}/resource/{dataset_id}.json`
- **Parameters**: `?$where=...&$limit=50000`. The WHERE clause filters dynamically on the discovered location columns (e.g. `upper(location_col) in ('CA', 'CAN', 'CANADA', 'CDN')` for country, or province abbreviations for state columns).

## Fields Used
- **Buyer**: Extracted from columns like `dept_name`, `agency`, `buyer`, or defaults to the dataset publisher's domain name if no explicit column is found. Website is extracted if a `url` or `website` field is present.
- **Vendor**: Extracted from columns matching `vendor`, `supp`, `payee`, `contractor`, or `name`.
- **Location**: Extracted dynamically based on the Socrata discovery phase which classifies columns into `country`, `state`, `zip`, `city`, and `address`. Uses `sweeplib.canadian` for strict filtering.
- **Dates**: Infers start, end, and award dates from column names containing `start`, `end`, `award`, `date`, etc.
- **Value**: Infers value from columns containing `amount`, `value`, `cost`, `total`, or `price`.
- **Description**: Infers description/title from columns containing `desc`, `title`, or `purp`.

## Counts
- **Total rows written (Canadian vendors & ongoing/inferred)**: ~1,561 records across 32 candidate datasets.

## Quirks
- The Socrata API query uses dynamic `$where` filters constructed based on the column classification. If a column isn't found, it might return a 400 Bad Request error. We catch this and continue.
- Status logic: For datasets seemingly containing payments/checkbook data (no end date), we use a 12-month activity window `end_date_unknown` logic via `sweeplib.status_activity`. Otherwise, we use standard contract term logic (`sweeplib.status_contract`).
- If no explicit buyer name column is identified, it defaults to the capitalized domain of the publisher (e.g., `Data` for `data.bayareametro.gov`).
