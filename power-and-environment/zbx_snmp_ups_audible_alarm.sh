#!/bin/bash
IP=$1
COMM=$2
# upsAlarmsPresent e upsAudibleStatus
BEEP=$(snmpget -v2c -c "$COMM" -Oqv "$IP" 1.3.6.1.2.1.33.1.6.1.0 2>/dev/null)
echo "{\"active_alarms_count\": $BEEP}"