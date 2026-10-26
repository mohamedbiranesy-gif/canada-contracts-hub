#!/usr/bin/env python3
"""Print compact sample records (normalized layer; raw summarized) for notes.
Usage: python3 -I samples.py <file.jsonl> <n> [record_id ...]   (picks spread-out records when no ids given)"""
import sys, json
p, n = sys.argv[1], int(sys.argv[2]); want = set(sys.argv[3:])
lines = open(p, encoding="utf-8").read().splitlines()
if want:
    picks = [json.loads(l) for l in lines if json.loads(l)["record_id"] in want]
else:
    step = max(1, len(lines) // n)
    picks = [json.loads(lines[i]) for i in range(0, len(lines), step)][:n]


def trim(o, depth=0):
    if isinstance(o, str):
        return o if len(o) <= 160 else o[:157] + "…"
    if isinstance(o, list):
        return [trim(x, depth + 1) for x in o[:4]] + ([f"... ({len(o)} total)"] if len(o) > 4 else [])
    if isinstance(o, dict):
        return {k: trim(v, depth + 1) for k, v in o.items()}
    return o


for r in picks:
    raw = r.get("raw") or {}
    summ = {k: (f"{len(v)} row(s)" if isinstance(v, list) else type(v).__name__) for k, v in raw.items()}
    r2 = {k: v for k, v in r.items() if k != "raw"}
    print(f"#### `{r['record_id']}`\n\nraw keys: `{json.dumps(summ, ensure_ascii=False)}`\n\n```json")
    print(json.dumps(trim(r2), ensure_ascii=False, indent=1))
    print("```\n")
