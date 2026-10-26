# tw_pcc — Taiwan Government e-Procurement System (政府電子採購網), award notices with Canadian winning bidders

Reference date 2026-10-25. Output `/home/claude/contracts/normalized/tw_pcc.jsonl`: **5 records, all `ongoing`**. (Earlier partial run had produced 3; re-run 2026-10-25 19:20 UTC after the download finished.)

## What was downloaded
- Daily award open-data XML `https://web.pcc.gov.tw/tps/tp/OpenData/downloadFile?fileName=award_YYYYMMDD.xml` — file list `downloads/tw_pcc/award_files.txt` (274 files, award_20150401 … award_20260802; twice-monthly), saved to `downloads/tw_pcc/award/` (85 MB). Script `scripts/tw_pcc/download.sh`, log `downloads/tw_pcc/download.log` (2026-10-25 18:24–18:48 UTC).
- GPA award JSON `…downloadFile?fileName=GPAaward_YYYYMMDD.json` — 51 files (`gpa_files.txt`), `downloads/tw_pcc/gpa/` (100 MB).
- Full award-notice detail for each candidate through the open mirror API `https://pcc-api.openfun.app/api/searchbytitle?query=<case no>` → `https://pcc-api.openfun.app/api/tender?unit_id=<unit>&job_number=<case no>` (cached in `downloads/tw_pcc/api_cache/`).

## Canadian vendor
Stage 1 (candidate) = bidder address `BIDDER_SUPP_ADDR` (XML) / `得標廠商地址清單` (GPA JSON) contains `canad`/`加拿大`, a Canadian province name or a Canadian postal code → 25 candidate cases. Stage 2 (decisive, structured) = award notice field `投標廠商N:得標廠商國別` (winning supplier country) contains `加拿大`/`Canada` **and** `投標廠商N:是否得標` = 是 (won). 21 Canadian winning bidders. Names never used.

## Ongoing
`投標廠商N:履約起迄日期` (performance period, ROC calendar `113/12/19－115/12/19`, converted +1911): start ≤ 2026-10-25 ≤ end → `ongoing`; 16 excluded as ended; no end-date-less cases.

## record_url
`https://web.pcc.gov.tw/prkms/tender/common/noticeDate/redirectPublic?ds=<notice date>&fn=<notice filename>.xml` — verified 2026-10-25: `ds=20250203&fn=BDM-1-70796540.xml` → HTTP 200, redirects to `…/QueryAtmAwardDetailHist?fkPmsMainHist=…` page naming Angstrom and 加拿大.

## Samples
- tw_pcc:2.1:113000752:BDM-1-70796540:bidder1 | Angstrom Engineering Inc. | 中央研究院 (Academia Sinica) | multi-chamber sputtering & dry-etch system | TWD 42,604,394 | 2024-12-19 → 2026-12-19
- tw_pcc:3.13.50:MEB1450023:BDM-2-71142100:bidder2 | PIPECARE Inspection Services Inc. | 台灣中油 (CPC Corp.) | smart pigging inspection group F | 2026-03-26 → 2026-10-26
- tw_pcc:3.13.50:MEB1450025:BDM-2-71185822:bidder1 | PIPECARE Inspection Services Inc. | 台灣中油 | group G | 2026-05-25 → 2027-01-10
- tw_pcc:02717206:FS1120108-1-1:BDM-1-70791254:bidder1 | Best Theratronics LTD. | 國家原子能科技研究院 | 70 MeV cyclotron — 1st contract change | TWD 68,754,000 | → 2026-12-15
- tw_pcc:3.37.1:FS1120108-1:BDM-1-70251046:bidder1 | Best Theratronics LTD. | 行政院原子能委員會核能研究所 | 70 MeV cyclotron | TWD 696,931,700 | 2023-03-16 → 2026-12-15

## Gaps
- The two Best Theratronics records are the same cyclotron contract (original award + 1st contract-change notice; the buyer institute was renamed in 2023) — keep one when merging (case FS1120108-1).
- Candidate stage depends on the bidder address text; a Canadian winner whose address omits country/province/postal code would be missed. Amounts null where the notice gives none per bidder.
- Daily XML covers 2015-04 → 2026-08; awards published after 2026-08-02 not included.
- Raw daily XML/GPA JSON files were gzip-compressed on 2026-10-25 ~19:36 UTC to relieve a nearly full shared disk; to re-run `scripts/tw_pcc/pipeline.py`, gunzip `downloads/tw_pcc/award/*.xml.gz` and `downloads/tw_pcc/gpa/*.json.gz` first.
