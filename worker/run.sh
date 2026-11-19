#!/usr/bin/env bash
# One worker pass, on the Oracle machine, every 10 minutes (started by /usr/local/bin/cch-pass after it has reset the
# checkout to origin/main). Starts the jobs of worker/jobs.json that are due, then publishes what they wrote.
set -uo pipefail
REPO=$(pwd)
DATA=/home/cch/data
mkdir -p "$DATA"
echo "== pass $(date -u +%FT%TZ) at $(git rev-parse --short HEAD)"
REQ=$(sha256sum worker/requirements.txt | cut -c1-12)
if [ ! -f "$DATA/venv/.req-$REQ" ]; then
  python3 -m venv "$DATA/venv" \
    && "$DATA/venv/bin/pip" install -q --upgrade pip \
    && "$DATA/venv/bin/pip" install -q -r worker/requirements.txt \
    && touch "$DATA/venv/.req-$REQ"
fi
"$DATA/venv/bin/python" worker/runner.py "$REPO" "$DATA"
"$DATA/venv/bin/python" worker/publish.py "$REPO" "$DATA"
