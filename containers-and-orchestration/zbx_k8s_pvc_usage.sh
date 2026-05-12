#!/bin/bash
kubectl exec $1 -n $2 -- df -h /mnt/data | awk 'NR==2 {print $5}' | sed 's/%//'