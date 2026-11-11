# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 120520 | 229 |
| v=DMARC1; p=none (monitor only) | 116477 | 597 |
| p=quarantine | 36763 | 596 |
| p=reject | 18372 | 610 |
| invalid DMARC record | 230 | 1 |
| lookup error | 87 | 0 |

Rows without enforcement (no record / p=none / invalid): **237227**

## By package (no record / p=none / quarantine / reject)
- P01: 25 / 180 / 205 / 215
- P01M: 27 / 32 / 34 / 30
- P01T: 69 / 151 / 130 / 96
- P02: 58 / 184 / 142 / 102
- P03: 2 / 63 / 86 / 113
- P04: 837 / 1634 / 986 / 669
- P05: 53 / 139 / 130 / 98
- P06: 20 / 87 / 79 / 110
- P06M: 5093 / 4578 / 2380 / 1178
- P06T: 37485 / 40739 / 11904 / 5363
- P07: 185 / 280 / 178 / 144
- P08: 8186 / 10374 / 4445 / 2407
- P09: 56 / 95 / 99 / 42
- P10: 623 / 992 / 576 / 460
- P10R: 51774 / 37955 / 10903 / 4898
- P11: 7637 / 13279 / 2291 / 1341
- P12: 2 / 4 / 0 / 1
- P13: 8388 / 5711 / 2195 / 1105
