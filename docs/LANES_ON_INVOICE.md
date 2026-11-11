# Lanes billed on invoice — what to build and how to hand it in

Owner, 2026-11-11 (AGENTS.md §1, rules 6 to 12). A row is **one buyer** that a **Canadian entity** bills **on invoice**, payable **by bank
transfer or cheque** (a card on file, or a registrar in between, is not a row). The Canadian entity may be a company, a regulator, a public
body or an association. The buyer may be any organisation anywhere. No buyer twice. Target: 1,000,000.

On 2026-11-11 19Z the table held 7,833 such buyers, nearly all public bodies under contract. Everything below is how it grows.

## What makes a row, and who does which part

| part | who | how |
|---|---|---|
| the relationship: a record that ties a named organisation to a Canadian biller | **any lane** | one of the three hand-in formats below |
| the organisation's own site | lane `claude` engines | the roster links it, or the register entry is tied to a site on file by its postal code and its name |
| its role mailbox | lane `claude` engines | read on its own site (`tools/lead_crawl.py`), re-read by the referee. Never taken from a roster or a register |
| how the biller bills and is paid | **any lane** + the vendor reader | format 3 below; `tools/vendor_billing.py` reads the rest |
| the test of the row | `tools/relationship_rows.py: owner_test` | `ship_ready`, `ship_ready_missing`, `payment_route`, `invoice_fields_for_kind` on every row |

Hard rules of AGENTS.md §2 hold for every format: only pages you actually opened; a quote of at most 300 characters that contains the
value; the biller is in Canada by its own printed address, never by its name; natural persons are left out; a register's or a roster's own
e-mail column is never read, stored or mapped; CAPTCHA / login / 403 / robots → `blocked`, move on; at most 2 requests a second to a host.

## Format 1 — a register (licences, registrations, permits a Canadian body bills for)

A register names its holders with an address but no website. The engine ties each entry to a site on file (same postal code, same
telephone or same street address, **and** the names agree) — `tools/biz_licences.py`, run by `biz-licences.yml` twice a day.

Hand in **one descriptor file**: `contrib/<lane>/registers/<key>.json`.

```json
{
  "key": "ca_bc_liquor_licences",
  "kind": "csv",                    "_kinds": "ods | socrata | ckan | csv | arcgis | file",
  "url": "https://…/licences.csv",  "_or": "base + dataset (+ where, with {today}) for ods / socrata / ckan; path for a file you harvested",
  "f": {"number": "Licence Number", "name": "Licensee Legal Name", "trade": "Establishment Name", "status": "Status",
        "issued": "Issue Date", "expires": "Expiry Date", "kind": "Licence Type",
        "addr": "Address", "city": "City", "postal": "Postal Code", "phone": "Phone"},
  "keep": {"Status": ["Active"]},
  "persons_mixed": true,
  "cities": [],
  "record_word": "Liquor licence",
  "payee": "the body that is paid", "payee_address": "its own printed postal address", "payee_site": "https://…/",
  "payee_url": "the page that says the holder pays it", "payee_read": "2026-11-12",
  "fee_quote": "one sentence of that page, at most 300 characters",
  "page": "the register's own page", "list_name": "the X's public list of licences in force"
}
```

`kind: "file"` is for a register with no API: harvest it to `data/incoming/<lane>/register_<key>.csv.gz` (columns as you name them in `f`)
and give `"path": "data/incoming/<lane>/register_<key>.csv.gz"`.

Registers wanted (each line is one descriptor; take any, say which in the lane's inbox):

- liquor licences: British Columbia (LCRB), Québec (RACJ), Alberta (AGLC), Ontario (AGCO), Manitoba (LGCA), Saskatchewan (SLGA), Nova Scotia
- business licences of more cities: Surrey, Burnaby, Richmond, Victoria, Kelowna, Saskatoon, Regina, Winnipeg (no licence number in its
  list: needs one), Ottawa, Mississauga, Brampton, Hamilton, Halifax
- delegated authorities and regulators that send a bill: AMVIC and VSA (vehicle dealers), ESA / ECRA (electrical contractors), HCRA
  (home builders), TICO (travel), RHRA (retirement homes), BAO (funeral homes), RECO / RECA / BCFSA (brokerages), provincial
  engineering, architecture and accounting bodies' firm permits, AMF (Québec financial firms), cannabis retail licences
- federal: Health Canada medical-device licences and establishment licences (manufacturers worldwide), radio licences (ISED's spectrum
  licence data: licensee, address, yearly fee invoiced), the Canadian Civil Aircraft Register (corporate owners: NAV CANADA bills each by
  the year), CNSC licensees, CRTC broadcasting licensees, Canadian Energy Regulator / Alberta Energy Regulator licensees (yearly levy invoiced)

A body that says it sends no invoice is not a lane: the Ontario Motor Vehicle Industry Council prints "OMVIC does not issue invoices".
Check the body's payment page first.

## Format 2 — a roster (who pays a Canadian body, listed by that body, with each one's website)

Members of a chamber or an association, dealers of a manufacturer or distributor, tenants of a landlord or a market, exhibitors and sponsors
of an event. The roster links each organisation's own site, so nothing has to be tied: these lanes turn into rows fastest.

Hand in **two files**: `contrib/<lane>/rosters/<key>.json` and `data/incoming/<lane>/roster_<key>.csv` (or `.csv.gz`).

```json
{"key": "ca_pdac_2027_exhibitors", "kind": "exhibitor",     "_kinds": "member | dealer | tenant | exhibitor | sponsor",
 "biller": "Prospectors & Developers Association of Canada", "biller_site": "https://www.pdac.ca/",
 "biller_address": "800-170 University Avenue, Toronto, ON M5H 3B3", "biller_address_url": "https://www.pdac.ca/contact",
 "biller_address_quote": "the sentence of that page that prints the address, at most 300 characters",
 "read": "2026-11-12",
 "pays_quote": "the body's own sentence that the listed party pays it, or how it bills (booth fee, dues, invoice, payment terms)",
 "pays_url": "the page of that sentence",
 "list_name": "the exhibitor list of the PDAC 2027 convention"}
```

CSV columns: `listed_name, listed_website, listed_address, list_url, ref` (`ref`: booth, member, dealer or unit number when the roster
prints one). `tools/roster_ingest.py` checks the proof itself (`python3 tools/roster_ingest.py check` shows what it would take).

Rosters wanted:

- **exhibitors and sponsors of trade shows and conferences run by a Canadian organiser** — the largest family: hundreds of events, each
  with 100 to 2,000 companies from everywhere, each with its website, a booth number and a published booth rate
- **member directories** of Canadian associations and chambers that are not on GrowthZone / ChamberMaster (those are read by
  `member-live.yml`): WildApricot, MemberClicks, YourMembership, custom directories
- **dealer and distributor locators** of Canadian manufacturers and of the Canadian subsidiaries that invoice dealers: recreational
  vehicles, farm and construction equipment, outdoor power equipment, boats, bicycles, fireplaces, hot tubs, windows and doors, furniture,
  paint, tires; franchise and banner networks (real-estate brokerages, mortgage brokers, building-supply buying groups, retail co-operatives)
- **tenant directories** of Canadian landlords: shopping centres, office buildings, public markets, business-improvement areas (levy payers)

## Format 3 — how a biller bills and is paid (one body a file)

The test of a row asks how the bill is paid. For a body behind many rows, read its own "how to pay" page and hand in
`contrib/<lane>/payees/<key>.json`:

```json
{"names": ["the body's name exactly as rows carry it in the column vendor"], "hosts": ["its-site.ca"],
 "url": "the page", "read": "2026-11-12",
 "period":   "…“Chaque année, vous devez payer votre licence pour la maintenir.”",
 "delivery": "a notice of assessment by mail: “…”",
 "payment":  "through a financial institution or by cheque: “…” … “…”",
 "terms": "“Payment is due 30 days from the date of the invoice.”", "unpaid": "“…”", "remit_to": "“…”",
 "no_invoice": "only when the body says it sends none: “…”"}
```

Every sentence between “ ” must be on the page, word for word, at most 300 characters each. `tools/payee_billing.py verify` opens the page
with the project's reader; an entry is used only after every quote was found (`data/incoming/claude/payee_verified.json`).

The billers behind the most rows that still lack this (2026-11-11): the Canadian Intellectual Property Office, the City of Toronto, the
City of Vancouver (its page refuses robots: leave it), the Better Business Bureaus of Canada, the Corporation des maîtres électriciens
du Québec, the Corporation des maîtres mécaniciens en tuyauterie du Québec, the Office de la protection du consommateur, the firms of
patent and trademark agents (Gowling WLG, Borden Ladner Gervais, ROBIC, Oyen Wiggs, Moffat & Co., Marks & Clerk, Fasken, Osler, Norton
Rose Fulbright, Lavery), and every chamber of commerce with more than 100 member rows.

## Records that are already in the dataset's own format

Contract awards and payments by public bodies to Canada-located vendors keep going in as before (`records_<source_key>.jsonl.gz`,
docs/SCHEMA.md): council award resolutions, municipal purchase-order and cheque-register data, US state and city payment books whose
vendor address says Canada, customs declarations that name a Canadian exporter (Colombia is built: Peru, Ecuador, Uruguay, Paraguay,
Costa Rica, Ukraine), US UCC financing statements whose secured party has an address in Canada.
