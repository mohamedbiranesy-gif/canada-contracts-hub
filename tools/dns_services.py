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
  sweep --shard K/8 [--minutes M]    every domain of Common Crawl's domain graph (118 M) on the endings most stores use (SWEEP_TLDS): ONE question
                                     each — is its address record on Shopify's storefront network? Only the stores found are kept (they join the
                                     records above, so the store crawl reads them), with the place in the list where the shard stopped
                                     (sweep_cursor.json): the next run goes on from there. `sweep-plan` prints the shards that still have work.
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
NOT_CA = re.compile(r"(^|\.)(wixdns\.net|wix\.com|squarespace\.com|github\.io|netlify\.app|vercel\.app|vercel-dns\.com|azurewebsites\.net|cloudfront\.net|herokuapp\.com|herokudns\.com|"
                    r"wpengine\.com|wpenginepowered\.com|pantheonsite\.io|kinsta\.cloud|webflow\.io|webflow\.com|weebly\.com|wordpress\.com|ghs\.googlehosted\.com|googlehosted\.com|"
                    r"hubspot\.net|hs-sites\.com|bigcommerce\.com|godaddysites\.com|strikingly\.com|duda\.co|multiscreensite\.com|cargo\.site|framer\.app|fastly\.net|akamaiedge\.net|"
                    r"edgekey\.net|edgesuite\.net|azureedge\.net|trafficmanager\.net|elasticbeanstalk\.com|elb\.amazonaws\.com|incapdns\.net|sucuri\.net|cdn\.cloudflare\.net|"
                    r"outlook\.com|google\.com|googlemail\.com|secureserver\.net|mcsv\.net|sendgrid\.net|mailgun\.org|amazonses\.com|amazonaws\.com|hubspotemail\.net|mandrillapp\.com|"
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
# Canada-based services with a free plan, or sold only through resellers: their records are not proof of a payment by the organisation.
# (2026-11-10: hover.com taken off this list — Hover is Tucows' RETAIL registrar, its customers pay it directly; the automatic provider test decides.
# Tucows' wholesale platforms — OpenSRS, hostedemail.com under a reseller's name — stay out: the organisation pays the reseller.)
FREE = re.compile(r"(^|\.)(cyberimpact\.com|wildapricot\.(org|com)|zeffy\.com|thinkific\.com|vidyard\.com|hostedemail\.com|opensrs\.(com|net)|tucows\.com|elasticemail\.com|"
                  r"canadahelps\.org|hootsuite\.com)$", re.I)
SERVICE_RX = re.compile(r"h[ée]berg|hosting|\bhost\b|domain|domaine|e-?mail|courriel|internet|t[ée]l[ée]com|managed|infog[ée]rance|\bIT\b|\bTI\b|informati|cloud|data ?cent|web|logiciel|software|"
                        r"s[ée]curit|marketing|\bcrm\b|platform|plateforme|solution|technolog|digital|num[ée]rique|network|r[ée]seau|server|serveur|saas|app\b", re.I)
# a provider's technical domain -> the domain of its public site, with the provider's own statement that the technical domain is its own
# (a page that was opened, its date). Only such stated aliases count: a technical domain nobody claims in public makes no lead.
_WHC = ("whc.ca", "https://help.whc.ca/en/articles/618475-how-to-update-the-dns-records-a-aaaa-cname-mx-txt-srv-for-my-domain",
        "Your DNS is hosted with us if your nameservers end in whc.ca, wpdns.ca, web-dns1.com or mywhc.ca.", "2026-11-10")
ALIAS = {"web-dns1.com": _WHC, "wpdns.ca": _WHC, "mywhc.ca": _WHC}
# the sweep (2026-11-10): the store crawl accepts ~24 % of the stores it reads, and the stores on file (542,022: the domains that LINK to Shopify
# and whose address record confirmed it) last about two days of crawling. A store that removed the "Powered by Shopify" link is in no such list;
# its address record still says where it is hosted. Endings: where Shopify Inc. (Ottawa) is the contracting party — Canada and the United States.
SWEEP_TLDS = ("com", "net", "org", "co", "us", "shop", "store")
SWEEP_SHARDS = 8   # fixed: a shard's place in the list is only meaningful for one way of cutting the list
CURSOR = os.path.join(DIR, "sweep_cursor.json")
SHOPIFY_A = re.compile(r"^23\.227\.38\.(?:3[2-9]|[4-9]\d|1[01]\d|12[0-7])$")  # Shopify's storefront addresses (23.227.38.32/27, .64/26): the apex A record of a store on its own domain
VERIF_KEY = re.compile(r"^([a-z0-9][a-z0-9._-]{2,48}?)[=:]")
# TXT verification keys of vetted Canada-HQ vendors -> vendor domain (each needs a business account with that vendor; quotes in tools/tech_relationships.py or DECISIONS.md)
TXT_VENDOR = {"1password-site-verification": "1password.com"}
# vendors read by hand once (terms opened, quoted): the DNS record is theirs by name, their contracting company and its address are stated in
# their own agreement. They need no client count and no live address check.
VETTED = {
    "1password.com": dict(name="AgileBits Inc. dba 1Password", address="4711 Yonge Street, 10th Floor, Toronto, Ontario, M2N 6K8, Canada",
                          url="https://1password.com/legal/terms-of-service", read="2026-11-10",
                          quote="This Subscription Agreement is entered into by and between AgileBits Inc. dba 1Password",
                          what="password manager for the organisation's staff (business subscription)",
                          basis="the vendor's subscription agreement names one contracting company for every customer, AgileBits Inc. dba 1Password, Toronto; the "
                                "domain's 1password-site-verification record was added by the owner of a 1Password Teams or Business account (support page, read "
                                "2026-11-10, https://support.1password.com/breach-report/: “With 1Password Teams and 1Password Business, you can create a report” … “add "
                                "a DNS text (TXT) record containing the verification string to the domain you want to verify”); both are paid subscriptions (a "
                                "trial account could add the record too)"),
}


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
        import parted_csv as _PC  # the file is written in parts (tools/dmarc_check.py)
        for r in _PC.rows(p, delimiter="\t"):
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
    for kind, hosts in (("spf", o.get("inc") or []), ("mx", o.get("mx") or []), ("ns", o.get("ns") or []), ("cname", [o["cn"]] if o.get("cn") else [])):
        for h in hosts:
            h = (h or "").strip(".").lower()
            if not h or "." not in h or not re.fullmatch(r"[a-z0-9._-]+", h):
                continue
            pd = C.registrable(h)
            if h.endswith(".hover.com.cust.hostedemail.com"):
                pd = "hover.com"  # Hover's own mail service on Tucows' platform (mx.hover.com.cust.hostedemail.com); other names on that platform belong to resellers
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

    def add(host, pri, light=False):
        if not host or "." not in host:
            return
        d = C.registrable(host)
        if d in seen or d in done or CS.PLATFORM.search(d) or not re.fullmatch(r"[a-z0-9.-]+", d) or int(hashlib.sha1(d.encode()).hexdigest(), 16) % n != k:
            return
        seen.add(d)
        tasks.append((pri, d, light))
    import ranked_io
    for r in ranked_io.rows():
        add(CS.host_of(r.get("buyer_website")), 0)
    import lead_store as LS
    for p in (os.path.join(INC, "claude_buyer_leads_cc.csv"), os.path.join(INC, "claude_buyer_leads.csv")):
        if os.path.exists(p):
            for r in LS.reader(p):
                add(CS.host_of(r.get("website")), 1)
    for path, pri in ((CS.GRAPH_IN, 2), (CS.OSM_SITES, 2), (CS.UNIVERSE, 3), (CS.GRAPH_CA, 4)):
        if os.path.exists(path):
            with gzip.open(path, "rt", encoding="utf-8", newline="") as fh:
                for r in csv.DictReader(fh):
                    add(r["dom"], pri)
    # store candidates (1.3 M domains that link to Shopify, most of them abroad): only the question that matters for them — is the domain on
    # Shopify's storefront addresses? (A record + the www alias: 2 queries, a 40-byte record). Asked before the .ca lists of pri 3-4.
    if os.path.exists(CS.GRAPH_SHOP):
        with gzip.open(CS.GRAPH_SHOP, "rt", encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                add(r["dom"], 2, light=True)
    tasks.sort()
    if limit:
        tasks = tasks[:limit]
    return [(d, light) for _, d, light in tasks], len(done)


# First cloud test (2026-11-10, 3,000 domains through the public resolvers at 500 queries/s): 45 % of the lookups timed out — public resolvers
# throttle a data-centre address. The lookups now go through a recursive resolver that the workflow starts on the runner itself (unbound, no
# forwarding): it asks each zone's own name servers, as every resolver does, and --qps caps the runner's total (default 480 = 120 domains/s).


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
    local = None
    if a.resolver:
        host, _, port = a.resolver.partition(":")
        probe = dns.resolver.Resolver(configure=False)
        probe.nameservers, probe.port, probe.timeout, probe.lifetime = [host], int(port or 53), 5, 10
        for _ in range(6):  # the runner's own resolver needs a few seconds to start
            try:
                probe.resolve("cira.ca", "NS")
                local = (host, int(port or 53))
                break
            except Exception as e:
                print("local resolver not answering yet: %s" % type(e).__name__, flush=True)
                time.sleep(5)
    qps = a.qps if local else min(a.qps, 60)  # without the local resolver: the public ones, slowly
    print("resolver: %s, %d queries/s" % ("%s:%d (local, recursive)" % local if local else "public resolvers", qps), flush=True)

    def turn():
        with gate:
            t = max(time.time(), nxt[0])
            nxt[0] = t + 1.0 / qps
        w = t - time.time()
        if w > 0:
            time.sleep(w)

    def resolver():
        r = getattr(tl, "r", None)
        if r is None:
            r = dns.resolver.Resolver(configure=False)
            if local:
                r.nameservers, r.port = [local[0]], local[1]
                r.timeout, r.lifetime = 8.0, 8.0
            else:
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

    def one(task):
        d, light = task
        if time.time() > deadline:
            return
        if light:  # a store candidate: only its address record and its www alias
            ip, st = ask(d, "A")
            o = {"d": d, "t": TODAY, "st": st, "l": 1}
            if ip:
                if SHOPIFY_A.match(ip[0]):
                    o["shop"], o["a"] = 1, ip[0]
            if st != "nx" and "shop" not in o:
                cn = ask("www." + d, "CNAME")[0]
                if cn and cn[0].endswith("myshopify.com"):
                    o["shop"], o["cn"] = 1, cn[0]
            with lock:
                stats["domains"] += 1
                stats["store_candidates"] += 1
                stats["shopify_address"] += "shop" in o
                if st != "fail" or local:
                    f.write(json.dumps(o, ensure_ascii=False, separators=(",", ": ")) + "\n")
                if stats["domains"] % 20000 == 0:
                    f.flush()
                    print(time.strftime("%H:%M:%S"), dict(stats), flush=True)
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
            cn = ask("www." + d, "CNAME")[0]  # the platform that serves the site: www.<domain> is an alias of <shop>.myshopify.com, <site>.thinkific.com, a web host's server …
            if cn and C.registrable(cn[0]) != d:
                o["cn"] = cn[0]
                if cn[0].endswith("myshopify.com"):
                    o["shop"] = 1
        with lock:
            stats["domains"] += 1
            stats[st] += 1
            stats["with_spf"] += "inc" in o or "spf" in o
            stats["with_mx"] += "mx" in o
            stats["shopify_address"] += "shop" in o
            if st != "fail" or local:  # through the local resolver a failure is the zone's own (dead name servers): kept, not asked again
                f.write(json.dumps(o, ensure_ascii=False, separators=(",", ": ")) + "\n")
            if stats["domains"] % 20000 == 0:
                f.flush()
                print(time.strftime("%H:%M:%S"), dict(stats), flush=True)
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(one, doms))
    f.close()
    print("finished", dict(stats), flush=True)


def sweep_cursor():
    try:
        return json.load(open(CURSOR, encoding="utf-8"))
    except Exception:
        return {}


def sweep_plan(a):
    """the sweep shards that still have work, least advanced first (for the workflow's matrix)"""
    cur = sweep_cursor()
    pos, done = cur.get("pos") or {}, cur.get("complete") or {}
    left = sorted((k for k in range(SWEEP_SHARDS) if not done.get(str(k))), key=lambda k: (int(pos.get(str(k), 0)), k))
    print(json.dumps(left[:max(1, a.limit or SWEEP_SHARDS)]))


def sweep(a):
    import subprocess
    import zlib
    import dns.exception
    import dns.resolver
    import credit_scan as CS
    import cc_clients as CCL
    k, n = int(a.shard.split("/")[0]), SWEEP_SHARDS
    os.makedirs("out", exist_ok=True)
    cur = sweep_cursor()
    rel = cur.get("release") or (a.release if a.release and a.release != "auto" else CS.newest_graph())
    tlds = tuple(cur.get("tlds") or SWEEP_TLDS)
    start = int((cur.get("pos") or {}).get(str(k), 0))
    state = {"release": rel, "tlds": list(tlds), "shard": k, "pos": start, "complete": bool((cur.get("complete") or {}).get(str(k))), "asked": 0, "stores": 0, "no_answer": 0}

    def save():
        with open("out/sweep_cursor_%d.json" % k, "w", encoding="utf-8") as fo:
            json.dump(state, fo)
    save()
    if k >= n or state["complete"]:
        print("sweep shard %d/%d: nothing left" % (k, n), flush=True)
        return
    work = next((d for d in (os.environ.get("RUNNER_TEMP") or "", ".") if d and os.access(d, os.W_OK)), ".")
    vfile = os.path.join(work, "vertices.txt.gz")
    url = a.base or "%sprojects/hyperlinkgraph/%s/domain/%s-domain-vertices.txt.gz" % (CCL.CC, rel, rel)
    t0 = time.time()
    if url.startswith("http"):
        subprocess.run(["curl", "-sS", "-L", "--fail", "--retry", "10", "--retry-delay", "10", "--retry-all-errors", "-C", "-", "-A", CCL.UA, "-o", vfile, url], check=True)
    else:
        vfile = url  # a local file (tests)
    print("sweep shard %d/%d of graph %s, endings %s: the list is %.0f MiB (%.0f s); starting after place %d" % (k, n, rel, ",".join(tlds), os.path.getsize(vfile) / 2 ** 20, time.time() - t0, start), flush=True)
    deadline = time.time() + a.minutes * 60
    local = None
    if a.resolver:
        host, _, port = a.resolver.partition(":")
        probe = dns.resolver.Resolver(configure=False)
        probe.nameservers, probe.port, probe.timeout, probe.lifetime = [host], int(port or 53), 5, 10
        for _ in range(6):
            try:
                probe.resolve("cira.ca", "NS")
                local = (host, int(port or 53))
                break
            except Exception as e:
                print("local resolver not answering yet: %s" % type(e).__name__, flush=True)
                time.sleep(5)
    qps = a.qps if local else min(a.qps, 60)  # without the runner's own resolver: the public ones, slowly
    print("resolver: %s, %d queries/s" % ("%s:%d (local, recursive)" % local if local else "public resolvers", qps), flush=True)
    tl = threading.local()
    gate, nxt = threading.Lock(), [0.0]

    def ask_a(d):
        with gate:
            t = max(time.time(), nxt[0])
            nxt[0] = t + 1.0 / qps
        w = t - time.time()
        if w > 0:
            time.sleep(w)
        r = getattr(tl, "r", None)
        if r is None:
            r = dns.resolver.Resolver(configure=False)
            if local:
                r.nameservers, r.port, r.timeout, r.lifetime = [local[0]], local[1], 6.0, 6.0
            else:
                r.nameservers, r.timeout, r.lifetime = random.sample(RESOLVERS, 3), 2.5, 5.0
            tl.r = r
        try:
            ans = r.resolve(d, "A", raise_on_no_answer=False)
        except dns.resolver.NXDOMAIN:
            return d, "", "nx"
        except dns.exception.DNSException:
            return d, "", "fail"
        if ans.rrset is None:
            return d, "", "none"
        return d, ans[0].address, "ok"

    pref = tuple(t + "." for t in tlds)
    ok_name = re.compile(r"[a-z0-9-]+(?:\.[a-z0-9-]+)+")

    def batches():
        pos, batch = 0, []
        with gzip.open(vfile, "rt", encoding="utf-8", errors="replace") as fh:
            for l in fh:
                q = l.split("\t")
                if len(q) < 2 or not q[1].startswith(pref):
                    continue
                pos += 1
                if pos <= start:
                    continue
                d = ".".join(reversed(q[1].strip().split(".")))
                if zlib.crc32(d.encode()) % n != k or len(d) > 80 or not ok_name.fullmatch(d) or CS.PLATFORM.search(d):
                    continue
                batch.append(d)
                if len(batch) >= a.batch:
                    yield pos, batch
                    batch = []
        if batch:
            yield pos, batch
        yield -1, []

    from concurrent.futures import ThreadPoolExecutor
    fo = open("out/dns_%d.jsonl" % k, "a", encoding="utf-8")
    with ThreadPoolExecutor(a.workers) as ex:
        for pos, batch in batches():
            if pos == -1:
                state["complete"] = True
                break
            if deadline - time.time() < 1.3 * len(batch) / qps + 20:
                break  # not enough time left for this batch: the next run starts with it
            st = collections.Counter()
            for d, ip, how in ex.map(ask_a, batch):
                st[how] += 1
                if ip and SHOPIFY_A.match(ip):
                    fo.write(json.dumps({"d": d, "t": TODAY, "st": "ok", "l": 1, "shop": 1, "a": ip, "sw": 1}, ensure_ascii=False, separators=(",", ": ")) + "\n")
                    state["stores"] += 1
            fo.flush()
            state["asked"] += len(batch)
            state["no_answer"] += st["fail"]
            state["pos"] = pos
            save()
            if state["asked"] % (10 * a.batch) == 0:
                print(time.strftime("%H:%M:%S"), "place %d: asked %d, stores %d, no answer %d (last batch: %s)" % (pos, state["asked"], state["stores"], state["no_answer"], dict(st)), flush=True)
    fo.close()
    save()
    print("finished: place %d%s; asked %d domains, %d on Shopify's storefront addresses, %d without an answer" % (
        state["pos"], " (end of the list)" if state["complete"] else "", state["asked"], state["stores"], state["no_answer"]), flush=True)


def merge(a):
    os.makedirs(DIR, exist_ok=True)
    stamp = a.stamp or time.strftime("%Y%m%dT%H%M%S", time.gmtime())
    have = set()  # domains with a cloud record (the MX / SPF checks made from the Mac are older and poorer: a cloud record replaces them)
    for pth in state_files("dns"):
        with gzip.open(pth, "rt", encoding="utf-8", errors="replace") as fh:
            for l in fh:
                i = l.find('"d": "')
                if i >= 0:
                    have.add(l[i + 6:l.find('"', i + 6)])
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
    cfiles = sorted(glob.glob(os.path.join(a.dir, "sweep_cursor_*.json")))
    if cfiles:  # the sweep: where each shard stopped (single writer: this merge)
        cur = sweep_cursor()
        cur.setdefault("pos", {}); cur.setdefault("complete", {})
        asked = stores = 0
        for cf in cfiles:
            try:
                o = json.load(open(cf, encoding="utf-8"))
            except Exception:
                continue
            if cur.get("release") and cur["release"] != o.get("release"):
                continue  # a shard that read another release of the list: its place means nothing here
            cur["release"], cur["tlds"], cur["shards"] = o["release"], o["tlds"], SWEEP_SHARDS
            ks = str(o["shard"])
            cur["pos"][ks] = max(int(cur["pos"].get(ks, 0)), int(o.get("pos") or 0))
            if o.get("complete"):
                cur["complete"][ks] = True
            asked += int(o.get("asked") or 0); stores += int(o.get("stores") or 0)
        cur["asked"] = int(cur.get("asked") or 0) + asked
        cur["stores_found"] = int(cur.get("stores_found") or 0) + stores
        cur["updated"] = time.strftime("%Y-%m-%dT%H:%MZ", time.gmtime())
        with open(CURSOR, "w", encoding="utf-8") as f:
            json.dump(cur, f, indent=1, sort_keys=True)
        print("sweep of graph %s (%s): +%d domains asked, +%d stores this run; %d asked and %d stores so far; shards finished: %d of %d" % (
            cur.get("release"), ",".join(cur.get("tlds") or []), asked, stores, cur["asked"], cur["stores_found"], len(cur["complete"]), SWEEP_SHARDS))
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
    shops = sum(1 for o in records() if o.get("shop"))
    print("DNS records from the cloud lookups: %d domains (+%d this run); stores on Shopify's addresses: %d; providers named by %d+ domains and not a known foreign giant: %d; "
          "most frequent TXT keys: %s" % (len(have) + n, n, shops, MIN_CLIENTS, len(candidates(100000)), ", ".join("%s %d" % kv for kv in keys.most_common(25))))


# ------------------------------------------------------------------------------------------------------------------- leads (called by credit_scan.merge)
KIND_TEXT = {"cname": ("website platform / hosting", "its website address (www) is an alias of %s (CNAME record)"),
             "spf": ("e-mail / web hosting", "its SPF record authorises %s to send its e-mail"), "mx": ("e-mail service", "its mail is received by %s (MX record)"),
             "ns": ("DNS / web hosting", "its DNS zone is served by %s (NS record)"), "txt": ("business account", "its DNS carries the vendor's domain-verification record “%s=…”")}


def leads(prev, pdet, proof, main_keys, vstate, stats, names=None, in_canada=None, kept=None):
    """add / refresh the DNS leads in prev (lead rows) and pdet (details). proof(domain) -> (address text, url, name, service?, basis) or None
    (tools/credit_scan.py: the provider's own site prints its Canadian address, on its own pages). One lead per client domain: the provider with
    the strongest record kind (MX and NS say where mail and the zone ARE today; an SPF include alone may be a leftover, so it counts only when
    another record agrees or the provider is the only outside sender the record names), then the provider most domains name."""
    tot, _ = provider_counts()
    rank = {"mx": 0, "cname": 0, "ns": 1, "spf": 2, "txt": 3}
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
            if vend in VETTED:  # a vendor read by hand: its own agreement is the proof
                v = VETTED[vend]
                pr = ("%s (%s: “%s”, read %s)" % (v["address"], v["url"], v["quote"], v["read"]), v["url"], v["name"], True, v["basis"])
                cand = (rank[kind], -10 ** 9, kind, h, pd, vend, pr)
                if best is None or cand[:2] < best[:2]:
                    best = cand
                continue
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
        if vend in VETTED:
            what = VETTED[vend]["what"]
        date = (o.get("t_mx") if kind == "mx" and o.get("t_mx") else o.get("t")) or TODAY
        quote = (o.get("spf") or "")[:260] if kind == "spf" else "%s TXT %s=…" % (d, h) if kind == "txt" else "%s %s %s" % (d, kind.upper(), h)
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
                     "evidence_dataset": "https://dns.google/resolve?name=%s&type=%s" % ("www." + d if kind == "cname" else d, {"spf": "TXT", "txt": "TXT", "mx": "MX", "ns": "NS", "cname": "CNAME"}[kind]),
                     "latest_record_date": date}
        pdet[key] = {"key": key, "platform": "dns_service_cc", "record_url": prev[key]["evidence_dataset"], "vendor": vname, "record_date": date,
                     "title": "%s by %s — %s: “%s”" % (what, vname, how % h, quote[:200]),
                     "vendor_address": pr[0], "vendor_address_url": pr[1], "vendor_site": "https://%s/" % vend, "dns_record_kind": kind, "dns_record": quote, "dns_provider_host": h,
                     "dns_provider_domain": pd, "dns_other_records_naming_the_provider": ",".join(also), "dns_alias_basis": alias, "provider_client_domains": tot[vend],
                     "vendor_location_basis": pr[4], "vendor_also_prints_addresses_in": (vstate.get(vend) or {}).get("also_prints") or "",
                     "relationship_note": "the service is rendered to this domain today; when a web agency or IT firm manages the account, the provider may bill that firm"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["lookup", "merge", "table", "sweep", "sweep-plan"])
    ap.add_argument("dir", nargs="?", default="shards")
    ap.add_argument("--shard", default="0/1")
    ap.add_argument("--minutes", type=float, default=100)
    ap.add_argument("--workers", type=int, default=120)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--stamp", default="")
    ap.add_argument("--resolver", default="", help="lookup: host:port of a recursive resolver on this machine (the workflow starts unbound); empty = public resolvers, slowly")
    ap.add_argument("--qps", type=int, default=480, help="lookup: queries per second of this runner")
    ap.add_argument("--batch", type=int, default=20000, help="sweep: domains asked between two saves of the shard's place")
    ap.add_argument("--release", default="auto", help="sweep: the web graph release (default: the one the sweep started with, else the newest)")
    ap.add_argument("--base", default="", help="sweep: URL or local path of the vertices file (tests)")
    a = ap.parse_args()
    if a.cmd == "sweep":
        sweep(a)
    elif a.cmd == "sweep-plan":
        sweep_plan(a)
    elif a.cmd == "lookup":
        lookup(a)
    elif a.cmd == "merge":
        merge(a)
    else:
        tot, by = provider_counts()
        for pd, c in tot.most_common(200):
            print("%6d %-34s %s%s" % (c, pd, dict(by[pd]), "  [not CA]" if NOT_CA.search(pd) else "  [free / wholesale]" if FREE.search(pd) else ""))


if __name__ == "__main__":
    main()
