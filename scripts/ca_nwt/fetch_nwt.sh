#!/bin/bash
# Download all GNWT Contract Report xlsx files listed under "Contracts Reporting" resources
cd downloads/ca_nwt
UA="contracts-research/1.0"
for n in 11994 11963 11817 11732 11650 11618 11514 11435 11337 11502 11317 11497 11500 11101 11499 11498 11493 11495 11494 11536 11504 10187 10093 10023 9164 8425 11980 11979 11978; do
  if ls node${n}_*.xlsx >/dev/null 2>&1; then echo "$n have"; continue; fi
  u=$(curl -sS -m 60 -A "$UA" -L "https://www.fin.gov.nt.ca/node/$n" | grep -o -E 'href="[^"]*\.xlsx[^"]*"' | head -1 | sed 's/href="//;s/"$//')
  if [ -n "$u" ]; then f="node${n}_$(basename "$u")"; curl -sS -m 180 -A "$UA" -o "$f" -w "$n %{http_code} $f %{size_download}\n" "$u"; else echo "$n NO XLSX"; fi
  sleep 0.3
done
echo FETCH_DONE
