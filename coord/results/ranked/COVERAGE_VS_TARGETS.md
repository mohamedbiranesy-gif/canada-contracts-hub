# Coverage vs the downstream team's targets — 2026-11-13

Benchmarks (field × package with a numeric target): **92 of 438 met** (21.0%); 64 within 10 points; 282 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 268, P01T 229, P01_GOLD 649, P02 475, P03 272, P04 4163, P05 423, P06M 23004, P06T 61957, P06 270, P07 823, P08 30550, P09 279, P10R 0, P10 2111, P11 1835, P12 10, P13 151276

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 268 | 0.0% | 13.8% | 7 | vendor GST/HST number (251 rows) |
| P01T | 229 | 1.3% | 37.1% | 8 | payment terms (182 rows) |
| P01_GOLD | 649 | 23.7% | 69.5% | 9 | payment terms (240 rows) |
| P02 | 475 | 7.4% | 54.1% | 9 | PO rule (366 rows) |
| P03 | 272 | 14.7% | 54.8% | 9 | PO rule (139 rows) |
| P04 | 4163 | 1.1% | 14.8% | 7 | PO rule (3963 rows) |
| P05 | 423 | 0.9% | 17.0% | 7 | payment terms (352 rows) |
| P06M | 23004 | 0.0% | 2.9% | 7 | PO rule (22628 rows) |
| P06T | 61957 | 0.1% | 13.1% | 7 | PO rule (61577 rows) |
| P06 | 270 | 0.0% | 10.4% | 7 | reference to quote (PO / contract / vendor id) (252 rows) |
| P07 | 823 | 0.0% | 2.9% | 6 | PO rule (783 rows) |
| P08 | 30550 | 0.0% | 1.5% | 6 | PO rule (30287 rows) |
| P09 | 279 | 1.4% | 42.3% | 8 | payment terms (259 rows) |
| P10 | 2111 | 0.0% | 1.2% | 5 | reference to quote (PO / contract / vendor id) (2111 rows) |
| P11 | 1835 | 0.1% | 8.4% | 6 | PO rule (1769 rows) |
| P12 | 10 | 0.0% | 40.0% | 8 | PO rule (10 rows) |
| P13 | 151276 | 0.0% | 0.3% | 7 | reference to quote (PO / contract / vendor id) (151276 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 268 | 10 | 57 | 201 | 0 | 0 | 69 |
| P01T | 229 | 27 | 39 | 163 | 0 | 0 | 68 |
| P01_GOLD | 649 | 256 | 171 | 222 | 0 | 0 | 82 |
| P02 | 475 | 0 | 188 | 287 | 0 | 0 | 66 |
| P03 | 272 | 0 | 0 | 260 | 12 | 0 | 57 |
| P04 | 4163 | 0 | 0 | 3536 | 627 | 0 | 46 |
| P05 | 423 | 16 | 28 | 366 | 13 | 0 | 51 |
| P06M | 23004 | 0 | 17 | 22932 | 55 | 0 | 46 |
| P06T | 61957 | 0 | 29 | 41596 | 20332 | 0 | 38 |
| P06 | 270 | 17 | 40 | 213 | 0 | 0 | 67 |
| P07 | 823 | 0 | 21 | 782 | 20 | 0 | 55 |
| P08 | 30550 | 0 | 0 | 27574 | 2976 | 0 | 46 |
| P09 | 279 | 5 | 10 | 263 | 1 | 0 | 53 |
| P10 | 2111 | 2 | 12 | 1436 | 661 | 0 | 41 |
| P11 | 1835 | 7 | 12 | 39 | 0 | 1777 | 24 |
| P12 | 10 | 0 | 0 | 10 | 0 | 0 | 54 |
| P13 | 151276 | 13 | 63 | 151188 | 12 | 0 | 43 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 268 | 203 | 75.7% | tax treatment (42) |
| P01T | 229 | 140 | 61.1% | bill-to legal name and address (74) |
| P01_GOLD | 649 | 488 | 75.2% | bill-to legal name and address (98) |
| P02 | 475 | 324 | 68.2% | the buyer's PO / reference rule (84) |
| P03 | 272 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (272) |
| P04 | 4163 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (4163) |
| P05 | 423 | 45 | 10.6% | a confirmed invoicing / AP or finance channel (335) |
| P06M | 23004 | 250 | 1.1% | a confirmed invoicing / AP or finance channel (22688) |
| P06T | 61957 | 336 | 0.5% | a confirmed invoicing / AP or finance channel (61143) |
| P06 | 270 | 53 | 19.6% | the buyer's PO / reference rule (115) |
| P07 | 823 | 49 | 6.0% | the buyer's PO / reference rule (329) |
| P08 | 30550 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (30550) |
| P09 | 279 | 40 | 14.3% | a confirmed invoicing / AP or finance channel (228) |
| P10 | 2111 | 5 | 0.2% | a confirmed invoicing / AP or finance channel (2035) |
| P11 | 1835 | 18 | 1.0% | a confirmed invoicing / AP or finance channel (1777) |
| P12 | 10 | 2 | 20.0% | a confirmed invoicing / AP or finance channel (8) |
| P13 | 151276 | 42 | 0.0% | a confirmed invoicing / AP or finance channel (149163) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 268 | 6 | 2.2% | 7 | 0 | the vendor's GST/HST number (BN9) (251) |
| P01T | 229 | 101 | 44.1% | 3 | 0 | the vendor's GST/HST number (BN9) (74) |
| P01_GOLD | 649 | 412 | 63.5% | 11 | 0 | the vendor's GST/HST number (BN9) (160) |
| P02 | 475 | 214 | 45.1% | 21 | 0 | the vendor's GST/HST number (BN9) (212) |
| P03 | 272 | 17 | 6.2% | 0 | 134 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (103) |
| P04 | 4163 | 43 | 1.0% | 7 | 901 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (3155) |
| P05 | 423 | 20 | 4.7% | 8 | 125 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (202) |
| P06M | 23004 | 8 | 0.0% | 12 | 558 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (22036) |
| P06T | 61957 | 389 | 0.6% | 14 | 19319 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (41739) |
| P06 | 270 | 24 | 8.9% | 54 | 0 | the vendor's GST/HST number (BN9) (127) |
| P07 | 823 | 15 | 1.8% | 142 | 37 | the vendor's GST/HST number (BN9) (406) |
| P08 | 30550 | 4 | 0.0% | 13 | 7584 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (22904) |
| P09 | 279 | 37 | 13.3% | 0 | 108 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (108) |
| P10 | 2111 | 6 | 0.3% | 15 | 304 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (1707) |
| P11 | 1835 | 7 | 0.4% | 3 | 0 | a confirmed invoicing / AP or finance channel (1761) |
| P12 | 10 | 1 | 10.0% | 0 | 5 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (3) |
| P13 | 151276 | 21 | 0.0% | 1036 | 60536 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (88446) |
| **all** | 278594 | 1325 | 0.5% | 1346 | 89611 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 258 | 0 | 0 | 0 | 174 | 9 | 0 | 212 | 230 | 1 |
| P01T | 202 | 0 | 0 | 0 | 123 | 66 | 31 | 167 | 184 | 4 |
| P01_GOLD | 393 | 0 | 0 | 0 | 32 | 79 | 31 | 216 | 255 | 3 |
| P02 | 475 | 0 | 475 | 0 | 49 | 54 | 14 | 366 | 294 | 2 |
| P03 | 272 | 0 | 272 | 0 | 25 | 45 | 25 | 139 | 148 | 2 |
| P04 | 4163 | 0 | 4163 | 0 | 2112 | 1265 | 957 | 3963 | 3709 | 32 |
| P05 | 407 | 0 | 355 | 0 | 82 | 95 | 40 | 339 | 354 | 7 |
| P06M | 23004 | 0 | 23004 | 0 | 17205 | 1353 | 136 | 22628 | 22382 | 20 |
| P06T | 61957 | 0 | 61957 | 0 | 55780 | 38797 | 26217 | 61577 | 61048 | 412 |
| P06 | 253 | 0 | 0 | 0 | 138 | 70 | 43 | 193 | 221 | 4 |
| P07 | 823 | 0 | 823 | 0 | 560 | 320 | 116 | 783 | 782 | 5 |
| P08 | 30550 | 0 | 30550 | 0 | 24162 | 13184 | 4656 | 30287 | 29928 | 191 |
| P09 | 274 | 0 | 255 | 0 | 12 | 69 | 1 | 249 | 261 | 7 |
| P10 | 2109 | 0 | 2077 | 0 | 1094 | 1126 | 959 | 2044 | 2004 | 16 |
| P11 | 1828 | 1777 | 1729 | 0 | 928 | 1229 | 557 | 1769 | 1762 | 21 |
| P12 | 10 | 0 | 9 | 0 | 0 | 2 | 0 | 10 | 10 | 1 |
| P13 | 151263 | 0 | 150872 | 0 | 121451 | 79302 | 18 | 150941 | 150165 | 71 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_phone | P13 | 71.9% | 95% | 34883 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 30203 |
| ap_system_hint | P13 | 0.4% | 20% | 29663 |
| buyer_bn_as_published | P13 | 13.9% | 30% | 24280 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 22546 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 22501 |
| buyer_payment_method_preference | P13 | 0.7% | 15% | 21665 |
| buyer_legal_name_as_published | P13 | 47.6% | 60% | 18792 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 12375 |
| ap_system_hint | P06T | 0.6% | 20% | 12042 |
| vendor_registered_address | P08 | 31.2% | 70% | 11847 |
| buyer_logo_url | P13 | 87.2% | 95% | 11837 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 9187 |
| buyer_tax_exempt_status | P06T | 0.2% | 15% | 9176 |
| buyer_payment_method_preference | P06T | 0.7% | 15% | 8877 |
| buyer_phone | P08 | 71.1% | 95% | 7298 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 6098 |
| ap_system_hint | P08 | 0.8% | 20% | 5878 |
| vendor_emails | P08 | 56.0% | 75% | 5806 |
| vendor_bn9 | P08 | 31.7% | 50% | 5591 |
| buyer_legal_name_as_published | P08 | 56.8% | 75% | 5547 |
| vendor_phone | P08 | 67.5% | 85% | 5342 |
| vendor_trading_name | P08 | 34.5% | 50% | 4724 |
| buyer_ap_cycle_published | P06M | 0.1% | 20% | 4588 |
| buyer_esignature_preference | P08 | 0.3% | 15% | 4481 |
| buyer_tax_exempt_status | P08 | 0.3% | 15% | 4477 |
| buyer_payment_method_preference | P08 | 0.6% | 15% | 4399 |
| ap_system_hint | P06M | 1.0% | 20% | 4364 |
| buyer_bn_as_published | P08 | 22.4% | 35% | 3835 |
| invoice_reference_hint | P08 | 12.5% | 25% | 3808 |
| buyer_esignature_preference | P06M | 0.4% | 15% | 3353 |
| buyer_tax_exempt_status | P06M | 0.6% | 15% | 3302 |
| buyer_payment_method_preference | P06M | 0.9% | 15% | 3255 |
| buyer_address | P08 | 84.7% | 95% | 3136 |
| average_contract_duration_days | P04 | 16.9% | 90% | 3044 |
| currency | P04 | 23.6% | 95% | 2974 |
| ap_phone | P04 | 18.4% | 85% | 2773 |
| commodity_codes | P04 | 19.0% | 85% | 2747 |
| award_or_notice_id | P04 | 21.3% | 85% | 2651 |
| contract_value | P04 | 23.2% | 85% | 2575 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 94.0% | 94.0% | +0.8 | 50% | ✅ met |
| P01T | 229 | 95.6% | 95.6% | +0.0 | 50% | ✅ met |
| P01_GOLD | 649 | 92.3% | 94.6% | +0.1 | 95% | 🟡 3 pts to go |
| P02 | 475 | 76.0% | 77.5% | +1.0 | 95% | ❌ 19 pts to go |
| P03 | 272 | 82.0% | 85.3% | +0.4 | 95% | ❌ 13 pts to go |
| P04 | 4163 | 41.7% | 43.2% | +9.9 | 90% | ❌ 48 pts to go |
| P05 | 423 | 39.5% | 42.6% | -0.1 | 70% | ❌ 30 pts to go |
| P06M | 23004 | 93.3% | 93.3% | +0.1 | n/a | no target |
| P06T | 61957 | 99.3% | 99.3% | +0.0 | n/a | no target |
| P06 | 270 | 34.8% | 34.8% | -0.6 | 30% | ✅ met |
| P07 | 823 | 14.0% | 14.0% | -0.2 | 30% | ❌ 16 pts to go |
| P08 | 30550 | 12.5% | 12.5% | +0.3 | 25% | ❌ 12 pts to go |
| P09 | 279 | 98.9% | 99.6% | +0.0 | 100% | 🟡 1 pts to go |
| P10 | 2111 | 3.2% | 3.2% | -0.1 | 25% | ❌ 22 pts to go |
| P11 | 1835 | 55.0% | 55.7% | +0.7 | 60% | 🟡 5 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 151276 | 99.6% | 99.6% | +0.0 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 229 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 649 | 5.7% | 5.7% | +0.0 | 50% | ❌ 44 pts to go |
| P02 | 475 | 5.7% | 5.7% | -0.5 | 50% | ❌ 44 pts to go |
| P03 | 272 | 1.5% | 1.5% | -0.4 | 40% | ❌ 38 pts to go |
| P04 | 4163 | 0.5% | 0.5% | -0.1 | 30% | ❌ 30 pts to go |
| P05 | 423 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 23004 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 61957 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 270 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 823 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30550 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 279 | 0.7% | 0.7% | +0.0 | 50% | ❌ 49 pts to go |
| P10 | 2111 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1835 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 151276 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 90.7% | 90.7% | +1.1 | n/a | no target |
| P01T | 229 | 79.9% | 79.9% | +0.0 | 50% | ✅ met |
| P01_GOLD | 649 | 68.1% | 68.1% | +0.8 | 85% | ❌ 17 pts to go |
| P02 | 475 | 67.4% | 67.4% | +1.2 | 90% | ❌ 23 pts to go |
| P03 | 272 | 62.1% | 62.1% | +1.6 | 85% | ❌ 23 pts to go |
| P04 | 4163 | 39.4% | 39.4% | +10.3 | 85% | ❌ 46 pts to go |
| P05 | 423 | 30.0% | 30.0% | +0.1 | 60% | ❌ 30 pts to go |
| P06M | 23004 | 93.1% | 93.1% | +0.1 | n/a | no target |
| P06T | 61957 | 99.3% | 99.3% | +0.1 | n/a | no target |
| P06 | 270 | 6.7% | 6.7% | +0.3 | n/a | no target |
| P07 | 823 | 9.1% | 9.1% | +0.0 | n/a | no target |
| P08 | 30550 | 11.7% | 11.7% | +0.4 | n/a | no target |
| P09 | 279 | 95.7% | 95.7% | +0.1 | 100% | 🟡 4 pts to go |
| P10 | 2111 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1835 | 52.3% | 52.3% | +0.8 | 60% | 🟡 8 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 151276 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 229 | 0.0% | 0.0% | +0.0 | 30% | ❌ 30 pts to go |
| P01_GOLD | 649 | 49.9% | 49.9% | -1.8 | 80% | ❌ 30 pts to go |
| P02 | 475 | 56.8% | 56.8% | -1.3 | 60% | 🟡 3 pts to go |
| P03 | 272 | 48.9% | 48.9% | -1.5 | 80% | ❌ 31 pts to go |
| P04 | 4163 | 20.5% | 20.5% | -3.5 | 50% | ❌ 30 pts to go |
| P05 | 423 | 12.5% | 12.5% | -0.1 | 40% | ❌ 28 pts to go |
| P06M | 23004 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 61957 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 270 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 823 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30550 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 279 | 81.4% | 81.4% | +0.3 | 50% | ✅ met |
| P10 | 2111 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1835 | 3.3% | 3.3% | +0.0 | 40% | ❌ 37 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 151276 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 229 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P01_GOLD | 649 | 59.2% | 59.2% | -1.7 | 85% | ❌ 26 pts to go |
| P02 | 475 | 56.8% | 56.8% | -1.3 | 90% | ❌ 33 pts to go |
| P03 | 272 | 57.4% | 57.4% | -2.0 | 85% | ❌ 28 pts to go |
| P04 | 4163 | 21.3% | 21.3% | -3.6 | 85% | ❌ 64 pts to go |
| P05 | 423 | 20.3% | 20.3% | -0.1 | 50% | ❌ 30 pts to go |
| P06M | 23004 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 61957 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 270 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 823 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30550 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 279 | 97.1% | 97.1% | +0.0 | 100% | 🟡 3 pts to go |
| P10 | 2111 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1835 | 3.7% | 3.7% | +0.1 | 60% | ❌ 56 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 151276 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 229 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 649 | 12.6% | 12.6% | +0.0 | 60% | ❌ 47 pts to go |
| P02 | 475 | 6.7% | 6.7% | -0.6 | 50% | ❌ 43 pts to go |
| P03 | 272 | 8.1% | 8.1% | -0.5 | 50% | ❌ 42 pts to go |
| P04 | 4163 | 1.6% | 1.6% | -0.3 | 40% | ❌ 38 pts to go |
| P05 | 423 | 0.7% | 0.7% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 23004 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 61957 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 270 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 823 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30550 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 279 | 3.2% | 3.2% | -0.4 | 50% | ❌ 47 pts to go |
| P10 | 2111 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1835 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 151276 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 229 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 649 | 34.8% | 34.8% | -1.1 | 80% | ❌ 45 pts to go |
| P02 | 475 | 51.4% | 51.4% | -1.6 | 90% | ❌ 39 pts to go |
| P03 | 272 | 32.7% | 32.7% | -1.1 | 80% | ❌ 47 pts to go |
| P04 | 4163 | 19.0% | 19.0% | -3.2 | 85% | ❌ 66 pts to go |
| P05 | 423 | 6.4% | 6.4% | +0.0 | 50% | ❌ 44 pts to go |
| P06M | 23004 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 61957 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 270 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 823 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30550 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 279 | 73.8% | 73.8% | +0.7 | 95% | ❌ 21 pts to go |
| P10 | 2111 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1835 | 2.7% | 2.7% | +0.1 | 50% | ❌ 47 pts to go |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 151276 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 229 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 649 | 8.0% | 8.0% | -0.1 | 50% | ❌ 42 pts to go |
| P02 | 475 | 5.7% | 5.7% | -0.5 | 50% | ❌ 44 pts to go |
| P03 | 272 | 2.2% | 2.2% | -0.4 | 30% | ❌ 28 pts to go |
| P04 | 4163 | 0.5% | 0.5% | -0.1 | 30% | ❌ 30 pts to go |
| P05 | 423 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 23004 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 61957 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 270 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 823 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30550 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 279 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P10 | 2111 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1835 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 151276 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 229 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 649 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 475 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 272 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4163 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 423 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 23004 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 61957 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 270 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 823 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 30550 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 279 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2111 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1835 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 151276 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 6.3% | 6.3% | -0.1 | 70% | ❌ 64 pts to go |
| P01T | 229 | 60.3% | 60.3% | +0.0 | 60% | ✅ met |
| P01_GOLD | 649 | 73.0% | 73.0% | -1.8 | 90% | ❌ 17 pts to go |
| P02 | 475 | 52.8% | 52.8% | -1.5 | 85% | ❌ 32 pts to go |
| P03 | 272 | 64.7% | 64.7% | -2.2 | 90% | ❌ 25 pts to go |
| P04 | 4163 | 32.8% | 32.8% | -5.4 | 75% | ❌ 42 pts to go |
| P05 | 423 | 54.4% | 54.4% | -0.3 | 50% | ✅ met |
| P06M | 23004 | 2.9% | 2.9% | +0.0 | n/a | no target |
| P06T | 61957 | 65.7% | 65.7% | +1.2 | n/a | no target |
| P06 | 270 | 42.2% | 42.2% | +0.1 | 40% | ✅ met |
| P07 | 823 | 32.3% | 32.3% | +0.2 | 50% | ❌ 18 pts to go |
| P08 | 30550 | 31.7% | 31.7% | +1.1 | 50% | ❌ 18 pts to go |
| P09 | 279 | 56.6% | 56.6% | -0.1 | 80% | ❌ 23 pts to go |
| P10 | 2111 | 38.8% | 38.8% | +0.0 | 40% | 🟡 1 pts to go |
| P11 | 1835 | 54.9% | 54.9% | +0.3 | 60% | 🟡 5 pts to go |
| P12 | 10 | 60.0% | 60.0% | +14.5 | 85% | ❌ 25 pts to go |
| P13 | 151276 | 44.8% | 44.8% | +0.0 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 44.0% | 44.0% | -2.6 | n/a | no target |
| P01T | 229 | 60.7% | 60.7% | +0.9 | n/a | no target |
| P01_GOLD | 649 | 73.8% | 73.8% | +0.9 | 95% | ❌ 21 pts to go |
| P02 | 475 | 75.6% | 75.6% | +1.0 | 95% | ❌ 19 pts to go |
| P03 | 272 | 70.2% | 70.2% | +0.7 | 95% | ❌ 25 pts to go |
| P04 | 4163 | 59.7% | 59.7% | +6.6 | 95% | ❌ 35 pts to go |
| P05 | 423 | 58.4% | 58.4% | +0.3 | 70% | ❌ 12 pts to go |
| P06M | 23004 | 40.7% | 40.7% | -0.6 | n/a | no target |
| P06T | 61957 | 71.6% | 71.6% | +4.1 | n/a | no target |
| P06 | 270 | 38.5% | 38.5% | +0.3 | 80% | ❌ 42 pts to go |
| P07 | 823 | 31.2% | 31.2% | +0.2 | 70% | ❌ 39 pts to go |
| P08 | 30550 | 31.2% | 31.2% | +1.5 | 70% | ❌ 39 pts to go |
| P09 | 279 | 86.7% | 86.7% | +0.5 | 100% | ❌ 13 pts to go |
| P10 | 2111 | 39.4% | 39.4% | +0.2 | 70% | ❌ 31 pts to go |
| P11 | 1835 | 59.8% | 59.8% | +1.2 | 75% | ❌ 15 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 151276 | 40.2% | 40.2% | +0.0 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 20.1% | 20.1% | -2.0 | n/a | no target |
| P01T | 229 | 64.6% | 64.6% | -0.9 | n/a | no target |
| P01_GOLD | 649 | 50.4% | 50.4% | +1.6 | 60% | 🟡 10 pts to go |
| P02 | 475 | 57.5% | 57.5% | +1.7 | 60% | 🟡 2 pts to go |
| P03 | 272 | 53.7% | 53.7% | +1.4 | 60% | 🟡 6 pts to go |
| P04 | 4163 | 50.5% | 50.5% | +7.9 | 55% | 🟡 4 pts to go |
| P05 | 423 | 23.4% | 23.4% | +0.7 | 50% | ❌ 27 pts to go |
| P06M | 23004 | 9.6% | 9.6% | +0.1 | n/a | no target |
| P06T | 61957 | 65.8% | 65.8% | -2.1 | n/a | no target |
| P06 | 270 | 50.4% | 50.4% | +1.8 | n/a | no target |
| P07 | 823 | 40.2% | 40.2% | +0.6 | 55% | ❌ 15 pts to go |
| P08 | 30550 | 34.5% | 34.5% | +1.5 | 50% | ❌ 16 pts to go |
| P09 | 279 | 72.8% | 72.8% | +0.8 | 70% | ✅ met |
| P10 | 2111 | 48.0% | 48.0% | -0.1 | 55% | 🟡 7 pts to go |
| P11 | 1835 | 59.5% | 59.5% | +0.3 | 50% | ✅ met |
| P12 | 10 | 90.0% | 90.0% | -0.9 | n/a | no target |
| P13 | 151276 | 3.2% | 3.2% | +0.0 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 30.2% | 30.2% | -3.1 | n/a | no target |
| P01T | 229 | 79.5% | 79.5% | +0.0 | n/a | no target |
| P01_GOLD | 649 | 48.7% | 48.7% | -1.7 | 70% | ❌ 21 pts to go |
| P02 | 475 | 55.4% | 55.4% | -1.4 | 70% | ❌ 15 pts to go |
| P03 | 272 | 48.9% | 48.9% | -1.5 | 70% | ❌ 21 pts to go |
| P04 | 4163 | 47.0% | 47.0% | -7.9 | 65% | ❌ 18 pts to go |
| P05 | 423 | 29.3% | 29.3% | +0.2 | 60% | ❌ 31 pts to go |
| P06M | 23004 | 26.8% | 26.8% | -0.6 | n/a | no target |
| P06T | 61957 | 83.3% | 83.3% | +0.6 | n/a | no target |
| P06 | 270 | 71.5% | 71.5% | +2.2 | 40% | ✅ met |
| P07 | 823 | 67.1% | 67.1% | +2.1 | 85% | ❌ 18 pts to go |
| P08 | 30550 | 67.5% | 67.5% | +3.5 | 85% | ❌ 18 pts to go |
| P09 | 279 | 56.6% | 56.6% | +0.2 | 85% | ❌ 28 pts to go |
| P10 | 2111 | 66.0% | 66.0% | -0.1 | 85% | ❌ 19 pts to go |
| P11 | 1835 | 68.7% | 68.7% | +0.6 | 75% | 🟡 6 pts to go |
| P12 | 10 | 40.0% | 40.0% | +3.6 | n/a | no target |
| P13 | 151276 | 91.8% | 91.8% | +0.0 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 34.3% | 34.3% | -3.5 | n/a | no target |
| P01T | 229 | 98.3% | 98.3% | +0.0 | n/a | no target |
| P01_GOLD | 649 | 76.1% | 76.1% | -2.5 | 90% | ❌ 14 pts to go |
| P02 | 475 | 79.6% | 79.6% | -2.2 | 90% | ❌ 10 pts to go |
| P03 | 272 | 83.1% | 83.1% | -2.2 | 90% | 🟡 7 pts to go |
| P04 | 4163 | 70.7% | 70.7% | -12.1 | 85% | ❌ 14 pts to go |
| P05 | 423 | 44.7% | 44.7% | +0.2 | 70% | ❌ 25 pts to go |
| P06M | 23004 | 32.3% | 32.3% | -0.7 | n/a | no target |
| P06T | 61957 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 270 | 99.3% | 99.3% | +0.0 | 50% | ✅ met |
| P07 | 823 | 99.9% | 99.9% | +0.0 | 100% | 🟡 0 pts to go |
| P08 | 30550 | 99.9% | 99.9% | +0.0 | 100% | 🟡 0 pts to go |
| P09 | 279 | 78.1% | 78.1% | +0.3 | 100% | ❌ 22 pts to go |
| P10 | 2111 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1835 | 97.7% | 97.7% | -0.3 | 100% | 🟡 2 pts to go |
| P12 | 10 | 60.0% | 60.0% | +5.5 | n/a | no target |
| P13 | 151276 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 14.6% | 14.6% | -1.5 | n/a | no target |
| P01T | 229 | 59.4% | 59.4% | -0.4 | n/a | no target |
| P01_GOLD | 649 | 41.8% | 41.8% | -1.6 | 70% | ❌ 28 pts to go |
| P02 | 475 | 46.1% | 46.1% | -1.1 | 75% | ❌ 29 pts to go |
| P03 | 272 | 44.1% | 44.1% | -0.6 | 75% | ❌ 31 pts to go |
| P04 | 4163 | 33.3% | 33.3% | -5.4 | 70% | ❌ 37 pts to go |
| P05 | 423 | 21.5% | 21.5% | +0.2 | 55% | ❌ 34 pts to go |
| P06M | 23004 | 5.9% | 5.9% | +0.0 | n/a | no target |
| P06T | 61957 | 46.2% | 46.2% | -1.2 | n/a | no target |
| P06 | 270 | 51.9% | 51.9% | +0.8 | n/a | no target |
| P07 | 823 | 53.6% | 53.6% | +0.9 | 70% | ❌ 16 pts to go |
| P08 | 30550 | 56.0% | 56.0% | +1.2 | 75% | ❌ 19 pts to go |
| P09 | 279 | 47.3% | 47.3% | +0.4 | 85% | ❌ 38 pts to go |
| P10 | 2111 | 44.5% | 44.5% | +0.1 | 80% | ❌ 36 pts to go |
| P11 | 1835 | 53.2% | 53.2% | -0.1 | 70% | ❌ 17 pts to go |
| P12 | 10 | 30.0% | 30.0% | +2.7 | n/a | no target |
| P13 | 151276 | 5.5% | 5.5% | +0.0 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 34.3% | 34.3% | -3.5 | n/a | no target |
| P01T | 229 | 96.5% | 96.5% | +0.0 | n/a | no target |
| P01_GOLD | 649 | 70.6% | 70.6% | -2.3 | 90% | ❌ 19 pts to go |
| P02 | 475 | 74.5% | 74.5% | -2.2 | 90% | ❌ 16 pts to go |
| P03 | 272 | 79.8% | 79.8% | -2.2 | 90% | ❌ 10 pts to go |
| P04 | 4163 | 66.4% | 66.4% | -11.3 | 85% | ❌ 19 pts to go |
| P05 | 423 | 43.3% | 43.3% | +0.4 | 75% | ❌ 32 pts to go |
| P06M | 23004 | 32.2% | 32.2% | -0.7 | n/a | no target |
| P06T | 61957 | 98.4% | 98.4% | +0.1 | n/a | no target |
| P06 | 270 | 92.2% | 92.2% | +2.2 | n/a | no target |
| P07 | 823 | 94.0% | 94.0% | +2.3 | 100% | 🟡 6 pts to go |
| P08 | 30550 | 92.3% | 92.3% | +5.0 | 100% | 🟡 8 pts to go |
| P09 | 279 | 66.7% | 66.7% | +0.2 | n/a | no target |
| P10 | 2111 | 90.2% | 90.2% | -0.1 | 100% | 🟡 10 pts to go |
| P11 | 1835 | 90.8% | 90.8% | +0.6 | n/a | no target |
| P12 | 10 | 60.0% | 60.0% | +5.5 | n/a | no target |
| P13 | 151276 | 69.8% | 69.8% | +0.0 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 34.0% | 34.0% | -2.9 | n/a | no target · QC vendors: 48 rows, 100.0% filled |
| P01T | 229 | 20.1% | 20.1% | +0.4 | n/a | no target · QC vendors: 34 rows, 88.2% filled |
| P01_GOLD | 649 | 44.7% | 44.7% | +1.2 | 95% | ❌ 50 pts to go · QC vendors: 48 rows, 97.9% filled |
| P02 | 475 | 57.9% | 57.9% | +1.9 | 95% | ❌ 37 pts to go · QC vendors: 110 rows, 100.0% filled |
| P03 | 272 | 43.8% | 43.8% | +0.9 | 95% | ❌ 51 pts to go · QC vendors: 18 rows, 100.0% filled |
| P04 | 4163 | 41.8% | 41.8% | +9.4 | 95% | ❌ 53 pts to go · QC vendors: 596 rows, 98.0% filled |
| P05 | 423 | 14.4% | 14.4% | +0.4 | n/a | no target · QC vendors: 37 rows, 100.0% filled |
| P06M | 23004 | 36.8% | 36.8% | -0.7 | n/a | no target · QC vendors: 6662 rows, 99.9% filled |
| P06T | 61957 | 32.5% | 32.5% | +1.9 | n/a | no target · QC vendors: 20437 rows, 96.0% filled |
| P06 | 270 | 7.4% | 7.4% | +0.3 | n/a | no target · QC vendors: 12 rows, 66.7% filled |
| P07 | 823 | 6.9% | 6.9% | +0.0 | n/a | no target · QC vendors: 47 rows, 78.7% filled |
| P08 | 30550 | 7.0% | 7.0% | +0.0 | n/a | no target · QC vendors: 1827 rows, 92.7% filled |
| P09 | 279 | 74.2% | 74.2% | +0.7 | 95% | ❌ 21 pts to go · QC vendors: 102 rows, 100.0% filled |
| P10 | 2111 | 15.6% | 15.6% | -0.1 | n/a | no target · QC vendors: 201 rows, 92.5% filled |
| P11 | 1835 | 19.8% | 19.8% | +0.2 | n/a | no target · QC vendors: 307 rows, 94.1% filled |
| P12 | 10 | 80.0% | 80.0% | -1.8 | n/a | no target · QC vendors: 2 rows, 100.0% filled |
| P13 | 151276 | 22.2% | 22.2% | +0.0 | n/a | no target · QC vendors: 33552 rows, 100.0% filled |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 43.7% | 43.7% | -2.5 | n/a | no target · vendors with a registry record: 117 rows, 100.0% filled |
| P01T | 229 | 60.7% | 60.7% | +0.9 | n/a | no target · vendors with a registry record: 139 rows, 100.0% filled |
| P01_GOLD | 649 | 81.7% | 81.7% | +0.8 | 100% | ❌ 18 pts to go · vendors with a registry record: 530 rows, 100.0% filled |
| P02 | 475 | 79.2% | 79.2% | +0.8 | 100% | ❌ 21 pts to go · vendors with a registry record: 376 rows, 100.0% filled |
| P03 | 272 | 78.7% | 78.7% | +0.5 | 100% | ❌ 21 pts to go · vendors with a registry record: 214 rows, 100.0% filled |
| P04 | 4163 | 60.5% | 60.5% | +6.5 | 100% | ❌ 40 pts to go · vendors with a registry record: 2517 rows, 100.0% filled |
| P05 | 423 | 62.9% | 62.9% | +0.1 | n/a | no target · vendors with a registry record: 266 rows, 100.0% filled |
| P06M | 23004 | 40.7% | 40.7% | -0.5 | n/a | no target · vendors with a registry record: 9353 rows, 100.0% filled |
| P06T | 61957 | 71.7% | 71.7% | +4.1 | n/a | no target · vendors with a registry record: 44413 rows, 100.0% filled |
| P06 | 270 | 39.3% | 39.3% | +0.0 | n/a | no target · vendors with a registry record: 106 rows, 100.0% filled |
| P07 | 823 | 31.8% | 31.8% | +0.0 | n/a | no target · vendors with a registry record: 262 rows, 100.0% filled |
| P08 | 30550 | 31.3% | 31.3% | +1.3 | n/a | no target · vendors with a registry record: 9558 rows, 100.0% filled |
| P09 | 279 | 90.0% | 90.0% | +0.5 | n/a | no target · vendors with a registry record: 251 rows, 100.0% filled |
| P10 | 2111 | 40.3% | 40.3% | +0.2 | n/a | no target · vendors with a registry record: 851 rows, 100.0% filled |
| P11 | 1835 | 60.5% | 60.5% | +1.2 | n/a | no target · vendors with a registry record: 1111 rows, 100.0% filled |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 10 rows, 100.0% filled |
| P13 | 151276 | 40.2% | 40.2% | +0.0 | n/a | no target · vendors with a registry record: 60821 rows, 100.0% filled |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 96.6% | 96.6% | +0.2 | 90% | ✅ met |
| P01T | 229 | 71.2% | 71.2% | +0.5 | 90% | ❌ 19 pts to go |
| P01_GOLD | 649 | 87.8% | 87.8% | +0.4 | 95% | 🟡 7 pts to go |
| P02 | 475 | 88.6% | 88.6% | +0.4 | 95% | 🟡 6 pts to go |
| P03 | 272 | 83.5% | 83.5% | +0.4 | 85% | 🟡 2 pts to go |
| P04 | 4163 | 69.6% | 69.6% | +5.1 | 90% | ❌ 20 pts to go |
| P05 | 423 | 77.5% | 77.5% | -0.5 | 75% | ✅ met |
| P06M | 23004 | 94.1% | 94.1% | +0.3 | n/a | no target |
| P06T | 61957 | 37.4% | 37.4% | +0.5 | n/a | no target |
| P06 | 270 | 74.1% | 74.1% | +3.0 | 80% | 🟡 6 pts to go |
| P07 | 823 | 61.1% | 61.2% | +2.9 | 80% | ❌ 19 pts to go |
| P08 | 30550 | 56.8% | 56.9% | +4.9 | 75% | ❌ 18 pts to go |
| P09 | 279 | 75.3% | 75.3% | -0.3 | 95% | ❌ 20 pts to go |
| P10 | 2111 | 46.7% | 46.7% | -0.1 | 70% | ❌ 23 pts to go |
| P11 | 1835 | 33.0% | 33.0% | +1.2 | 65% | ❌ 32 pts to go |
| P12 | 10 | 80.0% | 80.0% | +7.3 | 80% | ✅ met |
| P13 | 151276 | 47.6% | 47.6% | +2.0 | 60% | ❌ 12 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 20.5% | 20.5% | +2.0 | 50% | ❌ 30 pts to go |
| P01T | 229 | 16.6% | 16.6% | +0.4 | n/a | no target |
| P01_GOLD | 649 | 19.1% | 19.1% | -0.7 | 40% | ❌ 21 pts to go |
| P02 | 475 | 20.0% | 20.0% | +0.1 | 40% | ❌ 20 pts to go |
| P03 | 272 | 19.9% | 19.9% | -0.4 | 40% | ❌ 20 pts to go |
| P04 | 4163 | 15.0% | 15.0% | -1.3 | 40% | ❌ 25 pts to go |
| P05 | 423 | 21.3% | 21.3% | +0.4 | 25% | 🟡 4 pts to go |
| P06M | 23004 | 25.3% | 25.3% | +4.9 | n/a | no target |
| P06T | 61957 | 10.1% | 10.1% | +2.6 | n/a | no target |
| P06 | 270 | 21.1% | 21.1% | +3.6 | 35% | ❌ 14 pts to go |
| P07 | 823 | 23.0% | 23.0% | +3.9 | 35% | ❌ 12 pts to go |
| P08 | 30550 | 22.4% | 22.4% | +4.7 | 35% | ❌ 13 pts to go |
| P09 | 279 | 16.5% | 16.5% | -0.2 | n/a | no target |
| P10 | 2111 | 9.4% | 9.4% | +2.3 | 30% | ❌ 21 pts to go |
| P11 | 1835 | 10.1% | 10.1% | +3.6 | n/a | no target |
| P12 | 10 | 20.0% | 20.0% | +1.8 | n/a | no target |
| P13 | 151276 | 13.9% | 13.9% | +1.4 | 30% | ❌ 16 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 229 | 85.2% | 85.2% | +0.0 | 100% | ❌ 15 pts to go |
| P01_GOLD | 649 | 91.4% | 91.4% | +0.3 | 100% | 🟡 9 pts to go |
| P02 | 475 | 96.6% | 96.6% | +0.0 | 100% | 🟡 3 pts to go |
| P03 | 272 | 89.7% | 89.7% | +0.2 | 100% | ❌ 10 pts to go |
| P04 | 4163 | 76.5% | 76.5% | +4.0 | 100% | ❌ 24 pts to go |
| P05 | 423 | 89.8% | 89.8% | -0.2 | 100% | ❌ 10 pts to go |
| P06M | 23004 | 99.4% | 99.4% | +0.0 | n/a | no target |
| P06T | 61957 | 57.7% | 57.7% | -1.0 | n/a | no target |
| P06 | 270 | 82.6% | 82.6% | +0.5 | 95% | ❌ 12 pts to go |
| P07 | 823 | 85.7% | 85.7% | +0.3 | 95% | 🟡 9 pts to go |
| P08 | 30550 | 84.7% | 84.7% | +0.2 | 95% | ❌ 10 pts to go |
| P09 | 279 | 96.4% | 96.4% | +0.0 | 100% | 🟡 4 pts to go |
| P10 | 2111 | 54.5% | 54.5% | -0.1 | 95% | ❌ 40 pts to go |
| P11 | 1835 | 60.9% | 60.9% | +0.0 | 80% | ❌ 19 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 151276 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 78.0% | 78.0% | +6.9 | n/a | no target |
| P01T | 229 | 74.2% | 74.2% | +0.0 | n/a | no target |
| P01_GOLD | 649 | 72.1% | 72.1% | -1.1 | 90% | ❌ 18 pts to go |
| P02 | 475 | 76.8% | 76.8% | -1.6 | 95% | ❌ 18 pts to go |
| P03 | 272 | 72.1% | 72.1% | -2.0 | 95% | ❌ 23 pts to go |
| P04 | 4163 | 61.1% | 61.1% | -8.4 | 95% | ❌ 34 pts to go |
| P05 | 423 | 72.3% | 72.3% | -0.2 | 90% | ❌ 18 pts to go |
| P06M | 23004 | 81.0% | 81.0% | +4.3 | n/a | no target |
| P06T | 61957 | 59.6% | 59.6% | +1.0 | n/a | no target |
| P06 | 270 | 71.5% | 71.5% | +6.1 | 95% | ❌ 24 pts to go |
| P07 | 823 | 68.0% | 68.0% | +8.3 | 90% | ❌ 22 pts to go |
| P08 | 30550 | 71.1% | 71.1% | +12.5 | 95% | ❌ 24 pts to go |
| P09 | 279 | 86.0% | 86.0% | +0.2 | 100% | ❌ 14 pts to go |
| P10 | 2111 | 53.7% | 53.7% | -0.1 | 95% | ❌ 41 pts to go |
| P11 | 1835 | 33.8% | 33.8% | +3.1 | 75% | ❌ 41 pts to go |
| P12 | 10 | 80.0% | 80.0% | -1.8 | n/a | no target |
| P13 | 151276 | 71.9% | 71.9% | +4.0 | 95% | ❌ 23 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 91.0% | 91.0% | +7.5 | n/a | no target |
| P01T | 229 | 92.1% | 92.1% | +0.4 | 95% | 🟡 3 pts to go |
| P01_GOLD | 649 | 83.2% | 83.2% | -1.8 | 90% | 🟡 7 pts to go |
| P02 | 475 | 88.6% | 88.6% | -2.4 | 95% | 🟡 6 pts to go |
| P03 | 272 | 82.0% | 82.0% | -1.8 | 95% | ❌ 13 pts to go |
| P04 | 4163 | 80.3% | 80.3% | -11.3 | 90% | 🟡 10 pts to go |
| P05 | 423 | 92.7% | 92.7% | +0.3 | 95% | 🟡 2 pts to go |
| P06M | 23004 | 94.3% | 94.3% | +9.0 | n/a | no target |
| P06T | 61957 | 88.3% | 88.3% | +3.7 | n/a | no target |
| P06 | 270 | 93.7% | 93.7% | +8.3 | 100% | 🟡 6 pts to go |
| P07 | 823 | 94.5% | 94.5% | +10.9 | 100% | 🟡 6 pts to go |
| P08 | 30550 | 95.1% | 95.1% | +17.3 | 100% | 🟡 5 pts to go |
| P09 | 279 | 73.8% | 73.8% | -0.4 | n/a | no target |
| P10 | 2111 | 94.4% | 94.4% | +0.0 | 100% | 🟡 6 pts to go |
| P11 | 1835 | 55.7% | 55.7% | +4.6 | 80% | ❌ 24 pts to go |
| P12 | 10 | 90.0% | 90.0% | -0.9 | n/a | no target |
| P13 | 151276 | 87.2% | 87.2% | +6.4 | 95% | 🟡 8 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 3.4% | 3.4% | +0.2 | n/a | no target |
| P01T | 229 | 8.7% | 8.7% | +0.0 | n/a | no target |
| P01_GOLD | 649 | 13.4% | 13.4% | -0.6 | 25% | ❌ 12 pts to go |
| P02 | 475 | 24.4% | 24.4% | -0.4 | 40% | ❌ 16 pts to go |
| P03 | 272 | 8.5% | 8.5% | -0.5 | 20% | ❌ 12 pts to go |
| P04 | 4163 | 3.2% | 3.2% | -0.1 | 20% | ❌ 17 pts to go |
| P05 | 423 | 3.3% | 3.3% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 23004 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 61957 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06 | 270 | 5.6% | 5.6% | +0.2 | n/a | no target |
| P07 | 823 | 8.0% | 8.0% | +0.1 | n/a | no target |
| P08 | 30550 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 279 | 8.2% | 8.2% | +0.6 | n/a | no target |
| P10 | 2111 | 0.8% | 0.8% | +0.0 | n/a | no target |
| P11 | 1835 | 0.7% | 0.7% | +0.0 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 151276 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 15.3% | 15.3% | -0.8 | n/a | no target |
| P01T | 229 | 19.2% | 19.2% | +0.0 | 70% | ❌ 51 pts to go |
| P01_GOLD | 649 | 42.4% | 42.4% | +0.3 | 80% | ❌ 38 pts to go |
| P02 | 475 | 56.2% | 56.2% | -1.1 | 90% | ❌ 34 pts to go |
| P03 | 272 | 18.4% | 18.4% | -0.8 | 60% | ❌ 42 pts to go |
| P04 | 4163 | 18.4% | 18.4% | -1.8 | 85% | ❌ 67 pts to go |
| P05 | 423 | 11.8% | 11.8% | +0.7 | 50% | ❌ 38 pts to go |
| P06M | 23004 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06T | 61957 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P06 | 270 | 13.3% | 13.3% | +0.1 | n/a | no target |
| P07 | 823 | 9.2% | 9.2% | +0.1 | n/a | no target |
| P08 | 30550 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P09 | 279 | 74.9% | 74.9% | +2.9 | 95% | ❌ 20 pts to go |
| P10 | 2111 | 1.6% | 1.6% | +0.0 | n/a | no target |
| P11 | 1835 | 13.4% | 13.4% | +0.4 | n/a | no target |
| P12 | 10 | 30.0% | 30.0% | +2.7 | n/a | no target |
| P13 | 151276 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 5.6% | 5.6% | +0.0 | n/a | no target |
| P01T | 229 | 9.6% | 9.6% | +0.4 | n/a | no target |
| P01_GOLD | 649 | 33.6% | 33.6% | -0.2 | 70% | ❌ 36 pts to go |
| P02 | 475 | 38.3% | 38.3% | -0.4 | 75% | ❌ 37 pts to go |
| P03 | 272 | 18.8% | 18.8% | -0.4 | 55% | ❌ 36 pts to go |
| P04 | 4163 | 18.4% | 18.4% | -1.8 | 75% | ❌ 57 pts to go |
| P05 | 423 | 10.9% | 10.9% | +0.7 | 50% | ❌ 39 pts to go |
| P06M | 23004 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06T | 61957 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 270 | 5.2% | 5.2% | -0.5 | n/a | no target |
| P07 | 823 | 4.6% | 4.6% | +0.0 | n/a | no target |
| P08 | 30550 | 0.1% | 0.1% | -0.1 | n/a | no target |
| P09 | 279 | 71.7% | 71.7% | +3.0 | 95% | ❌ 23 pts to go |
| P10 | 2111 | 0.8% | 0.8% | +0.0 | n/a | no target |
| P11 | 1835 | 13.1% | 13.1% | +0.3 | n/a | no target |
| P12 | 10 | 20.0% | 20.0% | +1.8 | n/a | no target |
| P13 | 151276 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 7.1% | 7.1% | -0.5 | n/a | no target |
| P01T | 229 | 8.7% | 8.7% | +0.0 | n/a | no target |
| P01_GOLD | 649 | 56.4% | 56.5% | -0.7 | 80% | ❌ 24 pts to go |
| P02 | 475 | 44.4% | 44.6% | -0.9 | 75% | ❌ 31 pts to go |
| P03 | 272 | 35.3% | 35.3% | -0.8 | 70% | ❌ 35 pts to go |
| P04 | 4163 | 18.3% | 18.6% | -1.6 | 70% | ❌ 52 pts to go |
| P05 | 423 | 14.4% | 14.4% | +0.4 | 50% | ❌ 36 pts to go |
| P06M | 23004 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 61957 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06 | 270 | 13.7% | 13.7% | +0.5 | n/a | no target |
| P07 | 823 | 1.0% | 1.0% | -0.1 | n/a | no target |
| P08 | 30550 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P09 | 279 | 48.4% | 49.1% | +1.5 | 80% | ❌ 32 pts to go |
| P10 | 2111 | 1.1% | 1.1% | +0.0 | n/a | no target |
| P11 | 1835 | 4.5% | 4.6% | +0.0 | n/a | no target |
| P12 | 10 | 30.0% | 30.0% | -6.4 | n/a | no target |
| P13 | 151276 | 0.1% | 0.1% | +0.0 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 14.2% | 14.2% | -0.7 | n/a | no target |
| P01T | 229 | 19.7% | 19.7% | +0.5 | 60% | ❌ 40 pts to go |
| P01_GOLD | 649 | 60.7% | 60.7% | -1.5 | 70% | 🟡 9 pts to go |
| P02 | 475 | 38.1% | 38.1% | -1.4 | 50% | ❌ 12 pts to go |
| P03 | 272 | 45.6% | 45.6% | -2.1 | 55% | 🟡 9 pts to go |
| P04 | 4163 | 10.9% | 10.9% | -1.6 | 40% | ❌ 29 pts to go |
| P05 | 423 | 16.3% | 16.3% | -0.3 | 40% | ❌ 24 pts to go |
| P06M | 23004 | 2.7% | 2.7% | -0.1 | n/a | no target |
| P06T | 61957 | 1.5% | 1.5% | +0.0 | n/a | no target |
| P06 | 270 | 18.1% | 18.1% | -0.1 | n/a | no target |
| P07 | 823 | 5.0% | 5.0% | +0.1 | n/a | no target |
| P08 | 30550 | 2.0% | 2.0% | -0.1 | n/a | no target |
| P09 | 279 | 6.5% | 6.5% | +0.7 | n/a | no target |
| P10 | 2111 | 5.1% | 5.1% | +0.0 | n/a | no target |
| P11 | 1835 | 4.0% | 4.0% | +0.0 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 151276 | 0.7% | 0.7% | +0.0 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 20.9% | 20.9% | -0.8 | n/a | no target |
| P01T | 229 | 27.1% | 27.1% | -0.8 | 65% | ❌ 38 pts to go |
| P01_GOLD | 649 | 66.7% | 66.7% | -1.9 | 70% | 🟡 3 pts to go |
| P02 | 475 | 22.9% | 22.9% | -0.8 | 50% | ❌ 27 pts to go |
| P03 | 272 | 48.9% | 48.9% | -1.5 | 60% | ❌ 11 pts to go |
| P04 | 4163 | 4.8% | 4.8% | -0.8 | 40% | ❌ 35 pts to go |
| P05 | 423 | 19.9% | 19.9% | +0.0 | 45% | ❌ 25 pts to go |
| P06M | 23004 | 1.6% | 1.6% | -0.1 | n/a | no target |
| P06T | 61957 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06 | 270 | 28.5% | 28.5% | -0.8 | n/a | no target |
| P07 | 823 | 4.9% | 4.9% | -0.2 | n/a | no target |
| P08 | 30550 | 0.9% | 0.9% | +0.0 | n/a | no target |
| P09 | 279 | 10.8% | 10.8% | -0.1 | n/a | no target |
| P10 | 2111 | 3.2% | 3.2% | -0.1 | n/a | no target |
| P11 | 1835 | 3.6% | 3.6% | +0.0 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 151276 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 12.3% | 12.3% | +0.3 | n/a | no target |
| P01T | 229 | 12.7% | 12.7% | +0.0 | n/a | no target |
| P01_GOLD | 649 | 48.2% | 48.2% | -2.0 | 50% | 🟡 2 pts to go |
| P02 | 475 | 37.3% | 37.3% | -0.3 | n/a | no target |
| P03 | 272 | 49.6% | 49.6% | -1.2 | 60% | ❌ 10 pts to go |
| P04 | 4163 | 10.9% | 10.9% | -1.9 | n/a | no target |
| P05 | 423 | 15.4% | 15.4% | +0.2 | n/a | no target |
| P06M | 23004 | 0.7% | 0.7% | -0.1 | n/a | no target |
| P06T | 61957 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 270 | 20.0% | 20.0% | -0.4 | n/a | no target |
| P07 | 823 | 5.2% | 5.2% | -0.5 | n/a | no target |
| P08 | 30550 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P09 | 279 | 20.8% | 20.8% | +0.1 | n/a | no target |
| P10 | 2111 | 2.4% | 2.4% | -0.1 | n/a | no target |
| P11 | 1835 | 2.6% | 2.6% | -0.1 | n/a | no target |
| P12 | 10 | 20.0% | 20.0% | +1.8 | n/a | no target |
| P13 | 151276 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 8.6% | 8.6% | -0.2 | 15% | 🟡 6 pts to go |
| P01T | 229 | 12.7% | 12.7% | +0.0 | 15% | 🟡 2 pts to go |
| P01_GOLD | 649 | 34.1% | 34.1% | -1.0 | 40% | 🟡 6 pts to go |
| P02 | 475 | 11.8% | 12.0% | -0.4 | 25% | ❌ 13 pts to go |
| P03 | 272 | 15.8% | 15.8% | -0.7 | 25% | 🟡 9 pts to go |
| P04 | 4163 | 2.4% | 2.4% | -0.3 | 15% | ❌ 13 pts to go |
| P05 | 423 | 6.4% | 6.4% | -0.2 | 15% | 🟡 9 pts to go |
| P06M | 23004 | 0.9% | 0.9% | +0.1 | 15% | ❌ 14 pts to go |
| P06T | 61957 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P06 | 270 | 9.6% | 9.6% | +0.3 | 15% | 🟡 5 pts to go |
| P07 | 823 | 3.3% | 3.3% | -0.1 | 15% | ❌ 12 pts to go |
| P08 | 30550 | 0.6% | 0.6% | +0.1 | 15% | ❌ 14 pts to go |
| P09 | 279 | 1.1% | 1.1% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2111 | 1.4% | 1.4% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 1835 | 1.3% | 1.3% | +0.1 | 15% | ❌ 14 pts to go |
| P12 | 10 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 151276 | 0.7% | 0.7% | +0.1 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 6.3% | 6.3% | +0.7 | 15% | 🟡 9 pts to go |
| P01T | 229 | 10.9% | 10.9% | +0.0 | 25% | ❌ 14 pts to go |
| P01_GOLD | 649 | 27.9% | 27.9% | -1.0 | 25% | ✅ met |
| P02 | 475 | 24.6% | 24.6% | -0.8 | 15% | ✅ met |
| P03 | 272 | 21.7% | 21.7% | -0.1 | 15% | ✅ met |
| P04 | 4163 | 3.5% | 3.5% | -0.5 | 15% | ❌ 12 pts to go |
| P05 | 423 | 11.6% | 11.6% | +0.2 | 15% | 🟡 3 pts to go |
| P06M | 23004 | 0.6% | 0.6% | +0.0 | 15% | ❌ 14 pts to go |
| P06T | 61957 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 270 | 6.7% | 6.7% | -0.4 | 15% | 🟡 8 pts to go |
| P07 | 823 | 1.8% | 1.8% | +0.0 | 15% | ❌ 13 pts to go |
| P08 | 30550 | 0.3% | 0.3% | +0.0 | 15% | ❌ 15 pts to go |
| P09 | 279 | 1.4% | 1.4% | -0.1 | 15% | ❌ 14 pts to go |
| P10 | 2111 | 1.6% | 1.6% | +0.0 | 15% | ❌ 13 pts to go |
| P11 | 1835 | 1.8% | 1.8% | +0.0 | 15% | ❌ 13 pts to go |
| P12 | 10 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 151276 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 1.9% | 1.9% | +0.3 | 20% | ❌ 18 pts to go |
| P01T | 229 | 3.1% | 3.1% | +0.0 | 20% | ❌ 17 pts to go |
| P01_GOLD | 649 | 4.2% | 4.2% | -0.1 | 20% | ❌ 16 pts to go |
| P02 | 475 | 1.5% | 1.5% | +0.0 | 20% | ❌ 18 pts to go |
| P03 | 272 | 1.8% | 1.8% | -0.1 | 20% | ❌ 18 pts to go |
| P04 | 4163 | 0.6% | 0.6% | -0.1 | 20% | ❌ 19 pts to go |
| P05 | 423 | 0.9% | 0.9% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 23004 | 0.1% | 0.1% | +0.1 | 20% | ❌ 20 pts to go |
| P06T | 61957 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 270 | 1.5% | 1.5% | +0.1 | 20% | ❌ 18 pts to go |
| P07 | 823 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P08 | 30550 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P09 | 279 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2111 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 1835 | 0.1% | 0.1% | +0.0 | 20% | ❌ 20 pts to go |
| P12 | 10 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 151276 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 1.5% | 1.5% | -0.1 | 15% | ❌ 14 pts to go |
| P01T | 229 | 3.1% | 3.1% | +0.0 | 15% | ❌ 12 pts to go |
| P01_GOLD | 649 | 10.3% | 10.3% | -0.2 | 15% | 🟡 5 pts to go |
| P02 | 475 | 10.9% | 10.9% | -0.6 | 15% | 🟡 4 pts to go |
| P03 | 272 | 20.2% | 20.2% | -0.5 | 15% | ✅ met |
| P04 | 4163 | 2.0% | 2.0% | -0.4 | 15% | ❌ 13 pts to go |
| P05 | 423 | 2.8% | 2.8% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 23004 | 0.4% | 0.4% | +0.0 | 15% | ❌ 15 pts to go |
| P06T | 61957 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 270 | 4.1% | 4.1% | +0.2 | 15% | ❌ 11 pts to go |
| P07 | 823 | 1.2% | 1.2% | +0.0 | 15% | ❌ 14 pts to go |
| P08 | 30550 | 0.3% | 0.3% | +0.0 | 15% | ❌ 15 pts to go |
| P09 | 279 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2111 | 1.1% | 1.1% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 1835 | 0.8% | 0.8% | +0.0 | 15% | ❌ 14 pts to go |
| P12 | 10 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 151276 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 12.3% | 12.3% | -0.1 | 20% | 🟡 8 pts to go |
| P01T | 229 | 13.5% | 13.5% | +0.0 | 40% | ❌ 26 pts to go |
| P01_GOLD | 649 | 44.7% | 44.7% | -1.9 | 40% | ✅ met |
| P02 | 475 | 42.9% | 42.9% | -0.3 | 20% | ✅ met |
| P03 | 272 | 47.1% | 47.1% | -1.4 | 35% | ✅ met |
| P04 | 4163 | 12.8% | 12.8% | -2.1 | 20% | 🟡 7 pts to go |
| P05 | 423 | 15.8% | 15.8% | +0.2 | 20% | 🟡 4 pts to go |
| P06M | 23004 | 1.0% | 1.0% | +0.0 | 20% | ❌ 19 pts to go |
| P06T | 61957 | 0.6% | 0.6% | +0.0 | 20% | ❌ 19 pts to go |
| P06 | 270 | 20.4% | 20.4% | -0.7 | 20% | ✅ met |
| P07 | 823 | 5.7% | 5.7% | -0.4 | 20% | ❌ 14 pts to go |
| P08 | 30550 | 0.8% | 0.8% | +0.0 | 20% | ❌ 19 pts to go |
| P09 | 279 | 21.1% | 21.1% | +0.0 | 20% | ✅ met |
| P10 | 2111 | 3.7% | 3.7% | -0.1 | 20% | ❌ 16 pts to go |
| P11 | 1835 | 3.2% | 3.2% | +0.0 | 20% | ❌ 17 pts to go |
| P12 | 10 | 10.0% | 10.0% | +0.9 | 20% | 🟡 10 pts to go |
| P13 | 151276 | 0.4% | 0.4% | +0.0 | 20% | ❌ 20 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 16.4% | 16.4% | -1.7 | n/a | no target |
| P01T | 229 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P01_GOLD | 649 | 69.6% | 69.6% | -2.0 | 95% | ❌ 25 pts to go |
| P02 | 475 | 64.2% | 64.2% | -2.0 | 95% | ❌ 31 pts to go |
| P03 | 272 | 55.9% | 55.9% | -2.0 | 90% | ❌ 34 pts to go |
| P04 | 4163 | 23.2% | 23.2% | -3.3 | 85% | ❌ 62 pts to go |
| P05 | 423 | 39.0% | 39.0% | +0.1 | 75% | ❌ 36 pts to go |
| P06M | 23004 | 27.3% | 27.3% | -0.8 | n/a | no target |
| P06T | 61957 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 270 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 823 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30550 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 279 | 89.6% | 89.6% | +0.5 | 100% | ❌ 10 pts to go |
| P10 | 2111 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1835 | 3.9% | 3.9% | +0.1 | 60% | ❌ 56 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 151276 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 16.4% | 16.4% | -1.7 | n/a | no target |
| P01T | 229 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 649 | 71.3% | 71.3% | -2.2 | 100% | ❌ 29 pts to go |
| P02 | 475 | 66.3% | 66.3% | -1.9 | 100% | ❌ 34 pts to go |
| P03 | 272 | 58.5% | 58.5% | -2.0 | n/a | no target |
| P04 | 4163 | 23.6% | 23.6% | -3.4 | 95% | ❌ 71 pts to go |
| P05 | 423 | 34.8% | 34.8% | +0.2 | 80% | ❌ 45 pts to go |
| P06M | 23004 | 27.3% | 27.3% | -0.8 | n/a | no target |
| P06T | 61957 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 270 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 823 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30550 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 279 | 92.1% | 92.1% | +0.5 | 100% | 🟡 8 pts to go |
| P10 | 2111 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1835 | 4.0% | 4.0% | +0.0 | n/a | no target |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 151276 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 84.0% | 84.0% | -0.3 | n/a | no target |
| P01T | 229 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P01_GOLD | 649 | 53.8% | 53.8% | +1.5 | 85% | ❌ 31 pts to go |
| P02 | 475 | 60.2% | 60.2% | +1.0 | 90% | ❌ 30 pts to go |
| P03 | 272 | 46.0% | 46.0% | +2.0 | 85% | ❌ 39 pts to go |
| P04 | 4163 | 39.4% | 39.4% | +10.3 | 90% | ❌ 51 pts to go |
| P05 | 423 | 33.3% | 33.3% | +0.4 | 75% | ❌ 42 pts to go |
| P06M | 23004 | 84.0% | 84.0% | -0.3 | n/a | no target |
| P06T | 61957 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 270 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 823 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30550 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 279 | 82.4% | 82.4% | +0.6 | 95% | ❌ 13 pts to go |
| P10 | 2111 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1835 | 3.6% | 3.6% | +0.3 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 151276 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 61.6% | 61.6% | -4.3 | n/a | no target |
| P01T | 229 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P01_GOLD | 649 | 53.6% | 53.6% | +1.6 | 85% | ❌ 31 pts to go |
| P02 | 475 | 54.5% | 54.5% | +1.1 | 90% | ❌ 36 pts to go |
| P03 | 272 | 46.3% | 46.3% | +1.9 | 85% | ❌ 39 pts to go |
| P04 | 4163 | 35.1% | 35.1% | +10.5 | 90% | ❌ 55 pts to go |
| P05 | 423 | 42.6% | 42.6% | -0.1 | 75% | ❌ 32 pts to go |
| P06M | 23004 | 67.4% | 67.4% | -1.8 | n/a | no target |
| P06T | 61957 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 270 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 823 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30550 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 279 | 0.4% | 0.4% | +0.0 | 95% | ❌ 95 pts to go |
| P10 | 2111 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1835 | 2.8% | 2.8% | +0.3 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 151276 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 95.5% | 95.5% | +0.3 | n/a | no target |
| P01T | 229 | 96.1% | 96.1% | +0.0 | n/a | no target |
| P01_GOLD | 649 | 85.8% | 86.0% | +0.3 | 100% | ❌ 14 pts to go |
| P02 | 475 | 78.5% | 78.5% | +0.9 | 100% | ❌ 22 pts to go |
| P03 | 272 | 92.6% | 92.6% | +0.1 | n/a | no target |
| P04 | 4163 | 57.8% | 57.8% | +7.2 | 95% | ❌ 37 pts to go |
| P05 | 423 | 77.3% | 77.3% | +0.0 | 95% | ❌ 18 pts to go |
| P06M | 23004 | 99.3% | 99.3% | +0.0 | n/a | no target |
| P06T | 61957 | 94.7% | 94.7% | +0.2 | n/a | no target |
| P06 | 270 | 21.1% | 21.1% | +0.7 | n/a | no target |
| P07 | 823 | 10.3% | 10.3% | +0.1 | n/a | no target |
| P08 | 30550 | 4.5% | 4.5% | +0.0 | n/a | no target |
| P09 | 279 | 98.2% | 98.2% | +0.0 | 100% | 🟡 2 pts to go |
| P10 | 2111 | 70.5% | 70.5% | -0.1 | n/a | no target |
| P11 | 1835 | 70.0% | 70.0% | +0.2 | n/a | no target |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 151276 | 99.6% | 99.6% | +0.0 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 95.5% | 95.5% | +0.3 | n/a | no target |
| P01T | 229 | 96.1% | 96.1% | +0.0 | n/a | no target |
| P01_GOLD | 649 | 88.9% | 89.1% | +0.2 | 100% | ❌ 11 pts to go |
| P02 | 475 | 79.8% | 79.8% | +1.0 | 100% | ❌ 20 pts to go |
| P03 | 272 | 93.4% | 93.4% | +0.2 | n/a | no target |
| P04 | 4163 | 60.7% | 60.7% | +6.7 | 95% | ❌ 34 pts to go |
| P05 | 423 | 89.6% | 89.6% | +0.3 | 70% | ✅ met |
| P06M | 23004 | 99.3% | 99.3% | +0.0 | n/a | no target |
| P06T | 61957 | 94.7% | 94.7% | +0.2 | n/a | no target |
| P06 | 270 | 21.1% | 21.1% | +0.7 | n/a | no target |
| P07 | 823 | 10.3% | 10.3% | +0.1 | n/a | no target |
| P08 | 30550 | 4.5% | 4.5% | +0.0 | n/a | no target |
| P09 | 279 | 98.2% | 98.2% | +0.0 | 100% | 🟡 2 pts to go |
| P10 | 2111 | 70.5% | 70.5% | -0.1 | n/a | no target |
| P11 | 1835 | 70.0% | 70.0% | +0.1 | n/a | no target |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 151276 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 229 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 649 | 16.3% | 16.3% | -0.6 | 60% | ❌ 44 pts to go · rows from a source that publishes bids: 368 rows, 28.8% filled |
| P02 | 475 | 10.3% | 10.3% | -0.4 | n/a | no target · rows from a source that publishes bids: 295 rows, 16.6% filled |
| P03 | 272 | 13.2% | 13.2% | -0.7 | n/a | no target · rows from a source that publishes bids: 141 rows, 25.5% filled |
| P04 | 4163 | 1.5% | 1.5% | -0.2 | n/a | no target · rows from a source that publishes bids: 878 rows, 6.9% filled |
| P05 | 423 | 2.6% | 2.6% | +0.0 | n/a | no target · rows from a source that publishes bids: 55 rows, 20.0% filled |
| P06M | 23004 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 61957 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 270 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 823 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30550 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 279 | 3.9% | 3.9% | -0.5 | n/a | no target · rows from a source that publishes bids: 266 rows, 4.1% filled |
| P10 | 2111 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1835 | 0.4% | 0.4% | +0.0 | n/a | no target · rows from a source that publishes bids: 69 rows, 11.6% filled |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 10 rows, 0.0% filled |
| P13 | 151276 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 229 | 0.0% | 97.8% | +0.0 | n/a | no target |
| P01_GOLD | 649 | 51.8% | 82.7% | -1.6 | 90% | ❌ 38 pts to go |
| P02 | 475 | 51.8% | 87.2% | -1.6 | 90% | ❌ 38 pts to go |
| P03 | 272 | 44.5% | 80.5% | -1.4 | 90% | ❌ 46 pts to go |
| P04 | 4163 | 16.9% | 94.0% | -2.7 | 90% | ❌ 73 pts to go |
| P05 | 423 | 0.0% | 82.3% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 23004 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 61957 | 0.0% | 99.9% | +0.0 | n/a | no target |
| P06 | 270 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 823 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 30550 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 279 | 2.9% | 4.7% | +0.0 | 90% | ❌ 87 pts to go |
| P10 | 2111 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1835 | 2.2% | 97.7% | +0.1 | n/a | no target |
| P12 | 10 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 151276 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 229 | 0.9% | 98.7% | +0.0 | n/a | no target |
| P01_GOLD | 649 | 25.6% | 56.5% | -0.9 | 90% | ❌ 64 pts to go |
| P02 | 475 | 50.7% | 86.1% | -1.7 | n/a | no target |
| P03 | 272 | 24.6% | 60.7% | -0.6 | n/a | no target |
| P04 | 4163 | 18.3% | 95.4% | -3.1 | n/a | no target |
| P05 | 423 | 0.5% | 82.7% | +0.0 | n/a | no target |
| P06M | 23004 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 61957 | 0.1% | 99.9% | +0.0 | n/a | no target |
| P06 | 270 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 823 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 30550 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 279 | 40.9% | 42.7% | +0.5 | n/a | no target |
| P10 | 2111 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1835 | 2.3% | 97.8% | +0.1 | n/a | no target |
| P12 | 10 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 151276 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 229 | 2.2% | 100.0% | +0.0 | n/a | no target |
| P01_GOLD | 649 | 50.7% | 81.7% | -1.3 | 95% | ❌ 44 pts to go |
| P02 | 475 | 56.2% | 91.6% | -1.9 | n/a | no target |
| P03 | 272 | 48.5% | 84.6% | -1.9 | n/a | no target |
| P04 | 4163 | 19.0% | 96.1% | -3.2 | n/a | no target |
| P05 | 423 | 5.0% | 87.2% | +0.0 | n/a | no target |
| P06M | 23004 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 61957 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 270 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 823 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 30550 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 279 | 60.6% | 62.4% | +0.2 | n/a | no target |
| P10 | 2111 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1835 | 2.3% | 97.8% | -0.1 | n/a | no target |
| P12 | 10 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 151276 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 229 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 649 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 475 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 272 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4163 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 423 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 23004 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 61957 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 270 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 823 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 30550 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 279 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2111 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1835 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 10 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 151276 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 229 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 649 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 475 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 272 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4163 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 423 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 23004 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 61957 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 270 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 823 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 30550 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 279 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2111 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1835 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 10 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 151276 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 268 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 229 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 649 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 475 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 272 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4163 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 423 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 23004 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 61957 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 270 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 823 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 30550 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 279 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2111 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1835 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 10 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 151276 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

