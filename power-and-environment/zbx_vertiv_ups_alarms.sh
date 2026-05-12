#!/bin/bash
IP=$1
COMM=$2
# lgpConditionTable
CONDITIONS=$(snmpget -v2c -c "$COMM" -Oqv "$IP" 1.3.6.1.4.1.476.1.42.3.2.0 2>/dev/null)
echo "{\"vertiv_active_conditions\": ${CONDITIONS:-0}}"