# ca_pspc_standing_offers

- **Publisher**: Public Services and Procurement Canada (PSPC)
- **Dataset Name**: Active Standing Offers and Supply Arrangements (SOSA)
- **URL**: https://open.canada.ca/data/en/dataset/f5c8a5a0-354d-455a-99ab-8276aa38032e
- **Endpoint**: `https://sosa.canadabuys.canada.ca/cds/opendata/tpsgc-pwgsc_ocama-sosa.csv`

## Processing Notes
The primary dataset (SOSA) does not natively include supplier addresses. To fulfill the strict "Canadian vendors only" requirement where the country is based on source fields, the script fetches CanadaBuys legacy award notices (`https://canadabuys.canada.ca/opendata/pub/2012-2022-awardNoticeHistorical-avisAttributionHistorique.csv`) and CanadaBuys legacy contract history (`https://canadabuys.canada.ca/opendata/pub/2009-2023-contractHistoryHistorical-contratsOctroyesHistorique.csv`). It cross-references the CW numbers to find explicit Canadian addresses for the vendors. Records that cannot be verified against these legacy files with a Canadian address are excluded.

## Statistics from sample run:
- SOSA Rows seen: 6842
- Agreements parsed: 3981
- Excluded due to no Canadian address in legacy records: 3803
- Output Records: 178

## Fields Kept/Derived:
- **`vendor_country`**: CA (validated via CanadaBuys legacy datasets)
- **`vendor_country_basis`**: explicitly derived from `supplierAddressCountry` or `supplierAddressPostalCode` in legacy records.
- **`buyer`**: End-user entity or "Public Works and Government Services Canada".
- **`dates`**: Taken from SOSA start/expiry dates. Expiry year >= 2100 is treated as a placeholder (`end_date_unknown`).
