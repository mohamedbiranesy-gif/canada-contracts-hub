# Route to 1,000,000 buyers (lane `claude`, 2026-11-12 23:55Z)

One row per buyer; a Canadian biller with a current relationship that is a fact, a bill on invoice, a bank payment, the organisation's own
role mailbox re-read by the referee (AGENTS.md rules 1-17). Counts below are counted from files on hand (build 22:02Z, lead store, registers).

## Where we stand
- 217,145 ready rows of 281,683 buyer rows (276,030 with a mailbox); 921,843 leads on file (tech 704,531; vendor pages 155,752; member /
  licence 61,560). The mailbox reader has read 2,344,928 sites and found a role mailbox on 440,174 (19 %).
- $5,000+ a bill: 2,220 rows (1,871 published, 349 estimated).

## The route, pool by pool (target = rows ready; one row per buyer, so pools overlap and a record upgrades a by-location row)
| # | Pool | On file / size | Ready now | Target | Machinery | What it takes |
|---|------|----------------|-----------|--------|-----------|---------------|
| 1 | Canadian organisations by where they are (the distributor of their address) | ~1.4M Canadian organisation sites; ~500k with a role mailbox and a printed address | 141,248 | 400,000 | credit-scan (universe, graph, overture) -> lead-sites -> mailbox-crawl -> site-facts -> rank | read ~1.3M more Canadian sites at 19 % |
| 2 | Records in Canada: members, licences, registers, contracts | rosters 54,785 listed; trademark owners in Canada 107,583; patent owners 16,566; Health Canada ~2,700; regulators' firm registers 100k+ (ESA, HCRA, TICO, RECO, AMVIC …) | 75,897 (all non-location kinds) | 150,000 | roster_ingest, tm/pt/hc/radio/rbq/authority registers, contract dataset | registers queued in coord/source_registry.csv |
| 3 | Records abroad | trademark owners abroad 134,458; patent owners abroad 77,385; Health Canada abroad ~4,600; Colombian importers ~1,500 a year; US Form 5500 sponsors 3,923; listed issuers abroad ~200 | ~12,000 | 90,000 | tm-sites, pt-sites, hc-registers, dian-imports, f5500, exchange-issuers; tools/overture_names.py; domains tied only on a published identifier | site found for 40 % and mailbox for half of those |
| 4 | Services seen on the buyer's side, billed on invoice (not a card on file) | 704,531 tech leads | 25,174 | 50,000 | credit-scan / dns-services / tech portals | invoiced B2B services only (rule 6) |
| | **Mapped total** | | **217,145** | **~690,000** | | |
| 5 | Still to find: ~310,000 | certification bodies' directories (CSA Group, Canadian Welding Bureau ~7,000 companies, BNQ, QPS); customs declarations of more countries (Peru, Ecuador, Paraguay, Uruguay, Costa Rica, Ukraine — codex); US UCC filings naming a Canadian secured party; industrial-design owners abroad; CER levies, BC stumpage, CIRO, Accreditation Canada abroad | | 310,000 | to build (registry rows written 2026-11-12) | the search continues every session |

## Decisions that would move the line (the owner's to make)
- Client listings on a Canadian vendor's own site are "the vendor's statement" (rule 1): 155,752 such leads, 31,977 buyer rows with a
  mailbox. A dated page (12 months) and the client's live site could make them a labelled row ("stated by the vendor") — not done without
  the owner's word.
- A Canadian company's U.S. branch as the biller (Sun Life Assurance Company of Canada, 3,873 US employers): kept, labelled, unless he says no.

## How it runs without a session
Every lane above is a tool plus a workflow on a schedule; the rank build (rank-buyers, every 6 hours) gathers them; the mailbox reader runs
back to back. A session reads the counts (BUILD.json), reads rows, fixes rules and adds the next pool.
