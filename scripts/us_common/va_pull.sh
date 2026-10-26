#!/bin/bash
# usage: va_pull.sh <year> <url>
cd .
curl -sS -L -m 3000 -A "contracts-research/1.0" "$2" | python3 -I scripts/us_common/stream_filter_csv.py - downloads/us_state_virginia/eva_$1_canada.csv "Vendor_Address_State" "ON,QC,BC,AB,MB,SK,NS,NB,NL,PE,NT,YT,NU,ONTARIO,QUEBEC,BRITISH COLUMBIA,ALBERTA,MANITOBA,SASKATCHEWAN,NOVA SCOTIA,NEW BRUNSWICK,NEWFOUNDLAND,PRINCE EDWARD ISLAND,CANADA,CAN,PQ,NF,LB"
