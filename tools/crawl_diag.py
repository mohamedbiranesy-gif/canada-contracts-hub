#!/usr/bin/env python3
"""Why does the mailbox crawl find nothing on two thirds of the lead sites? A measurement, not a harvester: a sample of lead sites that gave
"nothing_found" (and a control sample that gave "found") is read again — home page plus up to 3 contact pages, same polite reader — and each
site is put in ONE class. Only counts are printed (and, for the rule lists, the mailbox NAMES before the @ that were turned down on 5+
different sites: role words we do not know yet show up there). Nothing is written to the dataset.

  python3 tools/crawl_diag.py --n 400 [--minutes 25]

Classes (first that applies):
  unreachable / blocked          the site did not answer or refused the reader
  obfuscated_cloudflare          the page carries Cloudflare's e-mail protection (data-cfemail): not decoded, by rule
  obfuscated_text                "info [at] domain", "info (at) domain", HTML-entity or script-built addresses: not decoded
  mailbox_other_domain           addresses printed, none on the organisation's own domain or name (webmail, a parent's domain)
  mailbox_person_like            addresses on its own domain, all shaped like a person's (first.last, initials)
  mailbox_unknown_word           addresses on its own domain whose name is not a known role word  -> candidates for the word lists
  would_be_found_now             a role mailbox IS on these pages (the earlier crawl missed it: time budget, page order, a rule added since)
  form_only                      no address anywhere on the pages read; a contact form
  nothing                        no address, no form on the pages read
"""
import argparse, collections, csv, os, random, re, sys, threading, time, urllib.parse
from concurrent.futures import ThreadPoolExecutor

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ap_crawler as C  # noqa: E402
import lead_crawl as LC  # noqa: E402

CONTACT = re.compile(r"contact|joindre|coordonn|about|propos|nous-trouver|find-us|reach|equipe|team|staff|personnel|bureau|office", re.I)
OBF_TEXT = re.compile(r"[A-Za-z0-9._-]{2,}\s*(?:\[\s*(?:at|arobase|a)\s*\]|\(\s*(?:at|arobase|a)\s*\)|\s+at\s+|\s+arobase\s+|&#0*64;|&#x0*40;|%40)\s*[A-Za-z0-9-]+\s*(?:\.|\[\s*dot\s*\]|\(\s*dot\s*\)|\s+dot\s+|\s+point\s+)\s*[A-Za-z]{2,}", re.I)
OBF_SCRIPT = re.compile(r"String\.fromCharCode|data-(?:user|name|local)=[\"'][^\"']+[\"'][^>]*data-(?:domain|host)=|document\.write\([^)]*@|unescape\(|\.replace\([^)]*(?:\(at\)|\[at\])", re.I)
FORM = re.compile(r"<form\b[^>]*>(?:(?!</form).){0,6000}?(?:<textarea|type=[\"']?email|name=[\"'][^\"']*(?:message|email|courriel)[^\"']*[\"'])", re.I | re.S)


def classify_site(site, name):
    host = LC.host_of(site)
    pages, raws = [], []
    st, ct, data, final = C.fetch(site)
    head = data[:20000].decode("utf-8", "replace") if data else ""
    if st == 0:
        return "unreachable", []
    if st in (401, 403, 429) or (C.BLOCK_RX.search(head) and len(data) < 30000):
        return "blocked", []
    if st != 200 or not data:
        return "unreachable", []
    raw = data.decode("utf-8", "replace")
    raws.append(raw)
    links, seen = [], set()
    for link, label in C.links(raw, final):
        p = urllib.parse.urlparse(link)
        if p.scheme in ("http", "https") and C.registrable((p.hostname or "").lower()) == C.registrable(host) and not C.SKIP_EXT.search(p.path) and CONTACT.search(p.path + " " + label):
            u = link.split("#")[0]
            if u not in seen and u.rstrip("/") != final.rstrip("/"):
                seen.add(u)
                links.append((0 if re.search(r"contact|joindre|coordonn", p.path + " " + label, re.I) else 1, len(p.path), u))
    for _, _, u in sorted(links)[:3]:
        if not C.allowed(u):
            continue
        s2, _, d2, _ = C.fetch(u)
        if s2 == 200 and d2:
            raws.append(d2.decode("utf-8", "replace"))
    import html as _h
    allraw = "\n".join(raws)
    if re.search(r"data-cfemail|/cdn-cgi/l/email-protection", allraw):
        cf = True
    else:
        cf = False
    un = _h.unescape(allraw)
    text = C.visible(un)
    found, own_unknown, own_person, other = [], [], [], []
    for e in set(x.lower().rstrip(".") for x in C.EMAIL_RX.findall(un)):
        if e.rsplit(".", 1)[-1] in ("png", "jpg", "jpeg", "gif", "svg", "webp", "js", "css"):
            continue
        local = e.split("@")[0]
        try:
            same = C.same_org(e, site, name or "")
        except Exception:
            same = False
        if not same:
            other.append(local)
            continue
        i = C.find_tok(text, e)
        kind = C.classify(e, text[max(0, i - 400):i + 400] if i >= 0 else "", "any")
        if kind and LC.ok_mailbox(e):
            found.append(kind)
        elif C.PERSONAL.match(local) and not C.ROLE_HINT.search(local):
            own_person.append(local)
        else:
            own_unknown.append(local)
    if found:
        return "would_be_found_now", []
    if own_unknown:
        return "mailbox_unknown_word", own_unknown
    if own_person:
        return "mailbox_person_like", []
    if cf:
        return "obfuscated_cloudflare", []
    if other:
        return "mailbox_other_domain", []
    if OBF_TEXT.search(text) or OBF_SCRIPT.search(allraw):
        return "obfuscated_text", []
    if FORM.search(allraw):
        return "form_only", []
    return "nothing", []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=400)
    ap.add_argument("--minutes", type=float, default=25)
    ap.add_argument("--workers", type=int, default=40)
    a = ap.parse_args()
    os.makedirs(C.STATE, exist_ok=True)
    leads = {}
    for p in (os.path.join(LC.INC, "claude_buyer_leads_cc.csv"), os.path.join(LC.INC, "claude_buyer_leads.csv")):
        if os.path.exists(p):
            for r in csv.DictReader(open(p, encoding="utf-8", errors="replace")):
                if (r.get("website") or "").startswith("http"):
                    leads.setdefault(r["buyer_key"], (r["website"], r.get("buyer_name") or "", (r.get("canada_field_value") or "")[:40]))
    groups = collections.defaultdict(list)
    for l in open(LC.DONE, encoding="utf-8"):
        q = l.rstrip("\n").split("\t")
        if len(q) > 2 and q[0] in leads and q[2] in ("nothing_found", "found"):
            groups[q[2]].append(q[0])
    rnd = random.Random(11)
    sample = [(k, "nothing_found") for k in rnd.sample(groups["nothing_found"], min(a.n, len(groups["nothing_found"])))] + \
             [(k, "found") for k in rnd.sample(groups["found"], min(a.n // 4, len(groups["found"])))]
    print("lead sites read before: nothing_found %d, found %d; sample %d + %d" % (len(groups["nothing_found"]), len(groups["found"]), min(a.n, len(groups["nothing_found"])), min(a.n // 4, len(groups["found"]))), flush=True)
    deadline = time.time() + a.minutes * 60
    lock, res, words = threading.Lock(), collections.defaultdict(collections.Counter), collections.Counter()

    def one(t):
        key, grp = t
        if time.time() > deadline:
            return
        site, name, _ = leads[key]
        try:
            cls, unknown = classify_site(site, name)
        except Exception as e:
            cls, unknown = "error:" + type(e).__name__, []
        with lock:
            res[grp][cls] += 1
            if grp == "nothing_found":
                for w in set(unknown):
                    words[re.sub(r"\d+", "", w)[:24]] += 1
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(one, sample))
    for grp in ("nothing_found", "found"):
        tot = sum(res[grp].values()) or 1
        print("\n== sites that gave '%s' before (%d read again)" % (grp, tot))
        for cls, c in res[grp].most_common():
            print("  %-26s %5d  %4.1f %%" % (cls, c, 100.0 * c / tot))
    print("\n== mailbox names (before the @) turned down as 'unknown word' on 5+ different sites of the sample")
    print("  " + ", ".join("%s %d" % kv for kv in words.most_common(80) if kv[1] >= 5))
    sys.stdout.flush()
    os._exit(0)


if __name__ == "__main__":
    main()
