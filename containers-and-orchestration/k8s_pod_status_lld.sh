#!/bin/bash
NAMESPACE=${1:-default}
kubectl get pods -n "$NAMESPACE" -o json | jq '{data: [ .items[] | { "{#POD_NAME}": .metadata.name, "{#NAMESPACE}": .metadata.namespace, "phase": .status.phase, "restarts": .status.containerStatuses[0].restartCount } ] }'