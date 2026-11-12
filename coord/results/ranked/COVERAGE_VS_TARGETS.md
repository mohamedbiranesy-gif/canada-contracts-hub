# Coverage vs the downstream team's targets — 2026-11-12

Benchmarks (field × package with a numeric target): **50 of 438 met** (11.4%); 106 within 10 points; 282 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 196, P01T 198, P01_GOLD 625, P02 463, P03 260, P04 3558, P05 419, P06M 19102, P06T 43728, P06 254, P07 666, P08 21518, P09 278, P10R 0, P10 2146, P11 1633, P12 16, P13 164561

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 196 | 0.0% | 15.3% | 8 | vendor GST/HST number (181 rows) |
| P01T | 198 | 1.0% | 33.8% | 8 | payment terms (155 rows) |
| P01_GOLD | 625 | 24.2% | 70.9% | 10 | payment terms (217 rows) |
| P02 | 463 | 7.6% | 55.1% | 9 | PO rule (353 rows) |
| P03 | 260 | 15.0% | 56.2% | 9 | PO rule (128 rows) |
| P04 | 3558 | 1.2% | 17.1% | 6 | PO rule (3357 rows) |
| P05 | 419 | 1.0% | 16.9% | 7 | payment terms (347 rows) |
| P06M | 19102 | 0.0% | 2.7% | 7 | PO rule (18716 rows) |
| P06T | 43728 | 0.1% | 9.8% | 6 | PO rule (43383 rows) |
| P06 | 254 | 0.0% | 11.8% | 6 | reference to quote (PO / contract / vendor id) (254 rows) |
| P07 | 666 | 0.0% | 2.4% | 6 | reference to quote (PO / contract / vendor id) (666 rows) |
| P08 | 21518 | 0.0% | 0.6% | 6 | reference to quote (PO / contract / vendor id) (21518 rows) |
| P09 | 278 | 1.4% | 44.2% | 8 | payment terms (260 rows) |
| P10 | 2146 | 0.0% | 1.3% | 5 | reference to quote (PO / contract / vendor id) (2146 rows) |
| P11 | 1633 | 0.1% | 6.9% | 6 | PO rule (1566 rows) |
| P12 | 16 | 0.0% | 50.0% | 9 | PO rule (15 rows) |
| P13 | 164561 | 0.0% | 0.2% | 6 | reference to quote (PO / contract / vendor id) (164561 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 196 | 8 | 55 | 133 | 0 | 0 | 71 |
| P01T | 198 | 23 | 38 | 137 | 0 | 0 | 68 |
| P01_GOLD | 625 | 224 | 198 | 203 | 0 | 0 | 82 |
| P02 | 463 | 0 | 188 | 275 | 0 | 0 | 66 |
| P03 | 260 | 0 | 0 | 247 | 13 | 0 | 57 |
| P04 | 3558 | 0 | 0 | 2918 | 640 | 0 | 46 |
| P05 | 419 | 14 | 29 | 363 | 13 | 0 | 51 |
| P06M | 19102 | 0 | 18 | 19018 | 66 | 0 | 46 |
| P06T | 43728 | 0 | 26 | 28371 | 15331 | 0 | 38 |
| P06 | 254 | 16 | 47 | 191 | 0 | 0 | 70 |
| P07 | 666 | 0 | 21 | 620 | 25 | 0 | 54 |
| P08 | 21518 | 0 | 0 | 18861 | 2657 | 0 | 44 |
| P09 | 278 | 4 | 11 | 262 | 1 | 0 | 53 |
| P10 | 2146 | 3 | 13 | 1454 | 676 | 0 | 41 |
| P11 | 1633 | 7 | 13 | 36 | 0 | 1577 | 23 |
| P12 | 16 | 0 | 0 | 16 | 0 | 0 | 54 |
| P13 | 164561 | 12 | 63 | 164473 | 13 | 0 | 38 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 196 | 145 | 74.0% | tax treatment (27) |
| P01T | 198 | 117 | 59.1% | bill-to legal name and address (67) |
| P01_GOLD | 625 | 472 | 75.5% | bill-to legal name and address (99) |
| P02 | 463 | 312 | 67.4% | the buyer's PO / reference rule (85) |
| P03 | 260 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (260) |
| P04 | 3558 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (3558) |
| P05 | 419 | 44 | 10.5% | a confirmed invoicing / AP or finance channel (332) |
| P06M | 19102 | 188 | 1.0% | a confirmed invoicing / AP or finance channel (18849) |
| P06T | 43728 | 239 | 0.5% | a confirmed invoicing / AP or finance channel (43095) |
| P06 | 254 | 43 | 16.9% | the buyer's PO / reference rule (112) |
| P07 | 666 | 6 | 0.9% | the buyer's PO / reference rule (270) |
| P08 | 21518 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (21518) |
| P09 | 278 | 40 | 14.4% | a confirmed invoicing / AP or finance channel (227) |
| P10 | 2146 | 7 | 0.3% | a confirmed invoicing / AP or finance channel (2068) |
| P11 | 1633 | 14 | 0.9% | a confirmed invoicing / AP or finance channel (1577) |
| P12 | 16 | 4 | 25.0% | a confirmed invoicing / AP or finance channel (11) |
| P13 | 164561 | 42 | 0.0% | a confirmed invoicing / AP or finance channel (162214) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 196 | 5 | 2.6% | 7 | 0 | the vendor's GST/HST number (BN9) (181) |
| P01T | 198 | 79 | 39.9% | 3 | 0 | the vendor's GST/HST number (BN9) (71) |
| P01_GOLD | 625 | 397 | 63.5% | 10 | 0 | the vendor's GST/HST number (BN9) (152) |
| P02 | 463 | 212 | 45.8% | 21 | 0 | the vendor's GST/HST number (BN9) (200) |
| P03 | 260 | 17 | 6.5% | 0 | 128 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (97) |
| P04 | 3558 | 43 | 1.2% | 7 | 841 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2609) |
| P05 | 419 | 19 | 4.5% | 8 | 119 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (205) |
| P06M | 19102 | 7 | 0.0% | 12 | 479 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (18281) |
| P06T | 43728 | 263 | 0.6% | 14 | 11004 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (32023) |
| P06 | 254 | 26 | 10.2% | 49 | 0 | the vendor's GST/HST number (BN9) (116) |
| P07 | 666 | 6 | 0.9% | 109 | 33 | the vendor's GST/HST number (BN9) (310) |
| P08 | 21518 | 4 | 0.0% | 14 | 4997 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (16463) |
| P09 | 278 | 38 | 13.7% | 0 | 112 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (103) |
| P10 | 2146 | 7 | 0.3% | 14 | 269 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (1774) |
| P11 | 1633 | 7 | 0.4% | 3 | 0 | a confirmed invoicing / AP or finance channel (1561) |
| P12 | 16 | 3 | 18.8% | 0 | 6 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (5) |
| P13 | 164561 | 10 | 0.0% | 712 | 41738 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (120285) |
| **all** | 259621 | 1143 | 0.4% | 983 | 59726 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 188 | 0 | 0 | 0 | 130 | 9 | 0 | 144 | 159 | 13 |
| P01T | 175 | 0 | 0 | 0 | 102 | 61 | 27 | 139 | 156 | 7 |
| P01_GOLD | 401 | 0 | 0 | 0 | 12 | 81 | 30 | 196 | 232 | 61 |
| P02 | 463 | 0 | 463 | 0 | 38 | 55 | 15 | 353 | 282 | 23 |
| P03 | 260 | 0 | 260 | 0 | 17 | 45 | 27 | 128 | 136 | 22 |
| P04 | 3558 | 0 | 3558 | 0 | 1528 | 1292 | 966 | 3357 | 3109 | 159 |
| P05 | 405 | 0 | 352 | 0 | 80 | 94 | 38 | 335 | 349 | 52 |
| P06M | 19102 | 0 | 19102 | 0 | 13604 | 1568 | 105 | 18716 | 18460 | 450 |
| P06T | 43728 | 0 | 43728 | 0 | 39432 | 29156 | 18581 | 43383 | 42968 | 903 |
| P06 | 238 | 0 | 0 | 0 | 113 | 66 | 42 | 170 | 201 | 9 |
| P07 | 666 | 0 | 666 | 0 | 425 | 271 | 117 | 622 | 625 | 11 |
| P08 | 21518 | 0 | 21518 | 0 | 16420 | 9710 | 3931 | 21244 | 20892 | 402 |
| P09 | 274 | 0 | 254 | 0 | 12 | 71 | 1 | 248 | 262 | 41 |
| P10 | 2143 | 0 | 2110 | 0 | 1114 | 1169 | 977 | 2075 | 2037 | 110 |
| P11 | 1626 | 1577 | 1529 | 0 | 792 | 1161 | 509 | 1566 | 1563 | 58 |
| P12 | 16 | 0 | 14 | 0 | 1 | 4 | 0 | 15 | 15 | 1 |
| P13 | 164549 | 0 | 164108 | 0 | 132135 | 105864 | 20 | 164199 | 163354 | 36 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_phone | P13 | 52.1% | 95% | 70644 |
| buyer_logo_url | P13 | 63.9% | 95% | 51194 |
| buyer_legal_name_as_published | P13 | 35.7% | 60% | 40040 |
| buyer_bn_as_published | P13 | 8.2% | 30% | 35918 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 32877 |
| ap_system_hint | P13 | 0.4% | 20% | 32309 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 24552 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 24499 |
| buyer_payment_method_preference | P13 | 0.5% | 15% | 23812 |
| mta_sts | P13 | 94.6% | 100% | 8928 |
| tls_rpt | P13 | 94.6% | 100% | 8928 |
| bimi | P13 | 94.6% | 100% | 8928 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 8733 |
| vendor_registered_address | P08 | 30.2% | 70% | 8562 |
| ap_system_hint | P06T | 0.6% | 20% | 8474 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 6470 |
| buyer_tax_exempt_status | P06T | 0.2% | 15% | 6458 |
| buyer_payment_method_preference | P06T | 0.5% | 15% | 6350 |
| buyer_phone | P08 | 68.5% | 95% | 5700 |
| invoice_reference_hint | P08 | 1.3% | 25% | 5106 |
| buyer_legal_name_as_published | P08 | 54.9% | 75% | 4331 |
| buyer_ap_cycle_published | P08 | 0.1% | 20% | 4293 |
| buyer_bn_as_published | P08 | 15.3% | 35% | 4239 |
| vendor_bn9 | P08 | 30.6% | 50% | 4167 |
| vendor_phone | P08 | 65.9% | 85% | 4114 |
| ap_system_hint | P08 | 1.0% | 20% | 4086 |
| vendor_emails | P08 | 56.4% | 75% | 4013 |
| buyer_ap_cycle_published | P06M | 0.0% | 20% | 3814 |
| ap_system_hint | P06M | 1.1% | 20% | 3614 |
| buyer_esignature_preference | P08 | 0.5% | 15% | 3126 |
| buyer_tax_exempt_status | P08 | 0.5% | 15% | 3123 |
| buyer_payment_method_preference | P08 | 0.6% | 15% | 3095 |
| vendor_trading_name | P08 | 36.3% | 50% | 2941 |
| buyer_address | P08 | 81.7% | 95% | 2862 |
| buyer_esignature_preference | P06M | 0.5% | 15% | 2767 |
| buyer_tax_exempt_status | P06M | 0.7% | 15% | 2728 |
| buyer_payment_method_preference | P06M | 0.8% | 15% | 2722 |
| average_contract_duration_days | P04 | 19.3% | 90% | 2517 |
| mta_sts | P06T | 94.3% | 100% | 2505 |
| tls_rpt | P06T | 94.3% | 100% | 2505 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 91.3% | 91.3% | +2.2 | 50% | ✅ met |
| P01T | 198 | 94.9% | 94.9% | +1.1 | 50% | ✅ met |
| P01_GOLD | 625 | 92.5% | 94.7% | +0.3 | 95% | 🟡 2 pts to go |
| P02 | 463 | 74.9% | 76.5% | +0.9 | 95% | ❌ 20 pts to go |
| P03 | 260 | 80.8% | 84.2% | -0.6 | 95% | ❌ 14 pts to go |
| P04 | 3558 | 31.3% | 33.0% | +1.1 | 90% | ❌ 59 pts to go |
| P05 | 419 | 38.9% | 41.8% | +0.3 | 70% | ❌ 31 pts to go |
| P06M | 19102 | 91.8% | 91.8% | +0.0 | n/a | no target |
| P06T | 43728 | 99.0% | 99.0% | +0.4 | n/a | no target |
| P06 | 254 | 33.1% | 33.1% | -1.3 | 30% | ✅ met |
| P07 | 666 | 6.6% | 6.6% | -0.3 | 30% | ❌ 23 pts to go |
| P08 | 21518 | 1.3% | 1.3% | +0.0 | 25% | ❌ 24 pts to go |
| P09 | 278 | 98.9% | 99.6% | -0.1 | 100% | 🟡 1 pts to go |
| P10 | 2146 | 3.3% | 3.3% | +0.2 | 25% | ❌ 22 pts to go |
| P11 | 1633 | 52.8% | 53.6% | +5.9 | 60% | 🟡 7 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 164561 | 99.6% | 99.6% | -0.1 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 198 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 625 | 6.1% | 6.1% | +0.0 | 50% | ❌ 44 pts to go |
| P02 | 463 | 6.0% | 6.0% | -0.2 | 50% | ❌ 44 pts to go |
| P03 | 260 | 1.5% | 1.5% | +0.0 | 40% | ❌ 38 pts to go |
| P04 | 3558 | 0.6% | 0.6% | +0.1 | 30% | ❌ 29 pts to go |
| P05 | 419 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 19102 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 43728 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 254 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 666 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21518 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 278 | 0.7% | 0.7% | +0.0 | 50% | ❌ 49 pts to go |
| P10 | 2146 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1633 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P12 | 16 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 164561 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 86.7% | 86.7% | +4.5 | n/a | no target |
| P01T | 198 | 76.8% | 76.8% | +2.3 | 50% | ✅ met |
| P01_GOLD | 625 | 67.2% | 67.2% | +0.4 | 85% | ❌ 18 pts to go |
| P02 | 463 | 65.9% | 65.9% | +1.1 | 90% | ❌ 24 pts to go |
| P03 | 260 | 60.0% | 60.0% | +0.3 | 85% | ❌ 25 pts to go |
| P04 | 3558 | 28.6% | 28.6% | +1.0 | 85% | ❌ 56 pts to go |
| P05 | 419 | 29.1% | 29.1% | +0.2 | 60% | ❌ 31 pts to go |
| P06M | 19102 | 91.5% | 91.5% | +0.0 | n/a | no target |
| P06T | 43728 | 98.9% | 98.9% | +0.5 | n/a | no target |
| P06 | 254 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 666 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21518 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 278 | 95.7% | 95.7% | -0.4 | 100% | 🟡 4 pts to go |
| P10 | 2146 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1633 | 49.7% | 49.7% | +6.4 | 60% | ❌ 10 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 164561 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 198 | 0.0% | 0.0% | +0.0 | 30% | ❌ 30 pts to go |
| P01_GOLD | 625 | 51.5% | 51.5% | +0.7 | 80% | ❌ 28 pts to go |
| P02 | 463 | 57.9% | 57.9% | +1.0 | 60% | 🟡 2 pts to go |
| P03 | 260 | 49.6% | 49.6% | -0.6 | 80% | ❌ 30 pts to go |
| P04 | 3558 | 23.6% | 23.6% | +0.7 | 50% | ❌ 26 pts to go |
| P05 | 419 | 11.7% | 11.7% | +0.3 | 40% | ❌ 28 pts to go |
| P06M | 19102 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 43728 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 254 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 666 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21518 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 278 | 81.3% | 81.3% | -2.1 | 50% | ✅ met |
| P10 | 2146 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1633 | 4.0% | 4.0% | -1.6 | 40% | ❌ 36 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 164561 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 198 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 61.3% | 61.3% | +0.9 | 85% | ❌ 24 pts to go |
| P02 | 463 | 58.1% | 58.1% | +1.9 | 90% | ❌ 32 pts to go |
| P03 | 260 | 58.5% | 58.5% | -0.1 | 85% | ❌ 26 pts to go |
| P04 | 3558 | 24.4% | 24.4% | +0.8 | 85% | ❌ 61 pts to go |
| P05 | 419 | 19.6% | 19.6% | -0.1 | 50% | ❌ 30 pts to go |
| P06M | 19102 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 43728 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 254 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 666 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21518 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 278 | 97.1% | 97.1% | +0.0 | 100% | 🟡 3 pts to go |
| P10 | 2146 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1633 | 4.4% | 4.4% | -1.6 | 60% | ❌ 56 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 164561 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 198 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 13.1% | 13.1% | +0.2 | 60% | ❌ 47 pts to go |
| P02 | 463 | 6.9% | 6.9% | +0.9 | 50% | ❌ 43 pts to go |
| P03 | 260 | 8.1% | 8.1% | -0.3 | 50% | ❌ 42 pts to go |
| P04 | 3558 | 1.9% | 1.9% | +0.1 | 40% | ❌ 38 pts to go |
| P05 | 419 | 0.7% | 0.7% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 19102 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 43728 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 254 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 666 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21518 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 278 | 3.2% | 3.2% | -0.1 | 50% | ❌ 47 pts to go |
| P10 | 2146 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1633 | 0.6% | 0.6% | -0.3 | n/a | no target |
| P12 | 16 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 164561 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 198 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 36.2% | 36.2% | +1.4 | 80% | ❌ 44 pts to go |
| P02 | 463 | 52.5% | 52.5% | +0.6 | 90% | ❌ 38 pts to go |
| P03 | 260 | 33.8% | 33.8% | +1.1 | 80% | ❌ 46 pts to go |
| P04 | 3558 | 21.8% | 21.8% | +0.2 | 85% | ❌ 63 pts to go |
| P05 | 419 | 5.7% | 5.7% | +0.2 | 50% | ❌ 44 pts to go |
| P06M | 19102 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 43728 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 254 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 666 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21518 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 278 | 73.4% | 73.4% | -0.9 | 95% | ❌ 22 pts to go |
| P10 | 2146 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1633 | 3.2% | 3.2% | -1.1 | 50% | ❌ 47 pts to go |
| P12 | 16 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 164561 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 198 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 8.5% | 8.5% | +0.0 | 50% | ❌ 42 pts to go |
| P02 | 463 | 6.0% | 6.0% | -0.2 | 50% | ❌ 44 pts to go |
| P03 | 260 | 2.3% | 2.3% | +0.4 | 30% | ❌ 28 pts to go |
| P04 | 3558 | 0.5% | 0.5% | +0.0 | 30% | ❌ 30 pts to go |
| P05 | 419 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 19102 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 43728 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 254 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 666 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21518 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 278 | 0.4% | 0.4% | +0.1 | n/a | no target |
| P10 | 2146 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1633 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P12 | 16 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 164561 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 198 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 463 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 260 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3558 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 419 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 19102 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 43728 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 254 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 666 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 21518 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 278 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2146 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1633 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 164561 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 7.7% | 7.7% | -3.9 | 70% | ❌ 62 pts to go |
| P01T | 198 | 54.5% | 54.5% | +4.0 | 60% | 🟡 6 pts to go |
| P01_GOLD | 625 | 73.4% | 73.4% | -1.4 | 90% | ❌ 17 pts to go |
| P02 | 463 | 54.0% | 54.0% | +0.4 | 85% | ❌ 31 pts to go |
| P03 | 260 | 66.5% | 66.5% | -3.1 | 90% | ❌ 24 pts to go |
| P04 | 3558 | 35.2% | 35.2% | +0.2 | 75% | ❌ 40 pts to go |
| P05 | 419 | 53.2% | 53.2% | -1.5 | 50% | ✅ met |
| P06M | 19102 | 3.0% | 3.0% | -0.2 | n/a | no target |
| P06T | 43728 | 51.9% | 51.9% | +4.6 | n/a | no target |
| P06 | 254 | 43.7% | 43.7% | -0.3 | 40% | ✅ met |
| P07 | 666 | 32.6% | 32.6% | -0.4 | 50% | ❌ 17 pts to go |
| P08 | 21518 | 30.6% | 30.6% | +0.1 | 50% | ❌ 19 pts to go |
| P09 | 278 | 58.6% | 58.6% | +0.3 | 80% | ❌ 21 pts to go |
| P10 | 2146 | 34.4% | 34.4% | -0.1 | 40% | 🟡 6 pts to go |
| P11 | 1633 | 49.5% | 49.5% | +2.6 | 60% | ❌ 10 pts to go |
| P12 | 16 | 56.2% | 56.2% | -3.8 | 85% | ❌ 29 pts to go |
| P13 | 164561 | 28.7% | 28.7% | -3.0 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 56.1% | 56.1% | -3.6 | n/a | no target |
| P01T | 198 | 56.1% | 56.1% | +5.1 | n/a | no target |
| P01_GOLD | 625 | 71.8% | 71.8% | -0.9 | 95% | ❌ 23 pts to go |
| P02 | 463 | 74.7% | 74.7% | +0.9 | 95% | ❌ 20 pts to go |
| P03 | 260 | 67.7% | 67.7% | -4.2 | 95% | ❌ 27 pts to go |
| P04 | 3558 | 49.7% | 49.7% | +0.5 | 95% | ❌ 45 pts to go |
| P05 | 419 | 56.8% | 56.8% | -1.5 | 70% | ❌ 13 pts to go |
| P06M | 19102 | 42.3% | 42.3% | -3.7 | n/a | no target |
| P06T | 43728 | 61.0% | 61.0% | +4.8 | n/a | no target |
| P06 | 254 | 41.3% | 41.3% | +0.3 | 80% | ❌ 39 pts to go |
| P07 | 666 | 32.1% | 32.1% | +0.2 | 70% | ❌ 38 pts to go |
| P08 | 21518 | 30.2% | 30.2% | -0.1 | 70% | ❌ 40 pts to go |
| P09 | 278 | 86.3% | 86.3% | -0.3 | 100% | ❌ 14 pts to go |
| P10 | 2146 | 35.3% | 35.3% | -0.2 | 70% | ❌ 35 pts to go |
| P11 | 1633 | 55.2% | 55.2% | +2.7 | 75% | ❌ 20 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 164561 | 24.2% | 24.2% | -2.7 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 25.0% | 25.0% | +7.9 | n/a | no target |
| P01T | 198 | 59.1% | 59.1% | +5.5 | n/a | no target |
| P01_GOLD | 625 | 49.0% | 49.0% | -0.8 | 60% | ❌ 11 pts to go |
| P02 | 463 | 56.2% | 56.2% | +0.0 | 60% | 🟡 4 pts to go |
| P03 | 260 | 53.8% | 53.8% | -1.3 | 60% | 🟡 6 pts to go |
| P04 | 3558 | 42.3% | 42.3% | +0.2 | 55% | ❌ 13 pts to go |
| P05 | 419 | 23.6% | 23.6% | -1.0 | 50% | ❌ 26 pts to go |
| P06M | 19102 | 9.2% | 9.2% | +2.4 | n/a | no target |
| P06T | 43728 | 51.5% | 51.5% | +0.6 | n/a | no target |
| P06 | 254 | 48.4% | 48.4% | +0.8 | n/a | no target |
| P07 | 666 | 41.6% | 41.6% | +0.7 | 55% | ❌ 13 pts to go |
| P08 | 21518 | 36.3% | 36.3% | +0.1 | 50% | ❌ 14 pts to go |
| P09 | 278 | 72.7% | 72.7% | +0.4 | 70% | ✅ met |
| P10 | 2146 | 47.8% | 47.8% | +1.0 | 55% | 🟡 7 pts to go |
| P11 | 1633 | 55.4% | 55.4% | +3.2 | 50% | ✅ met |
| P12 | 16 | 87.5% | 87.5% | +0.8 | n/a | no target |
| P13 | 164561 | 3.1% | 3.1% | -0.3 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 41.3% | 41.3% | -9.1 | n/a | no target |
| P01T | 198 | 75.8% | 75.8% | +1.3 | n/a | no target |
| P01_GOLD | 625 | 49.6% | 49.6% | -0.9 | 70% | ❌ 20 pts to go |
| P02 | 463 | 57.2% | 57.2% | -1.0 | 70% | ❌ 13 pts to go |
| P03 | 260 | 50.8% | 50.8% | -0.5 | 70% | ❌ 19 pts to go |
| P04 | 3558 | 54.9% | 54.9% | +0.8 | 65% | ❌ 10 pts to go |
| P05 | 419 | 28.9% | 28.9% | +0.5 | 60% | ❌ 31 pts to go |
| P06M | 19102 | 31.2% | 31.2% | -5.4 | n/a | no target |
| P06T | 43728 | 73.8% | 73.8% | -6.2 | n/a | no target |
| P06 | 254 | 70.9% | 70.9% | +2.0 | 40% | ✅ met |
| P07 | 666 | 65.8% | 65.8% | +0.9 | 85% | ❌ 19 pts to go |
| P08 | 21518 | 65.9% | 65.9% | +0.6 | 85% | ❌ 19 pts to go |
| P09 | 278 | 57.9% | 57.9% | -1.4 | 85% | ❌ 27 pts to go |
| P10 | 2146 | 66.1% | 66.1% | +2.6 | 85% | ❌ 19 pts to go |
| P11 | 1633 | 63.7% | 63.7% | +1.8 | 75% | ❌ 11 pts to go |
| P12 | 16 | 37.5% | 37.5% | +10.8 | n/a | no target |
| P13 | 164561 | 91.8% | 91.8% | +0.6 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 46.4% | 46.4% | -10.2 | n/a | no target |
| P01T | 198 | 98.0% | 98.0% | +0.6 | n/a | no target |
| P01_GOLD | 625 | 78.7% | 78.7% | -0.9 | 90% | ❌ 11 pts to go |
| P02 | 463 | 82.7% | 82.7% | -1.2 | 90% | 🟡 7 pts to go |
| P03 | 260 | 86.9% | 86.9% | -0.9 | 90% | 🟡 3 pts to go |
| P04 | 3558 | 83.1% | 83.1% | -1.3 | 85% | 🟡 2 pts to go |
| P05 | 419 | 44.9% | 44.9% | +0.1 | 70% | ❌ 25 pts to go |
| P06M | 19102 | 37.6% | 37.6% | -6.0 | n/a | no target |
| P06T | 43728 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 254 | 99.2% | 99.2% | -0.1 | 50% | ✅ met |
| P07 | 666 | 99.8% | 99.8% | -0.1 | 100% | 🟡 0 pts to go |
| P08 | 21518 | 99.9% | 99.9% | +0.1 | 100% | 🟡 0 pts to go |
| P09 | 278 | 78.4% | 78.4% | -1.4 | 100% | ❌ 22 pts to go |
| P10 | 2146 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1633 | 97.7% | 97.7% | +0.4 | 100% | 🟡 2 pts to go |
| P12 | 16 | 56.2% | 56.2% | +2.9 | n/a | no target |
| P13 | 164561 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 18.4% | 18.4% | +2.9 | n/a | no target |
| P01T | 198 | 67.7% | 67.7% | +2.6 | n/a | no target |
| P01_GOLD | 625 | 42.7% | 42.7% | -0.8 | 70% | ❌ 27 pts to go |
| P02 | 463 | 48.4% | 48.4% | -0.3 | 75% | ❌ 27 pts to go |
| P03 | 260 | 44.6% | 44.6% | +1.3 | 75% | ❌ 30 pts to go |
| P04 | 3558 | 38.8% | 38.8% | +0.1 | 70% | ❌ 31 pts to go |
| P05 | 419 | 21.7% | 21.7% | -0.3 | 55% | ❌ 33 pts to go |
| P06M | 19102 | 5.8% | 5.8% | +1.0 | n/a | no target |
| P06T | 43728 | 66.5% | 66.5% | +4.4 | n/a | no target |
| P06 | 254 | 52.0% | 52.0% | +5.1 | n/a | no target |
| P07 | 666 | 52.1% | 52.1% | +2.1 | 70% | ❌ 18 pts to go |
| P08 | 21518 | 56.4% | 56.4% | +1.6 | 75% | ❌ 19 pts to go |
| P09 | 278 | 48.2% | 48.2% | -1.0 | 85% | ❌ 37 pts to go |
| P10 | 2146 | 44.2% | 44.2% | +0.6 | 80% | ❌ 36 pts to go |
| P11 | 1633 | 58.5% | 58.5% | +4.2 | 70% | ❌ 12 pts to go |
| P12 | 16 | 37.5% | 37.5% | -2.5 | n/a | no target |
| P13 | 164561 | 5.4% | 5.4% | +0.2 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 46.4% | 46.4% | -10.2 | n/a | no target |
| P01T | 198 | 96.0% | 96.0% | +1.2 | n/a | no target |
| P01_GOLD | 625 | 72.0% | 72.0% | -1.8 | 90% | ❌ 18 pts to go |
| P02 | 463 | 77.8% | 77.8% | -1.2 | 90% | ❌ 12 pts to go |
| P03 | 260 | 83.1% | 83.1% | -0.2 | 90% | 🟡 7 pts to go |
| P04 | 3558 | 78.0% | 78.0% | +1.6 | 85% | 🟡 7 pts to go |
| P05 | 419 | 43.4% | 43.4% | +0.3 | 75% | ❌ 32 pts to go |
| P06M | 19102 | 37.5% | 37.5% | -5.8 | n/a | no target |
| P06T | 43728 | 97.2% | 97.2% | +0.5 | n/a | no target |
| P06 | 254 | 92.1% | 92.1% | +1.6 | n/a | no target |
| P07 | 666 | 93.7% | 93.7% | +1.2 | 100% | 🟡 6 pts to go |
| P08 | 21518 | 92.8% | 92.8% | +2.0 | 100% | 🟡 7 pts to go |
| P09 | 278 | 66.9% | 66.9% | +0.8 | n/a | no target |
| P10 | 2146 | 89.9% | 89.9% | +3.1 | 100% | ❌ 10 pts to go |
| P11 | 1633 | 89.7% | 89.7% | +2.0 | n/a | no target |
| P12 | 16 | 56.2% | 56.2% | +9.5 | n/a | no target |
| P13 | 164561 | 68.4% | 68.4% | +3.2 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 44.9% | 44.9% | -1.6 | n/a | no target · QC vendors: 50 rows, 100.0% filled |
| P01T | 198 | 9.1% | 9.1% | -0.3 | n/a | no target · QC vendors: 5 rows, 60.0% filled |
| P01_GOLD | 625 | 43.7% | 43.7% | -0.1 | 95% | ❌ 51 pts to go · QC vendors: 51 rows, 98.0% filled |
| P02 | 463 | 56.2% | 56.2% | +0.6 | 95% | ❌ 39 pts to go · QC vendors: 110 rows, 100.0% filled |
| P03 | 260 | 44.6% | 44.6% | -1.4 | 95% | ❌ 50 pts to go · QC vendors: 19 rows, 100.0% filled |
| P04 | 3558 | 32.1% | 32.1% | -0.1 | 95% | ❌ 63 pts to go · QC vendors: 581 rows, 97.9% filled |
| P05 | 419 | 13.6% | 13.6% | -0.4 | n/a | no target · QC vendors: 34 rows, 94.1% filled |
| P06M | 19102 | 38.7% | 38.7% | -4.1 | n/a | no target · QC vendors: 5981 rows, 99.8% filled |
| P06T | 43728 | 4.5% | 4.5% | -0.8 | n/a | no target · QC vendors: 1914 rows, 75.5% filled |
| P06 | 254 | 8.3% | 8.3% | -0.1 | n/a | no target · QC vendors: 14 rows, 71.4% filled |
| P07 | 666 | 6.2% | 6.2% | -0.1 | n/a | no target · QC vendors: 36 rows, 72.2% filled |
| P08 | 21518 | 6.4% | 6.4% | -0.2 | n/a | no target · QC vendors: 1204 rows, 92.8% filled |
| P09 | 278 | 74.8% | 74.8% | -2.1 | 95% | ❌ 20 pts to go · QC vendors: 96 rows, 100.0% filled |
| P10 | 2146 | 15.2% | 15.2% | -0.4 | n/a | no target · QC vendors: 199 rows, 89.4% filled |
| P11 | 1633 | 12.9% | 12.9% | -1.9 | n/a | no target · QC vendors: 157 rows, 89.8% filled |
| P12 | 16 | 75.0% | 75.0% | +1.7 | n/a | no target · QC vendors: 3 rows, 100.0% filled |
| P13 | 164561 | 23.6% | 23.6% | -2.6 | n/a | no target · QC vendors: 38912 rows, 100.0% filled |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 55.6% | 55.6% | -3.3 | n/a | no target · vendors with a registry record: 109 rows, 100.0% filled |
| P01T | 198 | 56.1% | 56.1% | +5.1 | n/a | no target · vendors with a registry record: 111 rows, 100.0% filled |
| P01_GOLD | 625 | 80.0% | 80.0% | -1.5 | 100% | ❌ 20 pts to go · vendors with a registry record: 500 rows, 100.0% filled |
| P02 | 463 | 78.0% | 78.0% | +0.5 | 100% | ❌ 22 pts to go · vendors with a registry record: 361 rows, 100.0% filled |
| P03 | 260 | 76.5% | 76.5% | -4.5 | 100% | ❌ 24 pts to go · vendors with a registry record: 199 rows, 100.0% filled |
| P04 | 3558 | 50.4% | 50.4% | +0.7 | 100% | ❌ 50 pts to go · vendors with a registry record: 1793 rows, 100.0% filled |
| P05 | 419 | 61.6% | 61.6% | -1.7 | n/a | no target · vendors with a registry record: 258 rows, 100.0% filled |
| P06M | 19102 | 42.2% | 42.2% | -3.7 | n/a | no target · vendors with a registry record: 8063 rows, 100.0% filled |
| P06T | 43728 | 61.0% | 61.0% | +4.8 | n/a | no target · vendors with a registry record: 26677 rows, 100.0% filled |
| P06 | 254 | 42.1% | 42.1% | +0.7 | n/a | no target · vendors with a registry record: 107 rows, 100.0% filled |
| P07 | 666 | 32.7% | 32.7% | +0.4 | n/a | no target · vendors with a registry record: 218 rows, 100.0% filled |
| P08 | 21518 | 30.4% | 30.4% | +0.0 | n/a | no target · vendors with a registry record: 6533 rows, 100.0% filled |
| P09 | 278 | 89.6% | 89.6% | -1.0 | n/a | no target · vendors with a registry record: 249 rows, 100.0% filled |
| P10 | 2146 | 36.0% | 36.0% | -0.2 | n/a | no target · vendors with a registry record: 773 rows, 100.0% filled |
| P11 | 1633 | 55.9% | 55.9% | +2.3 | n/a | no target · vendors with a registry record: 913 rows, 100.0% filled |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 16 rows, 100.0% filled |
| P13 | 164561 | 24.2% | 24.2% | -2.7 | n/a | no target · vendors with a registry record: 39773 rows, 100.0% filled |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 95.4% | 95.4% | +1.6 | 90% | ✅ met |
| P01T | 198 | 69.2% | 69.2% | -3.2 | 90% | ❌ 21 pts to go |
| P01_GOLD | 625 | 87.0% | 87.0% | -0.7 | 95% | 🟡 8 pts to go |
| P02 | 463 | 88.1% | 88.1% | +0.3 | 95% | 🟡 7 pts to go |
| P03 | 260 | 82.7% | 82.7% | -1.7 | 85% | 🟡 2 pts to go |
| P04 | 3558 | 63.7% | 63.7% | +0.7 | 90% | ❌ 26 pts to go |
| P05 | 419 | 77.6% | 77.6% | -1.5 | 75% | ✅ met |
| P06M | 19102 | 91.8% | 91.8% | +0.2 | n/a | no target |
| P06T | 43728 | 33.3% | 33.3% | -4.0 | n/a | no target |
| P06 | 254 | 74.0% | 74.0% | +0.4 | 80% | 🟡 6 pts to go |
| P07 | 666 | 59.3% | 59.5% | -0.5 | 80% | ❌ 21 pts to go |
| P08 | 21518 | 54.9% | 54.9% | +0.5 | 75% | ❌ 20 pts to go |
| P09 | 278 | 74.5% | 74.5% | -2.4 | 95% | ❌ 20 pts to go |
| P10 | 2146 | 45.5% | 45.6% | -1.2 | 70% | ❌ 24 pts to go |
| P11 | 1633 | 28.9% | 28.9% | -2.4 | 65% | ❌ 36 pts to go |
| P12 | 16 | 75.0% | 75.0% | -5.0 | 80% | 🟡 5 pts to go |
| P13 | 164561 | 35.7% | 35.7% | -11.8 | 60% | ❌ 24 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 12.8% | 12.8% | -7.4 | 50% | ❌ 37 pts to go |
| P01T | 198 | 13.6% | 13.6% | -2.5 | n/a | no target |
| P01_GOLD | 625 | 18.9% | 18.9% | -0.6 | 40% | ❌ 21 pts to go |
| P02 | 463 | 19.7% | 19.7% | +0.6 | 40% | ❌ 20 pts to go |
| P03 | 260 | 20.8% | 20.8% | -0.5 | 40% | ❌ 19 pts to go |
| P04 | 3558 | 14.6% | 14.6% | -0.6 | 40% | ❌ 25 pts to go |
| P05 | 419 | 16.9% | 16.9% | -0.6 | 25% | 🟡 8 pts to go |
| P06M | 19102 | 8.9% | 8.9% | -2.7 | n/a | no target |
| P06T | 43728 | 4.9% | 4.9% | -2.0 | n/a | no target |
| P06 | 254 | 12.2% | 12.2% | -0.6 | 35% | ❌ 23 pts to go |
| P07 | 666 | 14.1% | 14.1% | +0.0 | 35% | ❌ 21 pts to go |
| P08 | 21518 | 15.3% | 15.3% | -0.1 | 35% | ❌ 20 pts to go |
| P09 | 278 | 16.9% | 16.9% | +0.6 | n/a | no target |
| P10 | 2146 | 5.6% | 5.6% | -1.1 | 30% | ❌ 24 pts to go |
| P11 | 1633 | 6.1% | 6.1% | -1.3 | n/a | no target |
| P12 | 16 | 6.2% | 6.2% | -0.5 | n/a | no target |
| P13 | 164561 | 8.2% | 8.2% | -4.1 | 30% | ❌ 22 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 198 | 85.4% | 85.4% | +1.0 | 100% | ❌ 15 pts to go |
| P01_GOLD | 625 | 90.7% | 90.7% | +0.0 | 100% | 🟡 9 pts to go |
| P02 | 463 | 96.3% | 96.3% | +0.8 | 100% | 🟡 4 pts to go |
| P03 | 260 | 88.5% | 88.5% | -0.9 | 100% | ❌ 12 pts to go |
| P04 | 3558 | 72.3% | 72.3% | +0.9 | 100% | ❌ 28 pts to go |
| P05 | 419 | 90.2% | 90.2% | +0.9 | 100% | 🟡 10 pts to go |
| P06M | 19102 | 99.5% | 99.5% | +0.3 | n/a | no target |
| P06T | 43728 | 57.5% | 57.5% | -1.8 | n/a | no target |
| P06 | 254 | 81.9% | 81.9% | +3.1 | 95% | ❌ 13 pts to go |
| P07 | 666 | 82.1% | 82.1% | +0.9 | 95% | ❌ 13 pts to go |
| P08 | 21518 | 81.7% | 81.7% | +3.4 | 95% | ❌ 13 pts to go |
| P09 | 278 | 96.0% | 96.0% | -0.1 | 100% | 🟡 4 pts to go |
| P10 | 2146 | 54.3% | 54.4% | -0.1 | 95% | ❌ 41 pts to go |
| P11 | 1633 | 59.6% | 59.6% | +10.2 | 80% | ❌ 20 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 164561 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 59.7% | 59.7% | -26.3 | n/a | no target |
| P01T | 198 | 69.2% | 69.2% | +1.0 | n/a | no target |
| P01_GOLD | 625 | 73.1% | 73.1% | +0.1 | 90% | ❌ 17 pts to go |
| P02 | 463 | 78.4% | 78.4% | +0.5 | 95% | ❌ 17 pts to go |
| P03 | 260 | 73.8% | 73.8% | -1.1 | 95% | ❌ 21 pts to go |
| P04 | 3558 | 68.9% | 68.9% | +0.0 | 95% | ❌ 26 pts to go |
| P05 | 419 | 72.1% | 72.1% | -1.4 | 90% | ❌ 18 pts to go |
| P06M | 19102 | 70.8% | 70.8% | -16.1 | n/a | no target |
| P06T | 43728 | 50.8% | 50.8% | -6.4 | n/a | no target |
| P06 | 254 | 70.5% | 70.5% | +2.0 | 95% | ❌ 24 pts to go |
| P07 | 666 | 66.2% | 66.2% | +1.4 | 90% | ❌ 24 pts to go |
| P08 | 21518 | 68.5% | 68.5% | +0.7 | 95% | ❌ 26 pts to go |
| P09 | 278 | 86.0% | 86.0% | -1.0 | 100% | ❌ 14 pts to go |
| P10 | 2146 | 53.4% | 53.4% | -1.9 | 95% | ❌ 42 pts to go |
| P11 | 1633 | 28.4% | 28.4% | -0.5 | 75% | ❌ 47 pts to go |
| P12 | 16 | 87.5% | 87.5% | -5.8 | n/a | no target |
| P13 | 164561 | 52.1% | 52.1% | -18.7 | 95% | ❌ 43 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 65.8% | 65.8% | -21.8 | n/a | no target |
| P01T | 198 | 83.8% | 83.8% | +0.5 | 95% | ❌ 11 pts to go |
| P01_GOLD | 625 | 84.8% | 84.8% | +0.0 | 90% | 🟡 5 pts to go |
| P02 | 463 | 90.5% | 90.5% | -0.1 | 95% | 🟡 4 pts to go |
| P03 | 260 | 83.1% | 83.1% | -2.5 | 95% | ❌ 12 pts to go |
| P04 | 3558 | 90.8% | 90.8% | +1.6 | 90% | ✅ met |
| P05 | 419 | 91.9% | 91.9% | -1.2 | 95% | 🟡 3 pts to go |
| P06M | 19102 | 75.6% | 75.6% | -17.6 | n/a | no target |
| P06T | 43728 | 69.4% | 69.4% | -5.5 | n/a | no target |
| P06 | 254 | 92.5% | 92.5% | +0.2 | 100% | 🟡 8 pts to go |
| P07 | 666 | 92.8% | 92.8% | +0.6 | 100% | 🟡 7 pts to go |
| P08 | 21518 | 94.0% | 94.0% | +1.7 | 100% | 🟡 6 pts to go |
| P09 | 278 | 73.4% | 73.4% | +0.4 | n/a | no target |
| P10 | 2146 | 93.0% | 93.0% | +1.7 | 100% | 🟡 7 pts to go |
| P11 | 1633 | 45.4% | 45.4% | +3.5 | 80% | ❌ 35 pts to go |
| P12 | 16 | 93.8% | 93.8% | -6.2 | n/a | no target |
| P13 | 164561 | 63.9% | 63.9% | -19.8 | 95% | ❌ 31 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 2.6% | 2.6% | -0.5 | n/a | no target |
| P01T | 198 | 8.6% | 8.6% | -0.8 | n/a | no target |
| P01_GOLD | 625 | 13.9% | 13.9% | -0.3 | 25% | ❌ 11 pts to go |
| P02 | 463 | 25.1% | 25.1% | -0.2 | 40% | ❌ 15 pts to go |
| P03 | 260 | 8.8% | 8.8% | -0.3 | 20% | ❌ 11 pts to go |
| P04 | 3558 | 3.7% | 3.7% | +0.2 | 20% | ❌ 16 pts to go |
| P05 | 419 | 3.3% | 3.3% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 19102 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 43728 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 254 | 5.5% | 5.5% | +0.4 | n/a | no target |
| P07 | 666 | 8.4% | 8.4% | -0.1 | n/a | no target |
| P08 | 21518 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P09 | 278 | 8.3% | 8.3% | +0.5 | n/a | no target |
| P10 | 2146 | 0.8% | 0.8% | +0.0 | n/a | no target |
| P11 | 1633 | 0.8% | 0.8% | -0.2 | n/a | no target |
| P12 | 16 | 6.2% | 6.2% | -0.5 | n/a | no target |
| P13 | 164561 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 14.3% | 14.3% | -4.3 | n/a | no target |
| P01T | 198 | 20.7% | 20.7% | -1.7 | 70% | ❌ 49 pts to go |
| P01_GOLD | 625 | 43.5% | 43.5% | +0.0 | 80% | ❌ 36 pts to go |
| P02 | 463 | 57.5% | 57.5% | +0.2 | 90% | ❌ 32 pts to go |
| P03 | 260 | 19.2% | 19.2% | +0.6 | 60% | ❌ 41 pts to go |
| P04 | 3558 | 21.3% | 21.3% | -0.3 | 85% | ❌ 64 pts to go |
| P05 | 419 | 11.7% | 11.7% | +0.1 | 50% | ❌ 38 pts to go |
| P06M | 19102 | 0.7% | 0.7% | +0.1 | n/a | no target |
| P06T | 43728 | 0.6% | 0.6% | -0.1 | n/a | no target |
| P06 | 254 | 15.7% | 15.7% | +0.3 | n/a | no target |
| P07 | 666 | 9.9% | 9.9% | -0.6 | n/a | no target |
| P08 | 21518 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P09 | 278 | 74.8% | 74.8% | -3.1 | 95% | ❌ 20 pts to go |
| P10 | 2146 | 1.6% | 1.6% | -0.1 | n/a | no target |
| P11 | 1633 | 14.2% | 14.2% | -2.5 | n/a | no target |
| P12 | 16 | 31.2% | 31.2% | +4.5 | n/a | no target |
| P13 | 164561 | 0.3% | 0.3% | -0.2 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 5.1% | 5.1% | -1.1 | n/a | no target |
| P01T | 198 | 9.6% | 9.6% | -0.8 | n/a | no target |
| P01_GOLD | 625 | 34.7% | 34.7% | +0.7 | 70% | ❌ 35 pts to go |
| P02 | 463 | 39.3% | 39.3% | +0.2 | 75% | ❌ 36 pts to go |
| P03 | 260 | 19.6% | 19.6% | +1.0 | 55% | ❌ 35 pts to go |
| P04 | 3558 | 21.3% | 21.3% | -0.3 | 75% | ❌ 54 pts to go |
| P05 | 419 | 10.7% | 10.7% | +0.0 | 50% | ❌ 39 pts to go |
| P06M | 19102 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06T | 43728 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 254 | 6.3% | 6.3% | +0.4 | n/a | no target |
| P07 | 666 | 5.0% | 5.0% | -0.2 | n/a | no target |
| P08 | 21518 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 278 | 71.6% | 71.6% | -3.6 | 95% | ❌ 23 pts to go |
| P10 | 2146 | 0.8% | 0.8% | -0.1 | n/a | no target |
| P11 | 1633 | 13.8% | 13.8% | -2.6 | n/a | no target |
| P12 | 16 | 18.8% | 18.8% | -1.2 | n/a | no target |
| P13 | 164561 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 9.2% | 9.2% | +1.4 | n/a | no target |
| P01T | 198 | 8.6% | 8.6% | +0.3 | n/a | no target |
| P01_GOLD | 625 | 58.2% | 58.4% | +0.2 | 80% | ❌ 22 pts to go |
| P02 | 463 | 45.6% | 45.8% | -0.1 | 75% | ❌ 29 pts to go |
| P03 | 260 | 36.9% | 36.9% | -0.4 | 70% | ❌ 33 pts to go |
| P04 | 3558 | 21.2% | 21.7% | +0.1 | 70% | ❌ 49 pts to go |
| P05 | 419 | 14.6% | 14.6% | +0.4 | 50% | ❌ 35 pts to go |
| P06M | 19102 | 0.4% | 0.4% | +0.1 | n/a | no target |
| P06T | 43728 | 0.2% | 0.3% | -0.1 | n/a | no target |
| P06 | 254 | 15.4% | 15.4% | -1.1 | n/a | no target |
| P07 | 666 | 2.0% | 2.0% | +0.0 | n/a | no target |
| P08 | 21518 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P09 | 278 | 48.9% | 48.9% | +2.3 | 80% | ❌ 31 pts to go |
| P10 | 2146 | 1.1% | 1.2% | -0.1 | n/a | no target |
| P11 | 1633 | 5.4% | 5.4% | -1.4 | n/a | no target |
| P12 | 16 | 37.5% | 37.5% | -2.5 | n/a | no target |
| P13 | 164561 | 0.1% | 0.1% | -0.1 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 18.9% | 18.9% | +0.3 | n/a | no target |
| P01T | 198 | 21.2% | 21.2% | -0.2 | 60% | ❌ 39 pts to go |
| P01_GOLD | 625 | 62.9% | 62.9% | -0.5 | 70% | 🟡 7 pts to go |
| P02 | 463 | 39.1% | 39.1% | -0.6 | 50% | ❌ 11 pts to go |
| P03 | 260 | 47.7% | 47.7% | -0.6 | 55% | 🟡 7 pts to go |
| P04 | 3558 | 12.6% | 12.6% | +0.4 | 40% | ❌ 27 pts to go |
| P05 | 419 | 16.7% | 16.7% | -0.4 | 40% | ❌ 23 pts to go |
| P06M | 19102 | 3.4% | 3.4% | +1.2 | n/a | no target |
| P06T | 43728 | 1.7% | 1.7% | +0.0 | n/a | no target |
| P06 | 254 | 20.9% | 20.9% | -1.1 | n/a | no target |
| P07 | 666 | 6.2% | 6.2% | -0.4 | n/a | no target |
| P08 | 21518 | 2.9% | 2.9% | +0.0 | n/a | no target |
| P09 | 278 | 5.8% | 5.8% | -0.1 | n/a | no target |
| P10 | 2146 | 5.1% | 5.1% | +0.5 | n/a | no target |
| P11 | 1633 | 4.3% | 4.3% | -0.9 | n/a | no target |
| P12 | 16 | 6.2% | 6.2% | -0.5 | n/a | no target |
| P13 | 164561 | 0.7% | 0.7% | -0.3 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 26.5% | 26.5% | +4.8 | n/a | no target |
| P01T | 198 | 29.8% | 29.8% | +1.2 | 65% | ❌ 35 pts to go |
| P01_GOLD | 625 | 68.6% | 68.6% | -0.4 | 70% | 🟡 1 pts to go |
| P02 | 463 | 23.8% | 23.8% | -0.4 | 50% | ❌ 26 pts to go |
| P03 | 260 | 50.8% | 50.8% | -1.7 | 60% | 🟡 9 pts to go |
| P04 | 3558 | 5.6% | 5.6% | +0.2 | 40% | ❌ 34 pts to go |
| P05 | 419 | 20.0% | 20.0% | +0.3 | 45% | ❌ 25 pts to go |
| P06M | 19102 | 2.0% | 2.0% | +0.6 | n/a | no target |
| P06T | 43728 | 0.8% | 0.8% | +0.1 | n/a | no target |
| P06 | 254 | 33.1% | 33.1% | -1.3 | n/a | no target |
| P07 | 666 | 6.6% | 6.6% | -0.3 | n/a | no target |
| P08 | 21518 | 1.3% | 1.3% | +0.0 | n/a | no target |
| P09 | 278 | 10.8% | 10.8% | +1.0 | n/a | no target |
| P10 | 2146 | 3.3% | 3.3% | +0.2 | n/a | no target |
| P11 | 1633 | 4.1% | 4.1% | -1.0 | n/a | no target |
| P12 | 16 | 6.2% | 6.2% | -0.5 | n/a | no target |
| P13 | 164561 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 14.8% | 14.8% | +2.4 | n/a | no target |
| P01T | 198 | 13.6% | 13.6% | +0.1 | n/a | no target |
| P01_GOLD | 625 | 49.9% | 49.9% | +0.1 | 50% | 🟡 0 pts to go |
| P02 | 463 | 38.2% | 38.2% | +0.9 | n/a | no target |
| P03 | 260 | 51.2% | 51.2% | -0.9 | 60% | 🟡 9 pts to go |
| P04 | 3558 | 12.7% | 12.7% | +0.8 | n/a | no target |
| P05 | 419 | 15.3% | 15.3% | +0.1 | n/a | no target |
| P06M | 19102 | 0.8% | 0.8% | +0.3 | n/a | no target |
| P06T | 43728 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 254 | 24.0% | 24.0% | -1.6 | n/a | no target |
| P07 | 666 | 7.8% | 7.8% | -0.5 | n/a | no target |
| P08 | 21518 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P09 | 278 | 20.9% | 20.9% | +3.3 | n/a | no target |
| P10 | 2146 | 2.5% | 2.5% | +0.1 | n/a | no target |
| P11 | 1633 | 3.2% | 3.2% | -1.5 | n/a | no target |
| P12 | 16 | 25.0% | 25.0% | +11.7 | n/a | no target |
| P13 | 164561 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 10.7% | 10.7% | -0.9 | 15% | 🟡 4 pts to go |
| P01T | 198 | 12.6% | 12.6% | +0.1 | 15% | 🟡 2 pts to go |
| P01_GOLD | 625 | 35.0% | 35.0% | -0.3 | 40% | 🟡 5 pts to go |
| P02 | 463 | 12.1% | 12.3% | -0.8 | 25% | ❌ 13 pts to go |
| P03 | 260 | 16.2% | 16.2% | -1.3 | 25% | 🟡 9 pts to go |
| P04 | 3558 | 2.8% | 2.8% | +0.1 | 15% | ❌ 12 pts to go |
| P05 | 419 | 6.7% | 6.7% | +0.1 | 15% | 🟡 8 pts to go |
| P06M | 19102 | 0.8% | 0.8% | -0.1 | 15% | ❌ 14 pts to go |
| P06T | 43728 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |
| P06 | 254 | 11.0% | 11.0% | +0.4 | 15% | 🟡 4 pts to go |
| P07 | 666 | 4.1% | 4.1% | -0.2 | 15% | ❌ 11 pts to go |
| P08 | 21518 | 0.6% | 0.6% | +0.0 | 15% | ❌ 14 pts to go |
| P09 | 278 | 1.1% | 1.1% | +0.1 | 15% | ❌ 14 pts to go |
| P10 | 2146 | 1.3% | 1.3% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 1633 | 1.3% | 1.3% | -0.2 | 15% | ❌ 14 pts to go |
| P12 | 16 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 164561 | 0.5% | 0.5% | -0.2 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 7.1% | 7.1% | +1.7 | 15% | 🟡 8 pts to go |
| P01T | 198 | 12.6% | 12.6% | +1.1 | 25% | ❌ 12 pts to go |
| P01_GOLD | 625 | 29.0% | 29.0% | -0.2 | 25% | ✅ met |
| P02 | 463 | 25.5% | 25.5% | +0.2 | 15% | ✅ met |
| P03 | 260 | 22.7% | 22.7% | +0.6 | 15% | ✅ met |
| P04 | 3558 | 4.0% | 4.0% | +0.0 | 15% | ❌ 11 pts to go |
| P05 | 419 | 11.5% | 11.5% | +0.4 | 15% | 🟡 4 pts to go |
| P06M | 19102 | 0.7% | 0.7% | +0.2 | 15% | ❌ 14 pts to go |
| P06T | 43728 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 254 | 9.1% | 9.1% | +0.7 | 15% | 🟡 6 pts to go |
| P07 | 666 | 2.6% | 2.6% | -0.3 | 15% | ❌ 12 pts to go |
| P08 | 21518 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |
| P09 | 278 | 1.4% | 1.4% | +0.4 | 15% | ❌ 14 pts to go |
| P10 | 2146 | 1.6% | 1.6% | +0.0 | 15% | ❌ 13 pts to go |
| P11 | 1633 | 2.0% | 2.0% | -0.7 | 15% | ❌ 13 pts to go |
| P12 | 16 | 18.8% | 18.8% | -1.2 | 15% | ✅ met |
| P13 | 164561 | 0.1% | 0.1% | -0.1 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 2.0% | 2.0% | -0.3 | 20% | ❌ 18 pts to go |
| P01T | 198 | 3.5% | 3.5% | -0.7 | 20% | ❌ 16 pts to go |
| P01_GOLD | 625 | 4.3% | 4.3% | -0.2 | 20% | ❌ 16 pts to go |
| P02 | 463 | 1.5% | 1.5% | +0.0 | 20% | ❌ 18 pts to go |
| P03 | 260 | 1.9% | 1.9% | +0.4 | 20% | ❌ 18 pts to go |
| P04 | 3558 | 0.7% | 0.7% | +0.1 | 20% | ❌ 19 pts to go |
| P05 | 419 | 1.0% | 1.0% | -0.2 | 20% | ❌ 19 pts to go |
| P06M | 19102 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 43728 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 254 | 1.6% | 1.6% | +0.1 | 20% | ❌ 18 pts to go |
| P07 | 666 | 0.5% | 0.5% | +0.1 | 20% | ❌ 20 pts to go |
| P08 | 21518 | 0.1% | 0.1% | +0.1 | 20% | ❌ 20 pts to go |
| P09 | 278 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2146 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 1633 | 0.1% | 0.1% | -0.2 | 20% | ❌ 20 pts to go |
| P12 | 16 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 164561 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 2.0% | 2.0% | +0.4 | 15% | ❌ 13 pts to go |
| P01T | 198 | 3.5% | 3.5% | +0.4 | 15% | ❌ 12 pts to go |
| P01_GOLD | 625 | 10.6% | 10.6% | +0.2 | 15% | 🟡 4 pts to go |
| P02 | 463 | 11.2% | 11.2% | -0.8 | 15% | 🟡 4 pts to go |
| P03 | 260 | 21.2% | 21.2% | +1.0 | 15% | ✅ met |
| P04 | 3558 | 2.3% | 2.3% | +0.0 | 15% | ❌ 13 pts to go |
| P05 | 419 | 2.9% | 2.9% | +0.1 | 15% | ❌ 12 pts to go |
| P06M | 19102 | 0.5% | 0.5% | +0.2 | 15% | ❌ 14 pts to go |
| P06T | 43728 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 254 | 4.7% | 4.7% | -0.4 | 15% | ❌ 10 pts to go |
| P07 | 666 | 1.7% | 1.7% | +0.1 | 15% | ❌ 13 pts to go |
| P08 | 21518 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |
| P09 | 278 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2146 | 1.1% | 1.1% | +0.1 | 15% | ❌ 14 pts to go |
| P11 | 1633 | 0.9% | 0.9% | -0.3 | 15% | ❌ 14 pts to go |
| P12 | 16 | 6.2% | 6.2% | -0.5 | 15% | 🟡 9 pts to go |
| P13 | 164561 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 15.3% | 15.3% | +1.3 | 20% | 🟡 5 pts to go |
| P01T | 198 | 14.1% | 14.1% | +0.0 | 40% | ❌ 26 pts to go |
| P01_GOLD | 625 | 46.2% | 46.2% | +0.0 | 40% | ✅ met |
| P02 | 463 | 43.8% | 43.8% | +0.9 | 20% | ✅ met |
| P03 | 260 | 47.7% | 47.7% | -1.3 | 35% | ✅ met |
| P04 | 3558 | 14.8% | 14.8% | +0.6 | 20% | 🟡 5 pts to go |
| P05 | 419 | 15.8% | 15.8% | +0.4 | 20% | 🟡 4 pts to go |
| P06M | 19102 | 1.1% | 1.1% | +0.3 | 20% | ❌ 19 pts to go |
| P06T | 43728 | 0.6% | 0.6% | -0.1 | 20% | ❌ 19 pts to go |
| P06 | 254 | 24.4% | 24.4% | -0.9 | 20% | ✅ met |
| P07 | 666 | 8.3% | 8.3% | -0.3 | 20% | ❌ 12 pts to go |
| P08 | 21518 | 1.0% | 1.0% | +0.0 | 20% | ❌ 19 pts to go |
| P09 | 278 | 20.9% | 20.9% | +2.7 | 20% | ✅ met |
| P10 | 2146 | 3.8% | 3.8% | +0.1 | 20% | ❌ 16 pts to go |
| P11 | 1633 | 3.6% | 3.6% | -1.2 | 20% | ❌ 16 pts to go |
| P12 | 16 | 18.8% | 18.8% | +12.1 | 20% | 🟡 1 pts to go |
| P13 | 164561 | 0.4% | 0.4% | -0.1 | 20% | ❌ 20 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 22.4% | 22.4% | -10.9 | n/a | no target |
| P01T | 198 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 72.3% | 72.3% | +2.8 | 95% | ❌ 23 pts to go |
| P02 | 463 | 65.7% | 65.7% | +2.8 | 95% | ❌ 29 pts to go |
| P03 | 260 | 57.7% | 57.7% | +4.5 | 90% | ❌ 32 pts to go |
| P04 | 3558 | 26.1% | 26.1% | +1.3 | 85% | ❌ 59 pts to go |
| P05 | 419 | 38.7% | 38.7% | +1.0 | 75% | ❌ 36 pts to go |
| P06M | 19102 | 30.3% | 30.3% | -5.8 | n/a | no target |
| P06T | 43728 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 254 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 666 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21518 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 278 | 89.9% | 89.9% | +1.6 | 100% | ❌ 10 pts to go |
| P10 | 2146 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1633 | 4.7% | 4.7% | -1.3 | 60% | ❌ 55 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 164561 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 22.4% | 22.4% | -10.9 | n/a | no target |
| P01T | 198 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 74.1% | 74.1% | +1.3 | 100% | ❌ 26 pts to go |
| P02 | 463 | 67.8% | 67.8% | +1.5 | 100% | ❌ 32 pts to go |
| P03 | 260 | 60.0% | 60.0% | +1.1 | n/a | no target |
| P04 | 3558 | 26.5% | 26.5% | +1.0 | 95% | ❌ 68 pts to go |
| P05 | 419 | 34.1% | 34.1% | +0.7 | 80% | ❌ 46 pts to go |
| P06M | 19102 | 30.3% | 30.3% | -5.8 | n/a | no target |
| P06T | 43728 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 254 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 666 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21518 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 278 | 92.1% | 92.1% | +0.6 | 100% | 🟡 8 pts to go |
| P10 | 2146 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1633 | 4.8% | 4.8% | -1.6 | n/a | no target |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 164561 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 84.7% | 84.7% | +4.9 | n/a | no target |
| P01T | 198 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 52.6% | 52.6% | +1.0 | 85% | ❌ 32 pts to go |
| P02 | 463 | 58.5% | 58.5% | +1.0 | 90% | ❌ 32 pts to go |
| P03 | 260 | 43.8% | 43.8% | +1.2 | 85% | ❌ 41 pts to go |
| P04 | 3558 | 28.4% | 28.4% | +0.5 | 90% | ❌ 62 pts to go |
| P05 | 419 | 32.9% | 32.9% | +0.2 | 75% | ❌ 42 pts to go |
| P06M | 19102 | 86.2% | 86.2% | -0.9 | n/a | no target |
| P06T | 43728 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 254 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 666 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21518 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 278 | 82.4% | 82.4% | -1.0 | 95% | ❌ 13 pts to go |
| P10 | 2146 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1633 | 4.1% | 4.1% | -1.3 | n/a | no target |
| P12 | 16 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 164561 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 83.7% | 83.7% | +5.4 | n/a | no target |
| P01T | 198 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 52.5% | 52.5% | +0.7 | 85% | ❌ 32 pts to go |
| P02 | 463 | 53.1% | 53.1% | +0.5 | 90% | ❌ 37 pts to go |
| P03 | 260 | 43.5% | 43.5% | -0.2 | 85% | ❌ 42 pts to go |
| P04 | 3558 | 24.3% | 24.3% | +0.5 | 90% | ❌ 66 pts to go |
| P05 | 419 | 43.0% | 43.0% | -0.4 | 75% | ❌ 32 pts to go |
| P06M | 19102 | 77.9% | 77.9% | +0.1 | n/a | no target |
| P06T | 43728 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 254 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 666 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21518 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 278 | 0.4% | 0.4% | +0.1 | 95% | ❌ 95 pts to go |
| P10 | 2146 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1633 | 3.2% | 3.2% | -1.3 | n/a | no target |
| P12 | 16 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 164561 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 93.9% | 93.9% | +4.0 | n/a | no target |
| P01T | 198 | 95.5% | 95.5% | +1.2 | n/a | no target |
| P01_GOLD | 625 | 85.6% | 85.6% | +0.3 | 100% | ❌ 14 pts to go |
| P02 | 463 | 77.3% | 77.3% | +0.9 | 100% | ❌ 23 pts to go |
| P03 | 260 | 91.9% | 91.9% | +0.6 | n/a | no target |
| P04 | 3558 | 50.3% | 50.3% | +1.5 | 95% | ❌ 45 pts to go |
| P05 | 419 | 77.1% | 77.1% | -0.4 | 95% | ❌ 18 pts to go |
| P06M | 19102 | 99.2% | 99.2% | +0.3 | n/a | no target |
| P06T | 43728 | 92.6% | 92.6% | +2.0 | n/a | no target |
| P06 | 254 | 22.4% | 22.4% | -0.7 | n/a | no target |
| P07 | 666 | 12.9% | 12.9% | -0.9 | n/a | no target |
| P08 | 21518 | 6.5% | 6.5% | -0.6 | n/a | no target |
| P09 | 278 | 98.2% | 98.2% | -0.5 | 100% | 🟡 2 pts to go |
| P10 | 2146 | 70.5% | 70.5% | -0.5 | n/a | no target |
| P11 | 1633 | 71.7% | 71.7% | +3.6 | n/a | no target |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 164561 | 99.6% | 99.6% | -0.1 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 93.9% | 93.9% | +4.0 | n/a | no target |
| P01T | 198 | 95.5% | 95.5% | +1.2 | n/a | no target |
| P01_GOLD | 625 | 88.8% | 88.8% | +0.3 | 100% | ❌ 11 pts to go |
| P02 | 463 | 78.4% | 78.6% | +0.9 | 100% | ❌ 22 pts to go |
| P03 | 260 | 92.7% | 92.7% | +0.7 | n/a | no target |
| P04 | 3558 | 53.6% | 53.6% | +1.7 | 95% | ❌ 41 pts to go |
| P05 | 419 | 89.3% | 89.3% | -0.3 | 70% | ✅ met |
| P06M | 19102 | 99.2% | 99.2% | +0.3 | n/a | no target |
| P06T | 43728 | 92.6% | 92.6% | +2.0 | n/a | no target |
| P06 | 254 | 22.4% | 22.4% | -0.7 | n/a | no target |
| P07 | 666 | 12.9% | 12.9% | -0.9 | n/a | no target |
| P08 | 21518 | 6.5% | 6.5% | -0.6 | n/a | no target |
| P09 | 278 | 98.2% | 98.2% | -0.5 | 100% | 🟡 2 pts to go |
| P10 | 2146 | 70.5% | 70.5% | -0.5 | n/a | no target |
| P11 | 1633 | 71.8% | 71.8% | +3.6 | n/a | no target |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 164561 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 198 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 16.6% | 16.6% | -0.2 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 367 rows, 28.3% filled |
| P02 | 463 | 10.8% | 10.8% | -0.4 | n/a | no target · rows from a source that publishes bids: 294 rows, 17.0% filled |
| P03 | 260 | 13.5% | 13.5% | +0.6 | n/a | no target · rows from a source that publishes bids: 137 rows, 25.5% filled |
| P04 | 3558 | 1.7% | 1.7% | +0.2 | n/a | no target · rows from a source that publishes bids: 861 rows, 7.0% filled |
| P05 | 419 | 2.4% | 2.4% | -0.2 | n/a | no target · rows from a source that publishes bids: 51 rows, 19.6% filled |
| P06M | 19102 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 43728 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 254 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 666 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21518 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 278 | 4.0% | 4.0% | -0.2 | n/a | no target · rows from a source that publishes bids: 265 rows, 4.2% filled |
| P10 | 2146 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1633 | 0.6% | 0.6% | -0.3 | n/a | no target · rows from a source that publishes bids: 75 rows, 13.3% filled |
| P12 | 16 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 16 rows, 0.0% filled |
| P13 | 164561 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 198 | 0.0% | 98.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 53.8% | 82.6% | +0.6 | 90% | ❌ 36 pts to go |
| P02 | 463 | 53.1% | 87.0% | +0.7 | 90% | ❌ 37 pts to go |
| P03 | 260 | 45.4% | 80.0% | +0.9 | 90% | ❌ 45 pts to go |
| P04 | 3558 | 19.3% | 93.0% | +0.2 | 90% | ❌ 71 pts to go |
| P05 | 419 | 0.0% | 83.3% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 19102 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 43728 | 0.0% | 99.8% | +0.0 | n/a | no target |
| P06 | 254 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 666 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 21518 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 278 | 2.9% | 4.7% | +0.6 | 90% | ❌ 87 pts to go |
| P10 | 2146 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1633 | 2.8% | 97.3% | -1.3 | n/a | no target |
| P12 | 16 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 164561 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 198 | 0.5% | 98.5% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 26.6% | 55.4% | +0.7 | 90% | ❌ 63 pts to go |
| P02 | 463 | 51.8% | 85.7% | +0.3 | n/a | no target |
| P03 | 260 | 25.4% | 60.0% | +1.1 | n/a | no target |
| P04 | 3558 | 21.0% | 94.8% | +0.0 | n/a | no target |
| P05 | 419 | 0.5% | 83.8% | +0.0 | n/a | no target |
| P06M | 19102 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 43728 | 0.1% | 99.9% | +0.0 | n/a | no target |
| P06 | 254 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 666 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 21518 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 278 | 40.6% | 42.4% | -0.4 | n/a | no target |
| P10 | 2146 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1633 | 2.8% | 97.3% | -0.9 | n/a | no target |
| P12 | 16 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 164561 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 198 | 2.0% | 100.0% | -0.1 | n/a | no target |
| P01_GOLD | 625 | 52.6% | 81.4% | +0.8 | 95% | ❌ 42 pts to go |
| P02 | 463 | 57.5% | 91.4% | +1.1 | n/a | no target |
| P03 | 260 | 49.2% | 83.8% | +2.4 | n/a | no target |
| P04 | 3558 | 21.8% | 95.6% | +0.6 | n/a | no target |
| P05 | 419 | 4.8% | 88.1% | +0.3 | n/a | no target |
| P06M | 19102 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 43728 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 254 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 666 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 21518 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 278 | 61.2% | 62.9% | -1.3 | n/a | no target |
| P10 | 2146 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1633 | 2.9% | 97.4% | -1.2 | n/a | no target |
| P12 | 16 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 164561 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 95.9% | 95.9% | -4.1 | 100% | 🟡 4 pts to go |
| P01T | 198 | 96.5% | 96.5% | -3.5 | 100% | 🟡 4 pts to go |
| P01_GOLD | 625 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P02 | 463 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P03 | 260 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3558 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P05 | 419 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P06M | 19102 | 96.3% | 96.3% | -3.7 | 100% | 🟡 4 pts to go |
| P06T | 43728 | 94.3% | 94.3% | -5.7 | 100% | 🟡 6 pts to go |
| P06 | 254 | 99.6% | 99.6% | -0.4 | 100% | 🟡 0 pts to go |
| P07 | 666 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P08 | 21518 | 99.6% | 99.6% | -0.4 | 100% | 🟡 0 pts to go |
| P09 | 278 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2146 | 99.5% | 99.5% | -0.5 | 100% | 🟡 0 pts to go |
| P11 | 1633 | 97.3% | 97.3% | -2.7 | 100% | 🟡 3 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 164561 | 94.6% | 94.6% | -5.4 | 100% | 🟡 5 pts to go |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 95.9% | 95.9% | -4.1 | 100% | 🟡 4 pts to go |
| P01T | 198 | 96.5% | 96.5% | -3.5 | 100% | 🟡 4 pts to go |
| P01_GOLD | 625 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P02 | 463 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P03 | 260 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3558 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P05 | 419 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P06M | 19102 | 96.3% | 96.3% | -3.7 | 100% | 🟡 4 pts to go |
| P06T | 43728 | 94.3% | 94.3% | -5.7 | 100% | 🟡 6 pts to go |
| P06 | 254 | 99.6% | 99.6% | -0.4 | 100% | 🟡 0 pts to go |
| P07 | 666 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P08 | 21518 | 99.6% | 99.6% | -0.4 | 100% | 🟡 0 pts to go |
| P09 | 278 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2146 | 99.5% | 99.5% | -0.5 | 100% | 🟡 0 pts to go |
| P11 | 1633 | 97.3% | 97.3% | -2.7 | 100% | 🟡 3 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 164561 | 94.6% | 94.6% | -5.4 | 100% | 🟡 5 pts to go |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 196 | 95.9% | 95.9% | -4.1 | 100% | 🟡 4 pts to go |
| P01T | 198 | 96.5% | 96.5% | -3.5 | 100% | 🟡 4 pts to go |
| P01_GOLD | 625 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P02 | 463 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P03 | 260 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3558 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P05 | 419 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P06M | 19102 | 96.3% | 96.3% | -3.7 | 100% | 🟡 4 pts to go |
| P06T | 43728 | 94.3% | 94.3% | -5.7 | 100% | 🟡 6 pts to go |
| P06 | 254 | 99.6% | 99.6% | -0.4 | 100% | 🟡 0 pts to go |
| P07 | 666 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P08 | 21518 | 99.6% | 99.6% | -0.4 | 100% | 🟡 0 pts to go |
| P09 | 278 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2146 | 99.5% | 99.5% | -0.5 | 100% | 🟡 0 pts to go |
| P11 | 1633 | 97.3% | 97.3% | -2.7 | 100% | 🟡 3 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 164561 | 94.6% | 94.6% | -5.4 | 100% | 🟡 5 pts to go |

