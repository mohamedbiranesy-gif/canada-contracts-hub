#!/usr/bin/env python3
"""Search worker on the Anthropic API (owner 2026-11-08 13:07 EST: use the plan's API credits): finds candidate PAGE ADDRESSES for the
readers — nothing else. One Messages call per task with the server-side web_search tool restricted to the organisation's own host; the
URLs are taken from the tool's result blocks (not from the model's prose), so only addresses the search engine returned are kept. Every
page is then opened, read and quoted by the Mac readers (tools/award_facts.py, ap_terms.py, deep_pages.py, vendor_sites_check.py) —
the evidence rules of AGENTS.md §2 are unchanged.

Task kinds (TSV in --queue, one task per line, header task_id, kind, key, name, host, extra):
  af  award facts for a buyer–vendor pair: host = buyer site, name = vendor, key = buyer_key||vendor → query "<vendor core> contract award"
  pc  AP / PO-terms pages of a buyer: host = buyer site, key = buyer_key → query "accounts payable invoice payment terms purchase order supplier"
  vw  vendor website: name = vendor, host empty, key = vendor_key → query "<vendor> official website" (directories dropped)
Outputs (appended, deduplicated): --out-dir/af_urls.csv (row_key,buyer_key,buyer_name,website,vendor,url), pc_urls.csv
(buyer_key,buyer_name,website,official_site,url), vw_proposals.tsv (vendor_key, vendor_name, website, evidence_url, evidence_quote, confidence).
Resume: --out-dir/done.tsv (task_id, status, n_urls, cost_usd_estimate). Budget: --max-usd stops the worker (search $10 / 1,000 + tokens).
  python3 tools/api_search_worker.py --queue ~/cch-tasks/apiq/queue.tsv --out-dir ~/cch-tasks/apiq [--limit 500] [--max-usd 20] [--model claude-haiku-5-5]
"""
import argparse, csv, json, os, re, sys, time, urllib.error, urllib.parse, urllib.request

API = "https://api.anthropic.com/v1/messages"
DIRECTORY = re.compile(r"opencorporates|zoominfo|dnb\.com|linkedin|facebook|yellowpages|canada411|bloomberg|crunchbase|glassdoor|indeed|merx|biddingo|bidsandtenders|sedar|wikipedia|yelp|bbb\.org|manta\.com|cylex|hotfrog|\.gov\b|\.gc\.ca|\.gouv\.qc\.ca|instagram|twitter|x\.com|youtube|rocketreach|apollo\.io|signalhire|owler|craft\.co|tracxn|pitchbook|buzzfile|dandb|companieshouse|opengovca|canadacompanyregistry|infobel|cybo|bizapedia", re.I)
STOP = {"inc", "incorporated", "ltd", "limited", "ltee", "ltée", "corp", "corporation", "co", "company", "llc", "llp", "lp", "the", "group", "groupe", "canada", "international", "services", "service", "solutions", "consulting", "construction", "enterprises", "entreprises"}
PRICE = {"claude-haiku-4-5": (1.0, 5.0), "claude-sonnet-4-5": (3.0, 15.0), "claude-haiku-5-5": (1.0, 5.0), "claude-sonnet-5-5": (3.0, 15.0)}  # $ / M tokens in, out (approximate; the budget guard is conservative)
SEARCH_USD = 0.01


def key_file():
    for p in (os.environ.get("ANTHROPIC_API_KEY"), None):
        if p:
            return p.strip()
    for p in (os.path.expanduser("~/cch-crawler-state/anthropic.key"), os.path.expanduser("~/.anthropic.key")):
        if os.path.exists(p):
            return open(p).read().strip()
    return ""


def core(name):
    toks = [t for t in re.findall(r"[A-Za-z0-9ÀÂÄÇÉÈÊËÎÏÔÖÙÛÜŸàâäçéèêëîïôöùûüÿ'&.-]+", name or "") if t.lower().strip(".") not in STOP]
    return " ".join(toks[:5]) or (name or "")


def query_for(t):
    k = t["kind"]
    if k == "af":
        return '"%s" contract award' % core(t["name"]), [t["host"]] if t.get("host") else None
    if k == "pc":
        fr = t.get("host", "").endswith(".qc.ca") or re.search(r"\b(ville|municipalit|centre de services|cégep|cegep|québec|quebec|commission scolaire)\b", t.get("extra", "") + " " + t.get("name", ""), re.I)
        return ("comptes payables facture modalités de paiement bon de commande fournisseurs" if fr else "accounts payable invoice payment terms purchase order supplier"), [t["host"]] if t.get("host") else None
    if k == "vw":
        return "%s official website" % (t["name"]), None
    return t.get("name", ""), None


def call(api_key, model, query, allowed, max_uses=1):
    tool = {"type": "web_search_20250305", "name": "web_search", "max_uses": max_uses}
    if allowed:
        tool["allowed_domains"] = [h for h in allowed if h]
    body = {"model": model, "max_tokens": 300, "tools": [tool],
            "messages": [{"role": "user", "content": "Run exactly one web search for: %s\nThen reply with the single word DONE. Do not summarise." % query}]}
    req = urllib.request.Request(API, data=json.dumps(body).encode(), headers={"x-api-key": api_key, "anthropic-version": "2023-06-01", "content-type": "application/json", "user-agent": "canada-contracts-hub-crawler/1.0"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                return json.loads(r.read().decode()), ""
        except urllib.error.HTTPError as e:
            txt = e.read().decode(errors="replace")[:300]
            if e.code in (429, 529, 500, 502, 503) and attempt < 3:
                time.sleep(5 * (attempt + 1)); continue
            return None, "http_%d %s" % (e.code, txt)
        except Exception as e:
            if attempt < 3:
                time.sleep(3); continue
            return None, "error %s" % type(e).__name__
    return None, "retries"


def results_of(resp):
    """URLs and titles from the web_search_tool_result blocks — the search engine's own list, not the model's words"""
    out = []
    for b in resp.get("content") or []:
        if b.get("type") == "web_search_tool_result":
            c = b.get("content")
            if isinstance(c, list):
                for r in c:
                    if r.get("type") == "web_search_result" and r.get("url"):
                        out.append((r["url"], r.get("title") or "", r.get("page_age") or ""))
    u = resp.get("usage") or {}
    n_search = (u.get("server_tool_use") or {}).get("web_search_requests", 0)
    return out, n_search, u.get("input_tokens", 0), u.get("output_tokens", 0)


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--queue", required=True)
    a.add_argument("--out-dir", required=True)
    a.add_argument("--limit", type=int, default=0)
    a.add_argument("--max-usd", type=float, default=25.0)
    a.add_argument("--model", default="claude-haiku-5-5")
    a.add_argument("--sleep", type=float, default=0.7)
    a = a.parse_args()
    api_key = key_file()
    if not api_key:
        sys.exit("no API key (ANTHROPIC_API_KEY or ~/cch-crawler-state/anthropic.key)")
    os.makedirs(a.out_dir, exist_ok=True)
    done_p = os.path.join(a.out_dir, "done.tsv")
    done = {}
    if os.path.exists(done_p):
        for l in open(done_p, encoding="utf-8"):
            f = l.rstrip("\n").split("\t")
            if len(f) >= 2:
                done[f[0]] = f[1]
    spent = 0.0
    if os.path.exists(done_p):
        for l in open(done_p, encoding="utf-8"):
            f = l.rstrip("\n").split("\t")
            if len(f) >= 4:
                try:
                    spent += float(f[3])
                except ValueError:
                    pass
    tasks = [t for t in csv.DictReader(open(a.queue, encoding="utf-8", errors="replace"), delimiter="\t") if t.get("task_id") and t["task_id"] not in done]
    if a.limit:
        tasks = tasks[:a.limit]
    print("tasks: %d (done before: %d; spent so far ≈ $%.2f)" % (len(tasks), len(done), spent), flush=True)
    pin, pout = PRICE.get(a.model, (3.0, 15.0))
    af = open(os.path.join(a.out_dir, "af_urls.csv"), "a", newline="", encoding="utf-8"); afw = csv.writer(af)
    pc = open(os.path.join(a.out_dir, "pc_urls.csv"), "a", newline="", encoding="utf-8"); pcw = csv.writer(pc)
    vw = open(os.path.join(a.out_dir, "vw_proposals.tsv"), "a", encoding="utf-8")
    if os.path.getsize(os.path.join(a.out_dir, "af_urls.csv")) == 0:
        afw.writerow(["row_key", "buyer_key", "buyer_name", "website", "vendor", "url"])
    if os.path.getsize(os.path.join(a.out_dir, "pc_urls.csv")) == 0:
        pcw.writerow(["buyer_key", "buyer_name", "website", "official_site", "url"])
    if os.path.getsize(os.path.join(a.out_dir, "vw_proposals.tsv")) == 0:
        vw.write("vendor_key\tvendor_name\twebsite\tevidence_url\tevidence_quote\tconfidence\n")
    stats = {"ok": 0, "no_results": 0, "error": 0, "urls": 0}
    for t in tasks:
        if spent >= a.max_usd:
            print("budget reached: $%.2f" % spent, flush=True); break
        q, allowed = query_for(t)
        resp, err = call(api_key, a.model, q, allowed)
        if resp is None:
            stats["error"] += 1
            with open(done_p, "a", encoding="utf-8") as f:
                f.write("%s\t%s\t0\t0\n" % (t["task_id"], err.split(" ")[0]))
            if err.startswith("http_401") or err.startswith("http_403"):
                print("API refused:", err); break
            time.sleep(a.sleep); continue
        res, n_search, tin, tout = results_of(resp)
        cost = n_search * SEARCH_USD + tin / 1e6 * pin + tout / 1e6 * pout
        spent += cost
        host = (t.get("host") or "").lower().removeprefix("www.")
        kept = 0
        for url, title, age in res:
            h = (urllib.parse.urlparse(url).hostname or "").lower().removeprefix("www.")
            if t["kind"] in ("af", "pc"):
                if not host or not (h == host or h.endswith("." + host) or host.endswith("." + h)):
                    continue
                if t["kind"] == "af":
                    afw.writerow([t["key"], t.get("extra") or t["key"].split("||")[0], "", "https://%s" % host, t["name"], url])
                else:
                    pcw.writerow([t["key"], t.get("name") or "", "https://%s" % host, "", url])
                kept += 1
            else:
                if DIRECTORY.search(url) or not h:
                    continue
                root = "https://%s/" % h
                vw.write("\t".join([t["key"], t["name"], root, url, (title or "")[:200].replace("\t", " "), "search result"]) + "\n")
                kept += 1
                break  # one proposal per vendor: the reader confirms or rejects it
        stats["ok" if kept else "no_results"] += 1; stats["urls"] += kept
        with open(done_p, "a", encoding="utf-8") as f:
            f.write("%s\t%s\t%d\t%.4f\n" % (t["task_id"], "ok" if kept else "no_results", kept, cost))
        if (stats["ok"] + stats["no_results"]) % 25 == 0:
            af.flush(); pc.flush(); vw.flush()
            print(time.strftime("%H:%M"), stats, "spent ≈ $%.2f" % spent, flush=True)
        time.sleep(a.sleep)
    af.close(); pc.close(); vw.close()
    print("done", stats, "spent ≈ $%.2f" % spent, flush=True)


if __name__ == "__main__":
    main()
