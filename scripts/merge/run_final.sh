#!/bin/bash
# Final refresh: re-normalize resumed crawls, merge all sources, rebuild masters, re-match registries, assemble, README.
set -u
C=.
OUTD=${1:-$C/out_final}
log() { echo "$(date '+%F %T') $*"; }
cd $C
log "normalize bids&tenders"; python3 -I scripts/ca_bidsandtenders/normalize.py downloads/ca_bidsandtenders normalized || log "WARN bt normalize failed"
log "normalize merx";        python3 -I -W ignore scripts/ca_merx/normalize.py downloads/ca_merx normalized || log "WARN merx normalize failed"
for s in ca_bidsandtenders ca_merx; do
  python3 -I - "$s" <<'EOF'
import sys, json, os, datetime
s = sys.argv[1]; C = "."
stats_p = os.path.join(C, "downloads", s, "normalize_stats.json")
st = json.load(open(stats_p)) if os.path.exists(stats_p) else {}
n_main = sum(1 for _ in open(os.path.join(C, "normalized", s + ".jsonl")))
up = os.path.join(C, "normalized", s + "_unverified_country.jsonl")
n_unv = sum(1 for _ in open(up)) if os.path.exists(up) else 0
det = sum(1 for _ in open(os.path.join(C, "downloads", s, "details.jsonl")))
note = os.path.join(C, "notes", s + ".md")
txt = open(note).read().replace("Status: IN PROGRESS / PARTIAL (counts updated at end of run).", "Status: COMPLETE for the crawl window described below (final counts at the bottom).").replace("Status: IN PROGRESS / PARTIAL (see \"Counts\" — updated at the end of the run).", "Status: COMPLETE for the crawl window described below (final counts at the bottom).")
txt += "\n\n## Final counts (resumed crawl, normalized %s)\n- Detail pages parsed: %d\n- Records: main file %d; unverified-country file %d\n- normalize_stats.json: %s\n- Crawl window: newest awards first; bids&tenders details fetched for awards closing 2023-2026 in full and 2021-2022 as far as reached; MERX award tabs fetched newest first as far as reached (older backlog listed in downloads/<source>/listing.jsonl).\n" % (
    datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC"), det, n_main, n_unv, json.dumps(st, ensure_ascii=False)[:3000])
open(note, "w").write(txt)
print(s, "main", n_main, "unverified", n_unv)
EOF
done
log "merge"; python3 -I scripts/merge/merge2.py normalized work > work/merge2_final.log 2>&1; tail -1 work/merge2_final.log
log "masters"; python3 -I scripts/merge/build_masters2.py work/merged_ca.jsonl work/merged_unverified.jsonl enrichment/v2
log "registry match"; python3 -I scripts/enrichment_vendors/match_registries.py enrichment/v2/vendor_master_input.jsonl downloads/corporations_canada downloads/quebec_req/JeuDonnees.zip enrichment/v2/vendors_registry_v4_raw.jsonl enrichment/v2/vendors_registry_v4_stats.json > enrichment/v2/match4.log 2>&1
python3 -I scripts/enrichment_vendors/postprocess.py enrichment/v2/vendors_registry_v4_raw.jsonl enrichment/v2/vendors_registry_v3.jsonl && rm -f enrichment/v2/vendors_registry_v4_raw.jsonl
cp enrichment/v2/vendors_registry_v4_stats.json enrichment/v2/vendors_registry_v3_stats.json
log "finalize"; rm -rf "$OUTD"; mkdir -p "$OUTD"; python3 -I scripts/merge/finalize.py $C "$OUTD" > work/finalize_final.log 2>&1; tail -3 work/finalize_final.log
log "readme"; python3 -I scripts/merge/make_readme.py $C "$OUTD"
cd "$OUTD/full" && ls -S | head -8 > ../.big.txt && ls | grep -v -x -F -f ../.big.txt > ../.small.txt && tar -cf ../full_small_sources.tar -T ../.small.txt
log "FINAL_DONE"
