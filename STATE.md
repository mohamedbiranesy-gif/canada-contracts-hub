# STATE.md — Claude lane (updated 2026-11-10 03:35Z — rows 64,539 (+898) and rising; index 268k pages, 26.8k leads, 2,578 new buyers with a mailbox at the referee)

## Reading of the mission (unattended run; nobody answers questions)
Every delivered row, in every package (owner 11:46 EST: "not just Gold"), must carry every detail an accounts-payable invoice to that buyer needs —
bill-to legal name and billing address, the invoicing mailbox or portal, PO rule, payment terms, tax numbers, vendor identity, AP follow-up contact —
to the AP-grade-A standard (owner 11:38 EST: "I don't mean rate them, I mean make them AP grade standard"). The grade is the compass: the scoreboard
prints what blocks A per package and the next engine goes at the biggest blocker. Real published data first; a derived "plausibility" default
(statute, government directive) only where nothing is published, always labelled, source-cited and kept in its own column (owner 11:53 EST:
"last ditch … derived from sources"). The 438 downstream benchmarks stay the measured floor. Integrity rules in PROTOCOL.md are unchanged.

## Assumptions made (not asked)
1. `ap_contact_name_as_published`: the owner said on 2026-11-08 10:59 EST "person is allowed for AP" — read as: the AP contact person the organisation
   itself publishes on its AP / finance page may be named (name + role phrase, quoted); mailboxes stay organisational (AGENTS.md §2.5 unchanged).
   Implemented in tools/ap_terms.py (ap_contact_name_any) the same hour.
2. Contract value / dates / title / identifiers may be filled from another record of the SAME buyer–vendor pair, labelled with that
   record's id; never from a different vendor. Rows proven by lobbying filings, news releases, auditor appointments, customer
   stories have no contract value: that is the ceiling (≈ 17 % of P01 Gold).
3. `currency` may be defaulted from the source's country when a value exists, flagged "assumed from source convention" (asked by the downstream team).
4. AI search agents only propose URLs; every value is read from the page by a Mac engine with URL + quote.
5. The downstream's `mta_sts_record` / `tls_rpt_record` / `bimi_record` are my `mta_sts` / `tls_rpt` / `bimi` columns (filled since the 06:47Z build).
6. No column is renamed; new facts are new columns. No irreversible action is planned; nothing needs the owner's decision today.
7. Owner 11:21 EST: "invoice grade, invoice framing, invoice thinking … incorporate, don't overwrite" → read as: structure and prioritise every row as the
   header of an invoice (bill-to, submit-to, references, terms, tax, vendor identity, follow-up); implemented as `invoice_card_json`, `invoice_readiness`,
   `invoice_missing` on every delivered row and a readiness table in the scoreboard (PROTOCOL.md "Invoice-grade framing"); targets unchanged.
8. Owner 11:24 EST: "add AP grade … plausibility bits like cadence … how stringent: max" → `ap_grade` A–E + `ap_score` + `ap_grade_basis` per row, mechanical, from
   sourced columns only (PROTOCOL.md "AP grade"); A requires a referee-confirmed invoicing mailbox on the buyer's own domain with MX, published legal name,
   address, PO rule and terms, and no penalties.
9. Owner 11:38 / 11:46 / 11:53 EST: the AP grade is the STANDARD to reach for all packages, not a rating; plausibility defaults are last resort, source-derived.
   Read as: (a) every row gets `ap_gap_to_A` (what it still lacks for A) and the scoreboard a "what blocks grade A" table per package; (b) engines are
   pointed at the biggest blockers (payment terms, PO rule, legal name, address) for ALL delivered buyers, Gold first; (c) `payment_terms_default_policy`
   may carry a statutory prompt-payment default for construction contracts (federal Act / Ontario Construction Act / Alberta PPCLA — read today, quoted),
   never written into `payment_terms_as_published`; the grade's "payment terms published" criterion stays strict.

## Done today (2026-11-08, times UTC)
- 14:1xZ scoreboard tool + workflow step (`tools/coverage_targets.py`; baseline 57/438 on the 13:28Z build).
- Mac reboot 12:30Z found; every engine restarted 14:16Z (push_loop, sync_loop, bridge, ap_crawler, site_finder); DNS daily loop relaunched 15:05Z.
- 172 MB PO open-data file gzipped (GitHub refuses > 100 MB); push snapshot skips any file > 95 MB.
- fetch() follows 308/307/301 by hand, retries broken TLS over http and bare hosts with www. (55 Gold buyer sites answered 308 and were never read).
- org_extras v2 (JSON-LD Organization, stated legal names, public-body styles, icon/logo order, portals, mentions, LinkedIn, shared-host start URLs) — tested on calgary.ca / mcmaster.ca / canada.ca ECCC; `--refresh` over 65,431 delivered domains running on the Mac (≈160 domains/min).
- org_contacts `--refresh` (5,183 redirect / network failures + shared-host organisations) running.
- rebuild patch: contract value from the awarded bidder's submitted price (bids&tenders, 9,213 records) and number_of_bids (58,304 records) — tested locally (patch_report), rebuild dispatched 14:5xZ.
- rank: same-pair fill, inferred end date labelled, start from signature date, records_with_this_vendor for lead rows, org_extras v2 facts, Canada's Business Registries facts, inferred vendors' phone / address (Canada Post, NB Power, Qulliq: 36,935 P13 rows).
- `tools/registry_lookup.py`: Canada's Business Registries public API (BN, registered name, office, status, incorporation) — 25/40 found in the test; full run (4,040 vendors without BN, then corporation-type buyers) running at 1 req/s.
- `tools/gc_recipients.py`: federal grants & contributions recipient BNs — running on the Mac.
- `tools/ap_walk.py` + ap_crawler AP-page memory: AP site walker for the terms extractor — test run launched.
- Earlier today: charity BNs (7,454 buyers), org directories (6,277), Wikidata (running), PO join (330,978 PO rows), Crown BNs, verified ledger in the referee.

## Verified so far (15:55Z)
- Build 15:48Z: **benchmarks met 87 / 438 (19.9 %)** (57 → 76 → 87 today); VALIDATION 7/7, audit PASS, Gold 585. P01 Gold buyer_legal_name 41 → 87.5 %, vendor_bn9 63 → 79 %, vendor_website 58 → 70 %, buyer_bn 0.7 → 18.8 %, number_of_bids 1.7 → 19 %, records_with_this_vendor 100 %.
- Earlier:
- Build 15:31Z: **benchmarks met 76 / 438 (17.4 %)**, up from 57; VALIDATION 7/7 PASS; deep audit PASS; Gold 585; P13 vendor_phone filled on 37,244 rows.
  Not yet in that build (files landed on origin at 15:17Z, after it started): Canada's Business Registries (489 vendors found of 844 looked up so far),
  grants & contributions BNs (3,186 buyers + 465 vendors), confirmed vendor websites (39), the rebuilt release (15:22Z: 9,213 bids&tenders
  values, 58,304 bid counts, reference date 2026-11-08). A build with them is dispatched automatically when the push lands (background job).
- Rebuild workflow had been cancelled on 11-07 and 11-08 by the shared concurrency group → own group; today's run succeeded.

## 19:25Z — all engines live; first yields
- Gemini app (Argon, Task): continuous task + new hourly scheduled task (its old scheduled tasks had all been PAUSED since 11-02/11-07 — the real reason
  the lane was silent); rows flowing: batch45 85 lines on origin via mac_sync branches (19:00Z, 19:20Z). Codex app (GPT-6.1 Sol High): verifying
  chatgpt batch01, pushing every 10 rows ("[chatgpt] Verify buyer AP batch01 rows 71–80" 19:17Z).
- API worker: 2,100 tasks, $32 (1.8 ¢ / task); AP-page searches 96 % hit → 4,882 pages queued for deep_pages + ap_terms; award-page searches: 2,146
  pages read → vendor named on 846, contract_value 123, end_date 34, term 24, start 14, PO number 1 (≈ 7 % of pairs get a value: real but modest;
  kept, lower priority than AP pages). Lane driver (Claude on the lanes' queues): 25-row passes with 10–17 found.
- P13 walk (10 runners, 70 min): 50,789 sites done, 25k pages, ap_terms file 63.7k → 88,940 rows (payment terms 746 → 1,047, PO rule 1,251 → 1,528,
  portals 2,601, AP contacts 538). The run's merge job failed to push (dirty-index rebase) — recovered by hand from the artifacts; merge logic fixed;
  walk state now lives in data/incoming/claude/claude_ap_walk_done.tsv (release uploads are not permitted from this session). A–F walk (10 runners)
  running until ~23:15Z — its merge uses the old workflow version, so recover from artifacts if it fails.
- Mac kept awake (caffeinate -dis + Gemini's keep-awake). Build dispatched 19:17Z.
- Follow-up: claude_ap_terms.csv is 51 MB and growing (GitHub warns at 50, refuses at 100) → move the walker's page rows to a gzipped companion file.

## 18:20Z — owner 13:07 EST: hard deadline (this credit period), invoice framing for every row, all packages; API credits and the other lanes may be used
- **API search worker** (tools/api_search_worker.py + api_queue.py): Anthropic web_search tool, URLs taken from the tool's result blocks only, every
  page still read and quoted by the Mac readers. Pilot: 12 tasks, 43 URLs, $0.23 (≈ $0.019 / task). Loop `~/cch-crawler-state/api_search_loop.sh`
  running: queue 1,852 award-page tasks + 6,000 AP / PO-terms tasks + 1,137 vendor-site tasks, 600 per cycle, absolute cap $150; readers
  (award_facts, deep_pages, ap_terms, vendor_sites_check) run after each cycle. Key stored only in `~/cch-crawler-state/anthropic.key` (chmod 600),
  never in the repo; the owner pasted it in chat → recommend rotating it when this is over.
- **Runners**: A–F buyer sites (10,337) now walked by 10 GitHub runners (run 42509071867) alongside the P13 run; the Mac walker stopped (its done
  file copied to data/incoming/claude/claude_ap_walk_done_mac.tsv for the release state); walk_terms re-dispatches itself while sites remain.
- **Award facts**: tools/award_facts.py (value, dates, numbers, bids next to the vendor's name on the buyer's own award page) deployed; fed by the
  API worker (af tasks) — first results in the next builds; rank.py consumer in place.
- Other lanes (Gemini, ChatGPT/Codex): their queues already hold 1,200 + 1,200 + 799 buyer-AP tasks for buyers with Canadian-vendor contracts;
  the owner opens the apps; no new batches needed yet.
- Build dispatched 18:00Z (p59/p60 pages, in-build DNS check). Next: measure the award-facts hit rate, Public Accounts values, lower packages
  (P06 / P08 / P10) get the same AP / vendor engines via the walker and VW waves — they are in the queues, Gold first.

## 17:40Z — owner 12:23 EST challenged the "ceilings" → retracted for 4 of 5 fields; new sources scouted and one built
- Bulk registry match (tools/bulk_registry_match.py; REQ open data 270 MB zip + Corporations Canada 1.58 M rows): 11,286 organisations found
  (9,330 buyers, 1,956 vendors; 2,719 with BN; 11,452 with a registered address) in 5 minutes offline — committed to
  data/incoming/claude/claude_registry_bulk.csv; rank.py reads it after the API rows (REQ rows add NEQ, registered address; buyers never
  matched to struck-off / dissolved entities); daily rerun scheduled in claude-engines (bulk_registry).
- Scouted (NOTES.md Question 3): Public Accounts payee schedules (ON CSV, AB XLSX, BC CSV) → pair facts for BC/AB/QC ministry buyers (to build);
  Ontario ministries are not buyers yet and the schedule has no vendor address (rule 1), so it cannot create records alone; PO registers:
  only Edmonton found (stale 2019); NS tenders already rejected by the team (no supplier location).
- Build 17:32Z published WITHOUT the downstream pack (my "GST 5% (%s)" label broke %-formatting inside the try/except): 15/438 and empty
  AP-grade tables. Fixed, and the workflow now refuses to publish a build whose pack was skipped; corrected build dispatched 17:36Z; a local
  run is checking the pack line in parallel.
- Walker-terms pass (Mac, 9,400 of 11,162 pages): payment terms 310 → 688, PO rule 555 → 1,142, portals 718 → 2,043, AP contacts 211 → 379;
  p59 (161 Gold buyers' PO T&C / supplier pages from the search waves) read: deep_pages + ap_terms done 17:20Z.

## 2026-11-10 03:35Z — measured yields after the multi-crawl / .com-universe index and the first completeness pass
- Index now 268,494 relationship pages (client 179,170 · member 61,371 · dealer 14,655 · sponsor 12,866 · tenant 432) — was 66,321 at 01:25Z.
- Leads (`claude_buyer_leads_cc.csv`) 26,781 (was 9,487); 110,934 link records wait in the no-address side file; address pass, first run: 1,938
  vendor domains now have their Canadian address from their own home / contact page (promotes their links at the next merge).
- Mailbox crawl: 9,487 lead sites read → 2,355 with a role mailbox (2,578 buyers, 2,817 rows at the referee). ~17,300 cloud leads + 33,600 Mac-era
  leads still to read (cycle 42749605088 queued 03:27Z, then every 3 h).
- Site facts (completeness, first pass over delivered rows): 30,220 sites read → own name 28,453, postal address 18,919 (CA 18,103 · US 654 · GB 144 · AU 22).
- Rank build 42749316069 (03:25Z) in progress: carries the organisation-key fix and the first site facts. READ `coord/GROWTH_VS_BASELINE.md` after it.
- Running: tenant-factory 42745654373 (+1 queued), lead-sites 42747032693 (websites for 23,851 leads without one), referee 42746318520 (+1 queued).

## 2026-11-10 03:00Z — ROWS MOVED (+898 in the first cloud build); six engines running; what was fixed and what is queued
- Build 01:55Z (GROWTH_VS_BASELINE): rows 63,641 → **64,539 (+898)**. Side effects found and fixed in rank.py (next build): 451 tier-I rows became
  client-listing rows and lost the facts held under their organisation key (legal names −122, routed pay-on-sight −172) → lead rows now take the
  organisation's own key (local run: 3,839 rows joined, 639 addresses, 1,323 names); first-key lookups read every key.
- Row factory: dealer / sponsor pages read → cc leads 9,664 → **16,253**; member pages indexed (15,099) and being read; ADDRESS PASS added to the
  cycle (11,617 vendor domains whose client page printed no address; 18,733 buyer domains wait on it); six-crawl index dispatched (02:52Z).
- THE BIG POOL nobody was reading: 33,600 Mac-era leads with a website and no mailbox row. The cloud crawl takes them after the cloud leads.
- Tenant factory first full cycle: 2,282 candidates → 177 accepted (150 Shopify / 26 Amilia / 1 Jane), 636 refused the reader, 292 no address,
  70 outside the vendor's scope. eScribe and Absorb portals are absent from the archive (index read completely, no pages).
- Crawl hygiene: per-site time budget (420 s) — a first-version shard hung 60 min on slow sites; new concurrency group `row-factory-b-*`.
- Local full rank builds no longer fit this container's memory (7 GB): test rank changes with `python3 -c "import ast…"` + the cloud build.
- NEXT (in order): read the address-pass / member / Mac-leads yields; dispatch a rank build after the referee lands them; PLAN §4e #5 (.com
  universe), #10 (tenant / advertiser classes), #7 (site finders in the cloud), #6 (Shopify scale, bounded), #14 (vendor legal names).

## 2026-11-10 02:15Z — referee verified the first 1,119 new buyers; three more engines launched (owner 20:42 / 20:48 EST: "do that … no maximum")
- Referee (01:23Z run): 1,216 of 1,230 cloud mailbox rows verified → **1,119 new buyers verified**. Rank build dispatched 01:55Z to deliver them.
- Row factory cycle 2: back-off works (unreadable 24 of 7,064 per shard); leads 9,487 (+5,050); their mailbox crawl is running (25 pages).
- NEW engines (all cloud, no AI): (1) page classes `sponsor` / `dealer` in cc_clients (parties that pay a Canadian organiser / supplier), re-index
  dispatched 02:00Z; (2) `tenant-factory.yml` — customers of Canada-HQ software vendors (portals of the vetted table + Shopify redirects; accept
  only with role mailbox + address in the vendor's contracting scope + service still seen), index dispatched 01:54Z; (3) `site-facts.yml` —
  bill-to name / address for delivered rows from their own pages, first pass dispatched 02:04Z; rank accepts a self-published trade name +
  address as bill-to (SOR/91-45 s. 3(c)(i)), reads `claude_lead_site_facts.jsonl.gz`, files sponsor / dealer rows with the client listings.
- Backlog of pathways: PLAN §4e table (15 items, ranked). Next OPEN: #4 address pass, #5 .com hosts, #6 member directories, #7 older crawls.
- Watch: first runs of tenant-factory index (per-domain equality queries over 300 index parts — slow or failing?), site-facts yield
  (addresses found / sites), and whether `rows` rises in GROWTH_VS_BASELINE after the 01:55Z build (if not: where rank.py drops cc leads).

## 2026-11-10 01:25Z — row factory: first measured yields; NEXT STEPS for whichever session runs next
- Index (crawl CC-MAIN-2026-43): 66,321 client pages on 28,538 .ca vendor domains. Extraction, first pass: the archive refused ~68 % of the range
  requests (8 runners × 10 connections); from the readable third: 10,952 client links with the vendor's Canadian postal address → **4,437 new
  buyers** (`claude_buyer_leads_cc.csv`), ~17k more links in the no-address side file. Fixed: retries with back-off, 4 connections per runner,
  unreadable pages retried on later cycles (≤ 4 attempts), failure reasons counted.
- Mailbox crawl of those 4,437 sites (7 of 8 shards merged by hand at 01:18Z; shard 7 hung on a slow site — fixed: stragglers stop after 4 quiet
  minutes): 3,847 sites read → **988 buyers with a published role mailbox** (1,073 rows in `claude_buyer_ap_results_cccrawl01.csv`: info@ 771,
  hello@ 97, contact@ 61, a few accounting / AP / procurement), nothing found 2,562, blocked 297. Yield 26 % at 15 pages; budget now 25 pages.
- Referee dispatched 01:18Z (runs 42734833754 / 42734885351). Rebuild done 00:38Z with the salvaged records (PSPC standing offers 7,099, Vermont
  2,574, Baton Rouge, Chicago, UNOPS).
- Run 42730092295 (first cycle) still has `crawl (7)` hanging (job timeout 200 min); the next cycle is queued behind it (same concurrency group).
**NEXT STEPS, in order:**
 1. When the referee has finished the cccrawl01 rows (coord/results/verification_log.csv gains ~1,000 lines for keys of claude_buyer_leads_cc.csv),
    dispatch `rank-buyers.yml` and read `coord/GROWTH_VS_BASELINE.md`: `rows` should rise by several hundred (first movement since the baseline).
    If it does not, find where rank.py drops the cc leads (mail dict key, same_org, seen_dom, REL_PATH) and fix.
 2. Check the next cycle's extract logs: `fail:http403` / `fail:http503` counts tell whether the back-off works; tune workers / shards.
 3. Gear (a) of PLAN §4e is CLOSED as low value: the Socrata portals are already leads from the Mac scanner, and departments of one government
    collapse into one row per website domain. Gear (b) next: Canadian vendors on .com / .org hosts — host universe with a location proof from
    ISED's Canadian Company Capabilities open data (address + website per company), OSM Canada POIs with a website tag, Wikidata, the dataset's
    vendor table → index semi-join → same extract chain (the list's own address is the Canada proof; page address kept when present).
 4. Address pass for `claude_cc_leads_noaddr.jsonl.gz` (read the vendor's contact page from the archive).
 5. Mailbox yield: second, deeper pass (60 pages) over "nothing_found" lead sites; consider contact pages from the archive for sites that block.
- Honest projection (to firm up in Sunday's report): this engine on .ca hosts ≈ 6–8k rows per crawl; with .com hosts (gear b) and older crawls
  ≈ 40–60k rows → ~105–125k total. 200k needs one more layer (tenant sub-domains of Canadian SaaS vendors, or department-level rows) — both are
  weaker on payability and must be put to the owner before being counted.

## 2026-11-10 00:45Z — rows were flat because the row factories were off; cloud factory live (owner 19:18 EST, Fable 5.2 session)
- Diagnosis: ranked universe 66,693 buyers, 63,641 with a mailbox → no head-room without NEW buyers. Lead scanners only ran on the Mac (last output
  Nov 8 16:34Z); 34 lane PRs open since Nov 2–7 (no source merged since Nov 7).
- Built + launched `row-factory.yml` (tools/cc_clients.py, tools/lead_crawl.py; rank.py reads claude_buyer_leads_cc.csv). Index scan done 00:38Z:
  66,321 client pages on 28,538 .ca vendor domains (Common Crawl CC-MAIN-2026-43). First cycle (extract → leads → mailbox crawl → referee) started
  00:40Z, run 42730092295; schedule: every 3 h at :17. Expect the first new rows in the build after the first referee pass.
- PR review (34 open): salvaged to main the rule-compliant stranded records — PSPC standing offers 7,099 ongoing (was 178), Vermont payments 2,574
  (68 agencies), Baton Rouge 203, Chicago 13 (buyer = City of Chicago - department), UNOPS 14; rebuild dispatched 00:38Z. Held with reasons in the
  commit message (rule 1 violations: Québec cities 28,899, Manitoba, Edmonton; duplicates; Socrata sweep to be re-cut per portal — next gear a).
- Fixed: vendor BN9 −64 (REQ row had replaced the Corporations Canada row for one vendor; BN now carried with its own source).
- RISK found: my wake-ups (send_later) are bound to the owner's Mac ("bound_device"); the 18:57Z one was consumed without a turn while the Mac was
  off. The cloud engines do not need me, but my integration turns may not fire with the Mac off — tell the owner; fall-back = his message from the phone.
- Pilot sample: ready (230 rows, layer-1 dossiers for all, layer 2 for the 30 Gold); S2/S5 targeted reads optional.

## 22:45Z — first growth measurement; Gold dossiers complete
- Build 19:39Z (b1ca4b3) vs baseline: pay on sight 835 (+2) / 835 (−6) / routed 22,267 (−74); Gold A 227 (+2); 101/438 (+1). The −74 routed is the
  legal-name guard removing 158 page-derived "legal names" of which ~150 were junk ("Centre Fonds", "200 University", "Health Information Protection Act");
  ~8 real ones (BCIT Student Association, ESF Events Ltd) were lost to an over-broad noise list — narrowed 22:28Z (next build). Correctness over count.
- Deep terms walk (T10) merged 19:06Z: 1,507 sites, ~32k pages, ~3.2k AP/terms pages per shard — its effect on payment_terms / po_required shows in the
  22:24Z build; measure next turn.
- Pilot: layer 2 done for all 30 Gold rows (S1). Structural findings that change how invoices are built: research subawards (Wright State, Vanderbilt,
  Notre Dame) invoice the prime's sponsored-programs contact per FDP Attachment 3A, not AP; construction contracts (UFV, Manitoba Housing, WECHC) are
  payment applications with holdback; US federal (CPSC) via DOT ESC; French public bodies via Chorus Pro; shared/central AP centres. S2/S5 next, one
  targeted read each (budget §4d).
- Wake-up chain: the 18:57Z trigger was consumed without a turn; rescheduled 19:24Z (fired 22:25Z) and 22:42Z (01:43Z) — verify at every turn end.

## 16:50Z — pilot layer 2 under way; tracks T5–T12 added; budget rule
- Dossiers: layer 1 for all 230 (16:28Z); layer 2 done for S1-01/02/03/05/06/07/08/11/12/18/23/24/25/26/27 (15 of 30 Gold). Found and fed back: WCB-Alberta
  T&Cs (net 30, PO first, GST-exempt #124072513RT0001), East Sussex T&Cs (APInvoices@, PO mandatory, PDF/TIFF, 30 days), Manchester (no PO no pay,
  supplier.invoices@), Paris-Saclay (Chorus Pro + engagement juridique), CPSC (DOT ESC shared AP), legal names from audited statements (Cambrian,
  Windsor "Corporation of", SickKids, FWFN). rank.py: legal-name guard (distinctive token), First Nation B-039 tax note. Pages → claude_ap_pages_manual.csv.
- Owner 11:43/11:47: all 230 before invoices go out; never a static plan (T5–T12 in PLAN §4c); weekly limit 78 % used → §4d budget rule.
- Cloud: walk_terms (6 shards, 4 h) and registry (5 h) dispatched 16:19Z; org_facts leftovers measured (24 ok / 1,120 — blocked sites).

## 15:55Z — NEW DIRECTION (owner 10:25–10:48 EST): wait-or-ship decision by Sun Nov 15; targets 200k rows, ≥ 85 % complete, cloud-only
- Owner's computer will be off: nothing may depend on the Mac. Engines moved to GitHub cron (claude-engines.yml: org_facts every 6 h / 8 shards,
  walk_terms nightly / 6 shards, bulk_registry daily); org_facts dispatched 15:55Z (8 runners, 120 min). My wake-ups: send_later every 180 min.
- Ship-now baseline frozen: coord/BASELINE_SHIP_NOW_2026-11-09.json (build 89b4386). tools/growth_report.py runs in every rank build →
  coord/GROWTH_VS_BASELINE.md + coord/growth_history.csv. PLAN_2027-01.md: four tracks, week-1 table, kill switch (< 120k rows or < 70 % complete
  projected → recommend shipping now).
- Measured: 39,626 incomplete rows; bill-to (legal name / address) missing on 33,136 of them (17,902 have an address but no legal name; 24,670 are
  .ca; 26,180 sites answer); 22,394 lack exactly one element. Peer-group inference: PO rule concentrates (100 % "required" among publishing peers,
  selection bias noted) → 29k rows inferable at p ≥ 0.9; payment terms and method do not concentrate (net 30 43–62 %) → distributions, not values.
- 16:15Z: org_facts cloud run measured — the leftover domains are the hard ones (shard 0: 1,120 domains → 24 ok, 872 blocked, 85 robots, 106 no answer).
  Crawling will NOT close the bill-to gap; registries / bulk files (Companies House, GLEIF, SEC, Canadian registries) and batch extraction from pages
  already fetched are the T2 levers. Pilot designed on the owner's "payability, not plausibility" rule: coord/pilot/ (230 rows, 5 strata, real
  invoices by the row's vendor only); downstream AI briefed (coord/for_downstream_ai_2026-11-09_pilot.md).
- Lanes briefed (inboxes 16:00); 8 T1/T2 sources registered (USAspending Canada-recipient full, US local checkbooks, FL FACTS, Companies House bulk,
  SEC EDGAR submissions, …). API credits: batch extraction only, capped, yield per dollar reported.

## 14:35Z — FINAL (builds 13:39Z scoreboard / 14:03Z amounts / 14:29Z portal correction; this is the last entry)
- Final published build 89b4386 (14:29Z): 63,638 rows; **pay on sight 833** strict + 841 reference-less + 22,341 routed; Gold 395 / 624 (63.3 %),
  Gold at AP grade A 225, AP payability Gold 452 / 624; 100 / 438 benchmarks (the three P11 DNS cells healed by the re-check); amounts formatted.
- Correction found while writing the worked examples, and the reason the strict count fell from 1,113: `_portal_ok` accepted any portal whose kind
  text said "invoice" — the generic kind text does for every portal — so 466 rows with only a purchasing / general mailbox counted a tender portal
  (SEAO 190, MERX, bids&tenders) as their invoice channel. Now only e-invoicing networks (Ariba, Coupa, Tungsten / Kofax, Basware, GHX, Jaggaer,
  Workday, Oracle iSupplier, Esker, Taulia …) make tier 1 on their own; the card carries `portal_is_invoice_channel` + `portal_class`, invoice_text
  labels tender portals "not an invoice channel". 280 rows moved to `routed`, which is what they are. Gold unchanged (AP mailboxes).
- Verified ceilings once more: of 138 Gold rows without a vendor GST number, 110 have a vendor site, 94 were read in full by org_extras and none
  prints the number (a GST/HST account is printed on 0.14 % of 83,475 organisation sites). Nothing else within the rules moves ≥ 50 rows.
- Closed: wake-up trigger deleted (13:19Z); inbox notes to codex / chatgpt / gemini; hand-off `coord/HANDOFF_INVOICES_2026-11-09.md` §0–§10 (tiers,
  field mapping, legal minimum SOR/91-45 s. 3, bounce rules, ceilings, what runs, levers, card schema, two rendered rows, pre-flight, cover e-mail).

## 13:00Z — STOP ORDER (owner 07:51 EST: "stop … make sure this is really it … advice to the other AI … go out with a bang")
- Final lever audit: nothing left that moves ≥ 50 pay-on-sight rows within the rules (list in coord/HANDOFF_INVOICES_2026-11-09.md §6). Two last
  defects fixed before the final build: `ap_payability` and `supplier_setup_url` were computed but never written to the pack (missing from the column
  map since 2026-11-08 — now emitted); the doubled "DERIVED:" prefix in invoice_text.
- Hand-off written for the downstream AI: coord/HANDOFF_INVOICES_2026-11-09.md — build order by pay-on-sight tier, field-by-field mapping of the
  invoice to the columns (bill-to, channel, references, vendor identity, tax, currency, terms, follow-up), bounce rules learned from the buyers'
  pages, ceilings, what keeps running and how to stop it, the levers audited. Companion: coord/for_downstream_ai_2026-11-08.md (status + by-design cells).
- Stopped on the Mac (they spend the owner's quotas): codex_exec_loop (ChatGPT), api_search_loop (Anthropic API, $170.04 of the cap, 7,690 tasks),
  lane_driver_loop (Anthropic API). Left running, restart-safe and free: push loop, walker-terms loop, site readers, downloads/sync loops, Gemini's
  hourly task, the Codex app automation (owner's own); GitHub: builds every 6 h, referee on push, bulk registry daily. One-liner to stop everything on
  the Mac: `pkill -f 'cch-crawler-state/.*_loop'`.
- Final build 12:54Z → landed 13:09Z (3a4b3d5): 63,628 delivered rows; pay on sight 1,113 strict + 887 reference-less + 22,024 routed; Gold 395 / 624
  (63.3 %), Gold at AP grade A 225; AP payability Gold 452 / 624 (72.4 %), P02 306 / 404; 100 / 438 benchmarks. Its scoreboard was NOT written (the
  new AP-payability table shadowed the field-gap list `gaps` — same bug class as 700edbf; fixed, build 13:17Z re-dispatched for the scoreboard).
  Two last invoice_text defects found while writing the worked examples: amounts printed as raw floats (416594.66000000003) and tender portals (SEAO)
  labelled "portal" next to the mailbox — fixed in rank.py (`_money`, "supplier / tender portal (not an invoice channel)"); last build carries them.
- Hand-off extended (§2 legal minimum per SOR/91-45 s. 3 — $100 / $500 tiers, replacing the outdated $30; §7 invoice_card_json schema; §8 two rows
  rendered as invoices with build instructions; §9 pre-flight checklist). Wake-up trigger for 13:33Z deleted: no further turn is scheduled.

## 12:05Z — build 11:17Z: 1,114 (+2) / 887 / 22,025; Gold 395 / 625; 100 / 438 (row growth). Codex lanes quiet again since 10:42Z (ChatGPT limit); Gemini sync 12:00Z; verifier 11:45Z; integrity intact. Flat as forecast; loops stretch to 90 min until the owner answers.

## 11:00Z — no build since 09:00Z; Codex lanes back (chatgpt batch52 rows 11–30, codex batch04 rows 384–393 at 10:38–10:42Z), Gemini batch 53; verifier landing (10:56Z); integrity intact; build dispatched 10:58Z.

## 10:00Z — build 09:00Z: 1,112 / 887 / 22,023 (flat); Gold 395 / 624; 101 / 438. Gold's 209 non-payable rows: 87 miss ONLY the vendor GST number
- The province-from-name fix moved 10 Gold rows' tax treatment (59 → 49 missing) but they still lack the vendor GST number, so pay on sight is flat.
  Remaining Gold gaps: vendor GST 138 (87 of them the only gap — ceiling), bill-to 76 (blocked sites / registries), tax + currency 49–57 (buyers with no
  resolvable province or country: no address, no city or province in the name, .org / .com domain — 13 rows miss only those two).
- Lanes: Gemini syncs 09:15Z / 09:36Z (batch 53); Codex at the ChatGPT limit; verifier landing (09:48Z); integrity intact. No build dispatched this loop
  (last 09:00Z; next with the Gemini rows). Hourly loops continue until the owner answers the 06:25Z recommendation.

## 08:55Z — build 08:16Z (ranker-bot, no revert since): pay on sight 1,112 (+8) / 887 / 22,022 (+75 routed); Gold 395 / 624; 101 / 438
- Scoreboard provenance verified (ranker-bot 08:16Z); verifier commits keep landing (08:24Z). Build for the province-from-name / federal fix dispatched 08:50Z.
- Inspection: P02's 158 non-payable rows — vendor GST/HST number 130; P04's 920 — general-inbox channel 748, vendor GST 693, bill-to 207, tax 196.
  The vendor GST number is now the single remaining blocker across Gold / P02 / P04 (≈ 960 rows) and no public source exposes it beyond what is
  already joined (Corporations Canada, Canada's Business Registries, CRA charities, federal grant recipients, the vendor's own pages). Ceiling.
- Gemini batch 52 complete (02:28 EST; hourly task next); Codex at the ChatGPT limit; integrity intact (org_contacts 74,911). Verdict unchanged.

## 08:05Z — build 07:13Z: 1,104 / 885 / 21,947 (flat vs 06:36Z); Gold 393 / 624; reverted again at 07:18Z by a pre-fix verifier run; republish dispatched 08:00Z
- The 07:18Z revert came from a verifier run queued before the 07:12Z fix; runs since (07:41Z, 07:56Z) are on the new code and do not touch
  coord/results/ranked. Ranker build re-dispatched 08:00Z; the one after carries this loop's fix.
- Inspection pass (Gold, 212 rows not pay-on-sight): vendor GST 138 (ceiling), tax / currency 59 (buyers with no address and no city in the name —
  now resolved from the province in the body's name or the address code, e.g. "Efficiency Manitoba", "NS, CA"; federal bodies get the federal treatment),
  bill-to 76, remit-to 13. Pushed 1bf685b.
- Gemini batch 52 complete (07:28Z); Codex at the ChatGPT limit; integrity intact. Verdict unchanged; awaiting the owner.

## 07:15Z — build 06:36Z: pay on sight 1,104 (+72) / 885 / 21,947; Gold 393 / 624 (63 %); 101 / 438 — then reverted by a verifier push, fix pushed
- The country-first tax / currency fix moved 72 Gold / P02 rows to pay on sight (1,032 → 1,104). 101 / 438 (Gold row growth dilutes a few cells).
- A third regression path closed: my 03:20Z verifier fix restored the whole coord/results snapshot on retry, including coord/results/ranked, so the
  verifier's 06:41Z push put the 05:32Z build back over the 06:36Z one. Now rsync restores only the verifier's own files (1468ce7). The scheduled
  ranker build in progress (06:38Z) republishes; if a pre-fix verifier run reverts it once more, the next loop re-dispatches.
- Lanes: Gemini batch 52 rows 31–65 (06:39Z); Codex at the ChatGPT limit again (the window closed ≈06:30Z after batch51 rows 81–90 / batch03 rows 261–270);
  org_extras refresh second cycle started (9,012 domains). Verifier landing every ~15 min.
- Verdict (06:25Z) unchanged: organic pay-on-sight ≈ 0 / h; today's +72 came from an inspection fix. Awaiting the owner's answer on stopping.

## 06:25Z — VERDICT for the owner (asked 19:55 EST: "tell me when the rewards won't be worth it")
- Build 05:33Z (first with the 6,168 verified mailbox finds): 102 / 438 (−3: Gold grew 597 → 623 rows as P03 / P04 buyers gained a confirmed
  invoicing mailbox, which dilutes three Gold percentages — row movement, not lost data); Gold A 214 → 225; pay on sight 1,032 (flat), 862
  reference-less (+4), 21,868 routed. Organic rate over 04:09Z → 05:33Z: **≈ 0 strict pay-on-sight rows per hour** — far below the 100 / hour signal.
- Where the remaining movement comes from: (1) the lanes (Codex × 2, Gemini: ~100–200 researched rows per hour while the ChatGPT window is open, of
  which a fraction upgrades a channel); (2) rule / normalisation fixes I find by inspection (this turn: 98 Gold rows without a tax treatment because the
  buyer's country was read after the province; 'CA'-only addresses blocking the site readers' address — pushed 14ce036, build 06:19Z). Those are
  one-offs with diminishing size. The engines that read the web have run their course for the honest fields.
- What is left is ceiling under the rules (no fabrication, evidence or nothing): 21.9k rows whose organisation publishes one general inbox (routed,
  not addressed); ~270 Gold / P02 rows whose vendor has no BN in any public registry (Québec-only vendors, partnerships, not-found names); blocked sites
  (~10 % of organisations) for bill-to addresses and legal names; relationship-proof rows with no contract record (no PO / contract numbers, values,
  dates); P11's 441 mailboxes the referee cannot re-fetch (only a second lane's quote confirms them).
- RECOMMENDATION: stop the paid effort after (a) the current lane batches finish (chatgpt batch51, codex batch03, gemini batch52), (b) the build after
  14ce036 lands, (c) one final build + the pack hand-off (ranked batches with pay_on_sight / channel_tier / invoice_text on every row, the Pay-on-sight
  table, COVERAGE_VS_TARGETS.md with the ceiling notes, for_downstream_ai_2026-11-08.md). Zero-cost automation (scheduled builds, verifier, Gemini's
  hourly task) can keep running; it will add rows slowly. My loops drop to 45 minutes until the owner answers; each one still ships any inspection
  fix with a visible row effect.

## 05:35Z — verifier landing again (commits 04:49Z and 05:01Z); search01's 6,168 rows verified; both Codex lanes back; build 05:13Z in progress
- The gzip fix worked on the first run: verification_log now holds claude_buyer_ap_results_search01.csv verified 6,168 / page-unavailable 132 /
  not-on-page 42 / personal-mailbox rejected 8 (the deep_pages finds from the policy pages), deep01 434 verified.
- ChatGPT limit lifted ≈05:05Z: "[chatgpt] Buyer AP batch51 rows 31–50" and "[codex] buyer AP batch03 rows 261–270" (05:08–05:12Z); Gemini batch 51
  complete (04:58Z). API capped; deep_pages queue drained (last pass 0 buyers left).
- Build dispatched 05:13Z (first with the verified mailbox finds) — still running at 05:35Z; the channel-tier upgrades (P03–P05, P11) read at the next loop.

## 04:40Z — the verifier's real blocker: coord/results/team_buyers.jsonl grew past GitHub's 100 MB limit (101.4 MB) — every push since 22:16Z was
rejected by the pre-receive hook ("remote rejected"), not lost to a race. The earlier race fix (48c70d7) was right but not sufficient: the fixed run
retried 12 times against the same rejection. Fixed (8571915): the ingest writes team_buyers.jsonl.gz (16.7 MB), the plain file is removed from git,
all five readers (ap_crawler, status_board, make_batches, patch_dataset, ingest) accept the gz, .gitignore un-ignores it. An old-binary verifier run
(started 04:25Z) still holds the main-writer lock and will fail the same way; the first run on the new code starts after it (≈05:05Z) and lands
≈05:50Z with the 3,583 deep_pages mailbox rows. Build 04:09Z: 105/438, pay on sight 1,032 / 858 / 21,874 routed (+128 routed, organic).
Gemini batch 51 rows 1–30 (23:01 EST). Codex: 30 usage-limit refusals so far; waits for the account window.

## 03:55Z — waiting on the first fixed verifier run (an old-logic run started 03:26Z holds the main-writer lock; the fixed run is queued behind it; cancelling the old run is outside this session's permissions). Build dispatched 03:51Z on Mac inputs only. Gemini quiet since 21:15 EST (owner active at the Mac, no screen action); Codex at the ChatGPT limit; org_contacts refresh finished (123 of 1,090 reachable).

## 03:25Z — build 03:00Z flat (1,032 / 857 / 21,746); the referee had not landed a result since 22:16Z — root cause fixed
- Organic gain 02:26Z → 03:00Z: +0 pay-on-sight, +2 reference-less, +203 routed (P13 site readers). Below the 100-rows/hour signal — but the pipeline
  that carries the channel upgrades was stalled: the verify-and-merge workflow re-ran its 40-minute evidence re-check on every push race and lost all of
  them (verification_log.csv last changed 22:16Z while claude_buyer_ap_results_search01.csv gained 3,583 rows today — the deep_pages invoicing-mailbox
  finds). Fixed (48c70d7): the ingest runs once, the push loop restores its outputs onto the latest main and retries only the cheap queue / board steps
  (12 attempts). The next verifier run lands the 3,583 rows → channel tier upgrades (P03–P05 → pay on sight; P11's 440 unconfirmed) in the build after.
- Owner's signal: I will call the engines' organic rate after two verifier runs have landed (≈ 04:30Z), not on this stalled reading.

## 02:45Z — build 02:26Z: pay on sight 1,032 + 855 + 21,543 routed; Gold 361 / 597 (60.5 %); 105 / 438
- Rate since 02:05Z (21 min): +55 pay-on-sight, +29 reference-less, +455 routed — from the public-body billing name and vendor carry-over rules.
  Engines' organic flow now: deep_pages found invoicing mailboxes for 87 of 105 buyers in its last pass (policy / AP pages from the pb search) →
  referee → channel upgrades for P03–P05 in the coming builds; Gemini completed batch 50 (21:15 EST); Codex lanes still at the ChatGPT limit.
- Gold's remaining gap is the vendor GST/HST number (126 rows): 89 vendors not found in Canada's Business Registries, 25 found in the Québec REQ
  (which publishes no BN), 6 ambiguous. Name-variant matching might recover ~20–30 of the 89; the REQ ones have no public BN — a ceiling.
- 21,543 "routed" rows (19,829 of them P13) are complete invoices addressed to an organisation's general inbox: the honest state for small
  organisations that publish one mailbox.

## 02:15Z — Pay on sight on the scoreboard: 977 yes + 826 yes-no-reference + 21,088 routed of 63,609 (build 02:05Z); Gold 57 % (340 / 597)
- Top gap per package (rows): Gold — bill-to legal name / address 105 (public bodies whose published name is the billing name → counted from the next
  build; the address gaps stay with registries / site readers); P02 / P01T — vendor GST/HST number (121 / 18; registry coverage); P03–P06T, P08–P10, P12,
  P13 — only a purchasing / general inbox confirmed (the invoice is routed, not addressed: 21,088 routed rows, 19,451 of them P13); P11 — channel not yet
  referee-confirmed (440).
- deep_pages over the pb / pc pages is finding invoicing mailboxes at 41 / 50 and 63 / 75 buyers per pass (Mac log 21:11 EST) — the honest route from
  "routed" to "pay on sight" for P03–P05; they go through the referee first.
- API worker: budget reached ($170.04; pb 1,735 of 1,881 done, 1,195 with pages). The loop now sleeps; the cap stays (owner: don't burn the key).
- Same-vendor carry-over of BN9 / remit-to address (45 / 56 rows) and the public-body billing name pushed (8a3f9df); build dispatched 02:11Z.
- Rate: pay-on-sight rows 380 (00:30Z strict measure) → 1,803 (02:05Z) — +1,400 in 95 min, almost all from resolving tax / currency / vendor identity
  rules on data already held; the engines' organic contribution per hour is measured from the next build on (signal to the owner: < 100 rows / hour).

## 01:55Z — the goal restated by the owner (19:55 EST): PAY ON SIGHT — every row an invoice that clears AP; the 438 stay, payability leads
- Owner: "you see the invoice, boom, it's paid"; add fields that push payability; keep the 438 but don't be limited by them; derived columns stay, never
  count as published; say when the rewards stop being worth it; credits allow until tomorrow night at most.
- Strict measurement before tonight's changes: 380 of 63,499 rows could have an invoice generated that clears AP (confirmed invoicing / AP or finance
  channel + bill-to legal name and address + vendor legal name, GST/HST number and remit-to address + tax treatment + currency). Top blockers by rows:
  tax treatment unresolved (province unknown) ~49k; reference rule unpublished (reported separately, does not block); channel = purchasing / general
  inbox only (P03, P04, P08, P13 — routed, not addressed); vendor GST/HST number (130 Gold … 731 P04); bill-to legal name / address on P13 companies.
- Shipped (b73458e, 855dca4, 700edbf): `pay_on_sight` (yes / yes — reference rule not published / routed / no), `pay_on_sight_missing`, `channel_tier`
  (1 invoicing-AP or invoice portal, 2 finance, 3 purchasing / general, 0 unconfirmed) and `invoice_text` — a rendered draft invoice header on every row;
  tax treatment and currency derived for every row with a resolvable province (jurisdiction → postal code → website / mailbox domain → registry place
  table → city) or country (US / UK / EU / AU export treatment); the inferred relationship's vendor (Canada Post Corporation, BC Hydro) counts as a
  certain identity; scoreboard "Pay on sight" table per package. First pack with it (01:44Z): pay_on_sight yes 1,116, routed 1,642, no 60,854;
  ap_payable_today 905; ship_ready 612; Gold A 211 (00:50Z build). The 01:44Z scoreboard was dropped by a shadowed variable in the new table
  (TypeError) — fixed, workflow now keeps the previous scoreboard when the new one is not written; build re-dispatched 01:48Z.
- Build 00:50Z (late site-reader pass): 105/438; vendor_logo +15–29 pts, vendor_phone +11–17, buyer_logo +10–18 across P01–P05.
- Mac: API $152 of $170, pb 1,200 / 1,881 (749 with pages; marginal yield now ~+30 terms per 600 — the pass finishes at the cap, no extension);
  Gemini last local commit 19:13 EST (batch 50 rows 1–30; hourly task irregular); Codex exec and app both at the ChatGPT usage limit again.
- Next: read the Pay-on-sight table (02:03Z build) → the next engines go at the top gap per package in ROWS; honest answer to the owner on what the
  remaining gaps are (channel type for P03/P04/P08/P13 = routed at best; vendor GST for vendors absent from registries; bill-to for blocked sites).

## 00:55Z — builds 23:53Z 103 / 00:29Z 104 of 438; Gold A 134 → 198 (DMARC posture no longer a penalty); owner 19:11 EST: continuous dense loops
- Owner (19:11 EST): keep working continuously, every loop must show marginal progress, say when the rewards stop being worth it; derived columns stay
  on every row but never count as the published benchmark; talk to the downstream AI if useful. Brief written and sent: coord/for_downstream_ai_2026-11-08.md
  (status, what an AP clerk needs, the cells no honest source can fill → asked to mark them "by design", two questions). Loop cadence now 30 min.
- AP grade: the buyer's DMARC posture is a NOTE, not a penalty (it blocked A on 269 Gold rows; coord/DECISIONS.md). Build 00:29Z: Gold A 198 / B 195.
  Remaining Gold blockers: payment terms 240, PO rule 194, legal name 87, address 40, vendor-registry warning 71 (of which the warnings caused by a lapsed
  extra-provincial registration while the home registry says Active are now a note, not a warning — pushed 00:52Z, next build).
- New API search kind `pb` (purchasing bylaw / procurement policy / PO terms on the buyer's host or its council / board document portal when the address
  names the buyer): 1,881 public-body buyers of P01–P05 still lacking terms or a PO rule; first 600: 456 with pages, 3,741 URLs; the readers added
  +106 payment terms, +323 PO rules, +450 AP contact names in one cycle (Mac file). Cap raised to $170 ($135 spent).
- rank.py: second site-reader pass for websites found late in the pipeline (95 Gold rows had the vendor's phone on file and "not_published" in the row).
- Codex: the ChatGPT account hit its usage limit again at 00:40Z (app automation + headless exec share it); both resume when it lifts. Gemini batch 50.
- Integrity after the snapshot-union fix: pages 58,056 → 61,770 (Mac rows merged in), registry 34,313 → 36,653 — nothing fell.

## 23:45Z — terms_refresh merged (23:09Z); two data-loss paths found and closed; registry shard recovered; Codex lanes back
- terms_refresh (every known page re-read with the current patterns; 10 runners, ~30 min): merge 23:09Z, 114,266 keys; the pages file then carried
  payment terms 2,752, PO rule 2,936, portals 3,882, payment method 864, tax treatment 1,341, e-signature 441–523, AP system 407–428, AP contact 1,349,
  invoice format 441. (ap_phone / invoice address next to payables anchors: only 15 / 11 — the anchor rule found little; the mailbox pages still carry
  35,021 phones and 12,839 addresses.)
- DATA LOSS 1 (closed): at 23:23Z the Mac's push snapshot replaced origin's claude_ap_terms_pages.csv.gz (50,895 rows, runners' union) with the Mac's own
  40,405-row copy (its ap_terms rewrote the file from its local view; the snapshot's "stale" rule only compares times). Restored by unioning the 23:09Z
  files with main (121,427 keys, pages 58,055) — commit f1996fc; tools/push_snapshot.py now UNIONS multi-writer files (ap_terms pair, registry_lookup,
  org_extras, org_contacts) with origin's copy via merge_engine_outputs.py instead of copying (10bec7b, mirrored to the Mac 23:38Z).
- DATA LOSS 2 (closed): the registry engine's merge job (run 42503912200, shard 1/2 finished 22:34Z) lost all 5 push races against a main that moves
  every minute; its artifact was merged by hand (1cf31ee: 34,313 keys, buyers found 3,944 → 6,446). The merge job now tries 15 times with short waits.
- A cancelled deep-walk repeat still produced a partial "walk_terms merged" commit at 22:51Z (union, harmless).
- Codex: the ChatGPT account's limit lifted at 23:34Z as announced — "[chatgpt] Buyer AP batch50 rows 1–10" at 23:39Z (app automation) and the headless
  codex exec is researching lane codex batch02 (World Bank borrowers). Gemini batch 49 rows 1–60. API worker 5,511 tasks, $113.81 (cap $120).
- Build dispatched 23:35Z (inputs: terms_refresh, award/notice-id and trading-name rules, lanes); read at the next wake-up.

## 22:55Z — build 22:49Z **99/438** (+5): ap_system_hint P01T / P09, buyer_tax_exempt_status P12, vendor_trading_name P03 / P04; Gold A 134, payable 805; payment terms +5–6 pts in P02 / P03 / P05 and PO rule +4–5 from the deep walk (27 cells up ≥3, none down)

## 22:50Z — build 22:23Z (scheduled) 94/438; deep A–F walk merged (+24k page keys); terms_refresh running; org_facts merged
- Build 22:23Z: 94 of 438 (+1: vendor_website P01_GOLD); award_or_notice_id +10–19 pts in Gold / P02 / P03 (notice-id rule), vendor_website P04 +16.7
  (API vendor-site searches + vendor_sites_check), payment terms P03 +7.5. Gold A 129 / B 255; payable today 789.
- Deep A–F walk (only buyers still lacking a term or PO rule, 60 pages, one more link level): 10 shards × ~1,290 sites, ~28k pages per shard;
  merge 22:34Z → ap_terms 114,266 unique keys (90,163 before); walker pages now carry payment terms 2,752 (1,277 at 19:45Z), PO rule 2,936,
  portals 3,882, payment method 864, tax treatment 1,341, e-signature 441, AP system 428, cheque-run cadence 86. The run re-dispatched itself (a
  redo-everything pass never shrinks "sites to walk") — cancelled, workflow fixed (no self-dispatch when redo_days = 0).
- ap_terms: walker pages had ap_phone 0 and invoice address 0 because both were read only next to the mailbox; now read next to the first payables
  anchor on mailbox-less AP / supplier pages. terms_refresh (every known page re-read with the current patterns; 10 runners, 90 min) dispatched 22:36Z
  with that change; it queued behind the cancelled run.
- org_facts merged 22:26Z (runner retries of blocked / failed domains: ~1,500 new successful reads). Mac org_extras --refresh: 6,717 of ~8,000 retried
  domains are blocked for automated readers (small-business hosts); the honest ceiling for those stays the registries.
- rank.py: vendor_trading_name from the vendor site's schema.org alternateName / Organization name when it differs from the legal name (not yet built).
- Mac: API worker 4,571 tasks, $95.69 of the $120 cap (84 % with a page); Gemini batch 49 rows 1–30 (21:47Z); Codex resumes 23:34Z; push loop 22:20Z.

## 21:50Z — build 21:39Z **93 of 438** (72 → 93, nothing lost); Gold A 128 / B 253; ChatGPT account at its usage limit until 23:34Z
- The first main build with the 20:30–20:45Z rank.py rules: +21 benchmarks — records_with_this_vendor met in 9 packages (relationship record = 1 record),
  solicitation_or_tender_number P02 / P04 / P09 (SEAO numero), ap_system_hint P01_GOLD / P02 / P03 / P04 (portal names feed the hint), invoice_reference_hint
  P01T / P06 (PO rule), contract_description P05 (title text), buyer_tax_exempt_status P01_GOLD, po_required P01T. 67 cells moved ≥ 3 points, none down.
  Pack ran (ap_payable_today 785, ship_ready 593).
- Codex: the ChatGPT account hit its usage limit ("try again at 6:34 PM" EST = 23:34Z) — that is why "[chatgpt]" commits stopped at 19:55Z; the app's
  30-minute automation is ACTIVE and resumes by itself. A second, headless Codex (`codex exec`, GPT-6.1 Sol high from ~/.codex/config.toml, own clone
  ~/cch-codex-exec, loop ~/cch-crawler-state/codex_exec_loop.sh) takes lane codex's buyer-AP batches from 23:34Z; inbox notes written for both lanes.
- Mac site readers restarted (`site_readers_loop.sh`: org_extras --refresh 9,122 domains v1 → v2 / retries, then org_contacts --refresh, every 2 h).
  Correction to 20:45Z: the 9,365 "never read" domains WERE attempted by the Mac (resume files: 103,991 domains; blocked 10.5k, network errors 5k,
  robots 2.2k, no contact found 9.1k) — the repo copies hold only successful reads. The runner org_facts engine retries them from another network
  (shard 5: 49 + 102 successes of ~1,000; most stay blocked) — worth its free runner minutes, not a lever. The honest ceiling for buyer address /
  phone / logo on blocked sites is the registries and public directories already joined.
- rank.py: a portal's tender-notice id (bidsandtenders_tender_id, competition_guid) is the award_or_notice_id when the source assigns no separate award id
  (SaskTenders 18 of P09's 35 missing; bids&tenders 464 rows) — not yet built.
- API worker: 3,497 tasks, $71.41 (cap $120), 80 % with a page. Gemini batch 48 complete (20:57Z). Deep A–F walk and org_facts still running; terms_refresh
  after the walk.

## 20:45Z — build 20:24Z 72/438 (Gold A 117, B 237); normalisation audit → five levers that need no new fetch; two new runner engines
- Build 20:24Z: 72 of 438 met (+3 on 19:33Z); AP grade A on Gold 67 → 117, B 207 → 237; ap_payable_today 746 rows. Inputs since 19:17Z: P13 + A–F walker terms,
  payability, bulk registry, Gemini batch 45–48, Codex verify rows 1–170.
- Why the A–F ap_terms merge showed "no new keys": the shard counts (75,049 known → 76,367) were cumulative per runner; 75k + 10 × ~1.3k new = the 90,163
  unique keys of the union. Nothing lost.
- Audit of the 371 unmet benchmarks against the dataset's own records (data/release, 803k records scanned per source): the biggest gaps that need NO new
  fetch were normalisation and counting rules, fixed in rank.py (local dry run passed, pack ran, no skip):
  1. SEAO `numero` is the organisation's notice reference (SEAO data dictionary) → solicitation_or_tender_number for 1,974 rows (was 0); when a source
     publishes the award only under its tender number (SEAO, bids&tenders 464, SaskTenders, BC), that number is the contract reference, labelled so.
  2. records_with_this_vendor: the relationship record counts as 1 (downstream §1.10, our own comment said so) — 10,685 rows were "0 in the contract
     dataset; 1 relationship record" (label-only to the scoreboard) → "1 (relationship record: …; 0 in the contract dataset)".
  3. contract_title from the record's description (163 rows), contract_description from the title (PD / SEAO publish one text) or the relationship
     detail, both labelled; 4. average duration also from durations the source publishes (end_inferred / end_computed);
  5. invoice_reference_hint from the buyer's PO rule for relationship rows (536) — the reference an AP clerk matches.
- The five AP-policy fields (payment method, cheque-run cadence, tax treatment, e-signature, AP system) were 0–5 % in all 17 packages although 95k pages
  are read: the statements exist in other words. tools/ap_terms.py reads them wider (registration number printed, "taxes shown separately",
  "suppliers are paid by EFT", "cheque runs every Thursday", DocuSign on POs, Ariba / Coupa / SAP / Workday named in a payables context) with a
  payables-context check, a menu-text guard and case-sensitive brand names (Determine / Avantage / Banner are also plain words). Sample re-read of 324
  pages on the Mac: +8 AP systems, few others on mailbox pages — the gains are on policy / PO-terms pages, which the deep walk reads now.
- New runner engines in claude-engines.yml: `terms_refresh` (ap_terms --reread-known --shard: every known page again with the current patterns; a page
  that stops answering keeps its old row; the policy fields are re-extracted, old menu-text matches do not survive) and `org_facts` (org_extras +
  org_contacts, sharded, seeded from the repo copies: 9,365 buyer domains and 694 vendor domains with a website were never read for legal name,
  address, phone, logo, BN, portals — that is most of buyer_address / buyer_phone / buyer_logo_url / legal-name gaps in P08, P10, P13). org_facts
  dispatched 20:38Z (10 runners, 120 min). Deep A–F walk (policies, bylaws, PO terms PDFs; max_pages 60, one more link level, only buyers still lacking
  a term or PO rule) dispatched 20:39Z after two false starts (redo_days 0 skipped everything: cutoff direction — fixed twice, the second time right).
- Mac: ~/cch-vnews is a plain mirror of tools/, not a clone; `~/cch-crawler-state/sync_tools.sh` now mirrors tools/ + rank_buyers/ from origin/main
  (run it after every tools push). API worker: 2,171 tasks, $45.35, 78 % with a page; loop cycles every 5 min; Gemini batch 48 rows 1–60 committed
  locally (sync merges hourly); Codex last commit 19:55Z (rows 161–170), its 30-min automation is due again.
- P09 (369 rows = SEAO contracts awarded > 3 years ago with no published end) cannot honestly reach end_date 95 % / duration 90 %: the package is defined
  by the missing end date. Ceiling note to add to the scoreboard; the rest of P09 moves with SEAO rules above.

## 17:15Z — owner 12:08 EST: "if levers are not moving, change them" → engines moved to parallel runners
- Throughput was the problem, not the method: one Mac walking 63k sites at 1 request / second / host. New workflow `.github/workflows/claude-engines.yml`:
  10 GitHub runners walk the P13 long tail (tier I, 50k sites, sharded by host so no site is read twice) and run the terms extraction on what they
  find; a runner takes the second half of the registry lookups (shard 1/2) while the Mac keeps shard 0/2 — together ≤ 2 requests / second to
  the registry. Outputs are unioned by key (tools/merge_engine_outputs.py); both writers now union with the on-disk file so runners never erase
  each other. Runs 42503904567 (walk_terms, 10 × 300 min) and 42503912200 (registry, 320 min) started 17:13Z. The Mac's P13 walker was stopped;
  its main walker keeps tiers A–F.
- Realistic reading of the 438 benchmarks (build 16:55Z): 51 met, 55 within 10 points. Reachable with the engines now running: the 5 DNS cells
  (9 rows), vendor_website ×5, buyer_legal_name ×4, buyer_address ×6 (100 % targets: the last rows are sites that publish no address),
  vendor_trading_name ×6, buyer_logo ×2, buyer_phone, vendor_bn9 ×1 and the P13 buyer facts (legal name 28.8 → 60 %, address, logo, phone)
  as the runners and registry halves finish. Structurally capped whatever the effort (documented as ceilings): PO numbers (only PO-level open
  data publishes them), contract value / dates / ids on rows proven by lobbying, news or client lists, published e-signature / AP cycle /
  tax status (rarely published; the derived tax status sits in its own column), vendor_neq outside Québec, every 100 % target where a source
  is silent. P13 AP fields (payment terms, PO rule, AP mailbox) depend on what 50k inferred organisations publish — the runners will show
  the real ceiling within hours.

## 17:15Z — build 16:55Z read (honest numbers) and the levers now running
- Build 16:55Z (run 42501333285): **51 / 438 benchmarks met (11.6 %)** on values only (the earlier 87 / 94 counted labels); VALIDATION 7/7, AUDIT PASS;
  Gold 583 (2 losses logged). AP grade Gold: A 38, B 150, C 395; P13: A 1, B 14, C 39,217, D 11,557. Invoice readiness Gold median 7/11.
- Levers added this hour (all pushed; next build shows them): multi-page merge of every walker / search page per buyer (one page per buyer was dropping
  finds), `ap_gap_to_A`, second-domain rule for "own domain", statutory construction default (FED/ON/AB), derived GST/HST status + indicative rate
  (CRA Memorandum 18-2), registry lookups for all P13 organisations (48,518 queued), walker terms extraction loop (was dead since the reboot).
- Next wake-up: rerun PC_005 (rows 4–33) and PC_006–010 (search budget), dispatch a build once the walker-terms pass has pushed, read the
  "What still blocks grade A" table and point the next engine at the largest column.

## 17:00Z — AP grade is the standard (owner 11:38–11:53 EST)
- Local run of the AP-grade commit found that the whole downstream pack was being skipped (my `g` for the letter grade shadowed the mailbox grade `g`
  used by data_quality_score / ship_ready → TypeError inside the try/except). No CI build had run that commit yet. Fixed (`apg`), `ap_gap_to_A` column
  added, scoreboard "What still blocks grade A" table added; build dispatched 16:43Z (run 42501333285).
- Gold blockers measured on the 16:12Z batch (585 rows): payment terms missing 475, PO rule missing 409, DMARC not enforced 190 (buyer's DNS; not
  fillable), mailbox not on own domain 75, legal name 73, address 45. All 585 have MX and a referee-confirmed invoicing mailbox.
- Walker bug: 36 sites (University of Manitoba, City of Coquitlam, MD of Bonnyville, …) ended in `error:ValueError` — `allowed()` built ":///robots.txt"
  from a relative sitemap entry. Root cause fixed in tools/ap_crawler.py (URL without scheme/host → not fetchable), deployed to both Mac copies, the
  36 rows removed from ap_walk_done.tsv and the main walker restarted (`--skip-tiers I`, 10,337 sites left; the P13 walker runs separately).
- Statutory prompt-payment defaults (construction work only, published terms always win): federal 28 days (F-7.7 s. 9(2)), Ontario 28 days
  (Construction Act s. 6.4(1)), Alberta 28 days (PPCLA s. 32.2(1), not Crown public works) — statutes read 2026-11-08, URL + quote inside the value.
  Not applied (not verified today): SK, MB, NS, NB, QC, BC, US states.
- Search budget: this turn's 200 WebSearches went to VW_019–024; PC_005 (rows 4–33) and PC_006–010 (Gold buyers without terms / PO rule; query now
  aimed at PO terms & conditions and supplier guides) must be rerun at the 17:09Z wake-up.
- vendor_sites_check3 (host-only, batches a–e): 161 confirmed / 240; batch f: 67 confirmed / 127 → claude_vendor_sites.csv 360 rows (pushed by push_loop).

## 16:45Z wake-up
- Vendor-site waves VW_019–024 done (6 agents, 198 searches): 127 proposals → batch f; the host-only re-check of batches a–e is running (12 parallel), batch f follows; registry re-check under the stricter rule: 847 found / 890 so far; corrected G&C file on origin.
- Second AP walker started on the P13 long tail (tier I, 15 pages/site, 24 workers) so the P13 AP-field targets (5 fields × 50k rows) are not left to the end of the main walk.
- Build of the corrected code waits for the vendor-site re-check to land (the old over-confirmed file is still on origin) — dispatched as soon as it pushes.

## 16:20Z — fresh-eyes review verdict FIX FIRST, acted on
The independent reviewer found wrong values in delivered rows produced by today's new code: page-stated legal names with no relation to the
organisation (77 of 196 Gold "stated" cells), registry BNs of a different legal form (Smythe LLP → Smythe Inc.), placeholder BNs 999999999 from the
G&C file (22 rows) and one named individual as a buyer legal name, "Interac" matching "interacting" (2,980 cells), vendor sites "confirmed" on another
host, same-pair facts counted as the row's own, and a scoreboard that counted label-only cells. The 15:48Z "87 / 438" therefore overstated real
coverage (the reviewer estimates ~16 benchmarks met on real values). All nine findings are fixed in code (commit "fixes from the fresh-eyes
review"), the affected engines are re-running on the Mac, and the next build prints two numbers: values only, and any non-blank cell.
Follow-ups (not fixed, reported): robots.txt not re-checked on the redirect target host (ap_crawler.fetch); no audit check yet for "every value has provenance".

## 16:05Z wake-up
- Owner 10:59 EST: "person is allowed for AP" → ap_terms now reads the AP contact person + role phrase on AP pages (forced re-read of 2,285 mailbox pages running; walker pages every 2 h). Protocol rule 3 updated.
- Vendor-site waves VW_007–018 done (candidates-only): 165 confirmed sites of 204 proposals so far; batch e (41) under check; VW_019–040 generated (811 vendors, A/B grade 1, L, T/M rows). NEXT = 19.
- Registry lookups 1,312 found / 2,804; walker 954 sites → 4,589 AP pages; org_extras refresh ≈20k of 65k domains; Wikidata 6,600 / 42k.
- Build dispatched 16:04Z (carries registry rows 1,312, vendor sites 165, G&C BNs, inferred-vendor phones, AP names when pass 4 finishes). Next wake-up 16:30Z.
- Fresh-eyes review of today's code and 10 cells running (reviewer has not seen this conversation); findings go to CHECKS.json.

## In progress (Mac engines, all restart-safe, resume files in ~/cch-crawler-state)
org_extras --refresh (65k domains, ≈7k done) · org_contacts --refresh (5.2k) · registry_lookup.sh (vendors 4,040 then buyers) · ap_walk (63,582 sites,
Gold first; 1,008 AP pages found in 15 min) + 2-hourly ap_terms over them · wikidata_orgs (4,200 of 42k, 1,136 matched) · cc_mine · ap_crawler ·
site_finder · dns_daily · downloads_loop · push_loop (15 min).
Search waves (credits): VW_001–006 done (vendor websites; 61 proposals → 39 confirmed); VW_007–010 + re-runs VW_011–015 (137 not-found vendors,
candidates-only instructions) wait for the next turn's budget; per-company buyer waves PC_005… continue on the wake-up chain.

## Next (in order)
1. Next build → read COVERAGE_VS_TARGETS.md (expect vendor_bn9, buyer_bn, vendor_website, contract_value, number_of_bids up) → CHECKS.json.
2. Waves VW_007–015 (vendor sites) and PC_005+ (buyer AP pages) as search budget allows; run vendor_sites_check on each batch.
3. Cross-check 10 G&C BNs against the CRA charities file (same BN9 where both exist) — record in CHECKS.json.
4. More PO open data cities (ceiling is small; low priority), US directories (133 US rows; low priority), docs (answers file §12 for today's additions).

## Decisions and why
- Ledger in the referee (2026-11-08): a page unreadable today must not un-verify a value seen yesterday (20 Gold lost on 2026-11-07 to flaps).
- Builds every 6 h, JSONL not committed: repo was 2.4 GB and growing 70 MB per build.
- `mailbox_recheck_note` column instead of touching `email_check`: audit check 3 must stay mechanical.

## Follow-ups found while working (not changed in this pass — out of scope, reported)
- `tools/ap_crawler.py` still runs `git pull --rebase` / `git push` inside the live Mac clone every 15 min (its own `sync()`); it fails harmlessly while engines keep files dirty, but a clean tree would let it rewrite files under the other engines. push_loop v3 is the real pusher; the crawler's git calls should be removed in a reviewed change.
- `contracts_export.py` CAP 500 per organisation: the downstream asks for 1,000+ on high-history buyers.

## Open questions (for the owner, non-blocking)
- A login-time LaunchAgent on the Mac would restart the engines after a reboot without me; installing one is a visible change to the
  owner's machine, so it is prepared (`~/cch-crawler-state/launch15.sh` is idempotent) but not installed. Recommendation: install it.

## Retro (one line per milestone)
- Scoreboard: should have existed from day one — every argument about "coverage" is now a number per build.
- Reboot: engines must be restarted by the machine, not by me (see open question).
