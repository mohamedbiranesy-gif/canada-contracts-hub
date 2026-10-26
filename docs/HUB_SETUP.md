# Setup — what runs by itself, and the few clicks it needs

| Who | What it does | Runs by itself? | Needs |
|---|---|---|---|
| **ChatGPT** (Codex app on the Mac) | Lane `chatgpt`: invoicing contacts in English Canada + US, vendor contacts, QA. Uploads its own rows and Gemini's (`tools/mac_sync.py`) | Yes: automation "Continue Canada contracts research", every 30 minutes | Mac awake and plugged in, ChatGPT app open, ChatGPT usage left |
| **Gemini** (Gemini app on the Mac, Task mode) | Lane `gemini`: Québec invoicing contacts, then Québec vendor contacts. Saves and commits locally; ChatGPT uploads it | While a Gemini task is running | Gemini app open; restart a task with `prompts/gemini_app_task.md` after a usage reset |
| **Jules** (Gemini coding agent) | Builds a new data source twice a day and opens a pull request | Yes (GitHub Actions) | Secret `JULES_API_KEY` (done) |
| **Referee** (plain code) | Re-opens every evidence page, keeps only what is really there, merges data, updates the board | Yes (GitHub Actions) | Nothing |
| **Rebuild** (plain code) | Daily. Moves the reference date to today, applies everything verified, republishes the dataset, drops contracts that have ended | Yes (GitHub Actions) | Nothing |
| **Gemini researcher** (GitHub Actions) | Same research as the Gemini app, 4 runs a day | Standing by: the free Gemini API key has no Google Search | Billing on the Gemini API key turns it on |
| **Claude** | Integrator: merges code changes, refills queues, fixes tools | When your Claude usage allows | Nothing |

**The Mac matters.** ChatGPT and Gemini only run while the MacBook is awake, plugged in and the two apps are open. Closing
the lid or a dead battery pauses them, and they carry on when the Mac wakes up. A restart empties `/tmp`, so Gemini
loses at most the rows of its last half hour that were not uploaded yet.

## Codex (2 minutes)
1. Open **chatgpt.com/codex** → **Settings** → **Code review**.
2. Turn on **Automatic reviews** for `canada-contracts-hub`.

From then on, every pull request from Jules, Gemini or Claude gets an independent review from ChatGPT.

To make Codex *build* sources by itself too, pick one:
- **Codex app on your Mac:** create an automation, for example "every day, do the task in prompts/codex_kickoff.md on
  canada-contracts-hub and open a PR". It runs while your Mac is awake and the Codex app is open. It uses your ChatGPT
  plan.
- **OpenAI API key:** add the secret `OPENAI_API_KEY`. The `codex-builder` workflow then runs daily in the cloud. API
  usage is billed separately from ChatGPT Plus.
- **Or nothing.** Start a Codex task by hand whenever you like, with the text of `prompts/codex_kickoff.md`.

You do **not** need ChatGPT agent mode. The Gemini researcher already works the ChatGPT queue on alternate runs. If you
ever run agent mode anyway (`prompts/chatgpt_agent.md`), upload its CSV to `data/incoming/chatgpt/`.

## Claude (optional)
Either option works when your Claude usage allows:
- Ask Claude in the app to create the weekly integrator scheduled task.
- Or add the secret `CLAUDE_CODE_OAUTH_TOKEN`, made with `claude setup-token` on a computer with Claude Code. Then
  `@claude` works in issues and PRs.

## More capacity
- **Extra free Gemini keys from the same Google account do not add capacity.** Free-tier limits are per project, and
  creating extra projects or accounts to get around limits breaks Google's terms.
- **For more Gemini throughput:** enable billing on the same Google AI Studio project, then raise the repository variable
  `GEMINI_ROWS_PER_RUN` (default 15).
- **Keys from other providers add whole extra workers:** `OPENAI_API_KEY` for Codex, `CLAUDE_CODE_OAUTH_TOKEN` for
  Claude.

## Watch
- `coord/STATUS_BOARD.md` shows progress.
- `coord/inbox/claude.md` gets automatic health notes when a run saves nothing.
- **Actions** shows every run.
- **Pull requests** shows contributions and reviews.

Keys only ever go in **Settings → Secrets**, never in a file, issue or comment. The repo is public.
