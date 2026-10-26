#!/usr/bin/env python3
"""Fetch SEAO notice details from the public SEAO API to get planned contract durations / end dates
for Quebec records whose status was only inferred (no closure record).

Usage: python3 -I api_status_harvest.py <normalized_seao.jsonl> <out.jsonl> [threads] [rate_per_sec]
Resumable (skips notice UUIDs already in <out.jsonl>). Newest signed contracts first.
"""
import sys, os, re, json, time, threading, queue, urllib.request, datetime

SRC, OUT = sys.argv[1], sys.argv[2]
THREADS = int(sys.argv[3]) if len(sys.argv) > 3 else 2
RATE = float(sys.argv[4]) if len(sys.argv) > 4 else 2.0
API = "https://api.seao.gouv.qc.ca/prod/api/avis/%s/consulter"
UA = {"User-Agent": "contracts-research/1.0 (status verification; polite)"}
KEEP_KEYS = {"datePrevueFinContratUtc", "dateFinContratUtc", "dateDebutContratUtc", "dateConclusionContratUtc", "dateAnnulationUtc",
             "nomOrganisation", "neq", "montantContrat", "montantContratAvecOptions", "statutId", "nomLot", "numeroLot", "contractant"}

done = set()
if os.path.exists(OUT):
    with open(OUT, encoding="utf-8") as f:
        for line in f:
            try:
                done.add(json.loads(line)["uuid"])
            except Exception:
                pass

notices = {}
if SRC.endswith(".csv.gz") or SRC.endswith(".csv"):
    import csv, gzip
    with (gzip.open(SRC, "rt") if SRC.endswith(".gz") else open(SRC)) as f:
        for row in csv.DictReader(f):
            if row["uuid"] not in done:
                notices[row["uuid"]] = row.get("signed") or ""
    SRC = os.devnull
with open(SRC, encoding="utf-8") as f:
    for line in f:
        if '"ongoing_inferred"' not in line:
            continue
        r = json.loads(line)
        if r.get("status") != "ongoing_inferred":
            continue
        m = re.search(r"ItemId=([0-9a-f-]{36})", (r.get("source") or {}).get("record_url") or "")
        if not m or m.group(1) in done:
            continue
        d = (r.get("contract") or {}).get("dates") or {}
        signed = d.get("signed") or d.get("start") or d.get("published") or ""
        u = m.group(1)
        if u not in notices or signed > notices[u]:
            notices[u] = signed
todo = sorted(notices.items(), key=lambda kv: kv[1], reverse=True)
print("notices to fetch", len(todo), "already", len(done), file=sys.stderr, flush=True)

q = queue.Queue()
for u, s in todo:
    q.put((u, s))
lock = threading.Lock()
rate_lock = threading.Lock()
last = [0.0]
outf = open(OUT, "a", encoding="utf-8")
stats = {"ok": 0, "err": 0}


def throttle():
    with rate_lock:
        wait = last[0] + 1.0 / RATE - time.time()
        if wait > 0:
            time.sleep(wait)
        last[0] = time.time()


def extract(a):
    info = a.get("avisResumeInformation") or {}
    rec = {"dureePrevueSansOptions": info.get("dureePrevueSansOptions"), "dureePrevueIncluantOptions": info.get("dureePrevueIncluantOptions"),
           "sommaireOptionsRenouvellement": info.get("sommaireOptionsRenouvellement"), "sommaireOptionsAcquisitionSupplementaire": info.get("sommaireOptionsAcquisitionSupplementaire"),
           "sectionInfoFinaleVisible": a.get("sectionInfoFinaleVisible"), "dates": [], "parties": []}
    def walk(o, path):
        if isinstance(o, dict):
            sub = {k: v for k, v in o.items() if k in KEEP_KEYS and v not in (None, "")}
            if any(k.startswith("date") for k in sub) or "nomOrganisation" in sub:
                for k, v in list(sub.items()):
                    if isinstance(v, dict):
                        sub[k] = v.get("descriptionFr") or v.get("value")
                sub["_path"] = path
                rec["parties" if "nomOrganisation" in sub else "dates"].append(sub)
            for k, v in o.items():
                walk(v, path + "." + k)
        elif isinstance(o, list):
            for i, x in enumerate(o[:200]):
                walk(x, path + "[%d]" % i)
    walk(a, "")
    rec["dates"] = rec["dates"][:60]
    rec["parties"] = rec["parties"][:80]
    return rec


def worker():
    while True:
        try:
            u, s = q.get_nowait()
        except queue.Empty:
            return
        res = None
        for attempt in range(3):
            throttle()
            try:
                with urllib.request.urlopen(urllib.request.Request(API % u, headers=UA), timeout=40) as resp:
                    res = json.loads(resp.read().decode("utf-8"))
                break
            except Exception as e:
                err = str(e)
                time.sleep(5 * (attempt + 1) if ("429" in err or "503" in err) else 2)
        with lock:
            if res is None:
                stats["err"] += 1
                outf.write(json.dumps({"uuid": u, "signed": s, "error": True, "retrieved_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}) + "\n")
            else:
                stats["ok"] += 1
                rec = extract(res.get("apiData") or {})
                rec.update({"uuid": u, "signed": s, "api_url": API % u, "retrieved_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")})
                outf.write(json.dumps(rec, ensure_ascii=False) + "\n")
            outf.flush()
            n = stats["ok"] + stats["err"]
            if n % 500 == 0:
                print(datetime.datetime.now().strftime("%H:%M"), stats, file=sys.stderr, flush=True)


ths = [threading.Thread(target=worker, daemon=True) for _ in range(THREADS)]
for t in ths:
    t.start()
for t in ths:
    t.join()
print("done", stats, file=sys.stderr)
