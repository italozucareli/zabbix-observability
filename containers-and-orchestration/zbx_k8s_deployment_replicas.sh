#!/bin/bash
DESIRED=$(kubectl get deployment $1 -n $2 -o jsonpath='{.spec.replicas}')
READY=$(kubectl get deployment $1 -n $2 -o jsonpath='{.status.readyReplicas}')
echo | awk -v d="$DESIRED" -v r="${READY:-0}" 'd>0 {printf "%.0f", (r/d)*100} d==0 {print 0}'