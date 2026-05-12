#!/bin/bash
kubectl get pod $1 -n $2 -o jsonpath='{.status.containerStatuses[*].restartCount}' | awk '{s+=$1} END {print s}'