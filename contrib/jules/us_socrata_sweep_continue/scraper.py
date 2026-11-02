import json, re, sys, os, gzip, urllib.request, urllib.parse, datetime, hashlib

REF = "2026-11-01"
OUT_FILE = "data/incoming/jules/records_us_socrata_sweep_continue.jsonl.gz"

PROVS = ["ON", "QC", "BC", "AB", "MB", "SK", "NS", "NB", "NL", "PE", "YT", "NT", "NU", "ONT", "QUE", "PQ", "B.C.", "ALTA", "MAN", "SASK", "N.S.", "N.B.", "NFLD", "P.E.I.", "CANADA", "CAN", "CDN"]

PLACEHOLDER = re.compile(r"^(n/?a|none|null|unknown|undisclosed|confidential|withheld|redacted|various|multiple|tbd|-+|\.+)$|undisclosed|confidential client|nom retenu", re.I)

DATASETS = [
    ("corstat.coronaca.gov", "mdmf-aswt", "CorStat - Corona Open Expenditures", [("vendor_st", "state"), ("vendor_city", "city")]),
    ("citydata.mesaaz.gov", "u5x3-dvhs", "Business Services - Purchases", [("vendor_state", "state")]),
    ("controllerdata.lacity.org", "4bdv-srep", "EcheckBook_Data_2012_To_2017", [("supplier_country", "country"), ("supplier_city", "city")]),
    ("data.brla.gov", "7fq7-8j7r", "EBR Building Permits", [("address", "address")]),
    ("data.brla.gov", "vwa8-ps2a", "City-Parish Expenditures", [("vendor_state", "state")]),
    ("data.brla.gov", "54bn-2sqf", "Legacy Purchase Orders", [("vend_city", "city")]),
    ("data.brla.gov", "2ung-w7t4", "Purchase Orders and Contracts", [("vendor_state", "state")]),
    ("cthru.data.socrata.com", "f7y8-q6ex", "Comptroller of the Commonwealth Spending", [("state", "state"), ("city", "city")]),
    ("cthru.data.socrata.com", "2bxs-ytms", "Comptroller of the Commonwealth Spending", [("state", "state"), ("city", "city")]),
    ("cthru.data.socrata.com", "pegc-naaa", "Comptroller of the Commonwealth Spending", [("state", "state"), ("city", "city")]),
    ("data.cincinnati-oh.gov", "vmk6-gy84", "Cincinnati Building Permits Contacts", [("address_2", "address")]),
    ("controllerdata.lacity.org", "pggv-e4fn", "Checkbook L.A. Data", [("supplier_country", "country"), ("supplier_city", "city")]),
    ("data.brla.gov", "6w2f-pxr9", "City-Parish Vendors", [("vendor_state", "state")]),
    ("data.cityofchicago.org", "rsxa-ify5", "Contracts", [("state", "state"), ("address_1", "address"), ("city", "city")]),
    ("data.cityofchicago.org", "5wd9-d675", "List of Contractors Doing Business with the City Of Chi", [("state", "state"), ("city", "city")]),
    ("data.cityofchicago.org", "r5kz-chrr", "Business Licenses", [("state", "state"), ("city", "city")]),
    ("data.cityofnewyork.us", "da9u-wz3r", "Metal Content of Consumer Products Tested by the NYC He", [("purchase_country", "country"), ("made_in_country", "country")]),
    ("data.cityofnewyork.us", "dx8z-6nev", "Donations to Not-for-Profit Organizations Affiliated wi", [("donor_s_state_of_residence", "state")]),
    ("data.cityofnewyork.us", "dg92-zbpx", "City Record Online", [("vendor_address", "address")]),
    ("data.cityofnewyork.us", "qxzj-vkn2", "Campaign Expenditures", [("state", "state"), ("city", "city")]),
    ("data.colorado.gov", "66zf-qjdd", "City of Denver Procurement Transactions", [("merchant_state", "state")]),
    ("data.cityofchicago.org", "ypez-j3yg", "Lobbyist Data", [("lobbyist_country", "country"), ("employer_country", "country"), ("correspondent_country", "country"), ("client_address", "address")]),
    ("data.colorado.gov", "wnau-xrqi", "City of Denver Checkbook", [("state", "state")]),
    ("data.colorado.gov", "wwbh-7bpa", "Paid Solicitors Disclosed on Charity Registration Forms", [("state", "state"), ("city", "city")]),
    ("data.delaware.gov", "c6zw-7xr2", "I Can Help with Supplies During Coronavirus Response", [("primary_contact_state", "state")]),
    ("data.fultoncountyga.gov", "2jx8-2ffx", "Fulton County Vendors", [("state", "state"), ("city", "city")]),
    ("data.delaware.gov", "h9bb-iyu6", "Awarded Vendor Contact Info", [("state", "state"), ("city", "city")]),
    ("data.kingcounty.gov", "i6sy-ckp7", "Lead Content of Consumer Products tested in King County", [("made_in_country", "country")]),
    ("data.lacity.org", "5mrt-4zhe", "City Campaign Expenditures", [("payee_addr_st", "state"), ("payee_addr_cty", "address")]),
    ("data.mo.gov", "kf27-upwz", "Motor Fuel Licensee List", [("state", "state"), ("city", "city")]),
    ("data.mo.gov", "utxx-8sht", "Asbestos Courtesy Notifications", [("address", "address")]),
    ("data.ny.gov", "7xzk-zyk5", "NYSERDA Supported Clean Energy Research and Development", [("contractor_state_province", "state")]),
    ("data.ny.gov", "8bmh-tuz3", "Lobbying Clients Disclosures: Four Biannual Period Wind", [("client_state", "state")]),
    ("data.ny.gov", "8pp4-isha", "New York State Child Support Warrants: Beginning 7/1/20", [("state", "state"), ("city", "city"), ("debtor_address", "address")]),
    ("data.ny.gov", "c6c2-n3if", "State University Construction Fund (SUCF) Request for Q", [("state", "state"), ("city", "city")]),
    ("data.ny.gov", "d84c-dk28", "Procurement Report for Local Development Corporations", [("vendor_province_region", "state"), ("vendor_country", "country")]),
    ("data.ny.gov", "dprp-55ye", "Large-scale Renewable Projects Reported by NYSERDA: Beg", [("county_province", "state"), ("state_province", "state")])
]

def fetch_data(domain, dataset_id, cols):
    print(f"Fetching {domain}/{dataset_id}")
    where_clauses = []
    for col_info in cols:
        col = col_info[0]
        kind = col_info[1]
        c = f"upper(`{col}`)"
        if kind == "country":
            where_clauses.append(f"({c} in ('CA','CAN','CANADA','CDN') OR {c} like '%CANADA%')")
        elif kind == "state":
            proclist = ','.join(f"'{p}'" for p in PROVS)
            where_clauses.append(f"({c} in ({proclist}) OR {c} like '%CANADA%')")
        elif kind in ("city", "address"):
            where_clauses.append(f"({c} like '%CANADA%')")

    if not where_clauses:
        return []

    where_str = " OR ".join(where_clauses)
    params = urllib.parse.urlencode({
        "$where": where_str,
        "$limit": 50000
    })

    url = f"https://{domain}/resource/{dataset_id}.json?{params}"
    req = urllib.request.Request(url, headers={"User-Agent": "contracts-research/1.0"})
    try:
        resp = urllib.request.urlopen(req, timeout=30)
        return json.loads(resp.read().decode('utf-8'))
    except Exception as e:
        print(f"Error fetching {domain}/{dataset_id}: {e}")
        return []

def process_hits():
    datasets_to_process = []
    for d in DATASETS:
        datasets_to_process.append({
            "domain": d[0],
            "id": d[1],
            "name": d[2],
            "cols": d[3]
        })

    if not os.path.exists(os.path.dirname(OUT_FILE)):
        os.makedirs(os.path.dirname(OUT_FILE))

    print(f"Found {len(datasets_to_process)} datasets")
    with gzip.open(OUT_FILE, "wt", encoding="utf-8") as out:
        for ds in datasets_to_process:
            records = fetch_data(ds["domain"], ds["id"], ds["cols"])
            print(f"Got {len(records)} records")
            for i, row in enumerate(records):
                vendor_name = None
                # Try finding a name column
                for k, v in row.items():
                    k_low = k.lower()
                    if 'vendor' in k_low or 'supplier' in k_low or 'payee' in k_low or 'contractor' in k_low or 'merchant' in k_low or 'company' in k_low or 'business' in k_low:
                        if 'name' in k_low or k_low in ['vendor', 'supplier', 'payee', 'contractor', 'merchant']:
                            vendor_name = v
                            break

                if not vendor_name or PLACEHOLDER.search(str(vendor_name)):
                    vendor_name = "Missing Vendor Name"

                basis = ""
                for col_info in ds["cols"]:
                    col = col_info[0]
                    if col in row and row[col]:
                        basis = f"{col}={row[col]}"
                        break

                amt = None
                date = None
                for k, v in row.items():
                    k_low = k.lower()
                    if 'amount' in k_low or 'cost' in k_low or 'price' in k_low or 'total' in k_low or 'value' in k_low or 'spend' in k_low or 'payment' in k_low:
                        try:
                            amt = float(str(v).replace('$', '').replace(',', ''))
                        except:
                            pass
                    if 'date' in k_low and v:
                        date = str(v)[:10]
                        if len(date) == 10 and date.startswith("20") and re.match(r"^\d{4}-\d{2}-\d{2}$", date):
                            pass
                        else:
                            date = None

                record_id = f"{ds['domain']}_{ds['id']}_{i}"
                if 'id' in row:
                    record_id = f"{ds['domain']}_{ds['id']}_{row['id']}"

                rec = {
                    "record_id": f"us_socrata_sweep_continue:{record_id}",
                    "source": {
                        "key": "us_socrata_sweep_continue",
                        "name": f"{ds['domain']} - {ds['name']}",
                        "publisher": ds['domain'],
                        "dataset_url": f"https://{ds['domain']}/d/{ds['id']}",
                        "record_url": f"https://{ds['domain']}/resource/{ds['id']}.json",
                        "retrieved_at": datetime.datetime.now(datetime.timezone.utc).isoformat()
                    },
                    "status": "end_date_unknown",
                    "status_basis": "Socrata general dump, no explicit end date verified.",
                    "contract": {
                        "identifiers": {},
                        "value": amt,
                        "currency": "USD",
                        "dates": {
                            "start": date
                        }
                    },
                    "buyer": {
                        "name": ds['domain'],
                        "country": "US",
                        "type": "city/state/county",
                    },
                    "vendor": {
                        "name": str(vendor_name),
                        "country": "CA",
                        "country_basis": basis if basis else "Socrata sweep logic",
                        "address": {
                            "country": "CA"
                        }
                    },
                    "link": f"https://{ds['domain']}/d/{ds['id']}",
                    "link_type": "dataset",
                    "raw": row
                }
                out.write(json.dumps(rec, ensure_ascii=False) + "\n")

if __name__ == '__main__':
    process_hits()
