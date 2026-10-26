"""Write a candidates file of fetched-but-not-yet-digested round4 URLs. usage: next_digest.py <out_candidates.jsonl>"""
import json, glob, os, sys
B = "downloads/private_press"
dig = set()
for fn in glob.glob(f"{B}/round4_digest_*.jsonl"):
    for l in open(fn): dig.add(json.loads(l)["url"])
fetched = set()
for fn in glob.glob(f"{B}/fetched_round4*.jsonl") + [f"{B}/fetched_round3.jsonl"]:
    for l in open(fn):
        d = json.loads(l)
        if not d.get("error") and d.get("text"): fetched.add(d["url"])
cands = [json.loads(l) for l in open(f"{B}/round4_candidates_backlog.jsonl")]
extra = f"{B}/round4_candidates_new.jsonl"
if os.path.exists(extra): cands += [json.loads(l) for l in open(extra)]
todo = [c for c in cands if c["url"] in fetched and c["url"] not in dig]
with open(sys.argv[1], "w") as f:
    for c in todo: f.write(json.dumps(c, ensure_ascii=False) + "\n")
print(len(todo))
