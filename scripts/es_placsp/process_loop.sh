#!/bin/bash
# Waits for each zip from download.sh, extracts Canadian-winner entries, then deletes the zip (disk is scarce).
dl=downloads/es_placsp
while true; do
  done_all=$(grep -c "ALL DONE" $dl/download.log 2>/dev/null)
  for z in $(ls $dl/*.zip 2>/dev/null); do
    python3 -I scripts/es_placsp/extract.py "$z" --out $dl/matches.jsonl --log $dl/extract.log && rm -f "$z"
  done
  [ "$done_all" = "1" ] && [ -z "$(ls $dl/*.zip 2>/dev/null)" ] && break
  sleep 20
done
echo "$(date -u +%FT%TZ) LOOP DONE" >> $dl/extract.log
