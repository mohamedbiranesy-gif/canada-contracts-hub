import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request("https://sosa.canadabuys.canada.ca/cds/opendata/tpsgc-pwgsc_ocama-sosa.csv")
req.add_header("User-Agent", "Mozilla/5.0")
with urllib.request.urlopen(req, context=ctx) as f:
    print(f.read(100).decode("utf-8"))
