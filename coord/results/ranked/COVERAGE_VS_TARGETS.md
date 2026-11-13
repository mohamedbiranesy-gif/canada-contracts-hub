# Coverage vs the downstream team's targets — 2026-11-12

Benchmarks (field × package with a numeric target): **93 of 438 met** (21.2%); 62 within 10 points; 283 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 249, P01T 229, P01_GOLD 627, P02 468, P03 266, P04 3573, P05 422, P06M 22259, P06T 59840, P06 280, P07 831, P08 30624, P09 275, P10R 0, P10 2126, P11 1813, P12 11, P13 152067

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 249 | 0.0% | 14.5% | 7 | vendor GST/HST number (233 rows) |
| P01T | 229 | 1.3% | 37.1% | 8 | payment terms (183 rows) |
| P01_GOLD | 627 | 23.9% | 71.6% | 10 | payment terms (222 rows) |
| P02 | 468 | 7.5% | 55.6% | 9 | PO rule (357 rows) |
| P03 | 266 | 15.4% | 56.4% | 9 | PO rule (132 rows) |
| P04 | 3573 | 1.3% | 17.1% | 6 | PO rule (3373 rows) |
| P05 | 422 | 0.9% | 17.1% | 7 | payment terms (350 rows) |
| P06M | 22259 | 0.0% | 2.8% | 7 | PO rule (21880 rows) |
| P06T | 59840 | 0.1% | 13.0% | 7 | PO rule (59459 rows) |
| P06 | 280 | 0.0% | 10.0% | 6 | reference to quote (PO / contract / vendor id) (262 rows) |
| P07 | 831 | 0.0% | 2.4% | 6 | payment terms (790 rows) |
| P08 | 30624 | 0.0% | 0.9% | 6 | PO rule (30353 rows) |
| P09 | 275 | 1.5% | 42.2% | 8 | payment terms (257 rows) |
| P10 | 2126 | 0.0% | 1.3% | 5 | reference to quote (PO / contract / vendor id) (2126 rows) |
| P11 | 1813 | 0.1% | 7.7% | 6 | PO rule (1748 rows) |
| P12 | 11 | 0.0% | 36.4% | 8 | PO rule (11 rows) |
| P13 | 152067 | 0.0% | 0.3% | 7 | reference to quote (PO / contract / vendor id) (152067 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 249 | 9 | 56 | 184 | 0 | 0 | 70 |
| P01T | 229 | 27 | 38 | 164 | 0 | 0 | 67 |
| P01_GOLD | 627 | 254 | 169 | 204 | 0 | 0 | 82 |
| P02 | 468 | 0 | 192 | 276 | 0 | 0 | 66 |
| P03 | 266 | 0 | 0 | 254 | 12 | 0 | 57 |
| P04 | 3573 | 0 | 0 | 2943 | 630 | 0 | 46 |
| P05 | 422 | 15 | 28 | 366 | 13 | 0 | 51 |
| P06M | 22259 | 0 | 18 | 22186 | 55 | 0 | 46 |
| P06T | 59840 | 0 | 28 | 40257 | 19555 | 0 | 38 |
| P06 | 280 | 18 | 42 | 220 | 0 | 0 | 67 |
| P07 | 831 | 0 | 21 | 789 | 21 | 0 | 54 |
| P08 | 30624 | 0 | 0 | 27429 | 3195 | 0 | 43 |
| P09 | 275 | 4 | 10 | 260 | 1 | 0 | 53 |
| P10 | 2126 | 3 | 13 | 1445 | 665 | 0 | 41 |
| P11 | 1813 | 7 | 12 | 36 | 0 | 1758 | 23 |
| P12 | 11 | 0 | 0 | 11 | 0 | 0 | 51 |
| P13 | 152067 | 14 | 64 | 151977 | 12 | 0 | 43 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 249 | 190 | 76.3% | tax treatment (35) |
| P01T | 229 | 138 | 60.3% | bill-to legal name and address (76) |
| P01_GOLD | 627 | 475 | 75.8% | bill-to legal name and address (96) |
| P02 | 468 | 317 | 67.7% | the buyer's PO / reference rule (86) |
| P03 | 266 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (266) |
| P04 | 3573 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (3573) |
| P05 | 422 | 44 | 10.4% | a confirmed invoicing / AP or finance channel (335) |
| P06M | 22259 | 240 | 1.1% | a confirmed invoicing / AP or finance channel (21955) |
| P06T | 59840 | 332 | 0.6% | a confirmed invoicing / AP or finance channel (59036) |
| P06 | 280 | 50 | 17.9% | the buyer's PO / reference rule (114) |
| P07 | 831 | 39 | 4.7% | bill-to legal name and address (334) |
| P08 | 30624 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (30624) |
| P09 | 275 | 39 | 14.2% | a confirmed invoicing / AP or finance channel (225) |
| P10 | 2126 | 7 | 0.3% | a confirmed invoicing / AP or finance channel (2048) |
| P11 | 1813 | 14 | 0.8% | a confirmed invoicing / AP or finance channel (1758) |
| P12 | 11 | 2 | 18.2% | a confirmed invoicing / AP or finance channel (9) |
| P13 | 152067 | 43 | 0.0% | a confirmed invoicing / AP or finance channel (149951) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 249 | 6 | 2.4% | 7 | 0 | the vendor's GST/HST number (BN9) (233) |
| P01T | 229 | 100 | 43.7% | 3 | 0 | the vendor's GST/HST number (BN9) (73) |
| P01_GOLD | 627 | 407 | 64.9% | 11 | 0 | the vendor's GST/HST number (BN9) (144) |
| P02 | 468 | 216 | 46.2% | 22 | 0 | the vendor's GST/HST number (BN9) (202) |
| P03 | 266 | 17 | 6.4% | 0 | 134 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (95) |
| P04 | 3573 | 43 | 1.2% | 7 | 904 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2560) |
| P05 | 422 | 20 | 4.7% | 8 | 125 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (202) |
| P06M | 22259 | 8 | 0.0% | 12 | 541 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (21320) |
| P06T | 59840 | 385 | 0.6% | 14 | 19073 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (39878) |
| P06 | 280 | 25 | 8.9% | 54 | 0 | the vendor's GST/HST number (BN9) (132) |
| P07 | 831 | 16 | 1.9% | 139 | 36 | the vendor's GST/HST number (BN9) (409) |
| P08 | 30624 | 5 | 0.0% | 13 | 7274 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (23286) |
| P09 | 275 | 37 | 13.5% | 0 | 107 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (106) |
| P10 | 2126 | 7 | 0.3% | 15 | 304 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (1720) |
| P11 | 1813 | 7 | 0.4% | 3 | 0 | a confirmed invoicing / AP or finance channel (1742) |
| P12 | 11 | 1 | 9.1% | 0 | 4 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (5) |
| P13 | 152067 | 21 | 0.0% | 1038 | 60772 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (88997) |
| **all** | 275960 | 1321 | 0.5% | 1346 | 89274 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 240 | 0 | 0 | 0 | 164 | 9 | 0 | 195 | 212 | 1 |
| P01T | 202 | 0 | 0 | 0 | 124 | 67 | 32 | 165 | 185 | 4 |
| P01_GOLD | 373 | 0 | 0 | 0 | 13 | 79 | 29 | 197 | 237 | 3 |
| P02 | 468 | 0 | 468 | 0 | 36 | 55 | 14 | 357 | 283 | 2 |
| P03 | 266 | 0 | 266 | 0 | 17 | 45 | 26 | 132 | 139 | 2 |
| P04 | 3573 | 0 | 3573 | 0 | 1528 | 1270 | 962 | 3373 | 3125 | 33 |
| P05 | 407 | 0 | 355 | 0 | 83 | 93 | 39 | 338 | 352 | 7 |
| P06M | 22259 | 0 | 22259 | 0 | 16567 | 1372 | 144 | 21880 | 21631 | 19 |
| P06T | 59840 | 0 | 59840 | 0 | 53651 | 37776 | 24731 | 59459 | 58933 | 376 |
| P06 | 262 | 0 | 0 | 0 | 142 | 81 | 46 | 198 | 229 | 5 |
| P07 | 831 | 0 | 831 | 0 | 566 | 347 | 119 | 789 | 790 | 5 |
| P08 | 30624 | 0 | 30624 | 0 | 24259 | 14723 | 4748 | 30353 | 29996 | 159 |
| P09 | 271 | 0 | 252 | 0 | 12 | 67 | 1 | 245 | 259 | 7 |
| P10 | 2123 | 0 | 2090 | 0 | 1101 | 1130 | 963 | 2055 | 2017 | 16 |
| P11 | 1806 | 1758 | 1710 | 0 | 914 | 1236 | 555 | 1748 | 1741 | 20 |
| P12 | 11 | 0 | 10 | 0 | 0 | 3 | 0 | 11 | 11 | 2 |
| P13 | 152053 | 0 | 151662 | 0 | 122165 | 82799 | 18 | 151731 | 150950 | 60 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_phone | P13 | 67.9% | 95% | 41271 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 30365 |
| ap_system_hint | P13 | 0.4% | 20% | 29822 |
| buyer_bn_as_published | P13 | 12.5% | 30% | 26618 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 22670 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 22625 |
| buyer_legal_name_as_published | P13 | 45.6% | 60% | 21973 |
| buyer_payment_method_preference | P13 | 0.6% | 15% | 21840 |
| buyer_logo_url | P13 | 80.8% | 95% | 21619 |
| vendor_registered_address | P08 | 29.7% | 70% | 12331 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 11952 |
| ap_system_hint | P06T | 0.6% | 20% | 11621 |
| buyer_phone | P08 | 58.6% | 95% | 11161 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 8870 |
| buyer_tax_exempt_status | P06T | 0.2% | 15% | 8857 |
| buyer_payment_method_preference | P06T | 0.7% | 15% | 8579 |
| buyer_legal_name_as_published | P08 | 51.9% | 75% | 7067 |
| buyer_logo_url | P08 | 77.8% | 100% | 6813 |
| vendor_phone | P08 | 64.0% | 85% | 6425 |
| vendor_emails | P08 | 54.8% | 75% | 6196 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 6113 |
| vendor_bn9 | P08 | 30.6% | 50% | 5950 |
| ap_system_hint | P08 | 0.8% | 20% | 5893 |
| buyer_bn_as_published | P08 | 17.7% | 35% | 5294 |
| vendor_trading_name | P08 | 33.0% | 50% | 5219 |
| buyer_esignature_preference | P08 | 0.3% | 15% | 4493 |
| buyer_tax_exempt_status | P08 | 0.3% | 15% | 4492 |
| buyer_ap_cycle_published | P06M | 0.0% | 20% | 4441 |
| buyer_payment_method_preference | P08 | 0.5% | 15% | 4436 |
| ap_system_hint | P06M | 1.0% | 20% | 4223 |
| invoice_reference_hint | P08 | 12.2% | 25% | 3916 |
| vendor_logo_url | P08 | 87.3% | 100% | 3897 |
| buyer_esignature_preference | P06M | 0.4% | 15% | 3242 |
| buyer_address | P08 | 84.5% | 95% | 3224 |
| buyer_tax_exempt_status | P06M | 0.6% | 15% | 3196 |
| buyer_payment_method_preference | P06M | 0.8% | 15% | 3166 |
| average_contract_duration_days | P04 | 19.6% | 90% | 2514 |
| currency | P04 | 27.0% | 95% | 2430 |
| end_date | P04 | 24.6% | 90% | 2337 |
| ap_phone | P04 | 20.2% | 85% | 2318 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 93.2% | 93.2% | +4.1 | 50% | ✅ met |
| P01T | 229 | 95.6% | 95.6% | +1.8 | 50% | ✅ met |
| P01_GOLD | 627 | 92.2% | 94.6% | +0.0 | 95% | 🟡 3 pts to go |
| P02 | 468 | 75.0% | 76.5% | +1.0 | 95% | ❌ 20 pts to go |
| P03 | 266 | 81.6% | 85.0% | +0.2 | 95% | ❌ 13 pts to go |
| P04 | 3573 | 31.8% | 33.6% | +1.6 | 90% | ❌ 58 pts to go |
| P05 | 422 | 39.6% | 42.4% | +1.0 | 70% | ❌ 30 pts to go |
| P06M | 22259 | 93.2% | 93.2% | +1.4 | n/a | no target |
| P06T | 59840 | 99.3% | 99.3% | +0.7 | n/a | no target |
| P06 | 280 | 35.4% | 35.4% | +1.0 | 30% | ✅ met |
| P07 | 831 | 14.2% | 14.2% | +7.3 | 30% | ❌ 16 pts to go |
| P08 | 30624 | 12.2% | 12.2% | +10.9 | 25% | ❌ 13 pts to go |
| P09 | 275 | 98.9% | 99.6% | -0.1 | 100% | 🟡 1 pts to go |
| P10 | 2126 | 3.3% | 3.3% | +0.2 | 25% | ❌ 22 pts to go |
| P11 | 1813 | 54.3% | 55.0% | +7.4 | 60% | 🟡 6 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 152067 | 99.6% | 99.6% | -0.1 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 229 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 627 | 5.7% | 5.7% | -0.4 | 50% | ❌ 44 pts to go |
| P02 | 468 | 6.2% | 6.2% | +0.0 | 50% | ❌ 44 pts to go |
| P03 | 266 | 1.9% | 1.9% | +0.4 | 40% | ❌ 38 pts to go |
| P04 | 3573 | 0.6% | 0.6% | +0.1 | 30% | ❌ 29 pts to go |
| P05 | 422 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 22259 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 59840 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 280 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 831 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30624 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 275 | 0.7% | 0.7% | +0.0 | 50% | ❌ 49 pts to go |
| P10 | 2126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1813 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 152067 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 89.6% | 89.6% | +7.4 | n/a | no target |
| P01T | 229 | 79.9% | 79.9% | +5.4 | 50% | ✅ met |
| P01_GOLD | 627 | 67.3% | 67.3% | +0.5 | 85% | ❌ 18 pts to go |
| P02 | 468 | 66.2% | 66.2% | +1.4 | 90% | ❌ 24 pts to go |
| P03 | 266 | 60.5% | 60.5% | +0.8 | 85% | ❌ 24 pts to go |
| P04 | 3573 | 29.1% | 29.1% | +1.5 | 85% | ❌ 56 pts to go |
| P05 | 422 | 29.9% | 29.9% | +1.0 | 60% | ❌ 30 pts to go |
| P06M | 22259 | 93.0% | 93.0% | +1.5 | n/a | no target |
| P06T | 59840 | 99.2% | 99.2% | +0.8 | n/a | no target |
| P06 | 280 | 6.4% | 6.4% | +6.4 | n/a | no target |
| P07 | 831 | 9.1% | 9.1% | +9.1 | n/a | no target |
| P08 | 30624 | 11.3% | 11.3% | +11.3 | n/a | no target |
| P09 | 275 | 95.6% | 95.6% | -0.5 | 100% | 🟡 4 pts to go |
| P10 | 2126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1813 | 51.5% | 51.5% | +8.2 | 60% | 🟡 8 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 152067 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 229 | 0.0% | 0.0% | +0.0 | 30% | ❌ 30 pts to go |
| P01_GOLD | 627 | 51.7% | 51.7% | +0.9 | 80% | ❌ 28 pts to go |
| P02 | 468 | 58.1% | 58.1% | +1.2 | 60% | 🟡 2 pts to go |
| P03 | 266 | 50.4% | 50.4% | +0.2 | 80% | ❌ 30 pts to go |
| P04 | 3573 | 24.0% | 24.0% | +1.1 | 50% | ❌ 26 pts to go |
| P05 | 422 | 12.6% | 12.6% | +1.2 | 40% | ❌ 27 pts to go |
| P06M | 22259 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 59840 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 280 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 831 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30624 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 275 | 81.1% | 81.1% | -2.3 | 50% | ✅ met |
| P10 | 2126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1813 | 3.3% | 3.3% | -2.3 | 40% | ❌ 37 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 152067 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 229 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P01_GOLD | 627 | 60.9% | 60.9% | +0.5 | 85% | ❌ 24 pts to go |
| P02 | 468 | 58.1% | 58.1% | +1.9 | 90% | ❌ 32 pts to go |
| P03 | 266 | 59.4% | 59.4% | +0.8 | 85% | ❌ 26 pts to go |
| P04 | 3573 | 24.9% | 24.9% | +1.3 | 85% | ❌ 60 pts to go |
| P05 | 422 | 20.4% | 20.4% | +0.7 | 50% | ❌ 30 pts to go |
| P06M | 22259 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 59840 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 280 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 831 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30624 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 275 | 97.1% | 97.1% | +0.0 | 100% | 🟡 3 pts to go |
| P10 | 2126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1813 | 3.6% | 3.6% | -2.4 | 60% | ❌ 56 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 152067 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 229 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 627 | 12.6% | 12.6% | -0.3 | 60% | ❌ 47 pts to go |
| P02 | 468 | 7.3% | 7.3% | +1.3 | 50% | ❌ 43 pts to go |
| P03 | 266 | 8.6% | 8.6% | +0.2 | 50% | ❌ 41 pts to go |
| P04 | 3573 | 1.9% | 1.9% | +0.1 | 40% | ❌ 38 pts to go |
| P05 | 422 | 0.7% | 0.7% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 22259 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 59840 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 280 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 831 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30624 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 275 | 3.6% | 3.6% | +0.3 | 50% | ❌ 46 pts to go |
| P10 | 2126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1813 | 0.4% | 0.4% | -0.5 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 152067 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 229 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 627 | 35.9% | 35.9% | +1.1 | 80% | ❌ 44 pts to go |
| P02 | 468 | 53.0% | 53.0% | +1.1 | 90% | ❌ 37 pts to go |
| P03 | 266 | 33.8% | 33.8% | +1.1 | 80% | ❌ 46 pts to go |
| P04 | 3573 | 22.2% | 22.2% | +0.6 | 85% | ❌ 63 pts to go |
| P05 | 422 | 6.4% | 6.4% | +0.9 | 50% | ❌ 44 pts to go |
| P06M | 22259 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 59840 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 280 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 831 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30624 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 275 | 73.1% | 73.1% | -1.2 | 95% | ❌ 22 pts to go |
| P10 | 2126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1813 | 2.6% | 2.6% | -1.7 | 50% | ❌ 47 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 152067 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 229 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 627 | 8.1% | 8.1% | -0.4 | 50% | ❌ 42 pts to go |
| P02 | 468 | 6.2% | 6.2% | +0.0 | 50% | ❌ 44 pts to go |
| P03 | 266 | 2.6% | 2.6% | +0.7 | 30% | ❌ 27 pts to go |
| P04 | 3573 | 0.6% | 0.6% | +0.1 | 30% | ❌ 29 pts to go |
| P05 | 422 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 22259 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 59840 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 280 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 831 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30624 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 275 | 0.4% | 0.4% | +0.1 | n/a | no target |
| P10 | 2126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1813 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 152067 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 229 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 627 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 468 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 266 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3573 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 422 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 22259 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 59840 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 280 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 831 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 30624 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 275 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2126 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1813 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 152067 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 6.4% | 6.4% | -5.2 | 70% | ❌ 64 pts to go |
| P01T | 229 | 60.3% | 60.3% | +9.8 | 60% | ✅ met |
| P01_GOLD | 627 | 74.8% | 74.8% | +0.0 | 90% | ❌ 15 pts to go |
| P02 | 468 | 54.3% | 54.3% | +0.7 | 85% | ❌ 31 pts to go |
| P03 | 266 | 66.9% | 66.9% | -2.7 | 90% | ❌ 23 pts to go |
| P04 | 3573 | 38.2% | 38.2% | +3.2 | 75% | ❌ 37 pts to go |
| P05 | 422 | 54.7% | 54.7% | +0.0 | 50% | ✅ met |
| P06M | 22259 | 2.9% | 2.9% | -0.3 | n/a | no target |
| P06T | 59840 | 64.5% | 64.5% | +17.2 | n/a | no target |
| P06 | 280 | 42.1% | 42.1% | -1.9 | 40% | ✅ met |
| P07 | 831 | 32.1% | 32.1% | -0.9 | 50% | ❌ 18 pts to go |
| P08 | 30624 | 30.6% | 30.6% | +0.1 | 50% | ❌ 19 pts to go |
| P09 | 275 | 56.7% | 56.7% | -1.6 | 80% | ❌ 23 pts to go |
| P10 | 2126 | 38.8% | 38.8% | +4.3 | 40% | 🟡 1 pts to go |
| P11 | 1813 | 54.6% | 54.6% | +7.7 | 60% | 🟡 5 pts to go |
| P12 | 11 | 45.5% | 45.5% | -14.5 | 85% | ❌ 40 pts to go |
| P13 | 152067 | 44.8% | 44.8% | +13.1 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 46.6% | 46.6% | -13.1 | n/a | no target |
| P01T | 229 | 59.8% | 59.8% | +8.8 | n/a | no target |
| P01_GOLD | 627 | 72.9% | 72.9% | +0.2 | 95% | ❌ 22 pts to go |
| P02 | 468 | 74.6% | 74.6% | +0.8 | 95% | ❌ 20 pts to go |
| P03 | 266 | 69.5% | 69.5% | -2.4 | 95% | ❌ 26 pts to go |
| P04 | 3573 | 53.1% | 53.1% | +3.9 | 95% | ❌ 42 pts to go |
| P05 | 422 | 58.1% | 58.1% | -0.2 | 70% | ❌ 12 pts to go |
| P06M | 22259 | 41.3% | 41.3% | -4.7 | n/a | no target |
| P06T | 59840 | 67.5% | 67.5% | +11.3 | n/a | no target |
| P06 | 280 | 38.2% | 38.2% | -2.8 | 80% | ❌ 42 pts to go |
| P07 | 831 | 31.0% | 31.0% | -0.9 | 70% | ❌ 39 pts to go |
| P08 | 30624 | 29.7% | 29.7% | -0.6 | 70% | ❌ 40 pts to go |
| P09 | 275 | 86.2% | 86.2% | -0.4 | 100% | ❌ 14 pts to go |
| P10 | 2126 | 39.2% | 39.2% | +3.7 | 70% | ❌ 31 pts to go |
| P11 | 1813 | 58.6% | 58.6% | +6.1 | 75% | ❌ 16 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 152067 | 40.2% | 40.2% | +13.3 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 22.1% | 22.1% | +5.0 | n/a | no target |
| P01T | 229 | 65.5% | 65.5% | +11.9 | n/a | no target |
| P01_GOLD | 627 | 48.8% | 48.8% | -1.0 | 60% | ❌ 11 pts to go |
| P02 | 468 | 55.8% | 55.8% | -0.4 | 60% | 🟡 4 pts to go |
| P03 | 266 | 52.3% | 52.3% | -2.8 | 60% | 🟡 8 pts to go |
| P04 | 3573 | 42.6% | 42.6% | +0.5 | 55% | ❌ 12 pts to go |
| P05 | 422 | 22.7% | 22.7% | -1.9 | 50% | ❌ 27 pts to go |
| P06M | 22259 | 9.5% | 9.5% | +2.7 | n/a | no target |
| P06T | 59840 | 67.9% | 67.9% | +17.0 | n/a | no target |
| P06 | 280 | 48.6% | 48.6% | +1.0 | n/a | no target |
| P07 | 831 | 39.6% | 39.6% | -1.3 | 55% | ❌ 15 pts to go |
| P08 | 30624 | 33.0% | 33.0% | -3.2 | 50% | ❌ 17 pts to go |
| P09 | 275 | 72.0% | 72.0% | -0.3 | 70% | ✅ met |
| P10 | 2126 | 48.1% | 48.1% | +1.3 | 55% | 🟡 7 pts to go |
| P11 | 1813 | 59.2% | 59.2% | +7.0 | 50% | ✅ met |
| P12 | 11 | 90.9% | 90.9% | +4.2 | n/a | no target |
| P13 | 152067 | 3.2% | 3.2% | -0.2 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 33.3% | 33.3% | -17.1 | n/a | no target |
| P01T | 229 | 79.5% | 79.5% | +5.0 | n/a | no target |
| P01_GOLD | 627 | 50.4% | 50.4% | -0.1 | 70% | ❌ 20 pts to go |
| P02 | 468 | 56.8% | 56.8% | -1.4 | 70% | ❌ 13 pts to go |
| P03 | 266 | 50.4% | 50.4% | -0.9 | 70% | ❌ 20 pts to go |
| P04 | 3573 | 54.9% | 54.9% | +0.8 | 65% | ❌ 10 pts to go |
| P05 | 422 | 29.1% | 29.1% | +0.7 | 60% | ❌ 31 pts to go |
| P06M | 22259 | 27.4% | 27.4% | -9.2 | n/a | no target |
| P06T | 59840 | 82.7% | 82.7% | +2.7 | n/a | no target |
| P06 | 280 | 69.3% | 69.3% | +0.4 | 40% | ✅ met |
| P07 | 831 | 65.0% | 65.0% | +0.1 | 85% | ❌ 20 pts to go |
| P08 | 30624 | 64.0% | 64.0% | -1.3 | 85% | ❌ 21 pts to go |
| P09 | 275 | 56.4% | 56.4% | -2.9 | 85% | ❌ 29 pts to go |
| P10 | 2126 | 66.1% | 66.1% | +2.6 | 85% | ❌ 19 pts to go |
| P11 | 1813 | 68.1% | 68.1% | +6.2 | 75% | 🟡 7 pts to go |
| P12 | 11 | 36.4% | 36.4% | +9.7 | n/a | no target |
| P13 | 152067 | 91.8% | 91.8% | +0.6 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 37.8% | 37.8% | -18.8 | n/a | no target |
| P01T | 229 | 98.3% | 98.3% | +0.9 | n/a | no target |
| P01_GOLD | 627 | 78.6% | 78.6% | -1.0 | 90% | ❌ 11 pts to go |
| P02 | 468 | 81.8% | 81.8% | -2.1 | 90% | 🟡 8 pts to go |
| P03 | 266 | 85.3% | 85.3% | -2.5 | 90% | 🟡 5 pts to go |
| P04 | 3573 | 82.8% | 82.8% | -1.6 | 85% | 🟡 2 pts to go |
| P05 | 422 | 44.5% | 44.5% | -0.3 | 70% | ❌ 26 pts to go |
| P06M | 22259 | 33.0% | 33.0% | -10.6 | n/a | no target |
| P06T | 59840 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 280 | 99.3% | 99.3% | +0.0 | 50% | ✅ met |
| P07 | 831 | 99.9% | 99.9% | +0.0 | 100% | 🟡 0 pts to go |
| P08 | 30624 | 99.9% | 99.9% | +0.1 | 100% | 🟡 0 pts to go |
| P09 | 275 | 77.8% | 77.8% | -2.0 | 100% | ❌ 22 pts to go |
| P10 | 2126 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1813 | 98.0% | 98.0% | +0.7 | 100% | 🟡 2 pts to go |
| P12 | 11 | 54.5% | 54.5% | +1.2 | n/a | no target |
| P13 | 152067 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 16.1% | 16.1% | +0.6 | n/a | no target |
| P01T | 229 | 59.8% | 59.8% | -5.3 | n/a | no target |
| P01_GOLD | 627 | 43.4% | 43.4% | -0.1 | 70% | ❌ 27 pts to go |
| P02 | 468 | 47.2% | 47.2% | -1.5 | 75% | ❌ 28 pts to go |
| P03 | 266 | 44.7% | 44.7% | +1.4 | 75% | ❌ 30 pts to go |
| P04 | 3573 | 38.7% | 38.7% | +0.0 | 70% | ❌ 31 pts to go |
| P05 | 422 | 21.3% | 21.3% | -0.7 | 55% | ❌ 34 pts to go |
| P06M | 22259 | 5.9% | 5.9% | +1.1 | n/a | no target |
| P06T | 59840 | 47.4% | 47.4% | -14.7 | n/a | no target |
| P06 | 280 | 51.1% | 51.1% | +4.2 | n/a | no target |
| P07 | 831 | 52.7% | 52.7% | +2.7 | 70% | ❌ 17 pts to go |
| P08 | 30624 | 54.8% | 54.8% | +0.0 | 75% | ❌ 20 pts to go |
| P09 | 275 | 46.9% | 46.9% | -2.3 | 85% | ❌ 38 pts to go |
| P10 | 2126 | 44.4% | 44.4% | +0.8 | 80% | ❌ 36 pts to go |
| P11 | 1813 | 53.3% | 53.3% | -1.0 | 70% | ❌ 17 pts to go |
| P12 | 11 | 27.3% | 27.3% | -12.7 | n/a | no target |
| P13 | 152067 | 5.5% | 5.5% | +0.3 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 37.8% | 37.8% | -18.8 | n/a | no target |
| P01T | 229 | 96.5% | 96.5% | +1.7 | n/a | no target |
| P01_GOLD | 627 | 72.9% | 72.9% | -0.9 | 90% | ❌ 17 pts to go |
| P02 | 468 | 76.7% | 76.7% | -2.3 | 90% | ❌ 13 pts to go |
| P03 | 266 | 82.0% | 82.0% | -1.3 | 90% | 🟡 8 pts to go |
| P04 | 3573 | 77.7% | 77.7% | +1.3 | 85% | 🟡 7 pts to go |
| P05 | 422 | 42.9% | 42.9% | -0.2 | 75% | ❌ 32 pts to go |
| P06M | 22259 | 32.9% | 32.9% | -10.4 | n/a | no target |
| P06T | 59840 | 98.3% | 98.3% | +1.6 | n/a | no target |
| P06 | 280 | 90.0% | 90.0% | -0.5 | n/a | no target |
| P07 | 831 | 91.7% | 91.7% | -0.8 | 100% | 🟡 8 pts to go |
| P08 | 30624 | 87.3% | 87.3% | -3.5 | 100% | ❌ 13 pts to go |
| P09 | 275 | 66.5% | 66.5% | +0.4 | n/a | no target |
| P10 | 2126 | 90.3% | 90.3% | +3.5 | 100% | 🟡 10 pts to go |
| P11 | 1813 | 90.2% | 90.2% | +2.5 | n/a | no target |
| P12 | 11 | 54.5% | 54.5% | +7.8 | n/a | no target |
| P13 | 152067 | 69.8% | 69.8% | +4.6 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 36.9% | 36.9% | -9.6 | n/a | no target · QC vendors: 48 rows, 100.0% filled |
| P01T | 229 | 19.7% | 19.7% | +10.3 | n/a | no target · QC vendors: 33 rows, 87.9% filled |
| P01_GOLD | 627 | 43.5% | 43.5% | -0.3 | 95% | ❌ 52 pts to go · QC vendors: 50 rows, 98.0% filled |
| P02 | 468 | 56.0% | 56.0% | +0.4 | 95% | ❌ 39 pts to go · QC vendors: 111 rows, 100.0% filled |
| P03 | 266 | 42.9% | 42.9% | -3.1 | 95% | ❌ 52 pts to go · QC vendors: 19 rows, 100.0% filled |
| P04 | 3573 | 32.4% | 32.4% | +0.2 | 95% | ❌ 63 pts to go · QC vendors: 598 rows, 98.0% filled |
| P05 | 422 | 14.0% | 14.0% | +0.0 | n/a | no target · QC vendors: 35 rows, 100.0% filled |
| P06M | 22259 | 37.5% | 37.5% | -5.3 | n/a | no target · QC vendors: 6611 rows, 99.9% filled |
| P06T | 59840 | 30.6% | 30.6% | +25.3 | n/a | no target · QC vendors: 18604 rows, 95.7% filled |
| P06 | 280 | 7.1% | 7.1% | -1.3 | n/a | no target · QC vendors: 12 rows, 66.7% filled |
| P07 | 831 | 6.9% | 6.9% | +0.6 | n/a | no target · QC vendors: 47 rows, 78.7% filled |
| P08 | 30624 | 7.0% | 7.0% | +0.4 | n/a | no target · QC vendors: 1794 rows, 95.0% filled |
| P09 | 275 | 73.5% | 73.5% | -3.4 | 95% | ❌ 22 pts to go · QC vendors: 99 rows, 100.0% filled |
| P10 | 2126 | 15.7% | 15.7% | +0.1 | n/a | no target · QC vendors: 202 rows, 92.6% filled |
| P11 | 1813 | 19.6% | 19.6% | +4.8 | n/a | no target · QC vendors: 300 rows, 94.7% filled |
| P12 | 11 | 81.8% | 81.8% | +8.5 | n/a | no target · QC vendors: 2 rows, 100.0% filled |
| P13 | 152067 | 22.2% | 22.2% | -4.0 | n/a | no target · QC vendors: 33783 rows, 100.0% filled |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 46.2% | 46.2% | -12.7 | n/a | no target · vendors with a registry record: 115 rows, 100.0% filled |
| P01T | 229 | 59.8% | 59.8% | +8.8 | n/a | no target · vendors with a registry record: 137 rows, 100.0% filled |
| P01_GOLD | 627 | 80.9% | 80.9% | -0.6 | 100% | ❌ 19 pts to go · vendors with a registry record: 507 rows, 100.0% filled |
| P02 | 468 | 78.4% | 78.4% | +0.9 | 100% | ❌ 22 pts to go · vendors with a registry record: 367 rows, 100.0% filled |
| P03 | 266 | 78.2% | 78.2% | -2.8 | 100% | ❌ 22 pts to go · vendors with a registry record: 208 rows, 100.0% filled |
| P04 | 3573 | 54.0% | 54.0% | +4.3 | 100% | ❌ 46 pts to go · vendors with a registry record: 1929 rows, 100.0% filled |
| P05 | 422 | 62.8% | 62.8% | -0.5 | n/a | no target · vendors with a registry record: 265 rows, 100.0% filled |
| P06M | 22259 | 41.2% | 41.2% | -4.7 | n/a | no target · vendors with a registry record: 9180 rows, 100.0% filled |
| P06T | 59840 | 67.6% | 67.6% | +11.4 | n/a | no target · vendors with a registry record: 40433 rows, 100.0% filled |
| P06 | 280 | 39.3% | 39.3% | -2.1 | n/a | no target · vendors with a registry record: 110 rows, 100.0% filled |
| P07 | 831 | 31.8% | 31.8% | -0.5 | n/a | no target · vendors with a registry record: 264 rows, 100.0% filled |
| P08 | 30624 | 30.0% | 30.0% | -0.4 | n/a | no target · vendors with a registry record: 9180 rows, 100.0% filled |
| P09 | 275 | 89.5% | 89.5% | -1.1 | n/a | no target · vendors with a registry record: 246 rows, 100.0% filled |
| P10 | 2126 | 40.1% | 40.1% | +3.9 | n/a | no target · vendors with a registry record: 853 rows, 100.0% filled |
| P11 | 1813 | 59.3% | 59.3% | +5.7 | n/a | no target · vendors with a registry record: 1076 rows, 100.0% filled |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 11 rows, 100.0% filled |
| P13 | 152067 | 40.2% | 40.2% | +13.3 | n/a | no target · vendors with a registry record: 61165 rows, 100.0% filled |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 96.4% | 96.4% | +2.6 | 90% | ✅ met |
| P01T | 229 | 70.7% | 70.7% | -1.7 | 90% | ❌ 19 pts to go |
| P01_GOLD | 627 | 87.4% | 87.4% | -0.3 | 95% | 🟡 8 pts to go |
| P02 | 468 | 88.2% | 88.2% | +0.4 | 95% | 🟡 7 pts to go |
| P03 | 266 | 83.1% | 83.1% | -1.3 | 85% | 🟡 2 pts to go |
| P04 | 3573 | 64.5% | 64.5% | +1.5 | 90% | ❌ 26 pts to go |
| P05 | 422 | 78.0% | 78.0% | -1.1 | 75% | ✅ met |
| P06M | 22259 | 93.8% | 93.8% | +2.2 | n/a | no target |
| P06T | 59840 | 36.9% | 36.9% | -0.4 | n/a | no target |
| P06 | 280 | 71.1% | 71.1% | -2.5 | 80% | 🟡 9 pts to go |
| P07 | 831 | 58.2% | 58.4% | -1.6 | 80% | ❌ 22 pts to go |
| P08 | 30624 | 51.9% | 51.9% | -2.5 | 75% | ❌ 23 pts to go |
| P09 | 275 | 75.6% | 75.6% | -1.3 | 95% | ❌ 19 pts to go |
| P10 | 2126 | 46.8% | 46.9% | +0.1 | 70% | ❌ 23 pts to go |
| P11 | 1813 | 31.8% | 31.8% | +0.5 | 65% | ❌ 33 pts to go |
| P12 | 11 | 72.7% | 72.7% | -7.3 | 80% | 🟡 7 pts to go |
| P13 | 152067 | 45.6% | 45.6% | -1.9 | 60% | ❌ 14 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 18.5% | 18.5% | -1.7 | 50% | ❌ 32 pts to go |
| P01T | 229 | 16.2% | 16.2% | +0.1 | n/a | no target |
| P01_GOLD | 627 | 19.8% | 19.8% | +0.3 | 40% | ❌ 20 pts to go |
| P02 | 468 | 19.9% | 19.9% | +0.8 | 40% | ❌ 20 pts to go |
| P03 | 266 | 20.3% | 20.3% | -1.0 | 40% | ❌ 20 pts to go |
| P04 | 3573 | 16.3% | 16.3% | +1.1 | 40% | ❌ 24 pts to go |
| P05 | 422 | 20.9% | 20.9% | +3.4 | 25% | 🟡 4 pts to go |
| P06M | 22259 | 20.4% | 20.4% | +8.8 | n/a | no target |
| P06T | 59840 | 7.5% | 7.5% | +0.6 | n/a | no target |
| P06 | 280 | 17.5% | 17.5% | +4.7 | 35% | ❌ 18 pts to go |
| P07 | 831 | 19.1% | 19.1% | +5.0 | 35% | ❌ 16 pts to go |
| P08 | 30624 | 17.7% | 17.7% | +2.3 | 35% | ❌ 17 pts to go |
| P09 | 275 | 16.7% | 16.7% | +0.4 | n/a | no target |
| P10 | 2126 | 7.1% | 7.1% | +0.4 | 30% | ❌ 23 pts to go |
| P11 | 1813 | 6.5% | 6.5% | -0.9 | n/a | no target |
| P12 | 11 | 18.2% | 18.2% | +11.5 | n/a | no target |
| P13 | 152067 | 12.5% | 12.5% | +0.2 | 30% | ❌ 18 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 229 | 85.2% | 85.2% | +0.8 | 100% | ❌ 15 pts to go |
| P01_GOLD | 627 | 91.1% | 91.1% | +0.4 | 100% | 🟡 9 pts to go |
| P02 | 468 | 96.6% | 96.6% | +1.1 | 100% | 🟡 3 pts to go |
| P03 | 266 | 89.5% | 89.5% | +0.1 | 100% | ❌ 10 pts to go |
| P04 | 3573 | 72.5% | 72.5% | +1.1 | 100% | ❌ 28 pts to go |
| P05 | 422 | 90.0% | 90.0% | +0.7 | 100% | 🟡 10 pts to go |
| P06M | 22259 | 99.4% | 99.4% | +0.2 | n/a | no target |
| P06T | 59840 | 58.7% | 58.7% | -0.6 | n/a | no target |
| P06 | 280 | 82.1% | 82.1% | +3.3 | 95% | ❌ 13 pts to go |
| P07 | 831 | 85.4% | 85.4% | +4.2 | 95% | 🟡 10 pts to go |
| P08 | 30624 | 84.5% | 84.5% | +6.2 | 95% | ❌ 10 pts to go |
| P09 | 275 | 96.4% | 96.4% | +0.3 | 100% | 🟡 4 pts to go |
| P10 | 2126 | 54.6% | 54.7% | +0.2 | 95% | ❌ 40 pts to go |
| P11 | 1813 | 60.9% | 60.9% | +11.5 | 80% | ❌ 19 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 152067 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 71.1% | 71.1% | -14.9 | n/a | no target |
| P01T | 229 | 74.2% | 74.2% | +6.0 | n/a | no target |
| P01_GOLD | 627 | 73.2% | 73.2% | +0.2 | 90% | ❌ 17 pts to go |
| P02 | 468 | 78.4% | 78.4% | +0.5 | 95% | ❌ 17 pts to go |
| P03 | 266 | 74.1% | 74.1% | -0.8 | 95% | ❌ 21 pts to go |
| P04 | 3573 | 69.5% | 69.5% | +0.6 | 95% | ❌ 26 pts to go |
| P05 | 422 | 72.5% | 72.5% | -1.0 | 90% | ❌ 18 pts to go |
| P06M | 22259 | 76.7% | 76.7% | -10.2 | n/a | no target |
| P06T | 59840 | 58.6% | 58.6% | +1.4 | n/a | no target |
| P06 | 280 | 65.4% | 65.4% | -3.1 | 95% | ❌ 30 pts to go |
| P07 | 831 | 59.7% | 59.7% | -5.1 | 90% | ❌ 30 pts to go |
| P08 | 30624 | 58.6% | 58.6% | -9.2 | 95% | ❌ 36 pts to go |
| P09 | 275 | 85.8% | 85.8% | -1.2 | 100% | ❌ 14 pts to go |
| P10 | 2126 | 53.8% | 53.8% | -1.5 | 95% | ❌ 41 pts to go |
| P11 | 1813 | 30.7% | 30.7% | +1.8 | 75% | ❌ 44 pts to go |
| P12 | 11 | 81.8% | 81.8% | -11.5 | n/a | no target |
| P13 | 152067 | 67.9% | 67.9% | -2.9 | 95% | ❌ 27 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 83.5% | 83.5% | -4.1 | n/a | no target |
| P01T | 229 | 91.7% | 91.7% | +8.4 | 95% | 🟡 3 pts to go |
| P01_GOLD | 627 | 85.0% | 85.0% | +0.2 | 90% | 🟡 5 pts to go |
| P02 | 468 | 91.0% | 91.0% | +0.4 | 95% | 🟡 4 pts to go |
| P03 | 266 | 83.8% | 83.8% | -1.8 | 95% | ❌ 11 pts to go |
| P04 | 3573 | 91.6% | 91.6% | +2.4 | 90% | ✅ met |
| P05 | 422 | 92.4% | 92.4% | -0.7 | 95% | 🟡 3 pts to go |
| P06M | 22259 | 85.3% | 85.3% | -7.9 | n/a | no target |
| P06T | 59840 | 84.6% | 84.6% | +9.7 | n/a | no target |
| P06 | 280 | 85.4% | 85.4% | -6.9 | 100% | ❌ 15 pts to go |
| P07 | 831 | 83.6% | 83.6% | -8.6 | 100% | ❌ 16 pts to go |
| P08 | 30624 | 77.8% | 77.8% | -14.5 | 100% | ❌ 22 pts to go |
| P09 | 275 | 74.2% | 74.2% | +1.2 | n/a | no target |
| P10 | 2126 | 94.4% | 94.4% | +3.1 | 100% | 🟡 6 pts to go |
| P11 | 1813 | 51.1% | 51.1% | +9.2 | 80% | ❌ 29 pts to go |
| P12 | 11 | 90.9% | 90.9% | -9.1 | n/a | no target |
| P13 | 152067 | 80.8% | 80.8% | -2.9 | 95% | ❌ 14 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 3.2% | 3.2% | +0.1 | n/a | no target |
| P01T | 229 | 8.7% | 8.7% | -0.7 | n/a | no target |
| P01_GOLD | 627 | 14.0% | 14.0% | -0.2 | 25% | ❌ 11 pts to go |
| P02 | 468 | 24.8% | 24.8% | -0.5 | 40% | ❌ 15 pts to go |
| P03 | 266 | 9.0% | 9.0% | -0.1 | 20% | ❌ 11 pts to go |
| P04 | 3573 | 3.3% | 3.3% | -0.2 | 20% | ❌ 17 pts to go |
| P05 | 422 | 3.3% | 3.3% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 22259 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 59840 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P06 | 280 | 5.4% | 5.4% | +0.3 | n/a | no target |
| P07 | 831 | 7.9% | 7.9% | -0.6 | n/a | no target |
| P08 | 30624 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P09 | 275 | 7.6% | 7.6% | -0.2 | n/a | no target |
| P10 | 2126 | 0.8% | 0.8% | +0.0 | n/a | no target |
| P11 | 1813 | 0.7% | 0.7% | -0.3 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | -6.7 | n/a | no target |
| P13 | 152067 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 16.1% | 16.1% | -2.5 | n/a | no target |
| P01T | 229 | 19.2% | 19.2% | -3.2 | 70% | ❌ 51 pts to go |
| P01_GOLD | 627 | 42.1% | 42.1% | -1.4 | 80% | ❌ 38 pts to go |
| P02 | 468 | 57.3% | 57.3% | +0.0 | 90% | ❌ 33 pts to go |
| P03 | 266 | 19.2% | 19.2% | +0.6 | 60% | ❌ 41 pts to go |
| P04 | 3573 | 20.2% | 20.2% | -1.4 | 85% | ❌ 65 pts to go |
| P05 | 422 | 11.1% | 11.1% | -0.5 | 50% | ❌ 39 pts to go |
| P06M | 22259 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06T | 59840 | 0.5% | 0.5% | -0.2 | n/a | no target |
| P06 | 280 | 13.2% | 13.2% | -2.2 | n/a | no target |
| P07 | 831 | 9.1% | 9.1% | -1.4 | n/a | no target |
| P08 | 30624 | 0.5% | 0.5% | -0.1 | n/a | no target |
| P09 | 275 | 72.0% | 72.0% | -5.9 | 95% | ❌ 23 pts to go |
| P10 | 2126 | 1.6% | 1.6% | -0.1 | n/a | no target |
| P11 | 1813 | 13.0% | 13.0% | -3.7 | n/a | no target |
| P12 | 11 | 27.3% | 27.3% | +0.6 | n/a | no target |
| P13 | 152067 | 0.3% | 0.3% | -0.2 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 5.6% | 5.6% | -0.6 | n/a | no target |
| P01T | 229 | 9.2% | 9.2% | -1.2 | n/a | no target |
| P01_GOLD | 627 | 33.8% | 33.8% | -0.2 | 70% | ❌ 36 pts to go |
| P02 | 468 | 38.7% | 38.7% | -0.4 | 75% | ❌ 36 pts to go |
| P03 | 266 | 19.2% | 19.2% | +0.6 | 55% | ❌ 36 pts to go |
| P04 | 3573 | 20.2% | 20.2% | -1.4 | 75% | ❌ 55 pts to go |
| P05 | 422 | 10.2% | 10.2% | -0.5 | 50% | ❌ 40 pts to go |
| P06M | 22259 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06T | 59840 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 280 | 5.7% | 5.7% | -0.2 | n/a | no target |
| P07 | 831 | 4.6% | 4.6% | -0.6 | n/a | no target |
| P08 | 30624 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 275 | 68.7% | 68.7% | -6.5 | 95% | ❌ 26 pts to go |
| P10 | 2126 | 0.8% | 0.8% | -0.1 | n/a | no target |
| P11 | 1813 | 12.8% | 12.8% | -3.6 | n/a | no target |
| P12 | 11 | 18.2% | 18.2% | -1.8 | n/a | no target |
| P13 | 152067 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 7.6% | 7.6% | -0.2 | n/a | no target |
| P01T | 229 | 8.7% | 8.7% | +0.4 | n/a | no target |
| P01_GOLD | 627 | 57.1% | 57.3% | -0.9 | 80% | ❌ 23 pts to go |
| P02 | 468 | 45.3% | 45.5% | -0.4 | 75% | ❌ 30 pts to go |
| P03 | 266 | 36.1% | 36.1% | -1.2 | 70% | ❌ 34 pts to go |
| P04 | 3573 | 19.9% | 20.3% | -1.2 | 70% | ❌ 50 pts to go |
| P05 | 422 | 14.0% | 14.0% | -0.2 | 50% | ❌ 36 pts to go |
| P06M | 22259 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 59840 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P06 | 280 | 13.2% | 13.2% | -3.3 | n/a | no target |
| P07 | 831 | 1.1% | 1.1% | -0.9 | n/a | no target |
| P08 | 30624 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P09 | 275 | 46.9% | 46.9% | +0.3 | 80% | ❌ 33 pts to go |
| P10 | 2126 | 1.1% | 1.2% | -0.1 | n/a | no target |
| P11 | 1813 | 4.5% | 4.5% | -2.3 | n/a | no target |
| P12 | 11 | 36.4% | 36.4% | -3.6 | n/a | no target |
| P13 | 152067 | 0.1% | 0.1% | -0.1 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 14.9% | 14.9% | -3.7 | n/a | no target |
| P01T | 229 | 19.2% | 19.2% | -2.2 | 60% | ❌ 41 pts to go |
| P01_GOLD | 627 | 62.2% | 62.2% | -1.2 | 70% | 🟡 8 pts to go |
| P02 | 468 | 39.5% | 39.5% | -0.2 | 50% | ❌ 10 pts to go |
| P03 | 266 | 47.7% | 47.7% | -0.6 | 55% | 🟡 7 pts to go |
| P04 | 3573 | 12.5% | 12.5% | +0.3 | 40% | ❌ 28 pts to go |
| P05 | 422 | 16.6% | 16.6% | -0.5 | 40% | ❌ 23 pts to go |
| P06M | 22259 | 2.8% | 2.8% | +0.6 | n/a | no target |
| P06T | 59840 | 1.5% | 1.5% | -0.2 | n/a | no target |
| P06 | 280 | 18.2% | 18.2% | -3.8 | n/a | no target |
| P07 | 831 | 4.9% | 4.9% | -1.7 | n/a | no target |
| P08 | 30624 | 2.1% | 2.1% | -0.8 | n/a | no target |
| P09 | 275 | 5.8% | 5.8% | -0.1 | n/a | no target |
| P10 | 2126 | 5.1% | 5.1% | +0.5 | n/a | no target |
| P11 | 1813 | 4.0% | 4.0% | -1.2 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | -6.7 | n/a | no target |
| P13 | 152067 | 0.7% | 0.7% | -0.3 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 21.7% | 21.7% | +0.0 | n/a | no target |
| P01T | 229 | 27.9% | 27.9% | -0.7 | 65% | ❌ 37 pts to go |
| P01_GOLD | 627 | 68.6% | 68.6% | -0.4 | 70% | 🟡 1 pts to go |
| P02 | 468 | 23.7% | 23.7% | -0.5 | 50% | ❌ 26 pts to go |
| P03 | 266 | 50.4% | 50.4% | -2.1 | 60% | 🟡 10 pts to go |
| P04 | 3573 | 5.6% | 5.6% | +0.2 | 40% | ❌ 34 pts to go |
| P05 | 422 | 19.9% | 19.9% | +0.2 | 45% | ❌ 25 pts to go |
| P06M | 22259 | 1.7% | 1.7% | +0.3 | n/a | no target |
| P06T | 59840 | 0.6% | 0.6% | -0.1 | n/a | no target |
| P06 | 280 | 29.3% | 29.3% | -5.1 | n/a | no target |
| P07 | 831 | 5.1% | 5.1% | -1.8 | n/a | no target |
| P08 | 30624 | 0.9% | 0.9% | -0.4 | n/a | no target |
| P09 | 275 | 10.9% | 10.9% | +1.1 | n/a | no target |
| P10 | 2126 | 3.3% | 3.3% | +0.2 | n/a | no target |
| P11 | 1813 | 3.6% | 3.6% | -1.5 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | -6.7 | n/a | no target |
| P13 | 152067 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 12.0% | 12.0% | -0.4 | n/a | no target |
| P01T | 229 | 12.7% | 12.7% | -0.8 | n/a | no target |
| P01_GOLD | 627 | 50.2% | 50.2% | +0.4 | 50% | ✅ met |
| P02 | 468 | 37.6% | 37.6% | +0.3 | n/a | no target |
| P03 | 266 | 50.8% | 50.8% | -1.3 | 60% | 🟡 9 pts to go |
| P04 | 3573 | 12.8% | 12.8% | +0.9 | n/a | no target |
| P05 | 422 | 15.2% | 15.2% | +0.0 | n/a | no target |
| P06M | 22259 | 0.8% | 0.8% | +0.3 | n/a | no target |
| P06T | 59840 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 280 | 20.4% | 20.4% | -5.2 | n/a | no target |
| P07 | 831 | 5.7% | 5.7% | -2.6 | n/a | no target |
| P08 | 30624 | 0.4% | 0.4% | -0.2 | n/a | no target |
| P09 | 275 | 20.7% | 20.7% | +3.1 | n/a | no target |
| P10 | 2126 | 2.5% | 2.5% | +0.1 | n/a | no target |
| P11 | 1813 | 2.7% | 2.7% | -2.0 | n/a | no target |
| P12 | 11 | 18.2% | 18.2% | +4.9 | n/a | no target |
| P13 | 152067 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 8.8% | 8.8% | -2.8 | 15% | 🟡 6 pts to go |
| P01T | 229 | 12.7% | 12.7% | +0.2 | 15% | 🟡 2 pts to go |
| P01_GOLD | 627 | 35.1% | 35.1% | -0.2 | 40% | 🟡 5 pts to go |
| P02 | 468 | 12.2% | 12.4% | -0.7 | 25% | ❌ 13 pts to go |
| P03 | 266 | 16.5% | 16.5% | -1.0 | 25% | 🟡 8 pts to go |
| P04 | 3573 | 2.7% | 2.7% | +0.0 | 15% | ❌ 12 pts to go |
| P05 | 422 | 6.6% | 6.6% | +0.0 | 15% | 🟡 8 pts to go |
| P06M | 22259 | 0.8% | 0.8% | -0.1 | 15% | ❌ 14 pts to go |
| P06T | 59840 | 0.7% | 0.7% | +0.2 | 15% | ❌ 14 pts to go |
| P06 | 280 | 9.3% | 9.3% | -1.3 | 15% | 🟡 6 pts to go |
| P07 | 831 | 3.4% | 3.4% | -0.9 | 15% | ❌ 12 pts to go |
| P08 | 30624 | 0.5% | 0.5% | -0.1 | 15% | ❌ 14 pts to go |
| P09 | 275 | 1.1% | 1.1% | +0.1 | 15% | ❌ 14 pts to go |
| P10 | 2126 | 1.4% | 1.4% | +0.1 | 15% | ❌ 14 pts to go |
| P11 | 1813 | 1.2% | 1.2% | -0.3 | 15% | ❌ 14 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 152067 | 0.6% | 0.6% | -0.1 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 5.6% | 5.6% | +0.2 | 15% | 🟡 9 pts to go |
| P01T | 229 | 10.9% | 10.9% | -0.6 | 25% | ❌ 14 pts to go |
| P01_GOLD | 627 | 28.9% | 28.9% | -0.3 | 25% | ✅ met |
| P02 | 468 | 25.4% | 25.4% | +0.1 | 15% | ✅ met |
| P03 | 266 | 21.8% | 21.8% | -0.3 | 15% | ✅ met |
| P04 | 3573 | 4.0% | 4.0% | +0.0 | 15% | ❌ 11 pts to go |
| P05 | 422 | 11.4% | 11.4% | +0.3 | 15% | 🟡 4 pts to go |
| P06M | 22259 | 0.6% | 0.6% | +0.1 | 15% | ❌ 14 pts to go |
| P06T | 59840 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 280 | 7.1% | 7.1% | -1.3 | 15% | 🟡 8 pts to go |
| P07 | 831 | 1.8% | 1.8% | -1.1 | 15% | ❌ 13 pts to go |
| P08 | 30624 | 0.3% | 0.3% | -0.2 | 15% | ❌ 15 pts to go |
| P09 | 275 | 1.5% | 1.5% | +0.5 | 15% | ❌ 14 pts to go |
| P10 | 2126 | 1.6% | 1.6% | +0.0 | 15% | ❌ 13 pts to go |
| P11 | 1813 | 1.8% | 1.8% | -0.9 | 15% | ❌ 13 pts to go |
| P12 | 11 | 0.0% | 0.0% | -20.0 | 15% | ❌ 15 pts to go |
| P13 | 152067 | 0.1% | 0.1% | -0.1 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 1.6% | 1.6% | -0.7 | 20% | ❌ 18 pts to go |
| P01T | 229 | 3.1% | 3.1% | -1.1 | 20% | ❌ 17 pts to go |
| P01_GOLD | 627 | 4.3% | 4.3% | -0.2 | 20% | ❌ 16 pts to go |
| P02 | 468 | 1.5% | 1.5% | +0.0 | 20% | ❌ 18 pts to go |
| P03 | 266 | 1.9% | 1.9% | +0.4 | 20% | ❌ 18 pts to go |
| P04 | 3573 | 0.7% | 0.7% | +0.1 | 20% | ❌ 19 pts to go |
| P05 | 422 | 0.9% | 0.9% | -0.3 | 20% | ❌ 19 pts to go |
| P06M | 22259 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 59840 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 280 | 1.4% | 1.4% | -0.1 | 20% | ❌ 19 pts to go |
| P07 | 831 | 0.2% | 0.2% | -0.2 | 20% | ❌ 20 pts to go |
| P08 | 30624 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P09 | 275 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2126 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 1813 | 0.1% | 0.1% | -0.2 | 20% | ❌ 20 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 152067 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 1.6% | 1.6% | +0.0 | 15% | ❌ 13 pts to go |
| P01T | 229 | 3.1% | 3.1% | +0.0 | 15% | ❌ 12 pts to go |
| P01_GOLD | 627 | 10.5% | 10.5% | +0.1 | 15% | 🟡 4 pts to go |
| P02 | 468 | 11.5% | 11.5% | -0.5 | 15% | 🟡 4 pts to go |
| P03 | 266 | 20.7% | 20.7% | +0.5 | 15% | ✅ met |
| P04 | 3573 | 2.4% | 2.4% | +0.1 | 15% | ❌ 13 pts to go |
| P05 | 422 | 2.8% | 2.8% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 22259 | 0.4% | 0.4% | +0.1 | 15% | ❌ 15 pts to go |
| P06T | 59840 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 280 | 3.9% | 3.9% | -1.2 | 15% | ❌ 11 pts to go |
| P07 | 831 | 1.2% | 1.2% | -0.4 | 15% | ❌ 14 pts to go |
| P08 | 30624 | 0.3% | 0.3% | -0.2 | 15% | ❌ 15 pts to go |
| P09 | 275 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2126 | 1.1% | 1.1% | +0.1 | 15% | ❌ 14 pts to go |
| P11 | 1813 | 0.8% | 0.8% | -0.4 | 15% | ❌ 14 pts to go |
| P12 | 11 | 0.0% | 0.0% | -6.7 | 15% | ❌ 15 pts to go |
| P13 | 152067 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 12.4% | 12.4% | -1.6 | 20% | 🟡 8 pts to go |
| P01T | 229 | 13.5% | 13.5% | -0.6 | 40% | ❌ 26 pts to go |
| P01_GOLD | 627 | 46.6% | 46.6% | +0.4 | 40% | ✅ met |
| P02 | 468 | 43.2% | 43.2% | +0.3 | 20% | ✅ met |
| P03 | 266 | 48.5% | 48.5% | -0.5 | 35% | ✅ met |
| P04 | 3573 | 14.9% | 14.9% | +0.7 | 20% | 🟡 5 pts to go |
| P05 | 422 | 15.6% | 15.6% | +0.2 | 20% | 🟡 4 pts to go |
| P06M | 22259 | 1.0% | 1.0% | +0.2 | 20% | ❌ 19 pts to go |
| P06T | 59840 | 0.6% | 0.6% | -0.1 | 20% | ❌ 19 pts to go |
| P06 | 280 | 21.1% | 21.1% | -4.2 | 20% | ✅ met |
| P07 | 831 | 6.1% | 6.1% | -2.5 | 20% | ❌ 14 pts to go |
| P08 | 30624 | 0.8% | 0.8% | -0.2 | 20% | ❌ 19 pts to go |
| P09 | 275 | 21.1% | 21.1% | +2.9 | 20% | ✅ met |
| P10 | 2126 | 3.8% | 3.8% | +0.1 | 20% | ❌ 16 pts to go |
| P11 | 1813 | 3.2% | 3.2% | -1.6 | 20% | ❌ 17 pts to go |
| P12 | 11 | 9.1% | 9.1% | +2.4 | 20% | ❌ 11 pts to go |
| P13 | 152067 | 0.4% | 0.4% | -0.1 | 20% | ❌ 20 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 18.1% | 18.1% | -15.2 | n/a | no target |
| P01T | 229 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P01_GOLD | 627 | 71.6% | 71.6% | +2.1 | 95% | ❌ 23 pts to go |
| P02 | 468 | 66.2% | 66.2% | +3.3 | 95% | ❌ 29 pts to go |
| P03 | 266 | 57.9% | 57.9% | +4.7 | 90% | ❌ 32 pts to go |
| P04 | 3573 | 26.5% | 26.5% | +1.7 | 85% | ❌ 58 pts to go |
| P05 | 422 | 38.9% | 38.9% | +1.2 | 75% | ❌ 36 pts to go |
| P06M | 22259 | 28.1% | 28.1% | -8.0 | n/a | no target |
| P06T | 59840 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 280 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 831 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30624 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 275 | 89.1% | 89.1% | +0.8 | 100% | ❌ 11 pts to go |
| P10 | 2126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1813 | 3.8% | 3.8% | -2.2 | 60% | ❌ 56 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 152067 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 18.1% | 18.1% | -15.2 | n/a | no target |
| P01T | 229 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 627 | 73.5% | 73.5% | +0.7 | 100% | ❌ 26 pts to go |
| P02 | 468 | 68.2% | 68.2% | +1.9 | 100% | ❌ 32 pts to go |
| P03 | 266 | 60.5% | 60.5% | +1.6 | n/a | no target |
| P04 | 3573 | 27.0% | 27.0% | +1.5 | 95% | ❌ 68 pts to go |
| P05 | 422 | 34.6% | 34.6% | +1.2 | 80% | ❌ 45 pts to go |
| P06M | 22259 | 28.1% | 28.1% | -8.0 | n/a | no target |
| P06T | 59840 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 280 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 831 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30624 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 275 | 91.6% | 91.6% | +0.1 | 100% | 🟡 8 pts to go |
| P10 | 2126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1813 | 4.0% | 4.0% | -2.4 | n/a | no target |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 152067 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 84.3% | 84.3% | +4.5 | n/a | no target |
| P01T | 229 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P01_GOLD | 627 | 52.3% | 52.3% | +0.7 | 85% | ❌ 33 pts to go |
| P02 | 468 | 59.2% | 59.2% | +1.7 | 90% | ❌ 31 pts to go |
| P03 | 266 | 44.0% | 44.0% | +1.4 | 85% | ❌ 41 pts to go |
| P04 | 3573 | 29.1% | 29.1% | +1.2 | 90% | ❌ 61 pts to go |
| P05 | 422 | 32.9% | 32.9% | +0.2 | 75% | ❌ 42 pts to go |
| P06M | 22259 | 84.3% | 84.3% | -2.8 | n/a | no target |
| P06T | 59840 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 280 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 831 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30624 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 275 | 81.8% | 81.8% | -1.6 | 95% | ❌ 13 pts to go |
| P10 | 2126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1813 | 3.3% | 3.3% | -2.1 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 152067 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 65.9% | 65.9% | -12.4 | n/a | no target |
| P01T | 229 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P01_GOLD | 627 | 52.0% | 52.0% | +0.2 | 85% | ❌ 33 pts to go |
| P02 | 468 | 53.4% | 53.4% | +0.8 | 90% | ❌ 37 pts to go |
| P03 | 266 | 44.4% | 44.4% | +0.7 | 85% | ❌ 41 pts to go |
| P04 | 3573 | 24.6% | 24.6% | +0.8 | 90% | ❌ 65 pts to go |
| P05 | 422 | 42.7% | 42.7% | -0.7 | 75% | ❌ 32 pts to go |
| P06M | 22259 | 69.2% | 69.2% | -8.6 | n/a | no target |
| P06T | 59840 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 280 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 831 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30624 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 275 | 0.4% | 0.4% | +0.1 | 95% | ❌ 95 pts to go |
| P10 | 2126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1813 | 2.5% | 2.5% | -2.0 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 152067 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 95.2% | 95.2% | +5.3 | n/a | no target |
| P01T | 229 | 96.1% | 96.1% | +1.8 | n/a | no target |
| P01_GOLD | 627 | 85.5% | 85.6% | +0.2 | 100% | ❌ 14 pts to go |
| P02 | 468 | 77.6% | 77.6% | +1.2 | 100% | ❌ 22 pts to go |
| P03 | 266 | 92.5% | 92.5% | +1.2 | n/a | no target |
| P04 | 3573 | 50.6% | 50.6% | +1.8 | 95% | ❌ 44 pts to go |
| P05 | 422 | 77.3% | 77.3% | -0.2 | 95% | ❌ 18 pts to go |
| P06M | 22259 | 99.3% | 99.3% | +0.4 | n/a | no target |
| P06T | 59840 | 94.5% | 94.5% | +3.9 | n/a | no target |
| P06 | 280 | 20.4% | 20.4% | -2.7 | n/a | no target |
| P07 | 831 | 10.2% | 10.2% | -3.6 | n/a | no target |
| P08 | 30624 | 4.5% | 4.5% | -2.6 | n/a | no target |
| P09 | 275 | 98.2% | 98.2% | -0.5 | 100% | 🟡 2 pts to go |
| P10 | 2126 | 70.6% | 70.6% | -0.4 | n/a | no target |
| P11 | 1813 | 69.8% | 69.8% | +1.7 | n/a | no target |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 152067 | 99.6% | 99.6% | -0.1 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 95.2% | 95.2% | +5.3 | n/a | no target |
| P01T | 229 | 96.1% | 96.1% | +1.8 | n/a | no target |
| P01_GOLD | 627 | 88.7% | 88.8% | +0.2 | 100% | ❌ 11 pts to go |
| P02 | 468 | 78.8% | 78.8% | +1.3 | 100% | ❌ 21 pts to go |
| P03 | 266 | 93.2% | 93.2% | +1.2 | n/a | no target |
| P04 | 3573 | 54.0% | 54.0% | +2.1 | 95% | ❌ 41 pts to go |
| P05 | 422 | 89.3% | 89.3% | -0.3 | 70% | ✅ met |
| P06M | 22259 | 99.3% | 99.3% | +0.4 | n/a | no target |
| P06T | 59840 | 94.5% | 94.5% | +3.9 | n/a | no target |
| P06 | 280 | 20.4% | 20.4% | -2.7 | n/a | no target |
| P07 | 831 | 10.2% | 10.2% | -3.6 | n/a | no target |
| P08 | 30624 | 4.5% | 4.5% | -2.6 | n/a | no target |
| P09 | 275 | 98.2% | 98.2% | -0.5 | 100% | 🟡 2 pts to go |
| P10 | 2126 | 70.6% | 70.6% | -0.4 | n/a | no target |
| P11 | 1813 | 69.9% | 69.9% | +1.7 | n/a | no target |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 152067 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 229 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 627 | 16.9% | 16.9% | +0.1 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 367 rows, 28.9% filled |
| P02 | 468 | 10.7% | 10.7% | -0.5 | n/a | no target · rows from a source that publishes bids: 298 rows, 16.8% filled |
| P03 | 266 | 13.9% | 13.9% | +1.0 | n/a | no target · rows from a source that publishes bids: 143 rows, 25.9% filled |
| P04 | 3573 | 1.7% | 1.7% | +0.2 | n/a | no target · rows from a source that publishes bids: 881 rows, 6.9% filled |
| P05 | 422 | 2.6% | 2.6% | +0.0 | n/a | no target · rows from a source that publishes bids: 55 rows, 20.0% filled |
| P06M | 22259 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 59840 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 280 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 831 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 30624 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 275 | 4.4% | 4.4% | +0.2 | n/a | no target · rows from a source that publishes bids: 262 rows, 4.6% filled |
| P10 | 2126 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1813 | 0.4% | 0.4% | -0.5 | n/a | no target · rows from a source that publishes bids: 67 rows, 10.4% filled |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 11 rows, 0.0% filled |
| P13 | 152067 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 229 | 0.0% | 97.8% | +0.0 | n/a | no target |
| P01_GOLD | 627 | 53.4% | 82.3% | +0.2 | 90% | ❌ 37 pts to go |
| P02 | 468 | 53.4% | 87.0% | +1.0 | 90% | ❌ 37 pts to go |
| P03 | 266 | 45.9% | 79.7% | +1.4 | 90% | ❌ 44 pts to go |
| P04 | 3573 | 19.6% | 92.9% | +0.5 | 90% | ❌ 70 pts to go |
| P05 | 422 | 0.0% | 82.5% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 22259 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 59840 | 0.0% | 99.9% | +0.0 | n/a | no target |
| P06 | 280 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 831 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 30624 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 275 | 2.9% | 4.7% | +0.6 | 90% | ❌ 87 pts to go |
| P10 | 2126 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1813 | 2.1% | 97.6% | -2.0 | n/a | no target |
| P12 | 11 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 152067 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 229 | 0.9% | 98.7% | +0.4 | n/a | no target |
| P01_GOLD | 627 | 26.5% | 55.3% | +0.6 | 90% | ❌ 64 pts to go |
| P02 | 468 | 52.4% | 85.9% | +0.9 | n/a | no target |
| P03 | 266 | 25.2% | 59.0% | +0.9 | n/a | no target |
| P04 | 3573 | 21.4% | 94.6% | +0.4 | n/a | no target |
| P05 | 422 | 0.5% | 82.9% | +0.0 | n/a | no target |
| P06M | 22259 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 59840 | 0.1% | 99.9% | +0.0 | n/a | no target |
| P06 | 280 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 831 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 30624 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 275 | 40.4% | 42.2% | -0.6 | n/a | no target |
| P10 | 2126 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1813 | 2.2% | 97.7% | -1.5 | n/a | no target |
| P12 | 11 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 152067 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 229 | 2.2% | 100.0% | +0.1 | n/a | no target |
| P01_GOLD | 627 | 52.0% | 80.9% | +0.2 | 95% | ❌ 43 pts to go |
| P02 | 468 | 58.1% | 91.7% | +1.7 | n/a | no target |
| P03 | 266 | 50.4% | 84.2% | +3.6 | n/a | no target |
| P04 | 3573 | 22.2% | 95.4% | +1.0 | n/a | no target |
| P05 | 422 | 5.0% | 87.4% | +0.5 | n/a | no target |
| P06M | 22259 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 59840 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 280 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 831 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 30624 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 275 | 60.4% | 62.2% | -2.1 | n/a | no target |
| P10 | 2126 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1813 | 2.4% | 97.9% | -1.7 | n/a | no target |
| P12 | 11 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 152067 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 229 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 627 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 468 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 266 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3573 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 422 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 22259 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 59840 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 280 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 831 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 30624 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 275 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2126 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1813 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 152067 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 229 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 627 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 468 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 266 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3573 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 422 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 22259 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 59840 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 280 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 831 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 30624 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 275 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2126 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1813 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 152067 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 249 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 229 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 627 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 468 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 266 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3573 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 422 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 22259 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 59840 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 280 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 831 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 30624 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 275 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2126 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1813 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 152067 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

