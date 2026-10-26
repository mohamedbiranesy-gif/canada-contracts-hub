# austender — AusTender Contract Notices (Australian Government), supplier located in Canada

Reference date: 2026-10-25. Output: `/home/claude/contracts/normalized/austender.jsonl` (**97 records**, all `ongoing`).

## What was downloaded

| Item | Detail |
|---|---|
| Primary source | AusTender OCDS API, **contract END-date index**: `https://api.tenders.gov.au/ocds/findByDates/contractEnd/2026-10-24T00:00:00Z/2999-12-31T00:00:00Z`, cursor-paginated via `links.next` (100 releases/page). Docs: https://github.com/austender/austender-ocds-api , Swagger: https://app.swaggerhub.com/apis/austender/ocds-api/1.1 . Needs a browser-like `User-Agent` (bare curl to the API root gets 403). |
| Why end-date index | Every CN that can be ongoing on 2026-10-25 must have an end date ≥ that day, so one pass over `contractEnd ≥ 2026-10-24` (one day of slack for the UTC-vs-AEDT boundary) covers all publication years (API covers CNs from 01-01-2013; the historical data.gov.au extracts below cover earlier years). The index returns **both the original `contract` release and every `contractAmendment` release** of a CN (verified with CN4106552: 1 contract + 3 amendments). |
| Crawl | Script `/home/claude/contracts/scripts/austender/crawl_contract_end.py`; pages saved to `/home/claude/contracts/downloads/austender/ocds_end/pages/page_00000..00985.json` (986 pages, 186 MB), log `ocds_end/crawl.log`, resumable `state.json`. Retrieved 2026-10-25 12:13–13:09 UTC. **98,490 releases = 54,598 distinct CNs** (50,043 contract + 48,447 amendment releases). |
| Completeness check | Random end-date day window (2028-02-13) re-queried directly: 23 releases in API, 23 in crawl, 0 missing. For all 99 Canadian CNs the release set is gap-free (original present, amendments A1..An contiguous). |
| Historical bulk (pre-2013) | data.gov.au "Historical Australian Government Contract Notice Data" (https://data.gov.au/data/dataset/historical-australian-government-contract-data): downloaded `austenderallcnsupto31dec15.zip` (52.9 MB → `AusTender - All CNs upto 31Dec2015.csv`, 645,861 rows, columns incl. `Supplier Country`, `Start Date`, `End Date`, `ABN`) to `/home/claude/contracts/downloads/austender/hist/`. **1,499 rows with Supplier Country = CANADA; max End Date 2019-08-30 → 0 still ongoing**, so nothing to add from the pre-API era. Per-FY files 2014-15 … 2019-20 are superseded by the API (all post-2013). |
| UNSPSC descriptions | `AusTender Customised UNSPSC Codeset 1 July 2023.xlsx` from the same dataset (`/home/claude/contracts/downloads/austender/unspsc_codeset_2023.xlsx`) → `contract.commodity.unspsc_description` (all 97 codes resolved). |

## How "Canadian vendor" was determined
`parties[roles contains "supplier"].address.countryName` of the **latest release** of the CN, upper-cased == `CANADA` (values seen: `CANADA`, `Canada`). Names were never used. 99 of 54,598 CNs qualify. Address fields kept in `vendor.address` (`locality`, `region` is always "Outside Australia" for foreign suppliers, `postalCode`, `streetAddress`). ABN present for only 3 vendors (most foreign suppliers are "ABN exempt"; their party id is `EXEMPTUUID-…`).

One conflict (kept, flagged in `vendor.country_basis`): CN3831572 (Groupe Sharegate Inc, Montreal) — original CN release says CANADA, the A1 amendment release says AUSTRALIA/ACT with the same Montreal address; kept because the parent CN record on the website states Country: CANADA.

## How "ongoing" was determined
`contracts[0].period.startDate ≤ 2026-10-25 ≤ contracts[0].period.endDate` using the latest release, with the API's UTC instants converted to Australia/Sydney calendar dates (AusTender stores local midnight: `2026-12-30T13:00:00Z` = 31-Dec-2026 AEDT, matching the website). 97 ongoing; 2 excluded because start date is after the reference date (CN4271568 start 2026-11-09, CN4278101 start 2026-10-26). No `end_date_unknown` cases (the end-date index guarantees an end date). `status_basis` quotes both raw and converted dates.

## Record construction
- `record_id` = `austender:<CN id>`; one record per CN; **all releases (original + amendments, ordered original, A1, A2 …) under `raw.rows`**; normalized value/dates from the latest amendment; `contract.value_detail.original_value` = first release value; `contract.related.amendments` lists each amendment id with value/end after it.
- `record_url` = `https://www.tenders.gov.au/Cn/Show/<uuid>` where the UUID is the 32-hex suffix of `awards[0].id` (`CN4106552-76caeac4…` → `76caeac4-99f7-41cc-be7a-20fcf4affa74`). **Note: `/Cn/Show/CN4283780` (CN id in the path) does NOT work (302 → NotFound); the UUID form does.** Verified: https://www.tenders.gov.au/Cn/Show/4323cb63-66ec-4d21-8c93-6522c989d77d → "CN ID: CN3933986 … Contract Period: 1-Jan-2023 to 31-Dec-2026 … Contract Value (AUD): $113,226.63 Original: $31,406.08 … Supplier … International Civil Aviation Org. ICAO … Country: CANADA"; also checked CN4191569, CN4082320, CN4210639.
- Buyer = `parties[role=procuringEntity]` (agency name + AU-ABN). Commodity = UNSPSC from `contracts[0].items[].classification`. Procurement method from `tender.procurementMethodDetails` (83 Limited tender, 14 Open tender); limited-tender exemption/reason in `contract.related`.

## Counts
- Releases crawled 98,490 → distinct CNs 54,598 → Canadian-supplier CNs 99 → **ongoing 97**, excluded future start 2, excluded ended 0 (index only returns end ≥ 2026-10-24).
- Status: `ongoing` 97; `ongoing_inferred` 0; `end_date_unknown` 0.
- End years: 2026: 18, 2027: 49, 2028: 14, 2029: 8, 2030: 4, 2031: 3. Total latest value AUD 749.9 M (dominated by DFAT Australian Aid Program contracts to Cowater International Inc, and Defence).
- Top buyers: Department of Defence 22, DFAT – Australian Aid Program 9, Austrade 9, Geoscience Australia 7, DFAT 6, Bureau of Meteorology 5.

## 5 samples
- austender:CN4130327 | INTERNATIONAL AIR TRANSPORT ASSOCIA (Montreal) | Department of Home Affairs | Data services | AUD 54,241.20 | 2024-12-31 → 2026-12-31 | https://www.tenders.gov.au/Cn/Show/7d92e582-b492-4594-8b75-778fcbfd1e22
- austender:CN4252018 | MDA SPACE 49NORTH LTD. (Brampton) | Department of Defence | Software Licence Renewal | AUD 254,841 | 2026-06-01 → 2027-06-01 | https://www.tenders.gov.au/Cn/Show/88b32cc3-47f4-4b0f-ae5e-baab7c8612d9
- austender:CN4246992 | [OVS] Aerotech Herman Nelson International Inc. (Winnipeg) | Dept of Climate Change, Energy, the Environment and Water | Herman Nelson BT-400 Heaters – Australian Antarctic Division | AUD 110,000 | 2026-05-01 → 2027-06-30 | https://www.tenders.gov.au/Cn/Show/77d9d85a-70da-41a1-9e58-250bcf85af14
- austender:CN4024496 | APS AEROSPACE CORP. (Ottawa) | Department of Defence | Software Licencing | AUD 245,570.54 | 2023-12-07 → 2027-06-30 | https://www.tenders.gov.au/Cn/Show/3dff652e-68da-4e3d-a609-2bdefddde900
- austender:CN3933986 | International Civil Aviation Org. ICAO (Montreal) | DFAT | Professional Associations | AUD 113,226.63 (orig 31,406.08; 3 amendments) | 2023-01-01 → 2026-12-31 | https://www.tenders.gov.au/Cn/Show/4323cb63-66ec-4d21-8c93-6522c989d77d

## Known gaps / limits
- Only **Contract Notices** are covered. AusTender **Standing Offer Notices (SONs/panels)** are a separate object type not exposed by the OCDS API; not crawled. Contracts under a SON appear as CNs (with `SON ID`) and are included.
- Vendor country is as reported by the agency; data-entry errors exist (e.g. ITPS (CANADA) LTD with locality "LONDON" but Country CANADA; one supplier with Country CANADA but an Australian suburb was excluded only because its start date is in the future). We did not second-guess the country field except to flag the CN3831572 conflict.
- `tender.id` in the API is the OCDS ocid, not the ATM ID; ATM/SON ids visible on the website are not in the OCDS payload.
- Contracts whose end date was *amended* to a date < 2026-10-24 in the latest release are (correctly) not returned; contracts whose latest release still has end ≥ today are returned in full.
