#!/bin/bash
IP=$1
COMM=$2
BYPASS_VOLT=$(snmpget -v2c -c "$COMM" -Oqv "$IP" 1.3.6.1.2.1.33.1.5.3.1.2.1 2>/dev/null)
echo "{\"bypass_voltage\": $BYPASS_VOLT}"