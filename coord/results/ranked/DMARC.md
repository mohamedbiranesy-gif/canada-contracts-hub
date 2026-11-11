# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 57952 | 160 |
| v=DMARC1; p=none (monitor only) | 60696 | 514 |
| p=quarantine | 22785 | 525 |
| p=reject | 11619 | 533 |
| invalid DMARC record | 124 | 1 |
| lookup error | 37 | 0 |

Rows without enforcement (no record / p=none / invalid): **118772**

## By package (no record / p=none / quarantine / reject)
- P01: 25 / 180 / 206 / 215
- P01M: 28 / 37 / 36 / 32
- P01T: 52 / 116 / 105 / 61
- P02: 60 / 184 / 141 / 103
- P03: 2 / 63 / 87 / 112
- P04: 1041 / 1879 / 1060 / 702
- P05: 53 / 141 / 130 / 98
- P06: 19 / 87 / 78 / 110
- P06M: 5755 / 5392 / 2659 / 1317
- P06T: 23340 / 25640 / 8043 / 3598
- P07: 180 / 274 / 172 / 142
- P08: 8046 / 10210 / 4379 / 2348
- P09: 57 / 96 / 101 / 42
- P10: 884 / 1420 / 793 / 546
- P11: 367 / 605 / 277 / 208
- P12: 4 / 8 / 2 / 1
- P13: 18039 / 14364 / 4516 / 1984
