#!/bin/bash
# Requer execução no Manager
# Pega todos os serviços, busca as tasks e filtra pelas que estão presas em 'Pending'

SERVICES=$(docker service ls -q 2>/dev/null)

if [ -z "$SERVICES" ]; then
    echo "0"
    exit 0
fi

PENDING_COUNT=$(docker service ps $SERVICES -f "desired-state=running" -f "state=pending" -q 2>/dev/null | wc -l)

echo "${PENDING_COUNT:-0}"