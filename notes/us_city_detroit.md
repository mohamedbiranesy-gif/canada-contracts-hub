# us_city_detroit — City of Detroit "OCP Procurement Agreements" (ArcGIS): checked, 0 Canadian-vendor records

- Layer https://services2.arcgis.com/qvkbeam7Wirps6zC/arcgis/rest/services/OCP_Procurement_Contracts/FeatureServer/0 (found via ArcGIS Hub search), pulled in full 2026-10-25T19:29:34Z with `scripts/us_common/arcgis_pull.py` → `downloads/us_city_detroit/ocp_procurement_contracts_all.jsonl` (6,271 rows; fields amount, description, status, supplier, city, **state**, supp_addr, start_date, end_date, number, po_type, contract_link (PDF)).
- State values: MI 4,753, Michigan 320, IL 304, WI 127, … — **no Canadian province, no "Canada"/Canadian postal code in supp_addr/city**. The only text hit ("AtomAI Solutions Inc., La Canada, CA") is La Cañada, California.
- Result: 0 records (no output file). Useful source otherwise (dates + address + contract PDF links) — refresh later.
