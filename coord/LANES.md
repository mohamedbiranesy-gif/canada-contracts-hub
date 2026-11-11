# Cloud lanes — status from the files on main (2026-11-11 14:02 UTC)

## 1. Sites
- `.ca` domains of the archive index: **354248**
- `.ca` domains of the web graph + public list: **2485064**
- domains linking to a proven Canadian vendor / vetted portal: **717414**
- OpenStreetMap Canada sites: **73684**
- domains linking to Shopify (store candidates): **1323839**
- home pages read by the scan: **3311464** (ok 1621610, unreachable 1199828, robots 231686, blocked 145099, http_error 112349, not_html 892); by detector: {'t1': 23, 't4': 1004123, 't5': 2307318}
- detector 4 (readable pages: 1621595): **354338 print a role mailbox of the organisation (21.9 %)** — general 301347, role 50924, finance 1353, accounts_payable 269, supplier_payment 231, procurement 159, invoice_submission 55; printed address: none 1196911, CA 324426, US 87812, GB 10122, AU 2324
- `.ca` sites whose home page prints a role mailbox (registry candidates, tier R): **191283**

## 2. Vendors and providers checked live (their own site's address)
- 97241 domains: no_address 44125, unreachable 15019, CA 12080, US 6389, blocked 5330, robots 4749, CA-loc 4136, GB 2033

## 3. DNS lookups
- domains looked up in the cloud: **8410207**; on Shopify's storefront addresses: **1746487**; with a www alias: 762479

## 4. Relationship leads on file
- Mac era B/L dated record (payment, subaward, release): **10803**
- Mac era D/E listed on a Canadian vendor's page (client, member, dealer, sponsor): **52386**
- Mac era M member / regulated payer list: **2290**
- Mac era T vetted software service (store / portal): **5511**
- cloud D/E listed on a Canadian vendor's page (client, member, dealer, sponsor): **116935**
- cloud M accredited business (BBB) [bbb]: **3106**
- cloud M licence holder (the licensing body's own list of active licences) [lic]: **4334**
- cloud M licence holder (the licensing body's own list of active licences) [rbq]: **11585**
- cloud M member / regulated payer list: **11210**
- cloud M membership stated by the member: **1650**
- cloud T credit line on the buyer's site: **66961**
- cloud T provider in the buyer's DNS: **377866**
- cloud T vetted software service (store / portal): **2900**
- cloud T vetted software service (store / portal) [shards]: **31735**

## 5. Mailbox crawl
- lead sites read: **785719** (nothing_found 473398, found 218263, unreachable 54344, blocked 38871, timeout 756, error 87)
  - leads no longer on file (withdrawn by a stricter rule) and registry candidates: 327819 read, mailbox on 126673 (39 %), blocked 10365
  - T provider in the buyer's DNS: 252199 read, mailbox on 32601 (13 %), blocked 12067
  - D/E listed on a Canadian vendor's page (client, member, dealer, sponsor): 129358 read, mailbox on 31974 (25 %), blocked 13422
  - T credit line on the buyer's site: 56885 read, mailbox on 19772 (35 %), blocked 2035
  - M member / regulated payer list: 7155 read, mailbox on 3085 (43 %), blocked 217
  - M licence holder (the licensing body's own list of active licences) [rbq]: 6071 read, mailbox on 2787 (46 %), blocked 169
  - M accredited business (BBB) [bbb]: 2170 read, mailbox on 531 (24 %), blocked 236
  - B/L dated record (payment, subaward, release): 1572 read, mailbox on 177 (11 %), blocked 199
  - T vetted software service (store / portal): 1143 read, mailbox on 148 (13 %), blocked 143
  - M membership stated by the member: 1123 read, mailbox on 341 (30 %), blocked 17
  - M licence holder (the licensing body's own list of active licences) [lic]: 224 read, mailbox on 174 (78 %), blocked 1
- candidate sites (stores / portals) read: **135205**
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
  - shopify: 108590 read — nothing_found 36528, out_of_scope 31337, accepted 30002, blocked 6955, no_address 3047, service_not_seen 461, unreachable 201, no_name 41, no_role_mailbox 13, timeout 5
  - thinkific: 126 read — nothing_found 126
  - unbounce: 324 read — nothing_found 204, blocked 108, accepted 6, out_of_scope 4, no_address 1, no_name 1
- mailbox rows written by the cloud crawls (before the referee): **264505**

## 6. Delivered (last rank build on main)
- rows with a confirmed mailbox: **241338** — by tier: A 1225, B 1679, C 295, D 26391, E 4965, F 7, I 17623, L 422, M 13327, R 99941, T 75463
- named-vendor relationships (A B T M C D L): **118802** · registry contract R: **99941** · link only (E): **4965** · older / inferred (F I): **17630**
