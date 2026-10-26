# ca_new_brunswick — New Brunswick (BLOCKED: hosts not reachable through the session proxy)

Checked 2026-10-25 17:19 UTC. `https://nbon.gnb.ca/` (New Brunswick Opportunities Network, which carries "Contract awards") and `https://data.gnb.ca/` (GNB open data CKAN) both fail at the egress proxy with `CONNECT tunnel failed, response 502` (`connect_rejected` in the agent-proxy status log: host not allowed for this session). `https://www.gnb.ca/` and `https://www2.gnb.ca/` are reachable but hold no award data. Not retried beyond two attempts each. GNB awards also appear on MERX (`srcSystem` NB) — covered by the parallel `ca_merx` worker.

Result: 0 records from this source key.
