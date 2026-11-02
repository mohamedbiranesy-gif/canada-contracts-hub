# Standing orders — Claude, private-buyer expansion (handoff of 2026-11-01)

Start a new chat with: "Read prompts/claude_private_buyers.md in mohamedbiranesy-gif/canada-contracts-hub and continue."
Open that chat from the Claude desktop app with the owner's Mac linked; the crawlers run there.

You are Claude, lane `claude` (integrator). You continue the private-buyer work of the previous chat. Work
autonomously. The owner wants results and short updates, not narration.

## 0. First hour (do these in order)
1. Attach and clone the repo (add_repo owner=mohamedbiranesy-gif repo=canada-contracts-hub, access=push). Read
   AGENTS.md, CLAUDE.md, prompts/claude_integrator.md, coord/inbox/claude.md, the last entries of coord/DECISIONS.md,
   contrib/claude/rank_buyers/rank.py and batches.py, and the docstrings of the tools in section 3.
2. Check the Mac with the remote-devices MacOS-MCP Shell tool (user `mobzy`):
   `ps -eo pid,etime,command | grep -E "python3? .*(tools/|cch-private)" | grep -v grep`
   and `tail -3 ~/cch-crawler-state/search.log`. Shell replies time out after about 60 s. Start anything long with
   `(nohup /usr/bin/caffeinate -is <cmd> >> <log> 2>&1 &)` and poll the log. Use `git pull --rebase --autostash` and
   check the result afterwards when git is slow.
3. Restart whatever section 4 lists as not running and not finished.
4. Run one full loop round (section 5) and tell the owner, in one short message, the package counts before and after.

## 1. Goal and purpose
The owner is building, from public sources only, a sampling frame for a future high-level survey of organisations that
buy from Canada-located vendors. The survey will be designed later, so he wants as much data as possible. He plans to
ship the packages on Tuesday 2026-11-03.
Deliverable: one row per DISTINCT buyer (a buyer never repeats; a vendor may repeat). Each row has:
- the buyer's own published role mailbox;
- a named Canada-located vendor that buyer deals with;
- the relationship or contract details, with evidence.
Each buyer goes in the best package it qualifies for. Order of mailbox preference: AP/invoicing, then finance, then
purchasing, then general. Order of relationship strength: active, likely active (awarded 12–36 months ago, labelled),
client listing on the vendor's site, weaker link. Main metric: P01 GOLD (active relationship + confirmed invoicing/AP
mailbox); target 10,000.
**Focus: PRIVATE buyers.** The public buyers are nearly exhausted: about 3,100 have active contracts, and most of the
rest publish only a general mailbox.

## 2. Hard rules (AGENTS.md; the referee rejects anything that breaks them)
- The vendor's Canada location comes from the source itself: an address or country field, a Canada-HQ company's own
  site, a release dateline. Never infer it from the name.
- Evidence or nothing: the URL of a page actually opened, the retrieval date, and a quote of 300 characters or less
  containing the value. The referee re-fetches every page.
- Organisational role mailboxes only. Never a named person's mailbox, never an address built from a pattern. If no
  invoicing mailbox is published, keep the procurement mailbox, or failing that the general one, as `found` with a note.
- Rule 6: CAPTCHA, bot check, login wall or 401/403/429 means `blocked`; move on. No proxies, no archive copies of
  refused sites (archive copies only for pages that moved or are gone), no browser workarounds. Never automate the CRA
  registry.
- At most 2 requests per second per host, identify the user agent, cache everything. Never fabricate; `not_published`
  is a valid answer. GST/HST is derived (BN9 + RT0001) and always labelled `derived`.

## 3. Where things are
Mac (~ = /Users/mobzy):
- `~/cch-crawler`: main checkout. The crawlers run here. lead_scanner writes
  coord/tasks/claude/claude_buyer_ap_batch901.csv here, and the vendor lists batch902 (Wikidata), batch903 (verified
  vendors) and batch904 (OpenStreetMap) live only here.
- `~/cch-crawl-some`: checkout where `deep_pages.py --urls` runs. deep_pages commits and pushes its own rows to main.
- `~/cch-crawler-state`: venv (`~/cch-crawler-state/venv/bin/python3`), logs (search.log ...), done files.
- `~/cch-leads`: lead files `socrata_*.jsonl`:
  - rel = client pages, rel2 = client pages pass 2;
  - walls = home-page logo walls, stories = customer stories;
  - rel3_logos = Wikidata look-ups of logo names;
  - also `logo_names_*.jsonl` (names waiting for look-up).
- `~/cch-private`: build_new.py (new client domains not yet searched; appends them to new_targets_done.txt; run it with
  /usr/bin/python3), build_p2.py, edc_fetch.py, press_verify.py, peppol_targets.py, nw_lists.py.

Repo tools:
- `tools/ap_crawler.py`: crawler without AI that finds the AP mailbox on the buyer's website. In `same_org`, the
  PORTAL_MAIL list makes a shared government domain count only when the mailbox names the body. It uses Homebrew's
  pdftotext.
- `tools/deep_pages.py --urls <csv>`: opens page URLs found by search and keeps only mailboxes that are on the page, on
  the buyer's domain and role-type. Output: data/incoming/claude/claude_buyer_ap_results_search01.csv.
- `tools/lead_scanner.py --bridge`: turns `~/cch-leads/socrata_*.jsonl` into lead buyers (claude_buyer_leads.csv +
  batch901). It re-reads every 30 min.
- `tools/client_lists2.py`: vendor sitemap plus conventional paths (/clients, /case-studies, /nos-clients ...). Outbound
  links become relationship leads.
- `tools/logo_walls.py`: client logo walls on vendor home pages ("trusted by", "nos clients" ...; partner, award and
  certification sections excluded).
- `tools/customer_stories.py`: customer-story sitemaps of about 80 Canada-HQ companies (VENDORS list).
- `tools/logo_sites.py`: Wikidata website look-up for logo names (`find_any`; a one-word brand counts only when its
  domain spells it).
- `contrib/claude/rank_buyers/rank.py` + `batches.py`: the ranked deliverable.
  - Tiers: A active, B awarded under 12 months, L likely active (12–36 months), C older, D client listing, E other link
    on a vendor page.
  - Grades: 4 AP, 3 finance, 2 purchasing, 1 general.
  - Output: packages P01–P11 + Z in out/ranked/batches/.
  - Run both scripts locally (if inputs are missing: `gh release download dataset-latest -D data/release`) or with
    `gh workflow run rank-buyers.yml`.
- `contrib/claude/private_buyers/`: newswire contract releases, EDC transactions, client_page_domains_cleaned.csv,
  client_page_domains_new01–03.tsv (next is new04), dated_private_buyers*.csv.

## 4. State at handoff (2026-11-01 21:51 Toronto)
| Package | Buyers |
|---|---|
| P01 GOLD | 462 |
| P02 finance | 204 |
| P03 purchasing | 340 |
| P04 general | 1,099 |
| P05 likely active | 134 |
| P06 client listing + AP | 82 |
| P07 client listing + finance/purchasing | 75 |
| P08 client listing + general | 1,312 |
| P09 older | 646 |
| P10 linked from vendor site | 3,416 |
| P11 unconfirmed | 319 |
| Z no email | 1,984 |

About 8,090 rows have a mailbox. Confirmed AP across all packages is about 780.

Search rounds:
- Done: claude_search_urls_p1–p9 (B_001–017, B_101–103, B_201–206, B_301–310). Those batch files lived in the old
  chat's temporary folder and are gone; the merged p1–p9 CSVs are in the repo.
- The last `deep_pages --urls` run finished at 21:51 (139 buyers, 47 with a mailbox).
- **Next: p10, batch files numbered from B_311.**

Running on the Mac:
- client_lists2.py shards 0 and 1 (about 3 h in, about 42,600 vendor sites in total);
- ap_crawler.py ×2 (`--days 14 --workers 128`);
- deep_pages.py `--index 2 --targets ~/cch-private/p2_targets.csv`.

Not running:
- lead_scanner --bridge. Restart it in ~/cch-crawler:
  `(nohup /usr/bin/caffeinate -is ~/cch-crawler-state/venv/bin/python3 tools/lead_scanner.py --bridge >> ~/cch-crawler-state/bridge.log 2>&1 &)`
- logo_walls, logo_sites, customer_stories and the Peppol look-up. Check their `.done` files and logs, and restart
  whichever did not finish.

~/cch-private/new_targets.tsv holds only 33 rows; re-run build_new.py before the next round.

## 5. The loop (repeat; schedule yourself with send_later about every 40 min)
1. Mac: run `/usr/bin/python3 ~/cch-private/build_new.py`, copy ~/cch-private/new_targets.tsv to
   contrib/claude/private_buyers/client_page_domains_newNN.tsv (next NN) and push.
2. Cloud: split that file into `<scratchpad>/search/private2/B_NNN.tsv`, 330 rows each, with the header
   buyer_key, buyer, jurisdiction, website_host, tier, known_email. Write INSTRUCTIONS_BATCH.md (text below) to
   `<scratchpad>/search/`.
3. Launch up to 6 general-purpose subagents (model sonnet; haiku did worse) in ONE message, one B file each, with this
   prompt: "Read <dir>/INSTRUCTIONS_BATCH.md and follow it exactly. Input: <dir>/private2/B_NNN.tsv. Output:
   <dir>/private2/B_NNN_out.tsv. One WebSearch per group of 10 rows, never more. Reply with the one-line summary only."
   The budget is about 200 WebSearch calls per turn, shared by all agents, so 6 files per round.
4. Merge every B_*_out.tsv not yet marked `.done` into coord/tasks/claude/claude_search_urls_pNN.csv:
   - header buyer_key,buyer_name,website,official_site,url;
   - skip non-http URLs and empty keys; remove duplicates;
   - commit, push, and touch B_NNN.done.
5. Mac, in ~/cch-crawl-some:
   `git fetch -q && git show origin/main:coord/tasks/claude/claude_search_urls_pNN.csv > coord/tasks/claude/claude_search_urls_pNN.csv`
   then `(nohup /usr/bin/caffeinate -is ~/cch-crawler-state/venv/bin/python3 tools/deep_pages.py --urls coord/tasks/claude/claude_search_urls_pNN.csv --workers 12 >> ~/cch-crawler-state/search.log 2>&1 &)`
6. Run git pull, then rank.py and batches.py. Message the owner (one short message) only when P01 or P06 moved
   noticeably.
7. Append a short note to coord/inbox/claude.md (what ran, counts), then schedule the next check-in.

If new_targets.tsv is nearly empty, there is nothing new to search yet. Spend the round on section 6 instead, and on
restarting any finished crawler with a wider vendor list.

INSTRUCTIONS_BATCH.md (recreate verbatim):
```
# Find invoicing / accounts-payable pages for many organisations at once (10 sites per search)
You only LOCATE candidate page addresses. A separate program (no AI) opens every address you return and keeps an e-mail
only if it is really on that page, on the organisation's own domain, and a role mailbox (never a person). Never guess or
build an e-mail or URL; only copy URLs that appeared in search results.
## Input
TSV with header `buyer_key  buyer  jurisdiction  website_host  tier  known_email`, one organisation per row.
## Method
Take the rows in order, in groups of 10. For each group run exactly ONE WebSearch (mode "standard"):
- allowed_domains: the 10 website_host values of the group (as given);
- query: `accounts payable invoices email suppliers`
If a search fails with HTTP 400 PROXY_REJECTED, retry once as two searches of 5 domains.
Keep every URL whose host is one of the group's domains (or a subdomain) that could show an invoicing / AP / supplier /
vendor / finance e-mail: AP or invoicing pages, supplier/vendor information, supplier guides, purchase-order terms
(PDF/DOCX fine), vendor registration forms, finance department pages, contact pages. Skip news, careers, blog, products.
## Output
TSV (rewrite the whole file with the Write tool after every ~5 searches), header:
buyer_key<TAB>buyer_name<TAB>website<TAB>official_site<TAB>url<TAB>email_seen
One line per kept URL; buyer_key/buyer_name of the row whose website_host matches; website = https://<website_host>;
official_site empty; email_seen = an address shown next to AP words in the snippet, copied exactly, else empty.
Tabs only, no quotes.
Reply with ONE line: `<file>: <rows>, <searches run>, <urls kept>, <organisations with a url>`.
```

## 6. Ideas not built yet (biggest expected yield first; record the decision in coord/DECISIONS.md)
1. Owner's approved item 2: prove a vendor's Canada location by a business-registry match (Corporations Canada /
   provincial registries) for sources that name the supplier without an address, for example the ~33,000 rejected
   Nova Scotia records. Put these buyers in their own labelled package, never mixed with source-proven ones.
2. More Canada-HQ B2B vendors (TSX/TSXV) added to the customer_stories VENDORS list, and their sites added to the
   client_lists2 vendor list.
3. Dealer and member networks where the buyer pays a Canada-HQ supplier, each confirmed on the supplier's own dealer
   page: Home Hardware, Canadian Tire dealers, Federated Co-op, BRP/MacDon dealers, Familiprix/Uniprix.
4. Private prime contractors as buyers in US subaward data (socrata_usasub_*) where the sub-vendor's address is in Canada.

## 7. Quality checks every round
- Spot-check 10 new P01 rows: open the evidence URL and confirm three things. The mailbox is on that page, it is on the
  buyer's own domain (or a domain that spells the buyer), and it is a role mailbox, not a person.
- Expected yields, to tell whether a step works:
  - deep_pages --urls finds a mailbox for about a third of the searched buyers (last run 47 of 139);
  - a batch search keeps URLs for roughly half the organisations.
  - Far below either: inspect a sample before running more.
- Check coord/results/verification_log.csv for your rows. Fix the cause of any repeated `not_found_on_page`.

## 8. Lessons
- A shared government domain (canada.ca, gc.ca, gov.bc.ca ...) credits the wrong body unless the mailbox names it.
- Strip JSON escapes (u003e) from e-mails and reject word-glued addresses. Require the buyer's distinctive words on any
  page found by search.
- Sitemaps:
  - read both XML and gzip;
  - follow robots.txt sitemap lines and `<sitemapindex>` entries even without a .xml extension;
  - keep one URL per story across language copies.
- Some actions were refused by the safety system in the previous chat; do not attempt them:
  - deleting scheduled tasks;
  - fetching blocked sites.
- Keep your own context small. Subagents write files and reply in one line; never page large results through the chat.
- Before shipping on Tuesday:
  - run the ranker;
  - spot-check every package;
  - ask the owner which file format he wants for the packages.
