#!/usr/bin/env python3
"""Decide whether a PR is data-only (auto-mergeable). Reads changed paths on stdin, one per line.
Prints 'automerge' or 'needs-review: <paths>'. Exit 0 always."""
import json, sys
allowed = json.load(open("coord/config.json"))["automerge_paths"]
paths = [l.strip() for l in sys.stdin if l.strip()]
bad = [p for p in paths if not any(p == a or p.startswith(a) for a in allowed)]
print("automerge" if paths and not bad else "needs-review: " + " ".join(bad[:20]))
