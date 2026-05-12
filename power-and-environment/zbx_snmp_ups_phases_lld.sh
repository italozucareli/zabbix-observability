#!/bin/bash
# Uso: ./zbx_snmp_ups_phases_lld.sh <IP> <COMUNIDADE>
IP=$1
COMM=$2

# upsOutputPhaseTable: 1.3.6.1.2.1.33.1.4.4.1.1
PHASES=$(snmpwalk -v2c -c "$COMM" "$IP" 1.3.6.1.2.1.33.1.4.4.1.1 2>/dev/null)

echo "{\"data\":["
FIRST=1

while IFS= read -r line; do
    if [ -n "$line" ]; then
        # Extrai o índice da fase (geralmente 1, 2, 3)
        PHASE_ID=$(echo "$line" | awk -F'.' '{print $NF}' | awk '{print $1}')
        
        [ $FIRST -eq 0 ] && echo "," || FIRST=0
        echo -n "  {\"{#PHASE_ID}\": \"$PHASE_ID\", \"{#PHASE_NAME}\": \"Phase $PHASE_ID\"}"
    fi
done <<< "$PHASES"

echo -e "\n]}"