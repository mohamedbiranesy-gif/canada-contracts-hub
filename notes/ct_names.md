# ct_names — site names from the Certificate Transparency logs

Engine: `tools/ct_names.py`, workflow `.github/workflows/ct-names.yml` (cloud only). Decision and reading budget: `coord/DECISIONS.md`
2026-11-11 05:35Z. This is not a contract source: it brings **names of sites to look at**; nothing is delivered from a name alone.

## What it reads
The *names tiles* of the static CT logs that publish them — one gzip file of JSON lines per 256 certificates, about 6.5 KB:

    <monitoring prefix>/tile/names/x004/x000/000
    {"Timestamp":1794079951147,"Subject":{"CommonName":"example.ca"},"DNS":["example.ca","www.example.ca"]}

Tile number → path: the number in groups of three digits, every group but the last prefixed with `x` (`1234067` → `x001/x234/067`).
Only full tiles are read (`tree size // 256`, second line of `<prefix>/checkpoint`). The list of logs is Google's
`https://www.gstatic.com/ct/log_list/v3/log_list.json` (`tiled_logs`).

| log (2026-11-11) | names tiles | certificates | read |
|---|---|---|---|
| Let's Encrypt Sycamore 2027h1 / 2026h2 | yes | 1.14 G / 1.10 G | all / newest 40 % |
| Let's Encrypt Willow 2027h1 / 2026h2 | yes | 1.09 G / 1.05 G | all / newest 40 % |
| Geomys Tuscolo 2027h1 / 2026h2 | yes | 571 M / 1.05 G | all / newest 40 % |
| Geomys Trastevere 2027h1 / 2026h2 | yes | 45 M / 32 M | all / newest 40 % |
| IPng Gouda 2027h1 / 2026h2 | yes (not for its first tiles) | 381 M / 1.25 G | all / newest 40 % |
| IPng Halloumi | no (404) | 451 M / 1.30 G | — |
| Google ParcelYard, PlumbersArms | no (404) | 730 M / 1.65 G each | — |
| Sectigo, GoDaddy, TrustAsia, Microsec, HARICA static logs | not tried (only "qualified", small) | | — |

Which logs hold a certificate (final certificates found in four logs, 2026-11-11): Let's Encrypt, Google Trust Services, ZeroSSL and
Sectigo give each certificate one SCT of an RFC 6962 log (Argon, Xenon, Nimbus, Wyvern, Sphinx, Elephant, Tiger) and one of a static log
among Sycamore, Willow, Tuscolo, Halloumi, Gouda. GoDaddy, DigiCert, Amazon and Microsoft use RFC 6962 logs only: **not seen here**.

## Budget (all runners of a run together)
Let's Encrypt 90 requests/s per log service (Sycamore, Willow), Geomys 30, IPng 20; halved for the rest of the run after any 429 / 503;
a direction of a log stops at the first tile that cannot be had. Identified user agent. Three runners by default (the budget is divided).
Measured from one runner-like machine: the limits bind (2,704 tiles per Let's Encrypt service in 90 s at 30/s), 2.4 ms of CPU a tile.

## What comes out
- `data/incoming/claude/credit_scan/ctca_<stamp>.gz` — `.ca` registrable domains no list on file has (one per line). The home-page scan
  (`credit_scan.scan_queue`, priority 4) and the DNS lookups (`dns_services.queue`) read them. First measure: of 6,233 `.ca` names in
  1.9 M certificates, 2,833 (45 %) were new.
- release `harvest-state`: `ct_list_<stamp>.txt.gz` — names on the store sweep's endings (com net org co us shop store), each name
  once, in the web graph's line format (`0<TAB>com.example`); `ct_xlist_<stamp>.txt.gz` — 27 other endings shops use, kept for later;
  `ct_seen.bloom.zst` — the Bloom filter of the names listed (2^31 bits, 6 hashes; started with the web graph's 63 M names).
  `dns-services` mode `ctsweep` (`dns_services.py sweep --list auto`) asks each list once: address on Shopify's storefront network? name
  servers of a watched Canadian provider? Places per list under `ct` in `credit_scan/sweep_cursor.json`.
- `data/incoming/claude/ct_names/ov_ca_<stamp>.jsonl.gz` — subjects a certificate authority validated, country CA
  (`{"s": {"Organization": […], "Locality": […], "Province": […], …}, "d": [domains], "log": …, "tile": …}`). Not used yet (the subject
  is the certificate's subscriber, which can be a host or CDN covering customers' names).
- `data/incoming/claude/ct_names/cursor.json` — per log: `lo`, `hi` (tiles `[lo, hi)` are read), `floor`, `top`; the lists published;
  `tiles_left`.

## Counts
| run | tiles / certificates | `.ca` names | names on the sweep's endings | other endings | validated subjects (C=CA) |
|---|---|---|---|---|---|
| 42966486771 (test, 2026-11-11 05:40Z) | 45,000 / 11.52 M | 19,534 seen, **8,123 new (42 %)** | 1,095,327 seen, **657,286 new (60 %)** | 76,216 new | 175 |

Sweep of the list `ct_list_20261111T060239.txt.gz` (runs 42974942196 and 42976120689, complete 07:26Z): 657,286 names asked,
**47,751 on Shopify's storefront addresses (7.3 %)**, 1,087 with the name servers of a watched Canadian provider, 166 without an answer.
