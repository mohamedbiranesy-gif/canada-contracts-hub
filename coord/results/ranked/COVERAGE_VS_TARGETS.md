# Coverage vs the downstream team's targets — 2026-11-11

Benchmarks (field × package with a numeric target): **92 of 446 met** (20.6%); 54 within 10 points; 300 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 100, P01T 334, P01_GOLD 625, P02 473, P03 257, P04 3834, P05 427, P06M 10275, P06T 60046, P06 313, P07 841, P08 26848, P09 303, P10R 99167, P10 2750, P11 11585, P12 7, P13 18051

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 100 | 0.0% | 17.0% | 8 | vendor GST/HST number (86 rows) |
| P01T | 334 | 0.9% | 21.3% | 7 | payment terms (259 rows) |
| P01_GOLD | 625 | 23.7% | 67.5% | 9 | payment terms (214 rows) |
| P02 | 473 | 7.4% | 51.0% | 9 | PO rule (362 rows) |
| P03 | 257 | 13.6% | 57.6% | 9 | PO rule (123 rows) |
| P04 | 3834 | 1.2% | 15.4% | 6 | PO rule (3638 rows) |
| P05 | 427 | 0.9% | 16.6% | 7 | payment terms (351 rows) |
| P06M | 10275 | 0.0% | 1.4% | 8 | PO rule (10244 rows) |
| P06T | 60046 | 0.0% | 2.2% | 6 | PO rule (59696 rows) |
| P06 | 313 | 0.0% | 6.7% | 6 | reference to quote (PO / contract / vendor id) (313 rows) |
| P07 | 841 | 0.0% | 1.3% | 5 | reference to quote (PO / contract / vendor id) (841 rows) |
| P08 | 26848 | 0.0% | 0.2% | 5 | reference to quote (PO / contract / vendor id) (26848 rows) |
| P09 | 303 | 1.0% | 43.9% | 8 | payment terms (283 rows) |
| P10R | 99167 | 0.0% | 16.2% | 7 | PO rule (99125 rows) |
| P10 | 2750 | 0.0% | 0.7% | 5 | reference to quote (PO / contract / vendor id) (2750 rows) |
| P11 | 11585 | 0.1% | 1.5% | 6 | PO rule (11485 rows) |
| P12 | 7 | 0.0% | 42.9% | 8 | PO rule (7 rows) |
| P13 | 18051 | 0.0% | 0.0% | 5 | reference to quote (PO / contract / vendor id) (18051 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 100 | 7 | 9 | 84 | 0 | 0 | 71 |
| P01T | 334 | 31 | 56 | 247 | 0 | 0 | 71 |
| P01_GOLD | 625 | 226 | 189 | 210 | 0 | 0 | 81 |
| P02 | 473 | 0 | 190 | 283 | 0 | 0 | 66 |
| P03 | 257 | 0 | 0 | 246 | 11 | 0 | 57 |
| P04 | 3834 | 0 | 0 | 3071 | 763 | 0 | 45 |
| P05 | 427 | 15 | 29 | 365 | 18 | 0 | 51 |
| P06M | 10275 | 0 | 3 | 10207 | 65 | 0 | 46 |
| P06T | 60046 | 0 | 42 | 48811 | 11193 | 0 | 38 |
| P06 | 313 | 18 | 44 | 251 | 0 | 0 | 67 |
| P07 | 841 | 0 | 24 | 786 | 31 | 0 | 51 |
| P08 | 26848 | 0 | 0 | 22169 | 4679 | 0 | 38 |
| P09 | 303 | 3 | 12 | 285 | 3 | 0 | 53 |
| P10R | 99167 | 2 | 11 | 65122 | 34032 | 0 | 38 |
| P10 | 2750 | 2 | 13 | 2012 | 723 | 0 | 43 |
| P11 | 11585 | 6 | 9 | 44 | 0 | 11526 | 23 |
| P12 | 7 | 0 | 0 | 7 | 0 | 0 | 51 |
| P13 | 18051 | 2 | 14 | 14235 | 3800 | 0 | 40 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 100 | 80 | 80.0% | bill-to legal name and address (11) |
| P01T | 334 | 158 | 47.3% | bill-to legal name and address (137) |
| P01_GOLD | 625 | 461 | 73.8% | bill-to legal name and address (110) |
| P02 | 473 | 308 | 65.1% | the buyer's PO / reference rule (84) |
| P03 | 257 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (257) |
| P04 | 3834 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (3834) |
| P05 | 427 | 46 | 10.8% | a confirmed invoicing / AP or finance channel (340) |
| P06M | 10275 | 100 | 1.0% | a confirmed invoicing / AP or finance channel (10134) |
| P06T | 60046 | 324 | 0.5% | a confirmed invoicing / AP or finance channel (59147) |
| P06 | 313 | 41 | 13.1% | bill-to legal name and address (150) |
| P07 | 841 | 10 | 1.2% | bill-to legal name and address (411) |
| P08 | 26848 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (26848) |
| P09 | 303 | 41 | 13.5% | a confirmed invoicing / AP or finance channel (253) |
| P10R | 99167 | 439 | 0.4% | a confirmed invoicing / AP or finance channel (98031) |
| P10 | 2750 | 4 | 0.1% | a confirmed invoicing / AP or finance channel (2653) |
| P11 | 11585 | 10 | 0.1% | a confirmed invoicing / AP or finance channel (11526) |
| P12 | 7 | 2 | 28.6% | a confirmed invoicing / AP or finance channel (5) |
| P13 | 18051 | 7 | 0.0% | a confirmed invoicing / AP or finance channel (17701) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 100 | 6 | 6.0% | 6 | 0 | the vendor's GST/HST number (BN9) (86) |
| P01T | 334 | 68 | 20.4% | 23 | 0 | the vendor's GST/HST number (BN9) (184) |
| P01_GOLD | 625 | 396 | 63.4% | 13 | 0 | the vendor's GST/HST number (BN9) (152) |
| P02 | 473 | 212 | 44.8% | 23 | 0 | the vendor's GST/HST number (BN9) (199) |
| P03 | 257 | 17 | 6.6% | 0 | 131 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (89) |
| P04 | 3834 | 42 | 1.1% | 8 | 759 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2966) |
| P05 | 427 | 22 | 5.2% | 8 | 104 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (229) |
| P06M | 10275 | 1 | 0.0% | 10 | 119 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (9996) |
| P06T | 60046 | 62 | 0.1% | 94 | 9283 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (49717) |
| P06 | 313 | 14 | 4.5% | 26 | 0 | the vendor's GST/HST number (BN9) (190) |
| P07 | 841 | 4 | 0.5% | 53 | 24 | the vendor's GST/HST number (BN9) (470) |
| P08 | 26848 | 1 | 0.0% | 4 | 1758 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (25026) |
| P09 | 303 | 39 | 12.9% | 1 | 122 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (122) |
| P10R | 99167 | 834 | 0.8% | 0 | 52050 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (45919) |
| P10 | 2750 | 4 | 0.1% | 20 | 350 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2273) |
| P11 | 11585 | 11 | 0.1% | 13 | 0 | a confirmed invoicing / AP or finance channel (11494) |
| P12 | 7 | 1 | 14.3% | 0 | 3 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2) |
| P13 | 18051 | 10 | 0.1% | 246 | 10443 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (7220) |
| **all** | 236236 | 1744 | 0.7% | 548 | 75146 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 93 | 0 | 0 | 0 | 34 | 11 | 0 | 84 | 89 | 0 |
| P01T | 303 | 0 | 0 | 0 | 134 | 127 | 25 | 250 | 261 | 30 |
| P01_GOLD | 399 | 0 | 0 | 0 | 11 | 93 | 34 | 194 | 228 | 59 |
| P02 | 473 | 0 | 473 | 0 | 49 | 71 | 21 | 362 | 292 | 21 |
| P03 | 257 | 0 | 257 | 0 | 14 | 46 | 24 | 123 | 129 | 28 |
| P04 | 3834 | 0 | 3834 | 0 | 1795 | 1835 | 962 | 3638 | 3379 | 141 |
| P05 | 412 | 0 | 359 | 0 | 73 | 114 | 49 | 343 | 353 | 53 |
| P06M | 10275 | 0 | 10275 | 0 | 5357 | 1138 | 108 | 10244 | 10203 | 24 |
| P06T | 60046 | 0 | 60046 | 0 | 45924 | 40597 | 13323 | 59696 | 58600 | 366 |
| P06 | 295 | 0 | 0 | 0 | 128 | 136 | 54 | 221 | 256 | 5 |
| P07 | 841 | 0 | 841 | 0 | 499 | 462 | 147 | 789 | 791 | 15 |
| P08 | 26848 | 0 | 26848 | 0 | 19825 | 16995 | 5722 | 26591 | 26239 | 218 |
| P09 | 300 | 0 | 279 | 0 | 9 | 67 | 3 | 273 | 285 | 44 |
| P10R | 99165 | 0 | 98992 | 0 | 76439 | 71464 | 40242 | 99125 | 98976 | 17 |
| P10 | 2748 | 0 | 2711 | 0 | 1325 | 1645 | 946 | 2679 | 2628 | 115 |
| P11 | 11579 | 11526 | 11467 | 0 | 10186 | 10368 | 949 | 11485 | 11136 | 39 |
| P12 | 7 | 0 | 6 | 0 | 0 | 2 | 0 | 7 | 7 | 0 |
| P13 | 18049 | 0 | 17943 | 0 | 8945 | 10994 | 4366 | 18015 | 18012 | 21 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_ap_cycle_published | P10R | 0.0% | 20% | 19817 |
| ap_system_hint | P10R | 0.2% | 20% | 19640 |
| vendor_registered_address | P08 | 12.5% | 70% | 15425 |
| buyer_tax_exempt_status | P10R | 0.0% | 15% | 14856 |
| buyer_esignature_preference | P10R | 0.0% | 15% | 14844 |
| buyer_payment_method_preference | P10R | 0.4% | 15% | 14485 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 11990 |
| buyer_phone | P08 | 50.9% | 95% | 11838 |
| ap_system_hint | P06T | 0.7% | 20% | 11575 |
| vendor_bn9 | P08 | 9.6% | 50% | 10843 |
| buyer_legal_name_as_published | P08 | 36.7% | 75% | 10283 |
| buyer_logo_url | P08 | 66.8% | 100% | 8919 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 8870 |
| buyer_tax_exempt_status | P06T | 0.3% | 15% | 8834 |
| buyer_payment_method_preference | P06T | 0.4% | 15% | 8745 |
| buyer_phone | P13 | 46.7% | 95% | 8712 |
| vendor_phone | P08 | 53.2% | 85% | 8548 |
| buyer_logo_url | P13 | 50.0% | 95% | 8126 |
| vendor_phone | P11 | 5.2% | 75% | 8083 |
| vendor_emails | P11 | 4.1% | 70% | 7633 |
| buyer_phone | P11 | 9.3% | 75% | 7608 |
| vendor_emails | P08 | 46.8% | 75% | 7579 |
| buyer_logo_url | P11 | 15.6% | 80% | 7459 |
| vendor_logo_url | P08 | 73.3% | 100% | 7171 |
| contract_value | P11 | 0.7% | 60% | 6867 |
| award_or_notice_id | P11 | 0.7% | 60% | 6866 |
| vendor_trading_name | P08 | 25.1% | 50% | 6680 |
| buyer_bn_as_published | P08 | 10.1% | 35% | 6674 |
| invoice_reference_hint | P08 | 1.0% | 25% | 6455 |
| buyer_legal_name_as_published | P11 | 10.5% | 65% | 6314 |
| contract_or_agreement_number | P11 | 10.5% | 60% | 5739 |
| commodity_codes | P11 | 0.5% | 50% | 5732 |
| invoice_reference_hint | P11 | 11.2% | 60% | 5656 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 5363 |
| ap_system_hint | P08 | 0.8% | 20% | 5155 |
| solicitation_or_tender_number | P11 | 0.7% | 40% | 4556 |
| buyer_address | P08 | 78.7% | 95% | 4386 |
| buyer_esignature_preference | P08 | 0.3% | 15% | 3939 |
| buyer_tax_exempt_status | P08 | 0.4% | 15% | 3934 |
| buyer_payment_method_preference | P08 | 0.4% | 15% | 3927 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 89.0% | 89.0% | +0.3 | 50% | ✅ met |
| P01T | 334 | 88.9% | 88.9% | -0.6 | 50% | ✅ met |
| P01_GOLD | 625 | 92.2% | 94.4% | +0.0 | 95% | 🟡 3 pts to go |
| P02 | 473 | 72.5% | 74.0% | -1.3 | 95% | ❌ 22 pts to go |
| P03 | 257 | 81.7% | 84.8% | -0.3 | 95% | ❌ 13 pts to go |
| P04 | 3834 | 29.2% | 30.6% | -3.6 | 90% | ❌ 61 pts to go |
| P05 | 427 | 38.6% | 41.7% | +0.0 | 70% | ❌ 31 pts to go |
| P06M | 10275 | 92.4% | 92.4% | -0.2 | n/a | no target |
| P06T | 60046 | 79.4% | 79.4% | -0.9 | n/a | no target |
| P06 | 313 | 29.4% | 29.4% | -2.3 | 30% | 🟡 1 pts to go |
| P07 | 841 | 6.2% | 6.2% | -0.7 | 30% | ❌ 24 pts to go |
| P08 | 26848 | 1.0% | 1.0% | -0.1 | 25% | ❌ 24 pts to go |
| P09 | 303 | 99.0% | 99.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10R | 99167 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2750 | 2.6% | 2.6% | +0.0 | 25% | ❌ 22 pts to go |
| P11 | 11585 | 11.2% | 11.3% | -2.4 | 60% | ❌ 49 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 18051 | 0.2% | 0.2% | +0.0 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 334 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 625 | 6.1% | 6.1% | +0.0 | 50% | ❌ 44 pts to go |
| P02 | 473 | 6.1% | 6.1% | -0.1 | 50% | ❌ 44 pts to go |
| P03 | 257 | 1.6% | 1.6% | +0.0 | 40% | ❌ 38 pts to go |
| P04 | 3834 | 0.5% | 0.5% | +0.0 | 30% | ❌ 30 pts to go |
| P05 | 427 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 10275 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 60046 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 313 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 841 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 26848 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 0.7% | 0.7% | +0.0 | 50% | ❌ 49 pts to go |
| P10R | 99167 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2750 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 11585 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18051 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 82.0% | 82.0% | +0.6 | n/a | no target |
| P01T | 334 | 70.1% | 70.1% | -0.4 | 50% | ✅ met |
| P01_GOLD | 625 | 66.9% | 66.9% | +0.0 | 85% | ❌ 18 pts to go |
| P02 | 473 | 63.8% | 63.8% | -1.1 | 90% | ❌ 26 pts to go |
| P03 | 257 | 61.1% | 61.1% | -0.2 | 85% | ❌ 24 pts to go |
| P04 | 3834 | 26.8% | 26.8% | -3.3 | 85% | ❌ 58 pts to go |
| P05 | 427 | 29.0% | 29.0% | +0.0 | 60% | ❌ 31 pts to go |
| P06M | 10275 | 92.3% | 92.3% | -0.1 | n/a | no target |
| P06T | 60046 | 79.1% | 79.1% | -0.9 | n/a | no target |
| P06 | 313 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 841 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 26848 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 96.0% | 96.0% | +0.0 | 100% | 🟡 4 pts to go |
| P10R | 99167 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2750 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 11585 | 10.5% | 10.5% | -2.2 | 60% | ❌ 50 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18051 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 334 | 0.0% | 0.0% | +0.0 | 30% | ❌ 30 pts to go |
| P01_GOLD | 625 | 50.7% | 50.7% | +0.1 | 80% | ❌ 29 pts to go |
| P02 | 473 | 56.0% | 56.0% | -1.0 | 60% | 🟡 4 pts to go |
| P03 | 257 | 51.4% | 51.4% | -0.2 | 80% | ❌ 29 pts to go |
| P04 | 3834 | 22.2% | 22.2% | -2.8 | 50% | ❌ 28 pts to go |
| P05 | 427 | 11.9% | 11.9% | +0.0 | 40% | ❌ 28 pts to go |
| P06M | 10275 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 60046 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 313 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 841 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 26848 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 83.5% | 83.5% | +0.0 | 50% | ✅ met |
| P10R | 99167 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2750 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 11585 | 0.7% | 0.7% | -0.1 | 40% | ❌ 39 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 18051 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 334 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 60.5% | 60.5% | +0.1 | 85% | ❌ 24 pts to go |
| P02 | 473 | 55.4% | 55.4% | -0.9 | 90% | ❌ 35 pts to go |
| P03 | 257 | 59.9% | 59.9% | -0.3 | 85% | ❌ 25 pts to go |
| P04 | 3834 | 23.0% | 23.0% | -2.8 | 85% | ❌ 62 pts to go |
| P05 | 427 | 19.9% | 19.9% | +0.0 | 50% | ❌ 30 pts to go |
| P06M | 10275 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 60046 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 313 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 841 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 26848 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 97.0% | 97.0% | +0.0 | 100% | 🟡 3 pts to go |
| P10R | 99167 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2750 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 11585 | 0.7% | 0.7% | -0.2 | 60% | ❌ 59 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18051 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 334 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 13.0% | 13.0% | +0.1 | 60% | ❌ 47 pts to go |
| P02 | 473 | 5.9% | 5.9% | -0.1 | 50% | ❌ 44 pts to go |
| P03 | 257 | 8.6% | 8.6% | +0.0 | 50% | ❌ 41 pts to go |
| P04 | 3834 | 1.8% | 1.8% | -0.2 | 40% | ❌ 38 pts to go |
| P05 | 427 | 0.9% | 0.9% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 10275 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 60046 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 313 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 841 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 26848 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 2.3% | 2.3% | +0.0 | 50% | ❌ 48 pts to go |
| P10R | 99167 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2750 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 11585 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18051 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 334 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 34.9% | 34.9% | +0.1 | 80% | ❌ 45 pts to go |
| P02 | 473 | 51.2% | 51.2% | -0.8 | 90% | ❌ 39 pts to go |
| P03 | 257 | 33.5% | 33.5% | -0.1 | 80% | ❌ 46 pts to go |
| P04 | 3834 | 21.0% | 21.0% | -2.6 | 85% | ❌ 64 pts to go |
| P05 | 427 | 5.4% | 5.4% | +0.0 | 50% | ❌ 45 pts to go |
| P06M | 10275 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 60046 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 313 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 841 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 26848 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 75.9% | 75.9% | +0.0 | 95% | ❌ 19 pts to go |
| P10R | 99167 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2750 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 11585 | 0.5% | 0.5% | -0.1 | 50% | ❌ 50 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18051 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 334 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 8.5% | 8.5% | +0.0 | 50% | ❌ 42 pts to go |
| P02 | 473 | 6.1% | 6.1% | -0.1 | 50% | ❌ 44 pts to go |
| P03 | 257 | 1.9% | 1.9% | -0.1 | 30% | ❌ 28 pts to go |
| P04 | 3834 | 0.4% | 0.4% | -0.1 | 30% | ❌ 30 pts to go |
| P05 | 427 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 10275 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 60046 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 313 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 841 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 26848 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P10R | 99167 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2750 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 11585 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18051 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 334 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 473 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 257 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3834 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 427 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 10275 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 60046 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 313 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 841 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 26848 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 303 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 99167 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2750 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 11585 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18051 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 14.0% | 14.0% | -0.4 | 70% | ❌ 56 pts to go |
| P01T | 334 | 34.1% | 34.1% | +0.4 | 60% | ❌ 26 pts to go |
| P01_GOLD | 625 | 73.1% | 73.1% | +0.1 | 90% | ❌ 17 pts to go |
| P02 | 473 | 54.3% | 54.3% | -0.8 | 85% | ❌ 31 pts to go |
| P03 | 257 | 69.6% | 69.6% | -0.3 | 90% | ❌ 20 pts to go |
| P04 | 3834 | 29.0% | 29.0% | -3.5 | 75% | ❌ 46 pts to go |
| P05 | 427 | 49.9% | 49.9% | +0.0 | 50% | 🟡 0 pts to go |
| P06M | 10275 | 1.7% | 1.7% | -0.1 | n/a | no target |
| P06T | 60046 | 18.3% | 18.3% | +1.0 | n/a | no target |
| P06 | 313 | 21.1% | 21.1% | -1.7 | 40% | ❌ 19 pts to go |
| P07 | 841 | 14.7% | 14.7% | -1.7 | 50% | ❌ 35 pts to go |
| P08 | 26848 | 9.6% | 9.6% | -1.3 | 50% | ❌ 40 pts to go |
| P09 | 303 | 57.8% | 57.8% | +0.0 | 80% | ❌ 22 pts to go |
| P10R | 99167 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2750 | 28.2% | 28.2% | -0.5 | 40% | ❌ 12 pts to go |
| P11 | 11585 | 92.5% | 92.5% | +1.4 | 60% | ✅ met |
| P12 | 7 | 57.1% | 57.1% | -5.4 | 85% | ❌ 28 pts to go |
| P13 | 18051 | 91.0% | 91.0% | +0.0 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 66.0% | 66.0% | -1.0 | n/a | no target |
| P01T | 334 | 38.3% | 38.3% | +0.3 | n/a | no target |
| P01_GOLD | 625 | 70.6% | 70.6% | +0.2 | 95% | ❌ 24 pts to go |
| P02 | 473 | 72.5% | 72.5% | -1.3 | 95% | ❌ 22 pts to go |
| P03 | 257 | 71.6% | 71.6% | -0.3 | 95% | ❌ 23 pts to go |
| P04 | 3834 | 40.7% | 40.7% | -4.9 | 95% | ❌ 54 pts to go |
| P05 | 427 | 53.4% | 53.4% | +0.0 | 70% | ❌ 17 pts to go |
| P06M | 10275 | 53.1% | 53.1% | -1.5 | n/a | no target |
| P06T | 60046 | 31.1% | 31.1% | +0.8 | n/a | no target |
| P06 | 313 | 23.0% | 23.0% | -1.8 | 80% | ❌ 57 pts to go |
| P07 | 841 | 16.2% | 16.2% | -1.8 | 70% | ❌ 54 pts to go |
| P08 | 26848 | 12.5% | 12.5% | -1.6 | 70% | ❌ 58 pts to go |
| P09 | 303 | 87.5% | 87.5% | +0.0 | 100% | ❌ 12 pts to go |
| P10R | 99167 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2750 | 31.9% | 31.9% | -0.6 | 70% | ❌ 38 pts to go |
| P11 | 11585 | 93.4% | 93.4% | +1.2 | 75% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18051 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 16.0% | 16.0% | -0.5 | n/a | no target |
| P01T | 334 | 26.3% | 26.3% | +0.4 | n/a | no target |
| P01_GOLD | 625 | 48.0% | 48.0% | +0.1 | 60% | ❌ 12 pts to go |
| P02 | 473 | 54.5% | 54.5% | -0.8 | 60% | 🟡 6 pts to go |
| P03 | 257 | 54.9% | 54.9% | -0.2 | 60% | 🟡 5 pts to go |
| P04 | 3834 | 34.3% | 34.3% | -2.4 | 55% | ❌ 21 pts to go |
| P05 | 427 | 22.2% | 22.2% | +0.0 | 50% | ❌ 28 pts to go |
| P06M | 10275 | 4.0% | 4.0% | +0.4 | n/a | no target |
| P06T | 60046 | 27.8% | 27.8% | +0.8 | n/a | no target |
| P06 | 313 | 33.9% | 33.9% | -1.3 | n/a | no target |
| P07 | 841 | 31.3% | 31.3% | -1.9 | 55% | ❌ 24 pts to go |
| P08 | 26848 | 25.1% | 25.1% | -1.8 | 50% | ❌ 25 pts to go |
| P09 | 303 | 71.0% | 71.0% | +0.0 | 70% | ✅ met |
| P10R | 99167 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2750 | 38.8% | 38.8% | -0.7 | 55% | ❌ 16 pts to go |
| P11 | 11585 | 93.3% | 93.3% | +1.3 | 50% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +12.5 | n/a | no target |
| P13 | 18051 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 14.0% | 14.0% | -0.4 | n/a | no target |
| P01T | 334 | 56.3% | 56.3% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 48.0% | 48.0% | +0.1 | 70% | ❌ 22 pts to go |
| P02 | 473 | 53.7% | 53.7% | -0.3 | 70% | ❌ 16 pts to go |
| P03 | 257 | 49.4% | 49.4% | -0.2 | 70% | ❌ 21 pts to go |
| P04 | 3834 | 45.5% | 45.5% | -1.6 | 65% | ❌ 20 pts to go |
| P05 | 427 | 30.7% | 30.7% | +0.0 | 60% | ❌ 29 pts to go |
| P06M | 10275 | 3.2% | 3.2% | -0.3 | n/a | no target |
| P06T | 60046 | 63.0% | 63.0% | -0.8 | n/a | no target |
| P06 | 313 | 54.6% | 54.6% | -3.0 | 40% | ✅ met |
| P07 | 841 | 52.7% | 52.7% | -4.3 | 85% | ❌ 32 pts to go |
| P08 | 26848 | 53.2% | 53.2% | -3.7 | 85% | ❌ 32 pts to go |
| P09 | 303 | 53.5% | 53.5% | +0.0 | 85% | ❌ 32 pts to go |
| P10R | 99167 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2750 | 60.7% | 60.7% | -0.3 | 85% | ❌ 24 pts to go |
| P11 | 11585 | 5.2% | 5.2% | -1.2 | 75% | ❌ 70 pts to go |
| P12 | 7 | 28.6% | 28.6% | +3.6 | n/a | no target |
| P13 | 18051 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 19.0% | 19.0% | -0.6 | n/a | no target |
| P01T | 334 | 96.4% | 96.4% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 89.4% | 89.4% | +0.1 | 90% | 🟡 1 pts to go |
| P02 | 473 | 89.4% | 89.4% | +0.2 | 90% | 🟡 1 pts to go |
| P03 | 257 | 91.1% | 91.1% | +0.1 | 90% | ✅ met |
| P04 | 3834 | 91.3% | 91.3% | +1.1 | 85% | ✅ met |
| P05 | 427 | 52.2% | 52.2% | +0.0 | 70% | ❌ 18 pts to go |
| P06M | 10275 | 6.2% | 6.2% | +0.0 | n/a | no target |
| P06T | 60046 | 92.0% | 92.0% | +0.0 | n/a | no target |
| P06 | 313 | 98.4% | 98.4% | +0.1 | 50% | ✅ met |
| P07 | 841 | 99.2% | 99.2% | +0.1 | 100% | 🟡 1 pts to go |
| P08 | 26848 | 99.5% | 99.5% | +0.1 | 100% | 🟡 0 pts to go |
| P09 | 303 | 80.2% | 80.2% | +0.0 | 100% | ❌ 20 pts to go |
| P10R | 99167 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2750 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 11585 | 99.7% | 99.7% | +0.0 | 100% | 🟡 0 pts to go |
| P12 | 7 | 42.9% | 42.9% | +5.4 | n/a | no target |
| P13 | 18051 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 14.0% | 14.0% | -0.4 | n/a | no target |
| P01T | 334 | 48.8% | 48.8% | -0.3 | n/a | no target |
| P01_GOLD | 625 | 45.3% | 45.3% | +0.1 | 70% | ❌ 25 pts to go |
| P02 | 473 | 49.3% | 49.3% | -0.2 | 75% | ❌ 26 pts to go |
| P03 | 257 | 44.4% | 44.4% | -0.1 | 75% | ❌ 31 pts to go |
| P04 | 3834 | 37.0% | 37.0% | -0.4 | 70% | ❌ 33 pts to go |
| P05 | 427 | 25.5% | 25.5% | +0.0 | 55% | ❌ 30 pts to go |
| P06M | 10275 | 3.2% | 3.2% | -0.1 | n/a | no target |
| P06T | 60046 | 39.1% | 39.1% | -0.5 | n/a | no target |
| P06 | 313 | 40.6% | 40.6% | -2.2 | n/a | no target |
| P07 | 841 | 43.3% | 43.3% | -2.6 | 70% | ❌ 27 pts to go |
| P08 | 26848 | 46.8% | 46.8% | -3.1 | 75% | ❌ 28 pts to go |
| P09 | 303 | 49.8% | 49.8% | +0.0 | 85% | ❌ 35 pts to go |
| P10R | 99167 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2750 | 43.3% | 43.3% | -0.2 | 80% | ❌ 37 pts to go |
| P11 | 11585 | 4.1% | 4.1% | -0.9 | 70% | ❌ 66 pts to go |
| P12 | 7 | 28.6% | 28.6% | +3.6 | n/a | no target |
| P13 | 18051 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 13.0% | 13.0% | -0.4 | n/a | no target |
| P01T | 334 | 89.8% | 89.8% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 77.6% | 77.6% | +0.1 | 90% | ❌ 12 pts to go |
| P02 | 473 | 77.2% | 77.2% | -0.4 | 90% | ❌ 13 pts to go |
| P03 | 257 | 82.9% | 82.9% | -0.3 | 90% | 🟡 7 pts to go |
| P04 | 3834 | 71.9% | 71.9% | -3.7 | 85% | ❌ 13 pts to go |
| P05 | 427 | 48.7% | 48.7% | +0.0 | 75% | ❌ 26 pts to go |
| P06M | 10275 | 4.0% | 4.0% | -0.1 | n/a | no target |
| P06T | 60046 | 83.4% | 83.4% | +0.2 | n/a | no target |
| P06 | 313 | 75.7% | 75.7% | -3.6 | n/a | no target |
| P07 | 841 | 76.2% | 76.2% | -5.4 | 100% | ❌ 24 pts to go |
| P08 | 26848 | 73.3% | 73.3% | -5.6 | 100% | ❌ 27 pts to go |
| P09 | 303 | 61.4% | 61.4% | +0.0 | n/a | no target |
| P10R | 99167 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2750 | 83.7% | 83.7% | -0.5 | 100% | ❌ 16 pts to go |
| P11 | 11585 | 90.3% | 90.3% | +1.9 | n/a | no target |
| P12 | 7 | 42.9% | 42.9% | +5.4 | n/a | no target |
| P13 | 18051 | 83.3% | 83.3% | +0.1 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 53.0% | 53.0% | -0.6 | n/a | no target · QC vendors: 48 rows, 100.0% filled |
| P01T | 334 | 18.3% | 18.3% | +0.5 | n/a | no target · QC vendors: 17 rows, 100.0% filled |
| P01_GOLD | 625 | 43.7% | 43.7% | +0.1 | 95% | ❌ 51 pts to go · QC vendors: 53 rows, 98.1% filled |
| P02 | 473 | 54.1% | 54.1% | -1.0 | 95% | ❌ 41 pts to go · QC vendors: 110 rows, 100.0% filled |
| P03 | 257 | 46.3% | 46.3% | -0.2 | 95% | ❌ 49 pts to go · QC vendors: 18 rows, 100.0% filled |
| P04 | 3834 | 28.4% | 28.4% | -3.5 | 95% | ❌ 67 pts to go · QC vendors: 498 rows, 98.8% filled |
| P05 | 427 | 14.8% | 14.8% | +0.0 | n/a | no target · QC vendors: 35 rows, 94.3% filled |
| P06M | 10275 | 51.9% | 51.9% | -1.4 | n/a | no target · QC vendors: 5114 rows, 100.0% filled |
| P06T | 60046 | 18.5% | 18.5% | +1.0 | n/a | no target · QC vendors: 3295 rows, 100.0% filled |
| P06 | 313 | 7.7% | 7.7% | -0.6 | n/a | no target · QC vendors: 13 rows, 100.0% filled |
| P07 | 841 | 6.2% | 6.2% | -0.6 | n/a | no target · QC vendors: 36 rows, 97.2% filled |
| P08 | 26848 | 6.0% | 6.0% | -0.5 | n/a | no target · QC vendors: 1285 rows, 99.7% filled |
| P09 | 303 | 78.2% | 78.2% | +0.0 | 95% | ❌ 17 pts to go · QC vendors: 111 rows, 100.0% filled |
| P10R | 99167 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2750 | 17.2% | 17.2% | -0.4 | n/a | no target · QC vendors: 311 rows, 94.9% filled |
| P11 | 11585 | 84.6% | 84.6% | +3.1 | n/a | no target · QC vendors: 111 rows, 99.1% filled |
| P12 | 7 | 71.4% | 71.4% | +8.9 | n/a | no target · QC vendors: 1 rows, 100.0% filled |
| P13 | 18051 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 64.0% | 64.0% | -0.9 | n/a | no target · vendors with a registry record: 64 rows, 100.0% filled |
| P01T | 334 | 38.6% | 38.6% | +0.3 | n/a | no target · vendors with a registry record: 129 rows, 100.0% filled |
| P01_GOLD | 625 | 79.5% | 79.5% | +0.1 | 100% | ❌ 20 pts to go · vendors with a registry record: 497 rows, 100.0% filled |
| P02 | 473 | 76.1% | 76.1% | -1.3 | 100% | ❌ 24 pts to go · vendors with a registry record: 360 rows, 100.0% filled |
| P03 | 257 | 80.9% | 80.9% | -0.3 | 100% | ❌ 19 pts to go · vendors with a registry record: 208 rows, 100.0% filled |
| P04 | 3834 | 41.1% | 41.1% | -5.0 | 100% | ❌ 59 pts to go · vendors with a registry record: 1577 rows, 100.0% filled |
| P05 | 427 | 58.3% | 58.3% | +0.0 | n/a | no target · vendors with a registry record: 249 rows, 100.0% filled |
| P06M | 10275 | 52.9% | 52.9% | -1.4 | n/a | no target · vendors with a registry record: 5434 rows, 100.0% filled |
| P06T | 60046 | 31.2% | 31.2% | +0.8 | n/a | no target · vendors with a registry record: 18713 rows, 100.0% filled |
| P06 | 313 | 23.6% | 23.6% | -1.9 | n/a | no target · vendors with a registry record: 74 rows, 100.0% filled |
| P07 | 841 | 16.5% | 16.5% | -1.9 | n/a | no target · vendors with a registry record: 139 rows, 100.0% filled |
| P08 | 26848 | 12.7% | 12.7% | -1.6 | n/a | no target · vendors with a registry record: 3420 rows, 100.0% filled |
| P09 | 303 | 91.1% | 91.1% | +0.0 | n/a | no target · vendors with a registry record: 276 rows, 100.0% filled |
| P10R | 99167 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 99167 rows, 100.0% filled |
| P10 | 2750 | 32.5% | 32.5% | -0.7 | n/a | no target · vendors with a registry record: 893 rows, 100.0% filled |
| P11 | 11585 | 93.6% | 93.6% | +1.3 | n/a | no target · vendors with a registry record: 10838 rows, 100.0% filled |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 7 rows, 100.0% filled |
| P13 | 18051 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 89.0% | 89.0% | +0.3 | 90% | 🟡 1 pts to go |
| P01T | 334 | 62.0% | 62.0% | +5.7 | 90% | ❌ 28 pts to go |
| P01_GOLD | 625 | 85.1% | 85.1% | +1.4 | 95% | 🟡 10 pts to go |
| P02 | 473 | 85.0% | 85.0% | -0.2 | 95% | 🟡 10 pts to go |
| P03 | 257 | 82.1% | 82.1% | +3.2 | 85% | 🟡 3 pts to go |
| P04 | 3834 | 52.1% | 52.1% | -4.3 | 90% | ❌ 38 pts to go |
| P05 | 427 | 73.3% | 73.3% | +5.6 | 75% | 🟡 2 pts to go |
| P06M | 10275 | 88.9% | 88.9% | +1.8 | n/a | no target |
| P06T | 60046 | 32.4% | 32.4% | +3.4 | n/a | no target |
| P06 | 313 | 56.5% | 56.5% | -0.4 | 80% | ❌ 24 pts to go |
| P07 | 841 | 45.1% | 45.2% | -1.1 | 80% | ❌ 35 pts to go |
| P08 | 26848 | 36.7% | 36.7% | -1.8 | 75% | ❌ 38 pts to go |
| P09 | 303 | 77.9% | 77.9% | +0.7 | 95% | ❌ 17 pts to go |
| P10R | 99167 | 27.9% | 27.9% | +2.9 | n/a | no target |
| P10 | 2750 | 40.2% | 40.2% | +1.2 | 70% | ❌ 30 pts to go |
| P11 | 11585 | 10.5% | 10.5% | +0.9 | 65% | ❌ 54 pts to go |
| P12 | 7 | 71.4% | 71.4% | -3.6 | 80% | 🟡 9 pts to go |
| P13 | 18051 | 39.1% | 39.1% | -0.1 | 60% | ❌ 21 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 22.0% | 22.0% | +2.4 | 50% | ❌ 28 pts to go |
| P01T | 334 | 14.4% | 14.4% | +1.1 | n/a | no target |
| P01_GOLD | 625 | 20.8% | 20.8% | +0.2 | 40% | ❌ 19 pts to go |
| P02 | 473 | 19.5% | 19.5% | +0.6 | 40% | ❌ 20 pts to go |
| P03 | 257 | 23.0% | 23.0% | +0.7 | 40% | ❌ 17 pts to go |
| P04 | 3834 | 14.9% | 14.9% | -1.4 | 40% | ❌ 25 pts to go |
| P05 | 427 | 19.9% | 19.9% | +0.2 | 25% | 🟡 5 pts to go |
| P06M | 10275 | 8.8% | 8.8% | +0.0 | n/a | no target |
| P06T | 60046 | 8.5% | 8.5% | +1.0 | n/a | no target |
| P06 | 313 | 12.8% | 12.8% | +0.0 | 35% | ❌ 22 pts to go |
| P07 | 841 | 12.1% | 12.1% | +0.6 | 35% | ❌ 23 pts to go |
| P08 | 26848 | 10.1% | 10.1% | -0.3 | 35% | ❌ 25 pts to go |
| P09 | 303 | 16.5% | 16.5% | +0.3 | n/a | no target |
| P10R | 99167 | 7.7% | 7.7% | +0.6 | n/a | no target |
| P10 | 2750 | 8.8% | 8.8% | +2.3 | 30% | ❌ 21 pts to go |
| P11 | 11585 | 1.5% | 1.5% | +0.3 | n/a | no target |
| P12 | 7 | 14.3% | 14.3% | +1.8 | n/a | no target |
| P13 | 18051 | 20.8% | 20.8% | -0.2 | 30% | 🟡 9 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 334 | 91.9% | 91.9% | +0.0 | 100% | 🟡 8 pts to go |
| P01_GOLD | 625 | 89.9% | 89.9% | +0.4 | 100% | ❌ 10 pts to go |
| P02 | 473 | 95.1% | 95.1% | -0.2 | 100% | 🟡 5 pts to go |
| P03 | 257 | 89.5% | 89.5% | +0.0 | 100% | ❌ 10 pts to go |
| P04 | 3834 | 74.4% | 74.4% | -1.5 | 100% | ❌ 26 pts to go |
| P05 | 427 | 87.8% | 87.8% | +0.4 | 100% | ❌ 12 pts to go |
| P06M | 10275 | 98.9% | 98.9% | +0.1 | n/a | no target |
| P06T | 60046 | 77.8% | 77.8% | +0.4 | n/a | no target |
| P06 | 313 | 81.2% | 81.2% | +0.2 | 95% | ❌ 14 pts to go |
| P07 | 841 | 82.4% | 82.4% | -1.2 | 95% | ❌ 13 pts to go |
| P08 | 26848 | 78.7% | 78.7% | -1.5 | 95% | ❌ 16 pts to go |
| P09 | 303 | 95.7% | 95.7% | +0.0 | 100% | 🟡 4 pts to go |
| P10R | 99167 | 59.4% | 59.4% | +0.6 | n/a | no target |
| P10 | 2750 | 65.5% | 65.5% | +0.4 | 95% | ❌ 30 pts to go |
| P11 | 11585 | 89.9% | 89.9% | +2.7 | 80% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 18051 | 75.8% | 75.8% | +0.6 | 95% | ❌ 19 pts to go |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 86.0% | 86.0% | +0.4 | n/a | no target |
| P01T | 334 | 63.8% | 63.8% | +0.2 | n/a | no target |
| P01_GOLD | 625 | 69.4% | 69.4% | -0.1 | 90% | ❌ 21 pts to go |
| P02 | 473 | 74.4% | 74.4% | -1.3 | 95% | ❌ 21 pts to go |
| P03 | 257 | 73.5% | 73.5% | -0.3 | 95% | ❌ 22 pts to go |
| P04 | 3834 | 59.3% | 59.3% | -7.3 | 95% | ❌ 36 pts to go |
| P05 | 427 | 70.5% | 70.5% | +0.0 | 90% | ❌ 20 pts to go |
| P06M | 10275 | 84.1% | 84.1% | -2.3 | n/a | no target |
| P06T | 60046 | 47.5% | 47.5% | -0.4 | n/a | no target |
| P06 | 313 | 58.5% | 58.5% | -4.6 | 95% | ❌ 36 pts to go |
| P07 | 841 | 49.2% | 49.2% | -5.8 | 90% | ❌ 41 pts to go |
| P08 | 26848 | 50.9% | 50.9% | -7.9 | 95% | ❌ 44 pts to go |
| P09 | 303 | 86.1% | 86.1% | +0.0 | 100% | ❌ 14 pts to go |
| P10R | 99167 | 44.5% | 44.5% | -0.6 | n/a | no target |
| P10 | 2750 | 55.3% | 55.3% | -1.2 | 95% | ❌ 40 pts to go |
| P11 | 11585 | 9.3% | 9.3% | -1.9 | 75% | ❌ 66 pts to go |
| P12 | 7 | 71.4% | 71.4% | -3.6 | n/a | no target |
| P13 | 18051 | 46.7% | 46.7% | -0.9 | 95% | ❌ 48 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 71.0% | 71.0% | -0.1 | n/a | no target |
| P01T | 334 | 74.3% | 74.3% | +0.2 | 95% | ❌ 21 pts to go |
| P01_GOLD | 625 | 80.6% | 80.6% | -0.1 | 90% | 🟡 9 pts to go |
| P02 | 473 | 84.4% | 84.4% | -1.4 | 95% | ❌ 11 pts to go |
| P03 | 257 | 83.7% | 83.7% | -0.3 | 95% | ❌ 11 pts to go |
| P04 | 3834 | 74.0% | 74.0% | -9.3 | 90% | ❌ 16 pts to go |
| P05 | 427 | 88.5% | 88.5% | +0.0 | 95% | 🟡 6 pts to go |
| P06M | 10275 | 65.4% | 65.4% | -1.3 | n/a | no target |
| P06T | 60046 | 61.1% | 61.1% | -0.4 | n/a | no target |
| P06 | 313 | 76.0% | 76.0% | -6.1 | 100% | ❌ 24 pts to go |
| P07 | 841 | 69.3% | 69.3% | -7.9 | 100% | ❌ 31 pts to go |
| P08 | 26848 | 66.8% | 66.8% | -10.3 | 100% | ❌ 33 pts to go |
| P09 | 303 | 68.6% | 68.6% | +0.0 | n/a | no target |
| P10R | 99167 | 59.2% | 59.2% | -0.8 | n/a | no target |
| P10 | 2750 | 85.0% | 85.0% | -1.8 | 100% | ❌ 15 pts to go |
| P11 | 11585 | 15.6% | 15.6% | -3.2 | 80% | ❌ 64 pts to go |
| P12 | 7 | 71.4% | 71.4% | -3.6 | n/a | no target |
| P13 | 18051 | 50.0% | 50.0% | -1.0 | 95% | ❌ 45 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 4.0% | 4.0% | -0.1 | n/a | no target |
| P01T | 334 | 8.4% | 8.4% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 14.2% | 14.2% | +0.0 | 25% | ❌ 11 pts to go |
| P02 | 473 | 24.1% | 24.1% | -0.4 | 40% | ❌ 16 pts to go |
| P03 | 257 | 8.9% | 8.9% | -0.1 | 20% | ❌ 11 pts to go |
| P04 | 3834 | 3.2% | 3.2% | -0.4 | 20% | ❌ 17 pts to go |
| P05 | 427 | 3.3% | 3.3% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 10275 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 60046 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P06 | 313 | 5.8% | 5.8% | -0.4 | n/a | no target |
| P07 | 841 | 7.1% | 7.1% | -0.2 | n/a | no target |
| P08 | 26848 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P09 | 303 | 7.6% | 7.6% | +0.0 | n/a | no target |
| P10R | 99167 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P10 | 2750 | 0.9% | 0.9% | -0.1 | n/a | no target |
| P11 | 11585 | 0.1% | 0.1% | -0.1 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18051 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 26.0% | 26.0% | -0.8 | n/a | no target |
| P01T | 334 | 24.0% | 24.0% | -0.1 | 70% | ❌ 46 pts to go |
| P01_GOLD | 625 | 43.4% | 43.4% | +0.1 | 80% | ❌ 37 pts to go |
| P02 | 473 | 55.8% | 55.8% | -1.0 | 90% | ❌ 34 pts to go |
| P03 | 257 | 19.1% | 19.1% | +0.0 | 60% | ❌ 41 pts to go |
| P04 | 3834 | 21.1% | 21.1% | -2.6 | 85% | ❌ 64 pts to go |
| P05 | 427 | 11.9% | 11.9% | +0.0 | 50% | ❌ 38 pts to go |
| P06M | 10275 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P06T | 60046 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06 | 313 | 15.0% | 15.0% | -1.2 | n/a | no target |
| P07 | 841 | 11.5% | 11.5% | -1.5 | n/a | no target |
| P08 | 26848 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P09 | 303 | 77.6% | 77.6% | +0.0 | 95% | ❌ 17 pts to go |
| P10R | 99167 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P10 | 2750 | 1.7% | 1.7% | +0.0 | n/a | no target |
| P11 | 11585 | 3.0% | 3.0% | -0.6 | n/a | no target |
| P12 | 7 | 14.3% | 14.3% | -10.7 | n/a | no target |
| P13 | 18051 | 0.7% | 0.7% | +0.0 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 7.0% | 7.0% | -0.2 | n/a | no target |
| P01T | 334 | 12.0% | 12.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 33.9% | 33.9% | +0.0 | 70% | ❌ 36 pts to go |
| P02 | 473 | 38.3% | 38.3% | -0.6 | 75% | ❌ 37 pts to go |
| P03 | 257 | 19.1% | 19.1% | +0.0 | 55% | ❌ 36 pts to go |
| P04 | 3834 | 21.0% | 21.0% | -2.6 | 75% | ❌ 54 pts to go |
| P05 | 427 | 10.8% | 10.8% | +0.0 | 50% | ❌ 39 pts to go |
| P06M | 10275 | 0.1% | 0.1% | -0.1 | n/a | no target |
| P06T | 60046 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P06 | 313 | 7.7% | 7.7% | -0.6 | n/a | no target |
| P07 | 841 | 5.7% | 5.7% | -0.7 | n/a | no target |
| P08 | 26848 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 303 | 75.2% | 75.2% | +0.0 | 95% | ❌ 20 pts to go |
| P10R | 99167 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P10 | 2750 | 1.0% | 1.0% | +0.0 | n/a | no target |
| P11 | 11585 | 2.9% | 2.9% | -0.7 | n/a | no target |
| P12 | 7 | 14.3% | 14.3% | +1.8 | n/a | no target |
| P13 | 18051 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 6.0% | 6.0% | -0.2 | n/a | no target |
| P01T | 334 | 9.3% | 9.3% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 57.9% | 58.1% | -0.1 | 80% | ❌ 22 pts to go |
| P02 | 473 | 45.0% | 45.2% | -0.8 | 75% | ❌ 30 pts to go |
| P03 | 257 | 37.7% | 37.7% | -0.2 | 70% | ❌ 32 pts to go |
| P04 | 3834 | 20.6% | 21.0% | -2.5 | 70% | ❌ 49 pts to go |
| P05 | 427 | 14.3% | 14.3% | +0.0 | 50% | ❌ 36 pts to go |
| P06M | 10275 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P06T | 60046 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 313 | 12.5% | 12.5% | -0.9 | n/a | no target |
| P07 | 841 | 1.8% | 1.8% | -0.2 | n/a | no target |
| P08 | 26848 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P09 | 303 | 45.9% | 46.2% | +0.0 | 80% | ❌ 34 pts to go |
| P10R | 99167 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P10 | 2750 | 1.2% | 1.2% | +0.0 | n/a | no target |
| P11 | 11585 | 0.9% | 0.9% | -0.2 | n/a | no target |
| P12 | 7 | 42.9% | 42.9% | +5.4 | n/a | no target |
| P13 | 18051 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 11.0% | 11.0% | -0.3 | n/a | no target |
| P01T | 334 | 21.9% | 21.9% | -0.1 | 60% | ❌ 38 pts to go |
| P01_GOLD | 625 | 63.5% | 63.5% | -0.1 | 70% | 🟡 6 pts to go |
| P02 | 473 | 38.3% | 38.3% | -0.6 | 50% | ❌ 12 pts to go |
| P03 | 257 | 49.8% | 49.8% | -0.2 | 55% | 🟡 5 pts to go |
| P04 | 3834 | 11.9% | 11.9% | -1.4 | 40% | ❌ 28 pts to go |
| P05 | 427 | 17.3% | 17.3% | +0.0 | 40% | ❌ 23 pts to go |
| P06M | 10275 | 0.7% | 0.7% | +0.0 | n/a | no target |
| P06T | 60046 | 2.4% | 2.4% | +0.0 | n/a | no target |
| P06 | 313 | 18.2% | 18.2% | -1.5 | n/a | no target |
| P07 | 841 | 5.9% | 5.9% | -0.8 | n/a | no target |
| P08 | 26848 | 2.3% | 2.3% | -0.3 | n/a | no target |
| P09 | 303 | 5.9% | 5.9% | +0.0 | n/a | no target |
| P10R | 99167 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P10 | 2750 | 4.4% | 4.4% | -0.1 | n/a | no target |
| P11 | 11585 | 3.9% | 3.9% | -0.4 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | -12.5 | n/a | no target |
| P13 | 18051 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 16.0% | 16.0% | -0.5 | n/a | no target |
| P01T | 334 | 25.1% | 25.1% | -0.2 | 65% | ❌ 40 pts to go |
| P01_GOLD | 625 | 69.0% | 69.0% | +0.0 | 70% | 🟡 1 pts to go |
| P02 | 473 | 23.5% | 23.5% | -0.4 | 50% | ❌ 26 pts to go |
| P03 | 257 | 52.1% | 52.1% | -0.2 | 60% | 🟡 8 pts to go |
| P04 | 3834 | 5.1% | 5.1% | -0.7 | 40% | ❌ 35 pts to go |
| P05 | 427 | 19.7% | 19.7% | +0.0 | 45% | ❌ 25 pts to go |
| P06M | 10275 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 60046 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06 | 313 | 29.4% | 29.4% | -2.3 | n/a | no target |
| P07 | 841 | 6.2% | 6.2% | -0.7 | n/a | no target |
| P08 | 26848 | 1.0% | 1.0% | -0.1 | n/a | no target |
| P09 | 303 | 9.9% | 9.9% | +0.0 | n/a | no target |
| P10R | 99167 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2750 | 2.6% | 2.6% | +0.0 | n/a | no target |
| P11 | 11585 | 0.9% | 0.9% | -0.1 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18051 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 6.0% | 6.0% | -0.2 | n/a | no target |
| P01T | 334 | 14.7% | 14.7% | +0.2 | n/a | no target |
| P01_GOLD | 625 | 49.8% | 49.8% | +0.0 | 50% | 🟡 0 pts to go |
| P02 | 473 | 36.8% | 36.8% | -0.6 | n/a | no target |
| P03 | 257 | 52.9% | 52.9% | -0.2 | 60% | 🟡 7 pts to go |
| P04 | 3834 | 11.5% | 11.5% | -1.4 | n/a | no target |
| P05 | 427 | 15.2% | 15.2% | +0.0 | n/a | no target |
| P06M | 10275 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 60046 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P06 | 313 | 20.1% | 20.1% | -1.6 | n/a | no target |
| P07 | 841 | 6.4% | 6.4% | -0.8 | n/a | no target |
| P08 | 26848 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P09 | 303 | 18.2% | 18.2% | +0.0 | n/a | no target |
| P10R | 99167 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P10 | 2750 | 2.3% | 2.3% | +0.0 | n/a | no target |
| P11 | 11585 | 0.7% | 0.7% | -0.1 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18051 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 11.0% | 11.0% | -0.3 | 15% | 🟡 4 pts to go |
| P01T | 334 | 11.1% | 11.1% | +0.0 | 15% | 🟡 4 pts to go |
| P01_GOLD | 625 | 35.2% | 35.2% | -0.1 | 40% | 🟡 5 pts to go |
| P02 | 473 | 12.3% | 12.5% | -0.2 | 25% | ❌ 13 pts to go |
| P03 | 257 | 17.9% | 17.9% | -0.1 | 25% | 🟡 7 pts to go |
| P04 | 3834 | 2.5% | 2.5% | -0.3 | 15% | ❌ 12 pts to go |
| P05 | 427 | 6.8% | 6.8% | +0.0 | 15% | 🟡 8 pts to go |
| P06M | 10275 | 0.5% | 0.5% | -0.1 | 15% | ❌ 14 pts to go |
| P06T | 60046 | 0.4% | 0.4% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 313 | 8.6% | 8.6% | -0.7 | 15% | 🟡 6 pts to go |
| P07 | 841 | 2.9% | 2.9% | -0.3 | 15% | ❌ 12 pts to go |
| P08 | 26848 | 0.4% | 0.4% | +0.0 | 15% | ❌ 15 pts to go |
| P09 | 303 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P10R | 99167 | 0.4% | 0.4% | +0.0 | 15% | ❌ 15 pts to go |
| P10 | 2750 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 11585 | 0.1% | 0.1% | -0.1 | 15% | ❌ 15 pts to go |
| P12 | 7 | 14.3% | 14.3% | +1.8 | 15% | 🟡 1 pts to go |
| P13 | 18051 | 0.4% | 0.4% | +0.0 | 15% | ❌ 15 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 6.0% | 6.0% | -0.2 | 15% | 🟡 9 pts to go |
| P01T | 334 | 12.0% | 12.0% | +0.0 | 25% | ❌ 13 pts to go |
| P01_GOLD | 625 | 29.1% | 29.1% | -0.1 | 25% | ✅ met |
| P02 | 473 | 24.9% | 24.9% | -0.5 | 15% | ✅ met |
| P03 | 257 | 21.4% | 21.4% | -0.1 | 15% | ✅ met |
| P04 | 3834 | 3.7% | 3.7% | -0.4 | 15% | ❌ 11 pts to go |
| P05 | 427 | 10.8% | 10.8% | +0.0 | 15% | 🟡 4 pts to go |
| P06M | 10275 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06T | 60046 | 0.3% | 0.3% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 313 | 7.0% | 7.0% | -0.6 | 15% | 🟡 8 pts to go |
| P07 | 841 | 2.7% | 2.7% | -0.4 | 15% | ❌ 12 pts to go |
| P08 | 26848 | 0.4% | 0.4% | +0.0 | 15% | ❌ 15 pts to go |
| P09 | 303 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P10R | 99167 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P10 | 2750 | 1.6% | 1.6% | +0.0 | 15% | ❌ 13 pts to go |
| P11 | 11585 | 0.4% | 0.4% | -0.1 | 15% | ❌ 15 pts to go |
| P12 | 7 | 28.6% | 28.6% | +3.6 | 15% | ✅ met |
| P13 | 18051 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P01T | 334 | 3.9% | 3.9% | +0.0 | 20% | ❌ 16 pts to go |
| P01_GOLD | 625 | 4.3% | 4.3% | +0.0 | 20% | ❌ 16 pts to go |
| P02 | 473 | 1.3% | 1.3% | +0.0 | 20% | ❌ 19 pts to go |
| P03 | 257 | 1.6% | 1.6% | +0.0 | 20% | ❌ 18 pts to go |
| P04 | 3834 | 0.5% | 0.5% | -0.1 | 20% | ❌ 20 pts to go |
| P05 | 427 | 1.2% | 1.2% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 10275 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 60046 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 313 | 1.3% | 1.3% | -0.1 | 20% | ❌ 19 pts to go |
| P07 | 841 | 0.4% | 0.4% | +0.0 | 20% | ❌ 20 pts to go |
| P08 | 26848 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P09 | 303 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10R | 99167 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2750 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 11585 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 18051 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P01T | 334 | 2.4% | 2.4% | +0.0 | 15% | ❌ 13 pts to go |
| P01_GOLD | 625 | 10.4% | 10.4% | -0.1 | 15% | 🟡 5 pts to go |
| P02 | 473 | 11.8% | 11.8% | -0.2 | 15% | 🟡 3 pts to go |
| P03 | 257 | 20.6% | 20.6% | -0.1 | 15% | ✅ met |
| P04 | 3834 | 2.2% | 2.2% | -0.2 | 15% | ❌ 13 pts to go |
| P05 | 427 | 3.0% | 3.0% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 10275 | 0.1% | 0.1% | -0.1 | 15% | ❌ 15 pts to go |
| P06T | 60046 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 313 | 4.8% | 4.8% | -0.4 | 15% | ❌ 10 pts to go |
| P07 | 841 | 1.5% | 1.5% | -0.2 | 15% | ❌ 14 pts to go |
| P08 | 26848 | 0.3% | 0.3% | -0.1 | 15% | ❌ 15 pts to go |
| P09 | 303 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P10R | 99167 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P10 | 2750 | 0.9% | 0.9% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 11585 | 0.2% | 0.2% | -0.1 | 15% | ❌ 15 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 18051 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 7.0% | 7.0% | -0.2 | 20% | ❌ 13 pts to go |
| P01T | 334 | 15.3% | 15.3% | +0.2 | 40% | ❌ 25 pts to go |
| P01_GOLD | 625 | 45.8% | 45.8% | +0.0 | 40% | ✅ met |
| P02 | 473 | 42.1% | 42.1% | -0.7 | 20% | ✅ met |
| P03 | 257 | 48.6% | 48.6% | -0.2 | 35% | ✅ met |
| P04 | 3834 | 13.7% | 13.7% | -1.7 | 20% | 🟡 6 pts to go |
| P05 | 427 | 14.8% | 14.8% | +0.0 | 20% | 🟡 5 pts to go |
| P06M | 10275 | 0.4% | 0.4% | -0.1 | 20% | ❌ 20 pts to go |
| P06T | 60046 | 0.7% | 0.7% | +0.0 | 20% | ❌ 19 pts to go |
| P06 | 313 | 20.8% | 20.8% | -1.3 | 20% | ✅ met |
| P07 | 841 | 6.3% | 6.3% | -0.8 | 20% | ❌ 14 pts to go |
| P08 | 26848 | 0.8% | 0.8% | -0.1 | 20% | ❌ 19 pts to go |
| P09 | 303 | 18.2% | 18.2% | +0.0 | 20% | 🟡 2 pts to go |
| P10R | 99167 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2750 | 3.3% | 3.3% | -0.1 | 20% | ❌ 17 pts to go |
| P11 | 11585 | 0.8% | 0.8% | -0.2 | 20% | ❌ 19 pts to go |
| P12 | 7 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 18051 | 0.5% | 0.5% | +0.0 | 20% | ❌ 20 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 44.0% | 44.0% | -0.3 | n/a | no target |
| P01T | 334 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 69.4% | 69.4% | -0.1 | 95% | ❌ 26 pts to go |
| P02 | 473 | 61.9% | 61.9% | -1.1 | 95% | ❌ 33 pts to go |
| P03 | 257 | 54.5% | 54.5% | -0.2 | 90% | ❌ 36 pts to go |
| P04 | 3834 | 24.1% | 24.1% | -3.0 | 85% | ❌ 61 pts to go |
| P05 | 427 | 36.5% | 36.5% | +0.0 | 75% | ❌ 38 pts to go |
| P06M | 10275 | 47.9% | 47.9% | -2.2 | n/a | no target |
| P06T | 60046 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 313 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 841 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 26848 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 89.4% | 89.4% | +0.0 | 100% | ❌ 11 pts to go |
| P10R | 99167 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2750 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 11585 | 0.7% | 0.7% | -0.2 | 60% | ❌ 59 pts to go |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18051 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 44.0% | 44.0% | -0.3 | n/a | no target |
| P01T | 334 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 72.8% | 72.8% | +0.0 | 100% | ❌ 27 pts to go |
| P02 | 473 | 65.3% | 65.3% | -1.2 | 100% | ❌ 35 pts to go |
| P03 | 257 | 60.3% | 60.3% | -0.2 | n/a | no target |
| P04 | 3834 | 24.8% | 24.8% | -3.0 | 95% | ❌ 70 pts to go |
| P05 | 427 | 33.0% | 33.0% | +0.0 | 80% | ❌ 47 pts to go |
| P06M | 10275 | 47.9% | 47.9% | -2.2 | n/a | no target |
| P06T | 60046 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 313 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 841 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 26848 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 92.7% | 92.7% | +0.0 | 100% | 🟡 7 pts to go |
| P10R | 99167 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2750 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 11585 | 0.8% | 0.8% | -0.2 | n/a | no target |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18051 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 79.0% | 79.0% | +0.6 | n/a | no target |
| P01T | 334 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 51.7% | 51.7% | +0.1 | 85% | ❌ 33 pts to go |
| P02 | 473 | 56.7% | 56.7% | -0.9 | 90% | ❌ 33 pts to go |
| P03 | 257 | 44.0% | 44.0% | -0.1 | 85% | ❌ 41 pts to go |
| P04 | 3834 | 27.1% | 27.1% | -3.3 | 90% | ❌ 63 pts to go |
| P05 | 427 | 32.8% | 32.8% | +0.0 | 75% | ❌ 42 pts to go |
| P06M | 10275 | 90.4% | 90.4% | +0.0 | n/a | no target |
| P06T | 60046 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 313 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 841 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 26848 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 85.1% | 85.1% | +0.0 | 95% | 🟡 10 pts to go |
| P10R | 99167 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2750 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 11585 | 0.7% | 0.7% | -0.1 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18051 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 80.0% | 80.0% | +0.6 | n/a | no target |
| P01T | 334 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 51.8% | 51.8% | +0.0 | 85% | ❌ 33 pts to go |
| P02 | 473 | 51.8% | 51.8% | -0.9 | 90% | ❌ 38 pts to go |
| P03 | 257 | 45.1% | 45.1% | -0.2 | 85% | ❌ 40 pts to go |
| P04 | 3834 | 23.1% | 23.1% | -2.9 | 90% | ❌ 67 pts to go |
| P05 | 427 | 42.9% | 42.9% | +0.0 | 75% | ❌ 32 pts to go |
| P06M | 10275 | 84.4% | 84.4% | +0.7 | n/a | no target |
| P06T | 60046 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 313 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 841 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 26848 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 0.3% | 0.3% | +0.0 | 95% | ❌ 95 pts to go |
| P10R | 99167 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2750 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 11585 | 0.6% | 0.6% | -0.1 | n/a | no target |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 18051 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 86.0% | 86.0% | +0.4 | n/a | no target |
| P01T | 334 | 91.9% | 91.9% | -0.3 | n/a | no target |
| P01_GOLD | 625 | 85.4% | 85.4% | -0.1 | 100% | ❌ 15 pts to go |
| P02 | 473 | 74.4% | 74.4% | -1.3 | 100% | ❌ 26 pts to go |
| P03 | 257 | 91.8% | 91.8% | -0.4 | n/a | no target |
| P04 | 3834 | 45.8% | 45.8% | -5.7 | 95% | ❌ 49 pts to go |
| P05 | 427 | 77.8% | 77.8% | +0.0 | 95% | ❌ 17 pts to go |
| P06M | 10275 | 98.5% | 98.5% | +0.2 | n/a | no target |
| P06T | 60046 | 82.7% | 82.7% | -1.0 | n/a | no target |
| P06 | 313 | 24.3% | 24.3% | -1.9 | n/a | no target |
| P07 | 841 | 16.9% | 16.9% | -2.2 | n/a | no target |
| P08 | 26848 | 9.5% | 9.5% | -1.5 | n/a | no target |
| P09 | 303 | 98.7% | 98.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10R | 99167 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2750 | 70.4% | 70.4% | -1.3 | n/a | no target |
| P11 | 11585 | 13.2% | 13.2% | -2.9 | n/a | no target |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18051 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 86.0% | 86.0% | +0.4 | n/a | no target |
| P01T | 334 | 91.9% | 91.9% | -0.3 | n/a | no target |
| P01_GOLD | 625 | 88.6% | 88.6% | -0.1 | 100% | ❌ 11 pts to go |
| P02 | 473 | 75.5% | 75.7% | -1.3 | 100% | ❌ 24 pts to go |
| P03 | 257 | 92.6% | 92.6% | -0.4 | n/a | no target |
| P04 | 3834 | 49.0% | 49.0% | -6.1 | 95% | ❌ 46 pts to go |
| P05 | 427 | 90.2% | 90.2% | +0.0 | 70% | ✅ met |
| P06M | 10275 | 98.5% | 98.5% | +0.2 | n/a | no target |
| P06T | 60046 | 82.7% | 82.7% | -1.0 | n/a | no target |
| P06 | 313 | 24.3% | 24.3% | -1.9 | n/a | no target |
| P07 | 841 | 16.9% | 16.9% | -2.2 | n/a | no target |
| P08 | 26848 | 9.5% | 9.5% | -1.5 | n/a | no target |
| P09 | 303 | 98.7% | 98.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10R | 99167 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2750 | 70.4% | 70.4% | -1.3 | n/a | no target |
| P11 | 11585 | 13.2% | 13.2% | -2.9 | n/a | no target |
| P12 | 7 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18051 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 334 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 16.8% | 16.8% | +0.0 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 363 rows, 28.9% filled |
| P02 | 473 | 11.0% | 11.0% | -0.2 | n/a | no target · rows from a source that publishes bids: 290 rows, 17.9% filled |
| P03 | 257 | 13.2% | 13.2% | -0.1 | n/a | no target · rows from a source that publishes bids: 139 rows, 24.5% filled |
| P04 | 3834 | 1.4% | 1.4% | -0.2 | n/a | no target · rows from a source that publishes bids: 872 rows, 6.3% filled |
| P05 | 427 | 3.0% | 3.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 53 rows, 24.5% filled |
| P06M | 10275 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 60046 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 313 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 841 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 26848 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 3.0% | 3.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 290 rows, 3.1% filled |
| P10R | 99167 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P10 | 2750 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 11585 | 0.1% | 0.1% | +0.0 | n/a | no target · rows from a source that publishes bids: 87 rows, 12.6% filled |
| P12 | 7 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 7 rows, 0.0% filled |
| P13 | 18051 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 334 | 0.3% | 98.5% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 53.3% | 82.4% | +0.1 | 90% | ❌ 37 pts to go |
| P02 | 473 | 51.6% | 87.7% | -0.9 | 90% | ❌ 38 pts to go |
| P03 | 257 | 45.5% | 80.2% | -0.2 | 90% | ❌ 44 pts to go |
| P04 | 3834 | 18.6% | 94.1% | -2.3 | 90% | ❌ 71 pts to go |
| P05 | 427 | 0.0% | 82.9% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 10275 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 60046 | 0.0% | 99.9% | +0.0 | n/a | no target |
| P06 | 313 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 841 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 26848 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 303 | 2.3% | 4.0% | +0.0 | 90% | ❌ 88 pts to go |
| P10R | 99167 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2750 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 11585 | 0.5% | 99.6% | -0.1 | n/a | no target |
| P12 | 7 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18051 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 334 | 0.6% | 98.8% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 25.9% | 55.0% | +0.0 | 90% | ❌ 64 pts to go |
| P02 | 473 | 50.7% | 86.9% | -0.9 | n/a | no target |
| P03 | 257 | 24.9% | 59.5% | -0.1 | n/a | no target |
| P04 | 3834 | 20.4% | 95.9% | -2.5 | n/a | no target |
| P05 | 427 | 0.5% | 83.4% | +0.0 | n/a | no target |
| P06M | 10275 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 60046 | 0.1% | 99.9% | +0.0 | n/a | no target |
| P06 | 313 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 841 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 26848 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 303 | 41.9% | 43.6% | +0.0 | n/a | no target |
| P10R | 99167 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2750 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 11585 | 0.5% | 99.6% | -0.1 | n/a | no target |
| P12 | 7 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18051 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 334 | 1.5% | 99.7% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 51.8% | 81.0% | +0.0 | 95% | ❌ 43 pts to go |
| P02 | 473 | 55.6% | 91.8% | -1.0 | n/a | no target |
| P03 | 257 | 47.9% | 82.5% | -0.1 | n/a | no target |
| P04 | 3834 | 20.6% | 96.1% | -2.5 | n/a | no target |
| P05 | 427 | 4.7% | 87.6% | +0.0 | n/a | no target |
| P06M | 10275 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 60046 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 313 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 841 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 26848 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 303 | 64.0% | 65.7% | +0.0 | n/a | no target |
| P10R | 99167 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P10 | 2750 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 11585 | 0.5% | 99.6% | -0.1 | n/a | no target |
| P12 | 7 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 18051 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 334 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 473 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 257 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3834 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 427 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 10275 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 60046 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 313 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 841 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 26848 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 303 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 99167 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2750 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 11585 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 18051 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 334 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 473 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 257 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3834 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 427 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 10275 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 60046 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 313 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 841 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 26848 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 303 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 99167 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2750 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 11585 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 18051 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 100 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 334 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 473 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 257 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3834 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 427 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 10275 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 60046 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 313 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 841 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 26848 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 303 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 99167 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2750 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 11585 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 7 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 18051 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

