"""print groups whose label/names match a regex: rank gid records n_keys label website"""
import sys, os, json, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
G = json.load(open(WORK + '/groups.json'))
rx = re.compile(sys.argv[1], re.I)
for g in G:
    if rx.search(g['label']) or any(rx.search(n) for n in g['names']) or rx.search(norm(g['label'])):
        print(g['rank'], g['gid'], g['records'], g['n_keys'], '|', g['label'][:80], '|', g['website'], '|', g['source'])
