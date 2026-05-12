#!/bin/bash
# Retorna 1 se o nó for o Leader, 0 caso contrário
LEADER=$(docker node inspect self --format '{{if .ManagerStatus}}{{.ManagerStatus.Leader}}{{else}}false{{end}}' 2>/dev/null)
if [[ "$LEADER" == "true" ]]; then
    echo 1
else
    echo 0
fi