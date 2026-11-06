# us_city_baton_rouge_expenditures (City of Baton Rouge Expenditures)

* **Source**: City of Baton Rouge / Parish of East Baton Rouge "City-Parish Expenditures" via data.brla.gov (Socrata endpoint `vwa8-ps2a`).
* **Yield**: 203 records found that have a vendor state code corresponding to a Canadian province (ON, QC, BC, AB, MB, SK, NS, NB, NL, PE, YT, NT, NU). This provides a more robust indicator of Canadian location than guessing based on vendor name.
* **Fields**: `year`, `fund`, `department`, `invoice_line_item_amount`, `vendor_name_1`, `vendor_city`, `vendor_state`, `vendor_zip`, `check_number`, `invoice_number`, `source_document_number`, `check_date`.
* **Quirks**: Status is `end_date_unknown` because these are payments, and they don't feature end dates. Vendor country was inferred based on Canadian provinces in `vendor_state`.
