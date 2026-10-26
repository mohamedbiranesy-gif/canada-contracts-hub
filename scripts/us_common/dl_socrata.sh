#!/bin/bash
# usage: dl_socrata.sh <domain> <id> <outfile>
UA="contracts-research/1.0"
d=$1; id=$2; out=$3
echo "$(date -u +%FT%TZ) START https://$d/api/views/$id/rows.csv?accessType=DOWNLOAD -> $out" >> "$out.log"
curl -sS -L -m 3000 -A "$UA" "https://$d/api/views/$id/rows.csv?accessType=DOWNLOAD" -o "$out" 2>> "$out.log"
rc=$?
echo "$(date -u +%FT%TZ) END rc=$rc size=$(stat -c %s "$out" 2>/dev/null) lines=$(wc -l < "$out" 2>/dev/null)" >> "$out.log"
