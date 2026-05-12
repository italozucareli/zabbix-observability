#!/bin/bash
IP=$1
COMM=$2
# atsConfigPhaseSync e atsConfigSelectedSource
SYNC=$(snmpget -v2c -c "$COMM" -Oqv "$IP" 1.3.6.1.4.1.318.1.1.8.5.1.1.0 2>/dev/null)
SRC=$(snmpget -v2c -c "$COMM" -Oqv "$IP" 1.3.6.1.4.1.318.1.1.8.5.1.2.0 2>/dev/null)
echo "{\"is_synchronized\": $SYNC, \"active_source\": $SRC}"