#!/usr/bin/env python3
"""Request, poll and fetch USAspending bulk award downloads (Custom Award Data Download API)
for recipients located in Canada, one request per fiscal year (the API caps date_range at 366 days).

Usage:
  python3 -I bulk_download.py submit  --fy 2026            # submit one FY
  python3 -I bulk_download.py submit  --all                # submit FY2001..FY2027
  python3 -I bulk_download.py poll                         # poll all pending jobs, download finished zips, unzip
  python3 -I bulk_download.py run --all                    # submit all + poll until done

State is kept in downloads/usaspending/requests/FY<year>.json (request body + API response + status).
"""
import argparse
import json
import os
import subprocess
import sys
import time
import zipfile
from datetime import datetime, timezone

import requests

API = "https://api.usaspending.gov"
UA = "contracts-research/1.0"
BASE = "downloads/usaspending"
REQ_DIR = os.path.join(BASE, "requests")
ZIP_DIR = os.path.join(BASE, "zips")
EXT_DIR = os.path.join(BASE, "extracted")
LOG = "scripts/usaspending/logs/bulk_download.log"
REF_DATE = "2026-10-25"

PRIME_TYPES = ["A", "B", "C", "D", "IDV_A", "IDV_B", "IDV_B_A", "IDV_B_B", "IDV_B_C", "IDV_C", "IDV_D", "IDV_E"]
SUB_TYPES = ["procurement"]

for d in (REQ_DIR, ZIP_DIR, EXT_DIR, os.path.dirname(LOG)):
    os.makedirs(d, exist_ok=True)


def log(msg):
    line = f"{datetime.now(timezone.utc).isoformat()} {msg}"
    print(line, flush=True)
    with open(LOG, "a") as f:
        f.write(line + "\n")


def session():
    s = requests.Session()
    s.headers.update({"User-Agent": UA, "Content-Type": "application/json", "Accept": "application/json"})
    return s


def fy_range(fy):
    start = f"{fy-1}-10-01"
    end = f"{fy}-09-30"
    if end > REF_DATE:
        end = REF_DATE
    return start, end


def body_for(fy, agencies_variant="empty"):
    start, end = fy_range(fy)
    filters = {
        "prime_award_types": PRIME_TYPES,
        "sub_award_types": SUB_TYPES,
        "date_type": "action_date",
        "date_range": {"start_date": start, "end_date": end},
        "recipient_locations": [{"country": "CAN"}],
    }
    if agencies_variant == "empty":
        filters["agencies"] = []
    elif agencies_variant == "all":
        filters["agencies"] = [{"type": "awarding", "tier": "toptier", "name": "all"}]
    # "omit": no agencies key
    return {"filters": filters, "file_format": "csv"}


def state_path(fy):
    return os.path.join(REQ_DIR, f"FY{fy}.json")


def load_state(fy):
    p = state_path(fy)
    if os.path.exists(p):
        with open(p) as f:
            return json.load(f)
    return None


def save_state(fy, st):
    with open(state_path(fy), "w") as f:
        json.dump(st, f, indent=2)


def submit(s, fy, force=False):
    st = load_state(fy)
    if st and st.get("response") and not force:
        log(f"FY{fy}: already submitted as {st['response'].get('file_name')}, skip")
        return st
    last_err = None
    for variant in ("empty", "all", "omit"):
        body = body_for(fy, variant)
        for attempt in range(1, 6):
            try:
                r = s.post(f"{API}/api/v2/bulk_download/awards/", data=json.dumps(body), timeout=120)
            except requests.RequestException as e:
                last_err = f"network error: {e}"
                log(f"FY{fy} variant={variant} attempt {attempt}: {last_err}")
                time.sleep(10 * attempt)
                continue
            if r.status_code == 200:
                resp = r.json()
                st = {
                    "fy": fy,
                    "request_body": body,
                    "agencies_variant": variant,
                    "submitted_at": datetime.now(timezone.utc).isoformat(),
                    "response": resp,
                    "status": "submitted",
                }
                save_state(fy, st)
                log(f"FY{fy}: submitted ({variant}) -> {resp.get('file_name')}")
                return st
            last_err = f"HTTP {r.status_code}: {r.text[:500]}"
            log(f"FY{fy} variant={variant} attempt {attempt}: {last_err}")
            if r.status_code in (400, 422):
                break  # try next body variant
            time.sleep(10 * attempt)
    st = {"fy": fy, "status": "submit_failed", "error": last_err, "submitted_at": datetime.now(timezone.utc).isoformat()}
    save_state(fy, st)
    return st


def check_status(s, file_name):
    for attempt in range(1, 6):
        try:
            r = s.get(f"{API}/api/v2/download/status", params={"file_name": file_name}, timeout=120)
            if r.status_code == 200:
                return r.json()
            log(f"status {file_name}: HTTP {r.status_code} {r.text[:300]}")
        except requests.RequestException as e:
            log(f"status {file_name}: network error {e}")
        time.sleep(10 * attempt)
    return None


def download_zip(file_url, dest):
    # curl with resume + retries through the preconfigured proxy
    cmd = ["curl", "-sS", "-L", "-C", "-", "--retry", "5", "--retry-delay", "10", "--retry-all-errors",
           "-A", UA, "-o", dest, file_url]
    for attempt in range(1, 6):
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0:
            return True
        log(f"curl attempt {attempt} failed rc={res.returncode}: {res.stderr.strip()[:300]}")
        time.sleep(15 * attempt)
    return False


def unzip(zip_path, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    names = []
    with zipfile.ZipFile(zip_path) as z:
        for info in z.infolist():
            # guard against path traversal
            name = os.path.basename(info.filename)
            if not name:
                continue
            target = os.path.join(out_dir, name)
            with z.open(info) as src, open(target, "wb") as dst:
                while True:
                    chunk = src.read(1 << 20)
                    if not chunk:
                        break
                    dst.write(chunk)
            names.append({"name": name, "size": os.path.getsize(target)})
    return names


def poll(s, fys, interval=30, max_minutes=240):
    deadline = time.time() + max_minutes * 60
    pending = set()
    for fy in fys:
        st = load_state(fy)
        if st and st.get("response") and st.get("status") not in ("done", "failed"):
            pending.add(fy)
    log(f"polling {len(pending)} jobs: {sorted(pending)}")
    while pending and time.time() < deadline:
        for fy in sorted(pending):
            st = load_state(fy)
            fname = st["response"]["file_name"]
            js = check_status(s, fname)
            if js is None:
                continue
            st["last_status"] = js
            status = js.get("status")
            if status == "finished":
                file_url = js.get("file_url") or st["response"].get("file_url")
                dest = os.path.join(ZIP_DIR, fname)
                log(f"FY{fy}: finished rows={js.get('total_rows')} cols={js.get('total_columns')} size_kb={js.get('total_size')} secs={js.get('seconds_elapsed')}; downloading {file_url}")
                ok = download_zip(file_url, dest)
                if ok and zipfile.is_zipfile(dest):
                    files = unzip(dest, os.path.join(EXT_DIR, f"FY{fy}"))
                    st["status"] = "done"
                    st["zip_path"] = dest
                    st["zip_size"] = os.path.getsize(dest)
                    st["downloaded_at"] = datetime.now(timezone.utc).isoformat()
                    st["files"] = files
                    log(f"FY{fy}: downloaded {st['zip_size']} bytes; files={files}")
                    pending.discard(fy)
                else:
                    log(f"FY{fy}: download failed or not a zip; will retry")
                    if os.path.exists(dest) and not zipfile.is_zipfile(dest):
                        os.remove(dest)
            elif status == "failed":
                st["status"] = "failed"
                log(f"FY{fy}: FAILED: {js.get('message')}")
                pending.discard(fy)
            else:
                log(f"FY{fy}: {status} ({js.get('seconds_elapsed')}s)")
            save_state(fy, st)
        if pending:
            time.sleep(interval)
    if pending:
        log(f"poll timeout; still pending: {sorted(pending)}")
    return pending


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["submit", "poll", "run"])
    ap.add_argument("--fy", type=int, nargs="*")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--interval", type=int, default=30)
    ap.add_argument("--max-minutes", type=int, default=240)
    ap.add_argument("--batch", type=int, default=0, help="submit at most N new jobs per poll cycle (0 = all at once)")
    a = ap.parse_args()
    fys = list(range(2001, 2028)) if a.all else (a.fy or [])
    s = session()
    if a.cmd in ("submit", "run"):
        for fy in fys:
            submit(s, fy, force=a.force)
    if a.cmd in ("poll", "run"):
        all_fys = list(range(2001, 2028)) if a.cmd == "poll" and not fys else fys
        poll(s, all_fys, interval=a.interval, max_minutes=a.max_minutes)


if __name__ == "__main__":
    main()
