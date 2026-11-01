#!/usr/bin/env python3
import sys, json, os, urllib.request, urllib.parse
from datetime import datetime

REF_DATE = "2026-10-25"

def get_packages():
    url = "https://www.donneesquebec.ca/recherche/api/3/action/package_search?q=contrats&rows=1000"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    resp = urllib.request.urlopen(req).read()
    return json.loads(resp)["result"]["results"]

def process():
    packages = get_packages()
    buyers = ["Ville de Québec", "Ville de Laval", "Ville de Gatineau", "Ville de Longueuil"]
    # Check what organizations we actually find
    orgs = set([p["organization"]["title"] for p in packages if "organization" in p])
    print(f"Found organizations: {sorted(list(orgs))}")

if __name__ == "__main__":
    process()
