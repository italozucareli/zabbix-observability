#!/bin/bash
# Uso: ./zbx_snmp_ups_alarms_lld.sh <IP> <COMUNIDADE>
IP=$1
COMM=$2

# Faz o snmpwalk na upsAlarmDescr (1.3.6.1.2.1.33.1.6.2.1.2)
# Retorna algo como: SNMPv2-SMI::mib-2.33.1.6.2.1.2.1 = OID: SNMPv2-SMI::mib-2.33.1.6.3.3
ALARMS=$(snmpwalk -v2c -c "$COMM" "$IP" 1.3.6.1.2.1.33.1.6.2.1.2 2>/dev/null)

echo "{\"data\":["
FIRST=1

while IFS= read -r line; do
    if [ -n "$line" ]; then
        # Extrai apenas o último bloco numérico/texto que identifica o alarme
        ALARM_OID=$(echo "$line" | awk '{print $NF}')
        
        [ $FIRST -eq 0 ] && echo "," || FIRST=0
        echo -n "  {\"{#ALARM_TYPE}\": \"$ALARM_OID\"}"
    fi
done <<< "$ALARMS"

echo -e "\n]}"