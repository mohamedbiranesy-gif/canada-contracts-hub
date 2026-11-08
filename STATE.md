# STATE.md — Claude lane (updated 2026-11-08 17:00Z)

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
