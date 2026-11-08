# STATE.md — Claude lane (updated 2026-11-08 14:40Z)

## Reading of the mission (unattended run; nobody answers questions)
Raise the ranked deliverable's coverage against the downstream team's per-package targets (438 field × package benchmarks,
`COVERAGE_VS_TARGETS.md`), under the integrity rules in PROTOCOL.md, by adding sources and engines that run on their own on the
owner's Mac; report the benchmark count every build; document the ceiling of any benchmark that cannot be met honestly.

## Assumptions made (not asked)
1. `ap_contact_name_as_published` carries role titles only — the owner's "never a named person" rule wins over the downstream 25 % target.
2. Contract value / dates / title / identifiers may be filled from another record of the SAME buyer–vendor pair, labelled with that
   record's id; never from a different vendor. Rows proven by lobbying filings, news releases, auditor appointments, customer
   stories have no contract value: that is the ceiling (≈ 17 % of P01 Gold).
3. `currency` may be defaulted from the source's country when a value exists, flagged "assumed from source convention" (asked by the downstream team).
4. AI search agents only propose URLs; every value is read from the page by a Mac engine with URL + quote.
5. The downstream's `mta_sts_record` / `tls_rpt_record` / `bimi_record` are my `mta_sts` / `tls_rpt` / `bimi` columns (filled since the 06:47Z build).
6. No column is renamed; new facts are new columns. No irreversible action is planned; nothing needs the owner's decision today.

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

## In progress (Mac engines, all restart-safe, resume files in ~/cch-crawler-state)
org_extras --refresh (65k domains) · org_contacts --refresh (5.2k) · registry_lookup.sh (vendors then buyers) · gc_recipients · wikidata_orgs · cc_mine · ap_crawler · site_finder · ap_walk test → full run · dns_daily · downloads_loop · push_loop (15 min) · per-company search waves (self-scheduling wake-up).
Cloud: full local rank test of today's rank.py changes (rank_test2.log) before the next build is dispatched.

## Next (in order)
1. rank test passes → dispatch rank-buyers build → read COVERAGE_VS_TARGETS.md (expect: contract_value / end_date / buyer_legal_name / vendor_bn9 up) → record in CHECKS.json.
2. ap_walk full run (Gold → P02–P05 → rest) + 2-hourly `ap_terms --urls ~/cch-crawler-state/ap_pages_seen.csv`.
3. rank consumer for claude_gc_recipients.csv (buyer_bn_as_published / vendor_bn9 when empty).
4. vendor website waves (search credits; Gold vendors without a site first: 247 rows).
5. more PO open data cities; US directories; docs (README, answers file, D-items).

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
