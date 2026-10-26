"""Shared extraction helpers for press releases."""
import re, datetime
MONTHS = {m:i for i,m in enumerate(["january","february","march","april","may","june","july","august","september","october","november","december"],1)}
MON_ABBR = {"jan":1,"feb":2,"mar":3,"apr":4,"may":5,"jun":6,"jul":7,"aug":8,"sep":9,"sept":9,"oct":10,"nov":11,"dec":12}
CA_CITY = re.compile(r"\b(TORONTO|MONTR[EÉ]AL|VANCOUVER|CALGARY|OTTAWA|EDMONTON|WINNIPEG|HALIFAX|QU[EÉ]BEC(?: CITY)?|MISSISSAUGA|WATERLOO|KITCHENER|HAMILTON|SASKATOON|REGINA|VICTORIA|BURNABY|RICHMOND|KELOWNA|MARKHAM|OAKVILLE|BURLINGTON|LAVAL|LONGUEUIL|BOUCHERVILLE|SHERBROOKE|TROIS-RIVI[EÈ]RES|GATINEAU|ST\.? JOHN'S|FREDERICTON|MONCTON|SAINT JOHN|CHARLOTTETOWN|WHITEHORSE|YELLOWKNIFE|IQALUIT|GUELPH|BRAMPTON|VAUGHAN|THORNHILL|RICHMOND HILL|CAMBRIDGE|BARRIE|KINGSTON|SUDBURY|GREATER SUDBURY|THUNDER BAY|LETHBRIDGE|RED DEER|ABBOTSFORD|SURREY|NANAIMO|KAMLOOPS|SQUAMISH|NORTH VANCOUVER|DELTA|LANGLEY|COQUITLAM|ST\.? CATHARINES|NIAGARA FALLS|WINDSOR|SARNIA|PETERBOROUGH|BELLEVILLE|CORNWALL|ORILLIA|TERREBONNE|MIRABEL|SAINT-LAURENT|DORVAL|POINTE-CLAIRE|BROSSARD|ERIN|CORNER BROOK|SAINT-EUSTACHE|SAINT-HUBERT|BLAINVILLE|GRANBY|DRUMMONDVILLE|SAINT-JEAN-SUR-RICHELIEU|L[EÉ]VIS|SAGUENAY|RIMOUSKI|ROUYN-NORANDA|VAL-D'OR|SEPT-[IÎ]LES|OSHAWA|WHITBY|AJAX|PICKERING|NEWMARKET|AURORA|CONCORD|WOODBRIDGE|BOLTON|MILTON|STONEY CREEK|BRANTFORD|WOODSTOCK|STRATFORD|OWEN SOUND|COLLINGWOOD|NORTH BAY|TIMMINS|SAULT STE\.? MARIE|KENORA|MEDICINE HAT|GRANDE PRAIRIE|FORT MCMURRAY|AIRDRIE|LEDUC|NISKU|SHERWOOD PARK|ST\.? ALBERT|PRINCE GEORGE|PRINCE RUPERT|PORT COQUITLAM|MAPLE RIDGE|CHILLIWACK|VERNON|PENTICTON|CRANBROOK|SIDNEY|DARTMOUTH|BEDFORD|SYDNEY|TRURO|LUNENBURG|DIEPPE|BATHURST|MIRAMICHI|MOUNT PEARL|GANDER|HAPPY VALLEY|BRANDON|STEINBACH|PRINCE ALBERT|MOOSE JAW|LLOYDMINSTER)\b", re.I)
CA_PROV = re.compile(r"\b(ON|QC|BC|AB|MB|SK|NS|NB|PE|PEI|NL|YT|NT|NU|Ontario|Qu[eé]bec|Quebec|British Columbia|Alberta|Manitoba|Saskatchewan|Nova Scotia|New Brunswick|Prince Edward Island|Newfoundland(?: and Labrador)?|Yukon|Northwest Territories|Nunavut|Canada)\b")
PROV_MAP = {"ON":"ON","ONTARIO":"ON","QC":"QC","QUEBEC":"QC","QUÉBEC":"QC","BC":"BC","BRITISH COLUMBIA":"BC","AB":"AB","ALBERTA":"AB","MB":"MB","MANITOBA":"MB","SK":"SK","SASKATCHEWAN":"SK","NS":"NS","NOVA SCOTIA":"NS","NB":"NB","NEW BRUNSWICK":"NB","PE":"PE","PEI":"PE","PRINCE EDWARD ISLAND":"PE","NL":"NL","NEWFOUNDLAND":"NL","NEWFOUNDLAND AND LABRADOR":"NL","YT":"YT","YUKON":"YT","NT":"NT","NORTHWEST TERRITORIES":"NT","NU":"NU","NUNAVUT":"NU"}
CITY_PROV_DEFAULT = {"TORONTO":"ON","OTTAWA":"ON","MISSISSAUGA":"ON","WATERLOO":"ON","KITCHENER":"ON","HAMILTON":"ON","MARKHAM":"ON","OAKVILLE":"ON","BURLINGTON":"ON","GUELPH":"ON","BRAMPTON":"ON","VAUGHAN":"ON","THORNHILL":"ON","RICHMOND HILL":"ON","BARRIE":"ON","SUDBURY":"ON","GREATER SUDBURY":"ON","THUNDER BAY":"ON","MONTREAL":"QC","MONTRÉAL":"QC","QUEBEC":"QC","QUÉBEC":"QC","QUEBEC CITY":"QC","LAVAL":"QC","LONGUEUIL":"QC","BOUCHERVILLE":"QC","SHERBROOKE":"QC","GATINEAU":"QC","TERREBONNE":"QC","MIRABEL":"QC","SAINT-LAURENT":"QC","DORVAL":"QC","POINTE-CLAIRE":"QC","BROSSARD":"QC","SAINT-EUSTACHE":"QC","VANCOUVER":"BC","BURNABY":"BC","KELOWNA":"BC","SQUAMISH":"BC","NORTH VANCOUVER":"BC","COQUITLAM":"BC","NANAIMO":"BC","KAMLOOPS":"BC","ABBOTSFORD":"BC","CALGARY":"AB","EDMONTON":"AB","LETHBRIDGE":"AB","RED DEER":"AB","WINNIPEG":"MB","SASKATOON":"SK","REGINA":"SK","HALIFAX":"NS","FREDERICTON":"NB","MONCTON":"NB","SAINT JOHN":"NB","CHARLOTTETOWN":"PE","ST. JOHN'S":"NL","ST JOHN'S":"NL","CORNER BROOK":"NL","WHITEHORSE":"YT","YELLOWKNIFE":"NT","IQALUIT":"NU"}
US_STATE = re.compile(r"\b(Calif\.|California|N\.Y\.|New York|Texas|Fla\.|Florida|Mass\.|Ill\.|Va\.|Md\.|Ariz\.|Colo\.|Ga\.|N\.J\.|Pa\.|Wash\.|Ohio|Mich\.|Minn\.|Wis\.|Nev\.|Ore\.|Conn\.|N\.C\.|S\.C\.|Tenn\.|Mo\.|Ind\.|Ky\.|La\.|Ala\.|Okla\.|Utah|Kan\.|Iowa|Neb\.|Ark\.|Miss\.|N\.H\.|Vt\.|Maine|R\.I\.|Del\.|D\.C\.|Idaho|Mont\.|Wyo\.|N\.D\.|S\.D\.|N\.M\.|Alaska|Hawaii|W\.Va\.)\b")
def parse_dateline(dl):
    """Return (location_str, date_iso) from Cision dateline '... CITY, PROV[ and CITY2] , Mon. D, YYYY /CNW/ -- ...'"""
    if not dl: return None, None
    m = re.search(r"(\w+\.?\s+\d{1,2},\s+\d{4})\s*/(?:CNW|PRNewswire|PRN|CNW Telbec)", dl)
    if not m:
        m2 = re.search(r"(\w+\.?\s+\d{1,2},\s+\d{4})", dl)
        return None, (parse_date(m2.group(1)) if m2 else None)
    d = parse_date(m.group(1))
    pre = dl[:m.start()].rstrip(" ,")
    # walk back over ALL-CAPS tokens / ', XX' province / 'and' joiners / lowercase country words like 'Australia'
    toks = pre.split()
    loc_toks = []
    i = len(toks)-1
    def is_loc_tok(t):
        core = t.strip(",.;:()")
        if not core: return False
        if core.lower() in ("and","&","de","du","la","le","des","of","the","in","national","homeland","red","river","métis"): return True
        if core.isupper(): return True
        if re.fullmatch(r"[A-Z][a-zé\-\.']+", core) and (core in ("Calif","Fla","Mass","Conn","Wis","Ill","Ariz","Colo","Ga","Pa","Va","Md","Wash","Mich","Minn","Nev","Ore","Tenn","Mo","Ind","Ky","La","Ala","Okla","Kan","Neb","Ark","Miss","Vt","Del","Mont","Wyo") or core in ("Australia","Germany","England","France","Japan","Korea","Denmark","Sweden","Norway","Finland","Netherlands","Belgium","Switzerland","Italy","Spain","Portugal","Ireland","Scotland","Wales","Mexico","Brazil","Chile","Peru","Colombia","Argentina","India","China","Singapore","Israel","Texas","Calif.","Fla.","Mass.","Conn.","Wis.","Ill.","Ariz.","Colo.","Ga.","N.Y.","N.J.","Pa.","Va.","Md.","Wash.","Ohio","Mich.","Minn.","Nev.","Ore.","N.C.","S.C.","Tenn.","Mo.","Ind.","Ky.","La.","Ala.","Okla.","Utah","Kan.","Iowa","Neb.","Ark.","Miss.","N.H.","Vt.","Maine","R.I.","Del.","D.C.","Idaho","Mont.","Wyo.","N.D.","S.D.","N.M.","Alaska","Hawaii","Ontario","Quebec","Québec","Alberta","Manitoba","Saskatchewan","Yukon","Nunavut","Canada","Kingdom","United","Emirates","Arab","Dhabi","Abu","Dubai","Hong","Kong","Taiwan","Vietnam","Thailand","Malaysia","Indonesia","Philippines","Zealand","New","South","North","West","East","Africa","Egypt","Kenya","Nigeria","Ghana","Morocco","Turkey","Poland","Czech","Austria","Hungary","Romania","Greece","Luxembourg","Iceland","Estonia","Latvia","Lithuania","Ukraine","Qatar","Saudi","Arabia","Bahrain","Kuwait","Oman","Jordan")): return True
        return False
    while i >= 0 and is_loc_tok(toks[i]):
        loc_toks.insert(0, toks[i]); i -= 1
    # strip leading ticker noise like 'NYSE: VZLA TSX: VZLA'
    while len(loc_toks) >= 2 and loc_toks[0].rstrip(":").isupper() and loc_toks[0].endswith(":"):
        loc_toks = loc_toks[2:]
    loc = " ".join(loc_toks).strip(" ,")
    # drop leading lowercase joiners accidentally captured
    loc = re.sub(r"^(?:and|the|of|in)\s+", "", loc, flags=re.I).strip(" ,")
    return (loc or None), d
def parse_date(s):
    if not s: return None
    s = s.strip()
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", s)
    if m: return m.group(0)
    m = re.search(r"([A-Za-z]+)\.?\s+(\d{1,2})(?:st|nd|rd|th)?,?\s+(\d{4})", s)
    if m:
        mon = m.group(1).lower(); mi = MONTHS.get(mon) or MON_ABBR.get(mon[:4]) or MON_ABBR.get(mon[:3])
        if mi:
            try: return datetime.date(int(m.group(3)), mi, int(m.group(2))).isoformat()
            except: return None
    m = re.search(r"(\d{1,2})\s+([A-Za-z]+)\.?\s+(\d{4})", s)
    if m:
        mon = m.group(2).lower(); mi = MONTHS.get(mon) or MON_ABBR.get(mon[:3])
        if mi:
            try: return datetime.date(int(m.group(3)), mi, int(m.group(1))).isoformat()
            except: return None
    return None
def location_is_canada(loc):
    if not loc: return False, None, None
    L = loc.upper()
    # take first segment before ' AND ' (multi-dateline) for vendor location
    first = re.split(r"\s+AND\s+|\s*;\s*|\s*/\s*", L)[0]
    if US_STATE.search(first): return False, None, None
    city = None; prov = None
    mc = CA_CITY.search(first)
    if mc: city = mc.group(1).upper()
    mp = re.search(r",\s*(ON|QC|BC|AB|MB|SK|NS|NB|PE|PEI|NL|YT|NT|NU|ONTARIO|QU[EÉ]BEC|BRITISH COLUMBIA|ALBERTA|MANITOBA|SASKATCHEWAN|NOVA SCOTIA|NEW BRUNSWICK|PRINCE EDWARD ISLAND|NEWFOUNDLAND(?: AND LABRADOR)?|YUKON|NORTHWEST TERRITORIES|NUNAVUT)\b", first)
    if mp: prov = PROV_MAP.get(mp.group(1).upper().replace("É","É"), None) or PROV_MAP.get(mp.group(1).upper())
    if not prov and city: prov = CITY_PROV_DEFAULT.get(city)
    if "CANADA" in first and not city:
        return True, None, prov
    ok = bool(prov) or bool(city and city in CITY_PROV_DEFAULT)
    # ambiguous cities (VICTORIA, RICHMOND, SURREY, DELTA, LANGLEY, CAMBRIDGE, KINGSTON, WINDSOR, LONDON) need province
    if city and city in ("VICTORIA","RICHMOND","SURREY","DELTA","LANGLEY","CAMBRIDGE","KINGSTON","WINDSOR","LONDON","SYDNEY","HAMILTON","WATERLOO","BURLINGTON","ERIN","CONCORD","AURORA","MILTON","CORNWALL","BEDFORD","NEWMARKET","WOODSTOCK","STRATFORD","BARRIE","VERNON","SIDNEY") and not mp:
        ok = city in ("HAMILTON","WATERLOO","BURLINGTON","BARRIE") and True  # these are commonly Canadian in CNW datelines
    return ok, (city.title() if city else None), prov
MONEY = re.compile(r"(?:(C\$|CA\$|CAD\s?\$?|US\$|USD\s?\$?|U\.S\.\s?\$|\$|€|EUR\s?|£|GBP\s?|A\$|AUD\s?|CHF\s?|NOK\s?|SEK\s?|DKK\s?)\s?)(\d{1,3}(?:[,\.]\d{3})*(?:\.\d+)?|\d+(?:\.\d+)?)\s*(billion|million|thousand|bn|mn|M|B|K)?\b", re.I)
def parse_money(text, limit=12):
    out=[]
    for m in MONEY.finditer(text):
        cur_raw = (m.group(1) or "").upper().replace(" ","")
        num = m.group(2).replace(",","")
        try: val = float(num)
        except: continue
        mult = (m.group(3) or "").lower()
        if mult in ("billion","bn","b"): val *= 1e9
        elif mult in ("million","mn","m"): val *= 1e6
        elif mult in ("thousand","k"): val *= 1e3
        cur = {"C$":"CAD","CA$":"CAD","CAD":"CAD","CAD$":"CAD","US$":"USD","USD":"USD","USD$":"USD","U.S.$":"USD","€":"EUR","EUR":"EUR","£":"GBP","GBP":"GBP","A$":"AUD","AUD":"AUD","CHF":"CHF","NOK":"NOK","SEK":"SEK","DKK":"DKK","$":"$"}.get(cur_raw, cur_raw)
        out.append({"text": m.group(0).strip(), "value": val, "currency": cur, "pos": m.start()})
        if len(out)>=limit: break
    return out
DUR = re.compile(r"\b(\d{1,2}|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|fifteen|twenty|twenty-five|thirty)[\s-]*(?:\(\d+\)\s*)?(year|yr|month)s?\b", re.I)
WORDNUM = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10,"eleven":11,"twelve":12,"fifteen":15,"twenty":20,"twenty-five":25,"thirty":30}
def parse_durations(text):
    out=[]
    for m in DUR.finditer(text):
        n = m.group(1).lower(); n = WORDNUM.get(n) or (int(n) if n.isdigit() else None)
        if not n: continue
        unit = m.group(2).lower()
        ctx = text[max(0,m.start()-60):m.end()+60].replace("\n"," ")
        out.append({"n": n, "unit": "year" if unit.startswith("y") else "month", "text": m.group(0), "context": ctx})
    return out
DATE_RX = re.compile(r"\b((?:January|February|March|April|May|June|July|August|September|October|November|December|Jan\.|Feb\.|Mar\.|Apr\.|Jun\.|Jul\.|Aug\.|Sept?\.|Oct\.|Nov\.|Dec\.)\s+\d{1,2},?\s+\d{4}|\d{1,2}\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}|\d{4}-\d{2}-\d{2})\b")
def find_dates(text):
    out=[]
    for m in DATE_RX.finditer(text):
        iso = parse_date(m.group(1))
        if iso: out.append({"text": m.group(1), "iso": iso, "context": text[max(0,m.start()-80):m.end()+40].replace("\n"," ")})
    return out
TICKER = re.compile(r"\((?:(TSX|TSXV|TSX-V|TSX Venture|CSE|NEO|Cboe CA|Cboe Canada|NYSE|NASDAQ|Nasdaq|NYSE American|OTCQX|OTCQB|OTC|FSE|FRA|ASX|LSE|AIM)\s*:\s*([A-Z0-9\.\-]{1,12}))", re.I)
def parse_tickers(text):
    seen=[]; 
    for m in TICKER.finditer(text[:6000]):
        t = f"{m.group(1).upper().replace('TSX-V','TSXV').replace('TSX VENTURE','TSXV')}:{m.group(2).upper()}"
        if t not in seen: seen.append(t)
    return seen
