import json, os, re, collections, glob
B = "."; D = B + "/downloads/ch_simap"
R = [json.loads(l) for l in open(B + "/normalized/ch_simap.jsonl")] if os.path.exists(B + "/normalized/ch_simap.jsonl") else []
months = {}
for l in open(D + "/crawl.log"):
    m = re.search(r"(\S+) month (\S+) awards=(\d+) canada=(\d+)", l)
    if m: months[m.group(2)] = (m.group(1), int(m.group(3)), int(m.group(4)))
done = sorted(months)
allm = ["%d-%02d" % (y, mo) for y in (2024, 2025, 2026) for mo in range(1, 13) if "%d-%02d" % (y, mo) <= "2026-10"]
missing = [m for m in allm if m not in months]
st = json.load(open(D + "/normalize_stats.json")) if os.path.exists(D + "/normalize_stats.json") else {}
L = ["# ch_simap — simap.ch (Switzerland) award publications, vendor address in Canada\n",
     "Reference date 2026-10-25. Output `normalized/ch_simap.jsonl`: **%d records** %s.\n" % (len(R), dict(collections.Counter(r["status"] for r in R))),
     "## What was downloaded",
     "Public API of the new simap.ch (OpenAPI spec https://www.simap.ch/api/specifications/simap.yaml, Swagger UI https://www.simap.ch/api-doc/). Listing: `GET https://www.simap.ch/api/publications/v2/project/project-search?newestPubTypes=award_tender&newestPubTypes=award_study_contract&newestPubTypes=award_competition&newestPublicationFrom=<month start>&newestPublicationUntil=<month end>[&lastItem=<cursor>]` (20 per page). Detail of every listed award: `GET https://www.simap.ch/api/publications/v1/project/<projectId>/publication-details/<publicationId>`. For matches only, the referenced tender publication (`referencingPub`) is fetched the same way (cache `downloads/ch_simap/ref_cache/`). Crawler `scripts/ch_simap/crawl.py` (3 workers on disjoint months, ≈3 req/s total), started 2026-10-25 19:49 UTC; listing of every award seen `downloads/ch_simap/listing.jsonl`; matches (full JSON) `downloads/ch_simap/matches.jsonl`; per-month log `downloads/ch_simap/crawl.log`. **Direct awards (`direct_award`, freihändige Vergabe) were not crawled** (volume/time; a first test run included them).",
     "\nMonths completed (award publications seen / with Canadian vendor):\n",
     "| month | finished (UTC) | awards | Canadian |\n|---|---|---|---|"]
for m in sorted(months, reverse=True):
    t, a, c = months[m]; L.append("| %s | %s | %d | %d |" % (m, t, a, c))
L += ["\nTotal awards examined: %d. **Months not completed in the time box: %s.**" % (sum(v[1] for v in months.values()), ", ".join(missing) if missing else "none"),
      "\n## Canadian vendor",
      "`decision.vendors[].vendorAddress.countryId` = `CA` (structured ISO code; street, city, postal code kept in `vendor.address`). Names never used.",
      "\n## Ongoing",
      "Award publications carry only `decision.awardDecisionDate`; contract periods are, at best, in the referenced tender publication (`procurement.contractDeadlineType`/`executionDeadlineType` and period/duration fields). `scripts/ch_simap/normalize.py` reads any period start/end found there; when none is given (typically `not_specified`) the record is `end_date_unknown` with the award decision date as anchor.",
      "\nnormalize stats: `%s`" % json.dumps(st),
      "\n## record_url",
      "`https://www.simap.ch/en/project-detail/<projectId>#<publicationId>` — verified for project c2262a97-8ba9-4579-a65b-96456ff95b3a (HTTP 200, single-page app). API detail URL is reproducible from `contract.identifiers`.",
      "\n## Records"]
for r in R:
    c = r["contract"]
    L.append("- `%s` | %s (%s) | %s | %s | %s %s | award %s | %s" % (r["record_id"], r["vendor"]["name"], r["vendor"]["address"].get("city"), r["buyer"]["name"], (c["title"] or "")[:80], c["currency"], c["value"], c["dates"].get("award"), r["status"]))
L += ["\n## Known gaps", "- Direct awards and months listed as not completed are missing.", "- Publications from the old simap (pre-2024 platform) that were migrated as 'external' may lack vendor addresses.", "- Above-threshold Swiss awards are not in TED (CH is not EU); `ch_opentender` (TED-derived) is a different, older population."]
tmp = B + "/notes/.ch_simap.md.tmp"; open(tmp, "w").write("\n".join(L) + "\n"); os.replace(tmp, B + "/notes/ch_simap.md"); print(len(R), len(months))
