# Coverage vs the downstream team's targets — 2026-11-13

Benchmarks (field × package with a numeric target): **87 of 438 met** (19.9%); 67 within 10 points; 284 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 434, P01T 203, P01_GOLD 645, P02 484, P03 274, P04 4762, P05 429, P06M 32175, P06T 55107, P06 241, P07 758, P08 28706, P09 71, P10R 0, P10 2005, P11 1800, P12 11, P13 209522

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 434 | 0.0% | 13.4% | 7 | vendor GST/HST number (413 rows) |
| P01T | 203 | 1.0% | 32.5% | 8 | payment terms (159 rows) |
| P01_GOLD | 645 | 22.8% | 68.8% | 9 | payment terms (243 rows) |
| P02 | 484 | 7.0% | 52.9% | 9 | PO rule (372 rows) |
| P03 | 274 | 14.2% | 54.7% | 9 | PO rule (140 rows) |
| P04 | 4762 | 0.9% | 13.7% | 7 | PO rule (4497 rows) |
| P05 | 429 | 0.9% | 16.8% | 7 | payment terms (358 rows) |
| P06M | 32175 | 0.0% | 3.0% | 7 | PO rule (31351 rows) |
| P06T | 55107 | 0.1% | 14.7% | 7 | PO rule (54754 rows) |
| P06 | 241 | 0.4% | 11.6% | 7 | reference to quote (PO / contract / vendor id) (225 rows) |
| P07 | 758 | 0.0% | 5.3% | 6 | PO rule (720 rows) |
| P08 | 28706 | 0.0% | 3.2% | 6 | PO rule (28393 rows) |
| P09 | 71 | 4.2% | 35.2% | 8 | payment terms (62 rows) |
| P10 | 2005 | 0.0% | 1.2% | 5 | reference to quote (PO / contract / vendor id) (2005 rows) |
| P11 | 1800 | 0.1% | 8.2% | 6 | PO rule (1737 rows) |
| P12 | 11 | 0.0% | 36.4% | 8 | PO rule (11 rows) |
| P13 | 209522 | 0.0% | 0.3% | 6 | reference to quote (PO / contract / vendor id) (209522 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 434 | 13 | 130 | 291 | 0 | 0 | 70 |
| P01T | 203 | 26 | 31 | 146 | 0 | 0 | 66 |
| P01_GOLD | 645 | 250 | 174 | 221 | 0 | 0 | 81 |
| P02 | 484 | 0 | 196 | 288 | 0 | 0 | 66 |
| P03 | 274 | 0 | 0 | 263 | 11 | 0 | 57 |
| P04 | 4762 | 0 | 0 | 4129 | 633 | 0 | 46 |
| P05 | 429 | 14 | 29 | 374 | 12 | 0 | 51 |
| P06M | 32175 | 0 | 52 | 32084 | 39 | 0 | 46 |
| P06T | 55107 | 0 | 25 | 38528 | 16554 | 0 | 38 |
| P06 | 241 | 15 | 33 | 193 | 0 | 0 | 67 |
| P07 | 758 | 0 | 21 | 719 | 18 | 0 | 56 |
| P08 | 28706 | 0 | 0 | 26113 | 2593 | 0 | 46 |
| P09 | 71 | 3 | 6 | 62 | 0 | 0 | 52 |
| P10 | 2005 | 2 | 10 | 1355 | 638 | 0 | 41 |
| P11 | 1800 | 7 | 11 | 37 | 0 | 1745 | 25 |
| P12 | 11 | 0 | 0 | 11 | 0 | 0 | 51 |
| P13 | 209522 | 20 | 80 | 209407 | 15 | 0 | 38 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 434 | 318 | 73.3% | tax treatment (85) |
| P01T | 203 | 121 | 59.6% | bill-to legal name and address (66) |
| P01_GOLD | 645 | 486 | 75.3% | bill-to legal name and address (93) |
| P02 | 484 | 330 | 68.2% | the buyer's PO / reference rule (84) |
| P03 | 274 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (274) |
| P04 | 4762 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (4762) |
| P05 | 429 | 45 | 10.5% | a confirmed invoicing / AP or finance channel (341) |
| P06M | 32175 | 352 | 1.1% | a confirmed invoicing / AP or finance channel (31715) |
| P06T | 55107 | 345 | 0.6% | a confirmed invoicing / AP or finance channel (54357) |
| P06 | 241 | 44 | 18.3% | the buyer's PO / reference rule (108) |
| P07 | 758 | 52 | 6.9% | the buyer's PO / reference rule (318) |
| P08 | 28706 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (28706) |
| P09 | 71 | 10 | 14.1% | a confirmed invoicing / AP or finance channel (51) |
| P10 | 2005 | 5 | 0.2% | a confirmed invoicing / AP or finance channel (1932) |
| P11 | 1800 | 18 | 1.0% | a confirmed invoicing / AP or finance channel (1745) |
| P12 | 11 | 2 | 18.2% | a confirmed invoicing / AP or finance channel (9) |
| P13 | 209522 | 64 | 0.0% | a confirmed invoicing / AP or finance channel (206885) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 434 | 9 | 2.1% | 6 | 0 | the vendor's GST/HST number (BN9) (412) |
| P01T | 203 | 80 | 39.4% | 2 | 0 | the vendor's GST/HST number (BN9) (76) |
| P01_GOLD | 645 | 403 | 62.5% | 11 | 0 | the vendor's GST/HST number (BN9) (166) |
| P02 | 484 | 211 | 43.6% | 23 | 0 | the vendor's GST/HST number (BN9) (223) |
| P03 | 274 | 19 | 6.9% | 0 | 131 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (101) |
| P04 | 4762 | 42 | 0.9% | 6 | 927 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (3715) |
| P05 | 429 | 21 | 4.9% | 8 | 128 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (204) |
| P06M | 32175 | 12 | 0.0% | 14 | 779 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (30741) |
| P06T | 55107 | 362 | 0.7% | 15 | 19122 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (35150) |
| P06 | 241 | 25 | 10.4% | 47 | 0 | the vendor's GST/HST number (BN9) (107) |
| P07 | 758 | 37 | 4.9% | 142 | 39 | the vendor's GST/HST number (BN9) (343) |
| P08 | 28706 | 7 | 0.0% | 16 | 8243 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (20387) |
| P09 | 71 | 14 | 19.7% | 0 | 25 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (21) |
| P10 | 2005 | 5 | 0.2% | 14 | 276 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (1635) |
| P11 | 1800 | 7 | 0.4% | 1 | 0 | a confirmed invoicing / AP or finance channel (1729) |
| P12 | 11 | 1 | 9.1% | 0 | 5 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (4) |
| P13 | 209522 | 36 | 0.0% | 1253 | 82073 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (124612) |
| **all** | 337627 | 1291 | 0.4% | 1558 | 111748 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 421 | 0 | 0 | 0 | 319 | 12 | 0 | 314 | 356 | 1 |
| P01T | 177 | 0 | 0 | 0 | 114 | 61 | 26 | 150 | 160 | 2 |
| P01_GOLD | 395 | 0 | 0 | 0 | 39 | 76 | 29 | 218 | 258 | 2 |
| P02 | 484 | 0 | 484 | 0 | 56 | 56 | 13 | 372 | 301 | 1 |
| P03 | 274 | 0 | 274 | 0 | 27 | 45 | 25 | 140 | 146 | 2 |
| P04 | 4762 | 0 | 4762 | 0 | 2644 | 1437 | 961 | 4497 | 4265 | 31 |
| P05 | 415 | 0 | 362 | 0 | 87 | 100 | 39 | 345 | 360 | 7 |
| P06M | 32175 | 0 | 32175 | 0 | 25704 | 2795 | 120 | 31351 | 30823 | 26 |
| P06T | 55107 | 0 | 55107 | 0 | 49646 | 33510 | 21119 | 54754 | 54200 | 388 |
| P06 | 226 | 0 | 0 | 0 | 126 | 66 | 37 | 175 | 196 | 5 |
| P07 | 758 | 0 | 758 | 0 | 514 | 281 | 91 | 720 | 715 | 5 |
| P08 | 28706 | 0 | 28706 | 0 | 22735 | 11903 | 3939 | 28393 | 27955 | 183 |
| P09 | 68 | 0 | 53 | 0 | 9 | 38 | 0 | 49 | 63 | 1 |
| P10 | 2003 | 0 | 1974 | 0 | 1042 | 1092 | 924 | 1942 | 1906 | 16 |
| P11 | 1793 | 1745 | 1701 | 0 | 930 | 1192 | 502 | 1737 | 1727 | 19 |
| P12 | 11 | 0 | 10 | 0 | 0 | 3 | 0 | 11 | 11 | 2 |
| P13 | 209502 | 0 | 209007 | 0 | 178226 | 122380 | 21 | 209111 | 208153 | 91 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_phone | P13 | 55.9% | 95% | 81932 |
| buyer_logo_url | P13 | 71.3% | 95% | 49686 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 41846 |
| ap_system_hint | P13 | 0.3% | 20% | 41172 |
| buyer_legal_name_as_published | P13 | 41.6% | 60% | 38572 |
| buyer_bn_as_published | P13 | 15.1% | 30% | 31303 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 31256 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 31211 |
| buyer_payment_method_preference | P13 | 0.6% | 15% | 30238 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 11007 |
| ap_system_hint | P06T | 0.6% | 20% | 10669 |
| vendor_registered_address | P08 | 38.1% | 70% | 9154 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 8163 |
| buyer_tax_exempt_status | P06T | 0.2% | 15% | 8141 |
| buyer_payment_method_preference | P06T | 0.7% | 15% | 7906 |
| buyer_phone | P08 | 70.6% | 95% | 7013 |
| buyer_ap_cycle_published | P06M | 0.1% | 20% | 6417 |
| ap_system_hint | P06M | 1.3% | 20% | 6020 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 5729 |
| ap_system_hint | P08 | 0.9% | 20% | 5478 |
| vendor_emails | P08 | 56.0% | 75% | 5461 |
| vendor_phone | P08 | 67.5% | 85% | 5020 |
| buyer_legal_name_as_published | P08 | 58.5% | 75% | 4727 |
| buyer_esignature_preference | P06M | 0.5% | 15% | 4664 |
| buyer_payment_method_preference | P06M | 0.8% | 15% | 4583 |
| vendor_trading_name | P08 | 34.0% | 50% | 4582 |
| buyer_tax_exempt_status | P06M | 0.9% | 15% | 4534 |
| buyer_esignature_preference | P08 | 0.4% | 15% | 4191 |
| buyer_tax_exempt_status | P08 | 0.4% | 15% | 4182 |
| buyer_payment_method_preference | P08 | 0.6% | 15% | 4127 |
| vendor_bn9 | P08 | 36.4% | 50% | 3894 |
| invoice_reference_hint | P08 | 12.3% | 25% | 3636 |
| average_contract_duration_days | P04 | 14.8% | 90% | 3582 |
| currency | P04 | 21.2% | 95% | 3514 |
| ap_phone | P04 | 15.6% | 85% | 3306 |
| commodity_codes | P04 | 16.8% | 85% | 3250 |
| award_or_notice_id | P04 | 18.6% | 85% | 3161 |
| contract_value | P04 | 20.9% | 85% | 3053 |
| invoice_mailing_address | P04 | 15.3% | 75% | 2843 |
| end_date | P04 | 33.8% | 90% | 2676 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 95.2% | 95.2% | +2.0 | 50% | ✅ met |
| P01T | 203 | 94.6% | 94.6% | -1.0 | 50% | ✅ met |
| P01_GOLD | 645 | 92.1% | 94.6% | -0.1 | 95% | 🟡 3 pts to go |
| P02 | 484 | 75.8% | 77.3% | +0.8 | 95% | ❌ 19 pts to go |
| P03 | 274 | 83.2% | 86.5% | +1.6 | 95% | ❌ 12 pts to go |
| P04 | 4762 | 44.1% | 45.5% | +12.3 | 90% | ❌ 46 pts to go |
| P05 | 429 | 40.1% | 43.1% | +0.5 | 70% | ❌ 30 pts to go |
| P06M | 32175 | 94.6% | 94.6% | +1.4 | n/a | no target |
| P06T | 55107 | 99.5% | 99.5% | +0.2 | n/a | no target |
| P06 | 241 | 32.0% | 32.0% | -3.4 | 30% | ✅ met |
| P07 | 758 | 13.9% | 13.9% | -0.3 | 30% | ❌ 16 pts to go |
| P08 | 28706 | 12.3% | 12.3% | +0.1 | 25% | ❌ 13 pts to go |
| P09 | 71 | 95.8% | 98.6% | -3.1 | 100% | 🟡 4 pts to go |
| P10 | 2005 | 3.1% | 3.1% | -0.2 | 25% | ❌ 22 pts to go |
| P11 | 1800 | 55.3% | 56.1% | +1.0 | 60% | 🟡 5 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 209522 | 99.4% | 99.4% | -0.2 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 203 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 645 | 5.7% | 5.7% | +0.0 | 50% | ❌ 44 pts to go |
| P02 | 484 | 5.2% | 5.2% | -1.0 | 50% | ❌ 45 pts to go |
| P03 | 274 | 1.8% | 1.8% | -0.1 | 40% | ❌ 38 pts to go |
| P04 | 4762 | 0.5% | 0.5% | -0.1 | 30% | ❌ 30 pts to go |
| P05 | 429 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 32175 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55107 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 241 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 758 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 28706 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 71 | 1.4% | 1.4% | +0.7 | 50% | ❌ 49 pts to go |
| P10 | 2005 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1800 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 209522 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 92.6% | 92.6% | +3.0 | n/a | no target |
| P01T | 203 | 77.8% | 77.8% | -2.1 | 50% | ✅ met |
| P01_GOLD | 645 | 68.7% | 68.7% | +1.4 | 85% | ❌ 16 pts to go |
| P02 | 484 | 67.4% | 67.4% | +1.2 | 90% | ❌ 23 pts to go |
| P03 | 274 | 62.4% | 62.4% | +1.9 | 85% | ❌ 23 pts to go |
| P04 | 4762 | 42.0% | 42.0% | +12.9 | 85% | ❌ 43 pts to go |
| P05 | 429 | 30.8% | 30.8% | +0.9 | 60% | ❌ 29 pts to go |
| P06M | 32175 | 94.4% | 94.4% | +1.4 | n/a | no target |
| P06T | 55107 | 99.4% | 99.4% | +0.2 | n/a | no target |
| P06 | 241 | 6.6% | 6.6% | +0.2 | n/a | no target |
| P07 | 758 | 9.1% | 9.1% | +0.0 | n/a | no target |
| P08 | 28706 | 11.4% | 11.4% | +0.1 | n/a | no target |
| P09 | 71 | 83.1% | 83.1% | -12.5 | 100% | ❌ 17 pts to go |
| P10 | 2005 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1800 | 52.7% | 52.7% | +1.2 | 60% | 🟡 7 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 209522 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 203 | 0.0% | 0.0% | +0.0 | 30% | ❌ 30 pts to go |
| P01_GOLD | 645 | 49.0% | 49.0% | -2.7 | 80% | ❌ 31 pts to go |
| P02 | 484 | 55.6% | 55.6% | -2.5 | 60% | 🟡 4 pts to go |
| P03 | 274 | 48.2% | 48.2% | -2.2 | 80% | ❌ 32 pts to go |
| P04 | 4762 | 17.9% | 17.9% | -6.1 | 50% | ❌ 32 pts to go |
| P05 | 429 | 13.5% | 13.5% | +0.9 | 40% | ❌ 26 pts to go |
| P06M | 32175 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55107 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 241 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 758 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 28706 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 71 | 36.6% | 36.6% | -44.5 | 50% | ❌ 13 pts to go |
| P10 | 2005 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1800 | 3.3% | 3.3% | +0.0 | 40% | ❌ 37 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 209522 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 203 | 0.5% | 0.5% | +0.1 | n/a | no target |
| P01_GOLD | 645 | 58.1% | 58.1% | -2.8 | 85% | ❌ 27 pts to go |
| P02 | 484 | 55.6% | 55.6% | -2.5 | 90% | ❌ 34 pts to go |
| P03 | 274 | 56.6% | 56.6% | -2.8 | 85% | ❌ 28 pts to go |
| P04 | 4762 | 18.6% | 18.6% | -6.3 | 85% | ❌ 66 pts to go |
| P05 | 429 | 21.2% | 21.2% | +0.8 | 50% | ❌ 29 pts to go |
| P06M | 32175 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55107 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 241 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 758 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 28706 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 71 | 88.7% | 88.7% | -8.4 | 100% | ❌ 11 pts to go |
| P10 | 2005 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1800 | 3.7% | 3.7% | +0.1 | 60% | ❌ 56 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 209522 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 203 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 645 | 12.4% | 12.4% | -0.2 | 60% | ❌ 48 pts to go |
| P02 | 484 | 6.6% | 6.6% | -0.7 | 50% | ❌ 43 pts to go |
| P03 | 274 | 8.0% | 8.0% | -0.6 | 50% | ❌ 42 pts to go |
| P04 | 4762 | 1.4% | 1.4% | -0.5 | 40% | ❌ 39 pts to go |
| P05 | 429 | 0.7% | 0.7% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 32175 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55107 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 241 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 758 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 28706 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 71 | 5.6% | 5.6% | +2.0 | 50% | ❌ 44 pts to go |
| P10 | 2005 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1800 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 209522 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 203 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 645 | 34.7% | 34.7% | -1.2 | 80% | ❌ 45 pts to go |
| P02 | 484 | 50.6% | 50.6% | -2.4 | 90% | ❌ 39 pts to go |
| P03 | 274 | 32.8% | 32.8% | -1.0 | 80% | ❌ 47 pts to go |
| P04 | 4762 | 16.8% | 16.8% | -5.4 | 85% | ❌ 68 pts to go |
| P05 | 429 | 7.7% | 7.7% | +1.3 | 50% | ❌ 42 pts to go |
| P06M | 32175 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55107 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 241 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 758 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 28706 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 71 | 62.0% | 62.0% | -11.1 | 95% | ❌ 33 pts to go |
| P10 | 2005 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1800 | 2.7% | 2.7% | +0.1 | 50% | ❌ 47 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 209522 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 203 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 645 | 8.1% | 8.1% | +0.0 | 50% | ❌ 42 pts to go |
| P02 | 484 | 5.0% | 5.0% | -1.2 | 50% | ❌ 45 pts to go |
| P03 | 274 | 2.6% | 2.6% | +0.0 | 30% | ❌ 27 pts to go |
| P04 | 4762 | 0.5% | 0.5% | -0.1 | 30% | ❌ 30 pts to go |
| P05 | 429 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 32175 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55107 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 241 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 758 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 28706 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 71 | 1.4% | 1.4% | +1.0 | n/a | no target |
| P10 | 2005 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1800 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 209522 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 203 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 645 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 484 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 274 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4762 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 429 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 32175 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 55107 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 241 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 758 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 28706 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 71 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2005 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1800 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 209522 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 4.8% | 4.8% | -1.6 | 70% | ❌ 65 pts to go |
| P01T | 203 | 54.7% | 54.7% | -5.6 | 60% | 🟡 5 pts to go |
| P01_GOLD | 645 | 72.1% | 72.1% | -2.7 | 90% | ❌ 18 pts to go |
| P02 | 484 | 51.7% | 51.7% | -2.6 | 85% | ❌ 33 pts to go |
| P03 | 274 | 63.9% | 63.9% | -3.0 | 90% | ❌ 26 pts to go |
| P04 | 4762 | 29.5% | 29.5% | -8.7 | 75% | ❌ 46 pts to go |
| P05 | 429 | 54.5% | 54.5% | -0.2 | 50% | ✅ met |
| P06M | 32175 | 3.0% | 3.0% | +0.1 | n/a | no target |
| P06T | 55107 | 65.7% | 65.7% | +1.2 | n/a | no target |
| P06 | 241 | 45.2% | 45.2% | +3.1 | 40% | ✅ met |
| P07 | 758 | 37.2% | 37.2% | +5.1 | 50% | ❌ 13 pts to go |
| P08 | 28706 | 36.4% | 36.4% | +5.8 | 50% | ❌ 14 pts to go |
| P09 | 71 | 64.8% | 64.8% | +8.1 | 80% | ❌ 15 pts to go |
| P10 | 2005 | 38.8% | 38.8% | +0.0 | 40% | 🟡 1 pts to go |
| P11 | 1800 | 54.8% | 54.8% | +0.2 | 60% | 🟡 5 pts to go |
| P12 | 11 | 54.5% | 54.5% | +9.0 | 85% | ❌ 30 pts to go |
| P13 | 209522 | 44.9% | 44.9% | +0.1 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 44.7% | 44.7% | -1.9 | n/a | no target |
| P01T | 203 | 54.2% | 54.2% | -5.6 | n/a | no target |
| P01_GOLD | 645 | 74.3% | 74.3% | +1.4 | 95% | ❌ 21 pts to go |
| P02 | 484 | 75.0% | 75.0% | +0.4 | 95% | ❌ 20 pts to go |
| P03 | 274 | 71.5% | 71.5% | +2.0 | 95% | ❌ 24 pts to go |
| P04 | 4762 | 56.3% | 56.3% | +3.2 | 95% | ❌ 39 pts to go |
| P05 | 429 | 58.7% | 58.7% | +0.6 | 70% | ❌ 11 pts to go |
| P06M | 32175 | 39.2% | 39.2% | -2.1 | n/a | no target |
| P06T | 55107 | 65.5% | 65.5% | -2.0 | n/a | no target |
| P06 | 241 | 40.2% | 40.2% | +2.0 | 80% | ❌ 40 pts to go |
| P07 | 758 | 37.5% | 37.5% | +6.5 | 70% | ❌ 32 pts to go |
| P08 | 28706 | 38.1% | 38.1% | +8.4 | 70% | ❌ 32 pts to go |
| P09 | 71 | 60.6% | 60.6% | -25.6 | 100% | ❌ 39 pts to go |
| P10 | 2005 | 39.2% | 39.2% | +0.0 | 70% | ❌ 31 pts to go |
| P11 | 1800 | 59.6% | 59.6% | +1.0 | 75% | ❌ 15 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 209522 | 40.9% | 40.9% | +0.7 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 21.4% | 21.4% | -0.7 | n/a | no target |
| P01T | 203 | 61.6% | 61.6% | -3.9 | n/a | no target |
| P01_GOLD | 645 | 50.7% | 50.7% | +1.9 | 60% | 🟡 9 pts to go |
| P02 | 484 | 58.3% | 58.3% | +2.5 | 60% | 🟡 2 pts to go |
| P03 | 274 | 54.0% | 54.0% | +1.7 | 60% | 🟡 6 pts to go |
| P04 | 4762 | 54.3% | 54.3% | +11.7 | 55% | 🟡 1 pts to go |
| P05 | 429 | 23.5% | 23.5% | +0.8 | 50% | ❌ 26 pts to go |
| P06M | 32175 | 11.5% | 11.5% | +2.0 | n/a | no target |
| P06T | 55107 | 74.7% | 74.7% | +6.8 | n/a | no target |
| P06 | 241 | 50.2% | 50.2% | +1.6 | n/a | no target |
| P07 | 758 | 39.8% | 39.8% | +0.2 | 55% | ❌ 15 pts to go |
| P08 | 28706 | 34.0% | 34.0% | +1.0 | 50% | ❌ 16 pts to go |
| P09 | 71 | 39.4% | 39.4% | -32.6 | 70% | ❌ 31 pts to go |
| P10 | 2005 | 47.6% | 47.6% | -0.5 | 55% | 🟡 7 pts to go |
| P11 | 1800 | 59.7% | 59.7% | +0.5 | 50% | ✅ met |
| P12 | 11 | 90.9% | 90.9% | +0.0 | n/a | no target |
| P13 | 209522 | 2.9% | 2.9% | -0.3 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 23.0% | 23.0% | -10.3 | n/a | no target |
| P01T | 203 | 77.3% | 77.3% | -2.2 | n/a | no target |
| P01_GOLD | 645 | 47.9% | 47.9% | -2.5 | 70% | ❌ 22 pts to go |
| P02 | 484 | 54.8% | 54.8% | -2.0 | 70% | ❌ 15 pts to go |
| P03 | 274 | 47.8% | 47.8% | -2.6 | 70% | ❌ 22 pts to go |
| P04 | 4762 | 49.3% | 49.3% | -5.6 | 65% | ❌ 16 pts to go |
| P05 | 429 | 29.8% | 29.8% | +0.7 | 60% | ❌ 30 pts to go |
| P06M | 32175 | 22.7% | 22.7% | -4.7 | n/a | no target |
| P06T | 55107 | 87.1% | 87.1% | +4.4 | n/a | no target |
| P06 | 241 | 70.1% | 70.1% | +0.8 | 40% | ✅ met |
| P07 | 758 | 66.4% | 66.4% | +1.4 | 85% | ❌ 19 pts to go |
| P08 | 28706 | 67.5% | 67.5% | +3.5 | 85% | ❌ 18 pts to go |
| P09 | 71 | 31.0% | 31.0% | -25.4 | 85% | ❌ 54 pts to go |
| P10 | 2005 | 65.0% | 65.0% | -1.1 | 85% | ❌ 20 pts to go |
| P11 | 1800 | 68.4% | 68.4% | +0.3 | 75% | 🟡 7 pts to go |
| P12 | 11 | 36.4% | 36.4% | +0.0 | n/a | no target |
| P13 | 209522 | 90.7% | 90.7% | -1.1 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 27.6% | 27.6% | -10.2 | n/a | no target |
| P01T | 203 | 98.0% | 98.0% | -0.3 | n/a | no target |
| P01_GOLD | 645 | 75.0% | 75.0% | -3.6 | 90% | ❌ 15 pts to go |
| P02 | 484 | 78.3% | 78.3% | -3.5 | 90% | ❌ 12 pts to go |
| P03 | 274 | 81.0% | 81.0% | -4.3 | 90% | 🟡 9 pts to go |
| P04 | 4762 | 70.8% | 70.8% | -12.0 | 85% | ❌ 14 pts to go |
| P05 | 429 | 44.8% | 44.8% | +0.3 | 70% | ❌ 25 pts to go |
| P06M | 32175 | 28.4% | 28.4% | -4.6 | n/a | no target |
| P06T | 55107 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 241 | 99.2% | 99.2% | -0.1 | 50% | ✅ met |
| P07 | 758 | 99.9% | 99.9% | +0.0 | 100% | 🟡 0 pts to go |
| P08 | 28706 | 99.9% | 99.9% | +0.0 | 100% | 🟡 0 pts to go |
| P09 | 71 | 45.1% | 45.1% | -32.7 | 100% | ❌ 55 pts to go |
| P10 | 2005 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1800 | 97.4% | 97.4% | -0.6 | 100% | 🟡 3 pts to go |
| P12 | 11 | 54.5% | 54.5% | +0.0 | n/a | no target |
| P13 | 209522 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 12.7% | 12.7% | -3.4 | n/a | no target |
| P01T | 203 | 53.7% | 53.7% | -6.1 | n/a | no target |
| P01_GOLD | 645 | 41.7% | 41.7% | -1.7 | 70% | ❌ 28 pts to go |
| P02 | 484 | 45.0% | 45.0% | -2.2 | 75% | ❌ 30 pts to go |
| P03 | 274 | 43.4% | 43.4% | -1.3 | 75% | ❌ 32 pts to go |
| P04 | 4762 | 35.0% | 35.0% | -3.7 | 70% | ❌ 35 pts to go |
| P05 | 429 | 22.1% | 22.1% | +0.8 | 55% | ❌ 33 pts to go |
| P06M | 32175 | 6.8% | 6.8% | +0.9 | n/a | no target |
| P06T | 55107 | 41.6% | 41.6% | -5.8 | n/a | no target |
| P06 | 241 | 52.3% | 52.3% | +1.2 | n/a | no target |
| P07 | 758 | 53.8% | 53.8% | +1.1 | 70% | ❌ 16 pts to go |
| P08 | 28706 | 56.0% | 56.0% | +1.2 | 75% | ❌ 19 pts to go |
| P09 | 71 | 22.5% | 22.5% | -24.4 | 85% | ❌ 62 pts to go |
| P10 | 2005 | 44.4% | 44.4% | +0.0 | 80% | ❌ 36 pts to go |
| P11 | 1800 | 51.8% | 51.8% | -1.5 | 70% | ❌ 18 pts to go |
| P12 | 11 | 27.3% | 27.3% | +0.0 | n/a | no target |
| P13 | 209522 | 5.9% | 5.9% | +0.4 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 26.3% | 26.3% | -11.5 | n/a | no target |
| P01T | 203 | 96.1% | 96.1% | -0.4 | n/a | no target |
| P01_GOLD | 645 | 69.5% | 69.5% | -3.4 | 90% | ❌ 20 pts to go |
| P02 | 484 | 73.1% | 73.1% | -3.6 | 90% | ❌ 17 pts to go |
| P03 | 274 | 77.7% | 77.7% | -4.3 | 90% | ❌ 12 pts to go |
| P04 | 4762 | 66.4% | 66.4% | -11.3 | 85% | ❌ 19 pts to go |
| P05 | 429 | 43.6% | 43.6% | +0.7 | 75% | ❌ 31 pts to go |
| P06M | 32175 | 27.4% | 27.4% | -5.5 | n/a | no target |
| P06T | 55107 | 97.8% | 97.8% | -0.5 | n/a | no target |
| P06 | 241 | 91.7% | 91.7% | +1.7 | n/a | no target |
| P07 | 758 | 94.2% | 94.2% | +2.5 | 100% | 🟡 6 pts to go |
| P08 | 28706 | 92.8% | 92.8% | +5.5 | 100% | 🟡 7 pts to go |
| P09 | 71 | 35.2% | 35.2% | -31.3 | n/a | no target |
| P10 | 2005 | 89.9% | 89.9% | -0.4 | 100% | ❌ 10 pts to go |
| P11 | 1800 | 90.2% | 90.2% | +0.0 | n/a | no target |
| P12 | 11 | 54.5% | 54.5% | +0.0 | n/a | no target |
| P13 | 209522 | 69.0% | 69.0% | -0.8 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 35.0% | 35.0% | -1.9 | n/a | no target · QC vendors: 71 rows, 100.0% filled |
| P01T | 203 | 23.6% | 23.6% | +3.9 | n/a | no target · QC vendors: 36 rows, 88.9% filled |
| P01_GOLD | 645 | 45.4% | 45.4% | +1.9 | 95% | ❌ 50 pts to go · QC vendors: 49 rows, 95.9% filled |
| P02 | 484 | 58.3% | 58.3% | +2.3 | 95% | ❌ 37 pts to go · QC vendors: 113 rows, 100.0% filled |
| P03 | 274 | 45.6% | 45.6% | +2.7 | 95% | ❌ 49 pts to go · QC vendors: 20 rows, 100.0% filled |
| P04 | 4762 | 40.6% | 40.6% | +8.2 | 95% | ❌ 54 pts to go · QC vendors: 643 rows, 98.3% filled |
| P05 | 429 | 14.5% | 14.5% | +0.5 | n/a | no target · QC vendors: 38 rows, 100.0% filled |
| P06M | 32175 | 34.8% | 34.8% | -2.7 | n/a | no target · QC vendors: 8060 rows, 100.0% filled |
| P06T | 55107 | 38.8% | 38.8% | +8.2 | n/a | no target · QC vendors: 21786 rows, 96.0% filled |
| P06 | 241 | 7.5% | 7.5% | +0.4 | n/a | no target · QC vendors: 11 rows, 63.6% filled |
| P07 | 758 | 8.0% | 8.0% | +1.1 | n/a | no target · QC vendors: 52 rows, 82.7% filled |
| P08 | 28706 | 9.0% | 9.0% | +2.0 | n/a | no target · QC vendors: 2225 rows, 96.3% filled |
| P09 | 71 | 28.2% | 28.2% | -45.3 | 95% | ❌ 67 pts to go · QC vendors: 7 rows, 100.0% filled |
| P10 | 2005 | 15.9% | 15.9% | +0.2 | n/a | no target · QC vendors: 196 rows, 92.3% filled |
| P11 | 1800 | 21.3% | 21.3% | +1.7 | n/a | no target · QC vendors: 328 rows, 95.1% filled |
| P12 | 11 | 81.8% | 81.8% | +0.0 | n/a | no target · QC vendors: 2 rows, 100.0% filled |
| P13 | 209522 | 22.4% | 22.4% | +0.2 | n/a | no target · QC vendors: 46934 rows, 100.0% filled |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 44.2% | 44.2% | -2.0 | n/a | no target · vendors with a registry record: 192 rows, 100.0% filled |
| P01T | 203 | 54.2% | 54.2% | -5.6 | n/a | no target · vendors with a registry record: 110 rows, 100.0% filled |
| P01_GOLD | 645 | 81.9% | 81.9% | +1.0 | 100% | ❌ 18 pts to go · vendors with a registry record: 528 rows, 100.0% filled |
| P02 | 484 | 78.9% | 78.9% | +0.5 | 100% | ❌ 21 pts to go · vendors with a registry record: 382 rows, 100.0% filled |
| P03 | 274 | 79.6% | 79.6% | +1.4 | 100% | ❌ 20 pts to go · vendors with a registry record: 218 rows, 100.0% filled |
| P04 | 4762 | 56.9% | 56.9% | +2.9 | 100% | ❌ 43 pts to go · vendors with a registry record: 2709 rows, 100.0% filled |
| P05 | 429 | 63.2% | 63.2% | +0.4 | n/a | no target · vendors with a registry record: 271 rows, 100.0% filled |
| P06M | 32175 | 39.2% | 39.2% | -2.0 | n/a | no target · vendors with a registry record: 12615 rows, 100.0% filled |
| P06T | 55107 | 65.5% | 65.5% | -2.1 | n/a | no target · vendors with a registry record: 36093 rows, 100.0% filled |
| P06 | 241 | 41.5% | 41.5% | +2.2 | n/a | no target · vendors with a registry record: 100 rows, 100.0% filled |
| P07 | 758 | 38.1% | 38.1% | +6.3 | n/a | no target · vendors with a registry record: 289 rows, 100.0% filled |
| P08 | 28706 | 38.3% | 38.3% | +8.3 | n/a | no target · vendors with a registry record: 10994 rows, 100.0% filled |
| P09 | 71 | 73.2% | 73.2% | -16.3 | n/a | no target · vendors with a registry record: 52 rows, 100.0% filled |
| P10 | 2005 | 40.0% | 40.0% | -0.1 | n/a | no target · vendors with a registry record: 803 rows, 100.0% filled |
| P11 | 1800 | 60.4% | 60.4% | +1.1 | n/a | no target · vendors with a registry record: 1088 rows, 100.0% filled |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 11 rows, 100.0% filled |
| P13 | 209522 | 40.9% | 40.9% | +0.7 | n/a | no target · vendors with a registry record: 85632 rows, 100.0% filled |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 97.2% | 97.2% | +0.8 | 90% | ✅ met |
| P01T | 203 | 70.0% | 70.0% | -0.7 | 90% | ❌ 20 pts to go |
| P01_GOLD | 645 | 88.2% | 88.2% | +0.8 | 95% | 🟡 7 pts to go |
| P02 | 484 | 88.4% | 88.4% | +0.2 | 95% | 🟡 7 pts to go |
| P03 | 274 | 83.6% | 83.6% | +0.5 | 85% | 🟡 1 pts to go |
| P04 | 4762 | 69.8% | 69.8% | +5.3 | 90% | ❌ 20 pts to go |
| P05 | 429 | 76.7% | 76.7% | -1.3 | 75% | ✅ met |
| P06M | 32175 | 91.3% | 91.3% | -2.5 | n/a | no target |
| P06T | 55107 | 39.2% | 39.2% | +2.3 | n/a | no target |
| P06 | 241 | 72.6% | 72.6% | +1.5 | 80% | 🟡 7 pts to go |
| P07 | 758 | 62.9% | 63.1% | +4.7 | 80% | ❌ 17 pts to go |
| P08 | 28706 | 58.5% | 58.5% | +6.6 | 75% | ❌ 16 pts to go |
| P09 | 71 | 46.5% | 46.5% | -29.1 | 95% | ❌ 48 pts to go |
| P10 | 2005 | 45.5% | 45.6% | -1.3 | 70% | ❌ 24 pts to go |
| P11 | 1800 | 33.8% | 33.8% | +2.0 | 65% | ❌ 31 pts to go |
| P12 | 11 | 72.7% | 72.7% | +0.0 | 80% | 🟡 7 pts to go |
| P13 | 209522 | 41.6% | 41.6% | -4.0 | 60% | ❌ 18 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 17.7% | 17.7% | -0.8 | 50% | ❌ 32 pts to go |
| P01T | 203 | 16.3% | 16.3% | +0.1 | n/a | no target |
| P01_GOLD | 645 | 19.4% | 19.4% | -0.4 | 40% | ❌ 21 pts to go |
| P02 | 484 | 18.8% | 18.8% | -1.1 | 40% | ❌ 21 pts to go |
| P03 | 274 | 21.9% | 21.9% | +1.6 | 40% | ❌ 18 pts to go |
| P04 | 4762 | 15.9% | 15.9% | -0.4 | 40% | ❌ 24 pts to go |
| P05 | 429 | 21.0% | 21.0% | +0.1 | 25% | 🟡 4 pts to go |
| P06M | 32175 | 21.9% | 21.9% | +1.5 | n/a | no target |
| P06T | 55107 | 11.8% | 11.8% | +4.3 | n/a | no target |
| P06 | 241 | 22.4% | 22.4% | +4.9 | 35% | ❌ 13 pts to go |
| P07 | 758 | 28.0% | 28.0% | +8.9 | 35% | 🟡 7 pts to go |
| P08 | 28706 | 27.0% | 27.0% | +9.3 | 35% | 🟡 8 pts to go |
| P09 | 71 | 8.5% | 8.5% | -8.2 | n/a | no target |
| P10 | 2005 | 8.7% | 8.7% | +1.6 | 30% | ❌ 21 pts to go |
| P11 | 1800 | 11.3% | 11.3% | +4.8 | n/a | no target |
| P12 | 11 | 9.1% | 9.1% | -9.1 | n/a | no target |
| P13 | 209522 | 15.1% | 15.1% | +2.6 | 30% | ❌ 15 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 203 | 85.7% | 85.7% | +0.5 | 100% | ❌ 14 pts to go |
| P01_GOLD | 645 | 91.8% | 91.8% | +0.7 | 100% | 🟡 8 pts to go |
| P02 | 484 | 96.9% | 96.9% | +0.3 | 100% | 🟡 3 pts to go |
| P03 | 274 | 90.1% | 90.1% | +0.6 | 100% | 🟡 10 pts to go |
| P04 | 4762 | 79.4% | 79.4% | +6.9 | 100% | ❌ 21 pts to go |
| P05 | 429 | 90.2% | 90.2% | +0.2 | 100% | 🟡 10 pts to go |
| P06M | 32175 | 99.6% | 99.6% | +0.2 | n/a | no target |
| P06T | 55107 | 61.7% | 61.7% | +3.0 | n/a | no target |
| P06 | 241 | 83.0% | 83.0% | +0.9 | 95% | ❌ 12 pts to go |
| P07 | 758 | 87.7% | 87.7% | +2.3 | 95% | 🟡 7 pts to go |
| P08 | 28706 | 86.2% | 86.2% | +1.7 | 95% | 🟡 9 pts to go |
| P09 | 71 | 94.4% | 94.4% | -2.0 | 100% | 🟡 6 pts to go |
| P10 | 2005 | 53.8% | 53.9% | -0.8 | 95% | ❌ 41 pts to go |
| P11 | 1800 | 64.1% | 64.1% | +3.2 | 80% | ❌ 16 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 209522 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 64.3% | 64.3% | -6.8 | n/a | no target |
| P01T | 203 | 70.9% | 70.9% | -3.3 | n/a | no target |
| P01_GOLD | 645 | 72.7% | 72.7% | -0.5 | 90% | ❌ 17 pts to go |
| P02 | 484 | 77.5% | 77.5% | -0.9 | 95% | ❌ 18 pts to go |
| P03 | 274 | 74.1% | 74.1% | +0.0 | 95% | ❌ 21 pts to go |
| P04 | 4762 | 69.5% | 69.5% | +0.0 | 95% | ❌ 26 pts to go |
| P05 | 429 | 71.8% | 71.8% | -0.7 | 90% | ❌ 18 pts to go |
| P06M | 32175 | 68.0% | 68.0% | -8.7 | n/a | no target |
| P06T | 55107 | 57.5% | 57.5% | -1.1 | n/a | no target |
| P06 | 241 | 71.0% | 71.0% | +5.6 | 95% | ❌ 24 pts to go |
| P07 | 758 | 67.2% | 67.2% | +7.5 | 90% | ❌ 23 pts to go |
| P08 | 28706 | 70.6% | 70.6% | +12.0 | 95% | ❌ 24 pts to go |
| P09 | 71 | 66.2% | 66.2% | -19.6 | 100% | ❌ 34 pts to go |
| P10 | 2005 | 52.8% | 52.8% | -1.0 | 95% | ❌ 42 pts to go |
| P11 | 1800 | 32.8% | 32.8% | +2.1 | 75% | ❌ 42 pts to go |
| P12 | 11 | 81.8% | 81.8% | +0.0 | n/a | no target |
| P13 | 209522 | 55.9% | 55.9% | -12.0 | 95% | ❌ 39 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 76.0% | 76.0% | -7.5 | n/a | no target |
| P01T | 203 | 89.7% | 89.7% | -2.0 | 95% | 🟡 5 pts to go |
| P01_GOLD | 645 | 85.6% | 85.6% | +0.6 | 90% | 🟡 4 pts to go |
| P02 | 484 | 90.5% | 90.5% | -0.5 | 95% | 🟡 4 pts to go |
| P03 | 274 | 83.9% | 83.9% | +0.1 | 95% | ❌ 11 pts to go |
| P04 | 4762 | 90.2% | 90.2% | -1.4 | 90% | ✅ met |
| P05 | 429 | 92.8% | 92.8% | +0.4 | 95% | 🟡 2 pts to go |
| P06M | 32175 | 79.0% | 79.0% | -6.3 | n/a | no target |
| P06T | 55107 | 86.3% | 86.3% | +1.7 | n/a | no target |
| P06 | 241 | 92.5% | 92.5% | +7.1 | 100% | 🟡 8 pts to go |
| P07 | 758 | 94.3% | 94.3% | +10.7 | 100% | 🟡 6 pts to go |
| P08 | 28706 | 94.8% | 94.8% | +17.0 | 100% | 🟡 5 pts to go |
| P09 | 71 | 71.8% | 71.8% | -2.4 | n/a | no target |
| P10 | 2005 | 94.3% | 94.3% | -0.1 | 100% | 🟡 6 pts to go |
| P11 | 1800 | 55.4% | 55.4% | +4.3 | 80% | ❌ 25 pts to go |
| P12 | 11 | 90.9% | 90.9% | +0.0 | n/a | no target |
| P13 | 209522 | 71.3% | 71.3% | -9.5 | 95% | ❌ 24 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 3.5% | 3.5% | +0.3 | n/a | no target |
| P01T | 203 | 9.4% | 9.4% | +0.7 | n/a | no target |
| P01_GOLD | 645 | 14.0% | 14.0% | +0.0 | 25% | ❌ 11 pts to go |
| P02 | 484 | 24.4% | 24.4% | -0.4 | 40% | ❌ 16 pts to go |
| P03 | 274 | 9.1% | 9.1% | +0.1 | 20% | ❌ 11 pts to go |
| P04 | 4762 | 2.5% | 2.5% | -0.8 | 20% | ❌ 18 pts to go |
| P05 | 429 | 3.0% | 3.0% | -0.3 | 15% | ❌ 12 pts to go |
| P06M | 32175 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 55107 | 0.3% | 0.3% | +0.1 | n/a | no target |
| P06 | 241 | 5.4% | 5.4% | +0.0 | n/a | no target |
| P07 | 758 | 8.2% | 8.2% | +0.3 | n/a | no target |
| P08 | 28706 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 71 | 1.4% | 1.4% | -6.2 | n/a | no target |
| P10 | 2005 | 0.8% | 0.8% | +0.0 | n/a | no target |
| P11 | 1800 | 0.7% | 0.7% | +0.0 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 209522 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 13.6% | 13.6% | -2.5 | n/a | no target |
| P01T | 203 | 18.7% | 18.7% | -0.5 | 70% | ❌ 51 pts to go |
| P01_GOLD | 645 | 41.1% | 41.1% | -1.0 | 80% | ❌ 39 pts to go |
| P02 | 484 | 55.2% | 55.2% | -2.1 | 90% | ❌ 35 pts to go |
| P03 | 274 | 18.6% | 18.6% | -0.6 | 60% | ❌ 41 pts to go |
| P04 | 4762 | 15.6% | 15.6% | -4.6 | 85% | ❌ 69 pts to go |
| P05 | 429 | 10.7% | 10.7% | -0.4 | 50% | ❌ 39 pts to go |
| P06M | 32175 | 0.7% | 0.7% | +0.1 | n/a | no target |
| P06T | 55107 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P06 | 241 | 13.3% | 13.3% | +0.1 | n/a | no target |
| P07 | 758 | 9.9% | 9.9% | +0.8 | n/a | no target |
| P08 | 28706 | 0.6% | 0.6% | +0.1 | n/a | no target |
| P09 | 71 | 33.8% | 33.8% | -38.2 | 95% | ❌ 61 pts to go |
| P10 | 2005 | 1.4% | 1.4% | -0.2 | n/a | no target |
| P11 | 1800 | 12.6% | 12.6% | -0.4 | n/a | no target |
| P12 | 11 | 27.3% | 27.3% | +0.0 | n/a | no target |
| P13 | 209522 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 5.8% | 5.8% | +0.2 | n/a | no target |
| P01T | 203 | 11.8% | 11.8% | +2.6 | n/a | no target |
| P01_GOLD | 645 | 32.9% | 32.9% | -0.9 | 70% | ❌ 37 pts to go |
| P02 | 484 | 38.0% | 38.0% | -0.7 | 75% | ❌ 37 pts to go |
| P03 | 274 | 19.3% | 19.3% | +0.1 | 55% | ❌ 36 pts to go |
| P04 | 4762 | 15.3% | 15.3% | -4.9 | 75% | ❌ 60 pts to go |
| P05 | 429 | 10.0% | 10.0% | -0.2 | 50% | ❌ 40 pts to go |
| P06M | 32175 | 0.3% | 0.3% | +0.1 | n/a | no target |
| P06T | 55107 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 241 | 6.2% | 6.2% | +0.5 | n/a | no target |
| P07 | 758 | 5.1% | 5.1% | +0.5 | n/a | no target |
| P08 | 28706 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 71 | 33.8% | 33.8% | -34.9 | 95% | ❌ 61 pts to go |
| P10 | 2005 | 0.7% | 0.7% | -0.1 | n/a | no target |
| P11 | 1800 | 12.4% | 12.4% | -0.4 | n/a | no target |
| P12 | 11 | 18.2% | 18.2% | +0.0 | n/a | no target |
| P13 | 209522 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 11.3% | 11.3% | +3.7 | n/a | no target |
| P01T | 203 | 8.4% | 8.4% | -0.3 | n/a | no target |
| P01_GOLD | 645 | 55.0% | 55.2% | -2.1 | 80% | ❌ 25 pts to go |
| P02 | 484 | 44.2% | 44.4% | -1.1 | 75% | ❌ 31 pts to go |
| P03 | 274 | 34.3% | 34.3% | -1.8 | 70% | ❌ 36 pts to go |
| P04 | 4762 | 15.1% | 15.3% | -4.8 | 70% | ❌ 55 pts to go |
| P05 | 429 | 13.5% | 13.5% | -0.5 | 50% | ❌ 36 pts to go |
| P06M | 32175 | 0.4% | 0.4% | +0.1 | n/a | no target |
| P06T | 55107 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06 | 241 | 13.3% | 13.3% | +0.1 | n/a | no target |
| P07 | 758 | 1.5% | 1.5% | +0.4 | n/a | no target |
| P08 | 28706 | 0.4% | 0.4% | +0.1 | n/a | no target |
| P09 | 71 | 45.1% | 45.1% | -1.8 | 80% | ❌ 35 pts to go |
| P10 | 2005 | 1.1% | 1.1% | +0.0 | n/a | no target |
| P11 | 1800 | 4.3% | 4.3% | -0.2 | n/a | no target |
| P12 | 11 | 36.4% | 36.4% | +0.0 | n/a | no target |
| P13 | 209522 | 0.1% | 0.1% | +0.0 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 18.0% | 18.0% | +3.1 | n/a | no target |
| P01T | 203 | 21.2% | 21.2% | +2.0 | 60% | ❌ 39 pts to go |
| P01_GOLD | 645 | 60.0% | 60.0% | -2.2 | 70% | 🟡 10 pts to go |
| P02 | 484 | 37.8% | 37.8% | -1.7 | 50% | ❌ 12 pts to go |
| P03 | 274 | 46.7% | 46.7% | -1.0 | 55% | 🟡 8 pts to go |
| P04 | 4762 | 10.4% | 10.4% | -2.1 | 40% | ❌ 30 pts to go |
| P05 | 429 | 16.1% | 16.1% | -0.5 | 40% | ❌ 24 pts to go |
| P06M | 32175 | 4.2% | 4.2% | +1.4 | n/a | no target |
| P06T | 55107 | 1.6% | 1.6% | +0.1 | n/a | no target |
| P06 | 241 | 18.7% | 18.7% | +0.5 | n/a | no target |
| P07 | 758 | 5.7% | 5.7% | +0.8 | n/a | no target |
| P08 | 28706 | 2.6% | 2.6% | +0.5 | n/a | no target |
| P09 | 71 | 11.3% | 11.3% | +5.5 | n/a | no target |
| P10 | 2005 | 4.9% | 4.9% | -0.2 | n/a | no target |
| P11 | 1800 | 4.1% | 4.1% | +0.1 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 209522 | 0.7% | 0.7% | +0.0 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 27.6% | 27.6% | +5.9 | n/a | no target |
| P01T | 203 | 26.1% | 26.1% | -1.8 | 65% | ❌ 39 pts to go |
| P01_GOLD | 645 | 66.2% | 66.2% | -2.4 | 70% | 🟡 4 pts to go |
| P02 | 484 | 23.1% | 23.1% | -0.6 | 50% | ❌ 27 pts to go |
| P03 | 274 | 48.9% | 48.9% | -1.5 | 60% | ❌ 11 pts to go |
| P04 | 4762 | 5.6% | 5.6% | +0.0 | 40% | ❌ 34 pts to go |
| P05 | 429 | 19.6% | 19.6% | -0.3 | 45% | ❌ 25 pts to go |
| P06M | 32175 | 2.6% | 2.6% | +0.9 | n/a | no target |
| P06T | 55107 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06 | 241 | 27.4% | 27.4% | -1.9 | n/a | no target |
| P07 | 758 | 5.0% | 5.0% | -0.1 | n/a | no target |
| P08 | 28706 | 1.1% | 1.1% | +0.2 | n/a | no target |
| P09 | 71 | 31.0% | 31.0% | +20.1 | n/a | no target |
| P10 | 2005 | 3.1% | 3.1% | -0.2 | n/a | no target |
| P11 | 1800 | 3.5% | 3.5% | -0.1 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 209522 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 18.9% | 18.9% | +6.9 | n/a | no target |
| P01T | 203 | 13.3% | 13.3% | +0.6 | n/a | no target |
| P01_GOLD | 645 | 48.8% | 48.8% | -1.4 | 50% | 🟡 1 pts to go |
| P02 | 484 | 36.2% | 36.2% | -1.4 | n/a | no target |
| P03 | 274 | 50.7% | 50.7% | -0.1 | 60% | 🟡 9 pts to go |
| P04 | 4762 | 9.8% | 9.8% | -3.0 | n/a | no target |
| P05 | 429 | 15.2% | 15.2% | +0.0 | n/a | no target |
| P06M | 32175 | 1.1% | 1.1% | +0.3 | n/a | no target |
| P06T | 55107 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 241 | 18.3% | 18.3% | -2.1 | n/a | no target |
| P07 | 758 | 5.3% | 5.3% | -0.4 | n/a | no target |
| P08 | 28706 | 0.5% | 0.5% | +0.1 | n/a | no target |
| P09 | 71 | 23.9% | 23.9% | +3.2 | n/a | no target |
| P10 | 2005 | 2.3% | 2.3% | -0.2 | n/a | no target |
| P11 | 1800 | 2.3% | 2.3% | -0.4 | n/a | no target |
| P12 | 11 | 18.2% | 18.2% | +0.0 | n/a | no target |
| P13 | 209522 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 9.0% | 9.0% | +0.2 | 15% | 🟡 6 pts to go |
| P01T | 203 | 13.3% | 13.3% | +0.6 | 15% | 🟡 2 pts to go |
| P01_GOLD | 645 | 33.5% | 33.5% | -1.6 | 40% | 🟡 6 pts to go |
| P02 | 484 | 11.6% | 11.8% | -0.6 | 25% | ❌ 13 pts to go |
| P03 | 274 | 15.7% | 15.7% | -0.8 | 25% | 🟡 9 pts to go |
| P04 | 4762 | 2.2% | 2.2% | -0.5 | 15% | ❌ 13 pts to go |
| P05 | 429 | 6.5% | 6.5% | -0.1 | 15% | 🟡 8 pts to go |
| P06M | 32175 | 0.8% | 0.8% | +0.0 | 15% | ❌ 14 pts to go |
| P06T | 55107 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P06 | 241 | 9.5% | 9.5% | +0.2 | 15% | 🟡 6 pts to go |
| P07 | 758 | 3.6% | 3.6% | +0.2 | 15% | ❌ 11 pts to go |
| P08 | 28706 | 0.6% | 0.6% | +0.1 | 15% | ❌ 14 pts to go |
| P09 | 71 | 4.2% | 4.2% | +3.1 | 15% | ❌ 11 pts to go |
| P10 | 2005 | 1.3% | 1.3% | -0.1 | 15% | ❌ 14 pts to go |
| P11 | 1800 | 1.3% | 1.3% | +0.1 | 15% | ❌ 14 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 209522 | 0.6% | 0.6% | +0.0 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 8.8% | 8.8% | +3.2 | 15% | 🟡 6 pts to go |
| P01T | 203 | 12.3% | 12.3% | +1.4 | 25% | ❌ 13 pts to go |
| P01_GOLD | 645 | 28.5% | 28.5% | -0.4 | 25% | ✅ met |
| P02 | 484 | 24.2% | 24.2% | -1.2 | 15% | ✅ met |
| P03 | 274 | 21.5% | 21.5% | -0.3 | 15% | ✅ met |
| P04 | 4762 | 3.1% | 3.1% | -0.9 | 15% | ❌ 12 pts to go |
| P05 | 429 | 11.4% | 11.4% | +0.0 | 15% | 🟡 4 pts to go |
| P06M | 32175 | 0.9% | 0.9% | +0.3 | 15% | ❌ 14 pts to go |
| P06T | 55107 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 241 | 7.9% | 7.9% | +0.8 | 15% | 🟡 7 pts to go |
| P07 | 758 | 1.6% | 1.6% | -0.2 | 15% | ❌ 13 pts to go |
| P08 | 28706 | 0.4% | 0.4% | +0.1 | 15% | ❌ 15 pts to go |
| P09 | 71 | 2.8% | 2.8% | +1.3 | 15% | ❌ 12 pts to go |
| P10 | 2005 | 1.5% | 1.5% | -0.1 | 15% | ❌ 14 pts to go |
| P11 | 1800 | 1.8% | 1.8% | +0.0 | 15% | ❌ 13 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 209522 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 2.5% | 2.5% | +0.9 | 20% | ❌ 18 pts to go |
| P01T | 203 | 3.4% | 3.4% | +0.3 | 20% | ❌ 17 pts to go |
| P01_GOLD | 645 | 4.2% | 4.2% | -0.1 | 20% | ❌ 16 pts to go |
| P02 | 484 | 1.4% | 1.4% | -0.1 | 20% | ❌ 19 pts to go |
| P03 | 274 | 1.5% | 1.5% | -0.4 | 20% | ❌ 18 pts to go |
| P04 | 4762 | 0.6% | 0.6% | -0.1 | 20% | ❌ 19 pts to go |
| P05 | 429 | 0.9% | 0.9% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 32175 | 0.1% | 0.1% | +0.1 | 20% | ❌ 20 pts to go |
| P06T | 55107 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 241 | 1.2% | 1.2% | -0.2 | 20% | ❌ 19 pts to go |
| P07 | 758 | 0.3% | 0.3% | +0.1 | 20% | ❌ 20 pts to go |
| P08 | 28706 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P09 | 71 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2005 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 1800 | 0.2% | 0.2% | +0.1 | 20% | ❌ 20 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 209522 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 2.5% | 2.5% | +0.9 | 15% | ❌ 12 pts to go |
| P01T | 203 | 2.5% | 2.5% | -0.6 | 15% | ❌ 12 pts to go |
| P01_GOLD | 645 | 11.2% | 11.2% | +0.7 | 15% | 🟡 4 pts to go |
| P02 | 484 | 10.1% | 10.1% | -1.4 | 15% | 🟡 5 pts to go |
| P03 | 274 | 20.4% | 20.4% | -0.3 | 15% | ✅ met |
| P04 | 4762 | 2.0% | 2.0% | -0.4 | 15% | ❌ 13 pts to go |
| P05 | 429 | 3.0% | 3.0% | +0.2 | 15% | ❌ 12 pts to go |
| P06M | 32175 | 0.5% | 0.5% | +0.1 | 15% | ❌ 14 pts to go |
| P06T | 55107 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 241 | 4.1% | 4.1% | +0.2 | 15% | ❌ 11 pts to go |
| P07 | 758 | 1.8% | 1.8% | +0.6 | 15% | ❌ 13 pts to go |
| P08 | 28706 | 0.4% | 0.4% | +0.1 | 15% | ❌ 15 pts to go |
| P09 | 71 | 2.8% | 2.8% | +2.1 | 15% | ❌ 12 pts to go |
| P10 | 2005 | 1.1% | 1.1% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 1800 | 0.8% | 0.8% | +0.0 | 15% | ❌ 14 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 209522 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 18.7% | 18.7% | +6.3 | 20% | 🟡 1 pts to go |
| P01T | 203 | 14.3% | 14.3% | +0.8 | 40% | ❌ 26 pts to go |
| P01_GOLD | 645 | 45.3% | 45.3% | -1.3 | 40% | ✅ met |
| P02 | 484 | 41.7% | 41.7% | -1.5 | 20% | ✅ met |
| P03 | 274 | 49.3% | 49.3% | +0.8 | 35% | ✅ met |
| P04 | 4762 | 11.5% | 11.5% | -3.4 | 20% | 🟡 8 pts to go |
| P05 | 429 | 15.4% | 15.4% | -0.2 | 20% | 🟡 5 pts to go |
| P06M | 32175 | 1.3% | 1.3% | +0.3 | 20% | ❌ 19 pts to go |
| P06T | 55107 | 0.6% | 0.6% | +0.0 | 20% | ❌ 19 pts to go |
| P06 | 241 | 18.3% | 18.3% | -2.8 | 20% | 🟡 2 pts to go |
| P07 | 758 | 6.2% | 6.2% | +0.1 | 20% | ❌ 14 pts to go |
| P08 | 28706 | 0.9% | 0.9% | +0.1 | 20% | ❌ 19 pts to go |
| P09 | 71 | 12.7% | 12.7% | -8.4 | 20% | 🟡 7 pts to go |
| P10 | 2005 | 3.6% | 3.6% | -0.2 | 20% | ❌ 16 pts to go |
| P11 | 1800 | 3.0% | 3.0% | -0.2 | 20% | ❌ 17 pts to go |
| P12 | 11 | 9.1% | 9.1% | +0.0 | 20% | ❌ 11 pts to go |
| P13 | 209522 | 0.3% | 0.3% | -0.1 | 20% | ❌ 20 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 11.1% | 11.1% | -7.0 | n/a | no target |
| P01T | 203 | 0.5% | 0.5% | +0.1 | n/a | no target |
| P01_GOLD | 645 | 69.6% | 69.6% | -2.0 | 95% | ❌ 25 pts to go |
| P02 | 484 | 63.4% | 63.4% | -2.8 | 95% | ❌ 32 pts to go |
| P03 | 274 | 55.5% | 55.5% | -2.4 | 90% | ❌ 34 pts to go |
| P04 | 4762 | 20.9% | 20.9% | -5.6 | 85% | ❌ 64 pts to go |
| P05 | 429 | 39.4% | 39.4% | +0.5 | 75% | ❌ 36 pts to go |
| P06M | 32175 | 21.7% | 21.7% | -6.4 | n/a | no target |
| P06T | 55107 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 241 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 758 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 28706 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 71 | 77.5% | 77.5% | -11.6 | 100% | ❌ 22 pts to go |
| P10 | 2005 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1800 | 3.9% | 3.9% | +0.1 | 60% | ❌ 56 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 209522 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 11.1% | 11.1% | -7.0 | n/a | no target |
| P01T | 203 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 645 | 70.5% | 70.5% | -3.0 | 100% | ❌ 30 pts to go |
| P02 | 484 | 64.9% | 64.9% | -3.3 | 100% | ❌ 35 pts to go |
| P03 | 274 | 57.7% | 57.7% | -2.8 | n/a | no target |
| P04 | 4762 | 21.2% | 21.2% | -5.8 | 95% | ❌ 74 pts to go |
| P05 | 429 | 35.0% | 35.0% | +0.4 | 80% | ❌ 45 pts to go |
| P06M | 32175 | 21.7% | 21.7% | -6.4 | n/a | no target |
| P06T | 55107 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 241 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 758 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 28706 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 71 | 80.3% | 80.3% | -11.3 | 100% | ❌ 20 pts to go |
| P10 | 2005 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1800 | 4.1% | 4.1% | +0.1 | n/a | no target |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 209522 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 82.5% | 82.5% | -1.8 | n/a | no target |
| P01T | 203 | 0.5% | 0.5% | +0.1 | n/a | no target |
| P01_GOLD | 645 | 54.7% | 54.7% | +2.4 | 85% | ❌ 30 pts to go |
| P02 | 484 | 61.2% | 61.2% | +2.0 | 90% | ❌ 29 pts to go |
| P03 | 274 | 47.1% | 47.1% | +3.1 | 85% | ❌ 38 pts to go |
| P04 | 4762 | 38.2% | 38.2% | +9.1 | 90% | ❌ 52 pts to go |
| P05 | 429 | 33.1% | 33.1% | +0.2 | 75% | ❌ 42 pts to go |
| P06M | 32175 | 83.1% | 83.1% | -1.2 | n/a | no target |
| P06T | 55107 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 241 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 758 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 28706 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 71 | 64.8% | 64.8% | -17.0 | 95% | ❌ 30 pts to go |
| P10 | 2005 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1800 | 3.8% | 3.8% | +0.5 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 209522 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 52.5% | 52.5% | -13.4 | n/a | no target |
| P01T | 203 | 0.5% | 0.5% | +0.1 | n/a | no target |
| P01_GOLD | 645 | 54.1% | 54.1% | +2.1 | 85% | ❌ 31 pts to go |
| P02 | 484 | 55.2% | 55.2% | +1.8 | 90% | ❌ 35 pts to go |
| P03 | 274 | 47.1% | 47.1% | +2.7 | 85% | ❌ 38 pts to go |
| P04 | 4762 | 33.8% | 33.8% | +9.2 | 90% | ❌ 56 pts to go |
| P05 | 429 | 42.0% | 42.0% | -0.7 | 75% | ❌ 33 pts to go |
| P06M | 32175 | 58.9% | 58.9% | -10.3 | n/a | no target |
| P06T | 55107 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 241 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 758 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 28706 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 71 | 1.4% | 1.4% | +1.0 | 95% | ❌ 94 pts to go |
| P10 | 2005 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1800 | 3.0% | 3.0% | +0.5 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 209522 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 97.5% | 97.5% | +2.3 | n/a | no target |
| P01T | 203 | 95.1% | 95.1% | -1.0 | n/a | no target |
| P01_GOLD | 645 | 86.0% | 86.2% | +0.5 | 100% | ❌ 14 pts to go |
| P02 | 484 | 78.3% | 78.3% | +0.7 | 100% | ❌ 22 pts to go |
| P03 | 274 | 92.7% | 92.7% | +0.2 | n/a | no target |
| P04 | 4762 | 53.8% | 53.8% | +3.2 | 95% | ❌ 41 pts to go |
| P05 | 429 | 77.6% | 77.6% | +0.3 | 95% | ❌ 17 pts to go |
| P06M | 32175 | 99.5% | 99.5% | +0.2 | n/a | no target |
| P06T | 55107 | 97.9% | 97.9% | +3.4 | n/a | no target |
| P06 | 241 | 20.3% | 20.3% | -0.1 | n/a | no target |
| P07 | 758 | 10.3% | 10.3% | +0.1 | n/a | no target |
| P08 | 28706 | 4.5% | 4.5% | +0.0 | n/a | no target |
| P09 | 71 | 93.0% | 93.0% | -5.2 | 100% | 🟡 7 pts to go |
| P10 | 2005 | 71.0% | 71.0% | +0.4 | n/a | no target |
| P11 | 1800 | 70.3% | 70.3% | +0.5 | n/a | no target |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 209522 | 99.4% | 99.4% | -0.2 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 97.5% | 97.5% | +2.3 | n/a | no target |
| P01T | 203 | 95.1% | 95.1% | -1.0 | n/a | no target |
| P01_GOLD | 645 | 89.1% | 89.3% | +0.4 | 100% | ❌ 11 pts to go |
| P02 | 484 | 79.5% | 79.5% | +0.7 | 100% | ❌ 20 pts to go |
| P03 | 274 | 93.4% | 93.4% | +0.2 | n/a | no target |
| P04 | 4762 | 56.3% | 56.3% | +2.3 | 95% | ❌ 39 pts to go |
| P05 | 429 | 89.7% | 89.7% | +0.4 | 70% | ✅ met |
| P06M | 32175 | 99.5% | 99.5% | +0.2 | n/a | no target |
| P06T | 55107 | 97.9% | 97.9% | +3.4 | n/a | no target |
| P06 | 241 | 20.3% | 20.3% | -0.1 | n/a | no target |
| P07 | 758 | 10.3% | 10.3% | +0.1 | n/a | no target |
| P08 | 28706 | 4.5% | 4.5% | +0.0 | n/a | no target |
| P09 | 71 | 93.0% | 93.0% | -5.2 | 100% | 🟡 7 pts to go |
| P10 | 2005 | 71.0% | 71.0% | +0.4 | n/a | no target |
| P11 | 1800 | 70.4% | 70.4% | +0.5 | n/a | no target |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 209522 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 203 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 645 | 16.1% | 16.1% | -0.8 | 60% | ❌ 44 pts to go · rows from a source that publishes bids: 362 rows, 28.7% filled |
| P02 | 484 | 9.5% | 9.5% | -1.2 | n/a | no target · rows from a source that publishes bids: 291 rows, 15.8% filled |
| P03 | 274 | 13.1% | 13.1% | -0.8 | n/a | no target · rows from a source that publishes bids: 141 rows, 25.5% filled |
| P04 | 4762 | 1.2% | 1.2% | -0.5 | n/a | no target · rows from a source that publishes bids: 878 rows, 6.5% filled |
| P05 | 429 | 2.6% | 2.6% | +0.0 | n/a | no target · rows from a source that publishes bids: 59 rows, 18.6% filled |
| P06M | 32175 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55107 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 241 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 758 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 28706 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 71 | 5.6% | 5.6% | +1.2 | n/a | no target · rows from a source that publishes bids: 63 rows, 6.3% filled |
| P10 | 2005 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1800 | 0.4% | 0.4% | +0.0 | n/a | no target · rows from a source that publishes bids: 68 rows, 11.8% filled |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 11 rows, 0.0% filled |
| P13 | 209522 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 203 | 0.0% | 97.5% | +0.0 | n/a | no target |
| P01_GOLD | 645 | 51.0% | 82.8% | -2.4 | 90% | ❌ 39 pts to go |
| P02 | 484 | 50.6% | 87.4% | -2.8 | 90% | ❌ 39 pts to go |
| P03 | 274 | 44.2% | 81.0% | -1.7 | 90% | ❌ 46 pts to go |
| P04 | 4762 | 14.8% | 94.8% | -4.8 | 90% | ❌ 75 pts to go |
| P05 | 429 | 0.0% | 81.4% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 32175 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 55107 | 0.0% | 99.9% | +0.0 | n/a | no target |
| P06 | 241 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 758 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 28706 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 71 | 11.3% | 18.3% | +8.4 | 90% | ❌ 79 pts to go |
| P10 | 2005 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1800 | 2.2% | 97.6% | +0.1 | n/a | no target |
| P12 | 11 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 209522 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 203 | 1.0% | 98.5% | +0.1 | n/a | no target |
| P01_GOLD | 645 | 25.4% | 57.2% | -1.1 | 90% | ❌ 65 pts to go |
| P02 | 484 | 50.2% | 87.0% | -2.2 | n/a | no target |
| P03 | 274 | 24.5% | 61.3% | -0.7 | n/a | no target |
| P04 | 4762 | 16.0% | 96.0% | -5.4 | n/a | no target |
| P05 | 429 | 0.5% | 81.8% | +0.0 | n/a | no target |
| P06M | 32175 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 55107 | 0.1% | 99.9% | +0.0 | n/a | no target |
| P06 | 241 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 758 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 28706 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 71 | 2.8% | 9.9% | -37.6 | n/a | no target |
| P10 | 2005 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1800 | 2.3% | 97.7% | +0.1 | n/a | no target |
| P12 | 11 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 209522 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 203 | 2.5% | 100.0% | +0.3 | n/a | no target |
| P01_GOLD | 645 | 50.4% | 82.2% | -1.6 | 95% | ❌ 45 pts to go |
| P02 | 484 | 56.0% | 92.8% | -2.1 | n/a | no target |
| P03 | 274 | 48.2% | 85.0% | -2.2 | n/a | no target |
| P04 | 4762 | 16.5% | 96.5% | -5.7 | n/a | no target |
| P05 | 429 | 5.1% | 86.5% | +0.1 | n/a | no target |
| P06M | 32175 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 55107 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 241 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 758 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 28706 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 71 | 16.9% | 23.9% | -43.5 | n/a | no target |
| P10 | 2005 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1800 | 2.3% | 97.8% | -0.1 | n/a | no target |
| P12 | 11 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 209522 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 203 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 645 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 484 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 274 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4762 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 429 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 32175 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 55107 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 241 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 758 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 28706 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 71 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2005 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1800 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 209522 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 203 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 645 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 484 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 274 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4762 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 429 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 32175 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 55107 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 241 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 758 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 28706 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 71 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2005 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1800 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 209522 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 434 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 203 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 645 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 484 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 274 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4762 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 429 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 32175 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 55107 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 241 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 758 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 28706 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 71 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2005 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1800 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 209522 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

