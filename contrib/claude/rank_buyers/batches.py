import array, csv, collections, gzip, io, os, shutil, sys
csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
SRC = os.environ.get("BATCHES_SRC") or ROOT + "/out/ranked/ranked_buyers.csv"
DST = os.environ.get("BATCHES_DST") or ROOT + "/out/ranked/batches"
# 2026-11-10 (disk): the table is 15 KB a row as plain CSV — 2.6 GB at 170,000 rows, 15 GB at a million, on a runner with ~14 GB free. The ranker
# no longer writes the plain file; the table is read from ranked_buyers.csv.gz (same text, same line-end handling).
def src_open():
    """the ranked table as text: the plain CSV when it is there (local runs), otherwise the compressed copy"""
    if SRC.endswith(".gz"):
        return gzip.open(SRC, "rt", encoding="utf-8")
    if os.path.exists(SRC):
        return open(SRC, encoding="utf-8")
    return gzip.open(SRC + ".gz", "rt", encoding="utf-8")
# 2026-11-10: streaming. The table was loaded whole (list of dicts: ~6 times its size in memory — fine at 70,000 rows, impossible at a million).
# Now: pass 1 reads each row once and notes its package and score (two small integers per row); pass 2 writes each row to its package part,
# unsorted; pass 3 sorts one part at a time (a part is ~45 MB). Same packages, same order inside a package, same cells.
OK = ("confirmed",)  # owner 2026-11-04 ("ironclad"): referee-confirmed only; dataset-enrichment mailboxes wait in P11 until the referee has seen them
def rel(r):
    st, t = r["contract_status"], r.get("tier", "")
    return ("weak" if t == "F" else "inferred" if t == "I" else "member" if t == "M" else "registry" if t == "R" else
            "tech" if st.startswith("active service seen") else "client" if st.startswith("client listing") else "other_link" if st.startswith("linked from") else
            "older" if st.startswith(("end date unknown", "payment / subaward")) else "likely" if st.startswith("likely active (awarded 12-36") else "active")
# One row per buyer, in the best package it qualifies for (owner's layout, 2026-11-01): every package row has an email.
B = collections.OrderedDict([
 ("P01_GOLD_active_relationship_invoicing_AP_email", lambda r: r["rank_group"] == "GOLD"),
 ("P01T_active_service_seen_on_buyer_site_invoicing_AP_email", lambda r: r["rank_group"] == "GOLD-T"),
 ("P02_active_relationship_finance_accounting_email", lambda r: rel(r) == "active" and r["grade"] == "3" and r["email_check"] in OK),
 ("P03_active_relationship_purchasing_email", lambda r: rel(r) == "active" and r["grade"] == "2" and r["email_check"] in OK),
 ("P04_active_relationship_general_email", lambda r: rel(r) == "active" and r["grade"] == "1" and r["email_check"] in OK),
 ("P05_likely_active_awarded_12_36_months_any_email", lambda r: rel(r) == "likely" and r["email"] and r["email_check"] in OK),
 ("P06_client_listing_invoicing_AP_email", lambda r: rel(r) == "client" and r["grade"] == "4" and r["email_check"] in OK),
 ("P06T_active_service_seen_on_buyer_site_other_email", lambda r: rel(r) == "tech" and r["email"] and r["email_check"] in OK),
 ("P07_client_listing_finance_or_purchasing_email", lambda r: rel(r) == "client" and r["grade"] in ("2", "3") and r["email_check"] in OK),
 ("P08_client_listing_general_email", lambda r: rel(r) == "client" and r["grade"] == "1" and r["email_check"] in OK),
 ("P09_older_contract_or_payment_any_email", lambda r: rel(r) == "older" and r["email"] and r["email_check"] in OK),
 ("P10_linked_from_vendor_site_any_email", lambda r: rel(r) == "other_link" and r["email"] and r["email_check"] in OK),
 # claude 2026-11-10 (owner 2026-11-09: "some Canadian entity receives money for a service … established online"): the organisation's own .ca domain
 # name is registered — an agreement in force with the Canadian Internet Registration Authority, paid for through a CIRA-certified (Canadian)
 # registrar. A recorded current relationship, generic by nature: its own package, below every named-vendor relationship, above the inferred ones
 ("P10R_ca_domain_registration_contract_own_email", lambda r: rel(r) == "registry" and r["email"] and r["email_check"] in OK),
 ("P11_any_relationship_email_not_yet_confirmed", lambda r: bool(r["email"]) and rel(r) not in ("weak", "inferred", "member")),
 # owner 2026-11-03: P12 weaker relationship within 5 years (ended contract, or vendor in Canada only by registry match),
 # P13 inferred relationship (no record) from the buyer's type and province; both need the buyer's own confirmed mailbox
 ("P12_weaker_relationship_within_5_years_own_email", lambda r: rel(r) == "weak" and r["email"] and r["email_check"] in OK),
 ("P13_inferred_relationship_no_record_own_email", lambda r: rel(r) == "inferred" and r["email"] and r["email_check"] in OK),
 # claude 2026-11-03 (owner: "no door closed"; own package, never mixed with P01): the organisation is on the CURRENT member /
 # participant / regulated-institution list that a Canadian body publishes, and pays that body (premiums, market charges,
 # assessments, dues; the fee basis is quoted); P01M needs the organisation's own confirmed invoicing mailbox
 ("P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email", lambda r: r["rank_group"] == "GOLD-M"),
 ("P06M_member_or_regulated_payer_of_canadian_body_other_email", lambda r: rel(r) == "member" and r["email"] and r["email_check"] in OK),
 ("Z_no_email_yet_not_delivered", lambda r: True),
])
# owner 2026-11-03 "make sure all the fields are populated": a field no source gives is written as the literal
# not_published (never blank); Z has no mailbox found yet, which is not the same as none published.
EMAIL_COLS = ("email", "email_type", "email_check", "email_evidence_url", "email_evidence_quote")
GST_LABEL = " (derived: BN9 + RT0001, not confirmed in the CRA registry)"
def filled(r, package):
    r = dict(r)
    if r.get("vendor_gst_hst_derived") and "derived" not in r["vendor_gst_hst_derived"]:
        r["vendor_gst_hst_derived"] += GST_LABEL
    for c in r:
        v = (r[c] or "").strip()
        if v in ("", "{}", "[]", "null", "None"):
            r[c] = "not_found_yet" if (package.startswith("Z") and c in EMAIL_COLS) else "not_published"
    return r
PART_BYTES = 45 * 1024 * 1024
names = list(B.keys())
preds = list(B.values())
pk = array.array("H")       # package index of each row
score = array.array("i")    # -completeness score of each row
size = collections.Counter()  # bytes of each package as it will be written
count = collections.Counter()
blank = collections.Counter()
groups_left = collections.Counter()
with src_open() as f:  # as the earlier code read it (line ends inside a cell become \n)
    rd = csv.DictReader(f)
    cols = rd.fieldnames
    for r in rd:
        pi = next(i for i, fn in enumerate(preds) if fn(r))
        pk.append(pi)
        score.append(-int(float(r["completeness_score"] or 0)))
        count[pi] += 1
        nb = sum(1 for c in r if (r[c] or "").strip() in ("", "{}"))
        blank[pi] += nb
        size[pi] += sum(len(v or "") + 1 for v in r.values()) + nb * 13
# rank of each row inside its package: by score (best first), then by its place in the table (the sort the old code did, stable)
order = sorted(range(len(pk)), key=lambda i: (pk[i], score[i], i))
rank = array.array("l", [0]) * len(pk)
pos = collections.Counter()
for i in order:
    rank[i] = pos[pk[i]]
    pos[pk[i]] += 1
del order
parts = {pi: max(1, int(size[pi] // PART_BYTES) + 1) for pi in count}
step = {pi: -(-count[pi] // parts[pi]) for pi in count}
# 2026-11-10 (disk): the package files are written compressed (<package>.csv.gz — tools/batch_files.py reads them; the release's zip still holds
# plain .csv members). As plain text the packages are 15 KB a row: 2.6 GB at 170,000 rows, 15 GB at a million, on a runner with ~14 GB free —
# and a second, unsorted copy of them was on disk while they were written. A package whose rows already stand in the table in the package's own
# order (every package but Z, as the table is sorted today) is now written straight into its files; only the others take the unsorted working copy.
seen_n = collections.Counter()
in_order = {pi: True for pi in count}
for i in range(len(pk)):
    if rank[i] != seen_n[pk[i]]:
        in_order[pk[i]] = False
    seen_n[pk[i]] += 1
del seen_n


def final_path(pi, part):
    name = names[pi]
    return os.path.join(DST, name + ".csv.gz") if parts.get(pi, 1) == 1 else os.path.join(DST, "%s_part%d_of_%d.csv.gz" % (name, part + 1, parts[pi]))


def gz_writer(path):
    """a compressed text file whose bytes depend only on its content (no time stamp in the header)"""
    raw = open(path, "wb")
    gz = gzip.GzipFile(filename="", mode="wb", fileobj=raw, compresslevel=6, mtime=0)
    return raw, gz, io.TextIOWrapper(gz, encoding="utf-8", newline="")


def gz_close(h):
    raw, gz, tx = h
    tx.flush(); tx.detach(); gz.close(); raw.close()


shutil.rmtree(DST, ignore_errors=True)
os.makedirs(DST, exist_ok=True)
tmp = DST + ".tmp"
shutil.rmtree(tmp, ignore_errors=True)
os.makedirs(tmp)
handles = collections.OrderedDict()  # working copies (packages not in order): at most 200 part files open at a time
direct = {}  # package -> (part, handle, csv writer): the one file of the package that is being written


def out(pi, part):
    key = (pi, part)
    h = handles.pop(key, None)
    if h is None:
        if len(handles) >= 200:
            _, (fh0, _w0) = handles.popitem(last=False)
            fh0.close()
        fh = open(os.path.join(tmp, "%d_%d.csv" % key), "a", newline="", encoding="utf-8")
        h = (fh, csv.writer(fh))
    handles[key] = h
    return h[1]


with src_open() as f:  # as the earlier code read it (line ends inside a cell become \n)
    rd = csv.DictReader(f)
    for i, r in enumerate(rd):
        pi = pk[i]
        fr = filled(r, names[pi])
        part = rank[i] // step[pi]
        if in_order[pi]:
            cur = direct.get(pi)
            if cur is None or cur[0] != part:
                if cur is not None:
                    gz_close(cur[1])
                h = gz_writer(final_path(pi, part))
                cur = direct[pi] = (part, h, csv.writer(h[2]))
                cur[2].writerow(cols)
            cur[2].writerow([fr[c] for c in cols])
        else:
            out(pi, part).writerow([rank[i]] + [fr[c] for c in cols])
for fh, _w in handles.values():
    fh.close()
for _part, h, _w in direct.values():
    gz_close(h)
summary = []
for pi, name in enumerate(names):
    if not count[pi]:
        h = gz_writer(os.path.join(DST, name + ".csv.gz"))  # an empty package still has its file (header only), as before
        csv.writer(h[2]).writerow(cols)
        gz_close(h)
        summary.append((name, 0))
        continue
    for part in range(parts[pi]):
        if in_order[pi]:
            continue  # written above
        p = os.path.join(tmp, "%d_%d.csv" % (pi, part))
        rows_ = []
        if os.path.exists(p):
            with open(p, encoding="utf-8", newline="") as fh:
                rows_ = list(csv.reader(fh))
            os.remove(p)  # the working copy of this part is not needed again
        rows_.sort(key=lambda x: int(x[0]))
        h = gz_writer(final_path(pi, part))
        w = csv.writer(h[2])
        w.writerow(cols)
        for x in rows_:
            w.writerow(x[1:])
        gz_close(h)
    summary.append((name + ("" if parts[pi] == 1 else " (%d part files)" % parts[pi]), count[pi]))
shutil.rmtree(tmp, ignore_errors=True)
for n, c in summary: print("%-55s %6d" % (n, c))
print("unassigned", 0, [])
print("blank cells filled with not_published (delivered P01-P13):", sum(v for pi, v in blank.items() if not names[pi].startswith("Z")))
print("package files: compressed (.csv.gz); packages written straight from the table (already in order): %d of %d%s" % (
    sum(1 for pi in count if in_order[pi]), len(count),
    "".join("; sorted from a working copy: %s (%d rows)" % (names[pi].split("_")[0], count[pi]) for pi in sorted(count) if not in_order[pi])))
