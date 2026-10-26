#!/bin/bash
# Download PLACSP (Plataforma de Contratación del Sector Público) monthly/annual atom zip archives.
dl=downloads/es_placsp
cd "$dl" || exit 1
log=$dl/download.log
dlone() { # url name
  [ -s "$2" ] && { echo "$(date -u +%FT%TZ) SKIP $2 exists" >> "$log"; return; }
  echo "$(date -u +%FT%TZ) START $1" >> "$log"
  curl -sS -L --retry 2 -A "contracts-research/1.0" -o "$2.part" "$1" >> "$log" 2>&1 && mv "$2.part" "$2"
  echo "$(date -u +%FT%TZ) END $2 size=$(stat -c %s "$2" 2>/dev/null)" >> "$log"
}
B=https://contrataciondelestado.es/sindicacion
for m in 202610 202609 202608 202607 202606 202605 202604 202603 202602 202601; do
  dlone "$B/sindicacion_643/licitacionesPerfilesContratanteCompleto3_$m.zip" "s643_$m.zip"
done
dlone "$B/sindicacion_643/licitacionesPerfilesContratanteCompleto3_2025.zip" "s643_2025.zip"
for m in 202610 202609 202608 202607 202606 202605 202604 202603 202602 202601; do
  dlone "$B/sindicacion_1044/PlataformasAgregadasSinMenores_$m.zip" "s1044_$m.zip"
done
dlone "$B/sindicacion_1044/PlataformasAgregadasSinMenores_2025.zip" "s1044_2025.zip"
dlone "$B/sindicacion_643/licitacionesPerfilesContratanteCompleto3_2024.zip" "s643_2024.zip"
dlone "$B/sindicacion_1044/PlataformasAgregadasSinMenores_2024.zip" "s1044_2024.zip"
echo "$(date -u +%FT%TZ) ALL DONE" >> "$log"
