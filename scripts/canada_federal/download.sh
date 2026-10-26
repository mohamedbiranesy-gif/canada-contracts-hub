#!/bin/bash
# Download all source files for canada_federal with resume + retry.
# Usage: bash download.sh  (logs to logs/download.log)
set -u
DL=downloads/canada_federal
LOG=scripts/canada_federal/logs/download.log
UA="contracts-research/1.0"
mkdir -p "$DL"

fetch() {
  local url="$1" out="$2" attempt=1
  while [ $attempt -le 8 ]; do
    echo "$(date -u +%FT%TZ) GET attempt=$attempt $url -> $out" >> "$LOG"
    curl -sS -L -A "$UA" -C - --retry 5 --retry-delay 5 --retry-all-errors \
         --connect-timeout 60 --max-time 3600 -o "$DL/$out" "$url" >> "$LOG" 2>&1
    rc=$?
    if [ $rc -eq 0 ]; then
      echo "$(date -u +%FT%TZ) OK $out size=$(stat -c%s "$DL/$out")" >> "$LOG"
      return 0
    fi
    # curl rc 33 = range not supported / already complete, rc 22 = HTTP error
    if [ $rc -eq 33 ]; then
      echo "$(date -u +%FT%TZ) rc=33 (range not satisfiable; likely complete) $out size=$(stat -c%s "$DL/$out")" >> "$LOG"
      return 0
    fi
    echo "$(date -u +%FT%TZ) FAIL rc=$rc $out (size now $(stat -c%s "$DL/$out" 2>/dev/null))" >> "$LOG"
    attempt=$((attempt+1))
    sleep 10
  done
  return 1
}

echo "$(date -u +%FT%TZ) === download batch start ===" >> "$LOG"

# Schemas / dictionaries (small)
fetch "https://open.canada.ca/data/recombinant-published-schema/contracts.json" "contracts_schema.json"
fetch "https://open.canada.ca/data/recombinant-published-dictionary/contracts" "contracts_data_dictionary.xlsx"
fetch "https://donnees-data.tpsgc-pwgsc.gc.ca/ba2/ac-cb/achatscanada-canadabuys-dd.xml" "canadabuys_data_dictionary.xml"
fetch "https://donnees-data.tpsgc-pwgsc.gc.ca/ba2/ac-cb/COsoutien-CHsupport-eng.html" "canadabuys_contract_history_support_eng.html"
fetch "https://donnees-data.tpsgc-pwgsc.gc.ca/ba2/ac-cb/soutien-support-eng.html" "canadabuys_notices_support_eng.html"

# Proactive disclosure (small ones first)
fetch "https://open.canada.ca/data/dataset/d8f85d91-7dec-4fd1-8055-483b77225d8b/resource/fa4ff6c4-e9af-4491-9d4e-2b468e415a68/download/contracts-nil.csv" "contracts-nil.csv"
fetch "https://open.canada.ca/data/dataset/d8f85d91-7dec-4fd1-8055-483b77225d8b/resource/2e9a82e2-bb18-4bff-a61e-59af3b429672/download/contractsa.csv" "contractsa.csv"

# CanadaBuys files
fetch "https://canadabuys.canada.ca/opendata/pub/contractHistoryComplete-contratsOctroyesComplet.csv" "contractHistoryComplete-contratsOctroyesComplet.csv"
fetch "https://canadabuys.canada.ca/opendata/pub/awardNoticeComplete-avisAttributionComplet.csv" "awardNoticeComplete-avisAttributionComplet.csv"
fetch "https://canadabuys.canada.ca/opendata/pub/tenderNoticeComplete-avisAppelOffresComplet.csv" "tenderNoticeComplete-avisAppelOffresComplet.csv"

# The big one
fetch "https://open.canada.ca/data/dataset/d8f85d91-7dec-4fd1-8055-483b77225d8b/resource/fac950c0-00d5-4ec1-a4d3-9cbebf98a305/download/contracts.csv" "contracts.csv"

echo "$(date -u +%FT%TZ) === download batch done ===" >> "$LOG"
