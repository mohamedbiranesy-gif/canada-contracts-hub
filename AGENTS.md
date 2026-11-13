# AGENTS.md — the contract every AI on this repo follows

Read this whole file before doing anything. It applies to Codex, Jules, Gemini CLI, Claude, and any other agent.

## 1. Mission
Build the most complete, verified dataset of **ongoing contracts whose vendor is located in Canada**, with every
public fact about each contract, buyer and vendor:
- **Contract:** identifiers / PO / reference, dates, value, link.
- **Vendor:** legal name, registry numbers, Business Number, derived GST/HST, address, phone, website, role e-mails.
- **Buyer:** address, website, **accounts-payable / invoicing e-mail or portal**, procurement contact.

The target is every such contract on earth that a public source exposes. Today we have 511,762, and the goal is to
keep adding sources until none are left.

**Owner's goal (2026-10-28, binding): 30,000+ different buyers, each with a verified invoicing / AP e-mail and at least
one contract with a Canada-located vendor.** Today there are only ~5,851 distinct buyers behind 770k contracts, and
~2,858 have a verified e-mail. More contracts from buyers we already have add little. Rank every new source by how
many NEW distinct buyers it brings (towns, school boards, hospitals, universities, agencies, US cities/counties/states/
school districts/transit agencies, prime contractors in subaward data, other countries' public bodies) and build
those first. Keep each buyer's website when the source has it: the no-AI crawler (tools/ap_crawler.py) finds the
invoicing e-mail from the website.

**Owner rules (2026-11-11, binding; three messages, 06:24, 07:15 and 07:48 EST).**
1. **A row needs a relationship that is a fact.** "When do we know for a fact? When … something being where it is means that there's
   a relationship … the odds of it not being a relationship [are] extremely low." A store that runs on Shopify, a DNS zone on a
   provider's servers, a `.ca` name that answers, an entry on a public register, an award record: facts. A vendor's client list is the
   vendor's statement; a link is a link; an inference is not a fact. Every row says which it is (`relationship_fact_basis`).
   (Since 16:01 EST the same day a row may also stand on where the organisation is, said to be that: rule 13.)
2. **Around that fact the row carries what an invoice carries, every field of it**: "the amount that would be billed within that
   billing cadence, the correct address, the vendor, all the stuff that would be within an invoice". Billing period
   (`recurring_billing` + its quoted source), amount (`bill_amount_indicative` from the vendor's own price list, or the contract value),
   what is billed, currency, how the bill arrives and is paid, tax rule, bill number, both parties' legal names, addresses and tax
   numbers. `tools/vendor_billing.py` reads the vendors' own price and terms pages; the ranker's log gives the fill of each field.
3. **Published first; a calculated value only when several signals agree, and labelled as calculated** ("inference of inference …
   becomes a calculated guess"). Never an invented value, never a calculated one presented as published.
4. **Monthly or quarterly billing by the vendor is the strongest relationship** ("billed for something monthly … or every 3 months
   … systematically by the vendor"), and a store on Shopify was the agreed example of it (until 13:09 EST the same day: rule 6). It is one kind among others: "it is a
   subcategory of what I'm asking". Contracts, construction awards, services rendered stay in scope ("which company is doing it,
   which vendor, by the city").
5. **Do not lean on one lane, and do not inflate.** "Whatever can give us the most populated fields … and the most amount, but
   populated." Rank a source by the fact-level rows it brings times the invoice fields it fills. The target stays 1,000,000 rows, and
   the way a row is made keeps changing: "don't accept one state of things".

**Owner rules (2026-11-11 afternoon, binding; 12:31, 13:00, 13:09, 13:40, 13:58 and 14:20 EST). Where they differ from the five rules above,
these win.** He was shown where each kind of row is billed and paid, and was asked; the words in quotes are his.
6. **On invoice, by bank transfer — or it is not a row.** "It needs to be bank transfers relationship not credit card … Shopify is over
   saturated in this way … if it's not on invoice, by bank transfer then it's no." A relationship whose bill is charged to a card on file
   (a Shopify store, self-serve software, most hosting plans) or is paid through a go-between (a `.ca` name through its registrar) makes
   no row; those rows were taken out of the table ("Remove them": 137,000 of 282,000). An invoice that can be paid by bank transfer or
   cheque is in, also when the biller would take a card ("In"). Rule 4's example — a store on Shopify — no longer stands.
7. **Any Canadian entity may be the one that sends the invoice**: a company, a regulator, a public body, an association ("Any Canadian
   entity … some type of entity that would be like … whatever month, year thing, okay, now you owe us so and so amount of money").
   "The buyer does not matter at all": any organisation, anywhere.
8. **One row per buyer. No buyer twice** ("only 1 buyer so no buyer should be repeated") — a city that pays forty Canadian vendors is one row.
9. **The general mailbox is fine** when the organisation publishes no invoicing mailbox: "the general email is where they take in, they do
   their intake. So that is fine." A label that called such a row not ready was "moronic"; it survives only as `ap_mailbox_ready`.
10. **Every row ship ready, its invoice fields tailored to its kind of relationship**: "as populated as that relationship could expect it
    to be … Shopify … won't have a purchase order … maybe some other thing will"; "obviously can't be strict layout we have followed thus
    far, that was more so for contract, but tailor to each". One function decides (`tools/relationship_rows.py: owner_test`) and every row
    says it: `ship_ready`, `ship_ready_missing`, `payment_route`, `payment_route_basis`, `invoice_fields_for_kind`,
    `invoice_fields_missing_for_kind`. A row is ready when the relationship is established and current, the organisation's role mailbox was
    re-read by the referee, the bill comes on invoice and bank transfer is a published or inherent way to pay it, the fields of its kind
    are filled, and nothing flags it.
11. A contract awarded more than three years ago with no published end date is not a current relationship. When a vendor's GST/HST number
    is not public, its number in its home register (NEQ, corporation number) fills the vendor's number, labelled as such.
12. **Lanes — all of them, "and more, don't limit yourself, don't forget all invoice details"**: owners of Canadian patents billed every year
    by their Canadian patent agent; trademark owners and their Canadian agent; firms licensed by a Canadian regulator; members of Canadian
    chambers and associations; dealers, franchisees and commercial tenants of Canadian companies; importers abroad buying from Canadian
    exporters; US firms with a registered lien to a Canadian lender, lessor or supplier; more public bodies under contract. Rank a new
    source by the distinct NEW buyers it brings whose bill comes on invoice. The target stays 1,000,000 rows; on 2026-11-11 19Z the rows
    that meet rule 6 were 7,833 (5,461 with a mailbox, 1,343 ship ready) — nearly all public bodies under contract.

**Owner rule (2026-11-11 16:01 EST, binding).** He was told the count stood at 7,754 and answered, in full: "1 million goals think
differently if need be this your project take all liberty as long as under what we laid down invoice bank eft email Canadian vendor in
simple terms and just populate those field as best as you can don't just go empty there's clear goal and it is 1 million get there max".
13. **Four things make a row: a Canadian biller, a bill on invoice, a bank payment, the organisation's mailbox. Everything else is
    populated as well as it can be, and says how it was populated.** How lane `claude` reads it (coord/DECISIONS.md, 2026-11-11 21:30Z):
    - A field of a row's kind that nothing published fills no longer takes the row out. It is named on the row
      (`invoice_fields_missing_for_kind`, and inside `ship_ready`) and the row sorts below the complete ones. Two fields must be there: the
      biller's own printed address (it is what puts the biller in Canada, §2.1) and, for a row that stands on where the organisation is,
      the organisation's own address.
    - When a biller's own sentence on how it bills and is paid has not been found, the row says how a bill of that kind is billed and
      paid — an association's dues, a regulator's fee, an agent's account, a supplier's sales to its dealer, rent, a sponsorship — and says
      that it is "by the kind of relationship". A sentence of the biller always wins: card only takes the row out, "we send no invoice"
      fails it. Never for hosting or software, where the common way is a card on file.
    - **A relationship may stand on where the organisation is** (his own words that morning: "something being where it is means that
      there's a relationship"): electricity at an address is distributed and billed by one body, by law, every month, on an invoice, paid
      through a bank (`tools/by_location.py`). The biller is certain for the address; whose name is on the account is not published, and
      every such row says both. One row per buyer still: a record (a contract, a licence, a roster) or a service seen on the buyer's side
      comes first; the distributor of its address is what an organisation with a mailbox and an address has when it has nothing else.
    - Unchanged: never an invented value; never a calculated value presented as published; every hard rule of §2.
    `ship_ready` is "yes" (every field of its kind, in the biller's own words), "yes (…)" with what is by the kind, by where the
    organisation is, or not published, or "no". The log of each build counts the three apart.

**Owner rules (2026-11-11 evening, binding; 20:04, 20:14, 20:22 and 20:36 EST). Where they differ from the rules above, these win.** He was shown
how full the rows are (of 136,513 rows that met the test, 70,503 carried an amount and a billing period and 24,279 every main invoice field) and
what $5,000 a bill would leave (1,510 rows); for half an hour he chose a hard floor and one row per buyer and vendor, then settled it at 20:36.
14. **One row per buyer; no buyer twice — "hard rule … so it should be 1 million buyers, vendor can be repeated".** Rule 8 stands. The 316,131
    buyer-vendor relationships of the contract dataset stay on file behind their 5,590 buyers (`tools/relationship_rows.py main()`: an
    analysis, not the deliverable); a buyer's row carries, among the records of its best tier, one whose published value is $5,000 or more,
    and counts its other Canadian vendors.
15. **$5,000 a bill is a priority, not a wall.** "the relationship billed amount per cadence should be 5000 plus", then: "we will also include
    those of lower value but mark them, mark everything, prioritise over 5000 … that's why I was willing to lift 5000 cap, make it soft".
    Every row carries `amount_mark` — published $5,000 or more · estimated $5,000 or more · published under $5,000 · estimated under $5,000 ·
    no amount — and the table is written in that order (`tools/priority_sort.py`). Rank a new source by the new buyers it brings AND by how
    large its bills are: public bodies under contract, dealers of Canadian manufacturers, firms certified or licensed by Canadian bodies,
    customers of Canadian business software, organisations with large premises.
16. **Every invoice field, as far as the kind of relationship goes; an estimate where nothing is published.** "what about estimated value per
    billing cadence and all other rows/invoice fields … I want to make sure it's useful efficient work"; "an inference be permissible,
    combined with billing cadence a fair estimate can be made … if no findable amount at all … be sure to populate as much as possible per
    relationship, let's not slack". An estimate is calculated from published figures, says so and says from what (`bill_amount_calculated`,
    opening "estimated —" or "calculated —"); it never stands in a published cell, and where nothing published supports one (what a dealer
    buys) the cell stays "not published". Every build's log gives three counts: the rows that meet the test; of those, the rows with an
    amount and a billing period; the rows with every main invoice field. One page read at a biller fills thousands of rows: billers first.
17. **Built to run without long sessions.** "I have one credit reset left … it'll have to go back to short work sessions and your automation
    hand-offs [doing the] majority … this isn't sustainable". Whatever is done twice is a tool plus a workflow; a session reads the counts,
    reads rows, fixes rules. He was told plainly that a million buyers is not in sight from what is on file (an estimate of 400,000 to
    500,000 organisations in Canada with a site, a mailbox of their own and an address a distributor can be named for) and that the second
    half must come from organisations abroad tied to a Canadian biller by a record.

**Owner rule (2026-11-13 09:46 EST, binding).** Asked whether a U.S. power company owned by a Canadian company may be the biller: "And yes, we'll
count it. The U.S. power company owned by Canadian company counts as Canadian vendor. We will count it. … We're still getting to 1 million."
18. **A utility abroad that a Canadian company owns is a Canadian vendor.** Tampa Electric (Emera), Tucson Electric Power (Fortis), Green Mountain Power
    (Énergir), Versant Power (ENMAX), Liberty's utilities (Algonquin), the Caribbean utilities of Fortis, Emera and Algonquin: an organisation whose own
    printed address lies wholly inside such a utility's retail territory stands on that relationship exactly as a Canadian organisation stands on its
    distributor (rule 13): electricity only, the biller certain for the address, the account holder not published, the parent's own page quoted for the
    ownership. Households are never rows.

**Owner rules (2026-11-13 11:44 EST, binding).** Asked two yes/no questions, he answered "no" to both.
19. **A company abroad that a Canadian company owns is not a Canadian vendor — except the electric utilities of rule 18.** US cities paying the US
    companies of CGI, Stantec or WSP, plans paying Empower or John Hancock, tenants of a Canadian group's buildings abroad: no row. (A Canadian legal
    entity's own branch abroad — Sun Life Assurance Company of Canada's U.S. branch, owner 2026-11-13 08:07 EST — is the Canadian entity itself and stays.)
20. **A utility abroad held by several Canadian pension funds together is not a Canadian vendor.** Puget Sound Energy (OMERS, BCI, Ontario Teachers',
    AIMCo, with Macquarie and PGGM) and Minnesota Power (Canada Pension Plan with a US partner): no row. Rule 18 is a utility that a Canadian company owns.

**Owner rule (2026-10-28): when a buyer publishes no invoicing/AP mailbox, save its purchasing/procurement role mailbox
  (`ap_email_type=procurement`) or, failing that, its general role mailbox such as info@ / reception@ / greffe@
  (`ap_email_type=general`), with status `found` and a note saying no invoicing mailbox is published.** Still never
  a named person. `not_published` only when the organisation publishes no role mailbox at all.

You are a **lead**, not a worker. Your queue tells you where to start. If you see a better method, a missing source
or a bug, act on it: do it, write it down (section 6), and tell the others.

## 2. Hard rules (break one and the whole contribution is rejected by the verifier)
1. **Vendor in Canada** = the source's own vendor country / address field says Canada. Never infer it from the name.
2. **Buyer must be named.** No "undisclosed client".
3. **Ongoing** = start <= reference date and published end date >= reference date (reference date: `coord/config.json`;
   the daily rebuild advances it to today, so the dataset always means "ongoing now").
   No end date → keep the record, flagged `ongoing_no_end_date`. Never silently drop data.
4. **Evidence or nothing.** Every researched value carries:
   - the URL of a page you actually opened;
   - the retrieval date;
   - a quote of at most 300 characters that contains the value.

   The ingest workflow re-fetches the page and rejects any value that is not on it.
5. **Organisational contacts only.** Use role mailboxes the organisation publishes itself: `factures@`, `comptesapayer@`,
   `accountspayable@`, `ap@`, `invoices@`, `finance@`, `procurement@`, `info@` and the like.
   - Never a named person's mailbox.
   - Never an address built from a pattern.
6. **No getting around blocks.** CAPTCHA, bot check, login wall, "access denied" → status `blocked`, then move on.
   - Never use proxies, CAPTCHA solvers or stolen sessions.
   - Never automate the CRA GST/HST registry: it is CAPTCHA-protected.
7. **No fabrication.** `not_published`, with the queries you tried, is a valuable answer.
8. **GST/HST is derived, not published:** BN9 + `RT0001`. Always label it `derived`.
9. **Be polite to servers.**
   - At most 2 requests/second per host.
   - Identify your user agent.
   - Cache everything you fetch.

## 3. Map of the repo
| Path | What |
|---|---|
| `docs/SCHEMA.md` | Binding record format for contracts (normalized + raw + status + enrichment) |
| `docs/PIPELINE_KNOWLEDGE.md` | Everything learned building 82+ source pipelines (read before writing a scraper) |
| `docs/PLAYBOOK.md` | Where AP / invoicing contacts live, query bank, pitfalls (add to it!) |
| `docs/SOURCES_COVERED.md` | Sources already in the dataset, so you don't redo them |
| `docs/SOURCE_INTEL_BRIEF.md` | What kinds of sources are still missing |
| `docs/RETURN_FORMATS.md` | Exact CSV formats for research results |
| `docs/DATASET_README.md` | Fill rates, files, field meanings of the current dataset |
| `scripts/<source>/` | The pipeline code for every source already harvested |
| `scripts/enrichment_*` | Registry matching (Corporations Canada, Quebec REQ, BC OrgBook, RBQ, CRA charities), website discovery |
| `scripts/merge/` | Merge → enrich → assemble → README generation |
| `notes/<source>.md` | Per-source notes: endpoints, quirks, row counts |
| `coord/tasks/<lane>/` | Work queues (CSV batches of 100) |
| `coord/NEXT.md` | Auto-generated: the next open batch for every lane |
| `coord/STATUS_BOARD.md` | Auto-generated: what is done, fill rates, verification rates |
| `coord/inbox/<agent>.md` | Messages to each agent (read yours first, write to others) |
| `coord/source_registry.csv` | Candidate sources to build (scouted), with status |
| `coord/results/` | Verified team findings (written by the ingest workflow only) |
| `data/incoming/<lane>/` | Where you put results (CSV / JSONL.gz) |
| `contrib/<agent>/` | Your own scrapers and scripts. Never run automatically by workflows |
| `tools/` | Validator, ingest/verify, status board, dataset patcher |
| `prompts/` | Standing prompts the scheduled AI runs use |

**Big data is in GitHub Releases, not git:**

```
gh release download dataset-latest -D data/release
```

That fetches the dataset, vendor and buyer tables, and harvester state. `data/README.md` lists every asset.

## 4. Lanes (who owns what, so no work is duplicated)
| Lane | Agent | Owns |
|---|---|---|
| `gemini` | Gemini app on the owner's Mac (Task mode, §8); Gemini CLI in GitHub Actions when its API key can search | Québec buyers' AP/invoicing contacts (`coord/tasks/gemini/gemini_buyer_ap_*`), then Québec vendor contacts, French-language sources |
| `jules` | Jules (Gemini coding agent) | Building new source pipelines from `coord/source_registry.csv` (status `todo`), heavy harvest shards |
| `chatgpt` | ChatGPT / Codex app on the owner's Mac (automation every 30 minutes, §8) | Independent QA audit, English-Canada + US buyers' AP contacts (`coord/tasks/chatgpt/`), vendor contacts outside Québec |
| `codex` | Codex (ChatGPT coding agent; the ChatGPT automation takes this queue when its own is done) | New source pipelines outside Canada (US states/cities, EU, UK, AU, IGOs, private-sector disclosures), invoicing contacts of buyers outside Canada/US (`coord/tasks/codex/`), vendor-identifier enrichment code, reviewing every PR |
| `claude` | Claude (integrator, when available) | Merge/rebuild the dataset, registries, write new batches, fix tools, route hard cases |

Rules:
- Work your own lane first.
- When it is empty, or you can add more value elsewhere, write a message to the lane owner's inbox and take a
  clearly separate slice: for example "I'm doing rows 50-100 of chatgpt_vendor_contacts_batch07".
- Never overwrite another agent's results.
- Scheduled and automated agents never pause or disable their own schedule. When your queue is empty, take the
  next open work by the rule above and say which slice you took in that lane's inbox.

**Picking your batch.** The next batch is the lowest-numbered file in `coord/tasks/<lane>/` that has no results file in
`data/incoming/<lane>/`. `coord/NEXT.md` lists it.

## 5. How to contribute (so the automation verifies and merges your work without a human)
1. Put research results in `data/incoming/<lane>/<lane>_<task>_results_batchNN.csv`, in the exact format of
   `docs/RETURN_FORMATS.md`.
2. For new sources:
   - put normalized records in `data/incoming/<lane>/records_<source_key>.jsonl.gz`, one record per line in the
     `docs/SCHEMA.md` format;
   - put the scraper in `contrib/<lane>/<source_key>/`;
   - put the notes in `notes/<source_key>.md`.
3. Run the checks before you open a PR:
   - `python3 tools/validate_returns.py <csv>`
   - `python3 tools/validate_records.py <jsonl.gz>`
4. Open a PR titled `[<lane>] <what> <batch>`.
   - **Auto-merge** happens when the PR touches only `data/incoming/**`, `contrib/**`, `notes/**`, `coord/inbox/**`,
     `coord/source_registry.csv` and `docs/PLAYBOOK.md`, and validation passes.
   - Any other path (tools, scripts, workflows) waits for review by another agent or the owner.
5. After merge, the ingest workflow does the rest:
   - re-fetches every evidence page;
   - keeps only verified values in `coord/results/`. A value it cannot see (bot-protected page, or e-mails shown only
     in a browser) counts when two different lanes quote it from the same page (`cross_verified`);
   - logs every row's outcome in `coord/results/verification_log.csv`. Check your own rows there (lane `claude`'s rows are in
     `verification_log_claude.csv` and its `.partNN.csv` files);
   - updates `coord/STATUS_BOARD.md` and `coord/NEXT.md`;
   - creates `verify_*` tasks for the other lane when a page could not be fetched.
6. Small, frequent PRs. A PR with 30 solid rows beats a promise of 300.

## 6. Talking to each other
- **Start of every run:** read `coord/inbox/<you>.md`, `coord/STATUS_BOARD.md` and `coord/NEXT.md`.
- **End of every run:** append to the right inboxes. Use the format `## YYYY-MM-DD HH:MM from <agent>`, then a short
  message: what you did, what you learned, what you need.
- **Patterns that speed everyone up** go into `docs/PLAYBOOK.md`, for example "Québec CIUSSS all invoice through the
  central 'Fournisseurs' page".
- **Hard cases** (ambiguous vendor, conflicting e-mails): set `status=unclear` with notes, and the verifier routes them
  to a second agent.
- **Decisions that change the method:** write them in `coord/DECISIONS.md` with your reasoning.

## 7. Quality bar
- **Read before you code.** Read `docs/PIPELINE_KNOWLEDGE.md` and the notes of a similar source first.
- **Keep everything the source publishes.** Store all source fields verbatim in `raw`, then normalize. Never drop a field.
- **Prefer bulk files and APIs.** Look for open-data portals, CKAN, Socrata, ArcGIS, OCDS before HTML scraping.
- **Report counts.** Rows seen / Canadian-vendor rows / ongoing rows go in `notes/<source>.md`.
- **Test on a sample first,** then run the full pull.

## 8. Agents on the owner's Mac
Two agents run on the owner's MacBook while it is awake and their apps are open: ChatGPT (Codex app, an automation
every 30 minutes, lane `chatgpt`) and Gemini (Gemini app, Task mode, lane `gemini`).
- **ChatGPT / Codex: shell with network.** Start every run with:
  ```
  git pull --rebase            # commit or stash your own work first
  python3 tools/mac_sync.py    # uploads Gemini's local rows and refreshes Gemini's instructions
  ```
  Then work your queue. Commit, `git pull --rebase` and `git push origin main` every 10 rows.
- **Gemini app: shell without network.** It works in `/tmp/canada-contracts-hub` on a `gemini/...` branch, saves rows,
  commits locally, and never pushes, pulls or fetches. Its exact loop is in `GEMINI.md` §A.
- `tools/mac_sync.py` pushes Gemini's work, committed or not, as a branch `gemini/sync-<time>`. The `agent-branch`
  workflow folds it into main (lane paths only, CSV rows merged) and deletes the branch. Any agent that can push a
  branch but not main can do the same: push `<lane>/<anything>`.
