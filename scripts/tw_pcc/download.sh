#!/bin/bash
dl=downloads/tw_pcc; mkdir -p $dl/award $dl/gpa; log=$dl/download.log
for f in $(cat $dl/award_files.txt | sort -r); do
  [ -s "$dl/award/$f" ] && continue
  curl -sS -L --retry 2 -A "contracts-research/1.0" -o "$dl/award/$f.part" "https://web.pcc.gov.tw/tps/tp/OpenData/downloadFile?fileName=$f" >> $log 2>&1 && mv "$dl/award/$f.part" "$dl/award/$f"
  echo "$(date -u +%FT%TZ) $f $(stat -c %s $dl/award/$f 2>/dev/null)" >> $log
done
for f in $(cat $dl/gpa_files.txt | sort -r); do
  [ -s "$dl/gpa/$f" ] && continue
  curl -sS -L --retry 2 -A "contracts-research/1.0" -o "$dl/gpa/$f.part" "https://web.pcc.gov.tw/tps/tp/OpenData/downloadFile?fileName=$f" >> $log 2>&1 && mv "$dl/gpa/$f.part" "$dl/gpa/$f"
  echo "$(date -u +%FT%TZ) $f $(stat -c %s $dl/gpa/$f 2>/dev/null)" >> $log
done
echo "$(date -u +%FT%TZ) ALL DONE" >> $log
