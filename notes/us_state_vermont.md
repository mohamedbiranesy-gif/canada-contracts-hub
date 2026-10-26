# us_state_vermont — State of Vermont "Purchase Orders with Vendor Information" (data.vermont.gov) + contract registers checked

Reference date 2026-10-25. Output: `/home/claude/contracts/normalized/us_state_vermont.jsonl` (**355 records**, all `end_date_unknown`: 347 from purchase orders + 8 from quarterly vendor payments). Script: `scripts/us_state_vermont/normalize.py` (`python3 -I normalize.py <po_ca_8ewu-igdm.jsonl> <out.jsonl> <payments_ca_786x-sbp3.jsonl>`), grouping helper `scripts/us_common/po_group.py`.

## What was downloaded (SODA, `scripts/us_common/soda_pull.py`, 2026-10-25T19:20:03Z–19:20:10Z UTC)
- `8ewu-igdm` "Purchase Orders with Vendor Information" (150,758 rows; PO dates 2025-07-02…2026-09-29; columns po_id, business_unit, business_unit_descr, po_date, line, item, item_long_descr, po_qty, merchandise_amt, supplier, vendor_name, city, **st**), filtered `st in (province codes)` → `downloads/us_state_vermont/po_ca_8ewu-igdm.jsonl` (534 rows). Landing https://data.vermont.gov/d/8ewu-igdm.
- `786x-sbp3` "Vermont Vendor Payments" (2.59 M rows, quarterly, vendor city/**state**), Canadian rows → `payments_ca_786x-sbp3.jsonl` (2,019 rows, 2009–2026). Used to collect Canadian vendor numbers and, on resume, for payment-derived records (see below).
- `fxu3-43sg` "Active Vendors" (2024 snapshot, city/st/postal), Canadian rows → `active_vendors_ca_fxu3-43sg.jsonl` (92).
- Contract registers pulled in full: `dz5q-8uqb` "Executed Contracts for Service" (6,614 rows; start_date/exp_date/max_amount; last updated 2024-01) and `errv-rz95` "Contract List" (2,034 rows; last updated 2018) → `executed_contracts_dz5q-8uqb.jsonl`, `contract_list_errv-rz95.jsonl`. Joined on vendor number (leading zeros stripped) to the 272 Canadian vendor numbers: 12 + 7 matches, **all expired** before the reference date (registers are stale), so no `ongoing` records.

## Canadian vendor
`st` field of the PO dataset = Canadian province code (QC 478, ON 40, MB 6, …). City kept in vendor.address.

## Ongoing
POs carry no term. One record per (business_unit, po_id) with all lines in `raw.rows`; kept iff po_date within 2025-10-25…2026-10-25 → 347 of 357 POs (10 older). value = sum of merchandise_amt. No per-record page (`record_url` null).

## Payment-derived records (added on resume)
From `786x-sbp3` (columns qtrending (quarter end), govtunit, unitno, vno, vendor, city, **state**, description, objcode, amt, account, acctno, fund_description, fund): rows with a quarter ending within 2025-10-25…2026-10-25 (78 rows: quarters 2025-12-31, 2026-03-31, 2026-06-30), grouped by (vno, unitno). Skipped: one-time payees with vno = `SINGLE` (DMV/IFTA refunds) and individuals ("Surname,Given"), and pairs that already have a PO record (9). **8 records** `us_state_vermont:PAY-<unitno>-<vno>`: Drivewyze Ltd. (Edmonton AB; Transportation Agency/DMV, USD 1,635,000), ET Group (Etobicoke ON; Judiciary, USD 155,054), Global Online Learning Discussion (Vancouver; Health), OrgCode Consulting (Oakville; Housing & Conservation Board), Dunsky Energy & Climate Advisors (Montréal; Joint Fiscal Office), Caseware International (Toronto; Auditor of Accounts), Comtec Systems (Victoria BC; Crime Victims' Services), University of Toronto Press.

## Result: 355 end_date_unknown (347 PO-based, USD 7.82 M; 8 payment-based, USD 1.80 M)
Compass Minerals America Inc (Repentigny QC; road salt for VTrans garages) 294; Innovative Surface Solutions 18; Eco-Counter (Montréal) 5; Pollard Banknote (Liquor & Lottery) 5; Allerair Industries 5; CIDEP 4; Deighton Associates (Whitby ON; VAMIS) 3. Buyers: Transportation Agency 320, Liquor & Lottery 5, Education 5, Fish & Wildlife 4.

## Samples
- `us_state_vermont:08100-0000002708` Eco-Counter Inc (Montreal QC) — Transportation Agency — Evo counter — USD 7,035 — 2025-11-17
- `us_state_vermont:08100-0000006686` Compass Minerals America Inc (Repentigny QC) — Transportation Agency — salt 90.76 t — USD 8,145 — 2026-03-10
- `us_state_vermont:08100-0000008327` Compass Minerals America Inc — salt 165.6 t Island Pond garage — USD 16,017 — 2026-04-29
- `us_state_vermont:02320-0000002157` Pollard Banknote Limited (Winnipeg MB) — Department of Liquor & Lottery — lottery tickets — USD 700,000 — 2026-01-22
- `us_state_vermont:08100-0000002975` Innovative Surface Solutions (Ajax ON) — Transportation Agency — ProMelt for district garages — USD 8,708 — 2025-11-21
- `us_state_vermont:PAY-08100-0000422410` Drivewyze Ltd. (Edmonton AB) — Transportation Agency (Department of Motor Vehicles) — quarterly payments — USD 1,635,000

## Gaps
Vendor address = city + province only. Compass Minerals America's Canadian address is the address on the Vermont vendor record (Repentigny QC) — kept as published. Contract registers are stale (2018/2024), so long-term Vermont contracts with Canadian vendors are not visible.
