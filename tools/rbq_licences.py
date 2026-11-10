#!/usr/bin/env python3
"""Québec construction licence holders -> relationship leads (cloud; one bulk download + one polite home-page read per holder's own site).

In Québec "quiconque exécute ou fait exécuter des travaux de construction doit détenir une licence de la Régie du bâtiment du Québec (RBQ)"
and the Régie publishes, every day, "l'ensemble des détenteurs de licences actives" (Données Québec, CC-BY 4.0): licence number, holder's
legal name and other names, legal status, NEQ, address, telephone, e-mail, the date the licence was first issued, the date of the next annual
payment of the licence fees and the body that issued the licence (the Régie, or the corporation of master electricians / master pipe-mechanics).
The Régie's own page: "Chaque année, vous devez payer votre licence pour la maintenir." A licence on the active list is therefore a current,
dated, paid relationship between a named holder and a Québec body — published by the body that is paid.

What the list does not give is the holder's website. Its e-mail does when it is on a domain of the holder's own (not a webmail / internet
provider domain, not a domain shared by several unrelated holders). That site is read once (home page, then one or two contact pages) and
kept ONLY when it shows the holder's licence number, telephone number or postal code as the register has them, or its name. The mailbox is
then found on the holder's own site by the ordinary mailbox crawl (tools/lead_crawl.py reads lead_shards/); the register's e-mail is never
delivered as such. Natural persons ("Personne physique") are left out entirely: organisations only.

  pull                 the daily list -> out/rbq_holders.csv.gz (one line per licence of a legal person) + counts
  sites --minutes M    holders' own domains not checked yet -> out/rbq_sites.jsonl (one record per domain)
  merge DIR --stamp S  -> data/incoming/claude/rbq/ (holders, site checks) and lead_shards/leads_rbq_<S>.gz + details_rbq_<S>.gz
"""
import argparse, collections, csv, glob, gzip, hashlib, io, json, os, re, sys, threading, time, unicodedata, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
INC = os.path.join(ROOT, "data/incoming/claude")
DIR = os.path.join(INC, "rbq")
SHARDS = os.path.join(INC, "lead_shards")
HOLDERS = os.path.join(DIR, "holders.csv.gz")
UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
TODAY = time.strftime("%Y-%m-%d")
DATASET = "https://www.donneesquebec.ca/recherche/dataset/licencesactives"
API = "https://www.donneesquebec.ca/recherche/api/3/action/package_show?id=licencesactives"
DATASET_QUOTE = "Le jeu de donnée présente l'ensemble des détenteurs de licences actives de la RBQ."
FIELD_DOC = "https://www.donneesquebec.ca/recherche/dataset/755b45d6-7aee-46df-a216-748a0191c79f/resource/6fe2352f-cdec-4672-b80c-3cb9e123e933/download/fiche-descriptive-liste-des-licences-actives.pdf"
# the bodies that issue the licence and are paid for it — each one's address and fee statement as its own page prints them (pages opened 2026-11-10)
BODIES = {
    "rbq": dict(name="Régie du bâtiment du Québec", short="RBQ", site="https://www.rbq.gouv.qc.ca/",
                address="Rez-de-chaussée, local 040, 255, boulevard Crémazie Est, Montréal (Québec) H2M 1L5", address_url="https://www.rbq.gouv.qc.ca/nous-joindre/",
                fee_quote="Chaque année, vous devez payer votre licence pour la maintenir.", fee_url="https://www.rbq.gouv.qc.ca/licence/repondre-a-ses-obligations/payer-le-maintien-de-sa-licence", read="2026-11-10"),
    "cmeq": dict(name="Corporation des maîtres électriciens du Québec (CMEQ)", short="CMEQ", site="https://www.cmeq.org/",
                 address="5925, boul. Décarie, Montréal (Québec) H3W 3C9", address_url="https://www.cmeq.org/fileadmin/user_upload/documents/Images_Nouvelles/Maintien_Licence.pdf",
                 fee_quote="Droits et frais de maintien de votre licence; Cotisation annuelle CMEQ;", fee_url="https://www.cmeq.org/fileadmin/user_upload/documents/Images_Nouvelles/Maintien_Licence.pdf", read="2026-11-10"),
    "cmmtq": dict(name="Corporation des maîtres mécaniciens en tuyauterie du Québec (CMMTQ)", short="CMMTQ", site="https://www.cmmtq.org/",
                  address="8175, boul. St-Laurent, Montréal (Québec) H2P 2M1", address_url="https://www.cmmtq.org/client_file/upload/Devenir%20entrepreneur/Formulaires/Admission_personne_morale.pdf",
                  fee_quote="Les frais d'admission et la cotisation annuelle à la CMMTQ doivent faire l'objet d'un paiement distinct",
                  fee_url="https://www.cmmtq.org/client_file/upload/Devenir%20entrepreneur/Formulaires/Admission_personne_morale.pdf", read="2026-11-10"),
}
HCOLS = ["licence", "status", "type", "issued", "next_payment", "body", "legal_status", "name", "other_names", "neq", "address", "city", "postal", "phone", "email", "domain",
         "categories", "restriction"]
# webmail and internet-provider domains (the holder's own site cannot be read off such an address)
WEBMAIL = re.compile(r"(^|\.)(gmail|googlemail|hotmail|outlook|live|msn|yahoo|ymail|rocketmail|icloud|aol|gmx|protonmail|proton|zoho|yandex|fastmail|"
                     r"videotron|sympatico|bellnet|bellaliant|aliant|telus|shaw|rogers|cogeco|cgocable|eastlink|xplornet|xplore|teksavvy|distributel|oricom|"
                     r"globetrotter|sogetel|maskatel|cooptel|derytele|b2b2c|xittel|ccapcable|telupton|telwarwick|tellabaie|satelcom|navigue|"
                     r"uniserve|sasktel|accesscomm|tbaytel|execulink|wightman|netrevolution|wanadoo|laposte|comcast|verizon|sbcglobal)\.[a-z.]{2,8}$", re.I)
WEBMAIL_EXACT = set("""me.com mac.com pm.me mail.com hey.com free.fr orange.fr sfr.fr att.net bell.net bell.ca ebox.ca tlb.sympatico.ca axion.ca cablevision.qc.ca lino.com ivic.qc.ca colba.net
vif.com primus.ca total.net ncf.ca mts.net mymts.net persona.ca netcom.ca nt.net qc.aira.com aira.com aei.ca dery.ca transcontinental.ca hotmail.fr live.fr outlook.fr live.ca hotmail.ca
outlook.ca yahoo.ca yahoo.fr videotron.qc.ca vl.videotron.ca globetrotter.qc.ca sympatico.ca""".split())
# a holder's domain that sends the reader to an unrelated host (a social profile, a directory, a parked page) is not the holder's site
def related(d1, d2):
    x, y = re.sub(r"[^a-z0-9]", "", d1.split(".")[0]), re.sub(r"[^a-z0-9]", "", d2.split(".")[0])
    return x == y or (len(x) >= 5 and x in y) or (len(y) >= 5 and y in x)


LEGAL_OK = re.compile(r"morale|societe|compagnie|coop|corporation|association|syndicat|organisme|fiducie|municipal")


def keyname(s):
    return re.sub(r"[^a-z0-9]+", " ", unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()).strip()


def body_of(mandataire):
    k = keyname(mandataire)
    return "cmeq" if ("electric" in k or "cmeq" in k) else "cmmtq" if ("tuyauterie" in k or "cmmtq" in k) else "rbq"


def http(url, timeout=120):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    return urllib.request.urlopen(req, timeout=timeout)


def pull(a):
    os.makedirs("out", exist_ok=True)
    src = a.csv
    if not src:
        meta = json.loads(http(API).read().decode("utf-8", "replace"))["result"]
        res = [r for r in meta.get("resources") or [] if (r.get("format") or "").upper() == "CSV"]
        print("dataset: %s | modified %s | licence %s | resources: %s" % (meta.get("title"), meta.get("metadata_modified"), meta.get("license_title"),
                                                                          "; ".join("%s %s %s" % (r.get("format"), r.get("size"), r.get("url")) for r in meta.get("resources") or [])), flush=True)
        if not res:
            raise SystemExit("no CSV resource in the dataset")
        src = "out/rbq_raw.csv"
        t0 = time.time()
        with http(res[0]["url"], timeout=600) as r, open(src, "wb") as f:
            while True:
                b = r.read(1 << 20)
                if not b:
                    break
                f.write(b)
        print("downloaded %.0f MB in %.0f s" % (os.path.getsize(src) / 1e6, time.time() - t0), flush=True)
    lic, n = {}, 0
    with open(src, encoding="utf-8-sig", newline="") as f:
        rd = csv.DictReader(f)
        names = {keyname(c): c for c in rd.fieldnames or []}
        print("columns: %s" % rd.fieldnames, flush=True)

        def col(*cands):
            for c in cands:
                if c in names:
                    return names[c]
            return None
        C_ = dict(licence=col("numero de licence"), status=col("statut de la licence"), type=col("type de licence"), issued=col("date de delivrance"),
                  next_payment=col("date du paiement annuel"), body=col("mandataire"), legal_status=col("statut juridique"), name=col("nom de l intervenant"),
                  other=col("autre nom"), neq=col("neq"), address=col("adresse"), city=col("municipalite"), phone=col("numero de telephone"), email=col("courriel"),
                  cat=col("categorie", "categories et sous categories", "categories"), sub=col("sous categories", "sous categorie"), restriction=col("restriction"))
        missing = [k for k, v in C_.items() if v is None and k not in ("sub", "cat")]
        if missing:
            print("columns not found: %s" % missing, flush=True)
        g = lambda row, k: (row.get(C_[k]) or "").strip() if C_.get(k) else ""
        for row in rd:
            n += 1
            num = g(row, "licence")
            if not num:
                continue
            L = lic.get(num)
            if L is None:
                L = lic[num] = {k: g(row, k) for k in ("licence", "status", "type", "issued", "next_payment", "body", "legal_status", "name", "other", "neq", "address", "city", "phone", "email", "restriction")}
                L["cats"] = []
                if n <= 2:
                    print("sample row: %s" % json.dumps({k: (v if k not in (C_.get("email"), C_.get("phone")) else "…") for k, v in row.items()}, ensure_ascii=False)[:900], flush=True)
            for k in ("cat", "sub"):
                v = g(row, k)
                if v and v not in L["cats"] and len(L["cats"]) < 12:
                    L["cats"].append(v)
    st = collections.Counter(keyname(L["legal_status"]) or "(none)" for L in lic.values())
    print("rows %d; licences %d; legal status: %s; issuing body: %s; licence status: %s" % (
        n, len(lic), dict(st.most_common(8)), dict(collections.Counter(body_of(L["body"]) for L in lic.values())), dict(collections.Counter(L["status"] for L in lic.values()).most_common(5))), flush=True)
    out, stats = [], collections.Counter()
    PCQ = re.compile(r"\b([GHJ]\d[A-Z])\s?(\d[A-Z]\d)\b")
    for num, L in lic.items():
        ls = keyname(L["legal_status"])
        if "physique" in ls or not LEGAL_OK.search(ls):
            stats["natural persons / legal status not recognised as an organisation (left out)"] += 1
            continue
        em = L["email"].lower().strip()
        dom = ""
        if re.fullmatch(r"[a-z0-9._%+-]+@[a-z0-9-]+(\.[a-z0-9-]+)+", em):
            d = em.split("@")[1]
            if WEBMAIL.search(d) or d in WEBMAIL_EXACT:
                stats["e-mail on a webmail / provider domain"] += 1
            else:
                dom = d
                stats["e-mail on another domain"] += 1
        else:
            stats["no e-mail"] += 1
        m = PCQ.search(L["address"].upper())
        out.append(dict(licence=num, status=L["status"], type=L["type"], issued=L["issued"][:10], next_payment=L["next_payment"][:10], body=body_of(L["body"]), legal_status=L["legal_status"],
                        name=L["name"], other_names=L["other"], neq=re.sub(r"\D", "", L["neq"]), address=L["address"], city=L["city"], postal=(m.group(1) + " " + m.group(2)) if m else "",
                        phone=re.sub(r"\D", "", L["phone"])[-10:], email=em, domain=dom, categories=" | ".join(L["cats"])[:400], restriction=L["restriction"]))
    # a domain used by several unrelated holders is a provider's or an accountant's, not the holder's own
    per = collections.defaultdict(set)
    for o in out:
        if o["domain"]:
            per[reg_dom(o["domain"])].add(o["neq"] or o["licence"])
    shared = {d for d, s in per.items() if len(s) > 3}
    for o in out:
        if o["domain"] and reg_dom(o["domain"]) in shared:
            o["domain"] = ""
            stats["e-mail on a domain shared by more than 3 holders (left out)"] += 1
    # two copies: the full one stays on the runner (the register's e-mail is only used to see whether the holder's own site prints it); the
    # one that is committed carries the e-mail's DOMAIN only — an address of the register is never stored or delivered as a contact
    for path, cols in (("out/rbq_holders_full.csv.gz", HCOLS), ("out/rbq_holders.csv.gz", [c for c in HCOLS if c != "email"])):
        with gzip.open(path, "wt", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
            w.writeheader()
            w.writerows(sorted(out, key=lambda o: o["licence"]))
    own = [o for o in out if o["domain"]]
    print("licence holders kept (legal persons): %d; %s; holders with a domain of their own: %d (%d distinct domains); shared domains left out: %s" % (
        len(out), dict(stats), len(own), len({reg_dom(o["domain"]) for o in own}), ", ".join(sorted(shared, key=lambda d: -len(per[d]))[:25])), flush=True)
    print("next annual payment by year: %s" % dict(sorted(collections.Counter(o["next_payment"][:4] for o in out).items())), flush=True)


def reg_dom(d):
    import ap_crawler as C
    return C.registrable(d.lower())


def holders(path=None):
    p = path or next((x for x in ("out/rbq_holders_full.csv.gz", "out/rbq_holders.csv.gz") if os.path.exists(x)), HOLDERS)
    if not os.path.exists(p):
        return []
    with gzip.open(p, "rt", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def checked():
    done = {}
    for p in sorted(glob.glob(os.path.join(DIR, "sites_*.gz"))):
        with gzip.open(p, "rt", encoding="utf-8") as f:
            for l in f:
                try:
                    o = json.loads(l)
                    done[o["dom"]] = o
                except (ValueError, KeyError):
                    pass
    return done


CONTACT = re.compile(r"contact|joindre|coordonn|about|propos|nous-trouver", re.I)
SEP = r"[\s\-. ‐‑‒–—]{0,3}"


def proofs(h):
    """the patterns that tie a page to this holder: licence number, telephone, postal code (as the register has them)"""
    out = []
    lic = re.sub(r"\D", "", h["licence"])
    if len(lic) == 10:
        out.append(("licence number", re.compile(r"(?<!\d)%s%s%s%s%s(?!\d)" % (lic[:4], SEP, lic[4:8], SEP, lic[8:]))))
    ph = h.get("phone") or ""
    if len(ph) == 10:
        out.append(("telephone", re.compile(r"(?<!\d)\(?%s\)?%s%s%s%s(?!\d)" % (ph[:3], SEP, ph[3:6], SEP, ph[6:]))))
    pc = (h.get("postal") or "").replace(" ", "")
    if len(pc) == 6:
        out.append(("postal code", re.compile(r"(?<![A-Za-z0-9])%s\s?%s(?![A-Za-z0-9])" % (pc[:3], pc[3:]), re.I)))
    return out


def sites(a):
    import ap_crawler as C
    import biz_licences as BL
    import lead_crawl as LC
    import tech_relationships as T
    os.makedirs("out", exist_ok=True)
    os.makedirs(C.STATE, exist_ok=True)
    C.HOST_INTERVAL = 0.6
    by_dom = collections.defaultdict(list)
    for h in holders():
        if h.get("domain"):
            by_dom[h["domain"].lower()].append(h)
    done = checked()
    todo = [d for d in sorted(by_dom) if d not in done]
    if a.limit:
        todo = todo[:a.limit]
    print("holders' own domains: %d; checked before: %d; to read now: %d" % (len(by_dom), len(done), len(todo)), flush=True)
    deadline = time.time() + a.minutes * 60
    lock, stats = threading.Lock(), collections.Counter()
    fo = open("out/rbq_sites.jsonl", "a", encoding="utf-8")

    def page(url):
        if not C.allowed(url):
            return "robots", "", url
        st, ct, data, final = C.fetch(url, 1_500_000)
        if st == 0:
            return "unreachable", "", final
        head = data[:20000].decode("utf-8", "replace") if data else ""
        if st in (401, 403, 429) or (C.BLOCK_RX.search(head) and len(data) < 30000):
            return "blocked", "", final
        if st != 200 or not data:
            return "http_%s" % st, "", final
        return "ok", data.decode("utf-8", "replace"), final

    def one(dom):
        if time.time() > deadline:
            return
        rec = {"dom": dom, "date": TODAY, "st": "", "hits": []}
        try:
            res, raw, final = page("https://%s/" % dom)
            if res != "ok" and not dom.startswith("www.") and res in ("unreachable", "http_404"):
                res, raw, final = page("https://www.%s/" % dom)
            rec["st"], rec["final"] = res, final
            fhost = (urllib.parse.urlparse(final).hostname or dom).lower()
            if res == "ok" and C.registrable(fhost) != C.registrable(dom) and not related(C.registrable(dom), C.registrable(fhost)):
                rec["st"] = res = "redirected_elsewhere"
            if res == "ok":
                title, meta = T.page_meta(raw)
                name = LC.site_name_for(fhost, meta.get("og:site_name"), title, T)
                rec["name"] = name or ""
                pages = [(final, raw)]
                links, seen = [], set()
                for link, label in C.links(raw, final):
                    p = urllib.parse.urlparse(link)
                    if p.scheme in ("http", "https") and C.registrable((p.hostname or "").lower()) == C.registrable(fhost) and not C.SKIP_EXT.search(p.path) and CONTACT.search(p.path + " " + label):
                        u = link.split("#")[0]
                        if u not in seen and u.rstrip("/") != final.rstrip("/"):
                            seen.add(u)
                            links.append((0 if re.search(r"contact|joindre|coordonn", p.path + " " + label, re.I) else 1, len(p.path), u))
                more = [u for _, _, u in sorted(links)[:2]]
                for h in by_dom[dom]:
                    hit = None
                    pr = proofs(h)
                    for i in range(1 + len(more)):
                        if i >= len(pages):
                            r2, raw2, f2 = page(more[i - 1])
                            pages.append((f2, raw2 if r2 == "ok" else ""))
                        url, rw = pages[i]
                        if not rw:
                            continue
                        text = C.visible(rw)
                        for what, rx in pr:
                            m = rx.search(text)
                            if m:
                                hit = dict(licence=h["licence"], by=what, url=url, quote=re.sub(r"\s+", " ", text[max(0, m.start() - 110):m.end() + 110]).strip()[:300])
                                break
                        if hit:
                            break
                    if not hit and name and (BL.names_agree(name, h["name"]) or any(BL.names_agree(name, o) for o in re.split(r"\s*[;|]\s*", h.get("other_names") or "") if o.strip())):
                        hit = dict(licence=h["licence"], by="name", url=final, quote="site name “%s” — holder “%s”%s" % (name[:90], h["name"][:90], (" / “%s”" % h["other_names"][:80]) if h.get("other_names") else ""))
                    if hit:
                        hit["register_email_on_page"] = any(h.get("email") and h["email"] in rw.lower() for _, rw in pages if rw)
                        rec["hits"].append(hit)
                rec["st"] = "confirmed" if rec["hits"] else "not_confirmed"
        except Exception as e:
            rec["st"] = "error:" + type(e).__name__
        with lock:
            stats[rec["st"].split(":")[0]] += 1
            for h in rec["hits"]:
                stats["by " + h["by"]] += 1
                stats["register e-mail printed on the site"] += bool(h.get("register_email_on_page"))
            fo.write(json.dumps(rec, ensure_ascii=False) + "\n")
            if sum(v for k, v in stats.items() if not k.startswith(("by ", "register"))) % 500 == 0:
                fo.flush()
                print(time.strftime("%H:%M:%S"), dict(stats), flush=True)
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(one, todo))
    fo.close()
    print("finished", dict(stats), flush=True)
    sys.stdout.flush()
    os._exit(0)


LEAD_COLS = ["buyer_key", "buyer_name", "website", "canadian_vendor_rows", "example_vendor", "canada_field_value", "evidence_dataset", "latest_record_date"]


def lead_of(h, hit, site):
    B = BODIES[h["body"]]
    key = "lead:" + hashlib.sha1(("rbq|%s" % re.sub(r"\D", "", h["licence"])).encode()).hexdigest()[:16]
    other = [o.strip() for o in re.split(r"\s*[;|]\s*", h.get("other_names") or "") if o.strip()]
    numbered = re.fullmatch(r"\d{4}\s?-\s?\d{4}\s+qu[eé]bec\s+inc\.?", h["name"].strip(), re.I)  # a numbered company is known by its other name; the legal name stays in the register facts
    row = {"buyer_key": key, "buyer_name": other[0] if numbered and other else h["name"], "website": site, "canadian_vendor_rows": 1, "example_vendor": B["name"],
           "canada_field_value": "membership / statutory fee relationship: licence holder of the Canadian body (%s)=%s (as printed on %s, read %s); %s: “%s” (%s)"
                                 % (B["name"], B["address"], B["address_url"], B["read"], B["short"], B["fee_quote"], B["fee_url"]),
           "evidence_dataset": DATASET, "latest_record_date": TODAY}
    det = {"key": key, "platform": "rbq_licence", "record_url": DATASET, "vendor": B["name"], "record_date": TODAY, "start": h["issued"], "end": h["next_payment"],
           "reference": h["licence"], "title": "Licence %s no %s (%s)%s" % ("d'entrepreneur en construction" if "entrepreneur" in keyname(h["type"]) else "de constructeur-propriétaire" if "proprietaire" in keyname(h["type"]) else "RBQ",
                                                                           h["licence"], h["status"] or "active", (" — " + h["categories"][:200]) if h.get("categories") else ""),
           "vendor_address": "%s (as printed on %s)" % (B["address"], B["address_url"]), "vendor_site": B["site"],
           "member_address_quote": h["address"], "register_label": "the public register of active licences published by", "buyer_phone_as_printed": h["phone"],
           "buyer_register": {"legal_name": h["name"], "trade_names": other[:4], "registry_id": ("NEQ %s" % h["neq"]) if len(h["neq"]) == 10 else "", "legal_form": h["legal_status"],
                              "phone": ("%s-%s-%s" % (h["phone"][:3], h["phone"][3:6], h["phone"][6:])) if len(h["phone"]) == 10 else "",
                              "label": "the Régie du bâtiment du Québec's list of active licences, %s, read %s" % (DATASET, TODAY)},
           "licence_first_issued": h["issued"], "licence_fees_paid_until": h["next_payment"], "licence_issued_by": B["name"], "licence_type": h["type"], "licence_restriction": h["restriction"],
           "fee_basis": "%s (%s)" % (B["fee_quote"], B["fee_url"]), "dataset_basis": "%s (%s); field “Date du paiement annuel”: “date du prochain paiement des droits d'exercice” (%s)" % (DATASET_QUOTE, DATASET, FIELD_DOC),
           "site_tied_to_holder_by": hit["by"], "site_page": hit["url"], "site_quote": hit["quote"]}
    return row, det


def merge(a):
    os.makedirs(DIR, exist_ok=True)
    os.makedirs(SHARDS, exist_ok=True)
    stamp = a.stamp or time.strftime("%Y%m%dT%H%M%S", time.gmtime())
    msg = []
    src = os.path.join(a.dir, "rbq_holders.csv.gz")
    if os.path.exists(src) and os.path.getsize(src) > 200:
        with open(src, "rb") as fi, open(HOLDERS, "wb") as fo:
            fo.write(fi.read())
    H = {h["licence"]: h for h in holders(HOLDERS)}
    msg.append("licence holders on the active list (legal persons): %d" % len(H))
    recs = []
    for f in sorted(glob.glob(os.path.join(a.dir, "rbq_sites*.jsonl"))):
        for l in open(f, encoding="utf-8"):
            try:
                recs.append(json.loads(l))
            except ValueError:
                pass
    if recs:
        with gzip.open(os.path.join(DIR, "sites_%s.gz" % stamp), "wt", encoding="utf-8") as fh:
            for o in recs:
                fh.write(json.dumps(o, ensure_ascii=False) + "\n")
    allrec = checked()
    have = set()
    for p in glob.glob(os.path.join(SHARDS, "leads_rbq_*.gz")):
        with gzip.open(p, "rt", encoding="utf-8", newline="") as fh:
            have |= {r["buyer_key"] for r in csv.DictReader(fh)}
    rows, dets, by = [], [], collections.Counter()
    for dom, o in sorted(allrec.items()):
        for hit in o.get("hits") or []:
            h = H.get(hit["licence"])
            if not h:
                continue
            site = "https://%s/" % (urllib.parse.urlparse(o.get("final") or "").hostname or dom)
            row, det = lead_of(h, hit, site)
            if row["buyer_key"] in have:
                continue
            have.add(row["buyer_key"])
            rows.append(row); dets.append(det); by[hit["by"]] += 1
    # second way to a holder's site: a site the mailbox crawl read prints an RBQ licence number (tools/lead_crawl.py notes it in the site facts).
    # The number is looked up in the list; the holder must also be tied to that site by its name, its postal code or the domain of its register e-mail
    # (a directory or a supplier's page that lists other firms' licence numbers ties nobody).
    import biz_licences as BL
    import ap_crawler as C
    by_digits = {re.sub(r"\D", "", h["licence"]): h for h in H.values()}
    fp = os.path.join(INC, "claude_lead_site_facts.jsonl.gz")
    n_seen = n_untied = 0
    if os.path.exists(fp):
        for l in gzip.open(fp, "rt", encoding="utf-8"):
            if '"rbq"' not in l:
                continue
            try:
                o = json.loads(l)
                x = o["ids"]["rbq"]
            except (ValueError, KeyError, TypeError):
                continue
            h = by_digits.get(x.get("v") or "")
            if not h:
                continue
            n_seen += 1
            host = (urllib.parse.urlparse(o.get("site") or "").hostname or "").lower()
            names = [h["name"]] + [t for t in re.split(r"\s*[;|]\s*", h.get("other_names") or "") if t.strip()]
            pc = (h.get("postal") or "").replace(" ", "")
            tied = ("the domain of the holder's e-mail in the register" if h.get("domain") and host and C.registrable(h["domain"]) == C.registrable(host) else
                    "name" if o.get("site_name") and any(BL.names_agree(o["site_name"], nm) for nm in names) else
                    "postal code" if pc and re.search(r"(?<![A-Za-z0-9])%s\s?%s(?![A-Za-z0-9])" % (pc[:3], pc[3:]), o.get("address_quote") or "", re.I) else "")
            if not tied or not host:
                n_untied += 1
                continue
            row, det = lead_of(h, dict(by="licence number printed on the site (%s also agrees)" % tied, url=x.get("url") or o.get("site"), quote=x.get("q") or ""), "https://%s/" % host)
            if row["buyer_key"] in have:
                continue
            have.add(row["buyer_key"])
            rows.append(row); dets.append(det); by["licence number on a site already read"] += 1
        msg.append("sites already read that print a licence number of the list: %d (holder not tied to the site: %d)" % (n_seen, n_untied))
    if rows:
        with gzip.open(os.path.join(SHARDS, "leads_rbq_%s.gz" % stamp), "wt", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=LEAD_COLS)
            w.writeheader()
            w.writerows(rows)
        with gzip.open(os.path.join(SHARDS, "details_rbq_%s.gz" % stamp), "wt", encoding="utf-8") as fh:
            for d in dets:
                fh.write(json.dumps(d, ensure_ascii=False) + "\n")
    st = collections.Counter((o.get("st") or "?").split(":")[0] for o in allrec.values())
    msg.append("holders' own domains checked: %d (%s); new leads %d (%s); licence leads on file %d" % (len(allrec), ", ".join("%s %d" % kv for kv in st.most_common(7)), len(rows),
                                                                                                   ", ".join("%s %d" % kv for kv in by.most_common()), len(have)))
    print("RBQ licence holders: " + "; ".join(msg))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["pull", "sites", "merge"])
    ap.add_argument("dir", nargs="?", default="out")
    ap.add_argument("--csv", default="")
    ap.add_argument("--minutes", type=float, default=60)
    ap.add_argument("--workers", type=int, default=60)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--stamp", default="")
    a = ap.parse_args()
    {"pull": pull, "sites": sites, "merge": merge}[a.cmd](a)


if __name__ == "__main__":
    main()
