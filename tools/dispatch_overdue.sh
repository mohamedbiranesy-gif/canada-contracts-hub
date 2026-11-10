#!/usr/bin/env bash
# Start any workflow that is overdue. GitHub's own timer is best-effort: scheduled runs can be hours late or skipped.
# Called by the hourly `tick` workflow and after every referee run, so the team keeps moving whatever the timer does.
# Usage: bash tools/dispatch_overdue.sh        (needs GH_TOKEN with actions:write)
set -u
now=$(date -u +%s)
check() {  # <workflow file> <max hours since last run> [extra gh args]
  wf="$1"; hours="$2"; shift 2
  last=$(gh run list --workflow "$wf" --limit 1 --json createdAt --jq '.[0].createdAt' 2>/dev/null)
  if [ -z "$last" ] || [ "$last" = "null" ]; then age=9999; else age=$(( (now - $(date -u -d "$last" +%s)) / 3600 )); fi
  busy=$(gh run list --workflow "$wf" --limit 5 --json status --jq '[.[] | select(.status != "completed")] | length' 2>/dev/null || echo 0)
  if [ "$age" -ge "$hours" ] && [ "${busy:-0}" = "0" ]; then
    echo "dispatching $wf (last run ${age}h ago) $*"
    gh workflow run "$wf" --ref main "$@" || true
  else
    echo "ok: $wf (last run ${age}h ago, active runs: ${busy:-0})"
  fi
}
lane=gemini; [ $(( 10#$(date -u +%H) % 2 )) -eq 1 ] && lane=chatgpt
check gemini-researcher.yml 3 -f lane="$lane"
check jules-builder.yml 6
check harvest.yml 24
check rebuild.yml 24
# agent branches waiting to be folded into main (sandboxed agents push <lane>/<name>)
if git ls-remote --heads "https://github.com/${GITHUB_REPOSITORY}.git" 2>/dev/null | grep -qE 'refs/heads/(gemini|chatgpt|jules|codex|claude)/'; then
  echo "dispatching agent-branch.yml (agent branches waiting)"; gh workflow run agent-branch.yml --ref main || true
fi

# ---- the cloud engines (2026-11-10). Their own cron lines fire rarely: in the 4.5 hours after mailbox-crawl.yml was created its hourly schedule
# never fired once, tenant-factory and site-facts each missed two slots. The tick keeps them moving instead. The account runs 20 jobs at a time and
# the referee and the ranker need slots (at 10:35Z the ranker waited behind three engines with 19 jobs), so engines are started in priority order only
# while fewer than MAX_ENGINES engine runs are active (the mailbox crawl counts as one); the
# mailbox crawl (leads -> rows) and the ranker are always started when due.
MAX_ENGINES=3
active() { gh run list --limit 60 --json status,workflowName --jq '[.[] | select(.status != "completed") | select(.workflowName | test("^(mailbox-crawl|row-factory|tenant-factory|credit-scan|site-facts|bbb-accredited|member-live|biz-licences|dns-services|rbq-licences)$"))] | length' 2>/dev/null || echo 0; }
check mailbox-crawl.yml 0
check rank-buyers.yml 2
for spec in "row-factory.yml 3" "tenant-factory.yml 3" "credit-scan.yml 6" "site-facts.yml 6" "bbb-accredited.yml 6" "member-live.yml 6" "biz-licences.yml 12" "tm-register.yml 24" "dns-services.yml 24" "rbq-licences.yml 168"; do
  n=$(active)
  if [ "${n:-0}" -ge "$MAX_ENGINES" ]; then echo "engines active: $n (limit $MAX_ENGINES) — the rest waits for the next tick"; break; fi
  # shellcheck disable=SC2086
  check $spec
done
