#!/bin/bash
# usage: stream_one.sh <source_key> <pub_id> <name(e.g. 2026)> 
# Streams the OCP Data Registry jsonl.gz through gunzip + grep prefilter + python structural filter.
set -u
sk=$1; pid=$2; nm=$3
dl=downloads/$sk
mkdir -p "$dl"
url="https://data.open-contracting.org/en/publication/$pid/download?name=$nm.jsonl.gz"
echo "$(date -u +%FT%TZ) START $sk $pid $nm $url" >> "$dl/stream.log"
# prefilter: only lines that mention a Canada-like token or a bare "CA"/"CAN" string value
curl -sS -L --retry 3 -A "contracts-research/1.0" "$url" 2>>"$dl/stream.log" \
 | gunzip -c 2>>"$dl/stream.log" \
 | tee >(wc -l > "$dl/lines_total_$nm.txt") \
 | grep -a -i -E 'canad|kanada|канада|加拿大|カナダ|캐나다|"CA"|"CAN"|"CDN"' \
 | tee >(gzip -c > "$dl/prefiltered_$nm.jsonl.gz") \
 | python3 -I scripts/ocp_registry/ocds_filter.py --out "$dl/matches_$nm.jsonl" --stats "$dl/stats.jsonl" --label "$sk:$nm" 2>>"$dl/stream.log"
echo "$(date -u +%FT%TZ) END $sk $pid $nm total_lines=$(cat "$dl/lines_total_$nm.txt" 2>/dev/null) matches=$(wc -l < "$dl/matches_$nm.jsonl" 2>/dev/null || echo 0)" >> "$dl/stream.log"
