#!/bin/bash
# APC PowerNet-MIB Environmental Probes
IP=$1
COMM=$2

# empmProbeName: 1.3.6.1.4.1.318.1.1.10.4.2.3.1.3
PROBES=$(snmpwalk -v2c -c "$COMM" "$IP" 1.3.6.1.4.1.318.1.1.10.4.2.3.1.3 2>/dev/null)

echo "{\"data\":["
FIRST=1

while IFS= read -r line; do
    if [ -n "$line" ]; then
        INDEX=$(echo "$line" | grep -oP '(?<=\.1\.3\.)\d+')
        NAME=$(echo "$line" | awk -F'STRING: ' '{print $2}' | tr -d '"')
        
        [ $FIRST -eq 0 ] && echo "," || FIRST=0
        echo -n "  {\"{#PROBE_INDEX}\": \"$INDEX\", \"{#PROBE_NAME}\": \"$NAME\"}"
    fi
done <<< "$PROBES"

echo -e "\n]}"