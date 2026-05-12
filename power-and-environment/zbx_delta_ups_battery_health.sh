#!/bin/bash
IP=$1
COMM=$2
# deltaUpsBatteryReplaceIndicator (1=ok, 2=replace)
REPLACE=$(snmpget -v2c -c "$COMM" -Oqv "$IP" 1.3.6.1.4.1.2254.2.4.7.4.0 2>/dev/null)
echo "{\"delta_battery_replace\": ${REPLACE:-0}}"