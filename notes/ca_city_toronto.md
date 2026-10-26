# ca_city_toronto — City of Toronto, Toronto Bids Awarded + Non-Competitive Contracts (open data)

Status: COMPLETE. Output ONLY `normalized/ca_city_toronto_unverified_country.jsonl` (10,728 records) — the
`Supplier Address` column exists in both datasets but is EMPTY in every row (checked 7,786 + 3,027 rows), so vendor
country cannot be established.

## Source (Open Data Toronto, CKAN)
- Toronto Bids Awarded Contracts — https://open.toronto.ca/dataset/tobids-awarded-contracts/
  datastore dump `https://ckan0.cf.opendata.inter.prod-toronto.ca/datastore/dump/e211f003-5909-4bea-bd96-d75899d8e612`
  -> `downloads/ca_city_toronto/awarded-contracts-datastore.csv` (2.26 MB, 7,786 rows; also `awarded-contracts.csv`
  and `.json` resource copies, identical content). Resource last modified 2026-10-22. Award dates 2010-04-15 .. 2026-10-13.
  Fields: _id, Document Number, RFx (Solicitation) Type, High Level Category, Successful Supplier, Award,
  Award Authority Obtained Date, Division, Buyer Name, Buyer Email, Buyer Phone Number,
  Solicitation Document Description, Supplier Address (empty), Wards.
- Toronto Bids Non-Competitive Contracts — https://open.toronto.ca/dataset/tobids-non-competitive-contracts/
  `.../resource/56938e5b-f17c-4b10-a4e8-360164f35a99/download/non-competitive-contracts.csv` (321 KB, 3,027 rows;
  Contract Date 2013-01-01 .. 2026-12-18). Fields: _id, Workspace Number, Reason, Contract Date, Supplier Name,
  Contract Amount, Division, Supplier Address (empty), Wards.
- Downloaded 2026-10-25T17:18:50Z–17:19:07Z. Script `scripts/ca_city_toronto/normalize.py` (uses shared
  `scripts/_muni/terms.py`); stats in `downloads/ca_city_toronto/normalize_stats.json`.

## Canadian vendor
Not published -> `vendor.country = null`, `country_basis = "not published (Supplier Address column empty)"`.

## Ongoing logic
- Awarded: parse `Solicitation Document Description` for an explicit period ("from October 1, 2012 to February 28,
  2014", "until …") -> `ongoing` if end ≥ 2026-10-25 (excluded if ended: 82); else a stated term ("for a period of
  three (3) years", "five year contract") added to Award Authority Obtained Date -> `ongoing_inferred`;
  else `end_date_unknown`.
- Non-competitive: only Contract Date -> `end_date_unknown`; Contract Date after ref excluded (3).
- One record per row (each row = one supplier award line): `ca_city_toronto:awarded:<_id>` / `ca_city_toronto:noncompetitive:<_id>`.

## Counts
ongoing 2; ongoing_inferred 46; end_date_unknown 10,680 (awarded 7,656 + non-competitive 3,024).
Note: many end_date_unknown rows are old (2010–2019) awards that have almost certainly ended; they are kept per
the schema rule (nothing published about the end) — downstream users should filter on `contract.dates.awarded`.

## record_url
None (the open-data rows have no per-record page; the Ariba/Toronto Bids portal pages need login).

## Samples
- ca_city_toronto:awarded:77 | ongoing_inferred | City of Toronto - Technology Services | RUTHERFORD CONTRACTING LTD | 19,800,000 | 2024-05-08 -> 2027-05-08
- ca_city_toronto:awarded:92 | ongoing_inferred | Corporate Real Estate Management | GREATER TORONTO FIRE PROTECTION | 4,878,357 | 2024-12-23 -> 2027-12-23
- ca_city_toronto:awarded:62 | ongoing_inferred | Fire Services | CONCEPT CONTROLS INC | n/a | 2026-03-18 -> 2027-03-18
- ca_city_toronto:awarded:5000 | end_date_unknown | Fire Services | AJ Stone Company Ltd. | 225,399 | awarded 2019-05-14
- ca_city_toronto:noncompetitive:1 | end_date_unknown | Toronto Water | Accuworx Inc | 67,896.40 | 2015-07-29

## Known gaps
No supplier address; no per-record URL; TTC, Toronto Hydro, TCHC etc. not in these datasets (TTC awards appear in ca_merx).
