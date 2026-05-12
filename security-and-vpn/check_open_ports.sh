#!/bin/bash
# Uso: ./check_open_ports.sh 80
# Retorna 1 se estiver ouvindo, 0 se não estiver
ss -tuln | grep -q ":$1 " && echo 1 || echo 0