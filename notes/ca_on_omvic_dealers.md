# ca_on_omvic_dealers — OMVIC's public register of motor vehicle dealers (Ontario)

Engine: `tools/authority_registers.py` (entry `omvic` of `AUTH`), workflow `.github/workflows/authority-registers.yml` (daily, cloud only).
Not a contract source: a **register of a delegated authority**. A registered dealer pays the Council to be and to stay registered and a
fee on every vehicle it sells — the relationship is current, dated and published by the body that is paid.

## What was read (2026-11-11, from the container and a runner; robots.txt allows every address below)
- The Council's address: "Office: 65 Overlea Blvd. Suite 300 Toronto, ON M4H 1P1" (https://www.omvic.ca/contact).
- The fee: "As part of the transaction fee program, dealers must submit a $22.00 fee per vehicle for sales, leases, fleets, or as-is
  transactions, which is to be submitted with the registration renewal and fee." (https://www.omvic.ca/selling/fees/transaction-fees/)
- The search behind https://www.omvic.ca/dealer-search/: `GET /wp-admin/admin-ajax.php?action=searchDealerListAjax&dealershipName=<letters>
  &dealershipCity=&dealershipRegNumber=&activeRegistrationsOnly=true&disciplinaryActionOnly=false` → JSON, `data.dealers[]` = `id,
  legal_name, business_name, status, reason, reg_number, city`. No login, no CAPTCHA. It returns every name that CONTAINS the letters, in
  one answer, **5,000 at most**, and now and then an empty answer (the page itself asks again).
- A registrant's page: `/dealer-search/dealership-profile/?entry-id=<id>` — Legal Name, Business Phone, Website (or N/A), Legal Type,
  Business Fax, Email (hidden behind Cloudflare's obfuscation: never read), Address, Dealer Class and Sub-Class, Registration Status,
  Original Registration Date, Registration Expiry Date; then its salespeople and branches (not read).

## Counts (first pull, 2026-11-11)
| | |
|---|---|
| registered dealers in the register's answers | **7,865** (347 questions: 36 single characters, 11 of them at the 5,000 limit — a c e i l n o r s t u — asked again in pairs, 9 pairs in threes). Letters alone gave 6,888: the split found 977 more |
| profiles read in the test | 60: all corporations in the sample; 20 name a website (33 %) |
| sites the register names, checked (19) | 6 tied by the telephone number, 8 showed neither telephone nor postal code (the test still lacked the addresses: a parser fault, fixed), 3 robots, 2 refused (403) |

## Rules
- Legal persons only (`Legal Type` corporation / partnership); a sole proprietor is a natural person and is left out.
- The site is the one the register's own `Website` field names; kept only when its home page shows the registrant's telephone number
  (as text or as the page's call link) or postal code. A site named by more than three registrants is a group's site: left out.
- The row: buyer = the dealer (business name; the legal name goes to the bill-to legal name with the register as its source), vendor = the
  Council, reference = the registration number, start = first registration, end = expiry date — a dated, ongoing relationship (rule 3).
- Not done yet: the 67 % of dealers whose entry names no website (to be tied to the site facts on file by telephone / postal code,
  as `tools/biz_licences.py` does for city licences).
