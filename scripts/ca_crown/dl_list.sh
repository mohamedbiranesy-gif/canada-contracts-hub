#!/bin/bash
# usage: dl_list.sh <dir> <links.txt>   (1 request/second, resume-safe)
cd "$1"
while read u; do f=$(basename "${u%%\?*}"); [ -s "$f" ] && continue; code=$(curl -sS -L -A "contracts-research/1.0" -o "$f" -w "%{http_code}" --max-time 90 "$u"); echo "$(date -u +%FT%TZ) $code $(stat -c %s "$f" 2>/dev/null) $u" >> download.log; sleep 1; done < "$2"
echo "$(date -u +%FT%TZ) done" >> download.log
