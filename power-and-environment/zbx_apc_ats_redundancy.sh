#!/bin/bash
IP=$1
COMM=$2
# atsStatusRedundancyState (1=fullyRedundant, 2=redundancyLost)
RED=$(snmpget -v2c -c "$COMM" -Oqv "$IP" 1.3.6.1.4.1.318.1.1.8.5.1.13.0 2>/dev/null)
echo "{\"redundancy_state\": $RED}"