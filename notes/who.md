# who — WHO awarded contracts (annual goods & services lists), supplier country Canada

Reference date 2026-10-25. Output `/home/claude/contracts/normalized/who.jsonl`: **816 records, all `end_date_unknown`**.

## Downloaded
22 PDFs from the WHO contract-awards page https://www.who.int/about/accountability/procurement/contract-awards (retrieved 2026-10-25 ~17:26–17:27 UTC; exact `cdn.who.int/media/docs/default-source/procurement/...pdf?sfvrsn=…` URL of every file is in `scripts/igo_portals/normalize_who.py` → `SRC`, and per record in `contract.related.source_pdf_url`). Years 2015–2025 (goods and services; 2024–2025 include Unitaid). Saved in `downloads/igo_portals/who/` (~27 MB). No 2026 list published yet.
Parsing: `scripts/igo_portals/parse_who.py` (pdfplumber, header-driven column detection, rows anchored on the 9-digit contract reference) → `downloads/igo_portals/who/parsed_rows.json` (**67,961 rows**; per-file counts and detected column sets in `parse.out`). Normalisation: `scripts/igo_portals/normalize_who.py` → stats `downloads/igo_portals/who/normalize_stats.json`.

## Canadian vendor — verified
Structured column **"Supplier Country"** of each PDF table = `Canada` (all 816 records: raw cell value `Canada`; a couple of wrapped/pushed-cell cases are explained in `vendor.country_basis`). Names never used. Spot-checked against `pdftotext -layout` on 2026-10-25 19:3x UTC: 203714435 (EMERGENT BIOSOLUTIONS CANADA INC., Europe Office, 8/22/2025, $721,931, "Canada"), 203745054 (BIO BASIC CANADA INC, Africa Office, 10/14/2025, $49,252), 201334348 (DNA GENOTEK INC., Headquarters, 05-Oct-2015, $577,053) — all match the PDF rows.
**547 of 816 rows have the supplier name published as "Name withheld"** (WHO withholds names of individual contractors); `vendor.name` = null, `vendor.name_withheld` = true, published text in `vendor.name_as_published`. Such rows are still Canadian per the country column.

## Buyer — verified named
Buyer = "World Health Organization - <WHO office>" from the "WHO Office" column (Headquarters 534, Western Pacific 76, Eastern Mediterranean 71, Africa 65, Europe 56, South-East Asia 12) or "Unitaid (hosted by WHO)" (2). Every record has an office value. One page-counter artefact ("Headquarters 29/53") was cleaned on 2026-10-25 by the resuming worker (noted in `buyer.identifiers.note`).

## Ongoing
WHO publishes reference number, description/category, office, supplier, country, date of contract and USD amount only — no end date or term → all `end_date_unknown`; `contract.dates.signed` = "Date of contract" (numeric dates DMY for 2015–2021 files, MDY for 2022+ files, detected per file). Signed-year distribution: 2015 24, 2016 25, 2017 19, 2018 17, 2019 26, 2020 142, 2021 142, 2022 166, 2023 140, 2024 40, 2025 75. **Downstream users should treat older POs (esp. goods, pre-2024) as almost certainly completed**; they are kept only because the schema keeps end-date-less awards.

## record_url
null (PDF list, no per-contract page); PDF URL + page number in `contract.related`.

## De-duplication vs UNGM
`normalized/ungm.jsonl` has only 2 WHO awards to Canadian suppliers; the normaliser flags 3 WHO rows of SHIOTA HEALTH COMMUNICATIONS INC as *possible* overlaps with ungm:141393 (LTA-WPRO-SUP-2024-004) — these are individual POs (2023-01, 2023-12, 2024-01) vs a 2024-03 LTA, so they were kept, listed in `normalize_stats.json → possible_ungm_overlap`.

## Samples
- who:201334348 | DNA GENOTEK INC. | WHO – Headquarters | Diagnostics and Research Biologicals | USD 577,053 | signed 2015-10-05
- who:201380789 | APOTEX INC. | WHO – Eastern Mediterranean Office | USD 79,400 | 2015-11-16
- who:201184962 | GLOBAL EVALUATIVE SCIENCES | WHO – Headquarters | USD 330,000 | 2015-03-03
- who:203714435 | EMERGENT BIOSOLUTIONS CANADA INC. | WHO – Europe Office | Miscellaneous Drugs | USD 721,931 | 2025-08-22
- who:203745054 | BIO BASIC CANADA INC | WHO – Africa Office | Reagents, Chemicals, Laboratory | USD 49,252 | 2025-10-14

## Gaps
PDF parsing can mis-split wrapped cells (descriptions occasionally truncated); amounts parsed with per-file thousands-separator rules. One duplicate reference number (suffix `-2`). No 2026 awards yet.
