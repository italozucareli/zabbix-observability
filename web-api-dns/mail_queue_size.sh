#!/bin/bash
# Retorna o número de mensagens na fila.
postqueue -p | tail -n 1 | awk '/Requests/ {print $5}' | sed 's/[^0-9]//g'