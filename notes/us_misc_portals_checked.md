# us_misc_portals_checked — smaller US local portals checked on resume (2026-10-25, ≈19:28–19:55 UTC) and rejected

Discovery tools: Socrata catalog sweeps (`scripts/us_discovery/catalog_sweep.py`, inline second sweep → `downloads/us_discovery/catalog_sweep_resume.txt`, `catalog_sweep2.txt`), ArcGIS Hub sweeps with field inspection (`scripts/us_discovery/arcgis_sweep.py`, `arcgis_sweep2.py` → `downloads/us_discovery/arcgis_sweep*.txt`), CKAN sweeps (`scripts/us_discovery/ckan_sweep.py`). Each portal below was inspected (fields and, where relevant, a Canadian-address query) and yielded **0 records**:

| Portal / dataset | Why rejected |
|---|---|
| Pasadena CA "Purchase Orders and Contracts (3 years / 12 months)" (ArcGIS, CityOfPasadenaCAGIS) and "Vendor Payments" by FY | fields VENDOR_NAME, DEPARTMENT, PO_CONTRACT, STATUS, TOTAL_AMT — no vendor address |
| Glendale AZ "Contract Spend Report" (ArcGIS) | VendorCompanyName, contract dates/amounts — no vendor address |
| Nashville "Metro Vendor Payments" (ArcGIS, 1.31 M rows) | Supplier_Number only — no name/address |
| Scottsdale AZ "Vendor Payments" (ArcGIS MapServer/7) | VendorName only |
| Greensboro NC "Invoice Spend for Purchase Orders" (ArcGIS) | PO number/amount only, no vendor |
| Kansas City MO "Vendor Payments Calendar Year 2016–2026" and "List of KCMO City Contracts" (data.kcmo.org) | no vendor address columns |
| Cincinnati "City of Cincinnati Vendor Payments" (data.cincinnati-oh.gov qrj9-83t8) | no vendor address columns |
| Riverside County CA "Check Book" (data.countyofriverside.us swwh-4ka9) | no vendor address columns |
| Dallas "Vendor Payments FY2019–present" (dallasopendata x5ih-idh7) | 5-digit `zip5` only (cannot hold a Canadian postal code) |
| Prince George's County MD "Spending Information FY2022–FY2026" | zip_code only; query for alphabetic (Canadian-format) zips returned 0 rows |
| Maryland "County Board of Education – Spending Disclosures" (opendata.maryland.gov t6vk-rvwe) | payee_zip only; alphabetic values are placeholders ("ACH Payment", "ERROR: #N/A"), no Canadian postal codes |
| Nassau County NY "ARPA Spending" (vendor_state) | ARPA-only spending, last updated 2023 — outside the 12-month window |
| Idaho "ITS Vendors" (ArcGIS, State_of_Idaho, 16 rows with Country) | all vendors Country = United States |
| TxDOT "Vendor List" (data.texas.gov dw25-6md2) | no vendor with a Canadian physical/mailing state |
| Dedham MA "Vendors" (country field) | no expenditure/contract dataset on the domain to link to |
| Minnesota Open Checkbook (mn.gov/mmb/transparency-mn) | interactive app; no bulk vendor-payment download found |
