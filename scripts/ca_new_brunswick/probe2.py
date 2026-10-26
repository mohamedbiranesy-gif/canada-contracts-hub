import requests, re, sys, html, json
s = requests.Session(); s.headers["User-Agent"] = "contracts-research/1.0"
B = "https://nbon-rpanb.gnb.ca/"
r = s.get(B + "welcome", timeout=40)
sid = re.search(r'id="sessionId" value="(\d+)"', r.text).group(1)
def show(p, n=1500, links=True):
    rr = s.get(B + p, timeout=60)
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", rr.text, flags=re.S)
    print("==", p[:120], rr.status_code, len(rr.text))
    if links:
        for m in re.findall(r'(?:href|onclick|onClick|action)="([^"]+)"[^>]*>(.{0,100}?)<', t, re.S):
            if 'css' in m[0] or 'Help' in m[0]: continue
            print("  ", m[0][:260], "|", re.sub(r"\s+", " ", m[1]).strip()[:70])
    print(re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t)))[:n])
    return rr.text
show(f"submitLogin?sessionID={sid}&User_Name=Anonymous&Language=En&cssStyle=ext/&validate_method=OPEN", 600)
show(f"showMainMenu?sessionID={sid}&language=En&cssStyle=ext/", 800)
show(f"showMainContent?sessionID={sid}&language=En&cssStyle=ext/&reload=no", 2000)
open("downloads/ca_new_brunswick/session.json","w").write(json.dumps({"sid": sid, "cookies": s.cookies.get_dict()}))
