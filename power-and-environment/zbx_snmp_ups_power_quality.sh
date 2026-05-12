#!/bin/bash
IP=$1
COMM=$2

# Coleta em lote: Voltagem In, Freq In, Voltagem Out, Freq Out (RFC 1628)
OUTPUT=$(snmpget -v2c -c "$COMM" -Oqv "$IP" \
    1.3.6.1.2.1.33.1.3.3.1.3.1 \
    1.3.6.1.2.1.33.1.3.3.1.2.1 \
    1.3.6.1.2.1.33.1.4.4.1.2.1 \
    1.3.6.1.2.1.33.1.4.4.1.3.1 2>/dev/null)

if [ -z "$OUTPUT" ]; then
    echo "{\"error\": \"Timeout SNMP\"}"
    exit 1
fi

VIN=$(echo "$OUTPUT" | sed -n '1p')
FIN=$(echo "$OUTPUT" | sed -n '2p')
VOUT=$(echo "$OUTPUT" | sed -n '3p')
FOUT=$(echo "$OUTPUT" | sed -n '4p')

# A RFC 1628 retorna frequencia em deciHertz (ex: 600 = 60.0Hz). Tratamento:
cat <<EOF
{
  "input_voltage": $VIN,
  "input_frequency": $(awk "BEGIN {print $FIN/10}"),
  "output_voltage": $VOUT,
  "output_frequency": $(awk "BEGIN {print $FOUT/10}")
}
EOF