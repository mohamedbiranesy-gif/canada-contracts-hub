# ca_merx_backlog — MERX public "Awarded Solicitations" (award notices backlog)

Status: In progress (first slice uploaded).

## Source
- Same pipeline logic as `ca_merx`.
- Publisher: MERX (mdf commerce) on behalf of various issuing organizations.
- Crawl window for this slice: small backlog fetch to test functionality.
- Endpoints:
  - Listing: `https://www.merx.com/public/solicitations/awarded`
  - Detail page: `https://www.merx.com/public/solicitations/<merx_id>/abstract/award`

## Canadian vendor
- Address parsed from awardee "Address" block, requiring "Canada" as the country.

## Output for first slice
- Details parsed: 20
- Records output: 18
- Vendors: Validated Canadian vendors only.
- Output file: `records_ca_merx_backlog.jsonl.gz`
{
 "stats": {
  "details": 20,
  "excluded_future_award": 7,
  "no_awardees": 1,
  "excluded_not_started": 5,
  "no_award_tab": 2,
  "excluded_vendor_country": 1,
  "records": 18
 },
 "by_status": {
  "ongoing": 17,
  "end_date_unknown": 1
 },
 "by_status_unverified": {},
 "n_buyers": 6,
 "buyers": [
  [
   "Government of Newfoundland and Labrador (GNL) - Public Procurement Agency",
   8
  ],
  [
   "Toronto Metropolitan University",
   5
  ],
  [
   "Toronto Parking Authority",
   2
  ],
  [
   "Manitoba Transportation and Infrastructure - Tendering and Contracts",
   1
  ],
  [
   "Lambton College",
   1
  ],
  [
   "NL Provincial Health Shared Services Supply Chain",
   1
  ]
 ],
 "vendor_countries": [
  [
   "Canada",
   30
  ],
  [
   "United States",
   1
  ]
 ],
 "samples": [
  {
   "record_id": "ca_merx:3850211026:1",
   "vendor": "Access 2 Networks Inc.",
   "city": "Mississauga",
   "buyer": "Toronto Metropolitan University",
   "title": "Vendor of Record for HPE Aruba Support and Service",
   "value": 1.0,
   "start": "2026-05-01",
   "end": "2029-04-30",
   "url": "https://www.merx.com/oupma/torontomu/solicitations/Vendor-of-Record-for-HPE-Aruba-Support-and-Service/0000315044?origin=0"
  },
  {
   "record_id": "ca_merx:3850211026:2",
   "vendor": "Compugen Inc.",
   "city": "Richmond Hill",
   "buyer": "Toronto Metropolitan University",
   "title": "Vendor of Record for HPE Aruba Support and Service",
   "value": 1.0,
   "start": "2026-05-01",
   "end": "2029-04-30",
   "url": "https://www.merx.com/oupma/torontomu/solicitations/Vendor-of-Record-for-HPE-Aruba-Support-and-Service/0000315044?origin=0"
  },
  {
   "record_id": "ca_merx:3850211026:3",
   "vendor": "Eclipse Technology Solutions Inc. dba IMP Solutions",
   "city": "Mississauga",
   "buyer": "Toronto Metropolitan University",
   "title": "Vendor of Record for HPE Aruba Support and Service",
   "value": 1.0,
   "start": "2026-05-01",
   "end": "2029-04-30",
   "url": "https://www.merx.com/oupma/torontomu/solicitations/Vendor-of-Record-for-HPE-Aruba-Support-and-Service/0000315044?origin=0"
  },
  {
   "record_id": "ca_merx:3850211026:4",
   "vendor": "INSA Corp",
   "city": "Ottawa",
   "buyer": "Toronto Metropolitan University",
   "title": "Vendor of Record for HPE Aruba Support and Service",
   "value": 1.0,
   "start": "2026-05-01",
   "end": "2029-04-30",
   "url": "https://www.merx.com/oupma/torontomu/solicitations/Vendor-of-Record-for-HPE-Aruba-Support-and-Service/0000315044?origin=0"
  },
  {
   "record_id": "ca_merx:3850211026:5",
   "vendor": "Xerox IT Solutions Canada Ltd.",
   "city": "Winnipeg",
   "buyer": "Toronto Metropolitan University",
   "title": "Vendor of Record for HPE Aruba Support and Service",
   "value": 1.0,
   "start": "2026-05-01",
   "end": "2029-04-30",
   "url": "https://www.merx.com/oupma/torontomu/solicitations/Vendor-of-Record-for-HPE-Aruba-Support-and-Service/0000315044?origin=0"
  }
 ]
}