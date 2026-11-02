# US Socrata Sweep Continue

- Source Key: `us_socrata_sweep_continue`
- Target: Various Socrata open data portals in the US (state and local levels)
- Method:
  1. `scraper.py` enumerates the datasets matching "procurement", "contracts", "vendors", etc.
  2. Uses SoQL `$where` to filter the data on server-side to limit results to those with location matching Canadian provinces, states, postal codes, and countries (`CAN`, `CANADA`, `CA`, etc.).
  3. The datasets pulled down generated a total of 214 valid contract records with Canadian vendors, ignoring some Socrata APIs that threw HTTP 400 Bad Requests due to schema variations.
- Quirks: Some endpoints (e.g. data.ny.gov) threw 400 errors likely due to bad queries matching old schema enums. These were skipped, but 214 records were obtained from a few cities.
- Result: 214 rows extracted.
