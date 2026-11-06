# us_state_vermont (Vermont Vendor Payments)

* **Source**: State of Vermont "Vendor Payments" via data.vermont.gov (Socrata endpoints `786x-sbp3`, `w4us-y6js`, `kngi-j45t`, `e7ne-x7k2`, `9t8z-fmfj`, `i558-vamq`).
* **Yield**: 2574 records found that have a vendor state code corresponding to a Canadian province (ON, QC, BC, AB, MB, SK, NS, NB, NL, PE, YT, NT, NU). This provides a more robust indicator of Canadian location.
* **Fields**: `qtrending`, `govtunit`, `unitno`, `vno`, `vendor`, `city`, `state`, `description`, `objcode`, `amt`, `account`, `acctno`, `fund_description`, `fund`.
* **Quirks**: Status is `end_date_unknown` because these are payments, and they don't feature end dates. Vendor country was inferred based on Canadian provinces in `state`.
