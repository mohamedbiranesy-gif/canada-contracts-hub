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

## Update 2026-11-13 13:15Z — the map after the owner's direction (07:47 and 08:07 EST)
**Where we stand (build 11:39Z):** 276,301 ready of 333,286 rows (+58,913 since the 23:25Z build of 2026-11-12). The mailbox reader has found a role
mailbox for 550,516 organisations (2.66 million sites read, 19 %); most of the gap between them and the rows is location: 155,744 confirmed
mailboxes still unlocated after every pass on their own pages (text, structured data, maps, legal pages, street + city: 4,937 located by the last),
and ~31,000 in Alberta (no distributor row). Owner's word: Alberta water and workers' compensation — no; client lists — no rows (a lead to
investigate only); a subsidiary on its parent's site — yes, when the tie is published; Sun Life's U.S. branch — yes.

**Canada — levers being built (estimates in brackets):**
| Lever | Measured | Est. rows |
|---|---|---|
| Foursquare Open Source Places (Apache 2.0): new Canadian sites into the scan | 1,010,914 open places with a website, 572,583 hosts, **143,923 registrable domains the scan never had** | +20-25k |
| Foursquare: the one address a domain's places print, for the unlocated | 2,079 of the 155,744 have a Foursquare address and no Overture one | +2k |
| Foursquare: the place listing the unlocated organisation's own telephone number | running (fsq-places.yml) | +? |
| Head office declared to the Québec and federal business registers (exact legal name, province by telephone area code) | to build (tools/bulk_registry_match.py does it for rows) | +10-15k |
| Held rows that give way to the distributor of a located address | 5,276 held non-location rows are located with a mailbox | +4-5k |
| Billers first: the terms of the vendors behind 22,666 "payment: not published" | easyDNS 3,422, Rapidenet 1,154, Namespro 800, Exact Hosting 516 … | +3-5k |
| A subsidiary on its parent's site (tie published) | prepared | +2-4k |

**International — "any project, anything at all that requires a Canadian vendor" (owner 08:07 EST):**
1. Multilateral development banks' contract awards to Canadian suppliers: the World Bank publishes them (Finances One DS01166, CC BY 4.0: 617
   awards since FY2020 in 41 borrower countries; the buyer is the project's implementing agency, named by the Bank's projects API); then ADB,
   IDB, AfDB, EBRD, AIIB, CDB — a buyer abroad under a public contract, the source's own supplier country.
2. Ships that call at Canadian ports: pilotage is compulsory in Canadian waters and billed by the Crown pilotage authorities, harbour dues by
   the port authorities, port services by Canadian ship agents — the ship's operator abroad is the buyer when a port's own schedule names it.
3. Airlines at Canadian airports: the airport authorities bill landing and terminal fees, NAV CANADA air navigation — each airport lists the
   airlines it serves ($5,000+ bills).
4. Foreign owners of Canadian IP (agent of record): 134,458 trademark and 77,385 patent owners abroad; Foursquare names as a new site source.
5. Foreign organisations accredited or certified by Canadian bodies (Accreditation Canada International, the provinces' offshore schools,
   Royal College International); exhibitors and sponsors of Canadian trade shows (PDAC, Global Energy Show, SIAL Canada, CANSEC).
6. Measured and thin: Export Development Canada's transaction disclosure (2,777 transactions signed in 2024, 55 of them buyer financing abroad,
   most behind US Exim, which does not consent to name the buyer).

**Construction, live contracts (owner 08:07 EST):** Calgary's building permits name the applicant and the contractor, but the applicant is a
designer or the builder (48 organisation owners in 33,841 permits since May 2025) — not a lane; Ontario's Construction Act notices (certificates
of substantial performance, ConstructConnect/DCN) — robots.txt bars every reader but Google and Bing: blocked. Next: open-contracting (OCDS)
publishers abroad, provincial major-projects inventories that name proponents and contractors.

**Arithmetic:** the Canadian levers above ~+45-60k (→ ~320-335k); each international lane adds hundreds to thousands; 1,000,000 needs many such
pools abroad, or the foreign-subsidiary decision (by location abroad: Canadian-owned utilities bill every business of their areas — unanswered).

## How it runs without a session
Every lane above is a tool plus a workflow on a schedule; the rank build (rank-buyers, every 6 hours) gathers them; the mailbox reader runs
back to back. A session reads the counts (BUILD.json), reads rows, fixes rules and adds the next pool.

## Update 2026-11-13 15:18Z — owner's rule 18 and what it opens
**Owner 09:46 EST:** "The U.S. power company owned by Canadian company counts as Canadian vendor." Built the same day (tools/abroad_utilities.py,
abroad-utilities.yml; by_location.abroad_where; rank P13): eleven utilities (Tampa Electric, TEP, UNS Electric, Central Hudson, Green Mountain
Power, Versant, Liberty NH and Lake Tahoe, Caribbean Utilities, Barbados Light & Power, BELCO), 376 ZIP code areas wholly in their territories,
the Caribbean islands they serve whole; 94,929 organisations with a website among the places there are being read for a mailbox (Foursquare's
places added). Expected: ~20,000-30,000 rows (a fifth to a third of the sites give a mailbox and an address in the territory).

**Asked (about 15:16Z):** may any foreign company a Canadian company owns be the vendor (Empower and John Hancock with tens of thousands of U.S. plans
named in Form 5500 filings; Stantec, WSP, CGI, New Flyer, GFL, Waste Connections in U.S. public contracts; FirstService's managed associations)?
A yes is the next 100,000+ (estimate corrected below, 16:08Z: measured on the Form 5500 filings, the part billed on invoice is small).

**Canada, the same day:** the mailbox reader was starved (2 sites a run since 08:19Z) — 509,075 place domains had never been read for a mailbox:
third class (sites of places in Canada, other endings) 21 % with a mailbox on the first shard; Foursquare-only domains in a scan cycle (14:22Z);
the CrUX list of Canada (404,256 domains) next; a fourth class re-reads short reads on 12 pages (4 %). Registry head offices: 3,480 located.

| Pool | Status | Est. rows |
|---|---|---|
| Places in Canada never read (third class + Foursquare scan) | running | +15-25k |
| CrUX Canada, other endings | queued in the scan | +3-5k |
| Utilities abroad (rule 18) | leads written, crawl next | +20-30k |
| Registry head offices (QC other names) | done | +3.5k |
| Re-read on 12 pages | queued last | +4k |
| Any Canadian-owned foreign company as vendor | owner asked | +40-60k (corrected 16:08Z) |

## Update 2026-11-13 16:08Z — the two open questions, measured
**Any company abroad a Canadian company owns (asked 15:16Z, unanswered).** Measured on the U.S. Department of Labor's Form 5500 filings of 2024
(Schedule A, insurance contracts; Schedule C, providers paid $5,000 or more): plans that name Empower (Great-West Lifeco) 6,000+ sponsors, John Hancock
(Manulife) ~2,700, Sun Life and Health Insurance Company (U.S.) ~300, Crum & Forster (Fairfax) ~80; Schedule C names Empower on ~10,000 plans, John
Hancock ~3,000, RBC ~400, TELUS Health ~80. Most of that is a retirement plan's recordkeeping and annuity contracts, whose fees come out of the plan's
assets — no invoice to the employer (rule 6) — so the part that is billed on invoice is the welfare insurance (a few hundred employers). The larger
pools a yes would open are U.S. public bodies paying Canadian-owned firms (CGI, Stantec, WSP, AtkinsRéalis, Thomson Reuters' West, Constellation's
municipal software) and tenants of Canadian-owned buildings abroad: estimated +40-60k, not 100k.
**A utility abroad owned by several Canadian pension investors together (not asked yet).** Puget Sound Energy (Washington, 1,181,569 customers in
HIFLD) is owned 23.9 % OMERS, 20.9 % BCI, 15.8 % Ontario Teachers', 13.6 % AIMCo, 15.8 % Macquarie, 10 % PGGM (BCI's own page, 2019: "PSE is now fully
owned by public- and private-sector pension and retirement fund managers"; the stakes from IPE Real Assets) — 74 % Canadian. ALLETE (Minnesota Power,
148,332 customers) was acquired on 2025-12-15 "by a partnership led by Canada Pension Plan Investment Board and Global Infrastructure Partners"
(ALLETE's own release; shares not stated). SAESA (southern Chile) is held by Ontario Teachers' and AIMCo. Rule 18 says "a Canadian company owns"; a
majority held by several Canadian pension investors is the owner's call. Size by Tampa Electric's ratio (850k customers -> ~50k place sites -> rows at
a fifth to a quarter): Puget Sound Energy ~+12-15k rows, ALLETE ~+2k.
**Not taken, checked today:** FortisTCI — not among the companies Fortis lists on its own "Our Companies" page (read 16:08Z); Empire District
(Algonquin, confirmed by the LEI register) — no territory map of Missouri, Kansas or Oklahoma found (HIFLD has only a county fill of Benton County, AR);
Maine's state map of service areas dates from 1998 and says its lines "do not represent legal boundaries" (Versant stays on HIFLD's polygons).

## Update 2026-11-13 16:43Z — build 16:22Z: 283,713 ready of 341,713; rule 18 lane corrected and widened
- First abroad rows (organisations already on file): 184 — Tampa 66, GMP 20, Central Hudson 24, TEP 22, Liberty NH 24 (wrong: the county-fill error,
  removed by the rebuild dispatched 16:43Z), Barbados 11, Bermuda 6, Grand Cayman 5, Versant 5, UNS 1. The island names alone no longer locate
  anyone (a postal code or a street address on the island is needed).
- Territories now come from the utilities' own words where HIFLD's polygon is coarse (Versant's town list, Liberty's tariff, UNS's named cities).
- Places at a territory's edge are located by their own point (~200 m inside, clear of other utilities): ~41,000 places on Overture alone, plus
  Foursquare's — the places run with points follows the one running now. Leads: ~108,000 by ZIP code area + the points.
- Expected from the lane: +20,000-30,000 rows as the mailbox reader, the referee and the builds catch up (first crawl of the leads running since 15:36Z).
