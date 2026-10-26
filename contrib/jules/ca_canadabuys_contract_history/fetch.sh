#!/bin/bash
set -u
DL=downloads/ca_canadabuys_contract_history
mkdir -p "$DL"

curl -sS -L -o "$DL/contractHistoryHistorical.csv" "https://canadabuys.canada.ca/opendata/pub/2009-2023-contractHistoryHistorical-contratsOctroyesHistorique.csv"
curl -sS -L -o "$DL/awardNoticeHistorical.csv" "https://canadabuys.canada.ca/opendata/pub/2012-2022-awardNoticeHistorical-avisAttributionHistorique.csv"

echo "Done"
