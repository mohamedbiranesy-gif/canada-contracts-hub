# Coverage vs the downstream team's targets — 2026-11-11

Benchmarks (field × package with a numeric target): **91 of 438 met** (20.8%); 64 within 10 points; 283 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 129, P01T 192, P01_GOLD 626, P02 466, P03 263, P04 3723, P05 422, P06M 14643, P06T 36661, P06 273, P07 696, P08 22009, P09 307, P10R 0, P10 2390, P11 1455, P12 15, P13 93957

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 129 | 0.0% | 20.2% | 8 | vendor GST/HST number (114 rows) |
| P01T | 192 | 1.0% | 31.2% | 8 | payment terms (150 rows) |
| P01_GOLD | 626 | 25.1% | 71.7% | 10 | payment terms (215 rows) |
| P02 | 466 | 7.5% | 54.9% | 9 | PO rule (353 rows) |
| P03 | 263 | 14.8% | 57.4% | 9 | payment terms (130 rows) |
| P04 | 3723 | 1.3% | 16.7% | 6 | PO rule (3522 rows) |
| P05 | 422 | 1.2% | 17.8% | 7 | payment terms (348 rows) |
| P06M | 14643 | 0.0% | 3.2% | 8 | PO rule (14437 rows) |
| P06T | 36661 | 0.0% | 10.2% | 6 | PO rule (36417 rows) |
| P06 | 273 | 0.0% | 11.4% | 6 | reference to quote (PO / contract / vendor id) (273 rows) |
| P07 | 696 | 0.0% | 2.7% | 6 | reference to quote (PO / contract / vendor id) (696 rows) |
| P08 | 22009 | 0.0% | 0.6% | 6 | reference to quote (PO / contract / vendor id) (22009 rows) |
| P09 | 307 | 1.3% | 45.3% | 8 | payment terms (286 rows) |
| P10 | 2390 | 0.0% | 1.1% | 5 | reference to quote (PO / contract / vendor id) (2390 rows) |
| P11 | 1455 | 0.4% | 7.5% | 5 | PO rule (1381 rows) |
| P12 | 15 | 0.0% | 53.3% | 9 | PO rule (14 rows) |
| P13 | 93957 | 0.0% | 0.3% | 6 | reference to quote (PO / contract / vendor id) (93957 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 129 | 8 | 26 | 95 | 0 | 0 | 71 |
| P01T | 192 | 24 | 33 | 135 | 0 | 0 | 71 |
| P01_GOLD | 626 | 226 | 202 | 198 | 0 | 0 | 82 |
| P02 | 466 | 0 | 196 | 270 | 0 | 0 | 66 |
| P03 | 263 | 0 | 0 | 251 | 12 | 0 | 57 |
| P04 | 3723 | 0 | 0 | 3029 | 694 | 0 | 46 |
| P05 | 422 | 15 | 30 | 365 | 12 | 0 | 51 |
| P06M | 14643 | 0 | 10 | 14563 | 70 | 0 | 46 |
| P06T | 36661 | 0 | 24 | 24847 | 11790 | 0 | 38 |
| P06 | 273 | 17 | 51 | 205 | 0 | 0 | 70 |
| P07 | 696 | 0 | 23 | 650 | 23 | 0 | 54 |
| P08 | 22009 | 0 | 0 | 18730 | 3279 | 0 | 43 |
| P09 | 307 | 4 | 12 | 290 | 1 | 0 | 53 |
| P10 | 2390 | 3 | 15 | 1621 | 751 | 0 | 42 |
| P11 | 1455 | 7 | 16 | 41 | 0 | 1391 | 23 |
| P12 | 15 | 0 | 0 | 15 | 0 | 0 | 54 |
| P13 | 93957 | 8 | 56 | 93876 | 17 | 0 | 43 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 129 | 106 | 82.2% | the buyer's PO / reference rule (12) |
| P01T | 192 | 116 | 60.4% | bill-to legal name and address (62) |
| P01_GOLD | 626 | 474 | 75.7% | bill-to legal name and address (96) |
| P02 | 466 | 314 | 67.4% | the buyer's PO / reference rule (83) |
| P03 | 263 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (263) |
| P04 | 3723 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (3723) |
| P05 | 422 | 47 | 11.1% | a confirmed invoicing / AP or finance channel (336) |
| P06M | 14643 | 152 | 1.0% | a confirmed invoicing / AP or finance channel (14447) |
| P06T | 36661 | 234 | 0.6% | a confirmed invoicing / AP or finance channel (36084) |
| P06 | 273 | 47 | 17.2% | the buyer's PO / reference rule (116) |
| P07 | 696 | 8 | 1.1% | bill-to legal name and address (269) |
| P08 | 22009 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (22009) |
| P09 | 307 | 42 | 13.7% | a confirmed invoicing / AP or finance channel (255) |
| P10 | 2390 | 8 | 0.3% | a confirmed invoicing / AP or finance channel (2292) |
| P11 | 1455 | 14 | 1.0% | a confirmed invoicing / AP or finance channel (1391) |
| P12 | 15 | 4 | 26.7% | a confirmed invoicing / AP or finance channel (10) |
| P13 | 93957 | 36 | 0.0% | a confirmed invoicing / AP or finance channel (92348) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 129 | 6 | 4.7% | 7 | 0 | the vendor's GST/HST number (BN9) (112) |
| P01T | 192 | 67 | 34.9% | 4 | 0 | the vendor's GST/HST number (BN9) (71) |
| P01_GOLD | 626 | 409 | 65.3% | 11 | 0 | the vendor's GST/HST number (BN9) (143) |
| P02 | 466 | 211 | 45.3% | 21 | 0 | the vendor's GST/HST number (BN9) (199) |
| P03 | 263 | 16 | 6.1% | 0 | 137 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (88) |
| P04 | 3723 | 43 | 1.2% | 7 | 872 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2743) |
| P05 | 422 | 20 | 4.7% | 8 | 123 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (205) |
| P06M | 14643 | 6 | 0.0% | 11 | 385 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (14016) |
| P06T | 36661 | 222 | 0.6% | 17 | 8805 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (27217) |
| P06 | 273 | 28 | 10.3% | 50 | 0 | the vendor's GST/HST number (BN9) (116) |
| P07 | 696 | 8 | 1.1% | 111 | 35 | the vendor's GST/HST number (BN9) (306) |
| P08 | 22009 | 3 | 0.0% | 14 | 4886 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (17060) |
| P09 | 307 | 40 | 13.0% | 1 | 125 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (121) |
| P10 | 2390 | 8 | 0.3% | 19 | 306 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (1960) |
| P11 | 1455 | 9 | 0.6% | 4 | 0 | a confirmed invoicing / AP or finance channel (1373) |
| P12 | 15 | 3 | 20.0% | 0 | 6 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (4) |
| P13 | 93957 | 11 | 0.0% | 549 | 26493 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (65696) |
| **all** | 178227 | 1110 | 0.6% | 834 | 42173 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 121 | 0 | 0 | 0 | 67 | 8 | 0 | 101 | 105 | 4 |
| P01T | 168 | 0 | 0 | 0 | 89 | 53 | 28 | 137 | 151 | 7 |
| P01_GOLD | 400 | 0 | 0 | 0 | 11 | 77 | 31 | 194 | 229 | 60 |
| P02 | 466 | 0 | 466 | 0 | 39 | 57 | 19 | 353 | 281 | 22 |
| P03 | 263 | 0 | 263 | 0 | 15 | 41 | 25 | 125 | 136 | 26 |
| P04 | 3723 | 0 | 3723 | 0 | 1602 | 1376 | 1047 | 3522 | 3269 | 169 |
| P05 | 407 | 0 | 356 | 0 | 76 | 88 | 42 | 339 | 350 | 53 |
| P06M | 14643 | 0 | 14643 | 0 | 9324 | 1233 | 122 | 14437 | 14314 | 216 |
| P06T | 36661 | 0 | 36661 | 0 | 31438 | 22995 | 14927 | 36417 | 36055 | 885 |
| P06 | 256 | 0 | 0 | 0 | 116 | 72 | 54 | 179 | 213 | 9 |
| P07 | 696 | 0 | 696 | 0 | 436 | 280 | 129 | 648 | 650 | 13 |
| P08 | 22009 | 0 | 22009 | 0 | 16568 | 10047 | 4772 | 21721 | 21363 | 444 |
| P09 | 303 | 0 | 282 | 0 | 9 | 71 | 2 | 277 | 289 | 46 |
| P10 | 2387 | 0 | 2348 | 0 | 1157 | 1274 | 1088 | 2317 | 2280 | 118 |
| P11 | 1448 | 1391 | 1345 | 0 | 583 | 999 | 584 | 1381 | 1380 | 59 |
| P12 | 15 | 0 | 13 | 0 | 1 | 3 | 0 | 14 | 14 | 1 |
| P13 | 93949 | 0 | 93625 | 0 | 67047 | 49364 | 24 | 93668 | 92975 | 170 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_phone | P13 | 70.8% | 95% | 22734 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 18765 |
| ap_system_hint | P13 | 0.5% | 20% | 18330 |
| buyer_bn_as_published | P13 | 12.3% | 30% | 16640 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 13986 |
| buyer_tax_exempt_status | P13 | 0.2% | 15% | 13948 |
| buyer_payment_method_preference | P13 | 0.7% | 15% | 13421 |
| buyer_legal_name_as_published | P13 | 47.5% | 60% | 11782 |
| buyer_logo_url | P13 | 83.7% | 95% | 10590 |
| vendor_registered_address | P08 | 30.3% | 70% | 8740 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 7323 |
| ap_system_hint | P06T | 0.7% | 20% | 7090 |
| buyer_phone | P08 | 67.8% | 95% | 5985 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 5427 |
| buyer_tax_exempt_status | P06T | 0.2% | 15% | 5415 |
| buyer_payment_method_preference | P06T | 0.5% | 15% | 5315 |
| invoice_reference_hint | P08 | 1.3% | 25% | 5215 |
| buyer_legal_name_as_published | P08 | 54.4% | 75% | 4545 |
| vendor_emails | P08 | 54.8% | 75% | 4440 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 4391 |
| vendor_phone | P08 | 65.3% | 85% | 4328 |
| buyer_bn_as_published | P08 | 15.4% | 35% | 4306 |
| vendor_bn9 | P08 | 30.5% | 50% | 4294 |
| ap_system_hint | P08 | 1.0% | 20% | 4174 |
| buyer_address | P08 | 78.3% | 95% | 3676 |
| buyer_esignature_preference | P08 | 0.5% | 15% | 3198 |
| buyer_tax_exempt_status | P08 | 0.5% | 15% | 3187 |
| buyer_payment_method_preference | P08 | 0.6% | 15% | 3164 |
| vendor_trading_name | P08 | 36.2% | 50% | 3038 |
| buyer_ap_cycle_published | P06M | 0.0% | 20% | 2923 |
| ap_system_hint | P06M | 0.8% | 20% | 2805 |
| average_contract_duration_days | P04 | 19.1% | 90% | 2640 |
| currency | P04 | 25.5% | 95% | 2588 |
| end_date | P04 | 23.8% | 90% | 2464 |
| commodity_codes | P04 | 21.6% | 85% | 2362 |
| ap_phone | P04 | 21.6% | 85% | 2360 |
| vendor_neq | P04 | 32.2% | 95% | 2338 |
| start_date | P04 | 27.9% | 90% | 2314 |
| award_or_notice_id | P04 | 23.6% | 85% | 2286 |
| contract_value | P04 | 24.8% | 85% | 2240 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 89.1% | 89.1% | +0.4 | 50% | ✅ met |
| P01T | 192 | 93.8% | 93.8% | +4.3 | 50% | ✅ met |
| P01_GOLD | 626 | 92.2% | 94.4% | +0.0 | 95% | 🟡 3 pts to go |
| P02 | 466 | 74.0% | 75.5% | +0.2 | 95% | ❌ 21 pts to go |
| P03 | 263 | 81.4% | 84.4% | -0.6 | 95% | ❌ 14 pts to go |
| P04 | 3723 | 30.2% | 31.7% | -2.6 | 90% | ❌ 60 pts to go |
| P05 | 422 | 38.6% | 41.5% | +0.0 | 70% | ❌ 31 pts to go |
| P06M | 14643 | 91.8% | 91.8% | -0.8 | n/a | no target |
| P06T | 36661 | 98.6% | 98.6% | +18.3 | n/a | no target |
| P06 | 273 | 34.4% | 34.4% | +2.7 | 30% | ✅ met |
| P07 | 696 | 6.9% | 6.9% | +0.0 | 30% | ❌ 23 pts to go |
| P08 | 22009 | 1.3% | 1.3% | +0.2 | 25% | ❌ 24 pts to go |
| P09 | 307 | 99.0% | 99.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10 | 2390 | 3.1% | 3.1% | +0.5 | 25% | ❌ 22 pts to go |
| P11 | 1455 | 46.9% | 47.8% | +33.3 | 60% | ❌ 13 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 93957 | 99.7% | 99.7% | +99.5 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 192 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 626 | 6.1% | 6.1% | +0.0 | 50% | ❌ 44 pts to go |
| P02 | 466 | 6.2% | 6.2% | +0.0 | 50% | ❌ 44 pts to go |
| P03 | 263 | 1.5% | 1.5% | -0.1 | 40% | ❌ 38 pts to go |
| P04 | 3723 | 0.5% | 0.5% | +0.0 | 30% | ❌ 30 pts to go |
| P05 | 422 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 14643 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 36661 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 273 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 696 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22009 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 0.7% | 0.7% | +0.0 | 50% | ❌ 49 pts to go |
| P10 | 2390 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1455 | 0.3% | 0.3% | +0.3 | n/a | no target |
| P12 | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 93957 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 82.2% | 82.2% | +0.8 | n/a | no target |
| P01T | 192 | 74.5% | 74.5% | +4.0 | 50% | ✅ met |
| P01_GOLD | 626 | 66.8% | 66.8% | -0.1 | 85% | ❌ 18 pts to go |
| P02 | 466 | 64.8% | 64.8% | -0.1 | 90% | ❌ 25 pts to go |
| P03 | 263 | 59.7% | 59.7% | -1.6 | 85% | ❌ 25 pts to go |
| P04 | 3723 | 27.6% | 27.6% | -2.5 | 85% | ❌ 57 pts to go |
| P05 | 422 | 28.9% | 28.9% | -0.1 | 60% | ❌ 31 pts to go |
| P06M | 14643 | 91.5% | 91.5% | -0.9 | n/a | no target |
| P06T | 36661 | 98.4% | 98.4% | +18.4 | n/a | no target |
| P06 | 273 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 696 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22009 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 96.1% | 96.1% | +0.1 | 100% | 🟡 4 pts to go |
| P10 | 2390 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1455 | 43.3% | 43.3% | +30.6 | 60% | ❌ 17 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 93957 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 192 | 0.0% | 0.0% | +0.0 | 30% | ❌ 30 pts to go |
| P01_GOLD | 626 | 50.8% | 50.8% | +0.2 | 80% | ❌ 29 pts to go |
| P02 | 466 | 56.9% | 56.9% | -0.1 | 60% | 🟡 3 pts to go |
| P03 | 263 | 50.2% | 50.2% | -1.4 | 80% | ❌ 30 pts to go |
| P04 | 3723 | 22.9% | 22.9% | -2.1 | 50% | ❌ 27 pts to go |
| P05 | 422 | 11.4% | 11.4% | -0.5 | 40% | ❌ 29 pts to go |
| P06M | 14643 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 36661 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 273 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 696 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22009 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 83.4% | 83.4% | -0.1 | 50% | ✅ met |
| P10 | 2390 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1455 | 5.6% | 5.6% | +4.8 | 40% | ❌ 34 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 93957 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 192 | 0.5% | 0.5% | +0.2 | n/a | no target |
| P01_GOLD | 626 | 60.4% | 60.4% | +0.0 | 85% | ❌ 25 pts to go |
| P02 | 466 | 56.2% | 56.2% | -0.1 | 90% | ❌ 34 pts to go |
| P03 | 263 | 58.6% | 58.6% | -1.6 | 85% | ❌ 26 pts to go |
| P04 | 3723 | 23.6% | 23.6% | -2.2 | 85% | ❌ 61 pts to go |
| P05 | 422 | 19.7% | 19.7% | -0.2 | 50% | ❌ 30 pts to go |
| P06M | 14643 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 36661 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 273 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 696 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22009 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 97.1% | 97.1% | +0.1 | 100% | 🟡 3 pts to go |
| P10 | 2390 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1455 | 6.0% | 6.0% | +5.1 | 60% | ❌ 54 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 93957 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 192 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 12.9% | 12.9% | +0.0 | 60% | ❌ 47 pts to go |
| P02 | 466 | 6.0% | 6.0% | +0.0 | 50% | ❌ 44 pts to go |
| P03 | 263 | 8.4% | 8.4% | -0.2 | 50% | ❌ 42 pts to go |
| P04 | 3723 | 1.8% | 1.8% | -0.2 | 40% | ❌ 38 pts to go |
| P05 | 422 | 0.7% | 0.7% | -0.2 | 20% | ❌ 19 pts to go |
| P06M | 14643 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 36661 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 273 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 696 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22009 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 3.3% | 3.3% | +1.0 | 50% | ❌ 47 pts to go |
| P10 | 2390 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1455 | 0.9% | 0.9% | +0.8 | n/a | no target |
| P12 | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 93957 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 192 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 34.8% | 34.8% | +0.0 | 80% | ❌ 45 pts to go |
| P02 | 466 | 51.9% | 51.9% | -0.1 | 90% | ❌ 38 pts to go |
| P03 | 263 | 32.7% | 32.7% | -0.9 | 80% | ❌ 47 pts to go |
| P04 | 3723 | 21.6% | 21.6% | -2.0 | 85% | ❌ 63 pts to go |
| P05 | 422 | 5.5% | 5.5% | +0.1 | 50% | ❌ 44 pts to go |
| P06M | 14643 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 36661 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 273 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 696 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22009 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 74.3% | 74.3% | -1.6 | 95% | ❌ 21 pts to go |
| P10 | 2390 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1455 | 4.3% | 4.3% | +3.7 | 50% | ❌ 46 pts to go |
| P12 | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 93957 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 192 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 8.5% | 8.5% | +0.0 | 50% | ❌ 42 pts to go |
| P02 | 466 | 6.2% | 6.2% | +0.0 | 50% | ❌ 44 pts to go |
| P03 | 263 | 1.9% | 1.9% | -0.1 | 30% | ❌ 28 pts to go |
| P04 | 3723 | 0.5% | 0.5% | +0.0 | 30% | ❌ 30 pts to go |
| P05 | 422 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 14643 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 36661 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 273 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 696 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22009 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P10 | 2390 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1455 | 0.3% | 0.3% | +0.3 | n/a | no target |
| P12 | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 93957 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 192 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 466 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 263 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3723 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 422 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 14643 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 36661 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 273 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 696 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 22009 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 307 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2390 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1455 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 93957 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 11.6% | 11.6% | -2.8 | 70% | ❌ 58 pts to go |
| P01T | 192 | 50.5% | 50.5% | +16.8 | 60% | 🟡 10 pts to go |
| P01_GOLD | 626 | 74.8% | 74.8% | +1.8 | 90% | ❌ 15 pts to go |
| P02 | 466 | 53.6% | 53.6% | -1.5 | 85% | ❌ 31 pts to go |
| P03 | 263 | 69.6% | 69.6% | -0.3 | 90% | ❌ 20 pts to go |
| P04 | 3723 | 35.0% | 35.0% | +2.5 | 75% | ❌ 40 pts to go |
| P05 | 422 | 54.7% | 54.7% | +4.8 | 50% | ✅ met |
| P06M | 14643 | 3.2% | 3.2% | +1.4 | n/a | no target |
| P06T | 36661 | 47.3% | 47.3% | +30.0 | n/a | no target |
| P06 | 273 | 44.0% | 44.0% | +21.2 | 40% | ✅ met |
| P07 | 696 | 33.0% | 33.0% | +16.6 | 50% | ❌ 17 pts to go |
| P08 | 22009 | 30.5% | 30.5% | +19.6 | 50% | ❌ 20 pts to go |
| P09 | 307 | 58.3% | 58.3% | +0.5 | 80% | ❌ 22 pts to go |
| P10 | 2390 | 34.5% | 34.5% | +5.8 | 40% | 🟡 6 pts to go |
| P11 | 1455 | 46.9% | 46.9% | -44.2 | 60% | ❌ 13 pts to go |
| P12 | 15 | 60.0% | 60.0% | -2.5 | 85% | ❌ 25 pts to go |
| P13 | 93957 | 31.7% | 31.7% | -59.3 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 59.7% | 59.7% | -7.3 | n/a | no target |
| P01T | 192 | 51.0% | 51.0% | +13.0 | n/a | no target |
| P01_GOLD | 626 | 72.7% | 72.7% | +2.3 | 95% | ❌ 22 pts to go |
| P02 | 466 | 73.8% | 73.8% | +0.0 | 95% | ❌ 21 pts to go |
| P03 | 263 | 71.9% | 71.9% | +0.0 | 95% | ❌ 23 pts to go |
| P04 | 3723 | 49.2% | 49.2% | +3.6 | 95% | ❌ 46 pts to go |
| P05 | 422 | 58.3% | 58.3% | +4.9 | 70% | ❌ 12 pts to go |
| P06M | 14643 | 46.0% | 46.0% | -8.6 | n/a | no target |
| P06T | 36661 | 56.2% | 56.2% | +25.9 | n/a | no target |
| P06 | 273 | 41.0% | 41.0% | +16.2 | 80% | ❌ 39 pts to go |
| P07 | 696 | 31.9% | 31.9% | +13.9 | 70% | ❌ 38 pts to go |
| P08 | 22009 | 30.3% | 30.3% | +16.2 | 70% | ❌ 40 pts to go |
| P09 | 307 | 86.6% | 86.6% | -0.9 | 100% | ❌ 13 pts to go |
| P10 | 2390 | 35.5% | 35.5% | +3.0 | 70% | ❌ 34 pts to go |
| P11 | 1455 | 52.5% | 52.5% | -39.7 | 75% | ❌ 22 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 93957 | 26.9% | 26.9% | +26.9 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 17.1% | 17.1% | +0.6 | n/a | no target |
| P01T | 192 | 53.6% | 53.6% | +27.7 | n/a | no target |
| P01_GOLD | 626 | 49.8% | 49.8% | +1.9 | 60% | ❌ 10 pts to go |
| P02 | 466 | 56.2% | 56.2% | +0.9 | 60% | 🟡 4 pts to go |
| P03 | 263 | 55.1% | 55.1% | +0.0 | 60% | 🟡 5 pts to go |
| P04 | 3723 | 42.1% | 42.1% | +5.4 | 55% | ❌ 13 pts to go |
| P05 | 422 | 24.6% | 24.6% | +2.4 | 50% | ❌ 25 pts to go |
| P06M | 14643 | 6.8% | 6.8% | +3.2 | n/a | no target |
| P06T | 36661 | 50.9% | 50.9% | +23.9 | n/a | no target |
| P06 | 273 | 47.6% | 47.6% | +12.4 | n/a | no target |
| P07 | 696 | 40.9% | 40.9% | +7.7 | 55% | ❌ 14 pts to go |
| P08 | 22009 | 36.2% | 36.2% | +9.3 | 50% | ❌ 14 pts to go |
| P09 | 307 | 72.3% | 72.3% | +1.3 | 70% | ✅ met |
| P10 | 2390 | 46.8% | 46.8% | +7.3 | 55% | 🟡 8 pts to go |
| P11 | 1455 | 52.2% | 52.2% | -39.8 | 50% | ✅ met |
| P12 | 15 | 86.7% | 86.7% | -0.8 | n/a | no target |
| P13 | 93957 | 3.4% | 3.4% | +3.4 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 50.4% | 50.4% | +36.0 | n/a | no target |
| P01T | 192 | 74.5% | 74.5% | +18.2 | n/a | no target |
| P01_GOLD | 626 | 50.5% | 50.5% | +2.6 | 70% | ❌ 20 pts to go |
| P02 | 466 | 58.2% | 58.2% | +4.2 | 70% | ❌ 12 pts to go |
| P03 | 263 | 51.3% | 51.3% | +1.7 | 70% | ❌ 19 pts to go |
| P04 | 3723 | 54.1% | 54.1% | +7.0 | 65% | ❌ 11 pts to go |
| P05 | 422 | 28.4% | 28.4% | -2.3 | 60% | ❌ 32 pts to go |
| P06M | 14643 | 36.6% | 36.6% | +33.1 | n/a | no target |
| P06T | 36661 | 80.0% | 80.0% | +16.2 | n/a | no target |
| P06 | 273 | 68.9% | 68.9% | +11.3 | 40% | ✅ met |
| P07 | 696 | 64.9% | 64.9% | +7.9 | 85% | ❌ 20 pts to go |
| P08 | 22009 | 65.3% | 65.3% | +8.4 | 85% | ❌ 20 pts to go |
| P09 | 307 | 59.3% | 59.3% | +5.8 | 85% | ❌ 26 pts to go |
| P10 | 2390 | 63.5% | 63.5% | +2.5 | 85% | ❌ 22 pts to go |
| P11 | 1455 | 61.9% | 61.9% | +55.5 | 75% | ❌ 13 pts to go |
| P12 | 15 | 26.7% | 26.7% | +1.7 | n/a | no target |
| P13 | 93957 | 91.2% | 91.2% | -8.8 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 56.6% | 56.6% | +37.0 | n/a | no target |
| P01T | 192 | 97.4% | 97.4% | +1.0 | n/a | no target |
| P01_GOLD | 626 | 79.6% | 79.6% | -9.7 | 90% | ❌ 10 pts to go |
| P02 | 466 | 83.9% | 83.9% | -5.3 | 90% | 🟡 6 pts to go |
| P03 | 263 | 87.8% | 87.8% | -3.2 | 90% | 🟡 2 pts to go |
| P04 | 3723 | 84.4% | 84.4% | -5.8 | 85% | 🟡 1 pts to go |
| P05 | 422 | 44.8% | 44.8% | -7.4 | 70% | ❌ 25 pts to go |
| P06M | 14643 | 43.6% | 43.6% | +37.4 | n/a | no target |
| P06T | 36661 | 100.0% | 100.0% | +8.0 | n/a | no target |
| P06 | 273 | 99.3% | 99.3% | +1.0 | 50% | ✅ met |
| P07 | 696 | 99.9% | 99.9% | +0.8 | 100% | 🟡 0 pts to go |
| P08 | 22009 | 99.8% | 99.8% | +0.4 | 100% | 🟡 0 pts to go |
| P09 | 307 | 79.8% | 79.8% | -0.4 | 100% | ❌ 20 pts to go |
| P10 | 2390 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1455 | 97.3% | 97.3% | -2.4 | 100% | 🟡 3 pts to go |
| P12 | 15 | 53.3% | 53.3% | +15.8 | n/a | no target |
| P13 | 93957 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 15.5% | 15.5% | +1.1 | n/a | no target |
| P01T | 192 | 65.1% | 65.1% | +16.0 | n/a | no target |
| P01_GOLD | 626 | 43.5% | 43.5% | -1.7 | 70% | ❌ 26 pts to go |
| P02 | 466 | 48.7% | 48.7% | -0.8 | 75% | ❌ 26 pts to go |
| P03 | 263 | 43.3% | 43.3% | -1.2 | 75% | ❌ 32 pts to go |
| P04 | 3723 | 38.7% | 38.7% | +1.3 | 70% | ❌ 31 pts to go |
| P05 | 422 | 22.0% | 22.0% | -3.5 | 55% | ❌ 33 pts to go |
| P06M | 14643 | 4.8% | 4.8% | +1.5 | n/a | no target |
| P06T | 36661 | 62.1% | 62.1% | +22.5 | n/a | no target |
| P06 | 273 | 46.9% | 46.9% | +4.1 | n/a | no target |
| P07 | 696 | 50.0% | 50.0% | +4.1 | 70% | ❌ 20 pts to go |
| P08 | 22009 | 54.8% | 54.8% | +4.9 | 75% | ❌ 20 pts to go |
| P09 | 307 | 49.2% | 49.2% | -0.6 | 85% | ❌ 36 pts to go |
| P10 | 2390 | 43.6% | 43.6% | +0.1 | 80% | ❌ 36 pts to go |
| P11 | 1455 | 54.3% | 54.3% | +49.3 | 70% | ❌ 16 pts to go |
| P12 | 15 | 40.0% | 40.0% | +15.0 | n/a | no target |
| P13 | 93957 | 5.2% | 5.2% | +5.2 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 56.6% | 56.6% | +43.2 | n/a | no target |
| P01T | 192 | 94.8% | 94.8% | +5.0 | n/a | no target |
| P01_GOLD | 626 | 73.8% | 73.8% | -3.7 | 90% | ❌ 16 pts to go |
| P02 | 466 | 79.0% | 79.0% | +1.4 | 90% | ❌ 11 pts to go |
| P03 | 263 | 83.3% | 83.3% | +0.1 | 90% | 🟡 7 pts to go |
| P04 | 3723 | 76.4% | 76.4% | +0.8 | 85% | 🟡 9 pts to go |
| P05 | 422 | 43.1% | 43.1% | -5.6 | 75% | ❌ 32 pts to go |
| P06M | 14643 | 43.3% | 43.3% | +39.2 | n/a | no target |
| P06T | 36661 | 96.7% | 96.7% | +13.5 | n/a | no target |
| P06 | 273 | 90.5% | 90.5% | +11.2 | n/a | no target |
| P07 | 696 | 92.5% | 92.5% | +10.9 | 100% | 🟡 8 pts to go |
| P08 | 22009 | 90.8% | 90.8% | +11.9 | 100% | 🟡 9 pts to go |
| P09 | 307 | 66.1% | 66.1% | +4.7 | n/a | no target |
| P10 | 2390 | 86.8% | 86.8% | +2.6 | 100% | ❌ 13 pts to go |
| P11 | 1455 | 87.7% | 87.7% | -0.7 | n/a | no target |
| P12 | 15 | 46.7% | 46.7% | +9.2 | n/a | no target |
| P13 | 93957 | 65.2% | 65.2% | -18.0 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 46.5% | 46.5% | -7.1 | n/a | no target · QC vendors: 49 rows, 100.0% filled |
| P01T | 192 | 9.4% | 9.4% | -8.4 | n/a | no target · QC vendors: 4 rows, 75.0% filled |
| P01_GOLD | 626 | 43.8% | 43.8% | +0.2 | 95% | ❌ 51 pts to go · QC vendors: 54 rows, 98.1% filled |
| P02 | 466 | 55.6% | 55.6% | +0.5 | 95% | ❌ 39 pts to go · QC vendors: 113 rows, 100.0% filled |
| P03 | 263 | 46.0% | 46.0% | -0.5 | 95% | ❌ 49 pts to go · QC vendors: 21 rows, 100.0% filled |
| P04 | 3723 | 32.2% | 32.2% | +0.3 | 95% | ❌ 63 pts to go · QC vendors: 617 rows, 98.1% filled |
| P05 | 422 | 14.0% | 14.0% | -0.8 | n/a | no target · QC vendors: 34 rows, 94.1% filled |
| P06M | 14643 | 42.8% | 42.8% | -10.5 | n/a | no target · QC vendors: 5555 rows, 99.8% filled |
| P06T | 36661 | 5.3% | 5.3% | -12.2 | n/a | no target · QC vendors: 1993 rows, 77.2% filled |
| P06 | 273 | 8.4% | 8.4% | +0.1 | n/a | no target · QC vendors: 16 rows, 68.8% filled |
| P07 | 696 | 6.3% | 6.3% | -0.5 | n/a | no target · QC vendors: 39 rows, 76.9% filled |
| P08 | 22009 | 6.6% | 6.6% | +0.1 | n/a | no target · QC vendors: 1282 rows, 92.9% filled |
| P09 | 307 | 76.9% | 76.9% | -1.3 | 95% | ❌ 18 pts to go · QC vendors: 112 rows, 100.0% filled |
| P10 | 2390 | 15.6% | 15.6% | -2.0 | n/a | no target · QC vendors: 228 rows, 89.9% filled |
| P11 | 1455 | 14.8% | 14.8% | -66.7 | n/a | no target · QC vendors: 153 rows, 91.5% filled |
| P12 | 15 | 73.3% | 73.3% | +10.8 | n/a | no target · QC vendors: 3 rows, 100.0% filled |
| P13 | 93957 | 26.2% | 26.2% | +26.2 | n/a | no target · QC vendors: 24592 rows, 100.0% filled |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 58.9% | 58.9% | -6.0 | n/a | no target · vendors with a registry record: 76 rows, 100.0% filled |
| P01T | 192 | 51.0% | 51.0% | +12.7 | n/a | no target · vendors with a registry record: 98 rows, 100.0% filled |
| P01_GOLD | 626 | 81.5% | 81.5% | +2.1 | 100% | ❌ 18 pts to go · vendors with a registry record: 510 rows, 100.0% filled |
| P02 | 466 | 77.5% | 77.5% | +0.1 | 100% | ❌ 22 pts to go · vendors with a registry record: 361 rows, 100.0% filled |
| P03 | 263 | 81.0% | 81.0% | -0.2 | 100% | ❌ 19 pts to go · vendors with a registry record: 213 rows, 100.0% filled |
| P04 | 3723 | 49.7% | 49.7% | +3.6 | 100% | ❌ 50 pts to go · vendors with a registry record: 1851 rows, 100.0% filled |
| P05 | 422 | 63.3% | 63.3% | +5.0 | n/a | no target · vendors with a registry record: 267 rows, 100.0% filled |
| P06M | 14643 | 45.9% | 45.9% | -8.4 | n/a | no target · vendors with a registry record: 6718 rows, 100.0% filled |
| P06T | 36661 | 56.2% | 56.2% | +25.8 | n/a | no target · vendors with a registry record: 20619 rows, 100.0% filled |
| P06 | 273 | 41.4% | 41.4% | +15.9 | n/a | no target · vendors with a registry record: 113 rows, 100.0% filled |
| P07 | 696 | 32.3% | 32.3% | +13.9 | n/a | no target · vendors with a registry record: 225 rows, 100.0% filled |
| P08 | 22009 | 30.4% | 30.4% | +16.1 | n/a | no target · vendors with a registry record: 6701 rows, 100.0% filled |
| P09 | 307 | 90.6% | 90.6% | -0.5 | n/a | no target · vendors with a registry record: 278 rows, 100.0% filled |
| P10 | 2390 | 36.2% | 36.2% | +3.0 | n/a | no target · vendors with a registry record: 865 rows, 100.0% filled |
| P11 | 1455 | 53.6% | 53.6% | -38.7 | n/a | no target · vendors with a registry record: 780 rows, 100.0% filled |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 15 rows, 100.0% filled |
| P13 | 93957 | 26.9% | 26.9% | +26.9 | n/a | no target · vendors with a registry record: 25276 rows, 100.0% filled |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 93.8% | 93.8% | +5.1 | 90% | ✅ met |
| P01T | 192 | 72.4% | 72.4% | +16.1 | 90% | ❌ 18 pts to go |
| P01_GOLD | 626 | 87.7% | 87.7% | +4.0 | 95% | 🟡 7 pts to go |
| P02 | 466 | 87.8% | 87.8% | +2.6 | 95% | 🟡 7 pts to go |
| P03 | 263 | 84.4% | 84.4% | +5.5 | 85% | 🟡 1 pts to go |
| P04 | 3723 | 63.0% | 63.0% | +6.6 | 90% | ❌ 27 pts to go |
| P05 | 422 | 79.1% | 79.1% | +11.4 | 75% | ✅ met |
| P06M | 14643 | 91.6% | 91.6% | +4.5 | n/a | no target |
| P06T | 36661 | 37.3% | 37.3% | +8.3 | n/a | no target |
| P06 | 273 | 73.6% | 73.6% | +16.7 | 80% | 🟡 6 pts to go |
| P07 | 696 | 59.8% | 59.9% | +13.6 | 80% | ❌ 20 pts to go |
| P08 | 22009 | 54.4% | 54.4% | +15.9 | 75% | ❌ 21 pts to go |
| P09 | 307 | 76.9% | 76.9% | -0.3 | 95% | ❌ 18 pts to go |
| P10 | 2390 | 46.7% | 46.7% | +7.7 | 70% | ❌ 23 pts to go |
| P11 | 1455 | 31.3% | 31.3% | +21.7 | 65% | ❌ 34 pts to go |
| P12 | 15 | 80.0% | 80.0% | +5.0 | 80% | ✅ met |
| P13 | 93957 | 47.5% | 47.5% | +8.3 | 60% | ❌ 12 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 20.2% | 20.2% | +0.6 | 50% | ❌ 30 pts to go |
| P01T | 192 | 16.1% | 16.1% | +2.8 | n/a | no target |
| P01_GOLD | 626 | 19.5% | 19.5% | -1.1 | 40% | ❌ 20 pts to go |
| P02 | 466 | 19.1% | 19.1% | +0.2 | 40% | ❌ 21 pts to go |
| P03 | 263 | 21.3% | 21.3% | -1.0 | 40% | ❌ 19 pts to go |
| P04 | 3723 | 15.2% | 15.2% | -1.1 | 40% | ❌ 25 pts to go |
| P05 | 422 | 17.5% | 17.5% | -2.2 | 25% | 🟡 8 pts to go |
| P06M | 14643 | 11.6% | 11.6% | +2.8 | n/a | no target |
| P06T | 36661 | 6.9% | 6.9% | -0.6 | n/a | no target |
| P06 | 273 | 12.8% | 12.8% | +0.0 | 35% | ❌ 22 pts to go |
| P07 | 696 | 14.1% | 14.1% | +2.6 | 35% | ❌ 21 pts to go |
| P08 | 22009 | 15.4% | 15.4% | +5.0 | 35% | ❌ 20 pts to go |
| P09 | 307 | 16.3% | 16.3% | +0.1 | n/a | no target |
| P10 | 2390 | 6.7% | 6.7% | +0.2 | 30% | ❌ 23 pts to go |
| P11 | 1455 | 7.4% | 7.4% | +6.2 | n/a | no target |
| P12 | 15 | 6.7% | 6.7% | -5.8 | n/a | no target |
| P13 | 93957 | 12.3% | 12.3% | -8.7 | 30% | ❌ 18 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 192 | 84.4% | 84.4% | -7.5 | 100% | ❌ 16 pts to go |
| P01_GOLD | 626 | 90.7% | 90.7% | +1.2 | 100% | 🟡 9 pts to go |
| P02 | 466 | 95.5% | 95.5% | +0.2 | 100% | 🟡 4 pts to go |
| P03 | 263 | 89.4% | 89.4% | -0.1 | 100% | ❌ 11 pts to go |
| P04 | 3723 | 71.4% | 71.4% | -4.5 | 100% | ❌ 29 pts to go |
| P05 | 422 | 89.3% | 89.3% | +1.9 | 100% | ❌ 11 pts to go |
| P06M | 14643 | 99.2% | 99.2% | +0.4 | n/a | no target |
| P06T | 36661 | 59.3% | 59.3% | -18.1 | n/a | no target |
| P06 | 273 | 78.8% | 78.8% | -2.2 | 95% | ❌ 16 pts to go |
| P07 | 696 | 81.2% | 81.2% | -2.4 | 95% | ❌ 14 pts to go |
| P08 | 22009 | 78.3% | 78.3% | -1.9 | 95% | ❌ 17 pts to go |
| P09 | 307 | 96.1% | 96.1% | +0.4 | 100% | 🟡 4 pts to go |
| P10 | 2390 | 54.4% | 54.4% | -10.7 | 95% | ❌ 41 pts to go |
| P11 | 1455 | 49.4% | 49.4% | -37.8 | 80% | ❌ 31 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 93957 | 100.0% | 100.0% | +24.8 | 95% | ✅ met |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 86.0% | 86.0% | +0.4 | n/a | no target |
| P01T | 192 | 68.2% | 68.2% | +4.6 | n/a | no target |
| P01_GOLD | 626 | 73.0% | 73.0% | +3.5 | 90% | ❌ 17 pts to go |
| P02 | 466 | 77.9% | 77.9% | +2.2 | 95% | ❌ 17 pts to go |
| P03 | 263 | 74.9% | 74.9% | +1.1 | 95% | ❌ 20 pts to go |
| P04 | 3723 | 68.9% | 68.9% | +2.3 | 95% | ❌ 26 pts to go |
| P05 | 422 | 73.5% | 73.5% | +3.0 | 90% | ❌ 16 pts to go |
| P06M | 14643 | 86.9% | 86.9% | +0.5 | n/a | no target |
| P06T | 36661 | 57.2% | 57.2% | +9.3 | n/a | no target |
| P06 | 273 | 68.5% | 68.5% | +5.4 | 95% | ❌ 26 pts to go |
| P07 | 696 | 64.8% | 64.8% | +9.8 | 90% | ❌ 25 pts to go |
| P08 | 22009 | 67.8% | 67.8% | +9.0 | 95% | ❌ 27 pts to go |
| P09 | 307 | 87.0% | 87.0% | +0.9 | 100% | ❌ 13 pts to go |
| P10 | 2390 | 55.3% | 55.3% | -1.2 | 95% | ❌ 40 pts to go |
| P11 | 1455 | 28.9% | 28.9% | +17.7 | 75% | ❌ 46 pts to go |
| P12 | 15 | 93.3% | 93.3% | +18.3 | n/a | no target |
| P13 | 93957 | 70.8% | 70.8% | +23.2 | 95% | ❌ 24 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 87.6% | 87.6% | +16.5 | n/a | no target |
| P01T | 192 | 83.3% | 83.3% | +9.2 | 95% | ❌ 12 pts to go |
| P01_GOLD | 626 | 84.8% | 84.8% | +4.1 | 90% | 🟡 5 pts to go |
| P02 | 466 | 90.6% | 90.6% | +4.8 | 95% | 🟡 4 pts to go |
| P03 | 263 | 85.6% | 85.6% | +1.6 | 95% | 🟡 9 pts to go |
| P04 | 3723 | 89.2% | 89.2% | +5.9 | 90% | 🟡 1 pts to go |
| P05 | 422 | 93.1% | 93.1% | +4.6 | 95% | 🟡 2 pts to go |
| P06M | 14643 | 93.2% | 93.2% | +26.5 | n/a | no target |
| P06T | 36661 | 74.9% | 74.9% | +13.4 | n/a | no target |
| P06 | 273 | 92.3% | 92.3% | +10.2 | 100% | 🟡 8 pts to go |
| P07 | 696 | 92.2% | 92.2% | +15.0 | 100% | 🟡 8 pts to go |
| P08 | 22009 | 92.3% | 92.3% | +15.2 | 100% | 🟡 8 pts to go |
| P09 | 307 | 73.0% | 73.0% | +4.4 | n/a | no target |
| P10 | 2390 | 91.3% | 91.3% | +4.5 | 100% | 🟡 9 pts to go |
| P11 | 1455 | 41.9% | 41.9% | +23.1 | 80% | ❌ 38 pts to go |
| P12 | 15 | 100.0% | 100.0% | +25.0 | n/a | no target |
| P13 | 93957 | 83.7% | 83.7% | +32.7 | 95% | ❌ 11 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 3.1% | 3.1% | -1.0 | n/a | no target |
| P01T | 192 | 9.4% | 9.4% | +1.0 | n/a | no target |
| P01_GOLD | 626 | 14.2% | 14.2% | +0.0 | 25% | ❌ 11 pts to go |
| P02 | 466 | 25.3% | 25.3% | +0.8 | 40% | ❌ 15 pts to go |
| P03 | 263 | 9.1% | 9.1% | +0.1 | 20% | ❌ 11 pts to go |
| P04 | 3723 | 3.5% | 3.5% | -0.1 | 20% | ❌ 16 pts to go |
| P05 | 422 | 3.3% | 3.3% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 14643 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 36661 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 273 | 5.1% | 5.1% | -1.1 | n/a | no target |
| P07 | 696 | 8.5% | 8.5% | +1.2 | n/a | no target |
| P08 | 22009 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P09 | 307 | 7.8% | 7.8% | +0.2 | n/a | no target |
| P10 | 2390 | 0.8% | 0.8% | -0.2 | n/a | no target |
| P11 | 1455 | 1.0% | 1.0% | +0.8 | n/a | no target |
| P12 | 15 | 6.7% | 6.7% | +6.7 | n/a | no target |
| P13 | 93957 | 0.3% | 0.3% | -0.1 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 18.6% | 18.6% | -8.2 | n/a | no target |
| P01T | 192 | 22.4% | 22.4% | -1.7 | 70% | ❌ 48 pts to go |
| P01_GOLD | 626 | 43.5% | 43.5% | +0.2 | 80% | ❌ 36 pts to go |
| P02 | 466 | 57.3% | 57.3% | +0.5 | 90% | ❌ 33 pts to go |
| P03 | 263 | 18.6% | 18.6% | -0.5 | 60% | ❌ 41 pts to go |
| P04 | 3723 | 21.6% | 21.6% | -2.1 | 85% | ❌ 63 pts to go |
| P05 | 422 | 11.6% | 11.6% | -0.3 | 50% | ❌ 38 pts to go |
| P06M | 14643 | 0.6% | 0.6% | +0.2 | n/a | no target |
| P06T | 36661 | 0.7% | 0.7% | +0.1 | n/a | no target |
| P06 | 273 | 15.4% | 15.4% | -0.8 | n/a | no target |
| P07 | 696 | 10.5% | 10.5% | -2.5 | n/a | no target |
| P08 | 22009 | 0.6% | 0.6% | +0.1 | n/a | no target |
| P09 | 307 | 77.9% | 77.9% | +0.3 | 95% | ❌ 17 pts to go |
| P10 | 2390 | 1.7% | 1.7% | +0.0 | n/a | no target |
| P11 | 1455 | 16.7% | 16.7% | +13.1 | n/a | no target |
| P12 | 15 | 26.7% | 26.7% | +1.7 | n/a | no target |
| P13 | 93957 | 0.5% | 0.5% | -0.2 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 6.2% | 6.2% | -1.0 | n/a | no target |
| P01T | 192 | 10.4% | 10.4% | -1.6 | n/a | no target |
| P01_GOLD | 626 | 34.0% | 34.0% | +0.1 | 70% | ❌ 36 pts to go |
| P02 | 466 | 39.1% | 39.1% | +0.2 | 75% | ❌ 36 pts to go |
| P03 | 263 | 18.6% | 18.6% | -0.5 | 55% | ❌ 36 pts to go |
| P04 | 3723 | 21.6% | 21.6% | -2.0 | 75% | ❌ 53 pts to go |
| P05 | 422 | 10.7% | 10.7% | -0.1 | 50% | ❌ 39 pts to go |
| P06M | 14643 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06T | 36661 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P06 | 273 | 5.9% | 5.9% | -2.4 | n/a | no target |
| P07 | 696 | 5.2% | 5.2% | -1.2 | n/a | no target |
| P08 | 22009 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 307 | 75.2% | 75.2% | +0.0 | 95% | ❌ 20 pts to go |
| P10 | 2390 | 0.9% | 0.9% | -0.1 | n/a | no target |
| P11 | 1455 | 16.4% | 16.4% | +12.8 | n/a | no target |
| P12 | 15 | 20.0% | 20.0% | +7.5 | n/a | no target |
| P13 | 93957 | 0.3% | 0.3% | -0.1 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 7.8% | 7.8% | +1.6 | n/a | no target |
| P01T | 192 | 8.3% | 8.3% | -1.0 | n/a | no target |
| P01_GOLD | 626 | 58.0% | 58.1% | +0.0 | 80% | ❌ 22 pts to go |
| P02 | 466 | 45.7% | 45.9% | -0.1 | 75% | ❌ 29 pts to go |
| P03 | 263 | 37.3% | 37.3% | -0.6 | 70% | ❌ 33 pts to go |
| P04 | 3723 | 21.1% | 21.6% | -2.0 | 70% | ❌ 49 pts to go |
| P05 | 422 | 14.2% | 14.2% | -0.1 | 50% | ❌ 36 pts to go |
| P06M | 14643 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06T | 36661 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 273 | 16.5% | 16.5% | +3.1 | n/a | no target |
| P07 | 696 | 2.0% | 2.0% | +0.0 | n/a | no target |
| P08 | 22009 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P09 | 307 | 46.6% | 46.9% | +0.7 | 80% | ❌ 33 pts to go |
| P10 | 2390 | 1.2% | 1.3% | +0.0 | n/a | no target |
| P11 | 1455 | 6.8% | 6.9% | +5.7 | n/a | no target |
| P12 | 15 | 40.0% | 40.0% | +2.5 | n/a | no target |
| P13 | 93957 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 18.6% | 18.6% | +7.3 | n/a | no target |
| P01T | 192 | 21.4% | 21.4% | -0.6 | 60% | ❌ 39 pts to go |
| P01_GOLD | 626 | 63.4% | 63.4% | -0.2 | 70% | 🟡 7 pts to go |
| P02 | 466 | 39.7% | 39.7% | +0.8 | 50% | ❌ 10 pts to go |
| P03 | 263 | 48.3% | 48.3% | -1.7 | 55% | 🟡 7 pts to go |
| P04 | 3723 | 12.2% | 12.2% | -1.1 | 40% | ❌ 28 pts to go |
| P05 | 422 | 17.1% | 17.1% | -0.2 | 40% | ❌ 23 pts to go |
| P06M | 14643 | 2.2% | 2.2% | +1.5 | n/a | no target |
| P06T | 36661 | 1.7% | 1.7% | -0.7 | n/a | no target |
| P06 | 273 | 22.0% | 22.0% | +2.3 | n/a | no target |
| P07 | 696 | 6.6% | 6.6% | -0.1 | n/a | no target |
| P08 | 22009 | 2.9% | 2.9% | +0.3 | n/a | no target |
| P09 | 307 | 5.9% | 5.9% | +0.0 | n/a | no target |
| P10 | 2390 | 4.6% | 4.6% | +0.1 | n/a | no target |
| P11 | 1455 | 5.2% | 5.2% | +0.9 | n/a | no target |
| P12 | 15 | 6.7% | 6.7% | -5.8 | n/a | no target |
| P13 | 93957 | 1.0% | 1.0% | +0.8 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 21.7% | 21.7% | +5.2 | n/a | no target |
| P01T | 192 | 28.6% | 28.6% | +3.3 | 65% | ❌ 36 pts to go |
| P01_GOLD | 626 | 69.0% | 69.0% | +0.0 | 70% | 🟡 1 pts to go |
| P02 | 466 | 24.2% | 24.2% | +0.3 | 50% | ❌ 26 pts to go |
| P03 | 263 | 52.5% | 52.5% | +0.2 | 60% | 🟡 8 pts to go |
| P04 | 3723 | 5.4% | 5.4% | -0.4 | 40% | ❌ 35 pts to go |
| P05 | 422 | 19.7% | 19.7% | +0.0 | 45% | ❌ 25 pts to go |
| P06M | 14643 | 1.4% | 1.4% | +1.1 | n/a | no target |
| P06T | 36661 | 0.7% | 0.7% | +0.1 | n/a | no target |
| P06 | 273 | 34.4% | 34.4% | +2.7 | n/a | no target |
| P07 | 696 | 6.9% | 6.9% | +0.0 | n/a | no target |
| P08 | 22009 | 1.3% | 1.3% | +0.2 | n/a | no target |
| P09 | 307 | 9.8% | 9.8% | -0.1 | n/a | no target |
| P10 | 2390 | 3.1% | 3.1% | +0.5 | n/a | no target |
| P11 | 1455 | 5.1% | 5.1% | +4.1 | n/a | no target |
| P12 | 15 | 6.7% | 6.7% | +6.7 | n/a | no target |
| P13 | 93957 | 0.3% | 0.3% | +0.1 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 12.4% | 12.4% | +6.2 | n/a | no target |
| P01T | 192 | 13.5% | 13.5% | -1.0 | n/a | no target |
| P01_GOLD | 626 | 49.8% | 49.8% | +0.0 | 50% | 🟡 0 pts to go |
| P02 | 466 | 37.3% | 37.3% | -0.1 | n/a | no target |
| P03 | 263 | 52.1% | 52.1% | -1.0 | 60% | 🟡 8 pts to go |
| P04 | 3723 | 11.9% | 11.9% | -1.0 | n/a | no target |
| P05 | 422 | 15.2% | 15.2% | +0.0 | n/a | no target |
| P06M | 14643 | 0.5% | 0.5% | +0.2 | n/a | no target |
| P06T | 36661 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P06 | 273 | 25.6% | 25.6% | +3.9 | n/a | no target |
| P07 | 696 | 8.3% | 8.3% | +1.1 | n/a | no target |
| P08 | 22009 | 0.6% | 0.6% | +0.1 | n/a | no target |
| P09 | 307 | 17.6% | 17.6% | -0.6 | n/a | no target |
| P10 | 2390 | 2.4% | 2.4% | +0.1 | n/a | no target |
| P11 | 1455 | 4.7% | 4.7% | +3.9 | n/a | no target |
| P12 | 15 | 13.3% | 13.3% | +13.3 | n/a | no target |
| P13 | 93957 | 0.3% | 0.3% | -0.1 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 11.6% | 11.6% | +0.3 | 15% | 🟡 3 pts to go |
| P01T | 192 | 12.5% | 12.5% | +1.4 | 15% | 🟡 2 pts to go |
| P01_GOLD | 626 | 35.3% | 35.3% | +0.0 | 40% | 🟡 5 pts to go |
| P02 | 466 | 12.9% | 13.1% | +0.4 | 25% | ❌ 12 pts to go |
| P03 | 263 | 17.5% | 17.5% | -0.5 | 25% | 🟡 8 pts to go |
| P04 | 3723 | 2.7% | 2.7% | -0.1 | 15% | ❌ 12 pts to go |
| P05 | 422 | 6.6% | 6.6% | -0.2 | 15% | 🟡 8 pts to go |
| P06M | 14643 | 0.9% | 0.9% | +0.3 | 15% | ❌ 14 pts to go |
| P06T | 36661 | 0.5% | 0.5% | +0.1 | 15% | ❌ 14 pts to go |
| P06 | 273 | 10.6% | 10.6% | +1.3 | 15% | 🟡 4 pts to go |
| P07 | 696 | 4.3% | 4.3% | +1.1 | 15% | ❌ 11 pts to go |
| P08 | 22009 | 0.6% | 0.6% | +0.2 | 15% | ❌ 14 pts to go |
| P09 | 307 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2390 | 1.3% | 1.3% | +0.3 | 15% | ❌ 14 pts to go |
| P11 | 1455 | 1.5% | 1.5% | +1.3 | 15% | ❌ 14 pts to go |
| P12 | 15 | 0.0% | 0.0% | -12.5 | 15% | ❌ 15 pts to go |
| P13 | 93957 | 0.7% | 0.7% | +0.3 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 5.4% | 5.4% | -0.8 | 15% | 🟡 10 pts to go |
| P01T | 192 | 11.5% | 11.5% | -0.5 | 25% | ❌ 14 pts to go |
| P01_GOLD | 626 | 29.2% | 29.2% | +0.0 | 25% | ✅ met |
| P02 | 466 | 25.3% | 25.3% | -0.1 | 15% | ✅ met |
| P03 | 263 | 22.1% | 22.1% | +0.6 | 15% | ✅ met |
| P04 | 3723 | 4.0% | 4.0% | -0.1 | 15% | ❌ 11 pts to go |
| P05 | 422 | 11.1% | 11.1% | +0.3 | 15% | 🟡 4 pts to go |
| P06M | 14643 | 0.5% | 0.5% | +0.3 | 15% | ❌ 14 pts to go |
| P06T | 36661 | 0.2% | 0.2% | -0.1 | 15% | ❌ 15 pts to go |
| P06 | 273 | 8.4% | 8.4% | +0.8 | 15% | 🟡 7 pts to go |
| P07 | 696 | 2.9% | 2.9% | -0.2 | 15% | ❌ 12 pts to go |
| P08 | 22009 | 0.5% | 0.5% | +0.1 | 15% | ❌ 14 pts to go |
| P09 | 307 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2390 | 1.6% | 1.6% | +0.0 | 15% | ❌ 13 pts to go |
| P11 | 1455 | 2.7% | 2.7% | +2.2 | 15% | ❌ 12 pts to go |
| P12 | 15 | 20.0% | 20.0% | -5.0 | 15% | ✅ met |
| P13 | 93957 | 0.2% | 0.2% | +0.2 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 2.3% | 2.3% | +2.3 | 20% | ❌ 18 pts to go |
| P01T | 192 | 4.2% | 4.2% | +0.3 | 20% | ❌ 16 pts to go |
| P01_GOLD | 626 | 4.5% | 4.5% | +0.2 | 20% | ❌ 16 pts to go |
| P02 | 466 | 1.5% | 1.5% | +0.2 | 20% | ❌ 18 pts to go |
| P03 | 263 | 1.5% | 1.5% | -0.1 | 20% | ❌ 18 pts to go |
| P04 | 3723 | 0.6% | 0.6% | +0.0 | 20% | ❌ 19 pts to go |
| P05 | 422 | 1.2% | 1.2% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 14643 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 36661 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 273 | 1.5% | 1.5% | +0.1 | 20% | ❌ 18 pts to go |
| P07 | 696 | 0.4% | 0.4% | +0.0 | 20% | ❌ 20 pts to go |
| P08 | 22009 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P09 | 307 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2390 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 1455 | 0.3% | 0.3% | +0.3 | 20% | ❌ 20 pts to go |
| P12 | 15 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 93957 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 1.6% | 1.6% | +0.6 | 15% | ❌ 13 pts to go |
| P01T | 192 | 3.1% | 3.1% | +0.7 | 15% | ❌ 12 pts to go |
| P01_GOLD | 626 | 10.4% | 10.4% | -0.1 | 15% | 🟡 5 pts to go |
| P02 | 466 | 12.0% | 12.0% | +0.0 | 15% | 🟡 3 pts to go |
| P03 | 263 | 20.2% | 20.2% | -0.5 | 15% | ✅ met |
| P04 | 3723 | 2.3% | 2.3% | -0.1 | 15% | ❌ 13 pts to go |
| P05 | 422 | 2.8% | 2.8% | -0.2 | 15% | ❌ 12 pts to go |
| P06M | 14643 | 0.3% | 0.3% | +0.1 | 15% | ❌ 15 pts to go |
| P06T | 36661 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 273 | 5.1% | 5.1% | -0.1 | 15% | 🟡 10 pts to go |
| P07 | 696 | 1.6% | 1.6% | -0.1 | 15% | ❌ 13 pts to go |
| P08 | 22009 | 0.5% | 0.5% | +0.1 | 15% | ❌ 14 pts to go |
| P09 | 307 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2390 | 1.0% | 1.0% | +0.1 | 15% | ❌ 14 pts to go |
| P11 | 1455 | 1.2% | 1.2% | +0.9 | 15% | ❌ 14 pts to go |
| P12 | 15 | 6.7% | 6.7% | +6.7 | 15% | 🟡 8 pts to go |
| P13 | 93957 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 14.0% | 14.0% | +6.8 | 20% | 🟡 6 pts to go |
| P01T | 192 | 14.1% | 14.1% | -1.0 | 40% | ❌ 26 pts to go |
| P01_GOLD | 626 | 46.2% | 46.2% | +0.4 | 40% | ✅ met |
| P02 | 466 | 42.9% | 42.9% | +0.1 | 20% | ✅ met |
| P03 | 263 | 49.0% | 49.0% | +0.2 | 35% | ✅ met |
| P04 | 3723 | 14.2% | 14.2% | -1.2 | 20% | 🟡 6 pts to go |
| P05 | 422 | 15.4% | 15.4% | +0.6 | 20% | 🟡 5 pts to go |
| P06M | 14643 | 0.8% | 0.8% | +0.3 | 20% | ❌ 19 pts to go |
| P06T | 36661 | 0.7% | 0.7% | +0.0 | 20% | ❌ 19 pts to go |
| P06 | 273 | 25.3% | 25.3% | +3.2 | 20% | ✅ met |
| P07 | 696 | 8.6% | 8.6% | +1.5 | 20% | ❌ 11 pts to go |
| P08 | 22009 | 1.0% | 1.0% | +0.1 | 20% | ❌ 19 pts to go |
| P09 | 307 | 18.2% | 18.2% | +0.0 | 20% | 🟡 2 pts to go |
| P10 | 2390 | 3.7% | 3.7% | +0.3 | 20% | ❌ 16 pts to go |
| P11 | 1455 | 4.8% | 4.8% | +3.8 | 20% | ❌ 15 pts to go |
| P12 | 15 | 6.7% | 6.7% | +6.7 | 20% | ❌ 13 pts to go |
| P13 | 93957 | 0.5% | 0.5% | +0.0 | 20% | ❌ 20 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 33.3% | 33.3% | -11.0 | n/a | no target |
| P01T | 192 | 0.5% | 0.5% | +0.2 | n/a | no target |
| P01_GOLD | 626 | 69.5% | 69.5% | +0.0 | 95% | ❌ 26 pts to go |
| P02 | 466 | 62.9% | 62.9% | -0.1 | 95% | ❌ 32 pts to go |
| P03 | 263 | 53.2% | 53.2% | -1.5 | 90% | ❌ 37 pts to go |
| P04 | 3723 | 24.8% | 24.8% | -2.3 | 85% | ❌ 60 pts to go |
| P05 | 422 | 37.7% | 37.7% | +1.2 | 75% | ❌ 37 pts to go |
| P06M | 14643 | 36.1% | 36.1% | -14.0 | n/a | no target |
| P06T | 36661 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 273 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 696 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22009 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 88.3% | 88.3% | -1.1 | 100% | ❌ 12 pts to go |
| P10 | 2390 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1455 | 6.0% | 6.0% | +5.1 | 60% | ❌ 54 pts to go |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 93957 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 33.3% | 33.3% | -11.0 | n/a | no target |
| P01T | 192 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 72.8% | 72.8% | +0.0 | 100% | ❌ 27 pts to go |
| P02 | 466 | 66.3% | 66.3% | -0.2 | 100% | ❌ 34 pts to go |
| P03 | 263 | 58.9% | 58.9% | -1.6 | n/a | no target |
| P04 | 3723 | 25.5% | 25.5% | -2.3 | 95% | ❌ 70 pts to go |
| P05 | 422 | 33.4% | 33.4% | +0.4 | 80% | ❌ 47 pts to go |
| P06M | 14643 | 36.1% | 36.1% | -14.0 | n/a | no target |
| P06T | 36661 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 273 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 696 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22009 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 91.5% | 91.5% | -1.2 | 100% | 🟡 8 pts to go |
| P10 | 2390 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1455 | 6.4% | 6.4% | +5.4 | n/a | no target |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 93957 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 79.8% | 79.8% | +1.4 | n/a | no target |
| P01T | 192 | 0.5% | 0.5% | +0.2 | n/a | no target |
| P01_GOLD | 626 | 51.6% | 51.6% | +0.0 | 85% | ❌ 33 pts to go |
| P02 | 466 | 57.5% | 57.5% | -0.1 | 90% | ❌ 32 pts to go |
| P03 | 263 | 42.6% | 42.6% | -1.5 | 85% | ❌ 42 pts to go |
| P04 | 3723 | 27.9% | 27.9% | -2.5 | 90% | ❌ 62 pts to go |
| P05 | 422 | 32.7% | 32.7% | -0.1 | 75% | ❌ 42 pts to go |
| P06M | 14643 | 87.1% | 87.1% | -3.3 | n/a | no target |
| P06T | 36661 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 273 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 696 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22009 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 83.4% | 83.4% | -1.7 | 95% | ❌ 12 pts to go |
| P10 | 2390 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1455 | 5.4% | 5.4% | +4.6 | n/a | no target |
| P12 | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 93957 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 78.3% | 78.3% | -1.1 | n/a | no target |
| P01T | 192 | 0.5% | 0.5% | +0.2 | n/a | no target |
| P01_GOLD | 626 | 51.8% | 51.8% | +0.0 | 85% | ❌ 33 pts to go |
| P02 | 466 | 52.6% | 52.6% | -0.1 | 90% | ❌ 37 pts to go |
| P03 | 263 | 43.7% | 43.7% | -1.6 | 85% | ❌ 41 pts to go |
| P04 | 3723 | 23.8% | 23.8% | -2.2 | 90% | ❌ 66 pts to go |
| P05 | 422 | 43.4% | 43.4% | +0.5 | 75% | ❌ 32 pts to go |
| P06M | 14643 | 77.8% | 77.8% | -5.9 | n/a | no target |
| P06T | 36661 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 273 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 696 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22009 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 0.3% | 0.3% | +0.0 | 95% | ❌ 95 pts to go |
| P10 | 2390 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1455 | 4.5% | 4.5% | +3.8 | n/a | no target |
| P12 | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 93957 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 89.9% | 89.9% | +4.3 | n/a | no target |
| P01T | 192 | 94.3% | 94.3% | +2.1 | n/a | no target |
| P01_GOLD | 626 | 85.3% | 85.3% | -0.2 | 100% | ❌ 15 pts to go |
| P02 | 466 | 76.4% | 76.4% | +0.7 | 100% | ❌ 24 pts to go |
| P03 | 263 | 91.3% | 91.3% | -0.9 | n/a | no target |
| P04 | 3723 | 48.8% | 48.8% | -2.7 | 95% | ❌ 46 pts to go |
| P05 | 422 | 77.5% | 77.5% | -0.3 | 95% | ❌ 18 pts to go |
| P06M | 14643 | 98.9% | 98.9% | +0.6 | n/a | no target |
| P06T | 36661 | 90.6% | 90.6% | +6.9 | n/a | no target |
| P06 | 273 | 23.1% | 23.1% | -3.1 | n/a | no target |
| P07 | 696 | 13.8% | 13.8% | -5.3 | n/a | no target |
| P08 | 22009 | 7.1% | 7.1% | -3.9 | n/a | no target |
| P09 | 307 | 98.7% | 98.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10 | 2390 | 71.0% | 71.0% | -0.7 | n/a | no target |
| P11 | 1455 | 68.1% | 68.1% | +52.0 | n/a | no target |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 93957 | 99.7% | 99.7% | +99.7 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 89.9% | 89.9% | +4.3 | n/a | no target |
| P01T | 192 | 94.3% | 94.3% | +2.1 | n/a | no target |
| P01_GOLD | 626 | 88.5% | 88.5% | -0.2 | 100% | ❌ 12 pts to go |
| P02 | 466 | 77.5% | 77.7% | +0.7 | 100% | ❌ 22 pts to go |
| P03 | 263 | 92.0% | 92.0% | -1.0 | n/a | no target |
| P04 | 3723 | 51.9% | 51.9% | -3.2 | 95% | ❌ 43 pts to go |
| P05 | 422 | 89.6% | 89.6% | -0.6 | 70% | ✅ met |
| P06M | 14643 | 98.9% | 98.9% | +0.6 | n/a | no target |
| P06T | 36661 | 90.6% | 90.6% | +6.9 | n/a | no target |
| P06 | 273 | 23.1% | 23.1% | -3.1 | n/a | no target |
| P07 | 696 | 13.8% | 13.8% | -5.3 | n/a | no target |
| P08 | 22009 | 7.1% | 7.1% | -3.9 | n/a | no target |
| P09 | 307 | 98.7% | 98.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10 | 2390 | 71.0% | 71.0% | -0.7 | n/a | no target |
| P11 | 1455 | 68.2% | 68.2% | +52.1 | n/a | no target |
| P12 | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 93957 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 192 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 16.8% | 16.8% | +0.0 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 363 rows, 28.9% filled |
| P02 | 466 | 11.2% | 11.2% | +0.0 | n/a | no target · rows from a source that publishes bids: 290 rows, 17.9% filled |
| P03 | 263 | 12.9% | 12.9% | -0.4 | n/a | no target · rows from a source that publishes bids: 139 rows, 24.5% filled |
| P04 | 3723 | 1.5% | 1.5% | -0.1 | n/a | no target · rows from a source that publishes bids: 871 rows, 6.3% filled |
| P05 | 422 | 2.6% | 2.6% | -0.4 | n/a | no target · rows from a source that publishes bids: 50 rows, 22.0% filled |
| P06M | 14643 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 36661 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 273 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 696 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22009 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 307 | 4.2% | 4.2% | +1.2 | n/a | no target · rows from a source that publishes bids: 293 rows, 4.4% filled |
| P10 | 2390 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1455 | 0.9% | 0.9% | +0.8 | n/a | no target · rows from a source that publishes bids: 90 rows, 14.4% filled |
| P12 | 15 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 15 rows, 0.0% filled |
| P13 | 93957 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 192 | 0.0% | 97.9% | -0.3 | n/a | no target |
| P01_GOLD | 626 | 53.2% | 82.4% | +0.0 | 90% | ❌ 37 pts to go |
| P02 | 466 | 52.4% | 87.6% | -0.1 | 90% | ❌ 38 pts to go |
| P03 | 263 | 44.5% | 80.6% | -1.2 | 90% | ❌ 46 pts to go |
| P04 | 3723 | 19.1% | 93.9% | -1.8 | 90% | ❌ 71 pts to go |
| P05 | 422 | 0.0% | 83.4% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 14643 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 36661 | 0.0% | 99.8% | +0.0 | n/a | no target |
| P06 | 273 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 696 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 22009 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 307 | 2.3% | 3.9% | +0.0 | 90% | ❌ 88 pts to go |
| P10 | 2390 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1455 | 4.1% | 96.9% | +3.5 | n/a | no target |
| P12 | 15 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 93957 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 192 | 0.5% | 98.4% | -0.1 | n/a | no target |
| P01_GOLD | 626 | 25.9% | 55.1% | +0.0 | 90% | ❌ 64 pts to go |
| P02 | 466 | 51.5% | 86.7% | -0.1 | n/a | no target |
| P03 | 263 | 24.3% | 60.5% | -0.7 | n/a | no target |
| P04 | 3723 | 21.0% | 95.7% | -1.9 | n/a | no target |
| P05 | 422 | 0.5% | 83.9% | +0.0 | n/a | no target |
| P06M | 14643 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 36661 | 0.1% | 99.9% | +0.0 | n/a | no target |
| P06 | 273 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 696 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 22009 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 307 | 41.0% | 42.7% | -0.9 | n/a | no target |
| P10 | 2390 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1455 | 3.7% | 96.6% | +3.1 | n/a | no target |
| P12 | 15 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 93957 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 192 | 2.1% | 100.0% | +0.6 | n/a | no target |
| P01_GOLD | 626 | 51.8% | 81.0% | +0.0 | 95% | ❌ 43 pts to go |
| P02 | 466 | 56.4% | 91.6% | -0.2 | n/a | no target |
| P03 | 263 | 46.8% | 82.9% | -1.2 | n/a | no target |
| P04 | 3723 | 21.2% | 95.9% | -1.9 | n/a | no target |
| P05 | 422 | 4.5% | 87.9% | -0.2 | n/a | no target |
| P06M | 14643 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 36661 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 273 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 696 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 22009 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 307 | 62.5% | 64.2% | -1.5 | n/a | no target |
| P10 | 2390 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1455 | 4.1% | 97.0% | +3.5 | n/a | no target |
| P12 | 15 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 93957 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 192 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 466 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 263 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3723 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 422 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 14643 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 36661 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 273 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 696 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 22009 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 307 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2390 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1455 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 15 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 93957 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 192 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 466 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 263 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3723 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 422 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 14643 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 36661 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 273 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 696 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 22009 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 307 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2390 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1455 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 15 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 93957 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 129 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 192 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 466 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 263 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3723 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 422 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 14643 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 36661 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 273 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 696 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 22009 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 307 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2390 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1455 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 15 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 93957 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

