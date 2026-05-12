#!/bin/bash
IP=$1
COMM=$2

# RFC 1628 ext: upsOutputEnergy (kWh) ou APC/Eaton MIBs dependendo do modelo. 
# Exemplo genérico APC:
KWH=$(snmpget -v2c -c "$COMM" -Oqv "$IP" 1.3.6.1.4.1.318.1.1.1.4.3.6.0 2>/dev/null)

if [ -n "$KWH" ]; then
    echo "{\"total_kwh\": $KWH}"
else
    echo "{\"error\": \"Metrica de kWh nao suportada pelo hardware\"}"
fi