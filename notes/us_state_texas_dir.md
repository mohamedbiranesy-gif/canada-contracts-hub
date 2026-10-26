# us_state_texas_dir — Texas DIR cooperative contracts (data.texas.gov), Canadian primary vendor

Reference date 2026-10-25. Output: `/home/claude/contracts/normalized/us_state_texas_dir.jsonl` (**1 record**, `ongoing`). Script: `scripts/us_state_texas_dir/normalize.py`.

## What was downloaded (2026-10-25 18:04 UTC, SODA)
- `vipt-h4ye` "Official - DIR Current Active Cooperative Contracts" (5,182 rows; vendor name, contact, contract_start, contract_termination_date, type/subtype; **no vendor address**) → `downloads/us_state_texas_dir/dir_active_contracts_vipt-h4ye.jsonl`.
- `w64c-ndf7` "ARCHIVE DIR Cooperative Contract Sales Data Fiscal 2010 To 2025" (10.6 M sales rows with vendor_address/city/**vendor_state**/zip): pulled only rows with a Canadian vendor_state (526 rows, 7 contract numbers) → `dir_sales_archive_ca_w64c-ndf7.jsonl`. Vendor_state values across the archive include ON 402, BC 124.
- `a743-wj72` (VSR sales FY2026+) was started and aborted: it has customer_state but no vendor address columns.

## Canadian vendor / ongoing
Join on contract_number: of the 7 Canadian-vendor contracts in the sales archive (Bonfire Interactive, ACL Services, NetCentric, WinMagic, CutCom, GTY Software, CommunityLogiq), only **DIR-CPO-5134 (CommunityLogiq Software Inc, 700 W Pender St, Vancouver BC)** is in the current active list: contract_start 2023-05-31, contract_termination_date 2027-05-31 (renewal exercised; expiration 2028-05-31 per DIR page). Record URL verified: https://dir.texas.gov/contracts/dir-cpo-5134 ("Contract Term Date: 05/31/27 … Contract Status: Active … CommunityLogiq Software Inc"). The other six expired (2013–2025).

## Gaps
DIR vendor addresses are only available through the sales archive; a Canadian vendor whose contract never had reported sales would be missed. LBB (Texas state contracts ≥ $50k) is covered separately in `us_state_texas_lbb`.
