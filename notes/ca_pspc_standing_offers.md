# Source: PSPC standing offers and supply arrangements (ca_pspc_standing_offers)

## Endpoints and Data Flow
- **Active SOSA File:** `https://sosa.canadabuys.canada.ca/cds/opendata/tpsgc-pwgsc_ocama-sosa.csv`
  - Published by Public Services and Procurement Canada via Open.Canada.ca
  - Dataset URL: `https://open.canada.ca/data/en/dataset/f5c8a5a0-354d-455a-99ab-8276aa38032e`
- **CanadaBuys Historical Matching:**
  - Because the active SOSA file does not contain vendor addresses, this script acts as an extension to `ca_canadabuys_contract_history`.
  - It streams `data/incoming/jules/records_ca_canadabuys_contract_history.jsonl.gz`, extracting records that are standing offers or supply arrangements (`instrument_type == 'SOSA' / 'standing offer' / 'supply arrangement'` or contract numbers starting with `CW` / `EN`).
  - Active SOSA rows are parsed to fetch up-to-date `award-date` and `expiry-date`.
  - Historical SOSA records missing from the active SOSA file but present in CanadaBuys are preserved (full history).

## Fields & Quirks
- **SOSA matching:** Uses the base `agreement-number` (e.g. `CW2367526` or `EN...`) to correlate records from the active file to CanadaBuys historical data.
- **End Dates:** If a standing offer appears in the active file, its end date is pulled and will override the CanadaBuys historical end date if the active one is further in the future.
- **Excluded Records:**
  - Active SOSAs without a match in CanadaBuys are skipped, since vendor location cannot be established.
  - SOSA records that have ended prior to the `REF_DATE` (`2026-10-31`) are excluded.

## Row Counts (Reference Date: 2026-10-31)
- **Active SOSAs Downloaded:** 3,981
- **Matched against active file:** 167
- **Historical only:** 4,142
- **Valid ongoing:** 2,919
- **End date unknown (ongoing_inferred fallback):** 1,385
- **Total Valid Output Rows:** 4,304
