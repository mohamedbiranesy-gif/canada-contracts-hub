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
# what keeping a licence costs a year: the Régie's own tariff page (opened 2026-11-10; the same table is on the owner-builder page). The amount depends
# only on the kind of licence — general (annexe I) or specialised (annexes II, III) — which the register's categories state for every holder.
# Licences administered by the CMEQ / CMMTQ are billed by those corporations (their own dues on top): no amount is given for them.
RBQ_FEES = dict(url="https://www.rbq.gouv.qc.ca/licence/tarification-et-amendes/tarification-pour-lentrepreneur-de-construction/", read="2026-11-10", year="2026",
                quote="Maintien d’une licence – 2026 Type de licence Droits Frais Total Général (annexe I) 884,54 $ 105,27 $ 989,81 $ Général et spécialisé (annexes I, II et III) "
                      "884,54 $ 105,27 $ 989,81 $ Spécialisé (annexes II et III) 442,26 $ 105,27 $ 547,53 $",
                tax="Prenez note que les montants ne sont pas taxables")


def annual_fee(h):
    """(amount, kind of licence) from the Régie's tariff, or None: RBQ-administered licences only, kind read from the register's categories"""
    if h.get("body") != "rbq":
        return None
    cats = keyname(h.get("categories") or "")
    gen, spe = "generale" in cats, "specialisee" in cats
    if gen:
        return "989.81", "Général et spécialisé (annexes I, II et III)" if spe else "Général (annexe I)"
    if spe:
        return "547.53", "Spécialisé (annexes II et III)"
    return None


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


LEGAL_OK = re.compile(r"morale|societe|compagnie|coop|corporation|association|syndicat|organisme|fiducie|municipal|autorite publique|publique")


def keyname(s):
    return re.sub(r"[^a-z0-9]+", " ", unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()).strip()


def body_of(mandataire):
    k = keyname(mandataire)
    return "cmeq" if ("electric" in k or "cmeq" in k) else "cmmtq" if ("tuyauterie" in k or "cmmtq" in k) else "rbq"


def http(url, timeout=120):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    return urllib.request.urlopen(req, timeout=timeout)


def read_table(path):
    """rows of a CSV (encoding and delimiter found from the file) or of a JSON file (the first list of objects in it; nested objects are
    flattened one level), each row a dict with normalised keys (keyname)"""
    head = open(path, "rb").read(200000)
    if head.lstrip()[:1] in (b"[", b"{"):
        data = json.load(open(path, encoding="utf-8-sig"))

        def find(x, depth=0):
            if isinstance(x, list) and x and isinstance(x[0], dict):
                return x
            if isinstance(x, dict) and depth < 3:
                for v in x.values():
                    r = find(v, depth + 1)
                    if r:
                        return r
            return None
        rows = find(data) or []
        print("JSON: top %s; %d records; keys of the first: %s" % (type(data).__name__ if not isinstance(data, dict) else "object with keys %s" % list(data)[:12], len(rows), list(rows[0])[:40] if rows else []), flush=True)
        for r in rows:
            o = {}
            for k, v in r.items():
                if isinstance(v, dict):
                    for k2, v2 in v.items():
                        o[keyname(k2)] = v2
                        o[keyname(k + " " + k2)] = v2
                else:
                    o[keyname(k)] = v
            yield o
        return
    enc = "utf-8-sig"
    try:
        head.decode("utf-8-sig")
    except UnicodeDecodeError as e:
        if e.start < len(head) - 8:  # not just a multi-byte character cut at the end of the sample
            enc = "cp1252"
    first = head.split(b"\n", 1)[0].decode(enc, "replace")
    delim = max(",;\t|", key=first.count)
    print("CSV: encoding %s, delimiter %r, header: %s" % (enc, delim, first[:600]), flush=True)
    with open(path, encoding=enc, errors="replace", newline="") as f:
        for r in csv.DictReader(f, delimiter=delim):
            yield {keyname(k): v for k, v in r.items() if k}


FIELDS = dict(licence=("numero de licence", "no licence", "numero licence", "licence"), status=("statut de la licence", "statut licence", "statut"),
              type=("type de licence", "type licence"), issued=("date de delivrance", "date delivrance"), next_payment=("date du paiement annuel", "date paiement annuel", "date de paiement annuel"),
              body=("mandataire",), legal_status=("statut juridique",), name=("nom de l intervenant", "nom intervenant", "nom"), other=("autre nom", "autres noms"),
              neq=("neq", "numero d entreprise du quebec"), address=("adresse",), city=("municipalite",), phone=("numero de telephone", "telephone"), email=("courriel", "adresse courriel"),
              cat=("categorie", "categories et sous categories", "categories", "categories sous categories"), sub=("sous categories", "sous categorie"), restriction=("restriction",))


def text_of(v):
    if v is None:
        return ""
    if isinstance(v, (list, tuple)):
        return " | ".join(text_of(x) for x in v if x not in (None, ""))
    if isinstance(v, dict):
        return " ".join(text_of(x) for x in v.values() if x not in (None, ""))
    return str(v).strip()


def pull(a):
    os.makedirs("out", exist_ok=True)
    srcs = [a.csv] if a.csv else []
    if not srcs:
        meta = json.loads(http(API).read().decode("utf-8", "replace"))["result"]
        print("dataset: %s | modified %s | licence %s | resources: %s" % (meta.get("title"), meta.get("metadata_modified"), meta.get("license_title"),
                                                                          "; ".join("%s %s %s" % (r.get("format"), r.get("size"), r.get("url")) for r in meta.get("resources") or [])), flush=True)
        # the JSON resource first (the complete record of each licence); the CSV when the JSON cannot be read
        for fmt in ("JSON", "CSV"):
            for r in meta.get("resources") or []:
                if (r.get("format") or "").upper() == fmt:
                    dst = "out/rbq_raw.%s" % fmt.lower()
                    t0 = time.time()
                    try:
                        with http(r["url"], timeout=900) as resp, open(dst, "wb") as f:
                            while True:
                                b = resp.read(1 << 20)
                                if not b:
                                    break
                                f.write(b)
                        print("downloaded %s: %.0f MB in %.0f s" % (fmt, os.path.getsize(dst) / 1e6, time.time() - t0), flush=True)
                        srcs.append(dst)
                    except Exception as e:
                        print("%s not downloaded: %s" % (fmt, str(e)[:200]), flush=True)
                    break
        if not srcs:
            raise SystemExit("no resource downloaded")
    lic, n = {}, 0
    for src in srcs:
        lic, n, shown = {}, 0, 0
        try:
            for row in read_table(src):
                n += 1
                g = lambda k: next((text_of(row[c]) for c in FIELDS[k] if c in row and row[c] not in (None, "")), "")
                num = g("licence")
                if not num:
                    continue
                L = lic.get(num)
                if L is None:
                    L = lic[num] = {k: g(k) for k in ("licence", "status", "type", "issued", "next_payment", "body", "legal_status", "name", "other", "neq", "address", "city", "phone", "email", "restriction")}
                    L["cats"] = []
                    if shown < 2:
                        shown += 1
                        print("sample record: %s" % json.dumps({k: ("…" if re.search(r"courriel|telephone", k) else text_of(v)[:120]) for k, v in row.items()}, ensure_ascii=False)[:1500], flush=True)
                for k in ("cat", "sub"):
                    v = g(k)
                    if v and v not in L["cats"] and len(L["cats"]) < 12:
                        L["cats"].append(v[:160])
        except Exception as e:
            print("%s not read: %s: %s" % (src, type(e).__name__, str(e)[:200]), flush=True)
            lic = {}
        have = collections.Counter(k for L in lic.values() for k, v in L.items() if v)
        print("%s: rows %d; licences %d; fields filled: %s" % (src, n, len(lic), dict(have)), flush=True)
        if lic and have["name"] > 0.9 * len(lic) and have["legal_status"] > 0.5 * len(lic):
            break
        print("%s: the fields needed (holder's name, legal status) are not there — next resource" % src, flush=True)
        lic = {}
    if not lic:
        raise SystemExit("the list could not be read (see the lines above for its columns)")
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


ADDR = os.path.join(INC, "overture", "rbq_addr_candidates.csv")  # tools/overture_names.py addr --lanes rbq
ADONE = os.path.join(DIR, "addr_done.tsv")


def addr_sites(a):
    """2026-11-13: holders whose register entry gives no domain of their own (31,674 of 50,110): the websites an Overture Maps place at the
    holder's own postal code lists (tools/overture_names.py addr --lanes rbq). A site is kept by the same proofs as a register domain — the
    licence number or the telephone number as the register has them, or the site's own name agreeing with the holder's — except the postal
    code, which every business of the building prints: it counts only when the place itself bears the holder's name.
    -> out/rbq_sites.jsonl (the same records as `sites`, with "via"), out/rbq_addr_done.tsv"""
    import ap_crawler as C
    import biz_licences as BL
    import lead_crawl as LC
    import tech_relationships as T
    import tm_register as TM
    os.makedirs("out", exist_ok=True)
    os.makedirs(C.STATE, exist_ok=True)
    C.HOST_INTERVAL = 0.6
    if not os.path.exists(ADDR):
        print("no candidates (tools/overture_names.py addr --lanes rbq)", flush=True)
        return
    H = {h["licence"]: h for h in holders()}
    cand = collections.defaultdict(list)
    for r in csv.DictReader(open(ADDR, encoding="utf-8", newline="")):
        if r["key"] in H:
            cand[r["key"]].append(r)
    done = {l.split("\t")[0] for l in open(ADONE, encoding="utf-8")} if os.path.exists(ADONE) else set()
    todo = [k for k in sorted(cand) if k not in done]
    if a.limit:
        todo = todo[:a.limit]
    print("holders with a place at their own postal code that lists a website: %d; asked before: %d; to read now: %d" % (len(cand), len(done), len(todo)), flush=True)
    deadline = time.time() + a.minutes * 60
    lock, stats = threading.Lock(), collections.Counter()
    fo = open("out/rbq_sites.jsonl", "a", encoding="utf-8")
    fd = open("out/rbq_addr_done.tsv", "a", encoding="utf-8")

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

    def one(lic):
        if time.time() > deadline:
            return
        h = H[lic]
        got = ""
        for c in cand[lic]:
            dom = c["site"]
            rec = {"dom": dom, "date": TODAY, "st": "", "hits": [], "via": "an Overture Maps place at the holder's own postal code (%s; “%s”, place %s, release %s)" % (
                c["place_postcode"], c["place_name"], c["place_id"], c["release"])}
            try:
                res, raw, final = page("https://%s/" % dom)
                rec["st"], rec["final"] = res, final
                if res != "ok":
                    continue
                fhost = (urllib.parse.urlparse(final).hostname or dom).lower()
                title, meta = T.page_meta(raw)
                name = LC.site_name_for(fhost, meta.get("og:site_name"), title, T)
                rec["name"] = name or ""
                pages = [(final, raw)]
                for link, label in C.links(raw, final):
                    p_ = urllib.parse.urlparse(link)
                    if (p_.scheme in ("http", "https") and C.registrable((p_.hostname or "").lower()) == C.registrable(fhost) and not C.SKIP_EXT.search(p_.path)
                            and CONTACT.search(p_.path + " " + label) and len(pages) < 3 and link.split("#")[0].rstrip("/") != final.rstrip("/")):
                        r2, raw2, f2 = page(link.split("#")[0])
                        if r2 == "ok":
                            pages.append((f2, raw2))
                pr = [(w, rx) for w, rx in proofs(h) if w != "postal code" or TM.place_fits(h["name"] + " " + (h.get("other_names") or ""), c.get("place_name") or "")]
                hit = None
                for url, rw in pages:
                    text = C.visible(rw)
                    for what, rx in pr:
                        m = rx.search(text)
                        if m:
                            hit = dict(licence=lic, by=what, url=url, quote=re.sub(r"\s+", " ", text[max(0, m.start() - 110):m.end() + 110]).strip()[:300])
                            break
                    if hit:
                        break
                if not hit and name and (BL.names_agree(name, h["name"]) or any(BL.names_agree(name, o) for o in re.split(r"\s*[;|]\s*", h.get("other_names") or "") if o.strip())):
                    hit = dict(licence=lic, by="name", url=final, quote="site name “%s” — holder “%s”%s" % (name[:90], h["name"][:90], (" / “%s”" % h["other_names"][:80]) if h.get("other_names") else ""))
                if hit:
                    hit["register_email_on_page"] = any(h.get("email") and h["email"] in rw.lower() for _, rw in pages if rw)
                    rec["hits"].append(hit)
                rec["st"] = "confirmed" if rec["hits"] else "not_confirmed"
            except Exception as e:
                rec["st"] = "error:" + type(e).__name__
            finally:
                with lock:
                    stats[rec["st"].split(":")[0]] += 1
                    for x in rec["hits"]:
                        stats["by " + x["by"]] += 1
                    if rec["st"] in ("confirmed", "not_confirmed"):
                        fo.write(json.dumps(rec, ensure_ascii=False) + "\n")
            if rec["hits"]:
                got = dom
                break
        with lock:
            fd.write("%s\t%s\n" % (lic, got))
            stats["holders asked"] += 1
            stats["holders tied"] += bool(got)
            if stats["holders asked"] % 300 == 0:
                fo.flush(); fd.flush()
                print(time.strftime("%H:%M:%S"), dict(stats), flush=True)
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(one, todo))
    fo.close(); fd.close()
    print("addr finished", dict(stats), flush=True)


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
    fee = annual_fee(h)
    if fee:
        det.update(value=fee[0], currency="CAD",
                   value_basis="the Régie's published %s tariff for keeping a licence of the kind “%s” — the holder's categories in the register: %s; %s, read %s: “%s”; "
                               "“%s”; a tariff, not a payment record" % (RBQ_FEES["year"], fee[1], (h.get("categories") or "")[:120], RBQ_FEES["url"], RBQ_FEES["read"],
                                                                          RBQ_FEES["quote"], RBQ_FEES["tax"]))
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
    _ad = os.path.join(a.dir, "rbq_addr_done.tsv")
    if os.path.exists(_ad):  # 2026-11-13: holders asked with the places at their own postal code
        _old = open(ADONE, encoding="utf-8").read().splitlines() if os.path.exists(ADONE) else []
        _seen = set(_old)
        _new = [l for l in open(_ad, encoding="utf-8").read().splitlines() if l and l not in _seen]
        with open(ADONE, "a", encoding="utf-8") as _f:
            for l in _new:
                _f.write(l + "\n")
        msg.append("holders asked with the places at their own postal code: %d more" % len(_new))
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
    # the details on file per lead (the newest shard wins): a holder whose register facts changed — date of the next annual payment, categories,
    # the tariff — gets a fresh details record in this run's shard (the lead row itself stays where it is)
    old_det = {}
    for p in sorted(glob.glob(os.path.join(SHARDS, "details_rbq_*.gz"))):
        with gzip.open(p, "rt", encoding="utf-8") as fh:
            for l in fh:
                try:
                    d = json.loads(l)
                    old_det[d["key"]] = d
                except (ValueError, KeyError):
                    pass
    SUBST = ("value", "value_basis", "start", "end", "title", "reference", "member_address_quote", "vendor", "vendor_address")
    rows, dets, by, n_fresh, fresh_done = [], [], collections.Counter(), 0, set()
    for dom, o in sorted(allrec.items()):
        for hit in o.get("hits") or []:
            h = H.get(hit["licence"])
            if not h:
                continue
            site = "https://%s/" % (urllib.parse.urlparse(o.get("final") or "").hostname or dom)
            row, det = lead_of(h, hit, site)
            if row["buyer_key"] in have:
                od = old_det.get(row["buyer_key"])
                if od is not None and row["buyer_key"] not in fresh_done and any((od.get(k) or "") != (det.get(k) or "") for k in SUBST):
                    fresh_done.add(row["buyer_key"])
                    dets.append(det); n_fresh += 1
                continue
            have.add(row["buyer_key"])
            rows.append(row); dets.append(det); by[hit["by"]] += 1
    # second way to a holder's site: a site the mailbox crawl read prints an RBQ licence number (tools/lead_crawl.py notes it in the site facts).
    # The number is looked up in the list; the holder must also be tied to that site by its name, its postal code or the domain of its register e-mail
    # (a directory or a supplier's page that lists other firms' licence numbers ties nobody).
    import biz_licences as BL
    import ap_crawler as C
    by_digits = {re.sub(r"\D", "", h["licence"]): h for h in H.values()}
    import lead_crawl as LCF
    n_seen = n_untied = 0
    if True:
        for o in LCF.facts_records():  # the single facts file of before 2026-11-10 and the shards of site_facts/
            try:
                x = o["ids"]["rbq"]
            except (KeyError, TypeError):
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
    # fourth way (2026-11-10, scan detector 5): the scan keeps the register numbers every home page prints. A holder must print its licence
    # number, and on a home page that prints exactly ONE number it is the site operator's own. Measured on 19 such home pages: 17 numbers
    # are on the list, 9 of them holders the register's e-mail domain had not led to. A second fact must agree, as above: the site's own
    # name (site name, copyright line or stated legal name) with the holder's legal or other name, the holder's postal code on the home
    # page, or the domain of the holder's e-mail in the register.
    try:
        import credit_scan as CS
        n4 = collections.Counter()
        own = {}
        for l in CS.state_lines("links"):
            q = l.split("\t")
            if len(q) >= 4:
                own[q[0]] = (q[3].split("|") + ["", "", "", ""])[:4]
        for l in CS.state_lines("sections"):
            if '"n": ' not in l:
                continue
            try:
                o = json.loads(l)
            except ValueError:
                continue
            nums = {}
            for x in o.get("n") or []:  # ["rbq", "5760390401", "RBQ : 5760-3904-01"]; the first shards of the pass wrote "rbq:5760390401"
                kind, num, printed = (x + [""])[:3] if isinstance(x, list) else (x.split(":", 1) + [""])[:3]
                if kind == "rbq":
                    nums[num] = printed
            if not nums:
                continue
            n4["home pages that print an RBQ licence number"] += 1
            if len(nums) != 1:
                n4["several numbers on one home page (tied to nobody)"] += 1
                continue
            num, printed = next(iter(nums.items()))
            h = by_digits.get(num)
            if not h:
                n4["number not on the list of active licences of legal persons"] += 1
                continue
            host = o["dom"]
            f = own.get(host) or ["", "", "", ""]
            names = [h["name"]] + [t for t in re.split(r"\s*[;|]\s*", h.get("other_names") or "") if t.strip()]
            pc = (h.get("postal") or "").replace(" ", "").upper()
            tied = ("the domain of the holder's e-mail in the register" if h.get("domain") and C.registrable(h["domain"]) == C.registrable(host) else
                    "the site's own name" if any(f[i] and any(BL.names_agree(f[i], nm) for nm in names) for i in (0, 1, 2)) else
                    "the holder's postal code on the home page" if pc and f[3] == pc else "")
            if not tied:
                n4["holder not tied to the site by a second fact"] += 1
                continue
            row, det = lead_of(h, dict(by="its home page prints the holder's licence number (%s also agrees)" % tied, url=o.get("page") or "https://%s/" % host,
                                       quote=printed or "licence number %s-%s-%s (digits as read on the home page, %s)" % (num[:4], num[4:8], num[8:], o.get("date") or "")), "https://%s/" % host)
            if row["buyer_key"] in have:
                n4["already a lead"] += 1
                continue
            have.add(row["buyer_key"])
            rows.append(row); dets.append(det); by["licence number on the home page (scan)"] += 1
            n4["tied"] += 1
        if n4:
            msg.append("home pages read by the scan that print a licence number: %s" % dict(sorted(n4.items())))
    except Exception as e:
        msg.append("licence numbers on home pages (scan) skipped: %s: %s" % (type(e).__name__, str(e)[:160]))
    # third way (2026-11-10): 28,000 holders give the register a webmail address and 4,500 none, so their own site cannot be read off the register.
    # An organisation we already hold (a delivered row, or a site the crawl read) whose OWN site prints the holder's postal code or telephone, and
    # whose name agrees with the holder's legal or other name by the strict rule of the business licences, is that holder. Several holders fitting
    # one organisation tie nobody.
    try:
        n3 = collections.Counter()
        by_pc, by_ph = collections.defaultdict(list), collections.defaultdict(list)
        for h in H.values():
            _pc = re.sub(r"\s", "", h.get("postal") or "").upper()
            if len(_pc) == 6:
                by_pc[_pc].append(h)
            if len(h.get("phone") or "") == 10:
                by_ph[h["phone"]].append(h)
        for host, O in BL.org_universe().items():
            if not O["names"]:
                continue
            m = BL.PC.search((O["addr"] or "").upper())
            _pc = (m.group(1) + m.group(2)) if m else ""
            cands = {}
            for h in by_pc.get(_pc, []) if _pc else []:
                cands[h["licence"]] = (h, "postal code %s %s" % (_pc[:3], _pc[3:]))
            for h in by_ph.get(O["phone"], []) if len(O["phone"]) == 10 else []:
                cands[h["licence"]] = (h, (cands[h["licence"]][1] + " and telephone number") if h["licence"] in cands else "telephone number")
            if not cands:
                continue
            n3["organisations with a holder at their postal code / telephone"] += 1
            hits = [(h, how) for h, how in cands.values()
                    if BL.lic_agrees(O["names"], {"name": h["name"], "trade": " | ".join(t.strip() for t in re.split(r"\s*[;|]\s*", h.get("other_names") or "") if t.strip())})]
            if not hits:
                continue
            if len({keyname(h["name"]) for h, _ in hits}) > 1:
                n3["several holders fit one organisation (dropped)"] += 1
                continue
            h, how = sorted(hits, key=lambda x: x[0].get("next_payment") or "", reverse=True)[0]
            row, det = lead_of(h, dict(by="the organisation's own site prints the holder's %s and its name agrees with the register's (%s ~ %s)" % (how, O["names"][0][:60], h["name"][:60]),
                                       url=O.get("addr_url") or "https://%s/" % host, quote=(O["addr"] or "")[:300]), "https://%s/" % host)
            if row["buyer_key"] in have:
                n3["already a lead"] += 1
                continue
            have.add(row["buyer_key"])
            rows.append(row); dets.append(det); by["postal code / telephone + name"] += 1
            n3["tied (row tier %s)" % (O["tier"] or "not delivered yet")] += 1
        msg.append("holders tied to an organisation we hold by postal code / telephone + name: %s" % dict(sorted(n3.items())))
    except Exception as e:
        msg.append("postal code / telephone join skipped: %s: %s" % (type(e).__name__, str(e)[:160]))
    if rows:
        with gzip.open(os.path.join(SHARDS, "leads_rbq_%s.gz" % stamp), "wt", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=LEAD_COLS)
            w.writeheader()
            w.writerows(rows)
    if dets:
        msg.append("details refreshed for leads already on file: %d" % n_fresh)
        with gzip.open(os.path.join(SHARDS, "details_rbq_%s.gz" % stamp), "wt", encoding="utf-8") as fh:
            for d in dets:
                fh.write(json.dumps(d, ensure_ascii=False) + "\n")
    st = collections.Counter((o.get("st") or "?").split(":")[0] for o in allrec.values())
    msg.append("holders' own domains checked: %d (%s); new leads %d (%s); licence leads on file %d" % (len(allrec), ", ".join("%s %d" % kv for kv in st.most_common(7)), len(rows),
                                                                                                   ", ".join("%s %d" % kv for kv in by.most_common()), len(have)))
    print("RBQ licence holders: " + "; ".join(msg))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["pull", "sites", "merge", "addr-sites"])
    ap.add_argument("dir", nargs="?", default="out")
    ap.add_argument("--csv", default="")
    ap.add_argument("--minutes", type=float, default=60)
    ap.add_argument("--workers", type=int, default=60)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--stamp", default="")
    a = ap.parse_args()
    {"pull": pull, "sites": sites, "merge": merge, "addr-sites": addr_sites}[a.cmd](a)


if __name__ == "__main__":
    main()
