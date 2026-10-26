#!/bin/bash
C=.; OUTD=${1:-$C/out_final}
cd $C
echo "$(date '+%F %T') finalize"; rm -rf "$OUTD"; mkdir -p "$OUTD"; python3 -I scripts/merge/finalize.py $C "$OUTD" > work/finalize_final.log 2>&1; tail -3 work/finalize_final.log
echo "$(date '+%F %T') readme"; python3 -I scripts/merge/make_readme.py $C "$OUTD"
cd "$OUTD/full" && ls -S | head -8 > ../.big.txt && ls | grep -v -x -F -f ../.big.txt > ../.small.txt && tar -cf ../full_small_sources.tar -T ../.small.txt
echo "$(date '+%F %T') ASSEMBLE_DONE"
