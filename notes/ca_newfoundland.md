# ca_newfoundland — NL Public Procurement Agency "Contract Awards Reports" (semi-monthly PDFs), Canadian vendors

Reference date 2026-10-25. Output `/home/claude/contracts/normalized/ca_newfoundland.jsonl` — **4,500 records: 3 `ongoing`, 314 `ongoing_inferred`, 4,183 `end_date_unknown`**.

## What was downloaded
- Index pages: https://www.gov.nl.ca/ppa/tenders/awarded/ (2026) and https://www.gov.nl.ca/ppa/2022-contract-awards/ … `/2025-contract-awards/` — 118 PDF links (`downloads/ca_newfoundland/pdf_urls.txt`), all downloaded 2026-10-25 18:21–18:26 UTC (`scripts/ca_newfoundland/fetch_nl.sh`, log `fetch.log`), e.g. `https://www.gov.nl.ca/ppa/files/2026-September-16-30-Contract-Awards-Report.pdf`. These are the Agency's "Report to Chief Procurement Officer (s.31 Public Procurement Regulations)" listing every contract award ≥ reporting threshold by NL public bodies (departments, NL Hydro/Nalcor, NL Health Services, College of the North Atlantic, MUN, municipalities, OilCo, Bull Arm …) for limited calls, exceptions ("Other" with the regulation clause) and some open calls. (Open-call awards of government departments are on MERX `govnl` — parallel `ca_merx` worker.)
- Parsed with pdfplumber table extraction (`scripts/ca_newfoundland/parse_nl.py` → `downloads/ca_newfoundland/rows.jsonl`, 5,874 rows from 118 PDFs; stats `normalize_stats.json`). Two header generations (v4 2022-02-01: "Supplier Location (Prov/State)"; v5 2025-01-24: "(Province/State)" + "Term of Contract" + "Renewal Options") handled by header-keyword mapping. "REVISED" re-issues of a period are parsed too (duplicates removed by content hash: 1).

## Columns
`Public Body, Type of Procurement, Relevant Clause if Other, Description, Commodity Type (v5), Supplier Name, Supplier Location (City/Town), Supplier Location (Province/State), Contract Price (Exclusive of HST), Contract #, Date of Award, Term of Contract, Renewal Options` — all verbatim in `raw` with `_file`, `_page`, `_reporting_period`.

## How "Canadian vendor" was determined
`Supplier Location (Province/State)` is a Canadian province/territory code or name (NL 1,906, ON 1,498, QC 337, NS 328, AB 147, BC 110, NB 102, MB 47, PE 21, SK 4). Skipped: US states / "CO, USA" / foreign countries (228 + ~115 "other" values such as TX, UK, Germany, Scotland, "NL/ON"), blank (0 after header fix), missing supplier or public body (19).

## How "ongoing" was determined
- `Term of Contract` is an explicit date (3 rows, e.g. "4/1/2027") → `ongoing` when award ≤ ref ≤ that date.
- `Term of Contract` is a duration ("1 Year", "3 Years", "<6 Months", "9 Months", "6 Year Contract Year 2 of 6 Year Term" → 6 years) → end = Date of Award + duration (arithmetic shown in `status_basis`) → `ongoing_inferred` when ≥ 2026-10-25 (314), excluded when earlier (789).
- Otherwise ("N/A", "One Time", "Commodity Purchase", "Pricing until June 30, 2024" [not parsed], blank) → `end_date_unknown` (4,183). 3 awards dated after the reference date excluded. Unicode hyphens in dates ("22‐Mar‐23") normalised.

## Record construction
- `record_id` = `ca_newfoundland:` + sha1(file|public body|supplier|contract #|award date|price|description)[:16]; `record_url` = null (PDF reports; `contract.related.report_url` + `report_page` locate the row). Buyer = Public Body as printed (department names vary across years: "Transportation & Infrastructure" vs "Department of Transportation and Infrastructure"; not harmonised).
- `procurement_method` = Type of Procurement (Other 1,957 — exception awards with the clause in `solicitation_procedure`; Limited Call 1,729; Limited Call For Bids 781; Open Call 29).

## Counts
- Rows 5,874 → Canadian 4,500 (award year 2022 600, 2023 862, 2024 896, 2025 1,081, 2026 1,048, undated 6). Inferred/explicit end years: 2026 42, 2027 160, 2028 45, 2029 44, 2030 12, 2031 12, later 2. Total price CAD 835 M.
- Top buyers: Department of Transportation and Infrastructure 458 (+333 as "Transportation & Infrastructure"), NL Hydro 352 (+352 "Newfoundland & Labrador Hydro"), City of St. John's 344, College of the North Atlantic 284, NL Health Services 245.

## 5 samples
- ca_newfoundland:2cf44713a8da8621 | Illumina (Toronto, ON) | NL Health Services | Service Agreement Renewal - NovaSeq and MiniSeq | CAD 161,375.20 | ongoing_inferred 2026-06-25 + 1 year → 2027-06-25 | 2026-June-16-30 report
- ca_newfoundland:5902a1f119030f6a | Microsoft Canada Inc. (Toronto, ON) | Executive Council-OCIO | Microsoft Enterprise Agreement Subscription Renewal | CAD 3,570,783.76 | ongoing_inferred 2022-12-22 + 6 years → 2028-12-22
- ca_newfoundland:c8c08fb4d0db2181 | Steris (Richmond Hill, ON) | NL Health Services | PM service washer/sterilizer | CAD 58,124.37 | ongoing_inferred 2025-10-24 + 3 years → 2028-10-24
- ca_newfoundland:c9296508a854c098 | Facta Global (Montreal, QC) | Department of Justice and Public Safety | Launchers with munitions and training | CAD 181,164.08 | end_date_unknown (term N/A) | awarded 2026-08-12
- ca_newfoundland:0e0b2a18d1a0fe6a | C&J Excavation Ltd (Lark Harbour, NL) | Town of Lark Harbour | Garbage Collection Services | CAD 75,975 | ongoing_inferred 2026-09-22 + 2 years → 2028-09-21

## Known gaps / limits
- Only reports from 2022 onward are published on the site (earlier years not online). Supplier street address/postal code not published (city + province only).
- PDF table extraction: multi-line cells are joined; a few rows where pdfplumber split a cell may have slightly shifted text (spot-checked ~40 rows, none wrong). Renewal options are not applied to the inferred end date (base term only).
- "Date of Award" for a handful of rows is a free-text range (e.g. "PAL Apr 26 - Sep 26") → `awarded` null.
