# Owner's guide to the table (plain language)

*Kept current by lane `claude`. Last refreshed: 2026-11-14 04:10Z — the final corrected copy of the table built at 2026-11-13 22:10Z.*

## What it is
One row per organisation (the **buyer**) that a **Canadian biller** (the **vendor**) bills **on invoice**, payable **by bank transfer or cheque**,
with the organisation's own **role mailbox** (accounts payable, finance, purchasing, or its general mailbox when it publishes no other), re-read by the
referee. Every value says where it was read, and every estimate says that it is one and how it was calculated.

## Where it is
- The whole table: `ranked_buyers.csv.gz` on the release **ranked-latest**
  (https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/tag/ranked-latest). It is rebuilt every six hours.
- What changed between builds: `coord/results/ranked/SUMMARY.md` (counts), `CHANGELOG.md`.

## How to read a row
| Column | What it tells you |
|---|---|
| `ship_ready` | `yes` = every invoice field of its kind in the biller's or the record's own words; `yes (…)` = ready, and says what is by the kind of relationship, by where the organisation is, or not published; `no` = held back (`ship_ready_missing` says why) |
| `amount_mark` | 1 published $5,000+ · 2 estimated $5,000+ · 3 published under $5,000 · 4 estimated under $5,000 · 5 no amount. The table is sorted in that order |
| `buyer`, `buyer_address`, `email` | the organisation, its own printed address, its role mailbox (`email_evidence_url` is the page that prints it) |
| `vendor`, `vendor_address`, `vendor_tax_or_registration_number` | the Canadian biller, its printed address, its Business Number / GST-HST (derived, labelled) or its register number |
| `relationship_kind`, `relationship_fact_basis` | what ties them (a contract, a licence, a membership, an electricity account …) and why that is a fact |
| `recurring_billing`, `billing_cadence` | how often the bill comes |
| `bill_amount_indicative` / `bill_amount_calculated` | the published amount / the estimate (it starts with "estimated —" or "calculated —") |
| `bill_payment_method_as_published`, `bill_delivery_as_published`, `bill_due_terms_as_published` | how the bill is paid, how it arrives, when it is due — quoted |
| `payment_route` | "on invoice, by bank transfer / cheque", and whether that is in the biller's words or by the kind of relationship |

## The kinds of row (ready rows, table of 22:10Z)
- Electricity account by where the organisation is — 208,901: the distributor of its address bills electricity there every month; whose name is on the
  account is not published (the row says so). Ontario public bodies that report their own facilities' electricity (O. Reg. 25/23): 109, the account
  holder published.
- Services seen on the organisation's side (hosting and other invoiced services) — 30,765; memberships — 20,630; licences and registrations — 15,267;
  patent and trademark agents' clients — 12,891; sponsors and exhibitors — 5,209; public contracts — 3,095; dealers — 2,730; benefit plans — 784;
  stock-exchange listings — 348; tenants — 406; export sales — 49.

## The counts (table of 22:10Z)
- Ready rows: **301,184** of 362,875. Every main invoice field filled: 223,207. Amount and billing period: 267,672.
- $5,000+ a bill, ready: **2,873** (2,149 published, 724 estimated). Held back at $5,000+: 1,824 (956 no mailbox, 732 contract not shown current).

## What is never in it
A named person's mailbox; a guessed address; a card-on-file bill (owner's rule, 11 Nov); a company abroad that a Canadian company owns (except the
electric utilities of rule 18); households; anything behind a login or a bot check.

## The final corrected copy (2026-11-14) — use this one
- **On your Mac:** `Desktop/canada-contracts-hub-final/ranked_buyers_CORRECTED_2026-11-14.csv.gz` — the table of 22:10Z with every correction applied
  row by row (GitHub could not rebuild it). Beside it: `corrections.csv.gz` (every changed cell, before and after), `counts.json` (every correction
  counted), `folded_rows.csv` and `duplicate_buyers_dropped.csv` (second rows of one organisation taken out), and `HANDOFF_ROWS.md` — the full handoff
  for whoever picks this up: every column, every kind of relationship, where each fact comes from, amounts, payment, identifiers, limits. The original
  of 22:10Z is there too. The file was checked on your Mac after the copy (same fingerprint as here, and it opens).
- **The counts:** 362,833 rows; **298,247 ready** (was 301,184); $5,000 or more a bill: 2,895 ready rows (2,152 published, 743 estimated). Every main
  invoice field on 221,557 ready rows; an amount and a billing period on 265,143.
- **What changed, in plain words:** 4,466 organisation names cleaned (page-title words, addresses, phone numbers, slogans taken out); 920 wrong legal
  names of billers cleared; 923 addresses that were not the organisation's taken out (Google's, Shopify's head office printed on store pages, a
  template's "123 Main Street"); 2,944 rows taken out of the ready set — 2,131 domains that only sit on Web Hosting Canada's parking servers (no
  hosting is billed there, in WHC's own words), 382 billers that are U.S. companies (336 of them Marketplace Events' show exhibitors), about 290
  rows whose mailbox or site belonged to another country's office or to a namesake (Deloitte & Touche of Virginia with Deloitte Belgium's mailbox;
  the U.S. Treasury with the Australian Treasury's), the stores "located" at Shopify's Ottawa office, five mailboxes of named people; 19 rows became
  ready with mailboxes checked before Actions stopped.
- **What is still not perfect (handoff section 13):** rows by location (69% of the ready rows) do not name the account holder and mostly carry a small
  office's estimate; a few hundred names are a page's words rather than a name; contract values are as the source publishes them; the Marketplace
  Events exhibitors come back if you count that company as Canadian.
- **Everything is stopped:** no workflow runs or restarts by itself (`coord/ACTIONS_PAUSED`); the ChatGPT automation on your Mac was already paused
  and Gemini had no schedule. To restart anything: revert that one commit, and bring the crawlers back far slower.

## Right now: GitHub has switched Actions off on your account (since 2026-11-13 23:39Z)
- Nothing builds, crawls, checks or publishes until GitHub turns it back on. Only GitHub Support can do that (a ticket from your account).
- The table on the release **ranked-latest** (built 22:10Z) stays downloadable and is the current deliverable.
- The corrections below are saved in the repository and go into the first build after Actions returns. Until then, the 22:10Z table still has
  these rows (counted on it, with the new rules replayed row by row): about 380 ready rows whose biller is a U.S. legal entity (rule 19) — 336 of
  them exhibitors and sponsors of Marketplace Events' home and trade shows (the company is "Marketplace Events LLC", a U.S. company with offices in
  Canada; the rule can be lifted for it if you read it otherwise), the rest public contracts with "FieldTurf USA", "New Flyer of America" and the
  like; 39 rows where the postal code is in another province than the one printed (the electricity distributor is not certain); 36 foundations
  listed as sponsors (a grant, not an invoice); about 660 buyer names that are not names (75 image file names, 480 with the page word "Home",
  104 one trade word like "Accounting"); 3 buyers that appear twice; 989 Québec electrical and plumbing contractors whose yearly bill shows only
  the licence fee, without the CMEQ's or the CMMTQ's own dues; about 2,900 biller legal names read off a website that are not legal names
  ("Voice over Internet Protocol" for an Internet provider).
- When Actions returns, the first thing to run is the table build (rank-buyers); it takes about two hours.

