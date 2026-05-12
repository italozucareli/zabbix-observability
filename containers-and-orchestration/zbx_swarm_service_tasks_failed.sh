#!/bin/bash
# Uso: ./zbx_swarm_service_tasks_failed.sh <FULL_SERVICE_NAME>
# Requer Zabbix Agent no nó Manager no grupo 'docker'
SERVICE_NAME=$1

if [ -z "$SERVICE_NAME" ]; then
    echo "0"
    exit 1
fi

# Conta quantas tasks (containers) deste serviço possuem o status "Failed" no histórico atual do Swarm
FAILED_COUNT=$(docker service ps "$SERVICE_NAME" --filter "desired-state=shutdown" --format '{{.Error}}' 2>/dev/null | grep -v "^$" | wc -l)

echo "${FAILED_COUNT:-0}"