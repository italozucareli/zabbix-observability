#!/bin/bash
# Uso: APC/Schneider PDU (PowerNet-MIB)
IP=$1
COMM=$2

# sPDUOutletName: 1.3.6.1.4.1.318.1.1.4.4.2.1.4
OUTLETS=$(snmpwalk -v2c -c "$COMM" "$IP" 1.3.6.1.4.1.318.1.1.4.4.2.1.4 2>/dev/null)

echo "{\"data\":["
FIRST=1

while IFS= read -r line; do
    if [ -n "$line" ]; then
        INDEX=$(echo "$line" | grep -oP '(?<=\.1\.4\.)\d+')
        NAME=$(echo "$line" | awk -F'STRING: ' '{print $2}' | tr -d '"')
        
        [ $FIRST -eq 0 ] && echo "," || FIRST=0
        echo -n "  {\"{#OUTLET_INDEX}\": \"$INDEX\", \"{#OUTLET_NAME}\": \"$NAME\"}"
    fi
done <<< "$OUTLETS"

echo -e "\n]}"