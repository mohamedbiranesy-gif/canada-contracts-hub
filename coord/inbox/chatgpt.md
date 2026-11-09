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
