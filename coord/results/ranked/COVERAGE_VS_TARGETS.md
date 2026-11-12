# Coverage vs the downstream team's targets — 2026-11-12

Benchmarks (field × package with a numeric target): **46 of 438 met** (10.5%); 105 within 10 points; 287 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 131, P01T 194, P01_GOLD 627, P02 466, P03 265, P04 3733, P05 424, P06M 15579, P06T 40041, P06 272, P07 697, P08 22230, P09 307, P10R 0, P10 2389, P11 1527, P12 15, P13 117988

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 131 | 0.0% | 19.8% | 8 | vendor GST/HST number (116 rows) |
| P01T | 194 | 1.0% | 31.4% | 8 | payment terms (153 rows) |
| P01_GOLD | 627 | 25.0% | 71.8% | 10 | payment terms (215 rows) |
| P02 | 466 | 7.5% | 55.2% | 9 | PO rule (353 rows) |
| P03 | 265 | 14.7% | 57.0% | 9 | payment terms (132 rows) |
| P04 | 3733 | 1.3% | 16.7% | 6 | PO rule (3534 rows) |
| P05 | 424 | 1.2% | 17.7% | 7 | payment terms (350 rows) |
| P06M | 15579 | 0.0% | 3.0% | 7 | PO rule (15373 rows) |
| P06T | 40041 | 0.0% | 9.1% | 6 | PO rule (39795 rows) |
| P06 | 272 | 0.0% | 11.4% | 6 | reference to quote (PO / contract / vendor id) (272 rows) |
| P07 | 697 | 0.0% | 2.4% | 6 | reference to quote (PO / contract / vendor id) (697 rows) |
| P08 | 22230 | 0.0% | 0.6% | 6 | reference to quote (PO / contract / vendor id) (22230 rows) |
| P09 | 307 | 1.3% | 45.3% | 8 | payment terms (286 rows) |
| P10 | 2389 | 0.0% | 1.0% | 5 | reference to quote (PO / contract / vendor id) (2389 rows) |
| P11 | 1527 | 0.4% | 7.1% | 5 | PO rule (1453 rows) |
| P12 | 15 | 0.0% | 53.3% | 9 | PO rule (14 rows) |
| P13 | 117988 | 0.0% | 0.2% | 6 | reference to quote (PO / contract / vendor id) (117988 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 131 | 8 | 26 | 97 | 0 | 0 | 71 |
| P01T | 194 | 24 | 32 | 138 | 0 | 0 | 70 |
| P01_GOLD | 627 | 228 | 202 | 197 | 0 | 0 | 82 |
| P02 | 466 | 0 | 196 | 270 | 0 | 0 | 66 |
| P03 | 265 | 0 | 0 | 251 | 14 | 0 | 57 |
| P04 | 3733 | 0 | 0 | 3015 | 718 | 0 | 46 |
| P05 | 424 | 15 | 30 | 366 | 13 | 0 | 51 |
| P06M | 15579 | 0 | 10 | 15490 | 79 | 0 | 46 |
| P06T | 40041 | 0 | 24 | 25689 | 14328 | 0 | 38 |
| P06 | 272 | 16 | 50 | 206 | 0 | 0 | 70 |
| P07 | 697 | 0 | 20 | 653 | 24 | 0 | 54 |
| P08 | 22230 | 0 | 0 | 18861 | 3369 | 0 | 43 |
| P09 | 307 | 4 | 12 | 290 | 1 | 0 | 53 |
| P10 | 2389 | 3 | 13 | 1601 | 772 | 0 | 41 |
| P11 | 1527 | 7 | 15 | 43 | 0 | 1462 | 23 |
| P12 | 15 | 0 | 0 | 15 | 0 | 0 | 54 |
| P13 | 117988 | 9 | 61 | 117901 | 17 | 0 | 43 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 131 | 108 | 82.4% | the buyer's PO / reference rule (12) |
| P01T | 194 | 114 | 58.8% | bill-to legal name and address (66) |
| P01_GOLD | 627 | 475 | 75.8% | bill-to legal name and address (95) |
| P02 | 466 | 315 | 67.6% | the buyer's PO / reference rule (82) |
| P03 | 265 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (265) |
| P04 | 3733 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (3733) |
| P05 | 424 | 47 | 11.1% | a confirmed invoicing / AP or finance channel (337) |
| P06M | 15579 | 164 | 1.1% | a confirmed invoicing / AP or finance channel (15371) |
| P06T | 40041 | 227 | 0.6% | a confirmed invoicing / AP or finance channel (39455) |
| P06 | 272 | 46 | 16.9% | the buyer's PO / reference rule (115) |
| P07 | 697 | 6 | 0.9% | bill-to legal name and address (271) |
| P08 | 22230 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (22230) |
| P09 | 307 | 42 | 13.7% | a confirmed invoicing / AP or finance channel (255) |
| P10 | 2389 | 7 | 0.3% | a confirmed invoicing / AP or finance channel (2301) |
| P11 | 1527 | 14 | 0.9% | a confirmed invoicing / AP or finance channel (1462) |
| P12 | 15 | 4 | 26.7% | a confirmed invoicing / AP or finance channel (10) |
| P13 | 117988 | 40 | 0.0% | a confirmed invoicing / AP or finance channel (116054) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 131 | 6 | 4.6% | 7 | 0 | the vendor's GST/HST number (BN9) (114) |
| P01T | 194 | 70 | 36.1% | 4 | 0 | the vendor's GST/HST number (BN9) (69) |
| P01_GOLD | 627 | 408 | 65.1% | 11 | 0 | the vendor's GST/HST number (BN9) (144) |
| P02 | 466 | 211 | 45.3% | 21 | 0 | the vendor's GST/HST number (BN9) (198) |
| P03 | 265 | 17 | 6.4% | 0 | 137 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (90) |
| P04 | 3733 | 43 | 1.2% | 7 | 865 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2761) |
| P05 | 424 | 20 | 4.7% | 8 | 122 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (207) |
| P06M | 15579 | 6 | 0.0% | 11 | 402 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (14923) |
| P06T | 40041 | 225 | 0.6% | 16 | 9333 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (30061) |
| P06 | 272 | 28 | 10.3% | 51 | 0 | the vendor's GST/HST number (BN9) (115) |
| P07 | 697 | 6 | 0.9% | 111 | 35 | the vendor's GST/HST number (BN9) (305) |
| P08 | 22230 | 3 | 0.0% | 14 | 4920 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (17247) |
| P09 | 307 | 40 | 13.0% | 1 | 125 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (121) |
| P10 | 2389 | 7 | 0.3% | 15 | 302 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (1973) |
| P11 | 1527 | 9 | 0.6% | 3 | 0 | a confirmed invoicing / AP or finance channel (1445) |
| P12 | 15 | 3 | 20.0% | 0 | 6 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (4) |
| P13 | 117988 | 11 | 0.0% | 612 | 31277 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (84612) |
| **all** | 206885 | 1113 | 0.5% | 892 | 47524 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 123 | 0 | 0 | 0 | 69 | 8 | 0 | 103 | 107 | 4 |
| P01T | 170 | 0 | 0 | 0 | 93 | 57 | 30 | 139 | 154 | 7 |
| P01_GOLD | 399 | 0 | 0 | 0 | 12 | 76 | 31 | 195 | 229 | 60 |
| P02 | 466 | 0 | 466 | 0 | 40 | 54 | 21 | 353 | 281 | 22 |
| P03 | 265 | 0 | 265 | 0 | 17 | 43 | 27 | 127 | 138 | 26 |
| P04 | 3733 | 0 | 3733 | 0 | 1626 | 1398 | 1072 | 3534 | 3279 | 170 |
| P05 | 409 | 0 | 357 | 0 | 79 | 89 | 43 | 341 | 352 | 51 |
| P06M | 15579 | 0 | 15579 | 0 | 10200 | 1260 | 131 | 15373 | 15252 | 219 |
| P06T | 40041 | 0 | 40041 | 0 | 35003 | 26502 | 17578 | 39795 | 39435 | 929 |
| P06 | 256 | 0 | 0 | 0 | 117 | 73 | 53 | 179 | 214 | 9 |
| P07 | 697 | 0 | 697 | 0 | 442 | 282 | 134 | 651 | 652 | 13 |
| P08 | 22230 | 0 | 22230 | 0 | 16859 | 10306 | 4865 | 21946 | 21594 | 430 |
| P09 | 303 | 0 | 282 | 0 | 9 | 71 | 2 | 277 | 289 | 46 |
| P10 | 2386 | 0 | 2352 | 0 | 1194 | 1298 | 1109 | 2319 | 2280 | 123 |
| P11 | 1520 | 1462 | 1416 | 0 | 658 | 1072 | 606 | 1453 | 1451 | 60 |
| P12 | 15 | 0 | 13 | 0 | 1 | 3 | 0 | 14 | 14 | 1 |
| P13 | 117979 | 0 | 117594 | 0 | 90027 | 70601 | 24 | 117675 | 116946 | 34 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_phone | P13 | 58.6% | 95% | 42932 |
| buyer_logo_url | P13 | 69.5% | 95% | 30138 |
| buyer_bn_as_published | P13 | 10.0% | 30% | 23624 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 23569 |
| buyer_legal_name_as_published | P13 | 40.2% | 60% | 23406 |
| ap_system_hint | P13 | 0.4% | 20% | 23095 |
| mta_sts | P13 | 83.5% | 100% | 19512 |
| tls_rpt | P13 | 83.5% | 100% | 19512 |
| bimi | P13 | 83.5% | 100% | 19512 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 17587 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 17546 |
| buyer_payment_method_preference | P13 | 0.6% | 15% | 17008 |
| vendor_registered_address | P08 | 30.3% | 70% | 8818 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 7999 |
| ap_system_hint | P06T | 0.6% | 20% | 7771 |
| buyer_phone | P08 | 66.7% | 95% | 6293 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 5935 |
| buyer_tax_exempt_status | P06T | 0.2% | 15% | 5925 |
| buyer_payment_method_preference | P06T | 0.5% | 15% | 5823 |
| invoice_reference_hint | P08 | 1.3% | 25% | 5274 |
| buyer_legal_name_as_published | P08 | 53.6% | 75% | 4749 |
| vendor_emails | P08 | 54.8% | 75% | 4501 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 4435 |
| buyer_bn_as_published | P08 | 15.2% | 35% | 4407 |
| vendor_phone | P08 | 65.3% | 85% | 4372 |
| vendor_bn9 | P08 | 30.5% | 50% | 4339 |
| ap_system_hint | P08 | 1.0% | 20% | 4219 |
| mta_sts | P06T | 90.1% | 100% | 3950 |
| tls_rpt | P06T | 90.1% | 100% | 3950 |
| bimi | P06T | 90.1% | 100% | 3950 |
| buyer_address | P08 | 78.1% | 95% | 3758 |
| buyer_esignature_preference | P08 | 0.5% | 15% | 3231 |
| buyer_tax_exempt_status | P08 | 0.5% | 15% | 3222 |
| buyer_payment_method_preference | P08 | 0.6% | 15% | 3198 |
| buyer_ap_cycle_published | P06M | 0.0% | 20% | 3110 |
| vendor_trading_name | P08 | 36.1% | 50% | 3091 |
| ap_system_hint | P06M | 0.8% | 20% | 2991 |
| average_contract_duration_days | P04 | 19.0% | 90% | 2649 |
| currency | P04 | 25.4% | 95% | 2598 |
| end_date | P04 | 23.8% | 90% | 2471 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 89.3% | 89.3% | +0.2 | 50% | ✅ met |
| P01T | 194 | 93.8% | 93.8% | +0.0 | 50% | ✅ met |
| P01_GOLD | 627 | 92.2% | 94.4% | +0.0 | 95% | 🟡 3 pts to go |
| P02 | 466 | 74.0% | 75.8% | +0.0 | 95% | ❌ 21 pts to go |
| P03 | 265 | 80.8% | 83.8% | -0.6 | 95% | ❌ 14 pts to go |
| P04 | 3733 | 30.0% | 31.7% | -0.2 | 90% | ❌ 60 pts to go |
| P05 | 424 | 38.4% | 41.3% | -0.2 | 70% | ❌ 32 pts to go |
| P06M | 15579 | 91.9% | 91.9% | +0.1 | n/a | no target |
| P06T | 40041 | 98.7% | 98.7% | +0.1 | n/a | no target |
| P06 | 272 | 34.2% | 34.2% | -0.2 | 30% | ✅ met |
| P07 | 697 | 6.6% | 6.6% | -0.3 | 30% | ❌ 23 pts to go |
| P08 | 22230 | 1.3% | 1.3% | +0.0 | 25% | ❌ 24 pts to go |
| P09 | 307 | 99.0% | 99.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10 | 2389 | 2.9% | 3.0% | -0.2 | 25% | ❌ 22 pts to go |
| P11 | 1527 | 48.6% | 49.4% | +1.7 | 60% | ❌ 11 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 117988 | 99.8% | 99.8% | +0.1 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 194 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 627 | 6.1% | 6.1% | +0.0 | 50% | ❌ 44 pts to go |
| P02 | 466 | 6.2% | 6.2% | +0.0 | 50% | ❌ 44 pts to go |
| P03 | 265 | 1.5% | 1.5% | +0.0 | 40% | ❌ 38 pts to go |
| P04 | 3733 | 0.5% | 0.5% | +0.0 | 30% | ❌ 30 pts to go |
| P05 | 424 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 15579 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 40041 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 697 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22230 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 0.7% | 0.7% | +0.0 | 50% | ❌ 49 pts to go |
| P10 | 2389 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1527 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P12 | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 117988 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 82.4% | 82.4% | +0.2 | n/a | no target |
| P01T | 194 | 74.7% | 74.7% | +0.2 | 50% | ✅ met |
| P01_GOLD | 627 | 66.8% | 66.8% | +0.0 | 85% | ❌ 18 pts to go |
| P02 | 466 | 64.8% | 64.8% | +0.0 | 90% | ❌ 25 pts to go |
| P03 | 265 | 59.2% | 59.2% | -0.5 | 85% | ❌ 26 pts to go |
| P04 | 3733 | 27.5% | 27.5% | -0.1 | 85% | ❌ 58 pts to go |
| P05 | 424 | 28.8% | 28.8% | -0.1 | 60% | ❌ 31 pts to go |
| P06M | 15579 | 91.7% | 91.7% | +0.2 | n/a | no target |
| P06T | 40041 | 98.6% | 98.6% | +0.2 | n/a | no target |
| P06 | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 697 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22230 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 96.1% | 96.1% | +0.0 | 100% | 🟡 4 pts to go |
| P10 | 2389 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1527 | 45.1% | 45.1% | +1.8 | 60% | ❌ 15 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 117988 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 194 | 0.0% | 0.0% | +0.0 | 30% | ❌ 30 pts to go |
| P01_GOLD | 627 | 50.7% | 50.7% | -0.1 | 80% | ❌ 29 pts to go |
| P02 | 466 | 56.9% | 56.9% | +0.0 | 60% | 🟡 3 pts to go |
| P03 | 265 | 49.8% | 49.8% | -0.4 | 80% | ❌ 30 pts to go |
| P04 | 3733 | 22.8% | 22.8% | -0.1 | 50% | ❌ 27 pts to go |
| P05 | 424 | 11.3% | 11.3% | -0.1 | 40% | ❌ 29 pts to go |
| P06M | 15579 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 40041 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 697 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22230 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 83.4% | 83.4% | +0.0 | 50% | ✅ met |
| P10 | 2389 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1527 | 5.3% | 5.3% | -0.3 | 40% | ❌ 35 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 117988 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 194 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P01_GOLD | 627 | 60.4% | 60.4% | +0.0 | 85% | ❌ 25 pts to go |
| P02 | 466 | 56.2% | 56.2% | +0.0 | 90% | ❌ 34 pts to go |
| P03 | 265 | 58.1% | 58.1% | -0.5 | 85% | ❌ 27 pts to go |
| P04 | 3733 | 23.5% | 23.5% | -0.1 | 85% | ❌ 62 pts to go |
| P05 | 424 | 19.6% | 19.6% | -0.1 | 50% | ❌ 30 pts to go |
| P06M | 15579 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 40041 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 697 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22230 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 97.1% | 97.1% | +0.0 | 100% | 🟡 3 pts to go |
| P10 | 2389 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1527 | 5.8% | 5.8% | -0.2 | 60% | ❌ 54 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 117988 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 194 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 627 | 12.9% | 12.9% | +0.0 | 60% | ❌ 47 pts to go |
| P02 | 466 | 6.0% | 6.0% | +0.0 | 50% | ❌ 44 pts to go |
| P03 | 265 | 8.3% | 8.3% | -0.1 | 50% | ❌ 42 pts to go |
| P04 | 3733 | 1.8% | 1.8% | +0.0 | 40% | ❌ 38 pts to go |
| P05 | 424 | 0.7% | 0.7% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 15579 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 40041 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 697 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22230 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 3.3% | 3.3% | +0.0 | 50% | ❌ 47 pts to go |
| P10 | 2389 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1527 | 0.9% | 0.9% | +0.0 | n/a | no target |
| P12 | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 117988 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 194 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 627 | 34.8% | 34.8% | +0.0 | 80% | ❌ 45 pts to go |
| P02 | 466 | 51.9% | 51.9% | +0.0 | 90% | ❌ 38 pts to go |
| P03 | 265 | 32.5% | 32.5% | -0.2 | 80% | ❌ 48 pts to go |
| P04 | 3733 | 21.5% | 21.5% | -0.1 | 85% | ❌ 64 pts to go |
| P05 | 424 | 5.4% | 5.4% | -0.1 | 50% | ❌ 45 pts to go |
| P06M | 15579 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 40041 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 697 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22230 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 74.3% | 74.3% | +0.0 | 95% | ❌ 21 pts to go |
| P10 | 2389 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1527 | 4.1% | 4.1% | -0.2 | 50% | ❌ 46 pts to go |
| P12 | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 117988 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 194 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 627 | 8.5% | 8.5% | +0.0 | 50% | ❌ 42 pts to go |
| P02 | 466 | 6.2% | 6.2% | +0.0 | 50% | ❌ 44 pts to go |
| P03 | 265 | 1.9% | 1.9% | +0.0 | 30% | ❌ 28 pts to go |
| P04 | 3733 | 0.5% | 0.5% | +0.0 | 30% | ❌ 30 pts to go |
| P05 | 424 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 15579 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 40041 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 697 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22230 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P10 | 2389 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1527 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P12 | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 117988 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 194 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 627 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 466 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 265 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3733 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 424 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 15579 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 40041 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 272 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 697 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 22230 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 307 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2389 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1527 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 117988 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 11.5% | 11.5% | -0.1 | 70% | ❌ 58 pts to go |
| P01T | 194 | 52.1% | 52.1% | +1.6 | 60% | 🟡 8 pts to go |
| P01_GOLD | 627 | 74.6% | 74.6% | -0.2 | 90% | ❌ 15 pts to go |
| P02 | 466 | 53.9% | 53.9% | +0.3 | 85% | ❌ 31 pts to go |
| P03 | 265 | 69.4% | 69.4% | -0.2 | 90% | ❌ 21 pts to go |
| P04 | 3733 | 34.9% | 34.9% | -0.1 | 75% | ❌ 40 pts to go |
| P05 | 424 | 54.0% | 54.0% | -0.7 | 50% | ✅ met |
| P06M | 15579 | 3.1% | 3.1% | -0.1 | n/a | no target |
| P06T | 40041 | 48.5% | 48.5% | +1.2 | n/a | no target |
| P06 | 272 | 44.1% | 44.1% | +0.1 | 40% | ✅ met |
| P07 | 697 | 32.7% | 32.7% | -0.3 | 50% | ❌ 17 pts to go |
| P08 | 22230 | 30.5% | 30.5% | +0.0 | 50% | ❌ 20 pts to go |
| P09 | 307 | 58.3% | 58.3% | +0.0 | 80% | ❌ 22 pts to go |
| P10 | 2389 | 34.2% | 34.2% | -0.3 | 40% | 🟡 6 pts to go |
| P11 | 1527 | 47.7% | 47.7% | +0.8 | 60% | ❌ 12 pts to go |
| P12 | 15 | 60.0% | 60.0% | +0.0 | 85% | ❌ 25 pts to go |
| P13 | 117988 | 30.1% | 30.1% | -1.6 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 58.8% | 58.8% | -0.9 | n/a | no target |
| P01T | 194 | 53.1% | 53.1% | +2.1 | n/a | no target |
| P01_GOLD | 627 | 72.6% | 72.6% | -0.1 | 95% | ❌ 22 pts to go |
| P02 | 466 | 74.0% | 74.0% | +0.2 | 95% | ❌ 21 pts to go |
| P03 | 265 | 71.7% | 71.7% | -0.2 | 95% | ❌ 23 pts to go |
| P04 | 3733 | 49.4% | 49.4% | +0.2 | 95% | ❌ 46 pts to go |
| P05 | 424 | 57.8% | 57.8% | -0.5 | 70% | ❌ 12 pts to go |
| P06M | 15579 | 45.4% | 45.4% | -0.6 | n/a | no target |
| P06T | 40041 | 57.5% | 57.5% | +1.3 | n/a | no target |
| P06 | 272 | 41.2% | 41.2% | +0.2 | 80% | ❌ 39 pts to go |
| P07 | 697 | 32.1% | 32.1% | +0.2 | 70% | ❌ 38 pts to go |
| P08 | 22230 | 30.3% | 30.3% | +0.0 | 70% | ❌ 40 pts to go |
| P09 | 307 | 86.6% | 86.6% | +0.0 | 100% | ❌ 13 pts to go |
| P10 | 2389 | 35.5% | 35.5% | +0.0 | 70% | ❌ 34 pts to go |
| P11 | 1527 | 53.4% | 53.4% | +0.9 | 75% | ❌ 22 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 117988 | 25.6% | 25.6% | -1.3 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 16.8% | 16.8% | -0.3 | n/a | no target |
| P01T | 194 | 55.2% | 55.2% | +1.6 | n/a | no target |
| P01_GOLD | 627 | 49.8% | 49.8% | +0.0 | 60% | ❌ 10 pts to go |
| P02 | 466 | 56.2% | 56.2% | +0.0 | 60% | 🟡 4 pts to go |
| P03 | 265 | 55.1% | 55.1% | +0.0 | 60% | 🟡 5 pts to go |
| P04 | 3733 | 42.0% | 42.0% | -0.1 | 55% | ❌ 13 pts to go |
| P05 | 424 | 24.8% | 24.8% | +0.2 | 50% | ❌ 25 pts to go |
| P06M | 15579 | 6.8% | 6.8% | +0.0 | n/a | no target |
| P06T | 40041 | 50.9% | 50.9% | +0.0 | n/a | no target |
| P06 | 272 | 47.8% | 47.8% | +0.2 | n/a | no target |
| P07 | 697 | 41.6% | 41.6% | +0.7 | 55% | ❌ 13 pts to go |
| P08 | 22230 | 36.1% | 36.1% | -0.1 | 50% | ❌ 14 pts to go |
| P09 | 307 | 72.3% | 72.3% | +0.0 | 70% | ✅ met |
| P10 | 2389 | 46.6% | 46.6% | -0.2 | 55% | 🟡 8 pts to go |
| P11 | 1527 | 53.2% | 53.2% | +1.0 | 50% | ✅ met |
| P12 | 15 | 86.7% | 86.7% | +0.0 | n/a | no target |
| P13 | 117988 | 3.2% | 3.2% | -0.2 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 49.6% | 49.6% | -0.8 | n/a | no target |
| P01T | 194 | 75.3% | 75.3% | +0.8 | n/a | no target |
| P01_GOLD | 627 | 50.4% | 50.4% | -0.1 | 70% | ❌ 20 pts to go |
| P02 | 466 | 58.2% | 58.2% | +0.0 | 70% | ❌ 12 pts to go |
| P03 | 265 | 51.7% | 51.7% | +0.4 | 70% | ❌ 18 pts to go |
| P04 | 3733 | 54.2% | 54.2% | +0.1 | 65% | ❌ 11 pts to go |
| P05 | 424 | 28.5% | 28.5% | +0.1 | 60% | ❌ 32 pts to go |
| P06M | 15579 | 35.8% | 35.8% | -0.8 | n/a | no target |
| P06T | 40041 | 77.8% | 77.8% | -2.2 | n/a | no target |
| P06 | 272 | 69.1% | 69.1% | +0.2 | 40% | ✅ met |
| P07 | 697 | 65.1% | 65.1% | +0.2 | 85% | ❌ 20 pts to go |
| P08 | 22230 | 65.3% | 65.3% | +0.0 | 85% | ❌ 20 pts to go |
| P09 | 307 | 59.0% | 59.0% | -0.3 | 85% | ❌ 26 pts to go |
| P10 | 2389 | 63.8% | 63.8% | +0.3 | 85% | ❌ 21 pts to go |
| P11 | 1527 | 62.4% | 62.4% | +0.5 | 75% | ❌ 13 pts to go |
| P12 | 15 | 26.7% | 26.7% | +0.0 | n/a | no target |
| P13 | 117988 | 91.5% | 91.5% | +0.3 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 55.7% | 55.7% | -0.9 | n/a | no target |
| P01T | 194 | 97.4% | 97.4% | +0.0 | n/a | no target |
| P01_GOLD | 627 | 79.6% | 79.6% | +0.0 | 90% | ❌ 10 pts to go |
| P02 | 466 | 83.9% | 83.9% | +0.0 | 90% | 🟡 6 pts to go |
| P03 | 265 | 87.9% | 87.9% | +0.1 | 90% | 🟡 2 pts to go |
| P04 | 3733 | 84.3% | 84.3% | -0.1 | 85% | 🟡 1 pts to go |
| P05 | 424 | 45.0% | 45.0% | +0.2 | 70% | ❌ 25 pts to go |
| P06M | 15579 | 42.3% | 42.3% | -1.3 | n/a | no target |
| P06T | 40041 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 272 | 99.3% | 99.3% | +0.0 | 50% | ✅ met |
| P07 | 697 | 99.9% | 99.9% | +0.0 | 100% | 🟡 0 pts to go |
| P08 | 22230 | 99.8% | 99.8% | +0.0 | 100% | 🟡 0 pts to go |
| P09 | 307 | 79.8% | 79.8% | +0.0 | 100% | ❌ 20 pts to go |
| P10 | 2389 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1527 | 97.4% | 97.4% | +0.1 | 100% | 🟡 3 pts to go |
| P12 | 15 | 53.3% | 53.3% | +0.0 | n/a | no target |
| P13 | 117988 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 15.3% | 15.3% | -0.2 | n/a | no target |
| P01T | 194 | 66.0% | 66.0% | +0.9 | n/a | no target |
| P01_GOLD | 627 | 43.4% | 43.4% | -0.1 | 70% | ❌ 27 pts to go |
| P02 | 466 | 48.5% | 48.5% | -0.2 | 75% | ❌ 26 pts to go |
| P03 | 265 | 43.0% | 43.0% | -0.3 | 75% | ❌ 32 pts to go |
| P04 | 3733 | 38.8% | 38.8% | +0.1 | 70% | ❌ 31 pts to go |
| P05 | 424 | 22.2% | 22.2% | +0.2 | 55% | ❌ 33 pts to go |
| P06M | 15579 | 4.7% | 4.7% | -0.1 | n/a | no target |
| P06T | 40041 | 63.9% | 63.9% | +1.8 | n/a | no target |
| P06 | 272 | 47.8% | 47.8% | +0.9 | n/a | no target |
| P07 | 697 | 49.9% | 49.9% | -0.1 | 70% | ❌ 20 pts to go |
| P08 | 22230 | 54.8% | 54.8% | +0.0 | 75% | ❌ 20 pts to go |
| P09 | 307 | 49.2% | 49.2% | +0.0 | 85% | ❌ 36 pts to go |
| P10 | 2389 | 43.7% | 43.7% | +0.1 | 80% | ❌ 36 pts to go |
| P11 | 1527 | 55.3% | 55.3% | +1.0 | 70% | ❌ 15 pts to go |
| P12 | 15 | 40.0% | 40.0% | +0.0 | n/a | no target |
| P13 | 117988 | 5.1% | 5.1% | -0.1 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 55.7% | 55.7% | -0.9 | n/a | no target |
| P01T | 194 | 94.8% | 94.8% | +0.0 | n/a | no target |
| P01_GOLD | 627 | 73.8% | 73.8% | +0.0 | 90% | ❌ 16 pts to go |
| P02 | 466 | 78.8% | 78.8% | -0.2 | 90% | ❌ 11 pts to go |
| P03 | 265 | 83.4% | 83.4% | +0.1 | 90% | 🟡 7 pts to go |
| P04 | 3733 | 76.5% | 76.5% | +0.1 | 85% | 🟡 8 pts to go |
| P05 | 424 | 43.4% | 43.4% | +0.3 | 75% | ❌ 32 pts to go |
| P06M | 15579 | 42.1% | 42.1% | -1.2 | n/a | no target |
| P06T | 40041 | 96.5% | 96.5% | -0.2 | n/a | no target |
| P06 | 272 | 90.8% | 90.8% | +0.3 | n/a | no target |
| P07 | 697 | 92.5% | 92.5% | +0.0 | 100% | 🟡 8 pts to go |
| P08 | 22230 | 90.7% | 90.7% | -0.1 | 100% | 🟡 9 pts to go |
| P09 | 307 | 66.1% | 66.1% | +0.0 | n/a | no target |
| P10 | 2389 | 86.7% | 86.7% | -0.1 | 100% | ❌ 13 pts to go |
| P11 | 1527 | 88.0% | 88.0% | +0.3 | n/a | no target |
| P12 | 15 | 46.7% | 46.7% | +0.0 | n/a | no target |
| P13 | 117988 | 66.7% | 66.7% | +1.5 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 45.8% | 45.8% | -0.7 | n/a | no target · QC vendors: 49 rows, 100.0% filled |
| P01T | 194 | 8.8% | 8.8% | -0.6 | n/a | no target · QC vendors: 4 rows, 75.0% filled |
| P01_GOLD | 627 | 43.7% | 43.7% | -0.1 | 95% | ❌ 51 pts to go · QC vendors: 54 rows, 98.1% filled |
| P02 | 466 | 55.8% | 55.8% | +0.2 | 95% | ❌ 39 pts to go · QC vendors: 113 rows, 100.0% filled |
| P03 | 265 | 46.0% | 46.0% | +0.0 | 95% | ❌ 49 pts to go · QC vendors: 21 rows, 100.0% filled |
| P04 | 3733 | 32.1% | 32.1% | -0.1 | 95% | ❌ 63 pts to go · QC vendors: 619 rows, 97.9% filled |
| P05 | 424 | 14.2% | 14.2% | +0.2 | n/a | no target · QC vendors: 35 rows, 94.3% filled |
| P06M | 15579 | 42.3% | 42.3% | -0.5 | n/a | no target · QC vendors: 5832 rows, 99.8% filled |
| P06T | 40041 | 5.1% | 5.1% | -0.2 | n/a | no target · QC vendors: 2079 rows, 76.9% filled |
| P06 | 272 | 8.5% | 8.5% | +0.1 | n/a | no target · QC vendors: 16 rows, 68.8% filled |
| P07 | 697 | 6.6% | 6.6% | +0.3 | n/a | no target · QC vendors: 40 rows, 77.5% filled |
| P08 | 22230 | 6.6% | 6.6% | +0.0 | n/a | no target · QC vendors: 1295 rows, 92.7% filled |
| P09 | 307 | 76.9% | 76.9% | +0.0 | 95% | ❌ 18 pts to go · QC vendors: 112 rows, 100.0% filled |
| P10 | 2389 | 15.6% | 15.6% | +0.0 | n/a | no target · QC vendors: 230 rows, 90.0% filled |
| P11 | 1527 | 14.5% | 14.5% | -0.3 | n/a | no target · QC vendors: 156 rows, 91.0% filled |
| P12 | 15 | 73.3% | 73.3% | +0.0 | n/a | no target · QC vendors: 3 rows, 100.0% filled |
| P13 | 117988 | 25.0% | 25.0% | -1.2 | n/a | no target · QC vendors: 29498 rows, 100.0% filled |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 58.0% | 58.0% | -0.9 | n/a | no target · vendors with a registry record: 76 rows, 100.0% filled |
| P01T | 194 | 53.1% | 53.1% | +2.1 | n/a | no target · vendors with a registry record: 103 rows, 100.0% filled |
| P01_GOLD | 627 | 81.3% | 81.3% | -0.2 | 100% | ❌ 19 pts to go · vendors with a registry record: 510 rows, 100.0% filled |
| P02 | 466 | 77.7% | 77.7% | +0.2 | 100% | ❌ 22 pts to go · vendors with a registry record: 362 rows, 100.0% filled |
| P03 | 265 | 80.8% | 80.8% | -0.2 | 100% | ❌ 19 pts to go · vendors with a registry record: 214 rows, 100.0% filled |
| P04 | 3733 | 49.8% | 49.8% | +0.1 | 100% | ❌ 50 pts to go · vendors with a registry record: 1858 rows, 100.0% filled |
| P05 | 424 | 62.7% | 62.7% | -0.6 | n/a | no target · vendors with a registry record: 266 rows, 100.0% filled |
| P06M | 15579 | 45.2% | 45.2% | -0.7 | n/a | no target · vendors with a registry record: 7049 rows, 100.0% filled |
| P06T | 40041 | 57.6% | 57.6% | +1.4 | n/a | no target · vendors with a registry record: 23055 rows, 100.0% filled |
| P06 | 272 | 41.5% | 41.5% | +0.1 | n/a | no target · vendors with a registry record: 113 rows, 100.0% filled |
| P07 | 697 | 32.7% | 32.7% | +0.4 | n/a | no target · vendors with a registry record: 228 rows, 100.0% filled |
| P08 | 22230 | 30.5% | 30.5% | +0.1 | n/a | no target · vendors with a registry record: 6776 rows, 100.0% filled |
| P09 | 307 | 90.6% | 90.6% | +0.0 | n/a | no target · vendors with a registry record: 278 rows, 100.0% filled |
| P10 | 2389 | 36.2% | 36.2% | +0.0 | n/a | no target · vendors with a registry record: 865 rows, 100.0% filled |
| P11 | 1527 | 54.5% | 54.5% | +0.9 | n/a | no target · vendors with a registry record: 832 rows, 100.0% filled |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 15 rows, 100.0% filled |
| P13 | 117988 | 25.6% | 25.6% | -1.3 | n/a | no target · vendors with a registry record: 30154 rows, 100.0% filled |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 93.9% | 93.9% | +0.1 | 90% | ✅ met |
| P01T | 194 | 70.6% | 70.6% | -1.8 | 90% | ❌ 19 pts to go |
| P01_GOLD | 627 | 87.9% | 87.9% | +0.2 | 95% | 🟡 7 pts to go |
| P02 | 466 | 88.4% | 88.4% | +0.6 | 95% | 🟡 7 pts to go |
| P03 | 265 | 83.8% | 83.8% | -0.6 | 85% | 🟡 1 pts to go |
| P04 | 3733 | 62.6% | 62.6% | -0.4 | 90% | ❌ 27 pts to go |
| P05 | 424 | 79.0% | 79.0% | -0.1 | 75% | ✅ met |
| P06M | 15579 | 91.9% | 91.9% | +0.3 | n/a | no target |
| P06T | 40041 | 33.8% | 33.8% | -3.5 | n/a | no target |
| P06 | 272 | 73.2% | 73.2% | -0.4 | 80% | 🟡 7 pts to go |
| P07 | 697 | 59.5% | 59.7% | -0.3 | 80% | ❌ 20 pts to go |
| P08 | 22230 | 53.6% | 53.7% | -0.8 | 75% | ❌ 21 pts to go |
| P09 | 307 | 76.9% | 76.9% | +0.0 | 95% | ❌ 18 pts to go |
| P10 | 2389 | 45.7% | 45.7% | -1.0 | 70% | ❌ 24 pts to go |
| P11 | 1527 | 29.8% | 29.8% | -1.5 | 65% | ❌ 35 pts to go |
| P12 | 15 | 80.0% | 80.0% | +0.0 | 80% | ✅ met |
| P13 | 117988 | 40.2% | 40.2% | -7.3 | 60% | ❌ 20 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 19.8% | 19.8% | -0.4 | 50% | ❌ 30 pts to go |
| P01T | 194 | 15.5% | 15.5% | -0.6 | n/a | no target |
| P01_GOLD | 627 | 19.5% | 19.5% | +0.0 | 40% | ❌ 20 pts to go |
| P02 | 466 | 18.9% | 18.9% | -0.2 | 40% | ❌ 21 pts to go |
| P03 | 265 | 21.1% | 21.1% | -0.2 | 40% | ❌ 19 pts to go |
| P04 | 3733 | 14.9% | 14.9% | -0.3 | 40% | ❌ 25 pts to go |
| P05 | 424 | 17.5% | 17.5% | +0.0 | 25% | 🟡 8 pts to go |
| P06M | 15579 | 10.9% | 10.9% | -0.7 | n/a | no target |
| P06T | 40041 | 6.0% | 6.0% | -0.9 | n/a | no target |
| P06 | 272 | 12.1% | 12.1% | -0.7 | 35% | ❌ 23 pts to go |
| P07 | 697 | 13.8% | 13.8% | -0.3 | 35% | ❌ 21 pts to go |
| P08 | 22230 | 15.2% | 15.2% | -0.2 | 35% | ❌ 20 pts to go |
| P09 | 307 | 16.3% | 16.3% | +0.0 | n/a | no target |
| P10 | 2389 | 6.4% | 6.4% | -0.3 | 30% | ❌ 24 pts to go |
| P11 | 1527 | 6.9% | 6.9% | -0.5 | n/a | no target |
| P12 | 15 | 6.7% | 6.7% | +0.0 | n/a | no target |
| P13 | 117988 | 10.0% | 10.0% | -2.3 | 30% | ❌ 20 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 194 | 83.5% | 83.5% | -0.9 | 100% | ❌ 16 pts to go |
| P01_GOLD | 627 | 90.7% | 90.7% | +0.0 | 100% | 🟡 9 pts to go |
| P02 | 466 | 95.1% | 95.1% | -0.4 | 100% | 🟡 5 pts to go |
| P03 | 265 | 88.7% | 88.7% | -0.7 | 100% | ❌ 11 pts to go |
| P04 | 3733 | 70.8% | 70.8% | -0.6 | 100% | ❌ 29 pts to go |
| P05 | 424 | 89.2% | 89.2% | -0.1 | 100% | ❌ 11 pts to go |
| P06M | 15579 | 99.2% | 99.2% | +0.0 | n/a | no target |
| P06T | 40041 | 56.1% | 56.1% | -3.2 | n/a | no target |
| P06 | 272 | 79.0% | 79.0% | +0.2 | 95% | ❌ 16 pts to go |
| P07 | 697 | 80.5% | 80.5% | -0.7 | 95% | ❌ 14 pts to go |
| P08 | 22230 | 78.1% | 78.1% | -0.2 | 95% | ❌ 17 pts to go |
| P09 | 307 | 96.1% | 96.1% | +0.0 | 100% | 🟡 4 pts to go |
| P10 | 2389 | 53.5% | 53.5% | -0.9 | 95% | ❌ 42 pts to go |
| P11 | 1527 | 50.4% | 50.4% | +1.0 | 80% | ❌ 30 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 117988 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 85.5% | 85.5% | -0.5 | n/a | no target |
| P01T | 194 | 66.5% | 66.5% | -1.7 | n/a | no target |
| P01_GOLD | 627 | 72.9% | 72.9% | -0.1 | 90% | ❌ 17 pts to go |
| P02 | 466 | 77.9% | 77.9% | +0.0 | 95% | ❌ 17 pts to go |
| P03 | 265 | 74.0% | 74.0% | -0.9 | 95% | ❌ 21 pts to go |
| P04 | 3733 | 68.0% | 68.0% | -0.9 | 95% | ❌ 27 pts to go |
| P05 | 424 | 72.9% | 72.9% | -0.6 | 90% | ❌ 17 pts to go |
| P06M | 15579 | 83.5% | 83.5% | -3.4 | n/a | no target |
| P06T | 40041 | 51.1% | 51.1% | -6.1 | n/a | no target |
| P06 | 272 | 68.8% | 68.8% | +0.3 | 95% | ❌ 26 pts to go |
| P07 | 697 | 64.7% | 64.7% | -0.1 | 90% | ❌ 25 pts to go |
| P08 | 22230 | 66.7% | 66.7% | -1.1 | 95% | ❌ 28 pts to go |
| P09 | 307 | 87.0% | 87.0% | +0.0 | 100% | ❌ 13 pts to go |
| P10 | 2389 | 54.0% | 54.0% | -1.3 | 95% | ❌ 41 pts to go |
| P11 | 1527 | 27.6% | 27.6% | -1.3 | 75% | ❌ 47 pts to go |
| P12 | 15 | 93.3% | 93.3% | +0.0 | n/a | no target |
| P13 | 117988 | 58.6% | 58.6% | -12.2 | 95% | ❌ 36 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 86.3% | 86.3% | -1.3 | n/a | no target |
| P01T | 194 | 80.9% | 80.9% | -2.4 | 95% | ❌ 14 pts to go |
| P01_GOLD | 627 | 84.7% | 84.7% | -0.1 | 90% | 🟡 5 pts to go |
| P02 | 466 | 90.1% | 90.1% | -0.5 | 95% | 🟡 5 pts to go |
| P03 | 265 | 84.9% | 84.9% | -0.7 | 95% | ❌ 10 pts to go |
| P04 | 3733 | 88.1% | 88.1% | -1.1 | 90% | 🟡 2 pts to go |
| P05 | 424 | 92.5% | 92.5% | -0.6 | 95% | 🟡 2 pts to go |
| P06M | 15579 | 87.8% | 87.8% | -5.4 | n/a | no target |
| P06T | 40041 | 67.0% | 67.0% | -7.9 | n/a | no target |
| P06 | 272 | 92.3% | 92.3% | +0.0 | 100% | 🟡 8 pts to go |
| P07 | 697 | 91.0% | 91.0% | -1.2 | 100% | 🟡 9 pts to go |
| P08 | 22230 | 91.0% | 91.0% | -1.3 | 100% | 🟡 9 pts to go |
| P09 | 307 | 73.0% | 73.0% | +0.0 | n/a | no target |
| P10 | 2389 | 90.0% | 90.0% | -1.3 | 100% | 🟡 10 pts to go |
| P11 | 1527 | 39.9% | 39.9% | -2.0 | 80% | ❌ 40 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 117988 | 69.5% | 69.5% | -14.2 | 95% | ❌ 26 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 3.1% | 3.1% | +0.0 | n/a | no target |
| P01T | 194 | 9.3% | 9.3% | -0.1 | n/a | no target |
| P01_GOLD | 627 | 14.2% | 14.2% | +0.0 | 25% | ❌ 11 pts to go |
| P02 | 466 | 25.1% | 25.1% | -0.2 | 40% | ❌ 15 pts to go |
| P03 | 265 | 9.1% | 9.1% | +0.0 | 20% | ❌ 11 pts to go |
| P04 | 3733 | 3.5% | 3.5% | +0.0 | 20% | ❌ 16 pts to go |
| P05 | 424 | 3.3% | 3.3% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 15579 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 40041 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 272 | 5.1% | 5.1% | +0.0 | n/a | no target |
| P07 | 697 | 8.5% | 8.5% | +0.0 | n/a | no target |
| P08 | 22230 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P09 | 307 | 7.8% | 7.8% | +0.0 | n/a | no target |
| P10 | 2389 | 0.8% | 0.8% | +0.0 | n/a | no target |
| P11 | 1527 | 0.9% | 0.9% | -0.1 | n/a | no target |
| P12 | 15 | 6.7% | 6.7% | +0.0 | n/a | no target |
| P13 | 117988 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 18.3% | 18.3% | -0.3 | n/a | no target |
| P01T | 194 | 22.2% | 22.2% | -0.2 | 70% | ❌ 48 pts to go |
| P01_GOLD | 627 | 43.4% | 43.4% | -0.1 | 80% | ❌ 37 pts to go |
| P02 | 466 | 57.3% | 57.3% | +0.0 | 90% | ❌ 33 pts to go |
| P03 | 265 | 18.5% | 18.5% | -0.1 | 60% | ❌ 42 pts to go |
| P04 | 3733 | 21.6% | 21.6% | +0.0 | 85% | ❌ 63 pts to go |
| P05 | 424 | 11.6% | 11.6% | +0.0 | 50% | ❌ 38 pts to go |
| P06M | 15579 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06T | 40041 | 0.6% | 0.6% | -0.1 | n/a | no target |
| P06 | 272 | 15.4% | 15.4% | +0.0 | n/a | no target |
| P07 | 697 | 10.0% | 10.0% | -0.5 | n/a | no target |
| P08 | 22230 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P09 | 307 | 77.9% | 77.9% | +0.0 | 95% | ❌ 17 pts to go |
| P10 | 2389 | 1.5% | 1.5% | -0.2 | n/a | no target |
| P11 | 1527 | 15.9% | 15.9% | -0.8 | n/a | no target |
| P12 | 15 | 26.7% | 26.7% | +0.0 | n/a | no target |
| P13 | 117988 | 0.4% | 0.4% | -0.1 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 6.1% | 6.1% | -0.1 | n/a | no target |
| P01T | 194 | 9.8% | 9.8% | -0.6 | n/a | no target |
| P01_GOLD | 627 | 34.0% | 34.0% | +0.0 | 70% | ❌ 36 pts to go |
| P02 | 466 | 39.1% | 39.1% | +0.0 | 75% | ❌ 36 pts to go |
| P03 | 265 | 18.5% | 18.5% | -0.1 | 55% | ❌ 36 pts to go |
| P04 | 3733 | 21.5% | 21.5% | -0.1 | 75% | ❌ 54 pts to go |
| P05 | 424 | 10.6% | 10.6% | -0.1 | 50% | ❌ 39 pts to go |
| P06M | 15579 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06T | 40041 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 272 | 5.9% | 5.9% | +0.0 | n/a | no target |
| P07 | 697 | 4.9% | 4.9% | -0.3 | n/a | no target |
| P08 | 22230 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 307 | 75.2% | 75.2% | +0.0 | 95% | ❌ 20 pts to go |
| P10 | 2389 | 0.7% | 0.7% | -0.2 | n/a | no target |
| P11 | 1527 | 15.6% | 15.6% | -0.8 | n/a | no target |
| P12 | 15 | 20.0% | 20.0% | +0.0 | n/a | no target |
| P13 | 117988 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 7.6% | 7.6% | -0.2 | n/a | no target |
| P01T | 194 | 8.2% | 8.2% | -0.1 | n/a | no target |
| P01_GOLD | 627 | 57.9% | 58.1% | -0.1 | 80% | ❌ 22 pts to go |
| P02 | 466 | 45.7% | 45.9% | +0.0 | 75% | ❌ 29 pts to go |
| P03 | 265 | 37.0% | 37.0% | -0.3 | 70% | ❌ 33 pts to go |
| P04 | 3733 | 21.1% | 21.5% | +0.0 | 70% | ❌ 49 pts to go |
| P05 | 424 | 14.2% | 14.2% | +0.0 | 50% | ❌ 36 pts to go |
| P06M | 15579 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 40041 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P06 | 272 | 15.8% | 15.8% | -0.7 | n/a | no target |
| P07 | 697 | 1.9% | 1.9% | -0.1 | n/a | no target |
| P08 | 22230 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P09 | 307 | 46.6% | 46.9% | +0.0 | 80% | ❌ 33 pts to go |
| P10 | 2389 | 1.0% | 1.1% | -0.2 | n/a | no target |
| P11 | 1527 | 6.5% | 6.5% | -0.3 | n/a | no target |
| P12 | 15 | 40.0% | 40.0% | +0.0 | n/a | no target |
| P13 | 117988 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 18.3% | 18.3% | -0.3 | n/a | no target |
| P01T | 194 | 20.6% | 20.6% | -0.8 | 60% | ❌ 39 pts to go |
| P01_GOLD | 627 | 63.5% | 63.5% | +0.1 | 70% | 🟡 6 pts to go |
| P02 | 466 | 39.7% | 39.7% | +0.0 | 50% | ❌ 10 pts to go |
| P03 | 265 | 47.9% | 47.9% | -0.4 | 55% | 🟡 7 pts to go |
| P04 | 3733 | 12.2% | 12.2% | +0.0 | 40% | ❌ 28 pts to go |
| P05 | 424 | 17.0% | 17.0% | -0.1 | 40% | ❌ 23 pts to go |
| P06M | 15579 | 2.1% | 2.1% | -0.1 | n/a | no target |
| P06T | 40041 | 1.5% | 1.5% | -0.2 | n/a | no target |
| P06 | 272 | 21.3% | 21.3% | -0.7 | n/a | no target |
| P07 | 697 | 6.5% | 6.5% | -0.1 | n/a | no target |
| P08 | 22230 | 2.9% | 2.9% | +0.0 | n/a | no target |
| P09 | 307 | 5.9% | 5.9% | +0.0 | n/a | no target |
| P10 | 2389 | 4.6% | 4.6% | +0.0 | n/a | no target |
| P11 | 1527 | 5.0% | 5.0% | -0.2 | n/a | no target |
| P12 | 15 | 6.7% | 6.7% | +0.0 | n/a | no target |
| P13 | 117988 | 0.9% | 0.9% | -0.1 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 21.4% | 21.4% | -0.3 | n/a | no target |
| P01T | 194 | 28.4% | 28.4% | -0.2 | 65% | ❌ 37 pts to go |
| P01_GOLD | 627 | 68.9% | 68.9% | -0.1 | 70% | 🟡 1 pts to go |
| P02 | 466 | 24.2% | 24.2% | +0.0 | 50% | ❌ 26 pts to go |
| P03 | 265 | 52.1% | 52.1% | -0.4 | 60% | 🟡 8 pts to go |
| P04 | 3733 | 5.3% | 5.3% | -0.1 | 40% | ❌ 35 pts to go |
| P05 | 424 | 19.6% | 19.6% | -0.1 | 45% | ❌ 25 pts to go |
| P06M | 15579 | 1.3% | 1.3% | -0.1 | n/a | no target |
| P06T | 40041 | 0.6% | 0.6% | -0.1 | n/a | no target |
| P06 | 272 | 34.2% | 34.2% | -0.2 | n/a | no target |
| P07 | 697 | 6.6% | 6.6% | -0.3 | n/a | no target |
| P08 | 22230 | 1.3% | 1.3% | +0.0 | n/a | no target |
| P09 | 307 | 9.8% | 9.8% | +0.0 | n/a | no target |
| P10 | 2389 | 2.9% | 2.9% | -0.2 | n/a | no target |
| P11 | 1527 | 4.8% | 4.8% | -0.3 | n/a | no target |
| P12 | 15 | 6.7% | 6.7% | +0.0 | n/a | no target |
| P13 | 117988 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 12.2% | 12.2% | -0.2 | n/a | no target |
| P01T | 194 | 13.4% | 13.4% | -0.1 | n/a | no target |
| P01_GOLD | 627 | 49.8% | 49.8% | +0.0 | 50% | 🟡 0 pts to go |
| P02 | 466 | 37.3% | 37.3% | +0.0 | n/a | no target |
| P03 | 265 | 51.7% | 51.7% | -0.4 | 60% | 🟡 8 pts to go |
| P04 | 3733 | 11.8% | 11.8% | -0.1 | n/a | no target |
| P05 | 424 | 15.1% | 15.1% | -0.1 | n/a | no target |
| P06M | 15579 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P06T | 40041 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 272 | 25.4% | 25.4% | -0.2 | n/a | no target |
| P07 | 697 | 8.2% | 8.2% | -0.1 | n/a | no target |
| P08 | 22230 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P09 | 307 | 17.6% | 17.6% | +0.0 | n/a | no target |
| P10 | 2389 | 2.4% | 2.4% | +0.0 | n/a | no target |
| P11 | 1527 | 4.3% | 4.3% | -0.4 | n/a | no target |
| P12 | 15 | 13.3% | 13.3% | +0.0 | n/a | no target |
| P13 | 117988 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 11.5% | 11.5% | -0.1 | 15% | 🟡 4 pts to go |
| P01T | 194 | 11.9% | 11.9% | -0.6 | 15% | 🟡 3 pts to go |
| P01_GOLD | 627 | 35.4% | 35.4% | +0.1 | 40% | 🟡 5 pts to go |
| P02 | 466 | 12.9% | 13.1% | +0.0 | 25% | ❌ 12 pts to go |
| P03 | 265 | 17.4% | 17.4% | -0.1 | 25% | 🟡 8 pts to go |
| P04 | 3733 | 2.7% | 2.7% | +0.0 | 15% | ❌ 12 pts to go |
| P05 | 424 | 6.6% | 6.6% | +0.0 | 15% | 🟡 8 pts to go |
| P06M | 15579 | 0.8% | 0.8% | -0.1 | 15% | ❌ 14 pts to go |
| P06T | 40041 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |
| P06 | 272 | 10.7% | 10.7% | +0.1 | 15% | 🟡 4 pts to go |
| P07 | 697 | 4.2% | 4.2% | -0.1 | 15% | ❌ 11 pts to go |
| P08 | 22230 | 0.6% | 0.6% | +0.0 | 15% | ❌ 14 pts to go |
| P09 | 307 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2389 | 1.3% | 1.3% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 1527 | 1.4% | 1.4% | -0.1 | 15% | ❌ 14 pts to go |
| P12 | 15 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 117988 | 0.6% | 0.6% | -0.1 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 5.3% | 5.3% | -0.1 | 15% | 🟡 10 pts to go |
| P01T | 194 | 11.3% | 11.3% | -0.2 | 25% | ❌ 14 pts to go |
| P01_GOLD | 627 | 29.2% | 29.2% | +0.0 | 25% | ✅ met |
| P02 | 466 | 25.3% | 25.3% | +0.0 | 15% | ✅ met |
| P03 | 265 | 21.9% | 21.9% | -0.2 | 15% | ✅ met |
| P04 | 3733 | 4.0% | 4.0% | +0.0 | 15% | ❌ 11 pts to go |
| P05 | 424 | 11.1% | 11.1% | +0.0 | 15% | 🟡 4 pts to go |
| P06M | 15579 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |
| P06T | 40041 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 272 | 8.5% | 8.5% | +0.1 | 15% | 🟡 6 pts to go |
| P07 | 697 | 2.9% | 2.9% | +0.0 | 15% | ❌ 12 pts to go |
| P08 | 22230 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |
| P09 | 307 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2389 | 1.5% | 1.5% | -0.1 | 15% | ❌ 14 pts to go |
| P11 | 1527 | 2.5% | 2.5% | -0.2 | 15% | ❌ 12 pts to go |
| P12 | 15 | 20.0% | 20.0% | +0.0 | 15% | ✅ met |
| P13 | 117988 | 0.1% | 0.1% | -0.1 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 2.3% | 2.3% | +0.0 | 20% | ❌ 18 pts to go |
| P01T | 194 | 4.1% | 4.1% | -0.1 | 20% | ❌ 16 pts to go |
| P01_GOLD | 627 | 4.5% | 4.5% | +0.0 | 20% | ❌ 16 pts to go |
| P02 | 466 | 1.5% | 1.5% | +0.0 | 20% | ❌ 18 pts to go |
| P03 | 265 | 1.5% | 1.5% | +0.0 | 20% | ❌ 18 pts to go |
| P04 | 3733 | 0.6% | 0.6% | +0.0 | 20% | ❌ 19 pts to go |
| P05 | 424 | 1.2% | 1.2% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 15579 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 40041 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 272 | 1.5% | 1.5% | +0.0 | 20% | ❌ 18 pts to go |
| P07 | 697 | 0.4% | 0.4% | +0.0 | 20% | ❌ 20 pts to go |
| P08 | 22230 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P09 | 307 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2389 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 1527 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P12 | 15 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 117988 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 1.5% | 1.5% | -0.1 | 15% | ❌ 14 pts to go |
| P01T | 194 | 3.1% | 3.1% | +0.0 | 15% | ❌ 12 pts to go |
| P01_GOLD | 627 | 10.4% | 10.4% | +0.0 | 15% | 🟡 5 pts to go |
| P02 | 466 | 12.0% | 12.0% | +0.0 | 15% | 🟡 3 pts to go |
| P03 | 265 | 20.0% | 20.0% | -0.2 | 15% | ✅ met |
| P04 | 3733 | 2.3% | 2.3% | +0.0 | 15% | ❌ 13 pts to go |
| P05 | 424 | 2.8% | 2.8% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 15579 | 0.3% | 0.3% | +0.0 | 15% | ❌ 15 pts to go |
| P06T | 40041 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 272 | 5.1% | 5.1% | +0.0 | 15% | 🟡 10 pts to go |
| P07 | 697 | 1.6% | 1.6% | +0.0 | 15% | ❌ 13 pts to go |
| P08 | 22230 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |
| P09 | 307 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2389 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 1527 | 1.2% | 1.2% | +0.0 | 15% | ❌ 14 pts to go |
| P12 | 15 | 6.7% | 6.7% | +0.0 | 15% | 🟡 8 pts to go |
| P13 | 117988 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 13.7% | 13.7% | -0.3 | 20% | 🟡 6 pts to go |
| P01T | 194 | 13.9% | 13.9% | -0.2 | 40% | ❌ 26 pts to go |
| P01_GOLD | 627 | 46.1% | 46.1% | -0.1 | 40% | ✅ met |
| P02 | 466 | 42.9% | 42.9% | +0.0 | 20% | ✅ met |
| P03 | 265 | 48.7% | 48.7% | -0.3 | 35% | ✅ met |
| P04 | 3733 | 14.1% | 14.1% | -0.1 | 20% | 🟡 6 pts to go |
| P05 | 424 | 15.3% | 15.3% | -0.1 | 20% | 🟡 5 pts to go |
| P06M | 15579 | 0.8% | 0.8% | +0.0 | 20% | ❌ 19 pts to go |
| P06T | 40041 | 0.6% | 0.6% | -0.1 | 20% | ❌ 19 pts to go |
| P06 | 272 | 25.0% | 25.0% | -0.3 | 20% | ✅ met |
| P07 | 697 | 8.6% | 8.6% | +0.0 | 20% | ❌ 11 pts to go |
| P08 | 22230 | 1.0% | 1.0% | +0.0 | 20% | ❌ 19 pts to go |
| P09 | 307 | 18.2% | 18.2% | +0.0 | 20% | 🟡 2 pts to go |
| P10 | 2389 | 3.6% | 3.6% | -0.1 | 20% | ❌ 16 pts to go |
| P11 | 1527 | 4.6% | 4.6% | -0.2 | 20% | ❌ 15 pts to go |
| P12 | 15 | 6.7% | 6.7% | +0.0 | 20% | ❌ 13 pts to go |
| P13 | 117988 | 0.4% | 0.4% | -0.1 | 20% | ❌ 20 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 33.6% | 33.6% | +0.3 | n/a | no target |
| P01T | 194 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P01_GOLD | 627 | 69.5% | 69.5% | +0.0 | 95% | ❌ 26 pts to go |
| P02 | 466 | 62.9% | 62.9% | +0.0 | 95% | ❌ 32 pts to go |
| P03 | 265 | 52.8% | 52.8% | -0.4 | 90% | ❌ 37 pts to go |
| P04 | 3733 | 24.8% | 24.8% | +0.0 | 85% | ❌ 60 pts to go |
| P05 | 424 | 37.5% | 37.5% | -0.2 | 75% | ❌ 38 pts to go |
| P06M | 15579 | 36.2% | 36.2% | +0.1 | n/a | no target |
| P06T | 40041 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 697 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22230 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 88.3% | 88.3% | +0.0 | 100% | ❌ 12 pts to go |
| P10 | 2389 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1527 | 5.7% | 5.7% | -0.3 | 60% | ❌ 54 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 117988 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 33.6% | 33.6% | +0.3 | n/a | no target |
| P01T | 194 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 627 | 72.7% | 72.7% | -0.1 | 100% | ❌ 27 pts to go |
| P02 | 466 | 66.3% | 66.3% | +0.0 | 100% | ❌ 34 pts to go |
| P03 | 265 | 58.5% | 58.5% | -0.4 | n/a | no target |
| P04 | 3733 | 25.4% | 25.4% | -0.1 | 95% | ❌ 70 pts to go |
| P05 | 424 | 33.3% | 33.3% | -0.1 | 80% | ❌ 47 pts to go |
| P06M | 15579 | 36.2% | 36.2% | +0.1 | n/a | no target |
| P06T | 40041 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 697 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22230 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 91.5% | 91.5% | +0.0 | 100% | 🟡 8 pts to go |
| P10 | 2389 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1527 | 6.1% | 6.1% | -0.3 | n/a | no target |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 117988 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 80.2% | 80.2% | +0.4 | n/a | no target |
| P01T | 194 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P01_GOLD | 627 | 51.7% | 51.7% | +0.1 | 85% | ❌ 33 pts to go |
| P02 | 466 | 57.5% | 57.5% | +0.0 | 90% | ❌ 32 pts to go |
| P03 | 265 | 42.3% | 42.3% | -0.3 | 85% | ❌ 43 pts to go |
| P04 | 3733 | 27.8% | 27.8% | -0.1 | 90% | ❌ 62 pts to go |
| P05 | 424 | 32.3% | 32.3% | -0.4 | 75% | ❌ 43 pts to go |
| P06M | 15579 | 86.1% | 86.1% | -1.0 | n/a | no target |
| P06T | 40041 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 697 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22230 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 83.4% | 83.4% | +0.0 | 95% | ❌ 12 pts to go |
| P10 | 2389 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1527 | 5.2% | 5.2% | -0.2 | n/a | no target |
| P12 | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 117988 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 78.6% | 78.6% | +0.3 | n/a | no target |
| P01T | 194 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P01_GOLD | 627 | 51.8% | 51.8% | +0.0 | 85% | ❌ 33 pts to go |
| P02 | 466 | 52.6% | 52.6% | +0.0 | 90% | ❌ 37 pts to go |
| P03 | 265 | 43.4% | 43.4% | -0.3 | 85% | ❌ 42 pts to go |
| P04 | 3733 | 23.8% | 23.8% | +0.0 | 90% | ❌ 66 pts to go |
| P05 | 424 | 42.9% | 42.9% | -0.5 | 75% | ❌ 32 pts to go |
| P06M | 15579 | 76.7% | 76.7% | -1.1 | n/a | no target |
| P06T | 40041 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 697 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22230 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 0.3% | 0.3% | +0.0 | 95% | ❌ 95 pts to go |
| P10 | 2389 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1527 | 4.3% | 4.3% | -0.2 | n/a | no target |
| P12 | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 117988 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 90.1% | 90.1% | +0.2 | n/a | no target |
| P01T | 194 | 94.3% | 94.3% | +0.0 | n/a | no target |
| P01_GOLD | 627 | 85.2% | 85.2% | -0.1 | 100% | ❌ 15 pts to go |
| P02 | 466 | 76.6% | 76.6% | +0.2 | 100% | ❌ 23 pts to go |
| P03 | 265 | 91.3% | 91.3% | +0.0 | n/a | no target |
| P04 | 3733 | 49.0% | 49.0% | +0.2 | 95% | ❌ 46 pts to go |
| P05 | 424 | 77.4% | 77.4% | -0.1 | 95% | ❌ 18 pts to go |
| P06M | 15579 | 99.0% | 99.0% | +0.1 | n/a | no target |
| P06T | 40041 | 91.8% | 91.8% | +1.2 | n/a | no target |
| P06 | 272 | 22.8% | 22.8% | -0.3 | n/a | no target |
| P07 | 697 | 13.2% | 13.2% | -0.6 | n/a | no target |
| P08 | 22230 | 7.1% | 7.1% | +0.0 | n/a | no target |
| P09 | 307 | 98.7% | 98.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10 | 2389 | 71.0% | 71.0% | +0.0 | n/a | no target |
| P11 | 1527 | 69.2% | 69.2% | +1.1 | n/a | no target |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 117988 | 99.8% | 99.8% | +0.1 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 90.1% | 90.1% | +0.2 | n/a | no target |
| P01T | 194 | 94.3% | 94.3% | +0.0 | n/a | no target |
| P01_GOLD | 627 | 88.4% | 88.4% | -0.1 | 100% | ❌ 12 pts to go |
| P02 | 466 | 77.7% | 77.9% | +0.2 | 100% | ❌ 22 pts to go |
| P03 | 265 | 92.1% | 92.1% | +0.1 | n/a | no target |
| P04 | 3733 | 52.2% | 52.2% | +0.3 | 95% | ❌ 43 pts to go |
| P05 | 424 | 89.4% | 89.4% | -0.2 | 70% | ✅ met |
| P06M | 15579 | 99.0% | 99.0% | +0.1 | n/a | no target |
| P06T | 40041 | 91.8% | 91.8% | +1.2 | n/a | no target |
| P06 | 272 | 22.8% | 22.8% | -0.3 | n/a | no target |
| P07 | 697 | 13.2% | 13.2% | -0.6 | n/a | no target |
| P08 | 22230 | 7.1% | 7.1% | +0.0 | n/a | no target |
| P09 | 307 | 98.7% | 98.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10 | 2389 | 71.0% | 71.0% | +0.0 | n/a | no target |
| P11 | 1527 | 69.4% | 69.4% | +1.2 | n/a | no target |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 117988 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 194 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 627 | 16.7% | 16.7% | -0.1 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 363 rows, 28.9% filled |
| P02 | 466 | 11.2% | 11.2% | +0.0 | n/a | no target · rows from a source that publishes bids: 290 rows, 17.9% filled |
| P03 | 265 | 12.8% | 12.8% | -0.1 | n/a | no target · rows from a source that publishes bids: 139 rows, 24.5% filled |
| P04 | 3733 | 1.5% | 1.5% | +0.0 | n/a | no target · rows from a source that publishes bids: 871 rows, 6.3% filled |
| P05 | 424 | 2.6% | 2.6% | +0.0 | n/a | no target · rows from a source that publishes bids: 50 rows, 22.0% filled |
| P06M | 15579 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 40041 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 697 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22230 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 4.2% | 4.2% | +0.0 | n/a | no target · rows from a source that publishes bids: 293 rows, 4.4% filled |
| P10 | 2389 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1527 | 0.9% | 0.9% | +0.0 | n/a | no target · rows from a source that publishes bids: 90 rows, 14.4% filled |
| P12 | 15 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 15 rows, 0.0% filled |
| P13 | 117988 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 194 | 0.0% | 97.9% | +0.0 | n/a | no target |
| P01_GOLD | 627 | 53.1% | 82.5% | -0.1 | 90% | ❌ 37 pts to go |
| P02 | 466 | 52.4% | 87.6% | +0.0 | 90% | ❌ 38 pts to go |
| P03 | 265 | 44.2% | 80.8% | -0.3 | 90% | ❌ 46 pts to go |
| P04 | 3733 | 19.0% | 93.9% | -0.1 | 90% | ❌ 71 pts to go |
| P05 | 424 | 0.0% | 83.5% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 15579 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 40041 | 0.0% | 99.8% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 697 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 22230 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 307 | 2.3% | 3.9% | +0.0 | 90% | ❌ 88 pts to go |
| P10 | 2389 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1527 | 3.9% | 97.1% | -0.2 | n/a | no target |
| P12 | 15 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 117988 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 194 | 0.5% | 98.5% | +0.0 | n/a | no target |
| P01_GOLD | 627 | 25.8% | 55.2% | -0.1 | 90% | ❌ 64 pts to go |
| P02 | 466 | 51.5% | 86.7% | +0.0 | n/a | no target |
| P03 | 265 | 24.2% | 60.8% | -0.1 | n/a | no target |
| P04 | 3733 | 20.9% | 95.7% | -0.1 | n/a | no target |
| P05 | 424 | 0.5% | 84.0% | +0.0 | n/a | no target |
| P06M | 15579 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 40041 | 0.1% | 99.9% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 697 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 22230 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 307 | 41.0% | 42.7% | +0.0 | n/a | no target |
| P10 | 2389 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1527 | 3.5% | 96.7% | -0.2 | n/a | no target |
| P12 | 15 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 117988 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 194 | 2.1% | 100.0% | +0.0 | n/a | no target |
| P01_GOLD | 627 | 51.7% | 81.0% | -0.1 | 95% | ❌ 43 pts to go |
| P02 | 466 | 56.4% | 91.6% | +0.0 | n/a | no target |
| P03 | 265 | 46.4% | 83.0% | -0.4 | n/a | no target |
| P04 | 3733 | 21.1% | 96.0% | -0.1 | n/a | no target |
| P05 | 424 | 4.5% | 88.0% | +0.0 | n/a | no target |
| P06M | 15579 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 40041 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 697 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 22230 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 307 | 62.5% | 64.2% | +0.0 | n/a | no target |
| P10 | 2389 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1527 | 3.9% | 97.1% | -0.2 | n/a | no target |
| P12 | 15 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 117988 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 98.5% | 98.5% | -1.5 | 100% | 🟡 2 pts to go |
| P01T | 194 | 98.5% | 98.5% | -1.5 | 100% | 🟡 2 pts to go |
| P01_GOLD | 627 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P02 | 466 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P03 | 265 | 99.2% | 99.2% | -0.8 | 100% | 🟡 1 pts to go |
| P04 | 3733 | 98.7% | 98.7% | -1.3 | 100% | 🟡 1 pts to go |
| P05 | 424 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P06M | 15579 | 94.9% | 94.9% | -5.1 | 100% | 🟡 5 pts to go |
| P06T | 40041 | 90.1% | 90.1% | -9.9 | 100% | 🟡 10 pts to go |
| P06 | 272 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P07 | 697 | 98.9% | 98.9% | -1.1 | 100% | 🟡 1 pts to go |
| P08 | 22230 | 98.4% | 98.4% | -1.6 | 100% | 🟡 2 pts to go |
| P09 | 307 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2389 | 97.9% | 97.9% | -2.1 | 100% | 🟡 2 pts to go |
| P11 | 1527 | 95.5% | 95.5% | -4.5 | 100% | 🟡 4 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 117988 | 83.5% | 83.5% | -16.5 | 100% | ❌ 16 pts to go |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 98.5% | 98.5% | -1.5 | 100% | 🟡 2 pts to go |
| P01T | 194 | 98.5% | 98.5% | -1.5 | 100% | 🟡 2 pts to go |
| P01_GOLD | 627 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P02 | 466 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P03 | 265 | 99.2% | 99.2% | -0.8 | 100% | 🟡 1 pts to go |
| P04 | 3733 | 98.7% | 98.7% | -1.3 | 100% | 🟡 1 pts to go |
| P05 | 424 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P06M | 15579 | 94.9% | 94.9% | -5.1 | 100% | 🟡 5 pts to go |
| P06T | 40041 | 90.1% | 90.1% | -9.9 | 100% | 🟡 10 pts to go |
| P06 | 272 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P07 | 697 | 98.9% | 98.9% | -1.1 | 100% | 🟡 1 pts to go |
| P08 | 22230 | 98.4% | 98.4% | -1.6 | 100% | 🟡 2 pts to go |
| P09 | 307 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2389 | 97.9% | 97.9% | -2.1 | 100% | 🟡 2 pts to go |
| P11 | 1527 | 95.5% | 95.5% | -4.5 | 100% | 🟡 4 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 117988 | 83.5% | 83.5% | -16.5 | 100% | ❌ 16 pts to go |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 98.5% | 98.5% | -1.5 | 100% | 🟡 2 pts to go |
| P01T | 194 | 98.5% | 98.5% | -1.5 | 100% | 🟡 2 pts to go |
| P01_GOLD | 627 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P02 | 466 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P03 | 265 | 99.2% | 99.2% | -0.8 | 100% | 🟡 1 pts to go |
| P04 | 3733 | 98.7% | 98.7% | -1.3 | 100% | 🟡 1 pts to go |
| P05 | 424 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P06M | 15579 | 94.9% | 94.9% | -5.1 | 100% | 🟡 5 pts to go |
| P06T | 40041 | 90.1% | 90.1% | -9.9 | 100% | 🟡 10 pts to go |
| P06 | 272 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P07 | 697 | 98.9% | 98.9% | -1.1 | 100% | 🟡 1 pts to go |
| P08 | 22230 | 98.4% | 98.4% | -1.6 | 100% | 🟡 2 pts to go |
| P09 | 307 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2389 | 97.9% | 97.9% | -2.1 | 100% | 🟡 2 pts to go |
| P11 | 1527 | 95.5% | 95.5% | -4.5 | 100% | 🟡 4 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 117988 | 83.5% | 83.5% | -16.5 | 100% | ❌ 16 pts to go |

