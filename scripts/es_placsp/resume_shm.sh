#!/bin/bash
# Resume after reboot: root disk nearly full, so each zip is downloaded to /dev/shm, extracted, deleted.
dl=downloads/es_placsp
log=$dl/download.log
B=https://contrataciondelestado.es/sindicacion
one() { # url name
  t=/dev/shm/$2
  echo "$(date -u +%FT%TZ) START $1 (to /dev/shm)" >> "$log"
  curl -sS -L --retry 2 -A "contracts-research/1.0" -o "$t" "$1" >> "$log" 2>&1
  echo "$(date -u +%FT%TZ) END $2 size=$(stat -c %s "$t" 2>/dev/null)" >> "$log"
  python3 -I scripts/es_placsp/extract.py "$t" --out $dl/matches.jsonl --log $dl/extract.log
  rm -f "$t"
}
for m in 202604 202603 202602 202601; do one "$B/sindicacion_643/licitacionesPerfilesContratanteCompleto3_$m.zip" "s643_$m.zip"; done
for m in 202610 202609 202608 202607 202606 202605 202604 202603 202602 202601; do one "$B/sindicacion_1044/PlataformasAgregadasSinMenores_$m.zip" "s1044_$m.zip"; done
one "$B/sindicacion_643/licitacionesPerfilesContratanteCompleto3_2025.zip" "s643_2025.zip"
echo "$(date -u +%FT%TZ) RESUME ALL DONE" >> "$log"
