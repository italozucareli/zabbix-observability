#!/bin/bash
kubectl describe node $1 | grep -A 2 "Allocated resources:" | grep "cpu" | awk '{print $2}' | sed 's/%//'