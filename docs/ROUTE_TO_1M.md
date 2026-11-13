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

## Update 2026-11-13 06:00Z — what the ceilings are, measured
- Build 05:17Z: 220,736 ready of 286,065 rows. Held rows with a mailbox, by first reason (table of 04:08Z): payment not published 34,575
  (services; 3,407 vendors — billers read today: doteasy, Aplus, Canadian Web Hosting, HostedinCanada, Websites.ca, Coolcom, Vianet, PowerStores
  name an invoice and a bank payment; Jane, Hawk Host, Ex2 are card only), stated by the vendor 4,332, link only 4,348, shared postal code (a
  tower, a campus) ~10,000, mailbox not re-read ~1,700.
- The mailbox reader has read 2.61M lead sites and found a role mailbox on 501k (19 %); 185,837 organisations with a confirmed mailbox had no
  address naming a distributor (rank 04:08Z). Today's passes located 37,949 by their own page source (JSON-LD, embedded map, text) and 17,530 by
  the place that lists their telephone number — the next builds show how many become rows.
- Pool 1 (Canada by location) is bounded by mailboxes (19 % of sites) and addresses, not by sites: the Canadian universe (Overture 629k domains,
  Common Crawl .ca, the web graph, the certificate logs) is read. Realistic ceiling with today's rules: ~300k rows.
- Alberta: 27,946 mailbox owners print an Alberta postal code and electricity there is billed by retailers (no row); 6,310 Alberta rows stand on
  records (licences 1,729, members 1,586 …). Water by location would add ~10-18k (owner's decision, prepared).
- The second half must come from abroad and new relationship kinds: IP owners abroad (sites 18.9k trademark / 8.6k patent of ~150k owners);
  the cross-register and read-site joins add hundreds, not thousands; certification bodies (CSA: blocked; CWB: blocked); NAV CANADA's airlines
  (registered; the CTA's certificate chain is incomplete); more customs microdata (none found open beyond Colombia).

## Update 2026-11-13 08:13Z — 267,950 ready (build 07:49Z); what was added since, and where it leads
- Build 07:49Z: 267,950 ready of 326,765 rows (+12,791 since 06:44Z; +47,214 since 05:17Z). $5k+ a bill 2,814.
- **Bodies that bill by statute and publish whom they bill** (bc-crown, daily): B.C. water rentals 5,486 licensees · B.C. stumpage (invoice numbers and
  values) · Alberta Energy Regulator administration fee 1,197 · Health Canada PMRA annual charges 675 (four invoices a year) · CNSC yearly licence fees
  1,149. ~9,700 organisations, many in Alberta (where no electricity row exists); rows follow once each one's site and mailbox are found.
- **Owners abroad**: the site tests now know 22 countries (nine added today: JP, KR, IL, NO, FI, NZ, TW, IN, CN — ~45,000 owners never looked for), and
  two open registries give candidate sites (ROR 4,273; Wikidata 12,465). This morning's runs tied +640 trademark and +221 patent owners' sites with
  Wikidata, +69 / +127 with ROR; plain runs on the nine new countries are queued.
- Ceiling arithmetic, unchanged in shape: Canada by location ~300k with today's rules; records in Canada (registers, statutory billers, members) ~150k;
  records abroad (IP owners in 22 countries ~200k; Health Canada, PMRA, DIAN, Form 5500, exchanges) — at today's site and mailbox rates ~40-60k rows.
  1,000,000 needs either many more records abroad (customs microdata of more countries — none found open beyond Colombia) or a rule decision (client
  listings; a group's site for a subsidiary at the group's address).

## Update 2026-11-13 09:35Z — the locations no distributor covered, measured and partly closed
- Of 275,632 sites on file that print a postal code, 31,219 are in Alberta (no by-location row: the retailer bills) and ~9,000 elsewhere lay in
  areas the table left out. Closed today, each sentence checked: Ontario by every address point (Overture Maps addresses inside the Energy Board's
  map: +3,591 sites located, 298 withdrawn where two methods disagree), Cornwall Electric (mapped, never carried), Medicine Hat, Westmount, New
  Westminster, Penticton, Coaticook. Still open: Kelowna, Saskatoon, Sherbrooke, Joliette, the interior of FortisBC, the territories, Saint John
  (no open boundary, or a site the reader cannot open).
- Organisations that print no address anywhere: their own privacy / terms / legal pages give 2.5 % of them (4,162 of 165,740) an address beside
  their own name.
- Statutory billers: +AER (1,197 licensees), and an Overture name pass for registers with no address (B.C. stumpage, Alberta wells): 681 leads.
- Measured and not worth it: rendering JavaScript-only sites (17 % of the sites with no mailbox are script pages or parked; 2 role mailboxes in 70
  rendered); AMVIC (card only, no invoice); dealer locators behind their own APIs (not probed).
- Alberta stays the largest pool held by a rule: water by location (31,219 located organisations; ~20,000 rows if the owner says yes) and
  workers' compensation by law (prepared in STATE.md, recommended no) are the two decisions that would open it.

## How it runs without a session
Every lane above is a tool plus a workflow on a schedule; the rank build (rank-buyers, every 6 hours) gathers them; the mailbox reader runs
back to back. A session reads the counts (BUILD.json), reads rows, fixes rules and adds the next pool.
