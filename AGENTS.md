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

You are a **lead**, not a worker. Your queue tells you where to start. If you see a better method, a missing source
or a bug, act on it: do it, write it down (section 6), and tell the others.

## 2. Hard rules (break one and the whole contribution is rejected by the verifier)
1. **Vendor in Canada** = the source's own vendor country / address field says Canada. Never infer it from the name.
2. **Buyer must be named.** No "undisclosed client".
3. **Ongoing** = start <= reference date and published end date >= reference date (reference date: `coord/config.json`).
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
| `gemini` | Gemini CLI (scheduled in GitHub Actions) and Gemini chat | Québec buyers' AP/invoicing contacts (`coord/tasks/gemini/gemini_buyer_ap_*`), then Québec vendor contacts, French-language sources |
| `jules` | Jules (Gemini coding agent) | Building new source pipelines from `coord/source_registry.csv` (status `todo`), heavy harvest shards |
| `chatgpt` | ChatGPT agent mode | Independent QA audit, English-Canada + US buyers' AP contacts (`coord/tasks/chatgpt/`), vendor contacts outside Québec |
| `codex` | Codex (ChatGPT coding agent) | New source pipelines outside Canada (US states/cities, EU, UK, AU, IGOs, private-sector disclosures), vendor-identifier enrichment code, reviewing every PR |
| `claude` | Claude (integrator, when available) | Merge/rebuild the dataset, registries, write new batches, fix tools, route hard cases |

Rules:
- Work your own lane first.
- When it is empty, or you can add more value elsewhere, write a message to the lane owner's inbox and take a
  clearly separate slice: for example "I'm doing rows 50-100 of chatgpt_vendor_contacts_batch07".
- Never overwrite another agent's results.

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
   - **Auto-merge** happens when the PR touches only `data/incoming/**`, `contrib/**`, `notes/**`, `coord/inbox/**`
     and `docs/PLAYBOOK.md`, and validation passes.
   - Any other path (tools, scripts, workflows) waits for review by another agent or the owner.
5. After merge, the ingest workflow does the rest:
   - re-fetches every evidence page;
   - keeps only verified values in `coord/results/`;
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
