# PLAN.md — closing the downstream team's coverage targets (Claude lane, 2026-11-08)

Goal: raise "benchmarks met" in `coord/results/ranked/COVERAGE_VS_TARGETS.md` (baseline 2026-11-08 13:28Z build: **57 / 438**)
as far as the integrity rules allow, and document the ceiling of every benchmark that cannot be reached. Owner's measure stays
P01 Gold (585). Everything runs unattended on the Mac; the cloud session only writes code, prompts and reports.

## Approach chosen (and what was dropped)
Chosen: fix the readers first (one bug — unfollowed 308 redirects — hid 55 Gold buyer sites), then widen extraction on pages we
already read (JSON-LD, terms pages), then add registries and open data by join, then spend search credits only on what no engine
can find (vendor websites). Dropped: re-crawling every site from scratch (103,618 domains already read; 363 unread), buying data,
any registry behind a CAPTCHA or login (CRA GST, Ontario OBR), SMTP probing, LinkedIn.

## Tasks (each with its check)
| # | task | produces | check |
|---|---|---|---|
| 1 | coverage scoreboard in every build (`tools/coverage_targets.py`) | COVERAGE_VS_TARGETS.md, coverage_history.csv | SUMMARY.md prints "benchmarks met N / 438" |
| 2 | fetch follows 308/307/301, retries TLS/www (`tools/ap_crawler.py`) | all engines read 55+ more Gold sites | re-read of the http_308 domains returns 200 |
| 3 | org_extras v2: JSON-LD Organization, terms-page legal names, public-body name patterns, logo fallbacks, supplier-portal links, e-sign / payment / tax mentions; `--refresh` of read domains | claude_org_extras.jsonl.gz v2 rows | buyer_legal_name P01 Gold ≥ 41.2 % + and rising in the next build |
| 4 | rank: same-pair richest-record fill for value / dates / title / description / ids; currency default flagged; records_with_this_vendor = 1 for lead-based rows | contract columns | contract_value P01 Gold ≥ 65 % + |
| 5 | raw-field audit (bids&tenders, Biddingo, MERX full files) → mappers for amounts / dates / ids the normalizer dropped | rank.py mappers or pipeline fixes (follow-up to Codex/Jules lanes) | audit report in NOTES.md |
| 6 | Canada's Business Registries (MRAS) lookup for vendors lacking BN / address | claude_registry_lookup.csv | test: 20 known vendors return their BN |
| 7 | federal grants & contributions recipient BNs → buyer_bn_as_published, vendor_bn9 | claude_gc_recipients.csv | match rate on charities (BN agrees) |
| 8 | inferred-vendor facts table (Crown corps / utilities: phone, address, site) for P13 | claude_inferred_vendor_facts.csv | vendor_phone P13 ≥ 60 % |
| 9 | AP site walker: follow the buyer's own vendor / AP / purchasing links + PDFs, run ap_terms | claude_ap_terms.csv rows | payment_terms P01 Gold rising |
| 10 | vendor website waves (search credits; Gold first) → site readers | websites.tsv / vendor_website | vendor_website P01 Gold ≥ 57.8 % + |
| 11 | more PO open data (Ottawa, Calgary, Winnipeg, Vancouver, Halifax, Gatineau…) | claude_po_records.csv.gz | po_number P01 Gold rising |
| 12 | US directories (NCES, IPEDS, Census GUS, HRSA), USAspending UEI | claude_org_directories.csv | buyer_address / phone on US rows |
| 13 | docs: README, answers file, D-items status, coverage note on structural ceilings | prompts/, README | reviewed by a fresh subagent |

## Pre-mortem (how this fails in six months) and the check for each
1. A reader bug silently zeroes a column (as the 308 bug did) → `coverage_history.csv` delta per field per build; a drop > 5 points
   in any P01 Gold field is flagged in SUMMARY.md (task 1 prints gaps; add the drop alarm — done in coverage_targets.py Δ column).
2. A Mac reboot kills every engine (happened 2026-11-06 and 2026-11-08 07:30) → `launch15.sh` is idempotent; a LaunchAgent
   that runs it at login is the follow-up for the owner (cannot be installed without the owner: visible system change).
3. Joined open data goes stale (PO numbers, directories) → every row carries `retrieved_date`; weekly re-harvest in `sources_round1.sh`.
