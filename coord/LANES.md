# Cloud lanes — status from the files on main (2026-11-11 04:48 UTC)

## 1. Sites
- `.ca` domains of the archive index: **354248**
- `.ca` domains of the web graph + public list: **2485064**
- domains linking to a proven Canadian vendor / vetted portal: **717414**
- OpenStreetMap Canada sites: **73684**
- domains linking to Shopify (store candidates): **1323839**
- home pages read by the scan: **3219198** (ok 1499669, unreachable 1284068, robots 200153, blocked 130261, http_error 104235, not_html 812); by detector: {'t1': 23, 't4': 2711726, 't5': 507449}
- detector 4 (readable pages: 1499654): **329114 print a role mailbox of the organisation (21.9 %)** — general 281881, role 45294, finance 1278, accounts_payable 255, supplier_payment 209, procurement 146, invoice_submission 51; printed address: none 1104514, CA 304377, US 79052, GB 9492, AU 2219
- `.ca` sites whose home page prints a role mailbox (registry candidates, tier R): **178390**

## 2. Vendors and providers checked live (their own site's address)
- 95104 domains: no_address 43073, unreachable 14784, CA 11980, US 6018, blocked 5240, robots 4636, CA-loc 4092, GB 1963

## 3. DNS lookups
- domains looked up in the cloud: **7540938**; on Shopify's storefront addresses: **1176424**; with a www alias: 701769

## 4. Relationship leads on file
- Mac era B/L dated record (payment, subaward, release): **10803**
- Mac era D/E listed on a Canadian vendor's page (client, member, dealer, sponsor): **52386**
- Mac era M member / regulated payer list: **2290**
- Mac era T vetted software service (store / portal): **5511**
- cloud D/E listed on a Canadian vendor's page (client, member, dealer, sponsor): **116929**
- cloud M accredited business (BBB) [bbb]: **3106**
- cloud M licence holder (the licensing body's own list of active licences) [lic]: **3806**
- cloud M licence holder (the licensing body's own list of active licences) [rbq]: **11585**
- cloud M member / regulated payer list: **10126**
- cloud M membership stated by the member: **1560**
- cloud T credit line on the buyer's site: **68280**
- cloud T provider in the buyer's DNS: **230033**
- cloud T vetted software service (store / portal): **2900**
- cloud T vetted software service (store / portal) [shards]: **20145**

## 5. Mailbox crawl
- lead sites read: **579122** (nothing_found 371871, found 177090, blocked 29511, timeout 579, error 71)
  - leads no longer on file (withdrawn by a stricter rule) and registry candidates: 272077 read, mailbox on 108347 (40 %), blocked 9178
  - D/E listed on a Canadian vendor's page (client, member, dealer, sponsor): 127948 read, mailbox on 30144 (24 %), blocked 12938
  - T provider in the buyer's DNS: 107230 read, mailbox on 14420 (13 %), blocked 4743
  - T credit line on the buyer's site: 57391 read, mailbox on 19062 (33 %), blocked 1904
  - M licence holder (the licensing body's own list of active licences) [rbq]: 6065 read, mailbox on 2741 (45 %), blocked 168
  - M member / regulated payer list: 3984 read, mailbox on 1413 (35 %), blocked 169
  - B/L dated record (payment, subaward, release): 1471 read, mailbox on 165 (11 %), blocked 193
  - T vetted software service (store / portal): 1083 read, mailbox on 140 (13 %), blocked 130
  - M membership stated by the member: 1016 read, mailbox on 299 (29 %), blocked 15
  - M accredited business (BBB) [bbb]: 633 read, mailbox on 188 (30 %), blocked 72
  - M licence holder (the licensing body's own list of active licences) [lic]: 224 read, mailbox on 171 (76 %), blocked 1
- candidate sites (stores / portals) read: **104073**
  - absorb: 130 read — nothing_found 72, out_of_scope 29, no_address 18, accepted 8, blocked 1, portal_not_its_own 1, no_name 1
  - amilia: 521 read — nothing_found 219, accepted 151, no_address 64, out_of_scope 42, portal_not_its_own 23, blocked 13, no_name 9
  - benevity: 21 read — nothing_found 15, portal_not_its_own 2, out_of_scope 2, blocked 1, no_address 1
  - bibliocommons: 264 read — nothing_found 203, out_of_scope 30, accepted 18, no_address 4, no_name 4, blocked 3, portal_not_its_own 1, error 1
  - coconut: 82 read — nothing_found 61, out_of_scope 9, accepted 7, no_address 3, portal_not_its_own 1, no_name 1
  - coveo: 190 read — nothing_found 170, no_address 9, out_of_scope 5, accepted 4, no_name 1, timeout 1
  - d2l: 278 read — nothing_found 160, out_of_scope 34, blocked 33, accepted 19, no_address 17, portal_not_its_own 11, no_name 4
  - docebo: 84 read — nothing_found 52, out_of_scope 16, no_address 13, accepted 2, blocked 1
  - edsby: 69 read — nothing_found 37, accepted 14, portal_not_its_own 9, no_name 4, blocked 3, no_address 2
  - escribe: 74 read — nothing_found 58, no_address 8, accepted 4, out_of_scope 2, portal_not_its_own 1, blocked 1
  - jane: 19116 read — nothing_found 10374, accepted 4120, no_address 1982, portal_not_its_own 1852, blocked 490, no_name 294, error 2, no_role_mailbox 2
  - jobber: 4617 read — nothing_found 2985, no_address 830, accepted 676, no_name 68, blocked 57, error 1
  - kev: 153 read — nothing_found 110, blocked 11, accepted 8, out_of_scope 8, no_name 6, no_address 5, portal_not_its_own 5
  - lightspeed: 565 read — nothing_found 466, accepted 51, no_address 29, blocked 10, no_name 8, out_of_scope 1
  - shopify: 77458 read — nothing_found 25445, out_of_scope 21789, accepted 18326, blocked 8426, no_address 3020, service_not_seen 396, no_name 46, no_role_mailbox 5, timeout 5
  - thinkific: 126 read — nothing_found 126
  - unbounce: 324 read — nothing_found 204, blocked 108, accepted 6, out_of_scope 4, no_address 1, no_name 1
- mailbox rows written by the cloud crawls (before the referee): **209238**

## 6. Delivered (last rank build on main)
- rows with a confirmed mailbox: **227774** — by tier: A 1225, B 1677, C 295, D 26717, E 4984, F 7, I 17816, L 423, M 11238, R 97211, T 66181
- named-vendor relationships (A B T M C D L): **107756** · registry contract R: **97211** · link only (E): **4984** · older / inferred (F I): **17823**
