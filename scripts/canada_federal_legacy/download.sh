#!/bin/bash
# Downloads CanadaBuys legacy files (resume + retry). Run from anywhere.
D=downloads/canada_federal_legacy
LOG=$D/download.log
for u in https://canadabuys.canada.ca/opendata/pub/2009-2023-contractHistoryHistorical-contratsOctroyesHistorique.csv https://canadabuys.canada.ca/opendata/pub/2012-2022-awardNoticeHistorical-avisAttributionHistorique.csv; do
  f=$D/$(basename "$u")
  for i in 1 2 3 4 5 6; do
    echo "$(date -u +%FT%TZ) start $u attempt $i" >> $LOG
    curl -sS -L -C - -A "contracts-research/1.0" --retry 3 -o "$f" "$u" >> $LOG 2>&1 && { echo "$(date -u +%FT%TZ) done $u $(stat -c %s $f)" >> $LOG; break; }
    sleep 10
  done
done
