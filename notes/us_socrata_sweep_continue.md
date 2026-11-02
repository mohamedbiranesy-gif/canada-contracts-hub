# US Socrata Sweep Continue

- Explored Socrata Discovery API based on keywords to find datasets related to contracts and purchasing.
- Applied column-level search using SoQL `$where` to detect datasets that have "Canada" or Canadian province / postal code formats in vendor state/country/zip columns.
- Excluded domains already covered by specific `us_*` and `ca_*` scrapers, as well as `data.colorado.gov`, `controllerdata.lacity.org`, `cthru.data.socrata.com`, `data.brla.gov`, `data.cityofchicago.org`, `data.cityofnewyork.us`, `corstat.coronaca.gov`, `data.montgomerycountymd.gov`, and `data.texas.gov`.
- Output: 101 records of ongoing/unknown-end-date contracts found with Canadian vendors.
- Saved to: `data/incoming/jules/records_us_socrata_sweep_continue.jsonl.gz`.
- Records passed schema validation perfectly.
