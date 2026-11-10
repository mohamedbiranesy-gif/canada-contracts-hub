# Cloud lanes — status from the files on main (2026-11-10 14:30 UTC)

## 1. Sites
- `.ca` domains of the archive index: **354248**
- `.ca` domains of the web graph + public list: **2485064**
- domains linking to a proven Canadian vendor / vetted portal: **521219**
- OpenStreetMap Canada sites: **73684**
- domains linking to Shopify (store candidates): **1323837**
- home pages read by the scan: **3010354** (ok 1310325, unreachable 1285871, robots 195520, blocked 117898, http_error 99950, not_html 790); by detector: {'t1': 24, 't4': 3010330}
- detector 4 (readable pages: 1310309): **280623 print a role mailbox of the organisation (21.4 %)** — general 242723, role 36165, finance 1126, accounts_payable 235, supplier_payment 200, procurement 131, invoice_submission 43; printed address: none 961772, CA 287154, US 54400, GB 5827, AU 1156
- `.ca` sites whose home page prints a role mailbox (registry candidates, tier R): **176238**

## 2. Vendors and providers checked live (their own site's address)
- 87855 domains: no_address 39293, unreachable 14240, CA 11716, US 4850, blocked 4842, robots 4332, CA-loc 4055, GB 1497

## 3. DNS lookups
- domains looked up in the cloud: **4129026**; on Shopify's storefront addresses: **542022**; with a www alias: 161652

## 4. Relationship leads on file
- Mac era B/L dated record (payment, subaward, release): **10803**
- Mac era D/E listed on a Canadian vendor's page (client, member, dealer, sponsor): **52386**
- Mac era M member / regulated payer list: **2290**
- Mac era T vetted software service (store / portal): **5511**
- cloud D/E listed on a Canadian vendor's page (client, member, dealer, sponsor): **82814**
- cloud M accredited business (BBB) [bbb]: **816**
- cloud M licence holder (the licensing body's own list of active licences) [lic]: **1664**
- cloud M licence holder (the licensing body's own list of active licences) [rbq]: **11027**
- cloud M membership stated by the member: **1404**
- cloud T credit line on the buyer's site: **66896**
- cloud T provider in the buyer's DNS: **120480**
- cloud T vetted software service (store / portal): **2900**
- cloud T vetted software service (store / portal) [shards]: **7673**

## 5. Mailbox crawl
- lead sites read: **225441** (nothing_found 106005, found 103678, blocked 15514, timeout 211, error 33)
  - D/E listed on a Canadian vendor's page (client, member, dealer, sponsor): 88581 read, mailbox on 22643 (26 %), blocked 9064
  - leads no longer on file (withdrawn by a stricter rule) and registry candidates: 77780 read, mailbox on 62282 (80 %), blocked 4001
  - T credit line on the buyer's site: 28658 read, mailbox on 10336 (36 %), blocked 902
  - T provider in the buyer's DNS: 26286 read, mailbox on 6906 (26 %), blocked 1239
  - M licence holder (the licensing body's own list of active licences) [rbq]: 1397 read, mailbox on 897 (64 %), blocked 34
  - B/L dated record (payment, subaward, release): 1035 read, mailbox on 142 (14 %), blocked 147
  - T vetted software service (store / portal): 736 read, mailbox on 113 (15 %), blocked 79
  - M membership stated by the member: 508 read, mailbox on 207 (41 %), blocked 5
  - M member / regulated payer list: 271 read, mailbox on 36 (13 %), blocked 32
  - M accredited business (BBB) [bbb]: 161 read, mailbox on 90 (56 %), blocked 11
- candidate sites (stores / portals) read: **53482**
  - absorb: 128 read — nothing_found 70, out_of_scope 29, no_address 18, accepted 8, blocked 1, portal_not_its_own 1, no_name 1
  - amilia: 521 read — nothing_found 219, accepted 151, no_address 64, out_of_scope 42, portal_not_its_own 23, blocked 13, no_name 9
  - benevity: 21 read — nothing_found 15, portal_not_its_own 2, out_of_scope 2, blocked 1, no_address 1
  - bibliocommons: 264 read — nothing_found 203, out_of_scope 30, accepted 18, no_address 4, no_name 4, blocked 3, portal_not_its_own 1, error 1
  - coconut: 82 read — nothing_found 61, out_of_scope 9, accepted 7, no_address 3, portal_not_its_own 1, no_name 1
  - coveo: 190 read — nothing_found 170, no_address 9, out_of_scope 5, accepted 4, no_name 1, timeout 1
  - d2l: 268 read — nothing_found 158, out_of_scope 34, blocked 25, accepted 19, no_address 17, portal_not_its_own 11, no_name 4
  - docebo: 70 read — nothing_found 38, out_of_scope 16, no_address 13, accepted 2, blocked 1
  - edsby: 69 read — nothing_found 37, accepted 14, portal_not_its_own 9, no_name 4, blocked 3, no_address 2
  - escribe: 74 read — nothing_found 58, no_address 8, accepted 4, out_of_scope 2, portal_not_its_own 1, blocked 1
  - jane: 19116 read — nothing_found 10374, accepted 4120, no_address 1982, portal_not_its_own 1852, blocked 490, no_name 294, error 2, no_role_mailbox 2
  - jobber: 3586 read — nothing_found 2082, no_address 727, accepted 656, no_name 63, blocked 57, error 1
  - kev: 153 read — nothing_found 110, blocked 11, accepted 8, out_of_scope 8, no_name 6, no_address 5, portal_not_its_own 5
  - shopify: 28912 read — nothing_found 9759, blocked 8652, accepted 5869, no_address 2771, out_of_scope 1497, service_not_seen 315, no_name 45, no_role_mailbox 4
- mailbox rows written by the cloud crawls (before the referee): **120728**

## 6. Delivered (last rank build on main)
- rows with a confirmed mailbox: **160079** — by tier: A 1227, B 1661, C 305, D 20370, E 4306, F 8, I 14237, L 413, M 5078, R 74764, T 37710
- named-vendor relationships (A B T M C D L): **66764** · registry contract R: **74764** · link only (E): **4306** · older / inferred (F I): **14245**
