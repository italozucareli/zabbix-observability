#!/bin/bash
IP=$1
COMM=$2

# upsTestResultsSummary (RFC 1628)
RESULT=$(snmpget -v2c -c "$COMM" -Oqv "$IP" 1.3.6.1.2.1.33.1.7.3.0 2>/dev/null)

if [ -n "$RESULT" ]; then
    echo "{\"last_selftest_status\": $RESULT}"
else
    echo "{\"error\": \"Sem suporte a self-test\"}"
fi