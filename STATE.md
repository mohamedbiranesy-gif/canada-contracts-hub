# STATE.md — Claude lane (updated 2026-11-08 20:45Z)

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
