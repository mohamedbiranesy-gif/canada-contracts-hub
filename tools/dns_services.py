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
  sweep --shard K/8 [--minutes M]    every domain of Common Crawl's domain graph (118 M) on the endings most stores use (SWEEP_TLDS): TWO questions
                                     each — is its address record on Shopify's storefront network, and do its name servers belong to a provider
                                     that already yields leads (sweep_ns_watch.txt: the Canadian hosts, registrars and DNS services proven so
                                     far)? Only the hits are kept (they join the records above: the store crawl reads the stores, leads() makes
                                     the DNS leads), with the place in the list where the shard stopped (sweep_cursor.json): the next run goes
                                     on from there; the part swept before the second question existed is caught up at the end. `sweep-plan`
                                     prints the shards that still have work.
  hosts --shard K/8 [--minutes M]    stores that live on a SUBDOMAIN (shop.brand.com, store.brand.com, us.brand.com …): the host-level web graph
                                     (243 M host names, 48 files) names 7.2 M three-label hosts of ordinary domains on the endings the sweep
                                     covers and .ca; each is asked one question (its address record). A host on Shopify's storefront network
                                     whose domain is not already a known store is kept like a sweep hit; `hosts-plan` prints the shards left.
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
# 2026-11-10: the sweep asks a second question of every domain — who serves its zone. Kept only when a name server belongs to a provider that
# already yields leads (its own site proves it in Canada: whc.ca, webnames.ca, easydns.com, hover.com … — 330 provider domains, 88,604 leads from
# the 4.1 M domains looked up so far, most of them .ca). The graph's 63 M domains hold the same providers' clients on .com / .net / .org: the
# Canadian businesses that are not on .ca. The list is written by the merge (single writer) from the leads on file.
NS_WATCH = os.path.join(DIR, "sweep_ns_watch.txt")
# 2 (2026-11-10): both sweeps start again from the first place of their lists. Until then the runner's resolver had been started from a shell
# that allows 1,024 open files: it shrank its tables to ~165 questions at a time and dropped the rest (measured, dns-diag.yml: 25-49 % of
# the questions dropped; 55-61 % of the sweep's names got no answer, while the public resolvers answer 97 % of the same names). A place
# reached before this number says nothing about the names behind it.
SWEEP_REV = 2
MAX_FAIL = 0.12  # the largest share of names without an answer a run may have and still be believed (the public resolvers: 3-4 % of a list's names)
PUBLIC_QPS = 60  # a name the runner's resolver gives no answer for is asked once of the public resolvers, at most this many a second
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
    for p in reversed(state_files("dns")):  # newest file first: a domain asked again (SWEEP_REV) is read from its newest record
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
def record_states():
    """(done, again): domains whose newest record stands (asked through the repaired resolver, or "no such domain", or a sweep hit), and
    domains whose record was written before SWEEP_REV — {domain: 0 no answer | 1 answered} — which are asked once more. Measured
    2026-11-10 on samples of the 4.13 M records: 1,796,196 say "no answer" (43 %) and a public resolver answers 88 % of them; 87 % of the
    answered records without an address do have one; 31 % of those without an SPF record have one."""
    st = {}
    for p in state_files("dns"):  # oldest first: the newest line of a domain decides
        with gzip.open(p, "rt", encoding="utf-8", errors="replace") as f:
            for l in f:
                i = l.find('"d": "')
                if i < 0:
                    continue
                d = l[i + 6:l.find('"', i + 6)]
                fail = '"st": "fail"' in l
                if '"rv": ' in l or '"st": "nx"' in l or '"sw": ' in l or ('"l": 1' in l and not fail):
                    st[d] = 2  # (a store candidate that did answer was asked one question: nothing of it was dropped — 0 of 500 re-asked were stores)
                else:
                    st[d] = 0 if fail else 1
    done = {d for d, v in st.items() if v == 2}
    return done, {d: v for d, v in st.items() if v != 2}


def queue(k, n, limit=0):
    import credit_scan as CS
    done, again = record_states()
    seen, tasks = set(), []

    def add(host, pri, light=False):
        if not host or "." not in host:
            return
        d = C.registrable(host)
        if d in seen or d in done or CS.PLATFORM.search(d) or not re.fullmatch(r"[a-z0-9.-]+", d) or int(hashlib.sha1(d.encode()).hexdigest(), 16) % n != k:
            return
        seen.add(d)
        ag = again.get(d)
        # asked before the resolver was repaired (SWEEP_REV): a record that says "no answer" first (stores before the rest: -3, -2), then the
        # never-asked domains in their usual order, then the records that did answer (a later question of theirs may have been dropped: +10)
        tasks.append(((-3 if light else -2) if ag == 0 else pri + 10 if ag == 1 else pri, d, light))
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
    return [(d, light) for _, d, light in tasks], len(done) + len(again)


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
    steady = SteadyResolver() if a.resolver == "steady" else None  # the public resolvers over one socket per worker (see SteadyResolver)
    if a.resolver and not steady:
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
    qps = a.qps if (local or steady) else min(a.qps, 60)  # without either: the public ones with a new socket per question, slowly
    print("resolver: %s, %d queries/s" % ("public resolvers, one socket per worker" if steady else "%s:%d (local, recursive)" % local if local else "public resolvers", qps), flush=True)

    lock, stats, fails = threading.Lock(), collections.Counter(), []

    def turn():
        with gate:
            t = max(time.time(), nxt[0])
            nxt[0] = t + 1.0 / qps
        w = t - time.time()
        if w > 0:
            time.sleep(w)

    def resolver():
        if steady:
            return steady
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

    ask_public = _public_asker(dns, tl) if local else None

    def ask(d, typ):
        """(strings, status): status ok | none (no such record) | nx (no such domain) | fail"""
        turn()
        try:
            ans = resolver().resolve(d, typ, raise_on_no_answer=False)
        except dns.resolver.NXDOMAIN:
            return [], "nx"
        except dns.exception.DNSException:
            if not ask_public:
                return [], "fail"
            try:  # no answer from the runner's resolver: asked once of the public resolvers before it counts as no answer
                ans = ask_public(d, typ)
                with lock:
                    stats["answered_by_the_public_resolvers"] += 1
            except dns.resolver.NXDOMAIN:
                return [], "nx"
            except dns.exception.DNSException:
                with lock:
                    stats["question_without_an_answer"] += 1
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
    f = open("out/dns_%d.jsonl" % k, "a", encoding="utf-8")

    def one(task):
        d, light = task
        if time.time() > deadline:
            return
        if light:  # a store candidate: only its address record and its www alias
            ip, st = ask(d, "A")
            o = {"d": d, "t": TODAY, "st": st, "l": 1, "rv": SWEEP_REV}
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
                stats["fail"] += st == "fail"
                (fails.append if st == "fail" else f.write)(json.dumps(o, ensure_ascii=False, separators=(",", ": ")) + "\n")
                if stats["domains"] % 20000 == 0:
                    f.flush()
                    print(time.strftime("%H:%M:%S"), dict(stats), flush=True)
            return
        ns, st = ask(d, "NS")
        o = {"d": d, "t": TODAY, "st": st, "rv": SWEEP_REV}
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
            (fails.append if st == "fail" else f.write)(json.dumps(o, ensure_ascii=False, separators=(",", ": ")) + "\n")
            if stats["domains"] % 20000 == 0:
                f.flush()
                print(time.strftime("%H:%M:%S"), dict(stats), flush=True)
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(one, doms))
    # A name without an answer is a fact about the name only when the run answered nearly everything else. 2026-11-10: 43 % of the records
    # on file said "no answer" because the questions never left the runner, and were never asked again. Above MAX_FAIL the names stay unasked.
    share = len(fails) / max(1, stats["domains"])
    if share <= MAX_FAIL:
        f.write("".join(fails))
    else:
        print("::warning::%.0f %% of the names got no answer (limit %.0f %%): this run's resolver is not trusted for them — %d names are left for the next run" % (
            100 * share, 100 * MAX_FAIL, len(fails)), flush=True)
    f.close()
    if steady:
        per = collections.defaultdict(dict)
        for (ip, what), c in steady.stats.items():
            per[ip][what] = c
        print("by resolver: " + "; ".join("%s %s" % (ip, dict(sorted(v.items()))) for ip, v in sorted(per.items())), flush=True)
    print("finished", dict(stats), flush=True)


def sweep_cursor():
    try:
        return json.load(open(CURSOR, encoding="utf-8"))
    except Exception:
        return {}


def ns_watch():
    try:
        return {l.strip() for l in open(NS_WATCH, encoding="utf-8") if l.strip() and not l.startswith("#")}
    except OSError:
        return set()


def write_ns_watch():
    """the name-server domains of the providers that yield leads today (lead details: platform dns_service_cc, record kind ns), plus the
    technical domains of ALIAS. Returns how many."""
    import lead_store as LS
    _, det = LS.load(details=True)
    doms = {d.get("dns_provider_domain") for d in det.values() if d.get("platform") == "dns_service_cc" and d.get("dns_record_kind") == "ns" and d.get("dns_provider_domain")}
    doms |= set(ALIAS) | {v for v in (a[0] for a in ALIAS.values())}
    doms = sorted(d for d in doms if re.fullmatch(r"[a-z0-9.-]+\.[a-z]{2,}", d) and not NOT_CA.search(d) and not FREE.search(d))
    if len(doms) >= 50:  # never replace the list by a stub (a run without the lead files)
        with open(NS_WATCH, "w", encoding="utf-8") as f:
            f.write("# name-server domains of providers that yield leads (tools/dns_services.py write_ns_watch); the sweep keeps a domain served by one of them\n" + "\n".join(doms) + "\n")
    return len(doms)


# ---- questions over a handful of long-lived flows -------------------------------------------------------------------------------------
# 2026-11-10, two measurements on runners (dns-diag.yml): however the runner's own resolver was set, and also when the public resolvers
# were asked directly, a runner got about 52 answers a second and the rest timed out — the limit is on NEW flows leaving the runner (every
# question was a new socket: a new source port, to a new server). The questions now go to the public resolvers over ONE socket per worker
# thread, kept for the thread's life: a few hundred flows for a whole run instead of a new one per question.
PUBLIC_SERVERS = (("1.1.1.1", 3), ("1.0.0.1", 3), ("8.8.8.8", 3), ("8.8.4.4", 3), ("9.9.9.9", 1), ("149.112.112.112", 1))  # (address, share of the questions)


class _Ans:
    """the part of dnspython's Answer the lookups use: .rrset (None when the name has no such record), iteration, [i]"""
    __slots__ = ("rrset",)

    def __init__(self, rrset):
        self.rrset = rrset

    def __iter__(self):
        return iter(self.rrset or ())

    def __getitem__(self, i):
        return self.rrset[i]


class SteadyResolver:
    """resolve(name, type) like dnspython's Resolver (raises NXDOMAIN, Timeout, NoNameservers), over one UDP socket per thread kept open.
    A question goes to one public resolver; no answer in `timeout` seconds or a SERVFAIL -> the next one, `tries` in all."""

    def __init__(self, servers=PUBLIC_SERVERS, timeout=2.0, tries=3):
        import dns.exception, dns.message, dns.query, dns.rcode, dns.resolver  # noqa: E401
        self.dns = dns
        self.pool = [ip for ip, w in servers for _ in range(max(1, int(w)))]
        self.timeout, self.tries = timeout, tries
        self.tl = threading.local()
        self.stats = collections.Counter()  # (server, "answer" | "timeout" | "servfail" | "error"): which resolver carries the load, which one lets go

    def resolve(self, name, typ, raise_on_no_answer=False):
        import socket
        dns = self.dns
        sock = getattr(self.tl, "s", None)
        if sock is None:
            sock = self.tl.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        q = dns.message.make_query(name, typ)
        order = []
        for ip in random.sample(self.pool, len(self.pool)):
            if ip not in order:
                order.append(ip)
        last = None
        for ip in order[:self.tries]:
            try:
                r = dns.query.udp(q, ip, timeout=self.timeout, sock=sock, ignore_unexpected=True, raise_on_truncation=True)
            except dns.message.Truncated:
                try:  # a record set too large for one datagram (a long TXT set): this one question over TCP
                    r = dns.query.tcp(q, ip, timeout=self.timeout + 2)
                except Exception as e:
                    last = e
                    continue
            except dns.exception.Timeout as e:
                last = e
                self.stats[(ip, "timeout")] += 1
                continue
            except (OSError, dns.exception.DNSException) as e:
                last = e
                self.stats[(ip, "error")] += 1
                try:
                    sock.close()
                except OSError:
                    pass
                sock = self.tl.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                continue
            rc = r.rcode()
            self.stats[(ip, "answer" if rc in (dns.rcode.NOERROR, dns.rcode.NXDOMAIN) else "servfail")] += 1
            if rc == dns.rcode.NXDOMAIN:
                raise dns.resolver.NXDOMAIN()
            if rc != dns.rcode.NOERROR:
                last = dns.resolver.NoNameservers()  # SERVFAIL / REFUSED from this resolver: another one may answer
                continue
            try:
                return _Ans(r.resolve_chaining().answer)
            except dns.message.AnswerForNXDOMAIN:
                raise dns.resolver.NXDOMAIN()
            except Exception as e:
                last = e
                continue
        if isinstance(last, dns.exception.DNSException):
            raise last
        raise dns.exception.Timeout()


def _public_asker(dns, tl):
    """ask(name, type) of the public resolvers, all threads together at most PUBLIC_QPS a second: the second chance of a name the runner's
    own resolver gave no answer for (raises what dnspython raises)"""
    gate, nxt = threading.Lock(), [0.0]

    def ask(name, typ):
        with gate:
            t = max(time.time(), nxt[0])
            nxt[0] = t + 1.0 / PUBLIC_QPS
        w = t - time.time()
        if w > 0:
            time.sleep(w)
        r = getattr(tl, "rp", None)
        if r is None:
            r = dns.resolver.Resolver(configure=False)
            r.nameservers, r.timeout, r.lifetime = random.sample(RESOLVERS, 3), 2.5, 5.0
            tl.rp = r
        return r.resolve(name, typ, raise_on_no_answer=False)
    return ask


def sweep_left(cur):
    """shards with work: the list not finished, or the name-server question still owed for the part of the list swept before it was asked"""
    if int(cur.get("rev") or 1) < SWEEP_REV:
        return list(range(SWEEP_SHARDS))  # the whole list is swept again (SWEEP_REV)
    pos, done = cur.get("pos") or {}, cur.get("complete") or {}
    ns_from, ns_done = cur.get("ns_from") or {}, cur.get("ns_complete") or {}
    return sorted((k for k in range(SWEEP_SHARDS) if not done.get(str(k)) or (int(ns_from.get(str(k), 0)) > 0 and not ns_done.get(str(k)))),
                  key=lambda k: (bool(done.get(str(k))), int(pos.get(str(k), 0)), k))


def stalled(d, pattern):
    """True when the run whose shard files are in `d` stopped because its questions got no answers and moved its list nowhere: the next run
    is then left to the daily schedule instead of being started at once (a broken transport would otherwise restart itself every minute)"""
    objs = []
    for cf in glob.glob(os.path.join(d, pattern)):
        try:
            objs.append(json.load(open(cf, encoding="utf-8")))
        except Exception:
            pass
    return bool(objs) and any(o.get("stopped_unanswered") for o in objs) and not any(int(o.get("asked") or 0) for o in objs)


def sweep_plan(a):
    """the sweep shards that still have work, least advanced first (for the workflow's matrix)"""
    left = [] if (a.after and stalled(a.after, "sweep_cursor_*.json")) else sweep_left(sweep_cursor())
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
    if int(cur.get("rev") or 1) < SWEEP_REV:  # places reached with the resolver that dropped half its questions: the list starts again
        cur = {x: cur[x] for x in ("release", "tlds") if x in cur}
    rel = cur.get("release") or (a.release if a.release and a.release != "auto" else CS.newest_graph())
    tlds = tuple(cur.get("tlds") or SWEEP_TLDS)
    start = int((cur.get("pos") or {}).get(str(k), 0))
    watch = ns_watch()
    # where the name-server question began for this shard: everything before that place was swept with the address question only and is
    # caught up once the list is done (ns_pos / ns_complete)
    ns_from = int((cur.get("ns_from") or {})[str(k)]) if str(k) in (cur.get("ns_from") or {}) else (start if watch else 0)
    ns_pos = int((cur.get("ns_pos") or {}).get(str(k), 0))
    state = {"release": rel, "tlds": list(tlds), "shard": k, "pos": start, "complete": bool((cur.get("complete") or {}).get(str(k))), "asked": 0, "stores": 0, "no_answer": 0,
             "ns_from": ns_from, "ns_pos": ns_pos, "ns_complete": bool((cur.get("ns_complete") or {}).get(str(k))) or ns_from == 0, "ns_asked": 0, "ns_hits": 0, "watch": len(watch),
             "rev": SWEEP_REV, "by_public": 0}

    def save():
        with open("out/sweep_cursor_%d.json" % k, "w", encoding="utf-8") as fo:
            json.dump(state, fo)
    save()
    catch_up = state["complete"] and not state["ns_complete"] and bool(watch)
    if k >= n or (state["complete"] and not catch_up):
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
    print("sweep shard %d/%d of graph %s, endings %s: the list is %.0f MiB (%.0f s); %s; name-server providers watched: %d" % (
        k, n, rel, ",".join(tlds), os.path.getsize(vfile) / 2 ** 20, time.time() - t0,
        ("catching up the name-server question from place %d to %d" % (ns_pos, ns_from)) if catch_up else ("starting after place %d" % start), len(watch)), flush=True)
    deadline = time.time() + a.minutes * 60
    local = None
    if a.resolver and a.resolver != "steady":
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
    steady = SteadyResolver() if a.resolver == "steady" else None  # the public resolvers over one socket per worker (see SteadyResolver)
    qps = a.qps if (local or steady) else min(a.qps, 60)  # domains per second
    per = 1 if (catch_up or not watch) else 2  # questions per domain: its address, and who serves its zone
    rate = qps * per
    print("resolver: %s, %d domains/s, %d questions/s" % ("public resolvers, one socket per worker" if steady else "%s:%d (local, recursive)" % local if local else "public resolvers", qps, rate), flush=True)
    tl = threading.local()
    gate, nxt = threading.Lock(), [0.0]

    def turn():
        with gate:
            t = max(time.time(), nxt[0])
            nxt[0] = t + 1.0 / rate
        w = t - time.time()
        if w > 0:
            time.sleep(w)
        if steady:
            return steady
        r = getattr(tl, "r", None)
        if r is None:
            r = dns.resolver.Resolver(configure=False)
            if local:
                r.nameservers, r.port, r.timeout, r.lifetime = [local[0]], local[1], 6.0, 6.0
            else:
                r.nameservers, r.timeout, r.lifetime = random.sample(RESOLVERS, 3), 2.5, 5.0
            tl.r = r
        return r

    ask_public = _public_asker(dns, tl) if local else None

    def ask_ns(d):
        """the name servers of the zone that belong to a watched provider (lower case, no final dot), or []"""
        try:
            ans = turn().resolve(d, "NS", raise_on_no_answer=False)
        except dns.resolver.NXDOMAIN:
            return []
        except dns.exception.DNSException:
            try:
                ans = ask_public(d, "NS") if ask_public else None
            except dns.exception.DNSException:
                ans = None
            if ans is None:
                return []
        hosts = [str(x.target).strip(".").lower() for x in (ans.rrset or [])][:8]
        return hosts if any(C.registrable(h) in watch for h in hosts) else []

    def ask(d):
        if catch_up:
            return d, "", "ns_only", ask_ns(d)
        how = "ok"
        try:
            ans = turn().resolve(d, "A", raise_on_no_answer=False)
        except dns.resolver.NXDOMAIN:
            return d, "", "nx", []
        except dns.exception.DNSException:
            if not ask_public:
                return d, "", "fail", []
            try:  # no answer from the runner's resolver: asked once of the public resolvers before it counts as no answer
                ans = ask_public(d, "A")
                how = "ok_public"
            except dns.resolver.NXDOMAIN:
                return d, "", "nx_public", []
            except dns.exception.DNSException:
                return d, "", "fail", []
        # the zone answers: who serves it (the delegation is already with the resolver; this question goes to the zone's own servers)
        ns = ask_ns(d) if watch else []
        if ans.rrset is None:
            return d, "", "none" if how == "ok" else "none_public", ns
        return d, ans[0].address, how, ns

    pref = tuple(t + "." for t in tlds)
    ok_name = re.compile(r"[a-z0-9-]+(?:\.[a-z0-9-]+)+")
    first, last = (ns_pos, ns_from) if catch_up else (start, 0)

    def batches():
        pos, batch = 0, []
        with gzip.open(vfile, "rt", encoding="utf-8", errors="replace") as fh:
            for l in fh:
                q = l.split("\t")
                if len(q) < 2 or not q[1].startswith(pref):
                    continue
                pos += 1
                if pos <= first:
                    continue
                if last and pos > last:
                    break
                d = ".".join(reversed(q[1].strip().split(".")))
                if zlib.crc32(d.encode()) % n != k or len(d) > 80 or not ok_name.fullmatch(d) or CS.PLATFORM.search(d):
                    continue
                batch.append(d)
                if len(batch) >= a.batch:
                    yield pos, batch
                    batch = []
        if batch:
            yield (last or pos), batch
        yield -1, []

    from concurrent.futures import ThreadPoolExecutor
    fo = open("out/dns_%d.jsonl" % k, "a", encoding="utf-8")
    with ThreadPoolExecutor(a.workers) as ex:
        for pos, batch in batches():
            if pos == -1:
                state["ns_complete" if catch_up else "complete"] = True
                break
            if deadline - time.time() < 1.3 * len(batch) / qps + 20:
                break  # not enough time left for this batch: the next run starts with it
            st, todo, hits = collections.Counter(), batch, {}
            for attempt in (1, 2):
                st["fail"] = 0
                again = []
                for d, ip, how, ns in ex.map(ask, todo):
                    st[how] += 1
                    if how == "fail":
                        again.append(d)
                    shop = bool(ip and SHOPIFY_A.match(ip))
                    if shop or ns:
                        o = {"d": d, "t": TODAY, "st": "ok", "l": 1, "sw": 1, "rv": SWEEP_REV}
                        if shop:
                            o.update(shop=1, a=ip)
                        if ns:
                            o["ns"] = ns
                        hits[d] = o
                if len(again) <= MAX_FAIL * len(batch) or attempt == 2:
                    break
                print("%s place %d: %d of %d names without an answer — asked once more in 30 s" % (time.strftime("%H:%M:%S"), pos, len(again), len(batch)), flush=True)
                time.sleep(30)
                todo = again
            if st["fail"] > 2 * MAX_FAIL * len(batch):
                # the questions are not getting through (2026-11-10: a run that went on like this left 60 % of its names unasked for good):
                # the list is not moved on, the next run starts at this place
                print("::warning::place %d: %d of %d names still without an answer — the run stops here and the list stays at this place" % (pos, st["fail"], len(batch)), flush=True)
                state["stopped_unanswered"] = True
                break
            for o in hits.values():
                state["stores"] += 1 if o.get("shop") else 0
                state["ns_hits"] += 1 if o.get("ns") else 0
                fo.write(json.dumps(o, ensure_ascii=False, separators=(",", ": ")) + "\n")
            fo.flush()
            if catch_up:
                state["ns_asked"] += len(batch); state["ns_pos"] = pos
            else:
                state["asked"] += len(batch); state["no_answer"] += st["fail"]; state["pos"] = pos
                state["by_public"] += st["ok_public"] + st["nx_public"] + st["none_public"]
                state["ns_asked"] += (st["ok"] + st["none"] + st["ok_public"] + st["none_public"]) if watch else 0
            save()
            if (state["ns_asked"] if catch_up else state["asked"]) % (10 * a.batch) == 0:
                print(time.strftime("%H:%M:%S"), "place %d: asked %d, stores %d, served by a watched provider %d, no answer %d (last batch: %s)" % (
                    pos, state["asked"] or state["ns_asked"], state["stores"], state["ns_hits"], state["no_answer"], dict(st)), flush=True)
    fo.close()
    if not catch_up and state["complete"] and state["ns_from"] == 0:
        state["ns_complete"] = True
    save()
    print("finished: place %d%s; asked %d domains, %d on Shopify's storefront addresses, %d served by a watched provider (%d name-server questions), %d without an answer "
          "(%d answered by the public resolvers after the runner's own gave none)" % (
              state["ns_pos"] if catch_up else state["pos"], " (end)" if state["ns_complete" if catch_up else "complete"] else "", state["asked"], state["stores"], state["ns_hits"], state["ns_asked"],
              state["no_answer"], state["by_public"]), flush=True)


# ------------------------------------------------------------------------------------------------------------------- stores on a subdomain
HOSTS_SHARDS = 8
HOST_TLDS = SWEEP_TLDS + ("ca",)
# first labels that are never a storefront of their own: the site itself, mail and technical hosts
HOST_SKIP = frozenset("www www1 www2 www3 ww ww1 ww2 wwww m mail webmail email smtp pop pop3 imap mx mx1 mx2 ftp sftp cpanel whm webdisk autodiscover autoconfig ns ns1 ns2 ns3 ns4 dns "
                      "vpn remote rdp ssh git svn cdn cdn1 cdn2 static assets img images media files api dev staging stage test beta demo sandbox preview old legacy "
                      "admin secure login sso auth status analytics stats tracking track click links link email-links blog blogs help support docs doc kb wiki forum forums "
                      "community news careers career jobs pagead2 app apps portal dashboard intranet".split())
HOST_DOMAIN_MAX = 30  # a domain with more host names than this in the graph is a platform or a large organisation: its hosts are not asked


def hosts_left(cur):
    h = cur.get("hosts") or {}
    if int(h.get("rev") or 1) < SWEEP_REV:
        return list(range(HOSTS_SHARDS))  # the whole list is swept again (SWEEP_REV)
    done, pos = h.get("complete") or {}, h.get("pos") or {}
    return sorted((k for k in range(HOSTS_SHARDS) if not done.get(str(k))), key=lambda k: (int(pos.get(str(k), 0)), k))


def host_groups(lines, tlds=HOST_TLDS):
    """the host names of the graph, in its own order (reversed names, sorted: the hosts of one domain follow each other) ->
    (domain, [three-label hosts worth asking]) for every domain with at most HOST_DOMAIN_MAX host names"""
    cur, buf, size = None, [], 0
    for line in lines:
        rev = line.rstrip("\n").partition("\t")[2]
        q = rev.split(".")
        if len(q) < 3 or q[0] not in tlds:
            continue
        d = q[1] + "." + q[0]
        if d != cur:
            if cur is not None and buf and size <= HOST_DOMAIN_MAX:
                yield cur, buf
            cur, buf, size = d, [], 0
        size += 1
        if len(q) == 3 and q[2] not in HOST_SKIP and len(q[2]) <= 40:
            buf.append(q[2] + "." + d)
    if cur is not None and buf and size <= HOST_DOMAIN_MAX:
        yield cur, buf


def hosts_sweep(a):
    """one question per host: is its address record on Shopify's storefront network? (see the module text, `hosts`)"""
    import shutil
    import subprocess
    import zlib
    import dns.exception
    import dns.resolver
    import credit_scan as CS
    import cc_clients as CCL
    k, n = int(a.shard.split("/")[0]), HOSTS_SHARDS
    os.makedirs("out", exist_ok=True)
    cur = sweep_cursor()
    hc = cur.get("hosts") or {}
    if int(hc.get("rev") or 1) < SWEEP_REV:  # places reached with the resolver that dropped half its questions: the list starts again
        hc = {x: hc[x] for x in ("release",) if x in hc}
    rel = hc.get("release") or cur.get("release") or (a.release if a.release and a.release != "auto" else CS.newest_graph())
    start = int((hc.get("pos") or {}).get(str(k), 0))
    state = {"release": rel, "shard": k, "pos": start, "complete": bool((hc.get("complete") or {}).get(str(k))), "asked": 0, "stores": 0, "no_answer": 0, "skipped_known_store": 0,
             "rev": SWEEP_REV, "by_public": 0}

    def save():
        with open("out/hosts_cursor_%d.json" % k, "w", encoding="utf-8") as fo:
            json.dump(state, fo)
    save()
    if k >= n or state["complete"]:
        print("host sweep shard %d/%d: nothing left" % (k, n), flush=True)
        return
    known = {o["d"] for o in records() if o.get("shop")}  # stores already found: their other host names are the same store
    print("host sweep shard %d/%d of graph %s: starting after place %d; stores already known: %d" % (k, n, rel, start, len(known)), flush=True)
    deadline = time.time() + a.minutes * 60
    local = None
    if a.resolver and a.resolver != "steady":
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
    steady = SteadyResolver() if a.resolver == "steady" else None  # the public resolvers over one socket per worker (see SteadyResolver)
    qps = a.qps if (local or steady) else min(a.qps, 60)
    print("resolver: %s, %d hosts/s" % ("public resolvers, one socket per worker" if steady else "%s:%d (local, recursive)" % local if local else "public resolvers", qps), flush=True)
    tl = threading.local()
    gate, nxt = threading.Lock(), [0.0]

    def turn():
        with gate:
            t = max(time.time(), nxt[0])
            nxt[0] = t + 1.0 / qps
        w = t - time.time()
        if w > 0:
            time.sleep(w)
        if steady:
            return steady
        r = getattr(tl, "r", None)
        if r is None:
            r = dns.resolver.Resolver(configure=False)
            if local:
                r.nameservers, r.port, r.timeout, r.lifetime = [local[0]], local[1], 6.0, 6.0
            else:
                r.nameservers, r.timeout, r.lifetime = random.sample(RESOLVERS, 3), 2.5, 5.0
            tl.r = r
        return r

    ask_public = _public_asker(dns, tl) if local else None

    def ask(h):
        how = "ok"
        try:
            ans = turn().resolve(h, "A", raise_on_no_answer=False)
        except dns.resolver.NXDOMAIN:
            return h, "", "nx"
        except dns.exception.DNSException:
            if not ask_public:
                return h, "", "fail"
            try:  # no answer from the runner's resolver: asked once of the public resolvers before it counts as no answer
                ans = ask_public(h, "A")
                how = "ok_public"
            except dns.resolver.NXDOMAIN:
                return h, "", "nx_public"
            except dns.exception.DNSException:
                return h, "", "fail"
        if ans.rrset is None:
            return h, "", "none" if how == "ok" else "none_public"
        return h, ans[0].address, how

    work = next((d for d in (os.environ.get("RUNNER_TEMP") or "", ".") if d and os.access(d, os.W_OK)), ".")
    unz = shutil.which("pigz") or "gzip"
    ok_name = re.compile(r"[a-z0-9-]+(?:\.[a-z0-9-]+)+")
    if a.base:  # tests: local files, one per line or a single file
        parts = [x for x in a.base.split(",") if x]
    else:
        raw = CCL.http_get("%sprojects/hyperlinkgraph/%s/host/%s-host-vertices.paths.gz" % (CCL.CC, rel, rel))
        parts = [CCL.CC + l.strip() for l in gzip.decompress(raw).decode().split("\n") if l.strip()]
    print("host-level graph: %d files" % len(parts), flush=True)

    def lines():
        for i, src in enumerate(parts):
            f = src
            if src.startswith("http"):
                f = os.path.join(work, "hv_%02d.gz" % i)
                subprocess.run(["curl", "-sS", "-L", "--fail", "--retry", "10", "--retry-delay", "10", "--retry-all-errors", "-A", CCL.UA, "-o", f, src], check=True)
            pr = subprocess.Popen([unz, "-dc", f], stdout=subprocess.PIPE, text=True, encoding="utf-8", errors="replace", bufsize=1 << 20)
            for l in pr.stdout:
                yield l
            pr.wait()
            if src.startswith("http"):
                os.remove(f)

    def batches():
        pos, batch = 0, []
        for dom, hosts in host_groups(lines()):
            if zlib.crc32(dom.encode()) % n != k or CS.PLATFORM.search(dom):
                continue
            if dom in known:
                state["skipped_known_store"] += len(hosts)
                continue
            for h in hosts:
                if not ok_name.fullmatch(h):
                    continue
                pos += 1
                if pos <= start:
                    continue
                batch.append(h)
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
            st, todo, hits = collections.Counter(), batch, {}
            for attempt in (1, 2):
                st["fail"] = 0
                again = []
                for h, ip, how in ex.map(ask, todo):
                    st[how] += 1
                    if how == "fail":
                        again.append(h)
                    if ip and SHOPIFY_A.match(ip):
                        hits[h] = ip
                if len(again) <= MAX_FAIL * len(batch) or attempt == 2:
                    break
                print("%s place %d: %d of %d hosts without an answer — asked once more in 30 s" % (time.strftime("%H:%M:%S"), pos, len(again), len(batch)), flush=True)
                time.sleep(30)
                todo = again
            if st["fail"] > 2 * MAX_FAIL * len(batch):  # the questions are not getting through: the list is not moved on (see sweep)
                print("::warning::place %d: %d of %d hosts still without an answer — the run stops here and the list stays at this place" % (pos, st["fail"], len(batch)), flush=True)
                state["stopped_unanswered"] = True
                break
            for h, ip in hits.items():
                fo.write(json.dumps({"d": h, "t": TODAY, "st": "ok", "l": 1, "sw": 2, "shop": 1, "a": ip, "rv": SWEEP_REV}, ensure_ascii=False, separators=(",", ": ")) + "\n")
                state["stores"] += 1
            fo.flush()
            state["asked"] += len(batch); state["no_answer"] += st["fail"]; state["pos"] = pos
            state["by_public"] += st["ok_public"] + st["nx_public"] + st["none_public"]
            save()
            print(time.strftime("%H:%M:%S"), "place %d: asked %d hosts, %d on Shopify's storefront addresses, no answer %d (last batch: %s)" % (
                pos, state["asked"], state["stores"], state["no_answer"], dict(st)), flush=True)
    fo.close()
    save()
    print("finished: place %d%s; asked %d hosts, %d on Shopify's storefront addresses, %d without an answer; hosts of known stores not asked: %d" % (
        state["pos"], " (end)" if state["complete"] else "", state["asked"], state["stores"], state["no_answer"], state["skipped_known_store"]), flush=True)


def merge(a):
    os.makedirs(DIR, exist_ok=True)
    stamp = a.stamp or time.strftime("%Y%m%dT%H%M%S", time.gmtime())
    # domains with a cloud record (the MX / SPF checks made from the Mac are older and poorer: a cloud record replaces them). A lookup made
    # through the repaired resolver ("rv") replaces a record of before; a sweep hit never replaces a record (it holds one fact only).
    done, again = record_states()
    have = set(done) | set(again)
    n = n_again = 0
    for f in sorted(glob.glob(os.path.join(a.dir, "dns_*.jsonl"))):
        lines = []
        for l in open(f, encoding="utf-8"):
            i = l.find('"d": "')
            d = l[i + 6:l.find('"', i + 6)] if i >= 0 else ""
            if not d or not l.strip():
                continue
            if d not in have:
                lines.append(l.rstrip("\n"))
                have.add(d); done.add(d)
            elif d in again and '"rv": ' in l and '"sw": ' not in l:
                lines.append(l.rstrip("\n"))
                again.pop(d, None); done.add(d)
                n_again += 1
        if lines:
            k = re.search(r"dns_(\d+)\.jsonl$", f).group(1)
            with gzip.open(os.path.join(DIR, "dns_%s_%s.gz" % (stamp, k)), "wt", encoding="utf-8") as g:
                g.write("\n".join(lines) + "\n")
            n += len(lines)
    if n_again:
        print("domains asked again through the repaired resolver: %d records replace the ones of before; still to ask again: %d" % (n_again, len(again)))
    n -= n_again
    cfiles = sorted(glob.glob(os.path.join(a.dir, "sweep_cursor_*.json")))
    if cfiles:  # the sweep: where each shard stopped (single writer: this merge)
        cur = sweep_cursor()
        objs = []
        for cf in cfiles:
            try:
                objs.append(json.load(open(cf, encoding="utf-8")))
            except Exception:
                continue
        old_rev = [o for o in objs if int(o.get("rev") or 1) < SWEEP_REV]
        objs = [o for o in objs if int(o.get("rev") or 1) >= SWEEP_REV]
        if old_rev:  # shards of a run started before SWEEP_REV: their hits are kept (above), their places are not
            print("sweep shards of a run started before the list was begun again: %d (hits kept, places not)" % len(old_rev))
        if objs and int(cur.get("rev") or 1) < SWEEP_REV:  # the first shards of the list begun again: the old places and counts are set aside
            cur = {"release": cur.get("release"), "tlds": cur.get("tlds"), "rev": SWEEP_REV, **({"hosts": cur["hosts"]} if cur.get("hosts") else {}),
                   "before_rev_%d" % SWEEP_REV: {x: cur.get(x) for x in ("asked", "stores_found", "ns_hits", "pos", "updated") if cur.get(x) is not None}}
            cur = {x: v for x, v in cur.items() if v is not None}
        cur.setdefault("pos", {}); cur.setdefault("complete", {})
        asked = stores = by_public = no_answer = 0
        for o in objs:
            if cur.get("release") and cur["release"] != o.get("release"):
                continue  # a shard that read another release of the list: its place means nothing here
            by_public += int(o.get("by_public") or 0); no_answer += int(o.get("no_answer") or 0)
            cur["release"], cur["tlds"], cur["shards"] = o["release"], o["tlds"], SWEEP_SHARDS
            ks = str(o["shard"])
            cur["pos"][ks] = max(int(cur["pos"].get(ks, 0)), int(o.get("pos") or 0))
            if o.get("complete"):
                cur["complete"][ks] = True
            if o.get("watch"):  # the shard asked the name-server question: from which place on, how far the catch-up of the earlier part got
                cur.setdefault("ns_from", {}).setdefault(ks, int(o.get("ns_from") or 0))
                cur.setdefault("ns_pos", {})[ks] = max(int((cur.get("ns_pos") or {}).get(ks, 0)), int(o.get("ns_pos") or 0))
                if o.get("ns_complete"):
                    cur.setdefault("ns_complete", {})[ks] = True
                cur["ns_hits"] = int(cur.get("ns_hits") or 0) + int(o.get("ns_hits") or 0)
            asked += int(o.get("asked") or 0); stores += int(o.get("stores") or 0)
        if objs:
            cur["asked"] = int(cur.get("asked") or 0) + asked
            cur["stores_found"] = int(cur.get("stores_found") or 0) + stores
            cur["no_answer"] = int(cur.get("no_answer") or 0) + no_answer
            cur["updated"] = time.strftime("%Y-%m-%dT%H:%MZ", time.gmtime())
            with open(CURSOR, "w", encoding="utf-8") as f:
                json.dump(cur, f, indent=1, sort_keys=True)
            print("sweep of graph %s (%s): +%d domains asked, +%d stores this run (%d without an answer, %d answered by the public resolvers); %d asked, %d stores and %d domains served by a "
                  "watched provider so far; shards finished: %d of %d" % (cur.get("release"), ",".join(cur.get("tlds") or []), asked, stores, no_answer, by_public, cur["asked"], cur["stores_found"],
                                                                         int(cur.get("ns_hits") or 0), len(cur["complete"]), SWEEP_SHARDS))
    hfiles = sorted(glob.glob(os.path.join(a.dir, "hosts_cursor_*.json")))
    if hfiles:  # the host sweep: where each shard stopped (single writer: this merge; its own key of the cursor file)
        cur = sweep_cursor()
        objs = []
        for cf in hfiles:
            try:
                objs.append(json.load(open(cf, encoding="utf-8")))
            except Exception:
                continue
        old_rev = [o for o in objs if int(o.get("rev") or 1) < SWEEP_REV]
        objs = [o for o in objs if int(o.get("rev") or 1) >= SWEEP_REV]
        if old_rev:
            print("host sweep shards of a run started before the list was begun again: %d (hits kept, places not)" % len(old_rev))
        hc = cur.get("hosts") or {}
        if objs and int(hc.get("rev") or 1) < SWEEP_REV:  # the first shards of the list begun again: the old places and counts are set aside
            hc = {"release": hc.get("release"), "rev": SWEEP_REV, "before_rev_%d" % SWEEP_REV: {x: hc.get(x) for x in ("asked", "stores_found", "pos", "updated") if hc.get(x) is not None}}
            hc = {x: v for x, v in hc.items() if v is not None}
        cur["hosts"] = hc
        hc.setdefault("pos", {}); hc.setdefault("complete", {})
        asked = stores = 0
        for o in objs:
            if hc.get("release") and hc["release"] != o.get("release"):
                continue
            hc["release"], hc["shards"] = o["release"], HOSTS_SHARDS
            ks = str(o["shard"])
            hc["pos"][ks] = max(int(hc["pos"].get(ks, 0)), int(o.get("pos") or 0))
            if o.get("complete"):
                hc["complete"][ks] = True
            asked += int(o.get("asked") or 0); stores += int(o.get("stores") or 0)
        if objs:
            hc["asked"] = int(hc.get("asked") or 0) + asked
            hc["stores_found"] = int(hc.get("stores_found") or 0) + stores
            hc["updated"] = time.strftime("%Y-%m-%dT%H:%MZ", time.gmtime())
            with open(CURSOR, "w", encoding="utf-8") as f:
                json.dump(cur, f, indent=1, sort_keys=True)
            print("host sweep of graph %s: +%d hosts asked, +%d stores on a subdomain this run; %d asked and %d stores so far; shards finished: %d of %d" % (
                hc.get("release"), asked, stores, hc["asked"], hc["stores_found"], len(hc["complete"]), HOSTS_SHARDS))
    try:
        print("name-server providers watched by the sweep: %d" % write_ns_watch())
    except Exception as e:
        print("watch list not rewritten (%s): the one on file stays" % str(e)[:100])
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
          "most frequent TXT keys: %s" % (len(have), n, shops, MIN_CLIENTS, len(candidates(100000)), ", ".join("%s %d" % kv for kv in keys.most_common(25))))


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
    ap.add_argument("cmd", choices=["lookup", "merge", "table", "sweep", "sweep-plan", "hosts", "hosts-plan"])
    ap.add_argument("dir", nargs="?", default="shards")
    ap.add_argument("--shard", default="0/1")
    ap.add_argument("--minutes", type=float, default=100)
    ap.add_argument("--workers", type=int, default=120)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--stamp", default="")
    ap.add_argument("--resolver", default="", help="'steady' = the public resolvers over one socket per worker (the workflow's choice); host:port = a recursive resolver on this machine; empty = public resolvers with a new socket per question, slowly")
    ap.add_argument("--qps", type=int, default=480, help="lookup: queries per second of this runner")
    ap.add_argument("--batch", type=int, default=20000, help="sweep: domains asked between two saves of the shard's place")
    ap.add_argument("--release", default="auto", help="sweep: the web graph release (default: the one the sweep started with, else the newest)")
    ap.add_argument("--base", default="", help="sweep: URL or local path of the vertices file (tests)")
    ap.add_argument("--after", default="", help="sweep-plan / hosts-plan: the directory of the run that just ended — no shard is planned when that run got no answers at all")
    a = ap.parse_args()
    if a.cmd == "hosts":
        return hosts_sweep(a)
    if a.cmd == "hosts-plan":
        print(json.dumps(([] if (a.after and stalled(a.after, "hosts_cursor_*.json")) else hosts_left(sweep_cursor()))[:max(1, a.limit or HOSTS_SHARDS)]))
        return
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
