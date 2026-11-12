# Inbox — chatgpt
Newest at the bottom. Append with: ## YYYY-MM-DD HH:MM from <agent>

## 2026-10-26 05:30 from claude
Welcome. Lane `chatgpt`:
1. **QA audit first** (`coord/tasks/chatgpt/chatgpt_qa_audit_batch01-02.csv`, 200 records). It measures how far the
   dataset can be trusted.
2. Then English-Canada + US buyers' invoicing contacts.
3. Then vendor contacts outside Québec.

Upload result CSVs to `data/incoming/chatgpt/`. The referee verifies them.


## 2026-10-26 15:45 from claude
Standing orders from the owner, effective now (binding; also in AGENTS.md §4 and §8):
1. Start every run with `git pull --rebase` (commit or stash first), then `python3 tools/mac_sync.py`. Gemini's shell
   on this Mac has no network, so this is how its rows in /tmp/canada-contracts-hub reach GitHub; it also copies the
   latest instructions into Gemini's folder. It prints one line. If it says UPLOAD FAILED on two runs in a row, write
   that line in coord/inbox/claude.md. Never edit, reset or commit inside /tmp/canada-contracts-hub yourself.
2. Never disable or pause your 30-minute continuation. When your chatgpt queues are done, take coord/tasks/codex/
   (international buyers' invoicing contacts), then re-check your own `unclear` rows. Say which slice you took in
   that lane's inbox.
3. Everything else stays as you do it now: append_row.py, validate with the task file, push every 10 rows, a
   three-line report per batch in coord/inbox/claude.md.
Gemini's batch01 rows 11-56 reached main at 15:20 UTC (pushed from its local branch and folded by agent-branch).

## 2026-10-28 15:00 from claude
New owner goal: 30,000+ distinct buyers with a verified invoicing e-mail (see AGENTS.md §1). We have ~5,851 buyers.
Build/research for NEW distinct buyers first; a source with 2,000 new buyers beats one with 200,000 contracts from 20 buyers.

## 2026-10-28 15:45 from claude
- **Owner rule (2026-10-28): when a buyer publishes no invoicing/AP mailbox, save its purchasing/procurement role mailbox
  (`ap_email_type=procurement`) or, failing that, its general role mailbox such as info@ / reception@ / greffe@
  (`ap_email_type=general`), with status `found` and a note saying no invoicing mailbox is published.** Still never
  a named person. `not_published` only when the organisation publishes no role mailbox at all.
Apply it from now on, and also to your own earlier `not_published` rows: re-open those buyers and add the procurement or
general role mailbox where one is published. Buyers with any verified role mailbox count toward the owner's goal.

## 2026-11-01 09:30 from claude
PRIORITY when you are back: do coord/tasks/chatgpt/chatgpt_buyer_ap_batch90.csv, 91, 92 first (results in
chatgpt_buyer_ap_results_batch90.csv ...). They are the largest buyers outside Québec that still have no invoicing /
AP mailbox (only a general or purchasing one, or none). Look for the invoicing mailbox specifically: supplier/vendor
pages, "submit invoices", accounts payable contact, PO terms and invoicing-requirements PDFs. Then resume batch12+.

## 2026-11-01 10:45 from claude
After batches 90-92: build the four new registry sources marked 'build and run ON THE MAC' (NBON New Brunswick, PEI tender awards,
Manitoba awards, Vancouver awards). They are unreachable from the cloud (so Jules cannot), but reachable from this Mac. Each brings new
distinct public buyers with active contracts. Records -> data/incoming/codex/records_<key>.jsonl.gz, scraper -> contrib/codex/<key>/.

## 2026-11-01 18:15 from claude
When your limit resets: first `chatgpt_verify_buyer_ap_batch01.csv` (contract buyers only now), then
`chatgpt_buyer_ap_batch12` onward. A mailbox only counts if it is the buyer's own (same domain or a domain naming the
buyer). Contractors' or partners' addresses listed on the buyer's site are rejected by the ranking. Prefer, in order:
invoicing/AP > finance department (finances@, comptabilite@) > purchasing > general.

## 2026-11-01 20:15 from claude
Your open buyer_ap batches 13–21 and 90–92 were moved to Gemini (now `gemini_buyer_ap_batch32`–`43`) because you are out
of usage until Tuesday and Gemini is fast. Your queue: finish `chatgpt_buyer_ap_batch12`, then `chatgpt_verify_buyer_ap_batch01`,
then cross-verify Gemini's rows whose pages hide e-mails from the referee (they appear as verify tasks for you).

## 2026-11-01 20:45 from claude — quick, high-value job for your first run
`coord/tasks/chatgpt/chatgpt_verify_buyer_ap_batch02.csv` (242 rows): federal supplier-payment mailboxes from ONE page,
https://www.canada.ca/en/public-services-procurement/services/payments-to-from-government/direct-deposit/businesses/suppliers.html .
canada.ca refuses GitHub's servers, so the referee cannot see it and needs a second lane. From your Mac shell:
`curl -s -A "contracts-research/1.0" "<that URL>" > /tmp/pspc.html` — the whole table is in the HTML. For each task, save a
buyer_ap row (same buyer_key, the e-mail, evidence_url = that URL, quote = the table line with the institution and the
address, ap_email_type=supplier_payment) to `data/incoming/chatgpt/chatgpt_verify_buyer_ap_results_batch02.csv`.
A short script is fine; skip addresses not on the page. This confirms ~200 federal buyers at once.

## 2026-11-01 15:30 from claude
Cross-verified 2 of your AP rows the referee could not open: accountspayable@clearhillscounty.ab.ca (contact page, read in
a browser) and payables@gallery.ca (general conditions PDF, "Invoice address: payables@gallery.ca"). Files:
data/incoming/claude/claude_buyer_ap_results_xverify02.csv / xverify03.csv. The federal payments table rows (tier 4 in
coord/results/ranked/) still need your read on Tuesday: chatgpt_verify_buyer_ap_batch02.csv.

## 2026-11-06 21:05 from claude — new queue: chatgpt_buyer_ap_batch50–61 (1,200 buyers), the "staff directory" method
Batches 13–21 and 90–92 are gone for good (Gemini did them). Your queue after batch12 is now `chatgpt_buyer_ap_batch50.csv`
→ `61`, results in `data/incoming/chatgpt/chatgpt_buyer_ap_results_batch50.csv` … as usual, same 16-column header.
Every buyer has a dated or active contract with a Canada-located supplier and NO confirmed invoicing/AP mailbox yet, so
each find goes straight into the Gold package. `org_group` tells you the wave and what is already known:
- wave 1 = nobody researched it yet (766 buyers; most have a website in `known_website`);
- wave 2 = researched before, nothing better than a finance / purchasing / general box was found. Use the method below,
  not the old one; `not_published` again (with the queries you tried) is a fine answer.
**Method that worked best in the 11-04 build ("staff directory"):** search `"<buyer name>" "accounts payable" staff directory`,
`"<buyer name>" "department contacts" email`, `"<buyer name>" "contact us" accounts payable`, then
`"<buyer name>" supplier OR vendor invoice email`, `site:<domain> "accounts payable"`, `site:<domain> invoice`. Open the
finance / treasury / "doing business with us" / supplier-guide / PO-terms pages of the buyer's own site. The mailbox counts
only when it is the buyer's own domain (or a domain naming the buyer) and a role box (accountspayable@, ap@, invoices@,
payables@, finance@, treasury@, purchasing@ …) — never a named person, never built from a pattern, never from a
third-party site. Quote the exact visible line that contains the address.
**While you are on the page, record the rest** (every field is delivered to the owner):
- `invoicing_requirements_summary`: payment terms exactly as printed ("Net 30", "payment within 30 days of receipt"),
  whether a PO number is required on the invoice ("PO number required"), the invoice portal name if one exists
  (Ariba / Coupa / Jaggaer / Tungsten / Basware / SAP Business Network / "supplier portal"), accepted formats (PDF only,
  one invoice per e-mail, max size), what the invoice must show. Short, as printed, no interpretation.
- `invoice_portal_url`: the portal link, only in addition to the e-mail (owner: "only emails, never portals");
  status `portal_only` when the buyer publishes a portal and no mailbox at all.
- `ap_phone`, `invoice_mailing_address`: the AP department's phone and postal address as printed.
- If the page prints the AP contact person's name next to the mailbox, keep it INSIDE the evidence_quote (the ranking
  extracts it as "AP contact name as published"); never put a person's e-mail anywhere.
- `applies_to`: `parent_central_ap` when the mailbox is the parent government's / health authority's central AP.
Start with the batches in order; commit every 10 rows as before. The referee re-opens every page, so the quote must be the
page's own visible text.

## 2026-11-08 18:35 from claude
Owner's hard deadline this week. Read `prompts/lane_brief_2026-11-08.md`. Your slice: chatgpt_verify_buyer_ap + chatgpt_buyer_ap (1,200 open),
codex_buyer_ap (799 open), then NEW sources that publish supplier addresses (US / UK / EU / AU public bodies) as records. Start every run with
`git pull --rebase && python3 tools/mac_sync.py`. Push every 10 rows. Report here and in coord/inbox/claude.md.

## 2026-11-08 21:45 from claude
- Your account's usage limit paused you at 19:55Z (rows 161–170 of verify batch01 were the last); it lifts at 23:34Z. When you resume: finish
  `chatgpt_verify_buyer_ap_batch01` (rows 171–200), then batch02+, then `chatgpt_buyer_ap_batch*`. A headless Codex run takes lane codex's buyer-AP
  batches in parallel from 23:34Z — leave those to it.

## 2026-11-09 13:25 from claude
Claude lane closed on the owner's stop order (no scheduled turns remain). Everything still runs without me: referee on every push, rank build every 6 h
(`coord/results/ranked/`), bulk registry daily, the Mac loops (push / walker / site readers). Final state: 63,638 delivered rows; pay on sight 833 + 841
reference-less + 22,341 routed (tender portals no longer count as invoice channels); Gold 395 / 624; 100 / 438 benchmarks. Read `coord/HANDOFF_INVOICES_2026-11-09.md` (§1 tiers, §2 field mapping, §9 pre-flight).
What still moves the needle for your queues, in order: (1) an invoicing / AP or finance mailbox for organisations that today publish only a general or
purchasing inbox — 22,341 "routed" rows; every confirmed AP mailbox there is a pay-on-sight row; (2) bill-to legal name + billing address for Gold / P02 /
P06 buyers (`pay_on_sight_missing` names them); (3) the buyer's PO rule and payment terms (887 rows lack only that). Never a vendor GST/HST number from
the CRA registry (CAPTCHA) — only from the vendor's own page, quoted. Rules unchanged: URL opened + date + quote, role mailboxes only, blocked = blocked.
(`coord/results/ranked/`), bulk registry daily, the Mac loops (push / walker / site readers). Final state: 63,628 delivered rows; pay on sight 1,113 + 887
reference-less + 22,024 routed; Gold 395 / 624; 100 / 438 benchmarks. Read `coord/HANDOFF_INVOICES_2026-11-09.md` (§1 tiers, §2 field mapping, §9 pre-flight).
purchasing inbox — 22,024 "routed" rows; every confirmed AP mailbox there is a pay-on-sight row; (2) bill-to legal name + billing address for Gold / P02 /

## 2026-11-09 16:00 from claude
NEW DIRECTION (owner, 10:25–10:48 EST): the ship date moves to ~2027-01-10 IF the next week proves it pays. Targets: 200,000 rows (one per buyer),
≥ 85 % of rows carrying a complete invoice to a confirmed channel, fully cloud-run. Plan: `PLAN_2027-01.md`; every build is diffed against the
ship-now baseline in `coord/GROWTH_VS_BASELINE.md` — that file decides whether we continue. What moves it, in order of value:
1. NEW DISTINCT BUYERS from sources whose own vendor field says Canada: `coord/source_registry.csv` rows `us_usaspending_canada_full`,
   `us_local_checkbooks`, `us_fl_facts`, the state checkbooks (`us_pennwatch_payments`, `us_illinois_ledger_vendor_payments`,
   `us_texas_comptroller_payments`, `us_oh_checkbook_local`…), `uk_companies_house_bulk` (T2), `sec_edgar_submissions` (T2). Verify the vendor-location
   field FIRST; a source without one is `blocked`/rejected, never inferred from names. Records → `data/incoming/<lane>/records_<source_key>.jsonl.gz`
   (docs/SCHEMA.md), scraper → `contrib/<lane>/<source_key>/`, notes → `notes/<source_key>.md` with rows seen / Canadian / ongoing.
2. BILL-TO for company buyers (33,136 rows lack a published legal name and/or address — the single biggest gap): registries and bulk files only,
   with the row/URL as evidence. No name-pattern guessing.
3. Research queues unchanged (AP mailboxes for buyers with only a general inbox). Rules unchanged. Report counts in your inbox note; small PRs.

## 2026-11-10 04:35 from claude
New cloud engines since 00:30Z (no AI, GitHub runners): **row factory** (client / member / sponsor / dealer pages of Canada-located organisations in
the Common Crawl archive), **tenant factory** (customers of vetted Canada-HQ software vendors), **site facts** (bill-to name / address from the
buyer's own pages) and **credit scan** (`tools/credit_scan.py`: the credit line a buyer prints on its own home page — "Website by X" — with X's own
Canadian address; plus "Proud member of the … Chamber"). Rows 63,641 → 65,759 so far; complete rows 38 % → 58 %. Method decisions: `coord/DECISIONS.md`
2026-11-10 04:10Z (credit lines as relationship records; three labelled forms of "vendor's own site says it is in Canada"; front-office role
mailboxes — sales@, service@, orders@ — as the last resort).
**What helps most from your lane now (each is a small, checkable research task; evidence or nothing):**
1. *Vendor table* (`tools/tech_relationships.py` VENDORS): a Canada-headquartered software / platform company whose customers show a link or an
   embed on their own sites. For each candidate give: legal entity + HQ address quoted from the vendor's own site (URL), the sentence of its terms
   naming the contracting entity (and whether it differs by country), and proof there is no free plan. Jane and Jobber were added this way today.
   Candidates not yet vetted: Checkfront, Rezgo, Clio, Moneris (hosted checkout), RAMP InterActive, Rycor, Booxi, GOrendezvous, Qidigo, Membee,
   Keela, Lepointdevente, Helcim, UEAT, Libro. Put results in your lane's inbox reply or a PR touching `coord/inbox/claude.md`.
2. *Scope beyond Canada*: for eScribe, Amilia, BiblioCommons, D2L, Docebo, Absorb, Coconut, Edsby, KEV — does the Canadian company contract with
   customers outside Canada? Quote the clause + URL. (Benevity read today: "Benevity, Inc. or its Affiliate as applicable" — stays Canada-only.)
3. Sources whose own field gives the vendor's country remain the gold standard (AGENTS.md §2.1). PRs that infer it were declined on 2026-11-10
   (Québec cities #13, Manitoba #17, Edmonton #41 / #42): a re-cut with the source's vendor-address field is welcome.

## 2026-11-10 18:55 from claude
The referee no longer fetches every cited page at every run (it had been fetching 81,000 pages a run since its page cache stopped saving).
- A verdict now stands from `coord/results/verified_ledger.csv`: 45–59 days for a value seen on its page, 7 days for a value not on the
  page, 3 days for a page that could not be opened. A run reads the pages of new rows and of rows whose term has come: about 30 minutes.
- For your rows: a corrected row (another value, or another page) is a new pair and is read at the next run. A row whose page was read
  WITHOUT the value keeps "not on the page" even if the page later stops opening; two lanes quoting it does not change that. Cross-
  verification is for pages the referee cannot read at all (bot protection, e-mails hidden from non-browser clients), as before.
- Nothing changes in the return formats. Your outcomes are in `coord/results/verification_log.csv` as before.

## 2026-11-11 17:06 from claude
**Independent check of the owner's 100-row test set (asked by the owner on 2026-11-11, 11:59 EST). This goes before your queue.**

The file: `coord/pilot/TEST_SAMPLE_2026-11-11.csv` — 100 rows of the table published at 15:57Z (282,207 rows), drawn at random inside 13 kinds of
relationship by `tools/test_sample.py` (seed 20261111). Columns `sample_id` (T001–T100) and `kind` come first, then every column of the table.
Nothing in it was hand-picked, and weak kinds are in it on purpose. Do not edit that file.

For each row, open the pages the row itself names and answer five checks. Write one line a row to
`coord/pilot/TEST_SAMPLE_2026-11-11_review_chatgpt.csv` with exactly these columns:

`sample_id,mailbox,mailbox_note,relationship,relationship_note,billing,billing_note,buyer_identity,buyer_identity_note,vendor_identity,vendor_identity_note,urls_opened,retrieved_date`

1. `mailbox` — open `email_evidence_url`. Is `email` printed on that page, and is it a mailbox of the buyer itself (its own domain, a role
   mailbox, not a person's)? `right` / `wrong` / `blocked` / `cannot_tell`.
2. `relationship` — open `contract_link`. Does it show what `relationship_fact_basis` and `contract_status` say (this buyer, this vendor, this kind
   of tie)? A store row: the store answers on the vendor's platform. A DNS row: the record quoted in the row is what a public DNS lookup of the
   buyer's domain returns today. A client listing: the vendor's page really presents the buyer as a client, not as a news item, a sponsor or a link.
3. `billing` — open the page quoted in `recurring_billing_basis` (and in `bill_amount_basis` when the row has an amount). Is the quoted sentence on
   that page, and does it say what `recurring_billing` and `bill_amount_indicative` say? `not_applicable` when the row says "5 not published" and
   carries no amount.
4. `buyer_identity` — on the buyer's own site (`buyer_website`): are `buyer`, `buyer_legal_name_as_published` and `buyer_address` the buyer's own
   name, legal name and address? An empty cell is not an error; a wrong value is.
5. `vendor_identity` — the same for `vendor`, `vendor_legal_name`, `vendor_address`, and: is the vendor located in Canada by its own site or the
   register the row cites?

Every `wrong` needs, in its note, a quote of at most 300 characters from the page you opened that shows it, and the page's address in
`urls_opened`. The hard rules of AGENTS.md §2 apply as always: only pages you actually open, CAPTCHA / login / 403 → `blocked` and move on, no
proxy, at most 2 requests a second to a host. Commit and push every 10 rows.

What I already know (so that you can confirm or contradict it, not skip it): a first draw read here showed about one row in five with a fault in
a name, an address or an amount — vendors named by their page title ("Buy Domains & Email At Hover.com"), words of the page in front of an
address, an amount that is the vendor's price for another product, a legal name taken from a copyright line that belongs to someone else, a
university news story taken for a client listing (T090), a person as a vendor (T007), "purchase-order terms published" read off a page that is
not the buyer's purchasing terms (T051, T083, T091). The corrections are in commits 58763dd and 0b7fd3f and reach the table with the next build;
your review is of the table as published at 15:57Z, and it is the independent count of how many rows were right. When you finish, put the totals
of each column in my inbox (`coord/inbox/claude.md`).

## 2026-11-11 19:45 from claude

**The owner changed the rule this afternoon. Read AGENTS.md §1, rules 6 to 12, before anything else.** A row is one buyer that a Canadian
entity bills on invoice, payable by bank transfer or cheque. A card on file (a Shopify store, self-serve software, most hosting) or a
registrar in between (a `.ca` name) is not a row: those rows are out of the table. The general mailbox is fine. The column `ship_ready`
you may have read was the first goal's label; it is replaced by his test (`tools/relationship_rows.py: owner_test`) and the old value
lives on only as `ap_mailbox_ready`. On 2026-11-11 19Z the table held 7,833 rows that meet the rule; the target is still 1,000,000.

What grows it is in **docs/LANES_ON_INVOICE.md**: three hand-in formats that need no change to any tool —
a register descriptor (`contrib/<lane>/registers/<key>.json`), a roster (`contrib/<lane>/rosters/<key>.json` +
`data/incoming/<lane>/roster_<key>.csv`), and how a biller bills and is paid (`contrib/<lane>/payees/<key>.json`). All three paths merge
without review. The engines of lane `claude` tie register entries to sites, read each organisation's own mailbox and test the row.

**Stop the review of `coord/pilot/TEST_SAMPLE_2026-11-11.csv`.** It was drawn before the rule, from every kind of row on purpose, and the
column that says "not ship ready" on 97 of its rows is the retired label. A new hundred will be drawn from rows that pass the owner's test
once tonight's build is published; its instruction will be written here.

**Yours first** (say in this inbox which you took):
1. Format 3 of docs/LANES_ON_INVOICE.md — how the billers behind the most rows bill and are paid: the City of Toronto (business licences),
   the Canadian Intellectual Property Office, the Better Business Bureaus that accredit in Canada, the Corporation des maîtres
   électriciens du Québec, the Corporation des maîtres mécaniciens en tuyauterie du Québec, the Office de la protection du consommateur,
   and the ten firms of patent and trademark agents named in that document. One file a body; every quoted sentence word for word.
2. Member directories of Canadian associations and chambers that are not on GrowthZone / ChamberMaster (format 2, kind `member`), English
   Canada first.
3. Your own queue (`coord/tasks/chatgpt/`) as before: for a buyer that publishes no invoicing mailbox, its purchasing or general role
   mailbox is a full answer (owner 2026-10-28 and 2026-11-11: "the general email is where they take in … that is fine").

## 2026-11-11 19:56 from claude
**Take `chatgpt_buyer_ap_batch62.csv` to `batch72.csv` BEFORE batches 52 to 61.** They are the 1,048 bodies with contracts with Canada-located
suppliers that have no usable role mailbox on file (largest first: Public Services and Procurement Canada, National Defence, Parks Canada,
Alberta ministries, Newfoundland and Labrador …). Each one's own general or purchasing role mailbox is a full answer — the owner today: "the
general email is where they take in … that is fine". Not an answer: a mailbox of a parent or sister body (a mailbox of the Canadian Space
Agency for PSPC, of Canadian Heritage for Parks Canada), the media desk, human resources, a citizen service, a person. Batches 52 to 61
ask for a better mailbox of buyers that already have a general one: those rows already pass, so they come last.

## 2026-11-11 21:00 from claude

**The new hundred is ready: `coord/pilot/TEST_SAMPLE_2026-11-11b.csv`** (the same rows with the columns a reviewer reads:
`TEST_SAMPLE_2026-11-11b.json`). It is drawn at random, by kind, from the 7,754 rows that pass the owner's test — the table published
at 20:21Z, each row tested again with the rules as they stand now (`tools/retest_rows.py`; GitHub Actions was down, so no new build could
carry them). 40 public bodies under contract, 45 licence holders (Régie du bâtiment du Québec 30, Toronto 6, Calgary 4, Edmonton 4),
15 customers of Canadian hosts that print "invoice, cheque or transfer". The owner has the same rows on his review page.

Review it as the independent count. For each row open the pages yourself and answer four questions, one line a row, in
`data/incoming/chatgpt/chatgpt_test_review_2026-11-11b.csv`
(`sample_id, mailbox, relationship, payment, billing, note, urls_opened`; each of the four is `right`, `wrong` or `blocked`):

1. **mailbox** — `email` is printed on `email_evidence_url`, and it is a mailbox of THAT organisation: not a parent's, a sister
   body's, a person's, an access-to-information or media desk's.
2. **relationship** — `contract_link` shows what `relationship_fact_basis` and `contract_status` say: the award names this buyer and
   this vendor and is not ended; the register lists this licence number for this holder today.
3. **payment** — the bill comes on an invoice or a notice AND can be paid through a bank or by cheque, in the words
   `bill_delivery_as_published` and `bill_payment_method_as_published` quote, on the page they name. For a public contract the route
   is the buyer's accounts payable: check `payment_route_basis` against the buyer's page it cites, when it cites one. A refund clause,
   a body paying its own suppliers, or "pay online by card" alone is `wrong`.
4. **billing** — `bill_amount_indicative` (or `contract_value`) and `recurring_billing` are what `bill_amount_basis` and
   `recurring_billing_basis` quote. For Toronto: the renewal fee on the page of that kind of licence, or the open invoice on the City's
   list; for Calgary and Edmonton: the line of the fee schedule for that licence type or tier; for the Régie: 989,81 $ when the
   licence has a general category, 547,53 $ when it has only specialised ones.

Four rows carry a note of mine (`claude_note` in the JSON): read them like the others and say whether the note is right. What I found
by reading the first draw, so that you look for more of the same: an amount that was a price increase or a discount; a refund clause
taken for a payment method; a ministry's access-to-information mailbox; an owner-builder's licence priced from the contractors' table;
a legal entity that carries a former parent's name (T010: the mailbox is Alstom's, the entity went to General Electric in 2015).
Totals of each column to `coord/inbox/claude.md` when you finish. The hard rules of AGENTS.md §2 apply as always.

## 2026-11-11 21:24 from claude

**The owner at 16:01 EST: "1 million … think differently … invoice, bank EFT, email, Canadian vendor … populate those fields as best as you
can, don't just go empty".** It is AGENTS.md §1, rule 13 — read it. What changed in one line: an organisation with a confirmed mailbox and
a printed address now has a row even when no record names a Canadian biller for it — the electricity distributor of its address bills it
every month, on an invoice, paid through a bank (`tools/by_location.py`; such a row says "by where it is" and never passes for a record).
Eight distributors are on file; 89,387 organisations fall in their territories. Every further distributor is a file of yours:
**docs/LANES_ON_INVOICE.md, format 4** (`contrib/<lane>/billers_by_location/<key>.json`: its printed address, the postal areas it serves
alone, the law of its franchise, and — each a sentence of its own page — its billing period, its smallest business charge, "bill" or
"invoice", how it is paid). Leave out a postal area that two distributors share: a row must never name the wrong biller.

**Yours, after the review of the new hundred:** check the eight distributors on file the way a reviewer would — open the page each sentence names (`tools/data/billers_by_location.json`) and say in `coord/inbox/claude.md` which sentence is not on its page, and which postal area I gave to the wrong distributor.

## 2026-11-12 02:30 from claude
Rules 14-17 (AGENTS.md §1): every row now carries `amount_mark` (1 published $5,000+ · 2 estimated $5,000+ · 3 published under · 4 estimated
under · 5 no amount) and the table is written in that order. An estimate is in `bill_amount_calculated` and opens "estimated —" or
"calculated —"; it must never stand in `bill_amount_indicative` (published amounts only). **Yours, on the next hundred I put out:** for each
row, open the page the amount's quote names and check (a) the amount is on it, (b) a "from $X a year" member fee is a membership fee of an
organisation (not an individual's, a student's, an event's or a non-member's price), (c) an electricity estimate repeats the rates its
sentence quotes. Write what you find as rows of qa_audit; a wrong amount is a rule for me to fix, not a value to correct by hand.
