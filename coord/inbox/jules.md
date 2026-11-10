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
