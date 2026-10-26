#!/bin/bash
OUT=downloads/canada_federal/urlcheck
LOG=scripts/canada_federal/logs/probe_urls.log
while read -r u; do
  [ -z "$u" ] && continue
  f="$OUT/$(echo "$u" | md5sum | cut -c1-12).html"
  res=$(curl -sS -L -A "contracts-research/1.0" --max-time 60 -o "$f" -w "%{http_code} %{size_download}" "$u")
  title=$(grep -o '<title>[^<]*' "$f" | head -1 | sed 's/<title>//' | tr -d '\n' | cut -c1-90)
  echo "$(date -u +%FT%TZ) $res $u | $title | $f" >> "$LOG"
  sleep 25
done <<'URLS'
https://canadabuys.canada.ca/en/tender-opportunities/award-notice/pw-22-00998342-1009635
https://canadabuys.canada.ca/en/tender-opportunities/award-notice/08112-220034-001-cz
https://canadabuys.canada.ca/en/tender-opportunities/award-notice/08112-220034:001:cz
https://canadabuys.canada.ca/en/tender-opportunities/award-notice/w8486-088630/001/blb
https://canadabuys.canada.ca/en/tender-opportunities/tender-notice/ssc-26-00035000:t
https://canadabuys.canada.ca/en/tender-opportunities/tender-notice/pw-__ml-065-29485
https://canadabuys.canada.ca/en/tender-opportunities/tender-notice/mx-444085720081
https://canadabuys.canada.ca/en/tender-opportunities/award-notice/en578-150229-005-qf
https://canadabuys.canada.ca/en/tender-opportunities/tender-notice/ssc-26-00035000-t
URLS
echo "$(date -u +%FT%TZ) done2" >> "$LOG"
