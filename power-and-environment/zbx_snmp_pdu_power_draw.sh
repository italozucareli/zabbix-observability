#!/bin/bash
IP=$1
COMM=$2
# PDU Total Load
LOAD=$(snmpget -v2c -c "$COMM" -Oqv "$IP" 1.3.6.1.4.1.318.1.1.12.2.3.1.1.2.1 2>/dev/null)
echo "{\"pdu_total_amps\": $(awk "BEGIN {print $LOAD/10}")}"