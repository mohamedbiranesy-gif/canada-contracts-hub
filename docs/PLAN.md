# Max-coverage build plan (v3) — reference date 2026-10-25

Objective: (1) every in-scope contract that any reachable public source publishes; (2) every field about the contract, buyer and vendor that any public source publishes, attached to each contract with provenance; (3) nothing invented, nothing obtained by getting around a bot check, no personal mailboxes.

Baseline (build v2, delivered): 511,762 contracts with verified Canadian vendor + named buyer; 50,896 vendor-location-unverified; 1,831 parties-not-identified; 119,131 vendors; 5,851 buyers. Fill rates on the main file: vendor registry match 74%, BN 24%, vendor website 23%, vendor contact 24%, buyer website 89%, buyer AP mailbox 24%.

## Workstreams

### W1 Contract coverage (new records)
- W1a Canada federal gaps — CanadaBuys legacy contract history (2009-01→2023-05) and legacy award notices (2012→2022) for long-running contracts/standing offers not in proactive disclosure; PSPC/CanadaBuys standing offers & supply arrangements (active, with validity dates); Crown corporations' own contract disclosures (CBC/Radio-Canada, Canada Post, VIA Rail, BDC, EDC, FCC, CMHC, Canada Lands, NCC, Destination Canada, NAC, Telefilm…); any federal body publishing contracts outside the PD file.
- W1b Provinces/territories/municipal/BPS — finish bids&tenders 2015–2020 backlog and MERX backlog; city/provincial open-data award datasets not yet tried (Vancouver retry, etc.); hosts blocked by this session's network allowlist (NB NBON + data.gnb.ca, data.gov.mb.ca) need the user to allow those domains.
- W1c US state & local, systematic — enumerate every Socrata/CKAN/ArcGIS-Hub dataset about contracts/purchase orders/vendors/payments-to-contracts across US portals, detect vendor country/state/postal columns, query Canadian provinces/"Canada", normalize.
- W1d Rest of world + IGOs + private — supplier-country-bearing portals (Prozorro, Mexico, Colombia SECOP, Brazil PNCP, Korea, Israel, Australian states…), IGO own portals (UNICEF, UNOPS, UNDP full history, ADB, AfDB, EIB, NSPA/NCIA, ESA…), private announcements (unreviewed press-release backlog, deeper SEC EDGAR).
- W1e Promote vendor-location-unverified records to the main file when the vendor strongly matches a Canadian registry entity with a Canadian registered address (basis recorded).

### W2 Vendor enrichment (every vendor)
- Done/running: Corporations Canada (BN), Quebec REQ, BC OrgBook (BC + extraprovincial), website & role-mailbox discovery.
- New bulk sources: RBQ licence register (licence no., categories, phone, email, address; joined on NEQ), CRA charities (BN, address, website), GLEIF LEI records for Canada (LEI, legal/HQ address, registration authority IDs, parent/child links), Wikidata (official website, LEI, stock ticker, parent org), Health Canada medical-device & drug establishment licence lists, Canadian Importers Database, federal lobbying registry (client organisations' addresses/phones), city business-licence datasets (Toronto phones, other cities' addresses).
- Second website pass: domains of emails already published for the vendor (contract data, RBQ) and websites from charities/GLEIF/Wikidata → verify → crawl contact pages.
- GST/HST: derived from BN only (CRA registry is CAPTCHA-protected).

### W3 Buyer enrichment (every buyer)
- Deep AP/invoicing search for the 4,830 buyers without an AP mailbox or portal (415k contracts), largest first, French-language searches for Quebec bodies; invoicing clauses in publicly downloadable tender documents; parent-organisation inheritance; buyer phone/address fill.
- Full enrichment of the 104 buyers added by the last crawl.

### W4 Contract/service detail
- Human-readable descriptions for commodity codes (GSIN, UNSPSC, NAICS, PSC, CPV, CAE) where the source gives only codes; tender↔award linking where sources allow.

### W5 Assembly & QA
- One assembly that attaches every enrichment with provenance, best-contact summaries (vendor: emails/phones/website; buyer: AP email → invoice portal → procurement → general), identifiability split, promotion rule, cross-source duplicate flags.
- Per-field fill-rate table in README; random-sample precision checks for each new matcher (≥30 per source); files split under 400 MB.

## Rules (unchanged)
Vendor country from source country/address fields (or, for W1e, a strong registry match with a Canadian address — labelled). Named parties only. Role mailboxes only, copied from a page with URL + date. robots.txt honoured; ≤ 2–3 req/s per host; no CAPTCHA/bot-check circumvention. Never invent values; derived values labelled. Write outputs incrementally (usage limits may interrupt).

## Output contracts for workers
- New contract sources: `normalized/<source_key>.jsonl` + `notes/<source_key>.md` per SCHEMA.md.
- New vendor-data sources: `enrichment/v2/vendors_extra_<source>.jsonl`, one line per matched vendor:
  `{"vendor_key", "source", "matches": [{"match_confidence": "exact|strong|weak", "match_basis", "legal_name", "identifiers": {}, "address": {}, "phones": [], "emails": [{"email", "label", "evidence_url"}], "website", "status", "extra": {}, "source_url", "dataset_url", "retrieved_at", "raw": {}}]}` + `notes/enrichment_<source>.md` (with precision check).
- Buyer deep search: `enrichment/v2/buyers_deep.jsonl` (same layout as buyers_enriched.jsonl, keyed by buyer_key) + `notes/enrichment_buyers_deep.md`.
