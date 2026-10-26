# ca_ontario_otp — Ontario Tenders Portal / Supply Ontario / data.ontario.ca (REJECTED)

Checked 2026-10-25 17:21–18:22 UTC.

- **Ontario Tenders Portal** (`https://ontariotenders.app.jaggaer.com/`): the public "Past opportunities"/"Global opportunities" entry points (`/esop/guest/go/public/opportunity/past`, `/esop/nac-host/public/ontario/opportunities/global.jsp`) answer with Jaggaer's `browserNotSupported.jsp` ("Upgrade Your Browser") to a plain HTTP client, and `/esop/toolkit/opportunity/global/opportunityList.do` returns 401 (login required). WebFetch is refused by robots.txt. No export/API found; contract-award notifications on OTP are therefore not crawlable here. Not bypassed.
- **data.ontario.ca** (CKAN search for contract/procurement/awards/vendor/tender): the only downloadable datasets are *Enterprise Vendor of Record Arrangements* (`enterprise_vor_program.csv`, 1,834 rows: VOR number, VOR name, qualified vendor, start, end — **no vendor address/country**), *Consulting Services Contracts* FY2016-17/2017-18 (ministry, vendor name, assignment, ceiling — no vendor address; all pre-2019 so almost certainly ended), and *Advertising Review Board VOR arrangements* (names only). Datasets such as ProCon, PACT, MTO contract history are listed without downloadable resources ("not yet open"). All rejected: vendor country cannot be established.
- **Supply Ontario** (`supplyontario.ca`): no contract-award listing page (`/contract-awards/` 404).
- Ontario broader-public-sector awards posted on MERX / bids&tenders are covered by the parallel `ca_merx` / `ca_bidsandtenders` workers.

Result: 0 records.
