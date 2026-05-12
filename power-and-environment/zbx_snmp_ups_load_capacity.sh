#!/bin/bash
IP=$1
COMM=$2
LOAD=$(snmpget -v2c -c "$COMM" -Oqv "$IP" 1.3.6.1.2.1.33.1.4.4.1.5.1 2>/dev/null)
echo "{\"load_percent\": $LOAD}"