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

## 2026-11-04 06:45 from claude
Registered for you (volume toward the owner's 10,000-Gold goal; integrity rules unchanged): `us_oh_checkbook_local`
(Ohio Checkbook, >1,000 local buyers; find the bulk export / API, check for a vendor address or state field),
`us_ny_openbook_local_authorities`, `uk_council_spend_over_500` (low Canadian yield, last). Also for review when you have
time: tools/org_contacts.py, tools/org_extras.py, tools/mx_check.py, tools/buyer_pages.py (all no-AI, polite) and the new
columns in contrib/claude/rank_buyers/README.md.

## 2026-11-06 18:15 from claude
Owner (2026-11-06): **PO numbers matter — go max, and every other identifier.** Data side done (rank.py: 14 identifier columns per row;
contracts_of_delivered_buyers export with every record and identifier). Source side: PO-level ledgers with a vendor location field are
the only way to add PO numbers at volume — eight registered today in coord/source_registry.csv (us_pennwatch_payments,
us_illinois_ledger_vendor_payments, us_texas_comptroller_payments, us_indiana_transparency_vendor, us_kansas_kanview,
us_nj_yourmoney_vendor_payments, us_massachusetts_cthru for codex; ca_municipal_purchase_orders_open_data for jules, p1). Keep the PO
number in `contract.identifiers` under a key containing `po` or `order_number`; Canada proof from the source's vendor address/state field
(or the vendor's own site via tools/org_contacts.py when the ledger has no address). Records → data/incoming/<lane>/records_<source_key>.jsonl.gz.

## 2026-11-08 18:35 from claude
See `prompts/lane_brief_2026-11-08.md`: new sources with supplier addresses (US cities / counties / states / transit / school districts, UK, EU, AU)
ranked by NEW buyers with a findable AP mailbox; codex_buyer_ap_batch01+ (799 open). Records in docs/SCHEMA.md format, scraper in contrib/codex/<source>/.

## 2026-11-08 21:45 from claude
- The ChatGPT account hit its usage limit at ~19:55Z ("try again at 6:34 PM" EST = 23:34Z): that is why the 30-minute automation went quiet after
  "[chatgpt] Verify buyer AP batch01 rows 161–170". Nothing to fix on your side; it resumes by itself.
- From 23:34Z a second, headless Codex run (`codex exec`, GPT-6.1 Sol high, own clone ~/cch-codex-exec, prompt in the Mac's
  ~/cch-crawler-state/codex_exec_prompt.md) works lane **codex** (`coord/tasks/codex/codex_buyer_ap_batch02+`), commits "[codex] buyer AP batchNN rows A–B"
  every 10 rows and restarts every 4 hours. The app automation keeps lane **chatgpt** (verify batches). Do not take each other's batches.
- Owner's standard (2026-11-08): every row is an invoice an AP clerk can pay — record in `invoicing_requirements_summary` everything the page prints:
  PO rule, payment terms, format, payment method, cheque-run cadence, tax treatment (GST/HST number, taxes shown separately), e-signature, AP system.
