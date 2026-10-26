# igo_portals — international organisations' own award portals: index of what was checked

Reference date 2026-10-25. Probe script `scripts/igo_portals/probe_urls.py` (results `downloads/igo_portals/probe/probe_results.json` — 137 URLs, 2026-10-25 17:23–17:57 UTC; and `downloads/igo_portals/probe2/probe_results.json` — 20 URLs, 19:3x UTC). De-duplication baseline: `downloads/igo_portals/ungm_index.json` (287 UNGM Canadian awards by agency/ref/vendor, built from `normalized/ungm.jsonl`).

## Produced records
| key | records | note |
|---|---|---|
| who | 816 (end_date_unknown) | notes/who.md — PDF "Supplier Country" column, verified |
| undp | 51 (end_date_unknown) | notes/undp.md — "Country of Contractor" field |
| fao | 12 (11 end_date_unknown, 1 ongoing_inferred) | notes/fao.md — "Vendor Country" column |
| cdb | 7 (2 ongoing_inferred, 5 end_date_unknown) | notes/cdb.md — "Winning Bid: Canada - firm"; dates from linked award notices |

## Checked and rejected / blocked (status on 2026-10-25)
- **Cloudflare/WAF challenge (not bypassed):** ICAO, NSPA, NCIA, AfDB, ADB data portal, IAEA, UNHCR, IFAD, UNRWA, UNIDO, OECD, OAS, UN Secretariat PD (AWS WAF 202 challenge). Akamai "Access Denied": IOM, IMF.
- **No supplier country in published award list:** UNICEF (monthly PDFs), Commonwealth Secretariat (quarterly PDFs). WIPO awards page (200) and Interpol "Awarded contracts" page (200) list no Canadian suppliers / no country column (0 "Canad" hits).
- **No award list found (404 or info page only):** WFP, UNFPA, ILO, UNESCO (only EU-grant PDF), UN Women, UNEP, WMO, PAHO, ITU, EIB (TED-covered), NDB, IsDB, NIB, CEB, IFC, GCF, Gavi, GEF, CERN (eProcurement portal 200 but no awarded list), ITER, EUMETSAT, EMBL, ESO, OPCW, ICC, APEC, NATO HQ, ESA (SPA shell), AIIB (project procurement only), UNOPS own site (awards are on UNGM, 126 covered).
- **Covered elsewhere:** UNGM aggregates UNOPS, ICAO, IAEA, UNESCO, UNFPA, UN Secretariat, UNICEF, ILO, WMO, UNIDO … (`ungm`); World Bank (`worldbank`); IDB, EBRD (`other_igo`).
- **Also checked 19:5x UTC (probe3):** OSCE (TLS certificate failure via proxy), AIIB contract-awards (404 page), CARICOM procurement (agent page only), African Union bids (tenders only), IICA (Cloudflare 403), CGIAR (redirect, no awards), UNFCCC (empty), GCF (wrong domain/404) — 0 'Canad' hits.
Individual short notes: unicef, unops, un_secretariat, wfp, icao, nato_nspa, nato_ncia, esa, afdb, eib, adb, commonwealth.
