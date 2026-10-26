# us_state_massachusetts — CTHRU Comptroller of the Commonwealth Spending, vendor state = Canadian province

Reference date 2026-10-25. Output: `/home/claude/contracts/normalized/us_state_massachusetts.jsonl` (**58 records**, all `end_date_unknown`). Script: `scripts/us_state_massachusetts/normalize.py`.

## What was downloaded
- CTHRU (Massachusetts Comptroller's open records platform, Socrata domain cthru.data.socrata.com), dataset `pegc-naaa` "Comptroller of the Commonwealth Spending" (49.2 M payment rows; landing https://cthru.data.socrata.com/d/pegc-naaa → /Government/Comptroller-of-the-Commonwealth-Spending/pegc-naaa). Columns: base_id, budget_fiscal_year, fiscal_period, date, cabinet_secretariat, department(_code), appropriation_type/name/code, object_class, object_code, object, **encumbrance_id** (MMARS contract/PO document reference, e.g. `(CT) 2024RLDATIXPEERSUPP0`, `(GAE) 25USASDS000000000000`, `(PC) 7000PCMCB43306254022`), zip_code, amount, fund(_code), vendor, vendor_id, payment_id, payment_method, **state, city**, create_date.
- Pulled via SODA `$where=state in (provinces) AND budget_fiscal_year >= 2025` (`scripts/us_common/soda_pull.py`, 2026-10-25 18:27:51 UTC) → `downloads/us_state_massachusetts/cthru_spending_ca_pegc-naaa.jsonl`, 1,206 rows (FY2025 550, FY2026 633, FY2027 23).
- COMMBUYS (www.commbuys.com/bso) public contract records were checked: the site loads, but contract search is a JSF session app with no bulk export and vendor addresses only inside each contract page; not pulled (see `notes/us_state_massachusetts.md` gaps).

## How "Canadian vendor" was determined
Structured vendor address `state` field ∈ {ON, PQ, BC, AB, QC, …} (values seen: ON 598 rows FY2026, BC, AB, QC/PQ). Cities include Ajax, Toronto, Ottawa, Sidney BC, Drummondville, Edmonton, Barrie; `city` sometimes literally "CANADA". Names never used.

## How "ongoing" was determined
Payment-level data without contract dates. One record per (encumbrance_id, vendor, department) with all payments in `raw.rows`; kept as `end_date_unknown` iff the latest payment date is within the 12 months before the reference date (58 of 110 encumbrances; 52 excluded). The MMARS encumbrance document type is parsed from the id (`CT` contract, `GAE` general accounting encumbrance, `PC` purchase/contract, `RPO`…) into `contract.identifiers.encumbrance_document_type`.

## Record construction
`record_id` = `us_state_massachusetts:<sanitised encumbrance id : vendor : dept code>`; buyer = "Commonwealth of Massachusetts - <department>" with cabinet secretariat; value = sum of payments FY2025+; dates.start = first payment, amended_last = last payment. No per-encumbrance page (`record_url` null).

## Counts
58 end_date_unknown. Buyers: Mass. Commission for the Blind 11 (HumanWare, Drummondville QC: assistive equipment), MassDOT 11 (Innovative Municipal Products (US) Inc, Ajax ON: road salt/liquids), Worcester Sheriff 5, DYS 4 (Multi-Health Systems, Toronto), Gaming Commission 3, State Police 3 (Guardian Mobility, Ottawa). Sum of payments USD 2.92 M.

## 5 samples
- us_state_massachusetts:_CT_2024RLDATIXPEERSUPP0_… | RLDATIX NORTH AMERICA INC. (Toronto, PQ) | Center for Health Information & Analysis | (U12) IT cloud services | USD 10,986 | 2024-12-13 → last paid 2025-12
- us_state_massachusetts:_CT_09052500000000000331_… | LIDD CONSULTANTS INC. (QC) | Massachusetts State Lottery | (U11) IT contract services | USD 56,037.50 | from 2025-10-01
- us_state_massachusetts:_GAE_POPOL711026GUARDI000_… | GUARDIAN MOBILITY CORP (Ottawa ON K2E 7…) | Department of State Police | subscriptions/licensing | USD 11,956 | 2025-07-23
- us_state_massachusetts:_CT_2022CARLETONUNIVERSI_… | CARLETON UNIVERSITY (Ottawa ON K1S 5B6) | Massachusetts Gaming Commission | management consultants (research) | USD 13,981 | 2024-11-04
- us_state_massachusetts:_PC_7000PCMCB43306254022_… | HUMANWARE USA INC (Drummondville PQ) | Mass. Commission for the Blind | educational equipment | USD 2,623 | 2025-10-30

## Known gaps / limits
- Spending data only; contract terms live in COMMBUYS (not bulk-accessible) and the Comptroller's "Contracts" CTHRU module is not published as a dataset.
- Vendor zip codes are truncated to 5 characters in CTHRU (e.g. `L4G0Z`), city sometimes "CANADA".
