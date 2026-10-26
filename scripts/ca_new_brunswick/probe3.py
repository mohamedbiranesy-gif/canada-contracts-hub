import requests, re, sys, html, json
s = requests.Session(); s.headers["User-Agent"] = "contracts-research/1.0"
B = "https://nbon-rpanb.gnb.ca/"
r = s.get(B + "welcome", timeout=40)
sid = re.search(r'id="sessionId" value="(\d+)"', r.text).group(1)
s.get(B + f"submitLogin?sessionID={sid}&User_Name=Anonymous&Language=En&cssStyle=ext/&validate_method=OPEN", timeout=40)
rr = s.get(B + f"showBidResults?sessionID={sid}&fillDates=yes&searchType=Tender&menuName=ExtBrowseBidResultsTender", timeout=60)
open("downloads/ca_new_brunswick/showBidResults.html", "w").write(rr.text)
t = rr.text
print(rr.status_code, len(t))
for m in re.finditer(r"<form[^>]*>", t): print("FORM", m.group(0)[:300])
for m in re.finditer(r"<(input|select)[^>]*>", t):
    g = m.group(0)
    if 'hidden' in g or 'text' in g or 'select' in g or 'radio' in g: print("  ", g[:250])
for m in re.findall(r"<option[^>]*value=\"([^\"]*)\"[^>]*>([^<]{0,60})", t)[:60]: print("    opt", m)
js = re.findall(r"function\s+(\w+)\s*\(", t); print("functions", js[:30])
for m in re.findall(r"(submit\w+\?[^'\"]{0,200})", t)[:20]: print("  submit:", m)
print(re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"<script.*?</script>|<style.*?</style>", "", t, flags=re.S))))[:1500])
