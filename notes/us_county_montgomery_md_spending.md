# us_county_montgomery_md_spending — Montgomery County, Maryland "County Spending" (payments) with Canadian vendor postal codes

Reference date 2026-10-25. Output: `/home/claude/contracts/normalized/us_county_montgomery_md_spending.jsonl` (**16 records**: 1 `ongoing`, 15 `end_date_unknown`). Script: `scripts/us_county_montgomery_md_spending/normalize.py` (`python3 -I normalize.py <spending.jsonl> <contracts_vmu2-pnrc.csv> <us_county_montgomery_md.jsonl> <out.jsonl>`). Complements `us_county_montgomery_md` (active Contracts list, 3 records), which it de-duplicates against.

## What was downloaded
- dataMontgomery `vpf9-6irq` "County Spending" (payment lines; columns fiscal_year(_period), service, department, program, fund, category, expense_category, account_code, description, vendor, vendor_id, **vendor_zip**, contract_num, po_num, po_line, invoice_id/line/distribution_line, amount, inv_date, payment_method, payment_date, payment_id, payment_status; landing https://data.montgomerycountymd.gov/d/vpf9-6irq), SODA 2026-10-25T20:01:57Z with `upper(vendor_zip) >= 'A' and upper(vendor_zip) < 'ZZ' and payment_date >= '2025-10-25'` → `downloads/us_county_montgomery_md_spending/spending_alphazip_vpf9-6irq.jsonl` (102 rows).
- The active Contracts list `vmu2-pnrc` already downloaded for `us_county_montgomery_md` (`downloads/us_county_montgomery_md/contracts_vmu2-pnrc.csv`, 2026-10-25 17:25:53 UTC) is used to attach contract terms by contract_num.

## Canadian vendor
vendor_zip must be a full Canadian postal code (A1A 1A1, space optional): P3C 4J2 (Sudbury), H3B 3Z4, V6E 4M3, M5S 2B1, L4L 5Y2, T2H 2G4, L1S6W1, M5W 3W5. Excluded alphabetic zips: "WC2H 9EA" (London UK, Marathon Asset Management), "MD 20912-6627", "MD", "MD 21221" (US).

## Ongoing
Rows grouped per (vendor_id, contract_num | po_num | department) with all lines in `raw.rows`. If contract_num is in the active Contracts list: dates from Execution/Expiration Date → `ongoing` (1: The Hanen Centre contract 1194304, 2026-07-06 → 2027-06-30; the list's own address for it is coded "MD" with zip "M4PY1", so it was missed by the state-field filter of `us_county_montgomery_md`); contracts already emitted by `us_county_montgomery_md` are skipped (Pro-Bel 1190500). Otherwise `end_date_unknown` (payments within the 12 months before 2026-10-25; contract_num kept when present, e.g. Tristan Communications 1156861, not in the active list). value = Σ payment amount in the window. `record_url` null.

## Result: 16 records (1 ongoing, 15 end_date_unknown; USD 1.32 M of payments in 12 months)
Global Alpha Capital Management (Vancouver; investment manager, Non-Departmental/retirement funds) 3, Canadian Imperial Bank of Commerce (Montréal; investment manager services) 3, Northern Communications Services (Sudbury ON; Police / Correction 800-line answering service) 4, The Hanen Centre (Toronto; HHS speech-pathology training) 2, Tristan Communications (Vaughan ON; Alcohol Beverage Services), Waitwell Inc. (Calgary; Animal Services), Pro-Bel Enterprises (Ajax; General Services PO), Tumbleweed Press (Toronto; Public Libraries).

## Samples
- `us_county_montgomery_md_spending:58431-C1194304` The Hanen Centre — Health & Human Services — speech-pathologist training — 2026-07-06 → 2027-06-30 — ongoing
- `us_county_montgomery_md_spending:94422-C1156861` Tristan Communications Ltd. (L4L 5Y2) — Alcohol Beverage Services — supplies — USD 73,930 — end_date_unknown
- `us_county_montgomery_md_spending:88372-DNon-Departmental_Accounts` Global Alpha Capital Management Ltd. (V6E 4M3) — investment manager services — USD 621,181 — end_date_unknown
- `us_county_montgomery_md_spending:61552-P1194181` Northern Communications Services Inc (P3C 4J2) — Police — 800-line charges — USD 6,000 — end_date_unknown
- `us_county_montgomery_md_spending:102051-P1197376` Waitwell Inc. (T2H 2G4) — Office of Animal Services — USD 8,900 — end_date_unknown

## Gaps
Spending rows give only the vendor postal code (no street/city); city/province come from the Contracts list when the contract is active.
