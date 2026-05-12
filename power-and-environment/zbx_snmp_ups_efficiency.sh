#!/bin/bash
IP=$1
COMM=$2
# MIB genérica para eficiência se suportada (upsAdvInputLineFailCause / eficiência)
# Calculado no Zabbix através de (True Power / Apparent Power) ou lido diretamente.
EFF=$(snmpget -v2c -c "$COMM" -Oqv "$IP" 1.3.6.1.4.1.318.1.1.1.4.3.4.0 2>/dev/null)
echo "{\"efficiency_percent\": $EFF}"