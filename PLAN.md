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

## Plan v2 — every benchmark, by family (owner 2026-11-08 12:47 EST: "change the approach, not the goal"; written 18:00Z)
Measured base: build 17:49Z = 41 / 438 met, 72 within 10 points (the 12 DNS cells at 99.8 % return to 100 % with the in-build DNS check).
Each line: benchmarks → approach → engine → evidence of yield → when it is in the data.

| family (benchmarks) | approach now | engine | yield evidence (today) | in the data by |
|---|---|---|---|---|
| DNS posture (15) | check new mailbox domains inside every build | rank-buyers.yml step (dnspython) | 12 cells at 99.8 % only because of timing | next build |
| buyer legal name / address / phone / logo / BN (≈90 incl. P13) | offline bulk registries (REQ + Corporations Canada) daily; CBR API 2 req/s on two machines; org_extras refresh; G&C; charities | claude-engines bulk_registry; registry shards; Mac org_extras | 11,286 orgs matched in 5 min; build 17:49Z buyer_legal_name filled 5,938 rows from registries (369 the build before) | registries: now; P13 refresh: ~4 h; CBR passes: ~13 h |
| vendor website / emails / phone / logo / address / trading name / NEQ / BN (≈70) | VW search waves → Mac confirms; org_contacts/org_extras on confirmed sites; REQ NEQ for QC vendors; CC BN | 6 agents / turn (198 searches), Mac readers | VW: 228 sites confirmed of 380 proposals today; vendor_neq +422 rows in one build | each wave +~60 sites; NEQ now |
| AP facts as published — terms, PO rule, address, phone, requirements, portal, contact, system, method, cycle, tax, e-signature (≈150) | walk every buyer site for AP / supplier / purchasing / policy pages and PDFs → extractor; per-buyer searches for PO T&Cs and supplier guides; multi-page merge | 10 GitHub runners (P13) + Mac walker (A–F) + walk_terms loop; PC waves | walker pass on 11k pages: terms 310 → 746, PO rule 555 → 1,251, portals → 2,237, AP contacts → 421 in 2 h | runners' first merge ~22:30Z; Mac walker A–F ~10k sites ≈ 20 h; PC waves 200 buyers / turn |
| contract facts — value, dates, PO / contract / tender numbers, bids (≈90) | NEW: read the buyer's own award page (council report, bid results) for the pair and take value / dates / numbers / bids printed next to the vendor (tools/award_facts.py); Public Accounts payments (AB by department, BC CRF) as labelled values when no award value exists | AF search waves (1,767 pairs, 54 files, Gold first) → Mac award_facts.py | extractor unit-tested (EN + FR); first wave at the 18:22Z wake-up measures the hit rate | first results in the build after the 18:22Z wave |
| records / duration / YoY / commodity / vendor-id / org codes (≈50) | computed from records; award pages add tender / contract ids; PO open data adds vendor ids | same as above | capped by what records carry | — |

### Where a rule, not an approach, is the limit (decision for the owner; my recommendation in brackets)
1. `po_number_as_published` 10–50 % in packages whose buyers publish no PO-level data: award pages give PO numbers only where a report prints them. [keep the rule; report the measured maximum]
2. `contract_value` on rows proven by lobbying / news / client lists: Public Accounts payment totals can fill it only if "annual payments" is an acceptable value basis. [fill, labelled `value_basis = annual payments, not an award value`]
3. Published e-signature / AP cycle / tax status for 50,000 inferred companies: derived GST status exists in its own column; the "published" benchmark needs the buyer to print it. [keep the derived column; measure the published maximum]
4. `vendor_neq` is measured on QC vendors only (scoreboard SUBSET): REQ open data should carry it to the target; outside Québec the number does not exist. [no change]
5. 100 % targets: the last rows are organisations that publish nothing; business directories could close some. [not used: directory addresses are not the organisation's own publication]
