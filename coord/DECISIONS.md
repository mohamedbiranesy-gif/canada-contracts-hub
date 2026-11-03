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
