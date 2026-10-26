# us_city_austin — City of Austin (Texas) purchase-order detail, vendor country = CA

Reference date 2026-10-25. Output: `/home/claude/contracts/normalized/us_city_austin.jsonl` (**9 records**, all `end_date_unknown`). Script: `scripts/us_city_austin/normalize.py`.

## What was downloaded (datahub.austintexas.gov, Socrata, 2026-10-25 18:04 UTC)
- `3ebq-e9iz` "Purchase Order Quantity Price detail for Commodity/Goods procurements" (landing https://datahub.austintexas.gov/d/3ebq-e9iz → /Budget-and-Finance/Purchase-Order-Quantity-Price-detail-for-Commodity/3ebq-e9iz). Columns: commodity, commodity_description, extended_description, quantity, unit_of_measure(_desc), unit_price, itm_tot_am, master_agreement, contract_name, purchase_order, award_date, vendor_code, lgl_nm (vendor legal name), ad_ln_1, ad_ln_2, city, st, zip, **ctry**, data_build_date. Pulled with `$where=ctry='CA'` → `downloads/us_city_austin/po_detail_ca_3ebq-e9iz.jsonl`, 440 line rows (country distribution: US 320,272; blank 899; **CA 440**; GB 21; FR 8 …) → 273 purchase orders, award years 2009–2026.
- `84ih-p28j` "Contracts" (active long-term contracts; 625 rows, `contracts_84ih-p28j.jsonl`): has vendor legal name and vendor code but **no vendor address/country**. Joined on vendor_code against the Canadian vendor codes from 3ebq-e9iz: 0 matches, so no contract-term records could be built.

## How "Canadian vendor" was determined
Structured `ctry = 'CA'` (ISO-2 country code in the vendor address block; cities Ottawa, Montreal QC, Richmond BC, Georgetown ON, Chalk River…; `zip` are Canadian postal codes). Names never used.

## How "ongoing" was determined
Purchase orders have no term dates → `end_date_unknown`, kept only when `award_date` is within the 12 months before the reference date (9 of 273; 264 older). All lines of a PO are in `raw.rows`; value = sum of `itm_tot_am`.

## Record construction
`record_id` = `us_city_austin:<purchase_order>:<vendor_code>`; buyer = City of Austin, Texas (department not in the dataset; the PO number embeds the department code). No per-PO page (`record_url` null).

## Counts / samples
9 end_date_unknown, sum USD 342,893: ECO-COUNTER INC (Montreal) bike/ped counter equipment USD 211,567 (2026-06-01) and battery replacements; Customer Expressions Corp (Ottawa) Case IQ annual subscription FY27 USD 96,833 (2026-09-30); ICOR Technology (Ottawa) robot repair USD 11,662; bioLytical Laboratories (Richmond BC) HIV rapid tests ×2; Markland Specialty Engineering (Georgetown ON) density meter probes; Bubble Technology Industries (Chalk River ON) radiation detector repair; Sure-Close Inc. (Ottawa) compost collectors.

## Known gaps
Goods/commodity POs only (services POs are not in this dataset); the Contracts dataset lacks vendor addresses, so multi-year Austin contracts with Canadian vendors (if any) are not detectable.
