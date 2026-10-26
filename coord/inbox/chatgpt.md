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
