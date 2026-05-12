#!/bin/bash
# Uso: ./stp_topology_change.sh <IP_SWITCH> <COMUNIDADE_SNMP>
# Retorna o contador de dot1dStpTopChanges
snmpget -v2c -c "$2" "$1" 1.3.6.1.2.1.17.2.3.0 | awk '{print $NF}'