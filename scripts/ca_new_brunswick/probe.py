import requests, re, sys, html
s = requests.Session(); s.headers["User-Agent"] = "contracts-research/1.0"
r = s.get("https://nbon-rpanb.gnb.ca/welcome", timeout=40)
sid = re.search(r'id="sessionId" value="(\d+)"', r.text).group(1)
print("session", sid, r.status_code, s.cookies.get_dict())
for p in ["showWelcomeLinks", "showWelcomeContent", "showHeader"]:
    rr = s.get(f"https://nbon-rpanb.gnb.ca/{p}?sessionID={sid}&language=En&welcomeAccessLink=&cssStyle=ext/", timeout=40)
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", rr.text, flags=re.S)
    print("==", p, rr.status_code, rr.url, len(rr.text))
    for m in re.findall(r'(?:href|onclick|onClick)="([^"]+)"[^>]*>(.{0,120}?)<', t, re.S):
        print("  ", m[0][:220], "|", re.sub(r"\s+", " ", m[1]).strip()[:80])
    print(re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t)))[:800])
