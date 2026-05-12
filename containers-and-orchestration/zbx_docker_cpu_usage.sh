#!/bin/bash
# Uso: ./script.sh <nome_container>
docker stats --no-stream --format "{{.CPUPerc}}" $1 | sed 's/%//'