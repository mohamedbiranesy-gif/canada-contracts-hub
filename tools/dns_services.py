#!/usr/bin/env python3
"""DNS lane (cloud): the paid services an organisation's own public DNS records show — and which of the providers are in Canada.

Owner 2026-11-09 23:41 EST: "some Canadian entity receives money for a service they provided, and that relationship is established online …
think like that, where I completely miss it". A domain's DNS is published by the organisation itself and says who works for it today:
  SPF   "v=spf1 include:spf.likuid.com …"   the organisation authorises that provider's servers to send its mail (it is hosted there)
  MX    "mx1.zerospam.ca"                    its mail is received / filtered by that provider
  NS    "ns1.whc.ca"                         its DNS zone is served by that provider (web host, registrar, managed DNS)
  TXT   "1password-site-verification=…"      a domain-verification record a business account of that vendor requires
First look at the 66,764 SPF records already on file (buyers of the dataset): 1,600 include Web Hosting Canada's servers, 833 Tucows' hosted
e-mail, 571 Elastic Email, 389 Likuid, 336 HostPapa, 145 Vidéotron, 141 eSolutions … — thousands of delivered rows that carry only an
inferred relationship have a live, named, Canada-located service provider in their own DNS.

  lookup --shard K/N [--minutes M]   TXT / MX / NS of every domain of the scan universe (rows, leads, linking sites, OpenStreetMap, .ca) that
                                     was not looked up yet; public resolvers, a few queries per domain -> out/dns_<K>.jsonl
  merge DIR --stamp S                -> data/incoming/claude/credit_scan/dns_<S>_<k>.gz (append-only), and the table of providers by number of
                                     client domains (dns_providers_seen.csv)
The provider's location is proven the same way as for a credited web agency (tools/credit_scan.py `vendors`: its own site prints a Canadian
postal address, or schema.org address, or location line + Canadian telephone number), and the leads are made by tools/credit_scan.py `merge`
(leads() below). Nothing here contacts the organisations' own servers: only DNS resolvers are asked.
A provider counts only when (1) its own site proves it is in Canada, (2) its own site describes a hosting / e-mail / IT / software service,
(3) at least MIN_CLIENTS unrelated domains name it (a parent organisation in a subsidiary's SPF record is not a vendor), (4) it is not a
service with a free plan (FREE). Wholesale platforms sold through resellers (Tucows OpenSRS hosted e-mail) are left out: the organisation pays
the reseller, not the platform.
"""
import argparse, collections, csv, glob, gzip, hashlib, json, os, random, re, sys, threading, time

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ap_crawler as C  # noqa: E402

INC = os.path.join(ROOT, "data/incoming/claude")
DIR = os.path.join(INC, "credit_scan")
SEEN_TABLE = os.path.join(DIR, "dns_providers_seen.csv")
TODAY = time.strftime("%Y-%m-%d")
RESOLVERS = ["1.1.1.1", "8.8.8.8", "9.9.9.9", "1.0.0.1", "8.8.4.4", "149.112.112.112"]
MIN_CLIENTS = 8
CF_DNS = "service of a Canada-located vendor seen in the buyer's public DNS (tech)"
# the giants and other providers that are certainly not Canada-located: never checked, never a lead (saves the live check)
NOT_CA = re.compile(r"(^|\.)(outlook\.com|google\.com|googlemail\.com|secureserver\.net|mcsv\.net|sendgrid\.net|mailgun\.org|amazonses\.com|amazonaws\.com|hubspotemail\.net|mandrillapp\.com|"
                    r"zoho\.(com|eu|in)|zohocloud\.ca|zcsend\.(net|ca)|zohomail\.com|zeptomail\.net|transmail\.net|hostinger\.com|mlsend\.com|salesforce\.com|pardot\.com|ppe-hosted\.com|pphosted\.com|"
                    r"hornetsecurity\.com|barracudanetworks\.com|mimecast\.com|zendesk\.com|knowbe4\.com|smtp2go\.com|constantcontact\.com|createsend\.com|sendinblue\.com|brevo\.com|mailjet\.com|"
                    r"ionos\.com|1and1\.com|kundenserver\.de|perfora\.net|websitewelcome\.com|bluehost\.com|dreamhost\.com|a2hosting\.com|greengeeks\.net|web-hosting\.com|registrar-servers\.com|"
                    r"privateemail\.com|jellyfish\.systems|titan\.email|emailsrvr\.com|cloudflare\.(net|com)|mailchannels\.net|oxcs\.net|iphmx\.com|sophos\.com|trendmicro\.com|titanhq\.com|"
                    r"protonmail\.ch|icloud\.com|yahoodns\.net|messagingengine\.com|improvmx\.com|gandi\.net|porkbun\.com|squarespace-mail\.com|squarespace\.com|wixdns\.net|wix\.com|domaincontrol\.com|"
                    r"godaddy\.com|namecheap\.com|awsdns-\d+\.(com|net|org|co\.uk)|azure-dns\.(com|net|org|info)|nsone\.net|ultradns\.(com|net|org|biz)|dnsmadeeasy\.com|digitalocean\.com|linode\.com|"
                    r"exclaimer\.net|emailsignatures365\.com|blackbaud\.net|yardi\.com|intacct\.com|qualtrics\.com|oraclecloud\.com|atlassian\.net|mktomail\.com|sparkpostmail\.com|mailersend\.net|"
                    r"antispamcloud\.com|spamexperts\.(com|net|eu)|mailspamprotection\.com|siteground\.(com|net)|kinsta\.com|wpengine\.com|wpcloud\.com|netlify\.com|vercel-dns\.com|shopify\.com|myshopify\.com|"
                    r"easydmarc\.pro|dmarcian\.com|valimail\.com|ondmarc\.com|agari\.com|proofpoint\.com|fireeyecloud\.com|mx\.microsoft|msv1\.invalid|mtasv\.net|postmarkapp\.com|mailhop\.org|dynect\.net|"
                    r"megamailservers\.com|registeredsite\.com|networksolutions\.com|web\.com|wordpress\.com|automattic\.com|hostgator\.com|inmotionhosting\.com|liquidweb\.com|rackspace\.com|"
                    r"serverdata\.net|intermedia\.net|arsmtp\.com|appriver\.com|fortimailcloud\.com|forwardemail\.net|mxroute\.com|mxrouting\.net|zohobooks\.com|freshdesk\.com|freshemail\.io|"
                    r"klaviyomail\.com|activecampaign\.com|acems\d\.com|emsd1\.com|md02\.com|informz\.net|cvent\.com|ultipro\.com|adp\.com|paubox\.com|schoolmessenger\.com|autotask\.net|myconnectwise\.net)$", re.I)
# Canada-based services with a free plan, or sold only through resellers: their records are not proof of a payment by the organisation
FREE = re.compile(r"(^|\.)(cyberimpact\.com|wildapricot\.(org|com)|zeffy\.com|thinkific\.com|vidyard\.com|hostedemail\.com|opensrs\.(com|net)|tucows\.com|hover\.com|elasticemail\.com|"
                  r"canadahelps\.org|hootsuite\.com)$", re.I)
SERVICE_RX = re.compile(r"h[ée]berg|hosting|\bhost\b|domain|domaine|e-?mail|courriel|internet|t[ée]l[ée]com|managed|infog[ée]rance|\bIT\b|\bTI\b|informati|cloud|data ?cent|web|logiciel|software|"
                        r"s[ée]curit|marketing|\bcrm\b|platform|plateforme|solution|technolog|digital|num[ée]rique|network|r[ée]seau|server|serveur|saas|app\b", re.I)
# a provider's technical domain -> the domain of its public site, with the provider's own statement that the technical domain is its own
# (a page that was opened, its date). Only such stated aliases count: a technical domain nobody claims in public makes no lead.
_WHC = ("whc.ca", "https://help.whc.ca/en/articles/618475-how-to-update-the-dns-records-a-aaaa-cname-mx-txt-srv-for-my-domain",
        "Your DNS is hosted with us if your nameservers end in whc.ca, wpdns.ca, web-dns1.com or mywhc.ca.", "2026-11-10")
ALIAS = {"web-dns1.com": _WHC, "wpdns.ca": _WHC, "mywhc.ca": _WHC}
SHOPIFY_A = re.compile(r"^23\.227\.38\.(?:3[2-9]|[4-9]\d|1[01]\d|12[0-7])$")  # Shopify's storefront addresses (23.227.38.32/27, .64/26): the apex A record of a store on its own domain
VERIF_KEY = re.compile(r"^([a-z0-9][a-z0-9._-]{2,48}?)[=:]")
# TXT verification keys of vetted Canada-HQ vendors -> vendor domain (each needs a business account with that vendor; quotes in tools/tech_relationships.py or DECISIONS.md)
TXT_VENDOR = {}


def state_files(prefix):
    return sorted(glob.glob(os.path.join(DIR, prefix + "_*.gz")))


def records():
    """every DNS record set on file, one dict per domain: {"d", "t", "mx": [hosts], "ns": [hosts], "inc": [SPF include hosts], "txt": [keys]}.
    The cloud lookups first; then the MX / SPF checks the Mac ran on the dataset's buyers (2026-11-04 … 2026-11-08) for domains not looked up since."""
    seen = set()
    for p in state_files("dns"):
        with gzip.open(p, "rt", encoding="utf-8", errors="replace") as f:
            for l in f:
                try:
                    o = json.loads(l)
                except ValueError:
                    continue
                if o.get("d") and o["d"] not in seen:
                    seen.add(o["d"])
                    yield o
    legacy = {}
    p = os.path.join(INC, "claude_dmarc_check.tsv")
    if os.path.exists(p):
        for r in csv.DictReader(open(p, encoding="utf-8", errors="replace"), delimiter="\t"):
            rec = (r.get("spf_record") or "").strip()
            if rec.lower().startswith("v=spf1") and r.get("domain") and r["domain"] not in seen:
                legacy[r["domain"]] = {"d": r["domain"], "t": r.get("checked_date") or "", "mx": [], "ns": [], "txt": [], "spf": rec[:600],
                                       "inc": sorted(set(x.strip(".") for x in re.findall(r"(?:include:|redirect=)([a-z0-9._-]+)", rec.lower())))}
    p = os.path.join(INC, "claude_mx_check.tsv")
    if os.path.exists(p):
        for r in csv.DictReader(open(p, encoding="utf-8", errors="replace"), delimiter="\t"):
            if r.get("status") == "mx" and r.get("domain") and r["domain"] not in seen:
                o = legacy.setdefault(r["domain"], {"d": r["domain"], "t": r.get("checked_date") or "", "mx": [], "ns": [], "txt": [], "inc": []})
                o["mx"] = [h.strip(".").lower() for h in re.split(r"[;, ]+", r.get("mail_hosts") or "") if "." in h][:6]
                o.setdefault("t_mx", r.get("checked_date") or "")
    for o in legacy.values():
        yield o


def providers_of(o):
    """[(kind, provider host, provider registrable domain)] of one domain's records, its own domain and its own name left out"""
    own = C.registrable(o["d"])
    lab = own.split(".")[0]
    out, seen = [], set()
    for kind, hosts in (("spf", o.get("inc") or []), ("mx", o.get("mx") or []), ("ns", o.get("ns") or [])):
        for h in hosts:
            h = (h or "").strip(".").lower()
            if not h or "." not in h or not re.fullmatch(r"[a-z0-9._-]+", h):
                continue
            pd = C.registrable(h)
            if pd == own or (len(lab) >= 5 and lab in pd) or (kind, pd) in seen:
                continue
            seen.add((kind, pd))
            out.append((kind, h, pd))
    for key in o.get("txt") or []:
        if key in TXT_VENDOR and ("txt", TXT_VENDOR[key]) not in seen:
            seen.add(("txt", TXT_VENDOR[key]))
            out.append(("txt", key, TXT_VENDOR[key]))
    return out


def vendor_of(pd):
    """the public domain of the provider behind a technical domain (ALIAS), else the domain itself"""
    return ALIAS[pd][0] if pd in ALIAS else pd


def provider_counts():
    """{provider's public domain: number of distinct client domains}, all kinds together; and per kind"""
    tot, by = collections.Counter(), collections.defaultdict(collections.Counter)
    for o in records():
        ps = providers_of(o)
        for vd in {vendor_of(p[2]) for p in ps}:
            tot[vd] += 1
        for kind, vd in {(p[0], vendor_of(p[2])) for p in ps}:
            by[vd][kind] += 1
    return tot, by


def candidates(limit=2500):
    """provider domains worth one live check of their own site: named by MIN_CLIENTS+ client domains, not a known foreign giant"""
    tot, _ = provider_counts()
    return [(pd, c) for pd, c in tot.most_common() if c >= MIN_CLIENTS and not NOT_CA.search(pd) and not FREE.search(pd)][:limit]


# ------------------------------------------------------------------------------------------------------------------- lookup
def queue(k, n, limit=0):
    import credit_scan as CS
    done = set()
    for p in state_files("dns"):
        with gzip.open(p, "rt", encoding="utf-8", errors="replace") as f:
            for l in f:
                i = l.find('"d": "')
                if i >= 0:
                    done.add(l[i + 6:l.find('"', i + 6)])
    seen, tasks = set(), []

    def add(host, pri):
        if not host or "." not in host:
            return
        d = C.registrable(host)
        if d in seen or d in done or CS.PLATFORM.search(d) or not re.fullmatch(r"[a-z0-9.-]+", d) or int(hashlib.sha1(d.encode()).hexdigest(), 16) % n != k:
            return
        seen.add(d)
        tasks.append((pri, d))
    rp = os.path.join(ROOT, "coord/results/ranked/ranked_buyers.csv.gz")
    if os.path.exists(rp):
        with gzip.open(rp, "rt", encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                add(CS.host_of(r.get("buyer_website")), 0)
    for p in (os.path.join(INC, "claude_buyer_leads_cc.csv"), os.path.join(INC, "claude_buyer_leads.csv")):
        if os.path.exists(p):
            for r in csv.DictReader(open(p, encoding="utf-8", errors="replace")):
                add(CS.host_of(r.get("website")), 1)
    for path, pri in ((CS.GRAPH_IN, 2), (CS.OSM_SITES, 2), (CS.UNIVERSE, 3), (CS.GRAPH_CA, 4)):
        if os.path.exists(path):
            with gzip.open(path, "rt", encoding="utf-8", newline="") as fh:
                for r in csv.DictReader(fh):
                    add(r["dom"], pri)
    tasks.sort()
    if limit:
        tasks = tasks[:limit]
    return [d for _, d in tasks], len(done)


QPS = 500  # queries per second of one runner, spread over six public resolver addresses (Google's published limit alone is 1,500 per client address)


def lookup(a):
    import dns.exception
    import dns.resolver
    k, n = (int(x) for x in (a.shard.split("/") + ["1"])[:2])
    os.makedirs("out", exist_ok=True)
    doms, n_done = queue(k, max(1, n), a.limit)
    print("shard %d/%d: %d domains to look up (%d looked up before)" % (k, n, len(doms), n_done), flush=True)
    deadline = time.time() + a.minutes * 60
    tl = threading.local()
    gate, nxt = threading.Lock(), [0.0]

    def turn():
        with gate:
            t = max(time.time(), nxt[0])
            nxt[0] = t + 1.0 / QPS
        w = t - time.time()
        if w > 0:
            time.sleep(w)

    def resolver():
        r = getattr(tl, "r", None)
        if r is None:
            r = dns.resolver.Resolver(configure=False)
            r.nameservers = random.sample(RESOLVERS, 3)
            r.timeout, r.lifetime = 2.5, 5.0
            tl.r = r
        return r

    def ask(d, typ):
        """(strings, status): status ok | none (no such record) | nx (no such domain) | fail"""
        turn()
        try:
            ans = resolver().resolve(d, typ, raise_on_no_answer=False)
        except dns.resolver.NXDOMAIN:
            return [], "nx"
        except dns.exception.DNSException:
            return [], "fail"
        if ans.rrset is None:
            return [], "none"
        if typ == "TXT":
            return [b"".join(x.strings).decode("utf-8", "replace") for x in ans], "ok"
        if typ == "MX":
            return [str(x.exchange).rstrip(".").lower() for x in sorted(ans, key=lambda x: x.preference)], "ok"
        if typ == "A":
            return [x.address for x in ans], "ok"
        return [str(x.target).rstrip(".").lower() for x in ans], "ok"
    lock, stats = threading.Lock(), collections.Counter()
    f = open("out/dns_%d.jsonl" % k, "a", encoding="utf-8")

    def one(d):
        if time.time() > deadline:
            return
        ns, st = ask(d, "NS")
        o = {"d": d, "t": TODAY, "st": st}
        if st in ("ok", "none"):
            if ns:
                o["ns"] = ns[:4]
            txt, st_t = ask(d, "TXT")
            spf = next((x for x in txt if x.lower().startswith("v=spf1")), "")
            if spf:
                inc = sorted(set(x.strip(".") for x in re.findall(r"(?:include:|redirect=)([a-z0-9._-]+)", spf.lower())))[:12]
                if inc:
                    o["inc"] = inc
                if any(not NOT_CA.search(C.registrable(x)) for x in inc if "." in x):
                    o["spf"] = spf[:400]  # kept as the quote of a lead; records that name only the giants are not kept in full
            keys = set()
            for x in txt:
                m = VERIF_KEY.match(x.lower())
                if m and not x.lower().startswith(("v=spf1", "v=dkim", "v=dmarc")):
                    keys.add(m.group(1)[:48])
            if keys:
                o["txt"] = sorted(keys)[:20]
            mx = ask(d, "MX")[0]
            if mx:
                o["mx"] = mx[:4]
            ip = ask(d, "A")[0]
            if ip:
                o["a"] = ip[0]
                if SHOPIFY_A.match(ip[0]):
                    o["shop"] = 1
        with lock:
            stats["domains"] += 1
            stats[st] += 1
            stats["with_spf"] += "inc" in o or "spf" in o
            stats["with_mx"] += "mx" in o
            stats["shopify_address"] += "shop" in o
            if st != "fail":  # a failed lookup is asked again next time
                f.write(json.dumps(o, ensure_ascii=False, separators=(",", ": ")) + "\n")
            if stats["domains"] % 20000 == 0:
                f.flush()
                print(time.strftime("%H:%M:%S"), dict(stats), flush=True)
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(one, doms))
    f.close()
    print("finished", dict(stats), flush=True)


def merge(a):
    os.makedirs(DIR, exist_ok=True)
    stamp = a.stamp or time.strftime("%Y%m%dT%H%M%S", time.gmtime())
    have = set()
    for o in records():
        have.add(o["d"])
    n = 0
    for f in sorted(glob.glob(os.path.join(a.dir, "dns_*.jsonl"))):
        lines = []
        for l in open(f, encoding="utf-8"):
            i = l.find('"d": "')
            d = l[i + 6:l.find('"', i + 6)] if i >= 0 else ""
            if d and d not in have and l.strip():
                lines.append(l.rstrip("\n"))
        if lines:
            k = re.search(r"dns_(\d+)\.jsonl$", f).group(1)
            with gzip.open(os.path.join(DIR, "dns_%s_%s.gz" % (stamp, k)), "wt", encoding="utf-8") as g:
                g.write("\n".join(lines) + "\n")
            n += len(lines)
    tot, by = provider_counts()
    with open(SEEN_TABLE, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["provider_domain", "client_domains", "spf", "mx", "ns", "txt"])
        for pd, c in tot.most_common(4000):
            if c >= 3:
                w.writerow([pd, c, by[pd]["spf"], by[pd]["mx"], by[pd]["ns"], by[pd]["txt"]])
    keys = collections.Counter()
    for o in records():
        keys.update(o.get("txt") or [])
    print("DNS records on file: %d domains (+%d this run); providers named by %d+ domains and not a known foreign giant: %d; most frequent TXT keys: %s"
          % (len(have) + n, n, MIN_CLIENTS, len(candidates(100000)), ", ".join("%s %d" % kv for kv in keys.most_common(25))))


# ------------------------------------------------------------------------------------------------------------------- leads (called by credit_scan.merge)
KIND_TEXT = {"spf": ("e-mail / web hosting", "its SPF record authorises %s to send its e-mail"), "mx": ("e-mail service", "its mail is received by %s (MX record)"),
             "ns": ("DNS / web hosting", "its DNS zone is served by %s (NS record)"), "txt": ("business account", "its DNS carries the vendor's domain-verification record “%s=…”")}


def leads(prev, pdet, proof, main_keys, vstate, stats, names=None, in_canada=None, kept=None):
    """add / refresh the DNS leads in prev (lead rows) and pdet (details). proof(domain) -> (address text, url, name, service?, basis) or None
    (tools/credit_scan.py: the provider's own site prints its Canadian address, on its own pages). One lead per client domain: the provider with
    the strongest record kind (MX and NS say where mail and the zone ARE today; an SPF include alone may be a leftover, so it counts only when
    another record agrees or the provider is the only outside sender the record names), then the provider most domains name."""
    tot, _ = provider_counts()
    rank = {"mx": 0, "ns": 1, "spf": 2, "txt": 3}
    for o in records():
        d = o["d"]
        ps = providers_of(o)
        kinds = collections.defaultdict(set)
        for kind, h, pd in ps:
            kinds[vendor_of(pd)].add(kind)
        outside_senders = {vendor_of(pd) for kind, h, pd in ps if kind == "spf"}
        best = None
        for kind, h, pd in ps:
            vend = vendor_of(pd)
            if tot[vend] < MIN_CLIENTS or NOT_CA.search(pd) or FREE.search(pd) or NOT_CA.search(vend) or FREE.search(vend) or vend == C.registrable(d):
                continue
            if kind == "spf" and len(kinds[vend]) < 2 and len(outside_senders) > 1:
                stats["DNS: SPF include alone, next to other senders (may be a leftover; kept out)"] += 1
                continue
            pr = proof(vend)
            if not pr:
                stats["DNS: provider not proven in Canada (yet)"] += 1
                continue
            vs = vstate.get(vend) or {}
            if not SERVICE_RX.search(" ".join(str(vs.get(x) or "") for x in ("title", "desc", "name", "service_words"))):
                stats["DNS: provider's own site names no hosting / IT / software service (kept out)"] += 1
                continue
            if vs.get("free_signal"):
                stats["DNS: provider advertises a free plan (kept out)"] += 1
                continue
            if vs.get("also_prints") and in_canada and not in_canada(d, None):
                stats["DNS: provider also prints addresses abroad and the buyer is not shown to be in Canada (kept out)"] += 1
                continue
            cand = (rank[kind], -tot[vend], kind, h, pd, vend, pr)
            if best is None or cand[:2] < best[:2]:
                best = cand
        if not best:
            continue
        _, _, kind, h, pd, vend, pr = best
        key = "lead:" + hashlib.sha1(("%s|dns:%s" % (d, vend)).encode()).hexdigest()[:16]
        if key in main_keys:
            continue
        what, how = KIND_TEXT[kind]
        date = (o.get("t_mx") if kind == "mx" and o.get("t_mx") else o.get("t")) or TODAY
        quote = (o.get("spf") or "")[:260] if kind == "spf" else "%s %s %s" % (d, kind.upper(), h)
        vname = pr[2] or vend
        also = sorted(kinds[vend] - {kind})
        alias = ""
        if pd in ALIAS:
            alias = "%s is %s's own technical domain: “%s” (%s, read %s)" % (pd, vname, ALIAS[pd][2], ALIAS[pd][1], ALIAS[pd][3])
        stats["DNS leads (%s)" % kind] += 1
        if key not in prev:
            stats["new DNS leads"] += 1
        if kept is not None:
            kept.add(key)
        prev[key] = {"buyer_key": key, "buyer_name": (names or {}).get(d) or d, "website": "https://%s/" % d, "canadian_vendor_rows": 1, "example_vendor": vname,
                     "canada_field_value": "%s=%s; %s: %s" % (CF_DNS, vend, pr[4], pr[0][:240]),
                     "evidence_dataset": "https://dns.google/resolve?name=%s&type=%s" % (d, {"spf": "TXT", "txt": "TXT", "mx": "MX", "ns": "NS"}[kind]), "latest_record_date": date}
        pdet[key] = {"key": key, "platform": "dns_service_cc", "record_url": prev[key]["evidence_dataset"], "vendor": vname, "record_date": date,
                     "title": "%s by %s — %s: “%s”" % (what, vname, how % h, quote[:200]),
                     "vendor_address": pr[0], "vendor_address_url": pr[1], "vendor_site": "https://%s/" % vend, "dns_record_kind": kind, "dns_record": quote, "dns_provider_host": h,
                     "dns_provider_domain": pd, "dns_other_records_naming_the_provider": ",".join(also), "dns_alias_basis": alias, "provider_client_domains": tot[vend],
                     "vendor_location_basis": pr[4], "vendor_also_prints_addresses_in": (vstate.get(vend) or {}).get("also_prints") or "",
                     "relationship_note": "the service is rendered to this domain today; when a web agency or IT firm manages the account, the provider may bill that firm"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["lookup", "merge", "table"])
    ap.add_argument("dir", nargs="?", default="shards")
    ap.add_argument("--shard", default="0/1")
    ap.add_argument("--minutes", type=float, default=100)
    ap.add_argument("--workers", type=int, default=120)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--stamp", default="")
    a = ap.parse_args()
    if a.cmd == "lookup":
        lookup(a)
    elif a.cmd == "merge":
        merge(a)
    else:
        tot, by = provider_counts()
        for pd, c in tot.most_common(200):
            print("%6d %-34s %s%s" % (c, pd, dict(by[pd]), "  [not CA]" if NOT_CA.search(pd) else "  [free / wholesale]" if FREE.search(pd) else ""))


if __name__ == "__main__":
    main()
