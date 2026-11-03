# Gold programme loop (Claude, lane `claude`) — standing prompt, re-fired every ~60 minutes by a scheduled task

Owner (2026-11-03): "find new leads deep, use all tools, get Gold to the thousands, private and public buyers, give
yourself your own prompts, full autonomous." Gold = P01 (dated relationship ≤12 months + confirmed invoicing mailbox)
and P01T (active paid service of a Canada-HQ vendor seen on the buyer's own site + invoicing mailbox). Hard rules:
AGENTS.md §2 (no fabrication, evidence or nothing, robots/blocks respected, ≤1–2 req/s/host, no named persons).

## Each firing (keep each step short; everything heavy runs on the owner's Mac in the background)
1. **Engines on the Mac** (MacOS-MCP Shell, ~/cch-vnews for new tools, venv ~/cch-crawler-state/venv/bin/python3):
   `tail -1` of ~/cch-crawler-state/{fs_auditor,news_match,exchange,site_finder3,tech_cdx_*,crawl_some_*,crawler,push_loop}.log;
   `ps aux | grep -E "fs_auditor|news_match|exchange_listing|tech_relationships|site_finder|crawl_some|ap_crawler|lead_scanner|push_loop"`.
   Restart anything that died (same command lines as in coord/DECISIONS.md 2026-11-03 entries). Never run two copies.
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
   - AP-mailbox search rounds for new dated buyers without one (ap_upgrade_targets.py → B/D files → agents → merge_search.py).
   - once a day: `tech_relationships.py --reverse` over the new crawl results (big_companies, exchange_sites, crux)
     so Shopify / Coveo / Unbounce / Lightspeed / Benevity links on newly crawled sites become T leads; then
     `crawl_some.py` on ~/cch-crawl-some/exchange_sites.csv again (the done list skips finished issuers);
   - RDAP registrar check of AP-grade organisations' own domains (Tucows Domains Inc., Webnames.ca, Rebel.ca,
     easyDNS — Canadian registrars; current registration = paid service): own package, owner to decide.
6. Re-schedule this loop (send_later, 60 min) unless the owner said stop. Commit tools/docs; push with `timeout 200`.
