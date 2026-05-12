#!/bin/bash
# Uso: ./check_disk_inodes.sh <PONTO_DE_MONTAGEM> (ex: /var)
MOUNT=$1
df -i "$MOUNT" | awk 'NR==2 {print $5}' | sed 's/%//'