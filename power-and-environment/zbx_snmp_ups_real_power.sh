#!/bin/bash
IP=$1
COMM=$2
WATTS=$(snmpget -v2c -c "$COMM" -Oqv "$IP" 1.3.6.1.2.1.33.1.4.4.1.4.1 2>/dev/null)
echo "{\"real_power_watts\": $WATTS}"