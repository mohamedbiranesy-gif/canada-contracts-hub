# Source map — 50,000 different buyers (owner's goal of 2026-11-19)

**A row:** one buyer (any organisation, anywhere), one contract / purchase order / award of more than C$3,000 with a vendor located in
Canada, awarded or started on or after 2023-11-19, billed on invoice, paid by bank transfer or cheque, with the buyer's own mailbox.
**Counted 2026-11-19:** 3,139 different buyers (2,436 in Canada, 703 abroad) in the contract dataset; 1,434 of them from Québec's SEAO.

The machine (`worker/`) only runs what is written here as a job; this map is where the thinking is. The "new buyers" column is a rough
estimate made before any harvest — every job reports its real count in `worker-results/<job>/summary.json`, and this page is corrected
from those counts. Status: **have** (in the dataset), **job** (a worker job exists), **build** (to write), **check** (access to verify first),
**ask** (needs the owner's yes: is it a contract in his sense?).

## A. Canadian public bodies (universe ≈ 10,000 organisations; 2,436 counted)

| # | Source | What it adds | Vendor in Canada by | Est. new buyers | Status |
|---|---|---|---|---|---|
| A1 | Québec municipalities' lists of contracts over $2,000 (mandatory on each municipality's site; MRCs, régies) | small municipalities with no SEAO contract in the window | supplier address on the list, else REQ | 300 | build |
| A2 | BC Statements of Financial Information (every BC public body lists suppliers paid over $25,000 a year) | municipalities, regional districts, school districts, health authorities, colleges, universities, Crown corporations | BC OrgBook / Corporations Canada registration | 300 | build |
| A3 | Contracts already held but rejected for want of a supplier address: Nova Scotia 33,257, Toronto 10,728, Ottawa 5,220, Ontario VOR 1,818, Edmonton | Nova Scotia public bodies, Toronto agencies | registration (Corporations Canada, NS Registry of Joint Stock Companies, Ontario) | 250 | build |
| A4 | bids&tenders (≈600 public bodies), Biddingo, MERX, Bonfire public portals — full award history since 2023 | Ontario and Atlantic municipalities, utilities, school boards, colleges | supplier address on the award, else registration | 600 | have (part) → build |
| A5 | Alberta Purchasing Connection, SaskTenders, Manitoba, New Brunswick (NBON), PEI, Newfoundland, territories — awards since 2023 | prairie and Atlantic MASH sector | supplier address | 800 | have (part) → build |
| A6 | Federal: CanadaBuys award notices, proactive disclosure, Crown corporations' disclosures | the federal bodies not yet in | supplier address | 40 | have (part) |
| A7 | Universities, colleges, hospitals, school boards with their own award pages | the rest of the MASH sector | supplier address | 200 | build |

## B. United States (universe ≈ 90,000 governments, plus companies in subcontract data)

| # | Source | What it adds | Vendor in Canada by | Est. new buyers | Status |
|---|---|---|---|---|---|
| B1 | USAspending prime contracts (recipient located in Canada) | federal sub-agencies (counted as organisations, not offices) | the source's recipient country = CAN | 50 | **job `usaspending_ca`** |
| B2 | USAspending subcontracts (FFATA; sub-awardee located in Canada; 1,801 since 2023-11-19) | US prime contractors and universities buying from Canadian firms | the source's sub-awardee country = CAN | 500 | **job `usaspending_ca`** |
| B3 | Open-data catalog sweep (Socrata discovery API, ArcGIS Hub, CKAN, OpenGov): every "vendor payments", "checkbook", "purchase orders", "contracts" dataset, probed for Canadian vendor addresses | cities, counties, school districts, transit agencies, utilities, universities | vendor state/country/postal code fields | 300–800 | build (`scripts/us_discovery*` to reuse) |
| B4 | State comptrollers' vendor-payment files (agency-level) | state agencies | vendor address fields | 300–600 | build |
| B5 | Legistar / BoardDocs / Granicus council and board agendas naming a contract with a Canadian legal entity | cities and school boards | the Canadian entity's registration (rule 19: a US subsidiary is not Canadian) | ? | check |

## C. Rest of the world, public buyers

| # | Source | What it adds | Vendor in Canada by | Est. new buyers | Status |
|---|---|---|---|---|---|
| C1 | TED (EU/EEA) award notices 2023–2026, winner located in Canada | EU contracting authorities | winner address/country | 300–500 | have (part) → build |
| C2 | EU national data under the TED thresholds: France DECP, Italy ANAC, Spain PLACSP, Germany, Netherlands, Belgium, Poland, Portugal, Nordics (OCDS where offered) | European municipalities, hospitals, agencies | supplier country/ID | 300–600 | build |
| C3 | UK Contracts Finder + Find a Tender, all awards 2023–2026 | UK public bodies | supplier address | 150–300 | have (part) → build |
| C4 | AusTender + Australian states (NSW, VIC, QLD, SA, WA, TAS, ACT) + New Zealand GETS | Australian/NZ public bodies | supplier country | 100–200 | have (part) → build |
| C5 | Development banks: World Bank, ADB, IDB, AfDB, EBRD, CDB, IsDB, AIIB contract awards | borrowers' implementing agencies | supplier country | 300–500 | have (part) → build |
| C6 | UN system and other international organisations (UNGM, UNDP, UNICEF, UNOPS, WFP, WHO, FAO, UNHCR, IOM, NSPA, ESA) | the organisations themselves (one buyer each) | supplier country | 50–100 | have (part) |
| C7 | Open Contracting Data Registry publishers (Latin America, Africa, Asia) | public bodies there | supplier country/address | 100–300 | have (part) → build |

## D. Private buyers

| # | Source | What it adds | Vendor in Canada by | Est. new buyers | Status |
|---|---|---|---|---|---|
| D1 | Customs import declarations that name both sides: Colombia (DIAN), then Peru, Ecuador, Chile, Paraguay, Uruguay, Central America where published | importers buying from Canadian exporters (FOB value per declaration) | exporter country = Canada on the declaration | 500–2,000 | check (Colombia had 47 rows from one month) |
| D2 | Canadian companies' announced contracts (press releases, SEDAR+, EDGAR material contracts) | named customers | the announcing company | 200–500 | have (part) |
| D3 | Industry partners of Canadian university and college research (NSERC Alliance and other partnership programs, Mitacs, OCI, Alberta Innovates): the partner pays its cash contribution to the institution under a research agreement | companies, municipalities, NGOs, foreign firms | the institution | thousands | **ask** + check |
| D4 | Exhibitors of Canadian trade shows (the organiser's exhibitor list; the booth priced from its published rate card) | companies worldwide | the organiser | thousands | **ask** + check |
| D5 | Yearly fees over C$3,000 to a Canadian body: TSX/TSXV/CSE listed issuers, Health Canada drug and device establishment licences, CNSC licences | issuers and licence holders, many abroad | the exchange / regulator | 4,000–6,000 | **ask** |

## E. Sources nobody has named yet

The catalog sweeps (B3, and the same over CKAN/OpenDataSoft/ArcGIS Hub portals worldwide) are how the machine finds spending files that
are not on this page: each dataset whose name or columns look like payments, purchase orders or contract awards is probed for vendors
with a Canadian address, and every hit is written to `worker-results/discovery/` for a session to turn into a job.

## Honest ceiling (estimate, 2026-11-19)

Contracts only (A–C, D1–D2): about **9,000–13,000** different buyers, the 3,139 of today included (the sum of the estimates above). With D3–D5, if they count, the pools
are large enough for 50,000 to be in reach; without them, 50,000 is not reachable from any source named here.
