# PROTOCOL.md — Claude lane, operating protocol (refreshed 2026-11-08 from primary sources)

Scope: the ranked buyer deliverable (`coord/results/ranked/`) measured against the downstream team's per-package coverage
targets. Reread at every milestone and after any context reset, together with PLAN.md and STATE.md.

## Sources read (2026-11-08) and what changed
- platform.claude.com … /claude-prompting-best-practices and /prompting-claude-fable-5-1 (fetched 2026-11-08): "Never artificially
  stop any task early"; batch independent tool calls; "Never guess a parameter"; "Consider the reversibility and potential impact";
  before state-changing commands make sure "the evidence actually supports that specific action"; close every turn with a recap that
  stands alone; state assumptions; "say exactly what you left out and why"; keep thinking/history append-only. Nothing supersedes
  the owner's prompt; the pages add "don't stop because the session is long" and "report out-of-scope findings as follow-ups".
- code.claude.com/docs/en/best-practices (fetched 2026-11-08): "Claude stops when the work looks done. If it has nothing to run that
  tells it whether the work actually is done, 'looks done' is all it has to go on" → every deliverable here has a pass/fail check
  (CHECKS.json); ask for evidence (command + output), review by a subagent that did not see the conversation for high-stakes work.
- anthropic.com/engineering/effective-context-engineering-for-ai-agents: context is finite; keep state in files (NOTES.md etc.),
  clear old tool output, give subagents self-contained briefs and take back condensed reports.
- github.com/obra/superpowers verification-before-completion: "NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE";
  "should / probably / seems to" are signals to go and check.
- github.com/anthropics/skills skill-creator: instructions are written for a reader with no context; name the trigger and the
  output format; keep the file short, put the detail in referenced files.

## Domain rules this work must satisfy (binding; AGENTS.md §2 + owner's orders)
1. Vendor in Canada only from the source's own field or the vendor's own site. Never from the name.
2. Evidence or nothing: URL opened + retrieval date + quote ≤ 300 chars containing the value. Blank = `not_published`.
3. Organisational role mailboxes only; never a named person's mailbox; never pattern-built; no webmail. Owner 2026-11-08 10:59 EST:
   a named AP contact PERSON is allowed in `ap_contact_name_as_published` when the organisation itself publishes it on its AP / finance
   page (name + role phrase, quoted); the mailbox columns are unchanged.
4. No getting around blocks: 401/403/429/CAPTCHA/login/robots → `blocked`; no proxies; never automate the CRA GST registry.
5. ≤ 2 requests/s per host, identified UA, cache everything. Two engines on one host = 1 req/s each.
6. Nothing AI-written as a value: AI agents only propose URLs (leads); every value is read from the page by a Mac engine.
7. Never silently drop data; never git stash/rebase/checkout in the live Mac clone (push_loop v3 owns pushing).
8. Columns are append-only for the downstream team: new columns, never renames.

## Expert sign-off checklist (before any build is called "better")
- [ ] `COVERAGE_VS_TARGETS.md`: benchmarks met went up or a ceiling is documented; `coverage_history.csv` shows the delta.
- [ ] `VALIDATION.md` all gates pass; `AUDIT.md` PASS (no named person, no pattern mailbox, every value has provenance).
- [ ] Gold count did not fall without a logged reason (`CHANGELOG.md`, `rows_changed.csv`).
- [ ] A random sample of 10 new values re-opened by hand (URL shows the quote).
- [ ] Mac engines alive (`ps`), push_loop pushed within the last 30 min, Downloads folder refreshed.

## Verification method per deliverable → CHECKS.json
