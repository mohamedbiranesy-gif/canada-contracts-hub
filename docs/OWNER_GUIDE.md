# Owner's guide to the table (plain language)

*Kept current by lane `claude`. Last refreshed: 2026-11-13 23:20Z, from the table built at 22:10Z.*

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
