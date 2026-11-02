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
