#!/usr/bin/env bash
# What a rank build does before the table is ranked (rank-buyers.yml and rank-buyers-parts.yml): the previous table (from the release
# "ranked-latest"), the DNS posture of the mailbox domains not checked yet, whose site a client listing is on.
# Run from the repository root; needs GH_TOKEN and dnspython. Never fails the build: a table it could not refresh is used as it is on main.
set -u
python3 tools/ranked_io.py assemble || true
PREV=coord/results/ranked/ranked_buyers.csv.gz   # read compressed: as plain text it is 15 KB a row (2.6 GB at 170,000 rows) — see docs in rank_tail.sh
[ -s "$PREV" ] || PREV=""
# DNS posture (DMARC / SPF / MTA-STS / TLS-RPT / BIMI) for mailbox domains not yet checked: new mailboxes arrive every build. The tool stops by
# itself after 18 minutes and writes what it checked (it also writes every 5,000 domains); `timeout` is only the backstop.
# shellcheck disable=SC2046
timeout 22m python3 tools/dmarc_check.py --repo "$PWD" --recheck-days 30 --workers 128 --minutes 18 $PREV \
  $(ls data/incoming/*/*results*.csv data/incoming/claude/claude_buyer_leads.csv 2>/dev/null | head -400) > dmarc_check.log 2>&1 || true
tail -2 dmarc_check.log
# whose site a client listing is on (tools/site_owner_wd.py): Wikidata's official-website statements for the sites not asked yet.
# The query service allows one query a minute (100 sites each): at most 4 minutes a build, the rest at the next build.
if [ -n "$PREV" ]; then
  timeout 6m python3 tools/site_owner_wd.py --ranked "$PREV" --minutes 4 > site_owner.log 2>&1 || true
  tail -1 site_owner.log
fi
df -h / | tail -1 | sed 's/^/disk after prep:    /'
