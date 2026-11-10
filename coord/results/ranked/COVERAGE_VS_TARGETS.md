# Coverage vs the downstream team's targets — 2026-11-10

Benchmarks (field × package with a numeric target): **99 of 446 met** (22.2%); 76 within 10 points; 271 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 15, P01T 136, P01_GOLD 625, P02 403, P03 209, P04 1568, P05 378, P06M 143, P06T 8765, P06 220, P07 443, P08 8765, P09 349, P10R 30880, P10 2746, P11 1309, P12 8, P13 13602

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 15 | 0.0% | 40.0% | 8 | reference to quote (PO / contract / vendor id) (15 rows) |
| P01T | 136 | 0.7% | 32.4% | 8 | reference to quote (PO / contract / vendor id) (130 rows) |
| P01_GOLD | 625 | 24.3% | 71.2% | 10 | payment terms (214 rows) |
| P02 | 403 | 8.9% | 62.8% | 9 | PO rule (298 rows) |
| P03 | 209 | 17.7% | 69.9% | 9 | PO rule (92 rows) |
| P04 | 1568 | 2.9% | 38.5% | 8 | PO rule (1413 rows) |
| P05 | 378 | 1.3% | 18.8% | 7 | payment terms (309 rows) |
| P06M | 143 | 0.0% | 4.2% | 7 | reference to quote (PO / contract / vendor id) (143 rows) |
| P06T | 8765 | 0.0% | 1.6% | 6 | reference to quote (PO / contract / vendor id) (8732 rows) |
| P06 | 220 | 0.0% | 9.5% | 6 | reference to quote (PO / contract / vendor id) (220 rows) |
| P07 | 443 | 0.0% | 2.9% | 5 | reference to quote (PO / contract / vendor id) (443 rows) |
| P08 | 8765 | 0.0% | 0.3% | 4 | reference to quote (PO / contract / vendor id) (8765 rows) |
| P09 | 349 | 1.1% | 44.1% | 8 | payment terms (326 rows) |
| P10R | 30880 | 0.0% | 0.0% | 6 | vendor GST/HST number (30880 rows) |
| P10 | 2746 | 0.0% | 0.8% | 5 | reference to quote (PO / contract / vendor id) (2743 rows) |
| P11 | 1309 | 0.5% | 4.4% | 3 | PO rule (1277 rows) |
| P12 | 8 | 0.0% | 62.5% | 9 | PO rule (7 rows) |
| P13 | 13602 | 0.0% | 0.0% | 6 | reference to quote (PO / contract / vendor id) (13602 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 15 | 5 | 1 | 9 | 0 | 0 | 76 |
| P01T | 136 | 27 | 44 | 65 | 0 | 0 | 77 |
| P01_GOLD | 625 | 231 | 186 | 208 | 0 | 0 | 82 |
| P02 | 403 | 0 | 183 | 220 | 0 | 0 | 66 |
| P03 | 209 | 0 | 0 | 202 | 7 | 0 | 58 |
| P04 | 1568 | 0 | 0 | 1518 | 50 | 0 | 53 |
| P05 | 378 | 15 | 29 | 317 | 17 | 0 | 51 |
| P06M | 143 | 0 | 3 | 136 | 4 | 0 | 51 |
| P06T | 8765 | 0 | 25 | 7516 | 1224 | 0 | 43 |
| P06 | 220 | 18 | 32 | 170 | 0 | 0 | 69 |
| P07 | 443 | 0 | 16 | 398 | 29 | 0 | 51 |
| P08 | 8765 | 0 | 0 | 5975 | 2790 | 0 | 38 |
| P09 | 349 | 5 | 13 | 328 | 3 | 0 | 53 |
| P10R | 30880 | 1 | 7 | 25588 | 5284 | 0 | 43 |
| P10 | 2746 | 4 | 14 | 1910 | 818 | 0 | 43 |
| P11 | 1309 | 0 | 0 | 0 | 0 | 1309 | 22 |
| P12 | 8 | 0 | 1 | 7 | 0 | 0 | 54 |
| P13 | 13602 | 4 | 11 | 12531 | 1056 | 0 | 51 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 15 | 6 | 40.0% | the buyer's PO / reference rule (8) |
| P01T | 136 | 57 | 41.9% | the buyer's PO / reference rule (49) |
| P01_GOLD | 625 | 464 | 74.2% | bill-to legal name and address (109) |
| P02 | 403 | 305 | 75.7% | the buyer's PO / reference rule (54) |
| P03 | 209 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (209) |
| P04 | 1568 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (1568) |
| P05 | 378 | 47 | 12.4% | a confirmed invoicing / AP or finance channel (290) |
| P06M | 143 | 1 | 0.7% | a confirmed invoicing / AP or finance channel (123) |
| P06T | 8765 | 17 | 0.2% | a confirmed invoicing / AP or finance channel (8549) |
| P06 | 220 | 31 | 14.1% | bill-to legal name and address (127) |
| P07 | 443 | 9 | 2.0% | bill-to legal name and address (194) |
| P08 | 8765 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (8765) |
| P09 | 349 | 48 | 13.8% | a confirmed invoicing / AP or finance channel (292) |
| P10R | 30880 | 350 | 1.1% | a confirmed invoicing / AP or finance channel (30151) |
| P10 | 2746 | 10 | 0.4% | a confirmed invoicing / AP or finance channel (2607) |
| P11 | 1309 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (1309) |
| P12 | 8 | 2 | 25.0% | a confirmed invoicing / AP or finance channel (6) |
| P13 | 13602 | 5 | 0.0% | a confirmed invoicing / AP or finance channel (13263) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 15 | 6 | 40.0% | 7 | 0 | tax treatment (1) |
| P01T | 136 | 42 | 30.9% | 16 | 0 | the vendor's GST/HST number (BN9) (51) |
| P01_GOLD | 625 | 409 | 65.4% | 20 | 0 | the vendor's GST/HST number (BN9) (124) |
| P02 | 403 | 218 | 54.1% | 35 | 0 | the vendor's GST/HST number (BN9) (130) |
| P03 | 209 | 17 | 8.1% | 1 | 131 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (49) |
| P04 | 1568 | 43 | 2.7% | 10 | 706 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (771) |
| P05 | 378 | 22 | 5.8% | 10 | 93 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (188) |
| P06M | 143 | 2 | 1.4% | 14 | 66 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (54) |
| P06T | 8765 | 17 | 0.2% | 56 | 1352 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (7124) |
| P06 | 220 | 15 | 6.8% | 20 | 0 | the vendor's GST/HST number (BN9) (96) |
| P07 | 443 | 7 | 1.6% | 28 | 17 | the vendor's GST/HST number (BN9) (168) |
| P08 | 8765 | 2 | 0.0% | 3 | 711 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (8023) |
| P09 | 349 | 44 | 12.6% | 1 | 136 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (146) |
| P10R | 30880 | 572 | 1.9% | 0 | 21561 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (8523) |
| P10 | 2746 | 6 | 0.2% | 23 | 415 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2168) |
| P11 | 1309 | 6 | 0.5% | 0 | 0 | a confirmed invoicing / AP or finance channel (1292) |
| P12 | 8 | 2 | 25.0% | 0 | 3 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (3) |
| P13 | 13602 | 5 | 0.0% | 263 | 9651 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (3561) |
| **all** | 70564 | 1435 | 2.0% | 507 | 34842 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 10 | 0 | 0 | 0 | 0 | 1 | 0 | 8 | 9 | 1 |
| P01T | 109 | 0 | 0 | 0 | 5 | 19 | 7 | 68 | 79 | 30 |
| P01_GOLD | 394 | 0 | 0 | 0 | 11 | 94 | 34 | 192 | 227 | 60 |
| P02 | 403 | 0 | 403 | 0 | 4 | 38 | 8 | 298 | 227 | 22 |
| P03 | 209 | 0 | 209 | 0 | 2 | 34 | 11 | 92 | 94 | 25 |
| P04 | 1568 | 0 | 1568 | 0 | 12 | 328 | 93 | 1413 | 1208 | 106 |
| P05 | 363 | 0 | 313 | 0 | 8 | 91 | 44 | 296 | 311 | 55 |
| P06M | 143 | 0 | 143 | 0 | 0 | 17 | 29 | 134 | 124 | 0 |
| P06T | 8765 | 0 | 8765 | 0 | 981 | 4501 | 1609 | 8653 | 8444 | 122 |
| P06 | 202 | 0 | 0 | 0 | 34 | 115 | 53 | 137 | 171 | 8 |
| P07 | 443 | 0 | 443 | 0 | 133 | 252 | 104 | 385 | 401 | 16 |
| P08 | 8765 | 0 | 8765 | 0 | 4278 | 6730 | 3051 | 8691 | 8606 | 167 |
| P09 | 344 | 0 | 323 | 0 | 9 | 74 | 4 | 317 | 330 | 50 |
| P10R | 30879 | 0 | 30746 | 0 | 352 | 17660 | 7056 | 30849 | 30796 | 27 |
| P10 | 2742 | 0 | 2688 | 0 | 355 | 1887 | 983 | 2692 | 2648 | 118 |
| P11 | 1309 | 1309 | 1268 | 0 | 53 | 1167 | 768 | 1277 | 1273 | 31 |
| P12 | 8 | 0 | 7 | 0 | 0 | 2 | 0 | 7 | 6 | 0 |
| P13 | 13598 | 0 | 13477 | 0 | 222 | 3785 | 1590 | 13566 | 13574 | 29 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_ap_cycle_published | P10R | 0.0% | 20% | 6171 |
| ap_system_hint | P10R | 0.4% | 20% | 6049 |
| buyer_phone | P08 | 40.2% | 95% | 4807 |
| buyer_logo_url | P08 | 46.5% | 100% | 4691 |
| buyer_tax_exempt_status | P10R | 0.1% | 15% | 4609 |
| buyer_esignature_preference | P10R | 0.1% | 15% | 4609 |
| buyer_legal_name_as_published | P08 | 23.2% | 75% | 4539 |
| vendor_registered_address | P08 | 18.7% | 70% | 4494 |
| buyer_payment_method_preference | P10R | 0.6% | 15% | 4449 |
| vendor_logo_url | P08 | 53.6% | 100% | 4065 |
| vendor_phone | P08 | 40.6% | 85% | 3891 |
| vendor_emails | P08 | 36.7% | 75% | 3356 |
| vendor_bn9 | P08 | 15.1% | 50% | 3062 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 2719 |
| buyer_address | P08 | 65.1% | 95% | 2618 |
| ap_system_hint | P13 | 0.9% | 20% | 2599 |
| buyer_bn_as_published | P08 | 8.7% | 35% | 2302 |
| buyer_logo_url | P13 | 78.1% | 95% | 2299 |
| buyer_phone | P13 | 78.3% | 95% | 2274 |
| vendor_trading_name | P08 | 24.5% | 50% | 2232 |
| invoice_reference_hint | P08 | 0.8% | 25% | 2118 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 2032 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 2028 |
| buyer_payment_method_preference | P13 | 0.5% | 15% | 1978 |
| buyer_ap_cycle_published | P08 | 0.1% | 20% | 1748 |
| buyer_ap_cycle_published | P06T | 0.1% | 20% | 1746 |
| ap_system_hint | P08 | 0.9% | 20% | 1671 |
| ap_system_hint | P06T | 1.8% | 20% | 1596 |
| buyer_esignature_preference | P08 | 0.3% | 15% | 1291 |
| buyer_payment_method_preference | P08 | 0.3% | 15% | 1285 |
| buyer_tax_exempt_status | P08 | 0.3% | 15% | 1285 |
| buyer_esignature_preference | P06T | 0.4% | 15% | 1279 |
| buyer_payment_method_preference | P06T | 0.7% | 15% | 1255 |
| buyer_tax_exempt_status | P06T | 0.8% | 15% | 1243 |
| buyer_legal_name_as_published | P10 | 31.3% | 70% | 1064 |
| vendor_registered_address | P10 | 35.1% | 70% | 959 |
| vendor_emails | P10 | 46.4% | 80% | 924 |
| buyer_address | P13 | 88.3% | 95% | 918 |
| buyer_phone | P10 | 61.8% | 95% | 913 |
| buyer_address | P10 | 64.1% | 95% | 849 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 46.7% | 46.7% | +2.3 | 50% | 🟡 3 pts to go |
| P01T | 136 | 52.2% | 52.2% | -19.5 | 50% | ✅ met |
| P01_GOLD | 625 | 92.5% | 94.6% | +0.0 | 95% | 🟡 2 pts to go |
| P02 | 403 | 83.9% | 85.6% | +0.0 | 95% | ❌ 11 pts to go |
| P03 | 209 | 92.3% | 95.7% | -0.5 | 95% | 🟡 3 pts to go |
| P04 | 1568 | 68.8% | 71.4% | +0.2 | 90% | ❌ 21 pts to go |
| P05 | 378 | 41.8% | 44.7% | +0.7 | 70% | ❌ 28 pts to go |
| P06M | 143 | 6.3% | 6.3% | -0.8 | n/a | no target |
| P06T | 8765 | 1.6% | 1.7% | -2.8 | n/a | no target |
| P06 | 220 | 37.7% | 37.7% | -10.5 | 30% | ✅ met |
| P07 | 443 | 13.1% | 13.1% | -10.7 | 30% | ❌ 17 pts to go |
| P08 | 8765 | 0.8% | 0.8% | -1.6 | 25% | ❌ 24 pts to go |
| P09 | 349 | 99.1% | 99.7% | +0.1 | 100% | 🟡 1 pts to go |
| P10R | 30880 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2746 | 2.1% | 2.8% | -0.1 | 25% | ❌ 23 pts to go |
| P11 | 1309 | 59.5% | 60.7% | +35.4 | 60% | 🟡 0 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 13602 | 0.3% | 0.3% | +0.1 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 136 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 625 | 6.2% | 6.2% | +0.0 | 50% | ❌ 44 pts to go |
| P02 | 403 | 7.2% | 7.2% | +0.0 | 50% | ❌ 43 pts to go |
| P03 | 209 | 1.9% | 1.9% | +0.0 | 40% | ❌ 38 pts to go |
| P04 | 1568 | 1.1% | 1.1% | +0.0 | 30% | ❌ 29 pts to go |
| P05 | 378 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 143 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 8765 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 220 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 443 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 8765 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 349 | 0.6% | 0.6% | +0.1 | 50% | ❌ 49 pts to go |
| P10R | 30880 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2746 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P11 | 1309 | 0.3% | 0.3% | -0.5 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 13602 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 136 | 4.4% | 4.4% | -1.0 | 50% | ❌ 46 pts to go |
| P01_GOLD | 625 | 67.7% | 67.7% | +0.1 | 85% | ❌ 17 pts to go |
| P02 | 403 | 75.4% | 75.4% | -0.1 | 90% | ❌ 15 pts to go |
| P03 | 209 | 75.1% | 75.1% | -0.4 | 85% | 🟡 10 pts to go |
| P04 | 1568 | 65.7% | 65.7% | +0.2 | 85% | ❌ 19 pts to go |
| P05 | 378 | 31.5% | 31.5% | +0.5 | 60% | ❌ 28 pts to go |
| P06M | 143 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 8765 | 0.4% | 0.4% | +0.2 | n/a | no target |
| P06 | 220 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 443 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 8765 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 349 | 96.6% | 96.6% | +0.0 | 100% | 🟡 3 pts to go |
| P10R | 30880 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2746 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1309 | 58.1% | 58.1% | +38.1 | 60% | 🟡 2 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 13602 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 136 | 2.2% | 2.2% | +0.0 | 30% | ❌ 28 pts to go |
| P01_GOLD | 625 | 51.4% | 51.4% | +0.1 | 80% | ❌ 29 pts to go |
| P02 | 403 | 66.7% | 66.7% | -0.1 | 60% | ✅ met |
| P03 | 209 | 63.6% | 63.6% | -0.3 | 80% | ❌ 16 pts to go |
| P04 | 1568 | 54.7% | 54.7% | +0.2 | 50% | ✅ met |
| P05 | 378 | 13.5% | 13.5% | +0.2 | 40% | ❌ 26 pts to go |
| P06M | 143 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 8765 | 0.4% | 0.4% | +0.2 | n/a | no target |
| P06 | 220 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 443 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 8765 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 349 | 85.4% | 85.4% | -0.7 | 50% | ✅ met |
| P10R | 30880 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2746 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1309 | 6.3% | 6.3% | -11.2 | 40% | ❌ 34 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 13602 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 136 | 2.9% | 2.9% | -0.4 | n/a | no target |
| P01_GOLD | 625 | 61.1% | 61.1% | +0.0 | 85% | ❌ 24 pts to go |
| P02 | 403 | 65.8% | 65.8% | +0.0 | 90% | ❌ 24 pts to go |
| P03 | 209 | 74.2% | 74.2% | -0.3 | 85% | ❌ 11 pts to go |
| P04 | 1568 | 56.5% | 56.5% | +0.2 | 85% | ❌ 28 pts to go |
| P05 | 378 | 21.4% | 21.4% | +0.3 | 50% | ❌ 29 pts to go |
| P06M | 143 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 8765 | 0.4% | 0.4% | +0.2 | n/a | no target |
| P06 | 220 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 443 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 8765 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 349 | 97.1% | 97.1% | +0.0 | 100% | 🟡 3 pts to go |
| P10R | 30880 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2746 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1309 | 6.8% | 6.8% | -12.2 | 60% | ❌ 53 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 13602 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 136 | 1.5% | 1.5% | -0.7 | n/a | no target |
| P01_GOLD | 625 | 13.0% | 13.0% | +0.0 | 60% | ❌ 47 pts to go |
| P02 | 403 | 7.2% | 7.2% | +0.0 | 50% | ❌ 43 pts to go |
| P03 | 209 | 10.5% | 10.5% | -0.1 | 50% | ❌ 40 pts to go |
| P04 | 1568 | 4.3% | 4.3% | +0.0 | 40% | ❌ 36 pts to go |
| P05 | 378 | 1.3% | 1.3% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 143 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 8765 | 0.0% | 0.0% | -0.1 | n/a | no target |
| P06 | 220 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 443 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 8765 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 349 | 2.9% | 2.9% | +0.3 | 50% | ❌ 47 pts to go |
| P10R | 30880 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2746 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1309 | 1.1% | 1.1% | -1.9 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 13602 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 136 | 0.7% | 0.7% | +0.7 | n/a | no target |
| P01_GOLD | 625 | 35.0% | 35.0% | -0.1 | 80% | ❌ 45 pts to go |
| P02 | 403 | 60.8% | 60.8% | +0.2 | 90% | ❌ 29 pts to go |
| P03 | 209 | 41.1% | 41.1% | -0.2 | 80% | ❌ 39 pts to go |
| P04 | 1568 | 51.4% | 51.4% | +0.1 | 85% | ❌ 34 pts to go |
| P05 | 378 | 6.1% | 6.1% | +0.1 | 50% | ❌ 44 pts to go |
| P06M | 143 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 8765 | 0.2% | 0.2% | +0.2 | n/a | no target |
| P06 | 220 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 443 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 8765 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 349 | 76.5% | 76.5% | +0.6 | 95% | ❌ 18 pts to go |
| P10R | 30880 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2746 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1309 | 4.7% | 4.7% | -8.4 | 50% | ❌ 45 pts to go |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 13602 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 136 | 0.7% | 0.7% | -0.4 | n/a | no target |
| P01_GOLD | 625 | 8.5% | 8.5% | +0.0 | 50% | ❌ 42 pts to go |
| P02 | 403 | 7.2% | 7.2% | +0.0 | 50% | ❌ 43 pts to go |
| P03 | 209 | 2.4% | 2.4% | +0.0 | 30% | ❌ 28 pts to go |
| P04 | 1568 | 1.1% | 1.1% | +0.0 | 30% | ❌ 29 pts to go |
| P05 | 378 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 143 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 8765 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 220 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 443 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 8765 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 349 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P10R | 30880 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2746 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1309 | 0.3% | 0.3% | -0.5 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 13602 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 136 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 403 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 209 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 1568 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 378 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 143 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 8765 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 220 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 443 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 8765 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 349 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 30880 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2746 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1309 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 13602 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P01T | 136 | 56.6% | 56.6% | -23.8 | 60% | 🟡 3 pts to go |
| P01_GOLD | 625 | 77.8% | 77.8% | -0.1 | 90% | ❌ 12 pts to go |
| P02 | 403 | 67.2% | 67.2% | -0.1 | 85% | ❌ 18 pts to go |
| P03 | 209 | 82.3% | 82.3% | +0.1 | 90% | 🟡 8 pts to go |
| P04 | 1568 | 55.3% | 55.3% | -0.1 | 75% | ❌ 20 pts to go |
| P05 | 378 | 53.4% | 53.4% | +0.8 | 50% | ✅ met |
| P06M | 143 | 72.0% | 72.0% | -2.4 | n/a | no target |
| P06T | 8765 | 21.2% | 21.2% | -39.5 | n/a | no target |
| P06 | 220 | 31.8% | 31.8% | -12.2 | 40% | 🟡 8 pts to go |
| P07 | 443 | 21.9% | 21.9% | -16.2 | 50% | ❌ 28 pts to go |
| P08 | 8765 | 15.1% | 15.1% | -25.1 | 50% | ❌ 35 pts to go |
| P09 | 349 | 55.9% | 55.9% | +1.6 | 80% | ❌ 24 pts to go |
| P10R | 30880 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2746 | 30.8% | 30.8% | -5.8 | 40% | 🟡 9 pts to go |
| P11 | 1309 | 67.5% | 67.5% | +22.8 | 60% | ✅ met |
| P12 | 8 | 62.5% | 62.5% | +9.9 | 85% | ❌ 22 pts to go |
| P13 | 13602 | 89.4% | 89.4% | -2.3 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 93.3% | 93.3% | +32.2 | n/a | no target |
| P01T | 136 | 44.9% | 44.9% | -18.1 | n/a | no target |
| P01_GOLD | 625 | 74.9% | 74.9% | +0.1 | 95% | ❌ 20 pts to go |
| P02 | 403 | 84.9% | 84.9% | +0.0 | 95% | ❌ 10 pts to go |
| P03 | 209 | 78.0% | 78.0% | +0.1 | 95% | ❌ 17 pts to go |
| P04 | 1568 | 80.6% | 80.6% | -0.1 | 95% | ❌ 14 pts to go |
| P05 | 378 | 56.6% | 56.6% | +0.4 | 70% | ❌ 13 pts to go |
| P06M | 143 | 55.2% | 55.2% | +34.4 | n/a | no target |
| P06T | 8765 | 40.8% | 40.8% | -37.4 | n/a | no target |
| P06 | 220 | 39.1% | 39.1% | -16.3 | 80% | ❌ 41 pts to go |
| P07 | 443 | 29.3% | 29.3% | -22.7 | 70% | ❌ 41 pts to go |
| P08 | 8765 | 18.7% | 18.7% | -33.7 | 70% | ❌ 51 pts to go |
| P09 | 349 | 88.5% | 88.5% | +0.0 | 100% | ❌ 12 pts to go |
| P10R | 30880 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2746 | 35.1% | 35.1% | -7.3 | 70% | ❌ 35 pts to go |
| P11 | 1309 | 21.4% | 21.4% | -33.9 | 75% | ❌ 54 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 13602 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 60.0% | 60.0% | +10.0 | n/a | no target |
| P01T | 136 | 22.1% | 22.1% | +2.5 | n/a | no target |
| P01_GOLD | 625 | 52.3% | 52.3% | -0.1 | 60% | 🟡 8 pts to go |
| P02 | 403 | 67.2% | 67.2% | -0.1 | 60% | ✅ met |
| P03 | 209 | 64.6% | 64.6% | -0.3 | 60% | ✅ met |
| P04 | 1568 | 55.5% | 55.5% | +0.0 | 55% | ✅ met |
| P05 | 378 | 24.9% | 24.9% | -0.4 | 50% | ❌ 25 pts to go |
| P06M | 143 | 18.9% | 18.9% | +1.6 | n/a | no target |
| P06T | 8765 | 36.8% | 36.8% | -16.8 | n/a | no target |
| P06 | 220 | 41.4% | 41.4% | -11.6 | n/a | no target |
| P07 | 443 | 31.8% | 31.8% | -14.2 | 55% | ❌ 23 pts to go |
| P08 | 8765 | 24.5% | 24.5% | -23.0 | 50% | ❌ 26 pts to go |
| P09 | 349 | 72.5% | 72.5% | +1.1 | 70% | ✅ met |
| P10R | 30880 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2746 | 46.0% | 46.0% | -5.9 | 55% | 🟡 9 pts to go |
| P11 | 1309 | 18.0% | 18.0% | -25.0 | 50% | ❌ 32 pts to go |
| P12 | 8 | 87.5% | 87.5% | +3.3 | n/a | no target |
| P13 | 13602 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 73.3% | 73.3% | +12.2 | n/a | no target |
| P01T | 136 | 39.0% | 39.0% | +8.6 | n/a | no target |
| P01_GOLD | 625 | 51.8% | 51.8% | +0.0 | 70% | ❌ 18 pts to go |
| P02 | 403 | 57.1% | 57.1% | -0.1 | 70% | ❌ 13 pts to go |
| P03 | 209 | 57.4% | 57.4% | +0.2 | 70% | ❌ 13 pts to go |
| P04 | 1568 | 52.0% | 52.0% | +0.0 | 65% | ❌ 13 pts to go |
| P05 | 378 | 33.3% | 33.3% | -1.3 | 60% | ❌ 27 pts to go |
| P06M | 143 | 32.2% | 32.2% | +1.8 | n/a | no target |
| P06T | 8765 | 26.0% | 26.0% | +22.5 | n/a | no target |
| P06 | 220 | 50.5% | 50.5% | -9.1 | 40% | ✅ met |
| P07 | 443 | 50.1% | 50.1% | -17.8 | 85% | ❌ 35 pts to go |
| P08 | 8765 | 40.6% | 40.6% | -27.5 | 85% | ❌ 44 pts to go |
| P09 | 349 | 53.6% | 53.6% | -1.8 | 85% | ❌ 31 pts to go |
| P10R | 30880 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2746 | 60.5% | 60.5% | -5.8 | 85% | ❌ 24 pts to go |
| P11 | 1309 | 25.1% | 25.1% | -29.8 | 75% | ❌ 50 pts to go |
| P12 | 8 | 12.5% | 12.5% | -3.3 | n/a | no target |
| P13 | 13602 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 93.3% | 93.3% | -1.1 | n/a | no target |
| P01T | 136 | 93.4% | 93.4% | +3.2 | n/a | no target |
| P01_GOLD | 625 | 89.4% | 89.4% | +0.0 | 90% | 🟡 1 pts to go |
| P02 | 403 | 87.8% | 87.8% | +0.2 | 90% | 🟡 2 pts to go |
| P03 | 209 | 90.0% | 90.0% | +0.1 | 90% | ✅ met |
| P04 | 1568 | 81.2% | 81.2% | -0.1 | 85% | 🟡 4 pts to go |
| P05 | 378 | 50.3% | 50.3% | -0.7 | 70% | ❌ 20 pts to go |
| P06M | 143 | 64.3% | 64.3% | -3.6 | n/a | no target |
| P06T | 8765 | 91.3% | 91.3% | +13.4 | n/a | no target |
| P06 | 220 | 97.7% | 97.7% | +0.7 | 50% | ✅ met |
| P07 | 443 | 98.2% | 98.2% | +1.4 | 100% | 🟡 2 pts to go |
| P08 | 8765 | 98.7% | 98.7% | +2.6 | 100% | 🟡 1 pts to go |
| P09 | 349 | 79.7% | 79.7% | -0.1 | 100% | ❌ 20 pts to go |
| P10R | 30880 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2746 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1309 | 97.5% | 97.5% | +4.5 | 100% | 🟡 2 pts to go |
| P12 | 8 | 25.0% | 25.0% | -17.1 | n/a | no target |
| P13 | 13602 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 60.0% | 60.0% | +10.0 | n/a | no target |
| P01T | 136 | 41.2% | 41.2% | -4.5 | n/a | no target |
| P01_GOLD | 625 | 45.8% | 45.8% | +0.1 | 70% | ❌ 24 pts to go |
| P02 | 403 | 51.6% | 51.6% | +0.1 | 75% | ❌ 23 pts to go |
| P03 | 209 | 51.7% | 51.7% | +0.3 | 75% | ❌ 23 pts to go |
| P04 | 1568 | 42.9% | 42.9% | +0.0 | 70% | ❌ 27 pts to go |
| P05 | 378 | 24.1% | 24.1% | -0.4 | 55% | ❌ 31 pts to go |
| P06M | 143 | 17.5% | 17.5% | +1.4 | n/a | no target |
| P06T | 8765 | 18.9% | 18.9% | +16.0 | n/a | no target |
| P06 | 220 | 37.7% | 37.7% | -3.3 | n/a | no target |
| P07 | 443 | 36.1% | 36.1% | -0.8 | 70% | ❌ 34 pts to go |
| P08 | 8765 | 36.7% | 36.7% | -12.0 | 75% | ❌ 38 pts to go |
| P09 | 349 | 51.3% | 51.3% | -0.7 | 85% | ❌ 34 pts to go |
| P10R | 30880 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2746 | 46.4% | 46.4% | -4.9 | 80% | ❌ 34 pts to go |
| P11 | 1309 | 19.3% | 19.3% | -21.2 | 70% | ❌ 51 pts to go |
| P12 | 8 | 25.0% | 25.0% | -6.6 | n/a | no target |
| P13 | 13602 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 93.3% | 93.3% | -1.1 | n/a | no target |
| P01T | 136 | 81.6% | 81.6% | -7.5 | n/a | no target |
| P01_GOLD | 625 | 79.8% | 79.8% | +0.0 | 90% | ❌ 10 pts to go |
| P02 | 403 | 77.4% | 77.4% | +0.2 | 90% | ❌ 13 pts to go |
| P03 | 209 | 81.8% | 81.8% | +0.1 | 90% | 🟡 8 pts to go |
| P04 | 1568 | 70.8% | 70.8% | -0.1 | 85% | ❌ 14 pts to go |
| P05 | 378 | 47.6% | 47.6% | -0.8 | 75% | ❌ 27 pts to go |
| P06M | 143 | 64.3% | 64.3% | -3.6 | n/a | no target |
| P06T | 8765 | 53.3% | 53.3% | -23.8 | n/a | no target |
| P06 | 220 | 74.5% | 74.5% | -14.1 | n/a | no target |
| P07 | 443 | 67.7% | 67.7% | -22.8 | 100% | ❌ 32 pts to go |
| P08 | 8765 | 53.6% | 53.6% | -35.4 | 100% | ❌ 46 pts to go |
| P09 | 349 | 61.3% | 61.3% | -1.2 | n/a | no target |
| P10R | 30880 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2746 | 80.6% | 80.6% | -8.4 | 100% | ❌ 19 pts to go |
| P11 | 1309 | 33.0% | 33.0% | -41.5 | n/a | no target |
| P12 | 8 | 25.0% | 25.0% | -11.8 | n/a | no target |
| P13 | 13602 | 70.1% | 70.1% | -12.6 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 136 | 16.2% | 16.2% | -5.5 | n/a | no target · QC vendors: 3 rows, 100.0% filled |
| P01_GOLD | 625 | 48.0% | 48.0% | +0.1 | 95% | ❌ 47 pts to go · QC vendors: 52 rows, 98.1% filled |
| P02 | 403 | 68.5% | 68.5% | -0.1 | 95% | ❌ 26 pts to go · QC vendors: 107 rows, 100.0% filled |
| P03 | 209 | 55.5% | 55.5% | -0.3 | 95% | ❌ 40 pts to go · QC vendors: 17 rows, 100.0% filled |
| P04 | 1568 | 60.1% | 60.1% | -0.1 | 95% | ❌ 35 pts to go · QC vendors: 435 rows, 98.6% filled |
| P05 | 378 | 15.1% | 15.1% | +0.3 | n/a | no target · QC vendors: 31 rows, 93.5% filled |
| P06M | 143 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 8765 | 31.9% | 31.9% | -24.0 | n/a | no target · QC vendors: 1179 rows, 100.0% filled |
| P06 | 220 | 20.0% | 20.0% | -6.5 | n/a | no target · QC vendors: 20 rows, 100.0% filled |
| P07 | 443 | 13.1% | 13.1% | -8.3 | n/a | no target · QC vendors: 32 rows, 96.9% filled |
| P08 | 8765 | 10.9% | 10.9% | -18.0 | n/a | no target · QC vendors: 643 rows, 99.4% filled |
| P09 | 349 | 80.2% | 80.2% | +0.1 | 95% | ❌ 15 pts to go · QC vendors: 137 rows, 99.3% filled |
| P10R | 30880 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2746 | 19.3% | 19.3% | -4.1 | n/a | no target · QC vendors: 409 rows, 97.6% filled |
| P11 | 1309 | 11.8% | 11.8% | -17.5 | n/a | no target · QC vendors: 96 rows, 99.0% filled |
| P12 | 8 | 62.5% | 62.5% | -11.2 | n/a | no target · QC vendors: 1 rows, 100.0% filled |
| P13 | 13602 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 73.3% | 73.3% | +12.2 | n/a | no target · vendors with a registry record: 11 rows, 100.0% filled |
| P01T | 136 | 44.9% | 44.9% | -18.1 | n/a | no target · vendors with a registry record: 61 rows, 100.0% filled |
| P01_GOLD | 625 | 83.4% | 83.4% | -0.1 | 100% | ❌ 17 pts to go · vendors with a registry record: 521 rows, 100.0% filled |
| P02 | 403 | 89.1% | 89.1% | +0.0 | 100% | ❌ 11 pts to go · vendors with a registry record: 359 rows, 100.0% filled |
| P03 | 209 | 89.0% | 89.0% | +0.1 | 100% | ❌ 11 pts to go · vendors with a registry record: 186 rows, 100.0% filled |
| P04 | 1568 | 81.3% | 81.3% | -0.1 | 100% | ❌ 19 pts to go · vendors with a registry record: 1275 rows, 100.0% filled |
| P05 | 378 | 62.2% | 62.2% | +0.5 | n/a | no target · vendors with a registry record: 235 rows, 100.0% filled |
| P06M | 143 | 23.1% | 23.1% | +2.3 | n/a | no target · vendors with a registry record: 33 rows, 100.0% filled |
| P06T | 8765 | 40.8% | 40.8% | -37.4 | n/a | no target · vendors with a registry record: 3575 rows, 100.0% filled |
| P06 | 220 | 40.5% | 40.5% | -17.3 | n/a | no target · vendors with a registry record: 89 rows, 100.0% filled |
| P07 | 443 | 29.8% | 29.8% | -24.6 | n/a | no target · vendors with a registry record: 132 rows, 100.0% filled |
| P08 | 8765 | 19.2% | 19.2% | -35.1 | n/a | no target · vendors with a registry record: 1681 rows, 100.0% filled |
| P09 | 349 | 92.0% | 92.0% | +0.4 | n/a | no target · vendors with a registry record: 321 rows, 100.0% filled |
| P10R | 30880 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2746 | 36.2% | 36.2% | -7.5 | n/a | no target · vendors with a registry record: 994 rows, 100.0% filled |
| P11 | 1309 | 22.4% | 22.4% | -35.8 | n/a | no target · vendors with a registry record: 293 rows, 100.0% filled |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 8 rows, 100.0% filled |
| P13 | 13602 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 93.3% | 93.3% | -1.1 | 90% | ✅ met |
| P01T | 136 | 86.0% | 86.0% | -8.6 | 90% | 🟡 4 pts to go |
| P01_GOLD | 625 | 85.0% | 85.0% | +0.4 | 95% | 🟡 10 pts to go |
| P02 | 403 | 90.6% | 90.6% | +0.0 | 95% | 🟡 4 pts to go |
| P03 | 209 | 83.7% | 83.7% | +0.5 | 85% | 🟡 1 pts to go |
| P04 | 1568 | 79.1% | 79.1% | +0.3 | 90% | ❌ 11 pts to go |
| P05 | 378 | 75.9% | 75.9% | +0.1 | 75% | ✅ met |
| P06M | 143 | 88.1% | 88.1% | -0.6 | n/a | no target |
| P06T | 8765 | 48.6% | 48.6% | -15.8 | n/a | no target |
| P06 | 220 | 47.7% | 47.7% | -8.9 | 80% | ❌ 32 pts to go |
| P07 | 443 | 43.1% | 43.1% | -10.5 | 80% | ❌ 37 pts to go |
| P08 | 8765 | 23.2% | 23.2% | -13.6 | 75% | ❌ 52 pts to go |
| P09 | 349 | 78.8% | 78.8% | -2.0 | 95% | ❌ 16 pts to go |
| P10R | 30880 | 42.8% | 42.8% |  | n/a | no target |
| P10 | 2746 | 31.3% | 31.3% | -0.7 | 70% | ❌ 39 pts to go |
| P11 | 1309 | 10.8% | 10.8% | -14.1 | 65% | ❌ 54 pts to go |
| P12 | 8 | 75.0% | 75.0% | +1.3 | 80% | 🟡 5 pts to go |
| P13 | 13602 | 72.2% | 72.2% | +19.7 | 60% | ✅ met |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 46.7% | 46.7% | +7.8 | 50% | 🟡 3 pts to go |
| P01T | 136 | 19.1% | 19.1% | -1.6 | n/a | no target |
| P01_GOLD | 625 | 20.6% | 20.6% | +0.2 | 40% | ❌ 19 pts to go |
| P02 | 403 | 21.6% | 21.6% | -0.2 | 40% | ❌ 18 pts to go |
| P03 | 209 | 26.8% | 26.8% | -0.1 | 40% | ❌ 13 pts to go |
| P04 | 1568 | 27.6% | 27.6% | +0.0 | 40% | ❌ 12 pts to go |
| P05 | 378 | 23.0% | 23.0% | +0.1 | 25% | 🟡 2 pts to go |
| P06M | 143 | 25.9% | 25.9% | +0.3 | n/a | no target |
| P06T | 8765 | 22.3% | 22.3% | -8.6 | n/a | no target |
| P06 | 220 | 9.1% | 9.1% | -1.7 | 35% | ❌ 26 pts to go |
| P07 | 443 | 10.8% | 10.8% | +0.5 | 35% | ❌ 24 pts to go |
| P08 | 8765 | 8.7% | 8.7% | -2.4 | 35% | ❌ 26 pts to go |
| P09 | 349 | 16.9% | 16.9% | -0.2 | n/a | no target |
| P10R | 30880 | 19.4% | 19.4% |  | n/a | no target |
| P10 | 2746 | 9.5% | 9.5% | -0.1 | 30% | ❌ 20 pts to go |
| P11 | 1309 | 3.2% | 3.2% | -5.2 | n/a | no target |
| P12 | 8 | 12.5% | 12.5% | +2.0 | n/a | no target |
| P13 | 13602 | 39.7% | 39.7% | +13.8 | 30% | ✅ met |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 100.0% | 100.0% | +5.6 | 100% | ✅ met |
| P01T | 136 | 94.1% | 94.1% | +0.6 | 100% | 🟡 6 pts to go |
| P01_GOLD | 625 | 90.2% | 90.2% | +2.5 | 100% | 🟡 10 pts to go |
| P02 | 403 | 97.5% | 97.5% | +0.7 | 100% | 🟡 2 pts to go |
| P03 | 209 | 92.8% | 92.8% | +1.0 | 100% | 🟡 7 pts to go |
| P04 | 1568 | 93.0% | 93.0% | +2.0 | 100% | 🟡 7 pts to go |
| P05 | 378 | 87.3% | 87.3% | +2.4 | 100% | ❌ 13 pts to go |
| P06M | 143 | 79.7% | 79.7% | +7.7 | n/a | no target |
| P06T | 8765 | 81.5% | 81.5% | +1.3 | n/a | no target |
| P06 | 220 | 72.3% | 72.3% | +3.6 | 95% | ❌ 23 pts to go |
| P07 | 443 | 76.1% | 76.1% | +5.5 | 95% | ❌ 19 pts to go |
| P08 | 8765 | 65.1% | 65.1% | -1.1 | 95% | ❌ 30 pts to go |
| P09 | 349 | 96.3% | 96.3% | +0.8 | 100% | 🟡 4 pts to go |
| P10R | 30880 | 77.0% | 77.0% |  | n/a | no target |
| P10 | 2746 | 64.1% | 64.1% | -1.1 | 95% | ❌ 31 pts to go |
| P11 | 1309 | 24.1% | 24.1% | -10.3 | 80% | ❌ 56 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 13602 | 88.3% | 88.3% | +12.2 | 95% | 🟡 7 pts to go |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 86.7% | 86.7% | -2.2 | n/a | no target |
| P01T | 136 | 77.9% | 77.9% | -2.5 | n/a | no target |
| P01_GOLD | 625 | 70.4% | 70.4% | +0.2 | 90% | ❌ 20 pts to go |
| P02 | 403 | 79.7% | 79.7% | +0.0 | 95% | ❌ 15 pts to go |
| P03 | 209 | 73.2% | 73.2% | -0.4 | 95% | ❌ 22 pts to go |
| P04 | 1568 | 84.7% | 84.7% | -0.2 | 95% | ❌ 10 pts to go |
| P05 | 378 | 74.6% | 74.6% | -0.4 | 90% | ❌ 15 pts to go |
| P06M | 143 | 83.2% | 83.2% | -0.7 | n/a | no target |
| P06T | 8765 | 74.5% | 74.5% | -2.8 | n/a | no target |
| P06 | 220 | 55.5% | 55.5% | -9.0 | 95% | ❌ 40 pts to go |
| P07 | 443 | 50.8% | 50.8% | -15.5 | 90% | ❌ 39 pts to go |
| P08 | 8765 | 40.2% | 40.2% | -34.5 | 95% | ❌ 55 pts to go |
| P09 | 349 | 88.0% | 88.0% | -1.0 | 100% | ❌ 12 pts to go |
| P10R | 30880 | 77.7% | 77.7% |  | n/a | no target |
| P10 | 2746 | 61.8% | 61.8% | -9.7 | 95% | ❌ 33 pts to go |
| P11 | 1309 | 19.0% | 19.0% | -9.9 | 75% | ❌ 56 pts to go |
| P12 | 8 | 87.5% | 87.5% | -2.0 | n/a | no target |
| P13 | 13602 | 78.3% | 78.3% | -1.0 | 95% | ❌ 17 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 73.3% | 73.3% | -4.5 | n/a | no target |
| P01T | 136 | 88.2% | 88.2% | -3.1 | 95% | 🟡 7 pts to go |
| P01_GOLD | 625 | 82.2% | 82.2% | +0.0 | 90% | 🟡 8 pts to go |
| P02 | 403 | 88.3% | 88.3% | -0.1 | 95% | 🟡 7 pts to go |
| P03 | 209 | 84.2% | 84.2% | -0.4 | 95% | ❌ 11 pts to go |
| P04 | 1568 | 84.2% | 84.2% | +0.0 | 90% | 🟡 6 pts to go |
| P05 | 378 | 89.7% | 89.7% | +0.1 | 95% | 🟡 5 pts to go |
| P06M | 143 | 85.3% | 85.3% | +0.2 | n/a | no target |
| P06T | 8765 | 83.3% | 83.3% | -10.8 | n/a | no target |
| P06 | 220 | 75.0% | 75.0% | -15.4 | 100% | ❌ 25 pts to go |
| P07 | 443 | 64.6% | 64.6% | -23.5 | 100% | ❌ 35 pts to go |
| P08 | 8765 | 46.5% | 46.5% | -44.2 | 100% | ❌ 54 pts to go |
| P09 | 349 | 71.9% | 71.9% | -2.1 | n/a | no target |
| P10R | 30880 | 84.7% | 84.7% |  | n/a | no target |
| P10 | 2746 | 78.9% | 78.9% | -11.2 | 100% | ❌ 21 pts to go |
| P11 | 1309 | 25.0% | 25.0% | -11.5 | 80% | ❌ 55 pts to go |
| P12 | 8 | 87.5% | 87.5% | +3.3 | n/a | no target |
| P13 | 13602 | 78.1% | 78.1% | -6.1 | 95% | ❌ 17 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 20.0% | 20.0% | +3.3 | n/a | no target |
| P01T | 136 | 18.4% | 18.4% | -5.5 | n/a | no target |
| P01_GOLD | 625 | 14.2% | 14.2% | -0.1 | 25% | ❌ 11 pts to go |
| P02 | 403 | 27.8% | 27.8% | +0.1 | 40% | ❌ 12 pts to go |
| P03 | 209 | 10.5% | 10.5% | -0.1 | 20% | 🟡 10 pts to go |
| P04 | 1568 | 7.4% | 7.4% | +0.0 | 20% | ❌ 13 pts to go |
| P05 | 378 | 4.0% | 4.0% | +0.1 | 15% | ❌ 11 pts to go |
| P06M | 143 | 4.9% | 4.9% | +0.1 | n/a | no target |
| P06T | 8765 | 1.4% | 1.4% | -1.8 | n/a | no target |
| P06 | 220 | 5.5% | 5.5% | +0.1 | n/a | no target |
| P07 | 443 | 6.5% | 6.5% | +0.2 | n/a | no target |
| P08 | 8765 | 0.5% | 0.5% | -0.5 | n/a | no target |
| P09 | 349 | 7.4% | 7.4% | -0.5 | n/a | no target |
| P10R | 30880 | 0.6% | 0.6% |  | n/a | no target |
| P10 | 2746 | 1.0% | 1.0% | -0.3 | n/a | no target |
| P11 | 1309 | 1.0% | 1.0% | -1.5 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | -10.5 | n/a | no target |
| P13 | 13602 | 0.8% | 0.8% | +0.2 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 40.0% | 40.0% | +1.1 | n/a | no target |
| P01T | 136 | 39.0% | 39.0% | +4.2 | 70% | ❌ 31 pts to go |
| P01_GOLD | 625 | 43.4% | 43.4% | +0.1 | 80% | ❌ 37 pts to go |
| P02 | 403 | 64.3% | 64.3% | +0.2 | 90% | ❌ 26 pts to go |
| P03 | 209 | 23.4% | 23.4% | +0.3 | 60% | ❌ 37 pts to go |
| P04 | 1568 | 50.6% | 50.6% | +0.1 | 85% | ❌ 34 pts to go |
| P05 | 378 | 13.2% | 13.2% | +0.2 | 50% | ❌ 37 pts to go |
| P06M | 143 | 6.3% | 6.3% | -0.2 | n/a | no target |
| P06T | 8765 | 1.7% | 1.7% | -1.0 | n/a | no target |
| P06 | 220 | 18.2% | 18.2% | +0.1 | n/a | no target |
| P07 | 443 | 13.1% | 13.1% | -5.9 | n/a | no target |
| P08 | 8765 | 0.2% | 0.2% | -0.4 | n/a | no target |
| P09 | 349 | 78.8% | 78.8% | -1.8 | 95% | ❌ 16 pts to go |
| P10R | 30880 | 0.9% | 0.9% |  | n/a | no target |
| P10 | 2746 | 2.7% | 2.7% | -0.4 | n/a | no target |
| P11 | 1309 | 21.8% | 21.8% | -7.5 | n/a | no target |
| P12 | 8 | 25.0% | 25.0% | -6.6 | n/a | no target |
| P13 | 13602 | 1.1% | 1.1% | +0.1 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 136 | 16.9% | 16.9% | +0.6 | n/a | no target |
| P01_GOLD | 625 | 33.9% | 33.9% | -0.1 | 70% | ❌ 36 pts to go |
| P02 | 403 | 44.4% | 44.4% | +0.1 | 75% | ❌ 31 pts to go |
| P03 | 209 | 23.4% | 23.4% | +0.3 | 55% | ❌ 32 pts to go |
| P04 | 1568 | 50.6% | 50.6% | +0.1 | 75% | ❌ 24 pts to go |
| P05 | 378 | 11.9% | 11.9% | +0.2 | 50% | ❌ 38 pts to go |
| P06M | 143 | 2.1% | 2.1% | +0.3 | n/a | no target |
| P06T | 8765 | 1.1% | 1.1% | -0.4 | n/a | no target |
| P06 | 220 | 11.4% | 11.4% | +1.2 | n/a | no target |
| P07 | 443 | 7.2% | 7.2% | -3.1 | n/a | no target |
| P08 | 8765 | 0.2% | 0.2% | -0.3 | n/a | no target |
| P09 | 349 | 75.9% | 75.9% | -1.8 | 95% | ❌ 19 pts to go |
| P10R | 30880 | 0.6% | 0.6% |  | n/a | no target |
| P10 | 2746 | 1.5% | 1.5% | -0.3 | n/a | no target |
| P11 | 1309 | 22.1% | 22.1% | -6.8 | n/a | no target |
| P12 | 8 | 12.5% | 12.5% | -3.3 | n/a | no target |
| P13 | 13602 | 0.7% | 0.7% | +0.1 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 20.0% | 20.0% | +3.3 | n/a | no target |
| P01T | 136 | 14.7% | 14.7% | -4.9 | n/a | no target |
| P01_GOLD | 625 | 57.9% | 58.1% | +0.0 | 80% | ❌ 22 pts to go |
| P02 | 403 | 52.4% | 52.6% | +0.2 | 75% | ❌ 23 pts to go |
| P03 | 209 | 45.5% | 45.5% | +0.3 | 70% | ❌ 24 pts to go |
| P04 | 1568 | 48.9% | 49.9% | +0.2 | 70% | ❌ 21 pts to go |
| P05 | 378 | 16.7% | 16.7% | +0.3 | 50% | ❌ 33 pts to go |
| P06M | 143 | 4.2% | 4.2% | +0.0 | n/a | no target |
| P06T | 8765 | 0.9% | 1.0% | -0.7 | n/a | no target |
| P06 | 220 | 20.0% | 20.0% | -4.1 | n/a | no target |
| P07 | 443 | 3.4% | 3.4% | -1.8 | n/a | no target |
| P08 | 8765 | 0.4% | 0.4% | -0.6 | n/a | no target |
| P09 | 349 | 44.1% | 44.4% | +0.0 | 80% | ❌ 36 pts to go |
| P10R | 30880 | 0.3% | 0.3% |  | n/a | no target |
| P10 | 2746 | 1.3% | 1.5% | -0.2 | n/a | no target |
| P11 | 1309 | 6.7% | 6.8% | -10.0 | n/a | no target |
| P12 | 8 | 25.0% | 25.0% | -6.6 | n/a | no target |
| P13 | 13602 | 0.5% | 0.5% | +0.2 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 40.0% | 40.0% | +1.1 | n/a | no target |
| P01T | 136 | 41.9% | 41.9% | -14.6 | 60% | ❌ 18 pts to go |
| P01_GOLD | 625 | 63.7% | 63.7% | +0.2 | 70% | 🟡 6 pts to go |
| P02 | 403 | 43.7% | 43.7% | -0.1 | 50% | 🟡 6 pts to go |
| P03 | 209 | 55.0% | 55.0% | -0.3 | 55% | ✅ met |
| P04 | 1568 | 23.0% | 23.0% | +0.1 | 40% | ❌ 17 pts to go |
| P05 | 378 | 17.7% | 17.7% | +0.3 | 40% | ❌ 22 pts to go |
| P06M | 143 | 13.3% | 13.3% | -3.4 | n/a | no target |
| P06T | 8765 | 3.7% | 3.7% | -8.8 | n/a | no target |
| P06 | 220 | 22.3% | 22.3% | -8.4 | n/a | no target |
| P07 | 443 | 9.5% | 9.5% | -6.8 | n/a | no target |
| P08 | 8765 | 1.8% | 1.8% | -2.9 | n/a | no target |
| P09 | 349 | 5.4% | 5.4% | -0.4 | n/a | no target |
| P10R | 30880 | 0.3% | 0.3% |  | n/a | no target |
| P10 | 2746 | 3.6% | 3.6% | -0.3 | n/a | no target |
| P11 | 1309 | 2.8% | 2.8% | -4.8 | n/a | no target |
| P12 | 8 | 25.0% | 25.0% | +9.2 | n/a | no target |
| P13 | 13602 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 46.7% | 46.7% | +2.3 | n/a | no target |
| P01T | 136 | 50.0% | 50.0% | -19.6 | 65% | ❌ 15 pts to go |
| P01_GOLD | 625 | 69.3% | 69.3% | +0.1 | 70% | 🟡 1 pts to go |
| P02 | 403 | 26.1% | 26.1% | -0.1 | 50% | ❌ 24 pts to go |
| P03 | 209 | 56.0% | 56.0% | -0.2 | 60% | 🟡 4 pts to go |
| P04 | 1568 | 9.9% | 9.9% | +0.0 | 40% | ❌ 30 pts to go |
| P05 | 378 | 21.7% | 21.7% | +0.3 | 45% | ❌ 23 pts to go |
| P06M | 143 | 6.3% | 6.3% | -0.8 | n/a | no target |
| P06T | 8765 | 1.3% | 1.3% | -3.0 | n/a | no target |
| P06 | 220 | 37.7% | 37.7% | -10.5 | n/a | no target |
| P07 | 443 | 13.1% | 13.1% | -10.7 | n/a | no target |
| P08 | 8765 | 0.8% | 0.8% | -1.6 | n/a | no target |
| P09 | 349 | 9.2% | 9.2% | +0.5 | n/a | no target |
| P10R | 30880 | 0.1% | 0.1% |  | n/a | no target |
| P10 | 2746 | 2.0% | 2.0% | -0.1 | n/a | no target |
| P11 | 1309 | 2.4% | 2.4% | -4.4 | n/a | no target |
| P12 | 8 | 12.5% | 12.5% | +2.0 | n/a | no target |
| P13 | 13602 | 0.3% | 0.3% | +0.1 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 13.3% | 13.3% | +2.2 | n/a | no target |
| P01T | 136 | 30.9% | 30.9% | -13.7 | n/a | no target |
| P01_GOLD | 625 | 49.8% | 49.8% | +0.0 | 50% | 🟡 0 pts to go |
| P02 | 403 | 42.7% | 42.7% | +0.1 | n/a | no target |
| P03 | 209 | 58.4% | 58.4% | -0.3 | 60% | 🟡 2 pts to go |
| P04 | 1568 | 26.3% | 26.3% | -0.1 | n/a | no target |
| P05 | 378 | 16.7% | 16.7% | +0.0 | n/a | no target |
| P06M | 143 | 4.2% | 4.2% | +0.0 | n/a | no target |
| P06T | 8765 | 1.4% | 1.4% | -2.6 | n/a | no target |
| P06 | 220 | 28.2% | 28.2% | -7.3 | n/a | no target |
| P07 | 443 | 10.6% | 10.6% | -8.1 | n/a | no target |
| P08 | 8765 | 0.5% | 0.5% | -1.0 | n/a | no target |
| P09 | 349 | 19.5% | 19.5% | +0.6 | n/a | no target |
| P10R | 30880 | 0.3% | 0.3% |  | n/a | no target |
| P10 | 2746 | 2.2% | 2.2% | -0.2 | n/a | no target |
| P11 | 1309 | 2.8% | 2.8% | -5.0 | n/a | no target |
| P12 | 8 | 12.5% | 12.5% | -8.6 | n/a | no target |
| P13 | 13602 | 0.7% | 0.7% | +0.3 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 26.7% | 26.7% | -1.1 | 15% | ✅ met |
| P01T | 136 | 21.3% | 21.3% | -8.0 | 15% | ✅ met |
| P01_GOLD | 625 | 35.4% | 35.4% | +0.3 | 40% | 🟡 5 pts to go |
| P02 | 403 | 13.6% | 13.9% | -0.3 | 25% | ❌ 11 pts to go |
| P03 | 209 | 21.5% | 21.5% | -0.1 | 25% | 🟡 4 pts to go |
| P04 | 1568 | 5.2% | 5.2% | +0.0 | 15% | 🟡 10 pts to go |
| P05 | 378 | 7.9% | 7.9% | -0.2 | 15% | 🟡 7 pts to go |
| P06M | 143 | 5.6% | 5.6% | -0.4 | 15% | 🟡 9 pts to go |
| P06T | 8765 | 0.7% | 0.7% | -0.8 | 15% | ❌ 14 pts to go |
| P06 | 220 | 8.6% | 8.6% | -1.6 | 15% | 🟡 6 pts to go |
| P07 | 443 | 4.3% | 4.3% | -2.4 | 15% | ❌ 11 pts to go |
| P08 | 8765 | 0.3% | 0.3% | -0.6 | 15% | ❌ 15 pts to go |
| P09 | 349 | 0.9% | 0.9% | +0.1 | 15% | ❌ 14 pts to go |
| P10R | 30880 | 0.6% | 0.6% |  | 15% | ❌ 14 pts to go |
| P10 | 2746 | 1.4% | 1.4% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 1309 | 0.5% | 0.5% | -0.8 | 15% | ❌ 14 pts to go |
| P12 | 8 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 13602 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 13.3% | 13.3% | +2.2 | 15% | 🟡 2 pts to go |
| P01T | 136 | 23.5% | 23.5% | -9.1 | 25% | 🟡 2 pts to go |
| P01_GOLD | 625 | 29.1% | 29.1% | -0.1 | 25% | ✅ met |
| P02 | 403 | 28.0% | 28.0% | +0.0 | 15% | ✅ met |
| P03 | 209 | 25.8% | 25.8% | -0.2 | 15% | ✅ met |
| P04 | 1568 | 8.1% | 8.1% | -0.1 | 15% | 🟡 7 pts to go |
| P05 | 378 | 11.9% | 11.9% | -0.1 | 15% | 🟡 3 pts to go |
| P06M | 143 | 2.1% | 2.1% | -0.3 | 15% | ❌ 13 pts to go |
| P06T | 8765 | 0.8% | 0.8% | -1.9 | 15% | ❌ 14 pts to go |
| P06 | 220 | 8.2% | 8.2% | -3.8 | 15% | 🟡 7 pts to go |
| P07 | 443 | 4.3% | 4.3% | -3.2 | 15% | ❌ 11 pts to go |
| P08 | 8765 | 0.3% | 0.3% | -0.7 | 15% | ❌ 15 pts to go |
| P09 | 349 | 0.9% | 0.9% | +0.1 | 15% | ❌ 14 pts to go |
| P10R | 30880 | 0.1% | 0.1% |  | 15% | ❌ 15 pts to go |
| P10 | 2746 | 1.3% | 1.3% | -0.1 | 15% | ❌ 14 pts to go |
| P11 | 1309 | 1.8% | 1.8% | -3.3 | 15% | ❌ 13 pts to go |
| P12 | 8 | 25.0% | 25.0% | -1.3 | 15% | ✅ met |
| P13 | 13602 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 6.7% | 6.7% | +1.1 | 20% | ❌ 13 pts to go |
| P01T | 136 | 7.4% | 7.4% | -2.4 | 20% | ❌ 13 pts to go |
| P01_GOLD | 625 | 4.3% | 4.3% | +0.0 | 20% | ❌ 16 pts to go |
| P02 | 403 | 1.5% | 1.5% | +0.0 | 20% | ❌ 18 pts to go |
| P03 | 209 | 1.9% | 1.9% | +0.0 | 20% | ❌ 18 pts to go |
| P04 | 1568 | 1.0% | 1.0% | +0.0 | 20% | ❌ 19 pts to go |
| P05 | 378 | 1.1% | 1.1% | +0.1 | 20% | ❌ 19 pts to go |
| P06M | 143 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 8765 | 0.1% | 0.1% | -0.1 | 20% | ❌ 20 pts to go |
| P06 | 220 | 2.3% | 2.3% | -1.3 | 20% | ❌ 18 pts to go |
| P07 | 443 | 0.5% | 0.5% | -0.3 | 20% | ❌ 20 pts to go |
| P08 | 8765 | 0.1% | 0.1% | -0.1 | 20% | ❌ 20 pts to go |
| P09 | 349 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10R | 30880 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P10 | 2746 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 1309 | 0.2% | 0.2% | -0.4 | 20% | ❌ 20 pts to go |
| P12 | 8 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 13602 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 6.7% | 6.7% | +1.1 | 15% | 🟡 8 pts to go |
| P01T | 136 | 5.1% | 5.1% | -2.5 | 15% | 🟡 10 pts to go |
| P01_GOLD | 625 | 10.6% | 10.6% | +0.0 | 15% | 🟡 4 pts to go |
| P02 | 403 | 13.4% | 13.4% | +0.0 | 15% | 🟡 2 pts to go |
| P03 | 209 | 23.9% | 23.9% | -0.1 | 15% | ✅ met |
| P04 | 1568 | 4.5% | 4.5% | -0.1 | 15% | ❌ 10 pts to go |
| P05 | 378 | 2.9% | 2.9% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 143 | 2.1% | 2.1% | -0.3 | 15% | ❌ 13 pts to go |
| P06T | 8765 | 0.4% | 0.4% | -1.0 | 15% | ❌ 15 pts to go |
| P06 | 220 | 4.5% | 4.5% | -0.9 | 15% | ❌ 10 pts to go |
| P07 | 443 | 2.3% | 2.3% | -1.3 | 15% | ❌ 13 pts to go |
| P08 | 8765 | 0.3% | 0.3% | -0.4 | 15% | ❌ 15 pts to go |
| P09 | 349 | 0.6% | 0.6% | +0.1 | 15% | ❌ 14 pts to go |
| P10R | 30880 | 0.1% | 0.1% |  | 15% | ❌ 15 pts to go |
| P10 | 2746 | 0.7% | 0.7% | -0.1 | 15% | ❌ 14 pts to go |
| P11 | 1309 | 0.8% | 0.8% | -1.3 | 15% | ❌ 14 pts to go |
| P12 | 8 | 0.0% | 0.0% | -5.3 | 15% | ❌ 15 pts to go |
| P13 | 13602 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 13.3% | 13.3% | +2.2 | 20% | 🟡 7 pts to go |
| P01T | 136 | 28.7% | 28.7% | -12.6 | 40% | ❌ 11 pts to go |
| P01_GOLD | 625 | 45.8% | 45.8% | +0.0 | 40% | ✅ met |
| P02 | 403 | 48.6% | 48.6% | +0.1 | 20% | ✅ met |
| P03 | 209 | 55.5% | 55.5% | -0.3 | 35% | ✅ met |
| P04 | 1568 | 30.2% | 30.2% | -0.1 | 20% | ✅ met |
| P05 | 378 | 16.7% | 16.7% | +0.0 | 20% | 🟡 3 pts to go |
| P06M | 143 | 4.9% | 4.9% | +0.7 | 20% | ❌ 15 pts to go |
| P06T | 8765 | 1.8% | 1.8% | -2.7 | 20% | ❌ 18 pts to go |
| P06 | 220 | 27.7% | 27.7% | -7.8 | 20% | ✅ met |
| P07 | 443 | 9.0% | 9.0% | -5.7 | 20% | ❌ 11 pts to go |
| P08 | 8765 | 0.9% | 0.9% | -1.4 | 20% | ❌ 19 pts to go |
| P09 | 349 | 19.8% | 19.8% | -2.2 | 20% | 🟡 0 pts to go |
| P10R | 30880 | 0.4% | 0.4% |  | 20% | ❌ 20 pts to go |
| P10 | 2746 | 2.3% | 2.3% | -0.3 | 20% | ❌ 18 pts to go |
| P11 | 1309 | 3.0% | 3.0% | -5.0 | 20% | ❌ 17 pts to go |
| P12 | 8 | 12.5% | 12.5% | -3.3 | 20% | 🟡 8 pts to go |
| P13 | 13602 | 0.9% | 0.9% | +0.3 | 20% | ❌ 19 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 136 | 0.7% | 0.7% | -0.4 | n/a | no target |
| P01_GOLD | 625 | 69.8% | 69.8% | +0.1 | 95% | ❌ 25 pts to go |
| P02 | 403 | 73.2% | 73.2% | -0.1 | 95% | ❌ 22 pts to go |
| P03 | 209 | 67.0% | 67.0% | -0.3 | 90% | ❌ 23 pts to go |
| P04 | 1568 | 58.5% | 58.5% | +0.1 | 85% | ❌ 26 pts to go |
| P05 | 378 | 35.4% | 35.4% | +0.5 | 75% | ❌ 40 pts to go |
| P06M | 143 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 8765 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 220 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 443 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 8765 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 349 | 90.0% | 90.0% | -0.8 | 100% | 🟡 10 pts to go |
| P10R | 30880 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2746 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1309 | 6.7% | 6.7% | -12.1 | 60% | ❌ 53 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 13602 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 136 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 73.0% | 73.0% | +0.1 | 100% | ❌ 27 pts to go |
| P02 | 403 | 77.2% | 77.2% | +0.0 | 100% | ❌ 23 pts to go |
| P03 | 209 | 74.2% | 74.2% | -0.3 | n/a | no target |
| P04 | 1568 | 60.1% | 60.1% | +0.1 | 95% | ❌ 35 pts to go |
| P05 | 378 | 31.7% | 31.7% | +0.5 | 80% | ❌ 48 pts to go |
| P06M | 143 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 8765 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 220 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 443 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 8765 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 349 | 92.8% | 92.8% | -0.6 | 100% | 🟡 7 pts to go |
| P10R | 30880 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2746 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1309 | 7.2% | 7.2% | -12.8 | n/a | no target |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 13602 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 136 | 0.7% | 0.7% | -0.4 | n/a | no target |
| P01_GOLD | 625 | 51.8% | 51.8% | -0.1 | 85% | ❌ 33 pts to go |
| P02 | 403 | 66.7% | 66.7% | -0.1 | 90% | ❌ 23 pts to go |
| P03 | 209 | 54.5% | 54.5% | -0.3 | 85% | ❌ 30 pts to go |
| P04 | 1568 | 64.2% | 64.2% | +0.1 | 90% | ❌ 26 pts to go |
| P05 | 378 | 34.9% | 34.9% | -0.3 | 75% | ❌ 40 pts to go |
| P06M | 143 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 8765 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 220 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 443 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 8765 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 349 | 86.0% | 86.0% | +0.4 | 95% | 🟡 9 pts to go |
| P10R | 30880 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2746 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1309 | 6.2% | 6.2% | -11.1 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 13602 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 136 | 0.7% | 0.7% | -0.4 | n/a | no target |
| P01_GOLD | 625 | 52.0% | 52.0% | -0.1 | 85% | ❌ 33 pts to go |
| P02 | 403 | 61.0% | 61.0% | -0.1 | 90% | ❌ 29 pts to go |
| P03 | 209 | 56.0% | 56.0% | -0.2 | 85% | ❌ 29 pts to go |
| P04 | 1568 | 54.3% | 54.3% | +0.0 | 90% | ❌ 36 pts to go |
| P05 | 378 | 41.5% | 41.5% | -0.2 | 75% | ❌ 34 pts to go |
| P06M | 143 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 8765 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 220 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 443 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 8765 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 349 | 0.3% | 0.3% | +0.0 | 95% | ❌ 95 pts to go |
| P10R | 30880 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2746 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1309 | 5.1% | 5.1% | -9.0 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 13602 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 136 | 86.8% | 86.8% | +5.3 | n/a | no target |
| P01_GOLD | 625 | 85.8% | 85.8% | +0.1 | 100% | ❌ 14 pts to go |
| P02 | 403 | 81.6% | 81.6% | -0.1 | 100% | ❌ 18 pts to go |
| P03 | 209 | 92.3% | 92.3% | +0.0 | n/a | no target |
| P04 | 1568 | 72.7% | 72.7% | +0.1 | 95% | ❌ 22 pts to go |
| P05 | 378 | 75.4% | 75.4% | -0.1 | 95% | ❌ 20 pts to go |
| P06M | 143 | 0.7% | 0.7% | +0.1 | n/a | no target |
| P06T | 8765 | 89.4% | 89.4% | +6.0 | n/a | no target |
| P06 | 220 | 55.5% | 55.5% | -20.4 | n/a | no target |
| P07 | 443 | 41.8% | 41.8% | -35.2 | n/a | no target |
| P08 | 8765 | 28.1% | 28.1% | -56.8 | n/a | no target |
| P09 | 349 | 98.9% | 98.9% | -0.1 | 100% | 🟡 1 pts to go |
| P10R | 30880 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2746 | 83.6% | 83.6% | -14.8 | n/a | no target |
| P11 | 1309 | 86.0% | 86.0% | -3.9 | n/a | no target |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 13602 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 136 | 86.8% | 86.8% | +5.3 | n/a | no target |
| P01_GOLD | 625 | 89.0% | 89.0% | +0.1 | 100% | ❌ 11 pts to go |
| P02 | 403 | 82.9% | 83.1% | +0.0 | 100% | ❌ 17 pts to go |
| P03 | 209 | 93.8% | 93.8% | +0.0 | n/a | no target |
| P04 | 1568 | 79.1% | 79.1% | +0.1 | 95% | ❌ 16 pts to go |
| P05 | 378 | 89.7% | 89.7% | -0.4 | 70% | ✅ met |
| P06M | 143 | 0.7% | 0.7% | +0.1 | n/a | no target |
| P06T | 8765 | 89.4% | 89.4% | +6.0 | n/a | no target |
| P06 | 220 | 55.5% | 55.5% | -20.4 | n/a | no target |
| P07 | 443 | 41.8% | 41.8% | -35.2 | n/a | no target |
| P08 | 8765 | 28.1% | 28.1% | -56.8 | n/a | no target |
| P09 | 349 | 98.9% | 98.9% | -0.1 | 100% | 🟡 1 pts to go |
| P10R | 30880 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2746 | 83.6% | 83.6% | -14.8 | n/a | no target |
| P11 | 1309 | 86.2% | 86.2% | -4.1 | n/a | no target |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 13602 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 136 | 0.7% | 0.7% | -0.4 | n/a | no target · rows from a source that publishes bids: 4 rows, 25.0% filled |
| P01_GOLD | 625 | 17.3% | 17.3% | +0.0 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 367 rows, 29.4% filled |
| P02 | 403 | 13.2% | 13.2% | +0.1 | n/a | no target · rows from a source that publishes bids: 294 rows, 18.0% filled |
| P03 | 209 | 16.3% | 16.3% | +0.0 | n/a | no target · rows from a source that publishes bids: 140 rows, 24.3% filled |
| P04 | 1568 | 3.7% | 3.7% | +0.0 | n/a | no target · rows from a source that publishes bids: 878 rows, 6.6% filled |
| P05 | 378 | 3.4% | 3.4% | +0.0 | n/a | no target · rows from a source that publishes bids: 53 rows, 24.5% filled |
| P06M | 143 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 8765 | 0.0% | 0.0% | -0.1 | n/a | no target · rows from a source that publishes bids: 34 rows, 5.9% filled |
| P06 | 220 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 443 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 8765 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 349 | 3.4% | 3.4% | +0.3 | n/a | no target · rows from a source that publishes bids: 336 rows, 3.6% filled |
| P10R | 30880 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2746 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1309 | 1.0% | 1.0% | -1.7 | n/a | no target · rows from a source that publishes bids: 91 rows, 14.3% filled |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 8 rows, 0.0% filled |
| P13 | 13602 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 136 | 0.0% | 97.1% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 53.1% | 82.4% | -0.1 | 90% | ❌ 37 pts to go |
| P02 | 403 | 61.0% | 85.6% | -0.1 | 90% | ❌ 29 pts to go |
| P03 | 209 | 56.0% | 75.6% | -0.2 | 90% | ❌ 34 pts to go |
| P04 | 1568 | 45.5% | 85.6% | +0.2 | 90% | ❌ 44 pts to go |
| P05 | 378 | 0.0% | 80.7% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 143 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 8765 | 0.0% | 99.6% | +0.0 | n/a | no target |
| P06 | 220 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 443 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 8765 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 349 | 2.3% | 3.7% | +0.2 | 90% | ❌ 88 pts to go |
| P10R | 30880 | 0.0% | 100.0% |  | n/a | no target |
| P10 | 2746 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1309 | 4.6% | 96.6% | -8.1 | n/a | no target |
| P12 | 8 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 13602 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 136 | 0.7% | 97.8% | +0.7 | n/a | no target |
| P01_GOLD | 625 | 25.9% | 55.2% | -0.1 | 90% | ❌ 64 pts to go |
| P02 | 403 | 60.0% | 84.6% | +0.1 | n/a | no target |
| P03 | 209 | 30.6% | 50.2% | -0.2 | n/a | no target |
| P04 | 1568 | 49.8% | 89.9% | +0.1 | n/a | no target |
| P05 | 378 | 0.5% | 81.2% | +0.0 | n/a | no target |
| P06M | 143 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 8765 | 0.2% | 99.8% | +0.2 | n/a | no target |
| P06 | 220 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 443 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 8765 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 349 | 43.6% | 45.0% | -0.8 | n/a | no target |
| P10R | 30880 | 0.0% | 100.0% |  | n/a | no target |
| P10 | 2746 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1309 | 4.2% | 96.3% | -7.4 | n/a | no target |
| P12 | 8 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 13602 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 136 | 2.2% | 99.3% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 51.7% | 81.0% | +0.1 | 95% | ❌ 43 pts to go |
| P02 | 403 | 65.8% | 90.3% | +0.2 | n/a | no target |
| P03 | 209 | 58.9% | 78.5% | -0.2 | n/a | no target |
| P04 | 1568 | 50.4% | 90.5% | +0.1 | n/a | no target |
| P05 | 378 | 5.3% | 86.0% | +0.1 | n/a | no target |
| P06M | 143 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 8765 | 0.3% | 99.9% | +0.3 | n/a | no target |
| P06 | 220 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 443 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 8765 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 349 | 66.2% | 67.6% | -1.3 | n/a | no target |
| P10R | 30880 | 0.0% | 100.0% |  | n/a | no target |
| P10 | 2746 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1309 | 4.5% | 96.6% | -8.2 | n/a | no target |
| P12 | 8 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 13602 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 136 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 403 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 209 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 1568 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 378 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 143 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 8765 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 220 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 443 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 8765 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 349 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 30880 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2746 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1309 | 99.9% | 99.9% | -0.1 | 100% | 🟡 0 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 13602 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 136 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 403 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 209 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 1568 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 378 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 143 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 8765 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 220 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 443 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 8765 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 349 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 30880 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2746 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1309 | 99.9% | 99.9% | -0.1 | 100% | 🟡 0 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 13602 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 15 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 136 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 403 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 209 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 1568 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 378 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 143 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 8765 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 220 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 443 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 8765 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 349 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 30880 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2746 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1309 | 99.9% | 99.9% | -0.1 | 100% | 🟡 0 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 13602 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

