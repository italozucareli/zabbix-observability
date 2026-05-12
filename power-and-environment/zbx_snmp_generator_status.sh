#!/bin/bash
IP=$1
COMM=$2
# Exemplo focado no status de Input Source genérico (1=other, 2=none, 3=primaryUtility, 4=bypassUtility, 5=cable, 6=generator)
GEN=$(snmpget -v2c -c "$COMM" -Oqv "$IP" 1.3.6.1.2.1.33.1.3.3.1.1.1 2>/dev/null)
echo "{\"input_source_type\": $GEN}"