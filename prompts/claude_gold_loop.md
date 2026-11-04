# Gold programme loop (Claude, lane `claude`) — standing prompt, re-fired every ~60 minutes by a scheduled task

Owner (2026-11-03): "find new leads deep, use all tools, get Gold to the thousands, private and public buyers, give
yourself your own prompts, full autonomous." Gold = P01 (dated relationship ≤12 months + confirmed invoicing mailbox)
and P01T (active paid service of a Canada-HQ vendor seen on the buyer's own site + invoicing mailbox). Hard rules:
AGENTS.md §2 (no fabrication, evidence or nothing, robots/blocks respected, ≤1–2 req/s/host, no named persons).

## Mac access (since 2026-11-04 02:00Z)
The MacOS-MCP Shell is dead (a `pkill -f` matched its own bash). Use `mcp__remote-devices__Control_your_Mac__osascript` with
`do shell script "…; exit 0"`: output newlines collapse, keep each call under ~25 s, start background jobs with
`(cd DIR && nohup CMD > ~/cch-crawler-state/X.log 2>&1 < /dev/null &)` in a call of their own, kill by PID from `ps -axo pid=,command=`
(never a pattern the command itself contains). Never write files into ~/cch-crawler except data/incoming/claude (an untracked file
there blocks push_loop's rebase: "would be overwritten by checkout"); tool copies go to ~/cch-vnews/tools, task files to ~/cch-oc,
~/cch-bp, ~/cch-apfirst, ~/cch-crawl-some. Deploy a tool with `git fetch -q origin main && git show origin/main:tools/X.py > ~/cch-vnews/tools/X.py`.

## Each firing (keep each step short; everything heavy runs on the owner's Mac in the background)
1. **Engines on the Mac** (~/cch-vnews for tools, venv ~/cch-crawler-state/venv/bin/python3):
   `tail -1` of ~/cch-crawler-state/{org_contacts,buyer_pages,bridge,fs_auditor,stories_0,stories_1,stories_2,tech_cdx_*,site_finder5,
   crawl_some_big,crawl_some_crux,push_loop,ap_pages2,deep_pages_p3*}.log; `pgrep -f` each of org_contacts.py, buyer_pages.py,
   lead_scanner.py --bridge, fs_auditor, customer_stories, tech_relationships, site_finder_names, crawl_some, ap_crawler, push_loop.
   Restart anything that died (command lines in coord/DECISIONS.md 2026-11-03/04 entries). Never run two copies.
   - org_contacts (completeness: buyer/vendor address, phone, role mailboxes → data/incoming/claude/claude_org_contacts.jsonl.gz):
     `tools/org_contacts.py --tasks ~/cch-oc/tasks_all.csv --workers 48 --repo ~/cch-crawler`; when it finishes, regenerate the task
     lists from the latest ranked_buyers.csv (contrib/claude/org_contacts, the snippet in the 2026-11-04 session) for new organisations.
   - buyer_pages (dated awards on the buyer's own site → ~/cch-leads/socrata_buyer_pages.jsonl):
     `tools/buyer_pages.py --orgs ~/cch-bp/orgs_round1.csv --vendors ~/cch-bp/vendors_ca.tsv.gz --workers 24 --pages 40`; round 2 =
     the D/E/L/C/T organisations with any mailbox, round 3 = I-tier municipalities / school boards / health bodies.
2. **Feed the crawler**: new lead files (~/cch-leads/socrata_*.jsonl) are picked up by `lead_scanner.py --bridge`
   (running). New websites (~/cch-crawler-state/websites.tsv) are read by ap_crawler / crawl_some. For a new task CSV
   (e.g. ~/cch-crawl-some/exchange_sites.csv, big_companies.csv): start `crawl_some.py <csv> --workers 16` once.
3. **Rank**: the rank-buyers workflow runs every 3 h; dispatch it (`gh api -X POST repos/.../actions/workflows/rank-buyers.yml/dispatches -f ref=main`)
   when ≥30 min of new rows were pushed. Read coord/results/ranked/SUMMARY.md. Spot-check 5 NEW Gold / Gold-T rows
   (email on the buyer's own domain, invoicing word next to it, record date, vendor really Canadian) before telling the owner.
4. **Owner message** (SendUserMessage) only when a number moved or a new source started: P01 / P01T / P13 / total vs the
   previous message, one line per new source with its yield. No narration.
5. **Next lever** (pick the top one not yet running; record it in coord/DECISIONS.md when started):
   - more P01T vendors with verified Canadian HQ and visible tenants (see research/TENANTS_REPORT.md): Achievers, Axonify,
     Intelex (tenants robots-blocked: use buyer-side mentions), Procurify, Jostle, Uberflip, Influitive, PressReader,
     TumbleBooks, Moneris (re-check HQ page), CSE-listed issuers (CNSX Markets Inc., 100 King St W Toronto) in exchange_listing;
   - NY Ed Law 2-d district pages (vendor + contract term, public) and Illinois SOPPA lists for Canadian edtech
     (Prodigy, D2L, Edsby, SMART/Lumio, Xello, KEV, Showbie): write the scope into coord/source_registry.csv for jules;
   - text signals on buyer sites: EAP / benefits carriers named on HR pages (Homewood Health, TELUS Health, Sun Life,
     Manulife, Canada Life, GSC, Medavie, Pacific/Alberta Blue Cross, Desjardins, Beneva, iA), Maplesoft / Crowdmark on
     university pages, Moneris checkout on payment pages: a scanner over the crawl cache, each vendor's HQ quoted;
   - membership / statutory fee relationships with Canadian bodies printed on the buyer's own site (OSFI-regulated,
     CDIC member, Payments Canada member, IESO / AESO market participant, CIRO dealer) — own package, owner to decide;
   - fs_auditor for the organisations whose statements the crawler could not find: web-search rounds (sonnet agents,
     INSTRUCTIONS_FS.md) for AP-grade organisations first, then `fs_auditor.py <located.tsv>`;
   - AP-mailbox search rounds (200 WebSearch calls per turn, shared by all agents; launch every agent of a round in ONE message):
     upgrade files scratchpad search/up7/B_908.tsv (the last Gold-eligible organisations), B_909–B_911 (client listings → P06),
     then mailbox-first sector queries search/apfirst/Q_04_rest, Q_05_rest, Q_06–Q_12 (INSTRUCTIONS_APFIRST.md → base64 → Mac
     ~/cch-apfirst/roundN_urls.tsv → `tools/ap_pages.py <tsv> --workers 8`); B files → merge_search.py pNN → on the Mac
     `tools/deep_pages.py --urls <path outside ~/cch-crawler>`. Regenerate B files with ap_upgrade_targets.py --skip <all searched B files>.
   - once a day: `tech_relationships.py --reverse` over the new crawl results (big_companies, exchange_sites, crux)
     so Shopify / Coveo / Unbounce / Lightspeed / Benevity links on newly crawled sites become T leads; then
     `crawl_some.py` on ~/cch-crawl-some/exchange_sites.csv again (the done list skips finished issuers);
   - RDAP registrar check of AP-grade organisations' own domains (Tucows Domains Inc., Webnames.ca, Rebel.ca,
     easyDNS — Canadian registrars; current registration = paid service): own package, owner to decide.
6. Re-schedule this loop (send_later, 60 min) unless the owner said stop. Commit tools/docs; push with `timeout 200`.
