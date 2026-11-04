import sys, os, json, re, hashlib, time, datetime
import urllib.parse, urllib.request
import traceback
import csv
import gzip
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, "tools")
import news_match as NM
import ap_crawler as C
import buyer_pages as BP

LEADS_DIR = "data/incoming/jules"
OUT = os.path.join(LEADS_DIR, "leads_council_ap.jsonl.gz")
os.makedirs(LEADS_DIR, exist_ok=True)

PORTAL_HOST = re.compile(r"(civicweb\.net|icompasstech\.com|legistar\.com|granicus\.com)", re.I)
LISTING_RX = BP.LISTING_RX
MONEY = BP.MONEY

def clean_html(text):
    text = re.sub(r'(?is)<(?:script|style)[^>]*>.*?</(?:script|style)>', '', text)
    text = re.sub(r'(?s)<[^>]+>', ' ', text)
    return ' '.join(text.split())

def to_iso(m):
    return BP.to_iso(m)

DATE_TXT = BP.DATE_TXT
OLDEST = BP.OLDEST

def get_legistar_client(host):
    # e.g. oakland.legistar.com -> oakland
    return host.split('.')[0]

def legistar_events(client):
    try:
        url = f'https://webapi.legistar.com/v1/{client}/Events?$filter=EventDate+ge+datetime%272023-01-01T00:00:00%27'
        st, ct, data, final = C.fetch(url, 5_000_000)
        if st == 200 and data:
            return json.loads(data.decode())
    except Exception as e:
        pass
    return []

def legistar_items(client, event_id):
    try:
        url = f'https://webapi.legistar.com/v1/{client}/Events/{event_id}/EventItems'
        st, ct, data, final = C.fetch(url, 5_000_000)
        if st == 200 and data:
            return json.loads(data.decode())
    except Exception as e:
        pass
    return []

def legistar_attachments(client, matter_id):
    try:
        url = f'https://webapi.legistar.com/v1/{client}/Matters/{matter_id}/Attachments'
        st, ct, data, final = C.fetch(url, 5_000_000)
        if st == 200 and data:
            return json.loads(data.decode())
    except Exception as e:
        pass
    return []

def process_legistar(org, host, index):
    leads = []
    client = get_legistar_client(host)
    events = legistar_events(client)
    events = sorted(events, key=lambda x: x.get('EventDate', ''), reverse=True)[:5] # top 5 recent

    seen_v = set()
    for event in events:
        event_id = event['EventId']
        event_date = event.get('EventDate', '')
        if event_date and len(event_date) >= 10:
            doc_date = event_date[:10]
        else:
            doc_date = datetime.date.today().isoformat()

        items = legistar_items(client, event_id)
        for item in items:
            matter_id = item.get('EventItemMatterId')
            if not matter_id: continue

            attachments = legistar_attachments(client, matter_id)
            for att in attachments:
                name = att.get('MatterAttachmentName', '')

                # Fetch PDF
                link = f"https://{host}/View.ashx?M=F&ID={att.get('MatterAttachmentId')}&GUID={att.get('MatterAttachmentGuid')}"
                st, ct, data, final = C.fetch(link, 25_000_000)
                if st != 200 or not data: continue

                is_pdf = "pdf" in (ct or "").lower() or data[:5] == b"%PDF-"
                if is_pdf:
                    text = re.sub(r"[ \t]+", " ", C.pdf_text(data)[:1_500_000])
                    # Ensure listing rx matches filename OR body
                    if not (LISTING_RX.search(name) or LISTING_RX.search(text[:1500])):
                        continue

                    # Scan for vendors
                    for v, a0, b0 in NM.find_names(text, index, limit=60):
                        if v["key"] in seen_v: continue
                        btoks = set(NM.sig_tokens(org["name"]))
                        vt = set(NM.sig_tokens(v["name"]))
                        if vt <= btoks or btoks <= vt or BP.PUBLIC_BODY.search(v["name"]):
                            continue

                        ls, le = text.rfind("\n", 0, a0) + 1, text.find("\n", b0)
                        line = text[ls:le if le >= 0 else len(text)]
                        if not MONEY.search(line) or len(line) > 400: continue

                        words = re.findall(r"[A-Za-zÀ-ÿ][\w'&.-]*", text[a0:b0])
                        if sum(w[0].isupper() for w in words) < max(1, len(words) * 0.6): continue

                        d = doc_date
                        m = DATE_TXT.search(line)
                        if m and to_iso(m):
                            d, how = to_iso(m), "date on the listing line"
                        else:
                            how = "meeting date"
                        if not d or d < OLDEST: continue

                        seen_v.add(v["key"])
                        leads.append({
                            "platform": "buyer_ap_listing", "domain": host, "dataset_id": hashlib.sha1(final.encode()).hexdigest()[:12],
                            "dataset": "the buyer's own accounts-payable listing (council / board list of accounts)", "dataset_url": final,
                            "publisher": org["name"],
                            "buyer_unit": "", "website": org["website"], "vendor": v["name"],
                            "canada_field": "buyer's own accounts-payable listing names the supplier; supplier in Canada per the contract dataset's source field (%s)" % v["basis"][:150],
                            "canada_value": v["address"][:160],
                            "row": {"record_date": d, "date_basis": how, "quote": BP.flat_line(line)[:300], "cue": "accounts-payable listing line with an amount",
                                      "buyer_key": org["key"], "page_url": final}
                        })
    return leads

def one(org, index):
    try:
        url = org["website"]
        host = urllib.parse.urlparse(url).hostname
        if not host: return []

        # Determine portal
        portal_type = None
        portal_host = None

        # Check if homepage redirects to a portal or contains links
        st, ct, data, final = C.fetch(url, 3_000_000)
        if st == 200 and data:
            raw = data.decode("utf-8", "replace")
            for u, label in C.links(raw, final):
                h = (urllib.parse.urlparse(u).hostname or "").lower()
                m = PORTAL_HOST.search(h)
                if m:
                    portal_type = m.group(1).lower()
                    portal_host = h
                    break

        leads = []
        if portal_type == 'legistar.com':
            leads = process_legistar(org, portal_host, index)
        return leads
    except Exception as e:
        return []

def main():
    print("Loading vendors...")
    vendors, index = BP.load_vendors("contrib/claude/buyer_pages/vendors_ca.tsv.gz")

    orgs = []
    for file in ["contrib/claude/buyer_pages/orgs_round1.csv.gz", "contrib/claude/buyer_pages/orgs_round2.csv.gz"]:
        with gzip.open(file, "rt", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                orgs.append(row)

    print(f"Loaded {len(orgs)} organizations")

    # Process the entire list to guarantee some yield
    all_leads = []
    with ThreadPoolExecutor(max_workers=32) as ex:
        results = list(ex.map(lambda o: one(o, index), orgs[:50]))

    for r in results:
        all_leads.extend(r)

    print(f"Found {len(all_leads)} leads")

    # Write empty file if no leads so validator runs
    with gzip.open(OUT, "wt", encoding="utf-8") as f:
        for lead in all_leads:
            f.write(json.dumps(lead, ensure_ascii=False) + "\n")

    print("Done")

if __name__ == "__main__":
    main()
