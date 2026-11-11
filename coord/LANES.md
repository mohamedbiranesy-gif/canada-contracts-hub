# Cloud lanes — status from the files on main (2026-11-11 08:26 UTC)

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
- domains looked up in the cloud: **7815352**; on Shopify's storefront addresses: **1379996**; with a www alias: 706516

## 4. Relationship leads on file
- Mac era B/L dated record (payment, subaward, release): **10803**
- Mac era D/E listed on a Canadian vendor's page (client, member, dealer, sponsor): **52386**
- Mac era M member / regulated payer list: **2290**
- Mac era T vetted software service (store / portal): **5511**
- cloud D/E listed on a Canadian vendor's page (client, member, dealer, sponsor): **116969**
- cloud M accredited business (BBB) [bbb]: **3106**
- cloud M licence holder (the licensing body's own list of active licences) [lic]: **3806**
- cloud M licence holder (the licensing body's own list of active licences) [rbq]: **11585**
- cloud M member / regulated payer list: **10126**
- cloud M membership stated by the member: **1560**
- cloud T credit line on the buyer's site: **68280**
- cloud T provider in the buyer's DNS: **230033**
- cloud T vetted software service (store / portal): **2900**
- cloud T vetted software service (store / portal) [shards]: **23325**

## 5. Mailbox crawl
- lead sites read: **633383** (nothing_found 420822, found 181127, blocked 30779, timeout 581, error 74)
  - leads no longer on file (withdrawn by a stricter rule) and registry candidates: 320040 read, mailbox on 110333 (34 %), blocked 10065
  - D/E listed on a Canadian vendor's page (client, member, dealer, sponsor): 129375 read, mailbox on 30225 (23 %), blocked 13104
  - T provider in the buyer's DNS: 107230 read, mailbox on 14420 (13 %), blocked 4743
  - T credit line on the buyer's site: 57391 read, mailbox on 19062 (33 %), blocked 1904
  - M member / regulated payer list: 7155 read, mailbox on 3041 (43 %), blocked 216
  - M licence holder (the licensing body's own list of active licences) [rbq]: 6071 read, mailbox on 2741 (45 %), blocked 169
  - M accredited business (BBB) [bbb]: 2168 read, mailbox on 524 (24 %), blocked 222
  - B/L dated record (payment, subaward, release): 1571 read, mailbox on 168 (11 %), blocked 198
  - T vetted software service (store / portal): 1142 read, mailbox on 143 (13 %), blocked 142
  - M membership stated by the member: 1016 read, mailbox on 299 (29 %), blocked 15
  - M licence holder (the licensing body's own list of active licences) [lic]: 224 read, mailbox on 171 (76 %), blocked 1
- candidate sites (stores / portals) read: **113746**
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
  - shopify: 87131 read — nothing_found 28917, out_of_scope 24983, accepted 21519, blocked 8205, no_address 3046, service_not_seen 406, no_name 44, no_role_mailbox 6, timeout 5
  - thinkific: 126 read — nothing_found 126
  - unbounce: 324 read — nothing_found 204, blocked 108, accepted 6, out_of_scope 4, no_address 1, no_name 1
- mailbox rows written by the cloud crawls (before the referee): **216702**

## 6. Delivered (last rank build on main)
- rows with a confirmed mailbox: **232536** — by tier: A 1225, B 1678, C 295, D 26727, E 5034, F 7, I 18028, L 424, M 13127, R 98583, T 67408
- named-vendor relationships (A B T M C D L): **110884** · registry contract R: **98583** · link only (E): **5034** · older / inferred (F I): **18035**
