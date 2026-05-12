#!/bin/bash
IP=$1
COMM=$2
AMP=$(snmpget -v2c -c "$COMM" -Oqv "$IP" 1.3.6.1.2.1.33.1.4.4.1.3.1 2>/dev/null)
echo "{\"output_current_amps\": $(awk "BEGIN {print $AMP/10}")}"