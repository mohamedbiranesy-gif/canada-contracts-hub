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
