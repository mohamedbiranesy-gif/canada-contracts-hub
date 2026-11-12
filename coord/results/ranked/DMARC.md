# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 112223 | 233 |
| v=DMARC1; p=none (monitor only) | 107649 | 602 |
| p=quarantine | 37472 | 589 |
| p=reject | 18050 | 585 |
| invalid DMARC record | 212 | 1 |
| lookup error | 94 | 0 |

Rows without enforcement (no record / p=none / invalid): **220084**

## By package (no record / p=none / quarantine / reject)
- P01: 22 / 184 / 204 / 216
- P01M: 48 / 68 / 65 / 69
- P01T: 30 / 82 / 68 / 45
- P02: 54 / 163 / 143 / 107
- P03: 3 / 67 / 89 / 106
- P04: 706 / 1367 / 904 / 591
- P05: 52 / 140 / 132 / 100
- P06: 27 / 80 / 69 / 99
- P06M: 7514 / 7798 / 4384 / 2484
- P06T: 25752 / 24755 / 6442 / 2805
- P07: 218 / 297 / 175 / 128
- P08: 10307 / 12298 / 4978 / 2664
- P09: 50 / 89 / 91 / 43
- P10: 503 / 773 / 459 / 389
- P11: 556 / 713 / 312 / 223
- P12: 2 / 8 / 0 / 1
- P13: 66379 / 58767 / 18957 / 7980
