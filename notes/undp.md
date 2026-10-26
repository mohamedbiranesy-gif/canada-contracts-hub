# undp — UNDP Procurement Notices: Contract Awards

Reference date 2026-10-25. Output `/home/claude/contracts/normalized/undp.jsonl`: **51 records, all `end_date_unknown`**.

## Downloaded
`POST https://procurement-notices.undp.org/view_awards.cfm` with `date_from1/date_to1` per half-year, 2008-01-01 → 2026-12-31 (38 requests, all HTTP 200, 2026-10-25 17:21:39–17:23:22 UTC; log `downloads/igo_portals/undp/fetch_log.json`, HTML in `downloads/igo_portals/undp/awards_<from>_<to>.html`). Script `scripts/igo_portals/fetch_undp.py`; parser `scripts/igo_portals/normalize_undp.py`; stats `downloads/igo_portals/undp/normalize_stats.json`: 10,415 award rows, 7,244 with a contractor country, 3,171 without.

## Canadian vendor
Listing field **"Country of Contractor"** = `CANADA`/`Canada` → 55 rows. Names never used.

## Ongoing
The listing gives posting date, signature date, amount, office; no end date. Where the title/description states a term, it is applied: 4 SHL Canada LTAs (UNDP/OHR/LTA/2014/016–023, "for 3 years" from 2014-12-31 → 2017-12-31) excluded as ended. Remaining 51 → `end_date_unknown` (signed years 2008–2025; most are old — treat with caution).

## Buyer
"UNDP - <office>" from the listing (e.g. UNDP/PSO/GPU, Port-au-Prince – HAITI, CO UKRAINE).

## record_url
null (listing has no per-award page); query parameters in `contract.related.search_query`.

## De-dup vs UNGM
Checked against `normalized/ungm.jsonl` (UNDP Canadian awards: 2) by reference/vendor — no overlap (`already_covered_by_ungm: []`).

## Samples
- undp:92784-1 | Code Incorporated | UNDP/PSO/GPU | Translucent ballot boxes | USD 3,699,840 | 2008-06-12
- undp:92858 | Code Incorporated | UNDP Bangladesh | Ink pens for elections | USD 488,000 | 2008-12-04
- undp:noref-2008-12-02-globescan-incorporated | Globescan Incorporated | Bureau of Management HQ | corporate surveys | USD 405,845
- undp:92812 | Code Incorporated | UNDP/ELECT Afghanistan | training & registration material | USD 258,539
- undp:10377389 | Stuart Black (individual) | Multi-Country Office Trinidad and Tobago | final evaluation SISSTEM | USD 20,284 | 2025-04-15
