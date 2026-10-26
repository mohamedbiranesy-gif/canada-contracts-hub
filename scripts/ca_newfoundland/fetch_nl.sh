#!/bin/bash
cd downloads/ca_newfoundland
UA="contracts-research/1.0"
while read u; do f="pdf/$(basename "$u")"; [ -s "$f" ] && continue; curl -sS -m 120 -A "$UA" -o "$f" -w "%{http_code} $f %{size_download}\n" "$u"; sleep 0.4; done < pdf_urls.txt
echo FETCH_DONE
