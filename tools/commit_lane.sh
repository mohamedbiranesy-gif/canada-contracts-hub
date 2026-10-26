#!/usr/bin/env bash
# Kept for compatibility: the logic lives in tools/commit_lane.py (conflict-free, lane-restricted commits).
exec python3 "$(dirname "$0")/commit_lane.py" "$@"
