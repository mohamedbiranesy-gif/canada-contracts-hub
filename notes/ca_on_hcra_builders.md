# ca_on_hcra_builders — the HCRA's Ontario Builder Directory (licensed builders and vendors of new homes)

Engine: `tools/authority_registers.py` (entry `hcra` of `AUTH`), workflow `authority-registers.yml`. Pattern and rules: `notes/ca_on_omvic_dealers.md`.

## What was read (2026-11-11)
- The Authority's address: "40 Sheppard Ave. W, Suite 400 Toronto, ON M2N 6K9"; its fee: "Renewal $715 This is the annual fee every
  licensee must pay to maintain their licence. The renewal fee is paid each year through the licence renewal process."
  (both on https://www.hcraontario.ca/licensing-fees/).
- https://obd.hcraontario.ca/ is an application; its robots.txt is "User-agent: * / Disallow:" (nothing disallowed). Its own data calls:
  `GET /api/builders?builderName=<letters>&page=1` → every builder whose name holds the letters (no limit seen: 10,363 for "homes"), all
  licence statuses: `NAME, OPERATINGNAME, ACCOUNTNUMBER, ADDRESS_2_CITY, LICENSESTATUS`; `GET /api/buildersummary?id=<ACCOUNTNUMBER>` →
  `VB_Name, OPERATINGNAME, CITY, ADDRESS (street, no postal code), TELEPHONE, WEBSITEURL, HCRA_INITIALLICENSEDATE, Expiry_Date,
  LICENCE_STATUS` — and an `EMAIL`, which the engine never keeps.

## Counts (2026-11-11)
| | |
|---|---|
| licensed builders / vendors (36 questions, one per letter and digit) | **6,888** |
| entries read in the test | 80: 76 legal persons by their name (a legal form in it), 43 name a website (54 %) |
| sites checked (39) | **19 tied** (16 by the telephone number, 3 by the street address), 13 show neither, 3 robots, 3 errors, 1 leads to a site not its own |

## Rules particular to this register
- No legal-type field: a licensee is a legal person when its legal name carries a legal form; the others (people) are left out.
- No postal code: a site is tied by the telephone number or by the street number + street name of the entry.
- Evidence page of a row = the directory's own data call for that licensee (the page a browser shows is an empty shell without it).
- The annual renewal fee ($715) is the row's value, labelled "a tariff, not a payment record".
