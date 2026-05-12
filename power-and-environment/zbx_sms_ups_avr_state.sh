#!/bin/bash
IP=$1
COMM=$2

# OID proprietário SMS/Alerta24h para status de regulagem
# 1=Normal, 2=Boost (Elevando), 3=Buck (Reduzindo)
AVR_STATE=$(snmpget -v2c -c "$COMM" -Oqv "$IP" 1.3.6.1.4.1.18042.1.1.2.2.0 2>/dev/null)

if [ -n "$AVR_STATE" ]; then
    echo "{\"avr_status\": $AVR_STATE}"
else
    echo "{\"error\": \"Nobreak não suporta MIB SMS/Legrand\"}"
fi