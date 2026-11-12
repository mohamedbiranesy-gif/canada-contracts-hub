# Coverage vs the downstream team's targets — 2026-11-12

Benchmarks (field × package with a numeric target): **46 of 438 met** (10.5%); 99 within 10 points; 293 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 195, P01T 199, P01_GOLD 644, P02 472, P03 271, P04 3641, P05 426, P06M 18370, P06T 43858, P06 256, P07 677, P08 21636, P09 314, P10R 0, P10 2160, P11 1640, P12 16, P13 163822

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 195 | 0.0% | 13.8% | 8 | vendor GST/HST number (179 rows) |
| P01T | 199 | 1.0% | 33.7% | 8 | payment terms (158 rows) |
| P01_GOLD | 644 | 24.2% | 70.7% | 9 | payment terms (227 rows) |
| P02 | 472 | 7.4% | 55.5% | 9 | PO rule (356 rows) |
| P03 | 271 | 14.8% | 58.3% | 9 | payment terms (133 rows) |
| P04 | 3641 | 1.2% | 18.0% | 6 | PO rule (3442 rows) |
| P05 | 426 | 1.2% | 17.8% | 7 | payment terms (351 rows) |
| P06M | 18370 | 0.0% | 2.6% | 7 | PO rule (18163 rows) |
| P06T | 43858 | 0.0% | 9.8% | 6 | PO rule (43627 rows) |
| P06 | 256 | 0.0% | 11.7% | 6 | reference to quote (PO / contract / vendor id) (256 rows) |
| P07 | 677 | 0.0% | 2.5% | 6 | reference to quote (PO / contract / vendor id) (677 rows) |
| P08 | 21636 | 0.0% | 0.6% | 6 | reference to quote (PO / contract / vendor id) (21636 rows) |
| P09 | 314 | 1.3% | 45.2% | 8 | payment terms (293 rows) |
| P10 | 2160 | 0.0% | 1.2% | 5 | reference to quote (PO / contract / vendor id) (2160 rows) |
| P11 | 1640 | 0.1% | 6.8% | 6 | PO rule (1575 rows) |
| P12 | 16 | 0.0% | 50.0% | 9 | PO rule (15 rows) |
| P13 | 163822 | 0.0% | 0.2% | 6 | reference to quote (PO / contract / vendor id) (163822 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 195 | 8 | 37 | 150 | 0 | 0 | 68 |
| P01T | 199 | 23 | 36 | 140 | 0 | 0 | 67 |
| P01_GOLD | 644 | 230 | 207 | 207 | 0 | 0 | 82 |
| P02 | 472 | 0 | 199 | 273 | 0 | 0 | 66 |
| P03 | 271 | 0 | 0 | 258 | 13 | 0 | 57 |
| P04 | 3641 | 0 | 0 | 2999 | 642 | 0 | 46 |
| P05 | 426 | 15 | 30 | 368 | 13 | 0 | 51 |
| P06M | 18370 | 0 | 11 | 18292 | 67 | 0 | 46 |
| P06T | 43858 | 0 | 24 | 28488 | 15346 | 0 | 38 |
| P06 | 256 | 16 | 47 | 193 | 0 | 0 | 70 |
| P07 | 677 | 0 | 21 | 633 | 23 | 0 | 54 |
| P08 | 21636 | 0 | 0 | 19043 | 2593 | 0 | 44 |
| P09 | 314 | 4 | 12 | 297 | 1 | 0 | 53 |
| P10 | 2160 | 3 | 13 | 1466 | 678 | 0 | 41 |
| P11 | 1640 | 7 | 13 | 36 | 0 | 1584 | 23 |
| P12 | 16 | 0 | 0 | 16 | 0 | 0 | 54 |
| P13 | 163822 | 12 | 65 | 163732 | 13 | 0 | 38 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 195 | 142 | 72.8% | tax treatment (30) |
| P01T | 199 | 117 | 58.8% | bill-to legal name and address (67) |
| P01_GOLD | 644 | 490 | 76.1% | bill-to legal name and address (95) |
| P02 | 472 | 324 | 68.6% | the buyer's PO / reference rule (86) |
| P03 | 271 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (271) |
| P04 | 3641 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (3641) |
| P05 | 426 | 47 | 11.0% | a confirmed invoicing / AP or finance channel (339) |
| P06M | 18370 | 186 | 1.0% | a confirmed invoicing / AP or finance channel (18121) |
| P06T | 43858 | 245 | 0.6% | a confirmed invoicing / AP or finance channel (43218) |
| P06 | 256 | 43 | 16.8% | the buyer's PO / reference rule (114) |
| P07 | 677 | 6 | 0.9% | the buyer's PO / reference rule (274) |
| P08 | 21636 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (21636) |
| P09 | 314 | 42 | 13.4% | a confirmed invoicing / AP or finance channel (262) |
| P10 | 2160 | 7 | 0.3% | a confirmed invoicing / AP or finance channel (2082) |
| P11 | 1640 | 14 | 0.9% | a confirmed invoicing / AP or finance channel (1584) |
| P12 | 16 | 4 | 25.0% | a confirmed invoicing / AP or finance channel (11) |
| P13 | 163822 | 44 | 0.0% | a confirmed invoicing / AP or finance channel (161479) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 195 | 6 | 3.1% | 7 | 0 | the vendor's GST/HST number (BN9) (177) |
| P01T | 199 | 78 | 39.2% | 4 | 0 | the vendor's GST/HST number (BN9) (69) |
| P01_GOLD | 644 | 409 | 63.5% | 12 | 0 | the vendor's GST/HST number (BN9) (159) |
| P02 | 472 | 215 | 45.6% | 21 | 0 | the vendor's GST/HST number (BN9) (206) |
| P03 | 271 | 17 | 6.3% | 0 | 137 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (98) |
| P04 | 3641 | 44 | 1.2% | 7 | 881 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2651) |
| P05 | 426 | 20 | 4.7% | 8 | 122 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (209) |
| P06M | 18370 | 6 | 0.0% | 11 | 483 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (17592) |
| P06T | 43858 | 259 | 0.6% | 15 | 10919 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (32244) |
| P06 | 256 | 25 | 9.8% | 49 | 0 | the vendor's GST/HST number (BN9) (118) |
| P07 | 677 | 6 | 0.9% | 109 | 34 | the vendor's GST/HST number (BN9) (309) |
| P08 | 21636 | 3 | 0.0% | 14 | 5000 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (16580) |
| P09 | 314 | 39 | 12.4% | 1 | 129 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (121) |
| P10 | 2160 | 7 | 0.3% | 14 | 271 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (1787) |
| P11 | 1640 | 7 | 0.4% | 3 | 0 | a confirmed invoicing / AP or finance channel (1569) |
| P12 | 16 | 3 | 18.8% | 0 | 6 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (5) |
| P13 | 163822 | 11 | 0.0% | 704 | 41619 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (119669) |
| **all** | 258597 | 1155 | 0.4% | 979 | 59601 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 187 | 0 | 0 | 0 | 128 | 8 | 0 | 158 | 168 | 13 |
| P01T | 176 | 0 | 0 | 0 | 102 | 61 | 28 | 145 | 159 | 8 |
| P01_GOLD | 414 | 0 | 0 | 0 | 13 | 77 | 30 | 207 | 242 | 64 |
| P02 | 472 | 0 | 472 | 0 | 38 | 51 | 15 | 356 | 285 | 24 |
| P03 | 271 | 0 | 271 | 0 | 17 | 43 | 26 | 131 | 141 | 24 |
| P04 | 3641 | 0 | 3641 | 0 | 1531 | 1289 | 970 | 3442 | 3186 | 164 |
| P05 | 411 | 0 | 359 | 0 | 81 | 89 | 38 | 342 | 353 | 53 |
| P06M | 18370 | 0 | 18370 | 0 | 12946 | 1235 | 103 | 18163 | 18024 | 455 |
| P06T | 43858 | 0 | 43858 | 0 | 39495 | 29209 | 18602 | 43627 | 43275 | 913 |
| P06 | 240 | 0 | 0 | 0 | 114 | 66 | 42 | 172 | 203 | 9 |
| P07 | 677 | 0 | 677 | 0 | 433 | 273 | 117 | 632 | 637 | 11 |
| P08 | 21636 | 0 | 21636 | 0 | 16486 | 9747 | 3821 | 21368 | 21025 | 409 |
| P09 | 310 | 0 | 289 | 0 | 13 | 73 | 1 | 283 | 296 | 48 |
| P10 | 2157 | 0 | 2124 | 0 | 1116 | 1173 | 981 | 2093 | 2055 | 110 |
| P11 | 1633 | 1584 | 1536 | 0 | 794 | 1159 | 510 | 1575 | 1576 | 59 |
| P12 | 16 | 0 | 14 | 0 | 1 | 4 | 0 | 15 | 15 | 1 |
| P13 | 163810 | 0 | 163370 | 0 | 131226 | 104892 | 20 | 163455 | 162609 | 37 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_phone | P13 | 52.5% | 95% | 69675 |
| buyer_logo_url | P13 | 64.4% | 95% | 50169 |
| buyer_legal_name_as_published | P13 | 36.0% | 60% | 39364 |
| buyer_bn_as_published | P13 | 8.2% | 30% | 35636 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 32729 |
| ap_system_hint | P13 | 0.4% | 20% | 32153 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 24440 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 24386 |
| buyer_payment_method_preference | P13 | 0.5% | 15% | 23699 |
| mta_sts | P13 | 86.3% | 100% | 22498 |
| tls_rpt | P13 | 86.3% | 100% | 22498 |
| bimi | P13 | 86.3% | 100% | 22498 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 8763 |
| vendor_registered_address | P08 | 30.2% | 70% | 8621 |
| ap_system_hint | P06T | 0.5% | 20% | 8538 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 6511 |
| buyer_tax_exempt_status | P06T | 0.2% | 15% | 6502 |
| buyer_payment_method_preference | P06T | 0.5% | 15% | 6376 |
| mta_sts | P06T | 86.4% | 100% | 5945 |
| tls_rpt | P06T | 86.4% | 100% | 5945 |
| bimi | P06T | 86.4% | 100% | 5945 |
| buyer_phone | P08 | 68.6% | 95% | 5720 |
| invoice_reference_hint | P08 | 1.2% | 25% | 5141 |
| buyer_legal_name_as_published | P08 | 55.0% | 75% | 4338 |
| buyer_ap_cycle_published | P08 | 0.1% | 20% | 4317 |
| buyer_bn_as_published | P08 | 15.3% | 35% | 4264 |
| vendor_bn9 | P08 | 30.6% | 50% | 4205 |
| vendor_phone | P08 | 65.8% | 85% | 4146 |
| ap_system_hint | P08 | 1.0% | 20% | 4113 |
| vendor_emails | P08 | 56.3% | 75% | 4043 |
| buyer_ap_cycle_published | P06M | 0.0% | 20% | 3668 |
| ap_system_hint | P06M | 0.7% | 20% | 3540 |
| buyer_esignature_preference | P08 | 0.5% | 15% | 3147 |
| buyer_tax_exempt_status | P08 | 0.5% | 15% | 3142 |
| buyer_payment_method_preference | P08 | 0.6% | 15% | 3113 |
| vendor_trading_name | P08 | 36.3% | 50% | 2959 |
| buyer_address | P08 | 82.3% | 95% | 2746 |
| buyer_esignature_preference | P06M | 0.3% | 15% | 2704 |
| buyer_tax_exempt_status | P06M | 0.4% | 15% | 2680 |
| buyer_payment_method_preference | P06M | 0.7% | 15% | 2623 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 91.3% | 91.3% | +2.2 | 50% | ✅ met |
| P01T | 199 | 94.5% | 94.5% | +0.7 | 50% | ✅ met |
| P01_GOLD | 644 | 92.4% | 94.6% | +0.2 | 95% | 🟡 3 pts to go |
| P02 | 472 | 75.0% | 76.7% | +1.0 | 95% | ❌ 20 pts to go |
| P03 | 271 | 80.8% | 84.5% | -0.6 | 95% | ❌ 14 pts to go |
| P04 | 3641 | 32.5% | 34.2% | +2.3 | 90% | ❌ 58 pts to go |
| P05 | 426 | 39.0% | 41.8% | +0.4 | 70% | ❌ 31 pts to go |
| P06M | 18370 | 91.3% | 91.3% | -0.5 | n/a | no target |
| P06T | 43858 | 99.0% | 99.0% | +0.4 | n/a | no target |
| P06 | 256 | 32.8% | 32.8% | -1.6 | 30% | ✅ met |
| P07 | 677 | 6.6% | 6.6% | -0.3 | 30% | ❌ 23 pts to go |
| P08 | 21636 | 1.2% | 1.2% | -0.1 | 25% | ❌ 24 pts to go |
| P09 | 314 | 99.0% | 99.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10 | 2160 | 3.1% | 3.2% | +0.0 | 25% | ❌ 22 pts to go |
| P11 | 1640 | 52.7% | 53.5% | +5.8 | 60% | 🟡 7 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 163822 | 99.6% | 99.6% | -0.1 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 199 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 644 | 5.9% | 5.9% | -0.2 | 50% | ❌ 44 pts to go |
| P02 | 472 | 6.4% | 6.4% | +0.2 | 50% | ❌ 44 pts to go |
| P03 | 271 | 1.5% | 1.5% | +0.0 | 40% | ❌ 38 pts to go |
| P04 | 3641 | 0.5% | 0.5% | +0.0 | 30% | ❌ 30 pts to go |
| P05 | 426 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 18370 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 43858 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 256 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 677 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21636 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 314 | 0.6% | 0.6% | -0.1 | 50% | ❌ 49 pts to go |
| P10 | 2160 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1640 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P12 | 16 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 163822 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 86.2% | 86.2% | +4.0 | n/a | no target |
| P01T | 199 | 76.4% | 76.4% | +1.9 | 50% | ✅ met |
| P01_GOLD | 644 | 67.4% | 67.4% | +0.6 | 85% | ❌ 18 pts to go |
| P02 | 472 | 65.7% | 65.7% | +0.9 | 90% | ❌ 24 pts to go |
| P03 | 271 | 60.5% | 60.5% | +0.8 | 85% | ❌ 24 pts to go |
| P04 | 3641 | 29.9% | 29.9% | +2.3 | 85% | ❌ 55 pts to go |
| P05 | 426 | 29.3% | 29.3% | +0.4 | 60% | ❌ 31 pts to go |
| P06M | 18370 | 91.1% | 91.1% | -0.4 | n/a | no target |
| P06T | 43858 | 98.9% | 98.9% | +0.5 | n/a | no target |
| P06 | 256 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 677 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21636 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 314 | 96.2% | 96.2% | +0.1 | 100% | 🟡 4 pts to go |
| P10 | 2160 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1640 | 49.6% | 49.6% | +6.3 | 60% | ❌ 10 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 163822 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 199 | 0.0% | 0.0% | +0.0 | 30% | ❌ 30 pts to go |
| P01_GOLD | 644 | 51.6% | 51.6% | +0.8 | 80% | ❌ 28 pts to go |
| P02 | 472 | 57.6% | 57.6% | +0.7 | 60% | 🟡 2 pts to go |
| P03 | 271 | 50.6% | 50.6% | +0.4 | 80% | ❌ 29 pts to go |
| P04 | 3641 | 25.0% | 25.0% | +2.1 | 50% | ❌ 25 pts to go |
| P05 | 426 | 11.7% | 11.7% | +0.3 | 40% | ❌ 28 pts to go |
| P06M | 18370 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 43858 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 256 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 677 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21636 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 314 | 82.8% | 82.8% | -0.6 | 50% | ✅ met |
| P10 | 2160 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1640 | 4.0% | 4.0% | -1.6 | 40% | ❌ 36 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 163822 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 199 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P01_GOLD | 644 | 61.5% | 61.5% | +1.1 | 85% | ❌ 24 pts to go |
| P02 | 472 | 57.2% | 57.2% | +1.0 | 90% | ❌ 33 pts to go |
| P03 | 271 | 59.0% | 59.0% | +0.4 | 85% | ❌ 26 pts to go |
| P04 | 3641 | 25.9% | 25.9% | +2.3 | 85% | ❌ 59 pts to go |
| P05 | 426 | 20.0% | 20.0% | +0.3 | 50% | ❌ 30 pts to go |
| P06M | 18370 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 43858 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 256 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 677 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21636 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 314 | 97.1% | 97.1% | +0.0 | 100% | 🟡 3 pts to go |
| P10 | 2160 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1640 | 4.4% | 4.4% | -1.6 | 60% | ❌ 56 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 163822 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 199 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 644 | 13.5% | 13.5% | +0.6 | 60% | ❌ 46 pts to go |
| P02 | 472 | 6.4% | 6.4% | +0.4 | 50% | ❌ 44 pts to go |
| P03 | 271 | 7.7% | 7.7% | -0.7 | 50% | ❌ 42 pts to go |
| P04 | 3641 | 2.0% | 2.0% | +0.2 | 40% | ❌ 38 pts to go |
| P05 | 426 | 0.7% | 0.7% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 18370 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 43858 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 256 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 677 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21636 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 314 | 3.5% | 3.5% | +0.2 | 50% | ❌ 46 pts to go |
| P10 | 2160 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1640 | 0.5% | 0.5% | -0.4 | n/a | no target |
| P12 | 16 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 163822 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 199 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 644 | 35.9% | 35.9% | +1.1 | 80% | ❌ 44 pts to go |
| P02 | 472 | 52.5% | 52.5% | +0.6 | 90% | ❌ 38 pts to go |
| P03 | 271 | 33.2% | 33.2% | +0.5 | 80% | ❌ 47 pts to go |
| P04 | 3641 | 23.3% | 23.3% | +1.7 | 85% | ❌ 62 pts to go |
| P05 | 426 | 5.6% | 5.6% | +0.1 | 50% | ❌ 44 pts to go |
| P06M | 18370 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 43858 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 256 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 677 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21636 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 314 | 74.5% | 74.5% | +0.2 | 95% | ❌ 20 pts to go |
| P10 | 2160 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1640 | 3.1% | 3.1% | -1.2 | 50% | ❌ 47 pts to go |
| P12 | 16 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 163822 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 199 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 644 | 8.4% | 8.4% | -0.1 | 50% | ❌ 42 pts to go |
| P02 | 472 | 6.4% | 6.4% | +0.2 | 50% | ❌ 44 pts to go |
| P03 | 271 | 1.8% | 1.8% | -0.1 | 30% | ❌ 28 pts to go |
| P04 | 3641 | 0.5% | 0.5% | +0.0 | 30% | ❌ 30 pts to go |
| P05 | 426 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 18370 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 43858 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 256 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 677 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21636 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 314 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P10 | 2160 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1640 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P12 | 16 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 163822 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 199 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 644 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 472 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 271 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3641 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 426 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 18370 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 43858 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 256 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 677 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 21636 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 314 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2160 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1640 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 163822 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 8.2% | 8.2% | -3.4 | 70% | ❌ 62 pts to go |
| P01T | 199 | 54.8% | 54.8% | +4.3 | 60% | 🟡 5 pts to go |
| P01_GOLD | 644 | 73.1% | 73.1% | -1.7 | 90% | ❌ 17 pts to go |
| P02 | 472 | 53.6% | 53.6% | +0.0 | 85% | ❌ 31 pts to go |
| P03 | 271 | 67.5% | 67.5% | -2.1 | 90% | ❌ 22 pts to go |
| P04 | 3641 | 35.6% | 35.6% | +0.6 | 75% | ❌ 39 pts to go |
| P05 | 426 | 53.1% | 53.1% | -1.6 | 50% | ✅ met |
| P06M | 18370 | 3.1% | 3.1% | -0.1 | n/a | no target |
| P06T | 43858 | 51.9% | 51.9% | +4.6 | n/a | no target |
| P06 | 256 | 43.4% | 43.4% | -0.6 | 40% | ✅ met |
| P07 | 677 | 32.6% | 32.6% | -0.4 | 50% | ❌ 17 pts to go |
| P08 | 21636 | 30.6% | 30.6% | +0.1 | 50% | ❌ 19 pts to go |
| P09 | 314 | 57.6% | 57.6% | -0.7 | 80% | ❌ 22 pts to go |
| P10 | 2160 | 34.5% | 34.5% | +0.0 | 40% | 🟡 6 pts to go |
| P11 | 1640 | 49.4% | 49.4% | +2.5 | 60% | ❌ 11 pts to go |
| P12 | 16 | 56.2% | 56.2% | -3.8 | 85% | ❌ 29 pts to go |
| P13 | 163822 | 28.8% | 28.8% | -2.9 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 56.4% | 56.4% | -3.3 | n/a | no target |
| P01T | 199 | 56.3% | 56.3% | +5.3 | n/a | no target |
| P01_GOLD | 644 | 71.6% | 71.6% | -1.1 | 95% | ❌ 23 pts to go |
| P02 | 472 | 74.6% | 74.6% | +0.8 | 95% | ❌ 20 pts to go |
| P03 | 271 | 69.4% | 69.4% | -2.5 | 95% | ❌ 26 pts to go |
| P04 | 3641 | 50.6% | 50.6% | +1.4 | 95% | ❌ 44 pts to go |
| P05 | 426 | 57.3% | 57.3% | -1.0 | 70% | ❌ 13 pts to go |
| P06M | 18370 | 43.8% | 43.8% | -2.2 | n/a | no target |
| P06T | 43858 | 61.0% | 61.0% | +4.8 | n/a | no target |
| P06 | 256 | 41.0% | 41.0% | +0.0 | 80% | ❌ 39 pts to go |
| P07 | 677 | 32.1% | 32.1% | +0.2 | 70% | ❌ 38 pts to go |
| P08 | 21636 | 30.2% | 30.2% | -0.1 | 70% | ❌ 40 pts to go |
| P09 | 314 | 86.3% | 86.3% | -0.3 | 100% | ❌ 14 pts to go |
| P10 | 2160 | 35.3% | 35.3% | -0.2 | 70% | ❌ 35 pts to go |
| P11 | 1640 | 55.1% | 55.1% | +2.6 | 75% | ❌ 20 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 163822 | 24.3% | 24.3% | -2.6 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 25.6% | 25.6% | +8.5 | n/a | no target |
| P01T | 199 | 58.8% | 58.8% | +5.2 | n/a | no target |
| P01_GOLD | 644 | 48.6% | 48.6% | -1.2 | 60% | ❌ 11 pts to go |
| P02 | 472 | 56.4% | 56.4% | +0.2 | 60% | 🟡 4 pts to go |
| P03 | 271 | 55.4% | 55.4% | +0.3 | 60% | 🟡 5 pts to go |
| P04 | 3641 | 43.2% | 43.2% | +1.1 | 55% | ❌ 12 pts to go |
| P05 | 426 | 24.2% | 24.2% | -0.4 | 50% | ❌ 26 pts to go |
| P06M | 18370 | 9.6% | 9.6% | +2.8 | n/a | no target |
| P06T | 43858 | 51.6% | 51.6% | +0.7 | n/a | no target |
| P06 | 256 | 48.4% | 48.4% | +0.8 | n/a | no target |
| P07 | 677 | 41.8% | 41.8% | +0.9 | 55% | ❌ 13 pts to go |
| P08 | 21636 | 36.3% | 36.3% | +0.1 | 50% | ❌ 14 pts to go |
| P09 | 314 | 72.0% | 72.0% | -0.3 | 70% | ✅ met |
| P10 | 2160 | 47.8% | 47.8% | +1.0 | 55% | 🟡 7 pts to go |
| P11 | 1640 | 55.2% | 55.2% | +3.0 | 50% | ✅ met |
| P12 | 16 | 87.5% | 87.5% | +0.8 | n/a | no target |
| P13 | 163822 | 3.1% | 3.1% | -0.3 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 42.1% | 42.1% | -8.3 | n/a | no target |
| P01T | 199 | 75.9% | 75.9% | +1.4 | n/a | no target |
| P01_GOLD | 644 | 48.9% | 48.9% | -1.6 | 70% | ❌ 21 pts to go |
| P02 | 472 | 57.0% | 57.0% | -1.2 | 70% | ❌ 13 pts to go |
| P03 | 271 | 51.3% | 51.3% | +0.0 | 70% | ❌ 19 pts to go |
| P04 | 3641 | 55.1% | 55.1% | +1.0 | 65% | 🟡 10 pts to go |
| P05 | 426 | 29.1% | 29.1% | +0.7 | 60% | ❌ 31 pts to go |
| P06M | 18370 | 32.5% | 32.5% | -4.1 | n/a | no target |
| P06T | 43858 | 73.8% | 73.8% | -6.2 | n/a | no target |
| P06 | 256 | 71.1% | 71.1% | +2.2 | 40% | ✅ met |
| P07 | 677 | 65.7% | 65.7% | +0.8 | 85% | ❌ 19 pts to go |
| P08 | 21636 | 65.8% | 65.8% | +0.5 | 85% | ❌ 19 pts to go |
| P09 | 314 | 57.3% | 57.3% | -2.0 | 85% | ❌ 28 pts to go |
| P10 | 2160 | 66.1% | 66.1% | +2.6 | 85% | ❌ 19 pts to go |
| P11 | 1640 | 63.8% | 63.8% | +1.9 | 75% | ❌ 11 pts to go |
| P12 | 16 | 37.5% | 37.5% | +10.8 | n/a | no target |
| P13 | 163822 | 91.8% | 91.8% | +0.6 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 46.7% | 46.7% | -9.9 | n/a | no target |
| P01T | 199 | 98.0% | 98.0% | +0.6 | n/a | no target |
| P01_GOLD | 644 | 78.6% | 78.6% | -1.0 | 90% | ❌ 11 pts to go |
| P02 | 472 | 82.4% | 82.4% | -1.5 | 90% | 🟡 8 pts to go |
| P03 | 271 | 86.7% | 86.7% | -1.1 | 90% | 🟡 3 pts to go |
| P04 | 3641 | 83.2% | 83.2% | -1.2 | 85% | 🟡 2 pts to go |
| P05 | 426 | 45.1% | 45.1% | +0.3 | 70% | ❌ 25 pts to go |
| P06M | 18370 | 38.2% | 38.2% | -5.4 | n/a | no target |
| P06T | 43858 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 256 | 99.2% | 99.2% | -0.1 | 50% | ✅ met |
| P07 | 677 | 99.9% | 99.9% | +0.0 | 100% | 🟡 0 pts to go |
| P08 | 21636 | 99.9% | 99.9% | +0.1 | 100% | 🟡 0 pts to go |
| P09 | 314 | 78.0% | 78.0% | -1.8 | 100% | ❌ 22 pts to go |
| P10 | 2160 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1640 | 97.7% | 97.7% | +0.4 | 100% | 🟡 2 pts to go |
| P12 | 16 | 56.2% | 56.2% | +2.9 | n/a | no target |
| P13 | 163822 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 19.0% | 19.0% | +3.5 | n/a | no target |
| P01T | 199 | 67.3% | 67.3% | +2.2 | n/a | no target |
| P01_GOLD | 644 | 42.1% | 42.1% | -1.4 | 70% | ❌ 28 pts to go |
| P02 | 472 | 48.3% | 48.3% | -0.4 | 75% | ❌ 27 pts to go |
| P03 | 271 | 43.9% | 43.9% | +0.6 | 75% | ❌ 31 pts to go |
| P04 | 3641 | 39.4% | 39.4% | +0.7 | 70% | ❌ 31 pts to go |
| P05 | 426 | 22.1% | 22.1% | +0.1 | 55% | ❌ 33 pts to go |
| P06M | 18370 | 6.1% | 6.1% | +1.3 | n/a | no target |
| P06T | 43858 | 66.5% | 66.5% | +4.4 | n/a | no target |
| P06 | 256 | 51.6% | 51.6% | +4.7 | n/a | no target |
| P07 | 677 | 51.4% | 51.4% | +1.4 | 70% | ❌ 19 pts to go |
| P08 | 21636 | 56.3% | 56.3% | +1.5 | 75% | ❌ 19 pts to go |
| P09 | 314 | 47.8% | 47.8% | -1.4 | 85% | ❌ 37 pts to go |
| P10 | 2160 | 44.3% | 44.3% | +0.7 | 80% | ❌ 36 pts to go |
| P11 | 1640 | 58.4% | 58.4% | +4.1 | 70% | ❌ 12 pts to go |
| P12 | 16 | 37.5% | 37.5% | -2.5 | n/a | no target |
| P13 | 163822 | 5.4% | 5.4% | +0.2 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 46.7% | 46.7% | -9.9 | n/a | no target |
| P01T | 199 | 96.0% | 96.0% | +1.2 | n/a | no target |
| P01_GOLD | 644 | 72.0% | 72.0% | -1.8 | 90% | ❌ 18 pts to go |
| P02 | 472 | 77.3% | 77.3% | -1.7 | 90% | ❌ 13 pts to go |
| P03 | 271 | 83.0% | 83.0% | -0.3 | 90% | 🟡 7 pts to go |
| P04 | 3641 | 78.0% | 78.0% | +1.6 | 85% | 🟡 7 pts to go |
| P05 | 426 | 43.7% | 43.7% | +0.6 | 75% | ❌ 31 pts to go |
| P06M | 18370 | 38.0% | 38.0% | -5.3 | n/a | no target |
| P06T | 43858 | 97.2% | 97.2% | +0.5 | n/a | no target |
| P06 | 256 | 92.2% | 92.2% | +1.7 | n/a | no target |
| P07 | 677 | 93.6% | 93.6% | +1.1 | 100% | 🟡 6 pts to go |
| P08 | 21636 | 92.8% | 92.8% | +2.0 | 100% | 🟡 7 pts to go |
| P09 | 314 | 66.2% | 66.2% | +0.1 | n/a | no target |
| P10 | 2160 | 89.9% | 89.9% | +3.1 | 100% | ❌ 10 pts to go |
| P11 | 1640 | 89.7% | 89.7% | +2.0 | n/a | no target |
| P12 | 16 | 56.2% | 56.2% | +9.5 | n/a | no target |
| P13 | 163822 | 68.3% | 68.3% | +3.1 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 44.6% | 44.6% | -1.9 | n/a | no target · QC vendors: 49 rows, 100.0% filled |
| P01T | 199 | 9.0% | 9.0% | -0.4 | n/a | no target · QC vendors: 5 rows, 60.0% filled |
| P01_GOLD | 644 | 43.2% | 43.2% | -0.6 | 95% | ❌ 52 pts to go · QC vendors: 52 rows, 98.1% filled |
| P02 | 472 | 56.4% | 56.4% | +0.8 | 95% | ❌ 39 pts to go · QC vendors: 113 rows, 100.0% filled |
| P03 | 271 | 46.1% | 46.1% | +0.1 | 95% | ❌ 49 pts to go · QC vendors: 22 rows, 100.0% filled |
| P04 | 3641 | 33.3% | 33.3% | +1.1 | 95% | ❌ 62 pts to go · QC vendors: 621 rows, 98.1% filled |
| P05 | 426 | 13.8% | 13.8% | -0.2 | n/a | no target · QC vendors: 35 rows, 94.3% filled |
| P06M | 18370 | 40.1% | 40.1% | -2.7 | n/a | no target · QC vendors: 5936 rows, 99.8% filled |
| P06T | 43858 | 4.5% | 4.5% | -0.8 | n/a | no target · QC vendors: 1926 rows, 75.6% filled |
| P06 | 256 | 8.2% | 8.2% | -0.2 | n/a | no target · QC vendors: 14 rows, 71.4% filled |
| P07 | 677 | 6.1% | 6.1% | -0.2 | n/a | no target · QC vendors: 35 rows, 74.3% filled |
| P08 | 21636 | 6.4% | 6.4% | -0.2 | n/a | no target · QC vendors: 1213 rows, 92.7% filled |
| P09 | 314 | 76.1% | 76.1% | -0.8 | 95% | ❌ 19 pts to go · QC vendors: 116 rows, 100.0% filled |
| P10 | 2160 | 15.3% | 15.3% | -0.3 | n/a | no target · QC vendors: 198 rows, 89.4% filled |
| P11 | 1640 | 12.8% | 12.8% | -2.0 | n/a | no target · QC vendors: 158 rows, 89.2% filled |
| P12 | 16 | 75.0% | 75.0% | +1.7 | n/a | no target · QC vendors: 3 rows, 100.0% filled |
| P13 | 163822 | 23.8% | 23.8% | -2.4 | n/a | no target · QC vendors: 38918 rows, 100.0% filled |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 55.9% | 55.9% | -3.0 | n/a | no target · vendors with a registry record: 109 rows, 100.0% filled |
| P01T | 199 | 56.3% | 56.3% | +5.3 | n/a | no target · vendors with a registry record: 112 rows, 100.0% filled |
| P01_GOLD | 644 | 79.8% | 79.8% | -1.7 | 100% | ❌ 20 pts to go · vendors with a registry record: 514 rows, 100.0% filled |
| P02 | 472 | 77.8% | 77.8% | +0.3 | 100% | ❌ 22 pts to go · vendors with a registry record: 367 rows, 100.0% filled |
| P03 | 271 | 78.2% | 78.2% | -2.8 | 100% | ❌ 22 pts to go · vendors with a registry record: 212 rows, 100.0% filled |
| P04 | 3641 | 51.3% | 51.3% | +1.6 | 100% | ❌ 49 pts to go · vendors with a registry record: 1868 rows, 100.0% filled |
| P05 | 426 | 62.0% | 62.0% | -1.3 | n/a | no target · vendors with a registry record: 264 rows, 100.0% filled |
| P06M | 18370 | 43.8% | 43.8% | -2.1 | n/a | no target · vendors with a registry record: 8038 rows, 100.0% filled |
| P06T | 43858 | 61.0% | 61.0% | +4.8 | n/a | no target · vendors with a registry record: 26771 rows, 100.0% filled |
| P06 | 256 | 41.8% | 41.8% | +0.4 | n/a | no target · vendors with a registry record: 107 rows, 100.0% filled |
| P07 | 677 | 32.6% | 32.6% | +0.3 | n/a | no target · vendors with a registry record: 221 rows, 100.0% filled |
| P08 | 21636 | 30.3% | 30.3% | -0.1 | n/a | no target · vendors with a registry record: 6558 rows, 100.0% filled |
| P09 | 314 | 90.1% | 90.1% | -0.5 | n/a | no target · vendors with a registry record: 283 rows, 100.0% filled |
| P10 | 2160 | 36.1% | 36.1% | -0.1 | n/a | no target · vendors with a registry record: 779 rows, 100.0% filled |
| P11 | 1640 | 55.8% | 55.8% | +2.2 | n/a | no target · vendors with a registry record: 915 rows, 100.0% filled |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 16 rows, 100.0% filled |
| P13 | 163822 | 24.3% | 24.3% | -2.6 | n/a | no target · vendors with a registry record: 39769 rows, 100.0% filled |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 95.9% | 95.9% | +2.1 | 90% | ✅ met |
| P01T | 199 | 69.3% | 69.3% | -3.1 | 90% | ❌ 21 pts to go |
| P01_GOLD | 644 | 88.0% | 88.0% | +0.3 | 95% | 🟡 7 pts to go |
| P02 | 472 | 89.2% | 89.2% | +1.4 | 95% | 🟡 6 pts to go |
| P03 | 271 | 84.1% | 84.1% | -0.3 | 85% | 🟡 1 pts to go |
| P04 | 3641 | 64.6% | 64.6% | +1.6 | 90% | ❌ 25 pts to go |
| P05 | 426 | 79.1% | 79.1% | +0.0 | 75% | ✅ met |
| P06M | 18370 | 93.3% | 93.3% | +1.7 | n/a | no target |
| P06T | 43858 | 33.4% | 33.4% | -3.9 | n/a | no target |
| P06 | 256 | 74.2% | 74.2% | +0.6 | 80% | 🟡 6 pts to go |
| P07 | 677 | 59.7% | 59.8% | -0.1 | 80% | ❌ 20 pts to go |
| P08 | 21636 | 55.0% | 55.0% | +0.6 | 75% | ❌ 20 pts to go |
| P09 | 314 | 76.8% | 76.8% | -0.1 | 95% | ❌ 18 pts to go |
| P10 | 2160 | 45.7% | 45.7% | -1.0 | 70% | ❌ 24 pts to go |
| P11 | 1640 | 29.3% | 29.3% | -2.0 | 65% | ❌ 36 pts to go |
| P12 | 16 | 75.0% | 75.0% | -5.0 | 80% | 🟡 5 pts to go |
| P13 | 163822 | 36.0% | 36.0% | -11.5 | 60% | ❌ 24 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 13.3% | 13.3% | -6.9 | 50% | ❌ 37 pts to go |
| P01T | 199 | 13.6% | 13.6% | -2.5 | n/a | no target |
| P01_GOLD | 644 | 19.1% | 19.1% | -0.4 | 40% | ❌ 21 pts to go |
| P02 | 472 | 19.3% | 19.3% | +0.2 | 40% | ❌ 21 pts to go |
| P03 | 271 | 21.8% | 21.8% | +0.5 | 40% | ❌ 18 pts to go |
| P04 | 3641 | 14.9% | 14.9% | -0.3 | 40% | ❌ 25 pts to go |
| P05 | 426 | 17.4% | 17.4% | -0.1 | 25% | 🟡 8 pts to go |
| P06M | 18370 | 9.3% | 9.3% | -2.3 | n/a | no target |
| P06T | 43858 | 4.9% | 4.9% | -2.0 | n/a | no target |
| P06 | 256 | 12.1% | 12.1% | -0.7 | 35% | ❌ 23 pts to go |
| P07 | 677 | 14.0% | 14.0% | -0.1 | 35% | ❌ 21 pts to go |
| P08 | 21636 | 15.3% | 15.3% | -0.1 | 35% | ❌ 20 pts to go |
| P09 | 314 | 16.6% | 16.6% | +0.3 | n/a | no target |
| P10 | 2160 | 5.7% | 5.7% | -1.0 | 30% | ❌ 24 pts to go |
| P11 | 1640 | 6.2% | 6.2% | -1.2 | n/a | no target |
| P12 | 16 | 6.2% | 6.2% | -0.5 | n/a | no target |
| P13 | 163822 | 8.2% | 8.2% | -4.1 | 30% | ❌ 22 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 199 | 84.9% | 84.9% | +0.5 | 100% | ❌ 15 pts to go |
| P01_GOLD | 644 | 91.0% | 91.0% | +0.3 | 100% | 🟡 9 pts to go |
| P02 | 472 | 96.4% | 96.4% | +0.9 | 100% | 🟡 4 pts to go |
| P03 | 271 | 89.3% | 89.3% | -0.1 | 100% | ❌ 11 pts to go |
| P04 | 3641 | 72.8% | 72.8% | +1.4 | 100% | ❌ 27 pts to go |
| P05 | 426 | 90.4% | 90.4% | +1.1 | 100% | 🟡 10 pts to go |
| P06M | 18370 | 99.4% | 99.4% | +0.2 | n/a | no target |
| P06T | 43858 | 57.6% | 57.6% | -1.7 | n/a | no target |
| P06 | 256 | 82.0% | 82.0% | +3.2 | 95% | ❌ 13 pts to go |
| P07 | 677 | 82.4% | 82.4% | +1.2 | 95% | ❌ 13 pts to go |
| P08 | 21636 | 82.3% | 82.3% | +4.0 | 95% | ❌ 13 pts to go |
| P09 | 314 | 96.5% | 96.5% | +0.4 | 100% | 🟡 4 pts to go |
| P10 | 2160 | 54.5% | 54.5% | +0.1 | 95% | ❌ 40 pts to go |
| P11 | 1640 | 59.8% | 59.8% | +10.4 | 80% | ❌ 20 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 163822 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 60.5% | 60.5% | -25.5 | n/a | no target |
| P01T | 199 | 69.3% | 69.3% | +1.1 | n/a | no target |
| P01_GOLD | 644 | 72.8% | 72.8% | -0.2 | 90% | ❌ 17 pts to go |
| P02 | 472 | 77.5% | 77.5% | -0.4 | 95% | ❌ 18 pts to go |
| P03 | 271 | 73.8% | 73.8% | -1.1 | 95% | ❌ 21 pts to go |
| P04 | 3641 | 69.3% | 69.3% | +0.4 | 95% | ❌ 26 pts to go |
| P05 | 426 | 72.5% | 72.5% | -1.0 | 90% | ❌ 18 pts to go |
| P06M | 18370 | 73.0% | 73.0% | -13.9 | n/a | no target |
| P06T | 43858 | 50.8% | 50.8% | -6.4 | n/a | no target |
| P06 | 256 | 70.3% | 70.3% | +1.8 | 95% | ❌ 25 pts to go |
| P07 | 677 | 66.2% | 66.2% | +1.4 | 90% | ❌ 24 pts to go |
| P08 | 21636 | 68.6% | 68.6% | +0.8 | 95% | ❌ 26 pts to go |
| P09 | 314 | 86.6% | 86.6% | -0.4 | 100% | ❌ 13 pts to go |
| P10 | 2160 | 53.5% | 53.5% | -1.8 | 95% | ❌ 42 pts to go |
| P11 | 1640 | 28.5% | 28.5% | -0.4 | 75% | ❌ 46 pts to go |
| P12 | 16 | 87.5% | 87.5% | -5.8 | n/a | no target |
| P13 | 163822 | 52.5% | 52.5% | -18.3 | 95% | ❌ 42 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 66.7% | 66.7% | -20.9 | n/a | no target |
| P01T | 199 | 83.9% | 83.9% | +0.6 | 95% | ❌ 11 pts to go |
| P01_GOLD | 644 | 84.5% | 84.5% | -0.3 | 90% | 🟡 6 pts to go |
| P02 | 472 | 90.3% | 90.3% | -0.3 | 95% | 🟡 5 pts to go |
| P03 | 271 | 83.4% | 83.4% | -2.2 | 95% | ❌ 12 pts to go |
| P04 | 3641 | 90.2% | 90.2% | +1.0 | 90% | ✅ met |
| P05 | 426 | 92.0% | 92.0% | -1.1 | 95% | 🟡 3 pts to go |
| P06M | 18370 | 78.0% | 78.0% | -15.2 | n/a | no target |
| P06T | 43858 | 69.4% | 69.4% | -5.5 | n/a | no target |
| P06 | 256 | 92.6% | 92.6% | +0.3 | 100% | 🟡 7 pts to go |
| P07 | 677 | 92.6% | 92.6% | +0.4 | 100% | 🟡 7 pts to go |
| P08 | 21636 | 94.0% | 94.0% | +1.7 | 100% | 🟡 6 pts to go |
| P09 | 314 | 73.6% | 73.6% | +0.6 | n/a | no target |
| P10 | 2160 | 93.0% | 93.0% | +1.7 | 100% | 🟡 7 pts to go |
| P11 | 1640 | 45.4% | 45.4% | +3.5 | 80% | ❌ 35 pts to go |
| P12 | 16 | 93.8% | 93.8% | -6.2 | n/a | no target |
| P13 | 163822 | 64.4% | 64.4% | -19.3 | 95% | ❌ 31 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 2.6% | 2.6% | -0.5 | n/a | no target |
| P01T | 199 | 8.5% | 8.5% | -0.9 | n/a | no target |
| P01_GOLD | 644 | 13.8% | 13.8% | -0.4 | 25% | ❌ 11 pts to go |
| P02 | 472 | 25.0% | 25.0% | -0.3 | 40% | ❌ 15 pts to go |
| P03 | 271 | 8.9% | 8.9% | -0.2 | 20% | ❌ 11 pts to go |
| P04 | 3641 | 3.5% | 3.5% | +0.0 | 20% | ❌ 16 pts to go |
| P05 | 426 | 3.3% | 3.3% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 18370 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 43858 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 256 | 5.5% | 5.5% | +0.4 | n/a | no target |
| P07 | 677 | 8.6% | 8.6% | +0.1 | n/a | no target |
| P08 | 21636 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P09 | 314 | 7.6% | 7.6% | -0.2 | n/a | no target |
| P10 | 2160 | 0.8% | 0.8% | +0.0 | n/a | no target |
| P11 | 1640 | 0.8% | 0.8% | -0.2 | n/a | no target |
| P12 | 16 | 6.2% | 6.2% | -0.5 | n/a | no target |
| P13 | 163822 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 12.3% | 12.3% | -6.3 | n/a | no target |
| P01T | 199 | 20.1% | 20.1% | -2.3 | 70% | ❌ 50 pts to go |
| P01_GOLD | 644 | 42.9% | 42.9% | -0.6 | 80% | ❌ 37 pts to go |
| P02 | 472 | 57.6% | 57.6% | +0.3 | 90% | ❌ 32 pts to go |
| P03 | 271 | 18.8% | 18.8% | +0.2 | 60% | ❌ 41 pts to go |
| P04 | 3641 | 22.9% | 22.9% | +1.3 | 85% | ❌ 62 pts to go |
| P05 | 426 | 12.0% | 12.0% | +0.4 | 50% | ❌ 38 pts to go |
| P06M | 18370 | 0.5% | 0.5% | -0.1 | n/a | no target |
| P06T | 43858 | 0.5% | 0.5% | -0.2 | n/a | no target |
| P06 | 256 | 16.0% | 16.0% | +0.6 | n/a | no target |
| P07 | 677 | 10.0% | 10.0% | -0.5 | n/a | no target |
| P08 | 21636 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P09 | 314 | 77.1% | 77.1% | -0.8 | 95% | ❌ 18 pts to go |
| P10 | 2160 | 1.6% | 1.6% | -0.1 | n/a | no target |
| P11 | 1640 | 14.2% | 14.2% | -2.5 | n/a | no target |
| P12 | 16 | 25.0% | 25.0% | -1.7 | n/a | no target |
| P13 | 163822 | 0.3% | 0.3% | -0.2 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 4.1% | 4.1% | -2.1 | n/a | no target |
| P01T | 199 | 10.1% | 10.1% | -0.3 | n/a | no target |
| P01_GOLD | 644 | 34.0% | 34.0% | +0.0 | 70% | ❌ 36 pts to go |
| P02 | 472 | 39.4% | 39.4% | +0.3 | 75% | ❌ 36 pts to go |
| P03 | 271 | 18.8% | 18.8% | +0.2 | 55% | ❌ 36 pts to go |
| P04 | 3641 | 22.8% | 22.8% | +1.2 | 75% | ❌ 52 pts to go |
| P05 | 426 | 11.0% | 11.0% | +0.3 | 50% | ❌ 39 pts to go |
| P06M | 18370 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06T | 43858 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 256 | 6.2% | 6.2% | +0.3 | n/a | no target |
| P07 | 677 | 5.0% | 5.0% | -0.2 | n/a | no target |
| P08 | 21636 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 314 | 74.5% | 74.5% | -0.7 | 95% | ❌ 20 pts to go |
| P10 | 2160 | 0.7% | 0.7% | -0.2 | n/a | no target |
| P11 | 1640 | 14.0% | 14.0% | -2.4 | n/a | no target |
| P12 | 16 | 18.8% | 18.8% | -1.2 | n/a | no target |
| P13 | 163822 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 5.1% | 5.1% | -2.7 | n/a | no target |
| P01T | 199 | 8.0% | 8.0% | -0.3 | n/a | no target |
| P01_GOLD | 644 | 57.8% | 57.9% | -0.2 | 80% | ❌ 22 pts to go |
| P02 | 472 | 45.8% | 46.0% | +0.1 | 75% | ❌ 29 pts to go |
| P03 | 271 | 37.6% | 37.6% | +0.3 | 70% | ❌ 32 pts to go |
| P04 | 3641 | 22.3% | 22.8% | +1.2 | 70% | ❌ 48 pts to go |
| P05 | 426 | 14.8% | 14.8% | +0.6 | 50% | ❌ 35 pts to go |
| P06M | 18370 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 43858 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P06 | 256 | 15.6% | 15.6% | -0.9 | n/a | no target |
| P07 | 677 | 1.9% | 1.9% | -0.1 | n/a | no target |
| P08 | 21636 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P09 | 314 | 47.1% | 47.1% | +0.5 | 80% | ❌ 33 pts to go |
| P10 | 2160 | 1.1% | 1.2% | -0.1 | n/a | no target |
| P11 | 1640 | 5.5% | 5.5% | -1.3 | n/a | no target |
| P12 | 16 | 37.5% | 37.5% | -2.5 | n/a | no target |
| P13 | 163822 | 0.1% | 0.1% | -0.1 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 13.8% | 13.8% | -4.8 | n/a | no target |
| P01T | 199 | 20.1% | 20.1% | -1.3 | 60% | ❌ 40 pts to go |
| P01_GOLD | 644 | 62.4% | 62.4% | -1.0 | 70% | 🟡 8 pts to go |
| P02 | 472 | 39.6% | 39.6% | -0.1 | 50% | ❌ 10 pts to go |
| P03 | 271 | 48.0% | 48.0% | -0.3 | 55% | 🟡 7 pts to go |
| P04 | 3641 | 12.5% | 12.5% | +0.3 | 40% | ❌ 28 pts to go |
| P05 | 426 | 17.1% | 17.1% | +0.0 | 40% | ❌ 23 pts to go |
| P06M | 18370 | 1.9% | 1.9% | -0.3 | n/a | no target |
| P06T | 43858 | 1.3% | 1.3% | -0.4 | n/a | no target |
| P06 | 256 | 20.7% | 20.7% | -1.3 | n/a | no target |
| P07 | 677 | 5.9% | 5.9% | -0.7 | n/a | no target |
| P08 | 21636 | 2.8% | 2.8% | -0.1 | n/a | no target |
| P09 | 314 | 5.7% | 5.7% | -0.2 | n/a | no target |
| P10 | 2160 | 4.9% | 4.9% | +0.3 | n/a | no target |
| P11 | 1640 | 3.9% | 3.9% | -1.3 | n/a | no target |
| P12 | 16 | 6.2% | 6.2% | -0.5 | n/a | no target |
| P13 | 163822 | 0.7% | 0.7% | -0.3 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 19.0% | 19.0% | -2.7 | n/a | no target |
| P01T | 199 | 27.1% | 27.1% | -1.5 | 65% | ❌ 38 pts to go |
| P01_GOLD | 644 | 67.9% | 67.9% | -1.1 | 70% | 🟡 2 pts to go |
| P02 | 472 | 24.6% | 24.6% | +0.4 | 50% | ❌ 25 pts to go |
| P03 | 271 | 51.7% | 51.7% | -0.8 | 60% | 🟡 8 pts to go |
| P04 | 3641 | 5.5% | 5.5% | +0.1 | 40% | ❌ 34 pts to go |
| P05 | 426 | 19.7% | 19.7% | +0.0 | 45% | ❌ 25 pts to go |
| P06M | 18370 | 1.1% | 1.1% | -0.3 | n/a | no target |
| P06T | 43858 | 0.5% | 0.5% | -0.2 | n/a | no target |
| P06 | 256 | 32.8% | 32.8% | -1.6 | n/a | no target |
| P07 | 677 | 6.6% | 6.6% | -0.3 | n/a | no target |
| P08 | 21636 | 1.2% | 1.2% | -0.1 | n/a | no target |
| P09 | 314 | 9.9% | 9.9% | +0.1 | n/a | no target |
| P10 | 2160 | 3.1% | 3.1% | +0.0 | n/a | no target |
| P11 | 1640 | 4.0% | 4.0% | -1.1 | n/a | no target |
| P12 | 16 | 6.2% | 6.2% | -0.5 | n/a | no target |
| P13 | 163822 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 9.2% | 9.2% | -3.2 | n/a | no target |
| P01T | 199 | 13.1% | 13.1% | -0.4 | n/a | no target |
| P01_GOLD | 644 | 48.9% | 48.9% | -0.9 | 50% | 🟡 1 pts to go |
| P02 | 472 | 37.5% | 37.5% | +0.2 | n/a | no target |
| P03 | 271 | 50.9% | 50.9% | -1.2 | 60% | 🟡 9 pts to go |
| P04 | 3641 | 12.2% | 12.2% | +0.3 | n/a | no target |
| P05 | 426 | 15.0% | 15.0% | -0.2 | n/a | no target |
| P06M | 18370 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P06T | 43858 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 256 | 23.8% | 23.8% | -1.8 | n/a | no target |
| P07 | 677 | 7.5% | 7.5% | -0.8 | n/a | no target |
| P08 | 21636 | 0.5% | 0.5% | -0.1 | n/a | no target |
| P09 | 314 | 18.5% | 18.5% | +0.9 | n/a | no target |
| P10 | 2160 | 2.4% | 2.4% | +0.0 | n/a | no target |
| P11 | 1640 | 3.1% | 3.1% | -1.6 | n/a | no target |
| P12 | 16 | 12.5% | 12.5% | -0.8 | n/a | no target |
| P13 | 163822 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 8.2% | 8.2% | -3.4 | 15% | 🟡 7 pts to go |
| P01T | 199 | 12.6% | 12.6% | +0.1 | 15% | 🟡 2 pts to go |
| P01_GOLD | 644 | 34.6% | 34.6% | -0.7 | 40% | 🟡 5 pts to go |
| P02 | 472 | 12.7% | 12.9% | -0.2 | 25% | ❌ 12 pts to go |
| P03 | 271 | 17.0% | 17.0% | -0.5 | 25% | 🟡 8 pts to go |
| P04 | 3641 | 2.7% | 2.7% | +0.0 | 15% | ❌ 12 pts to go |
| P05 | 426 | 6.6% | 6.6% | +0.0 | 15% | 🟡 8 pts to go |
| P06M | 18370 | 0.7% | 0.7% | -0.2 | 15% | ❌ 14 pts to go |
| P06T | 43858 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |
| P06 | 256 | 10.9% | 10.9% | +0.3 | 15% | 🟡 4 pts to go |
| P07 | 677 | 4.1% | 4.1% | -0.2 | 15% | ❌ 11 pts to go |
| P08 | 21636 | 0.6% | 0.6% | +0.0 | 15% | ❌ 14 pts to go |
| P09 | 314 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2160 | 1.2% | 1.2% | -0.1 | 15% | ❌ 14 pts to go |
| P11 | 1640 | 1.3% | 1.3% | -0.2 | 15% | ❌ 14 pts to go |
| P12 | 16 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 163822 | 0.5% | 0.5% | -0.2 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 3.6% | 3.6% | -1.8 | 15% | ❌ 11 pts to go |
| P01T | 199 | 11.1% | 11.1% | -0.4 | 25% | ❌ 14 pts to go |
| P01_GOLD | 644 | 28.4% | 28.4% | -0.8 | 25% | ✅ met |
| P02 | 472 | 25.2% | 25.2% | -0.1 | 15% | ✅ met |
| P03 | 271 | 22.5% | 22.5% | +0.4 | 15% | ✅ met |
| P04 | 3641 | 4.0% | 4.0% | +0.0 | 15% | ❌ 11 pts to go |
| P05 | 426 | 11.3% | 11.3% | +0.2 | 15% | 🟡 4 pts to go |
| P06M | 18370 | 0.4% | 0.4% | -0.1 | 15% | ❌ 15 pts to go |
| P06T | 43858 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 256 | 9.0% | 9.0% | +0.6 | 15% | 🟡 6 pts to go |
| P07 | 677 | 2.7% | 2.7% | -0.2 | 15% | ❌ 12 pts to go |
| P08 | 21636 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |
| P09 | 314 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2160 | 1.5% | 1.5% | -0.1 | 15% | ❌ 14 pts to go |
| P11 | 1640 | 2.0% | 2.0% | -0.7 | 15% | ❌ 13 pts to go |
| P12 | 16 | 18.8% | 18.8% | -1.2 | 15% | ✅ met |
| P13 | 163822 | 0.1% | 0.1% | -0.1 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 1.5% | 1.5% | -0.8 | 20% | ❌ 18 pts to go |
| P01T | 199 | 4.0% | 4.0% | -0.2 | 20% | ❌ 16 pts to go |
| P01_GOLD | 644 | 4.3% | 4.3% | -0.2 | 20% | ❌ 16 pts to go |
| P02 | 472 | 1.5% | 1.5% | +0.0 | 20% | ❌ 18 pts to go |
| P03 | 271 | 1.8% | 1.8% | +0.3 | 20% | ❌ 18 pts to go |
| P04 | 3641 | 0.7% | 0.7% | +0.1 | 20% | ❌ 19 pts to go |
| P05 | 426 | 1.2% | 1.2% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 18370 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 43858 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 256 | 1.6% | 1.6% | +0.1 | 20% | ❌ 18 pts to go |
| P07 | 677 | 0.4% | 0.4% | +0.0 | 20% | ❌ 20 pts to go |
| P08 | 21636 | 0.1% | 0.1% | +0.1 | 20% | ❌ 20 pts to go |
| P09 | 314 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2160 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 1640 | 0.1% | 0.1% | -0.2 | 20% | ❌ 20 pts to go |
| P12 | 16 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 163822 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 1.0% | 1.0% | -0.6 | 15% | ❌ 14 pts to go |
| P01T | 199 | 3.0% | 3.0% | -0.1 | 15% | ❌ 12 pts to go |
| P01_GOLD | 644 | 10.1% | 10.1% | -0.3 | 15% | 🟡 5 pts to go |
| P02 | 472 | 11.9% | 11.9% | -0.1 | 15% | 🟡 3 pts to go |
| P03 | 271 | 20.3% | 20.3% | +0.1 | 15% | ✅ met |
| P04 | 3641 | 2.3% | 2.3% | +0.0 | 15% | ❌ 13 pts to go |
| P05 | 426 | 2.8% | 2.8% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 18370 | 0.3% | 0.3% | +0.0 | 15% | ❌ 15 pts to go |
| P06T | 43858 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 256 | 5.1% | 5.1% | +0.0 | 15% | 🟡 10 pts to go |
| P07 | 677 | 1.5% | 1.5% | -0.1 | 15% | ❌ 14 pts to go |
| P08 | 21636 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |
| P09 | 314 | 0.6% | 0.6% | -0.1 | 15% | ❌ 14 pts to go |
| P10 | 2160 | 1.1% | 1.1% | +0.1 | 15% | ❌ 14 pts to go |
| P11 | 1640 | 0.9% | 0.9% | -0.3 | 15% | ❌ 14 pts to go |
| P12 | 16 | 6.2% | 6.2% | -0.5 | 15% | 🟡 9 pts to go |
| P13 | 163822 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 10.3% | 10.3% | -3.7 | 20% | 🟡 10 pts to go |
| P01T | 199 | 13.6% | 13.6% | -0.5 | 40% | ❌ 26 pts to go |
| P01_GOLD | 644 | 45.3% | 45.3% | -0.9 | 40% | ✅ met |
| P02 | 472 | 43.0% | 43.0% | +0.1 | 20% | ✅ met |
| P03 | 271 | 48.0% | 48.0% | -1.0 | 35% | ✅ met |
| P04 | 3641 | 14.6% | 14.6% | +0.4 | 20% | 🟡 5 pts to go |
| P05 | 426 | 15.5% | 15.5% | +0.1 | 20% | 🟡 4 pts to go |
| P06M | 18370 | 0.7% | 0.7% | -0.1 | 20% | ❌ 19 pts to go |
| P06T | 43858 | 0.5% | 0.5% | -0.2 | 20% | ❌ 20 pts to go |
| P06 | 256 | 23.8% | 23.8% | -1.5 | 20% | ✅ met |
| P07 | 677 | 8.1% | 8.1% | -0.5 | 20% | ❌ 12 pts to go |
| P08 | 21636 | 1.0% | 1.0% | +0.0 | 20% | ❌ 19 pts to go |
| P09 | 314 | 18.5% | 18.5% | +0.3 | 20% | 🟡 2 pts to go |
| P10 | 2160 | 3.8% | 3.8% | +0.1 | 20% | ❌ 16 pts to go |
| P11 | 1640 | 3.5% | 3.5% | -1.3 | 20% | ❌ 16 pts to go |
| P12 | 16 | 6.2% | 6.2% | -0.5 | 20% | ❌ 14 pts to go |
| P13 | 163822 | 0.4% | 0.4% | -0.1 | 20% | ❌ 20 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 22.6% | 22.6% | -10.7 | n/a | no target |
| P01T | 199 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P01_GOLD | 644 | 72.0% | 72.0% | +2.5 | 95% | ❌ 23 pts to go |
| P02 | 472 | 65.3% | 65.3% | +2.4 | 95% | ❌ 30 pts to go |
| P03 | 271 | 57.6% | 57.6% | +4.4 | 90% | ❌ 32 pts to go |
| P04 | 3641 | 27.5% | 27.5% | +2.7 | 85% | ❌ 58 pts to go |
| P05 | 426 | 38.0% | 38.0% | +0.3 | 75% | ❌ 37 pts to go |
| P06M | 18370 | 30.7% | 30.7% | -5.4 | n/a | no target |
| P06T | 43858 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 256 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 677 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21636 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 314 | 90.1% | 90.1% | +1.8 | 100% | 🟡 10 pts to go |
| P10 | 2160 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1640 | 4.6% | 4.6% | -1.4 | 60% | ❌ 55 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 163822 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 22.6% | 22.6% | -10.7 | n/a | no target |
| P01T | 199 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 644 | 73.8% | 73.8% | +1.0 | 100% | ❌ 26 pts to go |
| P02 | 472 | 67.4% | 67.4% | +1.1 | 100% | ❌ 33 pts to go |
| P03 | 271 | 60.1% | 60.1% | +1.2 | n/a | no target |
| P04 | 3641 | 27.9% | 27.9% | +2.4 | 95% | ❌ 67 pts to go |
| P05 | 426 | 33.8% | 33.8% | +0.4 | 80% | ❌ 46 pts to go |
| P06M | 18370 | 30.7% | 30.7% | -5.4 | n/a | no target |
| P06T | 43858 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 256 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 677 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21636 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 314 | 92.0% | 92.0% | +0.5 | 100% | 🟡 8 pts to go |
| P10 | 2160 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1640 | 4.8% | 4.8% | -1.6 | n/a | no target |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 163822 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 84.6% | 84.6% | +4.8 | n/a | no target |
| P01T | 199 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P01_GOLD | 644 | 52.5% | 52.5% | +0.9 | 85% | ❌ 32 pts to go |
| P02 | 472 | 58.5% | 58.5% | +1.0 | 90% | ❌ 32 pts to go |
| P03 | 271 | 43.5% | 43.5% | +0.9 | 85% | ❌ 42 pts to go |
| P04 | 3641 | 29.9% | 29.9% | +2.0 | 90% | ❌ 60 pts to go |
| P05 | 426 | 32.6% | 32.6% | -0.1 | 75% | ❌ 42 pts to go |
| P06M | 18370 | 86.4% | 86.4% | -0.7 | n/a | no target |
| P06T | 43858 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 256 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 677 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21636 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 314 | 82.5% | 82.5% | -0.9 | 95% | ❌ 12 pts to go |
| P10 | 2160 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1640 | 4.0% | 4.0% | -1.4 | n/a | no target |
| P12 | 16 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 163822 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 83.6% | 83.6% | +5.3 | n/a | no target |
| P01T | 199 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P01_GOLD | 644 | 52.6% | 52.6% | +0.8 | 85% | ❌ 32 pts to go |
| P02 | 472 | 53.2% | 53.2% | +0.6 | 90% | ❌ 37 pts to go |
| P03 | 271 | 43.5% | 43.5% | -0.2 | 85% | ❌ 42 pts to go |
| P04 | 3641 | 25.5% | 25.5% | +1.7 | 90% | ❌ 64 pts to go |
| P05 | 426 | 42.5% | 42.5% | -0.9 | 75% | ❌ 32 pts to go |
| P06M | 18370 | 78.4% | 78.4% | +0.6 | n/a | no target |
| P06T | 43858 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 256 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 677 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21636 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 314 | 0.3% | 0.3% | +0.0 | 95% | ❌ 95 pts to go |
| P10 | 2160 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1640 | 3.1% | 3.1% | -1.4 | n/a | no target |
| P12 | 16 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 163822 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 93.3% | 93.3% | +3.4 | n/a | no target |
| P01T | 199 | 95.0% | 95.0% | +0.7 | n/a | no target |
| P01_GOLD | 644 | 85.6% | 85.6% | +0.3 | 100% | ❌ 14 pts to go |
| P02 | 472 | 77.3% | 77.3% | +0.9 | 100% | ❌ 23 pts to go |
| P03 | 271 | 91.5% | 91.5% | +0.2 | n/a | no target |
| P04 | 3641 | 51.1% | 51.1% | +2.3 | 95% | ❌ 44 pts to go |
| P05 | 426 | 77.5% | 77.5% | +0.0 | 95% | ❌ 18 pts to go |
| P06M | 18370 | 99.1% | 99.1% | +0.2 | n/a | no target |
| P06T | 43858 | 92.6% | 92.6% | +2.0 | n/a | no target |
| P06 | 256 | 22.3% | 22.3% | -0.8 | n/a | no target |
| P07 | 677 | 12.7% | 12.7% | -1.1 | n/a | no target |
| P08 | 21636 | 6.5% | 6.5% | -0.6 | n/a | no target |
| P09 | 314 | 98.4% | 98.4% | -0.3 | 100% | 🟡 2 pts to go |
| P10 | 2160 | 70.7% | 70.7% | -0.3 | n/a | no target |
| P11 | 1640 | 71.6% | 71.6% | +3.5 | n/a | no target |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 163822 | 99.6% | 99.6% | -0.1 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 93.3% | 93.3% | +3.4 | n/a | no target |
| P01T | 199 | 95.0% | 95.0% | +0.7 | n/a | no target |
| P01_GOLD | 644 | 88.7% | 88.7% | +0.2 | 100% | ❌ 11 pts to go |
| P02 | 472 | 78.4% | 78.6% | +0.9 | 100% | ❌ 22 pts to go |
| P03 | 271 | 92.3% | 92.3% | +0.3 | n/a | no target |
| P04 | 3641 | 54.4% | 54.4% | +2.5 | 95% | ❌ 41 pts to go |
| P05 | 426 | 89.4% | 89.4% | -0.2 | 70% | ✅ met |
| P06M | 18370 | 99.1% | 99.1% | +0.2 | n/a | no target |
| P06T | 43858 | 92.6% | 92.6% | +2.0 | n/a | no target |
| P06 | 256 | 22.3% | 22.3% | -0.8 | n/a | no target |
| P07 | 677 | 12.7% | 12.7% | -1.1 | n/a | no target |
| P08 | 21636 | 6.5% | 6.5% | -0.6 | n/a | no target |
| P09 | 314 | 98.4% | 98.4% | -0.3 | 100% | 🟡 2 pts to go |
| P10 | 2160 | 70.7% | 70.7% | -0.3 | n/a | no target |
| P11 | 1640 | 71.6% | 71.6% | +3.4 | n/a | no target |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 163822 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 199 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 644 | 16.6% | 16.6% | -0.2 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 378 rows, 28.3% filled |
| P02 | 472 | 11.0% | 11.0% | -0.2 | n/a | no target · rows from a source that publishes bids: 299 rows, 17.4% filled |
| P03 | 271 | 14.4% | 14.4% | +1.5 | n/a | no target · rows from a source that publishes bids: 144 rows, 27.1% filled |
| P04 | 3641 | 1.6% | 1.6% | +0.1 | n/a | no target · rows from a source that publishes bids: 933 rows, 6.3% filled |
| P05 | 426 | 2.6% | 2.6% | +0.0 | n/a | no target · rows from a source that publishes bids: 52 rows, 21.2% filled |
| P06M | 18370 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 43858 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 256 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 677 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 21636 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 314 | 4.5% | 4.5% | +0.3 | n/a | no target · rows from a source that publishes bids: 300 rows, 4.7% filled |
| P10 | 2160 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1640 | 0.5% | 0.5% | -0.4 | n/a | no target · rows from a source that publishes bids: 74 rows, 12.2% filled |
| P12 | 16 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 16 rows, 0.0% filled |
| P13 | 163822 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 199 | 0.0% | 98.0% | +0.0 | n/a | no target |
| P01_GOLD | 644 | 53.7% | 82.3% | +0.5 | 90% | ❌ 36 pts to go |
| P02 | 472 | 53.2% | 87.3% | +0.8 | 90% | ❌ 37 pts to go |
| P03 | 271 | 45.4% | 80.1% | +0.9 | 90% | ❌ 45 pts to go |
| P04 | 3641 | 20.6% | 93.0% | +1.5 | 90% | ❌ 69 pts to go |
| P05 | 426 | 0.0% | 82.9% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 18370 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 43858 | 0.0% | 99.8% | +0.0 | n/a | no target |
| P06 | 256 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 677 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 21636 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 314 | 2.5% | 4.1% | +0.2 | 90% | ❌ 88 pts to go |
| P10 | 2160 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1640 | 2.7% | 97.3% | -1.4 | n/a | no target |
| P12 | 16 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 163822 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 199 | 0.5% | 98.5% | +0.0 | n/a | no target |
| P01_GOLD | 644 | 26.6% | 55.1% | +0.7 | 90% | ❌ 63 pts to go |
| P02 | 472 | 51.9% | 86.0% | +0.4 | n/a | no target |
| P03 | 271 | 24.7% | 59.4% | +0.4 | n/a | no target |
| P04 | 3641 | 22.5% | 94.9% | +1.5 | n/a | no target |
| P05 | 426 | 0.5% | 83.3% | +0.0 | n/a | no target |
| P06M | 18370 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 43858 | 0.1% | 99.9% | +0.0 | n/a | no target |
| P06 | 256 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 677 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 21636 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 314 | 40.8% | 42.4% | -0.2 | n/a | no target |
| P10 | 2160 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1640 | 2.7% | 97.3% | -1.0 | n/a | no target |
| P12 | 16 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 163822 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 199 | 2.0% | 100.0% | -0.1 | n/a | no target |
| P01_GOLD | 644 | 52.5% | 81.1% | +0.7 | 95% | ❌ 42 pts to go |
| P02 | 472 | 57.4% | 91.5% | +1.0 | n/a | no target |
| P03 | 271 | 48.3% | 83.0% | +1.5 | n/a | no target |
| P04 | 3641 | 23.2% | 95.6% | +2.0 | n/a | no target |
| P05 | 426 | 4.7% | 87.6% | +0.2 | n/a | no target |
| P06M | 18370 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 43858 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 256 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 677 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 21636 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 314 | 61.8% | 63.4% | -0.7 | n/a | no target |
| P10 | 2160 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1640 | 2.8% | 97.4% | -1.3 | n/a | no target |
| P12 | 16 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 163822 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 84.1% | 84.1% | -15.9 | 100% | ❌ 16 pts to go |
| P01T | 199 | 94.5% | 94.5% | -5.5 | 100% | 🟡 6 pts to go |
| P01_GOLD | 644 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P02 | 472 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P03 | 271 | 99.6% | 99.6% | -0.4 | 100% | 🟡 0 pts to go |
| P04 | 3641 | 99.5% | 99.5% | -0.5 | 100% | 🟡 0 pts to go |
| P05 | 426 | 99.5% | 99.5% | -0.5 | 100% | 🟡 0 pts to go |
| P06M | 18370 | 89.9% | 89.9% | -10.1 | 100% | ❌ 10 pts to go |
| P06T | 43858 | 86.4% | 86.4% | -13.6 | 100% | ❌ 14 pts to go |
| P06 | 256 | 99.2% | 99.2% | -0.8 | 100% | 🟡 1 pts to go |
| P07 | 677 | 99.7% | 99.7% | -0.3 | 100% | 🟡 0 pts to go |
| P08 | 21636 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P09 | 314 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2160 | 98.9% | 98.9% | -1.1 | 100% | 🟡 1 pts to go |
| P11 | 1640 | 93.1% | 93.1% | -6.9 | 100% | 🟡 7 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 163822 | 86.3% | 86.3% | -13.7 | 100% | ❌ 14 pts to go |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 84.1% | 84.1% | -15.9 | 100% | ❌ 16 pts to go |
| P01T | 199 | 94.5% | 94.5% | -5.5 | 100% | 🟡 6 pts to go |
| P01_GOLD | 644 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P02 | 472 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P03 | 271 | 99.6% | 99.6% | -0.4 | 100% | 🟡 0 pts to go |
| P04 | 3641 | 99.5% | 99.5% | -0.5 | 100% | 🟡 0 pts to go |
| P05 | 426 | 99.5% | 99.5% | -0.5 | 100% | 🟡 0 pts to go |
| P06M | 18370 | 89.9% | 89.9% | -10.1 | 100% | ❌ 10 pts to go |
| P06T | 43858 | 86.4% | 86.4% | -13.6 | 100% | ❌ 14 pts to go |
| P06 | 256 | 99.2% | 99.2% | -0.8 | 100% | 🟡 1 pts to go |
| P07 | 677 | 99.7% | 99.7% | -0.3 | 100% | 🟡 0 pts to go |
| P08 | 21636 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P09 | 314 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2160 | 98.9% | 98.9% | -1.1 | 100% | 🟡 1 pts to go |
| P11 | 1640 | 93.1% | 93.1% | -6.9 | 100% | 🟡 7 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 163822 | 86.3% | 86.3% | -13.7 | 100% | ❌ 14 pts to go |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 195 | 84.1% | 84.1% | -15.9 | 100% | ❌ 16 pts to go |
| P01T | 199 | 94.5% | 94.5% | -5.5 | 100% | 🟡 6 pts to go |
| P01_GOLD | 644 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P02 | 472 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P03 | 271 | 99.6% | 99.6% | -0.4 | 100% | 🟡 0 pts to go |
| P04 | 3641 | 99.5% | 99.5% | -0.5 | 100% | 🟡 0 pts to go |
| P05 | 426 | 99.5% | 99.5% | -0.5 | 100% | 🟡 0 pts to go |
| P06M | 18370 | 89.9% | 89.9% | -10.1 | 100% | ❌ 10 pts to go |
| P06T | 43858 | 86.4% | 86.4% | -13.6 | 100% | ❌ 14 pts to go |
| P06 | 256 | 99.2% | 99.2% | -0.8 | 100% | 🟡 1 pts to go |
| P07 | 677 | 99.7% | 99.7% | -0.3 | 100% | 🟡 0 pts to go |
| P08 | 21636 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P09 | 314 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2160 | 98.9% | 98.9% | -1.1 | 100% | 🟡 1 pts to go |
| P11 | 1640 | 93.1% | 93.1% | -6.9 | 100% | 🟡 7 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 163822 | 86.3% | 86.3% | -13.7 | 100% | ❌ 14 pts to go |

