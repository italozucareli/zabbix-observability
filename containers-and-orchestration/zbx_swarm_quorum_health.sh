#!/bin/bash
TOTAL=$(docker node ls --filter "role=manager" -q 2>/dev/null | wc -l)
REACHABLE=$(docker node ls --filter "role=manager" --format '{{.ManagerStatus}}' 2>/dev/null | grep -icE "Reachable|Leader")

cat <<EOF
{
  "total_managers": ${TOTAL:-0},
  "reachable_managers": ${REACHABLE:-0}
}
EOF