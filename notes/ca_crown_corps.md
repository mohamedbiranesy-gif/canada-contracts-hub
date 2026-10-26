# ca_crown_corps — Provincial Crown corporations checked for their own award disclosures (REJECTED / covered elsewhere)

Checked 2026-10-25 18:27 UTC with `contracts-research/1.0`:
- **BC Hydro, ICBC, WorkSafeBC**: no own award listing; their competitive awards are posted on BC Bid. BC Bid itself is reCAPTCHA-gated (`notes/ca_bc_bid.md`), but the Province's open-data "Ministry Contract Awards" extract (`ca_bc_ministry_awards`) covers BC Bid contract award summaries; Crown-corp postings appear there only when they chose to publish a summary.
- **SaskPower**: procurement page 404; SaskPower awards are published on SaskTenders (covered in `ca_saskatchewan`, buyer name "SaskPower").
- **Manitoba Hydro** (`hydro.mb.ca/suppliers/`): supplier guides only, no award disclosure; its tenders/awards are on MERX (parallel `ca_merx` worker).
- **Ontario Power Generation** (`opg.com/suppliers/`): HTTP 403 Cloudflare "Attention Required"; not bypassed. **Hydro One**: supplier pages 404/relocated; no award register found. **Metrolinx**: publishes a procurement pipeline and tenders (via MERX/Ontario Tenders Portal) but no contract-award list with supplier addresses.
- **NB Power**: supplier page 404; NB Power awards are on NBON (blocked, `notes/ca_new_brunswick.md`).
- **NL Hydro / Nalcor, NLC, OilCo, Bull Arm**: their awards are included in the NL PPA semi-monthly Contract Awards Reports (`ca_newfoundland`).
- **Provincial lotteries (BCLC, OLG, ALC, WCLC, SLGA)**: not checked individually; BCLC posts on BC Bid, OLG on Ontario Tenders Portal/MERX.

Result: no separate Crown-corporation source key produced.
