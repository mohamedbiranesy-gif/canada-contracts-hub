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

## Done today (2026-11-08)
- Scoreboard tool + workflow step (`tools/coverage_targets.py`; baseline 57/438 on the 13:28Z build). Commit b… (see git log).
- Mac reboot 07:30 EST found; every engine restarted 09:16 EST (push_loop, sync_loop, bridge, ap_crawler, site_finder); DNS daily loop to relaunch (below).
- 172 MB PO open-data file gzipped (GitHub refuses > 100 MB); push snapshot now skips any file > 95 MB.
- fetch() follows 308/307/301 by hand, retries broken TLS over http and bare hosts with www. (55 Gold buyer sites answered 308 and were never read).
- Earlier today: charity BNs (7,454 buyers), org directories (6,277), Wikidata (running, 449 matched of 1,300), PO join (330,978 PO rows), Crown BNs, verified ledger in the referee.

## In progress
- org_extras v2 (task 3) — writing now; then `--refresh` run over all 65,431 delivered domains on the Mac (Gold first).
- raw-field audit of bids&tenders / Biddingo / MERX (background, cloud).
- Wikidata full run (Mac), cc_mine, ap_crawler, site_finder, per-company search waves (self-scheduling, next PC_005…).

## Next (in order)
rank same-pair fill + currency default (task 4) → MRAS registry lookup test (task 6) → inferred-vendor facts (task 8) → GC recipients (task 7)
→ AP walker (task 9) → vendor website waves (task 10) → PO cities (11) → US directories (12) → docs (13). Dispatch a build after each engine lands.

## Decisions and why
- Ledger in the referee (2026-11-08): a page unreadable today must not un-verify a value seen yesterday (20 Gold lost on 2026-11-07 to flaps).
- Builds every 6 h, JSONL not committed: repo was 2.4 GB and growing 70 MB per build.
- `mailbox_recheck_note` column instead of touching `email_check`: audit check 3 must stay mechanical.

## Open questions (for the owner, non-blocking)
- A login-time LaunchAgent on the Mac would restart the engines after a reboot without me; installing one is a visible change to the
  owner's machine, so it is prepared (`~/cch-crawler-state/launch15.sh` is idempotent) but not installed. Recommendation: install it.

## Retro (one line per milestone)
- Scoreboard: should have existed from day one — every argument about "coverage" is now a number per build.
- Reboot: engines must be restarted by the machine, not by me (see open question).
