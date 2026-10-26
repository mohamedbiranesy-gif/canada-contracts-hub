#!/bin/bash
out=downloads/ocp_registry/field_probe.jsonl
while read -r sk pid nm; do
  url="https://data.open-contracting.org/en/publication/$pid/download?name=$nm.jsonl.gz"
  curl -sS -L -A "contracts-research/1.0" "$url" 2>/dev/null | gunzip -c 2>/dev/null | head -n 3000 | python3 -I scripts/ocp_registry/field_probe.py "$sk:$nm" >> $out
  sleep 1
done <<'Q'
ar_mendoza 137 full
br_compras_gov 157 2025
do_dgcp 22 2025
gh_ppa 85 full
gt_guatecompras 142 2025
hn_oncae 122 2025
hn_sefin 123 2025
it_anac 117 2025
ke_ppip 147 2025
lr_ppcc 156 full
mx_nuevo_leon 149 full
ng_bpp 64 full
tz_nest 152 2025
ug_ppda 130 full
za_etenders 143 full
ec_sercop 110 2025
py_dncp 63 2025
cl_mercado_publico 144 2025
hr_eojn 80 full
nl_tenderned 133 full
rw_umucyo 145 2025
zm_zppa 3 2024
pe_oece 135 2025
de_bmi_oeffentlichevergabe 136 2025
Q
echo DONE >> $out
