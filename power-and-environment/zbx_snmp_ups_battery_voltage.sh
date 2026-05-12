#!/bin/bash
IP=$1
COMM=$2
VOLTAGE=$(snmpget -v2c -c "$COMM" -Oqv "$IP" 1.3.6.1.2.1.33.1.2.5.0 2>/dev/null)
if [ -n "$VOLTAGE" ]; then echo "{\"battery_voltage\": $(awk "BEGIN {print $VOLTAGE/10}")}"; else echo "{\"error\": \"Timeout\"}"; fi