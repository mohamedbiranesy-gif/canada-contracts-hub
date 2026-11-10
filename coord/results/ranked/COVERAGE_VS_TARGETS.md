# Coverage vs the downstream team's targets — 2026-11-10

Benchmarks (field × package with a numeric target): **99 of 446 met** (22.2%); 64 within 10 points; 283 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 47, P01T 173, P01_GOLD 626, P02 403, P03 209, P04 1569, P05 365, P06M 4103, P06T 12949, P06 263, P07 501, P08 10340, P09 312, P10R 25497, P10 2406, P11 3187, P12 7, P13 10644

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 47 | 0.0% | 23.4% | 8 | PO rule (39 rows) |
| P01T | 173 | 0.6% | 26.0% | 7 | reference to quote (PO / contract / vendor id) (165 rows) |
| P01_GOLD | 626 | 24.3% | 71.1% | 10 | payment terms (215 rows) |
| P02 | 403 | 8.9% | 62.8% | 9 | PO rule (298 rows) |
| P03 | 209 | 17.7% | 69.9% | 9 | PO rule (92 rows) |
| P04 | 1569 | 2.9% | 38.4% | 8 | PO rule (1414 rows) |
| P05 | 365 | 1.4% | 19.2% | 7 | payment terms (297 rows) |
| P06M | 4103 | 0.0% | 1.1% | 8 | PO rule (4094 rows) |
| P06T | 12949 | 0.0% | 1.1% | 6 | reference to quote (PO / contract / vendor id) (12884 rows) |
| P06 | 263 | 0.0% | 7.2% | 6 | reference to quote (PO / contract / vendor id) (263 rows) |
| P07 | 501 | 0.0% | 2.8% | 5 | reference to quote (PO / contract / vendor id) (501 rows) |
| P08 | 10340 | 0.0% | 0.2% | 5 | reference to quote (PO / contract / vendor id) (10340 rows) |
| P09 | 312 | 1.3% | 43.6% | 8 | payment terms (291 rows) |
| P10R | 25497 | 0.0% | 0.0% | 6 | vendor GST/HST number (25497 rows) |
| P10 | 2406 | 0.0% | 1.0% | 5 | reference to quote (PO / contract / vendor id) (2403 rows) |
| P11 | 3187 | 0.2% | 1.8% | 6 | PO rule (3156 rows) |
| P12 | 7 | 0.0% | 57.1% | 9 | PO rule (7 rows) |
| P13 | 10644 | 0.0% | 0.0% | 6 | reference to quote (PO / contract / vendor id) (10644 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 47 | 6 | 1 | 40 | 0 | 0 | 73 |
| P01T | 173 | 28 | 44 | 101 | 0 | 0 | 73 |
| P01_GOLD | 626 | 231 | 186 | 209 | 0 | 0 | 82 |
| P02 | 403 | 0 | 183 | 220 | 0 | 0 | 66 |
| P03 | 209 | 0 | 0 | 202 | 7 | 0 | 58 |
| P04 | 1569 | 0 | 0 | 1519 | 50 | 0 | 53 |
| P05 | 365 | 14 | 28 | 307 | 16 | 0 | 51 |
| P06M | 4103 | 0 | 2 | 4092 | 9 | 0 | 51 |
| P06T | 12949 | 0 | 28 | 11382 | 1539 | 0 | 43 |
| P06 | 263 | 21 | 34 | 208 | 0 | 0 | 71 |
| P07 | 501 | 0 | 16 | 452 | 33 | 0 | 53 |
| P08 | 10340 | 0 | 0 | 7795 | 2545 | 0 | 43 |
| P09 | 312 | 4 | 12 | 293 | 3 | 0 | 53 |
| P10R | 25497 | 0 | 7 | 20688 | 4802 | 0 | 43 |
| P10 | 2406 | 3 | 14 | 1703 | 686 | 0 | 43 |
| P11 | 3187 | 0 | 0 | 0 | 0 | 3187 | 23 |
| P12 | 7 | 0 | 1 | 6 | 0 | 0 | 51 |
| P13 | 10644 | 2 | 8 | 9571 | 1063 | 0 | 51 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 47 | 34 | 72.3% | the buyer's PO / reference rule (8) |
| P01T | 173 | 59 | 34.1% | the buyer's PO / reference rule (63) |
| P01_GOLD | 626 | 464 | 74.1% | bill-to legal name and address (109) |
| P02 | 403 | 305 | 75.7% | the buyer's PO / reference rule (54) |
| P03 | 209 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (209) |
| P04 | 1569 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (1569) |
| P05 | 365 | 45 | 12.3% | a confirmed invoicing / AP or finance channel (283) |
| P06M | 4103 | 27 | 0.7% | a confirmed invoicing / AP or finance channel (4048) |
| P06T | 12949 | 24 | 0.2% | a confirmed invoicing / AP or finance channel (12640) |
| P06 | 263 | 33 | 12.5% | bill-to legal name and address (136) |
| P07 | 501 | 8 | 1.6% | bill-to legal name and address (216) |
| P08 | 10340 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (10340) |
| P09 | 312 | 41 | 13.1% | a confirmed invoicing / AP or finance channel (262) |
| P10R | 25497 | 271 | 1.1% | a confirmed invoicing / AP or finance channel (24928) |
| P10 | 2406 | 9 | 0.4% | a confirmed invoicing / AP or finance channel (2282) |
| P11 | 3187 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (3187) |
| P12 | 7 | 2 | 28.6% | a confirmed invoicing / AP or finance channel (5) |
| P13 | 10644 | 3 | 0.0% | a confirmed invoicing / AP or finance channel (10373) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 47 | 6 | 12.8% | 7 | 0 | the vendor's GST/HST number (BN9) (32) |
| P01T | 173 | 42 | 24.3% | 17 | 0 | the vendor's GST/HST number (BN9) (73) |
| P01_GOLD | 626 | 409 | 65.3% | 21 | 0 | the vendor's GST/HST number (BN9) (124) |
| P02 | 403 | 218 | 54.1% | 35 | 0 | the vendor's GST/HST number (BN9) (130) |
| P03 | 209 | 17 | 8.1% | 1 | 131 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (49) |
| P04 | 1569 | 43 | 2.7% | 10 | 706 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (772) |
| P05 | 365 | 22 | 6.0% | 9 | 89 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (186) |
| P06M | 4103 | 1 | 0.0% | 14 | 63 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (3975) |
| P06T | 12949 | 17 | 0.1% | 60 | 1885 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (10673) |
| P06 | 263 | 14 | 5.3% | 17 | 0 | the vendor's GST/HST number (BN9) (137) |
| P07 | 501 | 7 | 1.4% | 29 | 15 | the vendor's GST/HST number (BN9) (208) |
| P08 | 10340 | 1 | 0.0% | 3 | 693 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (9614) |
| P09 | 312 | 39 | 12.5% | 1 | 125 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (128) |
| P10R | 25497 | 451 | 1.8% | 0 | 17170 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (7702) |
| P10 | 2406 | 6 | 0.2% | 20 | 362 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (1898) |
| P11 | 3187 | 5 | 0.2% | 0 | 0 | a confirmed invoicing / AP or finance channel (3171) |
| P12 | 7 | 2 | 28.6% | 0 | 3 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2) |
| P13 | 10644 | 3 | 0.0% | 206 | 7210 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (3124) |
| **all** | 73601 | 1303 | 1.8% | 450 | 28452 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 41 | 0 | 0 | 0 | 1 | 5 | 0 | 39 | 40 | 1 |
| P01T | 145 | 0 | 0 | 0 | 8 | 38 | 8 | 100 | 113 | 30 |
| P01_GOLD | 395 | 0 | 0 | 0 | 11 | 94 | 34 | 193 | 228 | 60 |
| P02 | 403 | 0 | 403 | 0 | 4 | 38 | 8 | 298 | 227 | 22 |
| P03 | 209 | 0 | 209 | 0 | 2 | 34 | 11 | 92 | 94 | 25 |
| P04 | 1569 | 0 | 1569 | 0 | 12 | 326 | 93 | 1414 | 1209 | 106 |
| P05 | 351 | 0 | 303 | 0 | 7 | 88 | 42 | 287 | 299 | 52 |
| P06M | 4103 | 0 | 4103 | 0 | 78 | 327 | 36 | 4094 | 4083 | 3 |
| P06T | 12949 | 0 | 12949 | 0 | 1819 | 6859 | 2034 | 12828 | 12611 | 137 |
| P06 | 242 | 0 | 0 | 0 | 32 | 123 | 61 | 175 | 212 | 7 |
| P07 | 501 | 0 | 501 | 0 | 127 | 277 | 107 | 445 | 458 | 16 |
| P08 | 10340 | 0 | 10340 | 0 | 3658 | 6956 | 2860 | 10270 | 10189 | 159 |
| P09 | 308 | 0 | 288 | 0 | 9 | 69 | 4 | 282 | 294 | 45 |
| P10R | 25497 | 0 | 25418 | 0 | 432 | 15128 | 6320 | 25471 | 25424 | 23 |
| P10 | 2403 | 0 | 2354 | 0 | 203 | 1615 | 846 | 2357 | 2316 | 108 |
| P11 | 3187 | 3187 | 3137 | 0 | 1837 | 3038 | 808 | 3156 | 3125 | 32 |
| P12 | 7 | 0 | 6 | 0 | 0 | 2 | 0 | 7 | 6 | 0 |
| P13 | 10642 | 0 | 10551 | 0 | 311 | 3186 | 1532 | 10614 | 10622 | 25 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| vendor_registered_address | P08 | 14.7% | 70% | 5715 |
| buyer_ap_cycle_published | P10R | 0.0% | 20% | 5096 |
| vendor_logo_url | P08 | 51.4% | 100% | 5022 |
| ap_system_hint | P10R | 0.4% | 20% | 4994 |
| vendor_phone | P08 | 37.9% | 85% | 4865 |
| buyer_phone | P08 | 50.7% | 95% | 4577 |
| buyer_logo_url | P08 | 56.5% | 100% | 4496 |
| buyer_legal_name_as_published | P08 | 32.7% | 75% | 4371 |
| vendor_emails | P08 | 36.8% | 75% | 3946 |
| vendor_bn9 | P08 | 12.4% | 50% | 3892 |
| buyer_tax_exempt_status | P10R | 0.1% | 15% | 3809 |
| buyer_esignature_preference | P10R | 0.1% | 15% | 3808 |
| buyer_payment_method_preference | P10R | 0.6% | 15% | 3682 |
| vendor_trading_name | P08 | 21.7% | 50% | 2931 |
| buyer_ap_cycle_published | P06T | 0.1% | 20% | 2583 |
| invoice_reference_hint | P08 | 0.7% | 25% | 2515 |
| ap_system_hint | P06T | 1.5% | 20% | 2397 |
| buyer_address | P08 | 72.3% | 95% | 2349 |
| buyer_logo_url | P11 | 10.8% | 80% | 2205 |
| buyer_phone | P11 | 8.2% | 75% | 2131 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 2127 |
| buyer_phone | P13 | 75.1% | 95% | 2115 |
| buyer_bn_as_published | P08 | 15.0% | 35% | 2072 |
| buyer_logo_url | P13 | 75.6% | 95% | 2066 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 2063 |
| ap_system_hint | P13 | 0.9% | 20% | 2035 |
| vendor_phone | P11 | 11.8% | 75% | 2016 |
| ap_system_hint | P08 | 0.8% | 20% | 1985 |
| buyer_legal_name_as_published | P11 | 4.7% | 65% | 1923 |
| vendor_emails | P11 | 10.0% | 70% | 1913 |
| buyer_esignature_preference | P06T | 0.3% | 15% | 1904 |
| buyer_tax_exempt_status | P06T | 0.6% | 15% | 1869 |
| buyer_payment_method_preference | P06T | 0.7% | 15% | 1856 |
| contract_value | P11 | 2.7% | 60% | 1826 |
| award_or_notice_id | P11 | 2.8% | 60% | 1824 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 1589 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 1587 |
| buyer_payment_method_preference | P13 | 0.5% | 15% | 1546 |
| commodity_codes | P11 | 1.9% | 50% | 1533 |
| buyer_esignature_preference | P08 | 0.3% | 15% | 1525 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 78.7% | 78.7% | +34.3 | 50% | ✅ met |
| P01T | 173 | 44.5% | 44.5% | -27.2 | 50% | 🟡 6 pts to go |
| P01_GOLD | 626 | 92.3% | 94.6% | -0.2 | 95% | 🟡 3 pts to go |
| P02 | 403 | 83.9% | 85.6% | +0.0 | 95% | ❌ 11 pts to go |
| P03 | 209 | 92.3% | 95.7% | -0.5 | 95% | 🟡 3 pts to go |
| P04 | 1569 | 68.8% | 71.4% | +0.2 | 90% | ❌ 21 pts to go |
| P05 | 365 | 41.9% | 44.9% | +0.8 | 70% | ❌ 28 pts to go |
| P06M | 4103 | 94.9% | 94.9% | +87.8 | n/a | no target |
| P06T | 12949 | 1.4% | 1.5% | -3.0 | n/a | no target |
| P06 | 263 | 33.5% | 33.5% | -14.7 | 30% | ✅ met |
| P07 | 501 | 11.2% | 11.2% | -12.6 | 30% | ❌ 19 pts to go |
| P08 | 10340 | 0.7% | 0.7% | -1.7 | 25% | ❌ 24 pts to go |
| P09 | 312 | 99.0% | 99.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10R | 25497 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2406 | 2.2% | 2.9% | +0.0 | 25% | ❌ 23 pts to go |
| P11 | 3187 | 20.5% | 20.9% | -3.6 | 60% | ❌ 40 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 10644 | 0.3% | 0.3% | +0.1 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 173 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 626 | 6.2% | 6.2% | +0.0 | 50% | ❌ 44 pts to go |
| P02 | 403 | 7.2% | 7.2% | +0.0 | 50% | ❌ 43 pts to go |
| P03 | 209 | 1.9% | 1.9% | +0.0 | 40% | ❌ 38 pts to go |
| P04 | 1569 | 1.1% | 1.1% | +0.0 | 30% | ❌ 29 pts to go |
| P05 | 365 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 4103 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 12949 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 263 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 501 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 10340 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 312 | 0.6% | 0.6% | +0.1 | 50% | ❌ 49 pts to go |
| P10R | 25497 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2406 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P11 | 3187 | 0.1% | 0.1% | -0.7 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 10644 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 63.8% | 63.8% | +63.8 | n/a | no target |
| P01T | 173 | 4.6% | 4.6% | -0.8 | 50% | ❌ 45 pts to go |
| P01_GOLD | 626 | 67.6% | 67.6% | +0.0 | 85% | ❌ 17 pts to go |
| P02 | 403 | 75.4% | 75.4% | -0.1 | 90% | ❌ 15 pts to go |
| P03 | 209 | 75.1% | 75.1% | -0.4 | 85% | 🟡 10 pts to go |
| P04 | 1569 | 65.6% | 65.6% | +0.1 | 85% | ❌ 19 pts to go |
| P05 | 365 | 32.3% | 32.3% | +1.3 | 60% | ❌ 28 pts to go |
| P06M | 4103 | 94.7% | 94.7% | +94.7 | n/a | no target |
| P06T | 12949 | 0.5% | 0.5% | +0.3 | n/a | no target |
| P06 | 263 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 501 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 10340 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 312 | 96.2% | 96.2% | -0.4 | 100% | 🟡 4 pts to go |
| P10R | 25497 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2406 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3187 | 19.9% | 19.9% | -0.1 | 60% | ❌ 40 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 10644 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 173 | 2.3% | 2.3% | +0.1 | 30% | ❌ 28 pts to go |
| P01_GOLD | 626 | 51.3% | 51.3% | +0.0 | 80% | ❌ 29 pts to go |
| P02 | 403 | 66.7% | 66.7% | -0.1 | 60% | ✅ met |
| P03 | 209 | 63.6% | 63.6% | -0.3 | 80% | ❌ 16 pts to go |
| P04 | 1569 | 54.6% | 54.6% | +0.1 | 50% | ✅ met |
| P05 | 365 | 14.0% | 14.0% | +0.7 | 40% | ❌ 26 pts to go |
| P06M | 4103 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 12949 | 0.5% | 0.5% | +0.3 | n/a | no target |
| P06 | 263 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 501 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 10340 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 312 | 84.0% | 84.0% | -2.1 | 50% | ✅ met |
| P10R | 25497 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2406 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3187 | 2.6% | 2.6% | -14.9 | 40% | ❌ 37 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 10644 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 173 | 3.5% | 3.5% | +0.2 | n/a | no target |
| P01_GOLD | 626 | 61.0% | 61.0% | -0.1 | 85% | ❌ 24 pts to go |
| P02 | 403 | 65.8% | 65.8% | +0.0 | 90% | ❌ 24 pts to go |
| P03 | 209 | 74.2% | 74.2% | -0.3 | 85% | ❌ 11 pts to go |
| P04 | 1569 | 56.5% | 56.5% | +0.2 | 85% | ❌ 28 pts to go |
| P05 | 365 | 21.9% | 21.9% | +0.8 | 50% | ❌ 28 pts to go |
| P06M | 4103 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 12949 | 0.5% | 0.5% | +0.3 | n/a | no target |
| P06 | 263 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 501 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 10340 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 312 | 97.1% | 97.1% | +0.0 | 100% | 🟡 3 pts to go |
| P10R | 25497 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2406 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3187 | 2.8% | 2.8% | -16.2 | 60% | ❌ 57 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 10644 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 173 | 1.2% | 1.2% | -1.0 | n/a | no target |
| P01_GOLD | 626 | 12.9% | 12.9% | -0.1 | 60% | ❌ 47 pts to go |
| P02 | 403 | 7.2% | 7.2% | +0.0 | 50% | ❌ 43 pts to go |
| P03 | 209 | 10.5% | 10.5% | -0.1 | 50% | ❌ 40 pts to go |
| P04 | 1569 | 4.3% | 4.3% | +0.0 | 40% | ❌ 36 pts to go |
| P05 | 365 | 1.4% | 1.4% | +0.1 | 20% | ❌ 19 pts to go |
| P06M | 4103 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 12949 | 0.0% | 0.0% | -0.1 | n/a | no target |
| P06 | 263 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 501 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 10340 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 312 | 2.6% | 2.6% | +0.0 | 50% | ❌ 47 pts to go |
| P10R | 25497 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2406 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3187 | 0.4% | 0.4% | -2.6 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 10644 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 173 | 1.7% | 1.7% | +1.7 | n/a | no target |
| P01_GOLD | 626 | 35.0% | 35.0% | -0.1 | 80% | ❌ 45 pts to go |
| P02 | 403 | 60.8% | 60.8% | +0.2 | 90% | ❌ 29 pts to go |
| P03 | 209 | 41.1% | 41.1% | -0.2 | 80% | ❌ 39 pts to go |
| P04 | 1569 | 51.4% | 51.4% | +0.1 | 85% | ❌ 34 pts to go |
| P05 | 365 | 6.3% | 6.3% | +0.3 | 50% | ❌ 44 pts to go |
| P06M | 4103 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 12949 | 0.4% | 0.4% | +0.4 | n/a | no target |
| P06 | 263 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 501 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 10340 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 312 | 75.6% | 75.6% | -0.3 | 95% | ❌ 19 pts to go |
| P10R | 25497 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2406 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3187 | 1.9% | 1.9% | -11.2 | 50% | ❌ 48 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 10644 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 173 | 0.6% | 0.6% | -0.5 | n/a | no target |
| P01_GOLD | 626 | 8.5% | 8.5% | +0.0 | 50% | ❌ 42 pts to go |
| P02 | 403 | 7.2% | 7.2% | +0.0 | 50% | ❌ 43 pts to go |
| P03 | 209 | 2.4% | 2.4% | +0.0 | 30% | ❌ 28 pts to go |
| P04 | 1569 | 1.1% | 1.1% | +0.0 | 30% | ❌ 29 pts to go |
| P05 | 365 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 4103 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 12949 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 263 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 501 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 10340 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 312 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P10R | 25497 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2406 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3187 | 0.1% | 0.1% | -0.7 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 10644 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 173 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 403 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 209 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 1569 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 365 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 4103 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 12949 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 263 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 501 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 10340 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 312 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 25497 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2406 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 3187 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 10644 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 31.9% | 31.9% | -68.1 | 70% | ❌ 38 pts to go |
| P01T | 173 | 45.1% | 45.1% | -35.3 | 60% | ❌ 15 pts to go |
| P01_GOLD | 626 | 77.8% | 77.8% | -0.1 | 90% | ❌ 12 pts to go |
| P02 | 403 | 67.2% | 67.2% | -0.1 | 85% | ❌ 18 pts to go |
| P03 | 209 | 82.3% | 82.3% | +0.1 | 90% | 🟡 8 pts to go |
| P04 | 1569 | 55.3% | 55.3% | -0.1 | 75% | ❌ 20 pts to go |
| P05 | 365 | 53.4% | 53.4% | +0.8 | 50% | ✅ met |
| P06M | 4103 | 2.4% | 2.4% | -72.0 | n/a | no target |
| P06T | 12949 | 18.5% | 18.5% | -42.2 | n/a | no target |
| P06 | 263 | 24.0% | 24.0% | -20.0 | 40% | ❌ 16 pts to go |
| P07 | 501 | 19.0% | 19.0% | -19.1 | 50% | ❌ 31 pts to go |
| P08 | 10340 | 12.4% | 12.4% | -27.8 | 50% | ❌ 38 pts to go |
| P09 | 312 | 57.7% | 57.7% | +3.4 | 80% | ❌ 22 pts to go |
| P10R | 25497 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2406 | 32.0% | 32.0% | -4.6 | 40% | 🟡 8 pts to go |
| P11 | 3187 | 79.5% | 79.5% | +34.8 | 60% | ✅ met |
| P12 | 7 | 71.4% | 71.4% | +18.8 | 85% | ❌ 14 pts to go |
| P13 | 10644 | 88.9% | 88.9% | -2.8 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 66.0% | 66.0% | +4.9 | n/a | no target |
| P01T | 173 | 42.8% | 42.8% | -20.2 | n/a | no target |
| P01_GOLD | 626 | 74.9% | 74.9% | +0.1 | 95% | ❌ 20 pts to go |
| P02 | 403 | 84.9% | 84.9% | +0.0 | 95% | ❌ 10 pts to go |
| P03 | 209 | 78.0% | 78.0% | +0.1 | 95% | ❌ 17 pts to go |
| P04 | 1569 | 80.6% | 80.6% | -0.1 | 95% | ❌ 14 pts to go |
| P05 | 365 | 56.4% | 56.4% | +0.2 | 70% | ❌ 14 pts to go |
| P06M | 4103 | 55.2% | 55.2% | +34.4 | n/a | no target |
| P06T | 12949 | 39.2% | 39.2% | -39.0 | n/a | no target |
| P06 | 263 | 30.0% | 30.0% | -25.4 | 80% | ❌ 50 pts to go |
| P07 | 501 | 24.8% | 24.8% | -27.2 | 70% | ❌ 45 pts to go |
| P08 | 10340 | 14.7% | 14.7% | -37.7 | 70% | ❌ 55 pts to go |
| P09 | 312 | 87.8% | 87.8% | -0.7 | 100% | ❌ 12 pts to go |
| P10R | 25497 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2406 | 35.9% | 35.9% | -6.5 | 70% | ❌ 34 pts to go |
| P11 | 3187 | 65.3% | 65.3% | +10.0 | 75% | 🟡 10 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 10644 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 21.3% | 21.3% | -28.7 | n/a | no target |
| P01T | 173 | 24.3% | 24.3% | +4.7 | n/a | no target |
| P01_GOLD | 626 | 52.4% | 52.4% | +0.0 | 60% | 🟡 8 pts to go |
| P02 | 403 | 67.2% | 67.2% | -0.1 | 60% | ✅ met |
| P03 | 209 | 64.6% | 64.6% | -0.3 | 60% | ✅ met |
| P04 | 1569 | 55.5% | 55.5% | +0.0 | 55% | ✅ met |
| P05 | 365 | 24.7% | 24.7% | -0.6 | 50% | ❌ 25 pts to go |
| P06M | 4103 | 1.3% | 1.3% | -16.0 | n/a | no target |
| P06T | 12949 | 36.6% | 36.6% | -17.0 | n/a | no target |
| P06 | 263 | 33.8% | 33.8% | -19.2 | n/a | no target |
| P07 | 501 | 28.7% | 28.7% | -17.3 | 55% | ❌ 26 pts to go |
| P08 | 10340 | 21.7% | 21.7% | -25.8 | 50% | ❌ 28 pts to go |
| P09 | 312 | 71.8% | 71.8% | +0.4 | 70% | ✅ met |
| P10R | 25497 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2406 | 47.4% | 47.4% | -4.5 | 55% | 🟡 8 pts to go |
| P11 | 3187 | 64.3% | 64.3% | +21.3 | 50% | ✅ met |
| P12 | 7 | 85.7% | 85.7% | +1.5 | n/a | no target |
| P13 | 10644 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 25.5% | 25.5% | -35.6 | n/a | no target |
| P01T | 173 | 37.6% | 37.6% | +7.2 | n/a | no target |
| P01_GOLD | 626 | 51.8% | 51.8% | +0.0 | 70% | ❌ 18 pts to go |
| P02 | 403 | 57.1% | 57.1% | -0.1 | 70% | ❌ 13 pts to go |
| P03 | 209 | 57.4% | 57.4% | +0.2 | 70% | ❌ 13 pts to go |
| P04 | 1569 | 51.9% | 51.9% | -0.1 | 65% | ❌ 13 pts to go |
| P05 | 365 | 33.2% | 33.2% | -1.4 | 60% | ❌ 27 pts to go |
| P06M | 4103 | 1.8% | 1.8% | -28.6 | n/a | no target |
| P06T | 12949 | 23.8% | 23.8% | +20.3 | n/a | no target |
| P06 | 263 | 46.8% | 46.8% | -12.8 | 40% | ✅ met |
| P07 | 501 | 47.7% | 47.7% | -20.2 | 85% | ❌ 37 pts to go |
| P08 | 10340 | 37.9% | 37.9% | -30.2 | 85% | ❌ 47 pts to go |
| P09 | 312 | 52.9% | 52.9% | -2.5 | 85% | ❌ 32 pts to go |
| P10R | 25497 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2406 | 61.1% | 61.1% | -5.2 | 85% | ❌ 24 pts to go |
| P11 | 3187 | 11.8% | 11.8% | -43.1 | 75% | ❌ 63 pts to go |
| P12 | 7 | 14.3% | 14.3% | -1.5 | n/a | no target |
| P13 | 10644 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 34.0% | 34.0% | -60.4 | n/a | no target |
| P01T | 173 | 94.8% | 94.8% | +4.6 | n/a | no target |
| P01_GOLD | 626 | 89.5% | 89.5% | +0.1 | 90% | 🟡 0 pts to go |
| P02 | 403 | 87.8% | 87.8% | +0.2 | 90% | 🟡 2 pts to go |
| P03 | 209 | 90.0% | 90.0% | +0.1 | 90% | ✅ met |
| P04 | 1569 | 81.1% | 81.1% | -0.2 | 85% | 🟡 4 pts to go |
| P05 | 365 | 50.4% | 50.4% | -0.6 | 70% | ❌ 20 pts to go |
| P06M | 4103 | 4.1% | 4.1% | -63.8 | n/a | no target |
| P06T | 12949 | 94.1% | 94.1% | +16.2 | n/a | no target |
| P06 | 263 | 98.1% | 98.1% | +1.1 | 50% | ✅ met |
| P07 | 501 | 98.8% | 98.8% | +2.0 | 100% | 🟡 1 pts to go |
| P08 | 10340 | 99.0% | 99.0% | +2.9 | 100% | 🟡 1 pts to go |
| P09 | 312 | 79.8% | 79.8% | +0.0 | 100% | ❌ 20 pts to go |
| P10R | 25497 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2406 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 3187 | 99.0% | 99.0% | +6.0 | 100% | 🟡 1 pts to go |
| P12 | 7 | 28.6% | 28.6% | -13.5 | n/a | no target |
| P13 | 10644 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 21.3% | 21.3% | -28.7 | n/a | no target |
| P01T | 173 | 44.5% | 44.5% | -1.2 | n/a | no target |
| P01_GOLD | 626 | 45.7% | 45.7% | +0.0 | 70% | ❌ 24 pts to go |
| P02 | 403 | 51.6% | 51.6% | +0.1 | 75% | ❌ 23 pts to go |
| P03 | 209 | 51.7% | 51.7% | +0.3 | 75% | ❌ 23 pts to go |
| P04 | 1569 | 42.8% | 42.8% | -0.1 | 70% | ❌ 27 pts to go |
| P05 | 365 | 24.4% | 24.4% | -0.1 | 55% | ❌ 31 pts to go |
| P06M | 4103 | 1.1% | 1.1% | -15.0 | n/a | no target |
| P06T | 12949 | 19.2% | 19.2% | +16.3 | n/a | no target |
| P06 | 263 | 35.7% | 35.7% | -5.3 | n/a | no target |
| P07 | 501 | 35.1% | 35.1% | -1.8 | 70% | ❌ 35 pts to go |
| P08 | 10340 | 36.8% | 36.8% | -11.9 | 75% | ❌ 38 pts to go |
| P09 | 312 | 50.0% | 50.0% | -2.0 | 85% | ❌ 35 pts to go |
| P10R | 25497 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2406 | 46.2% | 46.2% | -5.1 | 80% | ❌ 34 pts to go |
| P11 | 3187 | 10.0% | 10.0% | -30.5 | 70% | ❌ 60 pts to go |
| P12 | 7 | 28.6% | 28.6% | -3.0 | n/a | no target |
| P13 | 10644 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 31.9% | 31.9% | -62.5 | n/a | no target |
| P01T | 173 | 76.9% | 76.9% | -12.2 | n/a | no target |
| P01_GOLD | 626 | 79.9% | 79.9% | +0.1 | 90% | ❌ 10 pts to go |
| P02 | 403 | 77.4% | 77.4% | +0.2 | 90% | ❌ 13 pts to go |
| P03 | 209 | 81.8% | 81.8% | +0.1 | 90% | 🟡 8 pts to go |
| P04 | 1569 | 70.7% | 70.7% | -0.2 | 85% | ❌ 14 pts to go |
| P05 | 365 | 47.7% | 47.7% | -0.7 | 75% | ❌ 27 pts to go |
| P06M | 4103 | 3.2% | 3.2% | -64.7 | n/a | no target |
| P06T | 12949 | 47.7% | 47.7% | -29.4 | n/a | no target |
| P06 | 263 | 66.9% | 66.9% | -21.7 | n/a | no target |
| P07 | 501 | 63.3% | 63.3% | -27.2 | 100% | ❌ 37 pts to go |
| P08 | 10340 | 51.4% | 51.4% | -37.6 | 100% | ❌ 49 pts to go |
| P09 | 312 | 61.2% | 61.2% | -1.3 | n/a | no target |
| P10R | 25497 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2406 | 81.8% | 81.8% | -7.2 | 100% | ❌ 18 pts to go |
| P11 | 3187 | 71.7% | 71.7% | -2.8 | n/a | no target |
| P12 | 7 | 28.6% | 28.6% | -8.2 | n/a | no target |
| P13 | 10644 | 75.2% | 75.2% | -7.5 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 36.2% | 36.2% | +36.2 | n/a | no target · QC vendors: 17 rows, 100.0% filled |
| P01T | 173 | 20.2% | 20.2% | -1.5 | n/a | no target · QC vendors: 5 rows, 100.0% filled |
| P01_GOLD | 626 | 48.1% | 48.1% | +0.2 | 95% | ❌ 47 pts to go · QC vendors: 52 rows, 98.1% filled |
| P02 | 403 | 68.5% | 68.5% | -0.1 | 95% | ❌ 26 pts to go · QC vendors: 107 rows, 100.0% filled |
| P03 | 209 | 55.5% | 55.5% | -0.3 | 95% | ❌ 40 pts to go · QC vendors: 17 rows, 100.0% filled |
| P04 | 1569 | 60.1% | 60.1% | -0.1 | 95% | ❌ 35 pts to go · QC vendors: 435 rows, 98.6% filled |
| P05 | 365 | 15.1% | 15.1% | +0.3 | n/a | no target · QC vendors: 29 rows, 93.1% filled |
| P06M | 4103 | 53.4% | 53.4% | +53.4 | n/a | no target · QC vendors: 2192 rows, 100.0% filled |
| P06T | 12949 | 33.1% | 33.1% | -22.8 | n/a | no target · QC vendors: 1988 rows, 100.0% filled |
| P06 | 263 | 15.2% | 15.2% | -11.3 | n/a | no target · QC vendors: 18 rows, 100.0% filled |
| P07 | 501 | 10.6% | 10.6% | -10.8 | n/a | no target · QC vendors: 29 rows, 96.6% filled |
| P08 | 10340 | 8.4% | 8.4% | -20.5 | n/a | no target · QC vendors: 567 rows, 99.1% filled |
| P09 | 312 | 78.8% | 78.8% | -1.3 | 95% | ❌ 16 pts to go · QC vendors: 116 rows, 100.0% filled |
| P10R | 25497 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2406 | 19.5% | 19.5% | -3.9 | n/a | no target · QC vendors: 354 rows, 97.2% filled |
| P11 | 3187 | 61.3% | 61.3% | +32.0 | n/a | no target · QC vendors: 105 rows, 99.0% filled |
| P12 | 7 | 57.1% | 57.1% | -16.6 | n/a | no target · QC vendors: 1 rows, 100.0% filled |
| P13 | 10644 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 59.6% | 59.6% | -1.5 | n/a | no target · vendors with a registry record: 28 rows, 100.0% filled |
| P01T | 173 | 42.8% | 42.8% | -20.2 | n/a | no target · vendors with a registry record: 74 rows, 100.0% filled |
| P01_GOLD | 626 | 83.4% | 83.4% | -0.1 | 100% | ❌ 17 pts to go · vendors with a registry record: 522 rows, 100.0% filled |
| P02 | 403 | 89.1% | 89.1% | +0.0 | 100% | ❌ 11 pts to go · vendors with a registry record: 359 rows, 100.0% filled |
| P03 | 209 | 89.0% | 89.0% | +0.1 | 100% | ❌ 11 pts to go · vendors with a registry record: 186 rows, 100.0% filled |
| P04 | 1569 | 81.3% | 81.3% | -0.1 | 100% | ❌ 19 pts to go · vendors with a registry record: 1275 rows, 100.0% filled |
| P05 | 365 | 62.2% | 62.2% | +0.5 | n/a | no target · vendors with a registry record: 227 rows, 100.0% filled |
| P06M | 4103 | 54.2% | 54.2% | +33.4 | n/a | no target · vendors with a registry record: 2222 rows, 100.0% filled |
| P06T | 12949 | 39.2% | 39.2% | -39.0 | n/a | no target · vendors with a registry record: 5080 rows, 100.0% filled |
| P06 | 263 | 30.8% | 30.8% | -27.0 | n/a | no target · vendors with a registry record: 81 rows, 100.0% filled |
| P07 | 501 | 25.3% | 25.3% | -29.1 | n/a | no target · vendors with a registry record: 127 rows, 100.0% filled |
| P08 | 10340 | 15.0% | 15.0% | -39.3 | n/a | no target · vendors with a registry record: 1556 rows, 100.0% filled |
| P09 | 312 | 91.3% | 91.3% | -0.3 | n/a | no target · vendors with a registry record: 285 rows, 100.0% filled |
| P10R | 25497 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2406 | 36.9% | 36.9% | -6.8 | n/a | no target · vendors with a registry record: 888 rows, 100.0% filled |
| P11 | 3187 | 65.6% | 65.6% | +7.4 | n/a | no target · vendors with a registry record: 2092 rows, 100.0% filled |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 7 rows, 100.0% filled |
| P13 | 10644 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 89.4% | 89.4% | -5.0 | 90% | 🟡 1 pts to go |
| P01T | 173 | 78.0% | 78.0% | -16.6 | 90% | ❌ 12 pts to go |
| P01_GOLD | 626 | 85.0% | 85.0% | +0.4 | 95% | 🟡 10 pts to go |
| P02 | 403 | 90.6% | 90.6% | +0.0 | 95% | 🟡 4 pts to go |
| P03 | 209 | 83.7% | 83.7% | +0.5 | 85% | 🟡 1 pts to go |
| P04 | 1569 | 79.2% | 79.2% | +0.4 | 90% | ❌ 11 pts to go |
| P05 | 365 | 75.9% | 75.9% | +0.1 | 75% | ✅ met |
| P06M | 4103 | 92.0% | 92.0% | +3.3 | n/a | no target |
| P06T | 12949 | 47.0% | 47.0% | -17.4 | n/a | no target |
| P06 | 263 | 53.2% | 53.2% | -3.4 | 80% | ❌ 27 pts to go |
| P07 | 501 | 44.7% | 44.7% | -8.9 | 80% | ❌ 35 pts to go |
| P08 | 10340 | 32.7% | 32.7% | -4.1 | 75% | ❌ 42 pts to go |
| P09 | 312 | 77.9% | 77.9% | -2.9 | 95% | ❌ 17 pts to go |
| P10R | 25497 | 40.7% | 40.7% |  | n/a | no target |
| P10 | 2406 | 32.9% | 32.9% | +0.9 | 70% | ❌ 37 pts to go |
| P11 | 3187 | 4.7% | 4.7% | -20.2 | 65% | ❌ 60 pts to go |
| P12 | 7 | 71.4% | 71.4% | -2.3 | 80% | 🟡 9 pts to go |
| P13 | 10644 | 70.1% | 70.1% | +17.6 | 60% | ✅ met |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 25.5% | 25.5% | -13.4 | 50% | ❌ 24 pts to go |
| P01T | 173 | 16.8% | 16.8% | -3.9 | n/a | no target |
| P01_GOLD | 626 | 20.6% | 20.6% | +0.2 | 40% | ❌ 19 pts to go |
| P02 | 403 | 21.6% | 21.6% | -0.2 | 40% | ❌ 18 pts to go |
| P03 | 209 | 26.8% | 26.8% | -0.1 | 40% | ❌ 13 pts to go |
| P04 | 1569 | 27.7% | 27.7% | +0.1 | 40% | ❌ 12 pts to go |
| P05 | 365 | 23.0% | 23.0% | +0.1 | 25% | 🟡 2 pts to go |
| P06M | 4103 | 13.6% | 13.6% | -12.0 | n/a | no target |
| P06T | 12949 | 21.9% | 21.9% | -9.0 | n/a | no target |
| P06 | 263 | 14.4% | 14.4% | +3.6 | 35% | ❌ 21 pts to go |
| P07 | 501 | 12.2% | 12.2% | +1.9 | 35% | ❌ 23 pts to go |
| P08 | 10340 | 15.0% | 15.0% | +3.9 | 35% | ❌ 20 pts to go |
| P09 | 312 | 16.3% | 16.3% | -0.8 | n/a | no target |
| P10R | 25497 | 18.6% | 18.6% |  | n/a | no target |
| P10 | 2406 | 9.9% | 9.9% | +0.3 | 30% | ❌ 20 pts to go |
| P11 | 3187 | 1.3% | 1.3% | -7.1 | n/a | no target |
| P12 | 7 | 14.3% | 14.3% | +3.8 | n/a | no target |
| P13 | 10644 | 40.8% | 40.8% | +14.9 | 30% | ✅ met |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 100.0% | 100.0% | +5.6 | 100% | ✅ met |
| P01T | 173 | 95.4% | 95.4% | +1.9 | 100% | 🟡 5 pts to go |
| P01_GOLD | 626 | 90.3% | 90.3% | +2.6 | 100% | 🟡 10 pts to go |
| P02 | 403 | 97.5% | 97.5% | +0.7 | 100% | 🟡 2 pts to go |
| P03 | 209 | 92.8% | 92.8% | +1.0 | 100% | 🟡 7 pts to go |
| P04 | 1569 | 93.0% | 93.0% | +2.0 | 100% | 🟡 7 pts to go |
| P05 | 365 | 87.4% | 87.4% | +2.5 | 100% | ❌ 13 pts to go |
| P06M | 4103 | 99.1% | 99.1% | +27.1 | n/a | no target |
| P06T | 12949 | 84.1% | 84.1% | +3.9 | n/a | no target |
| P06 | 263 | 73.8% | 73.8% | +5.1 | 95% | ❌ 21 pts to go |
| P07 | 501 | 78.2% | 78.2% | +7.6 | 95% | ❌ 17 pts to go |
| P08 | 10340 | 72.3% | 72.3% | +6.1 | 95% | ❌ 23 pts to go |
| P09 | 312 | 95.5% | 95.5% | +0.0 | 100% | 🟡 4 pts to go |
| P10R | 25497 | 75.2% | 75.2% |  | n/a | no target |
| P10 | 2406 | 64.7% | 64.7% | -0.5 | 95% | ❌ 30 pts to go |
| P11 | 3187 | 66.6% | 66.6% | +32.2 | 80% | ❌ 13 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 10644 | 85.5% | 85.5% | +9.4 | 95% | 🟡 10 pts to go |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 91.5% | 91.5% | +2.6 | n/a | no target |
| P01T | 173 | 77.5% | 77.5% | -2.9 | n/a | no target |
| P01_GOLD | 626 | 70.4% | 70.4% | +0.2 | 90% | ❌ 20 pts to go |
| P02 | 403 | 79.7% | 79.7% | +0.0 | 95% | ❌ 15 pts to go |
| P03 | 209 | 73.2% | 73.2% | -0.4 | 95% | ❌ 22 pts to go |
| P04 | 1569 | 84.7% | 84.7% | -0.2 | 95% | ❌ 10 pts to go |
| P05 | 365 | 74.8% | 74.8% | -0.2 | 90% | ❌ 15 pts to go |
| P06M | 4103 | 95.6% | 95.6% | +11.7 | n/a | no target |
| P06T | 12949 | 70.6% | 70.6% | -6.7 | n/a | no target |
| P06 | 263 | 54.8% | 54.8% | -9.7 | 95% | ❌ 40 pts to go |
| P07 | 501 | 52.1% | 52.1% | -14.2 | 90% | ❌ 38 pts to go |
| P08 | 10340 | 50.7% | 50.7% | -24.0 | 95% | ❌ 44 pts to go |
| P09 | 312 | 86.9% | 86.9% | -2.1 | 100% | ❌ 13 pts to go |
| P10R | 25497 | 76.0% | 76.0% |  | n/a | no target |
| P10 | 2406 | 63.8% | 63.8% | -7.7 | 95% | ❌ 31 pts to go |
| P11 | 3187 | 8.2% | 8.2% | -20.7 | 75% | ❌ 67 pts to go |
| P12 | 7 | 85.7% | 85.7% | -3.8 | n/a | no target |
| P13 | 10644 | 75.1% | 75.1% | -4.2 | 95% | ❌ 20 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 80.9% | 80.9% | +3.1 | n/a | no target |
| P01T | 173 | 88.4% | 88.4% | -2.9 | 95% | 🟡 7 pts to go |
| P01_GOLD | 626 | 82.3% | 82.3% | +0.1 | 90% | 🟡 8 pts to go |
| P02 | 403 | 88.3% | 88.3% | -0.1 | 95% | 🟡 7 pts to go |
| P03 | 209 | 84.2% | 84.2% | -0.4 | 95% | ❌ 11 pts to go |
| P04 | 1569 | 84.3% | 84.3% | +0.1 | 90% | 🟡 6 pts to go |
| P05 | 365 | 89.3% | 89.3% | -0.3 | 95% | 🟡 6 pts to go |
| P06M | 4103 | 70.4% | 70.4% | -14.7 | n/a | no target |
| P06T | 12949 | 78.9% | 78.9% | -15.2 | n/a | no target |
| P06 | 263 | 75.3% | 75.3% | -15.1 | 100% | ❌ 25 pts to go |
| P07 | 501 | 67.5% | 67.5% | -20.6 | 100% | ❌ 32 pts to go |
| P08 | 10340 | 56.5% | 56.5% | -34.2 | 100% | ❌ 44 pts to go |
| P09 | 312 | 69.9% | 69.9% | -4.1 | n/a | no target |
| P10R | 25497 | 83.7% | 83.7% |  | n/a | no target |
| P10 | 2406 | 82.7% | 82.7% | -7.4 | 100% | ❌ 17 pts to go |
| P11 | 3187 | 10.8% | 10.8% | -25.7 | 80% | ❌ 69 pts to go |
| P12 | 7 | 100.0% | 100.0% | +15.8 | n/a | no target |
| P13 | 10644 | 75.6% | 75.6% | -8.6 | 95% | ❌ 19 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 8.5% | 8.5% | -8.2 | n/a | no target |
| P01T | 173 | 15.0% | 15.0% | -8.9 | n/a | no target |
| P01_GOLD | 626 | 14.2% | 14.2% | -0.1 | 25% | ❌ 11 pts to go |
| P02 | 403 | 27.8% | 27.8% | +0.1 | 40% | ❌ 12 pts to go |
| P03 | 209 | 10.5% | 10.5% | -0.1 | 20% | 🟡 10 pts to go |
| P04 | 1569 | 7.4% | 7.4% | +0.0 | 20% | ❌ 13 pts to go |
| P05 | 365 | 3.8% | 3.8% | -0.1 | 15% | ❌ 11 pts to go |
| P06M | 4103 | 0.5% | 0.5% | -4.3 | n/a | no target |
| P06T | 12949 | 1.2% | 1.2% | -2.0 | n/a | no target |
| P06 | 263 | 5.7% | 5.7% | +0.3 | n/a | no target |
| P07 | 501 | 7.6% | 7.6% | +1.3 | n/a | no target |
| P08 | 10340 | 0.5% | 0.5% | -0.5 | n/a | no target |
| P09 | 312 | 7.7% | 7.7% | -0.2 | n/a | no target |
| P10R | 25497 | 0.5% | 0.5% |  | n/a | no target |
| P10 | 2406 | 1.1% | 1.1% | -0.2 | n/a | no target |
| P11 | 3187 | 0.4% | 0.4% | -2.1 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | -10.5 | n/a | no target |
| P13 | 10644 | 0.8% | 0.8% | +0.2 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 44.7% | 44.7% | +5.8 | n/a | no target |
| P01T | 173 | 36.4% | 36.4% | +1.6 | 70% | ❌ 34 pts to go |
| P01_GOLD | 626 | 43.3% | 43.3% | +0.0 | 80% | ❌ 37 pts to go |
| P02 | 403 | 64.3% | 64.3% | +0.2 | 90% | ❌ 26 pts to go |
| P03 | 209 | 23.4% | 23.4% | +0.3 | 60% | ❌ 37 pts to go |
| P04 | 1569 | 50.5% | 50.5% | +0.0 | 85% | ❌ 34 pts to go |
| P05 | 365 | 13.4% | 13.4% | +0.4 | 50% | ❌ 37 pts to go |
| P06M | 4103 | 0.6% | 0.6% | -5.9 | n/a | no target |
| P06T | 12949 | 1.6% | 1.6% | -1.1 | n/a | no target |
| P06 | 263 | 21.3% | 21.3% | +3.2 | n/a | no target |
| P07 | 501 | 16.4% | 16.4% | -2.6 | n/a | no target |
| P08 | 10340 | 0.2% | 0.2% | -0.4 | n/a | no target |
| P09 | 312 | 78.2% | 78.2% | -2.4 | 95% | ❌ 17 pts to go |
| P10R | 25497 | 0.8% | 0.8% |  | n/a | no target |
| P10 | 2406 | 2.8% | 2.8% | -0.3 | n/a | no target |
| P11 | 3187 | 10.0% | 10.0% | -19.3 | n/a | no target |
| P12 | 7 | 28.6% | 28.6% | -3.0 | n/a | no target |
| P13 | 10644 | 1.1% | 1.1% | +0.1 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 4.3% | 4.3% | +4.3 | n/a | no target |
| P01T | 173 | 18.5% | 18.5% | +2.2 | n/a | no target |
| P01_GOLD | 626 | 33.9% | 33.9% | -0.1 | 70% | ❌ 36 pts to go |
| P02 | 403 | 44.4% | 44.4% | +0.1 | 75% | ❌ 31 pts to go |
| P03 | 209 | 23.4% | 23.4% | +0.3 | 55% | ❌ 32 pts to go |
| P04 | 1569 | 50.5% | 50.5% | +0.0 | 75% | ❌ 24 pts to go |
| P05 | 365 | 12.1% | 12.1% | +0.4 | 50% | ❌ 38 pts to go |
| P06M | 4103 | 0.2% | 0.2% | -1.6 | n/a | no target |
| P06T | 12949 | 1.2% | 1.2% | -0.3 | n/a | no target |
| P06 | 263 | 11.8% | 11.8% | +1.6 | n/a | no target |
| P07 | 501 | 7.8% | 7.8% | -2.5 | n/a | no target |
| P08 | 10340 | 0.2% | 0.2% | -0.3 | n/a | no target |
| P09 | 312 | 76.0% | 76.0% | -1.7 | 95% | ❌ 19 pts to go |
| P10R | 25497 | 0.6% | 0.6% |  | n/a | no target |
| P10 | 2406 | 1.8% | 1.8% | +0.0 | n/a | no target |
| P11 | 3187 | 10.1% | 10.1% | -18.8 | n/a | no target |
| P12 | 7 | 14.3% | 14.3% | -1.5 | n/a | no target |
| P13 | 10644 | 0.7% | 0.7% | +0.1 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 8.5% | 8.5% | -8.2 | n/a | no target |
| P01T | 173 | 15.0% | 15.0% | -4.6 | n/a | no target |
| P01_GOLD | 626 | 57.8% | 58.0% | -0.1 | 80% | ❌ 22 pts to go |
| P02 | 403 | 52.4% | 52.6% | +0.2 | 75% | ❌ 23 pts to go |
| P03 | 209 | 45.5% | 45.5% | +0.3 | 70% | ❌ 24 pts to go |
| P04 | 1569 | 48.8% | 49.9% | +0.1 | 70% | ❌ 21 pts to go |
| P05 | 365 | 16.4% | 16.4% | +0.0 | 50% | ❌ 34 pts to go |
| P06M | 4103 | 0.6% | 0.6% | -3.6 | n/a | no target |
| P06T | 12949 | 0.8% | 0.8% | -0.8 | n/a | no target |
| P06 | 263 | 18.6% | 18.6% | -5.5 | n/a | no target |
| P07 | 501 | 3.2% | 3.2% | -2.0 | n/a | no target |
| P08 | 10340 | 0.4% | 0.4% | -0.6 | n/a | no target |
| P09 | 312 | 45.8% | 46.2% | +1.7 | 80% | ❌ 34 pts to go |
| P10R | 25497 | 0.2% | 0.2% |  | n/a | no target |
| P10 | 2406 | 1.4% | 1.5% | -0.1 | n/a | no target |
| P11 | 3187 | 2.9% | 2.9% | -13.8 | n/a | no target |
| P12 | 7 | 28.6% | 28.6% | -3.0 | n/a | no target |
| P13 | 10644 | 0.4% | 0.4% | +0.1 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 14.9% | 14.9% | -24.0 | n/a | no target |
| P01T | 173 | 34.7% | 34.7% | -21.8 | 60% | ❌ 25 pts to go |
| P01_GOLD | 626 | 63.6% | 63.6% | +0.1 | 70% | 🟡 6 pts to go |
| P02 | 403 | 43.7% | 43.7% | -0.1 | 50% | 🟡 6 pts to go |
| P03 | 209 | 55.0% | 55.0% | -0.3 | 55% | ✅ met |
| P04 | 1569 | 22.9% | 22.9% | +0.0 | 40% | ❌ 17 pts to go |
| P05 | 365 | 18.1% | 18.1% | +0.7 | 40% | ❌ 22 pts to go |
| P06M | 4103 | 0.5% | 0.5% | -16.2 | n/a | no target |
| P06T | 12949 | 2.6% | 2.6% | -9.9 | n/a | no target |
| P06 | 263 | 19.4% | 19.4% | -11.3 | n/a | no target |
| P07 | 501 | 8.6% | 8.6% | -7.7 | n/a | no target |
| P08 | 10340 | 1.5% | 1.5% | -3.2 | n/a | no target |
| P09 | 312 | 5.8% | 5.8% | +0.0 | n/a | no target |
| P10R | 25497 | 0.3% | 0.3% |  | n/a | no target |
| P10 | 2406 | 3.7% | 3.7% | -0.2 | n/a | no target |
| P11 | 3187 | 1.9% | 1.9% | -5.7 | n/a | no target |
| P12 | 7 | 14.3% | 14.3% | -1.5 | n/a | no target |
| P13 | 10644 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 17.0% | 17.0% | -27.4 | n/a | no target |
| P01T | 173 | 42.2% | 42.2% | -27.4 | 65% | ❌ 23 pts to go |
| P01_GOLD | 626 | 69.2% | 69.2% | +0.0 | 70% | 🟡 1 pts to go |
| P02 | 403 | 26.1% | 26.1% | -0.1 | 50% | ❌ 24 pts to go |
| P03 | 209 | 56.0% | 56.0% | -0.2 | 60% | 🟡 4 pts to go |
| P04 | 1569 | 9.9% | 9.9% | +0.0 | 40% | ❌ 30 pts to go |
| P05 | 365 | 21.4% | 21.4% | +0.0 | 45% | ❌ 24 pts to go |
| P06M | 4103 | 0.2% | 0.2% | -6.9 | n/a | no target |
| P06T | 12949 | 0.9% | 0.9% | -3.4 | n/a | no target |
| P06 | 263 | 33.5% | 33.5% | -14.7 | n/a | no target |
| P07 | 501 | 11.2% | 11.2% | -12.6 | n/a | no target |
| P08 | 10340 | 0.7% | 0.7% | -1.7 | n/a | no target |
| P09 | 312 | 9.6% | 9.6% | +0.9 | n/a | no target |
| P10R | 25497 | 0.1% | 0.1% |  | n/a | no target |
| P10 | 2406 | 2.0% | 2.0% | -0.1 | n/a | no target |
| P11 | 3187 | 1.0% | 1.0% | -5.8 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | -10.5 | n/a | no target |
| P13 | 10644 | 0.3% | 0.3% | +0.1 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 4.3% | 4.3% | -6.8 | n/a | no target |
| P01T | 173 | 24.9% | 24.9% | -19.7 | n/a | no target |
| P01_GOLD | 626 | 49.7% | 49.7% | -0.1 | 50% | 🟡 0 pts to go |
| P02 | 403 | 42.7% | 42.7% | +0.1 | n/a | no target |
| P03 | 209 | 58.4% | 58.4% | -0.3 | 60% | 🟡 2 pts to go |
| P04 | 1569 | 26.3% | 26.3% | -0.1 | n/a | no target |
| P05 | 365 | 16.7% | 16.7% | +0.0 | n/a | no target |
| P06M | 4103 | 0.4% | 0.4% | -3.8 | n/a | no target |
| P06T | 12949 | 1.2% | 1.2% | -2.8 | n/a | no target |
| P06 | 263 | 25.1% | 25.1% | -10.4 | n/a | no target |
| P07 | 501 | 10.2% | 10.2% | -8.5 | n/a | no target |
| P08 | 10340 | 0.5% | 0.5% | -1.0 | n/a | no target |
| P09 | 312 | 18.3% | 18.3% | -0.6 | n/a | no target |
| P10R | 25497 | 0.3% | 0.3% |  | n/a | no target |
| P10 | 2406 | 2.4% | 2.4% | +0.0 | n/a | no target |
| P11 | 3187 | 1.1% | 1.1% | -6.7 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | -21.1 | n/a | no target |
| P13 | 10644 | 0.6% | 0.6% | +0.2 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 8.5% | 8.5% | -19.3 | 15% | 🟡 6 pts to go |
| P01T | 173 | 17.9% | 17.9% | -11.4 | 15% | ✅ met |
| P01_GOLD | 626 | 35.3% | 35.3% | +0.2 | 40% | 🟡 5 pts to go |
| P02 | 403 | 13.6% | 13.9% | -0.3 | 25% | ❌ 11 pts to go |
| P03 | 209 | 21.5% | 21.5% | -0.1 | 25% | 🟡 4 pts to go |
| P04 | 1569 | 5.2% | 5.2% | +0.0 | 15% | 🟡 10 pts to go |
| P05 | 365 | 7.4% | 7.4% | -0.7 | 15% | 🟡 8 pts to go |
| P06M | 4103 | 0.7% | 0.7% | -5.3 | 15% | ❌ 14 pts to go |
| P06T | 12949 | 0.7% | 0.7% | -0.8 | 15% | ❌ 14 pts to go |
| P06 | 263 | 8.4% | 8.4% | -1.8 | 15% | 🟡 7 pts to go |
| P07 | 501 | 3.8% | 3.8% | -2.9 | 15% | ❌ 11 pts to go |
| P08 | 10340 | 0.3% | 0.3% | -0.6 | 15% | ❌ 15 pts to go |
| P09 | 312 | 1.0% | 1.0% | +0.2 | 15% | ❌ 14 pts to go |
| P10R | 25497 | 0.6% | 0.6% |  | 15% | ❌ 14 pts to go |
| P10 | 2406 | 1.5% | 1.5% | +0.1 | 15% | ❌ 14 pts to go |
| P11 | 3187 | 0.2% | 0.2% | -1.1 | 15% | ❌ 15 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 10644 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 4.3% | 4.3% | -6.8 | 15% | ❌ 11 pts to go |
| P01T | 173 | 19.1% | 19.1% | -13.5 | 25% | 🟡 6 pts to go |
| P01_GOLD | 626 | 29.1% | 29.1% | -0.1 | 25% | ✅ met |
| P02 | 403 | 28.0% | 28.0% | +0.0 | 15% | ✅ met |
| P03 | 209 | 25.8% | 25.8% | -0.2 | 15% | ✅ met |
| P04 | 1569 | 8.1% | 8.1% | -0.1 | 15% | 🟡 7 pts to go |
| P05 | 365 | 12.1% | 12.1% | +0.1 | 15% | 🟡 3 pts to go |
| P06M | 4103 | 0.1% | 0.1% | -2.3 | 15% | ❌ 15 pts to go |
| P06T | 12949 | 0.6% | 0.6% | -2.1 | 15% | ❌ 14 pts to go |
| P06 | 263 | 7.6% | 7.6% | -4.4 | 15% | 🟡 7 pts to go |
| P07 | 501 | 4.0% | 4.0% | -3.5 | 15% | ❌ 11 pts to go |
| P08 | 10340 | 0.3% | 0.3% | -0.7 | 15% | ❌ 15 pts to go |
| P09 | 312 | 1.0% | 1.0% | +0.2 | 15% | ❌ 14 pts to go |
| P10R | 25497 | 0.1% | 0.1% |  | 15% | ❌ 15 pts to go |
| P10 | 2406 | 1.3% | 1.3% | -0.1 | 15% | ❌ 14 pts to go |
| P11 | 3187 | 0.8% | 0.8% | -4.3 | 15% | ❌ 14 pts to go |
| P12 | 7 | 14.3% | 14.3% | -12.0 | 15% | 🟡 1 pts to go |
| P13 | 10644 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 2.1% | 2.1% | -3.5 | 20% | ❌ 18 pts to go |
| P01T | 173 | 5.8% | 5.8% | -4.0 | 20% | ❌ 14 pts to go |
| P01_GOLD | 626 | 4.3% | 4.3% | +0.0 | 20% | ❌ 16 pts to go |
| P02 | 403 | 1.5% | 1.5% | +0.0 | 20% | ❌ 18 pts to go |
| P03 | 209 | 1.9% | 1.9% | +0.0 | 20% | ❌ 18 pts to go |
| P04 | 1569 | 1.0% | 1.0% | +0.0 | 20% | ❌ 19 pts to go |
| P05 | 365 | 1.1% | 1.1% | +0.1 | 20% | ❌ 19 pts to go |
| P06M | 4103 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 12949 | 0.1% | 0.1% | -0.1 | 20% | ❌ 20 pts to go |
| P06 | 263 | 1.9% | 1.9% | -1.7 | 20% | ❌ 18 pts to go |
| P07 | 501 | 0.6% | 0.6% | -0.2 | 20% | ❌ 19 pts to go |
| P08 | 10340 | 0.0% | 0.0% | -0.2 | 20% | ❌ 20 pts to go |
| P09 | 312 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10R | 25497 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P10 | 2406 | 0.2% | 0.2% | -0.1 | 20% | ❌ 20 pts to go |
| P11 | 3187 | 0.1% | 0.1% | -0.5 | 20% | ❌ 20 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 10644 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 2.1% | 2.1% | -3.5 | 15% | ❌ 13 pts to go |
| P01T | 173 | 4.0% | 4.0% | -3.6 | 15% | ❌ 11 pts to go |
| P01_GOLD | 626 | 10.5% | 10.5% | -0.1 | 15% | 🟡 4 pts to go |
| P02 | 403 | 13.4% | 13.4% | +0.0 | 15% | 🟡 2 pts to go |
| P03 | 209 | 23.9% | 23.9% | -0.1 | 15% | ✅ met |
| P04 | 1569 | 4.5% | 4.5% | -0.1 | 15% | ❌ 10 pts to go |
| P05 | 365 | 3.0% | 3.0% | +0.1 | 15% | ❌ 12 pts to go |
| P06M | 4103 | 0.2% | 0.2% | -2.2 | 15% | ❌ 15 pts to go |
| P06T | 12949 | 0.3% | 0.3% | -1.1 | 15% | ❌ 15 pts to go |
| P06 | 263 | 3.8% | 3.8% | -1.6 | 15% | ❌ 11 pts to go |
| P07 | 501 | 2.0% | 2.0% | -1.6 | 15% | ❌ 13 pts to go |
| P08 | 10340 | 0.3% | 0.3% | -0.4 | 15% | ❌ 15 pts to go |
| P09 | 312 | 0.6% | 0.6% | +0.1 | 15% | ❌ 14 pts to go |
| P10R | 25497 | 0.1% | 0.1% |  | 15% | ❌ 15 pts to go |
| P10 | 2406 | 0.7% | 0.7% | -0.1 | 15% | ❌ 14 pts to go |
| P11 | 3187 | 0.3% | 0.3% | -1.8 | 15% | ❌ 15 pts to go |
| P12 | 7 | 0.0% | 0.0% | -5.3 | 15% | ❌ 15 pts to go |
| P13 | 10644 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 6.4% | 6.4% | -4.7 | 20% | ❌ 14 pts to go |
| P01T | 173 | 23.1% | 23.1% | -18.2 | 40% | ❌ 17 pts to go |
| P01_GOLD | 626 | 45.7% | 45.7% | -0.1 | 40% | ✅ met |
| P02 | 403 | 48.6% | 48.6% | +0.1 | 20% | ✅ met |
| P03 | 209 | 55.5% | 55.5% | -0.3 | 35% | ✅ met |
| P04 | 1569 | 30.2% | 30.2% | -0.1 | 20% | ✅ met |
| P05 | 365 | 16.7% | 16.7% | +0.0 | 20% | 🟡 3 pts to go |
| P06M | 4103 | 0.4% | 0.4% | -3.8 | 20% | ❌ 20 pts to go |
| P06T | 12949 | 1.5% | 1.5% | -3.0 | 20% | ❌ 18 pts to go |
| P06 | 263 | 25.1% | 25.1% | -10.4 | 20% | ✅ met |
| P07 | 501 | 8.6% | 8.6% | -6.1 | 20% | ❌ 11 pts to go |
| P08 | 10340 | 0.8% | 0.8% | -1.5 | 20% | ❌ 19 pts to go |
| P09 | 312 | 18.3% | 18.3% | -3.7 | 20% | 🟡 2 pts to go |
| P10R | 25497 | 0.4% | 0.4% |  | 20% | ❌ 20 pts to go |
| P10 | 2406 | 2.5% | 2.5% | -0.1 | 20% | ❌ 18 pts to go |
| P11 | 3187 | 1.3% | 1.3% | -6.7 | 20% | ❌ 19 pts to go |
| P12 | 7 | 0.0% | 0.0% | -15.8 | 20% | ❌ 20 pts to go |
| P13 | 10644 | 0.9% | 0.9% | +0.3 | 20% | ❌ 19 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 40.4% | 40.4% | +40.4 | n/a | no target |
| P01T | 173 | 0.6% | 0.6% | -0.5 | n/a | no target |
| P01_GOLD | 626 | 69.6% | 69.6% | -0.1 | 95% | ❌ 25 pts to go |
| P02 | 403 | 73.2% | 73.2% | -0.1 | 95% | ❌ 22 pts to go |
| P03 | 209 | 67.0% | 67.0% | -0.3 | 90% | ❌ 23 pts to go |
| P04 | 1569 | 58.5% | 58.5% | +0.1 | 85% | ❌ 26 pts to go |
| P05 | 365 | 35.6% | 35.6% | +0.7 | 75% | ❌ 39 pts to go |
| P06M | 4103 | 60.8% | 60.8% | +60.8 | n/a | no target |
| P06T | 12949 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 263 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 501 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 10340 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 312 | 89.7% | 89.7% | -1.1 | 100% | ❌ 10 pts to go |
| P10R | 25497 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2406 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3187 | 2.7% | 2.7% | -16.1 | 60% | ❌ 57 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 10644 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 40.4% | 40.4% | +40.4 | n/a | no target |
| P01T | 173 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 72.8% | 72.8% | -0.1 | 100% | ❌ 27 pts to go |
| P02 | 403 | 77.2% | 77.2% | +0.0 | 100% | ❌ 23 pts to go |
| P03 | 209 | 74.2% | 74.2% | -0.3 | n/a | no target |
| P04 | 1569 | 60.1% | 60.1% | +0.1 | 95% | ❌ 35 pts to go |
| P05 | 365 | 31.8% | 31.8% | +0.6 | 80% | ❌ 48 pts to go |
| P06M | 4103 | 60.8% | 60.8% | +60.8 | n/a | no target |
| P06T | 12949 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 263 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 501 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 10340 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 312 | 92.9% | 92.9% | -0.5 | 100% | 🟡 7 pts to go |
| P10R | 25497 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2406 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3187 | 2.9% | 2.9% | -17.1 | n/a | no target |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 10644 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 59.6% | 59.6% | +59.6 | n/a | no target |
| P01T | 173 | 0.6% | 0.6% | -0.5 | n/a | no target |
| P01_GOLD | 626 | 51.8% | 51.8% | -0.1 | 85% | ❌ 33 pts to go |
| P02 | 403 | 66.7% | 66.7% | -0.1 | 90% | ❌ 23 pts to go |
| P03 | 209 | 54.5% | 54.5% | -0.3 | 85% | ❌ 30 pts to go |
| P04 | 1569 | 64.2% | 64.2% | +0.1 | 90% | ❌ 26 pts to go |
| P05 | 365 | 35.6% | 35.6% | +0.4 | 75% | ❌ 39 pts to go |
| P06M | 4103 | 91.8% | 91.8% | +91.8 | n/a | no target |
| P06T | 12949 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 263 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 501 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 10340 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 312 | 85.3% | 85.3% | -0.3 | 95% | 🟡 10 pts to go |
| P10R | 25497 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2406 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3187 | 2.5% | 2.5% | -14.8 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 10644 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 61.7% | 61.7% | +61.7 | n/a | no target |
| P01T | 173 | 0.6% | 0.6% | -0.5 | n/a | no target |
| P01_GOLD | 626 | 51.9% | 51.9% | -0.2 | 85% | ❌ 33 pts to go |
| P02 | 403 | 61.0% | 61.0% | -0.1 | 90% | ❌ 29 pts to go |
| P03 | 209 | 56.0% | 56.0% | -0.2 | 85% | ❌ 29 pts to go |
| P04 | 1569 | 54.3% | 54.3% | +0.0 | 90% | ❌ 36 pts to go |
| P05 | 365 | 41.9% | 41.9% | +0.2 | 75% | ❌ 33 pts to go |
| P06M | 4103 | 85.4% | 85.4% | +85.4 | n/a | no target |
| P06T | 12949 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 263 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 501 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 10340 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 312 | 0.3% | 0.3% | +0.0 | 95% | ❌ 95 pts to go |
| P10R | 25497 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2406 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3187 | 2.1% | 2.1% | -12.0 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 10644 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 68.1% | 68.1% | +68.1 | n/a | no target |
| P01T | 173 | 89.0% | 89.0% | +7.5 | n/a | no target |
| P01_GOLD | 626 | 85.6% | 85.6% | -0.1 | 100% | ❌ 14 pts to go |
| P02 | 403 | 81.6% | 81.6% | -0.1 | 100% | ❌ 18 pts to go |
| P03 | 209 | 92.3% | 92.3% | +0.0 | n/a | no target |
| P04 | 1569 | 72.7% | 72.7% | +0.1 | 95% | ❌ 22 pts to go |
| P05 | 365 | 75.6% | 75.6% | +0.1 | 95% | ❌ 19 pts to go |
| P06M | 4103 | 96.7% | 96.7% | +96.1 | n/a | no target |
| P06T | 12949 | 88.7% | 88.7% | +5.3 | n/a | no target |
| P06 | 263 | 43.7% | 43.7% | -32.2 | n/a | no target |
| P07 | 501 | 35.3% | 35.3% | -41.7 | n/a | no target |
| P08 | 10340 | 21.9% | 21.9% | -63.0 | n/a | no target |
| P09 | 312 | 98.7% | 98.7% | -0.3 | 100% | 🟡 1 pts to go |
| P10R | 25497 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2406 | 86.2% | 86.2% | -12.2 | n/a | no target |
| P11 | 3187 | 34.0% | 34.0% | -55.9 | n/a | no target |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 10644 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 68.1% | 68.1% | +68.1 | n/a | no target |
| P01T | 173 | 89.0% | 89.0% | +7.5 | n/a | no target |
| P01_GOLD | 626 | 88.8% | 88.8% | -0.1 | 100% | ❌ 11 pts to go |
| P02 | 403 | 82.9% | 83.1% | +0.0 | 100% | ❌ 17 pts to go |
| P03 | 209 | 93.8% | 93.8% | +0.0 | n/a | no target |
| P04 | 1569 | 79.2% | 79.2% | +0.2 | 95% | ❌ 16 pts to go |
| P05 | 365 | 89.9% | 89.9% | -0.2 | 70% | ✅ met |
| P06M | 4103 | 96.7% | 96.7% | +96.1 | n/a | no target |
| P06T | 12949 | 88.7% | 88.7% | +5.3 | n/a | no target |
| P06 | 263 | 43.7% | 43.7% | -32.2 | n/a | no target |
| P07 | 501 | 35.3% | 35.3% | -41.7 | n/a | no target |
| P08 | 10340 | 21.9% | 21.9% | -63.0 | n/a | no target |
| P09 | 312 | 98.7% | 98.7% | -0.3 | 100% | 🟡 1 pts to go |
| P10R | 25497 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2406 | 86.2% | 86.2% | -12.2 | n/a | no target |
| P11 | 3187 | 34.0% | 34.0% | -56.3 | n/a | no target |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 10644 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 173 | 0.6% | 0.6% | -0.5 | n/a | no target · rows from a source that publishes bids: 6 rows, 16.7% filled |
| P01_GOLD | 626 | 17.3% | 17.3% | +0.0 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 367 rows, 29.4% filled |
| P02 | 403 | 13.2% | 13.2% | +0.1 | n/a | no target · rows from a source that publishes bids: 294 rows, 18.0% filled |
| P03 | 209 | 16.3% | 16.3% | +0.0 | n/a | no target · rows from a source that publishes bids: 140 rows, 24.3% filled |
| P04 | 1569 | 3.7% | 3.7% | +0.0 | n/a | no target · rows from a source that publishes bids: 878 rows, 6.6% filled |
| P05 | 365 | 3.6% | 3.6% | +0.2 | n/a | no target · rows from a source that publishes bids: 53 rows, 24.5% filled |
| P06M | 4103 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 12949 | 0.0% | 0.0% | -0.1 | n/a | no target · rows from a source that publishes bids: 64 rows, 4.7% filled |
| P06 | 263 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 501 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 10340 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 312 | 3.2% | 3.2% | +0.1 | n/a | no target · rows from a source that publishes bids: 299 rows, 3.3% filled |
| P10R | 25497 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2406 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3187 | 0.4% | 0.4% | -2.3 | n/a | no target · rows from a source that publishes bids: 91 rows, 14.3% filled |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 7 rows, 0.0% filled |
| P13 | 10644 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 173 | 0.6% | 97.1% | +0.6 | n/a | no target |
| P01_GOLD | 626 | 53.0% | 82.4% | -0.2 | 90% | ❌ 37 pts to go |
| P02 | 403 | 61.0% | 85.6% | -0.1 | 90% | ❌ 29 pts to go |
| P03 | 209 | 56.0% | 75.6% | -0.2 | 90% | ❌ 34 pts to go |
| P04 | 1569 | 45.4% | 85.6% | +0.1 | 90% | ❌ 45 pts to go |
| P05 | 365 | 0.0% | 80.0% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 4103 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 12949 | 0.0% | 99.5% | +0.0 | n/a | no target |
| P06 | 263 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 501 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 10340 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 312 | 2.2% | 3.8% | +0.1 | 90% | ❌ 88 pts to go |
| P10R | 25497 | 0.0% | 100.0% |  | n/a | no target |
| P10 | 2406 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 3187 | 1.9% | 98.6% | -10.8 | n/a | no target |
| P12 | 7 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 10644 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 173 | 1.2% | 97.7% | +1.2 | n/a | no target |
| P01_GOLD | 626 | 25.9% | 55.3% | -0.1 | 90% | ❌ 64 pts to go |
| P02 | 403 | 60.0% | 84.6% | +0.1 | n/a | no target |
| P03 | 209 | 30.6% | 50.2% | -0.2 | n/a | no target |
| P04 | 1569 | 49.8% | 89.9% | +0.1 | n/a | no target |
| P05 | 365 | 0.5% | 80.5% | +0.0 | n/a | no target |
| P06M | 4103 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 12949 | 0.3% | 99.8% | +0.3 | n/a | no target |
| P06 | 263 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 501 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 10340 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 312 | 42.0% | 43.6% | -2.4 | n/a | no target |
| P10R | 25497 | 0.0% | 100.0% |  | n/a | no target |
| P10 | 2406 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 3187 | 1.7% | 98.5% | -9.9 | n/a | no target |
| P12 | 7 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 10644 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 173 | 2.9% | 99.4% | +0.7 | n/a | no target |
| P01_GOLD | 626 | 51.6% | 81.0% | +0.0 | 95% | ❌ 43 pts to go |
| P02 | 403 | 65.8% | 90.3% | +0.2 | n/a | no target |
| P03 | 209 | 58.9% | 78.5% | -0.2 | n/a | no target |
| P04 | 1569 | 50.4% | 90.5% | +0.1 | n/a | no target |
| P05 | 365 | 5.5% | 85.5% | +0.3 | n/a | no target |
| P06M | 4103 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 12949 | 0.4% | 99.9% | +0.4 | n/a | no target |
| P06 | 263 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 501 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 10340 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 312 | 64.1% | 65.7% | -3.4 | n/a | no target |
| P10R | 25497 | 0.0% | 100.0% |  | n/a | no target |
| P10 | 2406 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 3187 | 1.9% | 98.6% | -10.8 | n/a | no target |
| P12 | 7 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 10644 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 173 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 403 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 209 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 1569 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 365 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 4103 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 12949 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 263 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 501 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 10340 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 312 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 25497 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2406 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 3187 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 10644 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 173 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 403 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 209 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 1569 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 365 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 4103 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 12949 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 263 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 501 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 10340 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 312 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 25497 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2406 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 3187 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 10644 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 47 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 173 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 403 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 209 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 1569 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 365 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 4103 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 12949 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 263 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 501 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 10340 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 312 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 25497 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2406 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 3187 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 10644 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

