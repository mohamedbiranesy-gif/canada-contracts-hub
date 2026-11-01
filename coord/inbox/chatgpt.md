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
