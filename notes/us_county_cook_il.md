# us_county_cook_il — Cook County (IL) "Procurement - Awarded Contracts & Amendments" (datacatalog.cookcountyil.gov qh8j-6k63): checked, rejected

8,342 rows (contract_number, vendor_number, vendor_name, amount, description, lead_department, start_date, end_date, commodity_type) — **no vendor address/country field**. The related "Bid Tabulations" dataset has bidder city/state but covers bids, not awards. Rejected.

## Resume check (2026-10-25 ≈19:47 UTC)
Tried linking the "Procurement - Bid Tabulations" dataset (`32au-zaqn`: bid_opening_date, contract_number, company_name, **city, state**, bid_amount) to awards (`qh8j-6k63`) by contract_number: only 10 bids from Canadian addresses exist (state CANADA/ONTARIO/QC/BC; e.g. Terradyne Armored Vehicles, Newmarket ON; Vita Detection USA, St-Laurent QC, bid opened 2026-07-15). Of their contracts, only 1884-17374 was awarded to the Canadian bidder (Terradyne, 2018-06-06 … 2021-06-05, ended); 2612-05121 (Vita Detection) has no award row yet; the others went to US vendors. 0 records; rejection stands.
