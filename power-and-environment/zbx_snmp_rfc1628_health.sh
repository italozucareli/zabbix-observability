#!/bin/bash
# Uso: ./zbx_snmp_rfc1628_health.sh <IP> <COMUNIDADE>
IP=$1
COMM=$2

# OIDs Universais (RFC 1628 - UPS MIB)
# upsBatteryStatus (1=unknown, 2=batteryNormal, 3=batteryLow, 4=batteryDepleted)
# upsEstimatedMinutesRemaining
# upsEstimatedChargeRemaining

OUTPUT=$(snmpget -v2c -c "$COMM" -Oqv "$IP" \
    1.3.6.1.2.1.33.1.2.1.0 \
    1.3.6.1.2.1.33.1.2.3.0 \
    1.3.6.1.2.1.33.1.2.4.0 2>/dev/null)

if [ -z "$OUTPUT" ]; then
    echo "{\"error\": \"Timeout ou falha SNMP\"}"
    exit 1
fi

# Extrai os valores lendo linha por linha
STATUS=$(echo "$OUTPUT" | sed -n '1p')
MINUTES=$(echo "$OUTPUT" | sed -n '2p')
CHARGE=$(echo "$OUTPUT" | sed -n '3p')

cat <<EOF
{
  "battery_status_code": $STATUS,
  "minutes_remaining": $MINUTES,
  "charge_percent": $CHARGE
}
EOF