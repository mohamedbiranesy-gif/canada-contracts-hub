# STATE.md — Claude lane (updated 2026-11-08 14:40Z)

## Reading of the mission (unattended run; nobody answers questions)
Raise the ranked deliverable's coverage against the downstream team's per-package targets (438 field × package benchmarks,
`COVERAGE_VS_TARGETS.md`), under the integrity rules in PROTOCOL.md, by adding sources and engines that run on their own on the
owner's Mac; report the benchmark count every build; document the ceiling of any benchmark that cannot be met honestly.

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
