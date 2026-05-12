#!/bin/bash
FILE="/var/log/apcupsd.events"
CRITICAL=$(tail -n 20 "$FILE" | grep -ic "Power failure\|Battery low\|Shutdown")
echo "{\"recent_critical_events\": $CRITICAL}"