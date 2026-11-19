# worker/ — the Oracle Cloud machine that does the harvesting

Owner, 2026-11-19: the work runs on a cloud machine, not on his computer and not on GitHub Actions (GitHub switched Actions
off on the account on 2026-11-13 because of the crawling; its terms bar that use, and its terms allow one free account per person).

- **Machine:** one Oracle Cloud "Always Free" VM (Ubuntu 24.04, VM.Standard.A1.Flex, 2 OCPU / 12 GB, home region Toronto),
  created with `worker/cloud-init.yaml` (the owner puts his fine-grained GitHub token, this repository only, Contents read/write,
  into it; the token never leaves the machine).
- **Loop:** every 10 minutes the machine resets its checkout to `origin/main` and runs `worker/run.sh`:
  `runner.py` starts the jobs of `worker/jobs.json` that are due (each detached, own log, own output folder, at most
  `max_parallel` at once), then `publish.py` force-pushes everything the jobs wrote to the branch **`worker-results`**
  (one commit, the latest state; `_status/status.json` = the machine and every job's last lines).
- **Steering = editing this repository.** Add or change a job in `worker/jobs.json` and its script in `worker/jobs/`; the machine
  picks it up within 10 minutes. `worker/STOP` stops new job starts. Nothing listens on the machine; nobody logs in to it.
- **Job contract:** read `CCH_OUT` (published), `CCH_WORK` (kept on the machine), `CCH_CACHE`, `CCH_REPO` from the environment;
  be polite (AGENTS.md §2.9: at most 2 requests per second per host, the project user agent, robots.txt, cache); write files
  atomically; print progress lines.
- **Read the results here:** `git fetch origin worker-results && git show origin/worker-results:_status/status.json`.
