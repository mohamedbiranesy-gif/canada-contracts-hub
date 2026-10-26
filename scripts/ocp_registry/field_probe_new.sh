#!/bin/bash
out=downloads/ocp_registry/field_probe.jsonl
while read -r sk pid nm; do
  url="https://data.open-contracting.org/en/publication/$pid/download?name=$nm.jsonl.gz"
  curl -sS -L -A "contracts-research/1.0" "$url" 2>/dev/null | gunzip -c 2>/dev/null | head -n 3000 | python3 -I scripts/ocp_registry/field_probe.py "$sk:$nm" >> $out
  sleep 1
done <<'Q'
al_ppc 134 full
gr_diavgis 161 full
mx_inai 31 full
uy_arce 43 2025
md_mtender 34 2025
xk_pprc 115 full
pa_dgcp 120 2022
es_zaragoza 1 full
co_cce 61 2022
fr_dinum 23 2022
no_opentender 72 full
ch_opentender 91 full
si_mju 82 full
Q
echo DONE2 >> $out
