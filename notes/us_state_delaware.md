# us_state_delaware — Delaware Awarded Vendor Contact Info (statewide central contracts), vendor in Canada

Reference date 2026-10-25. Output: `/home/claude/contracts/normalized/us_state_delaware.jsonl` (**4 records**, all `ongoing`). Script: `scripts/us_state_delaware/normalize.py`.

## What was downloaded
- data.delaware.gov `h9bb-iyu6` "Awarded Vendor Contact Info" ("vendors currently under award for a contract with the State of Delaware"; landing https://data.delaware.gov/d/h9bb-iyu6), SODA JSON 2026-10-25 18:04:22 UTC → `downloads/us_state_delaware/awarded_vendor_contact_h9bb-iyu6.jsonl`, 2,911 rows. Columns: companyname, address1, address2, city, **state**, zipcode, website, contact1, phone1, fax1, email1, contracttitle, mwbecertified, vetservdisabled, delawarevendor, contracturl (mmp.delaware.gov/Contracts/Details/<id>), expiredate, geocoded_location, awarded_vendor, count.
- For each Canadian vendor, the contract page `https://mmp.delaware.gov/Contracts/Details/<id>` was fetched (18:22 UTC, saved under `downloads/us_state_delaware/pages/`, parsed into `contract_pages.jsonl`) to get the contract number, effective date and expiration date.

## Canadian vendor
`state` = 'ON' (D2L Ltd, Kitchener; ICOR Technology, Ottawa) or, where the state field is '--'/'NA', the address/city text contains "Canada" plus a province name/code and Canadian postal code (Umano Medical, L'Islet QC G0R 2C0; Waldale Manufacturing, Amherst NS B4H 4J6). Names never used; basis per record.

## Ongoing
Contract page Effective Date ≤ 2026-10-25 ≤ Expiration Date (and the dataset's expiredate agrees): D2L DTCC22322-LMS 2022-07-01 → 2027-06-30; Umano GSS25714-MATTRESS 2025-11-01 → 2027-10-31; Waldale DOT2607-LIC_PLATES 2025-08-26 → 2028-08-26; ICOR GSS22909-EOD_ROBOT 2022-06-29 → 2029-07-31. Record URL verified: https://mmp.delaware.gov/Contracts/Details/5633 → "Contract Status Details for EOD Robots GSS22909-EOD_ROBOT … Contract Effective Date 6/29/2022 Contract Expiration Date 7/31/2029".

## Gaps
Statewide central contracts only (not agency-specific contracts); no contract values published; vendor rows with state 'ON' but no country column (2 of 2,911) — plus two free-text Canadian addresses — were the only Canadian hits.
