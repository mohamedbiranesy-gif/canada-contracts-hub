#!/bin/bash
# Download EU Financial Transparency System yearly datasets (English) — one file at a time, 2 s pause.
cd downloads/eu_fts
for y in 2025 2024 2023 2022 2021 2020 2019 2018 2017 2016; do
  f=${y}_FTS_dataset_en.xlsx
  [ -s "$f" ] && continue
  u="https://ec.europa.eu/budget/financial-transparency-system/download/$f"
  curl -sS -A "contracts-research/1.0" -o "$f" -w "$(date -u +%FT%TZ) $u %{http_code} %{size_download}\n" "$u" >> fetch.log 2>&1
  sleep 2
done
echo DONE >> fetch.log
