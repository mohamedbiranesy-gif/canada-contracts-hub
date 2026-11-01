Endpoint: open.canada.ca dataset f5c8a5a0-354d-455a-99ab-8276aa38032e
Fields: SOSA columns + CanadaBuys complete/legacy row info
Counts:
Rows seen: 6842
Canadian-vendor rows: 3568 (extracted)
Ongoing rows: 3553 ongoing
Quirks:
- Added `https://buyandsell.gc.ca/procurement-data/standing-offers-and-supply-arrangements/{agreement_number}` link format
- Handled missing buyer names by setting it to "Public Services and Procurement Canada"
- Extends the existing `canada_sosa` pipeline to full history and ends dates lookup in CanadaBuys databases.
