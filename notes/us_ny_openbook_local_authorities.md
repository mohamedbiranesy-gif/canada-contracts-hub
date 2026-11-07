# New York Open Book - Local Authorities

* Source URL: `https://data.ny.gov`
* Datasets: Procurement Report for Local Authorities (`8w5p-k45m`), Procurement Report for Local Development Corporations (`d84c-dk28`), Procurement Report for Industrial Development Agencies (`p3p6-xqr5`).
* We identify Canadian vendors natively using Socrata's SoQL: `upper(vendor_country) in ('CAN', 'CANADA') OR upper(vendor_country) like '%CANADA%'`.
* Found ~119 unique Canadian ongoing/undated contracts across the 3 datasets. Excluded expired contracts.
