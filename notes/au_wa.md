# au_wa — Tenders WA Contract Award Details (Western Australia)

Reference date 2026-10-25. Output `/home/claude/contracts/normalized/au_wa.jsonl`: **4 records, all `ongoing`**.

## Downloaded (2026-10-25 ~17:38 UTC, by the earlier worker; URLs re-confirmed via the data.wa.gov.au CKAN API at 19:4x UTC)
| file | URL | rows |
|---|---|---|
| downloads/au_wa/wa_2021_22.csv | https://catalogue.data.wa.gov.au/dataset/cab2f08c-6776-4328-b4b3-776f1f88eb3a/resource/2f29a5b8-ad39-465a-8374-84cbe5a2afc9/download/tenders-wa-contract-award-details-2021-22-financial-year.csv | 5,262 |
| downloads/au_wa/wa_2022_23.csv | https://catalogue.data.wa.gov.au/dataset/a66013f6-07db-433b-bc6a-984b249a1013/resource/063fa676-4ae3-48dd-ad0b-0e207182abf8/download/tenders-wa-contract-award-details-2022-23-financial-year.csv | 5,672 |
| downloads/au_wa/wa_2023_24.csv | https://catalogue.data.wa.gov.au/dataset/90b272e8-9ae0-4995-8dc9-86f8249b51d1/resource/855378f8-0398-4a0a-a1c2-218816508ec9/download/tenders-wa-contract-award-details-2023-24-financial-year.csv | 5,817 |
Only these three financial years are published on data.wa.gov.au (CKAN `package_search` for "tenders wa" returns no 2024-25 or earlier datasets).

## Canadian vendor
No country column. `Supplier_Address` (free text "street, city, postcode") whose final token is a Canadian postal code (regex `[ABCEGHJ-NPRSTVXY]\d[A-Z] ?\d[A-Z]\d` at end of string). 8 rows matched (Vancouver, Calgary, Fredericton, Edmonton, Toronto, Midland ON); none were ambiguous. Script `scripts/au_wa/normalize.py`.

## Ongoing
`Commencement_Date` (or `Award_Date`) ≤ 2026-10-25 ≤ `Final_Expiry_Date` (falls back to `Initial_Expiry_Date`). 4 ongoing; 4 excluded as ended (Hootsuite 2026-05-09, Deighton 2023-09-21, Aster Funds 2024-08-06, Rockwood Psychotherapy 2026-08-31).

## record_url
null — Tenders WA has no stable public per-contract URL derivable from the reference number (reference kept in identifiers; source CSV URL in `contract.related.source_csv`).

## Records
- au_wa:DBCARIAT1422 | Rentrax Software (Vancouver V6B 3K6) | Dept of Biodiversity, Conservation and Attractions | equipment-hire management & POS system | AUD 468,469 | 2022-07-04 → 2027-07-03
- au_wa:DPIRD2022111 | Growsafe Systems Ltd (Calgary) | Dept of Primary Industries and Regional Development | feed-efficiency system | AUD 350,000 | 2022-12-02 → 2027-12-01
- au_wa:RFP222020 | Remsoft Incorporated (Fredericton) | Forest Products Commission | forestry planning software | AUD 1,457,920 | 2022-07-06 → 2032-07-05
- au_wa:LAWADTP2205CGLPM2C | Riva International, Inc. (Edmonton) | Legal Aid Commission of WA | client/grants/legal practice management solution | AUD 909,365 | 2023-07-17 → 2033-07-16

## Gaps
Contracts awarded before 1 July 2021 or after 30 June 2024 are not in the open data. Addresses without a postal code would be missed.
