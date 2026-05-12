#!/bin/bash
kubectl get ingress $1 -n $2 -o jsonpath='{.status.loadBalancer.ingress[0].ip}' | wc -w