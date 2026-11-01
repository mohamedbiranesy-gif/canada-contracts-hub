# PSPC standing offers and supply arrangements

## Dataset details
- Publisher: Public Services and Procurement Canada
- Resources:
  - `tpsgc-pwgsc_ocama-sosa.csv` (Active SOSA dataset: f5c8a5a0-354d-455a-99ab-8276aa38032e)
  - `contractHistoryComplete-contratsOctroyesComplet.csv` (CanadaBuys contract history)
  - `awardNoticeComplete-avisAttributionComplet.csv` (CanadaBuys award notices)
  - `2009-2023-contractHistoryHistorical-contratsOctroyesHistorique.csv` (Legacy CanadaBuys contract history)
  - `2012-2022-awardNoticeHistorical-avisAttributionHistorique.csv` (Legacy CanadaBuys award notices)

## Record linking
The active SOSA dataset does not contain supplier address data. The script connects active SOSAs to CanadaBuys historical records to obtain vendor locations.
To get a full history of SOSAs, the script also extracts all agreements with instrument type "Standing Offer" or "Supply Arrangement" from the historical and legacy files.

## Coverage and Logic
- **Canadian vendor logic:** Vendor country is determined by linking the agreement number to CanadaBuys records. Records are kept if the country parses as Canada (`supplierAddressCountry-fournisseurAdressePays-eng` / `fra` or postal code).
- **Status rules:**
  - `ongoing`: explicit `contractEndDate` or `expiry-date` is on or after the reference date (2026-10-31).
  - `end_date_unknown`: `contractEndDate` is blank/missing and not available in SOSA.
  - Excluded: End date before reference date or start date after reference date.
- **Link construction:** Links to the legacy notices are built as `https://canadabuys.canada.ca/en/tender-opportunities/award-notice/<referenceNumber_lowercased>` where possible.

## Row counts
- Active SOSA Agreements processed: 3,981
- Historical CanadaBuys Agreements processed: 9,514
- Total output records (Canadian vendor, valid status): 7,164
- `ongoing`: 7,149
- `ongoing_inferred`: 15
