# Cloud lanes — status from the files on main (2026-11-10 09:29 UTC)

## 1. Sites
- `.ca` domains of the archive index: **354248**
- `.ca` domains of the web graph + public list: **2485064**
- domains linking to a proven Canadian vendor / vetted portal: **521219**
- OpenStreetMap Canada sites: **73684**
- domains linking to Shopify (store candidates): **1323837**
- home pages read by the scan: **1308798** (ok 781441, unreachable 329533, robots 83838, blocked 69990, http_error 43649, not_html 347); by detector: {'t1': 1519, 't4': 1307279}
- detector 4 (readable pages: 780265): **185798 print a role mailbox of the organisation (23.8 %)** — general 162677, role 21943, finance 793, accounts_payable 163, supplier_payment 118, procurement 85, invoice_submission 19; printed address: none 544285, CA 209333, US 23512, GB 2718, AU 417
- `.ca` sites whose home page prints a role mailbox (registry candidates, tier R): **133597**

## 2. Vendors and providers checked live (their own site's address)
- 47468 domains: no_address 20914, CA 10660, CA-loc 3866, unreachable 3166, blocked 3026, US 2382, robots 1600, GB 639

## 3. DNS lookups
- domains looked up in the cloud: **673794**; on Shopify's storefront addresses: **18181**; with a www alias: 0

## 4. Relationship leads on file
- Mac era B/L dated record (payment, subaward, release): **10803**
- Mac era D/E listed on a Canadian vendor's page (client, member, dealer, sponsor): **52386**
- Mac era M member / regulated payer list: **2290**
- Mac era T vetted software service (store / portal): **5511**
- cloud D/E listed on a Canadian vendor's page (client, member, dealer, sponsor): **76685**
- cloud M accredited business (BBB) [bbb]: **816**
- cloud M licence holder (the licensing body's own list of active licences) [lic]: **1664**
- cloud M licence holder (the licensing body's own list of active licences) [rbq]: **10748**
- cloud M membership stated by the member: **938**
- cloud T credit line on the buyer's site: **40279**
- cloud T provider in the buyer's DNS: **47352**
- cloud T vetted software service (store / portal): **2900**

## 5. Mailbox crawl
- lead sites read: **29375** (nothing_found 18793, found 7923, blocked 2651, error 6, timeout 2)
  - D/E listed on a Canadian vendor's page (client, member, dealer, sponsor): 24617 read, mailbox on 6784 (28 %), blocked 2246
  - leads no longer on file (withdrawn by a stricter rule) and registry candidates: 4758 read, mailbox on 1139 (24 %), blocked 405
- candidate sites (stores / portals) read: **24445**
  - amilia: 178 read — nothing_found 81, accepted 49, out_of_scope 20, no_address 20, blocked 8
  - bibliocommons: 30 read — nothing_found 21, out_of_scope 7, no_address 2
  - d2l: 20 read — nothing_found 18, blocked 1, out_of_scope 1
  - jane: 776 read — nothing_found 322, accepted 196, out_of_scope 123, no_address 87, blocked 46, no_name 1, error 1
  - shopify: 23437 read — blocked 9024, nothing_found 7298, no_address 3517, accepted 2656, out_of_scope 542, service_not_seen 333, no_name 63, no_role_mailbox 4
- mailbox rows written by the cloud crawls (before the referee): **11886**

## 6. Delivered (last rank build on main)
- rows with a confirmed mailbox: **70414** — by tier: A 1227, B 1580, C 312, D 11104, E 2406, F 7, I 10644, L 365, M 4150, R 25497, T 13122
- named-vendor relationships (A B T M C D L E): **34266** · registry contract R: **25497** · weaker / inferred (F I): **10651**
