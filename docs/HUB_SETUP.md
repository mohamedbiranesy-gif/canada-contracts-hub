# Setup — what runs by itself, and the few clicks it needs

| Who | What it does | Runs by itself? | One-time setup |
|---|---|---|---|
| **Gemini researcher** (GitHub Actions) | Finds invoicing contacts and vendor contacts with evidence, 4 runs a day. Alternates between the Québec queue and the rest of Canada + US queue | Yes | Secret `GEMINI_API_KEY` (done) |
| **Jules** (Gemini coding agent) | Builds a new data source twice a day and opens a pull request | Yes | Secret `JULES_API_KEY` (done) |
| **Referee** (plain code) | Re-opens every evidence page, keeps only what is really there, merges data automatically, updates the board | Yes | None |
| **Rebuild** (plain code) | Daily. Moves the reference date to today, applies everything verified, republishes the dataset, drops contracts that have ended | Yes | None |
| **Codex** (ChatGPT coding agent) | Reviews every pull request automatically. Builds sources when started | Reviews: yes. Building: see below | Turn on automatic reviews (below) |
| **Claude** | Integrator: merges code changes, refills queues, fixes tools | When your Claude usage allows | Optional (below) |

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
