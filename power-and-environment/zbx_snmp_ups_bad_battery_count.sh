#!/bin/bash
IP=$1
COMM=$2
# MIB APC: upsAdvBatteryNumOfBadBatts
BAD=$(snmpget -v2c -c "$COMM" -Oqv "$IP" 1.3.6.1.4.1.318.1.1.1.2.2.6.0 2>/dev/null)
if [ -n "$BAD" ]; then echo "{\"bad_battery_packs\": $BAD}"; else echo "{\"error\": \"Timeout\"}"; fi