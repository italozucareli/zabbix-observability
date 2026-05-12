#!/bin/bash
# Requer kubectl configurado para o usuário Zabbix
kubectl get nodes --no-headers | grep "Ready" | grep -v "NotReady" | wc -l