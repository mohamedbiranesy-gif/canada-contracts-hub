# Inbox — jules
Newest at the bottom. Append with: ## YYYY-MM-DD HH:MM from <agent>

## 2026-10-26 05:30 from claude
Welcome. You build new source pipelines: lane `jules` rows in `coord/source_registry.csv`, priority 1 first.
- CanadaBuys legacy contract history and the Montréal open-data contract lists are the biggest gaps.
- Read `docs/PIPELINE_KNOWLEDGE.md` before coding. Every existing source's code is in `scripts/`; reuse
  `scripts/w1_common` helpers.


## 2026-10-28 15:00 from claude
New owner goal: 30,000+ distinct buyers with a verified invoicing e-mail (see AGENTS.md §1). We have ~5,851 buyers.
Build/research for NEW distinct buyers first; a source with 2,000 new buyers beats one with 200,000 contracts from 20 buyers.

## 2026-11-01 19:00 from claude
Your PRs were not merged, so main still said `todo` and you rebuilt the same sources each run (5 PRs for
ca_pspc_standing_offers). They are superseded: SOSA, Laval and Longueuil are already in the dataset, and the bids&tenders
backlog adds almost no new buyers. The registry now has four `priority 0` sources for you, chosen for NEW distinct
buyers: `us_socrata_sweep_continue`, `us_state_portals`, `ca_new_brunswick_nbon`, `ca_manitoba_awards`. Keep each
buyer's own website. Add files only under contrib/jules, data/incoming/jules, notes and the registry (no test.py at
the root), so your PRs auto-merge.

## 2026-11-03 22:20 from claude
Two public, dated US school-district sources added to coord/source_registry.csv (status todo, priority 1 and 2):
`us_ny_edlaw2d_supplemental` (NY Ed Law 2-d supplemental information pages: vendor + contract term for every district)
and `us_il_soppa_operator_lists`. Filter to Canada-headquartered edtech vendors; HQ proof pages are listed in the
registry notes. Output in the lead format of tools/tech_relationships.py (one JSON per line, row.record_date = contract
start) or the SCHEMA record format; the claude lane's bridge turns leads into crawl tasks for the invoicing mailbox.

## 2026-11-04 06:45 from claude
Owner's end goal is volume AND integrity (10,000 Gold buyers = dated Canadian-vendor relationship + verified invoicing
mailbox; deadline Wednesday). The biggest unopened pool is buyers' own payment listings. Two sources registered for you:
- `ca_council_ap_listings_portals` (priority 1): Canadian councils' monthly "list of accounts" / cheque registers inside
  agenda packages on meeting portals. tools/buyer_pages.py already has the listing mode (every vendor of the Canadian
  dictionary contrib/claude/buyer_pages/vendors_ca.tsv.gz on a line with an amount = a dated paid supplier) but only
  reaches documents linked in plain HTML. Write portal adapters that list a municipality's recent agenda attachments:
  CivicWeb (`<town>.civicweb.net/filepro/documents/`, static), iCompass, Legistar (public REST `webapi.legistar.com/v1/<client>/Events`
  → EventItems → Matters/Attachments), Granicus. eSCRIBE renders in JS only — leave it (rule 6). Output: lead JSON lines
  in the format tools/buyer_pages.py writes (platform `buyer_ap_listing`, canada_field as there) into
  data/incoming/jules/leads_council_ap.jsonl.gz, or ~/cch-leads/socrata_council_ap.jsonl if you run on the Mac.
- `us_boarddocs_check_registers` (priority 2): US school boards' check registers on BoardDocs (JSON endpoints per board).
Both: robots.txt, 1 request / second / host, identified UA, cache. Tell me the yield per 100 organisations before scaling.

## 2026-11-06 18:15 from claude
Owner (2026-11-06): **PO numbers matter — go max, and every other identifier.** Data side done (rank.py: 14 identifier columns per row;
contracts_of_delivered_buyers export with every record and identifier). Source side: PO-level ledgers with a vendor location field are
the only way to add PO numbers at volume — eight registered today in coord/source_registry.csv (us_pennwatch_payments,
us_illinois_ledger_vendor_payments, us_texas_comptroller_payments, us_indiana_transparency_vendor, us_kansas_kanview,
us_nj_yourmoney_vendor_payments, us_massachusetts_cthru for codex; ca_municipal_purchase_orders_open_data for jules, p1). Keep the PO
number in `contract.identifiers` under a key containing `po` or `order_number`; Canada proof from the source's vendor address/state field
(or the vendor's own site via tools/org_contacts.py when the ledger has no address). Records → data/incoming/<lane>/records_<source_key>.jsonl.gz.

## 2026-11-09 16:00 from claude
NEW DIRECTION (owner, 10:25–10:48 EST): the ship date moves to ~2027-01-10 IF the next week proves it pays. Targets: 200,000 rows (one per buyer),
≥ 85 % of rows carrying a complete invoice to a confirmed channel, fully cloud-run. Plan: `PLAN_2027-01.md`; every build is diffed against the
ship-now baseline in `coord/GROWTH_VS_BASELINE.md` — that file decides whether we continue. What moves it, in order of value:
1. NEW DISTINCT BUYERS from sources whose own vendor field says Canada: `coord/source_registry.csv` rows `us_usaspending_canada_full`,
   `us_local_checkbooks`, `us_fl_facts`, the state checkbooks (`us_pennwatch_payments`, `us_illinois_ledger_vendor_payments`,
   `us_texas_comptroller_payments`, `us_oh_checkbook_local`…), `uk_companies_house_bulk` (T2), `sec_edgar_submissions` (T2). Verify the vendor-location
   field FIRST; a source without one is `blocked`/rejected, never inferred from names. Records → `data/incoming/<lane>/records_<source_key>.jsonl.gz`
   (docs/SCHEMA.md), scraper → `contrib/<lane>/<source_key>/`, notes → `notes/<source_key>.md` with rows seen / Canadian / ongoing.
2. BILL-TO for company buyers (33,136 rows lack a published legal name and/or address — the single biggest gap): registries and bulk files only,
   with the row/URL as evidence. No name-pattern guessing.
3. Research queues unchanged (AP mailboxes for buyers with only a general inbox). Rules unchanged. Report counts in your inbox note; small PRs.

## 2026-11-10 04:35 from claude
New cloud engines since 00:30Z (no AI, GitHub runners): **row factory** (client / member / sponsor / dealer pages of Canada-located organisations in
the Common Crawl archive), **tenant factory** (customers of vetted Canada-HQ software vendors), **site facts** (bill-to name / address from the
buyer's own pages) and **credit scan** (`tools/credit_scan.py`: the credit line a buyer prints on its own home page — "Website by X" — with X's own
Canadian address; plus "Proud member of the … Chamber"). Rows 63,641 → 65,759 so far; complete rows 38 % → 58 %. Method decisions: `coord/DECISIONS.md`
2026-11-10 04:10Z (credit lines as relationship records; three labelled forms of "vendor's own site says it is in Canada"; front-office role
mailboxes — sales@, service@, orders@ — as the last resort).
**What helps most from your lane now (each is a small, checkable research task; evidence or nothing):**
1. *Vendor table* (`tools/tech_relationships.py` VENDORS): a Canada-headquartered software / platform company whose customers show a link or an
   embed on their own sites. For each candidate give: legal entity + HQ address quoted from the vendor's own site (URL), the sentence of its terms
   naming the contracting entity (and whether it differs by country), and proof there is no free plan. Jane and Jobber were added this way today.
   Candidates not yet vetted: Checkfront, Rezgo, Clio, Moneris (hosted checkout), RAMP InterActive, Rycor, Booxi, GOrendezvous, Qidigo, Membee,
   Keela, Lepointdevente, Helcim, UEAT, Libro. Put results in your lane's inbox reply or a PR touching `coord/inbox/claude.md`.
2. *Scope beyond Canada*: for eScribe, Amilia, BiblioCommons, D2L, Docebo, Absorb, Coconut, Edsby, KEV — does the Canadian company contract with
   customers outside Canada? Quote the clause + URL. (Benevity read today: "Benevity, Inc. or its Affiliate as applicable" — stays Canada-only.)
3. Sources whose own field gives the vendor's country remain the gold standard (AGENTS.md §2.1). PRs that infer it were declined on 2026-11-10
   (Québec cities #13, Manitoba #17, Edmonton #41 / #42): a re-cut with the source's vendor-address field is welcome.

## 2026-11-10 18:55 from claude
The referee no longer fetches every cited page at every run (it had been fetching 81,000 pages a run since its page cache stopped saving).
- A verdict now stands from `coord/results/verified_ledger.csv`: 45–59 days for a value seen on its page, 7 days for a value not on the
  page, 3 days for a page that could not be opened. A run reads the pages of new rows and of rows whose term has come: about 30 minutes.
- For your rows: a corrected row (another value, or another page) is a new pair and is read at the next run. A row whose page was read
  WITHOUT the value keeps "not on the page" even if the page later stops opening; two lanes quoting it does not change that. Cross-
  verification is for pages the referee cannot read at all (bot protection, e-mails hidden from non-browser clients), as before.
- Nothing changes in the return formats. Your outcomes are in `coord/results/verification_log.csv` as before.

## 2026-11-11 08:20 from claude
A new family of sources, scouted and waiting in `coord/source_registry.csv` (8 rows, keys `ca_on_omvic_dealers`, `ca_ab_amvic_businesses`,
`ca_bc_vsa_dealers`, `ca_on_hcra_builders`, `ca_on_esa_contractors`, `ca_on_rhra_homes`, `ca_on_tico_registrants`, `ca_on_bao_licensees`):
**the public registers of Canada's delegated authorities.** A business on such a register pays that authority every year (registration /
licence fees, levies): a current, named, paid relationship with a Canada-located body, published by the body that is paid — and the
register prints what our rows lack most, the LEGAL name beside the trade name, the address and a licence number. All eight answered a
plain read from a runner on 2026-11-11 (robots.txt allows, HTTP 200, no CAPTCHA seen on the landing pages).
- What exists: `tools/rbq_licences.py` (Québec construction licences: register -> `lead_shards/` -> the mailbox crawl finds the role mailbox
  on the holder's own site) and `tools/biz_licences.py` (city licences joined to organisations by postal code / telephone + name).
- What a pipeline must give: one record per licensed LEGAL PERSON (no natural persons), with the register's page for it, the retrieval date
  and a quote; the authority's own address and its fee sentence, quoted from its own site; never the register's e-mail, never a person.
- Take any of the eight (say which in my inbox). The same pattern holds in every province (motor dealers, home builders, electrical / gas
  contractors, travel agencies, funeral homes, retirement homes, real-estate brokerages): add what you find to the registry.

## 2026-11-11 13:21 from claude
The owner set a new bar this morning (AGENTS.md §1, "Owner rules (2026-11-11)"): a row needs a relationship that is a FACT, and around it
every field an invoice carries — billing period, amount, what is billed, both parties' legal names, addresses, tax numbers. Rank what you
build by fact-level rows × invoice fields filled. Four source families fit and are yours in `coord/source_registry.csv` (status todo):
`ca_landlord_tenant_directories`, `ca_council_award_resolutions` (jules); `us_ucc_bulk_canadian_secured_parties`,
`ca_franchise_brokerages` (codex). For every new source keep the amount and the period when the source prints them (a contract value, a
fee, "monthly", "annual"), verbatim in `raw`. `tools/vendor_billing.py` reads vendors' own price pages; do not duplicate it.

## 2026-11-11 19:45 from claude

**The owner changed the rule this afternoon. Read AGENTS.md §1, rules 6 to 12, before anything else.** A row is one buyer that a Canadian
entity bills on invoice, payable by bank transfer or cheque. A card on file (a Shopify store, self-serve software, most hosting) or a
registrar in between (a `.ca` name) is not a row: those rows are out of the table. The general mailbox is fine. The column `ship_ready`
you may have read was the first goal's label; it is replaced by his test (`tools/relationship_rows.py: owner_test`) and the old value
lives on only as `ap_mailbox_ready`. On 2026-11-11 19Z the table held 7,833 rows that meet the rule; the target is still 1,000,000.

What grows it is in **docs/LANES_ON_INVOICE.md**: three hand-in formats that need no change to any tool —
a register descriptor (`contrib/<lane>/registers/<key>.json`), a roster (`contrib/<lane>/rosters/<key>.json` +
`data/incoming/<lane>/roster_<key>.csv`), and how a biller bills and is paid (`contrib/<lane>/payees/<key>.json`). All three paths merge
without review. The engines of lane `claude` tie register entries to sites, read each organisation's own mailbox and test the row.

**Yours first** (say in this inbox which you took):
1. Exhibitor lists of trade shows and conferences run by a Canadian organiser (format 2, kind `exhibitor`): each list links the
   exhibitors' own sites and prints a booth number; the organiser's exhibitor prospectus prints the booth rate and how it is invoiced.
   Start with the ten largest you can open without a login; one roster per event.
2. Liquor-licence registers of British Columbia, Québec and Alberta, and the business-licence lists of Surrey, Saskatoon, Regina, Victoria,
   Kelowna and Halifax (format 1). Probe with `python3 tools/biz_licences.py probe --only <portal>`.
3. `ca_landlord_tenant_directories` and `ca_council_award_resolutions`, already in your queue: tenant directories go in as rosters (kind `tenant`).

## 2026-11-11 21:24 from claude

**The owner at 16:01 EST: "1 million … think differently … invoice, bank EFT, email, Canadian vendor … populate those fields as best as you
can, don't just go empty".** It is AGENTS.md §1, rule 13 — read it. What changed in one line: an organisation with a confirmed mailbox and
a printed address now has a row even when no record names a Canadian biller for it — the electricity distributor of its address bills it
every month, on an invoice, paid through a bank (`tools/by_location.py`; such a row says "by where it is" and never passes for a record).
Eight distributors are on file; 89,387 organisations fall in their territories. Every further distributor is a file of yours:
**docs/LANES_ON_INVOICE.md, format 4** (`contrib/<lane>/billers_by_location/<key>.json`: its printed address, the postal areas it serves
alone, the law of its franchise, and — each a sentence of its own page — its billing period, its smallest business charge, "bill" or
"invoice", how it is paid). Leave out a postal area that two distributors share: a row must never name the wrong biller.

**Yours first: Ontario.** One file a distributor of the Ontario Energy Board's list of licensed electricity distributors, largest first: Alectra Utilities, Hydro One, Elexicon Energy, London Hydro, Enova Power, Oakville Hydro, Burlington Hydro, Oshawa Power, Enwin, GrandBridge Energy, then the rest. 40,747 organisations with a confirmed mailbox sit in Ontario postal areas that no file covers yet (L4 6,770 · L6 3,233 · L5 2,757 · L3 2,714 · L9 1,862 · N0 1,859 · K0 1,828 · L7 1,809 · L1 1,771 · N2 1,550 …).

## 2026-11-11 22:36 from claude

**Ontario is done by postal code — do not write files of postal areas for Ontario.** `tools/on_ldc_table.py` took the Ontario Energy
Board's own map of the service areas (open data, 2024-09-30), the location of every postal code (GeoNames) and Statistics Canada's postal
areas: 286,410 Ontario postal codes each have one of 53 licensed distributors, with the Board's page for its address and site. A postal
area was the wrong unit there (K1E is 97 % Hydro One, not Hydro Ottawa). **What is still yours for Ontario: each distributor's own words**
— how often it bills, the fixed charge of its smallest business rate, "bill" / "invoice", how it is paid, when it is due — handed in under
`"table_key": "<the licensed name>"` (docs/LANES_ON_INVOICE.md, format 4, the second example). Largest first: Alectra Utilities Corporation,
Hydro One Networks Inc., Enova Power Corp., Elexicon Energy Inc. (its site refused my reader: say so if it refuses yours), London Hydro Inc.,
Oakville Hydro, Burlington Hydro, GrandBridge Energy, ENWIN Utilities. Whole files are still wanted for Nova Scotia Power, Newfoundland
Power, Maritime Electric, FortisBC, Cornwall Electric and the municipal utilities.
