# us_county_montgomery_md — Montgomery County, Maryland active contracts, vendor state = Canadian province

Reference date 2026-10-25. Output: `/home/claude/contracts/normalized/us_county_montgomery_md.jsonl` (**3 records**, all `ongoing`). Script: `scripts/us_county_montgomery_md/normalize.py`.

## What was downloaded
- dataMontgomery dataset `vmu2-pnrc` "Contracts" ("lists all active County contracts, updated daily"; landing https://data.montgomerycountymd.gov/d/vmu2-pnrc → /Government/Contracts/vmu2-pnrc), CSV export 2026-10-25 17:25:53 UTC → `downloads/us_county_montgomery_md/contracts_vmu2-pnrc.csv`, 2,370 rows. Columns: Contract Number, SolicitationNumber, Buyer First/Last Name, BuyerPhone, BuyerEmail, BuyerTitle, ContractType, ContractDesc, Vendor, Vendor Address Line 1/2, Vendor City, **Vendor State**, Vendor Zip Code, Vendor Contact, Vendor Email, Vendor Phone Number, Non-Profit, DeptName, Division, Contract Administrator (+phone/email), Execution Date, Expiration Date, Extend Date, Prevailing Wage Contracts, Living Wage Contracts.

## Canadian vendor
`Vendor State` ∈ {ON, QC} (3 rows: ON 2, QC 1; Zip codes V7M1A5, H2W1Y5, L1S6W1). Note Epact Network Ltd is coded ON with a North Vancouver address/BC postal code — kept as published. Names never used.

## Ongoing
All three: Execution Date ≤ 2026-10-25 ≤ Expiration Date (dataset is active-only). `Extend Date` (latest option date) stored in `contract.related.extend_date`.

## Records
- us_county_montgomery_md:1171436 | Epact Network Ltd (North Vancouver, V7M 1A5) | Department of Recreation | Electronic Health Management Records Software | Non-Competitive - Council Resolution | 2025-06-02 → 2027-06-30 (extend to 2028-06-30)
- us_county_montgomery_md:1184626 | Eco-Counter Inc (Montreal QC H2W 1Y5) | Department of Transportation | data transmission/storage/maintenance for automated bike counters | Non-Competitive | 2026-06-17 → 2027-06-16 (extend to 2031)
- us_county_montgomery_md:1190500 | Pro-Bel Enterprises Limited (Ajax ON L1S 6W1) | Department of General Services | fall-protection equipment inspection/maintenance | Informal - Mini Contract | 2026-03-23 → 2027-03-22
No contract values are published (value null). No per-contract page (`record_url` null; contract copies via MPIA request).
