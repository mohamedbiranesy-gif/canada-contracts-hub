# CanadaBuys legacy contract history (2009-2023)

## Dataset details
- Publisher: Public Services and Procurement Canada (CanadaBuys open data)
- Resources:
  - `2009-2023-contractHistoryHistorical-contratsOctroyesHistorique.csv` (dataset: 4fe645a1-ffcd-40c1-9385-2c771be956a4)
  - `2012-2022-awardNoticeHistorical-avisAttributionHistorique.csv` (dataset: a1acb126-9ce8-40a9-b889-5da2b1dd20cb)
- These files are the historical archive of PSPC contract history before the complete migration to CanadaBuys.

## Record linking
The legacy dataset is deduplicated against the modern `canada_federal` dataset.
Records are omitted if they have:
1. An exact identifier match to `canada_federal`
2. A match in the complete CanadaBuys files
3. A match in the proactive disclosure datasets

## Coverage and Logic
- **Canadian vendor logic:** The source provides a supplier address country field. Values are normalized. Records are kept if the country parses as Canada (`supplierAddressCountry-fournisseurAdressePays-eng` / `fra`).
- **Status rules:**
  - `ongoing`: explicit `contractEndDate` is on or after reference date 2026-10-25.
  - `end_date_unknown`: `contractEndDate` is blank/missing.
  - Excluded: End date before reference date.
- **Link construction:** Links to the legacy notices are built as `https://canadabuys.canada.ca/en/tender-opportunities/award-notice/<referenceNumber_lowercased>` where possible.

## Row counts
- Total candidates linked: ~18,700
- Kept: 18,575 distinct contract records
- `ongoing`: ~4,000
- `end_date_unknown`: ~14,600
