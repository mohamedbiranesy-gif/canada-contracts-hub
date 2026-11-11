# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 99292 | 210 |
| v=DMARC1; p=none (monitor only) | 92616 | 554 |
| p=quarantine | 30685 | 566 |
| p=reject | 15179 | 578 |
| invalid DMARC record | 181 | 1 |
| lookup error | 996 | 2 |
| not checked | 1595 | 6 |

Rows without enforcement (no record / p=none / invalid): **192089**

## By package (no record / p=none / quarantine / reject)
- P01: 25 / 180 / 205 / 215
- P01M: 26 / 23 / 29 / 25
- P01T: 56 / 115 / 116 / 78
- P02: 57 / 173 / 139 / 100
- P03: 2 / 59 / 84 / 112
- P04: 752 / 1466 / 938 / 621
- P05: 53 / 142 / 131 / 97
- P06: 21 / 88 / 81 / 106
- P06M: 4145 / 3595 / 1760 / 878
- P06T: 25438 / 27626 / 8696 / 3706
- P07: 186 / 286 / 181 / 141
- P08: 8082 / 10461 / 4423 / 2368
- P09: 56 / 96 / 99 / 42
- P10: 625 / 1006 / 575 / 444
- P10R: 47775 / 34682 / 9735 / 4391
- P11: 3701 / 6683 / 1208 / 742
- P12: 2 / 4 / 0 / 1
- P13: 8290 / 5931 / 2285 / 1112
