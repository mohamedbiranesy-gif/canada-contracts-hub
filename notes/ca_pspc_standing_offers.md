# ca_pspc_standing_offers

## Overview
This dataset contains active Standing Offers and Supply Arrangements from PSPC.

## Endpoints
Dataset URL: https://open.canada.ca/data/en/dataset/f5c8a5a0-354d-455a-99ab-8276aa38032e
Resource URL: https://sosa.canadabuys.canada.ca/cds/opendata/tpsgc-pwgsc_ocama-sosa.csv

## Stats
- Rows seen: 6842
- Agreements: 3981
- Canadian-vendor rows: 0 (the dataset doesn't have an address, needs matching with other sets)
- Ongoing rows: 3859

## Record URL
No distinct record URLs are available; everything comes from the CSV.

## Quirks
The source file doesn't have a vendor location. We rely on matches with the canada_federal and canada_federal_legacy datasets to determine if a supplier is in Canada.
