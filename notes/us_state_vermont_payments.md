# Vermont Vendor Payments (data.vermont.gov)

- **Source Type:** Open Checkbook (Socrata API)
- **URL:** https://data.vermont.gov/d/786x-sbp3
- **Query:** `https://data.vermont.gov/resource/786x-sbp3.json` filtered for `state` using Canadian provinces (`ON`, `QC`, `BC`, `AB`, `MB`, `SK`, `NS`, `NB`, `NL`, `PE`, `YT`, `NT`, `NU`).
- **Fields:** `qtrending` (date), `govtunit` (buyer dept), `vendor` (vendor name), `city`, `state` (vendor location), `amt` (value).
- **Quirks:**
  - `govtunit` lacks "State of Vermont" prefix, so it is prepended.
  - Payment date uses `qtrending` (Quarter ending).
  - Used `vno` + `qtrending` + `amt` to synthesize a unique `record_id`.
- **Row count:** 2020 Canadian vendor payments found.
