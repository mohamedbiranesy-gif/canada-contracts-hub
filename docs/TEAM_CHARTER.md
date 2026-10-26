# TEAM CHARTER — Claude · Gemini · ChatGPT

## Mission
Build the most complete, verified dataset in existence of **ongoing contracts whose vendor is located in Canada**, each carrying every public fact about the contract, the buyer and the vendor: all identifiers, dates, value, link; vendor legal name, registry numbers, Business Number, derived GST/HST, address, phone, website, role e-mails; buyer address, website, **accounts-payable / invoicing e-mail or portal**, and procurement contact.

## Where we are (details in 02_STATUS_BOARD.md)
- 511,762 contracts, 119,131 vendors, 5,851 buyers, from 82 sources.
- Biggest gaps:
  - buyer AP/invoicing contact (24% of contracts);
  - vendor phone, e-mail and website (~23%);
  - whether "ongoing" is truly ongoing for 305k Quebec contracts, which Claude is fixing via the SEAO API.

## Roles — three leads, no overlap

### Gemini — Lead, Québec & Source Intelligence
Owns, end to end:
1. **Québec buyers' invoicing contacts** — `TASKS/gemini/gemini_buyer_ap_batchNN.csv` (2,097 buyers, 275k contracts). French pages, PDFs, Google.
2. **Source intelligence** (Deep Research) — find every award source we don't have yet (see `05_SOURCE_INTEL_BRIEF.md`). Claude builds the pipelines.
3. **Project red team** — read `DATA/dataset_README.md` + `02_STATUS_BOARD.md` + `04_SOURCES_COVERED.md` with your long context and tell us what we are missing or doing wrong.
4. **Québec vendor contacts** — `TASKS/gemini/gemini_vendor_contacts_batchNN.csv`.

### ChatGPT — Lead, Quality & Rest of North America
Owns, end to end:
1. **Independent quality audit** — `TASKS/chatgpt/chatgpt_qa_audit_batch01-02.csv` (200 records). Open each record's page and check every field. This measures how far the dataset can be trusted.
2. **English-Canada + US buyers' invoicing contacts** — `TASKS/chatgpt/chatgpt_buyer_ap_batchNN.csv` (2,012 buyers, 138k contracts). Agent mode: click through sites, open supplier guides and purchase-order terms PDFs.
3. **Vendor contacts outside Québec** — `TASKS/chatgpt/chatgpt_vendor_contacts_batchNN.csv`.
4. **Source intelligence outside Canada** (Deep Research) — see `05_SOURCE_INTEL_BRIEF.md`.

### Claude — Lead Engineer & Integrator
- Runs the pipelines (82+ sources), registries (Corporations Canada, Quebec REQ, BC OrgBook, RBQ, CRA charities, LEI…), automated vendor website discovery, and the Quebec status truth engine.
- **Verifies every finding you return** by opening the evidence page itself.
- Merges findings into the master dataset with your name as provenance, and updates `02_STATUS_BOARD.md`.
- Writes your next batches and routes your messages to each other.

## How we work together (the synergy rules)
1. **One owner per item.** Only work rows in your own task files; that alone prevents duplicate work.
2. **Verify each other.** Claude re-opens every cited page. When Claude's crawler is blocked from a page, the *other* AI is asked to confirm it, via a `verify_*` task file.
3. **Share what you learn.** Patterns go into `MESSAGES/` (e.g. "every CIUSSS invoices through its central accounts-payable mailbox on the 'Fournisseurs' page"). Claude adds them to `03_PLAYBOOK.md` so everyone gets faster.
4. **Discover → build.** You find sources; Claude engineers them; the status board shows the records they add.
5. **Escalate hard cases.** For ambiguous vendors, conflicting e-mails or unclear evidence, write `status=unclear` with a note; Claude routes it for a second opinion.
6. **Every batch counts.** Return each batch as soon as it's done. A file with 30 solid rows beats a promise of 300.

## Non-negotiable rules
- **Evidence or nothing:** every value comes with the URL of a page you actually opened, the date, and a ≤300-character quote containing the value.
- **Organisational contacts only:** role mailboxes the organisation itself publishes (factures@, comptesapayer@, accountspayable@, ap@, invoices@, finance@, procurement@, info@…). Never a named person's mailbox. Never an address constructed from a pattern.
- **No getting around blocks:** CAPTCHA, bot check, login or "access denied" → record `blocked` and move on.
- **No fabrication:** `not_published`, with the queries you tried, is a valuable answer.
- **Exact formats:** `06_RETURN_FORMATS.md`; run `TOOLS/validate_returns.py` on your file if you can execute Python.
