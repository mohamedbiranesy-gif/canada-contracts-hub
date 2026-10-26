"""Print clean quotes around a regex from the saved copy of a probed URL (PDF via pdftotext in reading order, HTML via BeautifulSoup text).
usage: python3 -I quote.py URL REGEX [WIDTH]"""
import sys, os, json, re, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
from bs4 import BeautifulSoup
url, rx = sys.argv[1], re.compile(sys.argv[2], re.I)
w = int(sys.argv[3]) if len(sys.argv) > 3 else 220
pr = [json.loads(l) for l in open(WORK + '/probe_log.jsonl')]
pr = [p for p in pr if (p['url'] == url or p.get('final_url') == url) and p.get('saved')]
if not pr:
    sys.exit('not probed: ' + url)
p = BASE + '/' + pr[-1]['saved']
if p.endswith('.pdf'):
    t = subprocess.run(['pdftotext', p, '-'], capture_output=True, text=True).stdout
else:
    soup = BeautifulSoup(open(p, 'rb').read(), 'lxml')
    for x in soup(['script', 'style', 'noscript']):
        x.decompose()
    t = soup.get_text(' ', strip=True)
t = re.sub(r'\s+', ' ', t)
n = 0
for m in rx.finditer(t):
    print('>>', t[max(0, m.start() - w): m.end() + w])
    n += 1
    if n >= int(os.environ.get('MAXQ', '6')):
        break
print('retrieved_at', pr[-1]['retrieved_at'], 'matches', n)
