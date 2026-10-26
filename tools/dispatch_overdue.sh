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
