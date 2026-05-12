#!/bin/bash
IP=$1
COMM=$2

# xupsBypassStatus e xupsInverterStatus
OUTPUT=$(snmpget -v2c -c "$COMM" -Oqv "$IP" \
    1.3.6.1.4.1.534.1.4.1.0 \
    1.3.6.1.4.1.534.1.5.1.0 2>/dev/null)

if [ -z "$OUTPUT" ]; then
    echo "{\"error\": \"Falha de comunicacao com XUPS\"}"
    exit 1
fi

BYPASS=$(echo "$OUTPUT" | sed -n '1p')
INVERTER=$(echo "$OUTPUT" | sed -n '2p')

cat <<EOF
{
  "bypass_status": $BYPASS,
  "inverter_status": $INVERTER
}
EOF