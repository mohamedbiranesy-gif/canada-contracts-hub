# Prompt for Gemini — build the "Canadian-vendor ongoing contracts" pipeline (maximum-coverage edition)

You are a senior data engineer. Build a production-quality, resumable Python pipeline that finds **every contract worldwide where the vendor (supplier) is located in Canada and the contract is currently ongoing**, and attaches **every publicly available detail about the contract, the buyer and the vendor**. Coverage must be exhaustive. Every value must be sourced and verifiable. Read this whole brief before writing code. It records what an earlier build learned the hard way: which sources work, their exact quirks, and where naive approaches break.

---

## 1. Definitions (binding)

- **Reference date:** a parameter (default today, e.g. 2026-10-25).
- **Vendor located in Canada:** decided from the source's own vendor **country/address field**: country = Canada/CAN/CA *in a country field*, a Canadian province/territory code or name in a province/state field, or a Canadian postal code (`A1A 1A1`). **Never infer from the company name.**
  - A second, labelled basis is allowed: a strong match to a Canadian business registry entity with a Canadian registered address.
  - Records whose source publishes no vendor location go to a separate "vendor_country_unverified" output.
- **Buyer:** must be a **named** organization. Anonymized buyers ("undisclosed", "identity not disclosed") and placeholder vendors ("INDIVIDUAL CONSULTANT", "REDACTED", "Various", "SEE SUPPLIER NOTES", blank, or a withheld name) go to a separate "parties_not_identified" output.
- **Status:**
  - `ongoing`: start (or award/sign date) ≤ ref date ≤ an explicit published end date.
  - `ongoing_inferred`: no explicit end, but an end can be computed from a published duration or term ("36 months", "three-year contract"), a framework/ordering period, a project closing date, or the parent award's period. Always store the arithmetic.
  - `end_date_unknown`: award published, nothing about the end. Keep these and flag them.
  - Exclude records that have ended, are cancelled or terminated, or haven't started yet.
- **Confidence grade** on every record:
  - `high`: explicit end date.
  - `high_flagged_date`: explicit end date but a placeholder like 9999-12-31 or 2099.
  - `medium`: computed end.
  - `low`/`very_low`: inferred only from the absence of a closure record — the Quebec SEAO convention. Low = concluded in the last ~3 years; very low = older.
  - `unknown`: no end information.
- **Every record carries:**
  - `status_basis`: one sentence naming the exact fields and comparison used.
  - `link`: the record's own page if one exists, else the notice/project page, else the dataset page.
  - `raw`: every source field verbatim, including amendment/transaction rows as lists.

## 2. Output schema (JSON Lines, one object per contract)

```json
{
  "record_id": "<source_key>:<stable id>",
  "source": {"key": "", "name": "", "publisher": "", "dataset_url": "", "record_url": "", "retrieved_at": ""},
  "status": "ongoing | ongoing_inferred | end_date_unknown",
  "status_basis": "",
  "status_confidence": "", "status_confidence_basis": "",
  "link": "", "link_type": "",
  "contract": {"identifiers": {}, "title": "", "description": "", "instrument_type": "", "procurement_method": "",
               "solicitation_procedure": "", "commodity": {"<scheme>": "<code>", "<scheme>_description": ""},
               "value": 0, "currency": "ISO4217", "value_detail": {},
               "dates": {"published": "", "signed": "", "start": "", "end": "", "amended_last": ""}, "related": {}},
  "buyer": {"name": "", "country": "ISO2", "type": "", "identifiers": {}, "address": {}, "contact": {}},
  "vendor": {"name": "", "country": "CA", "country_basis": "<field + value used>", "identifiers": {}, "address": {}, "contact": {}},
  "vendor_enrichment": {"registry ids, business number, derived GST/HST, registered address, licences, website, phones, role e-mails — each with source + match confidence"},
  "buyer_enrichment": {"website, identifiers, address, ap_contact {emails, invoice_portal, invoicing_requirements, evidence[] with page_url + retrieved_at}, procurement_contact, general_contact"},
  "cross_source_matches": [{"record_id": "", "evidence": ""}],
  "raw": {}
}
```

Also produce:
- a vendor table, keyed by `vendor_key`, holding every registry candidate with its full raw row;
- a buyer table, keyed by `buyer_key`;
- a per-source coverage note: URLs, retrieval times, row counts, how vendor country and status were decided, gaps;
- a per-field fill-rate report.

## 3. Architecture requirements ("god mode" means exhaustive, robust, polite — not reckless)

- **Package layout:**
  - `sources/` — one plugin per source: fetch → parse → filter Canada → status → normalize;
  - `enrich/` — registries, licences, websites, buyer AP;
  - `match/` — name/address matching engine;
  - `assemble/` — joins, splits, dedupe flags, fill-rate report;
  - `qa/`;
  - `cli.py` — subcommands such as `fetch <source>`, `normalize <source>`, `enrich vendors`, `enrich buyers`, `assemble`, `qa`, `report`;
  - `config/sources.yaml`.
- **HTTP:**
  - async (httpx or aiohttp) with **per-host rate limiters** (default ≤ 2–3 req/s per host) and a global concurrency cap;
  - retries with exponential backoff on 429/5xx;
  - honour `robots.txt` for crawls;
  - descriptive User-Agent;
  - an on-disk HTTP cache; every fetched page saved, with its hash, for evidence.
- **Resumability:**
  - every crawler checkpoints and skips work already done;
  - outputs are written incrementally (append + flush) so an interruption never loses work.
- **Scale:**
  - stream large files — never hold a 600 MB CSV or a 2.6 GB JSONL in memory;
  - use DuckDB or SQLite for joins over hundreds of thousands of rows;
  - Parquet for intermediates;
  - gzip raw downloads after parsing;
  - the earlier build ran on 2 CPUs / 8 GB RAM / ~40 GB disk, and memory blew up when a whole registry with raw rows was loaded alongside other jobs — join files in lockstep or via a database instead.
- **Logging and run statistics** per source: rows read, kept, excluded by reason, and country values seen.
- **Tests:**
  - unit tests for the status logic, the country rule, and name normalization;
  - golden-sample tests per source.
- **Never** bypass CAPTCHAs, bot challenges (Cloudflare, Incapsula/Imperva, Radware, Akamai 403s, reCAPTCHA) or logins. Detect them, log them, skip.
- **Never** decode obfuscated (Cloudflare-protected) emails.
- **Never** collect personal mailboxes or personal phone numbers.

## 4. Contract sources — what works, with the quirks that matter

### Canada — federal
- **Proactive Disclosure of Contracts** (open.canada.ca dataset `d8f85d91-7dec-4fd1-8055-483b77225d8b`, `contracts.csv` ~640 MB; the resource URL 302-redirects to blob storage, so follow redirects; schema JSON at `https://open.canada.ca/data/recombinant-published-schema/contracts.json`).
  - One row per contract **or amendment**: group by `owner_org` + `procurement_id` (fall back to `reference_number`).
  - `delivery_date` = end date; `contract_period_start` = start; `country_of_vendor` is ISO-2 (≈420k rows blank); `vendor_postal_code` holds only the 3-character FSA.
  - `instrument_type`: C, A or SOSA.
  - End years like 2099/2201/9999 → `high_flagged_date`.
  - Per-record page: `https://search.open.canada.ca/contracts/record/<owner_org>,<reference_number>`.
- **CanadaBuys open data** (`https://canadabuys.canada.ca/opendata/pub/`):
  - `contractHistoryComplete-contratsOctroyesComplet.csv`, `awardNoticeComplete-avisAttributionComplet.csv`, `tenderNoticeComplete-…`;
  - legacy files: `2009-2023-contractHistoryHistorical-…`, `2012-2022-awardNoticeHistorical-…`;
  - data dictionary `achatscanada-canadabuys-dd.xml`;
  - the supplier country field is free text (CA, Canada, CANADA, Cananda, Canda…) — normalize it;
  - notice pages `https://canadabuys.canada.ca/en/tender-opportunities/award-notice/<referenceNumber lowercased>`; the site's WAF intermittently returns 403 to scripts (retry gently, never hammer); legacy references containing `:` or `/` have no page;
  - match across sources on contract number (CW…, W8482-…), solicitation number only when unique.
- **Gaps worth adding:**
  - standing offers / supply arrangements (active, with validity dates);
  - Crown corporations' own quarterly "contracts over $10,000" disclosures (CBC, Canada Post, VIA Rail, BDC, EDC, FCC, CMHC, NCC, museums, House of Commons, Senate…);
  - the Canadian Commercial Corporation's quarterly signed-transactions PDFs (they don't name the foreign buyer → parties-not-identified bucket).

### Canada — Quebec
- **SEAO** open data (Données Québec dataset `systeme-electronique-dappel-doffres-seao`, 438 resources):
  - XML yearly/monthly 2009-01 → 2024-05, including `Contrats_*.xml` "information finale" closure records;
  - OCDS-style monthly/weekly JSON from 2021-03 (supplier `pays` CAN/USA codes, NEQ, `contracts[].period.endDate`, contract status active/terminated).
  - There is no planned end date in the XML. Closure records are incomplete and published years late, so "no closure record" is weak evidence (low/very_low).
  - Use OCDS `period.endDate` where present (`high`).
  - Pair XML ↔ JSON suppliers by NEQ, then by name.
  - ~331k records; holds every Quebec public body and municipality.

### Canada — other provinces/territories, municipal and broader public sector
- **BC:** "Ministry Contract Awards" (BC Data Catalogue, CSV with supplier address, no end dates). The BC Bid awards tab is reCAPTCHA-protected — don't use it.
- **Alberta:** Alberta Purchasing Connection `purchasing.alberta.ca` (public awarded opportunities, crawlable), plus open.alberta.ca "Sole-source service contracts" (explicit dates).
- **Saskatchewan:** SaskTenders `www.sasktenders.ca` awarded competitions (use the `www` host; the bare host fails TLS).
- **Newfoundland and Labrador:** Public Procurement Agency semi-monthly "Contract Awards Reports" PDFs (term of contract column).
- **NWT:** "Contracts over $5,000" report.
- **New Brunswick:** NBON is at **`https://nbon-rpanb.gnb.ca/`** (the old `nbon.gnb.ca` no longer resolves); NB open data at `https://open-data-gnb.hub.arcgis.com/`.
- **Manitoba:** open data at **`https://geoportal.gov.mb.ca/`**; Manitoba awards are on MERX.
- **Ontario:** the Ontario Tenders Portal has no public award listing. Ontario "Enterprise Vendor of Record" arrangements (data.ontario.ca) carry no vendor address.
- **Nova Scotia:** "Awarded Public Tenders" (Socrata `data.novascotia.ca` `m6ps-8j6u`), with no supplier location → unverified bucket unless a registry match places the vendor in Canada.
- **Cities:** Toronto (Bids Awarded + Non-Competitive) and Ottawa (delegated-authority awards) publish no vendor address → unverified bucket.
- **Aggregators (largest municipal/BPS yield):**
  - **bids&tenders:** listing `https://opportunities.bidsandtenders.com/bid-opportunities/Embed?status=Awarded&page=N&pageSize=50&sort=UtcClosingDate&dir=DESC` (~102k awarded bids across ~365 portals). Detail pages `https://<client>.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/<uuid>` embed Ext.NET JSON stores with the awarded vendor's Address/City/ProvinceState/PostalCode/Country/Value, a "Duration in months" field and the award date (→ `ongoing_inferred`).
  - **MERX:** public "Awarded Solicitations" + per-solicitation award tab `https://www.merx.com/public/solicitations/<id>/abstract/award` (awardee address block, contract dates, contract number). Occasional 403 = restricted solicitation; retry once, then skip.
  - **Biddingo** (public no-auth API).
  - Bonfire portals are Cloudflare-challenged on award pages — skip.

### United States
- **USAspending** (`https://api.usaspending.gov/api/v2/bulk_download/awards/`):
  - filter `recipient_locations: [{"country": "CAN"}]`, prime award types A, B, C, D plus IDVs, by fiscal year; poll `download/status`;
  - **subawards** filtered on the sub-recipient location;
  - end = `period_of_performance_current_end_date` (IDVs: ordering-period end; IDV "value" is a ceiling);
  - exclude awards whose latest action is a cancellation/close-out/full termination;
  - subawards have no end date — infer from the prime's end;
  - permalink `https://www.usaspending.gov/award/<contract_award_unique_key>/`;
  - the Canadian Commercial Corporation appears as prime for many Canadian suppliers.
- **State/local:** do a **systematic sweep**:
  - Socrata Discovery API `https://api.us.socrata.com/api/catalog/v1` (terms: contract, purchase order, vendor, award, procurement, checkbook), data.gov CKAN `catalog.data.gov`, ArcGIS Hub;
  - keep datasets with vendor country/state/postal columns; query Canadian provinces server-side.
  - **Pitfall:** in a US state column, `CA` = California. Canada only via a country column, a province code or name, or a Canadian postal code.

### Europe, UK, Australia, NZ, rest of world
- **TED:** `POST https://api.ted.europa.eu/v3/notices/search`, query `winner-country=CAN OR organisation-country-tenderer=CAN` (eForms codes are alpha-3), plus legacy XML/CSV packages for 2015–2023. Durations: BT-36/BT-536/BT-537.
- **UK:**
  - **Contracts Finder** (OCDS search API + daily CSV; supplier address is one free-text string — "Canada Square"/"Canada Water" are London streets, so require "Canada" as the country or a Canadian postal code + province);
  - **Find a Tender** `GET /api/1.0/ocdsReleasePackages?updatedFrom=…&stages=award` (supplier `address.country`). Collapse duplicate awards repeated across UK5/UK7/F03 notices.
  - Dedupe CF vs FTS on vendor + buyer + value/dates.
- **AusTender:** OCDS API `https://api.tenders.gov.au/ocds/findByDates/contractEnd/<from>/<to>` (an end-date index captures everything still running). Supplier `countryName`. API instants are UTC: convert to Australia/Sydney dates.
- **NZ GETS:** the MBIE open-data CSVs sit behind an Incapsula challenge (don't bypass); GETS award pages list some supplier addresses.
- **OCDS publishers** (Open Contracting registry), plus Prozorro (Ukraine), Mexico, Colombia SECOP II (Socrata), Brazil PNCP, Chile, Peru, Paraguay, Spain PLACSP ATOM, Switzerland SIMAP, Norway/Denmark/Sweden via opentender — use only where supplier country is structured.

### International organizations
- **UNGM** contract awards: public search, supplier-country filter (Canada = option value 2328); no end dates.
- **World Bank** Finances One API (datasets DS01004 etc.; the old Socrata `kdui-wcs3` is gone) plus the Projects API for project closing dates; the procurement-notice feed gives contract durations.
- **IDB:** `data.iadb.org` datastore. **Pitfall:** Canada's code is `CD`, while `CA` means Central America — filter on the country *name*.
- **EBRD, ADB, AfDB, EIB, UNDP, UNICEF, UNOPS, WHO, FAO, UN Secretariat, NSPA/NCIA, ESA:** use their own award lists; most give no end date.

### Private sector
- Press releases (newswire.ca/CNW, GlobeNewswire, Business Wire, PR Newswire, ACCESS Newswire, company newsrooms):
  - keep signed contracts with a **named** counterparty and a stated term;
  - exclude M&A, financings, MOUs/LOIs, grants and unnamed "leading customer" deals;
  - vendor location from the dateline or "About" headquarters statement.
- **SEC EDGAR full-text search:** material agreements of Canada-located filers (8-K Item 1.01, 6-K, EX-10).
- SEDAR+ is behind a Radware bot block — don't use it.

## 5. Vendor enrichment (attach to every vendor; label every match exact/strong/weak with its basis)

- **Corporations Canada federal corporations** — open.canada.ca dataset `0032ce54-c5dd-4b66-99a0-320a7b5e99f2`; CSVs `https://d4bf66bykfyaf.cloudfront.net/corporations-{active|inactive-or-dissolved}-{cbca|non-cbca}-en.csv`.
  - Provides corporation number, **Business Number (BN9)**, status, registered office.
  - Detail page `https://ised-isde.canada.ca/cc/lgcy/fdrlCrpDtls.html?corpId=<n>`.
- **Registraire des entreprises du Québec** — Données Québec `registre-des-entreprises`, `JeuDonnees.zip`: Entreprise.csv, Nom.csv (current *and* former/other names), Etablissements.csv, DomaineValeur.csv (code tables).
  - Provides NEQ, legal form, status, employee band, activity codes, addresses.
  - "Other names" cause false matches: require city or postal-code agreement for name-only matches.
  - For sole proprietorships, omit street addresses (privacy).
- **BC OrgBook** API `https://orgbook.gov.bc.ca/api/v4/search/topic?q=<name>&inactive=any&revoked=false`: registration number, **BN**, status, entity type, home jurisdiction.
  - Use it for BC vendors.
  - Also use extraprovincial registrations (type `A`) for out-of-province companies: accept only when `home_jurisdiction` = the vendor's province.
- **RBQ active licences** (Données Québec `licencesactives`, CSV ~330 MB, one row per licence × sub-category):
  - licence number, categories, phone, email, address, **NEQ** (join on NEQ);
  - omit phone/email/street for "Personne physique".
- **CRA charities, latest list** (open.canada.ca "2024 List of charities": `ident_*.csv` with BN/registration number + address, and `weburl_*.csv` websites). Don't use the directors file (personal names).
- **GLEIF LEI** API (filter legal/HQ country CA): LEI, registration authority + number (exact joins to corporation number/NEQ), addresses, parents.
- **Wikidata** SPARQL: official website, LEI, ticker, parent.
- **Health Canada** MDEL/DEL establishment licence lists.
- **Federal lobbying registry:** organizational addresses/phones.
- **Canadian Importers Database.**
- **City business-licence datasets** (Toronto publishes business phone).
- **USAspending recipient data:** UEI, CAGE, DUNS, parent UEI.
- **GST/HST:**
  - no public list exists;
  - `gst_hst_account_derived = BN9 + "RT0001"` is the usual first GST/HST account, *derived not published*;
  - the CRA GST/HST Registry, which confirms one, uses **hCaptcha** — do NOT automate it; tell users to confirm manually.
- **Website discovery** (the earlier build verified ~25–30% of vendors this way):
  - candidate domains from the vendor's distinctive name words (`.ca`/`.com`, joined/hyphenated, with and without "canada"), plus domains of emails already published for the vendor (skip free-mail domains);
  - **accept only if the site shows the company name AND a location match** (vendor postal code, city or province from the contract data/registry);
  - label redirects to another domain as `verified_via_redirect`;
  - then read homepage + up to 3 contact/about pages;
  - keep only **role mailboxes on the site's own domain** (info@, sales@, contact@, accounting@, billing@, ar@, admin@, support@, orders@, quotes@ …) and main phone numbers;
  - drop personal-looking addresses (first.last@, initial+surname@);
  - most guessed domains don't exist, so use short timeouts and spread load across hosts.
- **Name matching engine:**
  - accent/case/punctuation folding;
  - canonical legal suffixes (INC/LTD/LTÉE/CORP/CIE/S.E.N.C.…);
  - split "o/a", "dba", "faisant affaire sous";
  - strict key (suffix kept) vs loose key (suffix removed);
  - numbered companies ("9123-4567 Québec inc.") are highly distinctive;
  - one-word names are never better than `weak`;
  - score with postal code (exact > FSA) > city > province, minus province conflicts;
  - grade: unique + location agreement = exact; unique strict without location = strong only if distinctive; else weak.
  - **Hand-check 30 random matches per source** and report precision.

## 6. Buyer enrichment (the payer side — "AP email" lives here)

For each buyer organization (group name variants and sub-units under the parent):
- official website, identifiers, address, phone;
- **accounts-payable / supplier-invoicing mailbox**, invoice portal, invoicing requirements;
- procurement contact; general contact.

Sources that worked:
- the PSPC "Direct deposit for government suppliers" table (supplier-payment contact mailbox for ~95 federal departments — label it as payment contact);
- invoicing clauses in free CanadaBuys solicitation documents;
- Treasury IPP agency list (US federal → invoice portal), DoD WAWF/PIEE, VA Tungsten;
- the Quebec MAMH municipal directory;
- the GC organization registry;
- supplier/vendor guides, purchase-order terms-and-conditions PDFs and "doing business with us" pages;
- French searches for Quebec ("facturation fournisseurs", "comptes à payer", "exigences de facturation", "guide du fournisseur").

Every email must be copied from a fetched page with URL + retrieval time + snippet. Never construct addresses from patterns.

## 7. Assembly and QA

- Join enrichment by `vendor_key` / `buyer_key` (normalized name stem).
- **Split outputs:** verified-Canadian; vendor-location-unverified; parties-not-identified.
- Promote unverified records only on a strong Canadian registry match (labelled).
- Add best-contact summaries:
  - vendor: emails, phones, website;
  - buyer: AP email → invoice portal → procurement email → general email.
- Flag likely duplicates across sources — same vendor + buyer + (same value ±1% | same dates | shared identifier) — rather than merging them.
- Produce a per-field fill-rate table.
- Validate every record: valid JSON, unique ids, allowed status values, Canadian vendor, named buyer, link present, `high` ⇒ start ≤ ref ≤ end.
- Split files under the delivery size limit (e.g. < 400 MB gzip).

## 8. Deliverables I want from you (Gemini)

1. An architecture document plus the package skeleton.
2. Full code for:
   - the core (HTTP client, rate limiter, cache, checkpointing, schema, status/confidence logic, name-matching engine);
   - at least these source plugins: proactive disclosure, CanadaBuys, SEAO, USAspending, bids&tenders, MERX, TED, UK FTS, AusTender, UNGM;
   - the enrichment plugins: Corporations Canada, REQ, OrgBook, RBQ, CRA charities, GLEIF, website discovery, buyer AP crawler;
   - assembly + QA.
3. A `sources.yaml` listing every source above, with URL, access method, country rule, status rule and known pitfalls.
4. Tests for status logic, country rule (including the California/Canada and IDB `CD` pitfalls), and name matching.
5. A list of **additional sources** you think are missing, each with a reason and a feasibility check.

Write clean, typed, documented Python 3.11+. Prefer standard, well-maintained libraries (httpx, pandas or polars, duckdb, lxml, ijson, pdfplumber, tenacity, pydantic). Deliver in stages: architecture first, then core, then plugins. Don't skip the quirks above.
