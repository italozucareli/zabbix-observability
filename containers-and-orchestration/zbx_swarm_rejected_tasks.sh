#!/bin/bash
# Requer execução no Manager

SERVICES=$(docker service ls -q 2>/dev/null)

if [ -z "$SERVICES" ]; then
    echo "0"
    exit 0
fi

REJECTED_COUNT=$(docker service ps $SERVICES -f "state=rejected" -q 2>/dev/null | wc -l)

echo "${REJECTED_COUNT:-0}"