#!/bin/bash
IP=$1
COMM=$2
BANKS=$(snmpwalk -v2c -c "$COMM" "$IP" 1.3.6.1.4.1.318.1.1.26.8.3.1.3 2>/dev/null)
echo "{\"data\":["
FIRST=1
while IFS= read -r line; do
    if [ -n "$line" ]; then
        IDX=$(echo "$line" | grep -oP '(?<=\.8\.3\.1\.3\.)\d+')
        [ $FIRST -eq 0 ] && echo "," || FIRST=0
        echo -n "  {\"{#BANK_INDEX}\": \"$IDX\"}"
    fi
done <<< "$BANKS"
echo -e "\n]}"