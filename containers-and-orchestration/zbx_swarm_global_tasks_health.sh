#!/bin/bash
# Conta serviços globais onde Réplicas Rodando != Réplicas Desejadas
FAILS=$(docker service ls --filter "mode=global" --format "{{.Replicas}}" 2>/dev/null | awk -F'/' '$1!=$2 {count++} END {print count+0}')
echo "$FAILS"