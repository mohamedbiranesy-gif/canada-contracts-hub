# Cloud lanes — status from the files on main (2026-11-10 08:20 UTC)

## 1. Sites
- `.ca` domains of the archive index: **354248**
- `.ca` domains of the web graph + public list: **2485064**
- domains linking to a proven Canadian vendor / vetted portal: **421156**
- OpenStreetMap Canada sites: **73684**
- domains linking to Shopify (store candidates): **1323818**
- home pages read by the scan: **435316** (ok 364948, blocked 26332, unreachable 25200, robots 11913, http_error 6763, not_html 156); by detector: {'t1': 435316}

## 2. Vendors and providers checked live (their own site's address)
- 26112 domains: no_address 10946, CA 6977, CA-loc 2307, blocked 1714, unreachable 1546, robots 944, US 870, GB 241

## 3. DNS lookups
- domains looked up in the cloud: **68**; on Shopify's storefront addresses: **4**; with a www alias: 0

## 4. Relationship leads on file
- Mac era B/L dated record (payment, subaward, release): **10803**
- Mac era D/E listed on a Canadian vendor's page (client, member, dealer, sponsor): **52386**
- Mac era M member / regulated payer list: **2290**
- Mac era T vetted software service (store / portal): **5511**
- cloud D/E listed on a Canadian vendor's page (client, member, dealer, sponsor): **76418**
- cloud M licence holder (the licensing body's own list of active licences) [lic]: **2226**
- cloud T credit line on the buyer's site: **24356**
- cloud T provider in the buyer's DNS: **1319**
- cloud T vetted software service (store / portal): **2900**

## 5. Mailbox crawl
- lead sites read: **29375** (nothing_found 18793, found 7923, blocked 2651, error 6, timeout 2)
  - D/E listed on a Canadian vendor's page (client, member, dealer, sponsor): 24781 read, mailbox on 6846 (28 %), blocked 2268
  - leads no longer on file (withdrawn by a stricter rule) and registry candidates: 4594 read, mailbox on 1077 (23 %), blocked 383
- candidate sites (stores / portals) read: **24445**
  - amilia: 178 read — nothing_found 81, accepted 49, out_of_scope 20, no_address 20, blocked 8
  - bibliocommons: 30 read — nothing_found 21, out_of_scope 7, no_address 2
  - d2l: 20 read — nothing_found 18, blocked 1, out_of_scope 1
  - jane: 776 read — nothing_found 322, accepted 196, out_of_scope 123, no_address 87, blocked 46, no_name 1, error 1
  - shopify: 23437 read — blocked 9024, nothing_found 7298, no_address 3517, accepted 2656, out_of_scope 542, service_not_seen 333, no_name 63, no_role_mailbox 4
- mailbox rows written by the cloud crawls (before the referee): **11886**

## 6. Delivered (last rank build on main)
- rows with a confirmed mailbox: **69663** — by tier: A 1227, B 1582, C 349, D 12163, E 2631, F 8, I 12223, L 378, M 1821, R 27809, T 9472
- named-vendor relationships (A B T M C D L E): **29623** · registry contract R: **27809** · weaker / inferred (F I): **12231**
