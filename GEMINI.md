# GEMINI.md
You are **Gemini**, a lead on this team. Read `AGENTS.md` first. It is the binding contract and overrides anything else.

Find your situation below and follow that section.

## A. Gemini app on the owner's Mac (Task mode) — lane `gemini`
This is how you run most of the time. Your folder is `/tmp/canada-contracts-hub`, a clone of
github.com/mohamedbiranesy-gif/canada-contracts-hub.

**What your environment can and cannot do** (learned the hard way; do not test it again):
- Your shell has **no network**. `git push`, `git pull`, `git fetch`, `git clone`, `curl`, `wget`, Python `urllib` /
  `requests` all fail there. Each attempt only burns your quota.
- The **Run Git Push** tool fails here too and keeps asking the owner for approval in a loop. Never call it.
- Your **browse and search tools work**. Read every web page and PDF with them, never from the shell.
- Your shell is for exactly three things: `tools/append_row.py`, `tools/validate_returns.py`, and local `git add` /
  `git commit`.

**Uploading is automatic. You never upload.** Every 30 minutes ChatGPT (on the same Mac, with network) runs
`tools/mac_sync.py`. It takes your rows from disk, committed or not, pushes them to GitHub as a branch
`gemini/sync-<time>`, and the agent-branch workflow merges them into main. The referee then re-opens every evidence page.
The same script copies the latest `AGENTS.md`, `GEMINI.md`, `tools/`, `coord/inbox/` and `coord/tasks/gemini/` into
your folder, because you cannot pull.

**Your loop:**
1. Start of a session: `cd /tmp/canada-contracts-hub && git branch --show-current`. It must start with `gemini/`.
   If it says `main`, run `git checkout -b gemini/work`. If the folder is missing, say so in the chat and stop:
   the next sync re-creates it within 30 minutes.
2. Read `coord/inbox/gemini.md` (newest at the bottom) and do what it asks first. Then look up your own rows in
   `coord/results/verification_log.csv`: outcome `not_found_on_page` means the referee opened your page and the
   value was not there. Fix those rows first (right page and quote, or `not_published`).
3. Pick the batch: the lowest-numbered `coord/tasks/gemini/gemini_verify_*` file, then `gemini_buyer_ap_batchNN.csv`,
   whose task ids are not all present in your results file `data/incoming/gemini/gemini_buyer_ap_results_batchNN.csv`.
   Trust your own results file, not `coord/NEXT.md` (it can lag behind your local rows).
4. Research one task id at a time with your browse/search tools (method: `prompts/gemini_researcher.md` §3 and
   `docs/PLAYBOOK.md`).
5. Save each finding at once (one row per mailbox), with a quoted heredoc so apostrophes are safe:
   ```
   python3 tools/append_row.py buyer_ap data/incoming/gemini/gemini_buyer_ap_results_batchNN.csv - <<'ROW'
   {"task_id": "...", ...}
   ROW
   ```
   If it prints `REJECTED`, fix the row and save it again. Never edit the tools to make a row pass.
6. Every 10 rows:
   ```
   python3 tools/validate_returns.py data/incoming/gemini/gemini_buyer_ap_results_batchNN.csv
   git add data/incoming/gemini coord/inbox docs/PLAYBOOK.md && git commit -qm "[gemini] buyer_ap batchNN rows A-B"
   ```
   That is all. No push.
7. Batch finished: append 3 lines to `coord/inbox/claude.md` (counts found / not_published / blocked, patterns, needs),
   commit, and go straight on to the next batch. Do not stop to ask; the owner is usually away.
8. Usage limit reached: just stop. Everything on disk gets uploaded.

**Never:**
- `git push`, `git pull`, `git fetch`, `git clone`, the Run Git Push tool.
- `git reset`, `git stash`, `git checkout -- <file>` or `git restore`. Files outside `data/incoming/gemini/` change under
  you on purpose: they are refreshed from GitHub. Leave them alone.
- Network calls from the shell (`curl`, `wget`, `python … urllib/requests`).
- Editing anything except `data/incoming/gemini/`, `coord/inbox/` and `docs/PLAYBOOK.md`.

**Quality rules for your rows** (these come from the referee's checks of earlier rows):
- `ap_email` must be literally in `evidence_quote`, and the quote must be literally on `evidence_url` (at most 300
  characters). The referee re-opens the page; a value that is not there is thrown away.
- Some sites show e-mails only in a browser (Cloudflare e-mail protection) or block plain downloads. Save the row
  anyway with the quote you see. The referee then sends it to another agent, and when that agent quotes the same
  value from the same page it counts (`cross_verified`). Never decode protected e-mails yourself.
- A complaints mailbox (`plaintes`), a tender-questions mailbox, or a patient-billing / `comptes.recevables` mailbox is
  **not** an invoicing contact. Mention it in `notes`. Do not put it in `ap_email`.
- `ap_email_type=procurement` is for the purchasing department's own mailbox (`approvisionnement@`, `achats@`,
  `purchasing@`). Use it only when no invoicing / AP mailbox is published.
- `applies_to=parent_central_ap` only when the buyer is part of that parent (for example an installation of a CIUSSS)
  and the parent's page is the one you quote. Say which parent in `notes`.
- **Owner rule (2026-10-28): when a buyer publishes no invoicing/AP mailbox, save its purchasing/procurement role mailbox
  (`ap_email_type=procurement`) or, failing that, its general role mailbox such as info@ / reception@ / greffe@
  (`ap_email_type=general`), with status `found` and a note saying no invoicing mailbox is published.** Still never
  a named person. `not_published` only when the organisation publishes no role mailbox at all.
- One row per mailbox. Do not save the same mailbox twice for the same task id.
- `not_published` only after you have looked at: the "Fournisseurs" / "Faire affaire avec nous" section, the
  invoicing requirements or purchase-order terms PDF ("exigences de facturation", "conditions générales d'achat"), and
  the finance department's contact page. List what you tried in `queries_tried`.
- Never a named person's mailbox, never an address you built from a pattern, never around a CAPTCHA or a login.

## B. Gemini CLI in GitHub Actions — lane `gemini` or `chatgpt`
Your standing orders are in `prompts/gemini_researcher.md`. You can push: `tools/commit_lane.py` does it for you.

## C. Jules — lane `jules`
Your standing orders are in `prompts/jules_builder.md`.

## D. Gemini app with this repo imported, no shell (chat only)
Act as red team and source scout. Read `docs/DATASET_README.md`, `coord/STATUS_BOARD.md` and `docs/SOURCES_COVERED.md`,
then give the owner what is missing or wrong, formatted as lines for `coord/inbox/claude.md` and rows for
`coord/source_registry.csv`.

Your strengths: Google Search, French-language sources (Québec), very long context. Use them.
