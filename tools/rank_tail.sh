#!/usr/bin/env bash
# Everything a rank build does after the table is written to out/ranked/ (ranked_buyers.csv.gz, .jsonl.gz) and rank.log exists: the package
# batches, the integrity gates, the reports, the release "ranked-latest", the commit of the reports. Used by both workflows: rank-buyers.yml
# (one process) and rank-buyers-parts.yml (the table put together from parts by tools/rank_merge.py). Needs GH_TOKEN. Run from the repository root.
#
# Disk (2026-11-10, measured): a row is 15 KB as plain CSV. A build used to hold the previous table as plain text, the new table as plain
# text, the packages and a working copy of the packages — ~65 KB a row, 11 GB at 170,000 rows (a runner has 85 GB free: build 15:47Z). Now: tables
# compressed only, package working parts removed as they are written — the packages (15 KB a row) are the only plain text left.
set -e
df -h / | tail -1 | sed 's/^/disk after ranking: /'
# the change list against the previous build (coord/results/ranked/ranked_buyers.csv.gz, put there by tools/rank_prep.sh) — before the publish
# step replaces that file with this build's table
python3 tools/release_diff.py coord/results/ranked/ranked_buyers.csv.gz out/ranked/ranked_buyers.csv.gz out/ranked > release_diff.log 2>&1 || echo "::warning::change list not made (see release_diff.log)"
head -6 release_diff.log || true
if grep -q "downstream pack skipped" rank.log; then echo "::error::downstream pack skipped — build not published (the previous build stays)"; grep -A3 -B3 "downstream pack skipped" rank.log; exit 1; fi
rm -rf out/ranked/batches && python3 contrib/claude/rank_buyers/batches.py > batches.log
python3 tools/validate_deliverable.py out/ranked --mx data/incoming/claude/claude_mx_check.tsv --write out/ranked/VALIDATION.md > validate.log || true
python3 tools/dmarc_report.py out/ranked > dmarc.log || true
python3 contrib/claude/rank_buyers/contracts_export.py > contracts.log || true
python3 tools/audit_deliverable.py out/ranked --write out/ranked > audit.log || true
python3 tools/coverage_targets.py --write out/ranked --history coord/results/coverage_history.csv > coverage.log 2>&1 || true
[ -s out/ranked/COVERAGE_VS_TARGETS.md ] || { echo "::warning::scoreboard not written (see coverage.log) — previous scoreboard kept"; cp coord/results/ranked/COVERAGE_VS_TARGETS.md out/ranked/ 2>/dev/null || true; }
python3 tools/growth_report.py --ranked out/ranked/ranked_buyers.csv.gz --coverage-json out/ranked/coverage_vs_targets.json --baseline coord/BASELINE_SHIP_NOW_2026-11-09.json --write coord/GROWTH_VS_BASELINE.md --history coord/growth_history.csv --label "$(git rev-parse --short HEAD)" > growth.log 2>&1 || echo "::warning::growth report failed (see growth.log)"
df -h / | tail -1 | sed 's/^/disk before publish: /'
if python3 tools/ranked_publish.py out/ranked --tag ranked-latest --git-dir coord/results/ranked > publish.log 2>&1; then
  tail -3 publish.log
else
  echo "::error::release publish failed — nothing committed (a table of this size cannot go to git)"; tail -20 publish.log; exit 1
fi
{ echo "# Ranked buyers — $(date -u +%Y-%m-%dT%H:%MZ)"; echo; echo '```'; cat rank.log batches.log; echo; echo "# coverage vs the downstream targets (COVERAGE_VS_TARGETS.md)"; cat coverage.log; echo '```'; echo; echo "Integrity gates: see VALIDATION.md in this folder; columns and rules: contrib/claude/rank_buyers/README.md"; } > coord/results/ranked/SUMMARY.md
python3 tools/lane_status.py --write coord/LANES.md > /dev/null 2>&1 || true
git config user.name "ranker-bot"; git config user.email "ranker-bot@users.noreply.github.com"
git add coord/results/ranked coord/results/coverage_history.csv coord/GROWTH_VS_BASELINE.md coord/growth_history.csv coord/LANES.md
git add -A -- 'data/incoming/claude/claude_dmarc_check*.tsv'   # written in parts (tools/dmarc_check.py)
[ -e data/incoming/claude/claude_site_owner_wd.csv ] && git add data/incoming/claude/claude_site_owner_wd.csv || true
if git diff --cached --quiet; then echo "nothing to commit"; exit 0; fi
git commit -q -m "ranker: buyers re-ranked into quality batches [skip ci]"
# no file over GitHub's limit may be in the commit (2026-11-10: a table of 151 MB that had stayed tracked made every push fail for an hour)
big=$(git diff-tree --no-commit-id -r --name-only HEAD | while read -r f; do [ -f "$f" ] && [ "$(stat -c %s "$f")" -gt 95000000 ] && echo "$f"; done || true)
if [ -n "$big" ]; then echo "::error::file(s) over 95 MB in the ranker's commit — not pushed: $big"; exit 1; fi
for j in 1 2 3 4 5 6 7 8 9 10; do  # the commit touches only the ranker's own files: put it on top of whatever landed meanwhile and push again
  git fetch -q origin main && git rebase -q --autostash origin/main || { git rebase --abort 2>/dev/null; echo "::error::the ranker's commit does not apply on main"; exit 1; }
  git push -q origin HEAD:main && { echo "pushed"; exit 0; }
  sleep $((j * 5))
done
echo "::error::the ranker's commit could not be pushed"; exit 1
