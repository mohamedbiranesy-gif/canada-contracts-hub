# Cloud lanes — status from the files on main (2026-11-12 21:16 UTC)

## 1. Sites
- `.ca` domains of the archive index: **354248**
- `.ca` domains of the web graph + public list: **2485064**
- domains linking to a proven Canadian vendor / vetted portal: **772302**
- OpenStreetMap Canada sites: **73684**
- domains linking to Shopify (store candidates): **1323855**
- home pages read by the scan: **4667297** (ok 2273868, unreachable 1382615, robots 599440, blocked 222919, http_error 187271, not_html 1184); by detector: {'t1': 23, 't4': 455161, 't5': 4212113}
- detector 4 (readable pages: 2273853): **478578 print a role mailbox of the organisation (21.0 %)** — general 405568, role 70374, finance 1683, supplier_payment 338, accounts_payable 318, procurement 222, invoice_submission 75; printed address: none 1740220, CA 412604, US 106379, GB 11702, AU 2948
- `.ca` sites whose home page prints a role mailbox (registry candidates, tier R): **291046**

## 2. Vendors and providers checked live (their own site's address)
- 103850 domains: no_address 47605, unreachable 15656, CA 12600, US 7057, blocked 5643, robots 5037, CA-loc 4528, GB 2158

## 3. DNS lookups
- domains looked up in the cloud: **10423780**; on Shopify's storefront addresses: **3488446**; with a www alias: 762479

## 4. Relationship leads on file
- Mac era B/L dated record (payment, subaward, release): **10803**
- Mac era D/E listed on a Canadian vendor's page (client, member, dealer, sponsor): **52386**
- Mac era M member / regulated payer list: **2290**
- Mac era T vetted software service (store / portal): **5511**
- cloud D/E listed on a Canadian vendor's page (client, member, dealer, sponsor): **150988**
- cloud M accredited business (BBB) [bbb]: **3106**
- cloud M licence holder (the licensing body's own list of active licences): **3760**
- cloud M licence holder (the licensing body's own list of active licences) [lic]: **9892**
- cloud M licence holder (the licensing body's own list of active licences) [rbq]: **13859**
- cloud M member / regulated payer list: **27758**
- cloud M membership stated by the member: **1875**
- cloud T credit line on the buyer's site: **74399**
- cloud T provider in the buyer's DNS: **627232**
- cloud T vetted software service (store / portal): **2900**
- cloud T vetted software service (store / portal) [shards]: **38991**

## 5. Mailbox crawl
- lead sites read: **2340772** (nothing_found 1599494, found 439117, unreachable 213810, blocked 74992, timeout 13145, error 214)
  - leads no longer on file (withdrawn by a stricter rule) and registry candidates: 1477114 read, mailbox on 289371 (20 %), blocked 27193
  - T provider in the buyer's DNS: 605385 read, mailbox on 74300 (12 %), blocked 28055
  - D/E listed on a Canadian vendor's page (client, member, dealer, sponsor): 152709 read, mailbox on 38499 (25 %), blocked 15851
  - T credit line on the buyer's site: 65665 read, mailbox on 22100 (34 %), blocked 2313
  - M member / regulated payer list: 21616 read, mailbox on 9507 (44 %), blocked 586
  - M licence holder (the licensing body's own list of active licences) [rbq]: 7725 read, mailbox on 3081 (40 %), blocked 219
  - M licence holder (the licensing body's own list of active licences) [lic]: 3436 read, mailbox on 768 (22 %), blocked 46
  - M accredited business (BBB) [bbb]: 2205 read, mailbox on 543 (25 %), blocked 303
  - B/L dated record (payment, subaward, release): 1593 read, mailbox on 223 (14 %), blocked 200
  - M membership stated by the member: 1298 read, mailbox on 373 (29 %), blocked 19
  - T vetted software service (store / portal): 1152 read, mailbox on 176 (15 %), blocked 147
  - M licence holder (the licensing body's own list of active licences): 874 read, mailbox on 176 (20 %), blocked 60
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
- mailbox rows written by the cloud crawls (before the referee): **501845**

## 6. Delivered (last rank build on main)
- rows with a confirmed mailbox: **272917** — by tier: A 1217, B 1722, C 277, D 30196, E 4186, F 10, I 152628, L 423, M 22224, T 60034
- named-vendor relationships (A B T M C D L): **116093** · registry contract R: **0** · link only (E): **4186** · older / inferred (F I): **152638**
