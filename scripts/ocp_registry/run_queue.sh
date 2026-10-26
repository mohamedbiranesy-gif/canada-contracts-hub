#!/bin/bash
# usage: run_queue.sh <queue_file>   (lines: source_key pub_id name)
q=$1
while read -r sk pid nm; do
  [ -z "$sk" ] && continue
  scripts/ocp_registry/stream_one.sh "$sk" "$pid" "$nm"
done < "$q"
echo "$(date -u +%FT%TZ) QUEUE DONE $q" >> downloads/ocp_registry/queues.log
