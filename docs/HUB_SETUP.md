# One-time setup (about 15 minutes, then the team runs by itself)

You only do this once. After it, Gemini, Jules, Codex and Claude pick up work on their own schedules, check each
other's work, and keep the dataset growing, whether or not you or Claude are around.

## 1. Gemini — fully autonomous and free (most important)
1. Open **https://aistudio.google.com/apikey** and sign in with your Google account.
2. Click **Create API key** and copy it.
3. Add it to the repo as a secret:
   1. On GitHub, open this repo → **Settings** → **Secrets and variables** → **Actions**.
   2. Click **New repository secret**.
   3. Name: `GEMINI_API_KEY`. Paste the key. Click **Add secret**.
4. Start the first run: **Actions** tab → **gemini-researcher** → **Run workflow**.

From then on it runs every day by itself.

## 2. Jules — Gemini's coding agent (builds new sources)
1. Open **https://jules.google.com** and sign in.
2. Click **Connect to GitHub** and allow access to `canada-contracts-hub`.
3. In Jules **Settings**, open **API keys**, create a key and copy it.
4. On GitHub, add it as the repository secret `JULES_API_KEY` (same steps as above).
5. **Actions** → **jules-builder** → **Run workflow**.

From then on it starts twice a day and opens a pull request each time.

## 3. Codex — ChatGPT's coding agent (builds sources, reviews everyone's work)
1. Open **https://chatgpt.com/codex**.
2. Connect GitHub and choose `canada-contracts-hub`.
3. Create an environment. In its settings, turn **Internet access** on and allow all domains.
4. Turn on automatic reviews: Codex **Settings** → **Code review** → **Automatic reviews** for this repo.
   Codex then reviews every PR that Gemini, Jules or Claude opens.
5. Start a task. Paste the text of `prompts/codex_kickoff.md`.
6. When the task finishes, click **Create PR**. The referee merges it automatically if it only adds data.

Optional, fully hands-off: if you have an OpenAI **API** key with credit, add it as the secret `OPENAI_API_KEY`. The
`codex-builder` workflow then runs Codex every day without you.

## 4. ChatGPT agent mode (browsing-heavy research)
1. In ChatGPT, turn on **Agent mode**.
2. Paste `prompts/chatgpt_agent.md`, with the batch number from `coord/NEXT.md` (lane chatgpt).
3. Upload the CSV it returns to the folder `data/incoming/chatgpt/`: **Add file** → **Upload files** → **Commit**.

The referee verifies every row automatically.

## 5. Claude (optional; when your Claude usage allows)
If you have Claude Code on a computer:
1. Run `claude setup-token` and copy the token.
2. Add it as the repository secret `CLAUDE_CODE_OAUTH_TOKEN`.

Then `@claude` works in any issue or PR, and a weekly integrator run happens automatically.

## Compute budget
The repo is **public**, so GitHub Actions minutes are unlimited and free:
- Gemini researches every 6 hours;
- the SEAO end-date harvester runs daily;
- the referee runs on every change.

The real limits are each AI's own quota (free Gemini API tier, Jules daily tasks, your ChatGPT/Claude plans). When a
quota runs out, a run stops early but saves what it did, and the next run continues.

Secrets (API keys) stay private even in a public repo. Never paste a key into a file, issue or comment; only into
**Settings → Secrets**.

## Where to watch
- `coord/STATUS_BOARD.md` shows progress.
- `coord/inbox/` shows the agents talking to each other.
- **Actions** shows every run.
- **Pull requests** shows contributions and reviews.
