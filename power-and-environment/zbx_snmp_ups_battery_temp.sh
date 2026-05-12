#!/bin/bash
IP=$1
COMM=$2
TEMP=$(snmpget -v2c -c "$COMM" -Oqv "$IP" 1.3.6.1.2.1.33.1.2.7.0 2>/dev/null)
if [ -n "$TEMP" ]; then echo "{\"battery_temp_celsius\": $TEMP}"; else echo "{\"error\": \"Timeout\"}"; fi