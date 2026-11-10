# Coverage vs the downstream team's targets — 2026-11-10

Benchmarks (field × package with a numeric target): **103 of 446 met** (23.1%); 67 within 10 points; 276 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 26, P01T 137, P01_GOLD 626, P02 403, P03 209, P04 1571, P05 378, P06M 1795, P06T 9335, P06 279, P07 532, P08 11352, P09 349, P10R 27809, P10 2631, P11 3190, P12 8, P13 12223

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 26 | 0.0% | 23.1% | 7 | payment terms (20 rows) |
| P01T | 137 | 0.7% | 32.1% | 8 | reference to quote (PO / contract / vendor id) (131 rows) |
| P01_GOLD | 626 | 24.3% | 71.1% | 10 | payment terms (215 rows) |
| P02 | 403 | 8.9% | 62.8% | 9 | PO rule (298 rows) |
| P03 | 209 | 17.7% | 69.9% | 9 | PO rule (92 rows) |
| P04 | 1571 | 2.9% | 38.4% | 8 | PO rule (1416 rows) |
| P05 | 378 | 1.3% | 18.8% | 7 | payment terms (309 rows) |
| P06M | 1795 | 0.0% | 0.3% | 7 | PO rule (1785 rows) |
| P06T | 9335 | 0.0% | 1.5% | 6 | reference to quote (PO / contract / vendor id) (9302 rows) |
| P06 | 279 | 0.0% | 7.5% | 6 | reference to quote (PO / contract / vendor id) (279 rows) |
| P07 | 532 | 0.0% | 2.4% | 5 | reference to quote (PO / contract / vendor id) (532 rows) |
| P08 | 11352 | 0.0% | 0.2% | 5 | reference to quote (PO / contract / vendor id) (11352 rows) |
| P09 | 349 | 1.1% | 44.1% | 8 | payment terms (326 rows) |
| P10R | 27809 | 0.0% | 0.0% | 6 | vendor GST/HST number (27809 rows) |
| P10 | 2631 | 0.0% | 0.9% | 5 | reference to quote (PO / contract / vendor id) (2628 rows) |
| P11 | 3190 | 0.2% | 1.8% | 6 | PO rule (3158 rows) |
| P12 | 8 | 0.0% | 62.5% | 9 | PO rule (7 rows) |
| P13 | 12223 | 0.0% | 0.0% | 6 | reference to quote (PO / contract / vendor id) (12223 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 26 | 5 | 1 | 20 | 0 | 0 | 73 |
| P01T | 137 | 27 | 44 | 66 | 0 | 0 | 76 |
| P01_GOLD | 626 | 231 | 186 | 209 | 0 | 0 | 82 |
| P02 | 403 | 0 | 183 | 220 | 0 | 0 | 66 |
| P03 | 209 | 0 | 0 | 202 | 7 | 0 | 58 |
| P04 | 1571 | 0 | 0 | 1521 | 50 | 0 | 53 |
| P05 | 378 | 15 | 29 | 317 | 17 | 0 | 51 |
| P06M | 1795 | 0 | 3 | 1788 | 4 | 0 | 51 |
| P06T | 9335 | 0 | 25 | 8321 | 989 | 0 | 43 |
| P06 | 279 | 21 | 35 | 223 | 0 | 0 | 71 |
| P07 | 532 | 0 | 16 | 482 | 34 | 0 | 53 |
| P08 | 11352 | 0 | 0 | 8610 | 2742 | 0 | 43 |
| P09 | 349 | 5 | 13 | 328 | 3 | 0 | 53 |
| P10R | 27809 | 0 | 7 | 22708 | 5094 | 0 | 43 |
| P10 | 2631 | 4 | 14 | 1881 | 732 | 0 | 43 |
| P11 | 3190 | 0 | 0 | 0 | 0 | 3190 | 23 |
| P12 | 8 | 0 | 1 | 7 | 0 | 0 | 54 |
| P13 | 12223 | 2 | 8 | 11091 | 1122 | 0 | 51 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 26 | 15 | 57.7% | the buyer's PO / reference rule (8) |
| P01T | 137 | 57 | 41.6% | the buyer's PO / reference rule (49) |
| P01_GOLD | 626 | 464 | 74.1% | bill-to legal name and address (109) |
| P02 | 403 | 305 | 75.7% | the buyer's PO / reference rule (54) |
| P03 | 209 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (209) |
| P04 | 1571 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (1571) |
| P05 | 378 | 47 | 12.4% | a confirmed invoicing / AP or finance channel (290) |
| P06M | 1795 | 13 | 0.7% | a confirmed invoicing / AP or finance channel (1756) |
| P06T | 9335 | 17 | 0.2% | a confirmed invoicing / AP or finance channel (9115) |
| P06 | 279 | 34 | 12.2% | bill-to legal name and address (146) |
| P07 | 532 | 9 | 1.7% | bill-to legal name and address (223) |
| P08 | 11352 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (11352) |
| P09 | 349 | 48 | 13.8% | a confirmed invoicing / AP or finance channel (292) |
| P10R | 27809 | 302 | 1.1% | a confirmed invoicing / AP or finance channel (27174) |
| P10 | 2631 | 10 | 0.4% | a confirmed invoicing / AP or finance channel (2490) |
| P11 | 3190 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (3190) |
| P12 | 8 | 2 | 25.0% | a confirmed invoicing / AP or finance channel (6) |
| P13 | 12223 | 3 | 0.0% | a confirmed invoicing / AP or finance channel (11935) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 26 | 6 | 23.1% | 7 | 0 | the vendor's GST/HST number (BN9) (11) |
| P01T | 137 | 42 | 30.7% | 17 | 0 | the vendor's GST/HST number (BN9) (52) |
| P01_GOLD | 626 | 409 | 65.3% | 21 | 0 | the vendor's GST/HST number (BN9) (124) |
| P02 | 403 | 218 | 54.1% | 35 | 0 | the vendor's GST/HST number (BN9) (130) |
| P03 | 209 | 17 | 8.1% | 1 | 131 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (49) |
| P04 | 1571 | 43 | 2.7% | 10 | 707 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (773) |
| P05 | 378 | 22 | 5.8% | 10 | 93 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (188) |
| P06M | 1795 | 2 | 0.1% | 14 | 66 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (1684) |
| P06T | 9335 | 17 | 0.2% | 60 | 1881 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (7160) |
| P06 | 279 | 15 | 5.4% | 20 | 0 | the vendor's GST/HST number (BN9) (143) |
| P07 | 532 | 7 | 1.3% | 27 | 16 | the vendor's GST/HST number (BN9) (227) |
| P08 | 11352 | 2 | 0.0% | 3 | 739 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (10573) |
| P09 | 349 | 44 | 12.6% | 1 | 136 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (146) |
| P10R | 27809 | 502 | 1.8% | 0 | 18932 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (8183) |
| P10 | 2631 | 6 | 0.2% | 23 | 402 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2065) |
| P11 | 3190 | 6 | 0.2% | 0 | 0 | a confirmed invoicing / AP or finance channel (3173) |
| P12 | 8 | 2 | 25.0% | 0 | 3 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (3) |
| P13 | 12223 | 3 | 0.0% | 227 | 8560 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (3333) |
| **all** | 72853 | 1363 | 1.9% | 476 | 31666 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 21 | 0 | 0 | 0 | 0 | 3 | 0 | 19 | 20 | 1 |
| P01T | 110 | 0 | 0 | 0 | 6 | 20 | 3 | 69 | 80 | 30 |
| P01_GOLD | 395 | 0 | 0 | 0 | 11 | 94 | 34 | 193 | 228 | 60 |
| P02 | 403 | 0 | 403 | 0 | 4 | 38 | 8 | 298 | 227 | 22 |
| P03 | 209 | 0 | 209 | 0 | 2 | 34 | 11 | 92 | 94 | 25 |
| P04 | 1571 | 0 | 1571 | 0 | 12 | 328 | 93 | 1416 | 1211 | 106 |
| P05 | 363 | 0 | 313 | 0 | 8 | 91 | 44 | 296 | 311 | 55 |
| P06M | 1795 | 0 | 1795 | 0 | 65 | 342 | 29 | 1785 | 1774 | 3 |
| P06T | 9335 | 0 | 9335 | 0 | 1501 | 5070 | 1356 | 9223 | 9010 | 123 |
| P06 | 258 | 0 | 0 | 0 | 34 | 133 | 63 | 188 | 226 | 8 |
| P07 | 532 | 0 | 532 | 0 | 135 | 287 | 110 | 474 | 490 | 16 |
| P08 | 11352 | 0 | 11352 | 0 | 3966 | 7568 | 3078 | 11277 | 11188 | 167 |
| P09 | 344 | 0 | 323 | 0 | 9 | 74 | 4 | 317 | 330 | 50 |
| P10R | 27809 | 0 | 27713 | 0 | 429 | 16070 | 6825 | 27781 | 27733 | 24 |
| P10 | 2627 | 0 | 2571 | 0 | 221 | 1767 | 897 | 2579 | 2534 | 117 |
| P11 | 3190 | 3190 | 3142 | 0 | 1839 | 3040 | 802 | 3158 | 3127 | 31 |
| P12 | 8 | 0 | 7 | 0 | 0 | 2 | 0 | 7 | 6 | 0 |
| P13 | 12221 | 0 | 12122 | 0 | 315 | 3515 | 1631 | 12192 | 12198 | 26 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| vendor_registered_address | P08 | 14.5% | 70% | 6296 |
| buyer_ap_cycle_published | P10R | 0.0% | 20% | 5558 |
| vendor_logo_url | P08 | 51.5% | 100% | 5509 |
| ap_system_hint | P10R | 0.4% | 20% | 5448 |
| vendor_phone | P08 | 38.2% | 85% | 5319 |
| buyer_phone | P08 | 51.5% | 95% | 4942 |
| buyer_logo_url | P08 | 57.1% | 100% | 4865 |
| buyer_legal_name_as_published | P08 | 33.3% | 75% | 4730 |
| vendor_bn9 | P08 | 11.9% | 50% | 4322 |
| vendor_emails | P08 | 37.1% | 75% | 4302 |
| buyer_tax_exempt_status | P10R | 0.1% | 15% | 4156 |
| buyer_esignature_preference | P10R | 0.1% | 15% | 4152 |
| buyer_payment_method_preference | P10R | 0.6% | 15% | 4003 |
| vendor_trading_name | P08 | 21.6% | 50% | 3228 |
| invoice_reference_hint | P08 | 0.7% | 25% | 2763 |
| buyer_address | P08 | 72.8% | 95% | 2519 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 2444 |
| ap_system_hint | P13 | 0.8% | 20% | 2344 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 2266 |
| buyer_logo_url | P13 | 76.6% | 95% | 2249 |
| buyer_bn_as_published | P08 | 15.2% | 35% | 2245 |
| buyer_phone | P13 | 76.9% | 95% | 2209 |
| buyer_logo_url | P11 | 11.2% | 80% | 2194 |
| ap_system_hint | P08 | 0.8% | 20% | 2176 |
| buyer_phone | P11 | 8.5% | 75% | 2121 |
| vendor_phone | P11 | 11.8% | 75% | 2015 |
| buyer_legal_name_as_published | P11 | 4.7% | 65% | 1924 |
| vendor_emails | P11 | 9.7% | 70% | 1923 |
| buyer_ap_cycle_published | P06T | 0.1% | 20% | 1860 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 1826 |
| contract_value | P11 | 2.8% | 60% | 1826 |
| award_or_notice_id | P11 | 2.8% | 60% | 1825 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 1823 |
| buyer_payment_method_preference | P13 | 0.5% | 15% | 1774 |
| ap_system_hint | P06T | 1.7% | 20% | 1709 |
| buyer_esignature_preference | P08 | 0.2% | 15% | 1676 |
| buyer_tax_exempt_status | P08 | 0.3% | 15% | 1669 |
| buyer_payment_method_preference | P08 | 0.3% | 15% | 1667 |
| commodity_codes | P11 | 1.9% | 50% | 1534 |
| buyer_esignature_preference | P06T | 0.4% | 15% | 1365 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 69.2% | 69.2% | +24.8 | 50% | ✅ met |
| P01T | 137 | 51.8% | 51.8% | -19.9 | 50% | ✅ met |
| P01_GOLD | 626 | 92.3% | 94.6% | -0.2 | 95% | 🟡 3 pts to go |
| P02 | 403 | 83.9% | 85.6% | +0.0 | 95% | ❌ 11 pts to go |
| P03 | 209 | 92.3% | 95.7% | -0.5 | 95% | 🟡 3 pts to go |
| P04 | 1571 | 68.7% | 71.3% | +0.1 | 90% | ❌ 21 pts to go |
| P05 | 378 | 41.8% | 44.7% | +0.7 | 70% | ❌ 28 pts to go |
| P06M | 1795 | 92.5% | 92.5% | +85.4 | n/a | no target |
| P06T | 9335 | 1.5% | 1.6% | -2.9 | n/a | no target |
| P06 | 279 | 32.6% | 32.6% | -15.6 | 30% | ✅ met |
| P07 | 532 | 10.9% | 10.9% | -12.9 | 30% | ❌ 19 pts to go |
| P08 | 11352 | 0.7% | 0.7% | -1.7 | 25% | ❌ 24 pts to go |
| P09 | 349 | 99.1% | 99.7% | +0.1 | 100% | 🟡 1 pts to go |
| P10R | 27809 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2631 | 2.1% | 2.9% | -0.1 | 25% | ❌ 23 pts to go |
| P11 | 3190 | 22.0% | 22.4% | -2.1 | 60% | ❌ 38 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 12223 | 0.3% | 0.3% | +0.1 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 137 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 626 | 6.2% | 6.2% | +0.0 | 50% | ❌ 44 pts to go |
| P02 | 403 | 7.2% | 7.2% | +0.0 | 50% | ❌ 43 pts to go |
| P03 | 209 | 1.9% | 1.9% | +0.0 | 40% | ❌ 38 pts to go |
| P04 | 1571 | 1.1% | 1.1% | +0.0 | 30% | ❌ 29 pts to go |
| P05 | 378 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 1795 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 9335 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 279 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 532 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 11352 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 349 | 0.6% | 0.6% | +0.1 | 50% | ❌ 49 pts to go |
| P10R | 27809 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2631 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P11 | 3190 | 0.1% | 0.1% | -0.7 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 12223 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 42.3% | 42.3% | +42.3 | n/a | no target |
| P01T | 137 | 4.4% | 4.4% | -1.0 | 50% | ❌ 46 pts to go |
| P01_GOLD | 626 | 67.6% | 67.6% | +0.0 | 85% | ❌ 17 pts to go |
| P02 | 403 | 75.4% | 75.4% | -0.1 | 90% | ❌ 15 pts to go |
| P03 | 209 | 75.1% | 75.1% | -0.4 | 85% | 🟡 10 pts to go |
| P04 | 1571 | 65.6% | 65.6% | +0.1 | 85% | ❌ 19 pts to go |
| P05 | 378 | 31.5% | 31.5% | +0.5 | 60% | ❌ 28 pts to go |
| P06M | 1795 | 92.0% | 92.0% | +92.0 | n/a | no target |
| P06T | 9335 | 0.4% | 0.4% | +0.2 | n/a | no target |
| P06 | 279 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 532 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 11352 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 349 | 96.6% | 96.6% | +0.0 | 100% | 🟡 3 pts to go |
| P10R | 27809 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2631 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3190 | 21.4% | 21.4% | +1.4 | 60% | ❌ 39 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 12223 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 137 | 2.2% | 2.2% | +0.0 | 30% | ❌ 28 pts to go |
| P01_GOLD | 626 | 51.3% | 51.3% | +0.0 | 80% | ❌ 29 pts to go |
| P02 | 403 | 66.7% | 66.7% | -0.1 | 60% | ✅ met |
| P03 | 209 | 63.6% | 63.6% | -0.3 | 80% | ❌ 16 pts to go |
| P04 | 1571 | 54.6% | 54.6% | +0.1 | 50% | ✅ met |
| P05 | 378 | 13.5% | 13.5% | +0.2 | 40% | ❌ 26 pts to go |
| P06M | 1795 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 9335 | 0.4% | 0.4% | +0.2 | n/a | no target |
| P06 | 279 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 532 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 11352 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 349 | 85.4% | 85.4% | -0.7 | 50% | ✅ met |
| P10R | 27809 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2631 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3190 | 2.6% | 2.6% | -14.9 | 40% | ❌ 37 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 12223 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 137 | 2.9% | 2.9% | -0.4 | n/a | no target |
| P01_GOLD | 626 | 61.0% | 61.0% | -0.1 | 85% | ❌ 24 pts to go |
| P02 | 403 | 65.8% | 65.8% | +0.0 | 90% | ❌ 24 pts to go |
| P03 | 209 | 74.2% | 74.2% | -0.3 | 85% | ❌ 11 pts to go |
| P04 | 1571 | 56.4% | 56.4% | +0.1 | 85% | ❌ 29 pts to go |
| P05 | 378 | 21.4% | 21.4% | +0.3 | 50% | ❌ 29 pts to go |
| P06M | 1795 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 9335 | 0.4% | 0.4% | +0.2 | n/a | no target |
| P06 | 279 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 532 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 11352 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 349 | 97.1% | 97.1% | +0.0 | 100% | 🟡 3 pts to go |
| P10R | 27809 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2631 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3190 | 2.8% | 2.8% | -16.2 | 60% | ❌ 57 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 12223 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 137 | 1.5% | 1.5% | -0.7 | n/a | no target |
| P01_GOLD | 626 | 12.9% | 12.9% | -0.1 | 60% | ❌ 47 pts to go |
| P02 | 403 | 7.2% | 7.2% | +0.0 | 50% | ❌ 43 pts to go |
| P03 | 209 | 10.5% | 10.5% | -0.1 | 50% | ❌ 40 pts to go |
| P04 | 1571 | 4.3% | 4.3% | +0.0 | 40% | ❌ 36 pts to go |
| P05 | 378 | 1.3% | 1.3% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 1795 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 9335 | 0.0% | 0.0% | -0.1 | n/a | no target |
| P06 | 279 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 532 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 11352 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 349 | 2.9% | 2.9% | +0.3 | 50% | ❌ 47 pts to go |
| P10R | 27809 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2631 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3190 | 0.4% | 0.4% | -2.6 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 12223 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 137 | 0.7% | 0.7% | +0.7 | n/a | no target |
| P01_GOLD | 626 | 35.0% | 35.0% | -0.1 | 80% | ❌ 45 pts to go |
| P02 | 403 | 60.8% | 60.8% | +0.2 | 90% | ❌ 29 pts to go |
| P03 | 209 | 41.1% | 41.1% | -0.2 | 80% | ❌ 39 pts to go |
| P04 | 1571 | 51.3% | 51.3% | +0.0 | 85% | ❌ 34 pts to go |
| P05 | 378 | 6.1% | 6.1% | +0.1 | 50% | ❌ 44 pts to go |
| P06M | 1795 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 9335 | 0.2% | 0.2% | +0.2 | n/a | no target |
| P06 | 279 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 532 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 11352 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 349 | 76.5% | 76.5% | +0.6 | 95% | ❌ 18 pts to go |
| P10R | 27809 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2631 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3190 | 1.9% | 1.9% | -11.2 | 50% | ❌ 48 pts to go |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 12223 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 137 | 0.7% | 0.7% | -0.4 | n/a | no target |
| P01_GOLD | 626 | 8.5% | 8.5% | +0.0 | 50% | ❌ 42 pts to go |
| P02 | 403 | 7.2% | 7.2% | +0.0 | 50% | ❌ 43 pts to go |
| P03 | 209 | 2.4% | 2.4% | +0.0 | 30% | ❌ 28 pts to go |
| P04 | 1571 | 1.1% | 1.1% | +0.0 | 30% | ❌ 29 pts to go |
| P05 | 378 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 1795 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 9335 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 279 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 532 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 11352 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 349 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P10R | 27809 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2631 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3190 | 0.1% | 0.1% | -0.7 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 12223 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 137 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 403 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 209 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 1571 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 378 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 1795 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 9335 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 279 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 532 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 11352 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 349 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 27809 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2631 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 3190 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 12223 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 57.7% | 57.7% | -42.3 | 70% | ❌ 12 pts to go |
| P01T | 137 | 56.9% | 56.9% | -23.5 | 60% | 🟡 3 pts to go |
| P01_GOLD | 626 | 77.8% | 77.8% | -0.1 | 90% | ❌ 12 pts to go |
| P02 | 403 | 67.2% | 67.2% | -0.1 | 85% | ❌ 18 pts to go |
| P03 | 209 | 82.3% | 82.3% | +0.1 | 90% | 🟡 8 pts to go |
| P04 | 1571 | 55.3% | 55.3% | -0.1 | 75% | ❌ 20 pts to go |
| P05 | 378 | 53.4% | 53.4% | +0.8 | 50% | ✅ met |
| P06M | 1795 | 5.7% | 5.7% | -68.7 | n/a | no target |
| P06T | 9335 | 25.6% | 25.6% | -35.1 | n/a | no target |
| P06 | 279 | 25.4% | 25.4% | -18.6 | 40% | ❌ 15 pts to go |
| P07 | 532 | 17.9% | 17.9% | -20.2 | 50% | ❌ 32 pts to go |
| P08 | 11352 | 11.9% | 11.9% | -28.3 | 50% | ❌ 38 pts to go |
| P09 | 349 | 55.9% | 55.9% | +1.6 | 80% | ❌ 24 pts to go |
| P10R | 27809 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2631 | 31.6% | 31.6% | -5.0 | 40% | 🟡 8 pts to go |
| P11 | 3190 | 81.6% | 81.6% | +36.9 | 60% | ✅ met |
| P12 | 8 | 62.5% | 62.5% | +9.9 | 85% | ❌ 22 pts to go |
| P13 | 12223 | 89.9% | 89.9% | -1.8 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 53.8% | 53.8% | -7.3 | n/a | no target |
| P01T | 137 | 45.3% | 45.3% | -17.7 | n/a | no target |
| P01_GOLD | 626 | 74.9% | 74.9% | +0.1 | 95% | ❌ 20 pts to go |
| P02 | 403 | 84.9% | 84.9% | +0.0 | 95% | ❌ 10 pts to go |
| P03 | 209 | 78.0% | 78.0% | +0.1 | 95% | ❌ 17 pts to go |
| P04 | 1571 | 80.5% | 80.5% | -0.2 | 95% | ❌ 14 pts to go |
| P05 | 378 | 56.6% | 56.6% | +0.4 | 70% | ❌ 13 pts to go |
| P06M | 1795 | 4.4% | 4.4% | -16.4 | n/a | no target |
| P06T | 9335 | 44.1% | 44.1% | -34.1 | n/a | no target |
| P06 | 279 | 30.8% | 30.8% | -24.6 | 80% | ❌ 49 pts to go |
| P07 | 532 | 23.9% | 23.9% | -28.1 | 70% | ❌ 46 pts to go |
| P08 | 11352 | 14.5% | 14.5% | -37.9 | 70% | ❌ 56 pts to go |
| P09 | 349 | 88.5% | 88.5% | +0.0 | 100% | ❌ 12 pts to go |
| P10R | 27809 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2631 | 36.2% | 36.2% | -6.2 | 70% | ❌ 34 pts to go |
| P11 | 3190 | 65.1% | 65.1% | +9.8 | 75% | 🟡 10 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 12223 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 34.6% | 34.6% | -15.4 | n/a | no target |
| P01T | 137 | 22.6% | 22.6% | +3.0 | n/a | no target |
| P01_GOLD | 626 | 52.4% | 52.4% | +0.0 | 60% | 🟡 8 pts to go |
| P02 | 403 | 67.2% | 67.2% | -0.1 | 60% | ✅ met |
| P03 | 209 | 64.6% | 64.6% | -0.3 | 60% | ✅ met |
| P04 | 1571 | 55.4% | 55.4% | -0.1 | 55% | ✅ met |
| P05 | 378 | 24.9% | 24.9% | -0.4 | 50% | ❌ 25 pts to go |
| P06M | 1795 | 1.5% | 1.5% | -15.8 | n/a | no target |
| P06T | 9335 | 40.3% | 40.3% | -13.3 | n/a | no target |
| P06 | 279 | 34.4% | 34.4% | -18.6 | n/a | no target |
| P07 | 532 | 28.2% | 28.2% | -17.8 | 55% | ❌ 27 pts to go |
| P08 | 11352 | 21.6% | 21.6% | -25.9 | 50% | ❌ 28 pts to go |
| P09 | 349 | 72.5% | 72.5% | +1.1 | 70% | ✅ met |
| P10R | 27809 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2631 | 47.7% | 47.7% | -4.2 | 55% | 🟡 7 pts to go |
| P11 | 3190 | 64.3% | 64.3% | +21.3 | 50% | ✅ met |
| P12 | 8 | 87.5% | 87.5% | +3.3 | n/a | no target |
| P13 | 12223 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 42.3% | 42.3% | -18.8 | n/a | no target |
| P01T | 137 | 38.7% | 38.7% | +8.3 | n/a | no target |
| P01_GOLD | 626 | 51.8% | 51.8% | +0.0 | 70% | ❌ 18 pts to go |
| P02 | 403 | 57.1% | 57.1% | -0.1 | 70% | ❌ 13 pts to go |
| P03 | 209 | 57.4% | 57.4% | +0.2 | 70% | ❌ 13 pts to go |
| P04 | 1571 | 51.9% | 51.9% | -0.1 | 65% | ❌ 13 pts to go |
| P05 | 378 | 33.3% | 33.3% | -1.3 | 60% | ❌ 27 pts to go |
| P06M | 1795 | 2.6% | 2.6% | -27.8 | n/a | no target |
| P06T | 9335 | 24.5% | 24.5% | +21.0 | n/a | no target |
| P06 | 279 | 46.6% | 46.6% | -13.0 | 40% | ✅ met |
| P07 | 532 | 46.4% | 46.4% | -21.5 | 85% | ❌ 39 pts to go |
| P08 | 11352 | 38.2% | 38.2% | -29.9 | 85% | ❌ 47 pts to go |
| P09 | 349 | 53.6% | 53.6% | -1.8 | 85% | ❌ 31 pts to go |
| P10R | 27809 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2631 | 61.2% | 61.2% | -5.1 | 85% | ❌ 24 pts to go |
| P11 | 3190 | 11.8% | 11.8% | -43.1 | 75% | ❌ 63 pts to go |
| P12 | 8 | 12.5% | 12.5% | -3.3 | n/a | no target |
| P13 | 12223 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 53.8% | 53.8% | -40.6 | n/a | no target |
| P01T | 137 | 93.4% | 93.4% | +3.2 | n/a | no target |
| P01_GOLD | 626 | 89.5% | 89.5% | +0.1 | 90% | 🟡 0 pts to go |
| P02 | 403 | 87.8% | 87.8% | +0.2 | 90% | 🟡 2 pts to go |
| P03 | 209 | 90.0% | 90.0% | +0.1 | 90% | ✅ met |
| P04 | 1571 | 81.0% | 81.0% | -0.3 | 85% | 🟡 4 pts to go |
| P05 | 378 | 50.3% | 50.3% | -0.7 | 70% | ❌ 20 pts to go |
| P06M | 1795 | 5.1% | 5.1% | -62.8 | n/a | no target |
| P06T | 9335 | 91.7% | 91.7% | +13.8 | n/a | no target |
| P06 | 279 | 98.2% | 98.2% | +1.2 | 50% | ✅ met |
| P07 | 532 | 98.7% | 98.7% | +1.9 | 100% | 🟡 1 pts to go |
| P08 | 11352 | 99.0% | 99.0% | +2.9 | 100% | 🟡 1 pts to go |
| P09 | 349 | 79.7% | 79.7% | -0.1 | 100% | ❌ 20 pts to go |
| P10R | 27809 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2631 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 3190 | 99.0% | 99.0% | +6.0 | 100% | 🟡 1 pts to go |
| P12 | 8 | 25.0% | 25.0% | -17.1 | n/a | no target |
| P13 | 12223 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 34.6% | 34.6% | -15.4 | n/a | no target |
| P01T | 137 | 40.9% | 40.9% | -4.8 | n/a | no target |
| P01_GOLD | 626 | 45.7% | 45.7% | +0.0 | 70% | ❌ 24 pts to go |
| P02 | 403 | 51.6% | 51.6% | +0.1 | 75% | ❌ 23 pts to go |
| P03 | 209 | 51.7% | 51.7% | +0.3 | 75% | ❌ 23 pts to go |
| P04 | 1571 | 42.8% | 42.8% | -0.1 | 70% | ❌ 27 pts to go |
| P05 | 378 | 24.1% | 24.1% | -0.4 | 55% | ❌ 31 pts to go |
| P06M | 1795 | 1.4% | 1.4% | -14.7 | n/a | no target |
| P06T | 9335 | 17.8% | 17.8% | +14.9 | n/a | no target |
| P06 | 279 | 36.9% | 36.9% | -4.1 | n/a | no target |
| P07 | 532 | 35.7% | 35.7% | -1.2 | 70% | ❌ 34 pts to go |
| P08 | 11352 | 37.1% | 37.1% | -11.6 | 75% | ❌ 38 pts to go |
| P09 | 349 | 51.3% | 51.3% | -0.7 | 85% | ❌ 34 pts to go |
| P10R | 27809 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2631 | 46.6% | 46.6% | -4.7 | 80% | ❌ 33 pts to go |
| P11 | 3190 | 9.7% | 9.7% | -30.8 | 70% | ❌ 60 pts to go |
| P12 | 8 | 25.0% | 25.0% | -6.6 | n/a | no target |
| P13 | 12223 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 53.8% | 53.8% | -40.6 | n/a | no target |
| P01T | 137 | 81.8% | 81.8% | -7.3 | n/a | no target |
| P01_GOLD | 626 | 79.9% | 79.9% | +0.1 | 90% | ❌ 10 pts to go |
| P02 | 403 | 77.4% | 77.4% | +0.2 | 90% | ❌ 13 pts to go |
| P03 | 209 | 81.8% | 81.8% | +0.1 | 90% | 🟡 8 pts to go |
| P04 | 1571 | 70.7% | 70.7% | -0.2 | 85% | ❌ 14 pts to go |
| P05 | 378 | 47.6% | 47.6% | -0.8 | 75% | ❌ 27 pts to go |
| P06M | 1795 | 5.1% | 5.1% | -62.8 | n/a | no target |
| P06T | 9335 | 55.9% | 55.9% | -21.2 | n/a | no target |
| P06 | 279 | 66.7% | 66.7% | -21.9 | n/a | no target |
| P07 | 532 | 62.4% | 62.4% | -28.1 | 100% | ❌ 38 pts to go |
| P08 | 11352 | 51.5% | 51.5% | -37.5 | 100% | ❌ 48 pts to go |
| P09 | 349 | 61.3% | 61.3% | -1.2 | n/a | no target |
| P10R | 27809 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2631 | 81.7% | 81.7% | -7.3 | 100% | ❌ 18 pts to go |
| P11 | 3190 | 72.1% | 72.1% | -2.4 | n/a | no target |
| P12 | 8 | 25.0% | 25.0% | -11.8 | n/a | no target |
| P13 | 12223 | 69.4% | 69.4% | -13.3 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 137 | 16.8% | 16.8% | -4.9 | n/a | no target · QC vendors: 3 rows, 100.0% filled |
| P01_GOLD | 626 | 48.1% | 48.1% | +0.2 | 95% | ❌ 47 pts to go · QC vendors: 52 rows, 98.1% filled |
| P02 | 403 | 68.5% | 68.5% | -0.1 | 95% | ❌ 26 pts to go · QC vendors: 107 rows, 100.0% filled |
| P03 | 209 | 55.5% | 55.5% | -0.3 | 95% | ❌ 40 pts to go · QC vendors: 17 rows, 100.0% filled |
| P04 | 1571 | 60.0% | 60.0% | -0.2 | 95% | ❌ 35 pts to go · QC vendors: 435 rows, 98.6% filled |
| P05 | 378 | 15.1% | 15.1% | +0.3 | n/a | no target · QC vendors: 31 rows, 93.5% filled |
| P06M | 1795 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 9335 | 35.7% | 35.7% | -20.2 | n/a | no target · QC vendors: 1183 rows, 100.0% filled |
| P06 | 279 | 15.8% | 15.8% | -10.7 | n/a | no target · QC vendors: 20 rows, 100.0% filled |
| P07 | 532 | 10.7% | 10.7% | -10.7 | n/a | no target · QC vendors: 31 rows, 96.8% filled |
| P08 | 11352 | 8.5% | 8.5% | -20.4 | n/a | no target · QC vendors: 651 rows, 99.4% filled |
| P09 | 349 | 80.2% | 80.2% | +0.1 | 95% | ❌ 15 pts to go · QC vendors: 137 rows, 99.3% filled |
| P10R | 27809 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2631 | 20.2% | 20.2% | -3.2 | n/a | no target · QC vendors: 409 rows, 97.6% filled |
| P11 | 3190 | 61.1% | 61.1% | +31.8 | n/a | no target · QC vendors: 97 rows, 99.0% filled |
| P12 | 8 | 62.5% | 62.5% | -11.2 | n/a | no target · QC vendors: 1 rows, 100.0% filled |
| P13 | 12223 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 42.3% | 42.3% | -18.8 | n/a | no target · vendors with a registry record: 11 rows, 100.0% filled |
| P01T | 137 | 45.3% | 45.3% | -17.7 | n/a | no target · vendors with a registry record: 62 rows, 100.0% filled |
| P01_GOLD | 626 | 83.4% | 83.4% | -0.1 | 100% | ❌ 17 pts to go · vendors with a registry record: 522 rows, 100.0% filled |
| P02 | 403 | 89.1% | 89.1% | +0.0 | 100% | ❌ 11 pts to go · vendors with a registry record: 359 rows, 100.0% filled |
| P03 | 209 | 89.0% | 89.0% | +0.1 | 100% | ❌ 11 pts to go · vendors with a registry record: 186 rows, 100.0% filled |
| P04 | 1571 | 81.2% | 81.2% | -0.2 | 100% | ❌ 19 pts to go · vendors with a registry record: 1276 rows, 100.0% filled |
| P05 | 378 | 62.2% | 62.2% | +0.5 | n/a | no target · vendors with a registry record: 235 rows, 100.0% filled |
| P06M | 1795 | 1.8% | 1.8% | -19.0 | n/a | no target · vendors with a registry record: 33 rows, 100.0% filled |
| P06T | 9335 | 44.1% | 44.1% | -34.1 | n/a | no target · vendors with a registry record: 4121 rows, 100.0% filled |
| P06 | 279 | 31.9% | 31.9% | -25.9 | n/a | no target · vendors with a registry record: 89 rows, 100.0% filled |
| P07 | 532 | 24.4% | 24.4% | -30.0 | n/a | no target · vendors with a registry record: 130 rows, 100.0% filled |
| P08 | 11352 | 14.9% | 14.9% | -39.4 | n/a | no target · vendors with a registry record: 1689 rows, 100.0% filled |
| P09 | 349 | 92.0% | 92.0% | +0.4 | n/a | no target · vendors with a registry record: 321 rows, 100.0% filled |
| P10R | 27809 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2631 | 37.2% | 37.2% | -6.5 | n/a | no target · vendors with a registry record: 980 rows, 100.0% filled |
| P11 | 3190 | 65.5% | 65.5% | +7.3 | n/a | no target · vendors with a registry record: 2089 rows, 100.0% filled |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 8 rows, 100.0% filled |
| P13 | 12223 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 88.5% | 88.5% | -5.9 | 90% | 🟡 2 pts to go |
| P01T | 137 | 85.4% | 85.4% | -9.2 | 90% | 🟡 5 pts to go |
| P01_GOLD | 626 | 85.0% | 85.0% | +0.4 | 95% | 🟡 10 pts to go |
| P02 | 403 | 90.6% | 90.6% | +0.0 | 95% | 🟡 4 pts to go |
| P03 | 209 | 83.7% | 83.7% | +0.5 | 85% | 🟡 1 pts to go |
| P04 | 1571 | 79.1% | 79.1% | +0.3 | 90% | ❌ 11 pts to go |
| P05 | 378 | 75.9% | 75.9% | +0.1 | 75% | ✅ met |
| P06M | 1795 | 80.9% | 80.9% | -7.8 | n/a | no target |
| P06T | 9335 | 45.7% | 45.7% | -18.7 | n/a | no target |
| P06 | 279 | 52.3% | 52.3% | -4.3 | 80% | ❌ 28 pts to go |
| P07 | 532 | 46.1% | 46.1% | -7.5 | 80% | ❌ 34 pts to go |
| P08 | 11352 | 33.3% | 33.3% | -3.5 | 75% | ❌ 42 pts to go |
| P09 | 349 | 78.8% | 78.8% | -2.0 | 95% | ❌ 16 pts to go |
| P10R | 27809 | 42.2% | 42.2% |  | n/a | no target |
| P10 | 2631 | 32.8% | 32.8% | +0.8 | 70% | ❌ 37 pts to go |
| P11 | 3190 | 4.7% | 4.7% | -20.2 | 65% | ❌ 60 pts to go |
| P12 | 8 | 75.0% | 75.0% | +1.3 | 80% | 🟡 5 pts to go |
| P13 | 12223 | 71.2% | 71.3% | +18.7 | 60% | ✅ met |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 50.0% | 50.0% | +11.1 | 50% | ✅ met |
| P01T | 137 | 19.0% | 19.0% | -1.7 | n/a | no target |
| P01_GOLD | 626 | 20.6% | 20.6% | +0.2 | 40% | ❌ 19 pts to go |
| P02 | 403 | 21.6% | 21.6% | -0.2 | 40% | ❌ 18 pts to go |
| P03 | 209 | 26.8% | 26.8% | -0.1 | 40% | ❌ 13 pts to go |
| P04 | 1571 | 27.6% | 27.6% | +0.0 | 40% | ❌ 12 pts to go |
| P05 | 378 | 23.0% | 23.0% | +0.1 | 25% | 🟡 2 pts to go |
| P06M | 1795 | 21.4% | 21.4% | -4.2 | n/a | no target |
| P06T | 9335 | 21.0% | 21.0% | -9.9 | n/a | no target |
| P06 | 279 | 13.3% | 13.3% | +2.5 | 35% | ❌ 22 pts to go |
| P07 | 532 | 13.3% | 13.3% | +3.0 | 35% | ❌ 22 pts to go |
| P08 | 11352 | 15.2% | 15.2% | +4.1 | 35% | ❌ 20 pts to go |
| P09 | 349 | 16.9% | 16.9% | -0.2 | n/a | no target |
| P10R | 27809 | 18.7% | 18.7% |  | n/a | no target |
| P10 | 2631 | 10.1% | 10.1% | +0.5 | 30% | ❌ 20 pts to go |
| P11 | 3190 | 1.4% | 1.4% | -7.0 | n/a | no target |
| P12 | 8 | 12.5% | 12.5% | +2.0 | n/a | no target |
| P13 | 12223 | 38.9% | 38.9% | +13.0 | 30% | ✅ met |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 100.0% | 100.0% | +5.6 | 100% | ✅ met |
| P01T | 137 | 97.8% | 97.8% | +4.3 | 100% | 🟡 2 pts to go |
| P01_GOLD | 626 | 90.3% | 90.3% | +2.6 | 100% | 🟡 10 pts to go |
| P02 | 403 | 97.5% | 97.5% | +0.7 | 100% | 🟡 2 pts to go |
| P03 | 209 | 92.8% | 92.8% | +1.0 | 100% | 🟡 7 pts to go |
| P04 | 1571 | 93.0% | 93.0% | +2.0 | 100% | 🟡 7 pts to go |
| P05 | 378 | 87.3% | 87.3% | +2.4 | 100% | ❌ 13 pts to go |
| P06M | 1795 | 98.4% | 98.4% | +26.4 | n/a | no target |
| P06T | 9335 | 85.4% | 85.4% | +5.2 | n/a | no target |
| P06 | 279 | 74.6% | 74.6% | +5.9 | 95% | ❌ 20 pts to go |
| P07 | 532 | 78.9% | 78.9% | +8.3 | 95% | ❌ 16 pts to go |
| P08 | 11352 | 72.8% | 72.8% | +6.6 | 95% | ❌ 22 pts to go |
| P09 | 349 | 96.3% | 96.3% | +0.8 | 100% | 🟡 4 pts to go |
| P10R | 27809 | 75.4% | 75.4% |  | n/a | no target |
| P10 | 2631 | 65.8% | 65.8% | +0.6 | 95% | ❌ 29 pts to go |
| P11 | 3190 | 67.1% | 67.1% | +32.7 | 80% | ❌ 13 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 12223 | 86.6% | 86.6% | +10.5 | 95% | 🟡 8 pts to go |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 88.5% | 88.5% | -0.4 | n/a | no target |
| P01T | 137 | 78.1% | 78.1% | -2.3 | n/a | no target |
| P01_GOLD | 626 | 70.4% | 70.4% | +0.2 | 90% | ❌ 20 pts to go |
| P02 | 403 | 79.7% | 79.7% | +0.0 | 95% | ❌ 15 pts to go |
| P03 | 209 | 73.2% | 73.2% | -0.4 | 95% | ❌ 22 pts to go |
| P04 | 1571 | 84.7% | 84.7% | -0.2 | 95% | ❌ 10 pts to go |
| P05 | 378 | 74.6% | 74.6% | -0.4 | 90% | ❌ 15 pts to go |
| P06M | 1795 | 87.7% | 87.7% | +3.8 | n/a | no target |
| P06T | 9335 | 70.3% | 70.3% | -7.0 | n/a | no target |
| P06 | 279 | 55.9% | 55.9% | -8.6 | 95% | ❌ 39 pts to go |
| P07 | 532 | 53.0% | 53.0% | -13.3 | 90% | ❌ 37 pts to go |
| P08 | 11352 | 51.5% | 51.5% | -23.2 | 95% | ❌ 44 pts to go |
| P09 | 349 | 88.0% | 88.0% | -1.0 | 100% | ❌ 12 pts to go |
| P10R | 27809 | 76.6% | 76.6% |  | n/a | no target |
| P10 | 2631 | 64.5% | 64.5% | -7.0 | 95% | ❌ 30 pts to go |
| P11 | 3190 | 8.5% | 8.5% | -20.4 | 75% | ❌ 66 pts to go |
| P12 | 8 | 87.5% | 87.5% | -2.0 | n/a | no target |
| P13 | 12223 | 76.9% | 76.9% | -2.4 | 95% | ❌ 18 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 84.6% | 84.6% | +6.8 | n/a | no target |
| P01T | 137 | 88.3% | 88.3% | -3.0 | 95% | 🟡 7 pts to go |
| P01_GOLD | 626 | 82.3% | 82.3% | +0.1 | 90% | 🟡 8 pts to go |
| P02 | 403 | 88.3% | 88.3% | -0.1 | 95% | 🟡 7 pts to go |
| P03 | 209 | 84.2% | 84.2% | -0.4 | 95% | ❌ 11 pts to go |
| P04 | 1571 | 84.3% | 84.3% | +0.1 | 90% | 🟡 6 pts to go |
| P05 | 378 | 89.7% | 89.7% | +0.1 | 95% | 🟡 5 pts to go |
| P06M | 1795 | 85.3% | 85.3% | +0.2 | n/a | no target |
| P06T | 9335 | 78.4% | 78.4% | -15.7 | n/a | no target |
| P06 | 279 | 75.6% | 75.6% | -14.8 | 100% | ❌ 24 pts to go |
| P07 | 532 | 67.9% | 67.9% | -20.2 | 100% | ❌ 32 pts to go |
| P08 | 11352 | 57.1% | 57.1% | -33.6 | 100% | ❌ 43 pts to go |
| P09 | 349 | 71.9% | 71.9% | -2.1 | n/a | no target |
| P10R | 27809 | 84.1% | 84.1% |  | n/a | no target |
| P10 | 2631 | 82.9% | 82.9% | -7.2 | 100% | ❌ 17 pts to go |
| P11 | 3190 | 11.2% | 11.2% | -25.3 | 80% | ❌ 69 pts to go |
| P12 | 8 | 87.5% | 87.5% | +3.3 | n/a | no target |
| P13 | 12223 | 76.6% | 76.6% | -7.6 | 95% | ❌ 18 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 11.5% | 11.5% | -5.2 | n/a | no target |
| P01T | 137 | 18.2% | 18.2% | -5.7 | n/a | no target |
| P01_GOLD | 626 | 14.2% | 14.2% | -0.1 | 25% | ❌ 11 pts to go |
| P02 | 403 | 27.8% | 27.8% | +0.1 | 40% | ❌ 12 pts to go |
| P03 | 209 | 10.5% | 10.5% | -0.1 | 20% | 🟡 10 pts to go |
| P04 | 1571 | 7.4% | 7.4% | +0.0 | 20% | ❌ 13 pts to go |
| P05 | 378 | 4.0% | 4.0% | +0.1 | 15% | ❌ 11 pts to go |
| P06M | 1795 | 0.7% | 0.7% | -4.1 | n/a | no target |
| P06T | 9335 | 1.3% | 1.3% | -1.9 | n/a | no target |
| P06 | 279 | 5.7% | 5.7% | +0.3 | n/a | no target |
| P07 | 532 | 7.9% | 7.9% | +1.6 | n/a | no target |
| P08 | 11352 | 0.5% | 0.5% | -0.5 | n/a | no target |
| P09 | 349 | 7.4% | 7.4% | -0.5 | n/a | no target |
| P10R | 27809 | 0.5% | 0.5% |  | n/a | no target |
| P10 | 2631 | 1.1% | 1.1% | -0.2 | n/a | no target |
| P11 | 3190 | 0.4% | 0.4% | -2.1 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | -10.5 | n/a | no target |
| P13 | 12223 | 0.7% | 0.7% | +0.1 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 38.5% | 38.5% | -0.4 | n/a | no target |
| P01T | 137 | 38.7% | 38.7% | +3.9 | 70% | ❌ 31 pts to go |
| P01_GOLD | 626 | 43.3% | 43.3% | +0.0 | 80% | ❌ 37 pts to go |
| P02 | 403 | 64.3% | 64.3% | +0.2 | 90% | ❌ 26 pts to go |
| P03 | 209 | 23.4% | 23.4% | +0.3 | 60% | ❌ 37 pts to go |
| P04 | 1571 | 50.5% | 50.5% | +0.0 | 85% | ❌ 34 pts to go |
| P05 | 378 | 13.2% | 13.2% | +0.2 | 50% | ❌ 37 pts to go |
| P06M | 1795 | 1.0% | 1.0% | -5.5 | n/a | no target |
| P06T | 9335 | 1.6% | 1.6% | -1.1 | n/a | no target |
| P06 | 279 | 21.9% | 21.9% | +3.8 | n/a | no target |
| P07 | 532 | 17.3% | 17.3% | -1.7 | n/a | no target |
| P08 | 11352 | 0.2% | 0.2% | -0.4 | n/a | no target |
| P09 | 349 | 78.8% | 78.8% | -1.8 | 95% | ❌ 16 pts to go |
| P10R | 27809 | 0.8% | 0.8% |  | n/a | no target |
| P10 | 2631 | 2.9% | 2.9% | -0.2 | n/a | no target |
| P11 | 3190 | 9.8% | 9.8% | -19.5 | n/a | no target |
| P12 | 8 | 25.0% | 25.0% | -6.6 | n/a | no target |
| P13 | 12223 | 1.1% | 1.1% | +0.1 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 3.8% | 3.8% | +3.8 | n/a | no target |
| P01T | 137 | 16.8% | 16.8% | +0.5 | n/a | no target |
| P01_GOLD | 626 | 33.9% | 33.9% | -0.1 | 70% | ❌ 36 pts to go |
| P02 | 403 | 44.4% | 44.4% | +0.1 | 75% | ❌ 31 pts to go |
| P03 | 209 | 23.4% | 23.4% | +0.3 | 55% | ❌ 32 pts to go |
| P04 | 1571 | 50.5% | 50.5% | +0.0 | 75% | ❌ 24 pts to go |
| P05 | 378 | 11.9% | 11.9% | +0.2 | 50% | ❌ 38 pts to go |
| P06M | 1795 | 0.4% | 0.4% | -1.4 | n/a | no target |
| P06T | 9335 | 1.0% | 1.0% | -0.5 | n/a | no target |
| P06 | 279 | 12.9% | 12.9% | +2.7 | n/a | no target |
| P07 | 532 | 8.5% | 8.5% | -1.8 | n/a | no target |
| P08 | 11352 | 0.2% | 0.2% | -0.3 | n/a | no target |
| P09 | 349 | 75.9% | 75.9% | -1.8 | 95% | ❌ 19 pts to go |
| P10R | 27809 | 0.6% | 0.6% |  | n/a | no target |
| P10 | 2631 | 1.7% | 1.7% | -0.1 | n/a | no target |
| P11 | 3190 | 9.9% | 9.9% | -19.0 | n/a | no target |
| P12 | 8 | 12.5% | 12.5% | -3.3 | n/a | no target |
| P13 | 12223 | 0.7% | 0.7% | +0.1 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 15.4% | 15.4% | -1.3 | n/a | no target |
| P01T | 137 | 14.6% | 14.6% | -5.0 | n/a | no target |
| P01_GOLD | 626 | 57.8% | 58.0% | -0.1 | 80% | ❌ 22 pts to go |
| P02 | 403 | 52.4% | 52.6% | +0.2 | 75% | ❌ 23 pts to go |
| P03 | 209 | 45.5% | 45.5% | +0.3 | 70% | ❌ 24 pts to go |
| P04 | 1571 | 48.8% | 49.8% | +0.1 | 70% | ❌ 21 pts to go |
| P05 | 378 | 16.7% | 16.7% | +0.3 | 50% | ❌ 33 pts to go |
| P06M | 1795 | 0.3% | 0.3% | -3.9 | n/a | no target |
| P06T | 9335 | 0.9% | 0.9% | -0.7 | n/a | no target |
| P06 | 279 | 18.3% | 18.3% | -5.8 | n/a | no target |
| P07 | 532 | 3.2% | 3.2% | -2.0 | n/a | no target |
| P08 | 11352 | 0.4% | 0.4% | -0.6 | n/a | no target |
| P09 | 349 | 44.1% | 44.4% | +0.0 | 80% | ❌ 36 pts to go |
| P10R | 27809 | 0.2% | 0.2% |  | n/a | no target |
| P10 | 2631 | 1.4% | 1.5% | -0.1 | n/a | no target |
| P11 | 3190 | 2.8% | 2.8% | -13.9 | n/a | no target |
| P12 | 8 | 25.0% | 25.0% | -6.6 | n/a | no target |
| P13 | 12223 | 0.5% | 0.5% | +0.2 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 23.1% | 23.1% | -15.8 | n/a | no target |
| P01T | 137 | 41.6% | 41.6% | -14.9 | 60% | ❌ 18 pts to go |
| P01_GOLD | 626 | 63.6% | 63.6% | +0.1 | 70% | 🟡 6 pts to go |
| P02 | 403 | 43.7% | 43.7% | -0.1 | 50% | 🟡 6 pts to go |
| P03 | 209 | 55.0% | 55.0% | -0.3 | 55% | ✅ met |
| P04 | 1571 | 22.9% | 22.9% | +0.0 | 40% | ❌ 17 pts to go |
| P05 | 378 | 17.7% | 17.7% | +0.3 | 40% | ❌ 22 pts to go |
| P06M | 1795 | 1.2% | 1.2% | -15.5 | n/a | no target |
| P06T | 9335 | 3.5% | 3.5% | -9.0 | n/a | no target |
| P06 | 279 | 19.0% | 19.0% | -11.7 | n/a | no target |
| P07 | 532 | 7.9% | 7.9% | -8.4 | n/a | no target |
| P08 | 11352 | 1.4% | 1.4% | -3.3 | n/a | no target |
| P09 | 349 | 5.4% | 5.4% | -0.4 | n/a | no target |
| P10R | 27809 | 0.3% | 0.3% |  | n/a | no target |
| P10 | 2631 | 3.7% | 3.7% | -0.2 | n/a | no target |
| P11 | 3190 | 2.0% | 2.0% | -5.6 | n/a | no target |
| P12 | 8 | 25.0% | 25.0% | +9.2 | n/a | no target |
| P13 | 12223 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 26.9% | 26.9% | -17.5 | n/a | no target |
| P01T | 137 | 49.6% | 49.6% | -20.0 | 65% | ❌ 15 pts to go |
| P01_GOLD | 626 | 69.2% | 69.2% | +0.0 | 70% | 🟡 1 pts to go |
| P02 | 403 | 26.1% | 26.1% | -0.1 | 50% | ❌ 24 pts to go |
| P03 | 209 | 56.0% | 56.0% | -0.2 | 60% | 🟡 4 pts to go |
| P04 | 1571 | 9.9% | 9.9% | +0.0 | 40% | ❌ 30 pts to go |
| P05 | 378 | 21.7% | 21.7% | +0.3 | 45% | ❌ 23 pts to go |
| P06M | 1795 | 0.6% | 0.6% | -6.5 | n/a | no target |
| P06T | 9335 | 1.2% | 1.2% | -3.1 | n/a | no target |
| P06 | 279 | 32.6% | 32.6% | -15.6 | n/a | no target |
| P07 | 532 | 10.9% | 10.9% | -12.9 | n/a | no target |
| P08 | 11352 | 0.7% | 0.7% | -1.7 | n/a | no target |
| P09 | 349 | 9.2% | 9.2% | +0.5 | n/a | no target |
| P10R | 27809 | 0.1% | 0.1% |  | n/a | no target |
| P10 | 2631 | 2.0% | 2.0% | -0.1 | n/a | no target |
| P11 | 3190 | 1.0% | 1.0% | -5.8 | n/a | no target |
| P12 | 8 | 12.5% | 12.5% | +2.0 | n/a | no target |
| P13 | 12223 | 0.3% | 0.3% | +0.1 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 7.7% | 7.7% | -3.4 | n/a | no target |
| P01T | 137 | 30.7% | 30.7% | -13.9 | n/a | no target |
| P01_GOLD | 626 | 49.7% | 49.7% | -0.1 | 50% | 🟡 0 pts to go |
| P02 | 403 | 42.7% | 42.7% | +0.1 | n/a | no target |
| P03 | 209 | 58.4% | 58.4% | -0.3 | 60% | 🟡 2 pts to go |
| P04 | 1571 | 26.3% | 26.3% | -0.1 | n/a | no target |
| P05 | 378 | 16.7% | 16.7% | +0.0 | n/a | no target |
| P06M | 1795 | 0.5% | 0.5% | -3.7 | n/a | no target |
| P06T | 9335 | 1.3% | 1.3% | -2.7 | n/a | no target |
| P06 | 279 | 24.0% | 24.0% | -11.5 | n/a | no target |
| P07 | 532 | 10.0% | 10.0% | -8.7 | n/a | no target |
| P08 | 11352 | 0.5% | 0.5% | -1.0 | n/a | no target |
| P09 | 349 | 19.5% | 19.5% | +0.6 | n/a | no target |
| P10R | 27809 | 0.3% | 0.3% |  | n/a | no target |
| P10 | 2631 | 2.3% | 2.3% | -0.1 | n/a | no target |
| P11 | 3190 | 1.2% | 1.2% | -6.6 | n/a | no target |
| P12 | 8 | 12.5% | 12.5% | -8.6 | n/a | no target |
| P13 | 12223 | 0.6% | 0.6% | +0.2 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 19.2% | 19.2% | -8.6 | 15% | ✅ met |
| P01T | 137 | 21.2% | 21.2% | -8.1 | 15% | ✅ met |
| P01_GOLD | 626 | 35.3% | 35.3% | +0.2 | 40% | 🟡 5 pts to go |
| P02 | 403 | 13.6% | 13.9% | -0.3 | 25% | ❌ 11 pts to go |
| P03 | 209 | 21.5% | 21.5% | -0.1 | 25% | 🟡 4 pts to go |
| P04 | 1571 | 5.2% | 5.2% | +0.0 | 15% | 🟡 10 pts to go |
| P05 | 378 | 7.9% | 7.9% | -0.2 | 15% | 🟡 7 pts to go |
| P06M | 1795 | 0.8% | 0.8% | -5.2 | 15% | ❌ 14 pts to go |
| P06T | 9335 | 0.6% | 0.6% | -0.9 | 15% | ❌ 14 pts to go |
| P06 | 279 | 7.5% | 7.5% | -2.7 | 15% | 🟡 8 pts to go |
| P07 | 532 | 3.6% | 3.6% | -3.1 | 15% | ❌ 11 pts to go |
| P08 | 11352 | 0.3% | 0.3% | -0.6 | 15% | ❌ 15 pts to go |
| P09 | 349 | 0.9% | 0.9% | +0.1 | 15% | ❌ 14 pts to go |
| P10R | 27809 | 0.6% | 0.6% |  | 15% | ❌ 14 pts to go |
| P10 | 2631 | 1.5% | 1.5% | +0.1 | 15% | ❌ 14 pts to go |
| P11 | 3190 | 0.2% | 0.2% | -1.1 | 15% | ❌ 15 pts to go |
| P12 | 8 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 12223 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 7.7% | 7.7% | -3.4 | 15% | 🟡 7 pts to go |
| P01T | 137 | 23.4% | 23.4% | -9.2 | 25% | 🟡 2 pts to go |
| P01_GOLD | 626 | 29.1% | 29.1% | -0.1 | 25% | ✅ met |
| P02 | 403 | 28.0% | 28.0% | +0.0 | 15% | ✅ met |
| P03 | 209 | 25.8% | 25.8% | -0.2 | 15% | ✅ met |
| P04 | 1571 | 8.1% | 8.1% | -0.1 | 15% | 🟡 7 pts to go |
| P05 | 378 | 11.9% | 11.9% | -0.1 | 15% | 🟡 3 pts to go |
| P06M | 1795 | 0.2% | 0.2% | -2.2 | 15% | ❌ 15 pts to go |
| P06T | 9335 | 0.8% | 0.8% | -1.9 | 15% | ❌ 14 pts to go |
| P06 | 279 | 7.5% | 7.5% | -4.5 | 15% | 🟡 8 pts to go |
| P07 | 532 | 3.8% | 3.8% | -3.7 | 15% | ❌ 11 pts to go |
| P08 | 11352 | 0.3% | 0.3% | -0.7 | 15% | ❌ 15 pts to go |
| P09 | 349 | 0.9% | 0.9% | +0.1 | 15% | ❌ 14 pts to go |
| P10R | 27809 | 0.1% | 0.1% |  | 15% | ❌ 15 pts to go |
| P10 | 2631 | 1.3% | 1.3% | -0.1 | 15% | ❌ 14 pts to go |
| P11 | 3190 | 0.8% | 0.8% | -4.3 | 15% | ❌ 14 pts to go |
| P12 | 8 | 25.0% | 25.0% | -1.3 | 15% | ✅ met |
| P13 | 12223 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 3.8% | 3.8% | -1.8 | 20% | ❌ 16 pts to go |
| P01T | 137 | 7.3% | 7.3% | -2.5 | 20% | ❌ 13 pts to go |
| P01_GOLD | 626 | 4.3% | 4.3% | +0.0 | 20% | ❌ 16 pts to go |
| P02 | 403 | 1.5% | 1.5% | +0.0 | 20% | ❌ 18 pts to go |
| P03 | 209 | 1.9% | 1.9% | +0.0 | 20% | ❌ 18 pts to go |
| P04 | 1571 | 1.0% | 1.0% | +0.0 | 20% | ❌ 19 pts to go |
| P05 | 378 | 1.1% | 1.1% | +0.1 | 20% | ❌ 19 pts to go |
| P06M | 1795 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 9335 | 0.1% | 0.1% | -0.1 | 20% | ❌ 20 pts to go |
| P06 | 279 | 1.8% | 1.8% | -1.8 | 20% | ❌ 18 pts to go |
| P07 | 532 | 0.6% | 0.6% | -0.2 | 20% | ❌ 19 pts to go |
| P08 | 11352 | 0.0% | 0.0% | -0.2 | 20% | ❌ 20 pts to go |
| P09 | 349 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10R | 27809 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P10 | 2631 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 3190 | 0.1% | 0.1% | -0.5 | 20% | ❌ 20 pts to go |
| P12 | 8 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 12223 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 3.8% | 3.8% | -1.8 | 15% | ❌ 11 pts to go |
| P01T | 137 | 5.1% | 5.1% | -2.5 | 15% | 🟡 10 pts to go |
| P01_GOLD | 626 | 10.5% | 10.5% | -0.1 | 15% | 🟡 4 pts to go |
| P02 | 403 | 13.4% | 13.4% | +0.0 | 15% | 🟡 2 pts to go |
| P03 | 209 | 23.9% | 23.9% | -0.1 | 15% | ✅ met |
| P04 | 1571 | 4.5% | 4.5% | -0.1 | 15% | ❌ 10 pts to go |
| P05 | 378 | 2.9% | 2.9% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 1795 | 0.2% | 0.2% | -2.2 | 15% | ❌ 15 pts to go |
| P06T | 9335 | 0.4% | 0.4% | -1.0 | 15% | ❌ 15 pts to go |
| P06 | 279 | 3.6% | 3.6% | -1.8 | 15% | ❌ 11 pts to go |
| P07 | 532 | 1.9% | 1.9% | -1.7 | 15% | ❌ 13 pts to go |
| P08 | 11352 | 0.2% | 0.2% | -0.5 | 15% | ❌ 15 pts to go |
| P09 | 349 | 0.6% | 0.6% | +0.1 | 15% | ❌ 14 pts to go |
| P10R | 27809 | 0.1% | 0.1% |  | 15% | ❌ 15 pts to go |
| P10 | 2631 | 0.7% | 0.7% | -0.1 | 15% | ❌ 14 pts to go |
| P11 | 3190 | 0.3% | 0.3% | -1.8 | 15% | ❌ 15 pts to go |
| P12 | 8 | 0.0% | 0.0% | -5.3 | 15% | ❌ 15 pts to go |
| P13 | 12223 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 7.7% | 7.7% | -3.4 | 20% | ❌ 12 pts to go |
| P01T | 137 | 28.5% | 28.5% | -12.8 | 40% | ❌ 12 pts to go |
| P01_GOLD | 626 | 45.7% | 45.7% | -0.1 | 40% | ✅ met |
| P02 | 403 | 48.6% | 48.6% | +0.1 | 20% | ✅ met |
| P03 | 209 | 55.5% | 55.5% | -0.3 | 35% | ✅ met |
| P04 | 1571 | 30.2% | 30.2% | -0.1 | 20% | ✅ met |
| P05 | 378 | 16.7% | 16.7% | +0.0 | 20% | 🟡 3 pts to go |
| P06M | 1795 | 0.6% | 0.6% | -3.6 | 20% | ❌ 19 pts to go |
| P06T | 9335 | 1.7% | 1.7% | -2.8 | 20% | ❌ 18 pts to go |
| P06 | 279 | 24.0% | 24.0% | -11.5 | 20% | ✅ met |
| P07 | 532 | 8.6% | 8.6% | -6.1 | 20% | ❌ 11 pts to go |
| P08 | 11352 | 0.8% | 0.8% | -1.5 | 20% | ❌ 19 pts to go |
| P09 | 349 | 19.8% | 19.8% | -2.2 | 20% | 🟡 0 pts to go |
| P10R | 27809 | 0.4% | 0.4% |  | 20% | ❌ 20 pts to go |
| P10 | 2631 | 2.4% | 2.4% | -0.2 | 20% | ❌ 18 pts to go |
| P11 | 3190 | 1.3% | 1.3% | -6.7 | 20% | ❌ 19 pts to go |
| P12 | 8 | 12.5% | 12.5% | -3.3 | 20% | 🟡 8 pts to go |
| P13 | 12223 | 0.8% | 0.8% | +0.2 | 20% | ❌ 19 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 11.5% | 11.5% | +11.5 | n/a | no target |
| P01T | 137 | 0.7% | 0.7% | -0.4 | n/a | no target |
| P01_GOLD | 626 | 69.6% | 69.6% | -0.1 | 95% | ❌ 25 pts to go |
| P02 | 403 | 73.2% | 73.2% | -0.1 | 95% | ❌ 22 pts to go |
| P03 | 209 | 67.0% | 67.0% | -0.3 | 90% | ❌ 23 pts to go |
| P04 | 1571 | 58.4% | 58.4% | +0.0 | 85% | ❌ 27 pts to go |
| P05 | 378 | 35.4% | 35.4% | +0.5 | 75% | ❌ 40 pts to go |
| P06M | 1795 | 27.9% | 27.9% | +27.9 | n/a | no target |
| P06T | 9335 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 279 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 532 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 11352 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 349 | 90.0% | 90.0% | -0.8 | 100% | 🟡 10 pts to go |
| P10R | 27809 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2631 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3190 | 2.8% | 2.8% | -16.0 | 60% | ❌ 57 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 12223 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 11.5% | 11.5% | +11.5 | n/a | no target |
| P01T | 137 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 72.8% | 72.8% | -0.1 | 100% | ❌ 27 pts to go |
| P02 | 403 | 77.2% | 77.2% | +0.0 | 100% | ❌ 23 pts to go |
| P03 | 209 | 74.2% | 74.2% | -0.3 | n/a | no target |
| P04 | 1571 | 60.0% | 60.0% | +0.0 | 95% | ❌ 35 pts to go |
| P05 | 378 | 31.7% | 31.7% | +0.5 | 80% | ❌ 48 pts to go |
| P06M | 1795 | 27.9% | 27.9% | +27.9 | n/a | no target |
| P06T | 9335 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 279 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 532 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 11352 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 349 | 92.8% | 92.8% | -0.6 | 100% | 🟡 7 pts to go |
| P10R | 27809 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2631 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3190 | 2.9% | 2.9% | -17.1 | n/a | no target |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 12223 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 34.6% | 34.6% | +34.6 | n/a | no target |
| P01T | 137 | 0.7% | 0.7% | -0.4 | n/a | no target |
| P01_GOLD | 626 | 51.8% | 51.8% | -0.1 | 85% | ❌ 33 pts to go |
| P02 | 403 | 66.7% | 66.7% | -0.1 | 90% | ❌ 23 pts to go |
| P03 | 209 | 54.5% | 54.5% | -0.3 | 85% | ❌ 30 pts to go |
| P04 | 1571 | 64.2% | 64.2% | +0.1 | 90% | ❌ 26 pts to go |
| P05 | 378 | 34.9% | 34.9% | -0.3 | 75% | ❌ 40 pts to go |
| P06M | 1795 | 82.2% | 82.2% | +82.2 | n/a | no target |
| P06T | 9335 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 279 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 532 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 11352 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 349 | 86.0% | 86.0% | +0.4 | 95% | 🟡 9 pts to go |
| P10R | 27809 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2631 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3190 | 2.5% | 2.5% | -14.8 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 12223 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 42.3% | 42.3% | +42.3 | n/a | no target |
| P01T | 137 | 0.7% | 0.7% | -0.4 | n/a | no target |
| P01_GOLD | 626 | 51.9% | 51.9% | -0.2 | 85% | ❌ 33 pts to go |
| P02 | 403 | 61.0% | 61.0% | -0.1 | 90% | ❌ 29 pts to go |
| P03 | 209 | 56.0% | 56.0% | -0.2 | 85% | ❌ 29 pts to go |
| P04 | 1571 | 54.4% | 54.4% | +0.1 | 90% | ❌ 36 pts to go |
| P05 | 378 | 41.5% | 41.5% | -0.2 | 75% | ❌ 34 pts to go |
| P06M | 1795 | 63.2% | 63.2% | +63.2 | n/a | no target |
| P06T | 9335 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 279 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 532 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 11352 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 349 | 0.3% | 0.3% | +0.0 | 95% | ❌ 95 pts to go |
| P10R | 27809 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2631 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3190 | 2.1% | 2.1% | -12.0 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 12223 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 42.3% | 42.3% | +42.3 | n/a | no target |
| P01T | 137 | 86.1% | 86.1% | +4.6 | n/a | no target |
| P01_GOLD | 626 | 85.6% | 85.6% | -0.1 | 100% | ❌ 14 pts to go |
| P02 | 403 | 81.6% | 81.6% | -0.1 | 100% | ❌ 18 pts to go |
| P03 | 209 | 92.3% | 92.3% | +0.0 | n/a | no target |
| P04 | 1571 | 72.6% | 72.6% | +0.0 | 95% | ❌ 22 pts to go |
| P05 | 378 | 75.4% | 75.4% | -0.1 | 95% | ❌ 20 pts to go |
| P06M | 1795 | 92.1% | 92.1% | +91.5 | n/a | no target |
| P06T | 9335 | 84.2% | 84.2% | +0.8 | n/a | no target |
| P06 | 279 | 42.7% | 42.7% | -33.2 | n/a | no target |
| P07 | 532 | 34.0% | 34.0% | -43.0 | n/a | no target |
| P08 | 11352 | 21.3% | 21.3% | -63.6 | n/a | no target |
| P09 | 349 | 98.9% | 98.9% | -0.1 | 100% | 🟡 1 pts to go |
| P10R | 27809 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2631 | 86.2% | 86.2% | -12.2 | n/a | no target |
| P11 | 3190 | 32.9% | 32.9% | -57.0 | n/a | no target |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 12223 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 42.3% | 42.3% | +42.3 | n/a | no target |
| P01T | 137 | 86.1% | 86.1% | +4.6 | n/a | no target |
| P01_GOLD | 626 | 88.8% | 88.8% | -0.1 | 100% | ❌ 11 pts to go |
| P02 | 403 | 82.9% | 83.1% | +0.0 | 100% | ❌ 17 pts to go |
| P03 | 209 | 93.8% | 93.8% | +0.0 | n/a | no target |
| P04 | 1571 | 79.1% | 79.1% | +0.1 | 95% | ❌ 16 pts to go |
| P05 | 378 | 89.7% | 89.7% | -0.4 | 70% | ✅ met |
| P06M | 1795 | 92.1% | 92.1% | +91.5 | n/a | no target |
| P06T | 9335 | 84.2% | 84.2% | +0.8 | n/a | no target |
| P06 | 279 | 42.7% | 42.7% | -33.2 | n/a | no target |
| P07 | 532 | 34.0% | 34.0% | -43.0 | n/a | no target |
| P08 | 11352 | 21.3% | 21.3% | -63.6 | n/a | no target |
| P09 | 349 | 98.9% | 98.9% | -0.1 | 100% | 🟡 1 pts to go |
| P10R | 27809 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2631 | 86.2% | 86.2% | -12.2 | n/a | no target |
| P11 | 3190 | 33.0% | 33.0% | -57.3 | n/a | no target |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 12223 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 137 | 0.7% | 0.7% | -0.4 | n/a | no target · rows from a source that publishes bids: 4 rows, 25.0% filled |
| P01_GOLD | 626 | 17.3% | 17.3% | +0.0 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 367 rows, 29.4% filled |
| P02 | 403 | 13.2% | 13.2% | +0.1 | n/a | no target · rows from a source that publishes bids: 294 rows, 18.0% filled |
| P03 | 209 | 16.3% | 16.3% | +0.0 | n/a | no target · rows from a source that publishes bids: 140 rows, 24.3% filled |
| P04 | 1571 | 3.7% | 3.7% | +0.0 | n/a | no target · rows from a source that publishes bids: 878 rows, 6.6% filled |
| P05 | 378 | 3.4% | 3.4% | +0.0 | n/a | no target · rows from a source that publishes bids: 53 rows, 24.5% filled |
| P06M | 1795 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 9335 | 0.0% | 0.0% | -0.1 | n/a | no target · rows from a source that publishes bids: 34 rows, 5.9% filled |
| P06 | 279 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 532 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 11352 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 349 | 3.4% | 3.4% | +0.3 | n/a | no target · rows from a source that publishes bids: 336 rows, 3.6% filled |
| P10R | 27809 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2631 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 3190 | 0.4% | 0.4% | -2.3 | n/a | no target · rows from a source that publishes bids: 91 rows, 14.3% filled |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 8 rows, 0.0% filled |
| P13 | 12223 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 137 | 0.0% | 97.1% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 53.0% | 82.4% | -0.2 | 90% | ❌ 37 pts to go |
| P02 | 403 | 61.0% | 85.6% | -0.1 | 90% | ❌ 29 pts to go |
| P03 | 209 | 56.0% | 75.6% | -0.2 | 90% | ❌ 34 pts to go |
| P04 | 1571 | 45.4% | 85.6% | +0.1 | 90% | ❌ 45 pts to go |
| P05 | 378 | 0.0% | 80.7% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 1795 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 9335 | 0.0% | 99.6% | +0.0 | n/a | no target |
| P06 | 279 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 532 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 11352 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 349 | 2.3% | 3.7% | +0.2 | 90% | ❌ 88 pts to go |
| P10R | 27809 | 0.0% | 100.0% |  | n/a | no target |
| P10 | 2631 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 3190 | 1.9% | 98.6% | -10.8 | n/a | no target |
| P12 | 8 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 12223 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 137 | 0.7% | 97.8% | +0.7 | n/a | no target |
| P01_GOLD | 626 | 25.9% | 55.3% | -0.1 | 90% | ❌ 64 pts to go |
| P02 | 403 | 60.0% | 84.6% | +0.1 | n/a | no target |
| P03 | 209 | 30.6% | 50.2% | -0.2 | n/a | no target |
| P04 | 1571 | 49.7% | 89.9% | +0.0 | n/a | no target |
| P05 | 378 | 0.5% | 81.2% | +0.0 | n/a | no target |
| P06M | 1795 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 9335 | 0.2% | 99.8% | +0.2 | n/a | no target |
| P06 | 279 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 532 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 11352 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 349 | 43.6% | 45.0% | -0.8 | n/a | no target |
| P10R | 27809 | 0.0% | 100.0% |  | n/a | no target |
| P10 | 2631 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 3190 | 1.7% | 98.5% | -9.9 | n/a | no target |
| P12 | 8 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 12223 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 137 | 2.2% | 99.3% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 51.6% | 81.0% | +0.0 | 95% | ❌ 43 pts to go |
| P02 | 403 | 65.8% | 90.3% | +0.2 | n/a | no target |
| P03 | 209 | 58.9% | 78.5% | -0.2 | n/a | no target |
| P04 | 1571 | 50.3% | 90.5% | +0.0 | n/a | no target |
| P05 | 378 | 5.3% | 86.0% | +0.1 | n/a | no target |
| P06M | 1795 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 9335 | 0.2% | 99.9% | +0.2 | n/a | no target |
| P06 | 279 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 532 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 11352 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 349 | 66.2% | 67.6% | -1.3 | n/a | no target |
| P10R | 27809 | 0.0% | 100.0% |  | n/a | no target |
| P10 | 2631 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 3190 | 1.8% | 98.6% | -10.9 | n/a | no target |
| P12 | 8 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 12223 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 137 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 403 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 209 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 1571 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 378 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 1795 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 9335 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 279 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 532 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 11352 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 349 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 27809 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2631 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 3190 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 12223 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 137 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 403 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 209 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 1571 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 378 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 1795 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 9335 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 279 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 532 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 11352 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 349 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 27809 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2631 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 3190 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 12223 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 26 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 137 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 403 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 209 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 1571 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 378 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 1795 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 9335 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 279 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 532 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 11352 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 349 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 27809 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2631 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 3190 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 12223 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

