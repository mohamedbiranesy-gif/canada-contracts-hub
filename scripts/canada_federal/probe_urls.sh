#!/bin/bash
# Slow-paced probes of CanadaBuys notice URL slugs (one request / 20 s) to verify URL patterns despite WAF 403s.
OUT=downloads/canada_federal/urlcheck
LOG=scripts/canada_federal/logs/probe_urls.log
mkdir -p "$OUT"
while read -r u; do
  [ -z "$u" ] && continue
  f="$OUT/$(echo "$u" | md5sum | cut -c1-12).html"
  res=$(curl -sS -L -A "contracts-research/1.0" --max-time 60 -o "$f" -w "%{http_code} %{size_download}" "$u")
  title=$(grep -o '<title>[^<]*' "$f" | head -1 | sed 's/<title>//' | tr -d '\n' | cut -c1-90)
  echo "$(date -u +%FT%TZ) $res $u | $title | $f" >> "$LOG"
  sleep 20
done <<'URLS'
https://canadabuys.canada.ca/en/tender-opportunities/tender-notice/ws5938553031-doc5945464169
https://canadabuys.canada.ca/en/tender-opportunities/tender-notice/cb-50-83063359
https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cw2437072
https://canadabuys.canada.ca/en/tender-opportunities/tender-notice/ssc-26-00035000-t
https://canadabuys.canada.ca/en/tender-opportunities/tender-notice/ssc-26-00035000t
https://canadabuys.canada.ca/en/tender-opportunities/tender-notice/pw-__ml-065-29485
https://canadabuys.canada.ca/en/tender-opportunities/tender-notice/pw-ml-065-29485
https://canadabuys.canada.ca/en/tender-opportunities/award-notice/w8486-088630-001-blb
https://canadabuys.canada.ca/en/tender-opportunities/award-notice/w8486-088630001blb
https://canadabuys.canada.ca/en/tender-opportunities/award-notice/en578-150229-005-qf
https://canadabuys.canada.ca/en/tender-opportunities/tender-notice/mx-444085720081
https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cb-867-73443244
URLS
echo "$(date -u +%FT%TZ) done" >> "$LOG"
