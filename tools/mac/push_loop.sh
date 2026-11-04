#!/bin/bash
# push_loop v3 (2026-11-04 06:50) — runs on the owner's Mac as ~/cch-crawler-state/push_loop.sh (this is the tracked copy).
# The engines append into ~/cch-crawler/data/incoming/claude around the clock, so git must NEVER rewrite that working
# tree: v1 (--autostash) and v2 (stash, rebase, pop) both lost rows when a file changed under git, and v2 stalled for
# 40 minutes on "does not match index". v3 never touches the live clone with git: a separate worktree
# (~/cch-crawler-state/pushwt, branch pushwt reset to origin/main every cycle) receives snapshot copies of the live files
# (tools/push_snapshot.py), commits them and pushes pushwt:main. Staged results (engines writing outside the clone) are
# unioned into the live files first (tools/stage_merge.py).
MAIN=~/cch-crawler; WT=~/cch-crawler-state/pushwt; PY=~/cch-crawler-state/venv/bin/python3; T=~/cch-vnews/tools
cd "$MAIN" || exit 1
if [ ! -d "$WT" ]; then
  git fetch -q origin main && git worktree add -q -B pushwt "$WT" origin/main || exit 1
fi
while true; do
  "$PY" "$T/stage_merge.py" >> ~/cch-crawler-state/stage_merge.log 2>&1
  for i in 1 2 3; do
    if ! ( cd "$WT" && git fetch -q origin main && git reset -q --hard origin/main && git clean -qfd data/incoming/claude ); then
      echo "$(date '+%F %T') fetch/reset failed"; sleep 30; continue
    fi
    "$PY" "$T/push_snapshot.py" "$MAIN/data/incoming/claude" "$WT"
    if [ -z "$(cd "$WT" && git status --porcelain data/incoming/claude)" ]; then
      echo "$(date '+%F %T') nothing new"; break
    fi
    if ( cd "$WT" && git add data/incoming/claude && git commit -q -m "[claude] crawler rows (ap_crawler, crawl_some, deep_pages, ap_pages, org_contacts, org_extras) $(date '+%Y-%m-%d %H:%M')

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01DCc3oVZd1LUpWRvxUBvXeg" && git push -q origin pushwt:main ); then
      echo "$(date '+%F %T') pushed"; break
    fi
    echo "$(date '+%F %T') push attempt $i failed"; sleep 30
  done
  sleep 900
done
