# Cloud lanes — status from the files on main (2026-11-11 19:37 UTC)

## 1. Sites
- `.ca` domains of the archive index: **354248**
- `.ca` domains of the web graph + public list: **2485064**
- domains linking to a proven Canadian vendor / vetted portal: **766792**
- OpenStreetMap Canada sites: **73684**
- domains linking to Shopify (store candidates): **1323854**
- home pages read by the scan: **3824384** (ok 1956240, unreachable 1211177, robots 315105, blocked 192961, http_error 147851, not_html 1050); by detector: {'t1': 23, 't4': 455216, 't5': 3369145}
- detector 4 (readable pages: 1956225): **419521 print a role mailbox of the organisation (21.4 %)** — general 355233, role 61923, finance 1524, accounts_payable 302, supplier_payment 279, procurement 195, invoice_submission 65; printed address: none 1474159, CA 367179, US 100779, GB 11205, AU 2903
- `.ca` sites whose home page prints a role mailbox (registry candidates, tier R): **239141**

## 2. Vendors and providers checked live (their own site's address)
- 101371 domains: no_address 46276, unreachable 15397, CA 12374, US 6879, blocked 5519, robots 4931, CA-loc 4365, GB 2134

## 3. DNS lookups
- domains looked up in the cloud: **8836686**; on Shopify's storefront addresses: **2106725**; with a www alias: 762479

## 4. Relationship leads on file
- Mac era B/L dated record (payment, subaward, release): **10803**
- Mac era D/E listed on a Canadian vendor's page (client, member, dealer, sponsor): **52386**
- Mac era M member / regulated payer list: **2290**
- Mac era T vetted software service (store / portal): **5511**
- cloud D/E listed on a Canadian vendor's page (client, member, dealer, sponsor): **116860**
- cloud M accredited business (BBB) [bbb]: **3106**
- cloud M licence holder (the licensing body's own list of active licences) [lic]: **4334**
- cloud M licence holder (the licensing body's own list of active licences) [rbq]: **12947**
- cloud M member / regulated payer list: **13439**
- cloud M membership stated by the member: **1755**
- cloud T credit line on the buyer's site: **70776**
- cloud T provider in the buyer's DNS: **444766**
- cloud T vetted software service (store / portal): **2900**
- cloud T vetted software service (store / portal) [shards]: **38991**

## 5. Mailbox crawl
- lead sites read: **902604** (nothing_found 539906, found 236200, unreachable 81407, blocked 44241, timeout 758, error 92)
  - leads no longer on file (withdrawn by a stricter rule) and registry candidates: 354602 read, mailbox on 133660 (38 %), blocked 10742
  - T provider in the buyer's DNS: 340866 read, mailbox on 42864 (13 %), blocked 16903
  - D/E listed on a Canadian vendor's page (client, member, dealer, sponsor): 129290 read, mailbox on 32325 (25 %), blocked 13503
  - T credit line on the buyer's site: 57930 read, mailbox on 19949 (34 %), blocked 2065
  - M member / regulated payer list: 7570 read, mailbox on 3174 (42 %), blocked 238
  - M licence holder (the licensing body's own list of active licences) [rbq]: 6071 read, mailbox on 2806 (46 %), blocked 170
  - M accredited business (BBB) [bbb]: 2171 read, mailbox on 533 (25 %), blocked 257
  - B/L dated record (payment, subaward, release): 1572 read, mailbox on 192 (12 %), blocked 200
  - M membership stated by the member: 1148 read, mailbox on 345 (30 %), blocked 17
  - T vetted software service (store / portal): 1143 read, mailbox on 154 (13 %), blocked 145
  - M licence holder (the licensing body's own list of active licences) [lic]: 241 read, mailbox on 198 (82 %), blocked 1
- candidate sites (stores / portals) read: **170061**
  - absorb: 314 read — nothing_found 172, out_of_scope 65, no_address 42, accepted 14, unreachable 7, blocked 6, portal_not_its_own 4, no_name 4
  - amilia: 608 read — nothing_found 264, accepted 170, no_address 68, out_of_scope 47, portal_not_its_own 27, blocked 13, no_name 11, unreachable 8
  - benevity: 67 read — nothing_found 45, portal_not_its_own 7, out_of_scope 7, no_address 7, blocked 1
  - bibliocommons: 514 read — nothing_found 410, out_of_scope 43, accepted 20, no_address 17, unreachable 8, blocked 7, no_name 4, portal_not_its_own 3, error 2
  - checkfront: 649 read — nothing_found 338, no_address 154, accepted 65, portal_not_its_own 32, out_of_scope 31, blocked 12, no_name 10, unreachable 7
  - clubrunner: 207 read — blocked 203, nothing_found 3, accepted 1
  - coconut: 156 read — nothing_found 107, out_of_scope 19, accepted 12, no_address 10, unreachable 3, no_name 2, blocked 2, portal_not_its_own 1
  - commerce7: 1464 read — out_of_scope 580, nothing_found 571, no_address 219, accepted 79, unreachable 7, no_name 6, blocked 2
  - coveo: 299 read — nothing_found 257, unreachable 15, no_address 10, out_of_scope 8, accepted 6, no_name 1, timeout 1, blocked 1
  - crowdriff: 130 read — nothing_found 74, accepted 42, no_address 9, no_name 3, unreachable 1, blocked 1
  - d2l: 446 read — nothing_found 260, out_of_scope 53, blocked 39, accepted 34, no_address 23, unreachable 15, portal_not_its_own 11, no_name 11
  - docebo: 108 read — nothing_found 72, out_of_scope 18, no_address 14, accepted 2, blocked 1, portal_not_its_own 1
  - edsby: 196 read — nothing_found 144, accepted 16, blocked 13, portal_not_its_own 12, no_name 5, no_address 3, unreachable 3
  - escribe: 126 read — nothing_found 95, no_address 13, accepted 5, unreachable 4, out_of_scope 3, portal_not_its_own 3, blocked 3
  - gorendezvous: 777 read — nothing_found 461, accepted 139, no_address 82, portal_not_its_own 50, no_name 22, unreachable 14, blocked 9
  - jane: 21711 read — nothing_found 11756, accepted 4539, no_address 2238, portal_not_its_own 2049, blocked 516, no_name 393, unreachable 215, error 3, no_role_mailbox 2
  - jobber: 4883 read — nothing_found 3116, no_address 874, accepted 726, no_name 77, blocked 61, unreachable 28, error 1
  - jumptools: 368 read — nothing_found 346, unreachable 13, accepted 7, no_name 2
  - juvonno: 185 read — nothing_found 71, accepted 47, portal_not_its_own 32, no_name 15, no_address 14, unreachable 5, blocked 1
  - kev: 699 read — nothing_found 605, blocked 28, no_name 19, no_address 14, out_of_scope 11, accepted 8, unreachable 8, portal_not_its_own 6
  - lightspeed: 796 read — nothing_found 600, accepted 96, no_address 40, unreachable 24, blocked 20, no_name 15, out_of_scope 1
  - lightspeed_golf: 91 read — nothing_found 46, accepted 32, portal_not_its_own 6, no_name 3, unreachable 2, out_of_scope 1, blocked 1
  - myrealpage: 2666 read — nothing_found 2076, accepted 341, unreachable 122, no_name 83, no_address 38, blocked 5, no_role_mailbox 1
  - nicejob: 1250 read — nothing_found 695, accepted 309, no_address 175, no_name 57, blocked 11, unreachable 3
  - owlpractice: 518 read — nothing_found 274, portal_not_its_own 112, no_address 84, unreachable 29, no_name 16, blocked 3
  - rezgo: 148 read — nothing_found 66, no_address 56, accepted 18, portal_not_its_own 4, unreachable 3, no_name 1
  - shopify: 122045 read — nothing_found 41360, out_of_scope 35837, accepted 34452, blocked 6392, no_address 3147, service_not_seen 482, unreachable 313, no_name 41, no_role_mailbox 16, timeout 5
  - socast: 267 read — nothing_found 135, unreachable 123, accepted 6, no_address 3
  - thinkific: 2998 read — nothing_found 1568, no_address 522, out_of_scope 366, blocked 240, unreachable 145, accepted 136, no_name 21
  - touchbistro: 162 read — nothing_found 80, accepted 34, no_address 21, portal_not_its_own 13, unreachable 9, no_name 3, blocked 2
  - unbounce: 3966 read — nothing_found 2142, accepted 717, no_address 421, blocked 420, unreachable 167, no_name 95, out_of_scope 4
  - webrezpro: 277 read — portal_not_its_own 115, nothing_found 98, no_address 35, unreachable 15, accepted 7, no_name 6, blocked 1
  - wellnessliving: 886 read — nothing_found 380, accepted 290, no_address 96, unreachable 47, no_name 37, portal_not_its_own 29, blocked 7
  - wellnessliving_widget: 83 read — nothing_found 39, accepted 25, unreachable 10, no_address 7, no_name 1, blocked 1
- mailbox rows written by the cloud crawls (before the referee): **290688**

## 6. Delivered (last rank build on main)
- rows with a confirmed mailbox: **267934** — by tier: A 1224, B 1687, C 294, D 26527, E 5312, F 7, I 17451, L 420, M 13363, R 105619, T 96030
- named-vendor relationships (A B T M C D L): **139545** · registry contract R: **105619** · link only (E): **5312** · older / inferred (F I): **17458**
