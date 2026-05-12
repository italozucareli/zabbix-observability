#!/bin/bash
# Retorna a contagem de nós com falha de comunicação
docker node ls --format '{{.Status}}' 2>/dev/null | grep -icE "Down|Unreachable" || echo 0