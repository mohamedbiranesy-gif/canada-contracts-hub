# us_city_indio_ca — City of Indio, California "Expenditures" + "Vendors" (indio.data.socrata.com)

Reference date 2026-10-25. Output: `/home/claude/contracts/normalized/us_city_indio_ca.jsonl` (**4 records**, all `end_date_unknown`). Script: `scripts/us_city_indio_ca/normalize.py` (same OpenGov/Tyler open-finance layout as us_city_richmond_ca).

## What was downloaded (SODA, 2026-10-25T19:47:21Z UTC)
- `xjj3-7uha` "Vendors" (vendorid, vendorname, address1, address2, city, **state**, zip, country, contact, vendortype, employee) filtered `state in (province codes)` → `downloads/us_city_indio_ca/vendors_ca_xjj3-7uha.jsonl` (9 vendors).
- `3tyh-g5za` "Expenditures" (GL rows: date, fiscal year/period, organization(+code), object, fund, project, description, actual, invoiceid, invoicestatus, paymentchecknumber, vendorid, vendorname, uniqueid…) filtered on those vendor ids → `expenditures_ca_3tyh-g5za.jsonl` (24 rows). Found via Socrata catalog search for vendor masters with state + id.

## Canadian vendor / ongoing
Vendor master state = Canadian province code (all 9 also have Canadian postal codes). One record per (vendorid, organizationcode); kept iff latest expenditure date within the 12 months before 2026-10-25: 4 of 11 groups. value = Σ actual (non-void). `record_url` null.

## Result: 4 end_date_unknown (USD 279,851)
- `us_city_indio_ca:8640-602` eSentire, Inc (451 Phillip St, Waterloo ON N2L 3X2) — Information Technology — cybersecurity services — USD 151,776
- `us_city_indio_ca:8998-602` InTime Services Inc (Vancouver BC V6E 0C5) — Information Technology — scheduling/timekeeping software — USD 25,668 — last 2026-09-04
- `us_city_indio_ca:6616-1014212` Eden K9 Consulting & Training Corp (Chestermere AB T1X 1T7) — Police Field Services — USD 1,074
- `us_city_indio_ca:8158-203` Sara Dabbagh (Mississauga ON L5E 1V6; artist) — Public Art In-Lieu — traffic-signal wraps / artwork — USD 101,333
(all four records listed; they double as samples). Excluded (no payment in 12 months): Metocean Telematics, ICOR Technology, Nightingale, Solinst Canada, Control Microsystems.

## Gaps
GL expenditure rows only; no contract terms.
