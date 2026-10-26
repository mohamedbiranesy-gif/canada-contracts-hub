#!/bin/bash
# after resume_shm.sh finishes: process the 2024 annual 643 file the same way (download to /dev/shm, extract, delete)
dl=downloads/es_placsp; log=$dl/download.log
while ! grep -q "RESUME ALL DONE" $log; do sleep 30; done
t=/dev/shm/s643_2024.zip
echo "$(date -u +%FT%TZ) START https://contrataciondelestado.es/sindicacion/sindicacion_643/licitacionesPerfilesContratanteCompleto3_2024.zip (to /dev/shm)" >> $log
curl -sS -L --retry 2 -A "contracts-research/1.0" -o $t "https://contrataciondelestado.es/sindicacion/sindicacion_643/licitacionesPerfilesContratanteCompleto3_2024.zip" >> $log 2>&1
echo "$(date -u +%FT%TZ) END s643_2024.zip size=$(stat -c %s $t 2>/dev/null)" >> $log
python3 -I scripts/es_placsp/extract.py $t --out $dl/matches.jsonl --log $dl/extract.log
rm -f $t
echo "$(date -u +%FT%TZ) RESUME2 DONE" >> $log
