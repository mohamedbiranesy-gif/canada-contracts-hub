# ca_ontario_vor — Ontario Enterprise Vendor of Record (VOR) arrangements

Status: COMPLETE. Output only `normalized/ca_ontario_vor_unverified_country.jsonl` (1,818 records, all `ongoing`).

## Source
- data.ontario.ca dataset "Enterprise Vendor of Record Arrangements"
  (https://data.ontario.ca/dataset/enterprise-vendor-of-record-arrangements); resource CSV
  `https://www.doingbusiness.mgs.gov.on.ca/mbs/psb/vordb.nsf/SettingDocView/enterprise_vor_program/$File/enterprise_vor_program.csv`
  downloaded 2026-10-25T19:29:55Z -> `downloads/ca_ontario_vor/enterprise_vor_program.csv`
  (202,778 bytes; extract tag `enterprise_vor_program_202610242340_50`; 1,832 rows = qualified vendor x arrangement,
  95 distinct VOR arrangements). Columns: VOR Number, VOR Name, Qualified Vendor, Start Date, End Date.
- Script `scripts/ca_ontario_vor/normalize.py`. (Previously rejected in `notes/ca_ontario_otp.md` for lack of vendor
  address; produced now under the coordinator's unverified-country rule.)

## Canadian vendor
No address -> vendor.country null, country_basis "not published (dataset has no vendor address)". Includes obvious
multinationals (Adobe Inc., Merative) — not filtered, since no location is published.

## Ongoing logic
Start Date ≤ 2026-10-25 ≤ End Date -> `ongoing` (1,818); ended 14 excluded. No values published.
Buyer: Government of Ontario (OPS ministries; enterprise VORs administered by Supply Ontario).
record_id `ca_ontario_vor:<VOR number>:<sha1(vendor)[:8]>`; record_url null (no per-row page).

## Samples
- Merative-VSLSA-001 | Merative Curam Enterprise Case Management VSLSA | Merative | 2025-05-01 – 2032-04-30
- Tender-17815 | Learning Training Research and Evaluation (LTRE) | Humanicity Consulting Group Inc. | 2023-05-15 – 2028-05-14
- Tender-18066 | Graphic Design and Creative Services | MadMacDesign Inc | 2023-11-01 – 2027-10-31
- Tender-19514 | Vehicle Acquisition and Upfitting Services | FCA Canada Inc | 2024-07-01 – 2028-06-30
- Tender-20935 | Human Resources Services | ThoughtStorm Inc | 2026-01-16 – 2032-01-15

## Known gaps
A VOR arrangement is a pre-qualification / standing agreement, not a guaranteed contract value; call-ups under it are not published.
