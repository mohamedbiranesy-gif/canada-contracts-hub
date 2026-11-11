# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 53028 | 157 |
| v=DMARC1; p=none (monitor only) | 60203 | 536 |
| p=quarantine | 22437 | 544 |
| p=reject | 11496 | 564 |
| invalid DMARC record | 111 | 1 |
| lookup error | 27 | 0 |

Rows without enforcement (no record / p=none / invalid): **113342**

## By package (no record / p=none / quarantine / reject)
- P01: 25 / 180 / 206 / 215
- P01M: 28 / 36 / 36 / 32
- P01T: 52 / 116 / 105 / 61
- P02: 60 / 184 / 141 / 103
- P03: 2 / 63 / 87 / 112
- P04: 1042 / 1883 / 1061 / 702
- P05: 53 / 141 / 130 / 98
- P06: 19 / 87 / 78 / 110
- P06M: 5503 / 5139 / 2590 / 1282
- P06T: 23340 / 25643 / 8043 / 3598
- P07: 181 / 276 / 174 / 142
- P08: 8084 / 10273 / 4399 / 2354
- P09: 57 / 96 / 101 / 42
- P10: 888 / 1427 / 796 / 547
- P11: 367 / 607 / 278 / 208
- P12: 4 / 8 / 2 / 1
- P13: 13323 / 14044 / 4210 / 1889
