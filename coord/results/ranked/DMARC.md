# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 98565 | 207 |
| v=DMARC1; p=none (monitor only) | 91846 | 556 |
| p=quarantine | 30500 | 565 |
| p=reject | 15098 | 578 |
| invalid DMARC record | 182 | 1 |
| lookup error | 71 | 0 |

Rows without enforcement (no record / p=none / invalid): **190593**

## By package (no record / p=none / quarantine / reject)
- P01: 25 / 180 / 205 / 215
- P01M: 25 / 25 / 30 / 25
- P01T: 52 / 106 / 106 / 70
- P02: 57 / 178 / 139 / 100
- P03: 2 / 59 / 84 / 112
- P04: 790 / 1505 / 956 / 630
- P05: 53 / 143 / 134 / 97
- P06: 22 / 93 / 85 / 111
- P06M: 4197 / 3716 / 1817 / 892
- P06T: 23310 / 25370 / 7870 / 3431
- P07: 196 / 305 / 186 / 150
- P08: 8442 / 11038 / 4659 / 2482
- P09: 58 / 100 / 101 / 42
- P10: 640 / 1034 / 603 / 457
- P10R: 48854 / 35593 / 10009 / 4457
- P11: 3433 / 6296 / 1149 / 698
- P12: 2 / 5 / 0 / 0
- P13: 8407 / 6100 / 2367 / 1129
