"""Print links (href + anchor) on already-probed pages matching a keyword regex. usage: links.py <url> <regex>"""
import sys, os, json, re, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
from bs4 import BeautifulSoup
P = [json.loads(l) for l in open(WORK + '/probe_log.jsonl')]
p = [x for x in P if x['url'] == sys.argv[1] and x.get('saved')][-1]
h = open(BASE + '/' + p['saved'], 'rb').read().decode('utf-8', 'replace')
for a in BeautifulSoup(h, 'lxml').find_all('a', href=True):
    t = a.get_text(' ', strip=True)
    if re.search(sys.argv[2], t + ' ' + a['href'], re.I):
        print(urllib.parse.urljoin(p['final_url'], a['href']), '|', t[:100])
