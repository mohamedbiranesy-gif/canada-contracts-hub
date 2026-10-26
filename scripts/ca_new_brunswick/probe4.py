import requests, re, sys, html, json
s = requests.Session(); s.headers["User-Agent"] = "contracts-research/1.0"
B = "https://nbon-rpanb.gnb.ca/"
r = s.get(B + "welcome", timeout=40)
sid = re.search(r'id="sessionId" value="(\d+)"', r.text).group(1)
s.get(B + f"submitLogin?sessionID={sid}&User_Name=Anonymous&Language=En&cssStyle=ext/&validate_method=OPEN", timeout=40)
s.get(B + f"showBidResults?sessionID={sid}&fillDates=yes&searchType=Tender&menuName=ExtBrowseBidResultsTender", timeout=60)
data = {"sessionID": sid, "mode": "", "menuName": "ExtBrowseBidResultsTender", "searchResult": "True", "isChanged": "no", "language": "En",
        "isFirst": "Yes", "searchType": "Tender", "dllPage": "bid_results.html", "dllAnchor_pageLevel": "pageLevel",
        "results_type": "Awards", "docNum": "", "issuedForName": "", "issuedFor": "", "issuedByName": "", "issuedBy": "",
        "beg_date": sys.argv[1], "end_date": sys.argv[2]}
rr = s.post(B + "showBidResults", data=data, timeout=120)
open("downloads/ca_new_brunswick/bidresults_test.html", "w").write(rr.text)
t = rr.text
print(rr.status_code, len(t))
tx = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " | ", re.sub(r"<script.*?</script>|<style.*?</style>", "", t, flags=re.S))))
tx = re.sub(r"(\|\s*)+", "| ", tx)
print(tx[:4000])
for m in re.findall(r"(?:href|onclick|onClick)=\"([^\"]+)\"", t)[:30]: print("  link:", m[:250])
