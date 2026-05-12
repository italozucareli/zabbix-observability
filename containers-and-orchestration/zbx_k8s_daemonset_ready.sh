#!/bin/bash
kubectl get ds $1 -n $2 -o jsonpath='{.status.numberReady}'