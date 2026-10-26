# Decisions log (append; newest at the bottom)

## 2026-10-26 from claude
- **GitHub repo as the shared brain.** Code, docs, queues, inboxes and verified results live in git. Big data lives in
  release assets (`dataset-latest`, `harvest-state`).
- **The verifier is code, not an AI.** `tools/ingest_results.py` re-fetches every evidence page. Only values that
  appear on the cited page enter `coord/results/`. Nobody, including Claude, can merge an unverified contact.
- **Data-only PRs auto-merge after validation**, so the team never waits on a human. Code, tool and workflow changes
  need a review.
- **Lanes are disjoint** (see AGENTS.md §4), so agents can run in parallel without coordination overhead.
- **Reference date** for "ongoing" stays 2026-10-25 until the rebuild workflow advances it (coord/config.json).

## 2026-10-26 from claude
- **SEAO API yield is low.** Of 8,600 notices fetched (newest first), only ~1-2% expose a planned end date
  (`datePrevueFinContratUtc`) or duration. The harvest continues daily (free on a public repo), but the 305k Québec
  "ongoing_inferred" records need a better public signal. Open question for the Gemini red team.
- **First rebuild (2026-10-26)** applied vendor-website discovery and BC OrgBook extraprovincial registrations:
  - vendor website: 116,394 → 127,981 records;
  - registry match: 380,868 → 401,879 records;
  - 70 SEAO records got explicit end dates.
- **How Claude sessions publish data.** They cannot create releases, so they push to the `data-upload` branch. The
  `publish-data` workflow joins the parts, checks SHA-256, publishes the releases and deletes the branch.

## 2026-10-26 from claude
- The free Gemini API key has no web search (Google's free tier: search grounding "not available" for Gemini 3+, and
  2.5 is closed to new keys). The scheduled `gemini-researcher` therefore stands by. It checks each run and starts
  working automatically the day the key's project gets billing.
- **Invoicing-contact research is done by the search-capable agents the owner runs from his subscriptions:**
  - Antigravity (Gemini, on his Mac): lane `gemini` (Québec). It pushes rows directly.
  - ChatGPT agent mode: lane `chatgpt` (rest of Canada + US). CSV uploaded to `data/incoming/chatgpt/`.
- **New sources:**
  - Jules: automatic, every 6 h and right after each merged task;
  - Codex: started from ChatGPT; opens PRs.
- If billing is enabled later, give the scheduled researcher a lane Antigravity is not working on (`--lane chatgpt`).
