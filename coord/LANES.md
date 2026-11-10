# Cloud lanes — status from the files on main (2026-11-10 22:39 UTC)

## 1. Sites
- `.ca` domains of the archive index: **354248**
- `.ca` domains of the web graph + public list: **2485064**
- domains linking to a proven Canadian vendor / vetted portal: **717414**
- OpenStreetMap Canada sites: **73684**
- domains linking to Shopify (store candidates): **1323839**
- home pages read by the scan: **3013688** (ok 1312776, unreachable 1286417, robots 195667, blocked 117982, http_error 100055, not_html 791); by detector: {'t1': 24, 't4': 3013664}
- detector 4 (readable pages: 1312760): **282405 print a role mailbox of the organisation (21.5 %)** — general 244323, role 36338, finance 1132, accounts_payable 237, supplier_payment 200, procurement 131, invoice_submission 44; printed address: none 963341, CA 287942, US 54489, GB 5832, AU 1156
- `.ca` sites whose home page prints a role mailbox (registry candidates, tier R): **176295**

## 2. Vendors and providers checked live (their own site's address)
- 87879 domains: no_address 39305, unreachable 14242, CA 11717, US 4856, blocked 4844, robots 4332, CA-loc 4055, GB 1498

## 3. DNS lookups
- domains looked up in the cloud: **4144726**; on Shopify's storefront addresses: **556326**; with a www alias: 161652

## 4. Relationship leads on file
- Mac era B/L dated record (payment, subaward, release): **10803**
- Mac era D/E listed on a Canadian vendor's page (client, member, dealer, sponsor): **52386**
- Mac era M member / regulated payer list: **2290**
- Mac era T vetted software service (store / portal): **5511**
- cloud D/E listed on a Canadian vendor's page (client, member, dealer, sponsor): **118232**
- cloud M accredited business (BBB) [bbb]: **816**
- cloud M licence holder (the licensing body's own list of active licences) [lic]: **3806**
- cloud M licence holder (the licensing body's own list of active licences) [rbq]: **11027**
- cloud M member / regulated payer list: **2633**
- cloud M membership stated by the member: **1404**
- cloud T credit line on the buyer's site: **66899**
- cloud T provider in the buyer's DNS: **120571**
- cloud T vetted software service (store / portal): **2900**
- cloud T vetted software service (store / portal) [shards]: **15234**

## 5. Mailbox crawl
- lead sites read: **471385** (nothing_found 278378, found 166722, blocked 25728, timeout 499, error 58)
  - leads no longer on file (withdrawn by a stricter rule) and registry candidates: 188226 read, mailbox on 103925 (55 %), blocked 7507
  - T provider in the buyer's DNS: 108228 read, mailbox on 14509 (13 %), blocked 4761
  - D/E listed on a Canadian vendor's page (client, member, dealer, sponsor): 105665 read, mailbox on 25203 (24 %), blocked 10877
  - T credit line on the buyer's site: 58801 read, mailbox on 19521 (33 %), blocked 1963
  - M licence holder (the licensing body's own list of active licences) [rbq]: 5866 read, mailbox on 2690 (46 %), blocked 164
  - B/L dated record (payment, subaward, release): 1427 read, mailbox on 165 (12 %), blocked 190
  - T vetted software service (store / portal): 1071 read, mailbox on 140 (13 %), blocked 128
  - M membership stated by the member: 1010 read, mailbox on 299 (30 %), blocked 15
  - M accredited business (BBB) [bbb]: 622 read, mailbox on 188 (30 %), blocked 72
  - M member / regulated payer list: 409 read, mailbox on 39 (10 %), blocked 51
  - M licence holder (the licensing body's own list of active licences) [lic]: 60 read, mailbox on 43 (72 %), blocked 0
- candidate sites (stores / portals) read: **89407**
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
  - shopify: 64837 read — nothing_found 21170, out_of_scope 18085, accepted 13433, blocked 8733, no_address 3010, service_not_seen 350, no_name 46, no_role_mailbox 5, timeout 5
- mailbox rows written by the cloud crawls (before the referee): **193302**

## 6. Delivered (last rank build on main)
- rows with a confirmed mailbox: **218124** — by tier: A 1225, B 1679, C 303, D 24403, E 4608, F 8, I 17822, L 427, M 9447, R 98530, T 59672
- named-vendor relationships (A B T M C D L): **97156** · registry contract R: **98530** · link only (E): **4608** · older / inferred (F I): **17830**
