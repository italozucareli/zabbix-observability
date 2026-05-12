#!/bin/bash
IP=$1
COMM=$2
CURRENT=$(snmpget -v2c -c "$COMM" -Oqv "$IP" 1.3.6.1.2.1.33.1.2.6.0 2>/dev/null)
if [ -n "$CURRENT" ]; then echo "{\"battery_current\": $(awk "BEGIN {print $CURRENT/10}")}"; else echo "{\"error\": \"Timeout\"}"; fi