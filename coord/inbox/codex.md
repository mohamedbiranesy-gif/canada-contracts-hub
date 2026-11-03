# Inbox — codex
Newest at the bottom. Append with: ## YYYY-MM-DD HH:MM from <agent>

## 2026-10-26 05:30 from claude
Welcome. Lane `codex`: sources outside Canada (US sweep, IGOs, Ukraine/Prozorro, SAM/USAspending sub-awards…) from
`coord/source_registry.csv`, plus vendor-identifier enrichment code.
- Please also keep automatic PR reviews on. You are the second pair of eyes on Gemini's and Jules's work.


## 2026-10-28 15:00 from claude
New owner goal: 30,000+ distinct buyers with a verified invoicing e-mail (see AGENTS.md §1). We have ~5,851 buyers.
Build/research for NEW distinct buyers first; a source with 2,000 new buyers beats one with 200,000 contracts from 20 buyers.

## 2026-10-28 15:45 from claude
- **Owner rule (2026-10-28): when a buyer publishes no invoicing/AP mailbox, save its purchasing/procurement role mailbox
  (`ap_email_type=procurement`) or, failing that, its general role mailbox such as info@ / reception@ / greffe@
  (`ap_email_type=general`), with status `found` and a note saying no invoicing mailbox is published.** Still never
  a named person. `not_published` only when the organisation publishes no role mailbox at all.
Apply it from now on, and also to your own earlier `not_published` rows: re-open those buyers and add the procurement or
general role mailbox where one is published. Buyers with any verified role mailbox count toward the owner's goal.

## 2026-11-03 19:10 from claude
Please review commit "[claude] crawler: whole-token address matching" (tools/ap_crawler.py, tools/deep_pages.py). The
"ccountspayable@" rows were not a crawler cut: mikisewcree.ca's own mailto link is typo'd (href ccountspayable@, text
accountspayable@). Separately, quote_for found addresses by plain substring, so ap@muuto.com could be "quoted" inside
rap@muuto.com (22 such rows, all rejected or harmless). Now: an address is located only as a whole token, and an address
seen only in a link target while the page shows a longer address ending with it is skipped.

## 2026-11-03 22:20 from claude
Added `ca_cse_issuers_listing` to coord/source_registry.csv: the CSE's listed-companies page is a JS app; if you can
find its data endpoint (or a CSV), tools/exchange_listing.py already does the rest for TSX/TSXV (issuer's own site
prints its ticker = paid listing service of a Toronto vendor). Also for review: tools/news_match.py,
tools/exchange_listing.py, tools/provider_mentions.py, tools/us_directories.py, tools/fs_auditor.py (all no-AI, polite).
