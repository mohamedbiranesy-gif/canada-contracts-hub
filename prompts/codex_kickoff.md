# Codex — paste this as a task in Codex (chatgpt.com/codex) with this repo selected

You are Codex, the ChatGPT-family coding agent and lead of lane `codex` on a three-AI team (Claude, Gemini, ChatGPT).
Read `AGENTS.md` first; it is binding.

1. **Pick a source.** Read `coord/inbox/codex.md` and `coord/source_registry.csv`. Take the highest-priority source
   with `lane=codex` and `status=todo`.
2. **Build it, following AGENTS.md §5 and §7.**
   - Bulk file or API first; test on a sample.
   - Scraper in `contrib/codex/<source_key>/`.
   - Records in `data/incoming/codex/records_<source_key>.jsonl.gz`, SCHEMA.md layout. Keep only rows where the
     source's vendor country / address field is Canada. Status computed against `coord/config.json`.
   - Notes in `notes/<source_key>.md` with counts.
3. **Validate.** Run `python3 tools/validate_records.py` on your output and fix every problem.
4. **Open a PR** `[codex] source <source_key>`. Update that row of `coord/source_registry.csv` to `done` / `blocked`.
5. **Report.** Append what you did and learned to `coord/inbox/claude.md`. Add new candidate sources you discovered
   to `coord/source_registry.csv`.

If internet access is off in this environment, say so in your report and instead build the scraper with tests against
saved sample responses. The scheduled workflow will run it.
