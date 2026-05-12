#!/bin/bash
IP=$1
COMM=$2
DATE_STR=$(snmpget -v2c -c "$COMM" -Oqv "$IP" 1.3.6.1.4.1.318.1.1.1.7.2.4.0 2>/dev/null | tr -d '"')
echo "{\"last_test_date\": \"$DATE_STR\"}"