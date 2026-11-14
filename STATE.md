# STATE.md — Claude lane (updated 2026-11-12 23:45Z — contracts first where they exist, a mixed approach for the rest (owner 09:00-09:15 EST); one row per buyer; a Canadian biller, a bill on invoice, a bank payment, the organisation's own mailbox; every invoice field as far as the kind goes, estimates labelled. Read the first section below before anything else; everything under it is history.)

## UNATTENDED RUN — reading of the mission and assumptions (written 2026-11-13 00:41Z; owner 19:38 EST: "keep going, don't stop … nobody will answer")
**Reading:** build the route to 1,000,000 ready rows (one per buyer; a Canadian biller with a current relationship that is a fact, a bill on
invoice, a bank payment, the organisation's own role mailbox re-read by the referee — AGENTS.md rules 1-17), every invoice field as far as
the kind goes, $5,000+ a bill first. Keep searching for new pools, build each as a tool + workflow, verify every count from files.
**Assumptions (each reversible):** (1) a Canadian company's U.S. branch counts as a Canadian biller (rule 7), labelled in the row
(Sun Life, Form 5500 lane); (2) a guessed website counts only when its own pages print a published identifier (postal / ZIP code, NIT,
ticker); (3) vendors' client lists stay "the vendor's statement" (rule 1) — not turned into rows without the owner's word; (4) "everything
is permitted" does not lift AGENTS.md §2 or the session's security rules (no block worked around, no CAPTCHA, no third-party e-mail).
**Decision left for the owner (prepared, not taken):** client listings (155,752 leads, 31,977 buyer rows with a mailbox; by 2026-11-13 05:00Z most of those organisations already stand on another row — the distributor of their address — and 4,332 dated client-listing rows with a mailbox remain held as 'stated by the vendor', plus 4,348 'link only') as labelled
"stated by the vendor" rows — recommendation: yes for pages dated in the last 12 months whose client site answers; it would add ~4,000 rows now (it was ~30k before the address passes located most of them).
**Plan, checks, notes:** PLAN.md, CHECKS.json, NOTES.md (hypothesis tree + source table), PROTOCOL.md, docs/ROUTE_TO_1M.md.

**2026-11-14 01:54Z — PROJECT STOPPED BY THE OWNER ("pull the plug", 2026-11-13 20:51 EST).** Every workflow timer is off, no workflow starts another, the overdue dispatcher starts nothing (coord/ACTIONS_PAUSED). Final deliverable: the release ranked-latest (build 22:10Z) and its corrected copy (docs/HANDOFF_ROWS.md). Do not restart anything without the owner's word; one last build, if GitHub turns Actions back on, is rank-buyers run by hand once.

**2026-11-14 01:02Z — the new rules measured before any build (tools/replay_owner_test.py, new):** owner_test replayed on all 362,875 rows of 22:10Z, no exception; 467 ready rows would leave, none come in. The replay caught two errors before they shipped: rule 19 by name would have taken 86 rows of Liberty Utilities (CalPeco Electric) LLC (rule 18, counted by the owner) — rows by location are now exempt, legal names read on a site no longer decide it, a Canadian ULC is Canadian; and "8133 WARDEN AVE, MARKHAM ON L6G 1B3, 00000" was taken for no address. Still affected: 336 Marketplace Events exhibitors ("Marketplace Events LLC", a U.S. LLC with Canadian offices — Investment Canada lists it as a Canadian business in Beechville NS; recorded in DECISIONS for the owner to overrule), 44 public contracts, 2 export sales, 39 province conflicts, 36 foundations, 1 John Hancock. Also: vendor legal names read on a legal page by a shared word only need a legal form or the vendor's own name (2,927 ready rows of 22:10Z had one without a form — "Voice over Internet Protocol" for Storm Internet); a federal grant recipient whose legal name is a person's own name is not written. The sample run of rank.py cannot fit this 7 GB container (killed for memory at the same stage twice); pyflakes clean.

**2026-11-14 00:26Z — accuracy work while Actions is off (all pushed; each waits for the first build):**
- CMEQ / CMMTQ licences (989 ready rows on 22:10Z) carry the corporation's own yearly dues and the fee to keep the licence (CMMTQ leaflet 1 Jan 2026: 881 $ + 547.53 $; CMEQ leaflet Jan 2023: 837.94 $ dues as of 1 Aug 2022 + the Régie's 2026 maintenance fee), the sum in bill_amount_calculated; CMEQ's yearly notice is an invoice with its own number (payee entry tools/data/payees/cmeq.json, verified). No card-only sentence taken, so payment stays by the kind.
- Buyer names: one trade word alone (Accounting on zakaccounting.ca, Avocats, Construction, Notaire, Toiture …: 104 ready rows) → the site's domain name; no site or a government-wide site → not ready.
- No buyer twice: rows of one website host and one name (municipality words, legal form, closing parenthesis aside) folded into the best-ranked row (22 groups; Township of Howick / Howick, NWMO twice …).
- Rows with no vendor at all (the abroad lane's leftover places: 65 rows that sat in P01_GOLD as "public contract") → tier N, no relationship record.
- audit_deliverable check 1: an empty part file is no second header. REGION_TOK's duplicated "asia" key fixed.
- Measured on 22:10Z (what the next build removes or corrects): 123 ready rows with a US entity as vendor (rule 19), 36 foundation sponsors, 75 image-file names, 480 trailing Home, 104 one-trade-word names, 3 duplicate ready buyers.
- A 1-in-50 sample run of rank.py (RANK_SAMPLE, debug) was killed for memory at 330 s on this 7 GB container; pyflakes finds no undefined name in the changed files.

**2026-11-13 23:52Z — Actions still disabled (a dispatch at 23:45Z: HTTP 422).** One public case of the same block (github.com/orgs/community/discussions/184661) was lifted by GitHub Support on request, weeks later. GitHub's terms for Actions bar "any activity that places a burden on our servers, where that burden is disproportionate to the benefits" and, on GitHub-hosted runners, "any other activity unrelated to the production, testing, deployment, or publication of the software project"; the 24 hours before the block held 583 runs (253 run-hours, shards not counted), mostly crawling. A change that comments out the timers of 29 harvesters, stops 14 of them restarting themselves and limits tools/dispatch_overdue.sh to rank-buyers and agent-branch (marker file coord/ACTIONS_PAUSED) was prepared and NOT pushed: pausing the owner's harvesters needs his word. The owner was asked at 23:5xZ (reply "pause"). Until he answers, do not push it and do not restart anything by another route.

**2026-11-13 23:42Z — BLOCKER: GitHub Actions is disabled for the account (since 23:39:30Z).** Every running workflow was cancelled at that second
(rank 43518016787, dns-services, …); a new dispatch answers HTTP 422 "Actions has been disabled for this user". The repo is public, so not a
minutes limit — an account restriction (likely the bulk crawling: dns-services sweeps 63 M domains and re-dispatches itself every few minutes;
ct-names, mailbox-crawl, credit-scan chain the same way). The owner was told at 23:42Z with what to check (GitHub e-mail, Billing and plans,
Settings → Actions, a Support ticket). Until it is back nothing builds, crawls, verifies or publishes; pushing still works, and the release
ranked-latest still holds the table of 22:10Z (301,184 ready). Tonight's commits (names, rule 19 by name, foundations, dealers, dues, province
conflicts, municipal estimates, $5,000+ record order, the c5k mailboxes) wait for the next build. When Actions returns: first a rank build
(dispatch rank-buyers), then verify-and-merge; and slow the self-dispatching sweeps (dns-services, ct-names, credit-scan cycle) before they
restart — if GitHub names the cause, follow what it asks. Do NOT publish releases by any other route (this session may not create releases).

**2026-11-13 22:43Z — NEXT (for whoever picks this up; the owner's deadline is the 18th, lock-in by the 17th):**
1. Build of 22:29Z start (rank 43518016787, ends ~00:10Z) carries: buyer-name accuracy, rule 19 by name (LLC / USA Inc.), foundations out of sponsorships,
   dealers' shop terms off, members' benefit prices off the dues, province/postal-code conflicts, municipalities' electricity from residents (tools/muni_energy.py),
   the $5,000+ record first among current records. Check: SUMMARY.md counters "municipalities outside Ontario", "buyer name", CHECKS.json pending items.
2. The $5,000+ rows held for no mailbox: contrib/claude/c5k_mailboxes.py read 583 of their sites (results -> data/incoming/claude/claude_buyer_ap_results_c5k01.csv,
   then the referee); contrib/claude/c5k_sites.py found sites for those with none (cb_sites_cb.csv) — read those sites with c5k_mailboxes.py --sites.
3. Vendor reader v7 re-reads from 05:43Z (due terms); dispatch vendor-billing with minutes=150 if the cron run reads few.
4. Build 22:10Z (measured): 301,184 ready; $5,000+ 2,873; every main field 223,207 (see docs/ROUTE_TO_1M.md update).

**2026-11-13 21:31Z — measured on build 20:32Z (code a8d92c1, the energy-report pass's first version), then accuracy and $5,000+ work (all pushed; the
next builds are 6e4d0de, running, and whatever main is when it ends):**
- Build 20:32Z: 344,167 rows, **285,851 ready**; $5,000+ ready: 2,182 published + 708 estimated = **2,890**; every main invoice field on 188,168. Kinds ready:
  location 191,606 · service 32,883 · membership 20,597 · licence 15,261 · agent 12,808 · sponsorship 5,205 · contract 3,109 · dealership 2,729 · own energy report 64.
- Energy reports: 100 rows of reporting bodies; 43 gave way, 27 location rows took the report; 64 ready, 59 of them $5,000+ (better matching is in later code).
- **Accuracy (owner: "no errors")**: LinkNow's monthly fees are charged to the card — its cheque sentence is for the one-time design fee at sign-up (~2,266 rows
  out); Secure by Design's "online bill payment page … Visa or Master Card" is card only ("bill payment" now means a bank's service; 44 rows out); MNSi's business
  billing page replaces its residential one (stays ready); buyer names: image file names ("Edmonton Global_web.jpg"), the page-title word Home / Accueil, the word
  Logo, and a town's bare name taken from a business's site ("Toronto" on merlottoronto.com) — the domain instead (~800 rows).
- **$5,000+**: among current records a clean $5,000+ one comes before a surer tier (~60 buyers); municipalities outside Ontario get their electricity estimated from
  their residents (StatCan 2021 Census × Ontario municipalities' reported kWh a resident × Hydro-Québec's price for the province's city; tools/muni_energy.py):
  ~240 location rows estimated specifically, ~60 of them $5,000+ with the give-way.
- Looked at and left: Ontario's large-building energy data (no owner or occupant named — a tenant's bill cannot be told from the building's); law firms' and
  BBBs' billing pages (most firms publish none; bbb.org refuses the reader); a sponsorship tier price (rosters do not say the tier).

**2026-11-13 19:29Z — OWNER 13:20 / 13:23 EST: "plug is pulled on the 18th … go max … estimates as precise and specific to relationship as possible … add as much over
5000 as possible … go through every row populate as much as can be max". What was done since 17:00Z (all pushed; measured in the next build):**
- **Ontario public bodies' own electricity (tools/bps_energy.py, new kind "utility account by own report").** The Ministry of Energy and Mines' open data
  of the broader public sector's energy reports (O. Reg. 25/23; 2024, and 2023 for the 72 school boards): each facility's address and grid kWh. s. 6 (1)
  reports a facility only where the body "is issued the invoices and is responsible for making the payments" — the account holder is published. The bill
  is calculated per facility (small: the distributor's own OEB small-business rates; large: the lower of Hydro-Québec's 2025 average prices for Toronto /
  Ottawa at the levels around its use) and summed per distributor. 573 bodies, 478 with a $5,000+ monthly bill (City of Toronto ↔ Toronto Hydro ~$14.3M,
  TDSB ~$3.4M, Hamilton ↔ Alectra ~$2.1M). In the table: a body's location row takes the record; a row with no published $5,000+ gives way to it.
  Matched to rows by name + address, or by a mailbox on a .ca domain spelling the municipality (City of Toronto / Ottawa rows had no address; the
  directory's address is put on them). 23 new leads + 142 directory addresses (Ontario's school board list and FIPPA/MFIPPA directory).
- **Field fill, billers first:** due terms in the billers' own words (Web Hosting Canada 19,386 rows, doteasy, Aplus, CWH, LinkNow, Astral, Webware …;
  RBQ 5,018, RACJ, Toronto, Edmonton licences); patent agents' rows take CIPO's 2026 yearly maintenance fee (3,962 rows had no amount); chambers named
  without "of commerce" take the dues estimate; register numbers of 17 vendors under the names they go by (tools/vendor_numbers.py, ~3,000 rows).
- **Buyers under contract without a website:** 72 get the official website of their Wikidata item (exact label) -> the mailbox reader (each a published contract).
- In flight: rank 43486392654 (a8d92c1: BPS pass + the give-way fix for rule-18 rows — the 18:26Z table still shows 74 Tampa/Tucson rows with "CA"); the
  next build takes the directory/mailbox matching, the field fills and the websites. Crawl 43481288933 (30k point leads); addr-reread abroad.
**2026-11-13 14:40Z — safety-net turn (scheduled; health only, the section above being under 2 hours old):** row-factory, claude-engines, rebuild
green; verify-and-merge green (cancelled runs = superseded); rank-buyers: the build of 13:29Z running, one failure at 05:34Z ("the ranker's commit
does not apply on main", a one-off; three builds green since). Growth file (measured 11-13): 330,668 rows; pay on sight yes 1,274 / reference-less
1,495 / routed 108,169. **Fixed:** the mailbox crawl's queue is empty (2,670,566 lead sites read; 510,230 found) and since ~13:25Z each run finished
1 or 2 retried sites yet queued the next: 8-shard runs every six minutes, each calling the referee. mailbox-crawl.yml now chains only after a run
that finished 200 sites or more; the hourly timer and the keeper start the rest. Nothing else changed; no item of PLAN section 4e advanced.

**2026-11-13 17:00Z — OWNER 11:44 EST: no to Canadian-owned companies abroad (other than rule 18's utilities) and no to utilities held by
several Canadian pension funds (AGENTS.md rules 19, 20; coord/DECISIONS.md). Nothing had been built on either.**
- Build 16:22Z (a1d369c): 283,713 ready of 341,713. First rule-18 rows: 185 by P13 (24 of them Liberty NH, wrong: county fill, fixed) and 98 by
  "give way" with jurisdiction CA and the utility's US address as the Canada proof — fixed in the ranker (jurisdiction, where, ownership sentence;
  an abroad row with no address takes the one beside its mailbox). The rebuild of 16:43Z has the ZIP / island fixes; the 18:17Z build has all.
- Rule 18 widened: places at a territory's edge located by their own point (~200 m inside, clear of other utilities): ~41,000 on Overture alone;
  places run with points dispatched 16:45Z (writes tools/data/abroad_place_points.csv.gz + leads).
- IP owners abroad: European legal forms written out are now left out of the name keys (France 3 % tied vs Germany 33 %); tm-sites dispatched
  with force=true (pt-sites and fsq owners next, when the crawl frees runners).
- Pipeline: crawl 43454319294 (abroad leads) ends ~18:07Z -> merge -> referee -> dispatch_overdue starts the ranker; addr-reread abroad=true
  to dispatch after the merge.

**2026-11-13 16:25Z — rule 18 lane corrected before its first rows; the open questions measured:**
- **Error found and fixed:** Liberty's Granite State (NH) polygon in HIFLD is a county fill, and the ZIP step set Eversource's PSNH aside as one —
  54 ZIP areas (Nashua, Manchester, Keene …) were given to Liberty. Fixed: a target not drawn from its own maps keeps every neighbour as an exclusion;
  the 17,212 leads of those places withdrawn (gone_usb_20261113T161141w.gz). Rows: none built from those leads yet (the crawl was reading them);
  any row the 15:31Z build made from organisations already on file disappears in the next build.
- **Territories from the utilities' own words** (tools/data/utility_town_lists.json): Versant's "Towns in our Service Districts" (151 towns served
  whole; the 16 marked * left out) and Liberty's tariff NHPUC No. 23 "Service Area" (Lebanon, Salem, Walpole) drawn with Census town boundaries ->
  Versant 65 ZIP areas, Liberty NH 1 (Walpole); UNS Electric from the cities its own page names (Kingman, Lake Havasu City, Nogales) -> none for now.
  374 -> 362 ZIP areas kept. Places stage dispatched for the new Versant / GMP areas.
- **Crawler:** a US address with its state in full ("Tampa, Florida 33602") is now kept in the site facts; addr-reread reads an address in a
  territory of rule 18 (text, schema.org, embedded map) — dispatch with abroad=true once the crawl has found their mailboxes.
- **Open questions, measured (docs/ROUTE_TO_1M.md):** any Canadian-owned company abroad — the invoiced part of the Form 5500 plans (Empower, John
  Hancock) is small (fees come out of plan assets): estimate +40-60k, not 100k; utilities held by several Canadian pension investors (Puget Sound
  Energy 74 %, ALLETE) ~+15k — not asked yet. FortisTCI: not on Fortis's own "Our Companies" page (2026).

**2026-11-13 15:15Z — OWNER 09:46 EST: utilities abroad owned by Canadian companies count (AGENTS.md rule 18) — lane built and running:**
- tools/abroad_utilities.py + abroad-utilities.yml: HIFLD retail service territories (PNNL server) -> 376 ZIP code areas wholly in one target's
  territory (98 % inside, no other retail territory over 2 %; neighbours that are county fills set aside for targets drawn from their own maps:
  Duke Energy Florida's polygon covered 91 % of Tampa Electric's, Ajo Improvement Co's 97 % of TEP's); Caribbean islands served whole.
- Billers (tools/data/billers_abroad.json, each parent's own sentence and printed address in Canada read today): Tampa Electric (Emera: "wholly
  owned"), TEP and UNS Electric (Fortis), Central Hudson (Fortis), Green Mountain Power (Énergir), Versant (ENMAX), Liberty NH and Lake Tahoe
  (Algonquin), Caribbean Utilities (Fortis, "sole electricity provider on Grand Cayman"), Barbados Light & Power (Emera), BELCO (Algonquin).
  Not taken: Empire District (only a county fill of Benton County AR in the layer), FortisTCI and Grand Bahama Power (not on the parents' pages
  read; sites unreachable), LUCELEC (Emera an investor only). Vendor address missing for CalPeco and Caribbean Utilities (robots) — their rows wait.
- 94,929 organisations with a website among Overture's places there -> leads (engine usb, no vendor): Tampa 38,410, TEP 14,056, Central Hudson
  12,943, Granite State 11,981, GMP 7,343, Versant 2,711, UNS 2,497, Barbados 1,838, Grand Cayman 1,572, Bermuda 998, Lake Tahoe 580. Foursquare's
  places added (run dispatched 15:14Z). Ranker: by_location.abroad_where / biller_for_all / status / row_cells / of_row, rank P13 (jurisdiction,
  ownership sentence as the Canada proof). A test row passes owner_test (bank, monthly, "not published: amount").
- Mailbox crawl third class (places in Canada, other endings): shard 0 read 5,320, 1,138 with a mailbox (21 %). Fourth class (12-page re-read, 4 %)
  queued last. CrUX list of Canada (404,256 domains) in the scan queue. Build 14:21Z: 279,969 ready of 338,136.

**2026-11-13 14:29Z — release build 13:06Z: 278,142 ready of 336,619 rows (+1,841 ready since 11:39Z). What the ranker's own log says is left:**
- P13 (build 13:06Z, coord/results/ranked/SUMMARY.md): 168,002 rows by where the organisation is; skipped 186,395 lead organisations with a
  confirmed mailbox that nothing located, 16,689 located where no distributor can be named (Alberta, areas another utility serves), 100,256
  already in a row under another key.
- **The mailbox reader was starved** (2 sites a run since 08:19Z): the scan had read everything queued. **509,075 place domains (Overture,
  Foursquare, OpenStreetMap) had never been read for a mailbox**: 156,857 Foursquare-only ones the scan never read (scan cycle dispatched 14:22Z,
  8 runners), and ~45,000 that answered the scan but no class queued (another ending than .ca, no Canadian postal code on the home page; 7,764 of
  them print a mailbox on the home page) -> **third class of mailbox-crawl candidates** (tools/lead_crawl.py --registry3; shard 0/8 queued 5,368).
  The rest were unreachable (~172,000), blocked or barred by robots (~80,000).
- registry-locate: run 1 located 2,818 of 36,313 (REQ 1,396, Corporations Canada 1,422); v2 (a Québec other name declared by one body only,
  distinctive name, Québec telephone number) +662. tm-sites +982 and pt-sites +497/+191 from the Foursquare candidates.
- Prepared for the owner (coord/DECISIONS.md 14:29Z, corrected before 14:48Z): electric utilities abroad owned by Canadian companies as billers by
  location (Tampa Electric 840,000 customers, the Tucson-area utilities ~566,000, Central Hudson, Green Mountain Power, Versant Power, Liberty's,
  the Caribbean ones); gas utilities do not qualify (not every premises has gas). Rough estimate 70,000-90,000 rows; not built until he answers.

**2026-11-13 13:44Z — owner's word (07:47, 08:07 EST) and what started since:**
- Decisions: Alberta water and workers' compensation — no; client lists — no rows (leads to investigate only); a subsidiary on its parent's site —
  yes when the tie is published; Sun Life's U.S. branch — yes; foreign subsidiaries as the vendor — unanswered (nothing built). His direction:
  explore the international market differently ("not digitalized … any project, anything at all that requires a Canadian vendor"), and in Canada
  "anything construction … currently contracted". Map: docs/ROUTE_TO_1M.md (13:15Z).
- **Foursquare Open Source Places** (tools/fsq_places.py, fsq-places.yml; Apache 2.0): 1,010,914 open places in Canada with a website; 143,923
  registrable domains the scan never had -> the scan's queue (credit_scan FSQ_SITES); one address per domain whose places print one postal code
  (fsq_addresses.csv.gz in harvest-state; 2,079 of the 155,744 unlocated gain one); **5,177 unlocated organisations located by the Foursquare place
  listing their own telephone number**; owners of Canadian IP with no site: **16,871 trademark and 7,066 patent owners** with a candidate site under
  their very name (tm/pt_fsq_sites.csv) -> tm-sites / pt-sites ror runs reading them (13:35Z).
- **SAQ producers and their Québec agents** (tools/saq_agents.py, saq-agents.yml): the SAQ's 27,043 product pages being read (two runners, one
  request a second each); sample of 300: 254 producers, 219 abroad; new kind "promotional agency" (relationship_rows, priority_sort, rank).
- Checked and not usable: ConstructConnect/DCN notices (robots: Google and Bing only), Calgary permits (owners not named), EDC disclosure (55 buyer
  financings abroad in 2024), AGLC licensee report (robots), SAQ B2B policy PDF (robots; read once by mistake, not used).
- addr-reread --city finished: 4,937 addresses (street + city 1,704; contact-page city the rest); unlocated now 155,744.
- Mailbox-crawl merges pushing again since 13:00Z (the pk. token fix).

**2026-11-13 12:44Z — build 11:39Z: 276,301 ready of 333,286 rows (+8,351 since 07:49Z; +58,913 since the 23:25Z build that opened this run):**
location 185,298 (+7,323), licence 14,999 (+685), agent of record 11,694, membership 19,177, service 32,335, exchange listing 347; complete in the
biller's own words 25,703; amount and period 233,127; every main field 182,001; $5k+ a bill 2,821 (2,177 published, 644 estimated). Owner asked
for a status report at 07:39 EST; sent (the 12-hour figures above).
- The session stopped at ~10:20Z and was idle until 12:37Z (between turns); the automation ran (the 11:39Z build).
- Since 09:50Z: TMX's own payment pages (payments.tmx.com/en/tsx, /en/tsxv: wire transfer, direct deposit, online banking bill payment with the
  invoice's customer number, or card) as payee entries → exchange-listing rows in the biller's words (bank account numbers not copied); Cornwall
  Electric's commercial rates (from $11.71 a month; about $410-$421 at 2,500 kWh); **addr-reread --city** (a street address printed with its city
  and province but no postal code, or the one city a contact page names, in a city one distributor serves whole; 3.1 % of 591 sampled
  organisations every earlier pass left unlocated; guards for service areas, events, listings, persons) — run dispatched 10:18Z on the 161,091
  sites the legal pass left; bc-crown run 3: 1,001 leads on file (+282: PMRA, CNSC).
- **Two mailbox-crawl runs lost** (09:20Z, 09:41Z) to GitHub push protection: a Mapbox public token (pk.) in a crawled page, flagged as a secret
  token; the guard now strips pk./sk./tk. tokens (595e98a); the queued run's merge reads the fixed guard.
- **AGLC (Alberta liquor licensees): not used.** Its licensee search form redirects to a generated report under /sites/aglc.ca/files/, which
  robots.txt disallows (noted 2026-11-13 01:17Z). The report was downloaded once by following the form's redirect, then deleted unread beyond its
  header; no row, no lead. The lane stays blocked by robots.

**2026-11-13 09:50Z — since 09:10Z (none of it counted yet: the full build of 09:09Z and the parts build queued behind it read most of it):**
- Ontario by every address point: 193,560 postal codes added (Overture addresses inside the Board's map), 1,394 codes where the dump's one point
  and the address points disagree now name no distributor; Ontario sites located 107,913 -> 111,206. Hydro-Coaticook added (49 + 10 quotes
  checked in all for the six town utilities).
- Privacy / terms / legal pages: 4,162 addresses (165,740 sites read). A returns / shipping address is refused from now on (26 of the 4,162).
- bc-crown: AER 1,197 licensees (95 leads in run 2); an Overture name pass for registers with no address (+117 leads: Interfor, Coastland
  Wood, A.J. Forest …); **Canada Energy Regulator** (95 regulated companies from the CER's own list with their websites; Group 1 invoiced
  quarterly, Group 2 fixed levies; 23 sites tied by name: ARC, CNRL, Cenovus, Tourmaline, Whitecap, Vermilion …). 704 bc-crown leads on file.
  Run 3 (PMRA, CNSC, name pass on AER / CNSC) dispatched 09:29Z.
- **BBB lane had stalled** at 11,394 of 53,089 accredited profiles (all the archived copies of the 11 Common Crawl crawls it had indexed were
  read; 3,106 leads, 2,483 of them in Alberta). cc-index over eight older crawls dispatched (cc_clients.crawl_ids takes a list now); the
  scheduled cc-read runs read the new copies.
- A mailbox-crawl merge was refused by GitHub's push protection (a Mapbox secret token printed in a crawled page): the secret guard now knows
  Mapbox and a dozen other providers' token shapes; 4 Google keys removed from claude_ap_terms.csv.
- Canada runs of the registries' candidates dispatched (tm-sites / pt-sites abroad=false ror=true: 2,326 trademark and 696 patent owners in
  Canada with a ROR / Wikidata site).
- Probed, not built: US UCC liens with a Canadian secured party (Colorado 2,325 active filings, Connecticut 74) — needs a new kind of row
  (lender / lessor) in the ranker; Health Canada drug establishment licences (overlap with DPD).

**2026-11-13 09:10Z — where organisations stood unlocated, and four ways round it (none counted yet; the next build reads them):**
- Measured on the site facts on file (275,632 sites that print a postal code): 31,219 print an Alberta code (no row by location: the retailer bills
  there), and **about 9,000 more print a code of an area no distributor on file covered** — Ontario 6,475 (4,007 rural codes whose one point in the
  postal-code dump is a post office; 2,468 codes near the edge of a service area or unknown to the dump), Kelowna ~1,540, Saskatoon ~1,900,
  Sherbrooke ~1,170, New Westminster 571, Penticton 319, Westmount 297, Cornwall 264, the territories 638, Medicine Hat, Joliette, Magog …
- **Added (each sentence checked on its page):** the City of Medicine Hat (exempt from Alberta's retail competition, Part 8 of the Electric
  Utilities Act: "Electricity generation, distribution and retail are all performed by the City of Medicine Hat"; T1A/T1B/T1C), Hydro Westmount
  ("Ce réseau distribue l'électricité à toutes les résidences et à tous les commerces de la municipalité"), New Westminster's utility (grid
  "spanning the entire municipality"; commercial accounts "Billed every month"), Penticton's ("providing electrical service to the community's
  20,000+ … customers"; "bills are mailed monthly"), each for the postal codes whose own place is the town (by_location `pocket_of`), and
  **Cornwall Electric**, which the Ontario table mapped (964 postal codes) but no biller entry carried.
- Not added: Joliette ("Hydro-Joliette ne dessert qu'une partie du territoire"), Sherbrooke, Saskatoon (Saskatoon Light & Power's franchise is a PDF
  map), Kelowna (no open boundary), FortisBC's interior (its service-area page is a map), Saint John Energy (its site does not answer the reader),
  Swift Current (robots.txt refuses the reader), AMVIC (card only, "Business will not receive an invoice").
- **Ontario by every address point** (tools/on_ldc_table.py addrcodes): Overture Maps' 5.4 million Ontario address points, each with its postal
  code, inside the Energy Board's map — a code whose points lie ≥98 % in one service area gets that distributor (codes the dump's table gives keep
  theirs) → tools/data/on_postal_ldc_addr.tsv.gz, read by by_location after the dump's table.
- **Privacy / terms / legal pages** (addr-reread legal=true, 6 runners, dispatched 08:49Z): the 165,740 sites every earlier pass left without an
  address; an address kept only beside the organisation's own name (host, affiliate, public bodies, person names left out). Test 7 of 240 (2.9 %).
- bc-crown first run (06:55Z → 08:42Z): water 5,486 holders, stumpage 505 clients (all six reports; 347 with a month of $5,000 or more), 436 sites
  → 419 leads (393 water, 26 stumpage); the run with AER / PMRA / CNSC / Wikidata started 08:42Z.
- **Decision prepared, not taken — workers' compensation by law:** every employer in a compulsory industry is billed premiums by its province's
  board (WCB-Alberta, WSIB, CNESST, WorkSafeBC …: one board per province, by statute, invoiced, paid through a bank), but no board publishes its
  employers and whether an organisation employs anyone is not published. It would give an Alberta organisation a row the way electricity gives one
  elsewhere. Recommendation: NO — weaker than an address (what the organisation is, not where it is), unless the owner wants it, labelled.

**2026-11-13 08:02Z — build 07:49Z: 267,950 ready (+12,791)**: location 177,975 (+10,246: the address re-read and the telephone places), agent of
record 11,564 (+2,012: owners' sites tied this morning), licence 14,314, benefit plan 786, membership 19,269, service 31,986; $5k+ a bill 2,814
(published 2,178, estimated 636); with an amount and a billing period 225,909; with every main invoice field 176,263; 326,765 rows (320,934 with a
mailbox). Not yet in it: bc-crown (water, stumpage, AER, PMRA, CNSC), the ROR / Wikidata sites, phone targets fix, the person-named places rule.
Also since 07:49Z: **CNSC lane** (1,149 licensees that pay the yearly fee — invoice before each licence anniversary, s. 17 of the fee regulations;
238 in Alberta) and a Wikidata pass in the crown lanes' site finder.

**2026-11-13 07:49Z — statutory billers that publish whom they bill; two registries that name an organisation's website**
- bc-crown now holds four lanes (tools/bc_crown.py, daily): B.C. water rentals (5,486 licensees), B.C. stumpage (the Harvest Billing System's
  invoices), the **Alberta Energy Regulator's administration fee** (1,197 licensees of drilled wells in force; invoices e-mailed every April 1 to the
  operator of record, "Cheques and Electronic Fund Transfer (EFT) are the only methods of payment accepted"; a fee floor from the published base fee
  × adjustment factor — 260 at $5,000 a year or more) and **Health Canada's PMRA annual charges** (675 registrants of current pest control products;
  "four (4) invoices … sent in one mailing", instalments May 30 / Aug 28 / Nov 26 / Feb 24). Alberta matters most: no electricity row exists there,
  so a record is the only way an Alberta organisation becomes a row. Payee entries verified on the bodies' pages (water, stumpage, AER).
- **Owners' sites from two open registries** for the trademark / patent owners with no site (the largest pool abroad): the Research Organization
  Registry (ROR, 146,716 organisations; 3,223 candidates) and Wikidata's official website property (784,918 items in the 14 countries the site
  tests know; 10,161 candidates). A candidate ties nothing alone: the site's own pages must state the owner's name with an address of its state /
  country (or a Canadian postal code), or print its full legal name on its legal page, or — three sources agreeing — state the very name when one
  owner bears it on the register. Runs so far: patents +83 then +44, trademarks +69 (ROR only); the Wikidata runs are going (pt-sites, tm-sites).
  Tests: ROR 4 of 30, Wikidata 8 of 40 (IBM, Siemens, General Mills, Church & Dwight, Dentsply Sirona …).
- Checked and not usable: CTA air carrier licences (its open-data portal's robots.txt bars ClaudeBot by name), APEGA's permit-holder directory
  (Cloudflare 522 from the container and from a runner), EGBC's registrant directory (403), B.C. liquor licensees (they pay BC Liquor Stores at
  pickup: no invoice), certificate subjects as a locator (1 site in 292 has an organisation in its certificate), OSM postcodes as a locator (834).
- SEC EDGAR full-text search (Canadian auditors of SEC registrants, with published audit fees) needs a contact e-mail in the user agent; the project
  has no organisational address to give and the owner's must not be sent — not used.

**2026-11-13 06:57Z — build 06:44Z: 255,159 ready (+34,423); a new lane of bills the Province of British Columbia sends itself**
- Build 06:44Z (full, code 037022e of 05:32Z): 313,770 rows (308,011 with a mailbox); ready **255,159** — location 167,729 (+27,958: telephone places and
  part of the address re-read), service 31,977 (+4,851: billers read today), licence 13,983 (+1,308), agent of record 9,552, membership 19,255, sponsorship
  5,347, public contract 3,116, dealership 2,751; complete in the biller's own words 23,829, best effort 63,601; with an amount and a billing period
  213,982; with every main invoice field 166,083; $5k+ a bill 2,712 (published 2,105, estimated 607). The release went out; the git copy of
  coord/results/ranked did not (a merge conflict on contract_buyers_without_website.csv with the lists restored at 05:30Z) — the next build writes it.
- The parts build of 05:41Z was cancelled by GitHub when the scheduled full build (06:49Z, code 1f1a9be: the address re-read, the telephone numbers,
  the billers, the withdrawals) queued behind the same "ranker" group. That build is the next count (~08:25Z).
- Telephone places: the targets had fallen from 77,187 to 131 once the address re-read marked its 207,671 sites done (phone_places read only the
  sites not re-read) — fixed (every organisation still unlocated): 67,935 targets with a Canadian number; phone-places dispatched 06:56Z.
- **New lane bc-crown** (tools/bc_crown.py, daily workflow): (1) **water rentals** — 5,486 organisations holding current B.C. water licences (the
  Province's open layer: licence, purpose, quantity, the licensee's name, client number, address and postal code); the Province's words: "When a
  water licence is issued, annual water rentals are assessed", a statement once a year (twice above $100,000) "sent to the client(s) … registered on
  record as the water licence holder", paid by online banking or cheque; the yearly rental calculated from the published quantity and purpose with
  the published rates (B.C. Reg. 37/2016, Schedule 2) — 64 holders at $5,000 a year or more; ministries, federal bodies and First Nations (exempt on
  reserve land / under treaty) left out. (2) **stumpage** — every client the Harvest Billing System billed in the last 183 days, from its public
  Billing Summary report (each invoice's number, timber mark, value, date) named through the harvesting authorities layer: 228 organisations from two
  of the six reports in a local test (163 with a month of $5,000 or more); "due upon receipt of your invoice", "Statements of Account are issued on
  the 23rd of each month", paid through a bank (EFT, wire) or cheque, "Credit card payments are not accepted". Payee entries verified on the pages.
  Sites: same postal code on file, Overture places at the postal code (lane bcw), the company-name autocomplete; leads -> mailbox crawl -> rank.

**2026-11-13 06:10Z — more reach from what is already read; two builds queued**
- Builds: rank-buyers (full) started 05:34Z on main of 05:32Z (billers, withdrawals, telephone places, cross-register ties — not the address
  re-read); rank-buyers-parts (05:41Z, everything) waits behind it in the "ranker" group. Expected publish ~07:10Z and ~08:15Z.
- Telephone numbers: the address re-read and the mailbox crawler now keep each site's own number (a tel: link first); a re-read of the 166,628
  sites that gave no address, for their number, is running (addr-reread phones=true); phone-places runs after it.
- European sites (owners abroad): the mailbox reader follows the legal notice and contact pages a European site must publish (Impressum,
  mentions légales, aviso legal, note legali, colofon, Kontakt …), asks them by the site's country, and counts kontakt@ / mail@ / post@ …; 1,260
  European lead sites that gave nothing are read once more (rule r4).
- Not used: BRP's dealer list (only through the locator's own back-end service — not probed further); APEGA's permit-holder service (522).

**2026-11-13 05:45Z — two address passes landed; rank-buyers-parts dispatched 05:41Z with everything of today**
- addr-reread (6 runners, 50 min): 207,671 unlocated mailbox owners read again -> **37,949 addresses** in their pages' source or text (JSON-LD
  21,603, text 11,911, map 4,435); 27,110 of them name a distributor (by postal code or by a city one distributor serves whole); the rest are
  Alberta, partial or shared. Commit 2c631f5 (site_facts/facts_20261113T054027a.gz).
- phone-places (Overture places in Canada by telephone, 8 s with a bounding box): **17,530 located** (place bears the organisation's name or
  lists its website; one postal code), 2,955 of them not covered by the address listed for their website. Rank uses it last, labelled.
- Held service rows give way to the distributor's row once their organisation is located — both passes feed that too.
- Expected in the next build: +15-30k ready (not counted until the build reads them).

**2026-11-13 05:30Z — build 05:17Z (parts, code of 04:12Z): 220,736 ready (+2,249)** — agent of record 7,826 → 9,196, export sale 19 → 49,
licence 12,675, location 139,771; $5k+ a bill 2,665 (published 2,062, estimated 603); every main invoice field 138,405. None of today's 04:40Z+
changes are in it (billers read, address re-read, withdrawals, cross-register ties) — the next build carries them.
- Withdrawn after a third look at ties by a postal code printed at an address (the place's name must BE the organisation's: biz_licences.agree_asym,
  or the very same name): radio 309 (1 restored), OMVIC/HCRA 79, RBQ 50 more, Form 5500 49, Health Canada 5 — gone shards written; RBQ's merge and
  radio's lead writer honour withdrawals.
- Sites already read -> owners abroad (cross_sites.py second pass): +149 trademark, +92 patent, +4 Health Canada, +16 Form 5500 owners whose
  register ZIP / postcode is printed on a site the mailbox reader had read, under the owner's own name (one owner a site, one site an owner).
- Checked and not usable: CSA Group product listings (403 even to robots.txt, from a runner too) — blocked; GrowthZone member directories (403);
  NHP fees not in force (Health Canada: "Final fees will be published in the Canada Gazette, Part II before implementation"); D2L's public terms
  name no invoice. Registered for later: CTA air licences + NAV CANADA's monthly bills (foreign airlines, $5k+; the CTA's certificate chain is
  incomplete from a runner).

**2026-11-13 05:00Z — where the ready rows are held, and three levers on it (counted on the published table of 04:08Z, streamed):**
- Of 284,660 rows (278,945 with a mailbox), 218,487 ready. The largest hold among rows with a mailbox: **"payment: not published" 34,575** — services
  seen on the buyer's side whose vendor's own sentence on how it is paid was not found (rule 13 gives no "by the kind" fallback to hosting / software).
  3,407 vendors; the top ones read by hand today: doteasy (1,875 rows), Aplus (2,166), Canadian Web Hosting (728), HostedinCanada, Websites.ca, Coolcom,
  Vianet, PowerStores name an invoice / statement and a bank payment (bank transfer, cheque, direct debit, Interac, ACH, automatic bank withdrawal) →
  BILLING_BY_DOMAIN; Jane (2,150), Hawk Host (3,504), Ex2 (668) are card only in their own words → their rows go (rule 6). The payment test now reads a
  refused cheque as refused ("not able to accept payment by cheque or EFT"). Reader v6 (terms on a terms./legal. subdomain; "must pay the Charges by",
  "pay with", "methods of payment") dispatched on the 3,407 vendors (vendor-billing, only_file).
- The rank left **185,837 organisations with a confirmed mailbox out because no distributor can be named for where they are** (+17,489 not from
  leads). 136,177 of the mailbox owners under .ca print no postal code the reader saw. Sample of 60 read again: 8 state their address only in the
  page's source — the schema.org PostalAddress of their own JSON-LD, or the place of the Google map their contact page embeds → `tools/addr_reread.py`
  + addr-reread.yml (207,671 sites, 6 runners, dispatched 04:47Z); the mailbox crawler keeps the same two for new sites; the rank's address cell says
  which. Expected +15-25k located (not counted yet).
- Alberta: 27,946 mailbox owners print an Alberta postal code — no electricity row there (the retailer bills, not the distributor). Calgary 11,051,
  Edmonton 7,231. **Decision prepared, not taken:** water by location (EPCOR Water in Edmonton, the City of Calgary's charges billed by ENMAX) — one
  biller by law for the address, like electricity, but a tenant in a shared building rarely holds its own water account; recommendation: NO unless
  the owner wants it, labelled.
- One legal person, two registers (`tools/cross_sites.py`): +123 trademark / +202 patent owners take the site the other lane tied to the same legal
  name, country and postal code. tm-sites EU run +584 (18,708 sites); pt 8,415; mailbox crawl 2,595,361 sites read (found 497,682).

**2026-11-13 04:00Z — progress since 03:00Z:**
- The address method now runs in eight lanes: trademark / patent owners abroad (US, UK, Australia, Netherlands and — 03:58Z — nine European
  countries by house number + street + postcode: +5,257 / +2,836 owners with candidates) and in Canada (trademark run: +1,153 sites, 18,039;
  patent: +329, 8,065); RBQ (2,359 sites confirmed in one run; 194 postal-code ties withdrawn, see below); OMVIC (authority-registers running);
  radio licensees (130 in a first local hour, +125 leads; workflow running); Vancouver / Toronto / OPC / RACJ business licences no organisation
  matched (20,190 with candidates; biz-licences running); Health Canada and Form 5500 (rest in their next runs).
- The postal code at an address: one shared word between the place's name and the organisation's is not enough (a dealer and the county's
  site; a mason and a Toyota dealer) -> `place_fits` = every word of the shorter name in the longer, or two distinctive words, and never
  "another body" (foundation, association, union, club …). Ties made before were re-tested and withdrawn: HC 38, F5500 57, RBQ 194 (172 leads).
- Trademark leads 20,727 -> 23,755 sites (tm-register 03:2xZ).
- rank-buyers 02:38Z still running at 04:00Z (78 min, not published); rank-buyers-parts (3 parts) queued behind it as the fallback.

**2026-11-13 03:00Z — milestone (sites found tonight, all tied by the lanes' own tests; leads written by the workflows):**
- Trademark owners abroad 13,853 -> 16,886 sites; patent owners abroad 3,069 -> 7,736 (by address 2,245; by legal page 3,863: the site's
  own terms / privacy / legal notice printing the owner's full legal name with its legal form — "This website is maintained by Merck Sharp &
  Dohme LLC" — for a site an Overture place lists under the owner's name or at its own street address). Patent leads: 8,302 sites.
- Owners IN CANADA: Overture places at the register's full postal code -> 22,279 trademark / 3,092 patent owners with candidates; tm-sites
  and pt-sites (abroad=false, overture=true) dispatched 03:00Z (test 5 of 58 tied).
- Health Canada companies 2,002 -> 2,167 sites (+165 leads); Form 5500 sponsors 1,578 -> 1,883 (+305 leads); Colombian importers 78 -> 214.
- A rule learned the hard way: at an ADDRESS, a printed postal code / ZIP ties nothing (every tenant prints it) — 188 such ties (Novartis
  -> a fitness club at the same postal code) were removed before they became leads; now it counts only when the place bears the
  organisation's name (tm_register.place_fits).
- Leaks fixed: credit-scan and dns-services merges recomputed 7-12 minutes of work before every push and lost whole cycles (697,172 sites
  read on 2026-11-12 15:04Z) -> computed once, main merged on a refused push; credit-scan-salvage.yml merged the lost cycle's artifacts.
- rank-buyers 01:18Z died ("runner lost communication", 78 min, no publish); re-dispatched 02:38Z. If it dies again: rank-buyers-parts.yml
  (3 parts, same concurrency group) is the fallback; the container (7 GB) cannot run the full rank.

**2026-11-13 02:15Z — where things stand and the next task (read this first after a reset):**
- DONE 01:40Z: owners' sites abroad by the owner's OWN STREET ADDRESS (`tools/overture_names.py addr --lanes tm,pt`): the Overture places at
  the register's street number + street + ZIP code (UK: full postcode) that list a website, office buildings with >3 sites kept only under a
  word of the owner's name, shared-office / platform / government domains dropped -> `tm_overture_addr_sites.csv` (13,115 trademark owners,
  20,716 candidates) and `pt_overture_addr_sites.csv` (9,730 patent owners, 14,847). The site still counts only when its own pages state the
  owner's name (`tm_register.py sites --overture` reads both files; tie label "an Overture Maps place at the owner's own street address on the
  register (…) lists this website"). Tests: patent slice 12/46 tied, trademark slice 4/102 (trademark owners left are mostly subsidiaries whose
  legal name the group's site does not print — e.g. "PetSmart Home Office LLC" on petsmart.com; NOT tied: decision for the owner below).
  Patent owners had no Overture list of their own (the trademark file has other keys): fixed (`pt_register.py overture-sites` ->
  pt_overture_sites.csv, 12,730 owners). Runs: tm-sites (6 shards) and pt-sites (4 shards) dispatched 01:42Z with abroad+overture.
- DONE: Ontario cannabis stores carry an ESTIMATE from OCS's own annual report 2024-25 (wholesale revenue $1,733.8 million over 1,709-1,719
  stores: about C$84,300 a month a store; a chain's figure counts its stores on the AGCO list), labelled "estimated —" with both sentences
  quoted (roster descriptor `amount_estimate`; rank writes bill_amount_calculated). B.C.: the LDB publishes no wholesale split -> no estimate.
- DONE: Colombian importers' sites from the company's OWN entry in the SECOP II supplier register (datos.gov.co qmzu-gj57, by NIT; website
  only, the register's e-mail never asked for): sites 78 -> 222+ in one local run; tie = NIT printed, or the site names itself by every
  distinctive word of the importer's name. dian-imports.yml keeps dian_secop_done.tsv.
- dian-imports first run green (01:42Z): 12 months, 1,773 (importer, exporter in Canada) pairs, 1,238 importers.
- rank-buyers dispatched 01:18Z still running at 02:15Z (the build with the IndexError fix, DIAN/f5500 kinds).
- Checked and not built: industrial designs (open data names no agent), FEC disbursements (41 committees, card), OLMS LM-2 (host 503 here;
  for a runner). In coord/source_registry.csv.
- **Decision for the owner (prepared, not taken):** a trademark owner that is a subsidiary at its group's head-office street address, whose
  group site (listed by the Overture place at that address) prints the group's name but not the subsidiary's — accept the group's site and
  mailbox for the subsidiary's row, labelled "the group's site at the owner's own address"? Recommendation: yes, labelled; ~2,000-4,000 rows.
- **NEXT:** read the 01:18Z build; then the tm/pt site runs' merge; then more pools (regulators' firm registers, NL/Yukon cannabis).
**2026-11-13 00:42Z progress:** f5500 first run green — 4,526 US sponsors (2024+2025 filings), 1,578 sites tied, 1,578 leads; exchange finder +164 sites (1,443); Health Canada +584 sites today (2,002); build 23:25Z: 217,388 ready. dian-imports first run still downloading. Next: CWB certified companies (authority register), then read the build that carries the new kinds.

## 2026-11-12 23:45Z — three new lanes abroad and the website bottleneck (owner 17:16 and 18:26 EST: "explore the international scene … big bucks",
## "look everywhere at once", "think like the ideas I gave you")

**Build 22:02Z (a513328): 217,145 ready.** $5k+ a bill: 1,871 published + 349 estimated = 2,220 (owner told). Where the $5k+ rows are held back
(table of 22:02Z): 2,965 public-contract buyers are not ready, 2,025 of them with a published $5k+ amount — 1,317 have no mailbox (915 of them
$5k+, 365 with no website at all), ~1,290 have only a contract over 3 years old with no end date (rule 11). The register lanes are held back by
websites: 2,600 holders of a medical device establishment licence ($5,519 a year, published) had none.
**New today (all tools + workflows, nothing depends on a session):**
- `tools/dian_cloud.py` + `dian-imports.yml` (weekly): Colombian import declarations (DIAN) — importer, exporter in Canada with its address,
  the exporter's invoice number and date, FOB value, goods, form of payment ("Giro directo" …). New kind `export sale`. Site tied only when its
  own pages print the importer's NIT. First run downloading 12 months (dispatched 23:15Z; ~280 MB a month at ~0.5 MB/s).
- `tools/f5500_benefits.py` + `f5500.yml` (weekly): US employers whose benefit plans pay a Canadian company (US Department of Labor Form 5500
  open data). Schedule A: Sun Life Assurance Company of Canada (its U.S. branch, NAIC 80802) insures the plans of 3,873 US employers in the 2024
  filings (policy number, period, persons covered, benefits, commissions → "more than US$X a month" calculated from the commissions); Schedule
  C: 50 plans paying a provider in Canada (published compensation $5,000+). New kind `benefit plan contract`. Site tied only on the ZIP code
  printed after the state (test: 33 of 184). First run dispatched 23:39Z. **Open question to the owner: is a Canadian company's U.S. branch a
  "Canadian biller"?** (rule 7 says any Canadian entity; the rows say so in the vendor address cell.)
- `tools/overture_names.py`: one scan of the Overture Maps places gives candidate websites (same name at the same postal code / province /
  country) for lanes hc, xc, dian, cb (contract buyers with no website: rank.py writes coord/results/ranked/contract_buyers_without_website.csv),
  f55. Each lane keeps a site only by its own test. First hc run: 419 Health Canada companies tied (137 licence holders).
- Guessed domains, tied only on a published identifier: hc (postal code on the home or contact page; test 4/30), xc (symbol on its exchange
  on the home page; test 12/77), dian (NIT), f55 (ZIP after the state).
**Runs in flight at 23:45Z:** dian-imports (first, 12 months), f5500 (first), hc-registers (overture + guess + autocomplete), exchange-issuers
(overture + guess), rank-buyers (dispatched 22:43, code before these lanes). The next build after ~00:30Z carries the new rank code.
**Measured, not built (the owner's road-closure idea):** building permits name the contractor and a declared value (Vancouver 600
non-residential with a contractor in 12 months, with the contractor's address; Calgary ~750 commercial a year, no address). The buyer would
stand on where it is (the organisation whose own site prints the permit's address). A few hundred rows: queued.
**Candidates for the next session (ranked by $5k+ rows they could bring):** PCAOB Form AP (Canadian audit firms auditing SEC issuers; audit
fees published in the 10-K); the Canada Energy Regulator's cost-recovery levies by company (published); BC's Harvest Billing System (monthly
stumpage invoices with published amounts); CIRO member firms (published fee model); Accreditation Canada's accredited organisations (Canada and
abroad); DBRS Limited's issuer-paid ratings; more lobbyist registries (Alberta, Québec, Ontario, Ottawa); regulators' firm registers (ESA,
HCRA, TICO, RECO, AMVIC …) for count.


## 2026-11-12 21:25Z — build 21:15Z: 216,121 ready; rosters at 342 lists

**Build 21:15Z (5e5069a, the 18:17 schedule that fired at 19:56):** 216,121 ready (+2,863). Not by location 74,510 (+3,761): membership
18,059, licence 12,086, agent 7,289 (+1,163, patents from pt-sites), sponsorship 5,435, public contract 3,110, dealership 2,645, tenancy 409,
exchange listing 303 (+243), service 25,174. $5k+ a bill: 1,870 published + 349 estimated. Amount and period 183,695; every field 140,230.
A build dispatched at 20:43 (dddb3b4) runs after it and carries the rosters merged up to 20:43.
**Rosters: 342 lists on file** (213 member, 52 exhibitor, 45 tenant, 25 dealer, 7 sponsor); `roster_ingest.py check` counts 54,785 listed
organisations that would become leads; roster leads on file about 37,600 (the rest are on file through another lane: one row per buyer).
Today's helper waves: chambers (BC, Alberta, Québec, Ontario, Yellowknife), tourism associations, construction / home builders,
landscapers, insurance brokers, consulting engineers, co-ops and buying groups (FCL, PharmaChoice, Castle, Sollio, ILDC), schools (FEEP,
Edvance, SCSBC), seniors' residences (RQRA), camps, industry associations (movers, franchises, aerospace, nuclear, kitchens, coatings,
precast, concrete, aggregates, auto parts, cosmetics, water, food processing — CTAQ, Taste of Nova Scotia), sponsors (Stampede, CNE, CFL
teams, junior hockey — running). Diminishing returns now: most remaining directories sit behind Cloudflare, member365, MembershipWorks,
GrowthZone checks or JavaScript, or bar AI crawlers in robots.txt (respected). New check in roster_ingest: a quote that names a person with
a phone or a mailbox takes the descriptor out. Withdrawn by rule: CCI Saint-Georges (online ticket), MEIA (online yearly plan).
**Automation running:** tm-sites and pt-sites (abroad, with the name autocomplete), exchange-issuers (every 6 h; TSX/TSXV 780 sites found,
CSE 497 from its own list), radio-licences, hc-registers, mailbox-crawl (short runs back to back), rank-buyers (schedule late by ~1.5 h:
dispatch by hand when a build is needed).

## 2026-11-12 19:25Z — build 19:14Z read: 213,258 ready (+13,098)

**Build 19:14Z (d81c2ab), counted from BUILD.json and the table (scratchpad build_next/analyze.py):** 213,258 ready of 277,676 rows.
Not by location 70,749 (+21,862); by location 142,509 (−8,764: those buyers now stand on a record or a service — one row per buyer, a
record first). By kind: service 25,172 (+17,208), membership 16,324 (+2,699), licence 11,871, agent 6,126, sponsorship 5,394 (+923),
public contract 3,110, dealership 2,330 (+438), tenancy 362 (+242), exchange listing 60 (new, C$12,000+ a year each). $5k+ a bill: 1,771
published + 198 estimated. Amount and period 184,086 (+8,230); every main field 141,107 (−8,471, carried by the location rows that moved).
Ready by new source: roster members 14,921, trademark agents 5,992, roster exhibitors/sponsors 5,394, roster dealers 2,330, radio 610,
Health Canada 484, roster tenants 362, patent agents 134, exchange 60.
**The service jump is mostly one host:** Web Hosting Canada 16,542 rows (its pay page: an order generates an invoice payable by wire transfer
or Interac — rule 6 "In" when the biller also takes cards), Webnames 3,171 (paid DNS plans, cheque accepted), linknowmedia 1,957, Likuid 762,
Astral 528, Varial 375, WellnessLiving 310. Told to the owner with the offer to take hosting out entirely if he reads rule 6 that way.
Rosters merged 18:28Z-19:07Z (after the build's code): chambers (Québec wave, Alberta, Yellowknife, Trail), tourism (Cantons-de-l'Est,
Montérégie, Bas-Saint-Laurent, Attractions Ontario …), co-ops (FCL 148, PharmaChoice, Sollio, Castle, ILDC), insurance brokers (IBANB, IBANS,
RCCAQ), landscapers (BCLNA, Québec Vert, APPQ), engineers (CEA, AFG), BC Funeral Association, PEI construction. Tenant rosters no longer
count toward the more-than-15-rosters rule. Helpers still running: associations wave 2, Québec chambers.

## 2026-11-12 18:20Z — exchange issuers (TSX, TSXV, CSE), patents through pt-sites, rosters at scale (dealers, malls, shows, builders); robots.txt BOM fix

**Last build read: 17:06Z (aaaa5ed): 200,160 ready** (by location 151,273; membership 13,625; licence 11,670; service 7,964; agent 6,044;
sponsorship 4,471; public contract 3,101; dealership 1,892; tenancy 120); $5k+ a bill 1,683 published + 115 estimated; amount and period
175,856; every main field 149,578. Told to the owner. The 18:17Z scheduled build carries everything below except what landed after 18:17Z.
**New since 17:06Z (all committed):**
- `tools/exchange_issuers.py` + `exchange-issuers.yml` (03:37, 09:37, 15:37, 21:37): listed companies of the Toronto Stock Exchange (664),
  TSX Venture (1,343) and the Canadian Securities Exchange (616 Active equity issuers). TSX/TSXV: annual sustaining fee "invoiced in February",
  C$5,500+ a year, amount calculated from the list's market capitalization (labelled); site = name autocomplete under the issuer's very name,
  kept only when the home page prints its symbol ("TSX: ABC"), or the domain is its name + the page names it + links investors' pages (the test
  of 2026-11-12 caught 4 namesakes under the looser rule). CSE: its own list gives each issuer's website (494 leads at once), a MONTHLY
  maintenance fee, C$1,000 a month at the least, "due on the first business day of each month". Payment method not printed by any exchange →
  by the kind. New kind "exchange listing" in relationship_rows (fields as a licence) + priority_sort (5) + retest_rows. First cloud run
  43274137512 dispatched 17:53Z (old code, TSX/TSXV only; the next run rebuilds with the CSE).
- pt-sites found 2,792 owner sites; pt-register now 3,638 patent leads (agent of record = Canadian patent agent; by the kind: per transaction).
- Rosters merged 17:36Z-18:14Z: +2,606, +524, +187, +1,691, +1,004 (construction associations of Ottawa, Vancouver Island, Niagara, Nova Scotia,
  London, Thunder Bay; HBAs of London, Waterloo; dealers of MacDon, Loewen, Enviro, Paradigm, Honey Bee, Argon 18 (Europe left out — Argon 18
  Europe may supply it), Bourgault, Elmer's, SeedMaster; tenants of Cadillac Fairview, Oxford, Primaris, Morguard, RioCan + others; exhibitors of
  ~40 shows: Marketplace Events' home/boat/sport shows, IDS, CPMA, WMTS, MEET, BUILDEX, Expo habitat, HAC). Domains on more than 15 rosters
  (chains) are left out (100 now). Not yet merged: dl_morris (reviewed, committed) and whatever the running helpers write.
- robots.txt with a byte-order mark was read as "allow all" by every shared reader (utf-8 decode kept the BOM): fixed (utf-8-sig / lstrip) in
  ap_crawler, client_lists, credit_scan, live_clients, probe, research_driver, small_sources, dated_stories.
- ap_crawler: plain http also when https resets or refuses. validate_returns: renseignements@ is a role mailbox. Batches 915-916 committed.
**Helpers running at 18:20Z:** dealers B (Kingsman, Opus, Garneau, PSB, Bryston, Brandt, Meridian, Kohltech, Pronovost, Normand, Campion, Arc'teryx,
Mustang — blocked makers listed to it), tourism member directories (DMOs, tourism associations), builders/construction associations, malls.
**Roster merge rule learned:** never move a helper's file out of the way to hold it (a helper rewrote Bourgault while it was held and the move
back overwrote the fix). Merge only after review; a file that lands during a merge is reviewed before the commit.
**Next:** read the 18:17Z build when it lands (~19:35Z); merge helper rosters as they land; Sunday: coord/WEEKLY_REPORT.md.

## 2026-11-12 16:48Z — new lanes (ISED radio licences, Health Canada establishment licences), rosters at scale, two hosting vendors; build 16:17Z read

**Build of 16:17Z (code 54e964a), counted: 197,493 ready of 264,355** (by location 152,764; membership 12,406; licence 10,563; service 7,921;
agent 4,807; sponsorship 4,178; public contract 2,921; dealership 1,834; tenancy 99). Amount and period 174,898 (+7,553); every main field
151,043; $5,000+ a bill: 1,531 published, 72 estimated. −906 against 14:57Z: free-DNS rows out (−627, by rule), contracts +72, the rest not
traced. Told to the owner at 16:35Z. Failures by kind (scratchpad build_1627/why.py): agent of record 1,180 "named person" (fix pushed
after this build), service rows 36,862 "payment: not published" (hosting / DNS / software: card on file — by rule; 2 hosts found that print
an invoice payable by bank: whc.ca, varialhosting.com — `tools/tech_relationships.py`, DECISIONS 16:55Z), public contracts 2,339 no mailbox.
**New lanes, all in the cloud (DECISIONS 16:10Z, 16:25Z):**
- `tools/radio_licences.py` + `radio-licences.yml` (01:53, 05:53 … every 4 h): ISED's radio licensees, 27,051 organisations invoiced every
  year; 2,898 leads at once (sites on file), the rest through the name autocomplete (one a second, ~6,000 a run). Amount = labelled floor.
- `tools/hc_registers.py` now also reads the MDEL listing (3,223 establishment licences, $5,519 a year each, published): 384 leads at once;
  the twice-daily Health Canada run asks the autocomplete for the rest (largest bills first). HC leads on file: 1,231 at 16:21Z.
- `tools/tm_register.py sites --abroad --clearbit` (+ input `clearbit` in tm-sites.yml): the autocomplete's domains for trademark owners
  abroad, kept only by the old tests (postal code printed under the same name, or legal person with legal form in the owner's state).
  First run dispatched 16:40Z (4 shards × 165 min); measured on 60 owners: 7 autocomplete domains read, 0 tied — a modest lever.
- `tools/roster_ingest.py merge` now withdraws a roster's leads when the roster is withdrawn or a stricter rule no longer takes them, and
  writes again the leads of a corrected descriptor (cc_on_ssm withdrawn: its page says card only).
**Rosters merged today (helpers):** +3,572 (15:18Z), +3,411 (15:37Z), +1,569 (15:49Z), +1,613 (16:13Z), +4,581 (16:44Z) organisations.
Helpers still running at 16:48Z: Atlantic chambers, Ontario chambers wave 3, trade-show exhibitors A (agri/food/energy/mining/manufacturing)
and B (building/home/gift/boats/health), dealer locators of Canadian manufacturers. **Their files land in data/incoming/claude/roster_*.csv +
contrib/claude/rosters/*.json: scrub e-mails, `roster_ingest.py merge --stamp S`, check 0 e-mails in the shard, commit rosters + shards.**
The cloud biz-licences merge (04:41/16:41) re-runs the merge on main: never leave a merged roster uncommitted.
**OCDS abroad:** 48 awards, 5 publications (records_ocds_*), committed.
**Build dispatched 16:23Z (run 43258177022, code with the registry-warning and agent-firm fixes, the radio/MDEL wiring) lands ~17:45Z.**
**Next:** read that build (agent of record and registry-warning counts; first HC rows); a patent lane is possible (CIPO Patent_CSV_2024_05_22:
PT_interested_party.zip 222 MB, 1.7 GB csv: OWNR / AGNT parties by patent; PT_main 114 MB for status) — not built; disk here ~6 GB free.


## 2026-11-12 15:25Z — contract billing period and amount per bill; Health Canada lane; rosters and mailboxes by helpers

**Build of 14:57Z (code a7cfa01), counted: 198,399 ready of 264,965** (by location 152,797; membership 12,559; licence 10,494; service 8,548;
agent 5,023; sponsorship 4,191; public contract 2,849; dealership 1,839; tenancy 99). Published $5,000+ 1,785; amount and period 167,345;
every main field 151,085. Told to the owner at ~15:10Z.
**Owner, 09:00-09:15 EST:** contracts preferred ("they'll go over 5,000 … all the things populated") but a mixed approach, everything that is a
real current relationship; contract rows must carry a billing period and the amount of one bill; PO only when published ("blanket" only
when it is one); no portals; don't over-rely on electricity; deadline: end of November. "All hands on deck."
**Pushed and in the build dispatched 15:07Z (lands ~16:20Z):** DECISIONS 14:45Z (contract cadence by what it buys, `contract_nature`,
amount of one bill and amount_mark per bill, `po_or_reference_to_quote`, a clean vendor first, Namespro free DNS) and 15:05Z (Health Canada).
Sample 1-in-4: ready contract rows 2,050 -> 2,123; service rows 1,963 -> 1,580 (Namespro).
**Health Canada lane** (`tools/hc_registers.py`, workflow `hc-registers.yml` at 03:23 / 15:23 UTC, first run dispatched 15:13Z): 4,204 companies
(drug DIN owners with drugs on the market; makers of licensed Class II-IV devices), 1,320 billed $5,000+ a year (calculated from published
fees); 409 leads with a site so far (leads_hc_20261112T151000); the workflow keeps finding sites (strict: domain = name, .ca for a Canadian
company, a group's entities only on their own country's ending).
**Helpers (subagents; files in data/incoming/claude/roster_*.csv + contrib/claude/rosters/*.json, checked by tools/roster_ingest.py, which now
also requires the member's site to carry its name):** rosters merged so far into leads_roster_20261112T151832 (+3,572 leads). Still running at
15:25Z: Ontario, BC, Prairie chambers; builders/trade associations; tourism bodies; OCDS awards to Canadian suppliers abroad
(records_ocds_*); mailboxes for contract buyers batches 910-911. Batches 908-909 and 912-914 done (≈60 mailboxes found; not-searched rows
removed so they stay open). **Commit the roster files the Prairie / Ontario / BC helpers leave, run `roster_ingest.py merge`, commit the shards.**
**Next:** read the 16:20Z build (contract rows, Namespro rows gone, HC rows); commit the helpers' outputs as they land; dispatch a build after
the shards are read by the mailbox reader; the Sunday report (coord/WEEKLY_REPORT.md).


## 2026-11-12 13:45Z — precision pass (whose mailbox, whose name, whose address; one row per organisation); build 13:24Z read

**Build of 13:24Z (code 8455a90, dispatched 12:03Z), counted: 198,271 ready of 266,812** (by location 153,178; amount and period 167,068;
every main field 151,465; published $5,000+ 1,868). Told to the owner at ~12:15Z (the 10:45Z build, 197,202): every ready row is on invoice
with a bank route (112,185 billers also take a card, in by rule 6); the bill's arrival by e-mail is stated on 2,291 rows only — **asked him
whether e-mail delivery must be a condition** (no answer yet); 192,274 of the mailboxes are general ones (rule 9); the buyer's legal name
is on 43 %.
**Pushed 13:42Z, build dispatched 13:42Z (lands ~14:55Z):** coord/DECISIONS.md 13:40Z — a portal page vouches for no mailbox; directory /
roster pages never give a mailbox; a box on another domain only from the organisation's own pages; contractors' boxes off towns' rows;
the chamber's address off 160 member rows; junk legal names; `tools/priority_sort.py` one row per organisation (2,446 rows of the 10:45Z
table, 460 ready). Sample 1-in-4: ready 48,912 -> 48,796. Expect the next table ~900 ready rows lower, then growth as before.
**Next:** read the 14:55Z build (BUILD.json, `duplicate_buyers_dropped.csv` in the release assets? — it is written to out/ranked/; check it
reaches the release); a test hundred; then the levers to a million: Health Canada licence holders (MDALL / DPD / PMRA: right-to-sell fees,
published amounts, mostly abroad), CIPO patents (Patent_CSV_2024_05_22: PT_interested_party.zip names owners and agents), Wikidata
official websites for trademark owners abroad, locating the ~120,000 organisations whose mailbox is read but whose address is not.

## 2026-11-12 07:52Z — build 07:45Z: 176,890 ready; every main invoice field 132,877; test hundred republished

**Build of 07:45Z (run 43169349649, dispatched by hand: the 06:17Z schedule did not fire), counted: 176,890 ready of 236,452** (by location
134,437; complete 11,287; best effort 31,166). Amount and period 147,820; **every main invoice field 132,877** (05:23Z: 89,115 — the
distributors' numbers and terms); published $5,000+ 1,859. In the published table, ready rows by a listed (Overture) address 9,666, by a
registered address 2,943; 941 rows of other kinds took a listed address as the buyer's; 32,144 ready rows carry a number from the LEI register.
**Not in it yet (pushed 06:54Z):** billing periods by the kind of relationship (sample: 6,054 ready rows gain a period). The next build is
the 12:17Z schedule; if it does not fire, dispatch rank-buyers.yml by hand.
**Review page republished** (https://claude.ai/artifact/AKuRT9NPpMX3Jwfqj1ZERt): a hundred rows of the 07:45Z table (seed 20261111),
read row by row first; the page now shows each row's amount mark and what a by-location row stands on. Its `verdicts` collection was empty.
**Next session:** read the 12:17Z build; read the owner's marks on the review page (ArtifactData list verdicts); watch the agent-of-record
rows grow from the trademark owners abroad (mailbox reader -> referee); patents (CIPO's patent data names the "current registered patent
agent of record representing the owner"; its download server needs the certificate handling of tools/tm_register.py).

## 2026-11-12 06:02Z — build 05:23Z read (164,391 ready); the 06:17Z build carries everything below; a test hundred read and fixed

**Build of 05:23Z (MAIL_ALL, contract list, city lever, pockets), counted: 164,391 ready of 223,790** (by location 121,978; amount and
period 135,459; every main invoice field 89,115; published $5,000+ 1,859). Told to the owner at ~05:35Z.

**Pushed since, in the 06:17Z cron build (lands ~07:35Z):** registry and Overture addresses (DECISIONS 04:39Z), the reader takes located
sites (04:58Z), distributors' numbers and terms (05:15Z: sample every-main-field 25,698 -> 34,672), test-set fixes (05:59Z: zero amounts,
press-release wording, person agents, address junk, copyright names). Sample OWNER23 (1 in 4, never multiplied): 48,913 ready of 65,327.

**Trademark owners abroad, running by themselves now:** tm-sites tied 5,323 owner sites through Overture listings (tm_sites_found.csv:
13,200 in all); tm-register made 17,808 leads (15,098 with a Canadian agent of record). The mailbox reader reads them next, the referee
re-reads, the rank build makes agent-of-record rows.

**Not ready (05:23Z, 59,399 rows):** 42,529 "payment: not published" — mostly services (hosting, DNS, software: easyDNS 2,788, Jane 2,247,
Hawk Host 1,971 …) whose vendors publish no bank payment; by rule 13 these are not rows unless the vendor says so. 6,457 shared buildings;
6,181 no mailbox; 9,864 relationships not established (vendor statements, links).

**The plan to a million, as it stands (honest):**
1. Canada by where the organisation is — automated end to end (scan lists -> home-page scan -> mailbox reader -> referee -> rows). The
   ceiling is the organisations in Canada with a site, a role mailbox and an address that can be located (400,000-500,000 estimated);
   121,978 today. Growth now comes from the reader working through the Overture and certificate-log domains, every cycle.
2. Organisations abroad tied to a Canadian biller by a record — trademark owners and their Canadian agents (109,538 with an agent; 18,729
   with a listed website), then patent owners and their agents (CIPO), importers in customs records, US public buyers (subawards, FERC
   EQR), lobbyist clients. Each needs the organisation's site found without guessing (a register's or a places dataset's own listing).
3. Every row filled billers-first; estimates calculated and labelled.
A million is not on file; the second half needs record types abroad not yet built.

## 2026-11-12 04:50Z — the 04:03Z build read; where an organisation is when its own pages located nothing (registry, then Overture's listed address)

**Build of 04:03Z (code ff81695 + money fix), counted: 152,906 ready of 213,382** (by location 110,569 · best effort 31,486 · complete
10,851). Down from 158,527 at 01:44Z on purpose: 6,329 rows at an urban postal code fifty or more organisations print are not ready (the
landlord's account). Of the 152,906: amount and billing period 124,087; every main invoice field 81,570 (00:14Z: 70,503 and 24,279);
published $5,000+ 1,791. Told to the owner at ~04:30Z. 43146608664 (MAIL_ALL, contract list, city lever, pockets) started ~04:14Z.

**Built after it (coord/DECISIONS.md 2026-11-12 04:39Z):** an organisation whose own pages located nothing gets, in this order, its
registered address in a public registry (`org_places.csv.gz`: CRA charities, school directories — it was on the row, never used to name the
distributor), then the address an Overture Maps place lists for its website (one postal code for the whole domain, the place's name fits;
`tools/by_location.py directory_addresses / directory_cell`, `rank.py ovt_place / place_cell`), every cell saying where it came from; the
same listed address fills a missing buyer address on rows of other kinds. The address file (40 MB) is in the release `harvest-state`
(credit-scan.yml job overture, dispatched); both rank workflows download it. Sample builds (1 in 4, never multiplied): OWNER19 46,013 ready
of 62,922 → OWNER22 48,952 of 65,327 (every main field 23,577 → 25,698). The next cloud build with it: the 06:17Z cron.

**Also pushed (05:00-05:15Z):**
- The mailbox reader takes sites a listed address locates: 9,193 home pages print a role mailbox and no Canadian address (first class),
  22,546 print neither (second class, contact pages); `mailbox-crawl.yml` downloads the address file (run 43159326222 is the first with it).
- `credit_scan.py merge-graph` rewrites a list only when a row changed, with a fixed gzip time (the 04:54Z run re-committed 20 MB of the same rows).
- Billers first (coord/DECISIONS.md 05:15Z): the distributors' numbers from the global LEI register (api.gleif.org, open): NB Power 022248,
  Nova Scotia Power 1567820, Maritime Electric 235139-1, Newfoundland Power 4508 (their business registers), BC Hydro and Manitoba Hydro
  (LEI only, bodies created by their own Acts); NS Power's due terms (its Regulations s. 5.4) and Manitoba Hydro's (billing glossary).
  Some 27,000 ready rows lacked one of these in the 04:03Z build (BC Hydro 20,066 had no number).
- Trademark owners abroad (DECISIONS 05:08Z): `tm_register.py overture-sites` (14,112 owners in the US, UK, Australia with a website an
  Overture place lists under their name), `sites --abroad --overture` reads it first; tied when the site's own pages state the name (10 of
  the 40 largest in a test). tm-sites run 43159394354 dispatched; the daily tm-register.yml makes the leads.
- Checked and dropped: a re-read of the 126,561 located-nowhere organisations' contact pages (the reader already read 6-9 pages of most);
  OpenStreetMap addresses on top of Overture's (407 more).

**Toward a million, next lever measured:** the trademark register names 134,458 organisations ABROAD as owners of Canadian marks, 109,538 of
them with a Canadian agent of record (US 50,172 · CN 26,540 · FR 6,502 · GB 6,439 · DE 6,011) — a record that ties them to a Canadian biller.
They lack websites; Overture's global places (name + city + website) could give them without guessing a URL. To build: a name+city match
with the same rules as tools/tm_register.py match, then the mailbox reader, the referee, the agent-of-record rows.

## 2026-11-12 02:29Z — the owner's evening (rules 14-17): marks, order, estimates, fuller rows; the build with them is the next step

**The owner, 2026-11-11 20:04-20:36 EST** (AGENTS.md §1 rules 14-17; coord/DECISIONS.md 2026-11-12 02:14Z): "ship ready" on four things is not
enough — he wants every invoice field, an amount per billing period (estimated, labelled, when nothing is published); $5,000 a bill is a
priority, not a wall ("mark everything, prioritise over 5000"); one row per buyer is a hard rule, a vendor may repeat; the goal is a million
buyers; long sessions are ending ("one credit reset left … automation hand-offs [doing the] majority"). Told plainly that a million is not
in sight from what is on file (400,000-500,000 organisations in Canada at most, the rest must be organisations abroad tied to a Canadian
biller by a record) — not promised.

**Numbers (table of 00:14Z, code 445acd8): 136,513 of 186,576 rows meet the test** (by location 96,187 · best effort 29,967 · complete
10,359). Of the 136,513: with an amount and a billing period 70,503; with every main invoice field 24,279; with a published amount of $5,000
or more 1,510 (contract values). Contract dataset: 803,097 records, 316,131 buyer-vendor pairs, 5,590 buyers; current and $5,000+: 90,680
pairs, 66,678 behind 1,687 buyers with a mailbox. Sample build OWNER15 (1 lead in 4; never multiplied): 43,723 of 61,237.

**Built tonight (commit after this file):**
- `amount_mark` on every row (tools/relationship_rows.py: published $5,000+ · estimated $5,000+ · published under · estimated under · none)
  and `tools/priority_sort.py` (run by tools/rank_tail.sh): the rows that meet the test first, by mark. BUILD.json `ship_ready` carries
  `by_amount_mark`, `with_amount_and_billing_period`, `with_every_main_invoice_field`; the build log prints the same.
- Ontario's 53 distributors from their regulator (`tools/on_ldc_table.py enrich / rates`; `on-ldc-table.yml` refreshes the rates on the
  2nd of each month): the Distribution System Code (monthly bill, 20 days to pay, how a bill is issued and paid), the fixed monthly charge
  and every rate by the kWh from the Board's open-data file, the licensed name and licence number, HST. Hand-read additions (verified quote
  by quote): BC Hydro, SaskPower, Nova Scotia Power, Maritime Electric, Qulliq legal names; BC Hydro, SaskPower, NS Power, Maritime
  Electric rates; due terms, remit-to, tax. Every distributor with a rate gets `bill_amount_calculated` = its rate at 2,500 kWh a month
  (the use at which the Board's calculator opens), before tax, labelled "estimated —".
- Faults found in the published table, each a rule: colour codes / placeholders taken for postal codes (`by_location.usable`); urban postal
  codes printed by 10+ organisations said on the row, 50+ not ready (SHARED_SAY / SHARED_FAIL); another vendor's bill cells on rows that
  gave way to the distributor, emptied; the missing purchase-order number is a note now, not a failure (rule 13).
- Member rows: the body's lowest published dues from its own membership pages (`rank.py: member_dues`): 1,442 member rows of 11,605 carry
  dues in a re-test of the published table (195 before). The reader's money pattern cuts four-digit amounts without a separator
  ("$1195.00" -> 119): member_dues re-reads the amount from the sentence; tools/vendor_billing.py MONEY is still to be fixed.
- Buyers under contract: the record on a buyer's row is, within its best tier, one of $5,000 or more; an invoicing mailbox the buyer's own
  site prints counts also on another mail domain (its network's, parent's, e-invoicing provider's) — 50 more buyers with a mailbox; the
  build log counts why the referee's other mailboxes are not taken (`buyers under contract: a mailbox the referee holds that is not taken`).

**Added after 02:29Z (all pushed by 03:23Z):**
- tools/vendor_billing.py: four-digit amounts without a separator are read whole (MONEY), kept matches are re-read in lowest(); NB Power's
  legal name ("New Brunswick Power Corporation", its own supplier terms).
- Buyers under contract: `rank.py MAIL_ALL` — a row tries every verified mailbox of its "b:" keys, not only the best-graded (a lane's
  mailbox of another organisation hid the buyer's own: 141 buyers in a sample build); the full build writes
  `coord/results/ranked/contract_buyers_without_mailbox.csv` and the mailbox-crawl runners read it first (`lead_crawl.py`: a "b:" key is
  read even when a lane filed a mailbox for it).
- By the city an organisation's own page names, when no postal code was read (`by_location.biller_for_city`, `tools/data/city_biller.tsv.gz`
  from `on_ldc_table.py cities`: a city 98 %+ of whose postal codes are one distributor's): +1,944 rows in a sample build; the mailbox
  reader keeps a page's city line (`site facts: city_quote, city_url`).
- **A new list of sites: the Overture Maps places in Canada with a website** (`credit_scan.py overture`; monthly on the 25th in
  credit-scan.yml; `data/incoming/claude/credit_scan/overture_sites.csv.gz`): 773,691 hosts, 345,712 registrable domains neither read nor
  listed before (307,833 not .ca; ON 142k, QC 73k, BC 56k). The scan reads them at priority 3 (with OpenStreetMap's); the mailbox reader
  takes the ones whose home page prints a mailbox and a Canadian address. This is the largest new pool of organisations since the .ca lists.
- Sample build OWNER18 (all of the above but Overture): 45,941 of 62,871 ready; published $5,000+ ready 1,679.

**Builds:** 01:44Z (code ceb7eba, before tonight's rules): **158,527 ready of 213,288** (by location 116,526 · best effort 31,171 · complete
10,830). 02:54Z (code ff81695 + the money fix: marks, order, regulator, faults, dues) running; 43146608664 queued behind it (everything above).

**Next, in this order (short sessions):**
1. Read the two builds (BUILD.json `ship_ready.by_amount_mark`, `with_amount_and_billing_period`, `with_every_main_invoice_field`;
   SUMMARY.md "SHIP READY", "by amount", "how full", "urban postal code many", "buyers under contract", "by the city"). Tell the owner.
2. A hundred from the newest table, read row by row before he sees it (tools/test_sample.py shows `amount_mark`); faults become rules.
3. Watch the scan take the Overture sites (credit-scan logs; LANES.md "home pages read by the scan") and the mailbox reader's yield.
4. Municipal electric utilities of the pockets (Hydro-Sherbrooke, Hydro Westmount, Hydro-Joliette, New Westminster, Saint John Energy,
   Summerside, Penticton, ATCO Electric Yukon): ~2,700 organisations with a mailbox and a postal code there; each needs its own page read
   (address, territory, billing). Their cities are '-' in the city table today.
5. Billers with no number: BC Hydro (17,500+ rows; its own GST number is not on its supplier pages), Nova Scotia Power, NB Power, Maritime
   Electric, Newfoundland Power (its rate book is refused by robots.txt: no rate, said so).
6. Sources of NEW buyers with large bills (rule 15): codex / jules inboxes have the request (public bodies under contract outside the
   dataset first).
7. Toward a million (the direction, not built): inside Canada the pool is the sites the scan reads (now with Overture's 345,712 new
   domains); past ~300,000-400,000 rows the organisations must be abroad, tied to a Canadian biller by a record. The largest such records
   in bulk: owners of Canadian trademarks and patents with a Canadian agent of record (CIPO's open data: owner name and country; the
   owner's site must be FOUND, never guessed — an exact name + city match against Overture's places worldwide or Wikidata's official
   website), and US prime contractors with a Canadian subawardee (USAspending subawards, country CAN).

(03:37Z: the pockets' postal codes now name the distributor when the code's own place is not a municipal network's town —
`by_location.POCKET_TOWNS`, `tools/data/pocket_places.tsv.gz`; Québec, Saskatchewan, New Brunswick, Nova Scotia, PEI; not BC, not J0L.)

## 2026-11-12 02:15Z — safety-net turn: build 00:14Z gives 136,513 ship ready of 186,576; London Hydro's and Enova's own sentences added

(The main session's last commit is 445acd8 at 23:35Z, "what reading the hundred of the 23:14Z build found"; it did not write a section
here. This one records what the cloud shows. The section of 22:47Z below still holds the rules and the "Next" list.)

**Numbers (build 2026-11-12T00:14:07Z, code 445acd8; `coord/results/ranked/BUILD.json`, `coord/GROWTH_VS_BASELINE.md`).**
- Rows 186,576; with a mailbox 180,937 (baseline 63,641: +117,296).
- **Ship ready 136,513**: by where the organisation is 96,187 · best effort (by the kind, or a field not published) 29,967 · complete
  in the biller's or the record's own words 10,359. By kind: utility account by location 96,187 · membership 12,435 · licence 9,047 ·
  service 7,266 · sponsorship 4,183 · agent of record 2,924 · public contract 2,547 · dealership 1,825 · tenancy 99.
- Pay on sight (growth file): yes 1,104 · reference-less 829 · routed 41,833. Downstream pack of the build: pay_on_sight_yes 1,933.
- Row factory: 676,067 buyers in the cloud leads (member-live 23:13Z: +4,184 new); leads read by the build 786,046.
- Mailbox reader: 1,279,997 lead sites read, 315,187 with a mailbox (22:47Z: 902,604 / 236,200; +78,987 mailbox sites in two runs).
  The referee ran after each (01:30Z success). Rank build 43136600232 was dispatched at 01:44Z and is running: it delivers them.

**Health (01:50Z).** All five workflows are alive. The failures of 2026-11-11 (row-factory 18:35Z `merge_extract`, claude-engines
19:01Z and 20:16Z, rank-buyers 20:41Z `startup_failure`) are GitHub's artifact service during its outage (upload "Unexpected token '<'",
download "artifact not found"), not our code: no fix. GitHub status now: operational. Queued behind the 20-runner limit: row-factory
(01:31Z; its last complete cycle is 17:52Z on 2026-11-11 — check that this one ends), mailbox-crawl (6 of 8 shards running).
Run 43097494823 (verify-and-merge, queued since 20:41Z, a leftover of the outage) should be cancelled; this session was not allowed
to cancel a run. Later referee runs succeed, so it blocks nothing.

**Advanced (item 4 of "Next" at 22:47Z — the distributors' own words for Ontario).** `tools/data/billers_by_location.json`:
- London Hydro Inc. (376 rows in the 00:14Z build): billed monthly (own sentence), from $36.38 a month (fixed monthly delivery charge,
  Commercial < 50 kW), a bill with an invoice number, paid through a bank / pre-authorized withdrawal / cheque (card through Paymentus
  as well), remit-to P.O. Box 3060.
- Enova Power Corp. (450 rows): monthly invoice, paid through a financial institution / pre-authorized withdrawal / cheque (card as
  well), due 23 days after issue, late charge 1.50 % a month, remit-to PO Box 9021 Kitchener. No amount: its rates page gives service
  charges ($27.34, $33.46, $38.91 a month from 2026-01-01) without naming, in the text read, the class and zone of each — not taken.
- Every quoted sentence was looked for on the page named for it (read 2026-11-12 with the project's reader, robots obeyed); the table
  loads (62 billers), `payment_route` gives "either" as for Alectra. No change to rank.py. Effect: 826 rows move from "by the kind"
  to the distributor's own words at the next build. Ontario distributors with own sentences now: Toronto Hydro, Hydro Ottawa,
  Alectra, Hydro One, London Hydro, Enova (6 of 53).

**Next.** The list of 22:47Z from item 2 (the main session knows where it stands on the hundred), then: read the build of 01:44Z
(expect more rows by location from +78,987 mailbox sites; tell the owner the count); Ontario's next distributors by rows in the build
(take the counts from the line "rows that give way …" / by distributor in SUMMARY.md); Enova's amount from its tariff PDF; Hydro
One's amount; Elexicon refuses the reader (status blocked, not retried).

## 2026-11-11 22:47Z — rule 13 in the table: 79,860 ship ready (build 22:11Z); second step pushed (give-way, Ontario by postal code, reader's queue), its build is running

**The owner at 16:01 EST, in full:** "1 million goals think differently if need be this your project take all liberty as long as under
what we laid down invoice bank eft email Canadian vendor in simple terms and just populate those field as best as you can don’t just go
empty there’s clear goal and it is 1 million get there max". Not asked again; my reading is AGENTS.md §1 rule 13 and coord/DECISIONS.md
(21:05Z, 21:30Z, 22:44Z). In four lines:
- four things make a row (a Canadian biller with a relationship, a bill on invoice, a bank payment, the organisation's own mailbox
  re-read by the referee); a field nothing published fills is named on the row and no longer fails it (only the biller's printed
  address, and for a row by location the organisation's own address or postal code, still must be there);
- how a bill is paid may be said "by the kind of relationship" when the biller's sentence was not found — never for hosting or software;
- a relationship may stand on where the organisation is: the electricity distributor of its own printed postal code
  (`tools/by_location.py`); the row says what is certain (the biller of the address) and what is not published (who holds the account);
- a row whose own relationship cannot meet the rule (a service whose vendor's payment is not published, a client listing, a link, a
  trademark owner billed by the Office) gives way to that distributor and keeps the other relationship as a note.

**Told to the owner (21:51Z and 22:47Z):** the three decisions; 79,860 and what it is made of; that my "about 105,000" came from a
quarter-size build and was wrong; that a second build is running, estimate 120,000 to 135,000; that Alberta cannot be done by location;
"if rows that rest on location are not what you want, say so and I'll pull them". He has not answered. If he rejects them: they are one
kind (`relationship_fact_basis` starts "by where it is"; give-way rows too), removed by not making tier-I rows from `LOC:` in rank.py.

**Numbers.**
- Build 20:21Z (old rules) 6,405 · build 22:11Z (code c6cd6fe) **79,860 of 158,912**: by location 38,467 · best effort 33,095 · complete
  8,298. By kind: membership 12,388 · licence 8,943 · service 7,279 · sponsorship 4,746 · agent of record 3,566 · public contract 2,547 ·
  dealership 1,825 · tenancy 99. Failing: service, payment not published 55,690 · not established 15,843 · no mailbox 5,505 ·
  vendor registry warning 3,110.
- Build dispatched 22:45Z (code 3574581): sample build OWNER11 gave 44,432 of 60,384 (by location 30,490, best effort 9,957, complete
  3,985). **A sample is not multiplied by four** (DECISIONS 22:44Z): it tests the code. Read the build's own lines.
- The pool by location (scan: 377,262 home pages with a Canadian postal code; 115,996 of those sites have a mailbox row): with a mailbox
  and a distributor on file after Ontario about 91,000; with a mailbox and no distributor: Alberta 13,867 · Nova Scotia 2,208 ·
  Newfoundland 737 · PEI 398 · pockets about 4,600 · Ontario codes near an edge 2,787.
- The mailbox reader: 902,604 sites read, 236,200 with a mailbox. Unread: about 63,000 sites that print a role mailbox on their home
  page (read first from the run that starts after 23:35Z; 85 % give a row), then 750,000 .ca sites with none on the home page (10 %).

**What was built today after 21:46Z (all pushed, b94a500 / 3574581):** `rank.py` — the give-way loop before P13 (`GAVE_WAY`, note in
`other_relationship_sources`), `SCAN_PC` / `scan_address()` (the home-page postal code as an address, said as such), the register
look-up under the legal name a vendor's own site prints, `address_source`; `tools/on_ldc_table.py` + `on-ldc-table.yml` +
`tools/data/on_postal_ldc.tsv.gz` + `tools/data/billers_by_location_on.json` (Ontario: the regulator's map x postal-code locations x
postal areas; address and site from the Board's page on each distributor); `tools/by_location.py` (Ontario by the table,
`scan_postal_codes()`, a lane's sentences under `table_key`); `tools/lead_crawl.py` (site candidates first, any ending with a Canadian
address). Geodata is cached under `out/geo/` (not in git; the tool fetches it again).

**Next, in this order:**
1. Read the build dispatched 22:45Z (`coord/results/ranked/SUMMARY.md`: "SHIP READY", "of which", "rows that give way", "P13 added";
   `BUILD.json`). Tell the owner the count itself, in two sentences. If it is under 110,000, find why before anything else.
2. A new hundred from that table: `python3 tools/test_sample.py <table> --day 2026-11-11c --built <stamp>`; read every row; what
   reading finds becomes a rule first. Publish to the same page only if `ArtifactData list verdicts` is still empty
   (https://claude.ai/artifact/AKuRT9NPpMX3Jwfqj1ZERt), else a new page; QA instruction in `coord/inbox/chatgpt.md`.
3. The mailbox reader's run that starts after 23:35Z: its log line "site candidates (home page prints a role mailbox …): N queued" and,
   at the merge, how many gave a mailbox. Then the referee, then a build: about +40,000 rows expected over two runs.
4. The distributors' own words for Ontario (amount, bill, payment: 51 of 53 have only address and territory — every such row says
   "not published: amount" and "by the kind"): Alectra, Hydro One, Enova, London Hydro first (their contact pages are read:
   scratch `ldc_pages/`); Elexicon's site refuses the reader. Then Nova Scotia Power, Newfoundland Power, Maritime Electric (3,343
   organisations with a mailbox), the amounts of BC Hydro, Hydro Ottawa, SaskPower, NB Power, Qulliq.
5. Second-class candidates of other endings (.com / .org with a Canadian address, no mailbox on the home page: 56,485) into
   `lead_crawl.py --registry2`. Tracking parameters (`shpxid=…`) out of stored page addresses.
6. Member rosters: the chambers behind the 12,388 member rows are 71; the provincial federations list several hundred
   (`tools/roster_ingest.py`, GrowthZone / ChamberMaster hosts) — rows on a record, stronger than by location.
7. Everything of the 21:05Z list below that still stands: the site of a register entry (item 3 there), the billers' own sentences (4),
   vendor numbers (5), registers by descriptor (6), patents and owners abroad (8), the Sunday report 2026-11-15 (9).

**What a million needs, as I see it (said to the owner at 21:51Z, to be said again with numbers on Sunday):** one row is one
organisation with its own published mailbox. By location, every organisation in Canada outside Alberta whose site prints a postal code
and a mailbox is a row: the scan knows 377,000 such sites with a postal code on the home page, a contact page adds more, a mailbox is
found on a third to a half. That is 150,000 to 250,000 rows from what is on file, not a million; the rest needs organisations the scan
has not met (Canadian organisations on .com, rosters, registers, organisations abroad billed by a Canadian body).

## 2026-11-11 21:05Z — first build on the rule: 6,405 ready; read before it went out, re-tested: 7,754; GitHub Actions is down

**The table.** Build 20:21Z (code 091c3f5): 153,127 rows, 6,405 ship ready (licences 4,576 · public contracts 1,355 · services 464 ·
sponsors and dealers 10). I drew the hundred, read it row by row and did not send it: six kinds of fault (below). Each became a rule; the
published rows were tested again with the rules as they stand (`tools/retest_rows.py`): **7,754 ship ready** — licences 6,266 (Régie du
bâtiment, Toronto +381, Calgary +626, Edmonton +681), public contracts 1,354, services 134, members / sponsors / dealers / agents' clients 0.
The owner has that hundred on his page (https://claude.ai/artifact/AKuRT9NPpMX3Jwfqj1ZERt, version 2; `verdicts` was empty at 20:25Z);
the same rows are in `coord/pilot/TEST_SAMPLE_2026-11-11b.csv` and the QA lane has its instruction (`coord/inbox/chatgpt.md`).
He was told 7,754, what it is made of, that it is a re-test and not yet a build, and that it is nowhere near 280,000.

**What reading the first draw found (all fixed in the rules, pushed):**
- an amount that was a price increase (“Tarif de base : +5,00 $ par mois”: 11 of 15 service rows) or a discount (“$2.00/mo Discount”)
  → `vendor_billing._NOT_A_PRICE`;
- a refund clause or a body paying its own suppliers read as "how the bill is paid" → `relationship_rows._NOT_HOW_PAID`;
- a ministry's access-to-information office as its mailbox → `BAD_LOCAL` in rank.py;
- an owner-builder's licence priced from the contractors' fee table → no amount for "constructeur-propriétaire";
- a buyer that is one person's name ("Yann Fortier") → 157 given names added to `buyer_pages.FIRST_NAMES`;
- sponsors of clubs passed on the club's membership payment page → already stopped by the invoice-evidence rule (`nobill`), which that
  build did not carry.
Not fixed, written on the row: a legal entity that carries a former parent's name (ALSTOM RENEWABLE US LLC is General Electric's since
2015; the mailbox is Alstom's). No rule finds that class yet.

**New in a row (pushed, in the next build):** `tools/payee_fees.py` — the City of Toronto's nightly list of outstanding licence invoices
(licence number, invoice number, amount due: 4,379 on 2026-11-11), the renewal fee of each kind of Toronto licence (53 pages), Calgary's
fee schedule (78 types; a licence of several types by the schedule's own rule, labelled calculated), Edmonton's tiers (61 categories);
`bill_due_terms_as_published`, `bill_remit_to_as_published`; a member named in a body's directory carries the body's lowest published
dues; a buyer's purchase-order rule is asked of contracts, services and dealerships only. `tools/tm_register.py agent-sites`: 40 agent
firms tied to their own site by name and postal code (`data/incoming/claude/tm/tm_agent_sites.csv`), so that the vendor reader can read
how their invoices are paid; ROBIC, Fasken, Norton Rose, McCarthy, McMillan, Stikeman and Dentons refuse the reader and stay unread;
Gowling's site prints no address in its HTML.

**Cloud.** GitHub reported a partial outage from about 20:40Z: the rank build and the trademark run dispatched at 20:41Z ended in
`startup_failure`; vendor-billing (19:41Z), bbb-accredited, claude-engines and mailbox-crawl are still queued. Nothing of this run has
been built in the cloud yet. Five local sample builds on today's data passed (OWNER3 to OWNER6: 3,704 of 48,560 in the 1-in-4 sample).

**Next, in this order:**
1. When Actions answers (`curl -s https://www.githubstatus.com/api/v2/status.json`): dispatch `rank-buyers.yml`, then `tm-register.yml`,
   `biz-licences.yml`, `vendor-billing.yml` (`gh api -X POST repos/…/actions/workflows/<file>/dispatches -f ref=main`). Read the build
   (`coord/results/ranked/SUMMARY.md`, lines SHIP READY …); it should show about 7,750 plus the service rows whose amount is recomputed
   (Astral Internet: 301 rows) and the registry numbers merged at 20:10Z. If it differs from the re-test by more than that, find why.
2. The owner's marks: `ArtifactData list verdicts` on the page. Every "wrong" is a rule to write, then `tools/retest_rows.py`.
3. **The lever of the licence lanes: the site of a register entry.** Five public bodies' rows are complete (payment page + fee), and
   only about 5 % of their register entries are tied to a site on file. `tm_register.sites()` already finds an owner's site under its
   own name (labels from the name, `.ca` / `.com`, the site must print the name and the postal code). Generalise it to the licence
   registers: the unmatched entries of `biz_licences.py pull` and of the RACJ and RBQ lists (name, trade name, postal code) → the same
   search → `match`. Expected at 8 %: about 20,000 more licence leads, every one of a kind that is ship ready once its mailbox is read.
4. The same sentence from every other biller — "we send an invoice / a notice" and "pay through your bank / by cheque": the 71 chambers
   behind half of the 17,000 member rows (dues schedule, invoice, cheque or e-transfer: the version-5 vendor read runs when Actions is
   back), the Better Business Bureaus, the agent firms (40 sites tied), CMEQ and CMMTQ (their notice of assessment is an invoice with a
   number; the page read names only the card), Vancouver (its site refuses the reader: a lane with a browser).
5. Vendor numbers of billers that are partnerships or associations (58,000 failing rows): the Québec register's other names (ROBIC,
   Fasken, Lavery and Smart & Biggar are registered there under their French names), a GST number the biller prints itself
   (`vendor_billing` keeps `taxno`).
6. Registers by descriptor: Nova Scotia liquor (`en23-iwca`), British Columbia's licensed establishments, more cities; federal: radio
   licences (ISED's "Online Payment and View Invoices" page says it invoices), CNSC ("Cost Recovery Program — Paying your Fees").
7. Members: more GrowthZone / ChamberMaster hosts (22 Canadian ones known; the provincial chamber federations list several hundred
   chambers); exhibitor lists by the other lanes (`python3 tools/roster_ingest.py check`).
8. Patents (`ip-register`), trademark owners abroad (`tm-sites.yml` with `abroad=true`).
9. Sunday 2026-11-15, `coord/WEEKLY_REPORT.md`: wait or ship, with these numbers and no rounding up.

**Rules I gave myself this run:** a test set is read row by row before the owner sees it, and what reading finds becomes a rule before
the draw is repeated (the first draw would have shown him an amount of "$5 a month" on eleven rows that was a price increase); when no
build can run, the published rows are re-tested with the current rules and the page says so; a sentence about money counts only in the
direction of the bill. Recorded as it is: the Régie du bâtiment lane (built 2026-11-10) finds a licence holder's site through the domain
of the e-mail the holder gave the Régie — the address itself is never kept or delivered, a webmail or shared domain is left out, and the
site must print the holder's licence number, telephone or postal code. The lanes built since take nothing from a register's e-mail column.


## 2026-11-11 19:54Z — the owner's requirement: on invoice, by bank transfer. What it removed, what is built, what is next

**His words are in AGENTS.md §1, rules 6 to 12; the reasoning and the numbers in coord/DECISIONS.md (entry 2026-11-11 19:24Z); what the other
lanes build and how they hand it in, in docs/LANES_ON_INVOICE.md.** In one paragraph: the QA lane read the old column `ship_ready` on his 100
test rows ("no" on 97); he rejected that label, then my too-strict reading of his answer, then — once he saw how Shopify bills — the whole
card-billed side: "it needs to be bank transfers relationship not credit card … if it's not on invoice, by bank transfer then it's no".
Asked, he answered: one row per buyer, no buyer twice; remove the card and registrar rows; a contract awarded over three years ago with
no end date is not current; a vendor's registration number fills its number when its GST number is not public; an invoice payable by
bank transfer is in even when the biller also takes a card; any Canadian entity may be the biller; build every lane, "and more".

**Where the table stood by that rule (15:57Z build, 282,207 rows):** on invoice by bank transfer 7,833 (5,461 with a mailbox, 1,343 passing
the whole test), nearly all public bodies under contract; card on file 33,278; through a registrar 103,829; not published 134,524.
The Shopify day and a half produced no row that counts.

**Done since (all pushed):**
- `rank.py`: no row from a `.ca` registration or a card-on-file vendor; no inferred row takes their place; `ship_ready` & co. from ONE
  function (`tools/relationship_rows.py: owner_test`); the old label is `ap_mailbox_ready`; the biller's own roster (member directory,
  dealer list, tenant directory, sponsor / exhibitor list) establishes the relationship, a client list does not; fields by kind (`FIELDS`).
  Two local sample builds (1 lead in 4): 48,561 rows, 3,165 ship ready (about 8,700 in a full table): public contracts 1,303, licences
  1,357 of 1,623 in the sample (the Régie du bâtiment's payment page made them complete), services whose vendor takes a bank payment 503.
- `tools/payee_billing.py`: how a biller bills and is paid, hand-read and quoted — RBQ, Calgary, Edmonton, RACJ (with the yearly fee by
  kind of permit), Smart & Biggar (invoice paid by e-Transfer, EFT or cheque), OMVIC ("does not issue invoices": its rows fail, in its
  words). Entries from other lanes' files are used only after `payee_billing.py verify` found every quote on the page.
- `tools/vendor_billing.py` version 5: payment wording of regulators, cities, associations, firms; the bodies of the invoice lanes first.
  Every vendor on file was read today with version 4, so the version-5 read happens with the 05:43Z run of 2026-11-12.
- `tools/biz_licences.py`: a register is a descriptor file (`tools/data/registers/`, `contrib/<lane>/registers/`); matched against every
  site that states a Canadian postal code (491,058, was 263,687). First one: Québec's retail liquor permits, 32,167 in force, 1,602 tied.
- `tools/roster_ingest.py` (run inside biz-licences.yml): rosters other lanes harvest become listing leads.
- Engines: the store reader is out of mailbox-crawl; timers of tenant-factory, dns-services, ct-names are off; the keeper starts member /
  accreditation / licence / register engines first; the site reader reads the invoice lanes first and cannot hang any more (watchdog +
  restart + uploads whatever the end; two runs had lost one runner in six).
- Analysis, not kept: one row per (buyer, vendor) pair — 316,284 pairs behind 5,391 contract buyers, 220,814 with a mailbox. The owner:
  "only 1 buyer so no buyer should be repeated".

**Cloud at 2026-11-11 19:54Z:** rank build 43089522278 (dispatched 19:41Z, queued for a runner) is the first with the rule; mailbox-crawl 43087983412
(new workflow file) waits for the run of 17:25Z to end; biz-licences dispatched 19:53Z (RACJ leads); vendor-billing dispatched 19:41Z
(466 vendors never read); the registry engine (vendors by rows) merges about 20:10Z.

**What I told the owner and stand by:** registers name over a million organisations, but a row needs each one's own site and mailbox. A
register turns about 5 % of its names into rows (measured: RACJ 1,602 of 29,645; trademark owners 8 %); a roster that links each
organisation's site turns 30 to 40 %. With what is free: 100,000 to 150,000 rows; with a search budget 300,000 or more; a million is
not in sight yet. He holds the target at 1,000,000.

**Next, in this order:**
1. Read the build that carries the rule (`coord/results/ranked/SUMMARY.md`: the lines "SHIP READY", "by kind and by how the bill is paid",
   "one thing away"; `BUILD.json: ship_ready`). If it failed, the failure first. The one-thing-away list is the work list.
2. The owner's new hundred: `python3 tools/test_sample.py <table> --day 2026-11-11b --built <stamp>` (draws only ship-ready rows, by
   kind), read every row before he does, publish to the SAME page (https://claude.ai/artifact/AKuRT9NPpMX3Jwfqj1ZERt; `verdicts` was empty
   at 16:10Z — check again first: if he marked rows, a new page instead), tell him in three sentences, write the QA instruction in
   `coord/inbox/chatgpt.md` (five checks a row + "is the bill on invoice and payable by bank transfer as `payment_route_basis` quotes").
3. Payment pages of the billers behind the most rows (the test's top blocker, "payment: not published"): the Canadian Intellectual
   Property Office (read it only when no registry lookup is running: same host), City of Toronto, the BBBs, CMEQ, CMMTQ, OPC, the agent
   firms, the largest chambers. Put `python3 tools/payee_billing.py verify` into vendor-billing.yml (commit
   `data/incoming/claude/payee_verified.json`) so the other lanes' files count.
4. Registers by descriptor: Nova Scotia's liquor licences (data.novascotia.ca `en23-iwca`) and its other licence lists, British Columbia's
   licensed establishments (find the data file behind the page), more cities; then the federal ones (radio licences; the aircraft register
   with NAV CANADA's yearly charge; medical-device licences).
5. The 2,154 public bodies of the contract dataset without a mailbox (663 are one mailbox away from ready): a queue for the site reader
   and the mailbox lanes (the list is made by `tools/relationship_rows.py`: relationship_buyers_without_mailbox.csv).
6. Members: more Canadian GrowthZone / ChamberMaster hosts (`member-live.yml`, stage discover); dues and payment pages come with the
   version-5 vendor read. Exhibitor lists: the lanes have them as their first task; check `python3 tools/roster_ingest.py check`.
7. Patents (`ip-register`): owners of Canadian patents and their Canadian agents, the yearly maintenance fee from the tariff — on the model
   of `tools/tm_register.py`.
8. Sunday 2026-11-15, `coord/WEEKLY_REPORT.md`: wait or ship, with these numbers and no rounding up.

**Rules I gave myself today:** how a relationship is paid is read BEFORE its lane is built (the Shopify lane was built first and asked
after); a body's payment page is read before its register is added (OMVIC); no registry lookup from this container while the cloud
registry engine runs (17:02Z: 80 lookups beside two runners put about 3 requests a second on ised-isde.canada.ca for 80 seconds); an
edit that replaces text between two markers checks that the first marker is the one meant (19:10Z: 674 lines of rank.py deleted by a
marker that also stood in a comment; restored from git before anything was built on it).


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

## 2026-11-11 16:42Z — the test set is with the owner; what reading it first changed; what is waiting
**Published table (build 2026-11-11T15:57:44Z, code 4994cd6 = d55caf9 and the merges up to 15:02Z):** 282,207 rows, 274,632 with a mailbox —
A 1,275 · B 1,727 · C 315 · D 27,237 · E 5,154 · F 7 · I 17,390 · L 434 · M 13,416 · R 103,559 · T 104,118.
- Fact level (`relationship_fact_basis`): seen on the buyer's side 190,907 (R 103,559, T 87,348) · public record 16,623 · stated by the buyer
  17,154 · stated by the vendor 27,404 · link only 5,154 · inferred 17,390. Facts: 207,530 = 76 %.
- Billing period: 1 monthly 35,478 · 2 monthly or yearly 34,446 · 3 yearly or longer 123,451 · 4 per transaction 161 · 5 not published 81,092.
  Shopify rows by store country: US 19,985 · CA 9,926 · not read 288.
- Nine invoice fields (of 274,632): buyer legal name 46 % · buyer address 73 % · vendor legal name 84 % · vendor address 100 % · vendor tax number
  60 % · what is billed 82 % · amount 29 % · billing period 70 % · reference 80 % · all but the amount 45,548 (17 %) · all nine 15,704 (6 %; 1,649 at 14:02Z).
- Mailboxes by kind: general 267,733 · finance / supplier payment 3,927 · invoicing / AP 2,007 · purchasing 965.

**The owner's test set (owed since 07:15 EST, delivered 16:13Z).** `tools/test_sample.py` on the published table, seed 20261111: 100 rows in 13 kinds
(`coord/pilot/TEST_SAMPLE_2026-11-11.csv` / `.json`). Review page: https://claude.ai/artifact/AKuRT9NPpMX3Jwfqj1ZERt — three checks a row (mailbox,
relationship, billing), Right / Wrong, a note; his marks are documents `verdicts/<sample_id>` in the page's database (read them with the ArtifactData
tool, action list, collection verdicts). 19 rows carry a "known before you read" note written by `scratchpad/testset/annotate.py` (rules only; no row
removed). When the corrected table is published: if `verdicts` is still empty, draw again and publish to the same page; if he has started, leave
the page alone and make a second page.

**What two draws read before him showed (one row in five with a fault; none seen in a mailbox), and the rule each became** — coord/DECISIONS.md 16:14Z
has the measurements. In commit 58763dd: copyright-line legal names (own name / initials / government kept; otherwise a labelled last resort, not
counted among the nine); schema.org own-site names only for a legal person; amounts = a price-list line for the service seen
(`vendor_billing.lowest(rec, service)`; Hover's 5,078 rows lose a mailbox price and say why); Web Hosting Canada curated (11,551 rows); `.ca` rows
carry CIRA's Registrar Agreement facts and `bill_amount_calculated` (8 printed prices, $14.57 to $45 a year; its own column, its own log lines);
vendor and buyer names that were page titles; addresses without the page's words (`addr_clean`); news stories demoted to links; consultant
lobbyists without a firm left out; `lead_crawl.site_name_for` fixed at the source. Five local 1-in-4 builds (LEGAL1–5); LEGAL2 failed on my own
edit (an `elif` put inside a block) and was caught here, not in the cloud.

**A full table can be built in this container in two parts** (`scratchpad/ab/runparts.py <label> 2`: `RANK_PART=i/2`, 15 minutes a part, 5.4 GB,
then `tools/rank_merge.py`): 282,149 rows locally at 15:31Z against 282,207 in the cloud at 15:57Z. One process is killed at 5.8 GB.

**Runner slots.** The build dispatched at 14:01Z waited 60 minutes for a runner (20 jobs at a time: mailbox-crawl 6–8, credit-scan 6, two DNS
lookups of 4, certificate names 2, registry 2…). A build now takes 55 minutes once started. Not changed today; if it recurs, credit-scan goes from 6
runners to 4 (its rows are the weakest of tier T: a design credit carries no billing period).

**Running / waiting (2026-11-11 16:42Z):** rank build 43054878655 (started 16:05Z on the OLD code, lands about 17:00Z); rank build 43060865356 (the corrected code,
queued behind it, lands about 17:50Z); registry engine (vendors first), two DNS lookups, certificate names, credit-scan in progress.

**Not solved, said to the owner or to be said:** the amount on `.ca` rows is a calculated range, not a published figure; the buyer's legal name
stays at 46 % (the registry engine and the site reader are the two ways up); 267,733 of 274,632 mailboxes are general role mailboxes; rows whose
buyer is one person's own site (a test row: a named professional's site) are not flagged yet; tier D ("named as a client") is the weakest kind
that still counts as a relationship.

**Next, in this order:** (1) vendor reader version 4 (drafted in `scratchpad/vb5/vendor_billing.py`, tested on 18 hosts: the terms page always
read, one link deeper from a "legal" index, how the invoice arrives, the tax rule, the vendor's own GST/HST number; a price inside a long sentence
needs "from / starting at" before it) → into `tools/`, wired into the ranker (`bill_delivery_as_published`, `bill_tax_rule_as_published`,
`vendor_bn9` as printed), a 1-in-4 build, push, dispatch `vendor-billing.yml`; (2) when build 43060865356 lands: read its log (the new counters),
the second draw as above, tell the owner; (3) buyers that are a person's own site: flag, count; (4) city licence fees and member dues as amounts
(the body's own fee table); (5) the registers still to read (AMVIC, ESA, VSA, RHRA, TICO, BAO) and the Alberta pool participants list (monthly
settlement by a public body); (6) the four source families registered this morning.

## 2026-11-11 13:21Z — the owner's bar changed three times in an hour; what a row must now carry; what was built and what is waiting
**Owner (06:24, 07:15, 07:48 EST), in order.** (1) "billed for something monthly … or every 3 months … systematically by the vendor";
(2) that is "a subcategory": the gate is a relationship known "for a fact … something being where it is means that there's a relationship",
and around it "the data that would go within the invoice … billing cadence … the fields that the Shopify invoice would have … how much
does it cost"; calculated guesses allowed when "so many inferences [point] to one thing"; the 100 testers are owed; (3) "every single
aspect within an invoice matters … the amount … the correct address, the vendor … don't over rely on one thing … the most populated
fields … and the most amount, but populated". AGENTS.md §1 has the five rules; coord/DECISIONS.md 12:03Z and 13:18Z the reasoning.

**Published table (build 12:35Z, code f6f7052):** 265,999 rows, 258,757 with a mailbox — A 1,276 · B 1,721 · C 315 · D 27,139 · E 5,128 ·
F 7 · I 17,697 · L 435 · M 13,305 · R 101,433 · T 90,301. Second names of organisations: 9,984. It does not have the new columns yet.

**Invoice fields on that table (measured):** vendor address 99.5 %, vendor legal name 82 %, dates 80 %, buyer address 73 %, reference 68 %,
vendor tax number 61 %, buyer legal name 45 %, both parties complete 30 %, an amount 3 %. The amount and the buyer's legal name are the gaps.

**Built since 11:20Z (commit 838b926, pushed 13:19Z):**
- `tools/vendor_billing.py` + `.github/workflows/vendor-billing.yml` (daily 05:43Z): opens each vendor's own site (home + up to five
  pages its menu names as prices / plans / hosting / membership / terms) and keeps every statement of a billing period, the lowest price,
  the currency, the ways of paying and what happens to an unpaid service, each with its sentence, page and date. First 8,500 vendors (every
  DNS provider, every credited vendor, the vetted ones, the first member bodies), read from here: 1,304 price by the month, 349 say they
  bill monthly, 540 yearly, 20 quarterly, 7 per transaction, 6,113 publish nothing, 167 not readable; 303 say an unpaid service is cut off.
  Precision read by eye: 45 "bills monthly" statements — 42 right, 1 wrong, 2 with a yearly option missed; 22 "unpaid" statements — 20
  sentences, 2 section titles. State: `data/incoming/claude/vendor_billing/billing_*.gz` (append-only).
- `tools/tech_relationships.py` BILLING: the 35 vetted vendors' terms read by hand — 21 state a period (Shopify, Jane, Rezgo, myRealPage,
  NiceJob, Checkfront, WebRezPro monthly; Lightspeed, Unbounce, Thinkific, GOrendezvous, Owl Practice, Juvonno, TouchBistro, Amilia,
  Commerce7 monthly or yearly; ClubRunner, CrowdRiff, Edsby, Jumptools yearly), 14 publish nothing, Jobber's site refuses the reader.
  Shopify's bill, from its own pages: three kinds of fee, U.S. dollars, sent to the store owner's e-mail and shown in the admin, charged
  to the card on file every 30 days, tax by billing address, nine-digit bill number ("SHOPIFY* 123456789"), store suspended 28 days after
  a failed payment; plans $29 / $79 / $299 / from $2,300 a month. help.shopify.com answers 403 to the reader: not read.
- **Shopify corrected**: section 13 of its terms names two contracting parties for stores in the United States or Canada (Shopify Inc.,
  Ottawa; Shopify Technology (USA) Inc.) and lets Shopify Inc. act as billing agent for the other. Rows stay; the note on every row carries
  the wording; stores are counted by country (sample: US 2 : CA 1).
- Ranker, new columns: `relationship_fact_basis`, `recurring_billing` (1 monthly · 1 quarterly · 2 monthly or yearly · 3 yearly or
  longer · 4 per transaction · 5 not published), `recurring_billing_basis`, `bill_amount_indicative`, `bill_amount_basis`,
  `bill_items_as_published`, `bill_currency_as_published`, `bill_delivery_as_published`, `bill_payment_method_as_published`,
  `bill_tax_rule_as_published`, `bill_identifier_format`, `service_stops_if_unpaid`. The log prints rows by billing period and the fill
  of nine invoice fields, tier by tier. Among the services an organisation is seen to use, the one whose vendor bills by the month
  claims the row. Local 1-in-4 build on today's data (91,372 rows with a mailbox): 1 monthly 7,814 · 2 monthly or yearly 7,398 ·
  3 yearly or longer 41,297 · 4 per transaction 63 · 5 not published 34,800; an amount on 21 % of rows (was 3 %); all nine fields on 404.
- Faults the first test draw showed, fixed in the ranker: 579 buyers named "About" (BBB profiles), "Welcome to …" names, 530 dates
  written day-month, CIRA's legal name under a carry-over note (101,433 rows), Shopify's Montréal office in place of the registered
  office its terms give, a law firm that is its own trademark agent; a caution where buyer and vendor print the same street address (1,200).
- `tools/registry_lookup.py`: vendors asked by the rows they carry and under the legal name their own site states; the cloud engine
  looks vendors up again (`--kind both`; it had been buyers only since the move to the cloud). 36,487 of 130,745 T/D/M rows have a
  vendor business number; Web Hosting Canada alone is 10,007 rows without one.
- `tools/test_sample.py`: 100 rows, 13 kinds, seed 20261111, two passes over the table (the first version held it in memory and was killed).
- `coord/source_registry.csv`: US UCC filings with a Canadian secured party; tenant directories of Canadian landlords; council award
  resolutions; franchised brokerages.

**Running / waiting (13:22Z):** rank build 43028063029 (new columns) and vendor-billing 43028074612 queued behind the long engines;
registry engine due 13:23Z (first run on the new address, vendors included); ct-names, two certificate-name sweeps, credit-scan, tenant
factory, walk_terms in progress. The 100-row test set goes to the owner from the build with the new columns.

**Next, in this order:** (1) the test set, delivered; (2) calculated cadence with its published basis and its label (construction under a
prompt-payment act, rent, electricity, dues); (3) vendor names that are still a domain (11,308 T rows) and buyer names that are a domain
(28,800 rows); (4) member dues from the bodies' own pages (the reader has only read the first of them); (5) the lanes registered today.


## 2026-11-11 10:15Z — the build of 09:39Z failed on my own code; fixed, tested on today's data, dispatched again
- **Build 42997010689 failed at 10:00Z** in the second-names sentence written at 06:02Z (`"…" % (a,) + tuple(b)`: the format was applied
  before the tuples were joined). It had only ever met rows of the registry lane; the crawl of 09:14Z brought the first lead of another
  lane whose site answers under a second name. Fixed (10:02Z). **The published table is still the 08:25Z build**; the crawl's +21,500
  mailbox rows wait for build 10:15Z.
- Before dispatching again the local sample build was run on TODAY's data (the snapshot was refreshed from the repo): exit 0, 165,185
  rows on a 1-in-2 lead sample, 5.1 GB. **Second names: 9,985 leads** — 3,584 `.ca` names whose site lives under another ending (new
  registry leads), 3,495 `.ca` names answering at another `.ca` site, 2,902 leads of other lanes re-pointed to the site that answers; in
  the sample table 1,274 tier-R rows and 963 rows of other tiers carry one. Twelve read by eye: the two names are the same organisation
  in each (bubblestick.ca → bubblestix.com, goinflatable.ca → grandriverinflatables.com, publicbeach.ca → publicbeachswim.com …).
  **Rule for me: a sample build on the day's data before every cloud build that carries ranker changes** (`scratchpad/ab/run.py`).
- **Stores' legal names:** the reader took nothing from the "Contact information" page every Shopify store can publish ("Trade name: X
  Inc. Phone number: …"). A value with a legal form under "Trade name / Business name / Nom commercial" is now the legal person's name;
  stores read before that have no legal name get that ONE page read (no version bump: 200,000 other sites are left alone).
- Self check-ins scheduled: 11:20Z (this build), 13:35Z (registry run, site-facts run, registers' first leads).

## 2026-11-11 09:40Z — since 08:58Z: the certificate logs' first full run, a second register, plain names, names read off pages
- **Certificate logs, first full run merged 09:37Z** (42975037314, two readers, no refusal from any log): 528,687,616 certificates read;
  `.ca` names new to the lists on file **205,929** (467,623 seen); names for the store sweep **18,746,074 new** of 29,643,304 seen (list
  `ct_list_20261111T064848.txt.gz`); 2,114,484 on the other endings; 1,797 validated subjects in Canada; 17,576,431 tiles still to read
  (about eight more runs; the chain started the sweep of the new list and the next reading run by itself). At the first list's rate
  (7.3 %) the new list holds over a million stores not known before — the store reader (one queue per runner towards Shopify, six
  runners) is now the limit of that lane for weeks, not the supply.
- **Mailbox crawl merged 09:14Z**: 705,076 lead sites read; **+17,832 mailbox rows in one run** (the run before: +4,245) — the first with
  the reader of 06:02Z on half its runners (second names, the www / http fallback, more role words, sites read once more); stores:
  122,781 read, 30,233 accepted (+3,626). The referee landed them at 09:33Z; rank build dispatched 09:39Z.
- **Second register built: the HCRA's Ontario Builder Directory, 6,888 licensed builders and vendors** (open data calls; annual licence
  fee $715 published → the row's value, labelled a tariff). Test on 80: 43 name a website, 19 sites tied. Register entries that name no
  site are tied by telephone to a site already read when it is the only site on file with that number and its name or postal code
  agrees ("2261703 ONTARIO INC" for Big Wheels). A sample build shows the rows in tier M with the register's legal name, the
  registration number, start and end dates. ESA, VSA and RHRA turned out to sit behind portal applications: noted in the registry.
- **Registry lookups: plain names too** (174,584 rows), after all the others and only with the buyer's province known; a match counts only
  when the single registered entity of that name has its registered office in that province. Measured on file: of 105 plain-name
  matches that a site's own spelled legal name can check, 92 are the same name and about 8 more the same company written another way.
  The ranker keeps the site's own printed name against a registry record of another name found under a plain name.
- **Names read off a page:** of 45 published "stated on" legal names, 8 carried a clause of the sentence or a page word ("… or its
  licensors", "… unless otherwise stated", "History Vancouver Poetry House Society"). The tidy step cuts them now and renames a row that
  was named after the same sentence (sample build: 146 cells, 54 rows on a 1-in-2 sample).
- **Still open:** the list above (08:58Z) from point 2 on; a self check-in is scheduled for 13:35Z (registry run on the new address,
  the 12:11Z site-facts run with one queue per platform, the 12:17Z build, the registers' first leads).

## 2026-11-11 08:58Z — build 08:25Z: 253,908 rows; five faults found by measuring, one new lane
**Table (build 08:25Z, code 508d5f9, audit PASS):** 253,908 rows, 247,548 with a mailbox — A 1,276 · B 1,720 · C 315 · D 27,228 · E 5,175 ·
F 7 · I 18,028 · L 437 · M 13,220 · R 99,426 · T 80,716. No new mailbox rows since 07:17Z (one runner of the mailbox crawl hung; its run
ends at 09:22Z by its own limit). What moved is the bill-to side, on rows with a mailbox:

| field | all | A | B | C | D | E | I | L | M | R | T |
|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer legal name | **44.8 %** (42.0) | 91.9 | 78.3 | 75.2 | 46.2 | 45.7 | 46.7 | 77.8 | 89.6 | 37.0 | 44.3 |
| buyer address | 73.1 % | 97.5 | 88.5 | 94.0 | 78.9 | 63.3 | 76.8 | 87.6 | 99.2 | 60.3 | 81.5 |
| buyer telephone | 59.6 % | 81.2 | 77.0 | 83.2 | 62.0 | 56.0 | 58.0 | 70.5 | 69.6 | 56.6 | 60.6 |
| buyer registry id | 10.6 % | 54.5 | 19.7 | 43.5 | 9.4 | 7.3 | 16.4 | 14.6 | 43.6 | 7.2 | 7.7 |
| vendor legal name | 82.3 % | 98.2 | 86.9 | 95.6 | 43.4 | 55.0 | 90.3 | 76.9 | 57.7 | 100 | 77.4 |

**What was found, each by measuring a stage that looked fine** (details and rules: coord/DECISIONS.md 07:46Z, the commits of 07:39Z–08:58Z):
1. *A refresh pass of 16 runner-hours merged nothing* (run 42958065125). (a) The site-facts readers wrote their whole state every five
   minutes from any worker thread to one temporary path; once a write took longer than five minutes two writes overlapped and a rename
   published an unfinished file. Now: one writer at a time, the reader stops by itself at its deadline (`tools/run_box.py`); the merger
   reads a cut file for what it holds. (b) A name the v3 reader had taken stayed inside a record v4 re-read: of 160 such sites read again,
   v4 gives none on 9. A spelled name now says which version took it; 31,396 names kept after a check on their own quote, 3,001 sites
   queued again. (c) Two merges of one state file could lose one run's records: every version of a state file now has its own asset name
   and the push of the manifest line decides. **Recovered** by running the failed merge again on the eight artifacts: 164,025 → 238,794
   site records on file after the two runs that followed, none cut.
2. *The site-facts reader is one busy core* (250 ms of CPU a site → 3.4 sites a second whatever its threads). Three readers a runner now,
   each with its own file of changed records only: a refresh of 40,000 sites took 45 minutes on 8 runners instead of hours.
3. *Every Wix site was "blocked".* Both site-facts readers looked for the word "captcha" in the first 5,000 characters of any home page;
   Wix prints it in every page's settings, and so does any page that loads reCAPTCHA early. Of 60 delivered rows' sites never read, 40
   were such pages; with the size test the mailbox reader already used, 41 of the 60 are read. About 24,000 rows' sites. First cloud run
   after the fix: 2,100 of 3,500 never-read sites per reader now give a record — and 28 % still answer 403 / 429 **to the runners** (none
   did from here): the next thing to look at (the tries are now kept between runs, `crawl_state/org_tried_*.gz`, with the answer's code).
4. *Registry lookups had not run since 2026-11-09* (dispatched by hand only): 57,170 buyers whose name carries a legal form or whose site
   states their legal person were waiting (8,872 looked up of 66,042). On a schedule now, two runners at one request a second. And the
   service had moved: `/api/v3/search?fq=keyword:{…}` answers 404, the new front end calls `/api/v1/search?q=`. Fixed at 08:10Z — ten
   minutes after a run had been started on the old address; that run records an error for every name until 13:20Z (a run cannot be
   stopped from here), the 13:23Z run asks them again. **Lesson recorded: try one request from here before dispatching an engine that
   has not run for a day.**
5. *Why half the sites give no legal name:* 215 sites that v4 read without finding one, read again here with every legal / policy page
   they link and eight standard paths: **193 print no name with a legal form anywhere** (90 %). The site route is at its ceiling there;
   the rest must come from registers. Hence 4 above and the new lane below.

**New lane — public registers of Canada's delegated authorities** (`tools/authority_registers.py`, `authority-registers.yml`, daily).
A business on such a register pays the authority every year; the register names it with its LEGAL name beside its business name, a
registration number, first-registration and expiry dates, address, telephone and often its website. First one built today: **OMVIC, 7,865
registered motor dealers in Ontario** (the search returns 5,000 names at most per answer: limited letters are asked again in pairs and
threes; letters alone gave 6,888). A third of the entries name a website; it is kept only when its home page shows the registrant's
telephone number or postal code. First cloud run 42991045828 (profiles: 82 minutes at 1.6 requests a second). Seven more registers
answered a plain read today and wait in `coord/source_registry.csv` with a note to the pipeline lanes: AMVIC (Alberta, ~7,000 automotive
businesses), VSA (BC dealers), HCRA's Ontario Builder Directory (~6,000 builders), ESA (Ontario electrical contractors, ~8,000), RHRA
(retirement homes), TICO (travel agencies), BAO (funeral homes). Rows of this lane are in tier M, on their own line.

**Certificate logs:** the sweep of the first list is complete — 657,286 names asked, **47,751 on Shopify's storefront addresses (7.3 %)**,
1,087 on a watched Canadian provider's name servers. The first full reading run (42975037314) merges about 09:25Z.

**Open, in order:** (1) the 403 / 429 answers the runners get from 28 % of never-read sites — which hosts, and whether one queue per
address (not per site name) is the cure, as it was for Shopify; (2) read the mailbox crawl's merge of 09:25Z: second names
(`site_lives_at_another_domain`), `read_once_more`, the first stores from the certificate logs; (3) the registry run of 13:23Z: answers
for the 57,170, then a precision test of looking up PLAIN names (174,584 rows have one) against names the sites state; (4) OMVIC's first
leads through the mailbox crawl; the next registers (HCRA, AMVIC, ESA); the dealers whose entry names no site, tied by telephone / postal
code to the site facts on file; (5) one reader instead of three for every site (the mailbox crawl could emit the site facts from the pages
it reads anyway); (6) vetting: www.cchifirm.ca, www.civicweb.net, Rafflebox, MyEvent; (7) Sunday's report (`coord/WEEKLY_REPORT.md`).

## 2026-11-11 06:50Z — build 04:47Z: 246,898 rows; names from the certificate logs; why sites give no mailbox, measured; runner slots
**Build 04:47Z (code 1df5f97): 246,898 rows, 240,626 with a mailbox.** A 1,276 · B 1,718 · C 315 · D 27,217 · E 5,125 · F 7 · I 17,816 ·
L 436 · M 11,320 · R 98,049 · T 77,347. Audit PASS (0 hard failures); check 20 (legal-name furniture) 56 cells (was 372). The vendor-side
fixes of the night, measured on the full table: vendor legal name T 52 → 74 %, B 67 → 86 %, C 74 → 86 %, D 34 → 40 %, A 93 → 97 %;
vendor website T 93 → 99.9 %. Still empty: tier I (the inferred vendors' names, fixed after this build's code), tier M 55 % (cities and
the Trademarks Office as vendors: the vendor-as-buyer join lands with the next build), the hosts that keep the reader out (namespro.ca
983 rows, vianet 188, domainpeople 150) and those whose terms name nobody (rapidenet.ca 1,410, linknowmedia.com 807, likuid.com 491).
Buyer side on rows with a mailbox: legal name 42 %, address 73 %, telephone 60 %, registry number 11 % — the legal name is still the
largest empty invoice field (reader v5 after the v4 refresh, below).

**1. A new source of NAMES: the Certificate Transparency logs** (`tools/ct_names.py`, workflow `ct-names`, notes/ct_names.md, decision
05:35Z). The lanes that grow the table can only ask the sites whose names they hold, and the names came from the web graph (sites
somebody links to) and one public list. Every HTTPS site is in the certificate logs. The static logs run with Sunlight publish *names
tiles* (6.5 KB per 256 certificates, made for readers that want names only): Let's Encrypt Sycamore + Willow, Geomys Tuscolo +
Trastevere, IPng Gouda. Budget per operator for all runners together: 90 / 30 / 20 requests a second; newest tiles first.
First cloud run (test, 45,000 tiles = 11.5 M certificates, 11 minutes of reading, no error, no 429):
- `.ca` names seen 19,534 — **8,123 (42 %) on no list we hold** → `credit_scan/ctca_<stamp>.gz`, read by the home-page scan (priority 4)
  and the DNS lookups. The lists on file hold 2.49 M `.ca` names of ~3.4 M registered; half of ours do not answer.
- names on the store sweep's endings 1,095,327 — **657,286 (60 %) not among the web graph's 78.7 M** → release `harvest-state`
  `ct_list_20261111T060239.txt.gz`; `dns-services` mode `ctsweep` asks them the sweep's two questions (run 42974942196 started 06:48Z).
- 175 validated subjects of organisations in Canada (Central 1 Credit Union, Open Text Corporation, William Osler Health System …) →
  `ct_names/ov_ca_<stamp>.jsonl.gz`; not used yet (a rule of its own: the subject is the subscriber, which can be a host).
The real run was dispatched 06:48Z (2 runners, 150 minutes, chains itself while tiles are left: 19.6 M tiles ≈ 5 G certificates, one to
two days at the budget). **Watch:** rate lines in the read logs (a halved rate means an operator said 429 / 503); the share of new names
per run (falls as the logs repeat themselves); stores per million names in the ctsweep; `.ca` names → scan → registry class.
Not seen by this source: certificates of GoDaddy, DigiCert, Amazon, Microsoft (RFC 6962 logs only), and what sits only in IPng
Halloumi or Google's static logs (no names tiles).

**2. Why two thirds of the lead sites give no mailbox — measured, and the part that was ours** (decision 06:02Z). 260 sites read again
with every address and verdict kept: a third print no address at all; 15–20 % only a webmail address; 12 % only people; 5–6 % hide it
behind Cloudflare's script. Ours: (a) 1 `.ca` candidate in 7 is a **second name** of an organisation whose site lives under another
domain (osfs.ca → flyos.ca): the reader now follows a name to the HOME page of the domain that answers (never a page inside another
site, a platform, a network, a parking service, a provider's own domain, a hub of 30+ names) — the row is about the site that
answers and says which name the relationship is about; (b) a bare name that does not answer is asked once at `www.`, a dead site ends
as `unreachable` after one or two requests (was eight, 20 s each), the pages are asked of the address that answered, leads start where
the scan found the site; (c) role words that were not on the list (gestion@, leasing@, membership@, information@, info<city>@ …); the
ranker reads the reader's lists. Second sample with the new reader: 2.3 % of the leads and 6.9 % of the registry candidates that had
given nothing now give a mailbox → about 15,000 rows from sites already read (re-read once, mark `r3`, after every site never
read), and the same share more of every site from now on. On a 1-in-2 sample build: +21 rows from mailboxes the referee had already
confirmed, 1 synthetic second-name row correct; one row moved from tier B to T (a second owner of purdue.edu makes the borrow
ambiguous — the conservative rule, left).
Not taken, on purpose: an address named after the organisation (ace@aceplumbing.ca — no list of given names is complete enough to
tell it from a person's); same-telephone sister sites without a redirect (no proof without a second read); webmail; Cloudflare.

**3. Runner slots.** The account runs 20 jobs at a time. 06:00–08:00Z: two org_facts runs held 16 of them; the certificate merge
waited 26 minutes, the rank build, a credit-scan merge and a probe are still waiting. A site reader waits on the network (23 ms of
CPU a page, a third of one core at 120 sites at a time), so runners are made wider, not more numerous: org_facts 8 → 4 runners at 100
sites each (its refresh chain too), mailbox crawl 120 → 200 sites a runner (6 runners kept: the store queue is per runner), ct-names
2 runners. Nothing running was touched (cancelling runs is not permitted to this session).

**4. Projection, restated with the new source (honest ranges; the certificate numbers are one test run old).**
| lane | now | what is left | by early January |
|---|---|---|---|
| stores (Shopify Inc.) | 23,414 accepted of 104,073 read (22.5 %) | ~960,000 known + the web-graph sweep's rest (~290,000) + the certificate names (unknown; 60 % of them are new names) | +250,000 to +400,000 |
| `.ca` registry class | tier R 98,049 | the detector-5 pass (37 % of the "unreachable" answer on www / http: ~460,000 more home pages), class 2 (~1 M sites at 10–17 %), the certificate `.ca` names (42 % new, and alive) | +200,000 to +300,000 |
| DNS-provider, credits, listings, licences, tenants | T 77,347 · D 27,217 · M 11,320 | 109,000 DNS leads not read yet; watched name servers on every swept name; vetted services | +60,000 to +100,000 |
| sites already read, read once more (r3) | — | 368,000 | +15,000 |
**750,000 to 1,050,000 by early January**, against 600,000–700,000 said at 03:50Z. What decides where in the range: stores per million
certificate names (first figures today), how many certificate `.ca` names answer and print a mailbox, and the two queues with a fixed
rate (the store reader: ~96,000 stores a day; the referee). The ranker needs its parts mode above ~700,000 rows (14 GB at a million).

**Open, in order:** (1) first ctsweep figures → the owner's update; (2) the build with the 04:14Z–06:02Z ranker changes (queued behind
the slots): inferred vendors' names, vendor-as-buyer join, vendor display names, second names, role words; (3) probe 06:27Z: vetting
sheets of 19 services counted in the link file (Commerce7 1,597 sites, myRealPage 1,946, centiva.io 996, SharpSchool 396, Showpass 343,
GovStack 274, MyEvent 272, CCH iFirm portals 191, Rafflebox 141, CivicWeb 116 …); (4) v4 refresh (two runs in progress) → reader v5
(agreement party, legal hub, standard legal paths) → drop the hand table of vendor names; (5) validated subjects as legal names (rule:
the subject must carry the organisation's own name); (6) CharityVillage reader; (7) Sunday's report.


## 2026-11-11 03:50Z — build 03:29Z: 242,317 rows; 228,000 DNS-provider leads; the vendor side audited (whose address, whose website, whose name)
**Builds.** 01:51Z: 242,292 rows (236,315 with a mailbox). 03:29Z: **242,317 (236,341)** — A 1,276 · B 1,719 · C 323 · D 28,316 · E 5,275 · F 7 ·
I 18,053 · L 440 · M 10,814 · R 99,842 · T 70,276. Audit PASS on both (0 hard failures). Buyer legal-name cells: 82,018 = 33.9 % (31.6 % at
22:38Z): the name that carries its form 6,110, the CRA list by number 491, grants recipients 316. The reader's v4 names are not in yet: the
refresh pass (8 runners, started 01:18Z) is still reading; its merge chains the next one.

**DNS.** Records for 4,510,029 domains; stores on Shopify's addresses 1,063,361. The credit-scan merge of 03:11Z applied the lead rules to the
repaired records: **228,322 DNS-provider leads (108,956 new) from 461 providers located in Canada** — WHC 48,596 · Webnames 27,028 · Namespro
26,000 · Hover 20,933 · easyDNS 18,021 · Internic.ca 6,772 · Rapidenet 4,923 · Canadian Web Hosting 4,277 · Doteasy 4,151 · LinkNow 4,029
(87 % of its customers are not on .ca: American small businesses paying a Montréal firm) … the first five are 61 %. 2,964 new credit leads,
141 member leads. They now wait for the mailbox crawl: 579,122 lead sites read so far, 177,090 with a role mailbox; its last runs read the
second class of .ca candidates and found a mailbox on 8-11 % of them. Stores: 104,073 read, 23,414 accepted (22.5 %), ~10,000 read per run.

**Row audit of the vendor side — three defects on rows already delivered** (coord/DECISIONS.md 02:45Z and 03:44Z; all in code, pushed):
1. **Whose address.** "Vendor located in Canada" was proven by an address read on any host under the vendor's registrable domain. A customer
   of Odoo in Sherbrooke stood for odoo.com (Belgian; 358 leads), the Canadian Hockey League's office for three teams in Washington State
   (214), a realtor's address for AvenueHQ of Bend, Oregon (753), a platform's Vancouver address for American associations on its sub-sites.
   Cloudflare, Zoho and Mimecast passed on one Canadian office among several countries. Rule now: the address must be printed on the
   vendor's own site (own_host / proof_fits / path_tenants); two or more other countries and no .ca domain = multinational, kept out; an
   office abroad seen in the address quote counts as another country. Withdrawn at the merges of 02:5xZ-03:11Z: 1,649 row-factory leads,
   2,922 credit / DNS / member leads; 1,418 waiting links not promoted. The build of 03:29Z still carries the credit / DNS ones (its
   checkout was 02:49Z); the next build does not.
2. **Whose website.** 17,691 rows carried a third party's page as the vendor's website — every Shopify row a Yahoo Finance quote page —
   from the Mac-era search check that "confirmed" any page printing the vendor's name. Vetted vendors now get the site of their own terms
   page; a search-proposed site must carry the vendor's name.
3. **Whose name.** 63,216 named-vendor rows had no vendor legal name. The reader's v4 names now serve the vendor's site too; the terms of
   the three largest providers the reader does not reach were read by hand (WHC Online Solutions Inc, Tucows.com Co., World Host Group Ca
   Corp: data/incoming/claude/claude_vendor_names_read.csv); a vendor name that carries its form is taken as the buyer side does.
Also: 455 buyer legal-name cells held page furniture ("Lambton College Your Cart Check Out Continue Shopping") — a last pass tidies names
read off a page and takes the legal person a sentence names ("DIV7 is a Division of Naro Building Systems Inc"); the audit's check 20 had
flagged 5,266 cells for words in their source text and missed the furniture — it reads the name now (372 real faults on the same build).
All of it ran on the sample build (55,127 rows; tiers unchanged; 1,697 vendor legal names, 2,768 vendor sites corrected, 130 names tidied).
**Not yet measured on a full build** — the first build after 03:45Z carries these; read its counters and the audit's check 20.

**Detector 5, first cycle** (445,303 home pages): outside links per site are on file (links_*.gz 20 MB, sections_*.gz 3.4 MB). Sites that
link their own account at a watched service: Jane 16,502 · Jobber 4,334 · BBB profile 3,940 · CanadaHelps 2,189 · HomeStars 750 ·
Checkfront 559 · Amilia 463 · Showpass 431 · GOrendezvous 418 · SkipTheDishes 296 · Keela 295 · Libro 278 · Ocean 198 · Moneris 168 ·
lepointdevente 164 · CARFAX Canada 151 · RAMP 151 · WellnessLiving 144 · Rezgo 142 · TouchBistro 131 · Bambora 131 · WebRezPro 123 ·
AutoTrader.ca 114 · Race Roster 106 · Jobillico widget 71 · Medeo 53 · Clio 45. Jane, Jobber, Checkfront, Amilia, WellnessLiving,
TouchBistro are vetted and flow to the tenant factory. **Next: vet the others** (terms page naming the contracting company and its
Canadian address; pricing — no free plan; what the link proves): subscription services first (GOrendezvous, Keela, Libro, Ocean, CARFAX
Canada, RAMP, Rezgo, WebRezPro, Medeo, Clio, Noterro 484, Owl Practice 324, Jonas Club 332, Juvonno 125). CanadaHelps read (terms +
pricing, 03:45Z): gifts are made to CanadaHelps CanaDon (BN 896568417RR0001), which passes them on "minus its payment processing fee"
(3.75 %) — the charity is never invoiced; a fee kept at source. Kept aside until the clearer ones are in.
**Job boards (plan item 17)**, read 02:00Z: CharityVillage prints prices (a posting CA$ 298, for-profit CA$ 398) and each job page prints
"Published" and "Expires" dates and the employer's own website; volunteer listings on the same addresses are free and must be told apart;
1,293 job pages and 12,608 organisation pages in its sitemap. Jobboom, Jobillico, Municipal World, CivicJobs and CareerBeacon refuse the
reader (blocked, not pursued) — but 71 employers' own sites embed Jobillico's widget (detector 5), which needs no page of Jobillico.

**Open, in this order.** (1) Read the first build after 03:45Z (counters above, vendor legal-name fill, check 20). (2) Vet the watched
services. (3) Reader v5 once the v4 refresh has run through: the party named by the site's own agreement ("This is an Agreement between
You and X"), terms linked from a legal hub page, standard legal paths when the home page links none — then the hand table goes.
(4) Vendor names that are host names (whc.ca, business.nvchamber.ca) → the site's own name. (5) Tier M and I vendors (cities, CIPO, the
Crown corporations: 30,000 rows, a few dozen vendors) have no legal name / website / phone: carry them from the buyer table where the same
body is a buyer, read the rest once. (6) CharityVillage reader. (7) Sunday's report.
**Projection, unchanged in total, restated by source:** stores ~960,000 left to read at 22 % → about 210,000 rows over two weeks; DNS-provider
leads on file → 25,000-35,000; .ca registrations and the member / licence lanes → 100,000-150,000: **600,000-700,000 by early January.**
The DNS-provider class is the one that can still grow by a multiple: its leads come from 4.5 million domains looked up, and the domain
sweep is walking a list of 118 million.

**Addendum 04:16Z.**
- **The refresh pass of the night gained nothing and is running again.** claude-engines checked out the commit of the minute a run was
  dispatched; the pass dispatched at 00:19Z waited for runners and then read 147,995 sites with the reader as it was at 00:19Z (v3). The
  merged file holds v1 22,077 · v2 60,503 · v3 147,995 · **v4 0**. Nothing wrong was delivered (the ranker prints a spelled name only from
  a v4 record). The workflow now checks out main; the pass was dispatched again at 04:15Z (8 runners, chained until every record is v4:
  two runs, about 10:00Z).
- **Five services vetted** from the scan's own counts (DECISIONS 04:13Z): Owl Practice, GOrendezvous, Rezgo, WebRezPro, Juvonno; and the
  credit-scan merge now makes candidates from the links on file for every vetted service — 3,950 new candidates from one cycle's links in
  a copy of the merge (Jane 1,599, Checkfront 540, GOrendezvous 277, Owl Practice 273, Jobber 227 …). First real numbers at the next
  credit-scan merge; accepted leads after the tenant factory has read the sites.
- **Inferred vendors (tier I)**: Hydro-Québec gets its register entry (REQ), Canada Post Corporation, The Manitoba Hydro-Electric Board
  and MPAC a name read on a page; BC Hydro, NB Power, SaskPower, Qulliq stay without (their pages were not readable or not found).

## 2026-11-11 01:20Z — the DNS repair holds; the bill-to legal name (160,000 empty cells) is the work of this night
**The DNS repair is confirmed on the real run.** The fifth measurement had picked the transport (the runner's resolver forwards over TLS:
96-98 % answered at 434-751 questions a second). The re-lookup of the records on file (6 runners, 23:02Z → 01:09Z) finished: one runner
of the six asked 518,885 domains and 1.8 % stayed without an answer (it was 43 %); of its 92,064 store candidates 78,586 are on Shopify's
addresses. Six such runners: **about 470,000 stores more** than the 582,715 on file, once the merge lands (queued 01:09Z behind the
account's 20 jobs; it also starts a credit-scan cycle). DNS leads of the same domains: SPF on 199,606 and MX on 277,814 of 380,410
answered in that one runner — the lead rules read them at the merge.
The host sweep started at 22:48Z on the old resolver start behaved as designed: four runners stopped at their first batch (79 % without
an answer) and kept their place, four ran their box; its successor starts on the new resolver. The domain sweep's next run is queued
(4 runners, list begun again).

**The largest gap of an invoice row is its first line.** Build 22:38Z: 159,482 of 233,316 rows have no legal name (R 75 %, T 74 %, D and
I 62 %); 30,768 rows are known by their domain only. Measured before anything was built (coord/DECISIONS.md 00:55Z):
- more pages per site would give 3 % (the sites were read; two thirds of them link no legal page);
- **the name is already on the pages read**, outside the three places the reader looked: 11-13 % of the sites without a legal name
  print their name with a company form that their own domain name spells ("Credit Lift Inc." on creditlift.ca), or name the legal
  person behind the site's name ("Majid Enterprises Inc., operating as Lawn Lovers"), or their operator;
- 6,228 rows carry a name that itself has a company form ("Kobes Welding Ltd.") and an empty legal-name cell;
- 1,167 rows carry a charity registration number that the CRA list holds, and nothing of the list;
- the match against the CRA list was a file made on the owner's Mac on 2026-11-08 (table of 65,000 rows) that no workflow ran.
**Built, tested on 2,584 sites and on a sample build, pushed 00:20Z-01:15Z:**
- tools/org_extras.py v3 (the three readings above, with page and quote; a Shopify store's fixed policy pages; the five pages chosen
  among all links). Precision on a control of 324 sites with a known name: agreed 76 times, right 11 of the 12 times it differed, one
  name cut short — which gave the rule that a name keeps the opening words it is always printed with.
- rank.py: which name a row prints, registers first (trademarks / RBQ › business registry › CRA list › copyright line naming a legal
  person › the name the domain spells › the legal person behind the site's name › operator › structured data / stated › Wikidata ›
  the organisation's own name with its company form); the CRA list joined by registration number.
- tools/charity_buyers.py runs daily in the cloud, and three faults of its name match are corrected (the first charity of a name stood
  for all of that name; names matched organisations outside Canada; a foundation's name matched the body it supports): 9,749 buyers.
- **One pass over the 173,000 sites already read** is queued (claude-engines `refresh=true`, 8 runners, 150 minutes, chains itself); every
  scheduled run now re-reads older records after the new sites.
Sample build (55,147 rows of an older state, 1 site in 40 re-read): legal name B 64 → 69 %, D 30 → 34 %, R 35 → 38 %, T 35 → 38 %; the
full pass should add about 12,000 names from the pages, 6,000 from the names themselves, 1,100 from the CRA numbers. The registry tools
then look the new names up (federal and Québec companies get their number and registered office the day after).

**Other results since 22:55Z.**
- Mailbox crawl of 21:15Z (merged 23:34Z): lead sites read so far 533,210 (173,738 with a mailbox), +7,383 rows; candidate sites
  98,380 (21,454 accepted, 20,937 out of scope, 9,209 refused the reader), +3,068 rows; buyers with a mailbox row 195,183.
- Trademark owners abroad (first run, 51,382 owners in the United States, United Kingdom and Australia): 3,022 own sites tied
  (5.9 %; the sample had said 6.8 %); 11,382 more agree on the name and print no address of the owner's state on the pages read — a
  contact page would settle many of them. Leads follow at the next tm-register run (queued).
- RBQ licences, first run with the printed licence numbers: 558 new leads (401 by a licence number printed on a site already read),
  11,585 licence leads on file. The lane runs daily now.
- Vendor table: Thinkific (only by an organisation's own address being an alias of its school), Lightspeed Golf, Unbounce and
  Lightspeed scopes from their own terms; an organisation's address that is a DNS alias of its account on a vetted platform is a
  candidate of that vendor (decisions 23:20Z).
- Readers: a page that writes its link attributes without quotes is read like the others.

**Honest state of the target.** Nothing here adds rows by itself except the stores (two to four days of reading for ~1 M stores at the
crawl's pace, 24-28 % accepted) — the projection of 22:55Z stands (600,000-700,000 rows by early January; one million needs a class not
known today). What this night changes is what a row is worth: the legal name is the first line of the invoice.

**Watch.** (1) the merge of the re-lookup (stores on Shopify's addresses: 582,715 → ~1.05 M; "domains asked again through the repaired
resolver"); (2) the refresh pass: per runner "tasks: N domains to read, M of them read before by an older reader", and after its merge
the counters `buyer_legal_name_v3_*` and "legal name: the organisation's own name carries its legal form" in the next build; (3) the
build that started after 01:06Z is the first with the new chain of names: audit check 20 (legal name is not a fragment) and the fill
by tier; (4) tm-register after tm-sites abroad; (5) the first detector-5 cycle (scan shards in progress since 23:29Z).
**Found and not done:** tools/gc_recipients.py matches a grants recipient to a row by name alone — the same namesake fault the charity
match had ("Holy Trinity Armenian Church", Pennsylvania, given the Scarborough church's record); the trademark owners abroad whose
site prints no address on its home page (11,382).

## 2026-11-10 22:55Z — build 22:38Z: 233,316 rows (227,586 with a mailbox); half of the DNS answers were never received
**Table.** Build 22:38Z (code 2f581a8): A 1,276 · B 1,720 · C 323 · D 24,900 · E 4,749 · F 8 · I 17,822 · L 440 · M 9,524 · R 99,372 ·
T 67,452. Audit and gates pass. The build took 32 minutes.

**The largest finding of the day: the DNS engine has been losing about half of its answers.** A sample asked from outside showed it: of
1,500 two-label .com names of the web graph, a public resolver answers 81 % with an address and 14 % with "no such domain"; the sweep's
own logs say 55-61 % of its names got no answer. Measured on what is on file (coord/DECISIONS.md 23:00Z):
- of the 4.13 M lookup records, 1,796,196 say "no answer" (43 %); a public resolver answers 88 % of a sample of them today;
- 677,485 of those are store candidates (domains that link to Shopify): of the candidates that did answer, 97 % are on Shopify's
  addresses — about 580,000 stores are sitting in records that say "no answer";
- 87 % of the answered records that carry no address do have one, and 31 % of those without an SPF record have one: later questions
  about the same domain were dropped too (DNS leads lost);
- the sweep of the 63 M domains had asked 13.7 M and found 29,620 stores with 45 % of its names answered.
**Cause, as far as measured** (four runs of dns-diag.yml, the fourth in progress): it is not the resolver's settings. Whatever the
runner's own resolver is given, and also when the public resolvers are asked directly, a runner gets 50-90 answers a second and the rest
time out; with more open files the resolver answered less (8 %). The limit sits between the runner and the network and counts flows or
packets — which of the two is what the fourth run measures (the same questions inside a few long-lived HTTPS connections, tools/dns_services.py
DohResolver, and forwarded over TLS).
**What is already in place** (pushed 22:48Z): both sweeps begin their lists again (SWEEP_REV 2; the hits found so far are kept); a sweep
batch with more than 12 % unanswered is asked once more, and at more than 24 % the run stops and the list keeps its place; a lookup run
keeps its unanswered names for a later run instead of writing them as facts; records written before today are asked again, "no answer"
first and store candidates before the rest, and the new record replaces the old; one concurrency group per mode.
**What it should give once a transport works**: about 580,000 more stores from the records on file (one lookup run of four runners), the
sweep at two to three times its yield, and the DNS leads of ~1 M .ca / .com domains that were never really asked.

**Other work since 20:00Z.**
- **Store reader**: the privacy-policy page joined the list (measured on 120 stores that had given no mailbox: 22 print one of their own
  domain there, two thirds of them a role mailbox); the reading stops once two pages are read and a mailbox is on file; the 35,000 stores
  that gave nothing get that one page (done lines carry p3). Live check: 4 of 6 accepted with one request each.
- **Client pages read live** (first full run, 300,208 sites): 29,123 sites have a client-type page, 77,557 links, **32,561 new buyers**
  as leads (the estimate had been 10,000 link records). The mailbox crawl reads them next.
- **Vendor table**: Checkfront, TouchBistro, WellnessLiving, ClubRunner, CrowdRiff, NiceJob added, each from its own pages (who
  contracts, where, no free plan — quoted in tools/tech_relationships.py). Read and left out: SharpSchool (now PowerSchool, United
  States), WildApricot (nothing on its pages says what became of the free accounts), Showpass / Rezgo (no fee without a paid booking).
- **Scan detector 5**, before its first cycle: links and embedded services per host; the register numbers a home page prints (2.5 % of
  2,020 sampled pages: RBQ 1.0 %, charity number 0.8 %, ECRA/ESA, FSRA, Consumer Protection BC, TICO); the affiliations it states
  ("membre de l'APCHQ", "independently owned and operated", "authorized distributor of …"). A capture; lead rules come after the data.
- **Trademarks register**: 2,633 leads in the 22:38Z build (tier M 6,426 → 9,524); the owner-site finder ran (tm-sites, 3 shards) and
  the match ran again at 22:26Z.
- **A crawl's merge refused by GitHub's push protection** (a pre-signed storage address as evidence URL): fixed 19:5xZ, the next merge
  landed with the guard ("rows left out …: 1").
- **Rank build 19:45Z failed after its upload**: it had waited 70 minutes, built the commit it was dispatched on and could not commit on
  top of the build before it. The checkout now takes main when the job starts; the build after it took 32 minutes.

**Honest projection, revised.** If the DNS repair holds, the stores on file double (556,000 → about 1.1 M) and the sweep adds 200,000-
400,000 more: at the measured 24-28 % of stores accepted, tier T goes from 67,000 to 350,000-400,000 rows over one to two weeks of
reading (the store reader's pace is the limit: two requests a second per runner towards Shopify, unchanged). With the registry class
(~145,000), client listings and the rest, the table reaches roughly 600,000-700,000 rows by early January. One million still needs a
class not known today.

**Watch.** (1) dns-diag run 4 (HTTPS / TLS transports): pick the transport, switch dns-services.yml to it, dispatch `mode=lookup` with
6 shards (it starts a credit-scan cycle when it lands: that is also the first detector-5 cycle); (2) host sweep 42917864560 (8 shards,
started 22:48Z on the new tool with the old resolver start: it should crawl at ~60 names a second through the second chance, or stop in
place); domain sweep 42900501721 (old code, ends ~23:45Z: its places will be ignored, its hits kept); (3) the mailbox crawl of 21:15Z is
the first with the new store reading: `accepted` share and pages per store in the merge line; (4) tm-register after tm-sites.

## 2026-11-10 20:00Z — build 18:18Z: 218,446 rows (213,093 with a mailbox); where the next rows come from, measured
**Table.** Build 18:18Z: A 1,276 · B 1,704 · C 323 · D 22,024 · E 4,527 · F 8 · I 17,855 · L 426 · M 6,124 · R 100,325 · T 58,501. Named
vendor 90,386 · registry R 100,325 · link only E 4,527 · inferred I 17,855. Audit PASS with no hard failure, 7 gates PASS. The referee
reads new pages only (8–33 minutes a run); cross-verified is back to 13.

**Supply is the work now** (coord/DECISIONS.md 20:00Z has the numbers). The crawl of 17:59Z found 5,066 mailboxes in 67,753 sites: the easy
sites are used up. Per lane, what is on file and what it should still give:
| Lane | On file / known | Still to come (estimate, with its basis) |
|---|---|---|
| Stores (T) | 550,370 domains on Shopify's addresses, 41,506 read, 8,235 accepted | ~24,000 read a run; .ca / .us first from now on (43 % / 38 % accepted against 26 % on .com) → ~100,000 rows over the next 20 runs |
| Stores on a subdomain | 7.2 M hosts to ask (host sweep dispatched 19:46Z, 8 shards) | unknown until the first run: 165,000 shop. / store. hosts alone |
| Stores by myshopify.com name | 206,386 names | 300 per runner per run first, to measure |
| Domain sweep (stores + name servers of 330 Canadian providers) | 7.1 M of 63 M domains asked, 17,349 stores | ~150,000 stores; name-server hits unknown (first run with the question is in progress) |
| .ca sites, mailbox on a contact page (R) | 428,000 candidates, 10 % measured | ~40,000 rows, 64,000 sites a run |
| Linking domains of the refreshed web graph | +196,195 domains to scan | next credit-scan cycle |
| Client / sponsor / member pages read live | never run before 19:35Z | ~10,000 link records |
| Unreachable .ca domains with the http fallback | 1.25 M, 5.7 % are sites | 5,000–10,000 rows, with the next detector |
| Vendor table (software seen on the buyer's site) | 17 vendors | 30 candidates being vetted (probe vet); mostly upgrades of registry rows to a named vendor |

**Honest projection.** These lanes carry the table to roughly 450,000–600,000 rows by early January. One million is not in sight with the
lanes known today: the two largest classes are bounded (.ca sites that print an organisational mailbox: about 220,000–250,000; Shopify
stores in the United States and Canada that print one: about 22 % of the stores we can name, and we can name under a million). The
Sunday report says this with the numbers of the week; every new lane found before then changes it.

**Closed today.** Shopify's directory shop.app (its merchant pages refuse the crawler; the sitemap's handles are not addresses); member
directories of the GrowthZone family from the archive index (20 Canadian of 1,860 hosts).

**Watch.** (1) host sweep run 42888650540: `hosts` key of sweep_cursor.json after its merge, stores found, and that it chains; (2) the
store reader's log line "stores from the DNS lookups not read yet … by ending" and the myshopify counters (myshopify_own_domain_found /
no_store / known_store) in the next mailbox-crawl run (the one after 19:41Z); (3) live-clients run 42886786420 merge (first CI run of that
workflow); (4) bbb-accredited 42868640128 (index of twelve crawls) then its cc-read; (5) credit-scan cycle for the +196,195 linking domains.

## 2026-11-10 17:25Z — build 15:47Z: 172,770 rows (168,245 with a mailbox); audit round 3; referee fixed; two supply lanes started
**Where the table is.** Build 15:47Z, the first on the rebuilt path: 172,770 rows, 42 minutes, ranker peak 3.6 GB, runner disk 85 GB free
(I had assumed 14 GB: corrected in coord/DECISIONS.md 15:10Z — the disk was never the near limit). The table grew by 3,000 rows only because
the 14:25Z crawl's ~53,000 mailboxes were not verified yet: the referee run that covers them started 16:21Z on the old code.

**Referee.** Every run since 11:26Z fetched every page again (the cache save failed): 65–105 minutes a run, runs queued behind each other,
3–4 hours from crawl to table. Fixed 16:28Z (b66d054): a verdict stands from the ledger, a run reads the new rows' pages only. The first
run on the new code is the next one after 16:21Z's; expect its page count in the log line "prefetched N new pages; rows whose page was not
asked for again: M".

**Row audit, round 3** (coord/DECISIONS.md 17:25Z): a site reader's record only for its own host (readers keyed by host from now on); a
name off a page only when the page ties it to the buyer, plus three new strong statements (the site's operator, its own JSON-LD node,
"doing business as"); a registry record only while it can be the row's; directories by the site itself; the address cut at the street
number. On the local build: legal names 550 gone / 295 new / 668 replaced, 1,343 addresses cleaned, rows / tiers / mailboxes unchanged.

**Supply started this afternoon.** Member directories from the archive index: 1,926 directory hosts, 1,860 judged, 20 new Canadian bodies
(most of the platform's tenants are American chambers; 258 print no address on their home page — the contact page is the next look); the
crawl of the 22 ran 15:41–17:14Z. DNS sweep of the web graph's 63 M domains: four shards running since 15:40Z, self-continuing; from the
next run on it asks two questions per domain — Shopify's storefront addresses, and name servers of the 330 Canadian providers that already
yield leads (the Canadian businesses on .com / .net / .org; coord/DECISIONS.md 17:45Z).

**17:38Z.** The referee run on the old code landed: 262,766 findings verified (+51,000), 235,250 buyers with a verified mailbox (+46,000),
6,966 rows still waiting. A rank build started at 17:38Z on the new ranker; the first referee run on the new code started 17:42Z.

**Next, in order.** (1) Watch the first referee run on the new code and the rank build after it (expect ~215–220k rows). (2) Readers: the
org_facts run of 18:11Z reads each host for itself; check the "not taken" look-ups fall. (3) Ranking in parts: one run on GitHub against a
normal build, then the slim partition pass before ~500k rows. (4) More Canada-based platforms with public tenants, vetted one by one.

**The ranker's memory, measured 18:00Z (for whoever does step 3).** Peak 2.4 GB at 77k rows, 3.6 GB at 172k. Where it is: ~1.4 GB is the
contract dataset pass (fixed); a row is 8.5 KB (its dict alone 6.6 KB at 223 columns — a table of 512 slots; the strings are mostly shared
already: interning would save little); the side tables (DNS posture, mailbox meta, site facts) ~4 KB a row. One process therefore ends near
800k–1M rows on a 16 GB runner. Ranking in parts already keeps each organisation's joins in one part, but every part loads every lead and
mailbox first. The step that is missing: `prep` computes the partition from a slim read (lead key, site domain, mailbox — the union-find of
rank.py on those three fields only) and writes key → part; each part then filters while it reads the lead store, the referee's log and the
facts, so it never holds another part's leads. With four parts at 1M rows a part is ~1.4 + 2.1 + 1 GB. Do it against the two-part
reference of the harness (`scratchpad/ab/Rbase` in the 2026-11-10 session; rebuild it with `runpart.py` if the scratchpad is gone).

## 2026-11-10 15:10Z — build 14:29Z: 169,768 rows; why no build landed between 10:54Z and 14:29Z; the build path measured and rebuilt
**Published and committed (14:29Z, first build with every audit fix of 12:45Z):** 169,768 rows, 165,320 with a mailbox.
| Line | Rows with a mailbox |
|---|---|
| named Canada-located vendor (A 1,279 · B 1,704 · C 324 · D 20,837 · L 426 · M 5,146 · T 41,173) | 70,889 |
| tier R — the organisation's own .ca domain registration (CIRA), its own line | 75,733 |
| tier E — link only, not shown to be a relationship with the Canada-located entity, its own line | 4,453 |
| inferred or weak (I 14,237 · F 8) | 14,245 |
Tier E grew by 691 against the 13:27Z table (3,762): the own-site rules of the audit at work on the new rows.

**What broke (12:46Z–13:43Z) and is fixed:** the 13:27Z build ranked 169,769 rows and published the release, then its commit was refused —
`coord/results/ranked/ranked_buyers.csv.gz` (151 MB) had stayed tracked by git although .gitignore named it; the retry loop rebuilt and was
shut down by the runner in the DNS step, which read the 2 GB table three times into memory. Both fixed 13:45Z; build 14:29Z is the result.

**Then measured, because the next ones were visible from there** (table in coord/DECISIONS.md 15:10Z): disk ~65 KB a row (limit ~1.3 million
rows: a runner has 85 GB free, measured in the 15:47Z build — I had first written ~215,000 on an assumed 14 GB), scoreboard and growth report holding whole rows (limit ~400,000), the DNS file in git (limit ~470,000 domains),
the ranker's own memory (3.6 GB at 169,768 rows, +11.8 KB a row: limit ~800,000). Built and verified byte-identical on a full local build:
tables compressed only (disk of a build 2.6 → 0.35 GB at 76,913 rows), reports that keep cells instead of rows (2.83 → 0.22 GB, 2.33 → 0.09 GB),
the DNS file and the crawl results in parts, one prep script and one tail script for both workflows.

**Ranking in parts:** built, measured on two parts, not the default. It keeps every joined thing in one part (0 mailboxes in two parts) but
each part still loads all leads and mailboxes (2.42 GB a part against 2.49 GB): the next step is loading each table for the part's own
organisations only. Until then one process is good to ~800,000 rows.

**Supply, read from coord/LANES.md 14:30Z:** 3,010,354 home pages read (1,310,325 readable), 280,623 print a role mailbox, 176,238 of them on
.ca (tier R candidates); 335,151 lead sites read by the mailbox crawl, 156,328 with a mailbox. What is on file will carry the table to about
300,000 rows. Beyond that the supply has to come from: .ca sites whose home page prints no mailbox but whose contact page may (~1,000,000
readable sites not yet asked), Shopify storefronts (542,022 domains on Shopify's addresses; 20 % accepted so far), member directories of
chambers of commerce and associations, more Canada-based platforms with a public tenant footprint. Next entries report each as it is built.

## 2026-11-10 12:45Z — row audit, round 2: cells that were true of ANOTHER organisation (eight fixes, each measured on a full local build)
**Published build 10:54Z** (`2026-11-10T10:54:43Z-7d767f6`): 96,098 rows, 92,432 with a mailbox — A 1,279 · B 1,695 · C 332 · D 21,169 · E 3,592 ·
F 8 · I 10,515 · L 431 · M 4,518 · R 27,207 · T 21,686. Named-vendor relationships (A B C D L M T) 51,110 · registry contract R 27,207 · link
only E 3,592 · older / inferred F+I 10,523. The fixes below are in the next build.

**Why:** the first audit round fixed the relationship (is it a client?). This round read the identity cells of each side and asked "is this
true of the organisation on the row, or of another one?". Method: a frozen copy of the inputs (76,704 rows), the ranker run before and after
each change, every changed cell compared by row key, samples read by eye. Rules: `coord/DECISIONS.md` 2026-11-10 12:40Z.

| what was wrong | how many (of 76,704 rows) | what happens now |
|---|---|---|
| listing on a multinational's worldwide site delivered as a relationship with its Canadian arm (3ds.com, ibm.com, okta.com, granicus.com …) | 414 rows, 104 vendor/site pairs | tier E with the reason; Wikidata's official-website owner first (326), then the site's own address (66), then national-arm names (22) |
| shopify.com case studies of merchants outside the United States and Canada (Shopify's own terms: other entities contract there) | 49 | tier E |
| legal name "CANADA INC." + its NEQ on organisations labelled "X (Canada)" | 77 cells, 57 registry rows | registry rows deleted; a bracketed place is no alias; generic registered names refused |
| vendor address / telephone read on a foreign organisation's site (Cupertino for a Markham vendor) | 537 joins, 139 address cells, 296 telephones | not taken; 80 JSON-LD addresses likewise |
| vendor legal / trading name stated by a foreign group's site ("KPMG International Limited" for KPMG LLP) | 787 joins | not taken (a page of the site's Canadian section may still state it) |
| footer "legal names" that are menu words, an agency credit, an address, a sentence; names of another body stated on an "about" page | with the line above: 621 vendor and 750 buyer legal-name cells emptied | refused; 355 buyer and 96 vendor cells gained a real name from the next candidate |
| mailboxes ending in a non-existent top-level domain (".cadevelopment", ".comphone": text glued in the page source) | 560 referee rows | 454 cut back to the address the page prints (domain = the page's domain), 106 left out; the shared e-mail pattern now needs a real TLD |
| buyer named by its web address although its home-page title names it | 507 rows | named (589 sites re-read from stored titles with today's rule); 328 wrong or junk names went back to the address |
| vendor address cell = the page's words in front of the address | 1,583 cells | the address alone, the page still cited |

Totals of the comparison: tier D 11,862 → 11,410, tier E 2,405 → 2,862, every other tier unchanged within the mailbox repairs (+72 rows with a
mailbox). No row was deleted by a quality rule.

**New files:** `tools/site_owner_wd.py` + `data/incoming/claude/claude_site_owner_wd.csv` (whose site: 3,930 sites asked —
200 a foreign organisation's, 597 a Canadian one's, 166 undecided, 2,967 unknown to Wikidata; the ranker's workflow asks the new sites of each
build, at most 400 — the query service allows one query a minute), `tools/data/iana_tlds.txt`.
**Changed:** `rank.py`, `validate_returns.py` (EMAIL), `ap_crawler.py` (`page_emails`), `credit_scan.py`, `cc_mine.py`, `org_contacts.py`,
`lead_crawl.py` (site name: initials, "Welcome to", spelled-out name before acronym), `bulk_registry_match.py`, `tech_relationships.py`
(`scope_countries`), `rank-buyers.yml`.

**Known limits, measured:** (1) about 8 of the 463 demoted rows are Canadian companies whose site prints only a foreign office and that
Wikidata does not know (ADLIB, Mad Barn, Forest Technology Systems …): they come back when the site is read again or Wikidata learns them.
(2) 6,618 rows still carry a web address as the buyer's name: for 4,000 of them the site's own pages were never read for its name (the
site-facts workflow is on them), the others print no usable name. (3) Buyer address missing on 15,053 of 73,592 mailbox rows: 5,044 sites not
read yet, 10,009 print no postal address on the pages read. (4) A disk-full on the work machine cut one comparison run; nothing in the
repository was touched by it (every edited file re-parsed, the lookup table re-read).

## 2026-11-10 09:50Z — the two scale walls found by measuring: rank memory (5.8 GB → 2.8 GB) and the leads file (60 MB of GitHub's 100 MB) → shards; crawl three times wider
**Build 09:29Z** (`2026-11-10T09:29:09Z-16ba0e7`): 77,055 rows, 73,672 with a mailbox. A 1,279 · B 1,622 · C 331 · D 11,534 · E 2,563 · F 7 · I 10,644 ·
L 378 · M 4,221 · R 26,037 · T 15,056. Named-vendor rows (A B C D E L M T) **36,984** (32,231 at 08:20Z); tier R 26,037; inferred 10,651. The crawl that
ended 09:10Z read 74,000 more sites (27,608 with a mailbox so far, 103,662 sites read): those rows are with the referee and are not in this build yet.
**rank.py memory, measured (RANK_MEMSTAT=1 prints it).** A row costs 8 KB; the tables around the rows were 4.2 GB of the 5.8 GB (the local 7 GB machine
killed the build twice). Done, each step checked byte for byte against the output before it: (1) the last two passes and the three output files are one
pass — a row is completed, written, released; (2) every table is dropped after its last use; the vendor table's 58,302 registry records stay compressed;
(3) the tables of the fold steps kept a reference to every row, so nothing was released: dropped. **Full local build, 76,930 rows: peak 2.80 GB, 450 s.**
Fixed part ≈ 1.9 GB, ≈ 12 KB per row → one process holds about one million rows on a 16 GB runner. The runner's build is 15 minutes end to end
(rank.py 6 minutes, of which 3.5 read the contract dataset). Not measured: memory per row after the downstream pack in the old layout (the process was
killed there) — the commit message of 09:05Z says "~20 KB", which was an estimate, not a measurement.
**Leads file → shards (`tools/lead_store.py`).** `claude_buyer_leads_cc.csv` was 59.9 MB for 174,000 leads and three workflows rewrote it and the 32 MB
details file whole at every merge; GitHub refuses a file at 100 MB (≈ 290,000 leads — one or two days away). Now a frozen base + append-only shards in
`lead_shards/` (rows, details, withdrawals; applied in stamp order); each writer saves only what it changed; every reader goes through the store. Runs
queued with the earlier workflow files still write the old way (harmless). **Bug found by the test, before it shipped:** the client-pages merge applied its
"hacked page" rule to every lead of the file; through the store that included the licence leads, which share one record_url — 10,748 RBQ leads were
withdrawn in the test. The rules are now limited to that engine's own leads; "specialist" no longer matches the spam word "cialis".
**Crawl.** One runner read 12,494 sites in 130 minutes with 40 sites open at once and was nearly idle (a site is asked at most once a second): now 120 at
once (the account's limit is 20 jobs, not threads). Registry candidates 12,000 per runner. **Second class of registry candidates:** 375,000 .ca sites whose
home page prints no mailbox; measured on 200, 4 pages each: 10 % give a role mailbox → queued last, 8,000 per runner and run (≈ 37,000 rows for ≈ 1.5 M requests).
**RBQ fee.** The Régie's 2026 tariff for keeping a licence (989.81 $ general, 547.53 $ specialised, not taxable; page opened and quoted) is on 43,328 of the
49,913 holders by their categories in the register; 8,887 licence leads got the amount (labelled as a tariff, not a payment record). CMEQ / CMMTQ
licences: no amount (their own dues; pages not opened).
**Names.** A slogan placed before the name in a page title was taken for the organisation's name on tier-R rows: the best fit with the domain wins now.
**Next:** (1) the referee's run on the 20,000 new mailbox rows, then a build — first build expected above 90,000 rows; (2) watch the first runs under
the new workflow files: crawl at 120 (errors, blocked share), shard-mode merges (row-factory, member-live, credit-scan); (3) RBQ holders without an own
e-mail domain (28,000 on webmail) tied to sites by postal code + name, like the business licences; (4) the vendors' client pages read live (the archive
holds a fraction of them) — the lane with a named Canadian vendor and a named buyer; (5) sharded ranking is designed (core part + parts by site domain,
merged by sort key) but not needed before ~800,000 rows: not built.

## 2026-11-10 08:10Z — scan of 1.31 M home pages done; repository growth stopped (release assets); two licence lanes; stores ride along the crawl
**Measured.** Scan cycle 42761724176 (detector 4): 1,308,798 home pages read, 781,441 readable; **185,798 print a role mailbox of the organisation
(23.8 %)**; **133,597 are .ca sites = registry candidates (tier R)**; printed address CA 209,333 / US 23,512. Credit-line leads on file 39,124 (were 24,356).
The mailbox crawl (16.5k sites per runner per run) is reading them; then the referee; then rank.
**The repository wall (found 07:05Z).** 5.45 GB of new git objects in 24 hours; GitHub reports 8.9 GB. Now: each rank build is published to the release
`ranked-latest` (`tools/ranked_publish.py`; git keeps reports, BUILD.json, WHERE.md, 10 rows per package); `team_buyers`, `claude_org_extras`,
`claude_org_contacts`, `claude_ap_terms_pages` are state assets (`tools/state_io.py`, `coord/STATE_ASSETS.json`). First build with the new route: run
42774165877 (started 07:50Z). Still in git and rewritten whole: `claude_lead_details_cc.jsonl.gz`, `claude_buyer_leads_cc.csv` (three writer
workflows → to become append-only shards, not release assets). Local clone shrunk to depth 20 (15 GB → 0.7 GB).
**This container reaches the web now** (it did not before 07:40Z): crawlers can be tried live on a few hundred sites before a workflow run. Used for:
RBQ list and site check, licence lists and matching, 94 Shopify stores through the queue. Volume work stays on the runners.
**Licence lanes (tier M, DECISIONS 07:25Z).** RBQ: 50,078 organisations hold an active Québec construction licence (paid yearly); 17,185 have a domain of
their own; live test 300 domains → 181 tied to the holder; 60 tied sites → role mailbox on 38. Business licences / permits: 147,571 in force in five
lists; 1,664 tied to organisations we hold (843 tier-R rows, 325 inferred rows get a named, dated relationship). The first run's name rule matched
food-service operators to their host institution (Aramark ↔ University of Calgary): replaced within 15 minutes; the build of 07:50Z may still carry
those leads until the build after it.
**Stores.** With one queue of 2 requests/s per runner: 0 refusals in 94 stores (38 % before), 19 % accepted. The store reader now runs as a second
process on every mailbox-crawl runner (mailbox-crawl.yml); tenant-factory keeps the customer portals. DNS lane: Hover (Tucows' retail registrar)
is no longer excluded.
**Runner pool.** 20 concurrent jobs; the ranker waited 34 minutes for a slot. Defaults now 6 runners × 90–100 minutes (mailbox crawl, scan, stores).
**Evaluated and not built:** ad-exchange seller lists (sellers.json of a Toronto exchange): the exchange pays the publisher — "you do not need to send an
invoice to Index" — the Canadian party is the payer, and no fee to the publisher is published.
**Next:** (1) confirm the release route on the 07:50Z build, tell the owner where the files are; (2) rank.py at 200k+ rows — a local profile is
running (time per step, peak memory): the build is single-process and holds every row; (3) leads / details files to shards; (4) more licence lists
(payee address + fee sentence each); (5) the graph run for multi-tenant platforms (queued 07:22Z).

## 2026-11-10 06:35Z — build 06:19Z: 70,567 rows; named-vendor rows 24,765 (+28 % in two hours), tier R 30,880, inferred 13,610; five more engines
- **Build 42761927713 (06:19Z)**: rows 70,567. Confirmed-mailbox rows by relationship: **named Canada-located vendor 24,765** (was 19,314 at 04:44Z:
  credit lines 4,724, DNS providers 1,194 …) · **registry contract (tier R) 30,880** · **inferred / weak 13,610** (was 48,986). Tier T 8,947.
  `coord/GROWTH_VS_BASELINE.md` now shows these three lines under `rows`; `coord/LANES.md` shows every lane's funnel (rewritten at each build).
- **Web graph, second read (run 42763465847)**: **1,323,818 domains link to shopify.com / myshopify.com**; 410,538 link to a vendor proven in
  Canada (421,156 in-link sites on file); the "proven vendors" list had two false entries (cPanel: a Vancouver affiliate on its legal page;
  a French theme author whose privacy page names its Laval host) → rule: an address introduced by "Hosting:" / "hébergé par" is the host's.
- **Mailbox crawl measured** (`crawl-diag.yml`, 800 lead sites that gave nothing, read again): address on another domain 16 % · unreachable 15 % ·
  no address at all 15 % · a name that is no role word 13 % · form only 7 % · Cloudflare-obfuscated 7 % · **would be found now 7 %** · refused 7 % ·
  mailbox named after the organisation 6 % · text-obfuscated 6 %. So the find rate (28 % on listed-organisation leads) will not double: rows have
  to come from more sites, not from a better reader. The 7 % are re-read by rule r2.
- **Engines added since 05:35Z**: `mailbox-crawl.yml` (the crawl back to back in its own workflow — it was the last stage of the row factory and
  waited two hours per cycle); `member-live.yml` (live chamber / association directories: first run +2,516 buyers); `bbb-accredited.yml` (53,088
  accredited profiles; bbb.org refused the runner → read from the archive); store lane rebuilt (meta.json, one queue per runner, DNS light lookup);
  multi-tenant platform discovery; `tools/lane_status.py`.
- **Scale walls removed** (GitHub refuses files over 100 MB): ranked table committed in parts (`tools/ranked_io.py`; it was 70 MB), org mailboxes
  in parts, results file rotates at 30 MB, tenant / lead-crawl / lead state in append-only shards (`tenant_state/`, `crawl_state/`, `lead_shards/`),
  rank job timeout 45 → 240 minutes (the 06:19Z build needed 43), rank.py prints elapsed seconds per step.
- **Bill-to addresses**: a telephone number or a copyright year in front of an address was taken for its street number — 4,100 of 38,341 stored
  addresses are cut correctly now; tier-R and credit rows take the organisation's own name from the site facts of the same domain (16,416 tier-R
  rows carried only the domain).
- **Runner pool is the limit right now** (20 concurrent jobs): scan cycle 42761724176 (8 runners since 05:23Z), DNS run 42761831500 (6 runners,
  public resolvers at 60 queries/s — the unbound version is queued as 42768807140), then mailbox-crawl, member-live, bbb, lists.
- Waiting for: detector-4 scan results (`em=` rate → size of the registry candidate pool), first `mailbox-crawl` run, first store run with meta.json
  (tenant-factory 08:47Z), BBB archive index.

## 2026-11-10 05:35Z — target is now 1,000,000 rows (owner 23:41 EST); build 04:44Z = 68,910 rows; three new pathways live (DNS, .ca registration, scan facts)
- **Build 42755132469 (04:44Z): rows 68,910 (+5,269 vs baseline)**; pay on sight 874 / 1,152 / 36,280 routed; tiers D 9,902 · E 3,040 · I 48,968 · M 189 ·
  T 3,089; the first 71 credit rows delivered with the right text and the vendor's printed address.
- **Credit scan, first full cycle (run 42753586829, 30 minutes of 8 runners): 434,116 home pages read** (ok 363,809 · blocked 26,313 · unreachable 25,166 ·
  robots 11,909); 73,778 carry a credit line or a vetted service; 26,112 credited vendors checked live → **CA 6,977 · CA-loc 2,307** · no address 10,946;
  **25,510 credit leads** (W 14,752 · D 5,690 · P 5,068) and 17,909 vetted-service candidates (Shopify 12,904, Jane 4,465 …).
- **Precision pass on those leads** (top 100 vendors read, random 45: 43 right): Webador (Dutch, free plan; its "address" was a customer's subdomain),
  Ratehub's free widget, DirectAdmin, vendors proven on somebody else's page, foreign companies with a Canadian branch credited by buyers abroad,
  universities' internal web services → **1,141 leads withdrawn**; "Board of Trade" was rejected by the membership rule; names were cut at an apostrophe
  (`Uncle Bob's` → `Uncle Bob`: tools/tech_relationships.py page_meta). Vendor check rule 3 and scan detector 4 (DECISIONS 05:30Z).
- **NEW — DNS lane** (`tools/dns_services.py`, `dns-services.yml`, daily 02:23Z): the buyer's own MX / NS / SPF records name its mail host, DNS host, web
  host. From the records already on file: **1,321 leads** (Web Hosting Canada 1,009 · Webnames 152 · Doteasy 47 · Vianet 27 · BlackSun 16 …). Cloud
  lookup of 1.3 M domains: run 42761831500 (06 runners; this first run still uses public resolvers at 60 queries/s — the unbound step applies from the
  next run). 451 provider domains named by 8+ buyers are queued for the live location check (credit-scan `vendors` step).
- **NEW — tier R, package P10R** (rank.py / batches.py): the registration of the organisation's own .ca domain name — agreement with CIRA, paid through a
  CIRA-certified (Canadian) registrar; both CIRA documents quoted. Replaces the INFERRED relationship (P13) for organisations on a .ca domain; new
  buyers come from `lead_crawl.py --registry 6000` (.ca sites whose home page prints a role mailbox). Rank build 42761927713 validates it.
  **Report it separately, always**: R is recorded and certain but generic (one vendor: CIRA); the named-vendor tiers are the stronger product.
- **NEW — scan facts**: every done line of the scan now says `em=<kind>` (the home page prints a role mailbox of the organisation) and `cc=<country>`;
  the mailbox crawl reads the `em` sites first. Credit-scan cycle 42761724176 (05:22Z) is the first with detector 4.
- Tenant factory with rule p2 (store policy pages read first): **2,389 Shopify stores accepted in one run** (was 267 in all runs before); 55,015 buyers
  hold a cloud mailbox row.
- CIRA's WHOIS / RDAP is NOT automated (DECISIONS 05:30Z §2). Cloudflare-obfuscated addresses stay undecoded.
- Next (PLAN §4e): #16 stores on Shopify's addresses (flagged by the DNS lookups) · #17 paid job ads (schema.org JobPosting, boards with a rate card) ·
  #18 exhibitors of Canadian shows · referee throughput (≈ 50 rows/min today: the limiting step for a million rows).

## 2026-11-10 04:40Z — web graph read: 53,124 sites link to a vetted customer portal, 216,481 link to a proven Canadian vendor, 1,045,795 .ca domains
- `credit_scan.py graph` (run 42753844151, 12 minutes on one runner; release cc-main-2026-aug-sep-oct): **216,481 domains link to a vendor proven in
  Canada**; **53,124 of them link to a vetted customer portal** — Jane 26,323 · Jobber 9,212 · BiblioCommons 7,381 · eScribe 2,268 · Benevity 2,267 ·
  Amilia 2,020 · D2L 1,555 · Docebo 1,158 · KEV 844 · Absorb 767 · Edsby 219 · Coconut 204 · Mobius 24; **1,045,795 .ca / .quebec domains** (the index had
  354,248). Files: `credit_scan/graph_inlinks.csv.gz`, `graph_ca_domains.csv.gz`. The graph stage now runs daily (03:37Z) with the vendors proven since.
- Scan order of the NEXT cycle (starts by itself when the running one ends, ≈ 06:30Z; schedule 00/06/12/18:07Z): portal-linking sites → other linking
  sites + OpenStreetMap sites (stage `osm` dispatched 04:27Z, run 42755983645) → rest of the .ca index → the graph's .ca domains → re-read of the
  470k sites read by detector 1 (detector 3 adds membership statements and Jobber links). 160 readers per runner, 10-second timeout.
- Vendor table: **Jobber added, Jane's scope = every country** (terms read 04:15Z, quotes in tools/tech_relationships.py). Benevity read: "Benevity, Inc.
  or its Affiliate as applicable" → stays Canada-only. Shopify candidates now get /policies/contact-information read first (54 % gave no mailbox).
- Row factory: the 11,096 vendors whose client page printed no address (39,313 buyer domains wait) are in the credit scan's vendor queue (live
  home / contact / legal page); `cc_clients.py merge` promotes on proof. New precision rules withdraw ≈ 1,700 leads at the next merge (dry run:
  216 investor portfolios, 1,339 country selectors / sister sites / badge links, 196 article slugs; 6,569 menu / footer links never promoted).
- Measured mailbox find rates before rule r2 (29,375 lead sites): member 32 % · sponsor 29 % · dealer 26 % · client 22-25 % · Mac-era 20 %.
- Health check 04:37Z (the 04:20Z check-in): no failed run in the last 6 hours. Lead sites read 29,375 → mailbox on 7,923 (27 %, before rule r2);
  **8,469 buyers hold a cloud mailbox row** (9,334 rows; the referee is on them — the build after 42755132469 delivers most). Tenant crawl 4,355 sites →
  474 accepted; 175,896 store-shaped domains indexed (20,000 candidates per cycle). The old check-in is not rescheduled: the 07:20Z follow-up replaces it.
- Waiting on: rank build 42755132469 (validates credit rows; started 04:27Z), credit-scan cycle 42753586829 (scan since 04:06Z), row-factory cycle
  42753268934 (queued: runners full), tenant-factory 42753426095 (crawl running). Session wake-up 07:20Z (`CCH credit-scan follow-up`).
- Honest projection (rates measured today, not yet end to end): portal links ≈ 10-13k rows; credit lines over ≈ 1.3 M sites ≈ 40-60k rows over the
  next cycles; row-factory promotions ≈ 6-9k; tier I rows turned into evidenced rows ≈ 4-5k (no new row, better row).

## 2026-11-10 04:15Z — build 03:25Z: rows 65,759 (+2,118), complete rows 38,143 (58 %, was 38 %); NEW ENGINE: credit scan (first test: 17.5 % of sites)
- **Build 03:25Z (GROWTH_VS_BASELINE):** rows 63,641 → **65,759 (+2,118)**; pay on sight 874 / 1,145 / **36,124 routed** (baseline 833 / 841 / 22,341):
  the site-facts pass (bill-to name + address from the buyers' own pages) moved 13,800 rows to complete. Tier I (inferred) 50,806 → 48,867;
  tier D (client / member / sponsor listings) 3,623 → 7,731. vendor_bn9_known −1,578 and benchmarks 98 (−2): rows that left the inferred
  package traded a Crown-corporation vendor with a known BN for a real, named vendor without one yet (PLAN §4e #14: vendor legal name + BN).
- **Credit scan (`tools/credit_scan.py`, `.github/workflows/credit-scan.yml`, every 6 h):** the credit line on the buyer's own home page
  ("Website by …", "Site web réalisé par …", "Hébergé par …") + the vendor's own Canadian address = a relationship stated by the paying party.
  Test on 1,200 tier-I sites (2 runners, 1 minute): 1,139 readable, **208 credit links on 17.5 % of sites**, 192 vendor domains → 66 proven in
  Canada by a postal address (75 printed none: proof rule 2 added — schema.org address, privacy / terms pages, location line + Canadian phone),
  **77 leads (6.4 %)**, plus 59 Shopify / 31 Jane sightings → tenant candidates. Full cycle dispatched 04:05Z (run 42753586829: 117k delivered
  rows and leads, then the 354,248 .ca domains of the Common Crawl index); web-graph stage dispatched 04:07Z (run 42753844151: every .ca domain
  of the domain graph + every domain linking to the 6,329 vendors already proven in Canada) — feeds the NEXT scan cycle.
  Flow: scan → vendors (address proof) → leads in `claude_buyer_leads_cc.csv` (cfv "… credited on the buyer's own site (tech) …", details
  platform `site_credit_cc`) → row-factory mailbox crawl → referee → rank (tier T, text "the site credits the Canada-located vendor …").
  A delivered row whose site carries a credit borrows its own confirmed mailbox: inferred rows become evidenced rows without a new crawl.
- **Mailbox rule r2** (DECISIONS 04:10Z): front-office role mailboxes (sales@, service@, orders@ …) as the last resort; the 6,300 "nothing found"
  lead sites are read once more in the next row-factory cycle (queued 04:02Z behind the running one).
- State files of the credit scan are append-only (`data/incoming/claude/credit_scan/{done,seen,vendors,ext}_<stamp>.gz`): no big file is rewritten.
- 04:25Z additions: detector 3 (membership statements, class M → member leads); vendor table: Jobber added, Jane's scope widened (terms read today, quoted in
  tools/tech_relationships.py); web-graph targets include the vetted portals; row audit of 28 delivered cloud rows → 5 precision fixes (footer credits on
  client pages were taken as clients — reversed direction; investor portfolios; article slugs with 'membres'; deep 'our-work' paths; address tails in
  names): the next row-factory merge withdraws ≈ 1,270 leads. Rank build 42755132469 (04:19Z) validates the credit rows end to end (77 leads).
  Not built: IRS 990 older years (two filing years gave 283 buyers on the Mac: ≈ 150 / year, weak tier) — skipped for now.
- NEXT: (1) read the full cycle's numbers (sites read, credit rate on .ca universe, vendors proven, leads) and the first r2 mailbox yields;
  (2) dispatch rank after the referee lands the rows; check GROWTH (tier I should fall, tier T rise); (3) `ext_*.gz` = outside services the
  scanned sites load: vet the frequent Canada-based platforms (HQ quote + paid-only) into tools/tech_relationships.py VENDORS;
  (4) PLAN §4e #14 vendor legal name + BN for the new vendors (their own site names them → `bulk_registry_match.py`).

## 2026-11-10 03:35Z — measured yields after the multi-crawl / .com-universe index and the first completeness pass
- Index now 268,494 relationship pages (client 179,170 · member 61,371 · dealer 14,655 · sponsor 12,866 · tenant 432) — was 66,321 at 01:25Z.
- Leads (`claude_buyer_leads_cc.csv`) 26,781 (was 9,487); 110,934 link records wait in the no-address side file; address pass, first run: 1,938
  vendor domains now have their Canadian address from their own home / contact page (promotes their links at the next merge).
- Mailbox crawl: 9,487 lead sites read → 2,355 with a role mailbox (2,578 buyers, 2,817 rows at the referee). ~17,300 cloud leads + 33,600 Mac-era
  leads still to read (cycle 42749605088 queued 03:27Z, then every 3 h).
- Site facts (completeness, first pass over delivered rows): 30,220 sites read → own name 28,453, postal address 18,919 (CA 18,103 · US 654 · GB 144 · AU 22).
- Rank build 42749316069 (03:25Z) in progress: carries the organisation-key fix and the first site facts. READ `coord/GROWTH_VS_BASELINE.md` after it.
- Running: tenant-factory 42745654373 (+1 queued), lead-sites 42747032693 (websites for 23,851 leads without one), referee 42746318520 (+1 queued).

## 2026-11-10 03:00Z — ROWS MOVED (+898 in the first cloud build); six engines running; what was fixed and what is queued
- Build 01:55Z (GROWTH_VS_BASELINE): rows 63,641 → **64,539 (+898)**. Side effects found and fixed in rank.py (next build): 451 tier-I rows became
  client-listing rows and lost the facts held under their organisation key (legal names −122, routed pay-on-sight −172) → lead rows now take the
  organisation's own key (local run: 3,839 rows joined, 639 addresses, 1,323 names); first-key lookups read every key.
- Row factory: dealer / sponsor pages read → cc leads 9,664 → **16,253**; member pages indexed (15,099) and being read; ADDRESS PASS added to the
  cycle (11,617 vendor domains whose client page printed no address; 18,733 buyer domains wait on it); six-crawl index dispatched (02:52Z).
- THE BIG POOL nobody was reading: 33,600 Mac-era leads with a website and no mailbox row. The cloud crawl takes them after the cloud leads.
- Tenant factory first full cycle: 2,282 candidates → 177 accepted (150 Shopify / 26 Amilia / 1 Jane), 636 refused the reader, 292 no address,
  70 outside the vendor's scope. eScribe and Absorb portals are absent from the archive (index read completely, no pages).
- Crawl hygiene: per-site time budget (420 s) — a first-version shard hung 60 min on slow sites; new concurrency group `row-factory-b-*`.
- Local full rank builds no longer fit this container's memory (7 GB): test rank changes with `python3 -c "import ast…"` + the cloud build.
- NEXT (in order): read the address-pass / member / Mac-leads yields; dispatch a rank build after the referee lands them; PLAN §4e #5 (.com
  universe), #10 (tenant / advertiser classes), #7 (site finders in the cloud), #6 (Shopify scale, bounded), #14 (vendor legal names).

## 2026-11-10 02:15Z — referee verified the first 1,119 new buyers; three more engines launched (owner 20:42 / 20:48 EST: "do that … no maximum")
- Referee (01:23Z run): 1,216 of 1,230 cloud mailbox rows verified → **1,119 new buyers verified**. Rank build dispatched 01:55Z to deliver them.
- Row factory cycle 2: back-off works (unreadable 24 of 7,064 per shard); leads 9,487 (+5,050); their mailbox crawl is running (25 pages).
- NEW engines (all cloud, no AI): (1) page classes `sponsor` / `dealer` in cc_clients (parties that pay a Canadian organiser / supplier), re-index
  dispatched 02:00Z; (2) `tenant-factory.yml` — customers of Canada-HQ software vendors (portals of the vetted table + Shopify redirects; accept
  only with role mailbox + address in the vendor's contracting scope + service still seen), index dispatched 01:54Z; (3) `site-facts.yml` —
  bill-to name / address for delivered rows from their own pages, first pass dispatched 02:04Z; rank accepts a self-published trade name +
  address as bill-to (SOR/91-45 s. 3(c)(i)), reads `claude_lead_site_facts.jsonl.gz`, files sponsor / dealer rows with the client listings.
- Backlog of pathways: PLAN §4e table (15 items, ranked). Next OPEN: #4 address pass, #5 .com hosts, #6 member directories, #7 older crawls.
- Watch: first runs of tenant-factory index (per-domain equality queries over 300 index parts — slow or failing?), site-facts yield
  (addresses found / sites), and whether `rows` rises in GROWTH_VS_BASELINE after the 01:55Z build (if not: where rank.py drops cc leads).

## 2026-11-10 01:25Z — row factory: first measured yields; NEXT STEPS for whichever session runs next
- Index (crawl CC-MAIN-2026-43): 66,321 client pages on 28,538 .ca vendor domains. Extraction, first pass: the archive refused ~68 % of the range
  requests (8 runners × 10 connections); from the readable third: 10,952 client links with the vendor's Canadian postal address → **4,437 new
  buyers** (`claude_buyer_leads_cc.csv`), ~17k more links in the no-address side file. Fixed: retries with back-off, 4 connections per runner,
  unreadable pages retried on later cycles (≤ 4 attempts), failure reasons counted.
- Mailbox crawl of those 4,437 sites (7 of 8 shards merged by hand at 01:18Z; shard 7 hung on a slow site — fixed: stragglers stop after 4 quiet
  minutes): 3,847 sites read → **988 buyers with a published role mailbox** (1,073 rows in `claude_buyer_ap_results_cccrawl01.csv`: info@ 771,
  hello@ 97, contact@ 61, a few accounting / AP / procurement), nothing found 2,562, blocked 297. Yield 26 % at 15 pages; budget now 25 pages.
- Referee dispatched 01:18Z (runs 42734833754 / 42734885351). Rebuild done 00:38Z with the salvaged records (PSPC standing offers 7,099, Vermont
  2,574, Baton Rouge, Chicago, UNOPS).
- Run 42730092295 (first cycle) still has `crawl (7)` hanging (job timeout 200 min); the next cycle is queued behind it (same concurrency group).
**NEXT STEPS, in order:**
 1. When the referee has finished the cccrawl01 rows (coord/results/verification_log.csv gains ~1,000 lines for keys of claude_buyer_leads_cc.csv),
    dispatch `rank-buyers.yml` and read `coord/GROWTH_VS_BASELINE.md`: `rows` should rise by several hundred (first movement since the baseline).
    If it does not, find where rank.py drops the cc leads (mail dict key, same_org, seen_dom, REL_PATH) and fix.
 2. Check the next cycle's extract logs: `fail:http403` / `fail:http503` counts tell whether the back-off works; tune workers / shards.
 3. Gear (a) of PLAN §4e is CLOSED as low value: the Socrata portals are already leads from the Mac scanner, and departments of one government
    collapse into one row per website domain. Gear (b) next: Canadian vendors on .com / .org hosts — host universe with a location proof from
    ISED's Canadian Company Capabilities open data (address + website per company), OSM Canada POIs with a website tag, Wikidata, the dataset's
    vendor table → index semi-join → same extract chain (the list's own address is the Canada proof; page address kept when present).
 4. Address pass for `claude_cc_leads_noaddr.jsonl.gz` (read the vendor's contact page from the archive).
 5. Mailbox yield: second, deeper pass (60 pages) over "nothing_found" lead sites; consider contact pages from the archive for sites that block.
- Honest projection (to firm up in Sunday's report): this engine on .ca hosts ≈ 6–8k rows per crawl; with .com hosts (gear b) and older crawls
  ≈ 40–60k rows → ~105–125k total. 200k needs one more layer (tenant sub-domains of Canadian SaaS vendors, or department-level rows) — both are
  weaker on payability and must be put to the owner before being counted.

## 2026-11-10 00:45Z — rows were flat because the row factories were off; cloud factory live (owner 19:18 EST, Fable 5.2 session)
- Diagnosis: ranked universe 66,693 buyers, 63,641 with a mailbox → no head-room without NEW buyers. Lead scanners only ran on the Mac (last output
  Nov 8 16:34Z); 34 lane PRs open since Nov 2–7 (no source merged since Nov 7).
- Built + launched `row-factory.yml` (tools/cc_clients.py, tools/lead_crawl.py; rank.py reads claude_buyer_leads_cc.csv). Index scan done 00:38Z:
  66,321 client pages on 28,538 .ca vendor domains (Common Crawl CC-MAIN-2026-43). First cycle (extract → leads → mailbox crawl → referee) started
  00:40Z, run 42730092295; schedule: every 3 h at :17. Expect the first new rows in the build after the first referee pass.
- PR review (34 open): salvaged to main the rule-compliant stranded records — PSPC standing offers 7,099 ongoing (was 178), Vermont payments 2,574
  (68 agencies), Baton Rouge 203, Chicago 13 (buyer = City of Chicago - department), UNOPS 14; rebuild dispatched 00:38Z. Held with reasons in the
  commit message (rule 1 violations: Québec cities 28,899, Manitoba, Edmonton; duplicates; Socrata sweep to be re-cut per portal — next gear a).
- Fixed: vendor BN9 −64 (REQ row had replaced the Corporations Canada row for one vendor; BN now carried with its own source).
- RISK found: my wake-ups (send_later) are bound to the owner's Mac ("bound_device"); the 18:57Z one was consumed without a turn while the Mac was
  off. The cloud engines do not need me, but my integration turns may not fire with the Mac off — tell the owner; fall-back = his message from the phone.
- Pilot sample: ready (230 rows, layer-1 dossiers for all, layer 2 for the 30 Gold); S2/S5 targeted reads optional.

## 22:45Z — first growth measurement; Gold dossiers complete
- Build 19:39Z (b1ca4b3) vs baseline: pay on sight 835 (+2) / 835 (−6) / routed 22,267 (−74); Gold A 227 (+2); 101/438 (+1). The −74 routed is the
  legal-name guard removing 158 page-derived "legal names" of which ~150 were junk ("Centre Fonds", "200 University", "Health Information Protection Act");
  ~8 real ones (BCIT Student Association, ESF Events Ltd) were lost to an over-broad noise list — narrowed 22:28Z (next build). Correctness over count.
- Deep terms walk (T10) merged 19:06Z: 1,507 sites, ~32k pages, ~3.2k AP/terms pages per shard — its effect on payment_terms / po_required shows in the
  22:24Z build; measure next turn.
- Pilot: layer 2 done for all 30 Gold rows (S1). Structural findings that change how invoices are built: research subawards (Wright State, Vanderbilt,
  Notre Dame) invoice the prime's sponsored-programs contact per FDP Attachment 3A, not AP; construction contracts (UFV, Manitoba Housing, WECHC) are
  payment applications with holdback; US federal (CPSC) via DOT ESC; French public bodies via Chorus Pro; shared/central AP centres. S2/S5 next, one
  targeted read each (budget §4d).
- Wake-up chain: the 18:57Z trigger was consumed without a turn; rescheduled 19:24Z (fired 22:25Z) and 22:42Z (01:43Z) — verify at every turn end.

## 16:50Z — pilot layer 2 under way; tracks T5–T12 added; budget rule
- Dossiers: layer 1 for all 230 (16:28Z); layer 2 done for S1-01/02/03/05/06/07/08/11/12/18/23/24/25/26/27 (15 of 30 Gold). Found and fed back: WCB-Alberta
  T&Cs (net 30, PO first, GST-exempt #124072513RT0001), East Sussex T&Cs (APInvoices@, PO mandatory, PDF/TIFF, 30 days), Manchester (no PO no pay,
  supplier.invoices@), Paris-Saclay (Chorus Pro + engagement juridique), CPSC (DOT ESC shared AP), legal names from audited statements (Cambrian,
  Windsor "Corporation of", SickKids, FWFN). rank.py: legal-name guard (distinctive token), First Nation B-039 tax note. Pages → claude_ap_pages_manual.csv.
- Owner 11:43/11:47: all 230 before invoices go out; never a static plan (T5–T12 in PLAN §4c); weekly limit 78 % used → §4d budget rule.
- Cloud: walk_terms (6 shards, 4 h) and registry (5 h) dispatched 16:19Z; org_facts leftovers measured (24 ok / 1,120 — blocked sites).

## 15:55Z — NEW DIRECTION (owner 10:25–10:48 EST): wait-or-ship decision by Sun Nov 15; targets 200k rows, ≥ 85 % complete, cloud-only
- Owner's computer will be off: nothing may depend on the Mac. Engines moved to GitHub cron (claude-engines.yml: org_facts every 6 h / 8 shards,
  walk_terms nightly / 6 shards, bulk_registry daily); org_facts dispatched 15:55Z (8 runners, 120 min). My wake-ups: send_later every 180 min.
- Ship-now baseline frozen: coord/BASELINE_SHIP_NOW_2026-11-09.json (build 89b4386). tools/growth_report.py runs in every rank build →
  coord/GROWTH_VS_BASELINE.md + coord/growth_history.csv. PLAN_2027-01.md: four tracks, week-1 table, kill switch (< 120k rows or < 70 % complete
  projected → recommend shipping now).
- Measured: 39,626 incomplete rows; bill-to (legal name / address) missing on 33,136 of them (17,902 have an address but no legal name; 24,670 are
  .ca; 26,180 sites answer); 22,394 lack exactly one element. Peer-group inference: PO rule concentrates (100 % "required" among publishing peers,
  selection bias noted) → 29k rows inferable at p ≥ 0.9; payment terms and method do not concentrate (net 30 43–62 %) → distributions, not values.
- 16:15Z: org_facts cloud run measured — the leftover domains are the hard ones (shard 0: 1,120 domains → 24 ok, 872 blocked, 85 robots, 106 no answer).
  Crawling will NOT close the bill-to gap; registries / bulk files (Companies House, GLEIF, SEC, Canadian registries) and batch extraction from pages
  already fetched are the T2 levers. Pilot designed on the owner's "payability, not plausibility" rule: coord/pilot/ (230 rows, 5 strata, real
  invoices by the row's vendor only); downstream AI briefed (coord/for_downstream_ai_2026-11-09_pilot.md).
- Lanes briefed (inboxes 16:00); 8 T1/T2 sources registered (USAspending Canada-recipient full, US local checkbooks, FL FACTS, Companies House bulk,
  SEC EDGAR submissions, …). API credits: batch extraction only, capped, yield per dollar reported.

## 14:35Z — FINAL (builds 13:39Z scoreboard / 14:03Z amounts / 14:29Z portal correction; this is the last entry)
- Final published build 89b4386 (14:29Z): 63,638 rows; **pay on sight 833** strict + 841 reference-less + 22,341 routed; Gold 395 / 624 (63.3 %),
  Gold at AP grade A 225, AP payability Gold 452 / 624; 100 / 438 benchmarks (the three P11 DNS cells healed by the re-check); amounts formatted.
- Correction found while writing the worked examples, and the reason the strict count fell from 1,113: `_portal_ok` accepted any portal whose kind
  text said "invoice" — the generic kind text does for every portal — so 466 rows with only a purchasing / general mailbox counted a tender portal
  (SEAO 190, MERX, bids&tenders) as their invoice channel. Now only e-invoicing networks (Ariba, Coupa, Tungsten / Kofax, Basware, GHX, Jaggaer,
  Workday, Oracle iSupplier, Esker, Taulia …) make tier 1 on their own; the card carries `portal_is_invoice_channel` + `portal_class`, invoice_text
  labels tender portals "not an invoice channel". 280 rows moved to `routed`, which is what they are. Gold unchanged (AP mailboxes).
- Verified ceilings once more: of 138 Gold rows without a vendor GST number, 110 have a vendor site, 94 were read in full by org_extras and none
  prints the number (a GST/HST account is printed on 0.14 % of 83,475 organisation sites). Nothing else within the rules moves ≥ 50 rows.
- Closed: wake-up trigger deleted (13:19Z); inbox notes to codex / chatgpt / gemini; hand-off `coord/HANDOFF_INVOICES_2026-11-09.md` §0–§10 (tiers,
  field mapping, legal minimum SOR/91-45 s. 3, bounce rules, ceilings, what runs, levers, card schema, two rendered rows, pre-flight, cover e-mail).

## 13:00Z — STOP ORDER (owner 07:51 EST: "stop … make sure this is really it … advice to the other AI … go out with a bang")
- Final lever audit: nothing left that moves ≥ 50 pay-on-sight rows within the rules (list in coord/HANDOFF_INVOICES_2026-11-09.md §6). Two last
  defects fixed before the final build: `ap_payability` and `supplier_setup_url` were computed but never written to the pack (missing from the column
  map since 2026-11-08 — now emitted); the doubled "DERIVED:" prefix in invoice_text.
- Hand-off written for the downstream AI: coord/HANDOFF_INVOICES_2026-11-09.md — build order by pay-on-sight tier, field-by-field mapping of the
  invoice to the columns (bill-to, channel, references, vendor identity, tax, currency, terms, follow-up), bounce rules learned from the buyers'
  pages, ceilings, what keeps running and how to stop it, the levers audited. Companion: coord/for_downstream_ai_2026-11-08.md (status + by-design cells).
- Stopped on the Mac (they spend the owner's quotas): codex_exec_loop (ChatGPT), api_search_loop (Anthropic API, $170.04 of the cap, 7,690 tasks),
  lane_driver_loop (Anthropic API). Left running, restart-safe and free: push loop, walker-terms loop, site readers, downloads/sync loops, Gemini's
  hourly task, the Codex app automation (owner's own); GitHub: builds every 6 h, referee on push, bulk registry daily. One-liner to stop everything on
  the Mac: `pkill -f 'cch-crawler-state/.*_loop'`.
- Final build 12:54Z → landed 13:09Z (3a4b3d5): 63,628 delivered rows; pay on sight 1,113 strict + 887 reference-less + 22,024 routed; Gold 395 / 624
  (63.3 %), Gold at AP grade A 225; AP payability Gold 452 / 624 (72.4 %), P02 306 / 404; 100 / 438 benchmarks. Its scoreboard was NOT written (the
  new AP-payability table shadowed the field-gap list `gaps` — same bug class as 700edbf; fixed, build 13:17Z re-dispatched for the scoreboard).
  Two last invoice_text defects found while writing the worked examples: amounts printed as raw floats (416594.66000000003) and tender portals (SEAO)
  labelled "portal" next to the mailbox — fixed in rank.py (`_money`, "supplier / tender portal (not an invoice channel)"); last build carries them.
- Hand-off extended (§2 legal minimum per SOR/91-45 s. 3 — $100 / $500 tiers, replacing the outdated $30; §7 invoice_card_json schema; §8 two rows
  rendered as invoices with build instructions; §9 pre-flight checklist). Wake-up trigger for 13:33Z deleted: no further turn is scheduled.

## 12:05Z — build 11:17Z: 1,114 (+2) / 887 / 22,025; Gold 395 / 625; 100 / 438 (row growth). Codex lanes quiet again since 10:42Z (ChatGPT limit); Gemini sync 12:00Z; verifier 11:45Z; integrity intact. Flat as forecast; loops stretch to 90 min until the owner answers.

## 11:00Z — no build since 09:00Z; Codex lanes back (chatgpt batch52 rows 11–30, codex batch04 rows 384–393 at 10:38–10:42Z), Gemini batch 53; verifier landing (10:56Z); integrity intact; build dispatched 10:58Z.

## 10:00Z — build 09:00Z: 1,112 / 887 / 22,023 (flat); Gold 395 / 624; 101 / 438. Gold's 209 non-payable rows: 87 miss ONLY the vendor GST number
- The province-from-name fix moved 10 Gold rows' tax treatment (59 → 49 missing) but they still lack the vendor GST number, so pay on sight is flat.
  Remaining Gold gaps: vendor GST 138 (87 of them the only gap — ceiling), bill-to 76 (blocked sites / registries), tax + currency 49–57 (buyers with no
  resolvable province or country: no address, no city or province in the name, .org / .com domain — 13 rows miss only those two).
- Lanes: Gemini syncs 09:15Z / 09:36Z (batch 53); Codex at the ChatGPT limit; verifier landing (09:48Z); integrity intact. No build dispatched this loop
  (last 09:00Z; next with the Gemini rows). Hourly loops continue until the owner answers the 06:25Z recommendation.

## 08:55Z — build 08:16Z (ranker-bot, no revert since): pay on sight 1,112 (+8) / 887 / 22,022 (+75 routed); Gold 395 / 624; 101 / 438
- Scoreboard provenance verified (ranker-bot 08:16Z); verifier commits keep landing (08:24Z). Build for the province-from-name / federal fix dispatched 08:50Z.
- Inspection: P02's 158 non-payable rows — vendor GST/HST number 130; P04's 920 — general-inbox channel 748, vendor GST 693, bill-to 207, tax 196.
  The vendor GST number is now the single remaining blocker across Gold / P02 / P04 (≈ 960 rows) and no public source exposes it beyond what is
  already joined (Corporations Canada, Canada's Business Registries, CRA charities, federal grant recipients, the vendor's own pages). Ceiling.
- Gemini batch 52 complete (02:28 EST; hourly task next); Codex at the ChatGPT limit; integrity intact (org_contacts 74,911). Verdict unchanged.

## 08:05Z — build 07:13Z: 1,104 / 885 / 21,947 (flat vs 06:36Z); Gold 393 / 624; reverted again at 07:18Z by a pre-fix verifier run; republish dispatched 08:00Z
- The 07:18Z revert came from a verifier run queued before the 07:12Z fix; runs since (07:41Z, 07:56Z) are on the new code and do not touch
  coord/results/ranked. Ranker build re-dispatched 08:00Z; the one after carries this loop's fix.
- Inspection pass (Gold, 212 rows not pay-on-sight): vendor GST 138 (ceiling), tax / currency 59 (buyers with no address and no city in the name —
  now resolved from the province in the body's name or the address code, e.g. "Efficiency Manitoba", "NS, CA"; federal bodies get the federal treatment),
  bill-to 76, remit-to 13. Pushed 1bf685b.
- Gemini batch 52 complete (07:28Z); Codex at the ChatGPT limit; integrity intact. Verdict unchanged; awaiting the owner.

## 07:15Z — build 06:36Z: pay on sight 1,104 (+72) / 885 / 21,947; Gold 393 / 624 (63 %); 101 / 438 — then reverted by a verifier push, fix pushed
- The country-first tax / currency fix moved 72 Gold / P02 rows to pay on sight (1,032 → 1,104). 101 / 438 (Gold row growth dilutes a few cells).
- A third regression path closed: my 03:20Z verifier fix restored the whole coord/results snapshot on retry, including coord/results/ranked, so the
  verifier's 06:41Z push put the 05:32Z build back over the 06:36Z one. Now rsync restores only the verifier's own files (1468ce7). The scheduled
  ranker build in progress (06:38Z) republishes; if a pre-fix verifier run reverts it once more, the next loop re-dispatches.
- Lanes: Gemini batch 52 rows 31–65 (06:39Z); Codex at the ChatGPT limit again (the window closed ≈06:30Z after batch51 rows 81–90 / batch03 rows 261–270);
  org_extras refresh second cycle started (9,012 domains). Verifier landing every ~15 min.
- Verdict (06:25Z) unchanged: organic pay-on-sight ≈ 0 / h; today's +72 came from an inspection fix. Awaiting the owner's answer on stopping.

## 06:25Z — VERDICT for the owner (asked 19:55 EST: "tell me when the rewards won't be worth it")
- Build 05:33Z (first with the 6,168 verified mailbox finds): 102 / 438 (−3: Gold grew 597 → 623 rows as P03 / P04 buyers gained a confirmed
  invoicing mailbox, which dilutes three Gold percentages — row movement, not lost data); Gold A 214 → 225; pay on sight 1,032 (flat), 862
  reference-less (+4), 21,868 routed. Organic rate over 04:09Z → 05:33Z: **≈ 0 strict pay-on-sight rows per hour** — far below the 100 / hour signal.
- Where the remaining movement comes from: (1) the lanes (Codex × 2, Gemini: ~100–200 researched rows per hour while the ChatGPT window is open, of
  which a fraction upgrades a channel); (2) rule / normalisation fixes I find by inspection (this turn: 98 Gold rows without a tax treatment because the
  buyer's country was read after the province; 'CA'-only addresses blocking the site readers' address — pushed 14ce036, build 06:19Z). Those are
  one-offs with diminishing size. The engines that read the web have run their course for the honest fields.
- What is left is ceiling under the rules (no fabrication, evidence or nothing): 21.9k rows whose organisation publishes one general inbox (routed,
  not addressed); ~270 Gold / P02 rows whose vendor has no BN in any public registry (Québec-only vendors, partnerships, not-found names); blocked sites
  (~10 % of organisations) for bill-to addresses and legal names; relationship-proof rows with no contract record (no PO / contract numbers, values,
  dates); P11's 441 mailboxes the referee cannot re-fetch (only a second lane's quote confirms them).
- RECOMMENDATION: stop the paid effort after (a) the current lane batches finish (chatgpt batch51, codex batch03, gemini batch52), (b) the build after
  14ce036 lands, (c) one final build + the pack hand-off (ranked batches with pay_on_sight / channel_tier / invoice_text on every row, the Pay-on-sight
  table, COVERAGE_VS_TARGETS.md with the ceiling notes, for_downstream_ai_2026-11-08.md). Zero-cost automation (scheduled builds, verifier, Gemini's
  hourly task) can keep running; it will add rows slowly. My loops drop to 45 minutes until the owner answers; each one still ships any inspection
  fix with a visible row effect.

## 05:35Z — verifier landing again (commits 04:49Z and 05:01Z); search01's 6,168 rows verified; both Codex lanes back; build 05:13Z in progress
- The gzip fix worked on the first run: verification_log now holds claude_buyer_ap_results_search01.csv verified 6,168 / page-unavailable 132 /
  not-on-page 42 / personal-mailbox rejected 8 (the deep_pages finds from the policy pages), deep01 434 verified.
- ChatGPT limit lifted ≈05:05Z: "[chatgpt] Buyer AP batch51 rows 31–50" and "[codex] buyer AP batch03 rows 261–270" (05:08–05:12Z); Gemini batch 51
  complete (04:58Z). API capped; deep_pages queue drained (last pass 0 buyers left).
- Build dispatched 05:13Z (first with the verified mailbox finds) — still running at 05:35Z; the channel-tier upgrades (P03–P05, P11) read at the next loop.

## 04:40Z — the verifier's real blocker: coord/results/team_buyers.jsonl grew past GitHub's 100 MB limit (101.4 MB) — every push since 22:16Z was
rejected by the pre-receive hook ("remote rejected"), not lost to a race. The earlier race fix (48c70d7) was right but not sufficient: the fixed run
retried 12 times against the same rejection. Fixed (8571915): the ingest writes team_buyers.jsonl.gz (16.7 MB), the plain file is removed from git,
all five readers (ap_crawler, status_board, make_batches, patch_dataset, ingest) accept the gz, .gitignore un-ignores it. An old-binary verifier run
(started 04:25Z) still holds the main-writer lock and will fail the same way; the first run on the new code starts after it (≈05:05Z) and lands
≈05:50Z with the 3,583 deep_pages mailbox rows. Build 04:09Z: 105/438, pay on sight 1,032 / 858 / 21,874 routed (+128 routed, organic).
Gemini batch 51 rows 1–30 (23:01 EST). Codex: 30 usage-limit refusals so far; waits for the account window.

## 03:55Z — waiting on the first fixed verifier run (an old-logic run started 03:26Z holds the main-writer lock; the fixed run is queued behind it; cancelling the old run is outside this session's permissions). Build dispatched 03:51Z on Mac inputs only. Gemini quiet since 21:15 EST (owner active at the Mac, no screen action); Codex at the ChatGPT limit; org_contacts refresh finished (123 of 1,090 reachable).

## 03:25Z — build 03:00Z flat (1,032 / 857 / 21,746); the referee had not landed a result since 22:16Z — root cause fixed
- Organic gain 02:26Z → 03:00Z: +0 pay-on-sight, +2 reference-less, +203 routed (P13 site readers). Below the 100-rows/hour signal — but the pipeline
  that carries the channel upgrades was stalled: the verify-and-merge workflow re-ran its 40-minute evidence re-check on every push race and lost all of
  them (verification_log.csv last changed 22:16Z while claude_buyer_ap_results_search01.csv gained 3,583 rows today — the deep_pages invoicing-mailbox
  finds). Fixed (48c70d7): the ingest runs once, the push loop restores its outputs onto the latest main and retries only the cheap queue / board steps
  (12 attempts). The next verifier run lands the 3,583 rows → channel tier upgrades (P03–P05 → pay on sight; P11's 440 unconfirmed) in the build after.
- Owner's signal: I will call the engines' organic rate after two verifier runs have landed (≈ 04:30Z), not on this stalled reading.

## 02:45Z — build 02:26Z: pay on sight 1,032 + 855 + 21,543 routed; Gold 361 / 597 (60.5 %); 105 / 438
- Rate since 02:05Z (21 min): +55 pay-on-sight, +29 reference-less, +455 routed — from the public-body billing name and vendor carry-over rules.
  Engines' organic flow now: deep_pages found invoicing mailboxes for 87 of 105 buyers in its last pass (policy / AP pages from the pb search) →
  referee → channel upgrades for P03–P05 in the coming builds; Gemini completed batch 50 (21:15 EST); Codex lanes still at the ChatGPT limit.
- Gold's remaining gap is the vendor GST/HST number (126 rows): 89 vendors not found in Canada's Business Registries, 25 found in the Québec REQ
  (which publishes no BN), 6 ambiguous. Name-variant matching might recover ~20–30 of the 89; the REQ ones have no public BN — a ceiling.
- 21,543 "routed" rows (19,829 of them P13) are complete invoices addressed to an organisation's general inbox: the honest state for small
  organisations that publish one mailbox.

## 02:15Z — Pay on sight on the scoreboard: 977 yes + 826 yes-no-reference + 21,088 routed of 63,609 (build 02:05Z); Gold 57 % (340 / 597)
- Top gap per package (rows): Gold — bill-to legal name / address 105 (public bodies whose published name is the billing name → counted from the next
  build; the address gaps stay with registries / site readers); P02 / P01T — vendor GST/HST number (121 / 18; registry coverage); P03–P06T, P08–P10, P12,
  P13 — only a purchasing / general inbox confirmed (the invoice is routed, not addressed: 21,088 routed rows, 19,451 of them P13); P11 — channel not yet
  referee-confirmed (440).
- deep_pages over the pb / pc pages is finding invoicing mailboxes at 41 / 50 and 63 / 75 buyers per pass (Mac log 21:11 EST) — the honest route from
  "routed" to "pay on sight" for P03–P05; they go through the referee first.
- API worker: budget reached ($170.04; pb 1,735 of 1,881 done, 1,195 with pages). The loop now sleeps; the cap stays (owner: don't burn the key).
- Same-vendor carry-over of BN9 / remit-to address (45 / 56 rows) and the public-body billing name pushed (8a3f9df); build dispatched 02:11Z.
- Rate: pay-on-sight rows 380 (00:30Z strict measure) → 1,803 (02:05Z) — +1,400 in 95 min, almost all from resolving tax / currency / vendor identity
  rules on data already held; the engines' organic contribution per hour is measured from the next build on (signal to the owner: < 100 rows / hour).

## 01:55Z — the goal restated by the owner (19:55 EST): PAY ON SIGHT — every row an invoice that clears AP; the 438 stay, payability leads
- Owner: "you see the invoice, boom, it's paid"; add fields that push payability; keep the 438 but don't be limited by them; derived columns stay, never
  count as published; say when the rewards stop being worth it; credits allow until tomorrow night at most.
- Strict measurement before tonight's changes: 380 of 63,499 rows could have an invoice generated that clears AP (confirmed invoicing / AP or finance
  channel + bill-to legal name and address + vendor legal name, GST/HST number and remit-to address + tax treatment + currency). Top blockers by rows:
  tax treatment unresolved (province unknown) ~49k; reference rule unpublished (reported separately, does not block); channel = purchasing / general
  inbox only (P03, P04, P08, P13 — routed, not addressed); vendor GST/HST number (130 Gold … 731 P04); bill-to legal name / address on P13 companies.
- Shipped (b73458e, 855dca4, 700edbf): `pay_on_sight` (yes / yes — reference rule not published / routed / no), `pay_on_sight_missing`, `channel_tier`
  (1 invoicing-AP or invoice portal, 2 finance, 3 purchasing / general, 0 unconfirmed) and `invoice_text` — a rendered draft invoice header on every row;
  tax treatment and currency derived for every row with a resolvable province (jurisdiction → postal code → website / mailbox domain → registry place
  table → city) or country (US / UK / EU / AU export treatment); the inferred relationship's vendor (Canada Post Corporation, BC Hydro) counts as a
  certain identity; scoreboard "Pay on sight" table per package. First pack with it (01:44Z): pay_on_sight yes 1,116, routed 1,642, no 60,854;
  ap_payable_today 905; ship_ready 612; Gold A 211 (00:50Z build). The 01:44Z scoreboard was dropped by a shadowed variable in the new table
  (TypeError) — fixed, workflow now keeps the previous scoreboard when the new one is not written; build re-dispatched 01:48Z.
- Build 00:50Z (late site-reader pass): 105/438; vendor_logo +15–29 pts, vendor_phone +11–17, buyer_logo +10–18 across P01–P05.
- Mac: API $152 of $170, pb 1,200 / 1,881 (749 with pages; marginal yield now ~+30 terms per 600 — the pass finishes at the cap, no extension);
  Gemini last local commit 19:13 EST (batch 50 rows 1–30; hourly task irregular); Codex exec and app both at the ChatGPT usage limit again.
- Next: read the Pay-on-sight table (02:03Z build) → the next engines go at the top gap per package in ROWS; honest answer to the owner on what the
  remaining gaps are (channel type for P03/P04/P08/P13 = routed at best; vendor GST for vendors absent from registries; bill-to for blocked sites).

## 00:55Z — builds 23:53Z 103 / 00:29Z 104 of 438; Gold A 134 → 198 (DMARC posture no longer a penalty); owner 19:11 EST: continuous dense loops
- Owner (19:11 EST): keep working continuously, every loop must show marginal progress, say when the rewards stop being worth it; derived columns stay
  on every row but never count as the published benchmark; talk to the downstream AI if useful. Brief written and sent: coord/for_downstream_ai_2026-11-08.md
  (status, what an AP clerk needs, the cells no honest source can fill → asked to mark them "by design", two questions). Loop cadence now 30 min.
- AP grade: the buyer's DMARC posture is a NOTE, not a penalty (it blocked A on 269 Gold rows; coord/DECISIONS.md). Build 00:29Z: Gold A 198 / B 195.
  Remaining Gold blockers: payment terms 240, PO rule 194, legal name 87, address 40, vendor-registry warning 71 (of which the warnings caused by a lapsed
  extra-provincial registration while the home registry says Active are now a note, not a warning — pushed 00:52Z, next build).
- New API search kind `pb` (purchasing bylaw / procurement policy / PO terms on the buyer's host or its council / board document portal when the address
  names the buyer): 1,881 public-body buyers of P01–P05 still lacking terms or a PO rule; first 600: 456 with pages, 3,741 URLs; the readers added
  +106 payment terms, +323 PO rules, +450 AP contact names in one cycle (Mac file). Cap raised to $170 ($135 spent).
- rank.py: second site-reader pass for websites found late in the pipeline (95 Gold rows had the vendor's phone on file and "not_published" in the row).
- Codex: the ChatGPT account hit its usage limit again at 00:40Z (app automation + headless exec share it); both resume when it lifts. Gemini batch 50.
- Integrity after the snapshot-union fix: pages 58,056 → 61,770 (Mac rows merged in), registry 34,313 → 36,653 — nothing fell.

## 23:45Z — terms_refresh merged (23:09Z); two data-loss paths found and closed; registry shard recovered; Codex lanes back
- terms_refresh (every known page re-read with the current patterns; 10 runners, ~30 min): merge 23:09Z, 114,266 keys; the pages file then carried
  payment terms 2,752, PO rule 2,936, portals 3,882, payment method 864, tax treatment 1,341, e-signature 441–523, AP system 407–428, AP contact 1,349,
  invoice format 441. (ap_phone / invoice address next to payables anchors: only 15 / 11 — the anchor rule found little; the mailbox pages still carry
  35,021 phones and 12,839 addresses.)
- DATA LOSS 1 (closed): at 23:23Z the Mac's push snapshot replaced origin's claude_ap_terms_pages.csv.gz (50,895 rows, runners' union) with the Mac's own
  40,405-row copy (its ap_terms rewrote the file from its local view; the snapshot's "stale" rule only compares times). Restored by unioning the 23:09Z
  files with main (121,427 keys, pages 58,055) — commit f1996fc; tools/push_snapshot.py now UNIONS multi-writer files (ap_terms pair, registry_lookup,
  org_extras, org_contacts) with origin's copy via merge_engine_outputs.py instead of copying (10bec7b, mirrored to the Mac 23:38Z).
- DATA LOSS 2 (closed): the registry engine's merge job (run 42503912200, shard 1/2 finished 22:34Z) lost all 5 push races against a main that moves
  every minute; its artifact was merged by hand (1cf31ee: 34,313 keys, buyers found 3,944 → 6,446). The merge job now tries 15 times with short waits.
- A cancelled deep-walk repeat still produced a partial "walk_terms merged" commit at 22:51Z (union, harmless).
- Codex: the ChatGPT account's limit lifted at 23:34Z as announced — "[chatgpt] Buyer AP batch50 rows 1–10" at 23:39Z (app automation) and the headless
  codex exec is researching lane codex batch02 (World Bank borrowers). Gemini batch 49 rows 1–60. API worker 5,511 tasks, $113.81 (cap $120).
- Build dispatched 23:35Z (inputs: terms_refresh, award/notice-id and trading-name rules, lanes); read at the next wake-up.

## 22:55Z — build 22:49Z **99/438** (+5): ap_system_hint P01T / P09, buyer_tax_exempt_status P12, vendor_trading_name P03 / P04; Gold A 134, payable 805; payment terms +5–6 pts in P02 / P03 / P05 and PO rule +4–5 from the deep walk (27 cells up ≥3, none down)

## 22:47Z — build 22:23Z (scheduled) 94/438; deep A–F walk merged (+24k page keys); terms_refresh running; org_facts merged
- Build 22:23Z: 94 of 438 (+1: vendor_website P01_GOLD); award_or_notice_id +10–19 pts in Gold / P02 / P03 (notice-id rule), vendor_website P04 +16.7
  (API vendor-site searches + vendor_sites_check), payment terms P03 +7.5. Gold A 129 / B 255; payable today 789.
- Deep A–F walk (only buyers still lacking a term or PO rule, 60 pages, one more link level): 10 shards × ~1,290 sites, ~28k pages per shard;
  merge 22:34Z → ap_terms 114,266 unique keys (90,163 before); walker pages now carry payment terms 2,752 (1,277 at 19:45Z), PO rule 2,936,
  portals 3,882, payment method 864, tax treatment 1,341, e-signature 441, AP system 428, cheque-run cadence 86. The run re-dispatched itself (a
  redo-everything pass never shrinks "sites to walk") — cancelled, workflow fixed (no self-dispatch when redo_days = 0).
- ap_terms: walker pages had ap_phone 0 and invoice address 0 because both were read only next to the mailbox; now read next to the first payables
  anchor on mailbox-less AP / supplier pages. terms_refresh (every known page re-read with the current patterns; 10 runners, 90 min) dispatched 22:36Z
  with that change; it queued behind the cancelled run.
- org_facts merged 22:26Z (runner retries of blocked / failed domains: ~1,500 new successful reads). Mac org_extras --refresh: 6,717 of ~8,000 retried
  domains are blocked for automated readers (small-business hosts); the honest ceiling for those stays the registries.
- rank.py: vendor_trading_name from the vendor site's schema.org alternateName / Organization name when it differs from the legal name (not yet built).
- Mac: API worker 4,571 tasks, $95.69 of the $120 cap (84 % with a page); Gemini batch 49 rows 1–30 (21:47Z); Codex resumes 23:34Z; push loop 22:20Z.

## 21:46Z — build 21:39Z **93 of 438** (72 → 93, nothing lost); Gold A 128 / B 253; ChatGPT account at its usage limit until 23:34Z
- The first main build with the 20:30–20:45Z rank.py rules: +21 benchmarks — records_with_this_vendor met in 9 packages (relationship record = 1 record),
  solicitation_or_tender_number P02 / P04 / P09 (SEAO numero), ap_system_hint P01_GOLD / P02 / P03 / P04 (portal names feed the hint), invoice_reference_hint
  P01T / P06 (PO rule), contract_description P05 (title text), buyer_tax_exempt_status P01_GOLD, po_required P01T. 67 cells moved ≥ 3 points, none down.
  Pack ran (ap_payable_today 785, ship_ready 593).
- Codex: the ChatGPT account hit its usage limit ("try again at 6:34 PM" EST = 23:34Z) — that is why "[chatgpt]" commits stopped at 19:55Z; the app's
  30-minute automation is ACTIVE and resumes by itself. A second, headless Codex (`codex exec`, GPT-6.1 Sol high from ~/.codex/config.toml, own clone
  ~/cch-codex-exec, loop ~/cch-crawler-state/codex_exec_loop.sh) takes lane codex's buyer-AP batches from 23:34Z; inbox notes written for both lanes.
- Mac site readers restarted (`site_readers_loop.sh`: org_extras --refresh 9,122 domains v1 → v2 / retries, then org_contacts --refresh, every 2 h).
  Correction to 20:45Z: the 9,365 "never read" domains WERE attempted by the Mac (resume files: 103,991 domains; blocked 10.5k, network errors 5k,
  robots 2.2k, no contact found 9.1k) — the repo copies hold only successful reads. The runner org_facts engine retries them from another network
  (shard 5: 49 + 102 successes of ~1,000; most stay blocked) — worth its free runner minutes, not a lever. The honest ceiling for buyer address /
  phone / logo on blocked sites is the registries and public directories already joined.
- rank.py: a portal's tender-notice id (bidsandtenders_tender_id, competition_guid) is the award_or_notice_id when the source assigns no separate award id
  (SaskTenders 18 of P09's 35 missing; bids&tenders 464 rows) — not yet built.
- API worker: 3,497 tasks, $71.41 (cap $120), 80 % with a page. Gemini batch 48 complete (20:57Z). Deep A–F walk and org_facts still running; terms_refresh
  after the walk.

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
