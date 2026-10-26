#!/usr/bin/env python3
"""Pull rows from a CKAN datastore via datastore_search_sql with a WHERE clause, paginated -> JSONL.
usage: python3 -I ckan_ds_pull.py <ckan_base> <resource_id> <out.jsonl> "<where clause>"
"""
import sys, json, time, urllib.parse, urllib.request

UA = "contracts-research/1.0"
PAGE = 1000


def main():
    base, rid, out, where = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    log = open(out + ".log", "a")
    log.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} START {base} {rid} where={where}\n"); log.flush()
    offset = 0
    with open(out, "w", encoding="utf-8") as fo:
        while True:
            sql = f'SELECT * FROM "{rid}" WHERE {where} ORDER BY "_id" LIMIT {PAGE} OFFSET {offset}'
            url = f"{base}/api/3/action/datastore_search_sql?sql=" + urllib.parse.quote(sql)
            for attempt in range(6):
                try:
                    req = urllib.request.Request(url, headers={"User-Agent": UA})
                    with urllib.request.urlopen(req, timeout=600) as r:
                        j = json.loads(r.read().decode("utf-8"))
                    break
                except Exception as e:
                    log.write(f"retry {attempt} {e}\n"); log.flush()
                    time.sleep(5 * (attempt + 1))
            else:
                raise SystemExit("failed")
            recs = j["result"]["records"]
            for rec in recs:
                fo.write(json.dumps(rec, ensure_ascii=False) + "\n")
            fo.flush()
            offset += len(recs)
            log.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} got {len(recs)} total {offset}\n"); log.flush()
            if len(recs) < PAGE:
                break
    log.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} DONE total={offset}\n"); log.close()


if __name__ == "__main__":
    main()
