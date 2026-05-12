#!/bin/bash
# Uso: ./raid_array_status.sh /dev/md0 (Retorna 1 se OK, 0 se degradado)
STATUS=$(mdadm --detail $1 | grep "State :" | grep -c "clean\|active")
echo $STATUS