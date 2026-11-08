# Brief for Gemini and ChatGPT/Codex — 2026-11-08 (owner's hard deadline: this week)

Read `AGENTS.md` first (binding), then this. Repo: https://github.com/mohamedbiranesy-gif/canada-contracts-hub (public; raw files at
https://raw.githubusercontent.com/mohamedbiranesy-gif/canada-contracts-hub/main/<path>). Live state: `STATE.md`, `PLAN.md` (Plan v2), `NOTES.md`,
scoreboard `coord/results/ranked/COVERAGE_VS_TARGETS.md`, your inbox `coord/inbox/<lane>.md`, your queue `coord/NEXT.md`.

## The goal, in one picture
Every delivered row (`coord/results/ranked/batches/*.csv`, 63,600 rows in 17 packages) is **an invoice a Canadian vendor sends to that buyer**.
The row must carry everything that invoice needs, each value read from a page the organisation itself publishes, with the URL, the date and a
quote of at most 300 characters:
1. **Bill-to**: the buyer's legal name as it publishes it, its billing / invoice address, its GST/HST or business number when printed.
2. **Submit-to**: the invoicing / accounts-payable role mailbox (`factures@`, `comptesapayer@`, `accountspayable@`, `ap@`, `invoices@` …) or the supplier /
   e-invoicing portal, the required format (PDF, one invoice per e-mail, portal upload), the AP system (Ariba, Coupa, Tungsten, Basware …).
3. **References the invoice must quote**: PO rule ("a purchase order number is required"), PO / contract / tender number, buyer's vendor id.
4. **Terms**: payment terms (net 30 …), payment method (EFT / direct deposit / cheque), payment cycle (weekly cheque run …), e-signature platform.
5. **Tax**: the buyer's tax status as published (exempt / registration number), currency.
6. **Follow-up**: AP phone, the AP contact person the organisation itself names on its AP page (allowed since 2026-11-08), requirements text.
**AP grade A** (the standard every row must reach) = referee-confirmed invoicing / AP mailbox on the buyer's own domain, published legal name, billing
address, PO rule and payment terms. Today only 67 of 582 Gold rows are A; the blockers are payment terms (342 Gold rows), PO rule, then legal name.
All packages matter, not only Gold: P02–P05 (contract rows with finance / purchasing / general mailboxes), P06–P10 (client-listing proofs), P13 (50,789
inferred relationships, mostly companies).

## Hard rules (AGENTS.md §2, unchanged)
Vendor in Canada only from the source's own field or the vendor's own site. Buyer named. Evidence or nothing (URL opened + date + ≤300-char quote).
Organisational role mailboxes only — never a named person's mailbox, never pattern-built (a named AP contact PERSON may go in the contact-name column
when the organisation publishes it). No getting around blocks (CAPTCHA / login / 403 → `blocked`). No fabrication: `not_published` with the queries tried
is a valuable answer. ≤ 2 requests / second per host, identified user agent. Never git stash / rebase / checkout in the owner's live clone.

## Where the published facts live (PLAYBOOK.md has more)
- "Doing business with us" / "Suppliers" / "Vendors" / "Accounts payable" pages; **purchase-order terms and conditions** (PDF) — payment terms and the PO
  rule are almost always there; **supplier guides / invoicing requirements**; purchasing bylaws and AP policies (cheque-run cadence, GST number).
- Council / board award reports and bid-results pages: contract value, term, PO / contract / tender numbers, number of bids — for the pair's vendor.
- Québec: CISSS / CIUSSS "Fournisseurs" pages, centres de services scolaires "Services aux fournisseurs", villes "Comptes payables"; SEAO for awards.
- Registries (legal name, address, NEQ / BN): Registraire des entreprises (REQ), Canada's Business Registries, Corporations Canada — already matched
  offline for 11,286 organisations; use them to CHECK a name, not to replace a published one.

## Your slice (so nobody duplicates)
- **Gemini (lane `gemini`, Québec and French-language)**: `coord/tasks/gemini/gemini_buyer_ap_batch*.csv` (1,200 open rows) then
  `gemini_vendor_contacts_batch*.csv`. For every buyer also record payment terms, PO rule, portal, AP phone, invoice address and format in
  `invoicing_requirements_summary` when the page prints them (that is what moves the AP grade). Follow `GEMINI.md` §A exactly: folder
  `/tmp/canada-contracts-hub`, branch `gemini/…`, `tools/append_row.py`, `tools/validate_returns.py`, local commits only — the sync pushes for you.
- **ChatGPT / Codex (lanes `chatgpt` and `codex`, English Canada, US, rest of world)**: start every run with `git pull --rebase` and
  `python3 tools/mac_sync.py` (it uploads Gemini's rows). Then (a) `coord/tasks/chatgpt/chatgpt_verify_buyer_ap_batch*.csv` and
  `chatgpt_buyer_ap_batch*.csv` (1,200 open), (b) `coord/tasks/codex/codex_buyer_ap_batch*.csv` (799 open), (c) **new sources that publish the
  supplier's address or country** (US cities / counties / states / transit agencies / school districts, UK, EU, AU) → records in `docs/SCHEMA.md`
  format under `data/incoming/codex/records_<source>.jsonl.gz` + scraper in `contrib/codex/<source>/` + `notes/<source>.md`; rank by how many NEW
  buyers with a findable AP mailbox a source brings (owner's 30,000-buyer goal). Commit and push every 10 rows; small PRs titled `[lane] what batchNN`.
- Both: when your queue is empty, say which slice you take in `coord/inbox/<other lane>.md` and take it (AGENTS.md §4). Write what you learn to
  `docs/PLAYBOOK.md`. Hard cases → `status=unclear` with notes.

## Output formats
`docs/RETURN_FORMATS.md` is exact. Buyer AP rows: `task_id,buyer_key,org_name_as_found,ap_email,ap_email_type,invoice_portal_url,ap_phone,
invoice_mailing_address,invoicing_requirements_summary,applies_to,evidence_url,evidence_quote,retrieved_date,status,queries_tried,notes`.
Run `python3 tools/validate_returns.py <csv>` before committing. The ingest workflow re-fetches every evidence page: a value that is not on the page
is rejected, so quote exactly what the page shows.

## Cadence
Work continuously; make yourself a recurring task in your app (every 30 minutes) if the app supports it. Report in `coord/inbox/claude.md` at the
end of each run: rows done, what you learned, what blocked you. Never pause or disable your own schedule (AGENTS.md §4).
