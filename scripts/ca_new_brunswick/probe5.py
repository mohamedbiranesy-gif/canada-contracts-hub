import requests, re, sys, html
s = requests.Session(); s.headers["User-Agent"] = "contracts-research/1.0"
B = "https://nbon-rpanb.gnb.ca/"
r = s.get(B + "welcome", timeout=40)
sid = re.search(r'id="sessionId" value="(\d+)"', r.text).group(1)
s.get(B + f"submitLogin?sessionID={sid}&User_Name=Anonymous&Language=En&cssStyle=ext/&validate_method=OPEN", timeout=40)
rr = s.get(B + f"showDisplayDocument?sessionID={sid}&disID={sys.argv[1]}&doc_search_by=Tend", timeout=60)
open(f"downloads/ca_new_brunswick/doc_{sys.argv[1]}.html", "w").write(rr.text)
t = re.sub(r"<script.*?</script>|<style.*?</style>", "", rr.text, flags=re.S)
tx = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " | ", t))); tx = re.sub(r"(\|\s*)+", "| ", tx)
print(rr.status_code, len(rr.text)); print(tx[:5000])
