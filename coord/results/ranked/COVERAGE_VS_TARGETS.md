# Coverage vs the downstream team's targets — 2026-11-10

Benchmarks (field × package with a numeric target): **52 of 446 met** (11.7%); 85 within 10 points; 309 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 60, P01T 272, P01_GOLD 625, P02 460, P03 255, P04 3199, P05 413, P06M 5018, P06T 40549, P06 276, P07 653, P08 19414, P09 303, P10R 75079, P10 2588, P11 4832, P12 8, P13 14182

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 60 | 0.0% | 25.0% | 8 | PO rule (48 rows) |
| P01T | 272 | 0.7% | 18.4% | 7 | payment terms (198 rows) |
| P01_GOLD | 625 | 24.3% | 68.0% | 9 | payment terms (214 rows) |
| P02 | 460 | 7.6% | 52.4% | 9 | PO rule (349 rows) |
| P03 | 255 | 13.7% | 57.3% | 9 | PO rule (121 rows) |
| P04 | 3199 | 1.4% | 18.2% | 6 | PO rule (3000 rows) |
| P05 | 413 | 1.0% | 17.2% | 7 | payment terms (337 rows) |
| P06M | 5018 | 0.0% | 1.9% | 8 | PO rule (4988 rows) |
| P06T | 40549 | 0.0% | 0.5% | 5 | PO rule (40230 rows) |
| P06 | 276 | 0.0% | 5.4% | 5 | reference to quote (PO / contract / vendor id) (276 rows) |
| P07 | 653 | 0.0% | 1.5% | 5 | reference to quote (PO / contract / vendor id) (653 rows) |
| P08 | 19414 | 0.0% | 0.2% | 4 | reference to quote (PO / contract / vendor id) (19414 rows) |
| P09 | 303 | 1.0% | 43.6% | 8 | payment terms (283 rows) |
| P10R | 75079 | 0.0% | 9.5% | 7 | PO rule (75046 rows) |
| P10 | 2588 | 0.0% | 0.6% | 4 | reference to quote (PO / contract / vendor id) (2588 rows) |
| P11 | 4832 | 0.1% | 1.5% | 6 | PO rule (4715 rows) |
| P12 | 8 | 0.0% | 50.0% | 9 | PO rule (8 rows) |
| P13 | 14182 | 0.0% | 0.0% | 6 | reference to quote (PO / contract / vendor id) (14182 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 60 | 6 | 6 | 48 | 0 | 0 | 71 |
| P01T | 272 | 31 | 49 | 192 | 0 | 0 | 71 |
| P01_GOLD | 625 | 229 | 185 | 211 | 0 | 0 | 81 |
| P02 | 460 | 0 | 186 | 274 | 0 | 0 | 66 |
| P03 | 255 | 0 | 0 | 241 | 14 | 0 | 57 |
| P04 | 3199 | 0 | 0 | 2544 | 655 | 0 | 45 |
| P05 | 413 | 15 | 29 | 345 | 24 | 0 | 51 |
| P06M | 5018 | 0 | 3 | 4934 | 81 | 0 | 51 |
| P06T | 40549 | 0 | 31 | 32230 | 8288 | 0 | 38 |
| P06 | 276 | 19 | 28 | 229 | 0 | 0 | 67 |
| P07 | 653 | 0 | 16 | 603 | 34 | 0 | 48 |
| P08 | 19414 | 0 | 0 | 15185 | 4229 | 0 | 38 |
| P09 | 303 | 3 | 12 | 285 | 3 | 0 | 53 |
| P10R | 75079 | 1 | 8 | 46373 | 28697 | 0 | 38 |
| P10 | 2588 | 2 | 9 | 1761 | 816 | 0 | 38 |
| P11 | 4832 | 6 | 8 | 43 | 0 | 4775 | 23 |
| P12 | 8 | 0 | 1 | 7 | 0 | 0 | 54 |
| P13 | 14182 | 2 | 12 | 11489 | 2679 | 0 | 43 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 60 | 46 | 76.7% | the buyer's PO / reference rule (7) |
| P01T | 272 | 115 | 42.3% | bill-to legal name and address (120) |
| P01_GOLD | 625 | 461 | 73.8% | bill-to legal name and address (111) |
| P02 | 460 | 306 | 66.5% | bill-to legal name and address (85) |
| P03 | 255 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (255) |
| P04 | 3199 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (3199) |
| P05 | 413 | 47 | 11.4% | a confirmed invoicing / AP or finance channel (326) |
| P06M | 5018 | 34 | 0.7% | a confirmed invoicing / AP or finance channel (4955) |
| P06T | 40549 | 167 | 0.4% | a confirmed invoicing / AP or finance channel (39882) |
| P06 | 276 | 30 | 10.9% | bill-to legal name and address (172) |
| P07 | 653 | 9 | 1.4% | bill-to legal name and address (385) |
| P08 | 19414 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (19414) |
| P09 | 303 | 40 | 13.2% | a confirmed invoicing / AP or finance channel (253) |
| P10R | 75079 | 268 | 0.4% | a confirmed invoicing / AP or finance channel (74038) |
| P10 | 2588 | 3 | 0.1% | a confirmed invoicing / AP or finance channel (2491) |
| P11 | 4832 | 9 | 0.2% | a confirmed invoicing / AP or finance channel (4775) |
| P12 | 8 | 3 | 37.5% | a confirmed invoicing / AP or finance channel (5) |
| P13 | 14182 | 6 | 0.0% | a confirmed invoicing / AP or finance channel (13854) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 60 | 6 | 10.0% | 6 | 0 | the vendor's GST/HST number (BN9) (46) |
| P01T | 272 | 45 | 16.5% | 18 | 0 | the vendor's GST/HST number (BN9) (147) |
| P01_GOLD | 625 | 395 | 63.2% | 13 | 0 | the vendor's GST/HST number (BN9) (150) |
| P02 | 460 | 211 | 45.9% | 20 | 0 | the vendor's GST/HST number (BN9) (188) |
| P03 | 255 | 18 | 7.1% | 0 | 129 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (89) |
| P04 | 3199 | 42 | 1.3% | 7 | 710 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2380) |
| P05 | 413 | 22 | 5.3% | 8 | 98 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (221) |
| P06M | 5018 | 1 | 0.0% | 10 | 77 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (4863) |
| P06T | 40549 | 19 | 0.0% | 80 | 3454 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (36298) |
| P06 | 276 | 13 | 4.7% | 16 | 0 | the vendor's GST/HST number (BN9) (164) |
| P07 | 653 | 6 | 0.9% | 30 | 14 | the vendor's GST/HST number (BN9) (353) |
| P08 | 19414 | 2 | 0.0% | 3 | 932 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (18419) |
| P09 | 303 | 39 | 12.9% | 1 | 121 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (123) |
| P10R | 75079 | 744 | 1.0% | 0 | 38954 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (35032) |
| P10 | 2588 | 4 | 0.2% | 17 | 318 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2143) |
| P11 | 4832 | 9 | 0.2% | 22 | 0 | a confirmed invoicing / AP or finance channel (4734) |
| P12 | 8 | 2 | 25.0% | 0 | 3 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2) |
| P13 | 14182 | 9 | 0.1% | 239 | 8650 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (5167) |
| **all** | 168186 | 1587 | 0.9% | 490 | 53460 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 54 | 0 | 0 | 0 | 11 | 6 | 0 | 48 | 51 | 0 |
| P01T | 241 | 0 | 0 | 0 | 72 | 116 | 18 | 188 | 200 | 30 |
| P01_GOLD | 396 | 0 | 0 | 0 | 11 | 96 | 34 | 193 | 228 | 59 |
| P02 | 460 | 0 | 460 | 0 | 36 | 79 | 20 | 349 | 279 | 21 |
| P03 | 255 | 0 | 255 | 0 | 12 | 54 | 23 | 121 | 127 | 27 |
| P04 | 3199 | 0 | 3199 | 0 | 1193 | 1674 | 756 | 3000 | 2745 | 135 |
| P05 | 398 | 0 | 345 | 0 | 64 | 138 | 49 | 329 | 339 | 52 |
| P06M | 5018 | 0 | 5018 | 0 | 1087 | 638 | 111 | 4988 | 4957 | 3 |
| P06T | 40549 | 0 | 40549 | 0 | 26730 | 33173 | 8874 | 40230 | 39420 | 208 |
| P06 | 257 | 0 | 0 | 0 | 90 | 166 | 55 | 180 | 219 | 5 |
| P07 | 653 | 0 | 653 | 0 | 341 | 470 | 125 | 599 | 603 | 15 |
| P08 | 19414 | 0 | 19414 | 0 | 13426 | 16196 | 4520 | 19148 | 18769 | 189 |
| P09 | 300 | 0 | 279 | 0 | 9 | 70 | 3 | 273 | 285 | 44 |
| P10R | 75078 | 0 | 74919 | 0 | 50924 | 65313 | 30229 | 75046 | 74934 | 22 |
| P10 | 2586 | 0 | 2550 | 0 | 1149 | 1997 | 957 | 2518 | 2467 | 112 |
| P11 | 4826 | 4775 | 4720 | 0 | 3389 | 4629 | 892 | 4715 | 4318 | 35 |
| P12 | 8 | 0 | 7 | 0 | 0 | 2 | 0 | 8 | 7 | 0 |
| P13 | 14180 | 0 | 14079 | 0 | 4349 | 7207 | 3125 | 14146 | 14150 | 22 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| mta_sts | P10R | 75.5% | 100% | 18416 |
| tls_rpt | P10R | 75.5% | 100% | 18416 |
| bimi | P10R | 75.5% | 100% | 18416 |
| buyer_ap_cycle_published | P10R | 0.0% | 20% | 15012 |
| ap_system_hint | P10R | 0.2% | 20% | 14879 |
| buyer_logo_url | P08 | 31.0% | 100% | 13401 |
| buyer_phone | P08 | 26.7% | 95% | 13251 |
| vendor_registered_address | P08 | 9.1% | 70% | 11817 |
| buyer_legal_name_as_published | P08 | 16.6% | 75% | 11343 |
| buyer_esignature_preference | P10R | 0.0% | 15% | 11246 |
| buyer_tax_exempt_status | P10R | 0.0% | 15% | 11245 |
| buyer_payment_method_preference | P10R | 0.2% | 15% | 11117 |
| vendor_logo_url | P08 | 45.5% | 100% | 10583 |
| vendor_phone | P08 | 33.5% | 85% | 9989 |
| vendor_bn9 | P08 | 8.0% | 50% | 8158 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 8097 |
| vendor_emails | P08 | 34.7% | 75% | 7829 |
| ap_system_hint | P06T | 0.9% | 20% | 7726 |
| vendor_trading_name | P08 | 15.8% | 50% | 6639 |
| mta_sts | P06T | 84.7% | 100% | 6215 |
| tls_rpt | P06T | 84.7% | 100% | 6215 |
| bimi | P06T | 84.7% | 100% | 6215 |
| buyer_esignature_preference | P06T | 0.3% | 15% | 5959 |
| buyer_payment_method_preference | P06T | 0.3% | 15% | 5951 |
| buyer_tax_exempt_status | P06T | 0.4% | 15% | 5929 |
| buyer_phone | P13 | 53.3% | 95% | 5914 |
| buyer_logo_url | P13 | 53.5% | 95% | 5879 |
| buyer_bn_as_published | P08 | 7.3% | 35% | 5376 |
| invoice_reference_hint | P08 | 1.4% | 25% | 4588 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 3878 |
| ap_system_hint | P08 | 0.9% | 20% | 3699 |
| buyer_address | P08 | 76.7% | 95% | 3556 |
| buyer_logo_url | P11 | 9.7% | 80% | 3399 |
| buyer_phone | P11 | 7.2% | 75% | 3278 |
| vendor_phone | P11 | 8.5% | 75% | 3213 |
| vendor_emails | P11 | 7.5% | 70% | 3020 |
| buyer_legal_name_as_published | P11 | 4.2% | 65% | 2938 |
| buyer_payment_method_preference | P08 | 0.2% | 15% | 2871 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 2836 |
| buyer_esignature_preference | P08 | 0.5% | 15% | 2825 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 85.0% | 85.0% | +40.6 | 50% | ✅ met |
| P01T | 272 | 88.2% | 88.2% | +16.5 | 50% | ✅ met |
| P01_GOLD | 625 | 92.2% | 94.4% | -0.3 | 95% | 🟡 3 pts to go |
| P02 | 460 | 74.6% | 76.1% | -9.3 | 95% | ❌ 20 pts to go |
| P03 | 255 | 82.4% | 85.5% | -10.4 | 95% | ❌ 13 pts to go |
| P04 | 3199 | 35.0% | 36.5% | -33.6 | 90% | ❌ 55 pts to go |
| P05 | 413 | 39.5% | 42.4% | -1.6 | 70% | ❌ 30 pts to go |
| P06M | 5018 | 91.6% | 91.6% | +84.5 | n/a | no target |
| P06T | 40549 | 78.4% | 78.4% | +74.0 | n/a | no target |
| P06 | 276 | 34.8% | 34.8% | -13.4 | 30% | ✅ met |
| P07 | 653 | 8.3% | 8.3% | -15.5 | 30% | ❌ 22 pts to go |
| P08 | 19414 | 1.4% | 1.4% | -1.0 | 25% | ❌ 24 pts to go |
| P09 | 303 | 99.0% | 99.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10R | 75079 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2588 | 2.7% | 2.7% | +0.5 | 25% | ❌ 22 pts to go |
| P11 | 4832 | 23.2% | 23.5% | -0.9 | 60% | ❌ 37 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 14182 | 0.3% | 0.3% | +0.1 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 272 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 625 | 6.1% | 6.1% | -0.1 | 50% | ❌ 44 pts to go |
| P02 | 460 | 6.3% | 6.3% | -0.9 | 50% | ❌ 44 pts to go |
| P03 | 255 | 1.6% | 1.6% | -0.3 | 40% | ❌ 38 pts to go |
| P04 | 3199 | 0.6% | 0.6% | -0.5 | 30% | ❌ 29 pts to go |
| P05 | 413 | 0.2% | 0.2% | -0.1 | 20% | ❌ 20 pts to go |
| P06M | 5018 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 40549 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 653 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 19414 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 0.7% | 0.7% | +0.2 | 50% | ❌ 49 pts to go |
| P10R | 75079 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2588 | 0.0% | 0.0% | -0.1 | n/a | no target |
| P11 | 4832 | 0.1% | 0.1% | -0.7 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 14182 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 73.3% | 73.3% | +73.3 | n/a | no target |
| P01T | 272 | 65.1% | 65.1% | +59.7 | 50% | ✅ met |
| P01_GOLD | 625 | 66.9% | 66.9% | -0.7 | 85% | ❌ 18 pts to go |
| P02 | 460 | 65.7% | 65.7% | -9.8 | 90% | ❌ 24 pts to go |
| P03 | 255 | 61.6% | 61.6% | -13.9 | 85% | ❌ 23 pts to go |
| P04 | 3199 | 32.0% | 32.0% | -33.5 | 85% | ❌ 53 pts to go |
| P05 | 413 | 29.5% | 29.5% | -1.5 | 60% | ❌ 30 pts to go |
| P06M | 5018 | 91.3% | 91.3% | +91.3 | n/a | no target |
| P06T | 40549 | 78.0% | 78.0% | +77.8 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 653 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 19414 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 96.0% | 96.0% | -0.6 | 100% | 🟡 4 pts to go |
| P10R | 75079 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2588 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 4832 | 21.1% | 21.1% | +1.1 | 60% | ❌ 39 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 14182 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 272 | 0.0% | 0.0% | -2.2 | 30% | ❌ 30 pts to go |
| P01_GOLD | 625 | 50.6% | 50.6% | -0.7 | 80% | ❌ 29 pts to go |
| P02 | 460 | 57.6% | 57.6% | -9.2 | 60% | 🟡 2 pts to go |
| P03 | 255 | 51.8% | 51.8% | -12.1 | 80% | ❌ 28 pts to go |
| P04 | 3199 | 26.6% | 26.6% | -27.9 | 50% | ❌ 23 pts to go |
| P05 | 413 | 12.3% | 12.3% | -1.0 | 40% | ❌ 28 pts to go |
| P06M | 5018 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 40549 | 0.0% | 0.0% | -0.2 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 653 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 19414 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 83.5% | 83.5% | -2.6 | 50% | ✅ met |
| P10R | 75079 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2588 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 4832 | 1.7% | 1.7% | -15.8 | 40% | ❌ 38 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 14182 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 272 | 0.4% | 0.4% | -2.9 | n/a | no target |
| P01_GOLD | 625 | 60.3% | 60.3% | -0.8 | 85% | ❌ 25 pts to go |
| P02 | 460 | 57.0% | 57.0% | -8.8 | 90% | ❌ 33 pts to go |
| P03 | 255 | 60.4% | 60.4% | -14.1 | 85% | ❌ 25 pts to go |
| P04 | 3199 | 27.4% | 27.4% | -28.9 | 85% | ❌ 58 pts to go |
| P05 | 413 | 20.3% | 20.3% | -0.8 | 50% | ❌ 30 pts to go |
| P06M | 5018 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 40549 | 0.0% | 0.0% | -0.2 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 653 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 19414 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 97.0% | 97.0% | -0.1 | 100% | 🟡 3 pts to go |
| P10R | 75079 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2588 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 4832 | 1.8% | 1.8% | -17.2 | 60% | ❌ 58 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 14182 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 272 | 0.0% | 0.0% | -2.2 | n/a | no target |
| P01_GOLD | 625 | 13.0% | 13.0% | +0.0 | 60% | ❌ 47 pts to go |
| P02 | 460 | 6.1% | 6.1% | -1.1 | 50% | ❌ 44 pts to go |
| P03 | 255 | 8.6% | 8.6% | -2.0 | 50% | ❌ 41 pts to go |
| P04 | 3199 | 2.1% | 2.1% | -2.2 | 40% | ❌ 38 pts to go |
| P05 | 413 | 1.0% | 1.0% | -0.3 | 20% | ❌ 19 pts to go |
| P06M | 5018 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 40549 | 0.0% | 0.0% | -0.1 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 653 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 19414 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 2.3% | 2.3% | -0.3 | 50% | ❌ 48 pts to go |
| P10R | 75079 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2588 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 4832 | 0.3% | 0.3% | -2.7 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 14182 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 34.9% | 34.9% | -0.2 | 80% | ❌ 45 pts to go |
| P02 | 460 | 52.6% | 52.6% | -8.0 | 90% | ❌ 37 pts to go |
| P03 | 255 | 33.7% | 33.7% | -7.6 | 80% | ❌ 46 pts to go |
| P04 | 3199 | 25.1% | 25.1% | -26.2 | 85% | ❌ 60 pts to go |
| P05 | 413 | 5.6% | 5.6% | -0.4 | 50% | ❌ 44 pts to go |
| P06M | 5018 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 40549 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 653 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 19414 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 75.9% | 75.9% | +0.0 | 95% | ❌ 19 pts to go |
| P10R | 75079 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2588 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 4832 | 1.3% | 1.3% | -11.8 | 50% | ❌ 49 pts to go |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 14182 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 272 | 0.0% | 0.0% | -1.1 | n/a | no target |
| P01_GOLD | 625 | 8.5% | 8.5% | +0.0 | 50% | ❌ 42 pts to go |
| P02 | 460 | 6.3% | 6.3% | -0.9 | 50% | ❌ 44 pts to go |
| P03 | 255 | 2.0% | 2.0% | -0.4 | 30% | ❌ 28 pts to go |
| P04 | 3199 | 0.5% | 0.5% | -0.6 | 30% | ❌ 30 pts to go |
| P05 | 413 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 5018 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 40549 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 653 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 19414 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P10R | 75079 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2588 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 4832 | 0.1% | 0.1% | -0.7 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 14182 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 272 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 460 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 255 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3199 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 413 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 5018 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 40549 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 276 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 653 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 19414 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 303 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 75079 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2588 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 4832 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 14182 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 23.3% | 23.3% | -76.7 | 70% | ❌ 47 pts to go |
| P01T | 272 | 30.1% | 30.1% | -50.3 | 60% | ❌ 30 pts to go |
| P01_GOLD | 625 | 73.1% | 73.1% | -4.8 | 90% | ❌ 17 pts to go |
| P02 | 460 | 54.8% | 54.8% | -12.5 | 85% | ❌ 30 pts to go |
| P03 | 255 | 68.6% | 68.6% | -13.6 | 90% | ❌ 21 pts to go |
| P04 | 3199 | 31.0% | 31.0% | -24.4 | 75% | ❌ 44 pts to go |
| P05 | 413 | 50.1% | 50.1% | -2.5 | 50% | ✅ met |
| P06M | 5018 | 2.3% | 2.3% | -72.1 | n/a | no target |
| P06T | 40549 | 9.9% | 9.9% | -50.8 | n/a | no target |
| P06 | 276 | 19.6% | 19.6% | -24.4 | 40% | ❌ 20 pts to go |
| P07 | 653 | 13.3% | 13.3% | -24.8 | 50% | ❌ 37 pts to go |
| P08 | 19414 | 8.0% | 8.0% | -32.2 | 50% | ❌ 42 pts to go |
| P09 | 303 | 57.8% | 57.8% | +3.5 | 80% | ❌ 22 pts to go |
| P10R | 75079 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2588 | 28.1% | 28.1% | -8.5 | 40% | ❌ 12 pts to go |
| P11 | 4832 | 79.0% | 79.0% | +34.3 | 60% | ✅ met |
| P12 | 8 | 62.5% | 62.5% | +9.9 | 85% | ❌ 22 pts to go |
| P13 | 14182 | 90.4% | 90.4% | -1.3 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 71.7% | 71.7% | +10.6 | n/a | no target |
| P01T | 272 | 29.8% | 29.8% | -33.2 | n/a | no target |
| P01_GOLD | 625 | 70.6% | 70.6% | -4.2 | 95% | ❌ 24 pts to go |
| P02 | 460 | 72.4% | 72.4% | -12.5 | 95% | ❌ 23 pts to go |
| P03 | 255 | 70.2% | 70.2% | -7.7 | 95% | ❌ 25 pts to go |
| P04 | 3199 | 44.4% | 44.4% | -36.3 | 95% | ❌ 51 pts to go |
| P05 | 413 | 53.0% | 53.0% | -3.2 | 70% | ❌ 17 pts to go |
| P06M | 5018 | 57.0% | 57.0% | +36.2 | n/a | no target |
| P06T | 40549 | 21.6% | 21.6% | -56.6 | n/a | no target |
| P06 | 276 | 21.0% | 21.0% | -34.4 | 80% | ❌ 59 pts to go |
| P07 | 653 | 14.4% | 14.4% | -37.6 | 70% | ❌ 56 pts to go |
| P08 | 19414 | 9.1% | 9.1% | -43.3 | 70% | ❌ 61 pts to go |
| P09 | 303 | 87.5% | 87.5% | -1.0 | 100% | ❌ 12 pts to go |
| P10R | 75079 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2588 | 30.7% | 30.7% | -11.7 | 70% | ❌ 39 pts to go |
| P11 | 4832 | 83.2% | 83.2% | +27.9 | 75% | ✅ met |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 14182 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 16.7% | 16.7% | -33.3 | n/a | no target |
| P01T | 272 | 18.8% | 18.8% | -0.8 | n/a | no target |
| P01_GOLD | 625 | 48.2% | 48.2% | -4.2 | 60% | ❌ 12 pts to go |
| P02 | 460 | 55.2% | 55.2% | -12.1 | 60% | 🟡 5 pts to go |
| P03 | 255 | 54.5% | 54.5% | -10.4 | 60% | 🟡 6 pts to go |
| P04 | 3199 | 33.5% | 33.5% | -22.0 | 55% | ❌ 22 pts to go |
| P05 | 413 | 23.0% | 23.0% | -2.3 | 50% | ❌ 27 pts to go |
| P06M | 5018 | 1.7% | 1.7% | -15.6 | n/a | no target |
| P06T | 40549 | 14.1% | 14.1% | -39.5 | n/a | no target |
| P06 | 276 | 26.8% | 26.8% | -26.2 | n/a | no target |
| P07 | 653 | 23.7% | 23.7% | -22.3 | 55% | ❌ 31 pts to go |
| P08 | 19414 | 15.8% | 15.8% | -31.7 | 50% | ❌ 34 pts to go |
| P09 | 303 | 71.0% | 71.0% | -0.4 | 70% | ✅ met |
| P10R | 75079 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2588 | 37.2% | 37.2% | -14.7 | 55% | ❌ 18 pts to go |
| P11 | 4832 | 80.0% | 80.0% | +37.0 | 50% | ✅ met |
| P12 | 8 | 87.5% | 87.5% | +3.3 | n/a | no target |
| P13 | 14182 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 20.0% | 20.0% | -41.1 | n/a | no target |
| P01T | 272 | 30.1% | 30.1% | -0.3 | n/a | no target |
| P01_GOLD | 625 | 49.6% | 49.6% | -2.2 | 70% | ❌ 20 pts to go |
| P02 | 460 | 52.2% | 52.2% | -5.0 | 70% | ❌ 18 pts to go |
| P03 | 255 | 49.4% | 49.4% | -7.8 | 70% | ❌ 21 pts to go |
| P04 | 3199 | 35.0% | 35.0% | -17.0 | 65% | ❌ 30 pts to go |
| P05 | 413 | 31.2% | 31.2% | -3.4 | 60% | ❌ 29 pts to go |
| P06M | 5018 | 3.1% | 3.1% | -27.3 | n/a | no target |
| P06T | 40549 | 21.1% | 21.1% | +17.6 | n/a | no target |
| P06 | 276 | 45.7% | 45.7% | -13.9 | 40% | ✅ met |
| P07 | 653 | 41.8% | 41.8% | -26.1 | 85% | ❌ 43 pts to go |
| P08 | 19414 | 33.5% | 33.5% | -34.6 | 85% | ❌ 52 pts to go |
| P09 | 303 | 53.1% | 53.1% | -2.3 | 85% | ❌ 32 pts to go |
| P10R | 75079 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2588 | 51.5% | 51.5% | -14.8 | 85% | ❌ 34 pts to go |
| P11 | 4832 | 8.5% | 8.5% | -46.4 | 75% | ❌ 66 pts to go |
| P12 | 8 | 25.0% | 25.0% | +9.2 | n/a | no target |
| P13 | 14182 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 25.0% | 25.0% | -69.4 | n/a | no target |
| P01T | 272 | 96.0% | 96.0% | +5.8 | n/a | no target |
| P01_GOLD | 625 | 89.4% | 89.4% | +0.0 | 90% | 🟡 1 pts to go |
| P02 | 460 | 89.1% | 89.1% | +1.5 | 90% | 🟡 1 pts to go |
| P03 | 255 | 91.0% | 91.0% | +1.1 | 90% | ✅ met |
| P04 | 3199 | 89.7% | 89.7% | +8.4 | 85% | ✅ met |
| P05 | 413 | 51.3% | 51.3% | +0.3 | 70% | ❌ 19 pts to go |
| P06M | 5018 | 7.5% | 7.5% | -60.4 | n/a | no target |
| P06T | 40549 | 88.6% | 88.6% | +10.7 | n/a | no target |
| P06 | 276 | 98.2% | 98.2% | +1.2 | 50% | ✅ met |
| P07 | 653 | 98.8% | 98.8% | +2.0 | 100% | 🟡 1 pts to go |
| P08 | 19414 | 99.4% | 99.4% | +3.3 | 100% | 🟡 1 pts to go |
| P09 | 303 | 80.2% | 80.2% | +0.4 | 100% | ❌ 20 pts to go |
| P10R | 75079 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2588 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 4832 | 96.4% | 96.4% | +3.4 | 100% | 🟡 4 pts to go |
| P12 | 8 | 37.5% | 37.5% | -4.6 | n/a | no target |
| P13 | 14182 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 16.7% | 16.7% | -33.3 | n/a | no target |
| P01T | 272 | 38.2% | 38.2% | -7.5 | n/a | no target |
| P01_GOLD | 625 | 46.2% | 46.2% | +0.5 | 70% | ❌ 24 pts to go |
| P02 | 460 | 48.5% | 48.5% | -3.0 | 75% | ❌ 26 pts to go |
| P03 | 255 | 43.9% | 43.9% | -7.5 | 75% | ❌ 31 pts to go |
| P04 | 3199 | 30.8% | 30.8% | -12.1 | 70% | ❌ 39 pts to go |
| P05 | 413 | 25.4% | 25.4% | +0.9 | 55% | ❌ 30 pts to go |
| P06M | 5018 | 2.0% | 2.0% | -14.1 | n/a | no target |
| P06T | 40549 | 17.4% | 17.4% | +14.5 | n/a | no target |
| P06 | 276 | 37.0% | 37.0% | -4.0 | n/a | no target |
| P07 | 653 | 36.9% | 36.9% | +0.0 | 70% | ❌ 33 pts to go |
| P08 | 19414 | 34.7% | 34.7% | -14.0 | 75% | ❌ 40 pts to go |
| P09 | 303 | 49.8% | 49.8% | -2.2 | 85% | ❌ 35 pts to go |
| P10R | 75079 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2588 | 38.9% | 38.9% | -12.4 | 80% | ❌ 41 pts to go |
| P11 | 4832 | 7.5% | 7.5% | -33.0 | 70% | ❌ 62 pts to go |
| P12 | 8 | 25.0% | 25.0% | -6.6 | n/a | no target |
| P13 | 14182 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 23.3% | 23.3% | -71.1 | n/a | no target |
| P01T | 272 | 64.3% | 64.3% | -24.8 | n/a | no target |
| P01_GOLD | 625 | 79.8% | 79.8% | +0.0 | 90% | ❌ 10 pts to go |
| P02 | 460 | 75.7% | 75.7% | -1.5 | 90% | ❌ 14 pts to go |
| P03 | 255 | 82.7% | 82.7% | +1.0 | 90% | 🟡 7 pts to go |
| P04 | 3199 | 60.1% | 60.1% | -10.8 | 85% | ❌ 25 pts to go |
| P05 | 413 | 48.4% | 48.4% | +0.0 | 75% | ❌ 27 pts to go |
| P06M | 5018 | 4.7% | 4.7% | -63.2 | n/a | no target |
| P06T | 40549 | 36.5% | 36.5% | -40.6 | n/a | no target |
| P06 | 276 | 60.5% | 60.5% | -28.1 | n/a | no target |
| P07 | 653 | 55.4% | 55.4% | -35.1 | 100% | ❌ 45 pts to go |
| P08 | 19414 | 45.5% | 45.5% | -43.5 | 100% | ❌ 54 pts to go |
| P09 | 303 | 61.4% | 61.4% | -1.1 | n/a | no target |
| P10R | 75079 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2588 | 70.6% | 70.6% | -18.4 | 100% | ❌ 29 pts to go |
| P11 | 4832 | 73.8% | 73.8% | -0.7 | n/a | no target |
| P12 | 8 | 37.5% | 37.5% | +0.7 | n/a | no target |
| P13 | 14182 | 80.5% | 80.5% | -2.2 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 50.0% | 50.0% | +50.0 | n/a | no target · QC vendors: 30 rows, 100.0% filled |
| P01T | 272 | 14.7% | 14.7% | -7.0 | n/a | no target · QC vendors: 5 rows, 100.0% filled |
| P01_GOLD | 625 | 43.8% | 43.8% | -4.1 | 95% | ❌ 51 pts to go · QC vendors: 53 rows, 98.1% filled |
| P02 | 460 | 54.8% | 54.8% | -13.8 | 95% | ❌ 40 pts to go · QC vendors: 106 rows, 100.0% filled |
| P03 | 255 | 46.3% | 46.3% | -9.5 | 95% | ❌ 49 pts to go · QC vendors: 17 rows, 100.0% filled |
| P04 | 3199 | 32.4% | 32.4% | -27.8 | 95% | ❌ 63 pts to go · QC vendors: 460 rows, 98.7% filled |
| P05 | 413 | 14.5% | 14.5% | -0.3 | n/a | no target · QC vendors: 34 rows, 94.1% filled |
| P06M | 5018 | 55.6% | 55.6% | +55.6 | n/a | no target · QC vendors: 2787 rows, 100.0% filled |
| P06T | 40549 | 11.6% | 11.6% | -44.3 | n/a | no target · QC vendors: 583 rows, 100.0% filled |
| P06 | 276 | 8.7% | 8.7% | -17.8 | n/a | no target · QC vendors: 13 rows, 100.0% filled |
| P07 | 653 | 6.0% | 6.0% | -15.4 | n/a | no target · QC vendors: 24 rows, 95.8% filled |
| P08 | 19414 | 4.8% | 4.8% | -24.1 | n/a | no target · QC vendors: 620 rows, 99.4% filled |
| P09 | 303 | 78.2% | 78.2% | -1.9 | 95% | ❌ 17 pts to go · QC vendors: 111 rows, 100.0% filled |
| P10R | 75079 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2588 | 16.8% | 16.8% | -6.6 | n/a | no target · QC vendors: 259 rows, 95.4% filled |
| P11 | 4832 | 64.3% | 64.3% | +35.0 | n/a | no target · QC vendors: 75 rows, 98.7% filled |
| P12 | 8 | 62.5% | 62.5% | -11.2 | n/a | no target · QC vendors: 1 rows, 100.0% filled |
| P13 | 14182 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 68.3% | 68.3% | +7.2 | n/a | no target · vendors with a registry record: 41 rows, 100.0% filled |
| P01T | 272 | 29.8% | 29.8% | -33.2 | n/a | no target · vendors with a registry record: 81 rows, 100.0% filled |
| P01_GOLD | 625 | 79.4% | 79.4% | -4.1 | 100% | ❌ 21 pts to go · vendors with a registry record: 496 rows, 100.0% filled |
| P02 | 460 | 76.1% | 76.1% | -13.0 | 100% | ❌ 24 pts to go · vendors with a registry record: 350 rows, 100.0% filled |
| P03 | 255 | 79.6% | 79.6% | -9.3 | 100% | ❌ 20 pts to go · vendors with a registry record: 203 rows, 100.0% filled |
| P04 | 3199 | 44.8% | 44.8% | -36.6 | 100% | ❌ 55 pts to go · vendors with a registry record: 1433 rows, 100.0% filled |
| P05 | 413 | 57.9% | 57.9% | -3.8 | n/a | no target · vendors with a registry record: 239 rows, 100.0% filled |
| P06M | 5018 | 56.2% | 56.2% | +35.4 | n/a | no target · vendors with a registry record: 2822 rows, 100.0% filled |
| P06T | 40549 | 21.6% | 21.6% | -56.6 | n/a | no target · vendors with a registry record: 8745 rows, 100.0% filled |
| P06 | 276 | 21.7% | 21.7% | -36.1 | n/a | no target · vendors with a registry record: 60 rows, 100.0% filled |
| P07 | 653 | 14.7% | 14.7% | -39.7 | n/a | no target · vendors with a registry record: 96 rows, 100.0% filled |
| P08 | 19414 | 9.1% | 9.1% | -45.2 | n/a | no target · vendors with a registry record: 1776 rows, 100.0% filled |
| P09 | 303 | 91.1% | 91.1% | -0.5 | n/a | no target · vendors with a registry record: 276 rows, 100.0% filled |
| P10R | 75079 | 100.0% | 100.0% |  | n/a | no target · vendors with a registry record: 75079 rows, 100.0% filled |
| P10 | 2588 | 31.6% | 31.6% | -12.1 | n/a | no target · vendors with a registry record: 819 rows, 100.0% filled |
| P11 | 4832 | 83.4% | 83.4% | +25.2 | n/a | no target · vendors with a registry record: 4031 rows, 100.0% filled |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 8 rows, 100.0% filled |
| P13 | 14182 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 90.0% | 90.0% | -4.4 | 90% | ✅ met |
| P01T | 272 | 57.4% | 57.4% | -37.2 | 90% | ❌ 33 pts to go |
| P01_GOLD | 625 | 84.6% | 84.6% | +0.0 | 95% | ❌ 10 pts to go |
| P02 | 460 | 82.8% | 82.8% | -7.8 | 95% | ❌ 12 pts to go |
| P03 | 255 | 78.8% | 78.8% | -4.4 | 85% | 🟡 6 pts to go |
| P04 | 3199 | 47.7% | 47.7% | -31.1 | 90% | ❌ 42 pts to go |
| P05 | 413 | 66.6% | 66.6% | -9.2 | 75% | 🟡 8 pts to go |
| P06M | 5018 | 87.3% | 87.3% | -1.4 | n/a | no target |
| P06T | 40549 | 18.2% | 18.2% | -46.2 | n/a | no target |
| P06 | 276 | 39.9% | 39.9% | -16.7 | 80% | ❌ 40 pts to go |
| P07 | 653 | 28.0% | 28.0% | -25.6 | 80% | ❌ 52 pts to go |
| P08 | 19414 | 16.6% | 16.6% | -20.2 | 75% | ❌ 58 pts to go |
| P09 | 303 | 76.9% | 76.9% | -3.9 | 95% | ❌ 18 pts to go |
| P10R | 75079 | 13.0% | 13.0% |  | n/a | no target |
| P10 | 2588 | 22.8% | 22.8% | -9.2 | 70% | ❌ 47 pts to go |
| P11 | 4832 | 4.2% | 4.2% | -20.7 | 65% | ❌ 61 pts to go |
| P12 | 8 | 75.0% | 75.0% | +1.3 | 80% | 🟡 5 pts to go |
| P13 | 14182 | 49.2% | 49.2% | -3.3 | 60% | ❌ 11 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 20.0% | 20.0% | -18.9 | 50% | ❌ 30 pts to go |
| P01T | 272 | 15.1% | 15.1% | -5.6 | n/a | no target |
| P01_GOLD | 625 | 20.5% | 20.5% | +0.1 | 40% | ❌ 20 pts to go |
| P02 | 460 | 19.1% | 19.1% | -2.7 | 40% | ❌ 21 pts to go |
| P03 | 255 | 22.4% | 22.4% | -4.5 | 40% | ❌ 18 pts to go |
| P04 | 3199 | 15.2% | 15.2% | -12.4 | 40% | ❌ 25 pts to go |
| P05 | 413 | 19.4% | 19.4% | -3.5 | 25% | 🟡 6 pts to go |
| P06M | 5018 | 10.6% | 10.6% | -15.0 | n/a | no target |
| P06T | 40549 | 8.3% | 8.3% | -22.6 | n/a | no target |
| P06 | 276 | 12.7% | 12.7% | +1.9 | 35% | ❌ 22 pts to go |
| P07 | 653 | 9.0% | 9.0% | -1.3 | 35% | ❌ 26 pts to go |
| P08 | 19414 | 7.3% | 7.3% | -3.8 | 35% | ❌ 28 pts to go |
| P09 | 303 | 16.2% | 16.2% | -0.9 | n/a | no target |
| P10R | 75079 | 6.0% | 6.0% |  | n/a | no target |
| P10 | 2588 | 4.9% | 4.9% | -4.7 | 30% | ❌ 25 pts to go |
| P11 | 4832 | 1.3% | 1.3% | -7.1 | n/a | no target |
| P12 | 8 | 12.5% | 12.5% | +2.0 | n/a | no target |
| P13 | 14182 | 29.0% | 29.0% | +3.1 | 30% | 🟡 1 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 100.0% | 100.0% | +5.6 | 100% | ✅ met |
| P01T | 272 | 92.6% | 92.6% | -0.9 | 100% | 🟡 7 pts to go |
| P01_GOLD | 625 | 90.2% | 90.2% | +2.5 | 100% | 🟡 10 pts to go |
| P02 | 460 | 95.2% | 95.2% | -1.6 | 100% | 🟡 5 pts to go |
| P03 | 255 | 89.4% | 89.4% | -2.4 | 100% | ❌ 11 pts to go |
| P04 | 3199 | 75.8% | 75.8% | -15.2 | 100% | ❌ 24 pts to go |
| P05 | 413 | 87.2% | 87.2% | +2.3 | 100% | ❌ 13 pts to go |
| P06M | 5018 | 97.8% | 97.8% | +25.8 | n/a | no target |
| P06T | 40549 | 78.1% | 78.1% | -2.1 | n/a | no target |
| P06 | 276 | 78.3% | 78.3% | +9.6 | 95% | ❌ 17 pts to go |
| P07 | 653 | 80.6% | 80.6% | +10.0 | 95% | ❌ 14 pts to go |
| P08 | 19414 | 76.7% | 76.7% | +10.5 | 95% | ❌ 18 pts to go |
| P09 | 303 | 95.7% | 95.7% | +0.2 | 100% | 🟡 4 pts to go |
| P10R | 75079 | 59.7% | 59.7% |  | n/a | no target |
| P10 | 2588 | 62.9% | 62.9% | -2.3 | 95% | ❌ 32 pts to go |
| P11 | 4832 | 76.2% | 76.2% | +41.8 | 80% | 🟡 4 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 14182 | 77.9% | 77.9% | +1.8 | 95% | ❌ 17 pts to go |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 91.7% | 91.7% | +2.8 | n/a | no target |
| P01T | 272 | 59.2% | 59.2% | -21.2 | n/a | no target |
| P01_GOLD | 625 | 70.4% | 70.4% | +0.2 | 90% | ❌ 20 pts to go |
| P02 | 460 | 74.1% | 74.1% | -5.6 | 95% | ❌ 21 pts to go |
| P03 | 255 | 72.9% | 72.9% | -0.7 | 95% | ❌ 22 pts to go |
| P04 | 3199 | 55.0% | 55.0% | -29.9 | 95% | ❌ 40 pts to go |
| P05 | 413 | 69.7% | 69.7% | -5.3 | 90% | ❌ 20 pts to go |
| P06M | 5018 | 90.4% | 90.4% | +6.5 | n/a | no target |
| P06T | 40549 | 28.6% | 28.6% | -48.7 | n/a | no target |
| P06 | 276 | 43.1% | 43.1% | -21.4 | 95% | ❌ 52 pts to go |
| P07 | 653 | 34.5% | 34.5% | -31.8 | 90% | ❌ 56 pts to go |
| P08 | 19414 | 26.7% | 26.7% | -48.0 | 95% | ❌ 68 pts to go |
| P09 | 303 | 86.5% | 86.5% | -2.5 | 100% | ❌ 14 pts to go |
| P10R | 75079 | 25.0% | 25.0% |  | n/a | no target |
| P10 | 2588 | 43.9% | 43.9% | -27.6 | 95% | ❌ 51 pts to go |
| P11 | 4832 | 7.2% | 7.2% | -21.7 | 75% | ❌ 68 pts to go |
| P12 | 8 | 75.0% | 75.0% | -14.5 | n/a | no target |
| P13 | 14182 | 53.3% | 53.3% | -26.0 | 95% | ❌ 42 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 70.0% | 70.0% | -7.8 | n/a | no target |
| P01T | 272 | 68.4% | 68.4% | -22.9 | 95% | ❌ 27 pts to go |
| P01_GOLD | 625 | 82.2% | 82.2% | +0.0 | 90% | 🟡 8 pts to go |
| P02 | 460 | 83.3% | 83.3% | -5.1 | 95% | ❌ 12 pts to go |
| P03 | 255 | 83.5% | 83.5% | -1.1 | 95% | ❌ 12 pts to go |
| P04 | 3199 | 61.3% | 61.3% | -22.9 | 90% | ❌ 29 pts to go |
| P05 | 413 | 86.2% | 86.2% | -3.4 | 95% | 🟡 9 pts to go |
| P06M | 5018 | 58.3% | 58.3% | -26.8 | n/a | no target |
| P06T | 40549 | 32.0% | 32.0% | -62.1 | n/a | no target |
| P06 | 276 | 56.9% | 56.9% | -33.5 | 100% | ❌ 43 pts to go |
| P07 | 653 | 45.9% | 45.9% | -42.2 | 100% | ❌ 54 pts to go |
| P08 | 19414 | 31.0% | 31.0% | -59.7 | 100% | ❌ 69 pts to go |
| P09 | 303 | 69.3% | 69.3% | -4.7 | n/a | no target |
| P10R | 75079 | 27.7% | 27.7% |  | n/a | no target |
| P10 | 2588 | 63.1% | 63.1% | -27.0 | 100% | ❌ 37 pts to go |
| P11 | 4832 | 9.7% | 9.7% | -26.8 | 80% | ❌ 70 pts to go |
| P12 | 8 | 100.0% | 100.0% | +15.8 | n/a | no target |
| P13 | 14182 | 53.5% | 53.5% | -30.7 | 95% | ❌ 42 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 6.7% | 6.7% | -10.0 | n/a | no target |
| P01T | 272 | 10.3% | 10.3% | -13.6 | n/a | no target |
| P01_GOLD | 625 | 14.2% | 14.2% | -0.1 | 25% | ❌ 11 pts to go |
| P02 | 460 | 24.8% | 24.8% | -2.9 | 40% | ❌ 15 pts to go |
| P03 | 255 | 9.0% | 9.0% | -1.6 | 20% | ❌ 11 pts to go |
| P04 | 3199 | 3.8% | 3.8% | -3.6 | 20% | ❌ 16 pts to go |
| P05 | 413 | 3.4% | 3.4% | -0.5 | 15% | ❌ 12 pts to go |
| P06M | 5018 | 0.4% | 0.4% | -4.4 | n/a | no target |
| P06T | 40549 | 0.5% | 0.5% | -2.7 | n/a | no target |
| P06 | 276 | 5.4% | 5.4% | +0.0 | n/a | no target |
| P07 | 653 | 7.4% | 7.4% | +1.1 | n/a | no target |
| P08 | 19414 | 0.3% | 0.3% | -0.7 | n/a | no target |
| P09 | 303 | 7.6% | 7.6% | -0.3 | n/a | no target |
| P10R | 75079 | 0.2% | 0.2% |  | n/a | no target |
| P10 | 2588 | 1.0% | 1.0% | -0.3 | n/a | no target |
| P11 | 4832 | 0.3% | 0.3% | -2.2 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | -10.5 | n/a | no target |
| P13 | 14182 | 0.6% | 0.6% | +0.0 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 30.0% | 30.0% | -8.9 | n/a | no target |
| P01T | 272 | 30.1% | 30.1% | -4.7 | 70% | ❌ 40 pts to go |
| P01_GOLD | 625 | 43.2% | 43.2% | -0.1 | 80% | ❌ 37 pts to go |
| P02 | 460 | 57.4% | 57.4% | -6.7 | 90% | ❌ 33 pts to go |
| P03 | 255 | 19.2% | 19.2% | -3.9 | 60% | ❌ 41 pts to go |
| P04 | 3199 | 25.1% | 25.1% | -25.4 | 85% | ❌ 60 pts to go |
| P05 | 413 | 12.3% | 12.3% | -0.7 | 50% | ❌ 38 pts to go |
| P06M | 5018 | 0.7% | 0.7% | -5.8 | n/a | no target |
| P06T | 40549 | 0.9% | 0.9% | -1.8 | n/a | no target |
| P06 | 276 | 17.8% | 17.8% | -0.3 | n/a | no target |
| P07 | 653 | 13.0% | 13.0% | -6.0 | n/a | no target |
| P08 | 19414 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P09 | 303 | 77.6% | 77.6% | -3.0 | 95% | ❌ 17 pts to go |
| P10R | 75079 | 0.3% | 0.3% |  | n/a | no target |
| P10 | 2588 | 1.9% | 1.9% | -1.2 | n/a | no target |
| P11 | 4832 | 7.3% | 7.3% | -22.0 | n/a | no target |
| P12 | 8 | 25.0% | 25.0% | -6.6 | n/a | no target |
| P13 | 14182 | 0.9% | 0.9% | -0.1 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 5.0% | 5.0% | +5.0 | n/a | no target |
| P01T | 272 | 15.1% | 15.1% | -1.2 | n/a | no target |
| P01_GOLD | 625 | 33.8% | 33.8% | -0.2 | 70% | ❌ 36 pts to go |
| P02 | 460 | 39.3% | 39.3% | -5.0 | 75% | ❌ 36 pts to go |
| P03 | 255 | 19.2% | 19.2% | -3.9 | 55% | ❌ 36 pts to go |
| P04 | 3199 | 25.0% | 25.0% | -25.5 | 75% | ❌ 50 pts to go |
| P05 | 413 | 11.1% | 11.1% | -0.6 | 50% | ❌ 39 pts to go |
| P06M | 5018 | 0.2% | 0.2% | -1.6 | n/a | no target |
| P06T | 40549 | 0.5% | 0.5% | -1.0 | n/a | no target |
| P06 | 276 | 9.4% | 9.4% | -0.8 | n/a | no target |
| P07 | 653 | 6.0% | 6.0% | -4.3 | n/a | no target |
| P08 | 19414 | 0.2% | 0.2% | -0.3 | n/a | no target |
| P09 | 303 | 75.2% | 75.2% | -2.5 | 95% | ❌ 20 pts to go |
| P10R | 75079 | 0.2% | 0.2% |  | n/a | no target |
| P10 | 2588 | 1.1% | 1.1% | -0.7 | n/a | no target |
| P11 | 4832 | 7.1% | 7.1% | -21.8 | n/a | no target |
| P12 | 8 | 12.5% | 12.5% | -3.3 | n/a | no target |
| P13 | 14182 | 0.6% | 0.6% | +0.0 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 6.7% | 6.7% | -10.0 | n/a | no target |
| P01T | 272 | 11.4% | 11.4% | -8.2 | n/a | no target |
| P01_GOLD | 625 | 57.9% | 58.1% | +0.0 | 80% | ❌ 22 pts to go |
| P02 | 460 | 46.3% | 46.5% | -5.9 | 75% | ❌ 29 pts to go |
| P03 | 255 | 38.0% | 38.0% | -7.2 | 70% | ❌ 32 pts to go |
| P04 | 3199 | 24.5% | 25.1% | -24.2 | 70% | ❌ 46 pts to go |
| P05 | 413 | 14.8% | 14.8% | -1.6 | 50% | ❌ 35 pts to go |
| P06M | 5018 | 0.7% | 0.7% | -3.5 | n/a | no target |
| P06T | 40549 | 0.4% | 0.4% | -1.2 | n/a | no target |
| P06 | 276 | 14.5% | 14.5% | -9.6 | n/a | no target |
| P07 | 653 | 2.6% | 2.6% | -2.6 | n/a | no target |
| P08 | 19414 | 0.4% | 0.4% | -0.6 | n/a | no target |
| P09 | 303 | 45.9% | 46.2% | +1.8 | 80% | ❌ 34 pts to go |
| P10R | 75079 | 0.1% | 0.1% |  | n/a | no target |
| P10 | 2588 | 1.3% | 1.3% | -0.2 | n/a | no target |
| P11 | 4832 | 2.3% | 2.3% | -14.4 | n/a | no target |
| P12 | 8 | 37.5% | 37.5% | +5.9 | n/a | no target |
| P13 | 14182 | 0.4% | 0.4% | +0.1 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 15.0% | 15.0% | -23.9 | n/a | no target |
| P01T | 272 | 26.5% | 26.5% | -30.0 | 60% | ❌ 34 pts to go |
| P01_GOLD | 625 | 63.5% | 63.5% | +0.0 | 70% | 🟡 6 pts to go |
| P02 | 460 | 39.3% | 39.3% | -4.5 | 50% | ❌ 11 pts to go |
| P03 | 255 | 50.2% | 50.2% | -5.1 | 55% | 🟡 5 pts to go |
| P04 | 3199 | 14.2% | 14.2% | -8.7 | 40% | ❌ 26 pts to go |
| P05 | 413 | 17.9% | 17.9% | +0.5 | 40% | ❌ 22 pts to go |
| P06M | 5018 | 1.2% | 1.2% | -15.5 | n/a | no target |
| P06T | 40549 | 2.8% | 2.8% | -9.7 | n/a | no target |
| P06 | 276 | 20.7% | 20.7% | -10.0 | n/a | no target |
| P07 | 653 | 7.7% | 7.7% | -8.6 | n/a | no target |
| P08 | 19414 | 3.3% | 3.3% | -1.4 | n/a | no target |
| P09 | 303 | 5.9% | 5.9% | +0.1 | n/a | no target |
| P10R | 75079 | 0.2% | 0.2% |  | n/a | no target |
| P10 | 2588 | 4.7% | 4.7% | +0.8 | n/a | no target |
| P11 | 4832 | 10.6% | 10.6% | +3.0 | n/a | no target |
| P12 | 8 | 12.5% | 12.5% | -3.3 | n/a | no target |
| P13 | 14182 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 20.0% | 20.0% | -24.4 | n/a | no target |
| P01T | 272 | 30.9% | 30.9% | -38.7 | 65% | ❌ 34 pts to go |
| P01_GOLD | 625 | 69.1% | 69.1% | -0.1 | 70% | 🟡 1 pts to go |
| P02 | 460 | 24.1% | 24.1% | -2.1 | 50% | ❌ 26 pts to go |
| P03 | 255 | 52.5% | 52.5% | -3.7 | 60% | 🟡 8 pts to go |
| P04 | 3199 | 6.2% | 6.2% | -3.7 | 40% | ❌ 34 pts to go |
| P05 | 413 | 20.3% | 20.3% | -1.1 | 45% | ❌ 25 pts to go |
| P06M | 5018 | 0.6% | 0.6% | -6.5 | n/a | no target |
| P06T | 40549 | 0.8% | 0.8% | -3.5 | n/a | no target |
| P06 | 276 | 34.8% | 34.8% | -13.4 | n/a | no target |
| P07 | 653 | 8.3% | 8.3% | -15.5 | n/a | no target |
| P08 | 19414 | 1.4% | 1.4% | -1.0 | n/a | no target |
| P09 | 303 | 9.9% | 9.9% | +1.2 | n/a | no target |
| P10R | 75079 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2588 | 2.7% | 2.7% | +0.6 | n/a | no target |
| P11 | 4832 | 2.4% | 2.4% | -4.4 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | -10.5 | n/a | no target |
| P13 | 14182 | 0.3% | 0.3% | +0.1 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 5.0% | 5.0% | -6.1 | n/a | no target |
| P01T | 272 | 17.6% | 17.6% | -27.0 | n/a | no target |
| P01_GOLD | 625 | 49.8% | 49.8% | +0.0 | 50% | 🟡 0 pts to go |
| P02 | 460 | 37.8% | 37.8% | -4.8 | n/a | no target |
| P03 | 255 | 53.3% | 53.3% | -5.4 | 60% | 🟡 7 pts to go |
| P04 | 3199 | 13.8% | 13.8% | -12.6 | n/a | no target |
| P05 | 413 | 15.7% | 15.7% | -1.0 | n/a | no target |
| P06M | 5018 | 0.4% | 0.4% | -3.8 | n/a | no target |
| P06T | 40549 | 0.6% | 0.6% | -3.4 | n/a | no target |
| P06 | 276 | 23.6% | 23.6% | -11.9 | n/a | no target |
| P07 | 653 | 8.6% | 8.6% | -10.1 | n/a | no target |
| P08 | 19414 | 0.6% | 0.6% | -0.9 | n/a | no target |
| P09 | 303 | 18.2% | 18.2% | -0.7 | n/a | no target |
| P10R | 75079 | 0.1% | 0.1% |  | n/a | no target |
| P10 | 2588 | 2.4% | 2.4% | +0.0 | n/a | no target |
| P11 | 4832 | 1.9% | 1.9% | -5.9 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | -21.1 | n/a | no target |
| P13 | 14182 | 0.5% | 0.5% | +0.1 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 13.3% | 13.3% | -14.5 | 15% | 🟡 2 pts to go |
| P01T | 272 | 12.1% | 12.1% | -17.2 | 15% | 🟡 3 pts to go |
| P01_GOLD | 625 | 35.4% | 35.4% | +0.3 | 40% | 🟡 5 pts to go |
| P02 | 460 | 12.6% | 12.8% | -1.3 | 25% | ❌ 12 pts to go |
| P03 | 255 | 18.0% | 18.0% | -3.6 | 25% | 🟡 7 pts to go |
| P04 | 3199 | 2.9% | 2.9% | -2.3 | 15% | ❌ 12 pts to go |
| P05 | 413 | 7.0% | 7.0% | -1.1 | 15% | 🟡 8 pts to go |
| P06M | 5018 | 0.6% | 0.6% | -5.4 | 15% | ❌ 14 pts to go |
| P06T | 40549 | 0.3% | 0.3% | -1.2 | 15% | ❌ 15 pts to go |
| P06 | 276 | 9.4% | 9.4% | -0.8 | 15% | 🟡 6 pts to go |
| P07 | 653 | 3.4% | 3.4% | -3.3 | 15% | ❌ 12 pts to go |
| P08 | 19414 | 0.2% | 0.2% | -0.7 | 15% | ❌ 15 pts to go |
| P09 | 303 | 1.0% | 1.0% | +0.2 | 15% | ❌ 14 pts to go |
| P10R | 75079 | 0.2% | 0.2% |  | 15% | ❌ 15 pts to go |
| P10 | 2588 | 0.8% | 0.8% | -0.6 | 15% | ❌ 14 pts to go |
| P11 | 4832 | 0.4% | 0.4% | -0.9 | 15% | ❌ 15 pts to go |
| P12 | 8 | 12.5% | 12.5% | +12.5 | 15% | 🟡 2 pts to go |
| P13 | 14182 | 0.4% | 0.4% | -0.1 | 15% | ❌ 15 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 6.7% | 6.7% | -4.4 | 15% | 🟡 8 pts to go |
| P01T | 272 | 14.7% | 14.7% | -17.9 | 25% | ❌ 10 pts to go |
| P01_GOLD | 625 | 29.1% | 29.1% | -0.1 | 25% | ✅ met |
| P02 | 460 | 25.4% | 25.4% | -2.6 | 15% | ✅ met |
| P03 | 255 | 21.6% | 21.6% | -4.4 | 15% | ✅ met |
| P04 | 3199 | 4.4% | 4.4% | -3.8 | 15% | ❌ 11 pts to go |
| P05 | 413 | 11.1% | 11.1% | -0.9 | 15% | 🟡 4 pts to go |
| P06M | 5018 | 0.4% | 0.4% | -2.0 | 15% | ❌ 15 pts to go |
| P06T | 40549 | 0.4% | 0.4% | -2.3 | 15% | ❌ 15 pts to go |
| P06 | 276 | 7.6% | 7.6% | -4.4 | 15% | 🟡 7 pts to go |
| P07 | 653 | 3.4% | 3.4% | -4.1 | 15% | ❌ 12 pts to go |
| P08 | 19414 | 0.5% | 0.5% | -0.5 | 15% | ❌ 14 pts to go |
| P09 | 303 | 1.0% | 1.0% | +0.2 | 15% | ❌ 14 pts to go |
| P10R | 75079 | 0.0% | 0.0% |  | 15% | ❌ 15 pts to go |
| P10 | 2588 | 1.6% | 1.6% | +0.2 | 15% | ❌ 13 pts to go |
| P11 | 4832 | 1.3% | 1.3% | -3.8 | 15% | ❌ 14 pts to go |
| P12 | 8 | 25.0% | 25.0% | -1.3 | 15% | ✅ met |
| P13 | 14182 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 0.0% | 0.0% | -5.6 | 20% | ❌ 20 pts to go |
| P01T | 272 | 4.8% | 4.8% | -5.0 | 20% | ❌ 15 pts to go |
| P01_GOLD | 625 | 4.3% | 4.3% | +0.0 | 20% | ❌ 16 pts to go |
| P02 | 460 | 1.3% | 1.3% | -0.2 | 20% | ❌ 19 pts to go |
| P03 | 255 | 1.6% | 1.6% | -0.3 | 20% | ❌ 18 pts to go |
| P04 | 3199 | 0.6% | 0.6% | -0.4 | 20% | ❌ 19 pts to go |
| P05 | 413 | 1.2% | 1.2% | +0.2 | 20% | ❌ 19 pts to go |
| P06M | 5018 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 40549 | 0.0% | 0.0% | -0.2 | 20% | ❌ 20 pts to go |
| P06 | 276 | 1.4% | 1.4% | -2.2 | 20% | ❌ 19 pts to go |
| P07 | 653 | 0.6% | 0.6% | -0.2 | 20% | ❌ 19 pts to go |
| P08 | 19414 | 0.0% | 0.0% | -0.2 | 20% | ❌ 20 pts to go |
| P09 | 303 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10R | 75079 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P10 | 2588 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 4832 | 0.1% | 0.1% | -0.5 | 20% | ❌ 20 pts to go |
| P12 | 8 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 14182 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 1.7% | 1.7% | -3.9 | 15% | ❌ 13 pts to go |
| P01T | 272 | 2.9% | 2.9% | -4.7 | 15% | ❌ 12 pts to go |
| P01_GOLD | 625 | 10.6% | 10.6% | +0.0 | 15% | 🟡 4 pts to go |
| P02 | 460 | 12.0% | 12.0% | -1.4 | 15% | 🟡 3 pts to go |
| P03 | 255 | 20.8% | 20.8% | -3.2 | 15% | ✅ met |
| P04 | 3199 | 2.6% | 2.6% | -2.0 | 15% | ❌ 12 pts to go |
| P05 | 413 | 3.1% | 3.1% | +0.2 | 15% | ❌ 12 pts to go |
| P06M | 5018 | 0.3% | 0.3% | -2.1 | 15% | ❌ 15 pts to go |
| P06T | 40549 | 0.3% | 0.3% | -1.1 | 15% | ❌ 15 pts to go |
| P06 | 276 | 5.8% | 5.8% | +0.4 | 15% | 🟡 9 pts to go |
| P07 | 653 | 2.0% | 2.0% | -1.6 | 15% | ❌ 13 pts to go |
| P08 | 19414 | 0.5% | 0.5% | -0.2 | 15% | ❌ 14 pts to go |
| P09 | 303 | 0.7% | 0.7% | +0.2 | 15% | ❌ 14 pts to go |
| P10R | 75079 | 0.0% | 0.0% |  | 15% | ❌ 15 pts to go |
| P10 | 2588 | 1.0% | 1.0% | +0.2 | 15% | ❌ 14 pts to go |
| P11 | 4832 | 0.8% | 0.8% | -1.3 | 15% | ❌ 14 pts to go |
| P12 | 8 | 0.0% | 0.0% | -5.3 | 15% | ❌ 15 pts to go |
| P13 | 14182 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 6.7% | 6.7% | -4.4 | 20% | ❌ 13 pts to go |
| P01T | 272 | 18.4% | 18.4% | -22.9 | 40% | ❌ 22 pts to go |
| P01_GOLD | 625 | 45.8% | 45.8% | +0.0 | 40% | ✅ met |
| P02 | 460 | 43.0% | 43.0% | -5.5 | 20% | ✅ met |
| P03 | 255 | 49.0% | 49.0% | -6.8 | 35% | ✅ met |
| P04 | 3199 | 16.3% | 16.3% | -14.0 | 20% | 🟡 4 pts to go |
| P05 | 413 | 15.3% | 15.3% | -1.4 | 20% | 🟡 5 pts to go |
| P06M | 5018 | 0.7% | 0.7% | -3.5 | 20% | ❌ 19 pts to go |
| P06T | 40549 | 0.9% | 0.9% | -3.6 | 20% | ❌ 19 pts to go |
| P06 | 276 | 23.2% | 23.2% | -12.3 | 20% | ✅ met |
| P07 | 653 | 8.3% | 8.3% | -6.4 | 20% | ❌ 12 pts to go |
| P08 | 19414 | 0.9% | 0.9% | -1.4 | 20% | ❌ 19 pts to go |
| P09 | 303 | 18.2% | 18.2% | -3.8 | 20% | 🟡 2 pts to go |
| P10R | 75079 | 0.2% | 0.2% |  | 20% | ❌ 20 pts to go |
| P10 | 2588 | 3.4% | 3.4% | +0.8 | 20% | ❌ 17 pts to go |
| P11 | 4832 | 2.0% | 2.0% | -6.0 | 20% | ❌ 18 pts to go |
| P12 | 8 | 0.0% | 0.0% | -15.8 | 20% | ❌ 20 pts to go |
| P13 | 14182 | 0.7% | 0.7% | +0.1 | 20% | ❌ 19 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 51.7% | 51.7% | +51.7 | n/a | no target |
| P01T | 272 | 0.4% | 0.4% | -0.7 | n/a | no target |
| P01_GOLD | 625 | 69.4% | 69.4% | -0.3 | 95% | ❌ 26 pts to go |
| P02 | 460 | 63.7% | 63.7% | -9.6 | 95% | ❌ 31 pts to go |
| P03 | 255 | 54.9% | 54.9% | -12.4 | 90% | ❌ 35 pts to go |
| P04 | 3199 | 28.9% | 28.9% | -29.5 | 85% | ❌ 56 pts to go |
| P05 | 413 | 36.8% | 36.8% | +1.9 | 75% | ❌ 38 pts to go |
| P06M | 5018 | 60.8% | 60.8% | +60.8 | n/a | no target |
| P06T | 40549 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 653 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 19414 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 89.4% | 89.4% | -1.4 | 100% | ❌ 11 pts to go |
| P10R | 75079 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2588 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 4832 | 1.8% | 1.8% | -17.0 | 60% | ❌ 58 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 14182 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 51.7% | 51.7% | +51.7 | n/a | no target |
| P01T | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 72.8% | 72.8% | -0.1 | 100% | ❌ 27 pts to go |
| P02 | 460 | 67.2% | 67.2% | -10.0 | 100% | ❌ 33 pts to go |
| P03 | 255 | 60.8% | 60.8% | -13.7 | n/a | no target |
| P04 | 3199 | 29.6% | 29.6% | -30.4 | 95% | ❌ 65 pts to go |
| P05 | 413 | 33.4% | 33.4% | +2.2 | 80% | ❌ 47 pts to go |
| P06M | 5018 | 60.8% | 60.8% | +60.8 | n/a | no target |
| P06T | 40549 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 653 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 19414 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 92.7% | 92.7% | -0.7 | 100% | 🟡 7 pts to go |
| P10R | 75079 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2588 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 4832 | 1.9% | 1.9% | -18.1 | n/a | no target |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 14182 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 70.0% | 70.0% | +70.0 | n/a | no target |
| P01T | 272 | 0.4% | 0.4% | -0.7 | n/a | no target |
| P01_GOLD | 625 | 51.7% | 51.7% | -0.2 | 85% | ❌ 33 pts to go |
| P02 | 460 | 58.3% | 58.3% | -8.5 | 90% | ❌ 32 pts to go |
| P03 | 255 | 44.3% | 44.3% | -10.5 | 85% | ❌ 41 pts to go |
| P04 | 3199 | 32.1% | 32.1% | -32.0 | 90% | ❌ 58 pts to go |
| P05 | 413 | 32.4% | 32.4% | -2.8 | 75% | ❌ 43 pts to go |
| P06M | 5018 | 89.5% | 89.5% | +89.5 | n/a | no target |
| P06T | 40549 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 653 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 19414 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 85.1% | 85.1% | -0.5 | 95% | 🟡 10 pts to go |
| P10R | 75079 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2588 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 4832 | 1.7% | 1.7% | -15.6 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 14182 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 70.0% | 70.0% | +70.0 | n/a | no target |
| P01T | 272 | 0.4% | 0.4% | -0.7 | n/a | no target |
| P01_GOLD | 625 | 51.7% | 51.7% | -0.4 | 85% | ❌ 33 pts to go |
| P02 | 460 | 53.3% | 53.3% | -7.8 | 90% | ❌ 37 pts to go |
| P03 | 255 | 45.5% | 45.5% | -10.7 | 85% | ❌ 40 pts to go |
| P04 | 3199 | 27.4% | 27.4% | -26.9 | 90% | ❌ 63 pts to go |
| P05 | 413 | 42.4% | 42.4% | +0.7 | 75% | ❌ 33 pts to go |
| P06M | 5018 | 82.5% | 82.5% | +82.5 | n/a | no target |
| P06T | 40549 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 653 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 19414 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 0.3% | 0.3% | +0.0 | 95% | ❌ 95 pts to go |
| P10R | 75079 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2588 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 4832 | 1.4% | 1.4% | -12.7 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 14182 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 76.7% | 76.7% | +76.7 | n/a | no target |
| P01T | 272 | 91.2% | 91.2% | +9.7 | n/a | no target |
| P01_GOLD | 625 | 85.4% | 85.4% | -0.3 | 100% | ❌ 15 pts to go |
| P02 | 460 | 76.3% | 76.3% | -5.4 | 100% | ❌ 24 pts to go |
| P03 | 255 | 92.2% | 92.2% | -0.1 | n/a | no target |
| P04 | 3199 | 53.5% | 53.5% | -19.1 | 95% | ❌ 42 pts to go |
| P05 | 413 | 77.7% | 77.7% | +2.2 | 95% | ❌ 17 pts to go |
| P06M | 5018 | 96.9% | 96.9% | +96.3 | n/a | no target |
| P06T | 40549 | 83.4% | 83.4% | +0.0 | n/a | no target |
| P06 | 276 | 28.3% | 28.3% | -47.6 | n/a | no target |
| P07 | 653 | 21.6% | 21.6% | -55.4 | n/a | no target |
| P08 | 19414 | 13.0% | 13.1% | -71.9 | n/a | no target |
| P09 | 303 | 98.7% | 98.7% | -0.3 | 100% | 🟡 1 pts to go |
| P10R | 75079 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2588 | 72.8% | 72.8% | -25.6 | n/a | no target |
| P11 | 4832 | 27.7% | 27.7% | -62.2 | n/a | no target |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 14182 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 76.7% | 76.7% | +76.7 | n/a | no target |
| P01T | 272 | 91.2% | 91.2% | +9.7 | n/a | no target |
| P01_GOLD | 625 | 88.6% | 88.6% | -0.3 | 100% | ❌ 11 pts to go |
| P02 | 460 | 77.4% | 77.6% | -5.5 | 100% | ❌ 23 pts to go |
| P03 | 255 | 92.9% | 92.9% | -0.9 | n/a | no target |
| P04 | 3199 | 57.2% | 57.2% | -21.8 | 95% | ❌ 38 pts to go |
| P05 | 413 | 90.3% | 90.3% | +0.2 | 70% | ✅ met |
| P06M | 5018 | 96.9% | 96.9% | +96.3 | n/a | no target |
| P06T | 40549 | 83.4% | 83.4% | +0.0 | n/a | no target |
| P06 | 276 | 28.3% | 28.3% | -47.6 | n/a | no target |
| P07 | 653 | 21.6% | 21.6% | -55.4 | n/a | no target |
| P08 | 19414 | 13.0% | 13.1% | -71.9 | n/a | no target |
| P09 | 303 | 98.7% | 98.7% | -0.3 | 100% | 🟡 1 pts to go |
| P10R | 75079 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2588 | 72.8% | 72.8% | -25.6 | n/a | no target |
| P11 | 4832 | 27.8% | 27.8% | -62.5 | n/a | no target |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 14182 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 272 | 0.0% | 0.0% | -1.1 | n/a | no target |
| P01_GOLD | 625 | 16.8% | 16.8% | -0.5 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 362 rows, 29.0% filled |
| P02 | 460 | 11.3% | 11.3% | -1.8 | n/a | no target · rows from a source that publishes bids: 290 rows, 17.9% filled |
| P03 | 255 | 13.3% | 13.3% | -3.0 | n/a | no target · rows from a source that publishes bids: 139 rows, 24.5% filled |
| P04 | 3199 | 1.7% | 1.7% | -2.0 | n/a | no target · rows from a source that publishes bids: 870 rows, 6.3% filled |
| P05 | 413 | 3.1% | 3.1% | -0.3 | n/a | no target · rows from a source that publishes bids: 53 rows, 24.5% filled |
| P06M | 5018 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 40549 | 0.0% | 0.0% | -0.1 | n/a | no target |
| P06 | 276 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 653 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 19414 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 3.0% | 3.0% | -0.1 | n/a | no target · rows from a source that publishes bids: 290 rows, 3.1% filled |
| P10R | 75079 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2588 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 4832 | 0.2% | 0.2% | -2.5 | n/a | no target · rows from a source that publishes bids: 90 rows, 12.2% filled |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 8 rows, 0.0% filled |
| P13 | 14182 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 272 | 0.4% | 98.2% | +0.4 | n/a | no target |
| P01_GOLD | 625 | 53.1% | 82.4% | -0.1 | 90% | ❌ 37 pts to go |
| P02 | 460 | 53.0% | 87.4% | -8.1 | 90% | ❌ 37 pts to go |
| P03 | 255 | 45.9% | 80.0% | -10.3 | 90% | ❌ 44 pts to go |
| P04 | 3199 | 22.2% | 92.9% | -23.1 | 90% | ❌ 68 pts to go |
| P05 | 413 | 0.0% | 82.3% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 5018 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 40549 | 0.0% | 99.8% | +0.0 | n/a | no target |
| P06 | 276 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 653 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 19414 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 303 | 2.3% | 4.0% | +0.2 | 90% | ❌ 88 pts to go |
| P10R | 75079 | 0.0% | 100.0% |  | n/a | no target |
| P10 | 2588 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 4832 | 1.3% | 99.1% | -11.4 | n/a | no target |
| P12 | 8 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 14182 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 272 | 0.7% | 98.5% | +0.7 | n/a | no target |
| P01_GOLD | 625 | 25.9% | 55.2% | -0.1 | 90% | ❌ 64 pts to go |
| P02 | 460 | 52.2% | 86.5% | -7.7 | n/a | no target |
| P03 | 255 | 25.1% | 59.2% | -5.7 | n/a | no target |
| P04 | 3199 | 24.4% | 95.1% | -25.3 | n/a | no target |
| P05 | 413 | 0.5% | 82.8% | +0.0 | n/a | no target |
| P06M | 5018 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 40549 | 0.1% | 99.9% | +0.1 | n/a | no target |
| P06 | 276 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 653 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 19414 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 303 | 41.9% | 43.6% | -2.5 | n/a | no target |
| P10R | 75079 | 0.0% | 100.0% |  | n/a | no target |
| P10 | 2588 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 4832 | 1.2% | 99.0% | -10.4 | n/a | no target |
| P12 | 8 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 14182 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 272 | 1.8% | 99.6% | -0.4 | n/a | no target |
| P01_GOLD | 625 | 51.7% | 81.0% | +0.1 | 95% | ❌ 43 pts to go |
| P02 | 460 | 57.2% | 91.5% | -8.4 | n/a | no target |
| P03 | 255 | 48.2% | 82.4% | -10.9 | n/a | no target |
| P04 | 3199 | 24.6% | 95.3% | -25.7 | n/a | no target |
| P05 | 413 | 4.8% | 87.2% | -0.4 | n/a | no target |
| P06M | 5018 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 40549 | 0.1% | 100.0% | +0.1 | n/a | no target |
| P06 | 276 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 653 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 19414 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 303 | 64.0% | 65.7% | -3.5 | n/a | no target |
| P10R | 75079 | 0.0% | 100.0% |  | n/a | no target |
| P10 | 2588 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 4832 | 1.2% | 99.1% | -11.5 | n/a | no target |
| P12 | 8 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 14182 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 98.3% | 98.3% | -1.7 | 100% | 🟡 2 pts to go |
| P01T | 272 | 96.0% | 96.0% | -4.0 | 100% | 🟡 4 pts to go |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 460 | 99.1% | 99.1% | -0.9 | 100% | 🟡 1 pts to go |
| P03 | 255 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3199 | 97.9% | 97.9% | -2.1 | 100% | 🟡 2 pts to go |
| P05 | 413 | 98.8% | 98.8% | -1.2 | 100% | 🟡 1 pts to go |
| P06M | 5018 | 93.8% | 93.8% | -6.2 | 100% | 🟡 6 pts to go |
| P06T | 40549 | 84.7% | 84.7% | -15.3 | 100% | ❌ 15 pts to go |
| P06 | 276 | 98.9% | 98.9% | -1.1 | 100% | 🟡 1 pts to go |
| P07 | 653 | 96.8% | 96.8% | -3.2 | 100% | 🟡 3 pts to go |
| P08 | 19414 | 96.4% | 96.4% | -3.6 | 100% | 🟡 4 pts to go |
| P09 | 303 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 75079 | 75.5% | 75.5% |  | 100% | ❌ 24 pts to go |
| P10 | 2588 | 96.6% | 96.6% | -3.4 | 100% | 🟡 3 pts to go |
| P11 | 4832 | 96.9% | 96.9% | -3.1 | 100% | 🟡 3 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 14182 | 89.3% | 89.3% | -10.7 | 100% | ❌ 11 pts to go |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 98.3% | 98.3% | -1.7 | 100% | 🟡 2 pts to go |
| P01T | 272 | 96.0% | 96.0% | -4.0 | 100% | 🟡 4 pts to go |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 460 | 99.1% | 99.1% | -0.9 | 100% | 🟡 1 pts to go |
| P03 | 255 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3199 | 97.9% | 97.9% | -2.1 | 100% | 🟡 2 pts to go |
| P05 | 413 | 98.8% | 98.8% | -1.2 | 100% | 🟡 1 pts to go |
| P06M | 5018 | 93.8% | 93.8% | -6.2 | 100% | 🟡 6 pts to go |
| P06T | 40549 | 84.7% | 84.7% | -15.3 | 100% | ❌ 15 pts to go |
| P06 | 276 | 98.9% | 98.9% | -1.1 | 100% | 🟡 1 pts to go |
| P07 | 653 | 96.8% | 96.8% | -3.2 | 100% | 🟡 3 pts to go |
| P08 | 19414 | 96.4% | 96.4% | -3.6 | 100% | 🟡 4 pts to go |
| P09 | 303 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 75079 | 75.5% | 75.5% |  | 100% | ❌ 24 pts to go |
| P10 | 2588 | 96.6% | 96.6% | -3.4 | 100% | 🟡 3 pts to go |
| P11 | 4832 | 96.9% | 96.9% | -3.1 | 100% | 🟡 3 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 14182 | 89.3% | 89.3% | -10.7 | 100% | ❌ 11 pts to go |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 60 | 98.3% | 98.3% | -1.7 | 100% | 🟡 2 pts to go |
| P01T | 272 | 96.0% | 96.0% | -4.0 | 100% | 🟡 4 pts to go |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 460 | 99.1% | 99.1% | -0.9 | 100% | 🟡 1 pts to go |
| P03 | 255 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3199 | 97.9% | 97.9% | -2.1 | 100% | 🟡 2 pts to go |
| P05 | 413 | 98.8% | 98.8% | -1.2 | 100% | 🟡 1 pts to go |
| P06M | 5018 | 93.8% | 93.8% | -6.2 | 100% | 🟡 6 pts to go |
| P06T | 40549 | 84.7% | 84.7% | -15.3 | 100% | ❌ 15 pts to go |
| P06 | 276 | 98.9% | 98.9% | -1.1 | 100% | 🟡 1 pts to go |
| P07 | 653 | 96.8% | 96.8% | -3.2 | 100% | 🟡 3 pts to go |
| P08 | 19414 | 96.4% | 96.4% | -3.6 | 100% | 🟡 4 pts to go |
| P09 | 303 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 75079 | 75.5% | 75.5% |  | 100% | ❌ 24 pts to go |
| P10 | 2588 | 96.6% | 96.6% | -3.4 | 100% | 🟡 3 pts to go |
| P11 | 4832 | 96.9% | 96.9% | -3.1 | 100% | 🟡 3 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 14182 | 89.3% | 89.3% | -10.7 | 100% | ❌ 11 pts to go |

