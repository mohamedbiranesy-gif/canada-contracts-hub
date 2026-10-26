# Standing orders — Claude (lane `claude`, integrator)

Read `AGENTS.md`. Each run:

1. **Check the inbox and the board.** Read `coord/inbox/claude.md`, `coord/STATUS_BOARD.md` and
   `coord/INGEST_REPORT.md`. Act on every request.
2. **Review PRs waiting on review** (label `needs-review`): code, tools, workflows. Merge the good ones. Comment on the
   rest with exact fixes.
3. **Refill queues.** When a lane has fewer than 3 open batches, generate new ones with `tools/make_batches.py`,
   largest buyers / vendors without contacts first.
4. **Promote new sources.**
   - Take merged `data/incoming/*/records_*.jsonl.gz` and spot-check 10 records per source against their links.
   - Then run the `rebuild` workflow, which patches the dataset release with new records, verified contacts and
     statuses.
5. **Route hard cases.** Rows with status `unclear` or verification failures go to the other lane as `verify_*` tasks.
6. **Improve the machine.** Anything you did by hand twice becomes a tool plus a workflow step.
7. **Report.** Append a summary to every lane's inbox and update `coord/DECISIONS.md` when the method changes.
