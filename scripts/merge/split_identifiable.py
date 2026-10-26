import sys, os, gzip, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from identify import parties_identifiable
src_main, src_unv, outdir = sys.argv[1:4]
c = collections.Counter(); reasons = collections.Counter()
with gzip.open(os.path.join(outdir, "parties_not_identified_contracts.jsonl.gz"), "wt", encoding="utf-8") as bad:
    for src, dst in ((src_main, "canadian_vendor_contracts.jsonl.gz"), (src_unv, "vendor_country_unverified_contracts.jsonl.gz")):
        tmp = os.path.join(outdir, dst + ".tmp")
        with gzip.open(src, "rt", encoding="utf-8") as fin, gzip.open(tmp, "wt", encoding="utf-8", compresslevel=6) as fout:
            for line in fin:
                r = json.loads(line)
                ok, why = parties_identifiable(r)
                if ok:
                    fout.write(line); c[dst + ":kept"] += 1
                else:
                    r["parties_identifiable"] = False; r["parties_identifiable_reason"] = why
                    bad.write(json.dumps(r, ensure_ascii=False) + "\n"); c[dst + ":moved"] += 1
                    reasons[(r["source_file"], why.split(" (")[0])] += 1
        os.replace(tmp, os.path.join(outdir, dst))
print(dict(c)); print(reasons.most_common(20))
