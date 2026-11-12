# Decisions log (append; newest at the bottom)

## 2026-10-26 from claude
- **GitHub repo as the shared brain.** Code, docs, queues, inboxes and verified results live in git. Big data lives in
  release assets (`dataset-latest`, `harvest-state`).
- **The verifier is code, not an AI.** `tools/ingest_results.py` re-fetches every evidence page. Only values that
  appear on the cited page enter `coord/results/`. Nobody, including Claude, can merge an unverified contact.
- **Data-only PRs auto-merge after validation**, so the team never waits on a human. Code, tool and workflow changes
  need a review.
- **Lanes are disjoint** (see AGENTS.md §4), so agents can run in parallel without coordination overhead.
- **Reference date** for "ongoing" stays 2026-10-25 until the rebuild workflow advances it (coord/config.json).

## 2026-10-26 from claude
- **SEAO API yield is low.** Of 8,600 notices fetched (newest first), only ~1-2% expose a planned end date
  (`datePrevueFinContratUtc`) or duration. The harvest continues daily (free on a public repo), but the 305k Québec
  "ongoing_inferred" records need a better public signal. Open question for the Gemini red team.
- **First rebuild (2026-10-26)** applied vendor-website discovery and BC OrgBook extraprovincial registrations:
  - vendor website: 116,394 → 127,981 records;
  - registry match: 380,868 → 401,879 records;
  - 70 SEAO records got explicit end dates.
- **How Claude sessions publish data.** They cannot create releases, so they push to the `data-upload` branch. The
  `publish-data` workflow joins the parts, checks SHA-256, publishes the releases and deletes the branch.

## 2026-10-26 from claude
- The free Gemini API key has no web search (Google's free tier: search grounding "not available" for Gemini 3+, and
  2.5 is closed to new keys). The scheduled `gemini-researcher` therefore stands by. It checks each run and starts
  working automatically the day the key's project gets billing.
- **Invoicing-contact research is done by the search-capable agents the owner runs from his subscriptions:**
  - Antigravity (Gemini, on his Mac): lane `gemini` (Québec). It pushes rows directly.
  - ChatGPT agent mode: lane `chatgpt` (rest of Canada + US). CSV uploaded to `data/incoming/chatgpt/`.
- **New sources:**
  - Jules: automatic, every 6 h and right after each merged task;
  - Codex: started from ChatGPT; opens PRs.
- If billing is enabled later, give the scheduled researcher a lane Antigravity is not working on (`--lane chatgpt`).

## 2026-11-01 — Owner's target is organisations with a mailbox; referee unblocked (Claude)
- Target (owner, 2026-10-28): 30,000+ organisations doing business in Canada, each with a published mailbox:
  invoicing/AP first, then purchasing, then general role mailbox. A contract/payment record with a Canada-located
  supplier is kept as proof where we have one (`b:` buyers, `lead:` buyers), but is no longer required.
- Organisation pools for the no-AI crawler (all on the owner's Mac): research queues, payment/subaward leads,
  Wikidata items located in Canada with a website (batch902), our verified vendor sites (903), OpenStreetMap
  offices/industry (904), institutions/hotels (905), shops (906).
- The referee had not finished a run since Oct 29 (60-min timeout re-fetching ~16k pages serially; cache only saved
  on success). Now: parallel polite prefetch, 60-min fetch budget with `pending_verification` for the rest, cache
  saved always. It also writes the owner deliverable `coord/results/org_mailboxes.csv` + `ORG_MAILBOXES.md`.
- Gemini's clone had lost its `origin` remote and ChatGPT (which ran the uploader) hit its weekly limit on Oct 30, so
  Gemini's rows stopped reaching GitHub. Now a no-AI loop on the Mac runs tools/mac_sync.py every 30 minutes and
  re-adds a missing remote. Jules sessions were all stuck "awaiting user feedback"; the builder now answers them
  ("decide yourself, open the PR") and reports session states.

## 2026-11-01 — claude: what counts in the ranked deliverable (contrib/claude/rank_buyers)
- A mailbox counts for a buyer only if it is the buyer's own (tools/ap_crawler.py `same_org`). Reason: the crawler and
  earlier enrichment attached contractors' and partners' mailboxes found on buyers' pages (a landfill operator's billing
  box on halifax.ca, a roofing contractor's AP box on a town's page, ministries' info boxes on agencies).
- "Invoicing / AP" needs an invoicing word in the mailbox name, or the words just before the address sending invoices
  there. Finance / accounting department mailboxes are a separate batch (1b). Person-looking mailboxes are never used.
- Known upstream defect: `scripts/merge/finalize.py` builds buyer keys from name + country, so provincial ministries with
  the same short name (Justice, Health, Education, Finance, Executive Council ...) in AB / SK / NL / NWT and some federal
  departments share one key. The ranking splits them by the source's government. Fix to do in the merge: add the source
  jurisdiction to bkey for names of three words or fewer without a place word, and re-key their team findings.
- Contract dates live in `contract.dates.awarded` (not `award`); "awarded in the last 12 months" uses awarded / signed /
  start, else published.

## 2026-11-01 — claude: referee verifies refused pages on the Internet Archive's recent copy
Some public sites (canada.ca above all) refuse requests from GitHub's servers, so the referee could never check their
values; they waited for a second agent forever. Now, for contract and relationship buyers only, when a cited page
refuses the referee, it looks up a capture of exactly that page made in the last 180 days (Wayback CDX index, 4 lookups
at a time) and accepts the value if it is on that copy. The evidence keeps the snapshot as `verified_via`. Failed pages
are remembered for 3 days so they no longer consume every run's time budget; second-read tasks go to the other lane
only for contract buyers (first) and relationship buyers.

## 2026-11-01 20:15 — delivery packages for the owner's survey (claude, approved by the owner in chat)
- The deliverable is one row per distinct buyer (vendors may repeat), each in its best package, and every delivered row
  carries the buyer's own e-mail: P01 active relationship + invoicing/AP (Gold) … P11 e-mail not yet confirmed
  (contrib/claude/rank_buyers/batches.py; refreshed every 3 h into coord/results/ranked/).
- Owner's item 1: contracts awarded 12–36 months ago with no end date are "likely active" (own package P05), never mixed
  with active ones.
- Owner's item 3: links to an organisation from a Canada-located vendor's own site count as a relationship at three
  strengths, kept apart: client listing (client / case-study / testimonial / portfolio page, logo wall "trusted by",
  customer story: P06–P08) and any other page of the vendor's site (P10, weakest).
- Private buyers are the focus: customer stories of Canada-HQ vendors (tools/customer_stories.py), home-page logo walls
  (tools/logo_walls.py), deeper client pages (tools/client_lists2.py), logo names resolved in Wikidata (tools/logo_sites.py),
  newswire.ca contract announcements and EDC buyer financing (dated, counted as active).
- Owner's item 2 (vendor located in Canada through a business-registry name match, e.g. the rejected Nova Scotia records)
  is approved for its own labelled package only; not built yet.

## 2026-11-01 22:20 — claude: dated private buyers from vendors' own news releases; announcements 12–36 months old are "likely active"
- tools/vendor_news.py reads the newsrooms of the ~42,600 Canada-located vendor sites (batch903/904/902 + the Canada-HQ
  list): release URLs from sitemaps / newsroom pages whose slug carries a deal word, titles parsed so that the site owner
  is the seller ("<Buyer> selects <Vendor>", "<Vendor> wins contract with <Buyer>", "<Vendor> to provide <Buyer> with",
  French forms). Financing, investment, grants, M&A, MOU/LOI, distribution, partnerships, prizes and rankings are dropped.
  A vendor site that is not .ca (outside the curated Canada-HQ list) must show a Canadian dateline, head-office phrase or
  postal code in the release, so a global group's newsroom never stands for its Canadian entity. Buyer website: a link in
  the release that spells the buyer, else an exact Wikidata label match (any country; one-word names only when the domain
  spells them). Leads carry row.news_date, so lead_scanner dates them.
- rank.py: a deal announced by the Canada-based vendor (newswire dateline, EDC transaction, own news release) dated in
  the last 12 months is tier B (GOLD with an invoicing mailbox); 12–36 months old is tier L, package P05 (owner's
  12–36 month rule), never mixed with active ones.
- same_org: a sibling campus domain (@tamuk.edu for tamu.edu, @uncc.edu for unc.edu) is not the buyer's own mailbox
  (found in the P01 spot-check).

## 2026-11-01 22:35 — claude: US nonprofits' Form 990 contractors in Canada as dated private buyers
- tools/irs990_contractors.py reads the IRS e-file XML (2026 + 2025 releases): a highest-paid independent contractor
  (990 Part VII-B, 990-PF Part VIII) whose address in the return is a foreign address with country CA is a Canada-located
  vendor proven by the source; the filer is the buyer (name, website from item J, fiscal year end = record date).
  Persons are skipped. Evidence page: ProPublica Nonprofit Explorer's full view of the same filing (EIN + object id).
- rank.py: any dated non-client relationship (deal announcement or payment record, incl. Form 990) 12–36 months old is
  tier L (P05, own package); within 12 months it is tier B (Gold with an invoicing mailbox).

## 2026-11-01 23:00 — claude: the 10k Gold arithmetic (for the owner's goal; rules unchanged)
Gold = distinct buyer with a dated relationship (active, or deal / payment dated in the last 12 months) with a
source-proven Canada-located vendor AND a confirmed invoicing / AP mailbox. Today every source together holds about
3,100 active contract buyers + a few hundred dated leads, so Gold cannot pass ~3,400 even at 100% AP coverage; the
lever is finding NEW dated relationships at scale, then AP mailboxes. Checked tonight:
- Vendor client listings: 30,472 buyer domains, but undated (P06–P08, never Gold). Public-looking clients: ~2,400.
- Buyer-side documents (council / board approvals naming a Canadian vendor): Canada-HQ vendors usually contract
  through US subsidiaries (e.g. Riverside County 2026: "Geotab USA, Inc., Las Vegas"), so few pass the vendor rule.
- EDC: 87 buyer-financing deals in two years (exhausted). IRS Form 990 2025+2026: 294 buyers, 61 with a fiscal year
  ending in the last 12 months. US subaward primes ~300; newswire ~136; vendor newsrooms ~1 per 100 vendor sites.
- Collapsed sub-units: 3,861 buyer keys inside 3,113 active rows (not a large lever).
Plan: (1) AP mailbox for every active non-Gold buyer (~2,600: P02–P04 + 967 with no email), search rounds every
~20 min, active first; (2) every new dated private source as found; (3) keep the long crawlers running.

## 2026-11-02 07:45 — claude: new dated private sources; dated customer stories; Colombian site search
- Built and running (leads in ~/cch-leads, picked up by lead_scanner): Colombia DIAN import declarations (exporter
  country Canada: 1,675 importers, 1,205 in the last 12 months), SEC/PCAOB providers in Canada (Form AP, ADV Sch. D,
  Form D, N-CEN: 1,066 in 12 months), Toronto + BC consultant-lobbyist registrations (1,006), FERC EQR, COR, EPA
  hazardous-waste exports, Form 5500 Sch. C, FEC, Czech register, Spain menores, CMS (1,069), Texas 1295 + state
  checkbooks (169), IRS 990 (61), dated customer stories (running). Blocked and skipped: federal OCL zip (Cloudflare),
  Québec Carrefour (403), Ontario OICO (login).
- A customer story that a Canada-located vendor dated within 12 months counts like its own news release ("deal
  announced by the vendor"), labelled with its source; undated stories stay client listings (owner: P06 not Gold).
- Website search for Colombian importers: the e-invoicing query returned only DIAN guidance (180 searches, 1 site);
  the query is now "<name> Colombia". Clearbit autocomplete finds ~2% of these names (exact name + verified title).

## 2026-11-02 08:40 — claude: Common Crawl AP-page mining stopped (politeness incident)
tools/cc_mine.py located AP / vendor / invoice pages in the Common Crawl URL index (DuckDB over the public columnar
index) and read their WARC records by HTTP range. A test ran at ~35 requests/second (an agent's mistake, against rule
9) and data.commoncrawl.org answered 403. Both the index scan and the miner were stopped; per rule 6 the source is
treated as blocked for now. The yield seen before the block was thin (0 AP-grade mailboxes in 810 pages; projected
<300 AP-grade organisations for a whole crawl), so it is not worth resuming. Lesson: every tool gets an explicit
per-host request cap in code, never only in the instructions.

## 2026-11-02 13:30 — claude: spot-check of 20 Gold rows before shipping, and fixes
An independent check of 10 P01 + 10 P01T rows: P01 10/10 without a blocking failure (7 fully clean); P01T 2/10 clean.
Causes fixed in rank.py: lead rows never ran same_org (a contractor's or the parent city's mailbox reached a lead);
receivable / tuition mailboxes passed as AP; the same organisation could appear twice (domain-named lead + named row);
the "Québec ... no closing notice" label appeared on non-Québec rows. Still open: department-suffixed lead names
("City of X — <dept>") are not folded into the parent; evidence that is a web.archive.org copy; FERC rows link the
quarterly file rather than the record.

## 2026-11-03 06:15 — claude: pre-shipment spot-check (3 rows per package) and fixes
Independent check of 39 rows: 22 clean. Strong: P01 2/3, P01T 2/3, P02 3/3, P06T 3/3. Weak: client-listing and link
packages (P06–P08, P10: building names, resellers, partners, a designer's footer credit, the vendor's own events),
P05 (ended lobbyist registrations counted as likely active), some receivable mailboxes typed AP, one person's address.
Fixed before shipping: JSON-escape debris on addresses; enrichment contacts without the page they were read on are
not delivered (their evidence key is 'snippet'); one delivered row per mailbox (branches sharing a government's
central box no longer count as separate buyers). Final counts 11:12Z: P01 490, P01T 24, P02 199, P03 196, P04 1,393,
P05 339, P06 154, P06T 964, P07 163, P08 2,183, P09 382, P10 2,610, P11 395; 9,492 delivered rows with a mailbox.
Open: tighten client-listing extraction (exclude partner / reseller / credit / event links), use lobbyist end dates.

## 2026-11-03 — claude: packages P12 / P13 and full field completeness (owner's request of 2026-11-03)
- P12 "weaker relationship (within 5 years)": an ended contract (ended_*.jsonl.gz) or a contract whose vendor is in Canada
  only through an exact / strong business-registry match with a Canadian registered office (owner's item 2 of 2026-11-01),
  dated on or after today minus 5 years; own confirmed mailbox; organisations not already in a row. Small (31 today):
  the release has only ~400 buyers in the unverified-country file and ~360 in the ended files, most already ranked.
- P13 "inferred relationship (no record)": every other organisation with its own confirmed role mailbox gets the
  Canada-located vendor it very likely pays, with the law / market fact and a confidence: federal body → Canada Post
  (exclusive letter privilege); Ontario municipality → MPAC; QC / MB / SK / NB / NU → the provincial electricity utility
  (BC Hydro at medium / low); anything else in Canada → Canada Post (medium for municipalities / institutions, low
  otherwise). Vendor locations are quoted from the vendors' own sites. Organisations not shown to be in Canada get none.
- Delivered cells are never blank: derived fills from the record and the release's vendor / buyer tables, else the
  literal not_published. Also fixed: government mail domains are anchored on a dot (aicanada.ca was read as federal),
  and the mailbox choice among a buyer's keys is now deterministic (a set's random order used to break ties).

## 2026-11-03 12:40 — claude: owner "add them all" for Gold; small categories built; robots-respecting cuts
- The owner (2026-11-03) asked to add every small category that yields buyers with an AP mailbox. Built
  (tools/small_sources.py): Ontario FIR Schedule 02 auditor of record (226 municipalities, 2026 filings: the audit firm
  is a paid supplier; firm address from the firm's site or the municipality's audited statements letterhead) and ACI
  World ASQ 2025 airports (paid survey programme, Montréal). eSCRIBE / D2L customer portals (tools/tech_portals2.py)
  feed P01T. Cross-web e-mail-domain search for 3,301 active buyers without an AP mailbox ("invoices "@domain" ..."):
  160 searches, ~15 organisations with a page — dropped as a method.
- Not used, to respect robots.txt: BC SOFI vendors proven through the OrgBook API (robots.txt disallows /api/) and the
  FNFTA audit-report class (robots.txt answers 401, which our fetcher treats as disallow-all). Leads moved to
  ~/cch-leads/disabled/. A Corporations Canada bulk-file match could replace the BC class later.
- Measured AP-mailbox rates (strict invoicing types): universities ~12%, school districts ~11%, cities ~7%, counties
  ~6.5%, companies / hospitals / libraries <2%; eSCRIBE customers 28–41%.

## 2026-11-03 19:55 — claude: auditor's report as a dated record; one organisation, one mailbox, the strongest record
- **fs_auditor (tools/fs_auditor.py, no AI).** An organisation that already publishes its own invoicing mailbox but has
  no dated record gets one from its OWN audited financial statements: the independent auditor's report signed in the
  last 12 months, the signature block printing the firm's city + province (the record itself puts the vendor, the audit
  firm it engages and pays, in Canada), the firm named in the report, its letterhead or "audited by ..." (or read from
  the signature image by on-device OCR on the owner's Mac, labelled so in the quote). The statements must name the
  organisation. First run: Canadian AP-grade organisations without a dated record (328), then every other Canadian
  organisation with a confirmed mailbox (20,259; moves P13 rows to P02-P05 when dated). Sample: 21 of the first 211
  kept; most misses are sites whose statements link the crawler cannot find.
- **rank.py.** (1) Leads are taken strongest first (dated record > service seen on the site > 12-36 months > client
  listing > other link), so a weak link no longer claims an organisation's domain before its dated record. (2) A lead
  whose own key has no mailbox yet borrows the confirmed mailbox of the same organisation found under another key, only
  when one organisation holds mailboxes on that registrable domain and the names fit (a person named in a customer story
  never borrows a university's mailbox). (3) A dated lead from the last 12 months upgrades the one delivered row with the
  same website domain when that row's relationship is older or undated. (4) Leads whose vendor is redacted / withheld
  are dropped. (5) "manufacturing" no longer counts as "factur" (FutureManufacturing@nsf.gov was typed invoicing).
  Local run before the fs_auditor leads: Gold 502 -> 530, P01T 34 -> 40.
- **Crawler fix (tools/ap_crawler.py, tools/deep_pages.py):** an address is located only as a whole token (ap@x inside
  rap@x is not ap@x); an address seen only in a link target while the page shows a longer one is skipped (the
  "ccountspayable@" rows were mikisewcree.ca's own typo'd mailto, not a crawler cut).

## 2026-11-03 21:40 — claude: the Gold programme (owner: "get Gold to the thousands, private and public, full autonomous")
Gold is bounded by organisations that BOTH publish an invoicing mailbox AND have a dated / active Canadian-vendor
record (today ~1,150 confirmed AP-grade organisations, 579 of them Gold / Gold-T). New engines, all no-AI, all on the
owner's Mac, each writing leads the bridge picks up:
- **tools/news_match.py** — our ~114,000 known organisations (buyers, crawled sites, leads) matched by name in the
  title / first paragraphs of Canadian vendors' own dated releases (4,325 newsrooms: Wikidata-listed Canadian
  companies, the Canada-HQ list, every newsroom vendor_news.py found releases on), next to a buying cue and away from
  financing / M&A / prize / partnership / sponsorship cues; vendor location from the release's Canadian dateline.
  (vendor_news.py's title parser gave 22 leads from 51,000 releases; the dictionary finds the organisations we care
  about — the ones with mailboxes — wherever the release names them.)
- **tools/exchange_listing.py** — TSX / TSXV issuers (tsx.com directory, websites from TMX's public quote service) whose
  OWN site prints "TSX: ABC": an active paid service (annual sustaining listing fee) of TMX Group Limited, Toronto
  (HQ quoted from tmx.com/privacy-policy). Tier T like the other vendor-hosted / buyer-published signals; ~3,000
  private-sector buyers; their sites are then crawled for the invoicing mailbox (exchange_sites.csv).
- **tools/tech_relationships.py --source cdx** — customer portals enumerated from the Internet Archive's CDX index
  (paginated, 3 s apart) instead of Common Crawl (403 after the 2026-11-02 incident); new vendors with HQ quoted from
  their own sites: Benevity (Calgary; <company>.benevity.org, enterprises), Coconut Software (Saskatoon;
  <bank>.coconutcalendar.com, 188 credit unions / banks), Möbius / DigitalEd (Waterloo; <inst>.mobius.cloud, 244
  universities). Dropped after checking their sites: Igloo (Appspace, Tampa), Bonfire / Questica (Euna, US), PerfectMind
  (Xplor), Achievers / Axonify / Intelex tenant pages (robots.txt disallows them; HQ is Canadian, so buyer-side mentions
  may still be used), SDPC registry (members-only since 2022; robots disallows /agreements/).
- **tools/site_finder_names.py** — names compared without legal suffixes and queried without them (the autocomplete is
  prefix-based): "LOCKHEED MARTIN CORPORATION" now resolves; 3,275 dated lead buyers without a website re-tried.
- **tools/fs_auditor.py** continues over the 20,000 Canadian organisations with a confirmed mailbox (102 kept of the
  first 1,698; most misses are statements the crawler cannot find).
- Standing prompt for the loop: prompts/claude_gold_loop.md (re-fired hourly by a scheduled task).

## 2026-11-03 23:59 — claude: loop #2 notes
- **Mac clone stuck in a rebase (push_loop "push attempt failed" from 18:52 local).** Eight autostashes had piled up.
  Fixed by: abort, save every version of data/incoming/claude/*.csv (working tree + each stash), reset to origin/main,
  union the RESULT files as CSV records (not lines: quoted fields span lines, a line union corrupted crawl01 for one
  push, repaired in the next commit), newest working copy for claude_buyer_leads.csv. Verified: every record of the
  pre-incident origin file and of the working copy is in the committed file (46,879 distinct records; the working copy
  held 56,178 rows because the crawler appends duplicates). push_loop restarted.
- **BC SOFI (small_sources.py bcsofi --proof site):** 214 BC bodies, 46 with a FY2025 schedule of payments whose
  suppliers are proven by the Canadian street address on their own site (112 dated payment records).
- **provider_mentions over 20,587 Canadian sites:** 88 leads — Voyent Alert! (28 municipalities), Brightspace (18),
  PressReader (14), Edsby (10), School Cash Online (9), Amilia (6); benefits carriers almost never appear with a binding
  phrase on public pages (1).
- **exchange_listing finished:** 956 of 2,109 reachable issuers print their TSX / TSXV ticker; crawl of their sites for
  the invoicing mailbox: first 340 → 167 sites with a role mailbox.
- **Benevity:** 442 enterprise portals read; websites resolved from the portal slug (microsoft.benevity.org → microsoft.com,
  first domain label = slug, home page title checked).

## 2026-11-04 02:40 — claude: loop #3 notes (owner 20:56: "every entry of every package as complete as possible", "×10")
- **Member / regulated-payer relationships are their own packages, P01M / P06M** (contrib/claude/rank_buyers: tier M,
  GOLD-M): the organisation is on the CURRENT list the Canadian body publishes (IESO / AESO participants, OSFI, CDIC,
  Payments Canada, CBA, CLHIA, IBC, Electricity Canada, CCUA, CICan, Alberta Municipalities ...) and pays it (fee basis and
  the body's head office quoted). Kept apart from P01 / P01T because the body is a regulator or association, not a
  supplier the buyer chose. tools/member_lists.py: 2,290 leads; websites via site_finder_names, then the crawler.
- **Customer stories at scale** (tools/customer_stories.py --vendors-file, 3 shards over 42,000 Canadian vendor sites):
  a dated story (≤12 months, vendor proven in Canada from the contract data or its own site address) is tier B; an
  undated one is a client listing (D). Vendor proof per vendor, never from the name.
- **Mailbox-first discovery** (tools/ap_pages.py): web searches locate pages that publish an invoicing mailbox; the reader
  (no AI) keeps the page's own role mailboxes (same_org against the page host) with the quote; the organisations found
  (apfirst_orgs.csv) are then fed to fs_auditor / news_match / exchange_listing for the dated record. Round 1: 122 URLs →
  89 rows (83 AP-grade). Town-by-town queries return job postings; sector × province queries work.
- **Every field the record gives** (tools/lead_scanner.py record_details → claude_lead_details.jsonl.gz, rank.py
  apply_details): amount (with its source field named; asset / budget / valuation fields excluded), identifiers (JSON of
  the id-like fields), dates, vendor address fields, title. 47,489 of 54,666 lead buyers carry details.
- **Completeness engine** (tools/org_contacts.py, 48 workers on the Mac over 37,913 buyer + vendor domains): head-office
  address, phone and role mailboxes from each organisation's OWN site, evidence URL + quote + date; rank.py fills
  buyer_address / buyer_phone / vendor_address / vendor_phone / vendor_emails and names the page. Contact pages are read
  before the home page (footers list several offices); the head-office / city-hall labelled address wins; Incapsula /
  Imperva walls are `blocked`.
- **registrable() fixed for public suffixes outside Canada** (tools/ap_crawler.py): govt.nz / ac.nz / vic.gov.au /
  ci.<city>.<st>.us / k12.<st>.us / co.jp ... were collapsing to the suffix, so the Department of Conservation's
  info@doc.govt.nz passed same_org for Christchurch City Libraries (ccc.govt.nz). One label above the shared suffix now.
- **Mac shell incident:** `pkill -f "lead_scanner.py --bridge"` matched the MacOS-MCP shell's own bash and killed it; the
  tool no longer answers. All Mac work now goes through Control_your_Mac (osascript `do shell script`); processes are
  killed by PID from `ps`, never by a pattern the command itself contains; background jobs are started with
  `(nohup … > log 2>&1 < /dev/null &)`.
- **Where Gold can still come from (honest):** the upgrade searches (10 known domains per search) have now covered almost
  every A / B / T organisation with a website (B_908 holds the last 189); the rest publish no invoicing mailbox that a
  crawl or a search can see. New Gold comes from NEW organisations with a dated record (member lists, stories, tech
  portals, auditors, exchange issuers) × the ~10 % that publish an AP mailbox. The search budget is therefore spent on
  B_908, then mailbox-first sector queries (Q_04–Q_11) and client-listing organisations (B_909–B_911, P06 growth).

## 2026-11-04 04:05 — claude: loop #4 notes
- **tools/buyer_pages.py direction rules** (after a first run at ~40 % precision): the vendor must be the OBJECT of the award —
  a cue just before the name ("awarded the contract to", "has contracted", "engaged", "services of", "mandaté à") or just
  after it ("has been awarded the tender", "will provide"), or a bid-table line with an amount on an award page; a name
  after "from" / "by" / "par" is the other party (the site's organisation is then the supplier); on company sites the
  symmetric words (agreement / contract with) do not count; prize, sponsor, awareness and calendar pages are skipped;
  every occurrence of a name on the page is tried (headlines name the firm, the body carries the cue); names are matched
  only when written as a name (capitalised) and only if one of their words is rare among vendor names and not an everyday
  word. Second run: 8 of 8 sampled leads correct (Enbridge Gas ← Dillon Consulting, Truro ← BioBurn Pros, Martensville ←
  Nustadia, Timmins hospital ← Waterhouse Executive Search, St. Thomas hospital ← Chorley & Bisset); yield ≈ 1.2 % of
  organisations, many of them 12–36 months old (P05, not Gold).
- **GOLD-M spot-check (16 rows) → 3 referee-mailbox rules tightened in rank.py:** payments@ / accounting@ mailboxes
  published where residents e-transfer taxes and fees ("make-a-payment", "payment-methods", "e-transfer", "tax roll",
  "late fees") are general / finance, not invoicing (8 earlier Gold rows fell with them: J.P. Morgan "payments unbound"
  magazine, Addington Highlands tax payments, Canada Vape Club EMT, Ashton College tuition …); French taxpayer phrases
  ("votre facture d'impôts", "compte de taxes") mark a receivables context; ptvi.invoice@vale.com (PT Vale Indonesia, on an
  overseas shipping instruction) is not Vale Canada's mailbox. P01 564 → 560, P01T 94 → 90, GOLD-M 16 → 11: all drops verified.
- **Completeness engine results (first 18,343 organisations):** buyer_address 14,466 → 26,322 rows, buyer_phone 12,099,
  vendor_phone 14,247, vendor_emails 2,879 → 4,992. A foreign-country number on a group site (Eco-Counter +33, LS telcom
  +49) is not filled for an entity with a Canadian / US address.
- **Search round 4 (177 searches):** B_906 rest / B_907 / B_908 → p35–p37 (117 URLs, 71 buyers; deep_pages: 29 rows from
  p37 alone); Q_04 rest / Q_05 rest / Q_06 → 77 mailbox-first URLs (19 new; 8 pages with the organisation's own mailbox).

## 2026-11-04 06:25 — claude: loops #5–#6 (owner 00:37 / 00:44 / 00:50: integrity + every field + volume; soft deadline 11:00 local)
- **Owner's earlier extract (pool_audit.jsonl.gz, 65,981 e-mails):** assessed in contrib/claude/pool_audit/README.md. 65 % RBQ
  licence-holder (vendor) e-mails, mostly personal; CanadaBuys "buyer_side" rows are named procurement officers (rule 5).
  Kept as hints only: the source pages of role mailboxes on 3,237 domains we lacked (10,097 URLs → tools/ap_pages.py,
  evidence or nothing; 48 % of pages show the organisation's own mailbox) and 8 delivered buyers that had no mailbox.
- **Deliverability (learning adopted from the extract):** tools/mx_check.py — MX, else A/AAAA, DNS only, never an SMTP
  probe; a `none` is confirmed by 8.8.8.8 and 1.1.1.1 before the mailbox is removed (16 of 272 first negatives were
  resolver misses). 257 domains confirmed without a mail server → 153 delivered rows lose their mailbox (stay in Z).
- **Integrity gates** (tools/validate_deliverable.py, VALIDATION.md written by the rank workflow): all hard gates PASS on
  37,088 rows; one lead row without a named vendor (CDP) found and excluded by rank.
- **Every field:** rank.py now carries instrument type / procurement method / commodity / description / bids from the
  record; AP phone, invoice mailing address, invoicing requirements, payment terms, PO requirement and invoice portal from
  the lanes' result rows (same page as the verified mailbox); registry id / url / registered address / trading name;
  AP contact name only as printed next to the AP mailbox with a known given name or honorific and a finance role word
  (85 rows; the first heuristic gave 615 with ~50 % place names and titles — rejected). tools/org_extras.py reads 61,598
  sites for the copyright-line legal name, BN / GST-HST / charity number / NEQ / QST as printed, logo, language.
- **buyer_pages round 2:** company / association / news pages name third parties (1 true lead in 9) → round 2 restricted
  to public bodies and institutions; prize / appointment / historical / event contexts dropped; "Last, First" and
  given-name vendor names dropped; "with" reverses only on company sites. **Accounts-payable listing mode** added
  (council lists of accounts / cheque registers: every dictionary vendor on a line with an amount, dated by the
  document; agenda packages scanned for the list-of-accounts section; the buyer's meeting portal followed one level).
  eSCRIBE renders agendas in JavaScript only — no public endpoint; portal adapters (CivicWeb, iCompass, Legistar API,
  Granicus, BoardDocs) registered for jules; Ohio Checkbook local, NY Open Book, UK spend-over-£500 for codex.
- **Honest position on 10,000 Gold:** every lever that respects the rules is running or handed to a lane; the count is
  bounded by organisations with a dated Canadian-vendor record × the ~10 % that publish an invoicing mailbox. The
  payment-listing sources (councils, school boards) are the only pool large enough to change the order of magnitude,
  and they need portal adapters.

## 2026-11-04 08:40 — claude: loops #7–#8
- **Second pass on the Gold-eligible pool:** 5,466 A / B / T / M organisations still without an invoicing mailbox were
  re-searched with a different query (INSTRUCTIONS_BATCH3.md); first 5 files → 342 URLs for 194 buyers (p39), deep_pages
  finds a mailbox on ~22 % of them — each one is a direct Gold / GOLD-T after the referee. Remaining files B_935–B_946
  run one block per loop. The city-by-city mailbox-first queries (Q_13–Q_16) gave 58 URLs for 160 searches: dropped in
  favour of the second pass.
- **Owner's extract pages read:** 10,097 pages → 4,502 with the organisation's own role mailbox (referee verifying in
  batches: 804 ap: keys verified so far).
- **buyer_pages round 2 (public bodies) sampled after the listing mode:** multinational names on non-Canadian buyers'
  pages (Motorola Solutions on a Wisconsin county) and persons (artists) slipped through → vendor names on non-Canadian
  buyers' pages must say Canada; two bare words are a person; another public body as the sentence's subject (a ministry's
  project reported on a town's site) is not this buyer's purchase; conservation / watershed / promotion bodies are not
  vendors. 10 leads pruned; round 2 re-run under the new rules.
- **org_extras finished its first pass (61,598 sites):** BN never read out of a URL / identifier; copyright-line legal names
  lose trailing navigation words.
- **Data-loss incident (08:50Z) and fix:** tools/ap_pages.py held its output file open for a whole run inside the clone;
  push_loop's rebase / autostash replaced the file's inode, so 4,502 rows written after that went into an orphan and were
  lost (ap_crawler / deep_pages open-append-close per row and were not affected). Fix: engines with long-lived handles
  write to ~/cch-crawler-state/stage/, tools/stage_merge.py unions staged records into the clone before each commit (also
  resolves a conflicted CSV by keeping every record of both sides), push_loop v2 stashes only data/incoming/claude by
  name and never pops a foreign stash; the two leftover autostashes were mined (15 rows) and dropped; the 4,502 pool pages
  are being re-read.
- **10:55Z spot-check of the 3 new Gold rows:** Novartis Pharmaceuticals Canada carried `invoices.aunz@novartis.com` (the
  group's Australia / New Zealand box, from a global supplier PDF). Rule added: a mailbox whose name carries a region
  token (aunz, anz, apac, emea, latam, uk, usa, india, china, france, germany, japan, singapore, ptvi …) is not the box of
  an entity in another country — 16 rows lose their mailbox (WSP Global uk-invoice@, Nike emea.ptp.invoices@, Citibank
  Canada isupplier.emea@, Thomson Reuters invoices.latam@ …).
- **Relationship searches for AP-grade organisations without a dated record (R_001, 30 searches, 45 award-page URLs):**
  buyer_pages --urls found no dictionary vendor with a cue on them; the second R file is not worth the budget.

## 2026-11-04 06:50 (claude) — push_loop v3: git never touches the live clone again
v2 (stash → rebase → pop) stalled from 06:00 to 06:40: `git stash push -- data/incoming/claude` failed with "does not match
index" while ap_crawler appended to `claude_buyer_ap_results_crawl01.csv`, the rebase then refused the dirty tree, the push was
non-fast-forward three times per cycle, and two earlier stashes (23 rows) were never popped. Root cause, same as the 02:00
incident: engines write into the clone around the clock, and every git operation that rewrites that working tree races them.
Decision: `tools/mac/push_loop.sh` v3 + `tools/push_snapshot.py`. A separate worktree (`~/cch-crawler-state/pushwt`, branch
`pushwt` reset to `origin/main` every cycle) receives snapshot copies of the live files (half-written last line dropped;
for append-only `*_results_*.csv` the lines present only on origin are kept; a file that origin changed after the live copy
was last written is left alone), commits and pushes `pushwt:main`. The live clone's own HEAD no longer matters: tasks and tools
are deployed with `git fetch origin main && git show origin/main:<path>`; mx_check reads `org_mailboxes.csv` from a
`git show` copy, never from the live checkout. The 23 stashed rows were appended back to crawl01 before the switch.

## 2026-11-04 07:00 (claude) — referee-confirmed mailboxes only (Gold and P02–P10)
A random spot-check of five P01 rows showed two whose `email_check` was `from dataset enrichment`: mailboxes the dataset
build had taken from a crawled page or a targeted search, never re-fetched by the referee, 53 of the 168 such delivered rows
with no page quote at all ("(targeted search)"). Owner's standard is "ironclad": a mailbox counts only when the referee saw it on
the cited page. Decision: (1) the 168 mailboxes are re-submitted as `data/incoming/claude/claude_buyer_ap_results_dsenrich01.csv`
so the referee fetches every page; (2) `rank.py` ranks a dataset-enrichment mailbox below any confirmed one and never as Gold;
(3) `batches.py` accepts only `confirmed` in P01–P10, P12, P13 — an unconfirmed mailbox waits in P11; (4) `validate_deliverable.py`
gate 3 fails on any non-confirmed mailbox outside P11. Expected effect: P01 dips by up to 82 rows on the first re-rank and
recovers as the referee confirms the pages (the ones it cannot see stay out, correctly). `validate_returns.py` ROLE_HINT now
recognises bilingual role boxes (`water-eau@`, `dfotenders-soumissionsmpo@`, `communications.<org>@`, `travaux.<x>@`, customer/client).

## 2026-11-04 08:05 (claude) — every referee-verified mailbox counts; legal-name and P13-name hygiene
- `coord/results/org_mailboxes.csv` keeps one mailbox per organisation key, so a verified invoicing mailbox could hide behind a
  general one or behind one rank.py rejects as person-like (Dalhousie: `fin.pay@` kept, `apinvoice@` verified too). rank.py now
  also reads `coord/results/verification_log.csv` (every verified / cross_verified key + mailbox) with the lane row's type, page
  and quote, and keeps the best graded mailbox per key: 587 organisations gain a better mailbox; P01 +12 (e.g. City of Kitchener,
  City of Windsor, London Hydro, University of Regina — `accountspayable@` boxes that a lane had filed as "finance" or "general").
- A mailbox NAMED for invoices / accounts payable (`accountspayable@`, `ap@`, `cap@`, `factures@`) is graded invoicing whatever the
  lane's label, after the receivables demotions.
- `first.last` locals whose first token is a first name are persons even when the surname looks like a role word
  (`marie.paiement@`), unless the second token is an unambiguous role word; finance abbreviations (`fin`, `acc`, `acct`, `pay`,
  `inv`, `ar`, `cp`) count as role tokens.
- Legal names from the copyright line: fragments ("Information posted by the Government of Canada is subject to the Copyright
  Act"), web-platform copyrights (SchoolMessenger, SportsEngine, LaunchIT, CivicPlus…) and names cut at a hyphen by
  org_extras ≤ 2026-11-04 ("Municipalité de Saint") are dropped (384 rows); org_extras now cuts only at a spaced dash.
- P13 rows whose "buyer" was a bare domain or a page title ("Contactez-nous") take the site's legal name when one is printed
  (794 rows), else the mailbox's domain (5 rows).

## 2026-11-04 10:15 (claude) — deadline state (owner's 11:00 soft deadline)
Final pre-deadline re-rank 15:12Z: **P01 Gold 565**, P01T 89, P01M 18 · P02 333 · P03 230 · P04 1,597 · P05 380 · P06 164 · P06T 2,425 ·
P06M 167 · P07 242 · P08 3,060 · P09 371 · P10 2,605 · P11 517 · P12 23 · P13 36,579 — 49,365 delivered rows in 17 packages, all seven
integrity gates PASS (VALIDATION.md). Since 07:00: push_loop v3 (git never touches the live clone), referee-confirmed-only rule for
every package but P11 (168 dataset-build mailboxes re-verified: 132 confirmed, 36 out), every referee-verified mailbox per
organisation considered (not only org_mailboxes' single pick), AP-named mailboxes graded invoicing, first.last persons rejected,
legal-name and P13-name hygiene, label/grade consistency, mx_check over 55,015 domains, search passes 3 (third query), 4 (documents),
5 (supplier EFT / direct-deposit forms) and the no-website and re-evidence rounds (p42–p47). 10,000 Gold was not reachable under the
quality rules: Gold needs an organisation with a dated Canadian-vendor record in a public source AND a published invoicing / AP
mailbox the referee can see; the first set is ~7,000 organisations after merging, roughly one in ten publishes such a mailbox, and
every remaining lever (more passes, documents, forms, no-website names, relationship searches) now yields single digits per round.
The loop continues until end of day: engines, hourly referee / re-rank, a search round only where a pool still yields.

## 2026-11-04 10:50 (claude) — e-mail security posture in every row; webmail addresses out
Owner (10:21, 10:45): which delivered mailboxes have no DMARC record or `p=none`, and put it in every package. `tools/dmarc_check.py`
(DNS TXT at `_dmarc.<domain>`, organizational-domain fallback for subdomains, SPF at the domain, negatives re-confirmed through 8.8.8.8;
queries go straight to 1.1.1.1 because the Mac's stub resolver serialised bulk lookups) → `data/incoming/claude/claude_dmarc_check.tsv`.
rank.py adds eight columns after `email_deliverability`: `email_security_posture`, `dmarc_policy`, `dmarc_record`, `dmarc_record_domain`,
`spf_policy`, `spf_record`, `mail_provider` (from the MX hosts), `dns_checked_date`. First full check (15:35Z): of 49,365 delivered rows,
16,479 no DMARC record, 19,611 p=none, 8,631 quarantine, 4,596 reject; among the 1,321 invoicing/AP mailboxes 91 / 377 / 408 / 445.
Summary `coord/results/ranked/DMARC.md`, list `dmarc_no_enforcement.csv`. Webmail addresses (gmail, hotmail, outlook, yahoo, icloud,
proton…) leave the delivered packages (159 P13 rows, tiny businesses): a webmail account is not an organisational mailbox, whoever
publishes it. ISP-hosted municipal mailboxes (videotron.ca, bellnet.ca) stay, labelled `mail_provider = ISP mail`.

## 2026-11-04 11:05 (claude) — every row tells its own story (18 narrative / provenance / aggregate columns)
Owner (10:50): each row must state the nature of the relationship, how it was found, and carry everything known about buyer and vendor.
rank.py now derives, from the final values of each row: `buyer_type`, `relationship_kind`, `relationship_detail`, `how_relationship_was_found`,
`mailbox_provenance` (lane / tool, page, quote, retrieval date, referee verification, DNS + security posture, lane file and task id — from the
lane result files joined by key + mailbox), `buyer_facts_provenance`, `vendor_facts_provenance`, `method_notes`; per-buyer aggregates over the
whole contract dataset (`distinct_canadian_vendors`, `records_last_12_months`, `latest_award_date_any_vendor`,
`total_known_value_canadian_suppliers`, `other_canadian_vendors_sample`, `record_sources`); vendor registry facts already in the release
(`vendor_registry_status`, `vendor_registry_match_level`, `vendor_incorporation_date`, `vendor_bn_source`). 92 columns; gates unchanged (PASS).

## 2026-11-04 11:45 (claude) — deliverable files split; staff-directory pass is the live lever
- The 18 narrative columns pushed `ranked_buyers.csv` to 232 MB and P13 to 187 MB; GitHub refused the ranker's push (100 MB limit, 16:11Z).
  Fix: `batches.py` writes any package over ~45 MB in numbered part files (`P13_…_part1_of_4.csv` …, same columns); `rank.py` writes
  `ranked_buyers.csv.gz` (21 MB) and the workflow commits the gz only; `method_notes` shortened to a pointer; readers (mx_check,
  news_match) accept the gz; `validate_deliverable.py` counts packages, not files. 16:43Z run: 92 columns, 50,024 rows, 7 gates PASS.
- Sixth mailbox pass = staff directories / department contact pages (`"accounts payable" staff directory OR "department contacts" OR
  "contact us" email`, 10 sites per search): A-tier 1,250 organisations → 392 pages for 336 of them → deep_pages found a mailbox for
  83 (136 rows) — by far the best yield of the day (the first five passes asked for invoice pages, documents and forms). The same pass
  runs on the 1,350 B-tier organisations (p50 = first 2 files, 172 pages); the rest follow in the next loops.
- Payment-listing search on the 180 public bodies that have an AP mailbox but no dated record: 9 bodies with listings, 0 dated
  vendor matches (buyer_pages.py) — the relationship side stays closed under the rules.

## 2026-11-04 13:40 (claude) — shared government domains: another agency's mailbox is not this buyer's
Spot-check of new Gold rows: `bi-centraloffice.ap@tn.gov` read on tn.gov/correction/… was credited to the Tennessee Department of
Transportation, and `micasevendordirectdeposit@gov.sk.ca` (the Income Assistance vendor direct-deposit box of Saskatchewan's Ministry of
Social Services) to 15 other Saskatchewan ministries — the same-organisation check passed because the mail domain is shared by the whole
government. rank.py: on a government-wide mail domain (tn.gov, state.xx.us, canada.ca, gc.ca, gov.bc.ca, gouv.qc.ca, ontario.ca, gov.uk,
gov.au…) a mailbox counts for a body only when the page or quote names that body (distinctive word or acronym), or when it is the
government's generic AP / shared-services box (`ap@`, `accountspayable@`, `financial_sharedservices@`…) read on a page whose first path
segment does not name another agency. Verified: GNWT Financial Shared Services stays for every GNWT department; the TDOT and the 14
Saskatchewan misattributions leave. Also: rows named only by a bare domain take the site's legal name in every tier (sickkids.ca → The
Hospital for Sick Children), with fragment guards (icon glyphs, "Connect with us…", "CRICOS No", cut-at-front "s Union Partners").

## 2026-11-04 14:40 (claude) — pause state (owner: "think of it like a pause")
Final re-rank 19:38Z: P01 Gold 564 · P01T 90 · P01M 18 · P02 338 · P03 226 · P04 1,568 · P05 375 · P06 160 · P06T 2,423 · P06M 168 · P07 245 ·
P08 3,054 · P09 364 · P10 2,600 · P11 504 · P12 22 · P13 39,899 — 52,620 delivered rows, 92 columns, VALIDATION 7/7 PASS, deep audit
(tools/audit_deliverable.py, 27 checks) 11/11 hard PASS with REVIEW items explained in AUDIT.md. Everything copied to the owner's Mac:
~/Downloads/canada-contracts-gold-2026-11-04/ (packages, part files, ranked_buyers_ALL_ROWS.csv, SUMMARY, VALIDATION, AUDIT + flags, DMARC
report + list, README, DECISIONS, START_HERE.md). The hourly loop is stopped; the Mac engines (ap_crawler, crawl_some, fs_auditor, bridge,
push loop v3) keep running and the referee keeps verifying, so the next re-rank will carry whatever they add. Open items for the resume:
419 rows whose mail domain entered after the last DNS pass (soft), the T/M staff-directory files T6_004–009 (unsearched), the no-name P13
rows (20,113 known only by domain), and the honest ceiling on Gold under the rules.

## 2026-11-06 18:40 (claude) — PO numbers and every other identifier, maximal
Owner: "PO matters, go max, and all other identifiers possible". Facts first: of 803,097 contract records, 796,667 carry an identifier,
681,650 a contract/agreement number, 151,791 a solicitation number and 32,425 a purchase-order / procurement number (federal proactive
disclosure `pd_procurement_id` — the department's contract/PO number — 29,616; US purchase and delivery orders `piid` 1,304; Virginia eVA,
Vermont, WHO, Checkbook L.A., Oregon, Montgomery County). Public procurement is disclosed at award level; PO ledgers exist for a handful of
US bodies and almost no Canadian one, so the contract number is the reference most buyers can match an invoice against.
Decisions: (1) rank.py classifies every identifier key of the record (and of lead details) into 14 columns after `contract_reference`
(itself no longer truncated at 200 chars): invoice_reference_hint, po_number_as_published, contract_or_agreement_number,
solicitation_or_tender_number, award_or_notice_id, buyer_vendor_id, vendor_ids_in_record, commodity_codes, buyer_org_codes,
amendment_or_modification, all_identifiers, identifier_count, records_with_this_vendor, all_references_with_this_vendor — 106 columns;
(2) `contrib/claude/rank_buyers/contracts_export.py` writes every record of every delivered buyer with a dataset relationship (2,391
organisations, 210,225 records, ≤ 500 per organisation, 11,672 with PO numbers, 65,315 for Gold buyers) to
`coord/results/ranked/contracts/*.csv.gz`, run by the rank workflow; (3) next lever for PO volume is new PO-ledger sources with vendor
addresses (Florida FACTS, NY Open Book, state checkbooks with vendor state fields) — registered for the harvest lanes.

## 2026-11-06 19:00 (claude) — delivered: identifiers maximal (106 columns) + every contract of every delivered buyer
Re-rank 23:52Z: P01 579 · P01T 91 · P01M 18 · P13 50,536 — 63,322 delivered rows, 106 columns, VALIDATION 7/7 PASS, deep audit 11/11
hard PASS. Copied to the owner's Mac: ~/Downloads/canada-contracts-gold-2026-11-06/ (packages, Z, ranked_buyers_ALL_ROWS.csv,
contracts_of_delivered_buyers/ with 7 CSVs = 210,141 records, SUMMARY / VALIDATION / AUDIT + flags / DMARC + list / README / DECISIONS /
START_HERE). Workflow: the ranker now rebases-and-retries its push instead of regenerating (8-minute passes were losing the race to the
push loop and timing out); budget 45 min. The 3-hourly scheduled rank keeps everything current while the loop is paused.

## 2026-11-06 20:40 (claude) — the other lanes' work, accounted for
Owner (20:23): "ChatGPT and Gemini have been working this whole time — did you include it? Jules too". Check: since 2026-11-01 the lanes
pushed 56 (chatgpt), 58 (gemini), 8 (jules), 1 (codex) commits. What was already in the packages: every buyer mailbox they found —
the referee verifies all lanes' rows and rank.py reads org_mailboxes.csv (8,521 organisations' best mailbox from gemini, 888 from chatgpt)
and every verified (key, mailbox) of the verification log; Jules' sources (bids&tenders backlog, CanadaBuys history, Hydro-Québec, MERX
backlog, Montréal, PSPC standing offers, Québec City/Laval/Gatineau/Longueuil, NYC, NY authorities, Socrata sweep, USAspending subawards)
are in the release dataset through the rebuild workflow. What was NOT in the packages until now: gemini's vendor-contact batches
(160 batches, 15,427 vendors; 4,035 with a referee-verified role mailbox, 171 billing / AR boxes) — rank.py now merges them into
`vendor_emails`, adds `vendor_billing_ar_email` and `vendor_contacts_found_by` (108 columns); and chatgpt's independent QA audit of 200
random dataset records (181 buyer matches, 173 vendor matches; the 5 "no" on buyer are ministries renamed since the award; 11 "status not
supported" are SEAO ongoing_inferred records that the packages rank B/C) — now a section of AUDIT.md. The chatgpt lane also flagged three
bilingual government role boxes rejected by validate_returns' person check (systemesfinanciers-financialsystems@, directdep-depdirect@,
sigmadonneesprincipales.sigmamasterdata@) — ROLE_HINT widened. Gemini's own GitHub researcher saves 0 rows (no search grounding on the
free API key); the Gemini app on the Mac is the one producing.

## 2026-11-06 21:40 (claude) — the owner's D1–D15 list: credit-free work tonight, agent work after the reset
Owner (2026-11-06): "credits reset tomorrow … set max god mode in motion to address these" and "if there's anything you can run on my
Mac do it … go max … I can't waste a day". Decisions: (1) everything that needs no AI credits runs tonight on the Mac or in code —
the Mac had rebooted at 06:05 and every engine was dead, so `launch15.sh` restarted push_loop / sync_loop / bridge / ap_crawler /
site_finder first; (2) `tools/ap_terms.py` re-reads the evidence page of every delivered mailbox at grade ≥ purchasing and extracts,
by regex on the page's own text, payment terms, the PO requirement, the portal name and link, the AP phone and mailing address, the
printed AP contact (rank's conservative rule) and the buyer's own GST number — every value with URL, date and quote; rank.py merges it
only into blank cells and labels the provenance; (3) `tools/peppol_directory.py` read the whole Peppol Directory for Canada: 77
participants, nearly all suppliers — the honest D8 answer is that Canadian public bodies are not on Peppol, and every row now says so
explicitly rather than leaving the cell blank; (4) rank.py gains `template_language` (fr for every Québec buyer), `sensitivity_tag`
(police oversight, police, corrections, intelligence / defence / border, coroners, child protection, shelters / crisis services,
courts, mental-health bodies — a tag, never a removal), `most_recent_record_reference_any_vendor` + `records_in_contract_dataset` +
`other_relationship_sources` (dataset ↔ lead cross-reference by website domain or exact name only), commodity codes from the record's
own commodity block, and the contracts export caps Gold buyers at 5,000 records; (5) D1 goes to the two Mac lanes tonight as 2,400
tasks (the ChatGPT automation and the Gemini app are open and working): A/B/T/L buyers without a confirmed AP mailbox, never-researched
first, with the staff-directory method and the extra fields (terms, PO rule, portal, AP contact) asked for in their inboxes; the
search-agent passes (D1 second variant, D4 terms pass, D11 municipal directories, T6_004–009) wait for the credit reset;
(6) D9 needs no action — the 11-06 build carries no MPAC-inferred rows. Plan and status table: `prompts/claude_d_items.md`.

## 2026-11-08 01:40 (claude) — the referee's verdict is now sticky: a value it has seen stays verified when the page cannot be read later
Between the 06:03Z and 13:07Z builds of 2026-11-07, 20 Gold rows and ~3,500 P13 rows disappeared although nothing had changed on
their pages: twenty-odd verifier runs in a few hours (one per push) re-checked every page from a thin fetch cache, and pages that
refused GitHub's runner that morning (tn.gov, psu.edu, bcm.edu, ag.gov.au …) came back `unverified_page_unavailable`, which the
ranking treats as "not confirmed". That is a false negative: the referee HAD seen the mailbox on that page (its own log said so).
Decision: `coord/results/verified_ledger.csv` records every (value, page) the referee verified, with first and last dates. When a
later run cannot read the page (unavailable, hidden, time budget), a sighting younger than 120 days keeps the verdict `verified`
and the log notes "referee saw it on this page on <date>; the page could not be read today". The verdict is overridden only when
the page IS read and the value is gone (`not_found_on_page`) — that is the honest meaning of re-verification. Seeded from the
verification logs of 2026-11-07 06:03Z and 2026-11-08. `evidence_age_days` / `reverify_due` in every row still flag stale sightings.

## 2026-11-08 19:15 EST — AP grade: DMARC posture is a note, not a penalty (claude)
`ap_grade` A requires the invoice data a vendor needs (confirmed invoicing mailbox on the buyer's own domain with MX, published legal name, billing
address, PO rule, payment terms). The buyer's DMARC enforcement was a 3-point penalty that also blocked A; it blocked A on 269 of 463 non-A Gold rows
while saying nothing about the vendor's invoice. It stays reported (`email_security_posture`, `dmarc_*` columns, a note in `ap_grade_basis`) but no
longer decides the grade. BN conflicts and vendor-registry warnings remain penalties: those are data-integrity doubts about the parties.


## 2026-11-09 07:55 EST — stop order (owner) and what it means for the data (claude)
The paid effort stops with the final build of 2026-11-09 12:54Z. The pack's compass is `pay_on_sight` (an invoice generated from the row clears AP);
the 438 downstream benchmarks stay as a secondary scoreboard with a ceiling note wherever no honest source exists. Derived values (tax treatment,
currency, statutory terms, GST/HST account from BN9) stay in their own labelled columns and feed the invoice card; they never count as published.
Zero-cost automation keeps adding referee-verified rows; nothing lands unverified.

## 2026-11-10 04:10Z — three method decisions of the cloud row engines (claude; owner 2026-11-09 20:48 EST: "a Canadian entity gets paid because it provided a service … establish that relationship, get the other party's contact … whatever you think is best for the data set, do it")
**1. A credit line on the buyer's own home page is a relationship record (tools/credit_scan.py, tier T).** "Website by X", "Site web réalisé par X",
"Hébergé par X", "Designed by X" (footer zone only), "Powered by X" (footer zone only, free-plan services excluded), linked to X's domain: the paying
party itself names the vendor that made / hosts its site. Read live, dated, quoted (≤ 300 characters), page URL kept. Not credits: sponsors, donors,
event hosts, themes, photo credits, "developed by" / "built by" without a web noun (real-estate developers, builders), "Website: https://…" in a
resource list. First test on 1,200 inferred-relationship rows: 17.5 % of the sites carry such a line (208 credit links, 192 vendor domains).
**2. A vendor counts as located in Canada when its OWN site says so, in one of three forms, each labelled in `vendor_country_basis`:**
(a) a Canadian postal address (province + postal code) printed on its home / contact / about / legal page — the rule the row factory already uses;
(b) a schema.org PostalAddress with a Canadian postal code in the page source; (c) only when no postal code is printed anywhere and no address abroad
is found: the site's own location line — a Canadian province next to a place name ("Halifax, Nova Scotia", "Montréal (Québec)", "Toronto, ON") —
together with a telephone number in a Canadian area code. A city name alone, a phone number alone, the domain or the firm's name never count
(AGENTS.md §2.1: never inferred from the name). A vendor whose site prints addresses in Canada and abroad is accepted on its Canadian address and
the other countries are kept in `vendor_also_prints_addresses_in` (lead details). First test: 66 of 185 credited vendors proven by (a); 75 printed
no postal code on the pages read — forms (b) and (c) are for them.
**3. Mailbox rule r2 — a front-office role mailbox is the last resort.** The owner's rule of 2026-10-28 ends "`not_published` only when the organisation
publishes no role mailbox at all". The cloud mailbox crawl found nothing on two thirds of the lead sites because small organisations publish sales@,
service@, orders@, bookings@, team@, bonjour@ instead of info@. Those are kept (explicit word list in tools/ap_crawler.py `OTHER_ROLE`; a first name
is never a role) only when the site publishes no invoicing, AP, purchasing, finance or general mailbox; they are written as `ap_email_type=general`
with the note "front-office role mailbox … the site publishes no invoicing, AP, purchasing or general mailbox", so the downstream can tell them apart.
The referee re-fetches the page as for every other mailbox. Sites that gave "nothing found" under the first rule are read once more.

## 2026-11-10 05:30Z — owner 2026-11-09 23:41 EST: "one million … think differently … established online, your interpretation" → five method decisions (claude)
**1. Tier R — the registration of an organisation's own .ca domain name is a recorded relationship (rank.py, package P10R).** Opened and quoted:
CIRA's Registrant Agreement v2.2 (https://stg-saas.cira.ca/uploads/2023/06/Registrant-Agreement-Version-2.2_0.pdf): "This agreement … is between you
(the "Registrant") and the Canadian Internet Registration Authority ("CIRA")"; ""Fees" means the fees payable to CIRA in connection with this Agreement,
including an application for a Domain Name and/or any renewal"; notice address 979 Bank Street, Suite 400, Ottawa K1S 5K5. And CIRA's Canadian Presence
Requirements For Registrars v1.1 (https://stg.cira.ca/uploads/2023/05/cprregistrar_-_en.pdf): only Canadian citizens / residents, corporations "under the
laws of Canada or any province … which has a place of business in Canada", Canadian partnerships, schools and governments may be registrars. So every
live .ca name is a service paid for through a Canadian registrar under an agreement with a Canadian registry. The domain is proven live by the referee
(it re-fetched the mailbox page on that very domain). Rules: weakest lead class (any named-vendor relationship of the organisation claims the row
first); it replaces the INFERRED relationship (P13: no record) for organisations on a .ca domain; names under a government's shared domain (gc.ca,
gov.xx.ca, canada.ca) and shared mail hosts are excluded; the status says the registrant of record was not read (normally the organisation, sometimes
its web agency). Always reported as its own tier, never mixed into the named-vendor counts.
**2. CIRA's WHOIS / RDAP is not queried in bulk.** It would give the registrar's name, the registration and expiry dates and (for organisations) the
registrant's legal name — but registry lookup services commonly forbid high-volume automated queries, CIRA's terms page refused our reader, and a
million lookups is high volume by any reading. Treated like the CRA registry: not automated. (A lane with a browser may read single records.)
**3. DNS records as relationship evidence (tools/dns_services.py, tier T).** MX = who receives the organisation's mail today; NS = who serves its zone
today; SPF include = whose servers it authorises to send its mail (counts alone only when it is the single outside sender of the record — otherwise it
may be a leftover — or when MX / NS name the same provider). The provider must be proven in Canada the same way as a credited web agency (its own
site prints a Canadian address, on its own pages), named by 8+ unrelated domains, describe a hosting / mail / IT / software service, and have no free
plan. Technical domains count only with the provider's own public statement (web-dns1.com, wpdns.ca, mywhc.ca: WHC's help page, quoted). Wholesale
platforms sold through resellers (Tucows hosted e-mail) are left out: the organisation pays the reseller. Each lead carries the note that an agency
managing the account may be the provider's direct customer.
**4. DNS lookups are not page requests.** AGENTS.md §2.9 (2 requests/s per host) protects the web servers of the organisations we read. DNS lookups
never touch them. They run through a recursive resolver started on the runner (the public resolvers throttled a 3,000-domain test: 45 % timed out),
capped at 480 queries/s per runner and 300 queries/s towards any one zone (unbound `ratelimit`).
**5. Credit lane, after reading the first 25,510 leads (sample of 45: 43 right):** a "powered by" platform with a free plan is out (Webador: Dutch,
free plan, 438 leads; its "Canadian address" was a customer's subdomain); the page proving a vendor's address must be on the vendor's own hosts, or on
the domain its address redirects to when that is a rename (shared name, or the new site names the old one); a vendor that also prints addresses
abroad is kept only for buyers shown to be in Canada (.ca / .quebec domain or a Canadian postal address on their own home page) — a Minnesota city
crediting Catalis deals with the US company; a university's own web service credited by its units is internal. 1,141 leads withdrawn.
Cloudflare-obfuscated e-mail addresses stay undecoded (the referee's rule): that obfuscation exists to keep readers like ours out.

## 2026-11-10 07:25Z — bulky outputs leave git for release assets; two new statutory-fee lanes (claude)
**1. The deliverable and the big rewritten state files are release assets, not git blobs.** Measured: 5.45 GB of new git objects in 24 hours —
package CSVs 1.47 GB, `team_buyers.jsonl.gz` 1.04 GB (61 rewritten versions), `ranked_buyers.csv.gz` 1.03 GB, contracts export 0.55 GB,
`claude_org_extras.jsonl.gz` 0.32 GB, `org_mailboxes.csv` 0.23 GB, `claude_org_contacts.jsonl.gz` 0.15 GB … — and GitHub reports the repository at 8.9 GB
after ten days; the row count is meant to grow more than tenfold. A compressed file that is rewritten whole cannot be stored as a difference, so git
keeps every version. From now on: (a) each rank build is published to the release `ranked-latest` (whole table, every package in `ranked_batches.zip`,
contracts export, audit / DMARC / change lists, `BUILD.json`); git keeps the reports, `BUILD.json`, `WHERE.md` and the first 10 rows of each package
(`tools/ranked_publish.py`; if the upload fails the build is committed in parts as before); (b) `team_buyers.jsonl.gz`, `claude_org_extras.jsonl.gz`,
`claude_org_contacts.jsonl.gz`, `claude_ap_terms_pages.csv.gz` are assets of the state release `harvest-state`, with one line each in
`coord/STATE_ASSETS.json` (asset, size, SHA-256); readers call `tools/state_io.py ensure`, which downloads the current version when a checkout does
not hold it. Only files with ONE writer workflow were moved (a release asset has no compare-and-swap); files with several writers
(`claude_buyer_leads_cc.csv`, `claude_lead_details_cc.jsonl.gz`) are to become append-only shards like `lead_shards/`. History already pushed is
not rewritten.
**2. Licence held from a Canadian licensing body = a dated, paid relationship (tier M).** First source: the Régie du bâtiment du Québec's daily
open-data list of active licences (Données Québec, CC-BY 4.0: "Le jeu de donnée présente l'ensemble des détenteurs de licences actives de la RBQ").
The Régie's own page: "Chaque année, vous devez payer votre licence pour la maintenir." … "Si vous n'avez pas acquitté les droits et frais de
maintien de votre licence à son échéance, elle cessera d'avoir effet." The list gives the holder's legal name, other names, NEQ, address, telephone,
e-mail, the first issue date and "Date du paiement annuel" = "date du prochain paiement des droits d'exercice" (the dataset's field description).
Payee per the list's "Mandataire": the Régie (address printed on rbq.gouv.qc.ca/nous-joindre), the Corporation des maîtres électriciens du Québec or
the Corporation des maîtres mécaniciens en tuyauterie du Québec (each one's address and fee statement quoted from its own document). Rules:
natural persons ("Personne physique") are left out entirely; the register's e-mail is NEVER delivered or stored (only its domain is kept, to find
the holder's site); the site is kept only when it shows the holder's licence number, telephone, postal code or name; a domain used by more than three
holders is a provider's or an accountant's and ties nobody; the mailbox comes from the holder's own site through the ordinary crawl and the referee.
A licence number printed on a site the crawl reads is a second way to the same join (number looked up in the list, holder tied by name / postal
code / e-mail domain).
**3. Municipal business licences (open data) are joined to organisations by postal code + name** (`tools/biz_licences.py`): every word of the
shorter name must be in the longer one and what agrees must identify (three words, or one word that is not a generic trade / place word); several
different licensees fitting one organisation = dropped. The portals' catalogues are probed on a runner first; only datasets whose fields were seen
in the probe log are configured.

## 2026-11-10 09:50Z from claude — leads as shards; an engine's withdrawal rules reach its own leads only; a published tariff may fill the amount; registry candidates without a home-page mailbox
**1. The cloud leads are a frozen base plus append-only shards** (`tools/lead_store.py`, `data/incoming/claude/lead_shards/`). Measured: the leads
file 59.9 MB for 174,000 leads (GitHub refuses 100 MB), the details file 32 MB stored again in full at every merge, three writer workflows. A writer
loads base + shards, works as before, and saves only rows / details that are new or changed and the keys it withdraws
(`leads_` / `details_` / `gone_<engine>_<stamp>.gz`, applied in the order of their stamps; the newest record of a key wins). Opt-in per workflow step
(`--stamp` + `--engine`, `--lead-shards`), so a run queued with an earlier workflow file keeps writing the old files without harm. Every reader of
the leads file reads through the store. Not chosen: release assets (no compare-and-swap between three writers), splitting the CSV in parts (every
merge would still rewrite all of it).
**2. A merge's withdrawal rules apply to that engine's own leads.** The client-pages merge (`cc_clients.merge`) judged every record of the shared
file with rules written for links on a vendor's page (spam words, "three spam links = hacked page", page class). In the test of the store that
withdrew 10,748 licence leads (one shared record_url). Each engine now tests `platform` before it withdraws; the spam word list no longer matches
inside ordinary words ("specialist") or a surname (Kumar).
**3. A licence's amount may come from the payee's own published tariff, labelled as such.** RBQ: "Maintien d'une licence – 2026 … Général (annexe I)
884,54 $ 105,27 $ 989,81 $ … Spécialisé (annexes II et III) 442,26 $ 105,27 $ 547,53 $" and "Prenez note que les montants ne sont pas taxables"
(rbq.gouv.qc.ca, tarification pour l'entrepreneur de construction, read 2026-11-10; the same table is on the owner-builder page). The kind of licence
is read from the holder's categories in the register. The cell says "a tariff, not a payment record". Only RBQ-administered licences: the CMEQ and
the CMMTQ bill their own dues on top and their fee pages were not opened.
**4. Registry candidates, second class.** A .ca site whose home page prints no role mailbox is read up to 4 pages (contact page) after every lead
and every first-class candidate. Measured yield 10 % (200 sites). Same relationship as tier R; always reported as its own line.
**5. rank.py stays one process for now.** Measured after the memory work: 1.9 GB fixed + ≈ 12 KB per row (2.8 GB at 76,930 rows) → about one
million rows on a 16 GB runner. The sharded design (a core part holding the contract organisations and every site domain touched by a non-lead key;
other parts by hash of the lead's site domain; the core exports its column list, the names it covers and the vendor carry-over table; parts merged
by the sort key with a cross-part check for inferred rows) is written down here and not built.

## 2026-11-10 12:40Z from claude — row audit, round 2: whose site, whose name, whose address (eight rules; all measured on a full local build)
Owner 2026-11-09 23:41 EST: "keep checking … this is working, this is not working". A second pass over the delivered table looked for cells that
are true of ANOTHER organisation than the one on the row. Each rule below removed a class of such cells; none removes a row (a row whose
relationship is no longer shown becomes tier E, reported on its own line).
**1. A listing proves a relationship with the organisation whose site it is.** The Mac-era lanes tied a vendor "located in Canada" (Wikidata,
OpenStreetMap, a contract record) to a website; for a multinational's Canadian arm that website is the group's worldwide site (3ds.com for
"Dassault Systèmes (Canada)", ibm.com for "IBM Canada", okta.com for the OpenStreetMap office "Okta - Toronto"), and its customers all over
the world were delivered as customers of a Canada-located vendor. Order of the evidence, non-.ca sites only: (0) a listing inside the site's
Canadian section (/ca/, /en-ca/, ca.…) is the Canadian arm's page; (1) Wikidata — `tools/site_owner_wd.py` asks which organisations give the
site as their official website (P856) and where their headquarters are; the organisation whose name is the site's name, without a region in
its name, decides, and it sits where its same-name parent (P749) sits; headquarters abroad → the group's site; headquarters in Canada → the
vendor's own site whatever office the site reader picked; (2) Wikidata silent → the address the site prints: abroad → not shown to be the
Canadian entity's, unless a Canadian registry holds a corporation of the site's own name with its registered office in Canada; (3) no address
in Canada on file and the vendor named as a national arm ("IBM Canada", "DMG EVENTS (CANADA) INC.") → not shown. Not chosen: the share of
Canadian buyers on the site (Canadian exporters such as Genetec or D2L list few Canadian customers), the reader's single address alone (17 of
the 76 sites that print a foreign address are Canadian companies with an office abroad), Wikidata's "(Canada)" label suffix (its batch items
all carry it). The query service allowed one query a minute on 2026-11-10 ("rate-limiting to 1 req / min … during active wdqs outage"): the
tool asks 100 sites per query, one query a minute, at most four minutes a build.
**2. A vendor's own published terms can exclude the buyer.** `tools/tech_relationships.py` already quotes Shopify's terms ("United States or
Canada: Shopify Inc., a Canadian corporation"); a customer story about a merchant not shown to be in those countries is a link (tier E).
`scope_countries` on a vendor entry carries the rule; only Shopify has one today.
**3. A registered name made only of legal-form and place words is nobody else's identity.** `tools/bulk_registry_match.py` took the bracketed
part of a name for an alias ("Thermofin (3075109 Canada Inc)") — and "(Canada)", "(Québec)" too: 53 organisations carried the legal name
"CANADA INC." and its NEQ, 4 "Co-Québec inc.". The tool no longer takes a bracketed place for a name; rank.py refuses such a registry row from
any file.
**4. What a foreign organisation's site says about itself is not the Canada-located vendor's.** Its address, its telephone, its legal name and
its trading name are not taken when the site is a foreign organisation's by rule 1 ("KPMG International Limited" from kpmg.com's legal page
for KPMG LLP, Cupertino for "CoreFour Inc. (Edsby)"). A legal name stated inside the site's Canadian section stays.
**5. A footer line is a legal name only when it reads as a name.** Refused: a run of menu words, the web agency's credit ("Made by …",
"Site créé par …"), an address or opening hours, a cookie / consent sentence, a mailbox, a fragment cut inside brackets, the credit of a
government template on the site of a body that is a legal person itself ("© Gouvernement du Québec" on a centre de services scolaire). A name
stated on a page must still agree with the organisation: its site's label has to be written with the name's own words in their order (whole
words, beginnings, initials — "usask" = U. of SASKatchewan, "austincc" = AUSTIN C. C.); "Town of Cochrane" on the Cochrane chamber's site is
another body.
**6. The last label of a mailbox must be a top-level domain that exists** (IANA list, `tools/data/iana_tlds.txt`). Descriptions and search
indexes made by stripping tags without spaces print "ap@town.caDevelopment"; the glued string is on the page, so the referee verified it (125
rows of the referee's table, 560 with the verification log). The shared pattern (`validate_returns.EMAIL`) now requires a real TLD — validator,
referee, every crawler — and the crawlers drop an address that is another address plus a word. rank.py cuts a glued one back to the address
the page prints only when its domain is then the domain of the page it was read on (454 of the 560); the rest is left out.
**7. A row that takes a newer relationship drops every cell of the old one** (the old contract's identifiers, text, amounts, dates, vendor
cells), and a vendor is looked up by a site's domain only when its name fits that domain or the website finder verified it; a web host's or
registrar's own site is nobody's website (918 DNS rows of one host had carried a festival's legal name and street address).
**8. Stored page text is read again with today's rule**: the buyer's name from the stored home-page title (589 sites named: initials such as
"Comox Valley Animal Hospital" on cvah.ca), the vendor's address cut out of its quote (4,244 lead records carried the page's words in front of
the street number).

## 2026-11-10 13:10Z from claude — the referee's log and ledger are written in parts
Measured 12:50Z: `coord/results/verification_log.csv` 31.8 MB at 215,624 rows (17 MB at 133,000 three hours earlier), 96 % of the rows the
cloud crawl's. GitHub refuses a file over 100 MB: about 680,000 rows — a day away at the crawl's pace (+80,000 verified mailboxes per run).
The team lanes' rows stay in `verification_log.csv` (the file AGENTS.md §5 names); lane claude's rows go to `verification_log_claude.csv`,
`.part02.csv`, … of at most ~40 MB (`tools/parted_csv.py`), and `verified_ledger.csv` is written the same way. Plain text in a stable order, so
git stores each version as a difference. Not chosen: a compressed release asset (other agents read their rows from the checkout, some without
network), one file per day (the referee re-judges every row at every run). Readers of every row: rank.py, `tools/export_orgs.py`.

## 2026-11-10 15:10Z from claude — the rank build at the size the crawl is taking it to (disk, memory, files in git)
The table went from 96,098 rows (build 10:54Z) to 169,768 (14:29Z); a crawl run now adds ~50,000 mailboxes (335,151 lead sites read by 14:25Z).
The 13:27Z build ranked the table, published the release and then could not commit: a 151 MB table file was still tracked by git, and the
retry died for lack of memory in the DNS step. Measuring the build end to end found five more limits of the same kind, all ahead of us:

| What | Measured | Limit reached at |
|---|---|---|
| disk used by one build | ~65 KB a row: previous table as plain text, new table as plain text, the packages, a working copy of the packages (11 GB at 170,000 rows; a runner has 85 GB free — see the correction below) | ~1.3 million rows (not ~215,000 as first written) |
| scoreboard (`coverage_targets.py`) | 2.83 GB of memory at 73,600 delivered rows (whole rows held) | ~400,000 rows |
| growth report | 2.33 GB at 73,600 delivered rows | ~500,000 rows |
| DNS-posture file `claude_dmarc_check.tsv` | 213 bytes a domain, one file in git | ~470,000 domains (GitHub's 100 MB) |
| crawl result file | rotated at 30 MB only between merges; one merge brought 35 MB | a merge of ~100,000 rows |
| the ranker itself | 3.6 GB at 169,768 rows, +11.8 KB a row | ~800,000 rows on a 16 GB runner |

**Correction, 16:20Z.** The disk line was written on an assumption (a runner with ~14 GB free) that I had not measured. The first build on
the new path printed it: `/dev/root 145G 61G 85G 42%` — 85 GB free. At ~65 KB a row the old path would have filled that at ~1.3 million rows,
not at 215,000: the disk was never "one build away". The compressed-only path stays (a build uses a fifth of the disk and nothing reads the
plain files), but it was not the urgent limit; the urgent ones were the commit of a 151 MB file and the memory of the DNS step, both fixed
at 13:45Z. Every build now prints the free disk at its start, after the prep, after the ranking and before the publish.

**Decided and built (each verified on a full local build of 76,913 rows: every report, every package file and every member of the release's
zips byte-identical to the build before the change):**
1. **A table exists on disk only compressed.** The ranker writes `ranked_buyers.csv.gz` / `.jsonl.gz` and no plain copy; the packages are
   written as `<package>.csv.gz` (`tools/batch_files.py` reads them) straight from the table when the table already holds a package's rows in
   order (17 of 19 packages; the other two are small), so no second copy of the packages; `ranked_batches.zip` still holds plain `.csv` members, streamed. Disk of a build:
   2.6 GB → 0.35 GB at 76,913 rows, ~6 KB a row.
2. **A report keeps the cells it reads, not the rows.** Scoreboard 2.83 → 0.22 GB, growth report 2.33 → 0.09 GB, change list 0.36 → 0.25 GB
   and no longer a child process of the ranker (it stood next to everything the ranker still held).
3. **A file that grows with the table is written in parts** (`tools/parted_csv.py`, now also tab-separated): the DNS-posture file; the crawl
   result file changes file while it is being written. The tail refuses to push a commit that holds a file over 95 MB and says which.
4. **One build path.** `tools/rank_prep.sh` (before the table) and `tools/rank_tail.sh` (after it) are the only copies of those steps; the
   old fallback that committed the packages to git when the release upload failed is gone (it could not have worked at this size) — the build
   fails loudly instead and the previous build stays published.
5. **Ranking in parts exists and is not yet the default** (`RANK_PART=i/N`, `tools/rank_merge.py`, `rank-buyers-parts.yml`). An
   organisation's part is decided so that everything the ranker joins — a website domain under any ending, a mailbox, a borrowed mailbox —
   is in one part. Measured on two parts of the 76,913-row build: no mailbox in two parts; the same rows plus 23 inferred ones; 28 carry-over
   notes name another row of the same vendor; 4 vendor facts not carried (the row that holds the fact is in the other part).
   **What it does not do yet:** each part still loads every lead and every mailbox before it keeps its own, so a part peaked at 2.42 GB
   against 2.49 GB for one process — it buys time on the clock, not memory. The memory cut needs each table to be loaded for the part's own
   organisations only; that is the next step, before ~800,000 rows.

The 23 extra inferred rows are worth a line: one process leaves out an inferred row whose NAME another row already carries (113 such rows).
Of the 23 that a second part let through, 18 are different organisations with a common name ("Calvary Baptist Church" of another town,
"First Presbyterian Church") and 5 the same organisation on a second domain. The name rule stays as it is — it costs ~0.1 % of the rows and
its mistakes go both ways.

## 2026-11-10 17:25Z from claude — row audit, round 3 (whose record, whose name) and a referee that reads a page once
Read on the published table (build 14:29Z, 169,768 rows), then measured on a full local build (76,706 rows; the rows, the tiers and the 73,665
mailboxes come out the same — only cells change).

**What was wrong**
- 549 rows carried a site reader's record read on ANOTHER host of the same registrable domain: "Texas Department of Insurance" (tdi.texas.gov)
  on five other Texas agencies, one municipality's name, address and telephone on the sixteen others hosted on ao.ca, one church's address on
  another church on churchcenter.com, a realtor's logo on the platform that hosts it. The readers kept one record per registrable domain.
- A name printed on a page was taken for the buyer's legal name when it shared one everyday word with it: "Canadian Dental Care" (a federal
  programme) on 71 dental clinics, "Canadian Real Estate Association" on 29 brokers, "Doctor of Dental Surgery" on 16, "University" on 11,
  "Réalisation : SIGNÉ FRANÇOIS ROY INC" (the web agency) on 9, "Company name" (a template) on 4.
- A buyer's registry record stayed under the row's key after the row's name changed: "VILLE DE QUÉBEC" with the City's NEQ on a row now named
  "LES YMCA DU QUÉBEC", "UNIVERSITÉ DU QUÉBEC" on calculquebec.ca.
- 3,792 of 82,492 printed buyer addresses carried words of the page in front of the street number (opening hours, menu words, a price).
- The provincial directories were looked up by registrable domain: "Village de Godbout" for every municipality with a page on
  municipalites-du-quebec.com.

**Decided (each rule measured on the local build; counts are cells or look-ups there)**
A. **A site reader's record is a row's own when it was read on the row's own host.** Read on another host of the domain it is taken in two
   cases only: the reader read that host for this very organisation (the name it was given is the row's name: bookstore.upei.ca and upei.ca),
   or the row's host is the member directory of the body whose own site was read (business.ottawabot.ca → ottawabot.ca, from
   tools/member_live.py). Look-ups not taken: 1,838; taken for the same name: 235; taken for a body's directory host: 1,569. The readers now
   keep one record per host (tools/org_extras.py, org_contacts.py), so each host gets its own at the next reader run; the hosts of one
   registrable domain share two requests a second (tools/ap_crawler.py).
B. **A name read off a page is the buyer's legal name when the page ties it to the buyer**: a shared word that few names carry (a word in more
   than 1 in 2,000 of the 83,191 names of organisations read proves nothing), or one name inside the other, or the site's address beginning
   with / made of the name's own words ("stonechurchvet" = Stone Church Animal Clinic; not "smiledentalcare" = Canadian Dental Care). A name
   printed on three or more sites (1,053 names) is somebody else's unless it is the row's own. Not a name: a placeholder, a degree, a
   professional title, a kind of body with no name ("University", "Canadian Association"), a credit line, a piece of a sentence, a date in front.
   New, because they are the strongest statements a site makes and a numbered company shares no word with the name it trades under:
   - the site says who operates it — "operated by 1688150 Alberta Ltd", "X Ltd. («we»)" — on its own domain, naming a legal person, not a web
     platform's own terms: 104 names;
   - the site's own JSON-LD Organization node (the node gives this very site as the organisation's address): 303 names;
   - "X Ltd doing business as <the site's name>", "<the site's name>, a division of X": X is taken: 8 names.
   Legal-name cells: 36,347 → 36,092 filled; 550 gone, 295 new, 668 replaced.
C. **A registry record is left out when the name it was looked up under is no longer the row's name AND the registered name fails the test of
   rule B** while being made of a kind of body, a place and everyday words only, or naming an institution of a kind the row is not: 33 records
   (27 visible names: Ville de Québec, de Montréal, de Lévis, de Granby …, Université du Québec, de Montréal, the Canadian Real Estate
   Association). A company's registered name stays. A record of another name than the legal person the site itself states is left out too (10).
   The registry tools look a row up again when its name has changed, and look up the stated legal person when the site states one
   (tools/registry_names.py).
D. **A directory entry is a row's own when the row's site is the entry's site** (same host; same first folder when the entry's address has
   one); a site that entries of different names give is a portal and names none of them (112 sites); a directory "address" must have a number
   and a word.
E. **The address is cut at the street number**: opening hours skipped like telephone numbers; the first number followed by its street with no
   page word in between; a unit or a floor in front stays. 1,343 addresses lost the page's words, 67 kept a unit or floor that was cut before.

**Tried and not kept** — dropping every registry record whose looked-up name had changed (it removed about 55 plausible numbered companies to
remove 15 wrong public bodies); taking the bare domain's record for any host under it (a client's portal on its software vendor's domain would
get the vendor's logo, telephone and address); a frequency rule on copyright-line names (a broadcaster's or developer's name on each of its
own sites is the true owner). Known to remain: a few stated operators that are partners, not operators; JSON-LD nodes left over from a
staging site; rows on a second host of an organisation wait for the readers to read that host.

**The referee reads a page once.** Its cache of fetched pages (300,000 files, 5.6 GB) had not been saved since 11:26Z, so every run fetched
every newer page again: 80,953 pages for 4,200 new rows, 65–105 minutes a run. The verdict is in git (`coord/results/verified_ledger.csv`):
it now stands for 45–59 days for a value seen on its page, 7 for a value not on it, 3 for a page that could not be opened, and the ledger
says how the value was seen. Checked offline on today's inputs with no page at hand: 205,325 values verified on their page, 4,906 seen
earlier and 997 on an archive copy come out as in the last real run. The cache steps are gone from the workflow.

## 2026-11-10 17:45Z from claude — the DNS sweep asks who serves the zone
The sweep of the web graph's 63 M domains asked one question (is the address record on Shopify's storefront network). It now asks a second:
do the zone's name servers belong to a provider that already yields leads? 330 provider domains do today (whc.ca 21,798 leads, webnames.ca
11,992, easydns.com 6,347, namespro.ca 5,574, hover.com 5,557 …) — 88,604 leads from the 4.1 M domains looked up so far, nearly all of them
.ca. The same providers serve .com / .net / .org domains: the Canadian businesses that are not on .ca, which no engine had looked for.
- Only a watched provider's clients are kept (the list is the providers the lead rules have already accepted: proven in Canada by their own
  site, a hosting / domain / IT service, no free plan). A provider seen for the first time in the sweep is not kept: new providers come from
  the full lookups of the .ca lists, where every record of a domain is on file.
- The lead rules are unchanged (tools/dns_services.py leads): a provider that also prints addresses abroad counts only for a buyer shown to
  be in Canada.
- Cost: one more question per domain, sent to the domain's own name servers; the ending's servers see 250 questions a second per runner as
  before. The part of the list swept before today is asked the second question once the list is done.
- Not chosen: the zone files of .com / .net / .org (they list every delegation, but access is by application to each registry).
What it will yield is not known yet — the first run with the second question starts when the current one merges (~18:20Z).

## 2026-11-10 20:00Z from claude — supply: three measurements, two new store lists, one source closed
**Why now.** The 17:59Z mailbox crawl read 67,753 sites and found 5,066 mailboxes: the sites whose home page prints a role mailbox are used
up. What follows is what was measured this evening and what was built or closed on the numbers.

1. **The scan's verdict "unreachable" (1,252,393 .ca domains) hides few sites.** A random 5,000 read again (crawl-diag what=unreachable): no
   DNS record 64.3 % (+4.1 % the resolver could not say), no port answers 11.6 %, a forward to another domain 4.9 %, robots refusal 4.0 %,
   parked 2.4 %, a site of its own 5.7 % (283) — and only 19 of those 283 print a role mailbox on the home page. Of the 1,005 that answered,
   691 answered on plain http only. Decision: the scan's reader asks the plain-http copy after ANY failure of https (it did so after a TLS
   error only), and remembers which address answered; the domains are read again with the next detector, not before. Expected: about
   70,000 more readable sites, 5,000–10,000 rows. Not a large lane; the fix is cheap and stays.
2. **Shopify's own directory (shop.app) is not a source.** Its robots file publishes a storefront sitemap (26 files of 50,000: about 1.3 M
   merchant pages, shop.app/m/<handle>). The handle is not the store's address, the merchant pages answer 429 to this crawler (asked twice,
   once alone: left alone from now on), and the archive holds none. Nothing was taken.
3. **Stores on a subdomain and stores named only by their myshopify.com address** (both from Common Crawl's HOST-level graph, 243 M host
   names, read once in this session): 7.2 M three-label hosts of ordinary domains (shop. 120k, store. 45k, account. 42k, order., us., ca.,
   tienda. …) are asked one question each by `dns_services.py hosts` (mode=hosts of dns-services.yml); 206,386 <store>.myshopify.com names
   are on file and the store reader asks a bounded number per run (300 per runner) — the store's own meta.json names the domain it calls
   its own, which is then read like any other store. Same proof as before for a row: the service seen on the store's own pages, the
   store's own statement of where it is, a role mailbox on its own domain.
4. **The store queue is ordered by ending.** Measured on the first 32,989 stores read: accepted 43 % on .ca, 38 % on .us, 26 % on .com,
   0–2 % on another country's ending (out of scope by Shopify's terms). A run reads about 24,000 stores (one queue of 2 requests a second
   per runner towards Shopify's network — unchanged): .ca / .us first, then .com / .co / .net / .org / .shop / .store, other countries last.
5. **Relationship pages read live** (`tools/live_clients.py`, built this morning, measured on 220 sites: 0.06 link records per site, never
   run at scale and not written up at the time): dispatched 19:35Z on the vendors proven in Canada and the .ca sites whose home page prints
   a Canadian postal address. Expected: about 10,000 link records.
6. **Two small tools for the planning session**, which cannot open arbitrary sites itself: `probe.yml` (a look at a few public pages from a
   runner: robots verdict, status, start of the page) and its `vet` mode (a vendor's own pages: who contracts, where, governing law, free
   plan) — the vendor table of tools/tech_relationships.py quotes those pages, one entry at a time.

**Not chosen.** Guessing store addresses from the directory's handles (asking a platform for names it did not give us); more runners to
raise the store rate (Shopify counts requests per reader: 9,024 of the first 23,437 stores refused before the single queue); older releases
of the domain graph for the sweep (each adds about 10 % new domains, mostly gone).

## 2026-11-10 20:25Z from claude — scan detector 5: a home page is read once more, and what it links to is kept
Every lane found since yesterday that needed "which sites link to X" or "which sites load X" needed the home pages read again (the scan
keeps what its detectors recognise, not the page). Detector 5 keeps, for every readable home page:
- the outside domains it loads (script / iframe / form targets) and links to, without the networks nearly every site carries; a link into
  a multi-tenant platform keeps its host, a link into a watched service (bbb.org profile, canadahelps.org form, a booking or ticketing
  page) its path start — `credit_scan/links_<stamp>.gz`, one line per site;
- the organisations linked under a heading such as "Our Sponsors", "Nos clients", "Our Members", with their labels, the page's own postal
  address beside them — `credit_scan/sections_<stamp>.gz`. Kept as read. A lead is made from them only by a rule of its own, once the
  volume and a sample have been looked at (a sponsor pays the organiser; a "partner" or a "funder" does not, and is not collected);
- which address answered when https://site/ did not (`via=http|www` on the done line): the lead readers start there.
With that on file, a vendor added to the vendor table is found by a join, and a badge that links to a register names the site's own entry,
without a new pass over 1.3 million sites.
Sites that refused the reader (robots.txt, a block: 313,649) are not read again. The pass runs at the scan's usual pace (one cycle when
the dispatcher has a slot); the 196,195 linking domains never read come first.

## 2026-11-10 20:55Z from claude — the Canadian trademarks register as a relationship source
**What it is.** The Canadian Intellectual Property Office publishes its whole trademarks register as open data (researcher datasets, CSV;
latest extract 2025-01-28). Each mark names its owner of record (legal name, full address) and, when the owner appointed one, its agent of
record: a Canadian trademark agent firm, with the firm's address. In force or pending on the extract and still inside their renewal date
today: 806,031 marks; 242,041 owners (107,583 in Canada, 134,458 abroad); 170,479 owners represented by one of 901 Canadian agent offices.
**Why it counts.** Both sides and the tie between them are named by a federal register: the owner pays its agent for acting before the
Office, and pays the Office to register and renew. Vendor in Canada = the register's own address field of the agent (rule 1). Start = the
first registration date, end = the latest renewal date (rule 3). Evidence = the dataset's own page and tables, quoted (rule 4).
**What is delivered.** The register has no websites. A lead exists only for an owner whose own site is on file and is tied to it, in this
order: the same name and the same postal code; every word of the shorter name in the longer one, the added words being everyday ones, and
the same postal code (never on a rural code, never when the longer name is a foundation, a friends' society, a union … of the shorter); or
the site itself states a legal person, with its legal form, that is word for word the name of one owner on the register — a site in
Canada, the same kind of legal person, and no other site stating that name. Natural persons who hold a mark are left out, as on every
register. Official marks of public authorities (section 9: published once, never renewed) are left out. An owner with an agent of record
is delivered as that firm's client; an owner without one, only when a registration is in force, as a registration holder of the Office.
**Measured** (local build on the frozen inputs, gates and audit passing): 2,633 sites tied; 946 rows; 14 new, 318 were registry rows, 264
inferred, 39 link-only, 309 client listings; every one of them now carries the owner's legal name and address from the register.
**What it will grow with.** The scan's detector 5 keeps each home page's own name facts for 1.3 million sites (158,724 sites state a
postal code today). The owners abroad (134,458) and the owners in Canada whose site is not on file need their site found: not built yet.
**The Office's server** sends its certificate without the intermediate that signed it. `tools/certs/` holds that intermediate (public;
fetched from the address the certificate itself names) and the download verifies the chain with it. Verification is never switched off.


## 2026-11-10 21:50Z from claude — detector 5 also keeps what a home page prints of itself: register numbers, stated affiliations; links per host
Decided before the first cycle of the pass ran (no page was read twice for it). Measured on 2,020 home pages read once each from the cloud
session (random sites of the "ok" list; one request per site):
- **Register numbers** — 2.5 % of the sites print one: an RBQ licence (1.0 %), a charity registration number (0.8 %), an ECRA/ESA licence,
  an FSRA licence, a Consumer Protection BC licence, a TICO registration, a Québec travel permit. A licence holder must print its number;
  the number ties the site to the register's own entry exactly, without any matching of names. Kept as printed (`"n": ["rbq:5760390401"]`).
  About 30,000 sites of the 1.3 million.
- **Stated affiliations** — 3.7 % of the sites: "membre de l'APCHQ", "Each Mortgage Centre office is independently owned and operated",
  "authorized distributor of Parker", "Accredited by …", and the badges under a line "Members of:". Kept as the site's own words with the
  outside address they link to, when they are a link (`"st": [[class, words, address]]`). Prose is part of it (a person's biography says
  "member of" too): this is a capture, not a lead. A lead rule comes after the data, as for the sections — it will need the payee named
  by a link or by an exact name, and the payee's own Canadian address.
- **Links and embedded services are kept per host**, not per registrable domain (`copperwell.janeapp.com`, `careers.example.org`): a
  host of its own is where a customer's account lives, on small platforms as on the 150-host ones the first version singled out. A watched
  service keeps the start of the path as before. Median line: 100 bytes a site.
Cost: 7 ms a page. No lead is made from any of this here.

## 2026-11-10 23:00Z from claude — the DNS engine lost half of its answers; questions now travel inside long-lived TLS connections
**How it was seen.** The sweep's own log: 600,235 of 1,100,000 names "without an answer" in one shard-run (55 %; 61 % the run before).
1,500 two-label .com names of the same web graph asked of a public resolver from outside: 81 % have an address, 14 % do not exist, 1 % fail.
**What it had cost** (measured on the records on file): 1,796,196 of 4,129,026 lookup records say "no answer" (43 %); a public resolver
answers 88 % of a sample of 500 of them. 677,485 are store candidates — and 97 % of the candidates that did answer are on Shopify's
addresses. Of the answered records without an address, 87 % have one; of those without an SPF record, 31 % have one. The tool wrote a
"no answer" as a fact about the domain ("its name servers are dead") and never asked again.
**Four measurements on runners** (tools/dns_diag.py, dns-diag.yml; 12,000-30,000 names a phase from one place of the sweep's list):
| How the questions leave the runner | Answered |
|---|---|
| the runner's own recursive resolver, 250 names a second, as the sweep ran (run 1) | 42 % |
| the same, no rate limit towards a zone / no query-name minimisation / 12 s for an answer (run 1) | 51 % / 64 % / 75 % |
| the same resolver given 200,000 open files (run 2) | 8 % |
| public resolvers, a new socket per question, 100 a second (run 1) / 250 a second (run 2) | 97 % / 13 % |
| public resolvers over HTTPS (HTTP/2, a few connections), 600 asked, 399 a second done (run 4) | 98 % |
| the runner's resolver forwarding over TLS to the public resolvers, 300 asked, 254 a second done (run 4) | 98 % |
| the same, 500 asked / 900 asked (run 5: 434 and 750 a second done) | 96 % / 97-98 % |
Every way that makes a new packet flow per question loses most of them above 50-90 a second; more sockets make it worse; a few long-lived
connections carry everything. The limit is on the runner's side of the network. (Run 3, one UDP socket per worker, did not finish in its
40 minutes: counted as not working.)
**Decided.**
1. dns-services.yml starts the runner's resolver as a forwarder over TLS (port 853, certificates checked) to Cloudflare, Google and
   Quad9, at about 600 questions a second per runner (run 5: 97-98 % answered at 750). Nothing else in the tool had to change for it.
2. Both sweeps begin their lists again (`SWEEP_REV` 2). The stores and name-server hits found so far stay; the places do not.
3. A "no answer" is no longer a fact by itself: a sweep batch with more than 12 % unanswered is asked once more after 30 seconds, and
   at more than 24 % the run stops and the list keeps its place (a run that got nothing does not start the next one); a lookup run
   writes its unanswered names only when they are at most 12 % of the run.
4. Every lookup record written before today is asked again — "no answer" first, store candidates before the rest, then the answered
   ones (their later questions were dropped too) — and the new record replaces the old. About 12.5 M questions: one run of six runners.
5. One concurrency group per mode: the sweep's own next run used to push a waiting lookup out of the shared group.
**The public resolvers' side.** Six runners at 600 questions a second are 3,600 a second in all, shared between three operators, for the
hours a run lasts; each runner has its own address and stays under the per-address limit the one operator that publishes one states
(Google Public DNS: 1,500 a second). If one of them starts refusing,
the health check stops the run in place.
**What it should give.** About 580,000 stores from the records on file; the sweep at two to three times its former yield; the DNS leads
of the ~1 M domains that were never really asked.

## 2026-11-10 23:10Z from claude — trademark owners abroad: a foreign company that pays a Canadian agent of record
The register holds 134,458 owners outside Canada; 109,538 of them appointed a Canadian agent of record (99,364 are organisations; United
States 50,172, China 26,540, France 6,502, United Kingdom 6,439, Germany 6,011 …). The relationship is the same as for an owner in Canada
and is named by the same federal register: the owner, its address, the Canadian firm that acts for it, the dates of its registrations.
The finder (`tm_register.py sites --abroad`, tm-sites.yml `abroad=true`) looks for the owner's own site in the three countries whose
addresses the readers recognise (United States, United Kingdom, Australia: about 47,000 organisations with a postal code in the
register's address line). A site is kept only when its own pages tie it to the owner, with the owner's country in the place of Canada:
the same name and the register's ZIP code / postcode printed in an address on the site; or the owner's legal person stated with its legal
form, or the owner's name as both domain name and site name, on a site that prints an address of the owner's state — one owner of that
name on the whole register in both cases. Measured on 117 owners: 8 tied, all eight the right company; 25 sites agreed on the name and
printed no address (not tied).
Not done: the owners in countries whose addresses are not read (China, France, Germany, Japan …).

## 2026-11-10 23:20Z from claude — an organisation's own address that is an alias of its account on a vetted platform
The lookups already keep the alias of `www.<domain>` (CNAME record); 229 organisations on file point their site at an account on a
vendor of the vendor table (Jobber's site builder 88, Unbounce 67, Lightspeed 49, Thinkific 21, D2L 2, Docebo 2), and none of them was a
candidate: the vendor lanes only looked at links on pages and at the platforms' own customer addresses.
- The host sweep (7 M three-label hosts, restarted today) keeps a host whose answer names an account on one of those platforms
  (`learn.example.org` → `example.docebosaas.com`; tools/tech_relationships.py `ALIAS_DOMAINS`) — no extra question, the alias is in the
  answer it already receives.
- tools/lead_crawl.py (candidates mode) makes a candidate of the organisation's own domain for that vendor: the organisation's own DNS
  names the vendor's platform, which is stronger than a link on a page. The site is then read like every candidate (role mailbox, an
  address in the countries the vendor's Canadian company contracts with, the organisation's name). Evidence address: the public DNS
  answer. Checked live on 13 such organisations: 1 accepted (Le Suroît, www.lesuroit.qc.ca → 609230.shoplightspeed.com), 10 print no
  role mailbox, 1 prints no address, 1 refused the reader.
- **Thinkific** enters the vendor table for this proof only. Its own pages: "Your contract and Account is with Thinkific Labs Inc. (if you
  register from within Canada and the rest of the world), or with its subsidiary, Thinkific.com Inc. (if you register from within the
  United States)"; "As part of any of our paid plans, you can set up a custom domain". So: a school on its thinkific.com address or a
  link to one proves nothing (old free plan) and is not counted; an organisation whose own address is an alias of its school is a paying
  customer, and is kept when it is outside the United States.

## 2026-11-11 00:55Z from claude — the bill-to legal name: what a site prints with its legal form; registers first; the CRA list by number
**Where the table stood** (build 22:38Z): 159,482 of 233,316 rows carry no legal name (R 75 %, T 74 %, D 62 %, I 62 %); 30,768 are known by
their domain only. The site reader had read 141,000 of the sites. Measured on 317 of them that had given no legal name: reading more
pages gives 3 % (two thirds of these sites link no privacy or terms page at all; the fifth-link limit lost 11 sites). What was missing
is recognition: the name is on the pages already read, outside the three places the reader looked (copyright line, "operated by"
sentence, structured data).
1. **A name printed with a company form that the site's own domain name spells** (tools/org_extras.py v3): "Credit Lift Inc." on
   creditlift.ca, "Autoénergie Canada inc." on autoenergie.com (the name begins with the domain; six letters at least), "Case Grypma
   Mechanical Ltd." on cgmechanical.ca (first words by their initials), "Global Institute of Forensic Research Inc." on gifrinc.com
   (initials). Anywhere on the home page and the legal pages. A company form only (Inc., Ltd., Ltée, Corp., LLP, S.E.N.C., LLC, GmbH
   …): "Society", "Association" and the like are left to the older rules. Never on a host many organisations share, never a platform's
   or a payment service's name. An opening word the name is printed with every time is kept ("Services Mobile Mediq inc.").
   Measured: 34 of 317 sites without a legal name; on 324 sites that had one, the rule agreed with it 76 times; of the 12 cases it
   differed, it was right 11 times ("Liberty Security Systems Inc." where the record held "Canadian Security Association", "Spurrell
   Professional Corporation" where it held "Secure Sockets Layer") and cut one name short ("End Plastic Waste Inc." for the Alliance to
   End Plastic Waste, Inc. — the words a name is printed with every time, in two different surroundings, are kept since); on 1,943
   further sites: 216 (11 %).
2. **The legal person a page puts behind the site's own name**: "Majid Enterprises Inc., operating as Lawn Lovers", "1234567 Ontario Inc.
   ("Acme", "we")", "Solaris (1457570 Alberta Ltd.)", "Legal Entity : Sleepera Mattress Wholesale Ltd." — the trade name must be the
   site's own. And **the operator a page names** ("exploité par Société Groupe Panican inc.", "édité par", "published by"): the ranker
   reads the sentence again in the quote. Neither is taken when the name is printed on three sites and more, or is a web agency's
   ("This website is operated by Dr. Marketing Inc." on a dental practice's terms page), unless it is the organisation's own name.
3. **Which name a row prints** (contrib/claude/rank_buyers/rank.py), in this order: a public register that named the row (trademarks,
   RBQ) › a business registry's record ("as registered": it replaces a name read off a page; it is not taken when the site states
   another legal person) › the CRA list of charities › a copyright line that names a legal person › the name the domain spells › the
   legal person behind the site's name › the operator › structured data and stated names › a Wikidata label › **the organisation's own
   name when it carries a company form** ("Kobes Welding Ltd.": 6,228 rows had such a name and an empty cell; the cell says where the
   name comes from and that no register was checked). The registry tools look up the names of 1 and 2 (tools/registry_names.py).
4. **The CRA list by registration number**: 1,167 rows carried a charity number printed on their own site (or from a federal grants
   record) that the list holds, and none of the list's facts: the match was by name and web address only. The number says more than
   either: "Ronald McDonald House Toronto" is TORONTO CHILDREN'S CARE INC., "Charlotte Street Arts Centre" is FREDERICTON ARTS AND
   LEARNING INCORPORATED. tools/charity_buyers.py writes the list in a compact form (83,761 accounts); rank.py joins on the number. A
   holder that is a foundation or a trust under another name than the organisation's is reported and not taken as the legal name (it
   may be the fundraising body).
5. **The name match against the CRA list was a file made on the owner's Mac on 2026-11-08** for a table of 65,000 rows; no workflow ran
   it. It runs daily now (claude-engines.yml, bulk_registry). Three faults found in it on the way and corrected: the first charity
   found under a name stood for every charity of that name ("Calvary Baptist Church" of Drayton Valley for the one in Chemainus: the
   city of the row's address decides now, or nothing does); a name alone matched organisations outside Canada ("City of Richmond",
   California; "Victoria University", Melbourne) — the row must be in Canada by its record, its .ca address or a Canadian postal
   code; a name of the kind many congregations carry needs the city to agree. 9,749 buyers matched on today's table (7,454 before).
6. **One pass over the 173,000 sites already read** (claude-engines.yml `refresh=true`, 8 runners; it chains itself while a runner is
   cut by its time box). Every scheduled run then re-reads, after the new sites, what an older reader read.
**Expected**, from the samples: 11-13 % of the ~100,000 buyer sites without a legal name get one from rule 1 or 2 (≈ 12,000 rows), the
older rules find one on 9 % more of them now that the legal pages are chosen among all links; 6,000 from the name itself; 1,100 from
the CRA number. On a sample build (55,000 rows of an older state, 1,943 sites re-read): legal name filled T 35 → 38 %, R 35 → 38 %,
D 30 → 34 %, B 64 → 69 % — with 1 site in 40 re-read.
**Not done.** Names whose form sits in the middle ("Die Autobahn GmbH des Bundes"); a dealer's or franchisee's site that carries the
maker's notice is guarded only by the three-sites rule and the name tie; Ontario, British Columbia and Alberta companies have no open
register to confirm a printed name against (federal and Québec companies do).

## 2026-11-11 01:45Z from claude — a spelled name must be a whole name (reader v4); the federal grants disclosure, daily and with a place check
**Reader v4.** A second run of the reader on 1,950 other sites without a legal name gave 239 names, and reading them one by one showed
17 wrong or cut short (7 %), from two causes the first samples had not shown: (a) the rule that kept the opening words of a name took
menu and heading words for them ("Data Protection Director Mirego inc.", "Carrière Total Fabrication Inc.", "Failing Properties Trinity
Development Group Inc."); (b) the words that spell the domain can be the tail of a longer name — another body's ("Crumpler Plastic Pipe
Inc." in the member list of plasticpipe.org) or the organisation's own, cut ("Pat Noble Lumber & Building Supplies Ltd.", "JPF Télébloc
Inc", "Les Disques Passeport Inc."). The rule now: the name is kept when at least one printing on the page has nothing of a name before
it (a small word, a number, a sign, a menu / button / sentence word, a title, the site's own short name), or when its printings have
different words before them; when every printing follows the same usual opening words of company names ("Services", "Construction",
"Les Entreprises" — a closed list) the name is kept with them; when every printing follows other capitalised words it is not kept. On
the three sets: 34 of 317 (unchanged), 89 of 324 (two fewer, both cut names), and of the 239 names 209 stand by their stored quote
alone (the 17 faulty ones are among those that do not).
Two runners of the refresh pass had started (01:20Z, 01:23Z) on the reader as it was before that rule. So the reader is **v4**; records
marked v3 keep what they hold, **the ranker prints a spelled name only from a v4 record**, and every scheduled run re-reads v3 records
after the sites never read. The lesson is the usual one: the first two samples (641 sites) said 100 % and the third (1,950) said 93 %.
**Federal grants and contributions** (tools/gc_recipients.py). Like the charity match, a file made on the owner's Mac on 2026-11-08
(3,668 organisations) that no workflow ran, matched by name with the province checked "when both are known". It runs daily now
(claude-engines.yml, bulk_registry) and:
- matches every organisation, whatever number its row carries (a run that skipped the rows it had itself numbered would drop them from
  its own file the next day);
- compares places: the recipient's postal code area or city against the organisation's address — 809 buyers of the same name are in
  another place and are not taken ("Holy Trinity Armenian Church", Pennsylvania, had the record of the church in Scarborough); the
  same legal name in another city of the same province is taken (an organisation with several offices: 666 buyers), unless the name
  is one that many congregations and clubs carry;
- takes a recipient's operating name with the postal code area when the recipient is a business (a trade name is shared by a chain's
  franchisees: "Paramount Fine Foods" is SKIES ENTERPRISE INC. for one restaurant), with the city when it is a public body, a First
  Nation, a school or a non-profit — 1,350 buyers get the legal person behind the name they trade under ("Biograde" is 8421005 Canada
  Inc., "Lux Voyages" is 9455-2304 Québec inc.); 524 are left because nothing settles them;
- leaves out recipients named by natural persons ("Janis Smith, Mark James Harris" for a farm: 3,083 agreements) and numbers that are
  not a program account of a Business Number ("900086828XX9999").
9,285 organisations matched on today's table (8,183 buyers, 1,102 vendors). In rank.py the recipient's legal name goes with its number
also on a row that had the number from another source. On the sample build the strict first version had lost 568 buyer numbers the
old file gave — some rightly (one number on three school service centres, a US tax number on a US university), some not (a provincial
agency whose row carries another office's city): hence the two relaxations above.

## 2026-11-11 02:45Z — whose address is it? A vendor's Canadian address must be printed on that vendor's own site (row audit of the leads on file)
Found while reading the vendors of the DNS and credit leads before the next merge (which adds about 109,000 DNS leads): **the address that
proves "vendor located in Canada" was taken from any host under the vendor's registrable domain.** On file because of it:
- "Just Pure Health", Sherbrooke — a customer of Odoo on acie1.odoo.com — standing for **odoo.com** (Odoo is Belgian): 358 leads;
- the Canadian Hockey League's office in Etobicoke standing for the Everett Silvertips, the Spokane Chiefs and the Tri-City Americans
  (Washington State), whose sponsor pages sit under chl.ca/whl-…/: 214 leads of sponsors of American teams delivered as paying a
  Canada-located vendor;
- a realtor's Vancouver address on a sub-site of avenuehq.com standing for AvenueHQ, whose own page says "Curious Three, Inc. (dba
  AvenueHQ) … Bend, OR": 753 leads; American associations on sub-sites of silkstart.com with the platform's Vancouver address; a client's
  site staged on a web agency's test host with the agency's address; expired domains parked at their registrar with the registrar's address;
- Cloudflare (pages.dev, 61 leads), Zoho (36), Mimecast (3): the Canadian address their pages print is one office — for Cloudflare a
  privacy representative — among offices in three other countries.
**Rules now (tools/cc_clients.py own_host / proof_fits / path_tenants; tools/credit_scan.py proof_page_ok / offices_abroad):**
1. The address must be printed on the vendor's own site: the host of the page that names its clients, or a site of the same holder. A
   sub-site is the holder's own when it is named after a function (business., members., events., shop., fr. …) or after the domain
   itself (infostiq.stiq.com); any other sub-site may be another body's — a platform's customer, a league's team, a university's unit, an
   agency's client. A page on such a sub-site is proven only by an address on that same sub-site, or, when the domain is small (fewer
   than three named sub-sites with vendor pages, fewer than 150 host names in the web graph, no test-host name), by the holder's.
2. Three or more unrelated site names, each under its own first path segment of one host, are several bodies on one site (chl.ca): each
   needs the address on its own pages. Language versions (/fr/, /zh/) are the same body.
3. For a provider or agency named by a credit line or a DNS record the vendor is the domain's holder: only its own hosts count. An
   address reached through a redirect to a registrar's or host's site (200+ client domains) is a parking page, unless the vendor's
   domain is itself a technical domain of that provider (easymail.ca → easydns.com).
4. A vendor that prints addresses in two or more other countries and has no .ca domain is a multinational: its Canadian office is not
   shown to be the company a customer deals with — kept out unless its agreement has been read (the vetted vendor table). With one
   other country the rule of 2026-11-10 stays (its Canadian address counts for a buyer shown to be in Canada), and "other country" now
   also means an office the address quote itself shows ("Pakistan … BRANCH OFFICE CANADA", "France 50 rue Breteuil 13006 Marseille
   +33…"): until now only American, British and Australian postal addresses were recognised, so a French or Indian firm with a Canadian
   branch was taken as Canadian for buyers anywhere.
**Measured on the leads on file (both merges run in a copy):** row factory 1,649 of 118,232 leads withdrawn (address on another body's
sub-site 709, on a sibling sub-site 575, page on a sub-site of a domain with several bodies 245, address on another domain not shown
to be the vendor's 118, path tenants 2) and 1,270 waiting links not promoted; credit / DNS / member 2,917 of 188,874 withdrawn.
Rightly lost with them, until their own site is read: associations whose only address on file was on a sub-site (caut.ca 82,
citizenlab.ca 58) — the address pass and the live vendor check now read the holder's own hosts only and take these domains again.
Not solved: a sub-site named after a function on a platform's domain would pass (none seen); the units of a university on their own
sub-sites lose the university's address as proof (about 500 leads) — the same legal person, but nothing on file says so.

## 2026-11-11 03:44Z — the vendor side of a row: its website, its legal name; page furniture in legal-name cells; the audit's check 20
Read in the published build of 01:51Z (242,292 rows) while checking the legal-name pass:
- **17,691 rows carried a third party's page as the vendor's website** — every Shopify row (16,993) "https://finance.yahoo.com/quote/SHOP/profile/",
  TMX Group another quote page, 30 vendors a page of leadiq.com, others a directory, a tender portal, an obituary. The search check of
  2026-11-08 (tools/vendor_sites_check.py, Mac era) had "confirmed" any page that prints the vendor's name. Now: a vetted software vendor's
  website is the site of its own terms page (tools/tech_relationships.py hq_url); a site proposed by search is taken only when its host
  carries the vendor's name (a distinctive word, the host inside the name, the name's initials: ey.com, mhs.com) and is not a directory,
  a quote page, an app store or a register. On the sample build: 2,768 rows get the vendor's own site, 299 lose a wrong one.
- **63,216 named-vendor rows had no vendor legal name** (tier T 48 %, D 66 %); one host, whc.ca, 7,333 rows — and 48,596 leads at the DNS
  merge of 03:11Z. The site reader had read the big providers before its v4 and does not reach terms two links below the home page.
  (1) The reader's v4 names (spelled by the domain, the legal person behind the site's name, the stated operator) are now taken for the
  vendor's site as for the buyer's. (2) data/incoming/claude/claude_vendor_names_read.csv: the vendor's own terms read by hand, URL and
  quote kept — WHC Online Solutions Inc ("Web Hosting Canada and https://whc.ca … are operated by WHC Online Solutions Inc"), Tucows.com
  Co. for Hover ("This is an Agreement between You and Tucows.com Co."), World Host Group Ca Corp for Doteasy. A hand table only for
  vendors with thousands of rows; the reader's next version gets the two patterns (the party named by the site's own agreement; terms
  linked from a legal hub page) and replaces it. (3) A vendor name that itself carries the company form is the legal name as the
  source gives it ("Octopusapp Inc. dba Jobber" → Octopusapp Inc.; "Teledyne Geospatial, a business unit of Teledyne Digital
  Imaging, Inc." → the latter). On the sample build 1,697 of 55,127 rows get a vendor legal name from (2) and (3).
- **455 of 82,018 buyer legal-name cells held page furniture** ("Lambton College Your Cart Check Out Continue Shopping", "Town of
  Kapuskasing Freedom of Information", "Perfected Coffee and protected by intellectual property laws", "· Temagami First Nation ·").
  A last pass (rank.py tidy_page_name) removes it from names read off a page — never from a register's name — and takes the legal
  person a sentence names behind the name: "DIV7 is a Division of Naro Building Systems Inc", "HR Property Maintenance · Operated by
  Haryana Enterprises Ltd". A trademark notice names the mark's owner, who may be a parent or Apple: taken only when it carries the
  organisation's own name. A name that begins with a small letter by design ("easyDNS Technologies Inc", "eGrr Services Inc.") is no
  longer refused as a fragment cut at the front; the reader takes such a first word (it had read "Technologies Inc."), and the ranker
  refuses a name made of generic words only.
- **The audit's check 20 measured the wrong thing**: it searched the whole cell, so "licence" in "(the Régie du bâtiment du Québec's
  list of active licences …)" flagged every register name — 5,266 cells flagged, of which 241 for the name itself, most of them names
  that begin with a small letter by design — while the furniture above passed. It now reads the name only (the source is the bracket
  that ends the cell) and looks for furniture: 372 cells on the same build, all of them faults.

## 2026-11-11 04:13Z — five more services vetted from the scan's own counts; candidates from the links on file; the inferred vendors' names
**Found, not guessed.** The scan's link detector (first cycle, 445,303 home pages) counts the sites that link their own account at a
service. The services with the most such sites whose own pages could be read were read today (terms, pricing, contact — each quote is in
tools/tech_relationships.py): **Owl Practice** (Owl Practice Inc., Toronto; subscription; 353 sites), **GOrendezvous** (Montréal; 59 $ and
69 $ a month; 472), **Rezgo** (Sentias Software Corp. dba Rezgo, British Columbia; no monthly fee, a fee on every booking; 367),
**WebRezPro** (World Web Technologies Inc., Calgary; property-management subscription; 200), **Juvonno** (Global Office Software Inc.,
Winnipeg; from 55 $ a month; 137). Read and not taken, each for its reason: RAMP InterActive, Clio and Spordle refuse the reader;
SkipTheDishes, CARFAX Canada, Moneris and Libro keep it out by robots.txt; Noterro's and Medeo's terms sit behind scripts; Keela's pages
print no address; Ocean's referrals are free to send and the price of its patient forms was not read; CanadaHelps keeps its fee from
the gift before passing it on (the charity is never billed). Scope by country in tools/cc_tenants.py SCOPE.
**Candidates from the links on file.** The links the scan keeps per home page name the account at a vetted service whether or not the
vendor was vetted when the page was read: the credit-scan merge now makes candidates from them (run in a copy: 3,950 new candidates from
one cycle's links — Jane 1,599, Checkfront 540, GOrendezvous 277, Owl Practice 273, Jobber 227, BiblioCommons 221, Rezgo 137, KEV 127,
Juvonno 101, WebRezPro 83 …). The candidate reader does the rest as for every candidate: role mailbox, address in the vendor's scope,
and the account must be the site's own (a practitioner's page that links the clinic's booking page is not the vendor's customer).
**The inferred vendors' names** (tier I, 18,053 rows, vendor legal name 0 %). An inferred vendor is that organisation — the inference is
about the relationship: its register entry is looked up under its name (Hydro-Québec: REQ, NEQ 8811141181, registered office), and
three names were read on a page today, URL and quote kept: Canada Post Corporation ("There is hereby established a corporation to be
called the Canada Post Corporation", Canada Post Corporation Act, s. 4), The Manitoba Hydro-Electric Board ("continued by this Act and
otherwise referred to as Manitoba Hydro"), Municipal Property Assessment Corporation (its own About page). BC Hydro, NB Power, SaskPower
and Qulliq stay without one: their statutes' sites keep the reader out or were not found; nothing is written from memory.

## 2026-11-11 05:35Z — site names from the Certificate Transparency logs (a new source of names for three lanes)
**Why.** The lanes that grow the table are limited by the NAMES they can ask: the registry class reads `.ca` sites, the store sweep asks
which domains sit on Shopify's storefront network, the DNS lane asks whose zone a Canadian provider serves. The names came from Common
Crawl's web graph — domains somebody links to: 63 M on the endings shops use, 1.05 M of the ~3.4 M registered `.ca` names — plus one
public list. A site nobody links to is in neither, and most small shops are such sites. Every HTTPS site is in the Certificate
Transparency logs: browsers only trust a certificate that was published there. Measured today on 1.9 M certificates of the newest tiles:
6,233 distinct `.ca` names, **2,833 of them (45 %) on no list we hold**; 385,000 distinct names on the store sweep's endings.
**What is read.** Only the *names tiles* of the static logs that publish them (Let's Encrypt Sycamore and Willow, Geomys Tuscolo and
Trastevere, IPng Gouda): one gzip file of JSON lines per 256 certificates, 6.5 KB, made by the logs' author for readers that want the
names and nothing else (ct-policy list, "The names tiles Static CT API extension"). Full tiles (170–440 KB) are not read. Which logs a
certificate is in was measured on final certificates found in four logs: Let's Encrypt, Google Trust Services, ZeroSSL and Sectigo give
each certificate one SCT of an RFC 6962 log and one of a static log chosen among Sycamore, Willow, Tuscolo, Halloumi and Gouda — a site
that renews twice is in one of the four read here with about 96 %. **Not seen:** certificates of GoDaddy, DigiCert, Amazon and Microsoft
(RFC 6962 logs only), and whatever sits only in IPng Halloumi or Google's static logs (no names tiles).
**Rule 9 (at most 2 requests a second per host) and these hosts.** The rule protects the web servers of the organisations we read. A
certificate log is a public archive whose files are immutable, served through a CDN and meant to be mirrored whole by monitors — the same
kind of host as Common Crawl's bucket and the public resolvers, which the engines already read at the rate their operators publish them
for. It still gets a fixed budget, small against what such a host serves: **Let's Encrypt 90 requests a second per log service, Geomys
30, IPng 20 — for all runners of a run together** (about 0.6 MB, 0.2 MB and 0.13 MB a second), an identified user agent that says what
is read, half the rate for the rest of the run after any 429 / 503, and a direction that stops where a tile cannot be had. Newest tiles
first; of the shard whose certificates are about to expire only the newest 40 %. About 21 M tiles: one to two days.
**What is kept.** Names, cut to the registrable domain. (1) `.ca` names no list has → `credit_scan/ctca_<stamp>.gz`, read by the
home-page scan and the DNS lookups like every other `.ca` name: such a site is delivered only when its own pages print a role mailbox,
as before. (2) Names on the store sweep's endings → lists published as release assets, each name once (a Bloom filter, started with the
web graph's names so the two sweeps do not ask a domain twice); `dns-services` mode `ctsweep` asks them the sweep's two questions.
Names on 27 other endings shops use are listed apart and not asked yet. (3) The subject of a certificate whose organisation a
certificate authority validated, country CA (O=, L=, ST=) → `ct_names/ov_ca_<stamp>.jsonl.gz`. **Not used yet:** a certificate's subject
is its subscriber, which can be a host or a CDN that covers its customers' names; a rule of its own will take it as a legal name only
when it carries the organisation's own name (the rule already applied to trademark notices).
**What a name is not.** A name in a log is not a relationship and not a fact about any organisation: it is a place to look. Nothing
is delivered from it alone.

## 2026-11-11 06:02Z — why two thirds of the lead sites give no mailbox, measured; what the reader does about the part that is ours to fix
**Measured** (260 sites that had given "nothing_found" — 130 leads, 130 `.ca` registry candidates — read again with every address seen
and every verdict kept): a third print no address at all (contact form only, or nothing); 15–20 % print only a webmail address (not an
organisational mailbox: owner 2026-11-04, not revisited); 12 % only people's addresses; 5–6 % hide the address behind Cloudflare's
script (left undecoded, decision of 2026-11-10). What was ours:
- **A second name of the organisation** (1 `.ca` candidate in 7): the home page asked for at `osfs.ca` answers at `flyos.ca`, `feuer.ca`
  at `valenciarisk.com` — the same organisation's site under its other domain. The mailbox printed there is of that domain, and the
  reader judged it against the name on file and dropped it. The reader now follows a name to the site its home page lives on **when the
  home page answers at the HOME page of the other domain** (never a page inside another site — an agent's profile on a brokerage's site;
  never a platform, a network, a marketplace, a parking or for-sale service, a registrar's or host's own domain, a government's shared
  site, a site with 150+ host names, a betting site fed by lapsed names). The row is then about the site that answers (website, name,
  mailbox, its page and quote); the relationship stays the one of the name on file and says so: "registration contract in force for
  the organisation's .ca domain name osfs.ca — a second name of the organisation: its home page answers at the organisation's site
  flyos.ca, redirect followed <day>". One row per organisation: such a lead is keyed by the site that answers; a `.ca` name that answers
  at another `.ca` site gives nothing new (that site has its own registry lead); a site that more than 30 names answer at is a hub and
  gives nobody a second name. Same-telephone sister sites without a redirect (1 in 20) are not taken: no proof without a second read.
- **A bare name that does not answer** (1 lead in 9 never answered at the address on file): `fetch()` turned to `www.` only when the
  bare name had no DNS record. The `www.` twin is now asked once; the pages that follow are asked of the address that answered (scheme
  and host of the home page's final URL), and leads start where the home-page scan found the site (as registry candidates already did).
  A site with no answer at all ends as `unreachable` after one or two requests instead of eight, and is no longer counted as "nothing found".
- **Role words that were not on the list** (1 site in 30): `gestion@`, `leasing@`, `membership@`, `admissions@`, `dispatch@`,
  `information@`, `info<city>@` … — the desk a small organisation answers from. Words only; a first name is never a role, and an address
  named after the organisation (`ace@aceplumbing.ca`) is NOT taken: no list of given names is complete enough to tell it from a person's.
  The ranker reads the reader's own list (one list, one place): 21 mailboxes the referee had already confirmed and the ranker refused
  come back on a 1-in-2 sample.
**What it is worth** (a second sample of 260, read with the new reader): 2.3 % of the leads and 6.9 % of the registry candidates that
had given nothing now give a confirmed-quality mailbox — about 15,000 rows from sites already read, and the same share more of every
site read from now on. Sites that gave nothing before are read once more (mark `r3`), after every site never read.

## 2026-11-11 07:15Z — four more services vetted (embedded ones this time); what was read and left out; certificate subjects as legal names
**Vetted from the scan's counts of what home pages LOAD** (445,303 home pages; vetting sheets of probe run 42972522675, each quote in
tools/tech_relationships.py): **Commerce7** (cdn.commerce7.com on 1,569 sites — its terms name two companies: the Canadian one, FS
Operations Canada Ltd., "if Client is located outside the United States"; mailing address Toronto; kept for wineries in Canada, the
United Kingdom and Australia, never the United States), **myRealPage** (MRP Ventures Inc., Winnipeg; an order form and a term; 1,804
sites), **Jumptools** (Jumptools Inc., Toronto; 324), **SoCast** (SoCast Inc., North York; licence fees; radio stations; 139). A vendor
vetted after a page was read gets its candidates from the embedded hosts on file, as the linked accounts already did (no new read).
**Read and not taken, each for its reason:** Showpass (Up In Code Inc., Calgary) — a fee on every ticket, which its pricing lets the
organiser pass to the ticket buyer: the same case as CanadaHelps (decision 03:44Z g), kept aside; GovStack — its site prints addresses
in three countries and the page that names the contracting company was not found; SharpSchool — now a page of PowerSchool (United
States); SportsPlus — "owned and operated by Thapos, a California corporation"; Yapla — "100 % gratuit"; My Music Staff (Port 443 Inc.,
Burlington) — its terms speak of free accounts and a free plan: a vendor with a free plan stays out; StackAdapt (Toronto) — the pixel on
an advertiser's page does not say whether the advertiser or its agency is the client; Renoworks (Calgary) — the visualisers that sites
link are its manufacturers' (the linking contractor is not the client); Rafflebox (Halifax), MyEvent (Montréal), Centiva, HockeyTech —
no terms or price page read yet; cchifirm.ca, civicweb.net, tuxedobillet.com — the bare name does not answer (the www. name is to be read).
**Certificate subjects as legal names** (the validated subjects the certificate reader keeps, decision 05:35Z). Used for a legal-name
cell still empty after every other source, when the row's site is one of the certificate's domains and the subject is the organisation
of that row: a row with a name of its own must share a distinctive word with the subject and must not be another body beside it (a
foundation, a student union) nor a company with its own legal form (TELUS Health (Canada) Ltd. is not TELUS Corporation); a row known
by its domain only needs a subject that fits the site's own name; never on a government's shared domain; never from a certificate
that covers more than twelve domains. Three sample builds: the first version gave SaskTel to a village whose page sits under
sasktel.net and Vidéotron ltée to a municipality — fixed before anything was built in the cloud; the third gives 6 names on a 1-in-2
sample, all the row's own (Royal Bank of Canada, The Toronto-Dominion Bank, Insurance Corporation of British Columbia, eHealth
Saskatchewan, The University of British Columbia, L'Arche Association of Calgary). The cell names the log's tile it was read in.

## 2026-11-11 07:46Z — a refresh pass that merged nothing: what went wrong three times over, and the rules that come out of it
**What happened.** The v4 refresh of the site-facts reader (run 42958065125: 8 runners, 2 hours) ended with a crashed merge: two runners
delivered a `.gz` that stops in the middle. Nothing of the run was merged and the chain did not go on. Three separate faults, each
repaired at its root (commits 480179e, 3085e1b):
1. **The half-written state file.** The reader wrote its whole state every five minutes from whichever worker thread had just finished
   a site, always to the same temporary path. With 230,000 records and 40 threads on one interpreter a write came to last longer than
   five minutes; the next write then opened the same path, and the first one's rename published the second one's unfinished file.
   `timeout` stopped the reader in that state. Now (`tools/run_box.py`, used by `org_extras.py` and `org_contacts.py`): one write at a
   time, a path of its own each, the next no sooner than 15 minutes after the last ended; the reader stops by itself at its deadline
   (or on SIGTERM), writes once more, and leaves. The merger reads a cut `.gz` for the records it holds instead of crashing.
2. **A v3 name inside a v4 record.** Two reads of one site were joined field by field: what today's read lacks stayed from the read
   before. Right for a page that does not answer today; wrong for a rule that changed — the names v3 took by the rule v4 no longer
   accepts stayed in the record, which now said v4, and the ranker prints spelled names "only from v4 records". Measured by reading 160
   sites with a v3 name again: v4 gives the same name on 149, **none on 9** (5.6 %: "CLC inc." for Les Cheminées CLC inc., "TST inc."
   for Systèmes Énergie TST inc., "Joyce Law Corporation" for David A. Joyce Law Corporation), 2 did not answer. **Rule:** a group of
   fields a version computes as a whole says which version made it (`legal_name_spelled_v`); a successful read replaces the group, with
   nothing when it finds nothing, unless the group on file was made by a version whose rule still stands (`org_extras.GROUP_MIN`). The
   ranker prints a spelled name only when the name itself is v4's. The 34,397 names in records the faulty runs had already made were
   put to the present rule on their own quote (`org_extras.settle`): 31,396 kept (in the sample, 140 of 141 kept names are the name v4
   reads), 3,001 removed and their sites queued for a new read.
3. **Two merges of one file at once.** A state file was one release asset replaced in place. Merge B, started from the version before
   merge A's, would upload over A's, lose the push, fetch "the current asset" — its own — and publish a state without A's records. It
   had not happened yet; the dispatched refresh and the scheduled run were about to merge within minutes of each other. **Rule:** every
   version of a state file has its own asset name (`claude_org_extras.<12 hex of its SHA-256>.jsonl.gz`); the push of the manifest line
   (`coord/STATE_ASSETS.json`) decides, and the merge that loses the push starts again from the version the manifest on main names.
   The writer deletes old versions: never the one its manifest names, none younger than three hours, never the three newest.
**Recovered:** the failed merge job was run again on the eight artifacts with the repaired merger (07:44Z): 164,025 of 230,582 site
records are v4, 31,396 spelled names stand; the two cut files cost about 30,000 sites, which the next refresh run reads.
**Found on the way — the reader of facts is one busy core.** 250 ms of CPU a site (12 sites, 3.0 s), so one reader does 3.4 sites a
second whatever its number of threads; "100 sites at a time" (set at 06:30Z on the mailbox reader's 23 ms a page) bought nothing here.
A runner has four cores: **three readers a runner**, each with a third of the runner's sites, a file of its own and only the records
it made or changed (`--out`, `--delta`). Three times the sites per runner-hour, and the files to merge are small.

## 2026-11-11 09:05Z — one queue per platform for the site-facts readers; a block page is a short page; the registers lane
- **A block page is a short page** (under 30,000 characters). The site-facts readers called any home page "blocked" that held "captcha"
  in its first 5,000 characters: every Wix site (the word is in the page's settings), every page that loads reCAPTCHA early. 40 of 60
  never-read sites. The mailbox reader already had the size test; all readers now share it.
- **One queue per /24 of addresses for the site-facts readers** (`ap_crawler.NET_INTERVAL`, 1.5 s per reader, three readers a runner = two
  requests a second per runner towards one platform — the rule the store reader has had for Shopify since 2026-11-10). Measured: of 70
  sites the runners were refused by (403 / 429), 51 answer one machine; 18 sit on Wix's addresses, 12 on Shopify's. Rule 9 names the host;
  for a platform the host is the platform. The mailbox crawl and the scan keep their per-site limit: their lists are a few per cent
  platform sites and they are not refused (4.9 % blocked over 633,000 sites).
- **Failed tries are remembered** (`crawl_state/org_tried_*.gz`): a site that refuses (403, robots) is not asked again for 30 days, one that
  has nothing for 21, one that did not answer or answered 429 after 2 days, then 14. Before, every run asked every failing site again.
- **Registers of delegated authorities are a lane** (tier M, own line in every report). A registrant = a business the authority's own
  public register names as currently registered / licensed; legal persons only; the authority's address and fee sentence quoted from its
  own pages; the registrant's site is the one its entry names, kept only when its home page shows the registrant's telephone number or
  postal code; the register's e-mail is never read, never delivered. Start and end of the row = first registration and expiry date.
  Built: OMVIC (Ontario motor dealers, 7,865). Scouted and open: AMVIC, VSA, HCRA, ESA, RHRA, TICO, BAO (`coord/source_registry.csv`).
- **Before an engine that has not run for a day is dispatched, one request to its source is made from here.** The registry lookup was
  started at 07:56Z on an address that had been retired; a run cannot be stopped from here, so it asks a dead address until 13:20Z.

## 2026-11-11 12:03Z — the owner's bar: a relationship is one the vendor bills for every month or every quarter; what a row may claim
Owner, 06:24 EST: "I want to know for a fact that there's a relationship to a point where they would be getting billed for something
monthly. That's my evaluation of a relationship. Or every 3 months, they get billed for something systematically by the vendor."
- **A billing period is a published fact or it is "not published".** Two columns on every row: `recurring_billing` (1 monthly ·
  1 quarterly · 2 monthly or yearly · 3 yearly or longer · 4 per transaction · 5 not published) and `recurring_billing_basis` (the quote,
  the page, the date). No period is ever inferred from the kind of vendor.
- **Where the period comes from.** (a) The 35 vetted software vendors: their terms and price pages read with the project's reader and
  then by hand (`tools/tech_relationships.py` BILLING, 21 with a statement; the 14 that publish no price are "not published").
  (b) Every other vendor of a live service, a credit, a membership or a client listing: `tools/vendor_billing.py` opens the vendor's own
  site (home page + up to five pages its menu names as prices / plans / hosting / membership / terms) and keeps each statement of a
  period with its sentence. Measured on the first 1,495 vendors: 233 price by the month, 137 by the month and the year, 75 by the year,
  84 say they bill monthly, 12 quarterly, 917 publish nothing, 37 could not be read. 45 "bills monthly" statements read by eye: 42 right, 1 wrong ("paid ads, email, and
  monthly reporting": "paid" now counts only right before the period), 2 right but with a yearly option the reader missed (one pattern
  added). (c) `.ca` names: CIRA's General Registration Rules, s. 2.4 and 7.3 (1 to 10 years). (d) Licences and registrations: their
  published start and expiry dates. (e) Contract records: only what the record's own text says.
- **"1 monthly" needs both halves**: the vendor's own statement that it bills by the month (or every 30 days) with no longer period on
  the pages read, AND the service seen in use by the buyer (platform under its site, its DNS records, a "powered by / hosted by" line).
  A price "per month" beside a yearly plan is "2 monthly or yearly": which one the buyer took is not published.
- **A design credit is not a bill.** "Website by X" says who made the site; 48,000 of the 66,888 credit leads are of that kind. They stay
  rows (a Canadian vendor was paid) with `5 not published`; "powered by / hosted by / maintained by" credits (18,329) follow the
  vendor's price list.
- **Shopify, corrected against the source** (terms last updated October 20, 2026, read 2026-11-11): "You will be billed for your
  Subscription Fees every 30 days." Section 13 names two contracting parties for stores whose billing address is in the United States
  or Canada — "Shopify Inc., a Canadian corporation" and "Shopify Technology (USA) Inc., a Nevada corporation" — and says "Shopify Inc.
  may act as the billing agent for Shopify Technology (USA) Inc."; it does not say which party serves which store. The vendor note on
  every Shopify row now carries that wording (the old note said Shopify Inc. alone), the rows stay (Shopify Inc. is a named party and
  the billing agent), and every report gives Canadian and US stores on separate lines.
- **Which relationship represents an organisation**: among the services it is seen to use, the one whose vendor bills by the month
  claims the row, then one priced by the month, a design credit last (`lead_strength`).
- **What this does to the plan.** Lanes are ranked by rows of class 1: stores and other subscriptions seen in use, monthly-billed
  hosting, leases, retainers. `.ca` rows (yearly), members and registrants (yearly or per transaction), client listings and links keep
  being built only where they cost nothing extra, and never count towards the bar.

## 2026-11-11 13:18Z — the owner's bar, as he clarified it twice the same morning (07:15 and 07:48 EST); what was built on it
- **The gate is the fact of the relationship, not the monthly bill.** My 12:03Z reading ("yearly fees … do not count") was too narrow:
  "it is a subcategory of what I'm asking … as long as … we know for a fact it is a relationship". AGENTS.md §1 now carries the five
  rules in his words. Monthly billing is the strongest kind, not the only one.
- **Every field of an invoice, and the amount first.** Measured on the table of 12:35Z (258,757 rows with a mailbox): vendor address
  100 %, vendor legal name 82 %, buyer address 73 %, vendor tax number 61 %, buyer legal name 45 %, an amount 3 %. So the amount and the
  buyer's legal name are the weak fields. Built today: `bill_amount_indicative` (the vendor's own price list: the lowest price of the
  period, as a floor — the buyer's own plan is never published; Shopify "from US$29 a month" with its four plan prices; a body's fee),
  `bill_items_as_published`, `bill_currency_as_published`, `bill_delivery_as_published`, `bill_payment_method_as_published`,
  `bill_tax_rule_as_published`, `bill_identifier_format`, `service_stops_if_unpaid`, `relationship_fact_basis`. On a 1-in-4 sample
  build the amount goes from 3 % to 21 % of rows and the ranker's log now prints the fill of nine invoice fields, tier by tier.
- **`service_stops_if_unpaid` is what turns "seen running" into "being paid for"**: Shopify suspends a store 28 days after a failed
  payment (terms, s. 5); CIRA's rules delete a name that is not renewed (s. 7.1); 303 of the first 8,500 vendors publish the same rule.
- **Vendors are looked up in the business registry by the rows they carry and under the legal name their own site states**
  (`tools/registry_lookup.py`, cloud engine now `--kind both`): Web Hosting Canada has 10,007 rows and no business number; its site
  states "WHC Online Solutions Inc". One answer fills every row of the vendor.
- **The 100-row test set is a tool, not a hand pick** (`tools/test_sample.py`): 13 kinds of relationship, a fixed number of rows of each,
  drawn with a seed; weak kinds are in it on purpose. Reading the first draw by eye found six faults that are now fixed in the ranker
  (579 buyers named "About" from BBB profiles; "Welcome to …" names; day-month dates; CIRA's legal name under a carry-over note on
  101,433 rows; Shopify's Montréal office instead of the registered office its terms give; a firm that is its own trademark agent) and
  three that are lanes to build (`coord/source_registry.csv`: tenant directories, council award resolutions, member dues).
- **Not done, and said so:** no calculated cadence yet (rent, construction progress claims under a prompt-payment act, electricity):
  each needs its own published basis before it is written in a row, and a label that says "calculated".

## 2026-11-11 13:24Z — runners go to reading stores before finding more of them
The DNS sweeps have found 1,633,424 domains on Shopify's storefront addresses; the store reader reads 36,000 a run (6 runners × 6,000 at
2 requests a second per runner), about 290,000 a day: six days of backlog, and the certificate-name sweep adds to it faster than it is
read. A store row arrives with the billing period, the amount, the bill's fields and the vendor's legal name, address and tax number on
it. So: mailbox-crawl 6 -> 8 runners (the store reader rides on each), certificate-name sweep 3 -> 2. The limit of 2 requests a second
per runner towards Shopify stays. Stores outside Canada and the United States still end after one request.

## 2026-11-11 16:14Z — the owner's 100 test rows went out; what reading two draws before him changed in the rules
The set (`coord/pilot/TEST_SAMPLE_2026-11-11.csv`, review page with his marks saved on it) is drawn from the table published at 15:57Z
(282,207 rows). I read a draw of 100 from a local build first, then his: about one row in five had a fault in a name, an address or an
amount, none in a mailbox. Each fault became a rule, measured before it was written:
- **A legal name from a copyright line must be the organisation's own.** 37,221 buyer names came from that line; the ranker's own test
  finds about 5,000 that share no distinctive word with the organisation's name or address. Read by eye (70, then 44): about half were
  the site's maker, a picture's owner ("Peanuts Worldwide LLC"), a parent, or the page's menu ("Disclaimer Browse Home Municipal Office
  Services Dep"). Now: kept when it is plainly the organisation's (the same name, its initials, its government on a government site);
  otherwise taken last, only a short company name with its legal form, printed on the organisation's own domain, not an agency's, not on
  three sites; the cell says "on that line alone" and such a name is **not counted** among the nine invoice fields (read by eye: about
  three in four right). The same rule on the vendor side ("SofterWare, Inc" on a charity's donation page was the charity's legal name).
- **A schema.org node that only gives the site as its own address counts when it names a legal person.** "Kennetcook District Fire
  Hall" was a municipality's legal name, "Daryl" a cabinet maker's.
- **An amount is a price-list line for the service seen.** 36,201 rows took their amount from the vendor reader, 439 vendors. Not a
  price: a blog sentence ("another $2,000 a month"), a late fee, a minimum payment on a balance, a first-purchase offer ("$8.88/yr only
  for new dot-CA domains!", 1,313 rows), the top of a printed range. Not the service: a mailbox price for a zone on the vendor's name
  servers (Hover, 5,078 rows: its domain prices are drawn by a script the reader does not run, so those rows now carry no amount and
  say why), an Internet provider's television box or telephone line. `vendor_billing.lowest(rec, service)` does both.
- **The largest vendor seen in DNS gets its terms read by hand**: Web Hosting Canada, 11,551 rows — how its invoice arrives, how it is
  paid, in which currency, what happens when it is not paid, its hosting price (`tech_relationships.BILLING_BY_DOMAIN["whc.ca"]`).
- **`.ca` rows (103,559): what CIRA's Registrar Agreement says, and a calculated amount.** CIRA charges the registrar "a fee for each
  registration … and a fee for the renewal", "at the time the Transaction Request is made", taxes not included; the amounts are "set
  forth at CIRA's website", which refuses the reader (403, not asked again). The registrant's own price is not published for any one
  name. So `bill_amount_calculated` (new column, always opening with "calculated") gives the range of what Canada-located vendors print
  for a `.ca` name by the year — today 8 prices, $14.57 to $45 — and never feeds `bill_amount_indicative` nor the nine-field count; the
  log counts it on its own lines.
- **A name is not a page title.** Vendors: "Buy Domains & Email At Hover.com" -> Hover, "… » Zenutech" -> Zenutech (1,756 rows on a
  1-in-4 sample); `lead_crawl.site_name_for` fixed at the source. Buyers: a title with bars, a domain with a slash, the title of the
  vendor's story. Addresses: the page's words in front ("today. Call us Message us Contact Info Cameron, MO"), a charity number, a
  written "\n". A subject that was the word "null".
- **A story is a client listing only when it is filed as one.** "And the honorary doctorate goes to" (a university's news story of
  2010) stood as a client; United Way, alumni and sustainability stories did the same. A story whose address is not under clients,
  customers, case studies, success stories or testimonials is now a link (tier E), with the reason on the row.
- **A person is not a vendor.** 15 rows named a consultant lobbyist registered without a firm. Left out.
- **A whole build does not fit this container (killed at 5.8 GB); two parts do** (`RANK_PART=i/2`, 15 minutes a part, 5.4 GB,
  `tools/rank_merge.py`): 282,149 rows locally against 282,207 in the cloud an hour later. That is how a full table is read here
  before a cloud build when the runners are all taken.
- **The test page shows what is already known.** 19 of his 100 rows carry a note where a rule can see the fault. Nothing was removed
  from the draw. When the corrected table is published and he has not marked a row yet, a second draw replaces the first; otherwise
  the first stays and the second is a new page.

## 2026-11-11 19:24Z — "on invoice, by bank transfer": the owner's requirement, what it takes out of the table, what is built in its place

**What happened.** The QA lane read the column `ship_ready` on the owner's 100 test rows and told him most were not ready. That column was
the first goal's label (an invoicing / AP mailbox, on four tiers); it said "no" on 97 rows, 87 because the mailbox is a general one. Over
five messages (12:31 to 14:20 EST) and three sets of questions he gave the rule that replaces it — AGENTS.md §1, rules 6 to 12:
on invoice and payable by bank transfer or it is not a row; any Canadian entity may be the biller; one row per buyer, no buyer twice; the
general mailbox is fine; the invoice fields tailored to each kind of relationship; all lanes, "and more".

**What it does to the table of 15:57Z (282,207 rows), measured with the new test on every row:**
card on file 33,278 (Shopify 30,202 and other self-serve software) · through a registrar 103,829 (`.ca` names) · paid on invoice by bank
transfer or cheque 7,833 (5,461 with a mailbox, 1,343 passing the whole test) · the vendor takes both 2,743 · not published 134,524
(hosting and DNS 69,645, licences and memberships 13,467, relationship not established 51,412). The day and a half spent on stores
produced no row that meets the requirement. I had not asked how a store pays before building the lane; the terms said it on their first
page ("Shopify will charge applicable Fees to any valid payment method that you authorize").

**Decisions.**
- **Card-on-file and registrar rows are not written** ("Remove them"). `rank.py`: registry leads are dropped before the lead pass; a
  software lead whose vendor is Shopify, or whose published payment methods name cards and no bank payment, makes no row and does not
  claim its organisation's site (another relationship of that organisation can); a last check in the writing loop drops any row whose
  route is a card or a registrar. `RANK_CARD_ROWS=1` / `RANK_REGISTRY_ROWS=1` rebuild the old table for a comparison.
- **One test, one function**: `tools/relationship_rows.py: owner_test`, called by `rank.py` on every row. `ship_ready`,
  `ship_ready_missing`, `payment_route`, `payment_route_basis`, `invoice_fields_for_kind`, `invoice_fields_missing_for_kind`,
  `vendor_tax_or_registration_number`. The old label is `ap_mailbox_ready` (no column is deleted).
- **Fields by kind** (`FIELDS`): a public contract has a reference and no billing period in its record; a licence has a number, a
  yearly fee from a public tariff and no tax number on its fee notice; a membership has dues by the year and no contract number; what a
  dealer buys and what a tenant pays are not public, so no amount is asked there. The buyer's legal name is not asked (the name it trades
  under and its address are what an invoice carries); a calculated amount, labelled, counts.
- **The biller's own roster establishes the relationship; a client list does not.** A member directory, a dealer list, a tenant directory,
  a sponsor / exhibitor list is the list of who pays, kept by the body that is paid and current by construction. The owner chose those
  lanes knowing what they are. A logo wall or a case study stays "stated by the vendor" (his rule of 07:15 EST). 16,000 rows of the
  27,000 that stood as client listings are member, dealer, tenant or sponsor listings by the address of their page.
- **How each biller is paid is read, not assumed.** `tools/payee_billing.py`: the bodies that carry thousands of rows, read by hand and
  quoted — the Régie du bâtiment du Québec (a notice of assessment by mail, paid through a financial institution or by cheque), the City
  of Calgary (invoice due in 30 days, through a bank or by cheque), the City of Edmonton (cheque, Interac, EFT from $10,000, cards). The
  vendor reader, version 5, reads the same from every other body's site. A public contract is on invoice by its kind; the buyer's own
  published payment terms are quoted when it has them.
- **A body that says it sends no invoice is not on invoice.** The Ontario Motor Vehicle Industry Council: "OMVIC does not issue invoices.
  Dealers are expected to self-report and remit payment with their renewal application." Its rows fail the test and say why.
- **One row per (buyer, vendor) pair was built, measured and not kept.** 316,284 pairs stand behind the 5,391 buyers of the contract
  dataset, 220,814 of them with a mailbox on file. Asked, the owner answered "only 1 buyer so no buyer should be repeated". The pair
  table stays an analysis (`relationship_rows.py`, main).
- **Engines.** The store reader is out of `mailbox-crawl.yml`; the timers of `tenant-factory`, `dns-services` and `ct-names` are off
  (they fed card-billed lanes; they can be started by hand); the keeper starts the member, accreditation, licence and register engines
  first. The `.ca` sites keep being read: with their names, addresses and mailboxes they are the pool the register lanes are matched
  against, not rows.
- **The reader that stops** (two mailbox runs lost a runner in six): a watchdog outside Python ends a frozen reader after ten minutes
  without a finished site and prints every thread's stack; the workflow starts it again; uploads happen whatever the step's end.

**What I told the owner, and stand by.** Under these rules the registers name over a million organisations; a row also needs each one's
own site and mailbox, which registers do not give. With what is free I see 100,000 to 150,000 rows; with a search budget, 300,000 or
more; I do not yet see a million.

## 2026-11-11 21:05Z — the first hundred on the owner's rule was read and not sent; six rules; the amount of one licence

- **A test set is read before the owner sees it, and a fault becomes a rule before the draw is repeated.** The first draw from the build
  of 20:21Z (6,405 ship-ready rows) had 11 service rows whose amount was a price increase, 2 whose amount was a discount, 3 whose
  "how it is paid" was a refund or a payout clause, an access-to-information mailbox, an owner-builder's licence priced from the
  contractors' table, a person's name as a buyer, 7 sponsors passed on a club's membership page. Showing them with a note would have
  been the first hundred again. The rules: `vendor_billing._NOT_A_PRICE` (a change of price, a discount), `relationship_rows._NOT_HOW_PAID`
  (money going the other way), `BAD_LOCAL` (ati / foip), no RBQ amount for "constructeur-propriétaire", 157 given names.
- **When no build can run, the published rows are re-tested, and the page says so.** GitHub Actions failed to start runs from 20:41Z.
  `tools/retest_rows.py` puts each published row through the functions the ranker uses (payee facts into empty cells, then the owner's
  test): 7,754 pass. The hundred is drawn from those; the page reads "each row tested again at 20:57Z with the rules as they stand".
  Nothing is added to a row that the ranker would not add.
- **The amount of a licence is the city's own figure for that licence, not a "from".** Toronto publishes its open licence invoices every
  night (licence number, invoice number, amount due) and a renewal fee on the page of each kind of licence; Calgary a schedule by licence
  type with the rule for several types; Edmonton a tier for each category. `tools/payee_fees.py` reads them twice a day. A type that the
  schedule does not list under that name gets no amount; a licence of several Calgary types gets what the schedule's Note 3 gives, in
  the column for calculated amounts, with the note quoted.
- **A buyer's purchase-order rule is asked where a purchase order exists**: a public contract, a service, a dealership. A regulator's
  notice, a chamber's dues, rent, an agent's account and a sponsorship are not ordered that way (the owner: "Shopify … won't have a
  purchase order … maybe some other thing will").
- **A candidate site is accepted on what it prints.** The trademark register names the agent of record with an address and no site. A
  hand list of candidate sites for the firms behind the most owners is checked by the reader: the site must print the firm's name and a
  postal code the register gives for it (an office tower's postal code is shared by its tenants). 40 of 64 tied; a site that refuses the
  reader stays unread.
- **A member's amount is the body's lowest published dues, said to be the lowest.** A member's own dues are never published; the floor is.

## 2026-11-11 21:30Z — the owner at 16:01 EST: "1 million … think differently … populate those fields as best as you can". What a row stands on now

His message in full is in AGENTS.md §1 (rule 13). He was not asked again: "this your project take all liberty". What I decided, and why.

- **A row stands on four things, and a field that nothing published fills does not take it out.** Until 16:01 a membership row without a
  published dues schedule, or a licence row whose regulator's payment page had not been read, was "not ship ready" — 7,754 rows passed.
  He holds the target at a million and says "don't just go empty". The four things he named are the test (a Canadian biller, a bill on
  invoice, a bank payment, the mailbox); the fields of a row's kind are populated as well as they can be, and what is missing is named on
  the row (`ship_ready` = "yes (not published: amount, …)"). Complete rows sort first; the build log counts the levels apart, so the
  number never hides what it is made of.
- **How a bill of a kind is billed and paid may be said by the kind** when the biller's own sentence is not found: a regulator's fee, an
  association's dues, an agent's account, a supplier's sales to a dealer, rent, a sponsorship. The row says "by the kind of
  relationship, not in this biller's own words". The biller's sentence wins when there is one. Not for hosting or software (a card on
  file is the common way there), and not for the Canadian Intellectual Property Office (its page was read and names no notice).
- **A relationship may stand on where the organisation is.** The scarce thing was never the relationship: it is the organisation with a
  mailbox we can show. 253,630 organisations have a referee-confirmed mailbox; 7,754 had a relationship that passed. Every one of them with
  premises in Canada outside Alberta is billed for electricity by one body — an exclusive franchise, a monthly invoice, paid through a
  bank; Hydro-Québec and Manitoba Hydro refuse cards in so many words. That is his own test of a fact from the morning ("something being
  where it is means that there's a relationship … the odds of it not being a relationship [are] extremely low") for the ADDRESS. For the
  ORGANISATION it holds when the organisation has its own meter, and not when its landlord does — and that is not published. So such a
  row says exactly that, in `relationship_fact_basis` ("by where it is: … whether the organisation or its landlord holds the account is
  not published") and in `ship_ready`, and it is counted on its own line. He asked for inferred rows once before (2026-11-03: "even more
  inferred"); the letter-carrier inference of that time is dropped (Canada Post does not send every organisation an invoice): 25,785 rows.
- **Where an organisation is, is read from its own page**: the postal code in the address the site reader kept, or printed beside its
  mailbox. No province from a domain name, no city from a name. A postal area that two distributors share is left out, and so is Alberta
  (the retailer is the customer's choice). 89,387 organisations with a confirmed mailbox fall in the eight territories on file.
- **One row per buyer still**: a record or a service seen on the buyer's side comes first; the distributor is what is left for an
  organisation that has neither. (Next step, not built: a row whose own relationship fails — a client listing, a link, a service paid by
  card — gives way to the distributor of its address and keeps the other relationship as a note.)
- What did not change: no invented value, no calculated value presented as published, §2 of AGENTS.md whole. A distributor's file from
  another lane is used only after its sentences were found on their pages (`by_location.py verify`).


## 2026-11-11 22:44Z — the first build on rule 13 gave 79,860, not the 105,000 a sample promised. Three changes that follow from reading it (claude)

**The number.** Build 22:11Z (code c6cd6fe): 158,912 rows, 79,860 ship ready — by where the organisation is 38,467 · best effort 33,095 ·
every field in the biller's or the record's own words 8,298. I had told the owner "about 105,000" from a build on one lead in four. The
sample over-counted the by-location rows: an organisation's service lead and its mailbox key are sampled apart, so in a sample three
organisations in four have lost the service row that, in the full table, stands in front of the row by location. A sample build tests
the code; it is not multiplied by four again for a count that depends on which row an organisation gets.

**1. A row whose own relationship cannot meet the rule gives way to the distributor of its address.** 55,690 rows of the build are a
hosting / DNS / web-agency service whose vendor's way of being paid is not published — never ship ready, and nothing may be said "by the
kind" there (a card on file is the common way). 15,843 are a client listing or a link (the vendor's statement). The organisation behind
each still has the one biller its address has by law. Decided before the row is enriched (so every cell is the distributor's), exact for
services (the same function that judges the route at the end judges it here; measured on a sample: 0 rows of 12,945 predicted "not
published" ended otherwise). The other relationship stays on the row, in words, in `other_relationship_sources`. A service whose vendor
publishes a bank payment keeps its row: a record or a fact seen on the buyer's side that MEETS the rule still comes first.

**2. Ontario by postal code, from the regulator's own map.** A rule "postal area -> distributor" is wrong in Ontario: sixty licensed
distributors, Hydro One's lines between the towns that kept a utility; my own rule of the afternoon had K1E (97 % Hydro One) and part of
K2S as Hydro Ottawa. `tools/on_ldc_table.py` overlays three public files — the Ontario Energy Board's map of service areas (open data,
2024-09-30), the location of every postal code (GeoNames), Statistics Canada's postal areas — and gives a postal code a distributor only
when its location is inside that distributor's area and no other, 300 m from the edge (5 km for a rural code), or its whole postal area
is. 286,410 of 295,544 Ontario codes; 9,134 get none. The address and site of each distributor are the Board's own page on it (the
source's own vendor address, §2.1). 44,015 organisations with a mailbox on file are in those areas (14,993 were Toronto and Ottawa).
The same method is the way for any province where two distributors share postal areas (FortisBC, the municipal networks of Québec)
once a public map of their areas is found.

**3. The mailbox reader reads first what is nearly certain to be a row.** Its queue put the .ca sites that print a role mailbox on their
home page last (after 900,000 lead sites), because a .ca registration stopped being a row. By location they are rows: about 63,000 such
sites are unread, 85 % of those read gave a mailbox. They are read first now, and a .com / .org site whose home page prints a Canadian
postal address and a mailbox is a candidate too (39,393 never queued).

Also: the organisation's postal code from the home-page scan is an address when the reader kept none (377,262 home pages), said as such
on the row; a vendor is looked up in the register under the legal name its own site prints (3,763 rows had lost the vendor's number).

## 2026-11-12 02:14Z — the owner's evening: how full a row is, $5,000 as a priority, one row per buyer; what was counted, decided and built (claude)

**What he said (2026-11-11, EST).** 20:04 "what is this ship ready for you … what about estimated value per billing cadence and all other rows/
invoice fields … I want to make sure it's useful efficient work". 20:14 "an inference be permissible, combined with billing cadence a fair
estimate can be made … be sure to populate as much as possible per relationship … I have one credit reset left … short work sessions and your
automation hand-offs". 20:22 "what about the contracts, also the relationship billed amount per cadence should be 5000 plus … we still need to
reach 1 million". Asked two questions at 20:35 he chose a hard floor and one row per buyer and vendor; at 20:36 he settled it: "we will also
include those of lower value but mark them, mark everything, prioritise over 5000 … no buyer twice is hard rule so it should be 1 million
buyers, vendor can be repeated … that's why I was willing to lift 5000 cap, make it soft". AGENTS.md §1 rules 14 to 17.

**What was counted for him (table of 00:14Z, 136,513 rows that met the test).** With an amount and a billing period 70,503; with every main
invoice field 24,279 (nearly all Hydro-Québec's); with no amount 66,010. Where an amount stood it was the biller's lowest published charge.
With a published amount of $5,000 or more: 1,510 contract values and one fee. The contract dataset: 803,097 records, 316,131 buyer-vendor
pairs, 5,590 buyers; current and $5,000 or more: 158,427 records, 90,680 pairs — 66,678 of them behind 1,687 buyers with a mailbox.

**1. Every row is marked by its amount and the table is written in that order.** `amount_mark` (tools/relationship_rows.py): published
$5,000 or more · estimated $5,000 or more · published under $5,000 · estimated under $5,000 · no amount. `tools/priority_sort.py` (run by
`tools/rank_tail.sh`) puts the rows that meet the test first, by mark; constant memory. The test itself does not look at the amount.

**2. What an estimate is.** A calculation from published figures, labelled, in `bill_amount_calculated` — never in a published cell. For
electricity: the distributor's own rate (fixed charge + price by the kilowatt-hour) at 2,500 kWh a month, before tax. The 2,500 is the use at
which the Ontario Energy Board's small-business bill calculator opens; it is used as one yardstick for every province and the row says so.
For a contract: its published value by the year of its published term. Where nothing published supports a figure (what a dealer buys from
its supplier) no estimate is made. Sponsors (the published price of the level a sponsor is listed under) and members (the body's dues
schedule) need a reader of their own: 1,261 and 1,258 billers, too many to read by hand.

**3. Ontario's distributors from their regulator, all 53 at once** (tools/on_ldc_table.py: enrich, rates). The Distribution System Code
binds every licensed distributor: a bill every month to each small-business customer (s. 2.6.1A), at least 20 days to pay (2.6.3), how a
bill is issued (2.6.4) and how a payment is made (2.6.5). The Board's file of current rates behind its bill calculator (open data, monthly)
gives each distributor's fixed monthly charge and every rate by the kilowatt-hour: field SC is the service charge with its fixed riders
(checked on two distributors: SC − OFC is the service charge their own tariff prints). The licensed name is the legal name; the licence
number is the distributor's number in the regulator's register. A distributor read by hand keeps its own sentences.

**4. Three faults found in the published table, each a rule now.** (a) 53 rows stood on a "postal code" that was a colour code or a form's
placeholder (E6E 6E6, A1B 2C3); the scan held 2,341 such codes. A code whose letters are all among A, B, C, E is taken only when printed in
capitals with a space or hyphen and found in the list of real codes; three equal pairs and the usual examples never (tools/by_location.py:
usable). (b) An urban postal code is one building or one side of a block: when ten or more organisations print the same one the row says
so; from fifty it does not meet the test (133 rows on M5C 1C4, 67 on First Canadian Place) — the account there is the landlord's. Counted
by registrable domain over the scan and the build; a rural code is a whole town and is not counted. (c) A row that gave way to the
distributor still carried the other vendor's bill cells (a web host's tax sentence on 2,600 electricity rows): emptied.

**5. Buyers under contract are the rows with large published amounts, and 1,401 of them had a verified mailbox that the ranker did not
take.** Sorted by why: no site on file 552 (many are a lane's mistake — one university's mailbox credited to dozens of unrelated buyers);
another mail domain read on the buyer's own site 331; another domain on another site 207 (mistakes); same domain, wrong purpose or a
duplicate of a row 182; Québec's health network domain 124. Decided: an INVOICING mailbox (by its local part) that the buyer's own site
prints counts as the buyer's also on another mail domain — its network's, its parent's, its shared-service centre's — never a
government-wide site, never webmail. A buyer's row also carries, among the records of its best tier, one whose value is $5,000 or more.

**6. What was told to the owner about a million.** One row is one organisation with a mailbox of its own and a Canadian biller. Inside
Canada an estimate of 400,000 to 500,000 such organisations at most; the rest must be organisations abroad tied to a Canadian biller by a
record (dealers, firms certified or licensed, customers of Canadian business software, owners of Canadian patents and trademarks). Not
promised; a counted number every time.

## 2026-11-12 03:10Z — three more levers for rows the owner ranks first, and for rows at all (claude)

**1. A buyer under contract takes any of its verified mailboxes that is its own.** The ranker kept one mailbox per key, the best-graded; a
lane's mailbox of another organisation (one US university's AP box was filed for dozens of unrelated buyers) hid the buyer's own one.
`rank.py: MAIL_ALL` keeps every verified mailbox of a "b:" key and `emailcols()` takes the best that fits. A sample build took 141 such
buyers; the rows with a published amount of $5,000 or more that meet the test went from 1,611 to 1,679 there.

**2. Buyers under a current contract with no mailbox of their own go to the mailbox reader.** The full build writes
`coord/results/ranked/contract_buyers_without_mailbox.csv` (key, name, own website; government-wide sites left out) and the mailbox-crawl
runners read it first; a lane's earlier (rejected) mailbox no longer keeps such a buyer out of the reader's queue.

**3. A distributor by the city an organisation's own page names, when no postal code was read.** 126,561 organisations with a mailbox
print no postal code that was read; 15,459 print "City, Province" beside their mailbox. A city names a distributor when 98 % or more of its
postal codes lie in one distributor's territory and at most 1 % in another's (`tools/on_ldc_table.py cities` -> `tools/data/city_biller.tsv.gz`:
5,105 of 7,294 places of the GeoNames dump; Toronto, Ottawa, London, Mississauga, Laval, Montréal, Winnipeg, Halifax, Regina, Surrey yes;
Kelowna, Westmount, Sherbrooke, Saskatoon, Barrie, Delta, Calgary no). The address cell says it is a city and where it was read; the
relationship sentence gives the share ("all", or "99.4 %"). A place the dump does not know (a region, a country: "Amsterdam (NL)") is not
one; two cities with two distributors in one text give none. The mailbox reader keeps the city line of a page with no postal address
(`site facts: city_quote, city_url`) for the sites it reads from now on.


## 2026-11-12 04:39Z — where an organisation is, when its own pages located nothing: its registered address, then the address a public places dataset lists for its website (claude)

The owner at 16:01 EST: "populate those fields as best as you can, don't just go empty … 1 million". Rule 13 needs, for a row that stands on
where the organisation is, the organisation's own address. Until now that address had to come from the organisation's own pages (the address
printed beside its mailbox or on its contact page, the postal code its home page prints, the city it names). 126,561 organisations whose
mailbox the referee re-read gave none of these; 145,060 keys of withdrawn leads were skipped in the 04:03Z build for that reason alone.

**1. Its registered address in a public registry, before anything else that is not its own page.** `org_places.csv.gz` (39,018 entries: the
CRA List of charities, Alberta's school authorities, Ontario's private schools) was already on the row as its address, but was never used to
name the distributor. It is now, after the organisation's own pages and before the city. The cell says "(its registered address in …)".
An entry on a public register is a fact (rule 1), and the address is the one the organisation filed.

**2. Then the address an Overture Maps place lists for its website** (Overture Maps Foundation, places theme: open data, a release a month,
taken from Meta's and Microsoft's business listings and others, most of them written by the business itself). Only:
- one address per registrable domain, when ALL of the domain's open places in Canada print the same postal code (629,062 of 734,698 domains,
  release 2026-10-21.0); a chain or a body with several sites gives none;
- when the place's name fits the organisation's (the domain's own label in the place's name, or a distinctive word both names share);
- when the postal code has a distributor (not Alberta, not an Ontario edge between two distributors, not a territory);
- and the shared-building rule applies as to any address (fifty organisations print the code: not ready).
Every cell says what it is: "(the address an Overture Maps place lists for its website <domain>: “<place's name>”, place <id>, from <datasets>;
Overture Maps Foundation open data, release <r> — a public places dataset, not the organisation's own pages)". The relationship sentence
says "the address a public places dataset lists for the organisation's website (Overture Maps; nothing on its own pages located it)", the
`source` column has its own wording, and `ship_ready` adds "the organisation's address is the one a public places dataset (Overture Maps)
lists for its website, not read on its own pages" — so these rows can be counted, sorted or taken out by one test. When the place gives no
province, the postal code's first letter gives it, and the cell says so.
Why it can carry a row: "something being where it is means that there's a relationship" (owner, 2026-11-11 06:24 EST). A business listing that
names the organisation's website and an address is a published statement that it is there; the distributor of that address bills an
occupant with its own meter by law. It is weaker than the organisation's own page, which always comes first, and the row says which it is.

**3. The same listed address fills the buyer's address of a row of another kind that has none** (4,938 rows that met the test had no buyer
address in the 04:03Z build: members, services, sponsors, dealers), with the same cell.

**Storage.** The address file is 40 MB compressed: not in git. `tools/credit_scan.py overture` writes it, `credit-scan.yml` (job overture,
monthly, the 25th) uploads it to the release `harvest-state`, and both rank workflows download it. A build without it is as before. The
merge step of that workflow no longer rewrites a site list that the run did not produce (it changed only the gzip header's time and
committed tens of megabytes of the same rows).

**Sample builds (1 in 4 of the leads, snapshot of 2026-11-11):** rows that meet the test 46,013 → 48,844 with the listed address
(2,176 rows by the listed address, 758 rows that gave way to it); with the registered address, 399 more rows by it (most of them would have
had the listed address or the city otherwise). In the sample, 1,646 listed addresses were not used because the place's name did not fit the
organisation's, and 3,987 because no distributor serves the postal code.

**Added at 04:58Z — the mailbox reader takes the sites a listed address locates.** `tools/lead_crawl.py` queued a site of another ending
than .ca only when its home page printed a Canadian postal address. A site whose domain an Overture Maps place lists with one postal code a
distributor serves is located all the same: 9,193 home pages the scan read print a role mailbox and no Canadian address (first class, read
with the other located sites), 22,546 print neither (second class, contact pages, 4 pages each). `mailbox-crawl.yml` downloads the address
file from `harvest-state`. `tools/credit_scan.py merge-graph` rewrites a list only when a row changed, with a fixed gzip time (the
Overture run at 04:54Z committed the same 20 MB list again).

## 2026-11-12 05:08Z — trademark owners abroad: the website an Overture Maps place lists under the owner's name, read first (claude)

The register names 134,458 organisations abroad as owners of Canadian marks, 109,538 with a Canadian agent of record (a record that ties
them to a Canadian biller; AGENTS.md §1 rule 12 names this lane). What was missing is their website, where their mailbox is. Guessing domain
names from their names (`tm_register.py sites --abroad`) tied 2,572 sites to 44,294 owners in the United States (5.8 %).
`tm_register.py overture-sites` joins the owners in the United States, the United Kingdom and Australia to the Overture Maps places of those
countries that list a website: the same name (legal forms left out, as `nkey`) at the register's postal code, or in its state — 14,112
owners (10,798 sites at the same postal code, 4,505 in the same state; release 2026-10-21.0) -> `data/incoming/claude/tm/tm_overture_sites.csv`.
`sites --abroad --overture` reads those published sites first. A site is tied as before (the register's postal code printed on its pages
and the same name; or the legal person with its legal form and an address of the owner's state), and now also when two sources agree: the
Overture place lists THIS website under the owner's name at the register's postal code (or in its state, and the site prints an address of
that state) AND the site's own pages state the owner's name. On 40 owners (the largest first): 10 tied (Google, Pfizer, Mattel, Henkel,
Honeywell, PepsiCo …), against 1 under the earlier tests alone. `tm-sites.yml` input `overture=true` writes the candidates first (job
candidates), then the runners read. The leads follow the daily `tm-register.yml` (match, leads), the mailbox reader, the referee.

## 2026-11-12 05:15Z — the distributors' numbers from the global LEI register; Nova Scotia Power's and Manitoba Hydro's due terms (claude)

Rule 16: "one page read at a biller fills thousands of rows: billers first". In the 04:03Z build the rows by where the organisation is that
met the test lacked the biller's number for BC Hydro (20,066 rows), Nova Scotia Power (2,528) and NB Power (1,497), and the due terms for
Manitoba Hydro (3,647) and Nova Scotia Power — so none of them counted among the rows with every main invoice field. Rule 11 lets a
biller's number in its home register stand for a GST/HST number that is not public, labelled. The global Legal Entity Identifier register
(GLEIF's open API, api.gleif.org) records, for each legal entity, its LEI and — where it has one — its number in its business register:
NB Power 022248 (New Brunswick Corporate Registry), Nova Scotia Power 1567820 (Nova Scotia Registry of Joint Stock Companies), Maritime
Electric 235139-1 (Corporations Canada), Newfoundland Power 4508 (Newfoundland and Labrador Registry of Companies); BC Hydro and Manitoba
Hydro (bodies created by their own Acts) have an LEI and no business-register number, and their cells say so. Each value carries a verbatim
excerpt of the register's record and its URL (`tools/data/billers_by_location.json: registration`; the row's `vendor_registry_id`, and
`vendor_tax_or_registration_number` says "this register entry carries no Business Number"). Due terms, each verified on the page: Nova
Scotia Power's Regulations, s. 5.4 ("Bills are due on the billing date." … not paid within twenty days after the billing date: an interest
charge; thirty days: disconnection), and Manitoba Hydro's billing glossary (due date; late payment charge of 1.25 % a month after it).

**Added at 05:24Z — owners in ten European countries too.** France, Germany, Italy, Spain, Switzerland, Austria, Belgium, Denmark, the
Netherlands, Sweden (`tm_register.py: EU_CODE`): the register's postal code is the last one of its one-line address; on a site it counts
when it is printed before a place name ("80331 München"), as a legal notice prints it; their legal forms (AG, GmbH, S.p.A., SARL, AB, N.V.
…) are left out of both names (`nkey_x`, the same pattern in Python and in DuckDB). 18,076 owners abroad now have a listed website (US
12,876 · DE 1,808 · GB 809 · IT 603 · AU 438 · CH 363 …). On 40 owners in Germany, Switzerland, Austria and Italy: 9 tied, four of them by
the postal code their own legal notice prints (Bosch, Osram, Kulzer, Prysmian …).

## 2026-11-12 05:59Z — a test hundred from the 05:23Z table, read row by row: five faults, each a rule (claude)

Drawn by `tools/test_sample.py` (seed 20261111, inside each kind; 164,391 ready rows). What was wrong, and the rule that now holds:
1. **A zero taken for an amount.** An import declaration (Colombia's customs statistics) whose value field was the duty paid, 0, was marked
   "published, under $5,000 (0)". A zero is no amount (`relationship_rows.published_amount`): the row is "no amount".
2. **A company's own press release labelled "fact, public record".** 73 ready rows stand on a contract a company announced on a newswire or
   in its newsroom (Cameco and Slovenské elektrárne, CGI and Caisse Alliance, AtkinsRéalis and Sizewell C). For a listed company that is
   a disclosure it answers for, and the rows stay public contracts; the sentence now says what it is: "fact, the vendor's own dated
   announcement of the agreement (not a public register)" (`relationship_rows.record_basis`).
3. **Agents of record that are persons.** "ANITA MAR", "LEI ZHOU", "MR. CHRISTOPHER TAN", "ME DANIEL ROUSSIN", "MAY M.M. CHENG": the test
   knew 575 given names and no honorific. It now reads honorifics (Mr., Me, Maître, Dr.), initials of several letters, "+" as a firm's sign
   ("PERRY + CURRIER"), and 37 more given names; a firm named after its founders ("ANDREWS ROBICHAUD", "STEWART MCKELVEY") stays a firm.
   Such rows do not meet the test (natural persons are left out, as everywhere).
4. **Page text in front of an address.** "dans la conception … à haute performance énergétique. Pont-Rouge, QC G3H2P9", "Contact Harry
   Walsh WPM Novar, ON" — with no street number in the quote, `ap_crawler.address_from` returned the whole quote. It now keeps the place in
   front of the province and postal code (the longest run of capitalised words that is a place of that province in the GeoNames names of
   `tools/data/city_biller.tsv.gz`), but only when what stands before it is the page's own text (a mailbox, a label, a sentence's end) and
   no street or box follows the last number. Over the 262,025 address quotes on file: 2,289 cuts change, every one shorter; a person's
   name before the place is no longer printed as part of an address.
5. **A copyright line taken for the name** ("© 2017-2026 ITMBC Enterprises Inc."): the sign and the years are taken off.
Seen and left as they are: a mailbox read on a directory page of the organisation's own domain (laconstruction.ca for defran.ca) — the
referee re-read it there; a mailbox in a link's title attribute (rpg.ca) — it is in the page as printed.

**Added at 06:36Z — three agent firms' numbers from the same register.** `tools/data/vendor_registers.json` (exact legal names in the global
LEI register only): Smart & Biggar S.E.C. — Québec enterprise number 3378010188; KPMG LLP — Ontario registration 981056021; Gowling WLG
(Canada) LLP — Ontario registration 260178397; each with the record's own words and URL. The ranker uses it last, only when nothing else
gave the row a vendor number (87 rows in a sample; most are clients of Smart & Biggar, the agent of record of many owners abroad).

## 2026-11-12 06:54Z — the billing period of a row's kind, when the biller's own sentence is not found (claude)

Rule 13 says a row whose biller's own sentence on how it bills is not found says how a bill of that kind comes, "by the kind of
relationship"; the payment route did, the billing period did not. In the 05:23Z build 9,710 membership rows that met the test, 272 licence
rows and 101 tenancy rows had "not published: billing period". `rank.py: billing_of` now gives, when nothing of the biller's own is read,
and says so in `recurring_billing_basis` ("by the kind of relationship: …; the body's own sentence … was not found"):
membership dues — by the year ("3 yearly or longer"); a licence or registration fee — for each year or period of the licence ("3");
rent — by the month ("1"); a sponsorship or an exhibitor's fee — for the event or the season ("3"); a dealer's purchases — for each order
("4 per transaction"); an agent of record's fees — for each filing, step and renewal ("4"). A biller's own sentence always comes first.
An electricity market operator (IESO, AESO) is the exception among the bodies: it settles its participants' charges every month ("1",
by the kind). In a 1-in-4 sample, 6,054 rows that meet the test now carry a period by the kind (membership 3,165, sponsorship 1,359,
agent of record 799, dealership 614, licence 74, tenancy 43); rows with an amount and a period 38,898 -> 38,987.

## 2026-11-12 13:40Z — whose mailbox, whose name, whose address; one row per organisation (claude)

The owner asked at 06:41 EST that nothing be misappropriated — no mailbox, no address — and that no buyer stand twice. The 10:45Z table was
read for it (197,202 ready rows). No mailbox stood twice. 5,425 ready rows had a mailbox on another domain than the organisation's website;
most were right (a town with two domains, a department on gc.ca), but a sample of 45 held eight wrong ones. What was found, and the rule now:

1. **A portal's page vouches for no mailbox.** A buyer whose site on file is a government portal page (gov.uk/government/organisations/…,
   canada.ca/…, quebec.ca/…) took any mailbox under that portal: @sutton.gov.uk "ended with .gov.uk", and Sutton Council's invoice mailbox went
   on the British Council's row. `ap_crawler.same_org`: such a site says nothing; the mailbox's own name decides (metoffice.gov.uk for the Met
   Office, cma.gov.uk for the Competition and Markets Authority pass; cabinetoffice.gov.uk for the Maritime and Coastguard Agency does not).
2. **The Québec health network's shared domain** (@ssss.gouv.qc.ca) counts for a body of the network, or when the mailbox is named after the
   buyer — a CIUSSS's procurement box had gone on the Buanderie centrale de Montréal's row.
3. **Where a mailbox was read decides whose it is** (AGENTS.md §2.5, "role mailboxes the organisation publishes itself"; and a register's or
   roster's e-mail is never used). Read on a directory or roster — 211, CIOC, informalberta, municipalites-du-quebec.com, a chamber's or an
   association's member list, a tourism site, Wikivoyage, the PEPPOL directory — a mailbox is not used: Wikivoyage had put a neighbouring
   parish's mailbox on Sainte-Marie-Madeleine's row. A mailbox on the organisation's own domain read on another site or file of its own stays
   (braudio.ca read on brianreimeraudio.com). A mailbox on ANOTHER domain must be read on the organisation's own pages, on a domain whose name
   spells it, on a government page that names it, or on its own files at a hosting service. `rank.py: mail_page_own`, in the three places a
   row takes a mailbox (contract buyers, leads, organisations by where they are).
4. **An invoicing mailbox on another mail domain, printed on the buyer's own site** (the rule of 00:14Z) — not from a page that lists other
   organisations (a town's business directory had given Crossfield Boom Construction's ap@, Crowsnest Pass Borne Industries', Penhold Epic
   Roofing's), and not a sister body's (Texas A&M took Kingsville's invoices@tamuk.edu). Those towns now carry their own mailboxes.
5. **PSPC's table of federal institutions**: the row of the institution named just before the mailbox — the Privy Council Office had taken the
   Privacy Commissioner's finances@priv.gc.ca, the line above its own. It now carries info@pco-bcp.gc.ca.
6. **Mailboxes for something else**: a service-quality / complaints box (qualite.services@), a register's (registretap@), a programme's funding
   box (financementpompiers@), stakeholder engagement (supplier engagement stays), surveys, recruiting (acquisition.talents@), a hospital's
   sales ledger, access to information written with a dot.
7. **Names and addresses.** A member directory's page prints the body's own address in its footer: 160 ready rows had the chamber's address
   as the member's (every Airdrie member at the Airdrie chamber's) — removed. A directory whose page title stood where the member's name goes
   had named five Tofino businesses "Tofino Chamber of Commerce" — such a row takes its own legal name or domain. Legal names read off a page
   lose a web agency's credit or page words ("City of Port Coquitlam Footer", "Municipalité de Val-Morin Conception", "Tous droits réservés,
   SPCTE Inc"); a photo credit, a slogan or a headline is no name; a professional regulator's name on a member's site is not the member's; a
   Wikidata label is kept only when it is the organisation's own name or its acronym's expansion (not "Public Safety Canada" for Québec's
   Ministère de la Sécurité publique, not "Umeå University" for Umeå universitet). Every copyright-line name now says the page it was read on
   (21,752 ready rows carried a bare name).
8. **One row per organisation** (owner, "the buyer is not repeated twice"; rule 14). The ranker keeps one row per key, but one organisation
   came in under two keys (rockyview.ca and mdrockyview.ab.ca; a contract record and a site reading). `tools/priority_sort.py` now joins rows
   with the same name (legal form aside) and the same postal code, mail domain or website domain, or the same mail domain and postal code
   (a domain no other body shares), and keeps the organisation's best row: the best class of priority, then the stronger relationship (rule 13),
   then the better mailbox. On the 10:45Z table: 2,446 rows left out, 460 of them ready; `out/ranked/duplicate_buyers_dropped.csv` lists each.

Measured on a 1-in-4 lead sample (never multiplied), the same data before and after: ready rows 48,912 -> 48,796. The 116 that went were
read row by row: mailboxes read on 211 / CIOC / municipalites-du-quebec.com / lecegep.ca / Wikivoyage / tourism and chamber lists /
the PEPPOL directory, an access-to-information or complaints box, a register's box, another body's box (Maritime and Coastguard Agency,
Buanderie centrale). Public bodies that lost a directory-read mailbox go back to the mailbox reader (contract_buyers_without_mailbox.csv).
Two rules tried and dropped the same hour: "cegep" as a category word and a stricter test for four-letter domain names — they took the
Cégeps of Victoriaville and Sorel-Tracy off their own mailboxes (cegepvicto.ca, cegepst.qc.ca).
Checked and kept as they are: two "Camp Massad" (Winnipeg, Montréal), two "Lakeview Dental" — different organisations with one name.

## 2026-11-12 14:45Z — a contract's billing period and the amount of one bill; the PO; a clean vendor first; free DNS (claude)

The owner, 09:00 EST: "those contract amounts, the billing cadence, you better have it set. Don't just put the value of the contract, but
also the billing cadence. So let's say it's monthly. What would that be?"; 09:11 EST: "If you can find a blanket PO, great. If you can't,
just state that … don't guess 8 digits"; 08:45 EST: an estimate where nothing is published, "very fairly accurate or plausible".

1. **A contract's billing period by what it buys** (`rank.py: contract_nature, contract_cadence_by_kind`). A public record gives parties,
   subject, value and dates, never a schedule of payments. What the contract buys is read from its commodity code (UNSPSC, CPV, NAICS),
   the record's own category, or the words of its title, and says how a contract of that kind is billed: works by progress invoice each
   month (in Ontario the Construction Act's rule, quoted), a service over a term each month in arrears, goods at each delivery, an unclear
   contract with a term of 60 days or more month by month. The row says "by the kind of relationship", from what the kind was read, and
   that the contract's own schedule is not published. A record whose own text names the period ("annual maintenance") keeps it.
   New column `contract_nature`.
2. **The amount of one bill** (`relationship_rows.py: contract_bill, value_by_buyer_term`). Monthly: the published value over the published
   term ("about $20,802 a month, calculated"). No end date published: over the average term of the buyer's own contracts whose two dates
   are published, two or more of them — an estimate, labelled. Yearly: one year of the term. At delivery with no term: the whole value.
   `billing_cadence` says it in words. **`amount_mark` of a contract is now by the amount of one bill** (rule 15, "per cadence"), not the
   whole value: a $20,000 contract over two years is "3 published, under $5,000 a bill (… about 833 a month …)". Expect the count of
   "published $5,000 or more" to fall by the contracts whose monthly bill is smaller.
3. **PO** (`po_or_reference_to_quote`): a PO number only when the record publishes one; "blanket" only when the record is a standing offer,
   blanket order or supply arrangement (its number is quoted on each call-up); otherwise "no PO number published; the contract number …
   (published in the record) is the reference an invoice quotes", or the award / notice number, or "no PO or contract number published".
   Other kinds say what their bill quotes instead (the account number on the distributor's bill, the member's number …) and that it is
   not published. Nothing is guessed.
4. **A clean vendor first.** Within a buyer's best tier, a record whose vendor the registers show alive and whose record prints the vendor's
   address comes before a bigger one: 254 buyers failed on a registry warning and 166 on a missing vendor address (13:24Z table) while
   other contracts of theirs were clean.
5. **Free DNS is no bill.** Namespro's own page: DNS hosting "100% free, included with all domain registrations … There is no monthly fee
   of any kind" (`tools/data/free_dns_providers.json`). Rows that stood on Namespro's DNS fail the test and say why (what is billed is the
   domain's registration, through a registrar: no row, rule 6).
6. Estimates for rows of other kinds with no amount (pushed with this): a trademark agent's row takes CIPO's official renewal fee as a
   floor; a chamber's member, the middle of the lowest dues the chambers of this build publish (twenty or more of them).

1-in-4 sample, never multiplied: ready contract rows 2,050 -> 2,123; service rows 1,963 -> 1,580 (Namespro, 422 rows); ready rows with an
amount and a billing period 39,775 -> 41,494, with a billing period 46,802 -> 48,477 of 48,498.

## 2026-11-12 15:05Z — Health Canada's right-to-sell invoices: a regulator lane of $5,000+ yearly bills; rosters by many hands (claude)

The owner, 09:00-09:15 EST: contracts first where they exist, "something damn near a contract", "most would be over 5,000", "a mixed
approach … all hands on deck". The mailbox reader has read 2,311,863 sites (431,882 with a role mailbox); the Canadian pool it reads is
nearly spent (13:08-14:23Z: +498 sites). Growth now needs new relationships, and new organisations, not more of the same sites.

1. **Health Canada invoices every company that sells a drug or a licensed medical device in Canada, every year** (`tools/hc_registers.py`,
   workflow `hc-registers.yml`, twice a day). Drug Product Database: the owner of each drug identification number with status Marketed;
   Health Canada's guidance: “Every October 1 st , Health Canada sends invoices for the upcoming year …”, “The person on record as owning the
   Drug Identification Number when the invoice is issued is responsible for payment.”, “Payment is due 30 days from date of issuance.” Fees
   as of April 1, 2026, from its fee page: $5,626 a drug ($3,391 a non-prescription drug, $1,760 a disinfectant). Medical Devices Active
   Licence Listing: the manufacturer of each Class II-IV licence issued and not cancelled, $460 a licence; “The invoices are mailed in
   February for payment within 30 days.” Payment, its own page: bill payment through a Canadian bank, direct deposit, wire, cheque, card.
   760 drug companies and 3,444 device makers (2,892 abroad); 1,320 of them are billed $5,000 or more a year (calculated from the published
   fees, labelled; a small business is billed 25 % less, not known per company). The row: kind "licence or registration", published amount
   = the fee of one product, `bill_amount_calculated` = the year's total, period yearly, delivery and terms in Health Canada's words.
   **Sites, no guessing:** a site on file that prints the company's postal code under a name that agrees (contact readings, trademark
   owners' sites): 353; then the company-name autocomplete, kept only when the domain IS the company's name on a generic ending or its
   country's (`domain_fits`), its home page carries the name, and — for a company whose register address is in Canada — the domain is .ca.
   The first pass without those two checks tied Janssen Inc. to a restaurant in Germany and Apotex to apotex.cz; they were taken out
   before anything was written (26 + 7 ties removed). A Canadian subsidiary is never given its parent's .com.
2. **Rosters and mailboxes by many hands.** Six helpers harvest public member directories (chambers and boards of trade of every province,
   construction associations) and Canadian trade shows' exhibitor lists into `data/incoming/claude/roster_<key>.csv` +
   `contrib/claude/rosters/<key>.json`, the format `tools/roster_ingest.py` checks (the body's own address with its postal code, its own
   sentence on dues or booth fees, the member's own site; never an e-mail from a roster). Three helpers research the 698 current contract
   buyers that have a website and no mailbox of their own (`coord/tasks/claude/claude_buyer_ap_batch908-914.csv`, largest contracts first),
   evidence re-read by the referee as for every lane.

## 2026-11-12 15:40Z — a namesake's dead register entry no longer takes out a vendor that a current record names (claude)

972 rows of the 13:24Z table failed on `vendor_registry_warning` alone (agents of record 444, contracts 254, members' bodies 95, suppliers
of dealers 83, …). Read row by row, many were living companies: GFL Environmental and Evertz Microsystems were "Inactive — amalgamated"
under old Ontario numbers, Kinectrics "Inactive" federally, Miller Paving matched to a struck-off Québec entity of another group. Now
(`rank.py`, R5.1): an amalgamated or continued corporation goes on as its successor (a note); a dead-looking entry keeps a note, not the
warning, when the row's own record is current — a body's roster or register read in the last year (tier M), a contract dated in the
last twelve months — or when the entry states no end ("Inactive" alone). The warning, which takes the row out, stays for a dissolution,
striking off, cancellation, revocation, liquidation or bankruptcy of a vendor no current record names. Tested on statuses taken from the
table (the 1-in-4 sample build could not run beside nine helpers: memory).

## 2026-11-12 15:50Z — an agent of record named as a person bills through the firm the register prints beside the name (claude)

1,292 agent-of-record rows (13:24Z table) failed on "the agent of record is a named person, not a firm". The trademarks register prints
the firm the agent works in, in brackets at the head of the agent's address: "(MILLER THOMSON LLP), 115 King Street South …", "(Yates IP),
17 Bellwood Avenue …", "(WITMART INC), 18 King Street East …". That firm sends the account. `relationship_rows.py`: when the bracket
carries a word of a firm (LLP, Inc., IP, Law, Agents …), the firm becomes the row's vendor, its address the rest of the line, and the
person is kept in `agent_named_on_register`; with no bracket, or a bracket with no firm word, the row stays out as before.

## 2026-11-12 16:10Z — lane `claude`: ISED's radio licensees (a regulator's yearly invoice, 27,051 organisations)

Every holder of a radio licence in Canada is invoiced by Innovation, Science and Economic Development Canada each year: "The annual fee
for the renewal of a radio licence is payable before the radio licence expires on March 31 of each year" and the fees "are used to
calculate licence renewal invoices" (RIC-42, Issue 16, April 2026); the invoice is paid by wire transfer or direct deposit to the
Receiver General for Canada, by cheque, or online (ISED's "Pay online" page). ISED's monthly open-data extract of the Spectrum
Management System names each licensee, its address, its client account and every authorization (status, in-service date, stations).
`tools/radio_licences.py` + `radio-licences.yml` (six runs a day until the names are all asked): granted, fee-paying authorizations;
organisations only (a name with a word of an organisation or a legal form; persons and names that say nothing are left out);
federal departments left out (they settle between departments, not by invoice); licensees holding only broadcasting, spectrum-licence or
earth-station authorizations left out (other fee orders, not read). 36,317 accounts → 27,051 organisations; 3,385 tied to a site on
file at once (2,898 leads after sites shared by more than three licensees are left out); the rest go to the company-name autocomplete,
one a second, kept only when the site's own home page carries the name. The amount is a floor, labelled so: "calculated — at least
C$X a year", from the lowest fee of ISED's own tables for each station (a fixed land-mobile station at the fee outside a metropolitan
area, a point-to-point station at the remote zone's rate); a fleet is counted once per authorization, and a record of more than 1,000
identical stations (meters, province-wide fleets) is not counted at all — leaving stations out keeps "at least" true. Rows go through
the member tier like Health Canada's; ISED is in `tools/payee_billing.py`. Quotes in a site tie no longer carry an e-mail address
(`hc_registers.no_mail`).

## 2026-11-12 16:25Z — lane `claude`: Health Canada's medical device establishment licences (3,223 holders, $5,519 a year each, invoiced)

The Health Canada lane (tools/hc_registers.py) now also reads the Medical Devices Establishment Licence listing: every importer or
distributor of medical devices in Canada holds an MDEL (2,219 in Canada, 684 in the United States, 131 in China …). Health Canada's fee
page: "Medical Device Establishment Licence $5,426 $5,519" (as of April 1, 2025 / 2026); its annual licence review: "We will issue an
invoice after we receive and screen your ALR application for completeness."; its fee guidance: "Payment is due upon issuance of the
invoice." The fee of one licence is the bill — published, over $5,000 — so these rows sort with the first mark. The listing is its own
search form (no robots.txt on the host, no CAPTCHA): three searches, one by activity, each returning every country. 384 holders tied to a
site on file at once; the rest go to the name autocomplete in the twice-daily Health Canada runs (the largest bills first).

## 2026-11-12 16:55Z — lane `claude`: two hosting vendors whose own pages offer the invoice paid by bank transfer

36,862 rows of a service seen on the buyer's side fail on "payment: not published"; 100 vendors stand behind 25,951 of them. Their own
sites were searched for how they are paid (sitemap pages on billing, payment, invoices, terms; the project's reader). Most take a card
or PayPal only (Hawk Host, easyDNS, doteasy …): those rows stay out. Two print an invoice payable by bank:
- Web Hosting Canada (whc.ca): "Complete our online order form to generate an invoice and select Wire Transfer / Interac / Deposit as
  the payment method." (https://whc.ca/pay). It also charges a card on file by default; its entry in `tools/tech_relationships.py`
  now carries both, bank first, and the row's route is "either" — in, by the owner's rule of 2026-11-11 14:20 EST ("an invoice that
  can be paid by bank transfer is in, also when the biller would take a card").
- Varial Hosting: "We accept payment by credit card, PayPal, Interac e-Transfer, electronic funds transfer (EFT) and..." and "If you
  wish to send payment for an invoice by cheque or money order …" (its knowledge base).
Canadian Web Hosting names wire transfers, Interac and cheques only in a refund clause: not taken (a refund clause is not how a bill is
paid). These rows are small bills (from C$2.79 a month) and sort under the $5,000 mark; a buyer with a record of its own keeps that.

## 2026-11-12 17:14Z — lane `claude`: the Canadian patents register (owners and their Canadian patent agent of record)

`tools/pt_register.py` + `pt-register.yml` (match + leads, daily) + `pt-sites.yml` (the owners' own sites, by dispatch). The Office's patent
register as open data (CSV extract of 2024-05-22, the one published as CSV): 386,885 patents and applications alive (status GR granted in
force; CO, ER, RP, AL, PG, AA, PI pending), each with its current owner and its agent of record. 91,523 owners have a Canadian agent of
record; 67,430 of them are organisations (28,150 in the United States, 8,879 in Canada …), 49,831 not on the trademarks register under the
same name. The agent firm's address is not in the patent table: it is taken from the same Office's trademarks register (its entry for the
firm, or the firm a person-agent's entry prints in brackets), and the row says so; an owner whose agent has no address there makes no row
(80,555 of 91,523 have one; Bereskin & Parr, 5,988 owners, is not on the trademarks register and its site did not answer). The relationship
is the agent's ("client of a Canadian patent agent of record"): the agent prosecutes the applications, pays the yearly maintenance fees and
bills the owner, sometimes through the owner's own counsel abroad — said on the row; kind "agent of record", billed per transaction. The
owner's site is tied by the trademarks lane's own tests, run on the patent owners' files (`tm_register.match / sites / merge_sites` with the
module's paths pointed at data/incoming/claude/pt/). First run here: 1,335 Canadian owners tied to sites on file → 1,127 leads. The extract
is 30 months old: a row says "extract of 2024-05-22" in its relationship; a newer CSV extract replaces it when the Office publishes one.

## 2026-11-12 17:22Z — lane `claude`: rosters at scale (chambers, exhibitors, dealers), lists on a platform, chambers' payment pages

- Today's roster merges added about 23,000 organisations as leads (chambers of commerce in every province, construction and trade
  associations, trade-show exhibitors, dealer networks of Canadian manufacturers). The merge now withdraws the leads of a roster that is
  withdrawn or no longer taken, and rewrites the leads of a corrected descriptor (cc_on_ssm withdrawn: its page says dues by credit card only).
- A trade show's exhibitor list is often kept on the organiser's platform (Map Your Show, a2z, PheedLoop, a second domain of the show):
  a descriptor may now name those hosts (`list_hosts`) with `list_host_link_url`, the organiser's own page that links the list there.
  The organiser's Canadian address still comes from its own site; a platform's domain is never taken as an exhibitor's site.
- Four chambers' own payment pages are payee entries (contrib/claude/payees/, verified by `payee_billing.py verify`): Saint John
  ("We accept Credit Card, Direct Deposit, E-transfer, Cash, Debit and Cheque"), Kensington ("… your KACC invoice"), Woodstock ("… an
  email and invoice for your yearly membership dues"), Bay St. George ("Payments can be made by cheque, cash or e-transfer.") — their
  rows say how they bill and are paid in the chamber's own words instead of "by the kind of relationship".

## 2026-11-12 18:17Z — lane `claude`: listed companies and their exchange (TSX, TSXV, CSE); who bills a dealer abroad; organisers with a Canadian office

- **A company listed on a Canadian exchange is billed by that exchange** — a fact the exchange itself publishes (its list of listed
  companies) and a bill it prints the rule of: Toronto Stock Exchange "The annual sustaining fee is invoiced in February of each year …"
  (C$12,000 at the least), TSX Venture Exchange "the annual sustaining fee is payable for each calendar year and is equal to $5,500 plus
  0.011% …" with "the remittance date specified by the Exchange in its invoice", the Canadian Securities Exchange "The monthly maintenance
  fee is due on the first business day of each month the Issuer is listed" ($1,000 a month at the least). Every such bill is over the
  $5,000 mark. New kind "exchange listing" (fields as a licence: buyer and biller addresses, what is billed, amount, period, reference =
  the symbol). The amount for TSX/TSXV is calculated from the market capitalization the exchange's own list gives (labelled "calculated");
  for the CSE the published floor. No exchange prints how its bill is paid: the row says it is by the kind (wire transfer, pre-authorised
  debit or cheque). Left out: ETPs, closed-end funds, depositary receipts (a manager or a bank pays, per product), SPACs and capital pool
  companies (shells), and CSE issuers suspended or halted. The issuer's site: the CSE's own list gives it; for TSX/TSXV the name
  autocomplete's domain under the issuer's very name, kept only when the home page prints the symbol on its exchange, or the domain is the
  name, the page names it and links investors' pages (the looser test took an airline's restaurant microsite and a consultancy named like
  a listed company: rejected).
- **A dealer abroad is the maker's only where the maker serves that market itself.** Where a maker's own pages name a separate company for
  a market (MacDon, Inc. for the US, MacDon Australia; Argon 18 Europe; Bourgault Australia), that market's dealers make no row of the
  Canadian maker: they are left out of its roster (dl_argon18 keeps 206 of 383 lines). Where the maker names no one, the Canadian maker is
  named and the row says the bill is by the kind of relationship.
- **An organiser that prints a Canadian office is a Canadian biller for the shows it runs from it** (§2.1 as written: the biller's own
  printed address): Marketplace Events (a US LLC) prints its Canadian offices — PO boxes in Scarborough and Toronto, Expo Média in
  Montréal — on its own sites; its 31 Canadian home, boat and equipment shows are kept, the row carrying the address it prints.
- **robots.txt that begins with a byte-order mark** was read as "allow all" by our readers (the first line did not parse): every shared
  reader now decodes it as utf-8-sig. A helper had fetched one disallowed script that way before noticing; nothing from it is kept.

## 2026-11-12 19:35Z — lane `claude`: rosters — tenants and the chain rule, who bills a member, sites that bar AI crawlers

- **A shopping centre's tenants do not count toward, and are not left out by, the more-than-15-rosters rule.** The rule (a domain that
  more than 15 bodies list is a chain's or a parent's site) protects against a franchisee or a branch that links its franchisor's site.
  A chain's store in a centre is leased by the chain itself, and one landlord's centres are each a roster (Cadillac Fairview's 14
  centres were 14): the rule had withdrawn lululemon, Sport Chek, Shoppers Drug Mart … from every list, chambers included. The chain's
  domain stays one buyer, one row.
- **A member billed by another body is not the roster's member.** Destination Québec cité says hotels' membership comes with their
  hotel association's and four MRCs' businesses join through their MRC: only its direct members are on its roster. Québec Vert's
  cards tagged with another association (APPQ, ASHOQ, AQPP, APGQ: "via cotisation à votre association") are left out of its roster.
  Municipalities that are free members of a tourism association (Bas-Saint-Laurent) are left out.
- **A directory that does not mark who pays is not a roster** (Destination Vancouver and Muskoka list paying members next to beaches,
  parks and trails; Destination Toronto and Discover Halifax are free for local businesses).
- **A site whose robots.txt bars ClaudeBot or anthropic-ai by name is not read, even when our project agent is allowed under `*`**
  (Tourisme Centre-du-Québec, Tourisme Côte-Nord; earlier Map Your Show). The site's intent is plain.
- **Dues payable by card only take the roster out** (Toronto Construction Association, Richmond Hill Board of Trade, Assiniboia Chamber:
  their own forms offer only a card), as cc_on_ssm was withdrawn. A body that prints no postal code does not pass (Kingston HBA,
  Brockville, Cape Breton).
