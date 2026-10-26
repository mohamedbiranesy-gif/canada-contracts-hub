#!/usr/bin/env bash
# Commit an unattended AI run's output to main, keeping only that lane's allowed paths.
# Usage: bash tools/commit_lane.sh <lane> "<message>"      (needs GH_TOKEN; run from repo root)
set -uo pipefail
LANE="$1"; MSG="$2"
ALLOWED="^(data/incoming/${LANE}/|contrib/${LANE}/|notes/|coord/inbox/|docs/PLAYBOOK\.md$)"
git config user.name "${LANE}-bot"; git config user.email "${LANE}-bot@users.noreply.github.com"
# drop everything outside the lane's allowed paths (protects workflows, tools, other lanes)
git status --porcelain --untracked-files=all | sed 's/^...//' | while read -r f; do
  [[ "$f" =~ $ALLOWED ]] && continue
  if git ls-files --error-unmatch "$f" >/dev/null 2>&1; then git checkout -- "$f"; else rm -f "$f"; fi
done
for f in $(git status --porcelain --untracked-files=all | sed 's/^...//' | grep -E "^data/incoming/${LANE}/.*\.csv$" || true); do
  python3 tools/validate_returns.py "$f" || echo "::warning::validation problems in $f (rows failing checks are ignored by the verifier)"
done
git add -A data/incoming/"$LANE" contrib/"$LANE" notes coord/inbox docs/PLAYBOOK.md 2>/dev/null
if git diff --cached --quiet; then echo "nothing to commit"; exit 0; fi
git commit -q -m "$MSG"
git remote set-url origin "https://x-access-token:${GH_TOKEN}@github.com/${GITHUB_REPOSITORY}.git"
for i in 1 2 3 4 5; do
  git pull -q --rebase origin main && git push -q origin HEAD:main && break
  sleep $((i * 7))
done
gh workflow run verify-and-merge.yml --ref main || true
