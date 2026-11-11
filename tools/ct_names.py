#!/usr/bin/env python3
"""Domain names from Certificate Transparency (cloud): every site that holds a web certificate, read from the logs' own names tiles.

Why (2026-11-11). The lanes that grow the table need NAMES OF SITES to ask: the registry class reads .ca sites, the store sweep asks which
domains sit on Shopify's storefront network, the DNS lane asks whose zone a Canadian provider serves. Until now the names came from Common
Crawl's web graph (domains somebody links to: 63 M on the endings stores use, 1.05 M of the ~3.4 M registered .ca names) and one public list.
A site nobody links to is in neither — and most small shops are such sites. Every site with HTTPS is in the Certificate Transparency logs:
publishing each certificate there is a condition of browsers trusting it. The logs are public, append-only, and made to be read whole.

What is read. The logs of the static-ct kind are sets of immutable files ("tiles") behind a CDN. Those run with the Sunlight software also
publish NAMES TILES for readers that only want the names — one small gzip file of JSON lines per 256 certificates:
    <log>/tile/names/x004/x000/000 ->  {"Timestamp":…, "Subject":{…}, "DNS":["www.example.com","example.com"]}
(6.5 KB instead of the 170-440 KB of the full tile; announced by the logs' author on the ct-policy list for exactly this use). Measured
2026-11-11 on final certificates found in four logs: Let's Encrypt, Google Trust Services, ZeroSSL and Sectigo give each certificate one
SCT of an RFC 6962 log and one of a static log, chosen among Let's Encrypt Sycamore / Willow, Geomys Tuscolo and IPng Halloumi / Gouda.
Sycamore, Willow, Tuscolo and Gouda publish names tiles (Halloumi and Google's own static logs do not): a site that renews twice is in one
of the four with ~96 %. Certificates of GoDaddy, DigiCert, Amazon and Microsoft are in RFC 6962 logs only and are not seen here.

What is kept. Names only, cut to the registrable domain:
  - .ca                        -> data/incoming/claude/credit_scan/ctca_<stamp>.gz (names the lists on file do not have); the home-page scan
                                  (tools/credit_scan.py) and the DNS lookups read them like the other .ca names
  - the endings the store sweep covers (com net org co us shop store) and a second group of endings kept for later
                               -> lists in the sweep's own format, published as assets of the release `harvest-state` (ct_list_<stamp>.txt.gz);
                                  a Bloom filter (ct_seen.bloom, same release) keeps a name from being listed twice, and is seeded with the web
                                  graph's names so the two sweeps do not ask the same domain; tools/dns_services.py `sweep --list` asks them
  - the certificate's subject when a CA validated the organisation (O=, L=, ST=, C=CA): the legal name behind a domain, as a certificate
    authority checked it -> data/incoming/claude/ct_names/ov_ca_<stamp>.jsonl.gz (for the bill-to name; used by a rule of its own, later)

How politely. Tiles are static files meant for bulk readers; still, each operator gets a fixed total of requests a second from all runners
together (RATE), an identified user agent, and half the rate after any 429 / 503. Newest tiles first (the certificates of the last weeks),
then backwards; the shard of certificates about to expire is read only for its newest 40 %.

  read  --shard K/N [--minutes M] [--max-tiles T]   -> out/ct_ca_K.txt.gz, out/ct_sw_K.txt.gz, out/ct_xt_K.txt.gz, out/ct_ov_K.jsonl.gz, out/ct_done_K.json
  merge DIR --stamp S --lists OUT [--bloom FILE]    -> cursor.json, ctca_<S>.gz, ov_ca_<S>.jsonl.gz in the repository; OUT/ct_list_<S>.txt.gz,
                                                       OUT/ct_xlist_<S>.txt.gz and OUT/ct_seen.bloom.zst for the release
  left                                              -> prints how many tiles are still to read (the workflow starts its next run on it)
No organisation's server is contacted here. No AI, no search engine, no Mac.
"""
import argparse, collections, glob, gzip, hashlib, json, os, re, subprocess, sys, threading, time

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
INC = os.path.join(ROOT, "data/incoming/claude")
DIR = os.path.join(INC, "ct_names")
SCAN_DIR = os.path.join(INC, "credit_scan")
CURSOR = os.path.join(DIR, "cursor.json")
LOG_LIST = "https://www.gstatic.com/ct/log_list/v3/log_list.json"
UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub; reads names tiles only)"
# operators whose static logs publish names tiles -> requests a second sent to each of them by ALL runners of a run together
RATE = {"Let's Encrypt": 90.0, "Geomys": 30.0, "IPng Networks": 20.0}
TAIL = 0.40          # of a shard whose certificates are about to expire, only the newest part is read (the rest expired months ago)
TODAY = time.strftime("%Y-%m-%d", time.gmtime())
SWEEP_TLDS = ("com", "net", "org", "co", "us", "shop", "store")   # tools/dns_services.py SWEEP_TLDS
EXTRA_TLDS = ("io", "biz", "info", "club", "life", "live", "boutique", "studio", "design", "art", "beauty", "fit", "fashion", "style", "clothing", "shoes", "jewelry",
              "coffee", "pet", "kids", "toys", "bike", "garden", "world", "me", "tv", "cc")  # other endings shops use: listed apart, asked later if the first group pays
GROUP = dict({t: "sw" for t in SWEEP_TLDS}, **{t: "xt" for t in EXTRA_TLDS})
CA_SECOND = frozenset("ab bc mb nb nf nl ns nt nu on pe qc sk yk gc".split())
CO_SECOND = frozenset("com net org nom edu gov mil".split())
LABELS = re.compile(r"[a-z0-9-]+(?:\.[a-z0-9-]+)+")
BLOOM_BITS, BLOOM_K = 31, 6  # 2^31 bits (256 MiB): 150 M names at 14 bits each -> about 1 name in 1,000 wrongly taken for listed


def registrable(name):
    """(registrable domain, group) of a certificate name: group "ca", "sw" (endings the store sweep covers), "xt" (kept for later) or None"""
    n = name.lower()
    if n.startswith("*."):
        n = n[2:]
    i = n.rfind(".")
    if i <= 0 or len(n) > 100:
        return None, None
    tld = n[i + 1:]
    if tld == "ca":
        p = n.split(".")
        d = ".".join(p[-3:]) if len(p) >= 3 and p[-2] in CA_SECOND else ".".join(p[-2:])
        return (d, "ca") if LABELS.fullmatch(d) and len(d) <= 70 else (None, None)
    g = GROUP.get(tld)
    if not g:
        return None, None
    j = n.rfind(".", 0, i)
    d = n[j + 1:]
    if tld == "co" and d[:d.find(".")] in CO_SECOND and j > 0:
        d = n[n.rfind(".", 0, j) + 1:]
    return (d, g) if LABELS.fullmatch(d) and len(d) <= 70 else (None, None)


def any_registrable(name):
    """the last two labels (three under a second-level ending we know): only for the note of which domains a validated subject covers"""
    n = name.lower().lstrip("*.")
    p = n.split(".")
    if len(p) < 2:
        return ""
    return ".".join(p[-3:]) if len(p) >= 3 and (p[-1] == "ca" and p[-2] in CA_SECOND or (len(p[-1]) == 2 and p[-2] in ("co", "com", "org", "net", "ac", "gov", "edu"))) else ".".join(p[-2:])


def tile_path(n):
    s = "%03d" % n
    while len(s) % 3:
        s = "0" + s
    parts = [s[i:i + 3] for i in range(0, len(s), 3)]
    return "/".join(["x" + p for p in parts[:-1]] + [parts[-1]])


def cursor():
    try:
        return json.load(open(CURSOR, encoding="utf-8"))
    except (OSError, ValueError):
        return {"logs": {}, "lists": []}


def _session():
    import requests
    s = requests.Session()
    s.headers.update({"User-Agent": UA, "Accept-Encoding": "gzip"})
    return s


def discover(sess):
    """the static logs that publish names tiles and still hold certificates in force: [{name, url, operator, start, end, tiles}]"""
    d = sess.get(LOG_LIST, timeout=60).json()
    out = []
    horizon = time.strftime("%Y-%m-%d", time.gmtime(time.time() + 120 * 86400))
    for op in d.get("operators") or []:
        if op.get("name") not in RATE:
            continue
        for lg in op.get("tiled_logs") or []:
            st = next(iter(lg.get("state") or {}), "")
            ti = lg.get("temporal_interval") or {}
            start, end = (ti.get("start_inclusive") or "")[:10], (ti.get("end_exclusive") or "")[:10]
            if st not in ("usable", "qualified", "readonly") or not end or end <= TODAY or start > horizon:
                continue  # every certificate of the shard has expired, or the shard is for certificates no CA issues yet
            url = lg["monitoring_url"].rstrip("/") + "/"
            try:
                cp = sess.get(url + "checkpoint", timeout=60)
                size = int(cp.text.split("\n")[1])
                if size < 256 or sess.get(url + "tile/names/" + tile_path(size // 256 - 1), timeout=60).status_code != 200:
                    continue  # no names tiles on this log (IPng Halloumi, 2026-11-11); the newest full tile is asked: Gouda has none for its first tiles
            except Exception as e:
                print("log %s not readable now (%s)" % (lg.get("description"), str(e)[:80]), flush=True)
                continue
            out.append({"name": lg["description"], "url": url, "operator": op["name"], "start": start, "end": end, "tiles": size // 256})
    return out


def plan(sess, cur):
    """what a run reads of each log: tiles [hi, top) written since the last run, then [floor, lo) backwards"""
    soon = time.strftime("%Y-%m-%d", time.gmtime(time.time() + 75 * 86400))
    logs = []
    for lg in discover(sess):
        c = (cur.get("logs") or {}).get(lg["name"]) or {}
        top = lg["tiles"]
        hi = int(c["hi"]) if "hi" in c else top
        lo = int(c["lo"]) if "lo" in c else top
        floor = int(c["floor"]) if "floor" in c else (int(top * (1 - TAIL)) if lg["end"] <= soon else 0)
        logs.append(dict(lg, hi=hi, lo=lo, floor=floor, top=top))
    # per operator: the logs of certificates issued now first (floor 0), the larger log first
    logs.sort(key=lambda g: (g["operator"], g["floor"] > 0, -g["top"]))
    return logs


class Sink:
    def __init__(self, k):
        self.lock = threading.Lock()
        self.ca, self.sw, self.xt, self.ov = set(), set(), set(), {}
        self.k = k
        self.n_names = self.n_entries = 0
        self.fsw = gzip.open("out/ct_sw_%d.txt.gz" % k, "wt", encoding="ascii", compresslevel=4)
        self.fxt = gzip.open("out/ct_xt_%d.txt.gz" % k, "wt", encoding="ascii", compresslevel=4)

    def add(self, ca, sw, xt, ov, entries):
        with self.lock:
            self.n_entries += entries
            self.ca |= ca
            self.sw |= sw
            self.xt |= xt
            for key, rec in ov:
                self.ov.setdefault(key, rec)
            if len(self.sw) > 5_000_000:
                self._flush(self.sw, self.fsw)
            if len(self.xt) > 2_000_000:
                self._flush(self.xt, self.fxt)

    @staticmethod
    def _flush(s, f):
        f.write("\n".join(s) + "\n")
        s.clear()

    def close(self):
        with self.lock:
            if self.sw:
                self._flush(self.sw, self.fsw)
            if self.xt:
                self._flush(self.xt, self.fxt)
            self.fsw.close(); self.fxt.close()
            with gzip.open("out/ct_ca_%d.txt.gz" % self.k, "wt", encoding="ascii") as f:
                f.write("\n".join(sorted(self.ca)) + ("\n" if self.ca else ""))
            with gzip.open("out/ct_ov_%d.jsonl.gz" % self.k, "wt", encoding="utf-8") as f:
                for key in sorted(self.ov):
                    f.write(json.dumps(self.ov[key], ensure_ascii=False, separators=(",", ":")) + "\n")


def parse_tile(body, log_name, idx):
    ca, sw, xt, ov, n = set(), set(), set(), [], 0
    for line in body.split(b"\n"):
        if not line:
            continue
        try:
            o = json.loads(line)
        except ValueError:
            continue
        n += 1
        subj = o.get("Subject") or {}
        names = o.get("DNS") or ([subj["CommonName"]] if subj.get("CommonName") else [])
        for nm in names:
            d, g = registrable(nm)
            if g == "sw":
                sw.add(d)
            elif g == "ca":
                ca.add(d)
            elif g == "xt":
                xt.add(d)
        if subj.get("Organization") and "CA" in (subj.get("Country") or ()):
            doms = sorted({any_registrable(x) for x in names} - {""})[:25]
            key = "%s|%s|%s" % ("; ".join(subj.get("Organization") or []), "; ".join(subj.get("Locality") or []), ",".join(doms))
            ov.append((key, {"s": subj, "d": doms, "log": log_name, "tile": idx, "ts": o.get("Timestamp")}))
    return ca, sw, xt, ov, n


def read(a):
    k, n = int(a.shard.split("/")[0]), max(1, int(a.shard.split("/")[1]))
    os.makedirs("out", exist_ok=True)
    sess0 = _session()
    cur = cursor()
    logs = plan(sess0, cur)
    deadline = time.time() + a.minutes * 60
    sink = Sink(k)
    hosts = collections.OrderedDict()
    for g in logs:
        up = [i for i in range(g["hi"], g["top"]) if i % n == k]
        down = [i for i in range(g["lo"] - 1, g["floor"] - 1, -1) if i % n == k]
        if a.max_tiles:
            up, down = up[:a.max_tiles], down[:max(0, a.max_tiles - len(up))]
        g.update(jobs=[("up", i) for i in up] + [("down", i) for i in down], pos=0, ok=set(), halted=set(), n_up=len(up), n_down=len(down))
        # one budget per operator; Let's Encrypt runs its two logs as two services (mon.sycamore…, mon.willow…): one budget each
        hk = g["url"].split("/")[2] if g["operator"] == "Let's Encrypt" else g["operator"]
        h = hosts.setdefault(hk, {"rate": RATE[g["operator"]] / n, "next": 0.0, "lock": threading.Lock(), "logs": [], "stat": collections.Counter()})
        h["logs"].append(g)
        print("%-34s tiles %9d | new since last run %7d | backwards %8d (from %d down to %d) | this shard: %d + %d" % (
            g["name"], g["top"], g["top"] - g["hi"], max(0, g["lo"] - g["floor"]), g["lo"], g["floor"], len(up), len(down)), flush=True)

    def next_job(h):
        with h["lock"]:
            for g in h["logs"]:
                while g["pos"] < len(g["jobs"]):
                    way, i = g["jobs"][g["pos"]]
                    g["pos"] += 1
                    if way not in g["halted"]:
                        return g, way, i
            return None

    def turn(h):
        with h["lock"]:
            t = max(time.time(), h["next"])
            h["next"] = t + 1.0 / h["rate"]
        w = t - time.time()
        if w > 0:
            time.sleep(w)

    def worker(h):
        sess = _session()
        while time.time() < deadline:
            job = next_job(h)
            if job is None:
                return
            g, way, i = job
            url = g["url"] + "tile/names/" + tile_path(i)
            body = None
            for attempt in range(5):
                turn(h)
                try:
                    r = sess.get(url, timeout=40)
                except Exception as e:
                    h["stat"]["error:" + type(e).__name__] += 1
                    sess = _session()
                    time.sleep(2 + 3 * attempt)
                    continue
                if r.status_code == 200:
                    body = r.content
                    break
                h["stat"]["http_%d" % r.status_code] += 1
                if r.status_code == 404:
                    break  # a tile the log has not published (yet)
                if r.status_code in (429, 503):
                    with h["lock"]:
                        h["rate"] = max(0.5, h["rate"] / 2)  # the operator asks for less: half the rate for the rest of the run
                    time.sleep(30)
                else:
                    time.sleep(2 + 3 * attempt)
            if body is None:
                with h["lock"]:
                    g["halted"].add(way)  # this direction of this log stops here: the next run starts with this tile
                continue
            if body[:2] == b"\x1f\x8b":
                body = gzip.decompress(body)
            ca, sw, xt, ov, cnt = parse_tile(body, g["name"], i)
            sink.add(ca, sw, xt, ov, cnt)
            with h["lock"]:
                g["ok"].add(i)
                h["stat"]["tiles"] += 1

    threads = []
    for op, h in hosts.items():
        for _ in range(int(min(48, max(2, h["rate"] * 0.8 + 1)))):
            t = threading.Thread(target=worker, args=(h,), daemon=True)
            t.start()
            threads.append(t)
    t0 = time.time()
    while any(t.is_alive() for t in threads):
        time.sleep(20)
        if int(time.time() - t0) % 300 < 20:
            print(time.strftime("%H:%M:%S"), {op: dict(h["stat"], rate=round(h["rate"], 1)) for op, h in hosts.items()}, "| certificates %d, .ca names %d" % (sink.n_entries, len(sink.ca)), flush=True)
        if time.time() > deadline + 90:
            break
    for t in threads:
        t.join(timeout=5)
    sink.close()
    done = {}
    for h in hosts.values():
        for g in h["logs"]:
            up_reach, down_reach = g["hi"], g["lo"]
            for way, i in g["jobs"]:  # the frontier of each direction: every tile of this shard up to it was read
                if way == "up":
                    if i not in g["ok"]:
                        break
                    up_reach = i + 1
            for way, i in g["jobs"]:
                if way == "down":
                    if i not in g["ok"]:
                        break
                    down_reach = i
            # a shard with nothing to do in a direction does not hold the others back
            done[g["name"]] = {"url": g["url"], "operator": g["operator"], "end": g["end"], "floor": g["floor"], "top": g["top"],
                               "up": up_reach if g["n_up"] else g["top"], "down": down_reach if g["n_down"] else g["floor"],
                               "up_all": g["n_up"] > 0 and up_reach >= max(i for w, i in g["jobs"] if w == "up") + 1,
                               "down_all": g["n_down"] > 0 and down_reach <= min(i for w, i in g["jobs"] if w == "down"), "tiles": len(g["ok"])}
    with open("out/ct_done_%d.json" % k, "w", encoding="utf-8") as f:
        json.dump({"shard": k, "of": n, "logs": done, "entries": sink.n_entries, "max_tiles": a.max_tiles}, f)
    print("finished: %d certificates read in %d tiles; .ca names %d; %s" % (sink.n_entries, sum(len(g["ok"]) for h in hosts.values() for g in h["logs"]), len(sink.ca),
                                                                           {op: dict(h["stat"]) for op, h in hosts.items()}), flush=True)


# ------------------------------------------------------------------------------------------------------------------- merge
class Bloom:
    """the names already listed. Kept between runs as a release asset: ct_seen.bloom.zst (or .gz where zstd is not installed)"""

    def __init__(self, path=None):
        import shutil
        self.m = 1 << BLOOM_BITS
        self.b = None
        for cand in ([path] if path and os.path.exists(path) else []) + ([path + x for x in (".zst", ".gz") if os.path.exists(path + x)] if path else []):
            if cand.endswith(".zst") and shutil.which("zstd"):
                raw = subprocess.run(["zstd", "-dc", cand], check=True, stdout=subprocess.PIPE).stdout
            elif cand.endswith(".gz"):
                raw = gzip.open(cand, "rb").read()
            else:
                raw = open(cand, "rb").read()
            if len(raw) == self.m // 8:
                self.b = bytearray(raw)
                break
        self.fresh = self.b is None
        if self.b is None:
            self.b = bytearray(self.m // 8)

    def add(self, name):
        """True when the name was not there before (and is now)"""
        h = hashlib.blake2b(name.encode("ascii", "replace"), digest_size=16).digest()
        x, y = int.from_bytes(h[:8], "little"), int.from_bytes(h[8:], "little") | 1
        b, mask, new = self.b, self.m - 1, False
        for _ in range(BLOOM_K):
            i = x & mask
            if not b[i >> 3] & (1 << (i & 7)):
                b[i >> 3] |= 1 << (i & 7)
                new = True
            x += y
        return new

    def save(self, path):
        """path without ending; returns the file written"""
        import shutil
        if shutil.which("zstd"):
            with open(path, "wb") as f:
                f.write(self.b)
            if subprocess.run(["zstd", "-q", "-3", "-f", "--rm", path, "-o", path + ".zst"]).returncode != 0:
                raise SystemExit("zstd failed: the Bloom filter was not saved")
            return path + ".zst"
        with gzip.open(path + ".gz", "wb", compresslevel=1) as f:
            f.write(self.b)
        return path + ".gz"


def known_ca():
    import csv
    csv.field_size_limit(1 << 30)
    known = set()
    for name in ("ca_domains.csv.gz", "graph_ca_domains.csv.gz"):
        p = os.path.join(SCAN_DIR, name)
        if os.path.exists(p):
            with gzip.open(p, "rt", encoding="utf-8", newline="") as fh:
                known |= {r["dom"] for r in csv.DictReader(fh)}
    for p in glob.glob(os.path.join(SCAN_DIR, "ctca_*.gz")):
        with gzip.open(p, "rt", encoding="ascii", errors="replace") as fh:
            known |= {l.strip() for l in fh if l.strip()}
    return known


def ct_ca_names():
    """the .ca names the certificate logs brought (append-only shards credit_scan/ctca_<stamp>.gz)"""
    for p in sorted(glob.glob(os.path.join(SCAN_DIR, "ctca_*.gz"))):
        with gzip.open(p, "rt", encoding="ascii", errors="replace") as fh:
            for l in fh:
                l = l.strip()
                if l:
                    yield l


def seed_bloom(bloom, release, base):
    """the names the web-graph sweep already asks (tools/dns_services.py sweep): never listed here"""
    import cc_clients as CCL
    url = "%sprojects/hyperlinkgraph/%s/domain/%s-domain-vertices.txt.gz" % (base or CCL.CC, release, release)
    pref = tuple(t + "." for t in SWEEP_TLDS)
    p = subprocess.Popen("curl -sS -L --fail --retry 10 --retry-delay 10 --retry-all-errors -A %s %s | gzip -dc" % (json.dumps(CCL.UA), json.dumps(url)), shell=True, stdout=subprocess.PIPE)
    n = 0
    for l in p.stdout:
        q = l.split(b"\t")
        if len(q) < 2:
            continue
        r = q[1].strip().decode("ascii", "replace")
        if r.startswith(pref):
            bloom.add(".".join(reversed(r.split("."))))
            n += 1
    if p.wait() != 0 or n < 1_000_000:
        raise SystemExit("the web graph's list could not be read whole (%d names): nothing is published this run" % n)
    return n


def merge(a):
    os.makedirs(DIR, exist_ok=True)
    os.makedirs(a.lists, exist_ok=True)
    cur = cursor()
    cur.setdefault("logs", {}); cur.setdefault("lists", [])
    objs = []
    for f in sorted(glob.glob(os.path.join(a.dir, "ct_done_*.json"))):
        try:
            objs.append(json.load(open(f, encoding="utf-8")))
        except ValueError:
            pass
    if not objs:
        print("no shard finished: nothing to merge")
        return
    of = max(int(o.get("of") or 1) for o in objs)
    whole = len({int(o["shard"]) for o in objs}) == of and not any(o.get("max_tiles") for o in objs)
    entries = sum(int(o.get("entries") or 0) for o in objs)
    left = 0
    for name in sorted({n for o in objs for n in o["logs"]}):
        per = [o["logs"][name] for o in objs if name in o["logs"]]
        c = cur["logs"].setdefault(name, {})
        c.update(url=per[0]["url"], operator=per[0]["operator"], end=per[0]["end"], floor=int(per[0]["floor"]))
        c.setdefault("hi", int(per[0]["top"])); c.setdefault("lo", int(per[0]["top"]))
        if whole and len(per) == of:  # the places move only when every shard reported: a tile is done when all of them passed it
            c["hi"] = max(int(c["hi"]), min(int(p["up"]) for p in per))
            c["lo"] = min(int(c["lo"]), max(int(p["down"]) for p in per))
        c["tiles_read"] = int(c.get("tiles_read") or 0) + sum(int(p.get("tiles") or 0) for p in per)
        c["top"] = max(int(p["top"]) for p in per)
        c["updated"] = time.strftime("%Y-%m-%dT%H:%MZ", time.gmtime())
        left += max(0, c["lo"] - c["floor"]) + max(0, c["top"] - c["hi"])
        print("%-34s read so far: tiles %d..%d of %d (floor %d); %d tiles this run" % (name, c["lo"], c["hi"], c["top"], c["floor"], sum(int(p.get("tiles") or 0) for p in per)))
    # .ca names the lists on file do not have
    known, new_ca = known_ca(), set()
    for f in glob.glob(os.path.join(a.dir, "ct_ca_*.txt.gz")):
        with gzip.open(f, "rt", encoding="ascii", errors="replace") as fh:
            new_ca |= {l.strip() for l in fh if l.strip()}
    seen_ca = len(new_ca)
    new_ca -= known
    if new_ca:
        os.makedirs(SCAN_DIR, exist_ok=True)
        with gzip.open(os.path.join(SCAN_DIR, "ctca_%s.gz" % a.stamp), "wt", encoding="ascii") as f:
            f.write("\n".join(sorted(new_ca)) + "\n")
    cur["ca_names"] = int(cur.get("ca_names") or 0) + len(new_ca)
    # subjects a certificate authority validated, organisation in Canada
    ov = {}
    for f in glob.glob(os.path.join(a.dir, "ct_ov_*.jsonl.gz")):
        with gzip.open(f, "rt", encoding="utf-8") as fh:
            for l in fh:
                try:
                    o = json.loads(l)
                except ValueError:
                    continue
                ov.setdefault("%s|%s" % ("; ".join(o["s"].get("Organization") or []), ",".join(o.get("d") or [])), o)
    if ov:
        with gzip.open(os.path.join(DIR, "ov_ca_%s.jsonl.gz" % a.stamp), "wt", encoding="utf-8") as f:
            for key in sorted(ov):
                f.write(json.dumps(ov[key], ensure_ascii=False, separators=(",", ":")) + "\n")
    cur["ov_records"] = int(cur.get("ov_records") or 0) + len(ov)
    # the names for the sweeps: listed once (Bloom filter), in the sweep's own list format (number <tab> name written backwards)
    bloom = Bloom(a.bloom)
    if bloom.fresh and (cur.get("bloom") or {}).get("entries") and not a.new_bloom:
        raise SystemExit("the Bloom filter of the earlier runs was not found (release asset ct_seen.bloom.zst): nothing is published — "
                         "every name would be listed again. Pass --new-bloom to start one on purpose.")
    seeded = 0
    if bloom.fresh and a.seed_release:
        seeded = seed_bloom(bloom, a.seed_release, a.base)
        print("Bloom filter started with the web graph's %d names on %s (%s)" % (seeded, ",".join(SWEEP_TLDS), a.seed_release))
    tmp = a.tmp or os.environ.get("RUNNER_TEMP") or "/tmp"
    counts = {}
    for grp, pat, out in (("sw", "ct_sw_*.txt.gz", "ct_list_%s.txt.gz"), ("xt", "ct_xt_*.txt.gz", "ct_xlist_%s.txt.gz")):
        files = sorted(glob.glob(os.path.join(a.dir, pat)))
        if not files:
            continue
        srt = os.path.join(tmp, "ct_%s_sorted.txt" % grp)
        subprocess.run("gzip -dc %s | LC_ALL=C sort -u -S 2G -T %s > %s" % (" ".join(json.dumps(f) for f in files), json.dumps(tmp), json.dumps(srt)), shell=True, check=True)
        n_in = n_new = 0
        path = os.path.join(a.lists, out % a.stamp)
        with open(srt, encoding="ascii", errors="replace") as fi, gzip.open(path, "wt", encoding="ascii", compresslevel=5) as fo:
            for l in fi:
                d = l.strip()
                if not d:
                    continue
                n_in += 1
                if bloom.add(d):
                    n_new += 1
                    fo.write("0\t%s\n" % ".".join(reversed(d.split("."))))
        os.remove(srt)
        counts[grp] = (n_in, n_new)
        if n_new:
            cur["lists"].append({"name": out % a.stamp, "names": n_new, "group": grp, "stamp": a.stamp})
        else:
            os.remove(path)
    bloom.save(os.path.join(a.lists, "ct_seen.bloom"))
    cur["bloom"] = {"bits": BLOOM_BITS, "k": BLOOM_K, "entries": int((cur.get("bloom") or {}).get("entries") or 0) + seeded + sum(v[1] for v in counts.values())}
    cur["certificates_read"] = int(cur.get("certificates_read") or 0) + entries
    cur["tiles_left"] = left
    cur["updated"] = time.strftime("%Y-%m-%dT%H:%MZ", time.gmtime())
    with open(CURSOR, "w", encoding="utf-8") as f:
        json.dump(cur, f, indent=1, sort_keys=True)
    print("certificate logs: %d certificates read this run (%d so far); .ca names seen %d, new to the lists on file %d (%d so far); validated subjects in Canada %d; "
          "names for the store sweep: %d seen, %d new (list %s); other endings: %d seen, %d new; tiles still to read: %d%s" % (
              entries, cur["certificates_read"], seen_ca, len(new_ca), cur["ca_names"], len(ov), counts.get("sw", (0, 0))[0], counts.get("sw", (0, 0))[1],
              "ct_list_%s.txt.gz" % a.stamp if counts.get("sw", (0, 0))[1] else "none", counts.get("xt", (0, 0))[0], counts.get("xt", (0, 0))[1], left,
              "" if whole else " (a partial run: the places in the logs were not moved)"))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("cmd", choices=["read", "merge", "left", "plan"])
    p.add_argument("dir", nargs="?", default="shards")
    p.add_argument("--shard", default="0/1")
    p.add_argument("--minutes", type=float, default=150)
    p.add_argument("--max-tiles", type=int, default=0, help="read: at most this many tiles per log and shard (tests; such a run does not move the places)")
    p.add_argument("--stamp", default=time.strftime("%Y%m%dT%H%M%S", time.gmtime()))
    p.add_argument("--lists", default="out_lists")
    p.add_argument("--bloom", default="")
    p.add_argument("--new-bloom", action="store_true")
    p.add_argument("--seed-release", default="", help="merge, first run: the web graph release whose names the other sweep asks (they are never listed here)")
    p.add_argument("--base", default="")
    p.add_argument("--tmp", default="")
    a = p.parse_args()
    if a.cmd == "read":
        read(a)
        sys.stdout.flush()
        os._exit(0)
    elif a.cmd == "merge":
        merge(a)
    elif a.cmd == "plan":
        for g in plan(_session(), cursor()):
            print(json.dumps(g))
    else:
        print(int(cursor().get("tiles_left") or 0))


if __name__ == "__main__":
    main()
