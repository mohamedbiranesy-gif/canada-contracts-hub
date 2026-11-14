# Handoff — the final table of Canada Contracts Hub, row by row

*Written by lane `claude` on <!--DATE-->, for whoever (human or AI) picks this up next. Generated from the corrected table by
`contrib/claude/final_correction/handoff.py`; the numbers in it are counted on that table, not remembered.*

---

## 0. Read this first

**The project is stopped.** The owner ended it on 2026-11-13 at 20:51 EST ("pull the plug"), after GitHub disabled Actions for the account at
23:39Z. Every workflow timer is commented out and no workflow starts another while `coord/ACTIONS_PAUSED` exists (see that file). Do not restart
anything without the owner's word. If GitHub turns Actions back on and the owner wants one last build, run `rank-buyers` by hand once.

**The deliverable** is one table: one row per organisation (the *buyer*) that a Canadian biller (the *vendor*) bills on invoice, payable by bank
transfer or cheque, with the organisation's own role mailbox. Two copies exist:

| copy | where | what it is |
|---|---|---|
| original | release `ranked-latest` on GitHub (`ranked_buyers.csv.gz`, build 2026-11-13 22:10Z), and on the owner's Mac: `~/Desktop/canada-contracts-hub-final/ranked_buyers_ORIGINAL_2026-11-13_2210Z.csv.gz` | the last table a build made |
| **corrected (use this one)** | the owner's Mac: `~/Desktop/canada-contracts-hub-final/ranked_buyers_CORRECTED_2026-11-14.csv.gz`, with `corrections.csv.gz` (every changed cell, before → after) and `folded_rows.csv` / `duplicate_buyers_dropped.csv` (rows taken out as a second row of one buyer), `counts.json` (every correction counted) and this handoff as `HANDOFF_ROWS.md` | the original with every correction written after the last build applied, row by row (section 12) |

Regenerate the corrected copy from the original at any time (about 25 minutes on two cores; 7 GB of memory is enough):

```
python3 contrib/claude/final_correction/correct_table.py correct ranked_buyers.csv.gz OUT
python3 tools/priority_sort.py OUT
python3 contrib/claude/final_correction/correct_table.py fold OUT
```

**Headline counts of the corrected table** (<!--ROWS--> rows):

<!--HEADLINE-->

---

## 1. What a row is

A row is a **buyer** — one organisation, never twice (owner, 2026-11-11 20:36 EST: "no buyer twice is hard rule") — and **one current
relationship** in which a **Canadian biller** sends that buyer **a bill on invoice** that can be **paid by bank transfer or cheque**, plus the
buyer's own **role mailbox** where the bill can be sent. Everything else on the row is what an invoice of that relationship carries, populated as
far as anything published allows, each value with the page it was read on.

Four things make a row ready (`ship_ready` starts with `yes`), the owner's rule 13 (2026-11-11 16:01 EST: "invoice bank eft email Canadian vendor"):

1. **A Canadian biller with a relationship that is a fact and current.** The vendor is in Canada by the source's own vendor country or address
   field, never by its name (AGENTS.md §2.1). "A fact" is defined by the owner's rule 1: something whose being there means the relationship
   exists — a contract award, a register entry, a roster the biller publishes, a service seen running on the buyer's side, the distributor that
   by law serves the buyer's address. A vendor's client list is the vendor's statement and does not count alone.
2. **A bill on invoice.** A bill charged to a card on file (a Shopify store, self-serve software, most hosting plans) or paid through a go-between
   (a `.ca` name through its registrar) makes no row (owner's rule 6, 2026-11-11 13:09 EST: "if it's not on invoice, by bank transfer then it's
   no"). These rows were removed from the table.
3. **A bank payment** — bank transfer, cheque, pre-authorised debit, online banking bill payment — published by the biller, or inherent to the
   kind of relationship (section 6).
4. **The organisation's own role mailbox**, printed on its own pages and re-read by the referee (the `verify-and-merge` workflow re-fetched the
   page and found the address on it). Never a named person's mailbox, never webmail, never an address built from a pattern (§2.5). When the
   organisation publishes no invoicing mailbox, its purchasing mailbox, then its general mailbox (info@, reception@, greffe@) is used and labelled
   (owner, 2026-10-28; rule 9).

And two fields must be there: the biller's own printed address (it is what puts the biller in Canada) and, for a row that stands on where the
organisation is, the organisation's own address. Every other field of the row's kind that nothing published fills is **named** on the row
(`invoice_fields_missing_for_kind`) and does not take the row out; the row sorts below complete ones.

`ship_ready` reads:
- `yes` — every field of its kind, in the biller's or the record's own words;
- `yes (…)` — ready, and the bracket says what is by the kind of relationship, by where the organisation is, calculated, or not published;
- `no` — held back; `ship_ready_missing` gives every reason.

**Order of the table** (owner, 2026-11-11 20:36 EST: "mark everything, prioritise over 5000"): ready rows first, then the rest; inside each, by
`amount_mark` 1 to 5 (section 5); inside a class, the ranker's own order (the stronger relationship and the better mailbox first).

---

## 2. Files

| path | what |
|---|---|
| release `ranked-latest` | `ranked_buyers.csv.gz` (the table), `ranked_buyers.jsonl.gz` (the same rows as JSON lines), the packages (`P01…P15`, one row per buyer in the best package it qualifies for, by mailbox type and relationship), `BUILD.json` |
| release `dataset-latest` | the contract dataset behind the public-contract rows (`canadian_vendor_contracts.jsonl.gz`), vendors and buyers enriched |
| `coord/results/ranked/` | the build's reports: `SUMMARY.md` (counters of every rule), `AUDIT.md` (28 checks), `VALIDATION.md`, `CHANGELOG.md`, `COVERAGE_VS_TARGETS.md` |
| `contrib/claude/rank_buyers/rank.py` | the ranker: every row is made here (≈7,300 lines; read the comments, they carry the reasons and the owner's words) |
| `tools/relationship_rows.py` | the owner's test (`owner_test`), the kinds (`kind_of`, `FIELDS`, `BY_KIND`), payment route, amount marks, estimates |
| `tools/by_location.py`, `tools/bps_energy.py`, `tools/muni_energy.py`, `tools/abroad_utilities.py` | the electricity distributors by address; Ontario public bodies' own energy reports; municipalities' bills from their residents; utilities abroad owned by Canadian companies (rule 18) |
| `tools/payee_billing.py` + `tools/data/payees/*.json` | how the bodies behind registers, rosters and licences bill and take payment, each sentence read on their own page (verified by `payee_billing.py verify`) |
| `tools/tech_relationships.py`, `tools/vendor_billing.py` | service rows: what is seen on the buyer's side; the vendors' own price and terms pages |
| `tools/replay_owner_test.py` | measure a change to the owner's test on a built table before any build uses it |
| `contrib/claude/final_correction/` | the final correction (this handoff's table) and this handoff's generator |
| `AGENTS.md` | the contract every agent follows: the mission, the owner's rules 1–20, the hard rules §2 — read it whole |
| `STATE.md`, `coord/DECISIONS.md`, `CHECKS.json`, `docs/OWNER_GUIDE.md`, `docs/ROUTE_TO_1M.md` | state, decisions with reasons, checks, the owner's plain-language guide, the route to the goal |

---

## 3. Every column

The table has <!--NCOLS--> columns. Fill = share of the ready rows of the corrected table where the column is not empty (and not `not_published`).

<!--COLUMNS-->

---

## 4. The kinds of relationship — what each row stands on, how deep it is, where it comes from

`invoice_fields_for_kind` names the kind and the fields an invoice of that kind carries; `relationship_kind` says it in words,
`relationship_fact_basis` says why it is a fact (or that it is not), `how_relationship_was_found` names the tool and the source, `contract_status`
says why it is current, `contract_link` / `source` point to the record.

**Depth, from strongest to weakest:**
1. **A record of the relationship itself, dated and current** — a public contract with a published end date (tier A) or awarded in the last 12
   months (B), an Ontario public body's own energy report (own report), an import declaration with the exporter's invoice number (export sale), a
   Form 5500 schedule naming the insurer and the policy (benefit plan).
2. **The biller's own current list** — a register of licences or registrations, the patent and trademark registers naming the agent of record, a
   stock exchange's list of issuers, a chamber's or association's member directory, a sponsor or exhibitor list, a dealer locator, a tenant
   directory (tier M and the rosters): current by construction (a lapsed member leaves the directory), but the amount billed to this buyer is not
   published.
3. **Seen on the buyer's side** — the buyer's own DNS records or site run on the vendor's service (tier T): the service is running today; who holds
   the account is normally the organisation, sometimes its web agency.
4. **By where the organisation is** — the distributor that by law bills electricity at the organisation's own printed address (tier I, rule 13
   since 2026-11-11 16:01 EST): the biller is certain for the address; whose name is on the account is not published, and every such row says so.

<!--KINDS-->

---

## 5. Amounts — published first, estimates labelled

Owner's rules 3 and 16: a published amount first; a calculated value only from published figures, saying so and saying from what
(`bill_amount_calculated` starts with `estimated —` or `calculated —`); never an estimate in a published cell; where nothing published supports
one, the cell says not published.

| column | holds |
|---|---|
| `contract_value` | the record's published value (a contract's total, a licence's fee paid, an import's FOB value), with its source field |
| `bill_amount_indicative` | a published amount of one bill (a fee in the biller's own table, a price list's lowest plan, the dues the body prints) |
| `bill_amount_basis` | the sentence or table line it was read in, the page and the day |
| `bill_amount_calculated` | the estimate or the calculation, labelled, with every figure it rests on |
| `amount_mark` | the class of the row's amount, and the figure it rests on: **1** published, $5,000 or more a bill · **2** estimated, $5,000 or more · **3** published, under $5,000 · **4** estimated, under $5,000 · **5** no amount (owner, 2026-11-11 20:36 EST: $5,000 a bill is a priority, not a wall) |

How each estimate is made (the code is the reference; these are its rules):

| kind | method |
|---|---|
| public contract | the contract's value spread over its own term (start to end) when both are published (`calculated —`); otherwise over the buyer's average contract term in the dataset, only when the buyer has at least 5 contracts and a plausible median (≤ $2 million) (`estimated —`); a framework, standing offer or multiple-award ceiling is never a bill (`5 no amount`) |
| utility account by location | the distributor's own published rates (fixed charge + energy price, read on its rate page) at a small office's use, 2,500 kWh a month — a floor for most organisations (`estimated —`) |
| municipality outside Ontario (by location) | its residents (Statistics Canada 2021 Census, table 98-10-0002-01) × the kWh a resident a year that Ontario municipalities of its size report under O. Reg. 25/23 (lower quartile for the mark, median beside it) × Hydro-Québec's 2025 price comparison for the province's city, the lower of its 10,000 and 100,000 kWh prices (`tools/muni_energy.py`); street lighting is not in the reports, so it is a floor |
| utility account by own report | each facility's reported grid electricity (Ontario BPS energy reports, O. Reg. 25/23) priced at its distributor's small-business rates (OEB file of current rates) or Hydro-Québec's comparison at its consumption level, summed by month |
| licence or registration | the body's own fee table for the licence's kind (RBQ, RACJ, CIPO, ISED spectrum, Health Canada …) or the fee the open data says was paid (Vancouver `feepaid`); a register with several types takes the schedule's own rule (`tools/payee_fees.py`) |
| agent of record | CIPO's official 2026 fees the agent advances and bills: at least $595.06 per trademark renewal (first class), at least $60.26 per patent maintenance fee (small entity) — the agent's own fee comes on top and is not published |
| membership | the body's lowest published membership fee (the member's own dues are that or more); a benefit's price or value, a discount, an individual's fee is not the dues |
| benefit plan contract | Form 5500 Schedule A: premiums received ÷ 12, or more than the commissions paid out of the premium ÷ 12 |
| export sale | Colombia's DIAN import declaration: the FOB value of the newest invoice, and the totals with this exporter |
| CMEQ / CMMTQ licences | the corporation's own yearly dues and the yearly fee to keep the licence, each published; their sum in `bill_amount_calculated` |
| service seen on the buyer's side | the vendor's lowest published price by the month or the year for the product seen (never a mailbox price for a DNS zone) |

---

## 6. How the bill comes and how it is paid

`payment_route` (and `payment_route_basis`, which quotes):
- `on invoice, by bank transfer / cheque` — the biller's own words name a bank payment;
- `on invoice; bank payment or card (the biller takes both)` — in; a card accepted beside a bank payment does not take the row out (owner, 13:58 EST: "In");
- `on invoice, by bank transfer / cheque — by the kind of relationship (the biller's own words were not found)` — the biller publishes nothing on
  it; the row says how a bill of that kind is billed and paid (below) and that it is by the kind (rule 13);
- `card on file, charged by the vendor`, `through the registrar of record`, `no invoice is sent …` — never ready (those rows were removed).

By the kind of relationship (`tools/relationship_rows.py BY_KIND`), used only where the biller's own sentence was not found:

<!--BYKIND-->

A biller's own sentence always wins: "card only" takes the row out, "we send no invoice" fails it. Never used for hosting or software, where the
common way is a card on file. The bodies with thousands of rows (the Régie du bâtiment du Québec, the cities of Calgary, Edmonton, Toronto, CIPO,
chambers …) were read by hand: `tools/payee_billing.py` and `tools/data/payees/*.json`, every sentence quoted with its page and day, and an entry is
used only after `payee_billing.py verify` found every quote on the page.

Bill columns: `bill_delivery_as_published` (how the bill reaches the payer), `bill_payment_method_as_published`, `bill_due_terms_as_published`
(when it is due), `service_stops_if_unpaid`, `bill_remit_to_as_published` (where a cheque goes), `bill_tax_rule_as_published`,
`bill_currency_as_published`, `bill_identifier_format` (the number an invoice carries), `bill_items_as_published` (what is billed),
`recurring_billing` (1 monthly · 2 quarterly · 3 yearly or longer · 4 per project / per order …) with `recurring_billing_basis` and `billing_cadence`.

---

## 7. The invoice a vendor could send

Each row with a mailbox carries a draft invoice header (`invoice_text`) and the same as structured data (`invoice_card_json`):

```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: <buyer legal name, or its name> — <address> — buyer tax no. <BN if published>
SUBMIT TO: <mailbox> (<type> mailbox, confirmed by the referee) | portal …
REFERENCE: <PO / contract / tender / vendor id> | PO rule: …
FROM / REMIT TO: <vendor legal name> — <remit address> | GST/HST <BN9>RT0001 (derived) …
TAX: <buyer's tax status, derived and labelled> | CURRENCY: … | TERMS: …
DESCRIPTION: <what is billed> | AMOUNT: …
```

`invoice_card_json` keys: `bill_to` (legal_name, legal_name_is_published, trade_name, address, tax_number, language), `submit_to` (email,
email_type, supplier_setup_url, portal_url, format, system, e_invoicing_peppol, portal_is_invoice_channel, portal_class), `references_required`
(po_required, po_number, contract_or_agreement_number, vendor_id_with_buyer, reference_hint), `terms`, `tax`, `vendor_identity` (legal_name, bn9,
neq, remit_address …), `follow_up`. Around them: `invoice_readiness` (n/14 elements present) and `invoice_missing`, `pay_on_sight` (could an
invoice made from the row clear AP matching), `channel_tier` (1 invoicing/AP mailbox or invoice portal · 2 finance · 3 purchasing/general · 0
unconfirmed), `ap_grade` A–E with `ap_score`, `ap_grade_basis`, `ap_gap_to_A`, `ap_payability`.

The fields an invoice of each kind carries (`tools/relationship_rows.py FIELDS`):

<!--FIELDS-->

---

## 8. Identifiers

| identifier | columns | rule |
|---|---|---|
| Business Number (9 digits) | `vendor_bn9`, `buyer_bn_as_published` | as published (registry, the CRA charities list, the federal grants disclosure, the organisation's own page) |
| GST/HST number | `vendor_gst_hst_derived`, `buyer_gst_hst_derived` | **derived**: BN9 + `RT0001`, always labelled derived — never published as such, never looked up in the CRA registry (CAPTCHA, §2.6) |
| Québec NEQ / QST | `vendor_neq`, `vendor_qst_as_published` | the Registraire des entreprises; QST only as printed |
| register entries | `vendor_registry_id`, `vendor_registry_url`, `vendor_registered_address`, `vendor_legal_form`, `vendor_incorporation_date`, `vendor_registry_status`, `buyer_registry_id` | Canada's Business Registries, Corporations Canada, REQ, BC OrgBook — matched by name; a partnership and a corporation of the same name are never matched |
| when the GST/HST is not public | `vendor_tax_or_registration_number` | the home register's number (NEQ, corporation number) fills the vendor's number, labelled as such (rule 11) |
| relationship references | `contract_reference`, `po_number_as_published`, `contract_or_agreement_number`, `solicitation_or_tender_number`, `award_or_notice_id`, `buyer_vendor_id`, `all_identifiers`, `po_or_reference_to_quote`, `invoice_reference_hint` | the record's own numbers; a licence, patent, trademark or policy number for the other kinds |
| others | `peppol_participant_id`, `vendor_peppol_id`, `buyer_wikidata`, `vendor_wikidata`, `org_group_key`, `keys` | `keys` are the buyer's keys in the pipeline (b:…, lead:…) |

---

## 9. Mailboxes

`email` is the organisation's own role mailbox; `email_type` its role (invoicing/AP · finance/accounting dept or supplier-payment office ·
purchasing · general); `email_check` how it was confirmed (`confirmed` = the referee re-fetched the page and found it; `cross_verified` = two
lanes quoted it from the same page); `email_evidence_url` and `email_evidence_quote` (≤ 300 characters containing the address) are the proof;
`mailbox_provenance` says who found it and how. Rules that keep a mailbox off the row: a named person's, webmail (gmail, outlook …), a hidden
form field only, a regional office's mailbox of a multinational on a body elsewhere, a mail domain that is not the buyer's own when the page does
not name the body, a recruitment / privacy / donations / media box. `email_deliverability`, `email_security_posture`, `dmarc_policy`,
`spf_policy`, `mail_provider`, `mta_sts`, `tls_rpt`, `bimi` describe the mail domain (DNS only). ISP-hosted municipal mailboxes (videotron.ca,
bellnet.ca) stay, labelled `mail_provider = ISP mail` (decision of 2026-11-04).

The corrected copy also takes off (section 12): the mailboxes of named persons that reached the table (`cindy.accounting@…`, `jen.accounting@…`);
a mailbox on another country's domain than both the organisation's site and its address (an affiliate's abroad — Deloitte & Touche LLP of Virginia
with `deloitte.be`, Hertz in Toronto with `hertz.nl` — or a namesake's); the site and mailbox of a namesake matched by name. A mailbox whose own page
says it is for queries only keeps its place under its true role (Durham University's AP mailbox: "Do not send invoices to this address").

**Addresses.** `buyer_address` may hold several parts (`; ` between them), each with where it was read. Read on the organisation's own pages, an
address can be someone else's: privacy and legal pages name the services a site uses — "Google LLC, 1600 Amphitheatre Parkway", "Cloudflare, Inc.,
101 Townsend St.", and every Shopify store's legal notice "Shopify Inc., 151 O'Connor Street, Ottawa". The corrected copy takes those parts out
(`address_checks.py` lists 31 such addresses), and a site template's sample address ("123 Main Street, New York, NY 10001", "Lorem ipsum"); a row
that stood on where the organisation is and was located by such an address has no relationship and is held (a Belgian store "in Ottawa" billed by
Hydro Ottawa). An address of another country than the organisation's own site and mailbox, read on that site, is another office's (taken out); a
register's address in one country with a site and mailbox of another is a namesake's site (held).

---

## 10. Evidence and provenance

Every researched value carries the page it was read on, the day, and a quote of at most 300 characters containing it (§2.4). The cells named
`*_as_published` quote; derived cells say `DERIVED` or `derived`; estimates say `estimated —` / `calculated —`; values by the kind of relationship
say so. `facts_provenance_json` gathers the sources of the mailbox, the buyer's facts, the vendor's facts and the relationship;
`buyer_facts_provenance`, `vendor_facts_provenance`, `method_notes` and `how_relationship_was_found` say how each was found.

---

## 11. The rules that never bend

The owner's rules are in AGENTS.md §1 (rules 1–20, each with his words and the date). The hard rules (§2) — a contribution that breaks one is
rejected: vendor in Canada by the source's own field, never by name; buyer named; ongoing = start ≤ today ≤ published end date (no end date:
kept and flagged); evidence or nothing (URL, date, quote ≤ 300 characters); organisational contacts only (never a person's mailbox, never a
pattern); no getting around blocks (CAPTCHA, login, bot check → `blocked`); no fabrication (`not_published` with the queries tried is an answer);
GST/HST derived, never published; at most 2 requests a second per host, identified user agent, cache.

Owner rules that shape every row: 6 (on invoice, by bank transfer — or no row), 8/14 (one row per buyer), 13 (four things; populate the rest;
say how), 15 ($5,000 a bill first, mark everything), 16 (every invoice field; estimates labelled), 18 (a utility abroad that a Canadian company
owns is a Canadian vendor: Tampa Electric, TEP, UNS Electric, Central Hudson, Green Mountain Power, Versant Power, Liberty's utilities, the
Caribbean utilities of Fortis, Emera and Algonquin — electricity only, never households), 19 (no other company abroad, even Canadian-owned), 20 (no
utility held jointly by several Canadian pension funds).

---

## 12. What the corrected copy changed, and why

<!--CORRECTIONS-->

How the corrections were made: each rule was written, run over every row, and its changes read before it was kept — the name rules
(`title_names.py`) were rewritten four times after reading their 2,000-odd changes (they had cut "Drivers On Call" to "Drivers On", "Ministère de
l'Environnement, de la Lutte contre les changements climatiques …" at its first comma, "Phoenix Contact" to "Phoenix"); the address rules
(`address_checks.py`) three times (a Canadian postal code typed with the letter O read as a British postcode; a German GmbH's own `.de` mailbox
held instead of its U.S. office's address being taken out; an embassy's mailbox on its government's domain). A person-name test for buyers was
tried and left out: it took "Tim Hortons" and "Paul Davis" for persons.

What the corrected copy could **not** apply (it needs a build's inputs): a municipality's record row giving way to its estimated electricity, a
legal name from another source where a junk one was cleared (the cell is left empty and the field shows as not published), mailboxes the
referee had not re-read when Actions stopped, the draft invoice header of the rows that received a mailbox in the correction (left empty), and the
packages (`P01…P15`) and JSON-lines copy (the release still holds the 22:10Z ones).

---

## 13. Known limits — said plainly

<!--LIMITS-->

---

## 14. If the project resumes

1. Read AGENTS.md, then `coord/ACTIONS_PAUSED`, `STATE.md` (top), `coord/DECISIONS.md` (bottom), this file.
2. Only with the owner's word: revert the commit that added `coord/ACTIONS_PAUSED`, then bring the crawlers back far slower than before (in the 24
   hours before GitHub's block the repository ran 583 workflow runs, 253 hours of run time, most of them crawls that restarted themselves; GitHub's
   terms bar a disproportionate burden and, on GitHub-hosted runners, activity unrelated to the software project).
3. Before any build uses a change to the owner's test, measure it: `python3 tools/replay_owner_test.py ranked_buyers.csv.gz` (it caught two errors
   on 2026-11-14 that would have shipped). A change to rank.py is checked with `python3 -m pyflakes` (a sample run, `RANK_SAMPLE=50`, needs more
   than 7 GB of memory).
4. Work billers first: one page read at a biller fills thousands of rows (rule 16). The billers with the most ready rows still billed "by the kind"
   are listed in section 13.
5. Never: a person's mailbox, a guessed address, webmail, a CAPTCHA or login worked around, the CRA GST/HST registry automated, an estimate in a
   published cell, a company abroad as a Canadian vendor (except rule 18's utilities), a buyer twice.
6. After any new build, run the final correction over its table (the three commands of section 0) — until its rules are moved into the build:
   the name rules (`title_names.py`), the address checks (`address_checks.py`), the site checks, the mailbox lists (`REVIEWED_OUT`,
   `PERSON_MAILBOX`, `WRONG_SITE`, `TYPE_OVERRIDE`) and the EPA export fix of `correct_table.py`. Two of its rules already are in rank.py (legal-page
   names, separators at a name's ends). Its lists are by address, not by row: a new build keeps them right.
7. What would add most, in order: (a) read the billing pages of the billers still "by the kind" (section 13 lists the largest — Gowling WLG,
   Central Hudson, Tucson Electric Power, the City of Vancouver, Green Mountain Power, Sun Life …): one page fills thousands of rows' payment and
   delivery fields in the biller's own words; (b) re-read by the referee the mailboxes found after Actions stopped
   (`data/incoming/claude/claude_buyer_ap_results_c5k*.csv` whose rows have no `verified` outcome); (c) the $5,000+ rows held for no mailbox
   (`contrib/claude/c5k_sites.py`, `c5k_mailboxes.py --sites`); (d) the organisations abroad tied to a Canadian biller by a record (the second half
   of the route to a million, `docs/ROUTE_TO_1M.md`).

---

## 15. Words used

**buyer** — the organisation billed. **vendor / biller** — the Canadian organisation that sends the bill. **referee** — the `verify-and-merge`
workflow (`tools/ingest_results.py`) that re-fetches every evidence page and keeps only values it finds on it. **tier** — A contract with a
published end date ≥ today · B awarded in the last 12 months · L 12–36 months ago · F older or ended · M register / roster of a Canadian body ·
T service seen on the buyer's side · C/D named as a client by the vendor (dated D) · E linked from the vendor's site · R `.ca` registration ·
I by where the organisation is · N no relationship record. **kind** — the relationship's kind (section 4). **lane** — an agent's share of the work
(claude, chatgpt, codex, gemini, jules).
