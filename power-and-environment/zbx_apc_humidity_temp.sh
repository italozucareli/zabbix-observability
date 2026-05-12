#!/bin/bash
IP=$1
COMM=$2
TEMP=$(snmpget -v2c -c "$COMM" -Oqv "$IP" 1.3.6.1.4.1.318.1.1.10.2.3.2.1.4.1 2>/dev/null)
HUMID=$(snmpget -v2c -c "$COMM" -Oqv "$IP" 1.3.6.1.4.1.318.1.1.10.2.3.2.1.6.1 2>/dev/null)
echo "{\"temperature_c\": $TEMP, \"humidity_percent\": $HUMID}"